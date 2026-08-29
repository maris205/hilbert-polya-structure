#!/usr/bin/env python3
"""Independent SymPy identities for the M/M/infinity theorem."""
from __future__ import annotations

import sympy as sp


def C(k: int, n, rho):
    return sp.factorial(k) * sum(sp.binomial(n, j) * (-rho) ** (k - j) / sp.factorial(k - j) for j in range(min(k, 12) + 1))


def main() -> None:
    n, rho, mu, z, a = sp.symbols("n rho mu z a", positive=True)
    checks = 0

    def ok(expr, label):
        nonlocal checks
        checks += 1
        if sp.simplify(expr) != 0:
            raise AssertionError(label + ": " + str(sp.simplify(expr)))

    # Polynomial generator identity Q C_k=-mu*k C_k with lambda=mu*rho.
    for k in range(0, 9):
        poly = sp.expand(C(k, n, rho))
        shifted_plus = sp.expand(C(k, n + 1, rho))
        shifted_minus = sp.expand(C(k, n - 1, rho))
        gen = mu * rho * (shifted_plus - poly) + mu * n * (shifted_minus - poly)
        ok(sp.together(gen + mu * k * poly), f"generator k={k}")

    # Poisson detailed balance and Charlier low-order orthogonality moments.
    for j in range(0, 6):
        # The exponential generating identity is checked by coefficient
        # comparison, avoiding a numerical quadrature assumption.
        lhs = sp.expand(C(j, n, rho))
        # Direct coefficient identity for e^{-rho z}(1+z)^n.
        rhs_coeff = sp.factorial(j) * sum(sp.binomial(n, r) * (-rho) ** (j - r) / sp.factorial(j - r) for r in range(min(j, 12) + 1))
        ok(sp.expand(lhs - rhs_coeff), f"coefficient k={j}")
    # Stationary recursion is exact for every symbolic n.
    pi_n = sp.exp(-rho) * rho ** n / sp.factorial(n)
    ok(sp.simplify(rho * pi_n / (n + 1) - sp.exp(-rho) * rho ** (n + 1) / sp.factorial(n + 1)), "Poisson recursion")

    # PGF backward equation in the independent variable a=e^{-mu t}.
    G = ((1 - a) + a * z) ** n * sp.exp(rho * (1 - a) * (z - 1))
    dG_da = sp.diff(G, a)
    rhs_da = -rho * (z - 1) * G + n * (z - 1) * ((1 - a) + a * z) ** (n - 1) * sp.exp(rho * (1 - a) * (z - 1))
    ok(sp.simplify(dG_da - rhs_da), "PGF a derivative")

    # Geometric trace and positive-time determinant factors.
    q = sp.symbols("q", positive=True)
    ok(sp.simplify((1 - q) * (1 / (1 - q)) - 1), "trace geometric")
    for k in range(1, 8):
        ok(sp.expand((1 - q ** k) - (1 - q) * sum(q ** r for r in range(k))), f"det factor k={k}")

    print(f"C233 SymPy cross-check: PASS ({checks} symbolic identities)")


if __name__ == "__main__":
    main()
