#!/usr/bin/env python3
"""Self-verifier for SHA256SUMS.txt and package hygiene."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "SHA256SUMS.txt"
LINE = re.compile(r"^([0-9a-f]{64})  ([^\n]+)$")
CACHE_NAMES = {"__pycache__"}
CACHE_SUFFIXES = {".pyc", ".pyo"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def main() -> None:
    if not MANIFEST.is_file() or MANIFEST.is_symlink():
        fail("missing or invalid SHA256SUMS.txt")

    listed: dict[str, str] = {}
    for number, line in enumerate(MANIFEST.read_text(encoding="utf-8").splitlines(), start=1):
        match = LINE.fullmatch(line)
        if not match:
            fail(f"malformed manifest line {number}")
        expected, name = match.groups()
        pure = PurePosixPath(name)
        if pure.is_absolute() or ".." in pure.parts or pure.as_posix() != name:
            fail(f"unsafe or noncanonical path on line {number}: {name}")
        if name in listed:
            fail(f"duplicate path: {name}")
        if any(part in CACHE_NAMES for part in pure.parts) or pure.suffix in CACHE_SUFFIXES:
            fail(f"cache path listed: {name}")
        listed[name] = expected

    actual: set[str] = set()
    symlink_count = 0
    nonregular_count = 0
    cache_count = 0
    for path in ROOT.rglob("*"):
        relative = path.relative_to(ROOT)
        name = relative.as_posix()
        if path.is_symlink():
            symlink_count += 1
            continue
        if any(part in CACHE_NAMES for part in relative.parts) or path.suffix in CACHE_SUFFIXES:
            cache_count += 1
        if path.is_dir():
            continue
        if not path.is_file():
            nonregular_count += 1
            continue
        if path != MANIFEST:
            actual.add(name)

    if symlink_count or nonregular_count or cache_count:
        fail(
            f"hygiene symlinks={symlink_count} nonregular={nonregular_count} caches={cache_count}"
        )
    if set(listed) != actual:
        fail(
            "manifest file-set mismatch; "
            f"missing={sorted(actual-set(listed))} extra={sorted(set(listed)-actual)}"
        )
    for name, expected in listed.items():
        path = ROOT / name
        observed = sha256(path)
        if observed != expected:
            fail(f"hash mismatch: {name}")

    result = {
        "cache_count": cache_count,
        "file_count": len(listed),
        "manifest_sha256": sha256(MANIFEST),
        "nonregular_count": nonregular_count,
        "result": "PASS",
        "symlink_count": symlink_count,
    }
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
