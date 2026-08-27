#!/usr/bin/env python3
"""Produce the exact/high-precision C198 SIR phase-portrait certificate."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import mpmath as mp


SOURCE_COMMIT = "c3a5b9bbb3b6d0881f395abe4a01accd322f69cb"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
DEFAULT_OUTPUT = Path(__file__).resolve().parents[1] / "results/c198_sir_evidence.json"
X0S = [F(1, 4), F(1, 2), F(3, 4), F(1), F(5, 4), F(3, 2), F(2), F(3)]
Y0S = [F(1, 10), F(1, 4), F(1, 2)]
PHYSICAL = [(F(2), F(1)), (F(3), F(2)), (F(5), F(3)), (F(7), F(5))]


def m(value: F) -> mp.mpf:
    return mp.mpf(value.numerator) / value.denominator


def fmt(value: mp.mpf) -> str:
    return mp.nstr(value, 82, strip_zeros=False)


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def initial_regime(x0: F) -> str:
    if x0 > 1:
        return "interior_peak_after_initial_growth"
    if x0 == 1:
        return "threshold_tangent_then_decay"
    return "monotone_decay_from_initial_time"


def build() -> dict:
    mp.mp.dps = 110
    cases = []
    for x0q in X0S:
        for y0q in Y0S:
            x0, y0 = m(x0q), m(y0q)
            constant = x0 + y0
            argument = -x0 * mp.e ** (-constant)
            final_x = -mp.lambertw(argument, 0).real
            companion_x = -mp.lambertw(argument, -1).real
            final_residual = final_x - mp.log(final_x) - (constant - mp.log(x0))
            if x0q > 1:
                peak_x = mp.mpf(1)
                peak_y = y0 + x0 - 1 - mp.log(x0)
            else:
                peak_x = x0
                peak_y = y0
            sensitivity = final_x / (final_x - 1)
            assert 0 < final_x < min(x0, mp.mpf(1))
            assert companion_x > max(x0, mp.mpf(1))
            assert abs(final_residual) < mp.mpf("1e-100")
            cases.append({
                "case_id": f"x{x0q}_y{y0q}",
                "x0": str(x0q),
                "y0": str(y0q),
                "invariant": "x+y-log(x)",
                "invariant_rational_part": str(x0q + y0q),
                "invariant_log_argument": str(x0q),
                "initial_regime": initial_regime(x0q),
                "lambert_argument": fmt(argument),
                "final_x_W0": fmt(final_x),
                "companion_x_Wminus1": fmt(companion_x),
                "absolute_final_equation_residual": fmt(abs(final_residual)),
                "peak_x": fmt(peak_x),
                "peak_y": fmt(peak_y),
                "d_final_x_d_y0": fmt(sensitivity),
                "final_below_x0_and_one": True,
                "companion_above_x0_and_one": True,
            })

    physical_rows = []
    for beta, gamma in PHYSICAL:
        physical_rows.append({
            "beta": str(beta),
            "gamma": str(gamma),
            "susceptible_threshold_kappa": str(gamma / beta),
            "dimensionless_time_tau_per_t": str(gamma),
            "dimensionless_state_scale": str(beta / gamma),
        })

    data = {
        "schema": "hcs-c198-sir-v1",
        "candidate_id": "HCS-C198",
        "evaluation_date": "2026-08-27",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "evaluator": {
            "path": "flow_systems/skills/route-a-evaluator.md",
            "version": "0.2.0",
            "sha256": EVALUATOR_SHA256,
        },
        "headline": (
            "Every positive-parameter closed SIR trajectory has one exact "
            "dimensionless phase curve, a complete peak and final-size atlas, "
            "and monotone convergence to the disease-free equilibrium line"
        ),
        "frozen_object": {
            "physical_system": "Sdot=-beta*S*I, Idot=beta*S*I-gamma*I, Rdot=gamma*I",
            "parameters": "beta>0, gamma>0, S0>0, I0>=0, R0>=0",
            "clock": "physical time t",
            "dimensionless_variables": "x=S/(gamma/beta), y=I/(gamma/beta), tau=gamma*t",
            "dimensionless_system": "x'=-xy, y'=y(x-1)",
            "normalization": "closed population S+I+R=N; mass-action beta*S*I",
            "allowed_data": "exact rational dimensionless initial conditions",
            "forbidden_data": "clinical observations, fitted outbreaks, prime tables, target zeros",
        },
        "theorem": {
            "first_integral": "x+y-log(x)",
            "phase_curve": "y=y0+x0-x+log(x/x0)",
            "peak": "if x0>1 then x_peak=1 and y_peak=y0+x0-1-log(x0); otherwise y decreases from t=0",
            "final_size": "for y0>0, x_infinity=-W_0(-x0*exp(-x0-y0)); for y0=0 the trajectory is the initial equilibrium",
            "companion_branch": "-W_-1 is the upper intersection of the invariant curve and is not the forward limit",
            "time_quadrature": "tau=-integral dx/[x*(y0+x0-x+log(x/x0))]",
            "sensitivity": "for y0>0, partial x_infinity/partial y0=x_infinity/(x_infinity-1)<0",
            "limit": "I tends to zero and every non-equilibrium orbit converges to the disease-free equilibrium line",
            "no_recurrence": "R is strictly increasing whenever I>0",
            "equilibrium_transverse_eigenvalue": "gamma*(S_star/(gamma/beta)-1)",
        },
        "regression": {
            "cases": cases,
            "physical_scalings": physical_rows,
        },
        "summary": {
            "case_count": len(cases),
            "subcritical_x_count": sum(x < 1 for x in X0S) * len(Y0S),
            "threshold_x_count": sum(x == 1 for x in X0S) * len(Y0S),
            "supercritical_x_count": sum(x > 1 for x in X0S) * len(Y0S),
            "physical_scaling_count": len(physical_rows),
            "lambert_branch_values": 2 * len(cases),
            "precision_decimal_digits": 100,
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "strongest_positive": "The nonlinear flow has a global phase-curve integral and exact final-size branch.",
            "strongest_failure": "Strict monotonicity removes nonconstant recurrence and the biological parameters carry no intrinsic prime arithmetic.",
        },
        "scope_flags": {
            "uses_clinical_or_personal_data": False,
            "gives_medical_advice": False,
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
                "key": "KermackMcKendrick1927",
                "claim": "classical epidemic model, threshold and final-size ancestry",
                "doi": "10.1098/rspa.1927.0118",
            },
            {
                "key": "Pakes2015",
                "claim": "Lambert-W final-size branch analysis",
                "doi": "10.1093/imamat/hxu057",
            },
        ],
        "nonclaims": [
            "priority for the Kermack--McKendrick SIR model, threshold, invariant, or final-size relation",
            "prediction, calibration, intervention advice, or applicability to any real outbreak",
            "an elementary explicit formula for S,I,R as functions of physical time",
            "a rational-prime orbit law, target determinant, Hilbert--Polya operator, or Route-B authorization",
            "global literature priority, external peer review, or an acceptance score",
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
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C198_PRODUCER_PASS",
        "cases": data["summary"]["case_count"],
        "branch_values": data["summary"]["lambert_branch_values"],
        "payload_sha256": data["payload_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
