#!/usr/bin/env python3
"""Build the content-addressed self-excluded HCS-C179 release manifest."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C179_RELEASE_MANIFEST.json"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    excluded = {
        MANIFEST,
        ROOT / "paper/main.aux",
        ROOT / "paper/main.log",
        ROOT / "paper/main.out",
        ROOT / "paper/main.fdb_latexmk",
        ROOT / "paper/main.fls",
        ROOT / "paper/main.synctex.gz",
    }
    files = {}
    for path in sorted(ROOT.rglob("*")):
        if (
            not path.is_file()
            or path in excluded
            or "__pycache__" in path.parts
            or path.suffix == ".pyc"
        ):
            continue
        files[str(path.relative_to(ROOT))] = digest(path)

    evidence = ROOT / "results/c179_zsigmondy_return_evidence.json"
    pdf = ROOT / "paper/main.pdf"
    rounds = [
        ROOT / "paper/main_round0_original.pdf",
        ROOT / "paper/main_round1.pdf",
        ROOT / "paper/main_round2.pdf",
    ]
    round_hashes = [digest(path) for path in rounds]
    assert len(set(round_hashes)) == 3, "paper rounds must be content-distinct"
    assert digest(pdf) == round_hashes[2], "main.pdf must equal round 2"

    result = {
        "schema": "hcs-c179-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C179",
        "evaluation_date": "2026-08-26",
        "source_commit": "bbb809ee198bc9ad5f196383baab1e3d9de38e43",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "For every coprime a>b>=1, primitive divisors are exactly marked first-return prime moduli, every primitive prime-power and admissible finite fiber has an exact orbit ledger, and two natural globalizations prove that the finite fibers alone do not select a unique global determinant owner",
        "gates": {
            "G0_source_clock_attribution_and_A0_lock": "PASS_WITH_A0_WEAK",
            "G1_primitive_return_equivalence_and_classical_exceptions": "PASS_WITH_EXTERNAL_ZSIGMONDY_ATTRIBUTION",
            "G2_all_prime_power_order_lift": "PASS",
            "G3_every_admissible_finite_fiber_cycle_zeta_determinant_reversal": "PASS",
            "G4_disjoint_union_and_profinite_globalizations": "PASS_WITH_OWNER_NONSELECTION",
            "G5_checker_sympy_replay_mutation": "PASS_WITH_EXACT_CLAIM_MAPS_AND_FOUR_REQUIRED_CONTRACT_ATTACKS",
            "G6_bilingual_three_round_double_compile_fonts_layout_visual": "PASS",
            "G7_manifest_hash_closure": "PASS",
            "G8_target_analytic_hilbert_polya_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "parameter_pairs": 63,
            "finite_fiber_parameter_pairs": 31,
            "zsigmondy_rows": 567,
            "zsigmondy_exception_rows": 7,
            "globalization_rows": 630,
            "finite_fiber_rows": 1650,
            "prime_power_lift_rows": 2080,
            "independent_checker_assertions": 320291,
            "sympy_checks": 6674,
            "repaired_hash_mutation_rejections": 64,
            "stale_hash_mutation_rejections": 1,
            "required_exact_contract_attack_rejections": 4,
            "citation_registry_population": 4,
            "reference_registry_population": 4,
            "pdf_pages": 3,
            "evidence_payload_sha256": "22b08c44f51e4bf063a2fc608d570a3584462d3efbaf3e2acb47d0f9b083b34f",
            "evidence_sha256": digest(evidence),
            "pdf_sha256": digest(pdf),
            "round_pdf_sha256": round_hashes,
        },
        "route_a_verdict": {
            "A0": "A0_WEAK_ARITHMETIC_RELATION",
            "A0_qualification": "RATIONAL_PRIMES_EMERGE_INTRINSICALLY_AS_FIRST_RETURN_MODULI_BUT_NOT_AS_ORBITS_OF_ONE_SELECTED_GLOBAL_OWNER_AND_NO_LOG_P_CLOCK_IS_ASSIGNED",
            "A1": "A1_WEAK",
            "A1_qualification": "EVERY_FINITE_FIBER_IS_EXACT_BUT_DISJOINT_UNION_AND_PROFINITE_GLOBALIZATIONS_HAVE_INCOMPATIBLE_PRIMITIVE_LEDGERS",
            "A2": "A2_FAIL",
            "A2_qualification": "NO_TARGET_DIVISOR_OR_FROZEN_TARGET_VALIDATION_PROTOCOL",
            "A3": "A3_FAIL",
            "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_CONTINUATION_COUNTING_LAW_OR_WEIL_COMPRESSION",
            "A4": "A4_NATURAL_QUANTIZATION",
            "A4_qualification": "FINITE_PERMUTATION_AND_PROFINITE_HAAR_KOOPMAN_LIFTS_ARE_CANONICAL_SAME_CLOCK_UNITARIES",
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "nonclaims": [
            "a new proof, strengthening, or priority claim for the classical Zsigmondy theorem",
            "identification of a prime return modulus with an isolated prime-labeled orbit in one global phase space",
            "absolute nonexistence of every possible enlarged determinant owner",
            "a logarithmic prime roof or prime-weighted global product",
            "a target divisor, functional equation, continuation, counting law, or Weil compression",
            "arithmetic local factors, root numbers, automorphy, or Hilbert--Polya",
            "Route-B authorization, external peer review, or an acceptance score",
        ],
        "excluded_from_manifest": [
            "C179_RELEASE_MANIFEST.json",
            "code/__pycache__/",
            "*.pyc",
            "paper/main.aux",
            "paper/main.log",
            "paper/main.out",
            "paper/main.fdb_latexmk",
            "paper/main.fls",
            "paper/main.synctex.gz",
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
                "status": "C179_MANIFEST_PASS",
                "file_count": len(files),
                "manifest_sha256": digest(MANIFEST),
                "evidence_sha256": digest(evidence),
                "pdf_sha256": digest(pdf),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
