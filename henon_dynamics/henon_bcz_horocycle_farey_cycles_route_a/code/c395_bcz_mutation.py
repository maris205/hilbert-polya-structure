#!/usr/bin/env python3
"""Repaired-hash attacks plus actual release-write YAML refusal."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("c395 mutation refuses optimized Python")
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
ROOT=Path(__file__).resolve().parents[1]
def can(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
def reject(cmd):
    p=subprocess.run(cmd,capture_output=True,text=True)
    assert p.returncode!=0,"accepted hostile input: "+str(cmd)
    return p.stdout+p.stderr
def main():
    x=json.loads((ROOT/"results/c395_bcz_evidence.json").read_text())
    attacks=[
      ("unknown top",["alien"],False),("epoch bool",["fixed_epoch"],True),("source",["source_commit"],"0"*40),
      ("scope zero",["scope_flags","claims_root_number"],0),("scope promotion",["scope_flags","claims_target_euler_factors"],True),
      ("route B",["route_a","route_b_invocation_allowed"],True),("A2 promotion",["route_a","tuple",2],"A2_PASS"),
      ("contract key",["contract","unknown"],1),("missing layer",["layer_rows"],x["layer_rows"][:-1]),
      ("N bool",["layer_rows",0,"N"],True),("least period",["layer_rows",2,"least_period"],5),
      ("lower closed",["layer_rows",2,"lower_included"],True),("upper open",["layer_rows",2,"upper_included"],False),
      ("flag integer",["layer_rows",2,"upper_included"],1),("unreduced scale",["layer_rows",2,"interior_scale"],[4,14]),
      ("scale bool",["layer_rows",2,"interior_scale"],[True,7]),("missing point",["layer_rows",2,"cycle"],x["layer_rows"][2]["cycle"][:-1]),
      ("noncoprime point",["layer_rows",2,"cycle",0],[2,2]),("floor off by one",["layer_rows",2,"branch_indices",0],2),
      ("identity monodromy",["layer_rows",2,"product_at_start"],[[1,0],[0,1]]),
      ("matrix entry bool",["layer_rows",0,"return_matrices",0,0,0],False),
      ("wrong cyclic matrix",["layer_rows",2,"return_matrices",1,0,1],1),
      ("roof clock mixed",["layer_rows",2,"interior_total_roof"],[4,1]),("gap count",["layer_rows",2,"gap_sum"],[2,1]),
      ("wrong repetition",["layer_rows",2,"repetitions",3,"matrix",0,0],0),
      ("negative physical roof",["layer_rows",2,"repetitions",0,"roof_multiplier"],-1),
      ("missing wall",["wall_rows"],x["wall_rows"][:-1]),("smooth wall",["wall_rows",0,"two_sided_derivative_exists"],True),
      ("wall near branch",["wall_rows",0,"near_branch"],4),("wall exact branch",["wall_rows",0,"exact_branch"],3),
      ("wall limit",["wall_rows",0,"one_sided_limit",1],[1,1]),("finite cardinality",["fixed_rows",0,"cardinality"],1),
      ("missing fixed layer",["fixed_rows",0,"layers"],[]),("wrong segments",["fixed_rows",1,"radial_segments"],2),
      ("summary type",["summary","layers"],64.0),("unknown nested",["layer_rows",0,"unknown"],False)]
    count=0
    with tempfile.TemporaryDirectory(prefix="c395-hostile-") as d:
        bad=Path(d)/"bad.json";check=ROOT/"code/c395_bcz_checker.py"
        for label,path,value in attacks:
            y=copy.deepcopy(x);node=y
            for key in path[:-1]:node=node[key]
            node[path[-1]]=value;y.pop("payload_sha256");y["payload_sha256"]=hashlib.sha256(can(y)).hexdigest();bad.write_text(json.dumps(y))
            reject([sys.executable,"-B",str(check),"--evidence",str(bad)]);count+=1
        raw=(ROOT/"results/c395_bcz_evidence.json").read_text()
        for badraw in (raw.replace('"candidate_id": "HCS-C395"','"candidate_id": "HCS-C395", "candidate_id": "HCS-C395"',1),raw.replace('"fixed_epoch": 1788566400','"fixed_epoch": NaN',1)):
            bad.write_text(badraw);reject([sys.executable,"-B",str(check),"--evidence",str(bad)]);count+=1
        raw=(ROOT/"evaluations/route_a/HCS-C395/2026-09-05.yaml").read_text();yp=Path(d)/"bad.yaml"
        variants=(raw+"unknown: false\n",raw.replace("claims_root_number: false","claims_root_number: 0"),raw.replace("evaluation_date: '2026-09-05'","evaluation_date: 2026-09-05"),raw+"candidate_id: HCS-C395\n",raw.replace("claims_automorphy: false","claims_automorphy: true"),raw.replace("fixed_epoch: 1788566400","fixed_epoch: 1788566400.0"))
        manifest=ROOT/"C395_RELEASE_MANIFEST.json";before=manifest.read_bytes() if manifest.exists() else None
        for badraw in variants:
            yp.write_text(badraw)
            reject([sys.executable,"-B",str(check),"--evaluation",str(yp),"--evaluation-only"])
            receipt=reject([sys.executable,"-B",str(ROOT/"code/c395_release_manifest.py"),"--write","--evaluation",str(yp)])
            assert "preflight evaluation rejected" in receipt,"write did not fail at strict preflight"
            assert (manifest.read_bytes() if manifest.exists() else None)==before,"hostile write changed manifest"
            count+=2
    print(f"C395 hostile PASS: {count}/{count} rejected; semantic={len(attacks)} JSON=2 YAML-checker=6 actual-write=6; release untouched")
if __name__=="__main__":main()
