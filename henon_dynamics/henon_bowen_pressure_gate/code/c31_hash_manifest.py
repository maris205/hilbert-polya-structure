#!/usr/bin/env python3
"""Write or verify the frozen HCS-C31 release artifact manifest."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
MANIFEST = PROJECT / "results" / "ARTIFACT_HASHES.sha256"
REQUIRED = {
    "README.md",
    "REPOSITORY_UPDATE.md",
    "RESEARCH_QUESTION.md",
    "METHODOLOGY_BLUEPRINT.md",
    "DEVILS_ADVOCATE.md",
    "PAPER_PLAN.md",
    "NARRATIVE_REPORT.md",
    "THEOREM_PACKAGE.md",
    "DERIVATION_PACKAGE.md",
    "SOURCE_AUDIT.md",
    "route_a_evaluation.yaml",
    "evaluations/route_a/HCS-C31/20260811T123751Z.yaml",
    "code/README.md",
    "code/c31_producer.py",
    "code/c31_independent_check.py",
    "code/test_c31.py",
    "code/c31_hash_manifest.py",
    "code/run_c31.sh",
    "results/README.md",
    "results/RESULTS.md",
    "results/VALIDATION_REPORT.md",
    "results/TEST_REPORT.md",
    "results/c31_certificate.json",
    "results/c31_independent_check.json",
    "paper/README.md",
    "paper/COMPILATION_REPORT.md",
    "paper/main.tex",
    "paper/math_commands.tex",
    "paper/references.bib",
    "paper/main.pdf",
    "paper/sections/0_abstract.tex",
    "paper/sections/1_introduction.tex",
    "paper/sections/2_context.tex",
    "paper/sections/3_survivor.tex",
    "paper/sections/4_roof.tex",
    "paper/sections/5_pressure_certificate.tex",
    "paper/sections/6_zeta_dimension.tex",
    "paper/sections/7_route_a_conclusion.tex",
    "paper/sections/A_interval_arithmetic.tex",
    "paper/sections/B_reproducibility.tex",
}


def args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    return parser.parse_args()


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def render() -> str:
    missing = sorted(relative for relative in REQUIRED if not (PROJECT / relative).is_file())
    if missing:
        raise SystemExit(f"required C31 artifacts missing: {', '.join(missing)}")
    return "".join(
        f"{digest(PROJECT / relative)}  {relative}\n" for relative in sorted(REQUIRED)
    )


def main() -> None:
    options = args()
    expected = render()
    if options.write:
        MANIFEST.parent.mkdir(parents=True, exist_ok=True)
        MANIFEST.write_text(expected, encoding="utf-8")
        print(f"wrote {MANIFEST.relative_to(PROJECT)} with {len(REQUIRED)} entries")
        return
    if not MANIFEST.is_file():
        raise SystemExit("C31 artifact manifest missing; use --write only for an intentional refresh")
    if MANIFEST.read_text(encoding="utf-8") != expected:
        raise SystemExit("C31 artifact hash manifest mismatch")
    print(f"verified {len(REQUIRED)} C31 artifact hashes")


if __name__ == "__main__":
    main()
