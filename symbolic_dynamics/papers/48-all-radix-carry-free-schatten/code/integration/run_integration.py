#!/usr/bin/env python3
"""Build twice, certify, and atomically install the exact Paper 48 outputs."""
from __future__ import annotations
import argparse,hashlib,json,os,re,shutil,signal,stat,subprocess,sys,tempfile
from pathlib import Path,PurePosixPath
from typing import Any

FILES=["EXPERIMENT_REPORT.md","evaluations/independent_evaluation.json","evaluations/main_evaluation.json","results/SHA256SUMS.txt","results/adversarial_tests.json","results/comparison.json","results/evaluator_a_native.json","results/evaluator_a_projection.json","results/evaluator_b_native.json","results/evaluator_b_projection.json","results/integrity_audit.json","results/mutation_outcomes.json","results/proof_audit.json"]
DIRS=["evaluations","results"]
MTIME=1787011200000000000
class Dup(Exception):pass
class Failure(Exception):
 def __init__(self,code):self.code=code
def pairs(seq):
 o={}
 for k,v in seq:
  if k in o:raise Dup(k)
  o[k]=v
 return o
def enc(v:Any)->bytes:return (json.dumps(v,sort_keys=True,indent=2,ensure_ascii=True,separators=(",",": "),allow_nan=False)+"\n").encode("ascii")
def load_bytes(raw:bytes):
 o=json.loads(raw.decode("ascii"),object_pairs_hook=pairs)
 if type(o) is not dict or raw!=enc(o):raise Failure("NONCANONICAL_SUBPROCESS")
 return o
def load(p):return load_bytes(Path(p).read_bytes())
def h(raw):return hashlib.sha256(raw).hexdigest()
def safe(root:Path,rel:str)->Path:
 p=PurePosixPath(rel)
 if type(rel) is not str or not rel or "\\" in rel or p.is_absolute() or any(x in ("",".","..") for x in p.parts):raise Failure("UNSAFE_PATH")
 node=root
 for part in p.parts:
  node=node/part
  if node.is_symlink():raise Failure("SYMLINK_COMPONENT")
 node=node.resolve(strict=True)
 if root not in node.parents or not node.is_file():raise Failure("STATIC_KIND")
 return node
def env(hostile:Path):return {"PATH":os.environ.get("PATH","/usr/bin:/bin"),"PYTHONPATH":str(hostile),"PYTHONDONTWRITEBYTECODE":"1","PYTHONHASHSEED":"0","LC_ALL":"C","LANG":"C"}
def invoke(root:Path,rel:str,args:list[str],cwd:Path,hostile:Path,timeout=300,canonical=True):
 q=subprocess.run([sys.executable,"-I","-B",str(safe(root,rel)),*args],cwd=cwd,env=env(hostile),stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False,timeout=timeout)
 if q.returncode!=0 or q.stderr:raise Failure("SUBPROCESS_"+Path(rel).stem.upper())
 if canonical:load_bytes(q.stdout)
 return q.stdout
def tree_rows(root:Path,exclude:set[str]|None=None):
 ex=exclude or set();out=[]
 for p in root.rglob("*"):
  rel=p.relative_to(root).as_posix()
  if rel in ex:continue
  s=os.lstat(p);mode=f"{stat.S_IMODE(s.st_mode):04o}"
  if stat.S_ISLNK(s.st_mode):raise Failure("TREE_SYMLINK")
  if stat.S_ISDIR(s.st_mode):out.append({"kind":"directory","mode":mode,"path":rel})
  elif stat.S_ISREG(s.st_mode):out.append({"kind":"regular","mode":mode,"path":rel,"sha256":h(p.read_bytes())})
  else:raise Failure("TREE_NONREGULAR")
 return sorted(out,key=lambda x:x["path"])
def snapshot(path:Path):
 if not path.exists() and not path.is_symlink():return {"exists":False}
 nodes=[path]+(sorted(path.rglob("*")) if path.is_dir() and not path.is_symlink() else [])
 rows=[]
 for p in nodes:
  s=os.lstat(p);kind="directory" if stat.S_ISDIR(s.st_mode) else "regular" if stat.S_ISREG(s.st_mode) else "symlink" if stat.S_ISLNK(s.st_mode) else "other"
  rows.append({"ctime_ns":s.st_ctime_ns,"dev":s.st_dev,"inode":s.st_ino,"kind":kind,"mode":stat.S_IMODE(s.st_mode),"mtime_ns":s.st_mtime_ns,"path":p.relative_to(path.parent).as_posix(),"sha256":h(p.read_bytes()) if kind=="regular" else None,"size":s.st_size})
 return {"exists":True,"rows":rows}
def validate_root(root:Path):
 if not root.is_absolute() or root.is_symlink() or not root.is_dir() or root.resolve(strict=True)!=root:raise Failure("ROOT_KIND")
 contract=load(root/"contracts/INTEGRATION_CONTRACT.json")
 if contract["declared_state_a_files"]!=FILES or contract["declared_output_directories"]!=DIRS:raise Failure("OUTPUT_CONTRACT")
 for p in root.rglob("*"):
  if "__pycache__" in p.parts or p.suffix in (".pyc",".pyo") or p.name in {".pytest_cache",".mypy_cache",".ruff_cache",".DS_Store"}:raise Failure("HYGIENE")
  s=os.lstat(p)
  if stat.S_ISLNK(s.st_mode) or not (stat.S_ISDIR(s.st_mode) or stat.S_ISREG(s.st_mode)):raise Failure("STATIC_KIND")
 target=root/"outputs"
 if target.exists() and (target.is_symlink() or not target.is_dir()):raise Failure("TARGET_KIND")
 manifest=load(root/"STATIC_TREE_MANIFEST.json");seal=load(root/"PREOUTPUT_STATIC_SEAL.json")
 if manifest["base_inventory_sha256"]!=seal["static_inventory_sha256"] or seal["status"]!="HOLD_FOR_INDEPENDENT_AUDIT":raise Failure("STATIC_SEAL")
 return manifest["base_inventory_sha256"]
def hostile_tree(build:Path):
 cwd=build/"hostile_cwd";modules=build/"hostile_modules";cwd.mkdir();modules.mkdir();(modules/"json.py").write_text("raise RuntimeError('shadow')\n",encoding="ascii");(modules/"sitecustomize.py").write_text("raise RuntimeError('startup')\n",encoding="ascii")
 naive=subprocess.run([sys.executable,"-c","import json"],cwd=cwd,env={"PATH":os.environ.get("PATH","/usr/bin:/bin"),"PYTHONPATH":str(modules)},stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False)
 isolated=subprocess.run([sys.executable,"-I","-B","-c","import json"],cwd=cwd,env={"PATH":os.environ.get("PATH","/usr/bin:/bin"),"PYTHONPATH":str(modules),"PYTHONDONTWRITEBYTECODE":"1"},stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False)
 if naive.returncode==0 or isolated.returncode!=0:raise Failure("HOSTILE_ISOLATION")
 return cwd,modules
def write(out:Path,rel:str,raw:bytes):
 p=out.joinpath(*PurePosixPath(rel).parts);p.parent.mkdir(parents=True,exist_ok=True)
 if p.exists() or p.is_symlink():raise Failure("STAGE_OVERWRITE")
 p.write_bytes(raw);p.chmod(0o644)
def launch_lane(root:Path,build:Path,lane:str,cwd:Path,hostile:Path):
 directory=build/("lane_"+lane.lower());directory.mkdir();projection=directory/"projection.json";native=directory/"native.json";rel=f"code/evaluator_{lane.lower()}/evaluate.py"
 q=subprocess.Popen([sys.executable,"-I","-B",str(safe(root,rel)),"--root",str(root),"--projection",str(projection),"--native",str(native)],cwd=cwd,env=env(hostile),stdout=subprocess.PIPE,stderr=subprocess.PIPE,start_new_session=True)
 return q,projection,native
def lanes(root:Path,build:Path,cwd:Path,hostile:Path):
 pa,ap,an=launch_lane(root,build,"A",cwd,hostile);pb,bp,bn=launch_lane(root,build,"B",cwd,hostile)
 try:
  ao,ae=pa.communicate(timeout=180);bo,be=pb.communicate(timeout=180)
 except subprocess.TimeoutExpired:
  for p in (pa,pb):
   if p.poll() is None:os.killpg(p.pid,signal.SIGKILL)
   p.communicate()
  raise Failure("EVALUATOR_TIMEOUT")
 if pa.returncode or pb.returncode or ao or bo or ae or be:raise Failure("EVALUATOR_FAILURE")
 for p in (ap,an,bp,bn):
  if p.is_symlink() or not p.is_file():raise Failure("EVALUATOR_OUTPUT")
  load(p)
 return ap,an,bp,bn
def result_manifest(out:Path):
 names=sorted(x for x in FILES if x!="results/SHA256SUMS.txt")
 return ("\n".join(f"{h((out/name).read_bytes())}  {name}" for name in names)+"\n").encode("ascii")
def paper_rows(root:Path,out:Path):
 result=[]
 for p in root.rglob("*"):
  rel=p.relative_to(root).as_posix()
  if rel in {"STATIC_TREE_MANIFEST.json","PREOUTPUT_STATIC_SEAL.json","outputs"} or rel.startswith("outputs/"):continue
  s=os.lstat(p);mode=f"{stat.S_IMODE(s.st_mode):04o}"
  if stat.S_ISDIR(s.st_mode):result.append({"kind":"directory","mode":mode,"path":rel})
  elif stat.S_ISREG(s.st_mode):result.append({"kind":"regular","mode":mode,"path":rel,"sha256":h(p.read_bytes())})
  else:raise Failure("PAPER_KIND")
 for p in out.rglob("*"):
  rel="outputs/"+p.relative_to(out).as_posix()
  if rel=="outputs/PAPER_MANIFEST.sha256":continue
  s=os.lstat(p);mode=f"{stat.S_IMODE(s.st_mode):04o}"
  if stat.S_ISDIR(s.st_mode):result.append({"kind":"directory","mode":mode,"path":rel})
  elif stat.S_ISREG(s.st_mode):result.append({"kind":"regular","mode":mode,"path":rel,"sha256":h(p.read_bytes())})
  else:raise Failure("PAPER_OUTPUT_KIND")
 return sorted(result,key=lambda x:x["path"])
def validate_prepared(path:Path,kind:str,root:Path):
 if path.is_symlink() or not path.is_file() or Path("/tmp") not in path.resolve(strict=True).parents:raise Failure("PREPARED_KIND")
 raw=path.read_bytes();o=load_bytes(raw)
 if kind=="mutations":
  if o.get("status")!="PASS" or o.get("mutation_instances")!=39 or o.get("designated_consumer_invocations")!=68 or o.get("nondesignated_acceptances")!=322 or o.get("survivors")!=0 or o.get("registry_sha256")!=h((root/"preauthority/MUTATION_REGISTRY.json").read_bytes()):raise Failure("PREPARED_MUTATIONS")
 else:
  if o.get("status")!="PASS" or o.get("survivors")!=0 or o.get("physical_instances",0)<20:raise Failure("PREPARED_ADVERSARIAL")
 return raw
def build_once(root:Path,build:Path,state:str,static:str,commit:str|None,mutation_raw:bytes,adversarial_raw:bytes):
 out=build/"outputs";out.mkdir(mode=0o755);(out/"evaluations").mkdir();(out/"results").mkdir();cwd,hostile=hostile_tree(build)
 ap,an,bp,bn=lanes(root,build,cwd,hostile)
 write(out,"results/evaluator_a_projection.json",ap.read_bytes());write(out,"results/evaluator_a_native.json",an.read_bytes());write(out,"results/evaluator_b_projection.json",bp.read_bytes());write(out,"results/evaluator_b_native.json",bn.read_bytes())
 comparison=invoke(root,"code/comparator/compare.py",["--root",str(root),"--a",str(out/"results/evaluator_a_projection.json"),"--b",str(out/"results/evaluator_b_projection.json")],cwd,hostile);write(out,"results/comparison.json",comparison)
 proof=invoke(root,"code/proof_auditor/audit.py",["--root",str(root),"--a",str(out/"results/evaluator_a_projection.json"),"--b",str(out/"results/evaluator_b_projection.json")],cwd,hostile);write(out,"results/proof_audit.json",proof)
 for rel,args in (("code/auditors/source_auditor.py",["--root",str(root)]),("code/auditors/type_auditor.py",["--root",str(root)]),("code/auditors/independence_auditor.py",["--root",str(root)]+(["--allow-outputs"] if (root/"outputs").exists() else [])),("code/integration/audit_integrity.py",["--root",str(root),"--preflight"])):
  obj=load_bytes(invoke(root,rel,args,cwd,hostile));
  if obj.get("status")!="PASS":raise Failure("PREFLIGHT_AUDIT")
 write(out,"results/mutation_outcomes.json",mutation_raw);write(out,"results/adversarial_tests.json",adversarial_raw)
 route_args=["--root",str(root),"--state",state,"--static-digest",static]+(["--commit",str(commit)] if commit else [])
 route=invoke(root,"code/route/render_route.py",route_args,cwd,hostile);route_path=build/"route.json";route_path.write_bytes(route)
 validator_args=["--root",str(root),"--route",str(route_path),"--state",state,"--static-digest",static]+(["--commit",str(commit)] if commit else [])
 write(out,"evaluations/main_evaluation.json",invoke(root,"code/route/validate_route.py",validator_args,cwd,hostile));write(out,"evaluations/independent_evaluation.json",invoke(root,"code/route/audit_route_independent.py",validator_args,cwd,hostile))
 report=invoke(root,"code/report/reconstruct_report.py",["--output-root",str(out),"--state",state],cwd,hostile,canonical=False);report.decode("ascii");write(out,"EXPERIMENT_REPORT.md",report)
 integrity_args=["--root",str(root),"--output-root",str(out),"--state",state,"--phase","PRE_CERT","--static-digest",static]+(["--commit",str(commit)] if commit else [])
 integrity=invoke(root,"code/integration/audit_integrity.py",integrity_args,cwd,hostile);write(out,"results/integrity_audit.json",integrity);write(out,"results/SHA256SUMS.txt",result_manifest(out))
 if state=="B":write(out,"PAPER_MANIFEST.sha256",enc({"exclude":["PREOUTPUT_STATIC_SEAL.json","STATIC_TREE_MANIFEST.json","outputs/PAPER_MANIFEST.sha256"],"rows":paper_rows(root,out),"schema":"paper48.state-b-paper-manifest.v1"}))
 final_args=["--root",str(root),"--output-root",str(out),"--state",state,"--phase","FINAL","--static-digest",static]+(["--commit",str(commit)] if commit else [])
 if invoke(root,"code/integration/audit_integrity.py",final_args,cwd,hostile)!=integrity:raise Failure("PRE_CERT_FINAL_MISMATCH")
 type_result=load_bytes(invoke(root,"code/auditors/type_auditor.py",["--root",str(root),"--output-root",str(out)],cwd,hostile,timeout=300))
 if type_result.get("projection_rows_validated")!=3930:raise Failure("RESULT_TYPES")
 rebuilt=invoke(root,"code/report/reconstruct_report.py",["--output-root",str(out),"--state",state],cwd,hostile,canonical=False)
 if rebuilt!=(out/"EXPERIMENT_REPORT.md").read_bytes():raise Failure("REPORT_RECONSTRUCTION")
 expected=sorted(FILES+(["PAPER_MANIFEST.sha256"] if state=="B" else []));actual=[x["path"] for x in tree_rows(out) if x["kind"]=="regular"]
 if actual!=expected:raise Failure("FINAL_NAMESPACE")
 for p in sorted(out.rglob("*"),reverse=True):
  if p.is_file():p.chmod(0o644);os.utime(p,ns=(MTIME,MTIME))
  elif p.is_dir():p.chmod(0o755);os.utime(p,ns=(MTIME,MTIME))
 out.chmod(0o755);os.utime(out,ns=(MTIME,MTIME));return out
def prepare(root:Path,temp:Path,state:str,static:str,commit:str|None,pm:Path|None,pa:Path|None):
 cwd,hostile=hostile_tree(temp/"preparation")
 if pm:mutation=validate_prepared(pm,"mutations",root)
 else:mutation=invoke(root,"code/tests/run_mutations.py",["--root",str(root),"--scratch",str(temp/"mutation_scratch")],cwd,hostile,timeout=900)
 if pa:adversarial=validate_prepared(pa,"adversarial",root)
 else:
  args=["--root",str(root),"--scratch",str(temp/"adversarial_scratch"),"--state",state,"--static-digest",static]+(["--commit",str(commit)] if commit else [])
  adversarial=invoke(root,"code/tests/run_adversarial.py",args,cwd,hostile,timeout=600)
 return mutation,adversarial
def main():
 p=argparse.ArgumentParser(allow_abbrev=False);p.add_argument("--root",type=Path,required=True);p.add_argument("--state",choices=["A","B"],required=True);p.add_argument("--commit");p.add_argument("--force-late-failure",action="store_true");p.add_argument("--prepared-mutations",type=Path);p.add_argument("--prepared-adversarial",type=Path)
 temp=None
 try:
  a=p.parse_args();root=a.root.resolve(strict=True)
  if a.state=="A" and a.commit is not None:raise Failure("A_COMMIT_FORBIDDEN")
  if a.state=="B" and (a.commit is None or re.fullmatch(r"[0-9a-f]{40}",a.commit) is None or a.commit=="0"*40):raise Failure("B_COMMIT_REQUIRED")
  static=validate_root(root);target=root/"outputs";before_target=snapshot(target);before_root=snapshot(root)
  temp=Path(tempfile.mkdtemp(prefix=".p48-transaction-",dir=root.parent));(temp/"preparation").mkdir();mutation,adversarial=prepare(root,temp,a.state,static,a.commit,a.prepared_mutations,a.prepared_adversarial)
  b1=Path(tempfile.mkdtemp(prefix="build-one-",dir=temp));b2=Path(tempfile.mkdtemp(prefix="build-two-",dir=temp));o1=build_once(root,b1,a.state,static,a.commit,mutation,adversarial);o2=build_once(root,b2,a.state,static,a.commit,mutation,adversarial)
  if tree_rows(o1)!=tree_rows(o2):raise Failure("DOUBLE_BUILD_MISMATCH")
  digest=h(enc(tree_rows(o1)))
  if a.force_late_failure:
   if snapshot(target)!=before_target or snapshot(root)!=before_root:raise Failure("LATE_FAILURE_IDENTITY")
   sys.stdout.buffer.write(enc({"candidate_id":"SD-C50","final_tree_sha256":digest,"physical_target_replacements":0,"schema":"paper48.integration-run.v1","state":a.state,"status":"FORCED_LATE_FAILURE"}));return 86
  if target.exists():
   if tree_rows(target)!=tree_rows(o1):raise Failure("PREEXISTING_TARGET_DIFFERENT")
   if snapshot(target)!=before_target or snapshot(root)!=before_root:raise Failure("IDEMPOTENT_METADATA_DRIFT")
   replacements=0
  else:
   os.replace(o1,target);replacements=1
  sys.stdout.buffer.write(enc({"candidate_id":"SD-C50","final_tree_sha256":digest,"physical_target_replacements":replacements,"schema":"paper48.integration-run.v1","state":a.state,"status":"PASS"}));return 0
 except Failure as e:sys.stderr.write("INTEGRATION_ERROR:"+e.code+"\n");return 3
 except Exception as e:sys.stderr.write(f"INTEGRATION_ERROR:{type(e).__name__}\n");return 3
 finally:
  if temp is not None and temp.exists():shutil.rmtree(temp)
if __name__=="__main__":raise SystemExit(main())
