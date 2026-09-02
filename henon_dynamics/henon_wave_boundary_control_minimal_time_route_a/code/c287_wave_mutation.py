#!/usr/bin/env python3
from __future__ import annotations
import copy, hashlib, json, os, subprocess, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; EVIDENCE=ROOT/"results/c287_wave_evidence.json"; CHECKER=ROOT/"code/c287_wave_checker.py"
def phash(d):
    b=dict(d); b.pop("payload_sha256",None); return hashlib.sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def main():
    original=json.loads(EVIDENCE.read_text()); attacks=[]
    def add(label,fn):
        d=copy.deepcopy(original); fn(d); d["payload_sha256"]=phash(d); attacks.append((label,d))
    add("candidate",lambda d:d.__setitem__("candidate_id","HCS-C000"))
    add("source",lambda d:d.__setitem__("source_commit","0"*40))
    add("epoch",lambda d:d.__setitem__("fixed_epoch",0))
    add("scope",lambda d:d.__setitem__("scope_literal","OPEN"))
    add("tuple",lambda d:d["route_a"]["tuple"].__setitem__(1,"A1_PASS_ANALYTIC"))
    add("overall",lambda d:d["route_a"].__setitem__("overall","ROUTE_A_VALIDATED"))
    add("route_b",lambda d:d["route_a"].__setitem__("route_b_invocation_allowed",True))
    add("flag",lambda d:d["scope_flags"].__setitem__("euler_factors",True))
    add("boundary",lambda d:d["model"].__setitem__("adjoint_boundary","Neumann"))
    add("critical theorem",lambda d:d["theorem_contract"].__setitem__("observability","T>L/c"))
    add("time",lambda d:d["parameter_rows"][0].__setitem__("critical_time","1"))
    add("ratio",lambda d:d["modal_cells"][0].__setitem__("velocity_ratio","1"))
    add("mode zero",lambda d:d["enumeration"].__setitem__("mode_min",0))
    add("revival",lambda d:d["revival_cells"][0].__setitem__("critical_cos","-1"))
    add("complement",lambda d:d["subcritical_cells"][0].__setitem__("complement_fraction","0"))
    add("reference",lambda d:d["references"][0].__setitem__("identifier","ghost"))
    add("critical identity contract",lambda d:d["theorem_contract"].__setitem__("critical_identity","WRONG"))
    add("proof energy coordinate",lambda d:d["proof_contract"].__setitem__("energy_coordinate","WRONG"))
    add("parameter duplicate drop",lambda d:d["parameter_rows"].__setitem__(-1,copy.deepcopy(d["parameter_rows"][0])))
    add("modal duplicate drop",lambda d:d["modal_cells"].__setitem__(-1,copy.deepcopy(d["modal_cells"][0])))
    add("revival duplicate drop",lambda d:d["revival_cells"].__setitem__(-1,copy.deepcopy(d["revival_cells"][0])))
    add("subcritical duplicate drop",lambda d:d["subcritical_cells"].__setitem__(-1,copy.deepcopy(d["subcritical_cells"][0])))
    env=dict(os.environ); env["PYTHONDONTWRITEBYTECODE"]="1"; env["TZ"]="UTC"; passed=0
    with tempfile.TemporaryDirectory(prefix="c287_mut_") as tmp:
        for label,d in attacks:
            p=Path(tmp)/(label.replace(" ","_")+".json"); p.write_text(json.dumps(d,sort_keys=True,indent=2)+"\n")
            r=subprocess.run([sys.executable,"-B",str(CHECKER),str(p)],env=env,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
            assert r.returncode!=0,label; passed+=1
        stale=copy.deepcopy(original); stale["candidate_id"]="HCS-C000"; p=Path(tmp)/"stale.json"; p.write_text(json.dumps(stale,sort_keys=True,indent=2)+"\n")
        r=subprocess.run([sys.executable,"-B",str(CHECKER),str(p)],env=env,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL); assert r.returncode!=0; passed+=1
    print(f"C287 mutation suite: PASS {passed}/{len(attacks)+1}")
if __name__=="__main__": main()
