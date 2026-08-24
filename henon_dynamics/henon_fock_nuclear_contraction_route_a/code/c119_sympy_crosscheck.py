#!/usr/bin/env python3
"""Fresh symbolic reconstruction of all finite C119 certificate fields."""
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "results/c119_fock_evidence.json").read_text())
A = sp.Matrix([[sp.Rational(3, 4), sp.Rational(-1, 4)], [sp.Rational(1, 2), 0]])
lam, z = sp.symbols("lam z")
checks = 0
assert sp.expand(A.charpoly(lam).as_expr() - (lam-sp.Rational(1,2))*(lam-sp.Rational(1,4))) == 0; checks += 1
assert A.det() == sp.Rational(1,8); checks += 1
gram_roots = set((A.T*A).eigenvals())
assert gram_roots == {(7+3*sp.sqrt(5))/16, (7-3*sp.sqrt(5))/16}; checks += 1
traces = []
for n in range(1, 9):
    value = sp.factor(1 / ((1-sp.Rational(1,2)**n)*(1-sp.Rational(1,4)**n)))
    assert value == sp.Rational(DATA["trace_and_fredholm_data"]["trace_powers_n1_to_8"][str(n)])
    traces.append(value); checks += 1
series = sp.Integer(1)
exponent = -sum(traces[n-1]*z**n/n for n in range(1,9))
series = sp.series(sp.exp(exponent), z, 0, 9).removeO().expand()
reported = [sp.Rational(v) for v in DATA["trace_and_fredholm_data"]["taylor_coefficients_ascending_z0_to_z8"]]
assert [series.coeff(z,k) for k in range(9)] == reported; checks += 1
for k, row in enumerate(DATA["zero_divisor"]["prefix_k0_to_8"]):
    assert len([(i,j) for i in range(k+1) for j in range(k+1) if i+2*j == k]) == row["multiplicity"]
    checks += 1
print("C119_SYMPY_PASS", checks)
