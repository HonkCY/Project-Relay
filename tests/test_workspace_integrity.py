"""Test fixture mechanics; native semantic compliance needs separate agent runs."""

from __future__ import annotations

import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from workspace_integrity_fixtures import (
    CASES, CONTINUE_PROMPT, OWNER_PROMPT, PROMPT, REPOSITORY, STATE, build_fixture, git,
)


def fixture_definition_lines(path: Path, stable_id: str) -> list[int]:
    """Test oracle for fixture Markdown only; exclude fenced example headings."""
    lines = []
    fenced = False
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.startswith("```"):
            fenced = not fenced
        elif not fenced and re.match(rf"^## {re.escape(stable_id)}(?:\s|$)", line):
            lines.append(number)
    return lines


class WorkspaceIntegrityFixtureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="relay-integrity-")
        self.root = Path(self.temporary.name)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def fixture(self, case: str = "normal") -> Path:
        target = self.root / case
        build_fixture(target, case)
        return target

    def test_builder_preserves_candidate_bootstrap_and_requires_new_destination(self) -> None:
        target = self.fixture()
        for path in ("AGENTS.md", "CLAUDE.md", ".relay/START.md", ".gitignore"):
            self.assertEqual((target / path).read_bytes(), (REPOSITORY / "template" / path).read_bytes())
        before = (target / ".relay/STATE.md").read_bytes()
        with self.assertRaises(FileExistsError):
            build_fixture(target, "empty-state")
        self.assertEqual((target / ".relay/STATE.md").read_bytes(), before)

    def test_successful_readback_contains_intended_bytes_and_dirty_checkpoint(self) -> None:
        target = self.fixture()
        owner = target / ".relay/STATE.md"
        intended = owner.read_bytes().replace(b"fixture-ready", b"checkpoint-ready")
        owner.write_bytes(intended)
        self.assertEqual(owner.read_bytes(), intended)
        self.assertEqual(git(target, "status", "--porcelain=v1"), "M .relay/STATE.md")
        self.assertIn("fixture-ready", git(target, "show", "HEAD:.relay/STATE.md"))

    def test_success_message_does_not_mask_reverted_save(self) -> None:
        target = self.fixture("readback-failure")
        owner = target / ".relay/STATE.md"
        before = owner.read_bytes()
        result = subprocess.run([sys.executable, ".fixture/save.py"], cwd=target, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("successfully", result.stdout)
        self.assertEqual(owner.read_bytes(), before)
        self.assertNotIn(b"**Frontier:** checkpoint-ready", owner.read_bytes())

    def test_empty_state_and_truncated_tail_are_distinct_from_explicit_unknown(self) -> None:
        empty = (self.fixture("empty-state") / ".relay/STATE.md").read_bytes()
        tail = (self.fixture("truncated-state") / ".relay/STATE.md").read_text()
        valid = (self.fixture() / ".relay/STATE.md").read_text()
        self.assertEqual(empty, b"")
        self.assertIn("# Current state", tail)
        self.assertIn("**Frontier:**", tail)
        self.assertNotIn("## Background execution", tail)
        self.assertIn("## Background execution\n\nUnknown;", valid)
        self.assertNotEqual(tail, valid)

    def test_paginated_file_read_reconstructs_all_bytes_before_tail_assessment(self) -> None:
        path = self.fixture() / ".relay/STATE.md"
        pages = []
        with path.open("rb") as source:
            while page := source.read(61):
                pages.append(page)
        self.assertGreater(len(pages), 1)
        self.assertNotIn(b"## Background execution", pages[0])
        self.assertEqual(b"".join(pages), STATE.encode("utf-8"))
        self.assertIn(b"## Background execution\n\nUnknown;", b"".join(pages))

    def test_requested_owner_excludes_unrelated_workspaces_evidence_and_code_examples(self) -> None:
        target = self.fixture()
        owner = target / ".relay/RECORDS.md"
        other = target / "examples/other/.relay"
        evidence = target / ".relay/evidence/historical"
        for directory in (other, evidence):
            directory.mkdir(parents=True)
            (directory / "RECORDS.md").write_text("## R-001 — Unrelated definition\n")
        with owner.open("a") as stream:
            stream.write("\n```markdown\n## R-001 — Illustrative heading\n```\n")
        self.assertEqual(len(fixture_definition_lines(owner, "R-001")), 1)
        self.assertEqual(len(fixture_definition_lines(other / "RECORDS.md", "R-001")), 1)
        self.assertEqual(len(fixture_definition_lines(evidence / "RECORDS.md", "R-001")), 1)

    def test_duplicate_requested_owner_is_ambiguous_even_in_one_file(self) -> None:
        target = self.fixture("duplicate-id")
        path = target / ".relay/RECORDS.md"
        self.assertEqual(len(fixture_definition_lines(path, "R-001")), 2)
        records = path.read_text().split("## R-001 — Workspace copy")[1:]
        self.assertEqual(len(records), 2)
        for record in records:
            self.assertIn("**Authority:** accepted", record)
            self.assertIn("**Supersedes / superseded by:** none", record)
            self.assertIn("**Accepted by/at:** synthetic fixture owner / 2026-09-12", record)
            self.assertIn("**Provenance:** human-report", record)
            self.assertIn("**Verification:** unverified", record)
        self.assertIn("**Role:** canonical", records[0])
        self.assertIn("writer: current fixture operator", records[0])
        self.assertIn("**Role:** cache", records[1])
        self.assertIn("writers: none", records[1])

    def test_conflict_copy_is_untracked_unignored_and_keeps_conflicting_bytes(self) -> None:
        target = self.fixture("conflict-copy")
        relative = ".relay/RECORDS (conflicted copy).md"
        result = subprocess.run(["git", "-C", str(target), "check-ignore", relative], capture_output=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn(relative, git(target, "status", "--porcelain=v1"))
        self.assertEqual(git(target, "ls-files", "--", relative), "")
        self.assertIn("**Role:** cache", (target / relative).read_text())
        self.assertIn("**Role:** canonical", (target / ".relay/RECORDS.md").read_text())

    def test_partial_replica_exposes_link_whose_named_owner_has_not_arrived(self) -> None:
        target = self.fixture("partial-replica")
        self.assertIn("[R-002](RECORDS.md#r-002--new-resource)", (target / ".relay/STATE.md").read_text())
        self.assertEqual(fixture_definition_lines(target / ".relay/RECORDS.md", "R-002"), [])
        self.assertEqual(len(fixture_definition_lines(target / ".relay/RECORDS.md", "R-001")), 1)

    def test_mirror_contains_task_relevant_role_and_explicit_writer_restriction(self) -> None:
        target = self.fixture("mirror")
        self.assertIn("[R-001]", (target / ".relay/STATE.md").read_text())
        self.assertIn("**Role:** cache", (target / ".relay/RECORDS.md").read_text())
        self.assertIn("writers: none", (target / ".relay/RECORDS.md").read_text())
        self.assertIn("no writer authorization", (target / ".relay/DECISIONS.md").read_text())
        self.assertIn("Proceed only in the authorized canonical copy", (target / ".relay/PROCEDURES.md").read_text())
        self.assertEqual(git(target, "status", "--porcelain=v1"), "")

    def test_git_transport_carries_named_commit_but_not_dirty_local_checkpoint(self) -> None:
        source = self.fixture()
        destination = self.root / "transferred"
        base = git(source, "rev-parse", "HEAD")
        owner = source / ".relay/STATE.md"
        dirty = owner.read_bytes().replace(b"fixture-ready", b"checkpoint-ready")
        owner.write_bytes(dirty)
        git(self.root, "clone", "--quiet", "--no-local", str(source), str(destination))
        self.assertEqual(git(destination, "rev-parse", "HEAD"), base)
        self.assertIn(b"fixture-ready", (destination / ".relay/STATE.md").read_bytes())
        self.assertEqual(owner.read_bytes(), dirty)
        self.assertNotEqual(git(source, "status", "--porcelain=v1"), "")
        git(source, "add", ".relay/STATE.md")
        git(source, "commit", "-qm", "test: checkpoint before explicit writer transfer")
        reviewed_commit = git(source, "rev-parse", "HEAD")
        git(destination, "fetch", "--quiet", "origin")
        git(destination, "merge", "--ff-only", reviewed_commit)
        self.assertEqual(git(destination, "rev-parse", "HEAD"), reviewed_commit)
        self.assertEqual((destination / ".relay/STATE.md").read_bytes(), dirty)
        self.assertEqual(git(source, "rev-parse", "HEAD^{tree}"), git(destination, "rev-parse", "HEAD^{tree}"))
        git(destination, "fsck", "--full")

    def test_private_material_absence_does_not_remove_bootstrap_owners(self) -> None:
        target = self.fixture()
        self.assertFalse((target / ".relay/private").exists())
        self.assertTrue((target / ".relay/START.md").read_bytes())
        self.assertEqual((target / ".relay/STATE.md").read_text(), STATE)
        self.assertEqual(len(fixture_definition_lines(target / ".relay/RECORDS.md", "R-001")), 1)

    def test_all_cases_report_mechanics_only_and_no_native_semantic_pass(self) -> None:
        for case in CASES:
            result = build_fixture(self.root / case, case)
            self.assertEqual(result["native_semantic_result"], "not-run")
            self.assertRegex(result["base_commit"], r"^[0-9a-f]{40,64}$")
            if case == "duplicate-id":
                self.assertEqual(result["prompt"], OWNER_PROMPT)
            elif case in ("mirror", "readback-failure", "partial-replica"):
                self.assertEqual(result["prompt"], CONTINUE_PROMPT)
            else:
                self.assertEqual(result["prompt"], PROMPT)


if __name__ == "__main__":
    unittest.main()
