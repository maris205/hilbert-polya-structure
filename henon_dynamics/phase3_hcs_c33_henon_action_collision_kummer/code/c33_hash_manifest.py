#!/usr/bin/env python3
"""Write or verify the frozen HCS-C33 Phase-3 artifact manifest."""

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
PAPER_SECTIONS = {
    "paper/sections/0_abstract.tex",
    "paper/sections/1_introduction.tex",
    "paper/sections/2_prior_work.tex",
    "paper/sections/3_action_curve.tex",
    "paper/sections/4_node_galois.tex",
    "paper/sections/5_hill_kummer.tex",
    "paper/sections/6_controls_reproducibility.tex",
    "paper/sections/7_discussion.tex",
    "paper/sections/A_exact_ledgers.tex",
}
REQUIRED = {
    "README.md",
    "RESEARCH_QUESTION.md",
    "METHODOLOGY_BLUEPRINT.md",
    "DERIVATION_PACKAGE.md",
    "DEVILS_ADVOCATE_CHECKPOINT2.md",
    "EXACT_GATE_PROTOCOL.md",
    "NARRATIVE_REPORT.md",
    "PAPER_PLAN.md",
    "PHASE3_CHECKPOINT.md",
    "SOURCE_AUDIT.md",
    "THEOREM_PACKAGE.md",
    "route_a_evaluation.yaml",
    "evaluations/route_a/HCS-C33/20260812T113001Z.yaml",
    "code/README.md",
    "code/c33_kummer_producer.py",
    "code/c33_kummer_checker.py",
    "code/test_c33.py",
    "code/c33_hash_manifest.py",
    "code/run_c33.sh",
    "results/README.md",
    "results/RESULTS.md",
    "results/TEST_REPORT.md",
    "results/c33_kummer_certificate.json",
    "results/c33_kummer_independent_check.json",
    "paper/README.md",
    "paper/COMPILATION_REPORT.md",
    "paper/main.tex",
    "paper/math_commands.tex",
    "paper/references.bib",
    "paper/main.pdf",
    *PAPER_SECTIONS,
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    return parser.parse_args()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tracked_files() -> list[Path]:
    missing = sorted(relative for relative in REQUIRED if not (PROJECT / relative).is_file())
    if missing:
        raise SystemExit(f"required release artifacts missing: {', '.join(missing)}")

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
    options = parse_args()
    expected = render()
    if options.write:
        MANIFEST.parent.mkdir(parents=True, exist_ok=True)
        MANIFEST.write_text(expected, encoding="utf-8")
        print(f"wrote {MANIFEST.relative_to(PROJECT)} with {len(tracked_files())} entries")
        return
    if not MANIFEST.is_file():
        raise SystemExit(
            "manifest missing; use --write only for an intentional release refresh"
        )
    if MANIFEST.read_text(encoding="utf-8") != expected:
        raise SystemExit("HCS-C33 artifact hash manifest mismatch")
    print(f"verified {len(tracked_files())} HCS-C33 artifact hashes")


if __name__ == "__main__":
    main()
