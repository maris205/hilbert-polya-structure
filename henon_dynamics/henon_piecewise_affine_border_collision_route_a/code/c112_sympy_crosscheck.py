#!/usr/bin/env python3
import json
from pathlib import Path
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]; d=json.loads((ROOT/"results/c112_border_evidence.json").read_text())
z=sp.Symbol('z'); b=sp.Matrix([[-5,-1],[1,0]]); w=[sp.Rational(1,2),sp.Rational(2,3)]; A=sp.zeros(4)
for i in range(2):
    for j in range(2): A[2*i:2*i+2,2*j:2*j+2]=w[j]*b
assert sp.simplify(sp.factor((sp.eye(4)-z*A).det())-sp.sympify(d["weighted_transfer_determinant"])) == 0
for n,s in d["weighted_transfer_traces"].items():
    assert sp.simplify(sp.factor(sp.trace(A**int(n)))-sp.sympify(s)) == 0
print("C112_SYMPY_PASS")
