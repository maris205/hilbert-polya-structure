#!/usr/bin/env python3
"""Apply every frozen mutation to ordinary full artifacts in disposable clones."""
from __future__ import annotations
import argparse,hashlib,json,os,re,shutil,subprocess,sys
from pathlib import Path
from typing import Any

CONSUMER_PATH={"A":"code/evaluator_a/evaluate.py","B":"code/evaluator_b/evaluate.py","G":"code/integration/audit_integrity.py","I":"code/auditors/independence_auditor.py","P":"code/proof_auditor/audit.py","R_INDEPENDENT":"code/route/audit_route_independent.py","R_MAIN":"code/route/validate_route.py","S":"code/auditors/source_auditor.py","T":"code/auditors/type_auditor.py","X":"code/comparator/compare.py"}
def enc(v:Any)->bytes:return (json.dumps(v,sort_keys=True,indent=2,ensure_ascii=True,separators=(",",": "),allow_nan=False)+"\n").encode("ascii")
def load(p):return json.loads(Path(p).read_text(encoding="ascii"))
def strict(a,b):return type(a) is type(b) and a==b
def parent(document,pointer):
 pieces=pointer.strip("/").split("/");node=document
 for piece in pieces[:-1]:node=node[int(piece)] if type(node) is list else node[piece]
 return node,pieces[-1]
def replace(document,pointer,old,new):
 node,key=parent(document,pointer);current=node[int(key)] if type(node) is list else node[key]
 if not strict(current,old):raise ValueError("mutation precondition "+pointer)
 if type(node) is list:node[int(key)]=new
 else:node[key]=new
def env():return {"PATH":os.environ.get("PATH","/usr/bin:/bin"),"PYTHONDONTWRITEBYTECODE":"1","PYTHONHASHSEED":"0","LC_ALL":"C","LANG":"C"}
def call(cmd,cwd,timeout=120):return subprocess.run(cmd,cwd=cwd,env=env(),stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False,timeout=timeout)
def baseline(root,scratch,static):
 a=scratch/"baseline-a.json";an=scratch/"baseline-an.json";b=scratch/"baseline-b.json";bn=scratch/"baseline-bn.json"
 pa=subprocess.Popen([sys.executable,"-I","-B",str(root/CONSUMER_PATH["A"]),"--root",str(root),"--projection",str(a),"--native",str(an)],cwd=scratch,env=env(),stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 pb=subprocess.Popen([sys.executable,"-I","-B",str(root/CONSUMER_PATH["B"]),"--root",str(root),"--projection",str(b),"--native",str(bn)],cwd=scratch,env=env(),stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 ao,ae=pa.communicate(timeout=180);bo,be=pb.communicate(timeout=180)
 if pa.returncode or pb.returncode or ao or bo or ae or be:raise ValueError("baseline lanes")
 route=scratch/"baseline-route.json";q=call([sys.executable,"-I","-B",str(root/"code/route/render_route.py"),"--root",str(root),"--state","A","--static-digest",static],scratch)
 if q.returncode or q.stderr:raise ValueError("baseline route")
 route.write_bytes(q.stdout);return a,b,route
def copy_candidate(root,dest):
 def ignore(_base,names):return {n for n in names if n=="outputs" or n=="__pycache__" or n.endswith((".pyc",".pyo"))}
 shutil.copytree(root,dest,symlinks=True,ignore=ignore)
def apply(clone,row,route_source,outer):
 if row["domain"]=="route":
  document=load(route_source);replace(document,row["target"],row["value_from"],row["value_to"]);path=clone/"mutated-route.json";path.write_bytes(enc(document));return path
 if row["id"]=="M037":
  sentinel=outer/"outside-sentinel";sentinel.mkdir(exist_ok=True);(clone/"results").symlink_to(sentinel,target_is_directory=True);return None
 if row["id"]=="M038":
  (clone/"__pycache__").mkdir();(clone/"__pycache__/host-token.pyc").write_bytes(b"forbidden");return None
 model_path=clone/"contracts/SCIENCE_MODEL.json";document=load(model_path)
 if row["id"] in {"M021","M022"}:
  anchors=document["ownership"]["internal"];key="P26" if row["id"]=="M021" else "P30";expected=anchors.get(key)
  if expected!=row["value_from"]:raise ValueError("ownership precondition")
  del anchors[key]
 else:replace(document,row["target"],row["value_from"],row["value_to"])
 model_path.write_bytes(enc(document));return None
def command(clone,consumer,a,b,route,static,scratch):
 script=clone/CONSUMER_PATH[consumer]
 if consumer=="A":return [sys.executable,"-I","-B",str(script),"--root",str(clone),"--projection",str(scratch/"mut-a.json"),"--native",str(scratch/"mut-an.json")]
 if consumer=="B":return [sys.executable,"-I","-B",str(script),"--root",str(clone),"--projection",str(scratch/"mut-b.json"),"--native",str(scratch/"mut-bn.json")]
 if consumer=="P":return [sys.executable,"-I","-B",str(script),"--root",str(clone),"--a",str(a),"--b",str(b)]
 if consumer=="X":return [sys.executable,"-I","-B",str(script),"--root",str(clone),"--a",str(a),"--b",str(b)]
 if consumer in {"R_MAIN","R_INDEPENDENT"}:return [sys.executable,"-I","-B",str(script),"--root",str(clone),"--route",str(route),"--state","A","--static-digest",static]
 if consumer=="G":return [sys.executable,"-I","-B",str(script),"--root",str(clone),"--preflight"]
 return [sys.executable,"-I","-B",str(script),"--root",str(clone)]
def run(root,scratch):
 scratch.mkdir(parents=True);registry=load(root/"preauthority/MUTATION_REGISTRY.json");static=load(root/"STATIC_TREE_MANIFEST.json")["base_inventory_sha256"];a,b,base_route=baseline(root,scratch,static);records=[];survivors=[];invocations=0
 for row in registry["mutations"]:
  clone=scratch/row["id"]/"candidate";clone.parent.mkdir();copy_candidate(root,clone);mutated_route=apply(clone,row,base_route,clone.parent) or base_route;observed={}
  for consumer in row["consumers"]:
   work=clone.parent/("work-"+consumer.lower());work.mkdir();q=call(command(clone,consumer,a,b,mutated_route,static,work),work,300);invocations+=1
   try:payload=json.loads(q.stdout.decode("ascii"))
   except Exception:payload={}
   code=payload.get("code");ok=q.returncode==2 and not q.stderr and payload=={"code":row["code"],"consumer":consumer,"exit_code":2,"outcome":"REJECT"}
   observed[consumer]={"code":code,"exit":q.returncode};
   if not ok:survivors.append(row["id"]+":"+consumer)
  records.append({"designated_consumers":row["consumers"],"id":row["id"],"observed":observed,"survivor":any(x.startswith(row["id"]+":") for x in survivors)})
  shutil.rmtree(clone.parent)
 if invocations!=68:raise ValueError("invocations")
 return {"candidate_id":"SD-C50","consumer_invocations":invocations,"instance_count":39,"records":records,"registry_sha256":hashlib.sha256((root/"preauthority/MUTATION_REGISTRY.json").read_bytes()).hexdigest(),"schema":"paper48.coordinated-mutations.v1","status":"PASS" if not survivors else "HOLD","survivor_ids":survivors,"survivors":len(survivors)}
def main():
 p=argparse.ArgumentParser(allow_abbrev=False);p.add_argument("--root",type=Path,required=True);p.add_argument("--scratch",type=Path,required=True)
 try:
  a=p.parse_args();o=run(a.root.resolve(strict=True),a.scratch);sys.stdout.buffer.write(enc(o));return 0 if o["status"]=="PASS" else 2
 except Exception as e:sys.stderr.write(f"COORDINATED_ERROR:{type(e).__name__}\n");return 3
if __name__=="__main__":raise SystemExit(main())
