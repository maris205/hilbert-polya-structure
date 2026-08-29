#!/usr/bin/env python3
"""Build and validate the self-excluded HCS-C232 release manifest."""
from __future__ import annotations
from hashlib import sha256
import json, os, re, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/"C232_RELEASE_MANIFEST.json"; EVIDENCE=ROOT/"results/c232_duffing_evidence.json"; PDF=ROOT/"paper/main.pdf"; EVAL=ROOT/"evaluations/route_a/HCS-C232/2026-08-29.yaml"
SOURCE_COMMIT="e1dc522e054c2d0ded74b017bc52c7b016a52c59"; EVALUATOR_SHA256="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"; SCOPE="NO_BAD_EULER_OR_ROOT_NUMBER"; FIXED_EPOCH=1787875200
EXPECTED={"EXPERIMENT_PLAN.md","NARRATIVE_REPORT.md","PAPER_IMPROVEMENT_LOG.md","PAPER_PLAN.md","README.md","RESEARCH_QUESTION.md","SOURCE_AUDIT.md","THEOREM_PACKAGE.md","code/README.md","code/c232_duffing_checker.py","code/c232_duffing_mutation.py","code/c232_duffing_producer.py","code/c232_duffing_replay.py","code/c232_duffing_sympy_crosscheck.py","code/c232_release_manifest.py","evaluations/route_a/HCS-C232/2026-08-29.yaml","paper/COMPILE_REPORT.md","paper/README.md","paper/main.pdf","paper/main.tex","paper/main_round0_original.pdf","paper/main_round1.pdf","paper/main_round2.pdf","results/HOSTILE_AUDIT.md","results/RESULTS.md","results/TEST_REPORT.md","results/c232_duffing_evidence.json"}

def digest(p): return sha256(p.read_bytes()).hexdigest()
def payload_hash(d):
    b=dict(d); b.pop("payload_sha256",None); return sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def run(script):
    env=dict(os.environ); env["PYTHONDONTWRITEBYTECODE"]="1"; return subprocess.check_output([sys.executable,str(ROOT/"code"/script)],text=True,env=env)
def sidecar(p): return p.suffix in {".aux",".log",".out",".toc",".fls",".fdb_latexmk",".pyc"} or "__pycache__" in p.parts or p.name.endswith(".synctex.gz")

def main():
    e=json.loads(EVIDENCE.read_text()); assert e["source_commit"]==SOURCE_COMMIT; assert e["evaluator"]["sha256"]==EVALUATOR_SHA256; assert e["scope_literal"]==SCOPE; assert e["payload_sha256"]==payload_hash(e); assert e["route_a"]["tuple"]==["A0_FAIL","A1_WEAK","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"]; assert e["route_a"]["overall"]=="ROUTE_A_REJECTED"; assert e["route_a"]["route_b_invocation_allowed"] is False; assert all(v is False for v in e["scope_flags"].values())
    et=EVAL.read_text();
    for lit in ("candidate_id: HCS-C232",f"source_commit: {SOURCE_COMMIT}",f"scope_literal: {SCOPE}",f"evaluator_authority_sha256: {EVALUATOR_SHA256}","overall_verdict: ROUTE_A_REJECTED","route_b_invocation_allowed: false","continuous energy"):
        assert lit in et,lit
    cr=(ROOT/"paper/COMPILE_REPORT.md").read_text(); assert f"SOURCE_DATE_EPOCH={FIXED_EPOCH}" in cr
    physical={str(p.relative_to(ROOT)):p for p in ROOT.rglob("*") if p.is_file()}; assert not [n for n,p in physical.items() if sidecar(p)]
    files={n:digest(p) for n,p in sorted(physical.items()) if p!=MANIFEST}; assert set(files)==EXPECTED, f"payload mismatch missing={sorted(EXPECTED-set(files))} extra={sorted(set(files)-EXPECTED)}"
    rounds=[ROOT/"paper/main_round0_original.pdf",ROOT/"paper/main_round1.pdf",ROOT/"paper/main_round2.pdf"]; hashes=[digest(p) for p in rounds]; assert len(set(hashes))==3 and digest(PDF)==hashes[2]
    info=subprocess.check_output(["pdfinfo",str(PDF)],text=True); pages=int(next(x.split(":",1)[1] for x in info.splitlines() if x.startswith("Pages:"))); assert 2<=pages<=6
    fonts=subprocess.check_output(["pdffonts",str(PDF)],text=True).splitlines()[2:]; assert fonts and all(len(x.split())>=7 and x.split()[4]=="yes" and x.split()[5]=="yes" for x in fonts)
    txt=subprocess.check_output(["pdftotext",str(PDF),"-"],text=True).lower()
    for phrase in ("duffing","homoclinic","quartic","790 assertions","21/21","route_a_rejected","a4_formal_hint",SCOPE.lower(),"not external peer review"): assert phrase in txt,phrase
    checker=run("c232_duffing_checker.py"); sympy=run("c232_duffing_sympy_crosscheck.py"); replay=run("c232_duffing_replay.py"); mutation=run("c232_duffing_mutation.py"); assert "independent checker: PASS" in checker; assert "SymPy cross-check: PASS" in sympy; assert "C232_REPLAY_PASS" in replay and "payload_sha256" in replay; mm=re.search(r"repaired_hash_rejections[\"']?\s*:\s*(\d+)",mutation); assert mm and int(mm.group(1))>=19
    checker_count=int(re.search(r"\((\d+) assertions",checker).group(1)); sympy_count=int(re.search(r"PASS \((\d+) symbolic",sympy).group(1)); hostile=int(re.search(r"total_rejections[\"']?\s*:\s*(\d+)",mutation).group(1))
    result={"schema":"hcs-c232-release-v1","status":"RELEASE_COMPLETE","candidate_id":"HCS-C232","evaluation_date":"2026-08-29","source_commit":SOURCE_COMMIT,"scope_literal":SCOPE,"headline":e["headline"],"build_contract":{"engine":"LuaLaTeX","fixed_epoch":FIXED_EPOCH,"passes_per_round":2,"round_artifacts":["paper/main_round0_original.pdf","paper/main_round1.pdf","paper/main_round2.pdf"],"final_equals":"paper/main_round2.pdf"},"gates":{"G0_source_scope_evaluator_lock":"PASS","G1_energy_topology_and_turning_roots":"PASS","G2_action_period_and_homoclinic":"PASS","G3_checker_sympy_replay_mutation":"PASS","G4_two_substantive_revisions":"PASS","G5_fixed_epoch_pdf_fonts_text_visual":"PASS","G6_manifest_hash_closure":"PASS","G7_target_operator_and_route_b":"NOT_CLAIMED"},"results":{"energy_rows":e["regression"]["energy_row_count"],"case_count":e["regression"]["case_count"],"checker_assertions":checker_count,"sympy_checks":sympy_count,"hostile_rejections":hostile,"pdf_pages":pages,"embedded_subset_fonts":len(fonts),"evidence_bytes":EVIDENCE.stat().st_size,"evidence_payload_sha256":e["payload_sha256"],"evidence_sha256":digest(EVIDENCE),"pdf_sha256":digest(PDF),"round_pdf_sha256":hashes},"route_a_verdict":e["route_a"],"nonclaims":e["nonclaims"],"excluded_from_manifest":["C232_RELEASE_MANIFEST.json","code/__pycache__/","*.pyc","paper build sidecars"],"files":files}
    assert len(files)==27; MANIFEST.write_text(json.dumps(result,sort_keys=True,indent=2,ensure_ascii=False)+"\n"); assert len([p for p in ROOT.rglob("*") if p.is_file()])==28
    print(json.dumps({"status":"C232_MANIFEST_PASS","payload_file_count":len(files),"physical_file_count":28,"manifest_sha256":digest(MANIFEST),"evidence_sha256":digest(EVIDENCE),"pdf_sha256":digest(PDF)},sort_keys=True))

if __name__=="__main__": main()
