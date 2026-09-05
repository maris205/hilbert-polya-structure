#!/usr/bin/env python3
"""Independent analytic receipt reconstruction: no producer import."""
if not __debug__:
    raise RuntimeError("c386 checker refuses optimized Python")
import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
import mpmath as mp
import yaml

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"results/c386_szego_evidence.json"
YAML=ROOT/"evaluations/route_a/HCS-C386/2026-09-05.yaml"
YAML_SHA="f8c7b832fc5756a6e6adcaf7ad6369648e2fadf97d357347d4e762012649687e"
EXPECTED_FLAGS={"claims_target_arithmetic_local_data","claims_target_euler_factors","claims_root_number","claims_automorphy","claims_target_divisor_or_counting_law","claims_target_functional_equation","claims_target_zero_match","claims_hilbert_polya_operator","invokes_route_b"}

def canon(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False).encode()
def pairs(rows):
    result={}
    for k,v in rows:
        if k in result:raise ValueError("duplicate JSON key")
        result[k]=v
    return result
def reject(x):raise ValueError("nonfinite JSON")
def strict_json(path):return json.loads(path.read_text(),object_pairs_hook=pairs,parse_constant=reject)
def rational(x):
    assert type(x) is list and len(x)==2 and all(type(y) is int for y in x) and x[1]>0
    value=Fraction(*x)
    assert [value.numerator,value.denominator]==x
    return value

class StrictYAML(yaml.SafeLoader):pass
StrictYAML.yaml_implicit_resolvers={k:[(t,r) for t,r in v if t!="tag:yaml.org,2002:timestamp"] for k,v in yaml.SafeLoader.yaml_implicit_resolvers.items()}
def yamlmap(loader,node,deep=False):
    d={}
    for k,v in node.value:
        if k.tag=="tag:yaml.org,2002:merge":raise ValueError("YAML merge")
        key=loader.construct_object(k,deep=deep)
        if type(key)is not str or key in d:raise ValueError("YAML duplicate/nonstring key")
        d[key]=loader.construct_object(v,deep=deep)
    return d
StrictYAML.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,yamlmap)
def strict_yaml(path):
    raw=path.read_bytes()
    for token in yaml.scan(raw):
        if isinstance(token,(yaml.tokens.AnchorToken,yaml.tokens.AliasToken)):raise ValueError("YAML alias/anchor")
    return yaml.load(raw,Loader=StrictYAML)

def check_yaml_lock():
    raw=YAML.read_bytes();evaluation=strict_yaml(YAML)
    assert hashlib.sha256(raw).hexdigest()==YAML_SHA,"evaluation changed"
    assert type(evaluation)is dict
    assert type(evaluation["evaluation_date"])is str and evaluation["evaluation_date"]=="2026-09-05"
    assert set(evaluation["scope_flags"])==EXPECTED_FLAGS
    assert all(v is False for v in evaluation["scope_flags"].values())
    assert evaluation["route_b_invocation_allowed"] is False
    return raw,evaluation

import sympy as sp
I=sp.I
def scalar(x):
    x=sp.cancel(sp.expand_complex(x));assert x.is_Rational
    return [int(sp.numer(x)),int(sp.denom(x))]
def complex_pair(x):return [scalar(sp.re(sp.expand_complex(x))),scalar(sp.im(sp.expand_complex(x)))]
def mod2(x):return sp.expand(x*sp.conjugate(x))
def independent_row(a,b,c,p):
    a,b,c,p=map(sp.sympify,(a,b,c,p));d=1-mod2(p);C=mod2(c);B=mod2(b)
    mass=sp.cancel(B+C/d);momentum=sp.cancel(C/d**2)
    # Factored defect is independent of producer's expanded quartic energy.
    defect=sp.cancel(momentum*d*(mod2(b+c*sp.conjugate(p)/d)-a)/2)
    energy=sp.cancel(defect+mass**2/4+a*mass/2)
    v_b=sp.expand(-I*((B+2*C/d+a)*b+momentum*c*sp.conjugate(p)))
    v_c=sp.expand(-I*((2*B+momentum)*c+2*b*C*p/d))
    v_p=sp.expand(-I*(c*sp.conjugate(b)+C*p/d))
    d1=sp.expand(-2*sp.re(v_p*sp.conjugate(p)))
    C1=sp.expand(2*sp.re(v_c*sp.conjugate(c)))
    # Differentiate the p equation, rather than producer's X=b*p*conj(c).
    p2=sp.expand(-I*(v_c*sp.conjugate(b)+c*sp.conjugate(v_b)+
                     (C1/d-C*d1/d**2)*p+C*v_p/d))
    d2=sp.expand(-2*(mod2(v_p)+sp.re(p2*sp.conjugate(p))))
    assert sp.cancel(2*sp.re(v_b*sp.conjugate(b))+C1/d-C*d1/d**2)==0
    assert sp.cancel(C1/d**2-2*C*d1/d**3)==0
    k2=sp.cancel(4*mass*momentum-(a-mass-momentum)**2)
    kind="cascade" if a>0 and defect==0 else "inner_phase" if a==0 and defect==0 else "compact"
    lower=2*abs(defect)/(momentum*(2*(mass+momentum)+abs(a))) if defect else 0
    if kind=="cascade":
        assert k2>0 and 0<k2/(4*a*momentum)<=1
        assert sp.cancel(d1**2-d*d*(k2-4*a*momentum*d))==0
        assert sp.cancel(d2-(k2*d-6*a*momentum*d*d))==0
    if kind=="inner_phase":
        assert sp.cancel(v_p)==0 and sp.expand(v_b+I*mass*b)==0 and sp.expand(v_c+I*mass*c)==0
    return dict(alpha=scalar(a),b=complex_pair(b),c=complex_pair(c),p=complex_pair(p),
        d=scalar(d),Q=scalar(mass),M=scalar(momentum),energy=scalar(energy),defect=scalar(defect),
        velocity=[complex_pair(x) for x in (v_b,v_c,v_p)],d_dot=scalar(d1),d_ddot=scalar(d2),
        kappa_squared=scalar(k2),d_star=scalar(k2/(4*a*momentum)) if kind=="cascade" else None,
        compact_lower_bound=scalar(lower),regime=kind,
        native_determinant_coefficients=[scalar(1),scalar(-momentum)])
def expected_rows():
    R=sp.Rational
    alphas=[-2,-1,0,R(1,4),1,4];bs=[0,1,I,(1+I)/2];cs=[R(1,2),(1+I)/3];ps=[0,R(1,3),I/2]
    generic=[independent_row(a,b,c,p) for a in alphas for b in bs for c in cs for p in ps]
    threshold=[]
    for root in (R(1,2),1,2):
      for amplitude in (R(1,2),1):
       for eta in (1,I):
        for phase in (1,(3+4*I)/5):
         for p in ps:
          d=1-mod2(p)
          threshold.append(independent_row(root**2,root*phase-amplitude*eta*sp.conjugate(p),
                                           amplitude*eta*d,p))
    inner=[independent_row(0,-m*eta*sp.conjugate(p),m*eta*(1-mod2(p)),p)
           for m in (R(1,2),1) for eta in (1,I) for p in ps]
    constants=[]
    for a in alphas:
      for b in bs:
        Q=mod2(b);freq=Q+a
        constants.append(dict(alpha=scalar(a),b=complex_pair(b),Q=scalar(Q),
             energy=scalar(Q*Q/4+a*Q/2),defect=scalar(0),frequency=scalar(freq),
             stationary=bool(Q==0 or freq==0),rank=0,cascade=False))
    controls=[dict(alpha=scalar(r*r),bounded=independent_row(r*r,0,1,0),
                   cascade=independent_row(r*r,r,1,0)) for r in (R(1,2),1,2)]
    return generic,threshold,inner,constants,controls
def check(path):
    data=strict_json(path)
    expected_keys={"schema","candidate_id","obstruction_id","source_commit","fixed_epoch","scope_literal",
        "scope_flags","evaluator","route_a_yaml","route_a","generic_rows","cascade_rows","inner_rows",
        "constant_rows","control_rows","counts","theorem_boundary","payload_sha256"}
    assert set(data)==expected_keys
    payload=data.pop("payload_sha256")
    assert type(payload)is str and payload==hashlib.sha256(canon(data)).hexdigest(),"payload hash"
    assert data["schema"]=="hcs-c386-szego-v1" and data["candidate_id"]=="HCS-C386" and data["obstruction_id"]=="HEN-O370"
    assert data["source_commit"]=="3e692da6fa94362225c7534e9b66c83c15c7f284"
    assert type(data["fixed_epoch"])is int and data["fixed_epoch"]==1788566400
    assert data["scope_literal"]=="NO_BAD_EULER_OR_ROOT_NUMBER"
    assert set(data["scope_flags"])==EXPECTED_FLAGS and all(v is False for v in data["scope_flags"].values())
    assert data["evaluator"]=={"authority":"flow_systems/skills/route-a-evaluator.md","version":"0.2.0",
                              "sha256":"6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"}
    raw,ev=check_yaml_lock()
    assert data["route_a_yaml"]=={"path":"evaluations/route_a/HCS-C386/2026-09-05.yaml","raw_sha256":YAML_SHA,
                                "semantic_sha256":hashlib.sha256(canon(ev)).hexdigest()}
    expected_route={"tuple":["A0_FAIL","A1_FAIL","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"],
                    "overall_verdict":"ROUTE_A_REJECTED","route_b_invocation_allowed":False}
    assert canon(data["route_a"])==canon(expected_route) and ev["tuple"]==expected_route["tuple"]
    assert ev["scope_flags"]==data["scope_flags"]
    expected_counts=dict(generic=144,cascade=72,inner=12,constants=24,controls=3)
    assert canon(data["counts"])==canon(expected_counts)
    groups=expected_rows()
    for name,rows in zip(("generic_rows","cascade_rows","inner_rows","constant_rows","control_rows"),groups):
        assert type(data[name])is list and len(data[name])==len(rows),name
        for i,(actual,expected) in enumerate(zip(data[name],rows)):
            assert canon(actual)==canon(expected),(name,i)
    assert data["theorem_boundary"]=="Rank one only; constants separately; physical time unchanged; finite rational checks are regression, not all-mode proofs; auxiliary K squared determinant is not time evolution; no target arithmetic or Route B"
    return payload
def main():
    p=argparse.ArgumentParser();p.add_argument("path",type=Path,nargs="?",default=OUT);p.add_argument("--yaml-only",action="store_true");a=p.parse_args()
    if a.yaml_only:check_yaml_lock();print("C386 locked strict YAML PASS");return
    print("C386 independent checker PASS",check(a.path))
if __name__=="__main__":main()
