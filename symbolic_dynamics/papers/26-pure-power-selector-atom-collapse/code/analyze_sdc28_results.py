#!/usr/bin/env python3
"""Derive the compact deterministic SD-C28 analysis summary."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"


def rows(name: str) -> list[dict[str, str]]:
    with (RESULTS / name).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> int:
    summary = json.loads((RESULTS / "summary.json").read_text(encoding="utf-8"))
    projector = rows("projector_word_ledger.csv")
    radical = rows("radical_word_ledger.csv")
    graded = rows("graded_word_ledger.csv")
    hankel = rows("hankel_syntactic_ledger.csv")
    aggregate = rows("aggregate_adversary.csv")
    support = rows("support_incidence_ledger.csv")
    color = rows("bar_hochschild_controls.csv")
    de_rham_local = rows("de_rham_local_controls.csv")
    de_rham_words = rows("de_rham_tensor_word_ledger.csv")
    inventories = rows("arbitrary_inventory_controls.csv")
    witnesses = [row for row in aggregate if row["kind"] == "mixed_word_witness"]
    payload = {
        "candidate_id": "SD-C28",
        "raw_data_table": summary["row_counts"],
        "finite_selector": {
            "projector_rows": len(projector),
            "radical_rows": len(radical),
            "graded_rows": len(graded),
            "all_exact": all(row["exact"] == "True" for row in projector + radical + graded),
        },
        "memory_lower_bound": {
            "rows": len(hankel),
            "largest_color_count": max(int(row["color_count"]) for row in hankel),
            "all_trace_completion_rank_equals_colors": all(
                row["trace_completion_hankel_rank"] == row["color_count"]
                for row in hankel
            ),
            "all_literal_rank_equals_colors_plus_one": all(
                int(row["literal_language_hankel_rank"]) == int(row["color_count"]) + 1
                for row in hankel
            ),
        },
        "aggregate_firewall": {
            "aggregate_power_rows": len(aggregate) - len(witnesses),
            "all_aggregate_rows_pass": all(
                row["aggregate_exact"] == "True"
                for row in aggregate
                if row["kind"] == "aggregate_power"
            ),
            "wordwise_witnesses": [
                {"word": row["word"], "supertrace": row["actual"]}
                for row in witnesses
            ],
            "wordwise_selector_fails": all(
                row["wordwise_selector_exact"] == "False" for row in witnesses
            ),
        },
        "canonical_complexes": {
            "support_rows": len(support),
            "support_euler_all_exact": all(row["exact"] == "True" for row in support),
            "mixed_support_cohomology_nonzero": all(
                row["mixed_cohomology_nonzero"] == "True"
                for row in support
                if int(row["support_size"]) > 1
            ),
            "color_algebra_rows": len(color),
            "all_color_algebras_atomic_h0": all(
                row["surviving_sector"] == "direct_sum_of_color_lines" for row in color
            ),
        },
        "de_rham_tensor": {
            "local_rows": len(de_rham_local),
            "word_rows": len(de_rham_words),
            "all_local_exact": all(
                row["power_exact"] == row["chain_exact"] == row["quotient_exact"] == "True"
                for row in de_rham_local
            ),
            "all_wordwise_exact": all(row["exact"] == "True" for row in de_rham_words),
        },
        "arbitrary_inventory": {
            "rows": len(inventories),
            "all_prove_too_much": all(row["proves_too_much"] == "True" for row in inventories),
            "prime_selectivity_credit": sum(int(row["prime_selectivity_credit"]) for row in inventories),
        },
        "strongest_advance": (
            "the exact wordwise selector is realizable and its finite graded character "
            "semisimplifies to one net one-dimensional sector per supplied color"
        ),
        "strongest_ceiling": (
            "Hankel rank grows with colors, bar/Hochschild H0 is the color algebra, "
            "and countable projectors are visibly the disjoint supplied inventory"
        ),
        "next_experiment": (
            "test a genuinely infinite-dimensional non-type-I cyclic trace with a "
            "source-derived factorization action; finite recognizable memory is closed"
        ),
        "route_tuple": summary["route_tuple"],
        "overall_verdict": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
        "target_zero_data_used": False,
    }
    (RESULTS / "analysis_summary.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
