#!/usr/bin/env python3
"""Freeze the exact Round-10 P29--P33 Stage-4.5 Round-2 audit inputs.

This authorizes and records audit-only work.  It never edits a manuscript,
bibliography, scientific tree, result, Route state, or canonical PDF.
"""

from __future__ import annotations

import hashlib
import json
import os
import stat
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STAMP = "2026-09-04T12:52:00Z"
EVENT = "BATCH_ROUND10_STAGE4_5_ROUND2_AUTHOR_EVENT_20260904.txt"
RECORD = "BATCH_ROUND10_STAGE4_5_ROUND2_AUTHORIZATION_RECORD.md"
LOCK = "BATCH_ROUND10_STAGE4_5_ROUND2_INPUT_LOCK.json"
RECEIPT = "BATCH_ROUND10_STAGE4_5_ROUND2_AUTHORIZATION_RECEIPT.json"

PAPERS = {
    29: {
        "slug": "29-bianchi-ideal-owner-refinement",
        "draft": "notes/stage4_prime_revision_round3.tex",
        "prior": "notes/stage4_prime_revision_round2.tex",
        "blocks": "notes/stage4_prime_revision_round3.block-manifest.json",
        "bib": "notes/stage4_prime_references_round2.bib",
        "bundle": "notes/stage4_prime_revision_evidence_bundle_round3.json",
        "patch": "notes/stage4_prime_revision_patch_round3_exact_confirmation.json",
        "apply": "notes/stage4_prime_revision_round3.tex.apply-report.json",
        "build": "notes/stage4_prime_revision_round3_build_receipt.json",
        "source": [
            "notes/stage4_prime_source_finalization_round3.json",
            "notes/stage4_prime_source_finalization_round3_validation.json",
            "notes/stage4_prime_claim_passage_matrix_round3.json",
        ],
        "traceability": "notes/stage3_prime_round3_traceability.json",
        "prior_integrity": "notes/stage4_5_round1_integrity_report.json",
        "prior_passport": "notes/stage4_5_round1_material_passport.json",
        "route": "A0/A1 preparation; formal tuple UNASSIGNED; positive arithmetic A2=0; A3=0; A4=0; Route B uninvoked",
        "initial": "torsion-free level-(3) Gaussian Bianchi unit-speed geodesic flow; hyperbolic-arclength clock; primitive loxodromic inversion-paired owner; one literal nonzero Gaussian prime ideal",
    },
    30: {
        "slug": "30-three-disk-nonconstant-roof-determinant",
        "draft": "notes/stage4_prime_revision_round3.tex",
        "prior": "notes/stage4_prime_revision_round2.tex",
        "blocks": "notes/stage4_prime_revision_round3.block-manifest.json",
        "bib": "notes/stage4_prime_references_round2.bib",
        "bundle": "notes/stage4_prime_revision_evidence_bundle_round3.json",
        "patch": "notes/stage4_prime_revision_patch_round3_exact_confirmation.json",
        "apply": "notes/stage4_prime_revision_round3.tex.apply-report.json",
        "build": "notes/stage4_prime_revision_round3_build_receipt.json",
        "source": ["notes/stage4_prime_claim_passage_matrix_round2.json"],
        "traceability": "notes/stage3_prime_round2_traceability.json",
        "prior_integrity": "notes/stage4_5_round1_integrity_report.json",
        "prior_passport": "notes/stage4_5_round1_material_passport.json",
        "route": "A0_FAIL / A2_NOT_ELIGIBLE; formal tuple UNASSIGNED; A3=0; A4=0; Route B uninvoked",
        "initial": "no-eclipse equilateral three-disk flow at d=6a; Euclidean free-flight clock; primitive cyclic collision-word owner; physical roof distinct from unit-roof control",
    },
    31: {
        "slug": "31-level11-conjugacy-owner-ledger",
        "draft": "notes/stage4_prime_revision_round3.tex",
        "prior": "notes/stage4_prime_revision_round2.tex",
        "blocks": "notes/stage4_prime_revision_round3.block-manifest.json",
        "bib": "notes/stage4_prime_references_round2.bib",
        "bundle": "notes/stage4_prime_revision_evidence_bundle_round3.json",
        "patch": "notes/stage4_prime_revision_patch_round3_exact_confirmation.json",
        "apply": "notes/stage4_prime_revision_round3.tex.apply-report.json",
        "build": "notes/stage4_prime_revision_round3_build_receipt.json",
        "source": ["notes/stage4_prime_method_passage_matrix_round2.json"],
        "traceability": "notes/stage3_prime_round2_traceability.json",
        "prior_integrity": "notes/stage4_5_round1_integrity_report.json",
        "prior_passport": "notes/stage4_5_round1_material_passport.json",
        "route": "A1-only preparation; formal tuple UNASSIGNED; positive arithmetic A2=0; A3=0; A4=0; Route B uninvoked",
        "initial": "fixed positive time change of the Gamma_0(11) geodesic flow; oriented primitive owner; inverse separate; powers are repetitions; Hecke degree distinct",
    },
    32: {
        "slug": "32-homology-cover-renormalization-uniformity",
        "draft": "notes/stage4_prime_revision_round3.tex",
        "prior": "notes/stage4_prime_revision_round2.tex",
        "blocks": "notes/stage4_prime_revision_round3.block-manifest.json",
        "bib": "notes/stage4_prime_references_round2.bib",
        "bundle": "notes/stage4_prime_revision_evidence_bundle_round3.json",
        "patch": "notes/stage4_prime_revision_patch_round3_exact_confirmation.json",
        "apply": "notes/stage4_prime_revision_round3.tex.apply-report.json",
        "build": "notes/stage4_prime_revision_round3_build_receipt.json",
        "source": [
            "notes/stage4_prime_source_finalization_round3.json",
            "notes/stage4_prime_source_finalization_round3_validation.json",
            "notes/stage4_prime_claim_passage_matrix_round3.json",
        ],
        "traceability": "notes/stage3_prime_round3_traceability.json",
        "prior_integrity": "notes/stage4_5_round1_integrity_report.json",
        "prior_passport": "notes/stage4_5_round1_material_passport.json",
        "route": "generic A1--A2 preparation with arithmetic A0 unavailable; formal tuple UNASSIGNED; positive arithmetic A2=0; A3=0; A4=0; Route B uninvoked",
        "initial": "unit-speed genus-two geodesic flow; pure homology tower; oriented primitive owner with inverse separate; full-content scope; clock 1/N; logarithmic normalization 1/N^3",
    },
    33: {
        "slug": "33-bolza-control-matched-census",
        "draft": "notes/stage4_prime_revision_round2.tex",
        "prior": "notes/stage4_revision_round1.tex",
        "blocks": "notes/stage4_prime_revision_round2.block-manifest.json",
        "bib": "paper/references.bib",
        "bundle": "notes/stage4_prime_revision_evidence_bundle_round2.json",
        "patch": "notes/stage4_prime_revision_patch_round6_exact_confirmation.json",
        "apply": "notes/stage4_prime_revision_round2.tex.apply-report.json",
        "build": "notes/stage4_prime_revision_round2_build_receipt.json",
        "source": [
            "notes/stage4_prime_round5_source_identity_replay_receipt.json",
            "notes/stage4_prime_round5_source_use_locator_final.json",
            "notes/stage4_prime_round5_artifact_inventory_final.json",
            "notes/stage4_prime_round6_bibliography_append_receipt.json",
        ],
        "traceability": "notes/stage3_prime_round5_traceability.json",
        "prior_integrity": "notes/stage4_integrity_pass_receipt.json",
        "prior_passport": None,
        "route": "A1 preparation with formal A0 prohibited/confounded; formal tuple UNASSIGNED; positive arithmetic A2=0; A3=0; A4=0; Route B uninvoked",
        "initial": "unit-speed Bolza geodesic flow with separately typed matched control; presentation-specific owner semantics; frozen generator/cutoff objects; target-blind no-retuning",
    },
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def encoded(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def reject_unsafe_path(path: Path) -> None:
    """Reject escape paths and symlinks in every existing path component."""
    try:
        relative = path.relative_to(ROOT)
    except ValueError as exc:
        raise RuntimeError(f"path escapes repository root: {path}") from exc
    current = ROOT
    for component in relative.parts:
        if component in {"", ".", ".."}:
            raise RuntimeError(f"unsafe path component in {relative}")
        current = current / component
        if current.is_symlink():
            raise RuntimeError(f"symlink is forbidden in frozen input path: {relative}")


def binding(relative: str) -> dict[str, object]:
    path = ROOT / relative
    reject_unsafe_path(path)
    try:
        mode = path.lstat().st_mode
    except FileNotFoundError as exc:
        raise FileNotFoundError(relative) from exc
    if not stat.S_ISREG(mode):
        raise FileNotFoundError(relative)
    return {"path": relative, "sha256": sha(path), "bytes": path.stat().st_size}


def tree_binding(relative: str) -> dict[str, object]:
    root = ROOT / relative
    reject_unsafe_path(root)
    try:
        root_mode = root.lstat().st_mode
    except FileNotFoundError as exc:
        raise FileNotFoundError(relative) from exc
    if not stat.S_ISDIR(root_mode):
        raise RuntimeError(f"frozen tree root is not a directory: {relative}")
    rows = []
    entries = sorted(root.rglob("*"))
    for path in entries:
        reject_unsafe_path(path)
        mode = path.lstat().st_mode
        if stat.S_ISLNK(mode):
            raise RuntimeError(f"symlink is forbidden in frozen tree: {path.relative_to(ROOT)}")
        if not stat.S_ISREG(mode):
            continue
        rel = path.relative_to(ROOT).as_posix()
        rows.append({"path": rel, "sha256": sha(path), "bytes": path.stat().st_size})
    digest_input = "".join(f"{row['sha256']}  {row['path']}\n" for row in rows).encode()
    return {
        "path": relative,
        "sha256": hashlib.sha256(digest_input).hexdigest(),
        "files": rows,
    }


def write_exclusive(path: Path, data: bytes) -> tuple[int, int, str]:
    reject_unsafe_path(path)
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    fd = os.open(path, flags, 0o644)
    try:
        view = memoryview(data)
        offset = 0
        while offset < len(view):
            written = os.write(fd, view[offset:])
            if written <= 0:
                raise OSError(f"short write while publishing {path.name}")
            offset += written
        os.fsync(fd)
    finally:
        os.close(fd)
    created = path.lstat()
    return created.st_dev, created.st_ino, hashlib.sha256(data).hexdigest()


def remove_if_exact(path: Path, identity: tuple[int, int, str]) -> None:
    """Rollback only the exact regular file created by this invocation."""
    expected_dev, expected_ino, expected_sha = identity
    try:
        observed = path.lstat()
    except FileNotFoundError:
        return
    if (
        stat.S_ISREG(observed.st_mode)
        and observed.st_dev == expected_dev
        and observed.st_ino == expected_ino
        and sha(path) == expected_sha
    ):
        path.unlink()


def publish_pair_exclusive(lock: object, receipt: object) -> None:
    """No-clobber publish with exact-file rollback if the second write fails."""
    lock_path = ROOT / LOCK
    receipt_path = ROOT / RECEIPT
    reject_unsafe_path(lock_path)
    reject_unsafe_path(receipt_path)
    if os.path.lexists(lock_path) or os.path.lexists(receipt_path):
        raise FileExistsError("lock/receipt publication refused because at least one target already exists")

    lock_data = encoded(lock)
    receipt_data = encoded(receipt)
    lock_identity: tuple[int, int, str] | None = None
    try:
        lock_identity = write_exclusive(lock_path, lock_data)
        write_exclusive(receipt_path, receipt_data)
    except BaseException:
        if lock_identity is not None:
            remove_if_exact(lock_path, lock_identity)
        raise

    directory_fd = os.open(ROOT, os.O_RDONLY)
    try:
        os.fsync(directory_fd)
    finally:
        os.close(directory_fd)


def main() -> int:
    common = [
        EVENT,
        RECORD,
        "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_EXACT_CONFIRMATION_MANDATORY_CHECKPOINT.md",
        "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_EXACT_CONFIRMATION_COMPLETION_REPORT.md",
        "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_EXACT_CONFIRMATION_COMPLETION_RECEIPT.json",
        "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_EXACT_CONFIRMATION_FINAL_AUDIT.json",
        "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_EXACT_CONFIRMATION_FINAL_EMISSION_MANIFEST.json",
        "skills/route-a-evaluator.md",
        "skills/route-b-evaluator.md",
    ]
    paper_rows = []
    for paper_id, cfg in PAPERS.items():
        base = f"papers/{cfg['slug']}"
        protected = [
            binding(f"{base}/paper/manuscript.tex"),
            binding(f"{base}/paper/paper.pdf"),
            binding(f"{base}/paper/references.bib"),
        ]
        audit_inputs = [
            binding(f"{base}/{cfg['draft']}"),
            binding(f"{base}/{cfg['bib']}"),
            binding(f"{base}/{cfg['bundle']}"),
            binding(f"{base}/{cfg['prior']}"),
            binding(f"{base}/{cfg['blocks']}"),
            binding(f"{base}/{cfg['patch']}"),
            binding(f"{base}/{cfg['apply']}"),
            binding(f"{base}/{cfg['build']}"),
            binding(f"{base}/notes/stage2_5_material_passport.json"),
            binding(f"{base}/notes/stage1_prestart_brief.md"),
            binding(f"{base}/notes/stage4_route_crosswalk.md"),
            binding(f"{base}/{cfg['traceability']}"),
            binding(f"{base}/{cfg['prior_integrity']}"),
        ]
        if cfg["prior_passport"]:
            audit_inputs.append(
                {
                    **binding(f"{base}/{cfg['prior_passport']}"),
                    "role": "LATEST_PASSPORT_SEED",
                }
            )
        audit_inputs.extend(binding(f"{base}/{path}") for path in cfg["source"])
        paper_rows.append(
            {
                "paper_id": f"P{paper_id}",
                "paper_slug": cfg["slug"],
                "audit_draft": audit_inputs[0],
                "audit_bibliography": audit_inputs[1],
                "revision_evidence_bundle": audit_inputs[2],
                "immediate_prior_draft": audit_inputs[3],
                "output_block_manifest": audit_inputs[4],
                "prior_integrity_evidence": {
                    **binding(f"{base}/{cfg['prior_integrity']}"),
                    "role": "COMPARISON_ONLY_NON_AUTHORIZING_PRIOR_INTEGRITY_EVIDENCE",
                },
                "prior_stage4_5_passport": (
                    {**binding(f"{base}/{cfg['prior_passport']}"), "role": "LATEST_PASSPORT_SEED"}
                    if cfg["prior_passport"] else {"path": None, "role": "ABSENT_NOT_RECONSTRUCTED"}
                ),
                "audit_inputs": audit_inputs,
                "protected_canonical_files": protected,
                "science_trees": [
                    tree_binding(f"{base}/code"),
                    tree_binding(f"{base}/experiments"),
                    tree_binding(f"{base}/results"),
                ],
                "frozen_route_state": cfg["route"],
                "frozen_initial_system": cfg["initial"],
            }
        )

    lock = {
        "schema_version": "round10-stage4.5-round2-input-lock/1.0",
        "batch_id": "round10-papers29-33-stage4.5-round2",
        "locked_at": STAMP,
        "authority_bindings": [binding(path) for path in common],
        "ars_protocol": {
            "package_version": "ars-codex/0.1.26",
            "integrity_protocol_sha256": hashlib.sha256(
                Path("/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/skills/academic-research-suite/ars/academic-pipeline/references/integrity_review_protocol.md").read_bytes()
            ).hexdigest(),
        },
        "scope": {
            "operation": "fresh_mode2_final_integrity_audit",
            "papers": [29, 30, 31, 32, 33],
            "silent_repair": False,
            "manuscript_or_bibliography_mutation": False,
            "scientific_execution_or_result_refresh": False,
            "route_or_initial_system_mutation": False,
            "canonical_promotion": False,
            "stage5_or_stage6_entry": False,
            "readme_or_status_mutation": False,
            "git_synchronization": False,
            "failure_action": "record_and_stop_without_fix",
        },
        "papers": paper_rows,
        "aggregate_route_boundary": {
            "formal_route_a_tuples": "0/5",
            "positive_arithmetic_A2": "0/5",
            "A3": "0/5",
            "A4": "0/5",
            "route_b_invocations": "0/5",
        },
        "citation_style": "natbib[numbers,sort&compress] + plainnat numeric",
    }
    lock_data = encoded(lock)
    lock_binding = {
        "path": LOCK,
        "sha256": hashlib.sha256(lock_data).hexdigest(),
        "bytes": len(lock_data),
    }
    receipt = {
        "schema_version": "round10-stage4.5-round2-authorization-receipt/1.0",
        "recorded_at": STAMP,
        "status": "AUTHORIZED_AUDIT_ONLY",
        "author_event": binding(EVENT),
        "authorization_record": binding(RECORD),
        "input_lock": lock_binding,
        "controlling_checkpoint": binding("BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_EXACT_CONFIRMATION_MANDATORY_CHECKPOINT.md"),
        "authorized_papers": ["P29", "P30", "P31", "P32", "P33"],
        "authorized_action": "fresh Stage 4.5 Mode-2 integrity audit from scratch",
        "repairs_authorized": False,
        "stage5_authorized": False,
    }
    publish_pair_exclusive(lock, receipt)
    print(json.dumps({"lock": binding(LOCK), "receipt": binding(RECEIPT)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
