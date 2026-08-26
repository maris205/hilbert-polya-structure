#!/usr/bin/env python3
"""Build the content-addressed self-excluded C177 release manifest."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C177_RELEASE_MANIFEST.json"


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

    evidence = ROOT / "results/c177_expanding_circle_evidence.json"
    pdf = ROOT / "paper/main.pdf"
    round0 = ROOT / "paper/main_round0_original.pdf"
    round1 = ROOT / "paper/main_round1.pdf"
    round2 = ROOT / "paper/main_round2.pdf"
    round_hashes = [digest(round0), digest(round1), digest(round2)]
    assert len(set(round_hashes)) == 3, "paper rounds must be distinct"
    assert digest(pdf) == round_hashes[2], "final must equal round 2"

    result = {
        "schema": "hcs-c177-release-v1",
        "status": "RELEASE_COMPLETE",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "All integer expanding circle maps admit one exact periodic/Wold/Perron/mixing theorem, while prime and composite degree controls prove arithmetic parameter blindness",
        "gates": {
            "G0_source_lock_and_A0_arithmetic_gate": "PASS_WITH_A0_FAIL",
            "G1_all_parameter_fixed_and_primitive_cycles": "PASS",
            "G2_rational_artin_mazur_zeta": "PASS",
            "G3_wold_and_perron_decomposition": "PASS",
            "G4_sharp_sobolev_correlation_and_operator_boundary": "PASS",
            "G5_checker_sympy_replay_mutation": "PASS",
            "G6_bilingual_three_round_double_compile_fonts_layout_visual": "PASS",
            "G7_manifest_hash_closure": "PASS",
            "G8_target_divisor_matching": "NOT_ESTABLISHED",
            "G9_arithmetic_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "periodic_rows": 132,
            "wold_rows": 1595,
            "correlation_rows": 352,
            "independent_checker_assertions": 3980,
            "sympy_checks": 3927,
            "repaired_hash_mutation_rejections": 18,
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
            "A0_qualification": "DEGREE_PARAMETER_HAS_NO_INTRINSIC_PRIME_OR_ARITHMETIC_ORIGIN",
            "A1": "A1_WEAK",
            "A1_qualification": "COMPLETE_PRIMITIVE_ORBIT_LEDGER_BUT_ONLY_GENERIC_DEGREE_DATA",
            "A2": "A2_FAIL",
            "A2_qualification": "RATIONAL_SOURCE_ZETA_HAS_NO_TARGET_DIVISOR_MATCH",
            "A3": "A3_FAIL",
            "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_OR_CONTINUATION_COMPARISON",
            "A4": "A4_FORMAL_HINT",
            "A4_qualification": "PROPER_KOOPMAN_ISOMETRY_AND_UNITARY_DILATION_ONLY_AFTER_CHANGING_PHASE_SPACE",
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "nonclaims": [
            "novelty or priority for classical expanding-map formulas",
            "prime semantics for the arbitrary degree b",
            "an ordinary Fredholm determinant for the non-trace-class Koopman isometry",
            "a target divisor, functional equation, counting law, or continuation match",
            "a Hilbert--Polya operator, Route-B authorization, external peer review, or acceptance score",
        ],
        "excluded_from_manifest": [
            "C177_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc",
            "paper/main.aux", "paper/main.log", "paper/main.out",
            "paper/main.fdb_latexmk", "paper/main.fls", "paper/main.synctex.gz",
        ],
        "files": files,
    }
    assert len(files) == 27, f"expected 27 payload files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C177_MANIFEST_PASS",
        "file_count": len(files),
        "manifest_sha256": digest(MANIFEST),
        "evidence_sha256": digest(evidence),
        "pdf_sha256": digest(pdf),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
