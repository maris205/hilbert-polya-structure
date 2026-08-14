"""Fail-closed evaluation and observable-scope gates."""

from __future__ import annotations

from typing import Any, Iterable, Mapping


REQUIRED_STEP_KEYS = (
    "map_defined_at_input",
    "potential_defined_at_input",
    "current_gauge_defined_at_input",
    "next_gauge_defined_at_output",
    "transition_defined",
)


def evaluation_scope_audit(
    steps: Iterable[Mapping[str, bool]],
    *,
    theta_evaluated: bool = False,
    theta_defined_at_every_required_point: bool = True,
) -> dict[str, Any]:
    """Audit every evaluation point in order and stop at the first failure."""

    records: list[dict[str, Any]] = []
    first_stop: str | None = None
    for index, step in enumerate(steps):
        missing = [key for key in REQUIRED_STEP_KEYS if key not in step]
        if missing:
            raise ValueError(f"step {index} missing fields: {missing}")
        failures = [key for key in REQUIRED_STEP_KEYS if not bool(step[key])]
        if first_stop is None and failures:
            first_stop = f"STOP_STEP_{index}_{failures[0].upper()}"
        records.append(
            {
                "step": index,
                "checks": {key: bool(step[key]) for key in REQUIRED_STEP_KEYS},
                "failures": failures,
                "pass": not failures,
            }
        )

    if theta_evaluated and not theta_defined_at_every_required_point and first_stop is None:
        first_stop = "STOP_THETA_POLE_OR_UNDEFINED_VALUE"

    return {
        "step_records": records,
        "theta_evaluated": theta_evaluated,
        "theta_defined_at_every_required_point": theta_defined_at_every_required_point,
        "formal_composite_cancellation_accepted": False,
        "undefined_infinity_minus_infinity_cancellation_accepted": False,
        "classification": first_stop or "ALL_EVALUATION_POINTS_DEFINED_AND_POLE_FREE",
        "pass": first_stop is None,
    }


def observable_scope_classification(observable: str) -> dict[str, Any]:
    """Classify the exact observable without applying numeric functions."""

    admitted = {"ACTION", "REAL_PART_ACTION", "IMAGINARY_PART_ACTION", "ABS_ACTION"}
    nonclaims = {
        "LOG_ABS_ACTION",
        "ARG_ACTION",
        "MULTIPLIER_LOG",
        "LYAPUNOV_EXPONENT",
        "RETURN_TIME",
    }
    if observable in admitted:
        classification = "ALGEBRAIC_TRANSFORM_CERTIFICATE_APPLIES"
        passed = True
    elif observable in nonclaims:
        classification = "OUTSIDE_SOURCE_LOCK_NONCLAIM"
        passed = True
    else:
        classification = "UNKNOWN_OBSERVABLE_FAIL_CLOSED"
        passed = False
    return {
        "observable": observable,
        "numeric_postprocessing_executed": False,
        "classification": classification,
        "pass": passed,
    }
