#!/usr/bin/env python3
"""Independent symbolic identities for the Katok navigation receipts."""
from __future__ import annotations

import math
import sys

import sympy as sp


def require_zero(value, label):
    if sp.simplify(value) != 0:
        raise AssertionError(f"nonzero symbolic residual {label}: {value}")


def main():
    if sys.flags.optimize:
        raise RuntimeError("C339 SymPy lane refuses optimized Python")
    checks = 0
    z, t = sp.symbols("z t", real=True)
    rotation = sp.Matrix([[sp.cos(t), sp.sin(t)], [-sp.sin(t), sp.cos(t)]])
    require_zero(rotation.det() - 1, "symplectic determinant"); checks += 1
    characteristic = sp.expand((z * sp.eye(2) - rotation).det())
    require_zero(characteristic - (z**2 - 2 * sp.cos(t) * z + 1), "characteristic polynomial"); checks += 1
    det_i_minus = sp.simplify((sp.eye(2) - rotation).det())
    require_zero(det_i_minus - (2 - 2 * sp.cos(t)), "Poincare determinant"); checks += 1
    require_zero(det_i_minus - 4 * sp.sin(t / 2)**2, "half-angle determinant"); checks += 1
    for q in range(2, 17):
        for p in range(-q + 1, q):
            if p == 0 or math.gcd(abs(p), q) != 1:
                continue
            epsilon = sp.Rational(p, q)
            plus = sp.Rational(q, q + p)
            minus = sp.Rational(q, q - p)
            require_zero((1 + epsilon) * plus - 1, "positive period"); checks += 1
            require_zero((1 - epsilon) * minus - 1, "negative period"); checks += 1
            require_zero(epsilon * q - p, "rational closure"); checks += 1
            require_zero((1 - epsilon**2) - sp.Rational(q*q-p*p, q*q), "convexity"); checks += 1
    x = sp.symbols("x")
    fixtures = [(8*x**2-1, sp.sqrt(2)/4), (25*x**2-3, sp.sqrt(3)/5),
                (4*x**2+2*x-1, (sp.sqrt(5)-1)/4)]
    for polynomial, root in fixtures:
        require_zero(polynomial.subs(x, root), "irrational fixture"); checks += 1
    print(f"C339 SymPy cross-check: PASS {checks} identities")


if __name__ == "__main__":
    main()
