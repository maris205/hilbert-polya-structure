"""Ordered execution of the frozen exact audit."""

from __future__ import annotations

import argparse
import json
import platform
import resource
import sys
import time
from pathlib import Path
from typing import Any, Callable

import sympy as sp

from .algebra import PARAMETER_POLYNOMIAL, polynomial_record
from .controls import run_controls
from .modulus import candidate_modulus_audit, rational_trace_polynomial
from .periods import L, T, candidate_period_record, multiplier_polynomial, trace_polynomial
from .preflight import parameter_preflight, proof_dependency_audit, symplectic_identity_audit
from .protocol import sha256_file, static_target_isolation_scan, validate_source_lock
from .scope import scope_audit


def _write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _timed(label: str, callback: Callable[[], Any], timings: dict[str, float]) -> Any:
    start = time.perf_counter()
    value = callback()
    timings[label] = round(time.perf_counter() - start, 6)
    return value


def _peak_memory_mib() -> float:
    # Linux reports KiB for ru_maxrss.
    return round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0, 3)


def _core_environment(project_root: Path, timings: dict[str, float]) -> dict[str, Any]:
    source_files = sorted((project_root / "code").rglob("*.py"))
    return {
        "candidate_id": "integral_area_henon_multiplier_support_v1",
        "execution_date_utc": "2026-08-13",
        "python": sys.version,
        "python_executable": sys.executable,
        "platform": platform.platform(),
        "sympy": sp.__version__,
        "gpu_used": False,
        "arithmetic": "exact SymPy QQ polynomial/resultant/Groebner arithmetic",
        "candidate_parameter_approximation_used_in_algebra": False,
        "external_prime_tables_accessed": False,
        "riemann_zero_data_accessed": False,
        "network_access_by_executable": False,
        "timings_seconds": timings,
        "peak_memory_mib": _peak_memory_mib(),
        "source_hashes": {
            str(path.relative_to(project_root)): sha256_file(path) for path in source_files
        },
    }


def run(project_root: Path, *, controls_only: bool = False) -> dict[str, Any]:
    project_root = project_root.resolve()
    results = project_root / "results"
    lock_path = project_root / "experiments" / "source_lock.json"
    proof_path = project_root / "notes" / "PROOF_PACKAGE.md"
    timings: dict[str, float] = {}
    registry: list[dict[str, Any]] = []

    lock = _timed("R000", lambda: validate_source_lock(lock_path), timings)
    _write_json(results / "source_lock_validation.json", lock)
    registry.append({"run_id": "R000", "status": "PASS" if lock["pass"] else "FAIL"})
    if not lock["pass"]:
        raise RuntimeError("R000 source-lock validation failed")

    isolation = _timed(
        "R001", lambda: static_target_isolation_scan(project_root / "code"), timings
    )
    _write_json(results / "target_isolation_audit.json", isolation)
    registry.append({"run_id": "R001", "status": "PASS" if isolation["pass"] else "FAIL"})
    if not isolation["pass"]:
        raise RuntimeError("R001 target-isolation scan failed")

    proof = _timed("R010", lambda: proof_dependency_audit(proof_path), timings)
    _write_json(results / "proof_audit.json", proof)
    registry.append({"run_id": "R010", "status": "PASS" if proof["pass"] else "FAIL"})
    if not proof["pass"]:
        raise RuntimeError("R010 proof-dependency audit failed")

    controls = _timed("R011-R013", run_controls, timings)
    _write_json(results / "control_audit.json", controls)
    for run_id, key in (
        ("R011", "planted_bad_prime_positive"),
        ("R012", "integral_negative"),
        ("R013", "non_area_preserving_scope"),
    ):
        registry.append(
            {"run_id": run_id, "status": "PASS" if controls[key]["pass"] else "FAIL"}
        )
    if not controls["pass"]:
        raise RuntimeError("control gate failed; candidate remains locked")

    parameter = _timed("R020", parameter_preflight, timings)
    _write_json(results / "parameter_preflight.json", parameter)
    registry.append({"run_id": "R020", "status": "PASS" if parameter["pass"] else "FAIL"})
    if not parameter["pass"]:
        raise RuntimeError("R020 parameter preflight failed")

    symplectic = _timed("R021", symplectic_identity_audit, timings)
    _write_json(results / "symplectic_identity_audit.json", symplectic)
    registry.append({"run_id": "R021", "status": "PASS" if symplectic["pass"] else "FAIL"})
    if not symplectic["pass"]:
        raise RuntimeError("R021 symplectic preflight failed")

    gate = {
        "source_lock": lock["pass"],
        "target_isolation": isolation["pass"],
        "proof_dependencies": proof["pass"],
        "controls": controls["pass"],
        "parameter": parameter["pass"],
        "symplectic_identity": symplectic["pass"],
    }

    if controls_only:
        summary = {
            "candidate_id": lock["candidate_id"],
            "mode": "controls_only",
            "candidate_executed": False,
            "candidate_gate": gate,
            "run_registry": registry,
            "status": "CONTROLS_PASS_CANDIDATE_NOT_EXECUTED",
        }
        _write_json(results / "run_summary.json", summary)
        _write_json(results / "command_environment_manifest.json", _core_environment(project_root, timings))
        return summary

    if not all(gate.values()):
        raise RuntimeError("candidate gate did not pass")

    period_records: list[dict[str, Any]] = []
    for period, run_id in ((1, "R031"), (2, "R032"), (3, "R033")):
        record = _timed(run_id, lambda period=period: candidate_period_record(period), timings)
        determinant_checks = []
        if period == 1:
            determinant_checks = [record["determinant"] == "1"]
            cyclic_checks = [record["cyclic_trace_check"]]
        elif period == 2:
            determinant_checks = [record["determinant_remainder"] == "0"]
            cyclic_checks = [record["cyclic_trace_difference_remainder"] == "0"]
        else:
            determinant_checks = [value == "0" for value in record["determinant_remainders"]]
            cyclic_checks = [value == "0" for value in record["cyclic_trace_difference_remainders"]]
        recurrence_values: list[str]
        if period == 1:
            recurrence_values = []
        elif period == 2:
            recurrence_values = record["recurrence_remainders_on_exact_branch"]
        else:
            recurrence_values = [
                value
                for branch in record["recurrence_remainders_on_exact_branches"]
                for value in branch
            ]
        pass_record = (
            all(determinant_checks)
            and all(cyclic_checks)
            and all(value == "0" for value in recurrence_values)
            and record.get("trace_resultant_matches", True)
            and record.get("trace_resultant_squarefree_matches", True)
            and record.get("period_separation_pass", True)
            and not record["rational_multiplier_audit"]["exact_rational_roots"]
            and record["unit_certificate"]["monic"]
            and record["unit_certificate"]["constant_term"] == "1"
            and record["galois_norm_certificate"][
                "all_irreducible_factor_norms_are_rational_units"
            ]
        )
        record["pass"] = pass_record
        period_records.append(record)
        registry.append({"run_id": run_id, "status": "PASS" if pass_record else "FAIL"})
        if not pass_record:
            raise RuntimeError(f"{run_id} exact candidate audit failed")

    modulus = _timed("R031-R033-modulus", candidate_modulus_audit, timings)
    if modulus["exact_rational_modulus_set"] != ["1"]:
        raise RuntimeError("exact rational candidate modulus outside the theorem prediction")
    if modulus["unresolved_square_test_classifications"]:
        raise RuntimeError("candidate modulus audit left an unresolved rational square test")
    if modulus["raw_rational_prime_modulus_count"] != 0:
        raise RuntimeError("candidate audit found an exact raw rational-prime modulus")

    exact_polynomials = {
        "parameter_polynomial": polynomial_record(PARAMETER_POLYNOMIAL, PARAMETER_POLYNOMIAL.gens[0]),
        "periods": {
            str(period): {
                "trace_polynomial_over_cubic_field": polynomial_record(
                    trace_polynomial(period), T, coefficient_field="QQ[u]/P"
                ),
                "trace_polynomial_over_Q": polynomial_record(rational_trace_polynomial(period), T),
                "multiplier_polynomial_over_cubic_field": polynomial_record(
                    multiplier_polynomial(period), L, coefficient_field="QQ[u]/P"
                ),
                "multiplier_polynomial_over_Q": period_records[period - 1]["multiplier_polynomial_over_Q"],
            }
            for period in (1, 2, 3)
        },
    }
    _write_json(results / "exact_polynomials.json", exact_polynomials)
    _write_json(
        results / "exact_period_ledger.json",
        {
            "cutoff": 3,
            "period_definition": "exact period after explicit lower-period branch removal",
            "records": period_records,
            "finite_ledger_role": "implementation audit only",
        },
    )
    candidate = {
        "candidate_id": lock["candidate_id"],
        "parameter_embedding": modulus["embedding"],
        "period_cutoff": 3,
        "period_records": period_records,
        "exact_modulus_audit": modulus,
        "all_period_theorem_certificate": {
            "periodic_coordinates": "algebraic integers",
            "monodromy": "SL_2 over algebraic integers",
            "multipliers": "algebraic units",
            "complex_conjugates": "algebraic units in a conjugation-stable Galois closure",
            "rational_modulus_implication": "|lambda| in Q_{>0} implies |lambda|=1",
            "raw_rational_prime_modulus_count_all_periods": 0,
            "source": "notes/PROOF_PACKAGE.md",
            "finite_audit_not_used_as_proof": True,
        },
        "classification": {
            "raw_rational_prime_modulus": "ABSENT_BY_THEOREM",
            "exact_rational_modulus_set": ["1"],
            "rational_multiplier_upper_bound": ["-1", "1"],
            "irrational_or_approximate_moduli": "OUTSIDE_SUPPORT_CONCLUSION",
            "carrier_geometry": "PASS_GLOBAL_POLYNOMIAL_SYMPLECTIC_AUTOMORPHISM",
            "route_a_a0": "A0_FAIL_EXACT_RATIONAL_PRIME_MODULUS_ABSENT_BY_THEOREM",
            "route_a_a1": "STOP_SCOPED_AFTER_A0",
            "route_a_a2_a4": "STOP_SCOPED_AFTER_A0",
            "route_b": "NOT_OPENED",
            "route_decision": "ROUTE_A_REJECTED_FOR_EXACT_RATIONAL_PRIME_MODULUS_CLOCK",
        },
        "pass": all(record["pass"] for record in period_records),
    }
    _write_json(results / "candidate_multiplier_audit.json", candidate)

    scope = _timed("R040-R043", scope_audit, timings)
    _write_json(results / "scope_audit.json", scope)
    for run_id in scope["run_ids"]:
        registry.append({"run_id": run_id, "status": "PASS" if scope["pass"] else "FAIL"})
    if not scope["pass"]:
        raise RuntimeError("scope/reporting guards failed")

    negative_ledger = {
        "candidate_id": lock["candidate_id"],
        "closed_by_all_period_proof": [
            "exact rational modulus other than 1 for the frozen integral map",
            "exact rational-prime modulus for the frozen integral map",
        ],
        "finite_audit_observations": {
            "periods": [1, 2, 3],
            "rational_multiplier_roots": [],
            "exact_rational_modulus_values": ["1"],
            "interpretation": "implementation consistency only",
        },
        "sharp_control": "a=-15/16 realizes 2 and 1/2 with bad support {2}",
        "route_a_decision": {
            "carrier_geometry": "PASS_GLOBAL_POLYNOMIAL_SYMPLECTIC_AUTOMORPHISM",
            "a0": "A0_FAIL_EXACT_RATIONAL_PRIME_MODULUS_ABSENT_BY_THEOREM",
            "a1": "STOP_SCOPED_AFTER_A0",
            "a2_a4": "STOP_SCOPED_AFTER_A0",
            "route_b": "NOT_OPENED",
            "final": "ROUTE_A_REJECTED_FOR_EXACT_RATIONAL_PRIME_MODULUS_CLOCK",
            "reason": "The all-period algebraic-unit theorem rules out the frozen exact rational-prime-modulus clock; finite periods only audit the implementation.",
        },
        "open_or_outside_scope": scope["nonclaims"],
        "forbidden_data_used": False,
    }
    _write_json(results / "negative_result_ledger.json", negative_ledger)

    summary = {
        "candidate_id": lock["candidate_id"],
        "mode": "full_exact_audit",
        "candidate_executed": True,
        "candidate_gate": gate,
        "run_registry": registry,
        "must_run_completed": len(registry),
        "must_run_failed": sum(item["status"] != "PASS" for item in registry),
        "main_result": "all-period proof excludes every exact rational multiplier modulus except 1; the n<=3 exact audit and all frozen controls pass",
        "candidate_raw_rational_prime_modulus_count_all_periods": 0,
        "candidate_finite_rational_modulus_set": ["1"],
        "gpu_used": False,
        "status": "PASS",
    }
    _write_json(results / "run_summary.json", summary)
    _write_json(results / "command_environment_manifest.json", _core_environment(project_root, timings))
    return summary


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--project-root",
        type=Path,
        default=Path(__file__).resolve().parents[2],
        help="Paper project root",
    )
    parser.add_argument(
        "--controls-only",
        action="store_true",
        help="Run source/proof/control/preflight gates without executing the candidate",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    arguments = build_parser().parse_args(argv)
    summary = run(arguments.project_root, controls_only=arguments.controls_only)
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0
