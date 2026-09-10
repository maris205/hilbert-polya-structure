#!/usr/bin/env python3
"""Exact rational and symbolic checks for C103."""
from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c103_minmax_aggregation_evidence.json"


def f(value: dict[str, int]) -> Fraction:
    return Fraction(value["numerator"], value["denominator"])


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    rows = data["aggregation_atlas"]["pair_rows"]
    checks = 0
    for row in rows:
        minimum = [int(row["minimum_permutation_count_by_time"][str(t)]) for t in range(17)]
        maximum = [int(row["maximum_permutation_count_by_time"][str(t)]) for t in range(17)]
        assert sum(minimum) == 16 * 15 * 14 * 13 * 12 * 11 * 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
        assert sum(maximum) == sum(minimum)
        assert f(row["expected_sum_identity"]["expected_min_plus_max"]) == f(row["expected_sum_identity"]["expected_left_plus_right"])
        checks += 3
        if row["left_target_index"] == row["right_target_index"]:
            assert minimum == [int(row["joint_first_passage_permutation_counts"][str(t)][str(t)]) for t in range(17)]
            assert row["diagonal_checks"]["minimum_identity_on_diagonal"]
            assert row["diagonal_checks"]["maximum_identity_on_diagonal"]
            checks += 2
    print(json.dumps({"status": "C103_SYMPY_CROSSCHECK_PASS", "checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
