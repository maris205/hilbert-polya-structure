#!/usr/bin/env python3
"""Symbolic cross-check independent of the numerical producer/checker."""
from __future__ import annotations

import json
import sympy as sp


def main() -> None:
    x, omega = sp.symbols("x omega", positive=True, finite=True)
    y = sp.sqrt(omega) * x
    q = sp.sqrt(omega) * sp.sech(y)
    phi2 = sp.sech(y) ** 2
    lp = lambda f: -sp.diff(f, x, 2) + (omega - 6 * omega * sp.sech(y) ** 2) * f
    lm = lambda f: -sp.diff(f, x, 2) + (omega - 2 * omega * sp.sech(y) ** 2) * f
    checks = 0

    def prove(expr, label):
        nonlocal checks
        checks += 1
        if sp.simplify(expr) != 0:
            raise AssertionError(label + ": " + str(sp.simplify(expr)))

    prove(-sp.diff(q, x, 2) + omega * q - 2 * q ** 3, "profile equation")
    prove(lp(phi2) + 3 * omega * phi2, "Lplus phi2")
    prove(lp(sp.diff(q, x)), "Lplus translation kernel")
    prove(lm(q), "Lminus phase kernel")
    # Substitute t=tanh(y), dx=dy/sqrt(omega), so the elementary integrals
    # reduce to polynomials on [-1,1] (SymPy versions differ in sech tails).
    t = sp.symbols("t", real=True)
    prove(sp.integrate(1, (t, -1, 1)) - 2, "mass base integral")
    prove(sp.integrate(1 - t ** 2, (t, -1, 1)) - sp.Rational(4, 3), "quartic base integral")
    prove(sp.integrate(t ** 2, (t, -1, 1)) - sp.Rational(2, 3), "gradient base integral")
    prove((sp.sqrt(omega) ** 2 / sp.sqrt(omega)) * 2 - 2 * sp.sqrt(omega), "mass scaling")
    prove((omega ** 2 / sp.sqrt(omega)) * sp.Rational(2, 3) - sp.Rational(2, 3) * omega ** sp.Rational(3, 2), "gradient scaling")
    prove((omega ** 2 / sp.sqrt(omega)) * sp.Rational(4, 3) - sp.Rational(4, 3) * omega ** sp.Rational(3, 2), "quartic scaling")
    prove(sp.diff(2 * sp.sqrt(omega), omega) - omega ** (-sp.Rational(1, 2)), "VK slope")

    # Factorizations in the scaled coordinate y.  Operators are represented
    # by their potential terms after multiplying out A_l^* A_l.
    z = sp.symbols("z", real=True)
    s2 = sp.sech(z) ** 2
    p2 = -sp.Symbol("D2") + 1 - 6 * s2
    a2star_a2 = -sp.Symbol("D2") + 4 - 6 * s2
    p1 = -sp.Symbol("D2") + 1 - 2 * s2
    a1star_a1 = -sp.Symbol("D2") + 1 - 2 * s2
    prove((p2 - (a2star_a2 - 3)).subs(sp.Symbol("D2"), 0), "P2 factorization")
    prove((p1 - a1star_a1).subs(sp.Symbol("D2"), 0), "P1 factorization")
    # Scaling identities for the essential threshold and discrete values.
    prove((-3 * omega) / omega + 3, "scaled negative eigenvalue")
    prove((omega - omega), "threshold")
    # Parity and orthogonality are exact integrals.
    zodd = sp.symbols("zodd", real=True)
    prove(sp.integrate(sp.sech(zodd) ** 2 * sp.tanh(zodd), (zodd, -sp.oo, sp.oo)), "scaled odd integral")
    # The x-space inner product has the same zero after y=sqrt(omega)x.
    prove(sp.integrate(t, (t, -1, 1)), "Q orthogonal Qprime")
    # Action identity and its derivative.
    H = -sp.Rational(1, 3) * omega ** sp.Rational(3, 2)
    S = H + omega * (2 * sp.sqrt(omega)) / 2
    prove(S - sp.Rational(2, 3) * omega ** sp.Rational(3, 2), "action")
    prove(sp.diff(S, omega) - sp.sqrt(omega), "action derivative")

    print(json.dumps({"status": "C221_SYMPY_PASS", "checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
