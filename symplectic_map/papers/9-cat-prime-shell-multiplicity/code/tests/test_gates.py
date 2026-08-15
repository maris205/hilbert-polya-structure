from __future__ import annotations

from pathlib import Path

from prime_shell.gates import (
    source_schema_contract,
    validate_source_and_design,
    validate_upstream,
)


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def test_live_source_design_and_upstream_bindings_pass() -> None:
    assert validate_source_and_design(PROJECT_ROOT)["pass"] is True
    assert validate_upstream(PROJECT_ROOT)["pass"] is True
    contract = source_schema_contract(PROJECT_ROOT)
    assert contract["pass"] is True
    assert contract["embedded_proof_only_contract"]["centralizer_computations_run"] == 0
