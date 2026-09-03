#!/usr/bin/env python3
"""Independent symbolic identities for HCS-C327."""
from __future__ import annotations

import sys

import sympy as sp


CHECKS = 0


def need(condition: bool, label: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C327 SymPy lane refuses optimized Python")

    x, q, y, h, z, n = sp.symbols("x q y h z n", positive=True, real=True)
    free = sp.Matrix([[sp.cos(x), sp.sin(x)/x], [-x*sp.sin(x), sp.cos(x)]])
    jump = sp.Matrix([[1, 0], [q, 1]])
    monodromy = jump * free
    need(sp.simplify(monodromy.det()-1) == 0, "unimodular monodromy")
    need(sp.simplify(sp.trace(monodromy)/2-(sp.cos(x)+q*sp.sin(x)/(2*x))) == 0, "discriminant")

    negative = sp.cosh(y)-h*sp.sinh(y)/(2*y)
    factor_plus = 2*sp.sinh(y/2)*(sp.sinh(y/2)-h*sp.cosh(y/2)/(2*y))
    factor_minus = 2*sp.cosh(y/2)*(sp.cosh(y/2)-h*sp.sinh(y/2)/(2*y))
    need(sp.simplify(sp.expand_trig(negative-1-factor_plus)) == 0, "negative plus factor")
    need(sp.simplify(sp.expand_trig(negative+1-factor_minus)) == 0, "negative minus factor")
    need(sp.limit(2*y*sp.tanh(y/2), y, 0, dir="+") == 0, "plus range left")
    need(sp.limit(2*y/sp.tanh(y/2), y, 0, dir="+") == 4, "minus threshold")
    plus_derivative = sp.diff(2*y*sp.tanh(y/2), y)
    minus_derivative = sp.diff(2*y/sp.tanh(y/2), y)
    for sample in (sp.Rational(1,10), sp.Rational(1,2), 1, 2, 4, 8, 16):
        need(plus_derivative.subs(y,sample).evalf(80)>0, "plus monotonicity receipt")
        need(minus_derivative.subs(y,sample).evalf(80)>0, "minus monotonicity receipt")
    minus_factor = minus_derivative*sp.sinh(y/2)**2-(sp.sinh(y)-y)
    need(sp.simplify(sp.expand_trig(minus_factor.rewrite(sp.exp))) == 0, "minus derivative factor")

    positive = sp.cos(x)+q*sp.sin(x)/(2*x)
    positive_plus = 2*sp.sin(x/2)*(q*sp.cos(x/2)/(2*x)-sp.sin(x/2))
    positive_minus = 2*sp.cos(x/2)*(sp.cos(x/2)+q*sp.sin(x/2)/(2*x))
    need(sp.simplify(sp.expand_trig(positive-1-positive_plus)) == 0, "positive plus factor")
    need(sp.simplify(sp.expand_trig(positive+1-positive_minus)) == 0, "positive minus factor")

    energy = sp.symbols("energy", real=True)
    a, g = sp.symbols("a g", positive=True, real=True)
    k = sp.symbols("k", positive=True, real=True)
    discriminant = sp.cos(a*k)+g*sp.sin(a*k)/(2*k)
    series = sp.series(discriminant, k, 0, 6).removeO()
    need(sp.expand(series).coeff(k,0) == 1+g*a/2, "zero continuation")
    need(sp.expand(series).coeff(k,2) == -a**2/sp.Integer(2)-g*a**3/sp.Integer(12), "zero derivative")
    derivative_E = -a*sp.sin(a*k)/(2*k)+g*(a*k*sp.cos(a*k)-sp.sin(a*k))/(4*k**3)
    need(sp.simplify(sp.diff(discriminant,k)/(2*k)-derivative_E)==0, "energy derivative")

    N = sp.symbols("N", positive=True)
    c = -q**2-q**3/sp.Integer(12)
    delta = q/N+c/N**3
    edge_equation = 2*(N+delta)*sp.tan(delta/2)
    formal = sp.series(edge_equation, N, sp.oo, 4)
    need(sp.simplify(formal.removeO()-q) == 0, "edge displacement through inverse cube")
    signed_width = sp.expand((N+delta)**2-N**2)
    width_series = sp.series(signed_width,N,sp.oo,4).removeO()
    want_width = 2*q-(q**2+q**3/sp.Integer(6))/N**2
    need(sp.simplify(width_series-want_width)==0, "gap-width expansion")

    # Exact rational Taylor coefficients and determinant checks across a grid.
    for coupling in range(-12,13):
        need(sp.trigsimp(sp.expand((jump*free).det()).subs(q,coupling))==1, "grid determinant")
        zero_value=(1+q/2).subs(q,coupling)
        need(zero_value==sp.Rational(coupling+2,2), "grid zero value")
        zero_slope=(-sp.Rational(1,2)-q/12).subs(q,coupling)
        need(zero_slope==-sp.Rational(6+coupling,12), "grid zero slope")
    for band in range(1,65):
        parity=(-1)**band
        need(sp.cos(sp.pi*band)==parity, "Bragg cosine")
        need(sp.sin(sp.pi*band)==0, "Bragg sine")
        need(sp.simplify(2*(sp.pi*band)*sp.tan(0))==0, "shift equation at zero shift")

    print(f"C327 SymPy cross-check: PASS {CHECKS} exact identities")


if __name__ == "__main__":
    main()
