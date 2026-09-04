#!/usr/bin/env python3
"""Independent symbolic resolvent and generating-function checks for HCS-C355."""
from __future__ import annotations

import math
import sys

import sympy as sp


def need(condition, label):
    if condition is not True and condition != sp.S.true:
        raise AssertionError(label)


def dyck_by_excursions(n, k):
    return sp.Rational(k, 2 * n - k) * sp.binomial(2 * n - k, n)


def main():
    if sys.flags.optimize:
        raise RuntimeError("C355 SymPy lane refuses optimized Python")
    z, w, D = sp.symbols("z w D", positive=True)
    checks = 0
    rho2 = 4 * (D - 1) / D ** 2
    square = sp.sqrt(z ** 2 - rho2)
    cavity = D ** 2 * (z - square) / (2 * (D - 1))
    green = (D * square - (D - 2) * z) / (2 * (z ** 2 - 1))
    need(sp.simplify((D - 1) * cavity ** 2 / D ** 2 - z * cavity + 1) == 0,
         "cavity quadratic")
    checks += 1
    need(sp.simplify(green - 1 / (z - cavity / D)) == 0, "root Schur complement")
    checks += 1
    need(sp.limit(z * green, z, sp.oo) == 1, "resolvent normalization")
    checks += 1
    need(sp.simplify(green.subs(D, 2) - 1 / sp.sqrt(z ** 2 - 1)) == 0,
         "rank-one arcsine resolvent")
    checks += 1

    # Coefficients from the resolvent agree with the weighted-Dyck formula.
    for degree in (4, 6, 8, 10):
        expression = sp.simplify((green.subs({D: degree, z: 1 / w})) / w)
        series = sp.series(expression, w, 0, 25).removeO().expand()
        for n in range(13):
            count = 1 if n == 0 else sum(
                dyck_by_excursions(n, k) * degree ** k * (degree - 1) ** (n - k)
                for k in range(1, n + 1))
            expected = sp.Rational(count, degree ** (2 * n))
            need(sp.expand(series).coeff(w, 2 * n) == expected,
                 f"resolvent moment D={degree} n={n}")
            need(sp.expand(series).coeff(w, 2 * n + 1) == 0,
                 f"odd moment D={degree} n={n}")
            checks += 2

    # First-return Catalan series and renewal identity U=1/(1-F).
    t = sp.symbols("t")
    for degree in (4, 6, 8, 10):
        p = sp.Rational(degree - 1, degree)
        q = sp.Rational(1, degree)
        catalan_series = (1 - sp.sqrt(1 - 4 * p * q * t)) / (2 * p)
        first = sp.series(catalan_series, t, 0, 14).removeO()
        renewal = sp.series(1 / (1 - catalan_series), t, 0, 14).removeO().expand()
        for n in range(1, 14):
            expected_first = sp.Rational(math.comb(2 * n - 2, n - 1), n) * p ** (n - 1) * q ** n
            need(sp.expand(first).coeff(t, n) == expected_first,
                 f"first return D={degree} n={n}")
            count = sum(dyck_by_excursions(n, k) * degree ** k *
                        (degree - 1) ** (n - k) for k in range(1, n + 1))
            need(renewal.coeff(t, n) == sp.Rational(count, degree ** (2 * n)),
                 f"renewal coefficient D={degree} n={n}")
            checks += 2
        need(sp.simplify(catalan_series.subs(t, 1) - sp.Rational(1, degree - 1)) == 0,
             f"eventual return D={degree}")
        checks += 1

    # Drift and variance of the coupled iid increments.
    p, q = sp.symbols("p q", positive=True)
    mean = p - q
    variance = sp.expand(p * (1 - mean) ** 2 + q * (-1 - mean) ** 2)
    need(sp.simplify(variance.subs(q, 1 - p) - 4 * p * (1 - p)) == 0,
         "increment variance")
    checks += 1
    for degree in range(3, 13):
        pd = sp.Rational(degree - 1, degree)
        qd = sp.Rational(1, degree)
        need(pd - qd == sp.Rational(degree - 2, degree), f"speed D={degree}")
        need(4 * pd * qd == sp.Rational(4 * (degree - 1), degree ** 2),
             f"variance D={degree}")
        checks += 2
    print(f"C355 SymPy cross-check: PASS {checks} exact symbolic checks")


if __name__ == "__main__":
    main()
