#!/usr/bin/env python3
"""Deterministic evidence producer for HCS-C278."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "results/c278_camassa_holm_evidence.json"
SOURCE = "418bcec5afb1f9e5905cc6e2ba7f9e099fef2e02"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH = 1788220800
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
mp.mp.dps = 90


def dec(x: mp.mpf) -> str:
    return mp.nstr(x, 70)


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def same_sign_row(P0: int, D0: int, t0: str) -> dict:
    P, D, t = mp.mpf(P0), mp.mpf(D0), mp.mpf(t0)
    a = D * t / 2
    A = P * P / (D * D) - 1
    y = 1 + A * mp.cosh(a) ** 2
    p = D * mp.tanh(a)
    gap = mp.log(y)
    p1, p2 = (P - p) / 2, (P + p) / 2
    energy = p1 * p1 + p2 * p2 + 2 * p1 * p2 / y
    ydot = A * D * mp.cosh(a) * mp.sinh(a)
    qdot = ydot / y
    pdot = D * D * mp.sech(a) ** 2 / 2
    ode_pdot = 2 * p1 * p2 / y
    centre = P * t + 2 * mp.sign(P) * mp.atanh((D / abs(P)) * mp.tanh(a))
    return {
        "P": P0,
        "D": D0,
        "t": t0,
        "y": dec(y),
        "gap": dec(gap),
        "p": dec(p),
        "p1": dec(p1),
        "p2": dec(p2),
        "energy": dec(energy),
        "centre": dec(centre),
        "q1": dec((centre - gap) / 2),
        "q2": dec((centre + gap) / 2),
        "gap_ode_residual": dec(qdot - p * (1 - 1 / y)),
        "p_ode_residual": dec(pdot - ode_pdot),
        "D2_reconstruction_residual": dec(2 * energy - P * P - D * D),
    }


def opposite_sign_row(P0: int, D0: int, s0: str) -> dict:
    P, D, s = mp.mpf(P0), mp.mpf(D0), mp.mpf(s0)
    a = D * s / 2
    B = 1 - P * P / (D * D)
    y = 1 + B * mp.sinh(a) ** 2
    p = -D * mp.coth(a)
    gap = mp.log(y)
    p1, p2 = (P - p) / 2, (P + p) / 2
    energy = p1 * p1 + p2 * p2 + 2 * p1 * p2 / y
    ydot = -B * D * mp.sinh(a) * mp.cosh(a)
    qdot = ydot / y
    pdot = -D * D * mp.csch(a) ** 2 / 2
    ode_pdot = 2 * p1 * p2 / y
    collision_coefficient = (D * D - P * P) / 4
    return {
        "P": P0,
        "D": D0,
        "time_to_collision": s0,
        "y": dec(y),
        "gap": dec(gap),
        "p": dec(p),
        "p1": dec(p1),
        "p2": dec(p2),
        "energy": dec(energy),
        "gap_ode_residual": dec(qdot - p * (1 - 1 / y)),
        "p_ode_residual": dec(pdot - ode_pdot),
        "D2_reconstruction_residual": dec(2 * energy - P * P - D * D),
        "gap_quadratic_coefficient": dec(collision_coefficient),
        "scaled_gap": dec(gap / (s * s)),
        "scaled_amplitude_difference": dec(p * s),
    }


def alpha_row(P0: int, D0: int, numerator: int, denominator: int) -> dict:
    P, D = mp.mpf(P0), mp.mpf(D0)
    alpha = mp.mpf(numerator) / denominator
    energy_minus = (P * P + D * D) / 2
    energy_plus = (1 - alpha) * energy_minus + alpha * P * P
    dplus2 = 2 * energy_plus - P * P
    return {
        "P": P0,
        "D_minus": D0,
        "alpha": f"{numerator}/{denominator}",
        "energy_minus": dec(energy_minus),
        "energy_plus": dec(energy_plus),
        "D_plus_squared": dec(dplus2),
        "energy_loss": dec(energy_minus - energy_plus),
        "postcollision_state": "single_peak" if numerator == denominator else "signed_pair",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    same_rows = [
        same_sign_row(P, D, t)
        for P, D in ((3, 1), (5, 3), (-4, 2))
        for t in ("-3", "-1", "0", "1", "3")
    ]
    opposite_rows = [
        opposite_sign_row(P, D, s)
        for P, D in ((1, 3), (0, 2), (-1, 4))
        for s in ("3", "1", "0.25", "0.0625")
    ]
    alpha_rows = [
        alpha_row(P, D, a, 4)
        for P, D in ((1, 3), (0, 2), (-1, 4))
        for a in range(5)
    ]
    data = {
        "schema": "hcs-c278-camassa-holm-two-peakon-v1",
        "candidate_id": "HCS-C278",
        "evaluation_date": "2026-09-01",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {"version": "0.2.0", "sha256": EVALUATOR},
        "model": {
            "equation": "m_t+u m_x+2 u_x m=0, m=u-u_xx",
            "ansatz": "u=sum_{j=1}^2 p_j exp(-|x-q_j|), q_1<q_2",
            "distribution_identity": "(1-partial_x^2)exp(-|x-q|)=2 delta_q",
            "clock": "physical Camassa-Holm time before collision; declared alpha-extension after collision",
            "invariants": "P=p_1+p_2 and E=p_1^2+p_2^2+2p_1p_2 exp(-(q_2-q_1))",
        },
        "theorem_contract": {
            "peakon_ode": "qdot_i=sum_j p_j exp(-|q_i-q_j|); pdot_i=p_i sum_j p_j sgn(q_i-q_j) exp(-|q_i-q_j|)",
            "reduction": "y=exp(q_2-q_1), p=p_2-p_1, D^2=2E-P^2 imply ydot^2=D^2(y-1)(y-P^2/D^2)",
            "chamber_partition": "for q>0, P^2-D^2=4p_1p_2(1-exp(-q)); p_1p_2!=0 gives exactly one strict chamber, while p_1p_2=0 is the degenerate single-peak or zero-field boundary",
            "same_sign": "P^2>D^2 gives a global cosh branch, positive gap, momentum exchange, and explicit scattering coordinates",
            "opposite_sign": "D^2>P^2 gives a finite collision with q~(D^2-P^2)(t_c-t)^2/4 and p~-2/(t_c-t)",
            "collision_limit": "the centre converges at finite collision time and u converges uniformly to the single peak P exp(-|x-q_c|), while E-P^2 is concentrated collision energy",
            "alpha_extension": "E_plus=(1-alpha)E_minus+alpha P^2; alpha=0 conservative reflection, alpha=1 sticky single peak",
            "boundaries": "single peak, P=0, zero field, and coincident extended collision state are explicit",
        },
        "proof_contract": {
            "classification": "PROVABLE AS STATED for p_1p_2!=0 inside the two strict ordered chambers, with p_1p_2=0 recorded separately as a degenerate boundary",
            "weak_reduction": "match delta and delta-prime coefficients in the momentum equation",
            "integrability": "two invariants reduce the flow to one separable quadratic equation in y",
            "profile_limit": "with c=(q_1+q_2)/2 and h=(q_2-q_1)/2, finite-time convergence of c and the kernel Lipschitz bound give ||u-P exp(-|.-c|)||_infinity <= (|P|+|p|)h -> 0",
            "global_scope": "no assertion of uniqueness for arbitrary H1 initial data or arbitrary weak continuations",
            "finite_evidence_role": "regression and normalization control only; analytic identities carry the theorem",
        },
        "regression": {
            "same_sign_rows": same_rows,
            "opposite_sign_rows": opposite_rows,
            "alpha_rows": alpha_rows,
            "boundaries": [
                {"name": "single_peak", "law": "u=p exp(-|x-q_0-pt|), E=P^2=p^2"},
                {"name": "zero_total_momentum", "law": "P=0 remains in the signed collision chamber when E>0"},
                {"name": "zero_field", "law": "P=E=0 gives u=0"},
                {"name": "coincident_pair", "law": "q=0 is an extended collision state, not an ordered pre-collision chart point"},
            ],
            "counts": {
                "same_sign_rows": len(same_rows),
                "opposite_sign_rows": len(opposite_rows),
                "alpha_rows": len(alpha_rows),
                "boundary_rows": 4,
            },
        },
        "references": [
            {
                "id": "CamassaHolm1993",
                "title": "An integrable shallow water equation with peaked solitons",
                "authors": "Roberto Camassa and Darryl D. Holm",
                "venue": "Physical Review Letters 71(11) (1993), 1661-1664",
                "doi": "10.1103/PhysRevLett.71.1661",
                "url": "https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.71.1661",
            },
            {
                "id": "GrunertHolden2016",
                "title": "The general peakon-antipeakon solution for the Camassa-Holm equation",
                "authors": "Katrin Grunert and Helge Holden",
                "venue": "Journal of Hyperbolic Differential Equations 13 (2016), 353-380",
                "doi": "10.1142/S0219891616500119",
                "url": "https://arxiv.org/abs/1502.07686",
            },
        ],
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": {
            "arithmetic_local_data": False,
            "euler_factors": False,
            "root_numbers": False,
            "automorphy": False,
            "target_divisor_or_counting_law": False,
            "target_functional_equation": False,
            "target_zero_match": False,
            "hilbert_polya_operator": False,
            "route_b_input": False,
        },
        "nonclaims": [
            "The alpha-extension is a declared two-peakon collision convention, not a theorem of uniqueness for all weak solutions.",
            "The finite regression rows do not prove the distributional PDE reduction or arbitrary-parameter theorem.",
            "The CH Lax/integrable context is not a target spectral operator or arithmetic determinant.",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "C278_PRODUCER_PASS", "payload_sha256": data["payload_sha256"], "rows": len(same_rows) + len(opposite_rows) + len(alpha_rows)}, sort_keys=True))


if __name__ == "__main__":
    main()
