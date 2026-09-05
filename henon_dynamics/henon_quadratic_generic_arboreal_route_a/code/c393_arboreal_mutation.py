#!/usr/bin/env python3
"""Repaired-hash semantic mutations; standalone checker is the gate."""
if not __debug__:
    raise RuntimeError("c393 mutation refuses optimized Python")
import copy,hashlib,json,subprocess,sys,tempfile
from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[1]
EVAL=ROOT/"evaluations/route_a/HCS-C393/2026-09-05.yaml"
def canonical(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
def main():
    original=json.loads((ROOT/"results/c393_arboreal_evidence.json").read_text())
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
      ("critical collision",lambda x:x["critical_values"].__setitem__(2,1)),
      ("tower omission",lambda x:x["tower"].pop()),
      ("tower numeric bool",lambda x:x["tower"][0].update(n=True)),
      ("tower numeric float",lambda x:x["tower"][0].update(n=1.0)),
      ("wrong group order",lambda x:x["tower"][2].update(order=64)),
      ("wrong genus",lambda x:x["tower"][2].update(genus=0)),
      ("wrong kernel",lambda x:x["tower"][1].update(kernel=2)),
      ("new branch",lambda x:x["tower"][2].update(new_branch_quadratic=0)),
      ("inertia",lambda x:x["tower"][2]["finite_inertia"][0].update(two_cycles=1)),
      ("cycle class omit",lambda x:x["cycle_indices"][4]["cycle_types"].pop()),
      ("cycle count",lambda x:x["cycle_indices"][0]["cycle_types"][0].update(count=2)),
      ("cycle length",lambda x:x["cycle_indices"][1]["cycle_types"][0]["lengths"].__setitem__(0,2)),
      ("probability noncanonical",lambda x:x["root_probabilities"][0].update(probability=[2,2])),
      ("probability wrong",lambda x:x["root_probabilities"][1].update(probability=[1,1])),
      ("fixed mean",lambda x:x["root_probabilities"][1].update(mean_fixed=0)),
      ("prime omission",lambda x:x["finite_fields"].pop()),
      ("composite owner",lambda x:x["finite_fields"][0].update(p=4)),
      ("bad characteristic",lambda x:x["finite_fields"][0]["levels"][0].update(good_reduction="yes")),
      ("false periodic point",lambda x:x["finite_fields"][1]["periodic_points"].append(2)),
      ("wrong image",lambda x:x["finite_fields"][1]["levels"][0].update(image_size=0)),
      ("uniform good tower",lambda x:x["clock_boundary"].__setitem__(1,"all heights before prime limit")),
    ]
    source=yaml.safe_load(EVAL.read_text());source_text=yaml.safe_dump(source,sort_keys=False,allow_unicode=True)
    passed=0
    with tempfile.TemporaryDirectory(prefix="c393-hostile-") as tmp:
        ep=Path(tmp)/"evidence.json";yp=Path(tmp)/"evaluation.yaml"
        def reject(label,raw,ytext=source_text):
            nonlocal passed
            ep.write_text(raw);yp.write_text(ytext)
            p=subprocess.run([sys.executable,"-B",str(ROOT/"code/c393_arboreal_checker.py"),str(ep),"--evaluation",str(yp)],capture_output=True,text=True)
            assert p.returncode!=0,"survived "+label
            passed+=1
        for label,change in changes:
            x=copy.deepcopy(original);change(x);x.pop("payload_sha256")
            x["payload_sha256"]=hashlib.sha256(canonical(x)).hexdigest();reject(label,json.dumps(x))
        raw=json.dumps(original)
        reject("duplicate JSON",raw[:-1]+', "candidate_id":"HCS-C393"}')
        reject("NaN",raw[:-1]+', "extra":NaN}')
        reject("Infinity",raw[:-1]+', "extra":Infinity}')
        variants=[source_text+"\ncandidate_id: HCS-C393\n",source_text+"\nunknown: 1\n",
          source_text.replace("evaluation_date: '2026-09-05'","evaluation_date: 2026-09-05"),
          source_text+"\na: &v 1\nb: *v\n",source_text+"\n1: value\n",
          source_text.replace("route_b_invocation_allowed: false","route_b_invocation_allowed: 0"),
          source_text+"\n<<: {x: 1}\n",source_text+"\nnew: !!str abc\n",
          source_text.replace("claims_target_zero_match: false","claims_target_zero_match: true")]
        for i,v in enumerate(variants):
            assert v!=source_text
            reject("YAML "+str(i),raw,v)
    print(f"C393 hostile PASS: {len(changes)} repaired-hash + 3 JSON + 9 YAML = {passed}/{passed}")
if __name__=="__main__":main()
