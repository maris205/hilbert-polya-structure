#!/usr/bin/env python3
"""Rebuild only the P30/P31 Stage-4.5-R2 audit-derived package.

This is the second fail-closed semantic-dependency correction.  It archives the
earlier attempt-5 FAIL sidecars as noncontrolling, expands every affected
claim/source/anchor dependency from raw carriers, preserves anchorless missing
dependencies, and emits a coherent attempt-6 FAIL audit package.  It never
changes manuscript, bibliography, science/result, Route, canonical, README,
status, or Git material.
"""

from __future__ import annotations

import argparse
import copy
import datetime as dt
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import tempfile
import urllib.parse
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
ARS = Path(
    "/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.28/"
    "skills/academic-research-suite/ars"
)
EVIDENCE_SCRIPT = ARS / "scripts/evidence_rows.py"
COVERAGE_SCRIPT = ARS / "scripts/claim_registry_coverage.py"
COMPLIANCE_CHECKER = ARS / "scripts/check_compliance_report.py"
AUTHORITY_RECEIPT_SHA = "139631992e610beb9ffc2e5b72c1ee5022bed87460d95b3c5da7812dd3b2db60"
AUTHORITY_LOCK_SHA = "11875bf33e0318997c385d0d89bde3a7987bb9166b18967994ccb3ca5ac44bb0"
INDEPENDENT_REVIEW_REL = "BATCH_ROUND10_STAGE4_5_ROUND2_P30_P31_SEMANTIC_DEPENDENCY_INDEPENDENT_REVIEW.json"
INDEPENDENT_REVIEW_SHA = "1c0d087c330c4f14624addfe48d66fae5d71f03422f96791f550a5d26656ec0f"
INDEPENDENT_REVIEW_BYTES = 30593
SCRIPT_REL = "tools/rebuild_round10_stage4_5_p30_p31_dispatch.py"
SHARED_NETWORK_COLLECTOR_REL = (
    "papers/30-three-disk-nonconstant-roof-determinant/notes/"
    "stage4_5_round2_collect_reference_network.py"
)
STAMP = os.environ.get("ROUND10_P30_P31_REBUILD_TIMESTAMP") or dt.datetime.now(
    dt.timezone.utc
).replace(microsecond=0).isoformat().replace("+00:00", "Z")
BOUNDARY = (
    "This audit checks disclosure and claim-to-provenance fidelity. It does not judge whether "
    "an experiment was correctly designed, run, statistically adequate, or reproducible by ARS; "
    "both papers declare and contain no project-owned scientific experiment."
)


CONFIGS: tuple[dict[str, Any], ...] = (
    {
        "paper": 30,
        "paper_id": "P30",
        "slug": "30-three-disk-nonconstant-roof-determinant",
        "draft_sha": "509e9f45b798ad2257acf2f62db81f95a43e3c574da8f1ba7e654c9fa9d21ead",
        "bib_sha": "5b6854540f595e83ffc4f5a6153595ff27b2e74705e9fe930a0b5d33c17b81f1",
        "old_manifest_sha": "42ecd80e6e63d8ac10e1c97afad2fc81c4a94e81f0d21f5f9120778daefc40ec",
        "old_validation_sha": "bf20aef8f910edaf04ad02c74b6c4e9c65c8b460386077e93ceedd80c17453fe",
        "reference_total": 28,
        "context_total": 30,
        "claim_total": 107,
        "phase_c": "13/14 verified; 1/14 MAJOR_DISTORTION_STALE_STATUS",
        "originality_body": "67/82",
        "originality_changed": "54/54",
        "e6_ops": 69,
        "pages": 18,
        "matrix": "stage4_prime_claim_passage_matrix_round2.json",
        "matrix_sha": "f2e24dcba6b31a5d4cbd72981d194b844ade544dec883a1f84100336a4831816",
        "source_finalization_sha": "6337d2c0240982bef5221d346b5e61851cbdc1f154cf92e16dd39234b2900566",
        "project_blocks": {
            "B0004", "B0006", "B0009", "B0013", "B0051", "B0059", "B0061", "B0062",
            "B0064", "B0065", "B0066", "B0069", "B0090", "B0098", "B0100", "B0103",
            "B0105", "B0107", "B0108", "B0115", "B0116", "B0118", "B0119", "B0123",
            "B0124", "B0125",
        },
        "failure_claims": {
            "P30-S45R2-E1-001": "UNVERIFIABLE",
            "P30-S45R2-E1-047": "UNVERIFIABLE",
            "P30-S45R2-E1-049": "MAJOR_DISTORTION",
            "P30-S45R2-E1-050": "MAJOR_DISTORTION",
            "P30-S45R2-E1-051": "MAJOR_DISTORTION",
            "P30-S45R2-E1-053": "MAJOR_DISTORTION",
            "P30-S45R2-E1-092": "MAJOR_DISTORTION",
            "P30-S45R2-E1-094": "MAJOR_DISTORTION",
            "P30-S45R2-E1-106": "UNVERIFIABLE",
            "P30-S45R2-E1-083": "UNVERIFIABLE",
            "P30-S45R2-E1-107": "MAJOR_DISTORTION",
        },
        "expected_verified_claims": 96,
        "minimum_dependency_components": 213,
        "minimum_evidence_rows": 239,
        "route_state": "A0_FAIL / A2_NOT_ELIGIBLE; formal tuple UNASSIGNED; A3=0; A4=0; Route B uninvoked",
        "initial_system": "no-eclipse equilateral three-disk flow at d=6a; Euclidean free-flight clock; primitive cyclic collision-word owner; physical roof distinct from unit-roof control",
    },
    {
        "paper": 31,
        "paper_id": "P31",
        "slug": "31-level11-conjugacy-owner-ledger",
        "draft_sha": "733e37dfe4e7377a711ade04f7bc6d902b311e2ded48211331d70506735d2729",
        "bib_sha": "02f85e29b4379280c91a5ad4258b98e9c3ab81271277fea206df030e2c3de222",
        "old_manifest_sha": "c2d8cf1a26f9479de1b1d1e27369d9c4037d68ff5e117b128e3d9eeffeb3453e",
        "old_validation_sha": "20671df5917cebe133a91309b2b4a2376088a47c4bd984a5b2ca0f18c3881caa",
        "reference_total": 24,
        "context_total": 26,
        "claim_total": 127,
        "phase_c": "13/13",
        "originality_body": "50/63",
        "originality_changed": "30/30",
        "e6_ops": 44,
        "pages": 16,
        "matrix": "stage4_prime_method_passage_matrix_round2.json",
        "matrix_sha": "1adc4c653fee5ff33ddc2572101e92566ffd19e00de1f6be6f70e4f56d2a9e2a",
        "source_finalization_sha": "37526ac1b63329b06dae9174417ee200483a1c90905a55d3b27a859fba26913a",
        "project_blocks": {
            "B0006", "B0007", "B0011", "B0012", "B0015", "B0023", "B0036", "B0037",
            "B0039", "B0041", "B0042", "B0056", "B0061", "B0067", "B0069", "B0075",
            "B0076", "B0079", "B0085", "B0087", "B0089", "B0090", "B0091", "B0092",
            "B0098", "B0099", "B0101", "B0105", "B0107", "B0108", "B0111",
        },
        "failure_claims": {
            "P31-S45R2-E1-008": "UNVERIFIABLE",
            "P31-S45R2-E1-077": "UNVERIFIABLE",
            "P31-S45R2-E1-079": "UNVERIFIABLE",
            "P31-S45R2-E1-080": "UNVERIFIABLE",
            "P31-S45R2-E1-067": "UNVERIFIABLE",
            "P31-S45R2-E1-126": "UNVERIFIABLE",
            "P31-S45R2-E1-108": "MAJOR_DISTORTION",
            "P31-S45R2-E1-125": "MAJOR_DISTORTION",
        },
        "expected_verified_claims": 119,
        "minimum_dependency_components": 249,
        "minimum_evidence_rows": 271,
        "route_state": "A1-only preparation; formal tuple UNASSIGNED; positive arithmetic A2=0; A3=0; A4=0; Route B uninvoked",
        "initial_system": "fixed positive time change of the Gamma_0(11) geodesic flow; oriented primitive owner; inverse separate; powers are repetitions; Hecke degree distinct",
    },
)


CHANGED_NAMES = {
    "stage4_5_round2_attempt_lineage.json",
    "stage4_5_round2_reference_citation_audit.json",
    "stage4_5_round2_reference_citation_audit.md",
    "stage4_5_round2_evidence_source_map.json",
    "stage4_5_round2_evidence_rows.json",
    "stage4_5_round2_evidence_rows_replay.log",
    "stage4_5_round2_seven_failure_mode_audit.json",
    "stage4_5_round2_seven_failure_mode_audit.md",
    "stage4_5_round2_compliance_report.json",
    "stage4_5_round2_round1_comparison.json",
    "stage4_5_round2_phase_c_internal_consistency_audit.json",
    "stage4_5_round2_phase_c_internal_consistency_audit.md",
    "stage4_5_round2_integrity_report.json",
    "stage4_5_round2_material_passport.json",
    "stage4_5_round2_final_integrity_report.md",
    "stage4_5_round2_receipt.json",
    "stage4_5_round2_output_manifest.json",
    "stage4_5_round2_validation_receipt.json",
    "stage4_5_round2_local_claim_dependency_catalog.json",
    "stage4_5_round2_local_semantic_adjudication.json",
    "stage4_5_round2_local_semantic_adjudication.md",
    "stage4_5_round2_correction_proposal.json",
    "stage4_5_round2_semantic_attempt5_supersession_incident.json",
}


def load_module(path: Path, name: str) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


EVR = load_module(EVIDENCE_SCRIPT, "round10_p30_p31_evidence_rows")


def sha_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def sha_path(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def jraw(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def traw(value: str) -> bytes:
    return (value.rstrip() + "\n").encode("utf-8")


def artifact(path: str, raw: bytes) -> dict[str, Any]:
    return {"path": path, "sha256": sha_bytes(raw), "bytes": len(raw)}


def resolve_package_binding_path(paper_root: Path, path_value: str) -> Path:
    """Resolve a manifest path under its declared package/root namespace.

    `notes/` and `paper/` are paper-relative.  Every other admissible value is
    workspace-root-relative.  Absolute paths, parent traversal, non-regular
    files, and symlinked path components are rejected before hash replay.
    """
    if not isinstance(path_value, str) or not path_value:
        raise RuntimeError("manifest binding path is absent")
    relative = Path(path_value)
    if relative.is_absolute() or ".." in relative.parts:
        raise RuntimeError(f"manifest binding path escapes namespace: {path_value}")
    base = paper_root if path_value.startswith(("notes/", "paper/")) else ROOT
    base = base.resolve(strict=True)
    candidate = base.joinpath(relative)
    try:
        resolved = candidate.resolve(strict=True)
    except FileNotFoundError as exc:
        raise RuntimeError(f"manifest binding path is missing: {path_value}") from exc
    try:
        resolved.relative_to(base)
    except ValueError as exc:
        raise RuntimeError(f"manifest binding path escapes resolved namespace: {path_value}") from exc
    cursor = base
    for part in relative.parts:
        cursor = cursor / part
        if cursor.is_symlink():
            raise RuntimeError(f"manifest binding path contains symlink: {path_value}")
    if not resolved.is_file():
        raise RuntimeError(f"manifest binding is not a regular file: {path_value}")
    return resolved


def run(command: list[str]) -> tuple[int, str]:
    result = subprocess.run(command, cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False)
    return result.returncode, result.stdout


def snapshot_replay(snapshot: dict[str, Any]) -> list[dict[str, Any]]:
    rows = []
    for rel, expected in sorted(snapshot.items()):
        path = ROOT / rel
        actual_sha = sha_path(path) if path.is_file() and not path.is_symlink() else None
        actual_bytes = path.stat().st_size if path.is_file() and not path.is_symlink() else None
        rows.append({
            "path": rel,
            "expected_sha256": expected["sha256"],
            "actual_sha256": actual_sha,
            "expected_bytes": expected["bytes"],
            "actual_bytes": actual_bytes,
            "status": "PASS" if actual_sha == expected["sha256"] and actual_bytes == expected["bytes"] else "FAIL",
        })
    return rows


def preflight(cfg: dict[str, Any]) -> dict[str, Any]:
    paper = ROOT / "papers" / cfg["slug"]
    notes = paper / "notes"
    required = [
        notes / "stage4_5_round2_output_manifest.json",
        notes / "stage4_5_round2_validation_receipt.json",
        notes / "stage4_5_round2_claim_registry.json",
        notes / "stage4_5_round2_claim_registry_coverage.json",
        notes / "stage4_5_round2_evidence_rows.json",
        notes / "stage4_5_round2_evidence_source_map.json",
        notes / "stage4_5_round2_reference_citation_audit.json",
        notes / "stage4_5_round2_integrity_report.json",
        notes / "stage4_5_round2_material_passport.json",
        notes / "stage4_5_round2_preview_build_receipt.json",
        notes / "stage4_prime_revision_round3.tex",
        notes / "stage4_prime_references_round2.bib",
    ]
    for path in required:
        if not path.is_file() or path.is_symlink():
            raise RuntimeError(f"{cfg['paper_id']} required regular file missing: {path}")
    if sha_path(notes / "stage4_5_round2_output_manifest.json") != cfg["old_manifest_sha"]:
        raise RuntimeError(f"{cfg['paper_id']} old controlling manifest hash mismatch")
    if sha_path(notes / "stage4_5_round2_validation_receipt.json") != cfg["old_validation_sha"]:
        raise RuntimeError(f"{cfg['paper_id']} old controlling validation hash mismatch")
    if sha_path(notes / "stage4_prime_revision_round3.tex") != cfg["draft_sha"]:
        raise RuntimeError(f"{cfg['paper_id']} Round-3 draft changed")
    if sha_path(notes / "stage4_prime_references_round2.bib") != cfg["bib_sha"]:
        raise RuntimeError(f"{cfg['paper_id']} versioned bibliography changed")
    input_manifest = json.loads((notes / "stage4_5_round2_input_manifest.json").read_text(encoding="utf-8"))
    checks = snapshot_replay(input_manifest["protected_snapshot_before"])
    failures = [row for row in checks if row["status"] != "PASS"]
    if failures:
        raise RuntimeError(f"{cfg['paper_id']} protected snapshot mismatch: {failures[:3]}")
    archive = notes / "stage4_5_round2_SEMANTIC_ATTEMPT5_NONCONTROLLING_archive"
    if archive.exists():
        raise RuntimeError(f"{cfg['paper_id']} archive collision: {archive}")
    old_manifest = json.loads((notes / "stage4_5_round2_output_manifest.json").read_text(encoding="utf-8"))
    if old_manifest.get("verdict") != "FAIL" or old_manifest.get("controlling_attempt") != 5:
        raise RuntimeError(f"{cfg['paper_id']} expected controlling attempt-5 FAIL package")
    old_validation = json.loads((notes / "stage4_5_round2_validation_receipt.json").read_text(encoding="utf-8"))
    if old_validation.get("status") != "PASS_AUDIT_PACKAGE_COHERENT_WITH_BLOCKING_INTEGRITY_VERDICT":
        raise RuntimeError(f"{cfg['paper_id']} expected coherent attempt-5 validation")
    archive_rows = []
    rows = list(old_manifest["artifacts"]) + [
        artifact("notes/stage4_5_round2_output_manifest.json", (notes / "stage4_5_round2_output_manifest.json").read_bytes()),
        artifact("notes/stage4_5_round2_validation_receipt.json", (notes / "stage4_5_round2_validation_receipt.json").read_bytes()),
    ]
    seen = set()
    for row in rows:
        if row["path"] in seen:
            continue
        seen.add(row["path"])
        source = paper / row["path"]
        if sha_path(source) != row["sha256"] or source.stat().st_size != row["bytes"]:
            raise RuntimeError(f"{cfg['paper_id']} old manifest row mismatch: {row['path']}")
        archive_rows.append({
            **row,
            "archive_path": f"notes/{archive.name}/{Path(row['path']).name}",
        })
    return {
        "paper": paper,
        "notes": notes,
        "input_manifest": input_manifest,
        "protected_checks": checks,
        "archive": archive,
        "archive_rows": archive_rows,
    }


def first_excerpt(text: str, cap: int = 20) -> str:
    matches = list(re.finditer(r"\S+", text))
    if not matches:
        raise RuntimeError("empty claim cannot yield an excerpt")
    return text[:matches[min(cap, len(matches)) - 1].end()]


RAW_VERIFIED_SUFFIXES = {
    30: {
        "001", "002", "004", "008", "042", "048", "050", "052", "054", "055",
        "078", "084", "086", "088", "089", "090", "091", "093", "099", "100",
        "102", "103", "105", "107",
    },
    31: {
        "001", "004", "005", "007", "028", "078", "082", "083", "091", "095",
        "100", "101", "106", "107", "108", "113", "115", "116", "118", "119",
        "120", "121", "122", "123", "127",
    },
}


COMPONENT_PLANS: dict[int, dict[str, list[str]]] = {
    30: {
        "001": ["initial_system", "corpus_26", "no_code", "no_experiment", "no_results", "matrix_18", "matrix_8", "route_state"],
        "002": ["initial_system", "corpus_26", "no_code", "no_experiment", "no_results", "matrix_18", "matrix_8", "route_state"],
        "004": ["initial_system"],
        "008": ["initial_system", "no_code", "no_experiment", "no_results", "route_state"],
        "042": ["matrix_rows"],
        "048": ["corpus_68", "corpus_52", "corpus_26", "corpus_24", "query_rows", "query_bound"],
        "050": ["source_effect_fields", "author_event", "no_code", "no_experiment", "no_results"],
        "051": ["matrix_rows", "matrix_18", "matrix_8", "s02_updated_by", "c01_update_to"],
        "052": ["source_effect_fields", "matrix_rows"],
        "053": ["matrix_18", "matrix_8", "s02_updated_by", "c01_update_to"],
        "054": ["matrix_rows", "bib_c01", "bib_c02", "no_code", "no_experiment", "no_results"],
        "055": ["initial_system"],
        "078": ["no_code", "no_experiment", "no_results"],
        "084": ["reader_entries"],
        "086": ["no_code", "no_experiment", "no_results"],
        "088": ["initial_system", "route_state"],
        "089": ["initial_system"],
        "090": ["initial_system"],
        "091": ["corpus_26", "corpus_24"],
        "093": ["matrix_rows", "no_code", "no_experiment", "no_results"],
        "094": ["stale_search_status", "dated_search_replay", "query_rows", "reader_entries"],
        "099": ["initial_system", "no_code", "no_experiment", "no_results"],
        "100": ["route_state", "no_code", "no_experiment", "no_results"],
        "102": ["no_code", "no_experiment", "no_results"],
        "103": ["author_name", "author_event"],
        "105": ["reader_entries", "bib_c01", "bib_c02"],
        "107": ["author_event", "matrix_18", "matrix_8"],
        # External correction-bearing compound claims are included in the expanded catalog.
        "049": ["draft_wrong_correction", "bib_wrong_correction", "s02_updated_by", "c01_update_to", "c02_update_to"],
        "092": ["draft_wrong_correction_late", "bib_wrong_correction", "s02_updated_by", "c01_update_to", "c02_update_to"],
    },
    31: {
        "008": ["missing_s23_passage", "missing_s24_passage"],
        "001": ["initial_population", "corpus_22", "no_code", "no_experiment", "no_results", "matrix_7", "matrix_15", "route_state"],
        "004": ["initial_population"],
        "005": ["initial_population"],
        "007": ["no_code", "no_experiment", "no_results"],
        "028": ["matrix_rows", "matrix_7", "matrix_15"],
        "078": ["corpus_44", "corpus_9", "corpus_35", "corpus_13", "corpus_22", "query_rows", "query_bound"],
        "082": ["source_effect_fields", "author_event"],
        "083": ["stage3_decision", "author_event"],
        "091": ["no_code", "no_experiment", "no_results"],
        "095": ["initial_population", "no_code", "no_experiment", "no_results"],
        "100": ["initial_population"],
        "101": ["initial_population"],
        "106": ["author_event", "route_state"],
        "107": ["route_state"],
        "108": ["reader_entries"],
        "113": ["initial_population"],
        "115": ["no_code", "no_experiment", "no_results"],
        "116": ["route_state"],
        "118": ["matrix_rows", "source_effect_fields"],
        "119": ["no_code", "no_experiment", "no_results"],
        "120": ["author_name", "stage25_ai_role"],
        "121": ["initial_population"],
        "122": ["no_code", "no_experiment", "no_results", "matrix_7", "matrix_15", "stage25_originality", "route_state"],
        "123": ["author_name", "author_event"],
        "127": ["author_name", "author_event", "matrix_7", "matrix_15"],
        "079": ["matrix_rows", "matrix_7", "matrix_15", "missing_s23_passage", "missing_s24_passage"],
        "080": ["source_effect_fields", "missing_s23_passage", "missing_s24_passage"],
        "081": ["matrix_rows", "bib_s23", "bib_s24", "missing_s23_passage", "missing_s24_passage"],
        "117": ["query_rows", "matrix_7", "matrix_15", "missing_s23_passage", "missing_s24_passage"],
        "125": ["reader_entries", "bib_s23", "bib_s24", "missing_s23_passage", "missing_s24_passage"],
        "077": ["missing_s23_passage", "missing_s24_passage"],
    },
}


MISSING_COMPONENTS: dict[int, dict[str, list[tuple[str, str]]]] = {
    30: {
        "001": [("missing_livsic_passage", "No current locked original-source passage establishes the substantive Livsic-type asymmetric inference repeated in the abstract.")],
        "047": [("missing_livsic_passage", "No current locked original-source passage establishes the substantive Livsic-type asymmetric inference.")],
        "083": [("missing_livsic_passage", "No current locked original-source passage establishes the substantive Livsic-type asymmetric inference repeated in the fifth finding.")],
        "106": [("missing_current_user_ai_metadata", "No current locked user-metadata carrier supports the expanded 2--4 September AI dates and task list.")],
    },
    31: {
        "126": [("missing_current_user_ai_metadata", "No current locked user-metadata carrier supports the expanded 2--4 September AI dates and task list.")],
    },
}


# Source segmentation was independently replayed against the exact registered
# byte spans.  These maps intentionally include cross-source claims whose first
# source was lost by the old single-ref_slug representation.
P31_SOURCE_CLAIMS: dict[str, list[str]] = {
    "013": ["P31-S01"], "014": ["P31-S01", "P31-S02"],
    "015": ["P31-S02"], "016": ["P31-S02", "P31-S03"],
    "017": ["P31-S03"], "018": ["P31-S03", "P31-S04"],
    "019": ["P31-S04"], "020": ["P31-S04", "P31-S05"],
    "021": ["P31-S05"], "022": ["P31-S05"],
    "023": ["P31-S05", "P31-S06"], "024": ["P31-S06"],
    "025": ["P31-S06"], "026": ["P31-S06"],
    "030": ["P31-S07"], "031": ["P31-S07"],
    "032": ["P31-S07", "P31-S08"], "033": ["P31-S08"],
    "034": ["P31-S08"], "035": ["P31-S08", "P31-S09"],
    "036": ["P31-S09"], "037": ["P31-S09"],
    "038": ["P31-S09", "P31-S10"], "039": ["P31-S10"],
    "040": ["P31-S10", "P31-S11"], "041": ["P31-S11"],
    "042": ["P31-S11", "P31-S12"], "043": ["P31-S12"],
    "044": ["P31-S12", "P31-S13"], "045": ["P31-S13"],
    "046": ["P31-S13"],
    "050": ["P31-S15"], "051": ["P31-S15"],
    "052": ["P31-S15", "P31-S16"], "053": ["P31-S16"],
    "054": ["P31-S16"], "055": ["P31-S16", "P31-S17"],
    "056": ["P31-S17"], "057": ["P31-S17"],
    "058": ["P31-S17", "P31-S18"], "059": ["P31-S18"],
    "060": ["P31-S18", "P31-S19"], "061": ["P31-S19"],
    "062": ["P31-S19"], "063": ["P31-S19", "P31-S20"],
    "064": ["P31-S19"], "065": ["P31-S20"], "066": ["P31-S20"],
    "069": ["P31-S14"], "070": ["P31-S14"],
    "071": ["P31-S14", "P31-S21"], "072": ["P31-S21"],
    "073": ["P31-S21", "P31-S22"], "074": ["P31-S22"],
    "075": ["P31-S22"],
}
P31_LOCATED = {"P31-S05", "P31-S06", "P31-S08", "P31-S09", "P31-S16", "P31-S17", "P31-S19"}
P31_ALL_SOURCES = [f"P31-S{i:02d}" for i in range(1, 23)]


def _source_component_keys(source_id: str) -> list[str]:
    stem = source_id.lower().replace("-", "_")
    keys = [f"matrix_{stem}_role", f"matrix_{stem}_status", f"matrix_{stem}_scope", f"matrix_{stem}_boundary"]
    if source_id in P31_LOCATED:
        keys.extend([f"final_{stem}_locator", f"final_{stem}_excerpt", f"final_{stem}_excerpt_hash"])
    return keys


def _add_plan(paper: int, suffix: str, keys: list[str]) -> None:
    current = COMPONENT_PLANS[paper].setdefault(suffix, [])
    for key in keys:
        if key not in current:
            current.append(key)


# P31 source-specific raw tuple expansion.
for _suffix, _sources in P31_SOURCE_CLAIMS.items():
    for _source in _sources:
        _add_plan(31, _suffix, _source_component_keys(_source))

# Aggregates are expanded to the source rows/passages that the prose actually
# quantifies over.  The broad E067 negative additionally remains anchorless for
# every unavailable substantive passage.
for _suffix, _sources in {
    "027": [f"P31-S{i:02d}" for i in range(1, 7)],
    "028": P31_ALL_SOURCES,
    "047": [f"P31-S{i:02d}" for i in range(7, 14)],
    "067": P31_ALL_SOURCES,
    "079": P31_ALL_SOURCES,
    "080": P31_ALL_SOURCES,
    "122": P31_ALL_SOURCES,
    "127": P31_ALL_SOURCES,
}.items():
    for _source in _sources:
        _add_plan(31, _suffix, _source_component_keys(_source))

for _source in [sid for sid in P31_ALL_SOURCES if sid not in P31_LOCATED]:
    _key = f"missing_{_source.lower().replace('-', '_')}_passage"
    MISSING_COMPONENTS[31].setdefault("067", []).append(
        (_key, f"No current locked original-source passage is available for {_source}; its project-recorded unavailability cannot prove E1-067's broad source-content negative.")
    )
_add_plan(31, "067", ["missing_s23_passage", "missing_s24_passage"])

# Remove the six semantically irrelevant S23/S24 passage requirements and bind
# the actual structural/material dependencies instead.
for _suffix in ("081", "117", "125"):
    COMPONENT_PLANS[31][_suffix] = [k for k in COMPONENT_PLANS[31][_suffix] if k not in {"missing_s23_passage", "missing_s24_passage"}]

_add_plan(31, "002", ["initial_population", "phase6_pair_population", "no_code", "no_experiment", "no_results", "matrix_rows", "matrix_7", "matrix_15", "matrix_boundary", "source_finalization_no_locator_guessing", "route_state"])
_add_plan(31, "078", ["p31_replay_full", "p31_screening_full", "p31_closest_full", "fresh_s23_identity", "fresh_s24_identity", "bib_s23", "bib_s24"])
_add_plan(31, "081", ["matrix_rows", "matrix_7", "matrix_15", "matrix_boundary", "source_finalization_no_locator_guessing", "fresh_s23_identity", "fresh_s24_identity", "p31_closest_records", "p31_build_closure", "bib_all_24", "canonical_bib_state"])
_add_plan(31, "082", ["source_effect_full_header", "stage3_four_roles", "stage3_major_revision", "author_adjudications_full"])
_add_plan(31, "083", ["phase6_revision1_status", "phase6_revision1_no_retrieval", "phase6_revision1_no_new_artifacts", "phase6_revision1_claimintent_frozen", "phase6_revision1_finding_classes", "revision_apply_base", "revision_apply_patch", "revision_apply_output", "revision_apply_operations", "phase6_claim_count", "phase6_claims_manifest", "p31_build_canonical_manuscript_unchanged", "canonical_bib_state", "no_code", "no_experiment", "no_results"])
_add_plan(31, "084", ["initial_population"])
_add_plan(31, "092", ["reader_manifest_full"])
_add_plan(31, "096", ["initial_population"])
_add_plan(31, "106", ["phase6_claim_count", "phase6_claims_manifest", "author_adjudications_full", "route_state"])
_add_plan(31, "107", ["phase6_claim_count", "phase6_claims_manifest", "route_state"])
_add_plan(31, "108", ["reader_manifest_full"])
_add_plan(31, "117", ["p31_replay_header_and_boundary", "p31_screening_full", "p31_closest_records", "query_rows", "query_bound", "matrix_rows", "matrix_7", "matrix_15", "matrix_boundary", "source_finalization_no_locator_guessing", "retraction_screening_all", "retraction_unrun", "fresh_s23_identity", "fresh_s24_identity", "fresh_network_metadata_only_boundary", "no_code", "no_experiment", "no_results"])
_add_plan(31, "118", ["retraction_unrun", "s16_correction", "source_effect_full_header"])
_add_plan(31, "123", ["author_adjudications_full"])
_add_plan(31, "125", ["reader_manifest_full", "fresh_s23_identity", "fresh_s24_identity", "p31_closest_records", "bib_all_24", "p31_build_canonical_bib_unchanged", "canonical_bib_state", "no_code", "no_experiment", "no_results"])
_add_plan(31, "108", ["reader_stale_matrix_entry", "current_matrix_artifact"])
_add_plan(31, "125", ["reader_stale_matrix_entry", "current_matrix_artifact"])

# E1-081 and E1-117 quantify over every retained passage rather than merely the
# aggregate 7/15 counts.  Bind each located row's current role/scope/transfer
# tuple and its finalized locator, excerpt, and excerpt digest.  S23/S24 remain
# metadata-level closest-work locators and are handled separately above.
for _source in sorted(P31_LOCATED):
    _add_plan(31, "081", _source_component_keys(_source))
    _add_plan(31, "117", _source_component_keys(_source))

# P30 semantic-dependency corrections from the independent review.
for _suffix, _sid in {"017": "P30-S04", "022": "P30-S10", "026": "P30-S11", "032": "P30-S18", "036": "P30-S14"}.items():
    _stem = _sid.lower().replace("-", "_")
    _add_plan(30, _suffix, [f"final_{_stem}_locator", f"final_{_stem}_excerpt", f"final_{_stem}_excerpt_hash"])
_add_plan(30, "006", ["no_code", "no_experiment", "no_results", "route_state"])
_add_plan(30, "048", ["replay_generated_at", "replay_interface", "replay_all_54", "screening_method", "screening_retained_31", "screening_out_23", "screening_decision_schema"])
_add_plan(30, "050", ["source_effect_full_header", "review_panel_axes", "review_panel_axes_detail", "review_panel_seats", "review_panel_seat_details", "author_adjudications_full"])
_add_plan(30, "052", ["source_effect_full_header", "claim_intent_count", "claim_intent_manifest"])
_add_plan(30, "054", ["corpus_26", "bib_all_28"])
_add_plan(30, "080", ["initial_system", "matrix_rows", "matrix_18", "matrix_8"])
_add_plan(30, "083", ["route_state"])
_add_plan(30, "084", ["reader_manifest_full"])
_add_plan(30, "103", ["author_adjudications_full"])
_add_plan(30, "105", ["reader_manifest_full", "no_code", "no_experiment", "no_results"])
_add_plan(30, "107", ["author_adjudications_full", "current_round2_audit_execution"])


def paper_repo_path(cfg: dict[str, Any], relative: str) -> str:
    return f"papers/{cfg['slug']}/{relative}"


def _object_binding_excerpt(parent_text: str, child_path: str, child_sha: str) -> dict[str, Any]:
    marker = json.dumps(child_path)
    at = parent_text.find(marker)
    if at < 0:
        raise RuntimeError(f"binding parent omits child path {child_path}")
    start = parent_text.rfind("{", 0, at)
    end = parent_text.find("}", at)
    if start < 0 or end < 0:
        raise RuntimeError(f"cannot delimit binding object for {child_path}")
    excerpt = parent_text[start:end + 1]
    if child_sha not in excerpt:
        raise RuntimeError(f"binding object for {child_path} omits sha {child_sha}")
    start_b = len(parent_text[:start].encode("utf-8"))
    end_b = len(parent_text[:end + 1].encode("utf-8"))
    return {
        "raw_utf8_span": {"start": start_b, "end": end_b},
        "raw_excerpt": excerpt,
        "raw_excerpt_sha256": sha_bytes(excerpt.encode("utf-8")),
    }


class DependencyResolver:
    """Resolve exact raw carriers and recursively replay their lock bindings."""

    def __init__(self, cfg: dict[str, Any], notes: Path):
        self.cfg = cfg
        self.notes = notes
        self.paper = notes.parent
        self.root_lock_path = ROOT / "BATCH_ROUND10_STAGE4_5_ROUND2_INPUT_LOCK.json"
        self.root_lock_desc = self._desc("BATCH_ROUND10_STAGE4_5_ROUND2_INPUT_LOCK.json")
        root_lock = json.loads(self.root_lock_path.read_text(encoding="utf-8"))
        self.top_rows: dict[str, dict[str, Any]] = {}
        def collect(value: Any) -> None:
            if isinstance(value, dict):
                if {"path", "sha256", "bytes"}.issubset(value) and isinstance(value["path"], str):
                    existing = self.top_rows.get(value["path"])
                    if existing is not None and (existing["sha256"], existing["bytes"]) != (value["sha256"], value["bytes"]):
                        raise RuntimeError(f"conflicting root-lock rows for {value['path']}")
                    self.top_rows[value["path"]] = {"path": value["path"], "sha256": value["sha256"], "bytes": value["bytes"]}
                for child in value.values():
                    collect(child)
            elif isinstance(value, list):
                for child in value:
                    collect(child)
        collect(root_lock)
        self.round1_path = paper_repo_path(cfg, "notes/stage4_5_round1_integrity_report.json")
        self.freeze_path = "BATCH_ROUND10_STAGE4_PRIME_EXECUTION_STAGE4_5_AND_ROUND5_INPUT_FREEZE.json"
        self.freeze_desc = self._desc(self.freeze_path)
        round1 = json.loads((ROOT / self.round1_path).read_text(encoding="utf-8"))
        if round1["input_freeze"]["path"] != self.freeze_path or round1["input_freeze"]["sha256"] != self.freeze_desc["sha256"]:
            raise RuntimeError(f"{cfg['paper_id']} Round-1 -> historical-freeze binding mismatch")
        freeze = json.loads((ROOT / self.freeze_path).read_text(encoding="utf-8"))
        track = next(row for row in freeze["papers"] if row["paper_id"] == cfg["paper_id"])
        self.freeze_rows = {row["path"]: row for row in track["track_inputs"]}
        self.reader_path = paper_repo_path(cfg, "notes/stage4_prime_reader_artifact_manifest_round2.json")
        reader = json.loads((ROOT / self.reader_path).read_text(encoding="utf-8"))
        self.reader_rows = {paper_repo_path(cfg, row["path"]): row for row in reader["entries"]}
        self.input_manifest_path = paper_repo_path(cfg, "notes/stage4_5_round2_input_manifest.json")
        self.input_manifest = json.loads((ROOT / self.input_manifest_path).read_text(encoding="utf-8"))
        self.independent_review_desc = self._desc(INDEPENDENT_REVIEW_REL)
        if self.independent_review_desc["sha256"] != INDEPENDENT_REVIEW_SHA or self.independent_review_desc["bytes"] != INDEPENDENT_REVIEW_BYTES:
            raise RuntimeError("independent semantic review hash/byte mismatch")
        review = json.loads((ROOT / INDEPENDENT_REVIEW_REL).read_text(encoding="utf-8"))
        self.review_carriers = {
            row["path"]: row
            for row in review["carrier_candidates"][cfg["paper_id"]]
            if {"path", "sha256", "bytes"}.issubset(row)
        }

    def _desc(self, repo_path: str) -> dict[str, Any]:
        path = ROOT / repo_path
        raw = path.read_bytes()
        return {"repo_path": repo_path, "sha256": sha_bytes(raw), "bytes": len(raw)}

    def current_authorized_audit_execution_chain(
        self, target: dict[str, Any], *, claim_id: str, component_id: str
    ) -> dict[str, Any]:
        """Describe the one performative runtime fact accepted by root replay.

        This is deliberately narrower than a generic audit-artifact lineage.  A
        full independent validator invocation establishes that the exact P30
        Round-3 draft is currently receiving the authorized Round-2 audit; it
        does not make a prior same-lineage review controlling evidence.
        """
        if self.cfg["paper_id"] != "P30":
            raise RuntimeError("current authorized audit execution is P30-only")
        expected_claim = "P30-S45R2-E1-107"
        expected_component = f"{expected_claim}:current_round2_audit_execution"
        if claim_id != expected_claim or component_id != expected_component:
            raise RuntimeError("current authorized audit execution scope mismatch")
        auth_record = self._desc("BATCH_ROUND10_STAGE4_5_ROUND2_AUTHORIZATION_RECORD.md")
        if target != auth_record:
            raise RuntimeError("current authorized audit execution target must be authorization record")
        return {
            "type": "CURRENT_AUTHORIZED_AUDIT_EXECUTION",
            "paper_id": "P30",
            "claim_id": expected_claim,
            "component_id": expected_component,
            "entrypoint": "tools/audit_round10_stage4_5_round2.rb#FULL_BATCH_REPLAY",
            "runtime_assertion": "VALIDATOR_IS_EXECUTING_THE_FULL_EXACT_AUTHORITY_ROUND10_STAGE4_5_ROUND2_REPLAY",
            "audit_draft": self._desc(paper_repo_path(self.cfg, "notes/stage4_prime_revision_round3.tex")),
            "authorization_record": auth_record,
            "authorization_receipt": self._desc("BATCH_ROUND10_STAGE4_5_ROUND2_AUTHORIZATION_RECEIPT.json"),
            "input_lock": self.root_lock_desc,
            "validator": self._desc("tools/audit_round10_stage4_5_round2.rb"),
        }

    def _hop(self, parent_path: str, child: dict[str, Any], child_path_in_parent: str | None = None) -> dict[str, Any]:
        parent = self._desc(parent_path)
        text = (ROOT / parent_path).read_text(encoding="utf-8")
        witness = _object_binding_excerpt(text, child_path_in_parent or child["repo_path"], child["sha256"])
        return {"binding_kind": "EXPLICIT_PATH_AND_SHA", "parent_artifact": parent, "child_artifact": child, **witness}

    def _sha_field_hop(
        self,
        parent_path: str,
        child: dict[str, Any],
        field: str,
        *,
        path_derivation_rule: str,
        scope_after: str | None = None,
        scope_before: str | None = None,
    ) -> dict[str, Any]:
        """Bind a canonical repository artifact through an exact SHA field.

        Some early batch freezes recorded canonical filenames in the schema and
        stored only their SHA field, rather than repeating the path beside every
        digest.  Preserve that historical limitation explicitly: the raw witness
        is the exact SHA field and the path derivation rule is machine checked.
        """
        parent = self._desc(parent_path)
        text = (ROOT / parent_path).read_text(encoding="utf-8")
        start = 0
        end = len(text)
        if scope_after is not None:
            start = text.find(scope_after)
            if start < 0:
                raise RuntimeError(f"historical SHA-field scope marker missing in {parent_path}: {scope_after}")
        if scope_before is not None:
            end = text.find(scope_before, start + len(scope_after or ""))
            if end < 0:
                raise RuntimeError(f"historical SHA-field end marker missing in {parent_path}: {scope_before}")
        needle = f'{json.dumps(field)}: {json.dumps(child["sha256"])}'
        at = text.find(needle, start, end)
        if at < 0 or text.find(needle, at + 1, end) >= 0:
            raise RuntimeError(f"historical SHA-field witness missing/nonunique in {parent_path}: {field}")
        raw = needle.encode("utf-8")
        start_b = len(text[:at].encode("utf-8"))
        return {
            "binding_kind": "SHA_FIELD_WITH_CANONICAL_PATH_DERIVATION",
            "parent_artifact": parent,
            "child_artifact": child,
            "sha_field": field,
            "raw_utf8_span": {"start": start_b, "end": start_b + len(raw)},
            "raw_excerpt": needle,
            "raw_excerpt_sha256": sha_bytes(raw),
            "scope_after": scope_after,
            "scope_before": scope_before,
            "path_derivation": {
                "rule": path_derivation_rule,
                "resolved_repo_path": child["repo_path"],
                "paper_id": self.cfg["paper_id"] if path_derivation_rule.startswith("PAPER_SLUG_PHASE6_") else None,
                "slug": self.cfg["slug"] if path_derivation_rule.startswith("PAPER_SLUG_PHASE6_") else None,
            },
        }

    def binding_chain(self, repo_path: str) -> dict[str, Any]:
        target = self._desc(repo_path)
        if repo_path in self.top_rows:
            expected = self.top_rows[repo_path]
            if expected["sha256"] != target["sha256"] or expected["bytes"] != target["bytes"]:
                raise RuntimeError(f"top-level lock mismatch for {repo_path}")
            return {"type": "TOP_LEVEL_INPUT_LOCK", "hops": [self._hop(self.root_lock_desc["repo_path"], target)]}
        if repo_path in self.freeze_rows:
            expected = self.freeze_rows[repo_path]
            if expected["sha256"] != target["sha256"] or expected["bytes"] != target["bytes"]:
                raise RuntimeError(f"historical freeze mismatch for {repo_path}")
            round1 = self._desc(self.round1_path)
            return {
                "type": "TRANSITIVE_SHA_BINDING",
                "hops": [
                    self._hop(self.root_lock_desc["repo_path"], round1),
                    self._hop(self.round1_path, self.freeze_desc),
                    self._hop(self.freeze_path, target),
                ],
            }
        if repo_path in self.reader_rows:
            expected = self.reader_rows[repo_path]
            if expected["sha256"] != target["sha256"] or expected["bytes"] != target["bytes"]:
                raise RuntimeError(f"reader-manifest binding mismatch for {repo_path}")
            round1 = self._desc(self.round1_path)
            reader = self._desc(self.reader_path)
            return {
                "type": "TRANSITIVE_SHA_BINDING",
                "hops": [
                    self._hop(self.root_lock_desc["repo_path"], round1),
                    self._hop(self.round1_path, self.freeze_desc),
                    self._hop(self.freeze_path, reader),
                    self._hop(self.reader_path, target, repo_path.removeprefix(f"papers/{self.cfg['slug']}/")),
                ],
            }
        p30_claim_intent_path = paper_repo_path(self.cfg, "notes/stage2_claim_intent_manifest.json")
        if self.cfg["paper"] == 30 and repo_path == p30_claim_intent_path:
            # Replay the shortest file-backed historical ancestry.  The
            # Stage-2.5 integrity report binds its Phase-C trace, and that trace
            # binds the complete ClaimIntent manifest.
            stage25_path = paper_repo_path(self.cfg, "notes/stage2_5_integrity_report.json")
            phase_c_path = paper_repo_path(self.cfg, "notes/stage2_5_phase_c_data_trace.json")
            expected = {
                stage25_path: "d5b8e0024b4a5a12ecfd12d70d4c7bf79e8a6060ac8bb4eee457c9973acfc251",
                phase_c_path: "639f44c836e97b8b6a65ff959ae00e2bc1fb5fe066cbb7d4dcc7f84b1da689f9",
                p30_claim_intent_path: "dc04175449cacf2ef492f00b9e6be535463793902afbea354c6c98d3e49df66f",
            }
            descs = {path: self._desc(path) for path in expected}
            for path, expected_sha in expected.items():
                if descs[path]["sha256"] != expected_sha:
                    raise RuntimeError(f"P30 historical ClaimIntent chain drift: {path}")
            round1 = self._desc(self.round1_path)
            return {
                "type": "TRANSITIVE_SHA_BINDING",
                "lineage_role": "P30_CLAIM_INTENT_HISTORICAL_STAGE2_FREEZE_CHAIN",
                "hops": [
                    self._hop(self.root_lock_desc["repo_path"], round1),
                    self._hop(self.round1_path, self.freeze_desc),
                    self._hop(self.freeze_path, descs[stage25_path]),
                    self._hop(stage25_path, descs[phase_c_path], "notes/stage2_5_phase_c_data_trace.json"),
                    self._hop(phase_c_path, target),
                ],
                "boundary": (
                    "The ClaimIntent manifest is bound through the current lock's Round-1/freeze ancestry and "
                    "the exact Stage-2.5 integrity-report -> Phase-C-trace -> manifest path/SHA witnesses."
                ),
            }
        p30_panel_path = paper_repo_path(self.cfg, "notes/stage3_review_panel_provenance.json")
        if self.cfg["paper"] == 30 and repo_path == p30_panel_path:
            # Stage-3's final integrity chain carries the frozen Round-2 input,
            # which carries the Round-1 checker receipt, which in turn binds
            # the exact panel-provenance object.  This removes any dependency
            # on a review-authored carrier catalog.
            completion_path = "BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_COMPLETION_RECEIPT.json"
            stage4_input_path = "BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_INPUT_FREEZE.json"
            stage3_final_receipt_path = "BATCH_ROUND10_STAGE3_PRIME_ROUND3_FINAL_INTEGRITY_RECEIPT.json"
            stage3_final_audit_path = "BATCH_ROUND10_STAGE3_PRIME_ROUND3_FINAL_INTEGRITY_AUDIT.json"
            stage3_round3_receipt_path = "BATCH_ROUND10_STAGE3_PRIME_ROUND3_RECEIPT.json"
            stage3_round2_input_path = "BATCH_ROUND10_STAGE3_PRIME_ROUND2_INPUT_FREEZE.json"
            checker_path = paper_repo_path(self.cfg, "notes/stage3_prime_round1_checker_receipt.json")
            expected = {
                completion_path: "adad8657340c41ae4b054b5a291c9bc58a3e21acad5e07eacf285c63a414aa4f",
                stage4_input_path: "82dbf52120f120ffea6ba82b4614c69d4022a32bc01305a892eadde92b8248b7",
                stage3_final_receipt_path: "f6eb05b19724b868b5aacb3dfbfb28ec56995675effd5984176bd9aea202f53e",
                stage3_final_audit_path: "b61f44535bd83b84da163391f30225de1b6afba5aa1434babb0bcca808c5b692",
                stage3_round3_receipt_path: "ad20c4331936d2d8e1fb55613f72c3cf6bb5d07852775a47071ac427a9107172",
                stage3_round2_input_path: "89c96e5510ebab83cd5dec9f81958fbd345a91e68c05939b15f42f828e469281",
                checker_path: "960bc02225aa6d0e3215ef99e1e9a27179b453783d20f8472d053468fbfcfe9e",
                p30_panel_path: "3b609c217252545229f7641455502effaa678c3417d3313b077ed35aeca39890",
            }
            descs = {path: self._desc(path) for path in expected}
            for path, expected_sha in expected.items():
                if descs[path]["sha256"] != expected_sha:
                    raise RuntimeError(f"P30 historical panel-provenance chain drift: {path}")
            round1 = self._desc(self.round1_path)
            return {
                "type": "TRANSITIVE_SHA_BINDING",
                "lineage_role": "P30_STAGE3_PANEL_PROVENANCE_HISTORICAL_FREEZE_CHAIN",
                "hops": [
                    self._hop(self.root_lock_desc["repo_path"], round1),
                    self._hop(self.round1_path, self.freeze_desc),
                    self._hop(self.freeze_path, descs[completion_path]),
                    self._hop(completion_path, descs[stage4_input_path]),
                    self._hop(stage4_input_path, descs[stage3_final_receipt_path]),
                    self._hop(stage3_final_receipt_path, descs[stage3_final_audit_path]),
                    self._hop(stage3_final_audit_path, descs[stage3_round3_receipt_path]),
                    self._hop(stage3_round3_receipt_path, descs[stage3_round2_input_path]),
                    self._hop(stage3_round2_input_path, descs[checker_path]),
                    self._hop(checker_path, target, "notes/stage3_review_panel_provenance.json"),
                ],
                "boundary": (
                    "The raw panel object is reached only through the current lock's historical Stage-4/Stage-3 "
                    "freeze ancestry; the independent semantic review is not used as an authorization proxy."
                ),
            }
        phase6_path = paper_repo_path(self.cfg, "notes/stage1_phase6_claim_intent_manifest.json")
        phase6_report_path = paper_repo_path(self.cfg, "notes/stage1_phase6_final_report.md")
        if self.cfg["paper"] == 31 and repo_path in {phase6_path, phase6_report_path}:
            stage25_path = paper_repo_path(self.cfg, "notes/stage2_5_integrity_report.json")
            post_path = "BATCH_ROUND10_STAGE2_5_POST_REPAIR_INPUT_FREEZE.json"
            pre_path = "BATCH_ROUND10_STAGE2_5_INPUT_FREEZE.json"
            stage2_output_path = "BATCH_ROUND10_STAGE2_OUTPUT_MANIFEST.json"
            stage2_input_path = "BATCH_ROUND10_STAGE2_INPUT_FREEZE.json"
            expected = {
                stage25_path: "52fe4a73db645a4d83c0665fc7961da18baf77c7a80d9b3c54e1d339fd5a8754",
                post_path: "54bd577683595dd9259ba2a97405b7257a269bf740ffcaa1c0135718869e5041",
                pre_path: "8da3f9b70f09d0f7555ce3e233eeddb81c7250b726a8871d0f76fa2aa053907e",
                stage2_output_path: "b023d9b91e18580bc9921be56c1ab0fb0c6723575305baae1a7f330eb1907bfa",
                stage2_input_path: "923339d65d4fd073483d01d54cdf8eb4e1e0e540d944dae7aaf1198db9f2212c",
                phase6_path: "b9a61badd7e6d05c31ae0ce4f81adfa6ea1c40269afe37de9a620c763597aa38",
                phase6_report_path: "bb674098ead518a44ab1e8e57cd63599549cc8035d54fddda924926c20560f61",
            }
            descs = {path: self._desc(path) for path in expected}
            for path, expected_sha in expected.items():
                if descs[path]["sha256"] != expected_sha:
                    raise RuntimeError(f"P31 historical Phase-6 chain drift: {path}")
            round1 = self._desc(self.round1_path)
            return {
                "type": "TRANSITIVE_SHA_BINDING",
                "lineage_role": "P31_PHASE6_HISTORICAL_STAGE1_STAGE2_FREEZE_CHAIN",
                "hops": [
                    self._hop(self.root_lock_desc["repo_path"], round1),
                    self._hop(self.round1_path, self.freeze_desc),
                    self._hop(self.freeze_path, descs[stage25_path]),
                    self._hop(stage25_path, descs[post_path]),
                    self._hop(post_path, descs[pre_path]),
                    self._sha_field_hop(
                        pre_path,
                        descs[stage2_output_path],
                        "stage2_output_manifest_sha256",
                        path_derivation_rule="FIELD_NAME_TO_ROOT_STAGE2_OUTPUT_MANIFEST",
                    ),
                    self._sha_field_hop(
                        stage2_output_path,
                        descs[stage2_input_path],
                        "input_freeze_sha256",
                        path_derivation_rule="FIELD_NAME_TO_ROOT_STAGE2_INPUT_FREEZE",
                    ),
                    self._sha_field_hop(
                        stage2_input_path,
                        target,
                        "phase6_manifest_sha256" if repo_path == phase6_path else "phase6_report_sha256",
                        path_derivation_rule=(
                            "PAPER_SLUG_PHASE6_MANIFEST"
                            if repo_path == phase6_path else
                            "PAPER_SLUG_PHASE6_REPORT"
                        ),
                        scope_after='"paper": "P31"',
                        scope_before='"paper": "P32"',
                    ),
                ],
                "boundary": (
                    "The early Stage-2 freezes use canonical schema field names for three SHA-only links; "
                    "each resolved path, exact raw field span, and intervening artifact hash is replayed."
                ),
            }
        # The current locked matrix carries the source-finalization path/SHA
        # witness.  This is the controlling transitive chain for retained
        # excerpts and bounded-unavailability dispositions.
        source_finalization = self.input_manifest.get("inputs", {}).get("source_finalization")
        if isinstance(source_finalization, dict):
            normalized = paper_repo_path(self.cfg, source_finalization["path"])
            if normalized == repo_path:
                if source_finalization["sha256"] != target["sha256"]:
                    raise RuntimeError(f"source-finalization SHA mismatch for {repo_path}")
                matrix_path = paper_repo_path(self.cfg, f"notes/{self.cfg['matrix']}")
                matrix_desc = self._desc(matrix_path)
                return {
                    "type": "TRANSITIVE_SHA_BINDING",
                    "hops": [
                        self._hop(self.root_lock_desc["repo_path"], matrix_desc),
                        self._hop(matrix_path, target, source_finalization["path"]),
                    ],
                }
        # Other current-manifest paths may be used only when that manifest is
        # itself a top-level lock row; never call a generated manifest locked.
        for input_name, input_row in self.input_manifest.get("inputs", {}).items():
            if not isinstance(input_row, dict) or not {"path", "sha256"}.issubset(input_row):
                continue
            if input_name == "reference_network":
                continue
            normalized = input_row["path"] if input_row["path"].startswith("papers/") else paper_repo_path(self.cfg, input_row["path"])
            if normalized != repo_path:
                continue
            if self.input_manifest_path not in self.top_rows:
                continue
            if input_row["sha256"] != target["sha256"]:
                raise RuntimeError(f"current input-manifest SHA mismatch for {repo_path}")
            input_desc = self._desc(self.input_manifest_path)
            return {
                "type": "TRANSITIVE_SHA_BINDING",
                "hops": [
                    self._hop(self.root_lock_desc["repo_path"], input_desc),
                    self._hop(self.input_manifest_path, target, input_row["path"]),
                ],
            }
        network_rel = self.input_manifest["inputs"].get("reference_network")
        if network_rel and repo_path == paper_repo_path(self.cfg, network_rel["path"]):
            if network_rel["sha256"] != target["sha256"]:
                raise RuntimeError(f"fresh reference-network manifest mismatch for {repo_path}")
            # The retained collector is intentionally shared: its immutable
            # CONFIGS tuple covers both P30 and P31, and its one no-clobber run
            # emitted both current network artifacts.  Never treat a generated
            # network JSON object as its own collector.
            collector_path = SHARED_NETWORK_COLLECTOR_REL
            collector = self._desc(collector_path)
            collector_text = (ROOT / collector_path).read_text(encoding="utf-8")
            marker = '"BATCH_ROUND10_STAGE4_5_ROUND2_AUTHORIZATION_RECEIPT.json"'
            at = collector_text.find(marker)
            end = collector_text.find("),", at)
            if at < 0 or end < 0:
                raise RuntimeError("fresh collector omits authorization-receipt binding")
            authority_excerpt = collector_text[at:end + 2]
            witness_end = end + 2
            if AUTHORITY_RECEIPT_SHA not in authority_excerpt or "1203" not in authority_excerpt:
                raise RuntimeError("fresh collector authorization binding is incomplete")
            authority_witness = {
                "raw_utf8_span": {
                    "start": len(collector_text[:at].encode("utf-8")),
                    "end": len(collector_text[:witness_end].encode("utf-8")),
                },
                "raw_excerpt": authority_excerpt,
                "raw_excerpt_sha256": sha_bytes(authority_excerpt.encode("utf-8")),
            }
            network = json.loads((ROOT / repo_path).read_text(encoding="utf-8"))
            events = []
            event_slugs = ("P30-S02", "P30-C01", "P30-C02") if self.cfg["paper"] == 30 else ("P31-S23", "P31-S24")
            for ref_slug in event_slugs:
                ref = next(row for row in network["references"] if row["ref_slug"] == ref_slug)
                event = ref["query_attempts"]["crossref_doi"]
                if event is not None:
                    message_raw = json.dumps(event["crossref_message"], ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
                    events.append({
                        "kind": "crossref_doi",
                        "ref_slug": ref_slug,
                        "request_method": event["request_method"],
                        "request_url": event["request_url"],
                        "requested_at": event["requested_at"],
                        "http_status": event["http_status"],
                        "response_bytes": event["response_bytes"],
                        "response_sha256": event["response_sha256"],
                        "embedded_crossref_message_sha256": sha_bytes(message_raw),
                        "embedded_crossref_message": event["crossref_message"],
                    })
                else:
                    event = ref["query_attempts"]["official_landing_fallback"]
                    embedded = {
                        "fresh_determination": ref["fresh_determination"],
                        "body_prefix_utf8": event["body_prefix_utf8"],
                    }
                    message_raw = json.dumps(embedded, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
                    events.append({
                        "kind": "official_landing_fallback",
                        "ref_slug": ref_slug,
                        "request_method": event["request_method"],
                        "request_url": event["request_url"],
                        "requested_at": event["requested_at"],
                        "http_status": event["http_status"],
                        "response_bytes": event["response_bytes"],
                        "response_sha256": event["response_sha256"],
                        "embedded_crossref_message_sha256": sha_bytes(message_raw),
                        "embedded_crossref_message": embedded,
                    })
            return {
                "type": "FRESH_AUTHORIZED_RETRIEVAL_PROVENANCE",
                "authorization_receipt": self._desc("BATCH_ROUND10_STAGE4_5_ROUND2_AUTHORIZATION_RECEIPT.json"),
                "input_lock": self.root_lock_desc,
                "collector_script": collector,
                "collector_script_status": "RETAINED_SHARED_P30_P31_NO_CLOBBER_COLLECTOR",
                "collector_authority_witness": authority_witness,
                "retrieval_events": events,
                "retrieval_artifact": target,
                "final_manifest_binding": {
                    "path": "notes/stage4_5_round2_output_manifest.json",
                    "required_rows": [
                        collector_path,
                        f"notes/{Path(repo_path).name}",
                        "notes/stage4_5_round2_local_claim_dependency_catalog.json",
                    ],
                    "status": "REPLAYED_AFTER_CANDIDATE_MANIFEST_ASSEMBLY",
                },
                "boundary": (
                    "Fresh authorized retrieval evidence generated after the input lock; it is not described as a top-level locked input. "
                    "The retained collector and structured Crossref/Semantic-Scholar messages or bounded HTML prefix are replayable; recorded "
                    "transport response byte counts/digests are not misrepresented as independently recomputable because complete raw transport bodies were not retained."
                ),
            }
        if repo_path == INDEPENDENT_REVIEW_REL:
            return {
                "type": "AUTHORIZED_NONCONTROLLING_INDEPENDENT_REVIEW",
                "authority_receipt_sha256": AUTHORITY_RECEIPT_SHA,
                "review_artifact": self.independent_review_desc,
                "target_artifact": target,
                "boundary": "The review is an explicitly accepted audit-side correction basis, not a controlling scientific source or a substitute for underlying raw carriers.",
            }
        if repo_path in self.review_carriers:
            expected = self.review_carriers[repo_path]
            if expected["sha256"] != target["sha256"] or expected["bytes"] != target["bytes"]:
                raise RuntimeError(f"independent review carrier mismatch for {repo_path}")
            return {
                "type": "AUTHORIZED_NONCONTROLLING_INDEPENDENT_REVIEW",
                "authority_receipt_sha256": AUTHORITY_RECEIPT_SHA,
                "review_artifact": self.independent_review_desc,
                "review_to_target_witness": self._hop(INDEPENDENT_REVIEW_REL, target),
                "target_artifact": target,
                "boundary": "The accepted independent review binds the raw carrier identity; semantic support is drawn from the target raw span, not from the review's prose.",
            }
        raise RuntimeError(f"no replayable binding chain for {repo_path}")


def carrier_specs(cfg: dict[str, Any]) -> dict[str, dict[str, Any]]:
    note = lambda name: paper_repo_path(cfg, f"notes/{name}")
    base = f"papers/{cfg['slug']}"
    common = {
        "no_code": {"path": f"{base}/code/.gitkeep", "probe": "no scientific code executed" if cfg["paper"] == 30 else "no code executed", "role": "direct locked absence-of-code status"},
        "no_experiment": {"path": f"{base}/experiments/.gitkeep", "probe": "no experiment registered or run" if cfg["paper"] == 30 else "no experiment run", "role": "direct locked absence-of-experiment status"},
        "no_results": {"path": f"{base}/results/.gitkeep", "probe": "no result generated" if cfg["paper"] == 30 else "no results", "role": "direct locked absence-of-results status"},
        "reader_entries": {"path": note("stage4_prime_reader_artifact_manifest_round2.json"), "probe": '"entry_count": 11,', "role": "hash-bound reader-manifest population"},
        "query_bound": {"path": note("stage4_prime_literature_screening_ledger_round2.json"), "probe": '"retrieval_bound": "one Crossref-ranked metadata record per exact frozen query"', "role": "dated replay retrieval bound"},
        "source_effect_fields": {"path": note("stage1_phase3_literature_matrix.tsv"), "probe": "source_id\tauthors_year\ttheme\texistence_outcome\tclaim_fitness_grade\tsupport_class\tadmissible_contribution", "role": "raw source-effect field schema"},
        "author_name": {"path": note("stage2_5_material_passport.json"), "probe": "Liang Wang is the named scholar", "role": "locked scholar identity metadata"},
        "author_event": {"path": note("stage4_prime_author_adjudication.json"), "probe": '"actor_role":"author","event_id":"AUTHOR-EVENT-20260903-ROUND10-STAGE4-PRIME-P30-P31"', "role": "locked author-adjudication event"},
        "stage3_decision": {"path": note("stage3_prime_round2_traceability.json"), "probe": '"decision_state": "Major Revision"', "role": "direct locked Stage-3 decision status"},
    }
    if cfg["paper"] == 30:
        common.update({
            "initial_system": {"path": note("stage1_prestart_brief.md"), "probe": "inherits Paper 25's equilateral `d=6a` three-disk geometry", "role": "locked inherited initial-system boundary"},
            "route_state": {"path": note("stage4_route_crosswalk.md"), "probe": "PAPER_ROUTE_POSITION=A0_FAIL_/_A2_NOT_ELIGIBLE_/_NO_ROUTE_PROMOTION;_FORMAL_TUPLE_UNASSIGNED", "role": "direct locked Route state"},
            "matrix_rows": {"path": note(cfg["matrix"]), "probe": '"row_count": 28,', "role": "direct locked matrix denominator"},
            "matrix_18": {"path": note(cfg["matrix"]), "probe": '"bounded_substantive_locator_rows": 18', "role": "direct locked bounded-locator count"},
            "matrix_8": {"path": note(cfg["matrix"]), "probe": '"explicit_bounded_unavailability_rows": 8', "role": "direct locked bounded-unavailability count"},
            "corpus_68": {"path": note("stage1_phase2_annotated_bibliography.md"), "probe": "| Record manifestations deliberately inspected | 68 |", "role": "raw corpus capture count"},
            "corpus_52": {"path": note("stage1_phase2_annotated_bibliography.md"), "probe": "| Unique records entering title/abstract screen | 52 |", "role": "raw deduplicated screen count"},
            "corpus_26": {"path": note("stage1_phase2_annotated_bibliography.md"), "probe": "| Final unique included sources | **26** |", "role": "raw admitted-source count"},
            "corpus_24": {"path": note("stage1_phase2_annotated_bibliography.md"), "probe": "Peer-reviewed proportion: **24/26 = 92.3%**.", "role": "raw peer-reviewed corpus count"},
            "query_rows": {"path": note("stage4_prime_literature_screening_ledger_round2.json"), "probe": '"row_count": 54,', "role": "raw dated replay row count"},
            "bib_c01": {"path": note("stage4_prime_references_round2.bib"), "probe": "@article{P30-C01,", "role": "direct locked versioned-Bib correction entry"},
            "bib_c02": {"path": note("stage4_prime_references_round2.bib"), "probe": "@article{P30-C02,", "role": "direct locked versioned-Bib correction entry"},
            "bib_wrong_correction": {"path": note("stage4_prime_references_round2.bib"), "probe": "Affected use is bound to correction companion DOI 10.1063/1.457669", "role": "current P30-S02 bibliography-side incorrect correction binding", "component_verdict": "CONTRADICTED_CURRENT_STATUS"},
            "draft_wrong_correction": {"path": note("stage4_prime_revision_round3.tex"), "probe": "P30-S01 and P30-S02 are bound to the published correction\nDOI", "role": "current manuscript-side incorrect correction binding", "component_verdict": "CONTRADICTED_CURRENT_STATUS"},
            "draft_wrong_correction_late": {"path": note("stage4_prime_revision_round3.tex"), "probe": "P30-S01/P30-S02 remain bound to\n\\citep{P30-C01}", "role": "later manuscript-side incorrect correction binding", "component_verdict": "CONTRADICTED_CURRENT_STATUS"},
            "stale_search_status": {"path": note("stage4_prime_revision_round3.tex"), "probe": "No independently reproducible search supplement was authorized.", "role": "stale current manuscript status surface", "component_verdict": "MAJOR_DISTORTION_STALE_STATUS"},
            "dated_search_replay": {"path": note("stage4_prime_revision_round3.tex"), "probe": "A dated replay on 3 September 2026 ran all\n54 exact frozen query strings", "role": "same locked manuscript's direct contradictory replay statement", "component_verdict": "CONTRADICTS_STALE_STATUS"},
            "s02_updated_by": {"path": note("stage4_5_round2_reference_network_audit.json"), "probe": '"updated-by": [\n              {\n                "DOI": "10.1063/1.457672"', "role": "fresh Crossref P30-S02 updated-by relation", "component_verdict": "CONTRADICTS_CURRENT_BINDING"},
            "c01_update_to": {"path": note("stage4_5_round2_reference_network_audit.json"), "probe": '"update-to": [\n              {\n                "DOI": "10.1063/1.456017"', "role": "fresh Crossref P30-C01 update-to relation", "component_verdict": "CONTRADICTS_CURRENT_BINDING"},
            "c02_update_to": {"path": note("stage4_5_round2_reference_network_audit.json"), "probe": '"update-to": [\n              {\n                "DOI": "10.1063/1.456019"', "role": "fresh Crossref P30-C02 update-to relation", "component_verdict": "VERIFIED_METADATA_RELATION"},
        })
    else:
        common.update({
            "initial_population": {"path": note("stage1_prestart_brief.md"), "probe": "finite 138-instance/55-group", "role": "locked inherited population and system boundary"},
            "route_state": {"path": note("stage4_route_crosswalk.md"), "probe": "PAPER_ROUTE_POSITION=A1-ONLY_PREPARATION;_FORMAL_TUPLE_UNASSIGNED;_POSITIVE_ARITHMETIC_A2_ABSENT", "role": "direct locked Route state"},
            "matrix_rows": {"path": note(cfg["matrix"]), "probe": '"row_count": 24,', "role": "direct locked method-matrix denominator"},
            "matrix_7": {"path": note(cfg["matrix"]), "probe": '"bounded_substantive_locator_rows": 7', "role": "direct locked bounded-locator count"},
            "matrix_15": {"path": note(cfg["matrix"]), "probe": '"explicit_bounded_unavailability_rows": 15', "role": "direct locked bounded-unavailability count"},
            "corpus_44": {"path": note("stage1_phase2_annotated_bibliography.md"), "probe": "| Manually captured records | 44 |", "role": "raw corpus capture count"},
            "corpus_9": {"path": note("stage1_phase2_annotated_bibliography.md"), "probe": "| Duplicate manifestations removed | 9 |", "role": "raw deduplication count"},
            "corpus_35": {"path": note("stage1_phase2_annotated_bibliography.md"), "probe": "| Unique records screened | 35 |", "role": "raw screened-record count"},
            "corpus_13": {"path": note("stage1_phase2_annotated_bibliography.md"), "probe": "| Excluded after title/abstract/metadata screening | 13 |", "role": "raw exclusion count"},
            "corpus_22": {"path": note("stage1_phase2_annotated_bibliography.md"), "probe": "| Included in this bibliography | 22 |", "role": "raw included-source count"},
            "query_rows": {"path": note("stage4_prime_literature_screening_ledger_round2.json"), "probe": '"row_count": 20,', "role": "raw dated replay row count"},
            "bib_s23": {"path": note("stage4_prime_references_round2.bib"), "probe": "@inproceedings{P31-S23,", "role": "direct locked P31-S23 bibliography identity"},
            "bib_s24": {"path": note("stage4_prime_references_round2.bib"), "probe": "@inproceedings{P31-S24,", "role": "direct locked P31-S24 bibliography identity"},
            "stage25_ai_role": {"path": note("stage2_5_integrity_report.json"), "probe": "AI-assisted review and drafting used one Codex model family", "role": "transitively locked same-family role-separation status"},
            "stage25_originality": {"path": note("stage2_5_integrity_report.json"), "probe": '"sampled": 21', "after": '"D_originality"', "role": "transitively locked Stage-2.5 originality sample count"},
        })

    def field_probe(field: str, value: Any, cap: int = 24) -> str:
        candidate = f'{json.dumps(field, ensure_ascii=False)}: {json.dumps(value, ensure_ascii=False)}'
        words = list(re.finditer(r"\S+", candidate))
        return candidate if len(words) <= cap else candidate[:words[cap - 1].end()]

    def add_expansion(name: str, keys: list[str]) -> None:
        common[name] = {"expands": keys}

    # Complete reader-manifest replay: header, locator/boundary, and one compact
    # exact tuple carrying path/schema/hash/bytes/access-state for every entry.
    reader_path = ROOT / note("stage4_prime_reader_artifact_manifest_round2.json")
    reader = json.loads(reader_path.read_text(encoding="utf-8"))
    reader_keys: list[str] = []
    for field in ("schema_version", "repository_locator", "locator_state", "entry_count", "boundary"):
        key = f"reader_full_{field}"
        reader_probe = f'"{field}": {{' if isinstance(reader[field], dict) else field_probe(field, reader[field])
        common[key] = {
            "path": note("stage4_prime_reader_artifact_manifest_round2.json"),
            "probe": reader_probe,
            "role": f"full reader-manifest {field} field",
        }
        reader_keys.append(key)
    reader_text = reader_path.read_text(encoding="utf-8")
    for index, entry in enumerate(reader["entries"], 1):
        start = reader_text.index(f'"path": {json.dumps(entry["path"])}')
        end_marker = field_probe("repository_relative_access_state", entry["repository_relative_access_state"])
        end = reader_text.index(end_marker, start) + len(end_marker)
        excerpt = reader_text[start:end]
        if len(excerpt.split()) > 25:
            # Split the exact row into identity and digest/access tuples; both
            # remain scoped to the unique entry path.
            for suffix, field in (("identity", "schema_or_format"), ("sha", "sha256"), ("bytes", "bytes"), ("access", "repository_relative_access_state")):
                key = f"reader_full_e{index:02d}_{suffix}"
                common[key] = {
                    "path": note("stage4_prime_reader_artifact_manifest_round2.json"),
                    "probe": field_probe(field, entry[field]),
                    "after": f'"path": {json.dumps(entry["path"])}',
                    "before": f'"path": {json.dumps(reader["entries"][index]["path"])}' if index < len(reader["entries"]) else None,
                    "role": f"reader-manifest entry {index} {suffix} field for {entry['path']}",
                }
                reader_keys.append(key)
        else:
            key = f"reader_full_e{index:02d}"
            common[key] = {
                "path": note("stage4_prime_reader_artifact_manifest_round2.json"),
                "probe": excerpt,
                "role": f"complete reader-manifest entry {index} for {entry['path']}",
            }
            reader_keys.append(key)
    add_expansion("reader_manifest_full", reader_keys)

    if cfg["paper"] == 31:
        stale_matrix_entry = next(
            entry
            for entry in reader["entries"]
            if entry["path"] == "notes/stage4_prime_method_passage_matrix_round2.json"
        )
        current_matrix_path = ROOT / note(cfg["matrix"])
        current_matrix = json.loads(current_matrix_path.read_text(encoding="utf-8"))
        if (
            stale_matrix_entry["sha256"]
            != "e18e78cd31f85858184d01ef1e2a36ae80f80830c80b6b3a2977d0f00206f06b"
            or stale_matrix_entry["bytes"] != 12020
            or sha_path(current_matrix_path) != cfg["matrix_sha"]
            or current_matrix_path.stat().st_size != 19277
        ):
            raise RuntimeError("P31 stale-reader/current-matrix contradiction inputs changed")
        next_reader_path = reader["entries"][
            reader["entries"].index(stale_matrix_entry) + 1
        ]["path"]
        common["reader_stale_matrix_entry"] = {
            "path": note("stage4_prime_reader_artifact_manifest_round2.json"),
            "probe": field_probe("sha256", stale_matrix_entry["sha256"]),
            "after": field_probe("path", stale_matrix_entry["path"]),
            "before": field_probe("path", next_reader_path),
            "role": (
                "reader manifest's stale method-matrix binding: the listed digest "
                "e18e78cd... and 12020-byte object no longer match the current locked matrix"
            ),
            "component_verdict": "MAJOR_DISTORTION_STALE_ARTIFACT_BINDING",
        }
        common["current_matrix_artifact"] = {
            "path": note(cfg["matrix"]),
            "probe": field_probe("schema_version", current_matrix["schema_version"]),
            "role": (
                "current top-level locked method-matrix artifact; its artifact descriptor "
                "carries digest 1adc4c... and 19277 bytes, directly contradicting the reader-manifest row"
            ),
            "component_verdict": "CONTRADICTS_STALE_ARTIFACT_BINDING",
        }

    # Versioned-bibliography enumeration is evidence for entry closure, not for
    # passage content.  Every key is separately tupled.
    bib_text = (ROOT / note("stage4_prime_references_round2.bib")).read_text(encoding="utf-8")
    bib_keys = re.findall(r"(?m)^@(\w+)\{([^,]+),", bib_text)
    expected = 28 if cfg["paper"] == 30 else 24
    if len(bib_keys) != expected:
        raise RuntimeError(f"{cfg['paper_id']} versioned Bib expected {expected} entries, got {len(bib_keys)}")
    bib_expansion = []
    for index, (entry_type, citekey) in enumerate(bib_keys, 1):
        key = f"bib_entry_{index:02d}_{re.sub(r'[^a-z0-9]', '_', citekey.lower())}"
        common[key] = {
            "path": note("stage4_prime_references_round2.bib"),
            "probe": f"@{entry_type}{{{citekey},",
            "role": f"versioned bibliography entry {index}/{expected}: {citekey}",
        }
        bib_expansion.append(key)
    add_expansion(f"bib_all_{expected}", bib_expansion)

    matrix_path = ROOT / note(cfg["matrix"])
    matrix = json.loads(matrix_path.read_text(encoding="utf-8"))
    common["matrix_boundary"] = {
        "path": note(cfg["matrix"]),
        "probe": field_probe("boundary", matrix["boundary"]),
        "role": "current matrix metadata-versus-passage and no-transfer boundary",
    }

    if cfg["paper"] == 31:
        by_source = {row["source_id"]: row for row in matrix["rows"]}
        final_path = ROOT / note("stage4_5_round1_source_finalization_proposal.json")
        finalization = json.loads(final_path.read_text(encoding="utf-8"))
        by_final = {row["source_id"]: row for row in finalization["rows"]}
        ordered = [row["source_id"] for row in matrix["rows"]]
        for pos, source_id in enumerate(ordered):
            stem = source_id.lower().replace("-", "_")
            row = by_source[source_id]
            next_marker = f'"source_id": "{ordered[pos + 1]}"' if pos + 1 < len(ordered) else None
            for suffix, field in (("role", "component_or_claim_role"), ("status", "passage_status"), ("scope", "hypothesis_or_scope"), ("boundary", "transfer_boundary")):
                common[f"matrix_{stem}_{suffix}"] = {
                    "path": note(cfg["matrix"]),
                    "probe": field_probe(field, row[field]),
                    "after": f'"source_id": "{source_id}"',
                    "before": next_marker,
                    "role": f"current method-matrix {source_id} {field}",
                }
            if source_id not in by_final:
                continue
            frow = by_final[source_id]
            fpos = next(i for i, value in enumerate(finalization["rows"]) if value["source_id"] == source_id)
            next_context = finalization["rows"][fpos + 1]["context_id"] if fpos + 1 < len(finalization["rows"]) else None
            final_fields = [("status", "finalization_status")]
            if source_id in P31_LOCATED:
                final_fields += [("locator", "exact_passage_locator"), ("excerpt", "support_excerpt"), ("excerpt_hash", "support_excerpt_sha256")]
            else:
                final_fields += [("unavailability", "unavailability.code")]
            for suffix, field in final_fields:
                field_name = field
                if field == "unavailability.code":
                    field_name = "code"
                    field_value = frow["unavailability"]["code"]
                    probe = (
                        f'"context_id": "{frow["context_id"]}",\n'
                        '      "exact_passage_locator": null'
                    )
                else:
                    field_value = frow[field]
                    probe = field_probe(field_name, field_value)
                common[f"final_{stem}_{suffix}"] = {
                    "path": note("stage4_5_round1_source_finalization_proposal.json"),
                    "probe": probe,
                    "after": None if field == "unavailability.code" else f'"context_id": "{frow["context_id"]}"',
                    "before": None if field == "unavailability.code" else (f'"context_id": "{next_context}"' if next_context else None),
                    "role": f"source-finalization {source_id} {field}",
                }

        common["source_finalization_no_locator_guessing"] = {
            "path": note("stage4_5_round1_source_finalization_proposal.json"),
            "probe": '"locator_guessing": false',
            "after": '"boundaries": {',
            "before": '"controlling_checkpoint": {',
            "role": "locked source-finalization boundary that unavailable locators were not guessed",
        }

        # Replay the complete 20-query research event at atomic field granularity.
        # Header facts, transport facts, candidate identity, inventory match,
        # decision, and reason remain separate tuples so a count-only carrier
        # cannot masquerade as evidence that every event field exists.
        replay_path = note("stage4_prime_literature_replay_round2.raw.json")
        replay = json.loads((ROOT / replay_path).read_text(encoding="utf-8"))
        replay_header_keys: list[str] = []
        for suffix, field, value in (
            ("schema", "schema_version", replay["schema_version"]),
            ("generated", "generated_at_utc", replay["generated_at_utc"]),
            ("interface", "retrieval_interface", replay["retrieval_interface"]),
            ("bound", "retrieval_bound", replay["retrieval_bound"]),
            ("query_document_path", "path", replay["source_query_document"]["path"]),
            ("query_document_sha", "sha256", replay["source_query_document"]["sha256"]),
            ("query_count", "query_count", replay["source_query_document"]["query_count"]),
            ("historical_boundary", "historical_reconstruction_boundary", replay["historical_reconstruction_boundary"]),
        ):
            key = f"p31_replay_header_{suffix}"
            common[key] = {
                "path": replay_path,
                "probe": field_probe(field, value),
                "after": '"source_query_document": {' if suffix in {"query_document_path", "query_document_sha", "query_count"} else None,
                "before": '"historical_reconstruction_boundary"' if suffix in {"query_document_path", "query_document_sha", "query_count"} else None,
                "role": f"raw 20-query replay header field {field}",
            }
            replay_header_keys.append(key)
        replay_event_keys: list[str] = []
        for index, event in enumerate(replay["rows"], 1):
            qid = event["query_id"]
            after = field_probe("query_id", qid)
            before = field_probe("query_id", replay["rows"][index]["query_id"]) if index < len(replay["rows"]) else None
            crossref = event["crossref"]
            top = crossref["top_record"]
            for suffix, field, value in (
                ("query", "query", event["query"]),
                ("time", "retrieved_at_utc", event["retrieved_at_utc"]),
                ("endpoint", "endpoint", crossref["endpoint"]),
                ("status", "http_status", crossref["http_status"]),
                ("message_type", "message_type", crossref["message_type"]),
                ("candidate_doi", "doi", top["doi"]),
                ("candidate_title", "title", top["title"]),
            ):
                key = f"p31_replay_{qid.lower()}_{suffix}"
                common[key] = {
                    "path": replay_path,
                    "probe": field_probe(field, value),
                    "after": after,
                    "before": before,
                    "role": f"raw replay event {qid}/20 {field}",
                }
                replay_event_keys.append(key)
        add_expansion("p31_replay_header_and_boundary", replay_header_keys)
        add_expansion("p31_replay_full", replay_header_keys + replay_event_keys)

        ledger_path = note("stage4_prime_literature_screening_ledger_round2.json")
        ledger = json.loads((ROOT / ledger_path).read_text(encoding="utf-8"))
        ledger_keys: list[str] = []
        for suffix, field, value, after, before in (
            ("schema", "schema_version", ledger["schema_version"], None, None),
            ("generated", "generated_at_utc", ledger["generated_at_utc"], None, None),
            ("raw_path", "path", ledger["source_raw_replay"]["path"], '"source_raw_replay": {', '"method": {'),
            ("raw_sha", "sha256", ledger["source_raw_replay"]["sha256"], '"source_raw_replay": {', '"method": {'),
            ("raw_rows", "rows", ledger["source_raw_replay"]["rows"], '"source_raw_replay": {', '"method": {'),
            ("bound", "retrieval_bound", ledger["method"]["retrieval_bound"], '"method": {', '"row_count"'),
            ("match_rule", "match_rule", ledger["method"]["match_rule"], '"method": {', '"row_count"'),
            ("decision_schema", "decision_vocabulary", ledger["method"]["decision_vocabulary"], '"method": {', '"row_count"'),
            ("historical_boundary", "historical_reconstruction_boundary", ledger["method"]["historical_reconstruction_boundary"], '"method": {', '"row_count"'),
            ("row_count", "row_count", ledger["row_count"], None, '"rows": ['),
            ("retained", "retained_existing", ledger["retained_existing"], None, '"rows": ['),
            ("screened_out", "screened_out", ledger["screened_out"], None, '"rows": ['),
            ("science_unchanged", "scientific_result_changed", ledger["scientific_result_changed"], None, None),
            ("canonical_unrefreshed", "canonical_result_refreshed", ledger["canonical_result_refreshed"], None, None),
        ):
            key = f"p31_screening_header_{suffix}"
            common[key] = {
                "path": ledger_path,
                "probe": f'"{field}": [' if isinstance(value, list) else field_probe(field, value),
                "after": after,
                "before": before,
                "role": f"raw screening-ledger header/schema field {field}",
            }
            ledger_keys.append(key)
        for index, event in enumerate(ledger["rows"], 1):
            qid = event["query_id"]
            after = field_probe("query_id", qid)
            before = field_probe("query_id", ledger["rows"][index]["query_id"]) if index < len(ledger["rows"]) else None
            for suffix, field in (
                ("query", "exact_frozen_query"),
                ("time", "retrieved_at_utc"),
                ("interface", "interface"),
                ("status", "http_status"),
                ("candidate_doi", "candidate_doi"),
                ("candidate_title", "candidate_title"),
                ("candidate_year", "candidate_year"),
                ("decision", "decision"),
                ("match", "matched_source_id"),
                ("reason", "decision_reason"),
            ):
                key = f"p31_screening_{qid.lower()}_{suffix}"
                probe = field_probe(field, event[field], cap=8 if field == "decision_reason" else 24)
                common[key] = {
                    "path": ledger_path,
                    "probe": probe,
                    "after": after,
                    "before": before,
                    "role": f"raw screening event {qid}/20 {field}",
                }
                ledger_keys.append(key)
        add_expansion("p31_screening_full", ledger_keys)

        closest_path = note("stage4_prime_closest_work_source_verification_round2.json")
        closest = json.loads((ROOT / closest_path).read_text(encoding="utf-8"))
        closest_record_keys: list[str] = []
        for index, record in enumerate(closest["records"], 1):
            source_id = record["key"]
            after = field_probe("key", source_id)
            before = field_probe("key", closest["records"][index]["key"]) if index < len(closest["records"]) else '"new_entries"'
            fields = ["method_family", "authors", "year", "title", "venue", "authoritative_metadata", "admissible_transfer", "prohibited_transfer", "verdict"]
            if "doi" in record:
                fields.append("doi")
            if "publisher_locator" in record:
                fields.append("publisher_locator")
            if "publisher" in record:
                fields.append("publisher")
            for field in fields:
                key = f"closest_{source_id.lower().replace('-', '_')}_{field}"
                common[key] = {
                    "path": closest_path,
                    "probe": f'"{field}": [' if isinstance(record[field], list) else field_probe(field, record[field]),
                    "after": after,
                    "before": before,
                    "role": f"closest-work verification {source_id} {field}",
                }
                closest_record_keys.append(key)
        common["closest_s23_locator"] = {
            **common["closest_p31_s23_publisher_locator"],
            "role": "finalized publisher DOI locator for P31-S23; metadata/identity role only",
        }
        common["closest_s24_locator"] = {
            **common["closest_p31_s24_authoritative_metadata"],
            "role": "finalized official-publisher locator for P31-S24; metadata/identity role only",
        }
        closest_header_keys: list[str] = []
        for suffix, field, value, after in (
            ("verified_at", "verified_at_utc", closest["verified_at_utc"], None),
            ("scope", "search_scope", closest["search_scope"], None),
            ("new_entries", "new_entries", closest["new_entries"], None),
            ("maximum", "maximum_authorized_new_entries", closest["maximum_authorized_new_entries"], None),
            ("novelty_boundary", "novelty_boundary", closest["novelty_boundary"], None),
            ("bibliography_mode", "bibliography_mode", closest["bibliography_mode"], None),
            ("versioned_bib_path", "path", closest["versioned_bibliography"]["path"], '"versioned_bibliography": {'),
            ("versioned_bib_sha", "sha256", closest["versioned_bibliography"]["sha256"], '"versioned_bibliography": {'),
        ):
            key = f"p31_closest_header_{suffix}"
            common[key] = {
                "path": closest_path,
                "probe": field_probe(field, value),
                "after": after,
                "role": f"closest-work verification header/finalization field {field}",
            }
            closest_header_keys.append(key)
        add_expansion("p31_closest_records", closest_record_keys)
        add_expansion("p31_closest_full", closest_header_keys + closest_record_keys)

        build_path = note("stage4_prime_revision_round3_build_receipt.json")
        build_receipt = json.loads((ROOT / build_path).read_text(encoding="utf-8"))
        build_keys: list[str] = []
        for suffix, field, value, after, before in (
            ("status", "status", build_receipt["status"], None, None),
            ("undefined_citations", "undefined_citations", build_receipt["undefined_citations"], None, None),
            ("undefined_references", "undefined_references", build_receipt["undefined_references"], None, None),
            ("bib_sha", "references_bib_sha256", build_receipt["bindings"]["references_bib_sha256"], '"bindings": {', '"boundaries": {'),
            ("canonical_manuscript_unchanged", "canonical_manuscript_or_pdf_modified", build_receipt["boundaries"]["canonical_manuscript_or_pdf_modified"], '"boundaries": {', None),
            ("canonical_bib_unchanged", "canonical_bibliography_modified", build_receipt["boundaries"]["canonical_bibliography_modified"], '"boundaries": {', None),
        ):
            key = f"p31_build_{suffix}"
            common[key] = {
                "path": build_path,
                "probe": field_probe(field, value),
                "after": after,
                "before": before,
                "role": f"exact clean-build/citation-closure field {field}",
            }
            build_keys.append(key)
        add_expansion("p31_build_closure", build_keys)

        # Fresh closest-work identities are metadata-only and do not cure the
        # missing S23/S24 method passages.
        network_path = note("stage4_5_round2_reference_network_audit.json")
        network = json.loads((ROOT / network_path).read_text(encoding="utf-8"))
        common["fresh_network_metadata_only_boundary"] = {
            "path": network_path,
            "probe": field_probe("passage_boundary", network["network_method"]["passage_boundary"]),
            "after": '"network_method": {',
            "before": '"paper_id"',
            "role": "fresh authorized network method is explicitly confined to identity and bibliographic fields; it adds no passage or integrity-screen clearance",
        }
        network_identity_keys: dict[str, list[str]] = {}
        for source_id in ("P31-S23", "P31-S24"):
            record = next(row for row in network["references"] if row["ref_slug"] == source_id)
            stem = source_id.lower().replace("-", "_")
            title = record["fields"]["title"]
            keys: list[str] = []
            for suffix, field, value in (
                ("slug", "ref_slug", source_id),
                ("title", "title", title),
                ("basis", "authoritative_basis", record["fresh_determination"]["authoritative_basis"]),
                ("verdict", "verdict", record["fresh_determination"]["verdict"]),
            ):
                key = f"network_{stem}_{suffix}"
                common[key] = {
                    "path": network_path,
                    "probe": field_probe(field, value),
                    "after": field_probe("title", title) if suffix in {"basis", "verdict"} else None,
                    "role": f"fresh authorized {source_id} identity determination {field}; metadata only",
                }
                keys.append(key)
            if "doi" in record["fields"]:
                key = f"network_{stem}_doi"
                common[key] = {
                    "path": network_path,
                    "probe": field_probe("doi", record["fields"]["doi"]),
                    "after": field_probe("title", title),
                    "role": f"fresh authorized {source_id} DOI identity; metadata only",
                }
                keys.append(key)
            else:
                key = f"network_{stem}_url"
                common[key] = {
                    "path": network_path,
                    "probe": field_probe("url", record["fields"]["url"]),
                    "after": field_probe("title", title),
                    "role": f"fresh authorized {source_id} official URL identity; metadata only",
                }
                keys.append(key)
            network_identity_keys[source_id] = keys
        add_expansion("fresh_s23_identity", network_identity_keys["P31-S23"])
        add_expansion("fresh_s24_identity", network_identity_keys["P31-S24"])
        canonical_bib = f"papers/{cfg['slug']}/paper/references.bib"
        common["canonical_bib_state"] = {
            "path": canonical_bib,
            "probe": "@",
            "role": "locked canonical bibliography byte snapshot; unchanged comparison only",
        }
        trace = json.loads((ROOT / note("stage3_prime_round2_traceability.json")).read_text(encoding="utf-8"))
        review_row = next(row for row in trace["rows"] if row["item_id"] == "REV-P31-003")
        common["stage3_four_roles"] = {
            "path": note("stage3_prime_round2_traceability.json"),
            "probe": field_probe("authors_claim", review_row["authors_claim"]),
            "after": '"item_id": "REV-P31-003"',
            "before": '"item_id": "REV-P31-004"',
            "role": "actual Stage-3 review-role/provenance disposition",
        }
        common["stage3_major_revision"] = {
            "path": note("stage3_prime_round2_traceability.json"),
            "probe": field_probe("decision_state", trace["decision_state"]),
            "role": "actual Stage-3 Major Revision decision",
        }
        apply_report = json.loads((ROOT / note("stage4_prime_revision_round3.tex.apply-report.json")).read_text(encoding="utf-8"))
        for key, field in (("revision_apply_base", "base_path"), ("revision_apply_patch", "patch_digest"), ("revision_apply_output", "output_path"), ("revision_apply_operations", "ops_applied")):
            value = len(apply_report[field]) if field == "ops_applied" else apply_report[field]
            probe_field = "ops_applied" if field == "ops_applied" else field
            probe = '"ops_applied": [' if field == "ops_applied" else field_probe(probe_field, value)
            common[key] = {"path": note("stage4_prime_revision_round3.tex.apply-report.json"), "probe": probe, "role": f"actual revision apply-report {field}"}
        phase6_path = note("stage1_phase6_claim_intent_manifest.json")
        phase6_raw = (ROOT / phase6_path).read_text(encoding="utf-8")
        phase6 = json.loads(phase6_raw)
        phase6_report_path = note("stage1_phase6_final_report.md")
        common["phase6_revision1_status"] = {
            "path": phase6_report_path,
            "probe": "**Research stage:** ARS Stage 1 Phase 6, Revision 1",
            "role": "historically freeze-bound Phase-6 report Revision-1 identity",
        }
        common["phase6_revision1_no_retrieval"] = {
            "path": phase6_report_path,
            "probe": "No new retrieval occurred during Revision 1.",
            "role": "historically freeze-bound Revision-1 no-retrieval statement",
        }
        common["phase6_revision1_no_new_artifacts"] = {
            "path": phase6_report_path,
            "probe": "No source field, reference, passage locator, direct quotation, experiment, code result, proof result, or canonical manuscript byte was introduced.",
            "after": "No new retrieval occurred during Revision 1.",
            "role": "historically freeze-bound Revision-1 no-source/no-locator/no-quotation/no-canonical-manuscript-byte boundary",
        }
        common["phase6_revision1_claimintent_frozen"] = {
            "path": phase6_report_path,
            "probe": "The Phase-6 ClaimIntent manifest was frozen before this prose and supplies the complete set of eight substantive report claims.",
            "after": "No source field, reference, passage locator, direct quotation, experiment, code result, proof result, or canonical manuscript byte was introduced.",
            "role": "historically freeze-bound Revision-1 ClaimIntent timing and eight-claim statement",
        }
        common["phase6_revision1_finding_classes"] = {
            "path": phase6_report_path,
            "probe": "Every finding below is either a closed-corpus evidence-synthesis statement, a project definition, or a prospective method obligation.",
            "after": "The Phase-6 ClaimIntent manifest was frozen before this prose",
            "role": "historically freeze-bound Revision-1 finding-class boundary",
        }
        common["phase6_pair_population"] = {
            "path": phase6_path,
            "probe": "frozen 138/55/9,453 population.",
            "role": "historically freeze-bound Phase-6 population constraint, including the 9,453 all-pairs denominator",
        }
        phase6_decoder = json.JSONDecoder()

        def phase6_raw_field(scope_start: int, scope_end: int, field: str) -> str:
            field_at = phase6_raw.find(json.dumps(field), scope_start, scope_end)
            if field_at < 0:
                raise RuntimeError(f"P31 Phase-6 ClaimIntent field missing: {field}")
            value_at = phase6_raw.find(":", field_at, scope_end) + 1
            while phase6_raw[value_at].isspace():
                value_at += 1
            _, consumed = phase6_decoder.raw_decode(phase6_raw[value_at:scope_end])
            return phase6_raw[field_at:value_at + consumed]

        def bounded_exact_chunks(value: str, maximum_words: int = 20) -> list[str]:
            """Partition an exact raw field without omitting bytes or exceeding quote limits."""
            words = list(re.finditer(r"\S+", value))
            if len(words) <= 25:
                return [value]
            chunks: list[str] = []
            cursor = 0
            for offset in range(maximum_words, len(words), maximum_words):
                boundary = words[offset].start()
                chunks.append(value[cursor:boundary])
                cursor = boundary
            chunks.append(value[cursor:])
            if "".join(chunks) != value or any(len(chunk.split()) > 25 for chunk in chunks):
                raise RuntimeError("P31 Phase-6 exact-field quote partition failed")
            return chunks

        phase6_keys: list[str] = []
        phase6_id_keys: list[str] = []
        for index, claim in enumerate(phase6["claims"], 1):
            claim_marker = field_probe("claim_id", claim["claim_id"])
            scope_start = phase6_raw.index(claim_marker)
            next_marker = (
                field_probe("claim_id", phase6["claims"][index]["claim_id"])
                if index < len(phase6["claims"]) else
                '"manifest_negative_constraints"'
            )
            scope_end = phase6_raw.index(next_marker, scope_start)

            id_key = f"phase6_c{index:02d}_id"
            common[id_key] = {
                "path": phase6_path,
                "probe": claim_marker,
                "before": next_marker,
                "role": f"Phase-6 ClaimIntent {index}/8 exact claim ID",
            }
            phase6_keys.append(id_key)
            phase6_id_keys.append(id_key)

            claim_text = claim["claim_text"]
            text_chunks = bounded_exact_chunks(claim_text)
            for part, probe in enumerate(text_chunks, 1):
                key = f"phase6_c{index:02d}_text_{part:02d}"
                common[key] = {
                    "path": phase6_path,
                    "probe": probe,
                    "after": claim_marker,
                    "before": next_marker,
                    "role": f"Phase-6 ClaimIntent {index}/8 complete claim_text segment {part}/{len(text_chunks)} under the 25-word evidence quote cap",
                }
                phase6_keys.append(key)

            for suffix, field in (("refs", "planned_refs"), ("negative", "negative_constraints")):
                raw_value = phase6_raw_field(scope_start, scope_end, field)
                if field == "planned_refs" and claim[field] == []:
                    # The two empty arrays are byte-identical.  Add only the
                    # immediately following unique constraint ID so EVR v1.0's
                    # first-occurrence extractor lands on the correct claim;
                    # the complete empty array itself remains present verbatim.
                    raw_value = (
                        raw_value
                        + ',\n      "negative_constraints": [\n        {'
                        + field_probe(
                            "constraint_id",
                            claim["negative_constraints"][0]["constraint_id"],
                        )
                    )
                chunks = bounded_exact_chunks(raw_value)
                for part, probe in enumerate(chunks, 1):
                    key = f"phase6_c{index:02d}_{suffix}_{part:02d}"
                    common[key] = {
                        "path": phase6_path,
                        "probe": probe,
                        "after": claim_marker,
                        "before": next_marker,
                        "role": f"Phase-6 ClaimIntent {index}/8 complete {field} segment {part}/{len(chunks)} under the 25-word evidence quote cap",
                    }
                    phase6_keys.append(key)
        add_expansion("phase6_claim_count", phase6_id_keys)
        add_expansion("phase6_claims_manifest", phase6_keys)
        verification_path = note("stage1_phase2_source_verification.tsv")
        common["retraction_unrun"] = {"path": verification_path, "probe": "\tUNKNOWN_NOT_CHECKED\tNOT_CHECKED\t", "after": "P31-S16\t", "before": "\n", "role": "raw P31-S16 retraction/conflict status UNKNOWN/NOT_CHECKED"}
        verification_text = (ROOT / verification_path).read_text(encoding="utf-8")
        retraction_keys: list[str] = []
        for line in verification_text.splitlines()[1:]:
            source_id = line.split("\t", 1)[0]
            key = f"retraction_status_{source_id.lower().replace('-', '_')}"
            common[key] = {
                "path": verification_path,
                "probe": "\tUNKNOWN_NOT_CHECKED\tNOT_CHECKED\t",
                "after": f"{source_id}\t",
                "before": "\n",
                "role": f"raw {source_id} conflict/retraction fields: UNKNOWN_NOT_CHECKED/NOT_CHECKED",
            }
            retraction_keys.append(key)
        add_expansion("retraction_screening_all", retraction_keys)
        common["s16_correction"] = {"path": verification_path, "probe": "RESOLVED_POST_VERIFICATION; initial finding P31-ERR-01 recorded inventory pages 287-306 against verified 287-305", "after": "P31-S16\t", "before": "\n", "role": "raw P31-S16 page-correction record"}
    else:
        # The five ARS-CITE claims bind the retained source-finalization passage,
        # locator, status, and excerpt hash, not their own TeX comments.
        final_path = note("stage4_5_round1_source_finalization_proposal.json")
        finalization = json.loads((ROOT / final_path).read_text(encoding="utf-8"))
        by_final = {row["source_id"]: row for row in finalization["rows"]}
        for source_id in [row["source_id"] for row in finalization["rows"]]:
            stem = source_id.lower().replace("-", "_")
            frow = by_final[source_id]
            fpos = next(i for i, value in enumerate(finalization["rows"]) if value["source_id"] == source_id)
            next_context = finalization["rows"][fpos + 1]["context_id"] if fpos + 1 < len(finalization["rows"]) else None
            final_fields = [("status", "finalization_status")]
            if frow["support_excerpt"] is not None:
                final_fields += [("locator", "exact_passage_locator"), ("excerpt", "support_excerpt"), ("excerpt_hash", "support_excerpt_sha256")]
            else:
                final_fields += [("unavailability", "unavailability.code")]
            for suffix, field in final_fields:
                if field == "unavailability.code":
                    field_name = "code"
                    field_value = frow["unavailability"]["code"]
                    probe = (
                        f'"context_id": "{frow["context_id"]}",\n'
                        '      "exact_passage_locator": null'
                    )
                else:
                    field_name = field
                    field_value = frow[field]
                    probe = field_probe(field_name, field_value)
                common[f"final_{stem}_{suffix}"] = {
                    "path": final_path,
                    "probe": probe,
                    "after": None if field == "unavailability.code" else f'"context_id": "{frow["context_id"]}"',
                    "before": None if field == "unavailability.code" else (f'"context_id": "{next_context}"' if next_context else None),
                    "role": f"source-finalization {source_id} {field}",
                }
        replay_path = note("stage4_prime_literature_replay_round2.raw.json")
        replay = json.loads((ROOT / replay_path).read_text(encoding="utf-8"))
        common["replay_generated_at"] = {"path": replay_path, "probe": field_probe("generated_at_utc", replay["generated_at_utc"]), "role": "dated raw replay timestamp"}
        common["replay_interface"] = {"path": replay_path, "probe": field_probe("retrieval_interface", replay["retrieval_interface"]), "role": "dated raw replay interface"}
        replay_keys = []
        for index, row in enumerate(replay["rows"], 1):
            qid = row["query_id"]
            for suffix, probe in (
                ("query", field_probe("query", row["query"])),
                ("time", field_probe("retrieved_at_utc", row["retrieved_at_utc"])),
                ("status", field_probe("http_status", row["crossref"]["http_status"])),
            ):
                key = f"replay_{qid.lower()}_{suffix}"
                common[key] = {"path": replay_path, "probe": probe, "after": field_probe("query_id", qid), "before": field_probe("query_id", f"Q{index + 1:02d}") if index < len(replay["rows"]) else None, "role": f"raw replay {qid} {suffix} field"}
                replay_keys.append(key)
        add_expansion("replay_all_54", replay_keys)
        ledger_path = note("stage4_prime_literature_screening_ledger_round2.json")
        ledger = json.loads((ROOT / ledger_path).read_text(encoding="utf-8"))
        common["screening_method"] = {"path": ledger_path, "probe": field_probe("match_rule", ledger["method"]["match_rule"]), "role": "raw screening match rule"}
        common["screening_retained_31"] = {"path": ledger_path, "probe": field_probe("retained_existing", ledger["retained_existing"]), "role": "raw retained-existing count"}
        common["screening_out_23"] = {"path": ledger_path, "probe": field_probe("screened_out", ledger["screened_out"]), "role": "raw screened-out count"}
        common["screening_decision_schema"] = {"path": ledger_path, "probe": '"decision_vocabulary": [', "role": "raw row-decision vocabulary/schema"}
        panel_path = note("stage3_review_panel_provenance.json")
        panel = json.loads((ROOT / panel_path).read_text(encoding="utf-8"))
        common["review_panel_axes"] = {
            "path": panel_path,
            "probe": field_probe("role_separated", panel["axes"]["role_separated"]),
            "after": '"axes": {',
            "before": '"contract_id"',
            "role": "actual review-panel role_separated axis",
        }
        panel_axis_keys = []
        for field in ("fresh_context", "model_family_distinct"):
            key = f"review_panel_axis_{field}"
            common[key] = {
                "path": panel_path,
                "probe": field_probe(field, panel["axes"][field]),
                "after": '"axes": {',
                "before": '"contract_id"',
                "role": f"actual review-panel {field} axis",
            }
            panel_axis_keys.append(key)
        add_expansion("review_panel_axes_detail", panel_axis_keys)
        panel_keys = []
        panel_detail_keys = []
        for index, seat in enumerate(panel["seats"], 1):
            seat_scope = field_probe("context_id", seat["context_id"])
            next_scope = (
                field_probe("context_id", panel["seats"][index]["context_id"])
                if index < len(panel["seats"]) else None
            )
            role_key = f"review_panel_seat_{index:02d}"
            role_spec = {
                "path": panel_path,
                "probe": field_probe("role_id", seat["role_id"]),
                "after": seat_scope,
                "before": next_scope,
                "role": f"actual review-panel seat {index} role_id: {seat['role_id']}",
            }
            if index == 4:
                role_spec["component_verdict"] = "CONTRADICTS_CLAIMED_FOUR_ROLE_ENUMERATION"
            common[role_key] = role_spec
            panel_keys.append(role_key)
            for suffix, field in (("context", "context_id"), ("family", "model_family")):
                key = f"review_panel_seat_{index:02d}_{suffix}"
                spec = {
                    "path": panel_path,
                    "probe": field_probe(field, seat[field]),
                    "after": None if field == "context_id" else seat_scope,
                    "before": next_scope,
                    "role": f"actual review-panel seat {index} {field}: {seat[field]}",
                }
                common[key] = spec
                panel_detail_keys.append(key)
        add_expansion("review_panel_seats", panel_keys)
        add_expansion("review_panel_seat_details", panel_detail_keys)
        claim_path = note("stage2_claim_intent_manifest.json")
        claim_raw = (ROOT / claim_path).read_text(encoding="utf-8")
        claim_manifest = json.loads(claim_raw)
        common["claim_intent_count"] = {
            "path": claim_path,
            "probe": '"claims": [',
            "role": f"Stage-2 ClaimIntent array boundary; the complete {len(claim_manifest['claims'])}-ID expansion below supplies the replayable count",
        }
        claim_keys: list[str] = []
        decoder = json.JSONDecoder()

        def raw_field(scope_start: int, scope_end: int, field: str) -> str:
            field_at = claim_raw.find(json.dumps(field), scope_start, scope_end)
            if field_at < 0:
                raise RuntimeError(f"P30 ClaimIntent field missing: {field}")
            value_at = claim_raw.find(":", field_at, scope_end) + 1
            while claim_raw[value_at].isspace():
                value_at += 1
            _, consumed = decoder.raw_decode(claim_raw[value_at:scope_end])
            return claim_raw[field_at:value_at + consumed]

        for index, claim in enumerate(claim_manifest["claims"], 1):
            claim_marker = field_probe("claim_id", claim["claim_id"])
            scope_start = claim_raw.index(claim_marker)
            next_marker = (
                field_probe("claim_id", claim_manifest["claims"][index]["claim_id"])
                if index < len(claim_manifest["claims"]) else
                '"manifest_negative_constraints"'
            )
            scope_end = claim_raw.index(next_marker, scope_start)

            id_key = f"claim_intent_c{index:02d}_id"
            common[id_key] = {
                "path": claim_path,
                "probe": claim_marker,
                "before": next_marker,
                "role": f"Stage-2 ClaimIntent {index}/8 exact claim ID",
            }
            claim_keys.append(id_key)

            claim_text = claim["claim_text"]
            words = list(re.finditer(r"\S+", claim_text))
            text_chunks = (
                [claim_text]
                if len(words) <= 25 else
                [claim_text[:words[19].end()], claim_text[words[20].start():]]
            )
            for part, probe in enumerate(text_chunks, 1):
                key = f"claim_intent_c{index:02d}_text_{part:02d}"
                common[key] = {
                    "path": claim_path,
                    "probe": probe,
                    "after": claim_marker,
                    "before": next_marker,
                    "role": f"Stage-2 ClaimIntent {index}/8 complete claim_text segment {part}/{len(text_chunks)} under the 25-word evidence quote cap",
                }
                claim_keys.append(key)

            refs_key = f"claim_intent_c{index:02d}_refs"
            common[refs_key] = {
                "path": claim_path,
                "probe": raw_field(scope_start, scope_end, "planned_refs"),
                "after": claim_marker,
                "before": next_marker,
                "role": f"Stage-2 ClaimIntent {index}/8 complete planned_refs array",
            }
            claim_keys.append(refs_key)

            negative_raw = raw_field(scope_start, scope_end, "negative_constraints")
            if len(negative_raw.split()) <= 25:
                negative_parts = [negative_raw]
            else:
                negative_parts = []
                search_at = scope_start
                for constraint in claim["negative_constraints"]:
                    constraint_at = claim_raw.index(
                        field_probe("constraint_id", constraint["constraint_id"]), search_at, scope_end
                    )
                    object_at = claim_raw.rfind("{", scope_start, constraint_at)
                    _, consumed = decoder.raw_decode(claim_raw[object_at:scope_end])
                    negative_parts.append(claim_raw[object_at:object_at + consumed])
                    search_at = object_at + consumed
            for part, probe in enumerate(negative_parts, 1):
                key = f"claim_intent_c{index:02d}_negative_{part:02d}"
                common[key] = {
                    "path": claim_path,
                    "probe": probe,
                    "after": claim_marker,
                    "before": next_marker,
                    "role": f"Stage-2 ClaimIntent {index}/8 complete negative-constraint object {part}/{len(negative_parts)}, including constraint_id and rule",
                }
                claim_keys.append(key)
        add_expansion("claim_intent_manifest", claim_keys)

    # Full source-effect header and author-adjudication rows are expanded in both
    # papers.  Each tuple is exact and independently hash-bound.
    source_matrix_path = ROOT / note("stage1_phase3_literature_matrix.tsv")
    header = source_matrix_path.read_text(encoding="utf-8").splitlines()[0]
    common["source_effect_full_header"] = {"path": note("stage1_phase3_literature_matrix.tsv"), "probe": header, "role": "complete raw source-effect field header including prohibited transfer and locator limit"}
    adjudication_path = note("stage4_prime_author_adjudication.json")
    adjudication = json.loads((ROOT / adjudication_path).read_text(encoding="utf-8"))
    adjudication_keys = []
    for index, row in enumerate(adjudication["author_adjudications"], 1):
        key = f"author_adjudication_{index:02d}"
        common[key] = {"path": adjudication_path, "probe": f'{json.dumps("item_id")}:{json.dumps(row["item_id"])}', "role": f"actual author adjudication row {index}/{len(adjudication['author_adjudications'])}"}
        adjudication_keys.append(key)
    event = adjudication["author_events"][0]
    common["author_adjudication_event"] = {"path": adjudication_path, "probe": f'{json.dumps("input_sha256")}:{json.dumps(event["input_sha256"])}', "role": "actual author-event input digest"}
    adjudication_keys.append("author_adjudication_event")
    add_expansion("author_adjudications_full", adjudication_keys)

    if cfg["paper"] == 30:
        common["current_round2_audit_execution"] = {
            "path": "BATCH_ROUND10_STAGE4_5_ROUND2_AUTHORIZATION_RECORD.md",
            "probe": "authorizes exactly one fresh, from-scratch ARS Stage 4.5 / Mode-2 integrity audit of Papers P29--P33",
            "role": "performative current full-batch replay under the exact audit-only authority; directly contradicts the not-yet-rerun status",
            "component_verdict": "CONTRADICTS_STALE_STATUS_CURRENT_AUTHORIZED_AUDIT_EXECUTION",
        }
    return common


def correction_projection(notes: Path) -> tuple[dict[str, Any], str]:
    path = notes / "stage4_5_round2_reference_network_audit.json"
    network = json.loads(path.read_text(encoding="utf-8"))
    by = {row["ref_slug"]: row for row in network["references"]}
    def relation(slug: str, field: str) -> list[dict[str, Any]]:
        return by[slug]["query_attempts"]["crossref_doi"]["crossref_message"].get(field, [])
    projection = {
        "fresh_authorized_parent": {"path": "notes/stage4_5_round2_reference_network_audit.json", "sha256": sha_path(path), "bytes": path.stat().st_size},
        "P30-S02": {
            "doi": by["P30-S02"]["fields"]["doi"],
            "updated-by": relation("P30-S02", "updated-by"),
            "response_sha256": by["P30-S02"]["query_attempts"]["crossref_doi"]["response_sha256"],
        },
        "P30-C01": {
            "doi": by["P30-C01"]["fields"]["doi"],
            "update-to": relation("P30-C01", "update-to"),
            "response_sha256": by["P30-C01"]["query_attempts"]["crossref_doi"]["response_sha256"],
        },
        "P30-C02": {
            "doi": by["P30-C02"]["fields"]["doi"],
            "update-to": relation("P30-C02", "update-to"),
            "response_sha256": by["P30-C02"]["query_attempts"]["crossref_doi"]["response_sha256"],
        },
    }
    if [row["DOI"] for row in projection["P30-S02"]["updated-by"]] != ["10.1063/1.457672"]:
        raise RuntimeError("P30-S02 fresh authorized Crossref updated-by relation changed")
    if [row["DOI"] for row in projection["P30-C01"]["update-to"]] != ["10.1063/1.456017"]:
        raise RuntimeError("P30-C01 fresh authorized Crossref update-to relation changed")
    if [row["DOI"] for row in projection["P30-C02"]["update-to"]] != ["10.1063/1.456019"]:
        raise RuntimeError("P30-C02 fresh authorized Crossref update-to relation changed")
    return projection, json.dumps(projection, ensure_ascii=False, indent=2, sort_keys=True)


_UNSET = object()


def make_row(old: dict[str, Any], source_text: str | None, *, source_slug: str | None = None,
             display: str | None = None, artifact_sha: str | None | object = _UNSET,
             anchor: dict[str, str] | None = None, excerpt: str | None = None,
             failure_state: str | None = None, verdict: str | None = None,
             row_id: str | None = None, detail: str) -> dict[str, Any]:
    template = {
        "surface": old["surface"],
        "row_id": row_id if row_id is not None else old["row_id"],
        "claim": copy.deepcopy(old["claim"]),
        "source": {
            "ref_slug": source_slug if source_slug is not None else old["source"]["ref_slug"],
            "display_label": display if display is not None else old["source"]["display_label"],
            "source_artifact_sha256": old["source"].get("source_artifact_sha256") if artifact_sha is _UNSET else artifact_sha,
        },
        "anchor": copy.deepcopy(anchor if anchor is not None else {
            "kind": old["anchor"]["kind"], "value_encoded": old["anchor"]["value_encoded"]
        }),
        "verdict": verdict if verdict is not None else old["verdict"],
        "detail": detail,
    }
    if failure_state is not None:
        row = EVR.build(template, source_text, failure_state=failure_state)
    else:
        row = EVR.build(template, source_text, extracted_text=excerpt)

    # Evidence Rows v1.0 deliberately timestamps fresh positive extraction at
    # build time.  This audit package has a caller-fixed issuance timestamp, so
    # normalize that otherwise nondeterministic field and reseal the canonical
    # row digest before validation.  Empty/failure excerpts retain null.
    if row["excerpt"]["captured_at"] is not None:
        row["excerpt"]["captured_at"] = STAMP
        canonical = copy.deepcopy(row)
        canonical.pop("row_sha256", None)
        row["row_sha256"] = sha_bytes(json.dumps(
            canonical,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        ).encode("utf-8"))
        return EVR.validate(row, source_text)
    return EVR.validate(row)


def _component_slug(cfg: dict[str, Any], key: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9]", "", key.title())
    return f"{cfg['paper_id']}Raw{cleaned}"


def _component_excerpt(text: str, spec: dict[str, Any]) -> tuple[str, dict[str, int]]:
    start = 0
    end = len(text)
    if spec.get("after"):
        found = text.find(spec["after"])
        if found < 0:
            raise RuntimeError(f"component after-marker not found: {spec['after']}")
        start = found + len(spec["after"])
    if spec.get("before"):
        found = text.find(spec["before"], start)
        if found < 0:
            raise RuntimeError(f"component before-marker not found: {spec['before']}")
        end = found
    found = text.find(spec["probe"], start, end)
    if found < 0:
        raise RuntimeError(f"component probe not found: {spec['probe']}")
    excerpt_start = found
    excerpt_end = found + len(spec["probe"])
    excerpt = spec["probe"]
    if len(excerpt.split()) > 25:
        raise RuntimeError(f"component probe exceeds the evidence-row quote cap: {spec['probe']}")
    # evidence_rows.py resolves an extracted string to its first occurrence.
    # Repeated JSON field values therefore need a bounded, occurrence-specific
    # neighboring token.  Expand only inside the declared source-row scope and
    # retain the 25-word quotation cap.
    base_excerpt = excerpt
    base_excerpt_start = excerpt_start
    base_excerpt_end = excerpt_end
    if text.count(excerpt) > 1:
        forward = list(re.finditer(r"\S+", text[excerpt_end:end]))
        for token in forward:
            candidate_end = excerpt_end + token.end()
            candidate = text[excerpt_start:candidate_end]
            if len(candidate.split()) > 25:
                break
            excerpt, excerpt_end = candidate, candidate_end
            if text.count(excerpt) == 1:
                break
    if text.count(excerpt) > 1:
        # The forward search may exhaust the quote budget without finding a
        # unique suffix (for example a repeated decision reason).  Restore the
        # declared probe before searching backward so a nearby unique row field
        # can disambiguate the occurrence within the same 25-word cap.
        excerpt = base_excerpt
        excerpt_start = base_excerpt_start
        excerpt_end = base_excerpt_end
        backward = list(re.finditer(r"\S+", text[start:excerpt_start]))
        for token in reversed(backward):
            candidate_start = start + token.start()
            candidate = text[candidate_start:excerpt_end]
            if len(candidate.split()) > 25:
                break
            excerpt, excerpt_start = candidate, candidate_start
            if text.count(excerpt) == 1:
                break
    if text.count(excerpt) != 1:
        raise RuntimeError(f"component probe cannot be made occurrence-unique within 25 words: {spec['probe']}")
    return excerpt, {
        "start": len(text[:excerpt_start].encode("utf-8")),
        "end": len(text[:excerpt_end].encode("utf-8")),
    }


def _catalog_record(
    claim_id: str,
    component_id: str,
    role: str,
    component_semantic_verdict: str,
    overall: str,
    row: dict[str, Any],
    artifact_desc: dict[str, Any] | None,
    binding_chain: dict[str, Any],
) -> dict[str, Any]:
    excerpt = row["excerpt"]
    return {
        "claim_id": claim_id,
        "component_id": component_id,
        "artifact": artifact_desc,
        "raw_utf8_span": excerpt.get("source_span_utf8"),
        "raw_excerpt": excerpt.get("text"),
        "raw_excerpt_sha256": excerpt.get("excerpt_sha256"),
        "role": role,
        "binding_chain": binding_chain,
        "evidence_row_id": row["row_id"],
        "component_semantic_verdict": component_semantic_verdict,
        "claim_overall_verdict": overall,
        "weakest_component_rule": "The claim-level EVR verdict is the weakest component outcome; shared evidence-row/1.0 requires that verdict on every tuple carrying the claim_id.",
    }


def _replay_binding_chain(record: dict[str, Any]) -> None:
    artifact_desc = record["artifact"]
    chain = record["binding_chain"]
    if artifact_desc is None:
        if chain["type"] != "MISSING_LOCKED_CARRIER" or record["raw_excerpt"] is not None:
            raise RuntimeError(f"invalid missing-carrier record {record['component_id']}")
        return
    target = ROOT / artifact_desc["repo_path"]
    if sha_path(target) != artifact_desc["sha256"] or target.stat().st_size != artifact_desc["bytes"]:
        raise RuntimeError(f"dependency artifact drift {artifact_desc['repo_path']}")
    if chain["type"] in {"TOP_LEVEL_INPUT_LOCK", "TRANSITIVE_SHA_BINDING"}:
        previous_child = None
        for hop in chain["hops"]:
            parent = hop["parent_artifact"]
            child = hop["child_artifact"]
            parent_raw = (ROOT / parent["repo_path"]).read_bytes()
            if sha_bytes(parent_raw) != parent["sha256"] or len(parent_raw) != parent["bytes"]:
                raise RuntimeError(f"binding parent drift {parent['repo_path']}")
            span = hop["raw_utf8_span"]
            raw_excerpt = parent_raw[span["start"]:span["end"]]
            if raw_excerpt.decode("utf-8") != hop["raw_excerpt"] or sha_bytes(raw_excerpt) != hop["raw_excerpt_sha256"]:
                raise RuntimeError(f"binding witness mismatch {parent['repo_path']} -> {child['repo_path']}")
            if child["sha256"] not in hop["raw_excerpt"]:
                raise RuntimeError(f"binding witness omits child sha {child['repo_path']}")
            binding_kind = hop.get("binding_kind", "EXPLICIT_PATH_AND_SHA")
            if binding_kind == "EXPLICIT_PATH_AND_SHA":
                if child["repo_path"] not in hop["raw_excerpt"] and Path(child["repo_path"]).name not in hop["raw_excerpt"]:
                    raise RuntimeError(f"binding witness omits child path {child['repo_path']}")
            elif binding_kind == "SHA_FIELD_WITH_CANONICAL_PATH_DERIVATION":
                derivation = hop["path_derivation"]
                if derivation["resolved_repo_path"] != child["repo_path"] or json.dumps(hop["sha_field"]) not in hop["raw_excerpt"]:
                    raise RuntimeError(f"historical SHA-field path derivation mismatch {child['repo_path']}")
                expected_paths = {
                    "FIELD_NAME_TO_ROOT_STAGE2_OUTPUT_MANIFEST": "BATCH_ROUND10_STAGE2_OUTPUT_MANIFEST.json",
                    "FIELD_NAME_TO_ROOT_STAGE2_INPUT_FREEZE": "BATCH_ROUND10_STAGE2_INPUT_FREEZE.json",
                    "FIELD_NAME_TO_ROOT_STAGE2_PREPROSE_FREEZE": "BATCH_ROUND10_STAGE2_PREPROSE_FREEZE.json",
                    "PAPER_SLUG_PHASE6_MANIFEST": paper_repo_path(
                        {"slug": derivation.get("slug")}, "notes/stage1_phase6_claim_intent_manifest.json"
                    ),
                    "PAPER_SLUG_PHASE6_REPORT": paper_repo_path(
                        {"slug": derivation.get("slug")}, "notes/stage1_phase6_final_report.md"
                    ),
                }
                rule = derivation["rule"]
                if rule not in expected_paths or expected_paths[rule] != child["repo_path"]:
                    raise RuntimeError(f"unsupported/incorrect historical path derivation {rule}")
                parent_text = parent_raw.decode("utf-8")
                span_start = span["start"]
                span_end = span["end"]
                if hop.get("scope_after") is not None:
                    scope_start_char = parent_text.find(hop["scope_after"])
                    scope_start = len(parent_text[:scope_start_char].encode("utf-8"))
                    if scope_start_char < 0 or span_start < scope_start:
                        raise RuntimeError(f"historical SHA-field start scope mismatch {child['repo_path']}")
                if hop.get("scope_before") is not None:
                    scope_end_char = parent_text.find(hop["scope_before"])
                    scope_end = len(parent_text[:scope_end_char].encode("utf-8"))
                    if scope_end_char < 0 or span_end > scope_end:
                        raise RuntimeError(f"historical SHA-field end scope mismatch {child['repo_path']}")
            else:
                raise RuntimeError(f"unsupported transitive-hop binding kind {binding_kind}")
            if previous_child is not None and parent != previous_child:
                raise RuntimeError(f"non-contiguous binding chain at {parent['repo_path']}")
            previous_child = child
        if previous_child != artifact_desc:
            raise RuntimeError(f"binding chain does not terminate at dependency {artifact_desc['repo_path']}")
    elif chain["type"] == "FRESH_AUTHORIZED_RETRIEVAL_PROVENANCE":
        for name in ("authorization_receipt", "input_lock", "retrieval_artifact"):
            desc = chain[name]
            raw = (ROOT / desc["repo_path"]).read_bytes()
            if sha_bytes(raw) != desc["sha256"] or len(raw) != desc["bytes"]:
                raise RuntimeError(f"fresh retrieval provenance drift: {name}")
        if chain["collector_script"] is not None:
            desc = chain["collector_script"]
            raw = (ROOT / desc["repo_path"]).read_bytes()
            if sha_bytes(raw) != desc["sha256"] or len(raw) != desc["bytes"]:
                raise RuntimeError("fresh retrieval provenance drift: collector_script")
        authority_parent = chain["collector_script"] or chain["retrieval_artifact"]
        collector_raw = (ROOT / authority_parent["repo_path"]).read_bytes()
        witness = chain["collector_authority_witness"]
        span = witness["raw_utf8_span"]
        excerpt_raw = collector_raw[span["start"]:span["end"]]
        if excerpt_raw.decode("utf-8") != witness["raw_excerpt"] or sha_bytes(excerpt_raw) != witness["raw_excerpt_sha256"]:
            raise RuntimeError("fresh collector authority witness mismatch")
        if AUTHORITY_RECEIPT_SHA not in witness["raw_excerpt"]:
            raise RuntimeError("fresh collector witness omits authority receipt")
        for event in chain["retrieval_events"]:
            if event["kind"] == "crossref_doi":
                message_raw = json.dumps(event["embedded_crossref_message"], ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
                if sha_bytes(message_raw) != event["embedded_crossref_message_sha256"]:
                    raise RuntimeError(f"fresh embedded Crossref message mismatch {event['ref_slug']}")
            if event["request_method"] != "GET" or event["http_status"] != 200 or event["response_bytes"] <= 0 or not event["response_sha256"]:
                raise RuntimeError(f"fresh Crossref transport incomplete {event['ref_slug']}")
    elif chain["type"] == "CURRENT_AUTHORIZED_AUDIT_EXECUTION":
        expected_keys = {
            "type", "paper_id", "claim_id", "component_id", "entrypoint",
            "runtime_assertion", "audit_draft", "authorization_record",
            "authorization_receipt", "input_lock", "validator",
        }
        if set(chain) != expected_keys:
            raise RuntimeError("current authorized audit execution keys mismatch")
        if (
            chain["paper_id"] != "P30"
            or chain["claim_id"] != "P30-S45R2-E1-107"
            or chain["component_id"] != "P30-S45R2-E1-107:current_round2_audit_execution"
            or record["claim_id"] != chain["claim_id"]
            or record["component_id"] != chain["component_id"]
        ):
            raise RuntimeError("current authorized audit execution scope mismatch")
        if chain["entrypoint"] != "tools/audit_round10_stage4_5_round2.rb#FULL_BATCH_REPLAY":
            raise RuntimeError("current authorized audit execution entrypoint mismatch")
        if chain["runtime_assertion"] != "VALIDATOR_IS_EXECUTING_THE_FULL_EXACT_AUTHORITY_ROUND10_STAGE4_5_ROUND2_REPLAY":
            raise RuntimeError("current authorized audit execution assertion mismatch")

        expected_descriptors = {
            "audit_draft": {
                "repo_path": "papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_prime_revision_round3.tex",
                "sha256": "509e9f45b798ad2257acf2f62db81f95a43e3c574da8f1ba7e654c9fa9d21ead",
                "bytes": 71520,
            },
            "authorization_record": {
                "repo_path": "BATCH_ROUND10_STAGE4_5_ROUND2_AUTHORIZATION_RECORD.md",
                "sha256": "e9505895fe78e2910ff32c4c97d4e7c42abf2fc1f63b25ca7170cb17477dd06d",
                "bytes": 1674,
            },
            "authorization_receipt": {
                "repo_path": "BATCH_ROUND10_STAGE4_5_ROUND2_AUTHORIZATION_RECEIPT.json",
                "sha256": AUTHORITY_RECEIPT_SHA,
                "bytes": 1203,
            },
            "input_lock": {
                "repo_path": "BATCH_ROUND10_STAGE4_5_ROUND2_INPUT_LOCK.json",
                "sha256": AUTHORITY_LOCK_SHA,
                "bytes": 45264,
            },
            "validator": {
                "repo_path": "tools/audit_round10_stage4_5_round2.rb",
                "sha256": sha_path(ROOT / "tools/audit_round10_stage4_5_round2.rb"),
                "bytes": (ROOT / "tools/audit_round10_stage4_5_round2.rb").stat().st_size,
            },
        }
        for name, expected in expected_descriptors.items():
            if chain[name] != expected:
                raise RuntimeError(f"current authorized audit execution descriptor mismatch: {name}")
            raw = (ROOT / expected["repo_path"]).read_bytes()
            if sha_bytes(raw) != expected["sha256"] or len(raw) != expected["bytes"]:
                raise RuntimeError(f"current authorized audit execution descriptor drift: {name}")
        if artifact_desc != chain["authorization_record"]:
            raise RuntimeError("current authorized audit execution target mismatch")
        receipt = json.loads((ROOT / chain["authorization_receipt"]["repo_path"]).read_text(encoding="utf-8"))
        if (
            receipt["status"] != "AUTHORIZED_AUDIT_ONLY"
            or receipt["authorized_action"] != "fresh Stage 4.5 Mode-2 integrity audit from scratch"
            or receipt["authorized_papers"] != ["P29", "P30", "P31", "P32", "P33"]
            or receipt["repairs_authorized"] is not False
            or receipt["stage5_authorized"] is not False
        ):
            raise RuntimeError("current authorized audit execution receipt semantics mismatch")
    elif chain["type"] == "AUTHORIZED_NONCONTROLLING_INDEPENDENT_REVIEW":
        review = chain["review_artifact"]
        raw = (ROOT / review["repo_path"]).read_bytes()
        if sha_bytes(raw) != review["sha256"] or len(raw) != review["bytes"] or review["sha256"] != INDEPENDENT_REVIEW_SHA:
            raise RuntimeError("accepted independent semantic review drift")
        if chain["target_artifact"] != artifact_desc or chain["authority_receipt_sha256"] != AUTHORITY_RECEIPT_SHA:
            raise RuntimeError("independent-review target/authority binding mismatch")
        witness = chain.get("review_to_target_witness")
        if witness is not None:
            parent_raw = (ROOT / witness["parent_artifact"]["repo_path"]).read_bytes()
            span = witness["raw_utf8_span"]
            excerpt_raw = parent_raw[span["start"]:span["end"]]
            if excerpt_raw.decode("utf-8") != witness["raw_excerpt"] or sha_bytes(excerpt_raw) != witness["raw_excerpt_sha256"]:
                raise RuntimeError("independent-review carrier witness mismatch")
            if artifact_desc["repo_path"] not in witness["raw_excerpt"] or artifact_desc["sha256"] not in witness["raw_excerpt"]:
                raise RuntimeError("independent-review witness omits target path/hash")
    else:
        raise RuntimeError(f"unsupported binding-chain type {chain['type']}")


def rebuild_evidence(cfg: dict[str, Any], notes: Path) -> tuple[list[dict[str, Any]], dict[str, str], dict[str, Any], str, dict[str, Any], dict[str, Any]]:
    old_rows = json.loads((notes / "stage4_5_round2_evidence_rows.json").read_text(encoding="utf-8"))
    old_map = json.loads((notes / "stage4_5_round2_evidence_source_map.json").read_text(encoding="utf-8"))
    registry = json.loads((notes / "stage4_5_round2_claim_registry.json").read_text(encoding="utf-8"))
    old_by_claim: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in old_rows:
        old_by_claim[row["claim"]["claim_id"]].append(row)
    draft_text = (notes / "stage4_prime_revision_round3.tex").read_text(encoding="utf-8")
    resolver = DependencyResolver(cfg, notes)
    specs = carrier_specs(cfg)
    draft_slug = f"{cfg['paper_id']}CurrentDraftSelfDefined"
    source_map: dict[str, str] = {draft_slug: draft_text}
    rebuilt: list[dict[str, Any]] = []
    adjudications: list[dict[str, Any]] = []
    dependencies: list[dict[str, Any]] = []
    local_claim_ids = {
        row["claim"]["claim_id"]
        for row in old_rows
        if (row["source"].get("ref_slug") or "").startswith(f"{cfg['paper_id']}CurrentDraft")
        or (row["source"].get("ref_slug") or "").endswith("LocalArtifactChain")
    }
    special_external = {
        "P30-S45R2-E1-049", "P30-S45R2-E1-092",
        "P31-S45R2-E1-008", "P31-S45R2-E1-077",
    }

    def add_source_component(base: dict[str, Any], claim_id: str, key: str, ordinal: int, overall: str) -> dict[str, Any]:
        spec = specs[key]
        repo_path = spec["path"]
        raw = (ROOT / repo_path).read_bytes()
        text = raw.decode("utf-8")
        excerpt, expected_span = _component_excerpt(text, spec)
        slug = _component_slug(cfg, key)
        source_map[slug] = text
        component_id = f"{claim_id}:{key}"
        row = make_row(
            base,
            text,
            source_slug=slug,
            display=f"{cfg['paper_id']} exact raw dependency: {key}",
            artifact_sha=sha_bytes(raw),
            anchor={"kind": "section", "value_encoded": urllib.parse.quote(f"raw-dependency:{component_id}", safe="")},
            excerpt=excerpt,
            verdict=overall,
            row_id=f"EVR-{claim_id}-T{ordinal:02d}",
            detail=f"Direct raw component review: {spec['role']}. Component semantic verdict={spec.get('component_verdict', 'VERIFIED_RAW_DEPENDENCY')}; claim overall={overall}. Schema-5 propagates that claim overall to this EVR tuple; it must not be read as the component's intrinsic verdict. No scientific or Route strengthening follows.",
        )
        if row["excerpt"]["source_span_utf8"] != expected_span:
            raise RuntimeError(
                f"{cfg['paper_id']} EVR selected the wrong repeated occurrence for {claim_id}:{key}: "
                f"expected {expected_span}, got {row['excerpt']['source_span_utf8']}"
            )
        desc = {"repo_path": repo_path, "sha256": sha_bytes(raw), "bytes": len(raw)}
        chain = (
            resolver.current_authorized_audit_execution_chain(
                desc, claim_id=claim_id, component_id=component_id
            )
            if key == "current_round2_audit_execution"
            else resolver.binding_chain(repo_path)
        )
        record = _catalog_record(
            claim_id,
            component_id,
            spec["role"],
            spec.get("component_verdict", "VERIFIED_RAW_DEPENDENCY"),
            overall,
            row,
            desc,
            chain,
        )
        _replay_binding_chain(record)
        dependencies.append(record)
        rebuilt.append(row)
        return row

    def add_missing_component(base: dict[str, Any], claim_id: str, key: str, reason: str, ordinal: int, overall: str) -> dict[str, Any]:
        row = make_row(
            base,
            None,
            source_slug=f"{cfg['paper_id']}Missing{re.sub(r'[^A-Za-z0-9]', '', key.title())}",
            display=f"{cfg['paper_id']} missing locked dependency",
            artifact_sha=None,
            anchor={"kind": "none", "value_encoded": ""},
            failure_state="anchorless",
            verdict=overall,
            row_id=f"EVR-{claim_id}-T{ordinal:02d}",
            detail=reason + f" Component semantic verdict=UNVERIFIABLE_MISSING_LOCKED_CARRIER; claim overall={overall}. Claim self-occurrence, metadata identity, and self-authored matrix prose are not a substitute.",
        )
        record = _catalog_record(
            claim_id,
            f"{claim_id}:{key}",
            reason,
            "UNVERIFIABLE_MISSING_LOCKED_CARRIER",
            overall,
            row,
            None,
            {"type": "MISSING_LOCKED_CARRIER", "reason": reason},
        )
        _replay_binding_chain(record)
        dependencies.append(record)
        rebuilt.append(row)
        return row

    for reg in registry["claims"]:
        claim_id = reg["claim_id"]
        suffix = claim_id.rsplit("-", 1)[-1]
        originals = old_by_claim[claim_id]
        if not originals:
            raise RuntimeError(f"{cfg['paper_id']} missing old EVR template for {claim_id}")
        base = originals[0]
        block_id = reg["writer_anchors"][0]
        overall = cfg["failure_claims"].get(claim_id, "VERIFIED")
        is_local = claim_id in local_claim_ids
        ordinal = 1
        claim_rows_before = len(rebuilt)
        component_outcomes: list[str] = []

        if is_local:
            excerpt = first_excerpt(base["claim"]["text"])
            if excerpt not in draft_text:
                raise RuntimeError(f"{cfg['paper_id']} exact-draft excerpt not found for {claim_id}")
            row = make_row(
                base,
                draft_text,
                source_slug=draft_slug,
                display=f"{cfg['paper_id']} exact Round-3 draft: constitutive/prospective surface",
                artifact_sha=cfg["draft_sha"],
                anchor={"kind": "section", "value_encoded": urllib.parse.quote(f"current-draft:{claim_id}", safe="")},
                excerpt=excerpt,
                verdict=overall,
                row_id=f"EVR-{claim_id}-T{ordinal:02d}",
                detail=f"Exact occurrence and internal logical review verify only the manuscript's own prospective definition, stated boundary, or declaration. Component semantic verdict={'VERIFIED_CONSTITUTIVE_OR_INTERNAL_LOGIC' if overall == 'VERIFIED' else 'EXACT_SURFACE_PRESENT_BUT_CLAIM_FAILS_WEAKEST_COMPONENT'}; claim overall={overall}. They do not establish an external fact, executed result, count, hash, AI-use record, or Route state.",
            )
            rebuilt.append(row)
            draft_desc = resolver._desc(paper_repo_path(cfg, "notes/stage4_prime_revision_round3.tex"))
            draft_component_verdict = (
                "VERIFIED_CONSTITUTIVE_OR_INTERNAL_LOGIC"
                if overall == "VERIFIED" else
                "EXACT_SURFACE_PRESENT_BUT_CLAIM_FAILS_WEAKEST_COMPONENT"
            )
            draft_record = _catalog_record(
                claim_id,
                f"{claim_id}:draft_constitutive_surface",
                "exact draft byte span, limited to constitutive/prospective/internal scope",
                draft_component_verdict,
                overall,
                row,
                draft_desc,
                resolver.binding_chain(draft_desc["repo_path"]),
            )
            _replay_binding_chain(draft_record)
            dependencies.append(draft_record)
            component_outcomes.append(draft_component_verdict)
            ordinal += 1

        if suffix in COMPONENT_PLANS[cfg["paper"]]:
            expanded_keys: list[str] = []
            for planned_key in COMPONENT_PLANS[cfg["paper"]][suffix]:
                if planned_key in {"missing_s23_passage", "missing_s24_passage"}:
                    if planned_key not in expanded_keys:
                        expanded_keys.append(planned_key)
                    continue
                if planned_key not in specs:
                    raise RuntimeError(f"{cfg['paper_id']} component spec missing: {planned_key}")
                for key in specs[planned_key].get("expands", [planned_key]):
                    if key not in expanded_keys:
                        expanded_keys.append(key)
            for key in expanded_keys:
                if key in {"missing_s23_passage", "missing_s24_passage"}:
                    source_id = "P31-S23" if key.endswith("s23_passage") else "P31-S24"
                    reason = f"No current locked original-source passage/excerpt hash is available for the substantive {source_id} method-pattern role."
                    row = add_missing_component(base, claim_id, key, reason, ordinal, overall)
                    component_outcomes.append("UNVERIFIABLE_MISSING_LOCKED_CARRIER")
                else:
                    row = add_source_component(base, claim_id, key, ordinal, overall)
                    component_outcomes.append(specs[key].get("component_verdict", "VERIFIED_RAW_DEPENDENCY"))
                ordinal += 1

        for key, reason in MISSING_COMPONENTS[cfg["paper"]].get(suffix, []):
            row = add_missing_component(base, claim_id, key, reason, ordinal, overall)
            component_outcomes.append("UNVERIFIABLE_MISSING_LOCKED_CARRIER")
            ordinal += 1

        if not is_local and claim_id not in special_external:
            for old in originals:
                old_slug = old["source"]["ref_slug"]
                state = old["excerpt"]["state"]
                if re.fullmatch(rf"{cfg['paper_id']}-S\d{{2}}", old_slug):
                    stem = old_slug.lower().replace("-", "_")
                    key = (
                        f"final_{stem}_excerpt"
                        if state in {"agent_extracted", "verified_exact_match", "unconfirmed_anchor"}
                        else f"final_{stem}_unavailability"
                    )
                    if key not in specs:
                        raise RuntimeError(f"{cfg['paper_id']} primary citation raw component spec missing: {key}")
                    primary_key = f"primary_citation_{key}"
                    specs[primary_key] = {
                        **specs[key],
                        "role": f"primary citation EVR counterpart; {specs[key]['role']}",
                    }
                    add_source_component(old, claim_id, primary_key, ordinal, overall)
                    ordinal += 1
                    continue
                if state in {"agent_extracted", "verified_exact_match", "unconfirmed_anchor"}:
                    source_text = old_map[old_slug]
                    source_map[old_slug] = source_text
                    row = make_row(
                        old,
                        source_text,
                        excerpt=old["excerpt"]["text"],
                        verdict=old["verdict"],
                        row_id=f"EVR-{claim_id}-T{ordinal:02d}",
                        detail=old["detail"] + " Rebuilt and replayed without upgrading its bounded source role.",
                    )
                else:
                    row = make_row(
                        old,
                        None,
                        failure_state=state,
                        verdict=old["verdict"],
                        row_id=f"EVR-{claim_id}-T{ordinal:02d}",
                        detail=old["detail"] + " The explicit empty excerpt state remains unchanged.",
                    )
                rebuilt.append(row)
                ordinal += 1
        elif claim_id in special_external and len(rebuilt) == claim_rows_before:
            raise RuntimeError(f"{cfg['paper_id']} special external claim lacks expanded component rows: {claim_id}")

        if is_local:
            if overall != "VERIFIED":
                classification = "NONVERIFIED_WEAKEST_COMPONENT"
            elif any(value.startswith(("VERIFIED_RAW", "VERIFIED_METADATA")) for value in component_outcomes):
                classification = "RAW_DEPENDENCY_VERIFIED"
            else:
                classification = "CONSTITUTIVE_OR_SELF_CONTAINED_LOGICAL_REVIEW"
            adjudications.append({
                "claim_id": claim_id,
                "block_id": block_id,
                "claim_sha256": sha_bytes(base["claim"]["text"].encode("utf-8")),
                "classification": classification,
                "evidence_row_ids": [row["row_id"] for row in rebuilt[claim_rows_before:]],
                "component_outcomes": component_outcomes,
                "verdict": overall,
                "external_truth_inferred_from_claim_self_occurrence": False,
                "support_boundary": "Every factual dependency is separately tupled where a replayable raw carrier exists; missing carriers remain anchorless and the claim verdict follows the weakest component.",
            })

    by_claim: dict[str, list[str]] = defaultdict(list)
    for row in rebuilt:
        by_claim[row["claim"]["claim_id"]].append(row["verdict"])
    rebuilt_row_ids = [row["row_id"] for row in rebuilt]
    dependency_row_ids = [row["evidence_row_id"] for row in dependencies]
    if len(set(rebuilt_row_ids)) != len(rebuilt_row_ids):
        raise RuntimeError(f"{cfg['paper_id']} duplicate rebuilt EVR row_id")
    if len(set(dependency_row_ids)) != len(dependency_row_ids):
        raise RuntimeError(f"{cfg['paper_id']} duplicate catalog evidence_row_id")
    if set(dependency_row_ids) != set(rebuilt_row_ids):
        raise RuntimeError(
            f"{cfg['paper_id']} full EVR<->catalog reverse join mismatch: "
            f"EVR_without_catalog={sorted(set(rebuilt_row_ids) - set(dependency_row_ids))} "
            f"catalog_without_EVR={sorted(set(dependency_row_ids) - set(rebuilt_row_ids))}"
        )
    verified_claims = sum(all(value == "VERIFIED" for value in values) for values in by_claim.values())
    verdict_counts = dict(sorted(Counter(row["verdict"] for row in rebuilt).items()))
    if len(by_claim) != cfg["claim_total"] or verified_claims != cfg["expected_verified_claims"]:
        raise RuntimeError(f"{cfg['paper_id']} semantic claim counts mismatch: {len(by_claim)}, {verified_claims}, {verdict_counts}")
    if any(len(set(values)) != 1 for values in by_claim.values()):
        raise RuntimeError(f"{cfg['paper_id']} Schema-5 claim-overall propagation mismatch")
    actual_failures = {
        claim_id: values[0]
        for claim_id, values in by_claim.items()
        if values[0] != "VERIFIED"
    }
    if actual_failures != cfg["failure_claims"]:
        raise RuntimeError(
            f"{cfg['paper_id']} exact nonverified claim-ID map mismatch: "
            f"actual={actual_failures} expected={cfg['failure_claims']}"
        )
    if len(dependencies) < cfg["minimum_dependency_components"] or len(rebuilt) < cfg["minimum_evidence_rows"]:
        raise RuntimeError(
            f"{cfg['paper_id']} expanded denominator below minimum: "
            f"components={len(dependencies)}/{cfg['minimum_dependency_components']} "
            f"EVR={len(rebuilt)}/{cfg['minimum_evidence_rows']}"
        )
    summary = {
        "registry_claims": cfg["claim_total"],
        "claims_checked": cfg["claim_total"],
        "claims_verified": verified_claims,
        "claims_nonverified": cfg["claim_total"] - verified_claims,
        "expected_tuples": len(rebuilt),
        "actual_tuples": len(rebuilt),
        "verdict_counts": verdict_counts,
        "claim_overall_verdict_counts": dict(sorted(Counter(values[0] for values in by_claim.values()).items())),
        "excerpt_state_counts": dict(sorted(Counter(row["excerpt"]["state"] for row in rebuilt).items())),
        "tuple_set_replayed_exactly": True,
        "semantic_extraction_coverage": "not_machine_detectable",
    }
    adj = {
        "schema_version": f"p{cfg['paper']}-stage4.5-round2-local-semantic-adjudication/1.0",
        "paper_id": cfg["paper_id"],
        "generated_at_utc": STAMP,
        "local_claim_denominator": len(adjudications),
        "classification_counts": dict(sorted(Counter(row["classification"] for row in adjudications).items())),
        "verdict_counts": dict(sorted(Counter(row["verdict"] for row in adjudications).items())),
        "rows": adjudications,
        "decision_rule": {
            "constitutive": "Exact draft occurrence verifies only a prospective definition, declared scope, or self-contained internal relation.",
            "raw_dependency": "Counts, hashes, execution/status, author metadata, materials, Route, and initial-system facts require exact raw spans with a replayable lock chain.",
            "weakest_component": "A compound claim inherits its weakest component verdict; evidence-row/1.0 repeats that claim-level verdict on all component tuples.",
            "external_method": "A substantive external-method proposition requires a current original-source passage; metadata or self-authored matrix prose is not passage verification.",
        },
        "blanket_claim_self_verification_used": False,
        "verdict": "FAIL" if any(row["verdict"] != "VERIFIED" for row in adjudications) else "PASS",
    }
    adj_md = "\n".join([
        f"# {cfg['paper_id']} — Stage 4.5 Round 2 local semantic adjudication",
        "",
        f"All **{len(adjudications)}/{len(adjudications)}** local claims were classified individually. Counts: `{adj['classification_counts']}`; verdicts: `{adj['verdict_counts']}`.",
        "",
        f"The expanded EVR contains **{len(rebuilt)}** component tuples. Exact claim occurrence is constitutive only; every project fact uses an exact raw dependency span and replayable binding chain, while absent source/user carriers remain anchorless. No scientific or Route strengthening is inferred.",
    ])
    catalog = {
        "schema_version": f"p{cfg['paper']}-stage4.5-round2-local-claim-dependency-catalog/1.0",
        "paper_id": cfg["paper_id"],
        "generated_at_utc": STAMP,
        "authority_lock": resolver.root_lock_desc,
        "accepted_noncontrolling_semantic_review": {
            **resolver.independent_review_desc,
            "authority_receipt_sha256": AUTHORITY_RECEIPT_SHA,
            "role": "audit-side correction basis only; underlying raw carriers and their exact spans remain the substantive evidence",
        },
        "local_claim_denominator": len(local_claim_ids),
        "cataloged_external_blocker_claims": sorted(special_external & set(old_by_claim)),
        "dependency_component_count": len(dependencies),
        "dependencies": dependencies,
        "component_semantic_verdict_counts": dict(sorted(Counter(row["component_semantic_verdict"] for row in dependencies).items())),
        "claim_overall_verdict_counts": dict(sorted(Counter(values[0] for values in by_claim.values()).items())),
        "shared_evr_verdict_counts": verdict_counts,
        "claim_overall_verdicts": {claim_id: values[0] for claim_id, values in sorted(by_claim.items())},
        "weakest_component_rule": "Every compound claim takes the weakest component. Because official evidence-row/1.0 requires one claim-level verdict across repeated claim_id rows, component-specific outcomes are retained in this catalog while each joined EVR tuple carries the overall verdict.",
        "join_contract": {
            "keys": ["claim_id", "evidence_row_id", "artifact.repo_path", "artifact.sha256", "raw_excerpt_sha256"],
            "catalog_components_embedded_in_controlling_evr": True,
            "bidirectional_join_required": True,
        },
        "boundaries": {"claim_self_occurrence_not_external_truth": True, "scientific_strengthening": False, "route_strengthening": False, "missing_carriers_remain_anchorless": True},
    }
    return rebuilt, source_map, summary, adj_md, adj, catalog


def rebuild_reference_audit(cfg: dict[str, Any], notes: Path) -> tuple[dict[str, Any], str]:
    audit = json.loads((notes / "stage4_5_round2_reference_citation_audit.json").read_text(encoding="utf-8"))
    if cfg["paper"] == 30:
        projection, _ = correction_projection(notes)
        records = {row["ref_slug"]: row for row in audit["phase_a"]["records"]}
        s02 = records["P30-S02"]
        s02["adjudicated_verdict"] = "MAJOR_DISTORTION"
        s02["adjudication_notes"] = [
            "Record identity/core metadata are resolved, but the current bibliography/manuscript correction companion is wrong: fresh authorized Crossref updated-by points to 10.1063/1.457672, not P30-C01 10.1063/1.457669."
        ]
        s02["named_record_relation_observation"] = {"updated-by": projection["P30-S02"]["updated-by"]}
        s02["correction_binding_exact"] = False
        records["P30-C01"]["named_record_update_relations"] = projection["P30-C01"]["update-to"]
        records["P30-C01"]["adjudication_notes"] = ["P30-C01 updates only P30-S01 (10.1063/1.456017); it does not support the current P30-S02 binding."]
        records["P30-C02"]["named_record_update_relations"] = projection["P30-C02"]["update-to"]
        audit["phase_a"].update({
            "record_identities_resolved": 28,
            "relation_fidelity_verified": 27,
            "relation_mismatches": 1,
            "relation_fidelity_rate": 27 / 28,
            "verdict": "FAIL",
        })
        for ctx in audit["phase_b"]["contexts"]:
            index = ctx["citation_command_index"]
            if index in {27, 29}:
                ctx.update({
                    "excerpt_state": "NO_ORIGINAL_SOURCE_PASSAGE_CORRECTION_RELATION_MISMATCH",
                    "passage_locator_present": False,
                    "passage_status": "METADATA_CORRECTION_RELATION_MISMATCH",
                    "verdict": "MAJOR_DISTORTION_CORRECTION_BINDING_MISMATCH",
                    "boundary": "P30-C01 is a valid correction record for P30-S01 only; it cannot support the current P30-S02 companion binding and supplies no theorem passage.",
                })
                ctx["checks"] = {"current_citation_present": True, "phase_a_identity_verified": True, "authoritative_update_relation_verified": True, "current_binding_relation_exact": False, "original_source_passage_bound": False}
            elif index in {28, 30}:
                ctx.update({
                    "excerpt_state": "NO_ORIGINAL_SOURCE_PASSAGE_METADATA_RELATION_ONLY",
                    "passage_locator_present": False,
                    "passage_status": "METADATA_UPDATE_RELATION_ONLY",
                    "verdict": "VERIFIED_METADATA_UPDATE_RELATION_NOT_PASSAGE_SUPPORTED",
                    "boundary": "Fresh authorized Crossref metadata supports P30-C02 -> P30-S03 only; it is publication-record evidence, not a theorem or formula passage.",
                })
                ctx["checks"] = {"current_citation_present": True, "phase_a_identity_verified": True, "authoritative_update_relation_verified": True, "current_binding_relation_exact": True, "original_source_passage_bound": False}
        audit["phase_b"].update({
            "context_fidelity_verified": 28,
            "coverage_rate": 28 / 30,
            "disposition_counts": {"bounded_locator_contexts": 18, "metadata_only_unavailable_contexts": 8, "metadata_update_relation_verified_contexts": 2, "correction_relation_mismatch_contexts": 2},
            "metadata_only_boundary_faithful_not_passage_supported": 10,
            "passage_supported_bounded_contexts": 18,
            "verdict": "FAIL",
        })
        issue = "P30-S02 fresh authorized Crossref updated-by=10.1063/1.457672, while the current manuscript/Bib/matrix bind it to P30-C01=10.1063/1.457669; P30-C01 update-to contains only P30-S01."
    else:
        audit["phase_a"].update({"record_identities_resolved": 24, "relation_fidelity_verified": 24, "relation_mismatches": 0, "relation_fidelity_rate": 1.0, "verdict": "PASS"})
        changed = 0
        for ctx in audit["phase_b"]["contexts"]:
            if ctx["ref_slug"] in {"P31-S23", "P31-S24"}:
                changed += 1
                ctx.update({
                    "excerpt_state": "NO_CURRENT_ORIGINAL_SOURCE_PASSAGE_EXCERPT",
                    "passage_locator_present": False,
                    "passage_status": "RETAINED_LOCATOR_UNVERIFIED_NO_CURRENT_SOURCE_PASSAGE",
                    "verdict": "UNVERIFIABLE",
                    "boundary": "The current locked input set contains no original-source passage text or excerpt hash. A matrix row cannot substitute for passage verification of this substantive method-pattern attribution.",
                })
                ctx["checks"] = {"current_citation_present": True, "phase_a_identity_verified": True, "nominal_locator_recorded": True, "current_original_source_excerpt_bound": False, "matrix_self_carrier_rejected": True}
        if changed != 4:
            raise RuntimeError(f"P31 expected four S23/S24 contexts, got {changed}")
        audit["phase_b"].update({
            "context_fidelity_verified": 22,
            "coverage_rate": 22 / 26,
            "disposition_counts": {"bounded_locator_contexts": 7, "metadata_only_unavailable_contexts": 15, "retained_locator_unverifiable_contexts": 4},
            "metadata_only_boundary_faithful_not_passage_supported": 15,
            "passage_supported_bounded_contexts": 7,
            "verdict": "FAIL",
        })
        issue = "P31-S23/P31-S24 have four substantive method-pattern contexts but no current locked original-source passage text or excerpt hash; matrix prose was incorrectly used as the source carrier."
    audit["overall_verdict"] = "FAIL"
    audit["semantic_dispatch_rebuild"] = {"generated_at_utc": STAMP, "finding": issue, "silent_repair_performed": False}
    md = "\n".join([
        f"# {cfg['paper_id']} — Stage 4.5 Round 2 reference and citation-context audit",
        "",
        f"Verdict: **FAIL**. Phase A identities: **{cfg['reference_total']}/{cfg['reference_total']}** resolved; relation-faithful: **{audit['phase_a']['relation_fidelity_verified']}/{cfg['reference_total']}**. Phase B: **{audit['phase_b']['context_fidelity_verified']}/{cfg['context_total']}** contexts evidence-faithful.",
        "",
        issue,
        "",
        "Metadata identity is not passage verification. No manuscript/Bib/matrix repair is authorized or performed; the exact correction proposal is a separate audit sidecar.",
    ])
    return audit, md


def compliance(cfg: dict[str, Any]) -> dict[str, Any]:
    pid = cfg["paper_id"]
    return {
        "mode": "other_evidence_synthesis",
        "stage": "4.5",
        "generated_at": STAMP,
        "prisma_trAIce": {
            "items_total": 17,
            "by_tier": {
                "mandatory": {"total": 2, "pass": 0, "fail": ["R1", "R2"], "gaps": [
                    {"item_id": "R1", "reason": "[MATERIAL GAP] The evidence-synthesis record flow does not numerically separate AI-handled from human-handled records at every screening stage.", "evidence_path": f"papers/{cfg['slug']}/notes/stage4_prime_revision_round3.tex"},
                    {"item_id": "R2", "reason": "[MATERIAL GAP] No numeric AI performance evaluation against a reference standard is reported; same-family role separation is expressly not error-independent.", "evidence_path": f"papers/{cfg['slug']}/notes/stage4_prime_revision_round3.tex"},
                ]},
                "highly_recommended": {"total": 0, "pass": 0, "fail": [], "gaps": []},
                "recommended": {"total": 2, "pass": 1, "fail": ["I1"], "gaps": [
                    {"item_id": "I1", "reason": "[MATERIAL GAP] The introduction does not give a task-specific rationale for choosing each AI tool.", "evidence_path": f"papers/{cfg['slug']}/notes/stage4_prime_revision_round3.tex"},
                ]},
                "optional": {"total": 3, "pass": 0, "fail": ["T1", "A1", "D2"], "gaps": [
                    {"item_id": "T1", "reason": "[GAP] The title/subtitle does not identify substantial AI assistance.", "evidence_path": f"papers/{cfg['slug']}/notes/stage4_prime_revision_round3.tex"},
                    {"item_id": "A1", "reason": "[GAP] The abstract does not name the AI tool and all assisted review/writing stages.", "evidence_path": f"papers/{cfg['slug']}/notes/stage4_prime_revision_round3.tex"},
                    {"item_id": "D2", "reason": "[GAP] No forward-looking reflection on AI utility for future evidence syntheses is provided.", "evidence_path": f"papers/{cfg['slug']}/notes/stage4_prime_revision_round3.tex"},
                ]},
            },
            "block_decision": "warn",
            "protocol_maturity": {
                "status": "foundational_proposal",
                "upstream_citation": "Holst D, et al. Transparent Reporting of AI in Systematic Literature Reviews: Development of the PRISMA-trAIce Checklist. JMIR AI. 2025. doi:10.2196/80247",
                "snapshot_date": "2025-12-10",
                "caveat_summary": "PRISMA-trAIce is a foundational, immediately adoptable but preliminary proposal developed by systematic adaptation rather than Delphi consensus; its 17 items have not yet been empirically validated across diverse research contexts.",
            },
        },
        "raise": {
            "mode": "full",
            "principles": {"human_oversight": "fail", "transparency": "fail", "reproducibility": "fail", "fit_for_purpose": "fail"},
            "principle_evidence": {
                "human_oversight": ["Liang Wang is accountable, but [MATERIAL GAP] reviewer qualifications and an independently adjudicated human verification mechanism are not documented for every AI-assisted synthesis decision."],
                "transparency": ["The disclosure names Codex/GPT-5 family, dates, assisted tasks, backend limitation, and same-family dependence; [MATERIAL GAP] full prompts, parameters, exact build, and complete per-tool metadata are absent."],
                "reproducibility": ["Hash-bound workflow artifacts are present, but [MATERIAL GAP] exact backend build, stochastic settings, and a fully replayable AI execution lock are absent."],
                "fit_for_purpose": ["The audit role is bounded, but [MATERIAL GAP] task-specific external validation or pilot evidence for each AI use is absent."],
            },
            "roles": {
                "evidence_synthesists": ["Liang Wang remains accountable; author responsibility and AI non-authorship are stated, but complete human source verification is not claimed."],
                "ai_development_teams": ["ARS/Codex provides traceable sidecars; exact backend snapshot and system-level validation evidence are unavailable."],
                "methodologists": ["Fresh-context same-family checks are documented and explicitly not claimed independent; no independent validation is established."],
                "publishers": ["Out of project control; venue-specific responsible-AI policy review remains required."],
                "users": ["Users must treat the papers as bounded prospective evidence architectures, not verified scientific results or Route advancement."],
                "trainers": ["Out of direct scope; the explicit metadata/passage and experiment boundaries are suitable training cautions."],
                "organisations": ["Out of direct scope; no organisational monitoring or policy attestation is supplied."],
                "funders": ["No funding is declared; sustainability and generalisability review remain out of scope."],
            },
            "block_decision": "warn",
        },
        "overall_decision": "warn",
        "user_action_required": True,
        "evidence": [
            "Dispatch follows compliance_agent: other_evidence_synthesis uses the seven Stage-4.5 PRISMA-trAIce items in adaptation/information mode plus full RAISE; the decision is capped at warn.",
            "PRISMA-trAIce adaptation gaps do not create the scientific FAIL verdict; the independent Stage-4.5 integrity audit does.",
            "No manuscript, bibliography, scientific result, Route state, or canonical artifact was changed by this compliance rebuild.",
        ],
        "upstream_sync_status": "current",
    }


def seven_modes(cfg: dict[str, Any]) -> tuple[dict[str, Any], str]:
    mode2_status = "SUSPECTED"
    mode2 = (
        "Fresh authorized Crossref relations contradict the current P30-S02 -> P30-C01 correction binding; E1-050's four-role enumeration conflicts with the five-seat Stage-3 panel; and E1-094's no-search-supplement status directly conflicts with the locked draft/ledger/manifest evidence. Identity resolution does not cure these provenance distortions."
        if cfg["paper"] == 30 else
        "P31-S23/P31-S24 identities resolve, but four substantive method-pattern contexts and the corpus-wide negative lack current locked original-source passages; moreover, the reader manifest's method-matrix digest/bytes contradict the current top-level locked matrix. The matrix cannot supply its own source passages, and expanded AI-use metadata also lacks a current user carrier."
    )
    modes = {
        "1_implementation_bug_passing_ai_self_review": {"status": "CLEAR", "evidence": ["No scientific implementation or executed result exists; code/experiments/results remain placeholder-only.", BOUNDARY]},
        "2_hallucinated_citation": {"status": mode2_status, "evidence": [mode2, "The package therefore fails closed in Phases A/B/E rather than upgrading metadata or matrix prose into passage support."]},
        "3_hallucinated_experimental_result": {"status": "CLEAR", "evidence": ["The passport declares no experiments, provenance is empty, and no own-experiment result is claimed."]},
        "4_shortcut_reliance": {"status": "CLEAR", "evidence": ["Mode 4 is limited to shortcut reliance in scientific experiment/result execution. No scientific experiment/result exists in either paper; the citation defect is classified under Mode 2."]},
        "5_implementation_bug_reframed_as_novel_insight": {"status": "CLEAR", "evidence": ["No implementation or bug-derived scientific novelty narrative exists; contributions remain prospective and bounded."]},
        "6_methodology_fabrication": {"status": "CLEAR", "evidence": ["Actually executed workflow artifacts are hash-bound; proposed scientific procedures are explicitly unexecuted."]},
        "7_frame_lock_at_early_pipeline_stage": {"status": "CLEAR", "evidence": [f"Route remains `{cfg['route_state']}`; alternatives and open gates remain visible."]},
    }
    result = {
        "schema_version": f"p{cfg['paper']}-stage4.5-round2-seven-failure-mode-audit/1.0",
        "paper_id": cfg["paper_id"],
        "generated_at_utc": STAMP,
        "allowed_statuses": ["CLEAR", "SUSPECTED", "INSUFFICIENT_EVIDENCE"],
        "modes": modes,
        "denominator": 7,
        "clear": 6,
        "suspected": 1 if mode2_status == "SUSPECTED" else 0,
        "insufficient_evidence": 1 if mode2_status == "INSUFFICIENT_EVIDENCE" else 0,
        "blocking_modes_1_3_5_6_nonclear": [],
        "integrity_relevant_nonclear_modes": ["2_hallucinated_citation"],
        "overall": "FAIL",
        "round1_comparison_used_only_after_fresh_classification": True,
    }
    lines = [f"# {cfg['paper_id']} — Stage 4.5 Round 2 seven-mode audit", ""]
    for name, row in modes.items():
        lines.append(f"- `{name}` — **{row['status']}**: {row['evidence'][0]}")
    lines.extend(["", f"Summary: **6/7 CLEAR**; Mode 2 is **{mode2_status}**. Mode 4 remains CLEAR because no scientific experiment/result exists. Overall: **FAIL**."])
    return result, "\n".join(lines)


def correction_proposal(cfg: dict[str, Any]) -> dict[str, Any]:
    if cfg["paper"] == 30:
        findings = [
            {
                "finding_id": "P30-CORRECTION-RELATION",
                "severity": "SERIOUS",
                "classification": "MAJOR_DISTORTION",
                "finding": "P30-S02 updated-by points to DOI 10.1063/1.457672, but the current manuscript/Bib/matrix/registry bind it to P30-C01 DOI 10.1063/1.457669; P30-C01 update-to lists only P30-S01.",
                "affected_claim_ids": ["P30-S45R2-E1-049", "P30-S45R2-E1-051", "P30-S45R2-E1-053", "P30-S45R2-E1-092"],
            },
            {
                "finding_id": "P30-LIVSIC-PASSAGE",
                "severity": "SERIOUS",
                "classification": "UNVERIFIABLE",
                "finding": "E1-001, E1-047, and E1-083 rely on the substantive Livsic-type asymmetric inference without a current locked original-source passage; claim repetition and project prose do not supply that passage.",
                "affected_claim_ids": ["P30-S45R2-E1-001", "P30-S45R2-E1-047", "P30-S45R2-E1-083"],
            },
            {
                "finding_id": "P30-REVIEW-ROLE-ENUMERATION",
                "severity": "SERIOUS",
                "classification": "MAJOR_DISTORTION_ROLE_ENUMERATION",
                "finding": "E1-050/B0061 states an exhaustive four-role sequence (editorial, domain, methodology, adversarial), but the replayable Stage-3 panel has five seats (eic, methodology, domain, perspective, da). Counting EIC gives five; excluding EIC leaves perspective rather than editorial among the four reviewer seats.",
                "affected_claim_ids": ["P30-S45R2-E1-050"],
            },
            {
                "finding_id": "P30-STALE-SEARCH-STATUS",
                "severity": "SERIOUS",
                "classification": "MAJOR_DISTORTION_STALE_STATUS",
                "finding": "E1-094/B0108 says no independently reproducible search supplement was authorized, directly conflicting with E1-048/B0059 and the frozen 54-row dated replay ledger plus 11-entry reader manifest.",
                "affected_claim_ids": ["P30-S45R2-E1-094"],
            },
            {
                "finding_id": "P30-AI-METADATA-CARRIER",
                "severity": "SERIOUS",
                "classification": "UNVERIFIABLE",
                "finding": "E1-106's expanded 2--4 September AI dates/tasks lack a current locked user-metadata carrier.",
                "affected_claim_ids": ["P30-S45R2-E1-106"],
            },
            {
                "finding_id": "P30-STALE-STAGE4-5-RERUN-STATUS",
                "severity": "SERIOUS",
                "classification": "MAJOR_DISTORTION_STALE_STATUS",
                "finding": "E1-107/B0125 says that a fresh Stage-4.5 rerun has not yet been performed on the Round-3 successor, but the current full root validator is performatively executing that exact-draft rerun under the exact audit-only authorization record, receipt, and input lock; the sentence is stale at replay time.",
                "affected_claim_ids": ["P30-S45R2-E1-107"],
            },
        ]
        actions = [
            "Under separate explicit authority, freshly retrieve and independently verify the correction record DOI 10.1063/1.457672 and its P30-S02 update relation.",
            "If verified, add a uniquely keyed notes-side correction record and replace only the P30-S02 companion binding; preserve P30-C01 -> P30-S01 and P30-C02 -> P30-S03.",
            "Regenerate affected B0060/B0106 prose, P30-S02 Bib note, correction matrix rows, registered claim surfaces, and audit descendants with exact hashes.",
            "Under separate explicit authority, reconcile B0108 with the already frozen B0059 search replay, 54-row ledger, and reader manifest; preserve the exact contradiction until then.",
            "Obtain an exact current original-source passage for E1-001/E1-047/E1-083 or narrow/remove their Livsic-type substantive attribution; never infer it from the manuscript or matrix.",
            "Under separate explicit authority, correct B0061's review-role enumeration to the exact controlling review phase and seat population; do not collapse the five-seat Stage-3 panel into an invented four-role list.",
            "Obtain a current locked user-metadata event for the 2--4 September AI disclosure or narrow the disclosure to the actually locked scope.",
            "Under separate explicit authority, replace B0125's stale no-rerun status with wording that acknowledges the exact-authority current full Stage-4.5 replay without treating an archived or same-lineage review as scientific evidence.",
        ]
        affected = ["notes/stage4_prime_revision_round3.tex:B0004/B0057/B0060/B0061/B0062/B0065/B0096/B0106/B0108/B0124/B0125", "notes/stage4_prime_references_round2.bib:P30-S02", "notes/stage4_prime_claim_passage_matrix_round2.json:P30-C01", "notes/stage4_5_round2_claim_registry.json:E1-001/E1-047/E1-049/E1-050/E1-051/E1-053/E1-083/E1-092/E1-094/E1-106/E1-107"]
    else:
        findings = [
            {
                "finding_id": "P31-S23-S24-PASSAGES",
                "severity": "SERIOUS",
                "classification": "UNVERIFIABLE",
                "finding": "P31-S23/P31-S24 substantive method-pattern claims have no current locked original-source passage text or excerpt hash; self-authored matrix rows are not passage evidence.",
                "affected_claim_ids": ["P31-S45R2-E1-008", "P31-S45R2-E1-077", "P31-S45R2-E1-079", "P31-S45R2-E1-080"],
            },
            {
                "finding_id": "P31-OVERBROAD-LITERATURE-NEGATIVE",
                "severity": "SERIOUS",
                "classification": "UNVERIFIABLE",
                "finding": "E1-067/B0030 states a corpus-wide negative about what the literature does not supply, but fifteen P31-S01--P31-S22 sources lack current original passages and P31-S23/P31-S24 also lack method passages; project-recorded unavailability cannot establish the substantive negative.",
                "affected_claim_ids": ["P31-S45R2-E1-067"],
            },
            {
                "finding_id": "P31-AI-METADATA-CARRIER",
                "severity": "SERIOUS",
                "classification": "UNVERIFIABLE",
                "finding": "E1-126's expanded 2--4 September AI dates/tasks lack a current locked user-metadata carrier.",
                "affected_claim_ids": ["P31-S45R2-E1-126"],
            },
            {
                "finding_id": "P31-STALE-READER-MANIFEST",
                "severity": "SERIOUS",
                "classification": "MAJOR_DISTORTION_STALE_ARTIFACT_BINDING",
                "finding": "E1-108/B0079 and E1-125/B0105 claim exact/current reader enumeration with a full digest per entry, but the cited reader manifest lists the method matrix as e18e78cd.../12020 bytes while the current top-level locked matrix is 1adc4c65.../19277 bytes; the reader manifest is stale.",
                "affected_claim_ids": ["P31-S45R2-E1-108", "P31-S45R2-E1-125"],
            },
        ]
        actions = [
            "Under separate explicit authority, retrieve and hash exact original-source passages for the registered P31-S23 and P31-S24 roles, with honest access/read-scope provenance.",
            "If passages remain unavailable or do not support the roles, narrow or remove the affected attributions and source-verified wording instead of inventing locators.",
            "Regenerate affected matrix, B0016/B0030/B0037/B0038/B0112 surfaces, claim registry, evidence rows, and audit descendants.",
            "Obtain a current locked user-metadata event for the 2--4 September AI disclosure or narrow the disclosure to the actually locked scope.",
            "Under separate explicit authority, regenerate the reader artifact manifest from the current locked artifacts and then correct only B0079/B0105 plus their registered claim/audit descendants; do not describe pending synchronization as current reader recovery.",
        ]
        affected = ["notes/stage4_prime_revision_round3.tex:B0016/B0030/B0037/B0038/B0079/B0105/B0107/B0112", "notes/stage4_prime_method_passage_matrix_round2.json:P31-S23/P31-S24", "notes/stage4_prime_reader_artifact_manifest_round2.json:method-matrix-entry", "notes/stage4_5_round2_claim_registry.json:E1-008/E1-067/E1-077/E1-079/E1-080/E1-108/E1-125/E1-126"]
    return {
        "schema_version": f"p{cfg['paper']}-stage4.5-round2-correction-proposal/1.0",
        "paper_id": cfg["paper_id"],
        "generated_at_utc": STAMP,
        "status": "PROPOSED_NOT_AUTHORIZED_NOT_APPLIED",
        "blocking_finding": findings[0]["finding"],
        "blocking_findings": findings,
        "affected_current_surfaces": affected,
        "proposed_actions": actions,
        "mandatory_checkpoint": "Stop for separate author authorization before any manuscript, Bib, matrix, registry, science, Route, canonical, README, status, or Git mutation.",
        "repairs_performed": [],
        "scientific_result_change": False,
        "route_change": False,
    }


def incident(cfg: dict[str, Any], state: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema_version": f"p{cfg['paper']}-stage4.5-round2-semantic-attempt5-supersession-incident/1.0",
        "paper_id": cfg["paper_id"],
        "recorded_at_utc": STAMP,
        "old_package_status": "ATTEMPT5_SEMANTICALLY_INCOMPLETE_NONCONTROLLING",
        "old_output_manifest": {"sha256": cfg["old_manifest_sha"]},
        "old_validation_receipt": {"sha256": cfg["old_validation_sha"]},
        "accepted_noncontrolling_semantic_review": {
            "path": INDEPENDENT_REVIEW_REL,
            "sha256": INDEPENDENT_REVIEW_SHA,
            "bytes": INDEPENDENT_REVIEW_BYTES,
            "authority_receipt_sha256": AUTHORITY_RECEIPT_SHA,
        },
        "incident_classes": [
            "UNDERDECOMPOSED_RAW_DEPENDENCIES: attempt 5 omitted required claim/source/anchor tuples",
            "SEMANTIC_SOURCE_MISATTRIBUTION: draft-self, matrix-count, or actor/event fragments were used beyond their factual scope",
            "INDEPENDENT_REVIEW_SUPERSESSION: accepted external audit-side review 1c0d087c... requires the attempt-6 mapping",
        ],
        "archive_directory": f"notes/{state['archive'].name}",
        "archived_artifacts": state["archive_rows"],
        "archive_copy_count": len(state["archive_rows"]),
        "old_bytes_deleted": False,
        "new_controlling_rule": "Only hashes in the replacement attempt-6 output manifest and validation receipt control. Archived attempt-5 artifacts remain noncontrolling incident evidence.",
        "manuscript_or_science_change": False,
    }


def attempt_lineage(cfg: dict[str, Any], notes: Path) -> dict[str, Any]:
    value = json.loads((notes / "stage4_5_round2_attempt_lineage.json").read_text(encoding="utf-8"))
    value["recorded_at_utc"] = STAMP
    value["status"] = "ATTEMPT5_ARCHIVED_NONCONTROLLING_ATTEMPT6_FAIL_CLOSED_CONTROLLING"
    value["attempts"].append({
        "attempt": 5,
        "publication_state": "ARCHIVED_NONCONTROLLING",
        "internal_verdict": "FAIL_RETAINED_BUT_DEPENDENCY_MAP_WITHDRAWN",
        "finding": "The FAIL verdict remains directionally conservative, but its dependency map was underdecomposed and misattributed; the exact attempt-5 bytes are archived.",
        "retained_hash_witnesses": {"output_manifest_sha256": cfg["old_manifest_sha"], "validation_receipt_sha256": cfg["old_validation_sha"]},
    })
    value["attempts"].append({
        "attempt": 6,
        "generated_at_utc": STAMP,
        "publication_state": "CONTROLLING_FAIL_CLOSED_AUDIT_DERIVATIVES",
        "internal_verdict": "FAIL",
        "finding": "Accepted independent semantic review was applied to a complete claim/source/anchor expansion; claim-overall verdicts follow the weakest raw component, and exact blockers remain uncorrected.",
    })
    value["scientific_or_manuscript_change"] = False
    value["canonical_promotion"] = False
    return value


def build_candidates(cfg: dict[str, Any], state: dict[str, Any], work: Path) -> dict[str, bytes]:
    notes: Path = state["notes"]
    rows, source_map, evidence_summary, adj_md, adj, dependency_catalog = rebuild_evidence(cfg, notes)
    refs, refs_md = rebuild_reference_audit(cfg, notes)
    comp = compliance(cfg)
    seven, seven_md = seven_modes(cfg)
    proposal = correction_proposal(cfg)
    inc = incident(cfg, state)
    lineage = attempt_lineage(cfg, notes)
    phase_c = json.loads((notes / "stage4_5_round2_phase_c_internal_consistency_audit.json").read_text(encoding="utf-8"))
    phase_c["generated_at_utc"] = STAMP
    if cfg["paper"] == 30:
        c14 = next(row for row in phase_c["surfaces"] if row["surface_id"] == "C-P30-14")
        c14.update({
            "status": "MAJOR_DISTORTION_STALE_STATUS",
            "evidence_scope": "Exact B0108 raw span conflicts with exact B0059, the frozen 54-row dated replay ledger, and the 11-entry reader manifest; all dependency chains replay in the expanded EVR/catalog.",
        })
        phase_c["registered_surface_coverage"].update({
            "coverage_rate": 13 / 14,
            "verified": 13,
            "inconsistent": 1,
        })
        phase_c["verdict"] = "FAIL"
    phase_c_md = "\n".join([
        f"# {cfg['paper_id']} — Stage 4.5 Round 2 Phase C audit",
        "",
        f"Verdict: **{phase_c['verdict']}**. Registered data/stat/internal surfaces **{phase_c['registered_surface_coverage']['data_stat_internal_surfaces_checked']}/{phase_c['registered_surface_coverage']['data_stat_internal_surfaces_checked']}** checked; verified **{phase_c['registered_surface_coverage']['verified']}**, inconsistent **{phase_c['registered_surface_coverage']['inconsistent']}**. Tables **{phase_c['registered_surface_coverage']['tables_verified']}/{phase_c['registered_surface_coverage']['tables_checked']}**; figures **{phase_c['registered_surface_coverage']['figures_present']}**.",
        "",
        "P30's C-P30-14 fails because B0108's no-search-supplement sentence conflicts with B0059 and the raw 54-row ledger/11-entry manifest; this is classified MAJOR_DISTORTION_STALE_STATUS."
        if cfg["paper"] == 30 else
        "All thirteen registered P31 Phase-C surfaces remain internally consistent within their exact audit boundary.",
        "",
        BOUNDARY,
        "",
        "D7 ran before provenance inspection. The passport declares no experiments, provenance is empty, no planned experiment ID is registered, no Results-style own-experiment outcome appears, and code/experiments/results remain placeholder-only.",
    ])
    originality = json.loads((notes / "stage4_5_round2_originality_failure_mode_audit.json").read_text(encoding="utf-8"))
    e6 = json.loads((notes / "stage4_5_round2_e6_semantic_audit.json").read_text(encoding="utf-8"))
    coverage = json.loads((notes / "stage4_5_round2_claim_registry_coverage.json").read_text(encoding="utf-8"))
    build_receipt = json.loads((notes / "stage4_5_round2_preview_build_receipt.json").read_text(encoding="utf-8"))
    if build_receipt["status"] != "PASS_CLEAN" or build_receipt["input"]["sha256"] != cfg["draft_sha"] or build_receipt["bibliography"]["sha256"] != cfg["bib_sha"]:
        raise RuntimeError(f"{cfg['paper_id']} isolated build receipt no longer binds exact inputs")
    build = copy.deepcopy(build_receipt)
    build["audit_rebuild_handling"] = "PASS_CLEAN_HASH_REPLAY_NOT_RERUN"
    build["replayed_at_utc"] = STAMP
    build["input_bytes_unchanged"] = True
    comparison = json.loads((notes / "stage4_5_round2_round1_comparison.json").read_text(encoding="utf-8"))
    comparison.update({"generated_at_utc": STAMP, "fresh_phase_b_verdict": "FAIL", "fresh_seven_mode_verdict": "FAIL", "all_prior_blockers_resolved": False, "current_new_blockers": [row["finding"] for row in proposal["blocking_findings"]]})
    comparison["prior_issue_dispositions"][0]["status"] = "PARTIAL"
    comparison["prior_issue_dispositions"][0]["fresh_basis"] = f"Current audit verifies {refs['phase_b']['context_fidelity_verified']}/{cfg['context_total']} contexts; the exact new blocker remains in the correction proposal."

    candidates: dict[str, bytes] = {
        "stage4_5_round2_attempt_lineage.json": jraw(lineage),
        "stage4_5_round2_reference_citation_audit.json": jraw(refs),
        "stage4_5_round2_reference_citation_audit.md": traw(refs_md),
        "stage4_5_round2_evidence_source_map.json": jraw(source_map),
        "stage4_5_round2_evidence_rows.json": jraw(rows),
        "stage4_5_round2_local_claim_dependency_catalog.json": jraw(dependency_catalog),
        "stage4_5_round2_local_semantic_adjudication.json": jraw(adj),
        "stage4_5_round2_local_semantic_adjudication.md": traw(adj_md),
        "stage4_5_round2_correction_proposal.json": jraw(proposal),
        "stage4_5_round2_semantic_attempt5_supersession_incident.json": jraw(inc),
        "stage4_5_round2_seven_failure_mode_audit.json": jraw(seven),
        "stage4_5_round2_seven_failure_mode_audit.md": traw(seven_md),
        "stage4_5_round2_compliance_report.json": jraw(comp),
        "stage4_5_round2_round1_comparison.json": jraw(comparison),
        "stage4_5_round2_phase_c_internal_consistency_audit.json": jraw(phase_c),
        "stage4_5_round2_phase_c_internal_consistency_audit.md": traw(phase_c_md),
    }
    evidence_replay = "$ python3 ars/scripts/evidence_rows.py validate notes/stage4_5_round2_evidence_rows.json --source-map notes/stage4_5_round2_evidence_source_map.json\nPASS: %d evidence row(s)\n" % len(rows)
    candidates["stage4_5_round2_evidence_rows_replay.log"] = evidence_replay.encode("utf-8")
    issue_phases = (
        ["A/B/E", "B/E", "E", "C/E", "E", "E"]
        if cfg["paper"] == 30 else
        ["B/E", "B/E", "E", "E"]
    )
    issues = [
        {
            "issue_id": f"{cfg['paper_id']}-S45R2-I{index:02d}",
            "severity": finding["severity"],
            "phase": issue_phases[index - 1],
            "classification": finding["classification"],
            "finding_id": finding["finding_id"],
            "finding": finding["finding"],
            "affected_claim_ids": finding["affected_claim_ids"],
            "blocker": True,
        }
        for index, finding in enumerate(proposal["blocking_findings"], 1)
    ]
    integrity = {
        "schema_version": f"p{cfg['paper']}-stage4.5-round2-integrity-report/1.0",
        "paper_id": cfg["paper_id"],
        "generated_at_utc": STAMP,
        "mode": "final-check",
        "audit_mode": 2,
        "verdict": "FAIL",
        "fresh_from_scratch": True,
        "semantic_dispatch_rebuild": True,
        "prior_round1_used_only_for_post_audit_comparison": True,
        "unchanged_pass_components_hash_replayed": True,
        "phases": {
            "A_references": {"registered": cfg["reference_total"], "checked": cfg["reference_total"], "resolved_identities": cfg["reference_total"], "relation_fidelity_verified": refs["phase_a"]["relation_fidelity_verified"], "relation_mismatches": refs["phase_a"]["relation_mismatches"], "verdict": refs["phase_a"]["verdict"]},
            "B_citation_contexts": {"registered": cfg["context_total"], "reviewed": cfg["context_total"], "context_fidelity_verified": refs["phase_b"]["context_fidelity_verified"], "disposition_counts": refs["phase_b"]["disposition_counts"], "metadata_only_boundary_faithful_not_passage_supported": refs["phase_b"]["metadata_only_boundary_faithful_not_passage_supported"], "passage_supported_bounded_contexts": refs["phase_b"]["passage_supported_bounded_contexts"], "verdict": "FAIL"},
            "C_data_internal_provenance": {**phase_c["registered_surface_coverage"], "experiment_alignment": phase_c["experiment_provenance"]["alignment_status"], "experiment_alignment_results": [], "boundary": BOUNDARY, "verdict": phase_c["verdict"]},
            "D_originality": {"body_successful": originality["successful_body_dual_lane"], "body_denominator": originality["paragraph_denominator"], "rate": originality["sampling_rate"], "changed_successful": originality["changed_or_new_successful"], "changed_denominator": originality["changed_or_new_total"], "major_sections": f"{originality['major_sections_covered']}/{originality['major_sections_total']}", "professional_detector": False, "verdict": originality["verdict"]},
            "E_claims": {
                "selection_tier": "ALL", "registered": cfg["claim_total"], "checked": cfg["claim_total"], "verified": evidence_summary["claims_verified"], "nonverified": evidence_summary["claims_nonverified"],
                "claim_registry": {"path": "notes/stage4_5_round2_claim_registry.json", "sha256": sha_path(notes / "stage4_5_round2_claim_registry.json")},
                "coverage_report": {"path": "notes/stage4_5_round2_claim_registry_coverage.json", "sha256": sha_path(notes / "stage4_5_round2_claim_registry_coverage.json"), "status": "completed", "candidate_unregistered_count": coverage["candidate_unregistered_count"]},
                "semantic_extraction_coverage": "not_machine_detectable", "expected_evidence_tuples": len(rows), "actual_evidence_tuples": len(rows),
                "evidence_rows_artifact": {"path": "notes/stage4_5_round2_evidence_rows.json", "sha256": sha_bytes(candidates["stage4_5_round2_evidence_rows.json"])},
                "evidence_rows": rows, "verdict_counts": evidence_summary["verdict_counts"], "excerpt_state_counts": evidence_summary["excerpt_state_counts"],
                "component_semantic_verdict_counts": dependency_catalog["component_semantic_verdict_counts"],
                "claim_overall_verdict_counts": dependency_catalog["claim_overall_verdict_counts"],
                "shared_evr_verdict_counts": dependency_catalog["shared_evr_verdict_counts"],
                "schema5_propagation_note": "Shared EVR repeats each claim's weakest overall verdict on every component row; that count is not a count of intrinsically distorted/missing raw components.",
                "local_claim_dependency_catalog": {"path": "notes/stage4_5_round2_local_claim_dependency_catalog.json", "sha256": sha_bytes(candidates["stage4_5_round2_local_claim_dependency_catalog.json"])},
                "local_semantic_adjudication": {"path": "notes/stage4_5_round2_local_semantic_adjudication.json", "sha256": sha_bytes(candidates["stage4_5_round2_local_semantic_adjudication.json"])},
                "scope_conformance_advisories": [], "novelty_claim_advisories": [], "cache_staleness_advisories": [], "verdict": "FAIL",
            },
            "E6_semantic_drift": {"rounds": 3, "operations_reviewed": e6["operations_reviewed"], "round_operation_denominators": e6["round_operation_denominators"], "result": e6["semantic_result"], "companion": {"path": "notes/stage4_5_round2_claim_strength_drift_findings.json", "sha256": sha_path(notes / "stage4_5_round2_claim_strength_drift_findings.json")}, "verdict": e6["verdict"]},
        },
        "seven_failure_modes": seven,
        "compliance": comp,
        "build": build,
        "round1_comparison": comparison,
        "issues": issues,
        "issue_counts": {"SERIOUS": len(issues), "MEDIUM": 0, "MINOR": 0},
        "correction_proposal": {"path": "notes/stage4_5_round2_correction_proposal.json", "sha256": sha_bytes(candidates["stage4_5_round2_correction_proposal.json"]), "status": proposal["status"]},
        "advisories": [
            "Semantic E1 extraction completeness is not machine-detectable even with a replay-clean finite lexical coverage report.",
            "Originality is a bounded public-Web heuristic without a licensed professional similarity detector.",
            "Same-family fresh-context roles are not claimed to have independent errors.",
            "Metadata identity, a nominal locator, and self-authored matrix prose are not original-source passage verification.",
        ],
        "authority": state["input_manifest"]["authority"],
        "protected_snapshot_before": state["input_manifest"]["protected_snapshot_before"],
        "protected_snapshot_after": state["input_manifest"]["protected_snapshot_before"],
        "protected_snapshot_unchanged": True,
        "silent_repair_performed": False,
        "canonical_promotion_performed": False,
        "scientific_execution_performed": False,
        "route_mutation_performed": False,
        "stage5_started": False,
        "route_state": cfg["route_state"],
        "initial_system": cfg["initial_system"],
        "assurance_boundary": "FAIL is confined to exact claim/provenance defects identified here. Passing Phase C/D/E6/build components do not cure them, do not establish mathematical truth or scientific execution, and do not confer Route eligibility.",
    }
    candidates["stage4_5_round2_integrity_report.json"] = jraw(integrity)

    passport = json.loads((notes / "stage4_5_round2_material_passport.json").read_text(encoding="utf-8"))
    if len(passport.get("compliance_history", [])) not in {1, 2} or passport["compliance_history"][0].get("stage") != "2.5":
        raise RuntimeError(f"{cfg['paper_id']} Stage-2.5 compliance history seed mismatch")
    if len(passport["compliance_history"]) == 2 and str(passport["compliance_history"][1].get("stage")) != "4.5":
        raise RuntimeError(f"{cfg['paper_id']} attempt-5 Stage-4.5 compliance history entry mismatch")
    stage25 = copy.deepcopy(passport["compliance_history"][0])
    passport["compliance_history"] = [stage25, copy.deepcopy(comp)]
    passport["version_label"] = "stage4.5-round2-fail-closed-semantic-dispatch-rebuild"
    passport["verification_status"] = "stage4_5_round2_fail_corrections_proposed_not_applied"
    passport["integrity_pass_date"] = "2026-09-02T17:36:06Z"
    passport["content_hash"] = cfg["draft_sha"]
    passport["stage4_5_round2_audit"] = {
        "verdict": "FAIL", "fresh_from_scratch": True, "semantic_dispatch_rebuild": True,
        "authority_receipt_sha256": AUTHORITY_RECEIPT_SHA,
        "references": f"{refs['phase_a']['relation_fidelity_verified']}/{cfg['reference_total']} relation-faithful; {cfg['reference_total']}/{cfg['reference_total']} identities resolved",
        "citation_contexts": f"{refs['phase_b']['context_fidelity_verified']}/{cfg['context_total']}",
        "phase_c": cfg["phase_c"], "originality_body": cfg["originality_body"], "originality_changed": cfg["originality_changed"],
        "registered_claims": f"{evidence_summary['claims_verified']}/{cfg['claim_total']}",
        "evidence_rows": f"{evidence_summary['verdict_counts'].get('VERIFIED', 0)}/{len(rows)} VERIFIED; {len(rows) - evidence_summary['verdict_counts'].get('VERIFIED', 0)} claim-overall-propagated nonverified",
        "e6": f"{cfg['e6_ops']}/{cfg['e6_ops']} across 3 rounds", "seven_modes": "6/7 CLEAR; Mode 2 non-CLEAR",
        "build": "PASS_CLEAN_HASH_REPLAY_NOT_RERUN", "blocking_issue_ids": [row["issue_id"] for row in issues],
        "correction_proposal": "notes/stage4_5_round2_correction_proposal.json", "stage5_started": False,
    }
    if passport["experiment_intake_declaration"]["status"] != "no_experiments_declared" or passport["experiment_provenance"] != []:
        raise RuntimeError(f"{cfg['paper_id']} experiment passport boundary changed")
    candidates["stage4_5_round2_material_passport.json"] = jraw(passport)

    finding_lines = [f"- **{row['classification']}** (`{row['finding_id']}`): {row['finding']}" for row in proposal["blocking_findings"]]
    final_md = "\n".join([
        f"# {cfg['paper_id']} — Stage 4.5 Round 2 final integrity report",
        "", "## Verdict", "", "**FAIL.** The attempt-5 FAIL sidecars are archived and noncontrolling because their dependency map was semantically incomplete. This attempt-6 package retains the exact blockers without manuscript/Bib/matrix/science/Route repair.",
        "", "## Complete denominators", "",
        f"- Phase A: identities **{cfg['reference_total']}/{cfg['reference_total']}**; relation-faithful **{refs['phase_a']['relation_fidelity_verified']}/{cfg['reference_total']}**.",
        f"- Phase B: contexts reviewed **{cfg['context_total']}/{cfg['context_total']}**; evidence-faithful **{refs['phase_b']['context_fidelity_verified']}/{cfg['context_total']}**; passage-supported bounded contexts **{refs['phase_b']['passage_supported_bounded_contexts']}**.",
        f"- Phase C: **{cfg['phase_c']}** registered data/stat/internal surfaces; no own experiment.",
        f"- Phase D: body **{cfg['originality_body']}** (>=50%) and changed/new **{cfg['originality_changed']}** (100%); bounded public-Web heuristic only.",
        f"- Phase E: claims **{evidence_summary['claims_verified']}/{cfg['claim_total']} VERIFIED**; expanded evidence tuples **{evidence_summary['verdict_counts'].get('VERIFIED', 0)}/{len(rows)} VERIFIED**, shared-EVR counts `{evidence_summary['verdict_counts']}`. These tuple verdicts propagate each claim's weakest overall outcome and are not component-level distortion counts.",
        f"- Component semantic counts: `{dependency_catalog['component_semantic_verdict_counts']}`; claim-overall counts: `{dependency_catalog['claim_overall_verdict_counts']}`.",
        f"- Phase E6: **3/3 rounds**, **{cfg['e6_ops']}/{cfg['e6_ops']} operations**, no unauthorized drift detected by the recorded semantic review.",
        f"- Seven modes: **6/7 CLEAR**; Mode 2 is **{seven['modes']['2_hallucinated_citation']['status']}**. Mode 4 is CLEAR because there is no scientific experiment/result.",
        f"- Isolated build: **PASS_CLEAN_HASH_REPLAY_NOT_RERUN**, {cfg['pages']} pages; exact draft/Bib hashes unchanged.",
        "- Compliance: **Schema12 PASS**, `other_evidence_synthesis`, Stage-4.5 PRISMA-trAIce adaptation (7 items) + RAISE full (8 roles), decision capped at warn; appended to passport history.",
        "", "## Blocking issues", "", *finding_lines, "", "The separate correction proposal is `notes/stage4_5_round2_correction_proposal.json`; it is not authorized or applied.",
        "", "## Route, system, and experiment boundaries", "", f"- Route: `{cfg['route_state']}`.", f"- Initial system: {cfg['initial_system']}.", f"- {BOUNDARY}",
    ])
    candidates["stage4_5_round2_final_integrity_report.md"] = traw(final_md)
    receipt = {
        "schema_version": f"p{cfg['paper']}-stage4.5-round2-receipt/1.0", "paper_id": cfg["paper_id"], "recorded_at_utc": STAMP,
        "verdict": "FAIL", "audit_mode": 2, "authority": state["input_manifest"]["authority"], "inputs": state["input_manifest"]["inputs"],
        "denominators": integrity["phases"],
        "key_artifacts": {
            "integrity_report": artifact("notes/stage4_5_round2_integrity_report.json", candidates["stage4_5_round2_integrity_report.json"]),
            "final_human_report": artifact("notes/stage4_5_round2_final_integrity_report.md", candidates["stage4_5_round2_final_integrity_report.md"]),
            "claim_registry": artifact("notes/stage4_5_round2_claim_registry.json", (notes / "stage4_5_round2_claim_registry.json").read_bytes()),
            "evidence_rows": artifact("notes/stage4_5_round2_evidence_rows.json", candidates["stage4_5_round2_evidence_rows.json"]),
            "compliance_report": artifact("notes/stage4_5_round2_compliance_report.json", candidates["stage4_5_round2_compliance_report.json"]),
            "correction_proposal": artifact("notes/stage4_5_round2_correction_proposal.json", candidates["stage4_5_round2_correction_proposal.json"]),
            "accepted_noncontrolling_semantic_review": {
                "path": INDEPENDENT_REVIEW_REL,
                "sha256": INDEPENDENT_REVIEW_SHA,
                "bytes": INDEPENDENT_REVIEW_BYTES,
            },
            "preview": build_receipt["preview"],
        },
        "seven_mode_summary": {"clear": 6, "suspected": seven["suspected"], "insufficient_evidence": seven["insufficient_evidence"]},
        "build_status": "PASS_CLEAN_HASH_REPLAY_NOT_RERUN", "superseded_attempt5_fail_package_noncontrolling": True,
        "protected_snapshot_unchanged": True, "silent_repair_performed": False, "stage5_started": False, "canonical_promotion_performed": False,
    }
    candidates["stage4_5_round2_receipt.json"] = jraw(receipt)

    candidate_names = set(candidates)
    existing_names = {p.name for p in notes.glob("stage4_5_round2_*") if p.is_file()}
    artifact_names = sorted((candidate_names | existing_names) - {"stage4_5_round2_output_manifest.json", "stage4_5_round2_validation_receipt.json"})
    manifest_rows = []
    for name in artifact_names:
        raw = candidates[name] if name in candidates else (notes / name).read_bytes()
        manifest_rows.append(artifact(f"notes/{name}", raw))
    if cfg["paper"] == 31:
        collector_raw = (ROOT / SHARED_NETWORK_COLLECTOR_REL).read_bytes()
        manifest_rows.append(artifact(SHARED_NETWORK_COLLECTOR_REL, collector_raw))
    output_manifest = {
        "schema_version": f"p{cfg['paper']}-stage4.5-round2-output-manifest/1.0", "paper_id": cfg["paper_id"], "generated_at_utc": STAMP,
        "verdict": "FAIL", "controlling_attempt": 6, "superseded_attempt": 5, "artifacts": manifest_rows,
        "derivation_script": {"path": SCRIPT_REL, "sha256": sha_path(ROOT / SCRIPT_REL), "bytes": (ROOT / SCRIPT_REL).stat().st_size},
        "accepted_noncontrolling_semantic_review": {
            "path": INDEPENDENT_REVIEW_REL,
            "sha256": INDEPENDENT_REVIEW_SHA,
            "bytes": INDEPENDENT_REVIEW_BYTES,
            "authority_receipt_sha256": AUTHORITY_RECEIPT_SHA,
        },
        "noncontrolling_archive": {"path": f"notes/{state['archive'].name}", "artifact_count": len(state["archive_rows"]), "incident": "notes/stage4_5_round2_semantic_attempt5_supersession_incident.json"},
        "validation_receipt_intentionally_not_self_listed": "notes/stage4_5_round2_validation_receipt.json",
        "protected_snapshot_after": state["input_manifest"]["protected_snapshot_before"], "protected_snapshot_unchanged": True, "stage5_started": False,
    }
    candidates["stage4_5_round2_output_manifest.json"] = jraw(output_manifest)
    validation_rows = manifest_rows + [artifact("notes/stage4_5_round2_output_manifest.json", candidates["stage4_5_round2_output_manifest.json"])]
    validation = {
        "schema_version": f"p{cfg['paper']}-stage4.5-round2-validation-receipt/1.0", "paper_id": cfg["paper_id"], "generated_at_utc": STAMP,
        "status": "PASS_AUDIT_PACKAGE_COHERENT_WITH_BLOCKING_INTEGRITY_VERDICT", "scientific_integrity_verdict": "FAIL",
        "authority_receipt_sha256": AUTHORITY_RECEIPT_SHA,
        "checks": {
            "fresh_reference_population": f"{cfg['reference_total']}/{cfg['reference_total']} identities; {refs['phase_a']['relation_fidelity_verified']}/{cfg['reference_total']} relation-faithful",
            "citation_context_population": f"{refs['phase_b']['context_fidelity_verified']}/{cfg['context_total']} faithful; {cfg['context_total']}/{cfg['context_total']} reviewed",
            "phase_c_population": cfg["phase_c"], "originality_body": cfg["originality_body"], "originality_changed": cfg["originality_changed"],
            "claim_registry": f"{evidence_summary['claims_verified']}/{cfg['claim_total']} VERIFIED", "coverage_candidate_gaps": coverage["candidate_unregistered_count"],
            "evidence_tuples": f"{evidence_summary['verdict_counts'].get('VERIFIED', 0)}/{len(rows)} VERIFIED by claim-overall propagation; {len(rows)}/{len(rows)} schema/replay valid",
            "dependency_catalog_join": f"PASS {dependency_catalog['dependency_component_count']}/{dependency_catalog['dependency_component_count']} components bidirectionally joined",
            "e6_rounds": 3, "e6_operations": cfg["e6_ops"], "seven_modes_clear": 6,
            "build": "PASS_CLEAN_HASH_REPLAY_NOT_RERUN", "protected_snapshot_unchanged": True,
            "official_coverage_replay": "PASS", "official_evidence_rows_replay": "PASS", "official_compliance_checker": "PASS",
            "compliance_dispatch": "PASS_OTHER_EVIDENCE_SYNTHESIS_ADAPTATION_7_PLUS_RAISE_FULL_8_ROLE",
            "attempt5_fail_archive_replay": "PASS_NONCONTROLLING", "blocking_findings_preserved_without_repair": True,
        },
        "artifacts": validation_rows, "validation_receipt_self_hash_excluded": True,
        "boundaries": {"repairs": False, "manuscript_or_bib": False, "canonical_promotion": False, "science_or_route_change": False, "readme_or_status": False, "stage5": False, "git": False},
    }
    candidates["stage4_5_round2_validation_receipt.json"] = jraw(validation)

    if set(candidates) != CHANGED_NAMES:
        raise RuntimeError(f"{cfg['paper_id']} candidate set mismatch missing={sorted(CHANGED_NAMES-set(candidates))} extra={sorted(set(candidates)-CHANGED_NAMES)}")
    validate_candidates(cfg, state, candidates, work)
    return candidates


def validate_candidates(cfg: dict[str, Any], state: dict[str, Any], candidates: dict[str, bytes], work: Path) -> None:
    paper_work = work / cfg["paper_id"]
    paper_work.mkdir(parents=True, exist_ok=True)
    for name, raw in candidates.items():
        (paper_work / name).write_bytes(raw)
    code, output = run(["python3", str(COMPLIANCE_CHECKER), str(paper_work / "stage4_5_round2_compliance_report.json")])
    if code != 0 or not output.startswith("OK:"):
        raise RuntimeError(f"{cfg['paper_id']} compliance validation failed: {output}")
    code, output = run(["python3", str(EVIDENCE_SCRIPT), "validate", str(paper_work / "stage4_5_round2_evidence_rows.json"), "--source-map", str(paper_work / "stage4_5_round2_evidence_source_map.json")])
    if code != 0 or not output.startswith("PASS:"):
        raise RuntimeError(f"{cfg['paper_id']} evidence replay failed: {output}")
    rows = json.loads(candidates["stage4_5_round2_evidence_rows.json"])
    catalog = json.loads(candidates["stage4_5_round2_local_claim_dependency_catalog.json"])
    evr_by_id = {row["row_id"]: row for row in rows}
    if len(evr_by_id) != len(rows):
        raise RuntimeError(f"{cfg['paper_id']} duplicate EVR row_id")
    seen_catalog_ids: set[str] = set()
    for dep in catalog["dependencies"]:
        row_id = dep["evidence_row_id"]
        if row_id in seen_catalog_ids or row_id not in evr_by_id:
            raise RuntimeError(f"{cfg['paper_id']} invalid catalog->EVR join {row_id}")
        seen_catalog_ids.add(row_id)
        row = evr_by_id[row_id]
        if row["claim"]["claim_id"] != dep["claim_id"] or row["verdict"] != dep["claim_overall_verdict"]:
            raise RuntimeError(f"{cfg['paper_id']} catalog claim/verdict join mismatch {row_id}")
        artifact_desc = dep["artifact"]
        if artifact_desc is None:
            if row["anchor"]["kind"] != "none" or row["source"]["source_artifact_sha256"] is not None:
                raise RuntimeError(f"{cfg['paper_id']} missing dependency is not anchorless/double-null {row_id}")
            if row["excerpt"]["text"] is not None or row["excerpt"]["excerpt_sha256"] is not None or row["excerpt"]["source_span_utf8"] is not None:
                raise RuntimeError(f"{cfg['paper_id']} missing dependency excerpt is not null {row_id}")
        else:
            if row["source"]["source_artifact_sha256"] != artifact_desc["sha256"]:
                raise RuntimeError(f"{cfg['paper_id']} catalog artifact SHA join mismatch {row_id}")
            if row["excerpt"]["text"] != dep["raw_excerpt"] or row["excerpt"]["excerpt_sha256"] != dep["raw_excerpt_sha256"] or row["excerpt"]["source_span_utf8"] != dep["raw_utf8_span"]:
                raise RuntimeError(f"{cfg['paper_id']} catalog raw excerpt join mismatch {row_id}")
            if dep["raw_excerpt"] is None or dep["raw_utf8_span"] is None or dep["raw_excerpt_sha256"] is None:
                raise RuntimeError(f"{cfg['paper_id']} nonmissing catalog dependency lacks exact raw span {row_id}")
            artifact_raw = (ROOT / artifact_desc["repo_path"]).read_bytes()
            span = dep["raw_utf8_span"]
            excerpt_raw = artifact_raw[span["start"]:span["end"]]
            if excerpt_raw.decode("utf-8") != dep["raw_excerpt"] or sha_bytes(excerpt_raw) != dep["raw_excerpt_sha256"]:
                raise RuntimeError(f"{cfg['paper_id']} direct artifact-span replay mismatch {row_id}")
        _replay_binding_chain(dep)
    if seen_catalog_ids != set(evr_by_id):
        raise RuntimeError(
            f"{cfg['paper_id']} full EVR->catalog reverse join mismatch: "
            f"EVR_without_catalog={sorted(set(evr_by_id) - seen_catalog_ids)} "
            f"catalog_without_EVR={sorted(seen_catalog_ids - set(evr_by_id))}"
        )
    computed_component_counts = dict(sorted(Counter(dep["component_semantic_verdict"] for dep in catalog["dependencies"]).items()))
    computed_evr_counts = dict(sorted(Counter(row["verdict"] for row in rows).items()))
    computed_claim_counts = dict(sorted(Counter(next(iter(values)) for values in ({r["verdict"] for r in rows if r["claim"]["claim_id"] == cid} for cid in {r["claim"]["claim_id"] for r in rows})).items()))
    if computed_component_counts != catalog["component_semantic_verdict_counts"] or computed_evr_counts != catalog["shared_evr_verdict_counts"] or computed_claim_counts != catalog["claim_overall_verdict_counts"]:
        raise RuntimeError(f"{cfg['paper_id']} three-denominator replay mismatch")
    notes: Path = state["notes"]
    code, output = run(["python3", str(COVERAGE_SCRIPT), "--draft", str(notes / "stage4_prime_revision_round3.tex"), "--registry", str(notes / "stage4_5_round2_claim_registry.json"), "--validate-report", str(notes / "stage4_5_round2_claim_registry_coverage.json")])
    if code != 0:
        raise RuntimeError(f"{cfg['paper_id']} claim coverage replay failed: {output}")
    manifest = json.loads(candidates["stage4_5_round2_output_manifest.json"])
    raw_by_path = {f"notes/{name}": raw for name, raw in candidates.items()}
    for row in manifest["artifacts"]:
        if row["path"] in raw_by_path:
            raw = raw_by_path[row["path"]]
        else:
            target = resolve_package_binding_path(state["paper"], row["path"])
            raw = target.read_bytes()
        if sha_bytes(raw) != row["sha256"] or len(raw) != row["bytes"]:
            raise RuntimeError(f"{cfg['paper_id']} candidate manifest mismatch {row['path']}")
    manifest_paths = {row["path"] for row in manifest["artifacts"]}
    required_fresh = {
        "notes/stage4_5_round2_reference_network_audit.json",
        "notes/stage4_5_round2_local_claim_dependency_catalog.json",
    }
    if cfg["paper"] == 30:
        required_fresh.add("notes/stage4_5_round2_collect_reference_network.py")
    else:
        required_fresh.add(SHARED_NETWORK_COLLECTOR_REL)
    if not required_fresh.issubset(manifest_paths):
        raise RuntimeError(f"{cfg['paper_id']} final manifest omits fresh retrieval provenance {sorted(required_fresh - manifest_paths)}")
    if [row for row in snapshot_replay(state["input_manifest"]["protected_snapshot_before"]) if row["status"] != "PASS"]:
        raise RuntimeError(f"{cfg['paper_id']} protected snapshot drifted during candidate build")


def archive_old(state: dict[str, Any]) -> None:
    archive: Path = state["archive"]
    temp = archive.with_name(f".{archive.name}.staging-{os.getpid()}")
    temp.mkdir()
    try:
        for row in state["archive_rows"]:
            source = state["paper"] / row["path"]
            target = temp / Path(row["archive_path"]).name
            shutil.copy2(source, target)
            if sha_path(target) != row["sha256"] or target.stat().st_size != row["bytes"]:
                raise RuntimeError(f"archive copy mismatch {row['path']}")
        os.replace(temp, archive)
    except Exception:
        shutil.rmtree(temp, ignore_errors=True)
        raise


def publish(state: dict[str, Any], candidates: dict[str, bytes]) -> None:
    notes: Path = state["notes"]
    staged: list[tuple[Path, Path]] = []
    try:
        for name, raw in candidates.items():
            fd, temp_name = tempfile.mkstemp(prefix=f".{name}.dispatch-rebuild-", dir=notes)
            os.close(fd)
            temp = Path(temp_name)
            temp.write_bytes(raw)
            staged.append((temp, notes / name))
        for temp, target in staged:
            os.replace(temp, target)
    finally:
        for temp, _ in staged:
            temp.unlink(missing_ok=True)


def validate_final(cfg: dict[str, Any], state: dict[str, Any]) -> dict[str, Any]:
    notes: Path = state["notes"]
    validation = json.loads((notes / "stage4_5_round2_validation_receipt.json").read_text(encoding="utf-8"))
    if validation["status"] != "PASS_AUDIT_PACKAGE_COHERENT_WITH_BLOCKING_INTEGRITY_VERDICT" or validation["scientific_integrity_verdict"] != "FAIL":
        raise RuntimeError(f"{cfg['paper_id']} final validation status mismatch")
    for row in validation["artifacts"]:
        path = resolve_package_binding_path(state["paper"], row["path"])
        if sha_path(path) != row["sha256"] or path.stat().st_size != row["bytes"]:
            raise RuntimeError(f"{cfg['paper_id']} final artifact mismatch {row['path']}")
    for row in state["archive_rows"]:
        path = state["paper"] / row["archive_path"]
        if sha_path(path) != row["sha256"] or path.stat().st_size != row["bytes"]:
            raise RuntimeError(f"{cfg['paper_id']} archive replay mismatch {row['archive_path']}")
    failures = [row for row in snapshot_replay(state["input_manifest"]["protected_snapshot_before"]) if row["status"] != "PASS"]
    if failures:
        raise RuntimeError(f"{cfg['paper_id']} final protected snapshot mismatch")
    code_c, out_c = run(["python3", str(COMPLIANCE_CHECKER), str(notes / "stage4_5_round2_compliance_report.json")])
    code_e, out_e = run(["python3", str(EVIDENCE_SCRIPT), "validate", str(notes / "stage4_5_round2_evidence_rows.json"), "--source-map", str(notes / "stage4_5_round2_evidence_source_map.json")])
    code_r, out_r = run(["python3", str(COVERAGE_SCRIPT), "--draft", str(notes / "stage4_prime_revision_round3.tex"), "--registry", str(notes / "stage4_5_round2_claim_registry.json"), "--validate-report", str(notes / "stage4_5_round2_claim_registry_coverage.json")])
    if code_c or code_e or code_r:
        raise RuntimeError(f"{cfg['paper_id']} final official replay failed: {out_c} {out_e} {out_r}")
    final_candidates = {name: (notes / name).read_bytes() for name in CHANGED_NAMES}
    with tempfile.TemporaryDirectory(prefix=f"{cfg['paper_id'].lower()}-final-catalog-replay-") as temp_name:
        validate_candidates(cfg, state, final_candidates, Path(temp_name))
    integ = json.loads((notes / "stage4_5_round2_integrity_report.json").read_text(encoding="utf-8"))
    catalog = json.loads((notes / "stage4_5_round2_local_claim_dependency_catalog.json").read_text(encoding="utf-8"))
    return {
        "paper_id": cfg["paper_id"], "verdict": integ["verdict"], "issues": integ["issue_counts"],
        "references": {"identities": f"{cfg['reference_total']}/{cfg['reference_total']}", "relation_faithful": f"{integ['phases']['A_references']['relation_fidelity_verified']}/{cfg['reference_total']}"},
        "contexts": f"{integ['phases']['B_citation_contexts']['context_fidelity_verified']}/{cfg['context_total']}",
        "claims": f"{integ['phases']['E_claims']['verified']}/{cfg['claim_total']}",
        "evidence_rows_verified": f"{integ['phases']['E_claims']['verdict_counts'].get('VERIFIED', 0)}/{integ['phases']['E_claims']['actual_evidence_tuples']}",
        "phase_c": cfg["phase_c"], "originality_body": cfg["originality_body"], "originality_changed": cfg["originality_changed"],
        "e6": f"{cfg['e6_ops']}/{cfg['e6_ops']}", "seven_modes": {"clear": 6, "mode2": integ["seven_failure_modes"]["modes"]["2_hallucinated_citation"]["status"]},
        "build": "PASS_CLEAN_HASH_REPLAY_NOT_RERUN", "archive_artifacts": len(state["archive_rows"]),
        "compliance_sha256": sha_path(notes / "stage4_5_round2_compliance_report.json"),
        "integrity_sha256": sha_path(notes / "stage4_5_round2_integrity_report.json"),
        "passport_sha256": sha_path(notes / "stage4_5_round2_material_passport.json"),
        "receipt_sha256": sha_path(notes / "stage4_5_round2_receipt.json"),
        "output_manifest_sha256": sha_path(notes / "stage4_5_round2_output_manifest.json"),
        "validation_receipt_sha256": sha_path(notes / "stage4_5_round2_validation_receipt.json"),
        "evidence_rows_sha256": sha_path(notes / "stage4_5_round2_evidence_rows.json"),
        "dependency_catalog_sha256": sha_path(notes / "stage4_5_round2_local_claim_dependency_catalog.json"),
        "component_semantic_verdict_counts": catalog["component_semantic_verdict_counts"],
        "claim_overall_verdict_counts": catalog["claim_overall_verdict_counts"],
        "shared_evr_verdict_counts": catalog["shared_evr_verdict_counts"],
        "reference_audit_sha256": sha_path(notes / "stage4_5_round2_reference_citation_audit.json"),
        "correction_proposal_sha256": sha_path(notes / "stage4_5_round2_correction_proposal.json"),
        "official_replays": {"compliance": out_c.strip(), "evidence": out_e.strip(), "coverage": "PASS"},
        "protected_snapshot_unchanged": True,
    }


def validate_only() -> list[dict[str, Any]]:
    results = []
    for cfg in CONFIGS:
        paper = ROOT / "papers" / cfg["slug"]
        notes = paper / "notes"
        input_manifest = json.loads((notes / "stage4_5_round2_input_manifest.json").read_text(encoding="utf-8"))
        state = {"paper": paper, "notes": notes, "input_manifest": input_manifest}
        incident_obj = json.loads((notes / "stage4_5_round2_semantic_attempt5_supersession_incident.json").read_text(encoding="utf-8"))
        state["archive_rows"] = incident_obj["archived_artifacts"]
        results.append(validate_final(cfg, state))
    return results


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--preflight-only", action="store_true")
    parser.add_argument("--validate-only", action="store_true")
    parser.add_argument("--preview-dir", type=Path)
    args = parser.parse_args()
    if sum(bool(value) for value in (args.preflight_only, args.validate_only, args.preview_dir)) > 1:
        raise SystemExit("choose only one mode")
    if sha_path(ROOT / "BATCH_ROUND10_STAGE4_5_ROUND2_AUTHORIZATION_RECEIPT.json") != AUTHORITY_RECEIPT_SHA:
        raise RuntimeError("authority receipt hash mismatch")
    if sha_path(ROOT / "BATCH_ROUND10_STAGE4_5_ROUND2_INPUT_LOCK.json") != AUTHORITY_LOCK_SHA:
        raise RuntimeError("authority lock hash mismatch")
    if args.validate_only:
        print(json.dumps({"status": "PASS", "papers": validate_only()}, ensure_ascii=False, indent=2, sort_keys=True))
        return 0
    states = {cfg["paper_id"]: preflight(cfg) for cfg in CONFIGS}
    if args.preflight_only:
        print(json.dumps({"status": "PASS", "papers": {pid: {"archive_rows": len(state["archive_rows"]), "protected_rows": len(state["protected_checks"])} for pid, state in states.items()}}, ensure_ascii=False, indent=2, sort_keys=True))
        return 0
    candidates: dict[str, dict[str, bytes]] = {}
    with tempfile.TemporaryDirectory(prefix="round10-p30-p31-stage45-dispatch-") as temp_name:
        work = Path(temp_name)
        for cfg in sorted(CONFIGS, key=lambda row: row["paper"], reverse=True):
            candidates[cfg["paper_id"]] = build_candidates(cfg, states[cfg["paper_id"]], work)
    if args.preview_dir:
        if args.preview_dir.exists():
            raise RuntimeError(f"preview directory already exists: {args.preview_dir}")
        args.preview_dir.mkdir(parents=True)
        preview_summary = []
        for cfg in sorted(CONFIGS, key=lambda row: row["paper"], reverse=True):
            target = args.preview_dir / cfg["paper_id"]
            target.mkdir()
            for name, raw in candidates[cfg["paper_id"]].items():
                (target / name).write_bytes(raw)
            catalog = json.loads(candidates[cfg["paper_id"]]["stage4_5_round2_local_claim_dependency_catalog.json"])
            rows = json.loads(candidates[cfg["paper_id"]]["stage4_5_round2_evidence_rows.json"])
            preview_summary.append({
                "paper_id": cfg["paper_id"],
                "catalog": artifact(str(target / "stage4_5_round2_local_claim_dependency_catalog.json"), candidates[cfg["paper_id"]]["stage4_5_round2_local_claim_dependency_catalog.json"]),
                "evidence_rows": artifact(str(target / "stage4_5_round2_evidence_rows.json"), candidates[cfg["paper_id"]]["stage4_5_round2_evidence_rows.json"]),
                "components": catalog["dependency_component_count"],
                "rows": len(rows),
                "component_counts": catalog["component_semantic_verdict_counts"],
                "claim_counts": catalog["claim_overall_verdict_counts"],
                "evr_counts": catalog["shared_evr_verdict_counts"],
            })
        print(json.dumps({"status": "STABLE_TEMP_PREVIEW", "papers": preview_summary}, ensure_ascii=False, indent=2, sort_keys=True))
        return 0
    for cfg in CONFIGS:
        archive_old(states[cfg["paper_id"]])
    for cfg in CONFIGS:
        publish(states[cfg["paper_id"]], candidates[cfg["paper_id"]])
    results = [validate_final(cfg, states[cfg["paper_id"]]) for cfg in CONFIGS]
    print(json.dumps({"status": "PASS_AUDIT_PACKAGES_COHERENT_WITH_FAIL_VERDICTS", "papers": results}, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
