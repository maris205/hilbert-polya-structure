#!/usr/bin/env python3
"""Independent symbolic identities for HCS-C278."""
from __future__ import annotations

import sympy as sp


def main() -> None:
    p1, p2, z = sp.symbols("p1 p2 z", real=True, positive=False)
    p1d = -p1 * p2 * z
    p2d = p1 * p2 * z
    qd = (p2 - p1) * (1 - z)
    zd = -z * qd
    P = p1 + p2
    E = p1**2 + p2**2 + 2 * p1 * p2 * z
    checks = []
    checks.append(sp.simplify(sp.diff(P, p1) * p1d + sp.diff(P, p2) * p2d) == 0)
    Ed = sp.diff(E, p1) * p1d + sp.diff(E, p2) * p2d + sp.diff(E, z) * zd
    checks.append(sp.simplify(Ed) == 0)

    P0, D, t = sp.symbols("P D t", positive=True)
    a = D * t / 2
    A = P0**2 / D**2 - 1
    y = 1 + A * sp.cosh(a) ** 2
    p = D * sp.tanh(a)
    checks.append(sp.simplify(sp.diff(y, t) - p * (y - 1)) == 0)
    checks.append(sp.simplify(sp.diff(p, t) - (P0**2 - p**2) / (2 * y)) == 0)
    checks.append(sp.simplify(sp.diff(y, t) ** 2 - D**2 * (y - 1) * (y - P0**2 / D**2)) == 0)

    s = sp.symbols("s", positive=True)
    B = 1 - P0**2 / D**2
    yo = 1 + B * sp.sinh(D * s / 2) ** 2
    po = -D * sp.coth(D * s / 2)
    checks.append(sp.simplify(-sp.diff(yo, s) - po * (yo - 1)) == 0)
    checks.append(sp.simplify(-sp.diff(po, s) - (P0**2 - po**2) / (2 * yo)) == 0)
    checks.append(sp.simplify(sp.limit((sp.log(yo) / s**2), s, 0) - (D**2 - P0**2) / 4) == 0)
    checks.append(sp.simplify(sp.limit(po * s, s, 0) + 2) == 0)

    alpha = sp.symbols("alpha", nonnegative=True)
    Em = (P0**2 + D**2) / 2
    Ep = (1 - alpha) * Em + alpha * P0**2
    checks.append(sp.simplify(Em - Ep - alpha * (D**2 - P0**2) / 2) == 0)
    assert all(checks), checks
    print(f"C278_SYMPY_PASS ({len(checks)} symbolic identities)")


if __name__ == "__main__":
    main()
