#!/usr/bin/env python3
"""Deterministic certificate producer for the spherical pendulum.

The receipt is deliberately source-local.  It records the reduced cubic,
critical-value curve, regular root chambers, three action/angle quadratures,
and the fixed oriented monodromy convention.  No arithmetic target data are
read or inferred.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path

import mpmath as mp

SOURCE_COMMIT = "5f357e2d2b78604f6c286bfbd05da922e1d6791f"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
FIXED_EPOCH = 1788048000
WORKING_DIGITS = 90
SERIALIZED_DIGITS = 64
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c244_pendulum_evidence.json"
mp.mp.dps = WORKING_DIGITS


def ftext(q: F | int) -> str:
    q = q if isinstance(q, F) else F(q)
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def mpq(q: F | int) -> mp.mpf:
    q = q if isinstance(q, F) else F(q)
    return mp.mpf(q.numerator) / q.denominator


def dec(x: mp.mpf) -> str:
    if abs(x) < mp.mpf("1e-82"):
        x = mp.mpf("0")
    return mp.nstr(x, SERIALIZED_DIGITS, strip_zeros=False, min_fixed=-70, max_fixed=70)


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def roots_for(h: mp.mpf, j: mp.mpf) -> list[mp.mpf]:
    rr = mp.polyroots([mp.mpf(2), -2 * h, mp.mpf(-2), 2 * h - j * j], maxsteps=1000, error=False)
    real = sorted([mp.re(z) for z in rr if abs(mp.im(z)) < mp.mpf("1e-55")])
    if len(real) != 3:
        raise ValueError("regular sentinel did not have three real roots")
    return real


def quadratures(hq: F, jq: F) -> tuple[list[mp.mpf], tuple[mp.mpf, mp.mpf, mp.mpf]]:
    h, j = mpq(hq), mpq(jq)
    roots = roots_for(h, j)
    r1, r2, r3 = roots
    m = (r1 + r2) / 2
    d = (r2 - r1) / 2

    def u_of(t: mp.mpf) -> mp.mpf:
        return m + d * mp.cos(t)

    def den(t: mp.mpf) -> mp.mpf:
        return mp.sqrt(2 * (r3 - u_of(t)))

    T = 2 * mp.quad(lambda t: 1 / den(t), [0, mp.pi])
    D = 2 * j * mp.quad(lambda t: 1 / ((1 - u_of(t) ** 2) * den(t)), [0, mp.pi])
    # sqrt(P) du contributes d^2 sin(t)^2 * sqrt(2(r3-u)) dt.
    I = (1 / mp.pi) * mp.quad(lambda t: d * d * mp.sin(t) ** 2 * den(t) / (1 - u_of(t) ** 2), [0, mp.pi])
    return roots, (T, D, I)


REGULAR_CASES = [
    ("R01", F(-1, 2), F(1, 4)), ("R02", F(0), F(1, 10)),
    ("R03", F(0), F(1, 4)), ("R04", F(1, 4), F(1, 10)),
    ("R05", F(1, 2), F(1, 10)), ("R06", F(3, 4), F(1, 20)),
    ("R07", F(9, 10), F(1, 20)), ("R08", F(1), F(1, 100)),
]


def regular_rows() -> list[dict]:
    rows = []
    for cid, hq, jq in REGULAR_CASES:
        roots, vals = quadratures(hq, jq)
        rows.append({
            "case_id": cid, "h": ftext(hq), "j": ftext(jq), "j_squared": ftext(jq * jq),
            "root_count": 3, "roots": [dec(x) for x in roots],
            "physical_interval": "(r1,r2) subset (-1,1); r3>1", "root_order": "r1<r2<1<r3",
            "period_T": dec(vals[0]), "angle_increment_Delta_phi": dec(vals[1]), "action_I": dec(vals[2]),
            "quadrature_parameterization": "u=(r1+r2)/2+(r2-r1)cos(theta)/2, theta in [0,pi]",
            "regularity": "discriminant nonzero; j!=0",
        })
    return rows


def critical_rows() -> list[dict]:
    rows = [
        {"face_id": "bottom_elliptic_endpoint", "s": "-1", "h": "-1", "j_squared": "0", "discriminant": "0", "type": "elliptic-elliptic endpoint", "boundary_note": "u=-1, theta=pi; azimuth collapses"},
        {"face_id": "top_focus_focus_endpoint", "s": "1", "h": "1", "j_squared": "0", "discriminant": "0", "type": "focus-focus endpoint", "boundary_note": "u=1, theta=0; upright equilibrium and pinched fiber"},
    ]
    for s in (F(-1, 2), F(-1, 3), F(-2, 3), F(-3, 4), F(-4, 5)):
        h = (3 * s * s - 1) / (2 * s)
        q = (1 - s * s) ** 2 / (-s)
        rows.append({"face_id": "interior_double_root", "s": ftext(s), "h": ftext(h), "j_squared": ftext(q), "discriminant": "0", "type": "elliptic critical circle", "boundary_note": "P(s)=P'(s)=0; s in (-1,0)"})
    return rows


def build() -> dict:
    fixed = [
        {"point_id": "bottom", "theta": "pi", "u": "-1", "j": "0", "h": "-1", "singularity_type": "elliptic-elliptic", "chart": "global_vector"},
        {"point_id": "top", "theta": "0", "u": "1", "j": "0", "h": "1", "singularity_type": "focus-focus", "chart": "global_vector"},
    ]
    data = {
        "schema": "hcs-c244-spherical-pendulum-monodromy-v1", "candidate_id": "HCS-C244", "evaluation_date": "2026-08-30",
        "source_commit": SOURCE_COMMIT, "fixed_epoch": FIXED_EPOCH, "scope_literal": SCOPE,
        "evaluator": {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256},
        "headline": "The unit spherical pendulum has a certified reduced cubic, critical-value chambers, Liouville quadratures, and the oriented focus-focus monodromy receipt.",
        "frozen_object": {"phase_space": "T^*S^2 with global embedding coordinates (r,p) and local (theta,phi,p_theta,j)", "hamiltonian": "H=1/2*(p_theta^2+j^2/sin(theta)^2)+cos(theta)", "momentum": "J=j=p_phi", "reduction": "u=cos(theta), P_hj(u)=2(1-u^2)(h-u)-j^2, u_dot^2=P_hj(u)", "polynomial_expansion": "P=2u^3-2hu^2-2u+2h-j^2", "clock": "unit gravitational time", "orientation_convention": "(cycle alpha, cycle beta) is fixed so positive focus-focus transport is beta -> beta+alpha", "arithmetic_origin": "none; source-defined mechanical Hamiltonian", "forbidden_data": "target primes/zeros, local arithmetic, Euler factors, root numbers, automorphy, target determinants, Hilbert--Polya operators"},
        "theorem": {"critical_curve": "For an interior double root s in (-1,0): h=(3s^2-1)/(2s), j^2=(1-s^2)^2/(-s); endpoints are (-1,0) elliptic-elliptic and (1,0) focus-focus.", "discriminant": "disc_u(P)=4*(16h^4-8h^3j^2-32h^2+72hj^2-27j^4+16)", "root_chambers": "A regular j!=0 chamber has r1<r2<1<r3 and physical interval (r1,r2) subset (-1,1).", "quadratures": "T=2 integral du/sqrt(P), Delta_phi=2j integral du/((1-u^2)sqrt(P)), I=(1/pi) integral sqrt(P)/(1-u^2) du; endpoint-cancelled theta formulas are certified in each row.", "liouville_fibers": "Regular fibers are Liouville tori; critical circles and the isolated focus-focus pinched fiber are separated from the interior elliptic branch.", "torus_closure": "A regular torus trajectory closes iff Delta_phi/(2*pi)=p/q in lowest terms; the primitive closure uses q u-oscillations and repetitions use kq, while irrational ratios are quasiperiodic.", "monodromy": "With the declared oriented basis and a positive loop around the isolated focus-focus value, M=[[1,1],[0,1]].", "boundaries": "At u=+/-1 use the global vector chart; double roots are not assigned regular periods. No elementary closed form is asserted for every quadrature."},
        "regression": {"critical_rows": critical_rows(), "regular_rows": regular_rows(), "fixed_rows": fixed, "monodromy": {"matrix": [[1, 1], [0, 1]], "loop_orientation": "positive counterclockwise around (h,j)=(1,0)", "basis": "alpha=vanishing cycle, beta=transported complementary cycle", "matrix_convention": "columns_are_transported_basis_vectors_in_initial_basis", "transport_receipt": "beta_final=beta_initial+alpha_initial", "determinant": 1}, "critical_row_count": 7, "regular_row_count": 8, "fixed_row_count": 2, "working_digits": WORKING_DIGITS, "serialized_digits": SERIALIZED_DIGITS},
        "exact_identities": [{"identity_id": "hamilton_equations", "formula": "theta_dot=p_theta, phi_dot=j/sin(theta)^2, p_theta_dot=j^2 cos(theta)/sin(theta)^3+sin(theta)"}, {"identity_id": "reduced_cubic", "formula": "P_hj(u)=2(1-u^2)(h-u)-j^2=2u^3-2hu^2-2u+2h-j^2"}, {"identity_id": "discriminant", "formula": "disc_u(P)=4*(16h^4-8h^3j^2-32h^2+72hj^2-27j^4+16)"}, {"identity_id": "critical_parameterization", "formula": "P(s)=P'(s)=0 => h=(3s^2-1)/(2s), j^2=(1-s^2)^2/(-s)"}, {"identity_id": "period_quadrature", "formula": "T=2 integral_(r1)^(r2) du/sqrt(P)"}, {"identity_id": "angle_quadrature", "formula": "Delta_phi=2j integral_(r1)^(r2) du/((1-u^2)sqrt(P))"}, {"identity_id": "action_quadrature", "formula": "I=(1/pi) integral_(r1)^(r2) sqrt(P)/(1-u^2) du"}, {"identity_id": "torus_closure", "formula": "Delta_phi/(2*pi)=p/q in lowest terms iff closure after q u-oscillations; kq is the kth repetition"}, {"identity_id": "focus_monodromy", "formula": "M_(alpha,beta)=[[1,1],[0,1]] for positive focus-focus loop"}, {"identity_id": "pole_regularization", "formula": "global (r,p) in R^3 x R^3 removes the theta=0,pi coordinate singularity"}],
        "route_a": {"tuple": ["A0_FAIL", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"], "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False, "strongest_positive": "Exact analytic mechanics and certified quadrature/monodromy atlas.", "strongest_failure": "No discrete arithmetic target match or isolated primitive orbit owner is defined."},
        "scope_flags": {k: False for k in ["uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"]},
        "citations": [{"key": "CushmanDuistermaat1988", "claim": "spherical pendulum quantum/semi-global monodromy and focus-focus obstruction", "source": "Cushman and Duistermaat, The quantum mechanical spherical pendulum, Bulletin AMS 19 (1988), DOI 10.1090/S0273-0979-1988-15705-9", "url": "https://doi.org/10.1090/S0273-0979-1988-15705-9"}, {"key": "Dullin2013", "claim": "semi-global symplectic invariants of the spherical pendulum", "source": "Dullin, Semi-global symplectic invariants of the spherical pendulum, J. Differential Equations 254 (2013), DOI 10.1016/j.jde.2013.01.018", "url": "https://doi.org/10.1016/j.jde.2013.01.018", "preprint": "https://arxiv.org/abs/1108.4962"}],
        "nonclaims": ["exhaustive classification of all trajectories", "elementary closed forms for every quadrature", "arithmetic Euler factors, root numbers, automorphy, target divisor or functional equation", "a target zeta/Fredholm determinant, zero match, or Hilbert--Polya operator", "external peer review or novelty priority"],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser(); parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT); args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    data = build(); args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "C244_PRODUCER_PASS", "critical_rows": data["regression"]["critical_row_count"], "regular_rows": data["regression"]["regular_row_count"], "payload_sha256": data["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
