#!/usr/bin/env python3
"""Release closure for HCS-C272."""
from __future__ import annotations
import hashlib,json,os,re,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];MANIFEST=ROOT/"C272_RELEASE_MANIFEST.json";EVIDENCE=ROOT/"results/c272_age_evidence.json";PDF=ROOT/"paper/main.pdf"
SOURCE="9cb7483e97ef82fdc06d45ecb3043f183ce22391";EVALUATOR="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c";SCOPE="NO_BAD_EULER_OR_ROOT_NUMBER";EPOCH=1788134400
EXPECTED={"EXPERIMENT_PLAN.md","NARRATIVE_REPORT.md","PAPER_IMPROVEMENT_LOG.md","PAPER_PLAN.md","README.md","RESEARCH_QUESTION.md","SOURCE_AUDIT.md","THEOREM_PACKAGE.md","code/README.md","code/c272_age_checker.py","code/c272_age_mutation.py","code/c272_age_producer.py","code/c272_age_replay.py","code/c272_age_sympy_crosscheck.py","code/c272_release_manifest.py","evaluations/route_a/HCS-C272/2026-09-01.yaml","paper/COMPILE_REPORT.md","paper/README.md","paper/main.pdf","paper/main.tex","paper/main_round0_original.pdf","paper/main_round1.pdf","paper/main_round2.pdf","results/HOSTILE_AUDIT.md","results/RESULTS.md","results/TEST_REPORT.md","results/c272_age_evidence.json"}
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def sidecar(p):return p.suffix in {".aux",".log",".out",".toc",".fls",".fdb_latexmk",".pyc"} or "__pycache__" in p.parts or p.name.endswith(".synctex.gz")
def run(name):
 e=dict(os.environ);e["PYTHONDONTWRITEBYTECODE"]="1";return subprocess.check_output([sys.executable,"-B",str(ROOT/"code"/name)],env=e,text=True)
def main():
 d=json.loads(EVIDENCE.read_text());assert d["source_commit"]==SOURCE and d["fixed_epoch"]==EPOCH and d["scope_literal"]==SCOPE and d["evaluator"]["sha256"]==EVALUATOR
 assert d["route_a"]["overall"]=="ROUTE_A_REJECTED" and not d["route_a"]["route_b_invocation_allowed"] and all(v is False for v in d["scope_flags"].values())
 y=(ROOT/"evaluations/route_a/HCS-C272/2026-09-01.yaml").read_text()
 for x in ("candidate_id: HCS-C272",SOURCE,EVALUATOR,SCOPE,"A1_FAIL","A4_FORMAL_HINT","overall_verdict: ROUTE_A_REJECTED","route_b_invocation_allowed: false"):assert x in y
 report=(ROOT/"paper/COMPILE_REPORT.md").read_text();assert f"SOURCE_DATE_EPOCH={EPOCH}" in report and "byte-identical" in report and "warning-free" in report
 physical={str(p.relative_to(ROOT)):p for p in ROOT.rglob("*") if p.is_file()};assert not [n for n,p in physical.items() if sidecar(p)]
 files={n:digest(p) for n,p in sorted(physical.items()) if p!=MANIFEST};assert set(files)==EXPECTED,(sorted(EXPECTED-set(files)),sorted(set(files)-EXPECTED))
 rounds=[ROOT/"paper/main_round0_original.pdf",ROOT/"paper/main_round1.pdf",ROOT/"paper/main_round2.pdf"];rh=[digest(p) for p in rounds];assert len(set(rh))==3 and digest(PDF)==rh[2]
 pages=int(next(x.split(":",1)[1] for x in subprocess.check_output(["pdfinfo",str(PDF)],text=True).splitlines() if x.startswith("Pages:")));assert 2<=pages<=6
 fonts=[x for x in subprocess.check_output(["pdffonts",str(PDF)],text=True).splitlines()[2:] if x.strip() and not x.lstrip().startswith("-")];assert fonts and all(len(x.split())>=7 and x.split()[-5]=="yes" and x.split()[-4]=="yes" for x in fonts)
 text=re.sub(r"\s+"," ",subprocess.check_output(["pdftotext",str(PDF),"-"],text=True).lower())
 for x in ("erlang age-transport","essential edge","algebraic root","asynchronous","route_a_rejected",SCOPE.lower()):assert x in text,x
 po=run("c272_age_producer.py");ch=run("c272_age_checker.py");sy=run("c272_age_sympy_crosscheck.py");rp=run("c272_age_replay.py");mu=run("c272_age_mutation.py")
 assert "C272_PRODUCER_PASS" in po and "independent checker: PASS" in ch and "C272_SYMPY_PASS" in sy and "byte replay: PASS" in rp
 mm=re.search(r"PASS (\d+)/(\d+)",mu);assert mm and mm.group(1)==mm.group(2)
 result={"schema":"hcs-c272-release-v1","status":"RELEASE_COMPLETE","candidate_id":"HCS-C272","evaluation_date":"2026-09-01","source_commit":SOURCE,"fixed_epoch":EPOCH,"scope_literal":SCOPE,"headline":"Exact renewal poles, L1 eigenvalue gate, and essential-spectrum transition for an Erlang age-transport semigroup","build_contract":{"engine":"LuaLaTeX","fixed_epoch":EPOCH,"passes_per_build":2,"fresh_builds_per_round":2,"final_equals":"paper/main_round2.pdf"},"gates":{"theorem_status":"PROVABLE_AS_STATED","independent_checker":"PASS","symbolic_crosscheck":"PASS","byte_replay":"PASS","hostile_mutation":"PASS","deterministic_pdf":"PASS","manifest_closure":"PASS","target_operator_route_b":"NOT_CLAIMED"},"results":{"parameter_cases":d["regression"]["counts"]["parameter_cases"],"root_cells":d["regression"]["counts"]["root_cells"],"checker_assertions":int(re.search(r"\((\d+) assertions",ch).group(1)),"sympy_checks":int(re.search(r"\((\d+) symbolic",sy).group(1)),"hostile_rejections":int(mm.group(1)),"pdf_pages":pages,"embedded_subset_fonts":len(fonts),"evidence_sha256":digest(EVIDENCE),"pdf_sha256":digest(PDF),"round_pdf_sha256":rh},"route_a_verdict":d["route_a"],"nonclaims":d["nonclaims"],"excluded_from_manifest":["C272_RELEASE_MANIFEST.json","code/__pycache__/","*.pyc","paper build sidecars"],"files":files}
 assert len(files)==27;MANIFEST.write_text(json.dumps(result,sort_keys=True,indent=2,ensure_ascii=False)+"\n");assert len([p for p in ROOT.rglob("*") if p.is_file()])==28
 print(json.dumps({"status":"C272_MANIFEST_PASS","payload_file_count":27,"physical_file_count":28,"manifest_sha256":digest(MANIFEST),"evidence_sha256":digest(EVIDENCE),"pdf_sha256":digest(PDF)},sort_keys=True))
if __name__=="__main__":main()
