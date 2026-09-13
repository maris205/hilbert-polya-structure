#!/usr/bin/env python3
"""Read-only exact-successor checks and support-artifact proposals for Round 3.

Only stdout is written. Official pure parser/manifest mechanics assign manifest
data; a separate raw-marker splice checks the five already-applied replacement
patches. This is not a scientific validator, full integrity gate, or applier.
"""
import argparse
import copy
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent.parent
PREFIX = "BATCH_ROUND10_STAGE4_5_ROUND3_"
REQUEST_SHA = "ddf2ebb85dfe2408eaae6bce0203a6e9c2d808f1a053407d9001aeac61ce6d54"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def read_json(path):
    return json.loads(path.read_bytes())


def serialized(value):
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def binding(path, root=ROOT):
    raw = path.read_bytes()
    return {"path": str(path.relative_to(root)), "bytes": len(raw), "sha256": digest(raw)}


def artifact(path, root):
    desc = binding(path, root)
    return {"path": desc["path"], "sha256": desc["sha256"]}


def check_binding(expected):
    observed = binding(ROOT / expected["path"])
    require(all(observed[k] == v for k, v in expected.items()),
            f"binding mismatch: {expected['path']}")


def independent_blocks(raw):
    """Concrete anchored UTF-8 TeX subset; does not use the ARS parser."""
    markers = list(re.finditer(rb"(?m)^<!--block:(B[0-9]{4,})-->\r?\n", raw))
    require(markers and markers[0].start() == 0, "unexpected marker prefix")
    blocks = {}
    for index, marker in enumerate(markers):
        end = markers[index + 1].start() if index + 1 < len(markers) else len(raw)
        segment = raw[marker.end():end]
        text = segment.rstrip(b"\r\n")
        block_id = marker[1].decode("ascii")
        require(block_id not in blocks, "duplicate raw marker")
        blocks[block_id] = {"start": marker.end(), "end": marker.end() + len(text),
                            "text": text, "whole": raw[marker.start():end]}
    return blocks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["prepare-support", "verify-support"])
    parser.add_argument("--paper", choices=["P29", "P30", "P31", "P32", "P33"])
    parser.add_argument("--ars-root", type=Path, required=True)
    args = parser.parse_args()
    sys.path.insert(0, str(args.ars_root))
    from scripts._block_parser import parse_document
    from scripts.ars_anchorize_draft import anchorize_text, build_manifest

    request_path = ROOT / (PREFIX + "EXACT_CORRECTION_PATCH_REQUEST.json")
    require(digest(request_path.read_bytes()) == REQUEST_SHA, "exact request changed")
    request = read_json(request_path)
    scope = read_json(ROOT / (PREFIX + "CORRECTION_PREPARATION_SCOPE.json"))
    prior_inputs = {p["paper_id"]: p for p in scope["current_inputs"]}
    check_binding({"path": request["new_reader"], "sha256": request["new_reader_sha256"]})
    rows, files = [], []
    for item in request["patches"]:
        paper_id = item["paper_id"]
        if args.paper and args.paper != paper_id:
            continue
        for key in ("base_draft", "block_manifest", "issue_list", "patch"):
            check_binding(item[key])
        prior = prior_inputs[paper_id]
        for key in ("bundle", "bibliography"):
            check_binding(prior[key])
        base_path = ROOT / item["base_draft"]["path"]
        paper_root = base_path.parent.parent
        notes = base_path.parent
        round_no = item["next_revision_round"]
        new_path = notes / f"stage4_prime_revision_round{round_no}.tex"
        report_path = Path(str(new_path) + ".apply-report.json")
        new_raw, base_raw = new_path.read_bytes(), base_path.read_bytes()
        patch = read_json(ROOT / item["patch"]["path"])
        report = read_json(report_path)
        require(report["patch_digest"] == item["patch"]["sha256"], f"{paper_id} report/patch mismatch")
        require(report["base_draft_hash"] == digest(base_raw)[:12] and
                report["output_draft_hash"] == digest(new_raw)[:12], f"{paper_id} report/base/post mismatch")
        old_blocks, new_blocks = independent_blocks(base_raw), independent_blocks(new_raw)
        require(list(old_blocks) == list(new_blocks), f"{paper_id} raw block order changed")
        ops = patch["ops"]
        targets = {op["block_id"] for op in ops}
        require(len(targets) == len(ops) and targets == set(item["proposed_blocks"]),
                f"{paper_id} approved targets differ")
        require({i for op in ops for i in op["roadmap_item_ids"]} == set(item["proposed_correction_ids"]),
                f"{paper_id} approved issue IDs differ")
        edits = []
        for op in ops:
            require(op["op"] == "replace_block", f"{paper_id} unsupported operation")
            block_id = op["block_id"]
            replacement = op["new_text"].encode("utf-8")
            require(replacement == new_blocks[block_id]["text"], f"{paper_id}/{block_id} new text mismatch")
            old = old_blocks[block_id]
            edits.append((old["start"], old["end"], replacement))
        replay = base_raw
        for start, end, replacement in sorted(edits, reverse=True):
            replay = replay[:start] + replacement + replay[end:]
        require(replay == new_raw, f"{paper_id} independent whole-byte splice mismatch")
        changed = {b for b in old_blocks if old_blocks[b]["whole"] != new_blocks[b]["whole"]}
        require(changed == targets, f"{paper_id} unexpected/no-op raw block changes")
        require(report["counters"]["blocks_preserved_byte_identical"] == len(old_blocks) - len(targets),
                f"{paper_id} preservation counter mismatch")
        new_text = new_raw.decode("utf-8")
        require(anchorize_text(new_text) == new_text, f"{paper_id} new anchors would be needed")
        parsed = parse_document(new_text)
        require(all(b.block_id is not None for b in parsed.blocks), f"{paper_id} unlabeled block")
        manifest = build_manifest(new_raw, parsed)
        manifest_path = notes / f"stage4_prime_revision_round{round_no}.block-manifest.json"
        previous = read_json(ROOT / prior["bundle"]["path"])
        require(previous["final_draft"] == artifact(base_path, paper_root), f"{paper_id} old endpoint mismatch")
        bundle = copy.deepcopy(previous)
        require(bundle["rounds"][-1]["revision_round"] + 1 == round_no, f"{paper_id} round gap")
        bundle["rounds"].append({
            "kind": "integrity_correction", "revision_round": round_no,
            "pre_round_draft": artifact(base_path, paper_root),
            "pre_round_block_manifest": artifact(ROOT / item["block_manifest"]["path"], paper_root),
            "issue_list": artifact(ROOT / item["issue_list"]["path"], paper_root),
            "integrity_authorization": artifact(notes / "stage4_5_round3_correction_integrity_authorization.json", paper_root),
            "revision_patch": artifact(ROOT / item["patch"]["path"], paper_root),
            "apply_report": artifact(report_path, paper_root),
            "post_round_draft": artifact(new_path, paper_root),
        })
        bundle["final_draft"] = artifact(new_path, paper_root)
        bundle_path = notes / f"stage4_prime_revision_evidence_bundle_round{round_no}.json"
        for path, value in ((manifest_path, manifest), (bundle_path, bundle)):
            content = serialized(value)
            if args.mode == "prepare-support":
                require(not path.exists(), f"new target already exists: {path}")
                files.append({"path": str(path.relative_to(ROOT)), "content": content})
            else:
                require(path.read_bytes() == content.encode("utf-8"), f"support bytes differ: {path}")
        rows.append({"paper_id": paper_id, "new_draft": binding(new_path),
                     "apply_report": binding(report_path), "prior_bundle": prior["bundle"],
                     "new_manifest_path": str(manifest_path.relative_to(ROOT)),
                     "new_bundle_path": str(bundle_path.relative_to(ROOT)),
                     "new_manifest_sha256": digest(serialized(manifest).encode("utf-8")),
                     "new_bundle_sha256": digest(serialized(bundle).encode("utf-8")),
                     "prior_rounds_preserved": len(previous["rounds"]),
                     "new_total_rounds": len(bundle["rounds"]),
                     "ordinary_issue_ids": item["proposed_correction_ids"],
                     "blocks_changed": sorted(changed), "blocks_total": len(old_blocks),
                     "blocks_byte_preserved": len(old_blocks) - len(changed),
                     "independent_byte_splice": "PASS_EXACT_CURRENT_REPLACEMENTS",
                     "official_anchorizer_would_change_draft": False,
                     "author_pending_no_write_ids": item["author_pending_no_write_ids"]})
    print(json.dumps({"schema_version": "round10-stage4.5-round3-applied-correction-check/1.0",
                      "status": "PASS_EXACT_SUCCESSOR_AND_SUPPORT_CHECKS_ONLY", "mode": args.mode,
                      "checked_at_utc": datetime.now(timezone.utc).isoformat(),
                      "request": binding(request_path), "script": binding(Path(__file__).resolve()),
                      "ars_root": str(args.ars_root), "papers": rows, "proposed_new_files": files,
                      "checker_writes": False, "full_integrity_pass": False}, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(json.dumps({"status": "STOP_APPLIED_CORRECTION_CHECK_FAILED",
                          "type": type(exc).__name__, "detail": str(exc), "checker_writes": False}))
        raise SystemExit(1)
