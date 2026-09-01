#!/usr/bin/env python3
"""Independent symbolic checks for HCS-C276."""
from __future__ import annotations

import math

import sympy as sp
from sympy.functions.combinatorial.numbers import stirling


def falling(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    return math.factorial(n) // math.factorial(n - k)


def main() -> None:
    checks = 0

    for n in range(1, 33):
        cyclic_sum = sum(
            sp.Rational(falling(n, k) * k, n ** (k + 1))
            for k in range(1, n + 1)
        )
        assert sp.simplify(cyclic_sum - 1) == 0
        checks += 1

        survival = [sp.Rational(falling(n - 1, m), n**m) for m in range(n + 1)]
        masses = [survival[k - 1] - survival[k] for k in range(1, n + 1)]
        cyclic = [
            sp.Rational(falling(n, k) * k, n ** (k + 1))
            for k in range(1, n + 1)
        ]
        assert masses == cyclic
        assert sum(masses, sp.Rational(0)) == 1
        checks += 2

        joint_total = 0
        for k in range(1, n + 1):
            forest = 1 if k == n else k * n ** (n - k - 1)
            cycle_sum = sum(stirling(k, r, kind=1, signed=False) for r in range(1, k + 1))
            assert cycle_sum == math.factorial(k)
            checks += 1
            joint_total += sp.binomial(n, k) * cycle_sum * forest
        assert sp.simplify(joint_total - n**n) == 0
        checks += 1

        marked_total = 0
        for total in range(1, n + 1):
            cell = sp.Rational(falling(n - 1, total - 1), n**total)
            marked_total += total * cell
        assert sp.simplify(marked_total - 1) == 0
        checks += 1

    for n in range(1, 13):
        for roots in range(1, n + 1):
            size = n - roots
            if size == 0:
                determinant = sp.Integer(1)
                expected = sp.Integer(1)
            else:
                matrix = n * sp.eye(size) - sp.ones(size)
                determinant = sp.factor(matrix.det())
                expected = roots * n ** (n - roots - 1)
            assert determinant == expected
            checks += 1

    z = sp.symbols("z")
    for n in range(1, 17):
        tree_series = sum(sp.Rational(k ** (k - 1), math.factorial(k)) * z**k for k in range(1, n + 1))
        assert sp.expand(tree_series.subs(z, 0)) == 0
        checks += 1
        for ell in range(1, n + 1):
            candidate_cycles = sp.Rational(falling(n, ell), ell)
            required_edges_probability = sp.Rational(1, n**ell)
            expected = sp.Rational(falling(n, ell), ell * n**ell)
            assert sp.simplify(candidate_cycles * required_edges_probability - expected) == 0
            checks += 1

    print(f"C276_SYMPY_PASS ({checks} symbolic checks)")


if __name__ == "__main__":
    main()
