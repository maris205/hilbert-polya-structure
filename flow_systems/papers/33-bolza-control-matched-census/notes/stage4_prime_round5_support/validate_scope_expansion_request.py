#!/usr/bin/env python3
"""Fail-closed validation and receipt emitter for the P33 successor request."""

from __future__ import annotations

import copy
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[4]
PAPER = ROOT / "papers/33-bolza-control-matched-census"
NOTES = PAPER / "notes"
SUPPORT = NOTES / "stage4_prime_round5_support"
REQUEST = ROOT / "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33_SCOPE_EXPANSION.json"
REQUEST_MD = ROOT / "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33_SCOPE_EXPANSION.md"
VALIDATION = ROOT / "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33_SCOPE_EXPANSION_VALIDATION.json"
RECEIPT = ROOT / "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33_SCOPE_EXPANSION_RECEIPT.json"
ORIGINAL = ROOT / "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33.json"
EXPECTED_REQUEST_SHA = "100c97df01c356a52e3dea39ab327873f544d3ac6b32107f1576ae4dcb02db65"
ARS_SCRIPTS = Path("/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/skills/academic-research-suite/ars/scripts")
sys.path.insert(0, str(ARS_SCRIPTS))
from _block_parser import parse_document  # noqa: E402


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def artifact(path: Path) -> dict[str, Any]:
    return {
        "path": str(path.relative_to(ROOT)),
        "sha256": digest(path),
        "bytes": len(path.read_bytes()),
    }


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    generated_at_utc = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    checks: list[dict[str, Any]] = []

    def check(check_id: str, condition: bool, detail: Any = None) -> None:
        checks.append({"check_id": check_id, "status": "PASS" if condition else "FAIL", "detail": detail})

    request = load(REQUEST)
    original = load(ORIGINAL)
    original_paper = original["papers"][0]
    manifest = load(NOTES / "stage4_prime_round5_base.block-manifest.json")
    support_validation = load(NOTES / "stage4_prime_round5_support_validation.json")
    inventory = load(NOTES / "stage4_prime_round5_artifact_inventory_final.json")
    source_replay = load(NOTES / "stage4_prime_round5_source_identity_replay_receipt.json")
    source_matrix = load(NOTES / "stage4_prime_round5_source_use_locator_final.json")
    fixture_receipt = load(SUPPORT / "serialized_fixture_validation_receipt.json")
    component_provenance = load(SUPPORT / "component_build_provenance.json")
    producer_receipt = load(SUPPORT / "producer_contract_validation_receipt.json")
    correction = load(NOTES / "stage4_prime_round5_correction_bibliography_prospective.json")

    check("request:sha256", digest(REQUEST) == EXPECTED_REQUEST_SHA,
          {"expected": EXPECTED_REQUEST_SHA, "actual": digest(REQUEST)})
    check("request:schema", request.get("schema_version") == "round10-stage4-prime-p33-scope-expansion-authorization-request/1.0")
    check("request:status", request.get("status") == "AWAITING_EXPLICIT_AUTHOR_CONFIRMATION")
    check("request:paper", request.get("paper_id") == "P33")
    check("request:confirmation", request.get("confirmation_contract") == {
        "required_author_reply": "确认",
        "binds_the_exact_sha256_of_this_json": True,
        "any_byte_change_requires_new_confirmation": True,
    })
    markdown = REQUEST_MD.read_text(encoding="utf-8")
    check("request-md:mentions-exact-request-sha", markdown.count(EXPECTED_REQUEST_SHA) == 2)
    check("request-md:counts", all(token in markdown for token in ["41 mapped pairs", "37 unique", "seven support"]))
    check("request-md:confirmation", "Reply `确认`" in markdown)

    exact_authorities = {
        "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33.json": "ff160416cd8316326d2ef15b806f41479e63e299e0523899dbe93dc2e0da1650",
        "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_EXECUTION_AUTHORIZATION_RECEIPT.json": "7fda096bc17ab453ba2defa5301838ebc9e4056e48282f2eef6783aa96381ddf",
        "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_EXECUTION_INPUT_FREEZE.json": "87ce645eeccbd3a179d05ee48d7abe8c468e1a8f04e9e84cd1ca4037bf95ccff",
    }
    for path, expected in exact_authorities.items():
        check(f"authority:{path}", digest(ROOT / path) == expected,
              {"expected": expected, "actual": digest(ROOT / path)})

    for row in request["authority_bindings"]:
        path = ROOT / row["path"]
        check(f"authority-binding:{row['path']}:exists", path.is_file())
        if path.is_file():
            check(f"authority-binding:{row['path']}:sha256", digest(path) == row["sha256"])
            check(f"authority-binding:{row['path']}:bytes", len(path.read_bytes()) == row["bytes"])

    check("scope-stop:triggered", request["scope_stop"]["status"] == "TRIGGERED_BEFORE_BIBLIOGRAPHY_OR_PATCH_WRITE")
    check("scope-stop:exact-two-blocks", all(block in request["scope_stop"]["reason"] for block in ["B0041", "B0124"]))
    incident = ROOT / request["scope_stop"]["incident"]["path"]
    check("scope-stop:incident-sha", digest(incident) == request["scope_stop"]["incident"]["sha256"])
    incident_text = incident.read_text(encoding="utf-8")
    check("scope-stop:incident-disposition", "FAIL_CLOSED_UNLISTED_TARGETS_REQUIRED" in incident_text)
    check("scope-stop:incident-no-bib-patch-build", all(token in incident_text for token in [
        "No entry was appended", "no Stage-4′ patch", "PDF", "build log",
    ]))

    frozen_expected = {
        "base_draft": "8a4ea5ff994db83b91c2f14ca5a8425e6e2f954cbc7c87faf7edf27ec98b99d4",
        "block_manifest": "69006ab2614eb3171527b19c7880e58eee198aa5c7576e91210b28d81e9a8262",
        "bibliography": "12143967175abb0d325e16d156b1bc227e51f886009e7acd64691e84b92cb5e0",
        "canonical_manuscript": "b407441c07091ad38fb7e918721d31d2c4e3d897db9a705d92d9ff1f231f96d3",
        "canonical_pdf": "487a8838d9d422e00dcf3e896c9231b96c58fedfc2cdeb2265045f8d11d70031",
        "claim_surface_manifest": "b502d19662adbebcc6f8c4193f4d5e73e9267ce0be875f2787ec3800edd12fec",
        "initial_system": "b530d2f53f118d57c5281aff8eb3c367a48f85ae8ef2acdb1e73790b69139ea6",
        "route_crosswalk": "0434982b38bf658bfd808469671431f089140850ceb2c01875539ef997f942cf",
    }
    check("frozen-inputs:exact-key-set", set(request["frozen_inputs"]) == set(frozen_expected))
    for name, expected in frozen_expected.items():
        row = request["frozen_inputs"][name]
        path = ROOT / row["path"]
        check(f"frozen:{name}:expected-sha", row["sha256"] == expected)
        check(f"frozen:{name}:current-sha", digest(path) == expected,
              {"expected": expected, "actual": digest(path)})
        check(f"frozen:{name}:bytes", len(path.read_bytes()) == row["bytes"])

    carried = request["carried_forward_exact_request"]
    check("carried:original-request-sha", carried["request"]["sha256"] == digest(ORIGINAL))
    check("carried:items-object-equality", carried["items"] == original_paper["items"])
    check("carried:exact-seven-items", len(carried["items"]) == 7)
    check("carried:exact-item-ids", [row["item_id"] for row in carried["items"]] == [
        "REV-P33-002", "REV-P33-003", "REV-P33-005", "REV-P33-006",
        "REV-P33-007", "REV-P33-008", "REV-P33-013",
    ])
    check("carried:no-semantic-or-operation-scope-change", carried["semantic_or_operation_scope_change"] is False)

    def mappings(items: list[dict[str, Any]], id_key: str) -> list[tuple[str, str, str, str]]:
        return [
            (item[id_key], target["block_id"], operation, target["expected_old_hash"])
            for item in items
            for target in item["proposed_targets"]
            for operation in target["allowed_operations"]
        ]

    original_pairs = mappings(original_paper["items"], "item_id")
    carried_pairs = mappings(carried["items"], "item_id")
    new_pairs = mappings(request["new_issue_actions"], "action_id")
    all_pairs = carried_pairs + new_pairs
    unique_pairs = {(block, operation) for _, block, operation, _ in all_pairs}
    check("carried:mapping-object-equality", carried_pairs == original_pairs)
    check("carried:39-mapped", len(carried_pairs) == 39)
    check("carried:35-unique", len({(b, op) for _, b, op, _ in carried_pairs}) == 35)
    check("new:exact-two-actions", [a["action_id"] for a in request["new_issue_actions"]] == [
        "REV-P33-SCOPE-001", "REV-P33-SCOPE-002",
    ])
    check("new:exact-two-pairs", new_pairs == [
        ("REV-P33-SCOPE-001", "B0041", "replace_block", "597eb230d326"),
        ("REV-P33-SCOPE-002", "B0124", "replace_block", "3f69d3822846"),
    ])
    check("new:no-overlap-with-original", {b for _, b, _, _ in new_pairs}.isdisjoint({b for _, b, _, _ in carried_pairs}))
    check("total:41-mapped", len(all_pairs) == 41)
    check("total:37-unique", len(unique_pairs) == 37)
    check("total:all-replace-block", {operation for _, operation in unique_pairs} == {"replace_block"})

    by_block = {row["block_id"]: row for row in manifest["blocks"]}
    parsed_blocks = parse_document((NOTES / "stage4_revision_round1.tex").read_bytes().decode("utf-8")).block_by_id()
    full_new_issue_hashes: dict[str, str] = {}
    for provenance, block, operation, old_hash in all_pairs:
        check(f"target:{provenance}:{block}:manifest-present", block in by_block)
        if block in by_block:
            check(f"target:{provenance}:{block}:old-hash", by_block[block]["old_hash"] == old_hash)
        check(f"target:{provenance}:{block}:operation", operation == "replace_block")
    for block in ["B0041", "B0124"]:
        parsed = parsed_blocks.get(block)
        full_hash = hashlib.sha256(parsed.normalized_text.encode("utf-8")).hexdigest() if parsed else ""
        full_new_issue_hashes[block] = full_hash
        expected_prefix = next(old_hash for _, mapped_block, _, old_hash in new_pairs if mapped_block == block)
        check(f"new-full-hash-replay:{block}:parsed", parsed is not None)
        check(f"new-full-hash-replay:{block}:64-hex", bool(re.fullmatch(r"[0-9a-f]{64}", full_hash)))
        check(f"new-full-hash-replay:{block}:request-prefix", full_hash.startswith(expected_prefix),
              {"full_sha256": full_hash, "request_old_hash": expected_prefix})
        check(f"new-full-hash-replay:{block}:manifest-prefix", full_hash.startswith(by_block[block]["old_hash"]))

    counts = request["counts"]
    exact_counts = {
        "carried_residual_items": 7,
        "carried_item_target_mappings": 39,
        "carried_unique_block_operation_pairs": 35,
        "new_issue_actions": 2,
        "new_issue_target_mappings": 2,
        "total_mapped_pairs_with_item_or_action_provenance": 41,
        "total_unique_block_operation_pairs": 37,
        "replace_block_pairs": 37,
        "supporting_operations": 7,
        "artifact_inventory_rows": 43,
        "source_use_rows": 48,
        "distinct_sources": 20,
        "exact_passage_locators": 0,
        "explicit_bounded_unavailability_rows": 48,
        "valid_synthetic_fixtures": 2,
        "invalid_synthetic_fixtures": 12,
        "production_components_available": 0,
    }
    for key, expected in exact_counts.items():
        check(f"counts:{key}", counts.get(key) == expected,
              {"expected": expected, "actual": counts.get(key)})

    support_ops = request["supporting_operations"]
    check("support:exact-seven", len(support_ops) == 7)
    check("support:exact-operation-ids", [row["operation_id"] for row in support_ops] == [
        "P33-CURRENT-ARTIFACT-INVENTORY", "P33-CORRECTION-BIBLIOGRAPHY",
        "P33-INDEPENDENCE-PROVENANCE", "P33-SERIALIZED-FIXTURES",
        "P33-PRODUCER-COVERAGE-CONTRACTS", "P33-48-USE-PASSAGE-FINALIZATION",
        "P33-CONSERVATIVE-CONDITIONAL-TYPING",
    ])
    for current, frozen in zip(support_ops, original["supporting_operations"]):
        stripped = copy.deepcopy(current)
        result = stripped.pop("current_execution_result", None)
        check(f"support:{current['operation_id']}:original-scope-equality", stripped == frozen)
        check(f"support:{current['operation_id']}:has-current-result", isinstance(result, dict))
        if isinstance(result, dict):
            check(f"support:{current['operation_id']}:result-status", bool(result.get("notes_side_status")))
            for row in result.get("artifacts", []):
                path = ROOT / row["path"]
                check(f"support-result:{row['path']}:sha", path.is_file() and digest(path) == row["sha256"])

    check("support-manifest:exact-32", len(request["support_artifact_manifest"]) == 32)
    check("support-manifest:no-duplicate-paths", len({row["path"] for row in request["support_artifact_manifest"]}) == 32)
    for row in request["support_artifact_manifest"]:
        path = ROOT / row["path"]
        check(f"support-artifact:{row['path']}:exists", path.is_file())
        if path.is_file():
            check(f"support-artifact:{row['path']}:sha", digest(path) == row["sha256"])
            check(f"support-artifact:{row['path']}:bytes", len(path.read_bytes()) == row["bytes"])

    check("support-validation:pass", support_validation["status"] == "PASS_SUPPORT_COMPLETE_SCOPE_STOPPED_REQUEST_REISSUE_REQUIRED")
    check("support-validation:73-checks", support_validation["checks_run"] == 73)
    check("support-validation:zero-failures", support_validation["failure_count"] == 0)
    check("support-validation:exact-extra-targets", support_validation["scope_stop"]["additional_targets_required"] == ["B0041/replace_block", "B0124/replace_block"])
    check("support-validation:no-patch-bib-build", support_validation["scope_stop"]["patch_or_bib_or_build_performed"] is False)

    check("inventory:43-rows", len(inventory["artifacts"]) == 43 and inventory["counts"]["rows"] == 43)
    check("inventory:43-exact-commit-matches", inventory["counts"]["exact_match_at_pinned_commit"] == 43)
    check("inventory:zero-unavailable-or-mismatch", inventory["counts"]["unavailable_or_mismatch"] == 0)
    for row in inventory["artifacts"]:
        check(f"inventory:{Path(row['path']).name}:pinned-exact", row["pinned_commit_membership_state"] == "EXACT_MATCH_AT_PINNED_COMMIT")
        check(f"inventory:{Path(row['path']).name}:digest-match", row["sha256"] == row["pinned_commit_sha256"] == row["local_sha256_replayed"])
        check(f"inventory:{Path(row['path']).name}:bytes-match", row["bytes"] == row["pinned_commit_bytes"] == row["local_bytes_replayed"])

    source_counts = source_matrix["counts"]
    check("source-matrix:48-rows", len(source_matrix["source_use_rows"]) == 48 and source_counts["rows"] == 48)
    check("source-matrix:20-sources", len({row["source_id"] for row in source_matrix["source_use_rows"]}) == 20 and source_counts["distinct_sources"] == 20)
    check("source-matrix:zero-locators", source_counts["exact_passage_or_hypothesis_locators"] == 0)
    check("source-matrix:48-unavailable", source_counts["explicit_bounded_unavailability"] == 48)
    check("source-matrix:48-inconclusive", source_counts["claim_to_passage_inconclusive"] == 48)
    check("source-matrix:exact-use-ids", [row["use_id"] for row in source_matrix["source_use_rows"]] == [f"P33-U{i:02d}" for i in range(1, 49)])
    for row in source_matrix["source_use_rows"]:
        check(f"source-use:{row['use_id']}:bounded-unavailable", row["locator_disposition"] == "EXPLICIT_BOUNDED_UNAVAILABLE")
        check(f"source-use:{row['use_id']}:no-locator", row["exact_passage_or_hypothesis_locator"] is None)
        check(f"source-use:{row['use_id']}:inconclusive", row["anchor"] == "none" and row["claim_to_passage"] == "INCONCLUSIVE")
    check("source-replay:20-sources", len(source_replay["sources"]) == 20)
    http_200 = sum(row["http_status"] == 200 for row in source_replay["sources"])
    non_200 = sum(row["http_status"] not in (None, 200) for row in source_replay["sources"])
    transport_unavailable = sum(row["http_status"] is None for row in source_replay["sources"])
    check("source-replay:outcomes-15-4-1", (http_200, non_200, transport_unavailable) == (15, 4, 1),
          {"http_200": http_200, "non_200": non_200, "transport_unavailable": transport_unavailable})

    execution_freeze = load(ROOT / "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_EXECUTION_INPUT_FREEZE.json")
    frozen_p33 = next(row for row in execution_freeze["papers"] if row["paper_id"] == "P33")
    current_science_files = sorted(
        str(path.relative_to(ROOT))
        for directory in [PAPER / "code", PAPER / "experiments", PAPER / "results"]
        for path in directory.rglob("*")
        if path.is_file() and path.name != ".gitkeep"
    )
    check("science-freeze:authority-declares-empty", frozen_p33["science_files"] == [])
    check("science-freeze:current-nonsentinel-files-empty", current_science_files == [], current_science_files)
    check("science-freeze:code-sentinel", digest(PAPER / "code/.gitkeep") == "48eea24e6b02ed0761f07a8af281c234fc9f6c9ccee9305e5395733c565155d9")
    check("science-freeze:experiments-sentinel", digest(PAPER / "experiments/.gitkeep") == "6df9d48c988acad5795519a644ebb5d55f52c4e88deb5ed87fd47fd1a193156e")
    check("science-freeze:results-sentinel", digest(PAPER / "results/.gitkeep") == "87fa44d1ac4bd48df8288c6389e99aa304351ab6c81879d7177c5c31a4e9a050")

    fixture_counts = fixture_receipt["counts"]
    check("fixtures:status", fixture_receipt["status"] == "PASS_SYNTHETIC_CONFORMANCE_ONLY")
    check("fixtures:exact-2-valid", fixture_counts["valid_fixture_files"] == 2)
    check("fixtures:exact-12-invalid", fixture_counts["invalid_fixture_files"] == 12)
    check("fixtures:14-matches", fixture_counts["outcomes_matching_oracle"] == 14 and all(row["match"] for row in fixture_receipt["results"]))
    check("fixtures:zero-failures", fixture_counts["failures"] == 0)
    check("fixtures:set-digest", fixture_receipt["fixture_set_digest"] == "eb42f9672b27fc9f46a93acef06717c031ca1bae7e58a5d47a83da9152d8a5f2")
    valid_files = sorted((SUPPORT / "fixtures/valid").glob("*.json"))
    invalid_files = sorted((SUPPORT / "fixtures/invalid").glob("*.json"))
    check("fixtures:filesystem-2-valid", len(valid_files) == 2)
    check("fixtures:filesystem-12-invalid", len(invalid_files) == 12)

    prod = component_provenance["production_components"]
    check("components:exact-seven-production-slots", len(prod) == 7)
    check("components:all-unavailable", all(row["availability"] == "UNAVAILABLE_COMPONENT_NOT_IMPLEMENTED" for row in prod))
    check("components:all-build-fields-null", all(row["source_tree_sha256"] is None and row["build_environment_sha256"] is None and row["build_sha256"] is None for row in prod))
    check("components:independence-not-established", load(SUPPORT / "trust_graph.json")["status"] == "FAIL_CLOSED_PRODUCTION_INDEPENDENCE_NOT_ESTABLISHED")
    check("producer-contracts:pass-contract-only", producer_receipt["status"] == "PASS_CONTRACTS_ONLY_NO_PRODUCER_RUN")
    check("producer-contracts:exact-four", len(producer_receipt["artifacts"]) == 4)
    check("producer-contracts:no-observed-digest", producer_receipt["checks"]["no_observed_coverage_digest"] is True)
    check("producer-contracts:no-run", producer_receipt["checks"]["no_producer_execution"] is True)

    check("corrections:exact-keys", [row["key"] for row in correction["prospective_entries"]] == ["P33-S03-CORR", "P33-S16-CORR"])
    check("corrections:exact-five-uses", [row["use_id"] for row in correction["affected_uses"]] == ["P33-U08", "P33-U22", "P33-U27", "P33-U28", "P33-U37"])
    bibliography = (PAPER / "paper/references.bib").read_text(encoding="utf-8")
    check("corrections:not-appended:S03", re.search(r"@\w+\{P33-S03-CORR\s*,", bibliography) is None)
    check("corrections:not-appended:S16", re.search(r"@\w+\{P33-S16-CORR\s*,", bibliography) is None)

    superseded = request["superseded_scope_attempt1"]
    check("superseded:status", superseded["status"] == "NONCONTROLLING_SUPERSEDED_DUE_TO_UNLISTED_TARGETS")
    check("superseded:not-applicable", superseded["may_be_used_for_apply"] is False)
    check("superseded:exact-four", [Path(row["path"]).name for row in superseded["artifacts"]] == [
        "stage4_prime_round5_revision_roadmap.json", "stage4_prime_round5_author_choices.json",
        "stage4_prime_round5_claim_surface_manifest.json", "stage4_prime_round5_author_adjudication.json",
    ])
    for row in superseded["artifacts"]:
        path = ROOT / row["path"]
        check(f"superseded:{path.name}:hash", digest(path) == row["sha256"])
        check(f"superseded:{path.name}:incident-listed", row["sha256"] in incident_text)

    next_execution = request["requested_next_execution"]
    check("next:fresh-successor-authority-required", next_execution["fresh_successor_authority_chain_required"] is True)
    check("next:exact-37-patch-ops", next_execution["patch_ops"] == 37 and next_execution["operation"] == "replace_block")
    check("next:exact-two-bib-keys", next_execution["append_bibliography_keys_exactly"] == ["P33-S03-CORR", "P33-S16-CORR"])
    check("next:exact-five-use-bindings", next_execution["bind_affected_uses"] == ["P33-U08", "P33-U22", "P33-U27", "P33-U28", "P33-U37"])

    absent_outputs = [
        NOTES / "stage4_prime_revision_round2.tex",
        NOTES / "stage4_prime_revision_round2.pdf",
        NOTES / "stage4_prime_revision_patch_round2.json",
        NOTES / "stage4_prime_revision_round2.tex.apply-report.json",
        NOTES / "stage4_prime_round5_writer_handoff.json",
        NOTES / "stage4_prime_round5_provisional_response.json",
    ]
    for path in absent_outputs:
        check(f"prohibited-output-absent:{path.name}", not path.exists())

    readme = PAPER / "README.md"
    readme_text = readme.read_text(encoding="utf-8")
    check("readme:support-complete-request-ready", "SUPPORT COMPLETE — SCOPE STOPPED — EXPANDED REQUEST" in readme_text)
    check("readme:not-stage4-prime-complete", "No Stage 4′ manuscript\nor bibliography execution is complete." in readme_text)
    check("readme:successor-links", all(name in readme_text for name in [
        "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33_SCOPE_EXPANSION.md",
        "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33_SCOPE_EXPANSION_VALIDATION.json",
        "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33_SCOPE_EXPANSION_RECEIPT.json",
    ]))

    failures = [row for row in checks if row["status"] != "PASS"]
    validation = {
        "schema_version": "round10-stage4-prime-p33-scope-expansion-validation/1.0",
        "generated_at_utc": generated_at_utc,
        "workflow_date": "2026-09-04",
        "paper_id": "P33",
        "status": "PASS_SCOPE_EXPANSION_REQUEST_READY_AWAITING_CONFIRMATION" if not failures else "FAIL_CLOSED",
        "request": artifact(REQUEST),
        "request_markdown": artifact(REQUEST_MD),
        "support_validation": artifact(NOTES / "stage4_prime_round5_support_validation.json"),
        "scope_stop_incident": artifact(NOTES / "stage4_prime_round5_scope_stop_incident.md"),
        "p33_readme": artifact(readme),
        "checks_run": len(checks),
        "failure_count": len(failures),
        "checks": checks,
        "new_issue_full_block_hash_replay": {
            block: {
                "normalization": "ARS patch protocol normalized block text; marker excluded; CRLF-to-LF; blank edges stripped",
                "sha256": full_hash,
                "authorized_old_hash_prefix": full_hash[:12],
            }
            for block, full_hash in full_new_issue_hashes.items()
        },
        "counts": {
            "carried_residual_items": 7,
            "carried_item_target_mappings": len(carried_pairs),
            "carried_unique_block_operation_pairs": len({(b, op) for _, b, op, _ in carried_pairs}),
            "new_issue_actions": len(request["new_issue_actions"]),
            "new_issue_target_mappings": len(new_pairs),
            "total_mapped_pairs_with_item_or_action_provenance": len(all_pairs),
            "total_unique_block_operation_pairs": len(unique_pairs),
            "replace_block_pairs": sum(operation == "replace_block" for _, operation in unique_pairs),
            "supporting_operations": len(support_ops),
            "support_artifacts_bound": len(request["support_artifact_manifest"]),
            "artifact_inventory_rows": len(inventory["artifacts"]),
            "source_use_rows": len(source_matrix["source_use_rows"]),
            "distinct_sources": len({row["source_id"] for row in source_matrix["source_use_rows"]}),
            "http_200_source_replays": http_200,
            "non_200_source_replays": non_200,
            "transport_unavailable_source_replays": transport_unavailable,
            "exact_passage_locators": source_counts["exact_passage_or_hypothesis_locators"],
            "explicit_bounded_unavailability_rows": source_counts["explicit_bounded_unavailability"],
            "valid_synthetic_fixtures": fixture_counts["valid_fixture_files"],
            "invalid_synthetic_fixtures": fixture_counts["invalid_fixture_files"],
            "fixture_outcomes_matching": fixture_counts["outcomes_matching_oracle"],
            "production_components_available": sum(row["availability"] != "UNAVAILABLE_COMPONENT_NOT_IMPLEMENTED" for row in prod),
        },
        "mutation_boundary": {
            "bibliography_appended": False,
            "patch_emitted_or_applied": False,
            "new_draft_or_pdf_emitted": False,
            "build_run": False,
            "scientific_producer_or_census_run": False,
            "result_refreshed": False,
            "canonical_or_route_or_initial_system_changed": False,
            "p33_readme_status_only": True,
        },
        "blockers": [
            "Explicit confirmation of the exact successor request SHA-256 is required.",
            "A fresh successor roadmap, choices, claim manifest, and adjudication must be generated after confirmation.",
            "All 48 source uses lack exact passage locators and remain INCONCLUSIVE.",
            "Production components and build provenance are unavailable; independence is not established.",
        ],
    }
    VALIDATION.write_text(json.dumps(validation, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if failures:
        return 1

    receipt = {
        "schema_version": "round10-stage4-prime-p33-scope-expansion-request-receipt/1.0",
        "generated_at_utc": generated_at_utc,
        "workflow_date": "2026-09-04",
        "paper_id": "P33",
        "status": "SUPPORT_COMPLETE_SCOPE_STOPPED_SUCCESSOR_REQUEST_READY_AWAITING_CONFIRMATION",
        "artifacts": [
            artifact(REQUEST), artifact(REQUEST_MD), artifact(VALIDATION),
            artifact(NOTES / "stage4_prime_round5_support_validation.json"),
            artifact(NOTES / "stage4_prime_round5_scope_stop_incident.md"), artifact(readme),
        ],
        "counts": validation["counts"],
        "new_issue_full_block_hash_replay": validation["new_issue_full_block_hash_replay"],
        "validation_checks": validation["checks_run"],
        "validation_failures": 0,
        "superseded_scope_attempt1": {
            "status": "NONCONTROLLING_SUPERSEDED_DUE_TO_UNLISTED_TARGETS",
            "may_be_used_for_apply": False,
            "artifacts": superseded["artifacts"],
        },
        "current_mutations": validation["mutation_boundary"],
        "next_gate": {
            "required_author_reply": "确认",
            "binds_exact_request_sha256": EXPECTED_REQUEST_SHA,
            "fresh_successor_authority_chain_required": True,
            "any_request_byte_change_requires_new_confirmation": True,
        },
        "blockers": validation["blockers"],
    }
    RECEIPT.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
