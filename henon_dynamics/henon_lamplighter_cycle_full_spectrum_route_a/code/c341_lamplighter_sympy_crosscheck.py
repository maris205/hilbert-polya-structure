#!/usr/bin/env python3
"""Independent SymPy algebra lane for HCS-C341."""
from __future__ import annotations

import sys

import sympy as sp


def need(condition, label):
    if condition is not True and condition != sp.S.true:
        raise AssertionError(label)


def cycle_kernel(n):
    if n == 1:
        return sp.Matrix([[1]])
    if n == 2:
        return sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2)],
                          [sp.Rational(1, 2), sp.Rational(1, 2)]])
    q = sp.zeros(n)
    for x in range(n):
        q[x, x] = sp.Rational(1, 2)
        q[x, (x - 1) % n] += sp.Rational(1, 4)
        q[x, (x + 1) % n] += sp.Rational(1, 4)
    return q


def full_kernel(n):
    size = n * 2 ** n
    p = sp.zeros(size)
    q = cycle_kernel(n)
    for bits in range(2 ** n):
        for x in range(n):
            row = bits * n + x
            for first in (0, 1):
                middle = (bits & ~(1 << x)) | (first << x)
                for y in range(n):
                    if q[x, y] == 0:
                        continue
                    for second in (0, 1):
                        final = (middle & ~(1 << y)) | (second << y)
                        p[row, final * n + y] += q[x, y] / 4
    return p


def main():
    if sys.flags.optimize:
        raise RuntimeError("C341 SymPy lane refuses optimized Python")
    z = sp.symbols("z")
    checks = 0
    d0, d1 = sp.Integer(1), z - sp.Rational(1, 2)
    for ell in range(1, 10):
        if ell == 1:
            recurrence = d1
        else:
            d0, d1 = d1, sp.expand((z - sp.Rational(1, 2)) * d1 - sp.Rational(1, 16) * d0)
            recurrence = d1
        path = sp.diag(*([sp.Rational(1, 2)] * ell))
        for i in range(ell - 1):
            path[i, i + 1] = path[i + 1, i] = sp.Rational(1, 4)
        need(sp.expand(path.charpoly(z).as_expr() - recurrence) == 0, f"path continuant {ell}")
        checks += 1
    for n in range(1, 9):
        q = cycle_kernel(n)
        formula = sp.expand(sp.Rational(1, 2 ** (2 * n - 1))
                            * (sp.chebyshevt(n, 2 * z - 1) - 1))
        need(sp.expand(q.charpoly(z).as_expr() - formula) == 0, f"cycle Chebyshev {n}")
        need(q == q.T and all(sum(q.row(i)) == 1 for i in range(n)), f"cycle stochastic {n}")
        checks += 2
    # Exact full-state kernels and the Walsh trace identities.
    for n in range(1, 6):
        p = full_kernel(n)
        need(p == p.T, f"full symmetry {n}")
        need(all(sum(p.row(i)) == 1 for i in range(p.rows)), f"full stochasticity {n}")
        block_trace = 0
        block_square_trace = 0
        q = cycle_kernel(n)
        for mask in range(2 ** n):
            d = sp.diag(*[0 if mask & (1 << x) else 1 for x in range(n)])
            block = d * q * d
            block_trace += sp.trace(block)
            block_square_trace += sp.trace(block * block)
        need(sp.trace(p) == block_trace, f"Walsh trace {n}")
        need(sp.trace(p * p) == block_square_trace, f"Walsh square trace {n}")
        checks += 4
    # Exact sine identity before any numerical specialization.
    theta = sp.symbols("theta", real=True)
    identity = sp.expand_trig(sp.sin(theta - theta) if False else
                              sp.sin(2 * theta) + sp.sin(0 * theta) - 2 * sp.cos(theta) * sp.sin(theta))
    need(sp.trigsimp(identity) == 0, "sine recurrence identity")
    checks += 1
    print(f"C341 SymPy cross-check: PASS {checks} symbolic/exact checks")


if __name__ == "__main__":
    main()
