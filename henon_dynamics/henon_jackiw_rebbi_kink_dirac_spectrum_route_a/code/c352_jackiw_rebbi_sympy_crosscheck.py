#!/usr/bin/env python3
"""Independent symbolic operator lane for HCS-C352."""
from __future__ import annotations

import sys

import sympy as sp


def need(condition, label):
    if condition is not True and condition != sp.S.true:
        raise AssertionError(label)


def main():
    if sys.flags.optimize:
        raise RuntimeError("C352 SymPy lane refuses optimized Python")
    x, k = sp.symbols("x k", real=True)
    f = sp.Function("f")(x)
    checks = 0

    def a(m, g):
        return sp.diff(g, x) + m * sp.tanh(x) * g

    def astar(m, g):
        return -sp.diff(g, x) + m * sp.tanh(x) * g

    def upper(m, g):
        return -sp.diff(g, x, 2) + (m * m - m * (m + 1) * sp.sech(x) ** 2) * g

    def lower(m, g):
        return -sp.diff(g, x, 2) + (m * m - m * (m - 1) * sp.sech(x) ** 2) * g

    for n in range(1, 13):
        need(sp.simplify(sp.trigsimp(astar(n, a(n, f)) - upper(n, f))) == 0,
             f"AstarA factorization {n}")
        need(sp.simplify(sp.trigsimp(a(n, astar(n, f)) - lower(n, f))) == 0,
             f"AAstar factorization {n}")
        need(sp.simplify(sp.trigsimp(lower(n, f) - upper(n - 1, f) - (2 * n - 1) * f)) == 0,
             f"shape invariance {n}")
        need(sp.simplify(a(n, sp.sech(x) ** n)) == 0, f"zero mode {n}")
        checks += 4

    # Work in y=tanh(x).  A state sech(x)^p P(y) is represented by (p,P),
    # so all Darboux and eigenvalue checks reduce to exact polynomial algebra.
    y = sp.symbols("y", real=True)

    def derivative_poly(p, polynomial):
        return sp.expand((1 - y ** 2) * sp.diff(polynomial, y) - p * y * polynomial)

    def astar_poly(m, p, polynomial):
        return sp.expand(-derivative_poly(p, polynomial) + m * y * polynomial)

    def upper_poly(n, p, polynomial):
        return sp.expand(-derivative_poly(p, derivative_poly(p, polynomial))
                         + (n * n - n * (n + 1) * (1 - y ** 2)) * polynomial)

    # Construct every upper-channel bound state through n=12 by Darboux raising.
    for n in range(1, 13):
        for j in range(n):
            p, polynomial = n - j, sp.Integer(1)
            for m in range(p + 1, n + 1):
                polynomial = astar_poly(m, p, polynomial)
            energy2 = j * (2 * n - j)
            need(sp.Poly(upper_poly(n, p, polynomial) - energy2 * polynomial, y).is_zero,
                 f"bound ladder n={n} j={j}")
            checks += 1

    # The Darboux image of a constant is the bounded non-L2 threshold state.
    for n in range(1, 13):
        p, polynomial = 0, sp.Integer(1)
        for m in range(1, n + 1):
            polynomial = astar_poly(m, p, polynomial)
        need(sp.Poly(upper_poly(n, p, polynomial) - n * n * polynomial, y).is_zero,
             f"threshold ladder {n}")
        checks += 1

    # Every elementary scattering multiplier has unit modulus on real momentum.
    for r in range(1, 33):
        factor = (k + sp.I * r) / (k - sp.I * r)
        need(sp.simplify(factor * sp.conjugate(factor)) == 1, f"unit factor {r}")
        checks += 1

    # Chiral symmetry forces nonzero energies into opposite pairs.
    a_symbol, b_symbol = sp.symbols("a_symbol b_symbol")
    h = sp.Matrix([[0, a_symbol], [b_symbol, 0]])
    gamma = sp.diag(1, -1)
    need(gamma * h * gamma == -h, "chiral anticommutation")
    checks += 1
    print(f"C352 SymPy cross-check: PASS {checks} exact symbolic checks")


if __name__ == "__main__":
    main()
