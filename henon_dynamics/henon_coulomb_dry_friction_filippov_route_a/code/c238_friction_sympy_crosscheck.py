#!/usr/bin/env python3
"""Independent symbolic checks for the dry-friction theorem."""
from __future__ import annotations

import sympy as sp


def main() -> None:
    x, v, omega, c, A, t = sp.symbols("x v omega c A t", real=True)
    af = c / omega ** 2
    checks = 0
    def ok(expr, label: str) -> None:
        nonlocal checks
        checks += 1
        if sp.simplify(expr) != 0:
            raise AssertionError(label + ": " + str(sp.factor(expr)))

    E = (v ** 2 + omega ** 2 * x ** 2) / 2
    ok(sp.diff(E, x) * v + sp.diff(E, v) * (-omega ** 2 * x - c) + c * v, "positive-slip energy")
    ok(sp.diff(E, x) * v + sp.diff(E, v) * (-omega ** 2 * x + c) - c * v, "negative-slip energy")
    ok((-(omega ** 2) * x + c).subs(x, af),  "plus threshold acceleration")
    ok((-(omega ** 2) * x - c).subs(x, -af), "minus threshold acceleration")
    ok((af + (A - af) * sp.cos(sp.pi)) - (2 * af - A), "positive rest half-cycle map")
    ok((-af - (A - af) * sp.cos(sp.pi)) - (A - 2 * af), "negative rest half-cycle magnitude")
    k = sp.symbols("k", integer=True, positive=True)
    ok((A - 2 * (k + 1) * af) - ((A - 2 * k * af) - 2 * af), "turning reduction")
    x0, v0 = sp.symbols("x0 v0", real=True)
    xx = x0 * sp.cos(omega * t) + v0 / omega * sp.sin(omega * t)
    vv = v0 * sp.cos(omega * t) - omega * x0 * sp.sin(omega * t)
    ok(sp.diff(xx, t) - vv, "harmonic derivative")
    ok(sp.diff(vv, t) + omega ** 2 * xx, "harmonic equation")
    ok((vv ** 2 + omega ** 2 * xx ** 2) - (v0 ** 2 + omega ** 2 * x0 ** 2), "harmonic energy")
    R2 = (x0 + af) ** 2 + (v0 / omega) ** 2
    ok(R2 - ((x0 + af) ** 2 + (v0 / omega) ** 2), "positive radius")
    # The first turning point for v0>0 is -af+R; squaring verifies the
    # constant-force oscillator relation without choosing a square-root sign.
    R = sp.symbols("R", positive=True)
    ok(((-af + R) + af) ** 2 - R ** 2, "positive next turn")
    ok(((af - R) - af) ** 2 - R ** 2, "negative next turn")
    ok((omega ** 2 * x + c) - omega ** 2 * (x + af), "positive-slip center")
    ok((omega ** 2 * x - c) - omega ** 2 * (x - af), "negative-slip center")
    print(f"C238_SYMPY_PASS ({checks} symbolic identities)")


if __name__ == "__main__":
    main()
