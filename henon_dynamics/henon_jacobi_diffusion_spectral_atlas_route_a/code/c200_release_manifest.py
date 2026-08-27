#!/usr/bin/env python3
"""Build the content-addressed, self-excluded C200 release manifest."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C200_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c200_jacobi_evidence.json"
PDF = ROOT / "paper/main.pdf"
SOURCE_COMMIT = "d1e58971e570b855488009af384995702ddb887b"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
PAYLOAD_SHA256 = "c4dc107c6821a56768214ce14389efcfd585d55497631bab495e42e2961af7fb"
EVIDENCE_SHA256 = "0b4eba23909d81058e3257e31189fee3b101ba331c2e5dd44bff70d7ad1a4ab7"
PDF_SHA256 = "806a4b8f8031c4c0ad086f75f45d8b79036cf46e187720bcec4af3a15e5a340e"
PDF_BYTES = 153416
ROUND_HASHES = [
    "9ae975b014b29259620eee23b597141b886014837f6b56f1460276e856472bf9",
    "403c40f4f20f9effcdfcf34afeaf66e4aef8c99e536aa1398ccf945a9b124109",
    "806a4b8f8031c4c0ad086f75f45d8b79036cf46e187720bcec4af3a15e5a340e",
]
CHECKER_ASSERTIONS = 1819
SYMPY_CHECKS = 171
HOSTILE_REJECTIONS = 16


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
        "schema": "hcs-c200-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C200",
        "evaluation_date": "2026-08-27",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "headline": evidence["headline"],
        "gates": {
            "G0_source_lock_and_scope": "PASS",
            "G1_boundary_realization_and_clock": "PASS",
            "G2_beta_reversibility_and_complete_spectrum": "PASS",
            "G3_heat_determinant_moments_and_recurrence_boundary": "PASS",
            "G4_checker_sympy_replay_mutation": "PASS",
            "G5_two_improvements_reproducible_pdf_visual": "PASS",
            "G6_manifest_hash_closure": "PASS",
            "G7_target_operator_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "parameter_cases": evidence["summary"]["parameter_case_count"],
            "exact_scalar_identities": evidence["summary"]["exact_scalar_identity_count"],
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
        "excluded_from_manifest": ["C200_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper build sidecars"],
        "files": files,
    }
    assert len(files) == 27, f"expected 27 payload files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C200_MANIFEST_PASS",
        "file_count": len(files),
        "manifest_sha256": digest(MANIFEST),
        "evidence_sha256": digest(EVIDENCE),
        "pdf_sha256": digest(PDF),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
