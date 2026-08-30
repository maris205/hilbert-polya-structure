#!/usr/bin/env python3
"""Exact pilot for the fixed-regular-unipotent Engel map on UT_n(F_q).

The field sizes used below are prime.  The theorem itself is formulated over
every finite field; the pilot is bounded falsification evidence only.
"""

from collections import Counter
from functools import lru_cache
from itertools import product


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def identity(n):
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))


def multiply(left, right, prime):
    n = len(left)
    return tuple(
        tuple(sum(left[i][h] * right[h][j] for h in range(n)) % prime for j in range(n))
        for i in range(n)
    )


@lru_cache(maxsize=None)
def inverse(matrix, prime):
    n = len(matrix)
    unit = identity(n)
    nilpotent = tuple(
        tuple((matrix[i][j] - unit[i][j]) % prime for j in range(n))
        for i in range(n)
    )
    answer = [list(row) for row in unit]
    power = unit
    sign = 1
    for _ in range(1, n):
        power = multiply(power, nilpotent, prime)
        sign = -sign
        for i in range(n):
            for j in range(n):
                answer[i][j] = (answer[i][j] + sign * power[i][j]) % prime
    return tuple(tuple(row) for row in answer)


def regular_unipotent(n):
    return tuple(
        tuple(int(i == j or j == i + 1) for j in range(n))
        for i in range(n)
    )


@lru_cache(maxsize=None)
def engel(matrix, regular, prime):
    """[matrix,regular]=matrix^-1 regular^-1 matrix regular."""
    return multiply(
        multiply(
            multiply(inverse(matrix, prime), inverse(regular, prime), prime),
            matrix,
            prime,
        ),
        regular,
        prime,
    )


def gamma_elements(n, prime, level):
    coordinates = [(i, j) for i in range(n) for j in range(i + level, n)]
    for values in product(range(prime), repeat=len(coordinates)):
        matrix = [list(row) for row in identity(n)]
        for (i, j), value in zip(coordinates, values):
            matrix[i][j] = value
        yield tuple(tuple(row) for row in matrix)


def in_gamma(matrix, level):
    n = len(matrix)
    return all(matrix[i][j] == 0 for i in range(n) for j in range(i + 1, min(n, i + level)))


@lru_cache(maxsize=None)
def depth(matrix, regular, prime):
    unit = identity(len(matrix))
    time = 0
    while matrix != unit:
        matrix = engel(matrix, regular, prime)
        time += 1
    return time


def cumulative_exponent(n, level, time):
    return sum(n - j for j in range(level, level + time))


def predicted_layer(n, prime, level, time):
    if time == 0:
        return 1
    previous = cumulative_exponent(n, level, time - 1)
    return (prime ** (n - level - time + 1) - 1) * prime**previous


def run_case(n, prime):
    regular = regular_unipotent(n)
    unit = identity(n)
    for level in range(1, n):
        domain = tuple(gamma_elements(n, prime, level))
        image_counts = Counter(engel(x, regular, prime) for x in domain)
        target = set(gamma_elements(n, prime, level + 1))
        check(set(image_counts) == target, (n, prime, level, "surjectivity"))
        check(set(image_counts.values()) == {prime ** (n - level)}, (n, prime, level, image_counts))

        histogram = Counter(depth(x, regular, prime) for x in domain)
        expected = {
            time: predicted_layer(n, prime, level, time)
            for time in range(0, n - level + 1)
        }
        check(histogram == Counter(expected), (n, prime, level, histogram, expected))
        check(sum(histogram.values()) == len(domain), (n, prime, level))

        for x in domain:
            y = engel(x, regular, prime)
            check(in_gamma(y, level + 1), (n, prime, level, x, y))
            check(depth(x, regular, prime) <= n - level, (n, prime, level, x))

        centralizer = [x for x in domain if engel(x, regular, prime) == unit]
        check(len(centralizer) == prime ** (n - level), (n, prime, level, len(centralizer)))


def main():
    for prime, maximum_n in ((2, 6), (3, 4), (5, 4)):
        for n in range(2, maximum_n + 1):
            run_case(n, prime)
    print("alg_regular_engel: PASS")
    print(f"assertions={ASSERTIONS}")
    print("gamma_k_to_gamma_(k+1)=surjective")
    print("fibre_on_gamma_k=q^(n-k)")
    print("max_depth_on_gamma_k=n-k")
    print("layer(k,t)=(q^(n-k-t+1)-1)q^sum_(j=k)^(k+t-2)(n-j)")


if __name__ == "__main__":
    main()
