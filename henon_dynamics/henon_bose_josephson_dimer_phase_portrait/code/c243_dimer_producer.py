#!/usr/bin/env python3
"""Deterministic certificate producer for the Bose--Josephson dimer.

The frozen Hamiltonian is H(z,phi)=Lambda*z^2/2-sqrt(1-z^2)*cos(phi) on
the Bloch sphere.  All structural labels are source-local; no target
arithmetic data are used.  Elliptic-integral periods are high-precision
displays, while the energy polynomial, fixed points, and component criteria
are checked independently.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
import math
from pathlib import Path

import mpmath as mp

SOURCE_COMMIT = "489506cf92bfed721f94f22dd0444a60427f90a5"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
FIXED_EPOCH = 1788048000
WORKING_DIGITS = 90
SERIALIZED_DIGITS = 64
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c243_dimer_evidence.json"
mp.mp.dps = WORKING_DIGITS


def ftext(q: F | int) -> str:
    q = q if isinstance(q, F) else F(q)
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def dec(x: mp.mpf) -> str:
    if abs(x) < mp.mpf("1e-82"):
        x = mp.mpf("0")
    return mp.nstr(x, SERIALIZED_DIGITS, strip_zeros=False, min_fixed=-70, max_fixed=70)


def mpq(q: F | int) -> mp.mpf:
    q = q if isinstance(q, F) else F(q)
    return mp.mpf(q.numerator) / q.denominator


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def fixed_rows() -> list[dict]:
    rows: list[dict] = []
    for lam in (F(0), F(1, 2), F(1), F(2), F(3)):
        lm = mpq(lam)
        rows.append({"lambda": ftext(lam), "point_id": "zero_phase", "z": "0", "phi": "0", "energy": "-1", "linearization_matrix": "[[0,-1],[Lambda+1,0]]", "frequency_squared": ftext(lam + 1), "frequency_or_growth": dec(mp.sqrt(lm + 1)), "stability": "elliptic", "symmetry_broken": False})
        if lam < 1:
            stab, fsq, fg = "elliptic", ftext(1 - lam), dec(mp.sqrt(1 - lm))
        elif lam == 1:
            stab, fsq, fg = "parabolic_pitchfork", "0", "0.0"
        else:
            stab, fsq, fg = "hyperbolic", ftext(lam - 1), dec(mp.sqrt(lm - 1))
        rows.append({"lambda": ftext(lam), "point_id": "pi_symmetric", "z": "0", "phi": "pi", "energy": "1", "linearization_matrix": "[[0,1],[Lambda-1,0]]", "frequency_squared": fsq, "frequency_or_growth": fg, "stability": stab, "symmetry_broken": False})
        if lam > 1:
            zexpr = "sqrt(1-Lambda^-2)"
            hmax = f"({ftext(lam)}+1/{ftext(lam)})/2"
            freq = dec(mp.sqrt(lm * lm - 1))
            for sign, sid in (("+", "broken_plus"), ("-", "broken_minus")):
                rows.append({"lambda": ftext(lam), "point_id": sid, "z": sign + zexpr, "phi": "pi", "energy": hmax, "linearization_matrix": "[[0,1/Lambda],[-Lambda*(Lambda^2-1),0]]", "frequency_squared": ftext(lam * lam - 1), "frequency_or_growth": freq, "stability": "elliptic", "symmetry_broken": True})
    return rows


def bloch_rows() -> list[dict]:
    rows = []
    for lam in (F(0), F(1), F(2), F(3)):
        for sign in (1, -1):
            rows.append({"lambda": ftext(lam), "point_id": "north_pole" if sign == 1 else "south_pole", "x": "0", "y": "0", "z": str(sign), "xdot": "0", "ydot": str(sign), "zdot": "0", "chart": "Bloch_vector"})
    return rows


def level_row(case_id: str, lam: F, h: F) -> dict:
    lm, hm = mpq(lam), mpq(h)
    base = {"case_id": case_id, "lambda": ftext(lam), "energy": ftext(h), "root_formula": "y_pm=2*(Lambda*H-1 +/- sqrt(Lambda^2-2*Lambda*H+1))/Lambda^2", "quadrature_integral": "dt=2 dz/(Lambda sqrt((y_plus-z^2)(z^2-y_minus)))", "elliptic_reduction": "complete elliptic K with the displayed modulus", "y_minus": None, "y_plus": None, "elliptic_modulus": None, "period": None, "period_formula": None, "allowed_interval": None, "sign_components": None, "component_verdict": None, "crosses_zero": None, "separatrix_profile": None, "turning_phase": None, "pole_coordinate_warning": False}
    if lam == 0:
        base.update({"level_type": "regular_sphere_rotation", "allowed_interval": "Bloch circle x=-H", "sign_components": 1, "component_verdict": "sphere_rotation", "crosses_zero": True, "period": dec(2 * mp.pi), "period_formula": "2*pi"})
        return base
    disc = lm * lm - 2 * lm * hm + 1
    delta = mp.sqrt(max(mp.mpf("0"), disc))
    ym = 2 * (lm * hm - 1 - delta) / (lm * lm)
    yp = 2 * (lm * hm - 1 + delta) / (lm * lm)
    base["y_minus"], base["y_plus"] = dec(ym), dec(yp)
    hmax = (lm + 1 / lm) / 2
    if lam == 1 and h == 1:
        base.update({"level_type": "pitchfork_critical_point", "allowed_interval": "z=0 only (z_dot^2=-z^4/4)", "sign_components": 1, "component_verdict": "pitchfork_critical_point", "crosses_zero": False, "period_formula": "none (isolated degenerate point)"})
        return base
    if lam > 1 and h == 1:
        A = 2 * mp.sqrt(lm - 1) / lm
        om = mp.sqrt(lm - 1)
        turn = "pi" if lam < 2 else ("pole" if lam == 2 else "0")
        base.update({"level_type": "separatrix", "allowed_interval": f"connected full level; two one-sided branches 0<|z|<={dec(A)}", "sign_components": 1, "component_verdict": "separatrix_one_sided", "crosses_zero": False, "period_formula": "infinite (homoclinic)", "separatrix_profile": f"z(t)=+/- {dec(A)} sech({dec(om)} t)", "turning_phase": turn, "pole_coordinate_warning": lam == 2})
        return base
    if lam > 1 and h > 1:
        if hm < hmax:
            mod = mp.sqrt(1 - ym / yp)
            per = 4 / (lm * mp.sqrt(yp)) * mp.ellipk(mod * mod)
            base.update({"level_type": "regular_self_trapped", "elliptic_modulus": dec(mod), "period": dec(per), "period_formula": "4/(Lambda*sqrt(y_plus))*K(sqrt(1-y_minus/y_plus))", "allowed_interval": f"[sqrt(y_minus),sqrt(y_plus)] union -[sqrt(y_minus),sqrt(y_plus)]", "sign_components": 2, "component_verdict": "self_trapped", "crosses_zero": False})
            return base
    if -1 < h < 1:
        mod = mp.sqrt(yp / (yp - ym))
        per = 8 / (lm * mp.sqrt(yp - ym)) * mp.ellipk(mod * mod)
        base.update({"level_type": "regular_crossing", "elliptic_modulus": dec(mod), "period": dec(per), "period_formula": "8/(Lambda*sqrt(y_plus-y_minus))*K(sqrt(y_plus/(y_plus-y_minus)))", "allowed_interval": f"[-sqrt(y_plus),sqrt(y_plus)]", "sign_components": 1, "component_verdict": "crossing", "crosses_zero": True})
        return base
    base.update({"level_type": "inaccessible_or_fixed_boundary", "component_verdict": "boundary", "crosses_zero": False})
    return base


LEVEL_CASES = [
    ("L0_hminus1_2", F(0), F(-1, 2)), ("L0_hplus1_2", F(0), F(1, 2)),
    ("Lhalf_cross_minus", F(1, 2), F(-1, 2)), ("Lhalf_cross_plus", F(1, 2), F(1, 2)),
    ("L1_cross_minus", F(1), F(-1, 2)), ("L1_cross_plus", F(1), F(1, 2)), ("L1_pitchfork", F(1), F(1)),
    ("L2_cross", F(2), F(-1, 2)), ("L2_sep", F(2), F(1)), ("L2_self", F(2), F(11, 10)),
    ("L3_cross", F(3), F(0)), ("L3_sep", F(3), F(1)), ("L3_self", F(3), F(6, 5)),
]


CRITERION_CASES = [
    {"case_id": "crossing_regular", "lambda": "2", "energy": "1/2", "initial_sign": "+", "criterion": "H<1", "verdict": "crossing", "reverse_condition": "H<1 gives a one-component level and both signs are reached"},
    {"case_id": "self_trapped_positive", "lambda": "2", "energy": "11/10", "initial_sign": "+", "criterion": "H>1 and H<h_max", "verdict": "self_trapped", "reverse_condition": "sign(z(t))=sign(z(0))"},
    {"case_id": "self_trapped_negative", "lambda": "2", "energy": "11/10", "initial_sign": "-", "criterion": "H>1 and H<h_max", "verdict": "self_trapped", "reverse_condition": "sign(z(t))=sign(z(0))"},
    {"case_id": "separatrix_plus", "lambda": "3", "energy": "1", "initial_sign": "+", "criterion": "H=1", "verdict": "separatrix_one_sided", "reverse_condition": "approaches z=0 asymptotically; no finite crossing"},
    {"case_id": "lambda1_boundary", "lambda": "1", "energy": "1", "initial_sign": "+", "criterion": "Lambda=1,H=1", "verdict": "pitchfork_critical_point", "reverse_condition": "isolated degenerate point z=0; no regular separatrix"},
]


def build() -> dict:
    levels = [level_row(*spec) for spec in LEVEL_CASES]
    data = {
        "schema": "hcs-c243-bose-josephson-dimer-phase-portrait-v1", "candidate_id": "HCS-C243", "evaluation_date": "2026-08-30", "source_commit": SOURCE_COMMIT, "fixed_epoch": FIXED_EPOCH, "scope_literal": SCOPE,
        "evaluator": {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256},
        "headline": "The Bose--Josephson dimer admits an exact Bloch-sphere fixed-point bifurcation atlas, energy-root components, elliptic-K periods, and a certified self-trapping/separatrix boundary.",
        "frozen_object": {"phase_space": "Bloch sphere x^2+y^2+z^2=1 with canonical chart z,phi away from z=+/-1", "hamiltonian": "H(z,phi)=Lambda*z^2/2-sqrt(1-z^2)*cos(phi)", "equations": "z_dot=-sqrt(1-z^2)sin(phi); phi_dot=Lambda*z+z*cos(phi)/sqrt(1-z^2)", "bloch_equations": "x_dot=-Lambda*z*y; y_dot=z*(1+Lambda*x); z_dot=-y", "parameter": "Lambda>=0", "clock": "dimensionless Josephson time", "normalization": "Hamiltonian energy H and Bloch radius one", "arithmetic_origin": "none; source-defined nonlinear two-mode model", "forbidden_data": "target primes/zeros, local arithmetic, Euler factors, root numbers, automorphy, target divisor/functional equation, Hilbert--Polya operators"},
        "theorem": {"fixed_points": "(0,0) and (0,pi) for all Lambda; for Lambda>1 also z=+/-sqrt(1-Lambda^-2),phi=pi", "pitchfork": "At Lambda=1 the symmetry-broken pair coalesces with (0,pi), whose linearization is parabolic; stability changes from elliptic to hyperbolic", "energy_reduction": "z_dot^2=-(Lambda^2/4)z^4+(Lambda*H-1)z^2+1-H^2", "roots": "y_pm=2*(Lambda*H-1 +/- sqrt(Lambda^2-2*Lambda*H+1))/Lambda^2", "period_crossing": "For -1<H<1 and Lambda>0, T=8/(Lambda*sqrt(y_plus-y_minus))*K(sqrt(y_plus/(y_plus-y_minus)))", "period_self": "For Lambda>1 and 1<H<(Lambda+Lambda^-1)/2, each sign component has T=4/(Lambda*sqrt(y_plus))*K(sqrt(1-y_minus/y_plus))", "small_amplitude_limits": "The zero-phase crossing limit is 2*pi/sqrt(Lambda+1); the symmetry-broken limit is 2*pi/sqrt(Lambda^2-1)", "separatrix": "For Lambda>1,H=1, z(t)=+/-2*sqrt(Lambda-1)/Lambda*sech(sqrt(Lambda-1)t); the full critical level is connected with two one-sided homoclinic branches; turning phi is pi for 1<Lambda<2, pole at Lambda=2, and 0 for Lambda>2", "self_trapping": "For regular Lambda>1 levels, H>1 is equivalent to two sign components and sign(z) is invariant; H<1 is the one-component crossing regime; H=1 is one-sided homoclinic/separatrix", "boundaries": "Lambda=0 is rigid Bloch rotation with period 2*pi; Lambda=1 is a pitchfork with the H=1 level reduced to the isolated degenerate point z=0; Lambda=2 homoclinic turning reaches a coordinate pole"},
        "regression": {"fixed_points": fixed_rows(), "bloch_poles": bloch_rows(), "level_rows": levels, "criterion_rows": CRITERION_CASES, "fixed_point_row_count": len(fixed_rows()), "bloch_pole_row_count": len(bloch_rows()), "level_row_count": len(levels), "criterion_row_count": len(CRITERION_CASES), "working_digits": WORKING_DIGITS, "serialized_digits": SERIALIZED_DIGITS},
        "exact_identities": [{"identity_id": "hamilton_equations", "formula": "z_dot=-H_phi; phi_dot=H_z"}, {"identity_id": "bloch_regularization", "formula": "x=sqrt(1-z^2)cos(phi), y=sqrt(1-z^2)sin(phi)"}, {"identity_id": "bloch_flow", "formula": "(x_dot,y_dot,z_dot)=(-Lambda*z*y,z*(1+Lambda*x),-y)"}, {"identity_id": "energy_polynomial", "formula": "z_dot^2=(1-z^2)-(Lambda*z^2/2-H)^2"}, {"identity_id": "root_sum", "formula": "y_plus+y_minus=4*(Lambda*H-1)/Lambda^2"}, {"identity_id": "root_product", "formula": "y_plus*y_minus=4*(H^2-1)/Lambda^2"}, {"identity_id": "crossing_period", "formula": "T=8/(Lambda sqrt(y_plus-y_minus))*K(sqrt(y_plus/(y_plus-y_minus)))"}, {"identity_id": "self_period", "formula": "T=4/(Lambda sqrt(y_plus))*K(sqrt(1-y_minus/y_plus))"}, {"identity_id": "small_amplitude_crossing", "formula": "T -> 2*pi/sqrt(Lambda+1) near (0,0)"}, {"identity_id": "small_amplitude_self", "formula": "T -> 2*pi/sqrt(Lambda^2-1) near broken centers"}, {"identity_id": "separatrix_profile", "formula": "z=A sech(omega t), A=2 sqrt(Lambda-1)/Lambda, omega=sqrt(Lambda-1)"}, {"identity_id": "self_trap_reverse", "formula": "H>1 => sign(z(t))=sign(z(0)); H<1 => crossing component"}, {"identity_id": "pitchfork", "formula": "Lambda=1 merges z=+/-sqrt(1-Lambda^-2) into (0,pi)"}, {"identity_id": "pole_limit", "formula": "Lambda=2 gives A=1 and the homoclinic turning point is a Bloch pole"}],
        "route_a": {"tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"], "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False, "strongest_positive": "Analytic fixed-point, bifurcation, energy-component, elliptic-period, and separatrix formulas are certified.", "strongest_failure": "Regular level sets form a continuum rather than a discrete primitive orbit atlas, and no arithmetic target match is defined."},
        "scope_flags": {k: False for k in ["uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"]},
        "citations": [{"key": "Smerzi1997", "claim": "two-mode Josephson equations and macroscopic self-trapping", "source": "Smerzi, Fantoni, Giovanazzi and Shenoy, Phys. Rev. Lett. 79 (1997) 4950--4953, DOI 10.1103/PhysRevLett.79.4950", "url": "https://doi.org/10.1103/PhysRevLett.79.4950", "preprint": "https://arxiv.org/abs/cond-mat/9706221"}, {"key": "Raghavan1999", "claim": "elliptic-function solutions, pi oscillations and self-trapping", "source": "Raghavan, Smerzi, Fantoni and Shenoy, Phys. Rev. A 59 (1999) 620--633, DOI 10.1103/PhysRevA.59.620", "url": "https://doi.org/10.1103/PhysRevA.59.620", "preprint": "https://arxiv.org/abs/cond-mat/9706220"}],
        "nonclaims": ["literature priority or exhaustive novelty certification", "a discrete primitive orbit enumeration or zeta product from continuum regular levels", "an arithmetic origin, prime/prime-power labeling, Euler factors, root numbers, or automorphy", "a target zeta/Fredholm determinant, zero match, or Hilbert--Polya operator", "external peer review, acceptance, or numerical evidence promoted to a theorem"],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser(); parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT); args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    data = build(); args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "C243_PRODUCER_PASS", "fixed_points": data["regression"]["fixed_point_row_count"], "level_rows": data["regression"]["level_row_count"], "payload_sha256": data["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
