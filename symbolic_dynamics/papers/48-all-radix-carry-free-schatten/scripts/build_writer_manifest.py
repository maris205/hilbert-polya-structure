#!/usr/bin/env python3
"""Build or verify Paper 48's exact self-excluding writer overlay."""

from __future__ import annotations

import argparse
import hashlib
import os
import stat
from pathlib import Path, PurePosixPath


CONTENT = (
    "CLAIMS_EVIDENCE.md",
    "IMPROVEMENT_LOG.md",
    "PAPER_PLAN.md",
    "PROTECTED_STATEA_TREE.tsv",
    "QA_REPORT.md",
    "STATIC_INPUT_SHA256SUMS.txt",
    "evidence/CANONICAL_RESULTS_LEDGER.md",
    "evidence/FINAL_BIBLIOGRAPHY.bbl",
    "evidence/FINAL_COMPILE.log",
    "evidence/PDF_QA.json",
    "evidence/PROTECTED_STATEA_REPLAY.json",
    "evidence/SOURCE_VERIFICATION.md",
    "figures/data/ASSET_DIGESTS.json",
    "figures/data/canonical_summary.json",
    "figures/generated/critical_surfaces.pdf",
    "figures/generated/critical_surfaces.png",
    "figures/tables/thresholds.tex",
    "figures/tables/validation_census.tex",
    "figures/tikz/mechanism_pipeline.tex",
    "figures/tikz/pinching_comparison.tex",
    "paper/CarryFreeRadixOperators.pdf",
    "paper/build.sh",
    "paper/macros.tex",
    "paper/main.tex",
    "paper/sections/01_introduction.tex",
    "paper/sections/02_related_work.tex",
    "paper/sections/03_digit_operator.tex",
    "paper/sections/04_shell_calculus.tex",
    "paper/sections/05_thresholds.tex",
    "paper/sections/06_traces_determinants_periods.tex",
    "paper/sections/07_validation.tex",
    "paper/sections/08_conclusion.tex",
    "paper/sections/a_digit_details.tex",
    "paper/sections/b_shell_bookkeeping.tex",
    "paper/sections/c_endpoint_and_determinant.tex",
    "paper/sections/d_reproducibility.tex",
    "references.bib",
    "reviews/MANUSCRIPT_PRECLOSURE_NONREGRESSION.md",
    "reviews/PAPER_REVIEW_ROUND1_RAW.md",
    "reviews/PAPER_REVIEW_ROUND1_RESPONSE.md",
    "reviews/PAPER_REVIEW_ROUND2_RAW.md",
    "reviews/PAPER_REVIEW_ROUND2_RESPONSE.md",
    "reviews/PLAN_RECHECK_FINAL.md",
    "reviews/PLAN_REVIEW_RAW.md",
    "reviews/PLAN_SELF_AUDIT.md",
    "scripts/build_writer_manifest.py",
    "scripts/capture_protected_statea.py",
    "scripts/check_pdf_qa.py",
    "scripts/extract_canonical_results.py",
    "scripts/generate_paper_assets.py",
)
EXCLUDED = ("HANDOFF.md", "PAPER_MANIFEST.tsv", "WRITER_REPORT.md", "WRITER_SEAL.json")
HEADER = "relative_path\tmode\tsize\tsha256\n"


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
    files: set[str] = set()
    directories = {"."}
    root_info = os.lstat(root)
    if not stat.S_ISDIR(root_info.st_mode) or stat.S_IMODE(root_info.st_mode) != 0o755:
        raise ValueError("overlay root must be a 0755 directory")
    for path in root.rglob("*"):
        relative = path.relative_to(root).as_posix()
        info = os.lstat(path)
        if stat.S_ISLNK(info.st_mode):
            raise ValueError(f"symlink forbidden: {relative}")
        if stat.S_ISDIR(info.st_mode):
            if stat.S_IMODE(info.st_mode) != 0o755:
                raise ValueError(f"directory mode: {relative}")
            directories.add(relative)
        elif stat.S_ISREG(info.st_mode):
            if stat.S_IMODE(info.st_mode) != 0o644:
                raise ValueError(f"regular-file mode: {relative}")
            files.add(relative)
        else:
            raise ValueError(f"nonregular node: {relative}")
    return files, directories


def manifest_bytes(root: Path) -> bytes:
    rows = [HEADER]
    for relative in CONTENT:
        path = root / relative
        if path.is_symlink() or not path.is_file():
            raise ValueError(f"missing content: {relative}")
        info = os.lstat(path)
        if stat.S_IMODE(info.st_mode) != 0o644:
            raise ValueError(f"content mode: {relative}")
        rows.append(f"{relative}\t0644\t{info.st_size}\t{sha(path)}\n")
    raw = "".join(rows).encode("ascii")
    if tuple(sorted(CONTENT)) != CONTENT or len(set(CONTENT)) != len(CONTENT):
        raise ValueError("internal content order/census")
    return raw


def reject_forbidden(files: set[str]) -> None:
    for relative in files:
        parts = PurePosixPath(relative).parts
        if "__pycache__" in parts or relative.endswith((".aux", ".blg", ".out")) \
                or relative.startswith("outputs/") \
                or relative.startswith("evidence/publication_gate/") \
                or ".git" in parts or relative == "README.md":
            raise ValueError(f"forbidden overlay path: {relative}")


def main() -> int:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--root", type=Path, required=True)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--record", action="store_true")
    action.add_argument("--check", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve(strict=True)
    files, directories = scan(root)
    reject_forbidden(files)
    expected_dirs = expected_directories()
    if directories != expected_dirs:
        raise ValueError(
            f"directory closure: missing={sorted(expected_dirs-directories)} "
            f"extra={sorted(directories-expected_dirs)}"
        )
    raw = manifest_bytes(root)
    manifest = root / "PAPER_MANIFEST.tsv"
    if args.record:
        if files != set(CONTENT):
            raise ValueError(
                f"pre-manifest file closure: missing={sorted(set(CONTENT)-files)} "
                f"extra={sorted(files-set(CONTENT))}"
            )
        if manifest.exists():
            raise ValueError("refuse to overwrite manifest")
        manifest.write_bytes(raw)
        print(f"RECORDED rows={len(CONTENT)} manifest_sha256={sha(manifest)}")
    else:
        expected_files = set(CONTENT + EXCLUDED)
        if files != expected_files:
            raise ValueError(
                f"final file closure: missing={sorted(expected_files-files)} "
                f"extra={sorted(files-expected_files)}"
            )
        if manifest.read_bytes() != raw:
            raise ValueError("manifest bytes")
        print(
            f"PASS content_rows={len(CONTENT)} final_files={len(files)} "
            f"directories={len(directories)} manifest_sha256={sha(manifest)}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
