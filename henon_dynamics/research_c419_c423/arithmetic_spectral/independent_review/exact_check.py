"""One frozen N=50 check, reconstructed from Young (7.1); no census."""

import json
from math import gcd

import sympy as sp


Q, LEVEL, L = 5, 50, 2
OLDFORMS = (1, 2)
CUSP_DENOMINATORS = (5, 10)
I = sp.I


def character(n, conjugate=False):
    value = {0: 0, 1: 1, 2: I, 3: -I, 4: -1}[n % Q]
    return sp.conjugate(value) if conjugate else value


def young_coefficient(s, conjugate=False):
    """Rows B, columns f, exact d/e sum in Young's Theorem 7.1."""
    result = sp.zeros(2)
    for row, b_old in enumerate(OLDFORMS):
        a_old = L // b_old
        for d in sp.divisors(a_old):
            for e in sp.divisors(b_old):
                if gcd(d, e) != 1:
                    continue
                f = Q * b_old * d // e
                other = Q * a_old * e // d
                coefficient = (
                    character(d, conjugate)
                    * character(e, conjugate)
                    * sp.Rational(d * e) ** (-s)
                    * sp.Rational(LEVEL, gcd(f, other)) ** s
                )
                result[row, CUSP_DENOMINATORS.index(f)] += coefficient
    return sp.simplify(result)


def normalized_channel_matrix(s, conjugate=False):
    return sp.simplify(
        sp.Integer(10) ** (2 * s - 1)
        * young_coefficient(s, conjugate).inv()
        * young_coefficient(1 - s, not conjugate)
    )


def paired_block(s):
    result = sp.zeros(4)
    result[:2, 2:] = normalized_channel_matrix(s)
    result[2:, :2] = normalized_channel_matrix(s, True)
    return result


def main():
    assert character(2) == I and character(2) ** 2 == -1
    assert all(sp.im(character(n) ** 2) == 0 for n in range(5))
    for s in (2, 3, -1, -2):
        expected = sp.Integer(10) ** s * sp.Matrix(
            [[1, I * sp.Integer(2) ** (-s)], [I * sp.Integer(2) ** (-s), 1]]
        )
        assert sp.simplify(young_coefficient(s) - expected) == sp.zeros(2)

    walsh = sp.Matrix([[1, 1], [1, -1]])
    fixed_transform = sp.diag(walsh, walsh)
    two = sp.simplify(fixed_transform.inv() * paired_block(2) * fixed_transform)
    three = sp.simplify(fixed_transform.inv() * paired_block(3) * fixed_transform)
    plus_two = two.extract([0, 2], [0, 2])
    plus_three = three.extract([0, 2], [0, 2])
    plus_commutator = sp.simplify(plus_two * plus_three - plus_three * plus_two)
    expected_commutator = sp.diag(sp.Rational(384, 221) * I, -sp.Rational(384, 221) * I)
    assert plus_commutator == expected_commutator
    full_commutator = sp.simplify(paired_block(2) * paired_block(3) - paired_block(3) * paired_block(2))
    assert full_commutator != sp.zeros(4)
    print(json.dumps({
        "scope": "N=50 only; s=2, t=3; exact Q(i) arithmetic",
        "young_formula_reconstruction": "PASS at s=2,3,-1,-2",
        "fixed_plus_block_s2": str(plus_two),
        "fixed_plus_block_s3": str(plus_three),
        "normalized_plus_commutator": str(plus_commutator),
        "full_normalized_fixed_block_commutator_nonzero": True,
        "classification_claimed": False,
    }, indent=2))


if __name__ == "__main__":
    main()
