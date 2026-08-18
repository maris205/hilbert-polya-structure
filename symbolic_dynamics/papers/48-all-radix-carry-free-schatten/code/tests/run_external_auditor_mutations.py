#!/usr/bin/env python3
"""Physically mutate disposable static trees against the frozen auditor."""
from __future__ import annotations
import argparse,json,os,shutil,stat,subprocess,sys
from pathlib import Path
from typing import Any
def enc(v:Any)->bytes:return (json.dumps(v,sort_keys=True,indent=2,ensure_ascii=True,separators=(",",": "))+"\n").encode("ascii")
CASES=[("byte_drift","STATIC_TREE_FAILURE"),("mode_drift","STATIC_TREE_FAILURE"),("root_mode_drift","ROOT_MODE_FAILURE"),("extra_empty_directory","STATIC_TREE_FAILURE"),("fifo_node","STATIC_TREE_FAILURE"),("symlink_node","STATIC_TREE_FAILURE"),("file_deletion","STATIC_TREE_FAILURE"),("file_rename","STATIC_TREE_FAILURE"),("seal_key_drift","STATIC_SEAL_SHAPE_FAILURE"),("seal_mode_drift","STATIC_SEAL_MODE_FAILURE"),("seal_value_drift","STATIC_SEAL_VALUE_FAILURE"),("manifest_order_drift","STATIC_TREE_FAILURE"),("installed_auditor_drift","STATIC_TREE_FAILURE")]
def mutate(tree:Path,name:str):
 if name=="byte_drift":(tree/"README.md").write_bytes((tree/"README.md").read_bytes()+b"x")
 elif name=="mode_drift":(tree/"README.md").chmod(0o600)
 elif name=="root_mode_drift":tree.chmod(0o700)
 elif name=="extra_empty_directory":(tree/"unexpected-empty").mkdir()
 elif name=="fifo_node":os.mkfifo(tree/"unexpected.fifo")
 elif name=="symlink_node":(tree/"unexpected-link").symlink_to("README.md")
 elif name=="file_deletion":(tree/"README.md").unlink()
 elif name=="file_rename":(tree/"README.md").rename(tree/"RENAMED_README.md")
 elif name=="seal_key_drift":
  p=tree/"PREOUTPUT_STATIC_SEAL.json";o=json.loads(p.read_text());o["unexpected"]=False;p.write_bytes(enc(o))
 elif name=="seal_mode_drift":(tree/"PREOUTPUT_STATIC_SEAL.json").chmod(0o600)
 elif name=="seal_value_drift":
  p=tree/"PREOUTPUT_STATIC_SEAL.json";o=json.loads(p.read_text());o["status"]="CLEAN";p.write_bytes(enc(o))
 elif name=="manifest_order_drift":
  p=tree/"STATIC_TREE_MANIFEST.json";o=json.loads(p.read_text());o["rows"]=list(reversed(o["rows"]));p.write_bytes(enc(o))
 elif name=="installed_auditor_drift":(tree/"external_auditor/frozen_auditor.py").write_bytes((tree/"external_auditor/frozen_auditor.py").read_bytes()+b"\n")
def run(root:Path,scratch:Path):
 scratch.mkdir(parents=True);records=[];survivors=[]
 for index,(name,expected) in enumerate(CASES):
  clone=scratch/f"case-{index:02d}";shutil.copytree(root,clone,symlinks=True,ignore=shutil.ignore_patterns("outputs","__pycache__","*.pyc"));mutate(clone,name)
  q=subprocess.run([sys.executable,"-I","-B",str(clone/"external_auditor/frozen_auditor.py"),"--root",str(clone)],cwd=scratch,env={"PATH":os.environ.get("PATH","/usr/bin:/bin"),"PYTHONDONTWRITEBYTECODE":"1"},stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False,timeout=20)
  try:o=json.loads(q.stdout.decode("ascii"))
  except Exception:o={}
  ok=q.returncode==2 and not q.stderr and o=={"code":expected,"consumer":"EXTERNAL","exit_code":2,"outcome":"REJECT"}
  if not ok:survivors.append(name)
  records.append({"id":name,"observed_code":o.get("code"),"observed_exit":q.returncode,"survivor":not ok})
  clone.chmod(0o755);shutil.rmtree(clone)
 return {"candidate_id":"SD-C50","instance_count":len(CASES),"records":records,"schema":"paper48.external-auditor-mutations.v1","status":"PASS" if not survivors else "HOLD","survivor_ids":survivors,"survivors":len(survivors)}
def main():
 p=argparse.ArgumentParser(allow_abbrev=False);p.add_argument("--root",type=Path,required=True);p.add_argument("--scratch",type=Path,required=True)
 try:
  a=p.parse_args();o=run(a.root.resolve(strict=True),a.scratch);sys.stdout.buffer.write(enc(o));return 0 if o["status"]=="PASS" else 2
 except Exception as e:sys.stderr.write(f"EXTERNAL_MUTATION_ERROR:{type(e).__name__}\n");return 3
if __name__=="__main__":raise SystemExit(main())
