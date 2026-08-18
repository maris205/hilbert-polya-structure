#!/usr/bin/env python3
"""Independent PRE_CERT/FINAL exact namespace and reconstruction auditor."""
from __future__ import annotations
import argparse,hashlib,json,os,re,stat,subprocess,sys
from pathlib import Path
from typing import Any
FILES=["RESULT_LEDGER.json","audits/external_auditor_mutations.json","audits/frozen_static_audit.json","audits/independence_audit.json","audits/integrity_audit.json","audits/literature_audit.json","audits/proof_result_audit.json","audits/route_independent.json","audits/route_primary.json","audits/runtime_controls.json","audits/source_audit.json","audits/type_audit.json","data/source_packet.json","evaluations/route_a/SD-C49/2026-08-18.json","reports/EXPERIMENT_REPORT.md","results/evaluator_d.json","results/evaluator_p.json","results/exact_comparison.json","tests/expanded_mutation_results.json","tests/mutation_results.json"]
DIRS=["audits","data","evaluations","evaluations/route_a","evaluations/route_a/SD-C49","reports","results","tests"]
HOST=[b"/home/",b"/root/",b"/tmp/",b"\\home\\",b"\\root\\",b"\\tmp\\"]
REGISTRY_SHA="80d72f804b7aaf1d5e196f69f7b28977954bc480875a7b4ede8955b729424dc0"
EXTERNAL_CASES=[("byte_drift","STATIC_TREE_FAILURE"),("mode_drift","STATIC_TREE_FAILURE"),("root_mode_drift","ROOT_MODE_FAILURE"),("extra_empty_directory","STATIC_TREE_FAILURE"),("fifo_node","STATIC_TREE_FAILURE"),("symlink_node","STATIC_TREE_FAILURE"),("file_deletion","STATIC_TREE_FAILURE"),("seal_key_drift","STATIC_SEAL_SHAPE_FAILURE"),("seal_mode_drift","STATIC_SEAL_MODE_FAILURE"),("seal_value_drift","STATIC_SEAL_SMOKE_TYPE_FAILURE"),("seal_forbidden_state_b_full_tree_hash","STATIC_SEAL_SMOKE_SHAPE_FAILURE"),("seal_smoke_commit_drift","STATIC_SEAL_SMOKE_COMMIT_FAILURE"),("seal_stable_domain_drift","STATIC_SEAL_SMOKE_DOMAIN_FAILURE"),("manifest_order_drift","NONCANONICAL_JSON"),("installed_auditor_drift","STATIC_TREE_FAILURE")]
def enc(v:Any)->bytes:return (json.dumps(v,sort_keys=True,indent=2,ensure_ascii=True,separators=(",",": "))+"\n").encode("ascii")
def pairs(seq:list[tuple[str,Any]])->dict[str,Any]:
 o={}
 for k,v in seq:
  if k in o:raise ValueError("duplicate")
  o[k]=v
 return o
def load(p:Path)->dict[str,Any]:
 raw=p.read_bytes();o=json.loads(raw.decode("ascii"),object_pairs_hook=pairs)
 if type(o) is not dict or raw!=enc(o):raise ValueError("canonical")
 return o
def invoke(script:Path,args:list[str],cwd:Path)->bytes:
 env={"PATH":os.environ.get("PATH","/usr/bin:/bin"),"PYTHONDONTWRITEBYTECODE":"1",
      "PYTHONPATH":str(cwd/"hostile_modules"),"PYTHONHASHSEED":"0","LC_ALL":"C","LANG":"C"}
 q=subprocess.run([sys.executable,"-I","-B",str(script),*args],cwd=cwd,env=env,
                  stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False,timeout=120)
 if q.returncode or q.stderr:raise ValueError("FINAL replay subprocess")
 return q.stdout
def rows(root:Path,exclude:set[str]|None=None)->list[dict[str,Any]]:
 ex=exclude or set();out=[]
 for p in root.rglob("*"):
  rel=p.relative_to(root).as_posix()
  if rel in ex:continue
  s=os.lstat(p);mode=f"{stat.S_IMODE(s.st_mode):04o}"
  if stat.S_ISLNK(s.st_mode):raise ValueError("symlink")
  if stat.S_ISDIR(s.st_mode):out.append({"kind":"directory","mode":mode,"path":rel})
  elif stat.S_ISREG(s.st_mode):out.append({"kind":"regular","mode":mode,"path":rel,"sha256":hashlib.sha256(p.read_bytes()).hexdigest()})
  else:raise ValueError("nonregular")
 return sorted(out,key=lambda x:x["path"])
def ledger_bytes(output:Path,state:str)->bytes:
 ex={"RESULT_LEDGER.json","audits/integrity_audit.json","PAPER_MANIFEST.sha256"}
 rr=rows(output,ex)
 return enc({"candidate_id":"SD-C49","payload":{"entry_count":len(rr),"rows":rr,"state":state},"schema":"paper47-result-ledger-v1","status":"PASS"})
def validate_mutation_objects(root:Path,output:Path)->None:
 registry_raw=(root/"contracts/MUTATION_REGISTRY.json").read_bytes()
 if hashlib.sha256(registry_raw).hexdigest()!=REGISTRY_SHA:raise ValueError("registry static hash")
 registry=load(root/"contracts/MUTATION_REGISTRY.json")
 if sorted(registry)!=["candidate_id","instances","schema"] or registry["candidate_id"]!="SD-C49" or registry["schema"]!="paper47-mutation-registry-v1" or type(registry["instances"]) is not list or len(registry["instances"])!=39:raise ValueError("registry schema")
 result=load(output/"tests/mutation_results.json")
 if sorted(result)!=["candidate_id","payload","schema","status"] or result["candidate_id"]!="SD-C49" or result["schema"]!="paper47-mutation-results-v1" or result["status"]!="PASS":raise ValueError("mutation top")
 payload=result["payload"]
 if sorted(payload)!=["consumer_invocation_count","instance_count","records","registry_sha256","survivors"] or type(payload["instance_count"]) is not int or type(payload["consumer_invocation_count"]) is not int or type(payload["survivors"]) is not int or payload["instance_count"]!=39 or payload["survivors"]!=0 or payload["registry_sha256"]!=REGISTRY_SHA or type(payload["records"]) is not list or len(payload["records"])!=39:raise ValueError("mutation payload")
 total=0
 for frozen,record in zip(registry["instances"],payload["records"]):
  if sorted(record)!=["designated_consumers","id","observed","rejection_code","survivor"] or record["id"]!=frozen["id"] or record["designated_consumers"]!=frozen["designated_consumers"] or record["rejection_code"]!=frozen["rejection_code"] or type(record["survivor"]) is not bool or record["survivor"] is not False or type(record["observed"]) is not dict or sorted(record["observed"])!=sorted(frozen["designated_consumers"]):raise ValueError("mutation record")
  total+=len(record["designated_consumers"])
  for consumer in record["designated_consumers"]:
   observed=record["observed"][consumer]
   if sorted(observed)!=["exit","rejection_code"] or type(observed["exit"]) is not int or observed["exit"]!=2 or type(observed["rejection_code"]) is not str or observed["rejection_code"]!=frozen["rejection_code"]:raise ValueError("mutation observed")
 if total!=payload["consumer_invocation_count"]:raise ValueError("mutation count")
 external=load(output/"audits/external_auditor_mutations.json")
 if sorted(external)!=["candidate_id","payload","schema","status"] or external["schema"]!="paper47-external-auditor-mutations-v1" or external["status"]!="PASS":raise ValueError("external top")
 ep=external["payload"]
 if sorted(ep)!=["instance_count","records","survivors"] or type(ep["instance_count"]) is not int or ep["instance_count"]!=15 or type(ep["survivors"]) is not int or ep["survivors"]!=0 or type(ep["records"]) is not list or len(ep["records"])!=15:raise ValueError("external payload")
 for (name,code),row in zip(EXTERNAL_CASES,ep["records"]):
  if sorted(row)!=["id","observed_exit","rejection_code","survivor"] or row["id"]!=name or type(row["observed_exit"]) is not int or row["observed_exit"]!=2 or type(row["rejection_code"]) is not str or row["rejection_code"]!=code or type(row["survivor"]) is not bool or row["survivor"] is not False:raise ValueError("external row")
 expanded=load(output/"tests/expanded_mutation_results.json")
 if sorted(expanded)!=["candidate_id","payload","schema","status"] or expanded["candidate_id"]!="SD-C49" or expanded["schema"]!="paper47-expanded-mutation-results-v1" or expanded["status"]!="PASS":raise ValueError("expanded top")
 xp=expanded["payload"]
 if sorted(xp)!=["consumer_invocation_count","instance_count","records","survivors"] or type(xp["consumer_invocation_count"]) is not int or xp["consumer_invocation_count"]!=48 or type(xp["instance_count"]) is not int or xp["instance_count"]!=35 or type(xp["survivors"]) is not int or xp["survivors"]!=0 or type(xp["records"]) is not list or len(xp["records"])!=35:raise ValueError("expanded payload")
 targets=["D"]*8+["P"]*10+["X"]*4+["ROUTE"]*13
 operations=["set","set","set","set","set","set","set","set","set","set","set","set","set","set","set","add","set","set","set","delete","set","set","set","delete","set","delete","set","set","set","set","set","delete","set","set","set"]
 total=0
 for index,(row,target,operation) in enumerate(zip(xp["records"],targets,operations),1):
  consumers=["A"] if index<=22 else ["R1","R2"]
  if sorted(row)!=["consumers","id","operation","pointer","survivor","target"] or row["id"]!=f"N{index:02d}" or row["target"]!=target or row["operation"]!=operation or type(row["pointer"]) is not str or not row["pointer"].startswith("/") or ".." in row["pointer"] or type(row["survivor"]) is not bool or row["survivor"] is not False or type(row["consumers"]) is not dict or sorted(row["consumers"])!=consumers:raise ValueError("expanded record")
  for consumer in consumers:
   observed=row["consumers"][consumer];expected_exit=3 if consumer=="A" else 2;expected_rejection="A_ERROR:ValueError" if consumer=="A" else "ROUTE_TERMINAL_FAILURE" if index==30 else "PROVENANCE_STATE_FAILURE" if index>=33 else "ROUTE_FULL_OBJECT_FAILURE"
   if sorted(observed)!=["exit","rejection"] or type(observed["exit"]) is not int or observed["exit"]!=expected_exit or observed["rejection"]!=expected_rejection:raise ValueError("expanded observed")
  total+=len(consumers)
 if total!=xp["consumer_invocation_count"]:raise ValueError("expanded count")
def expected_paths(output:Path,state:str,phase:str)->None:
 if stat.S_IMODE(os.lstat(output).st_mode)!=0o755:raise ValueError("output root mode")
 actual=rows(output);file_rows=[x for x in actual if x["kind"]=="regular"];dir_rows=[x for x in actual if x["kind"]=="directory"]
 expected=[x for x in FILES if phase=="FINAL" or x!="audits/integrity_audit.json"]
 if state=="B" and phase=="FINAL":expected.append("PAPER_MANIFEST.sha256")
 if [x["path"] for x in file_rows]!=sorted(expected) or [x["path"] for x in dir_rows]!=sorted(DIRS):raise ValueError("namespace")
 if any(x["mode"]!="0644" for x in file_rows) or any(x["mode"]!="0755" for x in dir_rows):raise ValueError("mode")
def paper_rows(root:Path,output:Path)->list[dict[str,Any]]:
 out=[]
 for p in root.rglob("*"):
  rel=p.relative_to(root).as_posix()
  if rel=="outputs" or rel.startswith("outputs/") or rel=="PREOUTPUT_STATIC_SEAL.json":continue
  s=os.lstat(p);mode=f"{stat.S_IMODE(s.st_mode):04o}"
  if stat.S_ISLNK(s.st_mode):raise ValueError("paper symlink")
  if stat.S_ISDIR(s.st_mode):out.append({"kind":"directory","mode":mode,"path":rel})
  elif stat.S_ISREG(s.st_mode):out.append({"kind":"regular","mode":mode,"path":rel,"sha256":hashlib.sha256(p.read_bytes()).hexdigest()})
  else:raise ValueError("paper kind")
 for p in output.rglob("*"):
  rel=p.relative_to(output).as_posix()
  if rel=="PAPER_MANIFEST.sha256":continue
  s=os.lstat(p);mode=f"{stat.S_IMODE(s.st_mode):04o}";name="outputs/"+rel
  if stat.S_ISDIR(s.st_mode):out.append({"kind":"directory","mode":mode,"path":name})
  elif stat.S_ISREG(s.st_mode):out.append({"kind":"regular","mode":mode,"path":name,"sha256":hashlib.sha256(p.read_bytes()).hexdigest()})
  else:raise ValueError("paper output kind")
 return sorted(out,key=lambda x:x["path"])
def audit(root:Path,output:Path,state:str,commit:str|None,phase:str)->dict[str,Any]:
 expected_paths(output,state,phase)
 for p in output.rglob("*"):
  if p.is_file() and any(t in p.read_bytes() for t in HOST):raise ValueError("host token")
 if (output/"RESULT_LEDGER.json").read_bytes()!=ledger_bytes(output,state):raise ValueError("ledger reconstruction")
 required={"audits/external_auditor_mutations.json":"paper47-external-auditor-mutations-v1","audits/frozen_static_audit.json":"paper47-frozen-static-audit-v1","audits/independence_audit.json":"paper47-independence-audit-v1","audits/literature_audit.json":"paper47-literature-audit-v1","audits/proof_result_audit.json":"paper47-proof-result-audit-v1","audits/route_independent.json":"paper47-route-independent-audit-v1","audits/route_primary.json":"paper47-route-primary-audit-v1","audits/runtime_controls.json":"paper47-runtime-controls-v1","audits/source_audit.json":"paper47-source-audit-v1","audits/type_audit.json":"paper47-type-audit-v1","data/source_packet.json":"paper47-source-packet-v1","results/evaluator_d.json":"paper47-evaluator-d-v1","results/evaluator_p.json":"paper47-evaluator-p-v1","results/exact_comparison.json":"paper47-exact-comparison-v1","tests/expanded_mutation_results.json":"paper47-expanded-mutation-results-v1","tests/mutation_results.json":"paper47-mutation-results-v1"}
 for rel,schema in required.items():
  obj=load(output/rel)
  if obj.get("schema")!=schema or obj.get("status")!="PASS":raise ValueError("artifact contract")
 validate_mutation_objects(root,output)
 # PRE_CERT and FINAL both replay the four physical science/audit producers.
 replay_cwd=output.parent
 replay_d=invoke(root/"code/evaluator_d/evaluate.py",["--root",str(root)],replay_cwd)
 replay_p=invoke(root/"code/evaluator_p/evaluate.py",["--root",str(root)],replay_cwd)
 if replay_d!=(output/"results/evaluator_d.json").read_bytes() or replay_p!=(output/"results/evaluator_p.json").read_bytes():
  raise ValueError("D/P physical replay")
 replay_x=invoke(root/"code/comparator/exact_compare.py",
   ["--direct",str(output/"results/evaluator_d.json"),"--parameter",str(output/"results/evaluator_p.json")],replay_cwd)
 if replay_x!=(output/"results/exact_comparison.json").read_bytes():raise ValueError("X physical replay")
 replay_a=invoke(root/"code/auditors/proof_result_auditor.py",
   ["--root",str(root),"--direct",str(output/"results/evaluator_d.json"),
    "--parameter",str(output/"results/evaluator_p.json"),
    "--comparison",str(output/"results/exact_comparison.json")],replay_cwd)
 if replay_a!=(output/"audits/proof_result_audit.json").read_bytes():raise ValueError("A physical replay")
 replay_frozen=invoke(root/"external_auditor/frozen_auditor.py",["--root",str(root)],replay_cwd)
 if replay_frozen!=(output/"audits/frozen_static_audit.json").read_bytes():raise ValueError("frozen static physical replay")
 r1=load(output/"audits/route_primary.json");r2=load(output/"audits/route_independent.json")
 if r1["payload"]!=r2["payload"] or r1["payload"]["state"]!=state or sorted(r1["payload"])!=["artifact_manifest_sha256","full_normalized_route_sha256","route_sha256","state"] or any(re.fullmatch(r"[0-9a-f]{64}",r1["payload"][key]) is None for key in ("artifact_manifest_sha256","full_normalized_route_sha256","route_sha256")):raise ValueError("route audits")
 route_args=["--route",str(output/"evaluations/route_a/SD-C49/2026-08-18.json"),"--root",str(root),"--state",state]+(["--commit",str(commit)] if state=="B" else [])
 replay_r1=invoke(root/"code/route/validate_route.py",route_args,replay_cwd)
 replay_r2=invoke(root/"code/route/audit_route_independent.py",route_args,replay_cwd)
 if replay_r1!=(output/"audits/route_primary.json").read_bytes() or replay_r2!=(output/"audits/route_independent.json").read_bytes():raise ValueError("Route physical replay")
 report=subprocess.run([sys.executable,"-I","-B",str(root/"code/report/reconstruct_report.py"),"--output-root",str(output)],cwd=root.parent,env={"PATH":os.environ.get("PATH","/usr/bin:/bin"),"PYTHONDONTWRITEBYTECODE":"1","PYTHONPATH":str(root/"hostile-does-not-exist")},stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False,timeout=120)
 if report.returncode or report.stderr or report.stdout!=(output/"reports/EXPERIMENT_REPORT.md").read_bytes():raise ValueError("report reconstruction")
 runtime=load(output/"audits/runtime_controls.json")
 expected_runtime={"candidate_id":"SD-C49","payload":{"cli_exact_arity_control":True,"coordinated_full_state_mutations":21,"expanded_nested_mutations":35,"hostile_cwd_control":True,"hostile_pythonpath_control":True,"isolated_python_flags":["-I","-B"],"outside_sentinel_unchanged":True,"pre_io_component_symlink_control":True,"state_A_B_and_mixed_provenance_controls":True,"subprocess_timeout_seconds":120,"timeout_totalization":"SUBPROCESS_TIMEOUT"},"schema":"paper47-runtime-controls-v1","status":"PASS"}
 if runtime!=expected_runtime:raise ValueError("runtime control schema")
 pre=rows(output,{"audits/integrity_audit.json","PAPER_MANIFEST.sha256"})
 cert={"candidate_id":"SD-C49","payload":{"expected_paper_manifest":state=="B","ledger_sha256":hashlib.sha256((output/"RESULT_LEDGER.json").read_bytes()).hexdigest(),"pre_certificate_tree_sha256":hashlib.sha256(enc(pre)).hexdigest(),"route_sha256":r1["payload"]["route_sha256"],"state":state},"schema":"paper47-integrity-audit-v1","status":"PASS"}
 if phase=="FINAL":
  if (output/"audits/integrity_audit.json").read_bytes()!=enc(cert):raise ValueError("certificate reconstruction")
  if state=="A":
   if commit is not None or (output/"PAPER_MANIFEST.sha256").exists():raise ValueError("A provenance")
  else:
   if commit is None or re.fullmatch(r"[0-9a-f]{40}",commit) is None or commit=="0"*40:raise ValueError("B commit")
   pm=load(output/"PAPER_MANIFEST.sha256")
   if pm!={"exclude":["PREOUTPUT_STATIC_SEAL.json","outputs/PAPER_MANIFEST.sha256"],"rows":paper_rows(root,output),"schema":"paper47-state-b-paper-manifest-v1"}:raise ValueError("paper manifest")
 return cert
def main()->None:
 p=argparse.ArgumentParser(allow_abbrev=False);p.add_argument("--root",required=True);p.add_argument("--output-root",required=True);p.add_argument("--state",required=True,choices=["A","B"]);p.add_argument("--commit");p.add_argument("--phase",required=True,choices=["PRE_CERT","FINAL"]);a=p.parse_args()
 try:
  root=Path(a.root).resolve(strict=True);output=Path(a.output_root).resolve(strict=True);sys.stdout.buffer.write(enc(audit(root,output,a.state,a.commit,a.phase)))
 except Exception as e:sys.stderr.write(f"INTEGRITY_ERROR:{type(e).__name__}\n");raise SystemExit(3)
if __name__=="__main__":main()
