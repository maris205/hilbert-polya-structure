#!/usr/bin/env python3
"""Exact symbolic cross-checks for HCS-C331."""
import sys

import sympy as s

if sys.flags.optimize:
    raise RuntimeError("C331 SymPy lane refuses optimized Python")

checks = 0
speed, charge = s.symbols("speed charge", real=True)
w2 = speed**2 + charge**2
for cosine, sine in ((1,0),(0,1),(-1,0),(0,-1),(1,0)):
    c, ss = s.Integer(cosine), s.Integer(sine)
    x = speed*ss/s.sqrt(w2)
    y = speed*charge*(1-c)/w2
    z = c+charge**2*(1-c)/w2
    if s.simplify(x*x+y*y+z*z-1) != 0:
        raise AssertionError("Rodrigues sphere identity")
    if s.simplify((speed*y+charge*z)/s.sqrt(w2)-charge/s.sqrt(w2)) != 0:
        raise AssertionError("Poincare plane identity")
    checks += 2

n, q = s.symbols("n q", integer=True, nonnegative=True)
ell = n+q/s.Integer(2)
if s.expand(ell*(ell+1)-q*q/4 - (n*(n+q+1)+q/2)) != 0:
    raise AssertionError("Casimir spectrum simplification")
if s.expand(2*ell+1-(2*n+q+1)) != 0:
    raise AssertionError("multiplicity simplification")
checks += 2

for qq in range(-20,21):
    aq = abs(qq)
    for nn in range(21):
        ell_value = s.Rational(aq,2)+nn
        casimir = s.simplify(ell_value*(ell_value+1)-s.Rational(qq*qq,4))
        closed = s.Rational(nn*(nn+aq+1),1)+s.Rational(aq,2)
        if casimir != closed or 2*ell_value+1 != 2*nn+aq+1:
            raise AssertionError("integer monopole spectrum")
        if closed.subs({}) < 0:
            raise AssertionError("positivity")
        checks += 3

for qq in range(13):
    lowest = s.Rational(qq,2)
    if lowest != s.Rational(abs(qq),2) or 2*(s.Rational(qq,2))+1 != qq+1:
        raise AssertionError("lowest level")
    checks += 2

print(f"C331 SymPy cross-check: PASS ({checks} exact identities)")
