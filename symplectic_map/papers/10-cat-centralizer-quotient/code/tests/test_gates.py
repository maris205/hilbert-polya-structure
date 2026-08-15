from pathlib import Path

from centralizer_q.gates import source_schema_contract, validate_source_and_design, validate_upstream


ROOT = Path(__file__).parents[2]


def test_source_design_and_upstream_bindings_pass() -> None:
    assert validate_source_and_design(ROOT)["pass"] is True
    assert validate_upstream(ROOT)["pass"] is True
    assert source_schema_contract(ROOT)["pass"] is True
