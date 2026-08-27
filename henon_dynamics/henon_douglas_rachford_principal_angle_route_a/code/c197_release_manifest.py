#!/usr/bin/env python3
"""Build the content-addressed, self-excluded C197 release manifest."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C197_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c197_douglas_rachford_evidence.json"
PDF = ROOT / "paper/main.pdf"
SOURCE_COMMIT = "c3a5b9bbb3b6d0881f395abe4a01accd322f69cb"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
PAYLOAD_SHA256 = "562a3b72ea23f28b760659d011370de28b4acef13255f358f2fba68669e342fe"
EVIDENCE_SHA256 = "d26e80678baf92fbcb7f4c65951773e1cfe3e5ca528dbdbc34707d31b8ea8d59"
PDF_SHA256 = "44977c38ebb09c96a7f796810d20228d55d25a4726d5f069f1283fecc15f897d"
PDF_BYTES = 141352
ROUND_HASHES = [
    "4edd165c910f3e35cae0704ccc9ebd35e7a86928cc308fd0226cc3e2dd456ffa",
    "dfb16be399eb955641b9cd76e90d079cd67e2fc7e19ad25a5d82a4c167229e99",
    "44977c38ebb09c96a7f796810d20228d55d25a4726d5f069f1283fecc15f897d",
]


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def is_sidecar(path: Path) -> bool:
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
    assert evidence["route_a"]["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]
    assert evidence["route_a"]["overall"] == "ROUTE_A_REJECTED"
    assert evidence["route_a"]["route_b_invocation_allowed"] is False
    assert all(value is False for value in evidence["scope_flags"].values())

    files = {}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path == MANIFEST or is_sidecar(path):
            continue
        files[str(path.relative_to(ROOT))] = digest(path)
    rounds = [ROOT / "paper/main_round0_original.pdf", ROOT / "paper/main_round1.pdf", ROOT / "paper/main_round2.pdf"]
    round_hashes = [digest(path) for path in rounds]
    assert round_hashes == ROUND_HASHES and len(set(round_hashes)) == 3
    assert digest(PDF) == round_hashes[2]
    info = subprocess.check_output(["pdfinfo", str(PDF)], text=True)
    pages = int(next(line.split(":", 1)[1] for line in info.splitlines() if line.startswith("Pages:")))
    result = {
        "schema": "hcs-c197-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C197",
        "evaluation_date": "2026-08-27",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "headline": evidence["headline"],
        "gates": {
            "G0_source_lock_and_scope": "PASS",
            "G1_all_parameter_principal_angle_theorem": "PASS",
            "G2_convergence_rate_and_endpoint_boundaries": "PASS",
            "G3_trace_determinant_and_shadow_limit": "PASS",
            "G4_checker_sympy_replay_mutation": "PASS",
            "G5_two_improvements_reproducible_pdf_visual": "PASS",
            "G6_manifest_hash_closure": "PASS",
            "G7_target_divisor_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "block_rows": evidence["summary"]["block_row_count"],
            "composite_rows": evidence["summary"]["composite_row_count"],
            "exact_matrix_cells": evidence["summary"]["exact_matrix_cells"],
            "exact_power_trace_cells": evidence["summary"]["exact_power_trace_cells"],
            "pdf_pages": pages,
            "evidence_bytes": EVIDENCE.stat().st_size,
            "evidence_payload_sha256": evidence["payload_sha256"],
            "evidence_sha256": digest(EVIDENCE),
            "pdf_sha256": digest(PDF),
            "round_pdf_sha256": round_hashes,
        },
        "route_a_verdict": evidence["route_a"],
        "nonclaims": evidence["nonclaims"],
        "excluded_from_manifest": ["C197_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper build sidecars"],
        "files": files,
    }
    assert len(files) == 27, f"expected 27 payload files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C197_MANIFEST_PASS",
        "file_count": len(files),
        "manifest_sha256": digest(MANIFEST),
        "evidence_sha256": digest(EVIDENCE),
        "pdf_sha256": digest(PDF),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
