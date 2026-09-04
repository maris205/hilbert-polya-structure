#!/usr/bin/env python3
"""Independent exact symbolic lane for HCS-C370."""
from __future__ import annotations

if not __debug__:
    raise RuntimeError("c370 SymPy lane refuses optimized Python")

import argparse
import math

import sympy as s


def main():
    argparse.ArgumentParser().parse_args()
    checks = 0

    # Ambient complex-coordinate calculation for the declared normalization.
    a, z, zb = s.symbols("a z zb", nonzero=True)
    dz_r = 2 * s.pi * s.I * z / a
    dzb_r = -2 * s.pi * s.I * zb / a
    alpha_piece = s.I * a * (z * dzb_r - zb * dz_r) / (4 * s.pi)
    assert s.simplify(alpha_piece - z * zb) == 0
    checks += 1

    # i_R d alpha is minus d of the sphere norm, hence vanishes on T S^5.
    coeff_dz = s.simplify(s.I * a * (-dzb_r) / (2 * s.pi))
    coeff_dzb = s.simplify(s.I * a * dz_r / (2 * s.pi))
    assert coeff_dz == -zb and coeff_dzb == -z
    checks += 1

    # R preserves the weighted polynomial: df(R)=2*pi*i*f.
    exponent = s.symbols("exponent", integer=True, positive=True)
    weighted_derivative = s.simplify(
        exponent * z ** (exponent - 1) * (2 * s.pi * s.I * z / exponent)
    )
    assert weighted_derivative == 2 * s.pi * s.I * z**exponent
    checks += 1

    rho = s.symbols("rho", real=True)
    angle = 2 * s.pi * rho
    rotation = s.Matrix([[s.cos(angle), -s.sin(angle)], [s.sin(angle), s.cos(angle)]])
    determinant = s.trigsimp((s.eye(2) - rotation).det())
    assert s.trigsimp(determinant - 4 * s.sin(s.pi * rho) ** 2) == 0
    checks += 1

    p_symbol, q_symbol = s.symbols("p q", integer=True, positive=True)
    chi = s.Rational(1, 2) + 1 / p_symbol + 1 / q_symbol - 1
    rs = -2 * p_symbol * q_symbol + 4 * p_symbol + 4 * q_symbol
    assert s.simplify(2 * (2 * p_symbol * q_symbol) * chi - rs) == 0
    checks += 1
    count_sum = (
        (2 * p_symbol * q_symbol - p_symbol - q_symbol)
        + (q_symbol - 1)
        + (p_symbol - 1)
        + 1
        + 1
    )
    assert s.expand(count_sum - 2 * p_symbol * q_symbol) == 0
    checks += 1

    pairs = [
        (p, q)
        for p in range(3, 102, 2)
        for q in range(p + 2, 102, 2)
        if math.gcd(p, q) == 1
    ]
    positive = []
    for p, q in pairs:
        assert s.ilcm(2, p, q) == 2 * p * q
        checks += 1
        rotation_numbers = (s.Rational(2 * p, q), s.Rational(2 * q, p), s.Rational(p * q, 2))
        assert [value.q for value in rotation_numbers] == [q, p, 2]
        checks += 1
        for value in rotation_numbers:
            assert all((cover * value).q != 1 for cover in range(1, value.q))
            assert (value.q * value).q == 1
            checks += 2
        exact_chi = s.Rational(1, 2) + s.Rational(1, p) + s.Rational(1, q) - 1
        exact_rs = -2 * p * q + 4 * p + 4 * q
        assert 2 * (2 * p * q) * exact_chi == exact_rs
        checks += 1
        assert exact_chi != 0 and exact_rs != 0
        checks += 1
        assert (exact_chi > 0) == (exact_rs > 0)
        checks += 1
        if exact_chi > 0:
            positive.append((p, q))
    assert positive == [(3, 5)]
    checks += 1
    assert len(pairs) == 1003
    checks += 1
    print(f"C370 SymPy PASS: exact_symbolic_checks={checks} pairs={len(pairs)}")


if __name__ == "__main__":
    main()
