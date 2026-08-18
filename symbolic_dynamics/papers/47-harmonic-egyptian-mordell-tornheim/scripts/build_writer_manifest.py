#!/usr/bin/env python3
"""Build or verify the exact acyclic P47 writer-content manifest."""

from __future__ import annotations

import argparse
import hashlib
import os
import stat
from pathlib import Path


HEADER = "relative_path\tmode\tsize\tsha256\n"
EXCLUDED_CLOSURE = {
    "HANDOFF.md",
    "PAPER_MANIFEST.tsv",
    "WRITER_REPORT.md",
    "WRITER_SEAL.json",
}
EXPECTED_CONTENT = {
    "CLAIMS_EVIDENCE.md",
    "PAPER_IMPROVEMENT_LOG.md",
    "PAPER_IMPROVEMENT_STATE.json",
    "PAPER_PLAN.md",
    "PROTECTED_STATEA_TREE.tsv",
    "STATIC_INPUT_SHA256SUMS.txt",
    "abstract.tex",
    "appendices/A_arithmetic_details.tex",
    "appendices/B_operator_details.tex",
    "appendices/C_determinants_walks.tex",
    "appendices/D_canonical_replay.tex",
    "evidence/CANONICAL_RESULTS_LEDGER.md",
    "evidence/FINAL_BIBLIOGRAPHY.bbl",
    "evidence/FINAL_COMPILE.log",
    "evidence/PDF_QA.md",
    "evidence/PROTECTED_STATEA_REPLAY.json",
    "evidence/SOURCE_VERIFICATION.md",
    "figures/data/canonical_summary.json",
    "figures/fig1_two_coordinates.tex",
    "figures/fig2_phase_diagram.tex",
    "figures/fig3_mixed_cycle.tex",
    "figures/gen_canonical_table.py",
    "figures/generated/canonical_replay_table.tex",
    "figures/generated/theorem_phase_table.tex",
    "figures/latex_includes.tex",
    "main.pdf",
    "main.tex",
    "main_round0_original.pdf",
    "main_round1.pdf",
    "main_round2.pdf",
    "math_commands.tex",
    "preamble.tex",
    "references.bib",
    "reviews/PLAN_RECHECK_FINAL.md",
    "reviews/PLAN_REVIEW.md",
    "reviews/ROUND1_REVIEW_RAW.md",
    "reviews/ROUND2_REVIEW_RAW.md",
    "scripts/build_improvement_record.py",
    "scripts/build_paper.sh",
    "scripts/build_writer_manifest.py",
    "scripts/capture_protected_statea.py",
    "scripts/check_pdf_qa.py",
    "scripts/extract_canonical_results.py",
    "sections/01_introduction.tex",
    "sections/02_related_work.tex",
    "sections/03_graph_coordinates.tex",
    "sections/04_bounded_compact.tex",
    "sections/05_ideal_thresholds.tex",
    "sections/06_traces_determinants.tex",
    "sections/07_cycles_sign.tex",
    "sections/08_replay_limitations.tex",
}
FORBIDDEN_COMPONENTS = {
    ".git", ".mypy_cache", ".pytest_cache", ".ruff_cache", "__pycache__",
}
FORBIDDEN_SUFFIXES = {".aux", ".blg", ".fls", ".fdb_latexmk", ".pyc", ".pyo", ".synctex"}


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def parent_directories(paths: set[str]) -> set[str]:
    result = {"."}
    for relative in paths:
        parent = Path(relative).parent
        while parent != Path("."):
            result.add(parent.as_posix())
            parent = parent.parent
    return result


def inventory(root: Path, require_complete_closure: bool) -> bytes:
    metadata = os.lstat(root)
    if (
        not stat.S_ISDIR(metadata.st_mode)
        or stat.S_IMODE(metadata.st_mode) != 0o755
        or root.resolve(strict=True) != root
    ):
        raise SystemExit("ROOT_NOT_CANONICAL_DIRECTORY_0755")
    regular: set[str] = set()
    directories = {"."}
    for base, names, files in os.walk(root, topdown=True, followlinks=False):
        base_path = Path(base)
        for name in names:
            path = base_path / name
            relative = path.relative_to(root).as_posix()
            info = os.lstat(path)
            if name in FORBIDDEN_COMPONENTS:
                raise SystemExit(f"FORBIDDEN_COMPONENT:{relative}")
            if not stat.S_ISDIR(info.st_mode) or stat.S_IMODE(info.st_mode) != 0o755:
                raise SystemExit(f"DIRECTORY_NOT_0755:{relative}")
            directories.add(relative)
        for name in files:
            path = base_path / name
            relative = path.relative_to(root).as_posix()
            info = os.lstat(path)
            if name in FORBIDDEN_COMPONENTS or path.suffix in FORBIDDEN_SUFFIXES:
                raise SystemExit(f"FORBIDDEN_FILE:{relative}")
            if relative == "outputs" or relative.startswith("outputs/"):
                raise SystemExit(f"FORBIDDEN_OUTPUTS:{relative}")
            if relative.startswith("evidence/publication_gate/"):
                raise SystemExit(f"FORBIDDEN_PUBLICATION_GATE:{relative}")
            if not stat.S_ISREG(info.st_mode) or stat.S_IMODE(info.st_mode) != 0o644:
                raise SystemExit(f"REGULAR_NOT_0644:{relative}")
            regular.add(relative)
    unknown = regular - EXPECTED_CONTENT - EXCLUDED_CLOSURE
    missing = EXPECTED_CONTENT - regular
    if unknown:
        raise SystemExit("UNEXPECTED_REGULAR:" + ",".join(sorted(unknown)))
    if missing:
        raise SystemExit("MISSING_CONTENT:" + ",".join(sorted(missing)))
    closure_present = regular & EXCLUDED_CLOSURE
    if require_complete_closure:
        if closure_present != EXCLUDED_CLOSURE:
            raise SystemExit("INCOMPLETE_CLOSURE")
    elif closure_present:
        raise SystemExit("CLOSURE_PREEXISTS")
    expected_dirs = parent_directories(EXPECTED_CONTENT | EXCLUDED_CLOSURE)
    if directories != expected_dirs:
        raise SystemExit("DIRECTORY_CLOSURE_MISMATCH")
    rows = []
    for relative in sorted(EXPECTED_CONTENT):
        path = root / relative
        info = os.lstat(path)
        rows.append(f"{relative}\t0644\t{info.st_size}\t{digest(path)}\n")
    return (HEADER + "".join(rows)).encode("ascii")


def write_exclusive(path: Path, raw: bytes) -> None:
    descriptor = os.open(
        path,
        os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0),
        0o644,
    )
    try:
        os.fchmod(descriptor, 0o644)
        offset = 0
        while offset < len(raw):
            offset += os.write(descriptor, raw[offset:])
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def main() -> int:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--root", required=True)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--write", action="store_true")
    action.add_argument("--check", action="store_true")
    parser.add_argument("--assert-output-new", action="store_true")
    args = parser.parse_args()
    supplied = Path(args.root)
    if not supplied.is_absolute() or supplied.is_symlink():
        raise SystemExit("ROOT_MUST_BE_ABSOLUTE_NONSYMLINK")
    root = supplied.resolve(strict=True)
    expected = inventory(root, require_complete_closure=args.check)
    manifest = root / "PAPER_MANIFEST.tsv"
    if args.check:
        if not manifest.is_file() or manifest.read_bytes() != expected:
            raise SystemExit("MANIFEST_MISMATCH")
        print(
            f"PASS rows={len(EXPECTED_CONTENT)} "
            f"sha256={hashlib.sha256(expected).hexdigest()}"
        )
        return 0
    if not args.assert_output_new:
        raise SystemExit("EXCLUSIVE_OUTPUT_ASSERTION_REQUIRED")
    write_exclusive(manifest, expected)
    print(
        f"WROTE rows={len(EXPECTED_CONTENT)} "
        f"sha256={hashlib.sha256(expected).hexdigest()}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
