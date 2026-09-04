#!/usr/bin/env python3
"""Deterministic 27-payload release gate for HCS-C365."""
from __future__ import annotations
if not __debug__: raise RuntimeError("c365 release refuses optimized Python")
import argparse, hashlib, json, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];MANIFEST=ROOT/"C365_RELEASE_MANIFEST.json"
EVID=ROOT/"results/c365_gelfand_tsetlin_evidence.json";TEX=ROOT/"paper/main.tex";MAIN=ROOT/"paper/main.pdf"
EVAL=ROOT/"evaluations/route_a/HCS-C365/2026-09-04.yaml"
YAML_RAW="9e0d4a9a3861749a2d48b0b30548da79e4f4ff721ba5deee0171a6497dfc7cbc";YAML_SEM="db67bc21cbbeb3ae27fa09766ff3de547b54740137026bd9322e29a5a396a99d"
AUTH="flow_systems/skills/route-a-evaluator.md";VERSION="0.2.0";AUTH_SHA="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
PDF_NAMES=("main_round0_original.pdf","main_round1.pdf","main_round2.pdf")
EXPECTED=(
 "EXPERIMENT_PLAN.md","NARRATIVE_REPORT.md","PAPER_IMPROVEMENT_LOG.md","PAPER_PLAN.md","README.md","RESEARCH_QUESTION.md","SOURCE_AUDIT.md","THEOREM_PACKAGE.md",
 "code/README.md","code/c365_gelfand_tsetlin_checker.py","code/c365_gelfand_tsetlin_mutation.py","code/c365_gelfand_tsetlin_producer.py",
 "code/c365_gelfand_tsetlin_replay.py","code/c365_gelfand_tsetlin_sympy_crosscheck.py","code/c365_release_manifest.py",
 "evaluations/route_a/HCS-C365/2026-09-04.yaml","paper/COMPILE_REPORT.md","paper/README.md","paper/main.pdf","paper/main.tex",
 "paper/main_round0_original.pdf","paper/main_round1.pdf","paper/main_round2.pdf","results/HOSTILE_AUDIT.md","results/RESULTS.md","results/TEST_REPORT.md",
 "results/c365_gelfand_tsetlin_evidence.json")
SCRIPTS=("c365_gelfand_tsetlin_producer.py","c365_gelfand_tsetlin_checker.py","c365_gelfand_tsetlin_sympy_crosscheck.py",
 "c365_gelfand_tsetlin_replay.py","c365_gelfand_tsetlin_mutation.py","c365_release_manifest.py")
WARN=re.compile(r"(?:LaTeX|Package [^:\n]+) Warning:|warning  \(pdf backend\)|Overfull|Underfull|undefined (?:references|citations)|Rerun to get|Missing character")
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def run(cmd,**kw):
    p=subprocess.run(cmd,capture_output=True,text=True,**kw)
    if p.returncode: raise AssertionError(f"command failed {cmd}:\n{p.stdout}\n{p.stderr}")
    return p.stdout.strip()
def actual(): return sorted(str(p.relative_to(ROOT)) for p in ROOT.rglob("*") if p.is_file())
def unique(pairs):
    out={}
    for k,v in pairs:
        if k in out: raise ValueError("duplicate JSON key")
        out[k]=v
    return out
def strict_json(p): return json.loads(p.read_text(),object_pairs_hook=unique,parse_constant=lambda x:(_ for _ in()).throw(ValueError(x)))
def canon(x): return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
def payload_hash():
    obj=strict_json(EVID);claim=obj.pop("payload_sha256");assert claim==hashlib.sha256(canon(obj)).hexdigest();return claim
def compile_round(r):
    blobs=[];logs=[]
    for _ in range(2):
        with tempfile.TemporaryDirectory(prefix=f"c365-tex-r{r}-") as td:
            w=Path(td);shutil.copy2(TEX,w/"main.tex");env=dict(os.environ,SOURCE_DATE_EPOCH="1788480000",FORCE_SOURCE_DATE="1")
            source=rf"\def\CRevisionRound{{{r}}}\input{{main.tex}}";cmd=["lualatex","-interaction=nonstopmode","-halt-on-error","-jobname=main",source]
            run(cmd,cwd=w,env=env);run(cmd,cwd=w,env=env);log=(w/"main.log").read_text(errors="replace")
            assert not WARN.search(log),f"round {r} settled LaTeX warning";blobs.append((w/"main.pdf").read_bytes());logs.append(log)
    assert blobs[0]==blobs[1],f"round {r} fresh builds differ";return blobs[0]
def pdf_gate(path,r):
    info=run(["pdfinfo",str(path)]);m=re.search(r"^Pages:\s+(\d+)",info,re.M);assert m;pages=int(m.group(1))
    fonts=run(["pdffonts",str(path)]).splitlines()[2:];assert fonts
    for line in fonts:
        c=line.split();assert len(c)>=7 and c[-5]=="yes" and c[-4]=="yes",f"font not embedded/subset: {line}"
    with tempfile.TemporaryDirectory(prefix="c365-pdf-") as td:
        textp=Path(td)/"text.txt";run(["pdftotext",str(path),str(textp)]);raw=textp.read_bytes()
        assert all(b>=32 or b in (9,10,12,13) for b in raw),"PDF text control character";text=raw.decode("utf-8")
        assert "Gelfand–Tsetlin System" in text and "qquad" not in text and "??" not in text and "TODO" not in text
        tokens=("round zero interlacing and arrow completion closure","round one thimm torus and closure rank","round two branching quantization and route a closure")
        assert tokens[r] in text
        if r==2: assert "NO_BAD_EULER_OR_ROOT_NUMBER" in text
        prefix=Path(td)/"page";run(["pdftoppm","-png","-r","72",str(path),str(prefix)]);imgs=sorted(Path(td).glob("page-*.png"))
        assert len(imgs)==pages;rasters=[x.stat().st_size for x in imgs];assert all(x>1000 for x in rasters)
    return pages,len(fonts),rasters
def optimized_gate():
    for name in SCRIPTS:
        for flag in ("-O","-OO"):
            p=subprocess.run([sys.executable,flag,str(ROOT/"code"/name),"--help"],capture_output=True,text=True)
            assert p.returncode and "refuses optimized Python" in p.stdout+p.stderr,(name,flag)
def source_gate():
    for p in ROOT.rglob("*"):
        if p.is_file() and p.suffix in (".md",".py",".tex",".yaml"):
            raw=p.read_bytes();assert all(b>=32 or b in (9,10,13) for b in raw),f"control byte in {p}"
    joined="\n".join(p.read_text(errors="replace") for p in ROOT.rglob("*") if p.is_file() and p.suffix in (".md",".py",".tex",".yaml"))
    for token in ("HCS-"+"C364","HEN-"+"O348","c364"+"_","Skoro"+"khod"): assert token not in joined,f"stale token {token}"
def lane_gate():
    out=[];py=sys.executable
    with tempfile.TemporaryDirectory(prefix="c365-release-evidence-") as td:
        p=Path(td)/"e.json";out.append(run([py,str(ROOT/"code/c365_gelfand_tsetlin_producer.py"),"--output",str(p)]));assert p.read_bytes()==EVID.read_bytes()
    out.append(run([py,str(ROOT/"code/c365_gelfand_tsetlin_checker.py")]))
    out.append(run([py,str(ROOT/"code/c365_gelfand_tsetlin_sympy_crosscheck.py")]))
    out.append(run([py,str(ROOT/"code/c365_gelfand_tsetlin_replay.py")]))
    out.append(run([py,str(ROOT/"code/c365_gelfand_tsetlin_mutation.py")]))
    return out
def make_manifest(rounds):
    files={rel:sha(ROOT/rel) for rel in EXPECTED};assert sha(EVAL)==YAML_RAW
    obj=strict_json(EVID);assert obj["route_a_yaml"]=={"relative_path":"evaluations/route_a/HCS-C365/2026-09-04.yaml","raw_sha256":YAML_RAW,"semantic_sha256":YAML_SEM}
    assert obj["evaluator"]=={"authority":AUTH,"version":VERSION,"sha256":AUTH_SHA}
    return {"schema":"hcs-release-manifest-v1","candidate_id":"HCS-C365","obstruction_id":"HEN-O349","source_commit":"323ea43f6970544467f8a89f0ed9be0c7c39f896",
      "fixed_epoch":1788480000,"scope_literal":"NO_BAD_EULER_OR_ROOT_NUMBER","evaluator_authority":AUTH,"evaluator_version":VERSION,
      "evaluator_authority_sha256":AUTH_SHA,"payload_file_count":27,"physical_file_count":28,"evaluation_raw_sha256":YAML_RAW,
      "evaluation_semantic_sha256":YAML_SEM,"evidence_sha256":sha(EVID),"evidence_payload_sha256":payload_hash(),"main_pdf_sha256":sha(MAIN),
      "release_lanes":{"producer":"PASS","independent_checker":"PASS","sympy_crosscheck":"PASS","isolated_byte_replay":"PASS",
        "hostile_mutation":"PASS","optimized_mode_refusal":"PASS","deterministic_pdf_rebuild":"PASS","payload_membership":"PASS"},
      "pdf_rounds":rounds,"files":{k:files[k] for k in sorted(files)}}
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");ap.add_argument("--build-pdfs",action="store_true");a=ap.parse_args()
    if a.build_pdfs:
        blobs=[compile_round(r) for r in range(3)]
        for blob,name in zip(blobs,PDF_NAMES):(ROOT/"paper"/name).write_bytes(blob)
        MAIN.write_bytes(blobs[2]);print("C365 PDF build PASS: three double-fresh rounds; main=round2");return
    cur=actual();allowed=sorted(EXPECTED+(MANIFEST.name,));permitted=sorted(EXPECTED) if a.write and not MANIFEST.exists() else allowed
    assert cur==permitted,f"file ledger mismatch extra={sorted(set(cur)-set(permitted))} missing={sorted(set(permitted)-set(cur))}"
    source_gate();outputs=lane_gate();optimized_gate();rounds=[];blobs=[]
    for r,name in enumerate(PDF_NAMES):
        blob=compile_round(r);p=ROOT/"paper"/name;assert blob==p.read_bytes(),f"stale {name}";pages,fonts,rasters=pdf_gate(p,r);blobs.append(blob)
        rounds.append({"round":r,"path":f"paper/{name}","sha256":sha(p),"bytes":p.stat().st_size,"pages":pages,"font_rows":fonts,"raster_bytes":rasters})
    assert len(set(blobs))==3 and MAIN.read_bytes()==blobs[2];pdf_gate(MAIN,2)
    report=(ROOT/"paper/COMPILE_REPORT.md").read_text()
    for row in rounds: assert row["sha256"] in report
    assert sha(EVID) in (ROOT/"results/RESULTS.md").read_text()
    manifest=make_manifest(rounds);blob=json.dumps(manifest,sort_keys=True,indent=2).encode()+b"\n"
    if a.write: MANIFEST.write_bytes(blob)
    else: assert MANIFEST.read_bytes()==blob,"manifest stale"
    print("C365 release PASS: payload=27 physical=28 "+" | ".join(outputs))
    print(f"manifest_sha256={hashlib.sha256(blob).hexdigest()} pdf_sha256={sha(MAIN)} evidence_sha256={sha(EVID)}")
if __name__=="__main__":
    try: main()
    except Exception as exc:
        print(f"C365 release FAIL: {type(exc).__name__}: {exc}",file=sys.stderr);sys.exit(1)
