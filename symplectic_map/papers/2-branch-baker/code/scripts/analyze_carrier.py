#!/usr/bin/env python3
"""Apply the frozen conjunctive Route-A decision rule to generated artifacts."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
import json
from pathlib import Path
from typing import Any

from _common import output_path, write_json_new
from branch_baker.protocol import (
    PROJECT_ROOT,
    REQUIRED_DEVELOPMENT_ARTIFACTS,
    REQUIRED_VALIDATION_ARTIFACTS,
    SOURCE_LOCK_PATH,
    append_access_log,
    require_split,
    sha256_file,
)


FROZEN_COUNTS = [
    0, 2, 0, 1, 0, 2, 0, 3, 0, 6,
    0, 9, 0, 18, 0, 30, 0, 56, 0, 99,
]


def require_field(payload: dict[str, Any], key: str, artifact: str) -> Any:
    if key not in payload:
        raise SystemExit(f"{artifact} is missing mandatory field {key!r}")
    return payload[key]


def require_false(payload: dict[str, Any], key: str, artifact: str) -> None:
    if require_field(payload, key, artifact) is not False:
        raise SystemExit(f"{artifact}.{key} must be explicitly false")


def decimal_field(value: Any, field: str) -> Decimal:
    try:
        converted = Decimal(str(value))
    except (InvalidOperation, ValueError) as exc:
        raise SystemExit(f"{field} is not a finite decimal") from exc
    if not converted.is_finite():
        raise SystemExit(f"{field} is not a finite decimal")
    return converted


def load(path: Path) -> tuple[Path, dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise SystemExit(f"Expected a JSON object: {path}")
    return path, value


def display_path(path: Path) -> str:
    try:
        return path.relative_to(PROJECT_ROOT).as_posix()
    except ValueError:
        return str(path)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--split", choices=("development", "validation", "test"), required=True)
    parser.add_argument(
        "--diagnostic-input-dir",
        help=(
            "Development-only diagnostic directory containing the four canonical "
            "input basenames; diagnostic output cannot enter any split whitelist"
        ),
    )
    parser.add_argument("--output")
    args = parser.parse_args()

    diagnostic_mode = args.diagnostic_input_dir is not None
    canonical_output = PROJECT_ROOT / "results" / f"analysis_{args.split}.json"
    if diagnostic_mode:
        if args.split != "development":
            raise SystemExit("Diagnostic input mode is development-only")
        if args.output is None:
            raise SystemExit("Diagnostic input mode requires an explicit --output")
        input_root = Path(args.diagnostic_input_dir).resolve()
        final_output = output_path(args.output).resolve()
        prohibited = {
            (PROJECT_ROOT / relative).resolve()
            for relative in (
                *REQUIRED_DEVELOPMENT_ARTIFACTS,
                *REQUIRED_VALIDATION_ARTIFACTS,
                "results/analysis_test.json",
            )
        }
        if final_output in prohibited:
            raise SystemExit("Diagnostic output cannot enter a frozen split whitelist")
    else:
        input_root = (PROJECT_ROOT / "results").resolve()
        final_output = canonical_output.resolve()
        if args.output is not None and output_path(args.output).resolve() != final_output:
            raise SystemExit("Formal analysis output path is fixed by split")

    require_split(args.split)
    access_time = datetime.now(timezone.utc).isoformat()
    if args.split in {"validation", "test"}:
        append_access_log(
            access_time,
            args.split,
            "analyze frozen split",
            "hash-bound unlock verified",
            "ACCESS BEGIN",
        )

    named_inputs = {
        "preflight": load(input_root / "exact_preflight.json"),
        "ledger": load(input_root / "ledger.json"),
        "parent_audit": load(input_root / "parent_audit.json"),
        "float_stress": load(input_root / f"float_stress_{args.split}.json"),
    }
    lock_hash = sha256_file(SOURCE_LOCK_PATH)
    lock = json.loads(SOURCE_LOCK_PATH.read_text(encoding="utf-8"))
    for name, (_, payload) in named_inputs.items():
        candidate_id = require_field(payload, "candidate_id", name)
        if candidate_id != "pcf_markov_baker_v1":
            raise SystemExit(f"{name} has wrong candidate_id: {candidate_id!r}")
        recorded = require_field(payload, "source_lock_sha256", name)
        if recorded != lock_hash:
            raise SystemExit(f"{name} was produced under a different source lock")
        require_false(payload, "external_prime_or_zero_data_accessed", name)

    preflight = named_inputs["preflight"][1]
    expected_preflight_gates = {
        "algebra",
        "candidate_cycle_ledger",
        "single_boundary_quotient",
        "zeta_conventions",
        "controls",
        "static_isolation",
    }
    if set(require_field(preflight, "gates", "preflight")) != expected_preflight_gates:
        raise SystemExit("preflight gate schema differs from the frozen schema")
    if any(value is not True for value in preflight["gates"].values()):
        raise SystemExit("preflight contains a failed or non-boolean gate")

    ledger = named_inputs["ledger"][1]
    if require_field(ledger, "max_period", "ledger") != 20:
        raise SystemExit("ledger max_period differs from the frozen period 20")
    if require_field(ledger, "primitive_counts", "ledger") != FROZEN_COUNTS:
        raise SystemExit("ledger primitive counts differ from the frozen vector")
    if require_field(ledger, "independent_direct_counts", "ledger") != FROZEN_COUNTS:
        raise SystemExit("independent ledger counts differ from the frozen vector")
    if require_field(ledger, "primitive_total", "ledger") != 226:
        raise SystemExit("ledger primitive total differs from 226")
    if require_field(ledger, "ledger_agreement", "ledger") is not True:
        raise SystemExit("the two exact ledger implementations do not agree")
    quotient = require_field(ledger, "parent_boundary_quotient", "ledger")
    if quotient.get("primitive_count_delta") != [1, -1] + [0] * 18:
        raise SystemExit("parent boundary quotient differs from the single frozen collapse")

    parent = named_inputs["parent_audit"][1]
    if require_field(parent, "digits", "parent_audit") != 100:
        raise SystemExit("parent audit did not use 100 digits")
    if require_field(parent, "max_period", "parent_audit") != 20:
        raise SystemExit("parent audit did not reach period 20")
    parent_thresholds = require_field(parent, "thresholds", "parent_audit")
    configured_target = decimal_field(
        require_field(
            parent_thresholds,
            "configured_residual_target",
            "parent_audit.thresholds",
        ),
        "parent_audit.thresholds.configured_residual_target",
    )
    effective_target = decimal_field(
        require_field(
            parent_thresholds,
            "effective_residual_target",
            "parent_audit.thresholds",
        ),
        "parent_audit.thresholds.effective_residual_target",
    )
    if configured_target != Decimal("1e-75") or effective_target != Decimal("1e-75"):
        raise SystemExit("parent audit configured/effective targets must both equal 1e-75")
    if require_field(parent, "frozen_scale_executed", "parent_audit") is not True:
        raise SystemExit("parent audit did not execute the frozen scale")
    if require_field(parent, "frozen_protocol_passed", "parent_audit") is not True:
        raise SystemExit("parent audit did not pass the frozen protocol")
    postcritical = require_field(parent, "postcritical", "parent_audit")
    periodic = require_field(parent, "periodic_factor", "parent_audit")
    if decimal_field(postcritical.get("max_abs_residual"), "postcritical.max_abs_residual") > effective_target:
        raise SystemExit("postcritical residual exceeds the frozen target")
    if decimal_field(periodic.get("max_periodic_residual"), "periodic_factor.max_periodic_residual") > effective_target:
        raise SystemExit("periodic residual exceeds the frozen target")

    float_payload = named_inputs["float_stress"][1]
    if float_payload.get("split") != args.split:
        raise SystemExit("Float stress split does not match analysis split")
    seed = lock["split_seed_derivation"][args.split]
    if require_field(float_payload, "seed", "float_stress") != seed:
        raise SystemExit("float stress seed differs from the source lock")
    if require_field(float_payload, "points", "float_stress") != 65536:
        raise SystemExit("float stress points differ from the source lock")
    if require_field(float_payload, "steps", "float_stress") != 256:
        raise SystemExit("float stress steps differ from the source lock")
    if require_field(float_payload, "frozen_scale_executed", "float_stress") is not True:
        raise SystemExit("float stress did not execute the frozen scale")
    expected_checks = 65536 * 256
    if require_field(float_payload, "expected_checks", "float_stress") != expected_checks:
        raise SystemExit("float stress expected-check count differs from frozen scale")
    if require_field(float_payload, "completed_checks", "float_stress") != expected_checks:
        raise SystemExit("float stress did not complete every frozen check")
    if require_field(float_payload, "edge_mismatches", "float_stress") != 0:
        raise SystemExit("float stress reported an edge mismatch")
    if require_field(float_payload, "boundary_failures", "float_stress") != 0:
        raise SystemExit("float stress reported a boundary failure")
    threshold = decimal_field(
        require_field(
            require_field(float_payload, "thresholds", "float_stress"),
            "max_roundtrip_error",
            "float_stress.thresholds",
        ),
        "float_stress.thresholds.max_roundtrip_error",
    )
    if threshold != Decimal("2e-13"):
        raise SystemExit("float roundtrip threshold differs from the source lock")
    observed = decimal_field(
        require_field(float_payload, "max_roundtrip_error", "float_stress"),
        "float_stress.max_roundtrip_error",
    )
    if observed > threshold:
        raise SystemExit("float roundtrip error exceeds the frozen threshold")

    gates = {
        "exact_carrier": require_field(preflight, "passed", "preflight") is True,
        "exact_ledger": require_field(ledger, "passed", "ledger") is True,
        "independent_parent_audit": require_field(parent, "passed", "parent_audit") is True,
        "floating_implementation": require_field(float_payload, "passed", "float_stress") is True,
        "finite_clock_rank_one": True,
        "termwise_exact_all_prime_clock_excluded": True,
        "external_prime_or_zero_data_absent": True,
    }
    structural_pass = all(
        gates[name]
        for name in (
            "exact_carrier",
            "exact_ledger",
            "independent_parent_audit",
            "floating_implementation",
            "external_prime_or_zero_data_absent",
        )
    )
    if structural_pass:
        pre_a0 = "PRE_A0_STRUCTURAL_PASS"
        route_a = "A0_FAIL / STRUCTURAL_ONLY"
        reason = (
            "The compact piecewise-symplectic carrier is verified, but every "
            "constant-slope primitive multiplier is a power of two and the "
            "fixed finite-memory scalar clock has finite rational rank."
        )
    else:
        pre_a0 = "PRE_A0_STRUCTURAL_FAIL"
        route_a = "IMPLEMENTATION_OR_CARRIER_STOP"
        reason = "At least one frozen carrier/audit gate failed."

    payload = {
        "candidate_id": "pcf_markov_baker_v1",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "split": args.split,
        "analysis_mode": "diagnostic" if diagnostic_mode else "formal_canonical_paths",
        "source_lock_sha256": lock_hash,
        "input_artifacts": {
            name: {
                "path": display_path(path),
                "sha256": sha256_file(path),
            }
            for name, (path, _) in named_inputs.items()
        },
        "gates": gates,
        "pre_a0_status": pre_a0,
        "route_a_status": route_a,
        "a1_status": (
            "PASS_PIECEWISE_EXACT_SYMPLECTIC_INTERIORS"
            if structural_pass
            else "FAIL_OR_UNVERIFIED"
        ),
        "a2_status": "STOP_SCOPED",
        "a3_status": "STOP_SCOPED",
        "a4_status": "STOP_SCOPED",
        "route_b_status": "FORBIDDEN",
        "reason": reason,
        "claim_scope": (
            "fixed finite-state finite-memory locally constant scalar "
            "multiplicative clock; termwise exact prime-length realization only"
        ),
        "excluded_inferences": [
            "no no-go for variable roofs or point-dependent derivatives",
            "no no-go for matrix spectral radii",
            "no quantitative statement about approximate prime matching",
            "no theorem that arbitrary analytic continuations differ",
            "no prime or Riemann-zero comparison",
            "no quantization claim",
        ],
        "external_prime_or_zero_data_accessed": False,
        "passed": structural_pass,
    }
    write_json_new(final_output, payload)


if __name__ == "__main__":
    main()
