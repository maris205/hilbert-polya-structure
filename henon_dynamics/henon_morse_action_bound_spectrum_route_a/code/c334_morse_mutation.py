#!/usr/bin/env python3
"""Hostile repaired-hash and strict-parser suite for HCS-C334."""
import copy,hashlib,json,subprocess,sys,tempfile
from pathlib import Path
if sys.flags.optimize:raise RuntimeError("C334 mutation lane refuses optimized Python")
root=Path(__file__).resolve().parents[1]; evidence=root/"results/c334_morse_evidence.json"; evaluation=root/"evaluations/route_a/HCS-C334/2026-09-03.yaml"; checker=root/"code/c334_morse_checker.py"; source=json.loads(evidence.read_text())
def repair(d):
    body=dict(d);body.pop("payload_sha256",None);d["payload_sha256"]=hashlib.sha256(json.dumps(body,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
mutators=[
 lambda d:d.__setitem__("candidate_id","HCS-C335"),lambda d:d.__setitem__("evaluation_date","2026-09-02"),lambda d:d["evaluator"].__setitem__("authority","wrong"),lambda d:d["evaluation_lock"].__setitem__("raw_sha256","0"*64),
 lambda d:d["model"].__setitem__("action_normalization","unscaled integral"),lambda d:d["theorem_contract"].__setitem__("spectral_boundary","threshold is L2"),lambda d:d["boundary_atlas"].pop(),lambda d:d["collision_boundary"].__setitem__("C999","invented"),
 lambda d:d["nonclaims"].pop(),lambda d:d["references"][0].__setitem__("doi","10.0000/fake"),lambda d:d["route_a"]["tuple"].__setitem__(0,"A0_PASS"),lambda d:d["scope_flags"].__setitem__("claims_target_zero_match",True),
 lambda d:d["classical_rows"][1].__setitem__("sigma","3/5"),lambda d:d["classical_rows"][2].__setitem__("energy_over_D","-8/2"),lambda d:d["classical_rows"][3].__setitem__("extra",1),lambda d:d["classical_rows"].__setitem__(4,copy.deepcopy(d["classical_rows"][3])),
 lambda d:d["bound_count_rows"][2].__setitem__("bound_state_count",9),lambda d:d["bound_level_rows"][0].__setitem__("energy_over_scale","0"),lambda d:d["bound_level_rows"][1]["laguerre_coefficients_low_to_high"].pop(),lambda d:d["bound_level_rows"][2].__setitem__("decay_exponent","0"),
 lambda d:d["threshold_rows"][0].__setitem__("l2_status","included"),lambda d:d["enumeration"].__setitem__("extra",1),lambda d:d["enumeration"].__setitem__("audited_leaf_count",0),
]
attempts=0
with tempfile.TemporaryDirectory(prefix="c334-mutations-") as td:
    td=Path(td)
    for i,mutate in enumerate(mutators):
        for fixed in (False,True):
            data=copy.deepcopy(source);mutate(data)
            if fixed:repair(data)
            path=td/f"e-{i}-{int(fixed)}.json";path.write_text(json.dumps(data,sort_keys=True,indent=2)+"\n")
            if subprocess.run([sys.executable,"-B",str(checker),"--evidence",str(path)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT).returncode==0:raise AssertionError(f"survived {i}/{fixed}")
            attempts+=1
    raw=evidence.read_text()
    for i,text in enumerate((raw.replace('"candidate_id": "HCS-C334",','"candidate_id": "HCS-C334",\n  "candidate_id": "dup",',1),raw.replace('"fixed_epoch": 1788393600','"fixed_epoch": NaN',1))):
        path=td/f"json-{i}";path.write_text(text)
        if subprocess.run([sys.executable,"-B",str(checker),"--evidence",str(path)],stdout=subprocess.PIPE).returncode==0:raise AssertionError("JSON parser attack")
        attempts+=1
    raw=evaluation.read_text()
    attacks=(raw.replace("HCS-C334","HCS-C335",1),raw.replace("evaluation_date: '2026-09-03'","evaluation_date: 2026-09-03",1),raw.replace("A1_PASS_ANALYTIC","A1_FAIL",1),raw.replace("A4_NATURAL_QUANTIZATION","A4_FAIL",1),raw.replace("route_b_invocation_allowed: false","route_b_invocation_allowed: true",1),raw.replace("evaluator_authority: flow_systems/skills/route-a-evaluator.md","evaluator_authority: wrong",1),raw.replace("  evidence_status: PROVED\n","",1),raw+"candidate_id: duplicate\n","base: &b\n  x: y\ncopy: *b\n"+raw,raw.replace("a0:\n","a0:\n  <<: {verdict: A0_FAIL}\n",1),raw.replace("candidate_id: HCS-C334","1: HCS-C334",1),raw.replace("artifact_paths:\n  - results","artifact_paths: results",1),raw.replace("theorem_status: PROVABLE_AS_STATED","unknown: x\ntheorem_status: PROVABLE_AS_STATED",1))
    for i,text in enumerate(attacks):
        path=td/f"yaml-{i}.yaml";path.write_text(text)
        if subprocess.run([sys.executable,"-B",str(checker),"--evaluation",str(path)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT).returncode==0:raise AssertionError(f"YAML attack {i}")
        attempts+=1
print(f"C334 hostile mutation suite: PASS ({attempts}/{attempts} rejected)")
