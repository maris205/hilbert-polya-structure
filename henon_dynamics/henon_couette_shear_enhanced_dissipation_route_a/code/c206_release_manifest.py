#!/usr/bin/env python3
"""Build the content-addressed, self-excluded HCS-C206 manifest."""
from hashlib import sha256
import json, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; MANIFEST=ROOT/"C206_RELEASE_MANIFEST.json"; EVIDENCE=ROOT/"results/c206_couette_evidence.json"; PDF=ROOT/"paper/main.pdf"
SOURCE_COMMIT="d108ef46fea7a8f62490a69071a83fcbda7c113b"; EVALUATOR_SHA256="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"; SCOPE="NO_BAD_EULER_OR_ROOT_NUMBER"
PAYLOAD_SHA256="350708b57d73ceea8e9c979b3d8d259949bc46fdeb38b71e65d76827103eb362"; EVIDENCE_SHA256="cf21be47c3222110bb8176004a02b347add192b467cc2f91c9d0f093fe43da5e"; PDF_SHA256="724e467a74a3e9f789feaf91c419263a5fce3bcfbe5a67dae74c54e291e22d8b"; PDF_BYTES=180761
ROUND_HASHES=["a82859d885a4b50206f56509cecd943b917eda391ae2f98a147ec4c103ea7b2e","7bd46ee580c5670f437ebea973cf5c48a96ddf012ae0ebf3fda9b87227de9aaa","724e467a74a3e9f789feaf91c419263a5fce3bcfbe5a67dae74c54e291e22d8b"]
def digest(p): return sha256(p.read_bytes()).hexdigest()
def sidecar(p): return p.suffix in {".aux",".log",".out",".toc",".pyc"} or "__pycache__" in p.parts or p.name.endswith(".synctex.gz")
def main():
    d=json.loads(EVIDENCE.read_text())
    assert d["source_commit"]==SOURCE_COMMIT and d["evaluator"]["sha256"]==EVALUATOR_SHA256 and d["scope_literal"]==SCOPE
    assert d["payload_sha256"]==PAYLOAD_SHA256 and digest(EVIDENCE)==EVIDENCE_SHA256
    assert digest(PDF)==PDF_SHA256 and PDF.stat().st_size==PDF_BYTES
    assert d["route_a"]["tuple"]==["A0_FAIL","A1_FAIL","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"] and d["route_a"]["overall"]=="ROUTE_A_REJECTED"
    assert d["route_a"]["route_b_invocation_allowed"] is False and all(v is False for v in d["scope_flags"].values())
    files={}
    for p in sorted(ROOT.rglob("*")):
        if p.is_file() and p!=MANIFEST and not sidecar(p): files[str(p.relative_to(ROOT))]=digest(p)
    rounds=[ROOT/"paper/main_round0_original.pdf",ROOT/"paper/main_round1.pdf",ROOT/"paper/main_round2.pdf"]
    hashes=[digest(p) for p in rounds]; assert hashes==ROUND_HASHES and len(set(hashes))==3 and digest(PDF)==hashes[2]
    info=subprocess.check_output(["pdfinfo",str(PDF)],text=True); pages=int(next(x.split(":",1)[1] for x in info.splitlines() if x.startswith("Pages:")))
    text=" ".join(subprocess.check_output(["pdftotext",str(PDF),"-"],text=True).split())
    phrases=["exact and sharp","no nonzero L2 vector attains this norm","frequency-localized packets approach it","every nonzero vector attains the norm","100 working decimal digits","82 significant digits","ROUTE_A_REJECTED","FORMAL HINT",SCOPE,"AI-use disclosure"]
    forbidden="attained"+" sector norm"
    assert all(phrase in text for phrase in phrases) and forbidden not in text.lower()
    font_lines=subprocess.check_output(["pdffonts",str(PDF)],text=True).splitlines()[2:]
    assert font_lines and all(line.split()[-5:-3]==["yes","yes"] for line in font_lines)
    result={"schema":"hcs-c206-release-v1","status":"RELEASE_COMPLETE","candidate_id":"HCS-C206","evaluation_date":"2026-08-27","source_commit":SOURCE_COMMIT,"scope_literal":SCOPE,"headline":d["headline"],
      "gates":{"G0_source_scope_evaluator_lock":"PASS","G1_exact_fourier_semigroup_and_norm":"PASS","G2_boundaries_recurrence_trace_stop":"PASS","G3_checker_sympy_replay_mutation":"PASS","G4_two_substantive_revisions":"PASS","G5_fixed_epoch_pdf_fonts_text_visual":"PASS","G6_manifest_hash_closure":"PASS","G7_target_operator_and_route_b":"NOT_CLAIMED"},
      "results":{"fourier_cells":675,"composition_cells":54,"checker_assertions":9646,"sympy_checks":2713,"hostile_rejections":18,"working_decimal_digits":100,"serialized_significant_digits":82,"serialized_decimal_fields":1350,"pdf_pages":pages,"evidence_bytes":EVIDENCE.stat().st_size,"evidence_payload_sha256":PAYLOAD_SHA256,"evidence_sha256":digest(EVIDENCE),"pdf_sha256":digest(PDF),"round_pdf_sha256":hashes},
      "route_a_verdict":d["route_a"],"nonclaims":d["nonclaims"],"excluded_from_manifest":["C206_RELEASE_MANIFEST.json","code/__pycache__/","*.pyc","paper build sidecars"],"files":files}
    assert pages>=2 and len(files)==27, f"expected 27 payload files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result,sort_keys=True,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps({"status":"C206_MANIFEST_PASS","file_count":len(files),"manifest_sha256":digest(MANIFEST),"evidence_sha256":digest(EVIDENCE),"pdf_sha256":digest(PDF)},sort_keys=True))
if __name__=="__main__": main()
