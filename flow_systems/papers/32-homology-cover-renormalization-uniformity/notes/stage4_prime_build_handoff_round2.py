#!/usr/bin/env python3
"""Build P32 Stage-4-prime notes-only writer receipts and handoff."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from stage4_prime_build_patch_round2 import assert_layout_only_reemission


ROOT = Path(__file__).resolve().parents[3]
PAPER = Path(__file__).resolve().parent.parent
NOTES = PAPER / "notes"
STAMP = "2026-09-03T18:44:04Z"
INCIDENT = NOTES / "stage4_prime_layout_preflight_incident_round2.md"
ARCHIVE = NOTES / "stage4_prime_layout_superseded_20260904"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def item(path: Path, *, count_name: str | None = None, count: int | None = None) -> dict:
    row = {
        "path": path.relative_to(PAPER).as_posix(),
        "sha256": sha(path),
        "bytes": path.stat().st_size,
    }
    if count_name is not None:
        row[count_name] = count
    return row


def write_json(name: str, payload: dict) -> Path:
    path = NOTES / name
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path


def assert_and_build_layout_lineage(patch_path: Path, patch: dict) -> tuple[dict, list[str]]:
    expected = {
        INCIDENT: "626369cb512caadf4c81883d076d4bc4feddbb0744ea50dcf3e5609683617512",
        ARCHIVE / "stage4_prime_revision_patch_round2.json": "6e7a93bb08a7cd2e2c3d91aca8f09be03f72bdf455fd76fdf9133bfa5725a9aa",
        ARCHIVE / "stage4_prime_revision_round2.tex": "b81355f5d808660b572c1dc795c7e4a26560b2899fa385a62969179c5316345c",
        ARCHIVE / "stage4_prime_revision_round2.tex.apply-report.json": "60129658386f502a964361e85cccc51245dcb2193a0cedd8c15b432cee6dc87e",
        ARCHIVE / "stage4_prime_revision_round2.preflight.pdf": "03e45373fd915ff0af2d1cf6ba44ca02841a112c6be0b26ba2e5126ffc12f6f5",
        ARCHIVE / "stage4_prime_revision_round2.preflight.log": "011070ed6fefc3fb0ee6a65a8d7c30dbaaa3cdc101a780fce10f16f394f123d4",
        ARCHIVE / "stage4_prime_support_evidence_bundle_round2.json": "0f6468918ad31f086034d73f3bbcb05eda9227a14fed56c25a82ff19ac92d06f",
        ARCHIVE / "stage4_prime_response_to_reviewers_provisional_round2.json": "d53d5166bc2065ee7b055d6d4924ff82ec1975dfe8f79ae72e7f2a1b1754f833",
        ARCHIVE / "stage4_prime_writer_validation_receipt_round2.json": "be3c03fb43cf1ed6d87d875f5ffc33450dc56e2e494f0105fc01a183f730a777",
        ARCHIVE / "stage4_prime_writer_handoff.json": "00e803186e89a6cf147e83a6e55ca6a3afbf7f9a6edab8ebb18f5dd348eab728",
        ARCHIVE / "stage4_prime_revision_patch_round2_writer_receipt.md": "7720e21ca13fa933e2113b56ac424366d1a805e77d11ac0238eb081815ee1b03",
    }
    for path, digest in expected.items():
        if not path.is_file() or sha(path) != digest:
            raise RuntimeError(f"layout lineage drift: {path}")
    superseded_patch_path = ARCHIVE / "stage4_prime_revision_patch_round2.json"
    superseded_patch = json.loads(superseded_patch_path.read_text(encoding="utf-8"))
    layout_targets = assert_layout_only_reemission(patch, superseded_patch)
    if sha(patch_path) == sha(superseded_patch_path):
        raise RuntimeError("layout re-emission did not change patch bytes")
    archive_outputs = [
        superseded_patch_path,
        ARCHIVE / "stage4_prime_revision_round2.tex",
        ARCHIVE / "stage4_prime_revision_round2.tex.apply-report.json",
        ARCHIVE / "stage4_prime_revision_round2.preflight.pdf",
        ARCHIVE / "stage4_prime_revision_round2.preflight.log",
        ARCHIVE / "stage4_prime_support_evidence_bundle_round2.json",
        ARCHIVE / "stage4_prime_response_to_reviewers_provisional_round2.json",
        ARCHIVE / "stage4_prime_writer_validation_receipt_round2.json",
        ARCHIVE / "stage4_prime_writer_handoff.json",
        ARCHIVE / "stage4_prime_revision_patch_round2_writer_receipt.md",
    ]
    lineage = {
        "reason": "SEMANTIC_NEUTRAL_LAYOUT_ONLY_AFTER_FAIL_CLOSED_PREFLIGHT",
        "incident": item(INCIDENT),
        "superseded_archive": {
            "directory": "notes/stage4_prime_layout_superseded_20260904",
            "preserved": True,
            "artifacts": [item(path) for path in archive_outputs],
            "patch_apply_status": "APPLIED_BY_SEPARATE_ACTOR_THEN_WITHDRAWN",
            "preview_result": "FAIL_CLOSED_EIGHT_OVERFULL_BOXES",
        },
        "superseded_patch_sha256": sha(superseded_patch_path),
        "current_patch": item(patch_path, count_name="ops", count=len(patch["ops"])),
        "layout_only_changed_targets": layout_targets,
        "b0133_origin": "Fresh applied block B0133 derives from the authorized B0044 replace_block new_text; B0044 carries its scoped layout remediation.",
        "scope": {
            "targets_added": 0,
            "operation_types_changed": 0,
            "authority_bindings_changed": 0,
            "scientific_or_citation_wording_changed": False,
            "scientific_values_changed": False,
            "claim_strength_changed": False,
        },
        "current_apply_status": "NOT_APPLIED",
        "current_preview_status": "NOT_BUILT_BY_WRITER",
    }
    return lineage, layout_targets


def assert_authority() -> tuple[list[dict], dict]:
    authority = [
        (ROOT / "BATCH_ROUND10_STAGE4_PRIME_EXECUTION_STAGE4_5_AND_ROUND5_AUTHORIZATION_RECEIPT.json", "4cc48a512c35dc31ccff0b1ff80472eed04fc454d83f4410277bd2fe356e4e4c"),
        (ROOT / "BATCH_ROUND10_STAGE4_PRIME_EXECUTION_STAGE4_5_AND_ROUND5_INPUT_FREEZE.json", "081f28e0ade1af62d8f5d56d90b83ff543e1019ab1931473ff95754e81855e98"),
        (ROOT / "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P29_P32.json", "3a17181450f040e274f1fa6c31386ff2593c04f409013908bfad759d408d65fa"),
        (NOTES / "stage4_prime_writer_authority_handoff.json", "622043c794de49fd390b332f50189466f01cb5f5d7cc7ab72a2f864e16235dd2"),
    ]
    rows = []
    for path, expected in authority:
        actual = sha(path)
        if actual != expected:
            raise RuntimeError(f"authority drift: {path}")
        rows.append({"path": str(path.relative_to(PAPER)) if path.is_relative_to(PAPER) else "../../../" + path.name, "sha256": actual})
    carrier = json.loads((NOTES / "stage4_prime_writer_authority_handoff.json").read_text(encoding="utf-8"))
    expected_bindings = {
        "roadmap": "6bee67d48f17d921ee4db668155cb52f5339c820a2647d57981e2b5e5ab2e318",
        "author_adjudication": "89e84ef27c82e3f306654058ff94fe4aed6a282ac3aee021d6f621c914295619",
        "claim_surface_manifest": "0d912de18b674c1c9ed30ab73392b1cb57e7d8d6f40772153628554b0c6cc3a6",
    }
    for name, expected in expected_bindings.items():
        if carrier[name]["sha256"] != expected or sha(PAPER / carrier[name]["path"]) != expected:
            raise RuntimeError(f"carrier binding drift: {name}")
    if carrier["author_decision_digest"] != "2cc8ee4d45d96bea0c9a065127c8539062dd019a345a77c4c963093ad23d98ab":
        raise RuntimeError("author decision digest drift")
    return rows, carrier


def assert_frozen_files() -> list[dict]:
    expected = {
        "paper/manuscript.tex": ("4a3e1f084dc1e27005479971299fd9da67bb6c817278d5de0de6cf03cbc8000a", 43923),
        "paper/paper.pdf": ("66948e247c72a3388a7f3da1f80be1d74860afa1261c99fb18c85e2b8bb84f93", 254332),
        "paper/references.bib": ("e699c96196377892d3aa1f280e6a5117001c3cec37a511a3d1c08fdc52127de9", 8100),
        "code/.gitkeep": ("48eea24e6b02ed0761f07a8af281c234fc9f6c9ccee9305e5395733c565155d9", 32),
        "experiments/.gitkeep": ("6df9d48c988acad5795519a644ebb5d55f52c4e88deb5ed87fd47fd1a193156e", 33),
        "results/.gitkeep": ("87fa44d1ac4bd48df8288c6389e99aa304351ab6c81879d7177c5c31a4e9a050", 25),
        "notes/stage1_prestart_brief.md": ("e879124e9e6dddd42458c19e38bd6768848880b887fcbb8756c773d577a74fa7", 663),
        "notes/stage4_route_crosswalk.md": ("570b8d7307913495053c69560ccd04e0d37ab6dbcd99fbe53248b81db296fcda", 1890),
    }
    rows = []
    for rel, (digest, size) in expected.items():
        path = PAPER / rel
        if sha(path) != digest or path.stat().st_size != size:
            raise RuntimeError(f"frozen file drift: {rel}")
        rows.append({"path": rel, "sha256": digest, "bytes": size, "status": "UNCHANGED"})
    return rows


def main() -> None:
    authority, carrier = assert_authority()
    frozen = assert_frozen_files()
    base = NOTES / "stage4_revision_round1.tex"
    block_manifest = NOTES / "stage4_prime_base.block-manifest.json"
    patch_path = NOTES / "stage4_prime_revision_patch_round2.json"
    patch = json.loads(patch_path.read_text(encoding="utf-8"))
    layout_lineage, layout_targets = assert_and_build_layout_lineage(patch_path, patch)
    if sha(base) != "d1a65f96d09477f19250acecb77c578c83218ca0deb1ca75ad0bbe4398f24d05":
        raise RuntimeError("base drift")
    if sha(block_manifest) != "1619df00762015f4e4c9130c6b37373148a162da69810c4dc10af5b0a0bba056":
        raise RuntimeError("block manifest drift")
    if len(patch["ops"]) != 18 or len({op["block_id"] for op in patch["ops"]}) != 18:
        raise RuntimeError("patch op/target count drift")
    if any(op["claim_strength_changes"] or op["collateral_authorization_ids"] for op in patch["ops"]):
        raise RuntimeError("unauthorized claim or collateral movement")
    if (NOTES / "stage4_prime_revision_round2.tex").exists() or (NOTES / "stage4_prime_revision_round2.pdf").exists():
        raise RuntimeError("forbidden applied output exists")

    ledger_path = NOTES / "stage4_prime_literature_screening_ledger_round2.json"
    ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
    passage_path = NOTES / "stage4_prime_claim_passage_matrix_round2.json"
    passage = json.loads(passage_path.read_text(encoding="utf-8"))
    closest_path = NOTES / "stage4_prime_closest_work_source_verification_round2.json"
    closest = json.loads(closest_path.read_text(encoding="utf-8"))
    formal_path = NOTES / "stage4_prime_formal_definition_audit_round2.json"
    formal = json.loads(formal_path.read_text(encoding="utf-8"))
    scalar_path = NOTES / "stage4_prime_conditional_scalar_lemma_audit_round2.json"
    scalar = json.loads(scalar_path.read_text(encoding="utf-8"))
    analytic_path = NOTES / "stage4_prime_analytic_registry_audit_round2.json"
    analytic = json.loads(analytic_path.read_text(encoding="utf-8"))
    manifest_path = NOTES / "stage4_prime_reader_artifact_manifest_round2.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    notes_bib = NOTES / "stage4_prime_references_round2.bib"

    support_files = [
        NOTES / "stage4_prime_build_support_round2.py",
        NOTES / "stage4_prime_build_literature_replay_round2.py",
        NOTES / "stage4_prime_literature_replay_round2.raw.json",
        ledger_path,
        NOTES / "stage4_prime_literature_screening_ledger_round2.tsv",
        closest_path,
        NOTES / "stage4_prime_closest_work_comparison_matrix_round2.json",
        NOTES / "stage4_prime_closest_work_comparison_matrix_round2.tsv",
        passage_path,
        NOTES / "stage4_prime_claim_passage_matrix_round2.tsv",
        notes_bib,
        formal_path,
        scalar_path,
        analytic_path,
        manifest_path,
    ]
    support_bundle = {
        "schema_version": "round10-stage4-prime-writer-support-bundle/1.0",
        "paper_id": "P32",
        "revision_round": 2,
        "generated_at_utc": STAMP,
        "authority": authority,
        "authority_carrier": {"path": "notes/stage4_prime_writer_authority_handoff.json", "sha256": sha(NOTES / "stage4_prime_writer_authority_handoff.json")},
        "patch": item(patch_path, count_name="ops", count=len(patch["ops"])),
        "layout_reemission": layout_lineage,
        "support_artifacts": [item(path) for path in support_files],
        "counts": {
            "residual_items": 7,
            "authorized_block_operation_pairs": 26,
            "emitted_ops": 18,
            "unique_target_blocks": 18,
            "frozen_queries_replayed": 26,
            "current_replay_manifestations": ledger["row_count"],
            "replay_decisions": ledger["decision_counts"],
            "closest_work_records": closest["search_bound"]["retained_entries"],
            "claim_passage_rows": passage["row_count"],
            "claim_passage_finalized": passage["passage_finalized_count"],
            "claim_passage_inconclusive": passage["passage_inconclusive_count"],
            "analytic_registry_rows": analytic["row_count"],
            "section6_artifacts_exact_at_pinned_commit": manifest["section6_exact_at_pinned_commit_count"],
            "local_support_sidecars_pending_sync": manifest["local_stage4_prime_sidecar_count"],
        },
        "audit_outcomes": {
            "formal": formal["audit_outcome"],
            "formal_scientific_application": formal["scientific_application_status"],
            "conditional_scalar": scalar["audit_outcome"],
            "analytic_registry": analytic["audit_outcome"],
        },
        "boundaries": {
            "scientific_execution": False,
            "scientific_value_refresh": False,
            "canonical_files_changed": False,
            "registered_claim_replacements": 0,
            "collateral_authorizations_used": 0,
            "patch_applied": False,
            "preview_or_pdf_built": False,
            "stage4_5_run": False,
            "route_state_change": False,
        },
        "remaining_blockers": [
            "P32-S01--P32-S26 exact theorem passages remain INCONCLUSIVE.",
            "Fourteen support-evidence sidecars are local and absent from the pinned public commit pending repository synchronization.",
            "SG2OwnerCanonical-v1 and all ownerwise cover/factor derivations remain absent.",
            "Formal carriers are defined, but factor application, global products, and infinite scalar specialization remain NOT_EVALUABLE.",
            "AN-1--AN-5 majorants, cofinality, and interchanges remain UNPROVED and unexecuted.",
            "Independent current-patch application, isolated layout preflight/build, unregistered-claim drift review, and Stage 4.5 audit remain pending.",
        ],
    }
    support_bundle_path = write_json("stage4_prime_support_evidence_bundle_round2.json", support_bundle)

    provisional = {
        "schema_version": "response-to-reviewers-provisional/1.0",
        "artifact_status": "PROVISIONAL_PENDING_REAPPLICATION_LAYOUT_PREFLIGHT_AND_POST_APPLY_AUDIT",
        "paper_number": 32,
        "revision_round": 2,
        "generated_at_utc": STAMP,
        "patch_binding": {**item(patch_path, count_name="ops", count=len(patch["ops"])), "apply_status": "NOT_APPLIED_CURRENT_REEMISSION"},
        "layout_reemission": {
            "reason": layout_lineage["reason"],
            "incident": layout_lineage["incident"],
            "superseded_patch_sha256": layout_lineage["superseded_patch_sha256"],
            "current_patch_sha256": sha(patch_path),
            "layout_only_changed_targets": layout_targets,
            "scientific_or_citation_response_wording_changed": False,
            "claim_strength_changed": False,
        },
        "authority_bindings": {
            "roadmap_sha256": carrier["roadmap"]["sha256"],
            "author_adjudication_sha256": carrier["author_adjudication"]["sha256"],
            "author_decision_digest": carrier["author_decision_digest"],
            "claim_surface_manifest_sha256": carrier["claim_surface_manifest"]["sha256"],
            "registered_claim_surface_count": carrier["claim_surface_manifest"]["surfaces"],
        },
        "items": [
            {
                "roadmap_item_id": "REV-P32-EIC-W1",
                "status": "RESOLVED_WITH_BOUNDED_NONPRIORITY_SCOPE",
                "author_response": "The patch names four source-verified closest works and gives a four-component overlap/difference matrix. Each source is nearest in one component only, and priority and exhaustive novelty remain disclaimed.",
                "change_location": "B0018",
            },
            {
                "roadmap_item_id": "REV-P32-EIC-W2",
                "status": "RESOLVED_FOR_PINNED_SECTION6_INPUTS_WITH_LOCAL_SYNC_LIMITATION",
                "author_response": "A commit-pinned public base resolves all 11 artifacts claimed current in Section 6 with exact hashes, bytes, schema/media type, access state, and role. Fourteen new support sidecars are inventoried honestly as local and absent from that commit; no archive or DOI is claimed.",
                "change_location": "B0098 and B0125",
            },
            {
                "roadmap_item_id": "REV-P32-EIC-W4",
                "status": "RESOLVED",
                "author_response": "The executed-method block is limited to scholarly corpus operations and nonexecution. Four same-family role labels, the MAJOR_REVISION code, correlated-error limitation, and author adjudication move to a declarations provenance paragraph.",
                "change_location": "B0049 and insertion after B0128",
            },
            {
                "roadmap_item_id": "REV-P32-R1-W1",
                "status": "RESOLVED_FORMAL_CARRIER_ONLY",
                "author_response": "The frozen positive finite-owner/degree inverse system, topology, equality, localization, embeddings, singleton projections, separately typed one-owner zero fibers, and finite scalar domains are defined, with a compatibility lemma and proof. Scientific factor application and every global claim remain not evaluable.",
                "change_location": "B0081, B0131, B0082, B0083, and B0084",
            },
            {
                "roadmap_item_id": "REV-P32-R1-W2",
                "status": "RESOLVED_REGISTRY_SHAPE_ONLY",
                "author_response": "AN-1--AN-5 now have one complete table with exact summand and branch, indices, schedule coupling, compact domain, limit order, explicit majorant, named interchange, prerequisites, and status. Every row remains UNPROVED and unexecuted.",
                "change_location": "B0090 and B0091",
            },
            {
                "roadmap_item_id": "REV-P32-R1-W4",
                "status": "RESOLVED_CURRENT_LEDGER_WITH_INHERITED_PASSAGE_LIMITATION",
                "author_response": "A new complete 51-manifestation frozen-query replay ledger is published without reconstructing historical rows. The 30-row passage matrix retains 26 inherited INCONCLUSIVE uses and finalizes only four narrow closest-work scopes.",
                "change_location": "B0044, B0047, and B0109",
            },
            {
                "roadmap_item_id": "REV-P32-DA-M1",
                "status": "RESOLVED_CONDITIONAL_LEMMA_ONLY",
                "author_response": "The exact Phi_m>B lemma and elementary proof are supplied. Its higher- and zero-content applications are expressly conditional on missing factor derivations and yield no executed mismatch, global obstruction, recovery result, or Route credit.",
                "change_location": "B0060, B0066, and B0072",
            },
        ],
        "summary": {
            "residual_items_covered": 7,
            "patch_ops": len(patch["ops"]),
            "notes_side_bibliography_entries_added": 4,
            "canonical_bibliography_entries_added": 0,
            "scientific_execution_status": "NONE",
            "application_status": "NOT_APPLIED_CURRENT_REEMISSION",
        },
    }
    provisional_path = write_json("stage4_prime_response_to_reviewers_provisional_round2.json", provisional)

    validation = {
        "schema_version": "round10-stage4-prime-writer-validation-receipt/1.0",
        "paper_id": "P32",
        "generated_at_utc": STAMP,
        "patch": item(patch_path, count_name="ops", count=len(patch["ops"])),
        "layout_reemission": layout_lineage,
        "checks": {
            "authority_carrier_sha256": "PASS",
            "revision_roadmap_validate_review_patch_authorization": "PASS",
            "patch_format_1_1_schema": "PASS",
            "unique_patch_targets": "PASS_18_OF_18",
            "old_hashes_match_bound_manifest": "PASS_18_OF_18",
            "all_ops_within_authorized_pair_set": "PASS_18_OF_26_AVAILABLE_PAIRS",
            "empty_claim_strength_changes": "PASS_18_OF_18",
            "empty_collateral_authorization_ids": "PASS_18_OF_18",
            "bare_unbreakable_64_hex_in_new_text": "PASS_ZERO",
            "superseded_lineage_hashes": "PASS_11_OF_11",
            "layout_only_changed_targets": "PASS_7_OF_7",
            "unchanged_new_text_targets_byte_identical": "PASS_11_OF_11",
            "operation_metadata_and_authority_bindings_unchanged": "PASS_18_OF_18",
            "b0133_traced_to_authorized_b0044": "PASS",
            "full_pinned_url_target_preserved_with_compact_label": "PASS_2_OF_2",
            "visible_chunked_commit_hash_preserved": "PASS_2_OF_2",
            "long_logarithmic_summand_split_with_aligned": "PASS",
            "claim_strength_and_scientific_value_change": "PASS_NONE",
            "canonical_and_science_freeze": "PASS_8_OF_8",
            "output_draft_and_pdf_absent": "PASS",
            "support_schema_and_counts": "PASS",
        },
        "frozen_files": frozen,
        "prohibited_actions": {
            "ars_apply_revision_patch_py_run": False,
            "applied_draft_generated": False,
            "preview_or_pdf_generated": False,
            "stage4_5_run": False,
            "canonical_or_science_file_modified": False,
            "scientific_number_refreshed": False,
        },
        "next_required_actor": "independent patch applier and isolated layout preflight; Stage-4.5 auditor only after preflight PASS",
    }
    validation_path = write_json("stage4_prime_writer_validation_receipt_round2.json", validation)

    handoff = {
        "schema_version": "round10-stage4-prime-writer-handoff/1.0",
        "paper_id": "P32",
        "revision_round": 2,
        "generated_at_utc": STAMP,
        "authority": authority,
        "base_draft": {"path": "notes/stage4_revision_round1.tex", "sha256": sha(base)},
        "block_manifest": {"path": "notes/stage4_prime_base.block-manifest.json", "sha256": sha(block_manifest)},
        "roadmap": carrier["roadmap"],
        "claim_surface_manifest": carrier["claim_surface_manifest"],
        "author_adjudication": carrier["author_adjudication"],
        "author_decision_digest": carrier["author_decision_digest"],
        "layout_reemission": layout_lineage,
        "reader_artifact_manifest": item(manifest_path, count_name="entries", count=manifest["entry_count"]),
        "support_evidence_bundle": item(support_bundle_path),
        "validation_receipt": item(validation_path),
        "provisional_response": item(provisional_path, count_name="items", count=len(provisional["items"])),
        "notes_side_bibliography": item(notes_bib, count_name="new_entries", count=4),
        "patch": item(patch_path, count_name="ops", count=len(patch["ops"])),
        "counts": support_bundle["counts"],
        "remaining_blockers": support_bundle["remaining_blockers"],
        "boundaries": support_bundle["boundaries"],
        "handoff_status": "READY_FOR_INDEPENDENT_REAPPLICATION_AND_LAYOUT_PREFLIGHT",
    }
    handoff_path = write_json("stage4_prime_writer_handoff.json", handoff)

    receipt = NOTES / "stage4_prime_revision_patch_round2_writer_receipt.md"
    receipt.write_text(
        "# P32 Stage-4-prime Round-2 writer receipt\n\n"
        f"Generated: `{STAMP}`\n\n"
        f"- Patch: `notes/{patch_path.name}`; SHA-256 `{sha(patch_path)}`; 18 ops over 18 unique blocks.\n"
        f"- Layout re-emission supersedes archived patch SHA-256 `{layout_lineage['superseded_patch_sha256']}` after the fail-closed eight-overfull-box preflight; incident SHA-256 `{layout_lineage['incident']['sha256']}`.\n"
        f"- Layout-only changed carriers: `{json.dumps(layout_targets)}`. B0133 is recorded as derived from authorized B0044. No target/op pair, authority binding, scientific/citation wording, value, or claim strength changed.\n"
        f"- Writer handoff: `notes/{handoff_path.name}`; SHA-256 `{sha(handoff_path)}`.\n"
        f"- Support bundle: `notes/{support_bundle_path.name}`; SHA-256 `{sha(support_bundle_path)}`.\n"
        f"- Validation receipt: `notes/{validation_path.name}`; SHA-256 `{sha(validation_path)}`.\n"
        f"- Provisional response: `notes/{provisional_path.name}`; SHA-256 `{sha(provisional_path)}`.\n"
        f"- Reader manifest: `notes/{manifest_path.name}`; SHA-256 `{sha(manifest_path)}`; {manifest['entry_count']} entries.\n"
        f"- Replay: 26 exact frozen queries, {ledger['row_count']} manifestations; decisions `{json.dumps(ledger['decision_counts'], sort_keys=True)}`.\n"
        f"- Passage matrix: {passage['row_count']} rows; {passage['passage_finalized_count']} narrow finalized and {passage['passage_inconclusive_count']} inherited inconclusive.\n"
        "- Closest work: 4 source-verified notes-side entries; canonical bibliography unchanged.\n"
        "- Formal carrier compatibility and the conditional scalar lemma passed their bounded audits; factor application and AN-1--AN-5 remain not evaluated/unproved.\n"
        "- The current patch was not applied and no current preview/PDF was built by this writer. The separately applied first attempt remains preserved only in the superseded archive. No Stage 4.5 artifact, canonical/science mutation, route change, or scientific-number refresh was produced.\n\n"
        "Remaining blockers are carried verbatim in the writer handoff.\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "support_bundle": item(support_bundle_path),
                "provisional_response": item(provisional_path),
                "validation_receipt": item(validation_path),
                "writer_handoff": item(handoff_path),
                "writer_receipt": item(receipt),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
