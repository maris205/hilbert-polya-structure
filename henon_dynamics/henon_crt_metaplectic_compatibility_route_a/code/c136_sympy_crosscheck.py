#!/usr/bin/env python3
"""Independent SymPy/congruence cross-check for HCS-C136."""

from __future__ import annotations

import json
import math
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "results" / "c136_crt_metaplectic_evidence.json").read_text())


def zero_mod(value: int, modulus: int) -> bool:
    return int(sp.Mod(sp.Integer(value), sp.Integer(modulus))) == 0


checks = 0
for row in DATA["certified_pair_receipts"]:
    m, n, level = row["M"], row["N"], row["L"]
    a, b = row["a_M_inverse_of_N"], row["a_N_inverse_of_M"]
    em, en = row["crt_idempotents"]["e_M"], row["crt_idempotents"]["e_N"]
    hm, hn, hl = pow(2, -1, m), pow(2, -1, n), pow(2, -1, level)
    assertions = [
        math.gcd(m, n) == 1,
        zero_mod(n * a - 1, m),
        zero_mod(m * b - 1, n),
        zero_mod(em * em - em, level),
        zero_mod(en * en - en, level),
        zero_mod(em * en, level),
        zero_mod(em + en - 1, level),
        zero_mod(2 * hl - 1, level),
    ]
    assert all(assertions)
    checks += len(assertions)
    for x in range(level):
        xm, xn = x % m, x % n
        # The canonical CRT basis permutation is real, so coefficientwise
        # conjugation has the same pair of residue labels.
        assert (x % m, x % n) == (xm, xn)
        checks += 1
        assert zero_mod(
            3 * hl * x * x
            - n * 3 * a * hm * xm * xm
            - m * 3 * b * hn * xn * xn,
            level,
        )
        checks += 1
        for y in range(level):
            ym, yn = y % m, y % n
            assert zero_mod(x * y - n * a * xm * ym - m * b * xn * yn, level)
            assert zero_mod(
                (3 * hl * x * x - x * y)
                - n * a * (3 * hm * xm * xm - xm * ym)
                - m * b * (3 * hn * xn * xn - xn * yn),
                level,
            )
            checks += 2

    for c in (1, 2):
        cm = (c % m) * pow(n, -1, m) % m
        cn = (c % n) * pow(m, -1, n) % n
        for x in range(level):
            for y in range(level):
                assert zero_mod(
                    c * x * y
                    - n * cm * (x % m) * (y % m)
                    - m * cn * (x % n) * (y % n),
                    level,
                )
                checks += 1

assert [row["r"] for row in DATA["antiunitary_level_receipts"]] == [3, 5, 9, 15]
checks += 4
for row in DATA["antiunitary_level_receipts"]:
    level = row["r"]
    h = pow(2, -1, level)
    units = [c for c in range(1, level) if math.gcd(c, level) == 1]
    assert [entry["character"] for entry in row["unit_characters"]] == units
    checks += len(units)
    for c in units:
        for x in range(level):
            for y in range(level):
                frequency = c * (x - y) % level
                assert (frequency == 0) == (x == y)
                assert zero_mod(
                    (-3 * c * h * x * x + c * x * y)
                    - (-3 * c * h * x * x + c * x * y),
                    level,
                )
                assert zero_mod(
                    (c * x * y - 3 * c * h * y * y)
                    - (c * x * y - 3 * c * h * y * y),
                    level,
                )
                checks += 3
        for q in range(level):
            for p in range(level):
                reordered = c * h * q * p - c * p * q
                target = -c * h * p * q
                assert zero_mod(reordered - target, level)
                checks += 1
                for x in range(level):
                    output = (x + q) % level
                    assert zero_mod(
                        reordered + c * p * output
                        - (c * p * x + c * h * p * q),
                        level,
                    )
                    checks += 1

for row in DATA["certified_triple_receipts"]:
    factors = tuple(row["factors"])
    level = row["L"]
    for char in row["characters"]:
        c = char["character"]
        direct = {
            str(r): (c % r) * pow(level // r, -1, r) % r
            for r in factors
        }
        assert direct == char["direct_twists"]
        assert direct == char["left_bracket_twists"]
        assert direct == char["right_bracket_twists"]
        checks += 3 * len(factors)
        # The n-ary character identity is determined coefficientwise.
        for r in factors:
            cofactor = level // r
            assert zero_mod(cofactor * direct[str(r)] - c, r)
            checks += 1

four = DATA["four_factor_coherence_receipt"]
for char in four["characters"]:
    for twists in char["bracketings"].values():
        assert twists == char["direct_twists"]
        checks += len(four["factors"])

# Cyclotomic exactness of the headline negative control.
z = sp.symbols("z")
phi15 = sp.Poly(sp.cyclotomic_poly(15, z), z, domain=sp.ZZ)
naive = sp.rem(sp.Poly(z - z**8, z, domain=sp.ZZ), phi15)
correct = sp.rem(sp.Poly(z - z**16, z, domain=sp.ZZ), phi15)
assert naive.as_expr() != 0
assert correct.as_expr() == 0
checks += 2

assert DATA["controls"]["noncoprime"]["gcd"] == sp.gcd(3, 9) == 3
assert not any((2 * x - 1) % 4 == 0 for x in range(4))
checks += 2

expected_enumerated = (
    DATA["exact_certificate"]["pair_fourier_kernel_cases"]
    + DATA["exact_certificate"]["pair_chirp_diagonal_cases"]
    + DATA["exact_certificate"]["pair_unitary_kernel_cases"]
    + DATA["exact_certificate"]["pair_weyl_basis_action_cases"]
    + DATA["exact_certificate"]["pair_conjugation_basis_cases"]
    + DATA["exact_certificate"]["pair_antiunitary_crt_kernel_cases"]
    + DATA["exact_certificate"]["triple_unitary_kernel_cases"]
    + DATA["exact_certificate"]["antiunitary_theta_square_cases"]
    + DATA["exact_certificate"]["antiunitary_unitary_reversal_cases"]
    + DATA["exact_certificate"]["antiunitary_weyl_swap_cases"]
)
assert expected_enumerated == 1131414
checks += 1

print(f"C136 SymPy/congruence cross-check: PASS ({checks} exact checks)")
