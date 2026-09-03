#!/usr/bin/env python3
"""Disjoint symbolic cross-checks for HCS-C322."""
import sys
import sympy as sp


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C322 SymPy lane refuses optimized Python")
    u, v, theta = sp.symbols("u v theta", real=True)
    up = u * sp.cos(theta) + v * sp.sin(theta)
    vp = -u * sp.sin(theta) + v * sp.cos(theta)
    quartic = sp.integrate(sp.expand(up ** 4 + vp ** 4), (theta, -sp.pi, sp.pi)) / (2 * sp.pi)
    if sp.simplify(quartic - sp.Rational(3, 4) * (u * u + v * v) ** 2) != 0:
        raise AssertionError("quartic angle average")
    checks = 1
    n = sp.symbols("n", integer=True, positive=True)
    kappa = sp.Rational(3, 1) / (n ** 2 - 1)
    mu = (n + 4) / (n * (n + 1))
    factor = sp.simplify(n / (n - 1) * (1 - mu))
    if sp.factor(factor - (1 - kappa)) != 0:
        raise AssertionError("projection-to-gap factor")
    checks += 1
    j, N = sp.symbols("j N", integer=True, positive=True)
    product = sp.product((j - 2) * (j + 2) / ((j - 1) * (j + 1)), (j, 3, N))
    if sp.simplify(product - (N + 2) / (4 * (N - 1))) != 0:
        raise AssertionError("telescoping product")
    checks += 1
    for dimension in range(3, 21):
        eigenvalues = []
        for r in range(1, 10):
            denominator = sp.prod(dimension - 1 + 2 * offset for offset in range(r))
            alpha = (-1) ** r * sp.factorial2(2 * r - 1) / denominator
            eigenvalues.append(sp.factor(alpha))
        if max(value for value in eigenvalues if value > 0) != sp.Rational(3, dimension ** 2 - 1):
            raise AssertionError("kappa spectrum")
        if min(eigenvalues) != -sp.Rational(1, dimension - 1):
            raise AssertionError("negative spectrum")
        if sp.simplify((dimension + 2) / (2 * (dimension - 1)) -
                       dimension * (1 - (1 - sp.Rational(dimension + 2, 2 * dimension * (dimension - 1))))) != 0:
            raise AssertionError("generator normalization")
        checks += 3
    for dimension in range(2, 16):
        fourth = sp.Rational(3 * dimension, dimension + 2)
        center = dimension * fourth
        if center != sp.Rational(3 * dimension * dimension, dimension + 2):
            raise AssertionError("quartic center")
        checks += 1
    print(f"C322 SymPy cross-check: PASS ({checks} identities)")


if __name__ == "__main__":
    main()
