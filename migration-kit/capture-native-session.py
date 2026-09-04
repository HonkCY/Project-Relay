#!/usr/bin/env python3
"""Capture one exact native-agent session as private Relay forensic evidence.

The helper never parses transcript content. It writes only below the target
repository's ignored .relay/private/ tree and emits metadata suitable for review
before recording safe provenance in a tracked migration dossier.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import stat
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable


TOOL_VERSION = "1"
SAFE_COMPONENT = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,254}$")
CODEX_ROLLOUT_NAME = re.compile(
    r"^rollout-\d{4}-\d{2}-\d{2}T\d{2}-\d{2}-\d{2}-(?P<thread_id>.+)\.jsonl$"
)
LIVE_BOUNDARY_NOTICE = (
    "The native session was live at capture time. Events written after the "
    "captured-through watermark, including later tool results or final messages, "
    "are not included; this is not a final closed-session transcript."
)


class CaptureError(Exception):
    """A handled capture failure or safety refusal."""


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace(
        "+00:00", "Z"
    )


def validate_component(value: str, label: str) -> str:
    if not SAFE_COMPONENT.fullmatch(value):
        raise CaptureError(f"{label} must be one safe path component")
    return value


def json_bytes(value: dict[str, Any]) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True) + "\n").encode("utf-8")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def write_private_file(path: Path, value: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    flags = os.O_WRONLY | os.O_CREAT | os.O_TRUNC
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    fd = os.open(path, flags, 0o600)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(value)
    except Exception:
        try:
            os.close(fd)
        except OSError:
            pass
        raise
    os.chmod(path, 0o600)


def write_private_json_atomic(path: Path, value: dict[str, Any]) -> None:
    temporary = path.with_name(f".{path.name}.tmp")
    if temporary.exists() or temporary.is_symlink():
        if temporary.is_symlink() or not temporary.is_file():
            raise CaptureError(f"unsafe existing temporary path: {temporary.name}")
        temporary.unlink()
    write_private_file(temporary, json_bytes(value))
    os.replace(temporary, path)


def path_is_within(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def reject_symlink_components(path: Path, root: Path) -> None:
    try:
        relative = path.relative_to(root)
    except ValueError as error:
        raise CaptureError("destination escapes repository root") from error
    current = root
    for part in relative.parts:
        current = current / part
        if current.is_symlink():
            raise CaptureError(
                f"destination component is a symlink: {current.relative_to(root)}"
            )


def run_git(repo: Path, arguments: list[str]) -> subprocess.CompletedProcess[bytes]:
    try:
        return subprocess.run(
            ["git", "-C", str(repo), *arguments],
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except OSError as error:
        raise CaptureError(f"could not run Git safety check: {error}") from error


def validate_private_destination(repo: Path, private_paths: list[Path]) -> None:
    top_level = run_git(repo, ["rev-parse", "--show-toplevel"])
    if top_level.returncode != 0:
        raise CaptureError("repo root is not inside a Git worktree")
    actual_root = Path(os.fsdecode(top_level.stdout).strip()).resolve()
    if actual_root != repo:
        raise CaptureError("--repo-root must be the Git worktree root")
    tracked = run_git(repo, ["ls-files", "-z", "--", ".relay/private"])
    if tracked.returncode != 0:
        raise CaptureError("could not check whether .relay/private is tracked")
    if tracked.stdout:
        raise CaptureError("refusing capture: .relay/private contains tracked paths")
    private_root = run_git(repo, ["check-ignore", "--quiet", "--", ".relay/private/"])
    if private_root.returncode != 0:
        raise CaptureError("refusing capture: .relay/private/ is not Git-ignored")
    for private_path in private_paths:
        ignored = run_git(
            repo, ["check-ignore", "--quiet", "--", private_path.as_posix()]
        )
        if ignored.returncode != 0:
            raise CaptureError(
                f"refusing capture: {private_path.as_posix()} is not Git-ignored"
            )


def configured_surface(harness: str) -> dict[str, Any]:
    home = Path(os.environ.get("HOME", str(Path.home()))).expanduser()
    if harness == "claude-code":
        identity_source = "CLAUDE_CODE_SESSION_ID"
        identity = os.environ.get(identity_source, "")
        claude_config = os.environ.get("CLAUDE_CONFIG_DIR")
        if claude_config:
            config_root = Path(claude_config).expanduser()
            safe_root = "${CLAUDE_CONFIG_DIR}/projects"
        else:
            config_root = home / ".claude"
            safe_root = "${HOME}/.claude/projects"
        source_root = config_root / "projects"
    else:
        if os.environ.get("CODEX_THREAD_ID"):
            identity_source = "CODEX_THREAD_ID"
            identity = os.environ[identity_source]
        else:
            identity_source = "CODEX_SESSION_ID"
            identity = os.environ.get(identity_source, "")
        codex_home = os.environ.get("CODEX_HOME")
        if codex_home:
            codex_root = Path(codex_home).expanduser()
            safe_root = "${CODEX_HOME}/sessions"
        else:
            codex_root = home / ".codex"
            safe_root = "${HOME}/.codex/sessions"
        source_root = codex_root / "sessions"
    return {
        "identity": identity,
        "identity_source": identity_source,
        "source_root": source_root,
        "safe_root": safe_root,
    }


def discover_exact_matches(
    source_root: Path, matcher: Callable[[str], bool]
) -> tuple[list[Path], list[str], list[str]]:
    matches: list[Path] = []
    errors: list[str] = []
    pruned_symlinks: list[str] = []

    def onerror(error: OSError) -> None:
        errors.append(f"{type(error).__name__}: {error.filename or source_root}")

    for current, directories, files in os.walk(
        source_root, topdown=True, onerror=onerror, followlinks=False
    ):
        current_path = Path(current)
        kept_directories: list[str] = []
        for name in sorted(directories):
            candidate = current_path / name
            try:
                if candidate.is_symlink():
                    pruned_symlinks.append(str(candidate))
                else:
                    kept_directories.append(name)
            except OSError as error:
                errors.append(f"{type(error).__name__}: {candidate}")
        directories[:] = kept_directories
        for name in sorted(files):
            if not matcher(name):
                continue
            candidate = current_path / name
            try:
                mode = candidate.lstat().st_mode
            except OSError as error:
                errors.append(f"{type(error).__name__}: {candidate}")
                continue
            if stat.S_ISREG(mode):
                matches.append(candidate)
            else:
                errors.append(f"exact match is not a regular file: {candidate}")
    return sorted(matches), errors, pruned_symlinks


def safe_source_locator(source: Path, source_root: Path, safe_root: str) -> str:
    # Native project-directory names can themselves encode private home/project
    # paths. The exact absolute source path is retained only in the manifest.
    return f"{safe_root}/**/{source.name}"


def copy_regular_file(source: Path, destination: Path) -> tuple[dict[str, Any], bool]:
    source_lstat = source.lstat()
    if not stat.S_ISREG(source_lstat.st_mode) or source.is_symlink():
        raise CaptureError(f"source is not a regular non-symlink file: {source}")

    source_flags = os.O_RDONLY
    if hasattr(os, "O_NOFOLLOW"):
        source_flags |= os.O_NOFOLLOW
    source_fd = os.open(source, source_flags)
    digest = hashlib.sha256()
    copied = 0
    try:
        before = os.fstat(source_fd)
        if not stat.S_ISREG(before.st_mode):
            raise CaptureError(f"source changed away from a regular file: {source}")
        if (before.st_dev, before.st_ino) != (
            source_lstat.st_dev,
            source_lstat.st_ino,
        ):
            raise CaptureError(f"source changed during safe open: {source}")
        expected = before.st_size
        destination.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
        destination_flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
        if hasattr(os, "O_NOFOLLOW"):
            destination_flags |= os.O_NOFOLLOW
        destination_fd = os.open(destination, destination_flags, 0o600)
        try:
            with os.fdopen(destination_fd, "wb") as target:
                remaining = expected
                while remaining:
                    chunk = os.read(source_fd, min(1024 * 1024, remaining))
                    if not chunk:
                        raise CaptureError(
                            f"source became shorter during capture: {source}"
                        )
                    target.write(chunk)
                    digest.update(chunk)
                    copied += len(chunk)
                    remaining -= len(chunk)
        except Exception:
            try:
                os.close(destination_fd)
            except OSError:
                pass
            destination.unlink(missing_ok=True)
            raise
        os.chmod(destination, 0o600)
        after = os.fstat(source_fd)
    finally:
        os.close(source_fd)

    changed = any(
        (
            before.st_size != after.st_size,
            before.st_mtime_ns != after.st_mtime_ns,
            before.st_dev != after.st_dev,
            before.st_ino != after.st_ino,
        )
    )
    return (
        {
            "bytes": copied,
            "sha256": digest.hexdigest(),
            "source_size_at_open": before.st_size,
            "source_mtime_ns_at_open": before.st_mtime_ns,
            "source_size_after_copy": after.st_size,
            "source_mtime_ns_after_copy": after.st_mtime_ns,
        },
        changed,
    )


def collect_companion_files(companion: Path) -> tuple[list[Path], list[dict[str, str]]]:
    files: list[Path] = []
    skipped: list[dict[str, str]] = []

    def onerror(error: OSError) -> None:
        skipped.append(
            {
                "path": str(error.filename or companion),
                "reason": f"unreadable directory: {type(error).__name__}",
            }
        )

    for current, directories, names in os.walk(
        companion, topdown=True, onerror=onerror, followlinks=False
    ):
        current_path = Path(current)
        kept_directories: list[str] = []
        for name in sorted(directories):
            candidate = current_path / name
            try:
                if candidate.is_symlink():
                    skipped.append({"path": str(candidate), "reason": "symlink"})
                else:
                    kept_directories.append(name)
            except OSError as error:
                skipped.append(
                    {
                        "path": str(candidate),
                        "reason": f"lstat failed: {type(error).__name__}",
                    }
                )
        directories[:] = kept_directories
        for name in sorted(names):
            candidate = current_path / name
            try:
                mode = candidate.lstat().st_mode
            except OSError as error:
                skipped.append(
                    {
                        "path": str(candidate),
                        "reason": f"lstat failed: {type(error).__name__}",
                    }
                )
                continue
            if stat.S_ISREG(mode) and not candidate.is_symlink():
                files.append(candidate)
            else:
                skipped.append(
                    {"path": str(candidate), "reason": "symlink or special file"}
                )
    return sorted(files), skipped


def remove_private_tree(path: Path) -> None:
    if not path.exists() and not path.is_symlink():
        return
    if path.is_symlink() or not path.is_dir():
        raise CaptureError(f"unsafe private refresh path: {path.name}")
    shutil.rmtree(path)


def prepare_refresh_paths(provider_dir: Path, key: str) -> tuple[Path, Path, Path]:
    target = provider_dir / key
    staging = provider_dir / f".{key}.staging"
    previous = provider_dir / f".{key}.previous"
    if target.is_symlink() or staging.is_symlink() or previous.is_symlink():
        raise CaptureError("refusing refresh through a symlink")
    if previous.exists():
        if target.exists():
            remove_private_tree(previous)
        else:
            os.replace(previous, target)
    if staging.exists():
        remove_private_tree(staging)
    staging.mkdir(mode=0o700)
    return target, staging, previous


def install_refresh(target: Path, staging: Path, previous: Path) -> None:
    moved_previous = False
    try:
        if target.exists():
            os.replace(target, previous)
            moved_previous = True
        os.replace(staging, target)
        if moved_previous:
            remove_private_tree(previous)
    except Exception:
        if not target.exists() and moved_previous and previous.exists():
            os.replace(previous, target)
        raise


def previous_snapshot_metadata(target: Path, repo: Path) -> dict[str, Any] | None:
    manifest_path = target / "manifest.json"
    if not manifest_path.is_file() or manifest_path.is_symlink():
        return None
    value = manifest_path.read_bytes()
    try:
        manifest = json.loads(value)
    except (OSError, json.JSONDecodeError):
        return None
    return {
        "private_snapshot_locator": target.relative_to(repo).as_posix(),
        "captured_through_watermark": manifest.get("captured_through_watermark"),
        "capture_result": manifest.get("capture_result"),
        "manifest_sha256": sha256_bytes(value),
        "primary_sha256": (manifest.get("primary_transcript") or {}).get("sha256"),
    }


def make_attempt_base(
    migration_id: str,
    harness: str,
    identity_source: str,
    identity: str,
    configured_source_root: Path,
    resolved_source_root: Path,
    safe_root: str,
    target: Path,
    repo: Path,
    watermark: str,
) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "tool": "Project Relay native-session forensic capture",
        "tool_version": TOOL_VERSION,
        "migration_id": migration_id,
        "harness": harness,
        "identity_source": identity_source,
        "native_session_id": identity or None,
        "configured_source_root": str(configured_source_root),
        "resolved_source_root": str(resolved_source_root),
        "safe_source_search_boundary": safe_root,
        "private_snapshot_locator": target.relative_to(repo).as_posix(),
        "capture_started_at": watermark,
        "captured_through_watermark": watermark,
        "closed_session": False,
        "canonical": False,
        "runtime_required": False,
        "boundary_notice": LIVE_BOUNDARY_NOTICE,
    }


def capture(args: argparse.Namespace) -> dict[str, Any]:
    migration_id = validate_component(args.migration_id, "migration ID")
    repo = Path(args.repo_root).expanduser().resolve()
    if not (repo / ".relay").is_dir() or (repo / ".relay").is_symlink():
        raise CaptureError("repo root must contain a non-symlink .relay directory")

    provider_relative = (
        Path(".relay")
        / "private"
        / "migrations"
        / migration_id
        / "native-sessions"
        / args.harness
    )
    provider_dir = repo / provider_relative
    reject_symlink_components(provider_dir, repo)

    surface = configured_surface(args.harness)
    identity = surface["identity"]
    identity_source = surface["identity_source"]
    configured_source_root = surface["source_root"]
    source_root = configured_source_root.resolve(strict=False)
    safe_root = surface["safe_root"]
    if identity:
        validate_component(identity, f"{identity_source} value")
        target_key = identity
    else:
        target_key = "unidentified"
    target = provider_dir / target_key
    last_attempt = provider_dir / f"{target_key}.last-attempt.json"
    validate_private_destination(
        repo,
        [
            provider_relative / target_key / "transcript.jsonl",
            provider_relative / target_key / "manifest.json",
            provider_relative / f"{target_key}.last-attempt.json",
            provider_relative / f".{target_key}.staging" / ".probe",
            provider_relative / f".{target_key}.previous" / ".probe",
        ],
    )
    private_root = (repo / ".relay" / "private").resolve(strict=False)
    if path_is_within(source_root, private_root) or path_is_within(
        provider_dir.resolve(strict=False), source_root
    ):
        raise CaptureError(
            "configured native source root overlaps the private snapshot destination"
        )
    provider_dir.mkdir(parents=True, exist_ok=True, mode=0o700)
    os.chmod(provider_dir, 0o700)
    watermark = utc_now()
    attempt = make_attempt_base(
        migration_id,
        args.harness,
        identity_source,
        identity,
        configured_source_root,
        source_root,
        safe_root,
        target,
        repo,
        watermark,
    )

    result = "unavailable"
    limitations: list[str] = []
    source_match: Path | None = None
    discovery_errors: list[str] = []
    pruned_symlinks: list[str] = []

    if not identity:
        limitations.append(f"{identity_source} is missing or empty; no session was guessed")
    elif not source_root.exists():
        limitations.append(f"configured native session root does not exist: {safe_root}")
    elif not source_root.is_dir():
        result = "inaccessible"
        limitations.append(f"configured native session root is not a directory: {safe_root}")
    else:
        if args.harness == "claude-code":
            matcher = lambda name: name == f"{identity}.jsonl"
        else:
            matcher = lambda name: bool(
                (match := CODEX_ROLLOUT_NAME.fullmatch(name))
                and match.group("thread_id") == identity
            )
        matches, discovery_errors, pruned_symlinks = discover_exact_matches(
            source_root, matcher
        )
        if discovery_errors:
            result = "inaccessible"
            limitations.append(
                "exact-session discovery encountered inaccessible or unsafe entries; "
                "no transcript was selected"
            )
        elif len(matches) == 0:
            limitations.append(
                f"no exact transcript matched {identity_source}={identity}; "
                "no newest-file fallback was used"
            )
            if pruned_symlinks:
                limitations.append("nested symlink directories were not followed")
        elif len(matches) > 1:
            limitations.append(
                f"{len(matches)} exact transcript paths matched the native ID; "
                "the result is ambiguous and no file was selected"
            )
        else:
            source_match = matches[0]

    if source_match is not None:
        target, staging, previous = prepare_refresh_paths(provider_dir, target_key)
        captured_files: list[dict[str, Any]] = []
        skipped_entries: list[dict[str, str]] = []
        partial_reasons: list[str] = []
        primary_destination = staging / "transcript.jsonl"
        try:
            primary_metadata, primary_changed = copy_regular_file(
                source_match, primary_destination
            )
        except (OSError, CaptureError) as error:
            remove_private_tree(staging)
            result = "inaccessible"
            limitations.append(
                "exact transcript could not be copied safely; details remain in "
                "the private last-attempt record"
            )
            attempt["private_capture_error"] = str(error)
        else:
            primary_entry = {
                "source_path": str(source_match),
                "safe_source_locator": safe_source_locator(
                    source_match, source_root, safe_root
                ),
                "snapshot_relative_path": "transcript.jsonl",
                **primary_metadata,
            }
            captured_files.append(primary_entry)
            if primary_changed:
                partial_reasons.append("primary transcript changed during capture")

            companion: Path | None = None
            if args.harness == "claude-code":
                companion = source_match.with_suffix("")
                if companion.is_symlink():
                    partial_reasons.append(
                        "the exact companion session directory is a symlink and was skipped"
                    )
                    companion = None
                elif companion.exists() and not companion.is_dir():
                    partial_reasons.append(
                        "the exact companion session path is not a directory and was skipped"
                    )
                    companion = None
            if companion is not None and companion.is_dir():
                companion_files, skipped_entries = collect_companion_files(companion)
                if skipped_entries:
                    partial_reasons.append(
                        f"{len(skipped_entries)} companion entries were skipped safely"
                    )
                for source_file in companion_files:
                    relative = source_file.relative_to(companion)
                    destination = staging / "artifacts" / relative
                    try:
                        metadata, changed = copy_regular_file(source_file, destination)
                    except (OSError, CaptureError) as error:
                        skipped_entries.append(
                            {"path": str(source_file), "reason": str(error)}
                        )
                        partial_reasons.append(
                            "one or more companion files could not be copied safely"
                        )
                        continue
                    if changed:
                        partial_reasons.append(
                            "one or more companion files changed during capture"
                        )
                    captured_files.append(
                        {
                            "source_path": str(source_file),
                            "snapshot_relative_path": (
                                Path("artifacts") / relative
                            ).as_posix(),
                            **metadata,
                        }
                    )

            result = "partial" if partial_reasons else "captured"
            limitations.extend(sorted(set(partial_reasons)))
            total_bytes = sum(item["bytes"] for item in captured_files)
            manifest = {
                **attempt,
                "capture_completed_at": utc_now(),
                "capture_result": result,
                "original_primary_source_path": str(source_match),
                "safe_original_source_locator": safe_source_locator(
                    source_match, source_root, safe_root
                ),
                "bounded_surface": (
                    "exact primary transcript plus regular non-symlink descendants of "
                    "the exact adjacent session directory"
                    if args.harness == "claude-code"
                    else "the one exact matching rollout JSONL"
                ),
                "primary_transcript": primary_entry,
                "captured_files": captured_files,
                "captured_file_count": len(captured_files),
                "captured_total_bytes": total_bytes,
                "skipped_entries": skipped_entries,
                "limitations": [LIVE_BOUNDARY_NOTICE, *limitations],
            }
            manifest_value = json_bytes(manifest)
            write_private_file(staging / "manifest.json", manifest_value)
            install_refresh(target, staging, previous)
            manifest_sha256 = sha256_bytes(manifest_value)
            attempt.update(
                {
                    "capture_completed_at": manifest["capture_completed_at"],
                    "capture_result": result,
                    "safe_original_source_locator": manifest[
                        "safe_original_source_locator"
                    ],
                    "bounded_surface": manifest["bounded_surface"],
                    "captured_file_count": len(captured_files),
                    "captured_total_bytes": total_bytes,
                    "primary_bytes": primary_entry["bytes"],
                    "primary_sha256": primary_entry["sha256"],
                    "manifest_locator": (
                        target / "manifest.json"
                    ).relative_to(repo).as_posix(),
                    "manifest_sha256": manifest_sha256,
                    "limitations": [LIVE_BOUNDARY_NOTICE, *limitations],
                    "previous_snapshot_preserved": False,
                }
            )

    if source_match is None or result in {"unavailable", "inaccessible"}:
        attempt.update(
            {
                "capture_completed_at": utc_now(),
                "capture_result": result,
                "bounded_surface": (
                    f"exact {identity_source} identity lookup only; no transcript copied"
                ),
                "captured_file_count": 0,
                "captured_total_bytes": 0,
                "limitations": limitations,
                "previous_snapshot_preserved": target.is_dir()
                and not target.is_symlink(),
            }
        )
        previous_metadata = previous_snapshot_metadata(target, repo)
        if previous_metadata:
            attempt["previous_snapshot"] = previous_metadata
        if discovery_errors:
            attempt["private_discovery_errors"] = discovery_errors
        if pruned_symlinks:
            attempt["private_pruned_symlink_count"] = len(pruned_symlinks)

    write_private_json_atomic(last_attempt, attempt)
    attempt["last_attempt_locator"] = last_attempt.relative_to(repo).as_posix()
    attempt["last_attempt_sha256"] = sha256_bytes(last_attempt.read_bytes())
    return attempt


def public_summary(attempt: dict[str, Any]) -> dict[str, Any]:
    """Emit safe provenance metadata, never absolute roots or private errors."""
    return {
        key: value
        for key, value in attempt.items()
        if (
            key not in {"configured_source_root", "resolved_source_root"}
            and not key.startswith("private_")
        )
        or key == "private_snapshot_locator"
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Capture one exact Claude Code or Codex session below an ignored Relay "
            "private migration path."
        )
    )
    parser.add_argument(
        "--harness", required=True, choices=("claude-code", "codex")
    )
    parser.add_argument("--migration-id", required=True)
    parser.add_argument("--repo-root", default=".")
    return parser.parse_args()


def main() -> int:
    os.umask(0o077)
    try:
        result = capture(parse_args())
    except CaptureError as error:
        print(json.dumps({"capture_result": "inaccessible", "error": str(error)}))
        return 2
    except OSError as error:
        print(
            json.dumps(
                {
                    "capture_result": "inaccessible",
                    "error": (
                        f"filesystem operation failed ({type(error).__name__}); "
                        "no completed capture result was emitted"
                    ),
                }
            )
        )
        return 2
    print(json.dumps(public_summary(result), sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
