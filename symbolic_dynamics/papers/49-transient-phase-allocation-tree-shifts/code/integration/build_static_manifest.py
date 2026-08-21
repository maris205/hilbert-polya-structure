#!/usr/bin/env python3
"""Build the self-excluding static path/type/mode/content manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import stat
from pathlib import Path
from typing import Any


EXCLUDED = {"PREOUTPUT_SEAL.txt", "STATIC_MANIFEST.json"}
CACHES = {"__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}
ANCHORS = ("STATIC_MANIFEST.json", "PREOUTPUT_SEAL.txt")


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True) + "\n").encode("ascii")


def digest(path: Path) -> str:
    answer = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            answer.update(block)
    return answer.hexdigest()


def require_root_and_anchors(root: Path) -> None:
    if not root.is_absolute():
        raise ValueError("unsafe root path")
    metadata = os.lstat(root)
    if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISDIR(metadata.st_mode) or stat.S_IMODE(metadata.st_mode) != 0o755:
        raise ValueError("unsafe root node")
    if root.resolve(strict=True) != root:
        raise ValueError("unsafe root resolution")
    for name in ANCHORS:
        metadata = os.lstat(root / name)
        if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode) or stat.S_IMODE(metadata.st_mode) != 0o644:
            raise ValueError("unsafe excluded anchor")


def overwrite_regular(path: Path, payload: bytes) -> None:
    if not hasattr(os, "O_NOFOLLOW"):
        raise ValueError("O_NOFOLLOW unavailable")
    descriptor = os.open(path, os.O_WRONLY | os.O_NOFOLLOW)
    try:
        metadata = os.fstat(descriptor)
        if not stat.S_ISREG(metadata.st_mode) or stat.S_IMODE(metadata.st_mode) != 0o644:
            raise ValueError("unsafe manifest target")
        os.ftruncate(descriptor, 0)
        with os.fdopen(descriptor, "wb") as handle:
            descriptor = -1
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
    finally:
        if descriptor >= 0:
            os.close(descriptor)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    root = Path(args.root)
    require_root_and_anchors(root)
    try:
        os.lstat(root / "outputs")
    except FileNotFoundError:
        pass
    else:
        raise ValueError("preoutput manifest cannot be built with outputs present")
    contract = json.loads((root / "contracts" / "PROJECT_CONTRACT.json").read_text(encoding="utf-8"))
    rows = []
    for path in sorted(root.rglob("*"), key=lambda item: item.relative_to(root).as_posix()):
        rel = path.relative_to(root).as_posix()
        if rel in EXCLUDED or rel == "outputs" or rel.startswith("outputs/"):
            continue
        metadata = os.lstat(path)
        if path.name in CACHES or path.name.endswith((".pyc", ".pyo")):
            raise ValueError(f"cache: {rel}")
        upper_name = path.name.upper()
        if path.name == ".git" or path.name in {"README", "README.md", "README.txt"} or path.suffix.lower() in {".pdf", ".tex"} or upper_name.startswith("PAPER_MANIFEST") or ("PUBLICATION" in upper_name and "SEAL" in upper_name):
            raise ValueError(f"forbidden static artifact: {rel}")
        if stat.S_ISLNK(metadata.st_mode):
            raise ValueError(f"symlink: {rel}")
        mode = f"{stat.S_IMODE(metadata.st_mode):04o}"
        if stat.S_ISDIR(metadata.st_mode):
            if mode != "0755":
                raise ValueError(f"directory mode: {rel}")
            rows.append({"kind": "directory", "mode": mode, "path": rel})
        elif stat.S_ISREG(metadata.st_mode):
            if mode != "0644":
                raise ValueError(f"file mode: {rel}")
            rows.append({"kind": "regular", "mode": mode, "path": rel, "sha256": digest(path), "size": metadata.st_size})
        else:
            raise ValueError(f"nonregular: {rel}")
    manifest = {
        "payload": {
            "entry_count": len(rows),
            "excluded": ["PREOUTPUT_SEAL.txt", "STATIC_MANIFEST.json", "outputs"],
            "project_slug": contract["project_slug"],
            "rows": rows,
        },
        "schema": "stage0-static-manifest-v1",
        "status": "SEALED",
    }
    payload = canonical(manifest)
    if args.write:
        target = root / "STATIC_MANIFEST.json"
        overwrite_regular(target, payload)
    else:
        print(payload.decode("ascii"), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
