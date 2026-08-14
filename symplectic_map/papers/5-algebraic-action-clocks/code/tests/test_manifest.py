import json
from pathlib import Path

import pytest

from action_audit.manifest import (
    EXPECTED_LOCK_SHA256,
    collect_manifest_inputs,
    validate_required_artifacts,
)


def _write_json(path: Path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload), encoding="utf-8")


def _complete_fixture(root: Path):
    results = root / "results"
    results.mkdir(parents=True)
    _write_json(
        results / "source_lock_validation.json",
        {
            "pass": True,
            "lock_version": 3,
            "sha256": EXPECTED_LOCK_SHA256,
            "prelock_execution_clean": True,
        },
    )
    _write_json(results / "target_isolation_audit.json", {"pass": True, "findings": []})
    _write_json(
        results / "proof_audit.json",
        {"pass": True, "proof_contract_version": 3, "dependency_checks": {"all": True}},
    )
    _write_json(
        results / "control_audit.json",
        {
            "pass": True,
            "controls_executed_before_henon_static_audit": True,
            "candidate_parameter_substituted": False,
            "candidate_periodic_point_computed": False,
            "candidate_action_computed": False,
        },
    )
    _write_json(
        results / "henon_static_audit.json",
        {
            key: {"pass": True}
            for key in (
                "henon_identity",
                "recurrence_multiplicity",
                "projective_infinity",
                "s_integral_denominator",
            )
        },
    )
    _write_json(
        results / "command_environment_manifest.json",
        {
            "execution_date_utc": "2026-08-14",
            "execution_timestamp_utc": "2026-08-14T00:00:00Z",
            "network_access_by_executable": False,
            "external_prime_tables_accessed": False,
            "riemann_zero_data_accessed": False,
            "candidate_parameter_substituted": False,
            "candidate_periodic_points_computed": False,
            "candidate_actions_computed": False,
        },
    )
    _write_json(
        results / "run_summary.json",
        {
            "status": "PASS_STATIC_CERTIFICATE_NO_CANDIDATE_EXECUTION",
            "candidate_execution_gate": "CLOSED",
            "candidate_parameter_substituted": False,
            "candidate_periodic_points_computed": False,
            "candidate_actions_computed": False,
        },
    )
    (results / "CODE_REVIEW.md").write_text(
        "# Review\n\nVerdict: DEPLOYMENT_FAIL\n\nVerdict: DEPLOYMENT_PASS\n",
        encoding="utf-8",
    )
    (results / "VALIDATION_REPORT.md").write_text(
        "# Validation Report\n\n"
        + EXPECTED_LOCK_SHA256
        + "\nPASS_STATIC_CERTIFICATE_NO_CANDIDATE_EXECUTION\n",
        encoding="utf-8",
    )
    (results / "EXPERIMENT_RESULTS.md").write_text(
        "# Experiment Results\n\n"
        "ALGEBRAIC_NORMALIZED_ACTION_CLOCK_REJECTED_BY_ALL_PERIOD_THEOREM\n"
        "Candidate periodic points computed: **no**\n",
        encoding="utf-8",
    )
    (results / "pytest.xml").write_text(
        '<testsuites><testsuite tests="1" failures="0" errors="0"/></testsuites>',
        encoding="utf-8",
    )
    for relative in (
        "experiments/source_lock.json",
        "experiments/EXPERIMENT_PLAN.md",
        "experiments/EXPERIMENT_TRACKER.md",
        "notes/PROOF_PACKAGE.md",
        "notes/INDEPENDENT_COUNTEREXAMPLE_REVIEW.md",
    ):
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("fixture", encoding="utf-8")
    code = root / "code" / "audit.py"
    code.parent.mkdir(parents=True)
    code.write_text("VALUE = 1\n", encoding="utf-8")


def test_manifest_selection_includes_markdown_review_and_reports(tmp_path):
    _complete_fixture(tmp_path)
    selected = {str(path.relative_to(tmp_path)) for path in collect_manifest_inputs(tmp_path)}
    assert "results/CODE_REVIEW.md" in selected
    assert "results/VALIDATION_REPORT.md" in selected
    assert "results/EXPERIMENT_RESULTS.md" in selected
    assert "results/pytest.xml" in selected


def test_required_artifact_semantics_pass_complete_fixture(tmp_path):
    _complete_fixture(tmp_path)
    record = validate_required_artifacts(tmp_path)
    assert record["pass"]
    assert all(record["semantic_checks"].values())


def test_required_artifact_semantics_reject_failed_final_review(tmp_path):
    _complete_fixture(tmp_path)
    (tmp_path / "results" / "CODE_REVIEW.md").write_text(
        "# Review\n\nVerdict: DEPLOYMENT_FAIL\n",
        encoding="utf-8",
    )
    record = validate_required_artifacts(tmp_path)
    assert not record["pass"]
    assert not record["semantic_checks"]["results/CODE_REVIEW.md"]


def test_required_artifact_semantics_reject_missing_report(tmp_path):
    _complete_fixture(tmp_path)
    (tmp_path / "results" / "VALIDATION_REPORT.md").unlink()
    record = validate_required_artifacts(tmp_path)
    assert not record["pass"]
    assert not record["required_existence"]["results/VALIDATION_REPORT.md"]


def test_required_artifact_semantics_reject_candidate_execution(tmp_path):
    _complete_fixture(tmp_path)
    path = tmp_path / "results" / "run_summary.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    payload["candidate_periodic_points_computed"] = True
    path.write_text(json.dumps(payload), encoding="utf-8")
    record = validate_required_artifacts(tmp_path)
    assert not record["semantic_checks"]["results/run_summary.json"]


def test_manifest_rejects_unexpected_result_json(tmp_path):
    _complete_fixture(tmp_path)
    (tmp_path / "results" / "unexpected.json").write_text(
        '{"unexpected": true}\n',
        encoding="utf-8",
    )
    record = validate_required_artifacts(tmp_path)
    assert not record["pass"]
    assert record["exact_result_schema"]["unknown_result_paths"] == [
        "results/unexpected.json"
    ]
    with pytest.raises(ValueError, match="result schema is not exact"):
        collect_manifest_inputs(tmp_path)


def test_manifest_rejects_nested_duplicate_required_basename(tmp_path):
    _complete_fixture(tmp_path)
    nested = tmp_path / "results" / "duplicate" / "run_summary.json"
    nested.parent.mkdir()
    nested.write_text("{}\n", encoding="utf-8")
    record = validate_required_artifacts(tmp_path)
    schema = record["exact_result_schema"]
    assert not record["pass"]
    assert "results/duplicate/run_summary.json" in schema["nested_result_paths"]
    assert "run_summary.json" in schema["duplicate_basenames"]


def test_manifest_rejects_result_symlink_resolving_outside_root(tmp_path):
    _complete_fixture(tmp_path)
    outside = tmp_path.parent / f"{tmp_path.name}-outside-result.json"
    outside.write_text("{}\n", encoding="utf-8")
    link = tmp_path / "results" / "external.json"
    link.symlink_to(outside)
    try:
        record = validate_required_artifacts(tmp_path)
        schema = record["exact_result_schema"]
        assert not record["pass"]
        assert "results/external.json" in schema["symlink_paths"]
        assert "results/external.json" in schema["outside_root_paths"]
    finally:
        outside.unlink()


def test_manifest_rejects_required_result_symlink(tmp_path):
    _complete_fixture(tmp_path)
    target = tmp_path / "run-summary-target.json"
    original = tmp_path / "results" / "run_summary.json"
    original.replace(target)
    original.symlink_to(target)
    record = validate_required_artifacts(tmp_path)
    assert not record["pass"]
    assert "results/run_summary.json" in record["exact_result_schema"]["symlink_paths"]


def test_existing_final_manifest_is_optional_output_not_input(tmp_path):
    _complete_fixture(tmp_path)
    output = tmp_path / "results" / "final_result_manifest.json"
    output.write_text("{}\n", encoding="utf-8")
    record = validate_required_artifacts(tmp_path)
    assert record["pass"]
    selected = {str(path.relative_to(tmp_path)) for path in collect_manifest_inputs(tmp_path)}
    assert "results/final_result_manifest.json" not in selected
