#!/usr/bin/env python3
"""Close or verify the exact 27-payload HCS-C316 release."""
from __future__ import annotations
import argparse, hashlib, json, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; MANIFEST=ROOT/"C316_RELEASE_MANIFEST.json"
EVIDENCE=ROOT/"results/c316_elephant_evidence.json"; TEX=ROOT/"paper/main.tex"; PDF=ROOT/"paper/main.pdf"
EPOCH=1788393600; SOURCE="1938bae19e5a92f9ce2411aafdc68323bd641bd0"; SCOPE="NO_BAD_EULER_OR_ROOT_NUMBER"
ROUNDS=[ROOT/f"paper/main_round{i}{'_original' if i==0 else ''}.pdf" for i in range(3)]
WARNING=re.compile(r"(?:LaTeX|Package [^:\n]+) Warning:|Overfull|Underfull|undefined (?:references|citations)|Rerun to get|Missing character")
EXPECTED={
"EXPERIMENT_PLAN.md","NARRATIVE_REPORT.md","PAPER_IMPROVEMENT_LOG.md","PAPER_PLAN.md","README.md","RESEARCH_QUESTION.md","SOURCE_AUDIT.md","THEOREM_PACKAGE.md",
"code/README.md","code/c316_release_manifest.py","code/c316_elephant_checker.py","code/c316_elephant_mutation.py","code/c316_elephant_producer.py","code/c316_elephant_replay.py","code/c316_elephant_sympy_crosscheck.py",
"evaluations/route_a/HCS-C316/2026-09-03.yaml","paper/COMPILE_REPORT.md","paper/README.md","paper/main.pdf","paper/main.tex","paper/main_round0_original.pdf","paper/main_round1.pdf","paper/main_round2.pdf",
"results/HOSTILE_AUDIT.md","results/RESULTS.md","results/TEST_REPORT.md","results/c316_elephant_evidence.json"}

def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def sidecar(path): return path.suffix in {".aux",".log",".out",".toc",".fls",".fdb_latexmk",".pyc"} or "__pycache__" in path.parts or path.name.endswith(".synctex.gz")
def run(name):
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1",TZ="UTC")
    return subprocess.check_output([sys.executable,"-B",str(ROOT/"code"/name)],env=env,text=True)
def pdf_pages(path):
    out=subprocess.check_output(["pdfinfo",str(path)],text=True)
    return int(next(line.split(":",1)[1] for line in out.splitlines() if line.startswith("Pages:")))
def fonts(path):
    out=subprocess.check_output(["pdffonts",str(path)],text=True)
    rows=[line for line in out.splitlines()[2:] if line.strip() and not line.lstrip().startswith("-")]
    if not rows or not all(len(row.split())>=7 and row.split()[-5]=="yes" and row.split()[-4]=="yes" for row in rows): raise AssertionError("fonts not embedded/subset")
    return len(rows)
def pdf_text(path): return " ".join(subprocess.check_output(["pdftotext","-layout",str(path),"-"],text=True).lower().split())
def raster(path,pages):
    sizes=[]
    with tempfile.TemporaryDirectory(prefix="c316-raster-") as tmp:
      for page in range(1,pages+1):
        prefix=Path(tmp)/f"p{page}"; subprocess.run(["pdftoppm","-f",str(page),"-l",str(page),"-r","72","-png",str(path),str(prefix)],check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        found=list(Path(tmp).glob(f"p{page}-*.png"))
        if len(found)!=1 or found[0].stat().st_size<1000: raise AssertionError("raster failure")
        sizes.append(found[0].stat().st_size)
    return sizes
def fresh(round_no):
    with tempfile.TemporaryDirectory(prefix=f"c316-build-{round_no}-") as tmp:
      work=Path(tmp); shutil.copy2(TEX,work/"main.tex"); env=dict(os.environ,SOURCE_DATE_EPOCH=str(EPOCH),FORCE_SOURCE_DATE="1",TZ="UTC")
      source=rf"\def\CRevisionRound{{{round_no}}}\input{{main.tex}}"; cmd=["lualatex","-interaction=nonstopmode","-halt-on-error","-jobname=main",source]
      for _ in range(2): subprocess.run(cmd,cwd=work,env=env,check=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
      log=(work/"main.log").read_text(errors="replace"); match=WARNING.search(log)
      if match: raise AssertionError(f"settled LaTeX warning: {match.group(0)}")
      return (work/"main.pdf").read_bytes()
def strict_json(path):
    def pairs(items):
      out={}
      for key,value in items:
        if key in out: raise ValueError("duplicate JSON key")
        out[key]=value
      return out
    return json.loads(path.read_text(),object_pairs_hook=pairs,parse_constant=lambda x: (_ for _ in ()).throw(ValueError("nonfinite JSON")))
def expected_manifest():
    physical={str(path.relative_to(ROOT)):path for path in ROOT.rglob("*") if path.is_file() and path!=MANIFEST}
    if set(physical)!=EXPECTED or len(physical)!=27: raise AssertionError(f"payload ledger mismatch missing={sorted(EXPECTED-set(physical))} extra={sorted(set(physical)-EXPECTED)}")
    evidence=strict_json(EVIDENCE); body=dict(evidence); payload=body.pop("payload_sha256")
    semantic=hashlib.sha256(json.dumps(body,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
    if semantic!=payload: raise AssertionError("evidence payload hash")
    tokens=("revision certificate: exact finite structure","revision certificate: complete phase and endpoint theorem","revision certificate: evidence, collisions, and scope closure")
    pdf_rows=[]
    for number,path in enumerate(ROUNDS):
      pages=pdf_pages(path); text=pdf_text(path)
      if tokens[number] not in text: raise AssertionError(f"round text token absent {number}")
      pdf_rows.append({"round":number,"path":str(path.relative_to(ROOT)),"sha256":sha(path),"bytes":path.stat().st_size,"pages":pages,"font_rows":fonts(path),"raster_bytes":raster(path,pages)})
    if len({row["sha256"] for row in pdf_rows})!=3 or PDF.read_bytes()!=ROUNDS[2].read_bytes(): raise AssertionError("round archive/final alias")
    return {"schema":"hcs-release-manifest-v1","candidate_id":"HCS-C316","obstruction_id":"HEN-O300","source_commit":SOURCE,"fixed_epoch":EPOCH,"scope_literal":SCOPE,"payload_file_count":27,"physical_file_count":28,"evidence_sha256":sha(EVIDENCE),"evidence_payload_sha256":payload,"pdf_rounds":pdf_rows,"files":{name:sha(path) for name,path in sorted(physical.items())}}
def main():
    parser=argparse.ArgumentParser();parser.add_argument("--write",action="store_true");args=parser.parse_args()
    if sys.flags.optimize: raise RuntimeError("C316 release refuses optimized Python")
    sentinels=[("c316_elephant_producer.py","C316_PRODUCER_PASS"),("c316_elephant_checker.py","C316 independent checker: PASS"),("c316_elephant_sympy_crosscheck.py","C316 SymPy cross-check: PASS"),("c316_elephant_replay.py","C316 byte replay: PASS"),("c316_elephant_mutation.py","C316 hostile mutation suite: PASS")]
    for name,sentinel in sentinels:
      if sentinel not in run(name): raise AssertionError(f"lane failed {name}")
    for number,archive in enumerate(ROUNDS):
      first=fresh(number);second=fresh(number)
      if first!=second or first!=archive.read_bytes(): raise AssertionError(f"nondeterministic round {number}")
    manifest=expected_manifest(); rendered=json.dumps(manifest,sort_keys=True,indent=2,ensure_ascii=False)+"\n"
    if args.write: MANIFEST.write_text(rendered)
    elif not MANIFEST.exists() or MANIFEST.read_text()!=rendered: raise AssertionError("manifest is absent or stale")
    physical=[path for path in ROOT.rglob("*") if path.is_file()]
    if any(sidecar(path) for path in physical): raise AssertionError("sidecar present")
    print(f"C316_RELEASE_PASS {sha(EVIDENCE)} {sha(PDF)} {sha(MANIFEST)}")
if __name__=="__main__": main()
