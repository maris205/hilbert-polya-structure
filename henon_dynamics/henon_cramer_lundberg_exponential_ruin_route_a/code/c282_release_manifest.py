#!/usr/bin/env python3
"""Close the exact 27-payload / 28-physical-file HCS-C282 release."""
from __future__ import annotations
import hashlib, json, os, re, subprocess, sys, tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/"C282_RELEASE_MANIFEST.json"
EVIDENCE=ROOT/"results/c282_ruin_evidence.json"
PAPER=ROOT/"paper"; PDF=PAPER/"main.pdf"; TEX=PAPER/"main.tex"
YAML=ROOT/"evaluations/route_a/HCS-C282/2026-09-01.yaml"
SOURCE="51fb3d46f96b854314811c1ad62d3103cd5d54e5"
EVAL="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE="NO_BAD_EULER_OR_ROOT_NUMBER"; EPOCH=1788220800
EVIDENCE_SHA="6551879f2a73af5afde9ebf008543fae66e2c4600cb2c90c3461816dfded29f0"
TUPLE=["A0_FAIL","A1_FAIL","A2_FAIL","A3_FAIL","A4_FAIL"]
ROUND_PATHS=[PAPER/"main_round0_original.pdf",PAPER/"main_round1.pdf",PAPER/"main_round2.pdf"]
ROUND_HASHES=[
 "9d839e63ac589b1f4f3188a36bf7738a39bf42a20e56a18827be43d076d25be0",
 "818037a1ffb543d4770aaa15a9a8629575b457e0e00f24a7779389507ac67060",
 "bb934cc9ed23105dac16c3ee7dba1acd37f0826f8da7a0b5c215f97ff9e4218e"]
EXPECTED={
 "EXPERIMENT_PLAN.md","NARRATIVE_REPORT.md","PAPER_IMPROVEMENT_LOG.md","PAPER_PLAN.md","README.md",
 "RESEARCH_QUESTION.md","SOURCE_AUDIT.md","THEOREM_PACKAGE.md","code/README.md",
 "code/c282_ruin_checker.py","code/c282_ruin_mutation.py","code/c282_ruin_producer.py",
 "code/c282_ruin_replay.py","code/c282_ruin_sympy_crosscheck.py","code/c282_release_manifest.py",
 "evaluations/route_a/HCS-C282/2026-09-01.yaml","paper/COMPILE_REPORT.md","paper/README.md",
 "paper/main.pdf","paper/main.tex","paper/main_round0_original.pdf","paper/main_round1.pdf","paper/main_round2.pdf",
 "results/HOSTILE_AUDIT.md","results/RESULTS.md","results/TEST_REPORT.md","results/c282_ruin_evidence.json"}
WARNING_RE=re.compile(r"LaTeX Warning|Package [^:\n]* Warning|Overfull|Underfull|undefined references|Rerun to get|Missing character")

def digest(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ph(d):
    c=dict(d); c.pop("payload_sha256",None)
    return hashlib.sha256(json.dumps(c,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def sidecar(p): return p.suffix in {".aux",".log",".out",".toc",".fls",".fdb_latexmk",".pyc"} or "__pycache__" in p.parts or p.name.endswith(".synctex.gz")
def runpy(name):
    env=dict(os.environ); env["PYTHONDONTWRITEBYTECODE"]="1"
    return subprocess.check_output([sys.executable,"-B",str(ROOT/"code"/name)],env=env,text=True)
def pages(p):
    out=subprocess.check_output(["pdfinfo",str(p)],text=True)
    return int(next(x.split(":",1)[1] for x in out.splitlines() if x.startswith("Pages:")))
def fonts(p):
    out=subprocess.check_output(["pdffonts",str(p)],text=True)
    return [x for x in out.splitlines()[2:] if x.strip() and not x.lstrip().startswith("-")]
def fresh(round_number):
    with tempfile.TemporaryDirectory(prefix=f"c282-r{round_number}-") as td:
        work=Path(td); env=dict(os.environ)
        env.update({"SOURCE_DATE_EPOCH":str(EPOCH),"FORCE_SOURCE_DATE":"1","TZ":"UTC"})
        src=rf"\def\CRevisionRound{{{round_number}}}\input{{{TEX}}}"
        cmd=["lualatex","-interaction=nonstopmode","-halt-on-error","-jobname=main",src]
        for _ in range(2): subprocess.run(cmd,cwd=work,env=env,check=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        log=(work/"main.log").read_text(errors="replace"); assert not WARNING_RE.search(log)
        return (work/"main.pdf").read_bytes()

def main():
    d=json.loads(EVIDENCE.read_text())
    assert digest(EVIDENCE)==EVIDENCE_SHA and d["payload_sha256"]==ph(d)
    assert d["schema"]=="hcs-c282-cramer-lundberg-exponential-ruin-v1" and d["candidate_id"]=="HCS-C282"
    assert d["source_commit"]==SOURCE and d["evaluation_date"]=="2026-09-01" and d["fixed_epoch"]==EPOCH
    assert d["scope_literal"]==SCOPE and d["evaluator"]["sha256"]==EVAL
    assert d["proof_contract"]["status"]=="PROVABLE AS STATED"
    assert d["transform_contract"]["formula"]=="Phi_{q,s}(u)=(beta-r_q)/(beta+s)*exp(-r_q*u)"
    assert "Phi(u)->0 selects beta-nu/c" in d["transform_contract"]["root_selection"]
    assert "two-dimensional inhomogeneous linear system" in d["transform_contract"]["uniqueness"]
    assert "strict ruin at u=0" in d["transform_contract"]["u_zero_extension"]
    assert "for nu=0 the conditional law is undefined" in d["transform_contract"]["memoryless_factorization"]
    assert "X_t=U_t for t<tau and X_t=Delta" in d["model_contract"]["killed_owner"]
    assert "conditional_first_mean_profitable" in d["regime_contract"] and "conditional_first_mean_adverse" in d["regime_contract"]
    assert d["regime_contract"]["critical_mean"]=="infinite"
    assert d["route_a"]=={"tuple":TUPLE,"overall":"ROUTE_A_REJECTED","route_b_invocation_allowed":False}
    assert all(v is False for v in d["scope_flags"].values())
    counts=d["regression"]["counts"]
    assert counts=={"regime_rows":36,"transform_rows":448,"first_mean_rows":144,"martingale_rows":12,"boundary_rows":6}
    yt=YAML.read_text()
    for token in ("candidate_id: HCS-C282",f"source_commit: {SOURCE}",f"fixed_epoch: {EPOCH}",f"scope_literal: {SCOPE}",
                  f"evaluator_authority_sha256: {EVAL}","A0_FAIL","A1_FAIL","A2_FAIL","A3_FAIL","A4_FAIL",
                  "overall_verdict: ROUTE_A_REJECTED","route_b_invocation_allowed: false"): assert token in yt,token
    cr=(PAPER/"COMPILE_REPORT.md").read_text()
    for token in (f"SOURCE_DATE_EPOCH={EPOCH}","byte-identical","warning-free","embedded and subset","visually inspected"): assert token in cr,token
    tt=" ".join(TEX.read_text().split())
    for token in (r"\cite{GerberShiu1998}",r"\cite{DrekicWillmot2003}","cited only for discounted-penalty lineage",
                  "cited only for exponential-claim ruin-time lineage","No formula or proof below is outsourced"): assert token in tt,token
    physical={str(p.relative_to(ROOT)):p for p in ROOT.rglob("*") if p.is_file()}
    assert not [n for n,p in physical.items() if sidecar(p)]
    files={n:digest(p) for n,p in sorted(physical.items()) if p!=MANIFEST}
    assert set(files)==EXPECTED,(sorted(EXPECTED-set(files)),sorted(set(files)-EXPECTED)); assert len(files)==27
    assert [digest(p) for p in ROUND_PATHS]==ROUND_HASHES and len(set(ROUND_HASHES))==3 and digest(PDF)==ROUND_HASHES[2]
    page_counts=[pages(p) for p in ROUND_PATHS]; assert page_counts==[2,3,3] and pages(PDF)==3
    font_counts=[]
    for p in ROUND_PATHS:
        rows=fonts(p); assert rows and all(len(x.split())>=7 and x.split()[-5]=="yes" and x.split()[-4]=="yes" for x in rows)
        font_counts.append(len(rows))
    txt=" ".join(subprocess.check_output(["pdftotext",str(PDF),"-"],text=True).lower().split())
    for token in ("complete exponential", "joint transform", "conditional on ruin", "safety-loading chamber",
                  "criticality", "adjustment martingale", "4,487", "26/26", "a0_fail", "a1_fail",
                  "route_a_rejected",SCOPE.lower(),"10.1080/10920277.1998.10595671","10.2143/ast.33.1.1036"):
        assert token in txt,token
    fresh_hashes=[]
    for i,(p,h) in enumerate(zip(ROUND_PATHS,ROUND_HASHES)):
        one,two=fresh(i),fresh(i); assert one==two==p.read_bytes()
        pair=[hashlib.sha256(one).hexdigest(),hashlib.sha256(two).hexdigest()]; assert pair==[h,h]; fresh_hashes.append(pair)
    producer,checker,sympy,replay,mutation=(runpy(x) for x in ["c282_ruin_producer.py","c282_ruin_checker.py","c282_ruin_sympy_crosscheck.py","c282_ruin_replay.py","c282_ruin_mutation.py"])
    assert "C282_PRODUCER_PASS" in producer and "C282 independent checker: PASS" in checker
    assert "C282_SYMPY_PASS" in sympy and "C282 byte replay: PASS" in replay
    cm=re.search(r"PASS \((\d+) assertions",checker); sm=re.search(r"PASS \((\d+) symbolic",sympy); mm=re.search(r"PASS (\d+)/(\d+)",mutation)
    assert cm and int(cm.group(1))==4487 and sm and int(sm.group(1))==15 and mm and mm.group(1)==mm.group(2)=="26"
    assert digest(EVIDENCE)==EVIDENCE_SHA
    result={"schema":"hcs-c282-release-v1","status":"RELEASE_COMPLETE","candidate_id":"HCS-C282","evaluation_date":"2026-09-01",
      "source_commit":SOURCE,"fixed_epoch":EPOCH,"scope_literal":SCOPE,"headline":d["headline"],"theorem_status":d["proof_contract"]["status"],
      "build_contract":{"engine":"LuaLaTeX","fixed_epoch":EPOCH,"passes_per_build":2,"fresh_builds_per_round":2,
        "round_artifacts":[str(p.relative_to(ROOT)) for p in ROUND_PATHS],"round_pdf_sha256":ROUND_HASHES,"fresh_build_sha256":fresh_hashes,"final_equals":"paper/main_round2.pdf"},
      "gates":{"G0_source_scope_evaluator":"PASS","G1_joint_transform":"PASS","G2_loading_atlas":"PASS","G3_overshoot_independence":"PASS",
        "G4_conditional_first_mean_critical_cusp":"PASS","G5_adjustment_martingale_supremum":"PASS","G6_checker_sympy_replay_mutation":"PASS",
        "G7_two_substantive_revisions":"PASS","G8_deterministic_pdf_fonts_log_visual":"PASS","G9_manifest_hash_closure":"PASS",
        "G10_claim_source_traceability":"PASS","G11_target_operator_route_b":"NOT_CLAIMED"},
      "results":{**counts,"checker_assertions":4487,"sympy_checks":15,"hostile_rejections":26,"pdf_pages":pages(PDF),"round_pdf_pages":page_counts,
        "embedded_subset_font_rows":font_counts,"evidence_bytes":EVIDENCE.stat().st_size,"evidence_payload_sha256":d["payload_sha256"],
        "evidence_sha256":EVIDENCE_SHA,"pdf_sha256":digest(PDF)},"route_a_verdict":d["route_a"],"nonclaims":d["nonclaims"],
      "excluded_from_manifest":["C282_RELEASE_MANIFEST.json","code/__pycache__/","*.pyc","paper build sidecars"],"files":files}
    MANIFEST.write_text(json.dumps(result,sort_keys=True,indent=2,ensure_ascii=False)+"\n")
    assert len([p for p in ROOT.rglob("*") if p.is_file()])==28
    print(json.dumps({"status":"C282_MANIFEST_PASS","payload_file_count":27,"physical_file_count":28,
      "manifest_sha256":digest(MANIFEST),"evidence_sha256":EVIDENCE_SHA,"pdf_sha256":digest(PDF)},sort_keys=True))

if __name__=="__main__": main()
