#!/usr/bin/env python3
"""Independent reconstruction: never imports the evidence producer."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("c398 checker refuses optimized Python")
import argparse, hashlib, json
from fractions import Fraction as F
from pathlib import Path
from math import gcd, prod
from collections import Counter
from itertools import product
import yaml
ROOT=Path(__file__).resolve().parents[1]
EVAL=ROOT/"evaluations/route_a/HCS-C398/2026-09-05.yaml"
EVALUATION_SEMANTIC_SHA="b00534e2f9c8a2225450eeb58dbdea37a010a5ac1f721d46c07ce59ed720a0fa"
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

def metadata():return {'schema':'hcs-exact-evidence-v1','candidate_id':'HCS-C398','source_commit':'697518b6db90458f86f7916fbf397b8ad5ef2372','fixed_epoch':1788566400,'scope_literal':'NO_BAD_EULER_OR_ROOT_NUMBER','scope_flags':{k:False for k in FLAGS},'route_a':{'tuple':['A0_FAIL','A1_FAIL','A2_FAIL','A3_FAIL','A4_NATURAL_QUANTIZATION'],'overall_verdict':'ROUTE_A_REJECTED','route_b_invocation_allowed':False},'evidence_role':'finite exact regression; not an infinite theorem or target match'}

def math_check(d):
    import sympy as s
    assert len(d['series'])==12 and len(d['tails'])==12 and len(d['actions'])==16
    def enc(x):
        x=s.Rational(x);return [int(x.p),int(x.q)]
    index=0;terms=0
    for a in (s.Rational(1,2),s.Integer(1),s.Integer(2),s.Integer(3)):
        for k in (8,16,32):
            row=d['series'][index];expected=[]
            for j in range(9):
                value=s.expand_complex((a*a/4)**j/(s.factorial(j)*s.rf(1-s.I*k,j)))
                expected.append([enc(s.re(value)),enc(s.im(value))])
            assert row=={'a':enc(a),'k':k,'terms':expected}
            h=a*a/(4*k);assert 0<h<1
            assert d['tails'][index]=={'a':enc(a),'k':k,'h':enc(h),'series_minus_one_bound':enc(h/(1-h)),'series_derivative_bound':enc(h/(k*(1-h)**2))}
            index+=1;terms+=9
    index=0
    for a in (s.Rational(1,2),s.Integer(1),s.Integer(2),s.Integer(3)):
        for r in (s.Rational(3,2),s.Integer(2),s.Integer(3),s.Integer(5)):
            k=a*s.cosh(s.log(r)).rewrite(s.exp)
            k=s.simplify(k);root=s.sqrt(k*k-a*a)
            assert d['actions'][index]=={'a':enc(a),'r':enc(r),'k':enc(k),'sqrt_energy_minus_a2':enc(root),'action_log_coefficient':enc(2*k),'action_constant':enc(-2*root),'period_log_coefficient':enc(1/k)}
            index+=1
    assert d['controls']=={'energy_order':[1,2],'schatten_threshold_strict':[1,2],'spectral_zeta_double_pole':[1,2],'double_pole_coefficient_times_pi':[1,4],'heat_log_coefficient_times_sqrt_pi':[1,4],'forced_frequency_scale':[1,2],'forced_a_over_pi':[2,1],'a_zero':'free Dirichlet half-line; no compact resolvent','normalizations':'all fixed a,c>0,b real in E=c^2 T^2+b; not arbitrary nonlinear changes','external_input':'Dobner arXiv:2101.01747v2 equation(1),Theorem1; unconditional unbounded S(T)'}
    return {'complex_rational_terms':terms,'action_rows':16,'tail_bound_rows':12}
DATA_KEYS={'series','actions','tails','controls'}

def check(path,evaluation_path=EVAL):
    data=read(path);exact_shape(data);digest=data.pop("payload_sha256")
    assert type(digest) is str and len(digest)==64 and hashlib.sha256(canonical(data)).hexdigest()==digest
    meta=metadata();assert set(data)==set(meta)|DATA_KEYS
    for k,v in meta.items():assert data[k]==v,f"metadata {k}"
    assert all(v is False for v in data["scope_flags"].values()) and data["route_a"]["route_b_invocation_allowed"] is False
    result=math_check(data);evaluation(evaluation_path)
    result["payload"]=digest;return result
def main():
    p=argparse.ArgumentParser();p.add_argument("evidence",nargs="?",type=Path,default=ROOT/"results/c398_wall_evidence.json");p.add_argument("--evaluation",type=Path,default=EVAL);a=p.parse_args()
    print("C398 independent checker PASS: "+json.dumps(check(a.evidence,a.evaluation),sort_keys=True))
if __name__=="__main__":main()
