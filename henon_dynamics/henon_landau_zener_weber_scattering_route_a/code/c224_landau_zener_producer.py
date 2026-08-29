#!/usr/bin/env python3
"""Canonical source-local certificate for Landau--Zener--Weber scattering.

The receipt combines the exact asymptotic Landau--Zener formula with a
deterministic finite-window RK4 control experiment.  The numerical window is
not used to define the scattering law; it only checks the ODE and its unitary
matrix structure at rational source parameters.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import mpmath as mp

SOURCE_COMMIT = "489672bd36abd3a4f6da92d1446a0af575917959"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c224_landau_zener_evidence.json"
WORKING_DIGITS = 80
SERIALIZED_DIGITS = 68

PARAMETERS = [
    ("reference", F(1), F(1, 2)),
    ("fast_weak", F(4), F(1, 3)),
    ("slow_strong", F(1, 4), F(3, 4)),
    ("negative_g", F(2), F(-1, 2)),
    ("uncoupled", F(3, 2), F(0)),
]
WINDOWS = [F(2), F(4), F(8)]
RK_STEPS = 2048


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def mpq(value: F | int) -> mp.mpf:
    if isinstance(value, F):
        return mp.mpf(value.numerator) / value.denominator
    return mp.mpf(value)


def fmt(value: mp.mpf | mp.mpc) -> str:
    return mp.nstr(value, SERIALIZED_DIGITS, strip_zeros=False)


def stokes_phase(delta: mp.mpf) -> mp.mpf:
    if delta == 0:
        return mp.pi / 4
    return mp.pi / 4 + delta * (mp.log(delta) - 1) + mp.im(mp.loggamma(1 - 1j * delta))


def rhs(t: mp.mpf, y: tuple[mp.mpc, mp.mpc], v: mp.mpf, g: mp.mpf) -> tuple[mp.mpc, mp.mpc]:
    a, b = y
    z = v * t / 2
    return (-1j * (z * a + g * b), -1j * (g * a - z * b))


def rk4_step(t: mp.mpf, y: tuple[mp.mpc, mp.mpc], h: mp.mpf, v: mp.mpf, g: mp.mpf) -> tuple[mp.mpc, mp.mpc]:
    k1 = rhs(t, y, v, g)
    k2 = rhs(t + h / 2, (y[0] + h * k1[0] / 2, y[1] + h * k1[1] / 2), v, g)
    k3 = rhs(t + h / 2, (y[0] + h * k2[0] / 2, y[1] + h * k2[1] / 2), v, g)
    k4 = rhs(t + h, (y[0] + h * k3[0], y[1] + h * k3[1]), v, g)
    return tuple(y[i] + h * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) / 6 for i in (0, 1))


def finite_propagator(v: mp.mpf, g: mp.mpf, T: mp.mpf) -> tuple[tuple[mp.mpc, mp.mpc], tuple[mp.mpc, mp.mpc]]:
    h = 2 * T / RK_STEPS
    cols = []
    for initial in ((1 + 0j, 0 + 0j), (0 + 0j, 1 + 0j)):
        y = (mp.mpc(initial[0]), mp.mpc(initial[1]))
        t = -T
        for _ in range(RK_STEPS):
            y = rk4_step(t, y, h, v, g)
            t += h
        cols.append(y)
    return ((cols[0][0], cols[1][0]), (cols[0][1], cols[1][1]))


def gram_residual(U: tuple[tuple[mp.mpc, mp.mpc], tuple[mp.mpc, mp.mpc]]) -> mp.mpf:
    vals = []
    for i in range(2):
        for j in range(2):
            value = sum(mp.conj(U[k][i]) * U[k][j] for k in range(2)) - (1 if i == j else 0)
            vals.append(abs(value))
    return max(vals)


def scattering_row(label: str, vq: F, gq: F) -> dict:
    v, g = mpq(vq), mpq(gq)
    delta = g * g / v
    p = mp.exp(-2 * mp.pi * delta)
    phase = stokes_phase(delta)
    amp = mp.sqrt(max(mp.mpf(0), 1 - p))
    sign = 1 if g >= 0 else -1
    s11, s12 = mp.sqrt(p), -sign * amp * mp.exp(1j * phase)
    s21, s22 = sign * amp * mp.exp(-1j * phase), mp.sqrt(p)
    sres = max(abs(mp.conj(s11) * s11 + mp.conj(s21) * s21 - 1),
               abs(mp.conj(s12) * s12 + mp.conj(s22) * s22 - 1),
               abs(mp.conj(s11) * s12 + mp.conj(s21) * s22))
    dP = -2 * mp.pi / v * p
    dphase = mp.log(delta) - mp.re(mp.digamma(1 - 1j * delta)) if delta else mp.mpf("0")
    return {
        "case_id": label, "v": str(vq), "g": str(gq),
        "adiabaticity_delta": fmt(delta), "P_diabatic": fmt(p), "P_adiabatic": fmt(1 - p),
        "stokes_phase": fmt(phase), "stokes_phase_derivative": fmt(dphase),
        "S11_real": fmt(mp.re(s11)), "S11_imag": fmt(mp.im(s11)),
        "S12_real": fmt(mp.re(s12)), "S12_imag": fmt(mp.im(s12)),
        "S21_real": fmt(mp.re(s21)), "S21_imag": fmt(mp.im(s21)),
        "S22_real": fmt(mp.re(s22)), "S22_imag": fmt(mp.im(s22)),
        "unitarity_residual": fmt(sres), "dP_d_delta": fmt(-2 * mp.pi * p),
        "dP_dg_at_fixed_v": fmt(2 * g * dP),
    }


def finite_row(label: str, vq: F, gq: F, Tq: F, asymptotic: mp.mpf) -> dict:
    v, g, T = mpq(vq), mpq(gq), mpq(Tq)
    U = finite_propagator(v, g, T)
    residual = gram_residual(U)
    pwin = abs(U[0][0]) ** 2
    return {
        "case_id": f"{label}_T{Tq}", "parameter_label": label,
        "v": str(vq), "g": str(gq), "T": str(Tq), "rk_steps": RK_STEPS,
        "U11_real": fmt(mp.re(U[0][0])), "U11_imag": fmt(mp.im(U[0][0])),
        "U12_real": fmt(mp.re(U[0][1])), "U12_imag": fmt(mp.im(U[0][1])),
        "U21_real": fmt(mp.re(U[1][0])), "U21_imag": fmt(mp.im(U[1][0])),
        "U22_real": fmt(mp.re(U[1][1])), "U22_imag": fmt(mp.im(U[1][1])),
        "finite_P_diabatic": fmt(pwin), "asymptotic_P_diabatic": fmt(asymptotic),
        "window_discrepancy": fmt(abs(pwin - asymptotic)), "unitarity_residual": fmt(residual),
    }


def build() -> dict:
    mp.mp.dps = WORKING_DIGITS
    scat = [scattering_row(label, v, g) for label, v, g in PARAMETERS]
    lookup = {r["case_id"]: mp.mpf(r["P_diabatic"]) for r in scat}
    finite = [finite_row(label, v, g, T, lookup[label]) for label, v, g in PARAMETERS for T in WINDOWS]
    boundaries = [
        {"boundary_id": "zero_coupling", "parameter": "g=0", "statement": "The channels decouple, P_diabatic=1 and the Stokes phase is taken by continuous delta=0 convention."},
        {"boundary_id": "adiabatic", "parameter": "v↓0 at fixed g≠0", "statement": "delta=g^2/v→∞, P_diabatic→0 and the finite crossing follows the adiabatic branch."},
        {"boundary_id": "sudden", "parameter": "v→∞ at fixed g", "statement": "delta→0, P_diabatic→1 and the mixing probability is O(g^2/v)."},
        {"boundary_id": "negative_coupling", "parameter": "g↦−g", "statement": "A constant sigma_z gauge changes the sign of g; probabilities and P_diabatic are unchanged while off-diagonal phases change gauge."},
        {"boundary_id": "finite_window", "parameter": "T<∞", "statement": "The RK4 propagator is a controlled finite-window approximation and is not identified with the infinite-time scattering matrix."},
        {"boundary_id": "weber_turning", "parameter": "t=0", "statement": "The diabatic gap closes at one avoided crossing; the scalar reduction is a Weber equation with complex turning points."},
    ]
    data = {
        "schema": "hcs-c224-landau-zener-weber-v1", "candidate_id": "HCS-C224", "evaluation_date": "2026-08-29",
        "source_commit": SOURCE_COMMIT, "scope_literal": SCOPE,
        "evaluator": {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256},
        "headline": "Landau--Zener--Weber crossing has exact asymptotic scattering, Stokes phase, monotonicity, and finite-window unitary controls",
        "frozen_object": {
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
        },
        "theorem": {
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
        },
        "regression": {
            "parameter_rows": [{"parameter_label": label, "v": str(v), "g": str(g)} for label, v, g in PARAMETERS],
            "window_values": [str(x) for x in WINDOWS], "scattering_rows": scat, "finite_window_rows": finite, "boundary_rows": boundaries,
        },
        "summary": {"parameter_count": len(PARAMETERS), "scattering_row_count": len(scat), "finite_window_row_count": len(finite), "boundary_row_count": len(boundaries), "rk_steps": RK_STEPS, "working_decimal_digits": WORKING_DIGITS, "serialized_significant_digits": SERIALIZED_DIGITS},
        "route_a": {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_UNITARY_OR_SCATTERING_CANDIDATE"], "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False, "strongest_positive": "Weber connection data gives an intrinsic unitary scattering matrix with a nontrivial Stokes/Gamma phase.", "strongest_failure": "The crossing has no primitive arithmetic owner, target divisor, or target zero correspondence; the scattering candidate is not a Hilbert--Polya bridge."},
        "scope_flags": {k: False for k in ["uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"]},
        "citations": [
            {"key": "Zener1932", "claim": "original nonadiabatic crossing calculation and transition law", "title": "Non-adiabatic crossing of energy levels", "authors": "Clarence Zener", "venue": "Proceedings of the Royal Society A 137, 696--702", "date": "1932", "url": "https://doi.org/10.1098/rspa.1932.0165", "persistent_url": "https://doi.org/10.1098/rspa.1932.0165"},
            {"key": "VitanovGarraway1996", "claim": "parabolic-cylinder/Weber treatment and finite-time Landau--Zener dynamics", "title": "Landau-Zener model: Effects of finite coupling duration", "authors": "Nikolay V. Vitanov and Barry M. Garraway", "venue": "Physical Review A 53, 4288--4304", "date": "1996", "url": "https://doi.org/10.1103/PhysRevA.53.4288", "persistent_url": "https://doi.org/10.1103/PhysRevA.53.4288"},
            {"key": "Shevchenko2010", "claim": "review of Landau--Zener/Stokes phase conventions and applications", "title": "Landau-Zener-Stuckelberg interferometry", "authors": "Sergey N. Shevchenko, Sergei Ashhab, Franco Nori", "venue": "Physics Reports 492, 1--30", "date": "2010", "url": "https://doi.org/10.1016/j.physrep.2010.03.002", "persistent_url": "https://doi.org/10.1016/j.physrep.2010.03.002"},
        ],
        "nonclaims": ["priority for the Landau--Zener model, Weber functions, or Stokes phases", "the finite RK4 grid is an exact finite-time propagator or a proof of an infinite-dimensional theorem", "P_diabatic, the Gamma phase, or any crossing parameter is target arithmetic spectral data", "a target divisor, Euler factor, root number, automorphy statement, Hilbert--Polya operator, or Route-B authorization"],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    path = parser.parse_args().output
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(build(), sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    data = json.loads(path.read_text())
    print(json.dumps({"status": "C224_PRODUCER_PASS", "scattering_rows": data["summary"]["scattering_row_count"], "finite_window_rows": data["summary"]["finite_window_row_count"], "payload_sha256": data["payload_sha256"], "output": str(path)}, sort_keys=True))


if __name__ == "__main__":
    main()
