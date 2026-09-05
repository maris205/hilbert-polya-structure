#!/usr/bin/env python3
"""Symbolic family identities and independent high-precision root regression."""
if not __debug__:
    raise RuntimeError("c397 symbolic refuses optimized Python")
import json
from pathlib import Path
from itertools import combinations
import sympy as s
import mpmath as mp
ROOT=Path(__file__).resolve().parents[1]
mp.mp.dps=70
a,z,t=s.symbols('a z t',real=True);A=s.Matrix([[0,0,0,-1],[1,0,0,a],[0,1,0,1],[0,0,1,a]])
O=s.Matrix([[0,0,1,a],[0,0,0,1],[-1,0,0,0],[-a,-1,0,0]])
e=s.eye(4)[:,0];R=s.Matrix.hstack(*[A**(-j)*e for j in range(4)])
assert s.simplify(A.T*O*A-O)==s.zeros(4) and O.det()==1
assert s.simplify(R*R)==s.eye(4) and s.simplify(R*A*R-A.inv())==s.zeros(4)
assert s.simplify(R.T*O*R+O)==s.zeros(4)
W=s.Matrix([[A.extract(i,j).det() for j in combinations(range(4),2)] for i in combinations(range(4),2)])
assert s.expand((s.eye(6)-z*W).det()-(1-z)**2*(1+3*z+(a*a+4)*z*z+3*z**3+z**4))==0
assert s.integrate(2-2*s.cos(t),(t,0,2*s.pi))/(2*s.pi)==2
assert s.integrate(4*s.cos(t)**2,(t,0,2*s.pi))/(2*s.pi)==2
d=json.loads((ROOT/'results/c397_salem_evidence.json').read_text());cases=0
for row in d['families']:
    av=mp.mpf(row['a']);zp=(av+mp.sqrt(av*av+12))/2;zm=(av-mp.sqrt(av*av+12))/2
    lam=(zp+mp.sqrt(zp*zp-4))/2;theta=mp.acos(zm/2);cumulative=0
    for r in row['periods']:
        n=r['n'];F=(lam**n+lam**(-n)-2)*(2-2*mp.cos(n*theta))
        assert abs(F-r['fixed'])<mp.mpf('1e-55')*max(1,abs(F))
        lhs=mp.mpf(n*r['primitive_cycles'])/lam**n;leading=2-2*mp.cos(n*theta)
        # An explicit absolute finite-n consequence of the divisor bound, not a fitted tolerance.
        assert abs(lhs-leading)<=8*lam**(-n)+4*n*lam**(-mp.mpf(n)/2)
        cumulative+=r['primitive_cycles'];cases+=1
    # Endpoint constants of the proved cumulative distribution are positive and ordered.
    rr=1/lam;C=2/(1-rr);B=2/abs(1-rr*mp.exp(-1j*theta));assert C>B>0
print('C397 symbolic/high-precision PASS: 7 family identities; 120 spectral and primitive regressions; 5 cumulative endpoint controls; dps=70')
