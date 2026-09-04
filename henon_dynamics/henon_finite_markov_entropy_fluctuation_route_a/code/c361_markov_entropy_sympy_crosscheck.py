#!/usr/bin/env python3
"""Independent symbolic lane for C361."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("c361 sympy crosscheck refuses optimized Python")
import json, sys
from fractions import Fraction
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
OBJ=json.loads((ROOT/"results/c361_markov_entropy_evidence.json").read_text())
count=0
for panel in OBJ["panel_rows"]:
    q=panel["rates"];n=len(q);L=sp.Matrix([[(-sum(q[i]) if i==j else q[i][j]) for j in range(n)] for i in range(n)])
    tau=sp.Matrix(panel["tau"]); z=panel["tree_normalizer"]
    assert (L.T*tau)==sp.zeros(n,1);count+=n
    assert L*sp.ones(n,1)==sp.zeros(n,1);count+=n
    assert sum(sp.Rational(x,z) for x in panel["tau"])==1;count+=1
    rows={r["lambda"]:r for r in OBJ["tilt_rows"] if r["panel"]==panel["panel"]}
    for lam,row in rows.items():
        M=sp.Matrix([[(-sum(q[i]) if i==j else sp.Rational(q[i][j])**(1-lam)*sp.Rational(q[j][i])**lam) for j in range(n)] for i in range(n)])
        partner=1-lam
        N=sp.Matrix([[(-sum(q[i]) if i==j else sp.Rational(q[i][j])**(1-partner)*sp.Rational(q[j][i])**partner) for j in range(n)] for i in range(n)])
        assert M.T==N;count+=n*n
        got=[str(c) for c in M.charpoly().all_coeffs()]
        assert got==row["characteristic_coefficients_descending"];count+=n+1
three=next(p for p in OBJ["panel_rows"] if p["panel"]=="three_cycle")
assert three["stationary"]==["1/3"]*3;count+=3
edges=[r for r in OBJ["edge_rows"] if r["panel"]=="three_cycle"]
assert len(edges)==3 and all(r["epr_term_sign"]==1 for r in edges);count+=4
# With the stored i<j orientations, positivity is checked termwise and the sum reduces to log 2.
sigma=0
for r in edges:
    a=sp.Rational(r["flux_ij"]);b=sp.Rational(r["flux_ji"])
    sigma+=(a-b)*sp.log(a/b); assert sp.simplify((a-b)*sp.log(a/b))>=0;count+=2
assert sp.simplify(sigma-sp.log(2))==0;count+=1
print(f"C361 SymPy PASS: symbolic_assertions={count} version={sp.__version__}")
