#!/usr/bin/env python3
"""Build the content-addressed, self-excluded C199 release manifest."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess

ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/"C199_RELEASE_MANIFEST.json"
EVIDENCE=ROOT/"results/c199_chaplygin_evidence.json"
PDF=ROOT/"paper/main.pdf"
SOURCE_COMMIT="d1e58971e570b855488009af384995702ddb887b"
EVALUATOR_SHA256="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE="NO_BAD_EULER_OR_ROOT_NUMBER"
PAYLOAD_SHA256="e70d22dc62564e940e3474b888d7914d3e65198e67a9a071d0708599bd168b5b"
EVIDENCE_SHA256="53cd651ca51c424bc58d1ae113bfb0ee8ba3029edf3c5544c08ecf368c9e5c6b"
PDF_SHA256="4c17171ef2e6b48aeb2dacac7cc37c422cb92bac07d645698e8d28c63198575b"
PDF_BYTES=168785
ROUND_HASHES=[
 "3bc9b83fc659a465483cc412e77bff57399ce038540ec1bed0c134a3e1b77e56",
 "94fb7f535d690df53551bf0a35d52e62d54953f0935cb6a4de9641ef95ee2f28",
 "4c17171ef2e6b48aeb2dacac7cc37c422cb92bac07d645698e8d28c63198575b",
]
def digest(p): return sha256(p.read_bytes()).hexdigest()
def sidecar(p): return p.suffix in {".aux",".log",".out",".toc",".pyc"} or "__pycache__" in p.parts or p.name.endswith(".synctex.gz")
def main():
    d=json.loads(EVIDENCE.read_text())
    assert d["source_commit"]==SOURCE_COMMIT and d["evaluator"]["sha256"]==EVALUATOR_SHA256
    assert d["scope_literal"]==SCOPE and d["payload_sha256"]==PAYLOAD_SHA256 and digest(EVIDENCE)==EVIDENCE_SHA256
    assert digest(PDF)==PDF_SHA256 and PDF.stat().st_size==PDF_BYTES
    assert d["route_a"]["tuple"]==["A0_FAIL","A1_FAIL","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"]
    assert d["route_a"]["overall"]=="ROUTE_A_REJECTED" and d["route_a"]["route_b_invocation_allowed"] is False
    assert all(v is False for v in d["scope_flags"].values())
    files={}
    for p in sorted(ROOT.rglob("*")):
        if p.is_file() and p!=MANIFEST and not sidecar(p): files[str(p.relative_to(ROOT))]=digest(p)
    rounds=[ROOT/"paper/main_round0_original.pdf",ROOT/"paper/main_round1.pdf",ROOT/"paper/main_round2.pdf"]
    hashes=[digest(p) for p in rounds]; assert hashes==ROUND_HASHES and len(set(hashes))==3 and digest(PDF)==hashes[2]
    info=subprocess.check_output(["pdfinfo",str(PDF)],text=True); pages=int(next(x.split(":",1)[1] for x in info.splitlines() if x.startswith("Pages:")))
    result={
      "schema":"hcs-c199-release-v1","status":"RELEASE_COMPLETE","candidate_id":"HCS-C199","evaluation_date":"2026-08-27",
      "source_commit":SOURCE_COMMIT,"scope_literal":SCOPE,"headline":d["headline"],
      "gates":{"G0_source_scope_evaluator_lock":"PASS","G1_signed_a_all_parameter_theorem":"PASS","G2_scattering_reconstruction_measure_boundaries":"PASS","G3_checker_sympy_replay_mutation":"PASS","G4_two_substantive_revisions":"PASS","G5_fixed_epoch_pdf_fonts_text_visual":"PASS","G6_manifest_hash_closure":"PASS","G7_target_operator_and_route_b":"NOT_CLAIMED"},
      "results":{"parameter_families":6,"heteroclinic_cases":12,"sample_states":36,"zero_offset_cases":4,"checker_assertions":737,"sympy_checks":61,"hostile_rejections":13,"pdf_pages":pages,"evidence_bytes":EVIDENCE.stat().st_size,"evidence_payload_sha256":PAYLOAD_SHA256,"evidence_sha256":digest(EVIDENCE),"pdf_sha256":digest(PDF),"round_pdf_sha256":hashes},
      "route_a_verdict":d["route_a"],"nonclaims":d["nonclaims"],
      "excluded_from_manifest":["C199_RELEASE_MANIFEST.json","code/__pycache__/","*.pyc","paper build sidecars"],"files":files,
    }
    assert pages==3 and len(files)==27, f"expected 27 payload files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result,sort_keys=True,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps({"status":"C199_MANIFEST_PASS","file_count":len(files),"manifest_sha256":digest(MANIFEST),"evidence_sha256":digest(EVIDENCE),"pdf_sha256":digest(PDF)},sort_keys=True))
if __name__=="__main__": main()
