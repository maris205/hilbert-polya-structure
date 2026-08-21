#!/usr/bin/env python3
"""Build the self-excluding SHA-256 manifest for this frozen cross-audit."""

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


def main() -> None:
    records: list[tuple[str, pathlib.Path]] = []
    for root, dirnames, filenames in os.walk(ROOT, followlinks=False):
        root_path = pathlib.Path(root)
        for name in dirnames:
            path = root_path / name
            if path.is_symlink() or not stat.S_ISDIR(path.lstat().st_mode):
                raise SystemExit(f"forbidden directory entry: {path}")
            if name == "__pycache__":
                raise SystemExit(f"cache directory: {path}")
        for name in filenames:
            path = root_path / name
            relative = path.relative_to(ROOT).as_posix()
            if path == MANIFEST:
                continue
            if path.is_symlink() or not stat.S_ISREG(path.lstat().st_mode):
                raise SystemExit(f"forbidden file entry: {path}")
            if "__pycache__" in path.parts or name.endswith((".pyc", ".pyo")):
                raise SystemExit(f"cache artifact: {path}")
            records.append((relative, path))
    records.sort()
    MANIFEST.write_text(
        "".join(f"{digest(path)}  {relative}\n" for relative, path in records),
        encoding="utf-8",
    )
    print(f"entries={len(records)}")


if __name__ == "__main__":
    main()
