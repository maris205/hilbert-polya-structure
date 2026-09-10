#!/usr/bin/env python3
"""SymPy checks for C101 normalization, moments, covariance, and cumulants."""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from math import factorial
from pathlib import Path

import sympy as sp

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c101_triple_coupling_evidence.json"
N, M, TOTAL = 16, 17, factorial(16)


def q(value: dict[str, int]) -> sp.Rational:
    return sp.Rational(value["numerator"], value["denominator"])


def main() -> None:
    raw = EVIDENCE.read_bytes()
    evidence = json.loads(raw)
    assert evidence["schema_id"] == "hcs-c101-first-passage-triple-coupling-prefreeze-v1"
    assert evidence["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
    rows = evidence["triple_atlas"]["rows"]
    assert len(rows) == 1140
    checked_cells = 0
    for row in rows:
        counts = row["joint_pmf_permutation_counts_flat"]
        assert len(counts) == M ** 3 and min(counts) >= 0
        assert sum(counts) == TOTAL
        # Exact low-order raw moments use Python integers before SymPy turns
        # them into rationals, avoiding floating-point summaries entirely.
        moments = {}
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    total = sum((a ** i) * (b ** j) * (c ** k) * counts[(a * M + b) * M + c] for a in range(M) for b in range(M) for c in range(M))
                    moments[f"{i},{j},{k}"] = sp.Rational(total, TOTAL)
        assert all(q(row["raw_mixed_moments_orders_0_to_3"][key]) == value for key, value in moments.items())
        means = [moments[key] for key in ("1,0,0", "0,1,0", "0,0,1")]
        covariance = []
        for i in range(3):
            values = []
            for j in range(3):
                exponents = [0, 0, 0]
                if i == j:
                    exponents[i] = 2
                else:
                    exponents[i] = exponents[j] = 1
                key = ",".join(map(str, exponents))
                values.append(moments[key] - means[i] * means[j])
            covariance.append(values)
        assert [[q(value) for value in line] for line in row["covariance_matrix"]] == covariance
        interaction = moments["1,1,1"] - moments["1,1,0"] * means[2] - moments["1,0,1"] * means[1] - moments["0,1,1"] * means[0] + 2 * means[0] * means[1] * means[2]
        assert q(row["third_interaction_cumulant"]) == interaction
        checked_cells += len(counts)
    print(json.dumps({"status": "C101_SYMPY_CROSSCHECK_PASS", "triple_count": len(rows), "pmf_cells": checked_cells, "mixed_moment_cells": len(rows) * 64, "evidence_sha256": sha256(raw).hexdigest()}, sort_keys=True))


if __name__ == "__main__":
    main()
