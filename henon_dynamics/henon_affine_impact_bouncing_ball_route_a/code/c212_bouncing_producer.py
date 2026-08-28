#!/usr/bin/env python3
"""Produce the exact C212 affine-impact bouncing-ball certificate."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
import os
from pathlib import Path

SOURCE_COMMIT = "e8054522273dbd545f9d406978e5d4648c627918"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c212_bouncing_evidence.json"
N_ITERATES = 8

CASE_SPECS = [
    ("forced_half", F(1), F(1, 2), F(1), F(2)),
    ("forced_three_quarters", F(5, 2), F(3, 4), F(3, 2), F(1)),
    ("forced_one_step", F(9, 4), F(0), F(2), F(5, 2)),
    ("zeno_half", F(1), F(1, 2), F(0), F(3)),
    ("zeno_three_quarters", F(2), F(3, 4), F(0), F(1)),
    ("sticking_r_zero", F(3, 2), F(0), F(0), F(4, 3)),
    ("elastic_identity_unit", F(1), F(1), F(0), F(1)),
    ("elastic_identity_scaled", F(5, 2), F(1), F(0), F(7, 4)),
    ("accelerating_unit", F(1), F(1), F(1), F(1)),
    ("accelerating_scaled", F(2), F(1), F(3, 2), F(1, 2)),
    ("forced_two_thirds", F(7, 3), F(2, 3), F(1, 3), F(5, 4)),
    ("forced_one_third", F(11, 6), F(1, 3), F(2), F(1, 2)),
]


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def q(value: F) -> str:
    return str(value)


def classify(r: F, impulse: F) -> str:
    if r == 1 and impulse == 0:
        return "elastic_identity"
    if r == 1:
        return "accelerating_translation"
    if impulse == 0 and r == 0:
        return "sticking_edge"
    if impulse == 0:
        return "zeno_contraction"
    if r == 0:
        return "forced_one_step"
    return "forced_contraction"


def formal_zeta(r: F, impulse: F) -> dict:
    # The regular section excludes zero; the closed affine section is a
    # separate formal object and must never be read as a flow zeta.
    if r < 1 and impulse > 0:
        return {
            "regular_section": "S_+=(0,infinity)",
            "physical_fixed_point": q(impulse / (1 - r)),
            "physical_event_map_series": "1/(1-z)",
            "closed_section": "S_closed=[0,infinity)",
            "closed_affine_series": "1/(1-z)",
            "interpretation": "one positive-duration forced cycle",
        }
    if r < 1:
        return {
            "regular_section": "S_+=(0,infinity)",
            "physical_fixed_point": None,
            "physical_event_map_series": "1",
            "closed_section": "S_closed=[0,infinity)",
            "closed_affine_series": "1/(1-z)",
            "interpretation": "closed-section fixed point u=0 is rest, not a flight",
        }
    if impulse == 0:
        return {
            "regular_section": "S_+=(0,infinity)",
            "physical_fixed_point": "continuum",
            "physical_event_map_series": "undefined_continuum",
            "closed_section": "S_closed=[0,infinity)",
            "closed_affine_series": "undefined_continuum",
            "interpretation": "elastic periods are a continuum; u=0 is rest",
        }
    return {
        "regular_section": "S_+=(0,infinity)",
        "physical_fixed_point": None,
        "physical_event_map_series": "1",
        "closed_section": "S_closed=[0,infinity)",
        "closed_affine_series": "1",
        "interpretation": "translation has no fixed point",
    }


def impact_samples(g: F, r: F, impulse: F) -> list[dict]:
    # Choose q0 so the discriminant is an exact square in all three controls.
    seeds = [(F(4), F(1), F(3)), (F(3, 2), F(-1), F(2)), (F(1, 2), F(0), F(1))]
    rows = []
    for label, (scaled_q, velocity, speed) in zip(("upward", "downward", "resting_start"), seeds):
        q0 = scaled_q / g
        tau = (velocity + speed) / g
        rows.append({
            "label": label,
            "q0": q(q0),
            "v0": q(velocity),
            "discriminant_speed": q(speed),
            "first_impact_time": q(tau),
            "outgoing_speed_after_reset": q(r * speed + impulse),
        })
    return rows


def build_case(case_id: str, g: F, r: F, impulse: F, u0: F) -> dict:
    regime = classify(r, impulse)
    speeds = [u0]
    for _ in range(N_ITERATES):
        speeds.append(r * speeds[-1] + impulse)
    times = [F(0)]
    for speed in speeds[:-1]:
        times.append(times[-1] + 2 * speed / g)
    if r < 1:
        fixed = impulse / (1 - r)
        fixed_text = q(fixed)
        total_zeno = q(2 * u0 / (g * (1 - r))) if impulse == 0 and 0 < r < 1 else None
    else:
        fixed_text = None
        total_zeno = None
    positive_flights = sum(1 for speed in speeds[:-1] if speed > 0)
    return {
        "case_id": case_id,
        "g": q(g),
        "restitution": q(r),
        "impulse": q(impulse),
        "u0": q(u0),
        "iterate_count": N_ITERATES,
        "regime": regime,
        "u_sequence_n0_to_n8": [q(speed) for speed in speeds],
        "cumulative_time_n0_to_n8": [q(time) for time in times],
        "flight_roof_n0_to_n7": [q(2 * speed / g) for speed in speeds[:-1]],
        "fixed_speed": fixed_text,
        "forced_period": q(2 * (impulse / (1 - r)) / g) if r < 1 and impulse > 0 else None,
        "event_multiplier": q(r),
        "positive_flight_count_in_ledger": positive_flights,
        "zeno_accumulation_time": total_zeno,
        "impact_samples": impact_samples(g, r, impulse),
        "zeta": formal_zeta(r, impulse),
    }


def build() -> dict:
    cases = [build_case(*spec) for spec in CASE_SPECS]
    data = {
        "schema": "hcs-c212-affine-impact-bouncing-ball-v1",
        "candidate_id": "HCS-C212",
        "evaluation_date": "2026-08-28",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "evaluator": {
            "path": "flow_systems/skills/route-a-evaluator.md",
            "version": "0.2.0",
            "sha256": EVALUATOR_SHA256,
        },
        "headline": (
            "An affine-impact bouncing ball has an exact physical event-time atlas: "
            "Zeno, forced-cycle, sticking, elastic, and accelerating boundaries"
        ),
        "frozen_object": {
            "flow": "q'=v, v'=-g for q>0",
            "guard": "q=0 with incoming v^-<0",
            "reset": "v^+=r*(-v^-)+J",
            "parameters": "g>0, 0<=r<=1, J>=0",
            "clock": "physical continuous time t; positive-flight roof tau(u)=2u/g",
            "section": "regular positive-flight section S_+=(0,infinity); S_closed=[0,infinity) only for a separate formal affine series",
            "rest_convention": "(q,v)=(0,0) is an absorbing rest state and is not a zero-duration periodic flight",
            "forbidden_data": "target primes, target zeros, local arithmetic, Euler factors, root numbers, automorphy, target functional equations",
        },
        "theorem": {
            "interior_impact": "tau0=(v0+sqrt(v0^2+2*g*q0))/g, w0=sqrt(v0^2+2*g*q0), u0=r*w0+J",
            "event_map": "P(u)=r*u+J on u>0 with roof tau(u)=2*u/g",
            "contraction_iterates": "for r!=1, u_n=u_*+r^n(u0-u_*), u_*=J/(1-r)",
            "contraction_times": "t_n=(2/g)[n*u_*+(u0-u_*)(1-r^n)/(1-r)]",
            "translation_iterates": "for r=1, u_n=u0+nJ and t_n=(2/g)[n*u0+J*n*(n-1)/2]",
            "strict_zeno": "J=0 and 0<r<1 with u0>0 gives geometric positive flights and accumulation 2*u0/[g*(1-r)]",
            "r_zero_boundary": "r=0,J=0 has at most one positive-duration flight and then sticks at rest; it is not an infinite Zeno sequence",
            "forced_cycle": "J>0 and 0<=r<1 gives unique positive fixed speed u*=J/(1-r), period 2*u*/g, multiplier r, and convergence",
            "elastic_boundary": "r=1,J=0 gives a continuum of positive flights of periods 2*u/g; u=0 is rest",
            "translation_boundary": "r=1,J>0 has no periodic positive flight and quadratic cumulative times",
            "multiplier": "the outgoing-section derivative is P'(u)=r; no full saltation matrix is claimed",
            "series_domain": "physical event series uses S_+; closed affine series at u=0 is formal and not a physical-flow zeta",
        },
        "cases": cases,
        "boundary_ledger": [
            {"label": "J=0, 0<r<1", "physical_status": "strict_Zeno", "series_status": "S_+ empty; S_closed formal fixed point at 0"},
            {"label": "r=0, J=0", "physical_status": "one_flight_then_sticking", "series_status": "S_+ empty; no infinite Zeno"},
            {"label": "J>0, 0<=r<1", "physical_status": "unique_forced_cycle", "series_status": "S_+ series 1/(1-z)"},
            {"label": "r=1, J=0", "physical_status": "continuum_elastic", "series_status": "undefined continuum"},
            {"label": "r=1, J>0", "physical_status": "accelerating_nonperiodic", "series_status": "empty series 1"},
        ],
        "summary": {
            "case_count": len(cases),
            "event_time_cells": len(cases) * N_ITERATES,
            "impact_sample_cells": len(cases) * 3,
            "iterate_count": N_ITERATES,
            "strict_zeno_cases": sum(1 for spec in CASE_SPECS if spec[3] == 0 and 0 < spec[2] < 1),
            "r_zero_sticking_cases": sum(1 for spec in CASE_SPECS if spec[2] == 0 and spec[3] == 0),
            "forced_cycle_cases": sum(1 for spec in CASE_SPECS if spec[3] > 0 and spec[2] < 1),
            "elastic_cases": sum(1 for spec in CASE_SPECS if spec[2] == 1 and spec[3] == 0),
            "translation_cases": sum(1 for spec in CASE_SPECS if spec[2] == 1 and spec[3] > 0),
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "strongest_positive": "The guard, affine reset, physical roof, and all boundary regimes are exact.",
            "strongest_failure": "The hybrid event system has no arithmetic primitive owner, target determinant, or same-clock self-adjoint lift.",
        },
        "scope_flags": {
            "uses_target_zero_table": False,
            "uses_prime_table": False,
            "claims_arithmetic_local_data": False,
            "claims_euler_factors": False,
            "claims_root_numbers": False,
            "claims_automorphy": False,
            "claims_target_divisor_or_functional_equation": False,
            "claims_hilbert_polya_operator": False,
            "invokes_route_b": False,
        },
        "citations": [
            {"key": "LeineNijmeijer2004", "claim": "non-smooth mechanical-system context", "title": "Dynamics and Bifurcations of Non-Smooth Mechanical Systems", "authors": "R. I. Leine and H. Nijmeijer", "venue": "Springer", "year": 2004, "doi": "10.1007/978-3-540-44398-8"},
            {"key": "GoebelSanfeliceTeel2012", "claim": "hybrid-system modeling and stability context", "title": "Hybrid Dynamical Systems: Modeling, Stability, and Robustness", "authors": "R. Goebel, R. G. Sanfelice, and A. R. Teel", "venue": "Princeton University Press", "year": 2012, "doi": "10.1515/9781400842636"},
        ],
        "nonclaims": [
            "a full two-dimensional saltation matrix",
            "a physical-flow zeta; only explicitly named event-map series are formal",
            "calling the r=0,J=0 edge an infinite Zeno execution",
            "target prime-orbit law, local arithmetic datum, Euler factor, root number, automorphy, target functional equation, or Hilbert--Polya operator",
            "external peer review, novelty certification, or an acceptance score",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path(os.environ.get("C212_OUTPUT", DEFAULT_OUTPUT)))
    args = parser.parse_args()
    result = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "C212_PRODUCER_PASS", "cases": result["summary"]["case_count"],
                      "event_time_cells": result["summary"]["event_time_cells"],
                      "payload_sha256": result["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
