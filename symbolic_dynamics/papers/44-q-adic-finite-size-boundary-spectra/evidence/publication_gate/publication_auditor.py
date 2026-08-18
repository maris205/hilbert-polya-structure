#!/usr/bin/env python3
"""Externally anchored dual-state publication auditor for Paper 44.

The frozen legacy auditor is never weakened.  Exact writer-overlay roots are
an explicit superseding state in which that auditor must reject the added
static paths with ``STATIC_TREE_MISMATCH``.  State B additionally requires an
out-of-band Stage1 commit and a direct legacy ``audit_integrity FINAL B``.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import stat
import subprocess
import sys
from pathlib import Path, PurePosixPath
from typing import Any


CANDIDATE_ID = "SD-C46"
LEGACY_STATIC_MANIFEST_SHA256 = "5f93fd2595a173e30e8d745c18fc74550fb6415df2f63429c4433576f05a30b0"
LEGACY_PREOUTPUT_SEAL_SHA256 = "2135bb54e94326b336cb384f25340339df1c057497d7eaeb170632e482122fec"
LEGACY_STATE_A_TREE_SHA256 = "be4f7ee57be4fc901b7ecc40f258937ebc20c504d07f0b0964348ffe20b57ed4"
PREDECESSOR_WRITER_MANIFEST_SHA256 = "3cae37f13f488d34008df4f237121c4faf37a498f717977a6cf5b9491cf0a380"
PREDECESSOR_PUBLICATION_SEAL_SHA256 = "4d1484da96bce56def7b97006a48bd0060b0306ce23248f7aed3b6fe66b5b92f"
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
FILES_A = [
    "RESULT_LEDGER.json", "audits/external_auditor_mutations.json",
    "audits/independence_audit.json", "audits/integrity_audit.json",
    "audits/proof_audit.json", "audits/route_independent.json",
    "audits/route_primary.json", "audits/source_audit.json", "audits/type_audit.json",
    "data/source_packet.json", "evaluations/route_a/SD-C46/2026-08-18.yaml",
    "reports/EXPERIMENT_REPORT.md", "results/evaluator_a.json", "results/evaluator_b.json",
    "results/exact_comparison.json", "tests/mutation_results.json",
]
OUTPUT_DIRS = [
    "outputs", "outputs/audits", "outputs/data", "outputs/evaluations",
    "outputs/evaluations/route_a", "outputs/evaluations/route_a/SD-C46",
    "outputs/reports", "outputs/results", "outputs/tests",
]
SMOKE_CASES = [
    ("source_exact", 0, "PASS", "SOURCE_OVERLAY_EXACT"),
    ("predecessor_exact", 0, "PASS", "PREDECESSOR_STATE_A_EXACT"),
    ("overlay_forced_late", 86, "FORCED_FAILURE", "FORCED_LATE_FAILURE"),
    ("overlay_rollback", 87, "ROLLED_BACK", "INJECTED_INSTALL_FAILURE_ROLLED_BACK"),
    ("overlay_first", 0, "PASS", "UPGRADED_TO_SUPERSEDING_OVERLAY"),
    ("overlay_second", 0, "PASS", "ALREADY_INSTALLED_EXACT"),
    ("stateb_forced_late", 86, "FORCED_FAILURE", "FORCED_LATE_FAILURE"),
    ("stateb_rollback", 87, "ROLLED_BACK", "INJECTED_POST_EXCHANGE_FAILURE_ROLLED_BACK"),
    ("stateb_first", 0, "PASS", "TRANSITIONED_TO_STATE_B_EXACT"),
    ("stateb_second", 0, "PASS", "ALREADY_STATE_B_EXACT"),
    ("stateb_publication_exact", 0, "PASS", "PUBLISHED_STATE_B_EXACT"),
    ("attack_missing_h1", 2, "REJECT", "EXPECTED_STAGE1_COMMIT_MISSING"),
    ("attack_wrong_h1", 2, "REJECT", "ROUTE_STAGE1_COMMIT_MISMATCH"),
    ("attack_uppercase_h1", 2, "REJECT", "EXPECTED_STAGE1_COMMIT_INVALID"),
    ("attack_route_commit_full_reclose", 2, "REJECT", "ROUTE_STAGE1_COMMIT_MISMATCH"),
    ("attack_paper_manifest_reclose", 2, "REJECT", "FINAL_RUNTIME_REJECT"),
    ("attack_writer_manifest_seal_reclose", 2, "REJECT", "PUBLICATION_SEAL_SHA256_MISMATCH"),
    ("attack_auditor_manifest_seal_reclose", 2, "REJECT", "PUBLICATION_SEAL_SHA256_MISMATCH"),
    ("attack_state_a_b_mixed", 2, "REJECT", "STATE_A_PROVENANCE_DRIFT"),
    ("governance_missing_seal", 2, "REJECT", "EXPECTED_PUBLICATION_SEAL_SHA256_MISSING"),
    ("governance_wrong_seal", 2, "REJECT", "PUBLICATION_SEAL_SHA256_MISMATCH"),
    ("governance_uppercase_seal", 2, "REJECT", "EXPECTED_PUBLICATION_SEAL_SHA256_INVALID"),
]
HEX64 = re.compile(r"[0-9a-f]{64}\Z")
HEX40 = re.compile(r"[0-9a-f]{40}\Z")


class AuditFailure(Exception):
    def __init__(self, code: str, **details: Any) -> None:
        super().__init__(code)
        self.code = code
        self.details = details


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       separators=(",", ": "), allow_nan=False) + "\n").encode("ascii")


def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def strict(left: Any, right: Any) -> bool:
    if type(left) is not type(right):
        return False
    if type(left) is dict:
        return set(left) == set(right) and all(strict(left[key], right[key]) for key in left)
    if type(left) is list:
        return len(left) == len(right) and all(strict(a, b) for a, b in zip(left, right))
    return left == right


def sha_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def sha_file(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def safe_relative(value: Any) -> bool:
    if type(value) is not str or not value or "\\" in value:
        return False
    pure = PurePosixPath(value)
    return not pure.is_absolute() and all(part not in {"", ".", ".."} for part in pure.parts)


def emit(status: str, code: str, payload: dict[str, Any], exit_code: int) -> int:
    sys.stdout.buffer.write(canonical({
        "payload": {"code": code, **payload},
        "schema": "paper44-stateb-publication-audit-v2",
        "status": status,
    }))
    return exit_code


def validate_seal_anchor(value: Any) -> str:
    if value is None:
        raise AuditFailure("EXPECTED_PUBLICATION_SEAL_SHA256_MISSING")
    if type(value) is not str or HEX64.fullmatch(value) is None:
        raise AuditFailure("EXPECTED_PUBLICATION_SEAL_SHA256_INVALID")
    return value


def validate_stage1_commit(value: Any, required: bool) -> str | None:
    if value is None:
        if required:
            raise AuditFailure("EXPECTED_STAGE1_COMMIT_MISSING")
        return None
    if type(value) is not str or HEX40.fullmatch(value) is None or value == "0" * 40:
        raise AuditFailure("EXPECTED_STAGE1_COMMIT_INVALID")
    return value


def secure_root(root: Path, code: str) -> Path:
    if not root.is_absolute() or root.is_symlink() or not root.is_dir():
        raise AuditFailure(code)
    try:
        if root.resolve(strict=True) != root:
            raise AuditFailure(code)
    except OSError as error:
        raise AuditFailure(code) from error
    if stat.S_IMODE(os.lstat(root).st_mode) != 0o755:
        raise AuditFailure(code, path=".")
    return root


def scan(root: Path) -> dict[str, os.stat_result]:
    rows: dict[str, os.stat_result] = {}
    for path in root.rglob("*"):
        relative = path.relative_to(root).as_posix()
        metadata = os.lstat(path)
        if any(part == "__pycache__" or part.endswith((".pyc", ".pyo"))
               for part in PurePosixPath(relative).parts):
            raise AuditFailure("CACHE_FORBIDDEN", path=relative)
        if stat.S_ISLNK(metadata.st_mode):
            raise AuditFailure("SYMLINK_FORBIDDEN", path=relative)
        if not (stat.S_ISREG(metadata.st_mode) or stat.S_ISDIR(metadata.st_mode)):
            raise AuditFailure("NONREGULAR_FORBIDDEN", path=relative)
        rows[relative] = metadata
    return rows


def load_canonical(path: Path) -> tuple[dict[str, Any], bytes]:
    raw = path.read_bytes()
    value = json.loads(raw.decode("ascii"), object_pairs_hook=unique)
    if type(value) is not dict or raw != canonical(value):
        raise ValueError("noncanonical JSON")
    return value, raw


def parse_manifest(raw: bytes) -> dict[str, str]:
    try:
        text = raw.decode("ascii")
    except UnicodeDecodeError as error:
        raise AuditFailure("WRITER_MANIFEST_TAMPER") from error
    if not text.endswith("\n") or "\r" in text:
        raise AuditFailure("WRITER_MANIFEST_TAMPER")
    result: dict[str, str] = {}
    order: list[str] = []
    for line in text.splitlines():
        if len(line) < 67 or line[64:66] != "  " or HEX64.fullmatch(line[:64]) is None:
            raise AuditFailure("WRITER_MANIFEST_TAMPER")
        relative = line[66:]
        if not safe_relative(relative) or relative in {WRITER_MANIFEST, PUBLICATION_SEAL} \
                or relative in result:
            raise AuditFailure("WRITER_MANIFEST_TAMPER")
        result[relative] = line[:64]
        order.append(relative)
    if not result or order != sorted(order):
        raise AuditFailure("WRITER_MANIFEST_TAMPER")
    return result


def parent_directories(paths: set[str]) -> set[str]:
    result: set[str] = set()
    for relative in paths:
        parent = PurePosixPath(relative).parent
        while parent.as_posix() != ".":
            result.add(parent.as_posix())
            parent = parent.parent
    return result


def validate_contract(source: Path) -> dict[str, Any]:
    try:
        contract, _ = load_canonical(source / BRIDGE_CONTRACT)
    except Exception as error:
        raise AuditFailure("BRIDGE_CONTRACT_INVALID") from error
    expected = {
        "candidate_id": CANDIDATE_ID,
        "external_anchors": {
            "publication_seal_sha256": {
                "format": "lowercase_hex64", "required_before_seal_parse": True,
                "value_embedded": False,
            },
            "stage1_commit": {
                "format": "lowercase_nonzero_hex40",
                "required_for_state_B": True,
                "route_fields": ["code_commit", "source_commit",
                                 "source_lock.code_commit"],
                "value_embedded": False,
            },
        },
        "legacy_core": {
            "preoutput_seal_sha256": LEGACY_PREOUTPUT_SEAL_SHA256,
            "state_A_final_tree_sha256": LEGACY_STATE_A_TREE_SHA256,
            "static_manifest_entry_count": 58,
            "static_manifest_sha256": LEGACY_STATIC_MANIFEST_SHA256,
        },
        "output_states": {
            "A": {
                "legacy_semantics_preserved": True,
                "paper_manifest_present": False,
                "route_commit_values": ["NONE", "PREAUTHORITY_NO_COMMIT", "NONE"],
            },
            "B": {
                "direct_legacy_integrity_FINAL_required": True,
                "paper_manifest_domain":
                    "full_published_root_including_exact_writer_overlay_excluding_PREOUTPUT_STATIC_SEAL_and_manifest_self",
                "paper_manifest_present": True,
                "seal_embeds_final_tree_sha256": False,
                "seal_embeds_stage1_commit": False,
            },
        },
        "overlay": {
            "new_manifest_excludes": [WRITER_MANIFEST, PUBLICATION_SEAL],
            "predecessor_publication_seal_sha256": PREDECESSOR_PUBLICATION_SEAL_SHA256,
            "predecessor_writer_manifest_sha256": PREDECESSOR_WRITER_MANIFEST_SHA256,
            "superseding_overlay_allowed": True,
        },
        "physical_attacks": [
            "missing_stage1_commit", "wrong_stage1_commit", "uppercase_stage1_commit",
            "route_commit_full_reclose", "paper_manifest_reclose",
            "writer_manifest_and_seal_reclose", "auditor_manifest_and_seal_reclose",
            "state_A_state_B_mixed",
        ],
        "schema": "paper44-stateb-bridge-contract-v1",
        "status": "HOLD_FOR_INDEPENDENT_STATEB_PUBLICATION_AUDIT",
        "transactions": {
            "first_state_B_transition": "one_atomic_RENAME_EXCHANGE",
            "forced_late_failure_exit": 86,
            "idempotent_second_transition_replacements": 0,
            "overlay_upgrade": "bounded_predecessor_to_superseding_overlay_with_rollback",
            "rollback_exit": 87,
            "stage_all_before_target_write": True,
        },
    }
    if not strict(contract, expected):
        raise AuditFailure("BRIDGE_CONTRACT_INVALID")
    return contract


def expected_smoke_evidence(observed: bool) -> dict[str, Any]:
    cases = [
        {"expected_code": code, "expected_exit": rc, "id": label,
         "expected_status": status}
        for label, rc, status, code in SMOKE_CASES
    ]
    if observed:
        for case in cases:
            case["observed_outcome"] = "EXACT"
    return {
        "candidate_id": CANDIDATE_ID,
        "case_count": len(SMOKE_CASES),
        "cases": cases,
        "execution_observations_recorded": observed,
        "external_values_recorded": False,
        "legacy_frozen_auditor_disposition":
            "EXPECTED_REJECT_STATIC_TREE_MISMATCH_SUPERSESSION",
        "replay_contract": {
            "publication_seal_sha256": "supply_out_of_band",
            "stage1_commit": "supply_out_of_band_lowercase40",
        },
        "schema": "paper44-stateb-publication-smoke-evidence-v2",
        "status": "HOLD_FOR_INDEPENDENT_STATEB_PUBLICATION_AUDIT",
    }


def validate_smoke_evidence(source: Path, allow_checklist: bool) -> None:
    try:
        evidence, _ = load_canonical(source / PUBLICATION_EVIDENCE)
    except Exception as error:
        raise AuditFailure("SMOKE_EVIDENCE_INVALID") from error
    if strict(evidence, expected_smoke_evidence(True)):
        return
    if strict(evidence, expected_smoke_evidence(False)):
        if allow_checklist:
            return
        raise AuditFailure("UNEXECUTED_SMOKE_CHECKLIST_FORBIDDEN")
    raise AuditFailure("SMOKE_EVIDENCE_INVALID")


def expected_seal(source: Path, manifest_raw: bytes, manifest: dict[str, str]) -> dict[str, Any]:
    return {
        "bridge_code_paths": BRIDGE_CODE_PATHS,
        "bridge_contract_sha256": sha_file(source / BRIDGE_CONTRACT),
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
        "publication_smoke_evidence_sha256": sha_file(source / PUBLICATION_EVIDENCE),
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


def audit_source(source: Path, expected_anchor: str, expected_commit: str | None,
                 allow_combined: bool = False,
                 allow_checklist: bool = False) -> tuple[dict[str, str], dict[str, Any]]:
    source = secure_root(source, "UNSAFE_SOURCE_ROOT")
    actual = scan(source)
    for special in (WRITER_MANIFEST, PUBLICATION_SEAL):
        metadata = actual.get(special)
        if metadata is None or not stat.S_ISREG(metadata.st_mode):
            raise AuditFailure("SOURCE_OVERLAY_PARTIAL", path=special)
        if stat.S_IMODE(metadata.st_mode) != 0o644:
            raise AuditFailure("SOURCE_OVERLAY_MODE_DRIFT", path=special)
    anchor = validate_seal_anchor(expected_anchor)
    observed_anchor = sha_file(source / PUBLICATION_SEAL)
    if observed_anchor != anchor:
        raise AuditFailure("PUBLICATION_SEAL_SHA256_MISMATCH",
                           expected_sha256=anchor, observed_sha256=observed_anchor)
    try:
        seal, seal_raw = load_canonical(source / PUBLICATION_SEAL)
    except Exception as error:
        raise AuditFailure("PUBLICATION_SEAL_INVALID") from error
    if expected_commit is not None and expected_commit.encode("ascii") in seal_raw:
        raise AuditFailure("SEAL_EMBEDS_STAGE1_COMMIT")
    manifest_raw = (source / WRITER_MANIFEST).read_bytes()
    manifest = parse_manifest(manifest_raw)
    validate_contract(source)
    validate_smoke_evidence(source, allow_checklist)
    wanted_seal = expected_seal(source, manifest_raw, manifest)
    if not strict(seal, wanted_seal):
        raise AuditFailure("PUBLICATION_SEAL_INVALID")
    expected_files = set(manifest) | {WRITER_MANIFEST, PUBLICATION_SEAL}
    expected_dirs = parent_directories(expected_files)
    actual_files = {path for path, metadata in actual.items() if stat.S_ISREG(metadata.st_mode)}
    actual_dirs = {path for path, metadata in actual.items() if stat.S_ISDIR(metadata.st_mode)}
    if not allow_combined:
        missing = expected_files - actual_files
        extras = actual_files - expected_files
        if missing:
            raise AuditFailure("SOURCE_OVERLAY_PARTIAL", path=sorted(missing)[0])
        if extras:
            raise AuditFailure("SOURCE_CANDIDATE_EXTRA", path=sorted(extras)[0])
        if actual_dirs != expected_dirs:
            delta = (actual_dirs - expected_dirs) or (expected_dirs - actual_dirs)
            raise AuditFailure("SOURCE_CANDIDATE_EXTRA" if actual_dirs - expected_dirs
                               else "SOURCE_OVERLAY_PARTIAL", path=sorted(delta)[0])
    else:
        if not expected_files <= actual_files or not expected_dirs <= actual_dirs:
            delta = (expected_files - actual_files) or (expected_dirs - actual_dirs)
            raise AuditFailure("SOURCE_OVERLAY_PARTIAL", path=sorted(delta)[0])
    for relative in sorted(expected_dirs):
        if stat.S_IMODE(actual[relative].st_mode) != 0o755:
            raise AuditFailure("SOURCE_OVERLAY_MODE_DRIFT", path=relative)
    for relative, promised in manifest.items():
        if stat.S_IMODE(actual[relative].st_mode) != 0o644:
            raise AuditFailure("SOURCE_OVERLAY_MODE_DRIFT", path=relative)
        if sha_file(source / relative) != promised:
            raise AuditFailure("SOURCE_OVERLAY_BYTE_DRIFT", path=relative)
    for relative in BRIDGE_CODE_PATHS:
        if relative not in manifest:
            raise AuditFailure("BRIDGE_CODE_NOT_MANIFESTED", path=relative)
    if sha_file(source / "main.pdf") != FINAL_PDF_SHA256:
        raise AuditFailure("SOURCE_OVERLAY_BYTE_DRIFT", path="main.pdf")
    return manifest, seal


def legacy_static_rows(root: Path) -> list[dict[str, Any]]:
    manifest_path = root / "STATIC_TREE_MANIFEST.json"
    seal_path = root / "PREOUTPUT_STATIC_SEAL.json"
    if not manifest_path.is_file() or sha_file(manifest_path) != LEGACY_STATIC_MANIFEST_SHA256:
        raise AuditFailure("STATIC_MANIFEST_HASH_MISMATCH")
    if not seal_path.is_file() or sha_file(seal_path) != LEGACY_PREOUTPUT_SEAL_SHA256:
        raise AuditFailure("PREOUTPUT_SEAL_HASH_MISMATCH")
    if stat.S_IMODE(os.lstat(manifest_path).st_mode) != 0o644 \
            or stat.S_IMODE(os.lstat(seal_path).st_mode) != 0o644:
        raise AuditFailure("LEGACY_CORE_MODE_DRIFT")
    try:
        value, _ = load_canonical(manifest_path)
        rows = value["payload"]["rows"]
        valid = value["schema"] == "paper44-static-tree-manifest-v2" \
            and value["status"] == "SEALED" and value["payload"]["entry_count"] == 58 \
            and len(rows) == 58 and rows == sorted(rows, key=lambda row: row.get("path", ""))
    except Exception as error:
        raise AuditFailure("STATIC_MANIFEST_OBJECT_INVALID") from error
    if not valid:
        raise AuditFailure("STATIC_MANIFEST_OBJECT_INVALID")
    return rows


def verify_legacy_core(root: Path, actual: dict[str, os.stat_result],
                       rows: list[dict[str, Any]]) -> set[str]:
    paths = {"STATIC_TREE_MANIFEST.json", "PREOUTPUT_STATIC_SEAL.json"}
    for row in rows:
        relative = row.get("path")
        if not safe_relative(relative) or relative not in actual:
            raise AuditFailure("LEGACY_CORE_PARTIAL", path=relative)
        metadata = actual[relative]
        if stat.S_IMODE(metadata.st_mode) != int(row.get("mode", "-1"), 8):
            raise AuditFailure("LEGACY_CORE_MODE_DRIFT", path=relative)
        if row.get("kind") == "directory":
            if not stat.S_ISDIR(metadata.st_mode) or set(row) != {"kind", "mode", "path"}:
                raise AuditFailure("LEGACY_CORE_TYPE_DRIFT", path=relative)
        elif row.get("kind") == "regular":
            if not stat.S_ISREG(metadata.st_mode) \
                    or set(row) != {"kind", "mode", "path", "sha256"}:
                raise AuditFailure("LEGACY_CORE_TYPE_DRIFT", path=relative)
            if sha_file(root / relative) != row["sha256"]:
                raise AuditFailure("LEGACY_CORE_BYTE_DRIFT", path=relative)
        else:
            raise AuditFailure("STATIC_MANIFEST_OBJECT_INVALID")
        paths.add(relative)
    return paths


def verify_overlay(root: Path, source: Path, source_manifest: dict[str, str],
                   source_seal: dict[str, Any], expected_anchor: str,
                   actual: dict[str, os.stat_result]) -> tuple[str, set[str]]:
    target_manifest = root / WRITER_MANIFEST
    target_seal = root / PUBLICATION_SEAL
    if not target_manifest.is_file() or not target_seal.is_file():
        raise AuditFailure("OVERLAY_PARTIAL")
    manifest_hash = sha_file(target_manifest)
    seal_hash = sha_file(target_seal)
    if seal_hash == expected_anchor:
        if manifest_hash != source_seal["writer_manifest_sha256"] \
                or target_manifest.read_bytes() != (source / WRITER_MANIFEST).read_bytes() \
                or target_seal.read_bytes() != (source / PUBLICATION_SEAL).read_bytes():
            raise AuditFailure("WRITER_MANIFEST_TAMPER")
        manifest = source_manifest
        kind = "SUPERSEDING"
    elif seal_hash == PREDECESSOR_PUBLICATION_SEAL_SHA256 \
            and manifest_hash == PREDECESSOR_WRITER_MANIFEST_SHA256:
        manifest = parse_manifest(target_manifest.read_bytes())
        kind = "PREDECESSOR"
    else:
        raise AuditFailure("OVERLAY_SEAL_UNRECOGNIZED", observed_sha256=seal_hash)
    files = set(manifest) | {WRITER_MANIFEST, PUBLICATION_SEAL}
    directories = parent_directories(files)
    for relative in sorted(directories):
        metadata = actual.get(relative)
        if metadata is None or not stat.S_ISDIR(metadata.st_mode):
            raise AuditFailure("OVERLAY_PARTIAL", path=relative)
        if stat.S_IMODE(metadata.st_mode) != 0o755:
            raise AuditFailure("OVERLAY_MODE_DRIFT", path=relative)
    for relative in sorted(files):
        metadata = actual.get(relative)
        if metadata is None or not stat.S_ISREG(metadata.st_mode):
            raise AuditFailure("OVERLAY_PARTIAL", path=relative)
        if stat.S_IMODE(metadata.st_mode) != 0o644:
            raise AuditFailure("OVERLAY_MODE_DRIFT", path=relative)
        if relative in manifest and sha_file(root / relative) != manifest[relative]:
            raise AuditFailure("OVERLAY_BYTE_DRIFT", path=relative)
    return kind, files | directories


def invoke_json(command: list[str], cwd: Path) -> tuple[int, bytes, bytes, dict[str, Any] | None]:
    environment = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "PYTHONPATH": "",
                   "PYTHONDONTWRITEBYTECODE": "1", "TZ": "UTC", "LC_ALL": "C", "LANG": "C"}
    process = subprocess.run(command, cwd=cwd, env=environment, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, check=False)
    value: dict[str, Any] | None = None
    try:
        parsed = json.loads(process.stdout.decode("ascii"), object_pairs_hook=unique)
        if type(parsed) is dict and process.stdout == canonical(parsed):
            value = parsed
    except Exception:
        pass
    return process.returncode, process.stdout, process.stderr, value


def route_state(root: Path) -> tuple[str, dict[str, Any]]:
    route_path = root / "outputs/evaluations/route_a/SD-C46/2026-08-18.yaml"
    try:
        route, _ = load_canonical(route_path)
        state = route["authority_integration"]["state"]
    except Exception as error:
        raise AuditFailure("OUTPUT_STATE_MIXED") from error
    if state not in {"A", "B"}:
        raise AuditFailure("OUTPUT_STATE_MIXED")
    return state, route


def verify_output_namespace(root: Path, actual: dict[str, os.stat_result], state: str) -> set[str]:
    files = FILES_A + (["PAPER_MANIFEST.sha256"] if state == "B" else [])
    paths = set(OUTPUT_DIRS) | {"outputs/" + relative for relative in files}
    for relative in OUTPUT_DIRS:
        metadata = actual.get(relative)
        if metadata is None or not stat.S_ISDIR(metadata.st_mode) \
                or stat.S_IMODE(metadata.st_mode) != 0o755:
            raise AuditFailure("OUTPUT_STATE_MIXED", path=relative)
    for relative in files:
        full = "outputs/" + relative
        metadata = actual.get(full)
        if metadata is None or not stat.S_ISREG(metadata.st_mode) \
                or stat.S_IMODE(metadata.st_mode) != 0o644:
            raise AuditFailure("OUTPUT_STATE_MIXED", path=full)
    forbidden = root / "outputs/PAPER_MANIFEST.sha256"
    if state == "A" and (forbidden.exists() or forbidden.is_symlink()):
        raise AuditFailure("OUTPUT_STATE_MIXED", path="outputs/PAPER_MANIFEST.sha256")
    return paths


def verify_route_provenance(route: dict[str, Any], state: str,
                            expected_commit: str | None) -> None:
    try:
        integration = route["authority_integration"]
        values = [route["code_commit"], route["source_commit"],
                  route["source_lock"]["code_commit"]]
        if state == "A":
            expected = ["NONE", "PREAUTHORITY_NO_COMMIT", "NONE"]
            valid = strict(values, expected) and strict(integration, {
                "authority_writes": 0, "git_operations": 0,
                "paper_manifest_present": False, "state": "A"})
        else:
            valid = strict(values, [expected_commit, expected_commit, expected_commit]) \
                and strict(integration, {"authority_writes": 0, "git_operations": 0,
                                         "paper_manifest_present": True, "state": "B"})
    except (KeyError, TypeError):
        valid = False
    if not valid:
        raise AuditFailure("ROUTE_STAGE1_COMMIT_MISMATCH" if state == "B"
                           else "STATE_A_PROVENANCE_DRIFT")


def direct_runtime(root: Path, state: str, expected_commit: str | None) -> dict[str, Any]:
    command = [sys.executable, "-I", "-B", str(root / "code/integration/audit_integrity.py"),
               "--root", str(root), "--output-root", str(root / "outputs"),
               "--state", state, "--phase", "FINAL"]
    if state == "B":
        command += ["--commit", str(expected_commit)]
    rc, stdout, stderr, value = invoke_json(command, root.parent)
    if rc != 0 or stderr or value is None \
            or value.get("schema") != "paper44-runtime-final-verification-v1" \
            or value.get("status") != "PASS" \
            or value.get("payload", {}).get("state") != state \
            or value.get("payload", {}).get("phase") != "FINAL":
        raise AuditFailure("FINAL_RUNTIME_REJECT")
    if state == "A" and value["payload"].get("final_tree_sha256") != LEGACY_STATE_A_TREE_SHA256:
        raise AuditFailure("STATE_A_SEMANTICS_DRIFT")
    return {"final_tree_sha256": value["payload"]["final_tree_sha256"],
            "verification_sha256": sha_bytes(stdout)}


def verify_paper_manifest_overlay(root: Path, overlay_paths: set[str]) -> int:
    path = root / "outputs/PAPER_MANIFEST.sha256"
    try:
        lines = path.read_text(encoding="ascii").splitlines()
        if lines[0] != "paper44-state-b-manifest-v2 exclude=PREOUTPUT_STATIC_SEAL.json,PAPER_MANIFEST.sha256":
            raise ValueError("header")
        rows = [line.split(" ", 3)[3] for line in lines[1:]]
    except Exception as error:
        raise AuditFailure("STATE_B_PAPER_MANIFEST_INVALID") from error
    required = {path for path in overlay_paths if not path.startswith("outputs/")}
    if not required <= set(rows) or "PREOUTPUT_STATIC_SEAL.json" in rows \
            or "outputs/PAPER_MANIFEST.sha256" in rows or rows != sorted(rows):
        raise AuditFailure("STATE_B_PAPER_MANIFEST_INVALID")
    return len(rows)


def legacy_disposition(root: Path) -> str:
    command = [sys.executable, "-I", "-B", str(root / "external_auditor/frozen_auditor.py"),
               "--root", str(root)]
    rc, _stdout, stderr, value = invoke_json(command, root.parent)
    if stderr or rc != 2 or value is None or value.get("status") != "REJECT" \
            or value.get("schema") != "paper44-frozen-external-audit-v2" \
            or value.get("payload", {}).get("code") != "STATIC_TREE_MISMATCH":
        raise AuditFailure("LEGACY_AUDITOR_UNEXPECTED_DISPOSITION")
    return "EXPECTED_REJECT_STATIC_TREE_MISMATCH_SUPERSESSION"


def audit_target(root: Path, source: Path, source_manifest: dict[str, str],
                 source_seal: dict[str, Any], expected_anchor: str,
                 expected_commit: str | None, relocated: bool) -> dict[str, Any]:
    if relocated and not str(root).startswith("/tmp/"):
        raise AuditFailure("RELOCATED_MODE_OUTSIDE_TMP_FORBIDDEN")
    root = secure_root(root, "UNSAFE_ROOT")
    actual = scan(root)
    base_paths = verify_legacy_core(root, actual, legacy_static_rows(root))
    overlay_kind, overlay_paths = verify_overlay(
        root, source, source_manifest, source_seal, expected_anchor, actual)
    state, route = route_state(root)
    commit = validate_stage1_commit(expected_commit, required=state == "B")
    if overlay_kind == "PREDECESSOR" and state != "A":
        raise AuditFailure("PREDECESSOR_STATE_B_FORBIDDEN")
    verify_route_provenance(route, state, commit)
    output_paths = verify_output_namespace(root, actual, state)
    expected_paths = base_paths | overlay_paths | output_paths
    actual_paths = set(actual)
    extras = actual_paths - expected_paths
    missing = expected_paths - actual_paths
    if missing:
        raise AuditFailure("ROOT_PARTIAL", path=sorted(missing)[0])
    if extras:
        raise AuditFailure("ROOT_EXTRA", path=sorted(extras)[0])
    runtime = direct_runtime(root, state, commit)
    manifest_rows = 0
    if state == "B":
        manifest_rows = verify_paper_manifest_overlay(root, overlay_paths)
    legacy = legacy_disposition(root)
    if overlay_kind == "PREDECESSOR":
        named_state = "PREDECESSOR_STATE_A_EXACT"
    else:
        named_state = "PUBLISHED_STATE_A_EXACT" if state == "A" else "PUBLISHED_STATE_B_EXACT"
    return {
        "legacy_frozen_auditor_disposition": legacy,
        "overlay_kind": overlay_kind,
        "paper_manifest_entry_count": manifest_rows,
        "runtime": runtime,
        "stage1_commit_bound_three_times": state == "B",
        "state": named_state,
        "writer_manifest_sha256": source_seal["writer_manifest_sha256"]
            if overlay_kind == "SUPERSEDING" else PREDECESSOR_WRITER_MANIFEST_SHA256,
    }


def main() -> int:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--root", required=True)
    parser.add_argument("--overlay-source")
    parser.add_argument("--expected-publication-seal-sha256")
    parser.add_argument("--expected-stage1-commit")
    parser.add_argument("--source-only", action="store_true")
    parser.add_argument("--relocated-disposable", action="store_true")
    parser.add_argument("--allow-unexecuted-checklist", action="store_true")
    arguments = parser.parse_args()
    try:
        anchor = validate_seal_anchor(arguments.expected_publication_seal_sha256)
        commit = validate_stage1_commit(arguments.expected_stage1_commit, required=False)
        root = Path(arguments.root)
        source = Path(arguments.overlay_source) \
            if arguments.overlay_source else root
        if arguments.allow_unexecuted_checklist and not arguments.relocated_disposable:
            raise AuditFailure("CHECKLIST_OVERRIDE_REQUIRES_RELOCATED_DISPOSABLE")
        combined = not arguments.source_only and source == root
        manifest, seal = audit_source(source, anchor, commit, allow_combined=combined,
                                      allow_checklist=arguments.allow_unexecuted_checklist)
        if arguments.source_only:
            return emit("PASS", "SOURCE_OVERLAY_EXACT", {
                "overlay_file_count": len(manifest) + 2,
                "state": "SOURCE_OVERLAY_EXACT",
                "writer_manifest_sha256": seal["writer_manifest_sha256"],
            }, 0)
        payload = audit_target(root, source, manifest, seal, anchor, commit,
                               arguments.relocated_disposable)
        return emit("PASS", payload["state"], payload, 0)
    except AuditFailure as error:
        return emit("REJECT", error.code, error.details, 2)
    except Exception as error:
        return emit("REJECT", "AUDIT_EXCEPTION", {"exception_type": type(error).__name__}, 2)


if __name__ == "__main__":
    raise SystemExit(main())
