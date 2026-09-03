#!/usr/bin/env python3
"""Deterministic finite receipts for HCS-C324."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c324_hunter_saxton_evidence.json"
SOURCE = "1aba1f6fd0cf81baa7c137a2ce7ce3d097ba63fc"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600
EVAL_RAW = "10becdeeecc683514b331994ed85b1def0eecaddb0c9ba32d12ba3886123b2ce"
EVAL_SEMANTIC = "5f3078d80b634bc13c6e705c0414e4e5add2c42a3999a6ce82c153073807f9f7"
mp.mp.dps = 100

PROFILE_PARAMETERS = (
    (3, 4, 1), (5, 12, 2), (8, 15, 3), (7, 24, 4),
    (20, 21, 5), (9, 40, 6), (12, 35, 7), (11, 60, 8),
    (28, 45, 9), (33, 56, 10), (16, 63, 11), (48, 55, 12),
)
TIME_FRACTIONS = (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4))
SLOPE_RATIOS = (Fraction(-1), Fraction(-1, 2), Fraction(0), Fraction(1, 2), Fraction(1))
ASYMMETRIC_PARAMETERS = ((1, 1), (1, 2), (1, 3), (-1, 1), (-1, 2), (-1, 3))
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


def rat(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def dec(value: mp.mpf) -> str:
    return mp.nstr(value, 72, strip_zeros=False, min_fixed=-90, max_fixed=90)


def mpq(value: Fraction) -> mp.mpf:
    return mp.mpf(value.numerator) / value.denominator


def leaves(value) -> int:
    if type(value) is dict:
        return sum(leaves(v) for v in value.values())
    if type(value) is list:
        return sum(leaves(v) for v in value)
    return 1


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def profile_row(a: int, b: int, k: int) -> dict:
    radius = mp.sqrt(a * a + b * b)
    energy_q = Fraction(a * a + b * b, 2)
    energy = mp.mpf(energy_q.numerator) / energy_q.denominator
    root_energy = mp.sqrt(energy)
    phase = mp.atan2(b, a)
    positive_lifespan = 2 * mp.atan(root_energy / radius) / root_energy
    negative_lifespan = -2 * mp.atan(root_energy / radius) / root_energy
    minima = [dec(mp.fmod((phase + mp.pi + 2 * mp.pi * j) / (2 * mp.pi * k), 1)) for j in range(k)]
    maxima = [dec(mp.fmod((phase + 2 * mp.pi * j) / (2 * mp.pi * k), 1)) for j in range(k)]
    samples = []
    for tau in TIME_FRACTIONS:
        tau_mp = mp.mpf(tau.numerator) / tau.denominator
        time = tau_mp * positive_lifespan
        angle = root_energy * time / 2
        for ratio in SLOPE_RATIOS:
            ratio_mp = mp.mpf(ratio.numerator) / ratio.denominator
            initial_slope = radius * ratio_mp
            factor = mp.cos(angle) + initial_slope * mp.sin(angle) / root_energy
            numerator = -root_energy * mp.sin(angle) + initial_slope * mp.cos(angle)
            samples.append({
                "time_fraction": rat(tau),
                "initial_slope_ratio": rat(ratio),
                "time": dec(time),
                "characteristic_factor": dec(factor),
                "jacobian": dec(factor * factor),
                "transported_slope": dec(numerator / factor),
                "transformed_energy_density": dec(numerator * numerator),
            })
    return {
        "profile_id": f"harmonic-{k:02d}-{a}-{b}",
        "cosine_amplitude": a,
        "sine_amplitude": b,
        "frequency": k,
        "amplitude": dec(radius),
        "energy": rat(energy_q),
        "minimum_slope": dec(-radius),
        "maximum_slope": dec(radius),
        "positive_lifespan": dec(positive_lifespan),
        "negative_lifespan": dec(negative_lifespan),
        "breaking_multiplicity": k,
        "minimum_points": minima,
        "maximum_points": maxima,
        "samples": samples,
    }


def asymmetric_profile_row(sign: int, k: int) -> dict:
    """Receipts for sign*(cos(2*pi*k*x)+cos(4*pi*k*x)/2)."""
    energy_q = Fraction(5, 8)
    root_energy = mp.sqrt(mp.mpf(5) / 8)
    if sign == 1:
        minimum, maximum = Fraction(-3, 4), Fraction(3, 2)
        minimum_points = sorted([Fraction(j, k) + offset / k for j in range(k)
                                 for offset in (Fraction(1, 3), Fraction(2, 3))])
        maximum_points = [Fraction(j, k) for j in range(k)]
        slopes = (minimum, Fraction(-1, 2), Fraction(0), Fraction(1, 2), maximum)
    else:
        minimum, maximum = Fraction(-3, 2), Fraction(3, 4)
        minimum_points = [Fraction(j, k) for j in range(k)]
        maximum_points = sorted([Fraction(j, k) + offset / k for j in range(k)
                                 for offset in (Fraction(1, 3), Fraction(2, 3))])
        slopes = (minimum, Fraction(-1, 2), Fraction(0), Fraction(1, 2), maximum)
    positive_lifespan = 2 * mp.atan(root_energy / (-mpq(minimum))) / root_energy
    negative_lifespan = -2 * mp.atan(root_energy / mpq(maximum)) / root_energy
    samples = []
    for tau in TIME_FRACTIONS:
        time = mpq(tau) * positive_lifespan
        angle = root_energy * time / 2
        for slope in slopes:
            slope_mp = mpq(slope)
            factor = mp.cos(angle) + slope_mp * mp.sin(angle) / root_energy
            numerator = -root_energy * mp.sin(angle) + slope_mp * mp.cos(angle)
            samples.append({
                "time_fraction": rat(tau),
                "initial_slope": rat(slope),
                "time": dec(time),
                "characteristic_factor": dec(factor),
                "jacobian": dec(factor * factor),
                "transported_slope": dec(numerator / factor),
                "transformed_energy_density": dec(numerator * numerator),
            })
    return {
        "profile_id": f"asymmetric-{'plus' if sign > 0 else 'minus'}-{k:02d}",
        "sign": sign,
        "frequency": k,
        "definition": "sign*(cos(2*pi*k*x)+cos(4*pi*k*x)/2)",
        "energy": rat(energy_q),
        "minimum_slope": rat(minimum),
        "maximum_slope": rat(maximum),
        "positive_lifespan": dec(positive_lifespan),
        "negative_lifespan": dec(negative_lifespan),
        "positive_breaking_multiplicity": len(minimum_points),
        "negative_breaking_multiplicity": len(maximum_points),
        "minimum_points": [rat(value) for value in minimum_points],
        "maximum_points": [rat(value) for value in maximum_points],
        "samples": samples,
    }


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C324 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    profiles = [profile_row(*row) for row in PROFILE_PARAMETERS]
    asymmetric_profiles = [asymmetric_profile_row(*row) for row in ASYMMETRIC_PARAMETERS]
    data = {
        "schema": "hcs-c324-hunter-saxton-wave-breaking-v1",
        "candidate_id": "HCS-C324",
        "obstruction_id": "HEN-O308",
        "evaluation_date": "2026-09-03",
        "fixed_epoch": EPOCH,
        "source_commit": SOURCE,
        "scope_literal": SCOPE,
        "evaluator": {"authority": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR},
        "evaluation_lock": {
            "relative_path": "evaluations/route_a/HCS-C324/2026-09-03.yaml",
            "raw_sha256": EVAL_RAW,
            "semantic_sha256": EVAL_SEMANTIC,
        },
        "model": {
            "domain": "unit circle R/Z",
            "equation": "u_tx+u*u_xx+(u_x)^2/2=-E/2 with E=integral_0^1 (u_x)^2 dx",
            "regularity": "C2 initial profile and once-integrated classical formulation before characteristic degeneration",
            "gauge": "an additive spatial constant fixes characteristic translation but does not affect the slope theorem",
        },
        "theorem_contract": {
            "jacobian": "eta_x=(cos(sqrt(E)t/2)+(u0_x/sqrt(E))sin(sqrt(E)t/2))^2",
            "slope": "u_x along eta is the logarithmic time derivative of eta_x",
            "positive_lifespan": "T_plus=2/sqrt(E)*atan(sqrt(E)/(-min u0_x))",
            "breaking_set": "the first positive breaking labels are exactly the minimizers of u0_x",
            "universal_rate": "u_x(t,eta(t,x))=-2/(T_plus-t)+O(1) at every first breaking label",
            "negative_boundary": "T_minus=-2/sqrt(E)*atan(sqrt(E)/(max u0_x))",
            "energy": "integral (u_x along eta)^2 eta_x dx equals E before breaking",
        },
        "profiles": profiles,
        "asymmetric_profiles": asymmetric_profiles,
        "boundary_atlas": [
            {"face": "E=0", "status": "u0 is spatially constant and no wave breaking occurs"},
            {"face": "multiple global minima", "status": "all minimizing labels break simultaneously at T_plus"},
            {"face": "negative time", "status": "the first backward endpoint is T_minus and is controlled by max u0_x"},
            {"face": "t=T_plus", "status": "eta_x vanishes and the classical diffeomorphism chart ends"},
            {"face": "t beyond first breaking", "status": "weak, conservative, and dissipative continuations are outside scope"},
            {"face": "unintegrated third-order equation", "status": "only distributionally inferred; C2 data are handled in the integrated formulation"},
        ],
        "collision_boundary": {
            "C195": "viscous Burgers has parabolic smoothing rather than Hunter--Saxton slope focusing",
            "C256": "KdV cnoidal waves are dispersive traveling waves rather than arbitrary-data breaking",
            "C278": "Camassa--Holm two-peakons form a finite-dimensional weak-solution manifold rather than this C2 pre-breaking theorem",
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": FLAGS,
        "nonclaims": [
            "No priority is claimed for the Hunter--Saxton equation, its geometric formulation, or classical wave breaking.",
            "No solution continuation after first breaking is constructed or selected.",
            "Finite harmonic-profile receipts do not prove the all-initial-data theorem.",
            "The geometric formulation is not a Hilbert--Polya operator or a Route-B authorization.",
            "No target arithmetic local data, Euler factors, root numbers, automorphy, target divisor, functional equation, or target-zero match is asserted.",
        ],
        "references": [
            {"doi": "10.1137/0151075", "role": "original Hunter--Saxton equation and finite-time breakdown source"},
            {"doi": "10.1137/050647451", "role": "periodic geometric formulation and explicit characteristic source"},
            {"doi": "10.1137/S0036141003425672", "role": "periodic strong-solution structure and blow-up source"},
        ],
    }
    data["enumeration"] = {
        "profiles": len(profiles),
        "breaking_labels": sum(row["breaking_multiplicity"] for row in profiles),
        "sample_rows": sum(len(row["samples"]) for row in profiles),
        "asymmetric_profiles": len(asymmetric_profiles),
        "asymmetric_positive_breaking_labels": sum(row["positive_breaking_multiplicity"] for row in asymmetric_profiles),
        "asymmetric_negative_breaking_labels": sum(row["negative_breaking_multiplicity"] for row in asymmetric_profiles),
        "asymmetric_sample_rows": sum(len(row["samples"]) for row in asymmetric_profiles),
    }
    data["enumeration"]["audited_leaf_count"] = leaves(data) + 1
    data["payload_sha256"] = payload_hash(data)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(f"C324_PRODUCER_PASS {data['payload_sha256']} {data['enumeration']['audited_leaf_count']}")


if __name__ == "__main__":
    main()
