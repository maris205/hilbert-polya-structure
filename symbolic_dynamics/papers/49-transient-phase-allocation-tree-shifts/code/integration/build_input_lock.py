#!/usr/bin/env python3
"""Build the exact regular-file lock for the copied immutable inputs."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import stat
from pathlib import Path
from typing import Any


FORBIDDEN_SUFFIXES = {".pdf", ".tex"}
FORBIDDEN_NAMES = {"README", "README.md", "README.txt"}
CACHE_NAMES = {"__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True) + "\n").encode("ascii")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def safe_root(raw: str) -> Path:
    root = Path(raw)
    if not root.is_absolute() or root.is_symlink() or not root.is_dir() or root.resolve(strict=True) != root:
        raise ValueError("unsafe root")
    return root


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    root = safe_root(args.root)
    inputs = root / "inputs"
    contract = json.loads((root / "contracts" / "PROJECT_CONTRACT.json").read_text(encoding="utf-8"))
    rows = []
    for path in sorted(inputs.rglob("*"), key=lambda item: item.relative_to(root).as_posix()):
        rel = path.relative_to(root).as_posix()
        metadata = os.lstat(path)
        name = path.name
        if name in CACHE_NAMES or name.endswith((".pyc", ".pyo")):
            raise ValueError(f"cache input: {rel}")
        if stat.S_ISLNK(metadata.st_mode):
            raise ValueError(f"symlink input: {rel}")
        if stat.S_ISDIR(metadata.st_mode):
            if stat.S_IMODE(metadata.st_mode) != 0o755:
                raise ValueError(f"input directory mode: {rel}")
            continue
        if not stat.S_ISREG(metadata.st_mode):
            raise ValueError(f"nonregular input: {rel}")
        if stat.S_IMODE(metadata.st_mode) != 0o644:
            raise ValueError(f"input file mode: {rel}")
        if path.suffix.lower() in FORBIDDEN_SUFFIXES or name in FORBIDDEN_NAMES or name.upper().startswith("PAPER_MANIFEST"):
            raise ValueError(f"forbidden input: {rel}")
        rows.append({"mode": "0644", "path": rel, "sha256": sha256(path), "size": metadata.st_size})
    result = {
        "entries": rows,
        "entry_count": len(rows),
        "project_slug": contract["project_slug"],
        "schema": "stage0-input-lock-v1",
        "upstream_roots": contract["upstream_roots"],
    }
    payload = canonical(result)
    if args.write:
        target = root / "contracts" / "INPUT_LOCK.json"
        target.write_bytes(payload)
        os.chmod(target, 0o644)
    else:
        print(payload.decode("ascii"), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
