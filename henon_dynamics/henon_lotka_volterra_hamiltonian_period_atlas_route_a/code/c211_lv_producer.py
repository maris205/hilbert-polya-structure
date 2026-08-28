#!/usr/bin/env python3
"""Produce the deterministic C211 Lotka--Volterra period/action certificate."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
import os
from pathlib import Path

import mpmath as mp

SOURCE_COMMIT = "e8054522273dbd545f9d406978e5d4648c627918"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c211_lv_evidence.json"
WORKING_DPS = 45
SERIALIZED_DIGITS = 34

PARAMETERS = [
    ("unit", F(1), F(1), F(1), F(1)),
    ("fast_center", F(2), F(1), F(3), F(2)),
    ("slow_center", F(1, 2), F(3), F(2, 1), F(5, 2)),
    ("mixed_scale", F(3, 2), F(2, 3), F(5, 4), F(7, 3)),
    ("large_rates", F(5), F(4, 3), F(7, 2), F(9, 5)),
    ("small_rates", F(2, 5), F(7, 4), F(3, 5), F(11, 6)),
]
ENERGIES = [F(1, 20), F(1, 5), F(1, 2), F(1)]


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def level_hash(level: dict) -> str:
    body = dict(level)
    body.pop("level_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def mpq(q: F) -> mp.mpf:
    return mp.mpf(q.numerator) / q.denominator


def decimal(value: mp.mpf) -> str:
    value = mp.re(value)
    if abs(value) < mp.mpf("1e-42"):
        return "0.0"
    return mp.nstr(value, SERIALIZED_DIGITS, strip_zeros=False, min_fixed=-SERIALIZED_DIGITS, max_fixed=SERIALIZED_DIGITS)


def convex_potential(s: mp.mpf) -> mp.mpf:
    return mp.expm1(s) - s


def inverse_branches(residual: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
    if residual < 0:
        residual = mp.mpf("0")
    argument = -mp.exp(-1 - residual)
    lower = -mp.lambertw(argument, 0) - 1 - residual
    upper = -mp.lambertw(argument, -1) - 1 - residual
    return mp.re(lower), mp.re(upper)


def quadratures(a: mp.mpf, c: mp.mpf, h: mp.mpf) -> tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf]:
    """Return (u_minus,u_plus,area,period) using an endpoint-cancelling angle."""
    u_minus, u_plus = inverse_branches(h / c)
    midpoint = (u_minus + u_plus) / 2
    halfwidth = (u_plus - u_minus) / 2

    def values(theta: mp.mpf, mode: str) -> mp.mpf:
        cosine = mp.cos(theta)
        # The Jacobian cancels the integrable square-root endpoint singularity.
        if abs(cosine) < mp.mpf("1e-30"):
            return mp.mpf("0")
        u = midpoint + halfwidth * mp.sin(theta)
        residual = (h - c * convex_potential(u)) / a
        if residual < 0:
            residual = mp.mpf("0")
        lower, upper = inverse_branches(residual)
        jacobian = halfwidth * cosine
        if mode == "area":
            return (upper - lower) * jacobian
        time_density = (1 / (1 - mp.exp(lower)) + 1 / (mp.exp(upper) - 1)) / a
        return time_density * jacobian

    area = mp.re(mp.quad(lambda theta: values(theta, "area"), [-mp.pi / 2, 0, mp.pi / 2]))
    period = mp.re(mp.quad(lambda theta: values(theta, "period"), [-mp.pi / 2, 0, mp.pi / 2]))
    return u_minus, u_plus, area, period


def build() -> dict:
    mp.mp.dps = WORKING_DPS
    parameter_rows = []
    all_levels = 0
    for case_id, a_q, b_q, c_q, d_q in PARAMETERS:
        a, b, c, d = map(mpq, (a_q, b_q, c_q, d_q))
        center_x, center_y = c / d, a / b
        center_period = 2 * mp.pi / mp.sqrt(a * c)
        levels = []
        for h_q in ENERGIES:
            h = mpq(h_q)
            um, up, area, period = quadratures(a, c, h)
            action = area / (2 * mp.pi)
            # These residuals are recomputed by the checker; they are diagnostics,
            # not extra hypotheses.
            residual_minus = convex_potential(um) - h / c
            residual_plus = convex_potential(up) - h / c
            level = {
                "h": str(h_q),
                "u_minus": decimal(um),
                "u_plus": decimal(up),
                "area": decimal(area),
                "period": decimal(period),
                "action": decimal(action),
                "period_over_center_limit": decimal(period / center_period),
                "branch_residual_minus": decimal(residual_minus),
                "branch_residual_plus": decimal(residual_plus),
            }
            level["level_sha256"] = level_hash(level)
            levels.append(level)
            all_levels += 1
        parameter_rows.append({
            "case_id": case_id,
            "a": str(a_q), "b": str(b_q), "c": str(c_q), "d": str(d_q),
            "center_x": decimal(center_x), "center_y": decimal(center_y),
            "center_period_limit": decimal(center_period),
            "levels": levels,
        })

    data = {
        "schema": "hcs-c211-lotka-volterra-v1",
        "candidate_id": "HCS-C211",
        "evaluation_date": "2026-08-28",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "evaluator": {
            "path": "flow_systems/skills/route-a-evaluator.md",
            "version": "0.2.0",
            "sha256": EVALUATOR_SHA256,
        },
        "headline": (
            "Positive Lotka--Volterra flow has a global strictly convex Hamiltonian "
            "period annulus with exact Lambert-W period, area, action, and cycle-average identities"
        ),
        "frozen_object": {
            "system": "x'=x(a-b*y), y'=y(-c+d*x) on x>0,y>0",
            "parameters": "a,b,c,d>0",
            "log_coordinates": "u=log(x/(c/d)), v=log(y/(a/b))",
            "clock": "physical continuous time t",
            "hamiltonian": "H(u,v)=c*(exp(u)-u-1)+a*(exp(v)-v-1)",
            "normalization": "geometric action J(h)=Area({H<=h})/(2*pi)",
            "boundary_convention": "axes and zero-rate cases are separate boundary models; h=0 is the center",
            "forbidden_data": "target primes, target zeros, local arithmetic, Euler factors, root numbers, automorphy, target functional equations",
        },
        "theorem": {
            "log_flow": "u'=a*(1-exp(v)), v'=c*(exp(u)-1)",
            "strict_convexity": "Hessian diag(c*exp(u),a*exp(v)) is positive definite and H is proper",
            "period_annulus": "each h>0 level is one smooth compact periodic oval",
            "inverse_branches": "ell(r)=-W_0(-exp(-1-r))-1-r; upp(r)=-W_{-1}(-exp(-1-r))-1-r",
            "area_quadrature": "Area(h)=integral_{u_-}^{u_+}(upp(r(u))-ell(r(u))) du",
            "period_quadrature": "T(h)=a^{-1} integral [1/(1-exp(ell(r(u))))+1/(exp(upp(r(u)))-1)] du",
            "action_coarea": "J(h)=Area(h)/(2*pi) and J'(h)=T(h)/(2*pi)",
            "center_limit": "lim_{h down 0} T(h)=2*pi/sqrt(a*c)",
            "cycle_averages": "<exp(u)>=<exp(v)>=1, hence <x>=c/d and <y>=a/b",
            "boundary_ledger": "positive axes are invariant and have no positive-quadrant oval; zero rates are outside the strict theorem",
            "explicit_nonclaims": "period monotonicity and high-energy asymptotics are not asserted",
        },
        "regression": {
            "parameter_cases": parameter_rows,
            "parameter_case_count": len(parameter_rows),
            "energy_levels_per_case": len(ENERGIES),
            "quadrature_level_count": all_levels,
            "working_decimal_digits": WORKING_DPS,
            "serialized_significant_digits": SERIALIZED_DIGITS,
        },
        "exact_identities": [
            {
                "case_id": case_id,
                "hamiltonian_time_derivative": "(-H_v)*H_u + H_u*H_v = 0",
                "hessian_determinant": "a*c*exp(u+v)>0",
                "linearization_characteristic": "lambda^2+a*c=0",
                "average_u_identity": "integral_0^T u' dt = a*(T-integral_0^T exp(v)dt)=0",
                "average_v_identity": "integral_0^T v' dt = c*(integral_0^T exp(u)dt-T)=0",
            }
            for case_id, *_ in PARAMETERS
        ],
        "route_a": {
            "tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "strongest_positive": "A global source-native Hamiltonian period annulus and exact quadrature/action identities are proved.",
            "strongest_failure": "The real-energy cycle continuum has no arithmetic primitive owner, target determinant, or same-clock self-adjoint lift.",
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
            {
                "key": "Waldvogel1983",
                "claim": "period analysis for the Volterra--Lotka model",
                "title": "The Period in the Volterra--Lotka Predator-Prey Model",
                "authors": "J. Waldvogel",
                "venue": "SIAM Journal on Numerical Analysis",
                "year": 1983,
                "doi": "10.1137/0720098",
            },
            {
                "key": "Waldvogel1986",
                "claim": "historical monotonicity context (not used as a theorem here)",
                "title": "The period in the Volterra-Lotka system is monotonic",
                "authors": "J. Waldvogel",
                "venue": "Journal of Mathematical Analysis and Applications",
                "year": 1986,
                "doi": "10.1016/0022-247X(86)90076-4",
            },
            {
                "key": "Hsu1983",
                "claim": "periodic-solution period context",
                "title": "A Remark on the Period of the Periodic Solution in the Lotka-Volterra System",
                "authors": "S.-B. Hsu",
                "venue": "Journal of Mathematical Analysis and Applications",
                "year": 1983,
                "doi": "10.1016/0022-247X(83)90117-8",
            },
        ],
        "nonclaims": [
            "period monotonicity or any unproved high-energy asymptotic",
            "priority or literature exhaustiveness",
            "target prime-orbit law, local arithmetic datum, Euler factor, root number, automorphy, target functional equation, or Hilbert--Polya operator",
            "a discrete primitive owner for the continuum of positive real energies",
            "external peer review, novelty certification, or an acceptance score",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path(os.environ.get("C211_OUTPUT", DEFAULT_OUTPUT)))
    args = parser.parse_args()
    result = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C211_PRODUCER_PASS",
        "parameter_cases": result["regression"]["parameter_case_count"],
        "quadrature_levels": result["regression"]["quadrature_level_count"],
        "payload_sha256": result["payload_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
