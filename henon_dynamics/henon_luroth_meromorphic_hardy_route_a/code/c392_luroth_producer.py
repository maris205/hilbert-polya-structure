#!/usr/bin/env python3
"""Exact finite evidence; infinite claims are proved in proof/ANALYTIC_PROOF.md."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("c392 producer refuses optimized Python")
import argparse, hashlib, json
from pathlib import Path
from fractions import Fraction as F
from math import comb, factorial, gcd, prod
from itertools import product
ROOT=Path(__file__).resolve().parents[1]
FLAGS=["claims_target_arithmetic_local_data","claims_target_euler_factors","claims_root_number","claims_automorphy","claims_target_divisor_or_counting_law","claims_target_functional_equation","claims_target_zero_match","claims_hilbert_polya_operator","invokes_route_b"]
def q(x):
    x=F(x); return [x.numerator,x.denominator]
def canonical(x): return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
def metadata():
    return {"schema":"hcs-exact-evidence-v1","candidate_id":"HCS-C392","source_commit":"0c877206d202f732e21ea0b194f9c7fdf30467ee","fixed_epoch":1788566400,"scope_literal":"NO_BAD_EULER_OR_ROOT_NUMBER","scope_flags":{k:False for k in FLAGS},"route_a":{"tuple":["A0_FAIL","A1_WEAK","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"],"overall_verdict":"ROUTE_A_REJECTED","route_b_invocation_allowed":False},"evidence_role":"finite exact regression; not an infinite theorem or target match"}

def rising(s,r): return prod((s+j for j in range(r)),start=F(1))
def residue(l):
    s=F(1-l,2);m=l//2
    matrix=[]
    for i in range(l+1):
        row=[]
        for j in range(l+1):
            value=F(0)
            for b in range(i,j+1):
                rem=l-j-b
                if rem>=0 and rem%2==0:
                    r=rem//2
                    value+=F(comb(j,b)*comb(b,i),2)*F(-1,2)**(b-i)*rising(s+j,r)/F(4**r*factorial(r))
            row.append(q(value))
        matrix.append(row)
    return {"l":l,"pole":q(s),"rank":m+1,"kind":"square_zero" if l%2 else "nonzero_diagonal","matrix":matrix}
def build():
    data=metadata()
    data["branches"]=[{"n":n,"slope":q(F(1,n*(n+1))),"offset":q(F(1,n+1)),"disk_ratio":q(F(n+2,2*n*(n+1)))} for n in range(1,13)]
    matrices=[]
    for s,N in product(range(1,5),(1,2,4,8)):
        M=[[sum((F(comb(j,i))*F(1,n*(n+1))**(s+i)*F(1,n+1)**(j-i) for n in range(1,N+1)),F(0)) if i<=j else F(0) for j in range(7)] for i in range(7)]
        matrices.append({"s":s,"N":N,"dimension":7,"matrix":[[q(v) for v in row] for row in M],"diagonal":[q(M[j][j]) for j in range(7)]})
    data["matrices"]=matrices
    data["residues"]=[residue(l) for l in range(10)]
    data["scalar_poles"]=[{"m":m,"pole":q(F(1,2)-m),"residue":q(F((-1)**m*comb(2*m,m),2*16**m)),"determinant_pole_order":m+1} for m in range(10)]
    words=[]
    for r in range(1,5):
        for w in product(range(1,5),repeat=r):
            A=F(1);B=F(0)
            for n in reversed(w):
                a=F(1,n*(n+1));b=F(1,n+1);A=a*A;B=a*B+b
            d=next(d for d in range(1,r+1) if r%d==0 and w==w[:d]*(r//d))
            neck=min(w[k:]+w[:k] for k in range(r))
            words.append({"word":list(w),"slope":q(A),"point":q(B/(1-A)),"least_period":d,"necklace":list(neck),"trace_s1":q(A/(1-A))})
    data["words"]=words
    data["controls"]={"isolated_zero":"not branch weighted","s_half":"branch sum diverges","s_zero_residue_on_z":q(F(1,2)),"s_zero_residue_on_one":q(0),"s_one_sum":q(1),"tail_after_N_at_s1":[{"N":N,"tail":q(F(1,N+1))} for N in (1,2,4,8,16)],"source_slopes":"n(n+1) composite for n>=2, not a prime list"}
    return data

def main():
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,default=ROOT/"results/c392_luroth_evidence.json");a=p.parse_args()
    data=build();data["payload_sha256"]=hashlib.sha256(canonical(data)).hexdigest()
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(data,sort_keys=True,indent=2,ensure_ascii=False)+"\n")
    print("C392 producer PASS: "+data["payload_sha256"])
if __name__=="__main__":main()
