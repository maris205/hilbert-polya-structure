#!/usr/bin/env python3
"""Exact dyadic enclosure producer for a proved intermittent source system."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("c381 producer refuses optimized Python")
import argparse
import hashlib
import json
from fractions import Fraction as F
from itertools import product
from math import isqrt
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BITS=160; Q=2**BITS; MBITS=80; MQ=2**MBITS
FLAGS=("claims_target_arithmetic_local_data","claims_target_euler_factors","claims_root_number","claims_automorphy","claims_target_divisor_or_counting_law","claims_target_functional_equation","claims_target_zero_match","claims_hilbert_polya_operator","invokes_route_b")
TUPLE=["A0_FAIL","A1_WEAK","A2_FAIL","A3_FAIL","A4_FAIL"]

def canonical(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
def ceildiv(a,b):return -((-a)//b)
def floorfrac(x,scale):return x.numerator*scale//x.denominator
def ceilfrac(x,scale):return ceildiv(x.numerator*scale,x.denominator)

def left_interval(lo,hi):
    lower=(isqrt(Q*Q+8*lo*Q)-Q)//4
    upper=(isqrt(Q*Q+8*hi*Q)-Q)//4+1
    return max(0,lower),upper

def inverse_word(word,lo,hi):
    for s in reversed(word):
        if s=="0":lo,hi=left_interval(lo,hi)
        else:lo,hi=(lo+Q)//2,ceildiv(hi+Q,2)
    return lo,hi

def least(w):
    return next(d for d in range(1,len(w)+1) if len(w)%d==0 and w==w[:d]*(len(w)//d))

def forward(word,x):
    deriv=F(1)
    for s in word:
        if s=="0":deriv*=1+4*x;x=x+2*x*x
        else:deriv*=2;x=2*x-1
    return x,deriv

def fixed(word):
    if set(word)=={"0"}:lo=hi=0
    elif set(word)=={"1"}:lo=hi=Q
    else:
        lo,hi=0,Q
        for _ in range(200):lo,hi=inverse_word(word,lo,hi)
    flo,dlo=forward(word,F(lo,Q));fhi,dhi=forward(word,F(hi,Q))
    assert flo<=F(lo,Q) and fhi>=F(hi,Q)
    assert hi-lo<=1024
    return [lo,hi],[floorfrac(dlo,MQ),ceilfrac(dhi,MQ)]

def make():
    periodic=[]; primitive=[]
    for n in range(1,7):
        count=0
        for bits in product("01",repeat=n):
            w="".join(bits);bounds,mult=fixed(w);d=least(w)
            periodic.append({"word":w,"n":n,"least_period":d,"repetition":n//d,"point_bounds":bounds,"multiplier_bounds":mult,"neutral":set(w)=={"0"},"orientation":1})
            if d==n and w==min(w[k:]+w[:k] for k in range(n)):count+=1
        primitive.append({"n":n,"fixed_count":2**n,"primitive_cycles":count,"neutral_cycles":1 if n==1 else 0})
    returns=[]
    for numerator,denominator in ((1,2),(5,8),(3,4),(7,8),(1,1)):
        lo=hi=Q*numerator//denominator;dl=du=Q
        for n in range(1,129):
            if n>1:
                lo,hi=left_interval(lo,hi)
                dl,du=dl*Q//(Q+4*hi),ceildiv(du*Q,Q+4*lo)
            returns.append({"x":[numerator,denominator],"n":n,"preimage_bounds":[lo,hi],"preimage_derivative_bounds":[dl,du],"h_bounds":[(Q+lo)//2,ceildiv(Q+hi,2)],"h_derivative_bounds":[dl//2,ceildiv(du,2)]})
    tails=[];lo=hi=Q//2
    for m in range(257):
        if m:lo,hi=left_interval(lo,hi)
        tails.append({"m":m,"a_bounds":[lo,hi],"reciprocal_bounds":[[1,2*m+2],[1,m+2]],"return_tail_n":m+1,"tail_bounds":[lo//2,ceildiv(hi,2)]})
    induced=[]
    for r in range(1,4):
        for branch in product(range(1,4),repeat=r):
            word="".join("1"+"0"*(n-1) for n in branch)
            point,mult=fixed(word)
            induced.append({"branches":list(branch),"return_period":r,"original_time":sum(branch),"word":word,"point_bounds":point,"multiplier_bounds":mult,"trace_weight_bounds":[floorfrac(F(MQ,mult[1]-MQ),MQ),ceilfrac(F(MQ,mult[0]-MQ),MQ)]})
    heads=[]
    for r in range(1,4):
        lo=hi=F(0)
        for row in induced:
            if row["return_period"]==r:
                a,b=row["trace_weight_bounds"]; factor=F(1,4**row["original_time"])
                lo+=F(a,MQ)*factor;hi+=F(b,MQ)*factor
        heads.append({"return_period":r,"branch_cutoff":3,"zeta":[1,4],"trace_head_bounds":[floorfrac(lo,MQ),ceilfrac(hi,MQ)],"infinite_trace_claim":False})
    return {"schema":"c381-lsv-evidence-v1","candidate_id":"HCS-C381","obstruction_id":"HEN-O365","source_commit":"0596f9d680277288225062a6fdd7ad7ce116e01d","evaluation_date":"2026-09-05","fixed_epoch":1788566400,"evaluator_authority":"flow_systems/skills/route-a-evaluator.md","evaluator_version":"0.2.0","evaluator_authority_sha256":"6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c","scope_literal":"NO_BAD_EULER_OR_ROOT_NUMBER","scope_flags":{k:False for k in FLAGS},"route_a":{"tuple":TUPLE,"overall_verdict":"ROUTE_A_REJECTED","route_b_invocation_allowed":False},"partition":"left [0,1/2]; right (1/2,1]","base":"Y=(1/2,1]","clock":"u counts returns; zeta counts original iterations","domain":"Hardy H2 on disk center 1 radius 3/4","cutoffs":{"period_max":6,"return_branch_max":128,"tail_m_max":256,"induced_alphabet_max":3,"induced_period_max":3,"point_bits":BITS,"multiplier_bits":MBITS},"periodic_rows":periodic,"primitive_rows":primitive,"return_rows":returns,"tail_rows":tails,"induced_rows":induced,"trace_head_rows":heads,"complex_bounds":{"domain_radius":[3,4],"image_radius":[1,2],"hardy_ratio":[2,3],"initial_reciprocal_real_lower":[4,7],"reciprocal_increment_real_lower":[2,25],"derivative_bound_prefactor":1250,"derivative_bound_exp_pi2_coefficient":[625,6],"nuclear_rank_sum":3,"absolute_branch_domain":"abs(zeta)<=1","outside_terms_tend_to_zero":False},"tail_asymptotic":{"lebesgue_constant":[1,4],"normalized_constant":[1,2],"mean_return_finite":False},"uninduced":{"space":"Lebesgue L1([0,1])","compact":False,"zero_integral_uniform_exponential_decay":False,"approximate_vector_norm":1,"residual_bound_factor":12,"invariant_density_claim":False},"nonclaims":["no target arithmetic carrier","no full uninduced Fredholm determinant","no infinite determinant inferred from branch cutoff","no claim against regularized determinants on other spaces","no literature-priority claim"]}

def main():
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,default=ROOT/"results/c381_lsv_evidence.json");a=p.parse_args()
    x=make();x["payload_sha256"]=hashlib.sha256(canonical(x)).hexdigest()
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(x,sort_keys=True,indent=2,ensure_ascii=False)+"\n")
    print(f"C381 producer PASS: periodic={len(x['periodic_rows'])} return={len(x['return_rows'])} tail={len(x['tail_rows'])} induced={len(x['induced_rows'])} payload={x['payload_sha256']}")

if __name__=="__main__":main()
