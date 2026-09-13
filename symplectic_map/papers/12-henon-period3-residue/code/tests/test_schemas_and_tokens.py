"""Closed definitions/ledger/types schemas and claim-bound token tests."""

from __future__ import annotations

import copy
import importlib.util
import ast

import pytest

from bootstrap.lifecycle import _validate_claim_types_schema, build_claim_object
from bootstrap.manifest import _definitions_findings, _ledger_findings
from bootstrap.protocol import load_exact_json
from conftest import CANDIDATE_ROOT, PROJECT_ROOT


def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError("module specification")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_definitions_and_private_ledger_are_recursively_closed():
    definitions = load_exact_json(CANDIDATE_ROOT / "shared/definitions.json")
    ledger = load_exact_json(CANDIDATE_ROOT / "adjudicator/acceptance_ledger.json")
    assert _definitions_findings(definitions) == []
    assert _ledger_findings(ledger) == []
    changed_definitions = copy.deepcopy(definitions)
    changed_definitions["category"]["answer"] = 7
    assert _definitions_findings(changed_definitions)
    changed_ledger = copy.deepcopy(ledger)
    changed_ledger["coefficient_boundary"]["expected_value_storage_count"] = False
    assert "PRIVATE_LEDGER_COEFFICIENT_EXPECTATION_PRESENT" in _ledger_findings(changed_ledger)
    planted = copy.deepcopy(ledger)
    planted["coefficient_boundary"]["comparison"] += ":MUTATED"
    assert "PRIVATE_LEDGER_BOUNDARY_COMPARISON" in _ledger_findings(planted)


def test_types_only_envelope_schema_is_nonhollow_and_recursive():
    adjudicator = _load(
        CANDIDATE_ROOT / "adjudicator/adjudicate.py", "paper12_adjudicator_schema_test"
    )
    schema = load_exact_json(CANDIDATE_ROOT / "shared/result_envelope.schema.json")
    adjudicator._a_validate_types_only_schema(schema)
    hollow = copy.deepcopy(schema)
    hollow["properties"]["quartic"] = {"type": "object"}
    with pytest.raises(ValueError):
        adjudicator._a_validate_types_only_schema(hollow)


def test_durable_claim_schema_matches_emitted_claim_shape():
    manifest = {
        "code_tree_sha256": "1" * 64,
        "definitions_sha256": "2" * 64,
        "preflight_sha256": "3" * 64,
    }
    claim = build_claim_object(manifest, "4" * 64, "5" * 64)
    _validate_claim_types_schema(PROJECT_ROOT, claim)
    bad = dict(claim)
    bad["registered_audit_count"] = True
    with pytest.raises(ValueError):
        _validate_claim_types_schema(PROJECT_ROOT, bad)


def test_track_capabilities_are_claim_and_code_hash_bound():
    q_runner = _load(CANDIDATE_ROOT / "track_q/runner.py", "paper12_q_runner_token_test")
    r_runner = _load(CANDIDATE_ROOT / "track_r/runner.py", "paper12_r_runner_token_test")
    digests = [character * 64 for character in "1234"]
    q_token = ("HENON_PERIOD3_TRACK_Q_START_V1:" + ":".join(digests) + "\n").encode()
    r_token = ("HENON_PERIOD3_TRACK_R_START_V1:" + ":".join(digests) + "\n").encode()
    assert q_runner._q_parse_capability(q_token)["claim_sha256"] == digests[0]
    assert r_runner._r_parse_capability(r_token)["engine_sha256"] == digests[2]
    with pytest.raises(RuntimeError):
        q_runner._q_parse_capability(b"HENON_PERIOD3_TRACK_Q_START_V1\n")


def test_postrun_analyzer_is_separate_and_science_free():
    path = PROJECT_ROOT / "code/postrun_analyzer/analyze.py"
    tree = ast.parse(path.read_text())
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module or "")
    assert set(imports) == {"__future__", "hashlib", "json", "os", "pathlib"}
    source = path.read_text()
    assert "track_q" not in source
    assert "track_r" not in source
    assert "run_science" not in source
