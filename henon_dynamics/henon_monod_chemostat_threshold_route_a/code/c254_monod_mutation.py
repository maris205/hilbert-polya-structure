#!/usr/bin/env python3
"""Semantic mutations are rehashed, so rejection is not a checksum shortcut."""
import copy,json,os,subprocess,sys,tempfile
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; E=ROOT/"results/c254_monod_evidence.json"; C=ROOT/"code/c254_monod_checker.py"
def ph(d):
 b=dict(d); b.pop("payload_sha256",None); return sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def add(muts,base,fn):
 x=copy.deepcopy(base); fn(x); x["payload_sha256"]=ph(x); muts.append(x)
def main():
 b=json.loads(E.read_text()); m=[]
 for k in ("schema","candidate_id","evaluation_date","source_commit","fixed_epoch","scope_literal"):
  add(m,b,lambda x,k=k:x.__setitem__(k,str(x[k])+"_mut"))
 add(m,b,lambda x:x["evaluator"].__setitem__("sha256","0"*64)); add(m,b,lambda x:x["route_a"].__setitem__("tuple",["A0_FAIL"])); add(m,b,lambda x:x["route_a"].__setitem__("overall","ROUTE_A_EXPLORATORY")); add(m,b,lambda x:x["route_a"].__setitem__("route_b_invocation_allowed",True))
 for k in b["scope_flags"]: add(m,b,lambda x,k=k:x["scope_flags"].__setitem__(k,True))
 add(m,b,lambda x:x["regression"]["rows"][0].__setitem__("threshold_numerator","0")); add(m,b,lambda x:x["regression"]["rows"][1].__setitem__("regime","washout")); add(m,b,lambda x:x["regression"]["rows"][6].__setitem__("critical_leaf_asymptotic_coefficient","1")); add(m,b,lambda x:x["regression"]["rows"][12].__setitem__("washout_eigenvalues",["0","0"])); add(m,b,lambda x:x["regression"].__setitem__("regime_counts",{"survival":18})); add(m,b,lambda x:x["regression"].__setitem__("boundary_rows",[])); add(m,b,lambda x:x.__setitem__("exact_identities",[])); add(m,b,lambda x:x.__setitem__("citations",[])); add(m,b,lambda x:x.__setitem__("nonclaims",[]))
 rejected=0
 with tempfile.TemporaryDirectory() as td:
  for i,x in enumerate(m):
   p=Path(td)/f"m{i}.json"; p.write_text(json.dumps(x,sort_keys=True,indent=2,ensure_ascii=False)+"\n"); env=dict(os.environ); env["PYTHONDONTWRITEBYTECODE"]="1"; r=subprocess.run([sys.executable,"-B",str(C),"--evidence",str(p)],env=env,text=True,capture_output=True); rejected+=r.returncode!=0
 assert rejected==len(m); print(f"C254 hostile mutation: PASS {rejected}/{len(m)} (semantic mutations rehashed before checking)")
if __name__=="__main__": main()
