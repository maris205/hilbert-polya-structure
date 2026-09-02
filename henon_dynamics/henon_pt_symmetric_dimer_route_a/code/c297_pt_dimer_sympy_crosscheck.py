#!/usr/bin/env python3
"""Independent symbolic matrix audit for HCS-C297."""
from __future__ import annotations

import json
import sympy as sp


def main() -> None:
    k, g, t, z = sp.symbols("k g t z", real=True)
    I = sp.I
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -I], [I, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])
    H = k * sx + I * g * sz
    eta = sp.eye(2) + (g / k) * sy
    delta = k**2 - g**2
    checks = []
    checks.append(sp.simplify(H * H - delta * sp.eye(2)) == sp.zeros(2))
    checks.append(sp.simplify(H.conjugate().T * eta - eta * H) == sp.zeros(2))
    checks.append(sp.simplify(H.conjugate().T * sx - sx * H) == sp.zeros(2))
    checks.append(sp.simplify(H.det() + delta) == 0)
    checks.append(H.trace() == 0)
    checks.append(sp.factor(eta.det()) == sp.factor(delta / k**2))
    checks.append(sp.factor(H.charpoly().as_expr()) == sp.Symbol("lambda")**2 - delta)

    a, b = sp.symbols("a b")
    adot = g * a - I * k * b
    bdot = -I * k * a - g * b
    zdot = sp.simplify((bdot * a - b * adot) / a**2).subs(b, z * a)
    checks.append(sp.expand(zdot - (I * k * (z**2 - 1) - 2 * g * z)) == 0)
    riccati_poly = I * k * (z**2 - 1) - 2 * g * z
    checks.append(sp.simplify(sp.discriminant(riccati_poly, z) + 4 * delta) == 0)

    omega = sp.symbols("omega", positive=True, real=True)
    U = sp.cos(omega * t) * sp.eye(2) - I * sp.sin(omega * t) / omega * H
    dU = sp.diff(U, t)
    checks.append(sp.simplify(dU + I * H * U).subs(omega**2, delta) == sp.zeros(2))
    nu = sp.symbols("nu", positive=True, real=True)
    V = sp.cosh(nu * t) * sp.eye(2) - I * sp.sinh(nu * t) / nu * H
    dV = sp.diff(V, t)
    checks.append(sp.simplify(dV + I * H * V).subs(nu**2, -delta) == sp.zeros(2))
    W = sp.eye(2) - I * t * H
    checks.append(sp.simplify(sp.diff(W, t) + I * H * W).subs(delta, 0) == sp.zeros(2))

    grid_checks = 0
    counts = {"unbroken": 0, "exceptional": 0, "broken": 0}
    for kv in range(1, 9):
        for gv in range(-10, 11):
            d = kv * kv - gv * gv
            label = "unbroken" if d > 0 else "exceptional" if d == 0 else "broken"
            counts[label] += 1
            numeric = H.subs({k: kv, g: gv})
            assert numeric * numeric == d * sp.eye(2)
            assert numeric.det() == -d
            assert sp.factor(eta.subs({k: kv, g: gv}).det()) == sp.Rational(d, kv * kv)
            grid_checks += 3
    assert all(checks), [i for i, value in enumerate(checks) if not value]
    print(json.dumps({"status": "C297_SYMPY_PASS", "symbolic_identities": len(checks), "grid_checks": grid_checks, "checks": len(checks) + grid_checks, "phase_counts": counts}, sort_keys=True))


if __name__ == "__main__":
    main()
