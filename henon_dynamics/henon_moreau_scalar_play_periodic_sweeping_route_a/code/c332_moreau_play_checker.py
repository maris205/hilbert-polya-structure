#!/usr/bin/env python3
"""Producer-independent structural and exact checker for HCS-C332."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from fractions import Fraction
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c332_moreau_play_evidence.json"
DEFAULT_EVAL = ROOT / "evaluations/route_a/HCS-C332/2026-09-03.yaml"
SOURCE = "5ca65027918c0fce7ef9af82f3faf2e46ed6530c"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EVAL_RAW = "97f9ec8a8abe0c6b4bf1a0a4609467088c6e78638d27329a382bd11068daa86b"
EVAL_SEMANTIC = "454ee341774e7da7c271ce9b88168d9dc0f5fcedf69aa8426cf8e7dd7eec35b9"
CASES = (
    (Fraction(0), Fraction(1), Fraction(1), "cornered"),
    (Fraction(-2), Fraction(3), Fraction(3), "maximum_plateau"),
    (Fraction(1), Fraction(5), Fraction(2), "minimum_plateau"),
    (Fraction(-3), Fraction(3), Fraction(3), "two_plateaus"),
    (Fraction(0), Fraction(5), Fraction(1), "cornered"),
    (Fraction(-2), Fraction(7), Fraction(2), "maximum_plateau"),
    (Fraction(0), Fraction(3), Fraction(0), "zero_radius"),
    (Fraction(2), Fraction(2), Fraction(1), "constant_input"),
    (Fraction(0), Fraction(0), Fraction(0), "constant_zero_radius"),
    (Fraction(-1), Fraction(2), Fraction(1, 2), "minimum_plateau"),
    (Fraction(1, 2), Fraction(5, 2), Fraction(3, 2), "smooth_reparameterization"),
    (Fraction(-5, 2), Fraction(1, 2), Fraction(3, 2), "two_plateaus"),
)


def object_pairs(items):
    out={}
    for key,value in items:
        if key in out: raise ValueError(f"duplicate JSON key: {key}")
        out[key]=value
    return out


def strict_json(path):
    return json.loads(path.read_text(),object_pairs_hook=object_pairs,parse_constant=lambda x:(_ for _ in ()).throw(ValueError(x)))


class UniqueLoader(yaml.SafeLoader): pass
UniqueLoader.yaml_implicit_resolvers={key:[(tag,p) for tag,p in values if tag!="tag:yaml.org,2002:timestamp"] for key,values in yaml.SafeLoader.yaml_implicit_resolvers.items()}
def unique_mapping(loader,node,deep=False):
    out={}
    for key_node,value_node in node.value:
        if key_node.tag=="tag:yaml.org,2002:merge": raise ValueError("YAML merge forbidden")
        key=loader.construct_object(key_node,deep=deep)
        if type(key) is not str or key in out: raise ValueError("duplicate/non-string YAML key")
        out[key]=loader.construct_object(value_node,deep=deep)
    return out
UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,unique_mapping)
def strict_yaml(path):
    raw=path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token,(yaml.tokens.AnchorToken,yaml.tokens.AliasToken)): raise ValueError("YAML anchors/aliases forbidden")
    return yaml.load(raw,Loader=UniqueLoader)


def semantic_hash(value): return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def payload_hash(data):
    body=dict(data); body.pop("payload_sha256",None); return semantic_hash(body)
def leaves(value):
    if type(value) is dict: return sum(leaves(v) for v in value.values())
    if type(value) is list: return sum(leaves(v) for v in value)
    return 1
def frac(text):
    if type(text) is not str or not re.fullmatch(r"-?(?:0|[1-9][0-9]*)(?:/[1-9][0-9]*)?",text): raise AssertionError("noncanonical rational syntax")
    value=Fraction(text); expected=str(value.numerator) if value.denominator==1 else f"{value.numerator}/{value.denominator}"
    if text!=expected: raise AssertionError("non-reduced rational")
    return value
def clamp(x,lo,hi): return min(hi,max(lo,x))
def P(z,m,M,r): return min(max(z,M-r),m+r)
def initials(m,r): return [m] if r==0 else [m-r,m-r/2,m,m+r/2,m+r]
def solve(levels,z,r):
    out=[z]
    for u in levels[1:]: out.append(clamp(out[-1],u-r,u+r))
    return out
def var(values): return sum((abs(b-a) for a,b in zip(values,values[1:])),Fraction(0))


def main():
    if sys.flags.optimize: raise RuntimeError("C332 checker refuses optimized Python")
    parser=argparse.ArgumentParser(); parser.add_argument("--evidence",type=Path,default=DEFAULT); parser.add_argument("--evaluation",type=Path,default=DEFAULT_EVAL); args=parser.parse_args()
    data=strict_json(args.evidence); evaluation=strict_yaml(args.evaluation); checks=0
    if hashlib.sha256(args.evaluation.read_bytes()).hexdigest()!=EVAL_RAW or semantic_hash(evaluation)!=EVAL_SEMANTIC: raise AssertionError("evaluation digest")
    if payload_hash(data)!=data.get("payload_sha256"): raise AssertionError("payload digest")
    checks+=3
    top={"schema","candidate_id","obstruction_id","evaluation_date","fixed_epoch","source_commit","scope_literal","evaluator","evaluation_lock","model","theorem_contract","case_rows","boundary_atlas","collision_boundary","route_a","scope_flags","nonclaims","references","enumeration","payload_sha256"}
    if type(data) is not dict or set(data)!=top: raise AssertionError("top-level schema")
    if tuple(data[k] for k in ("schema","candidate_id","obstruction_id","evaluation_date","fixed_epoch","source_commit","scope_literal")) != ("hcs-c332-moreau-play-v1","HCS-C332","HEN-O316","2026-09-03",1788393600,SOURCE,SCOPE): raise AssertionError("identity")
    if data["evaluator"]!={"authority":"flow_systems/skills/route-a-evaluator.md","version":"0.2.0","sha256":EVALUATOR}: raise AssertionError("evaluator")
    if data["evaluation_lock"]!={"relative_path":"evaluations/route_a/HCS-C332/2026-09-03.yaml","raw_sha256":EVAL_RAW,"semantic_sha256":EVAL_SEMANTIC}: raise AssertionError("evaluation lock")
    model={
        "input":"T-periodic W1,1 function starting at minimum m, nondecreasing to maximum M, then nonincreasing to m; plateaus allowed",
        "constraint":"y(t) belongs to [u(t)-r,u(t)+r]",
        "inclusion":"-dy belongs to the normal cone of [u-r,u+r]",
        "stop_variable":"s=u-y belongs to [-r,r]",
        "parameters":"r nonnegative and D=M-m nonnegative",
    }
    contract={
        "segment_projection":"on every monotone segment y(t)=projection of the segment initial state onto [u(t)-r,u(t)+r]",
        "poincare_map":"from a minimum P(z)=min(m+r,max(M-r,z))",
        "chambers":"D<2r has fixed interval [M-r,m+r]; D=2r has one fixed point; D>2r has one fixed point m+r and a nontrivial loop",
        "entrainment":"P composed with P equals P, so every admissible state reaches a periodic response in at most one period",
        "structure":"the flow and P are order preserving and nonexpansive, and orientation-preserving absolutely continuous time changes preserving W1,1 admissibility leave the path response invariant",
        "variation":"Var(u)=Var(y)+Var(s), integral s dy=r Var(y), and on a periodic single excursion Var(y)=2 max(D-2r,0)",
        "boundaries":"r=0, D=0, equality, plateaus, and W1,1 corners are included; no weak-continuation or smoothness claim is needed",
    }
    boundary=[
        {"face":"D<2r","status":"a continuum [M-r,m+r] of constant periodic play outputs"},
        {"face":"D=2r","status":"the fixed interval collapses to one constant periodic output and dissipation remains zero"},
        {"face":"D>2r","status":"one fixed state m+r and a unique nonconstant periodic play loop"},
        {"face":"r=0","status":"y=u, s=0, P maps the singleton feasible state to itself, and dissipation is zero"},
        {"face":"D=0","status":"the input is constant, P is the identity on [m-r,m+r], and every feasible constant output is periodic"},
        {"face":"plateaus and corners","status":"the W1,1 projection formula holds almost everywhere and is insensitive to plateau duration"},
        {"face":"time reparameterization","status":"only orientation-preserving absolutely continuous surjections preserving W1,1 admissibility are asserted"},
    ]
    collision={
        "C252":"the hysteretic relay oscillator has discrete guards and a hybrid switching cycle rather than a convex moving interval",
        "C238":"Coulomb dry friction is a forward Filippov capture law rather than a rate-independent play operator",
        "C310":"Dubins synthesis is endpoint-controlled bounded-curvature optimization rather than a constitutive sweeping process",
    }
    nonclaims=[
        "No priority is claimed for Moreau sweeping processes or scalar play operators.",
        "The analytic periodic classification carries no rational-prime labels.",
        "The normal-cone inclusion is not a natural self-adjoint or unitary quantization.",
        "Finite profiles are regression receipts and do not prove the W1,1 theorem.",
        "No target arithmetic local data, Euler factors, root numbers, automorphy, divisor, functional equation, zero match, or Hilbert--Polya operator is asserted.",
    ]
    refs=[
        {"doi":"10.1016/0022-0396(77)90085-7","role":"Moreau moving-convex-set evolution source"},
        {"doi":"10.1007/978-3-642-61302-9","role":"authoritative play and hysteresis monograph"},
        {"doi":"10.1007/978-1-4612-4048-8","role":"authoritative scalar play, convexity, and dissipation reference"},
    ]
    if (data["model"],data["theorem_contract"],data["boundary_atlas"],data["collision_boundary"],data["nonclaims"],data["references"])!=(model,contract,boundary,collision,nonclaims,refs): raise AssertionError("static theorem/source boundary")
    route={"tuple":["A0_FAIL","A1_PASS_ANALYTIC","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"],"overall":"ROUTE_A_REJECTED","route_b_invocation_allowed":False}
    if data["route_a"]!=route: raise AssertionError("Route-A")
    flag_keys={"claims_target_arithmetic_local_data","claims_target_euler_factors","claims_root_number","claims_automorphy","claims_target_divisor_or_counting_law","claims_target_functional_equation","claims_target_zero_match","claims_hilbert_polya_operator","invokes_route_b"}
    if set(data["scope_flags"])!=flag_keys or any(type(v) is not bool or v for v in data["scope_flags"].values()): raise AssertionError("scope flags")
    checks+=15
    eval_top={"schema","candidate_id","title","evaluation_date","source_commit","fixed_epoch","scope_literal","evaluator_authority","evaluator_version","evaluator_authority_sha256","obstruction_id","candidate_definition","family","phase_space","dynamics","parameters","parameter_provenance","arithmetic_origin","clock","normalization","determinant_convention","orbit_cutoff","precision","training_data","forbidden_data","artifact_paths","a0","a1","a2","a3","a4","tuple","overall_verdict","route_b_invocation_allowed","route_b_lock_reason","scope_flags","theorem_status","finite_evidence_role","source_owner_tokens"}
    if type(evaluation) is not dict or set(evaluation)!=eval_top: raise AssertionError("evaluation schema")
    layer_keys={"verdict","evidence_status","strongest_evidence","strongest_failure"}
    if any(type(evaluation[k]) is not dict or set(evaluation[k])!=layer_keys for k in ("a0","a1","a2","a3","a4")): raise AssertionError("layer schema")
    layers={
        "a0":{"verdict":"A0_FAIL","evidence_status":"PROVED","strongest_evidence":"no arithmetic source exists","strongest_failure":"threshold and excursion range do not intrinsically encode rational primes or prime powers"},
        "a1":{"verdict":"A1_PASS_ANALYTIC","evidence_status":"PROVED","strongest_evidence":"the complete one-period clamp map and every periodic response are classified analytically","strongest_failure":"the periodic responses are constitutive hysteresis loops without arithmetic labels"},
        "a2":{"verdict":"A2_FAIL","evidence_status":"STOP_SCOPED","strongest_evidence":"the scalar Poincare map is explicit","strongest_failure":"no primitive-orbit zeta, Euler product, or target determinant is defined"},
        "a3":{"verdict":"A3_FAIL","evidence_status":"STOP_SCOPED","strongest_evidence":"chamber boundaries and variation laws are exact","strongest_failure":"no target continuation, functional equation, Weil form, or explicit formula is produced"},
        "a4":{"verdict":"A4_FORMAL_HINT","evidence_status":"PROVED","strongest_evidence":"the play law is a normal-cone variational inclusion with an exact dissipation identity","strongest_failure":"this rate-independent inclusion supplies no natural unitary or self-adjoint prime-preserving lift"},
    }
    if any(evaluation[k]!=layers[k] for k in layers): raise AssertionError("evaluation layers")
    if (evaluation["schema"],evaluation["candidate_id"],evaluation["obstruction_id"],evaluation["evaluation_date"],evaluation["source_commit"],evaluation["fixed_epoch"],evaluation["scope_literal"],evaluation["evaluator_authority"],evaluation["evaluator_version"],evaluation["evaluator_authority_sha256"],evaluation["artifact_paths"],evaluation["tuple"],evaluation["overall_verdict"],evaluation["route_b_invocation_allowed"],evaluation["scope_flags"],evaluation["theorem_status"],evaluation["finite_evidence_role"],evaluation["source_owner_tokens"]) != ("route-a-evaluation-v0.2.0","HCS-C332","HEN-O316","2026-09-03",SOURCE,1788393600,SCOPE,"flow_systems/skills/route-a-evaluator.md","0.2.0",EVALUATOR,["results/c332_moreau_play_evidence.json","THEOREM_PACKAGE.md","paper/main.pdf"],route["tuple"],"ROUTE_A_REJECTED",False,data["scope_flags"],"PROVABLE_AS_STATED","convention and implementation receipt, not proof",["10.1016/0022-0396(77)90085-7","10.1007/978-3-642-61302-9","10.1007/978-1-4612-4048-8"]): raise AssertionError("evaluation semantics")
    checks+=42
    rows=data["case_rows"]
    if type(rows) is not list or len(rows)!=len(CASES): raise AssertionError("case row count")
    row_keys={"case_id","shape_tag","minimum","maximum","radius","range_D","chamber","fixed_set_low","fixed_set_high","initial_rows","periodic_representative","path_levels","periodic_play_nodes","periodic_stop_nodes","stretched_levels","stretched_play_nodes","input_variation","play_variation","stop_variation","dissipation_integral","variation_formula_check"}
    initial_keys={"initial","after_one_period","after_two_periods"}
    initial_total=path_total=reparam_total=0; chamber_counts={name:0 for name in ("D_lt_2r","D_eq_2r","D_gt_2r")}
    for index,(row,(m,M,r,shape)) in enumerate(zip(rows,CASES),1):
        if type(row) is not dict or set(row)!=row_keys: raise AssertionError("case schema")
        D=M-m; chamber="D_lt_2r" if D<2*r else "D_eq_2r" if D==2*r else "D_gt_2r"
        fixed_low=M-r if D<=2*r else m+r; fixed_high=m+r
        if (row["case_id"],row["shape_tag"],frac(row["minimum"]),frac(row["maximum"]),frac(row["radius"]),frac(row["range_D"]),row["chamber"],frac(row["fixed_set_low"]),frac(row["fixed_set_high"])) != (f"play-{index:02d}",shape,m,M,r,D,chamber,fixed_low,fixed_high): raise AssertionError("case identity")
        chamber_counts[chamber]+=1
        zs=initials(m,r)
        if type(row["initial_rows"]) is not list or len(row["initial_rows"])!=len(zs): raise AssertionError("initial count")
        outputs=[]
        for item,z in zip(row["initial_rows"],zs):
            if type(item) is not dict or set(item)!=initial_keys: raise AssertionError("initial schema")
            p=P(z,m,M,r); p2=P(p,m,M,r)
            if (frac(item["initial"]),frac(item["after_one_period"]),frac(item["after_two_periods"]))!=(z,p,p2) or p2!=p: raise AssertionError("Poincare map/idempotence")
            outputs.append(p); checks+=6
        if outputs!=sorted(outputs): raise AssertionError("order preservation")
        for a,b,pa,pb in zip(zs,zs[1:],outputs,outputs[1:]):
            if abs(pb-pa)>abs(b-a): raise AssertionError("nonexpansion")
            checks+=1
        rep=P(m,m,M,r); mid=(m+M)/2; levels=[m,mid,M,M,mid,m]; play=solve(levels,rep,r); stop=[u-y for u,y in zip(levels,play)]
        stretched=[m,m,mid,mid,M,M,M,mid,mid,m,m]; stretched_play=solve(stretched,rep,r)
        if frac(row["periodic_representative"])!=rep: raise AssertionError("representative")
        if [frac(x) for x in row["path_levels"]]!=levels or [frac(x) for x in row["periodic_play_nodes"]]!=play or [frac(x) for x in row["periodic_stop_nodes"]]!=stop: raise AssertionError("path projection")
        if [frac(x) for x in row["stretched_levels"]]!=stretched or [frac(x) for x in row["stretched_play_nodes"]]!=stretched_play: raise AssertionError("reparameterized path")
        retained=[stretched_play[i] for i in (0,2,4,6,8,10)]
        if retained!=play: raise AssertionError("rate independence")
        vu,vy,vs=2*D,var(play),var(stop)
        if (frac(row["input_variation"]),frac(row["play_variation"]),frac(row["stop_variation"]),frac(row["dissipation_integral"]),row["variation_formula_check"])!=(vu,vy,vs,r*vy,True): raise AssertionError("variation/dissipation")
        if vy!=2*max(D-2*r,Fraction(0)) or vu!=vy+vs: raise AssertionError("closed variation formula")
        if any(abs(u-y)>r for u,y in zip(levels,play)): raise AssertionError("feasibility")
        initial_total+=len(zs); path_total+=len(levels); reparam_total+=len(stretched); checks+=31
    enum=data["enumeration"]
    expected_enum={"case_rows":12,"initial_rows":initial_total,"path_nodes":path_total,"reparameterized_nodes":reparam_total,"chambers":chamber_counts}
    if type(enum) is not dict or set(enum)!=set(expected_enum)|{"audited_leaf_count"} or any(enum[k]!=v for k,v in expected_enum.items()): raise AssertionError("enumeration")
    body=dict(data); body.pop("payload_sha256")
    if enum["audited_leaf_count"]!=leaves(body): raise AssertionError("leaf count")
    checks+=8
    print(f"C332 independent checker: PASS ({checks} checks)")


if __name__=="__main__": main()
