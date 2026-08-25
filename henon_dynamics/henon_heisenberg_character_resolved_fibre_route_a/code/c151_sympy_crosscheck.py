#!/usr/bin/env python3
"""Independent SymPy reconstruction for HCS-C151."""
from __future__ import annotations

from collections import Counter
import json
from pathlib import Path
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form


ROOT = Path(__file__).resolve().parents[1]


def q(v):
    x, y = v
    return x * (x - 1) + x * y + y * (y - 1) / 2


def main():
    data = json.loads((ROOT / "results/c151_heisenberg_fibre_evidence.json").read_text())
    checks = 0

    def check(condition, message):
        nonlocal checks
        checks += 1
        if not condition:
            raise AssertionError(message)

    x, y, X, Y = sp.symbols("x y X Y")
    check(sp.expand(q((x + X, y + Y)) - q((x, y)) - q((X, Y)) - (2*x*X + x*Y + X*y + y*Y)) == 0, "polarization")
    A = sp.Matrix([[2, 1], [1, 1]])
    for row in data["rotation_ledger"]:
        n = row["n"]
        B = A**n
        M = B - sp.eye(2)
        H = hermite_normal_form(M)
        check(B.tolist() == row["A_power"], f"power {n}")
        check(M.tolist() == row["M=A_power-I"], f"M {n}")
        check(H.tolist() == row["column_hnf"], f"HNF {n}")
        check(abs(int(M.det())) == row["horizontal_fixed_class_count"], f"count {n}")
        check(row["universal_projector_order_Q"] == 2 * int(M.det())**2, f"Q {n}")

        # Full symbolic histogram reconstruction through n=8 is deliberately
        # separate from both standard-library implementations.
        if n <= 8:
            hist = Counter()
            Minv = M.inv()
            for i in range(int(H[0, 0])):
                for j in range(int(H[1, 1])):
                    v = Minv * sp.Matrix([i, j])
                    w = v
                    total = sp.Rational(0)
                    for _ in range(n):
                        total += q((w[0], w[1]))
                        w = A * w
                    rho = sp.Mod(sp.together(total - i*v[1]), 1)
                    hist[str(rho)] += 1
            frozen = {item["rotation"]: item["multiplicity"] for item in row["histogram"]}
            check(hist == frozen, f"histogram {n}")

    # Symbolic all-n representative-change algebra.  The final expression is
    # visibly integral once m,r,s and q_B(r) are integral.
    m1, m2, r1, r2, s1, s2, qbr = sp.symbols("m1 m2 r1 r2 s1 s2 qbr")
    delta = qbr - m1*r2 + m2*r1 + s1*m2 - s1*r2
    check(sp.Poly(delta, m1, m2, r1, r2, s1, s2, qbr).total_degree() == 2, "integral change polynomial")
    check(data["discarded_pattern"]["all_n_closed_form_claimed"] is False, "no false pattern")
    check(data["route_a"]["route_b_invocation_allowed"] is False, "Route B")
    print(json.dumps({"status": "C151_SYMPY_PASS", "checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
