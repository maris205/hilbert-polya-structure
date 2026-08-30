#!/usr/bin/env python3
"""Hostile mutation suite: every altered receipt must fail the hash preflight."""
import copy, json, os, subprocess, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
E=ROOT/"results/c250_ep_evidence.json"
CHECK=ROOT/"code/c250_ep_checker.py"
def main():
    base=json.loads(E.read_text()); mutations=[]
    for key in ("schema","candidate_id","source_commit","fixed_epoch","scope_literal","headline"):
        x=copy.deepcopy(base); x[key] = (x[key]+"_tampered") if isinstance(x[key],str) else x[key]+1; mutations.append(x)
    for key in ("tuple","overall","route_b_invocation_allowed"):
        x=copy.deepcopy(base)
        x["route_a"][key] = (list(x["route_a"][key])+["X"]) if key=="tuple" else (not x["route_a"][key]) if key=="route_b_invocation_allowed" else "PASS"
        mutations.append(x)
    for key in list(base["scope_flags"]):
        x=copy.deepcopy(base); x["scope_flags"][key]=True; mutations.append(x)
    for i in range(8):
        x=copy.deepcopy(base); x["regression"]["rows"][i%len(x["regression"]["rows"])]["x_t"]="0.0"; mutations.append(x)
    rejected=0
    with tempfile.TemporaryDirectory() as td:
        for i,x in enumerate(mutations):
            p=Path(td)/f"m{i}.json"; p.write_text(json.dumps(x,sort_keys=True,indent=2,ensure_ascii=False)+"\n"); env=dict(os.environ); env["PYTHONDONTWRITEBYTECODE"]="1"
            r=subprocess.run([sys.executable,"-B",str(CHECK),"--evidence",str(p),"--quick"],env=env,text=True,capture_output=True)
            if r.returncode!=0: rejected+=1
    print(f"C250 hostile mutation: PASS {rejected}/{len(mutations)}")
    assert rejected==len(mutations)
if __name__=="__main__": main()
