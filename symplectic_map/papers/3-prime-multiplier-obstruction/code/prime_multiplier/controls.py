"""Frozen controls for the exact multiplier pipeline."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import sympy as sp

from .resultant import certificate_record, multiplier_certificate


@dataclass(frozen=True)
class ControlSpec:
    identifier: str
    parameter: sp.Rational
    algebraic_integer_coefficients: bool
    fixed_multiplier_prediction: tuple[sp.Rational, ...]
    role: str


CONTROL_SPECS: tuple[ControlSpec, ...] = (
    ControlSpec(
        identifier="c_zero",
        parameter=sp.Rational(0),
        algebraic_integer_coefficients=True,
        fixed_multiplier_prediction=(sp.Rational(0), sp.Rational(2)),
        role="power-map positive control for the p=2 exponent clock",
    ),
    ControlSpec(
        identifier="c_minus_2",
        parameter=sp.Rational(-2),
        algebraic_integer_coefficients=True,
        fixed_multiplier_prediction=(sp.Rational(-2), sp.Rational(4)),
        role="Chebyshev boundary and fixed raw-prime residue control",
    ),
    ControlSpec(
        identifier="c_minus_3_over_4",
        parameter=sp.Rational(-3, 4),
        algebraic_integer_coefficients=False,
        fixed_multiplier_prediction=(sp.Rational(-1), sp.Rational(3)),
        role="assumption-violation control with an odd raw-prime multiplier",
    ),
)


def quadratic_map(parameter: sp.Rational, variable: sp.Symbol | None = None) -> sp.Poly:
    """Return ``z^2+c`` over ``QQ`` for an exact rational ``c``."""

    z = variable if variable is not None else sp.Symbol("z")
    return sp.Poly(z**2 + sp.Rational(parameter), z, domain=sp.QQ)


def _control_passes(spec: ControlSpec, period_records: list[dict[str, Any]]) -> tuple[bool, list[str]]:
    findings: list[str] = []
    fixed = tuple(sp.Rational(item) for item in period_records[0]["rational_candidates"])
    expected_fixed = tuple(sorted(spec.fixed_multiplier_prediction))
    if tuple(sorted(fixed)) != expected_fixed:
        findings.append(
            f"fixed multipliers {tuple(map(str, fixed))} differ from {tuple(map(str, expected_fixed))}"
        )

    for record in period_records:
        if record["chain_rule_identity"] != "PASS":
            findings.append(f"period {record['period']} chain-rule mismatch")
        if record["perfect_cycle_power"] != "PASS":
            findings.append(f"period {record['period']} cycle-power mismatch")
        if record["quotient_annihilation"] != "PASS":
            findings.append(f"period {record['period']} quotient mismatch")

    if spec.identifier == "c_zero":
        for record in period_records:
            period = int(record["period"])
            nonzero = [sp.Rational(item) for item in record["rational_candidates"] if sp.Rational(item) != 0]
            if any(item != 2**period for item in nonzero):
                findings.append(f"period {period} nonzero power-map multiplier is not 2^{period}")
            if period >= 2 and not nonzero:
                findings.append(f"period {period} power-map cycle unexpectedly absent")

    if spec.identifier == "c_minus_3_over_4":
        fixed_records = period_records[0]["rational_candidate_records"]
        if not any(
            item["multiplier"] == "3" and item["raw_rational_prime"] for item in fixed_records
        ):
            findings.append("odd raw-prime positive control was not detected")
        if not period_records[1]["formal_period_contamination"]:
            findings.append("expected multiplier -1 formal-period-2 contamination was not recorded")
        if period_records[1]["exact_period_degree"] != 0:
            findings.append("period-2 lower-period collision was not fully saturated")

    return not findings, findings


def audit_control(spec: ControlSpec, *, max_period: int = 4) -> dict[str, Any]:
    """Run one frozen control through the same exact pipeline as the candidate."""

    if max_period != 4:
        raise ValueError("the source lock freezes the required control audit at periods 1..4")
    base = quadratic_map(spec.parameter)
    records = [
        certificate_record(multiplier_certificate(base, period), derivative_content=2)
        for period in range(1, max_period + 1)
    ]
    passed, findings = _control_passes(spec, records)
    return {
        "control_id": spec.identifier,
        "map": f"z^2+({spec.parameter})",
        "parameter": str(spec.parameter),
        "role": spec.role,
        "algebraic_integer_coefficients": spec.algebraic_integer_coefficients,
        "assumption_flag_expected": (
            "THEOREM_ASSUMPTIONS_SATISFIED"
            if spec.algebraic_integer_coefficients
            else "ALGEBRAIC_INTEGER_COEFFICIENT_ASSUMPTION_VIOLATED"
        ),
        "periods": records,
        "status": "PASS" if passed else "FAIL",
        "findings": findings,
    }


def audit_controls(*, max_period: int = 4) -> dict[str, Any]:
    """Run all three frozen controls in their declared order."""

    records = [audit_control(spec, max_period=max_period) for spec in CONTROL_SPECS]
    passed = all(record["status"] == "PASS" for record in records)
    return {
        "run_ids": ["R011", "R012", "R013"],
        "max_period": max_period,
        "candidate_accessed": False,
        "external_data_accessed": False,
        "controls": records,
        "status": "PASS" if passed else "FAIL",
    }

