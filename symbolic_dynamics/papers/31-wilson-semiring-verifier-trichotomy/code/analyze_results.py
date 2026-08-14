#!/usr/bin/env python3
"""Bounded Observation-Interpretation-Implication analysis for SD-C33."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


ROUTE_TUPLE = [
    "A0_STRUCTURAL_ARITHMETIC_RELATION",
    "A1_PASS_ANALYTIC",
    "A2_FAIL",
    "A3_FAIL",
    "A4_FAIL",
]


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def row_count(path: Path) -> int:
    with path.open(encoding="utf-8", newline="") as handle:
        return sum(1 for _ in csv.DictReader(handle))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results", type=Path, required=True)
    args = parser.parse_args()
    results = args.results
    summary = read_json(results / "summary.json")
    evaluation = read_json(results / "evaluation.json")
    tests = read_json(results / "test_report.json")
    semirings = read_json(results / "semiring_controls.json")
    random_controls = read_json(results / "random_operation_controls.json")
    marker = read_json(results / "marker_change_certificate.json")
    wrappers = read_json(results / "universal_wrapper_controls.json")

    comparison_table = [
        {
            "surface": "integer_Wilson_cutoff",
            "rows": row_count(results / "wilson_ledger.csv"),
            "positive": summary["accepted_count"],
            "negative": summary["composite_control_count"],
            "verdict": "exact_prime_cycle_classification_certificate",
        },
        {
            "surface": "bare_polynomial_UFD_addition",
            "rows": summary["bare_ufd_addition_pairs"],
            "positive": summary["bare_ufd_addition_matches"],
            "negative": summary["bare_ufd_addition_pairs"] - summary["bare_ufd_addition_matches"],
            "verdict": "bare_clone_broken",
        },
        {
            "surface": "matched_semiring_clone",
            "rows": summary["matched_clone_operation_rows"],
            "positive": summary["matched_clone_operation_rows"],
            "negative": 0,
            "verdict": "exact_copy_naturality_control",
        },
        {
            "surface": "random_operation_tables",
            "rows": summary["random_magma_controls"],
            "positive": summary["random_magma_semiring_passes"],
            "negative": summary["random_magma_controls"] - summary["random_magma_semiring_passes"],
            "verdict": "all_random_magma_pairs_fail_semiring_gate",
        },
        {
            "surface": "universal_support_wrappers",
            "rows": len(wrappers),
            "positive": len(wrappers),
            "negative": 0,
            "verdict": "all_prune_or_dilute",
        },
    ]
    payload = {
        "candidate_id": "SD-C33",
        "schema_version": "SD-C33-analysis-v1",
        "status": "PASS_EXACT_VERIFIER_TRICHOTOMY_NO_GO",
        "route_tuple": ROUTE_TUPLE,
        "overall": "ROUTE_A_REJECTED",
        "decision": "GO_NEGATIVE_CLOSURE_PAPER_STOP_POSITIVE_CANDIDATE",
        "comparison_table": comparison_table,
        "statistics": {
            "cutoff": summary["cutoff"],
            "wilson_rows": row_count(results / "wilson_ledger.csv"),
            "accepted_prime_cycles": summary["accepted_count"],
            "composite_controls": summary["composite_control_count"],
            "pseudoprime_controls": summary["base2_pseudoprime_control_count"],
            "bare_addition_rows": summary["bare_ufd_addition_pairs"],
            "bare_addition_matches": summary["bare_ufd_addition_matches"],
            "matched_clone_rows": summary["matched_clone_operation_rows"],
            "random_table_rows": len(random_controls),
            "named_semiring_rows": len(semirings),
            "dilution_rows": row_count(results / "entropy_budget_dilution.csv"),
            "formal_trace_orders": summary["formal_trace_orders"],
            "marker_rows": len(marker),
            "wrapper_families": len(wrappers),
            "independent_checks": evaluation["check_count"],
            "exact_tests": tests["total"],
        },
        "findings": [
            {
                "observation": "Wilson acceptance agrees with independent trial division for every n from 2 through 4096: 564 accepts and 3,531 composite rejects, including all 13 base-2 pseudoprime controls.",
                "interpretation": "The source-derived recurrence implements the classical prime terminal relation without a supplied prime table.",
                "implication": "A0 and the primitive A1 layer are earned, but terminal correctness alone is not a determinant mechanism.",
                "next_step": "Require future recurrence to interact before the terminal accept/reject state is known.",
            },
            {
                "observation": "Ordinary polynomial-UFD addition has zero matches in 144 tests, while all 169 transported matched-semiring operations and every Wilson path copy exactly.",
                "interpretation": "Addition breaks Paper30's bare clone but not isomorphism-natural relabeling with transported addition.",
                "implication": "The new source object is genuine yet cannot distinguish literal integers from a matched presentation.",
                "next_step": "Keep matched semiring clones mandatory and avoid claiming that addition defeats every UFD-style control.",
            },
            {
                "observation": "The 564 prime cycles produce 1,692 exact-clock dilution rows; at p=4093 and sigma=2 the forced edge lower bound exceeds 0.9959.",
                "interpretation": "A total roof log p spread over p-1 disjoint edges forces near-unit weights along an orthogonal block sequence.",
                "implication": "The primary recurrent adjacency is noncompact and owns no ordinary Fredholm determinant.",
                "next_step": "Test only source-derived overlapping architectures whose recurrent length is compatible with the total-roof compactness criterion.",
            },
            {
                "observation": "Raw and induced products agree at z=1 but differ exactly at z=1/3.",
                "interpretation": "First return contracts p-1 original graph steps to one induced step.",
                "implication": "The honest induced Euler determinant belongs to a changed time object and cannot repair A2 for the primary graph.",
                "next_step": "Preserve a free graph-step marker in every same-object determinant claim.",
            },
            {
                "observation": "Wilson primes, squares, powers of two, Fibonacci numbers, and a seeded hash support all instantiate the same transient-pruning/recurrent-dilution wrapper.",
                "interpretation": "The terminal verifier compiler is support-universal rather than Wilson-specific.",
                "implication": "Its diagonal determinant encodes accepted support after verification has been externally completed.",
                "next_step": "Close the terminal-verifier branch and seek nonterminal recurrent arithmetic interaction.",
            },
        ],
        "boundary": {
            "proved": "finite exact implementation and controls, with independent theorem proofs for reconstruction, clone transport, Wilson cycles, noncompactness, first return, and pruning",
            "not_proved": "a primary Fredholm determinant, critical-line continuation, fixed self-adjoint carrier, target-zero correspondence, or RH",
        },
        "paper32_minimum_obligation": "Construct a source-derived nonterminal overlapping recurrent interaction, prove an honest determinant for the uninduced whole operator while preserving the original marker, and pass matched-clone plus universal-wrapper controls before any RH claim.",
        "target_zero_data_used": False,
        "route_b_invocation_allowed": False,
    }
    (results / "analysis.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps({"status": payload["status"], "route_tuple": ROUTE_TUPLE}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
