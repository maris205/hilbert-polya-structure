#!/usr/bin/env python3
"""Summarize SD-C34 exact artifacts and write O-I-I-N analysis."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


ROUTE_TUPLE = [
    "A0_STRUCTURAL_ARITHMETIC_RELATION",
    "A1_FAIL",
    "A2_ANALYTIC_DETERMINANT",
    "A3_FAIL",
    "A4_FAIL",
]


def rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def payload(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: object) -> None:
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results", type=Path, required=True)
    args = parser.parse_args()

    census = rows(args.results / "modulus_census.csv")
    clones = rows(args.results / "matched_clone.csv")
    random_controls = rows(args.results / "random_relation_controls.csv")
    diamonds = payload(args.results / "cross_modulus_diamonds.json")
    selector = rows(args.results / "static_selector_firewall.csv")
    evaluation = payload(args.results / "evaluation.json")
    fredholm = payload(args.results / "fredholm_ownership.json")
    primes = [row for row in census if row["evaluator_prime"] == "1"]
    composites = [row for row in census if row["evaluator_prime"] == "0"]

    summary = {
        "candidate_id": "SD-C34",
        "cutoff": 192,
        "trace_order": 8,
        "moduli": len(census),
        "prime_moduli": len(primes),
        "composite_moduli": len(composites),
        "static_defect_equivalence_passes": sum(int(row["static_defect_selects_prime"]) for row in census),
        "prime_recurrent_support_nonzero": sum(int(row["recurrent_support_nonzero"]) for row in primes),
        "composite_recurrent_support_nonzero": sum(int(row["recurrent_support_nonzero"]) for row in composites),
        "all_forward_actions_transitive": all(row["forward_component_size"] == row["state_count"] for row in census),
        "all_states_overlap_s_and_r_recurrence": all(row["overlap_state_count"] == row["state_count"] for row in census),
        "matched_clone_equal_rows": sum(int(row["exact_equal"]) for row in clones),
        "random_relation_controls": len(random_controls),
        "random_controls_recurrence_nonzero": sum(int(row["universal_recurrence_nonzero"]) for row in random_controls),
        "cross_modulus_nonbacktracking_diamonds": len(diamonds),
        "diamond_top_composites": sum(int(row["top_is_composite_evaluator"]) for row in diamonds),
        "bare_ufd_addition_control": "FAILS_SOURCE_LOCK_AT_2_EQ_1_PLUS_1",
        "route_tuple": ROUTE_TUPLE,
        "overall": "ROUTE_A_REJECTED",
        "route_b": "LOCKED",
        "branch_action": "CLOSE_EUCLIDEAN_PROJECTIVE_RESIDUE_RECURRENCE_BRANCH",
    }
    write_json(args.results / "summary.json", summary)

    largest = max(census, key=lambda row: int(row["state_count"]))
    analysis = {
        "candidate_id": "SD-C34",
        "schema_version": "SD-C34-analysis-v1",
        "status": "PASS_EXACT_PROJECTIVE_RECURRENCE_OBSTRUCTION",
        "route_tuple": ROUTE_TUPLE,
        "overall": "ROUTE_A_REJECTED",
        "route_b": "LOCKED",
        "statistics": {
            "moduli": len(census),
            "prime_moduli": len(primes),
            "prime_power_composites": evaluation["stratum_counts"]["prime_power"],
            "mixed_composites": evaluation["stratum_counts"]["mixed_composite"],
            "composite_recurrent_blocks": sum(int(row["recurrent_support_nonzero"]) for row in composites),
            "matched_clone_rows": len(clones),
            "full_addition_entries_checked": evaluation["full_addition_entries_checked"],
            "full_multiplication_entries_checked": evaluation["full_multiplication_entries_checked"],
            "projective_edges_checked": evaluation["projective_edges_checked"],
            "independent_checks": evaluation["check_count"],
            "random_relation_controls": len(random_controls),
            "cusp_diamonds": len(diamonds),
            "selector_firewall_rows": len(selector),
            "largest_state_count": int(largest["state_count"]),
            "largest_state_modulus": int(largest["modulus"]),
        },
        "findings": [
            {
                "observation": "All 191 static count rows agree with independent primality labels, but all 148 composite blocks retain recurrent support.",
                "interpretation": "The projective count is a static field diagnostic, whereas recurrence is generated universally by the modular presentation.",
                "implication": "Applying the static Boolean to delete blocks would be a completed terminal selector and cannot earn A1.",
                "next_step": "Require any future quotient to cancel universal cycles before arithmetic labels are evaluated.",
            },
            {
                "observation": "Every projective state participates in both S and R recurrence, and all 48 generic C2*C3 actions reproduce the same overlap.",
                "interpretation": "The nonterminal shared-state mechanism is real but belongs to the group presentation rather than to prime arithmetic.",
                "implication": "The primitive ledger fails A1 before roofs or determinants can help.",
                "next_step": "Test a source-natural cycle quotient against the same generic relation actions.",
            },
            {
                "observation": "All 31 cutoff-visible n-2n-6n-3n-n diamonds are nonbacktracking and have composite top modulus.",
                "interpretation": "Bidirectional cusp sharing converts the transient reduction skeleton into a universal composite mixed-cycle family.",
                "implication": "Cross-modulus recurrence strengthens interaction but worsens prime selectivity.",
                "next_step": "Annihilate cusp-diamond boundaries at chain level without consulting modulus labels.",
            },
            {
                "observation": "The uninduced operator owns an ordinary Fredholm determinant on Re(s)>2 with the original marker unchanged.",
                "interpretation": "Trace-class ownership is compatible with nonterminal shared recurrence in this architecture.",
                "implication": "A2 passes honestly, but the determinant encodes the already failed composite primitive ledger.",
                "next_step": "Preserve same-object determinant ownership only after a complete surviving cycle ledger is proved.",
            },
        ],
        "fredholm_ownership": fredholm,
        "target_zero_data_used": False,
        "route_b_invocation_allowed": False,
    }
    write_json(args.results / "analysis.json", analysis)
    print(json.dumps({"status": analysis["status"], "route_tuple": ROUTE_TUPLE}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
