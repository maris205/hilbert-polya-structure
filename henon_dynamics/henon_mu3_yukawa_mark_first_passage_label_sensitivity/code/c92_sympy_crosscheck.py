#!/usr/bin/env python3
"""Symbolic rational checks for the C92 sensitivity receipt."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

import sympy as sp

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c92_first_passage_label_sensitivity_evidence.json"
TOTAL = 16


def frac(value: dict[str, int]) -> sp.Rational:
    return sp.Rational(value["numerator"], value["denominator"])


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    rows = data["target_atlas"]["target_rows"]
    assert len(rows) == 20
    for target, row in enumerate(rows):
        probability_sum = sum((frac(label["pivotal_probability"]) for label in row["pivotal_label_rows"]), sp.Rational(0))
        expected = frac(row["c88_expected_first_passage_time"])
        rank_sum = sum((frac(label["unconditional_rank_mean_contribution"]) for label in row["pivotal_label_rows"]), sp.Rational(0))
        rank_square = sum((frac(label["unconditional_rank_square_mean_contribution"]) for label in row["pivotal_label_rows"]), sp.Rational(0))
        direct_square = frac(row["c88_expected_first_passage_square"])
        assert probability_sum == (sp.Rational(0) if target == 0 else sp.Rational(1))
        assert rank_sum == expected
        assert rank_square == direct_square
        polynomial = sum(
            sp.Rational(count, sp.factorial(16)) * sp.Symbol("z") ** int(time)
            for label in row["pivotal_label_rows"]
            for time, count in label["pivotal_permutation_count_by_rank"].items()
            if count
        )
        z = sp.Symbol("z")
        assert sp.diff(polynomial, z).subs(z, 1) == expected
    print(json.dumps({"status": "C92_SYMPY_CROSSCHECK_PASS", "target_count": 20, "labels_per_target": TOTAL}, sort_keys=True))


if __name__ == "__main__":
    main()
