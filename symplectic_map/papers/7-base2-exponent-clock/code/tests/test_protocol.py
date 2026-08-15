from pathlib import Path

import pytest

from base2_clock.protocol import (
    CANDIDATE_ID,
    EXPECTED_LOCK_SHA256,
    DuplicateJSONKeyError,
    code_tree_inventory,
    executable_isolation_scan,
    load_exact_json,
    regular_file,
    strict_json_loads,
    validate_source_lock,
    validate_upstream_bindings,
)


PROJECT_ROOT = Path(__file__).absolute().parents[2]


def test_live_v2_source_lock_and_upstreams_match():
    source = validate_source_lock(PROJECT_ROOT)
    upstream = validate_upstream_bindings(PROJECT_ROOT)
    assert source["candidate_id"] == CANDIDATE_ID
    assert source["source_lock_sha256"] == EXPECTED_LOCK_SHA256
    assert source["pass"] is True
    assert upstream["pass"] is True


def test_strict_json_rejects_duplicate_keys():
    with pytest.raises(DuplicateJSONKeyError):
        strict_json_loads('{"a":1,"a":2}')


def test_strict_json_rejects_nonfinite_numbers():
    parsed = strict_json_loads('{"x":0.125}')
    assert type(parsed["x"]) is float
    assert parsed["x"].as_integer_ratio() == (1, 8)
    for text in ('{"x":NaN}', '{"x":Infinity}', '{"x":-Infinity}'):
        with pytest.raises(ValueError):
            strict_json_loads(text)


def test_exact_official_json_rejects_finite_float(tmp_path):
    path = tmp_path / "evidence.json"
    path.write_text('{"x":0.125}\n', encoding="utf-8")
    with pytest.raises(ValueError):
        load_exact_json(path)


def test_executable_isolation_scans_entire_code_tree():
    record = executable_isolation_scan(PROJECT_ROOT / "code")
    assert record["pass"] is True
    assert record["forbidden_access_count"] == 0
    assert "base2_clock/candidate.py" in record["scanned_python_files"]
    assert "scripts/run_registered_audit.py" in record["scanned_python_files"]


def test_scanner_rejects_dynamic_import_and_decimal_matching_fixture(tmp_path):
    code = tmp_path / "code"
    code.mkdir()
    (code / "bad.py").write_text("__import__('x')\nx = 0.125\n", encoding="utf-8")
    record = executable_isolation_scan(code)
    assert record["pass"] is False
    kinds = {item["kind"] for item in record["findings"]}
    assert {"closed_world_inventory_mismatch", "forbidden_call", "floating_literal"} <= kinds


def test_regular_file_and_inventory_reject_symlink_components(tmp_path):
    real = tmp_path / "real"
    real.mkdir()
    artifact = real / "artifact.json"
    artifact.write_text("{}\n", encoding="utf-8")
    alias = tmp_path / "alias"
    alias.symlink_to(real, target_is_directory=True)
    assert regular_file(alias / "artifact.json") is False

    code = tmp_path / "code"
    code.mkdir()
    (code / "alias.py").symlink_to(artifact)
    inventory = code_tree_inventory(code)
    assert inventory["pass"] is False
    assert inventory["symlinks"] == ["alias.py"]
