#!/usr/bin/env python3
"""Exact SymPy checks for C89 probability generating functions and moments."""
from __future__ import annotations

from hashlib import sha256
import json
from math import comb, factorial
from pathlib import Path
import sympy as sp

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c89_first_passage_moments_evidence.json"


def q(value: dict[str, int]) -> sp.Rational:
    return sp.Rational(value["numerator"], value["denominator"])


def main() -> None:
    raw = EVIDENCE.read_bytes()
    evidence = json.loads(raw)
    assert evidence["schema_id"] == "hcs-c89-first-passage-moments-cumulants-prefreeze-v1"
    assert evidence["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
    z = sp.symbols("z")
    total = factorial(16)
    for row in evidence["moment_atlas"]["target_rows"]:
        counts = row["permutation_count_by_first_passage_time"]
        pgf = sp.expand(sum(value * z ** int(time) for time, value in counts.items()) / total)
        assert sp.simplify(pgf.subs(z, 1) - 1) == 0
        for order in range(1, 7):
            raw_moment = sp.diff(pgf, z, order).subs(z, 1)
            # Derivatives at one are the falling-factorial moments.
            assert raw_moment == q(row["falling_factorial_moments"][str(order)])
            ordinary = sp.diff((sp.exp(0 * z) * 1), z) if False else sum(
                sp.Rational(value, total) * int(time) ** order for time, value in ((int(k), v) for k, v in counts.items())
            )
            assert ordinary == q(row["raw_moments"][str(order)])
            centered = sum(
                sp.Rational(value, total) * (int(time) - q(row["mean"])) ** order
                for time, value in ((int(k), v) for k, v in counts.items())
            )
            assert centered == q(row["central_moments"][str(order)])
        assert q(row["cumulants"]["1"]) == q(row["mean"])
        tails = row["survival_permutation_counts"]
        for order in range(1, 7):
            tail_raw = sp.Rational(sum(((time + 1) ** order - time ** order) * tails[str(time)] for time in range(16)), total)
            assert tail_raw == q(row["raw_moments"][str(order)])
            tail_fact = sp.Rational(factorial(order) * sum(comb(time, order - 1) * tails[str(time)] for time in range(order - 1, 16)), total)
            assert tail_fact == q(row["falling_factorial_moments"][str(order)])
    print(json.dumps({"status": "C89_SYMPY_CROSSCHECK_PASS", "target_count": 20, "orders": 6, "evidence_sha256": sha256(raw).hexdigest()}, sort_keys=True))


if __name__ == "__main__":
    main()
