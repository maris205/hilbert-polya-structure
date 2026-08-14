"""Source-lock-aware command-line orchestration for the exact audit."""

from __future__ import annotations

import argparse
import json
import resource
import sys
import time
from pathlib import Path
from typing import Any, Callable

from .algebra import candidate_field
from .candidate import audit_candidate, audit_conjugacy, parameter_and_conjugacy_preflight
from .controls import audit_controls
from .protocol import (
    audit_proof_dependencies,
    environment_record,
    sha256_file,
    validate_source_lock,
    write_json,
)
from .symplectic import audit_symplectic_bridge


def _timed(callable_: Callable[[], Any]) -> tuple[Any, float, int]:
    before_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    started = time.perf_counter()
    result = callable_()
    elapsed = time.perf_counter() - started
    after_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return result, elapsed, max(before_memory, after_memory)


def _write_timed_record(path: Path, record: dict[str, Any], elapsed: float, peak_kib: int) -> None:
    record["engineering_diagnostics"] = {
        "wall_seconds": elapsed,
        "process_peak_rss_kib": peak_kib,
    }
    write_json(path, record)


def _require_pass(record: dict[str, Any], label: str, code: int) -> None:
    if record.get("status") != "PASS":
        raise SystemExit(f"{label} failed; candidate execution stopped (exit {code})")


def _polynomial_index(
    controls: dict[str, Any],
    candidate: dict[str, Any],
    conjugacy: dict[str, Any],
) -> dict[str, Any]:
    return {
        "schema": "exact-polynomial-index-v1",
        "coefficient_conventions": {
            "candidate": "coefficients in basis 1,u,u^2 with u^3-2u^2+2u-2=0",
            "controls": "coefficients over Q",
            "orbit_polynomials": "monic in z or x",
            "multiplier_polynomials": "monic in L",
        },
        "controls": {
            control["control_id"]: {
                str(period["period"]): {
                    "formal_dynatomic_polynomial": period["formal_dynatomic_polynomial"],
                    "exact_period_polynomial": period["exact_period_polynomial"],
                    "point_resultant": period["point_resultant"],
                    "cycle_multiplier_polynomial": period["cycle_multiplier_polynomial"],
                }
                for period in control["periods"]
            }
            for control in controls["controls"]
        },
        "candidate_g": {
            str(period["period"]): {
                "formal_dynatomic_polynomial": period["formal_dynatomic_polynomial"],
                "exact_period_polynomial": period["exact_period_polynomial"],
                "point_resultant": period["point_resultant"],
                "cycle_multiplier_polynomial": period["cycle_multiplier_polynomial"],
            }
            for period in candidate["periods"]
        },
        "conjugate_f_u": {
            str(period["period"]): {
                "formal_dynatomic_polynomial": period["f_u_certificate"]["formal_dynatomic_polynomial"],
                "exact_period_polynomial": period["f_u_certificate"]["exact_period_polynomial"],
                "point_resultant": period["f_u_certificate"]["point_resultant"],
                "cycle_multiplier_polynomial": period["f_u_certificate"]["cycle_multiplier_polynomial"],
            }
            for period in conjugacy["periods"]
        },
        "external_data_accessed": False,
    }


def build_parser() -> argparse.ArgumentParser:
    project_root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(
        description="Run the source-locked exact PCF prime-multiplier audit",
    )
    parser.add_argument(
        "--source-lock",
        type=Path,
        default=project_root / "experiments" / "source_lock.json",
    )
    parser.add_argument(
        "--proof-package",
        type=Path,
        default=project_root / "notes" / "PROOF_PACKAGE.md",
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=project_root / "results",
    )
    parser.add_argument(
        "--max-period",
        type=int,
        choices=(4,),
        default=4,
        help="frozen exact cutoff; values other than 4 are rejected",
    )
    return parser


def run(args: argparse.Namespace) -> dict[str, Any]:
    project_root = Path(__file__).resolve().parents[2]
    code_root = project_root / "code"
    output_root = args.output_root.resolve()
    output_root.mkdir(parents=True, exist_ok=True)

    source_validation, elapsed, memory = _timed(
        lambda: validate_source_lock(args.source_lock.resolve(), code_root)
    )
    _write_timed_record(output_root / "source_lock_validation.json", source_validation, elapsed, memory)
    _require_pass(source_validation, "source-lock/static integrity gate", 2)

    proof_audit, elapsed, memory = _timed(
        lambda: audit_proof_dependencies(args.proof_package.resolve())
    )
    _write_timed_record(output_root / "proof_audit.json", proof_audit, elapsed, memory)
    _require_pass(proof_audit, "proof-dependency gate", 3)

    controls, elapsed, memory = _timed(lambda: audit_controls(max_period=args.max_period))
    _write_timed_record(output_root / "control_audit.json", controls, elapsed, memory)
    _require_pass(controls, "controls-first gate", 4)

    field = candidate_field()
    preflight, elapsed, memory = _timed(lambda: parameter_and_conjugacy_preflight(field))
    _write_timed_record(output_root / "parameter_preflight.json", preflight, elapsed, memory)
    _require_pass(preflight, "candidate algebra preflight", 5)

    candidate_pair, elapsed, memory = _timed(
        lambda: audit_candidate(field=field, max_period=args.max_period)
    )
    candidate, certificates = candidate_pair
    _write_timed_record(output_root / "candidate_multiplier_audit.json", candidate, elapsed, memory)
    _require_pass(candidate, "candidate exact multiplier audit", 6)

    conjugacy, elapsed, memory = _timed(
        lambda: audit_conjugacy(certificates, field=field, max_period=args.max_period)
    )
    _write_timed_record(output_root / "conjugacy_audit.json", conjugacy, elapsed, memory)
    _require_pass(conjugacy, "conjugacy-invariant control", 7)

    bridge, elapsed, memory = _timed(lambda: audit_symplectic_bridge(max_period=args.max_period))
    _write_timed_record(output_root / "symplectic_bridge_audit.json", bridge, elapsed, memory)
    _require_pass(bridge, "branchwise symplectic bridge", 8)

    write_json(output_root / "exact_polynomials.json", _polynomial_index(controls, candidate, conjugacy))

    negative_ledger = {
        "candidate_id": "pcf_quadratic_prime_multiplier_obstruction_v1",
        "raw_rational_prime_all_periods": {
            "status": "ABSENT_BY_THEOREM",
            "basis": "Theorem A plus the exact fixed-point exclusion of lambda=+/-2",
        },
        "odd_rational_exponent_prime_all_periods": {
            "status": "ABSENT_BY_THEOREM",
            "basis": "2-adic valuation after lambda in 2^n Z",
        },
        "p2_rational_exponent_prime_period_1": {
            "status": "ABSENT",
            "basis": "fixed-point calculation",
        },
        "p2_rational_exponent_prime_period_ge_2": {
            "status": "OPEN",
            "finite_cutoff_does_not_close": True,
        },
        "complex_modulus_only_target": "OUTSIDE_THEOREM",
        "conditional_real_orbit_ledger": "DISABLED_NOT_EXECUTED",
        "external_prime_or_zero_data_accessed": False,
    }
    write_json(output_root / "negative_result_ledger.json", negative_ledger)

    manifest = {
        "candidate_id": "pcf_quadratic_prime_multiplier_obstruction_v1",
        "execution_command": "python code/scripts/run_exact_audit.py --max-period 4",
        "environment": environment_record(),
        "source_lock_sha256": source_validation["source_lock_sha256"],
        "source_lock_path": str(args.source_lock.resolve().relative_to(project_root)),
        "proof_package_sha256": sha256_file(args.proof_package.resolve()),
        "periods_executed": [1, 2, 3, 4],
        "candidate_exact_engine": "SymPy exact AlgebraicField and polynomial subresultants",
        "candidate_numerical_runs": 0,
        "external_prime_or_zero_data_accessed": False,
        "conditional_real_orbit_ledger_executed": False,
        "scientific_boundary": {
            "raw_rational_prime": "ABSENT_BY_THEOREM",
            "odd_rational_exponent_prime": "ABSENT_BY_THEOREM",
            "p2_exponent_prime_period_ge_2": "OPEN",
        },
        "gate_status": {
            "source_lock": source_validation["status"],
            "proof": proof_audit["status"],
            "controls": controls["status"],
            "preflight": preflight["status"],
            "candidate": candidate["status"],
            "conjugacy": conjugacy["status"],
            "symplectic_bridge": bridge["status"],
        },
        "status": "PASS",
    }
    write_json(output_root / "command_environment_manifest.json", manifest)

    summary = {
        "candidate_id": manifest["candidate_id"],
        "required_runs_completed": [
            "R000",
            "R001",
            "R010",
            "R011",
            "R012",
            "R013",
            "R020",
            "R021",
            "R022",
            "R031",
            "R032",
            "R033",
            "R034",
            "R040",
            "R041",
            "R042",
        ],
        "required_runs_passed": True,
        "candidate_rational_multiplier_counts_n1_to_n4": [
            len(item["rational_candidates"]) for item in candidate["periods"]
        ],
        "candidate_raw_prime_count_n1_to_n4": sum(
            int(record["raw_rational_prime"])
            for item in candidate["periods"]
            for record in item["rational_candidate_records"]
        ),
        "theorem_result": "NO_RAW_RATIONAL_PRIME_MULTIPLIER_AT_ANY_PERIOD",
        "open_boundary": "p=2 exponent-prime for n>=2 remains OPEN",
        "status": "PASS",
    }
    write_json(output_root / "run_summary.json", summary)
    return summary


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    summary = run(args)
    json.dump(summary, sys.stdout, indent=2, sort_keys=True)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
