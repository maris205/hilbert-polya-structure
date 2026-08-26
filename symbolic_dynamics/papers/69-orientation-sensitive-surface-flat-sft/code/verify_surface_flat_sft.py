#!/usr/bin/env python3
"""Finite regression controls for P69.

The script directly enumerates commutator and square-product tuple
counts for D8, Q8, and C3, applies the spanning-tree gauge factor, and compares
the results with the character formulas used in the paper.  The C3 control
also exercises the Frobenius--Schur indicator-zero branch and the full
(+, -, 0) reconstruction.  Finite checks are not proofs of the all-index
theorem.
"""

from collections import Counter
from fractions import Fraction
from itertools import permutations, product


def d8_elements():
    return [(i, j) for i in range(4) for j in range(2)]


def d8_mul(a, b):
    i, j = a
    k, ell = b
    return ((i + (-1 if j else 1) * k) % 4, (j + ell) % 2)


def q8_elements():
    return [(sgn, basis) for sgn in (1, -1) for basis in range(4)]


def q8_positive_mul(a, b):
    if a == 0:
        return 1, b
    if b == 0:
        return 1, a
    if a == b:
        return -1, 0
    positive = {(1, 2): 3, (2, 3): 1, (3, 1): 2}
    if (a, b) in positive:
        return 1, positive[(a, b)]
    sign, basis = q8_positive_mul(b, a)
    return -sign, basis


def q8_mul(a, b):
    sa, ba = a
    sb, bb = b
    sc, bc = q8_positive_mul(ba, bb)
    return sa * sb * sc, bc


def c3_mul(a, b):
    return (a + b) % 3


def cyclic_one_dimensional_fs_indicators(order):
    """Exact FS indicators of the one-dimensional characters of C_order.

    For chi_j(g)=zeta^(j*g), the defining sum is 1 exactly when 2*j is zero
    modulo order and is zero otherwise.
    """

    return [1 if (2 * j) % order == 0 else 0 for j in range(order)]


def inverse(elements, mul, identity, a):
    candidates = [b for b in elements if mul(a, b) == identity and mul(b, a) == identity]
    assert len(candidates) == 1
    return candidates[0]


def check_group(name, elements, mul, identity):
    assert identity in elements
    assert len(set(elements)) == len(elements)
    for a in elements:
        assert mul(identity, a) == a == mul(a, identity)
        inverse(elements, mul, identity, a)
    for a, b, c in product(elements, repeat=3):
        assert mul(mul(a, b), c) == mul(a, mul(b, c))
    print(f"{name}: group axioms PASS (order {len(elements)})")


def convolution(left, right, mul):
    out = Counter()
    for a, ca in left.items():
        for b, cb in right.items():
            out[mul(a, b)] += ca * cb
    return out


def power_convolution(distribution, exponent, mul, identity):
    out = Counter({identity: 1})
    for _ in range(exponent):
        out = convolution(out, distribution, mul)
    return out


def commutator_distribution(elements, mul, identity):
    inv = {a: inverse(elements, mul, identity, a) for a in elements}
    out = Counter()
    for a, b in product(elements, repeat=2):
        value = mul(mul(mul(a, b), inv[a]), inv[b])
        out[value] += 1
    return out


def square_distribution(elements, mul):
    return Counter(mul(a, a) for a in elements)


def orientable_hom_count(elements, mul, identity, genus):
    return power_convolution(
        commutator_distribution(elements, mul, identity), genus, mul, identity
    )[identity]


def nonorientable_hom_count(elements, mul, identity, genus):
    return power_convolution(square_distribution(elements, mul), genus, mul, identity)[identity]


def formula_orientable_fixed(order, degrees, m):
    value = order ** (4 * m) * sum(Fraction(1, d ** (2 * m)) for d in degrees)
    assert value.denominator == 1
    return value.numerator


def formula_nonorientable_fixed(order, degrees, indicators, n):
    value = order ** (2 * n) * sum(
        Fraction(nu ** (n + 2), d**n) for d, nu in zip(degrees, indicators)
    )
    assert value.denominator == 1
    return value.numerator


def verify_surface_formulas(name, elements, mul, identity, degrees, indicators):
    order = len(elements)
    orientable = []
    for m in range(1, 5):
        genus = m + 1
        hom_count = orientable_hom_count(elements, mul, identity, genus)
        direct_fixed = order ** (2 * m - 1) * hom_count
        predicted = formula_orientable_fixed(order, degrees, m)
        assert direct_fixed == predicted
        orientable.append(direct_fixed)

    nonorientable = []
    for n in range(1, 6):
        genus = n + 2
        hom_count = nonorientable_hom_count(elements, mul, identity, genus)
        direct_fixed = order ** (n - 1) * hom_count
        predicted = formula_nonorientable_fixed(order, degrees, indicators, n)
        assert direct_fixed == predicted
        nonorientable.append(direct_fixed)

    print(f"{name}: orientable fixed counts m=1..4 {orientable}")
    print(f"{name}: nonorientable fixed counts n=1..5 {nonorientable}")
    return orientable, nonorientable


def permutation_compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def verify_s3_control():
    elements = list(permutations(range(3)))
    identity = tuple(range(3))
    degrees = [1, 1, 2]
    indicators = [1, 1, 1]
    check_group("S3", elements, permutation_compose, identity)
    values = []
    for genus in range(1, 4):
        direct = orientable_hom_count(elements, permutation_compose, identity, genus)
        predicted = Fraction(len(elements) ** (2 * genus - 1)) * sum(
            Fraction(1, d ** (2 * genus - 2)) for d in degrees
        )
        assert predicted.denominator == 1 and direct == predicted.numerator
        values.append(direct)
    assert values == [18, 486, 16038]
    print(f"S3: orientable Hom counts genus=1..3 {values}")
    assert indicators == [1, 1, 1]


def verify_c3_zero_indicator_control():
    elements = list(range(3))
    identity = 0
    degrees = [1, 1, 1]
    indicators = cyclic_one_dimensional_fs_indicators(3)
    assert indicators == [1, 0, 0]

    check_group("C3", elements, c3_mul, identity)
    print(f"C3: exact one-dimensional FS indicators {indicators}")
    orientable, nonorientable = verify_surface_formulas(
        "C3", elements, c3_mul, identity, degrees, indicators
    )

    assert orientable == [3 ** (4 * m + 1) for m in range(1, 5)]
    assert nonorientable == [3 ** (2 * n) for n in range(1, 6)]

    p_moments = [
        Fraction(orientable[m - 1], 3 ** (4 * m)) for m in range(1, 5)
    ]
    q_moments = [
        Fraction(nonorientable[2 * m - 1], 3 ** (4 * m)) for m in range(1, 3)
    ]
    r_moments = [
        Fraction(nonorientable[2 * m], 3 ** (4 * m + 2)) for m in range(3)
    ]
    assert p_moments == [3, 3, 3, 3]
    assert q_moments == [1, 1]
    assert r_moments == [1, 1, 1]

    total = p_moments[0]
    self_dual = q_moments[0]
    recovered_coefficient = r_moments[0]
    degree = 1
    signed_difference = degree * recovered_coefficient
    c_plus = (self_dual + signed_difference) / 2
    c_minus = (self_dual - signed_difference) / 2
    c_zero = total - self_dual
    assert (c_plus, c_minus, c_zero) == (1, 0, 2)
    print(
        "C3: normalized moments "
        f"P={p_moments}, Q={q_moments}, R={r_moments}"
    )
    print("C3: reconstructed (c_1^+, c_1^-, c_1^0)=(1, 0, 2) PASS")


def main():
    d8 = d8_elements()
    q8 = q8_elements()
    check_group("D8", d8, d8_mul, (0, 0))
    check_group("Q8", q8, q8_mul, (1, 0))

    degrees = [1, 1, 1, 1, 2]
    d8_indicators = [1, 1, 1, 1, 1]
    q8_indicators = [1, 1, 1, 1, -1]

    d8_o, d8_n = verify_surface_formulas(
        "D8", d8, d8_mul, (0, 0), degrees, d8_indicators
    )
    q8_o, q8_n = verify_surface_formulas(
        "Q8", q8, q8_mul, (1, 0), degrees, q8_indicators
    )

    assert d8_o == q8_o
    for n, (left, right) in enumerate(zip(d8_n, q8_n), start=1):
        assert (left == right) == (n % 2 == 0)
    print("D8/Q8: orientable equality and even/odd nonorientable split PASS")

    verify_c3_zero_indicator_control()
    verify_s3_control()
    print("ALL CHECKS PASS")


if __name__ == "__main__":
    main()
