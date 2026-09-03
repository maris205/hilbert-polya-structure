#!/usr/bin/env python3
"""Build the exact P33 scope-expansion authorization request after scope stop."""

from __future__ import annotations

import copy
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def art(path: Path, root: Path) -> dict:
    return {"path": str(path.relative_to(root)), "sha256": sha(path), "bytes": len(path.read_bytes())}


def main() -> int:
    generated_at_utc = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    support = Path(__file__).resolve().parent
    notes = support.parent
    root = Path(__file__).resolve().parents[4]
    original_path = root / "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33.json"
    original = json.loads(original_path.read_text(encoding="utf-8"))
    paper = original["papers"][0]

    incident = notes / "stage4_prime_round5_scope_stop_incident.md"
    support_validation = notes / "stage4_prime_round5_support_validation.json"
    authority_paths = [
        original_path,
        root / "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_EXECUTION_AUTHORIZATION_RECEIPT.json",
        root / "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_EXECUTION_INPUT_FREEZE.json",
        root / "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33_VALIDATION.json",
        root / "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33_RECEIPT.json",
        support_validation,
        incident,
    ]
    support_paths = [
        notes / "stage4_prime_round5_artifact_inventory_final.json",
        notes / "stage4_prime_round5_artifact_inventory_receipt.json",
        notes / "stage4_prime_round5_correction_bibliography_prospective.json",
        notes / "stage4_prime_round5_source_identity_replay_receipt.json",
        notes / "stage4_prime_round5_source_use_locator_final.json",
        notes / "stage4_prime_round5_source_use_locator_receipt.json",
        support / "trust_graph.json",
        support / "fixture_oracle_manifest.json",
        support / "component_build_provenance.json",
        support / "producer_code_exclusion_audit.json",
        support / "synthetic_proof_registry_snapshot.json",
        support / "validate_synthetic_fixtures.py",
        support / "serialized_fixture_validation_receipt.json",
        support / "bp_enumeration_contract.json",
        support / "bp_coverage_ledger.schema.json",
        support / "cp_enumeration_contract.json",
        support / "cp_coverage_ledger.schema.json",
        support / "producer_contract_validation_receipt.json",
    ] + sorted((support / "fixtures/valid").glob("*.json")) + sorted((support / "fixtures/invalid").glob("*.json"))

    new_actions = [
        {
            "action_id": "REV-P33-SCOPE-001",
            "source": art(incident, root),
            "classification": "mandatory_scope_expansion_after_authorized_support_execution",
            "description": "Reconcile the executed 43-row commit replay, 20-source bounded identifier replay, and synthetic-only fixture conformance with the earlier blanket no-retrieval/no-fixture revision statement while retaining every scientific and production nonexecution boundary.",
            "proposed_author_triage": "will_address",
            "proposed_targets": [{
                "block_id": "B0041",
                "expected_old_hash": "597eb230d326",
                "first_line_excerpt": "No retrieval, new source, locator, quotation, experiment, or scientific computation occurred during revision.",
                "allowed_operations": ["replace_block"],
            }],
            "required_new_text_contract": [
                "state that Stage-4-prime performed only commit-pinned artifact and identifier-endpoint replay plus synthetic conformance",
                "state that no source passage was verified and no new source was added",
                "retain no geodesic, conjugacy, root, systole, owner-census, scientific experiment, or result-refresh execution",
                "distinguish the synthetic harness from an implemented production validator",
            ],
            "claim_strength_authorizations": [],
        },
        {
            "action_id": "REV-P33-SCOPE-002",
            "source": art(incident, root),
            "classification": "mandatory_scope_expansion_after_authorized_support_execution",
            "description": "Extend the AI-assistance disclosure to the authorized 4 September 2026 Stage-4-prime support work while retaining the 48-use passage-inconclusive boundary and making no source-cleanliness or method-validation claim.",
            "proposed_author_triage": "will_address",
            "proposed_targets": [{
                "block_id": "B0124",
                "expected_old_hash": "3f69d3822846",
                "first_line_excerpt": "\\paragraph{AI assistance and verification limitation.}",
                "allowed_operations": ["replace_block"],
            }],
            "required_new_text_contract": [
                "retain the 2 September 2026 workflow disclosure",
                "add the 4 September 2026 support-artifact, bounded-replay, correction-metadata, fixture, contract, and deterministic validation assistance",
                "state that the exact backend snapshot was not exposed",
                "retain that the accountable author did not attest personal full-text passage verification",
                "retain anchor=none and claim_to_passage=INCONCLUSIVE for all 48 uses",
            ],
            "claim_strength_authorizations": [],
        },
    ]

    op_results = {
        "P33-CURRENT-ARTIFACT-INVENTORY": {
            "notes_side_status": "COMPLETE_PASS_43_OF_43_PINNED_COMMIT_EXACT",
            "artifacts": [art(notes / "stage4_prime_round5_artifact_inventory_final.json", root), art(notes / "stage4_prime_round5_artifact_inventory_receipt.json", root)],
        },
        "P33-CORRECTION-BIBLIOGRAPHY": {
            "notes_side_status": "SOURCE_FINALIZED_APPEND_AND_FIVE_USE_MANUSCRIPT_BINDING_PENDING_NEW_CONFIRMATION",
            "artifacts": [art(notes / "stage4_prime_round5_correction_bibliography_prospective.json", root)],
        },
        "P33-INDEPENDENCE-PROVENANCE": {
            "notes_side_status": "COMPLETE_FAIL_CLOSED_PRODUCTION_INDEPENDENCE_NOT_ESTABLISHED",
            "artifacts": [art(support / name, root) for name in ["trust_graph.json", "fixture_oracle_manifest.json", "component_build_provenance.json", "producer_code_exclusion_audit.json"]],
        },
        "P33-SERIALIZED-FIXTURES": {
            "notes_side_status": "COMPLETE_SYNTHETIC_CONFORMANCE_ONLY_2_VALID_12_INVALID",
            "artifacts": [art(support / "synthetic_proof_registry_snapshot.json", root), art(support / "serialized_fixture_validation_receipt.json", root)],
        },
        "P33-PRODUCER-COVERAGE-CONTRACTS": {
            "notes_side_status": "COMPLETE_CONTRACT_ONLY_NO_PRODUCER_RUN",
            "artifacts": [art(support / name, root) for name in ["bp_enumeration_contract.json", "bp_coverage_ledger.schema.json", "cp_enumeration_contract.json", "cp_coverage_ledger.schema.json", "producer_contract_validation_receipt.json"]],
        },
        "P33-48-USE-PASSAGE-FINALIZATION": {
            "notes_side_status": "COMPLETE_48_ROWS_EXPLICIT_BOUNDED_UNAVAILABILITY_0_PASSAGE_LOCATORS",
            "artifacts": [art(notes / "stage4_prime_round5_source_identity_replay_receipt.json", root), art(notes / "stage4_prime_round5_source_use_locator_final.json", root), art(notes / "stage4_prime_round5_source_use_locator_receipt.json", root)],
        },
        "P33-CONSERVATIVE-CONDITIONAL-TYPING": {
            "notes_side_status": "AUDIT_COMPLETE_MANUSCRIPT_REPLACEMENTS_PENDING_NEW_CONFIRMATION",
            "artifacts": [art(notes / "stage4_prime_round5_implementation_contracts_prospective.json", root)],
        },
    }
    support_operations = copy.deepcopy(original["supporting_operations"])
    for operation in support_operations:
        operation["current_execution_result"] = op_results[operation["operation_id"]]

    item_target_pairs = [
        (item["item_id"], target["block_id"], operation)
        for item in paper["items"]
        for target in item["proposed_targets"]
        for operation in target["allowed_operations"]
    ]
    new_pairs = [
        (action["action_id"], target["block_id"], operation)
        for action in new_actions
        for target in action["proposed_targets"]
        for operation in target["allowed_operations"]
    ]
    all_pairs = item_target_pairs + new_pairs
    unique_pairs = sorted({(block, operation) for _, block, operation in all_pairs})

    request = {
        "schema_version": "round10-stage4-prime-p33-scope-expansion-authorization-request/1.0",
        "generated_at_utc": generated_at_utc,
        "workflow_date": "2026-09-04",
        "status": "AWAITING_EXPLICIT_AUTHOR_CONFIRMATION",
        "paper_id": "P33",
        "authority_bindings": [art(path, root) for path in authority_paths],
        "scope_stop": {
            "status": "TRIGGERED_BEFORE_BIBLIOGRAPHY_OR_PATCH_WRITE",
            "incident": art(incident, root),
            "reason": "Authorized support work makes B0041 and B0124 stale, but neither target occurs in the original 35-pair request.",
        },
        "superseded_scope_attempt1": {
            "status": "NONCONTROLLING_SUPERSEDED_DUE_TO_UNLISTED_TARGETS",
            "artifacts": [art(notes / name, root) for name in [
                "stage4_prime_round5_revision_roadmap.json",
                "stage4_prime_round5_author_choices.json",
                "stage4_prime_round5_claim_surface_manifest.json",
                "stage4_prime_round5_author_adjudication.json",
            ]],
            "may_be_used_for_apply": False,
        },
        "frozen_inputs": {
            "base_draft": art(notes / "stage4_revision_round1.tex", root),
            "block_manifest": art(notes / "stage4_prime_round5_base.block-manifest.json", root),
            "bibliography": art(root / "papers/33-bolza-control-matched-census/paper/references.bib", root),
            "canonical_manuscript": art(root / "papers/33-bolza-control-matched-census/paper/manuscript.tex", root),
            "canonical_pdf": art(root / "papers/33-bolza-control-matched-census/paper/paper.pdf", root),
            "claim_surface_manifest": art(notes / "stage4_claim_surface_manifest.json", root),
            "initial_system": art(notes / "stage1_prestart_brief.md", root),
            "route_crosswalk": art(notes / "stage4_route_crosswalk.md", root),
        },
        "carried_forward_exact_request": {
            "request": art(original_path, root),
            "items": copy.deepcopy(paper["items"]),
            "item_target_mappings": len(item_target_pairs),
            "unique_block_operation_pairs": len({(b, op) for _, b, op in item_target_pairs}),
            "semantic_or_operation_scope_change": False,
        },
        "new_issue_actions": new_actions,
        "supporting_operations": support_operations,
        "support_artifact_manifest": [art(path, root) for path in support_paths],
        "counts": {
            "carried_residual_items": len(paper["items"]),
            "carried_item_target_mappings": len(item_target_pairs),
            "carried_unique_block_operation_pairs": len({(b, op) for _, b, op in item_target_pairs}),
            "new_issue_actions": len(new_actions),
            "new_issue_target_mappings": len(new_pairs),
            "total_mapped_pairs_with_item_or_action_provenance": len(all_pairs),
            "total_unique_block_operation_pairs": len(unique_pairs),
            "replace_block_pairs": sum(op == "replace_block" for _, op in unique_pairs),
            "supporting_operations": len(support_operations),
            "artifact_inventory_rows": 43,
            "source_use_rows": 48,
            "distinct_sources": 20,
            "exact_passage_locators": 0,
            "explicit_bounded_unavailability_rows": 48,
            "valid_synthetic_fixtures": 2,
            "invalid_synthetic_fixtures": 12,
            "production_components_available": 0,
        },
        "requested_next_execution": {
            "fresh_successor_authority_chain_required": True,
            "emit_patch_format": "1.1",
            "patch_ops": 37,
            "operation": "replace_block",
            "append_bibliography_keys_exactly": ["P33-S03-CORR", "P33-S16-CORR"],
            "bind_affected_uses": ["P33-U08", "P33-U22", "P33-U27", "P33-U28", "P33-U37"],
            "apply_to_new_draft_only": "papers/33-bolza-control-matched-census/notes/stage4_prime_revision_round2.tex",
            "build_notes_side_pdf_only": "papers/33-bolza-control-matched-census/notes/stage4_prime_revision_round2.pdf",
            "update_only_p33_readme": True,
        },
        "confirmation_contract": {
            "required_author_reply": "确认",
            "binds_the_exact_sha256_of_this_json": True,
            "any_byte_change_requires_new_confirmation": True,
        },
        "boundaries": {
            "no_target_beyond_exact_37_pairs": True,
            "no_claim_strength_authorization": True,
            "no_collateral_authorization": True,
            "no_surface_producer_census_or_scientific_experiment": True,
            "no_result_refresh": True,
            "no_canonical_manuscript_or_pdf_promotion": True,
            "no_route_or_initial_system_change": True,
            "no_stage3_prime_re_review_or_stage4_5": True,
            "production_independence_remains_unestablished": True,
            "all_48_source_uses_remain_passage_inconclusive": True,
        },
        "stop_conditions": [
            "any frozen authority, base, manifest, bibliography, canonical, Route, or support-artifact hash differs",
            "any target or operation outside the exact 37 unique replace_block pairs is required",
            "any source-use row is silently upgraded beyond its explicit bounded-unavailability evidence",
            "any absent producer, adapter, predicate kernel, theorem encoding, or build hash would need to be invented",
            "any synthetic fixture would be represented as a surface record, census result, or production-validator proof",
            "any apply, citation, bibliography, schema, digest, untouched-block, build, or boundary check fails",
        ],
    }
    out = root / "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33_SCOPE_EXPANSION.json"
    out.write_text(json.dumps(request, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
