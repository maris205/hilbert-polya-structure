#!/usr/bin/env python3
"""Create the content-addressed C115 pre-freeze release ledger."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
MANIFEST = PROJECT / "C115_RELEASE_MANIFEST.json"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    excluded = {
        MANIFEST,
        PROJECT / "paper/main.aux",
        PROJECT / "paper/main.log",
        PROJECT / "paper/main.out",
        PROJECT / "paper/main.fdb_latexmk",
        PROJECT / "paper/main.fls",
        PROJECT / "paper/main.synctex.gz",
    }
    files: dict[str, str] = {}
    for path in sorted(PROJECT.rglob("*")):
        if not path.is_file() or path in excluded or "__pycache__" in path.parts:
            continue
        files[str(path.relative_to(PROJECT))] = digest(path)

    evidence = PROJECT / "results/c115_mcmillan_evidence.json"
    pdf = PROJECT / "paper/main.pdf"
    result = {
        "schema": "hcs-c115-release-v1",
        "status": "PREFREEZE_COMPLETE_NOT_RELEASED",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "Exact birational, invariant, pole-exclusion, and low-period certificates for a rational McMillan map",
        "gates": {
            "G0_rational_model_parameter_and_domain_freeze": "PASS",
            "G1_inverse_reversor_jacobian_and_integral_identities": "PASS",
            "G2_fixed_locus_period_two_and_pole_exclusion": "PASS",
            "G3_local_monodromy_and_control_polynomials": "PASS",
            "G4_independent_checker_and_sympy_crosscheck": "PASS",
            "G5_isolated_replay_and_hostile_mutation_audit": "PASS",
            "G6_paper_double_isolated_compile_and_font_check": "PASS",
            "G7_manifest_hash_closure": "PASS",
            "G8_complete_orbit_atlas_or_level_set_dynamics": "NOT_ESTABLISHED",
            "G9_transfer_or_fredholm_owner": "NOT_ESTABLISHED",
            "G10_arithmetic_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "valid_fixed_points_over_C": 3,
            "real_fixed_points": 1,
            "primitive_real_period_two_orbits": 1,
            "excluded_cleared_denominator_roots": 2,
            "independent_checker_assertions": 66,
            "sympy_crosschecks": 23,
            "mutation_rejections": 12,
            "pdf_pages": 2,
            "evidence_sha256": digest(evidence),
            "pdf_sha256": digest(pdf),
        },
        "route_a_verdict": {
            "A1": "A1_PARTIAL_CERTIFIED",
            "A1_qualification": "EXACT_BIRATIONAL_IDENTITIES_AND_VALIDATED_LOW_PERIOD_RATIONAL_WITNESSES_ONLY",
            "A2": "A2_FAIL",
            "A2_qualification": "NO_TRANSFER_OPERATOR_OR_FINITE_TRANSFER_OWNER_CONSTRUCTED",
            "A3": "A3_NOT_ADDRESSED",
            "A4": "A4_FAIL",
            "overall": "ROUTE_A_EXPLORATORY",
        },
        "nonclaims": [
            "complete real or complex orbit atlas, entropy, integrability classification, or global level-set dynamics",
            "transfer operator, finite transfer owner, Fredholm determinant, nuclearity, analytic continuation, or zero-count theorem",
            "arithmetic/local data, Euler factors, root numbers, automorphy",
            "Hilbert--Polya operator, Riemann-zero correspondence, or Route-B authorization",
        ],
        "excluded_from_manifest": [
            "C115_RELEASE_MANIFEST.json",
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
    print(json.dumps({"manifest_sha256": digest(MANIFEST), "file_count": len(files), "evidence_sha256": digest(evidence), "pdf_sha256": digest(pdf)}, sort_keys=True))


if __name__ == "__main__":
    main()
