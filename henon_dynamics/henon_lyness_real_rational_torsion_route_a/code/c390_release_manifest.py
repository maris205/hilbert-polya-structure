#!/usr/bin/env python3
"""Self-excluding exact release; write mode obeys the same validation gates."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("c390 release refuses optimized Python")
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
MANIFEST=ROOT/"C390_RELEASE_MANIFEST.json"
AUTHORITY="flow_systems/skills/route-a-evaluator.md"
AUTHORITY_SHA="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCRIPTS=("c390_lyness_producer.py","c390_lyness_checker.py","c390_lyness_sympy_crosscheck.py","c390_lyness_replay.py","c390_lyness_mutation.py","c390_release_manifest.py")
NAMES=("main_round0_original.pdf","main_round1.pdf","main_round2.pdf")
EXPECTED=(
 "README.md","PROJECT_README.md","RESEARCH_QUESTION.md","ASSUMPTIONS.md","SCOPE.md","LIMITATIONS.md",
 "THEOREM_PACKAGE.md","CLAIMS.md","NARRATIVE_REPORT.md","EXPERIMENT_PLAN.md","REFERENCES.md","SOURCE_AUDIT.md","REPRODUCIBILITY.md",
 "PAPER_PLAN.md","PAPER_IMPROVEMENT_LOG.md","requirements.txt","proof/ANALYTIC_PROOF.md",
 "code/README.md","code/c390_lyness_producer.py","code/c390_lyness_checker.py","code/c390_lyness_sympy_crosscheck.py",
 "code/c390_lyness_replay.py","code/c390_lyness_mutation.py","code/c390_release_manifest.py",
 "evaluations/route_a/HCS-C390/2026-09-05.yaml","tests/test_c390_smoke.py",
 "paper/README.md","paper/COMPILE_REPORT.md","paper/main.tex","paper/main_round0.tex","paper/main_round1.tex","paper/main_round2.tex",
 "paper/main.pdf","paper/main_round0_original.pdf","paper/main_round1.pdf","paper/main_round2.pdf",
 "paper/compile_round0.txt","paper/compile_round1.txt","paper/compile_round2.txt",
 "results/c390_lyness_evidence.json","results/RESULTS.md","results/TEST_REPORT.md","results/HOSTILE_AUDIT.md",
 "review/CROSS_REVIEW.md","review/FAILURE_MODE_AUDIT.md","review/CLAIM_REFERENCE_AUDIT.md","review/FINAL_INTEGRITY.md","review/SOURCE_PAGE_RECEIPT.md",
)
WARN=re.compile(r"(?:LaTeX|Package [^:\n]+) Warning:|warning  \(pdf backend\)|Overfull|Underfull|undefined (?:references|citations)|Rerun to get|Missing character")
def run(command,**kwargs):
    p=subprocess.run(command,capture_output=True,text=True,**kwargs)
    assert p.returncode==0,f"command failed {command}\n{p.stdout}\n{p.stderr}"
    return p.stdout.strip()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def canonical(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
def unique(pairs):
    d={}
    for k,v in pairs:assert k not in d,"duplicate JSON";d[k]=v
    return d
def strict(p):return json.loads(p.read_text(),object_pairs_hook=unique,parse_constant=lambda x:(_ for _ in ()).throw(ValueError(x)))
def compile_round(index):
    blobs=[];logs=[]
    for build in range(2):
        with tempfile.TemporaryDirectory(prefix=f"c390-tex-{index}-{build}-") as d:
            work=Path(d)
            for name in ("main.tex",f"main_round{index}.tex"):shutil.copy2(ROOT/"paper"/name,work/name)
            cmd=["lualatex","-interaction=nonstopmode","-halt-on-error","-jobname=main",f"main_round{index}.tex"]
            env=dict(os.environ,SOURCE_DATE_EPOCH="1788566400",FORCE_SOURCE_DATE="1")
            run(cmd,cwd=work,env=env);run(cmd,cwd=work,env=env)
            log=(work/"main.log").read_text(errors="replace");match=WARN.search(log)
            assert match is None,f"round {index} settled warning: "+log[max(0,match.start()-80):match.start()+700]
            blobs.append((work/"main.pdf").read_bytes());logs.append(log)
    assert blobs[0]==blobs[1],"nondeterministic PDF"
    return blobs[0],logs[0]
def pdf_audit(path,index):
    info=run(["pdfinfo",str(path)]);m=re.search(r"^Pages:\s+(\d+)",info,re.M);assert m;pages=int(m.group(1))
    fonts=run(["pdffonts",str(path)]).splitlines()[2:];assert fonts
    for line in fonts:assert line.split()[-5:-3]==["yes","yes"],line
    assert any("DroidSansFallback" in line.replace(" ","") for line in fonts)
    with tempfile.TemporaryDirectory(prefix="c390-pdf-audit-") as d:
        work=Path(d);out=work/"text.txt";run(["pdftotext",str(path),str(out)])
        raw=out.read_bytes();assert all(b>=32 or b in (10,12,13) for b in raw)
        text=raw.decode();flat=" ".join(text.split())
        assert "Positive Lyness Dynamics" in flat
        assert "??" not in text and "[VERIFY]" not in text and "TODO" not in text
        assert "中文摘要" in text and "Keywords:" in text and "关键词" in text
        en=text.split("Keywords:",1)[1].split("关键词",1)[0];cn=text.split("关键词",1)[1].split("One source",1)[0]
        assert en.count(";")==5 and cn.count("；")==5,"keyword count"
        assert f"Round {('zero','one','two')[index]}:" in flat
        if index==0:
            assert "Smooth cubics, exceptional parameters and rational torsion" not in flat
            assert "Real prime periods and the operator stopping result" not in flat
        elif index==1:
            assert "Smooth cubics, exceptional parameters and rational torsion" in flat
            assert "Real prime periods and the operator stopping result" not in flat
        else:
            assert "Real prime periods and the operator stopping result" in flat
            assert "NO_BAD_EULER_OR_ROOT_NUMBER" in text and "Route B remains disabled." in flat
        run(["pdftoppm","-png","-r","60",str(path),str(work/"page")])
        imgs=sorted(work.glob("page-*.png"));assert len(imgs)==pages
        sizes=[p.stat().st_size for p in imgs];assert all(n>1000 for n in sizes)
    return {"round":index,"file":"paper/"+path.name,"sha256":sha(path),"pages":pages,"embedded_subset_fonts":len(fonts),"raster_sizes":sizes}
def lanes():
    receipts=[]
    with tempfile.TemporaryDirectory(prefix="c390-release-evidence-") as d:
        out=Path(d)/"evidence.json";receipts.append(run([sys.executable,"-B",str(ROOT/"code/c390_lyness_producer.py"),"--output",str(out)]))
        assert out.read_bytes()==(ROOT/"results/c390_lyness_evidence.json").read_bytes()
    for name in SCRIPTS[1:-1]:receipts.append(run([sys.executable,"-B",str(ROOT/"code"/name)]))
    run([sys.executable,"-B","-m","unittest","discover","-s","tests"],cwd=ROOT);receipts.append("C390 smoke PASS: 3/3")
    for name in SCRIPTS:
        for flag in ("-O","-OO"):
            p=subprocess.run([sys.executable,flag,str(ROOT/"code"/name),"--help"],capture_output=True,text=True)
            assert p.returncode and "refuses optimized Python" in p.stdout+p.stderr
    receipts.append("C390 optimized-mode refusal PASS: 12/12")
    return receipts
def source_gate():
    assert sha(REPO/AUTHORITY)==AUTHORITY_SHA
    # This exact strict gate is mandatory in --write and nonwrite modes alike.
    run([sys.executable,"-B",str(ROOT/"code/c390_lyness_checker.py"),"--evaluation-only"])
    x=strict(ROOT/"results/c390_lyness_evidence.json")
    assert x["scope_literal"]=="NO_BAD_EULER_OR_ROOT_NUMBER" and all(v is False for v in x["scope_flags"].values())
    assert x["route_a"]["route_b_invocation_allowed"] is False
    for relative in EXPECTED:
        p=ROOT/relative;assert not p.is_symlink(),"symlink payload"
        if p.suffix in (".md",".tex",".py",".yaml",".txt"):
            raw=p.read_bytes();assert all(b>=32 or b==10 for b in raw),"control byte "+relative
    for i in range(3):
        assert (ROOT/f"paper/main_round{i}.tex").read_text()==f"\\def\\CRevisionRound{{{i}}}\n\\input{{main.tex}}\n"
        assert WARN.search((ROOT/f"paper/compile_round{i}.txt").read_text()) is None
    assert (ROOT/"paper/main.pdf").read_bytes()==(ROOT/"paper/main_round2.pdf").read_bytes()
def main():
    p=argparse.ArgumentParser();p.add_argument("--build-pdfs",action="store_true");p.add_argument("--write",action="store_true");a=p.parse_args()
    if a.build_pdfs:
        for i,name in enumerate(NAMES):
            blob,log=compile_round(i);(ROOT/"paper"/name).write_bytes(blob);(ROOT/f"paper/compile_round{i}.txt").write_text(log)
            if i==2:(ROOT/"paper/main.pdf").write_bytes(blob)
            print("C390 double-fresh PDF build PASS: round="+str(i),flush=True)
        return
    actual=sorted(str(f.relative_to(ROOT)) for f in ROOT.rglob("*") if f.is_file())
    expected=sorted(EXPECTED+((MANIFEST.name,) if MANIFEST.exists() or not a.write else ()))
    assert actual==expected,f"physical ledger extra={sorted(set(actual)-set(expected))} missing={sorted(set(expected)-set(actual))}"
    source_gate();receipts=lanes();rounds=[]
    for i,name in enumerate(NAMES):
        path=ROOT/"paper"/name;assert compile_round(i)[0]==path.read_bytes(),"fresh PDF mismatch"
        rounds.append(pdf_audit(path,i))
    assert rounds[0]["pages"]<rounds[1]["pages"]<rounds[2]["pages"]
    files={p:sha(ROOT/p) for p in sorted(EXPECTED)}
    m={"schema":"hcs-release-manifest-v1","candidate_id":"HCS-C390","obstruction_id":"HEN-O374","source_commit":"0c877206d202f732e21ea0b194f9c7fdf30467ee","fixed_epoch":1788566400,"scope_literal":"NO_BAD_EULER_OR_ROOT_NUMBER","evaluator_authority":AUTHORITY,"evaluator_version":"0.2.0","evaluator_authority_sha256":AUTHORITY_SHA,"payload_file_count":len(EXPECTED),"physical_file_count":len(EXPECTED)+1,"payload_ledger_sha256":hashlib.sha256(canonical(files)).hexdigest(),"evaluation_raw_sha256":sha(ROOT/"evaluations/route_a/HCS-C390/2026-09-05.yaml"),"evidence_sha256":sha(ROOT/"results/c390_lyness_evidence.json"),"evidence_payload_sha256":strict(ROOT/"results/c390_lyness_evidence.json")["payload_sha256"],"main_pdf_sha256":sha(ROOT/"paper/main.pdf"),"release_lanes":{k:"PASS" for k in ("producer","independent_checker","symbolic_high_precision","two_directory_byte_replay","repaired_hash_hostile_mutations","smoke","optimized_mode_refusal","strict_evaluation","deterministic_double_pdf_builds","fonts_text_raster","physical_file_membership","scope_firewall")},"lane_receipts":receipts,"pdf_rounds":rounds,"files":files}
    if a.write:
        MANIFEST.write_text(json.dumps(m,sort_keys=True,indent=2,ensure_ascii=False)+"\n");print(f"C390 manifest WRITE PASS: payload={len(EXPECTED)} physical={len(EXPECTED)+1}")
    else:
        assert strict(MANIFEST)==m,"manifest differs on nonwrite reconstruction"
        print("C390 nonwrite release PASS: evidence="+m["evidence_sha256"]+" pdf="+m["main_pdf_sha256"]+" manifest="+sha(MANIFEST))
if __name__=="__main__":main()
