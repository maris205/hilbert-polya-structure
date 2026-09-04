#!/usr/bin/env python3
"""Hostile repaired-hash and parser mutation suite for C361."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("c361 mutation suite refuses optimized Python")
import copy, hashlib, json, subprocess, sys, tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1];CHECK=ROOT/"code/c361_markov_entropy_checker.py"
EVID=ROOT/"results/c361_markov_entropy_evidence.json";YAML=ROOT/"evaluations/route_a/HCS-C361/2026-09-04.yaml"
BASE=json.loads(EVID.read_text())
SECTIONS=("panel_rows","tree_rows","edge_rows","cycle_rows","tilt_rows","path_rows","boundary_rows")
def canon(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
def repair(x):
    x=copy.deepcopy(x)
    for s in SECTIONS:x["section_sha256"][s]=hashlib.sha256(canon(x[s])).hexdigest()
    x.pop("payload_sha256",None);x["payload_sha256"]=hashlib.sha256(canon(x)).hexdigest();return x
def run(evidence_bytes=None,yaml_bytes=None):
    with tempfile.TemporaryDirectory(prefix="c361-mut-") as td:
        ep=Path(td)/"e.json";yp=Path(td)/"e.yaml"
        ep.write_bytes(EVID.read_bytes() if evidence_bytes is None else evidence_bytes)
        yp.write_bytes(YAML.read_bytes() if yaml_bytes is None else yaml_bytes)
        return subprocess.run([sys.executable,str(CHECK),"--input",str(ep),"--evaluation",str(yp)],capture_output=True).returncode
def enc(x):return json.dumps(repair(x),sort_keys=True,indent=2,ensure_ascii=False).encode()+b"\n"
assert run()==0;killed=0;labels=[]
mut=[]
def add(label,fn):
    x=copy.deepcopy(BASE);fn(x);mut.append((label,enc(x),None))
add("candidate",lambda x:x.__setitem__("candidate_id","HCS-C000"))
add("date",lambda x:x.__setitem__("evaluation_date","2026-09-03"))
add("epoch",lambda x:x.__setitem__("fixed_epoch",0))
add("source",lambda x:x.__setitem__("source_commit","0"*40))
add("scope",lambda x:x.__setitem__("scope_literal","BROKEN"))
add("authority",lambda x:x["evaluator"].__setitem__("authority","wrong"))
add("eval-sha",lambda x:x["evaluator"].__setitem__("sha256","0"*64))
add("yaml-path",lambda x:x["route_a_yaml"].__setitem__("relative_path","wrong.yaml"))
add("model",lambda x:x["model"].__setitem__("support","directed"))
add("contract",lambda x:x["theorem_contract"].__setitem__("rate_function","unconditional"))
add("contract-rn-sign",lambda x:x["theorem_contract"].__setitem__("finite_time","dP^R/dP=exp(Sigma_T)"))
add("contract-tilt-transpose",lambda x:x["theorem_contract"].__setitem__("tilt","L_lambda^T=L_lambda"))
add("collision",lambda x:x["collision_boundary"].__setitem__("C342","same"))
add("nonclaim",lambda x:x["nonclaims"].__setitem__(0,"claims arithmetic"))
add("reference",lambda x:x["references"][0].__setitem__("doi","wrong"))
add("route-tuple",lambda x:x["route_a"]["tuple"].__setitem__(4,"A4_FORMAL_HINT"))
add("overall",lambda x:x["route_a"].__setitem__("overall","PASS"))
add("route-b",lambda x:x["route_a"].__setitem__("route_b_invocation_allowed",True))
add("flag",lambda x:x["scope_flags"].__setitem__("claims_target_euler_factors",True))
add("extra-top",lambda x:x.__setitem__("surprise",1))
add("missing-top",lambda x:x.pop("model"))
add("panel-rate",lambda x:x["panel_rows"][1]["rates"][0].__setitem__(1,9))
add("panel-extra",lambda x:x["panel_rows"][0].__setitem__("extra",1))
add("tree-weight",lambda x:x["tree_rows"][0].__setitem__("weight",999))
add("tree-parent",lambda x:x["tree_rows"][1]["parent_map"][0].__setitem__(1,0))
add("tree-extra",lambda x:x["tree_rows"][0].__setitem__("extra",1))
add("tree-omit",lambda x:x["tree_rows"].pop())
add("tree-duplicate",lambda x:x["tree_rows"].append(copy.deepcopy(x["tree_rows"][0])))
add("edge-current",lambda x:x["edge_rows"][0].__setitem__("current_ij","99"))
add("edge-extra",lambda x:x["edge_rows"][0].__setitem__("extra",1))
add("cycle-ratio",lambda x:x["cycle_rows"][0].__setitem__("cycle_affinity_ratio","99"))
add("tilt-coeff",lambda x:x["tilt_rows"][0]["characteristic_coefficients_descending"].__setitem__(0,"2"))
add("tilt-order",lambda x:x["tilt_rows"].__setitem__(0,x["tilt_rows"][1]))
add("path-ratio",lambda x:x["path_rows"][9].__setitem__("total_entropy_ratio","7"))
add("path-medium",lambda x:x["path_rows"][9].__setitem__("medium_ratio","7"))
add("path-boundary",lambda x:x["path_rows"][9].__setitem__("boundary_ratio","7"))
add("path-truncate",lambda x:x["path_rows"].pop())
add("path-duplicate",lambda x:x["path_rows"].append(copy.deepcopy(x["path_rows"][0])))
add("boundary",lambda x:x["boundary_rows"][0].__setitem__("status","wrong"))
add("grid",lambda x:x["finite_grid"].__setitem__("path_rows",0))
for label,eb,yb in mut:
    assert run(eb,yb)!=0,label;killed+=1;labels.append(label)
# stale-hash control
x=copy.deepcopy(BASE);x["path_rows"][0]["states"]=[9]
raw=json.dumps(x,sort_keys=True,indent=2).encode()+b"\n";assert run(raw)!=0;killed+=1;labels.append("stale-payload")
# strict JSON attacks
for label,raw in [("duplicate-json",EVID.read_bytes().replace(b'{\n  "boundary_rows"',b'{\n  "schema": "evil",\n  "boundary_rows"',1)),
                  ("nonfinite-json",EVID.read_bytes().replace(b'"fixed_epoch": 1788480000',b'"fixed_epoch": NaN',1))]:
    assert run(raw)!=0;killed+=1;labels.append(label)
# YAML hostile forms; evidence hash is deliberately repaired to the hostile raw/semantic when parseable.
yraw=YAML.read_text()
yaml_cases=[
 ("yaml-duplicate",yraw+"candidate_id: HCS-C361\n"),("yaml-merge","base: &b {x: 1}\nmerged: {<<: *b}\n"+yraw),
 ("yaml-nonstring","1: bad\n"+yraw),("yaml-alias","anchor: &a bad\nalias: *a\n"+yraw),
 ("yaml-timestamp",yraw.replace("evaluation_date: '2026-09-04'","evaluation_date: 2026-09-04")),
 ("yaml-unknown",yraw+"unknown_field: true\n"),("yaml-type",yraw.replace("fixed_epoch: 1788480000","fixed_epoch: '1788480000'")),
 ("yaml-authority",yraw.replace("evaluator_authority: flow_systems/skills/route-a-evaluator.md","evaluator_authority: wrong")),
 ("yaml-evidence-status",yraw.replace("evidence_status: STOP_SCOPED","evidence_status: PROVED",1)),
 ("yaml-artifact",yraw.replace("paper/main.pdf","paper/wrong.pdf")),
]
for label,text in yaml_cases:
    assert run(yaml_bytes=text.encode())!=0,label;killed+=1;labels.append(label)
print(f"C361 mutation PASS: killed={killed}/{len(labels)} stale_hash_control=1 repaired_hash_attacks={len(mut)}")
