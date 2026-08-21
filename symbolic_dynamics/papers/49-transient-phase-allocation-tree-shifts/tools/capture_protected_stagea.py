#!/usr/bin/env python3
"""Capture and verify the immutable Paper 49 Stage-A authority tree.

The emitted manifest is path-relative.  In check mode this program performs no
writes under the overlay or either protected root.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import stat
from typing import Any


AUTHORITY = Path(
    "/root/autodl-tmp/hilbert-polya-structure/symbolic_dynamics/papers/"
    "49-transient-phase-allocation-tree-shifts"
)
STAGE0 = Path("/tmp/p49_stage0_candidate")
POST_AUDIT = Path("/tmp/p49_authority_postoutput_independent_cross_audit")
WRITER_AUDIT = Path("/tmp/p49_writer_fresh_independent_reaudit")
OVERLAY = Path(__file__).resolve().parents[1]
EVIDENCE = OVERLAY / "evidence"

STATIC_MANIFEST_SHA = "9498faaa791a619345eef6f61c0a677725423d0d04df515931d7e9c3913f5b4a"
PREOUTPUT_SEAL_SHA = "c214342e7a10664f53ff82f5fdf458ca58fb94caf8e479d5c8527062c9b82cb3"
INPUT_LOCK_SHA = "6dde8bf6106747beba9d905e784e0cb7eefe9a5837a962435f9a2dd6fedfb8b5"
RUN_SUMMARY_SHA = "7d69e6aa9617869a4e80a83bfa5dc2168d9461641c739e2de28a6cbdf0a5bbe7"
SCIENCE_SHA = "c3512ccc3f609c5c6f97fa55999270eee19db433d15aca8deefa285e7fcf60c1"
ACTIVE_PDF_SHA = "aa2a5df28cd7139d9e19aea9bb035cd03f5d787e36260d8a52ed2d33ead930a4"
INITIAL_RAW_CAPTURE_SHA = "b207fa77cf78efb777c69f64542bcf6f611663e9eb68f5847064dfd5306dfafc"
INITIAL_RAW_AGGREGATE_SHA = "529962fbc9cdba9fef627f2dcbafeb23fb599ba3a4f802254ccdd84b34484cc8"

POST_ANCHORS = {
    "AUDIT_MANIFEST.json": "ffa43d4e1b84ef4aa7c1fc977a8fa1ab311430f0d4d9c4ad3490aefbcc6f3cf0",
    "AUDIT_REPORT.md": "53a7f7aa85a894e5e9af5ea0a403a902fbb963f2100d9e6bc1ec67763d3ce121",
    "AUDIT_RESULT.json": "9f4a9d308e71671be29240f1864fb640ceb6e67b8b72e6b185d72748b005b671",
    "HANDOFF.md": "43e6f069673e7b0ed50a24e075a8a7dbeb496b671d3b3597adda767bb8b3fd62",
}
WRITER_ANCHORS = {
    "SHA256SUMS.txt": "3c883d01ad29874b91c70393b43b60661ea5bbe2bbf0040187d1e7cc61aa9041",
    "AUDIT_REPORT.md": "a65fba4719b0c446100240cf3034e55346cbbe0f9518e500fe79617a4dc736b9",
    "HANDOFF.md": "724c31dcf9b6f628058f98af890560636e5d16f93d7f68b74e5b6c8a13381d9c",
}

OUTPUT_FILES = [
    "outputs/state_A/RUN_SUMMARY.json",
    "outputs/state_A/audits/independence_audit.json",
    "outputs/state_A/audits/mutation_audit.json",
    "outputs/state_A/audits/source_audit.json",
    "outputs/state_A/audits/static_audit.json",
    "outputs/state_A/audits/type_audit.json",
    "outputs/state_A/results/exact_comparison.json",
    "outputs/state_A/results/independent.json",
    "outputs/state_A/results/production.json",
]
OUTPUT_DIRS = [
    "outputs",
    "outputs/state_A",
    "outputs/state_A/audits",
    "outputs/state_A/results",
]


def canonical(value: Any) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode("ascii")


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def read_regular(path: Path, expected_mode: int = 0o644) -> tuple[bytes, os.stat_result]:
    info = os.lstat(path)
    if not stat.S_ISREG(info.st_mode) or stat.S_IMODE(info.st_mode) != expected_mode:
        raise RuntimeError(f"unsafe regular file: {path}")
    descriptor = os.open(path, os.O_RDONLY | os.O_NOFOLLOW)
    try:
        opened = os.fstat(descriptor)
        if not stat.S_ISREG(opened.st_mode) or stat.S_IMODE(opened.st_mode) != expected_mode:
            raise RuntimeError(f"unsafe opened file: {path}")
        chunks = []
        while chunk := os.read(descriptor, 1 << 20):
            chunks.append(chunk)
    finally:
        os.close(descriptor)
    return b"".join(chunks), info


def unique_json(raw: bytes) -> Any:
    def hook(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        if len(pairs) != len({key for key, _ in pairs}):
            raise RuntimeError("duplicate JSON key")
        return dict(pairs)

    return json.loads(raw.decode("ascii"), object_pairs_hook=hook)


def frame(root: Path) -> list[dict[str, Any]]:
    root_info = os.lstat(root)
    if not stat.S_ISDIR(root_info.st_mode) or stat.S_ISLNK(root_info.st_mode):
        raise RuntimeError(f"unsafe root: {root}")
    rows: list[dict[str, Any]] = [
        {
            "kind": "directory",
            "mode": f"{stat.S_IMODE(root_info.st_mode):04o}",
            "mtime_ns": root_info.st_mtime_ns,
            "path": ".",
        }
    ]

    def visit(directory: Path) -> None:
        with os.scandir(directory) as stream:
            entries = sorted(stream, key=lambda entry: os.fsencode(entry.name))
        for entry in entries:
            path = Path(entry.path)
            info = os.lstat(path)
            relative = path.relative_to(root).as_posix()
            if stat.S_ISDIR(info.st_mode) and not stat.S_ISLNK(info.st_mode):
                rows.append(
                    {
                        "kind": "directory",
                        "mode": f"{stat.S_IMODE(info.st_mode):04o}",
                        "mtime_ns": info.st_mtime_ns,
                        "path": relative,
                    }
                )
                visit(path)
            elif stat.S_ISREG(info.st_mode):
                raw, opened = read_regular(path)
                rows.append(
                    {
                        "kind": "regular",
                        "mode": f"{stat.S_IMODE(opened.st_mode):04o}",
                        "mtime_ns": opened.st_mtime_ns,
                        "path": relative,
                        "sha256": digest(raw),
                        "size": len(raw),
                    }
                )
            else:
                raise RuntimeError(f"nonregular node: {path}")

    visit(root)
    return rows


def source_map(rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    result = {}
    for row in rows:
        path = row["path"]
        if path == "." or path == "outputs" or path.startswith("outputs/"):
            continue
        result[path] = {key: value for key, value in row.items() if key != "path"}
    return result


def count(rows: list[dict[str, Any]], kind: str) -> int:
    return sum(row["kind"] == kind for row in rows)


def tsv(rows: list[dict[str, Any]]) -> bytes:
    lines = ["relative_path\tkind\tmode\tsize\tmtime_ns\tsha256"]
    for row in rows:
        lines.append(
            "\t".join(
                [
                    row["path"],
                    row["kind"],
                    row["mode"],
                    str(row.get("size", "")),
                    str(row["mtime_ns"]),
                    str(row.get("sha256", "")),
                ]
            )
        )
    return ("\n".join(lines) + "\n").encode("ascii")


def exclusive_write(path: Path, raw: bytes) -> None:
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW
    descriptor = os.open(path, flags, 0o644)
    try:
        os.write(descriptor, raw)
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def build_outputs() -> dict[str, bytes]:
    authority_first = frame(AUTHORITY)
    authority_second = frame(AUTHORITY)
    if canonical(authority_first) != canonical(authority_second):
        raise RuntimeError("authority changed between consecutive captures")
    stage0 = frame(STAGE0)
    if count(authority_first, "directory") != 21 or count(authority_first, "regular") != 75:
        raise RuntimeError("authority count mismatch")
    if count(stage0, "directory") != 17 or count(stage0, "regular") != 66:
        raise RuntimeError("Stage0 count mismatch")
    if (STAGE0 / "outputs").exists() or (STAGE0 / "outputs").is_symlink():
        raise RuntimeError("source Stage0 candidate is not output-free")
    if source_map(authority_first) != source_map(stage0):
        raise RuntimeError("authority source is not byte/type/mode/mtime exact to Stage0")

    stage0_by_path = {row["path"]: row for row in stage0}
    if stage0_by_path["STATIC_MANIFEST.json"]["sha256"] != STATIC_MANIFEST_SHA:
        raise RuntimeError("Stage0 static manifest anchor mismatch")
    if stage0_by_path["PREOUTPUT_SEAL.txt"]["sha256"] != PREOUTPUT_SEAL_SHA:
        raise RuntimeError("Stage0 preoutput seal anchor mismatch")
    if stage0_by_path["contracts/INPUT_LOCK.json"]["sha256"] != INPUT_LOCK_SHA:
        raise RuntimeError("Stage0 input lock anchor mismatch")

    authority_by_path = {row["path"]: row for row in authority_first}
    output_paths = sorted(
        path for path in authority_by_path if path == "outputs" or path.startswith("outputs/")
    )
    if output_paths != sorted(OUTPUT_DIRS + OUTPUT_FILES):
        raise RuntimeError("authority output namespace mismatch")
    for path in OUTPUT_DIRS:
        row = authority_by_path[path]
        if row["kind"] != "directory" or row["mode"] != "0755":
            raise RuntimeError(f"unsafe output directory: {path}")
    for path in OUTPUT_FILES:
        row = authority_by_path[path]
        if row["kind"] != "regular" or row["mode"] != "0644":
            raise RuntimeError(f"unsafe output file: {path}")
        raw, _ = read_regular(AUTHORITY / path)
        value = unique_json(raw)
        if canonical(value) != raw or value.get("status") != "PASS":
            raise RuntimeError(f"noncanonical/non-PASS output: {path}")
    if authority_by_path["outputs/state_A/RUN_SUMMARY.json"]["sha256"] != RUN_SUMMARY_SHA:
        raise RuntimeError("run-summary anchor mismatch")
    production = authority_by_path["outputs/state_A/results/production.json"]["sha256"]
    independent = authority_by_path["outputs/state_A/results/independent.json"]["sha256"]
    if production != SCIENCE_SHA or independent != SCIENCE_SHA:
        raise RuntimeError("production/independent science mismatch")

    for name, expected in POST_ANCHORS.items():
        raw, _ = read_regular(POST_AUDIT / name)
        if digest(raw) != expected:
            raise RuntimeError(f"post-output audit anchor mismatch: {name}")
    post_result = unique_json(read_regular(POST_AUDIT / "AUDIT_RESULT.json")[0])
    if post_result.get("status") != "PASS" or post_result["payload"].get("verdict") != "P49 INDEPENDENT POST-OUTPUT CLEAN":
        raise RuntimeError("post-output independent verdict mismatch")
    for name, expected in WRITER_ANCHORS.items():
        raw, _ = read_regular(WRITER_AUDIT / name)
        if digest(raw) != expected:
            raise RuntimeError(f"writer re-audit anchor mismatch: {name}")
    writer_report = read_regular(WRITER_AUDIT / "AUDIT_REPORT.md")[0].decode("utf-8")
    if "WRITER PRE-INSTALL CLEAN" not in writer_report or ACTIVE_PDF_SHA not in writer_report:
        raise RuntimeError("writer re-audit verdict/PDF binding mismatch")

    static_lines = []
    for row in stage0:
        if row["kind"] == "regular":
            static_lines.append(f"{row['sha256']}  {row['path']}")
    if len(static_lines) != 66:
        raise RuntimeError("static source file count mismatch")
    static_manifest = ("\n".join(static_lines) + "\n").encode("ascii")

    protected_tsv = tsv(authority_first)
    frame_material = canonical(authority_first)
    replay = {
        "payload": {
            "active_pdf_sha256": ACTIVE_PDF_SHA,
            "authority_capture_twice_byte_exact": True,
            "authority_directory_count_including_root": 21,
            "authority_file_count": 75,
            "authority_relative_tree_sha256": digest(protected_tsv),
            "authority_source_equals_stage0_bytes_type_mode_mtime": True,
            "current_capture_rows_sha256": digest(frame_material),
            "initial_raw_capture_aggregate_sha256": INITIAL_RAW_AGGREGATE_SHA,
            "initial_raw_capture_file_sha256": INITIAL_RAW_CAPTURE_SHA,
            "output_directory_count": 4,
            "output_file_count": 9,
            "run_summary_sha256": RUN_SUMMARY_SHA,
            "science_sha256": SCIENCE_SHA,
            "stage0_directory_count_including_root": 17,
            "stage0_file_count": 66,
            "stage0_input_lock_sha256": INPUT_LOCK_SHA,
            "stage0_preoutput_seal_sha256": PREOUTPUT_SEAL_SHA,
            "stage0_static_manifest_sha256": STATIC_MANIFEST_SHA,
            "static_source_sha256s_sha256": digest(static_manifest),
        },
        "schema": "p49-final-writer-protected-stagea-replay-v1",
        "status": "PASS",
    }
    anchors = {
        "payload": {
            "active_pdf_sha256": ACTIVE_PDF_SHA,
            "post_output_audit": {
                "anchors": POST_ANCHORS,
                "verdict": "P49 INDEPENDENT POST-OUTPUT CLEAN",
            },
            "writer_reaudit": {
                "anchors": WRITER_ANCHORS,
                "candidate_before_after_exact": True,
                "verdict": "WRITER PRE-INSTALL CLEAN",
            },
        },
        "schema": "p49-final-writer-independent-audit-anchors-v1",
        "status": "PASS",
    }
    return {
        "INDEPENDENT_AUDIT_ANCHORS.json": canonical(anchors),
        "PROTECTED_STAGEA_REPLAY.json": canonical(replay),
        "PROTECTED_STAGEA_TREE.tsv": protected_tsv,
        "STATIC_SOURCE_SHA256SUMS.txt": static_manifest,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = build_outputs()
    if args.write:
        for name, raw in expected.items():
            exclusive_write(EVIDENCE / name, raw)
    else:
        for name, raw in expected.items():
            actual, _ = read_regular(EVIDENCE / name)
            if actual != raw:
                raise RuntimeError(f"protected evidence mismatch: {name}")
    print(
        "PROTECTED_STAGEA_PASS live_files=75 live_dirs=21 outputs=9+4 "
        f"tree_sha256={digest(expected['PROTECTED_STAGEA_TREE.tsv'])}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
