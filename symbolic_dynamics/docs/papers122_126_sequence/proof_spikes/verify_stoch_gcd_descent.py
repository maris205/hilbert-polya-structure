#!/usr/bin/env python3
"""Independent exact verifier for the proper-residue gcd descent dossier.

No imports are made from the scouting pilot.  All probabilities are Fractions;
there is no sampling, floating point arithmetic, or truncation.
"""

from fractions import Fraction
from functools import lru_cache
from itertools import permutations
from math import factorial, gcd


ASSERTIONS = 0


def check(statement):
    global ASSERTIONS
    ASSERTIONS += 1
    assert statement


def factorization(n):
    factors = []
    p = 2
    while p * p <= n:
        exponent = 0
        while n % p == 0:
            n //= p
            exponent += 1
        if exponent:
            factors.append((p, exponent))
        p += 1
    if n > 1:
        factors.append((n, 1))
    return tuple(factors)


def divisors(n):
    result = [1]
    for p, exponent in factorization(n):
        old = tuple(result)
        power = 1
        for _ in range(exponent):
            power *= p
            result.extend(d * power for d in old)
    return tuple(sorted(result))


def phi(n):
    value = n
    for p, _ in factorization(n):
        value -= value // p
    return value


def big_omega(n):
    return sum(exponent for _, exponent in factorization(n))


def add_scaled(target, source, scale, shift):
    while len(target) < len(source) + shift:
        target.append(Fraction(0))
    for degree, coefficient in enumerate(source):
        target[degree + shift] += scale * coefficient


@lru_cache(None)
def divisor_pgf(n):
    if n == 1:
        return (Fraction(1),)
    answer = []
    for d in divisors(n):
        if d < n:
            add_scaled(
                answer,
                divisor_pgf(d),
                Fraction(phi(n // d), n - 1),
                1,
            )
    return tuple(answer)


@lru_cache(None)
def residue_pgf(n):
    """Literal implementation: visit every allowed residue, not divisors."""
    if n == 1:
        return (Fraction(1),)
    answer = []
    for a in range(1, n):
        add_scaled(answer, residue_pgf(gcd(n, a)), Fraction(1, n - 1), 1)
    return tuple(answer)


@lru_cache(None)
def explicit_history_coefficients(n):
    """Enumerate strict divisor histories and multiply their edge weights."""
    if n == 1:
        return {0: Fraction(1)}
    answer = {}
    for d in divisors(n):
        if d == n:
            continue
        edge = Fraction(phi(n // d), n - 1)
        for length, mass in explicit_history_coefficients(d).items():
            answer[length + 1] = answer.get(length + 1, Fraction(0)) + edge * mass
    return answer


def leading_history_formula(n):
    """Sum maximal histories over distinct orders of the prime multiset."""
    primes = []
    for p, exponent in factorization(n):
        primes.extend([p] * exponent)
    total = Fraction(0)
    for ordering in set(permutations(primes)):
        state = n
        weight = Fraction(1)
        for p in ordering:
            weight *= Fraction(p - 1, state - 1)
            state //= p
        check(state == 1)
        total += weight
    return total


def multiply_by_bernoulli(poly, success_probability):
    answer = [Fraction(0)] * (len(poly) + 1)
    for degree, coefficient in enumerate(poly):
        answer[degree] += coefficient * (1 - success_probability)
        answer[degree + 1] += coefficient * success_probability
    return tuple(answer)


def prime_power_product(p, k):
    answer = (Fraction(0), Fraction(1))
    for j in range(1, k):
        c = p * (p**j - 1) // (p - 1)
        answer = multiply_by_bernoulli(answer, Fraction(1, c + 1))
    return answer


def moment(poly, order):
    return sum(Fraction(t**order) * probability for t, probability in enumerate(poly))


def main():
    # Kernel, normalization, degree, first coefficient, and literal agreement.
    for n in range(1, 301):
        pgf = divisor_pgf(n)
        check(sum(pgf) == 1)
        check(all(coefficient >= 0 for coefficient in pgf))
        check(len(pgf) - 1 == big_omega(n))
        if n == 1:
            check(pgf == (Fraction(1),))
            continue

        histogram = {}
        for a in range(1, n):
            d = gcd(n, a)
            histogram[d] = histogram.get(d, 0) + 1
        check(sum(histogram.values()) == n - 1)
        for d in divisors(n):
            if d < n:
                check(histogram.get(d, 0) == phi(n // d))
        check(pgf[0] == 0)
        check(pgf[1] == Fraction(phi(n), n - 1))

        if n <= 180:
            check(pgf == residue_pgf(n))
            check(pgf[-1] == leading_history_formula(n))
        if n <= 140:
            history = explicit_history_coefficients(n)
            reconstructed = tuple(history.get(t, Fraction(0)) for t in range(big_omega(n) + 1))
            check(pgf == reconstructed)

    # Prime-power factorization, moments, sharp atoms, and finite tail bounds.
    primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)
    for p in primes:
        for k in range(1, 11):
            exact = divisor_pgf(p**k)
            product = prime_power_product(p, k)
            check(exact == product)

            mean = Fraction(1)
            variance = Fraction(0)
            for j in range(1, k):
                c = p * (p**j - 1) // (p - 1)
                q = Fraction(1, c + 1)
                mean += q
                variance += q * (1 - q)
            check(moment(exact, 1) == mean)
            check(moment(exact, 2) - mean * mean == variance)

            one_step = Fraction(p ** (k - 1) * (p - 1), p**k - 1)
            check(exact[1] == one_step)
            check(one_step - Fraction(p - 1, p) == Fraction(p - 1, p * (p**k - 1)))

            max_time = Fraction(1)
            scaled_max_time = Fraction(1)
            for r in range(2, k + 1):
                max_time *= Fraction(p - 1, p**r - 1)
                scaled_max_time *= Fraction(1, 1 - Fraction(1, p**r))
            check(exact[k] == max_time)
            check(
                max_time
                == Fraction((p - 1) ** (k - 1), p ** (k * (k + 1) // 2 - 1))
                * scaled_max_time
            )

            for r in range(1, k):
                tail = sum(exact[r + 1 :])
                bound = Fraction(1, factorial(r) * (p - 1) ** r)
                check(tail <= bound)

    print("proper-residue gcd descent proof verifier: PASS")
    print(f"exact assertions: {ASSERTIONS:,}")
    print("kernel/degree/first coefficient: 1 <= n <= 300")
    print("literal-residue PGF and maximal-history formula: 1 <= n <= 180")
    print("explicit strict-history sum: 1 <= n <= 140")
    print("prime-power product/moments/endpoints/tails: p <= 31, 1 <= k <= 10")
    print("arithmetic: Fraction only; no sampling, floating point, or truncation")


if __name__ == "__main__":
    main()
