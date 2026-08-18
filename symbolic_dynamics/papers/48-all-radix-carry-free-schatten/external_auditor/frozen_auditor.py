#!/usr/bin/env python3
"""Frozen external static-tree auditor; imports no production module."""
from __future__ import annotations
import argparse,hashlib,json,os,stat,sys
from pathlib import Path
from typing import Any
class Dup(Exception):pass
class Reject(Exception):
 def __init__(self,code):self.code=code
def pairs(seq):
 o={}
 for k,v in seq:
  if k in o:raise Dup(k)
  o[k]=v
 return o
def enc(v:Any)->bytes:return (json.dumps(v,sort_keys=True,indent=2,ensure_ascii=True,separators=(",",": "),allow_nan=False)+"\n").encode("ascii")
def load(p):
 raw=Path(p).read_bytes();o=json.loads(raw.decode("ascii"),object_pairs_hook=pairs)
 if type(o) is not dict or raw!=enc(o):raise Reject("NONCANONICAL_JSON")
 return o
def inventory(root,base):
 answer=[]
 for p in root.rglob("*"):
  rel=p.relative_to(root).as_posix()
  if rel=="outputs" or rel.startswith("outputs/") or rel=="STATIC_TREE_MANIFEST.json" or (base and rel=="PREOUTPUT_STATIC_SEAL.json") or "__pycache__" in p.parts or p.suffix==".pyc":continue
  s=os.lstat(p);mode=f"{stat.S_IMODE(s.st_mode):04o}"
  if stat.S_ISLNK(s.st_mode):raise Reject("STATIC_TREE_FAILURE")
  if stat.S_ISDIR(s.st_mode):answer.append({"kind":"directory","mode":mode,"path":rel})
  elif stat.S_ISREG(s.st_mode):answer.append({"kind":"regular","mode":mode,"path":rel,"sha256":hashlib.sha256(p.read_bytes()).hexdigest()})
  else:raise Reject("STATIC_TREE_FAILURE")
 return sorted(answer,key=lambda x:x["path"])
def audit(root):
 if stat.S_IMODE(os.lstat(root).st_mode)!=0o755:raise Reject("ROOT_MODE_FAILURE")
 manifest=load(root/"STATIC_TREE_MANIFEST.json");seal=load(root/"PREOUTPUT_STATIC_SEAL.json")
 if stat.S_IMODE(os.lstat(root/"PREOUTPUT_STATIC_SEAL.json").st_mode)!=0o644:raise Reject("STATIC_SEAL_MODE_FAILURE")
 if set(seal)!={"candidate_id","contract_counts","preauthority_manifest_sha256","schema","smoke","static_inventory_sha256","status","zero_state"}:raise Reject("STATIC_SEAL_SHAPE_FAILURE")
 if seal["candidate_id"]!="SD-C50" or seal["schema"]!="paper48.preoutput-static-seal.v1" or seal["status"]!="HOLD_FOR_INDEPENDENT_AUDIT":raise Reject("STATIC_SEAL_VALUE_FAILURE")
 if seal["preauthority_manifest_sha256"]!="f5669e651c4c31ce860bad534d17e64956a8750412f74257d341810424252057":raise Reject("STATIC_SEAL_VALUE_FAILURE")
 base=inventory(root,True);base_hash=hashlib.sha256(enc(base)).hexdigest()
 if manifest.get("base_inventory_sha256")!=base_hash:raise Reject("STATIC_TREE_FAILURE")
 if seal["static_inventory_sha256"]!=manifest.get("base_inventory_sha256"):raise Reject("STATIC_SEAL_VALUE_FAILURE")
 if manifest!={"base_inventory_sha256":base_hash,"candidate_id":"SD-C50","output_root_mode":"0755","root_mode":"0755","rows":inventory(root,False),"schema":"paper48.static-tree-manifest.v1"}:raise Reject("STATIC_TREE_FAILURE")
 if seal["zero_state"]!={"cache_files":0,"candidate_output_files":0,"candidate_outputs_directory_present":False}:raise Reject("STATIC_SEAL_VALUE_FAILURE")
 return {"base_inventory_sha256":base_hash,"candidate_id":"SD-C50","outer_inventory_rows":len(manifest["rows"]),"schema":"paper48.frozen-static-audit.v1","status":"PASS"}
def main():
 p=argparse.ArgumentParser(allow_abbrev=False);p.add_argument("--root",type=Path,required=True)
 try:sys.stdout.buffer.write(enc(audit(p.parse_args().root.resolve(strict=True))));return 0
 except Reject as e:sys.stdout.buffer.write(enc({"code":e.code,"consumer":"EXTERNAL","exit_code":2,"outcome":"REJECT"}));return 2
 except Exception as e:sys.stderr.write(f"EXTERNAL_ERROR:{type(e).__name__}\n");return 3
if __name__=="__main__":raise SystemExit(main())
