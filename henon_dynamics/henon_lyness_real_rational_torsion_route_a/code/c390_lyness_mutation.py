#!/usr/bin/env python3
"""Repaired-hash semantic attacks and actual strict YAML/type attacks."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("c390 mutation refuses optimized Python")
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
ROOT=Path(__file__).resolve().parents[1]
def can(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
def main():
    original=json.loads((ROOT/"results/c390_lyness_evidence.json").read_text());attacks=[]
    def add(label,path,value):attacks.append((label,path,value))
    add("unknown top key",["unknown"],1);add("wrong source",["source_commit"],"0"*40)
    add("epoch bool",["fixed_epoch"],True);add("scope type false to zero",["scope_flags","claims_root_number"],0)
    add("scope escalation",["scope_flags","claims_target_euler_factors"],True)
    add("route B escalation",["route_a","route_b_invocation_allowed"],True)
    add("A2 escalation",["route_a","tuple",2],"A2_PASS")
    add("contract extra",["contract","extra"],False)
    add("missing orbit",["orbit_rows"],original["orbit_rows"][:-1])
    add("nonpositive point",["orbit_rows",0,"states",1,1],[-1,1])
    add("unreduced rational",["orbit_rows",0,"a"],[2,8])
    add("rational bool",["orbit_rows",0,"a"],[True,4])
    add("wrong map state",["orbit_rows",0,"states",1,1],[1,1])
    add("wrong energy",["orbit_rows",0,"energy"],[17,1])
    add("Cartesian det one",["orbit_rows",1,"jacobian_determinant"],[1,1])
    add("false derivative",["orbit_rows",0,"twelve_step_jacobian",0,0],[0,1])
    add("nonprimitive cycle",["cycle_rows",0,"least_period"],10)
    add("return identity at nine",["cycle_rows",10,"return_matrix"],[[[1,1],[0,1]],[[0,1],[1,1]]])
    add("identity flag type",["cycle_rows",0,"identity_return"],1)
    add("missing rational cycle",["cycle_rows"],original["cycle_rows"][:-1])
    add("center wrong coefficient",["fixed_rows",0,"a"],[1,1])
    add("pi broad enclosure",["pi_bounds"],[[3,1],[4,1]])
    add("cosine broad enclosure",["angle_rows",0,"endpoint_cosine_bounds",0],[[0,1],[1,1]])
    add("false rational interval",["angle_rows",0,"rotation_interval"],[[1,10],[1,5]])
    add("denominator bool",["angle_rows",0,"period_witnesses",0,"denominator"],True)
    add("prime label drift",["angle_rows",0,"period_witnesses",2,"prime_integer"],True)
    add("prime type drift",["angle_rows",0,"period_witnesses",0,"prime_integer"],1)
    add("unreduced witness",["angle_rows",0,"period_witnesses",8,"numerators"],[2])
    add("missing denominator",["angle_rows",0,"period_witnesses"],original["angle_rows"][0]["period_witnesses"][:-1])
    add("summary bool",["summary","fixed_controls"],True)
    add("unknown nested key",["cycle_rows",0,"extraneous"],0)
    receipts=[]
    with tempfile.TemporaryDirectory(prefix="c390-hostile-") as d:
        temp=Path(d);p=temp/"bad.json";checker=ROOT/"code/c390_lyness_checker.py"
        for label,path,value in attacks:
            x=copy.deepcopy(original);ref=x
            for key in path[:-1]:ref=ref[key]
            ref[path[-1]]=value;x.pop("payload_sha256");x["payload_sha256"]=hashlib.sha256(can(x)).hexdigest();p.write_text(json.dumps(x))
            r=subprocess.run([sys.executable,"-B",str(checker),"--evidence",str(p)],capture_output=True,text=True)
            assert r.returncode!=0,"accepted repaired hash attack: "+label;receipts.append(label)
        raw=(ROOT/"results/c390_lyness_evidence.json").read_text()
        for label,mutated in (("duplicate JSON",raw.replace('"candidate_id": "HCS-C390"','"candidate_id": "HCS-C390", "candidate_id": "HCS-C390"',1)),("NaN JSON",raw.replace('"fixed_epoch": 1788566400','"fixed_epoch": NaN',1))):
            p.write_text(mutated);r=subprocess.run([sys.executable,"-B",str(checker),"--evidence",str(p)],capture_output=True,text=True);assert r.returncode;receipts.append(label)
        y=(ROOT/"evaluations/route_a/HCS-C390/2026-09-05.yaml").read_text();yp=temp/"bad.yaml"
        mutations=(("YAML unknown key",y+"alien_field: false\n"),("YAML false to zero",y.replace("claims_root_number: false","claims_root_number: 0")),("YAML date unquoted",y.replace("evaluation_date: '2026-09-05'","evaluation_date: 2026-09-05")),("YAML duplicate key",y+"candidate_id: HCS-C390\n"),("YAML scope escalation",y.replace("claims_automorphy: false","claims_automorphy: true")))
        for label,raw in mutations:
            yp.write_text(raw);r=subprocess.run([sys.executable,"-B",str(checker),"--evaluation",str(yp),"--evaluation-only"],capture_output=True,text=True);assert r.returncode,"accepted "+label;receipts.append(label)
    print(f"C390 hostile repaired-hash/type/YAML PASS: {len(receipts)}/{len(receipts)} rejected; semantic={len(attacks)}; JSON=2; YAML=5")
if __name__=="__main__":main()
