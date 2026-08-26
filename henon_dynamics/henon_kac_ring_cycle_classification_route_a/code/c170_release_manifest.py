#!/usr/bin/env python3
"""Build the content-addressed self-excluded C170 release manifest."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C170_RELEASE_MANIFEST.json"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    excluded = {
        MANIFEST,
        ROOT / "paper/main.aux", ROOT / "paper/main.log", ROOT / "paper/main.out",
        ROOT / "paper/main.fdb_latexmk", ROOT / "paper/main.fls",
        ROOT / "paper/main.synctex.gz",
    }
    files = {}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path in excluded or "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        files[str(path.relative_to(ROOT))] = digest(path)
    evidence = ROOT / "results/c170_kac_ring_evidence.json"
    pdf = ROOT / "paper/main.pdf"
    round0 = ROOT / "paper/main_round0_original.pdf"
    round1 = ROOT / "paper/main_round1.pdf"
    round2 = ROOT / "paper/main_round2.pdf"
    round_hashes = [digest(round0), digest(round1), digest(round2)]
    assert len(set(round_hashes)) == 3, "paper rounds must be distinct"
    assert digest(pdf) == round_hashes[2], "final must equal round 2"
    result = {
        "schema": "hcs-c170-release-v1",
        "status": "RELEASE_COMPLETE",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "Every finite Kac ring at every size and marker word is classified by eta into two N-cycles or one 2N-cycle, with exact zeta, Koopman roots, gauge reversor, and antiunitary",
        "gates": {
            "G0_source_lock_and_A0_arithmetic_gate": "PASS_WITH_A0_FAIL",
            "G1_all_N_all_marker_cycle_classification": "PASS",
            "G2_all_time_fixed_zeta_determinant_and_roots": "PASS",
            "G3_gauge_unfolding_reversor_and_antiunitary": "PASS",
            "G4_N1_and_self_adjoint_boundaries": "PASS",
            "G5_checker_sympy_replay_mutation": "PASS",
            "G6_bilingual_three_round_double_compile_fonts_layout_visual": "PASS",
            "G7_manifest_hash_closure": "PASS",
            "G8_target_divisor_matching": "NOT_ESTABLISHED",
            "G9_arithmetic_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "class_rows": 48,
            "enumerated_marker_configurations": 2046,
            "enumerated_states": 36868,
            "fixed_time_checks": 36868,
            "reversor_identity_checks": 73736,
            "independent_checker_assertions": 114056,
            "sympy_checks": 221,
            "repaired_hash_mutation_rejections": 16,
            "stale_hash_mutation_rejections": 1,
            "citation_registry_population": 0,
            "reference_registry_population": 0,
            "pdf_pages": 2,
            "evidence_sha256": digest(evidence),
            "pdf_sha256": digest(pdf),
            "round_pdf_sha256": round_hashes,
        },
        "route_a_verdict": {
            "A0": "A0_FAIL",
            "A0_qualification": "NO_INTRINSIC_ARITHMETIC_ORIGIN_OR_PRIME_CORRESPONDENCE",
            "A1": "A1_WEAK",
            "A1_qualification": "ALL_N_ALL_MARKER_PRIMITIVE_CYCLE_CLASSIFICATION_BUT_FINITE_REDUCIBLE_TOY_DYNAMICS",
            "A2": "A2_FAIL",
            "A2_qualification": "EXACT_FINITE_SOURCE_ZETA_WITH_NO_TARGET_DIVISOR_COMPARISON",
            "A3": "A3_FAIL",
            "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_OR_CONTINUATION_COMPARISON",
            "A4": "A4_NATURAL_QUANTIZATION",
            "A4_qualification": "SAME_CLOCK_FINITE_KOOPMAN_UNITARY_WITH_EXPLICIT_ANTIUNITARY_REVERSAL",
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "nonclaims": [
            "prime-like arithmetic semantics for finite Kac-ring cycles",
            "a target divisor, functional equation, counting law, or continuation match",
            "arithmetic local factors, Euler factors, root numbers, automorphy, or target spectral data",
            "a uniform self-adjoint Hilbert--Polya construction or Route-B authorization",
            "novelty priority, external peer review, or an independent error process",
        ],
        "excluded_from_manifest": [
            "C170_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc",
            "paper/main.aux", "paper/main.log", "paper/main.out",
            "paper/main.fdb_latexmk", "paper/main.fls", "paper/main.synctex.gz",
        ],
        "files": files,
    }
    assert len(files) == 27, f"expected 27 payload files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C170_MANIFEST_PASS", "file_count": len(files),
        "manifest_sha256": digest(MANIFEST), "evidence_sha256": digest(evidence),
        "pdf_sha256": digest(pdf),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
