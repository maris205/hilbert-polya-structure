#!/usr/bin/env python3
"""Build or verify the self-excluding final overlay manifest."""

from __future__ import annotations

import argparse
import hashlib
import os
from pathlib import Path
import stat


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "PAPER_MANIFEST.tsv"
EXCLUDED = {
    "PAPER_MANIFEST.tsv",
    "WRITER_REPORT.md",
    "HANDOFF.md",
    "WRITER_SEAL.json",
}
FORBIDDEN_SUFFIXES = {".aux", ".blg", ".out", ".toc", ".synctex", ".pyc", ".pyo"}


def sha256(path: Path) -> str:
    descriptor = os.open(path, os.O_RDONLY | os.O_NOFOLLOW)
    digest = hashlib.sha256()
    try:
        info = os.fstat(descriptor)
        if not stat.S_ISREG(info.st_mode) or stat.S_IMODE(info.st_mode) != 0o644:
            raise RuntimeError(f"unsafe regular file: {path}")
        while chunk := os.read(descriptor, 1 << 20):
            digest.update(chunk)
    finally:
        os.close(descriptor)
    return digest.hexdigest()


def manifest_bytes() -> bytes:
    root_info = os.lstat(ROOT)
    if not stat.S_ISDIR(root_info.st_mode) or stat.S_ISLNK(root_info.st_mode):
        raise RuntimeError("unsafe overlay root")
    if stat.S_IMODE(root_info.st_mode) != 0o755:
        raise RuntimeError("overlay root mode is not 0755")
    rows = ["relative_path\tkind\tmode\tsize\tsha256", ".\tdirectory\t0755\t\t"]
    for path in sorted(ROOT.rglob("*"), key=lambda item: item.relative_to(ROOT).as_posix()):
        relative = path.relative_to(ROOT).as_posix()
        if relative in EXCLUDED:
            continue
        info = os.lstat(path)
        if stat.S_ISDIR(info.st_mode) and not stat.S_ISLNK(info.st_mode):
            if stat.S_IMODE(info.st_mode) != 0o755:
                raise RuntimeError(f"directory mode is not 0755: {relative}")
            rows.append(f"{relative}\tdirectory\t0755\t\t")
        elif stat.S_ISREG(info.st_mode):
            if stat.S_IMODE(info.st_mode) != 0o644:
                raise RuntimeError(f"file mode is not 0644: {relative}")
            if "__pycache__" in path.parts or path.suffix in FORBIDDEN_SUFFIXES:
                raise RuntimeError(f"cache/auxiliary artifact: {relative}")
            if path.suffix == ".log" and relative != "evidence/FINAL_COMPILE_NORMALIZED.log":
                raise RuntimeError(f"unapproved log artifact: {relative}")
            rows.append(f"{relative}\tregular\t0644\t{info.st_size}\t{sha256(path)}")
        else:
            raise RuntimeError(f"nonregular node: {relative}")
    return ("\n".join(rows) + "\n").encode("ascii")


def exclusive_write(path: Path, raw: bytes) -> None:
    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o644)
    try:
        os.write(descriptor, raw)
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def main() -> int:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = manifest_bytes()
    if args.write:
        exclusive_write(MANIFEST, expected)
    else:
        info = os.lstat(MANIFEST)
        if not stat.S_ISREG(info.st_mode) or stat.S_IMODE(info.st_mode) != 0o644:
            raise RuntimeError("unsafe manifest node")
        if MANIFEST.read_bytes() != expected:
            raise RuntimeError("manifest closure mismatch")
    count = len(expected.splitlines()) - 1
    print(f"PAPER_MANIFEST_OK entries={count} excluded={len(EXCLUDED)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
