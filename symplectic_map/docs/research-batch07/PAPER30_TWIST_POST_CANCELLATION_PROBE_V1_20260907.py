#!/usr/bin/env python3
"""Exact full-Fourier post-cancellation coefficients; prints JSON only.

Uses SUM action, positive kick, fixed lambda. No floating-point root scans.
"""
import json
import sympy as sp

LAM = sp.Symbol("lambda", real=True)


def add(*items):
    out = {}
    for item in items:
        for mode, value in item.items():
            out[mode] = out.get(mode, 0) + value
    return {m: sp.expand(c) for m, c in out.items() if sp.expand(c) != 0}


def scale(item, factor):
    return {m: sp.expand(factor * c) for m, c in item.items() if factor * c != 0}


def shift(item, delta):
    return {m + delta: c for m, c in item.items()}


def multiply(left, right):
    out = {}
    for a, x in left.items():
        for b, y in right.items():
            out[a + b] = out.get(a + b, 0) + x * y
    return {m: sp.expand(c) for m, c in out.items() if sp.expand(c) != 0}


def compute(s, denominators, order):
    """v=i*u; dictionaries retain BOTH positive and negative phase modes."""
    v = {0: {}}
    exponential = {alpha: {0: {0: sp.Integer(1)}} for alpha in (1, -1, 2, -2)}
    force = {}
    for n in range(1, order + 1):
        force[n] = add(
            scale(shift(exponential[1][n - 1], 1), sp.Rational(1, 2)),
            scale(shift(exponential[-1][n - 1], -1), -sp.Rational(1, 2)),
            scale(shift(exponential[2].get(n - 2, {}), 2), LAM),
            scale(shift(exponential[-2].get(n - 2, {}), -2), -LAM),
        )
        if n == order:
            break
        v[n] = {
            m: sp.expand(-value / denominators[m % s])
            for m, value in force[n].items()
            if m % s != 0
        }
        assert all(sp.expand(value + v[n].get(-m, 0)) == 0 for m, value in v[n].items())
        assert all(abs(m) <= n and (m - n) % 2 == 0 and m % s != 0 for m in v[n])
        for alpha in exponential:
            exponential[alpha][n] = scale(
                add(*(scale(multiply(v[k], exponential[alpha][n - k]), alpha * k)
                      for k in range(1, n + 1))),
                sp.Rational(1, n),
            )

    cosine = {}
    action_checks = []
    for n in range(1, order + 1):
        for mode in range(s, n + 1, s):
            value = sp.expand(-sp.Rational(2 * s, mode) * force[n].get(mode, 0))
            cosine[(n, mode)] = value
            # Independent evaluation of SUM action on the truncated full solution.
            # For resonant mode m, (zeta^a-1)(zeta^(m-a)-1)=D_a.
            kinetic = 0
            for k in range(1, n):
                for a, vk in v[k].items():
                    kinetic -= sp.Rational(1, 2) * denominators[a % s] * vk * v[n - k].get(mode - a, 0)
            potential = (
                -sp.Rational(1, 2) * exponential[1][n - 1].get(mode - 1, 0)
                -sp.Rational(1, 2) * exponential[-1][n - 1].get(mode + 1, 0)
                -LAM / 2 * exponential[2].get(n - 2, {}).get(mode - 2, 0)
                -LAM / 2 * exponential[-2].get(n - 2, {}).get(mode + 2, 0)
            )
            difference = sp.expand(2 * s * (kinetic + potential) - value)
            assert difference == 0, (s, n, mode, difference)
            action_checks.append([n, mode, str(difference)])
    return v, cosine, action_checks


def serialize_v(v):
    return {str(n): {str(m): str(c) for m, c in sorted(row.items())} for n, row in v.items() if n > 0}


def main():
    results = {}
    for s, Ds in ((3, {1: sp.Integer(3), 2: sp.Integer(3)}),
                  (4, {1: sp.Integer(2), 2: sp.Integer(4), 3: sp.Integer(2)})):
        v, coefficients, checks = compute(s, Ds, s + 2)
        C = coefficients[(s, s)]
        Q = coefficients[(s + 2, s)]
        roots = sp.solve(C, LAM)
        results[str(s)] = {
            "C": str(sp.factor(C)),
            "Q": str(sp.factor(Q)),
            "roots_C": [str(r) for r in roots],
            "Q_at_roots": [str(sp.simplify(Q.subs(LAM, r))) for r in roots],
            "gcd_C_Q": str(sp.gcd(C, Q)),
            "Q_mod_C": str(sp.rem(Q, C, LAM)),
            "resultant_C_Q": str(sp.resultant(C, Q, LAM)),
            "full_v": serialize_v(v),
            "cosine_coefficients": {f"{n},{m}": str(c) for (n, m), c in coefficients.items()},
            "SUM_action_minus_force_coefficients": checks,
        }
    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
