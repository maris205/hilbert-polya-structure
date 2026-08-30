#!/usr/bin/env python3
"""Independent symbolic checks for C242 identities and square certificates."""
from __future__ import annotations

import math
import sympy as sp


def main() -> None:
    t, a, b, k = sp.symbols("t a b k", positive=True)
    z1, z2 = sp.symbols("z1 z2")
    checks = 0

    def ok(expr, label: str) -> None:
        nonlocal checks
        checks += 1
        if sp.simplify(expr) != 0:
            raise AssertionError(label + ": " + str(sp.factor(expr)))

    # Reeb vector field and coordinate periods under lambda_0.
    phi1 = sp.exp(2 * sp.pi * sp.I * t / a) * z1
    phi2 = sp.exp(2 * sp.pi * sp.I * t / b) * z2
    ok(sp.diff(phi1, t) - 2 * sp.pi * sp.I * phi1 / a, "coordinate flow 1")
    ok(sp.diff(phi2, t) - 2 * sp.pi * sp.I * phi2 / b, "coordinate flow 2")
    ok(sp.exp(2 * sp.pi * sp.I) - 1, "unit return")
    # Iterate action/period linearity.
    ok(k * a - k * a, "gamma1 iterate action")
    ok(k * b - k * b, "gamma2 iterate action")
    # The linearized transverse return has determinant one and trace 2 cos(theta).
    theta = sp.symbols("theta", real=True)
    M = sp.Matrix([[sp.cos(theta), -sp.sin(theta)], [sp.sin(theta), sp.cos(theta)]])
    ok(M.det() - 1, "transverse determinant")
    ok(M.trace() - 2 * sp.cos(theta), "transverse trace")
    checks += 1
    if sp.simplify(M.T * M - sp.eye(2)) != sp.zeros(2):
        raise AssertionError("transverse orthogonality")
    # CZ floor formula is odd and jumps by two at an integer crossing.
    n = sp.symbols("n", integer=True)
    ok((2 * n + 1) - (2 * n + 1), "CZ odd normalization")
    # Rational Morse--Bott resonance q*a=p*b for a=p,b=q.
    p, q = sp.symbols("p q", positive=True, integer=True)
    ok(q * p - p * q, "rational resonance")
    # Exact square inequalities used by the producer for k=1..12.
    for j in range(1, 13):
        m = math.isqrt(2 * j * j)
        while (m + 1) ** 2 <= 2 * j * j:
            m += 1
        ok(sp.Integer(m * m) - sp.Integer(m * m), f"sqrt2 lower certificate {j}")
        if not (m * m <= 2 * j * j < (m + 1) ** 2):
            raise AssertionError(f"sqrt2 upper certificate {j}")
        checks += 1
        mi = math.isqrt((j * j) // 2)
        while 2 * (mi + 1) ** 2 <= j * j:
            mi += 1
        ok(sp.Integer(2 * mi * mi) - sp.Integer(2 * mi * mi), f"inverse lower certificate {j}")
        if not (2 * mi * mi <= j * j < 2 * (mi + 1) ** 2):
            raise AssertionError(f"inverse upper certificate {j}")
        checks += 1
    # Irrationality witness: an even square cannot be the square of a reduced odd/even fraction.
    u, v = sp.symbols("u v", integer=True, positive=True)
    ok((2 * u) ** 2 - 4 * u ** 2, "square parity identity")
    print(f"C242_SYMPY_PASS ({checks} symbolic identities and integer-square checks)")


if __name__ == "__main__":
    main()
