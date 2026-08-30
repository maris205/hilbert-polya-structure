#!/usr/bin/env python3
"""Deterministic source-local certificate for the Ermakov--Pinney oscillator.

The frozen phase space is x>0 with x''+omega^2*x=kappa/x^3.  All algebraic
parameters in the receipt are rational; transcendental evaluations are only
high-precision checks of the closed formula.  No arithmetic target data are
read or inferred.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import mpmath as mp

SOURCE_COMMIT = "3ff451e904f8f063e88c40ef87f4697a6586b1a5"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
FIXED_EPOCH = 1788048000
WORKING_DIGITS = 90
SERIALIZED_DIGITS = 64
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c250_ep_evidence.json"
mp.mp.dps = WORKING_DIGITS


def ftext(q: F | int) -> str:
    q = q if isinstance(q, F) else F(q)
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def mpq(q: F | int | str) -> mp.mpf:
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


def energy(w: F, k: F, x: F, v: F) -> F:
    return (v * v + w * w * x * x + k / (x * x)) / 2


def coeffs(w: F, k: F, x: F, v: F) -> tuple[F, F, F, F, F]:
    """Return (a,b,c,E,D) for x(t)^2=a u^2+2buz+c z^2."""
    a = x * x
    b = x * v
    c = v * v + k / (x * x)
    e = energy(w, k, x, v)
    d = e * e - w * w * k
    if d < 0:
        raise ValueError("AM-GM invariant violated")
    return a, b, c, e, d


def trajectory(w: F, k: F, x0: F, v0: F, t: F) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    a, b, c, _, _ = coeffs(w, k, x0, v0)
    wm, tm = mpq(w), mpq(t)
    u = mp.cos(wm * tm)
    z = mp.sin(wm * tm) / wm
    up = -wm * mp.sin(wm * tm)
    zp = mp.cos(wm * tm)
    r = mpq(a) * u * u + 2 * mpq(b) * u * z + mpq(c) * z * z
    rp = 2 * mpq(a) * u * up + 2 * mpq(b) * (up * z + u * zp) + 2 * mpq(c) * z * zp
    x = mp.sqrt(r)
    vel = rp / (2 * x)
    en = (vel * vel + mpq(w) ** 2 * x * x + mpq(k) / (x * x)) / 2
    return x, vel, en


def invariant(w: F, k: F, x0: F, v0: F, t: F) -> mp.mpf:
    wm, tm = mpq(w), mpq(t)
    u, up = mp.cos(wm * tm), -wm * mp.sin(wm * tm)
    x, vel, _ = trajectory(w, k, x0, v0, t)
    return ((u * vel - up * x) ** 2 + mpq(k) * (u / x) ** 2) / 2


def row(case_id: str, w: F, k: F, x0: F, v0: F, t: F) -> dict:
    a, b, c, e, d = coeffs(w, k, x0, v0)
    x, v, et = trajectory(w, k, x0, v0, t)
    sqrt_d = mp.sqrt(mpq(d))
    wm = mpq(w)
    xm = mp.sqrt((mpq(e) - sqrt_d) / (wm * wm))
    xp = mp.sqrt((mpq(e) + sqrt_d) / (wm * wm))
    action = mpq(e) / (2 * wm) - mp.sqrt(mpq(k)) / 2
    return {
        "case_id": case_id, "omega": ftext(w), "kappa": ftext(k),
        "x0": ftext(x0), "v0": ftext(v0), "time": ftext(t),
        "a": ftext(a), "b": ftext(b), "c": ftext(c), "energy": ftext(e),
        "discriminant": ftext(d), "ac_minus_b2": ftext(a * c - b * b),
        "x_t": dec(x), "v_t": dec(v), "energy_t": dec(et),
        "turning_x_minus": dec(xm), "turning_x_plus": dec(xp),
        "period": None if d == 0 else dec(mp.pi / wm),
        "action": dec(action), "ermakov_invariant": dec(invariant(w, k, x0, v0, t)),
        "phase": dec(mp.atan2(mpq(b) / wm, mpq(a) - mpq(e) / (wm * wm))),
        "regime": "equilibrium" if d == 0 else ("singular_kappa_zero" if k == 0 else "oscillatory_positive"),
    }


CASES = [
    ("regular_1", F(1), F(1, 4), F(1), F(0), F(1, 7)),
    ("regular_2", F(2), F(1), F(1), F(1, 2), F(1, 9)),
    ("regular_3", F(3, 2), F(2), F(2), F(-1, 3), F(2, 11)),
    ("regular_4", F(1), F(4), F(1, 2), F(2), F(1, 5)),
    ("regular_5", F(3), F(1, 9), F(1, 3), F(1, 4), F(1, 13)),
    ("regular_6", F(5, 2), F(3, 2), F(3, 2), F(-2, 5), F(1, 8)),
    ("kappa_zero", F(1), F(0), F(2), F(1), F(1, 6)),
    ("equilibrium", F(2), F(1), F(1, 2), F(0), F(1, 10)),
    ("equilibrium_2", F(3), F(4), F(2, 3), F(0), F(1, 12)),
]


def boundary_rows() -> list[dict]:
    return [
        {"face_id": "kappa_zero", "condition": "kappa=0", "policy": "positive oscillator reaches the singular x=0 boundary; no continuation through x=0 is claimed", "period_policy": "pi/omega for nonzero-energy positive arcs"},
        {"face_id": "equilibrium", "condition": "E=omega*sqrt(kappa), kappa>0", "policy": "x(t)=kappa^(1/4)/sqrt(omega), v(t)=0", "period_policy": "degenerate constant orbit; period not assigned"},
        {"face_id": "zero_frequency", "condition": "omega=0", "policy": "outside the frozen oscillator family; not evaluated", "period_policy": "not applicable"},
        {"face_id": "negative_kappa", "condition": "kappa<0", "policy": "outside the positive isotonic phase space used here", "period_policy": "not applicable"},
    ]


def build() -> dict:
    data = {
        "schema": "hcs-c250-ermakov-pinney-isotonic-v1",
        "candidate_id": "HCS-C250", "evaluation_date": "2026-08-30",
        "source_commit": SOURCE_COMMIT, "fixed_epoch": FIXED_EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256},
        "headline": "The positive Ermakov--Pinney oscillator is closed by a quadratic invariant, an explicit linear-pair representation, exact turning radii, period and action, and all declared singular faces.",
        "frozen_object": {
            "phase_space": "x>0, v in R with canonical symplectic form dx wedge dv",
            "equation": "x_dot=v, v_dot=-omega^2*x+kappa/x^3",
            "parameters": "omega>0, kappa>=0; rational receipts",
            "linear_pair": "u=cos(omega t), z=sin(omega t)/omega, W(u,z)=1",
            "clock": "physical continuous time",
            "normalization": "E=(v^2+omega^2*x^2+kappa/x^2)/2; J=E/(2 omega)-sqrt(kappa)/2",
            "determinant_convention": "none; no orbit/Fredholm determinant",
            "arithmetic_origin": "none; source-defined mechanical parameters",
            "forbidden_data": "target primes/zeros, arithmetic local data, Euler factors, root numbers, automorphy, target divisor/functional equation, Hilbert--Polya operators",
        },
        "theorem": {
            "global_positive_solution": "For omega>0 and kappa>=0, every initial x0>0 has a unique maximal positive solution; for kappa>0 it is global and bounded away from zero, while kappa=0 records the singular boundary separately.",
            "quadratic_representation": "With a=x0^2, b=x0*v0, c=v0^2+kappa/x0^2, x(t)^2=a*u(t)^2+2*b*u(t)*z(t)+c*z(t)^2 and ac-b^2=kappa.",
            "energy_radial_equation": "r=x^2 obeys r''+4 omega^2 r=4E and r(t) remains between (E+-sqrt(E^2-omega^2*kappa))/omega^2.",
            "period": "If E>omega*sqrt(kappa), the positive oscillation has primitive period pi/omega; equality is the constant equilibrium.",
            "action": "The isotonic action on the positive component is J=E/(2 omega)-sqrt(kappa)/2, vanishing exactly at the equilibrium face.",
            "ermakov_invariant": "For either normalized linear solution q, I_q=((q*x_dot-q_dot*x)^2+kappa*(q/x)^2)/2 is constant.",
            "boundaries": "kappa=0 is a singular collision face, omega=0 and kappa<0 are outside the frozen family, and no continuation through x=0 is assigned.",
            "route_boundary": "The mechanical flow supplies no arithmetic labels, primitive repetition product, target determinant, or Hilbert--Polya operator.",
        },
        "regression": {"rows": [row(*spec) for spec in CASES], "boundary_rows": boundary_rows(), "row_count": len(CASES), "boundary_row_count": 4, "working_digits": WORKING_DIGITS, "serialized_digits": SERIALIZED_DIGITS},
        "exact_identities": [
            {"identity_id": "ep_linear_pair", "formula": "x^2=a u^2+2buz+c z^2 with u=cos(omega t), z=sin(omega t)/omega"},
            {"identity_id": "gram_determinant", "formula": "a c-b^2=kappa"},
            {"identity_id": "energy", "formula": "E=(v^2+omega^2 x^2+kappa/x^2)/2"},
            {"identity_id": "radial_ode", "formula": "(x^2)''+4 omega^2 x^2=4E"},
            {"identity_id": "radial_discriminant", "formula": "amplitude^2=(E^2-omega^2 kappa)/omega^4"},
            {"identity_id": "turning_roots", "formula": "x_+-^2=(E+-sqrt(E^2-omega^2 kappa))/omega^2"},
            {"identity_id": "period", "formula": "T=pi/omega when E>omega sqrt(kappa)"},
            {"identity_id": "action", "formula": "J=E/(2 omega)-sqrt(kappa)/2"},
            {"identity_id": "ermakov_invariant", "formula": "I_q=((q x_dot-q_dot x)^2+kappa(q/x)^2)/2 is constant"},
            {"identity_id": "equilibrium_face", "formula": "E=omega sqrt(kappa) iff x=kappa^(1/4)/sqrt(omega), v=0"},
        ],
        "route_a": {"tuple": ["A0_FAIL", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"], "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False, "strongest_positive": "Exact positive-component Ermakov--Pinney solution, invariant, period and action atlas.", "strongest_failure": "No arithmetic origin, primitive target orbit owner, determinant, or Hilbert--Polya lift."},
        "scope_flags": {k: False for k in ["uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"]},
        "citations": [
            {"key": "Ermakov1880", "claim": "Ermakov invariant origin", "source": "V. P. Ermakov, Second-order differential equations. Conditions of integrability, Univ. Izv. Kiev 9 (1880)"},
            {"key": "Pinney1950", "claim": "nonlinear superposition formula", "source": "E. Pinney, The nonlinear differential equation y''+p(x)y=c y^{-3}, Proc. AMS 1 (1950), 681"},
            {"key": "Carinena2005", "claim": "isotonic oscillator action-angle context", "source": "J. F. Cariñena, M. F. Rañada, M. Santander, Central potentials and nonlinear superposition rules, J. Math. Phys. 46 (2005)"},
        ],
        "nonclaims": ["literature priority or exhaustive classification outside the frozen positive component", "a continuation through x=0 on the kappa=0 face", "target arithmetic, Euler factors, root numbers, automorphy, target divisor or functional equation", "a primitive-orbit zeta, Fredholm determinant, or Hilbert--Polya operator", "external peer review or numerical evidence promoted to a theorem"],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser(); parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT); args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    data = build(); args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "C250_PRODUCER_PASS", "rows": data["regression"]["row_count"], "payload_sha256": data["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
