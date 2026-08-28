#!/usr/bin/env python3
"""Produce the deterministic HCS-C219 Rayleigh cavity certificate.

The certificate is deliberately source-local.  It records the exact first
integral of the inviscid spherical-cavity equation, the pressure-sign atlas,
the incomplete-Beta collapse clock, the terminal Puiseux law, and the
Lagrangian/volume energy ledger.  No arithmetic target data are read.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
import os
from pathlib import Path

import mpmath as mp

SOURCE_COMMIT = "86c7bb8a39cdd1b8e941e45833b068170ca06287"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c219_rayleigh_evidence.json"
mp.mp.dps = 90

# The regression rows intentionally cover all three pressure signs and the
# zero-radius boundary.  Fractions keep the input convention exact.
CASES = [
    ("collapse_unit", Fraction(1), Fraction(1), Fraction(1), "collapse"),
    ("collapse_scaled", Fraction(3, 2), Fraction(5, 4), Fraction(7, 3), "collapse"),
    ("collapse_small_pressure", Fraction(1, 7), Fraction(9, 5), Fraction(4, 3), "collapse"),
    ("collapse_large_pressure", Fraction(11, 3), Fraction(2, 3), Fraction(5, 2), "collapse"),
    ("collapse_small_radius", Fraction(2), Fraction(7, 3), Fraction(1, 5), "collapse"),
    ("equilibrium_zero_pressure", Fraction(0), Fraction(4, 3), Fraction(9, 5), "equilibrium"),
    ("equilibrium_zero_pressure_unit", Fraction(0), Fraction(1), Fraction(1), "equilibrium"),
    ("expansion_unit", Fraction(-1), Fraction(1), Fraction(1), "expansion"),
    ("expansion_scaled", Fraction(-5, 2), Fraction(7, 4), Fraction(3, 2), "expansion"),
    ("expansion_weak", Fraction(-1, 6), Fraction(5, 2), Fraction(11, 6), "expansion"),
    ("zero_radius_collapse", Fraction(2), Fraction(1), Fraction(0), "boundary"),
    ("zero_radius_equilibrium", Fraction(0), Fraction(1), Fraction(0), "boundary"),
    ("zero_radius_expansion", Fraction(-2), Fraction(1), Fraction(0), "boundary"),
]
COLLAPSE_X = [Fraction(3, 4), Fraction(1, 2), Fraction(1, 4), Fraction(1, 16)]
EXPANSION_X = [Fraction(5, 4), Fraction(3, 2), Fraction(2), Fraction(4)]


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def frac_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def mp_frac(value: Fraction) -> mp.mpf:
    return mp.mpf(value.numerator) / value.denominator


def dec(value: mp.mpf | mp.mpc | None, digits: int = 54) -> str | None:
    if value is None:
        return None
    if isinstance(value, mp.mpc):
        value = mp.re(value)
    if abs(value) < mp.mpf("1e-80"):
        return "0.0"
    return mp.nstr(value, digits, strip_zeros=False, min_fixed=-60, max_fixed=60)


def beta_clock() -> mp.mpf:
    return mp.beta(mp.mpf(5) / 6, mp.mpf(1) / 2) / 3


def collapse_dimensionless_clock(x: mp.mpf) -> mp.mpf:
    """J_+(x)=int_x^1 u^(3/2)/sqrt(1-u^3) du.

    The substitution u=(1-s^2)^(1/3) removes the endpoint square root and
    gives a stable independent quadrature for the checker.
    """
    upper = mp.sqrt(1 - x**3)
    return mp.mpf(2) / 3 * mp.quad(lambda s: (1 - s**2) ** (-mp.mpf(1) / 6), [0, upper])


def expansion_dimensionless_clock(x: mp.mpf) -> mp.mpf:
    """J_-(x)=int_1^x u^(3/2)/sqrt(u^3-1) du."""
    upper = mp.sqrt(x**3 - 1)
    return mp.mpf(2) / 3 * mp.quad(lambda s: (1 + s**2) ** (-mp.mpf(1) / 6), [0, upper])


def row(case_id: str, pressure: Fraction, rho: Fraction, radius: Fraction, regime: str) -> dict:
    p = mp_frac(pressure)
    d = mp_frac(rho)
    r0 = mp_frac(radius)
    base = {
        "case_id": case_id,
        "pressure": frac_text(pressure),
        "density": frac_text(rho),
        "initial_radius": frac_text(radius),
        "regime": regime,
    }
    if regime == "boundary":
        base.update({
            "a": None,
            "beta_clock": None,
            "collapse_time": None,
            "terminal_coefficient": None,
            "initial_acceleration": None,
            "energy_constant": None,
            "volume_terminal_coefficient": None,
            "dimensionless_samples": [],
            "asymptotic_speed": None,
            "maximal_interval": "no positive-radius classical initial state at R0=0",
        })
        return base
    if p == 0:
        base.update({
            "a": "0.0",
            "beta_clock": dec(beta_clock()),
            "collapse_time": None,
            "terminal_coefficient": None,
            "initial_acceleration": "0.0",
            "energy_constant": "0.0",
            "volume_terminal_coefficient": None,
            "dimensionless_samples": [],
            "asymptotic_speed": "0.0",
            "maximal_interval": "[0,infinity), stationary R(t)=R0",
        })
        return base
    a = mp.sqrt(2 * abs(p) / (3 * d))
    bclock = beta_clock()
    energy = 4 * mp.pi * p * r0**3 / 3
    base.update({
        "a": dec(a),
        "beta_clock": dec(bclock),
        "collapse_time": dec(r0 * bclock / a) if p > 0 else None,
        "terminal_coefficient": dec(r0 ** (mp.mpf(3) / 5) * (5 * a / 2) ** (mp.mpf(2) / 5)) if p > 0 else None,
        "initial_acceleration": dec(-p / (d * r0)),
        "energy_constant": dec(energy),
        "volume_terminal_coefficient": dec(4 * mp.pi / 3 * (r0 ** (mp.mpf(3) / 5) * (5 * a / 2) ** (mp.mpf(2) / 5)) ** 3) if p > 0 else None,
        "dimensionless_samples": [],
        "asymptotic_speed": dec(a) if p < 0 else None,
        "maximal_interval": "[0,Tc) with R(Tc)=0" if p > 0 else "[0,infinity), monotone expansion",
    })
    if p > 0:
        for xq in COLLAPSE_X:
            x = mp_frac(xq)
            base["dimensionless_samples"].append({
                "x": frac_text(xq),
                "clock": dec(collapse_dimensionless_clock(x)),
            })
    else:
        for xq in EXPANSION_X:
            x = mp_frac(xq)
            base["dimensionless_samples"].append({
                "x": frac_text(xq),
                "clock": dec(expansion_dimensionless_clock(x)),
            })
    return base


def build() -> dict:
    rows = [row(*spec) for spec in CASES]
    bclock = beta_clock()
    data = {
        "schema": "hcs-c219-rayleigh-spherical-cavity-v1",
        "candidate_id": "HCS-C219",
        "evaluation_date": "2026-08-28",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "evaluator": {
            "path": "flow_systems/skills/route-a-evaluator.md",
            "version": "0.2.0",
            "sha256": EVALUATOR_SHA256,
        },
        "headline": "The inviscid spherical-cavity Rayleigh equation has a complete pressure-sign atlas, an exact incomplete-Beta collapse clock, a 2/5 terminal singularity, and a finite liquid-energy ledger.",
        "frozen_object": {
            "system": "R R_ddot + (3/2) R_dot^2 = -Pi/rho for R>0",
            "initial_data": "R(0)=R0>0, R_dot(0)=0",
            "parameters": "rho>0, R0>0, Pi in R; Pi>0 is the physical collapse sign",
            "pressure_definition": "Pi=P_infinity-P_v (positive pressure deficit for an empty cavity)",
            "clock": "physical continuous time t",
            "phase_space": "positive radius/velocity half-plane (R,V) with the R=0 boundary adjoined only as a labeled singular face",
            "energy_lagrangian": "L_phys=2*pi*rho*R^3*R_dot^2-(4*pi/3)*Pi*R^3",
            "forbidden_data": "target primes/zeros, local arithmetic, Euler factors, root numbers, automorphy, Hilbert-Polya operators",
        },
        "theorem": {
            "first_integral": "R^3 R_dot^2 + (2 Pi/(3 rho)) R^3 = (2 Pi/(3 rho)) R0^3",
            "collapse_branch": "Pi>0: R_dot=-sqrt(2 Pi/(3 rho))*sqrt((R0/R)^3-1)",
            "collapse_clock": "Tc=(R0/a)*(1/3)*B(5/6,1/2), a=sqrt(2 Pi/(3 rho))",
            "collapse_constant": dec(bclock),
            "collapse_decimal": "Tc=0.914681356501962... R0 sqrt(rho/Pi)",
            "terminal_puiseux": "R=C (Tc-t)^(2/5)*(1+O((Tc-t)^(6/5))), C=R0^(3/5)*(5a/2)^(2/5)",
            "velocity_singularity": "R_dot=-(2/5)C (Tc-t)^(-3/5)*(1+O((Tc-t)^(6/5)))",
            "acceleration_singularity": "R_ddot=-(6/25)C (Tc-t)^(-8/5)*(1+O((Tc-t)^(6/5)))",
            "sign_atlas": "Pi=0 is stationary; Pi<0 is global monotone expansion with R(t)~sqrt(2|Pi|/(3rho))*t; Pi>0 collapses at Tc",
            "energy_ledger": "K_liquid=2*pi*rho*R^3 R_dot^2=(4*pi/3)Pi(R0^3-R^3), U=(4*pi/3)Pi R^3, E=K+U=(4*pi/3)Pi R0^3",
            "volume_law": "V=(4*pi/3)R^3~(4*pi/3)C^3(Tc-t)^(6/5), V_dot=O((Tc-t)^(1/5))",
            "lp_thresholds": "near Tc, R_dot in L^p iff p<5/3 and R_ddot in L^p iff p<5/8",
            "lagrangian": "Euler-Lagrange equation of L_phys=2*pi*rho R^3 R_dot^2-(4*pi/3)Pi R^3 on R>0",
            "boundary": "R0=0 is not a positive-radius classical initial state; any absorbing R=0 extension is explicitly external to the ODE",
            "analytic_boundary": "inverse incomplete-Beta representation is source-local explicit solvability only; the source Beta clock is not target continuation/divisor/counting law and is not an A3 analytic-structure match",
        },
        "regression": {
            "cases": rows,
            "case_count": len(rows),
            "collapse_x": [frac_text(x) for x in COLLAPSE_X],
            "expansion_x": [frac_text(x) for x in EXPANSION_X],
            "working_decimal_digits": 90,
            "serialized_significant_digits": 54,
        },
        "exact_identities": [
            {"name": "energy_first_integral", "formula": "d/dt[R^3 R_dot^2+(2 Pi/(3 rho))R^3]=0"},
            {"name": "beta_substitution", "formula": "int_0^1 x^(3/2)/sqrt(1-x^3) dx=(1/3)B(5/6,1/2)"},
            {"name": "terminal_balance", "formula": "delta_t=(R0/a)*(2/5)*(R/R0)^(5/2)*(1+5/22*(R/R0)^3+...)"},
            {"name": "volume_energy", "formula": "2 pi rho R^3 R_dot^2+(4 pi/3)Pi R^3=(4 pi/3)Pi R0^3"},
            {"name": "lagrangian_euler_lagrange", "formula": "EL[L_phys]=4 pi rho R^2 [R R_ddot+(3/2)R_dot^2+Pi/rho]"},
            {"name": "lp_integrability", "formula": "int_0^epsilon delta^(-3p/5) ddelta finite iff p<5/3; int delta^(-8p/5) finite iff p<5/8"},
        ],
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "strongest_positive": "exact source-native nonlinear terminal singularity and sign/energy geometry",
            "strongest_failure": "a monotone finite-time collapse trajectory has no primitive periodic-orbit owner or arithmetic clock",
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
            {"key": "Rayleigh1917", "claim": "original spherical-cavity collapse equation and pressure calculation", "title": "VIII. On the pressure developed in a liquid during the collapse of a spherical cavity", "authors": "Lord Rayleigh", "venue": "The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science", "year": 1917, "doi": "10.1080/14786440808635681"},
            {"key": "PlessetProsperetti1977", "claim": "source-locked bubble-dynamics and cavitation context", "title": "Bubble Dynamics and Cavitation", "authors": "M. S. Plesset and A. Prosperetti", "venue": "Annual Review of Fluid Mechanics", "year": 1977, "doi": "10.1146/annurev.fl.09.010177.001045"},
            {"key": "BrennerHilgenfeldtLohse2002", "claim": "terminal 2/5 singularity and physical correction context", "title": "Single-bubble sonoluminescence", "authors": "M. P. Brenner, S. Hilgenfeldt, and D. Lohse", "venue": "Reviews of Modern Physics", "year": 2002, "doi": "10.1103/RevModPhys.74.425"},
            {"key": "ObreschkowBrudererFarhat2012", "claim": "dimensionless Rayleigh profile, collapse clock and endpoint approximation context", "title": "Analytical approximations for the collapse of an empty spherical bubble", "authors": "D. Obreschkow, M. Bruderer, and M. Farhat", "venue": "Physical Review E", "year": 2012, "doi": "10.1103/PhysRevE.85.066303"},
        ],
        "nonclaims": [
            "the inverse incomplete-Beta function is not presented as an elementary closed form",
            "the finite ledger is a deterministic regression certificate and does not replace the quantified proof",
            "no continuation through R=0 is asserted for the physical ODE",
            "the source Beta clock is not target continuation/divisor/counting law and does not satisfy A3",
            "no target prime/zero law, Euler factor, root number, automorphy, functional equation, or Hilbert-Polya operator",
            "the negative-pressure branch is a mathematical sign control, not a claim about the original cavitation experiment",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path(os.environ.get("C219_OUTPUT", DEFAULT_OUTPUT)))
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(build(), sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(f"C219 producer: wrote {args.output}")


if __name__ == "__main__":
    main()
