#!/usr/bin/env python3
"""Symbolic resultant and determinant-prefix cross-check."""
from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
doc = json.loads((ROOT / "results/c108_holomorphic_evidence.json").read_text())
x, y = sp.symbols("x y")
a = sp.Rational(1, 4)
res = sp.factor(sp.resultant(y - x**2 + a*x, x - y**2 + a*y, y))
assert sp.simplify(res - sp.sympify(doc["period_two_resultant"])) == 0
assert sp.Rational(-1664, 1725) == sp.Rational(doc["weighted_traces"]["2"])
assert sp.Rational(832, 1725) == sp.Rational(doc["formal_determinant_prefix"][2])
print("C108_SYMPY_PASS")
