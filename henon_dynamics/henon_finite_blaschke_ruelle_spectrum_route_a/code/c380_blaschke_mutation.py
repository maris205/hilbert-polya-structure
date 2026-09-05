#!/usr/bin/env python3
"""Semantic hostile mutations with repaired outer hash."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("c380 mutation refuses optimized Python")
import argparse
import copy
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def seal(x):
    x.pop("payload_sha256",None)
    x["payload_sha256"]=hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
    return json.dumps(x,sort_keys=True,indent=2,ensure_ascii=False).encode()+b"\n"
def main():
    argparse.ArgumentParser().parse_args()
    original=(ROOT/"results/c380_blaschke_evidence.json").read_bytes();base=json.loads(original)
    cases=[]
    def add(name,path,value):
        x=copy.deepcopy(base);d=x
        for key in path[:-1]:d=d[key]
        d[path[-1]]=value;cases.append((name,seal(x)))
    add("branch-globalization",["convention","branches"],"two global inverse branches")
    add("multiplier-sign",["parameter_rows",1,"q"],[1,7])
    add("trace-sign",["parameter_rows",1,"trace_n_1_to_16",0],[4,3])
    add("spectrum-multiplicity",["convention","spectrum"],"one channel")
    add("census-missing-boundary",["census",0,"fixed"],2)
    add("primitive-double-count",["census",5,"primitive_cycles"],100)
    add("linear-parent-rank",["boundary","a_zero"],"rank one")
    add("wall-continuation",["boundary","a_one"],"trace class at the wall")
    add("matrix-coefficient",["parameter_rows",2,"positive_section_0_to_10",1,2],[1,1])
    add("q-difference-coefficient",["parameter_rows",3,"det_coefficients_0_to_16",7],[0,1])
    add("truncation-tail",["parameter_rows",4,"tail_bounds",0,"log_tail_bound"],[0,1])
    add("root-multiplicity",["parameter_rows",4,"zero_census",4,"zero_count_with_boundary"],1)
    add("annulus-direction",["parameter_rows",3,"t"],[9,10])
    add("expansion-bound",["parameter_rows",4,"expansion_min"],[1,1])
    add("angular-value",["parameter_rows",3,"angular_rows",2,"angular_derivative"],[3,1])
    add("finite-section",["parameter_rows",2,"spectral_sections",1,"polynomial",2],[0,1])
    add("trace-tail",["parameter_rows",2,"spectral_sections",2,"trace_power4_tail"],[0,1])
    add("source",["source_commit"],"wrong")
    add("epoch",["fixed_epoch"],0)
    add("schema",["schema"],"wrong")
    add("candidate",["candidate_id"],"HCS-C381")
    add("scope",["scope_flags","claims_target_zero_match"],True)
    add("scope-int",["scope_flags","claims_target_zero_match"],0)
    add("route-b",["route_a","route_b_invocation_allowed"],True)
    add("route-b-int",["route_a","route_b_invocation_allowed"],0)
    add("bool-int",["census",0,"n"],True)
    add("float-int",["census",0,"n"],1.0)
    add("extra-key",["unexpected"],1)
    add("unreduced-fraction",["parameter_rows",0,"a"],[0,2])
    add("extra-row",["census"],base["census"]+[base["census"][0]])
    cases.append(("duplicate-json",b'{"candidate_id":"evil",'+original.lstrip()[1:]))
    cases.append(("nonfinite-json",original.replace(b'"fixed_epoch": 1788566400',b'"fixed_epoch": NaN')))
    with tempfile.TemporaryDirectory(prefix="c380-hostile-") as directory:
        path=Path(directory)/"evidence.json"
        for name,blob in [("positive",original)]+cases:
            path.write_bytes(blob)
            p=subprocess.run([sys.executable,"-B",str(ROOT/"code/c380_blaschke_checker.py"),"--input",str(path)],capture_output=True)
            assert (p.returncode==0)==(name=="positive"),name
    print(f"C380 repaired-hash mutations PASS: rejected={len(cases)}/{len(cases)}")
if __name__=="__main__":main()
