#!/usr/bin/env python3
"""Independent cyclic-system checker; no producer import or return solve."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("c385 checker refuses optimized Python")
import argparse
import hashlib
import json
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from math import gcd
from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[1]
EVAL=ROOT/"evaluations/route_a/HCS-C385/2026-09-05.yaml"
EVALUATION_SEMANTIC_SHA="cc5b191e6ea7f58e1f8e59355acf75e255d0fcfea83c688e8cb4a25501532bcb"
FLAGS=("claims_target_arithmetic_local_data","claims_target_euler_factors","claims_root_number","claims_automorphy","claims_target_divisor_or_counting_law","claims_target_functional_equation","claims_target_zero_match","claims_hilbert_polya_operator","invokes_route_b")
TUPLE=["A0_FAIL","A1_WEAK","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"]

def unique(pairs):
    d={}
    for k,v in pairs:
        if k in d: raise ValueError("duplicate JSON key")
        d[k]=v
    return d

def canonical(x): return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
def json_read(path): return json.loads(path.read_text(),object_pairs_hook=unique,parse_constant=lambda x: (_ for _ in ()).throw(ValueError("nonfinite JSON")))

def exact_shape(x,path=()):
    if isinstance(x,dict):
        assert all(type(k) is str for k in x)
        for k,v in x.items(): exact_shape(v,path+(k,))
    elif isinstance(x,list):
        for i,v in enumerate(x): exact_shape(v,path+(i,))
    else:
        assert type(x) in (str,int,bool),f"forbidden evidence type {type(x)}"
        if type(x) is bool:
            assert path and path[-1] in FLAGS+("route_b_invocation_allowed",),"boolean substituted for numeric data"

class LockedLoader(yaml.SafeLoader): pass

def mapping(loader,node,deep=False):
    result={}
    for k,v in node.value:
        key=loader.construct_object(k,deep=deep)
        if type(key) is not str or key in result or key=="<<": raise ValueError("invalid or repeated YAML key")
        result[key]=loader.construct_object(v,deep=deep)
    return result

LockedLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,mapping)

def read_evaluation(path):
    raw=path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token,(yaml.tokens.AliasToken,yaml.tokens.AnchorToken,yaml.tokens.TagToken)):
            raise ValueError("YAML references or explicit tags forbidden")
    value=yaml.load(raw,Loader=LockedLoader)
    exact_shape(value)
    assert hashlib.sha256(canonical(value)).hexdigest()==EVALUATION_SEMANTIC_SHA,"evaluation semantic lock"
    assert value["tuple"]==TUPLE
    assert value["route_b_invocation_allowed"] is False
    assert value["scope_flags"]=={k:False for k in FLAGS}
    assert all(v is False for v in value["scope_flags"].values()),"evaluation flags must be literal false"
    return value


def linear_solve(mat,rhs):
    n=len(rhs);a=[list(row)+[rhs[i]] for i,row in enumerate(mat)]
    for j in range(n):
        k=next(k for k in range(j,n) if a[k][j]);a[j],a[k]=a[k],a[j]
        t=a[j][j];a[j]=[v/t for v in a[j]]
        for i in range(n):
            if i!=j:
                t=a[i][j];a[i]=[v-t*w for v,w in zip(a[i],a[j])]
    return [r[-1] for r in a]

def frac(v):
    assert type(v) is list and len(v)==2 and all(type(t) is int for t in v)
    assert v[1]>0 and gcd(abs(v[0]),v[1])==1
    return Fraction(*v)

def check(path,evaluation=EVAL):
    data=json_read(path);exact_shape(data);claimed=data.pop("payload_sha256")
    assert hashlib.sha256(canonical(data)).hexdigest()==claimed,"payload hash"
    meta={"schema":"c385-lozi-evidence-v1","candidate_id":"HCS-C385","obstruction_id":"HEN-O369",
      "source_commit":"3e692da6fa94362225c7534e9b66c83c15c7f284","evaluation_date":"2026-09-05","fixed_epoch":1788566400,
      "evaluator_authority":"flow_systems/skills/route-a-evaluator.md","evaluator_version":"0.2.0",
      "evaluator_authority_sha256":"6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c",
      "scope_literal":"NO_BAD_EULER_OR_ROOT_NUMBER","scope_flags":{k:False for k in FLAGS},
      "route_a":{"tuple":TUPLE,"overall_verdict":"ROUTE_A_REJECTED","route_b_invocation_allowed":False},
      "definition":"F_a(x,y)=(1-a*abs(x)-y,x); a>4; all bounded two-sided orbits",
      "clock":"unit map iteration; derived instability suspension is a separate clock",
      "cutoffs":{"parameters":[[9,2],[5,1],[6,1]],"period_max":7},
      "controls":{"same_symbolic_counts_different_multipliers":"all three parameters",
        "prime_and_composite_exclusion":"all integers m>1; integer a>=5; rational positive clock scaling",
        "a4_boundary":"zero proven sign margin; no theorem asserted",
        "flat_germ_not_topological_zeta":"weights are abs(2-trace(M))^(-1)",
        "reversal_not_quotiented":"oriented primitive counts"},
      "nonclaims":["no sharp horseshoe boundary","no theorem for C116 pruned parameter",
        "no trace-class owner for flat germ","no irrational rescaling obstruction","no literature priority"]}
    assert set(data)==set(meta)|{"rows","summaries","primitive_rows"},"unexpected fields"
    for k,v in meta.items():assert data[k]==v and type(data[k]) is type(v),k
    # Nested dict equality alone identifies False with 0; reject that coercion.
    assert all(v is False for v in data["scope_flags"].values()),"evidence flags must be literal false"
    assert data["route_a"]["route_b_invocation_allowed"] is False,"evidence Route B must be literal false"
    wanted=[(a,n,"".join(w)) for a in (Fraction(9,2),Fraction(5),Fraction(6))
            for n in range(1,8) for w in product("01",repeat=n)]
    assert [(frac(r["a"]),r["n"],r["word"]) for r in data["rows"]]==wanted,"complete sorted rows"
    stats=defaultdict(list);expected_primitive=[]
    for r,(a,n,w) in zip(data["rows"],wanted):
        assert set(r)==set("a word n least_period necklace reversed_necklace x_cycle matrix trace flat_denominator unstable_sign".split())
        signs=[2*int(b)-1 for b in w]
        matrix=[[Fraction(0) for _ in range(n)] for _ in range(n)]
        for j in range(n):
            matrix[j][j]+=a*signs[j]
            matrix[j][(j-1)%n]+=1
            matrix[j][(j+1)%n]+=1
        xs=linear_solve(matrix,[Fraction(1)]*n)
        assert [frac(v) for v in r["x_cycle"]]==xs,"independent cyclic coordinate solve"
        delta=(a-4)/(a*(a-2));radius=1/(a-2)
        for j in range(n):
            assert delta<=signs[j]*xs[j]<=radius
            assert 1-a*abs(xs[j])-xs[(j-1)%n]==xs[(j+1)%n]
            xx,yy=xs[j],xs[(j-1)%n]
            # J F J = F^{-1}, checked directly at every point.
            def forward(v):return (1-a*abs(v[0])-v[1],v[0])
            def reverse(v):return v[::-1]
            def inverse(v):return (v[1],1-a*abs(v[1])-v[0])
            assert reverse(forward(reverse((xx,yy))))==inverse((xx,yy))
            assert inverse(forward((xx,yy)))==(xx,yy)
        d=next(k for k in range(1,n+1) if n%k==0 and all(w[j]==w[j%k] for j in range(n)))
        short=w[:d]
        neck=min(short[k:]+short[:k] for k in range(d))
        rev=short[::-1];rev=min(rev[k:]+rev[:k] for k in range(d))
        assert (r["least_period"],r["necklace"],r["reversed_necklace"])==(d,neck,rev)
        # Evolve two independent tangent vectors, not an affine return.
        columns=[]
        for start in ((Fraction(1),Fraction(0)),(Fraction(0),Fraction(1))):
            u,v=start
            for sign in signs:u,v=-a*sign*u-v,u
            columns.append((u,v))
        A,C=columns[0];B,D=columns[1]
        assert [frac(v) for v in r["matrix"]]==[A,B,C,D]
        assert A*D-B*C==1
        trace=A+D;assert abs(trace)>2 and frac(r["trace"])==trace
        assert frac(r["flat_denominator"])==abs(2-trace)
        assert r["unstable_sign"]==(-1 if trace<0 else 1)==(-1)**w.count("1")
        if a.denominator==1:
            from math import isqrt
            discr=trace.numerator**2-4
            assert trace.denominator==1 and isqrt(discr)**2!=discr
        stats[a,n].append((w,d,neck,trace,min(abs(t) for t in xs)))
        if d==n and w==neck:
            expected_primitive.append({"a":[a.numerator,a.denominator],"n":n,"word":w,"trace":r["trace"]})
    assert data["primitive_rows"]==expected_primitive
    assert [(frac(r["a"]),r["n"]) for r in data["summaries"]]==list(stats)
    previous={}
    for r in data["summaries"]:
        a,n=frac(r["a"]),r["n"];rows=stats[a,n]
        assert set(r)==set("a n fixed primitive flat_trace minimum_abs_coordinate".split())
        remaining=2**n-sum(d*previous[a,d] for d in range(1,n) if n%d==0)
        assert remaining%n==0;previous[a,n]=remaining//n
        assert r["fixed"]==len(rows)==2**n
        assert r["primitive"]==remaining//n
        assert frac(r["flat_trace"])==sum((1/abs(2-t) for _,_,_,t,_ in rows),Fraction(0))
        assert frac(r["minimum_abs_coordinate"])==min(v for _,_,_,_,v in rows)
    read_evaluation(evaluation)
    return {"affine_returns":len(wanted),"primitive_rows":len(expected_primitive),"summary_rows":len(stats),"payload":claimed}

def main():
    p=argparse.ArgumentParser();p.add_argument("evidence",nargs="?",type=Path,default=ROOT/"results/c385_lozi_evidence.json")
    p.add_argument("--evaluation",type=Path,default=EVAL);a=p.parse_args()
    print("C385 independent checker PASS: "+json.dumps(check(a.evidence,a.evaluation),sort_keys=True))
if __name__=="__main__":main()
