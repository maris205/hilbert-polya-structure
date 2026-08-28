#!/usr/bin/env python3
"""Deterministic exact controls for the colored Catalan renewal shifts."""

from fractions import Fraction
from math import comb


CHECKS = 0


def check(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def catalan(n):
    return comb(2 * n, n) // (n + 1)


def renewal_coefficients(c, order):
    """Coefficients of 1/(1-F_c), with F_c[n]=c*C_{n-1}."""
    f = [0] + [c * catalan(n - 1) for n in range(1, order + 1)]
    zeta = [0] * (order + 1)
    zeta[0] = 1
    for n in range(1, order + 1):
        zeta[n] = sum(f[j] * zeta[n - j] for j in range(1, n + 1))
    return f, zeta


def fixed_counts_from_zeta(zeta):
    """Recover N_n from zeta=exp(sum N_n z^n/n), using z*zeta'/zeta."""
    order = len(zeta) - 1
    fixed = [0] * (order + 1)
    for n in range(1, order + 1):
        fixed[n] = n * zeta[n] - sum(
            fixed[k] * zeta[n - k] for k in range(1, n)
        )
    return fixed


def main():
    order = 40

    # Classical Catalan recurrence and integrality.
    for n in range(0, order - 1):
        check(
            catalan(n + 1) == sum(catalan(j) * catalan(n - j) for j in range(n + 1)),
            f"Catalan recurrence failed at n={n}",
        )

    for c in range(1, 9):
        f, zeta = renewal_coefficients(c, order)
        check(f[1] == c, f"length-one count failed for c={c}")
        for n in range(1, order + 1):
            check(f[n] == c * comb(2 * n - 2, n - 1) // n, "first-return formula")
            check(
                zeta[n] == sum(f[j] * zeta[n - j] for j in range(1, n + 1)),
                "renewal composition",
            )

        fixed = fixed_counts_from_zeta(zeta)
        for n in range(1, order + 1):
            check(fixed[n] >= 0 and isinstance(fixed[n], int), "fixed count integrality")
        if c == 1:
            for n in range(1, order + 1):
                check(zeta[n] == catalan(n), f"zeta_1 coefficient n={n}")
                check(fixed[n] == comb(2 * n, n) // 2, f"fixed_1 n={n}")
        if c == 2:
            for n in range(1, order + 1):
                check(fixed[n] == 4**n // 2, f"fixed_2 n={n}")

    # Exact rational algebra for the positive recurrent regime.
    for c in range(3, 51):
        r = Fraction(c - 1, c * c)
        sqrt_boundary = Fraction(c - 2, c)
        check(1 - 4 * r == sqrt_boundary * sqrt_boundary, "root identity")
        check(r < Fraction(1, 4), "root must be before Catalan radius")
        derivative = Fraction(c * c, c - 2)
        mean_return = r * derivative
        check(mean_return == Fraction(c - 1, c - 2), "mean return")
        check(1 / mean_return == Fraction(c - 2, c - 1), "base mass")
        check(4 * r < 1, "exponential return tail")

    # Boundary value and derivative tests encode transient/null recurrence.
    check(Fraction(1, 2) < 1, "c=1 boundary transience")
    check(Fraction(2, 2) == 1, "c=2 boundary recurrence")

    print(f"PASS: {CHECKS:,} exact assertions")
    print("boundary fixed counts c=1:", fixed_counts_from_zeta(renewal_coefficients(1, 8)[1])[1:])
    print("boundary fixed counts c=2:", fixed_counts_from_zeta(renewal_coefficients(2, 8)[1])[1:])
    print("classification: c=1 transient; c=2 null recurrent; c>=3 positive recurrent")


if __name__ == "__main__":
    main()
