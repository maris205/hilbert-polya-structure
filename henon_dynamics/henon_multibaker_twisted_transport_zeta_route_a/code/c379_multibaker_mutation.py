#!/usr/bin/env python3
"""Hostile source changes with repaired hashes, plus strict serialization attacks."""
if not __debug__:
    raise RuntimeError("c379 mutation refuses optimized Python")
import copy
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
def canonical(x): return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()

def main():
    original=json.loads((ROOT/"results/c379_multibaker_evidence.json").read_text())
    changes=[
        ("candidate",lambda x:x.update(candidate_id="HCS-C379x")),
        ("baseline",lambda x:x.update(source_commit="0"*40)),
        ("epoch type",lambda x:x.update(fixed_epoch=True)),
        ("forbidden claim",lambda x:x["scope_flags"].update(claims_target_zero_match=True)),
        ("route upgrade",lambda x:x["route_a"]["tuple"].__setitem__(1,"A1_PASS_ANALYTIC")),
        ("route B",lambda x:x["route_a"].update(route_b_invocation_allowed=True)),
        ("corner omission",lambda x:x["fixed_rows"][0]["geometric"].append([0,1])),
        ("symbolic count",lambda x:x["fixed_rows"][0]["symbolic"][0].__setitem__(1,2)),
        ("primitive count",lambda x:x["primitive_rows"][0].update(count=2)),
        ("primitive period",lambda x:x["primitive_rows"][0].update(q=1)),
        ("winding normalization",lambda x:x["necklace_rows"][-1].update(W=999)),
        ("reversal complement",lambda x:x["necklace_rows"][0].update(reversed_necklace="00")),
        ("multiplicity",lambda x:x["necklace_rows"][0].update(multiplicity=999)),
        ("x reconstruction",lambda x:x["geometry_rows"][0].update(x=[1,2])),
        ("cell displacement",lambda x:x["geometry_rows"][-1]["cells"].__setitem__(0,999)),
        ("stable reciprocal",lambda x:x["geometry_rows"][0].update(stable=[1,2])),
        ("flat weight",lambda x:x["geometry_rows"][0].update(flat_denominator=[4,1])),
        ("determinant sign",lambda x:x["determinant_rows"][0]["coefficients"][-1].__setitem__(2,1)),
        ("zeta corner factor",lambda x:x["geometric_zeta_rows"][0]["coefficients"].append([1,0,1,1])),
        ("even mixing",lambda x:x["diffusion"].update(even_ring_uniform_mixing=True)),
        ("diffusion constant",lambda x:x["diffusion"].update(D=[1,1])),
        ("nested numeric bool",lambda x:x["fixed_rows"][0].update(L=True)),
        ("unknown field",lambda x:x.update(unapproved=True)),
        ("row omission",lambda x:x["necklace_rows"].pop()),
    ]
    yaml_source=(ROOT/"evaluations/route_a/HCS-C379/2026-09-05.yaml").read_text()
    passed=0
    with tempfile.TemporaryDirectory(prefix="c379-mutation-") as d:
        work=Path(d); evidence=work/"evidence.json"; evaluation=work/"evaluation.yaml"
        def reject(label,raw,evaluation_raw=yaml_source):
            nonlocal passed
            evidence.write_text(raw); evaluation.write_text(evaluation_raw)
            p=subprocess.run([sys.executable,"-B",str(ROOT/"code/c379_multibaker_checker.py"),str(evidence),"--evaluation",str(evaluation)],capture_output=True,text=True)
            assert p.returncode!=0,"survived: "+label
            passed+=1
        for label,mutate in changes:
            x=copy.deepcopy(original); mutate(x); x.pop("payload_sha256")
            x["payload_sha256"]=hashlib.sha256(canonical(x)).hexdigest()
            reject(label,json.dumps(x))
        raw=json.dumps(original)
        reject("duplicate JSON",raw[:-1]+',"candidate_id":"HCS-C379"}')
        reject("nonfinite JSON",raw[:-1]+',"extra":NaN}')
        attacks=[yaml_source+"\ncandidate_id: HCS-C379\n",yaml_source+"\nunknown: 1\n",yaml_source.replace("fixed_epoch: 1788566400","fixed_epoch: true"),yaml_source.replace("evaluation_date: '2026-09-05'","evaluation_date: 2026-09-05"),yaml_source+"\na: &v 1\nb: *v\n",yaml_source+"\n1: value\n",yaml_source.replace("route_b_invocation_allowed: false","route_b_invocation_allowed: true"),yaml_source+"\n<<: {x: 1}\n"]
        for i,bad in enumerate(attacks):reject("YAML "+str(i),raw,bad)
    print(f"C379 hostile mutation PASS: repaired_hash={len(changes)} serialization=10 total={passed}/{passed}")

if __name__=="__main__":main()
