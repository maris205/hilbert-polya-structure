import json
from pathlib import Path

from action_audit.protocol import (
    EXPECTED_LOCK_SHA256,
    static_executable_isolation_scan,
    validate_source_lock,
)


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def test_source_lock_v3_validation_passes():
    record = validate_source_lock(PROJECT_ROOT / "experiments" / "source_lock.json")
    assert record["pass"]
    assert record["sha256"] == EXPECTED_LOCK_SHA256


def test_source_lock_has_zero_candidate_execution():
    record = validate_source_lock(PROJECT_ROOT / "experiments" / "source_lock.json")
    assert record["prelock_execution_clean"]


def test_source_lock_closes_all_independent_repairs():
    record = validate_source_lock(PROJECT_ROOT / "experiments" / "source_lock.json")
    assert all(record["repair_closure"].values())


def test_modified_source_lock_fails_hash(tmp_path):
    source = PROJECT_ROOT / "experiments" / "source_lock.json"
    payload = json.loads(source.read_text(encoding="utf-8"))
    payload["positioning"] += " altered"
    changed = tmp_path / "source_lock.json"
    changed.write_text(json.dumps(payload), encoding="utf-8")
    assert not validate_source_lock(changed)["pass"]


def test_executable_isolation_scan_passes_current_code():
    record = static_executable_isolation_scan(PROJECT_ROOT / "code")
    assert record["pass"]
    assert record["findings"] == []
    assert "action_audit/protocol.py" in record["scanned_files"]


def test_executable_isolation_rejects_network_import(tmp_path):
    (tmp_path / "bad.py").write_text("import requests\n", encoding="utf-8")
    record = static_executable_isolation_scan(tmp_path)
    assert not record["pass"]
    assert record["findings"][0]["kind"] == "forbidden_import"


def test_executable_isolation_rejects_network_import_inside_protocol_filename(tmp_path):
    (tmp_path / "protocol.py").write_text("import requests\n", encoding="utf-8")
    record = static_executable_isolation_scan(tmp_path)
    assert not record["pass"]
    assert record["scanned_files"] == ["protocol.py"]
    assert record["findings"][0]["kind"] == "forbidden_import"


def test_executable_isolation_rejects_float_literal(tmp_path):
    (tmp_path / "bad.py").write_text("threshold = 0.001\n", encoding="utf-8")
    record = static_executable_isolation_scan(tmp_path)
    assert not record["pass"]
    assert record["findings"][0]["kind"] == "floating_literal"
