#!/usr/bin/env python3
"""Analyze SD-C23 exact artifacts and freeze the strict Route-A verdict."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"


def read_csv(name: str) -> list[dict[str, str]]:
    with (RESULTS / name).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(rows[0]),
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    summary = json.loads((RESULTS / "summary.json").read_text(encoding="utf-8"))
    oracle = json.loads(
        (RESULTS / "source_oracle_certificate.json").read_text(encoding="utf-8")
    )
    unweighted = read_csv("unweighted_trace_primitive.csv")
    cutoff_flags = read_csv("trace_cutoff_flags.csv")
    confinement = read_csv("confinement_certificates.csv")
    determinants = read_csv("determinant_coefficients.csv")
    controls = read_csv("graph_controls.csv")
    route_tuple = [
        "A0_STRUCTURAL_ARITHMETIC_RELATION",
        "A1_WEAK",
        "A2_ANALYTIC_DETERMINANT",
        "A3_FAIL",
        "A4_FAIL",
    ]

    route_rows = [
        {
            "layer": "A0",
            "verdict": route_tuple[0],
            "evidence_status": "PROVED",
            "strongest_gate": "successor_factorization_relation_from_full_shift_semiring",
            "strongest_failure": "two_quotient_spine_has_zero_selectivity_margin",
        },
        {
            "layer": "A1",
            "verdict": route_tuple[1],
            "evidence_status": "PROVED_OBSTRUCTION",
            "strongest_gate": "exact_confined_primitive_rotation_ledger",
            "strongest_failure": "primitive_cycle_at_every_length_and_no_length_one_orbit",
        },
        {
            "layer": "A2",
            "verdict": route_tuple[2],
            "evidence_status": "PROVED",
            "strongest_gate": "whole_operator_trace_class_iff_Re_s_gt_one_half",
            "strongest_failure": "marked_first_coefficient_disagrees_with_prime_Euler_target",
        },
        {
            "layer": "A3",
            "verdict": route_tuple[3],
            "evidence_status": "STOP_SCOPED",
            "strongest_gate": "same_object_Fredholm_family_on_sharp_half_plane",
            "strongest_failure": "no_continuation_functional_equation_completion_or_Weil_form",
        },
        {
            "layer": "A4",
            "verdict": route_tuple[4],
            "evidence_status": "NOT_TESTABLE_STOP_SCOPED",
            "strongest_gate": "explicit_symbolic_vertex_operator",
            "strongest_failure": "no_natural_self_adjoint_unitary_or_scattering_lift",
        },
    ]
    write_csv(RESULTS / "route_gate_summary.csv", route_rows)

    spine = next(row for row in controls if row["variant"] == "q_1_2_spine")
    successor = next(row for row in controls if row["variant"] == "successor_only")
    scientific_gates = {
        "source_rule_and_no_oracle": (
            oracle["loop_count"] == 0
            and oracle["quotient_identity_mismatches"] == 0
            and oracle["target_feedback_used"] is False
        ),
        "sparse_trace_orders_1_to_32": (
            len(unweighted) == 32
            and [int(row["power"]) for row in unweighted] == list(range(1, 33))
        ),
        "cutoff_flags_exact": all(
            (row["exact_infinite_trace"] == "True")
            == (int(row["cutoff"]) >= int(row["certified_cutoff"]))
            for row in cutoff_flags
        ),
        "confinement_stabilization": all(
            row["stabilized_exactly"] == "True" for row in confinement
        ),
        "necklace_reconstruction_exact": all(
            row["rooted_closed_walks"] == row["necklace_reconstruction"]
            for row in unweighted
        ),
        "determinant_cross_method_exact": all(
            row["exact_match"] == "True" for row in determinants
        ),
        "first_trace_zero": summary["first_trace_zero"] is True,
        "canonical_all_length_flood": summary["canonical_cycles_all_pass"] is True,
        "two_quotient_spine_zero_margin": (
            spine["all_lengths_2_to_32"] == "True"
            and spine["control_margin_against_full_flood"] == "0"
        ),
        "successor_only_acyclic": successor["first_positive_length"] == "",
        "sharp_trace_class_theorem": summary["trace_class_iff"] == "Re(s)>1/2",
        "target_zero_data_absent": summary["target_zero_data_used"] is False,
    }
    payload = {
        "candidate_id": "SD-C23",
        "claim_boundary": (
            "The successor-divisor shift is a strongly connected mixing countable "
            "Markov system whose natural whole adjacency is trace class exactly on "
            "Re(s)>1/2 and has an exact Fredholm ledger there. It nevertheless has "
            "no loop, primitive cycles at every length at least two, composite-square "
            "orbit norms, and the same flood on the q={1,2} spine. The determinant "
            "therefore fails the marked prime Euler target at degree one."
        ),
        "overall_verdict": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
        "route_tuple": route_tuple,
        "scientific_gates": scientific_gates,
        "stop_labels": [
            "STOP_PRIME_ORBIT_LEDGER",
            "CYCLE_FLOOD",
            "PRUNING_PERSISTS",
            "PROVES_TOO_MUCH",
            "STOP_SCOPED",
            "ROUTE_B_LOCKED",
        ],
        "target_zero_data_used": False,
        "target_zero_fields": {
            "training": "not_applicable; no_target_zero_evaluation",
            "validation": "not_applicable; no_target_zero_evaluation",
            "test": "not_applicable; no_target_zero_evaluation",
        },
    }
    if route_tuple != summary["route_tuple"] or not all(scientific_gates.values()):
        raise AssertionError(json.dumps(payload, sort_keys=True))
    (RESULTS / "analysis_summary.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
