#!/usr/bin/env python3
"""Validate P33 Round-5 revision-blind Phase 1 without reading revision evidence."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parent.parent
NOTES = ROOT / "papers/33-bolza-control-matched-census/notes"
ARS = Path("/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/skills/academic-research-suite/ars")
ROUND_ID = "p33-stage3-prime-round5-2026-09-04"
OUTPUT = NOTES / "stage3_prime_round5_phase1_validation.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(f"P33_ROUND5_PHASE1_FAIL: {message}")


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


def labels(raw: str) -> list[str]:
    stripped = re.sub(r"\([^()]*\)", "", raw).split(" — ", 1)[0]
    result: list[str] = []
    for token in re.split(r",|/|;| and |&", stripped):
        folded = token.strip().lower()
        label = None
        if folded in {"eic", "editor", "editor-in-chief"}:
            label = "EIC"
        elif folded in {"da", "devil's advocate", "devils advocate"}:
            label = "DA"
        elif re.fullmatch(r"r[1-3]", folded):
            label = folded.upper()
        elif re.fullmatch(r"(?:peer )?reviewer [1-3]", folded):
            label = "R" + folded[-1]
        if label and label not in result:
            result.append(label)
    return result


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
    manifest_path = NOTES / "stage3_prime_round5_input_manifest.json"
    freeze_path = NOTES / "stage3_prime_round5_input_freeze.json"
    input_receipt_path = NOTES / "stage3_prime_round5_input_manifest_receipt.json"
    pre_path = NOTES / "stage3_prime_round5_precommitment.json"
    receipt_path = NOTES / "stage3_prime_round5_phase1_receipt.md"
    roadmap_path = NOTES / "stage3_revision_roadmap.json"
    for path in (manifest_path, freeze_path, input_receipt_path, pre_path, receipt_path, roadmap_path):
        require(path.is_file(), f"missing {path.relative_to(ROOT)}")

    manifest = load(manifest_path)
    freeze = load(freeze_path)
    input_receipt = load(input_receipt_path)
    pre = load(pre_path)
    roadmap = load(roadmap_path)
    checks: list[str] = []

    require(manifest.get("contract_version") == "1.1", "manifest version")
    require(manifest.get("round_id") == ROUND_ID, "manifest round id")
    require(len(manifest.get("artifacts", {})) == 11, "manifest must have 11 artifact keys")
    require(input_receipt["input_manifest"]["sha256"] == sha(manifest_path), "manifest raw binding")
    require(input_receipt["input_manifest"]["jcs_sha256"] == jcs_sha(manifest), "manifest JCS binding")
    checks += ["manifest_version", "manifest_round_id", "manifest_11_keys", "manifest_raw_binding", "manifest_jcs_binding"]
    verify_frozen(freeze["round4_preservation"], checks, "round4_preservation")
    verify_frozen(freeze["immutable_boundaries"], checks, "immutable_boundaries")

    schema = load(ARS / "shared/contracts/re_review/precommitment.schema.json")
    errors = sorted(Draft202012Validator(schema).iter_errors(pre), key=lambda e: (list(e.absolute_path), e.message))
    require(not errors, "precommitment schema: " + "; ".join(e.message for e in errors))
    checks.append("precommitment_schema")
    require(pre["contract_version"] == "1.1" and pre["round_id"] == ROUND_ID, "precommitment identity")
    require(pre["input_manifest_hash"] == jcs_sha(manifest), "precommitment manifest binding")
    require(pre["new_standards"] == [], "new standards must be empty")
    checks += ["precommitment_identity", "precommitment_manifest_binding", "new_standards_empty"]

    expected = [row for row in roadmap["items"] if row["obligation_class"] in {"must_fix", "should_fix"}]
    rows = pre["items"]
    require([row["item_id"] for row in rows] == [row["id"] for row in expected], "coverage/order mismatch")
    checks.append("coverage_order")
    for row, item in zip(rows, expected):
        item_id = item["id"]
        require(row["obligation_class"] == item["obligation_class"], f"{item_id}: obligation")
        require(row["inherited_criterion"]["roadmap_text"] == item["verification_criteria"], f"{item_id}: criterion not verbatim")
        require(row["source_reviewer"] == item["reviewer"], f"{item_id}: reviewer not verbatim")
        require(row["source_reviewer_labels"] == labels(item["reviewer"]), f"{item_id}: labels")
        require(row["equivalence_policy"] == "allowed", f"{item_id}: equivalence")
        required_ops = {"fully_addressed", "partially_addressed", "made_worse_discriminator"} if item["obligation_class"] == "must_fix" else {"fully_addressed"}
        require(set(row["operationalization"]) == required_ops, f"{item_id}: operationalization shape")
        require(all(str(v).strip() for v in row["operationalization"].values()), f"{item_id}: empty operationalization")
        surface = row["expected_change_surface"]
        require(surface.strip(), f"{item_id}: empty surface")
        for target in item.get("proposed_targets", []):
            require(target["block_id"] in surface, f"{item_id}: missing target {target['block_id']}")
        checks += [f"{item_id}:criterion", f"{item_id}:operationalization", f"{item_id}:surface", f"{item_id}:reviewer"]

    receipt = receipt_path.read_text(encoding="utf-8")
    required_markers = [
        "fork_turns=none",
        "revision_blind=true",
        "prohibited_material_inspected=false",
        "phase1_retry_used=false",
    ]
    for marker in required_markers:
        require(marker in receipt, f"receipt marker absent: {marker}")
        checks.append(f"receipt:{marker}")
    require(next(line.strip() for line in reversed(receipt.splitlines()) if line.strip()) == "[CONTRACT-ACKNOWLEDGED]", "terminal marker")
    checks.append("contract_acknowledged")

    output = {
        "schema_version": "p33-stage3-prime-round5-phase1-validation/1.0",
        "generated_at": "2026-09-03T18:10:00Z",
        "paper_id": "P33",
        "round_id": ROUND_ID,
        "phase": "phase1_revision_blind_precommitment",
        "status": "PASS",
        "inputs": {
            "manifest_raw_sha256": sha(manifest_path),
            "manifest_jcs_sha256": jcs_sha(manifest),
            "input_freeze_sha256": sha(freeze_path),
            "roadmap_sha256": sha(roadmap_path),
        },
        "outputs": {
            "precommitment_raw_sha256": sha(pre_path),
            "precommitment_jcs_sha256": jcs_sha(pre),
            "phase1_receipt_sha256": sha(receipt_path),
        },
        "counts": {
            "roadmap_items": len(roadmap["items"]),
            "precommitted_items": len(rows),
            "must_fix": sum(row["obligation_class"] == "must_fix" for row in rows),
            "should_fix": sum(row["obligation_class"] == "should_fix" for row in rows),
            "new_standards": len(pre["new_standards"]),
            "validation_checks": len(checks),
        },
        "freshness": {
            "fresh_context": True,
            "fork_turns": "none",
            "revision_blind": True,
            "round4_context_reused": False,
            "phase2a_started": False,
        },
        "checks": checks,
    }
    OUTPUT.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"PASS -- P33 Round-5 Phase 1: {len(checks)} checks, {len(rows)} precommitments")


if __name__ == "__main__":
    main()
