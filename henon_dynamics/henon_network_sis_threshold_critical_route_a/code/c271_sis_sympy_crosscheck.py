#!/usr/bin/env python3
"""Independent symbolic reconstruction for HCS-C271."""
from __future__ import annotations

import sympy as sp


def main() -> None:
    checks = 0

    def ok(v: bool) -> None:
        nonlocal checks
        assert v
        checks += 1

    y, y0, t, beta, delta, r = sp.symbols("y y0 t beta delta r", positive=True)
    f = (beta * r - delta) * y - beta * r * y**2
    xstar = 1 - delta / (beta * r)
    ok(sp.simplify(f.subs(y, xstar)) == 0)
    ok(sp.simplify(sp.diff(f, y).subs(y, xstar) - (delta - beta * r)) == 0)
    critical = y0 / (1 + delta * y0 * t)
    ok(sp.simplify(sp.diff(critical, t) + delta * critical**2) == 0)
    ok(sp.limit(t * critical, t, sp.oo) == 1 / delta)

    for n in range(2, 11):
        A = sp.zeros(n)
        for i in range(n):
            A[i, (i + 1) % n] = 1
        one = sp.ones(n, 1)
        ok(A * one == one)
        M = beta * A - delta * sp.eye(n)
        ok(M * one == (beta - delta) * one)
        v = one
        w = one / n
        kappa = beta * (w.T * sp.diag(*list(v)) * A * v)[0]
        ok(sp.simplify(kappa - beta) == 0)

    # The endemic Jacobian identity for any r-regular owner.
    A2 = sp.Matrix([[0, r], [r, 0]])
    xs = sp.Matrix([xstar, xstar])
    J = beta * sp.diag(1 - xs[0], 1 - xs[1]) * A2 - beta * sp.diag(*(A2 * xs)) - delta * sp.eye(2)
    ok(sp.simplify(J * sp.ones(2, 1) - (delta - beta * r) * sp.ones(2, 1)) == sp.zeros(2, 1))
    ok(sp.simplify(sp.diff(xstar, beta) - delta / (beta**2 * r)) == 0)
    print(f"C271_SYMPY_PASS ({checks} symbolic checks; scalar center law and regular-network Jacobian)")


if __name__ == "__main__":
    main()
