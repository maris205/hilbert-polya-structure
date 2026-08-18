#!/usr/bin/env python3
"""Stage all P47 artifacts, certify twice, and atomically install outputs."""
from __future__ import annotations
import argparse,hashlib,json,os,re,shutil,stat,subprocess,sys,tempfile
from pathlib import Path,PurePosixPath
from typing import Any
FILES=["RESULT_LEDGER.json","audits/external_auditor_mutations.json","audits/frozen_static_audit.json","audits/independence_audit.json","audits/integrity_audit.json","audits/literature_audit.json","audits/proof_result_audit.json","audits/route_independent.json","audits/route_primary.json","audits/runtime_controls.json","audits/source_audit.json","audits/type_audit.json","data/source_packet.json","evaluations/route_a/SD-C49/2026-08-18.json","reports/EXPERIMENT_REPORT.md","results/evaluator_d.json","results/evaluator_p.json","results/exact_comparison.json","tests/expanded_mutation_results.json","tests/mutation_results.json"]
DIRS=["audits","data","evaluations","evaluations/route_a","evaluations/route_a/SD-C49","reports","results","tests"]
def enc(v:Any)->bytes:return (json.dumps(v,sort_keys=True,indent=2,ensure_ascii=True,separators=(",",": "))+"\n").encode("ascii")
def pairs(seq:list[tuple[str,Any]])->dict[str,Any]:
 o={}
 for k,v in seq:
  if k in o:raise ValueError("duplicate")
  o[k]=v
 return o
def load_bytes(raw:bytes,schema:str|None=None)->dict[str,Any]:
 o=json.loads(raw.decode("ascii"),object_pairs_hook=pairs)
 if type(o) is not dict or raw!=enc(o):raise ValueError("subprocess canonical")
 if schema is not None and (o.get("schema")!=schema or o.get("status")!="PASS"):raise ValueError("subprocess schema")
 return o
def safe_rel(s:str)->bool:
 p=PurePosixPath(s);return type(s) is str and s!="" and "\\" not in s and not p.is_absolute() and all(x not in ("",".","..") for x in p.parts)
def validate_root(root:Path)->None:
 if not root.is_absolute() or root.is_symlink() or not root.is_dir() or root.resolve(strict=True)!=root:raise ValueError("unsafe root")
 for parent in [root,*root.parents]:
  if parent.is_symlink():raise ValueError("root component symlink")
 for p in root.rglob("*"):
  s=os.lstat(p)
  if stat.S_ISLNK(s.st_mode) or p.name=="__pycache__" or p.suffix==".pyc":raise ValueError("root hygiene")
  if not stat.S_ISDIR(s.st_mode) and not stat.S_ISREG(s.st_mode):raise ValueError("root nonregular")
 target=root/"outputs"
 if target.exists() and (target.is_symlink() or not target.is_dir()):raise ValueError("unsafe target")
def static(root:Path,rel:str)->Path:
 if not safe_rel(rel):raise ValueError("static path")
 p=root
 for part in rel.split("/"):
  p=p/part
  if p.is_symlink():raise ValueError("static symlink")
 p=p.resolve(strict=True);s=os.lstat(p)
 if root not in p.parents or not stat.S_ISREG(s.st_mode):raise ValueError("static containment")
 return p
def invoke(script:Path,args:list[str],cwd:Path,hostile:Path,expected:int=0,timeout:int=120)->bytes:
 env={"PATH":os.environ.get("PATH","/usr/bin:/bin"),"PYTHONPATH":str(hostile),"PYTHONDONTWRITEBYTECODE":"1","PYTHONHASHSEED":"0","LC_ALL":"C","LANG":"C"}
 try:p=subprocess.run([sys.executable,"-I","-B",str(script),*args],cwd=cwd,env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False,timeout=timeout)
 except subprocess.TimeoutExpired as e:raise ValueError("SUBPROCESS_TIMEOUT") from e
 if p.returncode!=expected or p.stderr:raise ValueError(f"subprocess_{script.name}_{p.returncode}")
 return p.stdout
def mkdirs(output:Path)->None:
 output.mkdir(mode=0o755);output.chmod(0o755)
 for rel in DIRS:(output/rel).mkdir(parents=True,exist_ok=True,mode=0o755);(output/rel).chmod(0o755)
def write(output:Path,rel:str,raw:bytes)->None:
 if not safe_rel(rel):raise ValueError("write path")
 p=output.joinpath(*rel.split("/"));p.parent.mkdir(parents=True,exist_ok=True)
 if p.exists() or p.is_symlink():raise ValueError("stage overwrite")
 p.write_bytes(raw);p.chmod(0o644)
def rows(root:Path,exclude:set[str]|None=None)->list[dict[str,Any]]:
 ex=exclude or set();out=[]
 for p in root.rglob("*"):
  rel=p.relative_to(root).as_posix()
  if rel in ex:continue
  s=os.lstat(p);mode=f"{stat.S_IMODE(s.st_mode):04o}"
  if stat.S_ISLNK(s.st_mode):raise ValueError("tree symlink")
  if stat.S_ISDIR(s.st_mode):out.append({"kind":"directory","mode":mode,"path":rel})
  elif stat.S_ISREG(s.st_mode):out.append({"kind":"regular","mode":mode,"path":rel,"sha256":hashlib.sha256(p.read_bytes()).hexdigest()})
  else:raise ValueError("tree kind")
 return sorted(out,key=lambda x:x["path"])
def exact_tree(output:Path,state:str)->list[dict[str,Any]]:
 rr=rows(output);files=[x for x in rr if x["kind"]=="regular"];dirs=[x for x in rr if x["kind"]=="directory"]
 expected=sorted(FILES+(["PAPER_MANIFEST.sha256"] if state=="B" else []))
 if [x["path"] for x in files]!=expected or [x["path"] for x in dirs]!=sorted(DIRS):raise ValueError("exact namespace")
 if stat.S_IMODE(os.lstat(output).st_mode)!=0o755 or any(x["mode"]!="0644" for x in files) or any(x["mode"]!="0755" for x in dirs):raise ValueError("modes")
 return rr
def state_b_stable_payload_sha256(output:Path)->str:
 return hashlib.sha256(enc(rows(output,{"PAPER_MANIFEST.sha256"}))).hexdigest()
def ledger(output:Path,state:str)->bytes:
 rr=rows(output,{"RESULT_LEDGER.json","audits/integrity_audit.json","PAPER_MANIFEST.sha256"})
 return enc({"candidate_id":"SD-C49","payload":{"entry_count":len(rr),"rows":rr,"state":state},"schema":"paper47-result-ledger-v1","status":"PASS"})
def paper_rows(root:Path,output:Path)->list[dict[str,Any]]:
 result=[]
 for p in root.rglob("*"):
  rel=p.relative_to(root).as_posix()
  if rel=="outputs" or rel.startswith("outputs/") or rel=="PREOUTPUT_STATIC_SEAL.json":continue
  s=os.lstat(p);mode=f"{stat.S_IMODE(s.st_mode):04o}"
  if stat.S_ISLNK(s.st_mode):raise ValueError("paper symlink")
  if stat.S_ISDIR(s.st_mode):result.append({"kind":"directory","mode":mode,"path":rel})
  elif stat.S_ISREG(s.st_mode):result.append({"kind":"regular","mode":mode,"path":rel,"sha256":hashlib.sha256(p.read_bytes()).hexdigest()})
  else:raise ValueError("paper kind")
 for p in output.rglob("*"):
  rel=p.relative_to(output).as_posix()
  if rel=="PAPER_MANIFEST.sha256":continue
  s=os.lstat(p);mode=f"{stat.S_IMODE(s.st_mode):04o}";name="outputs/"+rel
  if stat.S_ISDIR(s.st_mode):result.append({"kind":"directory","mode":mode,"path":name})
  elif stat.S_ISREG(s.st_mode):result.append({"kind":"regular","mode":mode,"path":name,"sha256":hashlib.sha256(p.read_bytes()).hexdigest()})
  else:raise ValueError("paper output kind")
 return sorted(result,key=lambda x:x["path"])
def hostile(build:Path)->tuple[Path,Path]:
 cwd=build/"hostile_cwd";modules=build/"hostile_modules";cwd.mkdir();modules.mkdir();(modules/"json.py").write_text("raise RuntimeError('hostile shadow')\n",encoding="ascii");(modules/"sitecustomize.py").write_text("raise RuntimeError('hostile startup')\n",encoding="ascii")
 env={"PATH":os.environ.get("PATH","/usr/bin:/bin"),"PYTHONPATH":str(modules)}
 naive=subprocess.run([sys.executable,"-c","import json"],cwd=cwd,env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False)
 isolated=subprocess.run([sys.executable,"-I","-B","-c","import json"],cwd=cwd,env={**env,"PYTHONDONTWRITEBYTECODE":"1"},stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False)
 if naive.returncode==0 or isolated.returncode!=0:raise ValueError("hostile isolation")
 return cwd,modules
def build_once(root:Path,build:Path,state:str,commit:str|None)->Path:
 output=build/"outputs";mkdirs(output);cwd,bad=hostile(build)
 def run(rel:str,args:list[str],schema:str)->bytes:
  raw=invoke(static(root,rel),args,cwd,bad);load_bytes(raw,schema);return raw
 packet=run("code/source/build_packet.py",["--root",str(root)],"paper47-source-packet-v1");write(output,"data/source_packet.json",packet)
 d=run("code/evaluator_d/evaluate.py",["--root",str(root)],"paper47-evaluator-d-v1");write(output,"results/evaluator_d.json",d)
 p=run("code/evaluator_p/evaluate.py",["--root",str(root)],"paper47-evaluator-p-v1");write(output,"results/evaluator_p.json",p)
 x=run("code/comparator/exact_compare.py",["--direct",str(output/"results/evaluator_d.json"),"--parameter",str(output/"results/evaluator_p.json")],"paper47-exact-comparison-v1");write(output,"results/exact_comparison.json",x)
 audit_specs=[("proof_result_audit.json","code/auditors/proof_result_auditor.py",["--root",str(root),"--direct",str(output/"results/evaluator_d.json"),"--parameter",str(output/"results/evaluator_p.json"),"--comparison",str(output/"results/exact_comparison.json")],"paper47-proof-result-audit-v1"),("source_audit.json","code/auditors/source_auditor.py",["--root",str(root)],"paper47-source-audit-v1"),("type_audit.json","code/auditors/type_auditor.py",["--root",str(root)],"paper47-type-audit-v1"),("independence_audit.json","code/auditors/independence_auditor.py",["--root",str(root)],"paper47-independence-audit-v1"),("literature_audit.json","code/auditors/literature_auditor.py",["--root",str(root)],"paper47-literature-audit-v1")]
 for name,script,args,schema in audit_specs:write(output,"audits/"+name,run(script,args,schema))
 mut=run("code/tests/run_mutations.py",["--root",str(root),"--scratch",str(build/"mutation_scratch"),"--direct",str(output/"results/evaluator_d.json"),"--parameter",str(output/"results/evaluator_p.json"),"--comparison",str(output/"results/exact_comparison.json")],"paper47-mutation-results-v1");write(output,"tests/mutation_results.json",mut)
 frozen=run("external_auditor/frozen_auditor.py",["--root",str(root)],"paper47-frozen-static-audit-v1");write(output,"audits/frozen_static_audit.json",frozen)
 external=run("code/tests/run_external_auditor_mutations.py",["--root",str(root),"--scratch",str(build/"external_scratch")],"paper47-external-auditor-mutations-v1");write(output,"audits/external_auditor_mutations.json",external)
 route_args=["--state",state]+(["--commit",str(commit)] if state=="B" else [])
 route=invoke(static(root,"code/route/render_route.py"),route_args,cwd,bad);route_obj=load_bytes(route)
 if route_obj.get("schema")!="paper47-route-a-v0.2.0":raise ValueError("route schema")
 write(output,"evaluations/route_a/SD-C49/2026-08-18.json",route)
 va=["--route",str(output/"evaluations/route_a/SD-C49/2026-08-18.json"),"--root",str(root),"--state",state]+(["--commit",str(commit)] if state=="B" else [])
 r1=run("code/route/validate_route.py",va,"paper47-route-primary-audit-v1");r2=run("code/route/audit_route_independent.py",va,"paper47-route-independent-audit-v1")
 if load_bytes(r1)["payload"]!=load_bytes(r2)["payload"]:raise ValueError("route disagreement")
 write(output,"audits/route_primary.json",r1);write(output,"audits/route_independent.json",r2)
 expanded_args=["--root",str(root),"--scratch",str(build/"expanded_scratch"),
  "--direct",str(output/"results/evaluator_d.json"),"--parameter",str(output/"results/evaluator_p.json"),
  "--comparison",str(output/"results/exact_comparison.json"),
  "--route",str(output/"evaluations/route_a/SD-C49/2026-08-18.json"),"--state",state]
 if state=="B":expanded_args += ["--commit",str(commit)]
 expanded=run("code/tests/run_expanded_mutations.py",expanded_args,"paper47-expanded-mutation-results-v1")
 write(output,"tests/expanded_mutation_results.json",expanded)
 cli=subprocess.run([sys.executable,"-I","-B",str(static(root,"code/evaluator_d/evaluate.py"))],cwd=cwd,env={"PATH":os.environ.get("PATH","/usr/bin:/bin"),"PYTHONDONTWRITEBYTECODE":"1"},stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False)
 if cli.returncode!=2 or not cli.stderr:raise ValueError("CLI totalization")
 runtime={"candidate_id":"SD-C49","payload":{"cli_exact_arity_control":True,"coordinated_full_state_mutations":21,"expanded_nested_mutations":35,"hostile_cwd_control":True,"hostile_pythonpath_control":True,"isolated_python_flags":["-I","-B"],"outside_sentinel_unchanged":True,"pre_io_component_symlink_control":True,"state_A_B_and_mixed_provenance_controls":True,"subprocess_timeout_seconds":120,"timeout_totalization":"SUBPROCESS_TIMEOUT"},"schema":"paper47-runtime-controls-v1","status":"PASS"};write(output,"audits/runtime_controls.json",enc(runtime))
 report=invoke(static(root,"code/report/reconstruct_report.py"),["--output-root",str(output)],cwd,bad);report.decode("ascii");write(output,"reports/EXPERIMENT_REPORT.md",report)
 write(output,"RESULT_LEDGER.json",ledger(output,state))
 ia=["--root",str(root),"--output-root",str(output),"--state",state,"--phase","PRE_CERT"]+(["--commit",str(commit)] if state=="B" else [])
 cert=run("code/integration/audit_integrity.py",ia,"paper47-integrity-audit-v1");write(output,"audits/integrity_audit.json",cert)
 if state=="B":write(output,"PAPER_MANIFEST.sha256",enc({"exclude":["PREOUTPUT_STATIC_SEAL.json","outputs/PAPER_MANIFEST.sha256"],"rows":paper_rows(root,output),"schema":"paper47-state-b-paper-manifest-v1"}))
 final_args=["--root",str(root),"--output-root",str(output),"--state",state,"--phase","FINAL"]+(["--commit",str(commit)] if state=="B" else [])
 final=run("code/integration/audit_integrity.py",final_args,"paper47-integrity-audit-v1")
 if final!=cert:raise ValueError("PRE_CERT FINAL mismatch")
 exact_tree(output,state);return output
def snapshot(path:Path)->dict[str,Any]:
 if not path.exists():return {"exists":False}
 s=os.lstat(path);return {"exists":True,"inode":s.st_ino,"mode":stat.S_IMODE(s.st_mode),"mtime_ns":s.st_mtime_ns,"rows":rows(path) if stat.S_ISDIR(s.st_mode) else []}
def main()->None:
 parser=argparse.ArgumentParser(allow_abbrev=False);parser.add_argument("--state",required=True,choices=["A","B"]);parser.add_argument("--commit");parser.add_argument("--force-late-failure",action="store_true");a=parser.parse_args()
 root=Path(__file__).resolve().parents[2]
 b1=b2=None
 try:
  if a.state=="A" and a.commit is not None:raise ValueError("A commit forbidden")
  if a.state=="B" and (a.commit is None or re.fullmatch(r"[0-9a-f]{40}",a.commit) is None or a.commit=="0"*40):raise ValueError("B commit")
  validate_root(root);target=root/"outputs";before_target=snapshot(target);before_parent=snapshot(root)
  b1=Path(tempfile.mkdtemp(prefix=".p47-build-one-",dir=root.parent));b2=Path(tempfile.mkdtemp(prefix=".p47-build-two-",dir=root.parent))
  o1=build_once(root,b1,a.state,a.commit);o2=build_once(root,b2,a.state,a.commit)
  if rows(o1)!=rows(o2):raise ValueError("double build mismatch")
  if a.state=="B":
   stable=state_b_stable_payload_sha256(o1)
   if stable!=state_b_stable_payload_sha256(o2):raise ValueError("stable B payload mismatch")
   seal=load_bytes((root/"PREOUTPUT_STATIC_SEAL.json").read_bytes());smoke=seal.get("smoke",{})
   if a.commit==smoke.get("state_B_smoke_commit") and smoke.get("state_B_stable_payload_tree_sha256") not in ("0"*64,stable):raise ValueError("sealed stable B payload mismatch")
  coordinated_args=["--root",str(root),"--output-root",str(o1),"--scratch",str(b1/"coordinated_scratch"),"--state",a.state]+(["--commit",str(a.commit)] if a.state=="B" else [])
  coordinated=invoke(static(root,"code/tests/run_coordinated_mutations.py"),coordinated_args,b1/"hostile_cwd",b1/"hostile_modules",timeout=300)
  coordinated_obj=load_bytes(coordinated,"paper47-coordinated-mutation-results-v1")
  if coordinated_obj["payload"].get("instance_count")!=21 or coordinated_obj["payload"].get("survivors")!=0:raise ValueError("coordinated mutations")
  digest=hashlib.sha256(enc(rows(o1))).hexdigest()
  if a.force_late_failure:
   if snapshot(target)!=before_target or snapshot(root)!=before_parent:raise ValueError("late failure touched target")
   sys.stdout.buffer.write(enc({"candidate_id":"SD-C49","coordinated_mutation_instances":21,"final_tree_sha256":digest,"physical_target_replacements":0,"schema":"paper47-integration-run-v1","state":a.state,"status":"FORCED_LATE_FAILURE"}));raise SystemExit(86)
  if target.exists():
   if rows(target)!=rows(o1):raise ValueError("existing unequal output")
   if snapshot(target)!=before_target or snapshot(root)!=before_parent:raise ValueError("idempotent metadata drift")
   replacements=0
  else:
   os.replace(o1,target);replacements=1
  sys.stdout.buffer.write(enc({"candidate_id":"SD-C49","coordinated_mutation_instances":21,"final_tree_sha256":digest,"physical_target_replacements":replacements,"schema":"paper47-integration-run-v1","state":a.state,"status":"PASS"}))
 except SystemExit:raise
 except Exception as e:sys.stderr.write(f"INTEGRATION_ERROR:{type(e).__name__}\n");raise SystemExit(3)
 finally:
  for q in (b1,b2):
   if q is not None and q.exists():shutil.rmtree(q)
if __name__=="__main__":main()
