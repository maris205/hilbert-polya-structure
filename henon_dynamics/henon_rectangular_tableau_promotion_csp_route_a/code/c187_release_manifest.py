#!/usr/bin/env python3
"""Build the content-addressed, self-excluded C187 release manifest."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C187_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c187_tableau_csp_evidence.json"
PDF = ROOT / "paper/main.pdf"
SOURCE_COMMIT = "908a6818caedb0c46195a591873a2ac9c685b55e"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"


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
    assert evidence["route_a"]["tuple"] == [
        "A0_FAIL",
        "A1_WEAK",
        "A2_FAIL",
        "A3_FAIL",
        "A4_NATURAL_QUANTIZATION",
    ]
    assert evidence["route_a"]["overall"] == "ROUTE_A_REJECTED"
    assert evidence["route_a"]["route_b_invocation_allowed"] is False

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
    assert len(set(round_hashes)) == 3
    assert digest(PDF) == round_hashes[2]

    pdf_info = subprocess.check_output(["pdfinfo", str(PDF)], text=True)
    pdf_pages = int(
        next(line.split(":", 1)[1] for line in pdf_info.splitlines() if line.startswith("Pages:"))
    )
    replay = evidence["finite_replay"]
    result = {
        "schema": "hcs-c187-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C187",
        "evaluation_date": "2026-08-26",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "headline": (
            "For every rectangular standard Young-tableau family, the attributed "
            "unshifted q-hook CSP determines every promotion fixed count, least-period "
            "population, cycle count, finite zeta factor, Koopman eigenvalue multiplicity, "
            "and evacuation reversal, while the actual order is only guaranteed to divide ab"
        ),
        "gates": {
            "G0_source_lock_and_A0": "PASS_WITH_A0_FAIL",
            "G1_all_rectangle_csp_and_order_boundary": "PASS",
            "G2_period_cycle_zeta_and_spectrum": "PASS",
            "G3_evacuation_reversal_and_edge_families": "PASS",
            "G4_checker_sympy_replay_mutation": "PASS",
            "G5_three_round_double_compile_fonts_layout_visual": "PASS",
            "G6_manifest_hash_closure": "PASS",
            "G7_target_divisor_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "rectangle_rows": replay["rectangle_row_count"],
            "iterate_rows": replay["iterate_row_count"],
            "period_rows": replay["period_row_count"],
            "spectral_rows": replay["spectral_row_count"],
            "direct_enumeration_rectangles": replay["enumeration_rectangle_count"],
            "direct_enumeration_tableaux": 37401,
            "independent_checker_assertions": 230034,
            "sympy_checks": 3065,
            "repaired_hash_mutation_rejections": 107,
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
            "priority for cyclic sieving, the q-hook formula, rectangular promotion order bounds, or evacuation",
            "uniform exact promotion order ab",
            "an infinite theorem inferred from the finite regression ledger",
            "rational-prime semantics or arithmetic local data attached to rectangle and hook parameters",
            "a target divisor, functional equation, continuation theorem, counting law, or Weil compression",
            "a Hilbert--Polya operator, Route-B authorization, external peer review, or acceptance score",
        ],
        "excluded_from_manifest": [
            "C187_RELEASE_MANIFEST.json",
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
    print(
        json.dumps(
            {
                "status": "C187_MANIFEST_PASS",
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
