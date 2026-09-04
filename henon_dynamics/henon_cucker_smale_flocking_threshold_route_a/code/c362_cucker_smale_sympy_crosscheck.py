#!/usr/bin/env python3
"""Independent symbolic lane for the C362 theorem."""
from __future__ import annotations
import sys
import sympy as s

def main():
    if sys.flags.optimize: raise RuntimeError('C362 SymPy lane refuses optimized Python')
    r=s.symbols('r',nonnegative=True); checks=0
    primitives=[(0,r),(s.Rational(1,2),s.asinh(r)),(1,s.atan(r)),(s.Rational(3,2),r/s.sqrt(1+r*r)),(2,s.atan(r)/2+r/(2*(1+r*r)))]
    for beta,p in primitives:
        assert s.simplify(s.diff(p,r)-(1+r*r)**(-beta))==0; checks+=1
    assert s.limit(s.asinh(r),r,s.oo)==s.oo; checks+=1
    assert s.limit(s.atan(r),r,s.oo)==s.pi/2; checks+=1
    assert s.limit(r/s.sqrt(1+r*r),r,s.oo)==1; checks+=1
    assert s.limit(primitives[-1][1],r,s.oo)==s.pi/4; checks+=1
    R=s.symbols('R',positive=True)
    assert s.solve(s.Eq(R/s.sqrt(1+R**2),s.Rational(1,2)),R)==[s.sqrt(3)/3]; checks+=1
    tail=1-r/s.sqrt(1+r*r)
    assert s.limit(tail,r,s.oo)==0 and s.simplify(s.diff(tail,r)+(1+r*r)**s.Rational(-3,2))==0; checks+=2
    # N=2 normalized coupling: the two K/2 accelerations subtract to -K psi u.
    K,psi,u=s.symbols('K psi u',positive=True)
    # With r=x_2-x_1 and u=v_2-v_1, a_1=+K psi u/2 and a_2=-K psi u/2.
    a1=K*psi*u/2; a2=-K*psi*u/2
    assert s.simplify(a2-a1+K*psi*u)==0; checks+=1
    # Ordered-pair normalization for two agents and mean-zero velocities.
    energy=s.diff(((u/2)**2+(-u/2)**2)/2,u)*(-K*psi*u)
    rhs=-K/s.Integer(4)*(psi*u**2+psi*u**2)
    assert s.simplify(energy-rhs)==0; checks+=1
    q=s.symbols('q',positive=True)
    assert s.limit(s.Rational(3,2)-r/s.sqrt(1+r*r),r,s.oo)==s.Rational(1,2); checks+=1
    assert s.integrate((1+q*q)**s.Rational(-3,2),(q,0,s.oo))==1; checks+=1
    print(f'C362 SymPy cross-check: PASS ({checks} exact checks)')
if __name__=='__main__': main()
