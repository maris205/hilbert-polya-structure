#!/usr/bin/env python3
"""Build the deterministic package manifest after strict hygiene checks."""

from __future__ import annotations

import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "SHA256SUMS.txt"
CACHE_NAMES = {"__pycache__"}
CACHE_SUFFIXES = {".pyc", ".pyo"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    files = []
    for path in sorted(ROOT.rglob("*"), key=lambda item: item.relative_to(ROOT).as_posix()):
        relative = path.relative_to(ROOT)
        if path == MANIFEST:
            continue
        if path.is_symlink():
            raise SystemExit(f"REFUSE symlink: {relative}")
        if any(part in CACHE_NAMES for part in relative.parts) or path.suffix in CACHE_SUFFIXES:
            raise SystemExit(f"REFUSE cache: {relative}")
        if path.is_dir():
            continue
        if not path.is_file():
            raise SystemExit(f"REFUSE nonregular entry: {relative}")
        files.append(path)
    lines = [f"{sha256(path)}  {path.relative_to(ROOT).as_posix()}" for path in files]
    MANIFEST.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"WROTE {MANIFEST.name} WITH {len(files)} ENTRIES")


if __name__ == "__main__":
    main()
