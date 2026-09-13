#!/usr/bin/env python3
"""Read-only binding/proposal check; never applies a patch or writes a receipt.

The `bindings` mode supplies manifest-owned hashes to the patch assembly layer.
The `validate` mode runs the official integrity-list and structural patch
validators only. It does not validate author authorization, apply a patch,
construct a successor draft, build a PDF, or confer an integrity verdict.
"""
import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.dont_write_bytecode = True


def read_json(path):
    return json.loads(path.read_bytes())


def binding(path, root):
    raw = path.read_bytes()
    return {"path": str(path.relative_to(root)), "bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest()}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["bindings", "validate"])
    parser.add_argument("--ars-root", required=True, type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    sys.path.insert(0, str(args.ars_root))
    from scripts._block_parser import parse_document
    from scripts.revision_roadmap import validate_integrity_correction_list
    from scripts.ars_apply_revision_patch import validate_patch

    scope_path = root / "BATCH_ROUND10_STAGE4_5_ROUND3_CORRECTION_PREPARATION_SCOPE.json"
    scope = read_json(scope_path)
    proposals_path = root / "BATCH_ROUND10_STAGE4_5_ROUND3_CORRECTION_PROPOSALS.json"
    proposals = read_json(proposals_path)
    outputs = []
    for item in scope["current_inputs"]:
        paper_id = item["paper_id"]
        for key in ("current_draft", "block_manifest", "bibliography", "bundle"):
            expected = item[key]
            observed = binding(root / expected["path"], root)
            require(observed == expected, f"{paper_id} protected {key} binding mismatch")
        base_path = root / item["current_draft"]["path"]
        base_raw = base_path.read_bytes()
        parsed = parse_document(base_raw.decode("utf-8"))
        blocks = parsed.block_by_id()
        manifest = read_json(root / item["block_manifest"]["path"])
        require(manifest["base_draft_hash"] == item["current_draft"]["sha256"][:12],
                f"{paper_id} manifest base mismatch")
        hashes = {b["block_id"]: b["old_hash"] for b in manifest["blocks"]}
        require(len(hashes) == len(manifest["blocks"]) == len(blocks),
                f"{paper_id} duplicate/missing manifest blocks")
        for block_id, block in blocks.items():
            require(hashes.get(block_id) == block.norm_hash,
                    f"{paper_id}/{block_id} manifest normalization mismatch")
        candidate_path = base_path.parent / "stage4_5_round3_correction_candidate_blocks.json"
        candidate = read_json(candidate_path)
        require(candidate["base_path"] == item["current_draft"]["path"],
                f"{paper_id} wrong candidate base")
        require(candidate["next_revision_round"] == item["current_revision_round"] + 1,
                f"{paper_id} candidate round is not continuous")
        seen = set()
        candidates = []
        evidence_paths = set()
        for row in candidate["candidates"]:
            block_id = row["block_id"]
            require(block_id not in seen, f"{paper_id}/{block_id} duplicate candidate")
            seen.add(block_id)
            require(row["old_text"] == blocks[block_id].normalized_text,
                    f"{paper_id}/{block_id} old_text mismatch")
            require(row["new_text"] != row["old_text"], f"{paper_id}/{block_id} no-op candidate")
            for evidence in row["evidence"]:
                path = evidence["path"] if isinstance(evidence, dict) else evidence.split("#", 1)[0]
                require((root / path).is_file(), f"{paper_id}/{block_id} missing evidence: {path}")
                evidence_paths.add(path)
            candidates.append({"block_id": block_id, "old_hash": hashes[block_id],
                               "issue_ids": row["issue_ids"],
                               "ordinary_patch_selected": all(x.startswith("IL-") for x in row["issue_ids"]),
                               "new_text_sha256": hashlib.sha256(row["new_text"].encode()).hexdigest()})
        ordinary = [r for r in proposals["ordinary_items"] if r["paper_id"] == paper_id]
        expected_ids = {r["id"] for r in ordinary}
        proposed_ids = {x for r in candidates if r["ordinary_patch_selected"] for x in r["issue_ids"]}
        pending_ids = set(candidate["author_pending"])
        withdrawn_ids = {"IL-SERIOUS-1"} if paper_id == "P30" else set()
        require(not (proposed_ids & pending_ids or proposed_ids & withdrawn_ids or pending_ids & withdrawn_ids),
                f"{paper_id} overlapping dispositions")
        require(proposed_ids | pending_ids | withdrawn_ids == expected_ids,
                f"{paper_id} ordinary item accounting gap")
        out = {"paper_id": paper_id, "base": item["current_draft"],
               "block_manifest": item["block_manifest"], "candidate": binding(candidate_path, root),
               "next_revision_round": candidate["next_revision_round"],
               "blocks_total": len(blocks), "candidates": candidates,
               "ordinary_ids_proposed": sorted(proposed_ids), "author_pending": sorted(pending_ids),
               "withdrawn_false_positives": sorted(withdrawn_ids),
               "evidence_bindings": [binding(root / p, root) for p in sorted(evidence_paths)]}
        if args.mode == "validate":
            issue_path = base_path.parent / "stage4_5_round3_correction_issue_list.json"
            patch_path = base_path.parent / "stage4_5_round3_correction_patch.json"
            issue_raw = issue_path.read_bytes()
            issue_list = json.loads(issue_raw)
            patch = read_json(patch_path)
            issues = validate_integrity_correction_list(issue_list, issue_list_raw=issue_raw, base_raw=base_raw)
            require(set(issues) == expected_ids - withdrawn_ids, f"{paper_id} issue-list accounting gap")
            require(patch["issue_list_sha256"] == hashlib.sha256(issue_raw).hexdigest(),
                    f"{paper_id} patch/list mismatch")
            require(patch["revision_round"] == issue_list["revision_round"] == candidate["next_revision_round"],
                    f"{paper_id} patch/list round mismatch")
            wanted = {r["block_id"]: r for r in candidate["candidates"]
                      if all(x.startswith("IL-") for x in r["issue_ids"])}
            require(len(patch["ops"]) == len(wanted), f"{paper_id} patch operation count mismatch")
            for op in patch["ops"]:
                row = wanted[op["block_id"]]
                require(op["op"] == "replace_block" and op["new_text"] == row["new_text"]
                        and op["roadmap_item_ids"] == row["issue_ids"],
                        f"{paper_id}/{op['block_id']} patch differs from candidate")
                require(not op["claim_strength_changes"] and not op["collateral_authorization_ids"],
                        f"{paper_id} forbidden integrity authority declarations")
                for issue_id in op["roadmap_item_ids"]:
                    require(issue_id in proposed_ids, f"{paper_id} pending issue touched")
                    require({"block_id": op["block_id"], "allowed_operations": ["replace_block"]}
                            in issues[issue_id]["proposed_targets"], f"{paper_id} target outside proposal")
            analysis = validate_patch(patch, base_raw, parsed, touched_ratio_threshold=0.6)
            out.update({"issue_list": binding(issue_path, root), "patch": binding(patch_path, root),
                        "official_proposal_validation": "PASS_SCHEMA_BASE_TARGET_AND_STRUCTURE_ANALYSIS",
                        "structural_flags": analysis["structural_flags"],
                        "semantic_heading_target_requires_explicit_ack": ["B0041"] if paper_id == "P29" else [],
                        "author_authorization_checked": False, "author_authorization_satisfied": False,
                        "apply_run": False, "new_draft_created": False, "integrity_verdict": "NOT_ISSUED"})
        outputs.append(out)
    print(json.dumps({"schema_version": "round10-stage4.5-round3-proposal-binding-check/1.0",
                      "mode": args.mode, "status": "PASS_PROPOSAL_CHECKS_ONLY",
                      "checked_at_utc": datetime.now(timezone.utc).isoformat(),
                      "scope": binding(scope_path, root), "source_proposals": binding(proposals_path, root),
                      "script": binding(Path(__file__).resolve(), root),
                      "ars_root": str(args.ars_root), "papers": outputs,
                      "authorization_or_integrity_pass_claimed": False,
                      "writes_performed_by_checker": False}, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(json.dumps({"status": "STOP_PROPOSAL_CHECK_FAILED", "type": type(exc).__name__,
                          "detail": str(exc), "writes_performed_by_checker": False}, ensure_ascii=False))
        raise SystemExit(1)
