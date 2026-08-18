#!/usr/bin/env python3
"""Render the complete frozen Route-A expectation plus integration state."""
from __future__ import annotations
import argparse,hashlib,json,re,sys
from pathlib import Path
from typing import Any
import yaml
PRE="f5669e651c4c31ce860bad534d17e64956a8750412f74257d341810424252057"
def enc(v:Any)->bytes:return (json.dumps(v,sort_keys=True,indent=2,ensure_ascii=True,separators=(",",": "),allow_nan=False)+"\n").encode("ascii")
def sha(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()
def make(root:Path,state:str,static_digest:str,commit:str|None):
 expectation=yaml.safe_load((root/"preauthority/ROUTE_EXPECTATION.yaml").read_text(encoding="utf-8"))
 if type(expectation) is not dict or expectation.get("candidate_id")!="SD-C50" or expectation.get("evaluation_state")!="NOT_RUN_EXPECTATION_ONLY":raise ValueError("expectation")
 if expectation.get("route_tuple")!=["A0_FAIL","A1_FAIL","A2_ANALYTIC_DETERMINANT","A3_FAIL","A4_FAIL"] or expectation.get("overall_verdict")!="ROUTE_A_REJECTED":raise ValueError("terminal")
 if expectation.get("route_b_invocation_allowed") is not False or expectation.get("route_b",{}).get("invocation_allowed") is not False:raise ValueError("route B")
 if state=="A":
  if commit is not None:raise ValueError("A commit")
  status="PREAUTHORITY_INTEGRATION"
 else:
  if type(commit) is not str or re.fullmatch(r"[0-9a-f]{40}",commit) is None or commit=="0"*40:raise ValueError("B commit")
  status="PUBLICATION_SHAPED_AWAITING_ROOT_AUTHORIZATION"
 return {**expectation,
  "artifact_bindings":{"experiment_contract_sha256":sha(root/"preauthority/EXPERIMENT_CONTRACT.json"),"preauthority_manifest_sha256":PRE,"proof_package_sha256":sha(root/"preauthority/PROOF_PACKAGE.md"),"static_inventory_sha256":static_digest},
  "integration":{"authority_write_authorized":False,"commit":commit,"state":state,"status":status},
  "schema":"paper48.route-a.v0.2.0"}
def main():
 p=argparse.ArgumentParser(allow_abbrev=False);p.add_argument("--root",type=Path,required=True);p.add_argument("--state",choices=["A","B"],required=True);p.add_argument("--static-digest",required=True);p.add_argument("--commit")
 try:
  a=p.parse_args()
  if re.fullmatch(r"[0-9a-f]{64}",a.static_digest) is None:raise ValueError("static")
  sys.stdout.buffer.write(enc(make(a.root.resolve(strict=True),a.state,a.static_digest,a.commit)));return 0
 except Exception as e:sys.stderr.write(f"ROUTE_RENDER_ERROR:{type(e).__name__}\n");return 3
if __name__=="__main__":raise SystemExit(main())
