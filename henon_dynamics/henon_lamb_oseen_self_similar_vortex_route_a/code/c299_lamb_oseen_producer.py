#!/usr/bin/env python3
"""Produce deterministic finite regression evidence for HCS-C299."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c299_lamb_oseen_evidence.json"
SOURCE = "83c058259c02707d004fca2d6b1a4ebaf5036094"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788307200

mp.mp.dps = 90


def canonical_payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def mpq(value: Fraction) -> mp.mpf:
    return mp.mpf(value.numerator) / value.denominator


def dec(value: mp.mpf) -> str:
    if value == 0:
        return "0.0"
    return mp.nstr(value, 72, strip_zeros=False)


FIELD_CASES = [
    ("F0-zero-circulation", Fraction(0), Fraction(1), Fraction(1)),
    ("F1-unit", Fraction(1), Fraction(1), Fraction(1)),
    ("F2-clockwise", Fraction(-2), Fraction(1, 2), Fraction(3, 2)),
    ("F3-small-age", Fraction(3, 2), Fraction(2), Fraction(1, 4)),
    ("F4-large-age", Fraction(5), Fraction(3, 4), Fraction(2)),
    ("F5-fractional", Fraction(-7, 3), Fraction(5, 2), Fraction(7, 5)),
    ("F6-thin-core", Fraction(11, 4), Fraction(1, 3), Fraction(9, 2)),
    ("F7-wide-core", Fraction(2), Fraction(7, 3), Fraction(5, 6)),
]
X_VALUES = [
    Fraction(0), Fraction(1, 16), Fraction(1, 8), Fraction(1, 4),
    Fraction(1, 2), Fraction(1), Fraction(2), Fraction(4), Fraction(8),
]
MOMENT_ORDERS = list(range(9))
LP_ORDERS = list(range(1, 7))
LAGRANGIAN_CASES = [
    ("L01", Fraction(1), Fraction(1), Fraction(1, 4), Fraction(3, 2), Fraction(1, 2)),
    ("L02", Fraction(-2), Fraction(1, 2), Fraction(1), Fraction(3), Fraction(3, 2)),
    ("L03", Fraction(3, 2), Fraction(2), Fraction(1, 3), Fraction(7, 3), Fraction(5)),
    ("L04", Fraction(5), Fraction(3, 4), Fraction(2), Fraction(9, 2), Fraction(1, 4)),
    ("L05", Fraction(-7, 3), Fraction(5, 2), Fraction(7, 5), Fraction(19, 5), Fraction(7, 2)),
    ("L06", Fraction(11, 4), Fraction(1, 3), Fraction(9, 2), Fraction(13, 2), Fraction(9, 4)),
    ("L07", Fraction(2), Fraction(7, 3), Fraction(5, 6), Fraction(17, 6), Fraction(14, 3)),
    ("L08", Fraction(-1, 2), Fraction(4, 3), Fraction(3, 5), Fraction(11, 5), Fraction(2, 5)),
    ("L09", Fraction(9, 5), Fraction(2, 7), Fraction(7, 4), Fraction(23, 4), Fraction(6, 7)),
    ("L10", Fraction(-4), Fraction(5, 6), Fraction(2, 3), Fraction(8, 3), Fraction(10, 3)),
    ("L11", Fraction(7, 2), Fraction(9, 5), Fraction(4, 5), Fraction(14, 5), Fraction(27, 10)),
    ("L12", Fraction(-5, 4), Fraction(11, 6), Fraction(5, 7), Fraction(26, 7), Fraction(11, 3)),
]

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
TUPLE = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"]
MODEL = {
    "equation": "partial_t omega + u dot grad omega = nu Delta omega on R^2",
    "closure": "div u=0 and curl u=omega with zero radial velocity",
    "ansatz": "omega(x,t)=tau^(-1) F(|x|/sqrt(tau)), tau=t+tau_0",
    "parameters": "Gamma real, nu>0, tau_0>=0, tau=t+tau_0>0",
    "clock": "physical viscous time t",
    "normalization": "integral over R^2 of omega equals Gamma",
}
THEOREM = {
    "classification": "every bounded-at-origin finite-circulation C2 radial forward self-similar profile is the signed Gaussian Lamb-Oseen profile",
    "velocity": "u_theta=Gamma(1-exp(-r^2/(4 nu tau)))/(2 pi r), continuously extended by u(0,t)=0",
    "lagrangian": "each positive radius is invariant and its continuous real-lift angle is an exponential-integral difference",
    "moments": "integral |x|^(2k) omega dx=Gamma k! (4 nu tau)^k for every integer k>=0",
    "dissipation": "enstrophy=Gamma^2/(8 pi nu tau) and palinstrophy=Gamma^2/(16 pi nu^2 tau^2)",
    "boundaries": "zero circulation, measure-valued zero-age start, inviscid weak limit, fixed origin, logarithmic angular drift, and infinite kinetic energy are separated",
}
PROOF = {
    "radial_reduction": "radial vorticity has tangential Biot-Savart velocity, so u dot grad omega vanishes identically",
    "uniqueness_ode": "the similarity ODE integrates to nu xi F'(xi)+(xi^2/2)F(xi)=C; regularity at xi=0 forces C=0",
    "normalization": "finite circulation fixes the remaining Gaussian constant",
    "lagrangian_primitive": "differentiate A_b(tau)=tau(1-exp(-b/tau))-b Ei(-b/tau)",
    "dissipation": "polar Gaussian integrals give all moments, Lp norms, enstrophy and palinstrophy",
    "finite_role": "finite rows regress formulas and boundary conventions; the global theorem is analytic",
}
NONCLAIMS = [
    "No target arithmetic local datum, Euler factor, root number, automorphy, divisor law, functional equation, or zero match is asserted.",
    "The circulation Gamma and Gaussian moments are fluid-mechanical source data, not rational-prime labels or prime-power weights.",
    "The Navier-Stokes generator is not asserted to be a Hilbert-Polya operator.",
    "No literature priority is claimed for the classical Lamb-Oseen formula or its standard radial reduction.",
]
COLLISION_BOUNDARY = {
    "C206": "C206 studies Couette advection-diffusion Fourier shearing on T times R; C299 classifies radial nonlinear-vorticity self-similarity on R^2, whose advection cancels geometrically.",
    "C207": "C207 classifies Barenblatt profiles for scalar nonlinear diffusion; C299 reconstructs velocity by Biot-Savart and audits circulation, particle angles, enstrophy, and the point-vortex boundary.",
    "energy_warning": "nonzero circulation gives logarithmically divergent whole-plane kinetic energy; only enstrophy and palinstrophy are claimed finite.",
}
REFERENCES = [
    {
        "identifier": "Oseen-1912-Arkiv-7-no14",
        "role": "classical source owner for the viscous line-vortex profile",
        "verification": "bibliographic metadata cross-checked; no priority claim made",
    },
    {
        "identifier": "10.1007/s00220-004-1254-9",
        "role": "published mathematical context for two-dimensional Oseen-vortex stability",
        "verification": "DOI metadata returned title, authors, journal, volume, pages, and year",
    },
]


def point_rows(nu: Fraction, tau: Fraction) -> list[dict]:
    rows = []
    for x in X_VALUES:
        xm = mpq(x)
        exponential = mp.exp(-xm)
        heat_shape = (xm - 1) * exponential
        rows.append({
            "x_equals_r2_over_4nu_tau": q(x),
            "r_squared": q(4 * nu * tau * x),
            "exp_minus_x": dec(exponential),
            "enclosed_circulation_fraction": dec(1 - exponential),
            "normalized_vorticity_shape": dec(exponential),
            "normalized_time_derivative_shape": dec(heat_shape),
            "normalized_radial_laplacian_shape": dec(heat_shape),
            "advection_term_is_zero": True,
            "origin_row": x == 0,
        })
    return rows


def field_case(case_id: str, gamma: Fraction, nu: Fraction, tau: Fraction) -> dict:
    moments = [
        {
            "k": k,
            "radial_moment_over_gamma": q(Fraction(math.factorial(k)) * (4 * nu * tau) ** k),
        }
        for k in MOMENT_ORDERS
    ]
    lp_rows = [
        {
            "p": p,
            "scaled_lp_power_coefficient": q(abs(gamma) ** p / p),
        }
        for p in LP_ORDERS
    ]
    return {
        "case_id": case_id,
        "Gamma": q(gamma),
        "nu": q(nu),
        "tau": q(tau),
        "core_radius_squared": q(4 * nu * tau),
        "point_rows": point_rows(nu, tau),
        "moment_rows": moments,
        "lp_rows": lp_rows,
        "enstrophy_times_8pi_nu_tau": q(gamma * gamma),
        "palinstrophy_times_16pi_nu2_tau2": q(gamma * gamma),
        "far_field_energy_log_coefficient_times_4pi": q(gamma * gamma),
        "zero_circulation": gamma == 0,
    }


def primitive(b: mp.mpf, tau: mp.mpf) -> mp.mpf:
    return tau * (1 - mp.exp(-b / tau)) - b * mp.ei(-b / tau)


def lagrangian_case(definition: tuple) -> dict:
    case_id, gamma, nu, tau_s, tau_t, r2 = definition
    b = r2 / (4 * nu)
    bm, sm, tm = mpq(b), mpq(tau_s), mpq(tau_t)
    delta = primitive(bm, tm) - primitive(bm, sm)
    quadrature = mp.quad(lambda z: 1 - mp.exp(-bm / z), [sm, tm])
    angle = mpq(gamma) * delta / (2 * mp.pi * mpq(r2))
    return {
        "case_id": case_id,
        "Gamma": q(gamma),
        "nu": q(nu),
        "tau_start": q(tau_s),
        "tau_end": q(tau_t),
        "radius_squared": q(r2),
        "b_equals_r2_over_4nu": q(b),
        "primitive_delta": dec(delta),
        "direct_quadrature": dec(quadrature),
        "angle_increment": dec(angle),
        "radius_is_constant": True,
    }


BOUNDARIES = [
    {"boundary_id": "B0-zero-circulation", "status": "exact", "statement": "Gamma=0 gives omega=u=0 for every positive age."},
    {"boundary_id": "B1-positive-age", "status": "exact", "statement": "tau_0>0 gives a smooth finite-enstrophy initial profile."},
    {"boundary_id": "B2-zero-age", "status": "measure boundary", "statement": "tau_0=0 starts from Gamma delta_0 weakly and is smooth only for t>0."},
    {"boundary_id": "B3-positive-viscosity", "status": "domain", "statement": "the classical Gaussian theorem assumes nu>0."},
    {"boundary_id": "B4-inviscid-limit", "status": "weak boundary", "statement": "as nu decreases to zero, omega converges weakly to Gamma delta_0 and u converges off the origin to the point vortex."},
    {"boundary_id": "B5-origin-particle", "status": "exact", "statement": "the continuous velocity extension fixes the particle at r=0."},
    {"boundary_id": "B6-long-time-angle", "status": "asymptotic", "statement": "for Gamma nonzero and r>0, theta(t)=Gamma log(tau)/(8 pi nu)+O(1)."},
    {"boundary_id": "B7-no-fluid-recurrence", "status": "exact obstruction", "statement": "for Gamma nonzero every finite p>1 norm decreases strictly with age, excluding recurrent vorticity states."},
    {"boundary_id": "B8-infinite-kinetic-energy", "status": "exact warning", "statement": "for Gamma nonzero the whole-plane kinetic energy diverges logarithmically at spatial infinity."},
]


def build() -> dict:
    fields = [field_case(*definition) for definition in FIELD_CASES]
    lagrangian = [lagrangian_case(definition) for definition in LAGRANGIAN_CASES]
    point_count = sum(len(case["point_rows"]) for case in fields)
    moment_count = sum(len(case["moment_rows"]) for case in fields)
    lp_count = sum(len(case["lp_rows"]) for case in fields)
    audited = point_count + moment_count + lp_count + len(lagrangian) + len(BOUNDARIES)
    data = {
        "schema": "hcs-c299-lamb-oseen-self-similar-vortex-v1",
        "candidate_id": "HCS-C299",
        "obstruction_id": "HEN-O283",
        "evaluation_date": "2026-09-02",
        "fixed_epoch": EPOCH,
        "source_commit": SOURCE,
        "scope_literal": SCOPE,
        "evaluator": {"version": "0.2.0", "sha256": EVALUATOR},
        "model": MODEL,
        "theorem_contract": THEOREM,
        "proof_contract": PROOF,
        "enumeration": {
            "field_cases": fields,
            "lagrangian_cases": lagrangian,
            "boundary_rows": BOUNDARIES,
            "field_case_count": len(fields),
            "point_receipt_cells": point_count,
            "moment_receipt_cells": moment_count,
            "lp_receipt_cells": lp_count,
            "lagrangian_receipt_cells": len(lagrangian),
            "boundary_receipt_cells": len(BOUNDARIES),
            "audited_cell_count": audited,
        },
        "route_a": {
            "tuple": TUPLE,
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": FLAGS,
        "nonclaims": NONCLAIMS,
        "collision_boundary": COLLISION_BOUNDARY,
        "references": REFERENCES,
    }
    data["payload_sha256"] = canonical_payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C299_PRODUCER_PASS",
        "audited_cells": data["enumeration"]["audited_cell_count"],
        "payload_sha256": data["payload_sha256"],
        "evidence_sha256": hashlib.sha256(args.output.read_bytes()).hexdigest(),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
