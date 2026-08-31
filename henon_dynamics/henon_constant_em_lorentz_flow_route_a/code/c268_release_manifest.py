#!/usr/bin/env python3
"""Full release closure for HCS-C268."""
from __future__ import annotations
import hashlib,json,os,re,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];MANIFEST=ROOT/"C268_RELEASE_MANIFEST.json";EVIDENCE=ROOT/"results/c268_lorentz_evidence.json";PDF=ROOT/"paper/main.pdf";YAML=ROOT/"evaluations/route_a/HCS-C268/2026-08-31.yaml"
SOURCE="a24c701881d22a4e49eaa2a44b94395c3c540b3d";EVAL="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c";SCOPE="NO_BAD_EULER_OR_ROOT_NUMBER";EPOCH=1788048000
EXPECTED={"EXPERIMENT_PLAN.md","NARRATIVE_REPORT.md","PAPER_IMPROVEMENT_LOG.md","PAPER_PLAN.md","README.md","RESEARCH_QUESTION.md","SOURCE_AUDIT.md","THEOREM_PACKAGE.md","code/README.md","code/c268_lorentz_checker.py","code/c268_lorentz_mutation.py","code/c268_lorentz_producer.py","code/c268_lorentz_replay.py","code/c268_lorentz_sympy_crosscheck.py","code/c268_release_manifest.py","evaluations/route_a/HCS-C268/2026-08-31.yaml","paper/COMPILE_REPORT.md","paper/README.md","paper/main.pdf","paper/main.tex","paper/main_round0_original.pdf","paper/main_round1.pdf","paper/main_round2.pdf","results/HOSTILE_AUDIT.md","results/RESULTS.md","results/TEST_REPORT.md","results/c268_lorentz_evidence.json"}
TUPLE=["A0_FAIL","A1_WEAK","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"]
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def phash(d):
 q=dict(d);q.pop("payload_sha256",None);return hashlib.sha256(json.dumps(q,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def sidecar(p):return p.suffix in {".aux",".log",".out",".toc",".fls",".fdb_latexmk",".pyc"} or "__pycache__" in p.parts or p.name.endswith(".synctex.gz")
def run(name):
 e=dict(os.environ);e["PYTHONDONTWRITEBYTECODE"]="1";return subprocess.check_output([sys.executable,"-B",str(ROOT/"code"/name)],env=e,text=True)
def main():
 d=json.loads(EVIDENCE.read_text());assert d["candidate_id"]=="HCS-C268" and d["source_commit"]==SOURCE and d["fixed_epoch"]==EPOCH and d["scope_literal"]==SCOPE and d["evaluator"]["sha256"]==EVAL
 assert d["payload_sha256"]==phash(d);assert d["route_a"]["tuple"]==TUPLE and d["route_a"]["overall"]=="ROUTE_A_REJECTED" and d["route_a"]["route_b_invocation_allowed"] is False;assert all(v is False for v in d["scope_flags"].values())
 y=YAML.read_text()
 for x in ("candidate_id: HCS-C268",f"source_commit: {SOURCE}",f"scope_literal: {SCOPE}",f"evaluator_authority_sha256: {EVAL}","A1_WEAK","A4_FORMAL_HINT","overall_verdict: ROUTE_A_REJECTED","route_b_invocation_allowed: false"):assert x in y,x
 rep=(ROOT/"paper/COMPILE_REPORT.md").read_text();assert f"SOURCE_DATE_EPOCH={EPOCH}" in rep and "byte-identical" in rep and "warning-free" in rep
 physical={str(p.relative_to(ROOT)):p for p in ROOT.rglob("*") if p.is_file()};assert not [n for n,p in physical.items() if sidecar(p)]
 files={n:digest(p) for n,p in sorted(physical.items()) if p!=MANIFEST};assert set(files)==EXPECTED,(sorted(EXPECTED-set(files)),sorted(set(files)-EXPECTED))
 rounds=[ROOT/"paper/main_round0_original.pdf",ROOT/"paper/main_round1.pdf",ROOT/"paper/main_round2.pdf"];rh=[digest(p) for p in rounds];assert len(set(rh))==3 and digest(PDF)==rh[2]
 info=subprocess.check_output(["pdfinfo",str(PDF)],text=True);pages=int(next(x.split(":",1)[1] for x in info.splitlines() if x.startswith("Pages:")));assert 2<=pages<=6
 fonts=[x for x in subprocess.check_output(["pdffonts",str(PDF)],text=True).splitlines()[2:] if x.strip() and not x.lstrip().startswith("-")];assert fonts and all(len(x.split())>=7 and x.split()[-5]=="yes" and x.split()[-4]=="yes" for x in fonts)
 text=subprocess.check_output(["pdftotext",str(PDF),"-"],text=True).lower()
 for x in ("proper-time","characteristic polynomial","complementary projectors","least period","physical worldline","nonzero null field","a1_weak","a4_formal_hint","route_a_rejected",SCOPE.lower()):assert x in text,x
 po=run("c268_lorentz_producer.py");ch=run("c268_lorentz_checker.py");sy=run("c268_lorentz_sympy_crosscheck.py");rp=run("c268_lorentz_replay.py");mu=run("c268_lorentz_mutation.py")
 assert "C268_PRODUCER_PASS" in po and "C268 independent checker: PASS" in ch and "C268_SYMPY_PASS" in sy and "C268 byte replay: PASS" in rp
 mm=re.search(r"PASS (\d+)/(\d+)",mu);assert mm and mm.group(1)==mm.group(2);ac=int(re.search(r"PASS \((\d+) assertions",ch).group(1));sc=int(re.search(r"PASS \((\d+) symbolic",sy).group(1));hc=int(mm.group(1));c=d["regression"]["counts"]
 result={"schema":"hcs-c268-release-v1","status":"RELEASE_COMPLETE","candidate_id":"HCS-C268","evaluation_date":"2026-08-31","source_commit":SOURCE,"fixed_epoch":EPOCH,"scope_literal":SCOPE,"headline":"All-field invariant classification of constant electromagnetic proper-time Lorentz motion",
 "build_contract":{"engine":"LuaLaTeX","fixed_epoch":EPOCH,"passes_per_build":2,"fresh_builds_per_round":2,"round_artifacts":["paper/main_round0_original.pdf","paper/main_round1.pdf","paper/main_round2.pdf"],"final_equals":"paper/main_round2.pdf"},
 "gates":{"G0_source_scope_evaluator":"PASS","G1_EB_sign_and_eta_lie_algebra":"PASS","G2_characteristic_projectors":"PASS","G3_exponential_position_integral":"PASS","G4_norm_determinant_period_nonclosure":"PASS","G5_field_atlas_and_null_nilpotency":"PASS","G6_checker_sympy_replay_mutation":"PASS","G7_two_substantive_revisions":"PASS","G8_deterministic_pdf_fonts_log":"PASS","G9_manifest_hash_closure":"PASS","G10_target_operator_route_b":"NOT_CLAIMED"},
 "results":{"cases":c["cases"],"time_samples":c["time_samples"],"matrix_cells":c["matrix_cells"],"checker_assertions":ac,"sympy_checks":sc,"hostile_rejections":hc,"pdf_pages":pages,"embedded_subset_fonts":len(fonts),"evidence_bytes":EVIDENCE.stat().st_size,"evidence_payload_sha256":d["payload_sha256"],"evidence_sha256":digest(EVIDENCE),"pdf_sha256":digest(PDF),"round_pdf_sha256":rh},"route_a_verdict":d["route_a"],"nonclaims":d["nonclaims"],"excluded_from_manifest":["C268_RELEASE_MANIFEST.json","code/__pycache__/","*.pyc","paper build sidecars"],"files":files}
 assert len(files)==27;MANIFEST.write_text(json.dumps(result,sort_keys=True,indent=2,ensure_ascii=False)+"\n");assert len([p for p in ROOT.rglob("*") if p.is_file()])==28
 print(json.dumps({"status":"C268_MANIFEST_PASS","payload_file_count":27,"physical_file_count":28,"manifest_sha256":digest(MANIFEST),"evidence_sha256":digest(EVIDENCE),"pdf_sha256":digest(PDF)},sort_keys=True))
if __name__=="__main__":main()
