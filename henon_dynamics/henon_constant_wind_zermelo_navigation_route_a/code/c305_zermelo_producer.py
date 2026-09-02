#!/usr/bin/env python3
"""Deterministic all-chamber receipts for constant-wind Zermelo navigation."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c305_zermelo_evidence.json"
SOURCE = "c0259978b1d7ebae63fe7b39fce1af2655b8529d"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600
mp.mp.dps = 90

FLAGS = {
    "claims_target_arithmetic_local_data": False,
    "claims_target_euler_factors": False,
    "claims_root_number": False,
    "claims_automorphy": False,
    "claims_target_divisor_or_counting_law": False,
    "claims_target_functional_equation": False,
    "claims_target_zero_match": False,
    "claims_hilbert_polya_operator": False,
    "invokes_route_b": False,
}

CASE_SPECS = [
    ("W0-D1", ["0"], "2", ["3"]),
    ("W0-D2-345", ["0", "0"], "3", ["3", "4"]),
    ("WEAK-DOWNWIND", ["1", "0"], "2", ["3", "0"]),
    ("WEAK-UPWIND", ["1", "0"], "2", ["-3", "0"]),
    ("WEAK-CROSSWIND", ["1", "0"], "2", ["0", "2"]),
    ("WEAK-PYTHAGOREAN", ["3", "4"], "6", ["1", "2"]),
    ("WEAK-D3", ["1", "0", "0"], "2", ["1", "1", "1"]),
    ("WEAK-NEAR-CRITICAL", ["3", "4"], "26/5", ["-2", "1"]),
    ("CRIT-D1-FORWARD", ["1"], "1", ["3"]),
    ("CRIT-D2-FORWARD", ["1", "0"], "1", ["1", "1"]),
    ("CRIT-TANGENT-NO", ["1", "0"], "1", ["0", "1"]),
    ("CRIT-BACKWARD-NO", ["1", "0"], "1", ["-1", "0"]),
    ("CRIT-34-DOWNWIND", ["3", "4"], "5", ["3", "4"]),
    ("CRIT-D3-FORWARD", ["0", "0", "2"], "2", ["1", "0", "2"]),
    ("STRONG-D1-FORWARD", ["2"], "1", ["3"]),
    ("STRONG-D1-BACKWARD-NO", ["2"], "1", ["-1"]),
    ("STRONG-AXIS", ["5", "0"], "3", ["4", "0"]),
    ("STRONG-MACH-BOUNDARY", ["5", "0"], "3", ["4", "3"]),
    ("STRONG-OUTSIDE-NO", ["5", "0"], "3", ["3", "4"]),
    ("STRONG-BACKWARD-NO", ["5", "0"], "3", ["-1", "0"]),
    ("STRONG-D3-BOUNDARY", ["0", "0", "5"], "4", ["4", "0", "3"]),
    ("STRONG-D3-INTERIOR", ["0", "0", "5"], "4", ["1", "2", "5"]),
    ("CZERO-RAY", ["2", "0"], "0", ["4", "0"]),
    ("CZERO-OFF-RAY-NO", ["2", "0"], "0", ["4", "1"]),
    ("DEGENERATE-ZERO", ["0", "0"], "0", ["0", "0"]),
    ("DEGENERATE-NONZERO-NO", ["0", "0"], "0", ["1", "0"]),
    ("WEAK-ZERO-TARGET", ["1", "0"], "2", ["0", "0"]),
    ("CRIT-ZERO-TARGET", ["1", "0"], "1", ["0", "0"]),
    ("STRONG-ZERO-TARGET", ["2", "0"], "1", ["0", "0"]),
]

HJB_IDS = [
    "W0-D1", "W0-D2-345", "WEAK-DOWNWIND", "WEAK-UPWIND",
    "WEAK-CROSSWIND", "WEAK-PYTHAGOREAN", "CRIT-D1-FORWARD",
    "CRIT-D2-FORWARD", "CRIT-D3-FORWARD", "STRONG-D1-FORWARD",
    "STRONG-AXIS", "STRONG-D3-INTERIOR",
]


def f(text: str) -> Fraction:
    return Fraction(text)


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def mpf(value: Fraction) -> mp.mpf:
    return mp.mpf(value.numerator) / value.denominator


def dec(value: mp.mpf) -> str:
    if value == 0:
        return "0.0"
    return mp.nstr(value, 72, strip_zeros=False)


def dot(left, right):
    return sum((x * y for x, y in zip(left, right)), Fraction(0))


def sqnorm(vector):
    return dot(vector, vector)


def leaf_count(value) -> int:
    if type(value) is dict:
        return sum(leaf_count(item) for item in value.values())
    if type(value) is list:
        return sum(leaf_count(item) for item in value)
    return 1


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def solve(W, c, target):
    w2, p, r2 = sqnorm(W), dot(W, target), sqnorm(target)
    a = w2 - c * c
    discriminant = p * p - a * r2
    if w2 == 0 and c == 0:
        chamber = "degenerate_zero_velocity"
    elif a < 0:
        chamber = "weak_wind"
    elif a == 0:
        chamber = "critical_wind"
    else:
        chamber = "strong_wind"
    if r2 == 0:
        reachable = True
    elif chamber == "degenerate_zero_velocity":
        reachable = False
    elif a < 0:
        reachable = True
    elif a == 0:
        reachable = p > 0
    else:
        reachable = p > 0 and discriminant >= 0

    T = None
    upper = None
    formula = "unreachable"
    if r2 == 0:
        T = mp.mpf("0")
        formula = "zero_target"
        interval_kind = "all_nonnegative_times" if w2 <= c * c else "singleton_zero"
        upper = None if w2 <= c * c else mp.mpf("0")
    elif reachable and a < 0:
        T = (mp.sqrt(mpf(discriminant)) - mpf(p)) / mpf(-a)
        formula = "weak_radical"
        interval_kind = "lower_ray"
    elif reachable and a == 0:
        T = mpf(r2) / (2 * mpf(p))
        formula = "critical_parabolic"
        interval_kind = "lower_ray"
    elif reachable:
        root = mp.sqrt(mpf(discriminant))
        T = (mpf(p) - root) / mpf(a)
        upper = (mpf(p) + root) / mpf(a)
        formula = "strong_smaller_root"
        interval_kind = "closed_window"
    else:
        interval_kind = "empty"

    if T is not None and r2 != 0:
        control = [mpf(target[i]) / T - mpf(W[i]) for i in range(len(W))]
        speed = mp.sqrt(sum(item * item for item in control))
        residual = mp.sqrt(sum((mpf(W[i]) * T + control[i] * T - mpf(target[i])) ** 2 for i in range(len(W))))
    else:
        control = speed = residual = None
    return {
        "w_squared": w2, "p": p, "r_squared": r2, "a": a,
        "discriminant": discriminant, "chamber": chamber,
        "reachable": reachable, "T": T, "upper": upper,
        "interval_kind": interval_kind, "formula": formula,
        "control": control, "speed": speed, "residual": residual,
    }


def build_case(spec):
    case_id, W_text, c_text, target_text = spec
    W, c, target = [f(item) for item in W_text], f(c_text), [f(item) for item in target_text]
    answer = solve(W, c, target)
    upper_receipt = None
    if answer["interval_kind"] == "closed_window":
        upper_receipt = dec(answer["upper"])
    elif answer["interval_kind"] == "singleton_zero":
        upper_receipt = "0.0"
    return {
        "case_id": case_id,
        "dimension": len(W),
        "wind": [q(item) for item in W],
        "speed_cap": q(c),
        "target": [q(item) for item in target],
        "w_squared": q(answer["w_squared"]),
        "p": q(answer["p"]),
        "r_squared": q(answer["r_squared"]),
        "quadratic_coefficient": q(answer["a"]),
        "discriminant": q(answer["discriminant"]),
        "chamber": answer["chamber"],
        "reachable": answer["reachable"],
        "minimum_time": None if answer["T"] is None else dec(answer["T"]),
        "formula_branch": answer["formula"],
        "attainable_time_interval": {
            "kind": answer["interval_kind"],
            "lower": None if answer["T"] is None else dec(answer["T"]),
            "upper": upper_receipt,
        },
        "optimal_control": None if answer["control"] is None else [dec(item) for item in answer["control"]],
        "optimal_speed": None if answer["speed"] is None else dec(answer["speed"]),
        "terminal_residual": None if answer["residual"] is None else dec(answer["residual"]),
    }


def build_hjb(case, spec):
    case_id, W_text, c_text, target_text = spec
    W, c, target = [f(item) for item in W_text], f(c_text), [f(item) for item in target_text]
    answer = solve(W, c, target)
    T = answer["T"]
    denominator = mpf(answer["p"]) - mpf(answer["a"]) * T
    gradient = [(mpf(target[i]) - mpf(W[i]) * T) / denominator for i in range(len(W))]
    lhs = sum(mpf(W[i]) * gradient[i] for i in range(len(W))) + mpf(c) * mp.sqrt(sum(item * item for item in gradient))
    return {
        "case_id": case_id,
        "gradient": [dec(item) for item in gradient],
        "hjb_lhs": dec(lhs),
        "target_scale_three_time": dec(3 * T),
        "velocity_scale_two_time": dec(T / 2),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    cases = [build_case(spec) for spec in CASE_SPECS]
    by_id = {case["case_id"]: case for case in cases}
    specs = {spec[0]: spec for spec in CASE_SPECS}
    hjb = [build_hjb(by_id[case_id], specs[case_id]) for case_id in HJB_IDS]
    boundaries = [
        {"boundary_id": "B0-zero-target", "statement": "The zero target has minimum time zero; positive-time feasibility depends on whether the wind can be cancelled."},
        {"boundary_id": "B1-zero-wind", "statement": "For W=0 and c>0 the value is Euclidean distance divided by c."},
        {"boundary_id": "B2-zero-cap", "statement": "For c=0 only the nonnegative wind ray is reachable, with no control freedom."},
        {"boundary_id": "B3-critical", "statement": "At w=c>0 a nonzero target is reachable exactly when p>0 and T=r_squared/(2p)."},
        {"boundary_id": "B4-mach-cone", "statement": "For w>c the full finite-value domain, including the origin, is the closed forward Mach cone; its nonzero boundary has a double time root."},
        {"boundary_id": "B5-regularity", "statement": "The value is smooth on each finite-value interior away from zero and has square-root loss at a nontrivial strong-wind cone boundary."},
        {"boundary_id": "B6-symmetry", "statement": "The value is rotation equivariant, degree-one in target displacement, and inverse degree-one under common velocity scaling."},
        {"boundary_id": "B7-exclusion", "statement": "No variable wind, obstacle, state constraint, manifold navigation, or global strong-wind Finsler norm is claimed."},
    ]
    data = {
        "schema": "hcs-c305-constant-wind-zermelo-v1",
        "candidate_id": "HCS-C305",
        "obstruction_id": "HEN-O289",
        "evaluation_date": "2026-09-03",
        "fixed_epoch": EPOCH,
        "source_commit": SOURCE,
        "scope_literal": SCOPE,
        "evaluator": {"version": "0.2.0", "sha256": EVALUATOR},
        "model": {
            "state_space": "R^d for every finite integer d>=1",
            "dynamics": "xdot=W+u with constant W and measurable control satisfying norm(u)<=c",
            "parameters": "W in R^d and c>=0",
            "target_data": "displacement y in R^d from the origin",
        },
        "theorem_contract": {
            "fixed_time_geometry": "the exact-time reachable set is Wt+c t closed_unit_ball",
            "three_chambers": "weak, critical, and strong wind have complete reachability and minimum-time formulas",
            "optimizer": "every nonzero reachable target has a unique almost-everywhere constant time-optimal control",
            "time_sets": "all attainable time sets are lower rays, closed strong-wind windows, singleton zero, or empty",
            "value_geometry": "positive homogeneity, rotation equivariance, velocity scaling, and HJB hold on the finite-value interior",
            "boundaries": "zero wind, zero cap, zero target, critical half-space, and strong Mach cone are explicit",
        },
        "proof_contract": {
            "quadratic": "reachability is exactly the scalar inequality (w_squared-c_squared)t_squared-2pt+r_squared<=0",
            "root_choice": "minimum time is the sole positive root in weak and critical wind and the smaller positive root in strong wind",
            "uniqueness": "equality in the average-control norm bound forces the saturated optimal control to be constant almost everywhere",
            "hjb": "for c>0 implicit differentiation gives the HJB identity; the one-dimensional c=0 interior is checked directly",
            "finite_role": "finite cases are regression receipts only; the proof covers all finite d and all parameters",
        },
        "route_a": {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"], "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False},
        "scope_flags": FLAGS,
        "nonclaims": [
            "No target arithmetic local datum, Euler factor, root number, automorphy, divisor law, functional equation, or zero match is asserted.",
            "Wind, control speeds, cones, and travel times are source navigation data rather than rational-prime labels or target coefficients.",
            "The value function and HJB equation are not asserted to define a Hilbert--Polya operator.",
            "No novelty or priority is claimed for classical Zermelo navigation or constant-drift minimum-time control.",
        ],
        "collision_boundary": {
            "C222": "C222 studies second-order double-integrator bang-bang switching; C305 is first-order constant-drift navigation with Euclidean ball-valued controls in every finite dimension.",
            "C270": "C270 studies Heisenberg sub-Riemannian control; C305 has translation-invariant Euclidean velocity balls and no noncommutative horizontal geometry.",
            "C268": "C268 is an uncontrolled constant-electromagnetic-field Lorentz flow; C305 is a controlled first-order navigation problem with norm-bounded inputs.",
        },
        "references": [
            {"identifier": "10.1002/zamm.19310110205", "role": "historical Zermelo navigation owner attribution only"},
            {"identifier": "10.4310/jdg/1098137838", "role": "navigation and Randers geometric context only"},
        ],
        "enumeration": {
            "case_count": len(cases), "case_ids": [case["case_id"] for case in cases],
            "hjb_probe_count": len(hjb), "boundary_rows": len(boundaries),
            "audited_cell_count": leaf_count(cases) + leaf_count(hjb) + leaf_count(boundaries),
        },
        "cases": cases,
        "hjb_probes": hjb,
        "boundaries": boundaries,
    }
    data["payload_sha256"] = payload_hash(data)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "C305_PRODUCER_PASS", "cases": len(cases), "hjb_probes": len(hjb), "audited_cells": data["enumeration"]["audited_cell_count"], "payload_sha256": data["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
