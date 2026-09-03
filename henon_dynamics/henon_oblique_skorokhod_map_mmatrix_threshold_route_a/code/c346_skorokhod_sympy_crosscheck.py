#!/usr/bin/env python3
"""Separate exact symbolic lane for HCS-C346."""
import sys
from itertools import product

import sympy as s

if sys.flags.optimize:
    raise RuntimeError("C346 SymPy lane refuses optimized Python")

rho, sigma, a, b, u, v = s.symbols("rho sigma a b u v", positive=True)
R = s.Matrix([[1, -rho], [-sigma, 1]])
checks = 0
if s.factor(R.det()) != 1 - rho * sigma:
    raise AssertionError("determinant")
checks += 1
inverse = s.simplify(R.inv())
expected = s.Matrix([[1, rho], [sigma, 1]]) / (1 - rho * sigma)
for entry in inverse - expected:
    if s.simplify(entry) != 0:
        raise AssertionError("inverse")
    checks += 1

# Both-active jump formula and weighted contraction coefficients.
z = s.Matrix([u, v])
d = s.simplify(-inverse * z)
for entry in R * d + z:
    if s.simplify(entry) != 0:
        raise AssertionError("corner LCP")
    checks += 1
if s.simplify((a**2) * b / a - a * b) != 0 or s.simplify((b**2) * a / b - a * b) != 0:
    raise AssertionError("weighted contraction")
checks += 2


def candidates(z1, z2, r, q):
    det = 1 - r * q
    trials = [(s.Rational(0), s.Rational(0)), (-z1, s.Rational(0)), (s.Rational(0), -z2)]
    if det != 0:
        trials.append(((-z1-r*z2)/det, (-q*z1-z2)/det))
    out = set()
    for d1, d2 in trials:
        w1, w2 = z1+d1-r*d2, z2-q*d1+d2
        if d1 >= 0 and d2 >= 0 and w1 >= 0 and w2 >= 0 and d1*w1 == 0 and d2*w2 == 0:
            out.add((s.factor(d1), s.factor(d2)))
    return out


# Exhaust the four rational coupling chambers and a square of incoming states.
couplings = [(s.Rational(0), s.Rational(0)), (s.Rational(0), s.Rational(3, 2)),
             (s.Rational(2), s.Rational(0)), (s.Rational(1, 4), s.Rational(1, 4)),
             (s.Rational(4, 9), s.Rational(1, 4)), (s.Rational(9, 16), s.Rational(1, 9))]
for r, q in couplings:
    if r*q >= 1:
        raise AssertionError("bad fixture")
    for z1, z2 in product(range(-5, 6), repeat=2):
        answer = candidates(s.Rational(z1), s.Rational(z2), r, q)
        if len(answer) != 1:
            raise AssertionError((r, q, z1, z2, answer))
        d1, d2 = next(iter(answer))
        w1, w2 = z1+d1-r*d2, z2-q*d1+d2
        if min(d1, d2, w1, w2) < 0 or d1*w1 or d2*w2:
            raise AssertionError("complementarity")
        checks += 7

# Sharp-wall controls: null direction at product one and negative-jump failure.
for h in range(0, 11):
    y = s.Matrix([h, h])
    if s.Matrix([[1, -1], [-1, 1]]) * y != s.zeros(2, 1):
        raise AssertionError("critical null cone")
    checks += 2
for r, q in ((s.Rational(1), s.Rational(1)), (s.Rational(2), s.Rational(1)), (s.Rational(1, 2), s.Rational(3))):
    if candidates(s.Rational(-1), s.Rational(-1), r, q):
        raise AssertionError("negative jump unexpectedly solvable")
    checks += 4

print(f"C346 SymPy cross-check: PASS ({checks} exact identities)")
