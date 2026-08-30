#!/usr/bin/env python3
"""Content-addressed release gate for HCS-C252."""
from __future__ import annotations
import hashlib,json,os,re,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; MAN=ROOT/"C252_RELEASE_MANIFEST.json"; E=ROOT/"results/c252_relay_evidence.json"; PDF=ROOT/"paper/main.pdf"; YAML=ROOT/"evaluations/route_a/HCS-C252/2026-08-30.yaml"
SOURCE="3ff451e904f8f063e88c40ef87f4697a6586b1a5"; EVAL="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"; SCOPE="NO_BAD_EULER_OR_ROOT_NUMBER"; EPOCH=1788048000
EXPECTED={"EXPERIMENT_PLAN.md","NARRATIVE_REPORT.md","PAPER_IMPROVEMENT_LOG.md","PAPER_PLAN.md","README.md","RESEARCH_QUESTION.md","SOURCE_AUDIT.md","THEOREM_PACKAGE.md","code/README.md","code/c252_relay_checker.py","code/c252_relay_mutation.py","code/c252_relay_producer.py","code/c252_relay_replay.py","code/c252_relay_sympy_crosscheck.py","code/c252_release_manifest.py","evaluations/route_a/HCS-C252/2026-08-30.yaml","paper/COMPILE_REPORT.md","paper/README.md","paper/main.pdf","paper/main.tex","paper/main_round0_original.pdf","paper/main_round1.pdf","paper/main_round2.pdf","results/HOSTILE_AUDIT.md","results/RESULTS.md","results/TEST_REPORT.md","results/c252_relay_evidence.json"}
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def ph(d):
 b=dict(d); b.pop("payload_sha256",None); return hashlib.sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def side(p): return p.suffix in {".aux",".log",".out",".toc",".fls",".fdb_latexmk",".pyc"} or p.name.endswith(".synctex.gz") or "__pycache__" in p.parts
def run(n):
 e=dict(os.environ); e["PYTHONDONTWRITEBYTECODE"]="1"; return subprocess.check_output([sys.executable,"-B",str(ROOT/"code"/n)],env=e,text=True)
def main():
 d=json.loads(E.read_text()); assert d["candidate_id"]=="HCS-C252" and d["source_commit"]==SOURCE and d["fixed_epoch"]==EPOCH and d["scope_literal"]==SCOPE and d["evaluator"]["sha256"]==EVAL and d["payload_sha256"]==ph(d)
 assert d["route_a"]["tuple"]==["A0_FAIL","A1_PASS_ANALYTIC","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"] and d["route_a"]["overall"]=="ROUTE_A_REJECTED" and d["route_a"]["route_b_invocation_allowed"] is False and all(v is False for v in d["scope_flags"].values())
 y=YAML.read_text()
 for lit in ("candidate_id: HCS-C252",f"source_commit: {SOURCE}",f"scope_literal: {SCOPE}",f"evaluator_authority_sha256: {EVAL}","overall_verdict: ROUTE_A_REJECTED","route_b_invocation_allowed: false","A1_PASS_ANALYTIC","no sliding"):
  assert lit in y,lit
 assert f"SOURCE_DATE_EPOCH={EPOCH}" in (ROOT/"paper/COMPILE_REPORT.md").read_text()
 physical={str(p.relative_to(ROOT)):p for p in ROOT.rglob("*") if p.is_file()}; assert not [n for n,p in physical.items() if side(p)]
 files={n:digest(p) for n,p in sorted(physical.items()) if p!=MAN}; assert set(files)==EXPECTED,f"payload mismatch missing={sorted(EXPECTED-set(files))} extra={sorted(set(files)-EXPECTED)}"
 rounds=[ROOT/"paper/main_round0_original.pdf",ROOT/"paper/main_round1.pdf",ROOT/"paper/main_round2.pdf"]; rh=[digest(p) for p in rounds]; assert len(set(rh))==3 and digest(PDF)==rh[2]
 info=subprocess.check_output(["pdfinfo",str(PDF)],text=True); pages=int(next(x.split(":",1)[1] for x in info.splitlines() if x.startswith("Pages:"))); assert 2<=pages<=6
 fonts=[x for x in subprocess.check_output(["pdffonts",str(PDF)],text=True).splitlines()[2:] if x.strip() and not x.lstrip().startswith("-")]; assert fonts and all(len(x.split())>=7 and x.split()[-5]=="yes" and x.split()[-4]=="yes" for x in fonts)
 txt=subprocess.check_output(["pdftotext",str(PDF),"-"],text=True).lower()
 for phrase in ("hysteretic","relay","poincare","period","no-zeno","a1_pass_analytic","route_a_rejected",SCOPE.lower(),"arithmetic origin"): assert phrase in txt,phrase
 prod=run("c252_relay_producer.py"); chk=run("c252_relay_checker.py"); sym=run("c252_relay_sympy_crosscheck.py"); rep=run("c252_relay_replay.py"); mut=run("c252_relay_mutation.py")
 assert "C252_PRODUCER_PASS" in prod and "C252 independent checker: PASS" in chk and "C252_SYMPY_PASS" in sym and "C252 byte replay: PASS" in rep
 mm=re.search(r"PASS (\d+)/(\d+)",mut); assert mm and mm.group(1)==mm.group(2)
 ca=int(re.search(r"PASS \((\d+) assertions",chk).group(1)); sy=int(re.search(r"PASS \((\d+) symbolic",sym).group(1)); hostile=int(mm.group(1))
 result={"schema":"hcs-c252-release-v1","status":"RELEASE_COMPLETE","candidate_id":"HCS-C252","evaluation_date":"2026-08-30","source_commit":SOURCE,"fixed_epoch":EPOCH,"scope_literal":SCOPE,"headline":d["headline"],"build_contract":{"engine":"LuaLaTeX","fixed_epoch":EPOCH,"passes_per_round":2,"fresh_builds_per_round":2,"round_artifacts":["paper/main_round0_original.pdf","paper/main_round1.pdf","paper/main_round2.pdf"],"final_equals":"paper/main_round2.pdf"},"gates":{"G0_source_scope_evaluator_lock":"PASS","G1_guard_priority_and_forward_wellposedness":"PASS","G2_exact_event_return_map":"PASS","G3_periodic_set_and_no_zeno":"PASS","G4_checker_sympy_replay_mutation":"PASS","G5_two_substantive_revisions":"PASS","G6_fixed_epoch_pdf_fonts_text_visual":"PASS","G7_manifest_hash_closure":"PASS","G8_target_operator_and_route_b":"NOT_CLAIMED"},"results":{"rows":d["regression"]["row_count"],"boundary_rows":d["regression"]["boundary_row_count"],"checker_assertions":ca,"sympy_checks":sy,"hostile_rejections":hostile,"pdf_pages":pages,"embedded_subset_fonts":len(fonts),"evidence_bytes":E.stat().st_size,"evidence_payload_sha256":d["payload_sha256"],"evidence_sha256":digest(E),"pdf_sha256":digest(PDF),"round_pdf_sha256":rh},"route_a_verdict":d["route_a"],"nonclaims":d["nonclaims"],"excluded_from_manifest":["C252_RELEASE_MANIFEST.json","code/__pycache__/","*.pyc","paper build sidecars"],"files":files}
 assert len(files)==27; MAN.write_text(json.dumps(result,sort_keys=True,indent=2,ensure_ascii=False)+"\n"); assert len([p for p in ROOT.rglob("*") if p.is_file()])==28
 print(json.dumps({"status":"C252_MANIFEST_PASS","payload_file_count":27,"physical_file_count":28,"manifest_sha256":digest(MAN),"evidence_sha256":digest(E),"pdf_sha256":digest(PDF)},sort_keys=True))
if __name__=="__main__": main()
