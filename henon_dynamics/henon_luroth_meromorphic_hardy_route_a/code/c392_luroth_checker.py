#!/usr/bin/env python3
"""Independent reconstruction: never imports the evidence producer."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("c392 checker refuses optimized Python")
import argparse, hashlib, json
from fractions import Fraction as F
from pathlib import Path
from math import gcd, prod
from collections import Counter
from itertools import product
import yaml
ROOT=Path(__file__).resolve().parents[1]
EVAL=ROOT/"evaluations/route_a/HCS-C392/2026-09-05.yaml"
EVALUATION_SEMANTIC_SHA="8c3a29f7b68cfbca07800290bcc8eeb7ba5e6466cda9df0832c8a58156c7006e"
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
    return {"schema":"hcs-exact-evidence-v1","candidate_id":"HCS-C392","source_commit":"0c877206d202f732e21ea0b194f9c7fdf30467ee","fixed_epoch":1788566400,"scope_literal":"NO_BAD_EULER_OR_ROOT_NUMBER","scope_flags":{k:False for k in FLAGS},"route_a":{"tuple":["A0_FAIL","A1_WEAK","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"],"overall_verdict":"ROUTE_A_REJECTED","route_b_invocation_allowed":False},"evidence_role":"finite exact regression; not an infinite theorem or target match"}

def pmul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c
def tmul(a,b,L):
    c=[[F(0)] for _ in range(L+1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j>L:continue
            v=pmul(x,y)
            c[i+j]+=[F(0)]*max(0,len(v)-len(c[i+j]))
            for k,z in enumerate(v):c[i+j][k]+=z
    return c
def rank(M):
    M=[row[:] for row in M];r=0
    for j in range(len(M[0])):
        k=next((k for k in range(r,len(M)) if M[k][j]),None)
        if k is None:continue
        M[r],M[k]=M[k],M[r];scale=M[r][j];M[r]=[v/scale for v in M[r]]
        for k in range(len(M)):
            if k!=r:
                scale=M[k][j];M[k]=[a-scale*b for a,b in zip(M[k],M[r])]
        r+=1
    return r
def math_check(d):
    expected_branches=[]
    for n in range(1,13):
        a=F(1,n*(n+1));b=F(1,n+1)
        expected_branches.append({"n":n,"slope":q(a),"offset":q(b),"disk_ratio":q((b+2*a)/2)})
    assert d["branches"]==expected_branches
    assert len(d["matrices"])==16
    cells=0
    for row,(s,N) in zip(d["matrices"],product(range(1,5),(1,2,4,8))):
        M=[[F(0) for _ in range(7)] for _ in range(7)]
        for n in range(1,N+1):
            a=F(1,n*(n+1));b=F(1,n+1);power=[F(1)]
            for j in range(7):
                for i,v in enumerate(power):M[i][j]+=a**s*v
                power=pmul(power,[b,a])
        assert row=={"s":s,"N":N,"dimension":7,"matrix":[[q(v) for v in r] for r in M],"diagonal":[q(M[j][j]) for j in range(7)]}
        cells+=49
    assert len(d["residues"])==10
    for l,row in enumerate(d["residues"]):
        s=F(1-l,2);h=[[F(0)] for _ in range(l+1)]
        for k in range(1,l+1):
            h[k]=[F(1,4**((k-1)//2))] if k%2 else [F(-1,2*4**((k-2)//2)),F(1,4**((k-2)//2))]
        weight=[[F(0)] for _ in range(l+1)];v=F(1)
        for r in range(l//2+1):
            if r:v*=F(s+r-1,4*r)
            weight[2*r]=[v]
        power=[[F(1)]]+[[F(0)] for _ in range(l)]
        M=[[F(0) for _ in range(l+1)] for _ in range(l+1)]
        for j in range(l+1):
            col=tmul(weight,power,l)[l]
            for i,v in enumerate(col):M[i][j]=v/2
            power=tmul(power,h,l)
        assert row=={"l":l,"pole":q(s),"rank":l//2+1,"kind":"square_zero" if l%2 else "nonzero_diagonal","matrix":[[q(v) for v in r] for r in M]}
        assert rank(M)==l//2+1
        if l%2:assert all(sum((M[i][k]*M[k][j] for k in range(l+1)),F(0))==0 for i in range(l+1) for j in range(l+1))
        cells+=(l+1)**2
    r=F(1,2);expected=[]
    for m in range(10):
        if m:r*=-F(2*m-1,8*m)
        expected.append({"m":m,"pole":q(F(1,2)-m),"residue":q(r),"determinant_pole_order":m+1})
    assert d["scalar_poles"]==expected
    words=[w for r in range(1,5) for w in product(range(1,5),repeat=r)]
    assert len(d["words"])==len(words)
    for row,w in zip(d["words"],words):
        A=F(1);B=F(0)
        # Compose affine maps from the other end than the producer.
        for n in w:B+=A*F(1,n+1);A*=F(1,n*(n+1))
        x=B/(1-A);start=x
        for n in w:
            assert F(1,n+1)<x<=F(1,n)
            x=n*(n+1)*x-n
        assert x==start
        least=len(w)
        for k in range(1,len(w)+1):
            if all(w[i]==w[(i+k)%len(w)] for i in range(len(w))):least=k;break
        assert row=={"word":list(w),"slope":q(A),"point":q(start),"least_period":least,"necklace":list(min(w[k:]+w[:k] for k in range(len(w)))),"trace_s1":q(A/(1-A))}
    assert d["controls"]=={"isolated_zero":"not branch weighted","s_half":"branch sum diverges","s_zero_residue_on_z":q(F(1,2)),"s_zero_residue_on_one":q(0),"s_one_sum":q(1),"tail_after_N_at_s1":[{"N":N,"tail":q(1-sum((F(1,n)-F(1,n+1) for n in range(1,N+1)),F(0)))} for N in (1,2,4,8,16)],"source_slopes":"n(n+1) composite for n>=2, not a prime list"}
    return {"matrix_cells":cells,"word_rows":len(words),"residue_ranks":10}
DATA_KEYS={"branches","matrices","residues","scalar_poles","words","controls"}

def check(path,evaluation_path=EVAL):
    data=read(path);exact_shape(data);digest=data.pop("payload_sha256")
    assert type(digest) is str and len(digest)==64 and hashlib.sha256(canonical(data)).hexdigest()==digest
    meta=metadata();assert set(data)==set(meta)|DATA_KEYS
    for k,v in meta.items():assert data[k]==v,f"metadata {k}"
    assert all(v is False for v in data["scope_flags"].values()) and data["route_a"]["route_b_invocation_allowed"] is False
    result=math_check(data);evaluation(evaluation_path)
    result["payload"]=digest;return result
def main():
    p=argparse.ArgumentParser();p.add_argument("evidence",nargs="?",type=Path,default=ROOT/"results/c392_luroth_evidence.json");p.add_argument("--evaluation",type=Path,default=EVAL);a=p.parse_args()
    print("C392 independent checker PASS: "+json.dumps(check(a.evidence,a.evaluation),sort_keys=True))
if __name__=="__main__":main()
