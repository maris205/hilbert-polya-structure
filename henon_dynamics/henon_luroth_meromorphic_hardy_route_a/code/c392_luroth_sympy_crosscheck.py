#!/usr/bin/env python3
"""Separate symbolic backend and declared finite precision audit."""
if not __debug__:
    raise RuntimeError("c392 symbolic refuses optimized Python")
import json
from pathlib import Path
import sympy as S
import mpmath as mp
ROOT=Path(__file__).resolve().parents[1]
d=json.loads((ROOT/"results/c392_luroth_evidence.json").read_text())
t,z=S.symbols("t z");count=0
h=(t+(z-S.Rational(1,2))*t*t)/(1-t*t/4)
for l in range(8):
    s=S.Rational(1-l,2)
    for j in range(l+1):
        v=S.expand(S.series((1-t*t/4)**(-s)*h**j,t,0,l+1).removeO()).coeff(t,l)/2
        for i in range(l+1):
            assert S.expand(v).coeff(z,i)==S.Rational(*d["residues"][l]["matrix"][i][j]);count+=1
for row in d["matrices"]:
    M=S.Matrix([[S.Rational(*v) for v in r] for r in row["matrix"]])
    u=S.symbols("u")
    assert S.expand((S.eye(7)-u*M).det()-S.prod(1-u*S.Rational(*v) for v in row["diagonal"]))==0
    count+=1
mp.mp.dps=100
def A_center(s,N=160):
    coeff=mp.mpc(1);out=mp.mpc(0)
    for r in range(N):
        if r:coeff*= (s+r-1)/(4*r)
        out+=coeff*mp.zeta(2*s+2*r,mp.mpf("1.5"))
    return out
def A_uncentered(s,N=400):
    coeff=mp.mpc(1);out=mp.mpc(0)
    for r in range(N):
        if r:coeff*=(s+r-1)/r
        out+=coeff*mp.zeta(2*s+r,2)
    return out
points=[mp.mpf(2),mp.mpf(3),mp.mpf(3)/4+mp.j/3,-mp.mpf(1)/4+mp.j/5,-mp.mpf(3)/4+mp.j/7,-mp.mpf(1)/3]
for s in points:
    assert abs(A_center(s)-A_uncentered(s))<mp.mpf("1e-80")
assert abs(A_center(mp.mpf(1))-1)<mp.mpf("1e-80")
# At s=1, direct branch prefix versus exact telescoping tail.
for N in (1,2,10,100):
    value=mp.fsum(mp.mpf(1)/(n*(n+1)) for n in range(1,N+1))
    assert abs(value+mp.mpf(1)/(N+1)-1)<mp.mpf("1e-90")
# Complex phase, no absolute-value replacement in eigenvalues.
for s in points[2:5]:
    assert abs(mp.im(A_center(s)))>mp.mpf("1e-8")
print(f"C392 symbolic/high-precision PASS: {count} exact identities; 6 dual Hurwitz values, 1 s=1 value, 4 telescoping, 3 phase controls; working_digits=100 agreement=1e-80")
