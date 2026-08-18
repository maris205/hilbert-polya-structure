#!/usr/bin/env python3
"""Bounded predecessor-to-superseding Paper 44 overlay transaction."""

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
import tempfile
from pathlib import Path, PurePosixPath
from typing import Any


AUDITOR = "evidence/publication_gate/publication_auditor.py"
MANIFEST = "WRITER_MANIFEST.sha256"
SEAL = "evidence/publication_gate/PUBLICATION_OVERLAY_SEAL.json"
HEX64 = re.compile(r"[0-9a-f]{64}\Z")
HEX40 = re.compile(r"[0-9a-f]{40}\Z")


class InjectedFailure(Exception):
    pass


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       separators=(",", ": "), allow_nan=False) + "\n").encode("ascii")


def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def sha_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def safe_relative(value: Any) -> bool:
    if type(value) is not str or not value or "\\" in value:
        return False
    pure = PurePosixPath(value)
    return not pure.is_absolute() and all(part not in {"", ".", ".."} for part in pure.parts)


def emit(status: str, code: str, payload: dict[str, Any], exit_code: int) -> int:
    sys.stdout.buffer.write(canonical({
        "payload": {"code": code, **payload},
        "schema": "paper44-overlay-upgrade-transaction-v2",
        "status": status,
    }))
    return exit_code


def parse_manifest(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="ascii")
    if not text.endswith("\n") or "\r" in text:
        raise ValueError("manifest framing")
    result: dict[str, str] = {}
    order: list[str] = []
    for line in text.splitlines():
        if len(line) < 67 or line[64:66] != "  " \
                or HEX64.fullmatch(line[:64]) is None or not safe_relative(line[66:]) \
                or line[66:] in {MANIFEST, SEAL} or line[66:] in result:
            raise ValueError("manifest row")
        result[line[66:]] = line[:64]
        order.append(line[66:])
    if not result or order != sorted(order):
        raise ValueError("manifest order")
    return result


def parents(paths: set[str]) -> set[str]:
    result: set[str] = set()
    for relative in paths:
        parent = PurePosixPath(relative).parent
        while parent.as_posix() != ".":
            result.add(parent.as_posix())
            parent = parent.parent
    return result


def secure_root(path: Path, label: str) -> Path:
    if not path.is_absolute() or path.is_symlink() or not path.is_dir() \
            or path.resolve(strict=True) != path \
            or stat.S_IMODE(os.lstat(path).st_mode) != 0o755:
        raise ValueError("unsafe " + label)
    return path


def invoke_auditor(auditor: Path, root: Path, source: Path, anchor: str,
                   commit: str | None, source_only: bool,
                   relocated: bool,
                   allow_checklist: bool) -> tuple[int, dict[str, Any] | None, bytes]:
    command = [sys.executable, "-I", "-B", str(auditor), "--root", str(root),
               "--overlay-source", str(source), "--expected-publication-seal-sha256",
               anchor]
    if commit is not None:
        command += ["--expected-stage1-commit", commit]
    if source_only:
        command.append("--source-only")
    if relocated:
        command.append("--relocated-disposable")
    if allow_checklist:
        command.append("--allow-unexecuted-checklist")
    environment = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "PYTHONPATH": "",
                   "PYTHONDONTWRITEBYTECODE": "1", "TZ": "UTC", "LC_ALL": "C", "LANG": "C"}
    process = subprocess.run(command, cwd=root.parent, env=environment,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    value: dict[str, Any] | None = None
    try:
        parsed = json.loads(process.stdout.decode("ascii"), object_pairs_hook=unique)
        if type(parsed) is dict and process.stdout == canonical(parsed):
            value = parsed
    except Exception:
        pass
    if process.stderr:
        value = None
    return process.returncode, value, process.stderr


def protected_snapshot(root: Path, overlay_paths: set[str]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    overlay_directories = parents(overlay_paths)
    for path in sorted(root.rglob("*"), key=lambda item: item.relative_to(root).as_posix()):
        relative = path.relative_to(root).as_posix()
        if relative in overlay_paths or relative in overlay_directories or any(
                relative.startswith(directory + "/") for directory in overlay_directories):
            # Files below an overlay directory are handled by the exact post-audit.
            continue
        metadata = os.lstat(path)
        if stat.S_ISDIR(metadata.st_mode):
            kind, digest = "directory", None
        elif stat.S_ISREG(metadata.st_mode):
            kind, digest = "regular", sha_file(path)
        elif stat.S_ISLNK(metadata.st_mode):
            kind, digest = "symlink", os.readlink(path)
        else:
            kind, digest = "nonregular", None
        rows.append({
            "gid": metadata.st_gid, "inode": metadata.st_ino, "kind": kind,
            "mode": stat.S_IMODE(metadata.st_mode), "mtime_ns": metadata.st_mtime_ns,
            "nlink": metadata.st_nlink, "path": relative, "sha256": digest,
            "size": metadata.st_size, "uid": metadata.st_uid,
        })
    return rows


def logical_tree(root: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in [root] + sorted(root.rglob("*"), key=lambda item: item.relative_to(root).as_posix()):
        metadata = os.lstat(path)
        relative = "." if path == root else path.relative_to(root).as_posix()
        if stat.S_ISDIR(metadata.st_mode):
            kind, digest = "directory", None
        elif stat.S_ISREG(metadata.st_mode):
            kind, digest = "regular", sha_file(path)
        elif stat.S_ISLNK(metadata.st_mode):
            kind, digest = "symlink", os.readlink(path)
        else:
            kind, digest = "nonregular", None
        rows.append({"kind": kind, "mode": stat.S_IMODE(metadata.st_mode),
                     "path": relative, "sha256": digest})
    return rows


def restore_directory_times(saved: dict[Path, tuple[int, int]]) -> None:
    for path in sorted(saved, key=lambda item: len(item.parts), reverse=True):
        if path.is_dir() and not path.is_symlink():
            os.utime(path, ns=saved[path])


def main() -> int:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--source", required=True)
    parser.add_argument("--target", required=True)
    parser.add_argument("--expected-publication-seal-sha256")
    parser.add_argument("--expected-stage1-commit")
    parser.add_argument("--force-late-failure", action="store_true")
    parser.add_argument("--inject-install-failure-after", type=int)
    parser.add_argument("--relocated-disposable", action="store_true")
    parser.add_argument("--allow-unexecuted-checklist", action="store_true")
    arguments = parser.parse_args()

    anchor = arguments.expected_publication_seal_sha256
    commit = arguments.expected_stage1_commit
    if anchor is None:
        return emit("REJECT", "EXPECTED_PUBLICATION_SEAL_SHA256_MISSING", {}, 2)
    if type(anchor) is not str or HEX64.fullmatch(anchor) is None:
        return emit("REJECT", "EXPECTED_PUBLICATION_SEAL_SHA256_INVALID", {}, 2)
    if commit is not None and (type(commit) is not str or HEX40.fullmatch(commit) is None
                               or commit == "0" * 40):
        return emit("REJECT", "EXPECTED_STAGE1_COMMIT_INVALID", {}, 2)
    if arguments.inject_install_failure_after is not None \
            and arguments.inject_install_failure_after < 1:
        return emit("REJECT", "INVALID_FAILURE_INJECTION", {}, 2)

    try:
        source = secure_root(Path(arguments.source), "source")
        target = secure_root(Path(arguments.target), "target")
    except Exception as error:
        return emit("REJECT", "UNSAFE_ROOT", {"exception_type": type(error).__name__}, 2)
    if arguments.relocated_disposable:
        if not str(source).startswith("/tmp/") or not str(target).startswith("/tmp/"):
            return emit("REJECT", "RELOCATED_MODE_OUTSIDE_TMP_FORBIDDEN", {}, 2)
    if arguments.inject_install_failure_after is not None and not arguments.relocated_disposable:
        return emit("REJECT", "INJECTION_REQUIRES_RELOCATED_DISPOSABLE", {}, 2)
    if arguments.allow_unexecuted_checklist and not arguments.relocated_disposable:
        return emit("REJECT", "CHECKLIST_OVERRIDE_REQUIRES_RELOCATED_DISPOSABLE", {}, 2)

    # The operational protocol executes this transaction from a separately
    # authenticated, read-only controller directory.  Never bootstrap trust by
    # executing the mutable source overlay's copy of the auditor.
    auditor = Path(__file__).resolve(strict=True).with_name("publication_auditor.py")
    source_result = invoke_auditor(auditor, source, source, anchor, commit, True,
                                   arguments.relocated_disposable,
                                   arguments.allow_unexecuted_checklist)
    if source_result[0] != 0 or source_result[1] is None \
            or source_result[1].get("payload", {}).get("code") != "SOURCE_OVERLAY_EXACT":
        nested = source_result[1].get("payload", {}).get("code") \
            if source_result[1] else "INVALID_ENVELOPE"
        return emit("REJECT", "SOURCE_PREFLIGHT_REJECT", {"nested_code": nested}, 2)
    target_result = invoke_auditor(auditor, target, source, anchor, commit, False,
                                   arguments.relocated_disposable,
                                   arguments.allow_unexecuted_checklist)
    if target_result[0] != 0 or target_result[1] is None \
            or target_result[1].get("status") != "PASS":
        nested = target_result[1].get("payload", {}).get("code") \
            if target_result[1] else "INVALID_ENVELOPE"
        return emit("REJECT", "TARGET_PREFLIGHT_REJECT", {"nested_code": nested}, 2)
    state = target_result[1]["payload"]["state"]

    try:
        wanted_manifest = parse_manifest(source / MANIFEST)
        wanted_files = set(wanted_manifest) | {MANIFEST, SEAL}
        if state in {"PUBLISHED_STATE_A_EXACT", "PUBLISHED_STATE_B_EXACT"}:
            return emit("PASS", "ALREADY_INSTALLED_EXACT", {
                "overlay_file_count": len(wanted_files),
                "physical_target_replacements": 0,
                "protected_metadata_preserved": True,
                "state": state,
            }, 0)
        if state != "PREDECESSOR_STATE_A_EXACT":
            return emit("REJECT", "UPGRADE_SOURCE_STATE_FORBIDDEN", {"state": state}, 2)
        old_manifest = parse_manifest(target / MANIFEST)
        old_files = set(old_manifest) | {MANIFEST, SEAL}
        overlay_universe = old_files | wanted_files
        before_tree = logical_tree(target)
        protected_before = protected_snapshot(target, overlay_universe)
    except Exception as error:
        return emit("REJECT", "TRANSACTION_PREFLIGHT_EXCEPTION",
                    {"exception_type": type(error).__name__}, 2)

    temporary = Path(tempfile.mkdtemp(prefix=".paper44-overlay-upgrade-", dir=target.parent))
    stage = temporary / "stage"
    backup = temporary / "backup"
    installed: list[tuple[str, bool]] = []
    removed: list[str] = []
    created_directories: list[Path] = []
    saved_directory_times: dict[Path, tuple[int, int]] = {}
    physical = 0
    try:
        shutil.copytree(source, stage, copy_function=shutil.copy2)
        stage.chmod(0o755)
        staged = invoke_auditor(auditor, stage, stage, anchor, commit, True,
                                arguments.relocated_disposable,
                                arguments.allow_unexecuted_checklist)
        if staged[0] != 0 or staged[1] is None \
                or staged[1].get("payload", {}).get("code") != "SOURCE_OVERLAY_EXACT":
            raise ValueError("staged source audit")
        changed = [relative for relative in sorted(wanted_files)
                   if not (target / relative).is_file()
                   or sha_file(target / relative) != sha_file(stage / relative)
                   or stat.S_IMODE(os.lstat(target / relative).st_mode) != 0o644]
        obsolete = sorted(old_files - wanted_files)
        if logical_tree(target) != before_tree:
            shutil.rmtree(temporary)
            return emit("REJECT", "TARGET_CHANGED_DURING_STAGING", {
                "physical_target_replacements": 0,
                "target_writes_by_transaction": 0,
            }, 2)
        root_metadata = os.lstat(target)
        saved_directory_times[target] = (root_metadata.st_atime_ns, root_metadata.st_mtime_ns)
        if arguments.force_late_failure:
            shutil.rmtree(temporary)
            return emit("FORCED_FAILURE", "FORCED_LATE_FAILURE", {
                "overlay_bytes_fully_staged": True,
                "physical_target_replacements": 0,
                "protected_metadata_preserved":
                    protected_snapshot(target, overlay_universe) == protected_before,
                "target_unchanged": logical_tree(target) == before_tree,
            }, 86)

        for relative in sorted(parents(set(changed) | set(obsolete))):
            path = target / relative
            if path.exists():
                if path.is_symlink() or not path.is_dir():
                    raise ValueError("unsafe parent")
                metadata = os.lstat(path)
                saved_directory_times[path] = (metadata.st_atime_ns, metadata.st_mtime_ns)
            else:
                path.mkdir(mode=0o755)
                path.chmod(0o755)
                created_directories.append(path)
        backup.mkdir(mode=0o755)
        for relative in changed:
            destination = target / relative
            existed = destination.exists()
            if existed:
                backup_path = backup / relative
                backup_path.parent.mkdir(parents=True, exist_ok=True)
                os.replace(destination, backup_path)
            try:
                os.replace(stage / relative, destination)
            except Exception:
                if existed:
                    os.replace(backup / relative, destination)
                raise
            installed.append((relative, existed))
            destination.chmod(0o644)
            physical += 1
            if arguments.inject_install_failure_after == physical:
                raise InjectedFailure("injected install failure")
        for relative in obsolete:
            destination = target / relative
            backup_path = backup / relative
            backup_path.parent.mkdir(parents=True, exist_ok=True)
            os.replace(destination, backup_path)
            removed.append(relative)
            physical += 1
            if arguments.inject_install_failure_after == physical:
                raise InjectedFailure("injected install failure")
        restore_directory_times(saved_directory_times)
        if protected_snapshot(target, overlay_universe) != protected_before:
            raise RuntimeError("protected metadata changed")
        post = invoke_auditor(auditor, target, source, anchor, commit, False,
                              arguments.relocated_disposable,
                              arguments.allow_unexecuted_checklist)
        if post[0] != 0 or post[1] is None \
                or post[1].get("payload", {}).get("state") != "PUBLISHED_STATE_A_EXACT":
            raise RuntimeError("post-install audit")
        shutil.rmtree(temporary)
        return emit("PASS", "UPGRADED_TO_SUPERSEDING_OVERLAY", {
            "overlay_file_count": len(wanted_files),
            "physical_target_replacements": physical,
            "protected_metadata_preserved": True,
            "removed_predecessor_file_count": len(obsolete),
            "state": "PUBLISHED_STATE_A_EXACT",
        }, 0)
    except Exception as error:
        rollback_ok = True
        try:
            for relative in reversed(removed):
                os.replace(backup / relative, target / relative)
            for relative, existed in reversed(installed):
                destination = target / relative
                if destination.exists():
                    destination.unlink()
                if existed:
                    os.replace(backup / relative, destination)
            for directory in sorted(created_directories, key=lambda item: len(item.parts), reverse=True):
                try:
                    directory.rmdir()
                except OSError:
                    rollback_ok = False
            restore_directory_times(saved_directory_times)
            rollback_ok = rollback_ok and logical_tree(target) == before_tree \
                and protected_snapshot(target, overlay_universe) == protected_before
            prior = invoke_auditor(auditor, target, source, anchor, commit, False,
                                   arguments.relocated_disposable,
                                   arguments.allow_unexecuted_checklist)
            rollback_ok = rollback_ok and prior[0] == 0 and prior[1] is not None \
                and prior[1].get("payload", {}).get("state") == "PREDECESSOR_STATE_A_EXACT"
        except Exception:
            rollback_ok = False
        shutil.rmtree(temporary, ignore_errors=True)
        rollback_code = "INJECTED_INSTALL_FAILURE_ROLLED_BACK" \
            if isinstance(error, InjectedFailure) else "INSTALL_FAILURE_ROLLED_BACK"
        return emit("ROLLED_BACK" if rollback_ok else "ROLLBACK_FAILED",
                    rollback_code if rollback_ok else "INSTALL_FAILURE_ROLLBACK_FAILED", {
                        "exception_type": type(error).__name__,
                        "physical_target_replacements_before_failure": physical,
                        "protected_metadata_preserved": rollback_ok,
                        "target_unchanged": rollback_ok,
                    }, 87 if rollback_ok else 88)


if __name__ == "__main__":
    raise SystemExit(main())
