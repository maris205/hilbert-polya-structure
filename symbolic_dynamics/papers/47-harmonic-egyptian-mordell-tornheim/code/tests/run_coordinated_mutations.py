#!/usr/bin/env python3
"""Twenty-one full-state coordinated attacks judged by unchanged FINAL replay."""
from __future__ import annotations
import argparse,hashlib,json,os,shutil,stat,subprocess,sys
from pathlib import Path
from typing import Any
def enc(v:Any)->bytes:return (json.dumps(v,sort_keys=True,indent=2,ensure_ascii=True,separators=(",",": "))+"\n").encode("ascii")
def load(path:Path)->dict[str,Any]:
 raw=path.read_bytes();obj=json.loads(raw.decode("ascii"))
 if type(obj) is not dict or raw!=enc(obj):raise ValueError("canonical")
 return obj
def write(path:Path,obj:dict[str,Any])->None:path.write_bytes(enc(obj));path.chmod(0o644)
def mutate(obj:Any,path:str,value:Any,delete:bool=False)->None:
 bits=path.split("/")[1:];cursor=obj
 for bit in bits[:-1]:cursor=cursor[int(bit)] if type(cursor) is list else cursor[bit]
 key=bits[-1]
 if delete:
  if type(cursor) is list:del cursor[int(key)]
  else:del cursor[key]
 elif type(cursor) is list:cursor[int(key)]=value
 else:cursor[key]=value
def rows(root:Path,exclude:set[str]|None=None)->list[dict[str,Any]]:
 ex=exclude or set();answer=[]
 for path in root.rglob("*"):
  rel=path.relative_to(root).as_posix()
  if rel in ex:continue
  meta=os.lstat(path);mode=f"{stat.S_IMODE(meta.st_mode):04o}"
  if stat.S_ISDIR(meta.st_mode):answer.append({"kind":"directory","mode":mode,"path":rel})
  elif stat.S_ISREG(meta.st_mode):answer.append({"kind":"regular","mode":mode,"path":rel,"sha256":hashlib.sha256(path.read_bytes()).hexdigest()})
  elif stat.S_ISLNK(meta.st_mode):answer.append({"kind":"symlink","mode":mode,"path":rel})
  else:answer.append({"kind":"other","mode":mode,"path":rel})
 return sorted(answer,key=lambda x:x["path"])
def rebuild_ledger(output:Path,state:str)->None:
 rr=rows(output,{"RESULT_LEDGER.json","audits/integrity_audit.json","PAPER_MANIFEST.sha256"})
 write(output/"RESULT_LEDGER.json",{"candidate_id":"SD-C49","payload":{"entry_count":len(rr),"rows":rr,"state":state},"schema":"paper47-result-ledger-v1","status":"PASS"})
def rebuild_certificate(output:Path,state:str)->None:
 route=load(output/"audits/route_primary.json");pre=rows(output,{"audits/integrity_audit.json","PAPER_MANIFEST.sha256"})
 cert={"candidate_id":"SD-C49","payload":{"expected_paper_manifest":state=="B","ledger_sha256":hashlib.sha256((output/"RESULT_LEDGER.json").read_bytes()).hexdigest(),"pre_certificate_tree_sha256":hashlib.sha256(enc(pre)).hexdigest(),"route_sha256":route["payload"]["route_sha256"],"state":state},"schema":"paper47-integrity-audit-v1","status":"PASS"}
 write(output/"audits/integrity_audit.json",cert)
def paper_rows(root:Path,output:Path)->list[dict[str,Any]]:
 answer=[]
 for path in root.rglob("*"):
  rel=path.relative_to(root).as_posix()
  if rel=="outputs" or rel.startswith("outputs/") or rel=="PREOUTPUT_STATIC_SEAL.json":continue
  meta=os.lstat(path);mode=f"{stat.S_IMODE(meta.st_mode):04o}"
  if stat.S_ISDIR(meta.st_mode):answer.append({"kind":"directory","mode":mode,"path":rel})
  elif stat.S_ISREG(meta.st_mode):answer.append({"kind":"regular","mode":mode,"path":rel,"sha256":hashlib.sha256(path.read_bytes()).hexdigest()})
  else:raise ValueError("paper kind")
 for path in output.rglob("*"):
  rel=path.relative_to(output).as_posix()
  if rel=="PAPER_MANIFEST.sha256":continue
  meta=os.lstat(path);mode=f"{stat.S_IMODE(meta.st_mode):04o}";name="outputs/"+rel
  if stat.S_ISDIR(meta.st_mode):answer.append({"kind":"directory","mode":mode,"path":name})
  elif stat.S_ISREG(meta.st_mode):answer.append({"kind":"regular","mode":mode,"path":name,"sha256":hashlib.sha256(path.read_bytes()).hexdigest()})
  else:raise ValueError("paper output kind")
 return sorted(answer,key=lambda x:x["path"])
def rebuild_paper(root:Path,output:Path,state:str)->None:
 if state=="B":write(output/"PAPER_MANIFEST.sha256",{"exclude":["PREOUTPUT_STATIC_SEAL.json","outputs/PAPER_MANIFEST.sha256"],"rows":paper_rows(root,output),"schema":"paper47-state-b-paper-manifest-v1"})
def rerender_report(root:Path,output:Path,cwd:Path)->None:
 result=subprocess.run([sys.executable,"-I","-B",str(root/"code/report/reconstruct_report.py"),"--output-root",str(output)],cwd=cwd,env={"PATH":os.environ.get("PATH","/usr/bin:/bin"),"PYTHONDONTWRITEBYTECODE":"1","PYTHONPATH":str(cwd/"hostile")},stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False,timeout=120)
 if result.returncode or result.stderr:raise ValueError("attack report render")
 (output/"reports/EXPERIMENT_REPORT.md").write_bytes(result.stdout);(output/"reports/EXPERIMENT_REPORT.md").chmod(0o644)
def forge_chain(root:Path,output:Path,state:str,cwd:Path,report:bool=True)->None:
 if report:rerender_report(root,output,cwd)
 rebuild_ledger(output,state);rebuild_certificate(output,state);rebuild_paper(root,output,state)
def final_rejects(root:Path,output:Path,state:str,commit:str|None,cwd:Path,supplied_commit:str|None=None,force_commit:bool=False)->None:
 selected=supplied_commit if force_commit else commit
 args=["--root",str(root),"--output-root",str(output),"--state",state,"--phase","FINAL"]+(["--commit",str(selected)] if state=="B" or force_commit else [])
 result=subprocess.run([sys.executable,"-I","-B",str(root/"code/integration/audit_integrity.py"),*args],cwd=cwd,env={"PATH":os.environ.get("PATH","/usr/bin:/bin"),"PYTHONDONTWRITEBYTECODE":"1","PYTHONPATH":str(cwd/"hostile")},stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False,timeout=120)
 if result.returncode!=3 or result.stdout or not result.stderr.startswith(b"INTEGRITY_ERROR:"):raise ValueError("coordinated survivor")
def main()->None:
 p=argparse.ArgumentParser(allow_abbrev=False);p.add_argument("--root",required=True);p.add_argument("--output-root",required=True);p.add_argument("--scratch",required=True);p.add_argument("--state",required=True,choices=["A","B"]);p.add_argument("--commit");a=p.parse_args()
 try:
  root=Path(a.root).resolve(strict=True);baseline=Path(a.output_root).resolve(strict=True);scratch=Path(a.scratch)
  if scratch.exists() or scratch.is_symlink():raise ValueError("scratch")
  scratch.mkdir(parents=True,mode=0o700);cwd=scratch/"cwd";cwd.mkdir();outside=scratch/"outside";outside.write_text("P47_COORDINATED_SENTINEL\n",encoding="ascii");sentinel=outside.read_bytes();records=[]
  for index in range(1,22):
   case=scratch/f"C{index:02d}";shutil.copytree(baseline,case,symlinks=True)
   if index==1:
    q=case/"results/evaluator_d.json";o=load(q);mutate(o,"/payload/cutoffs/0/N",True);write(q,o);x=load(case/"results/exact_comparison.json");x["payload"]["direct_sha256"]=hashlib.sha256(q.read_bytes()).hexdigest();write(case/"results/exact_comparison.json",x);aa=load(case/"audits/proof_result_audit.json");aa["payload"]["result_hashes"]["direct"]=hashlib.sha256(q.read_bytes()).hexdigest();aa["payload"]["result_hashes"]["comparison"]=hashlib.sha256((case/"results/exact_comparison.json").read_bytes()).hexdigest();write(case/"audits/proof_result_audit.json",aa);forge_chain(root,case,a.state,cwd)
   elif index==2:
    q=case/"results/evaluator_p.json";o=load(q);mutate(o,"/payload/trace_powers/0/method","coordinated_method");write(q,o);forge_chain(root,case,a.state,cwd)
   elif index==3:
    q=case/"results/exact_comparison.json";o=load(q);mutate(o,"/payload/direct_sha256","0"*64);write(q,o);forge_chain(root,case,a.state,cwd)
   elif index==4:
    q=case/"audits/proof_result_audit.json";o=load(q);mutate(o,"/payload/finite_results_role","FINITE_RESULTS_PROVE_ENDPOINTS");write(q,o);forge_chain(root,case,a.state,cwd)
   elif index==5:
    q=case/"tests/mutation_results.json";o=load(q);mutate(o,"/payload/records/0/observed/D/exit",True);write(q,o);forge_chain(root,case,a.state,cwd)
   elif index==6:
    q=case/"tests/expanded_mutation_results.json";o=load(q);mutate(o,"/payload/records/0/consumers/A/exit",True);write(q,o);forge_chain(root,case,a.state,cwd)
   elif index==7:
    q=case/"evaluations/route_a/SD-C49/2026-08-18.json";o=load(q);mutate(o,"/source_lock/clock","coordinated_clock");write(q,o);digest=hashlib.sha256(q.read_bytes()).hexdigest()
    for name in ("route_primary.json","route_independent.json"):
     z=case/"audits"/name;v=load(z);v["payload"]["route_sha256"]=digest;write(z,v)
    forge_chain(root,case,a.state,cwd)
   elif index==8:
    (case/"reports/EXPERIMENT_REPORT.md").write_bytes((case/"reports/EXPERIMENT_REPORT.md").read_bytes()+b"tamper\n");forge_chain(root,case,a.state,cwd,report=False)
   elif index==9:
    forge_chain(root,case,a.state,cwd);q=case/"RESULT_LEDGER.json";o=load(q);o["payload"]["rows"][0]["path"]="../outside";write(q,o);rebuild_certificate(case,a.state);rebuild_paper(root,case,a.state)
   elif index==10:
    forge_chain(root,case,a.state,cwd);q=case/"audits/integrity_audit.json";o=load(q);o["payload"]["state"]=True;write(q,o);rebuild_paper(root,case,a.state)
   elif index==11:
    (case/"results/evaluator_d.json").unlink();forge_chain(root,case,a.state,cwd,report=False)
   elif index==12:
    (case/"results/evaluator_d.json").rename(case/"results/evaluator_direct.json");forge_chain(root,case,a.state,cwd,report=False)
   elif index==13:
    (case/"extra.json").write_bytes(b"{}\n");forge_chain(root,case,a.state,cwd)
   elif index==14:
    q=case/"results/evaluator_d.json";q.unlink();q.symlink_to(outside);rebuild_ledger(case,a.state);rebuild_certificate(case,a.state)
   elif index==15:
    case.chmod(0o700);forge_chain(root,case,a.state,cwd)
   elif index==16:
    if a.state=="B":
     q=case/"PAPER_MANIFEST.sha256";o=load(q);o["rows"][0]["mode"]="0000";write(q,o)
    else:(case/"audits/integrity_audit.json").chmod(0o600)
   elif index==17:
    pass
   elif index==18:
    if a.state=="B":
     q=case/"PAPER_MANIFEST.sha256";o=load(q);matches=[row for row in o["rows"] if row["path"]=="STATIC_TREE_MANIFEST.json"]
     if len(matches)!=1:raise ValueError("outer manifest row")
     matches[0]["sha256"]="0"*64;write(q,o)
    else:
     q=case/"audits/frozen_static_audit.json";o=load(q);o["payload"]["static_inventory_sha256"]="0"*64;write(q,o);forge_chain(root,case,a.state,cwd)
   else:
    q=case/"evaluations/route_a/SD-C49/2026-08-18.json";o=load(q);o["authority_integration"]["status"]={19:"DONE",20:True,21:1}[index];write(q,o);digest=hashlib.sha256(q.read_bytes()).hexdigest()
    for name in ("route_primary.json","route_independent.json"):
     z=case/"audits"/name;v=load(z);v["payload"]["route_sha256"]=digest;write(z,v)
    forge_chain(root,case,a.state,cwd)
   if index==17:final_rejects(root,case,a.state,a.commit,cwd,"2"*40,True)
   else:final_rejects(root,case,a.state,a.commit,cwd)
   records.append({"id":f"C{index:02d}","state":a.state,"survivor":False})
  if outside.read_bytes()!=sentinel:raise ValueError("outside sentinel")
  out={"candidate_id":"SD-C49","payload":{"instance_count":21,"records":records,"state":a.state,"survivors":0},"schema":"paper47-coordinated-mutation-results-v1","status":"PASS"};sys.stdout.buffer.write(enc(out))
 except Exception as e:sys.stderr.write(f"COORDINATED_MUTATION_ERROR:{type(e).__name__}\n");raise SystemExit(3)
if __name__=="__main__":main()
