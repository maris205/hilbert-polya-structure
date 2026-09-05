#!/usr/bin/env python3
"""Canonical exact finite BCZ evidence; universal statements live in the proof."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("c395 producer refuses optimized Python")
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
FLAGS=("claims_target_arithmetic_local_data","claims_target_euler_factors","claims_root_number","claims_automorphy","claims_target_divisor_or_counting_law","claims_target_functional_equation","claims_target_zero_match","claims_hilbert_polya_operator","invokes_route_b")
TUPLE=["A0_WEAK_ARITHMETIC_RELATION","A1_WEAK","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"]
def canonical(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
def rat(x):x=F(x);return [x.numerator,x.denominator]
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def step(a,b):
    k=(1+a)//b
    return (b,k*b-a),k
def totients(n):
    p=list(range(n+1))
    for q in range(2,n+1):
        if p[q]==q:
            for k in range(q,n+1,q):p[k]-=p[k]//q
    p[1]=1
    return p
def build():
    rows=[];phis=totients(64)
    for n in range(1,65):
        start=(1,n);point=start;cycle=[];indices=[];matrices=[];product=[[1,0],[0,1]]
        while not cycle or point!=start:
            assert point not in cycle
            q,r=point;k=(n+q)//r
            cycle.append([q,r]);indices.append(k)
            matrices.append([[1-q*r,q*q],[-r*r,1+q*r]])
            product=mm([[0,1],[-1,k]],product)
            point=(r,k*r-q)
        assert len(cycle)==sum(phis[1:n+1])
        roof=sum((F(1,q*r) for q,r in cycle),F())
        powers=[];power=[[1,0],[0,1]]
        for ell in range(1,6):
            power=mm(product,power)
            powers.append({"repetition":ell,"matrix":power,"roof_multiplier":ell})
        rows.append({"N":n,"least_period":len(cycle),"scale_interval":[rat(F(1,n+1)),rat(F(1,n))],"lower_included":False,"upper_included":True,"interior_scale":rat(F(2,2*n+1)),"cycle":cycle,"branch_indices":indices,"return_matrices":matrices,"product_at_start":product,"gap_sum":rat(roof),"interior_total_roof":rat(roof/F(2,2*n+1)**2),"endpoint_total_roof":rat(roof*n*n),"repetitions":powers})
    wall_rows=[]
    for n in range(2,18):
        eps=F(1,16*n*n);p=(F(1),F(1,n));near=(1-eps,F(1,n)+eps)
        v,k=step(*p);w,j=step(*near)
        wall_rows.append({"N":n,"epsilon":rat(eps),"point":[rat(t) for t in p],"exact_image":[rat(t) for t in v],"exact_branch":k,"near_point":[rat(t) for t in near],"near_image":[rat(t) for t in w],"near_branch":j,"one_sided_limit":[rat(F(1,n)),rat(1-F(1,n))],"two_sided_derivative_exists":False})
    fixed_rows=[]
    for t in range(1,129):
        layers=[r["N"] for r in rows if r["least_period"]<=t and t%r["least_period"]==0]
        fixed_rows.append({"iterate":t,"layers":layers,"radial_segments":sum(rows[n-1]["least_period"] for n in layers),"cardinality":"uncountable"})
    x={"schema":"c395-bcz-evidence-v1","candidate_id":"HCS-C395","obstruction_id":"HEN-O379","source_commit":"697518b6db90458f86f7916fbf397b8ad5ef2372","fixed_epoch":1788566400,"scope_literal":"NO_BAD_EULER_OR_ROOT_NUMBER","scope_flags":{k:False for k in FLAGS},"route_a":{"tuple":TUPLE,"route_b_invocation_allowed":False},"contract":{"domain":"0<a,b<=1; a+b>1","layer_range":[1,64],"wall_range":[2,17],"fixed_iterate_range":[1,128],"physical_repetition_range":[1,5],"arithmetic":"all positive coprime denominator pairs; no prime filtering","precision":"exact integers and reduced rationals","theorem_scope":"all N>=1 and all scales; finite ledger is a consistency control"},"layer_rows":rows,"wall_rows":wall_rows,"fixed_rows":fixed_rows,"summary":{"layers":64,"cycle_points":sum(r["least_period"] for r in rows),"rational_scale_step_controls":2*sum(r["least_period"] for r in rows),"return_matrices":sum(r["least_period"] for r in rows),"repetition_controls":320,"wall_controls":16,"fixed_iterates":128}}
    x["payload_sha256"]=hashlib.sha256(canonical(x)).hexdigest()
    return x
def main():
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,default=ROOT/"results/c395_bcz_evidence.json");a=p.parse_args();x=build()
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(x,sort_keys=True,indent=2,ensure_ascii=False)+"\n")
    print("C395 producer PASS: "+json.dumps(x["summary"],sort_keys=True)+" payload="+x["payload_sha256"])
if __name__=="__main__":main()
