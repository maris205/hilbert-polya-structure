#!/usr/bin/env python3
"""SymPy checks for the C99 polynomial spectrum and derivative identities."""
from __future__ import annotations
from hashlib import sha256
import json
from math import factorial, gcd
from pathlib import Path
import sympy as sp

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c99_generating_polynomial_evidence.json"
EXPECTED_C88 = "4511d434f477784782f2af5106afff4c2cf3b48cd7eb7a62ed05b8f2f42afb1b"
EXPECTED_C89 = "86a589505280721590674235626ddc21e37d57c891c726c7e6fbba98b2bd3af9"


def q(value: dict[str, int]) -> sp.Rational:
    return sp.Rational(value["numerator"], value["denominator"])


def s2(n: int, k: int) -> int:
    table = [[0] * (n + 1) for _ in range(n + 1)]
    table[0][0] = 1
    for row in range(1, n + 1):
        for col in range(1, row + 1):
            table[row][col] = table[row - 1][col - 1] + col * table[row - 1][col]
    return table[n][k]


def main() -> None:
    raw = EVIDENCE.read_bytes()
    evidence = json.loads(raw)
    assert evidence["schema_id"] == "hcs-c99-first-passage-generating-polynomial-prefreeze-v1"
    assert evidence["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
    assert evidence["authority"]["c88"] == EXPECTED_C88 and evidence["authority"]["c89"] == EXPECTED_C89
    z = sp.symbols("z")
    total = factorial(16)
    for row in evidence["polynomial_atlas"]["target_rows"]:
        counts = row["permutation_count_by_time"]
        pgf = sp.expand(sum(value * z ** int(time) for time, value in counts.items()) / total)
        assert sp.simplify(pgf.subs(z, 1) - 1) == 0
        support = sorted(int(time) for time, value in counts.items() if value)
        assert support == row["support_times"]
        assert row["degree"] == max(support) == row["support_maximum"]
        assert row["support_gcd"] == sp.igcd(*support) if len(support) > 1 else row["support_gcd"] == support[0]
        for order in range(7):
            derivative = sp.diff(pgf, z, order).subs(z, 1)
            assert derivative == q(row["derivative_at_one_orders_0_to_6"][str(order)])
            ordinary = sum(sp.Rational(value, total) * int(time) ** order for time, value in counts.items())
            assert ordinary == q(row["c89_raw_moments"][str(order)])
            recovered = sum(s2(order, falling_order) * q(row["derivative_at_one_orders_0_to_6"][str(falling_order)]) for falling_order in range(order + 1))
            assert recovered == ordinary == q(row["raw_moment_recovery_from_derivatives"][str(order)])
    print(json.dumps({"status": "C99_SYMPY_CROSSCHECK_PASS", "target_count": 20, "coefficient_cells": 340, "derivative_orders": 6, "evidence_sha256": sha256(raw).hexdigest()}, sort_keys=True))


if __name__ == "__main__":
    main()
