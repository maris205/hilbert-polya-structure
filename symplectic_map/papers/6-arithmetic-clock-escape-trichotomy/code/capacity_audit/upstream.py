"""Independent immutable binding to completed Paper-3 and Paper-4 packages."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .protocol import (
    CANDIDATE_ID,
    load_strict_json_file,
    regular_file_within,
    sha256_file,
)


EXPECTED_UPSTREAMS = {
    "PAPER3_INTEGRAL_HENON_MULTIPLIERS": {
        "paper_relative": "../4-integral-henon-multipliers",
        "candidate_id": "integral_area_henon_multiplier_support_v1",
        "source_lock_sha256": "3ae1623304b2cc68403cfc20de545edce7cea6af6e2df9c1cd56d4ae8f38d269",
        "proof_package_sha256": "2c536656bef0d98bfc0fd8fbf60ae04ac3e39943a178630a199203d52429afdd",
        "final_result_manifest_sha256": "e47c93ccc49cf37ffa5bab63bed758be9c1288500f459d539de806d7e4229863",
        "manifest_kind": "PAPER3_HENON",
        "pipeline_schema": "HENON_PAPER_PIPELINE_STATE_V1",
        "paper_id": "integral-area-henon-multiplier-support-v1",
        "pipeline_state_sha256": "61ec1ff8c39102bd12e651a0735a978b6e38f290c4f3ad9d5f9e9384e9d5592f",
        "final_integrity_sha256": "29d271c5b63e5d207830fafe0818101cea3994c32bd73989aef2b671377f1b43",
        "final_pdf_sha256": "f7368ecfa03929143311516303bb1c7a1a97e77869cb245f47e82e8e91a63156",
        "final_review_sha256": "9cd87c6110ee821886d220726aafcd816b60b312858c7a5b1da3df9719d6f8e9",
    },
    "PAPER4_ALGEBRAIC_ACTION_CLOCKS": {
        "paper_relative": "../5-algebraic-action-clocks",
        "candidate_id": "algebraic_exact_action_clock_obstruction_v1",
        "source_lock_sha256": "d15f5084900aa043e80ada46d3ce22772cd10bbdb348d4fcb000aa9fa2ca49d7",
        "proof_package_sha256": "c579e2da093a8ab588a5818bab0df59a47804792fcdfa338777f48e1bd1a1214",
        "final_result_manifest_sha256": "6b3dbfed68dbd058056c35139756d5ccbb4e9f3b9a263ccaddef64bb183326e7",
        "manifest_kind": "PAPER4_ACTION",
        "pipeline_schema": "ALGEBRAIC_ACTION_PAPER_PIPELINE_STATE_V2",
        "paper_id": "normalized-algebraic-action-prime-log-certificate-v1",
        "pipeline_state_sha256": "2e49c5025360648c8eedd2c1110a21c835b970194f3d96fb6fdfb35377f1904e",
        "final_integrity_sha256": "6239c69703d555f9607db6409817870d438a934089491295c0df24b2d0038d1e",
        "final_pdf_sha256": "871197f5a385f68accf6d3ba7876e5df830e9eef43b4bf9e9ae52a3edb7bc996",
        "final_review_sha256": "ca3d789bdcc3b4040be0338238a6f67cde5c76ea59a4f7b7f90d74484c060d71",
    },
}

BINDING_KEYS = {
    "id",
    "candidate_id",
    "paper_relative",
    "source_lock_path",
    "source_lock_sha256",
    "proof_package_path",
    "proof_package_sha256",
    "final_result_manifest_path",
    "final_result_manifest_sha256",
    "pipeline_state_path",
    "pipeline_state_sha256",
    "final_integrity_path",
    "final_integrity_sha256",
    "final_pdf_path",
    "final_pdf_sha256",
    "final_review_path",
    "final_review_sha256",
    "status",
}

ARTIFACT_PATHS = {
    "source_lock_path": "experiments/source_lock.json",
    "proof_package_path": "notes/PROOF_PACKAGE.md",
    "final_result_manifest_path": "results/final_result_manifest.json",
    "pipeline_state_path": "paper/PIPELINE_STATE.json",
    "final_integrity_path": "paper/FINAL_INTEGRITY.md",
    "final_pdf_path": "paper/paper_final.pdf",
    "final_review_path": "paper/reviews/round2_review.md",
}


def _paper3_manifest_valid(payload: Any, expected: dict[str, Any]) -> bool:
    if not isinstance(payload, dict):
        return False
    artifacts = payload.get("artifacts")
    linkage = payload.get("official_report_linkage")
    checks = linkage.get("checks") if isinstance(linkage, dict) else None
    return bool(
        payload.get("candidate_id") == expected["candidate_id"]
        and payload.get("source_lock_sha256") == expected["source_lock_sha256"]
        and payload.get("execution_status") == "PASS"
        and payload.get("all_must_run_pass") is True
        and payload.get("forbidden_data_used") is False
        and payload.get("external_prime_tables_accessed") is False
        and payload.get("riemann_zero_data_accessed") is False
        and isinstance(checks, dict)
        and checks
        and all(value is True for value in checks.values())
        and isinstance(artifacts, dict)
        and artifacts.get("notes/PROOF_PACKAGE.md", {}).get("sha256") == expected["proof_package_sha256"]
        and isinstance(artifacts.get("results/CODE_REVIEW.md", {}).get("sha256"), str)
    )


def _paper4_manifest_valid(payload: Any, expected: dict[str, Any]) -> bool:
    if not isinstance(payload, dict):
        return False
    validation = payload.get("required_artifact_validation")
    files = payload.get("files")
    semantic = validation.get("semantic_checks") if isinstance(validation, dict) else None
    return bool(
        payload.get("algorithm") == "sha256"
        and isinstance(validation, dict)
        and validation.get("pass") is True
        and isinstance(semantic, dict)
        and semantic
        and all(value is True for value in semantic.values())
        and isinstance(files, dict)
        and files.get("experiments/source_lock.json") == expected["source_lock_sha256"]
        and files.get("notes/PROOF_PACKAGE.md") == expected["proof_package_sha256"]
        and isinstance(files.get("results/CODE_REVIEW.md"), str)
    )


def _completed_stage(payload: dict[str, Any], stage: str) -> dict[str, Any] | None:
    records = payload.get("completed_stages")
    if not isinstance(records, list):
        return None
    matches = [record for record in records if isinstance(record, dict) and record.get("stage") == stage]
    return matches[0] if len(matches) == 1 else None


def _pipeline_final_valid(payload: Any, expected: dict[str, Any]) -> bool:
    """Require the terminal pipeline to bind final integrity, PDF, and review."""

    if not isinstance(payload, dict):
        return False
    final_pdf = _completed_stage(payload, "final_pdf")
    final_review = _completed_stage(payload, "independent_manuscript_review_round2")
    final_integrity = _completed_stage(payload, "final_integrity")
    indexes = payload.get("evidence_indexes")
    indexed_pdf = indexes.get("final_pdf") if isinstance(indexes, dict) else None
    indexed_review = indexes.get("independent_final_review") if isinstance(indexes, dict) else None
    finalization = payload.get("finalization_gates")
    if expected["manifest_kind"] == "PAPER3_HENON":
        independent_review_final = payload.get("independent_final_review_performed") is True
        review_zero = type(final_review.get("remaining_required_minors")) is int and final_review.get(
            "remaining_required_minors"
        ) == 0 if isinstance(final_review, dict) else False
        finalization_zero = (
            isinstance(finalization, dict)
            and finalization.get("independent_round2_verdict") == "PASS"
            and type(finalization.get("remaining_required_minors")) is int
            and finalization.get("remaining_required_minors") == 0
        )
    elif expected["manifest_kind"] == "PAPER4_ACTION":
        independence = payload.get("independence_boundary")
        independent_review_final = (
            isinstance(independence, dict)
            and independence.get("independent_round2_performed") is True
            and independence.get("independent_round2_verdict") == "PASS"
            and independence.get("author_self_check_is_independent_round2") is False
            and independence.get("finalization_authorized") is True
        )
        review_zero = type(final_review.get("remaining_blocking_issues")) is int and final_review.get(
            "remaining_blocking_issues"
        ) == 0 if isinstance(final_review, dict) else False
        finalization_zero = (
            isinstance(finalization, dict)
            and finalization.get("independent_round2_verdict") == "PASS"
            and type(finalization.get("remaining_blocking_issues")) is int
            and finalization.get("remaining_blocking_issues") == 0
        )
    else:
        independent_review_final = False
        review_zero = False
        finalization_zero = False
    return bool(
        payload.get("schema") == expected["pipeline_schema"]
        and payload.get("paper_id") == expected["paper_id"]
        and payload.get("stage") == "COMPLETE_LOCAL"
        and payload.get("final_status") == "COMPLETE_LOCAL_FINAL_REVIEW_PASS"
        and independent_review_final
        and finalization_zero
        and isinstance(finalization, dict)
        and finalization.get("scientific_source_unchanged_after_review") is True
        and finalization.get("external_prime_tables_accessed") is False
        and finalization.get("riemann_zero_data_accessed") is False
        and finalization.get("forbidden_data_used") is False
        and isinstance(final_pdf, dict)
        and final_pdf.get("status") == "COMPLETE"
        and final_pdf.get("artifact") == ARTIFACT_PATHS["final_pdf_path"]
        and final_pdf.get("sha256") == expected["final_pdf_sha256"]
        and type(final_pdf.get("pages")) is int
        and final_pdf["pages"] > 0
        and isinstance(final_review, dict)
        and final_review.get("status") == "PASS"
        and final_review.get("artifact") == ARTIFACT_PATHS["final_review_path"]
        and final_review.get("sha256") == expected["final_review_sha256"]
        and review_zero
        and final_review.get("finalization_authorized") is True
        and isinstance(final_integrity, dict)
        and final_integrity.get("status") == "COMPLETE"
        and final_integrity.get("artifact") == ARTIFACT_PATHS["final_integrity_path"]
        and isinstance(indexed_pdf, dict)
        and indexed_pdf.get("path") == ARTIFACT_PATHS["final_pdf_path"]
        and indexed_pdf.get("sha256") == expected["final_pdf_sha256"]
        and indexed_pdf.get("pages") == final_pdf.get("pages")
        and isinstance(indexed_review, dict)
        and indexed_review.get("path") == ARTIFACT_PATHS["final_review_path"]
        and indexed_review.get("sha256") == expected["final_review_sha256"]
        and indexed_review.get("verdict") == "PASS"
    )


def validate_upstream_bindings(project_root: Path) -> dict[str, Any]:
    """Require a strict binding file and independently frozen upstream hashes."""

    project_root = project_root.resolve()
    binding_path = project_root / "experiments" / "upstream_bindings.json"
    if not binding_path.exists():
        return {
            "gate_id": "G110",
            "path": str(binding_path),
            "errors": ["UPSTREAM_NOT_FINAL"],
            "records": [],
            "pass": False,
        }
    try:
        payload = load_strict_json_file(project_root, binding_path)
    except (ValueError, OSError) as error:
        return {
            "gate_id": "G110",
            "path": str(binding_path),
            "errors": [f"UPSTREAM_BINDING_INVALID:{type(error).__name__}"],
            "records": [],
            "pass": False,
        }
    errors: list[str] = []
    if not isinstance(payload, dict) or set(payload) != {"schema", "candidate_id", "bindings"}:
        errors.append("BINDING_ROOT_SCHEMA_NOT_EXACT")
        records: list[Any] = []
    else:
        records = payload.get("bindings", [])
        if payload.get("schema") != "CAPACITY_UPSTREAM_BINDINGS_V2":
            errors.append("BINDING_SCHEMA_MISMATCH")
        if payload.get("candidate_id") != CANDIDATE_ID:
            errors.append("BINDING_CANDIDATE_MISMATCH")
    if not isinstance(records, list):
        errors.append("BINDINGS_NOT_ARRAY")
        records = []

    ids = [record.get("id") for record in records if isinstance(record, dict)]
    if set(ids) != set(EXPECTED_UPSTREAMS) or len(ids) != len(EXPECTED_UPSTREAMS):
        errors.append("UPSTREAM_ID_SET_NOT_EXACT")

    audited: list[dict[str, Any]] = []
    papers_root = project_root.parent.resolve()
    for record in records:
        if not isinstance(record, dict) or set(record) != BINDING_KEYS:
            errors.append("UPSTREAM_RECORD_SCHEMA_NOT_EXACT")
            continue
        upstream_id = record["id"]
        expected = EXPECTED_UPSTREAMS.get(upstream_id)
        if expected is None:
            errors.append(f"UNKNOWN_UPSTREAM:{upstream_id}")
            continue
        frozen_final_available = all(
            isinstance(expected.get(key), str)
            for key in (
                "pipeline_state_sha256",
                "final_integrity_sha256",
                "final_pdf_sha256",
                "final_review_sha256",
            )
        )
        fields_match = all(
            record.get(key) == expected[key]
            for key in (
                "candidate_id",
                "paper_relative",
                "source_lock_sha256",
                "proof_package_sha256",
                "final_result_manifest_sha256",
            )
        ) and all(record.get(key) == value for key, value in ARTIFACT_PATHS.items()) and all(
            record.get(key) == expected.get(key)
            for key in (
                "pipeline_state_sha256",
                "final_integrity_sha256",
                "final_pdf_sha256",
                "final_review_sha256",
            )
        ) and record.get("status") == "FINAL_INTEGRITY_VERIFIED"
        paper_root = (project_root / expected["paper_relative"]).resolve()
        inside_papers = paper_root.parent == papers_root
        source_lock_path = paper_root / ARTIFACT_PATHS["source_lock_path"]
        proof_path = paper_root / ARTIFACT_PATHS["proof_package_path"]
        manifest_path = paper_root / ARTIFACT_PATHS["final_result_manifest_path"]
        pipeline_path = paper_root / ARTIFACT_PATHS["pipeline_state_path"]
        integrity_path = paper_root / ARTIFACT_PATHS["final_integrity_path"]
        final_pdf_path = paper_root / ARTIFACT_PATHS["final_pdf_path"]
        final_review_path = paper_root / ARTIFACT_PATHS["final_review_path"]
        files_safe = (
            inside_papers
            and regular_file_within(paper_root, source_lock_path)
            and regular_file_within(paper_root, proof_path)
            and regular_file_within(paper_root, manifest_path)
            and regular_file_within(paper_root, pipeline_path)
            and regular_file_within(paper_root, integrity_path)
            and regular_file_within(paper_root, final_pdf_path)
            and regular_file_within(paper_root, final_review_path)
        )
        source_lock_digest = sha256_file(source_lock_path) if files_safe else None
        proof_digest = sha256_file(proof_path) if files_safe else None
        manifest_digest = sha256_file(manifest_path) if files_safe else None
        pipeline_digest = sha256_file(pipeline_path) if files_safe else None
        integrity_digest = sha256_file(integrity_path) if files_safe else None
        final_pdf_digest = sha256_file(final_pdf_path) if files_safe else None
        final_review_digest = sha256_file(final_review_path) if files_safe else None
        try:
            manifest_payload = load_strict_json_file(paper_root, manifest_path) if files_safe else None
            pipeline_payload = load_strict_json_file(paper_root, pipeline_path) if files_safe else None
        except (ValueError, OSError):
            manifest_payload = None
            pipeline_payload = None
        if expected["manifest_kind"] == "PAPER3_HENON":
            manifest_semantics = _paper3_manifest_valid(manifest_payload, expected)
        else:
            manifest_semantics = _paper4_manifest_valid(manifest_payload, expected)
        pipeline_semantics = _pipeline_final_valid(pipeline_payload, expected) if frozen_final_available else False
        record_pass = (
            frozen_final_available
            and
            fields_match
            and files_safe
            and source_lock_digest == expected["source_lock_sha256"]
            and proof_digest == expected["proof_package_sha256"]
            and manifest_digest == expected["final_result_manifest_sha256"]
            and manifest_semantics
            and pipeline_digest == expected["pipeline_state_sha256"]
            and integrity_digest == expected["final_integrity_sha256"]
            and final_pdf_digest == expected["final_pdf_sha256"]
            and final_review_digest == expected["final_review_sha256"]
            and pipeline_semantics
        )
        if not record_pass:
            errors.append(f"UPSTREAM_NOT_FINAL:{upstream_id}")
        audited.append(
            {
                "id": upstream_id,
                "source_lock_sha256": source_lock_digest,
                "proof_package_sha256": proof_digest,
                "final_result_manifest_sha256": manifest_digest,
                "binding_matches_frozen_constants": fields_match,
                "manifest_semantics_pass": manifest_semantics,
                "pipeline_state_sha256": pipeline_digest,
                "final_integrity_sha256": integrity_digest,
                "final_pdf_sha256": final_pdf_digest,
                "final_review_sha256": final_review_digest,
                "pipeline_final_semantics_pass": pipeline_semantics,
                "pass": bool(record_pass),
            }
        )
    return {
        "gate_id": "G110",
        "path": str(binding_path),
        "records": audited,
        "errors": errors,
        "pass": not errors and len(audited) == len(EXPECTED_UPSTREAMS),
    }
