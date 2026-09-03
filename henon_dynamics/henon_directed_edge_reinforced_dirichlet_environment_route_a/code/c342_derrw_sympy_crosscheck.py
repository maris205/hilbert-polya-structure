#!/usr/bin/env python3
"""Independent SymPy cross-check for HCS-C342."""
from __future__ import annotations

import sys

import sympy as sp


def need(condition, label):
    if condition is not True and condition != sp.S.true:
        raise AssertionError(label)


def stationary(kernel):
    n = kernel.rows
    symbols = sp.symbols(f"p0:{n}")
    equations = [sum(symbols[i] * kernel[i, j] for i in range(n)) - symbols[j]
                 for j in range(n - 1)]
    equations.append(sum(symbols) - 1)
    solution = sp.solve(equations, symbols, dict=True)
    need(len(solution) == 1, "unique stationary solve")
    return sp.Matrix([[solution[0][symbol] for symbol in symbols]])


def main():
    if sys.flags.optimize:
        raise RuntimeError("C342 SymPy lane refuses optimized Python")
    a, b, c = sp.symbols("a b c", positive=True)
    checks = 0
    for left in range(5):
        for right in range(5):
            beta_ratio = (sp.gamma(a + b) / sp.gamma(a + b + left + right)
                          * sp.gamma(a + left) / sp.gamma(a)
                          * sp.gamma(b + right) / sp.gamma(b))
            rising_ratio = sp.rf(a, left) * sp.rf(b, right) / sp.rf(a + b, left + right)
            need(sp.simplify(beta_ratio - rising_ratio) == 0, f"beta ratio {left},{right}")
            checks += 1
    need(sp.simplify(a / (a + b) + b / (a + b) - 1) == 0, "prior prediction")
    need(sp.simplify((a + 3) / (a + b + 5) + (b + 2) / (a + b + 5) - 1) == 0,
         "posterior prediction")
    mean_a = a / (a + b)
    second_a = a * (a + 1) / ((a + b) * (a + b + 1))
    need(sp.factor(second_a - mean_a ** 2
                   - a * b / ((a + b) ** 2 * (a + b + 1))) == 0, "variance")
    mixed = a * b / ((a + b) * (a + b + 1))
    need(sp.factor(mixed - mean_a * b / (a + b)
                   + a * b / ((a + b) ** 2 * (a + b + 1))) == 0, "covariance")
    checks += 4
    # A concrete interleaved path: local factors regroup despite endogenous row visits.
    sequential = (a / (a + b)) * (c / (c + 1)) * ((b) / (a + b + 1))
    grouped = (a * b / ((a + b) * (a + b + 1))) * (c / (c + 1))
    need(sp.cancel(sequential - grouped) == 0, "interleaved regrouping")
    checks += 1
    kernels = [
        sp.Matrix([[sp.Rational(1, 3), sp.Rational(2, 3)],
                   [sp.Rational(3, 4), sp.Rational(1, 4)]]),
        sp.Matrix([[0, sp.Rational(3, 4), sp.Rational(1, 4)],
                   [sp.Rational(2, 3), 0, sp.Rational(1, 3)],
                   [sp.Rational(1, 3), sp.Rational(2, 3), 0]]),
        sp.Matrix([[1]]),
    ]
    for index, kernel in enumerate(kernels):
        pi = stationary(kernel)
        need(pi * kernel == pi and sum(pi) == 1, f"stationarity {index}")
        need(all(value > 0 for value in pi), f"positive stationary {index}")
        checks += 2
    # Parallel arcs remain separate coordinates even when the vertex kernel sums them.
    x, y, z = sp.symbols("x y z", positive=True)
    need(sp.simplify(x / (x + y + z) + y / (x + y + z)
                     - (x + y) / (x + y + z)) == 0, "parallel aggregation")
    checks += 1
    print(f"C342 SymPy cross-check: PASS {checks} symbolic/exact checks")


if __name__ == "__main__":
    main()
