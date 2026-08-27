#!/usr/bin/env python3
"""Build the content-addressed, self-excluded HCS-C207 manifest."""
from hashlib import sha256
import json,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; MANIFEST=ROOT/"C207_RELEASE_MANIFEST.json"; EVIDENCE=ROOT/"results/c207_barenblatt_evidence.json"; PDF=ROOT/"paper/main.pdf"
SOURCE_COMMIT="d108ef46fea7a8f62490a69071a83fcbda7c113b"; EVALUATOR_SHA256="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"; SCOPE="NO_BAD_EULER_OR_ROOT_NUMBER"
PAYLOAD_SHA256="3e10d74bd66d2e978cdbf9f6b27530b3367ceed7302b79b43f093fac6e4d58c0"; EVIDENCE_SHA256="aeb3b26292ffb91a4294c298d33d5d66af3a8bc122fa733fec3568dde42b69ad"; PDF_SHA256="e8270094821947d0c99bc2f59e011e73acfffb5a1f3bd495f5317ac18da863ea"; PDF_BYTES=188673; ROUND_HASHES=["122e5cc3513c8b04e1d710f3fb8d33bdcaddc4542ea989cd447c332d90bb96f0","49b47b489f55b9d718afa93b25dccac3884af3458b2df1a558f0706a31fe0841","e8270094821947d0c99bc2f59e011e73acfffb5a1f3bd495f5317ac18da863ea"]
EXPECTED_PAYLOADS=set("""EXPERIMENT_PLAN.md
NARRATIVE_REPORT.md
PAPER_IMPROVEMENT_LOG.md
PAPER_PLAN.md
README.md
RESEARCH_QUESTION.md
SOURCE_AUDIT.md
THEOREM_PACKAGE.md
code/README.md
code/c207_barenblatt_checker.py
code/c207_barenblatt_mutation.py
code/c207_barenblatt_producer.py
code/c207_barenblatt_replay.py
code/c207_barenblatt_sympy_crosscheck.py
code/c207_release_manifest.py
evaluations/route_a/HCS-C207/2026-08-27.yaml
paper/COMPILE_REPORT.md
paper/README.md
paper/main.pdf
paper/main.tex
paper/main_round0_original.pdf
paper/main_round1.pdf
paper/main_round2.pdf
results/HOSTILE_AUDIT.md
results/RESULTS.md
results/TEST_REPORT.md
results/c207_barenblatt_evidence.json""".splitlines())
def digest(p): return sha256(p.read_bytes()).hexdigest()
def sidecar(p): return p.suffix in {".aux",".log",".out",".toc",".pyc"} or "__pycache__" in p.parts or p.name.endswith(".synctex.gz")
def main():
    d=json.loads(EVIDENCE.read_text()); assert d["source_commit"]==SOURCE_COMMIT and d["evaluator"]["sha256"]==EVALUATOR_SHA256 and d["scope_literal"]==SCOPE
    assert d["payload_sha256"]==PAYLOAD_SHA256 and digest(EVIDENCE)==EVIDENCE_SHA256 and digest(PDF)==PDF_SHA256 and PDF.stat().st_size==PDF_BYTES
    assert d["route_a"]["tuple"]==["A0_FAIL","A1_FAIL","A2_FAIL","A3_FAIL","A4_FAIL"] and d["route_a"]["overall"]=="ROUTE_A_REJECTED" and d["route_a"]["route_b_invocation_allowed"] is False and all(v is False for v in d["scope_flags"].values())
    assert d["summary"]["working_decimal_digits"]==100 and d["summary"]["serialized_significant_digits"]==82
    physical={str(p.relative_to(ROOT)):p for p in ROOT.rglob("*") if p.is_file()}
    assert not [name for name,p in physical.items() if sidecar(p)],"build sidecar present"
    assert set(physical)==EXPECTED_PAYLOADS|{"C207_RELEASE_MANIFEST.json"},f"physical path mismatch: {set(physical)^ (EXPECTED_PAYLOADS|{'C207_RELEASE_MANIFEST.json'})}"
    files={name:digest(physical[name]) for name in sorted(EXPECTED_PAYLOADS)}
    rounds=[ROOT/"paper/main_round0_original.pdf",ROOT/"paper/main_round1.pdf",ROOT/"paper/main_round2.pdf"]; hashes=[digest(p) for p in rounds]
    assert hashes==ROUND_HASHES and len(set(hashes))==3 and digest(PDF)==hashes[2]
    info=subprocess.check_output(["pdfinfo",str(PDF)],text=True); pages=int(next(x.split(":",1)[1] for x in info.splitlines() if x.startswith("Pages:")))
    font_rows=subprocess.check_output(["pdffonts",str(PDF)],text=True).splitlines()[2:]
    assert font_rows and all(len(row.rsplit(maxsplit=5))==6 and row.rsplit(maxsplit=5)[1:3]==["yes","yes"] for row in font_rows),"fonts must be embedded and subsetted"
    pdf_text=subprocess.check_output(["pdftotext",str(PDF),"-"],text=True)
    assert len(pdf_text.strip())>1000 and SCOPE in pdf_text and "ROUTE_A_REJECTED" in pdf_text
    assert "100 working decimal digits" in pdf_text and "82 significant" in pdf_text
    result={"schema":"hcs-c207-release-v1","status":"RELEASE_COMPLETE","candidate_id":"HCS-C207","evaluation_date":"2026-08-27","source_commit":SOURCE_COMMIT,"scope_literal":SCOPE,"headline":d["headline"],
      "gates":{"G0_source_scope_evaluator_lock":"PASS","G1_full_exponent_similarity_classification":"PASS","G2_mass_moments_pressure_dissipation_boundaries":"PASS","G3_checker_sympy_replay_mutation":"PASS","G4_two_substantive_revisions":"PASS","G5_fixed_epoch_pdf_fonts_text_visual":"PASS","G6_manifest_hash_closure":"PASS","G7_target_operator_and_route_b":"NOT_CLAIMED"},
      "results":{"profiles":18,"profile_samples":90,"moment_cells":108,"checker_assertions":3462,"sympy_checks":56,"repaired_hash_rejections":33,"stale_hash_rejections":1,"hostile_rejections":34,"working_decimal_digits":100,"serialized_significant_digits":82,"serialized_decimal_fields":424,"serialized_nonzero_decimal_fields":382,"pdf_pages":pages,"evidence_bytes":EVIDENCE.stat().st_size,"evidence_payload_sha256":PAYLOAD_SHA256,"evidence_sha256":digest(EVIDENCE),"pdf_sha256":digest(PDF),"round_pdf_sha256":hashes},
      "route_a_verdict":d["route_a"],"nonclaims":d["nonclaims"],"excluded_from_manifest":["C207_RELEASE_MANIFEST.json","code/__pycache__/","*.pyc","paper build sidecars"],"files":files}
    assert pages>=2 and len(files)==27 and len(physical)==28,f"expected 28 physical/27 payload files, found {len(physical)}/{len(files)}"
    MANIFEST.write_text(json.dumps(result,sort_keys=True,indent=2,ensure_ascii=False)+"\n"); print(json.dumps({"status":"C207_MANIFEST_PASS","file_count":len(files),"manifest_sha256":digest(MANIFEST),"evidence_sha256":digest(EVIDENCE),"pdf_sha256":digest(PDF)},sort_keys=True))
if __name__=="__main__": main()
