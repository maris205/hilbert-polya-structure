#!/usr/bin/env python3
"""Emit the self-excluding recursive static path/kind/mode/hash manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import stat
import sys
from pathlib import Path
from typing import Any


EXCLUDED = {"PREOUTPUT_STATIC_SEAL.json", "STATIC_TREE_MANIFEST.json"}


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       separators=(",", ": ")) + "\n").encode("ascii")


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--root", required=True)
    args = parser.parse_args(); root = Path(args.root)
    if not root.is_absolute() or root.is_symlink() or not root.is_dir() \
            or root.resolve(strict=True) != root:
        raise ValueError("unsafe root")
    rows = []
    for path in root.rglob("*"):
        relative = path.relative_to(root).as_posix()
        if relative == "outputs" or relative.startswith("outputs/") or relative in EXCLUDED:
            continue
        metadata = os.lstat(path)
        if stat.S_ISLNK(metadata.st_mode): raise ValueError("symlink")
        mode = f"{stat.S_IMODE(metadata.st_mode):04o}"
        if stat.S_ISDIR(metadata.st_mode):
            rows.append({"kind": "directory", "mode": mode, "path": relative})
        elif stat.S_ISREG(metadata.st_mode):
            rows.append({"kind": "regular", "mode": mode, "path": relative,
                         "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
        else: raise ValueError("nonregular static node")
    rows.sort(key=lambda row: row["path"])
    sys.stdout.buffer.write(canonical({
        "payload": {"entry_count": len(rows),
                    "excluded_paths": ["PREOUTPUT_STATIC_SEAL.json", "STATIC_TREE_MANIFEST.json", "outputs"],
                    "rows": rows},
        "schema": "paper44-static-tree-manifest-v2", "status": "SEALED",
    }))
    return 0


if __name__ == "__main__": raise SystemExit(main())
