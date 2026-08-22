#!/usr/bin/env python3
"""Independent exact checker for the C108 period-one/two ledger."""
from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
doc = json.loads((ROOT / "results/c108_holomorphic_evidence.json").read_text())
x, y, z, w = sp.symbols("x y z w")
a = sp.Rational(1, 4)
assert doc["map"]["formula"] == "F(z,w)=(w,w^2-(1/4)z)"
assert doc["map"]["jacobian_determinant"] == "1/4"
assert sp.simplify(sp.factor(x - (x**2 - a * x)) - sp.sympify(doc["fixed_point_polynomial"])) == 0
assert {tuple(p["point"]) for p in doc["fixed_points"]} == {("0", "0"), ("5/4", "5/4")}
f1 = y - (x**2 - a * x)
f2 = x - (y**2 - a * y)
resultant = sp.factor(sp.resultant(f1, f2, y))
assert sp.simplify(resultant - sp.sympify(doc["period_two_resultant"])) == 0
assert len(doc["period_two_fixed_points"]) == 4
assert doc["weighted_traces"] == {"1": "0", "2": "-1664/1725"}
assert doc["formal_determinant_prefix"] == ["1/1", "0", "832/1725"]
current = z
inv = {z: 4 * z**2 - 4 * w, w: z}
degrees = []
for _ in range(3):
    current = sp.expand(current.xreplace(inv))
    degrees.append(sp.Poly(current, z, w).total_degree())
assert degrees == doc["inverse_pullback_degree_growth"] == [2, 4, 8]
assert doc["verdict"]["A1"] == "A1_OPEN"
assert doc["verdict"]["A2"] == "A2_CERTIFIED_PREFIX"
print("C108_CHECK_PASS")
