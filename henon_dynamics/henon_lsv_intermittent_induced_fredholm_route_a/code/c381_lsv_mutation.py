#!/usr/bin/env python3
"""Repaired-hash mathematical attacks and strict JSON/YAML mutations."""
if not __debug__:
    raise RuntimeError("c381 mutation refuses optimized Python")
import copy
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def canonical(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
def main():
    original=json.loads((ROOT/"results/c381_lsv_evidence.json").read_text())
    def widen_tail(x):
        row=x["tail_rows"][-1]
        row["a_bounds"][0]-=2048;row["a_bounds"][1]+=2048
        row["tail_bounds"]=[row["a_bounds"][0]//2,(row["a_bounds"][1]+1)//2]
    attacks=[
      ("candidate",lambda x:x.update(candidate_id="HCS-C381x")),
      ("baseline",lambda x:x.update(source_commit="0"*40)),
      ("scope",lambda x:x["scope_flags"].update(claims_target_zero_match=True)),
      ("boolean zero",lambda x:x["scope_flags"].update(invokes_route_b=0)),
      ("route B",lambda x:x["route_a"].update(route_b_invocation_allowed=True)),
      ("endpoint partition",lambda x:x.update(partition="left [0,1/2); right [1/2,1]")),
      ("clock swap",lambda x:x.update(clock="u counts original iterations; zeta counts returns")),
      ("missing periodic row",lambda x:x["periodic_rows"].pop()),
      ("neutral label",lambda x:x["periodic_rows"][0].update(neutral=False)),
      ("neutral multiplier",lambda x:x["periodic_rows"][0].update(multiplier_bounds=[2**81,2**81])),
      ("least period",lambda x:x["periodic_rows"][-1].update(least_period=6)),
      ("orientation",lambda x:x["periodic_rows"][0].update(orientation=-1)),
      ("root bracket",lambda x:x["periodic_rows"][3].update(point_bounds=[0,0])),
      ("primitive census",lambda x:x["primitive_rows"][0].update(primitive_cycles=1)),
      ("return inverse",lambda x:x["return_rows"][1].update(preimage_bounds=[0,0])),
      ("return derivative",lambda x:x["return_rows"][1].update(preimage_derivative_bounds=[0,0])),
      ("return branch endpoint",lambda x:x["return_rows"][1].update(h_bounds=[0,0])),
      ("return clock",lambda x:x["return_rows"][1].update(n=3)),
      ("tail normalization",lambda x:x["tail_asymptotic"].update(lebesgue_constant=[1,2])),
      ("mean return",lambda x:x["tail_asymptotic"].update(mean_return_finite=True)),
      ("tail interval",lambda x:x["tail_rows"][1].update(tail_bounds=[0,0])),
      ("tail widening",widen_tail),
      ("induced word",lambda x:x["induced_rows"][1].update(word="01")),
      ("induced original time",lambda x:x["induced_rows"][1].update(original_time=1)),
      ("trace denominator",lambda x:x["induced_rows"][1].update(trace_weight_bounds=[0,0])),
      ("infinite trace head",lambda x:x["trace_head_rows"][0].update(infinite_trace_claim=True)),
      ("image radius",lambda x:x["complex_bounds"].update(image_radius=[3,4])),
      ("derivative exponent",lambda x:x["complex_bounds"].update(derivative_bound_exp_pi2_coefficient=[1,6])),
      ("outside series",lambda x:x["complex_bounds"].update(outside_terms_tend_to_zero=True)),
      ("uninduced compact",lambda x:x["uninduced"].update(compact=True)),
      ("uninduced gap",lambda x:x["uninduced"].update(zero_integral_uniform_exponential_decay=True)),
      ("integer bool",lambda x:x["periodic_rows"][0].update(n=True)),
      ("unknown",lambda x:x.update(unapproved="extra")),
    ]
    yaml_raw=(ROOT/"evaluations/route_a/HCS-C381/2026-09-05.yaml").read_text();passed=0
    with tempfile.TemporaryDirectory(prefix="c381-hostile-") as d:
        work=Path(d);evidence=work/"evidence.json";evaluation=work/"evaluation.yaml"
        def reject(label,raw,ev=yaml_raw):
            nonlocal passed
            evidence.write_text(raw);evaluation.write_text(ev)
            p=subprocess.run([sys.executable,"-B",str(ROOT/"code/c381_lsv_checker.py"),str(evidence),"--evaluation",str(evaluation)],capture_output=True,text=True)
            assert p.returncode!=0,"survived mutation "+label
            passed+=1
        for label,mutate in attacks:
            value=copy.deepcopy(original);mutate(value);value.pop("payload_sha256")
            value["payload_sha256"]=hashlib.sha256(canonical(value)).hexdigest()
            reject(label,json.dumps(value))
        raw=json.dumps(original)
        reject("duplicate JSON",raw[:-1]+',"candidate_id":"HCS-C381"}')
        reject("nonfinite JSON",raw[:-1]+',"unexpected":Infinity}')
        bad_yaml=[yaml_raw+"\ncandidate_id: HCS-C381\n",yaml_raw+"\nunknown: 1\n",yaml_raw.replace("route_b_invocation_allowed: false","route_b_invocation_allowed: 0"),yaml_raw.replace("fixed_epoch: 1788566400","fixed_epoch: true"),yaml_raw.replace("evaluation_date: '2026-09-05'","evaluation_date: 2026-09-05"),yaml_raw+"\nx: &q 1\ny: *q\n",yaml_raw+"\n1: value\n",yaml_raw+"\n<<: {x: 1}\n"]
        for i,ev in enumerate(bad_yaml):reject("YAML "+str(i),raw,ev)
    print(f"C381 hostile mutation PASS: repaired_hash={len(attacks)} serialization=10 total={passed}/{passed}")
if __name__=="__main__":main()
