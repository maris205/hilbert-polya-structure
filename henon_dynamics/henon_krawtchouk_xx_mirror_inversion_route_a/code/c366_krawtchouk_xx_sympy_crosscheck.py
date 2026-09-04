#!/usr/bin/env python3
"""Independent symbolic matrix and polynomial lane for HCS-C366."""
from __future__ import annotations

import math
import sys
from fractions import Fraction

import sympy as sp


def refuse_optimized() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C366 SymPy lane refuses optimized Python")


def kval(n: int, r: int, j: int) -> int:
    return sum(
        (-1) ** ell * math.comb(j, ell) * math.comb(n - j, r - ell)
        for ell in range(max(0, r - (n - j)), min(r, j) + 1)
    )


def main() -> None:
    refuse_optimized()
    checks = 0
    x = sp.symbols("x")
    for n in range(9):
        hamiltonian = sp.zeros(n + 1)
        for j in range(n):
            hopping = sp.sqrt((j + 1) * (n - j)) / 2
            hamiltonian[j, j + 1] = hamiltonian[j + 1, j] = hopping
        expected = sp.prod(x - sp.Rational(n - 2 * r, 2) for r in range(n + 1))
        assert sp.expand(hamiltonian.charpoly(x).as_expr() - expected) == 0
        checks += 1
        for r in range(n + 1):
            vector = sp.Matrix([
                sp.sqrt(sp.binomial(n, j)) * kval(n, r, j) for j in range(n + 1)
            ])
            residual = hamiltonian * vector - sp.Rational(n - 2 * r, 2) * vector
            assert sp.simplify(residual) == sp.zeros(n + 1, 1)
            checks += n + 1
        for r in range(n + 1):
            for s in range(n + 1):
                inner = sum(sp.binomial(n, j) * kval(n, r, j) * kval(n, s, j)
                            for j in range(n + 1))
                target = (2 ** n) * sp.binomial(n, r) if r == s else 0
                assert sp.expand(inner - target) == 0
                checks += 1

    y, q = sp.symbols("y q")
    gaussian: dict[tuple[int, int], sp.Expr] = {(0, 0): sp.Integer(1)}
    for n in range(1, 12):
        for m in range(n + 1):
            if m in (0, n):
                gaussian[(n, m)] = sp.Integer(1)
            else:
                gaussian[(n, m)] = sp.expand(
                    gaussian[(n - 1, m)] + q ** (n - m) * gaussian[(n - 1, m - 1)]
                )
            checks += 1
        product = sp.Poly(sp.prod(1 + y * q ** r for r in range(n)), y, q)
        reconstructed = sp.Poly(sum(
            y ** m * q ** (m * (m - 1) // 2) * gaussian[(n, m)]
            for m in range(n + 1)
        ), y, q)
        assert product == reconstructed
        checks += len(product.terms())
        for m in range(n + 1):
            actual = sp.Poly(product.as_expr().coeff(y, m), q)
            expected = sp.Poly(q ** (m * (m - 1) // 2) * gaussian[(n, m)], q)
            assert actual == expected
            checks += max(1, len(actual.terms()))

    sine2, cosine2 = sp.symbols("sine2 cosine2")
    for n in range(21):
        probability_sum = sum(sp.binomial(n, k) * sine2 ** k * cosine2 ** (n - k)
                              for k in range(n + 1))
        assert sp.expand(probability_sum - (sine2 + cosine2) ** n) == 0
        checks += n + 1

    ratios = [Fraction(number, denominator)
              for denominator in range(1, 6) for number in range(-8, 9)]
    for n in range(9):
        for ratio in ratios:  # ratio = 2B/|omega|
            two_pi_identity = ratio.denominator == 1 and (ratio.numerator + n) % 2 == 0
            four_pi_identity = ratio.denominator == 1
            direct_two = all(
                ratio.denominator == 1 and ((ratio.numerator - n) * particles) % 2 == 0
                for particles in range(n + 2)
            )
            direct_four = all(
                ratio.denominator == 1 and (ratio.numerator * particles) % ratio.denominator == 0
                for particles in range(n + 2)
            )
            assert direct_two == two_pi_identity
            assert direct_four == four_pi_identity
            checks += 2

    print(f"C366 SymPy cross-check: PASS ({checks} identities; full Gaussian polynomials through n=11)")


if __name__ == "__main__":
    main()
