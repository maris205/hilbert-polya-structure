#!/usr/bin/env python3
"""Independent symbolic lane for HCS-C367."""
from __future__ import annotations
import sys
import sympy as s

def main():
    if sys.flags.optimize: raise RuntimeError('C367 SymPy lane refuses optimized Python')
    a,b,c,d,x=s.symbols('a b c d x',positive=True); k=s.symbols('k',positive=True); checks=0
    kexpr=(b*d-a*c)/(c*d); atom=c*k/(a+b)
    q0=a*c*k/((a+b)*d); q1=a*k/(a+b)
    f0=q0*s.exp(-k*x); f1=q1*s.exp(-k*x)
    assert s.simplify(c*f1-d*f0)==0; checks+=1
    assert s.simplify((d*s.diff(f0,x)-a*f0+b*f1).subs(k,kexpr))==0; checks+=1
    assert s.simplify((-c*s.diff(f1,x)+a*f0-b*f1).subs(k,kexpr))==0; checks+=1
    assert s.simplify(a*atom-d*f0.subs(x,0))==0; checks+=1
    int0=s.integrate(f0,(x,0,s.oo)); int1=s.integrate(f1,(x,0,s.oo))
    assert s.simplify((atom+int0-b/(a+b)).subs(k,kexpr))==0; checks+=1
    assert s.simplify((int1-a/(a+b)).subs(k,kexpr))==0; checks+=1
    assert s.simplify((atom+int0+int1-1).subs(k,kexpr))==0; checks+=1
    pplus=a*(c+d)/((a+b)*d)
    assert s.simplify((int0+int1-pplus).subs(k,kexpr))==0; checks+=1
    assert s.simplify((d*atom-(b*d-a*c)/(a+b)).subs(k,kexpr))==0; checks+=1
    assert s.simplify((c/b-d/a)/(1/b+1/a)-(a*c-b*d)/(a+b))==0; checks+=1
    for n in range(1,9):
        m0=s.integrate(x**n*f0,(x,0,s.oo)); m1=s.integrate(x**n*f1,(x,0,s.oo))
        assert s.simplify((m0+m1-pplus*s.factorial(n)/k**n).subs(k,kexpr))==0; checks+=1
        assert s.simplify(m0-q0*s.factorial(n)/k**(n+1))==0; checks+=1
        assert s.simplify(m1-q1*s.factorial(n)/k**(n+1))==0; checks+=1
    # Stable wall is exactly positivity of k and atom on the positive core.
    w=s.symbols('w',positive=True)
    assert s.simplify(kexpr.subs(b*d,a*c+w)-w/(c*d))==0; checks+=1
    assert s.simplify((atom.subs(k,kexpr)).subs(b*d,a*c+w)-w/((a+b)*d))==0; checks+=1
    print(f'C367 SymPy cross-check: PASS ({checks} exact checks)')
if __name__=='__main__': main()
