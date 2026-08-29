#!/usr/bin/env python3
"""Produce the deterministic HCS-C231 Allen--Cahn front certificate.

The certificate is deliberately source-local: it records exact formulas for
the equal-well Allen--Cahn front and its one-dimensional Pöschl--Teller
linearization.  Decimal probes are only regression receipts; the theorem
strings carry the analytic boundary of what is claimed.
"""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import argparse
import json
import math
import os
from pathlib import Path

import mpmath as mp

SOURCE_COMMIT = "e1dc522e054c2d0ded74b017bc52c7b016a52c59"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c231_allen_cahn_evidence.json"
mp.mp.dps = 90

EPS_PROBES = [Fraction(1, 4), Fraction(1, 2), Fraction(1), Fraction(2), Fraction(4)]
SPEED_PROBES = [Fraction(-2), Fraction(-1), Fraction(0), Fraction(1), Fraction(2)]
Y_PROBES = [Fraction(-2), Fraction(-1), Fraction(0), Fraction(1), Fraction(2)]


def ftext(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def mpq(value: Fraction) -> mp.mpf:
    return mp.mpf(value.numerator) / value.denominator


def dec(value: mp.mpf | int | Fraction, digits: int = 64) -> str:
    x = mp.mpf(value)
    if abs(x) < mp.mpf("1e-82"):
        return "0.0"
    return mp.nstr(x, digits, strip_zeros=False, min_fixed=-70, max_fixed=70)


def sech(y: mp.mpf) -> mp.mpf:
    return 1 / mp.cosh(y)


def epsilon_rows() -> list[dict]:
    rows: list[dict] = []
    for eps_q in EPS_PROBES:
        eps = mpq(eps_q)
        rows.append({
            "epsilon": ftext(eps_q),
            "front_width_sqrt2epsilon": dec(mp.sqrt(2) * eps),
            "surface_energy": dec(2 * mp.sqrt(2) / (3 * eps)),
            "integral_front_gradient_square": dec(2 * mp.sqrt(2) / (3 * eps)),
            "translation_eigenvalue": "0.0",
            "shape_eigenvalue": dec(-3 / (2 * eps**2)),
            "essential_edge": dec(-2 / eps**2),
            "spectral_gap_to_edge": dec(1 / (2 * eps**2)),
        })
    return rows


def speed_rows() -> list[dict]:
    rows: list[dict] = []
    eps = mp.mpf(1)
    integral = 2 * mp.sqrt(2) / (3 * eps)
    for c_q in SPEED_PROBES:
        rows.append({
            "speed_c": ftext(c_q),
            "well_energy_jump": "0.0",
            "front_gradient_integral": dec(integral),
            "selection_product_c_times_integral": dec(mpq(c_q) * integral),
            "admissible_equal_well_heteroclinic": c_q == 0,
        })
    return rows


def profile_rows() -> list[dict]:
    rows: list[dict] = []
    for y_q in Y_PROBES:
        y = mpq(y_q)
        t = mp.tanh(y)
        s = sech(y)
        # M = d_y^2 - 4 + 6 sech(y)^2 is the scaled linearization.
        # The residuals are represented symbolically as exact zeros; the
        # independent checker differentiates the closed forms numerically.
        rows.append({
            "y": ftext(y_q),
            "front_U": dec(t),
            "front_prime_scaled": dec(s**2),
            "kernel_mode": dec(s**2),
            "shape_mode": dec(s * t),
            "front_first_integral_residual": "0.0",
            "scaled_kernel_residual": "0.0",
            "scaled_shape_residual": "0.0",
            "factorization_quadratic_form_nonnegative": True,
        })
    return rows


def energy_rows() -> list[dict]:
    rows: list[dict] = []
    for y_q in Y_PROBES:
        y = mpq(y_q)
        s = sech(y)
        t = mp.tanh(y)
        # W(t)=1/4(1-t^2)^2 and 1/2 (dU/dxi)^2 = epsilon^-2 W.
        W = (1 - t**2) ** 2 / 4
        grad_scaled = s**4 / 4  # 1/2*(dU/dy)^2 for U=tanh(y)
        rows.append({
            "y": ftext(y_q),
            "potential_W": dec(W),
            "half_scaled_gradient_square": dec(grad_scaled),
            "equipartition_residual": dec(grad_scaled - W),
            "dissipation_density_symbol": "u_t^2",
        })
    return rows


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def build() -> dict:
    data = {
        "schema": "hcs-c231-allen-cahn-front-pt-spectrum-v1",
        "candidate_id": "HCS-C231",
        "evaluation_date": "2026-08-29",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "evaluator": {
            "path": "flow_systems/skills/route-a-evaluator.md",
            "version": "0.2.0",
            "sha256": EVALUATOR_SHA256,
        },
        "headline": "The equal-well Allen--Cahn gradient flow has a unique translated tanh heteroclinic, selected speed c=0, an exact energy dissipation law, and a Pöschl--Teller linearization with translation kernel and essential edge.",
        "frozen_object": {
            "equation": "u_t=u_xx+u-u^3",
            "epsilon_equation": "u_t=u_xx+epsilon^(-2)(u-u^3), epsilon>0",
            "potential": "W(u)=(1-u^2)^2/4",
            "gradient_flow_energy": "E_epsilon[u]=integral_R (u_x^2/2+epsilon^(-2)W(u)) dx",
            "traveling_ansatz": "u(x,t)=U(x-c t), U(-infinity)=-1, U(+infinity)=+1",
            "front_formula": "U_epsilon(xi)=tanh(xi/(sqrt(2) epsilon))",
            "clock": "physical PDE time t; no primitive periodic orbit clock",
            "primitive_periodic_orbit": False,
            "forbidden_data": "target primes/zeros and target zero table, arithmetic local data, Euler factors, root numbers, automorphy, target divisors, Hilbert-Polya operators",
        },
        "theorem": {
            "front_and_speed": "Every C2 monotone equal-well heteroclinic of U''+c U'+epsilon^(-2)(U-U^3)=0 is U_epsilon(xi-xi0) with c=0; the reverse orientation is -U_epsilon.",
            "first_integral": "For c=0, (U')^2/2=epsilon^(-2)W(U), with limits U(-infinity)=-1 and U(+infinity)=1.",
            "speed_selection": "Multiplication by U' gives c integral_R (U')^2 dxi = W(-1)/epsilon^2-W(1)/epsilon^2=0; a nonconstant front therefore has c=0.",
            "energy_dissipation": "For smooth finite-relative-energy solutions, dE_epsilon/dt=-integral_R u_t^2 dx <=0.",
            "surface_energy": "E_epsilon[U_epsilon]=integral_R (U_epsilon')^2 dxi=2 sqrt(2)/(3 epsilon).",
            "translation_uniqueness": "The first-order separable equation U'=sqrt(2 W(U))/epsilon has one increasing solution modulo xi-translation; the zero crossing fixes the translate.",
            "linearization": "L_epsilon=partial_xi^2+epsilon^(-2)(1-3 U_epsilon^2)=(2 epsilon^2)^(-1)(d_y^2-4+6 sech^2 y), y=xi/(sqrt(2)epsilon).",
            "factorization": "-d_y^2+4-6 sech^2 y=B^*B=(-d_y+2 tanh y)(d_y+2 tanh y).",
            "discrete_spectrum": "spec_disc(L_epsilon)={0,-3/(2 epsilon^2)}; kernel is span{U_epsilon'}, and the second mode is sech(y)tanh(y).",
            "essential_spectrum": "spec_ess(L_epsilon)=(-infinity,-2/epsilon^2].",
            "degenerate_boundaries": "epsilon downarrow 0 sharp-interface width collapse and diverging spectral scales; epsilon to infinity reaction/edge/gap collapse; zero reaction or zero diffusivity removes the smooth heteroclinic ODE; c nonzero is excluded by equal-well balance.",
            "scope": "This is a one-dimensional front and linear spectral theorem; no primitive periodic-orbit repetition law, target divisor, or operator realization is asserted.",
        },
        "regression": {
            "epsilon_rows": epsilon_rows(),
            "speed_rows": speed_rows(),
            "profile_rows": profile_rows(),
            "energy_rows": energy_rows(),
            "row_counts": {"epsilon": len(EPS_PROBES), "speed": len(SPEED_PROBES), "profile": len(Y_PROBES), "energy": len(Y_PROBES)},
            "working_decimal_digits": 90,
            "serialized_significant_digits": 64,
        },
        "exact_identities": [
            {"name": "equal_well_energy", "formula": "W(-1)=W(1)=0"},
            {"name": "tanh_ode", "formula": "U=tanh(xi/(sqrt(2)epsilon)) solves U''+epsilon^(-2)(U-U^3)=0"},
            {"name": "equipartition", "formula": "U'^2/2=epsilon^(-2)W(U)"},
            {"name": "speed_selection", "formula": "c integral U'^2=0, hence c=0"},
            {"name": "gradient_flow", "formula": "dE_epsilon/dt=-integral u_t^2"},
            {"name": "surface_tension", "formula": "integral U'^2 dxi=2sqrt(2)/(3epsilon)"},
            {"name": "pt_factorization", "formula": "-d_y^2+4-6sech^2 y=B^*B, B=d_y+2tanh y"},
            {"name": "pt_modes", "formula": "M sech^2 y=0 and M(sech y tanh y)=-3(sech y tanh y)"},
            {"name": "essential_edge", "formula": "V(y) tends to -4 for M, so sigma_ess(L)=(-infinity,-2/epsilon^2]"},
        ],
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "strongest_positive": "an exact gradient-flow front, speed-selection identity, and closed Pöschl--Teller spectral atlas",
            "strongest_failure": "the heteroclinic is not a primitive periodic-orbit owner and supplies no arithmetic divisor or cross-period repetition law",
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
            {"id": "AllenCahn1979", "title": "A microscopic theory for antiphase boundary motion and its application to antiphase domain coarsening", "authors": "S. M. Allen and J. W. Cahn", "venue": "Acta Metallurgica 27(6), 1085--1095", "year": 1979, "doi": "10.1016/0001-6160(79)90196-2", "role": "phase-field origin and equal-well interface context"},
            {"id": "FifeMcLeod1977", "title": "The approach of solutions of nonlinear diffusion equations to travelling front solutions", "authors": "P. C. Fife and J. B. McLeod", "venue": "Archive for Rational Mechanics and Analysis 65(4), 335--361", "year": 1977, "doi": "10.1007/BF00250432", "role": "travelling-front existence and convergence context"},
        ],
        "nonclaims": [
            "The tanh front and Pöschl--Teller spectrum are classical formulas, not claimed as new discoveries.",
            "The energy identity is stated for smooth finite-relative-energy solutions; no global attractor theorem is inferred.",
            "The equal-well model has no nonzero-speed heteroclinic; no tilted-potential speed law is silently substituted.",
            "Essential-spectrum and two-mode statements are one-dimensional; no multidimensional transverse stability or nonlinear orbital-stability rate is claimed.",
            "No primitive periodic orbit, target zero table, target arithmetic, Euler product, functional equation, Hilbert-Polya operator, or Route-B input is claimed.",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    output = parser.parse_args().output
    data = build()
    output.parent.mkdir(parents=True, exist_ok=True)
    raw = json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    tmp = output.with_name(output.name + ".tmp")
    tmp.write_text(raw)
    os.replace(tmp, output)
    print(json.dumps({"status": "C231_PRODUCER_PASS", "payload_sha256": data["payload_sha256"], "evidence_sha256": sha256(raw.encode()).hexdigest(), "epsilon_rows": len(EPS_PROBES), "speed_rows": len(SPEED_PROBES), "profile_rows": len(Y_PROBES)}, sort_keys=True))


if __name__ == "__main__":
    main()
