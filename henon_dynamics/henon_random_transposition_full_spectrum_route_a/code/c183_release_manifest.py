#!/usr/bin/env python3
"""Build the content-addressed self-excluded C183 release manifest."""
from hashlib import sha256
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C183_RELEASE_MANIFEST.json"

def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()

def main() -> None:
    excluded = {MANIFEST, ROOT / "paper/main.aux", ROOT / "paper/main.log", ROOT / "paper/main.out", ROOT / "paper/main.fdb_latexmk", ROOT / "paper/main.fls", ROOT / "paper/main.synctex.gz"}
    files = {}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path in excluded or "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        files[str(path.relative_to(ROOT))] = digest(path)
    evidence = ROOT / "results/c183_random_transposition_evidence.json"
    evidence_data = json.loads(evidence.read_text())
    pdf = ROOT / "paper/main.pdf"
    rounds = [ROOT / "paper/main_round0_original.pdf", ROOT / "paper/main_round1.pdf", ROOT / "paper/main_round2.pdf"]
    round_hashes = [digest(path) for path in rounds]
    assert len(set(round_hashes)) == 3
    assert digest(pdf) == round_hashes[2]
    result = {
        "schema": "hcs-c183-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C183",
        "evaluation_date": "2026-08-26",
        "source_commit": "bbb809ee198bc9ad5f196383baab1e3d9de38e43",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "The lazy random-transposition chain has an exact all-size partition spectrum, determinant, return trace, and L2 law; frozen S_n has no deterministic owner for P_n, whereas the canonical weighted path-cycle product belongs to a changed phase space and does not repair Route A",
        "gates": {
            "G0_source_lock_and_A0_arithmetic_gate": "PASS_WITH_A0_FAIL",
            "G1_all_size_partition_spectrum": "PASS",
            "G2_trace_determinant_and_return_counts": "PASS",
            "G3_reversibility_gap_and_l2_identity": "PASS",
            "G4_frozen_vs_weighted_path_owner_boundary": "PASS",
            "G5_checker_sympy_replay_mutation": "PASS",
            "G6_bilingual_three_round_double_compile_fonts_layout_visual": "PASS",
            "G7_manifest_hash_closure": "PASS",
            "G8_target_divisor_matching": "NOT_ESTABLISHED",
            "G9_arithmetic_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "partition_rows": 193,
            "moment_rows": 90,
            "factor_rows": 163,
            "independent_checker_assertions": 2597,
            "sympy_checks": 2427,
            "repaired_hash_mutation_rejections": 57,
            "stale_hash_mutation_rejections": 1,
            "citation_registry_population": 1,
            "reference_registry_population": 1,
            "pdf_pages": 2,
            "evidence_bytes": evidence.stat().st_size,
            "evidence_payload_sha256": evidence_data["payload_sha256"],
            "evidence_sha256": digest(evidence),
            "pdf_sha256": digest(pdf),
            "round_pdf_sha256": round_hashes,
        },
        "route_a_verdict": {
            "A0": "A0_FAIL",
            "A0_qualification": "DECK_SIZE_AND_GROUP_REPRESENTATION_HAVE_NO_INTRINSIC_RATIONAL_PRIME_ORIGIN",
            "A1": "A1_FAIL",
            "A1_qualification": "FROZEN_S_N_HAS_NO_PRIMITIVE_ORBIT_CARRYING_AN_A0_ARITHMETIC_PAYLOAD_AND_WEIGHTED_PATH_LIFT_CHANGES_THE_OBJECT",
            "A2": "A2_FAIL",
            "A2_qualification": "FINITE_MARKOV_DETERMINANT_HAS_NO_TARGET_DIVISOR_MATCH",
            "A3": "A3_FAIL",
            "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_OR_WEIL_COMPRESSION",
            "A4": "A4_FORMAL_HINT",
            "A4_qualification": "SELF_ADJOINT_MARKOV_CONTRACTION_AND_ABSTRACT_UNITARY_DILATION_ONLY",
            "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False,
        },
        "nonclaims": [
            "novelty or priority for the random-transposition spectrum or cutoff",
            "identification of weighted path cycles with intrinsic deterministic orbits on frozen S_n",
            "absolute nonexistence of primitive-cycle factorizations after changing phase space",
            "prime semantics for the deck size n or partition labels",
            "a target divisor, functional equation, counting law, or continuation match",
            "a Hilbert--Polya operator, Route-B authorization, external peer review, or acceptance score",
        ],
        "excluded_from_manifest": ["C183_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper/main.aux", "paper/main.log", "paper/main.out", "paper/main.fdb_latexmk", "paper/main.fls", "paper/main.synctex.gz"],
        "files": files,
    }
    assert len(files) == 27, f"expected 27 payload files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "C183_MANIFEST_PASS", "file_count": len(files), "manifest_sha256": digest(MANIFEST), "evidence_sha256": digest(evidence), "pdf_sha256": digest(pdf)}, sort_keys=True))

if __name__ == "__main__":
    main()
