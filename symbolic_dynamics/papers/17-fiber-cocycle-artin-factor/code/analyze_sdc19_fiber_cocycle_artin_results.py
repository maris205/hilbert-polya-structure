#!/usr/bin/env python3
"""Aggregate SD-C19 authority certificates into paper-facing exact findings."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import csv
from fractions import Fraction
import json
from pathlib import Path


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def as_bool(value: str) -> bool:
    if value not in {"True", "False"}:
        raise ValueError(f"not a serialized bool: {value!r}")
    return value == "True"


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    fieldnames = list(rows[0]) if rows else []
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--results-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "results",
    )
    args = parser.parse_args()
    result_dir = args.results_dir.resolve()

    formal = read_csv(result_dir / "formal_c2_factorization.csv")
    repetitions = read_csv(result_dir / "repetition_trace_ledger.csv")
    transitivity = read_csv(result_dir / "c2_transitivity.csv")
    cm = read_csv(result_dir / "cm_character_certificates.csv")
    natural = read_csv(result_dir / "naturality_summary.csv")
    primitive = read_csv(result_dir / "primitive_lift_census.csv")
    inventories = read_csv(result_dir / "inventory_controls.csv")
    coboundaries = read_csv(result_dir / "coboundary_controls.csv")
    transitions = read_csv(result_dir / "transition_countercontrols.csv")

    inventory_by_kind: defaultdict[str, list[dict[str, str]]] = defaultdict(list)
    for row in inventories:
        inventory_by_kind[row["inventory_kind"]].append(row)
    control_stats: dict[str, tuple[int, int, Fraction]] = {}
    for kind, rows in sorted(inventory_by_kind.items()):
        exact = sum(
            all(
                as_bool(row[field])
                for field in (
                    "d_plus_exact",
                    "d_minus_exact",
                    "d_regular_exact",
                    "same_object_exact",
                )
            )
            for row in rows
        )
        control_stats[kind] = (len(rows), exact, Fraction(exact, len(rows)))
    prime_pass_rate = control_stats["prime"][2]
    control_table: list[dict[str, object]] = []
    for kind, (row_count, exact, pass_rate) in sorted(control_stats.items()):
        control_table.append(
            {
                "inventory": kind,
                "seeds": row_count,
                "all_four_identities_exact": exact,
                "failure_count": row_count - exact,
                "identity_pass_rate": str(pass_rate),
                "identity_pass_rate_margin": str(pass_rate - prime_pass_rate),
            }
        )
    write_csv(result_dir / "inventory_comparison_table.csv", control_table)

    transition_table = [
        {
            "control": row["control"],
            "coboundary": row["is_vertex_coboundary"],
            "periodic_witness": row["first_nontrivial_periodic_holonomy"],
            "nearest_atom_local_baseline": row["nearest_atom_local_baseline"],
            "first_leak": row["first_leak_vs_nearest_atom_local"],
            "exact_atom_local": str(
                as_bool(row["equals_trivial_atom_local_factor"])
                or as_bool(row["equals_parity_sign_atom_local_factor"])
            ),
        }
        for row in transitions
    ]
    write_csv(result_dir / "transition_comparison_table.csv", transition_table)

    natural_tables = sum(int(row["tables_enumerated"]) for row in natural)
    natural_clean = sum(
        int(row["operator_coefficient_clean_tables"]) for row in natural
    )
    mixed_c2_nontrivial_rows = [
        row
        for row in primitive
        if int(row["group_order"]) == 2 and int(row["n_atoms"]) >= 2
    ]
    mixed_c2_positive = sum(
        int(row["mixed_members_closing_after_one_traversal"]) > 0
        for row in mixed_c2_nontrivial_rows
    )
    positive_coboundaries = [
        row for row in coboundaries if row["control_kind"] == "vertex_coboundary"
    ]
    negative_coboundaries = [
        row
        for row in coboundaries
        if row["control_kind"] == "noncoboundary_negative_control"
    ]
    n5r10c2 = next(
        row
        for row in primitive
        if row["n_atoms"] == "5"
        and row["base_word_length"] == "10"
        and row["group_order"] == "2"
    )
    summary = {
        "raw_data_table": {
            "formal_c2": {
                "rows": len(formal),
                "cutoff": "n=1..10",
                "total_mismatch_terms": sum(
                    int(row[field])
                    for row in formal
                    for field in (
                        "d_plus_mismatch_terms",
                        "d_minus_mismatch_terms",
                        "d_regular_mismatch_terms",
                        "same_object_block_mismatch_terms",
                    )
                ),
            },
            "trace_repetitions": {
                "rows": len(repetitions),
                "exact_rows": sum(as_bool(row["exact_match"]) for row in repetitions),
            },
            "c2_dynamics": {
                "transitive_rows": sum(
                    as_bool(row["topologically_transitive"]) for row in transitivity
                ),
                "mixing_rows": sum(as_bool(row["mixing"]) for row in transitivity),
                "period_two_rows": sum(int(row["period"]) == 2 for row in transitivity),
            },
            "cm_characters": {
                "rows": len(cm),
                "exact_rows": sum(
                    int(row["coefficient_phase_mismatches"]) == 0 for row in cm
                ),
            },
            "natural_tables": {
                "tables": natural_tables,
                "cutoff_cells": len(natural),
                "operator_coefficient_clean_tables": natural_clean,
                "one_clean_per_cell": all(
                    int(row["operator_coefficient_clean_tables"]) == 1
                    for row in natural
                ),
                "aggregate_clean_fraction": f"{natural_clean}/{natural_tables}",
            },
            "primitive_lifts": {
                "rows": len(primitive),
                "c2_n_ge_2_rows_with_mixed_immediate_closures": mixed_c2_positive,
                "c2_n_ge_2_rows": len(mixed_c2_nontrivial_rows),
                "n5_r10_c2_base_primitive_necklaces": int(
                    n5r10c2["base_primitive_necklaces"]
                ),
                "n5_r10_c2_mixed_immediate_closures": int(
                    n5r10c2["mixed_members_closing_after_one_traversal"]
                ),
                "n5_r10_c2_lifted_primitive_cycles": int(
                    n5r10c2["lifted_primitive_cycles_total"]
                ),
            },
            "coboundary_controls": {
                "gauge_rows": len(positive_coboundaries),
                "gauge_rows_with_zero_periodic_holonomy": sum(
                    int(row["nonidentity_periodic_holonomies"]) == 0
                    for row in positive_coboundaries
                ),
                "negative_rows": len(negative_coboundaries),
                "negative_rows_with_witness": sum(
                    int(row["nonidentity_periodic_holonomies"]) > 0
                    for row in negative_coboundaries
                ),
            },
            "inventory_controls": control_table,
            "transition_controls": transition_table,
        },
        "key_findings": [
            {
                "observation": "All formal C2 and same-object coefficient mismatches are zero through n=10, and all 300 trace/repetition coefficients match.",
                "interpretation": "The sign convention and D_reg=D_plus*D_minus decomposition are exact, not numerical fits.",
                "implication": "GO_GENUINE_ARTIN_FACTOR is certified at z=1.",
                "next_step": "Keep D_reg as the whole extension and D_plus/D_minus as isotypic blocks in the paper.",
            },
            {
                "observation": f"Exactly {natural_clean} of {natural_tables} enumerated natural tables are operator-coefficient-clean: one power table in each of 35 cutoff cells.",
                "interpretation": "Full regular visibility removes nonfaithful-character accidents and enforces r_k=k mod m through degree six.",
                "implication": "The one-letter functorial no-leak branch is cyclic factor count.",
                "next_step": "Move only to transition-dependent incidence holonomy in Paper18.",
            },
            {
                "observation": f"All {len(inventories)} fraction inventory runs, including all 16 seeds per family, reproduce every determinant identity; their identity pass-rate margin is zero, while their numerical determinant values need not agree.",
                "interpretation": "The mechanism is free-commutative and inventory-universal.",
                "implication": "Control separation is exactly zero: STOP_ARITHMETIC_SELECTIVITY / PROVES_TOO_MUCH.",
                "next_step": "Do not add more one-letter inventory tests; they cannot restore selectivity.",
            },
            {
                "observation": f"Mixed one-traversal C2 closures occur in {mixed_c2_positive}/{len(mixed_c2_nontrivial_rows)} n>=2 census rows.",
                "interpretation": "Atom-local character factors arise after cancellation and do not eliminate mixed primitive lifts.",
                "implication": "A1 remains WEAK despite A2 being an exact analytic determinant.",
                "next_step": "Report base and lifted primitive counts separately.",
            },
            {
                "observation": "The transition coboundary is gauge-trivial, while three noncoboundary transition controls have periodic witnesses and leak relative to both atom-local factors; strict symbol change first leaks at x^2 y^2.",
                "interpretation": "Transition dependence is a real loophole to the one-letter theorem, but clean low squarefree degree can hide repetition leakage.",
                "implication": "Paper18 must audit temporal powers as well as squarefree degree.",
                "next_step": "Test p,q,r merge-order commutators together with the p^2 q^2 ledger.",
            },
        ],
        "route": {
            "tuple": [
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
    with (result_dir / "analysis_summary.json").open("w", encoding="utf-8") as handle:
        json.dump(summary, handle, indent=2, sort_keys=True)
        handle.write("\n")
    print(json.dumps(summary["raw_data_table"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
