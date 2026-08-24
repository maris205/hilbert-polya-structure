#!/usr/bin/env python3
"""Fresh SymPy reconstruction of the C114 quotient operator."""
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "results/c114_jet_evidence.json").read_text())
u, v, z, lam = sp.symbols("u v z lam")
U = u**2 + sp.Rational(3, 2) * u - sp.Rational(1, 2) * v
V = u
basis = [(0, 0)]
for degree in range(1, 5):
    basis.extend((degree - j, j) for j in range(degree + 1))
index = {monomial: i for i, monomial in enumerate(basis)}
matrix = sp.zeros(15)
for column, (a, b) in enumerate(basis):
    expression = sp.Poly(sp.expand(U**a * V**b), u, v)
    for (i, j), coefficient in expression.terms():
        if i + j <= 4:
            matrix[index[(i, j)], column] = coefficient
reported = sp.Matrix([[sp.sympify(value) for value in row] for row in DATA["operator"]["matrix"]])
assert matrix == reported
assert matrix.trace() == sp.Rational(129, 16)
assert matrix.det() == sp.Rational(1, 2**20)
expected_char = (lam - 1) ** 5 * (lam - sp.Rational(1, 2)) ** 4 * (lam - sp.Rational(1, 4)) ** 3 * (lam - sp.Rational(1, 8)) ** 2 * (lam - sp.Rational(1, 16))
assert sp.expand(matrix.charpoly(lam).as_expr() - expected_char) == 0
expected_detz = (1 - z) ** 5 * (1 - z / 2) ** 4 * (1 - z / 4) ** 3 * (1 - z / 8) ** 2 * (1 - z / 16)
assert sp.expand((sp.eye(15) - z * matrix).det() - expected_detz) == 0
for degree in range(5):
    rows = [i for i, pair in enumerate(basis) if sum(pair) == degree]
    block = matrix.extract(rows, rows)
    assert sp.factor(block.charpoly(lam).as_expr() - sp.prod(lam - sp.Rational(1, 2**k) for k in range(degree + 1))) == 0
print("C114_SYMPY_PASS", 15, 5, 8)
