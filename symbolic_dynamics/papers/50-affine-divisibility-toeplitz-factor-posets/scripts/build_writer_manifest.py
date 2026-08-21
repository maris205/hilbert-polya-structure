#!/usr/bin/env python3
"""Build or verify the exact self-excluding P50 final writer overlay."""

from __future__ import annotations

import argparse
import hashlib
import os
import stat
from pathlib import Path, PurePosixPath


CONTENT = (
    "CITATION_LOCK.md",
    "CLAIMS_EVIDENCE.md",
    "PAPER_PLAN.md",
    "PROTECTED_STAGE0_SHA256SUMS.txt",
    "PROTECTED_STAGEA_TREE.tsv",
    "QA_REPORT.md",
    "WRITER_STATUS.json",
    "evidence/FINAL_BIBLIOGRAPHY.bbl",
    "evidence/FINAL_COMPILE.log",
    "evidence/FINAL_OVERLAY_REPLAY.json",
    "evidence/FRESH_AB_REPLAY.json",
    "evidence/INDEPENDENT_REPLAY_RECEIPT.json",
    "evidence/PDF_QA.json",
    "figures/diagnostic_receipt.json",
    "figures/fig1_mechanism.tex",
    "figures/fig2_constructive_split.tex",
    "figures/fig3_c4_poset.tex",
    "figures/gen_diagnostic_table.py",
    "figures/preview.tex",
    "figures/table1_owner_scope.tex",
    "figures/table2_diagnostics.tex",
    "inputs/frozen/p50_toeplitz_independent_audit/SHA256SUMS.txt",
    "inputs/frozen/p50_toeplitz_root_audit/AUDIT_RESULT.json",
    "inputs/frozen/p50_toeplitz_stage2/SHA256SUMS.txt",
    "paper/build_fixed.sh",
    "paper/main.pdf",
    "paper/main.tex",
    "paper/math_commands.tex",
    "paper/references.bib",
    "paper/sections/0_abstract.tex",
    "paper/sections/1_introduction.tex",
    "paper/sections/2_context.tex",
    "paper/sections/3_family.tex",
    "paper/sections/4_skeletons.tex",
    "paper/sections/5_factors.tex",
    "paper/sections/6_poset.tex",
    "paper/sections/7_examples.tex",
    "paper/sections/8_conclusion.tex",
    "paper/sections/A_boundary.tex",
    "paper/sections/B_reproducibility.tex",
    "scripts/build_writer_manifest.py",
    "scripts/capture_protected_statea.py",
    "scripts/check_c4_partitions.py",
    "scripts/check_pdf_qa.py",
    "scripts/replay_writer_overlay.py",
)
EXCLUDED = ("HANDOFF.md", "PAPER_MANIFEST.tsv", "WRITER_REPORT.md", "WRITER_SEAL.txt")
HEADER = "relative_path\tmode\tsize\tsha256\n"
CACHE_NAMES = {"__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}
FORBIDDEN_PARTS = {".git", "baseline_artifacts", "closure_replay", "history", "qa", "repair_history", "reviews", "rounds", "tmp"}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def expected_directories() -> set[str]:
    result = {"."}
    for relative in CONTENT + EXCLUDED:
        parent = PurePosixPath(relative).parent
        while parent.as_posix() != ".":
            result.add(parent.as_posix())
            parent = parent.parent
    return result


def scan(root: Path) -> tuple[set[str], set[str]]:
    metadata = os.lstat(root)
    if root.is_symlink() or not stat.S_ISDIR(metadata.st_mode) or stat.S_IMODE(metadata.st_mode) != 0o755:
        raise ValueError("overlay root must be an ordinary 0755 directory")
    files: set[str] = set()
    directories = {"."}
    for path in root.rglob("*"):
        relative = path.relative_to(root).as_posix()
        info = os.lstat(path)
        parts = PurePosixPath(relative).parts
        if path.name in CACHE_NAMES or path.suffix in {".pyc", ".pyo"} or any(part in FORBIDDEN_PARTS for part in parts):
            raise ValueError(f"forbidden path: {relative}")
        if path.name.lower().startswith("readme"):
            raise ValueError(f"README forbidden: {relative}")
        if stat.S_ISLNK(info.st_mode):
            raise ValueError(f"symlink forbidden: {relative}")
        if stat.S_ISDIR(info.st_mode):
            if stat.S_IMODE(info.st_mode) != 0o755:
                raise ValueError(f"directory mode: {relative}")
            directories.add(relative)
        elif stat.S_ISREG(info.st_mode):
            if stat.S_IMODE(info.st_mode) != 0o644:
                raise ValueError(f"file mode: {relative}")
            if path.suffix in {".aux", ".blg", ".out"}:
                raise ValueError(f"LaTeX auxiliary forbidden: {relative}")
            if path.suffix in {".log", ".bbl"} and not relative.startswith("evidence/FINAL_"):
                raise ValueError(f"nonfinal log/BBL forbidden: {relative}")
            files.add(relative)
        else:
            raise ValueError(f"nonregular node: {relative}")
    return files, directories


def manifest_bytes(root: Path) -> bytes:
    if tuple(sorted(CONTENT)) != CONTENT or len(CONTENT) != len(set(CONTENT)):
        raise ValueError("internal content ordering")
    lines = [HEADER]
    for relative in CONTENT:
        path = root / relative
        if path.is_symlink() or not path.is_file():
            raise ValueError(f"missing content: {relative}")
        metadata = os.lstat(path)
        if stat.S_IMODE(metadata.st_mode) != 0o644:
            raise ValueError(f"content mode: {relative}")
        lines.append(f"{relative}\t0644\t{metadata.st_size}\t{sha(path)}\n")
    return "".join(lines).encode("ascii")


def main() -> None:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--root", required=True, type=Path)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--record", action="store_true")
    action.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if not args.root.is_absolute() or args.root.is_symlink() or args.root.resolve(strict=True) != args.root:
        raise SystemExit("ROOT_INVALID")
    root = args.root
    files, directories = scan(root)
    wanted_directories = expected_directories()
    if directories != wanted_directories:
        raise SystemExit(f"DIRECTORY_CLOSURE missing={sorted(wanted_directories-directories)} extra={sorted(directories-wanted_directories)}")
    raw = manifest_bytes(root)
    manifest = root / "PAPER_MANIFEST.tsv"
    if args.record:
        if files != set(CONTENT) or os.path.lexists(manifest):
            raise SystemExit(f"PREMANIFEST_FILE_CLOSURE missing={sorted(set(CONTENT)-files)} extra={sorted(files-set(CONTENT))}")
        descriptor = os.open(manifest, os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0), 0o644)
        try:
            os.fchmod(descriptor, 0o644)
            offset = 0
            while offset < len(raw):
                offset += os.write(descriptor, raw[offset:])
            os.fsync(descriptor)
        finally:
            os.close(descriptor)
        print(f"RECORDED content_rows={len(CONTENT)} manifest_sha256={sha(manifest)}")
    else:
        expected_files = set(CONTENT + EXCLUDED)
        if files != expected_files or manifest.read_bytes() != raw:
            raise SystemExit(f"FINAL_FILE_CLOSURE missing={sorted(expected_files-files)} extra={sorted(files-expected_files)}")
        print(f"PASS content_rows={len(CONTENT)} final_files={len(files)} directories={len(directories)} manifest_sha256={sha(manifest)}")


if __name__ == "__main__":
    main()
