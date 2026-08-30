#!/usr/bin/env python3
"""Assemble the P25 Stage-4.5 Schema-5 integrity handoff.

The semantic findings live in the recorded Phase A--E audits.  This builder
checks their byte bindings and closed counts, then embeds the complete
persisted Phase-E evidence-row population in the machine handoff.  It does not
apply the proposed bibliography patch or mutate any manuscript/result file.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
PROJECT = ROOT / "papers" / "25-three-disk-scattering-flow"
NOTES = PROJECT / "notes"
PAPER = PROJECT / "paper"
OUTPUT = NOTES / "stage4_5_integrity_report.json"
TIMESTAMP = "2026-08-30T12:39:43Z"


EXPECTED_HASHES = {
    NOTES / "stage4_revision_round1.tex": "39a643c05b4820b782e45a5ec240caa7223ad444229e8a89bdcc98791ce23835",
    PAPER / "manuscript.tex": "283695c485a2a48abfab1ef0fe3d479f597f68f3082e20f4a5a1894ca37baefb",
    PAPER / "references.bib": "de776cc0bf16e6c837917f4a289f8c07b8b4f7e9146183b9a9e0e6294db99e6b",
    NOTES / "stage4_revision_evidence_bundle.json": "bf368e5757d30bf182eca18fe574814ecc11e750f5060b528bd1022b68b9fd51",
    NOTES / "stage4_5_input_manifest.json": "1e920cc6593fba373f5aa8e158bc0a292d5c0fd59a51f9cfb5c0b22fba6bc0e3",
    NOTES / "stage4_5_claim_registry.json": "9e333277db2225c1e9d68afadb1c55acdb7845a28a72cb896aca8bef0cd8b90b",
    NOTES / "stage4_5_claim_registry_coverage.json": "d8f9343806bbf42846f204a45a04ad4c7c07ae2eb7af3d5779da0d8b3cf61098",
    NOTES / "stage4_5_evidence_rows.json": "752504e737d4162dff1e189c878f4c1492054207cbd36752dfc6ff86cacce146",
    NOTES / "stage4_5_evidence_source_map.json": "2134ef5b70b85d93882a6d9616c7e2d4e9e45566186525b245b096ecfe9bd711",
    NOTES / "stage4_5_claim_strength_drift_findings.json": "f618185110e7264805743072b4f866eb85db1b4eced4e50ed9f755a4572bc644",
    NOTES / "stage4_5_reference_citation_audit.md": "891a027ca49c7e8fbab8244ed4abc8f98630a7ca41b872e814ddb42f44f647b7",
    NOTES / "stage4_5_phase_c_internal_consistency_audit.md": "7265849d0ad465ec0847cff8e69d600c5815904cdc63afe719292657c2f158bf",
    NOTES / "stage4_5_originality_failure_mode_audit.md": "52a8364c4fc5f4020bc8e6a3c2d941a57dcd47b42eda0a73b2a3e751c1775567",
    NOTES / "stage4_5_route_crosswalk.md": "f07c7936dfe4d4f6bbc0850fa4a5ad6b311819ffd40ac1050886dc6d8b8f28ac",
    NOTES / "stage4_5_compliance_report.json": "3873ec3b2b46c5f0079144c7aba8aecb251336d015ebaf3da89bbd8aa1324154",
    NOTES / "stage4_5_e6_semantic_audit.md": "c383b0f1f9b47ebc89e6b7351b32fcd25389189d2bacd2351dd435e3a5c85316",
    NOTES / "stage4_5_integrity_correction_list.json": "f25c80eae179acd0f50d948447000f775575a0c962ea9de3627c87d6d9c217c7",
    NOTES / "stage4_5_integrity_patch_round1.json": "c135b935ff154a9dd946f1bb9652e514ebae0cf82dc7894149a2b6872bc0cffc",
    NOTES / "STAGE4_5_INTEGRITY_CORRECTION_AUTHORIZATION_REQUEST.md": "72743007c76cff3079252f00ba23c64b4aa810f095b743c37552ed7e5567243e",
    NOTES / "stage4_5_material_passport.json": "f261c7a68d3b669301195950499fa6c92920078044984837fe2410fe7f171a6e",
    ROOT / "skills" / "route-a-evaluator.md": "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c",
    ROOT / "skills" / "route-b-evaluator.md": "170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def display_path(path: Path) -> str:
    return str(path.relative_to(ROOT))


def main() -> None:
    for path, expected in EXPECTED_HASHES.items():
        actual = sha256(path)
        if actual != expected:
            raise ValueError(f"stale binding: {display_path(path)}: {actual} != {expected}")

    registry = load_json(NOTES / "stage4_5_claim_registry.json")
    coverage = load_json(NOTES / "stage4_5_claim_registry_coverage.json")
    rows = load_json(NOTES / "stage4_5_evidence_rows.json")
    source_map = load_json(NOTES / "stage4_5_evidence_source_map.json")
    drift = load_json(NOTES / "stage4_5_claim_strength_drift_findings.json")
    correction_list = load_json(NOTES / "stage4_5_integrity_correction_list.json")

    claims = registry["claims"]
    claim_ids = {claim["claim_id"] for claim in claims}
    evidence_claim_ids = {row["claim"]["claim_id"] for row in rows}
    if len(claims) != 114 or any(claim["selection_tier"] != "ALL" for claim in claims):
        raise ValueError("Stage-4.5 registry must contain 114 ALL claims")
    if len(rows) != 127 or claim_ids != evidence_claim_ids:
        raise ValueError("evidence rows must contain 127 rows covering all 114 claims")
    if any(row["verdict"] != "VERIFIED" for row in rows):
        raise ValueError("all persisted Phase-E evidence rows must be VERIFIED")
    if any(row["excerpt"]["state"] != "agent_extracted" for row in rows):
        raise ValueError("all persisted Phase-E evidence rows must be source-bound")
    if len(source_map) != 9:
        raise ValueError("source-map population drifted")
    if coverage["candidate_unregistered_count"] != 0:
        raise ValueError("mechanical candidate gap count drifted")
    if coverage["registry_claim_count"] != 114:
        raise ValueError("coverage registry count drifted")
    if coverage["semantic_extraction_coverage"] != "not_machine_detectable":
        raise ValueError("semantic extraction boundary drifted")
    if drift["status"] != "completed" or drift["findings"]:
        raise ValueError("E6 companion is not the recorded completed empty finding set")
    if len(correction_list["issues"]) != 4:
        raise ValueError("integrity correction population drifted")

    reference_issues = [
        {
            "ref_id": "GaspardRice1989Semiclassical",
            "issue_type": "published_erratum_disclosure",
            "severity": "MINOR",
            "detail": "Add the published erratum DOI 10.1063/1.457672 to bibliography block B0001; the supported manuscript context does not require a claim rewrite.",
        },
        {
            "ref_id": "GaspardRice1989Exact",
            "issue_type": "published_erratum_disclosure",
            "severity": "MINOR",
            "detail": "Add the published erratum DOI 10.1063/1.457670 to bibliography block B0002; the supported manuscript contexts do not require a claim rewrite.",
        },
        {
            "ref_id": "Ruelle1976",
            "issue_type": "bibliographic_metadata_precision",
            "severity": "MINOR",
            "detail": "Add publisher-record issue number 3 to bibliography block B0006.",
        },
        {
            "ref_id": "Livsic1972",
            "issue_type": "author_metadata_normalization",
            "severity": "MINOR",
            "detail": "Normalize the author field to the authoritative initials form Livsic, A. N. in bibliography block B0008.",
        },
    ]

    report = {
        "verdict": "PASS_WITH_CONDITIONS",
        "mode": "final-check",
        "phases": {
            "A_references": {
                "checked": 8,
                "passed": 8,
                "failed": 0,
                "issues": reference_issues,
            },
            "B_citation_context": {
                "sampled": 13,
                "verified": 13,
                "issues": [],
            },
            "C_data": {
                "claims_checked": 18,
                "verified": 18,
                "issues": [],
            },
            "D_originality": {
                "checked": True,
                "issues": [],
            },
            "E_claims": {
                "checked": 114,
                "verified": 114,
                "distortions": [],
                "claim_registry_coverage": {
                    "status": "completed",
                    "registry_schema_version": "claim-registry/1.0",
                    "report_path": "notes/stage4_5_claim_registry_coverage.json",
                    "report_sha256": EXPECTED_HASHES[NOTES / "stage4_5_claim_registry_coverage.json"],
                    "draft_raw_sha256": EXPECTED_HASHES[NOTES / "stage4_revision_round1.tex"],
                    "registry_raw_sha256": EXPECTED_HASHES[NOTES / "stage4_5_claim_registry.json"],
                    "candidate_unregistered_count": 0,
                    "semantic_extraction_coverage": "not_machine_detectable",
                },
                "evidence_rows": rows,
                "claim_strength_drift_findings": {
                    "schema_version": "claim-strength-drift-findings/1.0",
                    "artifact_path": "notes/stage4_5_claim_strength_drift_findings.json",
                    "artifact_sha256": EXPECTED_HASHES[NOTES / "stage4_5_claim_strength_drift_findings.json"],
                },
            },
        },
        "overall_issues": {"SERIOUS": 0, "MEDIUM": 0, "MINOR": 4},
        "citation_integrity_score": 1.0,
        "fabrication_risk_score": 0.0,
        "timestamp": TIMESTAMP,
        "extensions": {
            "display_verdict": "HOLD FOR EXACT MINOR BIBLIOGRAPHY CORRECTIONS",
            "score_boundary": "Scores summarize the checked registered surfaces; they are not probabilities or guarantees of mathematical correctness, semantic extraction completeness, experiment design adequacy, or global originality.",
            "phase_A_B_detail": {
                "references": "8/8 existence and identity verified",
                "citation_contexts": "13/13 supported",
                "distorted_or_unverifiable_contexts": 0,
                "serious_or_medium_issues": 0,
                "minor_metadata_or_update_disclosure_issues": 4,
            },
            "phase_C_detail": {
                "statistical_and_data_families": 8,
                "internal_consistency_families": 18,
                "internal_consistency_passed": 18,
                "figures": 0,
                "tables": 2,
                "tables_traced": 2,
                "experiment_declarations_checked": 1,
                "experiment_backed_claims": 6,
                "experiment_alignment_results": "6/6 ALIGNED",
                "fresh_stage4_tests": "75/75 PASS",
                "locked_artifacts": 68,
                "canonical_results_refreshed": False,
            },
            "phase_D_detail": {
                "body_paragraph_denominator": 74,
                "sampled": 45,
                "sampling_rate": 0.608,
                "revised_body_paragraphs_checked": "17/17",
                "modified_declarations_checked": "all current declaration paragraphs",
                "title_byline_affiliation_metadata_checked": True,
                "grades": {
                    "ORIGINAL_NO_INDEXED_EXACT_MATCH": 38,
                    "COMMON_KNOWLEDGE": 7,
                    "PARAPHRASE": 0,
                    "CLOSE_MATCH": 0,
                    "VERBATIM": 0,
                },
                "self_reuse": "INSUFFICIENT_EVIDENCE_FOR_GLOBAL_CLEAN; no actionable signal in the searchable author-linked subset",
                "boundary": "Bounded public-Web heuristic screen; not professional similarity software and not a reliable global-overlap percentage.",
            },
            "phase_E_detail": {
                "registry_population": "114/114 ALL claims",
                "mechanical_candidates": 5,
                "mechanical_candidate_exact_matches": "5/5",
                "source_bound_evidence_rows": 127,
                "anchorless_evidence_rows": 0,
                "E4_scope_conformance_advisories": [],
                "E6_semantic_result": "none detected by the recorded model-mediated semantic review",
                "E6_disposition_required": False,
                "token_conservation_advisories": 4,
                "boundary": "E6 is semantic and non-deterministic; an empty finding set is not a completeness certificate or an overall Stage-4.5 PASS.",
            },
            "failure_modes": {
                "mode_1": "CLEAR_AFTER_REPLAY",
                "mode_2": "CLEAR_CONTEXT_WITH_MINOR_METADATA_HOLD",
                "mode_3": "CLEAR_AFTER_DECLARATION_AND_REPLAY",
                "mode_4": "CLEAR_WITH_SCOPE_BOUNDARY",
                "mode_5": "CLEAR",
                "mode_6": "CLEAR_FOR_DECLARED_FINITE_REPLAY",
                "mode_7": "INSUFFICIENT_EVIDENCE_WARNING",
                "suspected_count": 0,
                "gate_effect": "WARN_NOT_BLOCK; four independent bibliography MINORs keep Stage 5 closed",
            },
            "compliance": {
                "artifact_path": "notes/stage4_5_compliance_report.json",
                "artifact_sha256": EXPECTED_HASHES[NOTES / "stage4_5_compliance_report.json"],
                "schema_validation": "PASS",
                "overall_decision": "warn",
                "boundary": "RAISE principles-only extension to primary research; not official RAISE compliance and not the independent Stage-4.5 hold.",
            },
            "correction_control": {
                "correction_list_path": "notes/stage4_5_integrity_correction_list.json",
                "correction_list_sha256": EXPECTED_HASHES[NOTES / "stage4_5_integrity_correction_list.json"],
                "proposed_patch_path": "notes/stage4_5_integrity_patch_round1.json",
                "proposed_patch_sha256": EXPECTED_HASHES[NOTES / "stage4_5_integrity_patch_round1.json"],
                "authorization_request_path": "notes/STAGE4_5_INTEGRITY_CORRECTION_AUTHORIZATION_REQUEST.md",
                "authorization_request_sha256": EXPECTED_HASHES[NOTES / "STAGE4_5_INTEGRITY_CORRECTION_AUTHORIZATION_REQUEST.md"],
                "patch_authorized": False,
                "patch_applied": False,
                "manuscript_claim_rewrite_required": False,
            },
            "checkpoint": {
                "stage4_5_audit": "COMPLETE",
                "stage5_entry": "CLOSED_ZERO_ISSUE_BOUNDARY",
                "reason": "Four MINOR bibliography controls remain open and no exact correction authority has been supplied.",
            },
            "cross_model": "NOT_CONFIGURED_AND_NOT_AUTHORIZED",
            "route_crosswalk": {
                "artifact_path": "notes/stage4_5_route_crosswalk.md",
                "artifact_sha256": EXPECTED_HASHES[NOTES / "stage4_5_route_crosswalk.md"],
                "route_a_sha256": EXPECTED_HASHES[ROOT / "skills" / "route-a-evaluator.md"],
                "route_b_sha256": EXPECTED_HASHES[ROOT / "skills" / "route-b-evaluator.md"],
                "symbolic_calibrator_tuple": [
                    "A0_FAIL",
                    "A1_PASS_ANALYTIC",
                    "A2_ANALYTIC_DETERMINANT",
                    "A3_FAIL",
                    "A4_FAIL",
                ],
                "symbolic_calibrator_overall": "ROUTE_A_REJECTED",
                "physical_flow_tuple": "UNASSIGNED",
                "route_b": "UNINVOKED",
                "gate_credit": "NONE",
            },
            "input_manifest": {
                "artifact_path": "notes/stage4_5_input_manifest.json",
                "artifact_sha256": EXPECTED_HASHES[NOTES / "stage4_5_input_manifest.json"],
            },
            "material_passport": {
                "artifact_path": "notes/stage4_5_material_passport.json",
                "artifact_sha256": EXPECTED_HASHES[NOTES / "stage4_5_material_passport.json"],
                "verification_status": "UNVERIFIED",
                "boundary": "Open MINOR corrections prevent an integrity pass date; the passport records the audit hold without promoting Stage 5.",
            },
        },
    }

    OUTPUT.write_text(
        json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {OUTPUT}")
    print(f"sha256 {sha256(OUTPUT)}")
    print("Schema-5 counts: A 8/8 + 4 MINOR; B 13/13; C 18/18; D 45/74; E 114/114, 127 rows")


if __name__ == "__main__":
    main()
