#!/usr/bin/env python3
"""Hostile repaired-hash mutations for HCS-C282."""
from __future__ import annotations
import copy, hashlib, json, os, subprocess, sys, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT/"results/c282_ruin_evidence.json"
def ph(d):
    c=dict(d); c.pop("payload_sha256",None)
    return hashlib.sha256(json.dumps(c,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def setp(d,p,v):
    t=d
    for k in p[:-1]: t=t[k]
    t[p[-1]]=v
base=json.loads(SOURCE.read_text())
mutations=[
 (("source_commit",),"0"*40),(("fixed_epoch",),1),(("scope_literal",),"BROKEN"),
 (("evaluator","sha256"),"0"*64),(("proof_contract","status"),"HEURISTIC"),
 (("route_a","tuple",1),"A1_WEAK"),(("route_a","route_b_invocation_allowed"),True),
 (("scope_flags","euler_factors"),True),(("regression","counts","transform_rows"),447),
 (("regression","regime_rows",0,"regime"),"BROKEN"),
 (("regression","transform_rows",0,"root"),"9"),
 (("regression","transform_rows",1,"joint_transform"),"9"),
 (("regression","first_mean_rows",0,"ruin_probability"),"1"),
 (("regression","martingale_rows",0,"martingale_exponent"),"1/1"),
 (("transform_contract","formula"),"BROKEN"),
 (("transform_contract","root_selection"),"boundedness always selects a unique root"),
 (("transform_contract","uniqueness"),"the exponential ansatz is assumed exhaustive"),
 (("transform_contract","u_zero_extension"),"u=0 excluded"),
 (("transform_contract","memoryless_factorization"),"conditional law asserted when nu=0"),
 (("model_contract","killed_owner"),"U is absorbed without defining a killed process"),
 (("regime_contract","conditional_first_mean_profitable"),"all conditional moments are proved"),
]
accepted=0
with tempfile.TemporaryDirectory(prefix="c282-mutation-") as temp:
    trials=[]
    for p,v in mutations:
        trial=copy.deepcopy(base); setp(trial,p,v); trial["payload_sha256"]=ph(trial)
        trials.append(trial)
    for section in ("transform_rows","first_mean_rows","martingale_rows"):
        trial=copy.deepcopy(base)
        trial["regression"][section][1]=copy.deepcopy(trial["regression"][section][0])
        trial["payload_sha256"]=ph(trial); trials.append(trial)
    trial=copy.deepcopy(base)
    trial["regression"]["boundary_rows"][0]["status"]="semantically corrupted boundary"
    trial["payload_sha256"]=ph(trial); trials.append(trial)
    for i,trial in enumerate(trials):
        path=Path(temp)/f"m{i}.json"; path.write_text(json.dumps(trial,sort_keys=True,indent=2,ensure_ascii=False)+"\n")
        env=dict(os.environ); env["C282_EVIDENCE"]=str(path); env["PYTHONDONTWRITEBYTECODE"]="1"
        run=subprocess.run([sys.executable,"-B",str(ROOT/"code/c282_ruin_checker.py")],env=env,
                           stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        accepted += run.returncode != 0
    stale=copy.deepcopy(base); stale["headline"] += " tampered"
    path=Path(temp)/"stale.json"; path.write_text(json.dumps(stale,sort_keys=True,indent=2,ensure_ascii=False)+"\n")
    env=dict(os.environ); env["C282_EVIDENCE"]=str(path); env["PYTHONDONTWRITEBYTECODE"]="1"
    run=subprocess.run([sys.executable,"-B",str(ROOT/"code/c282_ruin_checker.py")],env=env,
                       stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    accepted += run.returncode != 0
total=len(trials)+1
assert accepted==total
print(f"C282 hostile mutation audit: PASS {accepted}/{total} (repaired semantic mutations plus stale-hash control)")
