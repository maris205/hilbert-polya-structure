#!/usr/bin/env python3
"""Exact coordinator controls for the P182--P186 breadth gate.

The promoted spike is the nonsingularity-feedback identity toggle

    T(A) = A + 1_{A invertible} I

on n by n matrices over GF(2^r).  The program exhausts GF(2), n <= 4 and
GF(4), n <= 3, and independently checks the subspace-Mobius formula for the
number of invertible A for which A+I is also invertible.
"""

from __future__ import annotations

from itertools import product
from math import prod


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def check(self, condition: bool, label: object) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(label)


class Field:
    """GF(2) or GF(4)=GF(2)[u]/(u^2+u+1), encoded by integers."""

    def __init__(self, order: int) -> None:
        if order not in (2, 4):
            raise ValueError(order)
        self.order = order

    @staticmethod
    def add(a: int, b: int) -> int:
        return a ^ b

    def mul(self, a: int, b: int) -> int:
        if self.order == 2:
            return a & b
        value = 0
        x, y = a, b
        while y:
            if y & 1:
                value ^= x
            y >>= 1
            x <<= 1
            if x & 0b100:
                x ^= 0b111
        return value

    def inv(self, a: int) -> int:
        if a == 0:
            raise ZeroDivisionError
        for b in range(1, self.order):
            if self.mul(a, b) == 1:
                return b
        raise AssertionError((self.order, a))


def is_invertible(entries: tuple[int, ...], n: int, field: Field) -> bool:
    rows = [list(entries[i * n : (i + 1) * n]) for i in range(n)]
    rank = 0
    for col in range(n):
        pivot = next((r for r in range(rank, n) if rows[r][col]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = field.inv(rows[rank][col])
        rows[rank] = [field.mul(scale, x) for x in rows[rank]]
        for r in range(n):
            if r != rank and rows[r][col]:
                factor = rows[r][col]
                rows[r] = [
                    field.add(rows[r][c], field.mul(factor, rows[rank][c]))
                    for c in range(n)
                ]
        rank += 1
    return rank == n


def add_identity(entries: tuple[int, ...], n: int) -> tuple[int, ...]:
    out = list(entries)
    for i in range(n):
        out[i * n + i] ^= 1
    return tuple(out)


def step(entries: tuple[int, ...], n: int, field: Field) -> tuple[int, ...]:
    return add_identity(entries, n) if is_invertible(entries, n, field) else entries


def gaussian_binomial(n: int, k: int, q: int) -> int:
    if not 0 <= k <= n:
        return 0
    numerator = prod(q ** (n - i) - 1 for i in range(k))
    denominator = prod(q ** (k - i) - 1 for i in range(k))
    return numerator // denominator


def gl_order(n: int, q: int) -> int:
    return prod(q**n - q**i for i in range(n))


def linear_derangements(n: int, q: int) -> int:
    """Invertible A with A-I invertible, by subspace Mobius inversion."""
    return sum(
        (-1) ** k
        * q ** (k * (k - 1) // 2)
        * gaussian_binomial(n, k, q)
        * q ** (k * (n - k))
        * gl_order(n - k, q)
        for k in range(n + 1)
    )


def exhaust(order: int, n: int, audit: Audit) -> str:
    field = Field(order)
    states = list(product(range(order), repeat=n * n))
    total = order ** (n * n)
    invertible = {a for a in states if is_invertible(a, n, field)}
    shifted = {a: add_identity(a, n) for a in states}
    images = {a: step(a, n, field) for a in states}
    indegree = {b: 0 for b in states}
    preimages = {b: set() for b in states}
    for source, b in images.items():
        indegree[b] += 1
        preimages[b].add(source)

    gl = gl_order(n, order)
    der = linear_derangements(n, order)
    literal_der = sum(a in invertible and shifted[a] in invertible for a in states)
    singular = total - gl
    recurrent = singular + der
    transient = gl - der

    audit.check(len(states) == total, (order, n, "carrier"))
    audit.check(len(invertible) == gl, (order, n, "GL"))
    audit.check(literal_der == der, (order, n, "linear derangements"))
    audit.check(der % 2 == 0, (order, n, "two-cycle parity"))

    literal_recurrent = 0
    literal_transient = 0
    cycles2 = 0
    for a in states:
        b = images[a]
        c = images[b]
        audit.check(images[c] == c or images[images[c]] == c, (order, n, "height/period", a))
        if b == a:
            literal_recurrent += 1
        elif c == a:
            literal_recurrent += 1
            cycles2 += 1
        else:
            audit.check(c == b, (order, n, "one-step landing", a))
            literal_transient += 1

        expected_sources = set()
        if a not in invertible:
            expected_sources.add(a)
        mate = shifted[a]
        if mate in invertible:
            expected_sources.add(mate)
        actual_sources = preimages[a]
        audit.check(actual_sources == expected_sources, (order, n, "target fibre", a))

    audit.check(literal_recurrent == recurrent, (order, n, "recurrent census"))
    audit.check(literal_transient == transient, (order, n, "transient census"))
    audit.check(cycles2 == der, (order, n, "oriented two-cycle census"))
    audit.check(len(set(images.values())) == recurrent, (order, n, "image census"))

    indegree_profile = {d: sum(v == d for v in indegree.values()) for d in range(3)}
    audit.check(indegree_profile[0] == transient, (order, n, "indegree zero"))
    audit.check(indegree_profile[2] == transient, (order, n, "indegree two"))
    audit.check(indegree_profile[1] == total - 2 * transient, (order, n, "indegree one"))

    for exponent in range(1, 7):
        fixed_iterate = sum(
            iterate(images, a, exponent) == a for a in states
        )
        expected = singular + (der if exponent % 2 == 0 else 0)
        audit.check(fixed_iterate == expected, (order, n, "fixed iterate", exponent))

    return (
        f"GF({order}) n={n} states={total} GL={gl} D={der} "
        f"fixed={singular} two_cycle_states={der} tail1={transient} "
        f"image={recurrent} indegree=0:{indegree_profile[0]},"
        f"1:{indegree_profile[1]},2:{indegree_profile[2]}"
    )


def iterate(images: dict[tuple[int, ...], tuple[int, ...]], state: tuple[int, ...], t: int) -> tuple[int, ...]:
    for _ in range(t):
        state = images[state]
    return state


def main() -> None:
    audit = Audit()
    rows = []
    for order, maximum_n in ((2, 4), (4, 3)):
        for n in range(1, maximum_n + 1):
            rows.append(exhaust(order, n, audit))
    print("ROOT_COORDINATOR_NFIT_PASS")
    for row in rows:
        print(row)
    print(f"ASSERTIONS {audit.assertions}")
    print("DECISION RECOMMEND_NFIT_OWNER_GATE")


if __name__ == "__main__":
    main()
