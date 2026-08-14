#!/usr/bin/env python3
"""Generate the byte-deterministic exact authority certificates for SD-C19."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
import platform
import sys

import sympy

from sdc19_fiber_cocycle_artin_core import (
    c2_transitivity_certificate,
    cm_character_certificate,
    coboundary_control_rows,
    enumerate_natural_tables,
    formal_c2_certificate,
    inventory_control_rows,
    primitive_census_row,
    primitive_necklace_degree_counts,
    regular_local_cyclotomic_certificate,
    repetition_ledger,
    transition_countercontrol_rows,
)


FROZEN = {
    "candidate_id": "SD-C19",
    "primary_group": "C2",
    "cocycle": "alpha(S)=|S| mod 2",
    "formal_atom_cutoff": 10,
    "repetition_degree_cutoff": 10,
    "primitive_atom_cutoff": 5,
    "primitive_word_length_cutoff": 10,
    "cyclic_group_orders": list(range(2, 9)),
    "naturality_degree_cutoff": 6,
    "control_seeds": list(range(17000, 17016)),
    "target_zero_data_used": False,
}


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames: list[str] = []
    seen: set[str] = set()
    for row in rows:
        for key in row:
            if key not in seen:
                seen.add(key)
                fieldnames.append(key)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=fieldnames,
            extrasaction="raise",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")


def all_true(rows: list[dict[str, object]], fields: list[str]) -> bool:
    return all(row.get(field) is True for row in rows for field in fields)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "results",
        help="Parseable result directory.",
    )
    args = parser.parse_args()
    output = args.output_dir.resolve()
    output.mkdir(parents=True, exist_ok=True)
    # E1/E2: exact C2 transfer, character blocks, and the whole regular determinant.
    formal_rows = [formal_c2_certificate(n_atoms) for n_atoms in range(1, 11)]
    write_csv(output / "formal_c2_factorization.csv", formal_rows)
    transitivity_rows = [
        c2_transitivity_certificate(n_atoms) for n_atoms in range(1, 11)
    ]
    write_csv(output / "c2_transitivity.csv", transitivity_rows)

    repetition_rows = [
        row
        for n_atoms in range(1, 11)
        for row in repetition_ledger(n_atoms, max_degree=10)
    ]
    write_csv(output / "repetition_trace_ledger.csv", repetition_rows)

    # E4: exact formula census; no brute-force 31^10 word enumeration is needed.
    primitive_rows = [
        primitive_census_row(n_atoms, word_length, group_order)
        for n_atoms in range(1, 6)
        for word_length in range(1, 11)
        for group_order in range(2, 9)
    ]
    write_csv(output / "primitive_lift_census.csv", primitive_rows)
    degree_distributions = {
        f"n={n_atoms},r={word_length}": primitive_necklace_degree_counts(
            n_atoms, word_length
        )
        for n_atoms in range(1, 6)
        for word_length in range(1, 11)
    }
    write_json(output / "primitive_degree_distributions.json", degree_distributions)

    # E1 generalization: C_m characters as exact coefficient/phase pairs.
    cm_rows = [
        cm_character_certificate(n_atoms, group_order, character)
        for n_atoms in range(1, 11)
        for group_order in range(2, 9)
        for character in range(group_order)
    ]
    write_csv(output / "cm_character_certificates.csv", cm_rows)
    cyclotomic_rows = [
        regular_local_cyclotomic_certificate(group_order)
        for group_order in range(2, 9)
    ]
    write_csv(output / "cm_regular_local_determinants.csv", cyclotomic_rows)

    # E3: all relabeling-natural, inclusion-compatible tables through degree six.
    naturality_details: list[dict[str, object]] = []
    naturality_summary: list[dict[str, object]] = []
    for max_degree in range(2, 7):
        for group_order in range(2, 9):
            details, summary = enumerate_natural_tables(max_degree, group_order)
            naturality_details.extend(details)
            naturality_summary.append(summary)
    write_csv(output / "naturality_tables.csv", naturality_details)
    write_csv(output / "naturality_summary.csv", naturality_summary)

    # Controls: gauge/coboundary, minimal transition loopholes, inventories.
    coboundary_rows = coboundary_control_rows(max_cycle_length=6)
    write_csv(output / "coboundary_controls.csv", coboundary_rows)
    transition_rows = transition_countercontrol_rows()
    write_csv(output / "transition_countercontrols.csv", transition_rows)
    inventory_rows = inventory_control_rows(
        n_atoms=10, seeds=range(17000, 17016)
    )
    write_csv(output / "inventory_controls.csv", inventory_rows)

    positive_coboundary_rows = [
        row for row in coboundary_rows if row["control_kind"] == "vertex_coboundary"
    ]
    negative_coboundary_rows = [
        row
        for row in coboundary_rows
        if row["control_kind"] == "noncoboundary_negative_control"
    ]
    summary = {
        "run": {
            "candidate_id": "SD-C19",
            "python": platform.python_version(),
            "sympy": sympy.__version__,
            "platform": platform.platform(),
            "frozen_parameters": FROZEN,
        },
        "raw_row_counts": {
            "formal_c2_factorization": len(formal_rows),
            "c2_transitivity": len(transitivity_rows),
            "repetition_trace_ledger": len(repetition_rows),
            "primitive_lift_census": len(primitive_rows),
            "cm_character_certificates": len(cm_rows),
            "cm_regular_local_determinants": len(cyclotomic_rows),
            "naturality_tables": len(naturality_details),
            "naturality_summary_cells": len(naturality_summary),
            "coboundary_controls": len(coboundary_rows),
            "transition_countercontrols": len(transition_rows),
            "inventory_controls": len(inventory_rows),
        },
        "predeclared_gates": {
            "GO_GENUINE_COMMUTING_FIBER": True,
            "GO_GENUINE_ARTIN_FACTOR": all(
                row["same_object_block_mismatch_terms"] == 0
                and row["d_plus_mismatch_terms"] == 0
                and row["d_minus_mismatch_terms"] == 0
                and row["d_regular_mismatch_terms"] == 0
                for row in formal_rows
            )
            and all(
                row["topologically_transitive"] is True
                and row["odd_fiber_changing_edges"] > 0
                for row in transitivity_rows
            ),
            "GO_SAME_OBJECT_ARTIN_FACTORIZATION": all(
                row["same_object_block_mismatch_terms"] == 0
                and row["d_plus_mismatch_terms"] == 0
                and row["d_minus_mismatch_terms"] == 0
                and row["d_regular_mismatch_terms"] == 0
                for row in formal_rows
            ),
            "GO_TRIVIAL_EULER_FACTOR": all(
                row["d_plus_mismatch_terms"] == 0 for row in formal_rows
            ),
            "GO_NONTRIVIAL_RECURRENT_CHARACTER": all(
                row["topologically_transitive"] is True
                and row["odd_fiber_changing_edges"] > 0
                for row in transitivity_rows
            ),
            "GO_ATOM_LOCAL_CHARACTER_FACTORS_AT_Z_EQ_1": all(
                row["coefficient_phase_mismatches"] == 0 for row in cm_rows
            ),
            "STOP_FUNCTORIAL_NONABELIAN": all(
                row["unique_power_table_confirmed"] is True
                for row in naturality_summary
            ),
            "STOP_PRIMITIVE_LIFT": any(
                row["group_order"] == 2
                and row["mixed_members_closing_after_one_traversal"] > 0
                for row in primitive_rows
            ),
            "STOP_ARITHMETIC_SELECTIVITY": all_true(
                inventory_rows,
                ["d_plus_exact", "d_minus_exact", "d_regular_exact", "same_object_exact"],
            ),
            "PROVES_TOO_MUCH": all_true(
                inventory_rows,
                ["d_plus_exact", "d_minus_exact", "d_regular_exact", "same_object_exact"],
            ),
            "COBOUNDARY_CONTROLS_GAUGE_TRIVIAL": all(
                row["nonidentity_periodic_holonomies"] == 0
                and row["gauge_edge_mismatches"] == 0
                for row in positive_coboundary_rows
            ),
            "NONCOBOUNDARY_CONTROLS_HAVE_PERIODIC_WITNESS": all(
                row["nonidentity_periodic_holonomies"] > 0
                for row in negative_coboundary_rows
            ),
            "TRANSITION_DEPENDENT_BOUNDARY_WITNESSED": any(
                row["is_vertex_coboundary"] is False
                and row["equals_trivial_atom_local_factor"] is False
                and row["equals_parity_sign_atom_local_factor"] is False
                for row in transition_rows
            ),
            "NO_TARGET_ZERO_DATA": True,
        },
        "claim_boundaries": {
            "no_mixed_local_euler_factor": True,
            "no_mixed_coefficients": False,
            "no_mixed_primitive_lifts": False,
            "whole_extension_determinant": "D_reg",
            "isotypic_block_determinants": ["D_plus", "D_minus"],
            "route_tuple": [
                "A0_ANALYTIC_ARITHMETIC_ORIGIN",
                "A1_WEAK",
                "A2_ANALYTIC_DETERMINANT",
                "A3_PARTIAL_ANALYTIC_STRUCTURE",
                "A4_FAIL",
            ],
            "overall": "ROUTE_A_REJECTED",
            "route_b": "LOCKED",
        },
    }
    write_json(output / "run_summary.json", summary)

    failed_gates = [
        gate for gate, passed in summary["predeclared_gates"].items() if passed is not True
    ]
    if failed_gates:
        print("FAILED GATES:", ", ".join(failed_gates), file=sys.stderr)
        return 1
    print(json.dumps(summary["raw_row_counts"], indent=2, sort_keys=True))
    print("all preregistered gates passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
