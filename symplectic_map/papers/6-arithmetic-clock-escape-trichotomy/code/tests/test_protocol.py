from pathlib import Path

from capacity_audit.protocol import (
    EXPECTED_LOCK_SHA256,
    static_executable_isolation_scan,
    validate_source_lock,
)


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def test_source_lock_v2_and_preexecution_provenance_pass():
    record = validate_source_lock(PROJECT_ROOT)
    assert record["pass"]
    assert record["sha256"] == EXPECTED_LOCK_SHA256
    assert record["history_bound"]
    assert record["execution_clean"]
    assert record["repairs_closed"]
    assert record["repair_count"] == 10
    assert record["formal_run_pre_review_closed"]


def test_static_isolation_scans_itself_and_script_wrappers():
    record = static_executable_isolation_scan(PROJECT_ROOT / "code")
    assert record["pass"]
    assert record["findings"] == []
    assert record["scanner_self_covered"]
    assert record["script_wrappers_covered"]


def test_static_isolation_rejects_network_import(tmp_path):
    (tmp_path / "bad.py").write_text("import requests\n", encoding="utf-8")
    record = static_executable_isolation_scan(tmp_path)
    assert not record["pass"]
    assert record["findings"][0]["kind"] == "forbidden_import"


def test_static_isolation_rejects_float_literal(tmp_path):
    (tmp_path / "bad.py").write_text("threshold = 0.001\n", encoding="utf-8")
    record = static_executable_isolation_scan(tmp_path)
    assert not record["pass"]
    assert record["findings"][0]["kind"] == "floating_literal"


def test_static_isolation_rejects_numeric_target_collection(tmp_path):
    (tmp_path / "bad.py").write_text("target_values = [4, 6]\n", encoding="utf-8")
    record = static_executable_isolation_scan(tmp_path)
    assert not record["pass"]
    assert record["findings"][0]["kind"] == "embedded_or_indirect_target_numeric_collection"


def test_static_isolation_rejects_unreviewed_file_read(tmp_path):
    (tmp_path / "bad.py").write_text("from pathlib import Path\nPath('x').read_text()\n", encoding="utf-8")
    record = static_executable_isolation_scan(tmp_path)
    assert not record["pass"]
    assert record["findings"][0]["kind"] == "unreviewed_file_read"


def test_static_isolation_rejects_aliased_dynamic_import(tmp_path):
    (tmp_path / "bad.py").write_text(
        "from importlib import import_module as loader\nloader('requests')\n",
        encoding="utf-8",
    )
    record = static_executable_isolation_scan(tmp_path)
    assert not record["pass"]
    assert {finding["kind"] for finding in record["findings"]} >= {
        "forbidden_import",
        "forbidden_call",
    }


def test_static_isolation_rejects_builtin_dynamic_import_and_getattr_log(tmp_path):
    (tmp_path / "bad.py").write_text(
        "module = __import__('math')\nfn = getattr(module, 'log')\nfn(4)\n",
        encoding="utf-8",
    )
    record = static_executable_isolation_scan(tmp_path)
    assert not record["pass"]
    assert any(finding["kind"] == "forbidden_call" for finding in record["findings"])


def test_static_isolation_rejects_indirect_target_array(tmp_path):
    (tmp_path / "bad.py").write_text(
        "values = [4, 6]\ntarget_values = values\n",
        encoding="utf-8",
    )
    record = static_executable_isolation_scan(tmp_path)
    assert not record["pass"]
    assert any(
        finding["kind"] == "embedded_or_indirect_target_numeric_collection"
        for finding in record["findings"]
    )
