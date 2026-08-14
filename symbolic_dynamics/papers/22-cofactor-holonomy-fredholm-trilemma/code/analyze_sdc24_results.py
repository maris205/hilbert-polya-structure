#!/usr/bin/env python3
"""Aggregate SD-C24 theorem audits into Route-A and research summaries."""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"


def read_csv(name: str) -> list[dict[str, str]]:
    with (RESULTS / name).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(name: str, rows: list[dict[str, object]]) -> None:
    with (RESULTS / name).open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    simple = read_csv("simple_cycle_holonomy.csv")
    rooted = read_csv("rooted_cycle_ledger.csv")
    atomic = read_csv("atomic_trace_coefficients.csv")
    fourier = read_csv("fourier_reconstruction.csv")
    trace_class = read_csv("trace_class_diagnostics.csv")
    inventory = read_csv("inventory_controls.csv")
    source = json.loads((RESULTS / "source_oracle_certificate.json").read_text())

    route_rows = [
        {
            "gate": "A0",
            "verdict": "A0_STRUCTURAL_ARITHMETIC_RELATION",
            "status": "PROVED",
            "evidence": "successor_tensor_cofactor_identity",
            "failure": "exposes_all_successor_divisors",
        },
        {
            "gate": "A1",
            "verdict": "A1_WEAK",
            "status": "PROVED_OBSTRUCTION",
            "evidence": "exact_primitive_repetition_holonomy_ledger",
            "failure": "infinitely_many_primitive_representatives_per_atom",
        },
        {
            "gate": "A2",
            "verdict": "A2_ANALYTIC_DETERMINANT",
            "status": "PROVED",
            "evidence": "sharp_two_parameter_S1_domain_and_fredholm_fibers",
            "failure": "neutral_group_trace_determinant_is_one",
        },
        {
            "gate": "A3",
            "verdict": "A3_FAIL",
            "status": "STOP_SCOPED",
            "evidence": "same_object_holonomy_resolution_only",
            "failure": "primitive_support_period_multiplicity_and_roof_mismatch",
        },
        {
            "gate": "A4",
            "verdict": "A4_FAIL",
            "status": "NOT_TESTABLE_STOP_SCOPED",
            "evidence": "none",
            "failure": "no_self_adjoint_carrier_or_critical_line_mechanism",
        },
    ]
    write_csv("route_gate_summary.csv", route_rows)

    simple_counts = Counter(int(row["cutoff"]) for row in simple)
    q2_counts = Counter(int(row["cutoff"]) for row in simple if int(row["holonomy"]) == 2)
    rooted_counts = Counter(int(row["power"]) for row in rooted)
    max_fourier_error = max(float(row["absolute_error"]) for row in fourier)
    payload = {
        "candidate_id": "SD-C24",
        "route_tuple": [row["verdict"] for row in route_rows],
        "overall_verdict": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
        "source_audit": {
            "cutoff": source["cutoff"],
            "edge_count": source["edge_count"],
            "identity_mismatches": source["quotient_identity_mismatches"],
            "target_zero_data_used": False,
        },
        "exact_census": {
            "simple_cycles": {str(key): simple_counts[key] for key in sorted(simple_counts)},
            "q2_cycles": {str(key): q2_counts[key] for key in sorted(q2_counts)},
            "rooted_cycles": {str(key): rooted_counts[key] for key in sorted(rooted_counts)},
            "rooted_rows": len(rooted),
            "atomic_trace_rows": len(atomic),
            "atomic_trace_mismatches": sum(row["match"] != "True" for row in atomic),
        },
        "analytic_diagnostics": {
            "trace_class_rows": len(trace_class),
            "classification_mismatches": sum(row["classification_match"] != "True" for row in trace_class),
            "fourier_rows": len(fourier),
            "max_fourier_reconstruction_error": max_fourier_error,
            "finite_prefix_role": "diagnostic_only; theorem_proves_infinite_domain",
            "sharp_domain": "Re(s)>1/2 and Re(s+u)>1/2",
        },
        "controls": {
            "inventory_rows": len(inventory),
            "inventory_names": sorted({row["inventory"] for row in inventory}),
            "positive_support_failures": sum(
                row["support_present"] != "True" or row["positive_weight"] != "True"
                for row in inventory
            ),
            "selection_margin": 0,
            "proves_too_much": True,
        },
        "observations": [
            "The cofactor cocycle resolves every cycle into an integer holonomy Q at exact finite support.",
            "Holonomy two contains one primitive canonical cycle at every length k at least two.",
            "Every tested unitary character gives the same nonzero phase to the whole holonomy-two spine.",
            "Endpoint damping supplies an honest Fredholm region but factorially suppresses the canonical spine.",
        ],
        "interpretation": [
            "The exact cofactor label is a useful source-intrinsic invariant but not an arithmetic selector.",
            "The regular neutral trace deletes all positive holonomy and therefore yields determinant one, not a prime Euler ledger.",
            "Changing positive inventories changes amplitudes but cannot change primitive support.",
        ],
        "implication": [
            "The abelian product-holonomy branch is closed for this graph under scalar characters and positive inventory changes.",
            "The next admissible test must add finite memory or noncommutative order data inside Symbolic Dynamics.",
        ],
        "target_zero_metrics": "not_applicable; no_target_zero_evaluation",
    }
    (RESULTS / "analysis_summary.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
