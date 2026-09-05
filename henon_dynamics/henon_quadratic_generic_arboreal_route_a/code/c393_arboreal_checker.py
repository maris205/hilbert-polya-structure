#!/usr/bin/env python3
"""Independent reconstruction: never imports the evidence producer."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("c393 checker refuses optimized Python")
import argparse, hashlib, json
from fractions import Fraction as F
from pathlib import Path
from math import gcd, prod
from collections import Counter
from itertools import product
import yaml
ROOT=Path(__file__).resolve().parents[1]
EVAL=ROOT/"evaluations/route_a/HCS-C393/2026-09-05.yaml"
EVALUATION_SEMANTIC_SHA="33b31b9e0cbc8ffafcf26c579da466c09bed948aca014f42e3b0910c4f5a1a79"
FLAGS=["claims_target_arithmetic_local_data","claims_target_euler_factors","claims_root_number","claims_automorphy","claims_target_divisor_or_counting_law","claims_target_functional_equation","claims_target_zero_match","claims_hilbert_polya_operator","invokes_route_b"]
def canonical(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
def q(x):
    x=F(x);return [x.numerator,x.denominator]
def unique(pairs):
    d={}
    for k,v in pairs:
        if k in d:raise ValueError("duplicate JSON key")
        d[k]=v
    return d
def read(path):return json.loads(path.read_text(),object_pairs_hook=unique,parse_constant=lambda x:(_ for _ in ()).throw(ValueError("nonfinite JSON")))
def exact_shape(x,path=()):
    if type(x) is dict:
        assert all(type(k) is str for k in x)
        for k,v in x.items():exact_shape(v,path+(k,))
    elif type(x) is list:
        for i,v in enumerate(x):exact_shape(v,path+(i,))
    else:
        assert type(x) in (str,int,bool),f"invalid type at {path}"
        if type(x) is bool:assert path[-1] in FLAGS+["route_b_invocation_allowed"],f"numeric boolean at {path}"
def frac(v):
    assert type(v) is list and len(v)==2 and all(type(t) is int for t in v)
    assert v[1]>0 and gcd(v[0],v[1])==1
    return F(*v)
class LockedLoader(yaml.SafeLoader):pass
def mapping(loader,node,deep=False):
    out={}
    for k,v in node.value:
        key=loader.construct_object(k,deep=deep)
        if type(key) is not str or key in out or key=="<<":raise ValueError("invalid YAML key")
        out[key]=loader.construct_object(v,deep=deep)
    return out
LockedLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,mapping)
def evaluation(path):
    raw=path.read_text()
    for token in yaml.scan(raw):
        assert not isinstance(token,(yaml.tokens.AliasToken,yaml.tokens.AnchorToken,yaml.tokens.TagToken)),"YAML alias anchor tag"
    v=yaml.load(raw,Loader=LockedLoader);exact_shape(v)
    assert v["route_b_invocation_allowed"] is False
    assert set(v["scope_flags"])==set(FLAGS) and all(x is False for x in v["scope_flags"].values())
    assert hashlib.sha256(canonical(v)).hexdigest()==EVALUATION_SEMANTIC_SHA,"evaluation semantic lock"
    return v

def metadata():
    return {"schema":"hcs-exact-evidence-v1","candidate_id":"HCS-C393","source_commit":"0c877206d202f732e21ea0b194f9c7fdf30467ee","fixed_epoch":1788566400,"scope_literal":"NO_BAD_EULER_OR_ROOT_NUMBER","scope_flags":{k:False for k in FLAGS},"route_a":{"tuple":["A0_STRUCTURAL_ARITHMETIC_RELATION","A1_WEAK","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"],"overall_verdict":"ROUTE_A_EXPLORATORY","route_b_invocation_allowed":False},"evidence_role":"finite exact regression; not an infinite theorem or target match"}

def cycle_type(p):
    unused=set(range(len(p)));lengths=[]
    while unused:
        start=min(unused);v=p[start];k=1;unused.remove(start)
        while v!=start:unused.remove(v);v=p[v];k+=1
        lengths.append(k)
    return tuple(sorted(lengths))
def permutation_levels():
    group=[(0,)];counts=[Counter({(1,):1})]
    for n in range(1,5):
        N=len(group[0]);new=[]
        for a,b in product(group,repeat=2):
            new.append(tuple(a)+tuple(N+x for x in b))
            new.append(tuple(N+x for x in a)+tuple(b))
        group=new;counts.append(Counter(cycle_type(p) for p in group))
    return counts
def periodic(nxt):
    result=set()
    for start in range(len(nxt)):
        path=[];position={};v=start
        while v not in position:
            position[v]=len(path);path.append(v);v=nxt[v]
        result.update(path[position[v]:])
    return result
def math_check(d):
    crit=[0]
    for _ in range(8):crit.append(crit[-1]*crit[-1]+1)
    assert d["critical_values"]==crit and len(set(crit))==9
    assert len(d["tower"])==8
    for n,row in enumerate(d["tower"],1):
        deg=2**n;order=prod(2**(2**i) for i in range(n))
        inertia=[{"i":i,"two_cycles":2**(n-i),"one_cycles":deg-2*2**(n-i)} for i in range(1,n+1)]
        RH=-2*order+n*(order-order//2)+(order-order//deg)
        A=1
        for i in range(1,n):A*=2*crit[i]
        assert row=={"n":n,"degree":deg,"order":order,"kernel":order//(prod(2**(2**i) for i in range(n-1))),"genus":(RH+2)//2,"new_branch_quadratic":A,"finite_inertia":inertia,"infinite_inertia":[deg]}
    counts=permutation_levels();last=counts[-1];N=sum(last.values());next_counts=Counter()
    # Complete convolution of independently enumerated height-4 classes.
    for a,ca in last.items():
        for b,cb in last.items():next_counts[tuple(sorted(a+b))]+=ca*cb
    for a,ca in last.items():next_counts[tuple(2*x for x in a)]+=N*ca
    counts.append(next_counts)
    assert len(d["cycle_indices"])==6
    for n,(row,C) in enumerate(zip(d["cycle_indices"],counts)):
        total=sum(C.values());fixed=sum(v for a,v in C.items() if 1 in a)
        assert sum(v*a.count(1) for a,v in C.items())==total
        assert all(sum(a)==2**n for a in C)
        assert row=={"n":n,"order":total,"cycle_types":[{"lengths":list(a),"count":v} for a,v in sorted(C.items())],"fixed_probability":q(F(fixed,total))}
    nofixed=F(0);expected=[]
    for n in range(13):
        if n:nofixed=(1+nofixed**2)/2
        expected.append({"n":n,"probability":q(1-nofixed),"mean_fixed":1})
    assert d["root_probabilities"]==expected
    primes=[p for p in range(2,100) if all(p%k for k in range(2,p))]
    assert len(d["finite_fields"])==len(primes)
    for p,row in zip(primes,d["finite_fields"]):
        nxt=[(x*x+1)%p for x in range(p)];path=[];v=0
        while v not in path:path.append(v);v=nxt[v]
        coll=[path.index(v),len(path)]
        per=sorted(periodic(nxt));levels=[];images=list(range(p))
        for n in range(1,7):
            images=[nxt[x] for x in images];hist=Counter(Counter(images).values());hist[0]=p-len(set(images))
            hist={r:c for r,c in hist.items() if c}
            good=p>2 and all((crit[j]-crit[i])%p for j in range(1,n+1) for i in range(j))
            assert set(per)<=set(images)
            levels.append({"n":n,"good_reduction":"yes" if good else "no","image_size":len(set(images)),"root_histogram":[[r,c] for r,c in sorted(hist.items())]})
        assert row=={"p":p,"critical_collision":coll,"periodic_points":per,"levels":levels}
    controls=[]
    for c in (-1,0,1):
        x=0;orbit=[x]
        for n in range(6):x=x*x+c;orbit.append(x)
        controls.append({"c":c,"orbit":orbit})
    assert d["controls"]==controls
    assert d["clock_boundary"]==["generic t not every specialization","fixed n then p limit then n limit","Frobenius iteration not tree height","composite moduli not fields"]
    return {"direct_tree_permutations":sum(2**(2**n-1) for n in range(1,5))+1,"cycle_types":sum(len(C) for C in counts),"finite_fields":len(primes),"finite_field_levels":6*len(primes)}
DATA_KEYS={"critical_values","tower","cycle_indices","root_probabilities","finite_fields","controls","clock_boundary"}

def check(path,evaluation_path=EVAL):
    data=read(path);exact_shape(data);digest=data.pop("payload_sha256")
    assert type(digest) is str and len(digest)==64 and hashlib.sha256(canonical(data)).hexdigest()==digest
    meta=metadata();assert set(data)==set(meta)|DATA_KEYS
    for k,v in meta.items():assert data[k]==v,f"metadata {k}"
    assert all(v is False for v in data["scope_flags"].values()) and data["route_a"]["route_b_invocation_allowed"] is False
    result=math_check(data);evaluation(evaluation_path)
    result["payload"]=digest;return result
def main():
    p=argparse.ArgumentParser();p.add_argument("evidence",nargs="?",type=Path,default=ROOT/"results/c393_arboreal_evidence.json");p.add_argument("--evaluation",type=Path,default=EVAL);a=p.parse_args()
    print("C393 independent checker PASS: "+json.dumps(check(a.evidence,a.evaluation),sort_keys=True))
if __name__=="__main__":main()
