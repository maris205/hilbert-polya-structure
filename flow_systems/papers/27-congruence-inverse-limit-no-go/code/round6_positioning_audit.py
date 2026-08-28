#!/usr/bin/env python3
"""Build the P27 Round-6 compact/cusped positioning contract.

The mathematical proofs remain in the human-readable notes.  This executable
serializes the frozen claim/source matrix, verifies its conservative novelty
labels and three-way go/no-go decision, and preserves the Route owner firewall.
It performs no network access and never emits USER_ATTESTED_READ.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path
from typing import Sequence


DATE = "2026-08-28"
HUMAN_PENDING = "HUMAN_CONFIRMATION_PENDING"
FORMAL_TUPLE = (
    "(A0_WEAK_ARITHMETIC_RELATION,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)"
)

FIELDS = (
    "claim_id",
    "claim_category",
    "claim_text",
    "support_class",
    "source_id",
    "source_title",
    "primary_url",
    "alternate_url",
    "exact_locator",
    "access_date",
    "verification_status",
    "human_confirmation_status",
    "domain_caveat",
    "novelty_consequence",
    "evidence_token",
)


CLAIM_ROWS = (
    {
        "claim_id": "P27-S1-FLOW",
        "claim_category": "DIRECT_STRUCTURAL_PRIOR",
        "claim_text": "The laminated geodesic flow is defined leafwise and restricts to the ordinary geodesic flow on each hyperbolic leaf.",
        "support_class": "PRIMARY_SOURCE_TECHNICAL",
        "source_id": "S1",
        "source_title": "Horocycle flows for laminations by hyperbolic Riemann surfaces and Hedlund's theorem",
        "primary_url": "https://arxiv.org/pdf/0711.2307",
        "alternate_url": "https://www.aimsciences.org/article/doi/10.3934/jmd.2016.10.113",
        "exact_locator": "arXiv:0711.2307v4, pp.2-3, Section 2.2; PDF lines 138-183 in the verified web extraction",
        "access_date": DATE,
        "verification_status": "PRIMARY_SOURCE_WEB_VERIFIED",
        "human_confirmation_status": HUMAN_PENDING,
        "domain_caveat": "Compact laminated setting; used for flow definition, not as proof of the noncompact P27 theorem.",
        "novelty_consequence": "OBJECT_AND_FLOW_FRAMEWORK_IS_PRIOR",
        "evidence_token": "PROVED_BY_SOURCE",
    },
    {
        "claim_id": "P27-S1-APERIODIC",
        "claim_category": "DIRECT_RESULT_PRIOR",
        "claim_text": "A compact hyperbolic lamination example without periodic geodesic-flow orbits already exists.",
        "support_class": "PRIMARY_SOURCE_TECHNICAL",
        "source_id": "S1",
        "source_title": "Horocycle flows for laminations by hyperbolic Riemann surfaces and Hedlund's theorem",
        "primary_url": "https://arxiv.org/pdf/0711.2307",
        "alternate_url": "https://doi.org/10.3934/jmd.2016.10.113",
        "exact_locator": "arXiv:0711.2307v4, p.12, Example 4; verified PDF lines 778-792",
        "access_date": DATE,
        "verification_status": "PRIMARY_SOURCE_WEB_VERIFIED",
        "human_confirmation_status": HUMAN_PENDING,
        "domain_caveat": "The example is not the Gamma(3 n!) tower, but it directly defeats broad aperiodicity novelty.",
        "novelty_consequence": "BROAD_APERIODICITY_NOVELTY_REJECTED",
        "evidence_token": "PROVED_BY_SOURCE",
    },
    {
        "claim_id": "P27-S1-UNIVERSAL",
        "claim_category": "DIRECT_STRUCTURAL_PRIOR",
        "claim_text": "The universal hyperbolic solenoid is a compact inverse-limit lamination with simply connected leaves.",
        "support_class": "PRIMARY_SOURCE_TECHNICAL",
        "source_id": "S1",
        "source_title": "Horocycle flows for laminations by hyperbolic Riemann surfaces and Hedlund's theorem",
        "primary_url": "https://arxiv.org/pdf/0711.2307",
        "alternate_url": "https://arxiv.org/abs/0711.2307",
        "exact_locator": "arXiv:0711.2307v4, pp.15-16, Example 6; verified PDF lines 923-930 and following",
        "access_date": DATE,
        "verification_status": "PRIMARY_SOURCE_WEB_VERIFIED",
        "human_confirmation_status": HUMAN_PENDING,
        "domain_caveat": "Compact universal solenoid, not the noncompact factorial congruence chain.",
        "novelty_consequence": "SIMPLY_CONNECTED_LEAF_MECHANISM_IS_PRIOR",
        "evidence_token": "PROVED_BY_SOURCE",
    },
    {
        "claim_id": "P27-S2-PUNCTURED",
        "claim_category": "CLOSEST_NONCOMPACT_STRUCTURAL_PRIOR",
        "claim_text": "The punctured solenoid is the noncompact inverse limit over finite-index modular covers and its leaves are dense unit disks.",
        "support_class": "PRIMARY_SOURCE_TECHNICAL",
        "source_id": "S2",
        "source_title": "Teichmuller theory of the punctured solenoid",
        "primary_url": "https://arxiv.org/pdf/math/0508476",
        "alternate_url": "https://doi.org/10.1007/s10711-007-9226-9",
        "exact_locator": "Introduction pp.1-2 and Section 2, Definition 2.1 with following discussion; verified web extraction lines 20-22 and 91-110",
        "access_date": DATE,
        "verification_status": "PRIMARY_SOURCE_WEB_VERIFIED",
        "human_confirmation_status": HUMAN_PENDING,
        "domain_caveat": "Directed system of all finite covers; not the one frozen Gamma(3 n!) chain and not a period-owner audit.",
        "novelty_consequence": "NONCOMPACT_MODULAR_SOLENOID_STRUCTURE_IS_PRIOR",
        "evidence_token": "PROVED_BY_SOURCE",
    },
    {
        "claim_id": "P27-S3-FLOW",
        "claim_category": "OBJECT_TAXONOMY_PRIOR",
        "claim_text": "A hyperbolic solenoidal geodesic flow acts leafwise on the unit tangent bundle.",
        "support_class": "PRIMARY_SOURCE_TECHNICAL",
        "source_id": "S3",
        "source_title": "Horocyclic trajectories in hyperbolic solenoidal surfaces of finite type",
        "primary_url": "https://arxiv.org/pdf/2411.18418",
        "alternate_url": "https://ems.press/journals/ggd/articles/14299725",
        "exact_locator": "arXiv:2411.18418v2, p.7, Definition 4; verified PDF lines 401-408",
        "access_date": DATE,
        "verification_status": "PRIMARY_SOURCE_WEB_VERIFIED",
        "human_confirmation_status": HUMAN_PENDING,
        "domain_caveat": "Source definitions support taxonomy; P27's no-period proof remains local.",
        "novelty_consequence": "LEAFWISE_FLOW_TAXONOMY_IS_PRIOR",
        "evidence_token": "PROVED_BY_SOURCE",
    },
    {
        "claim_id": "P27-S3-FINITE-TYPE",
        "claim_category": "OBJECT_TAXONOMY_PRIOR",
        "claim_text": "Noncompact finite-area inverse limits of finite covers form the hyperbolic-solenoidal finite-type object class used by P27.",
        "support_class": "PRIMARY_SOURCE_TECHNICAL",
        "source_id": "S3",
        "source_title": "Horocyclic trajectories in hyperbolic solenoidal surfaces of finite type",
        "primary_url": "https://arxiv.org/pdf/2411.18418",
        "alternate_url": "https://doi.org/10.4171/GGD/967",
        "exact_locator": "arXiv:2411.18418v2, p.8 Definition 5 and pp.13-14 Section 4 setup; verified PDF lines 429-441 and 738-768",
        "access_date": DATE,
        "verification_status": "PRIMARY_SOURCE_WEB_VERIFIED",
        "human_confirmation_status": HUMAN_PENDING,
        "domain_caveat": "The paper studies horocycle dynamics and does not state P27's Gamma(3 n!) geodesic-period proposition.",
        "novelty_consequence": "NONCOMPACT_FINITE_TYPE_OBJECT_CLASS_IS_PRIOR",
        "evidence_token": "PROVED_BY_SOURCE",
    },
    {
        "claim_id": "P27-S3-MCCORD",
        "claim_category": "OBJECT_TAXONOMY_PRIOR",
        "claim_text": "Inverse limits of finite regular covers are McCord solenoids; normal subgroup towers give the regular-cover case.",
        "support_class": "PRIMARY_SOURCE_TECHNICAL",
        "source_id": "S3",
        "source_title": "Horocyclic trajectories in hyperbolic solenoidal surfaces of finite type",
        "primary_url": "https://arxiv.org/pdf/2411.18418",
        "alternate_url": "https://ems.press/journals/ggd/articles/14299725",
        "exact_locator": "arXiv:2411.18418v2, pp.12-14, Section 3.3, Definition 7 and tower setup; verified PDF lines 655-680 and 740-751",
        "access_date": DATE,
        "verification_status": "PRIMARY_SOURCE_WEB_VERIFIED",
        "human_confirmation_status": HUMAN_PENDING,
        "domain_caveat": "Taxonomic support only; no finite-owner firewall or exact factorial-chain theorem is attributed to the source.",
        "novelty_consequence": "MCCORD_AND_REGULAR_TOWER_TERMINOLOGY_IS_PRIOR",
        "evidence_token": "PROVED_BY_SOURCE",
    },
    {
        "claim_id": "P27-S4-KERNEL",
        "claim_category": "GROUP_CHAIN_STRUCTURAL_PRIOR",
        "claim_text": "The kernel of a group chain is its subgroup intersection and is naturally identified with the fundamental group of the corresponding leaf.",
        "support_class": "PRIMARY_SOURCE_TECHNICAL",
        "source_id": "S4",
        "source_title": "Wild solenoids",
        "primary_url": "https://arxiv.org/pdf/1702.03032",
        "alternate_url": "https://doi.org/10.1090/tran/7339",
        "exact_locator": "arXiv:1702.03032, p.17, Definition 5.5 and following paragraph; verified PDF lines 1168-1194",
        "access_date": DATE,
        "verification_status": "PRIMARY_SOURCE_WEB_VERIFIED",
        "human_confirmation_status": HUMAN_PENDING,
        "domain_caveat": "Weak-solenoid setup has a closed compact base; it is comparison evidence, not a substitute for P27's noncompact proof.",
        "novelty_consequence": "GROUP_INTERSECTION_LEAF_MECHANISM_IS_PRIOR",
        "evidence_token": "PROVED_BY_SOURCE",
    },
    {
        "claim_id": "P27-S5-MALCEV",
        "claim_category": "STANDARD_THEOREM_SOURCE",
        "claim_text": "Finitely generated linear groups are residually finite (Malcev's theorem).",
        "support_class": "PRIMARY_EXPOSITORY_SOURCE",
        "source_id": "S5",
        "source_title": "Linear groups - Malcev's theorem and Selberg's lemma",
        "primary_url": "https://arxiv.org/abs/1306.2385",
        "alternate_url": "https://arxiv.org/pdf/1306.2385",
        "exact_locator": "arXiv:1306.2385v1, p.1, Introduction, displayed Theorem (Malcev 1940), with residual-finiteness definition immediately following; verified PDF lines 4-16",
        "access_date": DATE,
        "verification_status": "PRIMARY_SOURCE_WEB_VERIFIED",
        "human_confirmation_status": HUMAN_PENDING,
        "domain_caveat": "Used only for residual finiteness of the cocompact Fuchsian surface group; the P27 tower and period bound are proved locally.",
        "novelty_consequence": "RESIDUAL_FINITE_INPUT_IS_STANDARD",
        "evidence_token": "PROVED_BY_SOURCE",
    },
    {
        "claim_id": "P27-LOCAL-COMMON",
        "claim_category": "LOCAL_COMPARISON_THEOREM",
        "claim_text": "For a torsion-free Fuchsian group and a descending normal finite-index tower with trivial intersection, the coordinatewise inverse-limit geodesic flow has no periodic point and every fixed infinite-order owner's quotient orders divide forward and diverge.",
        "support_class": "LOCAL_PROOF",
        "source_id": "P27-R4-R6",
        "source_title": "P27 residual-tower common-core theorem",
        "primary_url": "notes/round4_period_escape_theorem.md",
        "alternate_url": "notes/round6_compact_cusped_positioning_audit.md",
        "exact_locator": "Round-6 common-core proposition and proof",
        "access_date": DATE,
        "verification_status": "LOCAL_PROOF_REPLAYED",
        "human_confirmation_status": "NOT_APPLICABLE_LOCAL_PROOF",
        "domain_caveat": "Elementary unifying proposition with direct structural prior; no broad first/novel claim.",
        "novelty_consequence": "COMPARATIVE_SYNTHESIS_NOT_GENERAL_APERIODICITY_NOVELTY",
        "evidence_token": "PROVED",
    },
    {
        "claim_id": "P27-LOCAL-CUSPED",
        "claim_category": "LOCAL_EXPLICIT_SPECIALIZATION",
        "claim_text": "The Gamma(3 n!) specialization has an explicit PSL-sign residual-intersection proof and exact finite quotient-order diagnostics, but the three old matrix owners lack full conjugacy-primitivity certification.",
        "support_class": "LOCAL_PROOF_AND_EXACT_LEDGER",
        "source_id": "P27-R1-R4",
        "source_title": "P27 factorial congruence specialization",
        "primary_url": "notes/stage1_research_brief.md",
        "alternate_url": "results/round4_period_escape_ledger.csv",
        "exact_locator": "Stage-1 no-go proposition and Round-4 finite-prefix theorem",
        "access_date": DATE,
        "verification_status": "LOCAL_PROOF_AND_ARTIFACT_REPLAYED",
        "human_confirmation_status": "NOT_APPLICABLE_LOCAL_PROOF",
        "domain_caveat": "Exact-chain non-hit is search-bounded; whole-g closing times are not called primitive minimal periods.",
        "novelty_consequence": "EXPLICIT_CASE_ONLY_NO_ABSOLUTE_NOVELTY",
        "evidence_token": "PROVED",
    },
    {
        "claim_id": "P27-LOCAL-CLOSED",
        "claim_category": "LOCAL_QUANTITATIVE_CONTROL",
        "claim_text": "The closed genus-2 residual/homology tower removes cusps, congruence, and arithmetic input; primitive homology gives n! dividing o_n and exact minimal lifted period T_n=o_n ell(g)>=n! ell(g).",
        "support_class": "LOCAL_PROOF_AND_EXACT_LEDGER",
        "source_id": "P27-R5",
        "source_title": "P27 closed-surface factorial control theorem",
        "primary_url": "notes/round5_cocompact_control_theorem.md",
        "alternate_url": "results/round5_cocompact_homology_escape_ledger.csv",
        "exact_locator": "Round-5 Theorems 1-2 and primitive-geodesic corollary",
        "access_date": DATE,
        "verification_status": "LOCAL_PROOF_AND_ARTIFACT_REPLAYED",
        "human_confirmation_status": "NOT_APPLICABLE_LOCAL_PROOF",
        "domain_caveat": "Full residual-core quotient orders are not computed; only exact homology lower bounds are machine replayed.",
        "novelty_consequence": "QUANTITATIVE_COMPACT_CONTROL_SUPPORTS_SHORT_METHOD_NOTE",
        "evidence_token": "PROVED",
    },
    {
        "claim_id": "P27-DECISION-THREE-WAY",
        "claim_category": "WRITTEN_GO_NO_GO",
        "claim_text": "Proceed with a short compact-versus-cusped comparative owner-audit; reject a standalone new aperiodicity theorem and reject same-owner Route-A A2 for the inverse-limit flow.",
        "support_class": "STAGE_1_POSITIONING_DECISION",
        "source_id": "P27-R6",
        "source_title": "P27 Round-6 three-way go/no-go",
        "primary_url": "notes/round6_go_no_go_decision.md",
        "alternate_url": "paper/round6_contribution_lock.md",
        "exact_locator": "Frozen three-way decision block",
        "access_date": DATE,
        "verification_status": "AUTHOR_PROJECT_DECISION_RECORDED",
        "human_confirmation_status": "HUMAN_SOURCE_LOCATOR_CONFIRMATION_PENDING",
        "domain_caveat": "Scientific positioning decision does not attest that the author personally read S1-S5.",
        "novelty_consequence": "GO_SHORT_NOTE_NO_GENERAL_NOVELTY_NO_A2",
        "evidence_token": "MODELING_CHOICE",
    },
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_rows(rows: Sequence[dict[str, str]]) -> list[str]:
    errors: list[str] = []
    expected_ids = {row["claim_id"] for row in CLAIM_ROWS}
    actual_ids = {row["claim_id"] for row in rows}
    if len(rows) != len(expected_ids) or actual_ids != expected_ids:
        errors.append("claim IDs are missing or duplicated")
    external = [row for row in rows if row["source_id"] in {"S1", "S2", "S3", "S4", "S5"}]
    for row in external:
        if not row["primary_url"].startswith("https://"):
            errors.append(f"external row lacks HTTPS primary URL: {row['claim_id']}")
        if not row["exact_locator"]:
            errors.append(f"external row lacks exact locator: {row['claim_id']}")
        if row["access_date"] != DATE:
            errors.append(f"external row has wrong access date: {row['claim_id']}")
        if row["verification_status"] != "PRIMARY_SOURCE_WEB_VERIFIED":
            errors.append(f"external row lacks primary-source verification: {row['claim_id']}")
        if row["human_confirmation_status"] != HUMAN_PENDING:
            errors.append(f"external row has invalid human status: {row['claim_id']}")
    if any("USER_ATTESTED_READ" in value for row in rows for value in row.values()):
        errors.append("forbidden USER_ATTESTED_READ token present")
    broad = next(row for row in rows if row["claim_id"] == "P27-S1-APERIODIC")
    if broad["novelty_consequence"] != "BROAD_APERIODICITY_NOVELTY_REJECTED":
        errors.append("broad aperiodicity novelty was not rejected")
    s4 = next(row for row in rows if row["claim_id"] == "P27-S4-KERNEL")
    if "closed compact base" not in s4["domain_caveat"]:
        errors.append("S4 compact-domain caveat missing")
    return errors


def write_csv(path: Path, rows: Sequence[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    rows = [dict(row) for row in CLAIM_ROWS]
    errors = validate_rows(rows)
    matrix_path = args.output_dir / "round6_claim_source_matrix.csv"
    summary_path = args.output_dir / "round6_positioning_summary.json"
    manifest_path = args.output_dir / "round6_artifact_manifest.json"
    write_csv(matrix_path, rows)

    source_rows = [row for row in rows if row["source_id"] in {"S1", "S2", "S3", "S4", "S5"}]
    summary = {
        "schema": "p27_round6_compact_cusped_positioning/1.0",
        "date": DATE,
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "claim_source_rows": len(rows),
        "primary_source_web_verified_rows": len(source_rows),
        "unique_external_primary_sources": sorted({row["source_id"] for row in source_rows}),
        "human_confirmation_pending_rows": sum(
            row["human_confirmation_status"] == HUMAN_PENDING for row in rows
        ),
        "user_attested_read_rows": 0,
        "technical_positioning": {
            "common_mechanism": (
                "DESCENDING_NORMAL_FINITE_INDEX_RESIDUAL_TOWER_PLUS_COMMON_"
                "ARCLENGTH_CLOCK_AND_OWNER_COMPATIBILITY"
            ),
            "common_inverse_limit_periodic_set": "EMPTY",
            "fixed_owner_quotient_orders": "DIVIDE_FORWARD_AND_DIVERGE",
            "cusped_specialization": (
                "EXPLICIT_GAMMA_3_FACTORIAL_PSL_SIGN_PROOF_AND_EXACT_FINITE_"
                "ORDER_DIAGNOSTIC"
            ),
            "closed_control": (
                "GENUS2_RESIDUAL_HOMOLOGY_TOWER_WITH_N_FACTORIAL_MINIMAL_"
                "PERIOD_LOWER_BOUND"
            ),
            "causal_exclusions": ["CUSP", "PRINCIPAL_CONGRUENCE", "ARITHMETIC_LATTICE"],
        },
        "closest_prior_decision": {
            "direct_structural_prior_found": True,
            "broad_aperiodicity_novelty_claim": "REJECTED",
            "absolute_novelty_claim_allowed": False,
            "exact_gamma_3_factorial_statement": "SEARCH_BOUNDED_SPECIALIZATION_ONLY",
        },
        "three_way_go_no_go": {
            "short_comparative_owner_audit": "GO",
            "standalone_new_aperiodicity_theorem": "NO_GO",
            "same_owner_route_a_a2": "NO_GO",
        },
        "human_source_gate": {
            "status": HUMAN_PENDING,
            "user_attested_read": False,
            "drafting_effect": (
                "POSITIONING_IS_FROZEN_BUT_AUTHOR_SOURCE_LOCATOR_CONFIRMATION_"
                "REMAINS_REQUIRED_BEFORE_SUBMISSION_PROSE"
            ),
        },
        "claim_boundary": {
            "ars_stage": "STAGE_1_RESEARCH",
            "proposal_stage": "STAGE_1_ROUTE_A_A0_A1",
            "formal_route_a_tuple": FORMAL_TUPLE,
            "formal_a1_verdict": "A1_FAIL",
            "a2_a4": "FAIL_NOT_TESTABLE",
            "overall_route_a_status": "ROUTE_A_REJECTED",
            "route_b_evaluation": "NOT_RUN",
            "route_b_invocation_allowed": False,
            "finite_level_to_inverse_limit_orbit_credit": "FORBIDDEN",
            "prime_or_zero_tables_used": False,
        },
    }
    summary_path.write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    manifest = {
        "schema": "p27_round6_artifact_manifest/1.0",
        "artifacts": [
            {"path": path.name, "bytes": path.stat().st_size, "sha256": sha256(path)}
            for path in (matrix_path, summary_path)
        ],
    }
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, sort_keys=True))
    return 0 if summary["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
