#!/usr/bin/env python3
"""Freeze the self-excluding static Paper-47 inventory."""
from __future__ import annotations
import argparse,hashlib,json,os,stat,sys
from pathlib import Path
from typing import Any
def enc(v:Any)->bytes:return (json.dumps(v,sort_keys=True,indent=2,ensure_ascii=True,separators=(",",": "))+"\n").encode("ascii")
def rows(root:Path,base:bool)->list[dict[str,Any]]:
 out=[]
 for p in root.rglob("*"):
  rel=p.relative_to(root).as_posix()
  if rel=="outputs" or rel.startswith("outputs/") or rel=="STATIC_TREE_MANIFEST.json" or (base and rel=="PREOUTPUT_STATIC_SEAL.json") or p.name=="__pycache__" or p.suffix==".pyc":continue
  s=os.lstat(p);mode=f"{stat.S_IMODE(s.st_mode):04o}"
  if stat.S_ISLNK(s.st_mode):raise ValueError("symlink")
  if stat.S_ISDIR(s.st_mode):out.append({"kind":"directory","mode":mode,"path":rel})
  elif stat.S_ISREG(s.st_mode):out.append({"kind":"regular","mode":mode,"path":rel,"sha256":hashlib.sha256(p.read_bytes()).hexdigest()})
  else:raise ValueError("nonregular")
 return sorted(out,key=lambda x:x["path"])
def main()->None:
 p=argparse.ArgumentParser(allow_abbrev=False);p.add_argument("--root",required=True);a=p.parse_args()
 try:
  r=Path(a.root).resolve(strict=True);base_rows=rows(r,True);outer_rows=rows(r,False)
  data={"base_inventory_sha256":hashlib.sha256(enc(base_rows)).hexdigest(),"candidate_id":"SD-C49",
        "output_root_mode":"0755","root_mode":f"{stat.S_IMODE(os.lstat(r).st_mode):04o}",
        "rows":outer_rows,"schema":"paper47-static-tree-manifest-v2"}
  (r/"STATIC_TREE_MANIFEST.json").write_bytes(enc(data));(r/"STATIC_TREE_MANIFEST.json").chmod(0o644)
  sys.stdout.buffer.write(enc({"base_inventory_sha256":data["base_inventory_sha256"],"manifest_sha256":hashlib.sha256(enc(data)).hexdigest(),"outer_row_count":len(outer_rows),"status":"PASS"}))
 except Exception as e:sys.stderr.write(f"STATIC_MANIFEST_ERROR:{type(e).__name__}\n");raise SystemExit(3)
if __name__=="__main__":main()
