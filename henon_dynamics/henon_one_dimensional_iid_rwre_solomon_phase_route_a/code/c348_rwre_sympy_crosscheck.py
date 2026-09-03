#!/usr/bin/env python3
"""Independent symbolic cross-checks for HCS-C348."""
from __future__ import annotations

import sys

import sympy as sp


def need(condition, label):
    if condition is not True and condition != sp.S.true:
        raise AssertionError(label)


def main():
    if sys.flags.optimize:
        raise RuntimeError("C348 SymPy lane refuses optimized Python")
    checks = 0
    p, r = sp.symbols("p r", positive=True)
    need(sp.factor((1 - (1 - p) / p) / (1 + (1 - p) / p) - (2 * p - 1)) == 0,
         "homogeneous speed")
    checks += 1
    alpha, beta = sp.symbols("alpha beta", positive=True)
    mean_rho = beta / (alpha - 1)
    mean_inverse = alpha / (beta - 1)
    need(sp.factor((1 - mean_rho) / (1 + mean_rho)
                   - (alpha - beta - 1) / (alpha + beta - 1)) == 0,
         "Beta right speed")
    need(sp.factor(-(1 - mean_inverse) / (1 + mean_inverse)
                   + (beta - alpha - 1) / (alpha + beta - 1)) == 0,
         "Beta left speed")
    checks += 2
    for a in range(2, 7):
        for b in range(2, 7):
            beta_mean = sp.beta(a - 1, b + 1) / sp.beta(a, b)
            inverse_mean = sp.beta(a + 1, b - 1) / sp.beta(a, b)
            need(sp.simplify(beta_mean.rewrite(sp.gamma) - sp.Rational(b, a - 1)) == 0,
                 f"Beta rho moment {a},{b}")
            need(sp.simplify(inverse_mean.rewrite(sp.gamma) - sp.Rational(a, b - 1)) == 0,
                 f"Beta inverse moment {a},{b}")
            checks += 2
    # The scale weights solve omega_i Delta_{i+1}=(1-omega_i)Delta_i.
    w1, w2, w3 = sp.symbols("w1 w2 w3", positive=True)
    omegas = [w1, w2, w3]
    scales = [sp.Integer(1)]
    for omega in omegas:
        scales.append(sp.cancel(scales[-1] * (1 - omega) / omega))
    total = sp.cancel(sum(scales))
    h = [sp.Integer(0)]
    for x in range(1, 4):
        h.append(sp.cancel(sum(scales[:x]) / total))
    h.append(sp.Integer(1))
    for i, omega in enumerate(omegas, start=1):
        need(sp.cancel(h[i] - omega * h[i + 1] - (1 - omega) * h[i - 1]) == 0,
             f"harmonic equation {i}")
        checks += 1
    # Crossing-time series and its reciprocal velocity.
    partial = 1 + 2 * sum(r ** k for k in range(1, 9))
    closed = (1 + r) / (1 - r)
    need(sp.cancel(partial - closed + 2 * r ** 9 / (1 - r)) == 0,
         "crossing geometric tail")
    need(sp.factor(1 / closed - (1 - r) / (1 + r)) == 0, "crossing reciprocal")
    checks += 2
    # Integer digamma differences reduce to exact harmonic-number differences.
    for a in range(1, 9):
        for b in range(1, 9):
            left = sp.digamma(b) - sp.digamma(a)
            right = sp.harmonic(b - 1) - sp.harmonic(a - 1)
            need(sp.simplify(left - right) == 0, f"digamma {a},{b}")
            checks += 1
    print(f"C348 SymPy cross-check: PASS {checks} symbolic/exact checks")


if __name__ == "__main__":
    main()
