#!/usr/bin/env python3
"""Small, independent symbolic witnesses for the HCS-C317 identities."""
from __future__ import annotations

import sys
import sympy as sp


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C317 SymPy cross-check refuses optimized Python")
    checks = 0
    a, b, c, d, e = sp.symbols("a b c d e")
    A = sp.Matrix([[2, 0], [0, 3]])
    X = sp.Matrix([[a, b], [c, d]])
    R = sp.eye(2) - A * X
    X1 = sp.expand(X * (2 * sp.eye(2) - A * X))
    if sp.simplify(sp.eye(2) - A * X1 - R**2) != sp.zeros(2):
        raise AssertionError("residual squaring")
    checks += 4

    lam = sp.symbols("lambda", nonzero=True)
    for size in range(1, 7):
        N = sp.zeros(size)
        for i in range(size - 1):
            N[i, i + 1] = 1
        J = lam * sp.eye(size) + N
        for power in (1, 2, 4, 8, 16):
            rhs = sum((sp.binomial(power, j) * lam ** (power - j) * N**j
                       for j in range(min(size - 1, power) + 1)), sp.zeros(size))
            if sp.simplify(J**power - rhs) != sp.zeros(size):
                raise AssertionError("Jordan binomial law")
            checks += size * size

    # Rectangular SVD-coordinate block recurrence, including every off-support block.
    sigma = sp.symbols("sigma", nonzero=True)
    Ar = sp.Matrix([[sigma, 0], [0, 0]])
    Xr = sp.Matrix([[a, b], [c, e]])
    got = sp.expand(Xr * (2 * sp.eye(2) - Ar * Xr))
    expected = sp.Matrix([[a * (2 - sigma * a), (2 - sigma * a) * b],
                          [c * (2 - sigma * a), 2 * e - sigma * c * b]])
    if sp.simplify(got - expected) != sp.zeros(2):
        raise AssertionError("SVD block recurrence")
    checks += 4

    # Canonical alpha start: every singular direction has residual 1-alpha*sigma^2
    # and coefficient (1-r^(2^k))/sigma.
    alpha = sp.symbols("alpha")
    for sval in (sp.Rational(1, 2), 1, 2, 3):
        residual = 1 - alpha * sval**2
        coefficient = alpha * sval
        for k in range(5):
            target = (1 - residual ** (2**k)) / sval
            if sp.simplify(coefficient - target) != 0:
                raise AssertionError("canonical alpha coefficient")
            coefficient = sp.expand(coefficient * (2 - sval * coefficient))
            checks += 1

    print(f"C317 SymPy cross-check: PASS ({checks} identities)")


if __name__ == "__main__":
    main()
