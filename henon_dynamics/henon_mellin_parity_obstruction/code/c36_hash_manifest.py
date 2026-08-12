#!/usr/bin/env python3
"""Write or verify the frozen HCS-C36 artifact hash manifest."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
MANIFEST = PROJECT / "results" / "ARTIFACT_HASHES.sha256"
EXCLUDED_SUFFIXES = {
    ".aux",
    ".bbl",
    ".bcf",
    ".blg",
    ".fdb_latexmk",
    ".fls",
    ".log",
    ".out",
    ".toc",
    ".pyc",
    ".pyo",
    ".pyd",
}
EXCLUDED_COMPOUND_SUFFIXES = (".run.xml", ".synctex.gz")
EXCLUDED_DIRECTORIES = {
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".ipynb_checkpoints",
    ".venv",
    "venv",
    ".tox",
    "build",
}
EXCLUDED_FILENAMES = {".DS_Store", ".env", "compile.log"}
REQUIRED_CODE_RESULTS = {
    "README.md",
    "RESEARCH_QUESTION.md",
    "METHODOLOGY_BLUEPRINT.md",
    "EXPERIMENT_PLAN.md",
    "EXPERIMENT_TRACKER.md",
    "PAPER_PLAN.md",
    "NARRATIVE_REPORT.md",
    "THEOREM_PACKAGE.md",
    "DERIVATION_PACKAGE.md",
    "DEVILS_ADVOCATE.md",
    "SOURCE_AUDIT.md",
    "requirements.txt",
    "route_a_evaluation.yaml",
    "evaluations/route_a/HCS-C36/20260813T003000Z.yaml",
    "code/README.md",
    "code/c36_mellin_producer.py",
    "code/c36_mellin_checker.py",
    "code/test_c36.py",
    "code/c36_hash_manifest.py",
    "code/run_c36.sh",
    "results/RESULTS.md",
    "results/TEST_REPORT.md",
    "results/c36_certificate.json",
    "results/c36_independent_check.json",
    "paper/README.md",
    "paper/COMPILATION_REPORT.md",
    "paper/main.pdf",
    "paper/main.tex",
    "paper/math_commands.tex",
    "paper/references.bib",
    "paper/sections/0_abstract.tex",
    "paper/sections/1_introduction.tex",
    "paper/sections/2_context.tex",
    "paper/sections/3_symbol.tex",
    "paper/sections/4_certificate.tex",
    "paper/sections/5_operator_route_a.tex",
    "paper/sections/6_homogeneous_pivot.tex",
    "paper/sections/7_conclusion.tex",
    "paper/sections/A_majorant.tex",
    "paper/sections/B_reproducibility.tex",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tracked_files() -> list[Path]:
    missing = sorted(
        relative for relative in REQUIRED_CODE_RESULTS if not (PROJECT / relative).is_file()
    )
    if missing:
        raise SystemExit(f"required C36 artifacts missing: {', '.join(missing)}")
    files: list[Path] = []
    for path in PROJECT.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(PROJECT)
        if (
            path == MANIFEST
            or path.name in EXCLUDED_FILENAMES
            or path.name.startswith(".env.")
            or path.suffix in EXCLUDED_SUFFIXES
            or path.name.endswith(EXCLUDED_COMPOUND_SUFFIXES)
            or any(part in EXCLUDED_DIRECTORIES for part in relative.parts)
        ):
            continue
        files.append(path)
    return sorted(files, key=lambda item: item.relative_to(PROJECT).as_posix())


def render() -> str:
    return "".join(
        f"{sha256(path)}  {path.relative_to(PROJECT)}\n" for path in tracked_files()
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    options = parser.parse_args()
    expected = render()
    if options.write:
        MANIFEST.parent.mkdir(parents=True, exist_ok=True)
        MANIFEST.write_text(expected, encoding="utf-8")
        print(f"wrote {MANIFEST.relative_to(PROJECT)} with {len(tracked_files())} entries")
        return
    if not MANIFEST.is_file():
        raise SystemExit("manifest missing; use --write only for an intentional release refresh")
    if MANIFEST.read_text(encoding="utf-8") != expected:
        raise SystemExit("HCS-C36 artifact hash manifest mismatch")
    print(f"verified {len(tracked_files())} HCS-C36 artifact hashes")


if __name__ == "__main__":
    main()
