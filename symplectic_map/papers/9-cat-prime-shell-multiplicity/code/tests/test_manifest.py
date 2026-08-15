from __future__ import annotations

import copy
from pathlib import Path

from prime_shell import manifest
from prime_shell.candidate import run_registered_candidate
from prime_shell.constants import CANDIDATE_ID, LOCKED_PRIMES, SOURCE_LOCK_SHA256
from prime_shell.manifest import _result_inventory


def test_manifest_rejects_extra_result_file(tmp_path: Path) -> None:
    root = tmp_path / "paper"
    results = root / "results"
    results.mkdir(parents=True)
    (results / "allowed.json").write_text("{}\n", encoding="utf-8")
    (results / "extra.json").write_text("{}\n", encoding="utf-8")
    audit = _result_inventory(root, frozenset({"allowed.json"}))
    assert audit["pass"] is False
    assert "RESULT_INVENTORY_NOT_EXACT" in audit["errors"]


def test_result_validator_rejects_round1_structural_bypass(
    tmp_path: Path, monkeypatch
) -> None:
    code_sha = "a" * 64
    claim_sha = "b" * 64
    live_review = {"stage": "P3_INDEPENDENT_DEPLOYMENT_REVIEW", "pass": True}
    official_gates = {
        name: {"stage": name, "pass": True}
        for name in manifest.PREEXECUTION_GATE_KEYS
    }
    official = {
        "schema": "PRIME_SHELL_PRE_EXECUTION_AUDIT_V1",
        "candidate_id": CANDIDATE_ID,
        "source_lock_sha256": SOURCE_LOCK_SHA256,
        "reviewed_code_sha256": code_sha,
        "gates": official_gates,
        "independent_review": live_review,
        "locked_primes": list(LOCKED_PRIMES),
        "formal_repeats": [1, 2, 3],
        "registered_exact_audits": 0,
        "registered_primes_executed": [],
        "candidate_numerical_runs": 0,
        "external_prime_tables_accessed": False,
        "generated_prime_target_arrays": 0,
        "riemann_zero_data_accessed": False,
        "numeric_s_or_log_evaluations": 0,
        "centralizer_computations_run": 0,
        "status": "AUTHORIZED_FOR_REGISTERED_EXECUTION",
        "pass": True,
    }
    good_audit = run_registered_candidate()
    wrong_rows = copy.deepcopy(good_audit)
    wrong_rows["rows"] = "abcde"
    assert "AUDIT_ROWS_NOT_FIVE_ELEMENT_LIST" in manifest._validate_audit_payload(
        wrong_rows
    )
    bool_counters = copy.deepcopy(good_audit)
    bool_counters["numeric_s_or_log_evaluations"] = False
    bool_counters["centralizer_computations_run"] = False
    bool_counters["composite_shells_enumerated"] = False
    bool_errors = manifest._validate_audit_payload(bool_counters)
    assert "AUDIT_NUMERIC_S_OR_LOG_EVALUATIONS_NOT_EXACT_INT" in bool_errors
    assert "AUDIT_CENTRALIZER_COMPUTATIONS_RUN_NOT_EXACT_INT" in bool_errors
    assert "AUDIT_COMPOSITE_SHELLS_ENUMERATED_NOT_EXACT_INT" in bool_errors
    missing_controls = copy.deepcopy(good_audit)
    missing_controls["controls"] = {}
    assert "AUDIT_CONTROLS_NOT_EXACT_TRUE_MAP" in manifest._validate_audit_payload(
        missing_controls
    )
    reordered = copy.deepcopy(good_audit)
    reordered["rows"][0], reordered["rows"][1] = reordered["rows"][1], reordered["rows"][0]
    assert "AUDIT_ROW_PRIME_ORDER_NOT_EXACT" in manifest._validate_audit_payload(
        reordered
    )

    malformed = copy.deepcopy(good_audit)
    malformed["rows"] = "abcde"
    malformed["numeric_s_or_log_evaluations"] = False
    malformed["centralizer_computations_run"] = False
    malformed["composite_shells_enumerated"] = False
    malformed["controls"] = {}
    malformed.pop("classification")
    payload = {
        "schema": "PRIME_SHELL_OFFICIAL_RESULT_V1",
        "candidate_id": CANDIDATE_ID,
        "source_lock_sha256": SOURCE_LOCK_SHA256,
        "reviewed_code_sha256": code_sha,
        "registered_claim_sha256": claim_sha,
        "pre_execution_gates": {},
        "independent_review_gate": {"pass": True},
        "audit": malformed,
        "registered_exact_audits": False,
        "candidate_numerical_runs": False,
        "pass": True,
    }
    monkeypatch.setattr(manifest, "code_tree_sha256", lambda root: code_sha)
    monkeypatch.setattr(
        manifest,
        "validate_claim",
        lambda root, digest: {"claim_sha256": claim_sha, "pass": True},
    )
    monkeypatch.setattr(manifest, "regular_file", lambda path: True)
    monkeypatch.setattr(manifest, "load_exact_json", lambda path: official)
    monkeypatch.setattr(manifest, "validate_deployment_authority", lambda root: live_review)
    monkeypatch.setattr(manifest, "collect_safe_preflight", lambda root: official)
    result = manifest.validate_registered_result(payload, tmp_path)
    assert result["pass"] is False
    assert "AUDIT_KEYS_NOT_EXACT" in result["errors"]
    assert "RESULT_REGISTERED_EXACT_AUDITS_MISMATCH" in result["errors"]
    assert "RESULT_CANDIDATE_NUMERICAL_RUNS_MISMATCH" in result["errors"]
    assert "EMBEDDED_PREFLIGHT_GATES_NOT_OFFICIAL_EXACT" in result["errors"]


def test_official_gate_records_must_match_live_recomputation(
    tmp_path: Path, monkeypatch
) -> None:
    code_sha = "c" * 64
    claim_sha = "d" * 64
    live_review = {"stage": "P3_INDEPENDENT_DEPLOYMENT_REVIEW", "pass": True}
    full_gates = {
        name: {"stage": name, "records": [], "errors": [], "pass": True}
        for name in manifest.PREEXECUTION_GATE_KEYS
    }
    live_preflight = {
        "schema": "PRIME_SHELL_PRE_EXECUTION_AUDIT_V1",
        "candidate_id": CANDIDATE_ID,
        "source_lock_sha256": SOURCE_LOCK_SHA256,
        "reviewed_code_sha256": code_sha,
        "gates": full_gates,
        "independent_review": live_review,
        "locked_primes": list(LOCKED_PRIMES),
        "formal_repeats": [1, 2, 3],
        "registered_exact_audits": 0,
        "registered_primes_executed": [],
        "candidate_numerical_runs": 0,
        "external_prime_tables_accessed": False,
        "generated_prime_target_arrays": 0,
        "riemann_zero_data_accessed": False,
        "numeric_s_or_log_evaluations": 0,
        "centralizer_computations_run": 0,
        "status": "AUTHORIZED_FOR_REGISTERED_EXECUTION",
        "pass": True,
    }

    def result_payload(gates):
        return {
            "schema": "PRIME_SHELL_OFFICIAL_RESULT_V1",
            "candidate_id": CANDIDATE_ID,
            "source_lock_sha256": SOURCE_LOCK_SHA256,
            "reviewed_code_sha256": code_sha,
            "registered_claim_sha256": claim_sha,
            "pre_execution_gates": gates,
            "independent_review_gate": live_review,
            "audit": run_registered_candidate(),
            "registered_exact_audits": 1,
            "candidate_numerical_runs": 0,
            "pass": True,
        }

    monkeypatch.setattr(manifest, "code_tree_sha256", lambda root: code_sha)
    monkeypatch.setattr(
        manifest,
        "validate_claim",
        lambda root, digest: {"claim_sha256": claim_sha, "pass": True},
    )
    monkeypatch.setattr(manifest, "regular_file", lambda path: True)
    monkeypatch.setattr(manifest, "validate_deployment_authority", lambda root: live_review)
    monkeypatch.setattr(manifest, "collect_safe_preflight", lambda root: live_preflight)
    monkeypatch.setattr(manifest, "load_exact_json", lambda path: live_preflight)
    legal = manifest.validate_registered_result(result_payload(full_gates), tmp_path)
    assert legal["pass"] is True, legal

    hollow = copy.deepcopy(live_preflight)
    hollow["gates"] = {
        name: {"pass": True} for name in manifest.PREEXECUTION_GATE_KEYS
    }
    monkeypatch.setattr(manifest, "load_exact_json", lambda path: hollow)
    rejected = manifest.validate_registered_result(
        result_payload(hollow["gates"]), tmp_path
    )
    assert rejected["pass"] is False
    assert "OFFICIAL_PREFLIGHT_NOT_LIVE_EXACT_RECOMPUTATION" in rejected["errors"]
