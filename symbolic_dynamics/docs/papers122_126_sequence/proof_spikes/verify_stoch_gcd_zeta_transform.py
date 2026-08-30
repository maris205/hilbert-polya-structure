#!/usr/bin/env python3
"""Exact coefficient checks for the all-integer gcd Dirichlet transform."""

from fractions import Fraction
from functools import lru_cache
from math import gcd, isqrt


ASSERTIONS = 0


def check(statement, context):
    global ASSERTIONS
    ASSERTIONS += 1
    if not statement:
        raise AssertionError(context)


def divisors(n):
    answer = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            answer.append(d)
            if d * d != n:
                answer.append(n // d)
    return sorted(answer)


def phi(n):
    value = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            value -= value // p
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        value -= value // n
    return value


def add_polynomial(target, source, scale=Fraction(1), shift=0):
    if len(target) < len(source) + shift:
        target.extend([Fraction(0)] * (len(source) + shift - len(target)))
    for degree, coefficient in enumerate(source):
        target[degree + shift] += scale * coefficient


@lru_cache(None)
def pgf(n):
    if n == 1:
        return (Fraction(1),)
    result = []
    for d in divisors(n):
        if d < n:
            add_polynomial(result, pgf(d), Fraction(phi(n // d), n - 1), 1)
    return tuple(result)


def scale(poly, scalar):
    return tuple(scalar * coefficient for coefficient in poly)


def add(*polys):
    result = []
    for poly in polys:
        add_polynomial(result, poly)
    while result and result[-1] == 0:
        result.pop()
    return tuple(result)


def main():
    maximum = 600
    for n in range(1, maximum + 1):
        left = scale(pgf(n), n)
        # Build the (1-z)G term without an opaque polynomial multiplication.
        rhs = []
        add_polynomial(rhs, pgf(n))
        add_polynomial(rhs, pgf(n), Fraction(-1), 1)
        for d in divisors(n):
            add_polynomial(rhs, pgf(d), Fraction(phi(n // d)), 1)
        while rhs and rhs[-1] == 0:
            rhs.pop()
        check(left == tuple(rhs), (n, left, tuple(rhs)))

        # Literal-residue first-step reconstruction remains independent of
        # the divisor convolution used above.
        if n > 1:
            literal = []
            for residue in range(1, n):
                add_polynomial(literal, pgf(gcd(n, residue)), Fraction(1, n - 1), 1)
            check(tuple(literal) == pgf(n), (n, "literal"))

    print("proper-residue gcd zeta-transform verifier: PASS")
    print(f"assertions={ASSERTIONS}")
    print(f"bivariate coefficient equation: 1 <= n <= {maximum}")
    print("exact arithmetic: Fraction only")


if __name__ == "__main__":
    main()
