#!/usr/bin/env python3
"""Independent exact checker for the C109 dissipative Hénon ledger."""
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
X2 = sp.expand(X**2 + a - Y)
Y2 = sp.expand(b * X)
J = sp.Matrix([[2 * x, -1], [b, 0]])


def q(value: object) -> sp.Expr:
    return sp.factor(sp.sympify(value))


def mat(doc_matrix: list[list[str]]) -> sp.Matrix:
    return sp.Matrix([[q(v) for v in row] for row in doc_matrix])


assert doc["schema"] == "hcs-c109-dissipative-henon-v1"
assert doc["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
assert doc["map"]["formula"] == "F(x,y)=(x^2-(91/16)-y,x/2)"
assert q(doc["map"]["a"]) == a and q(doc["map"]["b"]) == b
assert q(doc["map"]["jacobian_determinant"]) == b
assert sp.Abs(b) < 1

fixed_poly = sp.factor((X - x).subs(y, b * x))
assert sp.expand(fixed_poly - q(doc["fixed_point_polynomial"])) == 0
fixed = [(q(px), q(py)) for px, py in doc["fixed_points"]]
assert fixed == [(sp.Rational(13, 4), sp.Rational(13, 8)), (sp.Rational(-7, 4), sp.Rational(-7, 8))]
for px, py in fixed:
    assert sp.simplify(X.subs({x: px, y: py}) - px) == 0
    assert sp.simplify(Y.subs(x, px) - py) == 0

resultant = sp.factor(sp.resultant(X2 - x, Y2 - y, y))
assert sp.expand(resultant - q(doc["period_two_resultant"])) == 0
expected_dynatomic = sp.factor((4 * x - 5) * (4 * x + 11))
assert sp.expand(expected_dynatomic - q(doc["primitive_period_two_factor"])) == 0
two = [(q(px), q(py)) for px, py in doc["period_two_points"]]
assert two == [(sp.Rational(5, 4), sp.Rational(-11, 8)), (sp.Rational(-11, 4), sp.Rational(5, 8))]
for px, py in two:
    ix = sp.simplify(X.subs({x: px, y: py}))
    iy = sp.simplify(Y.subs(x, px))
    assert (ix, iy) in two
    assert (ix, iy) != (px, py)

expected_names = ["p_plus", "p_minus", "q_plus", "q_minus"]
assert [item["name"] for item in doc["cycle_ledger"]] == expected_names
expected_points = fixed + two
for item, (px, py) in zip(doc["cycle_ledger"], expected_points):
    jac = J.subs({x: px, y: py})
    assert mat(item["jacobian"]) == jac
    den = sp.factor((sp.eye(2) - jac).det())
    assert q(item["local_denominator_det_I_minus_DF"]) == den
    assert q(item["local_weight"]) == 1 / den
    assert q(item["jacobian_determinant"]) == b

assert doc["transition"] == {"p_plus": "p_plus", "p_minus": "p_minus", "q_plus": "q_minus", "q_minus": "q_plus"}
assert doc["witness_state_order"] == expected_names
weights = [q(item["local_weight"]) for item in doc["cycle_ledger"]]
M = sp.zeros(4)
targets = [0, 1, 3, 2]
for i, j in enumerate(targets):
    M[i, j] = weights[i]
assert mat(doc["witness_matrix"]) == M
for n in range(1, 7):
    assert q(doc["weighted_trace_sequence_n1_to_6"][str(n)]) == sp.trace(M**n)
det_expr = sp.factor((sp.eye(4) - z * M).det())
assert sp.expand(det_expr - q(doc["finite_witness_determinant"])) == 0
poly = sp.Poly(sp.expand(det_expr), z)
for k in range(poly.degree() + 1):
    assert q(doc["finite_witness_determinant_coefficients"][str(k)]) == poly.nth(k)

assert doc["unweighted_periodic_point_counts"] == {str(n): (2 if n % 2 else 4) for n in range(1, 7)}
assert doc["primitive_orbit_counts"] == {"1": 2, "2": 1}
assert doc["verdict"]["A1"] == "A1_PARTIAL_CERTIFIED"
assert doc["verdict"]["A2"] == "A2_CERTIFIED_PREFIX"
assert doc["verdict"]["A3"] == "A3_NOT_ADDRESSED"
assert doc["verdict"]["A4"] == "A4_FAIL"
print("C109_CHECK_PASS")
