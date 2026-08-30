#!/usr/bin/env python3
"""Hostile repaired-hash and semantic mutation suite for C244."""
from __future__ import annotations
import sys
sys.dont_write_bytecode=True
from copy import deepcopy
from hashlib import sha256
import json, os, subprocess, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
EVIDENCE=ROOT/"results/c244_pendulum_evidence.json"
CHECKER=ROOT/"code/c244_pendulum_checker.py"
def repair(d):
    b=dict(d); b.pop("payload_sha256",None); d["payload_sha256"]=sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest(); return d
def main():
    pristine=json.loads(EVIDENCE.read_text()); muts=[]
    def add(name,fn,repaired=True):
        x=deepcopy(pristine); fn(x)
        if repaired: repair(x)
        muts.append((name,x))
    add("source",lambda x:x.__setitem__("source_commit","0"*40))
    add("epoch",lambda x:x.__setitem__("fixed_epoch",0))
    add("scope",lambda x:x.__setitem__("scope_literal","BAD"))
    add("evaluator",lambda x:x["evaluator"].__setitem__("sha256","0"*64))
    add("schema",lambda x:x.__setitem__("schema","wrong"))
    add("route_a1",lambda x:x["route_a"]["tuple"].__setitem__(1,"A1_FAIL"))
    add("route_overall",lambda x:x["route_a"].__setitem__("overall","ROUTE_A_ACCEPTED"))
    add("route_b",lambda x:x["route_a"].__setitem__("route_b_invocation_allowed",True))
    add("firewall",lambda x:x["scope_flags"].__setitem__("claims_euler_factors",True))
    add("unknown_top",lambda x:x.__setitem__("unknown_top",True))
    add("critical_s",lambda x:x["regression"]["critical_rows"][2].__setitem__("s","-1/4"))
    add("critical_h",lambda x:x["regression"]["critical_rows"][3].__setitem__("h","9"))
    add("critical_j2",lambda x:x["regression"]["critical_rows"][4].__setitem__("j_squared","0"))
    add("critical_type",lambda x:x["regression"]["critical_rows"][5].__setitem__("type","regular"))
    add("critical_note",lambda x:x["regression"]["critical_rows"][6].__setitem__("boundary_note","fake"))
    add("critical_count",lambda x:x["regression"].__setitem__("critical_row_count",6))
    add("fixed_point",lambda x:x["regression"]["fixed_rows"][1].__setitem__("singularity_type","elliptic"))
    add("fixed_chart",lambda x:x["regression"]["fixed_rows"][0].__setitem__("chart","local"))
    add("regular_h",lambda x:x["regression"]["regular_rows"][0].__setitem__("h","0"))
    add("regular_j",lambda x:x["regression"]["regular_rows"][1].__setitem__("j","1/2"))
    add("regular_j2",lambda x:x["regression"]["regular_rows"][2].__setitem__("j_squared","1"))
    add("regular_root",lambda x:x["regression"]["regular_rows"][3]["roots"].__setitem__(0,"0"))
    add("regular_order",lambda x:x["regression"]["regular_rows"][4].__setitem__("root_order","wrong"))
    add("regular_period",lambda x:x["regression"]["regular_rows"][5].__setitem__("period_T","0"))
    add("regular_delta",lambda x:x["regression"]["regular_rows"][6].__setitem__("angle_increment_Delta_phi","0"))
    add("regular_action",lambda x:x["regression"]["regular_rows"][7].__setitem__("action_I","0"))
    add("regular_count",lambda x:x["regression"].__setitem__("regular_row_count",7))
    add("monodromy_matrix",lambda x:x["regression"]["monodromy"].__setitem__("matrix",[[1,0],[0,1]]))
    add("monodromy_basis",lambda x:x["regression"]["monodromy"].__setitem__("basis","wrong"))
    add("monodromy_convention",lambda x:x["regression"]["monodromy"].__setitem__("matrix_convention","rows"))
    add("identity",lambda x:x["exact_identities"].pop())
    add("citation",lambda x:x["citations"][0].__setitem__("url","https://doi.org/10.0000/fake"))
    add("theorem",lambda x:x["theorem"].__setitem__("monodromy","M=[[0,0],[0,0]]"))
    add("payload_stale",lambda x:x.__setitem__("payload_sha256","0"*64),False)
    env=dict(os.environ); env["PYTHONDONTWRITEBYTECODE"]="1"; caught=[]
    with tempfile.TemporaryDirectory(prefix="c244-mut-") as td:
        for name,item in muts:
            p=Path(td)/(name+".json"); p.write_text(json.dumps(item,sort_keys=True,indent=2,ensure_ascii=False)+"\n")
            r=subprocess.run([sys.executable,"-B",str(CHECKER),"--evidence",str(p)],env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
            if r.returncode!=0: caught.append(name)
    assert len(caught)==len(muts),"uncaught mutations: "+str(set(n for n,_ in muts)-set(caught))
    print(f"C244 hostile mutations: PASS {len(caught)}/{len(muts)}")
    print("caught="+",".join(caught))
if __name__=="__main__": main()
