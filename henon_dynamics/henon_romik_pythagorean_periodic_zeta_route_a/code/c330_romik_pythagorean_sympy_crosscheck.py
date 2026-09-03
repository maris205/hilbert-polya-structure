#!/usr/bin/env python3
"""Independent SymPy algebra lane for HCS-C330."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c330_romik_pythagorean_evidence.json"


def main():
    if sys.flags.optimize:
        raise RuntimeError("C330 SymPy lane refuses optimized Python")
    data = json.loads(EVIDENCE.read_text())
    qform = sp.diag(1, 1, -1)
    matrices = [sp.Matrix([[-1, 2, 2], [-2, 1, 2], [-2, 2, 3]]),
                sp.Matrix([[1, 2, 2], [2, 1, 2], [2, 2, 3]]),
                sp.Matrix([[1, -2, 2], [2, -1, 2], [2, -2, 3]])]
    checks = 0
    for matrix in matrices:
        assert matrix.T * qform * matrix == qform
        assert abs(matrix.det()) == 1
        checks += 2
    t = sp.symbols("t")
    inverses = [t / (1 + 2 * t), 1 / (2 + t), 1 / (2 - t)]
    forwards = [t / (1 - 2 * t), 1 / t - 2, 2 - 1 / t]
    for inverse, forward in zip(inverses, forwards):
        assert sp.cancel(forward.subs(t, inverse) - t) == 0
        checks += 1
    for row in data["word_rows"][::7]:
        a, b, c, d = row["mobius_matrix_row_major"]
        x = sp.symbols("x")
        polynomial = sp.expand(c * x ** 2 + (d - a) * x - b)
        assert sp.discriminant(polynomial, x) == row["discriminant"]
        u, v, w = row["pythagorean_triple"]
        assert sp.expand(u ** 2 + v ** 2 - w ** 2) == 0
        checks += 2
    z = sp.symbols("z")
    logarithm = sp.series(sp.log((1 - z) ** 2 / (1 - 3 * z)), z, 0, 13).removeO().expand()
    for row in data["period_count_rows"]:
        assert sp.expand(logarithm.coeff(z, row["n"]) * row["n"] - row["fixed_points"]) == 0
        checks += 1
    print(f"C330 SymPy cross-check: PASS ({checks} symbolic/exact checks)")


if __name__ == "__main__":
    main()
