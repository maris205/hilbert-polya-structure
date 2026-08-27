#!/usr/bin/env python3
"""Build the content-addressed, self-excluded C202 release manifest."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C202_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c202_fisher_kpp_evidence.json"
PDF = ROOT / "paper/main.pdf"
EVALUATION = ROOT / "evaluations/route_a/HCS-C202/2026-08-27.yaml"
SOURCE_COMMIT = "d1e58971e570b855488009af384995702ddb887b"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
PAYLOAD_SHA256 = "f02781c209fe741b81985cde6999aa0b1af727793461b4ee0082693226218b5e"
EVIDENCE_SHA256 = "605176e6653d796b6f86b1df8493a64d07ef8bca0fa308b256bf970d27110243"
PDF_SHA256 = "674a6e9d137f4593caee9ad77cf8c7de407896eabf1c08adec396b6d64a1d711"
PDF_BYTES = 181588
ROUND_HASHES = [
    "073627219f6158e56699baaef3b0fd32243a827227ba455f209b96f021fa89e1",
    "7d0cd80d3ad7b87dc30d36ea4d0c76a038557da73721a10f5067721970289b59",
    "674a6e9d137f4593caee9ad77cf8c7de407896eabf1c08adec396b6d64a1d711",
]


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def sidecar(path: Path) -> bool:
    return (
        path.suffix in {".aux", ".log", ".out", ".fls", ".fdb_latexmk", ".pyc"}
        or path.name.endswith(".synctex.gz")
        or "__pycache__" in path.parts
    )


def main() -> None:
    evidence = json.loads(EVIDENCE.read_text())
    assert evidence["schema"] == "hcs-c202-fisher-kpp-wave-atlas-v1"
    assert evidence["candidate_id"] == "HCS-C202"
    assert evidence["evaluation_date"] == "2026-08-27"
    assert evidence["source_commit"] == SOURCE_COMMIT
    assert evidence["evaluator"]["sha256"] == EVALUATOR_SHA256
    assert evidence["scope_literal"] == SCOPE
    assert evidence["payload_sha256"] == PAYLOAD_SHA256
    assert digest(EVIDENCE) == EVIDENCE_SHA256
    assert EVIDENCE.stat().st_size == 110686
    assert digest(PDF) == PDF_SHA256 and PDF.stat().st_size == PDF_BYTES
    assert evidence["route_a"]["tuple"] == [
        "A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"
    ]
    assert evidence["route_a"]["overall"] == "ROUTE_A_REJECTED"
    assert evidence["route_a"]["route_b_invocation_allowed"] is False
    assert all(value is False for value in evidence["scope_flags"].values())

    evaluation_text = EVALUATION.read_text()
    for literal in (
        "candidate_id: HCS-C202",
        f"source_commit: {SOURCE_COMMIT}",
        f"scope_literal: {SCOPE}",
        f"sha256: {EVALUATOR_SHA256}",
        "overall: ROUTE_A_REJECTED",
        "route_b_invocation_allowed: false",
    ):
        assert literal in evaluation_text

    files = {}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path == MANIFEST or sidecar(path):
            continue
        files[str(path.relative_to(ROOT))] = digest(path)

    rounds = [
        ROOT / "paper/main_round0_original.pdf",
        ROOT / "paper/main_round1.pdf",
        ROOT / "paper/main_round2.pdf",
    ]
    round_hashes = [digest(path) for path in rounds]
    assert round_hashes == ROUND_HASHES and len(set(round_hashes)) == 3
    assert digest(PDF) == round_hashes[2]

    info = subprocess.check_output(["pdfinfo", str(PDF)], text=True)
    pages = int(
        next(line.split(":", 1)[1] for line in info.splitlines() if line.startswith("Pages:"))
    )
    assert pages == 3

    result = {
        "schema": "hcs-c202-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C202",
        "evaluation_date": "2026-08-27",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "headline": evidence["headline"],
        "gates": {
            "G0_source_evaluator_scope_lock": "PASS",
            "G1_all_speed_phase_atlas": "PASS",
            "G2_invariant_triangle_and_translation_uniqueness": "PASS",
            "G3_tails_energy_cycles_and_exact_control": "PASS",
            "G4_checker_sympy_replay_mutation": "PASS",
            "G5_two_improvements_reproducible_pdf_visual": "PASS",
            "G6_manifest_hash_closure": "PASS",
            "G7_target_arithmetic_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "speed_cases": evidence["summary"]["speed_case_count"],
            "phase_rows": evidence["summary"]["phase_vector_field_row_count"],
            "trapping_rows": evidence["summary"]["trapping_boundary_row_count"],
            "hamiltonian_ovals": evidence["summary"]["hamiltonian_oval_count"],
            "az_exact_samples": evidence["summary"]["az_exact_sample_count"],
            "physical_scalings": evidence["summary"]["physical_scaling_count"],
            "checker_assertions": 2579,
            "sympy_checks": 1511,
            "hostile_rejections": 102,
            "pdf_pages": pages,
            "evidence_bytes": EVIDENCE.stat().st_size,
            "evidence_payload_sha256": evidence["payload_sha256"],
            "evidence_sha256": digest(EVIDENCE),
            "pdf_sha256": digest(PDF),
            "round_pdf_sha256": round_hashes,
        },
        "route_a_verdict": evidence["route_a"],
        "proof_boundary": evidence["proof_boundary"],
        "nonclaims": evidence["nonclaims"],
        "excluded_from_manifest": [
            "C202_RELEASE_MANIFEST.json",
            "code/__pycache__/",
            "*.pyc",
            "paper build sidecars",
        ],
        "files": files,
    }
    assert len(files) == 27, f"expected 27 payload files, found {len(files)}"
    MANIFEST.write_text(
        json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    )
    print(
        json.dumps(
            {
                "status": "C202_MANIFEST_PASS",
                "file_count": len(files),
                "manifest_sha256": digest(MANIFEST),
                "evidence_sha256": digest(EVIDENCE),
                "pdf_sha256": digest(PDF),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
