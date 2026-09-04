#!/usr/bin/env python3
"""Independent fail-closed checker for HCS-C365; never imports producer."""
from __future__ import annotations
if not __debug__: raise RuntimeError("c365 checker refuses optimized Python")
import argparse, hashlib, json, sys
from fractions import Fraction
from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[1]
EVID=ROOT/"results/c365_gelfand_tsetlin_evidence.json"
EVAL=ROOT/"evaluations/route_a/HCS-C365/2026-09-04.yaml"
SOURCE="323ea43f6970544467f8a89f0ed9be0c7c39f896"
AUTH_SHA="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
YAML_RAW="9e0d4a9a3861749a2d48b0b30548da79e4f4ff721ba5deee0171a6497dfc7cbc"
YAML_SEM="db67bc21cbbeb3ae27fa09766ff3de547b54740137026bd9322e29a5a396a99d"
TOP={"schema","candidate_id","obstruction_id","evaluation_date","source_commit","fixed_epoch","scope_literal","evaluator","route_a_yaml",
 "conventions","theorem_contract","finite_grid","collision_boundary","nonclaims","references","scope_flags","route_a","finite_evidence_role",
 "weight_rows","frequency_rows","closure_basepoint_rows","boundary_rows","section_sha256","payload_sha256"}
YAML_KEYS={"schema","candidate_id","title","evaluation_date","source_commit","fixed_epoch","scope_literal","evaluator_authority","evaluator_version",
 "evaluator_authority_sha256","obstruction_id","candidate_definition","family","phase_space","dynamics","parameters","parameter_provenance",
 "arithmetic_origin","clock","normalization","determinant_convention","orbit_cutoff","precision","training_data","forbidden_data","artifact_paths",
 "a0","a1","a2","a3","a4","tuple","overall_verdict","route_b_invocation_allowed","route_b_lock_reason","scope_flags","theorem_status",
 "finite_evidence_role","source_owner_tokens"}

def unique(pairs):
    out={}
    for k,v in pairs:
        if k in out: raise ValueError("duplicate JSON key")
        out[k]=v
    return out
def load_json(p): return json.loads(p.read_text(),object_pairs_hook=unique,parse_constant=lambda x:(_ for _ in()).throw(ValueError(f"nonfinite {x}")))
def canon(x): return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
def digest(x): return hashlib.sha256(canon(x)).hexdigest()
def typed_equal(actual,expected):
    if type(actual) is not type(expected): return False
    if type(actual) is dict:
        return set(actual)==set(expected) and all(typed_equal(actual[k],expected[k]) for k in expected)
    if type(actual) is list:
        return len(actual)==len(expected) and all(typed_equal(a,b) for a,b in zip(actual,expected))
    return actual==expected
def typed_exact(actual,expected,label):
    if not typed_equal(actual,expected): raise AssertionError(f"typed value mismatch: {label}")
def keys(x,s):
    if type(x) is not dict or set(x)!=set(s): raise AssertionError(f"key set mismatch: {set(x) if isinstance(x,dict) else type(x)}")

class StrictLoader(yaml.SafeLoader): pass
StrictLoader.yaml_implicit_resolvers={k:[(tag,rx) for tag,rx in v if tag!="tag:yaml.org,2002:timestamp"] for k,v in yaml.SafeLoader.yaml_implicit_resolvers.items()}
def strict_mapping(loader,node,deep=False):
    out={}
    for kn,vn in node.value:
        if kn.tag=="tag:yaml.org,2002:merge": raise ValueError("merge key")
        key=loader.construct_object(kn,deep=deep)
        if type(key) is not str or key in out: raise ValueError("duplicate/non-string YAML key")
        out[key]=loader.construct_object(vn,deep=deep)
    return out
StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,strict_mapping)
def load_yaml(path):
    raw=path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token,(yaml.tokens.AnchorToken,yaml.tokens.AliasToken)): raise ValueError("anchors forbidden")
    y=yaml.load(raw,Loader=StrictLoader)
    if type(y) is not dict: raise TypeError("YAML root")
    return y

FLAGS={k:False for k in ("claims_target_arithmetic_local_data","claims_target_euler_factors","claims_root_number","claims_automorphy",
 "claims_target_divisor_or_counting_law","claims_target_functional_equation","claims_target_zero_match","claims_hilbert_polya_operator","invokes_route_b")}
TUPLE=["A0_WEAK_ARITHMETIC_RELATION","A1_WEAK","A2_FAIL","A3_FAIL","A4_NATURAL_QUANTIZATION"]
CONVENTIONS={"kks":"omega_A([X,A],[Y,A])=-i Tr(A[X,Y])","moment_pairing":"f_X(A)=-i Tr(AX)","circle_period":"2*pi",
 "prequantum_curvature":"-i omega","half_form":"absent","rho_shift":"none","minor":"northwest principal minors",
 "quantum_weight":"dominant integral U(3) highest weight"}
CONTRACT={"image":"lambda1>=y1>=lambda2>=y2>=lambda3 and y1>=x>=y2, with explicit arrow completion",
 "regular_action":"strict interlacing fibers are effective Lagrangian T3 orbits",
 "linear_flow":"closure through theta0 is theta0+K_omega, where K_omega is the integer-relation annihilator and has Q-rank dimension; theta0+K_omega equals K_omega iff theta0 lies in K_omega; primitive rank-one direction gives least period 2*pi/alpha",
 "quantization":"no-half-form Borel-Weil branching basis is indexed by unshifted integral GT labels; no spectrum of unspecified quantum operators is asserted",
 "dimension":"(lambda1-lambda2+1)(lambda2-lambda3+1)(lambda1-lambda3+2)/2"}
COLLISION={"C298":"dissipative Grassmann and Schubert projection, not a KKS-Thimm system",
 "C313":"round-sphere geodesic and Laplacian dynamics, not nested-minor branching quantization",
 "C331":"rank-one monopole line-bundle quantization on S2, not a U(3) GT integrable system",
 "C349":"Neumann-sphere Uhlenbeck integrals, not a compact-group branching polytope"}
NONCLAIMS=["no arithmetic local data","no target Euler factor or root number","no target functional equation or divisor",
 "no universal toric description of singular facets","no half-form or rho shift","no Hilbert-Polya operator","no Route B"]
BOUNDARIES=[
 {"case":"regular","spectrum":"lambda1>lambda2>lambda3","orbit_real_dimension":6,"image_dimension":3,"regular_torus":"T3"},
 {"case":"upper_repeat","spectrum":"lambda1=lambda2>lambda3","orbit_real_dimension":4,"image_dimension":2,"regular_torus":"T2 only"},
 {"case":"lower_repeat","spectrum":"lambda1>lambda2=lambda3","orbit_real_dimension":4,"image_dimension":2,"regular_torus":"T2 only"},
 {"case":"scalar","spectrum":"lambda1=lambda2=lambda3","orbit_real_dimension":0,"image_dimension":0,"regular_torus":"point"},
 {"case":"facet","spectrum":"regular but an interlacing equality holds","orbit_real_dimension":6,"image_dimension":3,"regular_torus":"singular; no universal fiber topology claimed"},
 {"case":"nonintegral","spectrum":"ordered real nonintegral weight","orbit_real_dimension":-1,"image_dimension":-1,"regular_torus":"classical theorem only; no quantization assertion"}]
FREQ=[
 ("zero",[[0,0,0],[0,0,0],[0,0,0]],"fixed",None,None),
 ("primitive_123",[[1,0,0],[2,0,0],[3,0,0]],"periodic","[1,2,3]","2*pi"),
 ("scaled_2",[[2,0,0],[-4,0,0],[6,0,0]],"periodic","[1,-2,3]","pi"),
 ("axis",[[0,0,0],[3,0,0],[0,0,0]],"periodic","[0,1,0]","2*pi/3"),
 ("sqrt2_ray",[[0,1,0],[0,2,0],[0,-1,0]],"periodic","[1,2,-1]","sqrt(2)*pi"),
 ("rank2_basic",[[1,0,0],[0,1,0],[0,0,0]],"rank_2",None,None),
 ("rank2_relation",[[1,0,0],[0,1,0],[1,1,0]],"rank_2",None,None),
 ("rank3",[[1,0,0],[0,1,0],[0,0,1]],"rank_3",None,None)]
CLOSURE_BASEPOINTS=[
 {"case":"rank3_nonzero","frequency":["1","sqrt(2)","sqrt(3)"],"theta0_over_pi":["1/7","0","0"],
  "theta0_in_K":True,"coset_equals_K":True,"witness":"K=T3 because the frequency has Q-rank 3"},
 {"case":"rank1_nonzero_inside","frequency":["1","2","3"],"theta0_over_pi":["1/2","1","3/2"],
  "theta0_in_K":True,"coset_equals_K":True,"witness":"theta0=(pi/2)*(1,2,3) mod 2*pi"},
 {"case":"rank1_outside","frequency":["1","2","3"],"theta0_over_pi":["0","0","1"],
  "theta0_in_K":False,"coset_equals_K":False,"witness":"relation (-3,0,1) annihilates frequency but pairs with theta0 to pi"}]

def rank_q(rows):
    a=[[Fraction(x) for x in row] for row in rows];r=0
    for c in range(3):
        p=next((i for i in range(r,3) if a[i][c]),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r];z=a[r][c];a[r]=[x/z for x in a[r]]
        for i in range(3):
            if i!=r and a[i][c]:
                z=a[i][c];a[i]=[a[i][j]-z*a[r][j] for j in range(3)]
        r+=1
    return r
def patterns(lam):
    l1,l2,l3=lam
    return [[p,q,r] for p in range(l2,l1+1) for q in range(l3,l2+1) for r in range(q,p+1)]

def validate_yaml(path):
    raw=path.read_bytes();y=load_yaml(path)
    assert hashlib.sha256(raw).hexdigest()==YAML_RAW and digest(y)==YAML_SEM
    keys(y,YAML_KEYS)
    exact={"schema":"route-a-evaluation-v0.2.0","candidate_id":"HCS-C365","title":"Gelfand--Tsetlin integrability and unshifted U(3) quantization",
      "evaluation_date":"2026-09-04","source_commit":SOURCE,"fixed_epoch":1788480000,"scope_literal":"NO_BAD_EULER_OR_ROOT_NUMBER",
      "evaluator_authority":"flow_systems/skills/route-a-evaluator.md","evaluator_version":"0.2.0","evaluator_authority_sha256":AUTH_SHA,
      "obstruction_id":"HEN-O349","artifact_paths":["results/c365_gelfand_tsetlin_evidence.json","THEOREM_PACKAGE.md","paper/main.pdf"],
      "tuple":TUPLE,"overall_verdict":"ROUTE_A_EXPLORATORY","route_b_invocation_allowed":False,"theorem_status":"PROVABLE_AS_STATED",
      "source_owner_tokens":["10.1016/0022-1236(83)90092-7","10.1007/BF01398934"],"scope_flags":FLAGS,
      "route_b_lock_reason":"no target Euler factor, root number, divisor, functional equation, or target-zero identification is present",
      "finite_evidence_role":"exhaustive finite pattern digests, exact closure-rank rows, and basepoint/coset-equality witnesses are regression evidence only; the all-weight, all-orbit theorem is proved analytically"}
    for k,v in exact.items(): typed_exact(y[k],v,f"yaml.{k}")
    for b,v,s in zip(("a0","a1","a2","a3","a4"),TUPLE,("PROVED","PROVED","STOP_SCOPED","STOP_SCOPED","PROVED")):
        keys(y[b],{"verdict","evidence_status","strongest_evidence","strongest_failure"});typed_exact(y[b]["verdict"],v,f"yaml.{b}.verdict");typed_exact(y[b]["evidence_status"],s,f"yaml.{b}.evidence_status")
    for k in ("candidate_definition","family","phase_space","dynamics","parameters","parameter_provenance","arithmetic_origin","clock","normalization",
              "determinant_convention","orbit_cutoff","precision","training_data","forbidden_data"):
        assert type(y[k]) is str and y[k],k
    return y

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--input",type=Path,default=EVID);ap.add_argument("--evaluation",type=Path,default=EVAL);a=ap.parse_args()
    validate_yaml(a.evaluation);obj=load_json(a.input);keys(obj,TOP);count=len(TOP)
    fixed={"schema":"hcs-c365-gelfand-tsetlin-evidence-v1","candidate_id":"HCS-C365","obstruction_id":"HEN-O349","evaluation_date":"2026-09-04",
      "source_commit":SOURCE,"fixed_epoch":1788480000,"scope_literal":"NO_BAD_EULER_OR_ROOT_NUMBER",
      "evaluator":{"authority":"flow_systems/skills/route-a-evaluator.md","version":"0.2.0","sha256":AUTH_SHA},
      "route_a_yaml":{"relative_path":"evaluations/route_a/HCS-C365/2026-09-04.yaml","raw_sha256":YAML_RAW,"semantic_sha256":YAML_SEM},
      "conventions":CONVENTIONS,"theorem_contract":CONTRACT,"collision_boundary":COLLISION,"nonclaims":NONCLAIMS,
      "references":[{"doi":"10.1016/0022-1236(83)90092-7","role":"Gelfand-Cetlin integrable-system and flag quantization lineage"},
                    {"doi":"10.1007/BF01398934","role":"geometric quantization and multiplicity lineage"}],"scope_flags":FLAGS,
      "route_a":{"tuple":TUPLE,"overall":"ROUTE_A_EXPLORATORY","route_b_invocation_allowed":False,"theorem_status":"PROVABLE_AS_STATED"},
      "finite_evidence_role":"exact exhaustive finite pattern digests, frequency rows, and basepoint/coset-equality witnesses are regression evidence only; analytic proofs establish all general statements"}
    for k,v in fixed.items(): typed_exact(obj[k],v,k);count+=1
    tmp=dict(obj);claim=tmp.pop("payload_sha256");assert claim==digest(tmp);count+=1
    keys(obj["section_sha256"],{"weight_rows","frequency_rows","closure_basepoint_rows","boundary_rows"})
    for s in ("weight_rows","frequency_rows","closure_basepoint_rows","boundary_rows"): assert obj["section_sha256"][s]==digest(obj[s]);count+=1
    expected_coords={(a,b) for a in range(13) for b in range(13)};seen=set();total=0
    assert len(obj["weight_rows"])==169
    for row in obj["weight_rows"]:
        keys(row,{"a","b","lambda","pattern_count","weyl_dimension","strict_pattern_count","pattern_digest"})
        a0,b0=row["a"],row["b"];assert type(a0) is int and type(b0) is int and (a0,b0) in expected_coords and (a0,b0) not in seen;seen.add((a0,b0))
        lam=[a0+b0,b0,0];ps=patterns(lam);dim=(a0+1)*(b0+1)*(a0+b0+2)//2
        strict=sum(lam[0]>p>lam[1]>q>lam[2] and p>r>q for p,q,r in ps)
        typed_exact(row,{"a":a0,"b":b0,"lambda":lam,"pattern_count":len(ps),"weyl_dimension":dim,"strict_pattern_count":strict,"pattern_digest":digest(ps)},f"weight[{a0},{b0}]")
        total+=len(ps);count+=8
    assert seen==expected_coords and total==74529;count+=2
    expected_freq=[{"name":n,"basis":["1","sqrt(2)","sqrt(3)"],"coefficient_rows":c,"rational_rank":rank_q(c),"classification":s,
                    "primitive_direction":d,"least_period":p} for n,c,s,d,p in FREQ]
    typed_exact(obj["frequency_rows"],expected_freq,"frequency_rows");count+=8
    typed_exact(obj["closure_basepoint_rows"],CLOSURE_BASEPOINTS,"closure_basepoint_rows");count+=3
    typed_exact(obj["boundary_rows"],BOUNDARIES,"boundary_rows");count+=6
    grid={"gap_min":0,"gap_max":12,"weight_rows":169,"pattern_total":74529,"frequency_rows":8,"closure_basepoint_rows":3,"boundary_rows":6,
          "pattern_storage":"canonical per-weight exhaustive digests"}
    typed_exact(obj["finite_grid"],grid,"finite_grid");count+=8
    print(f"C365 checker PASS: assertions={count} weights=169 patterns={total} frequencies=8 basepoints=3 payload={claim}")
if __name__=="__main__":
    try: main()
    except Exception as exc:
        print(f"C365 checker FAIL: {type(exc).__name__}: {exc}",file=sys.stderr);sys.exit(1)
