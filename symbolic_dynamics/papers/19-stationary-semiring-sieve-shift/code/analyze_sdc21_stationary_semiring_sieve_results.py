#!/usr/bin/env python3
"""Analyze deterministic SD-C21 artifacts and freeze the strict Route tuple."""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Sequence


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"


def write_csv(path: Path, fieldnames: Sequence[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(fieldnames), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    run = json.loads((RESULTS / "run_summary.json").read_text(encoding="utf-8"))
    oracle = json.loads((RESULTS / "source_oracle_certificate.json").read_text(encoding="utf-8"))

    support_exact = all(row["exact"] for row in run["support_rows"])
    trace_exact = all(row["exact"] for row in run["finite_graph"]["trace_rows"])
    determinant_exact = run["finite_graph"]["determinant_exact"]
    recurrent_exact = run["finite_graph"]["recurrent_exact_accept_loops"]
    decider_exact = all(
        row["recurrent_exact"] and row["determinant_exact"]
        for row in run["universal_decider_controls"]
    )
    polynomial_exact = run["polynomial_ufd_control"]["exact"]
    no_oracle = oracle["no_oracle_pass"]

    route_rows = [
        {
            "layer": "A0",
            "verdict": "A0_STRUCTURAL_ARITHMETIC_RELATION",
            "evidence_status": "PROVED",
            "strongest_gate": "explicit_Q_state_semiring_verifier",
            "strongest_failure": "universal_total_decider_compiler",
        },
        {
            "layer": "A1",
            "verdict": "A1_PASS_ANALYTIC",
            "evidence_status": "PROVED",
            "strongest_gate": "one_primitive_loop_per_prime_and_exact_repetitions",
            "strongest_failure": "periodic_core_prunes_to_diagonal_loops",
        },
        {
            "layer": "A2",
            "verdict": "A2_ANALYTIC_DETERMINANT",
            "evidence_status": "PROVED",
            "strongest_gate": "trace_class_whole_operator_and_inverse_zeta_on_Re_s_gt_1",
            "strongest_failure": "no_dynamical_continuation_beyond_absolute_domain",
        },
        {
            "layer": "A3",
            "verdict": "A3_FAIL",
            "evidence_status": "STOP_SCOPED",
            "strongest_gate": "S1_holomorphy_on_Re_s_gt_1",
            "strongest_failure": "no_completion_functional_equation_counting_law_or_Weil_form",
        },
        {
            "layer": "A4",
            "verdict": "A4_FAIL",
            "evidence_status": "STOP_SCOPED",
            "strongest_gate": "single_symbolic_weighted_adjacency",
            "strongest_failure": "no_natural_operator_lift_and_diagonal_recurrent_core",
        },
    ]
    write_csv(
        RESULTS / "route_gate_summary.csv",
        ("layer", "verdict", "evidence_status", "strongest_gate", "strongest_failure"),
        route_rows,
    )

    control_rows = [
        {
            "control": "transported_semiring_presentation",
            "expected_behavior": "invariant",
            "observed_pass": run["transported_shuffle"]["accepted_decoded"]
            == [
                n for n in range(2, 513)
                if all(n % d for d in range(2, int(n**0.5) + 1))
            ],
            "interpretation": "presentation_invariance",
        },
        {
            "control": "entropy_shuffle",
            "expected_behavior": "break",
            "observed_pass": not run["entropy_shuffle_control"]["exact_target"],
            "interpretation": "clock_object_compatibility_required",
        },
        {
            "control": "additive_only",
            "expected_behavior": "break",
            "observed_pass": not run["additive_only_control"]["exact_target"],
            "interpretation": "tensor_product_required",
        },
        {
            "control": "bounded_trial_depth",
            "expected_behavior": "break",
            "observed_pass": all(row["false_positive_count"] > 0 for row in run["bounded_depth_controls"]),
            "interpretation": "complete_verification_required",
        },
        {
            "control": "shifted_factor_target",
            "expected_behavior": "break",
            "observed_pass": run["shifted_factor_control"]["symmetric_difference"] > 0,
            "interpretation": "neighboring_predicate_separates",
        },
        {
            "control": "polynomial_UFD",
            "expected_behavior": "compiler_reproduces_Euler_product",
            "observed_pass": polynomial_exact,
            "interpretation": "PROVES_TOO_MUCH",
        },
        {
            "control": "arbitrary_total_deciders",
            "expected_behavior": "compiler_reproduces_any_decidable_support",
            "observed_pass": decider_exact,
            "interpretation": "SELECTOR_TAUTOLOGICAL",
        },
    ]
    write_csv(
        RESULTS / "control_comparison_table.csv",
        ("control", "expected_behavior", "observed_pass", "interpretation"),
        control_rows,
    )

    payload = {
        "candidate_id": "SD-C21",
        "scientific_gates": {
            "support_exact_all_cutoffs": support_exact,
            "explicit_quotient_states_no_oracle": no_oracle,
            "recurrent_core_exact_accept_loops": recurrent_exact,
            "power_traces_exact": trace_exact,
            "finite_determinant_exact": determinant_exact,
            "polynomial_ufd_compiler_exact": polynomial_exact,
            "universal_total_decider_compiler_exact": decider_exact,
        },
        "route_tuple": [
            "A0_STRUCTURAL_ARITHMETIC_RELATION",
            "A1_PASS_ANALYTIC",
            "A2_ANALYTIC_DETERMINANT",
            "A3_FAIL",
            "A4_FAIL",
        ],
        "overall_verdict": "ROUTE_A_REJECTED",
        "stop_labels": [
            "SELECTOR_TAUTOLOGICAL",
            "PRUNING_EQUIVALENT",
            "PROVES_TOO_MUCH",
        ],
        "route_b_invocation_allowed": False,
        "target_zero_fields": {
            "training": "not_applicable_no_target_zero_evaluation",
            "validation": "not_applicable_no_target_zero_evaluation",
            "test": "not_applicable_no_target_zero_evaluation",
        },
        "target_zero_data_used": False,
        "claim_boundary": (
            "The expanded semiring verifier has an exact primitive/repetition ledger and a "
            "same-operator Fredholm-Euler identity on Re(s)>1. Its computation is transient, "
            "its periodic core is pruning-equivalent to diagonal accepted loops, and the "
            "universal total-decider wrapper compiles arbitrary decidable supports."
        ),
    }
    if not all(payload["scientific_gates"].values()):
        raise AssertionError(json.dumps(payload, sort_keys=True))
    if not all(row["observed_pass"] for row in control_rows):
        raise AssertionError(json.dumps(control_rows, sort_keys=True))
    (RESULTS / "analysis_summary.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
