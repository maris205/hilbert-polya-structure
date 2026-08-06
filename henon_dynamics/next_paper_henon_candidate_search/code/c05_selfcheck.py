#!/usr/bin/env python3
"""Independent small-case checks for the HCS-C05 pilot."""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("c05_maslov_pilot", HERE / "c05_maslov_pilot.py")
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load c05_maslov_pilot")
PILOT = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = PILOT
SPEC.loader.exec_module(PILOT)


def relative_error(left: float, right: float) -> float:
    return abs(left - right) / max(1.0, abs(left), abs(right))


def hill_check(coordinates: np.ndarray) -> float:
    hessian = PILOT.cyclic_hessian(coordinates)
    matrix = PILOT.monodromy(coordinates)
    left = float(np.linalg.det(hessian))
    right = ((-1) ** (len(coordinates) - 1)) * (2.0 - float(np.trace(matrix)))
    return relative_error(left, right)


def main() -> None:
    checks = {
        "n1_hill_error": hill_check(np.asarray([-0.6076252185107651])),
        "n2_special_hill_error": hill_check(np.asarray([0.2, -0.3])),
        "n3_hill_error": hill_check(np.asarray([-0.37, 0.54, -0.37])),
    }
    q = np.asarray([-0.37, 0.54, -0.37])
    checks["reversal_action_error"] = abs(
        PILOT.periodic_action(q) - PILOT.periodic_action(q[::-1])
    )
    checks["repeat_action_error"] = abs(
        PILOT.periodic_action(np.tile(q, 4)) - 4.0 * PILOT.periodic_action(q)
    )
    checks["n2_offdiagonal_is_two"] = bool(
        PILOT.cyclic_hessian(np.asarray([0.2, -0.3]))[0, 1] == 2.0
    )
    results = HERE.parent / "results" / "c05_maslov"
    required = (
        "phase_ledger.csv",
        "determinant_coefficients.csv",
        "cutoff_evaluations.csv",
        "controls.json",
        "summary.json",
        "RESULTS.md",
    )
    checks["full_results_present"] = all((results / name).is_file() for name in required)
    if checks["full_results_present"]:
        summary = json.loads((results / "summary.json").read_text(encoding="utf-8"))
        audit = summary["phase_audit"]
        aggregates = summary["controls"]["variant_aggregates"]
        checks["full_results_pass"] = bool(
            audit["primitive_cycle_count"] == 2170
            and audit["reversal_failure_count"] == 0
            and audit["repetition_maslov_additivity_failure_count"] == 0
            and audit["symbol_count_maslov_failure_count"] == 0
            and audit["maslov_orientation_parity_failure_count"] == 0
            and audit["hill_sign_mismatch_count"] == 0
            and audit["coordinate_bound_failure_count"] == 0
            and audit["minimum_strict_diagonal_dominance_margin"] > 0.0
            and audit["near_zero_hessian_count"] == 0
            and audit["maximum_hill_logabs_error"] < 1.0e-11
            and summary["gauge_audit"]["coefficient_rotation_numeric_audit"][
                "maximum_coefficient_rotation_error"
            ]
            < 1.0e-12
            and all(
                row["maximum_coefficient_prefix_drift"] < 1.0e-14
                for row in aggregates.values()
            )
            and summary["repetition_additivity_lemma"]["status"] == "PROVED"
            and summary["period4_zero_action_audit"]["pass"]
            and summary["decision"]["hard_kill"]
            and not summary["decision"]["promotion"]
        )
    else:
        checks["full_results_pass"] = False
    checks["all_pass"] = bool(
        max(value for key, value in checks.items() if key.endswith("error")) < 1.0e-12
        and checks["n2_offdiagonal_is_two"]
        and checks["full_results_pass"]
    )
    if not checks["all_pass"]:
        raise SystemExit(json.dumps(checks, sort_keys=True))
    print(json.dumps(checks, sort_keys=True))


if __name__ == "__main__":
    main()
