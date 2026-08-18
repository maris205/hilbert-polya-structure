#!/usr/bin/env python3
"""Auditor G: exact namespace, manifest, state, and transaction contract."""
from __future__ import annotations
import argparse,hashlib,json,os,re,stat,sys
from pathlib import Path,PurePosixPath
from typing import Any

FILES=["EXPERIMENT_REPORT.md","evaluations/independent_evaluation.json","evaluations/main_evaluation.json","results/SHA256SUMS.txt","results/adversarial_tests.json","results/comparison.json","results/evaluator_a_native.json","results/evaluator_a_projection.json","results/evaluator_b_native.json","results/evaluator_b_projection.json","results/integrity_audit.json","results/mutation_outcomes.json","results/proof_audit.json"]
DIRS=["evaluations","results"]
ATTACKS={
 ("provenance","/provenance/phase2_parent_manifest_sha256","all_zero_sha256"):"PARENT_SEAL_MISMATCH",
 ("integrity","/outputs/0/path","/outside/example.json"):"UNSAFE_ABSOLUTE_PATH",
 ("integrity","/outputs/0/path","../outside.json"):"UNSAFE_PARENT_PATH",
 ("integrity","/filesystem/results","symlink_to_external_sentinel"):"SYMLINK_COMPONENT",
 ("integrity","/filesystem/extra","cache_aux_or_host_token_file"):"HYGIENE_FORBIDDEN_ARTIFACT",
 ("transaction","/transaction/late_failure",True):"FORCED_LATE_PREINSTALL_FAILURE",
}
HOST=[b"/root/",b"/home/",b"/tmp/",b"\\root\\",b"\\home\\",b"\\tmp\\"]
class Dup(Exception):pass
class GReject(Exception):
 def __init__(self,code):self.code=code
def pairs(seq):
 o={}
 for k,v in seq:
  if k in o:raise Dup(k)
  o[k]=v
 return o
def enc(v:Any)->bytes:return (json.dumps(v,sort_keys=True,indent=2,ensure_ascii=True,separators=(",",": "),allow_nan=False)+"\n").encode("ascii")
def load(p:Path):
 raw=p.read_bytes();o=json.loads(raw.decode("ascii"),object_pairs_hook=pairs)
 if type(o) is not dict or raw!=enc(o):raise ValueError("canonical")
 return o
def h(raw:bytes)->str:return hashlib.sha256(raw).hexdigest()
def emit(code=None):
 o={"code":code,"consumer":"G","exit_code":2,"outcome":"REJECT"} if code else {"consumer":"G","exit_code":0,"outcome":"ACCEPT"};sys.stdout.buffer.write(enc(o));return o["exit_code"]
def attack(p):
 o=load(p)
 if set(o) not in ({"domain","target","value_to"},{"domain","target","value_from","value_to"}):raise ValueError("attack")
 return emit(ATTACKS.get((o["domain"],o["target"],o["value_to"])))
def safe_rel(text:str)->bool:
 if type(text) is not str or not text or "\\" in text:return False
 p=PurePosixPath(text);return not p.is_absolute() and all(x not in ("",".","..") for x in p.parts)
def rows(root:Path,exclude:set[str]|None=None):
 ex=exclude or set();out=[]
 for p in root.rglob("*"):
  rel=p.relative_to(root).as_posix()
  if rel in ex:continue
  s=os.lstat(p);mode=f"{stat.S_IMODE(s.st_mode):04o}"
  if stat.S_ISLNK(s.st_mode):raise ValueError("symlink")
  if stat.S_ISDIR(s.st_mode):out.append({"kind":"directory","mode":mode,"path":rel})
  elif stat.S_ISREG(s.st_mode):out.append({"kind":"regular","mode":mode,"path":rel,"sha256":h(p.read_bytes())})
  else:raise ValueError("nonregular")
 return sorted(out,key=lambda x:x["path"])
def validate_root(root:Path):
 if not root.is_absolute() or root.is_symlink() or not root.is_dir() or root.resolve(strict=True)!=root:raise ValueError("root")
 for p in root.rglob("*"):
  rel=p.relative_to(root).as_posix();s=os.lstat(p)
  if stat.S_ISLNK(s.st_mode):raise GReject("SYMLINK_COMPONENT")
  if not (stat.S_ISDIR(s.st_mode) or stat.S_ISREG(s.st_mode)):raise ValueError("kind")
  if "__pycache__" in p.parts or p.suffix in (".pyc",".pyo") or p.name in {".pytest_cache",".mypy_cache",".ruff_cache",".DS_Store"}:raise GReject("HYGIENE_FORBIDDEN_ARTIFACT")
 contract=load(root/"contracts/INTEGRATION_CONTRACT.json")
 if contract["declared_state_a_files"]!=FILES or contract["declared_output_directories"]!=DIRS:raise ValueError("contract paths")
 for x in FILES:
  if not safe_rel(x):raise ValueError("unsafe path")
 model=load(root/"contracts/SCIENCE_MODEL.json")
 if model.get("provenance",{}).get("phase2_parent_manifest_sha256")!="d035310ac046981abe7a37a033b1354e3d8da3f53f33d631786ed80f40b90181":raise GReject("PARENT_SEAL_MISMATCH")
 paths=model.get("outputs")
 if type(paths) is not list or not paths or type(paths[0]) is not dict or type(paths[0].get("path")) is not str:raise ValueError("model outputs")
 if paths[0]["path"].startswith("/"):raise GReject("UNSAFE_ABSOLUTE_PATH")
 if ".." in PurePosixPath(paths[0]["path"]).parts:raise GReject("UNSAFE_PARENT_PATH")
 if model.get("filesystem",{}).get("results")!="directory":raise GReject("SYMLINK_COMPONENT")
 if model.get("filesystem",{}).get("extra")!="absent":raise GReject("HYGIENE_FORBIDDEN_ARTIFACT")
 if model.get("transaction",{}).get("late_failure") is not False:raise GReject("FORCED_LATE_PREINSTALL_FAILURE")
def expected_paths(out:Path,state:str,phase:str):
 actual=rows(out);files=[x for x in actual if x["kind"]=="regular"];dirs=[x for x in actual if x["kind"]=="directory"]
 expected=[x for x in FILES if phase=="FINAL" or x not in {"results/SHA256SUMS.txt","results/integrity_audit.json"}]
 if state=="B" and phase=="FINAL":expected.append("PAPER_MANIFEST.sha256")
 if [x["path"] for x in files]!=sorted(expected) or [x["path"] for x in dirs]!=DIRS:raise ValueError("namespace")
 if stat.S_IMODE(os.lstat(out).st_mode)!=0o755 or any(x["mode"]!="0644" for x in files) or any(x["mode"]!="0755" for x in dirs):raise ValueError("modes")
def core_tree(out:Path):return rows(out,{"results/SHA256SUMS.txt","results/integrity_audit.json","PAPER_MANIFEST.sha256"})
def report(root:Path,out:Path,state:str,static:str,commit:str|None):
 main=load(out/"evaluations/main_evaluation.json");ind=load(out/"evaluations/independent_evaluation.json")
 if main["state"]!=state or ind["state"]!=state or main["route_sha256"]!=ind["route_sha256"] or main["full_normalized_route_sha256"]!=ind["full_normalized_route_sha256"]:raise ValueError("route audits")
 status="PREAUTHORITY_INTEGRATION" if state=="A" else "PUBLICATION_SHAPED_AWAITING_ROOT_AUTHORIZATION"
 return {"candidate_id":"SD-C50","expected_paper_manifest":state=="B","integration_status":status,"pre_certificate_tree_sha256":h(enc(core_tree(out))),"route_sha256":main["route_sha256"],"schema":"paper48.integrity-audit.v1","state":state,"static_inventory_sha256":static,"status":"PASS"}
def manifest_bytes(out:Path):
 names=sorted(x for x in FILES if x!="results/SHA256SUMS.txt")
 return ("\n".join(f"{h((out/name).read_bytes())}  {name}" for name in names)+"\n").encode("ascii")
def paper_rows(root:Path,out:Path):
 result=[]
 for p in root.rglob("*"):
  rel=p.relative_to(root).as_posix()
  if rel in {"STATIC_TREE_MANIFEST.json","PREOUTPUT_STATIC_SEAL.json","outputs"} or rel.startswith("outputs/"):continue
  s=os.lstat(p);mode=f"{stat.S_IMODE(s.st_mode):04o}"
  if stat.S_ISLNK(s.st_mode):raise ValueError("paper symlink")
  if stat.S_ISDIR(s.st_mode):result.append({"kind":"directory","mode":mode,"path":rel})
  elif stat.S_ISREG(s.st_mode):result.append({"kind":"regular","mode":mode,"path":rel,"sha256":h(p.read_bytes())})
  else:raise ValueError("paper kind")
 for p in out.rglob("*"):
  rel="outputs/"+p.relative_to(out).as_posix()
  if rel=="outputs/PAPER_MANIFEST.sha256":continue
  s=os.lstat(p);mode=f"{stat.S_IMODE(s.st_mode):04o}"
  if stat.S_ISDIR(s.st_mode):result.append({"kind":"directory","mode":mode,"path":rel})
  elif stat.S_ISREG(s.st_mode):result.append({"kind":"regular","mode":mode,"path":rel,"sha256":h(p.read_bytes())})
  else:raise ValueError("paper output kind")
 return sorted(result,key=lambda x:x["path"])
def audit(root:Path,out:Path,state:str,phase:str,static:str,commit:str|None):
 validate_root(root);expected_paths(out,state,phase)
 for p in out.rglob("*"):
  if p.is_file() and any(token in p.read_bytes() for token in HOST):raise ValueError("host token")
 if phase=="PRE_CERT":return report(root,out,state,static,commit)
 expected=report(root,out,state,static,commit)
 if (out/"results/integrity_audit.json").read_bytes()!=enc(expected):raise ValueError("integrity reconstruction")
 if (out/"results/SHA256SUMS.txt").read_bytes()!=manifest_bytes(out):raise ValueError("result manifest")
 if state=="A":
  if commit is not None or (out/"PAPER_MANIFEST.sha256").exists():raise ValueError("A provenance")
 else:
  if type(commit) is not str or re.fullmatch(r"[0-9a-f]{40}",commit) is None or commit=="0"*40:raise ValueError("B commit")
  pm=load(out/"PAPER_MANIFEST.sha256");wanted={"exclude":["PREOUTPUT_STATIC_SEAL.json","STATIC_TREE_MANIFEST.json","outputs/PAPER_MANIFEST.sha256"],"rows":paper_rows(root,out),"schema":"paper48.state-b-paper-manifest.v1"}
  if pm!=wanted:raise ValueError("paper manifest")
 return expected
def main():
 p=argparse.ArgumentParser(allow_abbrev=False);p.add_argument("--root",type=Path);p.add_argument("--output-root",type=Path);p.add_argument("--state",choices=["A","B"]);p.add_argument("--phase",choices=["PRE_CERT","FINAL"]);p.add_argument("--static-digest");p.add_argument("--commit");p.add_argument("--preflight",action="store_true");p.add_argument("--attack",type=Path)
 try:
  a=p.parse_args()
  if a.attack:
   if a.root or a.output_root or a.state or a.phase or a.static_digest or a.commit or a.preflight:raise ValueError("arity")
   return attack(a.attack)
  if a.root is None:raise ValueError("root")
  root=a.root.resolve(strict=True)
  if a.preflight:
   validate_root(root);sys.stdout.buffer.write(enc({"candidate_id":"SD-C50","consumer":"G","schema":"paper48.integrity-preflight.v1","status":"PASS"}));return 0
  if None in (a.output_root,a.state,a.phase,a.static_digest) or re.fullmatch(r"[0-9a-f]{64}",a.static_digest) is None:raise ValueError("arity")
  sys.stdout.buffer.write(enc(audit(root,a.output_root.resolve(strict=True),a.state,a.phase,a.static_digest,a.commit)));return 0
 except GReject as e:return emit(e.code)
 except Exception as e:sys.stderr.write(f"G_ERROR:{type(e).__name__}\n");return 3
if __name__=="__main__":raise SystemExit(main())
