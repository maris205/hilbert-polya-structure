#!/usr/bin/env python3
"""Separate SymPy reconstruction for HCS-C183."""
from __future__ import annotations

from fractions import Fraction
from math import factorial
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c183_random_transposition_evidence.json"


def partitions(n: int, maximum: int | None = None):
    if n == 0:
        yield ()
        return
    for first in range(min(n, maximum or n), 0, -1):
        for tail in partitions(n - first, first):
            yield (first,) + tail


def dimension(shape: tuple[int, ...]) -> int:
    hook_product = sp.Integer(1)
    for i, width in enumerate(shape):
        for j in range(width):
            hook_product *= width - j + sum(row > j for row in shape[i + 1 :])
    return int(sp.factorial(sum(shape)) / hook_product)


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    checks = 0
    row_map = {(row["n"], tuple(row["partition"])): row for row in data["finite_replay"]["partition_rows"]}
    z = sp.symbols("z")
    for n in range(2, 12):
        determinant = sp.Integer(1)
        formal_degree = 0
        trace_zero = 0
        for shape in partitions(n):
            d = dimension(shape)
            kappa = sum(part * (part - 2 * i + 1) for i, part in enumerate(shape, 1))
            beta = sp.Rational(1, n) + sp.Rational(kappa, n * n)
            row = row_map[(n, shape)]
            assert sp.Rational(row["lazy_eigenvalue"]["numerator"], row["lazy_eigenvalue"]["denominator"]) == beta
            checks += 1
            assert row["hook_dimension"] == d
            checks += 1
            if beta:
                formal_degree += d * d
                if n <= 5:
                    determinant *= (1 - z * beta) ** (d * d)
            trace_zero += d * d
            for step in range(9):
                assert sp.denom(sp.Rational(d * d) * beta**step) > 0
                checks += 1
        assert trace_zero == factorial(n)
        checks += 1
        expected_degree = sum(
            dimension(shape) ** 2
            for shape in partitions(n)
            if sp.Rational(1, n) + sp.Rational(
                sum(part * (part - 2 * i + 1) for i, part in enumerate(shape, 1)), n * n
            ) != 0
        )
        assert formal_degree == expected_degree
        checks += 1
        if n <= 5:
            assert sp.Poly(determinant, z).degree() == expected_degree
            checks += 1
        assert determinant.subs(z, 0) == 1
        checks += 1

    moments = {(r["n"], r["step"]): r for r in data["finite_replay"]["moment_rows"]}
    for n in range(2, 12):
        shapes = list(partitions(n))
        for step in range(9):
            trace = sp.Integer(0)
            for shape in shapes:
                d = dimension(shape)
                kappa = sum(part * (part - 2 * i + 1) for i, part in enumerate(shape, 1))
                beta = sp.Rational(1, n) + sp.Rational(kappa, n * n)
                trace += d * d * beta**step
            row = moments[(n, step)]
            recorded = sp.Rational(row["operator_trace"]["numerator"], row["operator_trace"]["denominator"])
            assert sp.simplify(trace - recorded) == 0
            checks += 1
            return_count = sp.simplify(trace * n ** (2 * step) / sp.factorial(n))
            assert return_count.is_Integer
            assert int(return_count) == row["ordered_pair_word_return_count"]
            checks += 2

    print(json.dumps({"status": "C183_SYMPY_PASS", "checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
