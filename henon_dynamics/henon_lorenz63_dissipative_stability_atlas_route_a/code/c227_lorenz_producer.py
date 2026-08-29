#!/usr/bin/env python3
"""Produce the deterministic HCS-C227 Lorenz-63 theorem certificate.

The certificate is source-local: it records a global absorbing ellipsoid,
the complete equilibrium and linear-stability atlas for sigma,beta>0, and
the sigma=0/beta=0 boundary families.  It never reads arithmetic targets.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
import os
from pathlib import Path

SOURCE_COMMIT = "489672bd36abd3a4f6da92d1446a0af575917959"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c227_lorenz_evidence.json"

MAIN_CASES = [
    ("classic_origin", Fraction(10), Fraction(8, 3), Fraction(0)),
    ("classic_pitchfork", Fraction(10), Fraction(8, 3), Fraction(1)),
    ("classic_stable_wings", Fraction(10), Fraction(8, 3), Fraction(20)),
    ("classic_hopf_surface", Fraction(10), Fraction(8, 3), Fraction(470, 19)),
    ("classic_post_hopf", Fraction(10), Fraction(8, 3), Fraction(28)),
    ("no_finite_hopf", Fraction(2), Fraction(3), Fraction(100)),
    ("negative_rho", Fraction(3), Fraction(1), Fraction(-4)),
    ("simple_pre_hopf", Fraction(4), Fraction(1), Fraction(10)),
    ("simple_hopf", Fraction(4), Fraction(1), Fraction(16)),
    ("simple_post_hopf", Fraction(4), Fraction(1), Fraction(20)),
]

DISSIPATION_SAMPLES = [
    (Fraction(10), Fraction(8, 3), Fraction(28), Fraction(1), Fraction(2), Fraction(3)),
    (Fraction(2), Fraction(3), Fraction(100), Fraction(-4), Fraction(5), Fraction(7)),
    (Fraction(3), Fraction(1), Fraction(-4), Fraction(2), Fraction(-3), Fraction(5)),
    (Fraction(4), Fraction(1), Fraction(16), Fraction(-7, 3), Fraction(11, 4), Fraction(-5, 2)),
    (Fraction(1, 5), Fraction(7, 4), Fraction(3, 2), Fraction(9, 5), Fraction(-2, 7), Fraction(8, 3)),
]


def ftext(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def main_row(case_id: str, sigma: Fraction, beta: Fraction, rho: Fraction) -> dict:
    assert sigma > 0 and beta > 0
    c = sigma + rho
    kappa = min(2 * sigma, Fraction(2), beta)
    absorber_floor = beta * c * c / kappa
    origin_poly = [Fraction(1), sigma + 1, sigma * (1 - rho)]
    origin_stability = "asymptotically_stable" if rho < 1 else (
        "nonhyperbolic_zero_eigenvalue" if rho == 1 else "saddle_unstable"
    )
    exists = rho > 1
    rho_h = None
    wing_stability = "not_present"
    wing_poly = None
    hurwitz_margin = None
    hopf_frequency_squared = None
    if exists:
        wing_poly = [
            Fraction(1), sigma + beta + 1, beta * (sigma + rho), 2 * sigma * beta * (rho - 1)
        ]
        hurwitz_margin = sigma * (sigma + beta + 3) + (beta + 1 - sigma) * rho
        if sigma <= beta + 1:
            wing_stability = "asymptotically_stable_all_rho_gt_1"
        else:
            rho_h = sigma * (sigma + beta + 3) / (sigma - beta - 1)
            if rho < rho_h:
                wing_stability = "asymptotically_stable"
            elif rho == rho_h:
                wing_stability = "linear_hopf_boundary"
                hopf_frequency_squared = beta * (sigma + rho_h)
            else:
                wing_stability = "linearly_unstable"
    return {
        "case_id": case_id,
        "sigma": ftext(sigma),
        "beta": ftext(beta),
        "rho": ftext(rho),
        "divergence": ftext(-(sigma + beta + 1)),
        "energy_center_c": ftext(c),
        "differential_inequality_kappa": ftext(kappa),
        "absorbing_floor_beta_c2_over_kappa": ftext(absorber_floor),
        "origin_quadratic_factor": [ftext(x) for x in origin_poly],
        "origin_stability": origin_stability,
        "wing_equilibria_exist": exists,
        "wing_amplitude_squared": ftext(beta * (rho - 1)) if exists else None,
        "wing_characteristic_polynomial": [ftext(x) for x in wing_poly] if wing_poly else None,
        "hurwitz_margin": ftext(hurwitz_margin) if hurwitz_margin is not None else None,
        "rho_h": ftext(rho_h) if rho_h is not None else None,
        "wing_stability": wing_stability,
        "hopf_frequency_squared": ftext(hopf_frequency_squared) if hopf_frequency_squared is not None else None,
    }


def dissipation_row(spec: tuple[Fraction, ...]) -> dict:
    sigma, beta, rho, x, y, z = spec
    c = sigma + rho
    xdot = sigma * (y - x)
    ydot = x * (rho - z) - y
    zdot = x * y - beta * z
    direct = 2 * x * xdot + 2 * y * ydot + 2 * (z - c) * zdot
    square_ledger = -2 * sigma * x * x - 2 * y * y - beta * z * z - beta * (z - c) ** 2 + beta * c * c
    return {
        "sigma": ftext(sigma), "beta": ftext(beta), "rho": ftext(rho),
        "point": [ftext(x), ftext(y), ftext(z)],
        "V": ftext(x * x + y * y + (z - c) ** 2),
        "Vdot_direct": ftext(direct),
        "Vdot_square_ledger": ftext(square_ledger),
    }


def build() -> dict:
    data = {
        "schema": "hcs-c227-lorenz63-atlas-v1",
        "candidate_id": "HCS-C227",
        "evaluation_date": "2026-08-29",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "evaluator": {
            "path": "flow_systems/skills/route-a-evaluator.md",
            "version": "0.2.0",
            "sha256": EVALUATOR_SHA256,
        },
        "headline": "For every sigma,beta>0, Lorenz-63 has an explicit absorbing ellipsoid and a complete equilibrium and linear-stability atlas, including the exact Hopf surface and all zero-rate boundary families.",
        "frozen_object": {
            "system": "x_dot=sigma(y-x), y_dot=x(rho-z)-y, z_dot=xy-beta z",
            "main_parameter_domain": "sigma>0, beta>0, rho in R",
            "clock": "physical continuous time t",
            "symmetry": "(x,y,z)->(-x,-y,z)",
            "lyapunov_function": "V=x^2+y^2+(z-rho-sigma)^2",
            "boundary_domains": "sigma=0 and/or beta=0 are separate non-dissipative controls",
            "forbidden_data": "target primes/zeros, arithmetic local data, Euler factors, root numbers, automorphy, target functional equations, Hilbert-Polya operators",
        },
        "theorem": {
            "exact_dissipation_ledger": "V_dot=-2 sigma x^2-2 y^2-beta z^2-beta(z-c)^2+beta c^2, c=rho+sigma",
            "absorbing_inequality": "V_dot<=-kappa V+beta c^2, kappa=min(2 sigma,2,beta)",
            "global_consequence": "V(t)<=exp(-kappa t)V(0)+(beta c^2/kappa)(1-exp(-kappa t)); every level R>beta c^2/kappa absorbs all trajectories and solutions are global forward",
            "divergence": "div f=-(sigma+beta+1)",
            "equilibria": "O=(0,0,0); for rho>1, E_pm=(+/-sqrt(beta(rho-1)),+/-sqrt(beta(rho-1)),rho-1)",
            "origin_polynomial": "chi_O=(ell+beta)(ell^2+(sigma+1)ell+sigma(1-rho))",
            "wing_polynomial": "chi_E=ell^3+(sigma+beta+1)ell^2+beta(sigma+rho)ell+2 sigma beta(rho-1)",
            "hopf_surface": "if sigma>beta+1, rho_H=sigma(sigma+beta+3)/(sigma-beta-1); at rho_H the roots are -(sigma+beta+1) and +/-i sqrt(beta(sigma+rho_H))",
            "stability_atlas": "O is stable for rho<1, nonhyperbolic at rho=1, and a saddle for rho>1; E_pm are stable for all rho>1 if sigma<=beta+1, otherwise stable below rho_H, on the linear Hopf boundary at rho_H, and unstable above",
            "sigma_zero_boundary": "for beta>0, E_s=(s,beta rho s/(beta+s^2),rho s^2/(beta+s^2)); transverse polynomial ell^2+(1+beta)ell+(beta+s^2)",
            "beta_zero_boundary": "for sigma>0, E_z=(0,0,z0); transverse polynomial ell^2+(sigma+1)ell+sigma(1-rho+z0)",
            "double_zero_boundary": "for sigma=beta=0 the equilibrium set is {(0,0,z)} union {(x,0,rho)}",
            "bifurcation_scope": "rho=1 is the equilibrium-merger nonhyperbolic boundary; only the linear Hopf locus is claimed, not nonlinear criticality or a global chaos classification",
        },
        "regression": {
            "main_rows": [main_row(*row) for row in MAIN_CASES],
            "main_row_count": len(MAIN_CASES),
            "dissipation_rows": [dissipation_row(row) for row in DISSIPATION_SAMPLES],
            "dissipation_row_count": len(DISSIPATION_SAMPLES),
            "degenerate_rows": [
                {"boundary": "sigma=0,beta>0", "samples": ["s=-2,beta=2,rho=3", "s=0,beta=2,rho=3", "s=3,beta=2,rho=3"]},
                {"boundary": "beta=0,sigma>0", "samples": ["z0=0,sigma=5,rho=4:saddle", "z0=3:sigma=5,rho=4:nonhyperbolic", "z0=5:sigma=5,rho=4:transversely_stable"]},
                {"boundary": "sigma=beta=0", "samples": ["origin_line", "rho_line", "intersection=(0,0,rho)"]},
            ],
        },
        "exact_identities": [
            {"name": "cross_term_cancellation", "formula": "for c=rho+sigma, all xy and xyz terms cancel in V_dot"},
            {"name": "square_ledger", "formula": "-2 beta z(z-c)=-beta z^2-beta(z-c)^2+beta c^2"},
            {"name": "hurwitz_margin", "formula": "(sigma+beta+1)(sigma+rho)-2sigma(rho-1)=sigma(sigma+beta+3)+(beta+1-sigma)rho"},
            {"name": "hopf_factorization", "formula": "chi_E at rho_H=(ell+sigma+beta+1)(ell^2+beta(sigma+rho_H))"},
            {"name": "sigma_zero_tangent", "formula": "chi_sigma0=ell[ell^2+(1+beta)ell+beta+s^2]"},
            {"name": "beta_zero_tangent", "formula": "chi_beta0=ell[ell^2+(sigma+1)ell+sigma(1-rho+z0)]"},
        ],
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "strongest_positive": "a source-native global absorbing set and exact all-parameter equilibrium stability atlas",
            "strongest_failure": "no complete primitive periodic-orbit owner, arithmetic clock, determinant bridge, target analytic structure, or natural unitary lift is constructed",
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
            {"id": "Lorenz1963", "doi": "10.1175/1520-0469(1963)020<0130:DNF>2.0.CO;2", "role": "original three-mode system and classical qualitative analysis"},
            {"id": "PadeRauhTsarouhas1986", "doi": "10.1016/0375-9601(86)90031-9", "role": "nonlinear Hopf direction background, which this certificate does not claim"},
            {"id": "Tucker2002", "doi": "10.1007/s002080010018", "role": "rigorous classical-parameter Lorenz-attractor context, not an all-parameter input"},
            {"id": "GuckenheimerWilliams1979", "doi": "10.1007/BF02684769", "role": "geometric Lorenz background, not used in the proof"},
        ],
        "nonclaims": [
            "The atlas does not classify every invariant set or assert chaos for every rho above rho_H.",
            "The linear imaginary-axis crossing is not promoted to a nonlinear Hopf criticality theorem.",
            "The divergence identity alone is not used as a proof of an absorbing set.",
            "The zero-rate boundary families are not silently included in the sigma,beta>0 dissipativity theorem.",
            "No target arithmetic, Euler product, functional equation, Hilbert-Polya operator, or Route-B input is claimed.",
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
    print(json.dumps({"status": "C227_PRODUCER_PASS", "rows": len(MAIN_CASES),
                      "payload_sha256": data["payload_sha256"],
                      "evidence_sha256": sha256(raw.encode()).hexdigest()}, sort_keys=True))


if __name__ == "__main__":
    main()
