#!/usr/bin/env python3
"""Generate the exact P33 Round-5 Stage-4-prime support artifacts.

The script is deliberately limited to repository-artifact replay, source-identity
replay, synthetic conformance fixtures, and prospective producer contracts.  It
does not run BP, CP, an owner census, or a scientific experiment.
"""

from __future__ import annotations

import copy
import csv
import hashlib
import json
import platform
import sys
import urllib.error
import urllib.request
from pathlib import Path


WORKFLOW_DATE = "2026-09-04"
COMMIT = "337994b72bd14c7ffbc1f01a6a9b878784df7694"
USER_AGENT = "P33-Stage4Prime-BoundedReplay/1.0"


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha_path(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def digest(label: str) -> str:
    return sha_bytes(label.encode("utf-8"))


def write_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_canonical_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8"))


def artifact(path: Path, root: Path) -> dict:
    raw = path.read_bytes()
    return {"path": str(path.relative_to(root)), "sha256": sha_bytes(raw), "bytes": len(raw)}


def find_request_items(obj: object) -> list[dict]:
    candidates: list[list[dict]] = []

    def walk(value: object) -> None:
        if isinstance(value, dict):
            for child in value.values():
                walk(child)
        elif isinstance(value, list):
            rows = [x for x in value if isinstance(x, dict) and str(x.get("item_id", "")).startswith("REV-P33-")]
            if rows:
                candidates.append(rows)
            for child in value:
                walk(child)

    walk(obj)
    if not candidates:
        raise RuntimeError("No P33 request items found")
    items = max(candidates, key=len)
    if len(items) != 7:
        raise RuntimeError(f"Expected seven P33 items, found {len(items)}")
    return items


def build_authority_carriers(root: Path, notes: Path) -> None:
    request_path = root / "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33.json"
    request = json.loads(request_path.read_text(encoding="utf-8"))
    items = find_request_items(request)
    roadmap_items = []
    for ordinal, item in enumerate(items, 1):
        item_id = item["item_id"]
        blocks = [t["block_id"] for t in item["proposed_targets"]]
        obligation = item["residual_obligation_class"]
        roadmap_items.append({
            "id": item_id,
            "source_refs": [{"seat": "EIC", "channel": "finding", "ordinal": ordinal, "subclaim_ordinal": 0}],
            "description": item["residual_gap"],
            "reviewer": "EIC",
            "sub_claim_ids": [f"SC-{item_id}-R5"],
            "obligation_class": obligation,
            "severity": "major" if obligation == "must_fix" else "minor",
            "evidence_anchor": {
                "anchor_type": "absence",
                "locator": f"notes/stage3_prime_round5_verification_report.md, {item_id}",
                "absence_scope": item["residual_gap"],
                "check_performed": "Checked the hash-bound Round-5 verdict and traceability against the exact Stage-4 Round-1 base and its 128-block manifest.",
            },
            "confidence": 5,
            "competence_basis": "Hash-bound Stage-3-prime Round-5 residual verification",
            "cost_scope": {"kind": "section", "locator": ", ".join(blocks)},
            "consequence_if_unaddressed": {"code": "evidence_gap_remains", "target": {"kind": "claim", "locator": item["residual_gap"]}},
            "target_section": ", ".join(blocks),
            "suggested_action": (item["implementation_branch"].replace("included/rejected digest domains", "included-stream and exclusion-stream digest domains")),
            "consensus_level": "SINGLE-VERIFIER",
            "verification_criteria": "Use every and only the exact authorized replace_block targets; retain all claim, science, canonical-promotion, Route, and execution boundaries.",
            "proposed_targets": [{"block_id": t["block_id"], "allowed_operations": list(t["allowed_operations"])} for t in item["proposed_targets"]],
        })
    roadmap = {
        "schema_version": "revision-roadmap/1.0",
        "revision_round": 2,
        "base_draft_sha256": "8a4ea5ff994db83b91c2f14ca5a8425e6e2f954cbc7c87faf7edf27ec98b99d4",
        "block_manifest_sha256": "69006ab2614eb3171527b19c7880e58eee198aa5c7576e91210b28d81e9a8262",
        "items": roadmap_items,
        "total_items": 7,
        "obligation_counts": {"must_fix": 6, "should_fix": 1, "consider": 0},
        "editorial_decision": "Major Revision",
        "consensus_summary": "Non-ranking carrier of exactly the seven author-confirmed P33 Round-5 residual items; the execution receipt and request remain the controlling authority.",
        "dissenting_opinions": [],
    }
    write_json(notes / "stage4_prime_round5_revision_roadmap.json", roadmap)
    roadmap_path = notes / "stage4_prime_round5_revision_roadmap.json"
    write_json(notes / "stage4_prime_round5_claim_surface_manifest.json", {
        "schema_version": "claim-surface-manifest/1.0",
        "revision_round": 2,
        "roadmap_sha256": sha_path(roadmap_path),
        "base_draft_sha256": "8a4ea5ff994db83b91c2f14ca5a8425e6e2f954cbc7c87faf7edf27ec98b99d4",
        "claim_intent_sources": [],
        "surfaces": [],
    })

    event_id = "AUTHOR-EVENT-20260904-ROUND10-STAGE4-PRIME-CORRECTION-EXECUTION"
    choices = {
        "schema_version": "author-adjudication-input/1.0",
        "author_events": [{
            "event_id": event_id,
            "source": "explicit_session_user_message",
            "actor_role": "author",
            "input_sha256": "111505020ac13b92ac253361e21777de8343455edd9ed3a4436fe924600cb812",
        }],
        "display_order": {"mode": "source_traceability", "item_ids": [i["item_id"] for i in items], "author_event_id": event_id},
        "author_adjudications": [{
            "item_id": item["item_id"],
            "author_event_id": event_id,
            "author_triage": "will_address",
            "authorized_targets": [{"block_id": t["block_id"], "allowed_operations": list(t["allowed_operations"])} for t in item["proposed_targets"]],
            "claim_strength_authorizations": [],
        } for item in items],
        "collateral_authorizations": [],
    }
    write_json(notes / "stage4_prime_round5_author_choices.json", choices)


def build_commit_inventory(root: Path, notes: Path) -> None:
    prospective_path = notes / "stage4_prime_round5_artifact_inventory_prospective.json"
    prospective = json.loads(prospective_path.read_text(encoding="utf-8"))
    rows = []
    failures = []
    for row in prospective["artifacts"]:
        relative = row["path"]
        local = root / relative
        local_raw = local.read_bytes()
        raw_url = f"https://raw.githubusercontent.com/maris205/hilbert-polya-structure/{COMMIT}/flow_systems/{relative}"
        request = urllib.request.Request(raw_url, headers={"User-Agent": USER_AGENT})
        remote_raw = b""
        http_status = None
        error = None
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                http_status = response.status
                remote_raw = response.read()
        except urllib.error.HTTPError as exc:
            http_status = exc.code
            error = f"HTTPError:{exc.code}"
        except Exception as exc:
            error = f"{type(exc).__name__}:{exc}"
        local_hash = sha_bytes(local_raw)
        remote_hash = sha_bytes(remote_raw) if remote_raw else None
        state = "EXACT_MATCH_AT_PINNED_COMMIT" if (
            http_status == 200 and remote_hash == row["sha256"] == local_hash
            and len(remote_raw) == row["bytes"] == len(local_raw)
        ) else "UNAVAILABLE_OR_MISMATCH_FAIL_CLOSED"
        if state != "EXACT_MATCH_AT_PINNED_COMMIT":
            failures.append(relative)
        rows.append({
            **row,
            "local_sha256_replayed": local_hash,
            "local_bytes_replayed": len(local_raw),
            "pinned_commit_raw_url": raw_url,
            "pinned_commit_http_status": http_status,
            "pinned_commit_sha256": remote_hash,
            "pinned_commit_bytes": len(remote_raw) if remote_raw else None,
            "pinned_commit_replay_error": error,
            "pinned_commit_membership_state": state,
        })
    final = {
        "schema_version": "p33-stage4-prime-round5-artifact-inventory-final/1.0",
        "workflow_date": WORKFLOW_DATE,
        "paper_id": "P33",
        "status": "PASS_EXACT_43_OF_43_AT_PINNED_COMMIT" if not failures else "FAIL_CLOSED",
        "source_prospectus": artifact(prospective_path, root),
        "repository_locator": f"https://github.com/maris205/hilbert-polya-structure/tree/{COMMIT}/flow_systems/papers/33-bolza-control-matched-census",
        "commit": COMMIT,
        "retrieval_interface": "raw.githubusercontent.com HTTPS GET by exact commit and repository-relative path",
        "retrieval_date_utc": WORKFLOW_DATE,
        "selection_rule": prospective["selection_rule"],
        "artifacts": rows,
        "counts": {"required_rows": 43, "rows": len(rows), "exact_match_at_pinned_commit": len(rows) - len(failures), "unavailable_or_mismatch": len(failures)},
        "boundaries": {"persistent_archive_claim": False, "doi_claim": False, "scientific_truth_inferred_from_hash": False},
    }
    final_path = notes / "stage4_prime_round5_artifact_inventory_final.json"
    write_json(final_path, final)
    receipt = {
        "schema_version": "p33-stage4-prime-round5-artifact-inventory-receipt/1.0",
        "workflow_date": WORKFLOW_DATE,
        "paper_id": "P33",
        "status": final["status"],
        "inventory": artifact(final_path, root),
        "commit": COMMIT,
        "counts": final["counts"],
        "failures": failures,
    }
    write_json(notes / "stage4_prime_round5_artifact_inventory_receipt.json", receipt)
    if failures:
        raise RuntimeError(f"Pinned-commit artifact replay failed for {failures}")


def build_source_matrix(root: Path, notes: Path) -> None:
    inventory_rows = list(csv.DictReader((notes / "stage1_phase2_source_inventory.tsv").open(encoding="utf-8"), delimiter="\t"))
    literature_rows = list(csv.DictReader((notes / "stage1_phase3_literature_matrix.tsv").open(encoding="utf-8"), delimiter="\t"))
    inventory = {f"P33-{r['source_id']}": r for r in inventory_rows}
    literature = {f"P33-{r['source_id']}": r for r in literature_rows}
    retrievals = {}
    for source_id in sorted(inventory):
        source = inventory[source_id]
        url = source["stable_url"]
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        result = {
            "receipt_id": f"P33-SOURCE-REPLAY-{source_id[-3:]}",
            "source_id": source_id,
            "interface": "HTTPS GET with redirects and a 4096-byte response-prefix ceiling",
            "retrieval_date_utc": WORKFLOW_DATE,
            "exact_query": url,
            "declared_identifier": source["doi"] or url,
            "http_status": None,
            "content_type": None,
            "returned_url": None,
            "response_prefix_bytes_read": 0,
            "transport_error": None,
        }
        try:
            with urllib.request.urlopen(req, timeout=25) as response:
                prefix = response.read(4096)
                result.update({
                    "http_status": response.status,
                    "content_type": response.headers.get("Content-Type"),
                    "returned_url": response.geturl(),
                    "response_prefix_bytes_read": len(prefix),
                })
        except urllib.error.HTTPError as exc:
            result.update({"http_status": exc.code, "content_type": exc.headers.get("Content-Type"), "returned_url": exc.geturl(), "transport_error": f"HTTPError:{exc.code}"})
        except Exception as exc:
            result["transport_error"] = f"{type(exc).__name__}:{exc}"
        result["identity_retrieval_state"] = "IDENTIFIER_ENDPOINT_RESPONDED" if result["http_status"] == 200 else "IDENTIFIER_ENDPOINT_UNAVAILABLE_IN_BOUNDED_REPLAY"
        result["passage_retrieval_state"] = "NOT_VERIFIED_PREFIX_ONLY_NO_FULL_TEXT_RETAINED_OR_PARSED"
        retrievals[source_id] = result

    retrieval_receipt = {
        "schema_version": "p33-stage4-prime-round5-source-identity-replay-receipt/1.0",
        "workflow_date": WORKFLOW_DATE,
        "paper_id": "P33",
        "status": "COMPLETE_20_SOURCE_BOUNDED_IDENTITY_REPLAY_PASSAGE_UNAVAILABLE",
        "scope": "Current identifier-endpoint replay only. No historical row is reconstructed and no response prefix is retained as a source passage.",
        "sources": [retrievals[k] for k in sorted(retrievals)],
        "counts": {
            "sources": 20,
            "http_200": sum(r["http_status"] == 200 for r in retrievals.values()),
            "http_non_200": sum(r["http_status"] not in (None, 200) for r in retrievals.values()),
            "transport_unavailable": sum(r["http_status"] is None for r in retrievals.values()),
            "passage_bodies_retained_or_parsed": 0,
        },
    }
    retrieval_path = notes / "stage4_prime_round5_source_identity_replay_receipt.json"
    write_json(retrieval_path, retrieval_receipt)

    prospective_path = notes / "stage4_prime_round5_source_use_locator_prospective.json"
    prospective = json.loads(prospective_path.read_text(encoding="utf-8"))
    corrections = {
        "P33-S03": "BASE_AND_P33-S03-CORR_BOUND_WHERE_AFFECTED",
        "P33-S16": "BASE_AND_P33-S16-CORR_BOUND_WHERE_AFFECTED",
        "P33-S12": "CORRECTED_PAGE_RANGE_287_305_RETAINED",
    }
    affected = {
        "P33-U08": "P33-S03-CORR", "P33-U22": "P33-S16-CORR",
        "P33-U27": "P33-S03-CORR", "P33-U28": "P33-S16-CORR",
        "P33-U37": "P33-S16-CORR",
    }
    final_rows = []
    for row in prospective["source_use_rows"]:
        sid = row["source_id"]
        inv = inventory[sid]
        lit = literature[sid]
        correction_key = affected.get(row["use_id"])
        replay = retrievals[sid]
        final_rows.append({
            "use_id": row["use_id"],
            "source_id": sid,
            "block_id": row["block_id"],
            "expected_old_hash": row["expected_old_hash"],
            "occurrence_in_block": row["occurrence_in_block"],
            "current_context_tail": row["current_context_tail"],
            "interface": replay["interface"],
            "retrieval_date_utc": replay["retrieval_date_utc"],
            "exact_query": replay["exact_query"],
            "returned_identifier_or_unavailable_total_receipt": {
                "declared_identifier": replay["declared_identifier"],
                "receipt_id": replay["receipt_id"],
                "http_status": replay["http_status"],
                "returned_url": replay["returned_url"],
                "transport_error": replay["transport_error"],
            },
            "screening_disposition": "RETAIN_FROZEN_SOURCE_IDENTITY_KEEP_PASSAGE_INCONCLUSIVE",
            "exact_passage_or_hypothesis_locator": None,
            "locator_disposition": "EXPLICIT_BOUNDED_UNAVAILABLE",
            "unavailability_receipt": "The bounded replay checked only the frozen identifier endpoint and at most 4096 response-prefix bytes. It retained and parsed no full-text body, and the frozen ledger supplied no exact page/section/paragraph. No passage locator is inferred.",
            "hypotheses": lit["compatibility_role"],
            "correction_state": corrections.get(sid, "NO_ITEM_SPECIFIC_CORRECTION_BINDING; SYSTEMATIC_RETRACTION_AUDIT_NOT_CLAIMED"),
            "citation_keys_required": [sid] + ([correction_key] if correction_key else []),
            "applicability_statement": lit["admissible_contribution"],
            "prohibited_stronger_transfer": lit["excluded_stronger_claim"],
            "anchor": "none",
            "claim_to_passage": "INCONCLUSIVE",
            "finalization_status": "FINALIZED_AS_EXPLICIT_BOUNDED_UNAVAILABILITY",
        })
    final = {
        "schema_version": "p33-stage4-prime-round5-source-use-locator-final/1.0",
        "workflow_date": WORKFLOW_DATE,
        "paper_id": "P33",
        "status": "COMPLETE_48_ROWS_WITH_EXPLICIT_BOUNDED_UNAVAILABILITY",
        "base_draft": prospective["base_draft"],
        "source_identity_replay": artifact(retrieval_path, root),
        "source_use_rows": final_rows,
        "counts": {
            "rows": len(final_rows),
            "distinct_sources": len({r["source_id"] for r in final_rows}),
            "exact_passage_or_hypothesis_locators": sum(r["exact_passage_or_hypothesis_locator"] is not None for r in final_rows),
            "explicit_bounded_unavailability": sum(r["locator_disposition"] == "EXPLICIT_BOUNDED_UNAVAILABLE" for r in final_rows),
            "claim_to_passage_inconclusive": sum(r["claim_to_passage"] == "INCONCLUSIVE" for r in final_rows),
            "correction_dual_bindings": sum(len(r["citation_keys_required"]) == 2 for r in final_rows),
        },
        "boundaries": {
            "historical_rows_fabricated": False,
            "inconclusive_silently_upgraded": False,
            "scientific_result_changed": False,
            "systematic_retraction_or_coi_audit_claimed": False,
        },
    }
    final_path = notes / "stage4_prime_round5_source_use_locator_final.json"
    write_json(final_path, final)
    write_json(notes / "stage4_prime_round5_source_use_locator_receipt.json", {
        "schema_version": "p33-stage4-prime-round5-source-use-locator-receipt/1.0",
        "workflow_date": WORKFLOW_DATE,
        "paper_id": "P33",
        "status": "PASS_EXACT_ROW_ACCOUNTING_WITH_RESIDUAL_PASSAGE_BLOCKER",
        "matrix": artifact(final_path, root),
        "counts": final["counts"],
        "residual_blocker": "All 48 rows have explicit bounded-unavailability receipts and remain claim_to_passage=INCONCLUSIVE; no exact source passage was verified.",
    })


def build_fixtures_and_provenance(root: Path, support: Path) -> None:
    registry = {
        "schema_version": "p33-synthetic-proof-registry-snapshot/1.0",
        "paper_contract": "P33-PROOF-TYPES/1",
        "scope": "Synthetic conformance fixture profile only; not a production theorem encoding or checker registry.",
        "proof_types": [
            "canonical_conjugacy_normal_form", "conjugacy_to_inverse", "coverage_replay",
            "exact_conjugator", "exact_cutoff_comparison", "exact_trace_comparison",
            "maximal_root", "no_proper_power", "systolic_primitive", "termination_measure",
        ],
    }
    registry_path = support / "synthetic_proof_registry_snapshot.json"
    write_json(registry_path, registry)
    registry_digest = sha_path(registry_path)

    zero = digest("P33 synthetic zero")
    one = digest("P33 synthetic one")
    two = digest("P33 synthetic two")
    base = {
        "candidate_id": "synthetic-candidate-001",
        "correction_provenance_digest": digest("synthetic correction provenance"),
        "coverage_digest": digest("synthetic coverage"),
        "cutoff": {"den": "10", "num": "21"},
        "cutoff_disposition": "within",
        "implementation_digest": digest("synthetic implementation"),
        "input_digest": digest("synthetic input"),
        "inverse_class_digest": one,
        "oriented_class_digest": zero,
        "owner_id": two,
        "owner_member_digests": [zero, one],
        "primitive_root_digest": zero,
        "producer_id": "BP-SYNTHETIC",
        "proof_payload": {"input_digests": [digest("synthetic input")], "witness": "synthetic-only"},
        "proof_registry_digest": registry_digest,
        "proof_type": "exact_trace_comparison",
        "record_type": "candidate",
        "root_exponent": "1",
        "run_id": "synthetic-bp-minimal",
        "schema_version": "P33-OWNER-CERT/1",
        "state": "accepted",
        "surface_id": "BOLZA-SOURCE-LOCK",
        "theorem_version_digest": digest("synthetic theorem"),
        "unresolved_count": "0",
    }
    bp = copy.deepcopy(base)
    cp = copy.deepcopy(base)
    cp.update({
        "candidate_id": "synthetic-candidate-002",
        "producer_id": "CP-SYNTHETIC",
        "proof_type": "canonical_conjugacy_normal_form",
        "run_id": "synthetic-cp-minimal",
        "surface_id": "NAZARENKO-EXP-OCTAGON-G2",
    })

    fixtures: dict[str, dict] = {
        "valid/bp_minimal.json": bp,
        "valid/cp_minimal.json": cp,
    }
    malformed = copy.deepcopy(bp); malformed["unknown_demo_field"] = "forbidden"
    unknown = copy.deepcopy(cp); unknown["proof_type"] = "unknown_demo"
    altered = copy.deepcopy(bp); altered["proof_registry_digest"] = "f" * 64
    unsupported = copy.deepcopy(cp); unsupported["proof_type"] = "search_timeout_negative"
    power = copy.deepcopy(bp); power["proof_type"] = "no_proper_power"; power["root_exponent"] = "2"
    missing_inverse = copy.deepcopy(cp); del missing_inverse["inverse_class_digest"]
    false_reciprocity = copy.deepcopy(bp); false_reciprocity["owner_rule_id"] = "self_reciprocal"
    duplicate = copy.deepcopy(cp); duplicate["owner_member_digests"] = [zero, zero]
    unresolved = copy.deepcopy(bp); unresolved["cutoff_disposition"] = "unresolved"
    incomplete = copy.deepcopy(cp); incomplete["record_type"] = "coverage"; incomplete["proof_type"] = "coverage_replay"; incomplete["unresolved_count"] = "1"
    bad_termination = copy.deepcopy(bp); bad_termination["record_type"] = "termination"; bad_termination["proof_type"] = "termination_measure"; bad_termination["termination_witness"] = "queue_nonempty"
    hash_mismatch = copy.deepcopy(cp); hash_mismatch["input_digest"] = "not-a-sha256"
    fixtures.update({
        "invalid/malformed_schema.json": malformed,
        "invalid/unknown_proof_type.json": unknown,
        "invalid/altered_digest.json": altered,
        "invalid/unsupported_negative_decision.json": unsupported,
        "invalid/primitive_power_conflict.json": power,
        "invalid/missing_inverse_link.json": missing_inverse,
        "invalid/false_reciprocity.json": false_reciprocity,
        "invalid/duplicate_owner.json": duplicate,
        "invalid/unresolved_cutoff.json": unresolved,
        "invalid/incomplete_coverage.json": incomplete,
        "invalid/invalid_termination.json": bad_termination,
        "invalid/hash_mismatch.json": hash_mismatch,
    })
    for relative, obj in fixtures.items():
        write_canonical_json(support / "fixtures" / relative, obj)

    expected = {
        "valid/bp_minimal.json": "accepted:synthetic_conformance",
        "valid/cp_minimal.json": "accepted:synthetic_conformance",
        "invalid/malformed_schema.json": "rejected:unknown_field",
        "invalid/unknown_proof_type.json": "not_evaluable:unrecognized_proof_type",
        "invalid/altered_digest.json": "rejected:proof_registry_digest_mismatch",
        "invalid/unsupported_negative_decision.json": "not_evaluable:unsupported_negative_decision",
        "invalid/primitive_power_conflict.json": "rejected:primitive_power_conflict",
        "invalid/missing_inverse_link.json": "rejected:missing_inverse_link",
        "invalid/false_reciprocity.json": "rejected:false_reciprocity",
        "invalid/duplicate_owner.json": "rejected:duplicate_owner",
        "invalid/unresolved_cutoff.json": "bounded_incomplete:unresolved_cutoff",
        "invalid/incomplete_coverage.json": "bounded_incomplete:incomplete_coverage",
        "invalid/invalid_termination.json": "rejected:invalid_termination",
        "invalid/hash_mismatch.json": "rejected:hash_mismatch",
    }
    oracle_rows = []
    for relative in sorted(fixtures):
        path = support / "fixtures" / relative
        oracle_rows.append({
            "relative_path": relative,
            "sha256": sha_path(path),
            "bytes": len(path.read_bytes()),
            "expected_disposition": expected[relative],
            "expected_outcome_basis": "Direct synthetic conformance rule named by this case; no producer label or surface result consumed.",
        })
    oracle = {
        "schema_version": "p33-stage4-prime-synthetic-fixture-oracle/1.0",
        "workflow_date": WORKFLOW_DATE,
        "paper_id": "P33",
        "status": "FROZEN_BEFORE_HARNESS_EXECUTION",
        "scope": "Expected outcomes for synthetic conformance fixtures only.",
        "independence_state": "PROCEDURALLY_SEPARATE_FROM_ANY_PRODUCER_OUTPUT_BUT_NOT_INDEPENDENTLY_AUTHORED_BY_A_SECOND_HUMAN_OR_RUNTIME",
        "producer_outputs_consumed": 0,
        "fixtures": oracle_rows,
        "counts": {"valid": 2, "invalid": 12},
    }
    write_json(support / "fixture_oracle_manifest.json", oracle)

    nodes = [
        ("BP", "UNAVAILABLE_COMPONENT_NOT_IMPLEMENTED"),
        ("CP", "UNAVAILABLE_COMPONENT_NOT_IMPLEMENTED"),
        ("A_BP", "UNAVAILABLE_COMPONENT_NOT_IMPLEMENTED"),
        ("A_CP", "UNAVAILABLE_COMPONENT_NOT_IMPLEMENTED"),
        ("V_parse", "UNAVAILABLE_COMPONENT_NOT_IMPLEMENTED"),
        ("V_pred", "UNAVAILABLE_COMPONENT_NOT_IMPLEMENTED"),
        ("fixture_oracle_O", "AVAILABLE_SYNTHETIC_ONLY_INDEPENDENCE_NOT_ESTABLISHED"),
        ("theorem_encodings", "UNAVAILABLE_COMPONENT_NOT_IMPLEMENTED"),
        ("external_libraries", "PYTHON_STANDARD_LIBRARY_ONLY_FOR_SYNTHETIC_HARNESS"),
        ("accountable_implementers", "NO_PRODUCTION_IMPLEMENTER_ATTESTATION"),
    ]
    write_json(support / "trust_graph.json", {
        "schema_version": "p33-stage4-prime-trust-graph/1.0",
        "workflow_date": WORKFLOW_DATE,
        "paper_id": "P33",
        "status": "FAIL_CLOSED_PRODUCTION_INDEPENDENCE_NOT_ESTABLISHED",
        "nodes": [{"node_id": n, "state": s} for n, s in nodes],
        "edges": [
            {"from": "BP", "to": "A_BP", "state": "PROSPECTIVE"},
            {"from": "CP", "to": "A_CP", "state": "PROSPECTIVE"},
            {"from": "A_BP", "to": "V_parse", "state": "PROSPECTIVE"},
            {"from": "A_CP", "to": "V_parse", "state": "PROSPECTIVE"},
            {"from": "V_parse", "to": "V_pred", "state": "PROSPECTIVE"},
            {"from": "fixture_oracle_O", "to": "synthetic_conformance_harness", "state": "SYNTHETIC_ONLY"},
        ],
        "allowed_shared_dependencies": ["frozen schema identifiers", "digest specification", "disclosed standard-library JSON and SHA-256"],
        "disqualifying_dependencies": ["producer decision code inside V_pred", "producer-derived expected outcomes", "undisclosed shared implementation"],
        "claim_boundary": "The graph records absent components and a synthetic-only harness; it does not establish validator independence.",
    })

    harness = support / "validate_synthetic_fixtures.py"
    generator = support / "generate_authorized_support.py"
    write_json(support / "component_build_provenance.json", {
        "schema_version": "p33-stage4-prime-component-build-provenance/1.0",
        "workflow_date": WORKFLOW_DATE,
        "paper_id": "P33",
        "status": "PRODUCTION_COMPONENTS_UNAVAILABLE_SYNTHETIC_SUPPORT_TOOLS_HASHED",
        "production_components": [{
            "component": name,
            "availability": "UNAVAILABLE_COMPONENT_NOT_IMPLEMENTED",
            "source_tree_sha256": None,
            "build_environment_sha256": None,
            "build_sha256": None,
        } for name in ["BP", "CP", "A_BP", "A_CP", "V_parse", "V_pred", "theorem_encodings"]],
        "synthetic_support_tools": [artifact(generator, root), artifact(harness, root)],
        "runtime": {
            "python_version": platform.python_version(),
            "implementation": platform.python_implementation(),
            "platform": platform.platform(),
            "runtime_descriptor_sha256": digest("|".join([platform.python_version(), platform.python_implementation(), platform.platform()])),
            "build_artifact": "NOT_APPLICABLE_INTERPRETED_SCRIPT",
        },
        "accountability_boundary": "Generated under explicit author authorization in one Codex execution context; no independent production implementer or second-runtime attestation exists.",
    })
    p33 = root / "papers/33-bolza-control-matched-census"
    candidates = [str(p.relative_to(root)) for folder in (p33 / "code", p33 / "experiments", p33 / "results") if folder.exists() for p in folder.rglob("*") if p.is_file()]
    write_json(support / "producer_code_exclusion_audit.json", {
        "schema_version": "p33-stage4-prime-producer-code-exclusion-audit/1.0",
        "workflow_date": WORKFLOW_DATE,
        "paper_id": "P33",
        "status": "NOT_EVALUABLE_PRODUCER_AND_PREDICATE_COMPONENTS_UNAVAILABLE",
        "locations_checked": ["papers/33-bolza-control-matched-census/code", "papers/33-bolza-control-matched-census/experiments", "papers/33-bolza-control-matched-census/results"],
        "candidate_files_found": candidates,
        "producer_decision_code_absent_from_v_pred": "NOT_EVALUABLE_NO_V_PRED_SOURCE_TREE",
        "synthetic_harness_boundary": "The notes-side harness dispatches fixed synthetic conformance failures only and is not V_pred.",
        "independence_established": False,
    })


def coverage_schema(producer_id: str) -> dict:
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": f"urn:p33:{producer_id.lower()}:coverage-ledger:1",
        "title": f"P33 {producer_id} coverage ledger contract",
        "type": "object",
        "additionalProperties": False,
        "required": [
            "schema_version", "producer_id", "input_sha256", "theorem_version_digest",
            "algorithm_version_digest", "enumeration_order", "cutoff", "termination",
            "included_stream_digest", "rejected_stream_digest", "coverage_digest",
            "unresolved_count", "unresolved_records", "population_bound_replay",
        ],
        "properties": {
            "schema_version": {"const": f"P33-{producer_id}-COVERAGE/1"},
            "producer_id": {"const": producer_id},
            "input_sha256": {"type": "string", "pattern": "^[0-9a-f]{64}$"},
            "theorem_version_digest": {"type": "string", "pattern": "^[0-9a-f]{64}$"},
            "algorithm_version_digest": {"type": "string", "pattern": "^[0-9a-f]{64}$"},
            "enumeration_order": {"type": "string", "minLength": 1},
            "cutoff": {"const": {"den": "10", "num": "21"}},
            "termination": {"type": "object"},
            "included_stream_digest": {"type": "string", "pattern": "^[0-9a-f]{64}$"},
            "rejected_stream_digest": {"type": "string", "pattern": "^[0-9a-f]{64}$"},
            "coverage_digest": {"type": "string", "pattern": "^[0-9a-f]{64}$"},
            "unresolved_count": {"type": "integer", "minimum": 0},
            "unresolved_records": {"type": "array", "items": {"type": "object"}},
            "population_bound_replay": {"type": "object"},
        },
    }


def build_producer_contracts(root: Path, support: Path) -> None:
    bp = {
        "schema_version": "p33-bp-enumeration-contract/1.0",
        "producer_id": "BP",
        "status": "CONTRACT_ONLY_NO_PRODUCER_RUN",
        "exact_input_representation": "papers/28-bolza-magnetic-flow/results/round4_bolza_group_certificate.json",
        "input_sha256": "e3e6c486c66116dc6fe9fdd054c2fce9d4b1a58318f56d1656f6db168c807eca",
        "theorem_version_digest": None,
        "algorithm_version_digest": None,
        "enumeration_domain": "Conditionally empty only if a separately passage-adequate strict-systole proof record and exact replay establish sys(S_Bolza)>21/10.",
        "unambiguous_enumeration_order": "EMPTY_STREAM_ONLY_AFTER_THE_CONDITIONAL_STRICT_SYSTOLE_GATE; otherwise no enumeration order is licensed and the ledger remains unresolved.",
        "exact_cutoff_procedure": "Compare the exact rational 21/10 only; no rounded decimal and no retuning.",
        "termination_measure": "A valid separately frozen strict-systole replay receipt; absent or conflicting evidence yields UPSTREAM_REPLAY_CONTRADICTION or NOT_EVALUABLE.",
        "included_stream_digest_domain": "ASCII P33-BP-INCLUDED, NUL, schema version, NUL, canonical sorted included bytes",
        "rejected_stream_digest_domain": "ASCII P33-BP-REJECTED, NUL, schema version, NUL, canonical sorted rejected bytes",
        "distinct_coverage_digest_domain": "ASCII P33-BP-COVERAGE, NUL, exact input/theorem/algorithm/cutoff/termination/included/rejected/unresolved bindings",
        "complete_unresolved_ledger_schema": "bp_coverage_ledger.schema.json",
        "independent_population_bound_replay": "Checker must replay the strict-systole gate and verify the empty included stream plus every bound digest; no status label is trusted.",
        "bp_empty_domain_conditional_path": True,
        "observed_coverage_digest": None,
        "execution_performed": False,
    }
    cp = {
        "schema_version": "p33-cp-enumeration-contract/1.0",
        "producer_id": "CP",
        "status": "CONTRACT_ONLY_NO_PRODUCER_RUN",
        "exact_input_representation": "papers/28-bolza-magnetic-flow/results/round7_nonarithmetic_control_matrices.json",
        "input_sha256": "a900749b6905a5f324c2e2670363ec1bc9480481f3f5aa1240ed0ebbee55e6ca",
        "bound_domain_certificate": "papers/28-bolza-magnetic-flow/results/round8_control_finite_ball_certificate.json",
        "bound_domain_certificate_sha256": "c1bf68a8a1485665680dba01d0012fb691c7ca1a795e36334639e34bbbdbcb1f",
        "theorem_version_digest": None,
        "algorithm_version_digest": None,
        "enumeration_domain": "Exact identity-connected centre-guard component with |alpha|^2<=20000 from the frozen certificate.",
        "unambiguous_enumeration_order": "FIFO breadth-first from identity through g0,g1,g2,g3,g0^-1,g1^-1,g2^-1,g3^-1; exact normalized-state deduplication; final included and rejected streams lexicographically sorted by canonical state bytes.",
        "exact_cutoff_procedure": "Exact translation length comparison ell(g)<=21/10; no rounded decimal and no retuning.",
        "termination_measure": "FIFO queue empty and every outgoing edge from every included state classified included or rejected.",
        "included_stream_digest_domain": "ASCII P33-CP-INCLUDED, NUL, schema version, NUL, canonical sorted included bytes",
        "rejected_stream_digest_domain": "ASCII P33-CP-REJECTED, NUL, schema version, NUL, canonical sorted rejected bytes",
        "distinct_coverage_digest_domain": "ASCII P33-CP-COVERAGE, NUL, exact input/theorem/algorithm/cutoff/termination/included/rejected/unresolved bindings",
        "complete_unresolved_ledger_schema": "cp_coverage_ledger.schema.json",
        "independent_population_bound_replay": "Checker reconstructs the centre-guard bound, traversal coverage, sorted streams, all digest domains, and the complete unresolved ledger.",
        "accepted_upstream_stream_digests_are_inputs_not_observed_outputs": [
            "814f72badce2cc90e8e26edc2a7db18d52c4c334c0f5dfc5bf7d8e4a90dcf545",
            "3017c21285daad5a1173b076c9b5700975f67cdbbdaa8a6218e80d4bc89da6f4",
        ],
        "observed_coverage_digest": None,
        "execution_performed": False,
    }
    paths = {
        "bp_enumeration_contract.json": bp,
        "bp_coverage_ledger.schema.json": coverage_schema("BP"),
        "cp_enumeration_contract.json": cp,
        "cp_coverage_ledger.schema.json": coverage_schema("CP"),
    }
    for name, obj in paths.items():
        write_json(support / name, obj)
    checks = {
        "exact_four_contract_or_schema_files": len(paths) == 4,
        "bp_cp_digest_domains_distinct": bp["distinct_coverage_digest_domain"] != cp["distinct_coverage_digest_domain"],
        "bp_empty_path_conditional": bp["bp_empty_domain_conditional_path"] is True,
        "theorem_and_algorithm_versions_unavailable_honestly": all(x["theorem_version_digest"] is None and x["algorithm_version_digest"] is None for x in (bp, cp)),
        "no_observed_coverage_digest": bp["observed_coverage_digest"] is None and cp["observed_coverage_digest"] is None,
        "no_producer_execution": not bp["execution_performed"] and not cp["execution_performed"],
    }
    write_json(support / "producer_contract_validation_receipt.json", {
        "schema_version": "p33-stage4-prime-producer-contract-validation-receipt/1.0",
        "workflow_date": WORKFLOW_DATE,
        "paper_id": "P33",
        "status": "PASS_CONTRACTS_ONLY_NO_PRODUCER_RUN" if all(checks.values()) else "FAIL_CLOSED",
        "artifacts": [artifact(support / name, root) for name in sorted(paths)],
        "checks": checks,
        "remaining_blockers": ["BP and CP are not implemented.", "Theorem and algorithm version digests are unavailable.", "No observed coverage ledger or coverage digest exists."],
    })


def main() -> int:
    support = Path(__file__).resolve().parent
    notes = support.parent
    root = Path(__file__).resolve().parents[4]
    build_authority_carriers(root, notes)
    build_commit_inventory(root, notes)
    build_source_matrix(root, notes)
    build_fixtures_and_provenance(root, support)
    build_producer_contracts(root, support)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
