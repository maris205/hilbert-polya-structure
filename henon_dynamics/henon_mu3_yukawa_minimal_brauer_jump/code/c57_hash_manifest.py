#!/usr/bin/env python3
"""Build or verify the exact self-excluding HCS-C57 scoped manifest."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import stat
import sys
from typing import Any

from c57_exact import (
    StrictDataError,
    canonical_json_bytes,
    deep_exact,
    read_stable,
    reject_optimized_python,
    require_exact_keys,
    safe_relative_path,
    strict_json_loads,
)


PROJECT = Path(__file__).resolve().parents[1]
CODE = PROJECT / "code"
RESULTS = PROJECT / "results"
MANIFEST_RELATIVE = "results/scoped_hash_manifest.json"
DEFAULT_MANIFEST = PROJECT / MANIFEST_RELATIVE
MAX_MANIFEST_BYTES = 100_000

CODE_NAMES = (
    "README.md",
    "c57_a12_reconstruction.py",
    "c57_atomic_promote.py",
    "c57_checker.py",
    "c57_exact.py",
    "c57_flint_carrier_identity.py",
    "c57_group.py",
    "c57_hash_manifest.py",
    "c57_incidence_bridge.py",
    "c57_incidence_char0_verify.py",
    "c57_irreducibility.py",
    "c57_modular_resolvent.py",
    "c57_pipeline.py",
    "c57_producer.py",
    "c57_quartic_pivot.py",
    "c57_resolver_replay.py",
    "run_all.sh",
    "test_c57.py",
)
PROSE_NAMES = ("RESULTS.md", "TEST_REPORT.md")
PROMOTED_NAMES = (
    "a12_crt_transcript.json.gz",
    "a12_table.json.gz",
    "delta_crt.json.gz",
    "incidence_char0_witness.json.gz",
    "theta_crt.json.gz",
    "c57_schema.json",
    "c57_certificate.json",
    "c57_check_report.json",
    "scoped_hash_manifest.json",
)
SCOPED_RELATIVES = tuple(f"code/{name}" for name in CODE_NAMES) + tuple(
    f"results/{name}" for name in PROSE_NAMES + PROMOTED_NAMES[:-1]
)
LIVE_RELATIVES = set(SCOPED_RELATIVES) | {MANIFEST_RELATIVE}


def _regular(path: Path, label: str) -> os.stat_result:
    try:
        metadata = path.lstat()
    except FileNotFoundError as exc:
        raise StrictDataError(f"missing {label}: {path}") from exc
    if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
        raise StrictDataError(f"{label} must be a non-symlink regular file: {path}")
    return metadata


def _validate_constants() -> None:
    if len(CODE_NAMES) != 18 or len(set(CODE_NAMES)) != 18:
        raise StrictDataError("manifest code allowlist must have 18 distinct names")
    if len(PROMOTED_NAMES) != 9 or len(set(PROMOTED_NAMES)) != 9:
        raise StrictDataError("manifest promotion allowlist must have 9 distinct names")
    if len(SCOPED_RELATIVES) != 28 or len(set(SCOPED_RELATIVES)) != 28:
        raise StrictDataError("manifest scope must have 28 distinct self-excluded entries")
    if not all(safe_relative_path(value) for value in LIVE_RELATIVES):
        raise StrictDataError("unsafe path in manifest allowlist")


def _active_stage(stage: Path | None) -> Path | None:
    if stage is None:
        return None
    try:
        before = stage.lstat()
    except FileNotFoundError as exc:
        raise StrictDataError("active stage is missing") from exc
    if stat.S_ISLNK(before.st_mode) or not stat.S_ISDIR(before.st_mode):
        raise StrictDataError("active stage must be a non-symlink directory")
    resolved_results = RESULTS.resolve(strict=True)
    resolved = stage.resolve(strict=True)
    if resolved.parent != resolved_results or not resolved.name.startswith(".c57-stage-"):
        raise StrictDataError("active stage must be one named direct child of results")
    after = resolved.lstat()
    if (before.st_dev, before.st_ino) != (after.st_dev, after.st_ino):
        raise StrictDataError("active stage changed while resolving")
    return resolved


def _directory_identity(path: Path) -> tuple[int, int, int]:
    metadata = path.lstat()
    if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISDIR(metadata.st_mode):
        raise StrictDataError("active stage identity is no longer a real directory")
    return metadata.st_dev, metadata.st_ino, metadata.st_mode


def _flat_inventory(root: Path, active_stage: Path | None) -> set[str]:
    observed: set[str] = set()
    for child in root.iterdir():
        absolute = child.absolute()
        if active_stage is not None and absolute == active_stage:
            continue
        metadata = child.lstat()
        relative = child.relative_to(PROJECT).as_posix()
        if stat.S_ISLNK(metadata.st_mode):
            raise StrictDataError(f"scoped symlink forbidden: {relative}")
        if not stat.S_ISREG(metadata.st_mode):
            raise StrictDataError(f"scoped directory/FIFO/socket forbidden: {relative}")
        observed.add(relative)
    return observed


def live_inventory(stage: Path | None = None) -> set[str]:
    active = _active_stage(stage)
    return _flat_inventory(CODE, active) | _flat_inventory(RESULTS, active)


def refresh_hygiene() -> None:
    _validate_constants()
    observed = live_inventory()
    base = {f"code/{name}" for name in CODE_NAMES} | {
        f"results/{name}" for name in PROSE_NAMES
    }
    permitted = base | {f"results/{name}" for name in PROMOTED_NAMES}
    if not base.issubset(observed) or not observed.issubset(permitted):
        raise StrictDataError(
            f"refresh hygiene mismatch; missing={sorted(base-observed)}; "
            f"extra={sorted(observed-permitted)}"
        )


def live_snapshot() -> dict[str, Any]:
    observed = live_inventory()
    if observed != LIVE_RELATIVES:
        raise StrictDataError("snapshot requires the exact 29-entry live inventory")
    entries = []
    for relative in sorted(observed):
        path = PROJECT / relative
        before = path.lstat()
        raw, fingerprint_value = read_stable(path, max_bytes=50_000_000)
        after = path.lstat()
        if (
            before.st_dev,
            before.st_ino,
            before.st_size,
            before.st_mode,
            before.st_mtime_ns,
        ) != (
            after.st_dev,
            after.st_ino,
            after.st_size,
            after.st_mode,
            after.st_mtime_ns,
        ):
            raise StrictDataError("live snapshot pathname changed during stable read")
        entries.append(
            {
                "path": relative,
                "sha256": fingerprint_value.sha256,
                "size_bytes": len(raw),
                "mode": fingerprint_value.mode,
                "mtime_ns": fingerprint_value.mtime_ns,
                "device": after.st_dev,
                "inode": after.st_ino,
            }
        )
    return {"schema_id": "hcs-c57-live-nonmutation-snapshot-v1", "entries": entries}


def _stage_sources(stage: Path) -> dict[str, Path]:
    expected = set(PROMOTED_NAMES[:-1])
    observed = set()
    for child in stage.iterdir():
        metadata = child.lstat()
        if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
            raise StrictDataError("stage contains a nonregular entry")
        observed.add(child.name)
    permitted = (expected, expected | {PROMOTED_NAMES[-1]})
    if observed not in permitted:
        raise StrictDataError(
            f"pre-manifest stage inventory mismatch; missing={sorted(expected-observed)}; "
            f"extra={sorted(observed-(expected | {PROMOTED_NAMES[-1]}))}"
        )
    return {f"results/{name}": stage / name for name in PROMOTED_NAMES[:-1]}


def artifact_paths(stage: Path | None = None) -> dict[str, Path]:
    _validate_constants()
    active = _active_stage(stage)
    stage_identity = _directory_identity(active) if active is not None else None
    observed = live_inventory(active)
    base = {f"code/{name}" for name in CODE_NAMES} | {
        f"results/{name}" for name in PROSE_NAMES
    }
    if active is None:
        if observed != LIVE_RELATIVES:
            raise StrictDataError(
                f"live scoped inventory mismatch; missing={sorted(LIVE_RELATIVES-observed)}; "
                f"extra={sorted(observed-LIVE_RELATIVES)}"
            )
        return {relative: PROJECT / relative for relative in SCOPED_RELATIVES}

    permitted_live_targets = {f"results/{name}" for name in PROMOTED_NAMES}
    reduced = observed - permitted_live_targets
    if reduced != base or observed - base - permitted_live_targets:
        raise StrictDataError(
            f"refresh live inventory mismatch; missing={sorted(base-reduced)}; "
            f"extra={sorted(reduced-base)}"
        )
    sources = {
        relative: PROJECT / relative
        for relative in SCOPED_RELATIVES
        if not relative.startswith("results/")
        or relative in {f"results/{name}" for name in PROSE_NAMES}
    }
    sources.update(_stage_sources(active))
    if _directory_identity(active) != stage_identity:
        raise StrictDataError("active stage changed during manifest inventory")
    if set(sources) != set(SCOPED_RELATIVES):
        raise StrictDataError("staged manifest source mapping is incomplete")
    return sources


def manifest_object(stage: Path | None = None) -> dict[str, Any]:
    active = _active_stage(stage)
    stage_identity = _directory_identity(active) if active is not None else None
    entries = []
    for relative, path in sorted(artifact_paths(active).items()):
        _regular(path, "manifest input")
        raw, fingerprint = read_stable(path, max_bytes=50_000_000)
        entries.append(
            {"path": relative, "sha256": fingerprint.sha256, "size_bytes": len(raw)}
        )
    if active is not None and _directory_identity(active) != stage_identity:
        raise StrictDataError("active stage changed while hashing manifest inputs")
    return {
        "schema": "hcs-c57-scoped-hash-manifest-v1",
        "status": "PREFREEZE_CODE_RESULTS_PASS",
        "scope": "exact_C57_code_and_results_artifacts",
        "manifest_self_included": False,
        "entry_count": len(entries),
        "entries": entries,
    }


def manifest_bytes(stage: Path | None = None) -> bytes:
    value = manifest_object(stage)
    if value["entry_count"] != 28:
        raise StrictDataError("wrong C57 manifest entry count")
    raw = canonical_json_bytes(value, pretty=True)
    if len(raw) > MAX_MANIFEST_BYTES:
        raise StrictDataError("C57 scoped manifest exceeds byte ceiling")
    return raw


def _atomic_write_bound_stage_manifest(
    stage: Path,
    expected_identity: tuple[int, int, int],
    raw: bytes,
) -> None:
    """Write the manifest through a directory FD bound to the active stage."""
    flags = (
        os.O_RDONLY
        | getattr(os, "O_CLOEXEC", 0)
        | getattr(os, "O_NOFOLLOW", 0)
        | getattr(os, "O_DIRECTORY", 0)
    )
    directory_fd = os.open(stage, flags)
    temporary_name = f".{PROMOTED_NAMES[-1]}.{os.getpid()}.new"
    temporary_fd = -1
    temporary_identity: tuple[int, int] | None = None
    try:
        opened = os.fstat(directory_fd)
        if (opened.st_dev, opened.st_ino, opened.st_mode) != expected_identity:
            raise StrictDataError("active stage identity changed before manifest write")
        pathname = stage.lstat()
        if (pathname.st_dev, pathname.st_ino, pathname.st_mode) != expected_identity:
            raise StrictDataError("active stage pathname changed before manifest write")

        protected_inodes = set()
        for name in PROMOTED_NAMES[:-1]:
            metadata = os.stat(name, dir_fd=directory_fd, follow_symlinks=False)
            if not stat.S_ISREG(metadata.st_mode) or metadata.st_nlink != 1:
                raise StrictDataError("manifest input became nonregular or hardlinked")
            protected_inodes.add((metadata.st_dev, metadata.st_ino))
        try:
            old = os.stat(PROMOTED_NAMES[-1], dir_fd=directory_fd, follow_symlinks=False)
        except FileNotFoundError:
            pass
        else:
            if (
                not stat.S_ISREG(old.st_mode)
                or old.st_nlink != 1
                or (old.st_dev, old.st_ino) in protected_inodes
            ):
                raise StrictDataError("stale stage manifest is unsafe to replace")
            os.unlink(PROMOTED_NAMES[-1], dir_fd=directory_fd)
            os.fsync(directory_fd)

        create_flags = (
            os.O_WRONLY
            | os.O_CREAT
            | os.O_EXCL
            | getattr(os, "O_CLOEXEC", 0)
            | getattr(os, "O_NOFOLLOW", 0)
        )
        temporary_fd = os.open(temporary_name, create_flags, 0o600, dir_fd=directory_fd)
        temporary_metadata = os.fstat(temporary_fd)
        temporary_identity = (temporary_metadata.st_dev, temporary_metadata.st_ino)
        view = memoryview(raw)
        while view:
            written = os.write(temporary_fd, view)
            if written <= 0:
                raise OSError("short stage-manifest write")
            view = view[written:]
        os.fchmod(temporary_fd, 0o644)
        os.fsync(temporary_fd)
        final_temporary = os.fstat(temporary_fd)
        if (
            (final_temporary.st_dev, final_temporary.st_ino) != temporary_identity
            or final_temporary.st_size != len(raw)
            or stat.S_IMODE(final_temporary.st_mode) != 0o644
        ):
            raise StrictDataError("stage-manifest temporary metadata mismatch")
        os.close(temporary_fd)
        temporary_fd = -1
        os.replace(
            temporary_name,
            PROMOTED_NAMES[-1],
            src_dir_fd=directory_fd,
            dst_dir_fd=directory_fd,
        )
        temporary_identity = None
        os.fsync(directory_fd)
        final = os.stat(PROMOTED_NAMES[-1], dir_fd=directory_fd, follow_symlinks=False)
        if (
            not stat.S_ISREG(final.st_mode)
            or final.st_nlink != 1
            or final.st_size != len(raw)
            or stat.S_IMODE(final.st_mode) != 0o644
        ):
            raise StrictDataError("placed stage manifest metadata mismatch")
        pathname_after = stage.lstat()
        if (
            pathname_after.st_dev,
            pathname_after.st_ino,
            pathname_after.st_mode,
        ) != expected_identity:
            raise StrictDataError("active stage pathname changed during manifest write")
    finally:
        if temporary_fd >= 0:
            os.close(temporary_fd)
        if temporary_identity is not None:
            try:
                current = os.stat(temporary_name, dir_fd=directory_fd, follow_symlinks=False)
            except FileNotFoundError:
                pass
            else:
                if (current.st_dev, current.st_ino) == temporary_identity:
                    os.unlink(temporary_name, dir_fd=directory_fd)
                    os.fsync(directory_fd)
        os.close(directory_fd)


def verify_manifest(path: Path, stage: Path | None = None) -> dict[str, Any]:
    raw, _ = read_stable(path, max_bytes=MAX_MANIFEST_BYTES)
    value = strict_json_loads(raw, max_bytes=MAX_MANIFEST_BYTES)
    if raw != canonical_json_bytes(value, pretty=True):
        raise StrictDataError("manifest is not canonical pretty JSON")
    require_exact_keys(
        value,
        {"schema", "status", "scope", "manifest_self_included", "entry_count", "entries"},
        "C57 scoped manifest",
    )
    expected = manifest_object(stage)
    if not deep_exact(value, expected):
        raise StrictDataError("C57 scoped manifest semantic rebuild mismatch")
    return value


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--stage-dir", type=Path)
    parser.add_argument("--refresh-hygiene", action="store_true")
    parser.add_argument("--snapshot", action="store_true")
    arguments = parser.parse_args()
    reject_optimized_python()
    sys.set_int_max_str_digits(0)
    if arguments.refresh_hygiene or arguments.snapshot:
        if arguments.write or arguments.stage_dir is not None or arguments.manifest != DEFAULT_MANIFEST:
            raise StrictDataError("hygiene/snapshot modes do not accept write overrides")
        if arguments.refresh_hygiene and arguments.snapshot:
            raise StrictDataError("choose exactly one special manifest mode")
        if arguments.refresh_hygiene:
            refresh_hygiene()
            print("C57 refresh hygiene PASS")
        else:
            sys.stdout.buffer.write(canonical_json_bytes(live_snapshot()))
        return 0
    stage = _active_stage(arguments.stage_dir)
    stage_identity = _directory_identity(stage) if stage is not None else None
    if arguments.write and stage is None:
        raise StrictDataError("manifest writes require one explicit active stage")
    if arguments.write and arguments.manifest.absolute() != stage / PROMOTED_NAMES[-1]:
        raise StrictDataError("manifest write target must be the active-stage manifest")
    expected = manifest_bytes(stage)
    if arguments.write:
        if stage is None or stage_identity is None:
            raise StrictDataError("manifest write lost its active stage")
        if _directory_identity(stage) != stage_identity:
            raise StrictDataError("active stage changed after manifest construction")
        _atomic_write_bound_stage_manifest(stage, stage_identity, expected)
        if _directory_identity(stage) != stage_identity:
            raise StrictDataError("active stage changed after manifest placement")
    verify_manifest(arguments.manifest, stage)
    print(f"verified_manifest_entries=28")
    print(f"manifest_sha256={__import__('hashlib').sha256(expected).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
