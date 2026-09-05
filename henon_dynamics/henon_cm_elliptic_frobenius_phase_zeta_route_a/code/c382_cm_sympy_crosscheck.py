#!/usr/bin/env python3
"""Symbolic finite-field zeta, reciprocal, phase and torsion identities."""
import json
from pathlib import Path
import sys
import sympy as s

if sys.flags.optimize:
    raise RuntimeError('C382 SymPy refuses optimized Python')
root=Path(__file__).resolve().parents[1]
u,p,t=s.symbols('u p t', nonzero=True)
Z=(1-t*u+p*u*u)/((1-u)*(1-p*u))
checks=0
def zero(expr):
    global checks
    checks+=1
    if s.cancel(expr)!=0:
        raise ValueError(str(expr))
zero(Z-Z.subs(u,1/(p*u)))
M=s.Matrix([[0,-p],[1,t]])
zero((s.eye(2)-u*M).det()-(1-t*u+p*u*u))
zero(s.trace(M*M)-(t*t-2*p))
zero(s.trace(M**3)-(t**3-3*p*t))
j=s.I
zero((j-1)**2-(j**3-j))
zero((j+1)**2-2*j)
zero((j+1)*j-(j-1))
data=json.loads((root/'results/c382_cm_evidence.json').read_text())
for r in data['prime_ledger']:
    q,tt=r['p'],r['trace']
    poly=s.Poly(1-tt*u+q*u*u,u)
    if s.discriminant(poly.as_expr(),u)>=0:
        raise ValueError('source roots must be nonreal and distinct')
    checks+=1
    if r['primary_upper_pair'] is not None:
        a,b=r['primary_upper_pair']
        zero((1-(a+s.I*b)*u)*(1-(a-s.I*b)*u)-poly.as_expr())
    else:
        zero((1-s.I*s.sqrt(q)*u)*(1+s.I*s.sqrt(q)*u)-poly.as_expr())
    zero(Z.subs({p:q,t:tt})-Z.subs({p:q,t:tt,u:1/(q*u)},simultaneous=True))
print('C382 SymPy cross-check: PASS (%d exact checks)'%checks)
