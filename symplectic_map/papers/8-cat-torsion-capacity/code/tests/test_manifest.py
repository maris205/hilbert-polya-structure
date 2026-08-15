from __future__ import annotations

import json
from pathlib import Path

import pytest

from cat_torsion.manifest import (
    EXPECTED_RAW_HASHES,
    PREWRITE_RESULT_FILES,
    PRE_EXECUTION_KEYS,
    REQUIRED_ANALYZER_JUNIT_TESTS,
    REQUIRED_JUNIT_TESTS,
    build_post_run_manifest,
    parse_passing_junit,
    validate_existing_post_run_manifest,
    validate_execution_chain_payloads,
    validate_junit_role_separation,
    validate_official_preflight,
    write_post_run_manifest,
    write_safe_preflight,
)
from cat_torsion.protocol import (
    CANDIDATE_ID,
    EXPECTED_CODE_FILES,
    EXPECTED_EXECUTION_TREE_SHA256,
    EXPECTED_LOCK_SHA256,
    LOCAL_BINDINGS,
    UPSTREAM_BINDINGS,
    load_exact_json,
    stable_file_bytes,
    write_json,
)
from cat_torsion.review_gate import (
    POSTRUN_AUTHORITY_PREFIX,
    reviewed_code_tree_sha256,
)


PROJECT_ROOT = Path(__file__).absolute().parents[2]


def _copy_file(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(stable_file_bytes(source))


def _isolated_postrun_project(tmp_path: Path) -> Path:
    project = tmp_path / "work" / "papers" / "8-cat-torsion-capacity"
    project_files = {
        "pyproject.toml",
        "experiments/source_lock.json",
        "experiments/EXPERIMENT_PLAN.md",
        "notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md",
        *[relative for relative, _ in LOCAL_BINDINGS.values()],
    }
    for relative in sorted(project_files):
        _copy_file(PROJECT_ROOT / relative, project / relative)
    for relative in sorted(EXPECTED_CODE_FILES):
        _copy_file(PROJECT_ROOT / "code" / relative, project / "code" / relative)
    for relative, _ in UPSTREAM_BINDINGS.values():
        _copy_file(PROJECT_ROOT / relative, project / relative)
    for name in sorted(PREWRITE_RESULT_FILES):
        _copy_file(PROJECT_ROOT / "results" / name, project / "results" / name)

    test_names = sorted(REQUIRED_ANALYZER_JUNIT_TESTS)
    cases = "".join(
        f'<testcase classname="isolated" name="{name}"/>' for name in test_names
    )
    analyzer_junit = (
        f'<testsuite tests="{len(test_names)}" failures="0" errors="0" skipped="0">'
        + cases
        + "</testsuite>"
    )
    (project / "results" / "POSTRUN_ANALYZER_PYTEST.xml").write_text(
        analyzer_junit, encoding="utf-8"
    )
    analyzer_hash = reviewed_code_tree_sha256(project)
    authority = {
        "analyzer_code_sha256": analyzer_hash,
        "candidate_id": CANDIDATE_ID,
        "execution_code_sha256": EXPECTED_EXECUTION_TREE_SHA256,
        "review_round": 2,
        "reviewer_independent": True,
        "source_lock_sha256": EXPECTED_LOCK_SHA256,
        "verdict": "POSTRUN_ANALYZER_PASS",
    }
    review = project / "results" / "POSTRUN_ANALYZER_REVIEW.md"
    review.write_bytes(
        stable_file_bytes(review)
        + b"\n"
        + POSTRUN_AUTHORITY_PREFIX.encode("utf-8")
        + json.dumps(authority, sort_keys=True, separators=(",", ":")).encode("utf-8")
        + b"\n"
    )
    return project


def _preflight() -> dict:
    payload = {key: None for key in PRE_EXECUTION_KEYS}
    payload.update(
        {
            "schema": "CAT_TORSION_PRE_EXECUTION_AUDIT_V1",
            "candidate_id": "cat_torsion_primitive_divisor_capacity_v1",
            "source_lock_sha256": "x" * 64,
            "reviewed_code_sha256": "y" * 64,
            "gates": {"nested": {"pass": True}},
            "independent_review": {"pass": True},
            "registered_exact_audits": 0,
            "registered_periods_executed": [],
            "candidate_numerical_runs": 0,
            "external_prime_tables_accessed": False,
            "generated_prime_target_arrays": 0,
            "riemann_zero_data_accessed": False,
            "floating_or_approximate_matching_used": False,
            "status": "AUTHORIZED_FOR_REGISTERED_EXECUTION",
            "pass": True,
        }
    )
    return payload


def test_manifest_rejects_nested_forgery():
    live = _preflight()
    official = _preflight()
    assert validate_official_preflight(official, live) == []
    official["gates"]["nested"]["pass"] = False
    assert "OFFICIAL_PREFLIGHT_NOT_LIVE_CANONICAL_SNAPSHOT" in validate_official_preflight(
        official, live
    )
    official = _preflight()
    official["gates"] = {}
    assert validate_official_preflight(official, live)


def test_junit_parser_requires_all_passing_security_tests(tmp_path):
    names = sorted(REQUIRED_JUNIT_TESTS)
    cases = "".join(f'<testcase classname="safe" name="{name}"/>' for name in names)
    xml = (
        f'<testsuite tests="{len(names)}" failures="0" errors="0" skipped="0">'
        + cases
        + "</testsuite>"
    )
    path = tmp_path / "pytest.xml"
    path.write_text(xml, encoding="utf-8")
    assert parse_passing_junit(path)["pass"] is True
    failing = (
        f'<testsuite tests="{len(names)}" failures="1" errors="0" skipped="0">'
        + cases
        + "</testsuite>"
    )
    path.write_text(failing, encoding="utf-8")
    assert parse_passing_junit(path)["pass"] is False


def test_dual_tree_junit_roles_allow_hash_change_but_not_malformed_evidence():
    preflight = load_exact_json(PROJECT_ROOT / "results" / "PRE_EXECUTION_AUDIT.json")
    execution_gate = preflight["gates"]["test_evidence"]
    postrun = parse_passing_junit(
        PROJECT_ROOT / "results" / "pytest.xml",
        required_tests=REQUIRED_JUNIT_TESTS,
        stage="R091_EXECUTION_TREE_POSTRUN_TEST_EVIDENCE",
        display_path="results/pytest.xml",
    )
    separated = validate_junit_role_separation(execution_gate, postrun)
    assert separated["pass"] is True
    assert separated["content_changed_after_execution"] is True
    assert (
        separated["execution_authorization_junit"]["sha256"]
        != separated["execution_postrun_junit"]["sha256"]
    )
    malformed = json.loads(json.dumps(postrun))
    malformed["totals"]["failures"] = 1
    assert validate_junit_role_separation(execution_gate, malformed)["pass"] is False
    malformed_gate = json.loads(json.dumps(execution_gate))
    malformed_gate["sha256"] = "0" * 64
    assert validate_junit_role_separation(malformed_gate, postrun)["pass"] is False


def test_execution_chain_rejects_malformed_preflight_and_claim():
    results = PROJECT_ROOT / "results"
    preflight = load_exact_json(results / "PRE_EXECUTION_AUDIT.json")
    claim = load_exact_json(results / "registered_run.claim.json")
    result = load_exact_json(results / "EXPERIMENT_RESULTS.json")
    terminal = load_exact_json(results / "registered_run.json")
    assert validate_execution_chain_payloads(
        preflight, claim, result, terminal, EXPECTED_RAW_HASHES
    )["pass"] is True
    bad_preflight = json.loads(json.dumps(preflight))
    bad_preflight["gates"]["test_evidence"]["pass"] = False
    assert validate_execution_chain_payloads(
        bad_preflight, claim, result, terminal, EXPECTED_RAW_HASHES
    )["pass"] is False
    bad_claim = json.loads(json.dumps(claim))
    bad_claim["reviewed_code_sha256"] = "0" * 64
    assert validate_execution_chain_payloads(
        preflight, bad_claim, result, terminal, EXPECTED_RAW_HASHES
    )["pass"] is False
    missing_key = json.loads(json.dumps(claim))
    del missing_key["pre_execution_audit_sha256"]
    assert validate_execution_chain_payloads(
        preflight, missing_key, result, terminal, EXPECTED_RAW_HASHES
    )["pass"] is False


def test_postrun_official_preflight_is_immutable():
    with pytest.raises(RuntimeError):
        write_safe_preflight(PROJECT_ROOT)


def test_postrun_manifest_write_is_one_shot_and_finally_closed(tmp_path):
    project = _isolated_postrun_project(tmp_path)
    assert build_post_run_manifest(project)["pass"] is True
    output = write_post_run_manifest(project)
    assert output == project / "results" / "result_manifest.json"
    closure = validate_existing_post_run_manifest(project)
    assert closure["pass"] is True
    assert closure["manifest_sha256"] is not None
    assert "result_manifest.json" in closure["observed_result_files"]
    assert build_post_run_manifest(project)["pass"] is False
    with pytest.raises(FileExistsError):
        write_post_run_manifest(project)


def test_existing_postrun_manifest_rejects_changed_missing_extra_symlink_and_json_tampering(
    tmp_path,
):
    attacks = (
        "changed",
        "missing",
        "extra",
        "symlink",
        "duplicate_key",
        "malformed",
        "unknown_key",
        "wrong_type",
        "tampered_semantics",
    )
    for attack in attacks:
        project = _isolated_postrun_project(tmp_path / attack)
        manifest_path = write_post_run_manifest(project)
        assert validate_existing_post_run_manifest(project)["pass"] is True
        results = project / "results"
        if attack == "changed":
            raw_result = results / "EXPERIMENT_RESULTS.json"
            raw_result.write_bytes(stable_file_bytes(raw_result) + b" ")
        elif attack == "missing":
            (results / "AUTHOR_POSTRUN_ROUND1_REPAIR_NOT_INDEPENDENT.md").unlink()
        elif attack == "extra":
            (results / "unexpected.txt").write_text("extra", encoding="utf-8")
        elif attack == "symlink":
            target = results / "AUTHOR_POSTRUN_ROUND1_REPAIR_NOT_INDEPENDENT.md"
            external = project / "external-author-note.md"
            external.write_bytes(stable_file_bytes(target))
            target.unlink()
            target.symlink_to(external)
        elif attack == "duplicate_key":
            raw = stable_file_bytes(manifest_path)
            manifest_path.write_bytes(
                b'{\n  "schema": "duplicate",\n' + raw[2:]
            )
        elif attack == "malformed":
            manifest_path.write_bytes(b"{")
        else:
            payload = load_exact_json(manifest_path)
            if attack == "unknown_key":
                payload["unexpected"] = False
            elif attack == "wrong_type":
                payload["registered_exact_audits"] = True
            else:
                payload["execution_tree"]["sha256"] = "0" * 64
            write_json(manifest_path, payload)
        assert validate_existing_post_run_manifest(project)["pass"] is False, attack
