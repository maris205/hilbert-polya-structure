#!/usr/bin/env python3
"""Independent reconstruction: never imports the evidence producer."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("c397 checker refuses optimized Python")
import argparse, hashlib, json
from fractions import Fraction as F
from pathlib import Path
from math import gcd, prod
from collections import Counter
from itertools import product
import yaml
ROOT=Path(__file__).resolve().parents[1]
EVAL=ROOT/"evaluations/route_a/HCS-C397/2026-09-05.yaml"
EVALUATION_SEMANTIC_SHA="66a8374b2444b604cf17935a7323f0a702cd8daabf51de793a73c98fd28c06c8"
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

def metadata():return {'schema':'hcs-exact-evidence-v1','candidate_id':'HCS-C397','source_commit':'697518b6db90458f86f7916fbf397b8ad5ef2372','fixed_epoch':1788566400,'scope_literal':'NO_BAD_EULER_OR_ROOT_NUMBER','scope_flags':{k:False for k in FLAGS},'route_a':{'tuple':['A0_WEAK_ARITHMETIC_RELATION','A1_WEAK','A2_FAIL','A3_FAIL','A4_FORMAL_HINT'],'overall_verdict':'ROUTE_A_REJECTED','route_b_invocation_allowed':False},'evidence_role':'finite exact regression; not an infinite theorem or target match'}

def math_check(d):
    import sympy as s
    from sympy.matrices.normalforms import smith_normal_form
    X,z=s.symbols('X z');assert len(d['families'])==5;cells=0
    for row,a in zip(d['families'],(1,3,4,5,8)):
        A=s.Matrix([[0,0,0,-1],[1,0,0,a],[0,1,0,1],[0,0,1,a]])
        P=X**4-a*X**3-X**2-a*X+1
        assert s.Poly(P,X).is_irreducible
        def coeff(f):return [int(s.expand(f).coeff(z,i)) for i in range(9)]
        assert set(row)=={'a','matrix','polynomial','zeta_numerator','zeta_denominator','periods'}
        assert row['a']==a and row['matrix']==[list(map(int,A.row(i))) for i in range(4)]
        assert row['polynomial']==[1,-a,-1,-a,1]
        assert row['zeta_numerator']==coeff((1-z)**4*(1+3*z+(a*a+4)*z*z+3*z**3+z**4))
        assert row['zeta_denominator']==coeff((1-a*z-z*z-a*z**3+z**4)**2)
        # Newton power sums of the characteristic polynomial, not determinant expansion.
        power=[4,a,a*a+2,a**3+6*a]
        for j in range(4,49):power.append(a*power[j-1]+power[j-2]+a*power[j-3]-power[j-4])
        fixed={j:2*power[j]-2-(power[j]**2-power[2*j])//2 for j in range(1,25)}
        assert len(row['periods'])==24
        for r,n in zip(row['periods'],range(1,25)):
            M=A**n-s.eye(4);S=smith_normal_form(M,domain=s.ZZ)
            smith=[abs(int(S[i,i])) for i in range(4)]
            count=sum(int(s.mobius(n//j))*fixed[j] for j in s.divisors(n))//n
            assert r=={'n':n,'return_matrix':[list(map(int,M.row(i))) for i in range(4)],'signed_determinant':-fixed[n],'fixed':fixed[n],'smith':smith,'primitive_cycles':count}
            assert prod(smith)==fixed[n] and all(smith[j+1]%smith[j]==0 for j in range(3))
            assert count>=0
            cells+=16
    A=s.Matrix([[0,0,0,-1],[1,0,0,2],[0,1,0,1],[0,0,1,2]])
    assert len(d['boundary'])==12
    for row,n in zip(d['boundary'],range(1,13)):
        M=A**n-s.eye(4);v=int(M.det());nullity=4-M.rank()
        assert row=={'a':2,'n':n,'signed_determinant':v,'identity_component_dimension':nullity,'cardinality':'infinite' if nullity else str(abs(v))}
    assert d['controls']=={'primitive_limit_mean':[2,1],'primitive_limit_variance':[2,1],'primitive_cluster_endpoints':[[0,1],[4,1]],'homoclinic_group':'trivial for all a>=1,a!=2','clock':'integer iteration, not log-prime','zeta_not_koopman_determinant':'unitary infinite-dimensional Koopman is noncompact'}
    return {'parameter_families':5,'period_groups':120,'matrix_cells':cells,'cyclotomic_controls':12}
DATA_KEYS={'families','boundary','controls'}

def check(path,evaluation_path=EVAL):
    data=read(path);exact_shape(data);digest=data.pop("payload_sha256")
    assert type(digest) is str and len(digest)==64 and hashlib.sha256(canonical(data)).hexdigest()==digest
    meta=metadata();assert set(data)==set(meta)|DATA_KEYS
    for k,v in meta.items():assert data[k]==v,f"metadata {k}"
    assert all(v is False for v in data["scope_flags"].values()) and data["route_a"]["route_b_invocation_allowed"] is False
    result=math_check(data);evaluation(evaluation_path)
    result["payload"]=digest;return result
def main():
    p=argparse.ArgumentParser();p.add_argument("evidence",nargs="?",type=Path,default=ROOT/"results/c397_salem_evidence.json");p.add_argument("--evaluation",type=Path,default=EVAL);a=p.parse_args()
    print("C397 independent checker PASS: "+json.dumps(check(a.evidence,a.evaluation),sort_keys=True))
if __name__=="__main__":main()
