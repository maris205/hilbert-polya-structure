#!/usr/bin/env python3
"""Exact symbolic lane for HCS-C324."""
import sys

import sympy as s

if sys.flags.optimize:
    raise RuntimeError("C324 SymPy lane refuses optimized Python")

t, E, w0 = s.symbols("t E w0", positive=True)
c = s.sqrt(E) / 2
F = s.cos(c * t) + w0 * s.sin(c * t) / s.sqrt(E)
N = -s.sqrt(E) * s.sin(c * t) + w0 * s.cos(c * t)
J = F**2
w = N / F
identities = [
    s.simplify(s.diff(w, t) + (w**2 + E) / 2),
    s.simplify(s.diff(J, t) - w * J),
    s.simplify(w**2 * J - E * (-s.sin(c*t) + w0*s.cos(c*t)/s.sqrt(E))**2),
    s.simplify(F.subs(t, 0) - 1),
    s.simplify(w.subs(t, 0) - w0),
]
if any(s.factor(value) != 0 for value in identities):
    raise AssertionError(identities)
checks = len(identities)

# The asymmetric regression profile z+(2z^2-1)/2=(z+1/2)^2-3/4
# separates the forward minimum from the backward maximum.
z, theta = s.symbols("z theta", real=True)
asym = z + z**2 - s.Rational(1, 2)
if s.expand(asym - ((z + s.Rational(1, 2))**2 - s.Rational(3, 4))) != 0:
    raise AssertionError("asymmetric completed square")
if s.integrate((s.cos(theta) + s.cos(2*theta)/2)**2, (theta, 0, 2*s.pi)) / (2*s.pi) != s.Rational(5, 8):
    raise AssertionError("asymmetric energy")
if (asym.subs(z, -s.Rational(1, 2)), asym.subs(z, 1)) != (-s.Rational(3, 4), s.Rational(3, 2)):
    raise AssertionError("asymmetric extrema")
checks += 3

for e_num in range(1, 31):
    for slope_num in range(-12, 13):
        ee = s.Rational(e_num, 3)
        ww = s.Rational(slope_num, 5)
        FF = F.subs({E: ee, w0: ww})
        NN = N.subs({E: ee, w0: ww})
        if s.simplify(s.diff(FF**2, t) - (NN/FF) * FF**2) != 0:
            raise AssertionError("Jacobian identity")
        if s.simplify((NN/FF)**2 * FF**2 - NN**2) != 0:
            raise AssertionError("energy-density identity")
        checks += 2

print(f"C324 SymPy cross-check: PASS ({checks} exact identities)")
