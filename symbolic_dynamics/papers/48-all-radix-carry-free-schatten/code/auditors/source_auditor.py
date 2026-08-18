#!/usr/bin/env python3
"""Source, ownership, and provenance auditor S."""
from __future__ import annotations
import argparse, hashlib, json, os, re, stat, sys
from pathlib import Path
from typing import Any

ATTACKS={
 ("source_type","/object/composite_radix","Kummer_equivalence"):"COMPOSITE_KUMMER_SCOPE",
 ("claim_scope","/claims/complex_trace_zero_free",True):"UNSUPPORTED_COMPLEX_ZERO_FREE",
 ("ownership","/ownership/internal","omitted"):None,
 ("ownership_control","/controls/randomized_digit_mask/credit","positive_novelty"):"RANDOM_MASK_NOVELTY",
 ("ownership","/ownership/finite_tensor_spectrum","novel"):"FINITE_CONTROL_NOVELTY",
 ("ownership","/ownership/priority",True):"PRIORITY_FROM_SEARCH_ABSENCE",
 ("provenance","/provenance/phase2_parent_manifest_sha256","all_zero_sha256"):"PARENT_SEAL_MISMATCH",
 ("source","/sources/Kummer/doi","10.0000/wrong"):"SOURCE_DOI_MISMATCH",
}
PARENT="d035310ac046981abe7a37a033b1354e3d8da3f53f33d631786ed80f40b90181"
P26="749e61a4e99ee55839928046a7114ea62ba0726a041d0e3bf971729f6fbf54ab"
P30="6a09c46e9c04326728cd838deb654e69529fc661cdb616e255fdb10910b5957e"

class Dup(Exception):pass
class OwnedReject(Exception):
 def __init__(self,code):self.code=code
def pairs(x):
 o={}
 for k,v in x:
  if k in o:raise Dup(k)
  o[k]=v
 return o
def enc(x:Any)->bytes:return (json.dumps(x,sort_keys=True,indent=2,ensure_ascii=True,separators=(",",": "),allow_nan=False)+"\n").encode("ascii")
def load(p:Path):
 raw=p.read_bytes();o=json.loads(raw.decode("ascii"),object_pairs_hook=pairs)
 if type(o) is not dict:return (_ for _ in ()).throw(ValueError("object"))
 return o
def emit(consumer:str,code:str|None)->int:
 if code is None:sys.stdout.buffer.write(enc({"consumer":consumer,"exit_code":0,"outcome":"ACCEPT"}));return 0
 sys.stdout.buffer.write(enc({"code":code,"consumer":consumer,"exit_code":2,"outcome":"REJECT"}));return 2
def attack(p:Path)->int:
 x=load(p)
 if set(x)!={"domain","target","value_from","value_to"}:raise ValueError("attack")
 key=(x["domain"],x["target"],x["value_to"])
 code=ATTACKS.get(key)
 if key==("ownership","/ownership/internal","omitted"):
  anchor=x["value_from"]
  code="P26_OWNERSHIP_OMITTED" if anchor=="includes_P26_749e61a4" else "P30_OWNERSHIP_OMITTED" if anchor=="includes_P30_6a09c46e" else None
 return emit("S",code)
def model_code(model):
 if model.get("object",{}).get("composite_radix")!="direct_no_carry_predicate":return "COMPOSITE_KUMMER_SCOPE"
 if model.get("claims",{}).get("complex_trace_zero_free") is not False:return "UNSUPPORTED_COMPLEX_ZERO_FREE"
 anchors=model.get("ownership",{}).get("internal",{})
 if anchors.get("P26")!="includes_P26_749e61a4":return "P26_OWNERSHIP_OMITTED"
 if anchors.get("P30")!="includes_P30_6a09c46e":return "P30_OWNERSHIP_OMITTED"
 if model.get("controls",{}).get("randomized_digit_mask",{}).get("credit")!="zero_novelty_control":return "RANDOM_MASK_NOVELTY"
 if model.get("ownership",{}).get("finite_tensor_spectrum")!="zero_credit":return "FINITE_CONTROL_NOVELTY"
 if model.get("ownership",{}).get("priority") is not False:return "PRIORITY_FROM_SEARCH_ABSENCE"
 if model.get("provenance",{}).get("phase2_parent_manifest_sha256")!=PARENT:return "PARENT_SEAL_MISMATCH"
 if model.get("sources",{}).get("Kummer",{}).get("doi")!="10.1515/crll.1852.44.93":return "SOURCE_DOI_MISMATCH"
 return None
def audit(root:Path)->dict:
 pre=root/"preauthority";manifest=pre/"SHA256SUMS.txt"
 if hashlib.sha256(manifest.read_bytes()).hexdigest()!="f5669e651c4c31ce860bad534d17e64956a8750412f74257d341810424252057":raise ValueError("manifest seal")
 raw=manifest.read_bytes()
 if not raw.endswith(b"\n") or b"\r" in raw:raise ValueError("manifest newline")
 lines=raw.decode("ascii").splitlines();names=[]
 for line in lines:
  m=re.fullmatch(r"([0-9a-f]{64})  ([A-Za-z0-9_.-]+)",line)
  if not m:raise ValueError("manifest syntax")
  h,name=m.groups();names.append(name)
  p=pre/name
  if p.is_symlink() or not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=h:raise ValueError("child hash")
 if len(lines)!=17 or names!=sorted(names) or len(names)!=len(set(names)) or "SHA256SUMS.txt" in names:raise ValueError("self excluding")
 actual=sorted(p.name for p in pre.iterdir())
 if actual!=sorted(names+["SHA256SUMS.txt"]):raise ValueError("preauthority namespace")
 for p in pre.iterdir():
  if stat.S_IMODE(os.lstat(p).st_mode)!=0o444:raise ValueError("frozen mode")
 texts={name:(pre/name).read_text(encoding="utf-8") for name in names if name.endswith((".md",".yaml"))}
 joined="\n".join(texts.values())
 for token in (PARENT,P26,P30,"10.1515/crll.1852.44.93","no complex zero-free claim","zero-credit controls"):
  if token not in joined:raise ValueError("source token")
 if "This is not a priority claim" not in texts["LITERATURE_NOVELTY_AUDIT.md"]:raise ValueError("priority firewall")
 model=load(root/"contracts/SCIENCE_MODEL.json")
 code=model_code(model)
 if code:raise OwnedReject(code)
 if model["provenance"]["phase2_parent_manifest_sha256"]!=PARENT or model["ownership"]["internal"]!={"P26":"includes_P26_749e61a4","P30":"includes_P30_6a09c46e"}:raise ValueError("model provenance")
 if model["sources"]["Kummer"]["doi"]!="10.1515/crll.1852.44.93" or model["ownership"]["priority"] is not False:raise ValueError("model source")
 return {"candidate_id":"SD-C50","consumer":"S","preauthority_child_count":17,"preauthority_manifest_sha256":hashlib.sha256(raw).hexdigest(),"schema":"paper48.source-audit.v1","status":"PASS"}
def main()->int:
 p=argparse.ArgumentParser(allow_abbrev=False);p.add_argument("--root",type=Path);p.add_argument("--attack",type=Path)
 try:
  a=p.parse_args()
  if a.attack is not None:
   if a.root is not None:raise ValueError("arity")
   return attack(a.attack)
  if a.root is None:raise ValueError("arity")
  sys.stdout.buffer.write(enc(audit(a.root.resolve(strict=True))));return 0
 except OwnedReject as e:return emit("S",e.code)
 except Exception as e:sys.stderr.write(f"S_ERROR:{type(e).__name__}\n");return 3
if __name__=="__main__":raise SystemExit(main())
