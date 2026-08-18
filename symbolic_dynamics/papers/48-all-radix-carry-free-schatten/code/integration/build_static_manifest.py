#!/usr/bin/env python3
"""Generate the acyclic outer static inventory."""
from __future__ import annotations
import argparse,hashlib,json,os,stat,sys
from pathlib import Path
from typing import Any
def enc(v:Any)->bytes:return (json.dumps(v,sort_keys=True,indent=2,ensure_ascii=True,separators=(",",": "))+"\n").encode("ascii")
def rows(root:Path,base:bool):
 out=[]
 for p in root.rglob("*"):
  rel=p.relative_to(root).as_posix()
  if rel=="outputs" or rel.startswith("outputs/") or rel=="STATIC_TREE_MANIFEST.json" or (base and rel=="PREOUTPUT_STATIC_SEAL.json") or "__pycache__" in p.parts or p.suffix==".pyc":continue
  s=os.lstat(p);mode=f"{stat.S_IMODE(s.st_mode):04o}"
  if stat.S_ISLNK(s.st_mode):raise ValueError("symlink")
  if stat.S_ISDIR(s.st_mode):out.append({"kind":"directory","mode":mode,"path":rel})
  elif stat.S_ISREG(s.st_mode):out.append({"kind":"regular","mode":mode,"path":rel,"sha256":hashlib.sha256(p.read_bytes()).hexdigest()})
  else:raise ValueError("nonregular")
 return sorted(out,key=lambda x:x["path"])
def main():
 p=argparse.ArgumentParser(allow_abbrev=False);p.add_argument("--root",type=Path,required=True)
 try:
  a=p.parse_args();root=a.root.resolve(strict=True);base=rows(root,True);outer=rows(root,False);obj={"base_inventory_sha256":hashlib.sha256(enc(base)).hexdigest(),"candidate_id":"SD-C50","output_root_mode":"0755","root_mode":f"{stat.S_IMODE(os.lstat(root).st_mode):04o}","rows":outer,"schema":"paper48.static-tree-manifest.v1"};(root/"STATIC_TREE_MANIFEST.json").write_bytes(enc(obj));(root/"STATIC_TREE_MANIFEST.json").chmod(0o644);sys.stdout.buffer.write(enc({"base_inventory_sha256":obj["base_inventory_sha256"],"manifest_sha256":hashlib.sha256(enc(obj)).hexdigest(),"outer_row_count":len(outer),"status":"PASS"}));return 0
 except Exception as e:sys.stderr.write(f"STATIC_MANIFEST_ERROR:{type(e).__name__}\n");return 3
if __name__=="__main__":raise SystemExit(main())
