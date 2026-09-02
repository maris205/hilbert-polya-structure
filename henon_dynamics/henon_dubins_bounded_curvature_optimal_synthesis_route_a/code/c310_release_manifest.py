#!/usr/bin/env python3
"""Close or verify the exact HCS-C310 release."""
from __future__ import annotations
import argparse,hashlib,json,os,re,shutil,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];M=ROOT/"C310_RELEASE_MANIFEST.json";E=ROOT/"results/c310_dubins_evidence.json";T=ROOT/"paper/main.tex";P=ROOT/"paper/main.pdf";EPOCH=1788393600;SOURCE="b3e2f3f7207b85d7be942ff72b1f49e754615c76";SCOPE="NO_BAD_EULER_OR_ROOT_NUMBER"
R=[ROOT/f"paper/main_round{i}{'_original' if i==0 else ''}.pdf" for i in range(3)];WARN=re.compile(r"(?:LaTeX|Package [^:\n]+) Warning:|Overfull|Underfull|undefined (?:references|citations)|Rerun to get|Missing character")
EXPECTED={"EXPERIMENT_PLAN.md","NARRATIVE_REPORT.md","PAPER_IMPROVEMENT_LOG.md","PAPER_PLAN.md","README.md","RESEARCH_QUESTION.md","SOURCE_AUDIT.md","THEOREM_PACKAGE.md","code/README.md","code/c310_release_manifest.py","code/c310_dubins_checker.py","code/c310_dubins_mutation.py","code/c310_dubins_producer.py","code/c310_dubins_replay.py","code/c310_dubins_sympy_crosscheck.py","evaluations/route_a/HCS-C310/2026-09-03.yaml","paper/COMPILE_REPORT.md","paper/README.md","paper/main.pdf","paper/main.tex","paper/main_round0_original.pdf","paper/main_round1.pdf","paper/main_round2.pdf","results/HOSTILE_AUDIT.md","results/RESULTS.md","results/TEST_REPORT.md","results/c310_dubins_evidence.json"}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(n):return subprocess.check_output([sys.executable,"-B",str(ROOT/"code"/n)],env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1",TZ="UTC"),text=True)
def pages(p):return int(next(x.split(":",1)[1] for x in subprocess.check_output(["pdfinfo",str(p)],text=True).splitlines() if x.startswith("Pages:")))
def fonts(p):
 rows=[x for x in subprocess.check_output(["pdffonts",str(p)],text=True).splitlines()[2:] if x.strip() and not x.lstrip().startswith("-")]
 if not rows or not all(len(x.split())>=7 and x.split()[-5]=="yes" and x.split()[-4]=="yes" for x in rows):raise AssertionError("font embedding")
 return len(rows)
def text(p):return " ".join(subprocess.check_output(["pdftotext","-layout",str(p),"-"],text=True).lower().split())
def raster(p,n):
 out=[]
 with tempfile.TemporaryDirectory(prefix="c310-raster-") as tmp:
  for i in range(1,n+1):
   pre=Path(tmp)/f"p{i}";subprocess.run(["pdftoppm","-f",str(i),"-l",str(i),"-r","72","-png",str(p),str(pre)],check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE);f=list(Path(tmp).glob(f"p{i}-*.png"))
   if len(f)!=1 or f[0].stat().st_size<1000:raise AssertionError("raster")
   out.append(f[0].stat().st_size)
 return out
def fresh(i):
 with tempfile.TemporaryDirectory(prefix=f"c310-build-{i}-") as tmp:
  w=Path(tmp);shutil.copy2(T,w/"main.tex");env=dict(os.environ,SOURCE_DATE_EPOCH=str(EPOCH),FORCE_SOURCE_DATE="1",TZ="UTC");src=rf"\def\CRevisionRound{{{i}}}\input{{main.tex}}";cmd=["lualatex","-interaction=nonstopmode","-halt-on-error","-jobname=main",src]
  for _ in range(2):subprocess.run(cmd,cwd=w,env=env,check=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
  hit=WARN.search((w/"main.log").read_text(errors="replace"))
  if hit:raise AssertionError(f"settled warning {hit.group(0)}")
  return (w/"main.pdf").read_bytes()
def evidence():
 def pairs(xs):
  d={}
  for k,v in xs:
   if k in d:raise ValueError("duplicate JSON")
   d[k]=v
  return d
 d=json.loads(E.read_text(),object_pairs_hook=pairs,parse_constant=lambda x:(_ for _ in()).throw(ValueError("nonfinite")));b=dict(d);h=b.pop("payload_sha256")
 if hashlib.sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()!=h:raise AssertionError("payload")
 return h
def build_manifest():
 files={str(p.relative_to(ROOT)):p for p in ROOT.rglob("*") if p.is_file() and p!=M}
 if set(files)!=EXPECTED or len(files)!=27:raise AssertionError(f"ledger missing={sorted(EXPECTED-set(files))} extra={sorted(set(files)-EXPECTED)}")
 rows=[];tokens=("six-word global synthesis","boundaries, ties, and symmetries","evidence and route-a boundary")
 for i,p in enumerate(R):
  n=pages(p)
  if tokens[i] not in text(p):raise AssertionError("PDF text")
  rows.append({"round":i,"path":str(p.relative_to(ROOT)),"sha256":sha(p),"bytes":p.stat().st_size,"pages":n,"font_rows":fonts(p),"raster_bytes":raster(p,n)})
 if len({x["sha256"] for x in rows})!=3 or P.read_bytes()!=R[2].read_bytes():raise AssertionError("round alias")
 return {"schema":"hcs-release-manifest-v1","candidate_id":"HCS-C310","obstruction_id":"HEN-O294","source_commit":SOURCE,"fixed_epoch":EPOCH,"scope_literal":SCOPE,"payload_file_count":27,"physical_file_count":28,"evidence_sha256":sha(E),"evidence_payload_sha256":evidence(),"pdf_rounds":rows,"files":{k:sha(v) for k,v in sorted(files.items())}}
def main():
 a=argparse.ArgumentParser();a.add_argument("--write",action="store_true");o=a.parse_args()
 if sys.flags.optimize:raise RuntimeError("C310 release refuses optimized Python")
 for n,s in [("c310_dubins_producer.py","C310_PRODUCER_PASS"),("c310_dubins_checker.py","C310 independent checker: PASS"),("c310_dubins_sympy_crosscheck.py","C310 SymPy cross-check: PASS"),("c310_dubins_replay.py","C310 byte replay: PASS"),("c310_dubins_mutation.py","C310 hostile mutation suite: PASS")]:
  if s not in run(n):raise AssertionError(n)
 for i,p in enumerate(R):
  a,b=fresh(i),fresh(i)
  if a!=b or a!=p.read_bytes():raise AssertionError(f"determinism {i}")
 d=build_manifest();raw=json.dumps(d,sort_keys=True,indent=2,ensure_ascii=False)+"\n"
 if o.write:M.write_text(raw)
 elif not M.exists() or M.read_text()!=raw:raise AssertionError("manifest stale")
 bad=[p for p in ROOT.rglob("*") if p.is_file() and (p.suffix in {".aux",".log",".out",".toc",".pyc"} or "__pycache__" in p.parts)]
 if bad:raise AssertionError(f"sidecars {bad}")
 print(f"C310_RELEASE_PASS {sha(E)} {sha(P)} {sha(M)}")
if __name__=="__main__":main()
