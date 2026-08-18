#!/usr/bin/env python3
"""Physical theorem and governance mutation harness for Paper 47."""
from __future__ import annotations
import argparse, hashlib, json, os, shutil, stat, subprocess, sys
from pathlib import Path
from typing import Any
FROZEN={
"F01":(["D","P","X"],"SOURCE_RELATION_CHANGED"),"F02":(["D","P","X"],"LOOP_CONVENTION_CHANGED"),
"F03":(["P","X"],"EDGE_PARAMETERIZATION_NONUNIQUE"),"F04":(["P","X"],"EDGE_PARAMETERIZATION_FALSE"),
"F05":(["A","P"],"UNBOUNDED_DEGREE_ENDPOINT"),"F06":(["A","P"],"LOOP_SCALE_HS_DIVERGENCE"),
"F07":(["A","P"],"EVEN_DIAGONAL_TRACE_DIVERGENCE"),"F08":(["D","P","X"],"SECOND_TRACE_SCALE_FAILURE"),
"F09":(["A","P","X"],"PRIMITIVE_MT_FACTOR_FAILURE"),"F10":(["D","P","X"],"ORDERED_EDGE_MULTIPLICITY_FAILURE"),
"F11":(["A"],"PRIMITIVE_TYPE_FAILURE"),"F12":(["A","D"],"NEGATIVE_PRINCIPAL_MINOR"),
"F13":(["A"],"DETERMINANT_DOMAIN_FAILURE"),"F14":(["L"],"LITERATURE_OWNERSHIP_FAILURE"),
"F15":(["D","P","X"],"SUPPORT_WITNESS_FAILURE")}
GOV={
"G01":(["F"],"DUPLICATE_JSON_KEY"),"G02":(["F"],"DUPLICATE_JSON_KEY"),"G03":(["F"],"NONCANONICAL_JSON"),
"G04":(["F"],"SCIENCE_MODEL_SHAPE_FAILURE"),"G05":(["F"],"SCIENCE_MODEL_SHAPE_FAILURE"),
"G06":(["F"],"SCIENCE_MODEL_TYPE_FAILURE"),"G07":(["F"],"SCIENCE_MODEL_TYPE_FAILURE"),"G08":(["F"],"SCIENCE_MODEL_TYPE_FAILURE"),
"G09":(["F"],"RESULT_CHECK_MAP_FAILURE"),"G10":(["F"],"RESULT_CHECK_MAP_FAILURE"),"G11":(["F"],"RESULT_CHECK_MAP_FAILURE"),
"G12":(["F"],"SEALED_RESULT_HASH_FAILURE"),"G13":(["F"],"MUTATION_REGISTRY_FAILURE"),"G14":(["F"],"MUTATION_REGISTRY_FAILURE"),
"G15":(["F"],"MUTATION_REGISTRY_FAILURE"),"G16":(["F"],"MUTATION_REGISTRY_FAILURE"),
"G17":(["R1","R2"],"ROUTE_TUPLE_FAILURE"),"G18":(["R1","R2"],"ROUTE_B_LOCK_FAILURE"),
"G19":(["R1","R2"],"PROVENANCE_STATE_FAILURE"),"G20":(["F"],"OUTPUT_NAMESPACE_FAILURE"),
"G21":(["F"],"OUTPUT_NAMESPACE_FAILURE"),"G22":(["F"],"OUTPUT_NAMESPACE_FAILURE"),
"G23":(["F"],"OUTPUT_NAMESPACE_FAILURE"),"G24":(["F"],"UNSAFE_PATH_FAILURE")}
SCRIPTS={"D":"code/evaluator_d/evaluate.py","P":"code/evaluator_p/evaluate.py","X":"code/comparator/exact_compare.py",
"A":"code/auditors/proof_result_auditor.py","L":"code/auditors/literature_auditor.py","F":"external_auditor/frozen_auditor.py",
"R1":"code/route/validate_route.py","R2":"code/route/audit_route_independent.py"}
def enc(v:Any)->bytes:return (json.dumps(v,sort_keys=True,indent=2,ensure_ascii=True,separators=(",",": "))+"\n").encode("ascii")
def pairs(seq:list[tuple[str,Any]])->dict[str,Any]:
 o={}
 for k,v in seq:
  if k in o:raise ValueError("duplicate")
  o[k]=v
 return o
def load(p:Path)->dict[str,Any]:
 raw=p.read_bytes();o=json.loads(raw.decode("ascii"),object_pairs_hook=pairs)
 if type(o) is not dict or raw!=enc(o):raise ValueError("canonical")
 return o
def tree_rows(root:Path)->list[dict[str,Any]]:
 out=[]
 for p in root.rglob("*"):
  s=os.lstat(p);rel=p.relative_to(root).as_posix();mode=f"{stat.S_IMODE(s.st_mode):04o}"
  if stat.S_ISDIR(s.st_mode):out.append({"kind":"directory","mode":mode,"path":rel})
  elif stat.S_ISREG(s.st_mode):out.append({"kind":"regular","mode":mode,"path":rel,"sha256":hashlib.sha256(p.read_bytes()).hexdigest()})
  else:raise ValueError("baseline namespace kind")
 return sorted(out,key=lambda x:x["path"])
def invoke(root:Path,consumer:str,args:list[str],cwd:Path,hostile:Path)->tuple[int,dict[str,Any]]:
 env={"PATH":os.environ.get("PATH","/usr/bin:/bin"),"PYTHONPATH":str(hostile),"PYTHONDONTWRITEBYTECODE":"1"}
 q=subprocess.run([sys.executable,"-I","-B",str(root/SCRIPTS[consumer]),*args],cwd=cwd,env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False)
 if q.stderr:raise ValueError("consumer stderr")
 try:o=json.loads(q.stdout.decode("ascii"),object_pairs_hook=pairs)
 except Exception as e:raise ValueError("consumer json") from e
 if q.stdout!=enc(o):raise ValueError("consumer canonical")
 return q.returncode,o
def observe(root:Path,consumers:list[str],code:str,argmaker:Any,cwd:Path,hostile:Path)->dict[str,Any]:
 seen={}
 for consumer in consumers:
  rc,obj=invoke(root,consumer,argmaker(consumer),cwd,hostile)
  if rc!=2 or obj!={"consumer":consumer,"rejection_code":code,"schema":"paper47-mutation-rejection-v1","status":"REJECT"}:raise ValueError("mutation survived")
  seen[consumer]={"exit":rc,"rejection_code":obj["rejection_code"]}
 if sorted(seen)!=sorted(consumers):raise ValueError("consumer set")
 return seen
def main()->None:
 p=argparse.ArgumentParser(allow_abbrev=False);p.add_argument("--root",required=True);p.add_argument("--scratch",required=True);p.add_argument("--direct",required=True);p.add_argument("--parameter",required=True);p.add_argument("--comparison",required=True);a=p.parse_args()
 try:
  root=Path(a.root).resolve(strict=True);scratch=Path(a.scratch)
  if scratch.exists() or scratch.is_symlink():raise ValueError("scratch exists")
  scratch.mkdir(parents=True,mode=0o700);cwd=scratch/"hostile_cwd";hostile=scratch/"hostile_modules";cwd.mkdir();hostile.mkdir()
  (hostile/"json.py").write_text("raise RuntimeError('shadow')\n",encoding="ascii")
  registry_path=root/"contracts/MUTATION_REGISTRY.json";registry=load(registry_path);rows=registry["instances"]
  expected={**FROZEN,**GOV}
  if [x["id"] for x in rows]!=list(expected) or any((x["designated_consumers"],x["rejection_code"])!=expected[x["id"]] or x["required_exit"]!=2 for x in rows):raise ValueError("registry not frozen")
  byid={x["id"]:x for x in rows};records=[];model0=load(root/"contracts/SCIENCE_MODEL.json")
  for mid,(consumers,code) in FROZEN.items():
   row=byid[mid];case=scratch/mid;case.mkdir();model=json.loads(json.dumps(model0))
   bits=row["pointer"].split("/")[1:];cur=model
   for bit in bits[:-1]:cur=cur[bit]
   cur[bits[-1]]=row["value"]
   mp=case/"SCIENCE_MODEL.json";mp.write_bytes(enc(model))
   seen=observe(root,consumers,code,lambda _:["--validate-model",str(mp)],cwd,hostile)
   records.append({"designated_consumers":consumers,"id":mid,"observed":seen,"rejection_code":code,"survivor":False})
  auditor=lambda args: observe(root,["F"],GOV[current][1],lambda _:args,cwd,hostile)
  model_raw=(root/"contracts/SCIENCE_MODEL.json").read_bytes();comparison0=load(Path(a.comparison));comparison_sha=hashlib.sha256(enc(comparison0)).hexdigest();registry_sha=hashlib.sha256(registry_path.read_bytes()).hexdigest()
  for current in [f"G{x:02d}" for x in range(1,17)]:
   case=scratch/current;case.mkdir();code=GOV[current][1]
   if current in ("G01","G02","G03"):
    target=case/"artifact.json"
    if current=="G01":raw=model_raw.replace(b'  "relation": "m_plus_n_divides_m_times_n",\n',b'  "relation": "m_plus_n_divides_m_times_n",\n  "relation": "m_plus_n_divides_m_times_n",\n')
    elif current=="G02":raw=model_raw.replace(b'    "ordinary": "Re_s_gt_1"\n',b'    "ordinary": "Re_s_gt_1",\n    "ordinary": "Re_s_gt_1"\n')
    else:raw=(json.dumps({k:model0[k] for k in reversed(list(model0))},sort_keys=False,indent=2,ensure_ascii=True,separators=(",",": "))+"\n").encode("ascii")
    target.write_bytes(raw);seen=auditor(["--artifact",str(target),"--kind","model"])
   elif current in ("G04","G05","G06","G07","G08"):
    obj=json.loads(json.dumps(model0))
    if current=="G04":del obj["candidate_id"]
    elif current=="G05":obj["unexpected"]=1
    elif current=="G06":obj["relation"]=[obj["relation"]]
    elif current=="G07":obj["ordered_edge_multiplier"]=True
    else:obj["ordered_edge_multiplier"]=1.0
    target=case/"model.json";target.write_bytes(enc(obj));seen=auditor(["--artifact",str(target),"--kind","model"])
   elif current in ("G09","G10","G11","G12"):
    obj=json.loads(json.dumps(comparison0))
    if current=="G09":del obj["payload"]["checks"]["based_closed_walks"]
    elif current=="G10":obj["payload"]["checks"]["unexpected"]="PASS"
    elif current=="G11":obj["payload"]["checks"]["minor_negative"]=obj["payload"]["checks"].pop("negative_principal_minor")
    else:
     declared=byid[current]
     if declared["operation"]!="replace" or declared["pointer"]!="/payload/direct_sha256":raise ValueError("G12 registry behavior")
     obj["payload"]["direct_sha256"]=declared["value"]
    target=case/"result.json";target.write_bytes(enc(obj));seen=auditor(["--artifact",str(target),"--kind","result","--expected-sha256",comparison_sha])
   else:
    obj=json.loads(json.dumps(registry))
    if current=="G13":del obj["instances"][0]
    elif current=="G14":obj["instances"].append({})
    elif current=="G15":obj["instances"][0],obj["instances"][1]=obj["instances"][1],obj["instances"][0]
    else:obj["instances"][0]["designated_consumers"]=["D","P"]
    target=case/"registry.json";target.write_bytes(enc(obj));seen=auditor(["--artifact",str(target),"--kind","registry","--expected-sha256",registry_sha])
   records.append({"designated_consumers":["F"],"id":current,"observed":seen,"rejection_code":code,"survivor":False})
  route_raw=subprocess.run([sys.executable,"-I","-B",str(root/"code/route/render_route.py"),"--state","A"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True).stdout;route0=json.loads(route_raw)
  for current in ("G17","G18","G19"):
   obj=json.loads(json.dumps(route0))
   if current=="G17":obj["route_tuple"][0]="A0_FAIL"
   elif current=="G18":obj["route_b"]["invocation_allowed"]=True
   else:obj["source_commit"]="0"*40
   rp=scratch/current;rp.mkdir();q=rp/"route.json";q.write_bytes(enc(obj));consumers,code=GOV[current]
   seen=observe(root,consumers,code,lambda consumer:["--route",str(q),"--root",str(root),"--state","A"],cwd,hostile)
   records.append({"designated_consumers":consumers,"id":current,"observed":seen,"rejection_code":code,"survivor":False})
  base=scratch/"namespace_baseline"; (base/"results").mkdir(parents=True);(base/"audits").mkdir();(base/"results/evaluator_d.json").write_bytes(Path(a.direct).read_bytes());(base/"results/evaluator_p.json").write_bytes(Path(a.parameter).read_bytes());(base/"audits/comparison.json").write_bytes(Path(a.comparison).read_bytes())
  for q in base.rglob("*"):
   q.chmod(0o755 if q.is_dir() else 0o644)
  manifest=scratch/"namespace_manifest.json";manifest.write_bytes(enc({"rows":tree_rows(base),"schema":"paper47-namespace-manifest-v1"}))
  outside=scratch/"outside_sentinel";outside.write_text("P47_OUTSIDE_SENTINEL\n",encoding="ascii");outside_before=outside.read_bytes()
  for current in ("G20","G21","G22","G23"):
   case=scratch/current;shutil.copytree(base,case)
   target=case/"results/evaluator_d.json"
   if current=="G20":target.unlink()
   elif current=="G21":target.rename(case/"results/evaluator_direct.json")
   elif current=="G22":(case/"extra.json").write_bytes(b"{}\n")
   else:target.unlink();target.symlink_to(outside)
   seen=auditor(["--namespace",str(case),"--namespace-manifest",str(manifest)])
   records.append({"designated_consumers":["F"],"id":current,"observed":seen,"rejection_code":GOV[current][1],"survivor":False})
  current="G24";seen=auditor(["--check-relative","../outside"]);records.append({"designated_consumers":["F"],"id":current,"observed":seen,"rejection_code":GOV[current][1],"survivor":False})
  if outside.read_bytes()!=outside_before:raise ValueError("outside sentinel changed")
  result={"candidate_id":"SD-C49","payload":{"consumer_invocation_count":sum(len(x["designated_consumers"]) for x in records),"instance_count":len(records),"records":records,"registry_sha256":registry_sha,"survivors":0},"schema":"paper47-mutation-results-v1","status":"PASS"}
  sys.stdout.buffer.write(enc(result))
 except Exception as e:sys.stderr.write(f"MUTATION_ERROR:{type(e).__name__}\n");raise SystemExit(3)
if __name__=="__main__":main()
