#!/usr/bin/env python3
"""Exact finite evidence; infinite claims are proved in proof/ANALYTIC_PROOF.md."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("c393 producer refuses optimized Python")
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
    return {"schema":"hcs-exact-evidence-v1","candidate_id":"HCS-C393","source_commit":"0c877206d202f732e21ea0b194f9c7fdf30467ee","fixed_epoch":1788566400,"scope_literal":"NO_BAD_EULER_OR_ROOT_NUMBER","scope_flags":{k:False for k in FLAGS},"route_a":{"tuple":["A0_STRUCTURAL_ARITHMETIC_RELATION","A1_WEAK","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"],"overall_verdict":"ROUTE_A_EXPLORATORY","route_b_invocation_allowed":False},"evidence_role":"finite exact regression; not an infinite theorem or target match"}

def cycles(p):
    seen=set();out=[]
    for i in range(len(p)):
        if i in seen:continue
        v=i;k=0
        while v not in seen:seen.add(v);k+=1;v=p[v]
        out.append(k)
    return tuple(sorted(out))
def cycle_index(n):
    current={(1,):1};rows=[{"n":0,"order":1,"cycle_types":[{"lengths":[1],"count":1}],"fixed_probability":q(1)}]
    for h in range(1,n+1):
        order=sum(current.values());new={}
        for a,ca in current.items():
            for b,cb in current.items():
                t=tuple(sorted(a+b));new[t]=new.get(t,0)+ca*cb
        for a,ca in current.items():
            t=tuple(2*v for v in a);new[t]=new.get(t,0)+ca*order
        current=new
        rows.append({"n":h,"order":sum(new.values()),"cycle_types":[{"lengths":list(a),"count":new[a]} for a in sorted(new)],"fixed_probability":q(F(sum(c for a,c in new.items() if 1 in a),sum(new.values())))})
    return rows
def prime(p):return p>=2 and all(p%d for d in range(2,int(p**.5)+1))
def build():
    data=metadata();crit=[0]
    for i in range(8):crit.append(crit[-1]**2+1)
    data["critical_values"]=crit
    data["tower"]=[]
    for n in range(1,9):
        order=2**(2**n-1)
        genus=1+F(order,2)*(F(n,2)-1-F(1,2**n))
        data["tower"].append({"n":n,"degree":2**n,"order":order,"kernel":2**(2**(n-1)),"genus":int(genus),"new_branch_quadratic":2**(n-1)*prod(crit[1:n]),"finite_inertia":[{"i":i,"two_cycles":2**(n-i),"one_cycles":2**n-2**(n-i+1)} for i in range(1,n+1)],"infinite_inertia":[2**n]})
    data["cycle_indices"]=cycle_index(5)
    delta=F(1);data["root_probabilities"]=[]
    for n in range(13):
        if n:delta-=delta*delta/2
        data["root_probabilities"].append({"n":n,"probability":q(delta),"mean_fixed":1})
    fields=[]
    for p in range(2,100):
        if not prime(p):continue
        orbit=[0];seen={0:0};x=0
        while True:
            x=(x*x+1)%p
            if x in seen:
                collision=[seen[x],len(orbit)];break
            seen[x]=len(orbit);orbit.append(x)
        nxt=[(x*x+1)%p for x in range(p)];alive=set(range(p))
        while True:
            image={nxt[x] for x in alive}
            if image==alive:break
            alive=image
        image=set(range(p));levels=[]
        for n in range(1,7):
            image={nxt[x] for x in image}
            good=(p!=2 and len(set(c%p for c in crit[:n+1]))==n+1)
            roots=[sum(1 for x in range(p) if iterate(x,n,p)==a) for a in range(p)]
            levels.append({"n":n,"good_reduction":"yes" if good else "no","image_size":len(image),"root_histogram":[[r,roots.count(r)] for r in sorted(set(roots))]})
        fields.append({"p":p,"critical_collision":collision,"periodic_points":sorted(alive),"levels":levels})
    data["finite_fields"]=fields
    data["controls"]=[{"c":c,"orbit":[0]+[iterate_c(0,n,c) for n in range(1,7)]} for c in (-1,0,1)]
    data["clock_boundary"]=["generic t not every specialization","fixed n then p limit then n limit","Frobenius iteration not tree height","composite moduli not fields"]
    return data
def iterate(x,n,p):
    for _ in range(n):x=(x*x+1)%p
    return x
def iterate_c(x,n,c):
    for _ in range(n):x=x*x+c
    return x

def main():
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,default=ROOT/"results/c393_arboreal_evidence.json");a=p.parse_args()
    data=build();data["payload_sha256"]=hashlib.sha256(canonical(data)).hexdigest()
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(data,sort_keys=True,indent=2,ensure_ascii=False)+"\n")
    print("C393 producer PASS: "+data["payload_sha256"])
if __name__=="__main__":main()
