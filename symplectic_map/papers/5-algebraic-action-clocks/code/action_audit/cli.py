"""Ordered execution of the source-locked exact static audit."""

from __future__ import annotations

import argparse
import json
import platform
import resource
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

import sympy as sp

from .algebraic import proof_dependency_audit
from .controls import run_controls
from .henon import (
    henon_static_identity_audit,
    projective_infinity_audit,
    recurrence_multiplicity_audit,
    s_integral_denominator_ledger,
)
from .protocol import sha256_file, static_executable_isolation_scan, validate_source_lock


def _write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _timed(label: str, callback: Callable[[], Any], timings: dict[str, str]) -> Any:
    start = time.perf_counter_ns()
    result = callback()
    elapsed_ns = time.perf_counter_ns() - start
    # Integer nanoseconds avoid floating literals in the exact executable.
    timings[label] = str(elapsed_ns)
    return result


def _peak_memory_kib() -> int:
    return int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)


def _environment(project_root: Path, timings: dict[str, str]) -> dict[str, Any]:
    source_files = sorted((project_root / "code").rglob("*.py"))
    execution_time = datetime.now(timezone.utc)
    return {
        "candidate_id": "algebraic_exact_action_clock_obstruction_v1",
        "execution_date_utc": execution_time.date().isoformat(),
        "execution_timestamp_utc": execution_time.isoformat().replace("+00:00", "Z"),
        "document_lock_date_policy": "source-lock and plan dates are frozen document metadata; runtime date is generated from the UTC clock",
        "python": sys.version,
        "python_executable": sys.executable,
        "platform": platform.platform(),
        "sympy": sp.__version__,
        "gpu_used": False,
        "arithmetic": "exact SymPy symbolic identities and categorical dependency checks",
        "floating_point_used_as_evidence": False,
        "external_prime_tables_accessed": False,
        "riemann_zero_data_accessed": False,
        "network_access_by_executable": False,
        "candidate_parameter_substituted": False,
        "candidate_periodic_points_computed": False,
        "candidate_actions_computed": False,
        "timings_nanoseconds": timings,
        "peak_memory_kib": _peak_memory_kib(),
        "source_hashes": {
            str(path.relative_to(project_root)): sha256_file(path)
            for path in source_files
        },
    }


def run(project_root: Path) -> dict[str, Any]:
    """Run the complete static audit; candidate execution remains closed."""

    root = project_root.resolve()
    result_directory = root / "results"
    lock_path = root / "experiments" / "source_lock.json"
    proof_path = root / "notes" / "PROOF_PACKAGE.md"
    timings: dict[str, str] = {}
    registry: list[dict[str, str]] = []

    lock = _timed("R000", lambda: validate_source_lock(lock_path), timings)
    _write_json(result_directory / "source_lock_validation.json", lock)
    registry.append({"run_id": "R000", "status": "PASS" if lock["pass"] else "FAIL"})
    if not lock["pass"]:
        raise RuntimeError("R000 source-lock validation failed")

    isolation = _timed(
        "R001",
        lambda: static_executable_isolation_scan(root / "code"),
        timings,
    )
    _write_json(result_directory / "target_isolation_audit.json", isolation)
    registry.append({"run_id": "R001", "status": "PASS" if isolation["pass"] else "FAIL"})
    if not isolation["pass"]:
        raise RuntimeError("R001 executable-isolation scan failed")

    proof = _timed("R002", lambda: proof_dependency_audit(proof_path), timings)
    _write_json(result_directory / "proof_audit.json", proof)
    registry.append({"run_id": "R002", "status": "PASS" if proof["pass"] else "FAIL"})
    if not proof["pass"]:
        raise RuntimeError("R002 proof-dependency audit failed")

    # Mandatory controls-first gate.  No Hénon static identity is evaluated
    # until all normalization, endpoint, logarithm, and pole controls pass.
    controls = _timed("R010-R019", run_controls, timings)
    _write_json(result_directory / "control_audit.json", controls)
    registry.append({"run_id": "R010-R019", "status": "PASS" if controls["pass"] else "FAIL"})
    if not controls["pass"]:
        raise RuntimeError("controls-first gate failed")

    henon = _timed("R020", henon_static_identity_audit, timings)
    recurrence = _timed("R021", recurrence_multiplicity_audit, timings)
    infinity = _timed("R022", projective_infinity_audit, timings)
    integral = _timed("R023", s_integral_denominator_ledger, timings)
    static_records = {
        "henon_identity": henon,
        "recurrence_multiplicity": recurrence,
        "projective_infinity": infinity,
        "s_integral_denominator": integral,
    }
    _write_json(result_directory / "henon_static_audit.json", static_records)
    for run_id, record in (
        ("R020", henon),
        ("R021", recurrence),
        ("R022", infinity),
        ("R023", integral),
    ):
        registry.append({"run_id": run_id, "status": "PASS" if record["pass"] else "FAIL"})
        if not record["pass"]:
            raise RuntimeError(f"{run_id} static audit failed")

    environment = _environment(root, timings)
    _write_json(result_directory / "command_environment_manifest.json", environment)
    summary = {
        "candidate_id": lock["candidate_id"],
        "mode": "SOURCE_LOCKED_STATIC_AUDIT_ONLY",
        "source_lock_version": lock["lock_version"],
        "source_lock_sha256": lock["sha256"],
        "controls_executed_before_henon_static_audit": True,
        "run_registry": registry,
        "candidate_execution_gate": "CLOSED",
        "candidate_parameter_substituted": False,
        "candidate_periodic_points_computed": False,
        "candidate_actions_computed": False,
        "external_prime_tables_accessed": False,
        "riemann_zero_data_accessed": False,
        "all_period_result_source": "deductive proof plus Hermite--Lindemann; static computations are implementation audits only",
        "classification": "ALGEBRAIC_NORMALIZED_ACTION_CLOCK_REJECTED_BY_ALL_PERIOD_THEOREM",
        "status": "PASS_STATIC_CERTIFICATE_NO_CANDIDATE_EXECUTION",
    }
    _write_json(result_directory / "run_summary.json", summary)
    return summary


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--project-root",
        type=Path,
        default=Path(__file__).resolve().parents[2],
        help="Paper project root containing experiments/, notes/, code/, and results/",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    arguments = build_parser().parse_args(argv)
    summary = run(arguments.project_root)
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
