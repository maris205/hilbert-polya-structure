#!/usr/bin/env python3
import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
d=json.loads((ROOT/"results/c113_memory_evidence.json").read_text())
x,y,z,lam=sp.symbols('x y z lam')
k=sp.Rational(1,2)
J=lambda u:sp.Matrix([[2*u,-1,-k],[1,0,0],[0,1,0]])
r=sp.sqrt(5)
for row,u in zip(d["fixed_point_rows"],[sp.Rational(5,4)-r,sp.Rational(5,4)+r]):
    assert sp.simplify(sp.sympify(row["characteristic_polynomial"])-J(u).charpoly(lam).as_expr())==0
m=J(sp.Rational(1,4))*J(sp.Rational(-7,4))
assert sp.simplify(sp.sympify(d["period_two_row"]["characteristic_polynomial"])-m.charpoly(lam).as_expr())==0
print("C113_SYMPY_PASS")
