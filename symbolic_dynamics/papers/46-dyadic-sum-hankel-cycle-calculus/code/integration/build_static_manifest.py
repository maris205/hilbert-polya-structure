#!/usr/bin/env python3
"""Build the C-sorted self-excluding P46 static-input manifest."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


STATIC_MANIFEST_SELF = "STATIC_INPUT_SHA256SUMS.txt"
PREOUTPUT_SEAL = "PREOUTPUT_STATIC_SEAL.json"
STATIC_MANIFEST_EXCLUSIONS = frozenset({STATIC_MANIFEST_SELF, PREOUTPUT_SEAL})


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    args = parser.parse_args()
    root = Path(args.root)
    if not root.is_absolute() or root.is_symlink() or not root.is_dir():
        raise ValueError("unsafe root")
    root = root.resolve(strict=True)
    rows = []
    for path in root.rglob("*"):
        relative = path.relative_to(root).as_posix()
        if relative.startswith("outputs/") or relative in STATIC_MANIFEST_EXCLUSIONS \
                or path.is_symlink() or not path.is_file():
            continue
        rows.append((relative, hashlib.sha256(path.read_bytes()).hexdigest()))
    rows.sort()
    names = [relative for relative, _ in rows]
    if len(names) != len(set(names)) or any(
            relative in STATIC_MANIFEST_EXCLUSIONS or relative.startswith("outputs/")
            for relative in names):
        raise ValueError("static manifest forbidden inclusion")
    raw = "".join(f"{digest}  {relative}\n" for relative, digest in rows).encode("ascii")
    (root / STATIC_MANIFEST_SELF).write_bytes(raw)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
