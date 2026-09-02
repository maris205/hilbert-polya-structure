#!/usr/bin/env python3
"""Close or verify the exact 27-payload HCS-C314 release."""
from __future__ import annotations
import argparse,hashlib,json,os,re,shutil,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];MANIFEST=ROOT/"C314_RELEASE_MANIFEST.json";EVIDENCE=ROOT/"results/c314_angenent_evidence.json";EVALUATION=ROOT/"evaluations/route_a/HCS-C314/2026-09-03.yaml";TEX=ROOT/"paper/main.tex";PDF=ROOT/"paper/main.pdf";EPOCH=1788393600;SOURCE="1938bae19e5a92f9ce2411aafdc68323bd641bd0";SCOPE="NO_BAD_EULER_OR_ROOT_NUMBER";EVAL_RAW="fdcfeb38069d8a86730b28cc5bcb8aee314bcddffb9eaf3652912fdef7590dd2";EVAL_SEMANTIC="3693ad2d8e0832465ea07701c94cfc55df176c1b74d9f9a2347931578564e4c2";ROUNDS=[ROOT/f"paper/main_round{i}{'_original' if i==0 else ''}.pdf" for i in range(3)];WARNING=re.compile(r"(?:LaTeX|Package [^:\n]+) Warning:|Overfull|Underfull|undefined (?:references|citations)|Rerun to get|Missing character")
EXPECTED={"EXPERIMENT_PLAN.md","NARRATIVE_REPORT.md","PAPER_IMPROVEMENT_LOG.md","PAPER_PLAN.md","README.md","RESEARCH_QUESTION.md","SOURCE_AUDIT.md","THEOREM_PACKAGE.md","code/README.md","code/c314_release_manifest.py","code/c314_angenent_checker.py","code/c314_angenent_mutation.py","code/c314_angenent_producer.py","code/c314_angenent_replay.py","code/c314_angenent_sympy_crosscheck.py","evaluations/route_a/HCS-C314/2026-09-03.yaml","paper/COMPILE_REPORT.md","paper/README.md","paper/main.pdf","paper/main.tex","paper/main_round0_original.pdf","paper/main_round1.pdf","paper/main_round2.pdf","results/HOSTILE_AUDIT.md","results/RESULTS.md","results/TEST_REPORT.md","results/c314_angenent_evidence.json"}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(n,opt=False):
 env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1",TZ="UTC");return subprocess.run([sys.executable,"-O" if opt else "-B",str(ROOT/"code"/n)],env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
def pages(p):return int(next(x.split(":",1)[1] for x in subprocess.check_output(["pdfinfo",str(p)],text=True).splitlines() if x.startswith("Pages:")))
def fonts(p):
 rows=[x for x in subprocess.check_output(["pdffonts",str(p)],text=True).splitlines()[2:] if x.strip() and not x.lstrip().startswith("-")]
 if not rows or not all(len(x.split())>=7 and x.split()[-5]=="yes" and x.split()[-4]=="yes" for x in rows):raise AssertionError("fonts")
 return len(rows)
def ptext(p):return " ".join(subprocess.check_output(["pdftotext","-layout",str(p),"-"],text=True).lower().split())
def raster(p,n):
 out=[]
 with tempfile.TemporaryDirectory(prefix="c314-raster-") as t:
  for i in range(1,n+1):
   pre=Path(t)/f"p{i}";subprocess.run(["pdftoppm","-f",str(i),"-l",str(i),"-r","72","-png",str(p),str(pre)],check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE);f=list(Path(t).glob(f"p{i}-*.png"))
   if len(f)!=1 or f[0].stat().st_size<1000:raise AssertionError("raster")
   out.append(f[0].stat().st_size)
 return out
def fresh(i):
 with tempfile.TemporaryDirectory(prefix=f"c314-build-{i}-") as t:
  w=Path(t);shutil.copy2(TEX,w/"main.tex");env=dict(os.environ,SOURCE_DATE_EPOCH=str(EPOCH),FORCE_SOURCE_DATE="1",TZ="UTC");src=rf"\def\CRevisionRound{{{i}}}\input{{main.tex}}";cmd=["lualatex","-interaction=nonstopmode","-halt-on-error","-jobname=main",src]
  for _ in range(2):subprocess.run(cmd,cwd=w,env=env,check=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
  m=WARNING.search((w/"main.log").read_text(errors="replace"))
  if m:raise AssertionError(f"warning {m.group(0)}")
  return (w/"main.pdf").read_bytes()
def strict(p):
 def pairs(xs):
  o={}
  for k,v in xs:
   if k in o:raise ValueError("duplicate JSON")
   o[k]=v
  return o
 return json.loads(p.read_text(),object_pairs_hook=pairs,parse_constant=lambda x:(_ for _ in()).throw(ValueError("nonfinite JSON")))
def expected_manifest():
 fs={str(p.relative_to(ROOT)):p for p in ROOT.rglob("*") if p.is_file() and p!=MANIFEST}
 if set(fs)!=EXPECTED or len(fs)!=27:raise AssertionError(f"ledger missing={sorted(EXPECTED-set(fs))} extra={sorted(set(fs)-EXPECTED)}")
 if sha(EVALUATION)!=EVAL_RAW:raise AssertionError("evaluation raw digest")
 d=strict(EVIDENCE);b=dict(d);payload=b.pop("payload_sha256");actual=hashlib.sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
 if payload!=actual:raise AssertionError("payload")
 tokens=("exact ancient solution and curvature","global geometry, arrival time, and two asymptotic regimes","evidence, collisions, and route-a boundary");rows=[]
 for i,p in enumerate(ROUNDS):
  n=pages(p)
  if tokens[i] not in ptext(p):raise AssertionError(f"round token {i}")
  rows.append({"round":i,"path":str(p.relative_to(ROOT)),"sha256":sha(p),"bytes":p.stat().st_size,"pages":n,"font_rows":fonts(p),"raster_bytes":raster(p,n)})
 if len({x["sha256"] for x in rows})!=3 or PDF.read_bytes()!=ROUNDS[2].read_bytes():raise AssertionError("rounds")
 return {"schema":"hcs-release-manifest-v1","candidate_id":"HCS-C314","obstruction_id":"HEN-O298","source_commit":SOURCE,"fixed_epoch":EPOCH,"scope_literal":SCOPE,"payload_file_count":27,"physical_file_count":28,"evaluation_raw_sha256":EVAL_RAW,"evaluation_semantic_sha256":EVAL_SEMANTIC,"evidence_sha256":sha(EVIDENCE),"evidence_payload_sha256":payload,"pdf_rounds":rows,"files":{k:sha(v) for k,v in sorted(fs.items())}}
def main():
 p=argparse.ArgumentParser();p.add_argument("--write",action="store_true");a=p.parse_args()
 if sys.flags.optimize:raise RuntimeError("C314 release refuses optimized Python")
 lanes=[("c314_angenent_producer.py","C314_PRODUCER_PASS"),("c314_angenent_checker.py","C314 independent checker: PASS"),("c314_angenent_sympy_crosscheck.py","C314 SymPy cross-check: PASS"),("c314_angenent_replay.py","C314 byte replay: PASS"),("c314_angenent_mutation.py","C314 hostile mutation suite: PASS")]
 for n,s in lanes:
  q=run(n)
  if q.returncode or s not in q.stdout:raise AssertionError(f"lane {n}: {q.stdout}")
  if run(n,True).returncode==0:raise AssertionError(f"optimized lane survived {n}")
 for i,pdf in enumerate(ROUNDS):
  x,y=fresh(i),fresh(i)
  if x!=y or x!=pdf.read_bytes():raise AssertionError(f"determinism round {i}")
 d=expected_manifest();raw=json.dumps(d,sort_keys=True,indent=2,ensure_ascii=False)+"\n"
 if a.write:MANIFEST.write_text(raw)
 elif not MANIFEST.exists() or MANIFEST.read_text()!=raw:raise AssertionError("manifest stale")
 bad=[p for p in ROOT.rglob("*") if p.is_file() and (p.suffix in {".aux",".log",".out",".toc",".pyc"} or "__pycache__" in p.parts)]
 if bad:raise AssertionError(f"sidecars {bad}")
 print(f"C314_RELEASE_PASS {sha(EVIDENCE)} {sha(PDF)} {sha(MANIFEST)}")
if __name__=="__main__":main()
