#!/usr/bin/env python3
"""Repaired-hash hostile mutation suite."""
import copy,hashlib,json,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];src=json.loads((ROOT/"results/c268_lorentz_evidence.json").read_text())
def phash(d):
 q=dict(d);q.pop("payload_sha256",None);return hashlib.sha256(json.dumps(q,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def main():
 mm=[]
 def add(name,fn):
  d=copy.deepcopy(src);fn(d);d["payload_sha256"]=phash(d);mm.append((name,d))
 add("source",lambda d:d.update(source_commit="0"*40));add("epoch",lambda d:d.update(fixed_epoch=0));add("scope",lambda d:d.update(scope_literal="BAD"));add("evaluator",lambda d:d["evaluator"].update(sha256="0"*64))
 add("route",lambda d:d["route_a"].update(overall="PASS"));add("route_b",lambda d:d["route_a"].update(route_b_invocation_allowed=True));add("tuple",lambda d:d["route_a"]["tuple"].__setitem__(1,"A1_PASS"));add("scope_flag",lambda d:d["scope_flags"].update(root_numbers=True))
 add("E_sign",lambda d:d["regression"]["cases"][1]["A"][0].__setitem__(1,"-2/1"));add("char_sign",lambda d:d["regression"]["cases"][4].update(char_c0="1/1"));add("a2",lambda d:d["regression"]["cases"][5].update(a2="9"));add("b2",lambda d:d["regression"]["cases"][6].update(b2="9"))
 add("projector_swap",lambda d:d["generic_contract"].update(Ph=d["generic_contract"]["Pr"]));add("exp_sign",lambda d:d["generic_contract"].update(exp="wrong"));add("expm_cell",lambda d:d["regression"]["cases"][7]["samples"][2]["exp"][1].__setitem__(2,"99"));add("integral_cell",lambda d:d["regression"]["cases"][8]["samples"][3]["integral"][0].__setitem__(0,"99"))
 add("null_truncation",lambda d:d["null_contract"].update(exp="I+tau A"));add("null_integral",lambda d:d["null_contract"].update(integral="wrong"));add("proper_coordinate",lambda d:d["dynamics_contract"].update(parameter="coordinate time"));add("closed_worldline",lambda d:d["dynamics_contract"].update(physical_worldline_closed=True))
 add("period",lambda d:d["dynamics_contract"].update(velocity_period="pi/b"));add("three_force",lambda d:d["convention"].update(three_force="E-v cross B"));add("invariant",lambda d:d["invariant_contract"].update(characteristic="(z^2+a^2)(z^2+b^2)"));add("counts",lambda d:d["regression"]["counts"].update(matrix_cells=1))
 passed=0
 for name,d in mm:
  with tempfile.TemporaryDirectory() as td:
   p=Path(td)/"x.json";p.write_text(json.dumps(d,sort_keys=True,indent=2)+"\n")
   code=(ROOT/"code/c268_lorentz_checker.py").read_text().replace('P=ROOT/"results/c268_lorentz_evidence.json"',f'P=Path({str(p)!r})');q=Path(td)/"c.py";q.write_text(code)
   r=subprocess.run([sys.executable,"-B",str(q)],capture_output=True,text=True)
   if r.returncode:passed+=1
   else:raise AssertionError(f"mutation survived: {name}")
 print(f"C268 hostile repaired-hash mutations: PASS {passed}/{len(mm)}")
if __name__=="__main__":main()
