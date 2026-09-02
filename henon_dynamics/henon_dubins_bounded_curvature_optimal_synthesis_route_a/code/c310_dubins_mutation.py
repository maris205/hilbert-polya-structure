#!/usr/bin/env python3
import copy,hashlib,json,os,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];E=ROOT/"results/c310_dubins_evidence.json";Y=ROOT/"evaluations/route_a/HCS-C310/2026-09-03.yaml";C=ROOT/"code/c310_dubins_checker.py"
def ph(d):
 b=dict(d);b.pop("payload_sha256",None);return hashlib.sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def setp(d,path,v):
 c=d
 for k in path[:-1]:c=c[k]
 c[path[-1]]=v
def main():
 pristine=json.loads(E.read_text());raw=E.read_text();yr=Y.read_text();att=[]
 muts=[(("candidate_id",),"HCS-C000"),(("obstruction_id",),"HEN-O000"),(("source_commit",),"0"*40),(("scope_literal",),"EXPANDED"),(("route_a","tuple",4),"A4_PASS"),(("route_a","route_b_invocation_allowed"),True),(("scope_flags","claims_target_euler_factors"),True),(("cases",0,"target","x"),"1"),(("cases",0,"minimum_length"),"1.0"),(("cases",1,"minimizers",0),"RLR"),(("cases",2,"target","radius"),"1"),(("cases",3,"normalized","d"),"2.0"),(("cases",4,"candidates",0,"word"),"RSR"),(("cases",5,"candidates",0,"feasible"),False),(("cases",6,"candidates",0,"segments",0),"0.0"),(("cases",7,"candidates",0,"physical_length"),"0.0"),(("cases",8,"candidates",4,"feasibility_value"),"0.0"),(("cases",9,"candidates",4,"feasible"),True),(("cases",10,"candidates",0,"endpoint_residual"),"1.0"),(("word_coverage","LSL"),0),(("enumeration","case_count"),29)]
 for path,v in muts:
  d=copy.deepcopy(pristine);setp(d,path,v);d["payload_sha256"]=ph(d);att.append(("semantic",json.dumps(d,sort_keys=True,indent=2)+"\n",yr))
 att += [("stale",raw.replace('"candidate_id": "HCS-C310"','"candidate_id": "HCS-C000"',1),yr),("duplicate",raw.replace("{\n",'{\n  "schema": "duplicate",\n',1),yr),("nan",raw.replace('"fixed_epoch": 1788393600','"fixed_epoch": NaN',1),yr),("array","[]\n",yr)]
 for name,y in [("yaml-duplicate",yr+"candidate_id: HCS-C310\n"),("yaml-anchor",yr.replace("candidate_id: HCS-C310","candidate_id: &x HCS-C310",1)),("yaml-routeb",yr.replace("route_b_invocation_allowed: false","route_b_invocation_allowed: true",1)),("yaml-scope",yr.replace("  claims_target_euler_factors: false","  claims_target_euler_factors: true",1)),("yaml-array","- bad\n")]:att.append((name,raw,y))
 env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1",TZ="UTC");rej=0
 with tempfile.TemporaryDirectory(prefix="c310-mut-") as tmp:
  for i,(name,j,y) in enumerate(att):
   jp=Path(tmp)/f"{i}.json";yp=Path(tmp)/f"{i}.yaml";jp.write_text(j);yp.write_text(y)
   run=subprocess.run([sys.executable,"-B",str(C),"--evidence",str(jp),"--evaluation",str(yp)],env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
   if run.returncode==0:raise AssertionError(f"mutation survived {name}-{i}")
   rej+=1
 print(f"C310 hostile mutation suite: PASS {rej}/{len(att)}")
if __name__=="__main__":main()
