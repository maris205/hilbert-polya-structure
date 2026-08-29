#!/usr/bin/env python3
"""Deterministic certificate for the constant-field LLG sphere flow.

The receipt records exact source-local formulas and high precision regression
rows.  It deliberately contains no target arithmetic data.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
import math
import os
from pathlib import Path

import mpmath as mp

SOURCE_COMMIT = "0ebc633706bc34b8b915a44749423486fd4cd243"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c234_llg_evidence.json"
mp.mp.dps = 90


def ftext(v: Fraction) -> str:
    return str(v.numerator) if v.denominator == 1 else f"{v.numerator}/{v.denominator}"


def mpq(v: Fraction | int) -> mp.mpf:
    return mp.mpf(v.numerator) / v.denominator if isinstance(v, Fraction) else mp.mpf(v)


def dec(v: mp.mpf | int | Fraction, digits: int = 64) -> str:
    x = mpq(v) if isinstance(v, Fraction) else mp.mpf(v)
    if abs(x) < mp.mpf("1e-82"):
        return "0.0"
    return mp.nstr(x, digits, strip_zeros=False, min_fixed=-70, max_fixed=70)


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def trajectory(alpha: Fraction, omega: Fraction, t: Fraction, m30: Fraction) -> dict:
    a = mpq(alpha) * mpq(omega)
    tm, m0 = mpq(t), mpq(m30)
    m3 = mp.tanh(a * tm + mp.atanh(m0))
    # The stereographic modulus decays exponentially, while the physical
    # transverse radius on S^2 is reconstructed nonlinearly from it.
    r = mp.sqrt(1 - m3 * m3)
    phase = mpq(omega) * tm
    z0 = mp.sqrt((1 - m0) / (1 + m0))
    z = z0 * mp.exp((-a + 1j * mpq(omega)) * tm)
    m1 = 2 * mp.re(z) / (1 + abs(z) ** 2)
    m2 = 2 * mp.im(z) / (1 + abs(z) ** 2)
    return {
        "alpha": ftext(alpha), "omega": ftext(omega), "time": ftext(t), "m3_initial": ftext(m30),
        "damping_rate_alpha_omega": dec(a), "m3_exact": dec(m3), "transverse_radius": dec(r),
        "z_real": dec(mp.re(z)), "z_imag": dec(mp.im(z)), "z_modulus": dec(abs(z)),
        "phase_unwrapped": dec(phase), "energy_one_minus_m3": dec(1 - m3),
        "energy_derivative": dec(-a * (1 - m3 * m3)),
        "norm_residual": dec(m1 * m1 + m2 * m2 + m3 * m3 - 1),
        "stereographic_residual": dec(abs(z) - mp.sqrt((1 - m3) / (1 + m3))),
    }


FLOW_CASES = [
    (Fraction(0), Fraction(1), Fraction(0), Fraction(-3, 4)),
    (Fraction(0), Fraction(1), Fraction(1, 2), Fraction(1, 3)),
    (Fraction(1, 2), Fraction(1), Fraction(1), Fraction(-1, 3)),
    (Fraction(1), Fraction(2), Fraction(3, 2), Fraction(0)),
    (Fraction(2), Fraction(1, 3), Fraction(2), Fraction(3, 4)),
    (Fraction(3, 2), Fraction(0), Fraction(2), Fraction(-1, 2)),
]


def stability_rows() -> list[dict]:
    cases = [(Fraction(0), Fraction(1)), (Fraction(1, 2), Fraction(1)), (Fraction(1), Fraction(2)), (Fraction(2), Fraction(1, 3))]
    rows = []
    for alpha, omega in cases:
        a = mpq(alpha) * mpq(omega)
        rows.append({
            "alpha": ftext(alpha), "omega": ftext(omega),
            "north_real_eigenvalue": dec(-a), "north_imaginary_frequency": dec(omega),
            "south_real_eigenvalue": dec(a), "south_imaginary_frequency": dec(omega),
            "north_class": "asymptotically_stable" if a > 0 else "center_neutral",
            "south_class": "unstable" if a > 0 else "center_neutral",
        })
    return rows


def sampled_class(alpha: Fraction, omega: Fraction, turns: Fraction) -> tuple[str, int]:
    if omega == 0 or turns == 0:
        return "identity_whole_sphere", 2
    if alpha == 0 and turns.denominator == 1:
        return "resonant_whole_sphere", 2
    if alpha == 0:
        return "nonresonant_two_poles", 0
    return "damped_two_poles", 0


SAMPLED_CASES = [
    (Fraction(0), Fraction(1), Fraction(1)),
    (Fraction(0), Fraction(1), Fraction(1, 2)),
    (Fraction(1), Fraction(1), Fraction(1)),
    (Fraction(2), Fraction(0), Fraction(3, 2)),
    (Fraction(0), Fraction(2), Fraction(3, 2)),
    (Fraction(1, 2), Fraction(2), Fraction(0)),
]


def sampled_rows() -> list[dict]:
    rows = []
    for alpha, omega, turns in SAMPLED_CASES:
        case, dim = sampled_class(alpha, omega, turns)
        rows.append({
            "alpha": ftext(alpha), "omega": ftext(omega), "tau_over_2pi_over_omega": ftext(turns),
            "fixed_set_class": case, "fixed_set_dimension": dim,
            "latitude_family": alpha == 0 and omega > 0,
        })
    return rows


def boundary_rows() -> list[dict]:
    return [
        {"face": "omega_zero", "condition": "omega=0", "flow": "identity", "energy_change": "0", "fixed_set": "whole_sphere"},
        {"face": "alpha_zero", "condition": "alpha=0,omega>0", "flow": "rigid_rotation", "energy_change": "0", "fixed_set": "resonant_or_two_poles"},
        {"face": "positive_damping", "condition": "alpha>0,omega>0", "flow": "north_attractor_south_repeller", "energy_change": "nonpositive", "fixed_set": "two_poles_for_tau>0"},
        {"face": "north_pole", "condition": "m=e3", "flow": "equilibrium", "energy_change": "0", "fixed_set": "north_pole"},
        {"face": "south_pole", "condition": "m=-e3", "flow": "equilibrium", "energy_change": "0", "fixed_set": "south_pole"},
    ]


def build() -> dict:
    data = {
        "schema": "hcs-c234-llg-constant-field-v1",
        "candidate_id": "HCS-C234",
        "evaluation_date": "2026-08-29",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "evaluator": {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256},
        "headline": "The constant-field Landau--Lifshitz--Gilbert sphere flow is exactly solvable in stereographic coordinates, with a damping-selected north pole, a repelling south pole, and a continuous periodic-latitude obstruction on the alpha=0 face.",
        "frozen_object": {
            "equation": "m_dot=-omega m cross e3-alpha omega m cross (m cross e3)",
            "phase_space": "S^2={m in R^3:|m|=1}",
            "parameters": "alpha>=0, omega>=0; normalized convention absorbs the usual (1+alpha^2) Gilbert factor into omega/time",
            "stereographic_coordinate": "z=(m1+i m2)/(1+m3)",
            "exact_stereographic_flow": "z_dot=(-alpha omega+i omega)z",
            "m3_formula": "m3(t)=tanh(alpha omega t+artanh(m3(0))) for -1<m3(0)<1",
            "energy": "E(m)=1-m3",
            "clock": "physical ODE time t; alpha=0 gives continuous latitude families, not isolated primitive cycles",
            "primitive_periodic_orbit": False,
            "forbidden_data": "target primes/zeros, arithmetic local data, Euler factors, root numbers, automorphy, target divisors, Hilbert-Polya operators",
        },
        "theorem": {
            "stereographic_solution": "On the chart m3>-1, z(t)=z(0) exp((-alpha omega+i omega)t) exactly.",
            "sphere_reconstruction": "m1+i m2=2z/(1+|z|^2) and m3=(1-|z|^2)/(1+|z|^2), with the poles treated separately.",
            "m3_solution": "m3(t)=tanh(alpha omega t+artanh(m3(0))) for interior initial data.",
            "energy_dissipation": "E=1-m3 obeys dE/dt=-alpha omega(1-m3^2)<=0.",
            "stability": "For alpha omega>0, north is asymptotically stable and south is unstable; for alpha=0 both are center-neutral with transverse frequency omega.",
            "periodic_face": "For alpha=0 and omega>0 every nonpolar latitude is periodic with period 2pi/omega; these are continuous families.",
            "identity_face": "For omega=0 the vector field and sampled maps are the identity for every alpha.",
            "sampled_fixed_sets": "For tau>0, positive damping fixes exactly the two poles; alpha=0 fixes the whole sphere iff omega tau is an integer multiple of 2pi, otherwise only the poles; omega=0 fixes the whole sphere.",
            "degenerate_boundaries": "The north/south charts, alpha=0, omega=0, tau=0 and the product alpha omega=0 are separate faces; no chart singularity is hidden.",
            "scope": "This is a source-local continuous ODE theorem; no arithmetic divisor, primitive-orbit zeta, Hilbert-Polya operator, or target spectral claim is asserted.",
        },
        "regression": {
            "flow_rows": [trajectory(*case) for case in FLOW_CASES],
            "stability_rows": stability_rows(),
            "boundary_rows": boundary_rows(),
            "sampled_rows": sampled_rows(),
            "row_counts": {"flow": len(FLOW_CASES), "stability": 4, "boundary": 5, "sampled": len(SAMPLED_CASES)},
            "working_decimal_digits": 90,
            "serialized_significant_digits": 64,
        },
        "exact_identities": [
            {"name": "stereographic_linearization", "formula": "z_dot=(-alpha omega+i omega)z"},
            {"name": "m3_logistic", "formula": "m3_dot=alpha omega(1-m3^2)"},
            {"name": "sphere_reconstruction", "formula": "m1+i m2=2z/(1+|z|^2), m3=(1-|z|^2)/(1+|z|^2)"},
            {"name": "norm_constraint", "formula": "m1^2+m2^2+m3^2=1"},
            {"name": "energy_law", "formula": "d(1-m3)/dt=-alpha omega(1-m3^2)"},
            {"name": "north_linear_mode", "formula": "lambda_N=-alpha omega+i omega"},
            {"name": "south_linear_mode", "formula": "lambda_S=+alpha omega+i omega"},
            {"name": "latitude_period", "formula": "T=2pi/omega when alpha=0, omega>0"},
            {"name": "sample_resonance", "formula": "alpha=0 and omega tau in 2pi Z gives identity sampled map"},
        ],
        "route_a": {
            "tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "strongest_positive": "exact stereographic flow, energy law, pole stability and sampled-time boundary atlas",
            "strongest_failure": "periodic latitudes are nonisolated continuous families and carry no intrinsic arithmetic repetition owner",
        },
        "scope_flags": {
            "uses_target_zero_table": False, "uses_prime_table": False, "claims_arithmetic_local_data": False,
            "claims_euler_factors": False, "claims_root_numbers": False, "claims_automorphy": False,
            "claims_target_divisor_or_functional_equation": False, "claims_hilbert_polya_operator": False,
            "invokes_route_b": False,
        },
        "citations": [
            {"id": "Lakshmanan2011", "title": "The fascinating world of the Landau--Lifshitz--Gilbert equation: an overview", "authors": "M. Lakshmanan", "venue": "Philosophical Transactions of the Royal Society A 369(1939), 1280--1300", "year": 2011, "doi": "10.1098/rsta.2010.0319", "role": "classical LLG convention and dynamical context"},
        ],
        "nonclaims": [
            "The stereographic solution and pole classification are classical source formulas, not claimed as a literature-priority result.",
            "Periodic latitude circles on alpha=0 are continuous families; no isolated primitive-orbit zeta is defined.",
            "The stability statement is for the exact sphere ODE and does not imply a PDE micromagnetic or spin-wave theorem.",
            "The sampled-time fixed-set ledger is source-local and does not encode primes, zeros, or a target divisor.",
            "No arithmetic local datum, Euler product, automorphy statement, Hilbert-Polya operator, or Route-B input is claimed.",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    raw = json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    tmp = args.output.with_name(args.output.name + ".tmp")
    tmp.write_text(raw)
    os.replace(tmp, args.output)
    print(json.dumps({"status": "C234_PRODUCER_PASS", "payload_sha256": data["payload_sha256"], "evidence_sha256": sha256(raw.encode()).hexdigest(), "flow_rows": 6, "stability_rows": 4, "boundary_rows": 5, "sampled_rows": 6}, sort_keys=True))


if __name__ == "__main__":
    main()
