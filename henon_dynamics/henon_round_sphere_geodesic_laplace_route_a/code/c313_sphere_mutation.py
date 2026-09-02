#!/usr/bin/env python3
import copy,hashlib,json,os,subprocess,sys,tempfile
from pathlib import Path
R=Path(__file__).resolve().parents[1];E=R/"results/c313_sphere_evidence.json";Y=R/"evaluations/route_a/HCS-C313/2026-09-03.yaml";C=R/"code/c313_sphere_checker.py"
def ph(d):
 b=dict(d);b.pop("payload_sha256",None);return hashlib.sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def setp(d,p,v):
 c=d
 for k in p[:-1]:c=c[k]
 c[p[-1]]=v
def main():
 d=json.loads(E.read_text());raw=E.read_text();yr=Y.read_text();att=[];m=[(("candidate_id",),"HCS-C000"),(("obstruction_id",),"HEN-O000"),(("source_commit",),"0"*40),(("scope_literal",),"EXPANDED"),(("route_a","tuple",4),"A4_PASS"),(("route_a","route_b_invocation_allowed"),True),(("scope_flags","claims_hilbert_polya_operator"),True),(("dimension_rows",0,"radius"),"1"),(("dimension_rows",0,"phase_dimension"),4),(("dimension_rows",0,"period_phase"),1),(("dimension_rows",0,"spectral_rows",1,"laplace_eigenvalue"),"1"),(("dimension_rows",1,"spectral_rows",2,"multiplicity"),1),(("dimension_rows",2,"spectral_rows",3,"cumulative_multiplicity"),0),(("dimension_rows",3,"spectral_rows",4,"shifted_frequency"),"0"),(("dimension_rows",4,"heat_partial_sums",0,"partial_trace"),"0.0"),(("geodesic_probes",0,"x",0),"0.0"),(("geodesic_probes",1,"sphere_residual"),"1.0"),(("enumeration","spectral_cells"),450)]
 for p,v in m:
  x=copy.deepcopy(d);setp(x,p,v);x["payload_sha256"]=ph(x);att.append(("semantic",json.dumps(x,sort_keys=True,indent=2)+"\n",yr))
 att += [("duplicate",raw.replace("{\n",'{\n  "schema": "duplicate",\n',1),yr),("nan",raw.replace('"fixed_epoch": 1788393600','"fixed_epoch": NaN',1),yr),("array","[]\n",yr)]
 for n,y in [("ydup",yr+"candidate_id: HCS-C313\n"),("yanchor",yr.replace("candidate_id: HCS-C313","candidate_id: &x HCS-C313",1)),("yroute",yr.replace("route_b_invocation_allowed: false","route_b_invocation_allowed: true",1)),("yscope",yr.replace("  claims_hilbert_polya_operator: false","  claims_hilbert_polya_operator: true",1)),("yarray","- bad\n")]:att.append((n,raw,y))
 env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1",TZ="UTC");rej=0
 with tempfile.TemporaryDirectory(prefix="c313-mut-") as t:
  for i,(n,j,y) in enumerate(att):
   jp=Path(t)/f"{i}.json";yp=Path(t)/f"{i}.yaml";jp.write_text(j);yp.write_text(y);p=subprocess.run([sys.executable,"-B",str(C),"--evidence",str(jp),"--evaluation",str(yp)],env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
   if p.returncode==0:raise AssertionError(f"survived {n}-{i}")
   rej+=1
 print(f"C313 hostile mutation suite: PASS {rej}/{len(att)}")
if __name__=="__main__":main()
