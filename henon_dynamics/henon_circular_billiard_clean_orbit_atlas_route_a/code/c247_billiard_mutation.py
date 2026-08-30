#!/usr/bin/env python3
"""Hostile repaired-hash semantic mutation suite for C247."""
from __future__ import annotations
import sys
sys.dont_write_bytecode=True
from copy import deepcopy
from hashlib import sha256
import json, os, subprocess, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; EVIDENCE=ROOT/"results/c247_billiard_evidence.json"; CHECKER=ROOT/"code/c247_billiard_checker.py"
def repair(d):
    b=dict(d);b.pop("payload_sha256",None);d["payload_sha256"]=sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest();return d
def main():
    pristine=json.loads(EVIDENCE.read_text()); muts=[]
    def add(name,fn,repaired=True):
        x=deepcopy(pristine);fn(x)
        if repaired:repair(x)
        muts.append((name,x))
    add("source",lambda x:x.__setitem__("source_commit","0"*40)); add("evaluator",lambda x:x["evaluator"].__setitem__("sha256","0"*64)); add("schema",lambda x:x.__setitem__("schema","bad")); add("route",lambda x:x["route_a"]["tuple"].__setitem__(1,"A1_FAIL")); add("route_b",lambda x:x["route_a"].__setitem__("route_b_invocation_allowed",True)); add("scope",lambda x:x["scope_flags"].__setitem__("claims_euler_factors",True)); add("unknown",lambda x:x.__setitem__("unknown",1))
    add("primitive_m",lambda x:x["regression"]["primitive_rows"][0].__setitem__("m",2)); add("primitive_alpha",lambda x:x["regression"]["primitive_rows"][1].__setitem__("alpha","0")); add("primitive_p",lambda x:x["regression"]["primitive_rows"][2].__setitem__("p","0")); add("primitive_fraction",lambda x:x["regression"]["primitive_rows"][3].__setitem__("rotation_fraction","9/9")); add("primitive_length",lambda x:x["regression"]["primitive_rows"][4].__setitem__("primitive_length","0")); add("primitive_action",lambda x:x["regression"]["primitive_rows"][5].__setitem__("action_length","0")); add("primitive_caustic",lambda x:x["regression"]["primitive_rows"][6].__setitem__("caustic_radius","0")); add("primitive_shear",lambda x:x["regression"]["primitive_rows"][7]["return_map_derivative"].__setitem__(0,["1","99"])); add("primitive_kernel",lambda x:x["regression"]["primitive_rows"][8].__setitem__("return_kernel","wrong")); add("primitive_det",lambda x:x["regression"]["primitive_rows"][9].__setitem__("det_identity_minus_return","1")); add("primitive_orientation",lambda x:x["regression"]["primitive_rows"][10].__setitem__("orientation","x")); add("primitive_cheb",lambda x:x["regression"]["primitive_rows"][11].__setitem__("chebyshev_residual","1"));
    add("repeat_k",lambda x:x["regression"]["repetition_rows"][0].__setitem__("repetition_k",9)); add("repeat_length",lambda x:x["regression"]["repetition_rows"][1].__setitem__("repeated_length","0")); add("repeat_action",lambda x:x["regression"]["repetition_rows"][2].__setitem__("repeated_action","0")); add("repeat_status",lambda x:x["regression"]["repetition_rows"][3].__setitem__("repetition_status","merged"));
    add("boundary_alpha",lambda x:x["regression"]["boundary_rows"][0].__setitem__("alpha","0")); add("boundary_kind",lambda x:x["regression"]["boundary_rows"][1].__setitem__("return_matrix_kind","unipotent_shear")); add("grazing",lambda x:x["regression"]["boundary_rows"][1].__setitem__("chord_length","1")); add("boundary_count",lambda x:x["regression"].__setitem__("boundary_row_count",1)); add("identity",lambda x:x["exact_identities"].pop()); add("theorem",lambda x:x["theorem"].__setitem__("clean_return","fake")); add("citation",lambda x:x["citations"][0].__setitem__("url","https://doi.org/10.0000/fake")); add("stale_hash",lambda x:x.__setitem__("payload_sha256","0"*64),False)
    env=dict(os.environ);env["PYTHONDONTWRITEBYTECODE"]="1";caught=[]
    with tempfile.TemporaryDirectory(prefix="c247-mut-") as td:
        for name,item in muts:
            p=Path(td)/(name+".json");p.write_text(json.dumps(item,sort_keys=True,indent=2,ensure_ascii=False)+"\n");r=subprocess.run([sys.executable,"-B",str(CHECKER),"--evidence",str(p)],env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
            if r.returncode!=0:caught.append(name)
    assert len(caught)==len(muts),"uncaught mutations: "+str(set(n for n,_ in muts)-set(caught));print(f"C247 hostile mutations: PASS {len(caught)}/{len(muts)}");print("caught="+",".join(caught))
if __name__=="__main__":main()
