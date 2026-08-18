#!/usr/bin/env python3
"""Build or verify the acyclic, self-excluding P45 writer manifest."""

from __future__ import annotations

import argparse
import hashlib
import os
import stat
import tempfile
from pathlib import Path


EXCLUDED_ROOT_FILES = {
    "HANDOFF.md",
    "PAPER_MANIFEST.tsv",
    "WRITER_REPORT.md",
    "WRITER_SEAL.json",
}
BANNED_DIR_NAMES = {"build", "__pycache__", ".pytest_cache", ".cache"}
BANNED_SUFFIXES = {
    ".aux",
    ".blg",
    ".fdb_latexmk",
    ".fls",
    ".out",
    ".pyc",
    ".synctex",
    ".toc",
}
HEADER = "relative_path\tmode\tsize\tsha256\n"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def inventory(root: Path) -> str:
    rows: list[str] = []
    for base, dirs, files in os.walk(root, topdown=True, followlinks=False):
        base_path = Path(base)
        for name in dirs:
            path = base_path / name
            rel = path.relative_to(root).as_posix()
            if name in BANNED_DIR_NAMES:
                raise SystemExit(f"BANNED_DIRECTORY:{rel}")
            info = path.lstat()
            if not stat.S_ISDIR(info.st_mode):
                raise SystemExit(f"NONREGULAR_DIRECTORY_ENTRY:{rel}")
        for name in files:
            path = base_path / name
            rel = path.relative_to(root).as_posix()
            if rel in EXCLUDED_ROOT_FILES:
                continue
            info = path.lstat()
            if not stat.S_ISREG(info.st_mode):
                raise SystemExit(f"NONREGULAR_FILE_ENTRY:{rel}")
            if path.suffix in BANNED_SUFFIXES:
                raise SystemExit(f"BANNED_BUILD_ARTIFACT:{rel}")
            mode = f"{stat.S_IMODE(info.st_mode):04o}"
            rows.append(f"{rel}\t{mode}\t{info.st_size}\t{sha256(path)}\n")
    return HEADER + "".join(sorted(rows))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--write", action="store_true")
    action.add_argument("--check", action="store_true")
    args = parser.parse_args()

    root = args.root.resolve()
    manifest = root / "PAPER_MANIFEST.tsv"
    expected = inventory(root).encode("utf-8")
    if args.check:
        if not manifest.is_file() or manifest.read_bytes() != expected:
            raise SystemExit("MANIFEST_MISMATCH")
        print(
            f"PASS rows={expected.count(bytes([10])) - 1} "
            f"sha256={hashlib.sha256(expected).hexdigest()}"
        )
        return

    descriptor, temporary = tempfile.mkstemp(prefix=".paper-manifest.", dir=root)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(expected)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(temporary, 0o644)
        os.replace(temporary, manifest)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)
    print(
        f"WROTE rows={expected.count(bytes([10])) - 1} "
        f"sha256={hashlib.sha256(expected).hexdigest()}"
    )


if __name__ == "__main__":
    main()
