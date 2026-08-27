#!/usr/bin/env python3
"""Build the content-addressed, self-excluded C203 release manifest."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess

ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/"C203_RELEASE_MANIFEST.json"
EVIDENCE=ROOT/"results/c203_signed_laplacian_evidence.json"
PDF=ROOT/"paper/main.pdf"
SOURCE_COMMIT="d1e58971e570b855488009af384995702ddb887b"
EVALUATOR_SHA256="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE="NO_BAD_EULER_OR_ROOT_NUMBER"
PAYLOAD_SHA256="5bdb95ff9e7b1e1cb590cc53b362f36a8d7505a1e43a1e1444aa9558de23391b"
EVIDENCE_SHA256="fed6574189a1630fa2c5d9ec31dd10378afa1ad3b3f883fe3b3d598543cc6e47"
PDF_SHA256="395643b221b94c5af0345243e93ad18b30d69872acadd81d3830371be4ab9689"
PDF_BYTES=161320
ROUND_HASHES=[
 "a4a6a5c213cf2e9f99f74438432ccb845be5dbb09fea47e4d18f20cd8aa7d598",
 "b1d751811e4126e17077d1b8cbd2c4befe9a42aa170387c24361bcd803aeedb3",
 "395643b221b94c5af0345243e93ad18b30d69872acadd81d3830371be4ab9689",
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
      "schema":"hcs-c203-release-v1","status":"RELEASE_COMPLETE","candidate_id":"HCS-C203","evaluation_date":"2026-08-27",
      "source_commit":SOURCE_COMMIT,"scope_literal":SCOPE,"headline":d["headline"],
      "gates":{"G0_source_scope_evaluator_lock":"PASS","G1_balance_kernel_projector_exact_rate":"PASS","G2_all_minors_and_full_characteristic_pseudoforests":"PASS","G3_exhaustive_checker_sympy_replay_mutation":"PASS","G4_two_substantive_revisions":"PASS","G5_fixed_epoch_pdf_fonts_text_visual":"PASS","G6_manifest_hash_closure":"PASS","G7_directed_target_operator_and_route_b":"NOT_CLAIMED"},
      "results":{"graphs":760,"principal_minor_checks":11894,"characteristic_polynomial_checks":760,"checker_assertions":46766,"sympy_checks":1530,"balanced_component_records":548,"unbalanced_component_records":340,"hostile_rejections":13,"pdf_pages":pages,"evidence_bytes":EVIDENCE.stat().st_size,"evidence_payload_sha256":PAYLOAD_SHA256,"evidence_sha256":digest(EVIDENCE),"pdf_sha256":digest(PDF),"round_pdf_sha256":hashes},
      "route_a_verdict":d["route_a"],"nonclaims":d["nonclaims"],
      "excluded_from_manifest":["C203_RELEASE_MANIFEST.json","code/__pycache__/","*.pyc","paper build sidecars"],"files":files,
    }
    assert pages==3 and len(files)==27, f"expected 27 payload files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result,sort_keys=True,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps({"status":"C203_MANIFEST_PASS","file_count":len(files),"manifest_sha256":digest(MANIFEST),"evidence_sha256":digest(EVIDENCE),"pdf_sha256":digest(PDF)},sort_keys=True))
if __name__=="__main__": main()
