from __future__ import annotations

from pathlib import Path

import pytest

from cat_torsion.protocol import (
    EXPECTED_LOCK_SHA256,
    load_exact_json,
    strict_json_loads,
    validate_source_lock,
    validate_upstream_bindings,
)
from cat_torsion.review_gate import reviewed_code_tree_sha256


PROJECT_ROOT = Path(__file__).absolute().parents[2]


def test_source_lock_local_and_upstream_bindings_are_live():
    source = validate_source_lock(PROJECT_ROOT)
    upstream = validate_upstream_bindings(PROJECT_ROOT)
    assert source["source_lock_sha256"] == EXPECTED_LOCK_SHA256
    assert source["pass"] is True
    assert upstream["pass"] is True
    assert len(upstream["records"]) == 7


def test_strict_json_rejects_duplicate_nonfinite_and_finite_float(tmp_path):
    with pytest.raises(ValueError):
        strict_json_loads('{"outer":{"x":1,"x":2}}')
    for constant in ("NaN", "Infinity", "-Infinity"):
        with pytest.raises(ValueError):
            strict_json_loads('{"x":' + constant + "}")
    path = tmp_path / "float.json"
    path.write_text('{"x":1.25}', encoding="utf-8")
    with pytest.raises(ValueError):
        load_exact_json(path)
    value = 1
    assert (type(value) is float) is False


def test_reviewed_tree_digest_is_stable_and_complete():
    first = reviewed_code_tree_sha256(PROJECT_ROOT)
    second = reviewed_code_tree_sha256(PROJECT_ROOT)
    assert first == second
    assert len(first) == 64
