#!/usr/bin/env python3
"""Mutate disposable trees while an unchanged external auditor judges them."""
from __future__ import annotations
import argparse, hashlib, json, os, shutil, stat, subprocess, sys
from pathlib import Path
from typing import Any
CASES=[("byte_drift","STATIC_TREE_FAILURE"),("mode_drift","STATIC_TREE_FAILURE"),("root_mode_drift","ROOT_MODE_FAILURE"),("extra_empty_directory","STATIC_TREE_FAILURE"),("fifo_node","STATIC_TREE_FAILURE"),("symlink_node","STATIC_TREE_FAILURE"),("file_deletion","STATIC_TREE_FAILURE"),("seal_key_drift","STATIC_SEAL_SHAPE_FAILURE"),("seal_mode_drift","STATIC_SEAL_MODE_FAILURE"),("seal_value_drift","STATIC_SEAL_SMOKE_TYPE_FAILURE"),("seal_forbidden_state_b_full_tree_hash","STATIC_SEAL_SMOKE_SHAPE_FAILURE"),("seal_smoke_commit_drift","STATIC_SEAL_SMOKE_COMMIT_FAILURE"),("seal_stable_domain_drift","STATIC_SEAL_SMOKE_DOMAIN_FAILURE"),("manifest_order_drift","NONCANONICAL_JSON"),("installed_auditor_drift","STATIC_TREE_FAILURE")]
def enc(v:Any)->bytes:return (json.dumps(v,sort_keys=True,indent=2,ensure_ascii=True,separators=(",",": "))+"\n").encode("ascii")
def pairs(seq:list[tuple[str,Any]])->dict[str,Any]:
 out={}
 for k,v in seq:
  if k in out:raise ValueError("duplicate")
  out[k]=v
 return out
def invoke(script:Path,root:Path,cwd:Path,hostile:Path)->tuple[int,dict[str,Any]]:
 env={"PATH":os.environ.get("PATH","/usr/bin:/bin"),"PYTHONPATH":str(hostile),"PYTHONDONTWRITEBYTECODE":"1"}
 p=subprocess.run([sys.executable,"-I","-B",str(script),"--root",str(root)],cwd=cwd,env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False)
 if p.stderr:raise ValueError("auditor stderr")
 obj=json.loads(p.stdout.decode("ascii"),object_pairs_hook=pairs)
 if p.stdout!=enc(obj):raise ValueError("auditor noncanonical")
 return p.returncode,obj
def rebind_seal(clone:Path)->None:
 seal=clone/"PREOUTPUT_STATIC_SEAL.json";manifest=clone/"STATIC_TREE_MANIFEST.json";obj=json.loads(manifest.read_text())
 target=[row for row in obj["rows"] if row["path"]=="PREOUTPUT_STATIC_SEAL.json"]
 if len(target)!=1:raise ValueError("seal manifest row")
 target[0]["mode"]=f"{stat.S_IMODE(os.lstat(seal).st_mode):04o}";target[0]["sha256"]=hashlib.sha256(seal.read_bytes()).hexdigest();manifest.write_bytes(enc(obj))
def main()->None:
 ap=argparse.ArgumentParser(allow_abbrev=False);ap.add_argument("--root",required=True);ap.add_argument("--scratch",required=True);q=ap.parse_args()
 try:
  root=Path(q.root).resolve(strict=True);scratch=Path(q.scratch)
  if scratch.exists() or scratch.is_symlink():raise ValueError("scratch exists")
  scratch.mkdir(parents=True,mode=0o700);cwd=scratch/"hostile_cwd";hostile=scratch/"hostile_modules";cwd.mkdir();hostile.mkdir();(hostile/"json.py").write_text("raise RuntimeError('shadow')\n",encoding="ascii")
  external=root/"external_auditor/frozen_auditor.py";records=[];outside=scratch/"outside_sentinel";outside.write_text("P47_EXTERNAL_SENTINEL\n",encoding="ascii");before=outside.read_bytes()
  for name,code in CASES:
   clone=scratch/("case_"+name);shutil.copytree(root,clone,symlinks=True,ignore=shutil.ignore_patterns("outputs","__pycache__","*.pyc"))
   if name=="byte_drift":
    p=clone/"README.md";p.chmod(0o644);p.write_bytes(p.read_bytes()+b"\n");p.chmod(0o644)
   elif name=="mode_drift":(clone/"README.md").chmod(0o600)
   elif name=="root_mode_drift":clone.chmod(0o700)
   elif name=="extra_empty_directory":(clone/"unexpected_empty").mkdir()
   elif name=="fifo_node":os.mkfifo(clone/"unexpected_fifo",0o600)
   elif name=="symlink_node":(clone/"unexpected_link").symlink_to(outside)
   elif name=="file_deletion":(clone/"README.md").unlink()
   elif name=="seal_key_drift":
    p=clone/"PREOUTPUT_STATIC_SEAL.json";o=json.loads(p.read_text());o["unexpected"]=True;p.write_bytes(enc(o));rebind_seal(clone)
   elif name=="seal_mode_drift":
    (clone/"PREOUTPUT_STATIC_SEAL.json").chmod(0o600);rebind_seal(clone)
   elif name=="seal_value_drift":
    p=clone/"PREOUTPUT_STATIC_SEAL.json";o=json.loads(p.read_text());o["smoke"]["completed"]=1;p.write_bytes(enc(o));rebind_seal(clone)
   elif name=="seal_forbidden_state_b_full_tree_hash":
    p=clone/"PREOUTPUT_STATIC_SEAL.json";o=json.loads(p.read_text());o["smoke"]["state_B_final_tree_sha256"]="0"*64;p.write_bytes(enc(o));rebind_seal(clone)
   elif name=="seal_smoke_commit_drift":
    p=clone/"PREOUTPUT_STATIC_SEAL.json";o=json.loads(p.read_text());o["smoke"]["state_B_smoke_commit"]="0"*40;p.write_bytes(enc(o));rebind_seal(clone)
   elif name=="seal_stable_domain_drift":
    p=clone/"PREOUTPUT_STATIC_SEAL.json";o=json.loads(p.read_text());o["smoke"]["state_B_stable_payload_domain"]="ambiguous_tree_hash";p.write_bytes(enc(o));rebind_seal(clone)
   elif name=="manifest_order_drift":
    p=clone/"STATIC_TREE_MANIFEST.json";o=json.loads(p.read_text());raw=(json.dumps({"schema":o["schema"],"rows":o["rows"],"candidate_id":o["candidate_id"]},sort_keys=False,indent=2,ensure_ascii=True,separators=(",",": "))+"\n").encode("ascii");p.write_bytes(raw)
   else:
    p=clone/"external_auditor/frozen_auditor.py";p.write_bytes(p.read_bytes()+b"# drift\n")
   rc,obj=invoke(external,clone,cwd,hostile)
   expected={"consumer":"F","rejection_code":code,"schema":"paper47-mutation-rejection-v1","status":"REJECT"}
   if rc!=2 or obj!=expected:raise ValueError("external mutation survived")
   records.append({"id":name,"observed_exit":rc,"rejection_code":code,"survivor":False})
  if outside.read_bytes()!=before:raise ValueError("outside sentinel")
  out={"candidate_id":"SD-C49","payload":{"instance_count":len(records),"records":records,"survivors":0},"schema":"paper47-external-auditor-mutations-v1","status":"PASS"};sys.stdout.buffer.write(enc(out))
 except Exception as e:sys.stderr.write(f"EXTERNAL_MUTATION_ERROR:{type(e).__name__}\n");raise SystemExit(3)
if __name__=="__main__":main()
