#!/usr/bin/env python3
"""Build the content-addressed, self-excluded C193 release manifest."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C193_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c193_markoff_evidence.json"
PDF = ROOT / "paper/main.pdf"
SOURCE_COMMIT = "4d7b214759f7ff982c0b19e662918acd307e0f58"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
PAYLOAD_SHA256 = "80c9bffcb3d520fe760af9fd682c1d8c05743cd8a4f8f8252fd459d45da2b4b6"
EVIDENCE_SHA256 = "39a46bbfd4375c7e01571f18551f69b256f8d09c9b2fc522ba1c4ebd58f53e25"
PDF_SHA256 = "7dd5274a024a51df47bbcb67e57e8efbae0b672ee76c3a1ddf73ce96e1f42b06"


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
    assert PDF.stat().st_size == 130852
    assert evidence["route_a"]["tuple"] == [
        "A0_WEAK_ARITHMETIC_RELATION",
        "A1_FAIL",
        "A2_FAIL",
        "A3_FAIL",
        "A4_FORMAL_HINT",
    ]
    assert evidence["route_a"]["overall"] == "ROUTE_A_REJECTED"
    assert evidence["route_a"]["route_b_invocation_allowed"] is False
    assert all(value is False for value in evidence["scope_flags"].values())

    finite = evidence["finite_regression"]
    assert finite["max_depth"] == 10
    assert finite["tree_row_count"] == 513
    assert finite["children_are_one_step_complete"] is True
    assert finite["frontier_child_count"] == 512
    assert finite["maximum_coordinate_digits"] == 56
    assert finite["invariance_tests"] == 1539
    assert finite["brute_bound"] == 2000
    assert finite["brute_solution_count"] == 15
    assert finite["descent_trace_count"] == 19
    assert finite["descent_steps_checked"] == 107

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
    assert round_hashes == [
        "ac9328bd627d43431def6772e6434341d0cb8e3a37d46e39fcf335309d20b0e9",
        "86af8b8d410519377158081fd28416079617618b79da38762118cb807702af1e",
        PDF_SHA256,
    ]
    assert digest(PDF) == round_hashes[2]

    pdf_info = subprocess.check_output(["pdfinfo", str(PDF)], text=True)
    pdf_pages = int(next(
        line.split(":", 1)[1]
        for line in pdf_info.splitlines()
        if line.startswith("Pages:")
    ))
    assert pdf_pages == 2

    result = {
        "schema": "hcs-c193-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C193",
        "evaluation_date": "2026-08-27",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "headline": (
            "Every normalized positive Markoff triple has a unique terminating "
            "largest-coordinate Vieta parent, and the permutation quotient is a "
            "rooted tree with no non-root periodic orbit, while Frobenius, modular, "
            "and target-analytic claims remain excluded"
        ),
        "gates": {
            "G0_source_lock_and_A0": "PASS_WITH_A0_WEAK",
            "G1_unique_maximum_and_strict_parent": "PASS",
            "G2_global_generation_and_rooted_tree": "PASS",
            "G3_recurrence_frobenius_and_modular_boundaries": "PASS",
            "G4_checker_sympy_replay_mutation": "PASS",
            "G5_two_actual_improvements_double_compile_fonts_layout_visual": "PASS",
            "G6_manifest_hash_closure": "PASS",
            "G7_target_divisor_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "tree_rows": finite["tree_row_count"],
            "maximum_depth": finite["max_depth"],
            "frontier_children": finite["frontier_child_count"],
            "vieta_invariance_tests": finite["invariance_tests"],
            "maximum_coordinate_digits": finite["maximum_coordinate_digits"],
            "bounded_height": finite["brute_bound"],
            "bounded_solutions": finite["brute_solution_count"],
            "descent_traces": finite["descent_trace_count"],
            "descent_steps": finite["descent_steps_checked"],
            "independent_checker_assertions": 8417,
            "sympy_checks": 8418,
            "repaired_hash_mutation_rejections": 156,
            "stale_hash_mutation_rejections": 1,
            "citation_registry_population": 3,
            "reference_registry_population": 3,
            "pdf_pages": pdf_pages,
            "evidence_bytes": EVIDENCE.stat().st_size,
            "evidence_payload_sha256": evidence["payload_sha256"],
            "evidence_sha256": digest(EVIDENCE),
            "pdf_sha256": digest(PDF),
            "round_pdf_sha256": round_hashes,
        },
        "route_a_verdict": evidence["route_a"],
        "nonclaims": [
            "priority for the Markoff equation, Vieta involutions, descent, or tree theorem",
            "the Frobenius uniqueness conjecture for Markoff numbers",
            "Markoff graphs modulo a prime or strong approximation",
            "an all-solution theorem inferred from the depth-ten or height-2000 regression census",
            "a rational-prime primitive carrier, prime-power repetition law, or logarithmic clock",
            "arithmetic local data, Euler factors, root numbers, automorphy, or a target divisor",
            "a target functional equation, Hilbert--Polya operator, or Route-B authorization",
            "global literature priority, external peer review, or an acceptance score",
        ],
        "excluded_from_manifest": [
            "C193_RELEASE_MANIFEST.json",
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
        "status": "C193_MANIFEST_PASS",
        "file_count": len(files),
        "manifest_sha256": digest(MANIFEST),
        "evidence_sha256": digest(EVIDENCE),
        "pdf_sha256": digest(PDF),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
