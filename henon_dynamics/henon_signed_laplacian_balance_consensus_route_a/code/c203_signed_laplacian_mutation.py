#!/usr/bin/env python3
"""Hostile repaired/stale-hash and unknown-schema attacks for C203."""
from copy import deepcopy
from hashlib import sha256
import json,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; E=ROOT/"results/c203_signed_laplacian_evidence.json"; C=Path(__file__).with_name("c203_signed_laplacian_checker.py")
def repair(d):
    b=dict(d); b.pop("payload_sha256",None); d["payload_sha256"]=sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def rejected(d,p):
    p.write_text(json.dumps(d,sort_keys=True,indent=2,ensure_ascii=False)+"\n"); return subprocess.run([sys.executable,str(C),"--evidence",str(p)],capture_output=True).returncode!=0
def main():
    o=json.loads(E.read_text()); attacks=[
        ("source",lambda d:d.__setitem__("source_commit","0"*40)),("evaluator",lambda d:d["evaluator"].__setitem__("sha256","0"*64)),
        ("scope",lambda d:d["scope_flags"].__setitem__("claims_root_numbers",True)),("route",lambda d:d["route_a"].__setitem__("overall","ROUTE_A_STRONG_CANDIDATE")),
        ("tuple",lambda d:d["route_a"].__setitem__("tuple",["A0_PASS"]*5)),("minor",lambda d:d["exhaustive_regression"]["graphs"][0]["principal_minors"][0].__setitem__("matrix_determinant",2)),
        ("pseudoforest",lambda d:d["exhaustive_regression"]["graphs"][100]["principal_minors"][1].__setitem__("pseudoforest_sum",99)),
        ("charpoly",lambda d:d["exhaustive_regression"]["graphs"][759]["characteristic_coefficients_pseudoforest"].__setitem__(0,123)),
        ("nullity",lambda d:d["exhaustive_regression"]["graphs"][50].__setitem__("nullity",9)),
        ("bridge",lambda d:d["counterexamples"]["bridge_negative_triangle"].__setitem__("delete_root_0_cofactor",3)),
        ("directed",lambda d:d["counterexamples"]["directed_exclusion"].__setitem__("orthogonal_projector",True)),
        ("unknown_key",lambda d:d["theorem"].__setitem__("unsafe_extension","directed")),
    ]
    with tempfile.TemporaryDirectory() as z:
        p=Path(z)/"m.json"; repaired=0
        for name,fn in attacks:
            d=deepcopy(o); fn(d); repair(d)
            if not rejected(d,p): raise AssertionError(name+" survived")
            repaired+=1
        d=deepcopy(o); d["summary"]["principal_minor_checks"]=1
        if not rejected(d,p): raise AssertionError("stale hash survived")
    print(json.dumps({"status":"C203_MUTATION_PASS","repaired_hash_rejections":repaired,"stale_hash_rejections":1,"unknown_key_rejections":1,"mathematical_hostile_rejections":6},sort_keys=True))
if __name__=="__main__": main()
