#!/usr/bin/env python3
"""Physical full-object Route, filesystem, hostile-CWD, and CLI probes."""
from __future__ import annotations
import argparse,json,os,shutil,subprocess,sys
from pathlib import Path
from typing import Any
def enc(v:Any)->bytes:return (json.dumps(v,sort_keys=True,indent=2,ensure_ascii=True,separators=(",",": "),allow_nan=False)+"\n").encode("ascii")
def invoke(cmd,cwd,expected):
 env={"PATH":os.environ.get("PATH","/usr/bin:/bin"),"PYTHONPATH":str(cwd/"hostile_modules"),"PYTHONDONTWRITEBYTECODE":"1","PYTHONHASHSEED":"0","LC_ALL":"C","LANG":"C"}
 q=subprocess.run(cmd,cwd=cwd,env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False,timeout=60)
 return q,q.returncode==expected
def pointer_set(obj,pointer,value):
 node=obj
 parts=pointer.strip("/").split("/")
 for part in parts[:-1]:node=node[int(part)] if isinstance(node,list) else node[part]
 last=parts[-1];node[int(last) if isinstance(node,list) else last]=value
def run(root:Path,scratch:Path,state:str,static:str,commit:str|None):
 scratch.mkdir(parents=True);(scratch/"hostile_modules").mkdir();(scratch/"hostile_modules/json.py").write_text("raise RuntimeError('hostile shadow')\n")
 records=[];survivors=[]
 coordinated_q=subprocess.run([sys.executable,"-I","-B",str(root/"code/tests/run_coordinated_mutations.py"),"--root",str(root),"--scratch",str(scratch/"coordinated")],cwd=scratch,env={"PATH":os.environ.get("PATH","/usr/bin:/bin"),"PYTHONDONTWRITEBYTECODE":"1"},stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False,timeout=900)
 coordinated=json.loads(coordinated_q.stdout.decode("ascii")) if coordinated_q.returncode in (0,2) and not coordinated_q.stderr else {"status":"HOLD","instance_count":0,"consumer_invocations":0,"survivors":1}
 if coordinated_q.returncode!=0 or coordinated.get("survivors")!=0:survivors.append("coordinated_mutations")
 route=scratch/"route.json";cmd=[sys.executable,"-I","-B",str(root/"code/route/render_route.py"),"--root",str(root),"--state",state,"--static-digest",static]+(["--commit",commit] if commit else [])
 q,ok=invoke(cmd,scratch,0);route.write_bytes(q.stdout)
 if not ok:raise ValueError("render")
 route_obj=json.loads(route.read_text())
 route_cases=[("evaluation_state","/evaluation_state","EVALUATED"),("overall","/overall_verdict","STOP_DUPLICATE"),("tuple","/route_tuple/0","A0_WEAK_ARITHMETIC_RELATION"),("route_b","/route_b/invocation_allowed",True),("status_bool","/integration/status",True),("status_int","/integration/status",1),("extra","/unexpected",True)]
 validators=[("R_MAIN","code/route/validate_route.py"),("R_INDEPENDENT","code/route/audit_route_independent.py")]
 for name,pointer,value in route_cases:
  attacked=json.loads(json.dumps(route_obj));
  if pointer=="/unexpected":attacked["unexpected"]=value
  else:pointer_set(attacked,pointer,value)
  path=scratch/(name+".json");path.write_bytes(enc(attacked))
  for consumer,rel in validators:
   args=[sys.executable,"-I","-B",str(root/rel),"--root",str(root),"--route",str(path),"--state",state,"--static-digest",static]+(["--commit",commit] if commit else [])
   observed,passed=invoke(args,scratch,2)
   ident=f"route_{name}_{consumer}";records.append({"id":ident,"exit":observed.returncode,"survivor":not passed})
   if not passed:survivors.append(ident)
 # Invalid mixed-state provenance is rejected before output creation.
 provenance=[("A_with_commit",["--state","A","--commit","1"*40]),("B_missing_commit",["--state","B"]),("B_zero_commit",["--state","B","--commit","0"*40])]
 for name,args in provenance:
  cmd=[sys.executable,"-I","-B",str(root/"code/route/render_route.py"),"--root",str(root),"--static-digest",static,*args]
  observed,passed=invoke(cmd,scratch,3);records.append({"id":name,"exit":observed.returncode,"survivor":not passed});
  if not passed:survivors.append(name)
 # G sees actual symlink, cache, and FIFO nodes in disposable whole-tree clones.
 for name,operation in (("physical_symlink","symlink"),("physical_cache","cache"),("physical_fifo","fifo")):
  clone=scratch/(name+"-tree");shutil.copytree(root,clone,symlinks=True,ignore=shutil.ignore_patterns("outputs","__pycache__","*.pyc"))
  if operation=="symlink":(clone/"bad-link").symlink_to("README.md")
  elif operation=="cache":(clone/"__pycache__").mkdir()
  else:os.mkfifo(clone/"bad.fifo")
  expected_exit=2 if operation in {"symlink","cache"} else 3
  observed,passed=invoke([sys.executable,"-I","-B",str(clone/"code/integration/audit_integrity.py"),"--root",str(clone),"--preflight"],scratch,expected_exit)
  records.append({"id":name,"exit":observed.returncode,"survivor":not passed});
  if not passed:survivors.append(name)
  shutil.rmtree(clone)
 # Exact arity and hostile import isolation.
 for name,rel in (("A_cli","code/evaluator_a/evaluate.py"),("B_cli","code/evaluator_b/evaluate.py"),("P_cli","code/proof_auditor/audit.py")):
  observed,passed=invoke([sys.executable,"-I","-B",str(root/rel)],scratch,3);records.append({"id":name,"exit":observed.returncode,"survivor":not passed});
  if not passed:survivors.append(name)
 observed,passed=invoke([sys.executable,"-I","-B",str(root/"code/auditors/source_auditor.py"),"--root",str(root)],scratch,0);records.append({"id":"hostile_cwd_pythonpath","exit":observed.returncode,"survivor":not passed});
 if not passed:survivors.append("hostile_cwd_pythonpath")
 # Frozen external auditor physical drift suite.
 external=subprocess.run([sys.executable,"-I","-B",str(root/"code/tests/run_external_auditor_mutations.py"),"--root",str(root),"--scratch",str(scratch/"external")],cwd=scratch,env={"PATH":os.environ.get("PATH","/usr/bin:/bin"),"PYTHONDONTWRITEBYTECODE":"1"},stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False,timeout=180)
 ext=json.loads(external.stdout.decode("ascii")) if external.returncode in (0,2) and not external.stderr else {"status":"HOLD","instance_count":0,"survivors":1}
 if external.returncode!=0 or ext.get("survivors")!=0:survivors.append("external_static_suite")
 records.append({"id":"external_static_suite","exit":external.returncode,"survivor":external.returncode!=0})
 physical=len(records)-1+ext.get("instance_count",0)+coordinated.get("instance_count",0)
 return {"candidate_id":"SD-C50","coordinated_consumer_invocations":coordinated.get("consumer_invocations",0),"coordinated_mutation_instances":coordinated.get("instance_count",0),"driver_transaction_probes":["forced_late_failure_target_and_parent_identity","fresh_sibling_idempotence_zero_replacements","state_A_and_state_B_manifest_replay"],"external_static_instances":ext.get("instance_count",0),"physical_instances":physical,"records":records,"schema":"paper48.adversarial-tests.v1","status":"PASS" if not survivors else "HOLD","survivor_ids":survivors,"survivors":len(survivors)}
def main():
 p=argparse.ArgumentParser(allow_abbrev=False);p.add_argument("--root",type=Path,required=True);p.add_argument("--scratch",type=Path,required=True);p.add_argument("--state",choices=["A","B"],required=True);p.add_argument("--static-digest",required=True);p.add_argument("--commit")
 try:
  a=p.parse_args();o=run(a.root.resolve(strict=True),a.scratch,a.state,a.static_digest,a.commit);sys.stdout.buffer.write(enc(o));return 0 if o["status"]=="PASS" else 2
 except Exception as e:sys.stderr.write(f"ADVERSARIAL_ERROR:{type(e).__name__}\n");return 3
if __name__=="__main__":raise SystemExit(main())
