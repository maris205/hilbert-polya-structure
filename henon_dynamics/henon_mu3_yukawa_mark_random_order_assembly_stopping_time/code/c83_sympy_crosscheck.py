#!/usr/bin/env python3
"""Symbolic stopping-time cross-check for C83."""

from __future__ import annotations

import json
from math import factorial
from pathlib import Path
import sympy as sp

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c83_random_order_stopping_time_evidence.json"


def main():
    evidence = json.loads(EVIDENCE.read_text())
    assert evidence["schema_id"] == "hcs-c83-random-order-prefix-stopping-time-prefreeze-v1"
    assert evidence["status"] == "PREFREEZE_G3_PASS"
    atlas = evidence["assembly_atlas"]
    z = sp.symbols("z")
    pivotal_poly = sum(value * int(key.split(",")[1]) *
                       z ** int(key.split(",")[0])
                       for key, value in atlas["pivotal_pattern_counts"].items())
    # The coefficient of z^k is the total number of pivotal labels over all
    # full supports of size k.  Convert it to the ordered-permutation count.
    expected = {}
    for k in range(17):
        coeff = int(sp.expand(pivotal_poly).coeff(z, k))
        expected[str(k)] = coeff * factorial(k - 1) * factorial(16 - k) if k else 0
    assert expected == atlas["permutation_count_by_stopping_time"]
    assert sum(expected.values()) == factorial(16)
    assert sp.expand(pivotal_poly).subs(z, 1) == sum(
        int(v) for v in atlas["pivotal_support_count_by_cardinality"].values()
    )
    # A probability generating function has value one at z=1 after division by
    # 16!, and its derivative gives the stored exact expectation.
    pgf = sp.expand(sum(value * z ** int(k) for k, value in expected.items()) / factorial(16))
    assert sp.simplify(pgf.subs(z, 1) - 1) == 0
    derivative_at_one = sp.factor(sp.diff(pgf, z).subs(z, 1))
    expected_fraction = sp.Rational(
        atlas["expected_stopping_time"]["numerator"],
        atlas["expected_stopping_time"]["denominator"],
    )
    assert derivative_at_one == expected_fraction
    print(json.dumps({"status": "C83_SYMPY_CROSSCHECK_PASS",
                      "pgf_at_one": 1, "expected_stopping_time": str(expected_fraction),
                      "pivotal_polynomial_degree": int(sp.degree(pivotal_poly, z))}, sort_keys=True))


if __name__ == "__main__":
    main()
