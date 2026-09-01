#!/usr/bin/env python3
"""Independent symbolic checks for HCS-C272."""
from __future__ import annotations

import sympy as sp


def main() -> None:
    checks = 0

    def ok(v: bool) -> None:
        nonlocal checks
        assert v
        checks += 1

    a, gamma, mu, beta, lam = sp.symbols("a gamma mu beta lam", positive=True)
    for k in range(1, 13):
        kernel = beta * gamma**k * a ** (k - 1) * sp.exp(-gamma * a) / sp.factorial(k - 1)
        transform = sp.integrate(kernel * sp.exp(-(lam + mu) * a), (a, 0, sp.oo), conds="none")
        ok(sp.simplify(transform - beta * (gamma / (gamma + lam + mu))**k) == 0)
        z = sp.symbols("z")
        poly = sp.expand((z + gamma + mu)**k - beta * gamma**k)
        ok(sp.Poly(poly, z).degree() == k)
        rho = sp.symbols(f"rho{k}", positive=True)
        ok(sp.simplify(poly.subs({z: gamma * rho - gamma - mu, beta: rho**k})) == 0)
        eig = sp.exp(-(gamma * (rho - 1)) * a)
        ok(sp.simplify(sp.diff(eig, a) + (gamma * (rho - 1)) * eig) == 0)
    print(f"C272_SYMPY_PASS ({checks} symbolic checks; Erlang transform, characteristic roots, stable-age profile)")


if __name__ == "__main__":
    main()
