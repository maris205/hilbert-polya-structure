#!/usr/bin/env python3
"""Hostile mutations must fail, even after attacker repairs payload hash."""
from __future__ import annotations
import copy,hashlib,json,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; src=json.loads((ROOT/"results/c267_wannier_evidence.json").read_text())
def phash(d):
 q=dict(d);q.pop("payload_sha256",None);return hashlib.sha256(json.dumps(q,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def muts():
 out=[]
 def add(name,fn):
  d=copy.deepcopy(src);fn(d);d["payload_sha256"]=phash(d);out.append((name,d))
 add("source",lambda d:d.update(source_commit="0"*40));add("epoch",lambda d:d.update(fixed_epoch=0));add("scope",lambda d:d.update(scope_literal="BROKEN"))
 add("eval",lambda d:d["evaluator"].update(sha256="0"*64));add("route",lambda d:d["route_a"].update(overall="PASS"))
 add("route_b",lambda d:d["route_a"].update(route_b_invocation_allowed=True));add("tuple",lambda d:d["route_a"]["tuple"].__setitem__(1,"A1_PASS"))
 add("flag",lambda d:d["scope_flags"].update(euler_factors=True));add("kernel",lambda d:d["regression"]["propagation_rows"][8]["kernel_entries"][1]["value"].update(re="9"))
 add("z",lambda d:d["regression"]["propagation_rows"][9].update(z="9"));add("moment",lambda d:d["regression"]["propagation_rows"][11].update(second_moment="9"))
 add("shell",lambda d:d["regression"]["propagation_rows"][12]["delta_shell"][7].update(probability="0.25"))
 add("eigen",lambda d:d["regression"]["eigen_rows"][5]["components"][4].update(value="3"));add("energy",lambda d:d["regression"]["eigen_rows"][6].update(energy=99))
 add("counts",lambda d:d["regression"]["counts"].update(kernel_cells=1));add("sp",lambda d:d["spectral_contract"].update(resolvent_Sp="all p"))
 add("compact",lambda d:d["spectral_contract"].update(U_compact=True));add("trace",lambda d:d["spectral_contract"].update(resolvent_trace_class=True))
 add("contract",lambda d:d["fourier_contract"].update(eigenvector="wrong"));add("period",lambda d:d["propagator_contract"].update(least_identity_return="pi/abs(F)"))
 return out
def main():
 passed=0; mm=muts()
 for name,d in mm:
  with tempfile.TemporaryDirectory() as td:
   p=Path(td)/"x.json";p.write_text(json.dumps(d,sort_keys=True,indent=2)+"\n")
   code=(ROOT/"code/c267_wannier_checker.py").read_text().replace('P=ROOT/"results/c267_wannier_evidence.json"',f'P=Path({str(p)!r})')
   q=Path(td)/"check.py";q.write_text(code)
   r=subprocess.run([sys.executable,"-B",str(q)],capture_output=True,text=True)
   if r.returncode!=0: passed+=1
   else: raise AssertionError(f"mutation survived: {name}")
 print(f"C267 hostile repaired-hash mutations: PASS {passed}/{len(mm)}")
if __name__=="__main__":main()
