#!/usr/bin/env python3
"""Hostile repaired-hash, nested-schema and stale-hash mutations for C225."""
from __future__ import annotations
from copy import deepcopy
from hashlib import sha256
import json, subprocess, sys, tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
EVIDENCE=ROOT/"results/c225_mm1k_evidence.json"
CHECKER=Path(__file__).with_name("c225_mm1k_checker.py")

def repair(d):
    b=dict(d); b.pop("payload_sha256",None)
    d["payload_sha256"]=sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def rejected(d,path):
    path.write_text(json.dumps(d,sort_keys=True,indent=2,ensure_ascii=False)+"\n")
    return subprocess.run([sys.executable,"-B",str(CHECKER),"--evidence",str(path)],capture_output=True).returncode != 0

def main():
    original=json.loads(EVIDENCE.read_text())
    muts=[
        lambda d:d.__setitem__("source_commit","0"*40),
        lambda d:d.__setitem__("fixed_epoch",0),
        lambda d:d["evaluator"].__setitem__("sha256","0"*64),
        lambda d:d.__setitem__("scope_literal","BAD_SCOPE"),
        lambda d:d.__setitem__("headline","synthetic"),
        lambda d:d["frozen_object"].__setitem__("generator","prime-fitted generator"),
        lambda d:d["frozen_object"].__setitem__("state_space","all primes"),
        lambda d:d["theorem"].__setitem__("spectrum","target zeros"),
        lambda d:d["theorem"].__setitem__("infinite_scope","continuous spectrum proved"),
        lambda d:d["route_a"].__setitem__("tuple",["A0_PASS"]*5),
        lambda d:d["route_a"].__setitem__("overall","ROUTE_A_STRONG_CANDIDATE"),
        lambda d:d["route_a"].__setitem__("route_b_invocation_allowed",True),
        lambda d:d["scope_flags"].__setitem__("claims_euler_factors",True),
        lambda d:d["citations"][0].__setitem__("url","https://doi.org/10.0000/bad"),
        lambda d:d["regression"].__setitem__("K_values",[99]),
        lambda d:d["regression"]["stationary_rows"][0].__setitem__("pi0","0"),
        lambda d:d["regression"]["stationary_rows"][1].__setitem__("weights",["1"]),
        lambda d:d["regression"]["spectral_rows"][0].__setitem__("eigenvalue","0"),
        lambda d:d["regression"]["spectral_rows"][1].__setitem__("eigenvector",["0"]),
        lambda d:d["regression"]["kernel_rows"][3].__setitem__("probabilities",["1"]),
        lambda d:d["regression"]["kernel_rows"][3].__setitem__("tv_bound","0"),
        lambda d:d["regression"]["limit_rows"][0].__setitem__("pi_state0","0"),
        lambda d:d["regression"]["boundary_rows"][0].__setitem__("condition","K=99"),
        lambda d:d.__setitem__("unknown_top_level_key",True),
        lambda d:d["regression"]["kernel_rows"][0].__setitem__("unknown_nested_key",True),
    ]
    repaired=0; unknown=0
    with tempfile.TemporaryDirectory() as td:
        path=Path(td)/"mutated.json"
        for idx,mut in enumerate(muts):
            d=deepcopy(original); mut(d)
            if idx>=len(muts)-2: unknown+=1
            repair(d)
            if not rejected(d,path): raise AssertionError(f"mutation {idx} survived")
            repaired+=1
        stale=deepcopy(original); stale["regression"]["kernel_rows"][0]["row_sum"]="777"
        if not rejected(stale,path): raise AssertionError("stale-hash mutation survived")
    print(json.dumps({"status":"C225_MUTATION_PASS","repaired_hash_rejections":repaired,"stale_hash_rejections":1,"unknown_key_rejections":unknown,"total_rejections":repaired+1},sort_keys=True))

if __name__ == "__main__": main()
