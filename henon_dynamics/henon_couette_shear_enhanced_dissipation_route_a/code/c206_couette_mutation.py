#!/usr/bin/env python3
"""Repaired/stale hostile mutations for HCS-C206."""
from copy import deepcopy
from hashlib import sha256
import json, subprocess, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; EVIDENCE=ROOT/"results/c206_couette_evidence.json"; CHECKER=Path(__file__).with_name("c206_couette_checker.py")
def repair(d):
    body=dict(d); body.pop("payload_sha256",None); d["payload_sha256"]=sha256(json.dumps(body,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def rejected(d,p):
    p.write_text(json.dumps(d,sort_keys=True,indent=2,ensure_ascii=False)+"\n"); return subprocess.run([sys.executable,str(CHECKER),"--evidence",str(p)],capture_output=True).returncode!=0
def main():
    original=json.loads(EVIDENCE.read_text())
    attacks=[
      ("source",lambda d:d.__setitem__("source_commit","0"*40)),
      ("evaluator",lambda d:d["evaluator"].__setitem__("sha256","0"*64)),
      ("scope",lambda d:d["scope_flags"].__setitem__("claims_euler_factors",True)),
      ("route",lambda d:d["route_a"].__setitem__("overall","ROUTE_A_STRONG_CANDIDATE")),
      ("tuple",lambda d:d["route_a"].__setitem__("tuple",["A0_ANALYTIC_ARITHMETIC_ORIGIN"]*5)),
      ("shift_sign",lambda d:d["regression"]["fourier_cells"][1].__setitem__("shift","999")),
      ("cubic_factor",lambda d:d["regression"]["fourier_cells"][400].__setitem__("sector_minimum","0")),
      ("heat_term",lambda d:d["regression"]["fourier_cells"][674].__setitem__("dissipation_exponent","1")),
      ("multiplier",lambda d:d["regression"]["fourier_cells"][500].__setitem__("multiplier","2")),
      ("composition",lambda d:d["regression"]["composition_cells"][10].__setitem__("combined","7")),
      ("norm_attainment",lambda d:d["theorem"].__setitem__("sector_norm_attainment","a nonzero L2 maximizer exists for nu*t>0")),
      ("periodic_scope",lambda d:d["theorem"].__setitem__("periodic_states","every state is periodic")),
      ("trace_class",lambda d:d["theorem"].__setitem__("trace_stop","the semigroup is trace class")),
      ("fourier_convention",lambda d:d["frozen_object"].__setitem__("fourier_convention","opposite unrecorded sign")),
      ("unknown_key",lambda d:d["theorem"].__setitem__("unsafe_extra","x")),
      ("citation",lambda d:d["citations"][0].__setitem__("doi","fake")),
      ("precision_declaration",lambda d:d["summary"].__setitem__("serialized_significant_digits",100)),
    ]
    with tempfile.TemporaryDirectory() as td:
        p=Path(td)/"mutant.json"
        for name,fn in attacks:
            x=deepcopy(original); fn(x); repair(x)
            if not rejected(x,p): raise AssertionError(name+" survived")
        stale=deepcopy(original); stale["regression"]["fourier_cells"][0]["shift"]="123"
        if not rejected(stale,p): raise AssertionError("stale hash survived")
    print(json.dumps({"status":"C206_MUTATION_PASS","repaired_hash_rejections":len(attacks),"stale_hash_rejections":1,"unknown_key_rejections":1,"precision_contract_rejections":1,"mathematical_hostile_rejections":8},sort_keys=True))
if __name__=="__main__": main()
