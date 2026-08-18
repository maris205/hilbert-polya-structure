#!/usr/bin/env python3
"""Primary full recursive Route-v0.2 validator R1."""
from __future__ import annotations
import argparse, copy, hashlib, json, os, re, sys
from pathlib import Path
from typing import Any
P="PENDING_FIRST_ARTIFACT_COMMIT"
FULL_NORMALIZED_SHA="a16a08b142c4eb2a892b8833a0fa168db28aa40215f43e398c121cd90e6cd4a7"
PREAUTH_SHA="59f08523b58b32df0308b9416c9164a3a1745ee4c15a8c143c693a79ef7eb885"
T=["A0_ANALYTIC_ARITHMETIC_ORIGIN","A1_PASS_ANALYTIC","A2_ANALYTIC_DETERMINANT","A3_PARTIAL_ANALYTIC_STRUCTURE","A4_FAIL"]
TOP={"a0","a1","a2","a3","a4","adversarial_controls","authority_integration","blocking_conditions","branch_status","candidate_id","claim_boundary","code_commit","evaluation_date","literature_disposition","next_smallest_test","overall_verdict","round2_clues","route_b","route_b_invocation_allowed","route_tuple","schema","skill","skill_version","source_commit","source_lock","source_lock_code_commit","target_and_root_metrics","terminal_codes","typed_return_map"}
def c(v:Any)->bytes:return (json.dumps(v,sort_keys=True,indent=2,ensure_ascii=True,separators=(",",": "))+"\n").encode("ascii")
def u(pairs:list[tuple[str,Any]])->dict[str,Any]:
 o={}
 for k,v in pairs:
  if k in o:raise ValueError("duplicate")
  o[k]=v
 return o
def load(p:Path)->dict[str,Any]:
 r=p.read_bytes();o=json.loads(r.decode("ascii"),object_pairs_hook=u)
 if type(o) is not dict or r!=c(o):raise ValueError("canonical")
 return o
def reject(code:str)->None:sys.stdout.buffer.write(c({"consumer":"R1","rejection_code":code,"schema":"paper47-mutation-rejection-v1","status":"REJECT"}));raise SystemExit(2)
def artifact_map(root:Path)->dict[str,str]:
 if not root.is_absolute() or root.is_symlink() or not root.is_dir() or root.resolve(strict=True)!=root:reject("ROUTE_ARTIFACT_FAILURE")
 manifest=root/"preauthority/SHA256SUMS.txt"
 if manifest.is_symlink() or hashlib.sha256(manifest.read_bytes()).hexdigest()!=PREAUTH_SHA:reject("ROUTE_ARTIFACT_FAILURE")
 result={}
 for line in manifest.read_text(encoding="ascii").splitlines():
  digest,name=line.split("  ",1)
  if re.fullmatch(r"[A-Z0-9_]+\.(?:md|yaml)",name) is None or name in result:reject("ROUTE_ARTIFACT_FAILURE")
  path=root/"preauthority"/name
  if path.is_symlink() or not path.is_file() or path.resolve(strict=True).parent!= (root/"preauthority").resolve(strict=True) or hashlib.sha256(path.read_bytes()).hexdigest()!=digest:reject("ROUTE_ARTIFACT_FAILURE")
  result[name]=digest
 return result
def validate(o:dict[str,Any],state:str,commit:str|None,root:Path)->None:
 if set(o)!=TOP:reject("ROUTE_SHAPE_FAILURE")
 if o["schema"]!="paper47-route-a-v0.2.0" or o["skill"]!="route-a-evaluator" or o["skill_version"]!="0.2.0" or o["candidate_id"]!="SD-C49" or o["evaluation_date"]!="2026-08-18":reject("ROUTE_IDENTITY_FAILURE")
 if type(o["route_tuple"]) is not list or o["route_tuple"]!=T:reject("ROUTE_TUPLE_FAILURE")
 if o["overall_verdict"]!="ROUTE_A_REJECTED":reject("ROUTE_VERDICT_FAILURE")
 rb=o["route_b"]
 if type(rb) is not dict or set(rb)!={"invocation_allowed","reason"} or type(rb["invocation_allowed"]) is not bool or rb["invocation_allowed"] is not False or type(o["route_b_invocation_allowed"]) is not bool or o["route_b_invocation_allowed"] is not False:reject("ROUTE_B_LOCK_FAILURE")
 for i,key in enumerate(["a0","a1","a2","a3","a4"]):
  if type(o[key]) is not dict or o[key].get("verdict")!=T[i] or type(o[key].get("artifacts")) is not list or not o[key]["artifacts"]:reject("ROUTE_STAGE_FAILURE")
 if set(o["terminal_codes"])!={"completed_divisor","spectral_lift","temporal_prime_support"} or sorted(o["terminal_codes"].values())!=sorted(["STOP_NO_COMPLETED_TARGET_STRUCTURE","STOP_NO_FIXED_SELF_ADJOINT_LIFT","STOP_NO_RATIONAL_PRIME_PRIMITIVES"]):reject("ROUTE_TERMINAL_FAILURE")
 if "STOP_DUPLICATE" in json.dumps(o["terminal_codes"]):reject("ROUTE_TERMINAL_FAILURE")
 if o["literature_disposition"]!="PROCEED_SEARCH_BOUNDED":reject("ROUTE_LITERATURE_FAILURE")
 authority=o["authority_integration"]
 if type(authority) is not dict:reject("PROVENANCE_STATE_FAILURE")
 commits=[o["source_commit"],o["code_commit"],o["source_lock_code_commit"]];present=authority.get("paper_manifest_present");authority_status=authority.get("status")
 if state=="A":
  if commit is not None or commits!=[P,P,P] or present is not False or type(authority_status) is not str or authority_status!="PREAUTHORITY_INTEGRATION":reject("PROVENANCE_STATE_FAILURE")
 else:
  if commit is None or re.fullmatch(r"[0-9a-f]{40}",commit) is None or commit=="0"*40 or commits!=[commit]*3 or present is not True or type(authority_status) is not str or authority_status!="PUBLICATION_SHAPED_AWAITING_ROOT_AUTHORIZATION":reject("PROVENANCE_STATE_FAILURE")
 if type(o["target_and_root_metrics"]) is not dict or o["target_and_root_metrics"]!={"finite_cutoffs_used_as_proof":False,"numerical_root_search_used":False,"target_zero_data_used":False,"theorem_endpoints_proved_analytically":True}:reject("ROUTE_METRIC_FAILURE")
 if type(o["source_lock"]) is not dict or set(o["source_lock"])!={"arithmetic_origin","artifact_path_base","clock","determinant_convention","forbidden_data","function_space","object","parameter_provenance","phase_space"}:reject("ROUTE_SOURCE_LOCK_FAILURE")
 # Normalize only the four declared provenance-dependent fields, then bind every
 # remaining nested key, scalar type, list order, and string by a full-object hash.
 normalized=copy.deepcopy(o);normalized["source_commit"]=P;normalized["code_commit"]=P;normalized["source_lock_code_commit"]=P
 normalized["authority_integration"]["paper_manifest_present"]=False
 normalized["authority_integration"]["status"]="PREAUTHORITY_INTEGRATION"
 if hashlib.sha256(c(normalized)).hexdigest()!=FULL_NORMALIZED_SHA:reject("ROUTE_FULL_OBJECT_FAILURE")
 frozen=artifact_map(root)
 expected_artifacts={"a0":["SOURCE_LOCK.md","DERIVATION_PACKAGE.md","EXACT_WITNESS_LEDGER.md"],
  "a1":["OBJECT_MARKER_OPERATOR_CONTRACT.md","PROOF_PACKAGE.md","THEOREM_FALSIFIERS.md"],
  "a2":["DERIVATION_PACKAGE.md","PROOF_PACKAGE.md","OBJECT_MARKER_OPERATOR_CONTRACT.md"],
  "a3":["DERIVATION_PACKAGE.md","LITERATURE_NOVELTY_AUDIT.md","SOURCE_LOCK.md"],
  "a4":["OBJECT_MARKER_OPERATOR_CONTRACT.md","THEOREM_FALSIFIERS.md","LITERATURE_NOVELTY_AUDIT.md"]}
 for stage,names in expected_artifacts.items():
  if o[stage]["artifacts"]!=names or any(name not in frozen for name in names):reject("ROUTE_ARTIFACT_FAILURE")
def main()->None:
 p=argparse.ArgumentParser(allow_abbrev=False);p.add_argument("--route",required=True);p.add_argument("--root",required=True);p.add_argument("--state",required=True,choices=["A","B"]);p.add_argument("--commit");a=p.parse_args()
 try:o=load(Path(a.route).resolve(strict=True));validate(o,a.state,a.commit,Path(a.root));sys.stdout.buffer.write(c({"candidate_id":"SD-C49","consumer":"R1","payload":{"artifact_manifest_sha256":PREAUTH_SHA,"full_normalized_route_sha256":FULL_NORMALIZED_SHA,"route_sha256":hashlib.sha256(c(o)).hexdigest(),"state":a.state},"schema":"paper47-route-primary-audit-v1","status":"PASS"}))
 except SystemExit:raise
 except Exception as e:sys.stderr.write(f"R1_ERROR:{type(e).__name__}\n");raise SystemExit(3)
if __name__=="__main__":main()
