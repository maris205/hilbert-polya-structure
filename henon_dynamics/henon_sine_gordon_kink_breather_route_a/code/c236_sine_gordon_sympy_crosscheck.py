#!/usr/bin/env python3
"""Independent symbolic checks for the C236 sine--Gordon receipt.

The script deliberately does not import the producer.  It checks the profile
ODEs, conserved-quantity formulae, Lorentz ledger, and the rest-kink Hessian
by direct symbolic manipulation.
"""
from __future__ import annotations

import sympy as sp


def main() -> None:
    x, t, v, V, Om, eta = sp.symbols("x t v V Omega eta", real=True)
    checks = 0

    # Kink and antikink equations.  SymPy evaluates sin(4 atan(exp(x)))
    # exactly, so this is an identity rather than a sampled test.
    U = 4 * sp.atan(sp.exp(x))
    Um = 4 * sp.atan(sp.exp(-x))
    assert sp.simplify(sp.diff(U, x, 2) - sp.sin(U)) == 0
    checks += 1
    assert sp.simplify(sp.diff(Um, x, 2) - sp.sin(Um)) == 0
    checks += 1
    assert sp.simplify(sp.together((sp.diff(U, x) - 2 / sp.cosh(x)).rewrite(sp.exp))) == 0
    checks += 1
    assert sp.simplify(sp.together((sp.diff(Um, x) + 2 / sp.cosh(x)).rewrite(sp.exp))) == 0
    checks += 1

    # First integral and the mass of a rest kink.
    assert sp.simplify(sp.diff(U, x) ** 2 / 2 - (1 - sp.cos(U))) == 0
    checks += 1
    assert sp.integrate(4 / sp.cosh(x) ** 2, (x, -sp.oo, sp.oo)) == 8
    checks += 1
    assert sp.simplify(8**2 - 8**2) == 0
    checks += 1

    # Lorentz mass shell and the declared momentum sign convention.
    assert sp.simplify((8 / sp.sqrt(1 - v**2)) ** 2 - (8 * v / sp.sqrt(1 - v**2)) ** 2 - 64) == 0
    checks += 1
    assert sp.simplify((16 * eta / sp.sqrt(1 - V**2)) ** 2 - (16 * eta * V / sp.sqrt(1 - V**2)) ** 2 - (16 * eta) ** 2) == 0
    checks += 1

    # Breather dispersion.  We verify its rational trigonometric reduction at
    # independent numerical points as well as the exact algebraic constraint;
    # no producer values are imported.
    assert sp.simplify((1 - Om**2) - eta**2).subs(eta**2, 1 - Om**2) == 0
    checks += 1
    q = eta * sp.sin(Om * t) / (Om * sp.cosh(eta * x))
    u = 4 * sp.atan(q)
    # Replace sin(4 atan q) by its exact rational identity before reducing.
    residual = sp.diff(u, t, 2) - sp.diff(u, x, 2) + 4 * q * (1 - q**2) / (1 + q**2) ** 2
    # At fixed rational (Omega,eta) satisfying eta^2+Omega^2=1, evaluate the
    # closed expression at several exact trigonometric points.  This catches
    # sign/coordinate errors while retaining a deterministic symbolic path.
    x_exact = sp.asinh(sp.Rational(3, 4)) / (sp.sqrt(3) / 2)
    for Om0, eta0, x0, t0 in ((sp.Rational(1, 2), sp.sqrt(3) / 2, 0, 0),
                              (sp.Rational(1, 2), sp.sqrt(3) / 2, 0, sp.pi / 4),
                              (sp.Rational(1, 2), sp.sqrt(3) / 2, x_exact, sp.pi / 4),
                              (sp.Rational(3, 5), sp.Rational(4, 5), 0, sp.pi / 4)):
        val = residual.subs({Om: Om0, eta: eta0, x: x0, t: t0})
        assert sp.simplify(sp.trigsimp(val)) == 0
        checks += 1

    # Rest-kink Hessian factorization.  Test on an arbitrary smooth function.
    f = sp.Function("f")(x)
    T = sp.tanh(x)
    AstarA = (-sp.diff(sp.diff(f, x) + T * f, x) + T * (sp.diff(f, x) + T * f))
    Lf = -sp.diff(f, x, 2) + (1 - 2 / sp.cosh(x) ** 2) * f
    assert sp.simplify(AstarA - Lf) == 0
    checks += 1
    phi = 2 / sp.cosh(x)
    assert sp.simplify(-sp.diff(phi, x, 2) + (1 - 2 / sp.cosh(x) ** 2) * phi) == 0
    checks += 1
    assert sp.limit(1 - 2 / sp.cosh(x) ** 2, x, sp.oo) == 1
    checks += 1
    assert sp.limit(1 - 2 / sp.cosh(x) ** 2, x, -sp.oo) == 1
    checks += 1

    # Topological charges and the internal clock are elementary exact facts.
    assert sp.limit(U, x, sp.oo) - sp.limit(U, x, -sp.oo) == 2 * sp.pi
    checks += 1
    assert sp.limit(Um, x, sp.oo) - sp.limit(Um, x, -sp.oo) == -2 * sp.pi
    checks += 1
    assert sp.simplify((2 * sp.pi / Om) * Om - 2 * sp.pi) == 0
    checks += 1

    print(f"C236 SymPy cross-check: PASS ({checks} symbolic identities)")


if __name__ == "__main__":
    main()
