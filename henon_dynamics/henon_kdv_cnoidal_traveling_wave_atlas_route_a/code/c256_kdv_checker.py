#!/usr/bin/env python3
"""Producer-independent structural, exact, and quadrature checker for C256."""
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
DEFAULT = ROOT / "results/c256_kdv_evidence.json"
SOURCE = "b89544f1f7b1043f4158dfdf9db77787b332f146"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788048000
mp.mp.dps = 85
NUM = re.compile(r"^[+-]?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?$")
TOP = {"schema", "candidate_id", "evaluation_date", "source_commit", "fixed_epoch", "scope_literal", "evaluator", "headline", "frozen_object", "theorem", "receipts", "exact_identities", "route_a", "scope_flags", "citations", "nonclaims", "payload_sha256"}
FLAGS = {"uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"}
ROOT_TRIPLES = [(-5, -2, 1), (-4, 1, 2), (-3, -1, 2), (-2, 0, 3), (-2, 3, 7), (-1, 0, 1), (-1, 1, 4), (0, 1, 2), (0, 1, 3), (0, 2, 5), (1, 2, 4), (2, 5, 9)]


def ph(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def q(value: str) -> F:
    if not isinstance(value, str):
        raise AssertionError("rational is not text")
    return F(value)


def m(value: str) -> mp.mpf:
    if not isinstance(value, str) or NUM.fullmatch(value) is None:
        raise AssertionError("decimal syntax")
    out = mp.mpf(value)
    if not mp.isfinite(out):
        raise AssertionError("nonfinite decimal")
    return out


def close(a: mp.mpf, b: mp.mpf, tol: mp.mpf = mp.mpf("2e-68")) -> bool:
    return abs(a - b) <= tol * max(mp.mpf(1), abs(a), abs(b))


def validate(data: dict, reconstruct: bool = True) -> int:
    checks = 0

    def ck(ok: bool, label: str) -> None:
        nonlocal checks
        checks += 1
        if not ok:
            raise AssertionError(label)

    def eq(a, b, label: str) -> None:
        ck(type(a) is type(b) and a == b, label)

    eq(set(data), TOP, "top closure")
    for key, value in (("schema", "hcs-c256-kdv-cnoidal-traveling-wave-atlas-v1"), ("candidate_id", "HCS-C256"), ("evaluation_date", "2026-08-31"), ("source_commit", SOURCE), ("fixed_epoch", EPOCH), ("scope_literal", SCOPE)):
        eq(data[key], value, key)
    eq(data["evaluator"], {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR}, "evaluator")
    eq(data["payload_sha256"], ph(data), "payload hash")
    frozen = data["frozen_object"]
    expected_frozen = {
        "equation": "u_t+6*u*u_x+u_xxx=0",
        "phase_space": "real classical profiles U(x-c*t) on R, with the periodic profile also read on its fundamental circle",
        "traveling_coordinate": "xi=x-c*t",
        "clock": "physical PDE time t; a nonstationary wave on its fundamental circle returns after L/abs(c)",
        "parameters": "real integration constants, equivalently ordered cubic roots including their double/triple-root faces",
        "arithmetic_origin": "none; continuously tunable dispersive-wave roots",
        "determinant_convention": "none; the auxiliary KdV Lax operator is only a formal A4 hint",
    }
    for key, value in expected_frozen.items():
        eq(frozen.get(key), value, "frozen " + key)
    ck("target primes/zeros" in frozen["forbidden_data"], "forbidden data")

    theorem = data["theorem"]
    theorem_expected = {
        "first_integral": "Every traveling profile satisfies U''=c*U-3*U^2+A and (U')^2=-2*U^3+c*U^2+2*A*U+B.",
        "bounded_classification": "A nonconstant bounded entire real profile exists exactly when the energy cubic has three real roots r1<r2<r3 and oscillates on [r2,r3], or on the lower-double-root homoclinic face r1=r2<r3; all other bounded entire profiles are constants.",
        "periodic_formula": "For r1<r2<r3, c=2*(r1+r2+r3), m=(r3-r2)/(r3-r1), k=sqrt((r3-r1)/2), and U=r2+(r3-r2)*cn^2(k*xi;m).",
        "period_and_mean": "The fundamental spatial period is L=2*sqrt(2/(r3-r1))*K(m), and the period mean is r1+(r3-r1)*E(m)/K(m).",
        "soliton_face": "As r2 decreases to r1, U tends to r1+(r3-r1)*sech^2(sqrt((r3-r1)/2)*xi), with speed 2*(2*r1+r3).",
        "harmonic_face": "As r2 increases to r3 with r1 fixed, amplitude vanishes and L tends to 2*pi/sqrt(2*(r3-r1)); the limiting constant itself has no selected traveling speed.",
        "galilean": "If u solves KdV, then u(x-6*a*t,t)+a solves it; every root shifts by a and c shifts by 6*a.",
        "temporal_return": "On the circle of fundamental length L, c!=0 gives a periodic PDE orbit of primitive time L/abs(c); c=0 gives a stationary profile.",
        "scope": "The classification is for bounded classical traveling profiles, not every KdV solution and not a nonlinear stability theorem.",
    }
    eq(set(theorem), set(theorem_expected), "theorem key closure")
    for key, value in theorem_expected.items():
        eq(theorem[key], value, "theorem " + key)

    route = data["route_a"]
    eq(route["tuple"], ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "route tuple")
    eq(route["overall"], "ROUTE_A_REJECTED", "route overall")
    eq(route["route_b_invocation_allowed"], False, "route B")
    ck("no intrinsic arithmetic" in route["strongest_failure"].lower(), "route failure")
    eq(set(data["scope_flags"]), FLAGS, "flag closure")
    ck(all(v is False for v in data["scope_flags"].values()), "flags false")

    receipts = data["receipts"]
    eq(receipts["periodic_row_count"], 12, "periodic count")
    eq(receipts["soliton_row_count"], 3, "soliton count")
    eq(receipts["harmonic_row_count"], 3, "harmonic count")
    eq(receipts["galilean_row_count"], 6, "galilean count")
    eq(receipts["working_decimal_digits"], 90, "working digits")
    eq(receipts["printed_significant_digits"], 75, "printed digits")
    ck("proof-driven" in receipts["finite_receipt_boundary"], "receipt boundary")
    pkeys = {"row_id", "roots", "root_order", "speed", "pair_sum", "modulus_m", "amplitude", "wave_number", "K", "E", "fundamental_period", "period_mean", "period_mean_square", "max_first_integral_residual_17_nodes", "max_profile_ode_residual_17_nodes"}
    eq(len(receipts["periodic_rows"]), 12, "periodic length")
    for idx, (row, expected_roots) in enumerate(zip(receipts["periodic_rows"], ROOT_TRIPLES), 1):
        eq(set(row), pkeys, f"P{idx} keys")
        eq(row["row_id"], f"P{idx:02d}", f"P{idx} id")
        rootsq = tuple(q(x) for x in row["roots"])
        eq(rootsq, tuple(F(x) for x in expected_roots), f"P{idx} roots")
        r1q, r2q, r3q = rootsq
        ck(r1q < r2q < r3q and row["root_order"] == "r1<r2<r3", f"P{idx} order")
        Dq, dq = r3q - r1q, r3q - r2q
        eq(q(row["speed"]), 2 * (r1q + r2q + r3q), f"P{idx} speed")
        eq(q(row["pair_sum"]), r1q*r2q + r1q*r3q + r2q*r3q, f"P{idx} pair")
        eq(q(row["modulus_m"]), dq / Dq, f"P{idx} modulus exact")
        eq(q(row["amplitude"]), dq, f"P{idx} amplitude")
        r1, r2, r3 = (mp.mpf(x.numerator) / x.denominator for x in rootsq)
        D, d = r3-r1, r3-r2
        mod = d/D
        k = mp.sqrt(D/2)
        K, E = mp.ellipk(mod), mp.ellipe(mod)
        L = 2*K/k
        mean = r1 + D*E/K
        avgcn2 = (E-(1-mod)*K)/(mod*K)
        avgsn2 = (K-E)/(mod*K)
        avgsn4 = ((2+mod)*K-2*(1+mod)*E)/(3*mod*mod*K)
        avgcn4 = 1-2*avgsn2+avgsn4
        mean2 = r2*r2 + 2*r2*d*avgcn2 + d*d*avgcn4
        for field, expected in (("wave_number", k), ("K", K), ("E", E), ("fundamental_period", L), ("period_mean", mean), ("period_mean_square", mean2)):
            ck(close(m(row[field]), expected), f"P{idx} {field}")
        ck(abs(m(row["max_first_integral_residual_17_nodes"])) < mp.mpf("1e-65"), f"P{idx} energy residual")
        ck(abs(m(row["max_profile_ode_residual_17_nodes"])) < mp.mpf("1e-65"), f"P{idx} ODE residual")
        if reconstruct:
            # Endpoint-regularized quadrature, independent of the cn formula.
            w = lambda th: 1/mp.sqrt((r2-r1)+d*mp.sin(th)**2)
            i0 = mp.quad(w, [0, mp.pi/4, mp.pi/2])
            i1 = mp.quad(lambda th: (r2+d*mp.sin(th)**2)*w(th), [0, mp.pi/4, mp.pi/2])
            i2 = mp.quad(lambda th: (r2+d*mp.sin(th)**2)**2*w(th), [0, mp.pi/4, mp.pi/2])
            ck(close(2*mp.sqrt(2)*i0, L, mp.mpf("3e-65")), f"P{idx} quadrature period")
            ck(close(i1/i0, mean, mp.mpf("3e-65")), f"P{idx} quadrature mean")
            ck(close(i2/i0, mean2, mp.mpf("3e-65")), f"P{idx} quadrature mean2")
            c = mp.mpf(q(row["speed"]).numerator)/q(row["speed"]).denominator
            pair = mp.mpf(q(row["pair_sum"]).numerator)/q(row["pair_sum"]).denominator
            for j in range(9):
                xi = L*mp.mpf(j)/9
                ss = k*xi
                cn, sn, dn = mp.ellipfun("cn", ss, mod), mp.ellipfun("sn", ss, mod), mp.ellipfun("dn", ss, mod)
                qq = cn*cn
                U = r2+d*qq
                Up = -2*d*k*cn*sn*dn
                poly = 2*(r3-U)*(U-r2)*(U-r1)
                fp = 4*((1-2*qq)*(1-mod+mod*qq)+mod*qq*(1-qq))
                Upp = d*k*k*fp/2
                ck(abs(Up*Up-poly) < mp.mpf("2e-70"), f"P{idx} cn energy {j}")
                ck(abs(Upp-(c*U-3*U*U-pair)) < mp.mpf("2e-70"), f"P{idx} cn ODE {j}")

    skeys = {"row_id", "r1_equals_r2", "r3", "speed", "height_above_background", "inverse_width", "excess_mass", "profile"}
    sols = [(-2, 1), (0, 2), (1, 4)]
    for idx, (row, (a0, b0)) in enumerate(zip(receipts["soliton_rows"], sols), 1):
        eq(set(row), skeys, f"S{idx} keys")
        eq(row["row_id"], f"S{idx}", f"S{idx} id")
        a, b = F(a0), F(b0)
        eq(q(row["r1_equals_r2"]), a, f"S{idx} lower")
        eq(q(row["r3"]), b, f"S{idx} upper")
        eq(q(row["speed"]), 2*(2*a+b), f"S{idx} speed")
        eq(q(row["height_above_background"]), b-a, f"S{idx} height")
        kk = mp.sqrt(mp.mpf((b-a).numerator)/(2*(b-a).denominator))
        ck(close(m(row["inverse_width"]), kk), f"S{idx} width")
        ck(close(m(row["excess_mass"]), 2*(mp.mpf((b-a).numerator)/(b-a).denominator)/kk), f"S{idx} mass")
        ck("sech^2" in row["profile"], f"S{idx} profile")

    hkeys = {"row_id", "r1", "r2_equals_r3", "constant_level", "limiting_angular_frequency", "limiting_period", "qualification"}
    harms = [(-3, 1), (0, 2), (2, 5)]
    for idx, (row, (a0, b0)) in enumerate(zip(receipts["harmonic_rows"], harms), 1):
        eq(set(row), hkeys, f"H{idx} keys")
        a, b = F(a0), F(b0)
        eq(row["row_id"], f"H{idx}", f"H{idx} id")
        eq(q(row["r1"]), a, f"H{idx} r1")
        eq(q(row["r2_equals_r3"]), b, f"H{idx} upper")
        eq(q(row["constant_level"]), b, f"H{idx} constant")
        om = mp.sqrt(2*mp.mpf((b-a).numerator)/(b-a).denominator)
        ck(close(m(row["limiting_angular_frequency"]), om), f"H{idx} omega")
        ck(close(m(row["limiting_period"]), 2*mp.pi/om), f"H{idx} period")
        ck("selects no speed" in row["qualification"], f"H{idx} qualification")

    gkeys = {"row_id", "shift_a", "base_roots", "shifted_roots", "base_speed", "shifted_speed", "speed_increment", "profile_increment"}
    shifts = [F(-3), F(-1), F(1,2), F(1), F(2), F(4)]
    base = (F(-1), F(0), F(2))
    c0 = 2*sum(base, F(0))
    for idx, (row, shift) in enumerate(zip(receipts["galilean_rows"], shifts), 1):
        eq(set(row), gkeys, f"G{idx} keys")
        eq(row["row_id"], f"G{idx}", f"G{idx} id")
        eq(q(row["shift_a"]), shift, f"G{idx} shift")
        eq(tuple(q(x) for x in row["base_roots"]), base, f"G{idx} base")
        shifted = tuple(x+shift for x in base)
        eq(tuple(q(x) for x in row["shifted_roots"]), shifted, f"G{idx} shifted")
        eq(q(row["base_speed"]), c0, f"G{idx} c0")
        eq(q(row["shifted_speed"]), c0+6*shift, f"G{idx} cshift")
        eq(q(row["speed_increment"]), 6*shift, f"G{idx} dc")
        eq(q(row["profile_increment"]), shift, f"G{idx} du")

    ids = {row["id"]: row["formula"] for row in data["exact_identities"]}
    eq(len(ids), 14, "identity count")
    for key, value in {
        "profile_ode": "U''=c*U-3*U^2+A", "speed": "c=2*(r1+r2+r3)",
        "period": "L=2*sqrt(2/(r3-r1))*K(m)", "mean": "mean(U)=r1+(r3-r1)*E(m)/K(m)",
        "circle_clock": "T=L/abs(c) for c!=0 on the fundamental circle; c=0 is stationary",
    }.items():
        eq(ids.get(key), value, "identity " + key)
    eq(len(data["citations"]), 3, "citation count")
    eq(data["citations"][0]["url"], "https://doi.org/10.1080/14786449508620739", "original DOI")
    eq(data["citations"][1]["url"], "https://doi.org/10.1002/mana.201300233", "cnoidal DOI")
    eq(data["citations"][2]["url"], "https://doi.org/10.1002/cpa.3160210503", "Lax DOI")
    eq(len(data["nonclaims"]), 6, "nonclaim count")
    ck(any("literature priority" in x for x in data["nonclaims"]), "priority nonclaim")
    return checks


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--evidence", type=Path, default=DEFAULT)
    ap.add_argument("--quick", action="store_true")
    args = ap.parse_args()
    data = json.loads(args.evidence.read_text())
    count = validate(data, reconstruct=not args.quick)
    if args.quick:
        print(f"C256 quick hostile preflight: PASS ({count} assertions)")
    else:
        print(f"C256 independent checker: PASS ({count} assertions; root atlas, quadratures, boundaries, Galilean covariance)")


if __name__ == "__main__":
    main()
