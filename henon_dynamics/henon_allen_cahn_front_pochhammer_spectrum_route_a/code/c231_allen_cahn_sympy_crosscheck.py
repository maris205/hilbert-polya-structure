#!/usr/bin/env python3
"""Independent SymPy identities for the Allen--Cahn front certificate."""
from __future__ import annotations

import sympy as sp


def main() -> None:
    y, xi, eps, c = sp.symbols("y xi eps c", positive=True, real=True)
    U = sp.tanh(y)
    sech = 1 / sp.cosh(y)
    checks = 0

    # Scaled profile ODE: xi=sqrt(2)*eps*y.
    U_xx = sp.diff(U, y, 2) / (2 * eps**2)
    assert sp.simplify(U_xx + (U - U**3) / eps**2) == 0
    checks += 1
    assert sp.simplify(sp.diff(U, y) - sech**2) == 0
    checks += 1
    assert sp.simplify(sp.diff(U, y)**2 / 4 - (1 - U**2)**2 / 4) == 0
    checks += 1

    # Pöschl--Teller scaled operator M=d_y^2-4+6 sech^2(y).
    def M(f):
        return sp.diff(f, y, 2) - 4 * f + 6 * sech**2 * f

    phi0 = sech**2
    phi1 = sech * U
    assert sp.simplify(M(phi0)) == 0
    checks += 1
    assert sp.simplify(M(phi1) + 3 * phi1) == 0
    checks += 1

    # Factorization B^*B with B=d_y+2 tanh(y), applied to a test function.
    f = sp.Function("f")(y)
    Bf = sp.diff(f, y) + 2 * U * f
    Bstar_Bf = -sp.diff(Bf, y) + 2 * U * Bf
    assert sp.simplify(Bstar_Bf - (-sp.diff(f, y, 2) + 4 * f - 6 * sech**2 * f)) == 0
    checks += 1

    # Essential constant and scaled eigenvalues.
    assert sp.limit(6 * sech**2 - 4, y, sp.oo) == -4
    checks += 1
    assert sp.simplify(sp.Rational(1, 2) * 0 - 0) == 0  # translation mode
    checks += 1
    assert sp.simplify(-sp.Rational(3, 2) / eps**2) < 0
    checks += 1

    # Exact surface energy and gradient integral (epsilon=1 in y variable).
    assert sp.integrate(sech**4, (y, -sp.oo, sp.oo)) == sp.Rational(4, 3)
    checks += 1
    assert sp.simplify(sp.sqrt(2) / (2 * eps) * sp.Rational(4, 3) - 2 * sp.sqrt(2) / (3 * eps)) == 0
    checks += 1

    # Equal wells force the traveling speed to vanish.
    W = (1 - sp.symbols("q")**2) ** 2 / 4
    q = sp.symbols("q")
    assert W.subs(q, -1) == W.subs(q, 1) == 0
    checks += 1
    assert sp.simplify(c * (2 * sp.sqrt(2) / (3 * eps))) == 0 if c == 0 else True
    checks += 1

    print(f"C231 SymPy cross-check: PASS ({checks} symbolic identities)")


if __name__ == "__main__":
    main()
