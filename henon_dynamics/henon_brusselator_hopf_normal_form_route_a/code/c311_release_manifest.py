#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json,os,re,shutil,subprocess,sys,tempfile
from pathlib import Path
R=Path(__file__).resolve().parents[1];M=R/"C311_RELEASE_MANIFEST.json";E=R/"results/c311_brusselator_evidence.json";T=R/"paper/main.tex";P=R/"paper/main.pdf";EPOCH=1788393600;SOURCE="b3e2f3f7207b85d7be942ff72b1f49e754615c76";SCOPE="NO_BAD_EULER_OR_ROOT_NUMBER";PDFS=[R/f"paper/main_round{i}{'_original' if i==0 else ''}.pdf" for i in range(3)];W=re.compile(r"(?:LaTeX|Package [^:\n]+) Warning:|Overfull|Underfull|undefined (?:references|citations)|Rerun to get|Missing character")
EXPECTED={"EXPERIMENT_PLAN.md","NARRATIVE_REPORT.md","PAPER_IMPROVEMENT_LOG.md","PAPER_PLAN.md","README.md","RESEARCH_QUESTION.md","SOURCE_AUDIT.md","THEOREM_PACKAGE.md","code/README.md","code/c311_release_manifest.py","code/c311_brusselator_checker.py","code/c311_brusselator_mutation.py","code/c311_brusselator_producer.py","code/c311_brusselator_replay.py","code/c311_brusselator_sympy_crosscheck.py","evaluations/route_a/HCS-C311/2026-09-03.yaml","paper/COMPILE_REPORT.md","paper/README.md","paper/main.pdf","paper/main.tex","paper/main_round0_original.pdf","paper/main_round1.pdf","paper/main_round2.pdf","results/HOSTILE_AUDIT.md","results/RESULTS.md","results/TEST_REPORT.md","results/c311_brusselator_evidence.json"}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(n):return subprocess.check_output([sys.executable,"-B",str(R/"code"/n)],env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1",TZ="UTC"),text=True)
def pages(p):return int(next(x.split(":",1)[1] for x in subprocess.check_output(["pdfinfo",str(p)],text=True).splitlines() if x.startswith("Pages:")))
def fonts(p):
 rows=[x for x in subprocess.check_output(["pdffonts",str(p)],text=True).splitlines()[2:] if x.strip() and not x.lstrip().startswith("-")]
 if not rows or not all(len(x.split())>=7 and x.split()[-5]=="yes" and x.split()[-4]=="yes" for x in rows):raise AssertionError("fonts")
 return len(rows)
def text(p):return " ".join(subprocess.check_output(["pdftotext","-layout",str(p),"-"],text=True).lower().split())
def raster(p,n):
 out=[]
 with tempfile.TemporaryDirectory(prefix="c311-raster-") as t:
  for i in range(1,n+1):
   pre=Path(t)/f"p{i}";subprocess.run(["pdftoppm","-f",str(i),"-l",str(i),"-r","72","-png",str(p),str(pre)],check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE);f=list(Path(t).glob(f"p{i}-*.png"))
   if len(f)!=1 or f[0].stat().st_size<1000:raise AssertionError("raster")
   out.append(f[0].stat().st_size)
 return out
def fresh(i):
 with tempfile.TemporaryDirectory(prefix=f"c311-build-{i}-") as t:
  w=Path(t);shutil.copy2(T,w/"main.tex");env=dict(os.environ,SOURCE_DATE_EPOCH=str(EPOCH),FORCE_SOURCE_DATE="1",TZ="UTC");src=rf"\def\CRevisionRound{{{i}}}\input{{main.tex}}";cmd=["lualatex","-interaction=nonstopmode","-halt-on-error","-jobname=main",src]
  for _ in range(2):subprocess.run(cmd,cwd=w,env=env,check=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
  h=W.search((w/"main.log").read_text(errors="replace"))
  if h:raise AssertionError(f"warning {h.group(0)}")
  return (w/"main.pdf").read_bytes()
def payload():
 d=json.loads(E.read_text());b=dict(d);h=b.pop("payload_sha256");actual=hashlib.sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
 if h!=actual:raise AssertionError("payload")
 return h
def manifest():
 fs={str(p.relative_to(R)):p for p in R.rglob("*") if p.is_file() and p!=M}
 if set(fs)!=EXPECTED or len(fs)!=27:raise AssertionError(f"ledger missing={sorted(EXPECTED-set(fs))} extra={sorted(set(fs)-EXPECTED)}")
 rows=[];tokens=("global existence and complete linear atlas","exact normalized hopf coefficient","evidence, collisions, and route-a boundary")
 for i,p in enumerate(PDFS):
  n=pages(p)
  if tokens[i] not in text(p):raise AssertionError("text")
  rows.append({"round":i,"path":str(p.relative_to(R)),"sha256":sha(p),"bytes":p.stat().st_size,"pages":n,"font_rows":fonts(p),"raster_bytes":raster(p,n)})
 if len({x["sha256"] for x in rows})!=3 or P.read_bytes()!=PDFS[2].read_bytes():raise AssertionError("rounds")
 return {"schema":"hcs-release-manifest-v1","candidate_id":"HCS-C311","obstruction_id":"HEN-O295","source_commit":SOURCE,"fixed_epoch":EPOCH,"scope_literal":SCOPE,"payload_file_count":27,"physical_file_count":28,"evidence_sha256":sha(E),"evidence_payload_sha256":payload(),"pdf_rounds":rows,"files":{k:sha(v) for k,v in sorted(fs.items())}}
def main():
 p=argparse.ArgumentParser();p.add_argument("--write",action="store_true");a=p.parse_args()
 if sys.flags.optimize:raise RuntimeError("C311 release refuses optimized Python")
 for n,s in [("c311_brusselator_producer.py","C311_PRODUCER_PASS"),("c311_brusselator_checker.py","C311 independent checker: PASS"),("c311_brusselator_sympy_crosscheck.py","C311 SymPy cross-check: PASS"),("c311_brusselator_replay.py","C311 byte replay: PASS"),("c311_brusselator_mutation.py","C311 hostile mutation suite: PASS")]:
  if s not in run(n):raise AssertionError(n)
 for i,pdf in enumerate(PDFS):
  x,y=fresh(i),fresh(i)
  if x!=y or x!=pdf.read_bytes():raise AssertionError("determinism")
 d=manifest();raw=json.dumps(d,sort_keys=True,indent=2,ensure_ascii=False)+"\n"
 if a.write:M.write_text(raw)
 elif not M.exists() or M.read_text()!=raw:raise AssertionError("manifest stale")
 bad=[p for p in R.rglob("*") if p.is_file() and (p.suffix in {".aux",".log",".out",".toc",".pyc"} or "__pycache__" in p.parts)]
 if bad:raise AssertionError(f"sidecars {bad}")
 print(f"C311_RELEASE_PASS {sha(E)} {sha(P)} {sha(M)}")
if __name__=="__main__":main()
