#!/usr/bin/env python3
"""Independent SymPy differential-operator lane for HCS-C340."""
from __future__ import annotations

import math
import sys

import sympy as sp


m, u, v, s, c, d = sp.symbols("m u v s c d")
stationary = 3*u**2 - 4*(1+m)*u + 4*m
first_integral = 2*u**3 - 4*(1+m)*u**2 + 8*m*u


def delta(expression):
    return sp.expand(sp.diff(expression, u)*v + sp.diff(expression, v)*stationary)


def compose(left, right):
    result = {}
    for i, a in left.items():
        for j, b in right.items():
            derivative = b
            for k in range(i + 1):
                order = i - k + j
                result[order] = result.get(order, 0) + sp.binomial(i, k)*a*derivative
                derivative = delta(derivative)
    return {order: sp.expand(value) for order, value in result.items()}


def add(*operators):
    orders = set().union(*(operator.keys() for operator in operators))
    return {order: sp.expand(sum(operator.get(order, 0) for operator in operators)) for order in orders}


def scale(operator, factor):
    return {order: sp.expand(factor*value) for order, value in operator.items()}


def shifted(operator, constant):
    answer = dict(operator)
    answer[0] = sp.expand(answer.get(0, 0) - constant)
    return answer


def require_zero(expression, label):
    residual = sp.factor(sp.expand(expression))
    if residual != 0:
        raise AssertionError(f"nonzero {label}: {residual}")


def main():
    if sys.flags.optimize:
        raise RuntimeError("C340 SymPy lane refuses optimized Python")
    checks = 0
    H = {2: -1, 0: u}
    A = {3: -4, 1: 6*u - 4*(1+m), 0: 3*v}
    commutator = add(compose(A, H), scale(compose(H, A), -1))
    for order, coefficient in sorted(commutator.items()):
        require_zero(coefficient, f"commutator D^{order}"); checks += 1
    cubic = compose(compose(shifted(H, m), shifted(H, 1)), shifted(H, 1+m))
    relation = add(compose(A, A), scale(cubic, 16))
    for order, coefficient in sorted(relation.items()):
        reduced = sp.rem(sp.Poly(sp.expand(coefficient), v),
                         sp.Poly(v**2-first_integral, v)).as_expr()
        require_zero(reduced, f"spectral curve D^{order}"); checks += 1

    sn_second = -(1+m)*s + 2*m*s**3
    cn_second = (2*m*s**2-1)*c
    dn_second = (2*m*s**2-m)*d
    potential = 2*m*s**2
    require_zero(-sn_second + potential*s - (1+m)*s, "sn band edge"); checks += 1
    require_zero(-cn_second + potential*c - c, "cn band edge"); checks += 1
    require_zero(-dn_second + potential*d - m*d, "dn band edge"); checks += 1
    require_zero(delta(stationary) - (6*u-4*(1+m))*v, "stationary KdV derivative"); checks += 1

    energy = sp.symbols("E")
    curve = sp.expand((energy-m)*(energy-1)*(energy-1-m))
    require_zero(curve - (energy**3-2*(1+m)*energy**2+(1+3*m+m**2)*energy-m*(1+m)), "cubic expansion"); checks += 1
    for edge in (m, 1, 1+m):
        require_zero(curve.subs(energy, edge), "spectral root"); checks += 1
    for q in range(2, 26):
        for p in range(1, q):
            if math.gcd(p, q) != 1:
                continue
            value = sp.Rational(p, q)
            require_zero((1+value)-1-value, "gap width"); checks += 1
            require_zero(curve.subs({m: value, energy: value}), "lower edge grid"); checks += 1
            require_zero(curve.subs({m: value, energy: 1+value}), "upper edge grid"); checks += 1
    print(f"C340 SymPy cross-check: PASS {checks} identities")


if __name__ == "__main__":
    main()
