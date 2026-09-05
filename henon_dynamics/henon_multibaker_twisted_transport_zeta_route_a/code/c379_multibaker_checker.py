#!/usr/bin/env python3
"""Independent checker: Möbius census, direct inverse geometry, Newton series."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("c379 checker refuses optimized Python")
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
EVAL=ROOT/"evaluations/route_a/HCS-C379/2026-09-05.yaml"
EVALUATION_SEMANTIC_SHA="d3f9aa763460ccc3aae8efcefa6e3d267cb23244f82277fdd1ccbde9195e522f"
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
            assert path and path[-1] in FLAGS+("route_b_invocation_allowed","prime_label_used","even_ring_uniform_mixing","L1_relaxation_gap_defined","L2_parity_class_relaxation_mode"),"boolean substituted for numeric data"

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
    return value

def sparse(rows):
    d={}
    for row in rows:
        assert len(row)==4 and all(type(v) is int for v in row)
        a,b,p,q=row
        assert a>=0 and q>0 and p!=0 and gcd(abs(p),q)==1
        assert (a,b) not in d
        d[a,b]=Fraction(p,q)
    assert rows==[[a,b,v.numerator,v.denominator] for (a,b),v in sorted(d.items())]
    return d

def times(a,b):
    out=defaultdict(Fraction)
    for k,v in a.items():
        for l,w in b.items(): out[k+l]+=v*w
    return {k:v for k,v in out.items() if v}

def series(traces,sgn,degree):
    a=[{0:Fraction(1)}]
    for n in range(1,degree+1):
        row=defaultdict(Fraction)
        for k in range(1,n+1):
            for w,c in times(traces[k],a[n-k]).items(): row[w]+=sgn*c/n
        a.append({w:c for w,c in row.items() if c})
    return {(n,w):c for n,row in enumerate(a) for w,c in row.items()}

def check(path,evaluation=EVAL):
    x=json_read(path); exact_shape(x)
    claimed=x.pop("payload_sha256")
    assert claimed==hashlib.sha256(canonical(x)).hexdigest(),"payload hash"
    assert set(x)==set("schema candidate_id obstruction_id source_commit evaluation_date fixed_epoch evaluator_authority evaluator_version evaluator_authority_sha256 scope_literal scope_flags route_a domain clock phase weight cutoffs fixed_rows primitive_rows necklace_rows geometry_rows determinant_rows geometric_zeta_rows control_rows diffusion nonclaims".split())
    meta={"schema":"c379-multibaker-evidence-v1","candidate_id":"HCS-C379","obstruction_id":"HEN-O363","source_commit":"0596f9d680277288225062a6fdd7ad7ce116e01d","evaluation_date":"2026-09-05","fixed_epoch":1788566400,"evaluator_authority":"flow_systems/skills/route-a-evaluator.md","evaluator_version":"0.2.0","evaluator_authority_sha256":"6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c","scope_literal":"NO_BAD_EULER_OR_ROOT_NUMBER","scope_flags":{k:False for k in FLAGS},"route_a":{"tuple":TUPLE,"overall_verdict":"ROUTE_A_REJECTED","route_b_invocation_allowed":False},"domain":"cell ring times two non-dyadic coordinates in (0,1)","clock":"unit map step; unit cell length","phase":"exp(i*phi*W), W=total_displacement/L on closed cycles","weight":"inverse unstable multiplier 2^(-period), not two-dimensional flat-trace weight","cutoffs":{"ring_max":8,"period_max":12,"geometry_ring_max":6,"geometry_period_max":6},"nonclaims":["no target arithmetic carrier","no full phase-space Perron Fredholm determinant","no constructed quantization","no literature-priority claim"]}
    for k,v in meta.items(): assert x[k]==v and type(x[k]) is type(v),k
    fixed={}; trace={}; geo_trace={}; expected_rows=[]
    # Count all signed walks by dynamic programming, not binomial coefficients.
    walk={0:1}
    for n in range(1,13):
        nxt=Counter()
        for displacement,count in walk.items():
            nxt[displacement-1]+=count; nxt[displacement+1]+=count
        walk=dict(nxt)
        for L in range(1,9):
            full={S//L:L*c for S,c in walk.items() if S%L==0}
            geo=dict(full)
            if n%L==0:
                for W in (-n//L,n//L):
                    geo[W]-=L
                    if geo[W]==0: del geo[W]
            fixed[L,n]=geo
            trace[L,n]={w:Fraction(c,2**n) for w,c in full.items()}
            geo_trace[L,n]={w:Fraction(c,2**n) for w,c in geo.items()}
            expected_rows.append({"L":L,"n":n,"symbolic":[[w,c] for w,c in sorted(full.items())],"geometric":[[w,c] for w,c in sorted(geo.items())]})
    assert x["fixed_rows"]==sorted(expected_rows,key=lambda r:(r["L"],r["n"])),"complete fixed ledger"
    primitive={}; expected=[]
    for L in range(1,9):
        for n in range(1,13):
            for W,c in sorted(fixed[L,n].items()):
                residual=c
                for d in range(1,n):
                    if n%d==0 and W%(n//d)==0:
                        residual-=d*primitive.get((L,d,W//(n//d)),0)
                assert residual>=0 and residual%n==0
                if residual:
                    primitive[L,n,W]=residual//n
                    expected.append({"L":L,"q":n,"W":W,"count":residual//n})
    assert x["primitive_rows"]==expected,"independent primitive-power inversion"
    necklace=[]
    for d in range(2,13):
        for bits in product("01",repeat=d):
            w="".join(bits)
            if w.count("1") in (0,d): continue
            if any(w==w[:k]*(d//k) for k in range(1,d) if d%k==0): continue
            if any(w[k:]+w[:k]<w for k in range(1,d)): continue
            S=sum(1 if b=="1" else -1 for b in bits)
            rev="".join(str(1-int(b)) for b in reversed(bits))
            for L in range(1,9):
                h=next(k for k in range(1,L+1) if k*S%L==0)
                if d*h>12: continue
                necklace.append({"L":L,"word":w,"d":d,"S":S,"q":d*h,"W":h*S//L,"multiplicity":L//h,"reversed_necklace":min(rev[k:]+rev[:k] for k in range(d))})
    assert x["necklace_rows"]==necklace,"necklace lift or reversal"
    wanted={(L,n,"".join(w)) for L in range(1,7) for n in range(2,7) for w in product("01",repeat=n) if 0<w.count("1")<n and (2*w.count("1")-n)%L==0}
    seen=set()
    for r in x["geometry_rows"]:
        assert set(r)==set("L n word x y cells W unstable stable flat_denominator".split())
        L,n,w=r["L"],r["n"],r["word"]
        key=(L,n,w); assert key in wanted and key not in seen; seen.add(key)
        xx,yy=Fraction(*r["x"]),Fraction(*r["y"])
        assert 0<xx<1 and 0<yy<1
        assert xx.denominator%2 and yy.denominator%2
        start=(0,xx,yy); cur=start; cells=[]; itinerary=[]
        def forward(p):
            j,a,b=p; s=int(2*a)
            return ((j+2*s-1)%L,2*a-s,(b+s)/2)
        def inverse(p):
            j,a,b=p; t=int(2*b)
            return ((j-(2*t-1))%L,(a+t)/2,2*b-t)
        def reversal(p):
            j,a,b=p; return (j,1-b,1-a)
        for _ in range(n):
            cells.append(cur[0]); itinerary.append(str(int(2*cur[1])))
            assert inverse(forward(cur))==cur
            assert reversal(forward(reversal(cur)))==inverse(cur),"IBI inverse"
            cur=forward(cur)
        assert cur==start and "".join(itinerary)==w and cells==r["cells"]
        assert r["W"]==sum(2*int(s)-1 for s in w)//L
        assert r["unstable"]==2**n and r["stable"]==[1,2**n]
        assert Fraction(*r["flat_denominator"])==abs((1-Fraction(2**n))*(1-Fraction(1,2**n)))
    assert seen==wanted,"geometry omission"
    assert [r["L"] for r in x["determinant_rows"]]==list(range(1,9))
    assert [r["L"] for r in x["geometric_zeta_rows"]]==list(range(1,9))
    for r in x["determinant_rows"]:
        L=r["L"]; assert set(r)=={"L","coefficients"}
        assert sparse(r["coefficients"])==series({n:trace[L,n] for n in range(1,13)},-1,L),"Newton determinant"
    for r in x["geometric_zeta_rows"]:
        L=r["L"]; assert set(r)=={"L","coefficients"}
        assert sparse(r["coefficients"])==series({n:geo_trace[L,n] for n in range(1,13)},1,12),"geometric zeta exponential"
    controls=[{"L":L,"prime_label_used":False,"relabel_cell_map":[(j+1)%L for j in range(L)],"neighbor_ring":L+1,"untilted_period":1 if L%2 else 2,"boundary_fixed_excess_at_nL":2*L,"lazy_gap_formula":"not_defined" if L==1 else "sin(pi/L)^2"} for L in range(1,9)]
    assert x["control_rows"]==controls
    assert x["diffusion"]=={"mean_per_step":0,"variance_per_step":1,"D":[1,2],"log_cos_coefficients":[[2,-1,2],[4,-1,12]],"even_ring_uniform_mixing":False,"L1_relaxation_gap_defined":False,"L2_parity_class_relaxation_mode":False}
    read_evaluation(evaluation)
    return {"fixed":len(expected_rows),"primitive":len(expected),"geometry":len(seen),"necklaces":len(necklace),"payload":claimed}

def main():
    p=argparse.ArgumentParser(); p.add_argument("evidence",nargs="?",type=Path,default=ROOT/"results/c379_multibaker_evidence.json"); p.add_argument("--evaluation",type=Path,default=EVAL); a=p.parse_args()
    print("C379 independent checker PASS: "+json.dumps(check(a.evidence,a.evaluation),sort_keys=True))

if __name__=="__main__":main()
