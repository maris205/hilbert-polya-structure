#!/usr/bin/env python3
"""Disjoint symbolic identities for HCS-C321."""
import sys
import sympy as sp


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C321 SymPy lane refuses optimized Python")
    d = sp.symbols("d", positive=True, integer=True)
    checks = 0
    for r in range(1, 13):
        before = sp.rf(d, r)
        if sp.expand(sp.rf(d + 1, r) - before - sp.Rational(r, 1) * before / d) != 0:
            raise AssertionError("rising difference")
        checks += 1
        n, s = sp.symbols("n s", positive=True, integer=True)
        formula_n = sp.factorial(r) * sp.gamma(n - 1 + sp.Rational(r, 2)) * sp.gamma(s - 1) / (
            sp.gamma(n - 1) * sp.gamma(s - 1 + sp.Rational(r, 2)))
        ratio = sp.simplify(sp.expand_func(formula_n.subs(n, n + 1) / formula_n))
        if sp.simplify(ratio - (1 + sp.Rational(r, 2) / (n - 1))) != 0:
            raise AssertionError("gamma recurrence")
        checks += 1
    k = sp.symbols("k", positive=True, integer=True)
    pk = 4 / (k * (k + 1) * (k + 2))
    pprev = 4 / ((k - 1) * k * (k + 1))
    if sp.simplify(pk - ((k - 1) * pprev) / (k + 2)) != 0:
        raise AssertionError("profile recurrence")
    checks += 1
    K = sp.symbols("K", positive=True, integer=True)
    if sp.simplify(sp.summation(4 / (k * (k + 1) * (k + 2)), (k, 1, K)) - (1 - 2 / ((K + 1) * (K + 2)))) != 0:
        raise AssertionError("profile mass")
    if sp.simplify(sp.summation(4 / ((k + 1) * (k + 2)), (k, 1, K)) - (2 - 4 / (K + 2))) != 0:
        raise AssertionError("profile degree")
    checks += 2
    x = sp.symbols("x")
    for r in range(2, 13):
        if sp.degree(sp.expand(sp.rf(x, r) - x ** r), x) > r - 1:
            raise AssertionError("lower-order comparison")
        checks += 1
    print(f"C321 SymPy cross-check: PASS ({checks} identities)")


if __name__ == "__main__":
    main()
