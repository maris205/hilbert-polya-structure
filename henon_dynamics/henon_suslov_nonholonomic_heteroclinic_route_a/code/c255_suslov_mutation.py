#!/usr/bin/env python3
"""Rehashed semantic corruption suite for HCS-C255."""
import copy,json,os,subprocess,sys,tempfile
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; E=ROOT/"results/c255_suslov_evidence.json"; C=ROOT/"code/c255_suslov_checker.py"
def ph(d):
 b=dict(d); b.pop("payload_sha256",None); return sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def add(m,b,fn):
 x=copy.deepcopy(b); fn(x); x["payload_sha256"]=ph(x); m.append(x)
def main():
 b=json.loads(E.read_text()); m=[]
 for k in ("schema","candidate_id","evaluation_date","source_commit","fixed_epoch","scope_literal"): add(m,b,lambda x,k=k:x.__setitem__(k,str(x[k])+"_mut"))
 add(m,b,lambda x:x["evaluator"].__setitem__("sha256","0"*64)); add(m,b,lambda x:x["route_a"].__setitem__("tuple",["A1_PASS_ANALYTIC"])); add(m,b,lambda x:x["route_a"].__setitem__("overall","ROUTE_A_EXPLORATORY")); add(m,b,lambda x:x["route_a"].__setitem__("route_b_invocation_allowed",True))
 for k in b["scope_flags"]: add(m,b,lambda x,k=k:x["scope_flags"].__setitem__(k,True))
 add(m,b,lambda x:x["regression"]["rows"][0].__setitem__("schur_complement","0")); add(m,b,lambda x:x["regression"]["rows"][1].__setitem__("kappa_squared","0")); add(m,b,lambda x:x["regression"]["rows"][2].__setitem__("equilibrium_raw_direction",["1","1"])); add(m,b,lambda x:x["regression"]["rows"][3].__setitem__("period_squared_over_pi_squared","1")); add(m,b,lambda x:x["regression"]["rows"][12].__setitem__("regime","generic")); add(m,b,lambda x:x["regression"].__setitem__("regime_counts",{"generic":16})); add(m,b,lambda x:x["regression"].__setitem__("boundary_rows",[])); add(m,b,lambda x:x.__setitem__("exact_identities",[])); add(m,b,lambda x:x["theorem"].__setitem__("clean_reconstruction","generic has no periodic motion")); add(m,b,lambda x:x.__setitem__("citations",[])); add(m,b,lambda x:x.__setitem__("nonclaims",[]))
 rej=0
 with tempfile.TemporaryDirectory() as td:
  for i,x in enumerate(m):
   p=Path(td)/f"m{i}.json"; p.write_text(json.dumps(x,sort_keys=True,indent=2,ensure_ascii=False)+"\n"); env=dict(os.environ); env["PYTHONDONTWRITEBYTECODE"]="1"; r=subprocess.run([sys.executable,"-B",str(C),"--evidence",str(p)],env=env,text=True,capture_output=True); rej+=r.returncode!=0
 assert rej==len(m); print(f"C255 hostile mutation: PASS {rej}/{len(m)} (including clean-periodic-family denial)")
if __name__=="__main__": main()
