import json
from pathlib import Path

import pytest

from henon_audit.preflight import parameter_preflight, proof_dependency_audit, symplectic_identity_audit
from henon_audit.manifest import (
    collect_artifacts,
    parse_audit_front_matter,
    render_audit_front_matter,
    validate_official_report_linkage,
)
from henon_audit.protocol import static_target_isolation_scan, validate_source_lock
from henon_audit.scope import scope_audit


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def test_immutable_source_lock_and_clean_prelock_state():
    record = validate_source_lock(PROJECT_ROOT / "experiments" / "source_lock.json")
    assert record["prelock_execution_clean"]
    assert record["pass"]


def test_executable_has_no_target_or_network_dependency():
    record = static_target_isolation_scan(PROJECT_ROOT / "code")
    assert record["findings"] == []
    assert record["pass"]


def test_isolation_scanner_detects_seeded_forbidden_paths_arrays_and_calls(tmp_path):
    code = tmp_path / "code"
    code.mkdir()
    (code / "bad.py").write_text(
        "import requests\n"
        "prime_targets = [2, 3, 5]\n"
        "values = open('riemann_zeros.csv').read()\n"
        "candidate = nsimplify(1.999999, tolerance=1e-5)\n",
        encoding="utf-8",
    )
    record = static_target_isolation_scan(code)
    kinds = {item["kind"] for item in record["findings"]}
    assert "forbidden_import" in kinds
    assert "embedded_target_array" in kinds
    assert "forbidden_target_path_literal" in kinds
    assert "forbidden_call" in kinds
    assert not record["pass"]


def test_isolation_scanner_detects_aliased_path_and_custom_tolerance(tmp_path):
    code = tmp_path / "code"
    code.mkdir()
    (code / "alias_escape.py").write_text(
        "from pathlib import Path\n"
        "prime_file = 'riemann_zeros.csv'\n"
        "payload = Path(prime_file).read_text()\n"
        "is_exact = abs(value - 2) < 1e-5\n",
        encoding="utf-8",
    )
    record = static_target_isolation_scan(code)
    kinds = {item["kind"] for item in record["findings"]}
    assert "suspicious_target_path_alias" in kinds
    assert "forbidden_target_path_literal" in kinds
    assert "tolerance_exactness_promotion" in kinds
    assert not record["pass"]


def test_manifest_collector_hashes_explicit_set_and_fails_closed(tmp_path):
    first = tmp_path / "first.json"
    second = tmp_path / "second.md"
    first.write_text("{}\n", encoding="utf-8")
    second.write_text("ok\n", encoding="utf-8")
    artifacts = collect_artifacts(tmp_path, [first, second])
    assert sorted(artifacts) == ["first.json", "second.md"]
    assert all(len(record["sha256"]) == 64 for record in artifacts.values())
    missing = tmp_path / "missing.txt"
    try:
        collect_artifacts(tmp_path, [missing])
    except FileNotFoundError as error:
        assert "missing.txt" in str(error)
    else:
        raise AssertionError("missing final artifacts must fail closed")


def _write_linked_official_report_fixture(tmp_path):
    results = tmp_path / "results"
    experiments = tmp_path / "experiments"
    results.mkdir(exist_ok=True)
    experiments.mkdir(exist_ok=True)
    summary = {
        "candidate_id": "integral_area_henon_multiplier_support_v1",
        "mode": "full_exact_audit",
        "status": "PASS",
        "candidate_executed": True,
        "must_run_failed": 0,
        "run_registry": [
            {"run_id": "R000", "status": "PASS"},
            {"run_id": "R001", "status": "PASS"},
        ],
    }
    candidate = {
        "candidate_id": "integral_area_henon_multiplier_support_v1",
        "pass": True,
    }
    (results / "run_summary.json").write_text(
        json.dumps(summary) + "\n", encoding="utf-8"
    )
    (results / "candidate_multiplier_audit.json").write_text(
        json.dumps(candidate) + "\n", encoding="utf-8"
    )
    (results / "pytest.xml").write_text("<testsuite failures='0'/>\n", encoding="utf-8")

    from henon_audit.protocol import sha256_file

    run_hash = sha256_file(results / "run_summary.json")
    candidate_hash = sha256_file(results / "candidate_multiplier_audit.json")
    pytest_hash = sha256_file(results / "pytest.xml")
    common = {
        "schema_version": 1,
        "candidate_id": "integral_area_henon_multiplier_support_v1",
        "official_full_run_status": "PASS",
        "run_summary_sha256": run_hash,
        "candidate_audit_sha256": candidate_hash,
    }
    (experiments / "EXPERIMENT_TRACKER.md").write_text(
        render_audit_front_matter(
            common | {"artifact": "experiment_tracker"}
        )
        + "\n# Tracker\n\n"
        + "| Run | Purpose | Status | Notes |\n"
        + "|---|---|---|---|\n"
        + "| R000 | lock | PASS | exact |\n"
        + "| R001 | scan | PASS | exact |\n",
        encoding="utf-8",
    )
    (results / "EXPERIMENT_RESULTS.md").write_text(
        render_audit_front_matter(
            common
            | {
                "artifact": "experiment_results",
                "candidate_executed": True,
                "must_run_failed": 0,
            }
        )
        + "\n# Results\n\nThe exact full run completed.\n",
        encoding="utf-8",
    )
    (results / "VALIDATION_REPORT.md").write_text(
        render_audit_front_matter(
            common
            | {
                "artifact": "validation_report",
                "pytest_status": "PASS",
                "pytest_xml_sha256": pytest_hash,
            }
        )
        + "\n# Validation\n\nAll checks passed.\n",
        encoding="utf-8",
    )
    return results, experiments, common


def test_official_report_linkage_rejects_placeholders_and_validates_hashes(tmp_path):
    results, _experiments, _common = _write_linked_official_report_fixture(tmp_path)
    assert validate_official_report_linkage(tmp_path)["status"] == "PASS"

    (results / "EXPERIMENT_RESULTS.md").write_text(
        "PENDING_OFFICIAL_FULL_RUN\n", encoding="utf-8"
    )
    with pytest.raises(ValueError, match="exactly one"):
        validate_official_report_linkage(tmp_path)


def test_official_report_metadata_rejects_contradiction_duplicate_and_unknown_state(tmp_path):
    results, experiments, common = _write_linked_official_report_fixture(tmp_path)
    tracker = experiments / "EXPERIMENT_TRACKER.md"
    experiment_results = results / "EXPERIMENT_RESULTS.md"

    # Round-3 reviewer repro: a legacy contradictory human field cannot
    # coexist beside the unique JSON authority.
    experiment_results.write_text(
        experiment_results.read_text(encoding="utf-8")
        + "\n**Official full-run status:** `FAIL`\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="forbidden legacy machine status fields"):
        validate_official_report_linkage(tmp_path)

    _write_linked_official_report_fixture(tmp_path)
    tracker.write_text(
        tracker.read_text(encoding="utf-8")
        + "| R001 | stale duplicate | FAIL | contradiction |\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="duplicate run IDs"):
        validate_official_report_linkage(tmp_path)

    _write_linked_official_report_fixture(tmp_path)
    bad_meta = common | {
        "artifact": "experiment_results",
        "candidate_executed": True,
        "must_run_failed": 0,
        "unknown_status": "MAYBE",
    }
    experiment_results.write_text(
        render_audit_front_matter(bad_meta) + "\n# Results\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="metadata schema mismatch"):
        validate_official_report_linkage(tmp_path)


@pytest.mark.parametrize(
    "legacy_line",
    [
        "  **Official full-run status:** `FAIL`",
        "\t**Candidate executed:** `false`",
        "> **Must-run failed:** `7`",
        ">\t- **Pytest status:** `FAIL`",
        "- **Run-summary SHA-256:** `stale`",
        "1. **Candidate-audit SHA-256:** `stale`",
        "+ **Pytest XML SHA-256:** `stale`",
    ],
)
def test_official_report_rejects_indented_quote_and_list_legacy_fields(
    tmp_path, legacy_line
):
    results, _experiments, _common = _write_linked_official_report_fixture(tmp_path)
    report = results / "EXPERIMENT_RESULTS.md"
    report.write_text(
        report.read_text(encoding="utf-8") + f"\n{legacy_line}\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="forbidden legacy machine status fields"):
        validate_official_report_linkage(tmp_path)


def test_official_report_does_not_flag_ordinary_narrative_field_mention(tmp_path):
    results, _experiments, _common = _write_linked_official_report_fixture(tmp_path)
    report = results / "EXPERIMENT_RESULTS.md"
    report.write_text(
        report.read_text(encoding="utf-8")
        + "\nFor context, the phrase **Official full-run status:** is machine-reserved.\n",
        encoding="utf-8",
    )
    assert validate_official_report_linkage(tmp_path)["status"] == "PASS"


def test_front_matter_requires_one_block_and_unique_json_keys(tmp_path):
    report = tmp_path / "report.md"
    payload = {
        "schema_version": 1,
        "artifact": "experiment_tracker",
        "candidate_id": "integral_area_henon_multiplier_support_v1",
        "official_full_run_status": "PASS",
        "run_summary_sha256": "a" * 64,
        "candidate_audit_sha256": "b" * 64,
    }
    block = render_audit_front_matter(payload)
    report.write_text(block + block, encoding="utf-8")
    with pytest.raises(ValueError, match="exactly one"):
        parse_audit_front_matter(report, "experiment_tracker")

    report.write_text(
        "<!-- HENON_AUDIT_META_V1\n"
        '{"schema_version":1,"schema_version":1,'
        '"artifact":"experiment_tracker",'
        '"candidate_id":"integral_area_henon_multiplier_support_v1",'
        '"official_full_run_status":"PASS",'
        f'"run_summary_sha256":"{"a" * 64}",'
        f'"candidate_audit_sha256":"{"b" * 64}"}}\n'
        "HENON_AUDIT_META_V1_END -->\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="duplicate JSON metadata keys"):
        parse_audit_front_matter(report, "experiment_tracker")


def test_proof_parameter_and_symplectic_preflights_pass():
    assert proof_dependency_audit(PROJECT_ROOT / "notes" / "PROOF_PACKAGE.md")["pass"]
    assert parameter_preflight()["pass"]
    assert symplectic_identity_audit()["pass"]


def test_proof_prose_equivalent_rewrite_is_advisory_not_blocking(tmp_path):
    original = (PROJECT_ROOT / "notes" / "PROOF_PACKAGE.md").read_text(encoding="utf-8")
    rewritten = original.replace(
        "every\npositive-dimensional projective subvariety",
        "any\npositive-dimensional projective subvariety",
        1,
    )
    assert rewritten != original
    proof = tmp_path / "PROOF_PACKAGE.md"
    proof.write_text(rewritten, encoding="utf-8")
    record = proof_dependency_audit(proof)
    assert not record["advisory_prose_checks"]["positive_dimension_hyperplane_argument"]
    assert record["natural_language_checks_are_blocking"] is False
    assert record["pass"]


def test_proof_duplicate_stable_id_remains_blocking(tmp_path):
    original = (PROJECT_ROOT / "notes" / "PROOF_PACKAGE.md").read_text(encoding="utf-8")
    proof = tmp_path / "PROOF_PACKAGE.md"
    proof.write_text(
        original + "\n<!-- HENON_PROOF_EQUATION_ID: CYCLIC_RECURRENCE -->\n",
        encoding="utf-8",
    )
    record = proof_dependency_audit(proof)
    assert not record["structural_checks"]["each_required_equation_id_unique"]
    assert not record["pass"]


def test_scope_guards_reject_overclaims():
    assert scope_audit()["pass"]
