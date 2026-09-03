#!/usr/bin/env python3
"""Independent symbolic identities for HCS-C335."""
import math
import sys
import sympy as s

if sys.flags.optimize:
    raise RuntimeError("C335 SymPy lane refuses optimized Python")

checks=0
gamma,kappa,beta,x,u,r=s.symbols("gamma kappa beta x u r",positive=True)
alpha=kappa/gamma
F=s.exp(-u*r*x)*((beta+u*r)/(beta+u))**alpha
lhs=-gamma*r*s.diff(F,r)
rhs=-gamma*x*s.diff(F,x)+kappa*(beta/(beta+u*r)-1)*F
if s.simplify((lhs-rhs)/F)!=0:
    raise AssertionError("backward transform PDE")
checks+=1
for gv,kv,bv in ((s.Integer(1),s.Rational(1,2),s.Integer(2)),(s.Integer(1),s.Integer(1),s.Integer(1)),(s.Integer(2),s.Integer(3),s.Rational(3,2)),(s.Rational(3,2),s.Integer(1),s.Integer(4)),(s.Rational(2,3),s.Rational(5,3),s.Rational(5,2))):
    av=kv/gv
    moments=[s.rf(av,n)/bv**n for n in range(14)]
    for n in range(1,13):
        drift=-n*gv*moments[n]
        jump=kv*sum(s.binomial(n,j)*math.factorial(n-j)/bv**(n-j)*moments[j] for j in range(n))
        if s.simplify(drift+jump)!=0:
            raise AssertionError("stationary moment recursion")
        checks+=1
    for n in range(13):
        diagonal=-n*gv
        if any(diagonal==-j*gv for j in range(n)):
            raise AssertionError("simple triangular diagonal")
        checks+=1
print(f"C335 SymPy cross-check: PASS ({checks} exact identities)")
