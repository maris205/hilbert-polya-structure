#!/usr/bin/env python3
"""Canonical exact source evidence; finite regression, not the all-period proof."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("c379 producer refuses optimized Python")
import argparse
import hashlib
import json
from collections import defaultdict
from fractions import Fraction as F
from math import comb, gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FLAGS = ("claims_target_arithmetic_local_data", "claims_target_euler_factors", "claims_root_number", "claims_automorphy", "claims_target_divisor_or_counting_law", "claims_target_functional_equation", "claims_target_zero_match", "claims_hilbert_polya_operator", "invokes_route_b")
TUPLE = ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]

def canonical(x):
    return json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()

def frac(x):
    x = F(x)
    return [x.numerator, x.denominator]

def pack(p):
    return [[a, b, v.numerator, v.denominator] for (a, b), v in sorted(p.items()) if v]

def multiply(p, q, cutoff=12):
    r = defaultdict(F)
    for (a,b),v in p.items():
        for (c,d),w in q.items():
            if a+c <= cutoff:
                r[a+c,b+d] += v*w
    return {k:v for k,v in r.items() if v}

def chebyshev(n):
    a,b = {0:1},{1:1}
    if n == 0: return a
    for _ in range(1,n):
        c = defaultdict(int)
        for k,v in b.items(): c[k+1] += 2*v
        for k,v in a.items(): c[k] -= v
        a,b = b,dict(c)
    return b

def determinant(L):
    p = {(L-k,0):F(v,2**(L-1)) for k,v in chebyshev(L).items() if v}
    p[L,1] = F(-1,2**L)
    p[L,-1] = F(-1,2**L)
    return p

def make():
    fixed=[]
    for L in range(1,9):
        for n in range(1,13):
            full=defaultdict(int)
            geo=defaultdict(int)
            for k in range(n+1):
                S=2*k-n
                if S%L == 0:
                    full[S//L] += L*comb(n,k)
                    if k not in (0,n): geo[S//L] += L*comb(n,k)
            fixed.append({"L":L,"n":n,"symbolic":[[w,c] for w,c in sorted(full.items())],"geometric":[[w,c] for w,c in sorted(geo.items())]})
    primitive=defaultdict(int)
    necklace=[]
    for d in range(2,13):
        for a in range(1,2**d-1):
            w=f"{a:0{d}b}"
            rotations=[w[k:]+w[:k] for k in range(d)]
            if w != min(rotations) or len(set(rotations)) != d: continue
            S=2*w.count("1")-d
            for L in range(1,9):
                g=gcd(L,S); q=d*L//g; W=S//g
                if q<=12:
                    primitive[L,q,W] += g
                    necklace.append({"L":L,"word":w,"d":d,"S":S,"q":q,"W":W,"multiplicity":g,"reversed_necklace":min((v:= "".join("1" if s=="0" else "0" for s in w[::-1]))[k:]+v[:k] for k in range(d))})
    witnesses=[]
    for L in range(1,7):
        for n in range(2,7):
            for a in range(1,2**n-1):
                w=f"{a:0{n}b}"; S=2*w.count("1")-n
                if S%L: continue
                x=F(a,2**n-1); y=F(int(w[::-1],2),2**n-1)
                xx,yy,j=x,y,0
                cells=[]
                for s in map(int,w):
                    cells.append(j)
                    assert int(2*xx)==s
                    xx,yy,j=2*xx-s,(yy+s)/2,(j+2*s-1)%L
                assert (xx,yy,j)==(x,y,0)
                witnesses.append({"L":L,"n":n,"word":w,"x":frac(x),"y":frac(y),"cells":cells,"W":S//L,"unstable":2**n,"stable":[1,2**n],"flat_denominator":frac(F((2**n-1)**2,2**n))})
    determinants=[]
    zetas=[]
    for L in range(1,9):
        p=determinant(L)
        determinants.append({"L":L,"coefficients":pack(p)})
        product={(0,0):F(1)}
        for (ell,q,W),m in sorted(primitive.items()):
            if ell!=L: continue
            factor={(r*q,r*W):F(comb(m+r-1,r),2**(r*q)) for r in range(13//q+1)}
            product=multiply(product,factor)
        zetas.append({"L":L,"coefficients":pack(product)})
    controls=[]
    for L in range(1,9):
        n=2*L
        row=next(r for r in fixed if r["L"]==L and r["n"]==n) if n<=12 else None
        controls.append({"L":L,"prime_label_used":False,"relabel_cell_map":[(j+1)%L for j in range(L)],"neighbor_ring":L+1,"untilted_period":1 if L%2 else 2,"boundary_fixed_excess_at_nL":2*L,"lazy_gap_formula":"not_defined" if L==1 else "sin(pi/L)^2"})
    return {"schema":"c379-multibaker-evidence-v1","candidate_id":"HCS-C379","obstruction_id":"HEN-O363","source_commit":"0596f9d680277288225062a6fdd7ad7ce116e01d","evaluation_date":"2026-09-05","fixed_epoch":1788566400,"evaluator_authority":"flow_systems/skills/route-a-evaluator.md","evaluator_version":"0.2.0","evaluator_authority_sha256":"6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c","scope_literal":"NO_BAD_EULER_OR_ROOT_NUMBER","scope_flags":{k:False for k in FLAGS},"route_a":{"tuple":TUPLE,"overall_verdict":"ROUTE_A_REJECTED","route_b_invocation_allowed":False},"domain":"cell ring times two non-dyadic coordinates in (0,1)","clock":"unit map step; unit cell length","phase":"exp(i*phi*W), W=total_displacement/L on closed cycles","weight":"inverse unstable multiplier 2^(-period), not two-dimensional flat-trace weight","cutoffs":{"ring_max":8,"period_max":12,"geometry_ring_max":6,"geometry_period_max":6},"fixed_rows":fixed,"primitive_rows":[{"L":L,"q":q,"W":W,"count":c} for (L,q,W),c in sorted(primitive.items())],"necklace_rows":necklace,"geometry_rows":witnesses,"determinant_rows":determinants,"geometric_zeta_rows":zetas,"control_rows":controls,"diffusion":{"mean_per_step":0,"variance_per_step":1,"D":[1,2],"log_cos_coefficients":[[2,-1,2],[4,-1,12]],"even_ring_uniform_mixing":False,"L1_relaxation_gap_defined":False,"L2_parity_class_relaxation_mode":False},"nonclaims":["no target arithmetic carrier","no full phase-space Perron Fredholm determinant","no constructed quantization","no literature-priority claim"]}

def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--output",type=Path,default=ROOT/"results/c379_multibaker_evidence.json"); args=parser.parse_args()
    x=make(); x["payload_sha256"]=hashlib.sha256(canonical(x)).hexdigest()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(x,sort_keys=True,indent=2,ensure_ascii=False)+"\n")
    print(f"C379 producer PASS: fixed={len(x['fixed_rows'])} primitive={len(x['primitive_rows'])} geometry={len(x['geometry_rows'])} payload={x['payload_sha256']}")

if __name__=="__main__": main()
