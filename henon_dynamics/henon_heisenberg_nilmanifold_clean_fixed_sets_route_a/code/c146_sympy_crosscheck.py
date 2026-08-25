#!/usr/bin/env python3
"""Independent SymPy reconstruction for HCS-C146."""
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def main():
    data = json.loads((ROOT / "results/c146_heisenberg_evidence.json").read_text())
    checks = 0

    def check(condition, message):
        nonlocal checks
        checks += 1
        if not condition:
            raise AssertionError(message)

    x, y, X, Y, z = sp.symbols("x y X Y z")
    q = lambda a, b: a * (a - 1) + a * b + b * (b - 1) / 2
    polarization = sp.expand(q(x + X, y + Y) - q(x, y) - q(X, Y))
    check(sp.expand(polarization - (2 * x * X + x * Y + X * y + y * Y)) == 0, "polarization")

    jac = sp.Matrix([[2, 1, 0], [1, 1, 0], [sp.diff(q(x, y), x), sp.diff(q(x, y), y), 1]])
    t = sp.symbols("t")
    check(sp.factor(jac.charpoly(t).as_expr()) == (t - 1) * (t**2 - 3 * t + 1), "Jacobian polynomial")
    check(sp.factor((sp.eye(3) - jac).det()) == 0, "singular denominator")

    A = sp.Matrix([[2, 1], [1, 1]])
    for row in data["iterate_ledger"]:
        n = row["n"]
        an = A**n
        check(an.tolist() == row["A_power"], f"power {n}")
        check(int(an.trace()) == row["trace"], f"trace {n}")
        check(int((an - sp.eye(2)).det()) == row["det_A_power_minus_I"], f"det {n}")
        derivative = sp.zeros(3)
        derivative[:2, :2] = an
        derivative[2, 2] = 1
        check(sp.factor((sp.eye(3) - derivative).det()) == 0, f"central singularity {n}")

    v = sp.Matrix([sp.Rational(1, 5), sp.Rational(2, 5)])
    av = A * v
    q2 = sp.simplify(q(v[0], v[1]) + q(av[0], av[1]))
    shift = (A**2 - sp.eye(2)) * v
    condition = sp.simplify(q2 - shift[0] * v[1])
    check(shift == sp.Matrix([2, 1]), "period-two base class")
    check(q2 == 0, "period-two q")
    check(condition == sp.Rational(-4, 5), "period-two obstruction")
    check(data["route_a"]["route_b_invocation_allowed"] is False, "Route B")
    print(json.dumps({"status": "C146_SYMPY_PASS", "checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
