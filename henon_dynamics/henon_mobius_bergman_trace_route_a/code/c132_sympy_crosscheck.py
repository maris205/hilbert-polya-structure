#!/usr/bin/env python3
"""Separate SymPy reconstruction for C132."""
from itertools import product
import sympy as sp


def main() -> None:
    z, s = sp.symbols("z s")
    checks = 0
    matrices = {3: sp.Matrix([[0, 1], [1, 3]]), 6: sp.Matrix([[0, 1], [1, 6]])}
    for digit in [3, 6]:
        center = sp.Rational(digit, digit**2 - 1)
        radius = sp.Rational(1, digit**2 - 1)
        assert center + radius == sp.Rational(1, digit - 1)
        checks += 1
    assert sp.Rational(3, 8) - sp.Rational(6, 35) - sp.Rational(1, 8) - sp.Rational(1, 35) == sp.Rational(1, 20)
    checks += 1
    for n in range(1, 9):
        for word in product((3, 6), repeat=n):
            M = sp.eye(2)
            for digit in word:
                M *= matrices[digit]
            a, b, c, d = map(int, [M[0, 0], M[0, 1], M[1, 0], M[1, 1]])
            determinant = int(M.det())
            trace = int(sp.trace(M))
            disc = trace**2 - 4 * determinant
            fixed = (a - d + s) / (2 * c)
            fixed_numerator = sp.together(c * fixed**2 + (d-a) * fixed - b).as_numer_denom()[0]
            assert determinant == (-1)**n
            assert sp.rem(sp.Poly(fixed_numerator, s), sp.Poly(s**2 - disc, s)).is_zero
            assert disc == (d-a)**2 + 4*b*c
            assert trace**2 - disc == 4 * determinant
            multiplier = (trace - s) / (trace + s)
            weight_identity = sp.cancel(1 / (1 - multiplier) - (sp.Rational(1, 2) + sp.Rational(trace, 2) / s))
            assert weight_identity == 0
            checks += 5
    M1 = matrices[3]**3 * matrices[6]**2
    M2 = matrices[3]**2 * matrices[6] * matrices[3] * matrices[6]
    assert M1 == sp.Matrix([[63, 388], [208, 1281]])
    assert M2 == sp.Matrix([[60, 379], [199, 1257]])
    assert sp.trace(M1) == 1344 and sp.trace(M2) == 1317
    t1, t2 = int(sp.trace(M1)), int(sp.trace(M2))
    assert t1**2 * (t2**2 + 4) != t2**2 * (t1**2 + 4)
    # The positive trace weight is 1/2+t/(2*sqrt(t^2+4)); the preceding
    # cross-product proves the two weights differ, hence so do the multipliers.
    first, second = (3, 3, 3, 6, 6), (3, 3, 6, 3, 6)
    assert second not in {first[i:] + first[:i] for i in range(5)}
    checks += 6
    r = sp.symbols("r", integer=True, nonnegative=True)
    assert sp.summation((r + 1) * sp.Rational(1, 2)**r, (r, 0, sp.oo)) == 4
    assert sp.summation((r + 1) * sp.Rational(1, 5)**r, (r, 0, sp.oo)) == sp.Rational(25, 16)
    checks += 2
    print(f"C132 SymPy cross-check: PASS ({checks} exact checks)")


if __name__ == "__main__":
    main()
