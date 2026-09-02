#!/usr/bin/env python3
import copy,hashlib,json,os,subprocess,sys,tempfile
from pathlib import Path
R=Path(__file__).resolve().parents[1];E=R/"results/c312_hk_evidence.json";Y=R/"evaluations/route_a/HCS-C312/2026-09-03.yaml";C=R/"code/c312_hk_checker.py"
def ph(d):
 b=dict(d);b.pop("payload_sha256",None);return hashlib.sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def setp(d,p,v):
 c=d
 for k in p[:-1]:c=c[k]
 c[p[-1]]=v
def main():
 d=json.loads(E.read_text());raw=E.read_text();yr=Y.read_text();att=[];m=[(("candidate_id",),"HCS-C000"),(("obstruction_id",),"HEN-O000"),(("source_commit",),"0"*40),(("scope_literal",),"EXPANDED"),(("route_a","tuple",1),"A1_PASS"),(("route_a","route_b_invocation_allowed"),True),(("scope_flags","claims_target_zero_match"),True),(("mean_counterexample","updated_mean"),"19/30"),(("cases",0,"epsilon"),"2"),(("cases",0,"termination_time"),0),(("cases",1,"initial",1),"1"),(("cases",2,"final_mean"),"19/30"),(("cases",3,"trajectory",0,0),"1"),(("cases",4,"trajectory_sha256"),"0"*64),(("cases",5,"neighbor_graph_changes"),99),(("cases",6,"theorem_bound"),1),(("cases",7,"final_clusters",0,"multiplicity"),99),(("enumeration","case_count"),0)]
 for p,v in m:
  x=copy.deepcopy(d);setp(x,p,v);x["payload_sha256"]=ph(x);att.append(("semantic",json.dumps(x,sort_keys=True,indent=2)+"\n",yr))
 att += [("duplicate",raw.replace("{\n",'{\n  "schema": "duplicate",\n',1),yr),("nan",raw.replace('"fixed_epoch": 1788393600','"fixed_epoch": NaN',1),yr),("array","[]\n",yr)]
 for n,y in [("ydup",yr+"candidate_id: HCS-C312\n"),("yanchor",yr.replace("candidate_id: HCS-C312","candidate_id: &x HCS-C312",1)),("yroute",yr.replace("route_b_invocation_allowed: false","route_b_invocation_allowed: true",1)),("yscope",yr.replace("  claims_target_zero_match: false","  claims_target_zero_match: true",1)),("yarray","- bad\n")]:att.append((n,raw,y))
 env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1",TZ="UTC");rej=0
 with tempfile.TemporaryDirectory(prefix="c312-mut-") as t:
  for i,(n,j,y) in enumerate(att):
   jp=Path(t)/f"{i}.json";yp=Path(t)/f"{i}.yaml";jp.write_text(j);yp.write_text(y);p=subprocess.run([sys.executable,"-B",str(C),"--evidence",str(jp),"--evaluation",str(yp)],env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
   if p.returncode==0:raise AssertionError(f"survived {n}-{i}")
   rej+=1
 print(f"C312 hostile mutation suite: PASS {rej}/{len(att)}")
if __name__=="__main__":main()
