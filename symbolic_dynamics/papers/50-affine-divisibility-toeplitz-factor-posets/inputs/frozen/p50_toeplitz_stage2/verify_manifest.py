#!/usr/bin/env python3
"""Verify the frozen Stage-2 file set, modes, and SHA-256 manifest."""

from __future__ import annotations

import hashlib
import json
import re
import stat
from pathlib import Path


ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "SHA256SUMS.txt"
LINE = re.compile(r"^([0-9a-f]{64})  ([^\0]+)$")
ALLOWED_SUFFIXES = {".json", ".md", ".py", ".txt"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def expected_mode(path: Path) -> int:
    return 0o755 if path.suffix == ".py" else 0o644


def collect_regular_files() -> dict[str, Path]:
    files: dict[str, Path] = {}
    for path in sorted(ROOT.rglob("*")):
        relative = path.relative_to(ROOT).as_posix()
        if path.is_symlink():
            raise AssertionError(f"symlink forbidden: {relative}")
        if path.is_dir():
            if path.name == "__pycache__" or path.name.lower() == "cache":
                raise AssertionError(f"cache directory forbidden: {relative}")
            continue
        if not path.is_file():
            raise AssertionError(f"nonregular package entry: {relative}")
        if path.name == MANIFEST.name:
            continue
        if path.suffix not in ALLOWED_SUFFIXES:
            raise AssertionError(f"unexpected file suffix: {relative}")
        if path.suffix in {".pyc", ".pyo"}:
            raise AssertionError(f"bytecode forbidden: {relative}")
        files[relative] = path
    return files


def parse_manifest() -> dict[str, str]:
    if not MANIFEST.is_file() or MANIFEST.is_symlink():
        raise AssertionError("SHA256SUMS.txt is missing or nonregular")
    lines = MANIFEST.read_text(encoding="utf-8").splitlines()
    if not lines:
        raise AssertionError("empty manifest")
    entries: dict[str, str] = {}
    for line in lines:
        match = LINE.fullmatch(line)
        if not match:
            raise AssertionError(f"malformed manifest line: {line!r}")
        digest, relative = match.groups()
        if relative in entries:
            raise AssertionError(f"duplicate manifest entry: {relative}")
        entries[relative] = digest
    if list(entries) != sorted(entries):
        raise AssertionError("manifest paths are not sorted")
    return entries


def main() -> None:
    files = collect_regular_files()
    entries = parse_manifest()
    if set(files) != set(entries):
        raise AssertionError(
            json.dumps(
                {
                    "missing_from_manifest": sorted(set(files) - set(entries)),
                    "missing_from_directory": sorted(set(entries) - set(files)),
                },
                sort_keys=True,
            )
        )
    manifest_mode = stat.S_IMODE(MANIFEST.stat().st_mode)
    if manifest_mode != 0o644:
        raise AssertionError(f"SHA256SUMS.txt mode {manifest_mode:o}, expected 644")
    for relative, path in files.items():
        actual = sha256(path)
        if actual != entries[relative]:
            raise AssertionError(f"hash mismatch: {relative}")
        mode = stat.S_IMODE(path.stat().st_mode)
        expected = expected_mode(path)
        if mode != expected:
            raise AssertionError(
                f"mode mismatch: {relative} has {mode:o}, expected {expected:o}"
            )
    print(
        json.dumps(
            {
                "file_count": len(files),
                "manifest_sha256": sha256(MANIFEST),
                "status": "PASS",
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
