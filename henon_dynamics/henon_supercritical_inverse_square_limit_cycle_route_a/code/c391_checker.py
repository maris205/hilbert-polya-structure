#!/usr/bin/env python3
"""Independent reconstruction, including strict scalar types; never imports producer."""
if not __debug__: raise RuntimeError("c391 checker refuses optimized Python")
import argparse
import hashlib
import json
import re
from fractions import Fraction
from pathlib import Path
import mpmath as mp
import sympy as sp
import yaml
ROOT=Path(__file__).resolve().parents[1]
YAML=ROOT/"evaluations/route_a/HCS-C391/2026-09-05.yaml"
YAML_SHA="93de77babcb16fc698d687a35584124eb110a3fba10ce454c77abcd9b8197bbb"
BASE="0c877206d202f732e21ea0b194f9c7fdf30467ee"
AUTH="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
FLAGS={"claims_target_arithmetic_local_data","claims_target_euler_factors","claims_root_number","claims_automorphy","claims_target_divisor_or_counting_law","claims_target_functional_equation","claims_target_zero_match","claims_hilbert_polya_operator","invokes_route_b"}
TUPLE=["A0_FAIL","A1_FAIL","A2_FAIL","A3_FAIL","A4_NATURAL_QUANTIZATION"]
def canon(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False).encode()
def same(a,b):assert canon(a)==canon(b),(a,b)
def pairs(rows):
    d={}
    for k,v in rows:
        if k in d:raise ValueError("duplicate JSON key")
        d[k]=v
    return d
def bad(x):raise ValueError("nonfinite JSON")
def strict_json(path):return json.loads(path.read_text(),object_pairs_hook=pairs,parse_constant=bad)
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
def check_yaml(path=YAML):
    raw=path.read_bytes()
    for token in yaml.scan(raw):
        if isinstance(token,(yaml.tokens.AnchorToken,yaml.tokens.AliasToken)):raise ValueError("YAML anchor/alias")
    ev=yaml.load(raw,Loader=StrictYAML)
    assert type(ev)is dict and type(ev["evaluation_date"])is str
    assert set(ev["scope_flags"])==FLAGS and all(x is False for x in ev["scope_flags"].values())
    assert ev["route_b_invocation_allowed"] is False and ev["a4"]["metrics"]["route_b_ready"] is False
    same(ev["tuple"],TUPLE);assert ev["overall_verdict"]=="ROUTE_A_REJECTED"
    assert hashlib.sha256(raw).hexdigest()==YAML_SHA,"locked YAML raw bytes changed"
    return ev
def rational(x):
    assert type(x)is list and len(x)==2 and all(type(y)is int for y in x) and x[1]>0
    r=Fraction(*x);same([r.numerator,r.denominator],x);return r
def q(x):
    x=sp.cancel(x);assert x.is_Rational;return [int(sp.numer(x)),int(sp.denom(x))]
def z(x):return [q(sp.re(sp.expand_complex(x))),q(sp.im(sp.expand_complex(x)))]
def exact_expected():
    Q=sp.Rational;I=sp.I;ss=(Q(1,2),sp.Integer(1),sp.Integer(2));unit=(1,-1,I,-I,(3+4*I)/5)
    cl=[];bd=[];sc=[]
    for s in ss:
      for x in (Q(1,2),sp.Integer(1),sp.Integer(2)):
       for p in map(sp.Integer,(-2,-1,0,1,2)):
        g=s*s+Q(1,4);energy=p*p-g/x**2
        # Differentiate Hamilton equations symbolically: y''=8h.
        cl.append(dict(sigma=q(s),x=q(x),p=q(p),g=q(g),energy=q(energy),y_coefficients=[q(x*x),q(4*x*p),q(4*energy)],
          discriminant=q(16*g),finite_collision=True,periodic=False,clock_component="bounded_interval" if energy<0 else "half_line"))
      for k in unit+(0,Q(1,2),2,1+I):
        n=sp.expand_complex(k*sp.conjugate(k))
        bd.append(dict(sigma=q(s),kappa=z(k),flux_over_i=q(2*s*(1-n)),self_adjoint=bool(n==1)))
    for h in map(sp.Integer,(2,3,5)):
      for t in unit:
        # Incoming/outgoing coefficient solve rather than producer complex division.
        reflection=sp.simplify(I*(h-t)/(h*t-1))
        assert sp.simplify(reflection*sp.conjugate(reflection))==1
        sc.append(dict(exp_pi_sigma=q(h),t=z(t),reflection=z(reflection),relative_scattering=z(-reflection),unitary=True))
    return cl,bd,sc
def number(x):
    assert type(x)is str and re.fullmatch(r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?",x)
    v=mp.mpf(x);assert mp.isfinite(v);return v
def complex_number(x):
    assert type(x)is list and len(x)==2;return number(x[0])+1j*number(x[1])
def close(a,b):assert abs(a-b)<=mp.mpf("2e-57")*max(1,abs(b)),(a,b)
def check_numbers(levels,waves):
    mp.mp.dps=110;index=0;wi=0
    assert type(levels)is list and len(levels)==60 and type(waves)is list and len(waves)==36
    for sq in ((1,2),(1,1),(2,1)):
      s=mp.mpf(sq[0])/sq[1]
      for hq in ((0,1),(1,3),(1,1),(5,3)):
        theta=mp.pi*hq[0]/hq[1];kappa=mp.exp(1j*theta)*mp.gamma(1j*s)/mp.gamma(-1j*s)
        for j in range(-2,3):
          row=levels[index];index+=1
          assert set(row)=={"sigma","phase_pi","j","kappa","log_rho","energy","normalizer"}
          same(row["sigma"],list(sq));same(row["phase_pi"],list(hq));assert type(row["j"])is int and row["j"]==j
          logr=number(row["log_rho"]);rho=mp.exp(logr);close(2*s*(logr-mp.log(2)),-theta-2*mp.pi*j)
          close(complex_number(row["kappa"]),kappa)
          close(mp.gamma(1j*s)/mp.gamma(-1j*s)*mp.exp(-2j*s*(logr-mp.log(2))),kappa)
          close(number(row["energy"]),-rho*rho)
          close(number(row["normalizer"]),rho*mp.sqrt(2*mp.sinh(mp.pi*s)/(mp.pi*s)))
        for kq in ((1,3),(1,1),(3,1)):
          row=waves[wi];wi+=1
          assert set(row)=={"sigma","phase_pi","momentum","reflection","relative_scattering","phi_at_7_over_10","density"}
          same(row["sigma"],list(sq));same(row["phase_pi"],list(hq));same(row["momentum"],list(kq))
          k=mp.mpf(kq[0])/kq[1];a=mp.exp(mp.pi*s/2);b=1/a
          A=mp.gamma(1+1j*s)*mp.exp(-1j*s*mp.log(k/2))
          B=kappa*mp.gamma(1-1j*s)*mp.exp(1j*s*mp.log(k/2))
          R=-1j*(A*a+B*b)/(A*b+B*a);x=mp.mpf(7)/10
          phi=mp.exp(-1j*mp.pi/4)*mp.sqrt(k*x)*(A*mp.besselj(1j*s,k*x)+B*mp.besselj(-1j*s,k*x))/(A*b+B*a)
          close(complex_number(row["reflection"]),R);close(complex_number(row["relative_scattering"]),-R)
          close(complex_number(row["phi_at_7_over_10"]),phi);close(number(row["density"]),abs(phi)**2)
def check(path):
    d=strict_json(path)
    assert set(d)=={"schema","candidate_id","obstruction_id","source_commit","fixed_epoch","scope_literal","scope_flags","evaluator","route_a_yaml","route_a","classical_rows","boundary_rows","scattering_algebra_rows","negative_levels","continuum_rows","counts","numerical_precision","theorem_boundary","payload_sha256"}
    payload=d.pop("payload_sha256");assert type(payload)is str and payload==hashlib.sha256(canon(d)).hexdigest()
    assert d["schema"]=="hcs-c391-inverse-square-v1" and d["candidate_id"]=="HCS-C391" and d["obstruction_id"]=="HEN-O375"
    assert d["source_commit"]==BASE and type(d["fixed_epoch"])is int and d["fixed_epoch"]==1788566400
    assert d["scope_literal"]=="NO_BAD_EULER_OR_ROOT_NUMBER"
    assert set(d["scope_flags"])==FLAGS and all(v is False for v in d["scope_flags"].values())
    same(d["evaluator"],dict(authority="flow_systems/skills/route-a-evaluator.md",version="0.2.0",sha256=AUTH))
    ev=check_yaml();same(d["route_a_yaml"],dict(path=str(YAML.relative_to(ROOT)),raw_sha256=YAML_SHA,semantic_sha256=hashlib.sha256(canon(ev)).hexdigest()))
    same(d["route_a"],dict(tuple=TUPLE,overall_verdict="ROUTE_A_REJECTED",route_b_invocation_allowed=False))
    same(d["counts"],dict(classical=45,boundary=27,scattering_algebra=15,negative_levels=60,continuum=36))
    same(d["numerical_precision"],dict(working_digits=100,stored_digits=60,interval_certified=False))
    for key,rows in zip(("classical_rows","boundary_rows","scattering_algebra_rows"),exact_expected()):same(d[key],rows)
    check_numbers(d["negative_levels"],d["continuum_rows"])
    assert d["theorem_boundary"]=="All sigma positive and all unit boundary phases; finite evidence is regression, not completeness; no critical case, target arithmetic, regularized determinant, or Route B"
    return payload
def main():
    p=argparse.ArgumentParser();p.add_argument("path",type=Path,nargs="?",default=ROOT/"results/c391_evidence.json");p.add_argument("--yaml-only",action="store_true");p.add_argument("--yaml-path",type=Path,default=YAML);a=p.parse_args()
    if a.yaml_only:check_yaml(a.yaml_path);print("C391 locked strict YAML PASS");return
    print("C391 independent checker PASS",check(a.path),"45+27+15 exact rows; 60+36 numerical rows")
if __name__=="__main__":main()
