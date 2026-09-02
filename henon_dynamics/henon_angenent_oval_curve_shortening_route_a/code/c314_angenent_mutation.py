#!/usr/bin/env python3
"""Repaired/stale-hash and parser attacks for HCS-C314."""
import copy,hashlib,json,os,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];E=ROOT/"results/c314_angenent_evidence.json";Y=ROOT/"evaluations/route_a/HCS-C314/2026-09-03.yaml";C=ROOT/"code/c314_angenent_checker.py"
def ph(d):
 b=dict(d);b.pop("payload_sha256",None);return hashlib.sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def setp(d,path,value):
 cur=d
 for key in path[:-1]:cur=cur[key]
 cur[path[-1]]=value
def main():
 if sys.flags.optimize:raise RuntimeError("C314 mutation lane refuses optimized Python")
 pristine=json.loads(E.read_text());raw=E.read_text();yr=Y.read_text();attacks=[]
 mutations=[
  (("candidate_id",),"HCS-C000"),(("obstruction_id",),"HEN-O000"),(("source_commit",),"0"*40),(("scope_literal",),"EXPANDED"),
  (("route_a","tuple",0),"A0_PASS"),(("route_a","overall"),"ROUTE_A_ACCEPTED"),(("route_a","route_b_invocation_allowed"),True),(("scope_flags","claims_target_zero_match"),True),
  (("model","implicit_curve"),"cos(x)=exp(-t) cosh(y)"),(("theorem_contract","foliation"),False),(("parameter_rows",0,"time"),"0"),(("parameter_rows",1,"horizontal_width"),"3"),
  (("parameter_rows",2,"area_formula"),"1"),(("parameter_rows",3,"length_formula"),"1"),(("parameter_rows",4,"curvature_min"),"1"),(("parameter_rows",5,"point_rows",0,"gradient_norm_squared"),"0"),
  (("parameter_rows",6,"point_rows",1,"arrival_pde_lhs"),"-1"),(("parameter_rows",7,"point_rows",2,"inward_speed"),"0"),(("extinction_rows",0,"scaled_curvature_max"),"7"),(("grim_rows",0,"samples",1,"grim_target"),"0"),
  (("enumeration","parameter_rows"),19),(("enumeration","point_rows"),219),
  (("evaluation_date",),"2099-01-01"),(("evaluator","version"),"9.9.9"),
  (("boundary_atlas",0,"status"),"smooth timeslice"),(("collision_boundary","C281"),"same owner"),
  (("nonclaims",0),"priority claimed"),(("references",0,"doi"),"invalid"),
  (("enumeration","audited_leaf_count"),1),
 ]
 for path,value in mutations:
  d=copy.deepcopy(pristine);setp(d,path,value);d["payload_sha256"]=ph(d);attacks.append(("repaired",json.dumps(d,sort_keys=True,indent=2)+"\n",yr))
 attacks += [("stale",raw.replace('"candidate_id": "HCS-C314"','"candidate_id": "HCS-C000"',1),yr),("duplicate",raw.replace("{\n",'{\n  "schema": "duplicate",\n',1),yr),("nan",raw.replace('"fixed_epoch": 1788393600','"fixed_epoch": NaN',1),yr),("array","[]\n",yr)]
 for name,text in [("yaml-duplicate",yr+"candidate_id: HCS-C314\n"),("yaml-anchor",yr.replace("candidate_id: HCS-C314","candidate_id: &x HCS-C314",1)),("yaml-alias",yr+"probe: *x\n"),("yaml-array","- bad\n"),("yaml-route",yr.replace("  - A0_FAIL","  - A0_PASS",1)),("yaml-routeb",yr.replace("route_b_invocation_allowed: false","route_b_invocation_allowed: true",1)),("yaml-scope",yr.replace("  claims_target_euler_factors: false","  claims_target_euler_factors: true",1)),("yaml-epoch",yr.replace("fixed_epoch: 1788393600",'fixed_epoch: "1788393600"',1)),("yaml-family",yr.replace("family: nonlinear geometric parabolic flow","family: altered family",1)),("yaml-raw-only",yr+"\n")]:attacks.append((name,raw,text))
 env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1",TZ="UTC");rejected=0
 with tempfile.TemporaryDirectory(prefix="c314-mutation-") as tmp:
  for i,(name,jtext,ytext) in enumerate(attacks):
   jp=Path(tmp)/f"{i}.json";yp=Path(tmp)/f"{i}.yaml";jp.write_text(jtext);yp.write_text(ytext)
   run=subprocess.run([sys.executable,"-B",str(C),"--evidence",str(jp),"--evaluation",str(yp)],env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
   if run.returncode==0:raise AssertionError(f"mutation survived {name}-{i}")
   rejected+=1
  opt=subprocess.run([sys.executable,"-O",str(C)],env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
  if opt.returncode==0:raise AssertionError("optimized checker survived")
  rejected+=1
 print(f"C314 hostile mutation suite: PASS {rejected}/{len(attacks)+1}")
if __name__=="__main__":main()
