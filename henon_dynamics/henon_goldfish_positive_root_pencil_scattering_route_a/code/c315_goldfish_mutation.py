#!/usr/bin/env python3
import copy,hashlib,json,os,subprocess,sys,tempfile
from pathlib import Path
R=Path(__file__).resolve().parents[1];E=R/"results/c315_goldfish_evidence.json";Y=R/"evaluations/route_a/HCS-C315/2026-09-03.yaml";C=R/"code/c315_goldfish_checker.py"
def ph(d):
 b=dict(d);b.pop("payload_sha256",None);return hashlib.sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def setp(d,p,v):
 c=d
 for x in p[:-1]:c=c[x]
 c[p[-1]]=v
def main():
 if sys.flags.optimize:raise RuntimeError("C315 mutation refuses optimized Python")
 d=json.loads(E.read_text());raw=E.read_text();yr=Y.read_text();att=[]
 muts=[(("candidate_id",),"HCS-C000"),(("obstruction_id",),"HEN-O000"),(("source_commit",),"0"*40),(("scope_literal",),"EXPANDED"),(("route_a","tuple",4),"A4_ROUTE_B_READY"),(("route_a","overall"),"ROUTE_A_ACCEPTED"),(("route_a","route_b_invocation_allowed"),True),(("scope_flags","claims_target_euler_factors"),True),(("model","dynamics"),"wrong"),(("theorem_contract","scattering"),False),(("cases",0,"P_coefficients",0),"2"),(("cases",0,"Q_coefficients",0),"2"),(("cases",1,"total_velocity"),"0"),(("cases",2,"ballistic_intercept"),"0"),(("cases",3,"anchor_roots",0),"999"),(("cases",4,"beta_coefficients",0),"-1"),(("cases",5,"time_rows",0,"roots",0),"0"),(("cases",6,"time_rows",1,"velocities",0),"-1"),(("cases",7,"time_rows",2,"sum_roots"),"0"),(("cases",8,"time_rows",3,"max_ode_residual"),"1"),(("cases",9,"asymptotic_rows",0,"ballistic_root_error"),"1"),(("enumeration","case_count"),13),(("enumeration","anchor_cells"),0),(("evaluation_date",),"2099-01-01"),(("evaluator","version"),"9.9.9"),(("boundary_atlas",0,"status"),"nontrivial"),(("collision_boundary","C196"),"same theorem"),(("nonclaims",0),"priority claimed"),(("references",0,"doi"),"invalid"),(("enumeration","audited_leaf_count"),1)]
 for p,v in muts:
  q=copy.deepcopy(d);setp(q,p,v);q["payload_sha256"]=ph(q);att.append(("repaired",json.dumps(q,sort_keys=True,indent=2)+"\n",yr))
 att += [("stale",raw.replace('"candidate_id": "HCS-C315"','"candidate_id": "HCS-C000"',1),yr),("duplicate",raw.replace("{\n",'{\n  "schema": "duplicate",\n',1),yr),("nan",raw.replace('"fixed_epoch": 1788393600','"fixed_epoch": NaN',1),yr),("array","[]\n",yr)]
 for n,y in [("yaml-duplicate",yr+"candidate_id: HCS-C315\n"),("yaml-anchor",yr.replace("candidate_id: HCS-C315","candidate_id: &x HCS-C315",1)),("yaml-alias",yr+"probe: *x\n"),("yaml-array","- bad\n"),("yaml-route",yr.replace("  - A0_FAIL","  - A0_PASS",1)),("yaml-routeb",yr.replace("route_b_invocation_allowed: false","route_b_invocation_allowed: true",1)),("yaml-scope",yr.replace("  claims_target_euler_factors: false","  claims_target_euler_factors: true",1)),("yaml-epoch",yr.replace("fixed_epoch: 1788393600",'fixed_epoch: "1788393600"',1)),("yaml-family",yr.replace("family: smooth velocity-coupled solvable many-body flow","family: altered family",1)),("yaml-raw-only",yr+"\n")]:att.append((n,raw,y))
 env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1",TZ="UTC");rej=0
 with tempfile.TemporaryDirectory(prefix="c315-mutation-") as tmp:
  for i,(n,j,y) in enumerate(att):
   jp=Path(tmp)/f"{i}.json";yp=Path(tmp)/f"{i}.yaml";jp.write_text(j);yp.write_text(y);p=subprocess.run([sys.executable,"-B",str(C),"--evidence",str(jp),"--evaluation",str(yp)],env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
   if p.returncode==0:raise AssertionError(f"mutation survived {n}-{i}")
   rej+=1
  if subprocess.run([sys.executable,"-O",str(C)],env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).returncode==0:raise AssertionError("optimized checker survived")
  rej+=1
 print(f"C315 hostile mutation suite: PASS {rej}/{len(att)+1}")
if __name__=="__main__":main()
