#!/usr/bin/env python3
"""Deterministic exact/high-precision receipt for the C256 KdV wave atlas."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path

import mpmath as mp

SOURCE_COMMIT = "b89544f1f7b1043f4158dfdf9db77787b332f146"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
FIXED_EPOCH = 1788048000
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c256_kdv_evidence.json"
mp.mp.dps = 90


def qtext(q: F | int) -> str:
    q = q if isinstance(q, F) else F(q)
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def mpq(q: F | int) -> mp.mpf:
    q = q if isinstance(q, F) else F(q)
    return mp.mpf(q.numerator) / q.denominator


def dec(x: mp.mpf) -> str:
    return mp.nstr(mp.mpf(x), 75, strip_zeros=False)


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


TRIPLES = [
    (F(-5), F(-2), F(1)), (F(-4), F(1), F(2)), (F(-3), F(-1), F(2)),
    (F(-2), F(0), F(3)), (F(-2), F(3), F(7)), (F(-1), F(0), F(1)),
    (F(-1), F(1), F(4)), (F(0), F(1), F(2)), (F(0), F(1), F(3)),
    (F(0), F(2), F(5)), (F(1), F(2), F(4)), (F(2), F(5), F(9)),
]


def periodic_row(idx: int, roots: tuple[F, F, F]) -> dict:
    r1q, r2q, r3q = roots
    Dq, dq = r3q - r1q, r3q - r2q
    mq = dq / Dq
    cq = 2 * (r1q + r2q + r3q)
    pairq = r1q * r2q + r1q * r3q + r2q * r3q
    r1, r2, r3, D, d, m = map(mpq, (r1q, r2q, r3q, Dq, dq, mq))
    k = mp.sqrt(D / 2)
    K, E = mp.ellipk(m), mp.ellipe(m)
    period = 2 * K / k
    mean = r1 + D * E / K
    avg_cn2 = (E - (1 - m) * K) / (m * K)
    avg_sn2 = (K - E) / (m * K)
    avg_sn4 = ((2 + m) * K - 2 * (1 + m) * E) / (3 * m * m * K)
    avg_cn4 = 1 - 2 * avg_sn2 + avg_sn4
    mean_square = r2 * r2 + 2 * r2 * d * avg_cn2 + d * d * avg_cn4
    max_energy, max_ode = mp.mpf("0"), mp.mpf("0")
    c, pair = mpq(cq), mpq(pairq)
    for j in range(17):
        xi = period * mp.mpf(j) / 17
        s = k * xi
        cn = mp.ellipfun("cn", s, m)
        sn = mp.ellipfun("sn", s, m)
        dn = mp.ellipfun("dn", s, m)
        q = cn * cn
        U = r2 + d * q
        Up = -2 * d * k * cn * sn * dn
        poly = 2 * (r3 - U) * (U - r2) * (U - r1)
        fprime = 4 * ((1 - 2 * q) * (1 - m + m * q) + m * q * (1 - q))
        Upp = d * k * k * fprime / 2
        max_energy = max(max_energy, abs(Up * Up - poly))
        max_ode = max(max_ode, abs(Upp - (c * U - 3 * U * U - pair)))
    return {
        "row_id": f"P{idx:02d}",
        "roots": [qtext(r1q), qtext(r2q), qtext(r3q)],
        "root_order": "r1<r2<r3",
        "speed": qtext(cq),
        "pair_sum": qtext(pairq),
        "modulus_m": qtext(mq),
        "amplitude": qtext(dq),
        "wave_number": dec(k),
        "K": dec(K),
        "E": dec(E),
        "fundamental_period": dec(period),
        "period_mean": dec(mean),
        "period_mean_square": dec(mean_square),
        "max_first_integral_residual_17_nodes": dec(max_energy),
        "max_profile_ode_residual_17_nodes": dec(max_ode),
    }


def soliton_rows() -> list[dict]:
    rows = []
    for idx, (a, b) in enumerate(((F(-2), F(1)), (F(0), F(2)), (F(1), F(4))), 1):
        D = b - a
        k = mp.sqrt(mpq(D) / 2)
        rows.append({
            "row_id": f"S{idx}", "r1_equals_r2": qtext(a), "r3": qtext(b),
            "speed": qtext(2 * (2 * a + b)), "height_above_background": qtext(D),
            "inverse_width": dec(k), "excess_mass": dec(2 * mpq(D) / k),
            "profile": "r1+(r3-r1)*sech^2(sqrt((r3-r1)/2)*xi)",
        })
    return rows


def harmonic_rows() -> list[dict]:
    rows = []
    for idx, (a, b) in enumerate(((F(-3), F(1)), (F(0), F(2)), (F(2), F(5))), 1):
        D = b - a
        omega = mp.sqrt(2 * mpq(D))
        rows.append({
            "row_id": f"H{idx}", "r1": qtext(a), "r2_equals_r3": qtext(b),
            "constant_level": qtext(b), "limiting_angular_frequency": dec(omega),
            "limiting_period": dec(2 * mp.pi / omega),
            "qualification": "small-amplitude limit with r1 fixed; a constant profile itself selects no speed",
        })
    return rows


def galilean_rows() -> list[dict]:
    base = (F(-1), F(0), F(2))
    c0 = 2 * sum(base, F(0))
    rows = []
    for idx, a in enumerate((F(-3), F(-1), F(1, 2), F(1), F(2), F(4)), 1):
        shifted = tuple(r + a for r in base)
        rows.append({
            "row_id": f"G{idx}", "shift_a": qtext(a),
            "base_roots": [qtext(x) for x in base], "shifted_roots": [qtext(x) for x in shifted],
            "base_speed": qtext(c0), "shifted_speed": qtext(2 * sum(shifted, F(0))),
            "speed_increment": qtext(6 * a), "profile_increment": qtext(a),
        })
    return rows


def build() -> dict:
    periodic = [periodic_row(i, roots) for i, roots in enumerate(TRIPLES, 1)]
    data = {
        "schema": "hcs-c256-kdv-cnoidal-traveling-wave-atlas-v1",
        "candidate_id": "HCS-C256",
        "evaluation_date": "2026-08-31",
        "source_commit": SOURCE_COMMIT,
        "fixed_epoch": FIXED_EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256},
        "headline": "The plus-sign KdV equation has a root-complete bounded traveling-wave atlas with exact cnoidal periods and means, soliton and harmonic degenerations, and Galilean covariance.",
        "frozen_object": {
            "equation": "u_t+6*u*u_x+u_xxx=0",
            "phase_space": "real classical profiles U(x-c*t) on R, with the periodic profile also read on its fundamental circle",
            "traveling_coordinate": "xi=x-c*t",
            "clock": "physical PDE time t; a nonstationary wave on its fundamental circle returns after L/abs(c)",
            "parameters": "real integration constants, equivalently ordered cubic roots including their double/triple-root faces",
            "arithmetic_origin": "none; continuously tunable dispersive-wave roots",
            "determinant_convention": "none; the auxiliary KdV Lax operator is only a formal A4 hint",
            "forbidden_data": "target primes/zeros, arithmetic local data, Euler factors, root numbers, automorphy, target divisors, Hilbert--Polya operators",
        },
        "theorem": {
            "first_integral": "Every traveling profile satisfies U''=c*U-3*U^2+A and (U')^2=-2*U^3+c*U^2+2*A*U+B.",
            "bounded_classification": "A nonconstant bounded entire real profile exists exactly when the energy cubic has three real roots r1<r2<r3 and oscillates on [r2,r3], or on the lower-double-root homoclinic face r1=r2<r3; all other bounded entire profiles are constants.",
            "periodic_formula": "For r1<r2<r3, c=2*(r1+r2+r3), m=(r3-r2)/(r3-r1), k=sqrt((r3-r1)/2), and U=r2+(r3-r2)*cn^2(k*xi;m).",
            "period_and_mean": "The fundamental spatial period is L=2*sqrt(2/(r3-r1))*K(m), and the period mean is r1+(r3-r1)*E(m)/K(m).",
            "soliton_face": "As r2 decreases to r1, U tends to r1+(r3-r1)*sech^2(sqrt((r3-r1)/2)*xi), with speed 2*(2*r1+r3).",
            "harmonic_face": "As r2 increases to r3 with r1 fixed, amplitude vanishes and L tends to 2*pi/sqrt(2*(r3-r1)); the limiting constant itself has no selected traveling speed.",
            "galilean": "If u solves KdV, then u(x-6*a*t,t)+a solves it; every root shifts by a and c shifts by 6*a.",
            "temporal_return": "On the circle of fundamental length L, c!=0 gives a periodic PDE orbit of primitive time L/abs(c); c=0 gives a stationary profile.",
            "scope": "The classification is for bounded classical traveling profiles, not every KdV solution and not a nonlinear stability theorem.",
        },
        "receipts": {
            "periodic_rows": periodic, "periodic_row_count": len(periodic),
            "soliton_rows": soliton_rows(), "soliton_row_count": 3,
            "harmonic_rows": harmonic_rows(), "harmonic_row_count": 3,
            "galilean_rows": galilean_rows(), "galilean_row_count": 6,
            "working_decimal_digits": 90,
            "printed_significant_digits": 75,
            "finite_receipt_boundary": "Rows test formulas and conventions; the all-root classification is proof-driven.",
        },
        "exact_identities": [
            {"id": "traveling_reduction", "formula": "-c*U'+6*U*U'+U'''=0"},
            {"id": "profile_ode", "formula": "U''=c*U-3*U^2+A"},
            {"id": "energy_cubic", "formula": "(U')^2=-2*U^3+c*U^2+2*A*U+B"},
            {"id": "root_factor", "formula": "(U')^2=2*(r3-U)*(U-r2)*(U-r1)"},
            {"id": "speed", "formula": "c=2*(r1+r2+r3)"},
            {"id": "integration_constants", "formula": "A=-(r1*r2+r1*r3+r2*r3); B=2*r1*r2*r3"},
            {"id": "modulus", "formula": "m=(r3-r2)/(r3-r1) in (0,1)"},
            {"id": "period", "formula": "L=2*sqrt(2/(r3-r1))*K(m)"},
            {"id": "mean", "formula": "mean(U)=r1+(r3-r1)*E(m)/K(m)"},
            {"id": "soliton", "formula": "U=r1+(r3-r1)*sech^2(sqrt((r3-r1)/2)*xi) when r1=r2"},
            {"id": "harmonic", "formula": "L->2*pi/sqrt(2*(r3-r1)) when r2->r3"},
            {"id": "galilean", "formula": "u_a(x,t)=u(x-6*a*t,t)+a; roots->roots+a; c->c+6*a"},
            {"id": "circle_clock", "formula": "T=L/abs(c) for c!=0 on the fundamental circle; c=0 is stationary"},
            {"id": "route_stop", "formula": "source traveling-wave periods are continuously tunable and carry no rational-prime clock"},
        ],
        "route_a": {
            "tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False,
            "strongest_positive": "The bounded traveling-wave root topology, periodic family, degenerations, periods, means, and circle returns are analytic and complete within the declared coherent family.",
            "strongest_failure": "There is no intrinsic arithmetic owner, rational-prime correspondence, target-weighted primitive census, target determinant, or global target analytic structure.",
        },
        "scope_flags": {k: False for k in ["uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"]},
        "citations": [
            {"key": "KortewegDeVries1895", "claim": "original long-wave equation and permanent-wave context", "source": "D. J. Korteweg and G. de Vries, Philosophical Magazine 39 (1895), 422--443", "url": "https://doi.org/10.1080/14786449508620739"},
            {"key": "LeitnerMikikits2014", "claim": "Jacobi-cn cnoidal differential identities and KdV ansatz", "source": "M. Leitner and A. Mikikits-Leitner, Mathematische Nachrichten 287 (2014), 2040--2056", "url": "https://doi.org/10.1002/mana.201300233"},
            {"key": "Lax1968", "claim": "KdV isospectral/Lax context used only for the formal A4 hint", "source": "P. D. Lax, Communications on Pure and Applied Mathematics 21 (1968), 467--490", "url": "https://doi.org/10.1002/cpa.3160210503"},
        ],
        "nonclaims": [
            "classification of every KdV solution or every finite-gap solution",
            "nonlinear, orbital, or spectral stability of the cnoidal family",
            "a complete primitive-orbit census for the full KdV phase space",
            "an arithmetic Euler product, target divisor, counting law, or functional equation",
            "a Hilbert--Polya operator, target quantization, or Route-B input",
            "literature priority for the classical cnoidal formulas",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = ap.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    data = build()
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "C256_PRODUCER_PASS", "periodic_rows": data["receipts"]["periodic_row_count"], "boundary_rows": data["receipts"]["soliton_row_count"] + data["receipts"]["harmonic_row_count"] + data["receipts"]["galilean_row_count"], "payload_sha256": data["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
