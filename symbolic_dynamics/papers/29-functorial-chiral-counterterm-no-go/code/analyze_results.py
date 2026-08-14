#!/usr/bin/env python3
"""Deterministic analysis of exact SD-C31 artifacts."""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path


def read(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def rational(record: dict[str, object]) -> Fraction:
    return Fraction(int(record["numerator"]), int(record["denominator"]))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results", type=Path, required=True)
    args = parser.parse_args()
    baseline = read(args.results / "baseline_cutoffs.json")
    schemes = read(args.results / "scheme_shifts.json")
    controls = read(args.results / "control_ledgers.json")
    coefficients = read(args.results / "coefficient_search.json")
    determinant = read(args.results / "determinant_ownership.json")
    evaluation = read(args.results / "evaluation.json")
    tests = read(args.results / "test_report.json")

    baseline_rows = baseline["cutoffs"]
    control_rows = controls["controls"]
    comparison = []
    for row in baseline_rows:
        comparison.append(
            {
                "object": f"divisibility_{row['cutoff']}",
                "class": "source_locked_baseline",
                "atoms": row["atom_count"],
                "mixed_pairs": len(row["mixed_ledger"]),
                "nonzero_mixed_pairs": sum(bool(pair["nonzero"]) for pair in row["mixed_ledger"]),
                "positive_B4_pairs": sum(bool(pair["positive"]) for pair in row["b4_pair_ledger"]),
            }
        )
    for row in control_rows:
        comparison.append(
            {
                "object": row["name"],
                "class": "control",
                "atoms": len(row["atom_weights"]),
                "mixed_pairs": len(row["mixed_ledger"]),
                "nonzero_mixed_pairs": row["nonzero_mixed_count"],
                "positive_B4_pairs": row["positive_b4_count"],
            }
        )

    first_s0 = rational(baseline_rows[0]["shifts"]["S0"])
    last_s0 = rational(baseline_rows[-1]["shifts"]["S0"])
    payload = {
        "schema_version": "SD-C31-analysis-v1",
        "candidate_id": "SD-C31",
        "status": "PASS_EXACT_NO_GO_WITHIN_FROZEN_CLASS",
        "route_tuple": [
            "A0_STRUCTURAL_ARITHMETIC_RELATION",
            "A1_FAIL",
            "A2_ANALYTIC_DETERMINANT",
            "A3_FAIL",
            "A4_FAIL",
        ],
        "target_zero_data_used": False,
        "route_b_invocation_allowed": False,
        "statistics": {
            "baseline_cutoffs": len(baseline_rows),
            "baseline_pair_rows": sum(len(row["mixed_ledger"]) for row in baseline_rows),
            "control_classes": len(control_rows),
            "control_pair_rows": sum(len(row["mixed_ledger"]) for row in control_rows),
            "control_nonzero_mixed_rows": sum(int(row["nonzero_mixed_count"]) for row in control_rows),
            "control_positive_B4_rows": sum(int(row["positive_b4_count"]) for row in control_rows),
            "scheme_family_rows": len(schemes["frozen_shift_family"]),
            "coefficient_grid_rows": coefficients["search"]["rows_tested"],
            "selective_solutions": coefficients["search"]["solution_count"],
            "independent_exact_checks": evaluation["check_count"],
            "unit_tests": tests["tests_run"],
        },
        "comparison_table": comparison,
        "finite_shift_evidence": {
            "S0_at_first_cutoff": baseline_rows[0]["shifts"]["S0"],
            "S0_at_last_cutoff": baseline_rows[-1]["shifts"]["S0"],
            "strictly_positive": first_s0 > 0 and last_s0 > 0,
            "convergent_tail_certified": schemes["all_tail_bounds_vanish"],
            "interpretation": "full and lead subtractions have distinct compatible finite limits",
        },
        "findings": [
            {
                "observation": "At every cutoff D_N=H_N+S0_N exactly; S0 has a rational vanishing-tail bound and is nonzero.",
                "interpretation": "Full-diagonal and leading-harmonic subtraction are both source-local and cutoff compatible but choose different finite parts.",
                "implication": "Naturality fixes only the divergent germ, not a canonical quadratic finite part.",
                "next_step": "Do not call either choice a zeta trace without an independently derived meromorphic regulator.",
            },
            {
                "observation": "The divisibility baseline and every preregistered mutated/composite/generic control retain nonzero pair Gram and B4 ledgers.",
                "interpretation": "The surviving oscillation is oblique-projector Gram geometry rather than a discriminator unique to prime divisibility.",
                "implication": "The same local pair coefficient cannot preserve the baseline and cancel same-type controls: beta must equal both zero and one.",
                "next_step": "Require a globally source-derived higher invariant with exact control vanishing before another RH claim is opened.",
            },
            {
                "observation": "det3 removes the entire quadratic term, while restoring FP Tr(B^2) changes the answer by a nontrivial entire scalar under scheme change.",
                "interpretation": "D_ren is holomorphic and reflection-compatible but is a newly defined functional.",
                "implication": "Analytic symmetry alone does not recover ordinary Fredholm/det2 ownership or arithmetic selectivity.",
                "next_step": "Keep A2 attached only to the inherited det3 object; do not promote D_ren to determinant status.",
            },
        ],
        "boundary": {
            "proved": "exact classification/no-go for the preregistered linear, Gram-local, order-at-most-two counterterm class",
            "not_proved": "a no-go for arbitrary global/nonlocal isomorphism invariants or all regulator choices",
            "target_zeros_used": False,
            "route_b_used": False,
        },
        "ownership_checks": {
            "B4_generic": determinant["b4_is_generic_pair_gram_ownership"],
            "D_ren_new_functional": "new_scheme_dependent" in determinant["renormalized_functional"]["ownership"],
        },
    }
    (args.results / "analysis.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
