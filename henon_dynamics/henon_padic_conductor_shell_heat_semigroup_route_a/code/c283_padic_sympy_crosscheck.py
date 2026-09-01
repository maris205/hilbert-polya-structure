#!/usr/bin/env python3
"""Exact symbolic and finite-filtration checks for HCS-C283."""
from __future__ import annotations

import sympy as sp


def expectation(order: int, modulus: int) -> sp.Matrix:
    size = order // modulus
    return sp.Matrix(order, order, lambda i, j: sp.Rational(1, size)
                     if i % modulus == j % modulus else 0)


def main() -> None:
    checks = 0

    def ok(value: bool) -> None:
        nonlocal checks
        assert value
        checks += 1

    for p, level in ((2, 3), (3, 2)):
        order = p**level
        projections = [expectation(order, p**n) for n in range(level + 1)]
        for n, projection in enumerate(projections):
            ok(projection * projection == projection)
            ok(projection.T == projection)
            ok(projection.trace() == p**n)
        for m in range(level + 1):
            for n in range(level + 1):
                ok(projections[m] * projections[n] == projections[min(m, n)])
        operator = sp.zeros(order)
        for n in range(1, level + 1):
            operator += p**n * (projections[n] - projections[n - 1])
        observed = operator.eigenvals()
        expected = {sp.Integer(0): 1}
        expected.update({sp.Integer(p**n): (p - 1) * p ** (n - 1)
                         for n in range(1, level + 1)})
        ok(observed == expected)
        ok(operator * sp.ones(order, 1) == sp.zeros(order, 1))

    s = sp.symbols("s")
    for p in (2, 3, 5, 7):
        for alpha in (sp.Rational(1, 2), sp.Integer(1), sp.Integer(2)):
            zeta = (1 - sp.Rational(1, p)) * p ** (1 - alpha * s) / (1 - p ** (1 - alpha * s))
            ok(sp.simplify(zeta.subs(s, 0) + 1) == 0)
            ok(sp.simplify(sp.diff(zeta, s).subs(s, 0) + alpha * sp.log(p) / (p - 1)) == 0)
            determinant = sp.exp(-sp.diff(zeta, s).subs(s, 0))
            ok(sp.simplify(determinant - p ** (alpha / (p - 1))) == 0)
            residue = sp.limit((s - 1 / alpha) * zeta, s, 1 / alpha)
            ok(sp.simplify(residue - (1 - sp.Rational(1, p)) / (alpha * sp.log(p))) == 0)

    x = sp.symbols("x")
    for p in (2, 3, 5, 7):
        series = sum((p - 1) * p ** (n - 1) * x**n for n in range(1, 9))
        closed_partial = (p - 1) * x * (1 - (p * x) ** 8) / (1 - p * x)
        ok(sp.simplify(series - closed_partial) == 0)
    print(f"C283_SYMPY_PASS ({checks} exact checks; filtration, spectrum, zeta, determinant)")


if __name__ == "__main__":
    main()
