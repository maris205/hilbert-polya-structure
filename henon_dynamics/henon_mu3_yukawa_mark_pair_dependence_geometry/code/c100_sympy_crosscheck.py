#!/usr/bin/env python3
"""SymPy checks for all C100 joint PMFs and exact dependence metrics."""
from __future__ import annotations
from hashlib import sha256
import json
from math import factorial
from pathlib import Path
import sympy as sp

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c100_pair_dependence_geometry_evidence.json"
N, M, TARGETS = 16, 17, 20
TOTAL = factorial(N)


def q(value: dict[str, int]) -> sp.Rational:
    return sp.Rational(value["numerator"], value["denominator"])


def main() -> None:
    raw = EVIDENCE.read_bytes()
    evidence = json.loads(raw)
    assert evidence["schema_id"] == "hcs-c100-pair-dependence-geometry-prefreeze-v1"
    assert evidence["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
    rows = evidence["dependence_atlas"]["pair_rows"]
    assert len(rows) == 400
    checked_cells = 0
    for index, row in enumerate(rows):
        i, j = divmod(index, TARGETS)
        assert (row["lower_target_index"], row["upper_target_index"]) == (i, j)
        counts = [[int(row["joint_pmf_permutation_counts"][str(a)][str(b)]) for b in range(M)] for a in range(M)]
        left = [int(row["marginal_permutation_counts"]["left"][str(a)]) for a in range(M)]
        right = [int(row["marginal_permutation_counts"]["right"][str(b)]) for b in range(M)]
        assert sum(map(sum, counts)) == TOTAL
        assert [sum(r) for r in counts] == left
        assert [sum(counts[a][b] for a in range(M)) for b in range(M)] == right
        mixed = sp.Rational(sum(a * b * counts[a][b] for a in range(M) for b in range(M)), TOTAL)
        ml = sp.Rational(sum(a * left[a] for a in range(M)), TOTAL)
        mr = sp.Rational(sum(b * right[b] for b in range(M)), TOTAL)
        vl = sp.Rational(sum(a * a * left[a] for a in range(M)), TOTAL) - ml**2
        vr = sp.Rational(sum(b * b * right[b] for b in range(M)), TOTAL) - mr**2
        cov = mixed - ml * mr
        rational_correlation = cov / (vl + vr) if vl + vr else sp.Rational(0)
        assert q(row["mixed_first_product_moment"]) == mixed
        assert q(row["covariance"]) == cov
        assert q(row["rational_correlation"]) == rational_correlation
        assert q(row["left_variance"]) == vl and q(row["right_variance"]) == vr
        if vl and vr:
            assert q(row["pearson_correlation_squared"]) == cov**2 / (vl * vr)
        else:
            assert row["pearson_correlation_squared"] is None
        tv = sp.Rational(0)
        frechet_width = sp.Rational(0)
        violation = sp.Rational(0)
        for a in range(M):
            for b in range(M):
                joint = sp.Rational(counts[a][b], TOTAL)
                product = sp.Rational(left[a] * right[b], TOTAL * TOTAL)
                tv += abs(joint - product) / 2
                lower = max(sp.Rational(0), sp.Rational(left[a] + right[b] - TOTAL, TOTAL))
                upper = min(sp.Rational(left[a], TOTAL), sp.Rational(right[b], TOTAL))
                frechet_width += upper - lower
                violation += max(sp.Rational(0), joint - upper) + max(sp.Rational(0), lower - joint)
                assert lower <= joint <= upper
                checked_cells += 1
        assert q(row["total_variation_from_product_marginals"]) == tv
        assert q(row["l1_from_product_marginals"]) == 2 * tv
        assert q(row["frechet_interval_width_l1"]) == frechet_width
        assert q(row["frechet_violation_l1"]) == violation
    for i in range(TARGETS):
        for j in range(TARGETS):
            a = rows[i * TARGETS + j]["joint_pmf_permutation_counts"]
            b = rows[j * TARGETS + i]["joint_pmf_permutation_counts"]
            assert all(a[str(x)][str(y)] == b[str(y)][str(x)] for x in range(M) for y in range(M))
    print(json.dumps({"status": "C100_SYMPY_CROSSCHECK_PASS", "ordered_pair_count": 400, "joint_probability_cells": checked_cells, "evidence_sha256": sha256(raw).hexdigest()}, sort_keys=True))


if __name__ == "__main__":
    main()
