#!/usr/bin/env python3
"""Self-excluding exact payload release, with fresh reproducibility verification."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("c398 release refuses optimized Python")
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[1]
MANIFEST=ROOT/"C398_RELEASE_MANIFEST.json"
AUTHORITY="flow_systems/skills/route-a-evaluator.md"
AUTHORITY_SHA="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
NAMES=("main_round0_original.pdf","main_round1.pdf","main_round2.pdf")
SCRIPTS=("c398_wall_producer.py","c398_wall_checker.py","c398_wall_sympy_crosscheck.py","c398_wall_replay.py","c398_wall_mutation.py","c398_release_manifest.py")
EXPECTED=(
 "ASSUMPTIONS.md","CLAIMS.md","EXPERIMENT_PLAN.md","LIMITATIONS.md","NARRATIVE_REPORT.md",
 "PAPER_IMPROVEMENT_LOG.md","PAPER_PLAN.md","README.md","REFERENCES.md","REPRODUCIBILITY.md",
 "RESEARCH_QUESTION.md","SCOPE.md","SOURCE_AUDIT.md","THEOREM_PACKAGE.md","requirements.txt",
 "proof/ANALYTIC_PROOF.md","code/README.md",
 "code/c398_wall_producer.py","code/c398_wall_checker.py","code/c398_wall_sympy_crosscheck.py",
 "code/c398_wall_replay.py","code/c398_wall_mutation.py","code/c398_release_manifest.py",
 "evaluations/route_a/HCS-C398/2026-09-05.yaml","paper/README.md","paper/COMPILE_REPORT.md",
 "paper/main.tex","paper/main_round0.tex","paper/main_round1.tex","paper/main_round2.tex",
 "paper/main.pdf","paper/main_round0_original.pdf","paper/main_round1.pdf","paper/main_round2.pdf",
 "paper/compile_round0.txt","paper/compile_round1.txt","paper/compile_round2.txt",
 "results/RESULTS.md","results/TEST_REPORT.md","results/HOSTILE_AUDIT.md",
 "results/c398_wall_evidence.json","tests/test_c398_smoke.py",
 "review/ROUND0_REVIEW.md","review/ROUND1_REVIEW.md","review/ROUND2_REVIEW.md",
 "review/FAILURE_MODE_AUDIT.md","review/FINAL_INTEGRITY.md",
)
WARN=re.compile(r"(?:LaTeX|Package [^:\n]+) Warning:|warning  \(pdf backend\)|Overfull|Underfull|undefined (?:references|citations)|Rerun to get|Missing character")

def run(command,**kwargs):
    p=subprocess.run(command,capture_output=True,text=True,**kwargs)
    assert p.returncode==0,f"command failed {command}\n{p.stdout}\n{p.stderr}"
    return p.stdout.strip()

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def canonical(x): return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
def unique(pairs):
    out={}
    for k,v in pairs:
        assert k not in out,"duplicate JSON"
        out[k]=v
    return out
def strict(path): return json.loads(path.read_text(),object_pairs_hook=unique,parse_constant=lambda x:(_ for _ in ()).throw(ValueError(x)))

def compile_round(index):
    blobs=[]; logs=[]
    for build in range(2):
        with tempfile.TemporaryDirectory(prefix=f"c398-tex-{index}-{build}-") as d:
            work=Path(d)
            for name in ("main.tex",f"main_round{index}.tex"):
                shutil.copy2(ROOT/"paper"/name,work/name)
            command=["lualatex","-interaction=nonstopmode","-halt-on-error","-jobname=main",f"main_round{index}.tex"]
            env=dict(os.environ,SOURCE_DATE_EPOCH="1788566400",FORCE_SOURCE_DATE="1")
            run(command,cwd=work,env=env); run(command,cwd=work,env=env)
            log=(work/"main.log").read_text(errors="replace")
            match=WARN.search(log)
            assert match is None,f"round {index} settled warning: "+log[max(0,match.start()-80):match.start()+600]
            logs.append(log); blobs.append((work/"main.pdf").read_bytes())
    assert blobs[0]==blobs[1],f"round {index} PDF bytes differ"
    return blobs[0],logs[0]

def pdf_audit(path,index):
    info=run(["pdfinfo",str(path)]); m=re.search(r"^Pages:\s+(\d+)",info,re.M); assert m
    pages=int(m.group(1)); fonts=run(["pdffonts",str(path)]).splitlines()[2:]
    assert fonts
    for line in fonts:
        cols=line.split(); assert cols[-5:-3]==["yes","yes"],line
    assert any("DroidSansFallback" in line.replace(" ","") for line in fonts)
    with tempfile.TemporaryDirectory(prefix="c398-pdf-audit-") as d:
        work=Path(d); target=work/"text.txt"
        run(["pdftotext",str(path),str(target)])
        raw=target.read_bytes(); assert all(b>=32 or b in (10,12,13) for b in raw)
        text=raw.decode(); flat=" ".join(text.split())
        assert "The Exponential Wall" in flat
        assert "??" not in text and "[VERIFY]" not in text and "TODO" not in text
        assert "Keywords:" in text and "中文摘要" in text and "关键词" in text
        en=text.split("Keywords:",1)[1].split("中文摘要",1)[0]
        cn=text.split("关键词",1)[1].split("1",1)[0]
        assert en.count(";")==5 and cn.count("；")==5
        assert f"Round {('zero','one','two')[index]}" in flat
        assert ("An exact phase and bounded Weyl residual" in flat)==(index>=1)
        assert ("Heat trace and all-parameter nonmatching theorem" in flat)==(index>=2)
        if index==2:assert "NO_BAD_EULER_OR_ROOT_NUMBER" in text
        run(["pdftoppm","-png","-r","60",str(path),str(work/"page")])
        images=sorted(work.glob("page-*.png")); assert len(images)==pages
        assert all(p.stat().st_size>1000 for p in images)
        sizes=[p.stat().st_size for p in images]
    return {"round":index,"file":"paper/"+path.name,"sha256":sha(path),"pages":pages,"embedded_subset_fonts":len(fonts),"raster_sizes":sizes}

def lanes():
    output=[]
    with tempfile.TemporaryDirectory(prefix="c398-release-evidence-") as d:
        target=Path(d)/"evidence.json"
        output.append(run([sys.executable,"-B",str(ROOT/"code/c398_wall_producer.py"),"--output",str(target)]))
        assert target.read_bytes()==(ROOT/"results/c398_wall_evidence.json").read_bytes()
    for name in SCRIPTS[1:-1]: output.append(run([sys.executable,"-B",str(ROOT/"code"/name)]))
    run([sys.executable,"-B","-m","unittest","tests/test_c398_smoke.py"],cwd=ROOT)
    output.append("C398 smoke PASS: 3/3")
    for name in SCRIPTS:
        for flag in ("-O","-OO"):
            p=subprocess.run([sys.executable,flag,str(ROOT/"code"/name),"--help"],capture_output=True,text=True)
            assert p.returncode and "refuses optimized Python" in p.stdout+p.stderr
    return output

def source_gate():
    assert sha(REPO/AUTHORITY)==AUTHORITY_SHA
    evidence=strict(ROOT/"results/c398_wall_evidence.json")
    assert all(v is False for v in evidence["scope_flags"].values())
    assert evidence["route_a"]["route_b_invocation_allowed"] is False
    assert evidence["scope_literal"]=="NO_BAD_EULER_OR_ROOT_NUMBER"
    for relative in EXPECTED:
        p=ROOT/relative
        if p.suffix in (".md",".tex",".py",".yaml",".txt"):
            raw=p.read_bytes(); assert all(b>=32 or b in (10,13) for b in raw),relative
    for i in range(3):
        assert (ROOT/f"paper/main_round{i}.tex").read_text()==f"\\def\\CRevisionRound{{{i}}}\n\\input{{main.tex}}\n"
        assert WARN.search((ROOT/f"paper/compile_round{i}.txt").read_text()) is None
    assert (ROOT/"paper/main.pdf").read_bytes()==(ROOT/"paper/main_round2.pdf").read_bytes()

def main():
    p=argparse.ArgumentParser(); p.add_argument("--build-pdfs",action="store_true");p.add_argument("--write",action="store_true");a=p.parse_args()
    assert not any(f.is_symlink() for f in ROOT.rglob("*")),"symlink payload refused"
    from c398_wall_checker import check, evaluation
    check(ROOT/"results/c398_wall_evidence.json")
    evaluation(ROOT/"evaluations/route_a/HCS-C398/2026-09-05.yaml")
    assert sha(REPO/AUTHORITY)==AUTHORITY_SHA
    if a.build_pdfs:
        for i,name in enumerate(NAMES):
            blob,log=compile_round(i)
            (ROOT/"paper"/name).write_bytes(blob)
            (ROOT/f"paper/compile_round{i}.txt").write_text(log)
            if i==2:(ROOT/"paper/main.pdf").write_bytes(blob)
            print("C398 double-fresh PDF build PASS: round="+str(i),flush=True)
        return
    actual=sorted(str(f.relative_to(ROOT)) for f in ROOT.rglob("*") if f.is_file())
    expected=sorted(EXPECTED+((MANIFEST.name,) if MANIFEST.exists() or not a.write else ()))
    assert actual==expected,f"physical ledger extra={sorted(set(actual)-set(expected))} missing={sorted(set(expected)-set(actual))}"
    source_gate(); receipts=lanes(); rounds=[]
    for i,name in enumerate(NAMES):
        path=ROOT/"paper"/name
        assert compile_round(i)[0]==path.read_bytes(),"fresh PDF mismatch"
        rounds.append(pdf_audit(path,i))
    assert len({r["sha256"] for r in rounds})==3,"revision PDFs must differ"
    lengths=[len(run(["pdftotext",str(ROOT/r["file"]),"-"])) for r in rounds]
    assert lengths[0]<lengths[1]<lengths[2],"revision text must grow with the checked new theorem sections"
    assert rounds[0]["pages"]<=rounds[1]["pages"]<=rounds[2]["pages"]
    files={f:sha(ROOT/f) for f in sorted(EXPECTED)}
    evaluation=ROOT/"evaluations/route_a/HCS-C398/2026-09-05.yaml"
    m={"schema":"hcs-release-manifest-v1","candidate_id":"HCS-C398","obstruction_id":"HEN-O382","source_commit":"697518b6db90458f86f7916fbf397b8ad5ef2372","fixed_epoch":1788566400,"scope_literal":"NO_BAD_EULER_OR_ROOT_NUMBER","evaluator_authority":AUTHORITY,"evaluator_version":"0.2.0","evaluator_authority_sha256":AUTHORITY_SHA,"payload_file_count":len(EXPECTED),"physical_file_count":len(EXPECTED)+1,"payload_ledger_sha256":hashlib.sha256(canonical(files)).hexdigest(),"evaluation_raw_sha256":sha(evaluation),"evidence_sha256":sha(ROOT/"results/c398_wall_evidence.json"),"evidence_payload_sha256":strict(ROOT/"results/c398_wall_evidence.json")["payload_sha256"],"main_pdf_sha256":sha(ROOT/"paper/main.pdf"),"release_lanes":{k:"PASS" for k in ("producer","independent_checker","symbolic_high_precision","two_directory_byte_replay","repaired_hash_hostile_mutations","smoke","optimized_mode_refusal","strict_evaluation","deterministic_double_pdf_builds","fonts_text_raster","physical_file_membership","scope_firewall")},"lane_receipts":receipts,"pdf_rounds":rounds,"files":files}
    if a.write:
        MANIFEST.write_text(json.dumps(m,sort_keys=True,indent=2,ensure_ascii=False)+"\n")
        print(f"C398 manifest WRITE PASS: payload={len(EXPECTED)} physical={len(EXPECTED)+1}")
    else:
        assert canonical(strict(MANIFEST))==canonical(m),"manifest mismatch on nonwrite reconstruction"
        print("C398 nonwrite release PASS: evidence="+m["evidence_sha256"]+" pdf="+m["main_pdf_sha256"]+" manifest="+sha(MANIFEST))

if __name__=="__main__":main()
