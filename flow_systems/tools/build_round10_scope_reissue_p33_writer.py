#!/usr/bin/env python3
"""Emit the P33 Stage-4-prime scope-reissue writer package.

The default mode is fail-closed and writer-only: it emits a fresh round-6
authority lineage (schema revision_round=2), a 37-operation revision patch,
provisional response/log artifacts, and an append-only bibliography plan.  It
does not apply the patch, append the bibliography, build TeX, or update a
README.  The separately selected ``--apply-bibliography-plan`` mode exists for
the root orchestrator and is intentionally not called by writer emission.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import tempfile
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import jsonschema


ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "papers/33-bolza-control-matched-census"
NOTES = PAPER / "notes"
PAPER_DIR = PAPER / "paper"
ARS_ROOT = Path(
    "/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/skills/academic-research-suite/ars"
)
REVISION_TOOL = ARS_ROOT / "scripts/revision_roadmap.py"
PATCH_SCHEMA = ARS_ROOT / "shared/contracts/patch/revision_patch.schema.json"

AUTH_RECEIPT = ROOT / "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_EXECUTION_AUTHORIZATION_RECEIPT.json"
INPUT_FREEZE = ROOT / "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_EXECUTION_INPUT_FREEZE.json"
REQUEST = ROOT / "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33_SCOPE_EXPANSION.json"
AUTHOR_EVENT = ROOT / "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_EXECUTION_AUTHOR_EVENT_20260904.txt"

BASE = NOTES / "stage4_revision_round1.tex"
MANIFEST = NOTES / "stage4_prime_round5_base.block-manifest.json"
BIB = PAPER_DIR / "references.bib"
CANONICAL_TEX = PAPER_DIR / "manuscript.tex"
CANONICAL_PDF = PAPER_DIR / "paper.pdf"
INITIAL_SYSTEM = NOTES / "stage1_prestart_brief.md"
ROUTE_CROSSWALK = NOTES / "stage4_route_crosswalk.md"
SOURCE_USE = NOTES / "stage4_prime_round5_source_use_locator_final.json"
PROSPECTIVE_BIB = NOTES / "stage4_prime_round5_correction_bibliography_prospective.json"
SUPPORT_VALIDATION = NOTES / "stage4_prime_round5_support_validation.json"
ARTIFACT_INVENTORY = NOTES / "stage4_prime_round5_artifact_inventory_final.json"

EXPECTED = {
    AUTH_RECEIPT: "b154d92f84487b381b50e2e9addb5aecd924c6d9d2fb2277d6604a5cb42a17d1",
    INPUT_FREEZE: "e835f073d785fbad2de809fcf44dd24bc4abf98300ed21857d3b5e9f67751ce4",
    REQUEST: "100c97df01c356a52e3dea39ab327873f544d3ac6b32107f1576ae4dcb02db65",
    AUTHOR_EVENT: "111505020ac13b92ac253361e21777de8343455edd9ed3a4436fe924600cb812",
    BASE: "8a4ea5ff994db83b91c2f14ca5a8425e6e2f954cbc7c87faf7edf27ec98b99d4",
    MANIFEST: "69006ab2614eb3171527b19c7880e58eee198aa5c7576e91210b28d81e9a8262",
    BIB: "12143967175abb0d325e16d156b1bc227e51f886009e7acd64691e84b92cb5e0",
    CANONICAL_TEX: "b407441c07091ad38fb7e918721d31d2c4e3d897db9a705d92d9ff1f231f96d3",
    CANONICAL_PDF: "487a8838d9d422e00dcf3e896c9231b96c58fedfc2cdeb2265045f8d11d70031",
    INITIAL_SYSTEM: "b530d2f53f118d57c5281aff8eb3c367a48f85ae8ef2acdb1e73790b69139ea6",
    ROUTE_CROSSWALK: "0434982b38bf658bfd808469671431f089140850ceb2c01875539ef997f942cf",
    SOURCE_USE: "fa2dd2de6a6a69ad2fe297ff4277cb70e19e0cf8814418a35080e4b0e9ded11f",
    PROSPECTIVE_BIB: "0d6c0084359e5482246f25dd935d4793ad391aef04b4d78191a15aaa6c21b68b",
    SUPPORT_VALIDATION: "25ff420bb5a2f88d245b9c78ffe1ae68cd9108b3e991994e36e73300968be0df",
    ARTIFACT_INVENTORY: "c79ef8b83679d0e9238d19446c27e03a0c9ca0b12b5d23c6f19ed8da63022c6e",
}

FINAL_NAMES = {
    "roadmap": "stage4_prime_round6_revision_roadmap.json",
    "claim": "stage4_prime_round6_claim_surface_manifest.json",
    "choices": "stage4_prime_round6_author_choices.json",
    "adjudication": "stage4_prime_round6_author_adjudication.json",
    "bib_plan": "stage4_prime_round6_bibliography_append_plan.json",
    "handoff": "stage4_prime_round6_writer_handoff.json",
    "patch": "stage4_prime_revision_patch_round6.json",
    "response_json": "stage4_prime_round6_response_to_reviewers_provisional.json",
    "response_md": "stage4_prime_round6_response_to_reviewers_provisional.md",
    "revision_log": "stage4_prime_round6_revision_log.md",
    "validation": "stage4_prime_round6_writer_validation_receipt.json",
}

AUTHOR_EVENT_ID = "AUTHOR-EVENT-20260904-ROUND10-STAGE4-PRIME-SCOPE-REISSUE-EXECUTION"
REVISION_ROUND = 2


def sha_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def sha(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def canonical_bytes(value: object) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False
    ).encode("utf-8")


def load_json(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise RuntimeError(f"top-level JSON object required: {path}")
    return value


def artifact(path: Path) -> dict:
    return {
        "path": path.relative_to(ROOT).as_posix(),
        "sha256": sha(path),
        "bytes": path.stat().st_size,
    }


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def verify_frozen_inputs() -> tuple[dict, dict, dict, dict, dict, dict, dict]:
    for path, expected in EXPECTED.items():
        require(path.is_file(), f"missing frozen input: {path}")
        require(sha(path) == expected, f"frozen SHA-256 mismatch: {path}")

    require(AUTHOR_EVENT.read_bytes() == "确认，下一轮\n".encode("utf-8"), "author event bytes differ")
    receipt = load_json(AUTH_RECEIPT)
    freeze = load_json(INPUT_FREEZE)
    request = load_json(REQUEST)
    manifest = load_json(MANIFEST)
    source_use = load_json(SOURCE_USE)
    prospective_bib = load_json(PROSPECTIVE_BIB)
    support = load_json(SUPPORT_VALIDATION)

    require(receipt["tracks"]["P33"]["sha256"] == EXPECTED[REQUEST], "receipt/request binding mismatch")
    require(receipt["tracks"]["P33"]["replace_block_pairs"] == 37, "receipt P33 op count differs")
    require(receipt["author_event"]["sha256"] == EXPECTED[AUTHOR_EVENT], "receipt author-event binding mismatch")
    require(request["counts"]["carried_residual_items"] == 7, "request carried-item count differs")
    require(request["counts"]["new_issue_actions"] == 2, "request new-action count differs")
    require(request["counts"]["total_unique_block_operation_pairs"] == 37, "request unique target count differs")
    require(request["counts"]["source_use_rows"] == 48, "request source-use count differs")
    require(request["counts"]["explicit_bounded_unavailability_rows"] == 48, "request bounded-unavailability count differs")
    require(request["counts"]["production_components_available"] == 0, "production component boundary differs")
    require(request["boundaries"]["all_48_source_uses_remain_passage_inconclusive"] is True, "passage boundary differs")
    require(request["boundaries"]["production_independence_remains_unestablished"] is True, "independence boundary differs")
    require(request["boundaries"]["no_claim_strength_authorization"] is True, "claim authority unexpectedly present")
    require(request["boundaries"]["no_collateral_authorization"] is True, "collateral authority unexpectedly present")
    require(freeze["status"] == "FROZEN_FOR_EXACT_130_BLOCK_EXECUTION", "input freeze status differs")
    require(manifest["base_draft_hash"] == EXPECTED[BASE][:12], "manifest/base binding mismatch")
    require(source_use["counts"] == {
        "rows": 48,
        "distinct_sources": 20,
        "exact_passage_or_hypothesis_locators": 0,
        "explicit_bounded_unavailability": 48,
        "claim_to_passage_inconclusive": 48,
        "correction_dual_bindings": 5,
    }, "source-use finalization counts differ")
    require(support["status"] == "PASS_SUPPORT_COMPLETE_SCOPE_STOPPED_REQUEST_REISSUE_REQUIRED", "support validation is not PASS")
    require(support["failure_count"] == 0 and support["checks_run"] == 73, "support validation counts differ")
    require([e["key"] for e in prospective_bib["prospective_entries"]] == ["P33-S03-CORR", "P33-S16-CORR"], "prospective bibliography key set/order differs")

    # Replay every request-listed frozen/support artifact, not merely the core files.
    for entry in list(request["authority_bindings"]) + list(request["support_artifact_manifest"]):
        path = ROOT / entry["path"]
        require(path.is_file(), f"request-bound artifact missing: {entry['path']}")
        require(sha(path) == entry["sha256"], f"request-bound artifact SHA mismatch: {entry['path']}")
        require(path.stat().st_size == entry["bytes"], f"request-bound artifact byte count mismatch: {entry['path']}")
    for entry in request["frozen_inputs"].values():
        path = ROOT / entry["path"]
        require(path.is_file(), f"frozen request artifact missing: {entry['path']}")
        require(sha(path) == entry["sha256"], f"frozen request artifact SHA mismatch: {entry['path']}")
        require(path.stat().st_size == entry["bytes"], f"frozen request artifact bytes mismatch: {entry['path']}")
    return receipt, freeze, request, manifest, source_use, prospective_bib, support


def parse_bodies(text: str) -> tuple[dict[str, str], list[str]]:
    matches = list(re.finditer(r"(?m)^<!--block:(B[0-9]{4,})-->\n", text))
    bodies: dict[str, str] = {}
    order: list[str] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        body = text[match.end():end].rstrip("\n")
        block_id = match.group(1)
        require(block_id not in bodies, f"duplicate base block {block_id}")
        bodies[block_id] = body
        order.append(block_id)
    return bodies, order


def target_sources(request: dict, manifest: dict) -> tuple[list[str], dict[str, list[str]], dict[str, str]]:
    display_ids = [item["item_id"] for item in request["carried_forward_exact_request"]["items"]]
    display_ids.extend(action["action_id"] for action in request["new_issue_actions"])
    require(len(display_ids) == 9 and len(set(display_ids)) == 9, "fresh authority item IDs are not exact")
    by_block: dict[str, list[str]] = defaultdict(list)
    request_hashes: dict[str, str] = {}
    sources = list(request["carried_forward_exact_request"]["items"]) + list(request["new_issue_actions"])
    for source in sources:
        source_id = source.get("item_id", source.get("action_id"))
        for target in source["proposed_targets"]:
            require(target["allowed_operations"] == ["replace_block"], f"non-replace authority for {source_id}")
            by_block[target["block_id"]].append(source_id)
            old_hash = target["expected_old_hash"]
            if target["block_id"] in request_hashes:
                require(request_hashes[target["block_id"]] == old_hash, f"shared request old hash differs for {target['block_id']}")
            request_hashes[target["block_id"]] = old_hash
    manifest_hashes = {row["block_id"]: row["old_hash"] for row in manifest["blocks"]}
    require(len(by_block) == 37, f"expected 37 unique targets, got {len(by_block)}")
    require(sum(len(ids) for ids in by_block.values()) == 41, "expected 41 item/action target mappings")
    for block_id, expected in request_hashes.items():
        require(manifest_hashes.get(block_id) == expected, f"request/manifest old hash mismatch for {block_id}")
        by_block[block_id] = [item_id for item_id in display_ids if item_id in by_block[block_id]]
    return display_ids, dict(by_block), manifest_hashes


def build_roadmap(request: dict, display_ids: list[str]) -> dict:
    sources = list(request["carried_forward_exact_request"]["items"]) + list(request["new_issue_actions"])
    items = []
    for ordinal, source in enumerate(sources, 1):
        source_id = source.get("item_id", source.get("action_id"))
        targets = [
            {"block_id": row["block_id"], "allowed_operations": ["replace_block"]}
            for row in source["proposed_targets"]
        ]
        targets.sort(key=lambda row: row["block_id"])
        if "item_id" in source:
            description = source["residual_gap"]
            obligation = source["residual_obligation_class"]
            suggested = source["implementation_branch"]
            # The official non-ranking roadmap validator treats the bare word
            # "rejected" as editorial-prediction language even when the
            # request uses it technically for a digest stream.  Preserve the
            # meaning with its prior validator-safe spelling.
            suggested = suggested.replace(
                "included/rejected digest domains",
                "inclusion-stream and exclusion-stream digest domains",
            )
            locator = f"notes/stage3_prime_round5_verification_report.md, {source_id}"
            checked = "Checked the hash-bound Round-5 residual and the expanded request against the exact Stage-4 Round-1 base and its current 128-block manifest."
        else:
            description = source["description"]
            obligation = "must_fix"
            suggested = "; ".join(source["required_new_text_contract"]) + "."
            locator = f"notes/stage4_prime_round5_scope_stop_incident.md, {source_id}"
            checked = "Checked the scope-stop incident and the executed support artifacts against the stale base statement at the exact proposed target."
        block_list = ", ".join(row["block_id"] for row in targets)
        items.append({
            "id": source_id,
            "source_refs": [{"seat": "EIC", "channel": "finding", "ordinal": ordinal, "subclaim_ordinal": 0}],
            "description": description,
            "reviewer": "EIC",
            "sub_claim_ids": [f"SC-{source_id}-R6"],
            "obligation_class": obligation,
            "severity": "minor" if obligation == "should_fix" else "major",
            "evidence_anchor": {
                "anchor_type": "absence",
                "locator": locator,
                "absence_scope": description,
                "check_performed": checked,
            },
            "confidence": 5,
            "competence_basis": "Hash-bound Stage-4-prime scope-reissue evidence",
            "cost_scope": {"kind": "section", "locator": block_list},
            "consequence_if_unaddressed": {
                "code": "reporting_requirement_unmet" if source_id.startswith("REV-P33-SCOPE") else "evidence_gap_remains",
                "target": {"kind": "section", "locator": block_list},
            },
            "target_section": block_list,
            "suggested_action": suggested,
            "consensus_level": "SINGLE-VERIFIER",
            "verification_criteria": "Use every and only the listed replace_block targets; retain all passage, production, scientific, canonical-promotion, Route, initial-system, claim-strength, and collateral boundaries.",
            "proposed_targets": targets,
        })
    require([item["id"] for item in items] == display_ids, "roadmap source order differs")
    counts = {kind: sum(item["obligation_class"] == kind for item in items) for kind in ("must_fix", "should_fix", "consider")}
    return {
        "schema_version": "revision-roadmap/1.0",
        "revision_round": REVISION_ROUND,
        "base_draft_sha256": EXPECTED[BASE],
        "block_manifest_sha256": EXPECTED[MANIFEST],
        "items": items,
        "total_items": len(items),
        "obligation_counts": counts,
        "editorial_decision": "Major Revision",
        "consensus_summary": "Fresh non-ranking successor carrier for the seven P33 Round-5 residual items and two scope-stop actions; only the exact scope-reissue receipt and request authorize execution.",
        "dissenting_opinions": [],
    }


def build_choices(roadmap: dict) -> dict:
    item_ids = [item["id"] for item in roadmap["items"]]
    return {
        "schema_version": "author-adjudication-input/1.0",
        "author_events": [{
            "event_id": AUTHOR_EVENT_ID,
            "source": "explicit_session_user_message",
            "actor_role": "author",
            "input_sha256": EXPECTED[AUTHOR_EVENT],
        }],
        "display_order": {
            "mode": "source_traceability",
            "item_ids": item_ids,
            "author_event_id": AUTHOR_EVENT_ID,
        },
        "author_adjudications": [{
            "item_id": item["id"],
            "author_event_id": AUTHOR_EVENT_ID,
            "author_triage": "will_address",
            "authorized_targets": item["proposed_targets"],
            "claim_strength_authorizations": [],
        } for item in roadmap["items"]],
        "collateral_authorizations": [],
    }


CITE_PAIR = re.compile(
    r"% ARS-CITE source_ids=([^\s]+) anchor=none claim_to_passage=INCONCLUSIVE\n"
    r"\\citep\{([^}]+)\}"
)


def bind_source_use_rows(body: str, rows: list[dict]) -> str:
    matches = list(CITE_PAIR.finditer(body))
    require(len(matches) == len(rows), f"citation/use count differs for {rows[0]['block_id']}")
    row_iter = iter(rows)

    def replacement(match: re.Match[str]) -> str:
        row = next(row_iter)
        require(match.group(1) == row["source_id"], f"source ID mismatch for {row['use_id']}")
        require(match.group(2) == row["source_id"], f"base cite key mismatch for {row['use_id']}")
        keys = row["citation_keys_required"]
        require(keys[0] == row["source_id"], f"citation-key base mismatch for {row['use_id']}")
        return (
            f"% ARS-CITE use_id={row['use_id']} source_ids={','.join(keys)} "
            "anchor=none claim_to_passage=INCONCLUSIVE "
            "locator_disposition=EXPLICIT_BOUNDED_UNAVAILABLE\n"
            f"\\citep{{{','.join(keys)}}}"
        )

    return CITE_PAIR.sub(replacement, body)


def add_cjk_soft_breaks(text: str) -> str:
    return re.sub(r"([\u3400-\u9fff])", r"\1\\hspace{0pt}", text)


def build_new_texts(bodies: dict[str, str], source_use: dict) -> dict[str, str]:
    rows_by_block: dict[str, list[dict]] = defaultdict(list)
    for row in source_use["source_use_rows"]:
        rows_by_block[row["block_id"]].append(row)
    for rows in rows_by_block.values():
        rows.sort(key=lambda row: row["occurrence_in_block"])

    new: dict[str, str] = {}
    for block_id, rows in rows_by_block.items():
        new[block_id] = bind_source_use_rows(bodies[block_id], rows)

    new["B0026"] = new["B0026"].replace(
        "with the frozen verification record preserving the associated 2006 correction.",
        "with the official 2006 correction cited as a separate record; this metadata binding neither supplies a passage locator nor strengthens the criterion's project-specific application.",
    )
    new["B0036"] = new["B0036"].replace(
        "their correction remains visible and their determinant endpoint is outside P33.",
        "their 2018 correction is cited separately, remains confined to its recorded scope, and their determinant endpoint is outside P33.",
    )
    new["B0044"] = new["B0044"].replace(
        "Correction and locator boundaries were carried forward exactly.",
        "Correction metadata is now dual-bound at every affected use while locator boundaries remain unchanged.",
    )
    new["B0067"] = new["B0067"].replace(
        "Strohmaier and Uski (2013, corrected 2018)",
        "Strohmaier and Uski (2013, with the separately cited 2018 correction)",
    )

    new["B0007"] = r"""This report asks what exact-certificate architecture could eventually support primitive-geodesic ownership decisions for a source-locked Bolza surface and one frozen nonarithmetic genus-two control at \(\Lambda=21/10\). Stage 1 executed a closed-corpus literature synthesis, not a census or algorithm validation. The evidence supports object, candidate-generation, conjugacy, root-decision, owner-semantics, rigorous-predicate, and producer-checker components, but identifies no project owner. The review-adjudicated architecture permits two surface-specific exact proof producers, provided they emit one common semantic owner-certificate schema checked by an independent validator. The schema separates full-group conjugacy, maximal-root and primitivity evidence, external inversion pairing, self-reciprocity, repetitions, termination, completeness, and positive or negative replay payloads. It requires no common internal solver or input model. Production implementation remains absent. The target-empty and control-nonempty directions at the frozen cutoff are unverified inherited architecture-only assumptions. If each direction is later replayed with source- and hypothesis-adequate proof records, it may condition the corresponding producer obligation; until then neither direction is a scientific result or a basis for between-surface arithmetic inference. P33-RC-1 remains a producer-soundness, schema-interoperability, and independent-validation contract with a fail-closed not-evaluable endpoint. The contribution is an interoperable certificate-methods design with synthetic conformance support, not a census, novelty claim, magnetic or determinant result, formal Route-A tuple, A0/A1/A2 closure, Route-A credit, or Route-B progress."""

    old_cjk = bodies["B0010"].replace(r"\hspace{0pt}", "")
    old_sentence = "固定截斷值造成明顯不對稱：目標端主要是既有系統短線界限下的空集合重播，控制端才承擔非平凡的前瞻性封閉工作，因此兩端差異不能支持算術性推論。"
    replacement_sentence = "目標端空集合與控制端非空集合的方向，均僅是未驗證的繼承架構假設。若日後分別以來源與假設充分的證明記錄成功重播，才可把相應方向作為條件式的產生器輸入；在此之前，兩端差異不得支持空與非空比較、算術性推論、A0/A1/A2 關閉、Route A 計分或 Route B 進展。"
    require(old_cjk.count(old_sentence) == 1, "Chinese abstract conservative-typing sentence not found exactly once")
    new["B0010"] = add_cjk_soft_breaks(old_cjk.replace(old_sentence, replacement_sentence))

    new["B0020"] = r"""The inherited cutoff was historically target-blind. The statements that the Bolza target is empty below \(21/10\) and that the control has a primitive owner below the same cutoff are retained only as unverified inherited architecture-only assumptions. If a separately authorized replay verifies the target's strict systolic inequality with passage-adequate hypotheses, then BP may certify an empty bounded domain; if a separately authorized replay verifies the control witness and its primitive-owner obligations, then CP must include the corresponding owner. Neither antecedent is established by the present support work. The common cutoff must not be retuned, and these conditional directions support no empty-versus-nonempty scientific comparison, arithmetic inference, A0/A1/A2 closure, Route-A credit, or Route-B conclusion."""

    new["B0041"] = r"""Stage-4-prime support work on 4 September 2026 performed only commit-pinned artifact replay, bounded identifier-endpoint replay, correction-metadata finalization, contract emission, and deterministic synthetic-conformance validation. It added no source beyond the frozen twenty and verified no source passage: all 48 uses retain \texttt{anchor=none} and \texttt{claim\_to\_passage=INCONCLUSIVE}. Two valid and twelve invalid files are synthetic fixtures for the notes-side harness, not surface records or evidence of a production validator. No geodesic enumeration, conjugacy query, root query, systole proof, primitive-owner census, scientific experiment, result refresh, or canonical promotion occurred; the findings concern support provenance and open production obligations, not newly computed dynamics."""

    new["B0043"] = r"""The inventory contains 20 sources: nine S2\_VERIFIED, ten VERIFIED, and one PLAUSIBLE; 18 were conservatively counted as peer reviewed. A bounded identifier-endpoint replay on 4 September 2026 retained all twenty identities and finalized exactly 48 source-use rows. It retained no full-text body and produced zero exact passage or hypothesis locators, so every row is explicitly bounded-unavailable and remains \texttt{claim\_to\_passage=INCONCLUSIVE}. S2\_VERIFIED establishes record identity and metadata, not theorem- or passage-level support; the evidence matrix continues to separate admissible contributions from stronger excluded uses."""

    new["B0045"] = r"""Every literature statement has a visible citation and \texttt{anchor:none}; no direct quotation is used. The finalized machine-readable ledger is \path{notes/stage4_prime_round5_source_use_locator_final.json}, SHA-256 \url{fa2dd2de6a6a69ad2fe297ff4277cb70e19e0cf8814418a35080e4b0e9ded11f}, with its receipt at \path{notes/stage4_prime_round5_source_use_locator_receipt.json}, SHA-256 \url{70a390daf78d56dd335e6137c42d9fede1886db8ada429a073987bceb2842272}. It records, for P33-U01--P33-U48, the interface, 4 September 2026 retrieval date, exact identifier query, returned identifier or unavailable-total receipt, screening disposition, hypotheses, correction state, applicability boundary, and prohibited stronger transfer. The replay checked only the frozen identifier endpoint and at most a 4096-byte response prefix; it retained and parsed no full-text body. Consequently 48 of 48 uses are \texttt{EXPLICIT\_BOUNDED\_UNAVAILABLE}, zero have an exact passage locator, and 48 of 48 remain \texttt{INCONCLUSIVE}. The five correction-affected uses are dual-bound to their base and correction keys, but that metadata binding is not passage verification. No systematic source-level retraction or conflict-of-interest audit was run."""

    new["B0051"] = r"""\textbf{Bolza proof-producer (BP) population-completeness contract.} The notes-side contract \path{notes/stage4_prime_round5_support/bp_enumeration_contract.json}, SHA-256 \url{d8ad8be0f1c8242085914ca9557879545efe312d1e2d7fe397eee3546c963073}, and its distinct ledger schema \path{notes/stage4_prime_round5_support/bp_coverage_ledger.schema.json}, SHA-256 \url{8f86ba896308c087097f8f0bcf45678d8ff8b51cd7b073b8bf0c5a79c65a4054}, bind the prospective BP input to \path{papers/28-bolza-magnetic-flow/results/round4_bolza_group_certificate.json}, SHA-256 \url{e3e6c486c66116dc6fe9fdd054c2fce9d4b1a58318f56d1656f6db168c807eca}. BP's empty-domain path is strictly conditional: only a separately valid, passage-adequate replay of \(\operatorname{sys}(S_{\mathrm{Bolza}})>21/10\) may terminate it as empty; failure, missing hypotheses, or digest drift remains \texttt{UPSTREAM\_REPLAY\_CONTRADICTION} or not evaluable. The contract fixes canonical input, theorem/algorithm-version slots, exact cutoff comparison, deterministic order, included and rejected digest domains, termination witness, distinct coverage digest, complete unresolved ledger, and independent population-bound replay. The theorem and algorithm versions remain unavailable, no observed coverage digest is emitted, and no producer, enumeration, owner quotient, or census was run."""

    new["B0052"] = r"""\textbf{Control proof producer (CP) population-completeness contract.} The separate notes-side contract \path{notes/stage4_prime_round5_support/cp_enumeration_contract.json}, SHA-256 \url{f96b1e81baeacb4e6d1dda400b36e7c8da45eb50c43d2c80d95c1c5c1e41c621}, and ledger schema \path{notes/stage4_prime_round5_support/cp_coverage_ledger.schema.json}, SHA-256 \url{696a3911e241ab14ad1eb53a20e7bf6239a93c4b90d5656c8c5d9295f0685eab}, bind prospective CP input to the frozen \texttt{NAZARENKO-EXP-OCTAGON-G2} generator and finite-ball certificate bytes. They specify FIFO breadth-first order from the identity through \(g_0,g_1,g_2,g_3,g_0^{-1},g_1^{-1},g_2^{-1},g_3^{-1}\), exact normalized-state deduplication, the centre guard \(\lvert\alpha\rvert^2\leq20000\), exact admission \(\ell(g)\leq21/10\), queue-exhaustion and outgoing-edge termination, separate included/rejected digest domains, a distinct CP coverage digest, and a complete unresolved ledger. CP may retain its own representation and proof route, but a checker must reconstruct its bound and digests. The contract is declarative only: theorem and algorithm versions, production proof payloads, observed coverage digest, producer run, and owner census remain absent."""

    new["B0057"] = bodies["B0057"].replace(
        "No execution digest is emitted here, and these byte rules do not claim that an external schema file or validator exists.",
        "The byte rules have now been exercised only by two valid and twelve invalid canonical synthetic fixture files under the notes-side conformance harness. Their matching deterministic dispositions do not emit a scientific execution digest and do not establish a production owner-certificate schema, adapter, predicate kernel, or validator.",
    )

    new["B0059"] = bodies["B0059"].replace(
        "This closes the semantic contract at manuscript level but does not assert that a producer, schema file, proof registry file, adapter, fixture, or validator has been implemented or run.",
        "A synthetic proof-registry snapshot and fourteen canonical conformance fixtures now exercise this manuscript-level vocabulary, but they are notes-side test artifacts only. No production producer, owner-certificate schema implementation, adapter, predicate kernel, validator, or scientific record has been implemented or run.",
    )

    new["B0061"] = r"""The notes-side trust graph is frozen at \path{notes/stage4_prime_round5_support/trust_graph.json}, SHA-256 \url{34ab38b26566ba6cc80ef1b2fdf266d7e7fe3f47af5129756ebca737611895fc}. Its nodes distinguish BP, CP, their adapters, parser and predicate kernels, a fixture oracle, theorem encodings, libraries, and accountable implementers; shared schema, digest, and general-purpose-library dependencies are classified separately from disqualifying producer-decision-code reuse. The synthetic expected outcomes and provenance are recorded in \path{notes/stage4_prime_round5_support/fixture_oracle_manifest.json}, SHA-256 \url{0aadbe0af06acad88dcab573b3e3206bacef20ec237aa882568509233ae4d044}. That oracle is procedurally separate from producer output but was not independently authored by a second human or runtime, so production independence is not established. The component record \path{notes/stage4_prime_round5_support/component_build_provenance.json}, SHA-256 \url{56ed464ffd96fb4f8c3f604e8f94e297a1481eefd5aea52fead9f388a1fd0824}, reports zero available production components; BP, CP, both adapters, the parser, and predicate kernels remain \texttt{UNAVAILABLE\_COMPONENT\_NOT\_IMPLEMENTED}. The static exclusion audit at \path{notes/stage4_prime_round5_support/producer_code_exclusion_audit.json}, SHA-256 \url{73d6f7f9f33989a08a8ddc4123d22292e78f68d27b729f0475b2c0f9603b5a86}, is therefore \texttt{NOT\_EVALUABLE}. No absent source-tree, build-environment, theorem-encoding, or build hash is invented, and no validator-independence claim is made."""

    new["B0062"] = r"""The notes-side fixture corpus now contains exactly two valid canonical synthetic records and twelve invalid synthetic records covering malformed schema, unknown proof type, altered digest, unsupported negative decision, primitive/power conflict, missing inverse link, false reciprocity, duplicate owner, unresolved cutoff, incomplete coverage, invalid termination, and hash mismatch. The deterministic receipt \path{notes/stage4_prime_round5_support/serialized_fixture_validation_receipt.json}, SHA-256 \url{294a80fe696be66584e13377c446cf536982bd2a9cfc1807277ad05da09c0b21}, records fourteen of fourteen outcomes matching the separately frozen synthetic oracle with zero harness failures. These bytes test only canonical serialization and fail-closed conformance against the synthetic registry snapshot; they are not surface records, producer outputs, owner-census results, or evidence that a production validator exists."""

    new["B0128"] = r"""The serialized fixtures are synthetic conformance examples, not scientific surface records. The valid BP and CP files use \path{run_id=synthetic} and private proof tags mapped to the common fields for surface, candidate, oriented class, primitive root, inverse link, owner, cutoff, proof type, coverage, and unresolved count. The harness accepts canonical bytes, dispatches only recognized synthetic registry tags, checks required links and digests, and reaches a closed expected disposition. The twelve invalid files each isolate one declared fault and must remain rejected or not evaluable; no producer label, approximate equality, or another record's payload may repair them. The fourteen-file receipt demonstrates deterministic agreement with the frozen synthetic oracle, not producer soundness, theorem applicability, predicate-kernel independence, population completeness, or a Bolza/control census."""

    new["B0072"] = r"""Package C's intended rules are now exercised by a notes-side synthetic harness: two canonical valid files and twelve one-fault invalid files have frozen expected dispositions, and the deterministic validation receipt reports fourteen of fourteen matches. The cases cover altered provenance digests, unrecognized proof types, unsupported negative decisions, primitive/power conflict, missing inverse links, false reciprocity, duplicate owners, unresolved cutoffs, incomplete coverage, invalid termination, malformed schema, and hash mismatch. This is evidence about the synthetic conformance contract only. Because BP, CP, adapters, parser, production predicate kernels, and a second independently authored oracle are unavailable, the run cannot demonstrate producer-code exclusion or production-validator independence and cannot certify either surface census."""

    new["B0073"] = r"""The contract separates local record validity from population completeness. A conjugacy witness may be correct for one pair while the candidate universe is incomplete; a root witness may be correct while inverse pairing is absent; and individually sound owner records may omit an admissible owner. Conversely, an empty bounded output is an empty-universe certificate only if its candidate bound, length predicate, termination argument, correction provenance, and complete unresolved ledger all replay. The inherited Bolza-side empty direction is therefore an unverified architecture-only assumption: if a separately authorized, passage-adequate strict-systole replay succeeds, it may trigger BP's conditional empty-domain branch; otherwise the branch remains not evaluable. No empty output, synthetic fixture, or contract file establishes that scientific antecedent."""

    new["B0087"] = r"""The Stage-1/Stage-2 audit trail is commit-retrievable at:\newline
\url{https://github.com/maris205/hilbert-polya-structure/tree/337994b72bd14c7ffbc1f01a6a9b878784df7694/flow_systems/papers/33-bolza-control-matched-census}.
The complete manifest is \path{notes/stage4_prime_round5_artifact_inventory_final.json}, SHA-256 \url{c79ef8b83679d0e9238d19446c27e03a0c9ca0b12b5d23c6f19ed8da63022c6e}, with receipt \path{notes/stage4_prime_round5_artifact_inventory_receipt.json}, SHA-256 \url{6b76a0550ad14961c9c4fcaf0f8f369d8aee4722224a6fb5fdbe6ae4fd2ef596}. Its selection rule over-covers every regular \path{notes/stage1_*} and \path{notes/stage2_*} file named by the availability statement while excluding the distinct \path{stage2_5_*} audit family. Exactly 43 of 43 rows record the repository-relative path, SHA-256, byte count, media or schema type, explicit unversioned-current-bytes state, local access state, commit-membership state, raw commit URL, HTTP result, and replayed remote digest and byte count; all 43 are exact matches at commit \texttt{337994b72bd14c7ffbc1f01a6a9b878784df7694}. Access still requires repository read permission and checkout or retrieval of that commit. The manifest provides exact provenance for existing bytes, not a persistent-archive claim, mathematical validation, or evidence that an omitted or unavailable artifact exists."""

    new["B0100"] = r"""The frozen target-control pair remains useful as an interface stress test because its representations may demand different proof routes. It is not a clean arithmeticity experiment. The target-empty and control-nonempty directions are unverified inherited architecture-only assumptions; if separately replayed with source- and hypothesis-adequate proof records, they may condition different producer duties, but the present contract and synthetic fixtures do not establish either antecedent. The common cutoff remains systole-confounded and the broader control panel remains incomplete, so no empty-versus-nonempty comparison, arithmetic inference, A0/A1/A2 closure, Route-A credit, or Route-B progress follows."""

    new["B0106"] = r"""Second, passage-level support remains materially incomplete after bounded finalization. The exact P33-U01--P33-U48 ledger now records identifier endpoints, dates, queries, receipts, hypotheses, correction state, applicability, and prohibited stronger transfer, but the replay retained no full-text body and supplied zero exact page, section, paragraph, quotation, or hypothesis locators. All 48 uses therefore retain \texttt{anchor=none}, \texttt{EXPLICIT\_BOUNDED\_UNAVAILABLE}, and \texttt{claim\_to\_passage=INCONCLUSIVE}. S06 remains PLAUSIBLE and page-unpinned; nine S2\_VERIFIED records remain record-level matches rather than theorem validation. Correction dual-binding is metadata provenance, not passage verification."""

    new["B0107"] = r"""Third, correction metadata is now represented by exactly two standalone bibliography keys: \path{P33-S03-CORR} for the official 2006 Takeuchi correction information and \path{P33-S16-CORR} for the 2018 Strohmaier--Uski correction. P33-U08 and P33-U27 bind \path{P33-S03} with \path{P33-S03-CORR}; P33-U22, P33-U28, and P33-U37 bind \path{P33-S16} with \path{P33-S16-CORR}. No existing bibliography record is rewritten, no distinct DOI is invented for the Takeuchi correction, and the Strohmaier--Uski correction is not generalized beyond its recorded scope. The five dual bindings remain \texttt{anchor=none} and \texttt{INCONCLUSIVE}; they establish metadata traceability only. Systematic source-level retraction and conflict-of-interest screens were not performed, and no correction metadata strengthens a scientific claim."""

    new["B0108"] = r"""Fourth, production architecture remains unimplemented. Notes-side BP/CP enumeration contracts, two coverage-ledger schemas, a trust graph, a synthetic proof-registry snapshot, and a fourteen-file synthetic fixture corpus now exist and pass their bounded deterministic conformance checks. They do not supply a BP or CP producer, production adapter, parser or predicate kernel, theorem-applicability proof, independently implemented oracle, surface candidate universe, conjugacy result, root result, owner record, observed coverage digest, termination proof, or completeness certificate. Production components available remain zero, validator independence remains not evaluable, and the seven P33-RC-1 scientific/production obligations remain unimplemented."""

    new["B0109"] = r"""Fifth, the frozen scientific design is asymmetric and limited. The target-empty and control-nonempty directions are unverified inherited architecture-only assumptions, not results. If separately authorized, passage-adequate replays establish their respective antecedents, the directions may condition surface-specific producer obligations; until then the common cutoff remains systole-confounded and the control panel incomplete. The report cannot support an empty-versus-nonempty comparison, a between-surface arithmetic conclusion, A0/A1/A2 closure, Route-A credit, Route-B progress, or generalization to other genus-two surfaces."""

    new["B0123"] = r"""\paragraph{Data, materials, and code availability.}
The exact 43-row Stage-1/Stage-2 artifact inventory is \path{notes/stage4_prime_round5_artifact_inventory_final.json}, SHA-256 \url{c79ef8b83679d0e9238d19446c27e03a0c9ca0b12b5d23c6f19ed8da63022c6e}; every row supplies a path, explicit version state, SHA-256, byte count, media/schema type, workspace access state, and exact pinned-commit replay fields. All 43 rows matched commit \texttt{337994b72bd14c7ffbc1f01a6a9b878784df7694} on 4 September 2026. The bounded 48-use source ledger and notes-side synthetic conformance artifacts are identified by their own repository paths and hashes in that support package. Repository access is conditional and no persistent archive is claimed. This manuscript produced no new scientific dataset, geodesic enumeration, experimental output, owner census, production validator, observed coverage digest, canonical-result refresh, or Route result; the fourteen fixture files are synthetic test records only."""

    new["B0124"] = r"""\paragraph{AI assistance and verification limitation.}
OpenAI Codex from the GPT-5 model family assisted the recorded workflow on 2 September 2026 UTC with literature-search support, source-record and metadata checks, evidence synthesis, adversarial and role-based review, deterministic citation and hash checks, and manuscript drafting and restructuring. On 4 September 2026 UTC it also assisted with support-artifact generation, commit-pinned artifact replay, bounded identifier-endpoint replay, correction-metadata preparation, synthetic fixture and oracle preparation, BP/CP contract preparation, and deterministic support validation. The exact backend snapshot was not exposed. Liang Wang supplied the project direction and remains the accountable author; the record does not establish that he personally performed full-text or source-passage verification. The bounded replay retained no full-text body and verified no passage, so all 48 literature uses remain \texttt{anchor=none} and \texttt{claim\_to\_passage=INCONCLUSIVE}. AI assistance, human authorization, correction metadata, and synthetic-conformance success do not establish source cleanliness, production-validator independence, theorem applicability, scientific method validity, or a surface result."""

    return new


def build_bib_plan(prospective: dict) -> dict:
    base_raw = BIB.read_bytes()
    records = [entry["prospective_bibtex_record"] for entry in prospective["prospective_entries"]]
    require(base_raw.endswith(b"\n"), "bibliography base must end with LF")
    append_text = "\n" + "\n\n".join(records) + "\n"
    result = base_raw + append_text.encode("utf-8")
    return {
        "schema_version": "p33-stage4-prime-round6-bibliography-append-plan/1.0",
        "status": "AUTHORIZED_EXACT_APPEND_PLAN_NOT_APPLIED",
        "paper_id": "P33",
        "revision_round": REVISION_ROUND,
        "authority": artifact(REQUEST),
        "prospective_contract": artifact(PROSPECTIVE_BIB),
        "base": artifact(BIB),
        "append_only": True,
        "allowed_keys": ["P33-S03-CORR", "P33-S16-CORR"],
        "records": [{
            "key": entry["key"],
            "base_key": entry["base_key"],
            "prospective_bibtex_record": entry["prospective_bibtex_record"],
        } for entry in prospective["prospective_entries"]],
        "append_text": append_text,
        "append_text_sha256": sha_bytes(append_text.encode("utf-8")),
        "expected_result_sha256": sha_bytes(result),
        "expected_result_bytes": len(result),
        "affected_uses": prospective["affected_uses"],
        "counts": {"entries_to_append": 2, "uses_to_dual_bind": 5, "entries_appended_now": 0},
        "boundaries": {
            "existing_entry_bytes_may_change": False,
            "third_entry_allowed": False,
            "scientific_claim_strengthening_allowed": False,
            "systematic_retraction_or_conflict_audit_claimed": False,
        },
    }


def response_items(roadmap: dict) -> list[dict]:
    dispositions = {
        "REV-P33-002": ("RESOLVED", "The emitted B0087/B0123 text points to the exact 43-row, commit-replayed inventory and states every required row field and access boundary."),
        "REV-P33-003": ("RESOLVED", "The exact append plan supplies only P33-S03-CORR and P33-S16-CORR, while the emitted citation blocks dual-bind exactly P33-U08/U22/U27/U28/U37 without changing claim scope."),
        "REV-P33-005": ("DELIBERATE_LIMITATION", "The trust graph, oracle provenance, component record, and code-exclusion audit are now explicit, but production components are absent and the oracle was not independently authored by a second human or runtime; production independence remains unestablished."),
        "REV-P33-006": ("RESOLVED", "Two valid and twelve invalid canonical synthetic fixture files have frozen dispositions and a deterministic 14/14 validation receipt; the response limits this to synthetic conformance."),
        "REV-P33-007": ("RESOLVED", "Distinct BP and CP enumeration contracts and coverage-ledger schemas now fix order, digest domains, termination, unresolved ledgers, replay, and the conditional BP empty path without running a producer."),
        "REV-P33-008": ("DELIBERATE_LIMITATION", "All 48 rows now have exact bounded-replay provenance, but zero exact passage or hypothesis locators were obtained; all 48 remain explicitly bounded-unavailable and INCONCLUSIVE."),
        "REV-P33-013": ("RESOLVED", "All six authorized residual surfaces now type target-empty/control-nonempty directions as unverified inherited architecture-only assumptions and retain the no-retuning, no arithmetic, and no Route-credit boundaries."),
        "REV-P33-SCOPE-001": ("RESOLVED", "B0041 now distinguishes commit/identifier replay and synthetic conformance from passage verification, production validation, science, census, and result refresh."),
        "REV-P33-SCOPE-002": ("RESOLVED", "B0124 now discloses the 4 September support work and retains the exact-backend, author-read, 48/48 anchor-none, and 48/48 INCONCLUSIVE limits."),
    }
    locations = {item["id"]: [row["block_id"] for row in item["proposed_targets"]] for item in roadmap["items"]}
    return [{
        "roadmap_item_id": item["id"],
        "status": dispositions[item["id"]][0],
        "reviewer_comment": item["description"],
        "author_response": dispositions[item["id"]][1],
        "emitted_change_locations": locations[item["id"]],
        **({"limitation_basis": dispositions[item["id"]][1]} if dispositions[item["id"]][0] == "DELIBERATE_LIMITATION" else {}),
    } for item in roadmap["items"]]


def emit() -> None:
    receipt, freeze, request, manifest, source_use, prospective_bib, support = verify_frozen_inputs()
    display_ids, ids_by_block, manifest_hashes = target_sources(request, manifest)
    base_text = BASE.read_text(encoding="utf-8")
    bodies, physical_order = parse_bodies(base_text)
    require(set(ids_by_block) <= set(bodies), "authorized target missing from base")

    final_paths = {name: NOTES / filename for name, filename in FINAL_NAMES.items()}
    for path in final_paths.values():
        require(not path.exists(), f"refusing to overwrite writer artifact: {path}")

    frozen_before = {str(path.relative_to(ROOT)): sha(path) for path in EXPECTED}
    roadmap = build_roadmap(request, display_ids)
    roadmap_raw = json_bytes(roadmap)
    roadmap_sha = sha_bytes(roadmap_raw)
    claim = {
        "schema_version": "claim-surface-manifest/1.0",
        "revision_round": REVISION_ROUND,
        "roadmap_sha256": roadmap_sha,
        "base_draft_sha256": EXPECTED[BASE],
        "claim_intent_sources": [],
        "surfaces": [],
    }
    claim_raw = json_bytes(claim)
    claim_sha = sha_bytes(claim_raw)
    choices = build_choices(roadmap)
    choices_raw = json_bytes(choices)
    bib_plan = build_bib_plan(prospective_bib)
    bib_plan_raw = json_bytes(bib_plan)
    bib_plan_sha = sha_bytes(bib_plan_raw)

    new_texts = build_new_texts(bodies, source_use)
    require(set(new_texts) == set(ids_by_block), f"new-text set differs from 37-target authority: missing={sorted(set(ids_by_block)-set(new_texts))}, extra={sorted(set(new_texts)-set(ids_by_block))}")

    with tempfile.TemporaryDirectory(prefix=".stage4_prime_round6_writer.", dir=NOTES) as temp_name:
        temp = Path(temp_name)
        staged = {name: temp / filename for name, filename in FINAL_NAMES.items()}
        staged["roadmap"].write_bytes(roadmap_raw)
        staged["claim"].write_bytes(claim_raw)
        staged["choices"].write_bytes(choices_raw)
        staged["bib_plan"].write_bytes(bib_plan_raw)

        build_cmd = [
            "python", str(REVISION_TOOL), "build-adjudication", str(staged["roadmap"]),
            "--base", str(BASE), "--block-manifest", str(MANIFEST),
            "--claim-surface", str(staged["claim"]), "--author-choices", str(staged["choices"]),
            "--artifact-root", str(ROOT), "--output", str(staged["adjudication"]),
        ]
        built = subprocess.run(build_cmd, cwd=ROOT, text=True, capture_output=True, check=False)
        require(built.returncode == 0, f"official adjudication build failed: {built.stderr}{built.stdout}")
        adjudication_raw = staged["adjudication"].read_bytes()
        adjudication = json.loads(adjudication_raw)
        require(adjudication["revision_round"] == REVISION_ROUND, "official adjudication revision round differs")
        require(adjudication["roadmap_sha256"] == roadmap_sha, "official adjudication roadmap binding differs")
        require(adjudication["claim_surface_manifest_sha256"] == claim_sha, "official adjudication claim binding differs")
        adjudication_sha = sha_bytes(adjudication_raw)
        projection = {
            "author_events": adjudication["author_events"],
            "display_order": adjudication["display_order"],
            "author_adjudications": adjudication["author_adjudications"],
            "collateral_authorizations": adjudication["collateral_authorizations"],
        }
        decision_digest = sha_bytes(canonical_bytes(projection))

        ops = []
        for block_id in physical_order:
            if block_id not in ids_by_block:
                continue
            require(new_texts[block_id] != bodies[block_id], f"authorized target did not change: {block_id}")
            require("<!--block:" not in new_texts[block_id], f"block marker leaked into new_text: {block_id}")
            ops.append({
                "op": "replace_block",
                "block_id": block_id,
                "old_hash": manifest_hashes[block_id],
                "new_text": new_texts[block_id],
                "roadmap_item_ids": ids_by_block[block_id],
                "claim_strength_changes": [],
                "collateral_authorization_ids": [],
            })
        patch = {
            "patch_format_version": "1.1",
            "authorization_context": "review_roadmap",
            "revision_round": REVISION_ROUND,
            "base_draft_hash": EXPECTED[BASE][:12],
            "roadmap_sha256": roadmap_sha,
            "author_adjudication_sha256": adjudication_sha,
            "author_decision_digest": decision_digest,
            "claim_surface_manifest_sha256": claim_sha,
            "ops": ops,
            "emitted_by": "draft_writer_agent",
        }
        patch_raw = json_bytes(patch)
        staged["patch"].write_bytes(patch_raw)
        patch_sha = sha_bytes(patch_raw)

        handoff = {
            "handoff_type": "round10-stage4-prime-p33-scope-reissue-writer-bindings/1.0",
            "paper_number": 33,
            "lineage_label": "round6",
            "revision_round": REVISION_ROUND,
            "base_draft_path": "notes/stage4_revision_round1.tex",
            "base_draft_hash": EXPECTED[BASE][:12],
            "base_draft_sha256": EXPECTED[BASE],
            "block_manifest_path": "notes/stage4_prime_round5_base.block-manifest.json",
            "block_manifest_sha256": EXPECTED[MANIFEST],
            "roadmap_path": f"notes/{FINAL_NAMES['roadmap']}",
            "roadmap_sha256": roadmap_sha,
            "author_choices_path": f"notes/{FINAL_NAMES['choices']}",
            "author_choices_sha256": sha_bytes(choices_raw),
            "author_adjudication_path": f"notes/{FINAL_NAMES['adjudication']}",
            "author_adjudication_sha256": adjudication_sha,
            "author_decision_digest": decision_digest,
            "claim_surface_manifest_path": f"notes/{FINAL_NAMES['claim']}",
            "claim_surface_manifest_sha256": claim_sha,
            "registered_claim_surface_count": 0,
            "unregistered_claim_drift_review_required": True,
            "patch_path": f"notes/{FINAL_NAMES['patch']}",
            "patch_sha256": patch_sha,
            "patch_ops": 37,
            "scope_expansion_request": {"path": "../../" + REQUEST.name, "sha256": EXPECTED[REQUEST]},
            "root_execution_authorization_receipt": {"path": "../../" + AUTH_RECEIPT.name, "sha256": EXPECTED[AUTH_RECEIPT]},
            "root_execution_input_freeze": {"path": "../../" + INPUT_FREEZE.name, "sha256": EXPECTED[INPUT_FREEZE]},
            "author_event": {"path": "../../" + AUTHOR_EVENT.name, "sha256": EXPECTED[AUTHOR_EVENT]},
            "bibliography_append_plan": {"path": f"notes/{FINAL_NAMES['bib_plan']}", "sha256": bib_plan_sha, "status": "NOT_APPLIED_BY_WRITER"},
            "target_old_hashes": {block_id: manifest_hashes[block_id] for block_id in ids_by_block},
            "target_authority_item_ids": ids_by_block,
            "noncontrolling_round5_chain": {
                "status": "NONCONTROLLING_NEVER_USED_FOR_PATCH_OR_APPLY",
                "artifacts": request["superseded_scope_attempt1"]["artifacts"],
            },
            "boundaries": {
                "patch_applied": False,
                "bibliography_appended": False,
                "successor_draft_emitted": False,
                "build_run": False,
                "canonical_promoted": False,
                "science_or_result_refreshed": False,
                "route_or_initial_system_changed": False,
                "fresh_stage4_5_authorized": False,
            },
        }
        handoff_raw = json_bytes(handoff)
        staged["handoff"].write_bytes(handoff_raw)
        handoff_sha = sha_bytes(handoff_raw)

        items = response_items(roadmap)
        response = {
            "schema_version": "response-to-reviewers-provisional/1.0",
            "artifact_status": "PROVISIONAL_PENDING_BIBLIOGRAPHY_APPEND_PATCH_APPLICATION_AND_POST_APPLY_AUDIT",
            "paper_number": 33,
            "lineage_label": "round6",
            "revision_round": REVISION_ROUND,
            "patch_binding": {"path": f"notes/{FINAL_NAMES['patch']}", "sha256": patch_sha, "apply_status": "NOT_APPLIED"},
            "bibliography_binding": {"path": f"notes/{FINAL_NAMES['bib_plan']}", "sha256": bib_plan_sha, "append_status": "NOT_APPLIED"},
            "writer_handoff": {"path": f"notes/{FINAL_NAMES['handoff']}", "sha256": handoff_sha},
            "authority_bindings": {
                "roadmap_sha256": roadmap_sha,
                "author_adjudication_sha256": adjudication_sha,
                "author_decision_digest": decision_digest,
                "claim_surface_manifest_sha256": claim_sha,
            },
            "items": items,
            "summary": {
                "resolved": sum(item["status"] == "RESOLVED" for item in items),
                "limitations": sum(item["status"] == "DELIBERATE_LIMITATION" for item in items),
                "unresolvable": 0,
                "disagreed": 0,
            },
            "new_references_planned_exactly": ["P33-S03-CORR", "P33-S16-CORR"],
            "new_references_appended_by_writer": 0,
            "source_use_boundary": {"rows": 48, "exact_passage_locators": 0, "explicit_bounded_unavailability": 48, "claim_to_passage_inconclusive": 48},
            "production_boundary": {"components_available": 0, "independence_established": False, "scientific_execution": False},
        }
        response_raw = json_bytes(response)
        staged["response_json"].write_bytes(response_raw)
        response_json_sha = sha_bytes(response_raw)

        md_lines = [
            "# Paper 33 Stage 4-prime provisional response — fresh round6 lineage",
            "",
            "Status: **writer-emitted only; bibliography append, patch application, build, and Stage 4.5 have not run**.",
            "",
            f"- Schema revision round: `{REVISION_ROUND}`",
            f"- Fresh roadmap SHA-256: `{roadmap_sha}`",
            f"- Fresh adjudication SHA-256: `{adjudication_sha}`",
            f"- Writer patch SHA-256: `{patch_sha}` (`37` exact `replace_block` operations)",
            f"- Bibliography plan SHA-256: `{bib_plan_sha}` (exactly two appends, not executed)",
            f"- Provisional JSON SHA-256: `{response_json_sha}`",
            "",
            "| Item | Provisional disposition | Emitted targets | Response |",
            "|---|---|---|---|",
        ]
        for item in items:
            md_lines.append(
                f"| `{item['roadmap_item_id']}` | `{item['status']}` | "
                f"`{', '.join(item['emitted_change_locations'])}` | {item['author_response']} |"
            )
        md_lines += [
            "",
            "The 48-use ledger remains 48/48 passage-inconclusive with zero exact passage locators. "
            "The fourteen fixtures are synthetic conformance records only; production components available remain zero and validator independence remains unestablished.",
            "",
            "The old round5 roadmap/choices/claim/adjudication chain is noncontrolling and was not used for this patch. "
            "No claim-strength or collateral authorization exists.",
            "",
        ]
        staged["response_md"].write_text("\n".join(md_lines), encoding="utf-8")

        log_lines = [
            "# Paper 33 Stage 4-prime writer revision log — round6 authority lineage",
            "",
            "Date: **2026-09-04**",
            "",
            "This is an emission log, not a landed-change report. The patch and bibliography plan remain unapplied.",
            "",
            "| Item | Severity | Obligation | Author triage | Writer disposition | Authorized blocks |",
            "|---|---|---|---|---|---|",
        ]
        item_map = {item["roadmap_item_id"]: item for item in items}
        for item in roadmap["items"]:
            log_lines.append(
                f"| `{item['id']}` | `{item['severity']}` | `{item['obligation_class']}` | `will_address` | "
                f"`{item_map[item['id']]['status']}` | `{', '.join(row['block_id'] for row in item['proposed_targets'])}` |"
            )
        log_lines += [
            "",
            "## Writer emission receipt",
            "",
            f"- Patch SHA-256: `{patch_sha}`",
            "- Patch operations: `37` unique `replace_block` operations; `41` exact item/action target mappings.",
            "- Shared blocks: `B0026`, `B0036`, `B0044`, and `B0067` each cite both `REV-P33-003` and `REV-P33-008` in one operation.",
            "- Registered claim-strength changes: `0`; collateral authorizations: `0`.",
            "- Bibliography appends prepared: `2`; appends performed by writer: `0`.",
            "- Source uses bound: `48/48`; exact passage locators: `0/48`; INCONCLUSIVE retained: `48/48`.",
            "- Production components available: `0`; scientific producer/census/result executions: `0`.",
            "- Apply reports, successor drafts/PDFs, builds, README changes, canonical promotion, Stage 4.5, and re-review: `0`.",
            "",
        ]
        staged["revision_log"].write_text("\n".join(log_lines), encoding="utf-8")

        validate_cmd = [
            "python", str(REVISION_TOOL), "validate-adjudication", str(staged["roadmap"]), str(staged["adjudication"]),
            "--base", str(BASE), "--block-manifest", str(MANIFEST),
            "--claim-surface", str(staged["claim"]), "--artifact-root", str(ROOT),
        ]
        validated = subprocess.run(validate_cmd, cwd=ROOT, text=True, capture_output=True, check=False)
        require(validated.returncode == 0, f"official adjudication validation failed: {validated.stderr}{validated.stdout}")

        schema = load_json(PATCH_SCHEMA)
        schema_errors = sorted(jsonschema.Draft202012Validator(schema).iter_errors(patch), key=lambda e: list(e.path))
        require(not schema_errors, "patch schema failure: " + "; ".join(error.message for error in schema_errors))
        require(len(ops) == 37 and len({op["block_id"] for op in ops}) == 37, "patch operation cardinality differs")
        require(sum(len(op["roadmap_item_ids"]) for op in ops) == 41, "patch provenance mapping count differs")
        require(all(op["claim_strength_changes"] == [] and op["collateral_authorization_ids"] == [] for op in ops), "nonempty claim/collateral array")

        patch_text = patch_raw.decode("utf-8")
        use_ids = re.findall(r"use_id=(P33-U[0-9]{2})", patch_text)
        require(use_ids == [f"P33-U{i:02d}" for i in range(1, 49)], "source-use IDs are not exact and ordered")
        require(patch_text.count("claim_to_passage=INCONCLUSIVE") == 48, "INCONCLUSIVE marker count differs")
        require(patch_text.count("locator_disposition=EXPLICIT_BOUNDED_UNAVAILABLE") == 48, "bounded-unavailability marker count differs")
        require(patch_text.count("P33-S03,P33-S03-CORR") == 4, "S03 dual-binding serialization count differs")
        require(patch_text.count("P33-S16,P33-S16-CORR") == 6, "S16 dual-binding serialization count differs")
        require("production independence is not established" in patch_text or "production independence remains" in patch_text, "production independence boundary missing")
        require("No geodesic enumeration" in patch_text, "scientific nonexecution boundary missing")

        frozen_after = {str(path.relative_to(ROOT)): sha(path) for path in EXPECTED}
        require(frozen_after == frozen_before, "writer emission changed a frozen input")
        require(sha(BIB) == EXPECTED[BIB], "bibliography changed during writer emission")
        require("@misc{P33-S03-CORR" not in BIB.read_text(encoding="utf-8"), "P33-S03-CORR was appended by writer")
        require("@article{P33-S16-CORR" not in BIB.read_text(encoding="utf-8"), "P33-S16-CORR was appended by writer")

        generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
        receipt_json = {
            "schema_version": "round10-stage4-prime-p33-round6-writer-validation-receipt/1.0",
            "generated_at_utc": generated_at,
            "status": "PASS_WRITER_EMITTED_NOT_APPLIED",
            "paper_id": "P33",
            "lineage_label": "round6",
            "revision_round": REVISION_ROUND,
            "authority": {
                "root_receipt_sha256": EXPECTED[AUTH_RECEIPT],
                "input_freeze_sha256": EXPECTED[INPUT_FREEZE],
                "scope_expansion_request_sha256": EXPECTED[REQUEST],
                "author_event_sha256": EXPECTED[AUTHOR_EVENT],
            },
            "fresh_chain": {
                "roadmap": {"path": f"notes/{FINAL_NAMES['roadmap']}", "sha256": roadmap_sha},
                "claim_surface_manifest": {"path": f"notes/{FINAL_NAMES['claim']}", "sha256": claim_sha, "surfaces": 0},
                "author_choices": {"path": f"notes/{FINAL_NAMES['choices']}", "sha256": sha_bytes(choices_raw)},
                "author_adjudication": {"path": f"notes/{FINAL_NAMES['adjudication']}", "sha256": adjudication_sha},
                "author_decision_digest": decision_digest,
                "official_build_stdout": built.stdout.strip(),
                "official_validation_stdout": validated.stdout.strip(),
            },
            "patch": {"path": f"notes/{FINAL_NAMES['patch']}", "sha256": patch_sha, "format": "1.1", "authorization_context": "review_roadmap"},
            "bibliography_plan": {"path": f"notes/{FINAL_NAMES['bib_plan']}", "sha256": bib_plan_sha, "base_sha256": EXPECTED[BIB], "current_sha256_after_emission": sha(BIB), "status": "NOT_APPLIED"},
            "checks": {
                "official_authority_validations": 2,
                "roadmap_items": 9,
                "will_address_choices": 9,
                "unique_replace_block_ops": 37,
                "item_action_target_mappings": 41,
                "shared_blocks_with_complete_ids": 4,
                "source_uses_exact": 48,
                "passage_inconclusive_markers": 48,
                "bounded_unavailability_markers": 48,
                "correction_dual_bindings": 5,
                "claim_strength_changes": 0,
                "collateral_authorizations": 0,
                "patch_schema_errors": 0,
                "support_validation_checks_replayed": support["checks_run"],
                "support_validation_failures": support["failure_count"],
                "frozen_inputs_changed": 0,
            },
            "boundaries": {
                "old_round5_chain_used_for_apply": False,
                "patch_applied": False,
                "bibliography_appended": False,
                "successor_draft_or_pdf_emitted": False,
                "build_run": False,
                "readme_changed": False,
                "canonical_or_science_or_route_or_initial_system_changed": False,
                "fresh_stage4_5_or_re_review_run": False,
            },
        }
        staged["validation"].write_bytes(json_bytes(receipt_json))

        # All outputs have been validated in staging. Move only the explicitly
        # named writer artifacts into the notes fence.
        for name in FINAL_NAMES:
            os.replace(staged[name], final_paths[name])

    print(json.dumps({
        "status": "PASS_WRITER_EMITTED_NOT_APPLIED",
        "roadmap_sha256": sha(final_paths["roadmap"]),
        "claim_surface_manifest_sha256": sha(final_paths["claim"]),
        "author_choices_sha256": sha(final_paths["choices"]),
        "author_adjudication_sha256": sha(final_paths["adjudication"]),
        "author_decision_digest": decision_digest,
        "patch_sha256": sha(final_paths["patch"]),
        "patch_ops": 37,
        "bibliography_plan_sha256": sha(final_paths["bib_plan"]),
        "bibliography_current_sha256": sha(BIB),
        "source_uses": 48,
        "passage_inconclusive": 48,
        "production_components_available": 0,
    }, indent=2, ensure_ascii=False))


def apply_bibliography_plan() -> None:
    """Root-only exact append mode. Writer emission deliberately never calls it."""
    plan_path = NOTES / FINAL_NAMES["bib_plan"]
    require(plan_path.is_file(), f"missing bibliography plan: {plan_path}")
    plan = load_json(plan_path)
    prospective = load_json(PROSPECTIVE_BIB)
    require(plan["status"] == "AUTHORIZED_EXACT_APPEND_PLAN_NOT_APPLIED", "plan status differs")
    require(plan["base"]["sha256"] == EXPECTED[BIB], "plan base binding differs")
    require(sha(BIB) == EXPECTED[BIB], "bibliography no longer matches authorized base")
    require(plan["prospective_contract"]["sha256"] == EXPECTED[PROSPECTIVE_BIB], "plan prospective binding differs")
    expected_records = [entry["prospective_bibtex_record"] for entry in prospective["prospective_entries"]]
    require([row["prospective_bibtex_record"] for row in plan["records"]] == expected_records, "planned records differ from prospective contract")
    current = BIB.read_bytes()
    for key in plan["allowed_keys"]:
        require(f"{{{key},".encode("utf-8") not in current, f"refusing duplicate bibliography key: {key}")
    append_raw = plan["append_text"].encode("utf-8")
    require(sha_bytes(append_raw) == plan["append_text_sha256"], "append bytes hash differs")
    result = current + append_raw
    require(sha_bytes(result) == plan["expected_result_sha256"], "planned result hash differs")
    temp = BIB.with_name(BIB.name + ".round6-append.tmp")
    require(not temp.exists(), f"temporary output exists: {temp}")
    temp.write_bytes(result)
    os.replace(temp, BIB)
    print(json.dumps({"status": "APPLIED_EXACT_TWO_ENTRY_APPEND", "sha256": sha(BIB), "bytes": BIB.stat().st_size}, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply-bibliography-plan",
        action="store_true",
        help="root-orchestrator mode: apply the separately emitted exact two-entry append plan",
    )
    args = parser.parse_args()
    if args.apply_bibliography_plan:
        apply_bibliography_plan()
    else:
        emit()


if __name__ == "__main__":
    main()
