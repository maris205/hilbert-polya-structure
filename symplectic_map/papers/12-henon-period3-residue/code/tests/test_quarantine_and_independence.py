"""Registered-tuple quarantine and hash-specific science independence tests."""

from __future__ import annotations

import ast
import hashlib

import pytest

from conftest import CANDIDATE_ROOT, PROJECT_ROOT


def test_science_reviewed_hashes_are_unchanged():
    expected = {
        "track_q/engine.py": "e90654feec9dadc197944c9ce260507d5d1206a6055a235a08edfbd343553995",
        "track_r/engine.py": "4e6451c3adcd4f053f9cb87a2aecf00d5c8b678b4c4dc38e54e39523f39c4a17",
        "bootstrap/contracts.py": "ca20bf06b272d99cc2d2d16c94a9282ce4b8dfbb4654e112c9797bd6243221d3",
    }
    for relative, digest in expected.items():
        assert hashlib.sha256((CANDIDATE_ROOT / relative).read_bytes()).hexdigest() == digest


def test_science_modules_have_disjoint_import_free_roots():
    q_source = (CANDIDATE_ROOT / "track_q/engine.py").read_text()
    r_source = (CANDIDATE_ROOT / "track_r/engine.py").read_text()
    for source in (q_source, r_source):
        tree = ast.parse(source)
        assert not [node for node in ast.walk(tree) if isinstance(node, (ast.Import, ast.ImportFrom))]
    for token in ("H_value", "A_value", "generalized_binomial", "9.27", "9.28"):
        assert token not in q_source
    for token in ("_q_reduction_state", "admissible", "9.8", "9.9", "9.13"):
        assert token not in r_source
    assert not list((CANDIDATE_ROOT / "shared").glob("*.py"))


@pytest.mark.parametrize("value", [7, 10, True, None])
def test_q_outside_registered_tuple_rejected_before_computation(q_engine, value):
    with pytest.raises((TypeError, ValueError)):
        q_engine._q_registered_coefficient_diagnostic(value)


@pytest.mark.parametrize("value", [7, 10, True, None])
def test_r_outside_registered_tuple_rejected_before_computation(r_engine, value):
    with pytest.raises((TypeError, ValueError)):
        r_engine._r_registered_collapsed_diagnostic(value)


def test_no_official_or_runtime_artifact_exists_preexecution():
    assert not (PROJECT_ROOT / "runtime/candidate_v1").exists()
    assert not (PROJECT_ROOT / "runtime/candidate_v1/official/durable_claim.json").exists()
