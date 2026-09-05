#!/usr/bin/env python3
"""Repaired-hash semantic mutations; standalone checker is the gate."""
if not __debug__:
    raise RuntimeError("c392 mutation refuses optimized Python")
import copy,hashlib,json,subprocess,sys,tempfile
from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[1]
EVAL=ROOT/"evaluations/route_a/HCS-C392/2026-09-05.yaml"
def canonical(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
def main():
    original=json.loads((ROOT/"results/c392_luroth_evidence.json").read_text())
    changes=[
      ("candidate",lambda x:x.update(candidate_id="WRONG")),
      ("baseline",lambda x:x.update(source_commit="0"*40)),
      ("epoch bool",lambda x:x.update(fixed_epoch=True)),
      ("claim true",lambda x:x["scope_flags"].update(claims_target_zero_match=True)),
      ("claim integer zero",lambda x:x["scope_flags"].update(claims_target_zero_match=0)),
      ("route B true",lambda x:x["route_a"].update(route_b_invocation_allowed=True)),
      ("route B integer zero",lambda x:x["route_a"].update(route_b_invocation_allowed=0)),
      ("route upgrade",lambda x:x["route_a"]["tuple"].__setitem__(1,"A1_PASS_ANALYTIC")),
      ("overall upgrade",lambda x:x["route_a"].update(overall_verdict="ROUTE_A_PROMISING")),
      ("unknown field",lambda x:x.update(extra=1)),
      ("missing metadata",lambda x:x.pop("evidence_role")),
      ("branch omit",lambda x:x["branches"].pop()),
      ("branch duplicate",lambda x:x["branches"].append(x["branches"][0])),
      ("branch numeric bool",lambda x:x["branches"][0].update(n=True)),
      ("branch numeric float",lambda x:x["branches"][0].update(n=1.0)),
      ("branch noncanonical fraction",lambda x:x["branches"][0].update(slope=[2,4])),
      ("branch offset",lambda x:x["branches"][0].update(offset=[0,1])),
      ("matrix omission",lambda x:x["matrices"].pop()),
      ("matrix scalar",lambda x:x["matrices"][0]["matrix"][0].__setitem__(0,[0,1])),
      ("matrix diagonal",lambda x:x["matrices"][0]["diagonal"].__setitem__(0,[0,1])),
      ("residue rank",lambda x:x["residues"][1].update(rank=0)),
      ("nilpotent classification",lambda x:x["residues"][1].update(kind="zero")),
      ("residue coefficient",lambda x:x["residues"][1]["matrix"][0].__setitem__(1,[0,1])),
      ("residue pole",lambda x:x["residues"][0].update(pole=[0,1])),
      ("scalar sign",lambda x:x["scalar_poles"][1].update(residue=[1,16])),
      ("determinant pole order",lambda x:x["scalar_poles"][1].update(determinant_pole_order=1)),
      ("word omission",lambda x:x["words"].pop()),
      ("word point",lambda x:x["words"][0].update(point=[0,1])),
      ("word least period",lambda x:x["words"][0].update(least_period=2)),
      ("word trace",lambda x:x["words"][0].update(trace_s1=[0,1])),
      ("endpoint inclusion",lambda x:x["controls"].update(isolated_zero="included")),
      ("s=1 fake tail",lambda x:x["controls"]["tail_after_N_at_s1"][0].update(tail=[0,1])),
    ]
    source=yaml.safe_load(EVAL.read_text());source_text=yaml.safe_dump(source,sort_keys=False,allow_unicode=True)
    passed=0
    with tempfile.TemporaryDirectory(prefix="c392-hostile-") as tmp:
        ep=Path(tmp)/"evidence.json";yp=Path(tmp)/"evaluation.yaml"
        def reject(label,raw,ytext=source_text):
            nonlocal passed
            ep.write_text(raw);yp.write_text(ytext)
            p=subprocess.run([sys.executable,"-B",str(ROOT/"code/c392_luroth_checker.py"),str(ep),"--evaluation",str(yp)],capture_output=True,text=True)
            assert p.returncode!=0,"survived "+label
            passed+=1
        for label,change in changes:
            x=copy.deepcopy(original);change(x);x.pop("payload_sha256")
            x["payload_sha256"]=hashlib.sha256(canonical(x)).hexdigest();reject(label,json.dumps(x))
        raw=json.dumps(original)
        reject("duplicate JSON",raw[:-1]+', "candidate_id":"HCS-C392"}')
        reject("NaN",raw[:-1]+', "extra":NaN}')
        reject("Infinity",raw[:-1]+', "extra":Infinity}')
        variants=[source_text+"\ncandidate_id: HCS-C392\n",source_text+"\nunknown: 1\n",
          source_text.replace("evaluation_date: '2026-09-05'","evaluation_date: 2026-09-05"),
          source_text+"\na: &v 1\nb: *v\n",source_text+"\n1: value\n",
          source_text.replace("route_b_invocation_allowed: false","route_b_invocation_allowed: 0"),
          source_text+"\n<<: {x: 1}\n",source_text+"\nnew: !!str abc\n",
          source_text.replace("claims_target_zero_match: false","claims_target_zero_match: true")]
        for i,v in enumerate(variants):
            assert v!=source_text
            reject("YAML "+str(i),raw,v)
    print(f"C392 hostile PASS: {len(changes)} repaired-hash + 3 JSON + 9 YAML = {passed}/{passed}")
if __name__=="__main__":main()
