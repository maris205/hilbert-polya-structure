#!/usr/bin/env python3
"""Build the content-addressed C121 pre-freeze release ledger."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C121_RELEASE_MANIFEST.json"


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
    files: dict[str, str] = {}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path in excluded or "__pycache__" in path.parts:
            continue
        files[str(path.relative_to(ROOT))] = digest(path)
    evidence = ROOT / "results/c121_projective_evidence.json"
    pdf = ROOT / "paper/main.pdf"
    result = {
        "schema": "hcs-c121-release-v1",
        "status": "PREFREEZE_COMPLETE_NOT_RELEASED",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "Algebraic stability and exact degree growth for a quadratic Hénon automorphism",
        "gates": {
            "G0_affine_and_projective_map_freeze": "PASS",
            "G1_birational_inverse_and_indeterminacy_certificate": "PASS",
            "G2_algebraic_stability_and_all_order_degree_theorem": "PASS",
            "G3_fixed_points_two_cycle_and_monodromy": "PASS",
            "G4_independent_checker_sympy_replay_and_controls": "PASS",
            "G5_hostile_mutation_audit": "PASS",
            "G6_paper_double_isolated_compile_and_font_check": "PASS",
            "G7_manifest_hash_closure": "PASS",
            "G8_prime_like_correspondence_complete_atlas_target_divisor_or_transfer_owner": "NOT_ESTABLISHED",
            "G9_analytic_bridge_entropy_arithmetic_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "maximum_replayed_iterate": 8,
            "largest_replayed_degree": 256,
            "dynamical_degree": "2",
            "fixed_point_count": 2,
            "primitive_two_cycle_count_certified": 1,
            "mutation_rejections": 16,
            "pdf_pages": 2,
            "evidence_sha256": digest(evidence),
            "pdf_sha256": digest(pdf),
        },
        "route_a_verdict": {
            "evaluator": "henon_dynamics/skills/route-a-evaluator.md",
            "canonical_tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "canonical_tuple_text": "(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)",
            "A1": "A1_WEAK",
            "A1_qualification": "EXACT_STRUCTURAL_EVIDENCE_ONLY_NO_PRIME_LIKE_TARGET_CORRESPONDENCE_OR_COMPLETE_ATLAS",
            "A2": "A2_FAIL",
            "A2_qualification": "NO_WEIGHTED_DYNAMICAL_ZETA_TRANSFER_OWNER_OR_TARGET_DIVISOR_TEST",
            "A3": "A3_FAIL",
            "A3_qualification": "NO_FUNCTIONAL_EQUATION_GAMMA_FACTOR_COUNTING_LAW_CONTINUATION_OR_ANALYTIC_BRIDGE",
            "A4": "A4_FAIL",
            "overall": "ROUTE_A_EXPLORATORY",
        },
        "nonclaims": [
            "complete periodic-orbit classification or complete primitive-orbit atlas",
            "prime-like target correspondence, log-prime clock, or target-amplitude law",
            "target divisor, weighted dynamical zeta, or determinant matching",
            "topological or metric entropy equality from the algebraic dynamical degree",
            "transfer-operator owner, invariant function space, nuclearity, or Fredholm determinant",
            "analytic bridge, functional equation, Gamma factor, trivial-zero treatment, counting law, or continuation",
            "arithmetic/local data, Euler factors, root numbers, or automorphy",
            "Hilbert--Polya operator, Riemann-zero correspondence, or Route-B authorization",
        ],
        "excluded_from_manifest": [
            "C121_RELEASE_MANIFEST.json",
            "code/__pycache__/",
            "paper/main.aux",
            "paper/main.log",
            "paper/main.out",
            "paper/main.fdb_latexmk",
            "paper/main.fls",
            "paper/main.synctex.gz",
        ],
        "files": files,
    }
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(
        json.dumps(
            {
                "manifest_sha256": digest(MANIFEST),
                "file_count": len(files),
                "evidence_sha256": digest(evidence),
                "pdf_sha256": digest(pdf),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
