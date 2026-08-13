import hashlib
import json
from copy import deepcopy
from pathlib import Path

import pytest

import capacity_audit.manifest as manifest_module
import capacity_audit.upstream as upstream_module
from capacity_audit.manifest import (
    GATE_KEYS,
    REQUIRED_RESULT_PATHS,
    build_result_manifest,
)
from capacity_audit.protocol import CANDIDATE_ID, EXPECTED_LOCK_SHA256
from capacity_audit.review_gate import AUTHORITY_PREFIX, validate_review_authority
from capacity_audit.upstream import (
    ARTIFACT_PATHS,
    EXPECTED_UPSTREAMS,
    _pipeline_final_valid,
    validate_upstream_bindings,
)


CODE_DIGEST = "a" * 64
STAMP = "2026-08-14T00:00:00+00:00"
PROJECT_ROOT = Path(__file__).resolve().parents[2]


def _authority(verdict: str) -> str:
    payload = {
        "candidate_id": CANDIDATE_ID,
        "reviewed_code_sha256": CODE_DIGEST,
        "reviewer_independent": True,
        "source_lock_sha256": EXPECTED_LOCK_SHA256,
        "verdict": verdict,
    }
    return AUTHORITY_PREFIX + json.dumps(payload, sort_keys=True) + "\n"


@pytest.mark.parametrize(
    ("verdict", "expected_pass"),
    [("DEPLOYMENT_FAIL", False), ("DEPLOYMENT_PASS", True)],
)
def test_review_authority_lifecycle_uses_isolated_fixture(
    tmp_path, monkeypatch, verdict, expected_pass
):
    root = tmp_path / "project"
    (root / "results").mkdir(parents=True)
    (root / "results" / "CODE_REVIEW.md").write_text(_authority(verdict), encoding="utf-8")
    monkeypatch.setattr(
        "capacity_audit.review_gate.reviewed_code_tree_sha256",
        lambda _: CODE_DIGEST,
    )
    record = validate_review_authority(root)
    assert record["pass"] is expected_pass
    assert ("VERDICT_NOT_DEPLOYMENT_PASS" in record["errors"]) is (not expected_pass)


def test_upstream_pending_without_binding_uses_isolated_fixture(tmp_path):
    root = tmp_path / "papers" / "paper5"
    (root / "experiments").mkdir(parents=True)
    record = validate_upstream_bindings(root)
    assert not record["pass"]
    assert record["errors"] == ["UPSTREAM_NOT_FINAL"]


def test_live_frozen_upstream_binding_closes_both_terminal_packages():
    record = validate_upstream_bindings(PROJECT_ROOT)
    assert record["pass"] is True
    assert record["errors"] == []
    assert {item["id"] for item in record["records"]} == set(EXPECTED_UPSTREAMS)
    for item in record["records"]:
        assert item["binding_matches_frozen_constants"] is True
        assert item["manifest_semantics_pass"] is True
        assert item["pipeline_final_semantics_pass"] is True
        assert type(item["pass"]) is bool and item["pass"] is True


def test_paper4_terminal_semantics_require_independent_review_not_status_only():
    expected = EXPECTED_UPSTREAMS["PAPER4_ALGEBRAIC_ACTION_CLOCKS"]
    paper_root = (PROJECT_ROOT / expected["paper_relative"]).resolve()
    payload = json.loads((paper_root / ARTIFACT_PATHS["pipeline_state_path"]).read_text(encoding="utf-8"))
    assert _pipeline_final_valid(payload, expected) is True

    attacked = deepcopy(payload)
    attacked["independence_boundary"]["author_self_check_is_independent_round2"] = True
    assert attacked["stage"] == "COMPLETE_LOCAL"
    assert attacked["final_status"] == "COMPLETE_LOCAL_FINAL_REVIEW_PASS"
    assert _pipeline_final_valid(attacked, expected) is False

    attacked = deepcopy(payload)
    round2 = next(
        item
        for item in attacked["completed_stages"]
        if item["stage"] == "independent_manuscript_review_round2"
    )
    round2["remaining_blocking_issues"] = False
    assert _pipeline_final_valid(attacked, expected) is False


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _write_upstream_package(paper: Path, *, complete: bool) -> dict:
    for relative in ARTIFACT_PATHS.values():
        (paper / relative).parent.mkdir(parents=True, exist_ok=True)
    (paper / ARTIFACT_PATHS["source_lock_path"]).write_text("locked", encoding="utf-8")
    (paper / ARTIFACT_PATHS["proof_package_path"]).write_text("proof", encoding="utf-8")
    (paper / ARTIFACT_PATHS["final_integrity_path"]).write_text("integrity", encoding="utf-8")
    (paper / ARTIFACT_PATHS["final_pdf_path"]).write_bytes(b"%PDF-final-fixture")
    (paper / ARTIFACT_PATHS["final_review_path"]).write_text("PASS", encoding="utf-8")

    expected = {
        "paper_relative": "../paper3",
        "candidate_id": "fixture_candidate",
        "source_lock_sha256": _sha(paper / ARTIFACT_PATHS["source_lock_path"]),
        "proof_package_sha256": _sha(paper / ARTIFACT_PATHS["proof_package_path"]),
        "manifest_kind": "PAPER3_HENON",
        "pipeline_schema": "FIXTURE_PIPELINE_V1",
        "paper_id": "fixture-paper",
        "final_integrity_sha256": _sha(paper / ARTIFACT_PATHS["final_integrity_path"]),
        "final_pdf_sha256": _sha(paper / ARTIFACT_PATHS["final_pdf_path"]),
        "final_review_sha256": _sha(paper / ARTIFACT_PATHS["final_review_path"]),
    }
    manifest = {
        "candidate_id": expected["candidate_id"],
        "source_lock_sha256": expected["source_lock_sha256"],
        "execution_status": "PASS",
        "all_must_run_pass": True,
        "forbidden_data_used": False,
        "external_prime_tables_accessed": False,
        "riemann_zero_data_accessed": False,
        "official_report_linkage": {"checks": {"closure": True}},
        "artifacts": {
            "notes/PROOF_PACKAGE.md": {"sha256": expected["proof_package_sha256"]},
            "results/CODE_REVIEW.md": {"sha256": "b" * 64},
        },
    }
    manifest_path = paper / ARTIFACT_PATHS["final_result_manifest_path"]
    manifest_path.write_text(json.dumps(manifest, sort_keys=True), encoding="utf-8")
    expected["final_result_manifest_sha256"] = _sha(manifest_path)

    final_pdf_stage = {
        "stage": "final_pdf",
        "status": "COMPLETE",
        "artifact": ARTIFACT_PATHS["final_pdf_path"],
        "sha256": expected["final_pdf_sha256"],
        "pages": 1,
    }
    review_stage = {
        "stage": "independent_manuscript_review_round2",
        "status": "PASS",
        "artifact": ARTIFACT_PATHS["final_review_path"],
        "sha256": expected["final_review_sha256"],
        "remaining_required_minors": 0,
        "finalization_authorized": True,
    }
    integrity_stage = {
        "stage": "final_integrity",
        "status": "COMPLETE",
        "artifact": ARTIFACT_PATHS["final_integrity_path"],
    }
    pipeline = {
        "schema": expected["pipeline_schema"],
        "paper_id": expected["paper_id"],
        "stage": "COMPLETE_LOCAL" if complete else "PRE_REVIEW_COMPLETE",
        "final_status": "COMPLETE_LOCAL_FINAL_REVIEW_PASS",
        "completed_stages": [final_pdf_stage, review_stage, integrity_stage],
        "evidence_indexes": {
            "final_pdf": {
                "path": ARTIFACT_PATHS["final_pdf_path"],
                "sha256": expected["final_pdf_sha256"],
                "pages": 1,
            },
            "independent_final_review": {
                "path": ARTIFACT_PATHS["final_review_path"],
                "sha256": expected["final_review_sha256"],
                "verdict": "PASS",
            },
        },
        "independent_final_review_performed": complete,
        "finalization_gates": {
            "independent_round2_verdict": "PASS",
            "remaining_required_minors": 0,
            "scientific_source_unchanged_after_review": True,
            "external_prime_tables_accessed": False,
            "riemann_zero_data_accessed": False,
            "forbidden_data_used": False,
        },
    }
    pipeline_path = paper / ARTIFACT_PATHS["pipeline_state_path"]
    pipeline_path.write_text(json.dumps(pipeline, sort_keys=True), encoding="utf-8")
    expected["pipeline_state_sha256"] = _sha(pipeline_path)
    return expected


@pytest.mark.parametrize(("complete", "expected_pass"), [(False, False), (True, True)])
def test_upstream_requires_actual_terminal_artifact_closure(
    tmp_path, monkeypatch, complete, expected_pass
):
    root = tmp_path / "papers" / "paper5"
    paper = tmp_path / "papers" / "paper3"
    (root / "experiments").mkdir(parents=True)
    expected = _write_upstream_package(paper, complete=complete)
    monkeypatch.setattr(upstream_module, "EXPECTED_UPSTREAMS", {"UPSTREAM": expected})
    record = {
        "id": "UPSTREAM",
        "candidate_id": expected["candidate_id"],
        "paper_relative": expected["paper_relative"],
        **ARTIFACT_PATHS,
        "source_lock_sha256": expected["source_lock_sha256"],
        "proof_package_sha256": expected["proof_package_sha256"],
        "final_result_manifest_sha256": expected["final_result_manifest_sha256"],
        "pipeline_state_sha256": expected["pipeline_state_sha256"],
        "final_integrity_sha256": expected["final_integrity_sha256"],
        "final_pdf_sha256": expected["final_pdf_sha256"],
        "final_review_sha256": expected["final_review_sha256"],
        "status": "FINAL_INTEGRITY_VERIFIED",
    }
    (root / "experiments" / "upstream_bindings.json").write_text(
        json.dumps(
            {
                "schema": "CAPACITY_UPSTREAM_BINDINGS_V2",
                "candidate_id": CANDIDATE_ID,
                "bindings": [record],
            },
            sort_keys=True,
        ),
        encoding="utf-8",
    )
    result = validate_upstream_bindings(root)
    assert result["pass"] is expected_pass
    assert type(result["records"][0]["manifest_semantics_pass"]) is bool
    assert type(result["records"][0]["pass"]) is bool


def _gate_records() -> dict:
    return {key: {"gate_id": key, "pass": True} for key in GATE_KEYS}


def _write_post_run_fixture(root: Path, monkeypatch) -> tuple[dict, dict]:
    for relative in REQUIRED_RESULT_PATHS:
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("fixture", encoding="utf-8")
    gates = _gate_records()
    expected_gates = json.loads(json.dumps(gates))
    monkeypatch.setattr(manifest_module, "reviewed_code_tree_sha256", lambda _: CODE_DIGEST)
    monkeypatch.setattr(manifest_module, "_expected_gate_records", lambda _: expected_gates)
    result = {
        "schema": "CAPACITY_REGISTERED_AUDIT_V1",
        "candidate_id": CANDIDATE_ID,
        "registered_at_utc": STAMP,
        "audit_type": "EXACT_SYMBOLIC_AND_STATIC_ONLY",
        "source_lock_sha256": EXPECTED_LOCK_SHA256,
        "reviewed_code_sha256": CODE_DIGEST,
        "gates": gates,
        "external_prime_tables_accessed": False,
        "prime_target_arrays_generated": False,
        "riemann_zero_data_accessed": False,
        "candidate_numerical_runs": 0,
        "target_matches_computed": 0,
        "classification": "CAPACITY_BOUND_CERTIFIED",
        "pass": True,
    }
    result_path = root / "results" / "EXPERIMENT_RESULTS.json"
    result_path.write_text(json.dumps(result, sort_keys=True), encoding="utf-8")
    registry = {
        "schema": "CAPACITY_REGISTERED_RUN_REGISTRY_V1",
        "candidate_id": CANDIDATE_ID,
        "registered_at_utc": STAMP,
        "result_path": "results/EXPERIMENT_RESULTS.json",
        "result_sha256": _sha(result_path),
        "source_lock_sha256": EXPECTED_LOCK_SHA256,
        "reviewed_code_sha256": CODE_DIGEST,
        "registered_run_count": 1,
        "candidate_numerical_runs": 0,
    }
    (root / "results" / "registered_run.json").write_text(
        json.dumps(registry, sort_keys=True), encoding="utf-8"
    )
    return result, registry


def _rewrite_post_run(root: Path, result: dict, registry: dict) -> None:
    result_path = root / "results" / "EXPERIMENT_RESULTS.json"
    result_path.write_text(json.dumps(result, sort_keys=True), encoding="utf-8")
    registry["result_sha256"] = _sha(result_path)
    (root / "results" / "registered_run.json").write_text(
        json.dumps(registry, sort_keys=True), encoding="utf-8"
    )


def test_post_run_manifest_accepts_exact_complete_fixture(tmp_path, monkeypatch):
    root = tmp_path / "project"
    _write_post_run_fixture(root, monkeypatch)
    assert build_result_manifest(root)["pass"]


@pytest.mark.parametrize(
    ("target", "field", "bad_value", "error"),
    [
        ("result", "registered_at_utc", 7, "RESULT_TYPES_NOT_EXACT"),
        ("result", "candidate_numerical_runs", False, "RESULT_TYPES_NOT_EXACT"),
        ("result", "target_matches_computed", False, "RESULT_TYPES_NOT_EXACT"),
        ("registry", "registered_run_count", True, "REGISTRY_TYPES_NOT_EXACT"),
        ("registry", "candidate_numerical_runs", False, "REGISTRY_TYPES_NOT_EXACT"),
    ],
)
def test_post_run_manifest_rejects_wrong_json_types(
    tmp_path, monkeypatch, target, field, bad_value, error
):
    root = tmp_path / "project"
    result, registry = _write_post_run_fixture(root, monkeypatch)
    (result if target == "result" else registry)[field] = bad_value
    _rewrite_post_run(root, result, registry)
    record = build_result_manifest(root)
    assert not record["pass"]
    assert error in record["semantic_checks"]["errors"]


def test_post_run_manifest_recomputes_exact_inner_gate_records(tmp_path, monkeypatch):
    root = tmp_path / "project"
    result, registry = _write_post_run_fixture(root, monkeypatch)
    result["gates"]["source_lock"] = {"pass": True}
    _rewrite_post_run(root, result, registry)
    record = build_result_manifest(root)
    assert not record["pass"]
    assert "RESULT_GATE_RECORDS_NOT_EXACT" in record["semantic_checks"]["errors"]


@pytest.mark.parametrize("attack", ["malformed", "duplicate"])
def test_post_run_malformed_and_duplicate_json_reach_strict_semantics(
    tmp_path, monkeypatch, attack
):
    root = tmp_path / "project"
    _, registry = _write_post_run_fixture(root, monkeypatch)
    result_path = root / "results" / "EXPERIMENT_RESULTS.json"
    text = "not-json" if attack == "malformed" else '{"schema":"a","schema":"b"}'
    result_path.write_text(text, encoding="utf-8")
    registry["result_sha256"] = _sha(result_path)
    (root / "results" / "registered_run.json").write_text(json.dumps(registry), encoding="utf-8")
    record = build_result_manifest(root)
    assert record["result_tree"]["pass"]
    assert not record["pass"]
    assert record["semantic_checks"]["errors"][0].startswith("STRICT_JSON_LOAD_FAIL:")


def test_post_run_cross_artifact_timestamp_mismatch_fails(tmp_path, monkeypatch):
    root = tmp_path / "project"
    result, registry = _write_post_run_fixture(root, monkeypatch)
    registry["registered_at_utc"] = "2026-08-14T00:00:01+00:00"
    _rewrite_post_run(root, result, registry)
    record = build_result_manifest(root)
    assert not record["pass"]
    assert "REGISTRY_SEMANTICS_FAIL" in record["semantic_checks"]["errors"]


@pytest.mark.parametrize("attack", ["extra", "nested", "symlink"])
def test_result_tree_flat_allowlist_rejects_each_attack(tmp_path, monkeypatch, attack):
    root = tmp_path / "project"
    _write_post_run_fixture(root, monkeypatch)
    if attack == "extra":
        (root / "results" / "extra.json").write_text("{}", encoding="utf-8")
    elif attack == "nested":
        (root / "results" / "nested").mkdir()
        (root / "results" / "nested" / "hidden.json").write_text("{}", encoding="utf-8")
    else:
        review = root / "results" / "CODE_REVIEW.md"
        outside = tmp_path / "outside.md"
        outside.write_text("outside", encoding="utf-8")
        review.unlink()
        review.symlink_to(outside)
    record = build_result_manifest(root)
    assert not record["pass"]
    assert not record["result_tree"]["pass"]
