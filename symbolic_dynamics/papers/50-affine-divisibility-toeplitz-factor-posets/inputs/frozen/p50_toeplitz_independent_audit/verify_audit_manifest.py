#!/usr/bin/env python3
"""Verify the self-excluding manifest and hygiene of this audit package."""

from __future__ import annotations

import hashlib
import json
import os
import stat
from pathlib import Path


ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "SHA256SUMS.txt"
CACHE_NAMES = {"__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}
EXECUTABLES = {"independent_checks.py", "verify_audit_manifest.py"}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    entries: list[tuple[str, str]] = []
    for lineno, line in enumerate(MANIFEST.read_text(encoding="utf-8").splitlines(), 1):
        if not line:
            raise SystemExit(f"FAIL: blank line {lineno}")
        try:
            digest, rel = line.split("  ", 1)
        except ValueError as exc:
            raise SystemExit(f"FAIL: malformed line {lineno}") from exc
        if len(digest) != 64 or any(ch not in "0123456789abcdef" for ch in digest):
            raise SystemExit(f"FAIL: invalid digest on line {lineno}")
        path = Path(rel)
        if path.is_absolute() or not rel or ".." in path.parts:
            raise SystemExit(f"FAIL: unsafe path on line {lineno}")
        entries.append((rel, digest))
    paths = [rel for rel, _ in entries]
    if paths != sorted(paths) or len(paths) != len(set(paths)):
        raise SystemExit("FAIL: manifest paths must be sorted and unique")

    discovered: list[str] = []
    for dirpath, dirnames, filenames in os.walk(ROOT, topdown=True, followlinks=False):
        directory = Path(dirpath)
        for name in sorted(dirnames + filenames):
            path = directory / name
            rel = path.relative_to(ROOT).as_posix()
            info = path.lstat()
            if name in CACHE_NAMES or name.endswith((".pyc", ".pyo")):
                raise SystemExit(f"FAIL: cache artifact {rel}")
            if stat.S_ISLNK(info.st_mode):
                raise SystemExit(f"FAIL: symlink {rel}")
            if not (stat.S_ISREG(info.st_mode) or stat.S_ISDIR(info.st_mode)):
                raise SystemExit(f"FAIL: nonregular path {rel}")
            expected_mode = 0o755 if stat.S_ISDIR(info.st_mode) else (
                0o755 if rel in EXECUTABLES else 0o644
            )
            if stat.S_IMODE(info.st_mode) != expected_mode:
                raise SystemExit(
                    f"FAIL: mode {stat.S_IMODE(info.st_mode):04o} != {expected_mode:04o} for {rel}"
                )
            if stat.S_ISREG(info.st_mode) and rel != "SHA256SUMS.txt":
                discovered.append(rel)
    discovered.sort()
    if paths != discovered:
        raise SystemExit("FAIL: manifest file set differs from package file set")
    for rel, expected in entries:
        observed = sha256_file(ROOT / rel)
        if observed != expected:
            raise SystemExit(f"FAIL: digest mismatch for {rel}")
    print(
        json.dumps(
            {
                "file_count": len(entries),
                "manifest_sha256": sha256_file(MANIFEST),
                "status": "PASS",
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
