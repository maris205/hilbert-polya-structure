#!/usr/bin/env python3
"""Capture and replay the protected P50 Stage-A tree without mutation.

The portable manifest contains only relative paths, types, modes, sizes, and
content hashes.  The writer-owned receipt authenticates independently
produced post-output and writer-reaudit reports but does not adopt either as a
writer-side CLEAN or installation claim.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import stat
from pathlib import Path
from typing import Any


HEADER = "relative_path\tkind\tmode\tsize\tsha256\n"
EXPECTED = {
    "live_nodes": 105,
    "live_regular": 80,
    "live_directories": 25,
    "stage0_nodes": 92,
    "stage0_regular": 71,
    "stage0_directories": 21,
    "output_nodes": 13,
    "output_regular": 9,
    "output_directories": 4,
}
ANCHORS = {
    "pre_writer_live_raw_frame_sha256": "b3a26554825eb11b691338ebca882997ffd0c75ba9b5046315e57398e226e9f8",
    "stage0_static_manifest_sha256": "7fbb2c4f02bf4cb9905d0b5221cdd071b5c22fa3decbb925851ad00f8704bc11",
    "stage0_preoutput_seal_sha256": "1244dd1554b930ce958451a4406f8383119e43d398e02d3fc19ac2ee8b8aa36c",
    "stage0_input_lock_sha256": "c4224cbf5a6248e1af28f1100f226e2d678c1db852829da17e2cbaaa6fe71b39",
    "postoutput_result_sha256": "9c08d2719d4b63a503c572dce37f812042ff483f91ba05b9673033251e4d2e0d",
    "postoutput_report_sha256": "ef3b13baf948711484fd15846d285835bc60728831d9e4658682a1b31e760039",
    "writer_reaudit_result_sha256": "9f57242d10556afa4a826cd0a7f7dbe6bec4cd2848add6cb1bb70add9e53c8f2",
    "writer_reaudit_report_sha256": "2edc7bf112a44de36c0a11aa8d3c58dcc01585380ef31bcfc3c7eb771a026f0b",
    "preclosure_writer_manifest_sha256": "3fb69bb1c13dfba87f97379eaf18a31503540f6ff56822ccfe6b433aba59ecdb",
    "active_pdf_sha256": "bf0c9ea39d55596fab6d873a4062a836451c0a65113d2d245b0a7d94e3243736",
}
OUTPUT_FILES = {
    "outputs/state_A/RUN_SUMMARY.json": "b5e6f9be00114bed563d6e5a2ee4be0d5fd9c8344a70e3f7c16bfb7577d1b1b5",
    "outputs/state_A/audits/independence_audit.json": "a38ae5abfeb1ce3f24a864d010c656a1aeeb82b58700c6517395f24d109063e8",
    "outputs/state_A/audits/mutation_audit.json": "3fda29b14da294faa229612aecf765a2de0b0fb209351e0938413f2b8fb5efa3",
    "outputs/state_A/audits/source_audit.json": "7641d5a0de418b64c56ec3a971c8af66a963f6e6be13cdff0f6d967d36331579",
    "outputs/state_A/audits/static_audit.json": "e1370fb8a11644e8de487246a36713f636dd080304ac84d35c5deb50894bc334",
    "outputs/state_A/audits/type_audit.json": "5dc199eb10692d2fe0c32712749bf279de3cfd6b7202a8dcf6f26de424dd40a8",
    "outputs/state_A/results/exact_comparison.json": "db56367f7849e973445f60a92acf0e10be81ff4347d760b8060541236a5648d3",
    "outputs/state_A/results/independent.json": "58bd79bb6cad6a5ec3c47f3d7816b4e1fcc57f8967244c78d62238d8690595ac",
    "outputs/state_A/results/production.json": "58bd79bb6cad6a5ec3c47f3d7816b4e1fcc57f8967244c78d62238d8690595ac",
}
OUTPUT_DIRECTORIES = {
    "outputs", "outputs/state_A", "outputs/state_A/audits", "outputs/state_A/results",
}


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True, allow_nan=False) + "\n").encode("ascii")


def sha_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def sha(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def strict_root(path: Path, label: str) -> Path:
    if not path.is_absolute() or path.is_symlink() or path.resolve(strict=True) != path:
        raise SystemExit(f"{label}_ROOT_INVALID")
    metadata = os.lstat(path)
    if not stat.S_ISDIR(metadata.st_mode):
        raise SystemExit(f"{label}_ROOT_INVALID")
    return path


def capture(root: Path) -> list[dict[str, Any]]:
    rows = []
    paths = [root]
    for directory, dirnames, filenames in os.walk(root, topdown=True, followlinks=False):
        dirnames.sort()
        filenames.sort()
        base = Path(directory)
        paths.extend(base / name for name in [*dirnames, *filenames])
    for path in paths:
        metadata = os.lstat(path)
        relative = "." if path == root else path.relative_to(root).as_posix()
        row: dict[str, Any] = {
            "mode": f"{stat.S_IMODE(metadata.st_mode):04o}",
            "mtime_ns": metadata.st_mtime_ns,
            "path": relative,
            "size": metadata.st_size,
        }
        if stat.S_ISDIR(metadata.st_mode):
            row["kind"] = "directory"
        elif stat.S_ISREG(metadata.st_mode):
            row.update(kind="regular", sha256=sha(path))
        else:
            raise SystemExit(f"NONREGULAR_NODE:{relative}")
        rows.append(row)
    rows.sort(key=lambda row: os.fsencode(row["path"]))
    if len(rows) != len({row["path"] for row in rows}):
        raise SystemExit("DUPLICATE_PATH")
    return rows


def portable(rows: list[dict[str, Any]]) -> bytes:
    lines = [HEADER]
    for row in rows:
        size = str(row["size"]) if row["kind"] == "regular" else "-"
        digest = row.get("sha256", "-")
        lines.append(f"{row['path']}\t{row['kind']}\t{row['mode']}\t{size}\t{digest}\n")
    return "".join(lines).encode("ascii")


def count(rows: list[dict[str, Any]], kind: str) -> int:
    return sum(row["kind"] == kind for row in rows)


def source_projection(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    result = []
    for row in rows:
        if row["path"] == "." or row["path"] == "outputs" or row["path"].startswith("outputs/"):
            continue
        normalized = dict(row)
        if normalized["kind"] == "directory":
            normalized.pop("size", None)
        result.append(normalized)
    return result


def static_sums(rows: list[dict[str, Any]]) -> bytes:
    selected = [row for row in rows if row["kind"] == "regular"]
    if len(selected) != EXPECTED["stage0_regular"]:
        raise SystemExit("STAGE0_REGULAR_COUNT")
    return "".join(f"{row['sha256']}  {row['path']}\n" for row in selected).encode("ascii")


def unique_json(path: Path) -> tuple[bytes, dict[str, Any]]:
    raw = path.read_bytes()
    def hook(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        if len(pairs) != len({key for key, _ in pairs}):
            raise ValueError("duplicate key")
        return dict(pairs)
    value = json.loads(raw.decode("utf-8"), object_pairs_hook=hook)
    return raw, value


def safe_new(path: Path, root: Path, raw: bytes) -> None:
    if root not in path.parents or os.path.lexists(path):
        raise SystemExit(f"UNSAFE_OR_EXISTING_OUTPUT:{path.name}")
    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0), 0o644)
    try:
        os.fchmod(descriptor, 0o644)
        offset = 0
        while offset < len(raw):
            offset += os.write(descriptor, raw[offset:])
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def build(authority: Path, stage0: Path, post_result: Path, post_report: Path,
          writer_result: Path, writer_report: Path) -> tuple[bytes, bytes, bytes]:
    first = capture(authority)
    second = capture(authority)
    if first != second:
        raise SystemExit("LIVE_DOUBLE_CAPTURE_CHANGED")
    if (len(first), count(first, "regular"), count(first, "directory")) != (
        EXPECTED["live_nodes"], EXPECTED["live_regular"], EXPECTED["live_directories"]
    ):
        raise SystemExit("LIVE_COUNTS")
    frozen = capture(stage0)
    if (len(frozen), count(frozen, "regular"), count(frozen, "directory")) != (
        EXPECTED["stage0_nodes"], EXPECTED["stage0_regular"], EXPECTED["stage0_directories"]
    ) or (stage0 / "outputs").exists():
        raise SystemExit("STAGE0_COUNTS_OR_OUTPUTS")
    if source_projection(first) != source_projection(frozen):
        raise SystemExit("LIVE_SOURCE_NOT_EXACT_STAGE0")
    outputs = [row for row in first if row["path"] == "outputs" or row["path"].startswith("outputs/")]
    if (len(outputs), count(outputs, "regular"), count(outputs, "directory")) != (
        EXPECTED["output_nodes"], EXPECTED["output_regular"], EXPECTED["output_directories"]
    ):
        raise SystemExit("OUTPUT_COUNTS")
    output_map = {row["path"]: row for row in outputs}
    if set(output_map) != set(OUTPUT_FILES) | OUTPUT_DIRECTORIES:
        raise SystemExit("OUTPUT_PATHS")
    for relative in OUTPUT_DIRECTORIES:
        if output_map[relative]["kind"] != "directory" or output_map[relative]["mode"] != "0755":
            raise SystemExit(f"OUTPUT_DIRECTORY:{relative}")
    for relative, digest in OUTPUT_FILES.items():
        row = output_map[relative]
        if row["kind"] != "regular" or row["mode"] != "0644" or row["sha256"] != digest:
            raise SystemExit(f"OUTPUT_FILE:{relative}")
    if sha(stage0 / "STATIC_MANIFEST.json") != ANCHORS["stage0_static_manifest_sha256"] \
            or sha(stage0 / "PREOUTPUT_SEAL.txt") != ANCHORS["stage0_preoutput_seal_sha256"] \
            or sha(stage0 / "contracts/INPUT_LOCK.json") != ANCHORS["stage0_input_lock_sha256"]:
        raise SystemExit("STAGE0_ANCHOR")
    summary_raw, summary = unique_json(authority / "outputs/state_A/RUN_SUMMARY.json")
    if sha_bytes(summary_raw) != OUTPUT_FILES["outputs/state_A/RUN_SUMMARY.json"] \
            or summary.get("status") != "PASS" or summary.get("payload", {}).get("artifact_count_excluding_summary") != 8:
        raise SystemExit("RUN_SUMMARY")
    for row in summary["payload"]["artifacts"]:
        target = authority / "outputs/state_A" / row["path"]
        if sha(target) != row["sha256"] or target.stat().st_size != row["size"]:
            raise SystemExit("RUN_SUMMARY_ROW")
    if (authority / "outputs/state_A/results/production.json").read_bytes() != (authority / "outputs/state_A/results/independent.json").read_bytes():
        raise SystemExit("SCIENCE_MISMATCH")

    post_raw, post = unique_json(post_result)
    if sha_bytes(post_raw) != ANCHORS["postoutput_result_sha256"] or sha(post_report) != ANCHORS["postoutput_report_sha256"] \
            or post.get("disposition") != "P50 INDEPENDENT POST-OUTPUT CLEAN" \
            or post.get("writer_owned_verdict_used") is not False \
            or post.get("live_top_level_integration_invocations") != 0 \
            or set(post.get("before_after", {}).values()) != {True}:
        raise SystemExit("POSTOUTPUT_AUDIT_ANCHOR")
    writer_raw, reaudit = unique_json(writer_result)
    if sha_bytes(writer_raw) != ANCHORS["writer_reaudit_result_sha256"] or sha(writer_report) != ANCHORS["writer_reaudit_report_sha256"] \
            or reaudit.get("status") != "WRITER PRE-INSTALL CLEAN" \
            or reaudit.get("active_pdf_sha256") != ANCHORS["active_pdf_sha256"] \
            or reaudit.get("candidate_manifest_sha256") != ANCHORS["preclosure_writer_manifest_sha256"]:
        raise SystemExit("WRITER_REAUDIT_ANCHOR")

    manifest_raw = portable(first)
    sums_raw = static_sums(frozen)
    output_tree_hash = sha_bytes(canonical([
        {key: value for key, value in row.items() if key != "mtime_ns"}
        for row in outputs
    ]))
    receipt = canonical({
        "anchors": {
            **ANCHORS,
            "protected_stagea_manifest_sha256": sha_bytes(manifest_raw),
            "protected_stage0_sums_sha256": sha_bytes(sums_raw),
            "installed_output_tree_sha256": output_tree_hash,
        },
        "counts": EXPECTED,
        "evidence_boundary": "This writer-owned replay authenticates protected bytes and independently produced audit records. It is not a proof, CLEAN verdict, installation, or authority-write authorization.",
        "external_independent_dispositions": {
            "postoutput": "P50 INDEPENDENT POST-OUTPUT CLEAN",
            "writer_reaudit": "WRITER PRE-INSTALL CLEAN",
            "adopted_as_writer_clean": False,
        },
        "output_mtimes_ns": {row["path"]: row["mtime_ns"] for row in outputs},
        "producer_role": "P50_WRITER",
        "replay": {
            "authority_double_capture_equal": True,
            "declared_output_namespace_exact": True,
            "frozen_stage0_source_exact_in_live": True,
            "independent_postoutput_result_report_exact": True,
            "independent_writer_reaudit_result_report_exact": True,
            "live_top_level_integration_invocations_by_writer": 0,
            "portable_manifest_exact": True,
            "run_summary_closure_exact": True,
            "science_engine_bytes_equal": True,
        },
        "schema": "paper50.writer-protected-stagea-replay.v1",
        "status": "PASS",
    })
    return manifest_raw, sums_raw, receipt


def main() -> None:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--authority", required=True, type=Path)
    parser.add_argument("--stage0", required=True, type=Path)
    parser.add_argument("--postoutput-result", required=True, type=Path)
    parser.add_argument("--postoutput-report", required=True, type=Path)
    parser.add_argument("--writer-reaudit-result", required=True, type=Path)
    parser.add_argument("--writer-reaudit-report", required=True, type=Path)
    parser.add_argument("--writer-root", required=True, type=Path)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--record", action="store_true")
    action.add_argument("--check", action="store_true")
    args = parser.parse_args()
    authority = strict_root(args.authority, "AUTHORITY")
    stage0 = strict_root(args.stage0, "STAGE0")
    writer = strict_root(args.writer_root, "WRITER")
    manifest, sums, receipt = build(authority, stage0, args.postoutput_result, args.postoutput_report,
                                    args.writer_reaudit_result, args.writer_reaudit_report)
    targets = (
        (writer / "PROTECTED_STAGEA_TREE.tsv", manifest),
        (writer / "PROTECTED_STAGE0_SHA256SUMS.txt", sums),
        (writer / "evidence/INDEPENDENT_REPLAY_RECEIPT.json", receipt),
    )
    if args.record:
        for path, raw in targets:
            safe_new(path, writer, raw)
        print(f"RECORDED protected_sha256={sha_bytes(manifest)} replay_sha256={sha_bytes(receipt)}")
    else:
        for path, raw in targets:
            if path.is_symlink() or not path.is_file() or path.read_bytes() != raw or stat.S_IMODE(os.lstat(path).st_mode) != 0o644:
                raise SystemExit(f"REPLAY_RECORD_MISMATCH:{path.name}")
        print(f"PASS protected_sha256={sha_bytes(manifest)} replay_sha256={sha_bytes(receipt)}")


if __name__ == "__main__":
    main()
