#!/usr/bin/env python3
"""Create or verify the last writer-owned closure node."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import stat
import subprocess
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SEAL = ROOT / "WRITER_SEAL.json"
PYTHON = str(Path(sys.executable).resolve())
SAFE_PATH = os.pathsep.join(
    [
        str(Path(PYTHON).parent),
        "/usr/local/bin",
        "/usr/bin",
        "/bin",
    ]
)
ACTIVE_STATUS = "HOLD_FOR_INDEPENDENT_WRITER_AUDIT"


def canonical(value: Any) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode("ascii")


def sha(path: Path) -> str:
    info = os.lstat(path)
    if not stat.S_ISREG(info.st_mode) or stat.S_IMODE(info.st_mode) != 0o644:
        raise RuntimeError(f"unsafe seal dependency: {path.name}")
    descriptor = os.open(path, os.O_RDONLY | os.O_NOFOLLOW)
    digest = hashlib.sha256()
    try:
        opened = os.fstat(descriptor)
        if not stat.S_ISREG(opened.st_mode) or stat.S_IMODE(opened.st_mode) != 0o644:
            raise RuntimeError(f"unsafe opened dependency: {path.name}")
        while chunk := os.read(descriptor, 1 << 20):
            digest.update(chunk)
    finally:
        os.close(descriptor)
    return digest.hexdigest()


def expected_bytes() -> bytes:
    clean_env = {
        "LANG": "C",
        "LC_ALL": "C",
        "PATH": SAFE_PATH,
        "PYTHONDONTWRITEBYTECODE": "1",
        "SOURCE_DATE_EPOCH": "1787270400",
        "TZ": "UTC",
    }
    clean_env.pop("PYTHONPATH", None)
    clean_env.pop("PYTHONHOME", None)
    subprocess.run(
        [PYTHON, "-I", "-B", str(ROOT / "tools/build_paper_manifest.py"), "--check"],
        check=True,
        capture_output=True,
        env=clean_env,
    )
    if (ROOT / "STATUS.txt").exists() or (ROOT / "STATUS.txt").is_symlink():
        raise RuntimeError("STATUS.txt must be absent from the overlay")
    for status_holder in (ROOT / "WRITER_REPORT.md", ROOT / "HANDOFF.md"):
        if f"`{ACTIVE_STATUS}`" not in status_holder.read_text(encoding="utf-8"):
            raise RuntimeError(f"active status missing from {status_holder.name}")
    dependencies = {
        "active_pdf_sha256": sha(ROOT / "main.pdf"),
        "handoff_sha256": sha(ROOT / "HANDOFF.md"),
        "independent_audit_anchors_sha256": sha(ROOT / "evidence/INDEPENDENT_AUDIT_ANCHORS.json"),
        "independent_replay_sha256": sha(ROOT / "evidence/INDEPENDENT_REPLAY.json"),
        "paper_manifest_sha256": sha(ROOT / "PAPER_MANIFEST.tsv"),
        "pdf_qa_sha256": sha(ROOT / "evidence/PDF_QA.json"),
        "protected_stagea_replay_sha256": sha(ROOT / "evidence/PROTECTED_STAGEA_REPLAY.json"),
        "protected_stagea_tree_sha256": sha(ROOT / "evidence/PROTECTED_STAGEA_TREE.tsv"),
        "replay_isolation_regression_sha256": sha(ROOT / "evidence/REPLAY_ISOLATION_REGRESSION.json"),
        "withdrawn_writer_anchors_sha256": sha(ROOT / "evidence/WITHDRAWN_WRITER_ANCHORS.json"),
        "writer_report_sha256": sha(ROOT / "WRITER_REPORT.md"),
    }
    if dependencies["active_pdf_sha256"] != "aa2a5df28cd7139d9e19aea9bb035cd03f5d787e36260d8a52ed2d33ead930a4":
        raise RuntimeError("active PDF anchor mismatch")
    files = 0
    directories = 1
    for path in ROOT.rglob("*"):
        info = os.lstat(path)
        if stat.S_ISDIR(info.st_mode) and not stat.S_ISLNK(info.st_mode):
            directories += 1
        elif stat.S_ISREG(info.st_mode):
            files += 1
        else:
            raise RuntimeError(f"nonregular overlay node: {path.relative_to(ROOT)}")
    if not SEAL.exists():
        files += 1
    value = {
        "payload": {
            "dependency_order": [
                "content_and_evidence",
                "PAPER_MANIFEST.tsv",
                "WRITER_REPORT.md",
                "HANDOFF.md",
                "WRITER_SEAL.json",
            ],
            "directory_count_including_root": directories,
            "file_count_including_seal": files,
            "hashes": dependencies,
            "manifest_exclusions": [
                "HANDOFF.md",
                "PAPER_MANIFEST.tsv",
                "WRITER_REPORT.md",
                "WRITER_SEAL.json",
            ],
            "status": ACTIVE_STATUS,
        },
        "schema": "p49-final-writer-seal-v1",
        "status": "SEALED",
    }
    return canonical(value)


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
    expected = expected_bytes()
    if args.write:
        exclusive_write(SEAL, expected)
    else:
        info = os.lstat(SEAL)
        if not stat.S_ISREG(info.st_mode) or stat.S_IMODE(info.st_mode) != 0o644:
            raise RuntimeError("unsafe writer seal")
        if SEAL.read_bytes() != expected:
            raise RuntimeError("writer seal mismatch")
    print(f"WRITER_SEAL_OK sha256={sha(SEAL)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
