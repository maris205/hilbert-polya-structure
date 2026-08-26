#!/usr/bin/env python3
"""Assemble the P22 Stage-4.5 Schema-5 integrity handoff.

The semantic findings are produced by the recorded audits.  This builder only
checks their byte bindings, reconciles their closed counts, and embeds the full
persisted Phase-E evidence-row array in the final machine handoff.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


PROJECT = Path(__file__).resolve().parent.parent
NOTES = PROJECT / "notes"
PAPER = PROJECT / "paper"
OUTPUT = NOTES / "stage4_5_integrity_report.json"
TIMESTAMP = "2026-08-25T11:56:46Z"


EXPECTED_HASHES = {
    PAPER / "manuscript.tex": "2e8a6872eabb512dbd7ef04f5be933717a472c931199b9be509cb654599d4da2",
    PAPER / "paper.pdf": "0ed4af9ef021876efafedf7b2457e3f371cfeb953b82c1773bcea20d8490cb8b",
    PAPER / "references.bib": "bd03813691db911316b18620ee4a1d212ac284fce7fb79af9f1b1cbc7ea71093",
    NOTES / "stage4_revision_round1.tex": "663ade71e41de81afd376db516ed8f548af3090cf342dd4db052eb212ce3c2d2",
    NOTES / "stage4_revision_evidence_bundle.json": "763f9e3cc12a8115f02a0d315dc9c74415448676c341a20e80cc0d292006f0ff",
    NOTES / "stage4_5_input_manifest.json": "7139194b137f40fbd4184b2f494fa78aeda5d3f6b146e799b96756ae2b79a7f4",
    NOTES / "stage4_5_claim_registry.json": "b5a62ee06844eff8c5f5aeec6fb73090cef998373d73c64917cd9f237cb81954",
    NOTES / "stage4_5_evidence_rows.json": "492412e025acf88ffbbe44f78379b936e8e0281c35cf5e54f717f610975fa3df",
    NOTES / "stage4_5_claim_registry_coverage.json": "7da7d0b6c1f1f4696928f6789fda818cac1b75266b253aa0d53d48779b9f0bee",
    NOTES / "stage4_5_claim_strength_drift_findings.json": "87dbff3aa4cd7533b18bd26f05bd665cd6dfe875573537a02e2fe0f8b8e797a8",
    NOTES / "stage4_5_reference_citation_audit.md": "fc9ec5b4275710f9dbb95cfa1f153ceaec52414903cf43314ccd745eb7b7d2d7",
    NOTES / "stage4_5_phase_c_internal_consistency_audit.md": "9c3e1e72d032c20aec956b3b0173a49807bc0d946275111c5f496fb0be6a9617",
    NOTES / "stage4_5_originality_failure_mode_audit.md": "e679078b7ac18ac35b25aa4b3d439f0171bdf014ce3193401e6e71f84bc02b4f",
    NOTES / "stage4_5_compliance_report.json": "1dfd3a71cd164de62057c504e080c5f2be94543cfcfe2e8ac26aff3a4dca4835",
    NOTES / "stage4_5_e6_semantic_audit.md": "4295e2cecc1f540eb1ce34fe8337769d446e8d8c984b441f7a37eb8324db5a99",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def relative(path: Path) -> str:
    return str(path.relative_to(PROJECT))


def main() -> None:
    for path, expected in EXPECTED_HASHES.items():
        actual = sha256(path)
        if actual != expected:
            raise ValueError(f"stale binding: {relative(path)}: {actual} != {expected}")

    registry = load_json(NOTES / "stage4_5_claim_registry.json")
    rows = load_json(NOTES / "stage4_5_evidence_rows.json")
    coverage = load_json(NOTES / "stage4_5_claim_registry_coverage.json")
    drift = load_json(NOTES / "stage4_5_claim_strength_drift_findings.json")

    claims = registry["claims"]
    claim_ids = {row["claim_id"] for row in claims}
    evidence_claim_ids = {row["claim"]["claim_id"] for row in rows}
    if len(claims) != 49 or any(row["selection_tier"] != "ALL" for row in claims):
        raise ValueError("Stage-4.5 registry must contain 49 ALL rows")
    if len(rows) != 63 or claim_ids != evidence_claim_ids:
        raise ValueError("evidence rows must contain 63 rows covering all 49 claims")
    if any(row["verdict"] != "VERIFIED" for row in rows):
        raise ValueError("all persisted Phase-E evidence rows must be VERIFIED")
    if coverage["candidate_unregistered_count"] != 6:
        raise ValueError("coverage receipt raw candidate gap count drifted")
    if coverage["semantic_extraction_coverage"] != "not_machine_detectable":
        raise ValueError("semantic coverage boundary drifted")
    if drift["status"] != "completed" or drift["findings"]:
        raise ValueError("E6 companion is not the recorded completed empty finding set")

    report = {
        "verdict": "PASS_WITH_CONDITIONS",
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
                "verified": 14,
                "issues": [
                    {
                        "claim": "Draft chronology",
                        "expected": "The displayed draft chronology does not predate an update included in that draft, or the chronology is explicitly explained.",
                        "actual": "The title block says Draft of 24 August 2026 while the included bounded update says it was completed on 25 August 2026.",
                        "severity": "MINOR",
                    },
                    {
                        "claim": "Materials availability",
                        "expected": "The author supplies a final public-access decision before dissemination.",
                        "actual": "The declaration still says that public-access status must be confirmed by the author before dissemination.",
                        "severity": "MINOR",
                    },
                ],
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
                    "report_path": "notes/stage4_5_claim_registry_coverage.json",
                    "report_sha256": EXPECTED_HASHES[NOTES / "stage4_5_claim_registry_coverage.json"],
                    "draft_raw_sha256": EXPECTED_HASHES[PAPER / "manuscript.tex"],
                    "registry_raw_sha256": EXPECTED_HASHES[NOTES / "stage4_5_claim_registry.json"],
                    "candidate_unregistered_count": 6,
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
        "overall_issues": {"SERIOUS": 0, "MEDIUM": 0, "MINOR": 2},
        "citation_integrity_score": 1.0,
        "fabrication_risk_score": 0.0,
        "timestamp": TIMESTAMP,
        "extensions": {
            "display_verdict": "PASS WITH NOTES",
            "score_boundary": "Scores summarize the checked registered surfaces; they are not probabilities or guarantees of mathematical correctness, extraction completeness, or global originality.",
            "phase_C_detail": {
                "statistical_data_surfaces": 0,
                "internal_consistency_families": 16,
                "internal_consistency_passed": 14,
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
                "revised_body_paragraphs_checked": "12/12",
                "revised_declarations_checked": "3/3",
                "revised_title_byline_metadata_checked": "1/1",
                "grades": {
                    "ORIGINAL": 29,
                    "COMMON_KNOWLEDGE": 8,
                    "PARAPHRASE": 0,
                    "CLOSE_MATCH": 0,
                    "VERBATIM": 0,
                },
                "self_reuse": "INSUFFICIENT_EVIDENCE_FOR_CLEAN; no actionable signal in the reliably linked public subset",
            },
            "phase_E_detail": {
                "E4_scope_conformance_advisories": [],
                "E5_novelty_classification": "SUPPORTED_WITHIN_SEARCH; bounded negative observation, not global priority",
                "E6_semantic_result": "none detected by the recorded semantic review",
                "E6_disposition_required": False,
                "token_conservation_advisories": 4,
            },
            "failure_modes": {
                "mode_1": "CLEAR",
                "mode_2": "CLEAR_AFTER_INTEGRATED_FRESH_PHASE_A_B",
                "mode_3": "CLEAR",
                "mode_4": "CLEAR",
                "mode_5": "CLEAR",
                "mode_6": "CLEAR",
                "mode_7": "INSUFFICIENT_EVIDENCE_WARNING",
                "suspected_count": 0,
                "gate_effect": "WARN_NOT_BLOCK",
            },
            "compliance": {
                "artifact_path": "notes/stage4_5_compliance_report.json",
                "artifact_sha256": EXPECTED_HASHES[NOTES / "stage4_5_compliance_report.json"],
                "schema_validation": "PASS",
                "overall_decision": "warn",
                "boundary": "RAISE principles-only extension to primary research; not official RAISE compliance and not a Stage-4.5 hard block.",
            },
            "frozen_stage3_prime_issues": [
                {"new_issue_id": "NEW-1", "integrity_id": "IL-MINOR-1", "status": "open"},
                {"new_issue_id": "NEW-2", "integrity_id": "IL-MINOR-2", "status": "open"},
            ],
            "checkpoint": {
                "stage4_5_audit": "COMPLETE",
                "stage5_entry": "CLOSED_ZERO_ISSUE_BOUNDARY",
                "reason": "Two MINOR issues remain open and no manuscript correction was authorized.",
            },
            "cross_model": "NOT_CONFIGURED_AND_NOT_AUTHORIZED",
            "route_crosswalk": {
                "route_a_sha256": "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c",
                "route_b_sha256": "170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595",
                "route_a": "NOT_TESTABLE",
                "route_b": "NOT_TESTABLE",
                "gate_credit": "NONE",
            },
            "input_manifest": {
                "artifact_path": "notes/stage4_5_input_manifest.json",
                "artifact_sha256": EXPECTED_HASHES[NOTES / "stage4_5_input_manifest.json"],
            },
        },
    }

    OUTPUT.write_text(
        json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {OUTPUT}")
    print(f"sha256 {sha256(OUTPUT)}")
    print("Schema-5 counts: A 3/3; B 21/21; C 14/16 + 2 MINOR; D 37/74; E 49/49, 63 rows")


if __name__ == "__main__":
    main()
