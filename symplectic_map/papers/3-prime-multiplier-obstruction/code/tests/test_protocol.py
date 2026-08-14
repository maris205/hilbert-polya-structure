import json
from pathlib import Path

from prime_multiplier.protocol import (
    audit_proof_dependencies,
    json_safe,
    scan_executable_tree,
    validate_source_lock,
)


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def test_source_lock_is_valid_and_prerun_clean():
    record = validate_source_lock(
        PROJECT_ROOT / "experiments" / "source_lock.json",
        PROJECT_ROOT / "code",
    )
    assert record["status"] == "PASS"
    assert record["source_lock_sha256"]
    assert all(record["state_checks"].values())


def test_executable_tree_has_no_forbidden_external_access():
    record = scan_executable_tree(PROJECT_ROOT / "code")
    assert record["status"] == "PASS"
    assert record["findings"] == []


def test_proof_dependency_audit_preserves_open_boundary():
    record = audit_proof_dependencies(PROJECT_ROOT / "notes" / "PROOF_PACKAGE.md")
    assert record["status"] == "PASS"
    checks = {item["id"]: item["status"] for item in record["checklist"]}
    assert checks["p2_residue_explicitly_open"] == "PASS"
    assert checks["modulus_only_nonclaim"] == "PASS"


def test_source_lock_has_exact_frozen_periods():
    payload = json.loads((PROJECT_ROOT / "experiments" / "source_lock.json").read_text())
    assert payload["exact_low_period_audit"]["periods"] == [1, 2, 3, 4]
    assert payload["conditional_real_orbit_ledger"]["status"].startswith("DISABLED")


def test_json_safe_normalizes_sympy_scalars():
    import sympy as sp

    assert json_safe({"truth": sp.true, "count": sp.Integer(4), "ratio": sp.Rational(3, 4)}) == {
        "truth": True,
        "count": 4,
        "ratio": "3/4",
    }


def test_scanner_rejects_path_constructor_resource(tmp_path):
    code_root = tmp_path / "code"
    code_root.mkdir()
    (code_root / "bad.py").write_text(
        "from pathlib import Path\nPath('prime_table.txt').read_text()\n",
        encoding="utf-8",
    )
    record = scan_executable_tree(code_root)
    assert record["status"] == "FAIL"
    assert any(item["kind"] == "forbidden_resource_path" for item in record["findings"])


def test_scanner_rejects_process_access(tmp_path):
    code_root = tmp_path / "code"
    code_root.mkdir()
    (code_root / "bad.py").write_text(
        "import subprocess\nsubprocess.run(['wget', 'example.invalid'])\n",
        encoding="utf-8",
    )
    record = scan_executable_tree(code_root)
    kinds = {item["kind"] for item in record["findings"]}
    assert record["status"] == "FAIL"
    assert "process_import" in kinds
    assert "external_process_call" in kinds


def test_scanner_rejects_post_hoc_tolerance_configuration(tmp_path):
    code_root = tmp_path / "code"
    code_root.mkdir()
    (code_root / "runtime.toml").write_text("prime_tolerance = 0.01\n", encoding="utf-8")
    record = scan_executable_tree(code_root)
    assert record["status"] == "FAIL"
    assert any(item["kind"] == "forbidden_configuration_token" for item in record["findings"])
