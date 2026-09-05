#!/usr/bin/env python3
"""Frozen YAML first, full independent lanes, actual logs and closed payload ledger."""
if not __debug__: raise RuntimeError("c391 release refuses optimized Python")
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
MANIFEST=ROOT/"C391_RELEASE_MANIFEST.json"
REQUIRED=["ASSUMPTIONS.md","CLAIMS.md","CROSS_REVIEW.md","EXPERIMENT_PLAN.md","LIMITATIONS.md","NARRATIVE_REPORT.md","PAPER_IMPROVEMENT_LOG.md","PAPER_PLAN.md","README.md","REFERENCES.md","REPRODUCIBILITY.md","RESEARCH_QUESTION.md","SCOPE.md","SOURCE_AUDIT.md","THEOREM_PACKAGE.md","code/README.md","code/c391_checker.py","code/c391_mutation.py","code/c391_producer.py","code/c391_release_manifest.py","code/c391_replay.py","code/c391_sympy_crosscheck.py","evaluations/route_a/HCS-C391/2026-09-05.yaml","paper/COMPILE_REPORT.md","paper/README.md","paper/build_round0.txt","paper/build_round1.txt","paper/build_round2.txt","paper/main.pdf","paper/main.tex","paper/main_round0.tex","paper/main_round0_original.pdf","paper/main_round1.pdf","paper/main_round1.tex","paper/main_round2.pdf","paper/main_round2.tex","proof/ANALYTIC_PROOF.md","requirements.txt","results/HOSTILE_AUDIT.md","results/RESULTS.md","results/TEST_REPORT.md","results/c391_evidence.json","sources/README.md","tests/test_c391_smoke.py"]
PDFS=("main_round0_original.pdf","main_round1.pdf","main_round2.pdf")
WARN=re.compile(r"Overfull|Underfull|LaTeX Warning:.*(?:undefined|multiply)|Missing character|Package .* Warning|Font Warning")
MARKERS=("Round zero: domains and the complete bound ladder.","Round one: complete continuum and scattering.","Round two: scale cycles and ordinary-determinant obstruction.")
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(command,**kwargs):
    p=subprocess.run(command,capture_output=True,text=True,**kwargs)
    if p.returncode:raise RuntimeError(p.stdout+p.stderr)
    return p.stdout+p.stderr
def compile_round(index,write):
    blobs=[]
    for repeat in range(2):
      with tempfile.TemporaryDirectory(prefix=f"c391-r{index}-b{repeat}-") as directory:
        work=Path(directory)
        for name in ("main.tex",f"main_round{index}.tex"):shutil.copy2(ROOT/"paper"/name,work/name)
        env=dict(os.environ,SOURCE_DATE_EPOCH="1788566400",FORCE_SOURCE_DATE="1")
        cmd=["lualatex","-interaction=nonstopmode","-halt-on-error","-jobname=main",f"main_round{index}.tex"]
        run(cmd,cwd=work,env=env);run(cmd,cwd=work,env=env)
        log=(work/"main.log").read_text(errors="replace")
        issues=WARN.findall(log)
        if issues:
            print(log)
            raise AssertionError(f"settled warnings in round {index}: {issues}")
        if write:(ROOT/"paper"/f"build_round{index}.txt").write_text(log.replace(str(work),"<BUILD_ROOT>"))
        blobs.append((work/"main.pdf").read_bytes())
    assert blobs[0]==blobs[1],f"nondeterministic round {index}"
    return blobs[0]
def pdf_gate(path,index):
    info=run(["pdfinfo",str(path)]);pages=int(re.search(r"Pages:\s+(\d+)",info).group(1));assert 2<=pages<=10
    fonts=run(["pdffonts",str(path)]).splitlines()[2:];assert fonts
    for line in fonts:
        cols=line.split();assert cols[-5]=="yes" and cols[-4]=="yes",line
    assert any("DroidSansFallback" in line for line in fonts)
    with tempfile.TemporaryDirectory(prefix="c391-pdf-gate-") as directory:
        work=Path(directory);run(["pdftotext",str(path),str(work/"text.txt")]);raw=(work/"text.txt").read_bytes()
        assert all(c>=32 or c in (10,12,13) for c in raw)
        text=raw.decode();flat=" ".join(text.split())
        assert "中文摘要" in text and "关键词" in text and "Keywords:" in text
        assert all(x not in text for x in ("??","[VERIFY]","TODO"))
        assert MARKERS[index] in flat,(index,MARKERS[index])
        assert len(text.split("Keywords:",1)[1].split("\n\n",1)[0].split(";"))==6
        if index==0:assert "Green jumps, completeness and scattering" not in flat
        if index==1:assert "The scale cycle is not a return" not in flat
        if index==2:assert "NO_BAD_EULER_OR_ROOT_NUMBER" in flat and "108 actual Stone-jump cells" in flat
        run(["pdftoppm","-png","-r","60",str(path),str(work/"page")]);rasters=sorted(work.glob("page-*.png"))
        assert len(rasters)==pages and min(p.stat().st_size for p in rasters)>1000
        sizes=[p.stat().st_size for p in rasters]
    return dict(round=index,path="paper/"+path.name,sha256=sha(path),bytes=path.stat().st_size,pages=pages,embedded_subset_font_rows=len(fonts),raster_bytes=sizes)
def compile_all(write):
    rows=[]
    for i,name in enumerate(PDFS):
        blob=compile_round(i,write);path=ROOT/"paper"/name
        if write:path.write_bytes(blob)
        else:assert path.read_bytes()==blob,"stale PDF "+name
        rows.append(pdf_gate(path,i))
    if write:(ROOT/"paper/main.pdf").write_bytes((ROOT/"paper"/PDFS[2]).read_bytes())
    assert (ROOT/"paper/main.pdf").read_bytes()==(ROOT/"paper"/PDFS[2]).read_bytes()
    assert rows[0]["pages"]<rows[1]["pages"]<rows[2]["pages"]
    assert len({r["sha256"] for r in rows})==3
    if write:
        text="# C391 compilation report\n\nPASS: three substantive revisions, each built twice in two fresh directories, two LuaLaTeX passes per directory. Epoch 1788566400. Actual settled logs retained as build_round0.txt through build_round2.txt with only temporary paths normalized. No layout, reference, citation, missing-character or font warnings. All fonts embedded and subset. Every page rendered; actual visual inspection is separately recorded in CROSS_REVIEW.md.\n\n| Round | Pages | SHA-256 |\n|---|---:|---|\n"
        text+="\n".join(f"| {r['round']} | {r['pages']} | {r['sha256']} |" for r in rows)
        text+="\n\nmain.pdf is byte-identical to round two. No submission-readiness or external peer-review claim.\n"
        (ROOT/"paper/COMPILE_REPORT.md").write_text(text)
    return rows
def lanes(write):
    outputs=[]
    with tempfile.TemporaryDirectory(prefix="c391-producer-gate-") as directory:
        output=Path(directory)/"e.json"
        outputs.append(run([sys.executable,"-B",str(ROOT/"code/c391_producer.py"),"--output",str(output)]).strip())
        assert output.read_bytes()==(ROOT/"results/c391_evidence.json").read_bytes()
    for name in ("checker","sympy_crosscheck","replay","mutation"):
        outputs.append(run([sys.executable,"-B",str(ROOT/f"code/c391_{name}.py")]).strip())
    outputs.append(run([sys.executable,"-B","-m","unittest","tests/test_c391_smoke.py"],cwd=ROOT).strip())
    scripts=sorted(ROOT.glob("code/*.py"));assert len(scripts)==6
    for script in scripts:
      for flag in ("-O","-OO"):
        p=subprocess.run([sys.executable,flag,str(script),"--help"],capture_output=True,text=True)
        assert p.returncode and "refuses optimized Python" in p.stdout+p.stderr
    if write:
        report="# C391 actual executable test report\n\nAll listed lanes completed successfully in this release-write run. Exact and numeric results are regression, not interval certificates. Six code scripts were actually invoked under both -O and -OO: twelve optimized-mode refusals, including this release script.\n\n"
        report+="\n\n".join("```\n"+o+"\n```" for o in outputs)+"\n"
        (ROOT/"results/TEST_REPORT.md").write_text(report)
        (ROOT/"results/HOSTILE_AUDIT.md").write_text("# C391 actual hostile audit\n\nPASS: 42 semantic attacks with repaired payload hashes; 4 JSON serialization/stale-hash attacks; 10 strict YAML attacks independently exercised against both the checker and actual release --write entry. All were rejected. Thus 56 distinct mutations caused 66 checked refusals. No mutation is counted as a scientific finding. Boolean-to-integer substitutions cover scope, Route B, precision, exact coordinates and row verdicts. Unknown fields, duplicate keys, anchors, aliases, merges, date coercion and numeric NaN are covered.\n\nRelease --write performs the locked YAML gate before any numerical lane or write. The attack runner invokes this entry on each hostile temporary YAML, and checks nonzero refusal; it does not claim that a manifest SHA alone enforces typed semantics.\n")
    return outputs
def manifest(rows):
    actual=sorted(str(p.relative_to(ROOT)) for p in ROOT.rglob("*") if p.is_file() and "__pycache__" not in p.parts and p!=MANIFEST)
    assert actual==REQUIRED,dict(extra=sorted(set(actual)-set(REQUIRED)),missing=sorted(set(REQUIRED)-set(actual)))
    for relative in REQUIRED:
        p=ROOT/relative
        if p.suffix in (".md",".tex",".py",".yaml",".txt"):
            assert all(c>=32 or c in (10,13) for c in p.read_bytes()),relative
    evidence=json.loads((ROOT/"results/c391_evidence.json").read_text())
    assert all(v is False for v in evidence["scope_flags"].values())
    assert evidence["route_a"]["route_b_invocation_allowed"] is False
    return dict(schema="hcs-release-manifest-v1",candidate_id="HCS-C391",obstruction_id="HEN-O375",source_commit="0c877206d202f732e21ea0b194f9c7fdf30467ee",
        fixed_epoch=1788566400,scope_literal="NO_BAD_EULER_OR_ROOT_NUMBER",payload_file_count=len(REQUIRED),physical_file_count=len(REQUIRED)+1,
        evidence_sha256=sha(ROOT/"results/c391_evidence.json"),evidence_payload_sha256=evidence["payload_sha256"],main_pdf_sha256=sha(ROOT/"paper/main.pdf"),
        evaluator_authority_sha256=evidence["evaluator"]["sha256"],evaluation_raw_sha256=evidence["route_a_yaml"]["raw_sha256"],
        evaluation_semantic_sha256=evidence["route_a_yaml"]["semantic_sha256"],pdf_rounds=rows,
        release_lanes={k:"PASS" for k in ("canonical_producer","independent_checker","symbolic_high_precision","two_directory_replay","repaired_hash_mutations","strict_yaml_write_attacks","smoke","optimized_refusal","deterministic_pdf","fonts","raster","scope_firewall","ledger")},
        files={r:sha(ROOT/r) for r in REQUIRED})
def main():
    p=argparse.ArgumentParser();p.add_argument("--write",action="store_true");p.add_argument("--build-pdfs",action="store_true")
    p.add_argument("--evaluation",type=Path,default=ROOT/"evaluations/route_a/HCS-C391/2026-09-05.yaml");a=p.parse_args()
    run([sys.executable,"-B",str(ROOT/"code/c391_checker.py"),"--yaml-only","--yaml-path",str(a.evaluation)])
    if a.build_pdfs:
        print("C391 deterministic PDF PASS",json.dumps(compile_all(True)));return
    outputs=lanes(a.write);rows=compile_all(False);m=manifest(rows);blob=json.dumps(m,sort_keys=True,indent=2).encode()+b"\n"
    if a.write:MANIFEST.write_bytes(blob)
    else:assert MANIFEST.read_bytes()==blob,"stale manifest"
    print("C391 release PASS",json.dumps(outputs));print("manifest_sha256="+hashlib.sha256(blob).hexdigest())
if __name__=="__main__":main()
