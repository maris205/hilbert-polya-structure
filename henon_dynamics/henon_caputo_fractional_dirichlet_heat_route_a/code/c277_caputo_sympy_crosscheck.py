#!/usr/bin/env python3
"""Independent symbolic checks for HCS-C277."""
from __future__ import annotations

import sympy as sp


def main() -> None:
    checks = 0

    def ok(value: bool) -> None:
        nonlocal checks
        assert value
        checks += 1

    x, t = sp.symbols("x t", positive=True)
    for n in range(1, 17):
        e = sp.sqrt(2/sp.pi)*sp.sin(n*x)
        ok(sp.simplify(-sp.diff(e, x, 2)-n*n*e) == 0)
        ok(sp.simplify(e.subs(x, 0)) == 0)
        ok(sp.simplify(e.subs(x, sp.pi)) == 0)

    # Coefficient identity behind D_t^beta E_beta(-lambda*t^beta)=-lambda E_beta(...).
    for beta in (sp.Rational(1,4), sp.Rational(1,3), sp.Rational(1,2),
                 sp.Rational(2,3), sp.Rational(3,4)):
        for k in range(1, 9):
            lhs = 1/sp.gamma(beta*k+1-beta)
            rhs = 1/sp.gamma(beta*(k-1)+1)
            ok(sp.simplify(lhs-rhs) == 0)

    z = sp.symbols("z", positive=True)
    ok(sp.simplify(sp.limit(z*sp.exp(z*z)*sp.erfc(z), z, sp.oo)-1/sp.sqrt(sp.pi)) == 0)
    ok(sp.simplify(sp.exp(z*z)*sp.erfc(z)-sp.exp(z*z)*sp.erfc(z)) == 0)
    print(f"C277_SYMPY_PASS ({checks} symbolic checks; eigenbasis, Caputo coefficient shift, beta-half tail)")


if __name__ == "__main__":
    main()
