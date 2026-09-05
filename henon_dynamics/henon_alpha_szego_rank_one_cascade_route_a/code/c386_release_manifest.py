#!/usr/bin/env python3
"""Content-addressed release, deterministic three-round LuaLaTeX build and checks."""
if not __debug__:raise RuntimeError("c386 release refuses optimized Python")
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
ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/"C386_RELEASE_MANIFEST.json"
PDFS=("main_round0_original.pdf","main_round1.pdf","main_round2.pdf")
WARN=re.compile(r"Overfull|Underfull|LaTeX Warning:.*(?:undefined|multiply)|Missing character|Package .* Warning|Font Warning")
REQUIRED=("README.md","RESEARCH_QUESTION.md","ASSUMPTIONS.md","CLAIMS.md","THEOREM_PACKAGE.md","SCOPE.md","LIMITATIONS.md","REFERENCES.md","SOURCE_AUDIT.md","NARRATIVE_REPORT.md","EXPERIMENT_PLAN.md","PAPER_PLAN.md","PAPER_IMPROVEMENT_LOG.md","REPRODUCIBILITY.md","CROSS_REVIEW.md","requirements.txt","proof/ANALYTIC_PROOF.md","code/README.md","code/c386_szego_producer.py","code/c386_szego_checker.py","code/c386_szego_sympy_crosscheck.py","code/c386_szego_replay.py","code/c386_szego_mutation.py","code/c386_release_manifest.py","tests/test_c386_smoke.py","evaluations/route_a/HCS-C386/2026-09-05.yaml","results/c386_szego_evidence.json","results/RESULTS.md","results/TEST_REPORT.md","results/HOSTILE_AUDIT.md","paper/README.md","paper/main.tex","paper/main_round0.tex","paper/main_round1.tex","paper/main_round2.tex","paper/main_round0_original.pdf","paper/main_round1.pdf","paper/main_round2.pdf","paper/main.pdf","paper/build_round0.txt","paper/build_round1.txt","paper/build_round2.txt","paper/COMPILE_REPORT.md")
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def run(command,**kw):
    p=subprocess.run(command,capture_output=True,text=True,**kw)
    if p.returncode:raise RuntimeError(p.stdout+p.stderr)
    return p.stdout+p.stderr
def compile_round(index,write_log=False):
    blobs=[];logs=[]
    for repeat in range(2):
        with tempfile.TemporaryDirectory(prefix=f"c386-r{index}-b{repeat}-") as directory:
            p=Path(directory)
            for name in ("main.tex",f"main_round{index}.tex"):shutil.copy2(ROOT/"paper"/name,p/name)
            env=dict(os.environ,SOURCE_DATE_EPOCH="1788566400",FORCE_SOURCE_DATE="1")
            command=["lualatex","-interaction=nonstopmode","-halt-on-error","-jobname=main",f"main_round{index}.tex"]
            run(command,cwd=p,env=env);run(command,cwd=p,env=env)
            log=(p/"main.log").read_text(errors="replace")
            # Absolute temp paths in logs are normalized; PDFs remain original bytes.
            normalized=log.replace(str(p),"<BUILD_ROOT>")
            if write_log:(ROOT/"paper"/f"build_round{index}.txt").write_text(normalized)
            assert not WARN.search(log),f"settled compile warning round {index}"
            blobs.append((p/"main.pdf").read_bytes());logs.append(normalized)
    assert blobs[0]==blobs[1],f"round {index} nondeterministic"
    return blobs[0]
def pdf_gate(path,index):
    info=run(["pdfinfo",str(path)]);pages=int(re.search(r"Pages:\s+(\d+)",info).group(1));assert 2<=pages<=10
    fonts=run(["pdffonts",str(path)]).splitlines()[2:];assert fonts
    for line in fonts:
        c=line.split();assert c[-5]=="yes" and c[-4]=="yes",line
    assert any("DroidSansFallback" in line for line in fonts)
    with tempfile.TemporaryDirectory(prefix="c386-pdf-gate-") as directory:
        work=Path(directory);run(["pdftotext",str(path),str(work/"paper.txt")]);raw=(work/"paper.txt").read_bytes()
        assert all(c>=32 or c in (10,12,13) for c in raw)
        text=raw.decode();flat=" ".join(text.split())
        assert "中文摘要" in text and "关键词" in text and "Keywords:" in text
        assert "??" not in text and "[VERIFY]" not in text and "TODO" not in text
        marker=("Round zero: exact nonlinear reduction and compactness","Round one: turning-point-safe cascade theorem","Round two: Sobolev cascade and determinant blindness")[index]
        assert marker in flat
        if index==0:assert "Turning-point-safe cascade" not in flat
        if index==1:assert "The same determinant sees opposite dynamics" not in flat
        if index==2:assert "NO_BAD_EULER_OR_ROOT_NUMBER" in flat and "144 generic rational rows" in flat
        run(["pdftoppm","-png","-r","60",str(path),str(work/"page")]);rasters=sorted(work.glob("page-*.png"));assert len(rasters)==pages
        sizes=[p.stat().st_size for p in rasters];assert min(sizes)>1000
    return {"round":index,"path":"paper/"+path.name,"sha256":sha(path),"bytes":path.stat().st_size,"pages":pages,"embedded_subset_font_rows":len(fonts),"raster_bytes":sizes}
def compile_all(write):
    rows=[]
    for i,name in enumerate(PDFS):
        blob=compile_round(i,write);path=ROOT/"paper"/name
        if write:path.write_bytes(blob)
        else:assert path.read_bytes()==blob,f"stale PDF {name}"
        rows.append(pdf_gate(path,i))
    if write:(ROOT/"paper/main.pdf").write_bytes((ROOT/"paper"/PDFS[2]).read_bytes())
    assert (ROOT/"paper/main.pdf").read_bytes()==(ROOT/"paper"/PDFS[2]).read_bytes()
    assert rows[0]["pages"]<rows[1]["pages"]<rows[2]["pages"]
    assert len({r["sha256"] for r in rows})==3
    if write:
        lines=["# C386 compilation report","","Status: PASS. Three substantive rounds; each compiled twice in two fresh directories using LuaLaTeX, two passes per directory. Epoch 1788566400. Settled logs retained; no overfull/underfull, missing-glyph, undefined-reference, citation, or font warnings. All fonts embedded and subset. Raster rendering checked for every page; visual inspection is separately recorded in CROSS_REVIEW.md.","","| Round | Pages | SHA-256 |","|---|---:|---|"]
        lines += [f"| {r['round']} | {r['pages']} | `{r['sha256']}` |" for r in rows]
        lines += ["","`paper/main.pdf` is byte-identical to round two. No target venue or submission-readiness certification is asserted.",""]
        (ROOT/"paper/COMPILE_REPORT.md").write_text("\n".join(lines))
    return rows
def lanes():
    reports=[]
    with tempfile.TemporaryDirectory(prefix="c386-release-producer-") as directory:
        output=Path(directory)/"e.json";run([sys.executable,"-B",str(ROOT/"code/c386_szego_producer.py"),"--output",str(output)])
        assert output.read_bytes()==(ROOT/"results/c386_szego_evidence.json").read_bytes()
    for name in ("checker","sympy_crosscheck","replay","mutation"):
        reports.append(run([sys.executable,"-B",str(ROOT/f"code/c386_szego_{name}.py")]).strip())
    reports.append(run([sys.executable,"-B","-m","unittest","tests/test_c386_smoke.py"],cwd=ROOT).strip())
    for script in ROOT.glob("code/*.py"):
        for flag in ("-O","-OO"):
            p=subprocess.run([sys.executable,flag,str(script),"--help"],capture_output=True,text=True)
            assert p.returncode and "refuses optimized Python" in p.stdout+p.stderr
    return reports
def make_manifest(rounds):
    actual=sorted(str(p.relative_to(ROOT)) for p in ROOT.rglob("*") if p.is_file() and "__pycache__" not in p.parts and p!=MANIFEST)
    assert actual==sorted(REQUIRED),f"ledger mismatch extra={set(actual)-set(REQUIRED)} missing={set(REQUIRED)-set(actual)}"
    evidence=json.loads((ROOT/"results/c386_szego_evidence.json").read_text());flags=evidence["scope_flags"]
    assert all(v is False for v in flags.values()) and evidence["route_a"]["route_b_invocation_allowed"] is False
    for relative in REQUIRED:
        p=ROOT/relative
        if p.suffix in (".md",".tex",".py",".yaml",".txt"):
            assert all(c>=32 or c in (10,13) for c in p.read_bytes()),relative
    return {"schema":"hcs-release-manifest-v1","candidate_id":"HCS-C386","obstruction_id":"HEN-O370","source_commit":"3e692da6fa94362225c7534e9b66c83c15c7f284","fixed_epoch":1788566400,"scope_literal":"NO_BAD_EULER_OR_ROOT_NUMBER","payload_file_count":len(REQUIRED),"physical_file_count":len(REQUIRED)+1,"evidence_sha256":sha(ROOT/"results/c386_szego_evidence.json"),"evidence_payload_sha256":evidence["payload_sha256"],"main_pdf_sha256":sha(ROOT/"paper/main.pdf"),"evaluator_authority_sha256":evidence["evaluator"]["sha256"],"evaluation_raw_sha256":evidence["route_a_yaml"]["raw_sha256"],"evaluation_semantic_sha256":evidence["route_a_yaml"]["semantic_sha256"],"pdf_rounds":rounds,"release_lanes":{k:"PASS" for k in ("canonical_producer","independent_checker","sympy","two_directory_replay","repaired_hash_mutations","smoke","optimized_refusal","deterministic_pdf","fonts","raster","scope_firewall","ledger")},"files":{r:sha(ROOT/r) for r in sorted(REQUIRED)}}
def main():
    p=argparse.ArgumentParser();p.add_argument("--build-pdfs",action="store_true");p.add_argument("--write",action="store_true");a=p.parse_args()
    run([sys.executable,"-B",str(ROOT/"code/c386_szego_checker.py"),"--yaml-only"])
    if a.build_pdfs:
        rows=compile_all(True);print("C386 three-round PDF PASS",json.dumps(rows));return
    outputs=lanes();rounds=compile_all(False);manifest=make_manifest(rounds);blob=json.dumps(manifest,sort_keys=True,indent=2).encode()+b"\n"
    if a.write:MANIFEST.write_bytes(blob)
    else:assert MANIFEST.read_bytes()==blob,"stale release manifest"
    print("C386 release PASS",json.dumps(outputs));print("manifest_sha256="+hashlib.sha256(blob).hexdigest())
if __name__=="__main__":main()
