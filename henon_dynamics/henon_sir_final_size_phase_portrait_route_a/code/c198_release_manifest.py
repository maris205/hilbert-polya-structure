#!/usr/bin/env python3
"""Build the content-addressed, self-excluded C198 release manifest."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C198_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c198_sir_evidence.json"
PDF = ROOT / "paper/main.pdf"
SOURCE_COMMIT = "c3a5b9bbb3b6d0881f395abe4a01accd322f69cb"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
PAYLOAD_SHA256 = "5b6114734a77816d288c4b7b9c7c523d7e280d9324f207bbbc20f1f0ee82e95d"
EVIDENCE_SHA256 = "9d426881cbf9bb9bc28a5c651dd99ba0d1395130f80b8b87e1e41f8a513a0115"
PDF_SHA256 = "6cfd1f076b390cc933801f1259942989676ec9b8eae6a0b47aac7ef0d721a426"
PDF_BYTES = 143321
ROUND_HASHES = [
    "cfbae96cdc33cc3474083e5881951bf6f2417c7e9dff4ab13ae1fef52007d247",
    "943261730aaf81b5e69baa8c64206755559fdbd4a7277e161da44d98d1265b4e",
    "6cfd1f076b390cc933801f1259942989676ec9b8eae6a0b47aac7ef0d721a426",
]


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def sidecar(path: Path) -> bool:
    return (path.suffix in {".aux", ".log", ".out", ".fls", ".fdb_latexmk", ".pyc"}
            or path.name.endswith(".synctex.gz") or "__pycache__" in path.parts)


def main() -> None:
    evidence = json.loads(EVIDENCE.read_text())
    assert evidence["source_commit"] == SOURCE_COMMIT
    assert evidence["evaluator"]["sha256"] == EVALUATOR_SHA256
    assert evidence["scope_literal"] == SCOPE
    assert evidence["payload_sha256"] == PAYLOAD_SHA256
    assert digest(EVIDENCE) == EVIDENCE_SHA256
    assert digest(PDF) == PDF_SHA256 and PDF.stat().st_size == PDF_BYTES
    assert evidence["route_a"]["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"]
    assert evidence["route_a"]["overall"] == "ROUTE_A_REJECTED"
    assert evidence["route_a"]["route_b_invocation_allowed"] is False
    assert all(value is False for value in evidence["scope_flags"].values())
    files = {}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path == MANIFEST or sidecar(path):
            continue
        files[str(path.relative_to(ROOT))] = digest(path)
    rounds = [ROOT/"paper/main_round0_original.pdf", ROOT/"paper/main_round1.pdf", ROOT/"paper/main_round2.pdf"]
    round_hashes = [digest(path) for path in rounds]
    assert round_hashes == ROUND_HASHES and len(set(round_hashes)) == 3
    assert digest(PDF) == round_hashes[2]
    info = subprocess.check_output(["pdfinfo", str(PDF)], text=True)
    pages = int(next(line.split(":",1)[1] for line in info.splitlines() if line.startswith("Pages:")))
    result = {
        "schema": "hcs-c198-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C198",
        "evaluation_date": "2026-08-27",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "headline": evidence["headline"],
        "gates": {
            "G0_source_lock_scope_and_no_clinical_data": "PASS",
            "G1_dimensionless_phase_portrait": "PASS",
            "G2_peak_final_size_branch_and_sensitivity": "PASS",
            "G3_global_convergence_and_no_recurrence": "PASS",
            "G4_checker_sympy_replay_mutation": "PASS",
            "G5_two_improvements_reproducible_pdf_visual": "PASS",
            "G6_manifest_hash_closure": "PASS",
            "G7_medical_target_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "phase_cases": evidence["summary"]["case_count"],
            "lambert_branch_values": evidence["summary"]["lambert_branch_values"],
            "physical_scalings": evidence["summary"]["physical_scaling_count"],
            "pdf_pages": pages,
            "evidence_bytes": EVIDENCE.stat().st_size,
            "evidence_payload_sha256": evidence["payload_sha256"],
            "evidence_sha256": digest(EVIDENCE),
            "pdf_sha256": digest(PDF),
            "round_pdf_sha256": round_hashes,
        },
        "route_a_verdict": evidence["route_a"],
        "nonclaims": evidence["nonclaims"],
        "excluded_from_manifest": ["C198_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper build sidecars"],
        "files": files,
    }
    assert len(files) == 27, f"expected 27 payload files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False)+"\n")
    print(json.dumps({
        "status": "C198_MANIFEST_PASS",
        "file_count": len(files),
        "manifest_sha256": digest(MANIFEST),
        "evidence_sha256": digest(EVIDENCE),
        "pdf_sha256": digest(PDF),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
