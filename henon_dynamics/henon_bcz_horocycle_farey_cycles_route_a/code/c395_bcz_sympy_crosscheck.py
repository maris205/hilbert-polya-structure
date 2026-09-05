#!/usr/bin/env python3
"""Independent exact symbolic identities and explicitly non-certified quadrature."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("c395 symbolic refuses optimized Python")
import json
from pathlib import Path
import mpmath as mp
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
def main():
    x=json.loads((ROOT/"results/c395_bcz_evidence.json").read_text())
    a,b,t,k,q,r=s.symbols("a b t k q r",nonzero=True)
    p=s.Matrix([[a,b],[0,1/a]]);h=s.Matrix([[1,0],[-t,1]]);B=s.Matrix([[0,-1],[1,k]])
    expected=s.Matrix([[b,k*b-a],[0,1/b]])
    assert s.simplify((h*p*B).subs(t,1/(a*b))-expected)==s.zeros(2)
    conjugate=p.inv()*h.subs(t,-t)*p
    assert s.simplify(conjugate-s.Matrix([[1-a*b*t,-b*b*t],[a*a*t,1+a*b*t]]))==s.zeros(2)
    M=s.Matrix([[1-q*r,q*q],[-r*r,1+q*r]]);D=M-s.eye(2)
    assert s.expand(M.det())==1 and s.expand(s.trace(M))==2 and s.simplify(D*D)==s.zeros(2)
    for ell in range(-3,6):assert s.simplify(M**ell-s.eye(2)-ell*D)==s.zeros(2)
    for row in x["layer_rows"]:
        n=row["N"];period=sum(s.totient(j) for j in range(1,n+1))
        assert period==row["least_period"]
        assert sum(s.mobius(d)*(n//d)**2 for d in range(1,n+1))==2*period-1
        assert sum(s.Rational(1,u*v) for u,v in row["cycle"])==1
        assert s.Matrix(row["product_at_start"])==M.subs({q:1,r:n})
    mp.mp.dps=90
    integral=2*mp.quad(lambda y:-mp.log1p(-y)/y,[0,mp.mpf("0.25"),mp.mpf("0.5"),mp.mpf("0.9"),1])
    assert abs(integral-mp.pi**2/3)<mp.mpf("1e-85")
    for row in x["layer_rows"]:
        n=row["N"];err=abs(row["least_period"]-3*n*n/mp.pi**2)
        assert err<=n*(1+mp.log(n))+mp.mpf(n)/2+mp.mpf("0.5")
    print("C395 symbolic PASS: 14 universal matrix identities; 256 exact layer checks; 65 ninety-digit numerical controls (not interval certificates)")
if __name__=="__main__":main()
