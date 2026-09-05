#!/usr/bin/env python3
"""Exact SymPy polynomial, finite determinant, and different identities."""
import json
from pathlib import Path
import sys
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
def main():
    if not __debug__: raise SystemExit('optimized mode forbidden')
    data=json.loads((ROOT/'results/c389_carlitz_evidence.json').read_text())['payload']
    X,T,z=s.symbols('X T z'); checks=0
    def verify(ok):
        nonlocal checks
        checks+=1
        if not ok: raise ValueError('symbolic mismatch '+str(checks))
    def expr(a): return sum(c*T**i for i,c in enumerate(a))
    for row in data['ring_cases']:
        q=row['q']
        for m in row['maps']:
            for n,count in enumerate(m['fixed'],1): verify(count==sum(l*c for l,c in m['cycles'] if n%l==0))
        if q==4: continue
        c=sum(expr(v)*X**(q**i) for i,v in enumerate(row['carlitz']))
        verify(s.Poly(s.diff(c,X)-expr(row['a']),X,T,modulus=q).is_zero)
        composed=s.Poly(c.subs(X,T*X+X**q)-(T*c+c**q),X,T,modulus=q)
        verify(composed.is_zero)
    for row in data['tower_cases']:
        q=row['q']
        if q==4: continue
        P=s.Poly(expr(row['P']),T,modulus=q)
        verify(s.rem(s.Poly(expr(dict(row['psi'])[0]),T,modulus=q),P).is_zero)
        for i,c in row['psi']:
            if i!=row['degree']: verify(s.rem(s.Poly(expr(c),T,modulus=q),P).is_zero)
        verify(dict(row['psi'])[0]==row['P'])
    # Direct integer finite-function matrices, independently of any Carlitz code.
    for q in (2,3,5):
        for a0 in range(q):
            for b in (0,1,q-1):
                M=s.zeros(q)
                for x in range(q): M[b*x%q,x]=1
                det=(s.eye(q)-z*M).det()
                for n in range(1,5): verify(int(s.trace(M**n))==sum(pow(b,n,q)*x%q==x for x in range(q)))
                verify(s.expand(det).subs(z,0)==1)
    w=s.symbols('w')
    for a in range(4):
        for b in range(4):
            aa=(a&1)+(a>>1)*w; bb=(b&1)+(b>>1)*w
            reduced=s.rem(s.Poly(aa*bb,w,modulus=2),s.Poly(w*w+w+1,w,modulus=2))
            table=((0,0,0,0),(0,1,2,3),(0,2,3,1),(0,3,1,2))[a][b]
            verify(s.Poly(reduced.as_expr()-((table&1)+(table>>1)*w),w,modulus=2).is_zero)
    Q=s.symbols('Q',positive=True,integer=True)
    for k in range(1,10):
        e=(Q-1)*Q**(k-1)
        summed=e-1+sum((Q**r-Q**(r-1))*(Q**(k-r)-1) for r in range(1,k))
        verify(s.expand(summed-Q**(k-1)*(k*(Q-1)-1))==0)
    print(json.dumps({'status':'PASS','exact_checks':checks,'arithmetic':'exact finite fields and symbolic identities; no numeric precision claim'}))
if __name__=='__main__': main()
