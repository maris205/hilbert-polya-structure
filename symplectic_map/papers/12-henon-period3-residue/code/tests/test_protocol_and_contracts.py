"""Strict serialization, source binding, P1-P10, and negative-control tests."""

from __future__ import annotations

import json

import pytest

from bootstrap.contracts import collect_contract_witnesses
from bootstrap.controls import NEGATIVE_FIXTURES, reject_request, run_negative_controls
from bootstrap.manifest import code_inventory, validate_source_package
from bootstrap.protocol import (
    DuplicateJSONKeyError,
    canonical_json_bytes,
    exact_json,
    exact_same,
    strict_json_loads,
    validate_canonical_json_file,
)
from conftest import PROJECT_ROOT


def test_strict_json_rejects_duplicate_float_and_nonfinite():
    with pytest.raises(DuplicateJSONKeyError):
        strict_json_loads('{"a":1,"a":2}')
    with pytest.raises(ValueError):
        strict_json_loads('{"a":1.25}')
    with pytest.raises(ValueError):
        strict_json_loads('{"a":NaN}')


def test_exact_json_rejects_nonexact_types_and_bool_integer_confusion():
    assert exact_same(0, False) is False
    assert exact_same([1, 2], (1, 2)) is False
    assert canonical_json_bytes({"z": [2, 1], "a": 0}) == b'{"a":0,"z":[2,1]}'
    with pytest.raises(TypeError):
        exact_json({"bad": 1.0})
    with pytest.raises(TypeError):
        exact_json({1: "bad-key"})


def test_canonical_file_validation_rejects_pretty_equivalent(tmp_path):
    canonical = tmp_path / "canonical.json"
    canonical.write_bytes(b'{"a":1,"b":[2]}')
    assert validate_canonical_json_file(canonical) == {"a": 1, "b": [2]}
    pretty = tmp_path / "pretty.json"
    pretty.write_text(json.dumps({"a": 1}, indent=2) + "\n")
    with pytest.raises(ValueError):
        validate_canonical_json_file(pretty)


def test_bound_source_package_is_exact():
    record = validate_source_package(PROJECT_ROOT)
    assert record["status"] == "VALID"
    assert record["errors"] == []
    assert record["source_lock_sha256"] == "2fa930f697f6040cb16916d2b4dba7ec591a712882c108848e9eecf53608e1c2"
    assert record["source_review_sha256"] == "5e66edcd7f33769f748c8b6bd6582aa7e05b3325329839c46bf3627945803d11"
    assert record["proof_sha256"] == "36f2edd5a1a25960a2c656adaeb07fbd4251c61b51c9e0a0382200460b589ba9"


def test_p1_p10_contracts_are_presence_records_not_proof_verdicts():
    inventory = code_inventory(PROJECT_ROOT / "code")
    assert inventory["status"] == "CLOSED"
    records = collect_contract_witnesses(PROJECT_ROOT, set(inventory["files"]))
    assert [record["contract_id"] for record in records] == ["P" + str(i) for i in range(1, 11)]
    p7 = records[6]
    assert p7["source_anchor_count"] == 26
    assert len(p7["implementation_subwitnesses"]) == 11
    serialized = canonical_json_bytes(records).lower()
    assert b'"proved"' not in serialized
    assert b'"theorem_pass"' not in serialized


def test_all_eight_negative_controls_reject_before_science():
    records = run_negative_controls()
    assert len(records) == 8
    assert [record["control_id"] for record in records] == ["K00" + str(i) for i in range(1, 9)]
    assert all(record["outcome"] == "REJECTED_BEFORE_SCIENTIFIC_DISPATCH" for record in records)
    assert all(record["scientific_engine_dispatch_count"] == 0 for record in records)
    mutated = dict(NEGATIVE_FIXTURES[0])
    mutated["request"] = "different"
    with pytest.raises(ValueError):
        reject_request(mutated)
