#!/usr/bin/env python3
"""Independent SymPy theorem-identity lane for HCS-C369."""
from __future__ import annotations

import itertools
import sys

import sympy as sp
from sympy.polys.domains import ZZ
from sympy.polys.galoistools import gf_factor, gf_irreducible_p

x, u = sp.symbols("x u")
f = x**4 - x - 1
PARTITIONS = [(1, 1, 1, 1), (1, 1, 2), (2, 2), (1, 3), (4,)]
EXPECTED_CLASSES = {(1, 1, 1, 1): 1, (1, 1, 2): 6, (2, 2): 3, (1, 3): 8, (4,): 6}
WITNESSES = {
    2: ((4,), x**4 + x + 1),
    7: ((1, 3), (x - 3) * (x**3 + 3*x**2 + 2*x - 2)),
    17: ((1, 1, 2), (x + 2) * (x + 5) * (x**2 - 7*x + 5)),
    71: ((2, 2), (x**2 + 15*x - 20) * (x**2 - 15*x + 32)),
    83: ((1, 1, 1, 1), (x + 3) * (x + 7) * (x + 14) * (x - 24)),
}


def cycle_partition(permutation):
    seen = set()
    lengths = []
    for start in range(4):
        if start in seen:
            continue
        current = start
        length = 0
        while current not in seen:
            seen.add(current)
            current = permutation[current]
            length += 1
        lengths.append(length)
    return tuple(sorted(lengths))


def permutation_matrix(partition):
    matrix = sp.zeros(4)
    offset = 0
    for length in partition:
        for j in range(length):
            matrix[offset + (j + 1) % length, offset + j] = 1
        offset += length
    return matrix


def mobius_primitive(fixed, n):
    return sum(sp.mobius(d) * fixed[n // d - 1] for d in sp.divisors(n))


def main():
    if sys.flags.optimize:
        raise RuntimeError("C369 SymPy verifier refuses optimized Python")
    checks = 0
    if sp.discriminant(f, x) != -283:
        raise AssertionError("discriminant")
    checks += 1
    if not gf_irreducible_p([1, 0, 0, 1, 1], 2, ZZ):
        raise AssertionError("mod-2 irreducibility")
    checks += 1
    if sp.integer_nthroot(283, 2)[1]:
        raise AssertionError("discriminant unexpectedly square")
    checks += 1

    for p, (partition, product) in WITNESSES.items():
        difference = sp.Poly(sp.expand(product - f), x, modulus=p)
        if not difference.is_zero:
            raise AssertionError(f"bad displayed factorization p={p}")
        unit, factors = gf_factor([1, 0, 0, -1, -1], p, ZZ)
        got = tuple(sorted(len(coeffs) - 1 for coeffs, multiplicity in factors for _ in range(multiplicity)))
        if unit % p != 1 or got != partition:
            raise AssertionError(f"factor signature p={p}")
        checks += 2

    # The exact group-order chain: irreducibility makes G transitive, while
    # the good-prime witnesses give elements of orders 4 and 3.  Thus 12|#G
    # and #G|24.  The order-12 alternative is the sign kernel A4, excluded by
    # the odd 4-cycle (equivalently by the nonsquare discriminant).
    possible_orders = [order for order in sp.divisors(sp.factorial(4)) if order % 12 == 0]
    if possible_orders != [12, 24] or sp.factorial(4) != 24:
        raise AssertionError("group order divisibility chain")
    if (-1) ** (4 - 1) != -1:
        raise AssertionError("4-cycle parity")
    checks += 3

    class_counts = {partition: 0 for partition in PARTITIONS}
    for permutation in itertools.permutations(range(4)):
        class_counts[cycle_partition(permutation)] += 1
        checks += 1
    if class_counts != EXPECTED_CLASSES or sum(class_counts.values()) != 24:
        raise AssertionError("S4 conjugacy classes")
    checks += 2
    densities = {partition: sp.Rational(size, 24) for partition, size in class_counts.items()}
    if sum(densities.values()) != 1:
        raise AssertionError("density normalization")
    checks += 1

    for partition in PARTITIONS:
        P = permutation_matrix(partition)
        if P.T * P != sp.eye(4):
            raise AssertionError(f"nonunitary permutation matrix {partition}")
        determinant = sp.factor((sp.eye(4) - u * P).det())
        expected_determinant = sp.prod(1 - u**length for length in partition)
        if sp.expand(determinant - expected_determinant) != 0:
            raise AssertionError(f"determinant identity {partition}")
        fixed = [sum(length for length in partition if r % length == 0) for r in range(1, 13)]
        for r in range(1, 13):
            if sp.trace(P**r) != fixed[r - 1]:
                raise AssertionError(f"fixed trace {partition} r={r}")
            primitive = mobius_primitive(fixed, r)
            if primitive != r * partition.count(r):
                raise AssertionError(f"primitive inversion {partition} r={r}")
            checks += 2
        log_derivative = sp.factor(-sp.diff(expected_determinant, u) / expected_determinant)
        cycle_log_derivative = sp.factor(sum(length * u ** (length - 1) / (1 - u**length) for length in partition))
        if sp.factor(log_derivative - cycle_log_derivative) != 0:
            raise AssertionError(f"formal zeta logarithm {partition}")
        if (P == P.T) != (max(partition) <= 2):
            raise AssertionError(f"self-adjoint boundary {partition}")
        checks += 4

    fp = sp.Poly(f, x, modulus=283)
    gcd = fp.gcd(fp.diff())
    if gcd.monic() != sp.Poly(x - 93, x, modulus=283):
        raise AssertionError("ramified gcd")
    ramified_product = (x - 115) * (x - 93) ** 2 * (x + 18)
    if not sp.Poly(sp.expand(ramified_product - f), x, modulus=283).is_zero:
        raise AssertionError("ramified factorization")
    if sp.rem(f, x - 93, domain=sp.GF(283)) != 0 or sp.rem(sp.diff(f, x), x - 93, domain=sp.GF(283)) != 0:
        raise AssertionError("repeated root")
    checks += 4
    print(f"C369 SymPy cross-check: PASS ({checks} exact checks)")


if __name__ == "__main__":
    main()
