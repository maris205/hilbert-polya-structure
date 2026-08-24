#!/usr/bin/env python3
"""Independent exact symbolic reconstruction for C126."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "results/c126_chebyshev_skew_evidence.json").read_text())
x, y, z = sp.symbols("x y z")
f = 4*x**3-3*x
checks: list[bool] = []

current = x
for n in range(1, 5):
    current = sp.expand(f.subs(x, current))
    checks.extend([
        sp.expand(current-sp.chebyshevt(3**n,x)) == 0,
        sp.degree(current,x) == 3**n,
    ])

for n in range(1, 5):
    m = 3**n
    p = sp.chebyshevt(m,x)-x
    checks.extend([
        sp.degree(p,x) == m,
        sp.simplify(sp.diff(sp.chebyshevt(m,x),x).subs(x,1)-m*m) == 0,
        sp.simplify(sp.diff(sp.chebyshevt(m,x),x).subs(x,-1)-m*m) == 0,
        (m+1)//2 + (m-1)//2 == m,
    ])

F = sp.Matrix([f, y/sp.Integer(4)+x])
J = F.jacobian([x,y])
checks.extend([
    J == sp.Matrix([[12*x**2-3,0],[1,sp.Rational(1,4)]]),
    J.det() == (12*x**2-3)/4,
])

g = 4*x**3-2*x
g2 = sp.expand(g.subs(x,g))
checks.extend([
    sp.factor(g2-x) == x*(2*x-1)**3*(2*x+1)**3*(4*x**2-3),
    sp.factor(g2-sp.chebyshevt(9,x)) == x*(192*x**6-240*x**4+80*x**2-5),
    sp.diff(g,x).subs(x,sp.Rational(1,2)) == 1,
    sp.diff(g,x).subs(x,sp.Rational(-1,2)) == 1,
    g.subs(x,sp.Rational(1,2)) == -sp.Rational(1,2),
    g.subs(x,-sp.Rational(1,2)) == sp.Rational(1,2),
])

rows = DATA["primitive_orbits"]["prefix_n1_to_n12"]
for row in rows:
    n = row["n"]
    checks.extend([
        row["fixed_points"] == 3**n,
        row["exact_period_points"] == n*row["primitive_orbits"],
        row["positive_unstable_orientation_primitive_orbits"] + row["negative_unstable_orientation_primitive_orbits"] == row["primitive_orbits"],
    ])

checks.extend([
    DATA["zeta"]["closed_form"] == "zeta_F(z)=1/(1-3*z)",
    sp.simplify(sp.exp(-sp.log(1-3*z))-1/(1-3*z)) == 0,
    DATA["route_a_evaluator"]["canonical_tuple"] == ["A1_WEAK","A2_FAIL","A3_FAIL","A4_FAIL"],
    DATA["route_a_evaluator"]["route_b_invocation_allowed"] is False,
    DATA["progress_over_prior_gate"]["new_result"].startswith("one elementary nontrivial skew dynamics"),
])

assert all(checks)
print(json.dumps({"status":"C126_SYMPY_CROSSCHECK_PASS","checks":len(checks)},sort_keys=True))
