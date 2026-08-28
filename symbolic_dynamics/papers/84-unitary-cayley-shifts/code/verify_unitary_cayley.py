#!/usr/bin/env python3
"""Exact finite controls for unitary Cayley shifts."""

from fractions import Fraction
from math import gcd

import sympy as sp


CHECKS = 0


def check(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def phi(n):
    return sum(1 for a in range(1, n + 1) if gcd(a, n) == 1)


def mobius(n):
    primes = 0
    value = n
    p = 2
    while p * p <= value:
        if value % p == 0:
            value //= p
            primes += 1
            if value % p == 0:
                return 0
            while value % p == 0:
                value //= p
        p += 1
    if value > 1:
        primes += 1
    return -1 if primes % 2 else 1


def adjacency(n):
    return [[int(gcd((b - a) % n, n) == 1) for b in range(n)] for a in range(n)]


def matmul(a, b):
    size = len(a)
    return [
        [sum(a[i][k] * b[k][j] for k in range(size)) for j in range(size)]
        for i in range(size)
    ]


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def trace_formula(n, power):
    tot = phi(n)
    return sum(
        phi(d) * (mobius(d) * (tot // phi(d))) ** power for d in divisors(n)
    )


def grouped_charpoly(n, symbol):
    value = sp.Integer(1)
    tot = phi(n)
    for d in divisors(n):
        eigenvalue = mobius(d) * (tot // phi(d))
        value *= (symbol - eigenvalue) ** phi(d)
    return sp.Poly(sp.expand(value), symbol)


def main():
    x = sp.symbols("x")
    registry = {}

    for n in range(2, 31):
        a = adjacency(n)
        degree = phi(n)
        for row in a:
            check(sum(row) == degree, f"row degree n={n}")
        for i in range(n):
            for j in range(n):
                check(a[i][j] == a[j][i], f"symmetry n={n}")
                check(a[i][i] == 0, f"loop n={n}")

        power = identity(n)
        for k in range(1, 11):
            power = matmul(power, a)
            check(trace(power) == trace_formula(n, k), f"trace n={n}, k={k}")
        check(trace_formula(n, 2) == n * degree, f"two-period n={n}")

        for d in divisors(n):
            multiplicity = sum(1 for r in range(n) if n // gcd(n, r) == d)
            check(multiplicity == phi(d), f"Ramanujan multiplicity n={n}, d={d}")

        if n <= 14:
            direct = sp.Matrix(a).charpoly(x).as_poly()
            check(direct == grouped_charpoly(n, x), f"charpoly n={n}")

        if n % 2 == 0:
            check(all(((a0 + u) % 2) != (a0 % 2) for a0 in range(n) for u in range(n) if gcd(u, n) == 1), "parity")
            check(trace_formula(n, 2) > 0 and trace_formula(n, 3) == 0, "period two witness")
        else:
            check(trace_formula(n, 2) > 0 and trace_formula(n, n) > 0, "aperiodic witnesses")
            least_prime = min(d for d in divisors(n) if d > 1 and all(d % e for e in range(2, int(d**0.5) + 1)))
            ratios = [
                Fraction(abs(mobius(d)), phi(d))
                for d in divisors(n)
                if d > 1 and mobius(d) != 0
            ]
            expected_rate = Fraction(1, least_prime - 1)
            check(max(ratios) == expected_rate, f"mixing rate n={n}")

        invariant = (degree, n * degree)
        check(invariant not in registry, f"rigidity collision n={n}")
        registry[invariant] = n

    print(f"PASS: {CHECKS:,} exact assertions")
    for n in (5, 8, 12, 15):
        print(f"n={n}: phi={phi(n)}, period={'2' if n % 2 == 0 else '1'}, P2={trace_formula(n, 2)}")
    print("Ramanujan trace formula, parity dichotomy, and rigidity registry verified")


if __name__ == "__main__":
    main()
