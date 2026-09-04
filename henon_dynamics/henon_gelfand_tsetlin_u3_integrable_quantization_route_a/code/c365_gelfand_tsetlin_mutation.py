#!/usr/bin/env python3
"""Repaired-hash hostile mutation suite for HCS-C365."""
from __future__ import annotations
if not __debug__: raise RuntimeError("c365 mutation suite refuses optimized Python")
import argparse, copy, hashlib, json, subprocess, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];CHECK=ROOT/"code/c365_gelfand_tsetlin_checker.py"
EVID=ROOT/"results/c365_gelfand_tsetlin_evidence.json";YAML=ROOT/"evaluations/route_a/HCS-C365/2026-09-04.yaml"
SECTIONS=("weight_rows","frequency_rows","closure_basepoint_rows","boundary_rows")
def canon(x): return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
def repair(x):
    x=copy.deepcopy(x)
    for s in SECTIONS:x["section_sha256"][s]=hashlib.sha256(canon(x[s])).hexdigest()
    x.pop("payload_sha256",None);x["payload_sha256"]=hashlib.sha256(canon(x)).hexdigest();return x
def enc(x): return json.dumps(repair(x),sort_keys=True,indent=2,ensure_ascii=False).encode()+b"\n"
def run(eb=None,yb=None):
    with tempfile.TemporaryDirectory(prefix="c365-mut-") as td:
        ep=Path(td)/"e.json";yp=Path(td)/"e.yaml";ep.write_bytes(EVID.read_bytes() if eb is None else eb);yp.write_bytes(YAML.read_bytes() if yb is None else yb)
        return subprocess.run([sys.executable,str(CHECK),"--input",str(ep),"--evaluation",str(yp)],capture_output=True).returncode
def main():
    argparse.ArgumentParser().parse_args();base=json.loads(EVID.read_text());assert run()==0
    cases=[]
    def add(label,fn):
        x=copy.deepcopy(base);fn(x);cases.append((label,enc(x)))
    add("candidate",lambda x:x.__setitem__("candidate_id","HCS-C000"));add("obstruction",lambda x:x.__setitem__("obstruction_id","HEN-O000"))
    add("date",lambda x:x.__setitem__("evaluation_date","2026-09-03"));add("source",lambda x:x.__setitem__("source_commit","0"*40))
    add("epoch",lambda x:x.__setitem__("fixed_epoch",0));add("scope",lambda x:x.__setitem__("scope_literal","BROKEN"))
    add("authority",lambda x:x["evaluator"].__setitem__("authority","wrong"));add("authority-version",lambda x:x["evaluator"].__setitem__("version","9"))
    add("authority-sha",lambda x:x["evaluator"].__setitem__("sha256","0"*64));add("yaml-path",lambda x:x["route_a_yaml"].__setitem__("relative_path","wrong"))
    add("yaml-raw",lambda x:x["route_a_yaml"].__setitem__("raw_sha256","0"*64));add("yaml-sem",lambda x:x["route_a_yaml"].__setitem__("semantic_sha256","0"*64))
    add("kks-sign",lambda x:x["conventions"].__setitem__("kks","+i Tr"));add("period",lambda x:x["conventions"].__setitem__("circle_period","pi"))
    add("half-form",lambda x:x["conventions"].__setitem__("half_form","present"));add("rho",lambda x:x["conventions"].__setitem__("rho_shift","rho"))
    add("minor",lambda x:x["conventions"].__setitem__("minor","southeast"));add("contract-image",lambda x:x["theorem_contract"].__setitem__("image","wrong"))
    add("contract-torus",lambda x:x["theorem_contract"].__setitem__("regular_action","all facets T3"));add("contract-coset",lambda x:x["theorem_contract"].__setitem__("linear_flow","every initial-phase closure is the subgroup K_omega"))
    add("contract-basepoint-only-zero",lambda x:x["theorem_contract"].__setitem__("linear_flow","theta0+K_omega equals K_omega only when theta0=0"))
    add("contract-label",lambda x:x["theorem_contract"].__setitem__("quantization","unspecified operator eigenvalues with a rho shift"));add("contract-dim",lambda x:x["theorem_contract"].__setitem__("dimension","wrong"))
    add("collision",lambda x:x["collision_boundary"].__setitem__("C331","same"));add("nonclaim",lambda x:x["nonclaims"].__setitem__(0,"claims local data"))
    add("reference",lambda x:x["references"][0].__setitem__("doi","wrong"));add("flag",lambda x:x["scope_flags"].__setitem__("claims_target_euler_factors",True))
    add("tuple",lambda x:x["route_a"]["tuple"].__setitem__(0,"A0_PASS"));add("overall",lambda x:x["route_a"].__setitem__("overall","ROUTE_A_ACCEPTED"))
    add("route-b",lambda x:x["route_a"].__setitem__("route_b_invocation_allowed",True));add("theorem-status",lambda x:x["route_a"].__setitem__("theorem_status","OPEN"))
    add("evidence-role",lambda x:x.__setitem__("finite_evidence_role","proof by enumeration"));add("extra-top",lambda x:x.__setitem__("extra",1))
    add("missing-top",lambda x:x.pop("conventions"));add("weight-a",lambda x:x["weight_rows"][0].__setitem__("a",99))
    add("weight-lambda",lambda x:x["weight_rows"][4]["lambda"].__setitem__(0,99));add("weight-count",lambda x:x["weight_rows"][9].__setitem__("pattern_count",0))
    add("weight-weyl",lambda x:x["weight_rows"][12].__setitem__("weyl_dimension",0));add("weight-strict",lambda x:x["weight_rows"][20].__setitem__("strict_pattern_count",9))
    add("weight-digest",lambda x:x["weight_rows"][30].__setitem__("pattern_digest","0"*64));add("weight-extra",lambda x:x["weight_rows"][0].__setitem__("extra",1))
    add("weight-omit",lambda x:x["weight_rows"].pop());add("weight-duplicate",lambda x:x["weight_rows"].append(copy.deepcopy(x["weight_rows"][0])))
    add("weight-type",lambda x:x["weight_rows"][0].__setitem__("b","0"));add("freq-coeff",lambda x:x["frequency_rows"][1]["coefficient_rows"][0].__setitem__(0,9))
    add("freq-rank",lambda x:x["frequency_rows"][5].__setitem__("rational_rank",1));add("freq-period",lambda x:x["frequency_rows"][2].__setitem__("least_period","2*pi"))
    add("freq-direction",lambda x:x["frequency_rows"][4].__setitem__("primitive_direction","[1,1,1]"));add("freq-extra",lambda x:x["frequency_rows"][0].__setitem__("extra",1))
    add("freq-omit",lambda x:x["frequency_rows"].pop());add("boundary-overclaim",lambda x:x["boundary_rows"][4].__setitem__("regular_torus","T3"))
    add("basepoint-rank3-zero",lambda x:x["closure_basepoint_rows"][0].__setitem__("theta0_over_pi",["0","0","0"]))
    add("basepoint-inside-false",lambda x:x["closure_basepoint_rows"][1].__setitem__("theta0_in_K",False))
    add("basepoint-outside-true",lambda x:x["closure_basepoint_rows"][2].__setitem__("coset_equals_K",True))
    add("basepoint-bool-int",lambda x:x["closure_basepoint_rows"][1].__setitem__("theta0_in_K",1))
    add("basepoint-extra",lambda x:x["closure_basepoint_rows"][0].__setitem__("extra",1))
    add("basepoint-omit",lambda x:x["closure_basepoint_rows"].pop())
    add("boundary-repeat",lambda x:x["boundary_rows"][1].__setitem__("regular_torus","T3"));add("boundary-extra",lambda x:x["boundary_rows"][0].__setitem__("extra",1))
    add("grid-total",lambda x:x["finite_grid"].__setitem__("pattern_total",1));add("grid-storage",lambda x:x["finite_grid"].__setitem__("pattern_storage","sampled"))
    add("bool-scope-flag",lambda x:x["scope_flags"].__setitem__("claims_root_number",0))
    add("bool-route-b",lambda x:x["route_a"].__setitem__("route_b_invocation_allowed",0))
    add("bool-rank-one",lambda x:x["frequency_rows"][1].__setitem__("rational_rank",True))
    add("bool-rank-zero",lambda x:x["frequency_rows"][0].__setitem__("rational_rank",False))
    add("bool-boundary-dimension",lambda x:x["boundary_rows"][3].__setitem__("orbit_real_dimension",False))
    add("bool-pattern-count",lambda x:x["weight_rows"][0].__setitem__("pattern_count",True))
    add("bool-weyl-dimension",lambda x:x["weight_rows"][0].__setitem__("weyl_dimension",True))
    add("float-grid-count",lambda x:x["finite_grid"].__setitem__("frequency_rows",8.0))
    add("float-basepoint-count",lambda x:x["finite_grid"].__setitem__("closure_basepoint_rows",3.0))
    add("float-epoch",lambda x:x.__setitem__("fixed_epoch",1788480000.0))
    killed=0
    for label,blob in cases: assert run(blob)!=0,label;killed+=1
    stale=copy.deepcopy(base);stale["weight_rows"][0]["pattern_count"]=9
    assert run(json.dumps(stale,sort_keys=True,indent=2).encode()+b"\n")!=0;killed+=1
    raw=EVID.read_bytes()
    for label,blob in (("duplicate-json",raw.replace(b'{\n  "boundary_rows"',b'{\n  "schema": "evil",\n  "boundary_rows"',1)),
                       ("nonfinite-json",raw.replace(b'"fixed_epoch": 1788480000',b'"fixed_epoch": NaN',1))):
        assert run(blob)!=0,label;killed+=1
    y=YAML.read_text();ycases=[
      ("yaml-duplicate",y+"candidate_id: HCS-C365\n"),("yaml-merge","base: &b {x: 1}\nmerged: {<<: *b}\n"+y),("yaml-nonstring","1: bad\n"+y),
      ("yaml-alias","anchor: &a bad\nalias: *a\n"+y),("yaml-timestamp",y.replace("evaluation_date: '2026-09-04'","evaluation_date: 2026-09-04")),
      ("yaml-unknown",y+"unknown_field: true\n"),("yaml-type",y.replace("fixed_epoch: 1788480000","fixed_epoch: '1788480000'")),
      ("yaml-authority",y.replace("evaluator_authority: flow_systems/skills/route-a-evaluator.md","evaluator_authority: wrong")),
      ("yaml-status",y.replace("evidence_status: STOP_SCOPED","evidence_status: PROVED",1)),
      ("yaml-path",y.replace("paper/main.pdf","paper/wrong.pdf")),("yaml-tuple",y.replace("  - A4_NATURAL_QUANTIZATION","  - A4_FAIL")),
      ("yaml-route-b",y.replace("route_b_invocation_allowed: false","route_b_invocation_allowed: true"))]
    for label,text in ycases: assert run(yb=text.encode())!=0,label;killed+=1
    print(f"C365 mutation PASS: killed={killed}/{len(cases)+15} repaired_hash_attacks={len(cases)} stale_hash_control=1")
if __name__=="__main__": main()
