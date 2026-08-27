#!/usr/bin/env python3
"""Repaired/stale-hash and schema/math hostile mutations for C199."""
from copy import deepcopy
from hashlib import sha256
import json, subprocess, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; EVIDENCE=ROOT/"results/c199_chaplygin_evidence.json"; CHECKER=Path(__file__).with_name("c199_chaplygin_checker.py")
def repair(d):
    body=dict(d); body.pop("payload_sha256",None); d["payload_sha256"]=sha256(json.dumps(body,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def rejected(d,p):
    p.write_text(json.dumps(d,sort_keys=True,indent=2,ensure_ascii=False)+"\n"); return subprocess.run([sys.executable,str(CHECKER),"--evidence",str(p)],capture_output=True).returncode!=0
def main():
    original=json.loads(EVIDENCE.read_text())
    attacks=[
        ("source_lock",lambda d:d.__setitem__("source_commit","0"*40)),
        ("evaluator",lambda d:d["evaluator"].__setitem__("sha256","0"*64)),
        ("scope",lambda d:d["scope_flags"].__setitem__("claims_euler_factors",True)),
        ("route",lambda d:d["route_a"].__setitem__("overall","ROUTE_A_STRONG_CANDIDATE")),
        ("tuple",lambda d:d["route_a"].__setitem__("tuple",["A0_PASS"]*5)),
        ("parameter_sign",lambda d:d["regression"]["heteroclinic_cases"][0]["parameters"].__setitem__("m","-1")),
        ("energy",lambda d:d["regression"]["heteroclinic_cases"][1]["samples"][0].__setitem__("energy","99")),
        ("scattering",lambda d:d["regression"]["heteroclinic_cases"][2]["derived"].__setitem__("blade_angle_deflection","0")),
        ("stable_half_axis",lambda d:d["regression"]["heteroclinic_cases"][3]["derived"].__setitem__("transverse_eigenvalue_at_u_plus","1")),
        ("zero_boundary",lambda d:d["regression"]["zero_offset_cases"][0].__setitem__("period","1")),
        ("density_scope",lambda d:d["theorem"].__setitem__("measure","no positive full-flow density exists")),
        ("unknown_key",lambda d:d["theorem"].__setitem__("surprise","unsafe")),
    ]
    repaired=0
    with tempfile.TemporaryDirectory() as d:
        p=Path(d)/"m.json"
        for name,fn in attacks:
            x=deepcopy(original); fn(x); repair(x)
            if not rejected(x,p): raise AssertionError(name+" survived")
            repaired+=1
        stale=deepcopy(original); stale["regression"]["heteroclinic_cases"][0]["samples"][0]["u"]="123"
        if not rejected(stale,p): raise AssertionError("stale hash survived")
    print(json.dumps({"status":"C199_MUTATION_PASS","repaired_hash_rejections":repaired,"stale_hash_rejections":1,"unknown_key_rejections":1,"mathematical_hostile_rejections":4},sort_keys=True))
if __name__=="__main__": main()
