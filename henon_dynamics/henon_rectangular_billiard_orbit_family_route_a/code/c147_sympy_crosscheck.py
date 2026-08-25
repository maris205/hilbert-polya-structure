#!/usr/bin/env python3
"""Independent SymPy checks for HCS-C147."""
from __future__ import annotations

import json
from math import gcd
from pathlib import Path
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def main():
    data = json.loads((ROOT / "results/c147_billiard_evidence.json").read_text())
    checks = 0

    def check(condition, message):
        nonlocal checks
        checks += 1
        if not condition:
            raise AssertionError(message)

    L = sp.symbols("L", positive=True)
    P = sp.Matrix([[1, L], [0, 1]])
    check((sp.eye(2) - P).det() == 0 and (sp.eye(2) - P).nullspace() == [sp.Matrix([1, 0])], "full Poincare clean kernel and denominator")
    check(sp.sqrt(1**2 + 8**2) == sp.sqrt(4**2 + 7**2) == sp.sqrt(65), "collision")
    check(gcd(1, 8) == gcd(4, 7) == 1, "primitive witness")
    check(sp.Poly(sp.minpoly(sp.sqrt(2))).degree() == 2, "irrational basis")
    a, b, c, d = sp.symbols("a b c d", integer=True, positive=True)
    expression = sp.expand(a**2 + sp.sqrt(2) * b**2 - c**2 - sp.sqrt(2) * d**2)
    check(sp.collect(expression, sp.sqrt(2), evaluate=False)[sp.Integer(1)] == a**2 - c**2, "rational coefficient")
    check(sp.collect(expression, sp.sqrt(2), evaluate=False)[sp.sqrt(2)] == b**2 - d**2, "irrational coefficient")

    # Möbius formula and ledger totals reconstructed with SymPy's mobius.
    exact_count = sum(int(sp.mobius(k)) * (40 // k) ** 2 for k in range(1, 41))
    check(exact_count == data["count_certificate"]["positive_primitive_direction_count"], "Mobius count")
    for row in data["symmetry_reduced_degeneracy_groups"][:20]:
        square = row["m2_plus_n2"]
        for m, n in row["representatives"]:
            check(m * m + n * n == square, f"degeneracy {square}")
            check(sp.gcd(m, n) == 1, f"primitive {m},{n}")
    check(data["route_a"]["route_b_invocation_allowed"] is False, "Route B")
    print(json.dumps({"status": "C147_SYMPY_PASS", "checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
