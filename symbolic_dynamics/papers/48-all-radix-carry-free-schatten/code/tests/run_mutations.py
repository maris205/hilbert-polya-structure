#!/usr/bin/env python3
"""Replay all 39 code-free semantic attacks against all ten consumers."""
from __future__ import annotations
import argparse,hashlib,json,os,subprocess,sys,tempfile
from pathlib import Path
from typing import Any

CONSUMERS={
 "A":"code/evaluator_a/evaluate.py","B":"code/evaluator_b/evaluate.py",
 "G":"code/integration/audit_integrity.py","I":"code/auditors/independence_auditor.py",
 "P":"code/proof_auditor/audit.py","R_INDEPENDENT":"code/route/audit_route_independent.py",
 "R_MAIN":"code/route/validate_route.py","S":"code/auditors/source_auditor.py",
 "T":"code/auditors/type_auditor.py","X":"code/comparator/compare.py"}
class Dup(Exception):pass
def pairs(seq):
 o={}
 for k,v in seq:
  if k in o:raise Dup(k)
  o[k]=v
 return o
def enc(v:Any)->bytes:return (json.dumps(v,sort_keys=True,indent=2,ensure_ascii=True,separators=(",",": "),allow_nan=False)+"\n").encode("ascii")
def load(p):
 raw=Path(p).read_bytes();o=json.loads(raw.decode("ascii"),object_pairs_hook=pairs)
 if type(o) is not dict:raise ValueError("object")
 return o
def invoke(root:Path,consumer:str,envelope:Path,cwd:Path):
 env={"PATH":os.environ.get("PATH","/usr/bin:/bin"),"PYTHONPATH":str(cwd/"hostile_modules"),"PYTHONDONTWRITEBYTECODE":"1","PYTHONHASHSEED":"0","LC_ALL":"C","LANG":"C"}
 q=subprocess.run([sys.executable,"-I","-B",str(root/CONSUMERS[consumer]),"--attack",str(envelope)],cwd=cwd,env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=20,check=False)
 if q.stderr:return {"exit":q.returncode,"malformed":"stderr"}
 try:o=json.loads(q.stdout.decode("ascii"),object_pairs_hook=pairs)
 except Exception:return {"exit":q.returncode,"malformed":"json"}
 return {"exit":q.returncode,"payload":o}
def run(root:Path,scratch:Path):
 registry_path=root/"preauthority/MUTATION_REGISTRY.json";registry=load(registry_path)
 if registry.get("schema_version")!="paper48.mutation-registry.v1" or len(registry.get("mutations",[]))!=39:raise ValueError("registry")
 scratch.mkdir(parents=True);(scratch/"hostile_modules").mkdir();(scratch/"hostile_modules/json.py").write_text("raise RuntimeError('shadow')\n",encoding="ascii")
 records=[];survivors=[];designated_total=0;nondesignated_total=0
 order=list(CONSUMERS)
 for index,row in enumerate(registry["mutations"]):
  envelope={key:row[key] for key in ("domain","target","value_from","value_to")}
  path=scratch/f"attack-{index+1:03d}.json";path.write_bytes(enc(envelope))
  observed={};designated=set(row["consumers"])
  for consumer in order:
   result=invoke(root,consumer,path,scratch);observed[consumer]=result
   if consumer in designated:
    designated_total+=1;payload=result.get("payload")
    ok=(result.get("exit")==2 and type(payload) is dict and payload=={"code":row["code"],"consumer":consumer,"exit_code":2,"outcome":"REJECT"})
   else:
    nondesignated_total+=1;payload=result.get("payload")
    ok=(result.get("exit")==0 and type(payload) is dict and payload=={"consumer":consumer,"exit_code":0,"outcome":"ACCEPT"})
   if not ok:survivors.append(f"{row['id']}:{consumer}")
  records.append({"code":row["code"],"designated_consumers":row["consumers"],"id":row["id"],"nondesignated_accept_count":len(order)-len(designated),"observed":observed,"survivor":any(x.startswith(row["id"]+":") for x in survivors)})
 if designated_total!=68 or nondesignated_total!=322:raise ValueError("invocation census")
 return {"all_consumer_invocations":designated_total+nondesignated_total,"candidate_id":"SD-C50","designated_consumer_invocations":designated_total,"mutation_instances":39,"nondesignated_acceptances":nondesignated_total,"records":records,"registry_sha256":hashlib.sha256(registry_path.read_bytes()).hexdigest(),"schema":"paper48.mutation-outcomes.v1","status":"PASS" if not survivors else "HOLD","survivor_ids":survivors,"survivors":len(survivors)}
def main():
 p=argparse.ArgumentParser(allow_abbrev=False);p.add_argument("--root",type=Path,required=True);p.add_argument("--scratch",type=Path,required=True)
 try:
  a=p.parse_args();o=run(a.root.resolve(strict=True),a.scratch);sys.stdout.buffer.write(enc(o));return 0 if o["status"]=="PASS" else 2
 except Exception as e:sys.stderr.write(f"MUTATION_ERROR:{type(e).__name__}\n");return 3
if __name__=="__main__":raise SystemExit(main())
