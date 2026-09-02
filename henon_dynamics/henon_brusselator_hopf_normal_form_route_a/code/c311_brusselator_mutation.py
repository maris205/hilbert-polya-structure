#!/usr/bin/env python3
import copy,hashlib,json,os,subprocess,sys,tempfile
from pathlib import Path
R=Path(__file__).resolve().parents[1];E=R/"results/c311_brusselator_evidence.json";Y=R/"evaluations/route_a/HCS-C311/2026-09-03.yaml";C=R/"code/c311_brusselator_checker.py"
def ph(d):
 b=dict(d);b.pop("payload_sha256",None);return hashlib.sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def setp(d,p,v):
 c=d
 for k in p[:-1]:c=c[k]
 c[p[-1]]=v
def main():
 d=json.loads(E.read_text());raw=E.read_text();yr=Y.read_text();att=[];m=[(("candidate_id",),"HCS-C000"),(("obstruction_id",),"HEN-O000"),(("source_commit",),"0"*40),(("scope_literal",),"EXPANDED"),(("route_a","tuple",1),"A1_PASS"),(("route_a","route_b_invocation_allowed"),True),(("scope_flags","claims_root_number"),True),(("model","dynamics"),False),(("parameter_rows",0,"hopf_B"),"1"),(("parameter_rows",1,"equilibrium","y"),"0"),(("parameter_rows",2,"jacobian",0,0),"0"),(("parameter_rows",3,"linear_boundaries","stable_defective_B"),"0"),(("parameter_rows",4,"hopf_data","G21_real"),"1"),(("parameter_rows",5,"hopf_data","G21_imag"),"0"),(("parameter_rows",6,"hopf_data","kuznetsov_l1"),"1"),(("parameter_rows",7,"hopf_data","radius_squared_per_mu"),"0"),(("parameter_rows",8,"linear_probes",0,"trace"),"0"),(("enumeration","A_rows"),11)]
 for p,v in m:
  x=copy.deepcopy(d);setp(x,p,v);x["payload_sha256"]=ph(x);att.append(("semantic",json.dumps(x,sort_keys=True,indent=2)+"\n",yr))
 att += [("duplicate",raw.replace("{\n",'{\n  "schema": "duplicate",\n',1),yr),("nan",raw.replace('"fixed_epoch": 1788393600','"fixed_epoch": NaN',1),yr),("array","[]\n",yr)]
 for n,y in [("ydup",yr+"candidate_id: HCS-C311\n"),("yanchor",yr.replace("candidate_id: HCS-C311","candidate_id: &x HCS-C311",1)),("yroute",yr.replace("route_b_invocation_allowed: false","route_b_invocation_allowed: true",1)),("yscope",yr.replace("  claims_root_number: false","  claims_root_number: true",1)),("yarray","- bad\n")]:att.append((n,raw,y))
 env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1",TZ="UTC");rej=0
 with tempfile.TemporaryDirectory(prefix="c311-mut-") as t:
  for i,(n,j,y) in enumerate(att):
   jp=Path(t)/f"{i}.json";yp=Path(t)/f"{i}.yaml";jp.write_text(j);yp.write_text(y);p=subprocess.run([sys.executable,"-B",str(C),"--evidence",str(jp),"--evaluation",str(yp)],env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
   if p.returncode==0:raise AssertionError(f"survived {n}-{i}")
   rej+=1
 print(f"C311 hostile mutation suite: PASS {rej}/{len(att)}")
if __name__=="__main__":main()
