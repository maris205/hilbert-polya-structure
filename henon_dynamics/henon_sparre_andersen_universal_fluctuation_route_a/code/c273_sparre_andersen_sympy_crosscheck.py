#!/usr/bin/env python3
"""Independent symbolic generating-function checks for HCS-C273."""
from __future__ import annotations

import math

import sympy as sp


def main() -> None:
    z, u = sp.symbols("z u")
    checks = 0
    q = lambda n: sp.Rational(math.comb(2 * n, n), 4**n)

    q_series = sp.series((1 - z) ** sp.Rational(-1, 2), z, 0, 42).removeO()
    for n in range(41):
        assert sp.expand(q_series).coeff(z, n) == q(n)
        checks += 1

    square = sp.series(q_series**2, z, 0, 41).removeO()
    for n in range(41):
        assert sp.expand(square).coeff(z, n) == 1
        checks += 1

    first_gf = 1 - sp.sqrt(1 - z)
    first_series = sp.series(first_gf, z, 0, 42).removeO()
    for n in range(1, 41):
        expected = q(n - 1) - q(n)
        assert sp.expand(first_series).coeff(z, n) == expected
        assert sp.simplify(expected - q(n - 1) / (2 * n)) == 0
        checks += 2

    bivariate = sp.series(
        (1 - z) ** sp.Rational(-1, 2) * (1 - u * z) ** sp.Rational(-1, 2),
        z,
        0,
        19,
    ).removeO()
    for n in range(19):
        coefficient = sp.expand(bivariate).coeff(z, n)
        for k in range(n + 1):
            assert coefficient.coeff(u, k) == q(k) * q(n - k)
            checks += 1
        assert sp.simplify(coefficient.subs(u, 1) - 1) == 0
        checks += 1

    for n in range(1, 41):
        assert sp.simplify(q(n) / q(n - 1) - sp.Rational(2 * n - 1, 2 * n)) == 0
        checks += 1

    print(f"C273_SYMPY_PASS ({checks} symbolic checks)")


if __name__ == "__main__":
    main()
