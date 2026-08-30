#!/usr/bin/env python3
"""Exact pilot for the proper-residue gcd descent.

For n > 1 choose A uniformly from 1,...,n-1 and replace n by gcd(n,A).
The process is strictly decreasing and is absorbed at 1.  Fractions only.
"""

from functools import lru_cache
from fractions import Fraction
from math import gcd, isqrt


ASSERTIONS = 0


def check(condition):
    global ASSERTIONS
    ASSERTIONS += 1
    assert condition


def divisors(n):
    low = []
    high = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            low.append(d)
            if d * d != n:
                high.append(n // d)
    return low + high[::-1]


def phi(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            result -= result // p
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        result -= result // n
    return result


def poly_add(target, source, scale=Fraction(1), shift=0):
    if len(target) < len(source) + shift:
        target.extend([Fraction(0)] * (len(source) + shift - len(target)))
    for i, value in enumerate(source):
        target[i + shift] += scale * value


@lru_cache(None)
def divisor_pgf(n):
    if n == 1:
        return (Fraction(1),)
    out = []
    for d in divisors(n):
        if d < n:
            poly_add(out, divisor_pgf(d), Fraction(phi(n // d), n - 1), 1)
    return tuple(out)


@lru_cache(None)
def literal_pgf(n):
    if n == 1:
        return (Fraction(1),)
    out = []
    for a in range(1, n):
        poly_add(out, literal_pgf(gcd(n, a)), Fraction(1, n - 1), 1)
    return tuple(out)


def prime_power_formula(p, k):
    out = [Fraction(0), Fraction(1)]
    for j in range(1, k):
        c = p * (p**j - 1) // (p - 1)
        nxt = [Fraction(0)] * (len(out) + 1)
        for degree, value in enumerate(out):
            nxt[degree] += value * Fraction(c, c + 1)
            nxt[degree + 1] += value * Fraction(1, c + 1)
        out = nxt
    return tuple(out)


def omega(n):
    count = 0
    p = 2
    while p * p <= n:
        while n % p == 0:
            n //= p
            count += 1
        p += 1
    return count + (n > 1)


def main():
    for n in range(1, 241):
        a = divisor_pgf(n)
        b = literal_pgf(n)
        check(a == b)
        check(sum(a) == 1)
        check(all(x >= 0 for x in a))
        check(len(a) - 1 == omega(n))
        if n > 1:
            check(a[0] == 0)
            check(a[1] == Fraction(phi(n), n - 1))

        if n > 1:
            histogram = {}
            for residue in range(1, n):
                d = gcd(n, residue)
                histogram[d] = histogram.get(d, 0) + 1
            check(sum(histogram.values()) == n - 1)
            for d in divisors(n):
                if d < n:
                    check(histogram.get(d, 0) == phi(n // d))

    primes = (2, 3, 5, 7, 11, 13, 17, 19)
    for p in primes:
        check(phi(p) == p - 1)
        for k in range(1, 9):
            exact = divisor_pgf(p**k)
            product = prime_power_formula(p, k)
            check(exact == product)
            check(sum(product) == 1)

            mean = sum(Fraction(i) * value for i, value in enumerate(exact))
            predicted_mean = Fraction(1)
            predicted_variance = Fraction(0)
            for j in range(1, k):
                c = p * (p**j - 1) // (p - 1)
                predicted_mean += Fraction(1, c + 1)
                predicted_variance += Fraction(c, (c + 1) ** 2)
            second = sum(Fraction(i * i) * value for i, value in enumerate(exact))
            check(mean == predicted_mean)
            check(second - mean * mean == predicted_variance)

    examples = (6, 12, 24, 30, 36, 60, 72, 120)
    print("proper-residue gcd descent pilot: PASS")
    print(f"exact assertions: {ASSERTIONS:,}")
    print("literal/divisor-PGF agreement: 1 <= n <= 240")
    print("prime-power product law: p <= 19, 1 <= k <= 8")
    print("PGF convention: coefficient of z^t is P(T_n=t)")
    for n in examples:
        coeffs = ",".join(str(x) for x in divisor_pgf(n))
        print(f"n={n}: [{coeffs}]")


if __name__ == "__main__":
    main()
