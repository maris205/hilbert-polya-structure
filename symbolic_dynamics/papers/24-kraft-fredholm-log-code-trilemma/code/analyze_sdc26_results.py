#!/usr/bin/env python3
"""Derive the compact deterministic SD-C26 analysis summary."""

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
    disjoint = rows("disjoint_cycle_witnesses.csv")
    mixed = rows("mixed_primitive_ledger.csv")
    code = rows("finite_code_counting.csv")
    controls = rows("arbitrary_inventory_controls.csv")
    prime_witness = next(
        row
        for row in disjoint
        if row["cutoff"] == "8191"
        and row["inventory"] == "prime_evaluator"
        and row["encoder"] == "elias_gamma"
        and row["allocation"] == "equal"
        and row["sigma"] == "1"
    )
    prime_mixed = {
        int(row["return_count"]): int(row["mixed_primitive_necklaces"])
        for row in mixed
        if row["inventory"] == "prime_evaluator"
        and row["encoder"] == "elias_gamma"
    }
    payload = {
        "candidate_id": "SD-C26",
        "finite_local_code": {
            "rows": len(code),
            "cyclic_collisions": sum(int(row["cyclic_collision_count"]) for row in code),
            "target_calls": sum(int(row["encoder_target_calls"]) for row in code),
        },
        "prime_8191_equal_gamma": {
            "cycle_length": int(prime_witness["cycle_length"]),
            "max_singular_value": prime_witness["max_singular_value"],
            "universal_lower_bound": prime_witness[
                "universal_max_sv_lower_bound"
            ],
            "block_s1_norm": prime_witness["block_s1_norm"],
        },
        "prime_trie_mixed_necklaces": prime_mixed,
        "arbitrary_inventory": {
            "rows": len(controls),
            "all_prove_too_much": all(row["proves_too_much"] == "True" for row in controls),
            "matched_random_hash_controls": sorted(
                {
                    row["inventory"]
                    for row in controls
                    if row["prime_density_matched"] == "True"
                }
            ),
        },
        "strongest_result": (
            "finite orbit separation plus a literal positive prime-only ledger "
            "forces vertex-disjoint long cycles, and total roof log(p) makes the "
            "whole counting-space adjacency noncompact"
        ),
        "only_frozen_escape": (
            "countable one-symbol-per-atom diagonal; selector-tautological and "
            "identical for all supplied inventories"
        ),
        "route_tuple": [
            "A0_STRUCTURAL_ARITHMETIC_RELATION",
            "A1_FAIL",
            "A2_FAIL",
            "A3_FAIL",
            "A4_FAIL",
        ],
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

