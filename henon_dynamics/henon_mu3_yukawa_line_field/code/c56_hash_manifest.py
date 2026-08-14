#!/usr/bin/env python3
"""Build or verify the self-excluding HCS-C56 scoped PREFREEZE manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import stat
import sys
from typing import Any


PROJECT = Path(__file__).resolve().parents[1]
MANIFEST_RELATIVE = "results/scoped_hash_manifest.json"
DEFAULT_MANIFEST = PROJECT / MANIFEST_RELATIVE
CERTIFICATE_RELATIVE = "results/c56_certificate.json"
SCHEMA_RELATIVE = "results/c56_schema.json"
CHECK_RELATIVE = "results/c56_check_report.json"
OVERRIDABLE = (CERTIFICATE_RELATIVE, SCHEMA_RELATIVE, CHECK_RELATIVE)
SCOPED_REQUIRED = {
    "code/README.md",
    "code/c56_atomic_promote.py",
    "code/c56_checker.py",
    "code/c56_hash_manifest.py",
    "code/c56_producer.py",
    "code/run_all.sh",
    "code/test_c56.py",
    "results/RESULTS.md",
    "results/TEST_REPORT.md",
    CERTIFICATE_RELATIVE,
    SCHEMA_RELATIVE,
    CHECK_RELATIVE,
}
INVENTORY_REQUIRED = SCOPED_REQUIRED | {MANIFEST_RELATIVE}
IGNORED_PARTS = {"__pycache__", ".pytest_cache", ".ipynb_checkpoints"}
MAX_MANIFEST_BYTES = 100_000


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def regular_file(path: Path) -> bool:
    try:
        mode = path.lstat().st_mode
    except FileNotFoundError:
        return False
    return stat.S_ISREG(mode) and not path.is_symlink()


def safe_relative(relative: str) -> bool:
    pure = PurePosixPath(relative)
    return (
        type(relative) is str
        and not pure.is_absolute()
        and str(pure) == relative
        and "\\" not in relative
        and all(part not in ("", ".", "..") for part in pure.parts)
    )


def live_inventory(*, ignore_private_stage: bool) -> set[str]:
    inventory: set[str] = set()
    for root_name in ("code", "results"):
        root = PROJECT / root_name
        if not root.is_dir():
            continue
        for path in root.rglob("*"):
            relative_path = path.relative_to(PROJECT)
            if any(part in IGNORED_PARTS for part in relative_path.parts):
                continue
            if ignore_private_stage and any(part.startswith(".c56-stage-") for part in relative_path.parts):
                continue
            if path.is_symlink():
                raise AssertionError(f"symlink forbidden in scoped inventory: {relative_path}")
            if path.is_file():
                relative = relative_path.as_posix()
                if not safe_relative(relative):
                    raise AssertionError(f"unsafe scoped path: {relative}")
                inventory.add(relative)
    return inventory


def artifact_paths(overrides: dict[str, Path] | None = None) -> dict[str, Path]:
    overrides = overrides or {}
    if set(overrides) - set(OVERRIDABLE):
        raise AssertionError("unknown manifest override")
    inventory = live_inventory(ignore_private_stage=bool(overrides))
    expected_inventory = INVENTORY_REQUIRED if not overrides else SCOPED_REQUIRED - set(OVERRIDABLE)
    observed_for_gate = inventory if not overrides else inventory - set(OVERRIDABLE) - {MANIFEST_RELATIVE}
    missing = expected_inventory - observed_for_gate
    extras = observed_for_gate - expected_inventory
    if missing or extras:
        raise AssertionError(
            "scoped inventory mismatch; missing=" + ",".join(sorted(missing))
            + "; extras=" + ",".join(sorted(extras))
        )
    paths: dict[str, Path] = {}
    for relative in sorted(SCOPED_REQUIRED):
        path = overrides.get(relative, PROJECT / relative)
        if not regular_file(path):
            raise AssertionError(f"required regular file missing: {relative}")
        paths[relative] = path
    return paths


def manifest_object(overrides: dict[str, Path] | None = None) -> dict[str, Any]:
    paths = artifact_paths(overrides)
    entries = [
        {
            "path": relative,
            "sha256": sha256_file(path),
            "size_bytes": path.stat().st_size,
        }
        for relative, path in sorted(paths.items())
    ]
    return {
        "schema": "hcs-c56-scoped-hash-manifest-v1",
        "status": "PREFREEZE_CODE_RESULTS_PASS",
        "scope": "exact_C56_code_and_results_artifacts",
        "manifest_self_included": False,
        "entry_count": len(entries),
        "entries": entries,
    }


def manifest_bytes(overrides: dict[str, Path] | None = None) -> bytes:
    return json.dumps(
        manifest_object(overrides), sort_keys=True, indent=2, ensure_ascii=False
    ).encode("utf-8") + b"\n"


def atomic_write(output: Path, raw: bytes) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_name(f".{output.name}.{os.getpid()}.new")
    try:
        temporary.write_bytes(raw)
        os.replace(temporary, output)
    finally:
        temporary.unlink(missing_ok=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--certificate", type=Path)
    parser.add_argument("--schema-file", type=Path)
    parser.add_argument("--check-report", type=Path)
    arguments = parser.parse_args()
    if sys.flags.optimize or os.environ.get("PYTHONOPTIMIZE") not in (None, "", "0"):
        raise SystemExit("optimized Python is forbidden")
    supplied = (arguments.certificate, arguments.schema_file, arguments.check_report)
    if any(value is not None for value in supplied) and not all(value is not None for value in supplied):
        parser.error("certificate, schema-file, and check-report overrides are all-or-none")
    overrides = None
    if all(value is not None for value in supplied):
        overrides = dict(zip(OVERRIDABLE, supplied))
    expected = manifest_bytes(overrides)
    if len(expected) > MAX_MANIFEST_BYTES:
        raise AssertionError("scoped manifest exceeds size budget")
    if arguments.write:
        if arguments.manifest.exists() and not regular_file(arguments.manifest):
            raise SystemExit("manifest output exists and is not a regular file")
        atomic_write(arguments.manifest, expected)
        print(f"wrote {len(SCOPED_REQUIRED)} scoped manifest entries")
    if not regular_file(arguments.manifest):
        raise SystemExit(f"scoped manifest missing: {arguments.manifest}")
    actual = arguments.manifest.read_bytes()
    if len(actual) > MAX_MANIFEST_BYTES or actual != expected:
        raise SystemExit("scoped manifest inventory/digest mismatch")
    print(f"verified {len(SCOPED_REQUIRED)} scoped manifest entries")
    print(f"manifest_sha256={hashlib.sha256(actual).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
