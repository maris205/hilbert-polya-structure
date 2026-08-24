#!/usr/bin/env python3
"""Symbolic Newton/determinant cross-check for C117."""
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
D = json.loads((ROOT / "results/c117_markov_evidence.json").read_text())


def parse_matrix(rows: list[list[str]]) -> sp.Matrix:
    return sp.Matrix([[sp.Rational(x) for x in row] for row in rows])


def newton_coefficients(a: sp.Matrix) -> list[sp.Expr]:
    # det(I-zA)=sum c_k z^k; k*c_k=-sum_{i=1}^k c_(k-i) Tr(A^i)
    c = [sp.Integer(1)]
    for k in range(1, a.rows + 1):
        c.append(sp.factor(-sum(c[k-i] * sp.trace(a**i) for i in range(1, k+1)) / k))
    return c


checks = 0
for section, mkey, pkey, tkey in (
    ("tangent_cocycle", "first_moment_operator", "first_moment_det_I_minus_z", "first_moment_traces"),
    ("symmetric_second_moment_cocycle", "operator", "det_I_minus_z", "traces"),
):
    a = parse_matrix(D[section][mkey])
    coeff = newton_coefficients(a)
    assert [str(sp.factor(x)) for x in coeff] == D[section][pkey]
    checks += len(coeff)
    for n in range(1, 7):
        assert str(sp.factor(sp.trace(a**n))) == D[section][tkey][str(n)]
        checks += 1

gap = parse_matrix(D["stationary_averaging_control"]["intermittency_gap"])
assert gap.rank() == 1 and gap != sp.zeros(3)
checks += 2
print(json.dumps({"status": "C117_SYMPY_CROSSCHECK_PASS", "checks": checks}, sort_keys=True))
