#!/usr/bin/env python3
"""Fail-closed artifact manifest for HCS-C37."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
MANIFEST = PROJECT / "results/ARTIFACT_HASHES.sha256"
REQUIRED = {
    "README.md",
    "RESEARCH_QUESTION.md",
    "METHODOLOGY_BLUEPRINT.md",
    "DERIVATION_PACKAGE.md",
    "THEOREM_PACKAGE.md",
    "DEVILS_ADVOCATE.md",
    "SOURCE_AUDIT.md",
    "EXPERIMENT_PLAN.md",
    "EXPERIMENT_TRACKER.md",
    "PAPER_PLAN.md",
    "NARRATIVE_REPORT.md",
    "route_a_evaluation.yaml",
    "code/README.md",
    "code/c37_homogeneous_index_producer.py",
    "code/c37_homogeneous_index_checker.py",
    "code/test_c37.py",
    "code/c37_hash_manifest.py",
    "code/run_c37.sh",
    "results/RESULTS.md",
    "results/TEST_REPORT.md",
    "results/c37_certificate.json",
    "results/c37_independent_check.json",
    "paper/main.tex",
    "paper/math_commands.tex",
    "paper/references.bib",
    "paper/README.md",
    "paper/sections/0_abstract.tex",
    "paper/sections/1_introduction.tex",
    "paper/sections/2_setup.tex",
    "paper/sections/3_trivialization.tex",
    "paper/sections/4_boundary_index.tex",
    "paper/sections/5_hardy.tex",
    "paper/sections/6_mellin_routea.tex",
    "paper/sections/7_conclusion.tex",
    "paper/sections/A_exact_bounds.tex",
    "paper/sections/B_reproducibility.tex",
    "paper/main.pdf",
    "paper/COMPILATION_REPORT.md",
    "evaluations/route_a/HCS-C37/20260813T120000Z.yaml",
}
EXCLUDED_NAMES = {
    "ARTIFACT_HASHES.sha256",
    "__pycache__",
    ".pytest_cache",
    ".DS_Store",
}
EXCLUDED_SUFFIXES = {
    ".aux",
    ".bbl",
    ".bcf",
    ".blg",
    ".fdb_latexmk",
    ".fls",
    ".log",
    ".out",
    ".pyc",
    ".run.xml",
    ".synctex.gz",
}


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def tracked_files() -> list[Path]:
    missing = sorted(relative for relative in REQUIRED if not (PROJECT / relative).is_file())
    if missing:
        raise SystemExit("required release artifacts missing: " + ", ".join(missing))
    files: list[Path] = []
    for path in PROJECT.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(PROJECT)
        if any(part in EXCLUDED_NAMES for part in relative.parts):
            continue
        if any(path.name.endswith(suffix) for suffix in EXCLUDED_SUFFIXES):
            continue
        files.append(relative)
    return sorted(files, key=lambda item: item.as_posix())


def expected_text() -> str:
    return "".join(
        f"{digest(PROJECT / relative)}  {relative.as_posix()}\n"
        for relative in tracked_files()
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    expected = expected_text()
    if args.write:
        MANIFEST.parent.mkdir(parents=True, exist_ok=True)
        MANIFEST.write_text(expected, encoding="utf-8")
        print(f"wrote {MANIFEST.relative_to(PROJECT)} with {len(tracked_files())} entries")
        return
    if not MANIFEST.is_file():
        raise SystemExit("artifact manifest missing")
    actual = MANIFEST.read_text(encoding="utf-8")
    if actual != expected:
        raise SystemExit("artifact manifest mismatch")
    print(f"verified {len(tracked_files())} HCS-C37 artifact hashes")


if __name__ == "__main__":
    main()
