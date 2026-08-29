#!/usr/bin/env python3
"""Exact controls for P98.

Lane A compares polynomial gcd degrees with literal companion-matrix ranks.
Lane B enumerates configurations over prime and nonprime fields using only
their additive vector-space structure, and independently checks the affine
residue normal form, local rule, shift action, order, and fixed counts.
"""

from itertools import product
from math import gcd


CHECKS = 0


def check(condition: bool, message: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def vp_split(value: int, p: int) -> tuple[int, int]:
    exponent = 0
    while value % p == 0:
        exponent += 1
        value //= p
    return exponent, value


def predicted_dimension(p: int, r: int, n: int) -> int:
    a, r0 = vp_split(r, p)
    b, n0 = vp_split(n, p)
    common = gcd(r0, n0)
    return min(2 * p**a - 1, p**b) + (common - 1) * min(
        2 * p**a, p**b
    )


def trim(poly: list[int], p: int) -> list[int]:
    poly = [entry % p for entry in poly]
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def poly_divmod(left: list[int], right: list[int], p: int) -> tuple[list[int], list[int]]:
    left = trim(left[:], p)
    right = trim(right[:], p)
    check(right != [0], "nonzero polynomial divisor")
    if len(left) < len(right):
        return [0], left
    quotient = [0] * (len(left) - len(right) + 1)
    inverse = pow(right[-1], -1, p)
    while left != [0] and len(left) >= len(right):
        degree = len(left) - len(right)
        factor = left[-1] * inverse % p
        quotient[degree] = factor
        for index, coefficient in enumerate(right):
            left[index + degree] = (left[index + degree] - factor * coefficient) % p
        left = trim(left, p)
    return trim(quotient, p), left


def poly_gcd(left: list[int], right: list[int], p: int) -> list[int]:
    left, right = trim(left, p), trim(right, p)
    while right != [0]:
        _, remainder = poly_divmod(left, right, p)
        left, right = right, remainder
    inverse = pow(left[-1], -1, p)
    return [(coefficient * inverse) % p for coefficient in left]


def f_polynomial(r: int, p: int) -> list[int]:
    return [(-1) % p] * r + [1] * r


def zn_minus_one(n: int, p: int) -> list[int]:
    out = [0] * (n + 1)
    out[0] = (-1) % p
    out[n] = 1
    return out


def matmul(left: list[list[int]], right: list[list[int]], p: int) -> list[list[int]]:
    size = len(left)
    return [
        [
            sum(left[i][k] * right[k][j] for k in range(size)) % p
            for j in range(size)
        ]
        for i in range(size)
    ]


def identity(size: int) -> list[list[int]]:
    return [[int(i == j) for j in range(size)] for i in range(size)]


def matpow(matrix: list[list[int]], exponent: int, p: int) -> list[list[int]]:
    result = identity(len(matrix))
    base = matrix
    while exponent:
        if exponent & 1:
            result = matmul(result, base, p)
        base = matmul(base, base, p)
        exponent //= 2
    return result


def rank_mod(matrix: list[list[int]], p: int) -> int:
    work = [[entry % p for entry in row] for row in matrix]
    rows = len(work)
    cols = len(work[0]) if rows else 0
    rank = 0
    for col in range(cols):
        pivot = next((row for row in range(rank, rows) if work[row][col]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = pow(work[rank][col], -1, p)
        work[rank] = [(entry * inverse) % p for entry in work[rank]]
        for row in range(rows):
            if row != rank and work[row][col]:
                factor = work[row][col]
                work[row] = [
                    (a - factor * b) % p for a, b in zip(work[row], work[rank])
                ]
        rank += 1
        if rank == rows:
            break
    return rank


def state_matrix(p: int, r: int) -> list[list[int]]:
    dimension = 2 * r - 1
    matrix = [[0] * dimension for _ in range(dimension)]
    for row in range(dimension - 1):
        matrix[row][row + 1] = 1
    for col in range(r):
        matrix[-1][col] = 1
    for col in range(r, dimension):
        matrix[-1][col] = (-1) % p
    return matrix


class AdditiveField:
    """Additive model of F_(p^e); multiplication is not needed here."""

    def __init__(self, p: int, e: int):
        self.p = p
        self.e = e
        self.q = p**e

    def decode(self, value: int) -> list[int]:
        out = []
        for _ in range(self.e):
            out.append(value % self.p)
            value //= self.p
        return out

    def encode(self, vector: list[int]) -> int:
        value = 0
        place = 1
        for coordinate in vector:
            value += (coordinate % self.p) * place
            place *= self.p
        return value

    def add(self, left: int, right: int) -> int:
        return self.encode(
            [(a + b) % self.p for a, b in zip(self.decode(left), self.decode(right))]
        )

    def neg(self, value: int) -> int:
        return self.encode([(-a) % self.p for a in self.decode(value)])

    def sub(self, left: int, right: int) -> int:
        return self.add(left, self.neg(right))

    def scale(self, scalar: int, value: int) -> int:
        return self.encode([(scalar * a) % self.p for a in self.decode(value)])

    def total(self, values) -> int:
        answer = 0
        for value in values:
            answer = self.add(answer, value)
        return answer


def transition(state: tuple[int, ...], r: int, field: AdditiveField) -> tuple[int, ...]:
    nxt = field.sub(field.total(state[:r]), field.total(state[r:]))
    return state[1:] + (nxt,)


def iterate(state: tuple[int, ...], steps: int, r: int, field: AdditiveField) -> tuple[int, ...]:
    for _ in range(steps):
        state = transition(state, r, field)
    return state


def reconstruct_normal(
    state: tuple[int, ...], r: int, field: AdditiveField
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    a = state[:r]
    slopes = [field.sub(state[j + r], state[j]) for j in range(r - 1)]
    slopes.append(field.neg(field.total(slopes)))
    return tuple(a), tuple(slopes)


def normal_value(
    a: tuple[int, ...], slopes: tuple[int, ...], index: int, r: int, field: AdditiveField
) -> int:
    quotient, residue = divmod(index, r)
    return field.add(a[residue], field.scale(quotient, slopes[residue]))


def divisors(value: int) -> list[int]:
    return [candidate for candidate in range(1, value + 1) if value % candidate == 0]


def mobius(value: int) -> int:
    primes = 0
    candidate = 2
    remaining = value
    while candidate * candidate <= remaining:
        if remaining % candidate == 0:
            remaining //= candidate
            primes += 1
            if remaining % candidate == 0:
                return 0
            while remaining % candidate == 0:
                remaining //= candidate
        candidate += 1
    if remaining > 1:
        primes += 1
    return -1 if primes % 2 else 1


def polynomial_and_matrix_lane() -> None:
    for p in (2, 3, 5, 7):
        for r in range(1, 9):
            dimension = 2 * r - 1
            matrix = state_matrix(p, r)
            for n in range(1, 33):
                common = poly_gcd(f_polynomial(r, p), zn_minus_one(n, p), p)
                gcd_dimension = len(common) - 1
                power = matpow(matrix, n, p)
                difference = [
                    [(power[i][j] - int(i == j)) % p for j in range(dimension)]
                    for i in range(dimension)
                ]
                kernel_dimension = dimension - rank_mod(difference, p)
                formula = predicted_dimension(p, r, n)
                check(gcd_dimension == formula, f"gcd formula p={p}, r={r}, n={n}")
                check(kernel_dimension == formula, f"matrix formula p={p}, r={r}, n={n}")

            order = 1 if r == 1 else p * r
            check(predicted_dimension(p, r, order) == dimension, "order reaches all states")
            for n in range(1, order):
                check(
                    predicted_dimension(p, r, n) < dimension,
                    f"order is minimal p={p}, r={r}, n={n}",
                )


def configuration_lane() -> None:
    lanes = [(2, 1, 5), (3, 1, 4), (2, 2, 3), (5, 1, 3), (2, 3, 2), (3, 2, 2)]
    for p, e, r in lanes:
        field = AdditiveField(p, e)
        q = field.q
        dimension = 2 * r - 1
        order = 1 if r == 1 else p * r
        states = list(product(range(q), repeat=dimension))
        fixed = [0] * (order + 1)

        for state in states:
            a, slopes = reconstruct_normal(state, r, field)
            check(field.total(slopes) == 0, "slope sum vanishes")
            rebuilt = tuple(normal_value(a, slopes, i, r, field) for i in range(dimension))
            check(rebuilt == state, "normal form reconstructs state")

            shifted = transition(state, r, field)
            shifted_a = a[1:] + (field.add(a[0], slopes[0]),)
            shifted_d = slopes[1:] + (slopes[0],)
            shifted_normal = tuple(
                normal_value(shifted_a, shifted_d, i, r, field)
                for i in range(dimension)
            )
            check(shifted_normal == shifted, "normal-form shift action")
            check(iterate(state, order, r, field) == state, "registered order")

            for index in range(-2 * r, 2 * r + 1):
                left = field.total(
                    normal_value(a, slopes, index + j, r, field) for j in range(r)
                )
                right = field.total(
                    normal_value(a, slopes, index + r + j, r, field)
                    for j in range(r)
                )
                check(left == right, "local equal-block rule")

            current = state
            for n in range(1, order + 1):
                current = transition(current, r, field)
                fixed[n] += current == state

        for n in range(1, order + 1):
            expected = q ** predicted_dimension(p, r, n)
            check(fixed[n] == expected, f"literal fixed count q={q}, r={r}, n={n}")

        cycle_points = 0
        for m in divisors(order):
            exact = sum(
                mobius(m // d) * q ** predicted_dimension(p, r, d)
                for d in divisors(m)
            )
            check(exact >= 0 and exact % m == 0, "cycle multiplicity is integral")
            cycle_points += exact
        check(cycle_points == q**dimension, "cycle census covers phase space")
        print(
            f"configuration lane q={q}, char={p}, r={r}: "
            f"states={q**dimension}, order={order} PASS"
        )


def main() -> None:
    polynomial_and_matrix_lane()
    configuration_lane()
    print(f"TOTAL EXACT ASSERTIONS: {CHECKS}")
    print("ALL P98 CONTROLS PASS")


if __name__ == "__main__":
    main()
