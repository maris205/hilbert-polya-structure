#!/usr/bin/env python3
"""Independent SymPy reconstruction of the C139 determinant and sentinels."""
from __future__ import annotations

import itertools
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c139_marker_evidence.json"


def counts(word, width):
    values = [0] * (2 ** width)
    for start in range(len(word)):
        index = 0
        for offset in range(width):
            index = 2 * index + word[(start + offset) % len(word)]
        values[index] += 1
    return tuple(values)


def vector(word):
    return counts(word, 2) + (counts(word, 4)[3],)


def main():
    data = json.loads(EVIDENCE.read_text())
    checks = 0

    def ck(condition, label):
        nonlocal checks
        if not bool(condition):
            raise AssertionError(label)
        checks += 1

    x00, x01, x10, x11, y = sp.symbols("x00 x01 x10 x11 y")
    variables = (x00, x01, x10, x11, y)
    edge = {(0, 0): x00, (0, 1): x01, (1, 0): x10, (1, 1): x11}
    states = tuple(itertools.product((0, 1), repeat=3))
    index = {state: position for position, state in enumerate(states)}
    matrix = sp.zeros(8)
    for a, b, c in states:
        for d in (0, 1):
            matrix[index[(a, b, c)], index[(b, c, d)]] = edge[(a, b)] * (y if (a, b, c, d) == (0, 0, 1, 1) else 1)
    determinant = sp.expand((sp.eye(8) - matrix).det())
    expected = 1 - x00 - x11 - x01 * x10 + x00 * x11 + (1 - y) * x00 * x01 * x10 * x11
    ck(sp.expand(determinant - expected) == 0, "determinant")
    ck(sp.expand(determinant.subs(y, 1) - (1 - x00 - x11 - x01 * x10 + x00 * x11)) == 0, "C135 reduction")
    receipt = {
        ",".join(map(str, monomial)): int(coefficient)
        for monomial, coefficient in sp.Poly(determinant, *variables).terms()
    }
    ck(receipt == data["frozen_model"]["formal_determinant_receipt"], "det receipt")

    power = sp.eye(8)
    for n, row in enumerate(data["replay_prefix"]["rows"], start=1):
        power = power * matrix
        trace = sp.Poly(sp.expand(sp.trace(power)), *variables)
        trace_receipt = {",".join(map(str, monomial)): int(coefficient) for monomial, coefficient in trace.terms()}
        ck(trace_receipt == row["weighted_trace_coefficients"], f"trace n={n}")
        ck(sum(trace_receipt.values()) == 2 ** n, f"trace mass n={n}")

    first = tuple(map(int, "001011"))
    second = tuple(map(int, "001101"))
    for width in (1, 2, 3):
        ck(counts(first, width) == counts(second, width), f"memory equality k={width}")
    ck(counts(first, 4)[3] == 0 and counts(second, 4)[3] == 1, "marker separation")
    residual_first = tuple(map(int, "0101111"))
    residual_second = tuple(map(int, "0110111"))
    ck(vector(residual_first) == vector(residual_second), "residual collision")
    ck(residual_second not in [residual_first[k:] + residual_first[:k] for k in range(7)], "residual nonrotation")

    embedding_rows = []
    for sign2, sign3, sign5 in itertools.product((-1, 1), repeat=3):
        embedding_rows.append([1, sign2 * sp.sqrt(2), sign3 * sp.sqrt(3), sign2 * sign3 * sp.sqrt(6), sign5 * sp.sqrt(5)])
    ck(sp.Matrix(embedding_rows).rank() == 5, "basis independence")
    sqrt6_polynomial = sp.Poly(sp.minpoly(sp.sqrt(6)))
    ck(sqrt6_polynomial.degree() == 2 and sqrt6_polynomial.all_coeffs() == [1, 0, -6], "sqrt6 irrationality")

    print(json.dumps({"status": "C139_SYMPY_PASS", "checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
