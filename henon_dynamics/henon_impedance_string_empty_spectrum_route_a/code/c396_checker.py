#!/usr/bin/env python3
"""Independent exact loops and integral Green checks; never imports producer."""
if not __debug__: raise RuntimeError("c396 checker refuses optimized Python")
import argparse
import hashlib
import json
import re
from fractions import Fraction as F
from pathlib import Path
import mpmath as mp
import yaml
ROOT=Path(__file__).resolve().parents[1]
YAML=ROOT/"evaluations/route_a/HCS-C396/2026-09-05.yaml"
YAML_SHA="b9f3ae12e0294002acf0aec9d499f42bb0b1537ae75b30b253e5b5a600a048d8"
BASE="697518b6db90458f86f7916fbf397b8ad5ef2372"
AUTH="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
AUTHORITY=ROOT.parents[1]/"flow_systems/skills/route-a-evaluator.md"
FLAGS={"claims_target_arithmetic_local_data","claims_target_euler_factors","claims_root_number","claims_automorphy","claims_target_divisor_or_counting_law","claims_target_functional_equation","claims_target_zero_match","claims_hilbert_polya_operator","invokes_route_b"}
TUPLE=["A0_FAIL","A1_FAIL","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"]
def canon(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False).encode()
def same(a,b):assert canon(a)==canon(b),(a,b)
def pairs(rows):
    d={}
    for k,v in rows:
        if k in d:raise ValueError("duplicate JSON key")
        d[k]=v
    return d
def bad(x):raise ValueError("nonfinite JSON")
def strict_json(p):return json.loads(p.read_text(),object_pairs_hook=pairs,parse_constant=bad)
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
def check_yaml(path=YAML,authority=AUTHORITY):
    assert hashlib.sha256(authority.read_bytes()).hexdigest()==AUTH,"live evaluator bytes changed"
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
def q(x):return [x.numerator,x.denominator]
def real(x):return mp.mpf(x.numerator)/x.denominator
def number(x):
    assert type(x)is str and re.fullmatch(r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?",x)
    v=mp.mpf(x);assert mp.isfinite(v);return v
def complex_number(x):
    assert type(x)is list and len(x)==2;return number(x[0])+1j*number(x[1])
def close(a,b):assert abs(a-b)<=mp.mpf("2e-56")*max(1,abs(b)),(a,b)
def check(path,authority=AUTHORITY):
    d=strict_json(path);mp.mp.dps=105
    assert set(d)=={"schema","candidate_id","obstruction_id","source_commit","fixed_epoch","scope_literal","scope_flags","evaluator","route_a_yaml","route_a","boundary_rows","transport_rows","spectrum_rows","pseudospectrum_rows","green_rows","counts","numerical_precision","theorem_boundary","payload_sha256"}
    payload=d.pop("payload_sha256");assert type(payload)is str and payload==hashlib.sha256(canon(d)).hexdigest()
    assert d["schema"]=="hcs-c396-impedance-string-v1" and d["candidate_id"]=="HCS-C396" and d["obstruction_id"]=="HEN-O380"
    assert d["source_commit"]==BASE and type(d["fixed_epoch"])is int and d["fixed_epoch"]==1788566400
    assert d["scope_literal"]=="NO_BAD_EULER_OR_ROOT_NUMBER"
    assert set(d["scope_flags"])==FLAGS and all(v is False for v in d["scope_flags"].values())
    same(d["evaluator"],dict(authority="flow_systems/skills/route-a-evaluator.md",version="0.2.0",sha256=AUTH))
    ev=check_yaml(YAML,authority);same(d["route_a_yaml"],dict(path=str(YAML.relative_to(ROOT)),raw_sha256=YAML_SHA,semantic_sha256=hashlib.sha256(canon(ev)).hexdigest()))
    same(d["route_a"],dict(tuple=TUPLE,overall_verdict="ROUTE_A_REJECTED",route_b_invocation_allowed=False))
    same(d["counts"],dict(boundary=7,transport=588,spectrum=126,pseudospectrum=27,green=21))
    same(d["numerical_precision"],dict(working_digits=100,stored_digits=60,interval_certified=False))
    for field,count in (("boundary_rows",7),("transport_rows",588),("spectrum_rows",126),("pseudospectrum_rows",27),("green_rows",21)):
        assert type(d[field])is list and len(d[field])==count
    boundary=[];transport=[];ni=0;gi=0
    for eta in (F(0),F(1,3),F(1,2),F(1),F(2),F(3),F(7)):
      Q=(eta-1)/(eta+1)
      boundary.append(dict(eta=q(eta),q=q(Q),flux=q(-2*eta/(eta+1)**2),transparent=eta==1,conservative=eta==0))
      for tau in (F(1,2),F(1),F(2)):
        for tr in (F(0),F(1,4),F(1),F(5,4),F(2),F(11,4),F(3)):
          for sr in (F(1,8),F(3,8),F(5,8),F(7,8)):
            t=tau*tr;s=tau*sr;rem=s+t;k=0;amp=F(1)
            while rem>=tau:rem-=tau;k+=1;amp*=Q
            rest=t;norm=F(1)
            while rest>=tau:rest-=tau;norm*=abs(Q)
            transport.append(dict(eta=q(eta),tau=q(tau),t=q(t),s=q(s),crossings=k,remainder=q(rem),amplitude=q(amp),operator_norm=q(norm),extinct=Q==0 and t>=tau))
        T=real(tau);Qr=real(Q)
        if Q:
          for n in range(-3,4):
            r=d["spectrum_rows"][ni];ni+=1
            assert set(r)=={"eta","tau","n","eigenvalue","similarity_condition"}
            same(r["eta"],q(eta));same(r["tau"],q(tau));assert type(r["n"])is int and r["n"]==n
            lam=complex_number(r["eigenvalue"])
            close(mp.exp(lam*T),Qr);close(mp.re(lam)*T,mp.log(abs(Qr)))
            close(mp.im(lam)*T,mp.pi*(2*n+(1 if Q<0 else 0)))
            close(number(r["similarity_condition"])*abs(Qr),1)
        r=d["green_rows"][gi];gi+=1
        assert set(r)=={"eta","tau","z","w_zero","w_third","w_end"}
        same(r["eta"],q(eta));same(r["tau"],q(tau));same(r["z"],["0.5","1.0"])
        z=complex_number(r["z"]);den=mp.exp(z*T)-Qr
        # Integrate the Green kernel, unlike producer's polynomial ODE solution.
        for s,key in ((mp.mpf(0),"w_zero"),(T/3,"w_third"),(T,"w_end")):
            left=mp.quad(lambda v:mp.exp(z*(s-v))*Qr/den*(v*v+1),[0,s]) if s else 0
            right=mp.quad(lambda v:mp.exp(z*(s-v))*mp.exp(z*T)/den*(v*v+1),[s,T]) if s<T else 0
            close(complex_number(r[key]),left+right)
        close(complex_number(r["w_end"]),Qr*complex_number(r["w_zero"]))
    same(d["boundary_rows"],boundary);same(d["transport_rows"],transport)
    pi=0
    for tau in (F(1,2),F(1),F(2)):
      T=real(tau)
      for branch,param in [("trigonometric",F(j,6)) for j in (1,2,3,4,5)]+[("hyperbolic",p) for p in (F(1,2),F(1),F(2))]+[("critical",F(0))]:
        r=d["pseudospectrum_rows"][pi];pi+=1
        assert set(r)=={"tau","branch","parameter","real_part","resolvent_norm","least_mu","hs_squared"}
        same(r["tau"],q(tau));same(r["branch"],branch);same(r["parameter"],q(param))
        x=number(r["real_part"]);rho=number(r["resolvent_norm"]);mu=number(r["least_mu"])
        if branch=="trigonometric":
            theta=mp.pi*real(param);u=lambda s:mp.sin(theta*(1-s/T));mu_expected=x*x+(theta/T)**2
        elif branch=="hyperbolic":
            h=real(param);u=lambda s:mp.sinh(h*(1-s/T));mu_expected=x*x-(h/T)**2
        else:u=lambda s:T-s;mu_expected=x*x
        close(mp.diff(u,0),x*u(0));close(mu,mu_expected);close(rho*rho*mu,1)
        assert rho>0 and mu>0
        hs=mp.quad(lambda gap:(T-gap)*mp.exp(-2*x*gap),[0,T])
        close(number(r["hs_squared"]),hs)
    assert d["theorem_boundary"]=="Finite eta nonnegative; full physical time and spectrum proved analytically; exact pseudospectra only at eta one; no target arithmetic, ordinary trace or Route B"
    return payload
def main():
    p=argparse.ArgumentParser();p.add_argument("path",type=Path,nargs="?",default=ROOT/"results/c396_evidence.json");p.add_argument("--yaml-only",action="store_true");p.add_argument("--yaml-path",type=Path,default=YAML);p.add_argument("--authority-path",type=Path,default=AUTHORITY);a=p.parse_args()
    if a.yaml_only:check_yaml(a.yaml_path,a.authority_path);print("C396 locked strict YAML PASS");return
    print("C396 independent checker PASS",check(a.path,a.authority_path),"7+588 exact rows; 126+27+21 numerical rows")
if __name__=="__main__":main()
