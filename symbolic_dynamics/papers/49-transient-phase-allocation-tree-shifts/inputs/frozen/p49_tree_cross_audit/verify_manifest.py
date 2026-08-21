#!/usr/bin/env python3
"""Verify hashes, file coverage, modes, and hygiene of the cross-audit."""

from __future__ import annotations

import hashlib
import os
import pathlib
import stat


ROOT = pathlib.Path(__file__).resolve().parent
MANIFEST = ROOT / "SHA256SUMS.txt"


def digest(path: pathlib.Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            value.update(block)
    return value.hexdigest()


def expected_mode(relative: str) -> int:
    return 0o755 if relative.endswith(".py") else 0o644


def main() -> None:
    if not MANIFEST.is_file() or MANIFEST.is_symlink():
        raise SystemExit("missing or invalid SHA256SUMS.txt")
    entries: dict[str, str] = {}
    for number, raw in enumerate(MANIFEST.read_text(encoding="utf-8").splitlines(), 1):
        fields = raw.split(maxsplit=1)
        if len(fields) != 2:
            raise SystemExit(f"bad manifest line {number}")
        checksum, relative = fields
        relative = relative.lstrip(" *")
        pure = pathlib.PurePosixPath(relative)
        if (len(checksum) != 64 or any(c not in "0123456789abcdef" for c in checksum)
                or pure.is_absolute() or relative != pure.as_posix()
                or "." in pure.parts or ".." in pure.parts or relative in entries):
            raise SystemExit(f"bad manifest entry at line {number}")
        entries[relative] = checksum

    actual: dict[str, pathlib.Path] = {}
    for root, dirnames, filenames in os.walk(ROOT, followlinks=False):
        root_path = pathlib.Path(root)
        for name in dirnames:
            path = root_path / name
            mode = path.lstat().st_mode
            if stat.S_ISLNK(mode) or not stat.S_ISDIR(mode):
                raise SystemExit(f"forbidden directory entry: {path}")
            if stat.S_IMODE(mode) != 0o755:
                raise SystemExit(f"bad directory mode: {path}")
            if name == "__pycache__":
                raise SystemExit(f"cache directory: {path}")
        for name in filenames:
            path = root_path / name
            relative = path.relative_to(ROOT).as_posix()
            mode = path.lstat().st_mode
            if stat.S_ISLNK(mode) or not stat.S_ISREG(mode):
                raise SystemExit(f"forbidden file entry: {path}")
            if "__pycache__" in path.parts or name.endswith((".pyc", ".pyo")):
                raise SystemExit(f"cache artifact: {path}")
            required = 0o644 if path == MANIFEST else expected_mode(relative)
            if stat.S_IMODE(mode) != required:
                raise SystemExit(f"bad file mode: {relative}")
            if path != MANIFEST:
                actual[relative] = path

    if set(entries) != set(actual):
        missing = sorted(set(actual) - set(entries))
        extra = sorted(set(entries) - set(actual))
        raise SystemExit(f"manifest coverage mismatch missing={missing} extra={extra}")
    for relative, checksum in entries.items():
        if digest(actual[relative]) != checksum:
            raise SystemExit(f"hash mismatch: {relative}")
    print(f"entries={len(entries)}")
    print(f"manifest_sha256={digest(MANIFEST)}")
    print("cache_count=0")
    print("symlink_count=0")
    print("nonregular_count=0")


if __name__ == "__main__":
    main()
