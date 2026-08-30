#!/usr/bin/env python3
"""Producer-independent checker for the C243 dimer phase portrait."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
import math
from pathlib import Path
import re

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c243_dimer_evidence.json"
SOURCE_COMMIT = "489506cf92bfed721f94f22dd0444a60427f90a5"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
FIXED_EPOCH = 1788048000
SERIALIZED_DIGITS = 64
mp.mp.dps = 90
NUM_RE = re.compile(r"^-?(?:0|[1-9][0-9]*)(?:\.[0-9]+|[eE][+-]?[0-9]+)$")
TOP_KEYS = {"schema", "candidate_id", "evaluation_date", "source_commit", "fixed_epoch", "scope_literal", "evaluator", "headline", "frozen_object", "theorem", "regression", "exact_identities", "route_a", "scope_flags", "citations", "nonclaims", "payload_sha256"}
SCOPE_KEYS = {"uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"}
LEVEL_CASES = [("L0_hminus1_2", F(0), F(-1, 2)), ("L0_hplus1_2", F(0), F(1, 2)), ("Lhalf_cross_minus", F(1, 2), F(-1, 2)), ("Lhalf_cross_plus", F(1, 2), F(1, 2)), ("L1_cross_minus", F(1), F(-1, 2)), ("L1_cross_plus", F(1), F(1, 2)), ("L1_pitchfork", F(1), F(1)), ("L2_cross", F(2), F(-1, 2)), ("L2_sep", F(2), F(1)), ("L2_self", F(2), F(11, 10)), ("L3_cross", F(3), F(0)), ("L3_sep", F(3), F(1)), ("L3_self", F(3), F(6, 5))]
CRITERION_CASES = [{"case_id": "crossing_regular", "lambda": "2", "energy": "1/2", "initial_sign": "+", "criterion": "H<1", "verdict": "crossing", "reverse_condition": "H<1 gives a one-component level and both signs are reached"}, {"case_id": "self_trapped_positive", "lambda": "2", "energy": "11/10", "initial_sign": "+", "criterion": "H>1 and H<h_max", "verdict": "self_trapped", "reverse_condition": "sign(z(t))=sign(z(0))"}, {"case_id": "self_trapped_negative", "lambda": "2", "energy": "11/10", "initial_sign": "-", "criterion": "H>1 and H<h_max", "verdict": "self_trapped", "reverse_condition": "sign(z(t))=sign(z(0))"}, {"case_id": "separatrix_plus", "lambda": "3", "energy": "1", "initial_sign": "+", "criterion": "H=1", "verdict": "separatrix_one_sided", "reverse_condition": "approaches z=0 asymptotically; no finite crossing"}, {"case_id": "lambda1_boundary", "lambda": "1", "energy": "1", "initial_sign": "+", "criterion": "Lambda=1,H=1", "verdict": "pitchfork_critical_point", "reverse_condition": "isolated degenerate point z=0; no regular separatrix"}]


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def dec(x: mp.mpf) -> str:
    if abs(x) < mp.mpf("1e-82"):
        x = mp.mpf("0")
    return mp.nstr(x, SERIALIZED_DIGITS, strip_zeros=False, min_fixed=-70, max_fixed=70)


def mpq(q: F | int) -> mp.mpf:
    q = q if isinstance(q, F) else F(q)
    return mp.mpf(q.numerator) / q.denominator


def ftext(q: F | int) -> str:
    q = q if isinstance(q, F) else F(q)
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def close_num(value: object, expected: mp.mpf, label: str, check) -> None:
    ok = isinstance(value, str) and NUM_RE.fullmatch(value) is not None
    check(ok, label + " syntax")
    if ok:
        check(abs(mp.mpf(value) - expected) <= mp.mpf("4e-40") * max(1, abs(expected)), label + " value")


def validate(data: dict) -> int:
    checks = 0

    def check(ok: bool, label: str) -> None:
        nonlocal checks
        checks += 1
        if not ok:
            raise AssertionError(label)

    def exact(actual, expected, label: str) -> None:
        check(type(actual) is type(expected), label + " type")
        check(actual == expected, label)

    check(set(data) == TOP_KEYS, "top closure")
    exact(data["schema"], "hcs-c243-bose-josephson-dimer-phase-portrait-v1", "schema")
    exact(data["candidate_id"], "HCS-C243", "candidate")
    exact(data["evaluation_date"], "2026-08-30", "date")
    exact(data["source_commit"], SOURCE_COMMIT, "source lock")
    exact(data["fixed_epoch"], FIXED_EPOCH, "epoch")
    exact(data["scope_literal"], SCOPE, "scope")
    exact(data["evaluator"], {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256}, "evaluator lock")
    check(data["payload_sha256"] == payload_hash(data), "payload hash")
    exact(data["route_a"]["tuple"], ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"], "route tuple")
    check(data["route_a"]["overall"] == "ROUTE_A_REJECTED" and data["route_a"]["route_b_invocation_allowed"] is False, "route boundary")
    check(set(data["scope_flags"]) == SCOPE_KEYS and all(v is False for v in data["scope_flags"].values()), "scope firewall")
    check(data["regression"]["working_digits"] == 90 and data["regression"]["serialized_digits"] == 64, "precision")
    check("two sign components" in data["theorem"]["self_trapping"] and "H>1" in data["theorem"]["self_trapping"], "self-trapping theorem")
    check("Lambda=1" in data["theorem"]["boundaries"] and "Lambda=2" in data["theorem"]["boundaries"], "boundary theorem")
    check("2*pi/sqrt(Lambda+1)" in data["theorem"]["small_amplitude_limits"] and "2*pi/sqrt(Lambda^2-1)" in data["theorem"]["small_amplitude_limits"], "small-amplitude limits")

    # Fixed-point atlas, independently rebuilt from the linearizations.
    fixed = data["regression"]["fixed_points"]
    expected_lams = [F(0), F(1, 2), F(1), F(2), F(3)]
    expected_count = 14
    check(len(fixed) == expected_count, "fixed row count")
    fi = 0
    fkeys = {"lambda", "point_id", "z", "phi", "energy", "linearization_matrix", "frequency_squared", "frequency_or_growth", "stability", "symmetry_broken"}
    for lam in expected_lams:
        lm = mpq(lam)
        row = fixed[fi]; fi += 1
        check(set(row) == fkeys, f"fixed {fi} keys")
        exact(row["lambda"], str(lam.numerator) if lam.denominator == 1 else f"{lam.numerator}/{lam.denominator}", f"fixed {fi} lambda")
        exact(row["point_id"], "zero_phase", f"fixed {fi} id"); exact(row["z"], "0", f"fixed {fi} z"); exact(row["phi"], "0", f"fixed {fi} phi"); exact(row["energy"], "-1", f"fixed {fi} energy"); exact(row["linearization_matrix"], "[[0,-1],[Lambda+1,0]]", f"fixed {fi} matrix"); exact(row["frequency_squared"], str(lam + 1) if (lam + 1).denominator == 1 else f"{(lam+1).numerator}/{(lam+1).denominator}", f"fixed {fi} freq sq"); close_num(row["frequency_or_growth"], mp.sqrt(lm + 1), f"fixed {fi} freq", check); exact(row["stability"], "elliptic", f"fixed {fi} stability"); exact(row["symmetry_broken"], False, f"fixed {fi} symmetry")
        row = fixed[fi]; fi += 1
        check(set(row) == fkeys, f"fixed {fi} keys")
        exact(row["lambda"], str(lam.numerator) if lam.denominator == 1 else f"{lam.numerator}/{lam.denominator}", f"fixed {fi} lambda"); exact(row["point_id"], "pi_symmetric", f"fixed {fi} id"); exact(row["z"], "0", f"fixed {fi} z"); exact(row["phi"], "pi", f"fixed {fi} phi"); exact(row["energy"], "1", f"fixed {fi} energy"); exact(row["linearization_matrix"], "[[0,1],[Lambda-1,0]]", f"fixed {fi} matrix")
        if lam < 1:
            stab, fsq, fg = "elliptic", (1 - lam), mp.sqrt(1 - lm)
            fs = str(fsq.numerator) if fsq.denominator == 1 else f"{fsq.numerator}/{fsq.denominator}"
            close_num(row["frequency_or_growth"], fg, f"fixed {fi} freq", check)
        elif lam == 1:
            stab, fs = "parabolic_pitchfork", "0"; exact(row["frequency_or_growth"], "0.0", f"fixed {fi} zero growth")
        else:
            stab, fsq, fg = "hyperbolic", lam - 1, mp.sqrt(lm - 1)
            fs = str(fsq.numerator) if fsq.denominator == 1 else f"{fsq.numerator}/{fsq.denominator}"
            close_num(row["frequency_or_growth"], fg, f"fixed {fi} growth", check)
        exact(row["frequency_squared"], fs, f"fixed {fi} freq sq"); exact(row["stability"], stab, f"fixed {fi} stability"); exact(row["symmetry_broken"], False, f"fixed {fi} symmetry")
        if lam > 1:
            for sign, sid in (("+", "broken_plus"), ("-", "broken_minus")):
                row = fixed[fi]; fi += 1
                check(set(row) == fkeys, f"fixed {fi} keys")
                exact(row["lambda"], str(lam), f"fixed {fi} lambda"); exact(row["point_id"], sid, f"fixed {fi} id"); exact(row["z"], sign + "sqrt(1-Lambda^-2)", f"fixed {fi} z"); exact(row["phi"], "pi", f"fixed {fi} phi"); exact(row["energy"], f"({str(lam)}+1/{str(lam)})/2", f"fixed {fi} energy"); exact(row["linearization_matrix"], "[[0,1/Lambda],[-Lambda*(Lambda^2-1),0]]", f"fixed {fi} matrix"); exact(row["frequency_squared"], str(lam*lam-1), f"fixed {fi} freq sq"); close_num(row["frequency_or_growth"], mp.sqrt(lm*lm-1), f"fixed {fi} freq", check); exact(row["stability"], "elliptic", f"fixed {fi} stability"); exact(row["symmetry_broken"], True, f"fixed {fi} symmetry")
    exact(fi, expected_count, "fixed traversal")

    poles = data["regression"]["bloch_poles"]
    pkeys = {"lambda", "point_id", "x", "y", "z", "xdot", "ydot", "zdot", "chart"}
    check(len(poles) == 8, "pole row count")
    pi = 0
    for lam in (F(0), F(1), F(2), F(3)):
        for sign in (1, -1):
            row = poles[pi]; pi += 1
            check(set(row) == pkeys, f"pole {pi} keys"); exact(row["lambda"], ftext(lam), f"pole {pi} lambda"); exact(row["point_id"], "north_pole" if sign == 1 else "south_pole", f"pole {pi} id"); exact(row["x"], "0", f"pole {pi} x"); exact(row["y"], "0", f"pole {pi} y"); exact(row["z"], str(sign), f"pole {pi} z"); exact(row["xdot"], "0", f"pole {pi} xdot"); exact(row["ydot"], str(sign), f"pole {pi} ydot"); exact(row["zdot"], "0", f"pole {pi} zdot"); exact(row["chart"], "Bloch_vector", f"pole {pi} chart")

    level_keys = {"case_id", "lambda", "energy", "root_formula", "quadrature_integral", "elliptic_reduction", "y_minus", "y_plus", "elliptic_modulus", "period", "period_formula", "allowed_interval", "sign_components", "component_verdict", "crosses_zero", "separatrix_profile", "turning_phase", "pole_coordinate_warning", "level_type"}
    levels = data["regression"]["level_rows"]
    check(len(levels) == len(LEVEL_CASES), "level row count")
    for i, (cid, lam, h) in enumerate(LEVEL_CASES):
        row = levels[i]; check(set(row) == level_keys, f"level {i} keys"); exact(row["case_id"], cid, f"level {i} id"); exact(row["lambda"], str(lam), f"level {i} lambda"); exact(row["energy"], str(h), f"level {i} energy"); exact(row["root_formula"], "y_pm=2*(Lambda*H-1 +/- sqrt(Lambda^2-2*Lambda*H+1))/Lambda^2", f"level {i} roots formula"); exact(row["quadrature_integral"], "dt=2 dz/(Lambda sqrt((y_plus-z^2)(z^2-y_minus)))", f"level {i} quadrature"); exact(row["elliptic_reduction"], "complete elliptic K with the displayed modulus", f"level {i} K reduction")
        lm, hm = mpq(lam), mpq(h)
        if lam == 0:
            exact(row["level_type"], "regular_sphere_rotation", f"level {i} type"); exact(row["y_minus"], None, f"level {i} y-"); exact(row["y_plus"], None, f"level {i} y+"); exact(row["elliptic_modulus"], None, f"level {i} modulus"); close_num(row["period"], 2*mp.pi, f"level {i} period", check); exact(row["period_formula"], "2*pi", f"level {i} formula"); exact(row["allowed_interval"], "Bloch circle x=-H", f"level {i} interval"); exact(row["sign_components"], 1, f"level {i} components"); exact(row["component_verdict"], "sphere_rotation", f"level {i} verdict"); exact(row["crosses_zero"], True, f"level {i} crossing"); exact(row["separatrix_profile"], None, f"level {i} profile"); exact(row["turning_phase"], None, f"level {i} phase"); exact(row["pole_coordinate_warning"], False, f"level {i} pole warning"); continue
        disc = lm*lm - 2*lm*hm + 1; delta = mp.sqrt(disc); ym = 2*(lm*hm-1-delta)/(lm*lm); yp = 2*(lm*hm-1+delta)/(lm*lm)
        close_num(row["y_minus"], ym, f"level {i} y-", check); close_num(row["y_plus"], yp, f"level {i} y+", check)
        if lam == 1 and h == 1:
            exact(row["level_type"], "pitchfork_critical_point", f"level {i} type"); exact(row["period"], None, f"level {i} period"); exact(row["elliptic_modulus"], None, f"level {i} modulus"); exact(row["period_formula"], "none (isolated degenerate point)", f"level {i} formula"); exact(row["allowed_interval"], "z=0 only (z_dot^2=-z^4/4)", f"level {i} interval"); exact(row["sign_components"], 1, f"level {i} components"); exact(row["component_verdict"], "pitchfork_critical_point", f"level {i} verdict"); exact(row["crosses_zero"], False, f"level {i} crossing"); exact(row["separatrix_profile"], None, f"level {i} profile"); exact(row["turning_phase"], None, f"level {i} phase"); exact(row["pole_coordinate_warning"], False, f"level {i} pole"); continue
        if lam > 1 and h == 1:
            A=2*mp.sqrt(lm-1)/lm; om=mp.sqrt(lm-1); turn="pi" if lam<2 else ("pole" if lam==2 else "0")
            exact(row["level_type"], "separatrix", f"level {i} type"); exact(row["elliptic_modulus"], None, f"level {i} modulus"); exact(row["period"], None, f"level {i} period"); exact(row["period_formula"], "infinite (homoclinic)", f"level {i} formula"); exact(row["allowed_interval"], f"connected full level; two one-sided branches 0<|z|<={dec(A)}", f"level {i} interval"); exact(row["sign_components"], 1, f"level {i} components"); exact(row["component_verdict"], "separatrix_one_sided", f"level {i} verdict"); exact(row["crosses_zero"], False, f"level {i} crossing"); exact(row["separatrix_profile"], f"z(t)=+/- {dec(A)} sech({dec(om)} t)", f"level {i} profile"); exact(row["turning_phase"], turn, f"level {i} phase"); exact(row["pole_coordinate_warning"], lam == 2, f"level {i} pole"); continue
        if lam > 1 and h > 1 and hm < (lm+1/lm)/2:
            mod=mp.sqrt(1-ym/yp); per=4/(lm*mp.sqrt(yp))*mp.ellipk(mod*mod)
            exact(row["level_type"], "regular_self_trapped", f"level {i} type"); close_num(row["elliptic_modulus"], mod, f"level {i} modulus", check); close_num(row["period"], per, f"level {i} period", check); exact(row["period_formula"], "4/(Lambda*sqrt(y_plus))*K(sqrt(1-y_minus/y_plus))", f"level {i} formula"); exact(row["allowed_interval"], "[sqrt(y_minus),sqrt(y_plus)] union -[sqrt(y_minus),sqrt(y_plus)]", f"level {i} interval"); exact(row["sign_components"], 2, f"level {i} components"); exact(row["component_verdict"], "self_trapped", f"level {i} verdict"); exact(row["crosses_zero"], False, f"level {i} crossing"); exact(row["separatrix_profile"], None, f"level {i} profile"); exact(row["turning_phase"], None, f"level {i} phase"); exact(row["pole_coordinate_warning"], False, f"level {i} pole"); continue
        mod=mp.sqrt(yp/(yp-ym)); per=8/(lm*mp.sqrt(yp-ym))*mp.ellipk(mod*mod)
        exact(row["level_type"], "regular_crossing", f"level {i} type"); close_num(row["elliptic_modulus"], mod, f"level {i} modulus", check); close_num(row["period"], per, f"level {i} period", check); exact(row["period_formula"], "8/(Lambda*sqrt(y_plus-y_minus))*K(sqrt(y_plus/(y_plus-y_minus)))", f"level {i} formula"); exact(row["allowed_interval"], "[-sqrt(y_plus),sqrt(y_plus)]", f"level {i} interval"); exact(row["sign_components"], 1, f"level {i} components"); exact(row["component_verdict"], "crossing", f"level {i} verdict"); exact(row["crosses_zero"], True, f"level {i} crossing"); exact(row["separatrix_profile"], None, f"level {i} profile"); exact(row["turning_phase"], None, f"level {i} phase"); exact(row["pole_coordinate_warning"], False, f"level {i} pole")

    exact(data["regression"]["fixed_point_row_count"], 14, "fixed summary"); exact(data["regression"]["bloch_pole_row_count"], 8, "pole summary"); exact(data["regression"]["level_row_count"], 13, "level summary"); exact(data["regression"]["criterion_row_count"], 5, "criterion summary"); exact(data["regression"]["criterion_rows"], CRITERION_CASES, "criterion rows")
    check(len(data["exact_identities"]) == 14, "identity count"); check(len(data["citations"]) == 2 and all(set(c) == {"key", "claim", "source", "url", "preprint"} for c in data["citations"]), "citation closure"); check(len(data["nonclaims"]) == 5 and all(isinstance(x, str) for x in data["nonclaims"]), "nonclaim closure")
    return checks


def quick_preflight(data: dict) -> None:
    assert set(data) == TOP_KEYS and data["candidate_id"] == "HCS-C243" and data["payload_sha256"] == payload_hash(data)
    assert data["route_a"]["tuple"] == ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"]
    print("C243 quick hostile preflight: PASS")


def main() -> None:
    parser = argparse.ArgumentParser(); parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE); parser.add_argument("--quick", action="store_true"); args = parser.parse_args(); data = json.loads(args.evidence.read_text())
    if args.quick: quick_preflight(data)
    else: print(f"C243 independent checker: PASS ({validate(data)} assertions; fixed points, elliptic periods and component criteria)")


if __name__ == "__main__": main()
