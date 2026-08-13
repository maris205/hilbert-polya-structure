from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys

from branch_baker import protocol


SCRIPT = protocol.CODE_ROOT / "scripts" / "analyze_carrier.py"


def write(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload), encoding="utf-8")


def base_payloads(tmp_path: Path) -> dict[str, Path]:
    lock_hash = protocol.sha256_file(protocol.SOURCE_LOCK_PATH)
    shared = {
        "candidate_id": "pcf_markov_baker_v1",
        "source_lock_sha256": lock_hash,
        "external_prime_or_zero_data_accessed": False,
        "passed": True,
    }
    preflight = dict(shared) | {
        "gates": {
            "algebra": True,
            "candidate_cycle_ledger": True,
            "single_boundary_quotient": True,
            "zeta_conventions": True,
            "controls": True,
            "static_isolation": True,
        }
    }
    ledger = dict(shared) | {
        "max_period": 20,
        "primitive_counts": [0, 2, 0, 1, 0, 2, 0, 3, 0, 6, 0, 9, 0, 18, 0, 30, 0, 56, 0, 99],
        "independent_direct_counts": [0, 2, 0, 1, 0, 2, 0, 3, 0, 6, 0, 9, 0, 18, 0, 30, 0, 56, 0, 99],
        "primitive_total": 226,
        "ledger_agreement": True,
        "parent_boundary_quotient": {"primitive_count_delta": [1, -1] + [0] * 18},
    }
    parent = dict(shared) | {
        "digits": 100,
        "max_period": 20,
        "frozen_scale_executed": True,
        "frozen_protocol_passed": True,
        "thresholds": {
            "configured_residual_target": "1e-75",
            "effective_residual_target": "1e-75",
        },
        "postcritical": {"max_abs_residual": "0"},
        "periodic_factor": {"max_periodic_residual": "0"},
    }
    float_payload = dict(shared) | {
        "split": "development",
        "seed": 9296786003925294372,
        "points": 65536,
        "steps": 256,
        "frozen_scale_executed": True,
        "expected_checks": 65536 * 256,
        "completed_checks": 65536 * 256,
        "edge_mismatches": 0,
        "boundary_failures": 0,
        "max_roundtrip_error": 0.0,
        "thresholds": {"max_roundtrip_error": 2e-13},
    }
    paths: dict[str, Path] = {}
    for name, filename, payload in (
        ("preflight", "exact_preflight.json", preflight),
        ("ledger", "ledger.json", ledger),
        ("parent", "parent_audit.json", parent),
        ("float", "float_stress_development.json", float_payload),
    ):
        paths[name] = tmp_path / filename
        write(paths[name], payload)
    return paths


def run_analysis(paths: dict[str, Path], output: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--split",
            "development",
            "--diagnostic-input-dir",
            str(paths["preflight"].parent),
            "--output",
            str(output),
        ],
        cwd=protocol.PROJECT_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


def test_analysis_accepts_only_full_frozen_schema(tmp_path: Path) -> None:
    paths = base_payloads(tmp_path)
    output = tmp_path / "analysis.json"
    result = run_analysis(paths, output)
    assert result.returncode == 0, result.stderr
    payload = json.loads(output.read_text(encoding="utf-8"))
    assert payload["route_a_status"] == "A0_FAIL / STRUCTURAL_ONLY"
    assert payload["passed"] is True


def test_analysis_rejects_reduced_parent_audit(tmp_path: Path) -> None:
    paths = base_payloads(tmp_path)
    parent = json.loads(paths["parent"].read_text(encoding="utf-8"))
    parent["frozen_scale_executed"] = False
    write(paths["parent"], parent)
    result = run_analysis(paths, tmp_path / "analysis.json")
    assert result.returncode != 0
    assert "frozen scale" in result.stderr


def test_analysis_rejects_reduced_float_stress(tmp_path: Path) -> None:
    paths = base_payloads(tmp_path)
    stress = json.loads(paths["float"].read_text(encoding="utf-8"))
    stress["frozen_scale_executed"] = False
    stress["points"] = 1
    stress["steps"] = 1
    write(paths["float"], stress)
    result = run_analysis(paths, tmp_path / "analysis.json")
    assert result.returncode != 0
    assert "points differ" in result.stderr or "frozen scale" in result.stderr


def test_analysis_rejects_missing_external_data_declaration(tmp_path: Path) -> None:
    paths = base_payloads(tmp_path)
    ledger = json.loads(paths["ledger"].read_text(encoding="utf-8"))
    del ledger["external_prime_or_zero_data_accessed"]
    write(paths["ledger"], ledger)
    result = run_analysis(paths, tmp_path / "analysis.json")
    assert result.returncode != 0
    assert "mandatory field" in result.stderr
