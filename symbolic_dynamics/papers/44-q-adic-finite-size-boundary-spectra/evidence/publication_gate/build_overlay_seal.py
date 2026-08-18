#!/usr/bin/env python3
"""Build the acyclic writer manifest and externally anchored overlay seal."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import stat
import sys
from pathlib import Path, PurePosixPath
from typing import Any


CANDIDATE_ID = "SD-C46"
LEGACY_STATIC_MANIFEST_SHA256 = "5f93fd2595a173e30e8d745c18fc74550fb6415df2f63429c4433576f05a30b0"
LEGACY_PREOUTPUT_SEAL_SHA256 = "2135bb54e94326b336cb384f25340339df1c057497d7eaeb170632e482122fec"
LEGACY_STATE_A_TREE_SHA256 = "be4f7ee57be4fc901b7ecc40f258937ebc20c504d07f0b0964348ffe20b57ed4"
PREDECESSOR_WRITER_MANIFEST_SHA256 = "f3b98a455ac6dd2aaeaf32f37a5ef9d69cb7bff45c640a24a80a9ed40f8814b5"
PREDECESSOR_PUBLICATION_SEAL_SHA256 = "9dfcedb2dba3fd0b637c565e974c5831a6f4a2fa6f7e2269583d862811e5eb72"
FINAL_PDF_SHA256 = "3ee4b7662f9d5f8fdd6a410461c7c8094cb5c2782fbbb486603f56b9841cb66d"

WRITER_MANIFEST = "WRITER_MANIFEST.sha256"
PUBLICATION_SEAL = "evidence/publication_gate/PUBLICATION_OVERLAY_SEAL.json"
PUBLICATION_EVIDENCE = "evidence/publication_gate/PUBLICATION_SMOKE_EVIDENCE.json"
BRIDGE_CONTRACT = "evidence/publication_gate/STATEB_BRIDGE_CONTRACT.json"
BRIDGE_CODE_PATHS = [
    "evidence/publication_gate/build_overlay_seal.py",
    "evidence/publication_gate/publication_auditor.py",
    "evidence/publication_gate/publication_transaction.py",
    "evidence/publication_gate/run_publication_smoke.py",
    "evidence/publication_gate/stateb_bridge.py",
]


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       separators=(",", ": "), allow_nan=False) + "\n").encode("ascii")


def sha_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def sha_file(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def safe_relative(value: str) -> bool:
    pure = PurePosixPath(value)
    return value != "" and "\\" not in value and not pure.is_absolute() \
        and all(part not in {"", ".", ".."} for part in pure.parts)


def secure_root(root: Path) -> None:
    if not root.is_absolute() or root.is_symlink() or not root.is_dir() \
            or root.resolve(strict=True) != root \
            or stat.S_IMODE(os.lstat(root).st_mode) != 0o755:
        raise ValueError("unsafe root")


def build_manifest(root: Path) -> tuple[dict[str, str], bytes]:
    excluded = {WRITER_MANIFEST, PUBLICATION_SEAL}
    files: list[str] = []
    for path in root.rglob("*"):
        relative = path.relative_to(root).as_posix()
        metadata = os.lstat(path)
        if path.name == "__pycache__" or path.suffix in {".pyc", ".pyo"}:
            raise ValueError("cache forbidden")
        if stat.S_ISLNK(metadata.st_mode) or not (
                stat.S_ISREG(metadata.st_mode) or stat.S_ISDIR(metadata.st_mode)):
            raise ValueError("nonregular node")
        expected_mode = 0o644 if stat.S_ISREG(metadata.st_mode) else 0o755
        if stat.S_IMODE(metadata.st_mode) != expected_mode:
            raise ValueError("overlay mode drift: " + relative)
        if stat.S_ISREG(metadata.st_mode) and relative not in excluded:
            if not safe_relative(relative):
                raise ValueError("unsafe relative")
            files.append(relative)
    files.sort()
    manifest = {relative: sha_file(root / relative) for relative in files}
    raw = "".join(f"{manifest[relative]}  {relative}\n" for relative in files).encode("ascii")
    return manifest, raw


def seal_object(root: Path, manifest: dict[str, str], manifest_raw: bytes) -> dict[str, Any]:
    return {
        "bridge_code_paths": BRIDGE_CODE_PATHS,
        "bridge_contract_sha256": sha_file(root / BRIDGE_CONTRACT),
        "candidate_id": CANDIDATE_ID,
        "excluded_from_writer_manifest": [PUBLICATION_SEAL, WRITER_MANIFEST],
        "external_anchor_contract": {
            "publication_seal_sha256": "required_out_of_band_lowercase_hex64_before_parse",
            "stage1_commit": "required_out_of_band_nonzero_lowercase_hex40_for_state_B",
            "values_embedded_in_seal": False,
        },
        "final_pdf_sha256": FINAL_PDF_SHA256,
        "hash_domains": {
            "legacy_static_core": "frozen_58_row_STATIC_TREE_MANIFEST",
            "publication_seal": "excluded_from_writer_manifest_and_anchored_out_of_band",
            "state_B_paper_manifest": "full_published_root_including_writer_overlay_excluding_PREOUTPUT_STATIC_SEAL_and_manifest_self",
            "writer_manifest": "C_sorted_regular_file_rows_excluding_manifest_self_and_publication_seal",
        },
        "legacy_core": {
            "preoutput_seal_sha256": LEGACY_PREOUTPUT_SEAL_SHA256,
            "state_A_final_tree_sha256": LEGACY_STATE_A_TREE_SHA256,
            "static_manifest_entry_count": 58,
            "static_manifest_sha256": LEGACY_STATIC_MANIFEST_SHA256,
        },
        "legacy_frozen_auditor_state_B_disposition":
            "REJECT_STATIC_TREE_MISMATCH_EXPECTED_SUPERSESSION",
        "overlay_file_count": len(manifest) + 2,
        "physical_negative_expectations": {
            "required_state_B_attacks": 8,
            "seal_reclose_rejection_code": "PUBLICATION_SEAL_SHA256_MISMATCH",
        },
        "predecessor_overlay": {
            "publication_seal_sha256": PREDECESSOR_PUBLICATION_SEAL_SHA256,
            "writer_manifest_sha256": PREDECESSOR_WRITER_MANIFEST_SHA256,
        },
        "publication_smoke_evidence_sha256": sha_file(root / PUBLICATION_EVIDENCE),
        "schema": "paper44-stateb-publication-overlay-seal-v2",
        "state_semantics": {
            "PUBLISHED_STATE_A_EXACT": "legacy_State_A_runtime_preserved_under_exact_superseding_overlay",
            "PUBLISHED_STATE_B_EXACT": "external_H1_bound_three_times_and_direct_FINAL_B_passes",
            "PREDECESSOR_STATE_A_EXACT": "bounded_upgrade_source_state_only",
        },
        "status": "HOLD_FOR_INDEPENDENT_STATEB_PUBLICATION_AUDIT",
        "transaction_expectations": {
            "first_state_B_atomic_output_exchanges": 1,
            "forced_late_failure_exit": 86,
            "idempotent_second_replacements": 0,
            "overlay_upgrade_rollback_exit": 87,
            "state_B_rollback_exit": 87,
            "stage_all_before_target_write": True,
        },
        "writer_manifest_entry_count": len(manifest),
        "writer_manifest_sha256": sha_bytes(manifest_raw),
    }


def main() -> int:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--root", required=True)
    arguments = parser.parse_args()
    root = Path(arguments.root)
    secure_root(root)
    manifest, manifest_raw = build_manifest(root)
    manifest_path = root / WRITER_MANIFEST
    seal_path = root / PUBLICATION_SEAL
    manifest_path.write_bytes(manifest_raw)
    manifest_path.chmod(0o644)
    seal_raw = canonical(seal_object(root, manifest, manifest_raw))
    seal_path.write_bytes(seal_raw)
    seal_path.chmod(0o644)
    sys.stdout.buffer.write(canonical({
        "payload": {
            "overlay_file_count": len(manifest) + 2,
            "publication_seal_sha256": sha_bytes(seal_raw),
            "writer_manifest_entry_count": len(manifest),
            "writer_manifest_sha256": sha_bytes(manifest_raw),
        },
        "schema": "paper44-stateb-overlay-build-v1",
        "status": "SEALED",
    }))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
