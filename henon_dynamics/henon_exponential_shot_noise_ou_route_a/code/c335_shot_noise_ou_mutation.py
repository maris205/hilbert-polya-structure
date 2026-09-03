#!/usr/bin/env python3
"""Hostile repaired-hash and strict-parser suite for HCS-C335."""
import copy,hashlib,json,subprocess,sys,tempfile
from pathlib import Path
if sys.flags.optimize:raise RuntimeError("C335 mutation lane refuses optimized Python")
root=Path(__file__).resolve().parents[1];evidence=root/"results/c335_shot_noise_ou_evidence.json";evaluation=root/"evaluations/route_a/HCS-C335/2026-09-03.yaml";checker=root/"code/c335_shot_noise_ou_checker.py";source=json.loads(evidence.read_text())
def repair(d):
    body=dict(d);body.pop("payload_sha256",None);d["payload_sha256"]=hashlib.sha256(json.dumps(body,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
mutators=[
 lambda d:d.__setitem__("candidate_id","HCS-C334"),lambda d:d.__setitem__("source_commit","0"*40),lambda d:d["evaluator"].__setitem__("authority","wrong"),lambda d:d["evaluation_lock"].__setitem__("semantic_sha256","0"*64),
 lambda d:d["model"].__setitem__("positive_parameters","gamma may vanish"),lambda d:d["theorem_contract"].__setitem__("spectral_boundary","full L2 spectrum"),lambda d:d["boundary_atlas"].pop(),lambda d:d["collision_boundary"].__setitem__("C999","invented"),lambda d:d["references"][0].__setitem__("doi","fake"),lambda d:d["nonclaims"].pop(),
 lambda d:d["route_a"].__setitem__("overall","ROUTE_A_PASS"),lambda d:d["scope_flags"].__setitem__("claims_target_euler_factors",True),lambda d:d["parameter_rows"][0].__setitem__("alpha","2/4"),lambda d:d["parameter_rows"][1]["stationary_moments_0_to_12"].pop(),
 lambda d:d["transition_rows"][0].__setitem__("transition_laplace","nan"),lambda d:d["transition_rows"][1].__setitem__("decay_factor","1/2"),lambda d:d["semigroup_rows"][0].__setitem__("factor_direct","nan"),lambda d:d["semigroup_rows"].__setitem__(1,copy.deepcopy(d["semigroup_rows"][0])),
 lambda d:d["polynomial_rows"][1]["coefficients_low_to_high"].__setitem__(0,"0"),lambda d:d["polynomial_rows"][2].__setitem__("diagonal","-8/2"),lambda d:d["polynomial_rows"][3].__setitem__("extra",1),lambda d:d["enumeration"].__setitem__("extra",1),lambda d:d["enumeration"].__setitem__("audited_leaf_count",0),
]
attempts=0
with tempfile.TemporaryDirectory(prefix="c335-mutations-") as td:
    td=Path(td)
    for i,mutate in enumerate(mutators):
        for fixed in (False,True):
            data=copy.deepcopy(source);mutate(data)
            if fixed:repair(data)
            path=td/f"e-{i}-{int(fixed)}.json";path.write_text(json.dumps(data,sort_keys=True,indent=2)+"\n")
            if subprocess.run([sys.executable,"-B",str(checker),"--evidence",str(path)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT).returncode==0:raise AssertionError(f"survived {i}/{fixed}")
            attempts+=1
    raw=evidence.read_text()
    for i,text in enumerate((raw.replace('"candidate_id": "HCS-C335",','"candidate_id": "HCS-C335",\n  "candidate_id": "dup",',1),raw.replace('"fixed_epoch": 1788393600','"fixed_epoch": Infinity',1))):
        path=td/f"json-{i}";path.write_text(text)
        if subprocess.run([sys.executable,"-B",str(checker),"--evidence",str(path)],stdout=subprocess.PIPE).returncode==0:raise AssertionError("JSON parser")
        attempts+=1
    raw=evaluation.read_text();attacks=(raw.replace("HCS-C335","HCS-C334",1),raw.replace("evaluation_date: '2026-09-03'","evaluation_date: 2026-09-03",1),raw.replace("  evidence_status: STOP_SCOPED\n","",1),raw.replace("A0_FAIL","A0_PASS",1),raw.replace("route_b_invocation_allowed: false","route_b_invocation_allowed: true",1),raw.replace("evaluator_authority: flow_systems/skills/route-a-evaluator.md","evaluator_authority: wrong",1),raw+"candidate_id: duplicate\n","base: &b\n  x: y\ncopy: *b\n"+raw,raw.replace("a0:\n","a0:\n  <<: {verdict: A0_FAIL}\n",1),raw.replace("candidate_id: HCS-C335","1: HCS-C335",1),raw.replace("artifact_paths:\n  - results","artifact_paths: results",1),raw.replace("theorem_status: PROVABLE_AS_STATED","unknown: x\ntheorem_status: PROVABLE_AS_STATED",1))
    for i,text in enumerate(attacks):
        path=td/f"yaml-{i}.yaml";path.write_text(text)
        if subprocess.run([sys.executable,"-B",str(checker),"--evaluation",str(path)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT).returncode==0:raise AssertionError(f"YAML attack {i}")
        attempts+=1
print(f"C335 hostile mutation suite: PASS ({attempts}/{attempts} rejected)")
