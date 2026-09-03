#!/usr/bin/env python3
"""Closed release and deterministic-PDF verifier for HCS-C335."""
from __future__ import annotations
import argparse,hashlib,json,os,re,shutil,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];MANIFEST=ROOT/"C335_RELEASE_MANIFEST.json";EVIDENCE=ROOT/"results/c335_shot_noise_ou_evidence.json";TEX=ROOT/"paper/main.tex";PDF=ROOT/"paper/main.pdf";ROUNDS=[ROOT/"paper/main_round0_original.pdf",ROOT/"paper/main_round1.pdf",ROOT/"paper/main_round2.pdf"]
SOURCE="db2c816b7b6bd450f51f79b91842cb882b0bd773";EPOCH=1788393600;SCOPE="NO_BAD_EULER_OR_ROOT_NUMBER"
WARNING=re.compile(r"LaTeX Warning|Package .* Warning|Overfull|Underfull|Missing character|undefined reference",re.I);CONTROL=re.compile(rb"[\x00-\x08\x0b\x0e-\x1f\x7f]")
EXPECTED={"EXPERIMENT_PLAN.md","NARRATIVE_REPORT.md","PAPER_IMPROVEMENT_LOG.md","PAPER_PLAN.md","README.md","RESEARCH_QUESTION.md","SOURCE_AUDIT.md","THEOREM_PACKAGE.md","code/README.md","code/c335_shot_noise_ou_checker.py","code/c335_shot_noise_ou_mutation.py","code/c335_shot_noise_ou_producer.py","code/c335_shot_noise_ou_replay.py","code/c335_shot_noise_ou_sympy_crosscheck.py","code/c335_release_manifest.py","evaluations/route_a/HCS-C335/2026-09-03.yaml","paper/COMPILE_REPORT.md","paper/README.md","paper/main.pdf","paper/main.tex","paper/main_round0_original.pdf","paper/main_round1.pdf","paper/main_round2.pdf","results/HOSTILE_AUDIT.md","results/RESULTS.md","results/TEST_REPORT.md","results/c335_shot_noise_ou_evidence.json"}
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def run(script,opt="-B"):
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1",TZ="UTC");return subprocess.run([sys.executable,opt,str(ROOT/"code"/script)],env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
def pages(path):
    out=subprocess.check_output(["pdfinfo",str(path)],text=True);return int(next(x.split(":",1)[1] for x in out.splitlines() if x.startswith("Pages:")))
def fonts(path):
    rows=[x for x in subprocess.check_output(["pdffonts",str(path)],text=True).splitlines()[2:] if x.strip() and not x.lstrip().startswith("-")]
    if not rows or not all(len(x.split())>=7 and x.split()[-5]=="yes" and x.split()[-4]=="yes" for x in rows):raise AssertionError("font embedding/subset")
    return len(rows)
def text_gate(path):
    raw=subprocess.check_output(["pdftotext","-layout",str(path),"-"]);low=raw.lower()
    if CONTROL.search(raw) or b"qquad" in low or b"??" in raw or b"[verify]" in low or b"unfinished" in low or b"placeholder" in low:raise AssertionError("PDF text gate")
    return raw
def raster(path,count):
    sizes=[]
    with tempfile.TemporaryDirectory(prefix="c335-raster-") as td:
        for n in range(1,count+1):
            prefix=Path(td)/f"page{n}";subprocess.run(["pdftoppm","-f",str(n),"-l",str(n),"-r","72","-png",str(path),str(prefix)],check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE);images=list(Path(td).glob(f"page{n}-*.png"))
            if len(images)!=1 or images[0].stat().st_size<1000:raise AssertionError("raster")
            sizes.append(images[0].stat().st_size)
    return sizes
def fresh(round_number):
    with tempfile.TemporaryDirectory(prefix=f"c335-build-{round_number}-") as td:
        work=Path(td);shutil.copy2(TEX,work/"main.tex");env=dict(os.environ,SOURCE_DATE_EPOCH=str(EPOCH),FORCE_SOURCE_DATE="1",TZ="UTC");source=rf"\def\CRevisionRound{{{round_number}}}\input{{main.tex}}"
        for _ in range(2):subprocess.run(["lualatex","-interaction=nonstopmode","-halt-on-error","-jobname=main",source],cwd=work,env=env,check=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        match=WARNING.search((work/"main.log").read_text(errors="replace"))
        if match:raise AssertionError(f"settled warning {match.group(0)}")
        return (work/"main.pdf").read_bytes()
def expected_manifest():
    physical={str(p.relative_to(ROOT)):p for p in ROOT.rglob("*") if p.is_file() and p!=MANIFEST}
    if set(physical)!=EXPECTED or len(physical)!=27:raise AssertionError(f"payload missing={sorted(EXPECTED-set(physical))} extra={sorted(set(physical)-EXPECTED)}")
    for name,path in physical.items():
        if not name.endswith(".pdf") and CONTROL.search(path.read_bytes()):raise AssertionError(f"control byte {name}")
    data=json.loads(EVIDENCE.read_text());body=dict(data);payload=body.pop("payload_sha256");canonical=json.dumps(body,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
    if payload!=hashlib.sha256(canonical).hexdigest():raise AssertionError("evidence payload")
    tokens=("shot-noise laplace semigroup owner","equilibrium, contraction, and correlations","exact finite polynomial filtration");receipts=[]
    for n,path in enumerate(ROUNDS):
        count=pages(path);raw=text_gate(path);normalized=" ".join(raw.decode("utf-8").lower().split())
        if tokens[n] not in normalized:raise AssertionError(f"round token {n}")
        receipts.append({"round":n,"path":str(path.relative_to(ROOT)),"sha256":sha(path),"bytes":path.stat().st_size,"pages":count,"font_rows":fonts(path),"raster_bytes":raster(path,count)})
    if len({x["sha256"] for x in receipts})!=3 or PDF.read_bytes()!=ROUNDS[2].read_bytes():raise AssertionError("round identity")
    return {"schema":"hcs-release-manifest-v1","candidate_id":"HCS-C335","obstruction_id":"HEN-O319","source_commit":SOURCE,"fixed_epoch":EPOCH,"scope_literal":SCOPE,"payload_file_count":27,"physical_file_count":28,"evidence_sha256":sha(EVIDENCE),"evidence_payload_sha256":payload,"pdf_rounds":receipts,"files":{name:sha(path) for name,path in sorted(physical.items())}}
def main():
    if sys.flags.optimize:raise RuntimeError("C335 release refuses optimized Python")
    ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");args=ap.parse_args();lanes=(("c335_shot_noise_ou_producer.py","C335_PRODUCER_PASS"),("c335_shot_noise_ou_checker.py","C335 independent checker: PASS"),("c335_shot_noise_ou_sympy_crosscheck.py","C335 SymPy cross-check: PASS"),("c335_shot_noise_ou_replay.py","C335 byte replay: PASS"),("c335_shot_noise_ou_mutation.py","C335 hostile mutation suite: PASS"))
    for script,sentinel in lanes:
        result=run(script)
        if result.returncode or sentinel not in result.stdout:raise AssertionError(result.stdout)
        hostile=run(script,"-OO")
        if hostile.returncode==0 or "refuses optimized Python" not in hostile.stdout:raise AssertionError(f"optimized refusal {script}")
    for n,archive in enumerate(ROUNDS):
        one,two=fresh(n),fresh(n)
        if one!=two or one!=archive.read_bytes():raise AssertionError(f"PDF determinism {n}")
    manifest=expected_manifest();rendered=json.dumps(manifest,sort_keys=True,indent=2,ensure_ascii=False)+"\n"
    if args.write:MANIFEST.write_text(rendered)
    elif not MANIFEST.exists() or MANIFEST.read_text()!=rendered:raise AssertionError("manifest stale")
    sidecars={".aux",".log",".out",".toc",".fls",".fdb_latexmk",".pyc"}
    if any(p.suffix in sidecars or "__pycache__" in p.parts for p in ROOT.rglob("*") if p.is_file()):raise AssertionError("build sidecar")
    print(f"C335_RELEASE_PASS {sha(EVIDENCE)} {sha(PDF)} {sha(MANIFEST)}")
if __name__=="__main__":main()
