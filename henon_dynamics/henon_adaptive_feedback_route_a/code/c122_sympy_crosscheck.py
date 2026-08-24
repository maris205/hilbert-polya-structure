#!/usr/bin/env python3
"""Fresh symbolic reconstruction of the C122 headline identities."""
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "results" / "c122_adaptive_evidence.json").read_text())
x, y, a, X, Y, A, z = sp.symbols("x y a X Y A z")
F = sp.Matrix([x**2 + a - y, x, a / 2 + 3 * x - sp.Rational(1, 2)])
old_a = 2 * A - 6 * Y + 1
Inv = sp.Matrix([Y, Y**2 + old_a - X, old_a])
J = F.jacobian([x, y, a])
checks = []
checks += [sp.simplify(v) == 0 for v in Inv.subs({X: F[0], Y: F[1], A: F[2]}) - sp.Matrix([x, y, a])]
checks += [sp.simplify(v) == 0 for v in F.subs({x: Inv[0], y: Inv[1], a: Inv[2]}, simultaneous=True) - sp.Matrix([X, Y, A])]
checks.append(J.det() == sp.Rational(1, 2))
cycle = [sp.Matrix([1, -1, -3]), sp.Matrix([-1, 1, 1])]
for u, v in zip(cycle, cycle[1:] + cycle[:1]):
    checks += [sp.simplify(t) == 0 for t in F.subs({x: u[0], y: u[1], a: u[2]}) - v]
M = J.subs(x, -1) * J.subs(x, 1)
checks.append(M == sp.Matrix([[-2, 2, sp.Rational(-3, 2)], [2, -1, 1], [sp.Rational(15, 2), -3, sp.Rational(13, 4)]]))
checks.append(sp.simplify((sp.eye(3) - z * M).det() - (1 - z / 4 + 5 * z**2 / 2 - z**3 / 4)) == 0)
for q in (-2 + sp.sqrt(5), -2 - sp.sqrt(5)):
    state = sp.Matrix([q, q, 6 * q - 1])
    checks += [sp.simplify(t) == 0 for t in F.subs({x: state[0], y: state[1], a: state[2]}) - state]
verdict = data["route_a_verdict"]
checks += [
    verdict["A1"] == "A1_WEAK",
    verdict["A2"] == "A2_FAIL",
    verdict["A3"] == "A3_FAIL",
    verdict["A4"] == "A4_FAIL",
    verdict["overall"] == "ROUTE_A_EXPLORATORY",
    data["claims"]["prime_like_target_correspondence"] is False,
    data["claims"]["target_divisor_match"] is False,
    data["claims"]["analytic_bridge"] is False,
]
assert all(checks)
print(json.dumps({"status": "C122_SYMPY_CROSSCHECK_PASS", "checks": len(checks)}, sort_keys=True))
