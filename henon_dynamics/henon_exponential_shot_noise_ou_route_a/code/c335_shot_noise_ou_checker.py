#!/usr/bin/env python3
"""Producer-independent structural and mathematical checker for HCS-C335."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import yaml

ROOT=Path(__file__).resolve().parents[1]
DEFAULT=ROOT/"results/c335_shot_noise_ou_evidence.json"
DEFAULT_EVAL=ROOT/"evaluations/route_a/HCS-C335/2026-09-03.yaml"
SOURCE="db2c816b7b6bd450f51f79b91842cb882b0bd773"
EVALUATOR="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EVAL_RAW="7fbc0434474de616b456ac56c3ac69ed858982b10deee22f53e08cb787fb2a42"
EVAL_SEMANTIC="f635ccc64622b3592891c6e900d48817bb87b17e531f067d3ce07a7b05272bf1"
SCOPE="NO_BAD_EULER_OR_ROOT_NUMBER"
PARAMETERS=((Fraction(1),Fraction(1,2),Fraction(2)),(Fraction(1),Fraction(1),Fraction(1)),(Fraction(2),Fraction(3),Fraction(3,2)),(Fraction(3,2),Fraction(1),Fraction(4)),(Fraction(2,3),Fraction(5,3),Fraction(5,2)))
DECAYS=(Fraction(1,5),Fraction(1,3),Fraction(1,2),Fraction(3,4))
LAPLACE=(Fraction(1,4),Fraction(1),Fraction(3))
MAX_DEGREE=12
mp.mp.dps=110


def pairs(items):
    out={}
    for key,value in items:
        if key in out: raise ValueError("duplicate JSON key")
        out[key]=value
    return out


def strict_json(path):
    return json.loads(path.read_text(),object_pairs_hook=pairs,parse_constant=lambda x:(_ for _ in()).throw(ValueError(x)))


class UniqueLoader(yaml.SafeLoader): pass
UniqueLoader.yaml_implicit_resolvers={k:[(t,r) for t,r in v if t!="tag:yaml.org,2002:timestamp"] for k,v in yaml.SafeLoader.yaml_implicit_resolvers.items()}
def mapping(loader,node,deep=False):
    out={}
    for kn,vn in node.value:
        if kn.tag=="tag:yaml.org,2002:merge": raise ValueError("merge forbidden")
        key=loader.construct_object(kn,deep=deep)
        if type(key) is not str or key in out: raise ValueError("bad YAML key")
        out[key]=loader.construct_object(vn,deep=deep)
    return out
UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,mapping)
def strict_yaml(path):
    raw=path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token,(yaml.tokens.AnchorToken,yaml.tokens.AliasToken)): raise ValueError("alias")
    return yaml.load(raw,Loader=UniqueLoader)


def semantic(value): return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def payload(data):
    body=dict(data); body.pop("payload_sha256",None); return semantic(body)
def leaves(value):
    if type(value) is dict:return sum(leaves(v) for v in value.values())
    if type(value) is list:return sum(leaves(v) for v in value)
    return 1
def q(text):
    if type(text) is not str or not re.fullmatch(r"-?(?:0|[1-9][0-9]*)(?:/[1-9][0-9]*)?",text):raise AssertionError("rational syntax")
    value=Fraction(text); rendered=str(value.numerator) if value.denominator==1 else f"{value.numerator}/{value.denominator}"
    if rendered!=text:raise AssertionError("rational canonical")
    return value
def mpq(value):return mp.mpf(value.numerator)/value.denominator
def d(text):
    if type(text) is not str:raise AssertionError("decimal type")
    value=mp.mpf(text)
    if not mp.isfinite(value):raise AssertionError("decimal finite")
    if mp.nstr(value,80,strip_zeros=False,min_fixed=-120,max_fixed=120)!=text:raise AssertionError("decimal canonical")
    return value
def close(text,expected):
    value=d(text)
    if abs(value-expected)>mp.mpf("4e-78")*max(1,abs(expected)):raise AssertionError("decimal mismatch")
def rising(a,n):
    out=Fraction(1)
    for j in range(n):out*=a+j
    return out


def main():
    if sys.flags.optimize:raise RuntimeError("C335 checker refuses optimized Python")
    ap=argparse.ArgumentParser();ap.add_argument("--evidence",type=Path,default=DEFAULT);ap.add_argument("--evaluation",type=Path,default=DEFAULT_EVAL);args=ap.parse_args()
    data=strict_json(args.evidence); evaluation=strict_yaml(args.evaluation); checks=0
    if hashlib.sha256(args.evaluation.read_bytes()).hexdigest()!=EVAL_RAW or semantic(evaluation)!=EVAL_SEMANTIC:raise AssertionError("evaluation digest")
    if payload(data)!=data.get("payload_sha256"):raise AssertionError("payload")
    checks+=3
    top={"schema","candidate_id","obstruction_id","evaluation_date","fixed_epoch","source_commit","scope_literal","evaluator","evaluation_lock","model","theorem_contract","parameter_rows","transition_rows","semigroup_rows","polynomial_rows","boundary_atlas","collision_boundary","route_a","scope_flags","nonclaims","references","enumeration","payload_sha256"}
    if type(data) is not dict or set(data)!=top:raise AssertionError("evidence schema")
    if tuple(data[k] for k in ("schema","candidate_id","obstruction_id","evaluation_date","fixed_epoch","source_commit","scope_literal"))!=("hcs-c335-shot-noise-ou-v1","HCS-C335","HEN-O319","2026-09-03",1788393600,SOURCE,SCOPE):raise AssertionError("identity")
    if data["evaluator"]!={"authority":"flow_systems/skills/route-a-evaluator.md","version":"0.2.0","sha256":EVALUATOR}:raise AssertionError("evaluator")
    if data["evaluation_lock"]!={"relative_path":"evaluations/route_a/HCS-C335/2026-09-03.yaml","raw_sha256":EVAL_RAW,"semantic_sha256":EVAL_SEMANTIC}:raise AssertionError("evaluation lock")
    expected_model={"sde":"dX_t=-gamma X_t dt+dJ_t on [0,infinity)","driver":"J is compound Poisson of rate kappa with independent Exp(beta) marks","positive_parameters":"gamma,kappa,beta>0","generator":"Lf=-gamma x f'(x)+kappa integral beta exp(-beta y)(f(x+y)-f(x))dy"}
    expected_theorem={"pathwise_semigroup":"X_t=exp(-gamma t)x+sum_{T_j<=t}exp(-gamma(t-T_j))Y_j","transition_transform":"E_x exp(-sX_t)=exp(-s exp(-gamma t)x)((beta+s exp(-gamma t))/(beta+s))^(kappa/gamma)","stationarity":"the unique invariant probability is Gamma(shape kappa/gamma, rate beta)","coupling":"for every p>=1, W_p(P_t(x,.),P_t(y,.))=exp(-gamma t)|x-y|","stationary_statistics":"moments are (alpha)_n/beta^n, cumulants alpha(n-1)!/beta^n, and covariance is alpha exp(-gamma|t|)/beta^2","polynomial_filtration":"P_m is invariant and the restriction has exactly the simple eigenvalues 0,-gamma,...,-m gamma","spectral_boundary":"the filtration theorem makes no assertion about the full L2 spectrum, completeness, normality, or reversibility"}
    if data["model"]!=expected_model or data["theorem_contract"]!=expected_theorem:raise AssertionError("static theorem")
    static_hashes={"boundary_atlas":"413bd45491f99b5ba070a5efd3d3b2f7956bfe42d901721e23b2f8549b37fa60","collision_boundary":"00cc9292928097624d7f833fe3cf2ec60c41ba61910541f48bbd7c462371fb40","nonclaims":"9543ed1c74c907529f93db02e539a5956fe091c06e2719009f89e35ff5ac99f3","references":"ba099d553ab76164f7903d922e9aef1ae9353b6da84350e638780a5459e1883c"}
    if any(semantic(data[k])!=v for k,v in static_hashes.items()):raise AssertionError("static boundary/source lock")
    route={"tuple":["A0_FAIL","A1_FAIL","A2_FAIL","A3_FAIL","A4_FAIL"],"overall":"ROUTE_A_REJECTED","route_b_invocation_allowed":False}
    flag_keys={"claims_target_arithmetic_local_data","claims_target_euler_factors","claims_root_number","claims_automorphy","claims_target_divisor_or_counting_law","claims_target_functional_equation","claims_target_zero_match","claims_hilbert_polya_operator","invokes_route_b"}
    if data["route_a"]!=route or set(data["scope_flags"])!=flag_keys or any(type(v) is not bool or v for v in data["scope_flags"].values()):raise AssertionError("route")
    checks+=10
    eval_top={"schema","candidate_id","title","evaluation_date","source_commit","fixed_epoch","scope_literal","evaluator_authority","evaluator_version","evaluator_authority_sha256","obstruction_id","candidate_definition","family","phase_space","dynamics","parameters","parameter_provenance","arithmetic_origin","clock","normalization","determinant_convention","orbit_cutoff","precision","training_data","forbidden_data","artifact_paths","a0","a1","a2","a3","a4","tuple","overall_verdict","route_b_invocation_allowed","route_b_lock_reason","scope_flags","theorem_status","finite_evidence_role","source_owner_tokens"}
    if type(evaluation) is not dict or set(evaluation)!=eval_top:raise AssertionError("evaluation schema")
    if any(type(evaluation[k]) is not dict or set(evaluation[k])!={"verdict","evidence_status","strongest_evidence","strongest_failure"} for k in ("a0","a1","a2","a3","a4")):raise AssertionError("layers")
    if (evaluation["candidate_id"],evaluation["obstruction_id"],evaluation["evaluation_date"],evaluation["source_commit"],evaluation["fixed_epoch"],evaluation["scope_literal"],evaluation["evaluator_authority"],evaluation["evaluator_version"],evaluation["evaluator_authority_sha256"],evaluation["artifact_paths"],evaluation["tuple"],evaluation["overall_verdict"],evaluation["route_b_invocation_allowed"],evaluation["scope_flags"],evaluation["theorem_status"],evaluation["finite_evidence_role"],evaluation["source_owner_tokens"])!=("HCS-C335","HEN-O319","2026-09-03",SOURCE,1788393600,SCOPE,"flow_systems/skills/route-a-evaluator.md","0.2.0",EVALUATOR,["results/c335_shot_noise_ou_evidence.json","THEOREM_PACKAGE.md","paper/main.pdf"],route["tuple"],"ROUTE_A_REJECTED",False,data["scope_flags"],"PROVABLE_AS_STATED","convention and implementation receipt, not proof",["10.1016/S0165-1684(98)00226-6","10.1016/0304-4149(84)90312-0","10.1111/1467-9868.00282"]):raise AssertionError("evaluation semantics")
    if [evaluation[k]["verdict"] for k in ("a0","a1","a2","a3","a4")]!=route["tuple"] or [evaluation[k]["evidence_status"] for k in ("a0","a1","a2","a3","a4")]!=["STOP_SCOPED"]*5:raise AssertionError("layers semantics")
    checks+=40

    parameters=data["parameter_rows"]
    pkeys={"parameter_id","gamma","kappa","beta","alpha","stationary_moments_0_to_12","stationary_cumulants_1_to_12","stationary_variance"}
    if len(parameters)!=len(PARAMETERS):raise AssertionError("parameter count")
    for pid,(row,(gamma,kappa,beta)) in enumerate(zip(parameters,PARAMETERS),1):
        if type(row) is not dict or set(row)!=pkeys:raise AssertionError("parameter schema")
        alpha=kappa/gamma; moments=[rising(alpha,n)/beta**n for n in range(13)]; cumulants=[alpha*math.factorial(n-1)/beta**n for n in range(1,13)]
        if (row["parameter_id"],q(row["gamma"]),q(row["kappa"]),q(row["beta"]),q(row["alpha"]),[q(x) for x in row["stationary_moments_0_to_12"]],[q(x) for x in row["stationary_cumulants_1_to_12"]],q(row["stationary_variance"]))!=(f"p{pid}",gamma,kappa,beta,alpha,moments,cumulants,alpha/beta**2):raise AssertionError("parameter identities")
        checks+=10+len(moments)+len(cumulants)

    transition=data["transition_rows"]; coords=[(pid,params,r,s) for pid,params in enumerate(PARAMETERS,1) for r in DECAYS for s in LAPLACE]
    tkeys={"parameter_id","decay_factor","laplace_s","initial_x","time","transition_laplace"}
    if len(transition)!=len(coords):raise AssertionError("transition count")
    for row,(pid,(gamma,kappa,beta),r,s) in zip(transition,coords):
        if type(row) is not dict or set(row)!=tkeys:raise AssertionError("transition schema")
        alpha=kappa/gamma; initial=Fraction(pid,3); time=-mp.log(mpq(r))/mpq(gamma)
        expected=mp.exp(-mpq(s)*mpq(r)*mpq(initial))*((mpq(beta)+mpq(s)*mpq(r))/(mpq(beta)+mpq(s)))**mpq(alpha)
        if (row["parameter_id"],q(row["decay_factor"]),q(row["laplace_s"]),q(row["initial_x"]))!=(f"p{pid}",r,s,initial):raise AssertionError("transition coords")
        close(row["time"],time);close(row["transition_laplace"],expected);checks+=8

    semigroup=data["semigroup_rows"]; scoords=[(pid,p,r1,r2,Fraction(pid+1,3)) for pid,p in enumerate(PARAMETERS,1) for r1,r2 in ((Fraction(1,2),Fraction(1,3)),(Fraction(3,4),Fraction(1,5)))]
    skeys={"parameter_id","r1","r2","laplace_s","factor_first","factor_second","factor_direct"}
    if len(semigroup)!=len(scoords):raise AssertionError("semigroup count")
    for row,(pid,(gamma,kappa,beta),r1,r2,s) in zip(semigroup,scoords):
        if type(row) is not dict or set(row)!=skeys:raise AssertionError("semigroup schema")
        alpha=kappa/gamma;bb=mpq(beta);ss=mpq(s)
        first=((bb+ss*mpq(r1))/(bb+ss))**mpq(alpha);second=((bb+ss*mpq(r1*r2))/(bb+ss*mpq(r1)))**mpq(alpha);direct=((bb+ss*mpq(r1*r2))/(bb+ss))**mpq(alpha)
        if (row["parameter_id"],q(row["r1"]),q(row["r2"]),q(row["laplace_s"]))!=(f"p{pid}",r1,r2,s):raise AssertionError("semigroup coords")
        close(row["factor_first"],first);close(row["factor_second"],second);close(row["factor_direct"],direct)
        if abs(d(row["factor_first"])*d(row["factor_second"])-d(row["factor_direct"]))>mp.mpf("1e-77"):raise AssertionError("semigroup product")
        checks+=10

    poly=data["polynomial_rows"]; pcoords=[(pid,p,n) for pid,p in enumerate(PARAMETERS,1) for n in range(13)]
    if len(poly)!=len(pcoords):raise AssertionError("polynomial count")
    for row,(pid,(gamma,kappa,beta),n) in zip(poly,pcoords):
        if type(row) is not dict or set(row)!={"degree","coefficients_low_to_high","diagonal","parameter_id"}:raise AssertionError("polynomial schema")
        expected=[Fraction(0)]*(n+1);expected[n]=-n*gamma
        for j in range(n):expected[j]=kappa*Fraction(math.factorial(n),math.factorial(j))*beta**(-(n-j))
        if (row["parameter_id"],row["degree"],[q(x) for x in row["coefficients_low_to_high"]],q(row["diagonal"]))!=(f"p{pid}",n,expected,-n*gamma):raise AssertionError("generator row")
        checks+=5+len(expected)

    expected_enum={"parameter_rows":len(parameters),"transition_rows":len(transition),"semigroup_rows":len(semigroup),"polynomial_rows":len(poly),"moment_entries":sum(len(r["stationary_moments_0_to_12"]) for r in parameters),"generator_coefficients":sum(len(r["coefficients_low_to_high"]) for r in poly)}
    if type(data["enumeration"]) is not dict or set(data["enumeration"])!=set(expected_enum)|{"audited_leaf_count"}:raise AssertionError("enumeration schema")
    if any(data["enumeration"][k]!=v for k,v in expected_enum.items()) or data["enumeration"]["audited_leaf_count"]!=leaves({k:v for k,v in data.items() if k not in ("enumeration","payload_sha256")})+leaves(data["enumeration"]):raise AssertionError("enumeration")
    checks+=12
    print(f"C335 independent checker: PASS ({checks} checks)")


if __name__=="__main__":main()
