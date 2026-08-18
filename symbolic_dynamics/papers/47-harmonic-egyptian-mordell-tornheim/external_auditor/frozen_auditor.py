#!/usr/bin/env python3
"""Frozen external whole-tree, artifact, and namespace auditor for Paper 47."""
from __future__ import annotations
import argparse, hashlib, json, os, re, stat, sys
from pathlib import Path, PurePosixPath
from typing import Any
PRE="59f08523b58b32df0308b9416c9164a3a1745ee4c15a8c143c693a79ef7eb885"
B_COMMIT="1111111111111111111111111111111111111111"
B_DOMAIN="sha256_of_canonical_sorted_recursive_path_kind_mode_hash_rows_excluding_exact_PAPER_MANIFEST.sha256"
CHECKS=["based_closed_walks","coprime_coordinate_bijection","endpoint_and_complex_phase_controls","exact_trace_powers_1_through_5","finite_evidence_class","first_trace_even_harmonic","full_divisor_rows","literal_matrices","negative_principal_minor","ordered_support_quotients_loops","rectangular_primitive_mt_gcd_extraction","second_trace_termwise_finite_cutoff"]
MODEL=["bounded_domain","candidate_id","coprime_required","determinant_domains","edge_parameterization","hilbert_schmidt_domain","loops","mixed_triangle","mt_novelty_claimed","operator_positive_semidefinite","ordered_edge_multiplier","primitive_mt_factor","relation","scale_factor","temporal_primitive","trace_class_domain"]
IDS=[f"F{x:02d}" for x in range(1,16)]+[f"G{x:02d}" for x in range(1,25)]
def enc(v:Any)->bytes:return (json.dumps(v,sort_keys=True,indent=2,ensure_ascii=True,separators=(",",": "))+"\n").encode("ascii")
def pairs(p:list[tuple[str,Any]])->dict[str,Any]:
 o={}
 for k,v in p:
  if k in o:raise KeyError("duplicate")
  o[k]=v
 return o
def decode(path:Path)->tuple[bytes,dict[str,Any]]:
 raw=path.read_bytes()
 try:o=json.loads(raw.decode("ascii"),object_pairs_hook=pairs)
 except KeyError:reject("DUPLICATE_JSON_KEY")
 except Exception:reject("INVALID_JSON")
 if type(o) is not dict:reject("JSON_TOP_LEVEL_FAILURE")
 if raw!=enc(o):reject("NONCANONICAL_JSON")
 return raw,o
def reject(code:str)->None:sys.stdout.buffer.write(enc({"consumer":"F","rejection_code":code,"schema":"paper47-mutation-rejection-v1","status":"REJECT"}));raise SystemExit(2)
def safe_relative(text:str)->bool:
 if type(text) is not str or text=="" or "\\" in text:return False
 p=PurePosixPath(text)
 return not p.is_absolute() and all(x not in ("",".","..") for x in p.parts)
def root_safe(text:str)->Path:
 if not os.path.isabs(text):reject("UNSAFE_PATH_FAILURE")
 r=Path(text)
 if r.is_symlink() or not r.is_dir() or r.resolve(strict=True)!=r:reject("UNSAFE_PATH_FAILURE")
 for parent in [r,*r.parents]:
  if parent.is_symlink():reject("UNSAFE_PATH_FAILURE")
 return r
def tree_rows(root:Path,skip:set[str]|None=None)->list[dict[str,Any]]:
 skip=skip or set();out=[]
 for p in root.rglob("*"):
  rel=p.relative_to(root).as_posix()
  if rel in skip or any(rel.startswith(x+"/") for x in skip):continue
  st=os.lstat(p);mode=f"{stat.S_IMODE(st.st_mode):04o}"
  if stat.S_ISLNK(st.st_mode):out.append({"kind":"symlink","mode":mode,"path":rel})
  elif stat.S_ISDIR(st.st_mode):out.append({"kind":"directory","mode":mode,"path":rel})
  elif stat.S_ISREG(st.st_mode):out.append({"kind":"regular","mode":mode,"path":rel,"sha256":hashlib.sha256(p.read_bytes()).hexdigest()})
  elif stat.S_ISFIFO(st.st_mode):out.append({"kind":"fifo","mode":mode,"path":rel})
  else:out.append({"kind":"other","mode":mode,"path":rel})
 return sorted(out,key=lambda z:z["path"])
def valid_sha(value:Any,allow_zero:bool=False)->bool:
 return type(value) is str and re.fullmatch(r"[0-9a-f]{64}",value) is not None and (allow_zero or value!="0"*64)
def validate_seal(seal:dict[str,Any],base_count:int)->None:
 if set(seal)!={"candidate_id","contract_counts","preauthority_manifest_sha256","schema","smoke","static_inventory_sha256","status","zero_state"}:reject("STATIC_SEAL_SHAPE_FAILURE")
 preliminary=seal.get("status")=="PRELIMINARY_FOR_DISPOSABLE_SMOKE"
 if seal.get("candidate_id")!="SD-C49" or seal.get("schema")!="paper47-preoutput-static-seal-v2" or seal.get("status") not in ("HOLD_FOR_INDEPENDENT_AUDIT","PRELIMINARY_FOR_DISPOSABLE_SMOKE") or seal.get("preauthority_manifest_sha256")!=PRE or not valid_sha(seal.get("static_inventory_sha256")):reject("STATIC_SEAL_VALUE_FAILURE")
 counts=seal.get("contract_counts")
 expected_count_keys={"declared_output_directories","declared_state_A_files","expanded_nested_mutations","external_auditor_mutations","frozen_theorem_falsifiers","governance_mutations","mutation_instances","preauthority_files","static_inventory_rows"}
 if type(counts) is not dict or set(counts)!=expected_count_keys or any(type(v) is not int or v<0 for v in counts.values()) or counts["declared_output_directories"]!=8 or counts["declared_state_A_files"]!=20 or counts["expanded_nested_mutations"]!=35 or counts["external_auditor_mutations"]!=15 or counts["frozen_theorem_falsifiers"]!=15 or counts["governance_mutations"]!=24 or counts["mutation_instances"]!=39 or counts["preauthority_files"]!=15 or counts["static_inventory_rows"]!=base_count:reject("STATIC_SEAL_COUNT_FAILURE")
 zero=seal.get("zero_state")
 if zero!={"cache_files":0,"candidate_output_files":0,"candidate_outputs_directory_present":False}:reject("STATIC_SEAL_ZERO_STATE_FAILURE")
 smoke=seal.get("smoke")
 keys={"candidate_run_in_place","cold_hostile_byte_identical","completed","coordinated_full_state_mutations","expanded_mutation_instances","external_auditor_mutation_result_sha256","external_auditor_mutation_survivors","first_install_physical_replacements","forced_late_failure_exit","forced_late_failure_parent_unchanged","forced_late_failure_target_unchanged","mixed_state_rejected_unchanged","mutation_consumer_invocations","mutation_instances","mutation_result_sha256","mutation_survivors","normal_and_hostile_outputs_byte_identical","report_sha256","result_ledger_sha256","second_run_physical_replacements","second_run_target_and_parent_metadata_unchanged","state_A_final_tree_sha256","state_A_output_files","state_B_manifest_rows","state_B_output_files","state_B_smoke_commit","state_B_stable_payload_domain","state_B_stable_payload_tree_sha256","unsafe_cli_and_provenance_matrix_rejected_pre_output","unsafe_symlink_outside_sentinel_unchanged"}
 if type(smoke) is not dict or set(smoke)!=keys:reject("STATIC_SEAL_SMOKE_SHAPE_FAILURE")
 bools=keys-{"expanded_mutation_instances","external_auditor_mutation_result_sha256","external_auditor_mutation_survivors","first_install_physical_replacements","forced_late_failure_exit","mutation_consumer_invocations","mutation_instances","mutation_result_sha256","mutation_survivors","report_sha256","result_ledger_sha256","second_run_physical_replacements","state_A_final_tree_sha256","state_A_output_files","state_B_manifest_rows","state_B_output_files","state_B_smoke_commit","state_B_stable_payload_domain","state_B_stable_payload_tree_sha256"}
 if any(type(smoke[k]) is not bool for k in bools):reject("STATIC_SEAL_SMOKE_TYPE_FAILURE")
 ints={"expanded_mutation_instances":35,"external_auditor_mutation_survivors":0,"first_install_physical_replacements":1,"forced_late_failure_exit":86,"mutation_consumer_invocations":60,"mutation_instances":39,"mutation_survivors":0,"second_run_physical_replacements":0,"state_A_output_files":20,"state_B_output_files":21}
 if any(type(smoke[k]) is not int or smoke[k]!=v for k,v in ints.items()) or type(smoke["state_B_manifest_rows"]) is not int or smoke["state_B_manifest_rows"]<1:reject("STATIC_SEAL_SMOKE_COUNT_FAILURE")
 if smoke["state_B_smoke_commit"]!=B_COMMIT:reject("STATIC_SEAL_SMOKE_COMMIT_FAILURE")
 if smoke["state_B_stable_payload_domain"]!=B_DOMAIN:reject("STATIC_SEAL_SMOKE_DOMAIN_FAILURE")
 hashes=["external_auditor_mutation_result_sha256","mutation_result_sha256","report_sha256","result_ledger_sha256","state_A_final_tree_sha256","state_B_stable_payload_tree_sha256"]
 if any(not valid_sha(smoke[k],allow_zero=preliminary) for k in hashes):reject("STATIC_SEAL_SMOKE_HASH_FAILURE")
 if not preliminary and (not all(smoke[k] for k in bools if k!="candidate_run_in_place") or smoke["candidate_run_in_place"] is not False):reject("STATIC_SEAL_SMOKE_VALUE_FAILURE")
def audit_static(root:Path)->dict[str,Any]:
 _,seal=decode(root/"PREOUTPUT_STATIC_SEAL.json");manifest_raw,manifest=decode(root/"STATIC_TREE_MANIFEST.json")
 if stat.S_IMODE(os.lstat(root).st_mode)!=0o755:reject("ROOT_MODE_FAILURE")
 if stat.S_IMODE(os.lstat(root/"STATIC_TREE_MANIFEST.json").st_mode)!=0o644:reject("STATIC_MANIFEST_MODE_FAILURE")
 if stat.S_IMODE(os.lstat(root/"PREOUTPUT_STATIC_SEAL.json").st_mode)!=0o644:reject("STATIC_SEAL_MODE_FAILURE")
 if set(manifest)!={"base_inventory_sha256","candidate_id","output_root_mode","root_mode","rows","schema"} or manifest["candidate_id"]!="SD-C49" or manifest["schema"]!="paper47-static-tree-manifest-v2" or manifest["root_mode"]!="0755" or manifest["output_root_mode"]!="0755" or type(manifest["rows"]) is not list:reject("STATIC_MANIFEST_SHAPE_FAILURE")
 actual_outer=tree_rows(root,{"outputs","STATIC_TREE_MANIFEST.json"})
 if actual_outer!=manifest["rows"]:reject("STATIC_TREE_FAILURE")
 actual_base=tree_rows(root,{"outputs","PREOUTPUT_STATIC_SEAL.json","STATIC_TREE_MANIFEST.json"})
 inventory=hashlib.sha256(enc(actual_base)).hexdigest()
 if inventory!=manifest["base_inventory_sha256"] or inventory!=seal.get("static_inventory_sha256"):reject("STATIC_INVENTORY_FAILURE")
 validate_seal(seal,len(actual_base))
 if hashlib.sha256((root/"preauthority/SHA256SUMS.txt").read_bytes()).hexdigest()!=PRE:reject("PREAUTHORITY_SEAL_FAILURE")
 if (root/"outputs").exists() and ((root/"outputs").is_symlink() or not (root/"outputs").is_dir()):reject("OUTPUT_NAMESPACE_FAILURE")
 if (root/"outputs").exists() and stat.S_IMODE(os.lstat(root/"outputs").st_mode)!=0o755:reject("OUTPUT_ROOT_MODE_FAILURE")
 return {"candidate_id":"SD-C49","payload":{"preauthority_manifest_sha256":PRE,"static_inventory_sha256":inventory,"static_row_count":len(actual_base)},"schema":"paper47-frozen-static-audit-v1","status":"PASS"}
def audit_model(path:Path)->dict[str,Any]:
 _,o=decode(path)
 if sorted(o)!=MODEL:reject("SCIENCE_MODEL_SHAPE_FAILURE")
 strings=["bounded_domain","candidate_id","edge_parameterization","hilbert_schmidt_domain","loops","primitive_mt_factor","relation","scale_factor","temporal_primitive","trace_class_domain"]
 if any(type(o[k]) is not str for k in strings) or type(o["coprime_required"]) is not bool or type(o["mt_novelty_claimed"]) is not bool or type(o["operator_positive_semidefinite"]) is not bool or type(o["ordered_edge_multiplier"]) is not int or type(o["mixed_triangle"]) is not list or any(type(x) is not int for x in o["mixed_triangle"]) or type(o["determinant_domains"]) is not dict or sorted(o["determinant_domains"])!=["det2","ordinary"] or any(type(x) is not str for x in o["determinant_domains"].values()):reject("SCIENCE_MODEL_TYPE_FAILURE")
 return {"consumer":"F","schema":"paper47-artifact-accept-v1","status":"PASS"}
def audit_result(path:Path,expected:str|None)->dict[str,Any]:
 raw,o=decode(path)
 if sorted(o)!=["candidate_id","payload","schema","status"] or o.get("schema")!="paper47-exact-comparison-v1" or o.get("status")!="PASS" or type(o.get("payload")) is not dict:reject("RESULT_SHAPE_FAILURE")
 checks=o["payload"].get("checks")
 if type(checks) is not dict or sorted(checks)!=CHECKS or any(type(v) is not str or v!="PASS" for v in checks.values()):reject("RESULT_CHECK_MAP_FAILURE")
 if sorted(o["payload"])!=["checks","direct_sha256","parameter_sha256"] or any(re.fullmatch(r"[0-9a-f]{64}",o["payload"].get(k,"")) is None for k in ("direct_sha256","parameter_sha256")):reject("RESULT_SHAPE_FAILURE")
 if expected is not None and hashlib.sha256(raw).hexdigest()!=expected:reject("SEALED_RESULT_HASH_FAILURE")
 return {"consumer":"F","schema":"paper47-artifact-accept-v1","status":"PASS"}
def audit_registry(path:Path,expected:str|None)->dict[str,Any]:
 raw,o=decode(path)
 if sorted(o)!=["candidate_id","instances","schema"] or o.get("candidate_id")!="SD-C49" or o.get("schema")!="paper47-mutation-registry-v1" or type(o["instances"]) is not list or [x.get("id") for x in o["instances"] if type(x) is dict]!=IDS:reject("MUTATION_REGISTRY_FAILURE")
 if expected is not None and hashlib.sha256(raw).hexdigest()!=expected:reject("MUTATION_REGISTRY_FAILURE")
 return {"consumer":"F","schema":"paper47-artifact-accept-v1","status":"PASS"}
def audit_namespace(path:Path,manifest_path:Path)->dict[str,Any]:
 _,manifest=decode(manifest_path)
 if sorted(manifest)!=["rows","schema"] or manifest["schema"]!="paper47-namespace-manifest-v1":reject("OUTPUT_NAMESPACE_FAILURE")
 if path.is_symlink() or not path.is_dir():reject("OUTPUT_NAMESPACE_FAILURE")
 if tree_rows(path)!=manifest["rows"]:reject("OUTPUT_NAMESPACE_FAILURE")
 return {"consumer":"F","schema":"paper47-artifact-accept-v1","status":"PASS"}
def main()->None:
 p=argparse.ArgumentParser(allow_abbrev=False);p.add_argument("--root");p.add_argument("--artifact");p.add_argument("--kind",choices=["model","result","registry"]);p.add_argument("--expected-sha256");p.add_argument("--namespace");p.add_argument("--namespace-manifest");p.add_argument("--check-relative");a=p.parse_args()
 try:
  modes=sum(x is not None for x in (a.root,a.artifact,a.namespace,a.check_relative))
  if modes!=1:raise ValueError("one mode")
  if a.root is not None:out=audit_static(root_safe(a.root))
  elif a.check_relative is not None:
   if not safe_relative(a.check_relative):reject("UNSAFE_PATH_FAILURE")
   out={"consumer":"F","schema":"paper47-artifact-accept-v1","status":"PASS"}
  elif a.namespace is not None:
   if a.namespace_manifest is None or a.kind is not None or a.expected_sha256 is not None:raise ValueError("namespace args")
   out=audit_namespace(Path(a.namespace).resolve(strict=True),Path(a.namespace_manifest).resolve(strict=True))
  else:
   if a.kind is None or a.namespace_manifest is not None:raise ValueError("artifact args")
   q=Path(a.artifact).resolve(strict=True)
   out=audit_model(q) if a.kind=="model" else audit_result(q,a.expected_sha256) if a.kind=="result" else audit_registry(q,a.expected_sha256)
  sys.stdout.buffer.write(enc(out))
 except SystemExit:raise
 except Exception as e:sys.stderr.write(f"F_ERROR:{type(e).__name__}\n");raise SystemExit(3)
if __name__=="__main__":main()
