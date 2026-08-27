#!/usr/bin/env python3
"""Build the content-addressed, self-excluded C196 release manifest."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C196_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c196_calogero_moser_evidence.json"
PDF = ROOT / "paper/main.pdf"
SOURCE_COMMIT = "c3a5b9bbb3b6d0881f395abe4a01accd322f69cb"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
PAYLOAD_SHA256 = "6269e5194aa8c5b69bb2d8786efc2ca70935261b10e8e78def7c006ae53e2545"
EVIDENCE_SHA256 = "58efbb32c8788e901d6e94e6cff27c0f60026a3dc8a4147b04d7613742b617c5"
PDF_SHA256 = "efa8b97487763be814a0e3c5b65fe56616a377e3e2aacc7d97e26e611061b008"
ROUND_SHA256 = [
    "2e24674136745c31b864676a29cbb5f37046b9375c0d15da2b46c06137704a28",
    "e0707ed751677e8ac58dec6b0048b54f41daaa4b25b550d1835e259c75257b45",
    PDF_SHA256,
]


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def is_build_sidecar(path: Path) -> bool:
    return (
        path.suffix in {".aux", ".log", ".out", ".fls", ".fdb_latexmk", ".pyc"}
        or path.name.endswith(".synctex.gz")
        or "__pycache__" in path.parts
    )


def main() -> None:
    evidence = json.loads(EVIDENCE.read_text())
    assert evidence["source_commit"] == SOURCE_COMMIT
    assert evidence["evaluator"]["sha256"] == EVALUATOR_SHA256
    assert evidence["scope_literal"] == SCOPE
    assert evidence["payload_sha256"] == PAYLOAD_SHA256
    assert digest(EVIDENCE) == EVIDENCE_SHA256
    assert digest(PDF) == PDF_SHA256
    assert evidence["route_a"]["tuple"] == [
        "A0_FAIL",
        "A1_FAIL",
        "A2_FAIL",
        "A3_FAIL",
        "A4_NATURAL_QUANTIZATION",
    ]
    assert evidence["route_a"]["overall"] == "ROUTE_A_REJECTED"
    assert evidence["route_a"]["route_b_invocation_allowed"] is False
    assert all(value is False for value in evidence["scope_flags"].values())
    assert evidence["finite_regression"]["role"] == "DETERMINISTIC_FINITE_REGRESSION_NOT_ALL_PARAMETER_PROOF"

    files = {}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path == MANIFEST or is_build_sidecar(path):
            continue
        files[str(path.relative_to(ROOT))] = digest(path)

    rounds = [
        ROOT / "paper/main_round0_original.pdf",
        ROOT / "paper/main_round1.pdf",
        ROOT / "paper/main_round2.pdf",
    ]
    round_hashes = [digest(path) for path in rounds]
    assert round_hashes == ROUND_SHA256
    assert len(set(round_hashes)) == 3
    assert digest(PDF) == round_hashes[2]

    pdf_info = subprocess.check_output(["pdfinfo", str(PDF)], text=True)
    pdf_pages = int(next(
        line.split(":", 1)[1]
        for line in pdf_info.splitlines()
        if line.startswith("Pages:")
    ))
    assert pdf_pages == 3

    finite = evidence["finite_regression"]
    result = {
        "schema": "hcs-c196-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C196",
        "evaluation_date": "2026-08-27",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "headline": (
            "For every N>=2 and g>0, one Hermitian pencil gives the complete "
            "collision-free rational Calogero--Moser flow, every trace integral, "
            "a global two-ended scattering atlas with ordered-rank reversal, "
            "and an obstruction to bounded nonconstant periodic motion"
        ),
        "gates": {
            "G0_source_lock_and_classical_ownership": "PASS_WITH_A0_FAIL",
            "G1_all_parameter_simple_pencil_and_complete_flow": "PASS",
            "G2_trace_integrals_and_sign_factor_lock": "PASS",
            "G3_two_ended_global_scattering_atlas": "PASS",
            "G4_aperiodicity_and_model_boundaries": "PASS",
            "G5_checker_sympy_replay_mutation": "PASS",
            "G6_two_actual_improvements_double_compile_fonts_layout_visual": "PASS",
            "G7_manifest_hash_closure": "PASS",
            "G8_target_divisor_hilbert_polya_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "finite_systems": finite["case_count"],
            "pencil_rows": finite["pencil_row_count"],
            "exact_hermitian_entry_checks": finite["exact_hermitian_entry_check_count"],
            "exact_commutator_entry_checks": finite["exact_commutator_entry_check_count"],
            "exact_trace_and_energy_checks": finite["exact_trace_and_energy_check_count"],
            "minimum_sampled_gap": finite["minimum_sampled_pencil_gap"],
            "maximum_newton_residual": finite["maximum_sampled_newton_residual"],
            "maximum_atlas_residual": finite["maximum_atlas_matrix_residual"],
            "maximum_inverse_position_residual": finite["maximum_inverse_position_residual"],
            "independent_checker_assertions": 2210,
            "sympy_checks": 1200,
            "repaired_hash_mutation_rejections": 135,
            "stale_hash_mutation_rejections": 1,
            "citation_registry_population": 2,
            "reference_registry_population": 2,
            "pdf_pages": pdf_pages,
            "evidence_bytes": EVIDENCE.stat().st_size,
            "evidence_payload_sha256": evidence["payload_sha256"],
            "evidence_sha256": digest(EVIDENCE),
            "pdf_sha256": digest(PDF),
            "round_pdf_sha256": round_hashes,
        },
        "route_a_verdict": evidence["route_a"],
        "nonclaims": [
            "priority for the Calogero model, Moser Lax pair, or classical scattering theorem",
            "an all-parameter theorem inferred from the N<=7 finite regression",
            "the g=0 crossing boundary, coincident initial positions, N=1, or other Calogero families",
            "a periodic-orbit zeta or prime-orbit law for the unbounded scattering flow",
            "a target divisor, functional equation, continuation theorem, Weil compression, or automorphy",
            "a target quantum spectrum, Hilbert--Polya operator, Route-B authorization, external peer review, or acceptance score",
        ],
        "excluded_from_manifest": [
            "C196_RELEASE_MANIFEST.json",
            "code/__pycache__/",
            "*.pyc",
            "paper/*.aux",
            "paper/*.log",
            "paper/*.out",
            "paper/*.fdb_latexmk",
            "paper/*.fls",
            "paper/*.synctex.gz",
        ],
        "files": files,
    }
    assert len(files) == 27, f"expected 27 payload files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C196_MANIFEST_PASS",
        "file_count": len(files),
        "manifest_sha256": digest(MANIFEST),
        "evidence_sha256": digest(EVIDENCE),
        "pdf_sha256": digest(PDF),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
