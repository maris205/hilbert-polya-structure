#!/usr/bin/env python3
"""Verify copied-input hashes, upstream package manifests, and source anchors."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import stat
import sys
from pathlib import Path, PurePosixPath
from typing import Any


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True) + "\n").encode("ascii")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def read_unique(path: Path) -> Any:
    def hook(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        if len(pairs) != len({key for key, _ in pairs}):
            raise ValueError("duplicate JSON key")
        return dict(pairs)
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


def locked_review_path(root: Path, relative: str) -> Path:
    pure = PurePosixPath(relative)
    if (type(relative) is not str or pure.is_absolute() or ".." in pure.parts
            or relative != pure.as_posix() or pure.parts[:3] != ("inputs", "preauthority", "reviews")):
        raise AssertionError("unsafe review path")
    path = root.joinpath(*pure.parts)
    review_root = (root / "inputs" / "preauthority" / "reviews").resolve(strict=True)
    if not path.is_file() or path.is_symlink() or path.resolve(strict=True).parent != review_root:
        raise AssertionError("review path")
    return path


def exact_ready(path: Path) -> str:
    text = path.read_bytes().decode("utf-8")
    lines = text.splitlines()
    if not lines or lines[-1] != "PLAN_READY":
        raise AssertionError("exact PLAN_READY verdict")
    return text


def verify_nested_manifest(root: Path, manifest: Path) -> int:
    entries: dict[str, str] = {}
    for line in manifest.read_text(encoding="utf-8").splitlines():
        digest, rel = line.split(maxsplit=1)
        rel = rel.lstrip(" *")
        pure = PurePosixPath(rel)
        if len(digest) != 64 or any(ch not in "0123456789abcdef" for ch in digest) or pure.is_absolute() or ".." in pure.parts or rel != pure.as_posix() or rel in entries:
            raise AssertionError("unsafe nested manifest")
        entries[rel] = digest
    actual = sorted(path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_file() and not path.is_symlink() and path != manifest)
    if sorted(entries) != actual:
        raise AssertionError("nested manifest file set")
    for rel, expected in entries.items():
        if sha256(root / rel) != expected:
            raise AssertionError("nested manifest hash")
    return len(entries)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    args = parser.parse_args()
    root = Path(args.root)
    try:
        if not root.is_absolute() or root.is_symlink() or not root.is_dir() or root.resolve(strict=True) != root:
            raise AssertionError("root")
        contract = read_unique(root / "contracts" / "PROJECT_CONTRACT.json")
        lock = read_unique(root / "contracts" / "INPUT_LOCK.json")
        if lock["project_slug"] != contract["project_slug"] or lock["schema"] != "stage0-input-lock-v1" or lock["upstream_roots"] != contract["upstream_roots"]:
            raise AssertionError("input lock header")
        actual_rows = []
        for path in sorted((root / "inputs").rglob("*"), key=lambda item: item.relative_to(root).as_posix()):
            metadata = os.lstat(path)
            rel = path.relative_to(root).as_posix()
            if stat.S_ISLNK(metadata.st_mode) or (not stat.S_ISDIR(metadata.st_mode) and not stat.S_ISREG(metadata.st_mode)):
                raise AssertionError("input node type")
            if stat.S_ISREG(metadata.st_mode):
                actual_rows.append({"mode": f"{stat.S_IMODE(metadata.st_mode):04o}", "path": rel, "sha256": sha256(path), "size": metadata.st_size})
        if lock["entries"] != actual_rows or lock["entry_count"] != len(actual_rows):
            raise AssertionError("input rows")
        plan = contract["plan_gate"]
        if (plan.get("status") != "PLAN_READY" or type(plan.get("plan_review_path")) is not str
                or type(plan.get("plan_review_sha256")) is not str
                or type(plan.get("plan_review_receipt_path")) is not str
                or type(plan.get("plan_review_receipt_sha256")) is not str
                or len(plan["plan_review_receipt_sha256"]) != 64
                or any(character not in "0123456789abcdef" for character in plan["plan_review_receipt_sha256"])):
            raise AssertionError("plan gate is not fail-closed")
        handoff_path = root / "inputs" / "preauthority" / "PRE_STAGE0_HANDOFF.md"
        plan_path = root / "inputs" / "preauthority" / "PAPER_PLAN.md"
        claims_path = root / "inputs" / "preauthority" / "CLAIMS_EVIDENCE.md"
        if sha256(handoff_path) != contract["pre_stage0_handoff_sha256"]:
            raise AssertionError("handoff")
        if sha256(plan_path) != plan["paper_plan_sha256"]:
            raise AssertionError("plan")
        if sha256(claims_path) != plan["claims_evidence_sha256"]:
            raise AssertionError("claims")
        if "plan_gate_sha256" in plan and sha256(root / "inputs" / "preauthority" / "PLAN_GATE.json") != plan["plan_gate_sha256"]:
            raise AssertionError("plan gate")
        review_path = locked_review_path(root, plan["plan_review_path"])
        receipt_path = locked_review_path(root, plan["plan_review_receipt_path"])
        if sha256(review_path) != plan["plan_review_sha256"] or sha256(receipt_path) != plan["plan_review_receipt_sha256"]:
            raise AssertionError("plan review")
        if exact_ready(review_path).rstrip("\n") != exact_ready(receipt_path).rstrip("\n"):
            raise AssertionError("review/receipt content")
        receipt = plan["plan_review_receipt_sha256"]
        gate_path = root / "inputs" / "preauthority" / "PLAN_GATE.json"
        gate_text = gate_path.read_text(encoding="utf-8") if gate_path.is_file() else ""
        if receipt not in handoff_path.read_text(encoding="utf-8") or receipt not in plan_path.read_text(encoding="utf-8") + gate_text:
            raise AssertionError("plan review receipt provenance")
        nested_counts = []
        for record in contract["frozen_manifests"]:
            manifest = root / record["path"]
            if sha256(manifest) != record["sha256"]:
                raise AssertionError("frozen manifest digest")
            nested_counts.append({"entry_count": verify_nested_manifest(manifest.parent, manifest), "path": record["path"], "sha256": record["sha256"]})
        source_paths = sorted(list((root / "inputs").rglob("SOURCE_LOCK.md")) + list((root / "inputs").rglob("SOURCE_AUDIT.md")) + list((root / "inputs").rglob("SOURCE_REAUDIT.md")))
        source_text = "\n".join(path.read_text(encoding="utf-8") for path in source_paths)
        missing = [token for token in contract["source_anchor_tokens"] if token not in source_text]
        if missing:
            raise AssertionError("source anchor")
        output = {
            "payload": {
                "copied_input_entry_count": len(actual_rows),
                "frozen_manifests": nested_counts,
                "input_lock_sha256": sha256(root / "contracts" / "INPUT_LOCK.json"),
                "plan_status": plan["status"],
                "plan_review_receipt_path": plan["plan_review_receipt_path"],
                "plan_review_receipt_sha256": receipt,
                "plan_review_sha256": plan["plan_review_sha256"],
                "source_anchor_count": len(contract["source_anchor_tokens"]),
            },
            "schema": "stage0-source-audit-v1",
            "status": "PASS",
        }
        sys.stdout.buffer.write(canonical(output))
        return 0
    except (AssertionError, KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
        sys.stdout.buffer.write(canonical({"payload": {"code": "REJECT_SOURCE_LOCK"}, "schema": "stage0-source-audit-v1", "status": "REJECT"}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
