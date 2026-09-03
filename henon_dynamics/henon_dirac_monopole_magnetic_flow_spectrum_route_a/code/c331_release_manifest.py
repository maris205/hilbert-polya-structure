#!/usr/bin/env python3
"""Final 27-payload release gate and manifest writer for HCS-C331."""
from __future__ import annotations
import argparse, hashlib, json, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C331_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c331_dirac_monopole_evidence.json"
TEX = ROOT / "paper/main.tex"; MAIN_PDF = ROOT / "paper/main.pdf"
EPOCH = 1788393600; SOURCE = "5ca65027918c0fce7ef9af82f3faf2e46ed6530c"; SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EVALUATION = ROOT / "evaluations/route_a/HCS-C331/2026-09-03.yaml"
EVALUATION_RAW_SHA256 = "02af8e9102ec43a62b69b5131952ff6e49f83e0ab1826b9a916ed32a953abd4a"
EVALUATION_SEMANTIC_SHA256 = "03ca40b5c17fa8858846885ae2c4a48375c114b71594550f3896ab4b69779a21"
ROUND_PDFS = [ROOT / "paper/main_round0_original.pdf", ROOT / "paper/main_round1.pdf", ROOT / "paper/main_round2.pdf"]
WARNING = re.compile(r"(?:LaTeX|Package [^:\n]+) Warning:|Overfull|Underfull|undefined (?:references|citations)|Rerun to get|Missing character")
EXPECTED = {
    "EXPERIMENT_PLAN.md","NARRATIVE_REPORT.md","PAPER_IMPROVEMENT_LOG.md","PAPER_PLAN.md","README.md","RESEARCH_QUESTION.md","SOURCE_AUDIT.md","THEOREM_PACKAGE.md",
    "code/README.md","code/c331_release_manifest.py","code/c331_dirac_monopole_checker.py","code/c331_dirac_monopole_mutation.py","code/c331_dirac_monopole_producer.py","code/c331_dirac_monopole_replay.py","code/c331_dirac_monopole_sympy_crosscheck.py",
    "evaluations/route_a/HCS-C331/2026-09-03.yaml","paper/COMPILE_REPORT.md","paper/README.md","paper/main.pdf","paper/main.tex","paper/main_round0_original.pdf","paper/main_round1.pdf","paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md","results/RESULTS.md","results/TEST_REPORT.md","results/c331_dirac_monopole_evidence.json",
}
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def run_lane(name): return subprocess.check_output([sys.executable,"-B",str(ROOT/"code"/name)],env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1",TZ="UTC"),text=True)
def optimized_refusal(name):
    cmd=[sys.executable,"-O","-B",str(ROOT/"code"/name)]
    with tempfile.TemporaryDirectory(prefix="c331-opt-") as directory:
        if name=="c331_dirac_monopole_producer.py": cmd += ["--output",str(Path(directory)/"forbidden.json")]
        p=subprocess.run(cmd,env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1",TZ="UTC"),stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        if p.returncode==0 or "refuses optimized Python" not in p.stdout: raise AssertionError(f"optimized execution not explicitly refused: {name}")
def pages(path):
    out=subprocess.check_output(["pdfinfo",str(path)],text=True)
    return int(next(x.split(":",1)[1] for x in out.splitlines() if x.startswith("Pages:")))
def fonts(path):
    out=subprocess.check_output(["pdffonts",str(path)],text=True); rows=[x for x in out.splitlines()[2:] if x.strip() and not x.lstrip().startswith("-")]
    if not rows or not all(len(x.split())>=7 and x.split()[-5:-3]==["yes","yes"] for x in rows): raise AssertionError(f"font embedding/subsetting failure: {path}")
    return len(rows)
def text_of(path):
    output=subprocess.check_output(["pdftotext","-layout",str(path),"-"],text=True).translate({16:ord("("),17:ord(")"),18:ord("("),19:ord(")")})
    if "\ufffd" in output or any(ord(ch)<32 and ch not in "\n\r\t\f" for ch in output): raise AssertionError(f"nonprintable or replacement character in PDF text: {path}")
    normalized=" ".join(output.lower().split())
    for literal in ("qquad", "??", "[verify]"):
        if literal in normalized: raise AssertionError(f"forbidden literal {literal!r} in PDF text: {path}")
    return normalized
def raster(path,count):
    sizes=[]
    with tempfile.TemporaryDirectory(prefix="c331-raster-") as directory:
        directory=Path(directory)
        for page in range(1,count+1):
            prefix=directory/f"page-{page}"; subprocess.run(["pdftoppm","-f",str(page),"-l",str(page),"-r","72","-png",str(path),str(prefix)],check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            images=list(directory.glob(f"page-{page}-*.png"))
            if len(images)!=1 or images[0].stat().st_size<1000: raise AssertionError("raster failure")
            sizes.append(images[0].stat().st_size)
    return sizes
def fresh(round_number):
    with tempfile.TemporaryDirectory(prefix=f"c331-build-{round_number}-") as directory:
        work=Path(directory); shutil.copy2(TEX,work/"main.tex"); env=dict(os.environ,SOURCE_DATE_EPOCH=str(EPOCH),FORCE_SOURCE_DATE="1",TZ="UTC")
        source=rf"\def\CRevisionRound{{{round_number}}}\input{{main.tex}}"; cmd=["lualatex","-interaction=nonstopmode","-halt-on-error","-jobname=main",source]
        for _ in range(2): subprocess.run(cmd,cwd=work,env=env,check=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        match=WARNING.search((work/"main.log").read_text(errors="replace"))
        if match: raise AssertionError(f"paper warning round {round_number}: {match.group(0)}")
        return (work/"main.pdf").read_bytes()
def evidence_payload_hash():
    data=json.loads(EVIDENCE.read_text(),parse_constant=lambda x:(_ for _ in ()).throw(ValueError(x))); body=dict(data); claimed=body.pop("payload_sha256")
    computed=hashlib.sha256(json.dumps(body,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
    if computed!=claimed: raise AssertionError("stale evidence payload")
    return claimed
def build_manifest():
    files={str(p.relative_to(ROOT)):p for p in ROOT.rglob("*") if p.is_file() and p!=MANIFEST}
    if set(files)!=EXPECTED or len(files)!=27: raise AssertionError(f"payload ledger mismatch: missing={sorted(EXPECTED-set(files))}, extra={sorted(set(files)-EXPECTED)}")
    if sha(EVALUATION)!=EVALUATION_RAW_SHA256: raise AssertionError("evaluation raw digest")
    tokens=("poincare vector and every magnetic circle","complete monopole-harmonic spectrum","route-a obstruction and finite certificate"); pdf_rows=[]
    for r,path in enumerate(ROUND_PDFS):
        count=pages(path)
        if tokens[r] not in text_of(path): raise AssertionError(f"revision token absent: {r}")
        pdf_rows.append({"round":r,"path":str(path.relative_to(ROOT)),"sha256":sha(path),"bytes":path.stat().st_size,"pages":count,"font_rows":fonts(path),"raster_bytes":raster(path,count)})
    if len({x["sha256"] for x in pdf_rows})!=3: raise AssertionError("revision PDFs not distinct")
    if MAIN_PDF.read_bytes()!=ROUND_PDFS[2].read_bytes(): raise AssertionError("main.pdf not final")
    return {"schema":"hcs-release-manifest-v1","candidate_id":"HCS-C331","obstruction_id":"HEN-O315","source_commit":SOURCE,"fixed_epoch":EPOCH,"scope_literal":SCOPE,"payload_file_count":27,"physical_file_count":28,"evaluation_raw_sha256":EVALUATION_RAW_SHA256,"evaluation_semantic_sha256":EVALUATION_SEMANTIC_SHA256,"evidence_sha256":sha(EVIDENCE),"evidence_payload_sha256":evidence_payload_hash(),"pdf_rounds":pdf_rows,"files":{n:sha(p) for n,p in sorted(files.items())}}
def main():
    if sys.flags.optimize: raise RuntimeError("C331 release refuses optimized Python")
    parser=argparse.ArgumentParser(); parser.add_argument("--write",action="store_true"); args=parser.parse_args()
    lanes=[("c331_dirac_monopole_producer.py","C331_PRODUCER_PASS"),("c331_dirac_monopole_checker.py","C331 independent checker: PASS"),("c331_dirac_monopole_sympy_crosscheck.py","C331 SymPy cross-check: PASS"),("c331_dirac_monopole_replay.py","C331 byte replay: PASS"),("c331_dirac_monopole_mutation.py","C331 hostile mutation suite: PASS")]
    for name,sentinel in lanes:
        if sentinel not in run_lane(name): raise AssertionError(f"lane sentinel absent: {name}")
        optimized_refusal(name)
    for r,path in enumerate(ROUND_PDFS):
        one=fresh(r); two=fresh(r)
        if one!=two or one!=path.read_bytes(): raise AssertionError(f"stale/nondeterministic PDF: {r}")
    manifest=build_manifest(); raw=json.dumps(manifest,sort_keys=True,indent=2,ensure_ascii=False)+"\n"
    if args.write: MANIFEST.write_text(raw)
    elif not MANIFEST.exists() or MANIFEST.read_text()!=raw: raise AssertionError("release manifest missing/stale")
    sidecars=[p for p in ROOT.rglob("*") if p.is_file() and (p.suffix in {".aux",".log",".out",".toc",".pyc"} or "__pycache__" in p.parts)]
    if sidecars: raise AssertionError(f"forbidden sidecars: {sidecars}")
    print(f"C331_RELEASE_PASS {sha(EVIDENCE)} {sha(MAIN_PDF)} {sha(MANIFEST)}")
if __name__=="__main__": main()
