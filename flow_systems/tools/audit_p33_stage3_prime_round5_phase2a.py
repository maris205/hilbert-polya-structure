#!/usr/bin/env python3
"""Fail-closed validation for P33 Stage 3-prime Round-5 Phase 2A."""

from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path
import re

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parent.parent
NOTES = ROOT / "papers/33-bolza-control-matched-census/notes"
ARS = Path("/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/skills/academic-research-suite/ars")
ROUND_ID = "p33-stage3-prime-round5-2026-09-04"
OUTPUT = NOTES / "stage3_prime_round5_phase2a_validation.json"
VERDICTS = {"FULLY_ADDRESSED", "PARTIALLY_ADDRESSED", "NOT_ADDRESSED", "MADE_WORSE", "CANNOT_VERIFY"}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(f"P33_ROUND5_PHASE2A_FAIL: {message}")


def load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    require(isinstance(value, dict), f"top-level object required: {path}")
    return value


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def jcs_sha(value: object) -> str:
    return hashlib.sha256(canonical(value)).hexdigest()


def verify_frozen(node: object, checks: list[str], prefix: str) -> None:
    if isinstance(node, dict):
        if set(node) == {"path", "sha256", "bytes"}:
            path = ROOT / str(node["path"])
            require(path.is_file() and not path.is_symlink(), f"{prefix}: missing/symlink {path}")
            require(path.stat().st_size == node["bytes"], f"{prefix}: byte drift {path}")
            require(sha(path) == node["sha256"], f"{prefix}: hash drift {path}")
            checks.append(f"{prefix}:{node['path']}")
        else:
            for key, child in node.items():
                verify_frozen(child, checks, f"{prefix}.{key}")
    elif isinstance(node, list):
        for index, child in enumerate(node):
            verify_frozen(child, checks, f"{prefix}[{index}]")


def main() -> None:
    require(not OUTPUT.exists(), f"refusing to overwrite {OUTPUT}")
    paths = {
        "freeze": NOTES / "stage3_prime_round5_input_freeze.json",
        "manifest": NOTES / "stage3_prime_round5_input_manifest.json",
        "manifest_receipt": NOTES / "stage3_prime_round5_input_manifest_receipt.json",
        "phase1_validation": NOTES / "stage3_prime_round5_phase1_validation.json",
        "precommitment": NOTES / "stage3_prime_round5_precommitment.json",
        "verdict": NOTES / "stage3_prime_round5_verdict_record.json",
        "semantic_audit": NOTES / "stage3_prime_round5_phase2a_semantic_audit.json",
        "semantic_audit_md": NOTES / "stage3_prime_round5_phase2a_semantic_audit.md",
        "receipt": NOTES / "stage3_prime_round5_phase2a_receipt.md",
        "roadmap": NOTES / "stage3_revision_roadmap.json",
        "emitter_preflight": NOTES / "stage3_prime_round5_verdict_emitter_preflight.json",
        "emitter": ROOT / "tools/p33_stage3_prime_round5_verdict_emitter.py",
        "private_payload": ROOT / ".p33_stage3_prime_round5_phase2a_payload.private.json",
    }
    for label, path in paths.items():
        require(path.is_file() and not path.is_symlink(), f"missing/symlink {label}: {path}")

    freeze = load(paths["freeze"])
    manifest = load(paths["manifest"])
    manifest_receipt = load(paths["manifest_receipt"])
    phase1 = load(paths["phase1_validation"])
    pre = load(paths["precommitment"])
    verdict = load(paths["verdict"])
    semantic = load(paths["semantic_audit"])
    roadmap = load(paths["roadmap"])
    emitter_preflight = load(paths["emitter_preflight"])
    payload = load(paths["private_payload"])
    checks: list[str] = []

    require(phase1.get("status") == "PASS", "Phase 1 gate is not PASS")
    require(phase1["outputs"]["precommitment_raw_sha256"] == sha(paths["precommitment"]), "Phase 1/precommitment raw drift")
    require(phase1["outputs"]["precommitment_jcs_sha256"] == jcs_sha(pre), "Phase 1/precommitment JCS drift")
    require(emitter_preflight.get("status") == "PASS", "emitter preflight not PASS")
    require(emitter_preflight["emitter"]["sha256"] == sha(paths["emitter"]), "emitter drift")
    require(manifest_receipt["input_manifest"]["sha256"] == sha(paths["manifest"]), "manifest raw drift")
    require(manifest_receipt["input_manifest"]["jcs_sha256"] == jcs_sha(manifest), "manifest JCS drift")
    checks += ["phase1_gate", "precommitment_raw_immutability", "precommitment_jcs_immutability", "emitter_preflight", "emitter_immutability", "manifest_raw_binding", "manifest_jcs_binding"]
    verify_frozen(freeze["round4_preservation"], checks, "round4_preservation")
    verify_frozen(freeze["immutable_boundaries"], checks, "immutable_boundaries")

    schema = load(ARS / "shared/contracts/re_review/verdict_record.schema.json")
    errors = sorted(Draft202012Validator(schema).iter_errors(verdict), key=lambda error: (list(error.absolute_path), error.message))
    require(not errors, "verdict schema: " + "; ".join(error.message for error in errors))
    checks.append("official_verdict_schema")
    require(verdict.get("contract_version") == "1.1" and verdict.get("round_id") == ROUND_ID, "verdict identity")
    require(verdict.get("precommitment_hash") == jcs_sha(pre), "verdict/precommitment JCS binding")
    require(set(payload) == {"round_id", "items", "new_issues", "dissents", "escalation_exceptions"}, "private payload keys")
    require(payload["round_id"] == ROUND_ID, "private payload round")
    for key in ("items", "new_issues", "dissents", "escalation_exceptions"):
        require(payload[key] == verdict[key], f"payload/verdict mismatch: {key}")
    checks += ["verdict_identity", "precommitment_binding", "payload_shape", "payload_verdict_identity"]

    expected_ids = [item["item_id"] for item in pre["items"]]
    rows = verdict["items"]
    require([row["item_id"] for row in rows] == expected_ids, "13-item coverage/order")
    require(len(rows) == 13 and len(set(expected_ids)) == 13, "unique 13-item population")
    pre_by_id = {item["item_id"]: item for item in pre["items"]}
    dissent_by_id = {row["dissent_id"]: row for row in verdict["dissents"]}
    for row in rows:
        item_id = row["item_id"]
        require(row["verdict"] in VERDICTS, f"{item_id}: closed verdict")
        source_seats = pre_by_id[item_id]["source_reviewer_labels"]
        expected_seat = next((seat for seat in source_seats if seat != "DA"), "EIC")
        require(row["verified_by"] == expected_seat, f"{item_id}: reviewer routing")
        applied = row["applied_criterion"]
        if applied != "precommitted":
            match = re.fullmatch(r"dissented:(DIS-[1-9][0-9]*)", applied)
            require(bool(match) and match.group(1) in dissent_by_id and dissent_by_id[match.group(1)]["item_id"] == item_id,
                    f"{item_id}: criterion/dissent binding")
        require(str(row["change_summary"]).strip(), f"{item_id}: empty change summary")
        if row["verdict"] == "CANNOT_VERIFY":
            require("cannot_verify_reason" in row and "evidence_anchor" not in row, f"{item_id}: cannot-verify shape")
        else:
            anchors = row.get("evidence_anchor", [])
            require(anchors and all(re.fullmatch(r"(?:text|table|figure|equation|dataset|absence): .+", anchor) for anchor in anchors),
                    f"{item_id}: typed evidence anchors")
        if row["verdict"] == "PARTIALLY_ADDRESSED":
            residual = row.get("residual_gap", {})
            require(str(residual.get("text", "")).strip(), f"{item_id}: residual text")
            require(residual.get("residual_obligation_class") in {"must_fix", "should_fix", "consider"}, f"{item_id}: residual class")
        else:
            require("residual_gap" not in row, f"{item_id}: spurious residual")
        checks += [f"{item_id}:routing", f"{item_id}:criterion", f"{item_id}:evidence", f"{item_id}:residual_shape"]

    serialized = json.dumps(verdict, ensure_ascii=False).lower()
    for forbidden in ("stage4_response_to_reviewers", "author_response", "authors_claim"):
        require(forbidden not in serialized, f"forbidden persuasion reference: {forbidden}")
        checks.append(f"no_{forbidden}")
    require(verdict["new_issues"] == [] and verdict["dissents"] == [] and verdict["escalation_exceptions"] == [], "unexpected Phase 2A side populations")
    checks.append("empty_side_populations")

    scope = semantic["scope_controls"]
    require(semantic.get("status") == "PASS", "semantic audit status")
    require(scope.get("fresh_context") is True and scope.get("persuasion_blind") is True, "fresh/persuasion blind")
    for key in ("response_to_reviewers_inspected", "prior_round4_rereview_material_inspected", "author_adjudication_content_inspected", "phase2b_material_inspected", "directory_listing_performed", "manuscript_modified", "phase2b_started"):
        require(scope.get(key) is False, f"scope control failed: {key}")
    require(semantic["allowed_input_compliance"]["status"] == "PASS", "allowed-input status")
    require(semantic["allowed_input_compliance"]["unlisted_p33_project_inputs_accessed"] == [], "unlisted project input")
    emission = semantic["emission"]
    require(emission["emitter_invocation_count"] == 1, "emitter invocation count")
    require(emission["emitter_retry_count"] == 0 and emission["schema_or_lint_failures"] == 0, "emitter retry/failure")
    require(emission["post_emit_modification_count"] == 0, "verdict modified after emission")
    require(emission["verdict_record_raw_sha256"] == sha(paths["verdict"]), "semantic/verdict raw binding")
    require(emission["verdict_record_jcs_sha256"] == jcs_sha(verdict), "semantic/verdict JCS binding")
    require(emission["private_payload_raw_sha256"] == sha(paths["private_payload"]), "semantic/private payload binding")
    checks += ["semantic_status", "fresh_persuasion_blind", "scope_controls", "allowed_input_compliance", "single_emission", "no_retry", "no_post_emit_modification", "semantic_hash_bindings"]

    receipt = paths["receipt"].read_text(encoding="utf-8")
    require(next(line.strip() for line in reversed(receipt.splitlines()) if line.strip()) == "[EVIDENCE-COMMITTED]", "receipt terminal marker")
    for marker in ("Emitter invocation count: `1`", "Emitter retries: `0`", "Evidence-emission schema/lint failures: `0`", "Phase 2B was not started."):
        require(marker in receipt, f"receipt marker absent: {marker}")
        checks.append(f"receipt:{marker}")
    checks.append("evidence_committed")

    counts = Counter(row["verdict"] for row in rows)
    roadmap_by_id = {row["id"]: row for row in roadmap["items"]}
    residual_counts = Counter(
        row["residual_gap"]["residual_obligation_class"]
        for row in rows if row["verdict"] == "PARTIALLY_ADDRESSED"
    )
    output = {
        "schema_version": "p33-stage3-prime-round5-phase2a-validation/1.0",
        "generated_at": "2026-09-03T18:45:00Z",
        "paper_id": "P33",
        "round_id": ROUND_ID,
        "phase": "phase2a_persuasion_blind_evidence_verdict",
        "status": "PASS",
        "bindings": {
            "precommitment_raw_sha256": sha(paths["precommitment"]),
            "precommitment_jcs_sha256": jcs_sha(pre),
            "verdict_record_raw_sha256": sha(paths["verdict"]),
            "verdict_record_jcs_sha256": jcs_sha(verdict),
            "semantic_audit_sha256": sha(paths["semantic_audit"]),
            "semantic_audit_md_sha256": sha(paths["semantic_audit_md"]),
            "phase2a_receipt_sha256": sha(paths["receipt"]),
        },
        "counts": {
            "roadmap_items": len(roadmap_by_id),
            "verdict_rows": len(rows),
            "verdicts": {name: counts.get(name, 0) for name in sorted(VERDICTS)},
            "residual_obligation_classes": dict(sorted(residual_counts.items())),
            "new_issues": len(verdict["new_issues"]),
            "dissents": len(verdict["dissents"]),
            "escalation_exceptions": len(verdict["escalation_exceptions"]),
            "validation_checks": len(checks),
        },
        "protocol": {
            "phase1_gate": "PASS",
            "fresh_context": True,
            "persuasion_blind": True,
            "emitter_invocations": 1,
            "retries": 0,
            "verdict_record_immutable_after_emission": True,
            "phase2b_started": False,
        },
        "checks": checks,
    }
    OUTPUT.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"PASS -- P33 Round-5 Phase 2A: {len(checks)} checks; {counts['FULLY_ADDRESSED']} FULL / {counts['PARTIALLY_ADDRESSED']} PARTIAL")


if __name__ == "__main__":
    main()
