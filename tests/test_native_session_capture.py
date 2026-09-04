from __future__ import annotations

import hashlib
import json
import os
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPOSITORY = Path(__file__).resolve().parents[1]
CAPTURE_HELPER = REPOSITORY / "migration-kit" / "capture-native-session.py"


class NativeSessionCaptureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.repo = self.root / "target"
        self.repo.mkdir()
        (self.repo / ".relay").mkdir()
        (self.repo / ".relay" / "START.md").write_text("# Start\n", encoding="utf-8")
        (self.repo / ".relay" / "STATE.md").write_text("# State\n", encoding="utf-8")
        (self.repo / ".gitignore").write_text(
            "**/.relay/private/\n", encoding="utf-8"
        )
        subprocess.run(
            ["git", "init", "-q", str(self.repo)], check=True, capture_output=True
        )
        self.environment = os.environ.copy()
        for name in (
            "CLAUDE_CODE_SESSION_ID",
            "CLAUDE_CONFIG_DIR",
            "CODEX_THREAD_ID",
            "CODEX_SESSION_ID",
            "CODEX_HOME",
        ):
            self.environment.pop(name, None)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def run_capture(
        self, harness: str, migration_id: str = "2026-09-05-test", **environment: str
    ) -> tuple[subprocess.CompletedProcess[str], dict]:
        invocation_environment = self.environment | environment
        completed = subprocess.run(
            [
                sys.executable,
                str(CAPTURE_HELPER),
                "--harness",
                harness,
                "--migration-id",
                migration_id,
                "--repo-root",
                str(self.repo),
            ],
            check=False,
            text=True,
            capture_output=True,
            env=invocation_environment,
        )
        output = json.loads(completed.stdout)
        return completed, output

    def snapshot(self, harness: str, identity: str) -> Path:
        return (
            self.repo
            / ".relay"
            / "private"
            / "migrations"
            / "2026-09-05-test"
            / "native-sessions"
            / harness
            / identity
        )

    def assert_digest(self, path: Path, expected: str) -> None:
        self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), expected)

    def test_claude_copies_only_exact_session_and_preserves_source(self) -> None:
        config = self.root / "claude"
        project = config / "projects" / "project-a"
        project.mkdir(parents=True)
        session_id = "session-exact"
        source = project / f"{session_id}.jsonl"
        source_bytes = b'not parsed\x00{"sentinel":"exact"}\n'
        source.write_bytes(source_bytes)
        decoy = project / "session-newer.jsonl"
        decoy.write_bytes(b"newer-decoy")
        os.utime(decoy, (source.stat().st_mtime + 60, source.stat().st_mtime + 60))
        source_stat = source.stat()

        completed, output = self.run_capture(
            "claude-code",
            CLAUDE_CONFIG_DIR=str(config),
            CLAUDE_CODE_SESSION_ID=session_id,
        )

        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertEqual(output["capture_result"], "captured")
        self.assertNotIn(str(self.root), completed.stdout)
        transcript = self.snapshot("claude-code", session_id) / "transcript.jsonl"
        self.assertEqual(transcript.read_bytes(), source_bytes)
        self.assertEqual(source.read_bytes(), source_bytes)
        self.assertEqual(source.stat().st_mtime_ns, source_stat.st_mtime_ns)
        self.assertNotIn(b"newer-decoy", transcript.read_bytes())
        self.assert_digest(transcript, output["primary_sha256"])

    def test_claude_missing_exact_session_never_uses_newest(self) -> None:
        config = self.root / "claude"
        project = config / "projects" / "project-a"
        project.mkdir(parents=True)
        (project / "some-other-session.jsonl").write_bytes(b"do-not-copy")

        completed, output = self.run_capture(
            "claude-code",
            CLAUDE_CONFIG_DIR=str(config),
            CLAUDE_CODE_SESSION_ID="missing-session",
        )

        self.assertEqual(completed.returncode, 0)
        self.assertEqual(output["capture_result"], "unavailable")
        self.assertEqual(output["captured_file_count"], 0)
        self.assertFalse(self.snapshot("claude-code", "missing-session").exists())
        self.assertIn("no newest-file fallback", " ".join(output["limitations"]))

    def test_claude_captures_only_exact_companion_regular_files(self) -> None:
        config = self.root / "claude"
        project = config / "projects" / "project-a"
        project.mkdir(parents=True)
        session_id = "session-with-artifacts"
        (project / f"{session_id}.jsonl").write_bytes(b"primary")
        companion = project / session_id
        (companion / "tool-results").mkdir(parents=True)
        (companion / "subagents").mkdir()
        (companion / "tool-results" / "result.bin").write_bytes(b"tool-result")
        (companion / "subagents" / "agent.jsonl").write_bytes(b"subagent")
        unrelated = project / "different-session"
        unrelated.mkdir()
        (unrelated / "secret.txt").write_bytes(b"outside-session")

        completed, output = self.run_capture(
            "claude-code",
            CLAUDE_CONFIG_DIR=str(config),
            CLAUDE_CODE_SESSION_ID=session_id,
        )

        self.assertEqual(completed.returncode, 0)
        self.assertEqual(output["capture_result"], "captured")
        snapshot = self.snapshot("claude-code", session_id)
        self.assertEqual(
            (snapshot / "artifacts" / "tool-results" / "result.bin").read_bytes(),
            b"tool-result",
        )
        self.assertEqual(
            (snapshot / "artifacts" / "subagents" / "agent.jsonl").read_bytes(),
            b"subagent",
        )
        self.assertFalse((snapshot / "artifacts" / "secret.txt").exists())
        manifest = json.loads((snapshot / "manifest.json").read_text())
        self.assertEqual(manifest["captured_file_count"], 3)
        self.assertFalse(manifest["canonical"])
        self.assertFalse(manifest["runtime_required"])
        self.assertFalse(manifest["closed_session"])
        self.assertRegex(
            manifest["captured_through_watermark"], r"^\d{4}-\d{2}-\d{2}T"
        )
        for entry in manifest["captured_files"]:
            self.assert_digest(snapshot / entry["snapshot_relative_path"], entry["sha256"])
        self.assert_digest(snapshot / "manifest.json", output["manifest_sha256"])

    def test_claude_skips_symlinked_companion_artifact(self) -> None:
        if not hasattr(os, "symlink"):
            self.skipTest("symlinks unavailable")
        config = self.root / "claude"
        project = config / "projects" / "project-a"
        project.mkdir(parents=True)
        session_id = "session-symlink"
        (project / f"{session_id}.jsonl").write_bytes(b"primary")
        companion = project / session_id
        companion.mkdir()
        outside = self.root / "outside-secret"
        outside.write_bytes(b"must-not-copy")
        (companion / "escape").symlink_to(outside)

        completed, output = self.run_capture(
            "claude-code",
            CLAUDE_CONFIG_DIR=str(config),
            CLAUDE_CODE_SESSION_ID=session_id,
        )

        self.assertEqual(completed.returncode, 0)
        self.assertEqual(output["capture_result"], "partial")
        snapshot = self.snapshot("claude-code", session_id)
        self.assertFalse((snapshot / "artifacts" / "escape").exists())
        self.assertNotIn(b"must-not-copy", (snapshot / "transcript.jsonl").read_bytes())

    def test_claude_ambiguous_exact_matches_do_not_choose_by_mtime(self) -> None:
        config = self.root / "claude"
        session_id = "duplicate-id"
        for project_name, value in (("one", b"one"), ("two", b"two")):
            project = config / "projects" / project_name
            project.mkdir(parents=True)
            (project / f"{session_id}.jsonl").write_bytes(value)

        completed, output = self.run_capture(
            "claude-code",
            CLAUDE_CONFIG_DIR=str(config),
            CLAUDE_CODE_SESSION_ID=session_id,
        )

        self.assertEqual(completed.returncode, 0)
        self.assertEqual(output["capture_result"], "unavailable")
        self.assertFalse(self.snapshot("claude-code", session_id).exists())
        self.assertIn("ambiguous", " ".join(output["limitations"]))

    def test_codex_custom_home_copies_only_exact_thread_rollout(self) -> None:
        codex_home = self.root / "custom-codex"
        day = codex_home / "sessions" / "2026" / "09" / "05"
        day.mkdir(parents=True)
        thread_id = "thread-exact"
        exact = day / f"rollout-2026-09-05T00-00-00-{thread_id}.jsonl"
        exact.write_bytes(b"exact-thread")
        (day / "rollout-2026-09-05T00-00-01-thread-other.jsonl").write_bytes(
            b"other-thread"
        )
        (day / f"rollout-2026-09-05T00-00-02-other-{thread_id}.jsonl").write_bytes(
            b"suffix-decoy"
        )

        completed, output = self.run_capture(
            "codex", CODEX_HOME=str(codex_home), CODEX_THREAD_ID=thread_id
        )

        self.assertEqual(completed.returncode, 0)
        self.assertEqual(output["capture_result"], "captured")
        self.assertEqual(output["identity_source"], "CODEX_THREAD_ID")
        self.assertNotIn("exact-thread", completed.stdout)
        self.assertNotIn(str(self.root), completed.stdout)
        transcript = self.snapshot("codex", thread_id) / "transcript.jsonl"
        self.assertEqual(transcript.read_bytes(), b"exact-thread")
        self.assert_digest(transcript, output["primary_sha256"])

    def test_codex_thread_id_does_not_fall_back_to_session_id(self) -> None:
        codex_home = self.root / "codex"
        day = codex_home / "sessions" / "2026" / "09" / "05"
        day.mkdir(parents=True)
        (day / "rollout-2026-09-05T00-00-00-session-fallback.jsonl").write_bytes(
            b"wrong-session"
        )

        completed, output = self.run_capture(
            "codex",
            CODEX_HOME=str(codex_home),
            CODEX_THREAD_ID="missing-thread",
            CODEX_SESSION_ID="session-fallback",
        )

        self.assertEqual(completed.returncode, 0)
        self.assertEqual(output["capture_result"], "unavailable")
        self.assertEqual(output["identity_source"], "CODEX_THREAD_ID")
        self.assertFalse(self.snapshot("codex", "missing-thread").exists())

    def test_codex_ambiguous_exact_rollouts_are_unavailable(self) -> None:
        codex_home = self.root / "codex"
        thread_id = "duplicate-thread"
        for day_name in ("04", "05"):
            day = codex_home / "sessions" / "2026" / "09" / day_name
            day.mkdir(parents=True)
            (day / f"rollout-2026-09-{day_name}T12-00-00-{thread_id}.jsonl").write_bytes(
                day_name.encode("ascii")
            )

        completed, output = self.run_capture(
            "codex", CODEX_HOME=str(codex_home), CODEX_THREAD_ID=thread_id
        )

        self.assertEqual(completed.returncode, 0)
        self.assertEqual(output["capture_result"], "unavailable")
        self.assertIn("ambiguous", " ".join(output["limitations"]))
        self.assertFalse(self.snapshot("codex", thread_id).exists())

    def test_codex_session_id_is_used_only_when_thread_id_is_absent(self) -> None:
        codex_home = self.root / "codex"
        day = codex_home / "sessions" / "2026" / "09" / "05"
        day.mkdir(parents=True)
        session_id = "session-only"
        (day / f"rollout-2026-09-05T00-00-00-{session_id}.jsonl").write_bytes(
            b"fallback-allowed"
        )

        completed, output = self.run_capture(
            "codex", CODEX_HOME=str(codex_home), CODEX_SESSION_ID=session_id
        )

        self.assertEqual(completed.returncode, 0)
        self.assertEqual(output["capture_result"], "captured")
        self.assertEqual(output["identity_source"], "CODEX_SESSION_ID")
        self.assertEqual(
            (self.snapshot("codex", session_id) / "transcript.jsonl").read_bytes(),
            b"fallback-allowed",
        )

    def test_missing_native_identity_is_recorded_without_guessing(self) -> None:
        codex_home = self.root / "codex"
        sessions = codex_home / "sessions"
        sessions.mkdir(parents=True)
        (sessions / "rollout-2026-09-05T00-00-00-some-thread.jsonl").write_bytes(
            b"do-not-guess"
        )

        completed, output = self.run_capture("codex", CODEX_HOME=str(codex_home))

        self.assertEqual(completed.returncode, 0)
        self.assertEqual(output["capture_result"], "unavailable")
        self.assertIsNone(output["native_session_id"])
        self.assertEqual(output["captured_file_count"], 0)
        self.assertFalse(self.snapshot("codex", "unidentified").exists())
        self.assertNotIn("do-not-guess", completed.stdout)

    def test_empty_config_environment_uses_documented_home_fallback(self) -> None:
        fallback_home = self.root / "home"
        codex_sessions = fallback_home / ".codex" / "sessions"
        codex_sessions.mkdir(parents=True)
        (codex_sessions / "rollout-2026-09-05T00-00-00-empty-home.jsonl").write_bytes(
            b"codex"
        )
        codex_completed, codex_output = self.run_capture(
            "codex",
            migration_id="codex-empty-env",
            HOME=str(fallback_home),
            CODEX_HOME="",
            CODEX_THREAD_ID="empty-home",
        )
        self.assertEqual(codex_completed.returncode, 0)
        self.assertEqual(codex_output["capture_result"], "captured")
        self.assertEqual(codex_output["safe_source_search_boundary"], "${HOME}/.codex/sessions")

        claude_project = fallback_home / ".claude" / "projects" / "project"
        claude_project.mkdir(parents=True)
        (claude_project / "empty-config.jsonl").write_bytes(b"claude")
        claude_completed, claude_output = self.run_capture(
            "claude-code",
            migration_id="claude-empty-env",
            HOME=str(fallback_home),
            CLAUDE_CONFIG_DIR="",
            CLAUDE_CODE_SESSION_ID="empty-config",
        )
        self.assertEqual(claude_completed.returncode, 0)
        self.assertEqual(claude_output["capture_result"], "captured")
        self.assertEqual(
            claude_output["safe_source_search_boundary"],
            "${HOME}/.claude/projects",
        )

    def test_refresh_replaces_same_snapshot_and_failed_refresh_preserves_it(self) -> None:
        codex_home = self.root / "codex"
        sessions = codex_home / "sessions"
        sessions.mkdir(parents=True)
        thread_id = "refresh-thread"
        source = sessions / f"rollout-2026-09-05T00-00-00-{thread_id}.jsonl"
        source.write_bytes(b"first")
        first_completed, first = self.run_capture(
            "codex", CODEX_HOME=str(codex_home), CODEX_THREAD_ID=thread_id
        )
        self.assertEqual(first_completed.returncode, 0)
        snapshot = self.snapshot("codex", thread_id)
        self.assertEqual((snapshot / "transcript.jsonl").read_bytes(), b"first")

        source.write_bytes(b"second")
        second_completed, second = self.run_capture(
            "codex", CODEX_HOME=str(codex_home), CODEX_THREAD_ID=thread_id
        )
        self.assertEqual(second_completed.returncode, 0)
        self.assertEqual(second["capture_result"], "captured")
        self.assertEqual((snapshot / "transcript.jsonl").read_bytes(), b"second")
        provider = snapshot.parent
        self.assertEqual(
            sorted(path.name for path in provider.iterdir()),
            [thread_id, f"{thread_id}.last-attempt.json"],
        )

        source.unlink()
        failed_completed, failed = self.run_capture(
            "codex", CODEX_HOME=str(codex_home), CODEX_THREAD_ID=thread_id
        )
        self.assertEqual(failed_completed.returncode, 0)
        self.assertEqual(failed["capture_result"], "unavailable")
        self.assertTrue(failed["previous_snapshot_preserved"])
        self.assertEqual((snapshot / "transcript.jsonl").read_bytes(), b"second")
        self.assertEqual(
            sorted(path.name for path in provider.iterdir()),
            [thread_id, f"{thread_id}.last-attempt.json"],
        )

    def test_private_destination_is_ignored_untracked_and_not_runtime_required(self) -> None:
        codex_home = self.root / "codex"
        sessions = codex_home / "sessions"
        sessions.mkdir(parents=True)
        thread_id = "private-thread"
        (sessions / f"rollout-2026-09-05T00-00-00-{thread_id}.jsonl").write_bytes(
            b"private"
        )

        completed, output = self.run_capture(
            "codex", CODEX_HOME=str(codex_home), CODEX_THREAD_ID=thread_id
        )
        self.assertEqual(completed.returncode, 0)
        snapshot = self.snapshot("codex", thread_id)
        ignored = subprocess.run(
            ["git", "-C", str(self.repo), "check-ignore", "--quiet", str(snapshot)],
            check=False,
        )
        self.assertEqual(ignored.returncode, 0)
        tracked = subprocess.run(
            ["git", "-C", str(self.repo), "ls-files", "--", ".relay/private"],
            check=True,
            text=True,
            capture_output=True,
        )
        self.assertEqual(tracked.stdout, "")
        transcript_mode = stat.S_IMODE((snapshot / "transcript.jsonl").stat().st_mode)
        self.assertEqual(transcript_mode, 0o600)
        private = self.repo / ".relay" / "private"
        for path in private.rglob("*"):
            if path.is_file() or path.is_symlink():
                path.unlink()
        for path in sorted(private.rglob("*"), reverse=True):
            if path.is_dir():
                path.rmdir()
        private.rmdir()
        bootstrap = self.root / "bootstrap-without-private"
        shutil.copytree(REPOSITORY / "template", bootstrap)
        required = (
            "AGENTS.md",
            "CLAUDE.md",
            ".relay/START.md",
            ".relay/STATE.md",
            ".relay/DECISIONS.md",
            ".relay/RECORDS.md",
            ".relay/PROCEDURES.md",
        )
        self.assertTrue(all((bootstrap / path).is_file() for path in required))
        self.assertFalse((bootstrap / ".relay" / "private").exists())
        adapter_text = (bootstrap / "AGENTS.md").read_text()
        self.assertIn(".relay/START.md", adapter_text)
        self.assertIn(".relay/STATE.md", adapter_text)
        self.assertNotIn(".relay/private", adapter_text)
        self.assertFalse(output["runtime_required"])
        self.assertFalse(output["canonical"])

    def test_unsafe_identity_and_unignored_destination_are_refused(self) -> None:
        codex_home = self.root / "codex"
        (codex_home / "sessions").mkdir(parents=True)
        unsafe, unsafe_output = self.run_capture(
            "codex", CODEX_HOME=str(codex_home), CODEX_THREAD_ID="../escape"
        )
        self.assertEqual(unsafe.returncode, 2)
        self.assertEqual(unsafe_output["capture_result"], "inaccessible")
        self.assertFalse((self.repo / ".relay" / "private").exists())

        (self.repo / ".gitignore").write_text("", encoding="utf-8")
        refused, refused_output = self.run_capture(
            "codex", CODEX_HOME=str(codex_home), CODEX_THREAD_ID="safe-id"
        )
        self.assertEqual(refused.returncode, 2)
        self.assertIn("not Git-ignored", refused_output["error"])

    def test_negated_real_private_output_path_is_refused(self) -> None:
        (self.repo / ".gitignore").write_text(
            ".relay/private/**\n"
            "!.relay/private/**/\n"
            "!.relay/private/migrations/2026-09-05-test/native-sessions/"
            "codex/safe-id.last-attempt.json\n",
            encoding="utf-8",
        )
        codex_home = self.root / "codex"
        sessions = codex_home / "sessions"
        sessions.mkdir(parents=True)
        (sessions / "rollout-2026-09-05T00-00-00-safe-id.jsonl").write_bytes(
            b"must-stay-private"
        )

        completed, output = self.run_capture(
            "codex", CODEX_HOME=str(codex_home), CODEX_THREAD_ID="safe-id"
        )

        self.assertEqual(completed.returncode, 2)
        self.assertIn("not Git-ignored", output["error"])
        self.assertFalse((self.repo / ".relay" / "private").exists())


if __name__ == "__main__":
    unittest.main()
