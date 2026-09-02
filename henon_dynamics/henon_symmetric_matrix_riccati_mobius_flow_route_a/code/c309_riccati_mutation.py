#!/usr/bin/env python3
"""Repaired-hash semantic attacks for HCS-C309."""
import copy, hashlib, json, os, subprocess, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; E=ROOT/"results/c309_riccati_evidence.json"; Y=ROOT/"evaluations/route_a/HCS-C309/2026-09-03.yaml"; C=ROOT/"code/c309_riccati_checker.py"
def ph(data):
    body=dict(data);body.pop("payload_sha256",None)
    return hashlib.sha256(json.dumps(body,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def setp(data,path,value):
    cur=data
    for item in path[:-1]:cur=cur[item]
    cur[path[-1]]=value
def main():
    pristine=json.loads(E.read_text()); yaml_raw=Y.read_text(); attacks=[]
    mutations=[
      (("candidate_id",),"HCS-C000"),(("obstruction_id",),"HEN-O000"),(("source_commit",),"0"*40),
      (("scope_literal",),"EXPANDED"),(("route_a","tuple",4),"A4_PASS"),(("route_a","overall"),"ROUTE_A_ACCEPTED"),
      (("route_a","route_b_invocation_allowed"),True),(("scope_flags","claims_target_euler_factors"),True),
      (("model","dynamics"),"Xdot=X^2-I"),(("theorem_contract","forward_atlas"),False),
      (("cases",0,"forward_global"),True),(("cases",0,"forward_poles",0,"index"),1),
      (("cases",1,"forward_limit",0),"1"),(("cases",2,"probe_rows",0,"time"),"0"),
      (("cases",3,"loewner_time"),"0.8"),(("cases",4,"loewner_factors",0,0),"1.0"),
      (("cases",7,"eigenvalues",0),"-2"),(("cases",8,"backward_poles",0,"time"),"0.0"),
      (("equilibrium_strata",0,"stable_dimension"),1),(("equilibrium_strata",10,"center_dimension"),99),
      (("enumeration","case_count"),15),(("enumeration","stratum_count"),43),
    ]
    for path,value in mutations:
        changed=copy.deepcopy(pristine);setp(changed,path,value);changed["payload_sha256"]=ph(changed)
        attacks.append(("semantic",json.dumps(changed,sort_keys=True,indent=2)+"\n",yaml_raw))
    raw=E.read_text(); attacks += [("stale",raw.replace('"candidate_id": "HCS-C309"','"candidate_id": "HCS-C000"',1),yaml_raw),("duplicate",raw.replace("{\n",'{\n  "schema": "duplicate",\n',1),yaml_raw),("nan",raw.replace('"fixed_epoch": 1788393600','"fixed_epoch": NaN',1),yaml_raw),("array","[]\n",yaml_raw)]
    yaml_attacks=[
      ("yaml-duplicate",yaml_raw+"candidate_id: HCS-C309\n"),
      ("yaml-anchor",yaml_raw.replace("candidate_id: HCS-C309","candidate_id: &bad HCS-C309",1)),
      ("yaml-alias",yaml_raw+"probe: *bad\n"),("yaml-array","- bad\n"),
      ("yaml-route",yaml_raw.replace("  - A0_FAIL","  - A0_PASS",1)),
      ("yaml-routeb",yaml_raw.replace("route_b_invocation_allowed: false","route_b_invocation_allowed: true",1)),
      ("yaml-scope",yaml_raw.replace("  claims_target_euler_factors: false","  claims_target_euler_factors: true",1)),
      ("yaml-epoch",yaml_raw.replace("fixed_epoch: 1788393600",'fixed_epoch: "1788393600"',1)),
    ]
    attacks += [(name,raw,text) for name,text in yaml_attacks]
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1",TZ="UTC"); rejected=0
    with tempfile.TemporaryDirectory(prefix="c309-mutation-") as tmp:
      for i,(name,text,yaml_text) in enumerate(attacks):
        path=Path(tmp)/f"{i}.json";ypath=Path(tmp)/f"{i}.yaml";path.write_text(text);ypath.write_text(yaml_text)
        run=subprocess.run([sys.executable,"-B",str(C),"--evidence",str(path),"--evaluation",str(ypath)],env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        if run.returncode==0:raise AssertionError(f"mutation survived {name}-{i}")
        rejected+=1
    print(f"C309 hostile mutation suite: PASS {rejected}/{len(attacks)}")
if __name__=="__main__":main()
