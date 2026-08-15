from pathlib import Path

import pytest

import base2_clock.candidate as candidate_module
from base2_clock.candidate import REGISTERED_PERIODS, run_registered_candidate
from base2_clock.cli import build_parser
from base2_clock.manifest import (
    collect_safe_preflight,
    write_safe_preflight,
)


PROJECT_ROOT = Path(__file__).absolute().parents[2]


def test_registered_periods_are_fixed_without_cli_override():
    assert REGISTERED_PERIODS == tuple(range(2, 8))
    parser = build_parser()
    with pytest.raises(SystemExit):
        parser.parse_args(["registered", "--max-period", "4"])


def test_candidate_map_is_not_touched_when_deployment_gate_fails(monkeypatch):
    def blocked(_):
        raise RuntimeError("blocked before candidate")

    def forbidden_map():
        raise AssertionError("candidate map was accessed")

    monkeypatch.setattr(candidate_module, "_require_deployment_authority", blocked)
    monkeypatch.setattr(candidate_module, "candidate_map", forbidden_map)
    with pytest.raises(RuntimeError, match="blocked before candidate"):
        run_registered_candidate(PROJECT_ROOT)


def test_safe_preflight_reports_zero_registered_candidate_runs(tmp_path):
    record = collect_safe_preflight(PROJECT_ROOT)
    assert record["pass"] is True
    assert record["status"] in {
        "READY_FOR_INDEPENDENT_PRE_EXECUTION_REVIEW",
        "AUTHORIZED_FOR_REGISTERED_EXECUTION",
    }
    assert record["registered_candidate_runs"] == 0
    assert record["registered_candidate_periods_executed"] == []
    output = write_safe_preflight(PROJECT_ROOT, tmp_path)
    assert output == tmp_path / "PRE_EXECUTION_AUDIT.json"
    assert output.is_file()
