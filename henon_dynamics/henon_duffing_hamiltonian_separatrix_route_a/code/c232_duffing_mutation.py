#!/usr/bin/env python3
"""Hostile mutation suite for the C232 certificate."""
from __future__ import annotations
from copy import deepcopy
from hashlib import sha256
import json, subprocess, sys, tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; EVIDENCE=ROOT/"results/c232_duffing_evidence.json"; CHECKER=Path(__file__).with_name("c232_duffing_checker.py")

def repair(d):
    b=dict(d); b.pop("payload_sha256",None); d["payload_sha256"]=sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def rejected(d,p):
    p.write_text(json.dumps(d,sort_keys=True,indent=2,ensure_ascii=False)+"\n"); return subprocess.run([sys.executable,"-B",str(CHECKER),"--quick","--evidence",str(p)],capture_output=True).returncode!=0

def main():
    original=json.loads(EVIDENCE.read_text())
    muts=[
        lambda d:d.__setitem__("source_commit","0"*40),
        lambda d:d.__setitem__("fixed_epoch",0),
        lambda d:d["evaluator"].__setitem__("sha256","0"*64),
        lambda d:d.__setitem__("scope_literal","BAD_SCOPE"),
        lambda d:d.__setitem__("candidate_id","HCS-C000"),
        lambda d:d["regression"]["energy_rows"][0].__setitem__("delta","999"),
        lambda d:d["regression"]["energy_rows"][0].__setitem__("regime","outer"),
        lambda d:d["regression"]["energy_rows"][1].__setitem__("component_count",9),
        lambda d:d["regression"]["energy_rows"][2].__setitem__("period","0"),
        lambda d:d["regression"]["energy_rows"][3].__setitem__("action","0"),
        lambda d:d["regression"]["energy_rows"][4]["selected_interval"].__setitem__(0,"0"),
        lambda d:d["regression"]["energy_rows"][5].__setitem__("turning_residual_left","1"),
        lambda d:d["route_a"].__setitem__("tuple",["A0_PASS"]*5),
        lambda d:d["route_a"].__setitem__("overall","ROUTE_A_STRONG_CANDIDATE"),
        lambda d:d["route_a"].__setitem__("route_b_invocation_allowed",True),
        lambda d:d["scope_flags"].__setitem__("claims_euler_factors",True),
        lambda d:d["citations"][0].__setitem__("doi","bad-doi"),
        lambda d:d.__setitem__("unknown_top_level_key",True),
        lambda d:d["regression"]["energy_rows"][0].__setitem__("unknown_nested_key",True),
    ]
    rej=0; unknown=0
    with tempfile.TemporaryDirectory() as td:
        p=Path(td)/"mutated.json"
        for i,m in enumerate(muts):
            d=deepcopy(original);m(d)
            if i>=len(muts)-2:unknown+=1
            repair(d)
            if not rejected(d,p):raise AssertionError(f"mutation {i} survived")
            rej+=1
        stale=deepcopy(original); stale["regression"]["energy_rows"][0]["period"]="777"
        if not rejected(stale,p):raise AssertionError("stale hash survived")
    print(json.dumps({"status":"C232_MUTATION_PASS","repaired_hash_rejections":rej,"stale_hash_rejections":1,"unknown_key_rejections":unknown,"total_rejections":rej+1},sort_keys=True))
if __name__=="__main__":main()
