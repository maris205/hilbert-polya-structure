#!/usr/bin/env python3
"""Exact controls for periodic-alphabet full shifts."""

from itertools import product
from math import prod

import sympy as sp


CHECKS = 0


def check(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def adjacency(schedule):
    offsets = [0]
    for q in schedule:
        offsets.append(offsets[-1] + q)
    size = offsets[-1]
    matrix = [[0] * size for _ in range(size)]
    p = len(schedule)
    for phase, q in enumerate(schedule):
        next_phase = (phase + 1) % p
        for a in range(offsets[phase], offsets[phase + 1]):
            for b in range(offsets[next_phase], offsets[next_phase + 1]):
                matrix[a][b] = 1
    return matrix


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


def fixed_formula(schedule, n):
    p = len(schedule)
    q_product = prod(schedule)
    return 0 if n % p else p * q_product ** (n // p)


def block_indices(p, phase, block):
    """Old-coordinate indices used by Phi_phase at a given block."""
    return tuple(block * p - phase + offset for offset in range(p))


def audit_block_alignment():
    """Check the two coordinate identities in the normal-form proof."""
    for p in range(1, 7):
        for phase in range(p):
            for block in range(-3, 4):
                old = block_indices(p, phase, block)
                for offset, site in enumerate(old):
                    check((phase + site) % p == offset, f"alphabet alignment p={p}, phase={phase}")

                next_phase = (phase + 1) % p
                # T reads old site s+1 at new coordinate s.
                shifted_new = tuple(
                    site + 1 for site in block_indices(p, next_phase, block)
                )
                expected = old if phase < p - 1 else block_indices(p, phase, block + 1)
                check(shifted_new == expected, f"block alignment p={p}, phase={phase}, block={block}")


def main():
    lam = sp.symbols("lambda")
    class_registry = {}

    audit_block_alignment()

    schedules = []
    for p in range(1, 5):
        schedules.extend(product(range(1, 5), repeat=p))

    for schedule in schedules:
        matrix = adjacency(schedule)
        size = len(matrix)
        p = len(schedule)
        q_product = prod(schedule)

        power = identity(size)
        for n in range(1, 2 * p + 5):
            power = matmul(power, matrix)
            check(trace(power) == fixed_formula(schedule, n), f"trace {schedule}, n={n}")

        if size <= 12:
            direct = sp.Matrix(matrix).charpoly(lam).as_expr().expand()
            expected = (lam ** (size - p) * (lam**p - q_product)).expand()
            check(sp.expand(direct - expected) == 0, f"charpoly {schedule}")

        key = (p, q_product)
        ledger = tuple(fixed_formula(schedule, n) for n in range(1, 3 * p + 1))
        if key in class_registry:
            check(class_registry[key] == ledger, f"class ledger {schedule}")
        else:
            class_registry[key] = ledger

    check((2, 12) in class_registry, "expected (p,Q) class")
    check(fixed_formula((2, 6), 2) == fixed_formula((3, 4), 2) == 24, "factorization collapse")
    check(fixed_formula((2, 6), 4) == fixed_formula((3, 4), 4) == 288, "factorization collapse order four")

    print(f"PASS: {CHECKS:,} exact assertions across {len(schedules):,} schedules")
    for schedule in ((2, 6), (3, 4), (1, 2, 3), (2, 2, 2)):
        p = len(schedule)
        q_product = prod(schedule)
        counts = [fixed_formula(schedule, n) for n in range(1, 2 * p + 1)]
        print(f"schedule={schedule}: (p,Q)=({p},{q_product}), fixed={counts}")
    print("normal-form periodic ledgers and characteristic polynomials verified")


if __name__ == "__main__":
    main()
