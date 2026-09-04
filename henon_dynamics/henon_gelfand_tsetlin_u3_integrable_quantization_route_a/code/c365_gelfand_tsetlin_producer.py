#!/usr/bin/env python3
"""Canonical exact evidence producer for HCS-C365."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("c365 producer refuses optimized Python")
import argparse, hashlib, json
from fractions import Fraction
from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"results/c365_gelfand_tsetlin_evidence.json"
YAML_PATH=ROOT/"evaluations/route_a/HCS-C365/2026-09-04.yaml"
SOURCE="323ea43f6970544467f8a89f0ed9be0c7c39f896"
EVAL_SHA="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
YAML_RAW="9e0d4a9a3861749a2d48b0b30548da79e4f4ff721ba5deee0171a6497dfc7cbc"
YAML_SEM="db67bc21cbbeb3ae27fa09766ff3de547b54740137026bd9322e29a5a396a99d"

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
    value=yaml.load(raw,Loader=StrictLoader)
    if type(value) is not dict: raise TypeError("YAML root")
    return value
def canon(x): return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
def digest(x): return hashlib.sha256(canon(x)).hexdigest()

def patterns(lam):
    l1,l2,l3=lam
    return [[p,q,r] for p in range(l2,l1+1) for q in range(l3,l2+1) for r in range(q,p+1)]

def rank_q(rows):
    a=[[Fraction(x) for x in row] for row in rows]; m=len(a); n=len(a[0]); r=0
    for c in range(n):
        pivot=next((i for i in range(r,m) if a[i][c]),None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]; p=a[r][c]; a[r]=[x/p for x in a[r]]
        for i in range(m):
            if i!=r and a[i][c]:
                f=a[i][c]; a[i]=[a[i][j]-f*a[r][j] for j in range(n)]
        r+=1
    return r

FREQUENCIES=[
 ("zero",[[0,0,0],[0,0,0],[0,0,0]],"fixed",None,None),
 ("primitive_123",[[1,0,0],[2,0,0],[3,0,0]],"periodic","[1,2,3]","2*pi"),
 ("scaled_2",[[2,0,0],[-4,0,0],[6,0,0]],"periodic","[1,-2,3]","pi"),
 ("axis",[[0,0,0],[3,0,0],[0,0,0]],"periodic","[0,1,0]","2*pi/3"),
 ("sqrt2_ray",[[0,1,0],[0,2,0],[0,-1,0]],"periodic","[1,2,-1]","sqrt(2)*pi"),
 ("rank2_basic",[[1,0,0],[0,1,0],[0,0,0]],"rank_2",None,None),
 ("rank2_relation",[[1,0,0],[0,1,0],[1,1,0]],"rank_2",None,None),
 ("rank3",[[1,0,0],[0,1,0],[0,0,1]],"rank_3",None,None),
]

CLOSURE_BASEPOINTS=[
 {"case":"rank3_nonzero","frequency":["1","sqrt(2)","sqrt(3)"],"theta0_over_pi":["1/7","0","0"],
  "theta0_in_K":True,"coset_equals_K":True,"witness":"K=T3 because the frequency has Q-rank 3"},
 {"case":"rank1_nonzero_inside","frequency":["1","2","3"],"theta0_over_pi":["1/2","1","3/2"],
  "theta0_in_K":True,"coset_equals_K":True,"witness":"theta0=(pi/2)*(1,2,3) mod 2*pi"},
 {"case":"rank1_outside","frequency":["1","2","3"],"theta0_over_pi":["0","0","1"],
  "theta0_in_K":False,"coset_equals_K":False,"witness":"relation (-3,0,1) annihilates frequency but pairs with theta0 to pi"},
]

def build(yaml_path):
    raw=yaml_path.read_bytes(); sem=load_yaml(yaml_path)
    assert hashlib.sha256(raw).hexdigest()==YAML_RAW
    assert digest(sem)==YAML_SEM
    weights=[]; total=0
    for a in range(13):
        for b in range(13):
            lam=[a+b,b,0]; ps=patterns(lam); dim=(a+1)*(b+1)*(a+b+2)//2
            strict=sum(lam[0]>p>lam[1]>q>lam[2] and p>r>q for p,q,r in ps)
            weights.append({"a":a,"b":b,"lambda":lam,"pattern_count":len(ps),"weyl_dimension":dim,
                            "strict_pattern_count":strict,"pattern_digest":digest(ps)})
            total+=len(ps)
    freqs=[]
    for name,coeff,status,direction,period in FREQUENCIES:
        freqs.append({"name":name,"basis":["1","sqrt(2)","sqrt(3)"],"coefficient_rows":coeff,
                      "rational_rank":rank_q(coeff),"classification":status,
                      "primitive_direction":direction,"least_period":period})
    boundaries=[
      {"case":"regular","spectrum":"lambda1>lambda2>lambda3","orbit_real_dimension":6,"image_dimension":3,"regular_torus":"T3"},
      {"case":"upper_repeat","spectrum":"lambda1=lambda2>lambda3","orbit_real_dimension":4,"image_dimension":2,"regular_torus":"T2 only"},
      {"case":"lower_repeat","spectrum":"lambda1>lambda2=lambda3","orbit_real_dimension":4,"image_dimension":2,"regular_torus":"T2 only"},
      {"case":"scalar","spectrum":"lambda1=lambda2=lambda3","orbit_real_dimension":0,"image_dimension":0,"regular_torus":"point"},
      {"case":"facet","spectrum":"regular but an interlacing equality holds","orbit_real_dimension":6,"image_dimension":3,"regular_torus":"singular; no universal fiber topology claimed"},
      {"case":"nonintegral","spectrum":"ordered real nonintegral weight","orbit_real_dimension":-1,"image_dimension":-1,"regular_torus":"classical theorem only; no quantization assertion"},
    ]
    sections={"weight_rows":weights,"frequency_rows":freqs,"closure_basepoint_rows":CLOSURE_BASEPOINTS,"boundary_rows":boundaries}
    body={
      "schema":"hcs-c365-gelfand-tsetlin-evidence-v1","candidate_id":"HCS-C365","obstruction_id":"HEN-O349",
      "evaluation_date":"2026-09-04","source_commit":SOURCE,"fixed_epoch":1788480000,"scope_literal":"NO_BAD_EULER_OR_ROOT_NUMBER",
      "evaluator":{"authority":"flow_systems/skills/route-a-evaluator.md","version":"0.2.0","sha256":EVAL_SHA},
      "route_a_yaml":{"relative_path":"evaluations/route_a/HCS-C365/2026-09-04.yaml","raw_sha256":YAML_RAW,"semantic_sha256":YAML_SEM},
      "conventions":{"kks":"omega_A([X,A],[Y,A])=-i Tr(A[X,Y])","moment_pairing":"f_X(A)=-i Tr(AX)",
        "circle_period":"2*pi","prequantum_curvature":"-i omega","half_form":"absent","rho_shift":"none",
        "minor":"northwest principal minors","quantum_weight":"dominant integral U(3) highest weight"},
      "theorem_contract":{"image":"lambda1>=y1>=lambda2>=y2>=lambda3 and y1>=x>=y2, with explicit arrow completion",
        "regular_action":"strict interlacing fibers are effective Lagrangian T3 orbits",
        "linear_flow":"closure through theta0 is theta0+K_omega, where K_omega is the integer-relation annihilator and has Q-rank dimension; theta0+K_omega equals K_omega iff theta0 lies in K_omega; primitive rank-one direction gives least period 2*pi/alpha",
        "quantization":"no-half-form Borel-Weil branching basis is indexed by unshifted integral GT labels; no spectrum of unspecified quantum operators is asserted",
        "dimension":"(lambda1-lambda2+1)(lambda2-lambda3+1)(lambda1-lambda3+2)/2"},
      "finite_grid":{"gap_min":0,"gap_max":12,"weight_rows":169,"pattern_total":total,
                     "frequency_rows":len(freqs),"closure_basepoint_rows":len(CLOSURE_BASEPOINTS),
                     "boundary_rows":len(boundaries),"pattern_storage":"canonical per-weight exhaustive digests"},
      "collision_boundary":{"C298":"dissipative Grassmann and Schubert projection, not a KKS-Thimm system",
        "C313":"round-sphere geodesic and Laplacian dynamics, not nested-minor branching quantization",
        "C331":"rank-one monopole line-bundle quantization on S2, not a U(3) GT integrable system",
        "C349":"Neumann-sphere Uhlenbeck integrals, not a compact-group branching polytope"},
      "nonclaims":["no arithmetic local data","no target Euler factor or root number","no target functional equation or divisor",
        "no universal toric description of singular facets","no half-form or rho shift","no Hilbert-Polya operator","no Route B"],
      "references":[{"doi":"10.1016/0022-1236(83)90092-7","role":"Gelfand-Cetlin integrable-system and flag quantization lineage"},
                    {"doi":"10.1007/BF01398934","role":"geometric quantization and multiplicity lineage"}],
      "scope_flags":{k:False for k in ("claims_target_arithmetic_local_data","claims_target_euler_factors","claims_root_number","claims_automorphy",
        "claims_target_divisor_or_counting_law","claims_target_functional_equation","claims_target_zero_match","claims_hilbert_polya_operator","invokes_route_b")},
      "route_a":{"tuple":["A0_WEAK_ARITHMETIC_RELATION","A1_WEAK","A2_FAIL","A3_FAIL","A4_NATURAL_QUANTIZATION"],
        "overall":"ROUTE_A_EXPLORATORY","route_b_invocation_allowed":False,"theorem_status":"PROVABLE_AS_STATED"},
      "finite_evidence_role":"exact exhaustive finite pattern digests, frequency rows, and basepoint/coset-equality witnesses are regression evidence only; analytic proofs establish all general statements",
      **sections,"section_sha256":{k:digest(v) for k,v in sections.items()}}
    body["payload_sha256"]=digest(body)
    return body

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--output",type=Path,default=OUT);ap.add_argument("--evaluation",type=Path,default=YAML_PATH);a=ap.parse_args()
    obj=build(a.evaluation);a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_bytes(json.dumps(obj,sort_keys=True,indent=2,ensure_ascii=False).encode()+b"\n")
    print(f"C365 producer PASS: weights={len(obj['weight_rows'])} patterns={obj['finite_grid']['pattern_total']} frequencies={len(obj['frequency_rows'])} basepoints={len(obj['closure_basepoint_rows'])} payload={obj['payload_sha256']}")
if __name__=="__main__": main()
