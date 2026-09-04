#!/usr/bin/env python3
"""Build P30/P31 Round-10 Stage-4-prime scope-reissue writer artifacts.

The ``prepare`` phase creates the fresh roadmap, empty registered-claim
surface manifest, and explicit author-choice input.  The official ARS
``revision_roadmap.py build-adjudication`` command must create the adjudication.
The ``emit`` phase then creates and validates a patch but never applies it.
This script never changes a matrix, bibliography, README, canonical file,
scientific result, Route record, or initial-system record.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
ARS_ROOT = Path(
    "/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/skills/"
    "academic-research-suite/ars"
)
sys.path.insert(0, str(ARS_ROOT / "scripts"))

from _block_parser import parse_document  # noqa: E402
import revision_roadmap as rr  # noqa: E402


RECEIPT = ROOT / "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_EXECUTION_AUTHORIZATION_RECEIPT.json"
FREEZE = ROOT / "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_EXECUTION_INPUT_FREEZE.json"
REQUEST = ROOT / "BATCH_ROUND10_STAGE4_PRIME_EXPANDED_CORRECTION_AUTHORIZATION_REQUEST_P30_P31.json"
EXPECTED_ROOT_HASHES = {
    RECEIPT: "b154d92f84487b381b50e2e9addb5aecd924c6d9d2fb2277d6604a5cb42a17d1",
    FREEZE: "e835f073d785fbad2de809fcf44dd24bc4abf98300ed21857d3b5e9f67751ce4",
    REQUEST: "9fecba23da5ea90f3c8f252d0a7fbd019d042f600dbeaa320167865273692135",
}
AUTHOR_EVENT_SHA256 = "111505020ac13b92ac253361e21777de8343455edd9ed3a4436fe924600cb812"
AUTHOR_EVENT_ID = "AUTHOR-EVENT-20260904-ROUND10-STAGE4-PRIME-SCOPE-REISSUE-P30-P31"
REVISION_ROUND = 3
P30_INITIAL_PATCH_SHA256 = "2cdad8744f56dcb3f7ed46dd0be9f8fa203bbd67c1c3cd224d620a60e273a649"
P30_ALLOWBREAK_PATCH_SHA256 = "f99ad6f18eb1bc1941bcaadd1a8c33fcb60b0d399479db2ca9c1d590dc4c42b6"
P30_ALLOWBREAK_INCIDENT_SHA256 = "6bec307f6850d3db09977ae3d7018c545ce398773f9394d4e5fdb7612017719c"
P31_INITIAL_PATCH_SHA256 = "b02be96f6d6793ad67e3b3cee48a384dbcf409852fbfde5e6de0a88919d4580c"
P30_CONTEXT_BOUND_PATCH_SHA256 = "658784eb249cb39c1ece3265ef0782c27bf4efa09fd59c1b3c253e2d0bf87d60"
P31_CONTEXT_BOUND_PATCH_SHA256 = "79bfa868cdc9e62cec22ce11c1a42eba5493c18808a6e6b1a9b03bb119bd771f"
P30_CONTEXT_SEMANTIC_PREFLIGHT_SHA256 = "0737db6ea98cf583066cd06d6b7bf9d63a2958686b3bcddb5e23d3c7259c0ad8"
P31_CONTEXT_SEMANTIC_PREFLIGHT_SHA256 = "5562806f58a134600533bc6da9afd9881e29265493e5d622b985a49b3652e04f"
P30_CONTEXT_LAYOUT_INCIDENT_SHA256 = "ab6cab07a825e347b36df05c83a4caf8fe164b91f51ecebdf18267c7e5c929bb"
P30_CONTEXT_ROOT_LAYOUT_RECEIPT_SHA256 = "bdbb4018f9bf747e5e72c26da57f3fe4bcc2d0c5da293d95399da99b7abc357c"
P30_COHERENCE_PARTIAL_PATCH_SHA256 = "8d8c209bec0c639878b63b7faffcbafafcb1dfe46967cf69b790217e6b1a365b"
P30_COHERENCE_PARTIAL_INCIDENT_SHA256 = "b6b11b8579ac598743e958c83928843ba08e63e6ec7ed45416c8058fd0c5abb5"
PAPERS = {
    "P30": {"slug": "30-three-disk-nonconstant-roof-determinant", "ops": 34, "matrix_kind": "claim-passage"},
    "P31": {"slug": "31-level11-conjugacy-owner-ledger", "ops": 13, "matrix_kind": "method-passage"},
}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def file_digest(path: Path) -> str:
    return digest(path.read_bytes())


def load_json(path: Path) -> tuple[dict, bytes]:
    raw = path.read_bytes()
    return json.loads(raw), raw


def encoded_json(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
        os.replace(temp_name, path)
    except BaseException:
        if os.path.exists(temp_name):
            os.unlink(temp_name)
        raise


def ensure(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def ensure_hash(path: Path, expected: str) -> None:
    ensure(path.is_file(), f"missing frozen artifact: {path.relative_to(ROOT)}")
    actual = file_digest(path)
    ensure(actual == expected, f"hash mismatch: {path.relative_to(ROOT)} expected={expected} actual={actual}")


def timestamp() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def artifact(path: Path) -> dict:
    raw = path.read_bytes()
    return {"path": str(path.relative_to(ROOT)), "sha256": digest(raw), "bytes": len(raw)}


def latex_plain(value: str) -> str:
    ensure("\\" not in value, f"unexpected backslash in frozen prose field: {value!r}")
    replacements = {"&": r"\&", "%": r"\%", "#": r"\#", "_": r"\_"}
    return "".join(replacements.get(char, char) for char in value)


def cite_keys(text: str) -> set[str]:
    keys: set[str] = set()
    for match in re.finditer(r"\\cite[tp]?\{([^}]+)\}", text):
        keys.update(value.strip() for value in match.group(1).split(",") if value.strip())
    return keys


def replace_once(text: str, old: str, new: str, label: str) -> str:
    ensure(text.count(old) == 1, f"{label}: stale surface is not exact-once")
    return text.replace(old, new, 1)


def output_paths(base_path: Path) -> dict[str, Path]:
    notes = base_path.parent
    return {
        "roadmap": notes / "stage4_prime_correction_round3_revision_roadmap.json",
        "claim_surface": notes / "stage4_prime_correction_round3_claim_surface_manifest.json",
        "author_choices": notes / "stage4_prime_correction_round3_author_choices.json",
        "author_adjudication": notes / "stage4_prime_correction_round3_author_adjudication.json",
        "patch": notes / "stage4_prime_revision_patch_round3.json",
        "handoff": notes / "stage4_prime_correction_round3_writer_handoff.json",
        "response_json": notes / "stage4_prime_response_to_reviewers_provisional_round3.json",
        "response_md": notes / "stage4_prime_response_to_reviewers_provisional_round3.md",
        "revision_log": notes / "stage4_prime_revision_log_round3.md",
        "validation": notes / "stage4_prime_correction_round3_writer_validation_receipt.json",
        "matrix_plan": notes / "stage4_prime_correction_round3_matrix_regeneration_plan.json",
        "layout_incident": notes / "stage4_prime_correction_round3_layout_preflight_incident.json",
        "semantic_preflight": notes / "stage4_prime_correction_round3_semantic_preflight_lineage.json",
    }


def load_context() -> dict:
    for path, expected in EXPECTED_ROOT_HASHES.items():
        ensure_hash(path, expected)
    receipt, _ = load_json(RECEIPT)
    freeze, _ = load_json(FREEZE)
    request, _ = load_json(REQUEST)
    ensure(receipt["author_event"]["sha256"] == AUTHOR_EVENT_SHA256, "receipt author-event mismatch")
    ensure(receipt["tracks"]["P30_P31"]["sha256"] == EXPECTED_ROOT_HASHES[REQUEST], "receipt request mismatch")
    ensure(receipt["tracks"]["P30_P31"]["replace_block_pairs"] == 47, "receipt target count mismatch")
    ensure(freeze["author_event"]["sha256"] == AUTHOR_EVENT_SHA256, "freeze author-event mismatch")
    ensure(request["totals"]["expanded_block_operation_pairs"] == 47, "request operation count mismatch")
    ensure(request["totals"]["unique_target_blocks"] == 47, "request unique-target count mismatch")
    ensure(request["requested_authorization"]["bibliography_operations"] == 0, "bibliography operation appeared")
    frozen_by_id = {value["paper_id"]: value for value in freeze["papers"]}
    requested_by_id = {value["paper_id"]: value for value in request["papers"]}
    result = {"receipt": receipt, "freeze": freeze, "request": request, "papers": {}}
    for paper_id, config in PAPERS.items():
        frozen = frozen_by_id[paper_id]
        requested = requested_by_id[paper_id]
        ensure(requested["expanded_target_count"] == config["ops"], f"{paper_id}: expanded count mismatch")
        ensure(len(requested["all_requested_targets"]) == config["ops"], f"{paper_id}: target array mismatch")
        ensure(frozen["authorized_unique_replace_block_pairs"] == config["ops"], f"{paper_id}: freeze count mismatch")
        frozen_records = [
            frozen["current_working_draft"], frozen["current_working_bibliography"],
            frozen["block_manifest"], frozen["initial_system_source"],
            frozen["route_crosswalk"], frozen["authorized_in_place_matrix_regeneration"],
            *frozen["canonical_files"], *frozen.get("science_files", []),
        ]
        for record in frozen_records:
            bound_path = ROOT / record["path"]
            ensure_hash(bound_path, record["sha256"])
            ensure(bound_path.stat().st_size == record["bytes"], f"{paper_id}: byte count mismatch for {record['path']}")
        base_path = ROOT / frozen["current_working_draft"]["path"]
        bib_path = ROOT / frozen["current_working_bibliography"]["path"]
        manifest_path = ROOT / frozen["block_manifest"]["path"]
        matrix_path = ROOT / frozen["authorized_in_place_matrix_regeneration"]["path"]
        source_path = ROOT / requested["frozen_source_finalization"]["path"]
        ensure_hash(source_path, requested["frozen_source_finalization"]["sha256"])
        ensure_hash(base_path, requested["current_stage4_prime_draft"]["sha256"])
        ensure_hash(bib_path, requested["current_stage4_prime_bibliography"]["sha256"])
        ensure_hash(matrix_path, requested["matrix_regeneration"]["expected_current_sha256"])
        ensure(not (ROOT / requested["requested_new_versioned_draft"]["path"]).exists(), f"{paper_id}: successor draft already exists")
        base_raw = base_path.read_bytes()
        parsed = parse_document(base_raw.decode("utf-8"))
        blocks = parsed.block_by_id()
        manifest, manifest_raw = load_json(manifest_path)
        manifest_blocks = {value["block_id"]: value for value in manifest["blocks"]}
        ensure(manifest["base_draft_hash"] == digest(base_raw)[:12], f"{paper_id}: manifest base mismatch")
        ensure(set(manifest_blocks) == set(blocks), f"{paper_id}: manifest population mismatch")
        for block_id, block in blocks.items():
            ensure(manifest_blocks[block_id]["old_hash"] == block.norm_hash, f"{paper_id}/{block_id}: manifest old hash mismatch")
        target_ids = [value["block_id"] for value in requested["all_requested_targets"]]
        ensure(len(target_ids) == len(set(target_ids)), f"{paper_id}: duplicate target")
        for target in requested["all_requested_targets"]:
            block_id = target["block_id"]
            ensure(target["allowed_operations"] == ["replace_block"], f"{paper_id}/{block_id}: unauthorized operation")
            ensure(block_id in blocks, f"{paper_id}/{block_id}: target absent")
            block = blocks[block_id]
            ensure(target["parser_norm_hash"] == block.norm_hash, f"{paper_id}/{block_id}: short hash mismatch")
            ensure(target["expected_old_hash"] == digest(block.normalized_text.encode()), f"{paper_id}/{block_id}: full hash mismatch")
        source_finalization, _ = load_json(source_path)
        rows = source_finalization["rows"]
        available = sum(value["finalization_status"] == "EXACT_LOCATOR_AVAILABLE_FOR_AUTHORIZED_LATER_REPLACEMENT" for value in rows)
        unavailable = sum(value["finalization_status"] == "EXPLICIT_BOUNDED_PASSAGE_UNAVAILABILITY" for value in rows)
        ensure(len(rows) == requested["frozen_source_finalization"]["rows"], f"{paper_id}: source row count mismatch")
        ensure(available == requested["frozen_source_finalization"]["locator_available"], f"{paper_id}: available count mismatch")
        ensure(unavailable == requested["frozen_source_finalization"]["explicit_bounded_unavailability"], f"{paper_id}: unavailable count mismatch")
        proposal_path = ROOT / f"papers/{config['slug']}/notes/stage4_5_round1_stage4_prime_correction_authorization_proposal.json"
        proposal, _ = load_json(proposal_path)
        issues = {value["issue_id"]: value for value in proposal["issues"]}
        new_issue = requested["new_scope_closure_issue"]
        issues[new_issue["issue_id"]] = new_issue
        issue_order: list[str] = []
        for target in requested["all_requested_targets"]:
            if target["issue_id"] not in issue_order:
                issue_order.append(target["issue_id"])
        ensure(set(issue_order) == set(issues), f"{paper_id}: issue population mismatch")
        result["papers"][paper_id] = {
            "config": config, "frozen": frozen, "requested": requested,
            "base_path": base_path, "base_raw": base_raw, "blocks": blocks,
            "bib_path": bib_path, "manifest_path": manifest_path,
            "manifest": manifest, "manifest_raw": manifest_raw,
            "manifest_blocks": manifest_blocks, "matrix_path": matrix_path,
            "source_path": source_path, "source_finalization": source_finalization,
            "proposal_path": proposal_path, "issues": issues, "issue_order": issue_order,
        }
    return result


def make_roadmap(paper_id: str, paper: dict) -> dict:
    items = []
    targets = paper["requested"]["all_requested_targets"]
    for ordinal, source_issue_id in enumerate(paper["issue_order"], 1):
        issue = paper["issues"][source_issue_id]
        selected = [value for value in targets if value["issue_id"] == source_issue_id]
        proposed = [{"block_id": value["block_id"], "allowed_operations": value["allowed_operations"]} for value in selected]
        locator = ", ".join(value["block_id"] for value in selected)
        items.append({
            "id": f"REV-{source_issue_id}",
            "source_refs": [{"seat": "EIC", "channel": "editorial", "ordinal": ordinal, "subclaim_ordinal": 0}],
            "description": issue["finding"],
            "reviewer": "Stage 4.5 integrity gate via the expanded scope-reissue request",
            "source_kind": "editorial",
            "obligation_class": "must_fix",
            "cost_scope": {"kind": "section", "locator": locator},
            "consequence_if_unaddressed": {
                "code": "reader_traceability_reduced" if issue["phase"].startswith("B/E") else "reporting_requirement_unmet",
                "target": {"kind": "section", "locator": locator},
            },
            "target_section": locator,
            "suggested_action": issue["implementation_rule"],
            "consensus_level": "SINGLE-VERIFIER",
            "verification_criteria": (
                "Apply every listed target exactly once with replace_block, obey every request "
                "constraint and semantic branch, preserve claim strength and transfer boundaries, "
                "and stop on any hash, scope, or structural mismatch."
            ),
            "proposed_targets": proposed,
        })
    return {
        "schema_version": "revision-roadmap/1.0",
        "revision_round": REVISION_ROUND,
        "base_draft_sha256": digest(paper["base_raw"]),
        "block_manifest_sha256": digest(paper["manifest_raw"]),
        "items": items,
        "total_items": len(items),
        "obligation_counts": {"must_fix": len(items), "should_fix": 0, "consider": 0},
        "editorial_decision": "Major Revision",
        "consensus_summary": f"The expanded request identifies {len(items)} fail-closed correction blockers for {paper_id}; request order and exact proposed targets are preserved.",
        "dissenting_opinions": [],
    }


def prepare() -> None:
    context = load_context()
    for paper_id, paper in context["papers"].items():
        paths = output_paths(paper["base_path"])
        for key in ("author_adjudication", "patch", "handoff", "response_json", "response_md", "revision_log", "validation", "matrix_plan"):
            ensure(not paths[key].exists(), f"prepare refuses existing artifact: {paths[key].relative_to(ROOT)}")
        roadmap = make_roadmap(paper_id, paper)
        roadmap_raw = encoded_json(roadmap)
        atomic_write(paths["roadmap"], roadmap_raw)
        claim_surface = {
            "schema_version": "claim-surface-manifest/1.0",
            "revision_round": REVISION_ROUND,
            "roadmap_sha256": digest(roadmap_raw),
            "base_draft_sha256": digest(paper["base_raw"]),
            "claim_intent_sources": [], "surfaces": [],
        }
        atomic_write(paths["claim_surface"], encoded_json(claim_surface))
        item_ids = [value["id"] for value in roadmap["items"]]
        choices = {
            "schema_version": "author-adjudication-input/1.0",
            "author_events": [{
                "event_id": AUTHOR_EVENT_ID, "source": "explicit_session_user_message",
                "actor_role": "author", "input_sha256": AUTHOR_EVENT_SHA256,
            }],
            "display_order": {"mode": "source_traceability", "item_ids": item_ids, "author_event_id": AUTHOR_EVENT_ID},
            "author_adjudications": [{
                "item_id": item["id"], "author_event_id": AUTHOR_EVENT_ID,
                "author_triage": "will_address", "authorized_targets": item["proposed_targets"],
                "claim_strength_authorizations": [],
            } for item in roadmap["items"]],
            "collateral_authorizations": [],
        }
        atomic_write(paths["author_choices"], encoded_json(choices))
        print(f"PREPARED {paper_id} items={len(items) if (items := roadmap['items']) else 0} roadmap={digest(roadmap_raw)} claim_surface={file_digest(paths['claim_surface'])}")


def source_row_text(row: dict) -> str:
    source_id = row["source_id"]
    role = latex_plain(row["registered_role"])
    scope = latex_plain(row["hypothesis_or_scope"])
    boundary = latex_plain(row["transfer_boundary_preserved"])
    context_id = row["context_id"]
    status = row["finalization_status"]
    if status == "EXACT_LOCATOR_AVAILABLE_FOR_AUTHORIZED_LATER_REPLACEMENT":
        locator = latex_plain(row["exact_passage_locator"])
        encoded_locator = quote(row["exact_passage_locator"], safe="")
        return "\n".join([
            f"The bounded source-finalization record for \\citep{{{source_id}}} identifies",
            f"the exact locator ``{locator}''.  The retained excerpt supplies only the",
            "bounded context recorded for that locator; it is not treated as proof of the",
            f"registered role in full.  Manuscript use is limited to the registered role ``{role}''.",
            f"Its recorded scope is ``{scope}'', and the preserved",
            f"transfer boundary is ``{boundary}''.",
            f"% ARS-CITE source_ids={source_id} anchor={encoded_locator} claim_to_passage=SUPPORTED_BOUNDED context_ids={context_id} transfer_boundary=PRESERVED",
        ])
    ensure(status == "EXPLICIT_BOUNDED_PASSAGE_UNAVAILABILITY", f"{source_id}: unsupported finalization status")
    code = row["unavailability"]["code"]
    rendered_code = latex_plain(code)
    if source_id == "P30-S05":
        # Root's transient scratch-layout preflight found a 1.91772 pt overfull
        # box in this paragraph.  These discretionary breaks are local and do
        # not alter the recorded unavailability code or its semantics.
        rendered_code = rendered_code.replace(r"\_", r"\_\allowbreak ")
    lines = [
        f"The bibliographic record \\citep{{{source_id}}} remains metadata-identified and",
        f"prospectively coded for ``{role}'', but the bounded source-finalization",
        f"run retained no inspectable exact passage ({rendered_code}).  No substantive",
        "attribution from this record is used here.  Its recorded scope remains",
        f"``{scope}'', and the preserved transfer boundary is ``{boundary}''.",
        f"% ARS-CITE source_ids={source_id} anchor=none claim_to_passage=EXPLICIT_BOUNDED_UNAVAILABILITY context_ids={context_id} unavailability_code={code} transfer_boundary=PRESERVED",
    ]
    if source_id == "P30-S05":
        return "\n".join([r"\begingroup", r"\sloppy", *lines[:-1], r"\par", r"\endgroup", lines[-1]])
    return "\n".join(lines)


def p30_non_source(block_id: str, old: str) -> str:
    if block_id == "B0004":
        return replace_once(
            old,
            "All citations lack passage locators, so claim-to-passage support is inconclusive.",
            "Bounded source finalization yielded 18/26 locator-available rows and 8/26 explicit bounded-unavailability rows; no unavailable locator is guessed and every registered transfer boundary remains in force.",
            "P30/B0004",
        )
    if block_id == "B0006":
        return replace_once(
            old,
            "所有引文均缺段落定位，故支持狀態仍不確定；",
            "有界來源定稿產生十八筆可定位列與八筆明確有界不可得列；未猜測不可得定位，且所有轉移界線維持不變；",
            "P30/B0006",
        )
    if block_id == "B0062":
        return r"""The claim-to-passage matrix has 28 rows: one for each of P30-S01--P30-S26 and
one record-level row for each correction P30-C01 and P30-C02.  Among the 26
paper-specific source rows, 18 now carry bounded exact locators whose retained
passages provide bounded context for the registered uses without proving the
registered roles in full, while eight record explicit bounded passage unavailability
rather than guessed anchors.  Every source-specific hypothesis, scope, and
prohibited transfer remains in force.  The two correction rows remain finalized
only at publication-record level and bind the affected source IDs; they add no
formula or theorem locator.  No direct quotation is used.  Retraction status
remains \texttt{NOT\_\allowbreak CHECKED}, and source-level conflict-of-interest
status remains \texttt{UNKNOWN\_\allowbreak NOT\_\allowbreak AUDITED}."""
    if block_id == "B0065":
        return r"""Metadata verification is not passage verification. All inventory records have verified existence and normalized core metadata within the frozen workflow. Bounded source finalization yielded exact locators for 18 of the 26 substantive source rows; each retained passage provides bounded context within its registered use under the recorded hypothesis, scope, and prohibited transfer, but none is treated as proof of the registered role in full. The remaining eight rows record explicit bounded passage unavailability rather than a guessed theorem, page, section, or paragraph locator, so no substantive attribution from those records is used. Correction provenance is kept separately: the three Gaspard--Rice records retain their companion-DOI obligations, and P30-S17 remains paired with P30-S18 for affected use. This handling prevents an uncorrected formula transfer but does not amount to a structured retraction or full integrity audit."""
    if block_id == "B0066":
        return replace_once(
            old,
            "complete 26-entry bibliography",
            "28-entry bibliography comprising 26 admitted substantive source records and the two correction records P30-C01 and P30-C02",
            "P30/B0066",
        )
    if block_id == "B0106":
        return r"""The 28-row matrix records bounded exact locators for 18 of
P30-S01--P30-S26 and explicit bounded passage unavailability for the other eight;
each located passage provides bounded context for its registered use, is not
proof of the role in full, and clears no project-specific formula or theorem
transfer.  P30-S01/P30-S02 remain bound to
\citep{P30-C01}, P30-S03 remains bound to \citep{P30-C02}, and
P30-S17/P30-S18 remain paired for affected use.  The two correction records are
publication-level rows only.  Retraction status remains unchecked, and
source-level conflicts remain unaudited."""
    if block_id == "B0124":
        return r"""\section*{AI-Assistance Disclosure and Verification Limitation}
OpenAI Codex, operating in the GPT-5 model family, assisted during the sessions dated 2--4 September 2026 UTC; the exact backend snapshot or build was not exposed. Assistance covered organization of the frozen bibliography and source identities, bounded evidence synthesis, drafting, Stage-4 and Stage-4-prime revision work, source-finalization support, review integration, LaTeX conversion, deterministic checks of identifiers, citations, references, hashes, and word counts, and the already recorded fresh Stage-4.5 audit role for the Round-2 working draft. Role-separated assessments used fresh contexts within the same model family and are not claimed to be error-independent. No fresh Stage-4.5 rerun of the Round-3 successor is claimed here. No AI-authored scientific data, physical roof, operator, proof, determinant, error bound, cohomology result, or numerical experiment is presented. AI assistance is not credited with authorship."""
    if block_id == "B0125":
        return r"""Liang Wang made the recorded stage-gate confirmations and author-adjudicated design decisions. Neither that responsibility nor the present composition implies human full-text or source-passage verification. Stage~2.5 is complete. The later bounded source-finalization run yielded 18/26 locator-available rows and 8/26 explicit bounded-unavailability rows; no unavailable locator was guessed, and every located passage remains confined to its registered role and transfer boundary. A fresh Stage~4.5 integrity rerun has not yet been performed on the Round-3 successor draft. Verification remains limited to the frozen metadata, the retained authoritative passages and bounded unavailability records, source-verification ledgers, the source-effect matrix, and review artifacts."""
    raise RuntimeError(f"P30/{block_id}: missing replacement writer")


def p31_non_source(block_id: str, old: str) -> str:
    if block_id == "B0006":
        return replace_once(
            old,
            "All 22 inherited citations retain \\texttt{anchor:none};\nsource identities and metadata close, but claim-to-passage faithfulness\nremains \\texttt{INCONCLUSIVE}.",
            "Bounded source finalization yielded 7/22 locator-available rows and\n15/22 explicit bounded-unavailability rows; the located passages provide\nbounded context for the registered uses but do not prove the registered roles\nin full, and no unavailable locator was guessed.",
            "P31/B0006",
        )
    if block_id == "B0007":
        return replace_once(
            old,
            "所有引文均無段落定位， 逐主張的來源支持仍屬未定；",
            "有界來源定稿產生七筆可定位列與十五筆明確有界不可得列； 可定位段落僅提供登記用途內的有界脈絡， 並不構成對登記角色的完整證明， 且未猜測不可得定位；",
            "P31/B0007",
        )
    if block_id == "B0023":
        return """For the present article, this is a negative-boundary finding rather than a claim of
literature absence. The corpus was frozen by a bounded search, and bounded source
finalization yielded 7/22 locator-available rows plus 15/22 explicit bounded-
unavailability rows. The seven located passages provide bounded context for their
registered uses but do not prove the registered roles in full; no unavailable
locator was guessed. We can say that no retained source was
admitted as the complete project solver; we cannot say that no such theorem or
method exists anywhere. A later implementation still requires exact representation
hypotheses and passage-bound licenses for every subroutine. Thus, even a
mathematically promising route remains an unbound component rather than an
available certificate engine."""
    if block_id == "B0037":
        return r"""The method-component matrix has 24 rows: seven of P31-S01--P31-S22
carry bounded exact locators whose retained passages provide bounded context for
the registered uses without proving the registered roles in full, while the other
15 record explicit bounded passage unavailability rather than guessed
anchors. P31-S23 and P31-S24 retain their finalized publisher-level method
locators for the narrow proof-carrying and tamper-evident patterns cited here.
Every row states the component or claim role, passage status, applicable hypothesis
or scope, and a prohibited transfer. None establishes a P31 owner theorem,
implementation, semantic adjudicator, or scientific result. No direct quotation
is used."""
    if block_id == "B0039":
        return r"""Citation closure is checked against the notes-side versioned bibliography: all
24 cited source identifiers resolve to one entry, including source-verified
P31-S23 and P31-S24. The canonical bibliography is unchanged. This structural
check does not validate a theorem passage. Among P31-S01--P31-S22, seven rows
carry bounded exact locators that provide bounded context for their registered
uses without proving the registered roles in full, and 15 record explicit bounded
passage unavailability; no unavailable locator was guessed.
P31-S23/P31-S24 retain only their finalized publisher-level method locators. The
wording remains limited to inherited components, prospective use, and explicit
exclusions."""
    if block_id == "B0089":
        return r"""The dated supplement exposes one screening decision for each of the 20 frozen
query strings, but it is a new bounded Crossref replay and not a reconstruction
of the unavailable original-session excluded rows. In the 24-row method-passage
matrix, seven of P31-S01--P31-S22 have bounded exact locators, 15 have explicit
bounded passage-unavailability records, and P31-S23/P31-S24 retain their two
existing narrow publisher-level method locators. Every located passage provides
bounded context within its registered use and preserves the prohibited transfer;
none proves the role in full. These records provide no
\texttt{Gamma\_0(11)} owner theorem, solver, inverse witness, semantic adjudicator,
or scientific result. Retraction and source-conflict screening were not expanded
by this revision."""
    if block_id == "B0099":
        return replace_once(
            old,
            "The source corpus\nremains passage-unresolved.",
            "Bounded source finalization partially resolves passage provenance: 7/22 rows\nhave exact bounded locators and 15/22 record explicit bounded unavailability,\nwithout guessing or licensing project-specific transfer.",
            "P31/B0099",
        )
    if block_id == "B0107":
        return r"""OpenAI Codex, using the GPT-5 model family, assisted during the
sessions dated 2026-09-02 through 2026-09-04 UTC; the exact backend
snapshot/build was not exposed. Recorded assistance included literature-search
support, source-identity and metadata checking, evidence-matrix construction,
evidence synthesis, report drafting, role-separated fresh-context review,
ClaimIntent-constrained revision drafting, Stage-4 and Stage-4-prime Round-2
work, bounded source-finalization support, citation/reference/hash accounting,
and the already recorded fresh Stage-4.5 audit role for the Round-2 working
draft. Same-family fresh-context roles are not claimed to be error-independent,
and no fresh Stage-4.5 rerun of the Round-3 successor is claimed here. No AI
system executed a P31 solver, proof, pair decision, owner census, experiment, or
canonical-results refresh."""
    if block_id == "B0108":
        return r"""Liang Wang is the responsible human author. He approved the project
restrictions, stage gates, and the Phase-6 author-adjudicated design
choice. Those approvals must not be interpreted as a statement that he
personally read every source in full or verified every claim at the exact
source-passage level. The recorded verification was bounded mainly to
source identity, metadata, abstracts, authoritative landing pages, and
project-local claim-fitness records. Bounded source finalization yielded
7/22 locator-available rows and 15/22 explicit bounded-unavailability rows;
the located passages provide bounded context for the registered uses but do not
prove the registered roles in full, no unavailable locator was guessed, and no
project-specific theorem transfer follows. The
article does not claim complete theorem-level source verification, novelty
clearance, or a clean retraction/conflict screen."""
    raise RuntimeError(f"P31/{block_id}: missing replacement writer")


P31_GROUP_PREAMBLES = {
    "B0021": "The frozen modular-subgroup sources are retained only under the following source-specific bounded dispositions.",
    "B0025": "The matrix and arithmetic-conjugacy sources are retained only under the following source-specific bounded dispositions.",
    "B0029": "The canonicalization and arithmetic-subroutine sources are retained only under the following source-specific bounded dispositions.",
    "B0032": "The aggregate-census sources are retained only under the following source-specific bounded dispositions.",
}


def make_replacements(paper_id: str, paper: dict) -> dict[str, str]:
    rows_by_block: dict[str, list[dict]] = {}
    for row in paper["source_finalization"]["rows"]:
        rows_by_block.setdefault(row["block_id"], []).append(row)
    replacements = {}
    for target in paper["requested"]["all_requested_targets"]:
        block_id = target["block_id"]
        old = paper["blocks"][block_id].normalized_text
        if block_id in rows_by_block:
            rows = rows_by_block[block_id]
            if paper_id == "P30":
                ensure(len(rows) == 1, f"P30/{block_id}: source aggregation changed")
                new_text = source_row_text(rows[0])
            else:
                ensure(block_id in P31_GROUP_PREAMBLES, f"P31/{block_id}: aggregate block not declared")
                new_text = "\n".join([P31_GROUP_PREAMBLES[block_id], *(source_row_text(row) for row in rows)])
        else:
            new_text = p30_non_source(block_id, old) if paper_id == "P30" else p31_non_source(block_id, old)
        ensure(new_text != old, f"{paper_id}/{block_id}: replacement is no-op")
        ensure("<!--block:" not in new_text, f"{paper_id}/{block_id}: block marker leaked")
        parse_document(new_text, fragment=True)
        old_keys, new_keys = cite_keys(old), cite_keys(new_text)
        ensure(new_keys.issubset(old_keys), f"{paper_id}/{block_id}: introduced citation keys {sorted(new_keys - old_keys)}")
        source_ids = set(target.get("source_ids", []))
        if source_ids:
            ensure(source_ids == new_keys, f"{paper_id}/{block_id}: source/citation mapping changed")
        replacements[block_id] = new_text
    return replacements


def response_documents(
    paper_id: str,
    paper: dict,
    patch_path: Path,
    patch_sha: str,
    layout_incident: dict | None = None,
    semantic_preflight: dict | None = None,
) -> tuple[dict, str, str]:
    items, response_rows, log_rows = [], [], []
    targets = paper["requested"]["all_requested_targets"]
    for source_issue_id in paper["issue_order"]:
        issue = paper["issues"][source_issue_id]
        blocks = [value["block_id"] for value in targets if value["issue_id"] == source_issue_id]
        roadmap_id = f"REV-{source_issue_id}"
        items.append({
            "source_issue_id": source_issue_id,
            "roadmap_item_id": roadmap_id,
            "reviewer_comment": issue["finding"],
            "author_response": (
                f"The writer emitted exactly {len(blocks)} authorized replace_block operation(s) "
                f"for {', '.join(blocks)}, following the frozen semantic branches and constraints. "
                "Application, matrix regeneration, build, and post-apply integrity review remain pending."
            ),
            "proposed_block_ids": blocks,
            "proposed_operation": "replace_block",
            "status": "PROPOSED_PENDING_APPLICATION",
        })
        response_rows.append(f"| `{source_issue_id}` | `{roadmap_id}` | {len(blocks)} | `PROPOSED_PENDING_APPLICATION` |")
        targets_md = ", ".join(f"`{block}`" for block in blocks)
        log_rows.append(
            f"| `{source_issue_id}` | `{roadmap_id}` | `{issue.get('severity', 'UNSPECIFIED')}` | "
            f"`must_fix` | `will_address` | {targets_md} | Patch emitted; not applied. |"
        )
    response = {
        "schema_version": "response-to-reviewers-provisional/1.0",
        "artifact_status": "PROVISIONAL_PENDING_APPLICATION_AND_POST_APPLY_AUDIT",
        "paper_id": paper_id,
        "revision_round": REVISION_ROUND,
        "patch_binding": {"path": str(patch_path.relative_to(ROOT)), "sha256": patch_sha, "apply_status": "NOT_APPLIED"},
        "items": items,
        "summary": {"proposed": len(items), "resolved": 0, "applied_operations": 0, "matrix_regenerations": 0},
        "new_references_added": 0,
        "boundary": "Writer judgment text only; mechanical fields await the independent applier.",
    }
    if layout_incident is not None:
        response["layout_preflight_lineage"] = {
            "incident_path": layout_incident["path"],
            "superseded_patch_sha256": [P30_INITIAL_PATCH_SHA256, P30_ALLOWBREAK_PATCH_SHA256, P30_CONTEXT_BOUND_PATCH_SHA256],
            "resolution": "B0025 local nonsemantic scoped-sloppy re-emission",
        }
    if semantic_preflight is not None:
        response["semantic_preflight_lineage"] = semantic_preflight
    incident_md = [] if layout_incident is None else [
        "Layout lineage: root scratch preflights found the same 1.91772 pt overfull box in `B0025` in the initial patch and the first local-break remediation; the scoped-sloppy remedy then passed independently, and that clean-layout patch was later superseded only to narrow summary semantics.",
        "",
    ]
    semantic_md = [] if semantic_preflight is None else [
        "Semantic preflight lineage: every exact-locator replacement and every locator-count summary now says that retained passages provide bounded context within the registered use and do not prove the full role.",
        "",
    ]
    response_md = "\n".join([
        f"# {paper_id} Stage-4-prime Round-3 provisional response", "",
        "Status: **patch emitted, not applied**.", "",
        "| Source issue | Roadmap item | Proposed ops | Status |", "|---|---|---:|---|",
        *response_rows, "", *incident_md, *semantic_md,
        "No successor draft, matrix regeneration, bibliography change, build, or fresh Stage 4.5 rerun is claimed.", "",
    ])
    incident_log = [] if layout_incident is None else [
        f"- Superseded patch SHA-256 values: `{P30_INITIAL_PATCH_SHA256}` and `{P30_ALLOWBREAK_PATCH_SHA256}`.",
        f"- Layout-preflight incident: `{layout_incident['path']}`; B0025 was re-emitted with a local nonsemantic scoped-sloppy paragraph remedy.",
    ]
    semantic_log = [] if semantic_preflight is None else [
        f"- Semantic-preflight lineage: `{semantic_preflight['path']}`; all exact-locator and summary prose uses the cautious context/use-bound wording.",
    ]
    revision_log = "\n".join([
        f"# {paper_id} Stage-4-prime Round-3 writer revision log", "", "Date: **2026-09-04**", "",
        "| Source issue | Roadmap item | Request severity | Obligation | Author triage | Exact targets | Writer action |",
        "|---|---|---|---|---|---|---|", *log_rows, "", "## Writer boundary", "",
        f"- Patch SHA-256: `{patch_sha}`.",
        *incident_log,
        *semantic_log,
        f"- Emitted operations: `{paper['config']['ops']}`; applied operations: `0`.",
        "- Claim-strength authorizations: `0`; collateral authorizations: `0`.",
        "- Bibliography changes: `0`; matrix regenerations performed: `0`.",
        "- Successor draft/PDF/apply report: not created by the writer.",
        "- Fresh Stage 4.5, Stage 5, Stage 6, canonical promotion, science/result refresh, and Route changes remain unauthorized.", "",
    ])
    return response, response_md, revision_log


def emit(
    *,
    refresh_p30_layout: bool = False,
    finalize_preflight: bool = False,
    coherence_narrow: bool = False,
) -> None:
    context = load_context()
    for paper_id, paper in context["papers"].items():
        if refresh_p30_layout and not finalize_preflight and not coherence_narrow and paper_id != "P30":
            continue
        paths = output_paths(paper["base_path"])
        for key in ("roadmap", "claim_surface", "author_choices", "author_adjudication"):
            ensure(paths[key].is_file(), f"{paper_id}: missing authority artifact {paths[key].relative_to(ROOT)}")
        output_keys = ("patch", "handoff", "response_json", "response_md", "revision_log", "validation", "matrix_plan")
        superseded_semantic_artifact = None
        superseded_root_layout_receipt = None
        if coherence_narrow:
            for key in output_keys:
                ensure(paths[key].is_file(), f"coherence narrowing requires existing output: {paths[key].relative_to(ROOT)}")
            if paper_id == "P30" and file_digest(paths["patch"]) == P30_COHERENCE_PARTIAL_PATCH_SHA256:
                ensure_hash(paths["layout_incident"], P30_COHERENCE_PARTIAL_INCIDENT_SHA256)
            else:
                ensure_hash(
                    paths["patch"],
                    P30_CONTEXT_BOUND_PATCH_SHA256 if paper_id == "P30" else P31_CONTEXT_BOUND_PATCH_SHA256,
                )
            ensure_hash(
                paths["semantic_preflight"],
                P30_CONTEXT_SEMANTIC_PREFLIGHT_SHA256 if paper_id == "P30" else P31_CONTEXT_SEMANTIC_PREFLIGHT_SHA256,
            )
            superseded_semantic_artifact = artifact(paths["semantic_preflight"])
            if paper_id == "P30":
                if file_digest(paths["layout_incident"]) != P30_COHERENCE_PARTIAL_INCIDENT_SHA256:
                    ensure_hash(paths["layout_incident"], P30_CONTEXT_LAYOUT_INCIDENT_SHA256)
                root_layout_receipt = paths["layout_incident"].with_name(
                    "stage4_prime_correction_round3_root_layout_repreflight_receipt.json"
                )
                ensure_hash(root_layout_receipt, P30_CONTEXT_ROOT_LAYOUT_RECEIPT_SHA256)
                superseded_root_layout_receipt = artifact(root_layout_receipt)
            else:
                ensure(not paths["layout_incident"].exists(), "P31 unexpectedly has a P30 layout incident")
        elif finalize_preflight:
            for key in output_keys:
                ensure(paths[key].is_file(), f"preflight finalization requires existing output: {paths[key].relative_to(ROOT)}")
            ensure_hash(
                paths["patch"],
                P30_ALLOWBREAK_PATCH_SHA256 if paper_id == "P30" else P31_INITIAL_PATCH_SHA256,
            )
            if paper_id == "P30":
                ensure_hash(paths["layout_incident"], P30_ALLOWBREAK_INCIDENT_SHA256)
            else:
                ensure(not paths["layout_incident"].exists(), "P31 unexpectedly has a P30 layout incident")
            ensure(not paths["semantic_preflight"].exists(), f"semantic preflight lineage already exists: {paths['semantic_preflight'].relative_to(ROOT)}")
        elif refresh_p30_layout:
            for key in output_keys:
                ensure(paths[key].is_file(), f"layout refresh requires existing output: {paths[key].relative_to(ROOT)}")
            ensure_hash(paths["patch"], P30_ALLOWBREAK_PATCH_SHA256)
            ensure_hash(paths["layout_incident"], P30_ALLOWBREAK_INCIDENT_SHA256)
        else:
            for key in output_keys:
                ensure(not paths[key].exists(), f"emit refuses existing output: {paths[key].relative_to(ROOT)}")
        roadmap, roadmap_raw = load_json(paths["roadmap"])
        claim_surface, claim_raw = load_json(paths["claim_surface"])
        choices, _ = load_json(paths["author_choices"])
        adjudication, adjudication_raw = load_json(paths["author_adjudication"])
        ensure(roadmap == make_roadmap(paper_id, paper), f"{paper_id}: roadmap is not the mechanical projection")
        ensure(claim_surface["surfaces"] == [] and claim_surface["claim_intent_sources"] == [], f"{paper_id}: unexpected claim surface")
        ensure(choices["collateral_authorizations"] == [], f"{paper_id}: unexpected collateral authority")
        rr.validate_roadmap(
            roadmap, roadmap_raw=roadmap_raw, base_raw=paper["base_raw"],
            block_manifest=paper["manifest"], block_manifest_raw=paper["manifest_raw"],
        )
        store = rr._standalone_store(ROOT)
        surfaces = rr.validate_claim_surface_manifest(
            claim_surface, claim_surface_raw=claim_raw, roadmap=roadmap,
            roadmap_raw=roadmap_raw, base_raw=paper["base_raw"], artifact_store=store,
        )
        author_state = rr.validate_author_adjudication(
            adjudication, adjudication_raw=adjudication_raw, roadmap=roadmap,
            roadmap_raw=roadmap_raw, claim_surface=claim_surface,
            claim_surface_raw=claim_raw, base_raw=paper["base_raw"], surfaces_by_id=surfaces,
        )
        replacements = make_replacements(paper_id, paper)
        ops, target_checks = [], []
        for target in paper["requested"]["all_requested_targets"]:
            block_id, source_issue_id = target["block_id"], target["issue_id"]
            op = {
                "op": "replace_block", "block_id": block_id,
                "old_hash": paper["manifest_blocks"][block_id]["old_hash"],
                "new_text": replacements[block_id],
                "roadmap_item_ids": [f"REV-{source_issue_id}"],
                "claim_strength_changes": [], "collateral_authorization_ids": [],
            }
            ops.append(op)
            target_checks.append({
                "source_issue_id": source_issue_id,
                "roadmap_item_id": f"REV-{source_issue_id}",
                "block_id": block_id, "operation": "replace_block",
                "request_expected_old_sha256": target["expected_old_hash"],
                "request_parser_norm_hash": target["parser_norm_hash"],
                "patch_old_hash": op["old_hash"],
                "old_hash_replay": "PASS", "exact_authority_projection": "PASS",
                "new_text_fragment_parse": "PASS", "block_marker_absence": "PASS",
                "citation_nonexpansion": "PASS", "claim_strength_authorizations": 0,
                "collateral_authorizations": 0,
            })
        ensure(len(ops) == paper["config"]["ops"], f"{paper_id}: operation count mismatch")
        ensure(len({value["block_id"] for value in ops}) == len(ops), f"{paper_id}: block reused")
        patch = {
            "patch_format_version": "1.1", "authorization_context": "review_roadmap",
            "revision_round": REVISION_ROUND, "base_draft_hash": digest(paper["base_raw"])[:12],
            "roadmap_sha256": digest(roadmap_raw),
            "author_adjudication_sha256": digest(adjudication_raw),
            "author_decision_digest": rr.author_decision_digest(adjudication),
            "claim_surface_manifest_sha256": digest(claim_raw),
            "ops": ops, "emitted_by": "draft_writer_agent",
        }
        authority_validation = rr.validate_review_patch_authorization(
            patch, base_raw=paper["base_raw"], roadmap=roadmap, roadmap_raw=roadmap_raw,
            adjudication=adjudication, adjudication_raw=adjudication_raw,
            claim_surface=claim_surface, claim_surface_raw=claim_raw, surfaces_by_id=surfaces,
        )
        ensure(authority_validation["status"] == "pass", f"{paper_id}: patch authority failed")
        patch_raw = encoded_json(patch)
        atomic_write(paths["patch"], patch_raw)
        patch_sha = digest(patch_raw)
        layout_incident_record = None
        if refresh_p30_layout or ((finalize_preflight or coherence_narrow) and paper_id == "P30"):
            ensure(patch_sha not in {P30_INITIAL_PATCH_SHA256, P30_ALLOWBREAK_PATCH_SHA256}, "layout refresh did not change the patch")
            b0025 = next(value for value in ops if value["block_id"] == "B0025")
            ensure(r"IOP\_\allowbreak OFFICIAL\_\allowbreak ENDPOINT" in b0025["new_text"], "B0025 discretionary breaks missing")
            ensure(r"\begingroup" in b0025["new_text"] and r"\sloppy" in b0025["new_text"] and r"\par" in b0025["new_text"] and r"\endgroup" in b0025["new_text"], "B0025 scoped-sloppy remedy missing")
            superseded_layout_patches = [
                {
                    "attempt": 1,
                    "remedy": "none",
                    "path": str(paths["patch"].relative_to(ROOT)),
                    "sha256": P30_INITIAL_PATCH_SHA256,
                    "retained_as_file": False,
                    "root_scratch_preflight": "FAILED_IDENTICAL_1.91772PT_OVERFULL",
                },
                {
                    "attempt": 2,
                    "remedy": "local discretionary breaks after displayed-code underscores",
                    "path": str(paths["patch"].relative_to(ROOT)),
                    "sha256": P30_ALLOWBREAK_PATCH_SHA256,
                    "retained_as_file": False,
                    "root_scratch_preflight": "FAILED_IDENTICAL_1.91772PT_OVERFULL",
                },
            ]
            if coherence_narrow:
                superseded_layout_patches.append({
                    "attempt": 3,
                    "remedy": "scoped sloppy paragraph at B0025",
                    "path": str(paths["patch"].relative_to(ROOT)),
                    "sha256": P30_CONTEXT_BOUND_PATCH_SHA256,
                    "retained_as_file": False,
                    "root_scratch_preflight": "PASS_CLEAN_18_PAGES_ZERO_LAYOUT_OR_REFERENCE_DIAGNOSTICS",
                    "supersession_reason": "Unrelated locator-summary semantic coherence narrowing",
                    "root_receipt": superseded_root_layout_receipt,
                })
            incident = {
                "schema_version": "round10-stage4-prime-round3-layout-preflight-incident/1.0",
                "paper_id": "P30",
                "revision_round": REVISION_ROUND,
                "incident_source": "root_transient_scratch_apply_and_layout_preflight_report",
                "finding": {
                    "kind": "Overfull \\hbox",
                    "excess_width_pt": 1.91772,
                    "rendered_line_span": "93--99",
                    "block_id": "B0025",
                    "source_id": "P30-S05",
                },
                "lineage": {
                    "superseded_patches": superseded_layout_patches,
                    "successor_patch": {
                        "path": str(paths["patch"].relative_to(ROOT)),
                        "sha256": patch_sha,
                        "apply_status": "NOT_APPLIED_BY_WRITER",
                    },
                },
                "resolution": {
                    "scope": "B0025 only",
                    "operation": "replace_block remains unchanged",
                    "change": "Retain the local discretionary breaks and scope TeX sloppy paragraph layout to B0025 with begingroup/par/endgroup.",
                    "semantic_change": False,
                    "citation_change": False,
                    "claim_strength_change": False,
                },
                "boundary": {
                    "scratch_draft_or_pdf_retained": False,
                    "canonical_or_matrix_mutation": False,
                    "writer_latex_build_run": False,
                    "independent_root_repreflight_required": True,
                },
                "status": "REMEDIATION_REEMITTED_NOT_APPLIED_ROOT_REPREFLIGHT_PENDING",
            }
            atomic_write(paths["layout_incident"], encoded_json(incident))
            layout_incident_record = artifact(paths["layout_incident"])
        semantic_preflight_record = None
        if finalize_preflight or coherence_narrow:
            available_rows = [
                row for row in paper["source_finalization"]["rows"]
                if row["finalization_status"] == "EXACT_LOCATOR_AVAILABLE_FOR_AUTHORIZED_LATER_REPLACEMENT"
            ]
            op_by_block = {value["block_id"]: value for value in ops}
            per_source = []
            for row in available_rows:
                ensure(digest(row["support_excerpt"].encode("utf-8")) == row["support_excerpt_sha256"], f"{paper_id}/{row['source_id']}: excerpt hash mismatch")
                new_text = op_by_block[row["block_id"]]["new_text"]
                ensure(f"\\citep{{{row['source_id']}}}" in new_text, f"{paper_id}/{row['source_id']}: citation absent after semantic narrowing")
                ensure("supports only the registered role" not in new_text, f"{paper_id}/{row['source_id']}: full-role support assertion survived")
                ensure("it is not treated as proof of the" in new_text and "Manuscript use is limited to the registered role" in new_text, f"{paper_id}/{row['source_id']}: cautious context/use wording absent")
                per_source.append({
                    "source_id": row["source_id"],
                    "block_id": row["block_id"],
                    "exact_passage_locator": row["exact_passage_locator"],
                    "support_excerpt_sha256": row["support_excerpt_sha256"],
                    "support_excerpt_word_count": row["support_excerpt_word_count"],
                    "registered_role": row["registered_role"],
                    "transfer_boundary_preserved": row["transfer_boundary_preserved"],
                    "audit_disposition": "CONTEXT_IDENTIFIED_USE_BOUNDED_NO_FULL_ROLE_PROOF_ASSERTION",
                    "claim_strength_increase_allowed": False,
                })
            summary_blocks = (
                ["B0062", "B0065", "B0106"] if paper_id == "P30"
                else ["B0006", "B0007", "B0023", "B0037", "B0039", "B0089", "B0108"]
            )
            summary_checks = []
            for block_id in summary_blocks:
                summary_text = op_by_block[block_id]["new_text"]
                summary_flat = " ".join(summary_text.split())
                ensure("supports only their registered roles" not in summary_text, f"{paper_id}/{block_id}: plural full-role support assertion survived")
                ensure("supports only its registered role" not in summary_text, f"{paper_id}/{block_id}: singular full-role support assertion survived")
                if block_id == "B0007":
                    ensure("僅提供登記用途內的有界脈絡" in summary_text and "不構成對登記角色的完整證明" in summary_text, f"{paper_id}/{block_id}: Chinese cautious summary absent")
                else:
                    ensure("bounded context" in summary_flat and ("not proof" in summary_flat or "do not prove" in summary_flat or "without proving" in summary_flat or "none proves" in summary_flat or "none is treated as proof" in summary_flat), f"{paper_id}/{block_id}: cautious summary absent")
                summary_checks.append({
                    "block_id": block_id,
                    "disposition": "BOUNDED_CONTEXT_FOR_REGISTERED_USE_NOT_PROOF_OF_ROLE_IN_FULL",
                    "counts_science_route_citations_preserved": True,
                })
            superseded_patches = (
                [P30_INITIAL_PATCH_SHA256, P30_ALLOWBREAK_PATCH_SHA256]
                if paper_id == "P30" else [P31_INITIAL_PATCH_SHA256]
            )
            if coherence_narrow:
                superseded_patches.append(
                    P30_CONTEXT_BOUND_PATCH_SHA256 if paper_id == "P30" else P31_CONTEXT_BOUND_PATCH_SHA256
                )
            semantic = {
                "schema_version": "round10-stage4-prime-round3-semantic-preflight-lineage/1.0",
                "paper_id": paper_id,
                "revision_round": REVISION_ROUND,
                "audit_scope": "every exact-locator source replacement and every locator-count summary emitted by the writer",
                "source_finalization": artifact(paper["source_path"]),
                "finding": "The retained excerpts identify bounded context but do not uniformly establish every component of the broader registered-role labels; a cross-track audit also found that the first narrowed patch retained full-role support wording in locator-count summaries.",
                "resolution": "Every exact-locator paragraph and locator-count summary states that the passage supplies bounded context for or within the registered use, preserves the transfer boundary, and does not prove the role in full.",
                "superseded_patch_sha256": superseded_patches,
                "current_patch": {
                    "path": str(paths["patch"].relative_to(ROOT)),
                    "sha256": patch_sha,
                    "apply_status": "NOT_APPLIED_BY_WRITER",
                },
                "audited_exact_locator_rows": len(available_rows),
                "audited_target_blocks": len({row["block_id"] for row in available_rows}),
                "per_source_audit": per_source,
                "audited_summary_blocks": len(summary_checks),
                "summary_coherence_audit": summary_checks,
                "claim_strength_authorizations": 0,
                "collateral_authorizations": 0,
                "status": "PASS_WRITER_SOURCE_EXCERPT_AND_SUMMARY_COHERENCE_PREFLIGHT",
            }
            if superseded_semantic_artifact is not None:
                semantic["superseded_semantic_preflight"] = {
                    **superseded_semantic_artifact,
                    "status": "SUPERSEDED_AFTER_CROSS_TRACK_SUMMARY_COHERENCE_RETURN",
                }
            expected_rows = paper["requested"]["frozen_source_finalization"]["locator_available"]
            ensure(len(per_source) == expected_rows, f"{paper_id}: semantic audit population mismatch")
            atomic_write(paths["semantic_preflight"], encoded_json(semantic))
            semantic_preflight_record = artifact(paths["semantic_preflight"])
        response, response_md, revision_log = response_documents(
            paper_id, paper, paths["patch"], patch_sha,
            layout_incident_record, semantic_preflight_record,
        )
        atomic_write(paths["response_json"], encoded_json(response))
        atomic_write(paths["response_md"], response_md.encode())
        atomic_write(paths["revision_log"], revision_log.encode())
        matrix_plan = {
            "schema_version": "round10-stage4-prime-round3-matrix-regeneration-plan/1.0",
            "paper_id": paper_id, "revision_round": REVISION_ROUND,
            "status": "NOT_RUN_WRITER_ROLE_FORBIDDEN", "matrix_kind": paper["config"]["matrix_kind"],
            "matrix": {
                "path": str(paper["matrix_path"].relative_to(ROOT)),
                "current_sha256": file_digest(paper["matrix_path"]),
                "authorized_operation": paper["requested"]["matrix_regeneration"]["operation"],
                "in_place_explicit_exception": paper["requested"]["matrix_regeneration"]["in_place_explicit_exception"],
                "expected_result_counts": paper["requested"]["matrix_regeneration"]["expected_result_counts"],
            },
            "preconditions": [
                "The independent applier has applied every authorized manuscript replacement successfully.",
                "The successor draft and apply report replay the exact patch and authority hashes.",
                "No scientific value, registered claim, structure, bibliography, Route state, or initial system changed.",
            ],
            "writer_statement": "No matrix bytes were modified or regenerated in writer emission.",
        }
        atomic_write(paths["matrix_plan"], encoded_json(matrix_plan))
        ensure_hash(paper["matrix_path"], paper["requested"]["matrix_regeneration"]["expected_current_sha256"])
        ensure_hash(paper["bib_path"], paper["requested"]["current_stage4_prime_bibliography"]["sha256"])
        item_mapping = []
        for index, source_issue_id in enumerate(paper["issue_order"], 1):
            blocks = [value["block_id"] for value in paper["requested"]["all_requested_targets"] if value["issue_id"] == source_issue_id]
            item_mapping.append({
                "source_issue_id": source_issue_id, "roadmap_item_id": f"REV-{source_issue_id}",
                "display_order": index,
                "authorized_targets": [{"block_id": block, "allowed_operations": ["replace_block"]} for block in blocks],
            })
        handoff = {
            "schema_version": "round10-stage4-prime-scope-reissue-writer-handoff/1.0",
            "paper_id": paper_id, "revision_round": REVISION_ROUND,
            "generated_at_utc": timestamp(), "status": "WRITER_PATCH_EMITTED_NOT_APPLIED",
            "controlling_authority": {
                "receipt": artifact(RECEIPT), "input_freeze": artifact(FREEZE),
                "expanded_request": artifact(REQUEST), "author_event_sha256": AUTHOR_EVENT_SHA256,
            },
            "base_draft": artifact(paper["base_path"]), "block_manifest": artifact(paper["manifest_path"]),
            "fresh_authority": {
                "revision_roadmap": artifact(paths["roadmap"]),
                "claim_surface_manifest": {**artifact(paths["claim_surface"]), "surfaces": 0},
                "author_choices": artifact(paths["author_choices"]),
                "author_adjudication": artifact(paths["author_adjudication"]),
                "author_decision_digest": author_state["author_decision_digest"],
                "display_order": "source_traceability", "claim_strength_authorizations": 0,
                "collateral_authorizations": 0,
            },
            "source_issue_mapping": item_mapping,
            "patch": {**artifact(paths["patch"]), "ops": len(ops), "applied": False},
            "provisional_response": {"json": artifact(paths["response_json"]), "markdown": artifact(paths["response_md"])},
            "revision_log": artifact(paths["revision_log"]),
            "matrix_regeneration_plan": artifact(paths["matrix_plan"]),
            "boundaries": {
                "patch_applied": False, "successor_draft_pdf_or_apply_report_created": False,
                "matrix_regenerated": False, "bibliography_modified": False,
                "canonical_science_result_route_initial_system_or_readme_modified": False,
                "fresh_stage4_5_stage5_or_stage6_run": False,
            },
            "next_legal_action": "Independent root applier validates and applies this exact patch to a new versioned draft, then regenerates the authorized matrix in place.",
        }
        if layout_incident_record is not None:
            handoff["layout_preflight_lineage"] = {
                "incident": layout_incident_record,
                "superseded_patch_sha256": [P30_INITIAL_PATCH_SHA256, P30_ALLOWBREAK_PATCH_SHA256, P30_CONTEXT_BOUND_PATCH_SHA256],
                "current_patch_sha256": patch_sha,
                "root_repreflight_status": "PENDING",
            }
        if semantic_preflight_record is not None:
            handoff["semantic_preflight_lineage"] = semantic_preflight_record
        atomic_write(paths["handoff"], encoded_json(handoff))
        frozen_replay = []
        records = [
            paper["frozen"]["current_working_draft"], paper["frozen"]["current_working_bibliography"],
            paper["frozen"]["block_manifest"], paper["frozen"]["initial_system_source"],
            paper["frozen"]["route_crosswalk"], paper["frozen"]["authorized_in_place_matrix_regeneration"],
            *paper["frozen"]["canonical_files"], *paper["frozen"].get("science_files", []),
        ]
        for record in records:
            ensure_hash(ROOT / record["path"], record["sha256"])
            frozen_replay.append({**record, "status": "PASS_EXACT"})
        requested_successor = ROOT / paper["requested"]["requested_new_versioned_draft"]["path"]
        forbidden_checks = {
            "successor_draft_absent": not requested_successor.exists(),
            "successor_pdf_absent": not requested_successor.with_suffix(".pdf").exists(),
            "successor_apply_report_absent": not requested_successor.with_name(requested_successor.name + ".apply-report.json").exists(),
            "matrix_hash_unchanged": file_digest(paper["matrix_path"]) == paper["requested"]["matrix_regeneration"]["expected_current_sha256"],
            "bibliography_hash_unchanged": file_digest(paper["bib_path"]) == paper["requested"]["current_stage4_prime_bibliography"]["sha256"],
        }
        ensure(all(forbidden_checks.values()), f"{paper_id}: forbidden output or mutation detected")
        validation = {
            "schema_version": "round10-stage4-prime-scope-reissue-writer-validation-receipt/1.0",
            "paper_id": paper_id, "revision_round": REVISION_ROUND,
            "validated_at_utc": timestamp(), "status": "PASS_WRITER_EMISSION_ONLY",
            "authority": {
                "receipt_sha256": EXPECTED_ROOT_HASHES[RECEIPT],
                "freeze_sha256": EXPECTED_ROOT_HASHES[FREEZE],
                "expanded_request_sha256": EXPECTED_ROOT_HASHES[REQUEST],
                "author_event_sha256": AUTHOR_EVENT_SHA256,
            },
            "official_ars_validation": {
                "roadmap_schema_and_source_order": "PASS",
                "claim_surface_manifest": "PASS_EMPTY_REGISTERED_POPULATION",
                "author_adjudication_schema_scope_and_digest": "PASS",
                "patch_authorization_projection": authority_validation,
                "ars_revision_roadmap_module": str(ARS_ROOT / "scripts/revision_roadmap.py"),
            },
            "totals": {
                "requested_unique_replace_block_pairs": paper["config"]["ops"],
                "emitted_unique_replace_block_ops": len(ops),
                "old_hash_replay_pass": len(target_checks),
                "exact_authority_projection_pass": len(target_checks),
                "fragment_parse_pass": len(target_checks),
                "citation_nonexpansion_pass": len(target_checks),
                "claim_strength_authorizations": 0, "collateral_authorizations": 0,
                "bibliography_operations": 0, "matrix_regenerations_run": 0,
                "patch_applications_run": 0, "latex_builds_run": 0,
            },
            "per_target_checks": target_checks, "frozen_artifact_replay": frozen_replay,
            "outputs": {
                "revision_roadmap": artifact(paths["roadmap"]),
                "claim_surface_manifest": artifact(paths["claim_surface"]),
                "author_choices": artifact(paths["author_choices"]),
                "author_adjudication": artifact(paths["author_adjudication"]),
                "revision_patch": artifact(paths["patch"]), "writer_handoff": artifact(paths["handoff"]),
                "provisional_response_json": artifact(paths["response_json"]),
                "provisional_response_markdown": artifact(paths["response_md"]),
                "revision_log": artifact(paths["revision_log"]),
                "matrix_regeneration_plan": artifact(paths["matrix_plan"]),
            },
            "forbidden_output_checks": forbidden_checks,
            "boundary": "This receipt validates writer emission, not application, build, semantic completeness, or Stage 4.5 integrity.",
        }
        if layout_incident_record is not None:
            validation["outputs"]["layout_preflight_incident"] = layout_incident_record
            validation["layout_preflight_remediation"] = {
                "block_id": "B0025",
                "superseded_patch_sha256": [P30_INITIAL_PATCH_SHA256, P30_ALLOWBREAK_PATCH_SHA256, P30_CONTEXT_BOUND_PATCH_SHA256],
                "current_patch_sha256": patch_sha,
                "local_nonsemantic_break_present": True,
                "local_scoped_sloppy_paragraph_present": True,
                "independent_root_repreflight": "PENDING",
            }
        if semantic_preflight_record is not None:
            validation["outputs"]["semantic_preflight_lineage"] = semantic_preflight_record
            validation["semantic_preflight"] = {
                "exact_locator_rows_audited": paper["requested"]["frozen_source_finalization"]["locator_available"],
                "full_role_proof_assertions_remaining": 0,
                "cautious_context_use_bound_replacements": paper["requested"]["frozen_source_finalization"]["locator_available"],
                "summary_blocks_audited": 3 if paper_id == "P30" else 7,
                "summary_full_role_support_assertions_remaining": 0,
                "status": "PASS",
            }
        atomic_write(paths["validation"], encoded_json(validation))
        print(f"EMITTED {paper_id} patch={patch_sha} ops={len(ops)} adjudication={digest(adjudication_raw)} validation={file_digest(paths['validation'])}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("phase", choices=("prepare", "emit", "refresh-p30-layout", "finalize-preflight", "coherence-narrow"))
    args = parser.parse_args()
    if args.phase == "prepare":
        prepare()
    elif args.phase == "emit":
        emit()
    elif args.phase == "refresh-p30-layout":
        emit(refresh_p30_layout=True)
    elif args.phase == "finalize-preflight":
        emit(finalize_preflight=True)
    else:
        emit(coherence_narrow=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
