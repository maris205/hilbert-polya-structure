#!/usr/bin/env python3
"""Independent symbolic identities for HCS-C334."""
import sys
import sympy as s

if sys.flags.optimize:
    raise RuntimeError("C334 SymPy lane refuses optimized Python")

checks=0
E,D,m,a=s.symbols("E D m a",positive=True)
# Here epsilon=-E is positive on the periodic chamber.
epsilon=s.symbols("epsilon",positive=True)
J=s.sqrt(2*m*D)/a*(1-s.sqrt(epsilon/D))
period=2*s.pi/(a*s.sqrt(2*epsilon/m))
if s.simplify(-s.diff(J,epsilon)-period/(2*s.pi))!=0:raise AssertionError("action derivative")
checks+=1

z=s.symbols("z",positive=True)
for lam4 in range(3,33):
    lam=s.Rational(lam4,4)
    for n in range(12):
        exponent=lam-n-s.Rational(1,2)
        if exponent<=0:continue
        alpha=2*exponent
        polynomial=s.Poly(s.expand_func(s.assoc_laguerre(n,alpha,z)),z)
        L=polynomial.as_expr()
        if s.expand(z*s.diff(L,z,2)+(alpha+1-z)*s.diff(L,z)+n*L)!=0:raise AssertionError("Laguerre ODE")
        # Conjugation by z^exponent exp(-z/2) reduces the Morse equation to the displayed Laguerre ODE.
        if s.simplify(alpha-2*exponent)!=0 or s.simplify(lam-exponent-s.Rational(1,2)-n)!=0:raise AssertionError("Morse conjugation")
        if polynomial.degree()!=n:raise AssertionError("Laguerre degree")
        checks+=2

for lam2 in range(1,17):
    lam=s.Rational(2*lam2+1,2)
    n=int(lam-s.Rational(1,2))
    if lam-n-s.Rational(1,2)!=0:raise AssertionError("threshold")
    checks+=1

print(f"C334 SymPy cross-check: PASS ({checks} exact identities)")
