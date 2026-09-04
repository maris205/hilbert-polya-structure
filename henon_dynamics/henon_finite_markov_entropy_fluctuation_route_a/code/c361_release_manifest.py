#!/usr/bin/env python3
"""Deterministic 27-payload release gate for HCS-C361."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("c361 release refuses optimized Python")
import argparse, hashlib, json, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/"C361_RELEASE_MANIFEST.json"
EVID=ROOT/"results/c361_markov_entropy_evidence.json"
TEX=ROOT/"paper/main.tex"
MAIN_PDF=ROOT/"paper/main.pdf"
EVALUATION=ROOT/"evaluations/route_a/HCS-C361/2026-09-04.yaml"
EVALUATION_RAW_SHA256="e61d1cc50b0891d2ecefb02bd460bf8b2bde48bf8f78fa6fb0e7524c6c931c7b"
EVALUATION_SEMANTIC_SHA256="f8b6e53916659fb22cdc2b4278c5ef43ce5a24ea09ece76e86ada0dd3ff3c09b"
EVALUATOR_AUTHORITY="flow_systems/skills/route-a-evaluator.md"
EVALUATOR_VERSION="0.2.0"
EVALUATOR_AUTHORITY_SHA256="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
PDF_NAMES=("main_round0_original.pdf","main_round1.pdf","main_round2.pdf")
EXPECTED=(
 "EXPERIMENT_PLAN.md","NARRATIVE_REPORT.md","PAPER_IMPROVEMENT_LOG.md","PAPER_PLAN.md","README.md","RESEARCH_QUESTION.md","SOURCE_AUDIT.md","THEOREM_PACKAGE.md",
 "code/README.md","code/c361_markov_entropy_checker.py","code/c361_markov_entropy_mutation.py","code/c361_markov_entropy_producer.py",
 "code/c361_markov_entropy_replay.py","code/c361_markov_entropy_sympy_crosscheck.py","code/c361_release_manifest.py",
 "evaluations/route_a/HCS-C361/2026-09-04.yaml","paper/COMPILE_REPORT.md","paper/README.md","paper/main.pdf","paper/main.tex",
 "paper/main_round0_original.pdf","paper/main_round1.pdf","paper/main_round2.pdf","results/HOSTILE_AUDIT.md","results/RESULTS.md","results/TEST_REPORT.md","results/c361_markov_entropy_evidence.json")
SCRIPTS=("c361_markov_entropy_producer.py","c361_markov_entropy_checker.py","c361_markov_entropy_sympy_crosscheck.py",
 "c361_markov_entropy_replay.py","c361_markov_entropy_mutation.py","c361_release_manifest.py")
WARN=re.compile(r"(?:LaTeX|Package [^:\n]+) Warning:|warning  \(pdf backend\)|"
                r"Overfull|Underfull|undefined (?:references|citations)|Rerun to get|Missing character")

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def run(cmd,**kw):
    p=subprocess.run(cmd,capture_output=True,text=True,**kw)
    if p.returncode:
        raise AssertionError(f"command failed {cmd}:\n{p.stdout}\n{p.stderr}")
    return p.stdout.strip()
def actual_files():return sorted(str(p.relative_to(ROOT)) for p in ROOT.rglob("*") if p.is_file())

def strict_json(path):
    def unique(pairs):
        answer={}
        for key,value in pairs:
            if key in answer: raise ValueError("duplicate JSON key")
            answer[key]=value
        return answer
    return json.loads(path.read_text(),object_pairs_hook=unique,
                      parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)))

def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()

def evidence_payload_hash():
    body=strict_json(EVID);claimed=body.pop("payload_sha256")
    computed=hashlib.sha256(canonical(body)).hexdigest()
    assert claimed==computed,"stale evidence payload hash"
    return claimed

def compile_round(round_number):
    blobs=[]; settled=""
    for _ in range(2):
        with tempfile.TemporaryDirectory(prefix=f"c361-tex-r{round_number}-") as td:
            work=Path(td);shutil.copy2(TEX,work/"main.tex")
            env=dict(os.environ, SOURCE_DATE_EPOCH="1788480000", FORCE_SOURCE_DATE="1")
            source=rf"\def\CRevisionRound{{{round_number}}}\input{{main.tex}}"
            cmd=["lualatex","-interaction=nonstopmode","-halt-on-error","-jobname=main",source]
            run(cmd,cwd=work,env=env);run(cmd,cwd=work,env=env)
            settled=(work/"main.log").read_text(errors="replace")
            assert not WARN.search(settled),"settled LaTeX warning"
            blobs.append((work/"main.pdf").read_bytes())
    assert blobs[0]==blobs[1],f"round {round_number} fresh builds differ"
    return blobs[0]

def pdf_gate(path,round_number):
    info=run(["pdfinfo",str(path)]);m=re.search(r"^Pages:\s+(\d+)",info,re.M);assert m
    fonts=run(["pdffonts",str(path)]).splitlines()[2:];assert fonts
    for line in fonts:
        cols=line.split();assert len(cols)>=7 and cols[-5]=="yes" and cols[-4]=="yes",f"font not embedded/subset: {line}"
    with tempfile.TemporaryDirectory(prefix="c361-text-") as td:
        txt=Path(td)/"paper.txt";run(["pdftotext",str(path),str(txt)])
        raw=txt.read_bytes();assert all(b>=32 or b in (9,10,12,13) for b in raw),"control character"
        text=raw.decode("utf-8");assert "Finite Markov Networks" in text
        if round_number==2:assert "NO_BAD_EULER_OR_ROOT_NUMBER" in text
        assert "qquad" not in text and "??" not in text
        prefix=Path(td)/"page";run(["pdftoppm","-png","-r","72",str(path),str(prefix)])
        images=sorted(Path(td).glob("page-*.png"))
        assert len(images)==int(m.group(1))
        raster_bytes=[item.stat().st_size for item in images]
        assert all(size>=1000 for size in raster_bytes),"implausibly small PDF raster"
    return int(m.group(1)),len(fonts),raster_bytes

def optimized_gate():
    for name in SCRIPTS:
        script=ROOT/"code"/name
        for flag in ("-O","-OO"):
            p=subprocess.run([sys.executable,flag,str(script),"--help"],capture_output=True,text=True)
            assert p.returncode!=0 and "refuses optimized Python" in p.stderr+p.stdout,(name,flag)

def lane_gate():
    py=sys.executable
    outputs=[]
    with tempfile.TemporaryDirectory(prefix="c361-release-evidence-") as td:
        out=Path(td)/"evidence.json"
        outputs.append(run([py,str(ROOT/"code/c361_markov_entropy_producer.py"),"--output",str(out)]))
        assert out.read_bytes()==EVID.read_bytes(),"canonical evidence stale"
    outputs.append(run([py,str(ROOT/"code/c361_markov_entropy_checker.py")]))
    outputs.append(run([py,str(ROOT/"code/c361_markov_entropy_sympy_crosscheck.py")]))
    outputs.append(run([py,str(ROOT/"code/c361_markov_entropy_replay.py")]))
    outputs.append(run([py,str(ROOT/"code/c361_markov_entropy_mutation.py")]))
    return outputs

def build_manifest(pdf_rounds):
    entries={}
    for rel in EXPECTED:
        p=ROOT/rel;assert p.is_file(),rel
        entries[rel]=sha(p)
    assert sha(EVALUATION)==EVALUATION_RAW_SHA256,"evaluation raw-byte digest"
    evidence=strict_json(EVID)
    assert evidence["route_a_yaml"]=={
        "relative_path":"evaluations/route_a/HCS-C361/2026-09-04.yaml",
        "raw_sha256":EVALUATION_RAW_SHA256,
        "semantic_sha256":EVALUATION_SEMANTIC_SHA256,
    },"evaluation semantic lock"
    assert evidence["evaluator"]=={
        "authority":EVALUATOR_AUTHORITY,"version":EVALUATOR_VERSION,
        "sha256":EVALUATOR_AUTHORITY_SHA256,
    },"evaluator authority lock"
    return {"schema":"hcs-release-manifest-v1","candidate_id":"HCS-C361","obstruction_id":"HEN-O345",
      "source_commit":"05ca5f96b2c69a6ad6ba153d1084df750d7722c0","fixed_epoch":1788480000,
      "scope_literal":"NO_BAD_EULER_OR_ROOT_NUMBER","evaluator_authority":EVALUATOR_AUTHORITY,
      "evaluator_version":EVALUATOR_VERSION,"evaluator_authority_sha256":EVALUATOR_AUTHORITY_SHA256,
      "payload_file_count":len(entries),"physical_file_count":len(entries)+1,
      "evaluation_raw_sha256":EVALUATION_RAW_SHA256,"evaluation_semantic_sha256":EVALUATION_SEMANTIC_SHA256,
      "evidence_sha256":sha(EVID),"evidence_payload_sha256":evidence_payload_hash(),
      "main_pdf_sha256":sha(MAIN_PDF),
      "release_lanes":{"producer":"PASS","independent_checker":"PASS","sympy_crosscheck":"PASS",
                       "isolated_byte_replay":"PASS","hostile_mutation":"PASS",
                       "optimized_mode_refusal":"PASS","deterministic_pdf_rebuild":"PASS",
                       "payload_membership":"PASS"},
      "pdf_rounds":pdf_rounds,"files":{key:entries[key] for key in sorted(entries)}}

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");a=ap.parse_args()
    current=actual_files();allowed=sorted(EXPECTED+(MANIFEST.name,))
    permitted=sorted(EXPECTED) if a.write and not MANIFEST.exists() else allowed
    assert current==permitted,f"file ledger mismatch\nextra={sorted(set(current)-set(permitted))}\nmissing={sorted(set(permitted)-set(current))}"
    outputs=lane_gate();optimized_gate();pdf_rounds=[];round_blobs=[]
    for r,name in enumerate(PDF_NAMES):
        blob=compile_round(r);stored=ROOT/"paper"/name;assert blob==stored.read_bytes(),f"stale {name}"
        pages,fonts,raster_bytes=pdf_gate(stored,r);round_blobs.append(blob)
        pdf_rounds.append({"round":r,"path":f"paper/{name}","sha256":sha(stored),
                           "bytes":stored.stat().st_size,"pages":pages,"font_rows":fonts,
                           "raster_bytes":raster_bytes})
    assert len(set(round_blobs))==3,"revision PDFs not distinct"
    assert MAIN_PDF.read_bytes()==round_blobs[2],"main is not round2"
    pdf_gate(MAIN_PDF,2)
    report=(ROOT/"paper/COMPILE_REPORT.md").read_text()
    for item in pdf_rounds: assert item["sha256"] in report
    assert sha(EVID) in (ROOT/"results/RESULTS.md").read_text()
    manifest=build_manifest(pdf_rounds);blob=json.dumps(manifest,sort_keys=True,indent=2).encode()+b"\n"
    if a.write: MANIFEST.write_bytes(blob)
    else: assert MANIFEST.read_bytes()==blob,"manifest stale"
    print("C361 release PASS: payload=27 physical=28 " + " | ".join(outputs))
    print(f"manifest_sha256={hashlib.sha256(blob).hexdigest()} pdf_sha256={sha(ROOT/'paper/main.pdf')} evidence_sha256={sha(EVID)}")

if __name__=="__main__":
    try:main()
    except Exception as exc:
        print(f"C361 release FAIL: {type(exc).__name__}: {exc}",file=sys.stderr);sys.exit(1)
