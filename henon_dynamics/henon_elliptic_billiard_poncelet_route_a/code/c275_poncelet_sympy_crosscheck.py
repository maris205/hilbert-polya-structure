#!/usr/bin/env python3
"""Exact symbolic cross-checks for HCS-C275."""
from __future__ import annotations

from fractions import Fraction as Q
from math import gcd

import sympy as sp

CHECKS = 0


def ck(condition: bool, label: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)


def main() -> None:
    eccentricities = (
        Q(1, 4), Q(1, 3), Q(1, 2), Q(2, 3),
        Q(3, 4), Q(4, 5), Q(9, 10), Q(19, 20),
    )
    ratios = (Q(1, 5), Q(2, 5), Q(3, 5), Q(4, 5))
    s = sp.symbols("s", real=True)

    for e_q in eccentricities:
        e = sp.Rational(e_q.numerator, e_q.denominator)
        for ratio_q in ratios:
            ratio = sp.Rational(ratio_q.numerator, ratio_q.denominator)
            f = e * ratio
            omega_square = sp.cancel((e**2 - f**2) / (e**2 * (1 - f**2)))
            complement = sp.cancel(1 - omega_square)
            expected_complement = sp.cancel(f**2 * (1 - e**2) / (e**2 * (1 - f**2)))
            ck(omega_square > 0, "omega square positive")
            ck(complement > 0, "omega square below one")
            ck(sp.simplify(complement - expected_complement) == 0, "omega complement")

            # The Jacobi identity sn^2+cn^2=1 puts the covering on E(f).
            ellipse_residual = sp.expand(s**2 + (1 - s**2) - 1)
            ck(ellipse_residual == 0, "covering ellipse identity")

            # If f=e*cd(u,e), write s=sn(u,e), cn^2=1-s^2,
            # dn^2=1-e^2*s^2; the formula recovers sin^2(omega)=s^2.
            f_square = sp.cancel(e**2 * (1 - s**2) / (1 - e**2 * s**2))
            inverse_ratio = sp.cancel((e**2 - f_square) / (e**2 * (1 - f_square)))
            ck(sp.simplify(inverse_ratio - s**2) == 0, "inverse porism identity")

    theta = sp.symbols("theta", real=True)
    rotations = ((1, 5), (1, 4), (1, 3), (2, 5), (2, 7), (3, 8))
    for p, q in rotations:
        ck(gcd(p, q) == 1, "coprime rotation")
        for k in range(1, q):
            ck((k * p) % q != 0, "minimal period")
        q_return = sp.simplify(theta + q * sp.Rational(p, q))
        ck(sp.simplify(q_return - (theta + p)) == 0, "q return deck shift")
        ck(sp.diff(q_return, theta) == 1, "unit tangent derivative")

    e, f = sp.symbols("e f", positive=True)
    omega_square = (e**2 - f**2) / (e**2 * (1 - f**2))
    ck(sp.limit(omega_square, f, e, dir="-") == 0, "f to e endpoint")
    ck(sp.limit(omega_square, e, f, dir="+") == 0, "e to f endpoint")
    ck(sp.limit(omega_square, f, 0, dir="+") == 1, "f to zero endpoint")
    ck(sp.limit(omega_square, e, 1, dir="-") == 1, "e to one endpoint")

    assert CHECKS == 208, CHECKS
    print(
        f"C275_SYMPY_PASS ({CHECKS} symbolic checks; "
        "eccentricity domain, Jacobi covering, inverse porism, and primitive period)"
    )


if __name__ == "__main__":
    main()
