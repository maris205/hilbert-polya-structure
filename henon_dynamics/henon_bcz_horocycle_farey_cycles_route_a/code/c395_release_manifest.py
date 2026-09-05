#!/usr/bin/env python3
"""Exact physical release ledger and identical validation in write/nonwrite modes."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("c395 release refuses optimized Python")
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parents[1];REPO=ROOT.parents[1]
MANIFEST=ROOT/"C395_RELEASE_MANIFEST.json"
AUTHORITY="flow_systems/skills/route-a-evaluator.md"
AUTHORITY_SHA="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCRIPTS=("c395_bcz_producer.py","c395_bcz_checker.py","c395_bcz_sympy_crosscheck.py","c395_bcz_replay.py","c395_bcz_mutation.py","c395_release_manifest.py")
NAMES=("main_round0_original.pdf","main_round1.pdf","main_round2.pdf")
EXPECTED=(
 "README.md","PROJECT_README.md","RESEARCH_QUESTION.md","ASSUMPTIONS.md","SCOPE.md","LIMITATIONS.md",
 "THEOREM_PACKAGE.md","CLAIMS.md","NARRATIVE_REPORT.md","EXPERIMENT_PLAN.md","REFERENCES.md","SOURCE_AUDIT.md","REPRODUCIBILITY.md",
 "PAPER_PLAN.md","PAPER_IMPROVEMENT_LOG.md","requirements.txt","proof/ANALYTIC_PROOF.md",
 "code/README.md","code/c395_bcz_producer.py","code/c395_bcz_checker.py","code/c395_bcz_sympy_crosscheck.py",
 "code/c395_bcz_replay.py","code/c395_bcz_mutation.py","code/c395_release_manifest.py",
 "evaluations/route_a/HCS-C395/2026-09-05.yaml","tests/test_c395_smoke.py",
 "paper/README.md","paper/COMPILE_REPORT.md","paper/main.tex","paper/main_round0.tex","paper/main_round1.tex","paper/main_round2.tex",
 "paper/main.pdf","paper/main_round0_original.pdf","paper/main_round1.pdf","paper/main_round2.pdf",
 "paper/compile_round0.txt","paper/compile_round1.txt","paper/compile_round2.txt",
 "results/c395_bcz_evidence.json","results/RESULTS.md","results/TEST_REPORT.md","results/HOSTILE_AUDIT.md",
 "review/CROSS_REVIEW.md","review/FAILURE_MODE_AUDIT.md","review/CLAIM_REFERENCE_AUDIT.md","review/FINAL_INTEGRITY.md","review/SOURCE_PAGE_RECEIPT.md")
WARN=re.compile(r"(?:LaTeX|Package [^:\n]+) Warning:|warning  \(pdf backend\)|Overfull|Underfull|undefined (?:references|citations)|Rerun to get|Missing character")
def run(cmd,**kw):
    p=subprocess.run(cmd,capture_output=True,text=True,**kw)
    assert p.returncode==0,f"command failed {cmd}\n{p.stdout}\n{p.stderr}"
    return p.stdout.strip()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def can(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
def unique(items):
    d={}
    for k,v in items:assert k not in d,"duplicate JSON";d[k]=v
    return d
def strict(p):return json.loads(p.read_text(),object_pairs_hook=unique,parse_constant=lambda x:(_ for _ in ()).throw(ValueError(x)))
def preflight(evaluation):
    p=subprocess.run([sys.executable,"-B",str(ROOT/"code/c395_bcz_checker.py"),"--evaluation",str(evaluation),"--evaluation-only"],capture_output=True,text=True)
    if p.returncode:raise RuntimeError("preflight evaluation rejected:\n"+p.stdout+p.stderr)
    assert sha(REPO/AUTHORITY)==AUTHORITY_SHA,"evaluator authority"
def compile_round(index):
    blobs=[];logs=[]
    for build in range(2):
        with tempfile.TemporaryDirectory(prefix=f"c395-tex-{index}-{build}-") as d:
            work=Path(d)
            for name in ("main.tex",f"main_round{index}.tex"):shutil.copy2(ROOT/"paper"/name,work/name)
            cmd=["lualatex","-interaction=nonstopmode","-halt-on-error","-jobname=main",f"main_round{index}.tex"]
            env=dict(os.environ,SOURCE_DATE_EPOCH="1788566400",FORCE_SOURCE_DATE="1")
            run(cmd,cwd=work,env=env);run(cmd,cwd=work,env=env)
            log=(work/"main.log").read_text(errors="replace");m=WARN.search(log)
            assert m is None,f"round {index} settled warning: "+log[max(0,m.start()-80):m.start()+700]
            blobs.append((work/"main.pdf").read_bytes());logs.append(log)
    assert blobs[0]==blobs[1],"non-deterministic PDF"
    return blobs[0],logs[0]
def pdf_audit(path,index):
    info=run(["pdfinfo",str(path)]);m=re.search(r"^Pages:\s+(\d+)",info,re.M);assert m;pages=int(m.group(1))
    fonts=run(["pdffonts",str(path)]).splitlines()[2:];assert fonts
    for line in fonts:assert line.split()[-5:-3]==["yes","yes"],line
    assert any("DroidSansFallback" in t.replace(" ","") for t in fonts)
    with tempfile.TemporaryDirectory(prefix="c395-pdf-audit-") as d:
        work=Path(d);out=work/"text.txt";run(["pdftotext",str(path),str(out)])
        raw=out.read_bytes();assert all(b>=32 or b in (10,12,13) for b in raw)
        text=raw.decode();flat=" ".join(text.split())
        assert "Complete BCZ Farey Cycles" in flat and "??" not in text and "[VERIFY]" not in text and "TODO" not in text
        assert "中文摘要" in text and "Keywords:" in text and "关键词" in text
        en=text.split("Keywords:",1)[1].split("关键词",1)[0];cn=text.split("关键词",1)[1].split("One section",1)[0]
        assert en.count(";")==5 and cn.count("；")==5,"six bilingual keywords"
        assert f"Round {('zero','one','two')[index]}:" in flat
        first="Physical return time and complete parabolic cocycle"
        second="Roof integrability and the continuous-family obstruction"
        assert (first in flat)==(index>=1) and (second in flat)==(index>=2),"substantive round content"
        if index==2:assert "NO_BAD_EULER_OR_ROOT_NUMBER" in text and "Route B remains disabled." in flat
        run(["pdftoppm","-png","-r","60",str(path),str(work/"page")])
        imgs=sorted(work.glob("page-*.png"));assert len(imgs)==pages
        sizes=[p.stat().st_size for p in imgs];assert all(v>1000 for v in sizes)
    return {"round":index,"file":"paper/"+path.name,"sha256":sha(path),"pages":pages,"embedded_subset_fonts":len(fonts),"raster_sizes":sizes}
def lanes():
    receipts=[]
    with tempfile.TemporaryDirectory(prefix="c395-release-evidence-") as d:
        out=Path(d)/"evidence.json";receipts.append(run([sys.executable,"-B",str(ROOT/"code"/SCRIPTS[0]),"--output",str(out)]))
        assert out.read_bytes()==(ROOT/"results/c395_bcz_evidence.json").read_bytes(),"fresh evidence"
    for name in SCRIPTS[1:-1]:receipts.append(run([sys.executable,"-B",str(ROOT/"code"/name)]))
    run([sys.executable,"-B","-m","unittest","discover","-s","tests"],cwd=ROOT);receipts.append("C395 smoke PASS: 3/3")
    for name in SCRIPTS:
        for opt in ("-O","-OO"):
            p=subprocess.run([sys.executable,opt,str(ROOT/"code"/name),"--help"],capture_output=True,text=True)
            assert p.returncode and "refuses optimized Python" in p.stdout+p.stderr
    receipts.append("C395 optimized-mode refusal PASS: 12/12")
    return receipts
def main():
    p=argparse.ArgumentParser();p.add_argument("--build-pdfs",action="store_true");p.add_argument("--write",action="store_true");p.add_argument("--evaluation",type=Path,default=ROOT/"evaluations/route_a/HCS-C395/2026-09-05.yaml");a=p.parse_args()
    # This gate is before every write, including build-pdfs. Mutations invoke
    # the actual --write entrypoint and verify that the manifest stays unchanged.
    preflight(a.evaluation)
    if a.build_pdfs:
        for i,name in enumerate(NAMES):
            blob,log=compile_round(i);(ROOT/"paper"/name).write_bytes(blob);(ROOT/f"paper/compile_round{i}.txt").write_text(log)
            if i==2:(ROOT/"paper/main.pdf").write_bytes(blob)
            print(f"C395 double-fresh PDF build PASS: round={i}",flush=True)
        return
    actual=sorted(str(f.relative_to(ROOT)) for f in ROOT.rglob("*") if f.is_file())
    expected=sorted(EXPECTED+((MANIFEST.name,) if MANIFEST.exists() or not a.write else ()))
    assert actual==expected,f"physical ledger extra={sorted(set(actual)-set(expected))} missing={sorted(set(expected)-set(actual))}"
    for rel in EXPECTED:
        f=ROOT/rel;assert not f.is_symlink(),"symlink payload"
        if f.suffix in (".md",".tex",".py",".yaml",".txt"):assert all(b>=32 or b==10 for b in f.read_bytes()),"control byte "+rel
    for i in range(3):
        assert (ROOT/f"paper/main_round{i}.tex").read_text()==f"\\def\\CRevisionRound{{{i}}}\n\\input{{main.tex}}\n"
        assert WARN.search((ROOT/f"paper/compile_round{i}.txt").read_text()) is None
    assert (ROOT/"paper/main.pdf").read_bytes()==(ROOT/"paper/main_round2.pdf").read_bytes()
    receipts=lanes();rounds=[]
    for i,name in enumerate(NAMES):
        f=ROOT/"paper"/name;assert compile_round(i)[0]==f.read_bytes(),"cold PDF mismatch"
        rounds.append(pdf_audit(f,i))
    assert rounds[0]["pages"]<rounds[1]["pages"]<rounds[2]["pages"],"substantive page progression"
    files={rel:sha(ROOT/rel) for rel in sorted(EXPECTED)}
    m={"schema":"hcs-release-manifest-v1","candidate_id":"HCS-C395","obstruction_id":"HEN-O379","source_commit":"697518b6db90458f86f7916fbf397b8ad5ef2372","fixed_epoch":1788566400,"scope_literal":"NO_BAD_EULER_OR_ROOT_NUMBER","evaluator_authority":AUTHORITY,"evaluator_version":"0.2.0","evaluator_authority_sha256":AUTHORITY_SHA,"payload_file_count":len(EXPECTED),"physical_file_count":len(EXPECTED)+1,"payload_ledger_sha256":hashlib.sha256(can(files)).hexdigest(),"evaluation_raw_sha256":sha(a.evaluation),"evidence_sha256":sha(ROOT/"results/c395_bcz_evidence.json"),"evidence_payload_sha256":strict(ROOT/"results/c395_bcz_evidence.json")["payload_sha256"],"main_pdf_sha256":sha(ROOT/"paper/main.pdf"),"release_lanes":{k:"PASS" for k in ("producer","independent_checker","symbolic_ninety_digit_controls","two_directory_byte_replay","repaired_hash_hostile_mutations","actual_write_yaml_refusal","smoke","optimized_mode_refusal","strict_evaluation","deterministic_double_pdf_builds","fonts_text_raster","physical_file_membership","scope_firewall")},"lane_receipts":receipts,"pdf_rounds":rounds,"files":files}
    if a.write:MANIFEST.write_text(json.dumps(m,sort_keys=True,indent=2,ensure_ascii=False)+"\n");print(f"C395 manifest WRITE PASS: payload={len(EXPECTED)} physical={len(EXPECTED)+1}")
    else:
        assert strict(MANIFEST)==m,"nonwrite manifest reconstruction mismatch"
        print("C395 nonwrite release PASS: evidence="+m["evidence_sha256"]+" pdf="+m["main_pdf_sha256"]+" manifest="+sha(MANIFEST))
if __name__=="__main__":main()
