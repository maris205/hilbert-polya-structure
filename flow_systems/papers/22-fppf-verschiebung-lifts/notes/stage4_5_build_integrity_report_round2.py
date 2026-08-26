#!/usr/bin/env python3
"""Assemble the P22 Stage-4.5 Round-2 zero-issue Schema-5 handoff.

Semantic judgments live in the separately recorded audit carriers. This
builder checks their exact byte bindings and closed counts, then embeds the
persisted Phase-E evidence rows in the machine handoff.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


PROJECT = Path(__file__).resolve().parent.parent
NOTES = PROJECT / "notes"
PAPER = PROJECT / "paper"
REPOSITORY = PROJECT.parents[1]
OUTPUT = NOTES / "stage4_5_round2_integrity_report.json"
TIMESTAMP = "2026-08-25T15:18:43Z"


EXPECTED_HASHES = {
    PAPER / "manuscript.tex": "e90dd88109d4e53d1f789808286c15cc917003cd38b69f49ddaff8661b9158ed",
    PAPER / "paper.pdf": "20e2d14f5a9e46b7d4f5eafac6669032c72fc69367fdf902e54440816a4a3f04",
    PAPER / "references.bib": "bd03813691db911316b18620ee4a1d212ac284fce7fb79af9f1b1cbc7ea71093",
    NOTES / "stage4_5_integrity_revision_round2.tex": "a93b64f5ad41ede0ddaef8ad6fa46800092a9abd5d75fb099d357b54ea2058a2",
    NOTES / "stage4_5_integrity_revision_patch_round2.json": "421e969a54bcd5a783faeab1485605533e4465bd8b7e4289cdf522de0770ebc0",
    NOTES / "stage4_5_integrity_authorization_round2.json": "01bedd0142b6942f1df5f21ef2c15af0a87cef2e89d3152f86f095a4666fc60b",
    NOTES / "stage4_5_integrity_revision_round2.tex.apply-report.json": "88c2becd2a644537d3ba356f2b97eb9d3eecca00fdbab93713d02226e1b51765",
    NOTES / "stage4_5_revision_evidence_bundle_round2.json": "c665cee2e8c2288fb2c8e17a0e7e7e935b8062813a42d67cc8cea892ed6c10a9",
    NOTES / "stage4_5_round2_input_manifest.json": "d9769b23a0597d6472652b8564867dafcea0788380bc73d93d71e963121ea7d8",
    NOTES / "stage4_5_round2_claim_registry.json": "eddfa08f0b9d8f9e1b0b6c9433d28da7ffef078b886b77b0c29f44055955b240",
    NOTES / "stage4_5_round2_evidence_rows.json": "1f0d696a8988aebd0b00924c30c1dd8ec12a70b6a5ce7ffbd2156c38192ded1a",
    NOTES / "stage4_5_round2_claim_registry_coverage.json": "6ad28465bfd126a748440957389f01264ef1546956bf09c81cc3caaee302c749",
    NOTES / "stage4_5_round2_claim_registry_coverage_adjudication.md": "491502d67255dbecaff5ae9090ff889ac01669406d86470a557aac2174af37c7",
    NOTES / "stage4_5_round2_claim_strength_drift_findings.json": "9f3e7795831e2086686d6f527b51c117d6d73afbccd2453685e1df30b652e982",
    NOTES / "stage4_5_round2_reference_citation_audit.md": "c389dcf60077c3ccde4f4e92f0463ef574964b4ae43e2a214e9c6cf04ffb616a",
    NOTES / "stage4_5_round2_phase_c_internal_consistency_audit.md": "388afc5c29ddf3b13d25163a15553c660367db46e805f0963fa9c90fce774e56",
    NOTES / "stage4_5_round2_originality_failure_mode_audit.md": "b212e5c5cf877d4d7d4f0726a08e072bfe615115b298ae7171055025aa914bed",
    NOTES / "stage4_5_round2_compliance_report.json": "a34c4a2009b855fbbcef69d460ccf7abe1fab4feb854af5fcfa8ea552e0970e6",
    NOTES / "stage4_5_round2_e6_semantic_audit.md": "c8f4de2bd76e6cd30607047b4976229705e299910a47cae17fdb2d6da7c33150",
    NOTES / "stage4_5_round2_route_crosswalk.md": "67a7a4abf8a5c425b19cf679c3bd5d0d0348e6c6632f51738a269d98b80cae5b",
    REPOSITORY / "skills/route-a-evaluator.md": "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c",
    REPOSITORY / "skills/route-b-evaluator.md": "170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def relative(path: Path) -> str:
    try:
        return str(path.relative_to(PROJECT))
    except ValueError:
        return str(path.relative_to(REPOSITORY))


def main() -> None:
    for path, expected in EXPECTED_HASHES.items():
        actual = sha256(path)
        if actual != expected:
            raise ValueError(f"stale binding: {relative(path)}: {actual} != {expected}")

    public_text = (PAPER / "manuscript.tex").read_text(encoding="utf-8")
    anchored_text = (NOTES / "stage4_5_integrity_revision_round2.tex").read_text(
        encoding="utf-8"
    )
    projected = "".join(
        line
        for line in anchored_text.splitlines(keepends=True)
        if not line.startswith("<!--block:")
    )
    if projected != public_text:
        raise ValueError("public manuscript is not the exact marker-stripped anchored draft")
    if "Draft of 24 August 2026" in public_text:
        raise ValueError("old draft date remains")
    if "public-access status must be confirmed" in public_text:
        raise ValueError("old materials deferral remains")
    if public_text.count("available from the author upon reasonable request") != 1:
        raise ValueError("Round-2 materials policy must occur exactly once")

    registry = load_json(NOTES / "stage4_5_round2_claim_registry.json")
    rows = load_json(NOTES / "stage4_5_round2_evidence_rows.json")
    coverage = load_json(NOTES / "stage4_5_round2_claim_registry_coverage.json")
    drift = load_json(NOTES / "stage4_5_round2_claim_strength_drift_findings.json")
    compliance = load_json(NOTES / "stage4_5_round2_compliance_report.json")
    authorization = load_json(NOTES / "stage4_5_integrity_authorization_round2.json")
    apply_report = load_json(
        NOTES / "stage4_5_integrity_revision_round2.tex.apply-report.json"
    )

    claims = registry["claims"]
    claim_ids = {row["claim_id"] for row in claims}
    evidence_claim_ids = {row["claim"]["claim_id"] for row in rows}
    if len(claims) != 49 or any(row["selection_tier"] != "ALL" for row in claims):
        raise ValueError("Round-2 registry must contain 49 ALL claims")
    if len(rows) != 63 or claim_ids != evidence_claim_ids:
        raise ValueError("evidence rows must contain 63 rows covering all 49 claims")
    if any(row["verdict"] != "VERIFIED" for row in rows):
        raise ValueError("all persisted Phase-E evidence rows must be VERIFIED")
    if coverage["candidate_unregistered_count"] != 6:
        raise ValueError("coverage receipt raw lexical-candidate count drifted")
    if coverage["semantic_extraction_coverage"] != "not_machine_detectable":
        raise ValueError("semantic coverage boundary drifted")
    if drift["status"] != "completed" or drift["findings"]:
        raise ValueError("E6 companion is not the completed empty finding set")
    if drift["final_draft_sha256"] != EXPECTED_HASHES[NOTES / "stage4_5_integrity_revision_round2.tex"]:
        raise ValueError("E6 final-draft binding drifted")
    if drift["revision_evidence_bundle_sha256"] != EXPECTED_HASHES[NOTES / "stage4_5_revision_evidence_bundle_round2.json"]:
        raise ValueError("E6 bundle binding drifted")
    if compliance["overall_decision"] != "warn":
        raise ValueError("primary-research compliance advisory must remain warn")
    if authorization["revision_patch_sha256"] != EXPECTED_HASHES[NOTES / "stage4_5_integrity_revision_patch_round2.json"]:
        raise ValueError("authorization patch binding drifted")
    if apply_report["authorization_witness"]["status"] != "pass":
        raise ValueError("integrity-correction authorization witness is not pass")

    report = {
        "verdict": "PASS",
        "mode": "final-check",
        "phases": {
            "A_references": {
                "checked": 3,
                "passed": 3,
                "failed": 0,
                "issues": [],
            },
            "B_citation_context": {
                "sampled": 21,
                "verified": 21,
                "issues": [],
            },
            "C_data": {
                "claims_checked": 16,
                "verified": 16,
                "issues": [],
            },
            "D_originality": {
                "checked": True,
                "issues": [],
            },
            "E_claims": {
                "checked": 49,
                "verified": 49,
                "distortions": [],
                "claim_registry_coverage": {
                    "status": "completed",
                    "registry_schema_version": "claim-registry/1.0",
                    "report_path": "notes/stage4_5_round2_claim_registry_coverage.json",
                    "report_sha256": EXPECTED_HASHES[NOTES / "stage4_5_round2_claim_registry_coverage.json"],
                    "adjudication_path": "notes/stage4_5_round2_claim_registry_coverage_adjudication.md",
                    "adjudication_sha256": EXPECTED_HASHES[NOTES / "stage4_5_round2_claim_registry_coverage_adjudication.md"],
                    "draft_raw_sha256": EXPECTED_HASHES[PAPER / "manuscript.tex"],
                    "registry_raw_sha256": EXPECTED_HASHES[NOTES / "stage4_5_round2_claim_registry.json"],
                    "candidate_unregistered_count": 6,
                    "candidate_unregistered_disposition": "6/6 adjudicated lexical false positives",
                    "semantic_extraction_coverage": "not_machine_detectable",
                },
                "evidence_rows": rows,
                "claim_strength_drift_findings": {
                    "schema_version": "claim-strength-drift-findings/1.0",
                    "artifact_path": "notes/stage4_5_round2_claim_strength_drift_findings.json",
                    "artifact_sha256": EXPECTED_HASHES[NOTES / "stage4_5_round2_claim_strength_drift_findings.json"],
                },
            },
        },
        "overall_issues": {"SERIOUS": 0, "MEDIUM": 0, "MINOR": 0},
        "citation_integrity_score": 1.0,
        "fabrication_risk_score": 0.0,
        "timestamp": TIMESTAMP,
        "extensions": {
            "display_verdict": "PASS",
            "score_boundary": "Scores summarize checked registered surfaces; they are not probabilities or guarantees of mathematical correctness, semantic-extraction completeness, corpus completeness, or global originality.",
            "phase_C_detail": {
                "statistical_data_surfaces": 0,
                "internal_consistency_families": 16,
                "internal_consistency_passed": 16,
                "figures": 0,
                "tables": 0,
                "experiment_declarations_checked": 1,
                "experiment_backed_claims": 0,
                "experiment_alignment_results": [],
            },
            "phase_D_detail": {
                "body_paragraph_denominator": 74,
                "sampled": 37,
                "sampling_rate": 0.5,
                "round2_changed_surfaces_checked": "2/2",
                "grades": {
                    "ORIGINAL": 29,
                    "COMMON_KNOWLEDGE": 8,
                    "PARAPHRASE": 0,
                    "CLOSE_MATCH": 0,
                    "VERBATIM": 0,
                },
                "disposition": "PASS_WITH_LIMITATIONS",
                "self_reuse": "INSUFFICIENT_EVIDENCE_FOR_CLEAN; no actionable signal in the reliably email-linked public subset",
            },
            "phase_E_detail": {
                "E4_scope_conformance_advisories": [],
                "E5_novelty_classification": "SUPPORTED_WITHIN_SEARCH; bounded negative observation, not global priority",
                "E6_semantic_result": "none detected by the recorded semantic review",
                "E6_disposition_required": False,
                "continuous_bundle_rounds": 2,
                "continuous_bundle_operations": 15,
                "token_conservation_advisories": 5,
            },
            "failure_modes": {
                "mode_1": "CLEAR_BY_NON_APPLICABILITY",
                "mode_2": "CLEAR_AFTER_INTEGRATED_FRESH_PHASE_A_B",
                "mode_3": "CLEAR_BY_NON_APPLICABILITY",
                "mode_4": "CLEAR_BY_NON_APPLICABILITY",
                "mode_5": "CLEAR_BY_NON_APPLICABILITY",
                "mode_6": "CLEAR_BY_NON_APPLICABILITY",
                "mode_7": "INSUFFICIENT_EVIDENCE_WARNING",
                "suspected_count": 0,
                "gate_effect": "WARN_NOT_BLOCK",
            },
            "compliance": {
                "artifact_path": "notes/stage4_5_round2_compliance_report.json",
                "artifact_sha256": EXPECTED_HASHES[NOTES / "stage4_5_round2_compliance_report.json"],
                "schema_validation": "PASS",
                "overall_decision": "warn",
                "boundary": "RAISE principles-only extension to primary research; not official RAISE compliance and not a Stage-4.5 hard block.",
            },
            "frozen_stage3_prime_issues": [
                {"new_issue_id": "NEW-1", "integrity_id": "IL-MINOR-1", "status": "closed_verified"},
                {"new_issue_id": "NEW-2", "integrity_id": "IL-MINOR-2", "status": "closed_verified"},
            ],
            "revision_authority": {
                "patch_sha256": EXPECTED_HASHES[NOTES / "stage4_5_integrity_revision_patch_round2.json"],
                "authorization_sha256": EXPECTED_HASHES[NOTES / "stage4_5_integrity_authorization_round2.json"],
                "apply_report_sha256": EXPECTED_HASHES[NOTES / "stage4_5_integrity_revision_round2.tex.apply-report.json"],
                "revision_evidence_bundle_sha256": EXPECTED_HASHES[NOTES / "stage4_5_revision_evidence_bundle_round2.json"],
                "authorized_targets": ["IL-MINOR-1:B0005/replace_block", "IL-MINOR-2:B0094/replace_block"],
            },
            "checkpoint": {
                "stage4_5_audit": "COMPLETE_ZERO_ISSUE_PASS",
                "zero_issue_boundary": "MET",
                "stage5_entry": "READY_FOR_MANDATORY_ADVISORY_SEQUENCE_AND_EXPLICIT_USER_CONFIRMATION",
                "reason": "SERIOUS=0, MEDIUM=0, MINOR=0; Stage 5 remains unentered pending #660 then #672 and explicit user confirmation.",
            },
            "cross_model": "NOT_CONFIGURED_AND_NOT_AUTHORIZED",
            "route_crosswalk": {
                "artifact_path": "notes/stage4_5_round2_route_crosswalk.md",
                "artifact_sha256": EXPECTED_HASHES[NOTES / "stage4_5_round2_route_crosswalk.md"],
                "route_a_sha256": EXPECTED_HASHES[REPOSITORY / "skills/route-a-evaluator.md"],
                "route_b_sha256": EXPECTED_HASHES[REPOSITORY / "skills/route-b-evaluator.md"],
                "route_a": "NOT_TESTABLE",
                "route_b": "NOT_TESTABLE",
                "gate_credit": "NONE",
            },
            "input_manifest": {
                "artifact_path": "notes/stage4_5_round2_input_manifest.json",
                "artifact_sha256": EXPECTED_HASHES[NOTES / "stage4_5_round2_input_manifest.json"],
            },
        },
    }

    OUTPUT.write_text(
        json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {OUTPUT}")
    print(f"sha256 {sha256(OUTPUT)}")
    print("Schema-5 counts: A 3/3; B 21/21; C 16/16; D 37/74; E 49/49, 63 rows; issues 0/0/0")


if __name__ == "__main__":
    main()
