#!/usr/bin/env python3
"""Write or verify the frozen HCS-C30 artifact hash manifest."""

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
EXCLUDED_FILENAMES = {".DS_Store", ".env"}
PAPER_SECTION_RELATIVE_PATHS = {
    "paper/sections/0_abstract.tex",
    "paper/sections/1_introduction.tex",
    "paper/sections/2_setting.tex",
    "paper/sections/3_cone_obstruction.tex",
    "paper/sections/4_roof_and_repetition.tex",
    "paper/sections/5_operator_and_flat_trace.tex",
    "paper/sections/6_group_trace_control.tex",
    "paper/sections/7_route_a_and_pivot.tex",
    "paper/sections/8_conclusion.tex",
    "paper/sections/A_certificate_protocol.tex",
    "paper/sections/B_scope_table.tex",
}
REQUIRED_RELATIVE_PATHS = {
    "README.md",
    "RESEARCH_QUESTION.md",
    "METHODOLOGY_BLUEPRINT.md",
    "DERIVATION_PACKAGE.md",
    "DEVILS_ADVOCATE_CHECKPOINT1.md",
    "FINAL_CHECKPOINT.md",
    "SOURCE_BOUNDARY.md",
    "SOURCE_VERIFICATION.md",
    "THEOREM_PACKAGE.md",
    "route_a_evaluation.yaml",
    "code/README.md",
    "code/c30_producer.py",
    "code/c30_independent_check.py",
    "code/test_c30.py",
    "code/c30_hash_manifest.py",
    "code/run_c30.sh",
    "evaluations/route_a/hcs_c30/20260811T183000Z.yaml",
    "paper/README.md",
    "paper/main.tex",
    "paper/main.pdf",
    "paper/COMPILATION_REPORT.md",
    "paper/references.bib",
    "results/README.md",
    "results/RESULTS.md",
    "results/VALIDATION_REPORT.md",
    "results/TEST_REPORT.md",
    "results/MATERIAL_PASSPORTS.md",
    "results/c30_certificate.json",
    "results/c30_independent_check.json",
    *PAPER_SECTION_RELATIVE_PATHS,
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    return parser.parse_args()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tracked_files() -> list[Path]:
    missing = sorted(
        relative
        for relative in REQUIRED_RELATIVE_PATHS
        if not (PROJECT / relative).is_file()
    )
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
    args = parse_args()
    expected = render()
    if args.write:
        MANIFEST.parent.mkdir(parents=True, exist_ok=True)
        MANIFEST.write_text(expected, encoding="utf-8")
        print(
            f"wrote {MANIFEST.relative_to(PROJECT)} "
            f"with {len(tracked_files())} entries"
        )
        return
    if not MANIFEST.exists():
        raise SystemExit(
            "manifest missing; use --write only for an intentional release update"
        )
    if MANIFEST.read_text(encoding="utf-8") != expected:
        raise SystemExit("artifact hash manifest mismatch")
    print(f"verified {len(tracked_files())} artifact hashes")


if __name__ == "__main__":
    main()
