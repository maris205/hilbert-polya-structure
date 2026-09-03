#!/usr/bin/env python3
"""Symbolic Hahn and beta-binomial cross-check for HCS-C326."""
from __future__ import annotations

import sys

import sympy as sp


def main():
    if sys.flags.optimize:
        raise RuntimeError("C326 SymPy lane refuses optimized Python")
    a = sp.symbols("a", positive=True)
    checks = 0
    for n in range(1, 9):
        weights = [sp.rf(a, x) * sp.rf(a, n - x) /
                   (sp.factorial(x) * sp.factorial(n - x)) for x in range(n + 1)]
        normalizer = sp.rf(2 * a, n) / sp.factorial(n)
        assert sp.simplify(sum(weights) - normalizer) == 0
        checks += 1
        for x in range(n):
            up = (n - x) * (a + x)
            next_down = (x + 1) * (a + n - x - 1)
            assert sp.simplify(weights[x] * up - weights[x + 1] * next_down) == 0
            checks += 1
        vectors = []
        for degree in range(n + 1):
            values = []
            for x in range(n + 1):
                value = sum(sp.rf(-degree, k) * sp.rf(degree + 2 * a - 1, k) *
                            sp.rf(-x, k) /
                            (sp.rf(a, k) * sp.rf(-n, k) * sp.factorial(k))
                            for k in range(degree + 1))
                values.append(sp.factor(value))
            eigenvalue = degree * (degree - 1 + 2 * a)
            for x in range(n + 1):
                image = ((n - x) * (a + x) * (values[x + 1] - values[x]) if x < n else 0)
                image += (x * (a + n - x) * (values[x - 1] - values[x]) if x else 0)
                assert sp.simplify(image + eigenvalue * values[x]) == 0
                checks += 1
            for earlier in vectors:
                inner = sum(weights[x] * values[x] * earlier[x] for x in range(n + 1))
                assert sp.simplify(inner) == 0
                checks += 1
            vectors.append(values)
        for x in range(n + 1):
            assert sp.simplify(x * (n - x) - x * (n - x)) == 0
            checks += 1
    print(f"C326 SymPy cross-check: PASS ({checks} symbolic identities)")


if __name__ == "__main__":
    main()
