#!/usr/bin/env python3
"""Exact SymPy checks of all C98 kernel and variance identities."""
from __future__ import annotations

import json
from math import factorial
from pathlib import Path
import sympy as sp

PROJECT = Path(__file__).resolve().parents[1]
TOTAL = factorial(16)


def q(value: dict[str, int]) -> sp.Rational:
    return sp.Rational(value["numerator"], value["denominator"])


def main() -> None:
    data = json.loads((PROJECT / "results/c98_conditional_kernel_evidence.json").read_text())
    atlas = data["conditional_kernel_atlas"]
    rows = atlas["pair_rows"]
    assert len(rows) == 400
    attainable = empty = 0
    for row in rows:
        left = row["conditioning_target_index"]
        right = row["response_target_index"]
        assert sum(row["conditioning_marginal_permutation_counts"].values()) == TOTAL
        assert sum(row["response_marginal_permutation_counts"].values()) == TOTAL
        for conditional in row["conditional_rows"]:
            denominator = conditional["conditioning_permutation_count"]
            probabilities = conditional["conditional_probability_by_response_time"]
            if denominator:
                attainable += 1
                values = [q(probabilities[str(time)]) for time in range(17)]
                assert sum(values) == 1
                mean = sum(sp.Integer(time) * values[time] for time in range(17))
                second = sum(sp.Integer(time * time) * values[time] for time in range(17))
                assert mean == q(conditional["conditional_mean_response_time"])
                assert second == q(conditional["conditional_second_moment_response_time"])
                assert second - mean**2 == q(conditional["conditional_variance_response_time"])
            else:
                empty += 1
                assert probabilities is None
                assert conditional["conditional_mean_response_time"] is None
                assert conditional["conditional_variance_response_time"] is None
        tower = row["tower_identities"]
        assert q(tower["kernel_recovered_response_expectation"]) == q(tower["c88_response_expectation"])
        assert q(tower["expected_conditional_variance"]) + q(tower["variance_of_conditional_mean"]) == q(tower["c88_response_variance"])
        reverse = rows[right * 20 + left]
        for a in range(17):
            for b in range(17):
                assert row["joint_first_passage_permutation_counts"][str(a)][str(b)] == reverse["joint_first_passage_permutation_counts"][str(b)][str(a)]
    assert attainable == atlas["attainable_conditioning_row_count"] == 4980
    assert empty == atlas["empty_conditioning_row_count"] == 1820
    print(json.dumps({"status": "C98_SYMPY_CROSSCHECK_PASS", "ordered_pair_count": len(rows), "attainable_rows": attainable, "bayes_cells": 400 * 17 * 17}, sort_keys=True))


if __name__ == "__main__":
    main()
