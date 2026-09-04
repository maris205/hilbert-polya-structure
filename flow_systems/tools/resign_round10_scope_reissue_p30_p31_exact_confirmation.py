#!/usr/bin/env python3
"""Exact-confirmation re-emission for Round-10 P30/P31 writer evidence.

This is a writer-only operation.  It re-signs the already frozen author
choices and patch operations against the exact ``确认\n`` authority event.
It never applies a patch and never writes a manuscript, bibliography, matrix,
README, build product, or Git state.
"""

from __future__ import annotations

import copy
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARS_ROOT = Path(
    "/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/skills/"
    "academic-research-suite/ars"
)
ROADMAP_CLI = ARS_ROOT / "scripts/revision_roadmap.py"
sys.path.insert(0, str(ARS_ROOT / "scripts"))

import revision_roadmap as rr  # noqa: E402


PREFIX = "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_EXACT_CONFIRMATION"
AUTHORITY_FILES = {
    "author_event": ROOT / f"{PREFIX}_AUTHOR_EVENT_20260904.txt",
    "authorization_record": ROOT / f"{PREFIX}_AUTHORIZATION_RECORD.md",
    "input_freeze": ROOT / f"{PREFIX}_INPUT_FREEZE.json",
    "authorization_receipt": ROOT / f"{PREFIX}_AUTHORIZATION_RECEIPT.json",
    "authority_audit": ROOT / f"{PREFIX}_AUTHORITY_AUDIT.json",
}
AUTHORITY_HASHES = {
    "author_event": "f449b78edf3805c05f297591a9593158d475b87f289b39f69c3f6eb813889ebe",
    "authorization_record": "98755a5998aeee16034db32c89d997b3349a1b77b0c41a93ab32ac994a8d8f79",
    "input_freeze": "7a140287ce95ad6304cc52e7568d66780d77f54d7aaba461515cb087886075e1",
    "authorization_receipt": "a21655745ea33c565626c5cc980b8f91a82f4b87ce2d74cfcb012f0c5d7bae21",
    "authority_audit": "813a600253cdeac98003a69beb7f28dbf35080cfdfe7bb974d1d8c9a323857b2",
}
EXACT_EVENT_BYTES = "确认\n".encode("utf-8")
EXACT_EVENT_ID = (
    "AUTHOR-EVENT-20260904-ROUND10-STAGE4-PRIME-SCOPE-REISSUE-EXACT-CONFIRMATION"
)
PREPARATION_ROLE = (
    "NON_AUTHORIZING_PREPARATION_EVIDENCE_FOR_EXACT_CONFIRMATION_REEMISSION_ONLY"
)
REQUEST = ROOT / "BATCH_ROUND10_STAGE4_PRIME_EXPANDED_CORRECTION_AUTHORIZATION_REQUEST_P30_P31.json"
REQUEST_SHA256 = "9fecba23da5ea90f3c8f252d0a7fbd019d042f600dbeaa320167865273692135"

PAPERS = {
    "P30": {
        "slug": "30-three-disk-nonconstant-roof-determinant",
        "ops": 34,
        "prepared_patch_sha256": "8d8c209bec0c639878b63b7faffcbafafcb1dfe46967cf69b790217e6b1a365b",
        "prepared_choices_sha256": "3037afaa22174c1b4d772415d4d8432a7aebc77b438b170410d7630cfa58f113",
        "prepared_adjudication_sha256": "0f39cc2bef92622ad0e80b202f9370330b941418e50a52feaacdac72557ebc48",
        "prepared_handoff_sha256": "08f8856ac8b524992fa89e0af2d598d932c3dcbc32ede4b086536445f4f2e8e6",
        "prepared_validation_sha256": "f3d76ab7bb504da6085d1f2363e7fb8b6140fd3658c44f3f23cdecca27459478",
    },
    "P31": {
        "slug": "31-level11-conjugacy-owner-ledger",
        "ops": 13,
        "prepared_patch_sha256": "778b35df262cc28fc7aec2bb2d8a1f1c51f62fd6556ece02a5fd88c0266056b5",
        "prepared_choices_sha256": "3f152d005593621fe9398a10bcaf1655202641fba96e0536c377b46879e52456",
        "prepared_adjudication_sha256": "26df423226d1fa0474789a489223988567f6a50bf1a9615a2df25b0345833fe2",
        "prepared_handoff_sha256": "57d35678744c248f4de5f07612abb58e37442874e09b3e6f81241108fccd1ae5",
        "prepared_validation_sha256": "fc6611a7051d92abcf79ebdcffeda7f9dcda9b268f7befb530cb73ca3e6c5260",
    },
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(f"ROUND10_P30_P31_EXACT_RESIGN_FAIL: {message}")


def sha_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def sha(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def load_json(path: Path) -> dict:
    return json.loads(path.read_bytes())


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def canonical_json_digest(value: object) -> str:
    return sha_bytes(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8"))


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT))


def binding(path: Path, *, represented_path: Path | None = None) -> dict:
    raw = path.read_bytes()
    return {
        "path": relative(represented_path or path),
        "sha256": sha_bytes(raw),
        "bytes": len(raw),
    }


def paths_for(config: dict) -> dict[str, Path]:
    notes = ROOT / "papers" / config["slug"] / "notes"
    return {
        "notes": notes,
        "base": notes / "stage4_prime_revision_round2.tex",
        "manifest": notes / "stage4_prime_correction_round3_base.block-manifest.json",
        "roadmap": notes / "stage4_prime_correction_round3_revision_roadmap.json",
        "claim": notes / "stage4_prime_correction_round3_claim_surface_manifest.json",
        "old_choices": notes / "stage4_prime_correction_round3_author_choices.json",
        "old_adjudication": notes / "stage4_prime_correction_round3_author_adjudication.json",
        "old_patch": notes / "stage4_prime_revision_patch_round3.json",
        "old_handoff": notes / "stage4_prime_correction_round3_writer_handoff.json",
        "old_validation": notes / "stage4_prime_correction_round3_writer_validation_receipt.json",
        "choices": notes / "stage4_prime_correction_round3_exact_confirmation_author_choices.json",
        "adjudication": notes / "stage4_prime_correction_round3_exact_confirmation_author_adjudication.json",
        "patch": notes / "stage4_prime_revision_patch_round3_exact_confirmation.json",
        "handoff": notes / "stage4_prime_correction_round3_exact_confirmation_writer_handoff.json",
        "validation": notes / "stage4_prime_writer_validation_receipt_round3_exact_confirmation.json",
    }


def same_artifact_row(actual: dict, expected: dict, label: str) -> None:
    for key in ("path", "sha256", "bytes"):
        require(actual[key] == expected[key], f"{label} {key} drift")


def exact_authority() -> tuple[dict, dict, dict]:
    for key, path in AUTHORITY_FILES.items():
        require(path.is_file(), f"missing exact authority {path.name}")
        require(sha(path) == AUTHORITY_HASHES[key], f"exact authority hash drift {path.name}")
    require(AUTHORITY_FILES["author_event"].read_bytes() == EXACT_EVENT_BYTES, "author event is not exact 确认\\n bytes")
    require(sha(REQUEST) == REQUEST_SHA256, "P30/P31 expanded request drift")

    receipt = load_json(AUTHORITY_FILES["authorization_receipt"])
    freeze = load_json(AUTHORITY_FILES["input_freeze"])
    audit = load_json(AUTHORITY_FILES["authority_audit"])
    require(
        receipt["status"] == "AUTHORIZED_BY_EXACT_CONFIRMATION_FOR_130_BLOCK_STAGE4_PRIME_EXECUTION",
        "exact receipt status",
    )
    require(receipt["prepared_evidence_authority_role"] == PREPARATION_ROLE, "receipt preparation role")
    require(freeze["status"] == "FROZEN_FOR_EXACT_CONFIRMATION_130_BLOCK_EXECUTION", "exact freeze status")
    require(freeze["prepared_evidence_authority_role"] == PREPARATION_ROLE, "freeze preparation role")
    require(
        audit["status"] == "PASS_EXACT_CONFIRMATION_AUTHORITY_FROZEN_READY_FOR_DETERMINISTIC_APPLY",
        "exact authority audit status",
    )
    require(receipt["author_event"]["exact_text"].encode("utf-8") == EXACT_EVENT_BYTES, "receipt exact event text")
    require(freeze["author_event"]["exact_text"].encode("utf-8") == EXACT_EVENT_BYTES, "freeze exact event text")
    request_row = receipt["tracks"]["P30_P31"]
    same_artifact_row(request_row, binding(REQUEST), "receipt P30/P31 request")
    require(request_row["replace_block_pairs"] == 47, "receipt P30/P31 operation total")

    authority = {
        "author_event": copy.deepcopy(receipt["author_event"]),
        "authorization_record": copy.deepcopy(receipt["authorization_record"]),
        "input_freeze": copy.deepcopy(receipt["input_freeze"]),
        "authorization_receipt": binding(AUTHORITY_FILES["authorization_receipt"]),
        "authority_audit": binding(AUTHORITY_FILES["authority_audit"]),
    }
    for key, row in authority.items():
        same_artifact_row(row, binding(AUTHORITY_FILES[key]), f"exact authority row {key}")
    return authority, receipt, freeze


def replace_event_ids(value: dict) -> dict:
    result = copy.deepcopy(value)
    result["author_events"] = [{
        "event_id": EXACT_EVENT_ID,
        "source": "explicit_session_user_message",
        "actor_role": "author",
        "input_sha256": AUTHORITY_HASHES["author_event"],
    }]
    result["display_order"]["author_event_id"] = EXACT_EVENT_ID
    for row in result["author_adjudications"]:
        row["author_event_id"] = EXACT_EVENT_ID
        for authorization in row.get("claim_strength_authorizations", []):
            authorization["author_event_id"] = EXACT_EVENT_ID
    for authorization in result["collateral_authorizations"]:
        authorization["author_event_id"] = EXACT_EVENT_ID
    return result


def decision_projection(value: dict) -> dict:
    projected = copy.deepcopy(value)
    projected.pop("author_events", None)
    projected["display_order"].pop("author_event_id", None)
    for row in projected["author_adjudications"]:
        row.pop("author_event_id", None)
        for authorization in row.get("claim_strength_authorizations", []):
            authorization.pop("author_event_id", None)
    for authorization in projected["collateral_authorizations"]:
        authorization.pop("author_event_id", None)
    return projected


def run_official(*args: str) -> str:
    completed = subprocess.run(
        [sys.executable, str(ROADMAP_CLI), *args],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        check=False,
    )
    require(completed.returncode == 0, f"official revision_roadmap.py failed: {completed.stdout.strip()}")
    return completed.stdout.strip()


def request_targets(request: dict, paper_id: str) -> tuple[list[str], list[str]]:
    paper = next(row for row in request["papers"] if row["paper_id"] == paper_id)
    blocks = [row["block_id"] for row in paper["all_requested_targets"]]
    item_ids: list[str] = []
    for row in paper["all_requested_targets"]:
        item_id = row["issue_id"]
        if not item_id.startswith("REV-"):
            item_id = f"REV-{item_id}"
        if item_id not in item_ids:
            item_ids.append(item_id)
    return blocks, item_ids


def promote_all(candidates: list[tuple[Path, Path]]) -> None:
    promoted: list[Path] = []
    try:
        for candidate, target in candidates:
            require(candidate.is_file(), f"missing candidate {candidate}")
            require(not target.exists(), f"output collision at promotion {relative(target)}")
        for candidate, target in candidates:
            os.replace(candidate, target)
            promoted.append(target)
    except BaseException:
        for target in reversed(promoted):
            target.unlink(missing_ok=True)
        raise


def main() -> int:
    authority, receipt, freeze = exact_authority()
    request = load_json(REQUEST)
    require(request["totals"]["expanded_block_operation_pairs"] == 47, "request operation total")
    require(request["totals"]["unique_target_blocks"] == 47, "request unique target total")

    all_targets = [path for config in PAPERS.values() for key, path in paths_for(config).items() if key in {
        "choices", "adjudication", "patch", "handoff", "validation"
    }]
    require(len(all_targets) == 10 and len(set(all_targets)) == 10, "fresh output path collision inventory")
    for path in all_targets:
        require(not path.exists(), f"refusing to overwrite {relative(path)}")

    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    candidates: list[tuple[Path, Path]] = []
    summary: list[dict] = []
    staging = Path(tempfile.mkdtemp(prefix=".round10-p30-p31-exact-resign-", dir=ROOT))
    try:
        for paper_id, config in PAPERS.items():
            paths = paths_for(config)
            staged = {key: staging / paper_id / path.name for key, path in paths.items() if key in {
                "choices", "adjudication", "patch", "handoff", "validation"
            }}
            staged["choices"].parent.mkdir(parents=True, exist_ok=True)

            prepared_rows = receipt["prepared_execution_evidence"][paper_id]
            expected_prepared = {
                "author_choices": paths["old_choices"],
                "author_adjudication": paths["old_adjudication"],
                "patch": paths["old_patch"],
                "writer_handoff": paths["old_handoff"],
                "writer_validation": paths["old_validation"],
                "revision_roadmap": paths["roadmap"],
                "claim_surface_manifest": paths["claim"],
            }
            for key, path in expected_prepared.items():
                require(path.is_file(), f"{paper_id}: missing prepared artifact {relative(path)}")
                same_artifact_row(prepared_rows[key], binding(path), f"{paper_id} prepared {key}")
            for name in ("choices", "adjudication", "patch", "handoff", "validation"):
                expected = config.get(f"prepared_{name}_sha256")
                old_name = "old_" + name
                if old_name in paths and expected:
                    require(sha(paths[old_name]) == expected, f"{paper_id}: pinned prepared {name} drift")

            old_choices = load_json(paths["old_choices"])
            choices = replace_event_ids(old_choices)
            require(decision_projection(choices) == decision_projection(old_choices), f"{paper_id}: substantive choice drift")
            require(choices["display_order"]["mode"] == "source_traceability", f"{paper_id}: display mode drift")
            require(all(row["author_triage"] == "will_address" for row in choices["author_adjudications"]), f"{paper_id}: triage drift")
            require(not choices["collateral_authorizations"], f"{paper_id}: collateral authority appeared")
            require(all(not row["claim_strength_authorizations"] for row in choices["author_adjudications"]), f"{paper_id}: claim authority appeared")
            staged["choices"].write_bytes(json_bytes(choices))

            build_stdout = run_official(
                "build-adjudication", str(paths["roadmap"]),
                "--base", str(paths["base"]),
                "--block-manifest", str(paths["manifest"]),
                "--claim-surface", str(paths["claim"]),
                "--author-choices", str(staged["choices"]),
                "--artifact-root", str(ROOT),
                "--output", str(staged["adjudication"]),
            )
            validate_stdout = run_official(
                "validate-adjudication", str(paths["roadmap"]), str(staged["adjudication"]),
                "--base", str(paths["base"]),
                "--block-manifest", str(paths["manifest"]),
                "--claim-surface", str(paths["claim"]),
                "--artifact-root", str(ROOT),
            )
            adjudication = load_json(staged["adjudication"])
            require(decision_projection(adjudication) == decision_projection(choices) | {
                "schema_version": "author-adjudication/1.0",
                "revision_round": adjudication["revision_round"],
                "roadmap_sha256": adjudication["roadmap_sha256"],
                "base_draft_sha256": adjudication["base_draft_sha256"],
                "claim_surface_manifest_sha256": adjudication["claim_surface_manifest_sha256"],
                "adjudication_status": "complete",
            }, f"{paper_id}: official adjudication decision projection drift")
            require(adjudication["author_events"] == choices["author_events"], f"{paper_id}: official event divergence")

            old_patch = load_json(paths["old_patch"])
            patch = copy.deepcopy(old_patch)
            patch["author_adjudication_sha256"] = sha(staged["adjudication"])
            patch["author_decision_digest"] = rr.author_decision_digest(adjudication)
            require(patch["ops"] == old_patch["ops"], f"{paper_id}: prepared patch ops/new_text changed")
            unchanged_patch = copy.deepcopy(patch)
            unchanged_old = copy.deepcopy(old_patch)
            for value in (unchanged_patch, unchanged_old):
                value.pop("author_adjudication_sha256")
                value.pop("author_decision_digest")
            require(unchanged_patch == unchanged_old, f"{paper_id}: patch changed outside exact re-sign bindings")

            roadmap_raw = paths["roadmap"].read_bytes()
            claim_raw = paths["claim"].read_bytes()
            base_raw = paths["base"].read_bytes()
            roadmap = load_json(paths["roadmap"])
            claim = load_json(paths["claim"])
            store = rr._standalone_store(ROOT)
            surfaces = rr.validate_claim_surface_manifest(
                claim, claim_surface_raw=claim_raw, roadmap=roadmap,
                roadmap_raw=roadmap_raw, base_raw=base_raw, artifact_store=store,
            )
            rr.validate_author_adjudication(
                adjudication, adjudication_raw=staged["adjudication"].read_bytes(),
                roadmap=roadmap, roadmap_raw=roadmap_raw, claim_surface=claim,
                claim_surface_raw=claim_raw, base_raw=base_raw, surfaces_by_id=surfaces,
            )
            patch_validation = rr.validate_review_patch_authorization(
                patch, base_raw=base_raw, roadmap=roadmap, roadmap_raw=roadmap_raw,
                adjudication=adjudication, adjudication_raw=staged["adjudication"].read_bytes(),
                claim_surface=claim, claim_surface_raw=claim_raw, surfaces_by_id=surfaces,
            )
            require(patch_validation["status"] == "pass", f"{paper_id}: patch authorization projection")
            staged["patch"].write_bytes(json_bytes(patch))

            block_order, item_order = request_targets(request, paper_id)
            require(len(block_order) == config["ops"] == len(set(block_order)), f"{paper_id}: request count/order")
            require([op["block_id"] for op in patch["ops"]] == block_order, f"{paper_id}: patch/request block order")
            require(choices["display_order"]["item_ids"] == item_order, f"{paper_id}: source-traceability item order")
            require(adjudication["display_order"]["item_ids"] == item_order, f"{paper_id}: adjudication item order")
            require(all(op["op"] == "replace_block" for op in patch["ops"]), f"{paper_id}: non-replace op")

            old_handoff = load_json(paths["old_handoff"])
            handoff = copy.deepcopy(old_handoff)
            handoff["generated_at_utc"] = generated_at
            handoff["status"] = "WRITER_PATCH_REEMITTED_UNDER_EXACT_CONFIRMATION_NOT_APPLIED"
            handoff["preparation_evidence_authority_role"] = PREPARATION_ROLE
            handoff["authority"] = copy.deepcopy(authority)
            handoff["controlling_authority"] = {
                "mode": "EXACT_CONFIRMATION_130_BLOCK_STAGE4_PRIME_EXECUTION",
                "prepared_evidence_authority_role": PREPARATION_ROLE,
                "exact_confirmation_authority": copy.deepcopy(authority),
                "expanded_request": binding(REQUEST),
            }
            handoff["prepared_writer_evidence"] = {
                "authority_role": PREPARATION_ROLE,
                "author_choices": binding(paths["old_choices"]),
                "author_adjudication": binding(paths["old_adjudication"]),
                "revision_patch": binding(paths["old_patch"]),
                "writer_handoff": binding(paths["old_handoff"]),
                "writer_validation": binding(paths["old_validation"]),
            }
            handoff["fresh_authority"]["author_choices"] = binding(staged["choices"], represented_path=paths["choices"])
            handoff["fresh_authority"]["author_adjudication"] = binding(staged["adjudication"], represented_path=paths["adjudication"])
            handoff["fresh_authority"]["author_decision_digest"] = patch["author_decision_digest"]
            handoff["patch"] = binding(staged["patch"], represented_path=paths["patch"]) | {
                "ops": config["ops"], "applied": False,
            }
            handoff["next_legal_action"] = (
                "Independent root audit must first bind this exact-confirmation re-emission; "
                "only the independently pinned final-emission manifest may then feed the independent applier."
            )
            if paper_id == "P30":
                root_layout = paths["notes"] / "stage4_prime_correction_round3_root_layout_repreflight_receipt.json"
                require(root_layout.is_file(), "P30: missing prepared root layout receipt")
                handoff["layout_preflight_lineage"]["prepared_patch_sha256"] = old_patch and sha(paths["old_patch"])
                handoff["layout_preflight_lineage"]["current_patch_sha256"] = sha(staged["patch"])
                handoff["layout_preflight_lineage"]["root_repreflight_status"] = (
                    "PREPARED_PATCH_PASS_REUSED_BY_EXACT_OP_EQUALITY"
                )
                handoff["layout_preflight_lineage"]["root_repreflight_receipt"] = binding(root_layout)
                handoff["layout_preflight_lineage"]["fresh_ops_byte_equal_to_prepared"] = True
            staged["handoff"].write_bytes(json_bytes(handoff))

            old_validation = load_json(paths["old_validation"])
            validation = copy.deepcopy(old_validation)
            validation["validated_at_utc"] = generated_at
            validation["status"] = "PASS_EXACT_CONFIRMATION_WRITER_REEMISSION_ONLY"
            validation["preparation_evidence_authority_role"] = PREPARATION_ROLE
            validation["authority"] = copy.deepcopy(authority)
            validation["prepared_writer_evidence"] = handoff["prepared_writer_evidence"]
            validation["official_ars_validation"] = {
                "build_adjudication": "PASS",
                "build_adjudication_stdout": build_stdout,
                "validate_adjudication": "PASS",
                "validate_adjudication_stdout": validate_stdout,
                "author_choice_input_schema": "PASS",
                "roadmap_schema_and_source_order": "PASS",
                "claim_surface_manifest": "PASS_EMPTY_REGISTERED_POPULATION",
                "author_adjudication_schema_scope_and_digest": "PASS",
                "patch_authorization_projection": patch_validation,
                "ars_revision_roadmap_module": str(ROADMAP_CLI),
            }
            validation["prepared_patch_equivalence"] = {
                "prepared_patch": binding(paths["old_patch"]),
                "fresh_patch": binding(staged["patch"], represented_path=paths["patch"]),
                "ops_equal_including_new_text": True,
                "only_resigned_top_level_fields": [
                    "author_adjudication_sha256", "author_decision_digest",
                ],
                "op_count": config["ops"],
                "ops_canonical_sha256": canonical_json_digest(patch["ops"]),
            }
            validation["outputs"]["author_choices"] = binding(staged["choices"], represented_path=paths["choices"])
            validation["outputs"]["author_adjudication"] = binding(staged["adjudication"], represented_path=paths["adjudication"])
            validation["outputs"]["revision_patch"] = binding(staged["patch"], represented_path=paths["patch"])
            validation["outputs"]["writer_handoff"] = binding(staged["handoff"], represented_path=paths["handoff"])
            validation["totals"]["requested_unique_replace_block_pairs"] = config["ops"]
            validation["totals"]["emitted_unique_replace_block_ops"] = config["ops"]
            validation["totals"]["old_hash_replay_pass"] = config["ops"]
            validation["totals"]["exact_authority_projection_pass"] = config["ops"]
            validation["totals"]["patch_applications_run"] = 0
            validation["totals"]["latex_builds_run"] = 0
            validation["boundary"] = (
                "This receipt validates exact-confirmation writer re-emission only; it does not "
                "apply the patch, regenerate a matrix, build a manuscript, or authorize a later stage."
            )
            staged["validation"].write_bytes(json_bytes(validation))

            # Final candidate checks, including the exact hashes searched by the root finalizer.
            fresh_bindings = {
                "author_choices": binding(staged["choices"], represented_path=paths["choices"]),
                "author_adjudication": binding(staged["adjudication"], represented_path=paths["adjudication"]),
                "patch": binding(staged["patch"], represented_path=paths["patch"]),
                "writer_handoff": binding(staged["handoff"], represented_path=paths["handoff"]),
                "writer_validation": binding(staged["validation"], represented_path=paths["validation"]),
            }
            for document_path in (staged["handoff"], staged["validation"]):
                document = load_json(document_path)
                for key, row in authority.items():
                    same_artifact_row(document["authority"][key], row, f"{paper_id} internal authority {key}")
                serialized = json.dumps(document, ensure_ascii=False)
                for key in ("author_choices", "author_adjudication", "patch"):
                    require(fresh_bindings[key]["sha256"] in serialized, f"{paper_id}: writer evidence lacks {key} hash")
            require(load_json(staged["patch"])["ops"] == old_patch["ops"], f"{paper_id}: final candidate ops drift")
            require(load_json(staged["validation"])["totals"]["emitted_unique_replace_block_ops"] == config["ops"], f"{paper_id}: validation count")

            for key in ("choices", "adjudication", "patch", "handoff", "validation"):
                candidates.append((staged[key], paths[key]))
            summary.append({
                "paper_id": paper_id,
                "ops": config["ops"],
                "ops_canonical_sha256": canonical_json_digest(patch["ops"]),
                "artifacts": fresh_bindings,
            })

        require(sum(row["ops"] for row in summary) == 47, "aggregate operation count")
        promote_all(candidates)

        for row in summary:
            config = PAPERS[row["paper_id"]]
            paths = paths_for(config)
            target_key_for_artifact = {
                "author_choices": "choices",
                "author_adjudication": "adjudication",
                "patch": "patch",
                "writer_handoff": "handoff",
                "writer_validation": "validation",
            }
            for key, expected in row["artifacts"].items():
                target_key = target_key_for_artifact[key]
                same_artifact_row(binding(paths[target_key]), expected, f"{row['paper_id']} promoted {key}")
            require(load_json(paths["patch"])["ops"] == load_json(paths["old_patch"])["ops"], f"{row['paper_id']}: promoted ops drift")

        print(json.dumps({
            "status": "PASS_EXACT_CONFIRMATION_P30_P31_WRITER_REEMISSION",
            "generated_at_utc": generated_at,
            "authority_sha256": AUTHORITY_HASHES,
            "aggregate_ops": 47,
            "papers": summary,
        }, ensure_ascii=False, indent=2))
    finally:
        shutil.rmtree(staging, ignore_errors=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
