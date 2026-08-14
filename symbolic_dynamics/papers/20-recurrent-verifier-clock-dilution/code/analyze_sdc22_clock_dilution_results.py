#!/usr/bin/env python3
"""Analyze SD-C22 artifacts and freeze its strict Route-A verdict."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    run = json.loads((RESULTS / "summary.json").read_text(encoding="utf-8"))
    oracle = json.loads(
        (RESULTS / "source_oracle_certificate.json").read_text(encoding="utf-8")
    )
    route_tuple = [
        "A0_STRUCTURAL_ARITHMETIC_RELATION",
        "A1_PASS_ANALYTIC",
        "A2_FAIL",
        "A3_FAIL",
        "A4_FAIL",
    ]
    route_rows = [
        {
            "layer": "A0",
            "verdict": route_tuple[0],
            "evidence_status": "PROVED",
            "strongest_gate": "expanded_Q_state_semiring_verifier",
            "strongest_failure": "universal_total_decider_compiler",
        },
        {
            "layer": "A1",
            "verdict": route_tuple[1],
            "evidence_status": "PROVED",
            "strongest_gate": "one_closed_verifier_cycle_per_prime_with_exact_total_roof",
            "strongest_failure": "raw_graph_step_marker_depends_on_runtime_length",
        },
        {
            "layer": "A2",
            "verdict": route_tuple[2],
            "evidence_status": "STOP_PROVED",
            "strongest_gate": "normally_convergent_combinatorial_orbit_product_on_Re_s_gt_1",
            "strongest_failure": "whole_adjacency_noncompact_and_outside_all_finite_Schatten_classes",
        },
        {
            "layer": "A3",
            "verdict": route_tuple[3],
            "evidence_status": "STOP_SCOPED",
            "strongest_gate": "unmarked_orbit_product_equals_inverse_zeta_on_Re_s_gt_1",
            "strongest_failure": "no_operator_continuation_completion_or_Weil_form",
        },
        {
            "layer": "A4",
            "verdict": route_tuple[4],
            "evidence_status": "STOP_SCOPED",
            "strongest_gate": "explicit_symbolic_vertex_operator",
            "strongest_failure": "no_natural_self_adjoint_unitary_or_scattering_lift",
        },
    ]
    write_csv(RESULTS / "route_gate_summary.csv", route_rows)

    scientific_gates = {
        "cycle_formula_matches_simulation": all(
            row["cycle_length"] == row["simulated_length"]
            for row in csv.DictReader(
                (RESULTS / "cycle_clock_ledger.csv").open(encoding="utf-8", newline="")
            )
        ),
        "contracted_acceptance_boundary": oracle["contracted_acceptance_boundary"],
        "explicit_quotient_states_no_oracle": oracle["no_oracle_pass"]
        and oracle["q_states_materialized"],
        "z_one_orbit_product_exact": run["z_one_exact_collapse"],
        "marked_return_firewall_exact": run["small_marked_determinants_differ"],
        "whole_operator_noncompact": not run["whole_operator"]["compact"],
        "ordinary_fredholm_absent": not run["whole_operator"][
            "ordinary_fredholm_determinant_exists"
        ],
        "universal_controls_exact": all(
            row["all_cycle_products_exact_by_construction"]
            for row in run["padded_decider_controls"]
        ),
    }
    payload = {
        "candidate_id": "SD-C22",
        "scientific_gates": scientific_gates,
        "route_tuple": route_tuple,
        "overall_verdict": "ROUTE_A_REJECTED",
        "stop_labels": [
            "CLOCK_DILUTION_OBSTRUCTION",
            "ESSENTIAL_UNIT_CIRCLE",
            "POINCARE_COLLAPSE",
            "SELECTOR_TAUTOLOGICAL",
            "PROVES_TOO_MUCH",
        ],
        "route_b_invocation_allowed": False,
        "target_zero_fields": {
            "training": "not_applicable; no_target_zero_evaluation",
            "validation": "not_applicable; no_target_zero_evaluation",
            "test": "not_applicable; no_target_zero_evaluation",
        },
        "target_zero_data_used": False,
        "claim_boundary": (
            "The closed expanded verifier has exact prime-cycle products, but every "
            "nonnegative exact-clock roof distribution makes its natural whole "
            "adjacency noncompact. The z=1 orbit product survives combinatorially; "
            "first return restores the diagonal Paper-04 operator only by contracting "
            "the verification clock."
        ),
    }
    if route_tuple != run["route_tuple"] or not all(scientific_gates.values()):
        raise AssertionError(json.dumps(payload, sort_keys=True))
    (RESULTS / "analysis_summary.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
