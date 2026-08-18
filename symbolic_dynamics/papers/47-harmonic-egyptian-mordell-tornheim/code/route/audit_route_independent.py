#!/usr/bin/env python3
"""Second, non-importing full Route-v0.2 validator R2."""
from __future__ import annotations
import argparse,hashlib,json,os,re,sys
from pathlib import Path
from typing import Any
NORMAL_FORM_SHA="a16a08b142c4eb2a892b8833a0fa168db28aa40215f43e398c121cd90e6cd4a7"
INPUT_SHA="59f08523b58b32df0308b9416c9164a3a1745ee4c15a8c143c693a79ef7eb885"
def enc(x:Any)->bytes:return (json.dumps(x,ensure_ascii=True,indent=2,separators=(",",": "),sort_keys=True)+"\n").encode("ascii")
def pairs(seq:list[tuple[str,Any]])->dict[str,Any]:
 d={}
 for k,v in seq:
  if k in d:raise RuntimeError("duplicate")
  d[k]=v
 return d
def read(path:Path)->dict[str,Any]:
 raw=path.read_bytes();data=json.loads(raw.decode("ascii"),object_pairs_hook=pairs)
 if data.__class__ is not dict or enc(data)!=raw:raise RuntimeError("encoding")
 return data
def no(code:str)->None:sys.stdout.buffer.write(enc({"consumer":"R2","rejection_code":code,"schema":"paper47-mutation-rejection-v1","status":"REJECT"}));raise SystemExit(2)
def audit_inputs(root:Path,route:dict[str,Any])->None:
 if not root.is_absolute() or root.is_symlink() or not root.is_dir() or root.resolve(strict=True)!=root:no("ROUTE_ARTIFACT_FAILURE")
 manifest=root/"preauthority/SHA256SUMS.txt"
 if manifest.is_symlink() or hashlib.sha256(manifest.read_bytes()).hexdigest()!=INPUT_SHA:no("ROUTE_ARTIFACT_FAILURE")
 table={}
 for raw in manifest.read_text(encoding="ascii").splitlines():
  try:digest,name=raw.split("  ",1)
  except ValueError:no("ROUTE_ARTIFACT_FAILURE")
  if name in table or "/" in name or "\\" in name or name in (".","..") or re.fullmatch("[0-9a-f]{64}",digest) is None:no("ROUTE_ARTIFACT_FAILURE")
  item=root/"preauthority"/name
  if item.is_symlink() or not item.is_file() or item.resolve(strict=True).parent!=(root/"preauthority").resolve(strict=True) or hashlib.sha256(item.read_bytes()).hexdigest()!=digest:no("ROUTE_ARTIFACT_FAILURE")
  table[name]=digest
 exact={"a0":["SOURCE_LOCK.md","DERIVATION_PACKAGE.md","EXACT_WITNESS_LEDGER.md"],"a1":["OBJECT_MARKER_OPERATOR_CONTRACT.md","PROOF_PACKAGE.md","THEOREM_FALSIFIERS.md"],"a2":["DERIVATION_PACKAGE.md","PROOF_PACKAGE.md","OBJECT_MARKER_OPERATOR_CONTRACT.md"],"a3":["DERIVATION_PACKAGE.md","LITERATURE_NOVELTY_AUDIT.md","SOURCE_LOCK.md"],"a4":["OBJECT_MARKER_OPERATOR_CONTRACT.md","THEOREM_FALSIFIERS.md","LITERATURE_NOVELTY_AUDIT.md"]}
 if any(route[key].get("artifacts")!=value or any(name not in table for name in value) for key,value in exact.items()):no("ROUTE_ARTIFACT_FAILURE")
def normalized_digest(x:dict[str,Any])->str:
 # A fresh JSON round trip makes the normalization non-aliasing and preserves
 # the strict JSON scalar types checked by the final canonical digest.
 y=json.loads(json.dumps(x,sort_keys=True,separators=(",",":")))
 for field in ("source_commit","code_commit","source_lock_code_commit"):y[field]="PENDING_FIRST_ARTIFACT_COMMIT"
 y["authority_integration"]["paper_manifest_present"]=False;y["authority_integration"]["status"]="PREAUTHORITY_INTEGRATION"
 return hashlib.sha256(enc(y)).hexdigest()
def audit(x:dict[str,Any],state:str,commit:str|None,root:Path)->None:
 required=["a0","a1","a2","a3","a4","adversarial_controls","authority_integration","blocking_conditions","branch_status","candidate_id","claim_boundary","code_commit","evaluation_date","literature_disposition","next_smallest_test","overall_verdict","round2_clues","route_b","route_b_invocation_allowed","route_tuple","schema","skill","skill_version","source_commit","source_lock","source_lock_code_commit","target_and_root_metrics","terminal_codes","typed_return_map"]
 if sorted(x)!=required:no("ROUTE_SHAPE_FAILURE")
 desired=("A0_ANALYTIC_ARITHMETIC_ORIGIN","A1_PASS_ANALYTIC","A2_ANALYTIC_DETERMINANT","A3_PARTIAL_ANALYTIC_STRUCTURE","A4_FAIL")
 if x["route_tuple"].__class__ is not list or tuple(x["route_tuple"])!=desired:no("ROUTE_TUPLE_FAILURE")
 for position,name in enumerate(("a0","a1","a2","a3","a4")):
  part=x[name]
  if part.__class__ is not dict or part.get("verdict")!=desired[position] or part.get("evidence_status") not in ("PROVED","OPEN") or part.get("artifacts",[]).__class__ is not list:no("ROUTE_STAGE_FAILURE")
 if x.get("schema")!="paper47-route-a-v0.2.0" or x.get("skill_version")!="0.2.0" or x.get("candidate_id")!="SD-C49":no("ROUTE_IDENTITY_FAILURE")
 if x.get("overall_verdict")!="ROUTE_A_REJECTED":no("ROUTE_VERDICT_FAILURE")
 branch=x.get("route_b")
 if branch.__class__ is not dict or sorted(branch)!=["invocation_allowed","reason"] or branch["invocation_allowed"] is not False or branch["invocation_allowed"].__class__ is not bool or x.get("route_b_invocation_allowed") is not False or x.get("route_b_invocation_allowed").__class__ is not bool:no("ROUTE_B_LOCK_FAILURE")
 terminals=x.get("terminal_codes")
 if terminals.__class__ is not dict or terminals!={"completed_divisor":"STOP_NO_COMPLETED_TARGET_STRUCTURE","spectral_lift":"STOP_NO_FIXED_SELF_ADJOINT_LIFT","temporal_prime_support":"STOP_NO_RATIONAL_PRIME_PRIMITIVES"}:no("ROUTE_TERMINAL_FAILURE")
 if x.get("literature_disposition")!="PROCEED_SEARCH_BOUNDED":no("ROUTE_LITERATURE_FAILURE")
 authority=x.get("authority_integration")
 if authority.__class__ is not dict:no("PROVENANCE_STATE_FAILURE")
 values=(x.get("source_commit"),x.get("code_commit"),x.get("source_lock_code_commit"));present=authority.get("paper_manifest_present");authority_status=authority.get("status")
 if state=="A":
  if commit is not None or values!=("PENDING_FIRST_ARTIFACT_COMMIT",)*3 or present is not False or authority_status.__class__ is not str or authority_status!="PREAUTHORITY_INTEGRATION":no("PROVENANCE_STATE_FAILURE")
 else:
  if commit is None or re.fullmatch("[0-9a-f]{40}",commit) is None or commit==40*"0" or values!=(commit,commit,commit) or present is not True or authority_status.__class__ is not str or authority_status!="PUBLICATION_SHAPED_AWAITING_ROOT_AUTHORIZATION":no("PROVENANCE_STATE_FAILURE")
 sl=x.get("source_lock");
 if sl.__class__ is not dict or sorted(sl)!=["arithmetic_origin","artifact_path_base","clock","determinant_convention","forbidden_data","function_space","object","parameter_provenance","phase_space"] or "Paper46_generated_evidence" not in sl["forbidden_data"]:no("ROUTE_SOURCE_LOCK_FAILURE")
 metrics=x.get("target_and_root_metrics")
 if metrics!={"finite_cutoffs_used_as_proof":False,"numerical_root_search_used":False,"target_zero_data_used":False,"theorem_endpoints_proved_analytically":True}:no("ROUTE_METRIC_FAILURE")
 if normalized_digest(x)!=NORMAL_FORM_SHA:no("ROUTE_FULL_OBJECT_FAILURE")
 audit_inputs(root,x)
def main()->None:
 ap=argparse.ArgumentParser(allow_abbrev=False);ap.add_argument("--route",required=True);ap.add_argument("--root",required=True);ap.add_argument("--state",required=True,choices=("A","B"));ap.add_argument("--commit");q=ap.parse_args()
 try:
  obj=read(Path(q.route).resolve(strict=True));audit(obj,q.state,q.commit,Path(q.root));sys.stdout.buffer.write(enc({"candidate_id":"SD-C49","consumer":"R2","payload":{"artifact_manifest_sha256":INPUT_SHA,"full_normalized_route_sha256":NORMAL_FORM_SHA,"route_sha256":hashlib.sha256(enc(obj)).hexdigest(),"state":q.state},"schema":"paper47-route-independent-audit-v1","status":"PASS"}))
 except SystemExit:raise
 except Exception as e:sys.stderr.write("R2_ERROR:"+e.__class__.__name__+"\n");raise SystemExit(3)
if __name__=="__main__":main()
