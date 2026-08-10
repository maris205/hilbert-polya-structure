#!/usr/bin/env python3
"""Write or verify the frozen SHA-256 release manifest for HCS-C27."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
OUTPUT = PROJECT / "results" / "ARTIFACT_HASHES.sha256"
ARTIFACTS = (
    "README.md",
    "RESEARCH_QUESTION.md",
    "EXPERIMENT_PLAN.md",
    "PAPER_PLAN.md",
    "NARRATIVE_REPORT.md",
    "THEOREM_PACKAGE.md",
    "SOURCE_AUDIT.md",
    "REPOSITORY_UPDATE.md",
    "requirements.txt",
    "route_a_evaluation.yaml",
    "evaluations/route_a/HCS-C27/20260810T074125Z.yaml",
    "code/README.md",
    "code/c27_producer.py",
    "code/c27_independent_check.py",
    "code/c27_hash_manifest.py",
    "code/test_c27.py",
    "code/run_c27.sh",
    "results/c27_certificate.json",
    "results/c27_independent_check.json",
    "results/README.md",
    "results/RESULTS.md",
    "results/VALIDATION_REPORT.md",
    "results/TEST_REPORT.md",
    "results/MATERIAL_PASSPORTS.md",
    "paper/COMPILATION_REPORT.md",
    "paper/main.pdf",
    "paper/main.tex",
    "paper/math_commands.tex",
    "paper/references.bib",
    "paper/sections/0_abstract.tex",
    "paper/sections/1_introduction.tex",
    "paper/sections/2_related_work.tex",
    "paper/sections/3_source_lock.tex",
    "paper/sections/4_finite_weil.tex",
    "paper/sections/5_fredholm.tex",
    "paper/sections/6_exact_results.tex",
    "paper/sections/7_conjugacy_obstruction.tex",
    "paper/sections/8_route_a.tex",
    "paper/sections/9_conclusion.tex",
    "paper/sections/A_appendix.tex",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write",
        action="store_true",
        help="replace the manifest after an intentional release update; default is read-only verification",
    )
    return parser.parse_args()


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def expected_payload() -> str:
    missing = [relative for relative in ARTIFACTS if not (PROJECT / relative).is_file()]
    if missing:
        raise SystemExit(f"refusing incomplete manifest; missing: {missing}")
    return "\n".join(f"{digest(PROJECT / relative)}  {relative}" for relative in ARTIFACTS) + "\n"


def main() -> None:
    args = parse_args()
    expected = expected_payload()
    if args.write:
        OUTPUT.write_text(expected, encoding="utf-8")
        print(f"wrote frozen {OUTPUT} with {len(ARTIFACTS)} artifacts")
        return
    if not OUTPUT.is_file():
        raise SystemExit("frozen manifest is missing; release preparation requires --write")
    observed = OUTPUT.read_text(encoding="utf-8")
    if observed != expected:
        raise SystemExit(
            "frozen manifest mismatch; inspect the changed artifacts and use --write only for an intentional release update"
        )
    print(f"verified frozen {OUTPUT} with {len(ARTIFACTS)} artifacts")


if __name__ == "__main__":
    main()
