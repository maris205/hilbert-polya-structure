#!/usr/bin/env python3
"""Deterministic non-scientific A4.16 branch transcript generator.

This executable exists only for the 102-cell scheduler/checker engineering
replay.  It performs no ODE integration, no interval proof, and no CAPD work.
The full transcript shape lets the independent mock checker exercise every
phase-record parser and tube-arithmetic path without licensing a theorem.
"""

from __future__ import annotations

import os
import sys
from decimal import Decimal


def canonical_argv0() -> str:
    value = sys.argv[0]
    if value.startswith("/proc/self/fd/"):
        value = os.readlink(value)
        if value.endswith(" (deleted)"):
            value = value[:-10]
    return value


def decimal_token(value: Decimal) -> str:
    text = format(value, "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return "0" if text in {"", "-0", "+0"} else text


def interval(lower: str, upper: str) -> str:
    return f"[{lower},{upper}]"


def vector(values: list[str]) -> str:
    return "{" + ",".join(values) + "}"


def main() -> int:
    argv = [canonical_argv0(), *sys.argv[1:]]
    print("protocol_id=R401-VAL-L3-A1")
    print("artifact_role=BRANCH_CELL_EVALUATOR_TRANSCRIPT")
    print("authority=PRODUCER_ONLY")
    print("scientific_licensing_enabled=false")
    print("dispatch_authorized_by_evaluator=false")
    print("component_status=null")
    print("milestone_status=null")
    print("theorem_status=null")
    print("final_status=null")
    print("claim_boundary=synthetic branch ABI replay only; no scientific proof")
    if len(argv) != 12 or argv[1] not in {"128", "256"}:
        print("contract_error=ARGUMENT_COUNT_OR_PRECISION")
        print("status=INVALID_BRANCH_PROOF_CONTRACT")
        return 5

    print("input_argv_count=12")
    for index, value in enumerate(argv):
        print(f"input_arg_{index:02d}={value}")
    bits = argv[1]
    print(f"precision_bits={bits}")
    print("taylor_order=24")
    print("tolerance=" + ("1e-30" if bits == "128" else "1e-60"))
    print("phase_grid=64")

    epsilon = interval(argv[2], argv[3])
    q_slow = interval(argv[4], argv[5])
    q_fast = interval(argv[6], argv[7])
    p_slow = interval(argv[8], argv[9])
    period = interval(argv[10], argv[11])
    root_box = vector([q_slow, q_fast, p_slow, period])
    zero = "[0,0]"
    synthetic_state = vector([zero, zero, zero, zero, epsilon, period])
    print(f"epsilon={epsilon}")
    print(f"root_box={root_box}")
    print(f"initial_state_box={vector([q_slow, q_fast, p_slow, zero, epsilon, period])}")
    print("omega_slow=[4,5]")
    print("tube_radius_sq=[0.0016,0.0016]")

    denominator = Decimal(64)
    for index in range(64):
        left = decimal_token(Decimal(index) / denominator)
        right = decimal_token(Decimal(index + 1) / denominator)
        stem = f"segment_{index:03d}"
        print(f"{stem}_phase={interval(left, right)}")
        print(f"{stem}_state={synthetic_state}")
        print(f"{stem}_rslow_sq=[0,0]")
        print(f"{stem}_margin_sq=[0.0016,0.0016]")
        print(f"{stem}_relation=INSIDE")

    print("solution_left_domain=[0,0]")
    print("solution_right_domain=[1,1]")
    print("solution_piece_count=64")
    print(f"terminal_state_box={synthetic_state}")
    print("maximum_rslow_sq_upper=[0,0]")
    print("all_segments_inside=1")
    print("lower_bound_violation_witness=0")
    print("status=BRANCH_CELL_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
