#!/usr/bin/env python3
"""Canonical exact finite certificates; universal claims live in the proof."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("c388 producer refuses optimized Python")
import argparse
from fractions import Fraction
import hashlib
import json
from math import gcd, prod
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
BASELINE="3e692da6fa94362225c7534e9b66c83c15c7f284"
FLAGS=("claims_target_arithmetic_local_data","claims_target_euler_factors","claims_root_number","claims_automorphy","claims_target_divisor_or_counting_law","claims_target_functional_equation","claims_target_zero_match","claims_hilbert_polya_operator","invokes_route_b")
TUPLE=["A0_WEAK_ARITHMETIC_RELATION","A1_WEAK","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"]
def canonical(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
def grid():
    q={(a,b,c) for a in range(1,13) for c in range(1,13) if a*c<=12 for b in range(a)}
    q.update((a,b,c) for a,c in ((3,6),(6,3),(6,6)) for b in range(a))
    return sorted(q,key=lambda v:(v[0]*v[2],v))
def matrix(a,b,c):
    n=a*c;out=[[0]*n for _ in range(n)]
    for i in range(a):
        for j in range(c):
            for x,y in ((i,j),(i+1,j),(i,j+1)):
                q,r=divmod(y,c);out[i*c+j][((x-q*b)%a)*c+r]+=1
    return out
def smith_certificate(source):
    n=len(source);m=[r[:] for r in source]
    u=[[int(i==j) for j in range(n)] for i in range(n)]
    v=[r[:] for r in u]
    def rs(i,j):m[i],m[j]=m[j],m[i];u[i],u[j]=u[j],u[i]
    def cs(i,j):
        for q in (m,v):
            for row in q:row[i],row[j]=row[j],row[i]
    def ra(i,j,k):
        for q in (m,u):q[i]=[x+k*y for x,y in zip(q[i],q[j])]
    def ca(i,j,k):
        for q in (m,v):
            for row in q:row[i]+=k*row[j]
    for k in range(n):
        candidates=[(abs(m[i][j]),i,j) for i in range(k,n) for j in range(k,n) if m[i][j]]
        if not candidates:break
        _,i,j=min(candidates);rs(k,i);cs(k,j)
        while True:
            changed=False
            for i in range(k+1,n):
                if m[i][k]:
                    ra(i,k,-(m[i][k]//m[k][k]))
                    if m[i][k]:rs(i,k)
                    changed=True;break
            if changed:continue
            for j in range(k+1,n):
                if m[k][j]:
                    ca(j,k,-(m[k][j]//m[k][k]))
                    if m[k][j]:cs(j,k)
                    changed=True;break
            if changed:continue
            bad=next(((i,j) for i in range(k+1,n) for j in range(k+1,n) if m[i][j]%m[k][k]),None)
            if bad is None:break
            ra(k,bad[0],1)
        if m[k][k]<0:ra(k,k,-2)
    d=[m[i][i] for i in range(n)]
    assert all(m[i][j]==0 for i in range(n) for j in range(n) if i!=j)
    return d,u,v
def lattice_row(a,b,c):
    n=a*c;A=matrix(a,b,c);d,u,v=smith_certificate(A)
    cp=list(map(int,sp.Matrix(A).charpoly().all_coeffs()))
    null=d.count(0);pdet=abs(cp[n-null]);tors=prod(x for x in d if x)
    resonance=(a%3==0 and (b-c)%3==0)
    assert null==2*resonance
    assert tors==Fraction(3,n*n)*pdet if resonance else tors==pdet
    gram=[[2*n//3,n//3],[n//3,2*n//3]] if resonance else []
    return {"hnf":[a,b,c],"index":n,"resonant":resonance,"matrix":A,"smith_diagonal":d,"left_unimodular":u,"right_unimodular":v,"rank":n-null,"torus_dimension":null,"component_count":tors,"characteristic_polynomial":cp,"nonzero_eigenvalue_product_abs":pdet,"kernel_gram":gram,"kernel_gram_determinant":n*n//3 if resonance else 1}
def torus_row(q):
    seen=set();cycles=[]
    for a in range(q):
        for b in range(q):
            if (a,b) in seen:continue
            path=[];p=(a,b)
            while p not in seen:
                seen.add(p);path.append(list(p));p=(p[1],(-p[0]-p[1])%q)
            assert p==(a,b);cycles.append(path)
    return {"denominator":q,"state_count":q*q,"fixed_count":sum(len(c)==1 for c in cycles),"period_three_cycles":sum(len(c)==3 for c in cycles),"cycles":cycles}
def rational(x):return [x.numerator,x.denominator]
def produce():
    rows=[lattice_row(*v) for v in grid()]
    partial=[]
    for h in (1,2,4,8,16,32,64,128):
        s=sum((Fraction(1,(3*k+1)**2)-Fraction(1,(3*k+2)**2) for k in range(h)),Fraction())
        tail=Fraction(2,(3*h+1)**3)+Fraction(1,3*(3*h+1)**2)
        partial.append({"paired_terms":h,"partial_sum":rational(s),"tail_upper":rational(tail)})
    out={"schema":"c388-connected-algebraic-evidence-v1","candidate_id":"HCS-C388","obstruction_id":"HEN-O372","source_commit":BASELINE,"fixed_epoch":1788566400,"scope_literal":"NO_BAD_EULER_OR_ROOT_NUMBER","scope_flags":{k:False for k in FLAGS},"route_a":{"tuple":TUPLE,"route_b_invocation_allowed":False},"contract":{"source_polynomial":"1+u+v","hnf":"columns (a,0),(b,c); a,c>0; 0<=b<a","grid":"all HNF index <=12 plus (a,c)=(3,6),(6,3),(6,6)","rational_torus_denominators":[1,24],"evidence_role":"finite exact certificates; not proof of universal claims"},"lattice_rows":rows,"torus_rows":[torus_row(q) for q in range(1,25)],"dirichlet_rows":partial,"summary":{"lattice_count":len(rows),"resonant_count":sum(r["resonant"] for r in rows),"nonresonant_count":sum(not r["resonant"] for r in rows),"torus_state_count":sum(q*q for q in range(1,25)),"dirichlet_bound_count":len(partial)}}
    out["payload_sha256"]=hashlib.sha256(canonical(out)).hexdigest();return out
def main():
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,default=ROOT/"results/c388_algebraic_evidence.json");a=p.parse_args()
    x=produce();a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(x,sort_keys=True,indent=2,ensure_ascii=False)+"\n")
    print("C388 producer PASS: "+json.dumps(x["summary"],sort_keys=True)+" payload="+x["payload_sha256"])
if __name__=="__main__":main()
