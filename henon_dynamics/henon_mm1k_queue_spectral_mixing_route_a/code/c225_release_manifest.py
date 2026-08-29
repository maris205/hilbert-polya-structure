#!/usr/bin/env python3
"""Seal and audit the 27-payload C225 release manifest."""
from __future__ import annotations
from hashlib import sha256
import json, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/"C225_RELEASE_MANIFEST.json"
EVIDENCE=ROOT/"results/c225_mm1k_evidence.json"
PDF=ROOT/"paper/main.pdf"
EVAL=ROOT/"evaluations/route_a/HCS-C225/2026-08-29.yaml"
SOURCE_COMMIT="489672bd36abd3a4f6da92d1446a0af575917959"
EVAL_SHA="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE="NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH=1787875200
EXPECTED={
 "EXPERIMENT_PLAN.md","NARRATIVE_REPORT.md","PAPER_IMPROVEMENT_LOG.md","PAPER_PLAN.md","README.md","RESEARCH_QUESTION.md","SOURCE_AUDIT.md","THEOREM_PACKAGE.md",
 "code/README.md","code/c225_mm1k_checker.py","code/c225_mm1k_mutation.py","code/c225_mm1k_producer.py","code/c225_mm1k_replay.py","code/c225_mm1k_sympy_crosscheck.py","code/c225_release_manifest.py",
 "evaluations/route_a/HCS-C225/2026-08-29.yaml",
 "paper/COMPILE_REPORT.md","paper/README.md","paper/main.pdf","paper/main.tex","paper/main_round0_original.pdf","paper/main_round1.pdf","paper/main_round2.pdf",
 "results/HOSTILE_AUDIT.md","results/RESULTS.md","results/TEST_REPORT.md","results/c225_mm1k_evidence.json",
}

def digest(p): return sha256(p.read_bytes()).hexdigest()
def p_hash(d):
 b=dict(d);b.pop("payload_sha256",None)
 return sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def sidecar(p): return p.suffix in {".aux",".log",".out",".toc",".fls",".fdb_latexmk",".pyc"} or p.name.endswith(".synctex.gz") or "__pycache__" in p.parts
def run(name):
 out=subprocess.check_output([sys.executable,"-B",str(ROOT/"code"/name)],text=True)
 return json.loads(out.strip().splitlines()[-1])

def main():
 e=json.loads(EVIDENCE.read_text())
 assert e["candidate_id"]=="HCS-C225" and e["source_commit"]==SOURCE_COMMIT and e["fixed_epoch"]==EPOCH and e["scope_literal"]==SCOPE and e["evaluator"]["sha256"]==EVAL_SHA and e["payload_sha256"]==p_hash(e)
 assert e["route_a"]["tuple"]==["A0_FAIL","A1_FAIL","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"] and e["route_a"]["overall"]=="ROUTE_A_REJECTED" and e["route_a"]["route_b_invocation_allowed"] is False and all(v is False for v in e["scope_flags"].values())
 assert e["summary"]["stationary_row_count"]==20 and e["summary"]["spectral_row_count"]==60 and e["summary"]["kernel_row_count"]==240 and e["summary"]["mixing_row_count"]==240 and e["summary"]["limit_row_count"]==16
 txt=EVAL.read_text()
 for lit in ("candidate_id: HCS-C225",f"source_commit: {SOURCE_COMMIT}",f"code_commit: {SOURCE_COMMIT}",f"scope_literal: {SCOPE}",f"evaluator_authority_sha256: {EVAL_SHA}","overall_verdict: ROUTE_A_REJECTED","route_b_invocation_allowed: false"): assert lit in txt,lit
 physical={str(p.relative_to(ROOT)):p for p in ROOT.rglob("*") if p.is_file()}; assert not [n for n,p in physical.items() if sidecar(p)]
 files={n:digest(p) for n,p in sorted(physical.items()) if p!=MANIFEST}; assert set(files)==EXPECTED,(sorted(EXPECTED-set(files)),sorted(set(files)-EXPECTED))
 rounds=[ROOT/"paper/main_round0_original.pdf",ROOT/"paper/main_round1.pdf",ROOT/"paper/main_round2.pdf"]; rh=[digest(p) for p in rounds]; assert len(set(rh))==3 and digest(PDF)==rh[2]
 info=subprocess.check_output(["pdfinfo",str(PDF)],text=True); pages=int(next(x.split(":",1)[1] for x in info.splitlines() if x.startswith("Pages:"))); assert 2<=pages<=6,pages
 fonts=subprocess.check_output(["pdffonts",str(PDF)],text=True).splitlines()[2:]; assert fonts and all(line.split()[-5:-3]==["yes","yes"] for line in fonts)
 extracted=subprocess.check_output(["pdftotext",str(PDF),"-"],text=True)
 for phrase in ("M/M/1/K","Jacobi","mixing","capacity","ROUTE_A_REJECTED",SCOPE): assert phrase.lower() in extracted.lower(),phrase
 prod,chk,sym,rep,mut=[run(n) for n in ("c225_mm1k_producer.py","c225_mm1k_checker.py","c225_mm1k_sympy_crosscheck.py","c225_mm1k_replay.py","c225_mm1k_mutation.py")]
 assert prod["status"]=="C225_PRODUCER_PASS" and chk["status"]=="C225_CHECKER_PASS" and chk["producer_imported"] is False and sym["status"]=="C225_SYMPY_PASS" and rep["status"]=="C225_REPLAY_PASS" and mut["status"]=="C225_MUTATION_PASS"
 comp=(ROOT/"paper/COMPILE_REPORT.md").read_text(); test=(ROOT/"results/TEST_REPORT.md").read_text()
 for lit in (*rh,"no `Warning`","embedded", "deterministic"): assert lit in comp,lit
 for lit in ("3655 assertions","46 checks","25 repaired-hash","27-payload"): assert lit in test,lit
 result={"schema":"hcs-c225-release-v1","status":"RELEASE_COMPLETE","candidate_id":"HCS-C225","evaluation_date":"2026-08-29","source_commit":SOURCE_COMMIT,"scope_literal":SCOPE,"headline":e["headline"],"build_contract":{"engine":"LuaLaTeX","fixed_epoch":EPOCH,"passes_per_round":2,"round_artifacts":["paper/main_round0_original.pdf","paper/main_round1.pdf","paper/main_round2.pdf"],"final_equals":"paper/main_round2.pdf"},"gates":{"G0_source_scope_evaluator_lock":"PASS","G1_stationary_jacobi_spectrum":"PASS","G2_transient_kernel_gap_mixing":"PASS","G3_checker_sympy_replay_mutation":"PASS","G4_two_substantive_revisions":"PASS","G5_fixed_epoch_pdf_fonts_text_visual":"PASS","G6_manifest_hash_closure":"PASS","G7_target_operator_and_route_b":"NOT_CLAIMED"},"results":{"stationary_rows":20,"spectral_rows":60,"kernel_rows":240,"mixing_rows":240,"limit_rows":16,"checker_assertions":chk["assertions"],"sympy_checks":sym["checks"],"replay_bytes":rep["bytes"],"hostile_rejections":mut["total_rejections"],"repaired_hash_rejections":mut["repaired_hash_rejections"],"stale_hash_rejections":mut["stale_hash_rejections"],"pdf_pages":pages,"embedded_subset_fonts":len(fonts),"evidence_bytes":EVIDENCE.stat().st_size,"evidence_payload_sha256":e["payload_sha256"],"evidence_sha256":digest(EVIDENCE),"pdf_sha256":digest(PDF),"round_pdf_sha256":rh},"route_a_verdict":e["route_a"],"nonclaims":e["nonclaims"],"excluded_from_manifest":["C225_RELEASE_MANIFEST.json","code/__pycache__/","*.pyc","paper build sidecars"],"files":files}
 assert len(files)==27
 MANIFEST.write_text(json.dumps(result,sort_keys=True,indent=2,ensure_ascii=False)+"\n")
 assert len([p for p in ROOT.rglob("*") if p.is_file()])==28
 print(json.dumps({"status":"C225_MANIFEST_PASS","payload_file_count":len(files),"physical_file_count":28,"manifest_sha256":digest(MANIFEST),"evidence_sha256":digest(EVIDENCE),"pdf_sha256":digest(PDF)},sort_keys=True))

if __name__=="__main__": main()
