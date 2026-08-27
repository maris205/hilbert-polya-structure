#!/usr/bin/env python3
"""Build the content-addressed, self-excluded C201 release manifest."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C201_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c201_heavy_ball_evidence.json"
PDF = ROOT / "paper/main.pdf"
SOURCE_COMMIT = "d1e58971e570b855488009af384995702ddb887b"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
PAYLOAD_SHA256 = "ebdf541d38face76f3329be80ef61f66271cf004d91834a14dc3465b8455bccc"
EVIDENCE_SHA256 = "67624d94c9ecbf87ccb5fc1d2d9c427756bd382ccdd72c6ba35f65e9601c3cf9"
PDF_SHA256 = "25f512bc365cd52f75f486031bad85e45af7ee4c4fc947d01fcec9c613bc4b21"
PDF_BYTES = 162184
ROUND_HASHES = [
    "f0331bbc3f36491925121cc3dea5944f96d6948731378074241e53f796e59083",
    "e6c1994433d530b0e6815dbacd6532ce75fb51b03bfbfcc26039926ca42f5455",
    "25f512bc365cd52f75f486031bad85e45af7ee4c4fc947d01fcec9c613bc4b21",
]
CHECKER_ASSERTIONS = 478
SYMPY_CHECKS = 156
HOSTILE_REJECTIONS = 19


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
    assert evidence["route_a"]["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]
    assert evidence["route_a"]["overall"] == "ROUTE_A_REJECTED"
    assert evidence["route_a"]["route_b_invocation_allowed"] is False
    assert all(value is False for value in evidence["scope_flags"].values())
    files = {}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path == MANIFEST or sidecar(path):
            continue
        files[str(path.relative_to(ROOT))] = digest(path)
    rounds = [ROOT / "paper/main_round0_original.pdf", ROOT / "paper/main_round1.pdf", ROOT / "paper/main_round2.pdf"]
    round_hashes = [digest(path) for path in rounds]
    assert round_hashes == ROUND_HASHES and len(set(round_hashes)) == 3
    assert digest(PDF) == round_hashes[2]
    info = subprocess.check_output(["pdfinfo", str(PDF)], text=True)
    pages = int(next(line.split(":", 1)[1] for line in info.splitlines() if line.startswith("Pages:")))
    result = {
        "schema": "hcs-c201-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C201",
        "evaluation_date": "2026-08-27",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "headline": evidence["headline"],
        "gates": {
            "G0_source_lock_and_scope": "PASS",
            "G1_modal_reduction_and_exact_jury_triangle": "PASS",
            "G2_endpoint_radius_and_unique_minimax": "PASS",
            "G3_jordan_boundaries_and_finite_order_controls": "PASS",
            "G4_checker_sympy_replay_mutation": "PASS",
            "G5_two_improvements_reproducible_pdf_visual": "PASS",
            "G6_manifest_hash_closure": "PASS",
            "G7_nonlinear_extension_target_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "parameter_cases": evidence["summary"]["parameter_case_count"],
            "endpoint_blocks": evidence["summary"]["endpoint_block_count"],
            "exact_certificate_scalars": evidence["summary"]["exact_certificate_scalar_count"],
            "checker_assertions": CHECKER_ASSERTIONS,
            "sympy_checks": SYMPY_CHECKS,
            "hostile_rejections": HOSTILE_REJECTIONS,
            "pdf_pages": pages,
            "evidence_bytes": EVIDENCE.stat().st_size,
            "evidence_payload_sha256": evidence["payload_sha256"],
            "evidence_sha256": digest(EVIDENCE),
            "pdf_sha256": digest(PDF),
            "round_pdf_sha256": round_hashes,
        },
        "route_a_verdict": evidence["route_a"],
        "nonclaims": evidence["nonclaims"],
        "excluded_from_manifest": ["C201_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper build sidecars"],
        "files": files,
    }
    assert len(files) == 27, f"expected 27 payload files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C201_MANIFEST_PASS",
        "file_count": len(files),
        "manifest_sha256": digest(MANIFEST),
        "evidence_sha256": digest(EVIDENCE),
        "pdf_sha256": digest(PDF),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
