#!/usr/bin/env python3
"""Producer-independent checker for HCS-C278."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = Path(os.environ.get(
    "C278_EVIDENCE_PATH", ROOT / "results/c278_camassa_holm_evidence.json"
))
SOURCE = "418bcec5afb1f9e5905cc6e2ba7f9e099fef2e02"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
mp.mp.dps = 90

TOP_LEVEL_KEYS = {
    "schema", "candidate_id", "evaluation_date", "source_commit", "fixed_epoch",
    "scope_literal", "evaluator", "model", "theorem_contract", "proof_contract",
    "regression", "references", "route_a", "scope_flags", "nonclaims",
    "payload_sha256",
}
THEOREM_CONTRACT = {
    "peakon_ode": "qdot_i=sum_j p_j exp(-|q_i-q_j|); pdot_i=p_i sum_j p_j sgn(q_i-q_j) exp(-|q_i-q_j|)",
    "reduction": "y=exp(q_2-q_1), p=p_2-p_1, D^2=2E-P^2 imply ydot^2=D^2(y-1)(y-P^2/D^2)",
    "chamber_partition": "for q>0, P^2-D^2=4p_1p_2(1-exp(-q)); p_1p_2!=0 gives exactly one strict chamber, while p_1p_2=0 is the degenerate single-peak or zero-field boundary",
    "same_sign": "P^2>D^2 gives a global cosh branch, positive gap, momentum exchange, and explicit scattering coordinates",
    "opposite_sign": "D^2>P^2 gives a finite collision with q~(D^2-P^2)(t_c-t)^2/4 and p~-2/(t_c-t)",
    "collision_limit": "the centre converges at finite collision time and u converges uniformly to the single peak P exp(-|x-q_c|), while E-P^2 is concentrated collision energy",
    "alpha_extension": "E_plus=(1-alpha)E_minus+alpha P^2; alpha=0 conservative reflection, alpha=1 sticky single peak",
    "boundaries": "single peak, P=0, zero field, and coincident extended collision state are explicit",
}
BOUNDARIES = [
    {"name": "single_peak", "law": "u=p exp(-|x-q_0-pt|), E=P^2=p^2"},
    {"name": "zero_total_momentum", "law": "P=0 remains in the signed collision chamber when E>0"},
    {"name": "zero_field", "law": "P=E=0 gives u=0"},
    {"name": "coincident_pair", "law": "q=0 is an extended collision state, not an ordered pre-collision chart point"},
]
NONCLAIMS = [
    "The alpha-extension is a declared two-peakon collision convention, not a theorem of uniqueness for all weak solutions.",
    "The finite regression rows do not prove the distributional PDE reduction or arbitrary-parameter theorem.",
    "The CH Lax/integrable context is not a target spectral operator or arithmetic determinant.",
]
MODEL = {
    "equation": "m_t+u m_x+2 u_x m=0, m=u-u_xx",
    "ansatz": "u=sum_{j=1}^2 p_j exp(-|x-q_j|), q_1<q_2",
    "distribution_identity": "(1-partial_x^2)exp(-|x-q|)=2 delta_q",
    "clock": "physical Camassa-Holm time before collision; declared alpha-extension after collision",
    "invariants": "P=p_1+p_2 and E=p_1^2+p_2^2+2p_1p_2 exp(-(q_2-q_1))",
}
PROOF_CONTRACT = {
    "classification": "PROVABLE AS STATED for p_1p_2!=0 inside the two strict ordered chambers, with p_1p_2=0 recorded separately as a degenerate boundary",
    "weak_reduction": "match delta and delta-prime coefficients in the momentum equation",
    "integrability": "two invariants reduce the flow to one separable quadratic equation in y",
    "profile_limit": "with c=(q_1+q_2)/2 and h=(q_2-q_1)/2, finite-time convergence of c and the kernel Lipschitz bound give ||u-P exp(-|.-c|)||_infinity <= (|P|+|p|)h -> 0",
    "global_scope": "no assertion of uniqueness for arbitrary H1 initial data or arbitrary weak continuations",
    "finite_evidence_role": "regression and normalization control only; analytic identities carry the theorem",
}
ROUTE_A = {
    "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
    "overall": "ROUTE_A_REJECTED",
    "route_b_invocation_allowed": False,
}
SCOPE_FLAGS = {
    "arithmetic_local_data": False,
    "euler_factors": False,
    "root_numbers": False,
    "automorphy": False,
    "target_divisor_or_counting_law": False,
    "target_functional_equation": False,
    "target_zero_match": False,
    "hilbert_polya_operator": False,
    "route_b_input": False,
}
REGRESSION_KEYS = {
    "same_sign_rows", "opposite_sign_rows", "alpha_rows", "boundaries", "counts",
}
SAME_SIGN_ROW_KEYS = {
    "P", "D", "t", "y", "gap", "p", "p1", "p2", "energy", "centre",
    "q1", "q2", "gap_ode_residual", "p_ode_residual",
    "D2_reconstruction_residual",
}
OPPOSITE_SIGN_ROW_KEYS = {
    "P", "D", "time_to_collision", "y", "gap", "p", "p1", "p2",
    "energy", "gap_ode_residual", "p_ode_residual",
    "D2_reconstruction_residual", "gap_quadratic_coefficient", "scaled_gap",
    "scaled_amplitude_difference",
}
ALPHA_ROW_KEYS = {
    "P", "D_minus", "alpha", "energy_minus", "energy_plus", "D_plus_squared",
    "energy_loss", "postcollision_state",
}
REFERENCES = [
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
]


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def close(a: str | mp.mpf, b: mp.mpf, tol: str = "1e-60") -> bool:
    return abs(mp.mpf(a) - b) < mp.mpf(tol)


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    checks = 0

    def ok(condition: bool) -> None:
        nonlocal checks
        assert condition
        checks += 1

    ok(set(data) == TOP_LEVEL_KEYS)
    ok(data["schema"] == "hcs-c278-camassa-holm-two-peakon-v1")
    ok(data["candidate_id"] == "HCS-C278")
    ok(data["evaluation_date"] == "2026-09-01")
    ok(data["source_commit"] == SOURCE)
    ok(data["evaluator"] == {"version": "0.2.0", "sha256": EVALUATOR})
    ok(data["evaluator"]["sha256"] == EVALUATOR)
    ok(data["model"] == MODEL)
    ok(data["fixed_epoch"] == 1788220800)
    ok(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER")
    ok(data["payload_sha256"] == payload_hash(data))
    ok(data["route_a"]["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"])
    ok(data["route_a"]["overall"] == "ROUTE_A_REJECTED")
    ok(data["route_a"]["route_b_invocation_allowed"] is False)
    ok(data["route_a"] == ROUTE_A)
    ok(all(value is False for value in data["scope_flags"].values()))
    ok(data["scope_flags"] == SCOPE_FLAGS)
    ok(data["theorem_contract"] == THEOREM_CONTRACT)
    ok(set(data["proof_contract"]) == {"classification", "weak_reduction", "integrability", "profile_limit", "global_scope", "finite_evidence_role"})
    ok(data["proof_contract"]["classification"] == "PROVABLE AS STATED for p_1p_2!=0 inside the two strict ordered chambers, with p_1p_2=0 recorded separately as a degenerate boundary")
    ok(data["proof_contract"]["profile_limit"] == "with c=(q_1+q_2)/2 and h=(q_2-q_1)/2, finite-time convergence of c and the kernel Lipschitz bound give ||u-P exp(-|.-c|)||_infinity <= (|P|+|p|)h -> 0")
    ok(data["proof_contract"] == PROOF_CONTRACT)
    ok(data["nonclaims"] == NONCLAIMS)
    ok(set(data["regression"]) == REGRESSION_KEYS)

    for row in data["regression"]["same_sign_rows"]:
        ok(set(row) == SAME_SIGN_ROW_KEYS)
        P, D, t = mp.mpf(row["P"]), mp.mpf(row["D"]), mp.mpf(row["t"])
        a = D * t / 2
        y = 1 + (P * P / (D * D) - 1) * mp.cosh(a) ** 2
        p = D * mp.tanh(a)
        p1, p2 = (P - p) / 2, (P + p) / 2
        E = p1 * p1 + p2 * p2 + 2 * p1 * p2 / y
        centre = P * t + 2 * mp.sign(P) * mp.atanh((D / abs(P)) * mp.tanh(a))
        ok(P * P > D * D)
        ok(close(row["y"], y))
        ok(close(row["gap"], mp.log(y)))
        ok(close(row["p"], p))
        ok(close(row["p1"], p1))
        ok(close(row["p2"], p2))
        ok(close(row["energy"], E))
        ok(close(row["centre"], centre))
        ok(close(row["q1"], (centre - mp.log(y)) / 2))
        ok(close(row["q2"], (centre + mp.log(y)) / 2))
        ok(close(row["D2_reconstruction_residual"], mp.mpf("0")))
        ok(abs(mp.mpf(row["gap_ode_residual"])) < mp.mpf("1e-60"))
        ok(abs(mp.mpf(row["p_ode_residual"])) < mp.mpf("1e-60"))
        ok(y >= P * P / (D * D))
        ok(p1 * p2 > 0)

    for row in data["regression"]["opposite_sign_rows"]:
        ok(set(row) == OPPOSITE_SIGN_ROW_KEYS)
        P, D, s = mp.mpf(row["P"]), mp.mpf(row["D"]), mp.mpf(row["time_to_collision"])
        a = D * s / 2
        y = 1 + (1 - P * P / (D * D)) * mp.sinh(a) ** 2
        p = -D * mp.coth(a)
        p1, p2 = (P - p) / 2, (P + p) / 2
        E = p1 * p1 + p2 * p2 + 2 * p1 * p2 / y
        ok(D * D > P * P)
        ok(close(row["y"], y))
        ok(close(row["gap"], mp.log(y)))
        ok(close(row["p"], p))
        ok(close(row["p1"], p1))
        ok(close(row["p2"], p2))
        ok(close(row["energy"], E))
        ok(close(row["D2_reconstruction_residual"], mp.mpf("0")))
        ok(abs(mp.mpf(row["gap_ode_residual"])) < mp.mpf("1e-60"))
        ok(abs(mp.mpf(row["p_ode_residual"])) < mp.mpf("1e-60"))
        ok(close(row["gap_quadratic_coefficient"], (D * D - P * P) / 4))
        ok(close(row["scaled_gap"], mp.log(y) / (s * s)))
        ok(close(row["scaled_amplitude_difference"], p * s))
        ok(p1 * p2 < 0)
        ok(y > 1)

    for row in data["regression"]["alpha_rows"]:
        ok(set(row) == ALPHA_ROW_KEYS)
        P, D = mp.mpf(row["P"]), mp.mpf(row["D_minus"])
        num, den = map(int, row["alpha"].split("/"))
        alpha = mp.mpf(num) / den
        eminus = (P * P + D * D) / 2
        eplus = (1 - alpha) * eminus + alpha * P * P
        ok(close(row["energy_minus"], eminus))
        ok(close(row["energy_plus"], eplus))
        ok(close(row["D_plus_squared"], 2 * eplus - P * P))
        ok(close(row["energy_loss"], alpha * (eminus - P * P)))
        ok(row["postcollision_state"] == ("single_peak" if num == den else "signed_pair"))

    ok(data["regression"]["counts"] == {"same_sign_rows": 15, "opposite_sign_rows": 12, "alpha_rows": 15, "boundary_rows": 4})
    ok(data["regression"]["boundaries"] == BOUNDARIES)
    ok(len(data["references"]) == 2)
    ok({row["doi"] for row in data["references"]} == {"10.1103/PhysRevLett.71.1661", "10.1142/S0219891616500119"})
    ok(data["references"] == REFERENCES)
    print(f"C278 independent checker: PASS ({checks} assertions; producer import forbidden)")


if __name__ == "__main__":
    main()
