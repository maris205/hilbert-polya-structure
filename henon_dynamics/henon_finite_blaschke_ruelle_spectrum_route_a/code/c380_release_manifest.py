#!/usr/bin/env python3
"""C380 strict deterministic release; default is read-only."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("c380 release refuses optimized Python")
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
import yaml
ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/"C380_RELEASE_MANIFEST.json"
YAML_PATH=ROOT/"evaluations/route_a/HCS-C380/2026-09-05.yaml"
YAML_SHA="27dbf688846b7f4ee5202d5f8a7cca7ebce1196f4c58e840ddb40e8026fddac8"
SOURCE="0596f9d680277288225062a6fdd7ad7ce116e01d"
EVALUATOR="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH=1788566400
EXPECTED={"README.md",
"PROJECT_README.md",
"RESEARCH_QUESTION.md",
"ASSUMPTIONS.md",
"SCOPE.md",
"LIMITATIONS.md",
"THEOREM_PACKAGE.md",
"CLAIMS.md",
"NARRATIVE_REPORT.md",
"EXPERIMENT_PLAN.md",
"PAPER_PLAN.md",
"PAPER_IMPROVEMENT_LOG.md",
"REFERENCES.md",
"SOURCE_AUDIT.md",
"REPRODUCIBILITY.md",
"code/README.md",
"review/ROUND0_REVIEW.md",
"review/ROUND1_REVIEW.md",
"review/ROUND2_REVIEW.md",
"review/CLAIM_REFERENCE_AUDIT.md",
"review/FAILURE_MODE_AUDIT.md",
"review/FINAL_INTEGRITY.md",
"requirements.txt",
"proof/ANALYTIC_PROOF.md",
"results/c380_blaschke_evidence.json",
"tests/test_c380_smoke.py",
"evaluations/route_a/HCS-C380/2026-09-05.yaml",
"code/c380_blaschke_producer.py",
"code/c380_blaschke_checker.py",
"code/c380_blaschke_sympy_crosscheck.py",
"code/c380_blaschke_replay.py",
"code/c380_blaschke_mutation.py",
"code/c380_release_manifest.py",
"paper/main.tex",
"paper/main.pdf",
"results/RESULTS.md",
"results/TEST_REPORT.md",
"results/HOSTILE_AUDIT.md",
"paper/COMPILE_REPORT.md",
"paper/README.md",
"RELEASE.md",
"paper/main_round0.tex",
"paper/main_round0.pdf",
"paper/round0_settled_log.txt",
"paper/main_round1.tex",
"paper/main_round1.pdf",
"paper/round1_settled_log.txt",
"paper/main_round2.tex",
"paper/main_round2.pdf",
"paper/round2_settled_log.txt"}
TUPLE=["A0_FAIL","A1_WEAK","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"]
WARNING=re.compile(r"^(?:LaTeX|Package [^:\n]+) Warning:|Overfull|Underfull|badness|undefined references|Missing character|missing glyph",re.M)
ENV=dict(os.environ,PYTHONDONTWRITEBYTECODE="1",SOURCE_DATE_EPOCH=str(EPOCH),FORCE_SOURCE_DATE="1",TZ="UTC")
def canonical(x):
    return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
def strict_json(path):
    def unique(pairs):
        ans={}
        for k,v in pairs:
            if k in ans: raise ValueError("duplicate JSON key")
            ans[k]=v
        return ans
    return json.loads(path.read_text(),object_pairs_hook=unique,parse_constant=lambda s:(_ for _ in ()).throw(ValueError(s)))
class Loader(yaml.SafeLoader):
    pass
def mapping(loader,node,deep=False):
    ans={}
    for k,v in node.value:
        if k.tag=="tag:yaml.org,2002:merge":raise ValueError("YAML merge")
        key=loader.construct_object(k,deep=deep)
        if type(key) is not str or key in ans:raise ValueError("YAML key")
        ans[key]=loader.construct_object(v,deep=deep)
    return ans
Loader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,mapping)
def evaluation(path):
    raw=path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token,(yaml.tokens.AnchorToken,yaml.tokens.AliasToken)):raise ValueError("YAML aliases")
    value=yaml.load(raw,Loader=Loader)
    def scalar_types(x):
        if isinstance(x,dict):
            for v in x.values():scalar_types(v)
        elif isinstance(x,list):
            for v in x:scalar_types(v)
        elif type(x) not in (str,int,bool,type(None)):raise ValueError("YAML implicit date/float/type")
    scalar_types(value)
    if sha(path)!=YAML_SHA:raise ValueError("frozen YAML raw/schema/type drift")
    if value["tuple"]!=TUPLE or value["overall_verdict"]!="ROUTE_A_REJECTED":raise ValueError("route drift")
    if value["source_commit"]!=SOURCE or value["code_commit"]!=SOURCE:raise ValueError("source drift")
    if value["evaluator_authority_sha256"]!=EVALUATOR:raise ValueError("evaluator drift")
    if any(type(v) is not bool or v for v in value["scope_flags"].values()):raise ValueError("scope flags")
    if type(value["route_b_invocation_allowed"]) is not bool or value["route_b_invocation_allowed"]:raise ValueError("route B")
    authority=ROOT.parents[1]/"flow_systems/skills/route-a-evaluator.md"
    if sha(authority)!=EVALUATOR:raise ValueError("authority content drift")
    return value
def yaml_attacks():
    raw=YAML_PATH.read_text()
    variants=[raw+"\nunexpected: true\n",raw+"\ncandidate_id: HCS-C999\n",
        raw.replace("route_b_invocation_allowed: false","route_b_invocation_allowed: 0"),
        raw.replace("evaluation_date: '2026-09-05'","evaluation_date: 2026-09-05"),
        raw.replace("title: Nonlinear","title: &alias Nonlinear"),raw+"\nalias: *missing\n",
        raw+"\n<<: {injected: true}\n",raw+"\n1: scalar-key\n",raw.replace("A1_WEAK","A1_PASS"),
        raw.replace("fixed_epoch: 1788566400","fixed_epoch: 1788566400.0")]
    with tempfile.TemporaryDirectory(prefix="c380-yaml-") as d:
        path=Path(d)/"attack.yaml"
        for i,text in enumerate(variants):
            path.write_text(text)
            try:evaluation(path)
            except (ValueError,TypeError,yaml.YAMLError):pass
            else:raise AssertionError(f"YAML attack accepted {i}")
    return len(variants)
def command(args,cwd=ROOT):
    p=subprocess.run(args,cwd=cwd,env=ENV,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    if p.returncode:raise RuntimeError(p.stdout)
    return p.stdout.strip()
def numerical():
    result={}
    for lane in ("checker","sympy_crosscheck","replay","mutation"):
        result[lane]=command([sys.executable,"-B",str(ROOT/f"code/c380_blaschke_{lane}.py")])
        print(result[lane],flush=True)
    with tempfile.TemporaryDirectory(prefix="c380-producer-") as d:
        path=Path(d)/"evidence.json"
        result["producer"]=command([sys.executable,"-B",str(ROOT/"code/c380_blaschke_producer.py"),"--output",str(path)])
        if path.read_bytes()!=(ROOT/"results/c380_blaschke_evidence.json").read_bytes():raise AssertionError("producer drift")
    out=command([sys.executable,"-B","-m","unittest","discover","-s","tests"])
    if "Ran 3 tests" not in out or "OK" not in out:raise AssertionError(out)
    result["smoke"]="3/3 PASS"
    for name in ("producer","checker","sympy_crosscheck","replay","mutation","release_manifest"):
        file=ROOT/("code/c380_release_manifest.py" if name=="release_manifest" else f"code/c380_blaschke_{name}.py")
        for opt in ("-O","-OO"):
            p=subprocess.run([sys.executable,opt,"-B",str(file)],cwd=ROOT,env=ENV,capture_output=True,text=True)
            if p.returncode==0 or "refuses optimized Python" not in p.stdout+p.stderr:raise AssertionError(f"optimized execution {file}")
    result["optimized_refusals"]="12/12 PASS"
    result["yaml_hostile"]=f"{yaml_attacks()}/10 PASS"
    return result
def build_pdf(n):
    with tempfile.TemporaryDirectory(prefix=f"c380-pdf-{n}-") as d:
        work=Path(d)
        for name in ("main.tex",f"main_round{n}.tex"):shutil.copy2(ROOT/"paper"/name,work/name)
        for _ in range(2):command(["lualatex","-interaction=nonstopmode","-halt-on-error","-jobname=artifact",f"main_round{n}.tex"],cwd=work)
        log=(work/"artifact.log").read_text()
        found=WARNING.search(log)
        if found:
            p=found.start()
            raise AssertionError(f"round {n} warning: "+log[max(0,p-100):p+450])
        return (work/"artifact.pdf").read_bytes(),log.replace(str(work),"<BUILD_DIR>")
def put(path,data,write):
    blob=data.encode() if isinstance(data,str) else data
    if write:path.write_bytes(blob)
    elif path.read_bytes()!=blob:raise AssertionError(f"artifact drift: {path.relative_to(ROOT)}")
def pdfs(write):
    rows=[]
    for n in range(3):
        first,log=build_pdf(n);second,_=build_pdf(n)
        if first!=second:raise AssertionError(f"nondeterministic PDF {n}")
        path=ROOT/f"paper/main_round{n}.pdf";put(path,first,write)
        if write:(ROOT/f"paper/round{n}_settled_log.txt").write_text(log)
        elif WARNING.search((ROOT/f"paper/round{n}_settled_log.txt").read_text()):raise AssertionError("stored log warning")
        pages=int(re.search(r"^Pages:\s+(\d+)",command(["pdfinfo",str(path)]),re.M).group(1))
        fonts=command(["pdffonts",str(path)]).splitlines()[2:]
        if not fonts or not any("DroidSansFallback" in line for line in fonts):raise AssertionError("CJK font missing")
        for line in fonts:
            if line.split()[-5:-3]!=["yes","yes"]:raise AssertionError(f"font not embedded/subset {line}")
        raw=command(["pdftotext","-layout",str(path),"-"])
        if re.search(r"[\x00-\x08\x0b\x0e-\x1f\x7f]",raw):raise AssertionError("PDF control")
        text=" ".join(re.sub(r"(?<=[A-Za-z])-\s*\n\s*(?=[A-Za-z])","",raw).lower().split());compact=text.replace(" ","")
        for token in ("??","[verify]","todo","fixme"):
            if token in text:raise AssertionError("PDF placeholder")
        for token in ("abstract","keywords:"):
            if token not in text:raise AssertionError("English abstract missing")
        for token in ("中文摘要","关键词："):
            if token not in compact:raise AssertionError("Chinese abstract missing")
        english=("blaschke products","periodic orbits","stability multipliers","transfer operators","fredholm determinants","singular limits")
        chinese=("布拉施克乘积","周期轨道","稳定性乘子","转移算子","弗雷德霍姆行列式","奇异极限")
        for token in english:
            if token.replace(" ","") not in compact:raise AssertionError("English keyword missing")
        for token in chinese:
            if token not in compact:raise AssertionError("Chinese keyword missing")
        markers=("round-zero certificate","round-one certificate","round-two certificate")
        if markers[n] not in text:raise AssertionError("round increment missing")
        for later in markers[n+1:]:
            if later in text:raise AssertionError("later round leak")
        with tempfile.TemporaryDirectory(prefix="c380-raster-") as d:
            command(["pdftoppm","-r","45","-png",str(path),str(Path(d)/"page")])
            images=list(Path(d).glob("page-*.png"))
            if len(images)!=pages or any(p.stat().st_size<1000 for p in images):raise AssertionError("raster")
        rows.append({"round":n,"path":str(path.relative_to(ROOT)),"sha256":sha(path),"pages":pages,"font_rows":len(fonts)})
        print(f"C380 PDF round {n}: {pages} pages, deterministic, fonts/text/raster PASS",flush=True)
    if len({r["sha256"] for r in rows})!=3:raise AssertionError("duplicate round PDF")
    put(ROOT/"paper/main.pdf",(ROOT/"paper/main_round2.pdf").read_bytes(),write)
    return rows
def reports(outputs,rows):
    return {
      "results/RESULTS.md":"# Results\n\nComplete native orbit/trace/determinant theorem; no target identification. Exact parameters: 5; census orders: 24; trace orders: 16; direct orbit points: 171.\n\nEvidence file SHA-256: "+sha(ROOT/"results/c380_blaschke_evidence.json")+"\n",
      "results/TEST_REPORT.md":"# Executed test receipts\n\n"+"\n".join(f"- {k}: {v}" for k,v in outputs.items())+"\n\nFinite computations audit the analytic theorem and do not replace it.\n",
      "results/HOSTILE_AUDIT.md":"# Hostile audit\n\n32/32 JSON attacks rejected (semantic cases repair the hash; duplicate/nonfinite parser attacks are raw). Ten YAML schema/type/source attacks rejected. All six executable lanes refuse -O and -OO. The checker imports no producer.\n",
      "paper/COMPILE_REPORT.md":"# Compile report\n\nEach round: two fresh builds, two LuaLaTeX passes each; fixed epoch 1788566400. Byte equality, warning-free settled logs, embedded/subset fonts, bilingual extracted text, layered theorem markers, and every-page rasterization passed. Retained settled logs are receipts, not claimed byte-reproducible logs.\n\n"+"\n".join(f"- Round {r['round']}: {r['pages']} pages; SHA-256 {r['sha256']}." for r in rows)+"\n\nmain.pdf equals round 2 byte for byte. Automated rasterization is distinct from visual inspection.\n",
      "paper/README.md":"# Paper artifacts\n\nmain.tex is the conditional source with default round 2. Wrappers main_round0/1/2.tex select distinct theorem layers. main.pdf equals main_round2.pdf. Each revision has English and Chinese abstracts and six language-matched keywords. Snapshots are revisions of one paper.\n",
      "RELEASE.md":"# Release\n\nRun python -B code/c380_release_manifest.py --write to build and python -B code/c380_release_manifest.py to verify without mutation. The exact ledger excludes only C380_RELEASE_MANIFEST.json. No commit or push is performed by this script.\n"}
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true")
    ap.add_argument("--evaluation",type=Path);ap.add_argument("--pdf-only",action="store_true");args=ap.parse_args()
    route=evaluation(args.evaluation or YAML_PATH)
    if args.evaluation:print("C380 evaluation PASS");return
    if args.pdf_only:pdfs(args.write);return
    checker=(ROOT/"code/c380_blaschke_checker.py").read_text()
    if re.search(r"(?:from|import)\s+[^\n]*c380_blaschke_producer",checker):raise AssertionError("checker independence")
    outputs=numerical();rows=pdfs(args.write)
    for name,body in reports(outputs,rows).items():put(ROOT/name,body,args.write)
    files={str(p.relative_to(ROOT)):p for p in ROOT.rglob("*") if p.is_file() and p!=MANIFEST}
    if set(files)!=EXPECTED:raise AssertionError(f"file set missing={EXPECTED-set(files)} extra={set(files)-EXPECTED}")
    obj={"schema":"hcs-release-manifest-v1","candidate_id":"HCS-C380","obstruction_id":"HEN-O364",
         "source_commit":SOURCE,"fixed_epoch":EPOCH,"scope_literal":"NO_BAD_EULER_OR_ROOT_NUMBER",
         "evaluator_authority_sha256":EVALUATOR,"route_a_tuple":TUPLE,"route_b_invocation_allowed":False,
         "scope_flags":route["scope_flags"],"evidence_sha256":sha(ROOT/"results/c380_blaschke_evidence.json"),
         "pdfs":rows,"payload_file_count":len(files),"physical_file_count":len(files)+1,
         "files":{name:{"sha256":sha(p),"bytes":p.stat().st_size} for name,p in sorted(files.items())}}
    obj["payload_sha256"]=hashlib.sha256(canonical(obj)).hexdigest()
    blob=json.dumps(obj,sort_keys=True,indent=2,ensure_ascii=False)+"\n"
    if not args.write:strict_json(MANIFEST)
    put(MANIFEST,blob,args.write)
    print(f"C380 release PASS: {len(files)} payload files, {len(files)+1} physical files; manifest={sha(MANIFEST)}")
if __name__=="__main__":main()
