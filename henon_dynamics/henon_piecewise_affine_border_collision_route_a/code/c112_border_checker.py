#!/usr/bin/env python3
"""Independent exact checker for C112."""
from __future__ import annotations
import itertools, json
from fractions import Fraction as Q
from pathlib import Path
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]; D=json.loads((ROOT/"results/c112_border_evidence.json").read_text())
N=int(D["source_model"]["max_period"]); B=((Q(-5),Q(-1)),(Q(1),Q(0))); SHIFT=((Q(-2),Q(0)),(Q(2),Q(0))); RHO=(Q(1,2),Q(2,3))
def mm(a,b): return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def mv(a,v): return tuple(sum(a[i][j]*v[j] for j in range(2)) for i in range(2))
def det(a): return a[0][0]*a[1][1]-a[0][1]*a[1][0]
def canon(w): return min(tuple(w[i:]+w[:i]) for i in range(len(w)))
def primitive(w): return all(tuple(w)!=tuple(w[:d]*(len(w)//d)) for d in range(1,len(w)) if len(w)%d==0)
def fixed(word):
    m=((Q(1),Q(0)),(Q(0),Q(1))); t=(Q(0),Q(0))
    for s in word: m=mm(B,m); t=tuple(x+y for x,y in zip(mv(B,t),SHIFT[s]))
    a=((Q(1)-m[0][0],-m[0][1]),(-m[1][0],Q(1)-m[1][1])); dd=det(a)
    z=((t[0]*a[1][1]-a[0][1]*t[1])/dd,(a[0][0]*t[1]-t[0]*a[1][0])/dd); cur=z
    for s in word:
        assert cur[0]!=0 and ((cur[0]<0)==(s==0)); cur=(-5*cur[0]-cur[1]+SHIFT[s][0],cur[0])
    assert cur==z; return m,z
rows=[]
for n in range(1,N+1):
    seen=set()
    for w in itertools.product((0,1),repeat=n):
        if not primitive(list(w)): continue
        c=canon(list(w))
        if c in seen: continue
        seen.add(c); m,z=fixed(c); q=lambda x:str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"; wt=Q(1)
        for s in c: wt*=RHO[s]
        rows.append((n,''.join(map(str,c)),[q(x) for x in z],q(m[0][0]+m[1][1]),q(det(m)),q(wt)))
assert len(rows)==sum(int(v) for v in D["primitive_necklace_counts"].values())
for row in D["primitive_rows"]:
    got=next(x for x in rows if x[:2]==(row["length"],row["word"])); assert row["fixed_point"]==got[2] and row["monodromy_trace"]==got[3] and row["monodromy_determinant"]==got[4] and row["branch_weight"]==got[5]
z=sp.Symbol('z'); W=sp.zeros(4); b=sp.Matrix([[-5,-1],[1,0]])
for i in range(2):
    for j in range(2): W[2*i:2*i+2,2*j:2*j+2]=sp.Rational(RHO[j].numerator,RHO[j].denominator)*b
assert str(sp.factor((sp.eye(4)-z*W).det()))==D["weighted_transfer_determinant"]
assert D["verdict"]["A1"]=="A1_PARTIAL_CERTIFIED" and D["verdict"]["A2"]=="A2_CERTIFIED_PREFIX"
print("C112_CHECK_PASS",len(rows))
