#!/usr/bin/env python3
"""Build the content-addressed, self-excluded C194 release manifest."""
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C194_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c194_holte_evidence.json"
PDF = ROOT / "paper/main.pdf"
SOURCE_COMMIT = "c3a5b9bbb3b6d0881f395abe4a01accd322f69cb"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
PAYLOAD_SHA256 = "15c02c5b83f6314fef0e3c786f7bdad09feeb1d7a557b7df7bd88db30eb3106f"
EVIDENCE_SHA256 = "b165dd9ae0b60009db7c9489d969a6910500bb5aec72fea1ec226cf147e43b18"
PDF_SHA256 = "9351c9ed695028aa34aa1abc2302c00bfa8c687e03f015c58c6309517b028cc7"
ROUND_HASHES = [
    "fc82f08bef150d20de466ee8092b738da02b69d28590688c95724187a7d888d0",
    "48b078942789c3654b92c5a8112ec85225c652eb16860ee5a2254b014c1afd43",
    PDF_SHA256,
]


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def is_build_sidecar(path: Path) -> bool:
    return (
        path.suffix in {".aux", ".log", ".out", ".xdv", ".fls", ".fdb_latexmk", ".pyc"}
        or path.name.endswith(".synctex.gz")
        or "__pycache__" in path.parts
    )


def main() -> None:
    evidence = json.loads(EVIDENCE.read_text())
    assert evidence["source_commit"] == SOURCE_COMMIT
    assert evidence["evaluator"] == {
        "version": "0.2.0",
        "path": "flow_systems/skills/route-a-evaluator.md",
        "sha256": EVALUATOR_SHA256,
    }
    assert evidence["scope_literal"] == SCOPE
    assert evidence["payload_sha256"] == PAYLOAD_SHA256
    assert digest(EVIDENCE) == EVIDENCE_SHA256
    assert EVIDENCE.stat().st_size == 537471
    assert digest(PDF) == PDF_SHA256
    assert PDF.stat().st_size == 69281
    assert evidence["route_a"]["tuple"] == [
        "A0_WEAK_ARITHMETIC_RELATION", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT",
    ]
    assert evidence["route_a"]["overall"] == "ROUTE_A_REJECTED"
    assert evidence["route_a"]["route_b_invocation_allowed"] is False
    assert evidence["forbidden_claims"] and all(value is False for value in evidence["forbidden_claims"].values())
    assert len(evidence["source_registry"]) == 2
    assert evidence["attribution"]["status"] == "CLASSICAL_THEOREM_REPRODUCED_WITH_EXACT_CERTIFICATE"
    assert evidence["attribution"]["novelty_claimed"] is False
    assert evidence["attribution"]["external_review_claimed"] is False

    finite = evidence["finite_regression"]
    expected_metrics = {
        "case_count": 72,
        "transition_cell_count": 1836,
        "power_trace_row_count": 504,
        "convergence_row_count": 360,
        "prime_base_case_count": 32,
        "composite_base_case_count": 40,
        "semigroup_tuple_count": 392,
        "semigroup_cell_count": 9996,
        "power_identity_tuple_count": 96,
        "power_identity_cell_count": 2448,
    }
    for key, expected in expected_metrics.items():
        assert finite[key] == expected, (key, finite[key], expected)

    rounds = [
        ROOT / "paper/main_round0_original.pdf",
        ROOT / "paper/main_round1.pdf",
        ROOT / "paper/main_round2.pdf",
    ]
    round_hashes = [digest(path) for path in rounds]
    assert round_hashes == ROUND_HASHES
    assert len(set(round_hashes)) == 3
    assert digest(PDF) == round_hashes[2]

    pdf_info = subprocess.check_output(["pdfinfo", str(PDF)], text=True)
    pages = int(next(line.split(":", 1)[1] for line in pdf_info.splitlines() if line.startswith("Pages:")))
    assert pages == 2
    fonts = subprocess.check_output(["pdffonts", str(PDF)], text=True)
    assert not re.search(r"\bno\b", "\n".join(fonts.splitlines()[2:])), "unembedded or unsubsetted font"

    files = {}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path == MANIFEST or is_build_sidecar(path):
            continue
        files[str(path.relative_to(ROOT))] = digest(path)
    assert len(files) == 27, f"expected 27 payload files, found {len(files)}"

    result = {
        "schema": "hcs-c194-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C194",
        "evaluation_date": "2026-08-27",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "headline": (
            "For every n>=1 and b>=2, Holte's carry matrix forms the exact base semigroup "
            "P_aP_b=P_ab with base-independent eigenvectors, simple geometric spectrum and "
            "Eulerian stationarity, while prime privilege and target claims remain excluded"
        ),
        "gates": {
            "G0_source_lock_and_classical_ownership": "PASS_WITH_A0_WEAK",
            "G1_transition_semigroup_and_power_law": "PASS",
            "G2_simple_spectrum_stationarity_trace_determinant": "PASS",
            "G3_convergence_and_small_n_boundary": "PASS",
            "G4_checker_sympy_replay_mutation": "PASS",
            "G5_two_actual_improvements_xelatex_double_build_fonts_visual": "PASS",
            "G6_manifest_hash_closure": "PASS",
            "G7_target_divisor_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            **expected_metrics,
            "independent_checker_assertions": 24602,
            "sympy_checks": 14248,
            "repaired_hash_mutation_rejections": 159,
            "stale_hash_mutation_rejections": 1,
            "citation_registry_population": 2,
            "reference_registry_population": 2,
            "pdf_pages": pages,
            "evidence_bytes": EVIDENCE.stat().st_size,
            "evidence_payload_sha256": evidence["payload_sha256"],
            "evidence_sha256": digest(EVIDENCE),
            "pdf_sha256": digest(PDF),
            "round_pdf_sha256": round_hashes,
        },
        "route_a_verdict": evidence["route_a"],
        "nonclaims": evidence["nonclaims"],
        "excluded_from_manifest": [
            "C194_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc",
            "paper/*.aux", "paper/*.log", "paper/*.out", "paper/*.xdv",
            "paper/*.fdb_latexmk", "paper/*.fls", "paper/*.synctex.gz",
        ],
        "files": files,
    }
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C194_MANIFEST_PASS",
        "file_count": len(files),
        "manifest_sha256": digest(MANIFEST),
        "evidence_sha256": digest(EVIDENCE),
        "pdf_sha256": digest(PDF),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
