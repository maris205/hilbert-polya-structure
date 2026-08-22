#!/usr/bin/env python3
"""Independent SymPy cross-check of C109 elimination and transfer algebra."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

PROJECT = Path(__file__).resolve().parents[1]
doc = json.loads((PROJECT / "results/c109_dissipative_evidence.json").read_text())
x, y, z = sp.symbols("x y z")
a = sp.Rational(-91, 16)
b = sp.Rational(1, 2)
X = x**2 + a - y
Y = b * x
resultant = sp.factor(sp.resultant(sp.expand(X**2 + a - Y) - x, sp.expand(b * X) - y, y))
assert sp.expand(resultant - sp.sympify(doc["period_two_resultant"])) == 0
assert sp.factor(resultant / ((4 * x - 13) * (4 * x + 7) / 256)) == sp.sympify(doc["primitive_period_two_factor"])

M = sp.Matrix([
    [-sp.Rational(1, 5), 0, 0, 0],
    [0, sp.Rational(1, 5), 0, 0],
    [0, 0, 0, -1],
    [0, 0, sp.Rational(1, 7), 0],
])
for n in range(1, 7):
    assert sp.factor(sp.trace(M**n)) == sp.sympify(doc["weighted_trace_sequence_n1_to_6"][str(n)])
det = sp.factor((sp.eye(4) - z * M).det())
assert sp.expand(det - sp.sympify(doc["finite_witness_determinant"])) == 0
assert sp.factor(sp.Poly(det, z).nth(2)) == sp.Rational(18, 175)
assert sp.factor(sp.Poly(det, z).nth(4)) == -sp.Rational(1, 175)
print("C109_SYMPY_PASS")
