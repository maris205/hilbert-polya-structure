#!/usr/bin/env python3
"""Produce the deterministic C199 signed-a Chaplygin-sleigh certificate."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import mpmath as mp


SOURCE_COMMIT = "d1e58971e570b855488009af384995702ddb887b"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
DEFAULT_OUTPUT = Path(__file__).resolve().parents[1] / "results/c199_chaplygin_evidence.json"
PARAMETERS = [
    (F(1), F(1), F(1), F(1)),
    (F(2), F(3), F(-1), F(5)),
    (F(3), F(2), F(2), F(7)),
    (F(5), F(7), F(-2), F(11)),
    (F(7), F(5), F(1, 2), F(13)),
    (F(11), F(13), F(-3, 2), F(17)),
]
QS = [F(1, 2), F(1), F(2)]


def mpq(q: F) -> mp.mpf:
    return mp.mpf(q.numerator) / q.denominator


def fmt(x: mp.mpf) -> str:
    return mp.nstr(x, 82, strip_zeros=False)


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def build() -> dict:
    mp.mp.dps = 110
    theta0 = F(1, 7)
    cases = []
    for family, (m_q, j_q, a_q, h_q) in enumerate(PARAMETERS, 1):
        m, j, a, h = map(mpq, (m_q, j_q, a_q, h_q))
        ic = j + m*a*a
        radius = mp.sqrt(2*h/m)
        rate = m*abs(a)*radius/ic
        eta = mp.sqrt(ic/m)/abs(a)
        for sigma in (-1, 1):
            samples = []
            for q_q in QS:
                q = mpq(q_q)
                tanh_s = (q*q-1)/(q*q+1)
                sech_s = 2*q/(q*q+1)
                time = mp.log(q)/rate
                u = mp.sign(a)*radius*tanh_s
                omega = sigma*radius*mp.sqrt(m/ic)*sech_s
                theta = mpq(theta0) + sigma*eta*mp.asin(tanh_s)
                energy = m*u*u/2 + ic*omega*omega/2
                du = a*omega*omega
                domega = -(m*a/ic)*u*omega
                samples.append({
                    "q": str(q_q),
                    "time": fmt(time),
                    "tanh_s_exact": str((q_q*q_q-F(1))/(q_q*q_q+F(1))),
                    "sech_s_exact": str(2*q_q/(q_q*q_q+F(1))),
                    "u": fmt(u),
                    "omega": fmt(omega),
                    "theta": fmt(theta),
                    "energy": fmt(energy),
                    "du_dt": fmt(du),
                    "domega_dt": fmt(domega),
                })
            cases.append({
                "case_id": f"family_{family}_sigma_{sigma:+d}",
                "parameters": {"m": str(m_q), "J": str(j_q), "a": str(a_q), "H": str(h_q)},
                "sigma": sigma,
                "theta0": str(theta0),
                "derived": {
                    "I_c": str(j_q+m_q*a_q*a_q),
                    "R": fmt(radius),
                    "A": fmt(rate),
                    "eta": fmt(eta),
                    "u_minus": fmt(-mp.sign(a)*radius),
                    "u_plus": fmt(mp.sign(a)*radius),
                    "omega_endpoint": "0",
                    "blade_angle_deflection": fmt(sigma*mp.pi*eta),
                    "stable_endpoint": "u_plus",
                    "transverse_eigenvalue_at_u_plus": fmt(-(m*a/ic)*(mp.sign(a)*radius)),
                },
                "samples": samples,
            })

    boundary = [
        {"case_id": "a0_omega_pos", "m": "2", "J": "3", "a": "0", "u": "5/2", "omega": "3/2", "class": "periodic_SE2_circle", "period": fmt(2*mp.pi/mpq(F(3, 2)))},
        {"case_id": "a0_omega_neg", "m": "5", "J": "7", "a": "0", "u": "-4/3", "omega": "-2", "class": "periodic_SE2_circle", "period": fmt(mp.pi)},
        {"case_id": "a0_omega_zero_pos", "m": "3", "J": "2", "a": "0", "u": "7/3", "omega": "0", "class": "straight_line", "period": None},
        {"case_id": "a0_omega_zero_neg", "m": "7", "J": "5", "a": "0", "u": "-9/4", "omega": "0", "class": "straight_line", "period": None},
    ]
    data = {
        "schema": "hcs-c199-chaplygin-v1",
        "candidate_id": "HCS-C199",
        "evaluation_date": "2026-08-27",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "evaluator": {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256},
        "headline": "The signed-offset Chaplygin sleigh admits a complete all-parameter heteroclinic scattering and reconstruction theorem with singular measure and a sharp zero-offset recurrence boundary",
        "frozen_object": {
            "configuration": "contact point r in R^2 and blade angle theta on S^1",
            "parameters": "m>0, J>0, a in R; I_c=J+m*a^2",
            "body_velocities": "u along the blade and omega=theta_dot",
            "equations": "r_dot=u(cos theta,sin theta), theta_dot=omega, u_dot=a omega^2, omega_dot=-(ma/I_c)u omega",
            "energy": "H=m u^2/2+I_c omega^2/2",
            "convention_warning": "theta is blade angle, not velocity heading; negative u reverses velocity direction by pi",
        },
        "theorem": {
            "nonzero_offset_solution": "u=sgn(a)R tanh(A(t-t0)); omega=sigma R sqrt(m/I_c) sech(A(t-t0)); theta=theta0+sigma eta asin(tanh(A(t-t0)))",
            "constants": "R=sqrt(2H/m), A=m|a|R/I_c, eta=sqrt(I_c/m)/|a|",
            "scattering": "heteroclinic from u=-sgn(a)R to u=sgn(a)R; Delta theta=sigma*pi*eta independent of H",
            "reconstruction": "r(t)=r0+integral u(cos theta,sin theta)dt; after subtracting endpoint velocities it converges to two asymptotic affine lines",
            "stability": "on omega=0 the transverse eigenvalue is -(ma/I_c)u_*; exactly the half-axis a u_*>0 is transversely stable",
            "poisson": "on omega>0 or omega<0, {u,omega}=(a/I_c)omega and Hamiltonian H generates the reduced flow",
            "measure": "du domega/|omega| is invariant on each reduced half-plane and its Haar-configuration lift is an off-line full-flow measure; no positive C1 reduced or configuration-Haar-factor density crosses a nonzero reduced equilibrium",
            "reversor": "(r,theta,u,omega) maps to (r,theta,-u,-omega)",
            "zero_offset": "a=0 gives constant u,omega: omega nonzero is an SE(2)-periodic circle of period 2pi/|omega|; omega=0 is a straight line",
        },
        "regression": {"heteroclinic_cases": cases, "zero_offset_cases": boundary},
        "summary": {
            "parameter_families": len(PARAMETERS),
            "heteroclinic_cases": len(cases),
            "sample_states": len(cases)*len(QS),
            "positive_a_cases": sum(F(row["parameters"]["a"]) > 0 for row in cases),
            "negative_a_cases": sum(F(row["parameters"]["a"]) < 0 for row in cases),
            "zero_offset_cases": len(boundary),
            "precision_decimal_digits": 100,
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "strongest_positive": "The reduced nonholonomic flow has a source-native half-plane Poisson form and exact scattering data.",
            "strongest_failure": "No primitive-orbit prime carrier, target determinant, or same-clock Hilbert--Polya operator is supplied.",
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
            {"key": "Bloch2000", "claim": "Hamiltonization and classical Chaplygin-sleigh structure", "doi": "10.1016/S0167-2789(00)00046-4"},
            {"key": "BorisovMamaev2009", "claim": "Chaplygin-sleigh dynamics and nonholonomic mechanics", "doi": "10.1016/j.jappmathmech.2009.04.005"},
            {"key": "Moshchuk1987", "claim": "classical sleigh stability and motion", "doi": "10.1016/0021-8928(87)90079-7"},
            {"key": "BlochRojo2008", "claim": "quantum/nonholonomic comparison used only as an A4 boundary", "doi": "10.1103/PhysRevLett.101.030402"},
        ],
        "nonclaims": [
            "priority for the Chaplygin sleigh, its reduction, Hamiltonization, or asymptotic behavior",
            "that finite numerical regression proves the all-parameter theorem",
            "that blade orientation is always the velocity heading",
            "an exclusion of every configuration-dependent full-flow C1 density; the proved obstruction is for reduced and configuration-Haar-factor densities",
            "a prime-orbit law, Euler product, root number, automorphy, target determinant, or Hilbert--Polya operator",
            "external peer review, literature exhaustiveness, or an acceptance score",
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
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False)+"\n")
    print(json.dumps({"status": "C199_PRODUCER_PASS", "cases": data["summary"]["heteroclinic_cases"], "samples": data["summary"]["sample_states"], "payload_sha256": data["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
