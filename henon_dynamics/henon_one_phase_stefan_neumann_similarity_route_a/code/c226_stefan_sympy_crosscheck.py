#!/usr/bin/env python3
"""Independent symbolic identities for the C226 Stefan theorem."""
from __future__ import annotations

import sympy as s


def main() -> None:
    x, t, lam, beta, ste, eta = s.symbols("x t lam beta ste eta", positive=True)
    pi = s.pi
    u = 1 - s.erf(x / (2 * s.sqrt(t))) / s.erf(lam)
    checks = []

    def add(expr, label):
        checks.append((s.simplify(expr), label))

    add(s.diff(u, t) - s.diff(u, x, 2), "heat PDE")
    add(u.subs(x, 0) - 1, "wall value")
    add(u.subs(x, 2 * lam * s.sqrt(t)), "interface value")
    ux_s = s.diff(u, x).subs(x, 2 * lam * s.sqrt(t))
    add(s.simplify(ux_s + s.exp(-lam**2) / (s.sqrt(pi * t) * s.erf(lam))), "interface derivative")
    ste_expr = s.sqrt(pi) * lam * s.exp(lam**2) * s.erf(lam)
    # beta*lambda equals the interface flux coefficient after cancelling
    # the common t^{-1/2} factor.
    add(s.simplify((beta * lam - s.exp(-lam**2) / (s.sqrt(pi) * s.erf(lam))).subs(beta, 1 / ste_expr)), "Stefan balance")
    F = s.sqrt(pi) * lam * s.exp(lam**2) * s.erf(lam)
    add(s.simplify(s.diff(F, lam) - (s.sqrt(pi) * s.exp(lam**2) * s.erf(lam) * (1 + 2 * lam**2) + 2 * lam)), "root derivative")

    # Five-term small-Stefan series and its formal reversion.
    z = s.symbols("z")
    Fseries = s.series(s.sqrt(pi) * s.sqrt(z) * s.exp(z) * s.erf(s.sqrt(z)), z, 0, 7).removeO()
    expected_F = 2*z + s.Rational(4, 3)*z**2 + s.Rational(8, 15)*z**3 + s.Rational(16, 105)*z**4 + s.Rational(32, 945)*z**5 + s.Rational(64, 10395)*z**6
    add(s.expand(Fseries - expected_F), "F series")
    y = s.symbols("y")
    coeffs = s.symbols("a1:7")
    zseries = sum(coeffs[i-1] * y**i for i in range(1, 7))
    reverted = s.series(Fseries.subs(z, zseries), y, 0, 7).removeO() - y
    sol = {}
    for order, coeff in enumerate(coeffs, start=1):
        equation = s.expand(reverted.subs(sol)).coeff(y, order)
        sol[coeff] = s.solve(equation, coeff)[0]
    expected_inv = y/s.Integer(2) - y**2/s.Integer(6) + s.Rational(7,90)*y**3 - s.Rational(79,1890)*y**4 + s.Rational(689,28350)*y**5 + s.Rational(-103,6930)*y**6
    add(s.expand(zseries.subs(sol) - expected_inv), "inverse series")
    lambda_factor = 1 - y/s.Integer(6) + s.Rational(23,360)*y**2 - s.Rational(157,5040)*y**3
    add(s.series(y * lambda_factor**2 / 2 - expected_inv, y, 0, 5).removeO(), "lambda series factor")

    # Integrate the similarity profile and verify the exact energy partition.
    integral_erf = lam * s.erf(lam) + (s.exp(-lam**2) - 1) / s.sqrt(pi)
    sensible = s.simplify(2 * s.sqrt(t) * (lam - integral_erf / s.erf(lam)))
    expected_sensible = 2 * s.sqrt(t) * (1 - s.exp(-lam**2)) / (s.sqrt(pi) * s.erf(lam))
    add(s.simplify(sensible - expected_sensible), "sensible energy")
    latent = s.simplify(2 * (1 / ste_expr) * lam * s.sqrt(t))
    input_energy = 2 * s.sqrt(t) / (s.sqrt(pi) * s.erf(lam))
    add(s.simplify(input_energy - sensible - latent), "energy ledger")
    add(s.simplify((s.exp(-lam**2) / (s.sqrt(pi) * s.erf(lam))) / (1 / (s.sqrt(pi) * s.erf(lam))) - s.exp(-lam**2)), "flux ratio")

    failures = [(label, expr) for expr, label in checks if s.simplify(expr) != 0]
    if failures:
        raise AssertionError(failures)
    print(f"C226 SymPy symbolic identities: PASS ({len(checks)} symbolic identities)")


if __name__ == "__main__":
    main()
