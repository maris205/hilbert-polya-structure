#!/usr/bin/env python3
"""Producer-independent exact/ODE audit for HCS-C224."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c224_landau_zener_evidence.json"
SOURCE_COMMIT = "489672bd36abd3a4f6da92d1446a0af575917959"
EVALUATOR = {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"}
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
HEADLINE = "Landau--Zener--Weber crossing has exact asymptotic scattering, Stokes phase, monotonicity, and finite-window unitary controls"
PARAMETERS = [("reference", F(1), F(1, 2)), ("fast_weak", F(4), F(1, 3)), ("slow_strong", F(1, 4), F(3, 4)), ("negative_g", F(2), F(-1, 2)), ("uncoupled", F(3, 2), F(0))]
WINDOWS = [F(2), F(4), F(8)]
RK_STEPS = 2048
TOL = mp.mpf("1e-60")


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def mpq(x: F | int) -> mp.mpf:
    return mp.mpf(x.numerator) / x.denominator if isinstance(x, F) else mp.mpf(x)


def close(a: str | mp.mpf, b: mp.mpf, tol: mp.mpf = TOL) -> bool:
    return abs(mp.mpf(a) - b) < tol


def rhs(t, y, v, g):
    a, b = y
    z = v * t / 2
    return (-1j * (z * a + g * b), -1j * (g * a - z * b))


def step(t, y, h, v, g):
    k1 = rhs(t, y, v, g)
    k2 = rhs(t + h / 2, (y[0] + h*k1[0]/2, y[1] + h*k1[1]/2), v, g)
    k3 = rhs(t + h / 2, (y[0] + h*k2[0]/2, y[1] + h*k2[1]/2), v, g)
    k4 = rhs(t + h, (y[0] + h*k3[0], y[1] + h*k3[1]), v, g)
    return tuple(y[i] + h*(k1[i] + 2*k2[i] + 2*k3[i] + k4[i])/6 for i in (0, 1))


def finite_propagator(v, g, T):
    h = 2*T/RK_STEPS
    cols = []
    for initial in ((1+0j, 0+0j), (0+0j, 1+0j)):
        y = (mp.mpc(initial[0]), mp.mpc(initial[1])); t = -T
        for _ in range(RK_STEPS):
            y = step(t, y, h, v, g); t += h
        cols.append(y)
    return ((cols[0][0], cols[1][0]), (cols[0][1], cols[1][1]))


def residual(U):
    return max(abs(sum(mp.conj(U[k][i])*U[k][j] for k in range(2)) - (1 if i == j else 0)) for i in range(2) for j in range(2))


def phase(delta):
    return mp.pi/4 if delta == 0 else mp.pi/4 + delta*(mp.log(delta)-1) + mp.im(mp.loggamma(1-1j*delta))


def keys(obj, expected, where, check):
    check(isinstance(obj, dict), where + " must be a mapping")
    check(set(obj) == set(expected), where + " key closure")


def main() -> None:
    parser = argparse.ArgumentParser(); parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    data = json.loads(parser.parse_args().evidence.read_text())
    mp.mp.dps = 80
    assertions = 0
    def check(condition, message):
        nonlocal assertions
        assertions += 1
        if not condition: raise AssertionError(message)

    top = ["schema", "candidate_id", "evaluation_date", "source_commit", "scope_literal", "evaluator", "headline", "frozen_object", "theorem", "regression", "summary", "route_a", "scope_flags", "citations", "nonclaims", "payload_sha256"]
    keys(data, top, "top", check)
    keys(data["evaluator"], ["path", "version", "sha256"], "evaluator", check)
    frozen = ["phase_space", "equation", "parameters", "clock", "normalization", "determinant_convention", "arithmetic_origin", "allowed_data", "forbidden_data", "finite_window_status"]
    theorem = ["weber_reduction", "scattering_probability", "scattering_matrix", "stokes_phase", "unitarity", "monotonicity", "asymptotics", "finite_control", "boundaries", "scope_boundary"]
    keys(data["frozen_object"], frozen, "frozen", check); keys(data["theorem"], theorem, "theorem", check)
    keys(data["regression"], ["parameter_rows", "window_values", "scattering_rows", "finite_window_rows", "boundary_rows"], "regression", check)
    keys(data["summary"], ["parameter_count", "scattering_row_count", "finite_window_row_count", "boundary_row_count", "rk_steps", "working_decimal_digits", "serialized_significant_digits"], "summary", check)
    keys(data["route_a"], ["tuple", "overall", "route_b_invocation_allowed", "strongest_positive", "strongest_failure"], "route", check)
    flags = ["uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"]
    keys(data["scope_flags"], flags, "scope_flags", check)
    check(data["schema"] == "hcs-c224-landau-zener-weber-v1" and data["candidate_id"] == "HCS-C224", "identity")
    check(data["evaluation_date"] == "2026-08-29" and data["source_commit"] == SOURCE_COMMIT, "date/source lock")
    check(data["scope_literal"] == SCOPE and data["evaluator"] == EVALUATOR and data["headline"] == HEADLINE, "scope/evaluator/headline lock")
    expected_frozen = {
        "phase_space": "C^2 with the standard Hermitian norm and a two-channel diabatic basis",
        "equation": "i d_t psi(t)=[(v t/2) sigma_z+g sigma_x] psi(t), with v>0 and real g",
        "parameters": "sweep rate v>0, coupling g in R, physical time t, finite window T>0",
        "clock": "physical laboratory time t; the sweep is nonautonomous and has no fitted target clock",
        "normalization": "sigma_z=diag(1,-1), ||psi||_2=1, hbar=1; scattering gauge fixed by the displayed SU(2) matrix",
        "determinant_convention": "2x2 propagator determinant only; no infinite-dimensional determinant or target divisor",
        "arithmetic_origin": "none; v,g and the Weber index are source parameters with no prime or orbit owner",
        "allowed_data": "exact rational v,g,T sentinels, Gamma/Weber functions, and source-local ODE integration",
        "forbidden_data": "prime or zero tables, target labels, Euler factors, root numbers, automorphy and Route-B input",
        "finite_window_status": "finite-window entries are numerical controls; the exact theorem is the asymptotic scattering law",
    }
    expected_theorem = {
        "weber_reduction": "Eliminating one component and rotating t by exp(-i*pi/4) gives Weber's parabolic-cylinder equation; its connection formula fixes the Stokes multiplier.",
        "scattering_probability": "For delta=g^2/v, the diabatic survival probability is P_diab=exp(-2*pi*delta), with transition probability 1-P_diab.",
        "scattering_matrix": "In the fixed diabatic gauge S=[[sqrt(P),-sqrt(1-P)e^{i phi_S}],[sqrt(1-P)e^{-i phi_S},sqrt(P)]].",
        "stokes_phase": "phi_S=pi/4+delta(log delta-1)+arg Gamma(1-i delta), continuously phi_S(0)=pi/4.",
        "unitarity": "The Weber Wronskian and the Hermitian ODE imply S^*S=I and det S=1 in this gauge.",
        "monotonicity": "P_diab is strictly decreasing in delta>0; dP/ddelta=-2*pi*exp(-2*pi*delta).",
        "asymptotics": "P_diab=1-2*pi*delta+O(delta^2) as delta down to 0 and P_diab~exp(-2*pi*delta) as delta tends to infinity; phi_S has the stated Gamma-controlled limits.",
        "finite_control": "A fixed-step RK4 integration on [-T,T] supplies an independently checkable finite-window propagator and its norm residual; it is not promoted to an exact finite-time Weber formula.",
        "boundaries": "g=0, v down to 0, v tends to infinity, g to -g, T<infinity, and the t=0 turning point are treated separately.",
        "scope_boundary": "The result is a nonautonomous two-level scattering theorem and is distinct from the autonomous Jaynes--Cummings excitation blocks in C223.",
    }
    check(data["frozen_object"] == expected_frozen and data["theorem"] == expected_theorem, "frozen/theorem semantic lock")
    expected_nonclaims = [
        "priority for the Landau--Zener model, Weber functions, or Stokes phases",
        "the finite RK4 grid is an exact finite-time propagator or a proof of an infinite-dimensional theorem",
        "P_diabatic, the Gamma phase, or any crossing parameter is target arithmetic spectral data",
        "a target divisor, Euler factor, root number, automorphy statement, Hilbert--Polya operator, or Route-B authorization",
    ]
    check(data["nonclaims"] == expected_nonclaims, "nonclaim semantic lock")
    expected_route = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_UNITARY_OR_SCATTERING_CANDIDATE"]
    check(data["route_a"]["tuple"] == expected_route and data["route_a"]["overall"] == "ROUTE_A_REJECTED" and data["route_a"]["route_b_invocation_allowed"] is False, "route verdict")
    check(all(value is False for value in data["scope_flags"].values()), "scope flags")
    check(data["payload_sha256"] == payload_hash(data), "payload hash")
    check(data["regression"]["parameter_rows"] == [{"parameter_label": l, "v": str(v), "g": str(g)} for l, v, g in PARAMETERS], "parameter rows")
    check(data["regression"]["window_values"] == [str(x) for x in WINDOWS], "window grid")
    check(data["summary"]["rk_steps"] == RK_STEPS and data["summary"]["parameter_count"] == 5, "summary locks")
    # Validate exact strings and all source-local scattering formulae before any ODE work.
    scat_keys = ["case_id", "v", "g", "adiabaticity_delta", "P_diabatic", "P_adiabatic", "stokes_phase", "stokes_phase_derivative", "S11_real", "S11_imag", "S12_real", "S12_imag", "S21_real", "S21_imag", "S22_real", "S22_imag", "unitarity_residual", "dP_d_delta", "dP_dg_at_fixed_v"]
    check(len(data["regression"]["scattering_rows"]) == len(PARAMETERS), "scattering count")
    scattering = {}
    for i, row in enumerate(data["regression"]["scattering_rows"]):
        keys(row, scat_keys, f"scattering[{i}]", check)
        label, vq, gq = PARAMETERS[i]; check(row["case_id"] == label and row["v"] == str(vq) and row["g"] == str(gq), f"scattering[{i}] identity")
        v, g = mpq(vq), mpq(gq); d = g*g/v; p = mp.exp(-2*mp.pi*d); ph = phase(d); a = mp.sqrt(max(mp.mpf(0), 1-p)); sign = 1 if g >= 0 else -1
        vals = ((mp.sqrt(p), 0), (-sign*a*mp.cos(ph), -sign*a*mp.sin(ph)), (sign*a*mp.cos(ph), -sign*a*mp.sin(ph)), (mp.sqrt(p), 0))
        check(close(row["adiabaticity_delta"], d), f"scattering[{i}] delta"); check(close(row["P_diabatic"], p) and close(row["P_adiabatic"], 1-p), f"scattering[{i}] probabilities")
        check(close(row["stokes_phase"], ph), f"scattering[{i}] phase"); check(close(row["stokes_phase_derivative"], mp.log(d)-mp.re(mp.digamma(1-1j*d)) if d else mp.mpf(0)), f"scattering[{i}] phase derivative")
        names = [("S11_real", vals[0][0]), ("S11_imag", vals[0][1]), ("S12_real", vals[1][0]), ("S12_imag", vals[1][1]), ("S21_real", vals[2][0]), ("S21_imag", vals[2][1]), ("S22_real", vals[3][0]), ("S22_imag", vals[3][1])]
        for name, value in names: check(close(row[name], value), f"scattering[{i}] {name}")
        check(close(row["unitarity_residual"], mp.mpf(0)) and close(row["dP_d_delta"], -2*mp.pi*p) and close(row["dP_dg_at_fixed_v"], -4*mp.pi*g*p/v), f"scattering[{i}] derivatives/unitarity")
        check(0 <= p <= 1 and (d == 0 or -2*mp.pi*p < 0), f"scattering[{i}] monotonicity")
        scattering[label] = p

    finite_keys = ["case_id", "parameter_label", "v", "g", "T", "rk_steps", "U11_real", "U11_imag", "U12_real", "U12_imag", "U21_real", "U21_imag", "U22_real", "U22_imag", "finite_P_diabatic", "asymptotic_P_diabatic", "window_discrepancy", "unitarity_residual"]
    check(len(data["regression"]["finite_window_rows"]) == len(PARAMETERS)*len(WINDOWS), "finite count")
    seen = set()
    for i, row in enumerate(data["regression"]["finite_window_rows"]):
        keys(row, finite_keys, f"finite[{i}]", check)
        label = row["parameter_label"]; check(label in scattering, f"finite[{i}] label")
        vq, gq = next((v, g) for l, v, g in PARAMETERS if l == label); Tq = F(row["T"])
        check(Tq in WINDOWS and row["v"] == str(vq) and row["g"] == str(gq) and row["rk_steps"] == RK_STEPS, f"finite[{i}] domain")
        check(row["case_id"] == f"{label}_T{Tq}", f"finite[{i}] identity"); ident = (label, Tq); check(ident not in seen, f"finite[{i}] duplicate"); seen.add(ident)
        U = finite_propagator(mpq(vq), mpq(gq), mpq(Tq)); names = [("U11_real", mp.re(U[0][0])), ("U11_imag", mp.im(U[0][0])), ("U12_real", mp.re(U[0][1])), ("U12_imag", mp.im(U[0][1])), ("U21_real", mp.re(U[1][0])), ("U21_imag", mp.im(U[1][0])), ("U22_real", mp.re(U[1][1])), ("U22_imag", mp.im(U[1][1]))]
        for name, value in names: check(close(row[name], value), f"finite[{i}] {name}")
        pwin = abs(U[0][0])**2; r = residual(U); check(close(row["finite_P_diabatic"], pwin) and close(row["asymptotic_P_diabatic"], scattering[label]), f"finite[{i}] probabilities")
        check(close(row["window_discrepancy"], abs(pwin-scattering[label])) and close(row["unitarity_residual"], r), f"finite[{i}] residual")
        check(r < mp.mpf("1e-3") and 0 <= pwin <= 1 + mp.mpf("1e-3"), f"finite[{i}] control bounds")
    check(len(seen) == 15, "finite closure")
    boundaries = data["regression"]["boundary_rows"]; check(len(boundaries) == 6, "boundary count")
    bkeys = ["boundary_id", "parameter", "statement"]
    expected_bids = {"zero_coupling", "adiabatic", "sudden", "negative_coupling", "finite_window", "weber_turning"}
    for i, row in enumerate(boundaries): keys(row, bkeys, f"boundary[{i}]", check); check(row["boundary_id"] in expected_bids, f"boundary[{i}] id")
    citation_keys = ["key", "claim", "title", "authors", "venue", "date", "url", "persistent_url"]
    check(len(data["citations"]) == 3, "citation count")
    for i, citation in enumerate(data["citations"]):
        keys(citation, citation_keys, f"citation[{i}]", check); check(citation["url"] == citation["persistent_url"] and citation["url"].startswith("https://doi.org/"), f"citation[{i}] persistent DOI")
    print(json.dumps({"status": "C224_CHECKER_PASS", "assertions": assertions, "scattering_rows": 5, "finite_window_rows": 15, "max_unitarity_residual": max(float(row["unitarity_residual"]) for row in data["regression"]["finite_window_rows"]), "payload_sha256": data["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
