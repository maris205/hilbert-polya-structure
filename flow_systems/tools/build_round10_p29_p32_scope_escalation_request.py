#!/usr/bin/env python3
"""Prepare the fail-closed P29/P32 expanded exact-hash authorization request.

This builder is intentionally non-executing: it records the unlisted-target
stop condition, carries the original 36 replace_block pairs forward, adds the
10 stale current-state surfaces, and proves that no Round-3 manuscript patch,
draft, build receipt, or PDF was emitted.
"""

from __future__ import annotations

import copy
import datetime as dt
import hashlib
import json
from pathlib import Path
import re
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OLD_REQUEST = ROOT / "BATCH_ROUND10_STAGE4_5_CORRECTION_AUTHORIZATION_REQUEST_P29_P32.json"
OLD_REQUEST_SHA = "2b8a1c5d57cc01589ca6c926dc5590be0cbe58cae187a0b70d0b4c6c9a6bf3b3"
EXEC_AUTH = ROOT / "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_EXECUTION_AUTHORIZATION_RECEIPT.json"
EXEC_AUTH_SHA = "7fda096bc17ab453ba2defa5301838ebc9e4056e48282f2eef6783aa96381ddf"
INPUT_FREEZE = ROOT / "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_EXECUTION_INPUT_FREEZE.json"
INPUT_FREEZE_SHA = "87ce645eeccbd3a179d05ee48d7abe8c468e1a8f04e9e84cd1ca4037bf95ccff"

INCIDENT = ROOT / "BATCH_ROUND10_P29_P32_STAGE4_PRIME_SCOPE_ESCALATION_INCIDENT.json"
EXPANDED_REQUEST = ROOT / "BATCH_ROUND10_STAGE4_5_CORRECTION_AUTHORIZATION_REQUEST_P29_P32_EXPANDED.json"
EXPANDED_HUMAN = ROOT / "BATCH_ROUND10_STAGE4_5_CORRECTION_AUTHORIZATION_REQUEST_P29_P32_EXPANDED.md"
EXPANDED_VALIDATION = ROOT / "BATCH_ROUND10_STAGE4_5_CORRECTION_AUTHORIZATION_REQUEST_P29_P32_EXPANDED_VALIDATION.json"

STAMP = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

CONFIGS: dict[str, dict[str, Any]] = {
    "P29": {
        "slug": "29-bianchi-ideal-owner-refinement",
        "additional_ids": ["B0004", "B0050", "B0054", "B0090", "B0091"],
        "required_phrases": {
            "B0004": "Because every inherited citation lacks a passage locator",
            "B0050": "all 22 inherited prose citation pairs retain \\texttt{anchor:none}",
            "B0054": "every citation is paired with the same unresolved passage status",
            "B0090": "All 22 paper-specific citation pairs, and all 144 citation pairs in the five-paper batch, lack passage locators",
            "B0091": "No separately authorized field-wide novelty analysis or passage adjudication was performed",
        },
        "reason_by_id": {
            "B0004": "abstract makes a present-tense all-citations locator claim contradicted by completed source finalization",
            "B0050": "methods ceiling gives stale P29 and batch-wide anchor/count/status assertions",
            "B0054": "methods prose gives a stale all-citations unresolved-status assertion",
            "B0090": "limitations prose gives stale P29 and batch-wide no-locator assertions",
            "B0091": "limitations prose says no passage adjudication was performed, which is no longer current after the authorized read-only pass",
        },
        "issue_id": "P29-S45R1-I04",
        "branch": (
            "Replace only the stale locator-count, passage-status, and passage-adjudication clauses in B0004, B0050, B0054, B0090, and B0091 with the exact current split: 13 exact locators finalized and 9 explicit bounded-unavailability records across 22 P29 contexts. Preserve the abstract's no-result boundary, the batch-history context, correction/retraction/conflict limitations, novelty limitations, claim strength, scientific values, Route tuple, and initial-system definition."
        ),
        "expected_summary": {
            "registered_contexts": 22,
            "exact_locators_finalized": 13,
            "prior_bounded_scopes_retained": 0,
            "explicit_bounded_unavailability": 9,
            "passage_bounded_total": 13,
        },
    },
    "P32": {
        "slug": "32-homology-cover-renormalization-uniformity",
        "additional_ids": ["B0006", "B0047", "B0109", "B0128", "B0137"],
        "required_phrases": {
            "B0006": "All 26 inherited citations retain \\texttt{anchor:none}",
            "B0047": "P32-S01--P32-S26 retain \\texttt{anchor:none} and \\texttt{INCONCLUSIVE}",
            "B0109": "preserves \\texttt{INCONCLUSIVE} status for all 26 inherited \\texttt{anchor:none} uses",
            "B0128": "All 26 citations lack passage locators",
            "B0137": "inventories 14 current Stage-4-prime notes sidecars",
        },
        "reason_by_id": {
            "B0006": "abstract makes a present-tense all-inherited-citations anchor claim contradicted by completed source finalization",
            "B0047": "literature section binds the obsolete Round-2 matrix and stale all-26 unresolved state",
            "B0109": "supplement gives the stale all-26 anchorless/INCONCLUSIVE split and pre-finalization synchronization state",
            "B0128": "disclosure section gives a stale all-26 no-locator assertion",
            "B0137": "reader-artifact paragraph gives a current sidecar count and pending-state assertion invalidated by newly created source artifacts",
        },
        "issue_id": "P32-S45R1-I04",
        "branch": (
            "Replace only the stale locator-count/status clauses in B0006, B0047, B0109, and B0128 with the exact current 30-row split: 4 prior bounded closest-work scopes retained, 18 inherited-source exact locators newly finalized, and 8 explicit bounded-unavailability records; update only the artifact inventory/count/status clauses in B0137. Preserve all scientific, falsification-first, arithmetic-gate, disclosure, conflict/retraction, claim-strength, Route, and initial-system boundaries."
        ),
        "expected_summary": {
            "registered_contexts": 30,
            "exact_locators_finalized": 18,
            "prior_bounded_scopes_retained": 4,
            "explicit_bounded_unavailability": 8,
            "passage_bounded_total": 22,
        },
    },
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def binding(path: Path) -> dict[str, Any]:
    return {
        "path": path.relative_to(ROOT).as_posix(),
        "sha256": sha(path),
        "bytes": path.stat().st_size,
    }


def dump(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write(path: Path, value: str) -> None:
    path.write_text(value.rstrip() + "\n", encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def parse_blocks(text: str) -> dict[str, dict[str, Any]]:
    markers = list(re.finditer(r"(?m)^<!--block:(B\d{4})-->\s*$", text))
    rows: dict[str, dict[str, Any]] = {}
    for index, marker in enumerate(markers):
        end = markers[index + 1].start() if index + 1 < len(markers) else len(text)
        value = text[marker.end():end].strip()
        block_id = marker.group(1)
        require(block_id not in rows, f"duplicate block marker: {block_id}")
        rows[block_id] = {
            "block_id": block_id,
            "expected_old_hash": hashlib.sha256(value.encode("utf-8")).hexdigest(),
            "first_line_excerpt": re.sub(r"\s+", " ", value)[:160],
            "allowed_operations": ["replace_block"],
            "full_text": value,
        }
    return rows


def flattened_targets(paper: dict[str, Any]) -> list[dict[str, Any]]:
    return [target for issue in paper["issues"] for target in issue["proposed_targets"]]


def verify_frozen_paper(entry: dict[str, Any]) -> list[dict[str, Any]]:
    frozen = [
        entry["current_working_draft"],
        entry["current_working_bibliography"],
        entry["available_block_manifest"],
        *entry["canonical_files"],
        *entry["science_files"],
        entry["initial_system_source"],
        entry["route_crosswalk"],
    ]
    for row in frozen:
        path = ROOT / row["path"]
        require(path.exists(), f"frozen path missing: {row['path']}")
        require(sha(path) == row["sha256"], f"frozen hash drift: {row['path']}")
        require(path.stat().st_size == row["bytes"], f"frozen byte drift: {row['path']}")
    return frozen


def future_support_operations(slug: str) -> list[dict[str, str]]:
    prefix = f"papers/{slug}/notes/"
    return [
        {"path": prefix + "stage4_prime_source_finalization_round3.json", "operation": "consume_immutable_input"},
        {"path": prefix + "stage4_prime_claim_passage_matrix_round3.json", "operation": "consume_immutable_input"},
        {"path": prefix + "stage4_prime_source_finalization_round3_validation.json", "operation": "consume_immutable_input"},
        {"path": prefix + "stage4_prime_revision_patch_round3.json", "operation": "create_file"},
        {"path": prefix + "stage4_prime_revision_round3.tex", "operation": "create_file"},
        {"path": prefix + "stage4_prime_revision_evidence_bundle_round3.json", "operation": "create_file"},
        {"path": prefix + "stage4_prime_response_to_reviewers_round3.json", "operation": "create_file"},
        {"path": prefix + "stage4_prime_revision_round3.pdf", "operation": "create_file"},
        {"path": prefix + "stage4_prime_revision_round3_build_receipt.json", "operation": "create_file"},
        {"path": f"papers/{slug}/README.md", "operation": "append_progress_only"},
    ]


def main() -> int:
    for path, expected in [
        (OLD_REQUEST, OLD_REQUEST_SHA),
        (EXEC_AUTH, EXEC_AUTH_SHA),
        (INPUT_FREEZE, INPUT_FREEZE_SHA),
    ]:
        require(path.exists(), f"authority missing: {path.name}")
        require(sha(path) == expected, f"authority digest mismatch: {path.name}")

    old_request = json.loads(OLD_REQUEST.read_text(encoding="utf-8"))
    freeze = json.loads(INPUT_FREEZE.read_text(encoding="utf-8"))
    old_by_id = {paper["paper_id"]: paper for paper in old_request["papers"]}
    freeze_by_id = {paper["paper_id"]: paper for paper in freeze["papers"]}
    require(set(CONFIGS) <= set(old_by_id), "old request paper missing")
    require(set(CONFIGS) <= set(freeze_by_id), "input-freeze paper missing")

    expanded_papers: list[dict[str, Any]] = []
    incident_papers: list[dict[str, Any]] = []
    all_frozen_rows: list[dict[str, Any]] = []

    for paper_id, cfg in CONFIGS.items():
        old_paper = old_by_id[paper_id]
        freeze_paper = freeze_by_id[paper_id]
        all_frozen_rows.extend(verify_frozen_paper(freeze_paper))

        draft = ROOT / freeze_paper["current_working_draft"]["path"]
        bib = ROOT / freeze_paper["current_working_bibliography"]["path"]
        blocks = parse_blocks(draft.read_text(encoding="utf-8"))
        original_targets = flattened_targets(old_paper)
        original_ids = [target["block_id"] for target in original_targets]
        require(len(original_ids) == len(set(original_ids)), f"{paper_id}: duplicate original target")
        for target in original_targets:
            block_id = target["block_id"]
            require(block_id in blocks, f"{paper_id}: original target missing: {block_id}")
            require(target["allowed_operations"] == ["replace_block"], f"{paper_id}: original op drift")
            require(
                target["expected_old_hash"] == blocks[block_id]["expected_old_hash"],
                f"{paper_id}: original old hash mismatch: {block_id}",
            )

        additional_targets = []
        for block_id in cfg["additional_ids"]:
            require(block_id not in original_ids, f"{paper_id}: additional target overlaps original: {block_id}")
            require(block_id in blocks, f"{paper_id}: additional target missing: {block_id}")
            phrase = cfg["required_phrases"][block_id]
            normalized_block = re.sub(r"\s+", " ", blocks[block_id]["full_text"])
            require(phrase in normalized_block, f"{paper_id}: stale phrase absent: {block_id}")
            row = {key: value for key, value in blocks[block_id].items() if key != "full_text"}
            row.update(
                {
                    "required_reason": cfg["reason_by_id"][block_id],
                    "stale_current_fact_excerpt": phrase,
                }
            )
            additional_targets.append(row)

        notes = ROOT / "papers" / cfg["slug"] / "notes"
        source_path = notes / "stage4_prime_source_finalization_round3.json"
        matrix_path = notes / "stage4_prime_claim_passage_matrix_round3.json"
        validation_path = notes / "stage4_prime_source_finalization_round3_validation.json"
        for path in [source_path, matrix_path, validation_path]:
            require(path.exists(), f"{paper_id}: source-finalization artifact missing: {path.name}")
        source = json.loads(source_path.read_text(encoding="utf-8"))
        source_validation = json.loads(validation_path.read_text(encoding="utf-8"))
        require(source_validation["verdict"] == "PASS", f"{paper_id}: source validation did not pass")
        require(source["summary"] == {**cfg["expected_summary"], "manuscript_patch_applied": False}, f"{paper_id}: source summary mismatch")
        require(all(not row["locator_guessed"] for row in source["rows"]), f"{paper_id}: guessed locator present")
        require(all(not row["manuscript_patch_applied"] for row in source["rows"]), f"{paper_id}: source row claims patch")

        expanded_paper = copy.deepcopy(old_paper)
        new_issue = {
            "issue_id": cfg["issue_id"],
            "severity": "SCOPE_BLOCKING",
            "implementation_branch": cfg["branch"],
            "proposed_author_triage": "will_address",
            "proposed_targets": additional_targets,
        }
        expanded_paper["issues"].append(new_issue)
        expanded_ids = original_ids + cfg["additional_ids"]
        expanded_paper["blocking_issue_count"] = len(expanded_paper["issues"])
        expanded_paper["unique_target_blocks"] = len(set(expanded_ids))
        expanded_paper["block_operation_pairs"] = len(expanded_ids)
        expanded_paper["completed_read_only_source_finalization"] = binding(source_path)
        expanded_paper["completed_read_only_claim_passage_matrix"] = binding(matrix_path)
        expanded_paper["completed_read_only_source_validation"] = binding(validation_path)
        expanded_paper["scope_expansion"] = {
            "original_authorized_pairs": len(original_ids),
            "additional_required_pairs": len(cfg["additional_ids"]),
            "expanded_requested_pairs": len(expanded_ids),
            "additional_block_ids": cfg["additional_ids"],
        }
        expanded_paper["supporting_operations_after_new_authorization"] = future_support_operations(cfg["slug"])
        expanded_paper.pop("supporting_operations_after_authorization", None)
        expanded_papers.append(expanded_paper)

        incident_papers.append(
            {
                "paper_id": paper_id,
                "current_draft": binding(draft),
                "current_bibliography": binding(bib),
                "source_finalization": binding(source_path),
                "claim_passage_matrix": binding(matrix_path),
                "source_validation": binding(validation_path),
                "source_summary": cfg["expected_summary"],
                "original_authorized_replace_block_pairs": len(original_ids),
                "additional_unlisted_targets_required": additional_targets,
                "additional_count": len(additional_targets),
                "expanded_required_replace_block_pairs": len(expanded_ids),
            }
        )

    retained_incidents = [
        ROOT / "papers/29-bianchi-ideal-owner-refinement/notes/stage4_prime_p29_p32_source_finalization_round3_incident_001.json",
        ROOT / "papers/29-bianchi-ideal-owner-refinement/notes/stage4_prime_p29_p32_source_finalization_round3_incident_002.json",
        ROOT / "papers/29-bianchi-ideal-owner-refinement/notes/stage4_prime_p29_p32_source_finalization_round3_incident_003.json",
        ROOT / "BATCH_ROUND10_P29_P32_STAGE4_PRIME_SCOPE_REQUEST_PREP_INCIDENT_001.json",
    ]
    require(all(path.exists() for path in retained_incidents), "retained fail-closed source incident missing")

    prohibited_outputs = []
    for cfg in CONFIGS.values():
        notes = ROOT / "papers" / cfg["slug"] / "notes"
        prohibited_outputs.extend(
            [
                notes / "stage4_prime_revision_patch_round3.json",
                notes / "stage4_prime_revision_round3.tex",
                notes / "stage4_prime_revision_round3.pdf",
                notes / "stage4_prime_revision_round3_build_receipt.json",
                notes / "stage4_prime_revision_evidence_bundle_round3.json",
                notes / "stage4_prime_response_to_reviewers_round3.json",
            ]
        )
    require(all(not path.exists() for path in prohibited_outputs), "prohibited Round-3 execution output already exists")

    incident = {
        "schema_version": "round10-p29-p32-stage4-prime-scope-escalation-incident/1.0",
        "recorded_at_utc": STAMP,
        "status": "FAIL_CLOSED_AWAITING_EXPANDED_EXACT_AUTHORIZATION",
        "triggered_stop_condition": "any target or operation outside this request is required",
        "detection_phase": "after authorized read-only source finalization and before manuscript patch emission or application",
        "classification": (
            "The additional surfaces are present-tense/current factual claims. They are not explicit historical pre-correction snapshots; adding a later supersession sentence would leave internal contradictions."
        ),
        "authority_at_detection": [binding(OLD_REQUEST), binding(EXEC_AUTH), binding(INPUT_FREEZE)],
        "papers": incident_papers,
        "totals": {
            "original_authorized_replace_block_pairs": 36,
            "additional_unlisted_targets_required": 10,
            "expanded_required_replace_block_pairs": 46,
            "source_contexts_finalized_or_bounded": 52,
            "exact_locators_newly_finalized": 31,
            "prior_bounded_scopes_retained": 4,
            "explicit_bounded_unavailability": 17,
            "passage_bounded_total": 35,
        },
        "retained_fail_closed_source_incidents": [binding(path) for path in retained_incidents],
        "execution_observations": {
            "manuscript_patch_emitted": False,
            "manuscript_patch_applied": False,
            "round3_draft_created": False,
            "round3_pdf_created": False,
            "round3_build_run": False,
            "bibliography_mutation": False,
            "canonical_science_result_route_or_initial_system_mutation": False,
            "stage4_5_rerun": False,
        },
        "frozen_boundary_reverification": all_frozen_rows,
        "required_next_checkpoint": "new exact-hash author confirmation covering all 46 replace_block pairs",
    }
    dump(INCIDENT, incident)

    expanded_request = {
        "schema_version": "round10-stage4.5-correction-authorization-request-p29-p32-expanded/1.0",
        "generated_at_utc": STAMP,
        "status": "AWAITING_EXPLICIT_AUTHOR_CONFIRMATION",
        "supersession_scope": (
            "If confirmed, this request supersedes the old 36-pair request only for future P29/P32 manuscript correction execution. The completed read-only source-finalization artifacts remain immutable inputs."
        ),
        "authorization_lineage": [binding(OLD_REQUEST), binding(EXEC_AUTH), binding(INPUT_FREEZE)],
        "scope_escalation_incident": binding(INCIDENT),
        "proposed_display_order": old_request["proposed_display_order"],
        "proposed_author_triage": old_request["proposed_author_triage"],
        "proposed_revision_round": old_request["proposed_revision_round"],
        "papers": expanded_papers,
        "totals": {
            "papers": 2,
            "blocking_issues": sum(paper["blocking_issue_count"] for paper in expanded_papers),
            "original_authorized_replace_block_pairs": 36,
            "additional_required_replace_block_pairs": 10,
            "unique_target_blocks": 46,
            "block_operation_pairs": 46,
            "registered_citation_contexts": 52,
            "exact_locators_newly_finalized": 31,
            "prior_bounded_scopes_retained": 4,
            "explicit_bounded_unavailability": 17,
            "passage_bounded_total": 35,
        },
        "confirmation_effect": (
            "After the SHA-256 of this JSON is presented, one unqualified author confirmation authorizes only the 46 exact replace_block pairs and named future supporting operations in this request."
        ),
        "boundaries": {
            "request_preparation_only_now": True,
            "patch_application_now": False,
            "bibliography_mutation": False,
            "canonical_or_science_result_mutation": False,
            "scientific_execution_or_result_refresh": False,
            "stage4_5_rerun": False,
            "stage5_or_stage6": False,
            "route_or_initial_system_mutation": False,
            "registered_claim_strength_replacement": False,
            "citation_style": "plainnat numeric",
        },
        "stop_conditions_for_later_execution": old_request["stop_conditions_for_later_execution"],
    }
    dump(EXPANDED_REQUEST, expanded_request)

    lines = [
        "# Round 10 P29/P32 — expanded exact Stage 4.5 correction authorization request",
        "",
        "Status: **AWAITING EXPLICIT AUTHOR CONFIRMATION. No manuscript patch has been emitted or applied.**",
        "",
        f"Machine request: `{EXPANDED_REQUEST.name}` SHA-256 `{sha(EXPANDED_REQUEST)}`.",
        "",
        "The authorized read-only source pass completed, but it made ten additional present-tense locator/count/status surfaces stale. Because those blocks were absent from the original 36-pair request, the unlisted-target stop condition fired before patch emission. This request carries the original 36 pairs forward and adds exactly those ten blocks.",
        "",
        "Source outcome: P29 = 13 exact locators + 9 explicit bounded-unavailability records; P32 = 18 newly exact locators + 4 retained bounded scopes + 8 explicit bounded-unavailability records. Overall = 35 passage-bounded + 17 explicitly unavailable across 52 contexts.",
        "",
    ]
    for paper in expanded_papers:
        lines.extend([f"## {paper['paper_id']}", ""])
        for issue in paper["issues"]:
            lines.append(f"### `{issue['issue_id']}` — {issue['severity']}")
            lines.append("")
            lines.append(issue["implementation_branch"])
            lines.append("")
            for target in issue["proposed_targets"]:
                lines.append(
                    f"- `{target['block_id']}` / `replace_block` / expected old SHA-256 `{target['expected_old_hash']}`"
                )
            lines.append("")
    lines.extend(
        [
            "## Confirmation boundary",
            "",
            "A short unqualified confirmation after presentation of the machine-request SHA authorizes only these 46 exact `replace_block` pairs and the named per-paper Round-3 support outputs. It does not authorize Bib changes, canonical/science/result changes, a Stage 4.5 rerun, claim strengthening, Route changes, or initial-system changes.",
        ]
    )
    write(EXPANDED_HUMAN, "\n".join(lines))

    checks: list[dict[str, str]] = []

    def check(check_id: str, condition: bool, detail: str) -> None:
        checks.append({"check_id": check_id, "status": "PASS" if condition else "FAIL", "detail": detail})

    expanded_by_id = {paper["paper_id"]: paper for paper in expanded_papers}
    check("V001", sha(OLD_REQUEST) == OLD_REQUEST_SHA, "original exact request digest")
    check("V002", sha(EXEC_AUTH) == EXEC_AUTH_SHA, "execution authorization receipt digest")
    check("V003", sha(INPUT_FREEZE) == INPUT_FREEZE_SHA, "execution input-freeze digest")
    check("V004", incident["totals"]["additional_unlisted_targets_required"] == 10, "five P29 plus five P32 additional blocks")
    check("V005", expanded_request["totals"]["block_operation_pairs"] == 46, "36 carried pairs plus 10 added pairs")
    check("V006", expanded_request["totals"]["unique_target_blocks"] == 46, "all expanded targets are unique within the two-paper scope")
    check("V007", sum(len(flattened_targets(p)) for p in expanded_papers) == 46, "serialized target count")
    check(
        "V008",
        all(target["allowed_operations"] == ["replace_block"] for paper in expanded_papers for target in flattened_targets(paper)),
        "replace_block is the only manuscript operation",
    )
    check(
        "V009",
        all(
            old_by_id[paper_id]["issues"] == expanded_by_id[paper_id]["issues"][: len(old_by_id[paper_id]["issues"])]
            for paper_id in CONFIGS
        ),
        "all original issues and 36 target records carried byte-semantically unchanged",
    )
    check(
        "V010",
        all(
            set(CONFIGS[paper_id]["additional_ids"]).isdisjoint(
                {target["block_id"] for target in flattened_targets(old_by_id[paper_id])}
            )
            for paper_id in CONFIGS
        ),
        "additional targets do not overlap original targets",
    )
    check("V011", expanded_request["totals"]["registered_citation_contexts"] == 52, "22 P29 plus 30 P32 contexts")
    check("V012", expanded_request["totals"]["passage_bounded_total"] == 35, "31 newly exact plus 4 retained bounded scopes")
    check("V013", expanded_request["totals"]["explicit_bounded_unavailability"] == 17, "9 P29 plus 8 P32 explicit unavailable records")
    check(
        "V014",
        all(
            json.loads((ROOT / p["completed_read_only_source_validation"]["path"]).read_text(encoding="utf-8"))["verdict"] == "PASS"
            for p in expanded_papers
        ),
        "both source-finalization validations pass",
    )
    check(
        "V015",
        all(sha(ROOT / row["path"]) == row["sha256"] for row in all_frozen_rows),
        "P29/P32 draft, Bib, manifest, canonical, science, initial-system, and Route files remain frozen",
    )
    check("V016", all(not path.exists() for path in prohibited_outputs), "no Round-3 patch/draft/PDF/build/evidence/response output exists")
    check(
        "V017",
        expanded_request["boundaries"]["patch_application_now"] is False
        and expanded_request["boundaries"]["stage4_5_rerun"] is False,
        "request preparation remains non-executing",
    )
    check("V018", expanded_request["boundaries"]["citation_style"] == "plainnat numeric", "citation style boundary retained")
    check(
        "V019",
        all(
            target["expected_old_hash"]
            == parse_blocks((ROOT / expanded_by_id[paper_id]["current_stage4_prime_draft"]["path"]).read_text(encoding="utf-8"))[target["block_id"]]["expected_old_hash"]
            for paper_id in CONFIGS
            for target in flattened_targets(expanded_by_id[paper_id])
        ),
        "all 46 expected old block hashes rebound to the current Round-2 drafts",
    )
    check("V020", incident["execution_observations"]["manuscript_patch_emitted"] is False, "scope escalation recorded before patch emission")

    validation = {
        "schema_version": "round10-stage4.5-correction-authorization-request-p29-p32-expanded-validation/1.0",
        "generated_at_utc": STAMP,
        "request": binding(EXPANDED_REQUEST),
        "human_request": binding(EXPANDED_HUMAN),
        "scope_escalation_incident": binding(INCIDENT),
        "checks": checks,
        "passed": sum(row["status"] == "PASS" for row in checks),
        "failed": sum(row["status"] == "FAIL" for row in checks),
        "verdict": "PASS" if all(row["status"] == "PASS" for row in checks) else "FAIL",
    }
    dump(EXPANDED_VALIDATION, validation)
    require(validation["verdict"] == "PASS", "expanded request validation failed")

    print(
        json.dumps(
            {
                "status": "PASS_AWAITING_AUTHOR_CONFIRMATION",
                "incident": binding(INCIDENT),
                "expanded_request": binding(EXPANDED_REQUEST),
                "human_request": binding(EXPANDED_HUMAN),
                "validation": binding(EXPANDED_VALIDATION),
                "totals": expanded_request["totals"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
