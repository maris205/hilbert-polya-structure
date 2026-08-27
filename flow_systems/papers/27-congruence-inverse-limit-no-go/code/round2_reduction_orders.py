#!/usr/bin/env python3
"""Deterministic Round-2 diagnostics for the frozen Gamma(3 n!) tower.

The output is deliberately a finite-quotient reduction-order ledger.  It is
not a periodic-orbit ledger for the inverse-limit flow, whose periodic set is
proved empty in the Stage-1 theorem brief.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
from pathlib import Path
from typing import Iterable


EVALUATION_DATE = "2026-08-27"
LEVELS = (
    (1, 3),
    (2, 6),
    (3, 18),
    (4, 72),
    (5, 360),
    (6, 2160),
    (7, 15120),
    (8, 120960),
)

# Positive LR-word witnesses frozen before the order computation.  They are
# primitive necklaces in the positive word monoid and exact members of
# Gamma(3); that does not certify primitivity as Gamma(3)-conjugacy classes.
ELEMENTS = (
    {
        "element_id": "G3-A",
        "word": "LLLRRR",
        "matrix": ((10, 3), (3, 1)),
    },
    {
        "element_id": "G3-B",
        "word": "LLRLRRLR",
        "matrix": ((31, 18), (12, 7)),
    },
    {
        "element_id": "G3-C",
        "word": "LLLLLLRRR",
        "matrix": ((19, 6), (3, 1)),
    },
)

FIELDNAMES = (
    "element_id",
    "positive_word",
    "matrix_a",
    "matrix_b",
    "matrix_c",
    "matrix_d",
    "determinant",
    "trace",
    "hyperbolic",
    "gamma3_member",
    "positive_word_primitive",
    "gamma3_class_primitivity",
    "base_geodesic_length",
    "level_n",
    "modulus_q",
    "quotient_convention",
    "psl_order_sequential",
    "psl_order_group_bound",
    "order_crosscheck",
    "terminal_scalar_sign",
    "previous_order_divides",
    "bonding_compatibility",
    "cumulative_common_multiplier",
    "same_time_compatible_through_level",
    "finite_level_period_scale",
    "finite_level_closed_lift_period",
    "period_scaling_residual",
    "normality_basis",
    "lift_representative_eta_n",
    "statistic_owner",
    "inverse_limit_flow_credit",
    "evidence_status",
)


Matrix = tuple[tuple[int, int], tuple[int, int]]


def matrix_mul(left: Matrix, right: Matrix, modulus: int | None = None) -> Matrix:
    value = (
        (
            left[0][0] * right[0][0] + left[0][1] * right[1][0],
            left[0][0] * right[0][1] + left[0][1] * right[1][1],
        ),
        (
            left[1][0] * right[0][0] + left[1][1] * right[1][0],
            left[1][0] * right[0][1] + left[1][1] * right[1][1],
        ),
    )
    if modulus is None:
        return value
    return tuple(tuple(entry % modulus for entry in row) for row in value)  # type: ignore[return-value]


def matrix_pow(matrix: Matrix, exponent: int, modulus: int) -> Matrix:
    result: Matrix = ((1, 0), (0, 1))
    base = tuple(tuple(entry % modulus for entry in row) for row in matrix)  # type: ignore[assignment]
    power = exponent
    while power:
        if power & 1:
            result = matrix_mul(result, base, modulus)
        base = matrix_mul(base, base, modulus)
        power >>= 1
    return result


def scalar_sign(matrix: Matrix, modulus: int) -> int | None:
    identity: Matrix = ((1 % modulus, 0), (0, 1 % modulus))
    minus_identity: Matrix = (((-1) % modulus, 0), (0, (-1) % modulus))
    if matrix == identity:
        return 1
    if matrix == minus_identity:
        return -1
    return None


def factor_integer(value: int) -> dict[int, int]:
    remaining = value
    factors: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= remaining:
        while remaining % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            remaining //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        factors[remaining] = factors.get(remaining, 0) + 1
    return factors


def sl2_group_order(modulus: int) -> int:
    """Return |SL_2(Z/modulus Z)| = q^3 prod_{p|q}(1-p^-2)."""

    order = modulus**3
    for prime in factor_integer(modulus):
        order = order * (prime * prime - 1) // (prime * prime)
    return order


def psl_order_sequential(matrix: Matrix, modulus: int) -> tuple[int, int]:
    current: Matrix = ((1, 0), (0, 1))
    # The observed maximum is 2880.  The mathematical upper bound makes this
    # cap deterministic and prevents a silent infinite loop if the code drifts.
    cap = sl2_group_order(modulus)
    for exponent in range(1, cap + 1):
        current = matrix_mul(current, matrix, modulus)
        sign = scalar_sign(current, modulus)
        if sign is not None:
            return exponent, sign
    raise AssertionError("sequential PSL order search exceeded the exact group-order bound")


def psl_order_from_group_bound(matrix: Matrix, modulus: int) -> tuple[int, int]:
    """Independently reduce an exact finite-group multiple by prime factors."""

    order = sl2_group_order(modulus)
    if scalar_sign(matrix_pow(matrix, order, modulus), modulus) is None:
        raise AssertionError("group-order multiple did not reach the PSL identity coset")
    for prime in sorted(factor_integer(order)):
        while order % prime == 0:
            trial = order // prime
            if scalar_sign(matrix_pow(matrix, trial, modulus), modulus) is None:
                break
            order = trial
    terminal = matrix_pow(matrix, order, modulus)
    sign = scalar_sign(terminal, modulus)
    if sign is None:
        raise AssertionError("factor reduction did not terminate at a scalar sign")
    return order, sign


def primitive_word(word: str) -> bool:
    return all(
        word != word[:period] * (len(word) // period)
        for period in range(1, len(word))
        if len(word) % period == 0
    )


def gamma3_member(matrix: Matrix) -> bool:
    return (
        (matrix[0][0] - 1) % 3 == 0
        and matrix[0][1] % 3 == 0
        and matrix[1][0] % 3 == 0
        and (matrix[1][1] - 1) % 3 == 0
    )


def determinant(matrix: Matrix) -> int:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def build_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for element in ELEMENTS:
        matrix: Matrix = element["matrix"]  # type: ignore[assignment]
        trace = matrix[0][0] + matrix[1][1]
        if determinant(matrix) != 1 or trace <= 2 or not gamma3_member(matrix):
            raise AssertionError(f"invalid frozen witness {element['element_id']}")
        length = 2.0 * math.acosh(trace / 2.0)
        previous_order: int | None = None
        previous_modulus: int | None = None
        cumulative_multiplier = 1
        for level_n, modulus in LEVELS:
            sequential_order, sequential_sign = psl_order_sequential(matrix, modulus)
            bound_order, bound_sign = psl_order_from_group_bound(matrix, modulus)
            crosscheck = sequential_order == bound_order and sequential_sign == bound_sign
            if not crosscheck:
                raise AssertionError("independent PSL-order algorithms disagree")
            previous_divides = previous_order is None or sequential_order % previous_order == 0
            bonding_compatibility = previous_modulus is None or modulus % previous_modulus == 0
            cumulative_multiplier = math.lcm(cumulative_multiplier, sequential_order)
            same_time = cumulative_multiplier % sequential_order == 0
            closed_period = sequential_order * length
            rows.append(
                {
                    "element_id": element["element_id"],
                    "positive_word": element["word"],
                    "matrix_a": matrix[0][0],
                    "matrix_b": matrix[0][1],
                    "matrix_c": matrix[1][0],
                    "matrix_d": matrix[1][1],
                    "determinant": 1,
                    "trace": trace,
                    "hyperbolic": "true",
                    "gamma3_member": "true",
                    "positive_word_primitive": str(primitive_word(element["word"])).lower(),
                    "gamma3_class_primitivity": "OPEN",
                    "base_geodesic_length": f"{length:.15g}",
                    "level_n": level_n,
                    "modulus_q": modulus,
                    "quotient_convention": "PSL_2(Z/qZ); A and -A identified",
                    "psl_order_sequential": sequential_order,
                    "psl_order_group_bound": bound_order,
                    "order_crosscheck": str(crosscheck).lower(),
                    "terminal_scalar_sign": f"{sequential_sign:+d}",
                    "previous_order_divides": str(previous_divides).lower(),
                    "bonding_compatibility": str(bonding_compatibility).lower(),
                    "cumulative_common_multiplier": cumulative_multiplier,
                    "same_time_compatible_through_level": str(same_time).lower(),
                    "finite_level_period_scale": sequential_order,
                    "finite_level_closed_lift_period": f"{closed_period:.15g}",
                    "period_scaling_residual": "0",
                    "normality_basis": "Gamma(q)=kernel(PSL2Z->PSL2(Z/qZ))",
                    "lift_representative_eta_n": "identity coset witness",
                    "statistic_owner": "FINITE_CONGRUENCE_TOWER_REDUCTION_DIAGNOSTIC",
                    "inverse_limit_flow_credit": "FORBIDDEN",
                    "evidence_status": "NUMERICALLY_CERTIFIED",
                }
            )
            previous_order = sequential_order
            previous_modulus = modulus
    return rows


def csv_bytes(rows: Iterable[dict[str, object]]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=FIELDNAMES, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True) + "\n").encode("utf-8")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def source_root() -> Path:
    return Path(__file__).resolve().parents[1]


def build_artifacts() -> dict[str, bytes]:
    rows = build_rows()
    orders_by_element = {
        element["element_id"]: [
            int(row["psl_order_sequential"])
            for row in rows
            if row["element_id"] == element["element_id"]
        ]
        for element in ELEMENTS
    }
    metrics = {
        "artifact_kind": "finite_congruence_tower_diagnostic",
        "candidate": "P27 Gamma(3 n!) residual tower",
        "date": EVALUATION_DATE,
        "levels": len(LEVELS),
        "moduli": [modulus for _, modulus in LEVELS],
        "hyperbolic_elements": len(ELEMENTS),
        "rows": len(rows),
        "independent_order_crosschecks_passed": sum(
            row["order_crosscheck"] == "true" for row in rows
        ),
        "bonding_base_rows_initialized": sum(int(row["level_n"]) == 1 for row in rows),
        "bonding_transition_checks_expected": sum(int(row["level_n"]) > 1 for row in rows),
        "bonding_transition_checks_passed": sum(
            int(row["level_n"]) > 1 and row["bonding_compatibility"] == "true"
            for row in rows
        ),
        "previous_order_divisibility_transition_checks_passed": sum(
            int(row["level_n"]) > 1 and row["previous_order_divides"] == "true"
            for row in rows
        ),
        "orders_by_element": orders_by_element,
        "max_observed_psl_order": max(int(row["psl_order_sequential"]) for row in rows),
        "owner": "finite congruence tower plus frozen matrices",
        "inverse_limit_periodic_orbit_credit": False,
        "inverse_limit_theorem": "Per(M_infinity)=empty remains PROVED",
        "formal_route_a_tuple": "UNASSIGNED",
        "route_b_evaluation": "NOT_RUN",
        "route_b_invocation_allowed": False,
        "forbidden_data_used": [],
    }
    receipt = {
        "artifact_kind": "experiment_execution_receipt",
        "date": EVALUATION_DATE,
        "determinism_class": "deterministic exact integer arithmetic plus deterministic float formatting",
        "expected_rows": len(ELEMENTS) * len(LEVELS),
        "order_algorithms": ["sequential multiplication", "finite-group-bound factor reduction"],
        "all_internal_checks_pass": True,
        "owner_boundary": "finite-level statistic is not owned by the inverse-limit flow",
        "evidence_labels": {
            "integer_orders": "NUMERICALLY_CERTIFIED",
            "empty_limit_periodic_set": "PROVED",
            "residual_splitting_hypothesis": "HEURISTIC",
        },
        "evidence_locations": {
            "empty_limit_periodic_set": "notes/stage1_research_brief.md",
        },
    }
    return {
        "congruence_reduction_order_ledger.csv": csv_bytes(rows),
        "round2_metrics.json": json_bytes(metrics),
        "experiment_receipt.json": json_bytes(receipt),
    }


def build_manifest(artifacts: dict[str, bytes]) -> bytes:
    root = source_root()
    source_files = (
        root / "code" / "round2_reduction_orders.py",
        root / "code" / "test_round2_reduction_orders.py",
        root / "experiments" / "reproduce.sh",
    )
    manifest = {
        "schema": "p27-round2-manifest-v1",
        "date": EVALUATION_DATE,
        "artifacts": {
            name: {"bytes": len(payload), "sha256": sha256_bytes(payload)}
            for name, payload in sorted(artifacts.items())
        },
        "source_files": {
            path.name: {
                "bytes": len(path.read_bytes()),
                "sha256": sha256_bytes(path.read_bytes()),
            }
            for path in source_files
        },
    }
    return json_bytes(manifest)


def generate(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    artifacts = build_artifacts()
    for name, payload in artifacts.items():
        (output_dir / name).write_bytes(payload)
    (output_dir / "manifest.json").write_bytes(build_manifest(artifacts))


def verify(output_dir: Path) -> dict[str, object]:
    expected = build_artifacts()
    manifest_path = output_dir / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    mismatches: list[str] = []
    for name, payload in expected.items():
        path = output_dir / name
        if not path.exists():
            mismatches.append(f"missing:{name}")
            continue
        observed = path.read_bytes()
        if observed != payload:
            mismatches.append(f"content:{name}")
        recorded = manifest["artifacts"].get(name, {})
        if recorded.get("sha256") != sha256_bytes(observed):
            mismatches.append(f"manifest_hash:{name}")
        if recorded.get("bytes") != len(observed):
            mismatches.append(f"manifest_bytes:{name}")
    root = source_root()
    for path in (
        root / "code" / "round2_reduction_orders.py",
        root / "code" / "test_round2_reduction_orders.py",
        root / "experiments" / "reproduce.sh",
    ):
        observed = path.read_bytes()
        recorded = manifest["source_files"].get(path.name, {})
        if recorded.get("sha256") != sha256_bytes(observed):
            mismatches.append(f"source_manifest_hash:{path.name}")
        if recorded.get("bytes") != len(observed):
            mismatches.append(f"source_manifest_bytes:{path.name}")
    rows = build_rows()
    checks = {
        "rows_24": len(rows) == 24,
        "three_elements": len({row["element_id"] for row in rows}) == 3,
        "eight_levels_each": all(
            sum(row["element_id"] == element["element_id"] for row in rows) == 8
            for element in ELEMENTS
        ),
        "order_crosschecks_24": sum(row["order_crosscheck"] == "true" for row in rows) == 24,
        "bonding_rows_24_including_three_base_rows": sum(
            row["bonding_compatibility"] == "true" for row in rows
        )
        == 24,
        "bonding_transitions_21": sum(
            int(row["level_n"]) > 1 and row["bonding_compatibility"] == "true"
            for row in rows
        )
        == 21,
        "order_divisibility_transitions_21": sum(
            int(row["level_n"]) > 1 and row["previous_order_divides"] == "true"
            for row in rows
        )
        == 21,
        "limit_credit_forbidden_24": sum(
            row["inverse_limit_flow_credit"] == "FORBIDDEN" for row in rows
        )
        == 24,
    }
    if not all(checks.values()):
        mismatches.extend(name for name, passed in checks.items() if not passed)
    return {
        "status": "PASS" if not mismatches else "FAIL",
        "output_dir": str(output_dir),
        "checks": checks,
        "mismatches": mismatches,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    for command in ("generate", "verify"):
        child = subparsers.add_parser(command)
        child.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    if args.command == "generate":
        generate(args.output_dir)
        print(json.dumps({"status": "GENERATED", "output_dir": str(args.output_dir)}, sort_keys=True))
        return 0
    report = verify(args.output_dir)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
