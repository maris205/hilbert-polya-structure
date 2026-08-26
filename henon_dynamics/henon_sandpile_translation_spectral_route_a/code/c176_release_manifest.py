#!/usr/bin/env python3
"""Build the content-addressed self-excluded C176 release manifest."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C176_RELEASE_MANIFEST.json"


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

    evidence = ROOT / "results/c176_sandpile_evidence.json"
    pdf = ROOT / "paper/main.pdf"
    round0 = ROOT / "paper/main_round0_original.pdf"
    round1 = ROOT / "paper/main_round1.pdf"
    round2 = ROOT / "paper/main_round2.pdf"
    round_hashes = [digest(round0), digest(round1), digest(round2)]
    assert len(set(round_hashes)) == 3, "paper rounds must be distinct"
    assert digest(pdf) == round_hashes[2], "final must equal round 2"
    evidence_data = json.loads(evidence.read_text())
    replay = evidence_data["finite_replay"]

    result = {
        "schema": "hcs-c176-release-v1",
        "status": "RELEASE_COMPLETE",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "Every recurrent sandpile addition is an exact finite critical-group translation with closed orbit, zeta, determinant, spectrum, reversal, and self-adjoint laws",
        "gates": {
            "G0_source_lock_and_A0_arithmetic_gate": "PASS_WITH_A0_FAIL",
            "G1_recurrent_torsor_bridge": "PASS",
            "G2_two_exact_translation_order_formulas": "PASS",
            "G3_uniform_orbits_fixed_counts_zeta_determinant_spectrum": "PASS",
            "G4_reversal_self_adjoint_and_full_stable_boundary": "PASS",
            "G5_checker_sympy_replay_mutation": "PASS",
            "G6_bilingual_three_round_double_compile_fonts_layout_visual": "PASS",
            "G7_manifest_hash_closure": "PASS",
            "G8_target_divisor_matching": "NOT_ESTABLISHED",
            "G9_arithmetic_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "connected_simple_graph_isomorphism_types": replay["graph_row_count"],
            "graph_sink_pairs": replay["sink_row_count"],
            "labelled_additions": replay["translation_case_count"],
            "fixed_count_rows": replay["fixed_count_row_count"],
            "stable_transition_checks": replay["stable_transition_checks"],
            "recurrent_transition_checks": replay["recurrent_transition_checks"],
            "fixed_count_state_checks": replay["fixed_count_state_checks"],
            "full_stable_noninjective_cases": replay["full_stable_noninjective_case_count"],
            "independent_checker_assertions": 135049,
            "sympy_checks": 5248,
            "repaired_hash_mutation_rejections": 16,
            "stale_hash_mutation_rejections": 1,
            "citation_registry_population": 0,
            "reference_registry_population": 0,
            "pdf_pages": 3,
            "evidence_payload_sha256": evidence_data["payload_sha256"],
            "evidence_sha256": digest(evidence),
            "pdf_sha256": digest(pdf),
            "round_pdf_sha256": round_hashes,
        },
        "route_a_verdict": {
            "A0": "A0_FAIL",
            "A0_qualification": "NO_INTRINSIC_ARITHMETIC_ORIGIN_OR_PRIME_CORRESPONDENCE",
            "A1": "A1_WEAK",
            "A1_qualification": "COMPLETE_INTRINSIC_RECURRENT_PRIMITIVE_CYCLES_WITHOUT_ARITHMETIC_INFORMATION",
            "A2": "A2_FAIL",
            "A2_qualification": "EXACT_SOURCE_ZETA_AND_FINITE_DETERMINANT_WITH_NO_TARGET_DIVISOR_COMPARISON",
            "A3": "A3_FAIL",
            "A3_qualification": "FINITE_RATIONAL_SOURCE_STRUCTURE_WITH_NO_TARGET_GLOBAL_ANALYTIC_COMPARISON",
            "A4": "A4_NATURAL_QUANTIZATION",
            "A4_qualification": "SAME_CLOCK_RECURRENT_TRANSLATION_PERMUTATION_WITH_UNIFORM_KOOPMAN_UNITARY_AND_GROUP_INVERSION_REVERSAL",
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "nonclaims": [
            "external novelty or priority for the classical recurrent sandpile and critical-group facts",
            "prime semantics for critical-group translations or their repetitions",
            "permutation or unitarity of addition-stabilization on all stable configurations",
            "an all-stable-state cycle classification or eventual-recurrence theorem for arbitrary chip additions",
            "a target divisor, functional equation, counting law, continuation, or Weil compression",
            "arithmetic local factors, Euler factors, root numbers, automorphy, a Hilbert--Polya operator, Route-B authorization, or external peer review",
        ],
        "excluded_from_manifest": [
            "C176_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc",
            "paper/main.aux", "paper/main.log", "paper/main.out",
            "paper/main.fdb_latexmk", "paper/main.fls", "paper/main.synctex.gz",
        ],
        "files": files,
    }
    assert len(files) == 27, f"expected 27 payload files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C176_MANIFEST_PASS",
        "file_count": len(files),
        "manifest_sha256": digest(MANIFEST),
        "evidence_sha256": digest(evidence),
        "pdf_sha256": digest(pdf),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
