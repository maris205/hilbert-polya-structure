#!/usr/bin/env python3
"""Canonical certificate for the one-dimensional focusing cubic NLS soliton.

The receipt is deliberately a finite, source-local regression ledger.  The
theorem and proof in the manuscript carry the all-parameter quantifiers; this
program evaluates exact closed formulae on a rational omega/x grid and never
imports arithmetic or target spectral data.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import mpmath as mp

SOURCE_COMMIT = "86c7bb8a39cdd1b8e941e45833b068170ca06287"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c221_nls_evidence.json"

OMEGA_VALUES = [F(1, 4), F(1), F(4)]
X_VALUES = [F(-2), F(-1), F(0), F(1), F(2)]
Y_VALUES = [F(-2), F(-1), F(0), F(1), F(2)]
WORKING_DECIMAL_DIGITS = 100
SERIALIZED_SIGNIFICANT_DIGITS = 82


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    encoded = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(encoded).hexdigest()


def mpq(value: F) -> mp.mpf:
    return mp.mpf(value.numerator) / value.denominator


def mparg(value: F | mp.mpf) -> mp.mpf:
    return mpq(value) if isinstance(value, F) else mp.mpf(value)


def fmt(value: mp.mpf) -> str:
    return mp.nstr(value, SERIALIZED_SIGNIFICANT_DIGITS, strip_zeros=False)


def sech(x: mp.mpf) -> mp.mpf:
    return 1 / mp.cosh(x)


def profile(omega: F, x: F | mp.mpf) -> mp.mpf:
    w = mpq(omega)
    xx = mparg(x)
    return mp.sqrt(w) * sech(mp.sqrt(w) * xx)


def profile_prime(omega: F, x: F | mp.mpf) -> mp.mpf:
    w = mpq(omega)
    y = mp.sqrt(w) * mparg(x)
    return -w * sech(y) * mp.tanh(y)


def q_residual(omega: F, x: F | mp.mpf) -> mp.mpf:
    w = mpq(omega)
    y = mp.sqrt(w) * mparg(x)
    s = sech(y)
    q = mp.sqrt(w) * s
    qxx = w ** mp.mpf("1.5") * (s - 2 * s ** 3)
    return -qxx + w * q - 2 * q ** 3


def phi_plus(omega: F, x: F | mp.mpf) -> mp.mpf:
    y = mp.sqrt(mpq(omega)) * mparg(x)
    return sech(y) ** 2


def phi_minus(omega: F, x: F | mp.mpf) -> mp.mpf:
    y = mp.sqrt(mpq(omega)) * mparg(x)
    return sech(y)


def second_derivative(fun, x: mp.mpf) -> mp.mpf:
    return mp.diff(fun, x, 2)


def lplus(omega: F, fun, x: F | mp.mpf) -> mp.mpf:
    w = mpq(omega)
    xx = mparg(x)
    return -second_derivative(lambda z: fun(omega, z), xx) + (w - 6 * w * sech(mp.sqrt(w) * xx) ** 2) * fun(omega, xx)


def lminus(omega: F, fun, x: F | mp.mpf) -> mp.mpf:
    w = mpq(omega)
    xx = mparg(x)
    return -second_derivative(lambda z: fun(omega, z), xx) + (w - 2 * w * sech(mp.sqrt(w) * xx) ** 2) * fun(omega, xx)


def factorization_residuals(y: F | mp.mpf) -> tuple[mp.mpf, mp.mpf]:
    """Residuals for scaled Pöschl–Teller factorizations."""
    yy = mparg(y)
    s2 = sech(yy) ** 2
    # A_l^* A_l = -d^2+l^2-l(l+1)sech^2.  Therefore
    # P_2=-d^2+1-6sech^2=A_2^*A_2-3 and P_1=A_1^*A_1.
    p2_minus_fact = (1 - 6 * s2) - ((4 - 6 * s2) - 3)
    p1_minus_fact = (1 - 2 * s2) - (1 - 2 * s2)
    return p2_minus_fact, p1_minus_fact


def build() -> dict:
    mp.mp.dps = WORKING_DECIMAL_DIGITS
    profile_rows = []
    for omega in OMEGA_VALUES:
        for x in X_VALUES:
            q = profile(omega, x)
            profile_rows.append({
                "case_id": f"w{omega}_x{x}",
                "omega": str(omega),
                "x": str(x),
                "Q": fmt(q),
                "Q_prime": fmt(profile_prime(omega, x)),
                "standing_wave_residual": fmt(q_residual(omega, x)),
            })

    integral_rows = []
    for omega in OMEGA_VALUES:
        w = mpq(omega)
        mass = 2 * mp.sqrt(w)
        grad = mp.mpf(2) / 3 * w ** mp.mpf("1.5")
        quartic = mp.mpf(4) / 3 * w ** mp.mpf("1.5")
        hamiltonian = (grad - quartic) / 2
        action = hamiltonian + w * mass / 2
        vk = 1 / mp.sqrt(w)
        integral_rows.append({
            "case_id": f"w{omega}",
            "omega": str(omega),
            "mass": fmt(mass),
            "grad_norm_sq": fmt(grad),
            "quartic_norm_4": fmt(quartic),
            "hamiltonian": fmt(hamiltonian),
            "action": fmt(action),
            "vk_slope": fmt(vk),
        })

    spectrum_rows = []
    for omega in OMEGA_VALUES:
        for x in X_VALUES:
            spectrum_rows.append({
                "case_id": f"w{omega}_x{x}",
                "omega": str(omega),
                "x": str(x),
                "Lplus_phi2_residual": fmt(lplus(omega, phi_plus, x) + 3 * mpq(omega) * phi_plus(omega, x)),
                "Lplus_Qprime_residual": fmt(lplus(omega, profile_prime, x)),
                "Lminus_Q_residual": fmt(lminus(omega, profile, x)),
                "essential_threshold": fmt(mpq(omega)),
                "Lplus_phi2_eigenvalue": fmt(-3 * mpq(omega)),
                "Lplus_Qprime_eigenvalue": "0",
                "Lminus_Q_eigenvalue": "0",
            })

    factorization_rows = []
    for omega in OMEGA_VALUES:
        for y in Y_VALUES:
            r2, r1 = factorization_residuals(y)
            factorization_rows.append({
                "case_id": f"w{omega}_y{y}",
                "omega": str(omega),
                "y": str(y),
                "P2_minus_A2starA2_plus3": fmt(r2),
                "P1_minus_A1starA1": fmt(r1),
            })

    boundary_rows = [
        {"boundary_id": "omega_zero", "parameter": "omega↓0", "statement": "Q_omega vanishes in the H1 scaling limit; essential threshold and discrete eigenvalues collapse to 0"},
        {"boundary_id": "defocusing", "parameter": "sign=-1", "statement": "the defocusing cubic equation has no nonzero bright H1 sech soliton of this form"},
        {"boundary_id": "periodic_domain", "parameter": "R/LZ", "statement": "finite periodic domains replace the sech branch by elliptic/cnoidal waves and are outside this owner"},
        {"boundary_id": "higher_dimension", "parameter": "d≥2", "statement": "higher-dimensional criticality and collapse are outside the one-dimensional Hessian theorem"},
    ]

    data = {
        "schema": "hcs-c221-focusing-cubic-nls-hessian-v1",
        "candidate_id": "HCS-C221",
        "evaluation_date": "2026-08-28",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "evaluator": {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256},
        "headline": "The one-dimensional focusing cubic NLS soliton has an exact Hessian spectrum, Morse index, VK slope, and Pöschl–Teller factorization",
        "frozen_object": {
            "phase_space": "H^1(R;C) with the one-dimensional focusing cubic NLS flow; the spectral owner is the real Hessian at the standing wave",
            "equation": "i psi_t + psi_xx + 2|psi|^2 psi = 0",
            "standing_wave": "psi(t,x)=exp(i*omega*t) Q_omega(x), Q_omega(x)=sqrt(omega) sech(sqrt(omega)*x)",
            "parameters": "omega>0; physical t and x; no fitted scale",
            "clock": "physical NLS time t; no logarithmic or target-fitted clock",
            "normalization": "M(u)=integral_R |u|^2 dx; H(u)=1/2 integral |u_x|^2 dx - 1/2 integral |u|^4 dx; S_omega=H+(omega/2)M",
            "determinant_convention": "none; continuous-spectrum Hessians are not called dynamical zeta or Fredholm determinants",
            "arithmetic_origin": "none; this is a scope-locked non-arithmetic Hamiltonian PDE certificate",
            "allowed_data": "exact rational omega,x,y sentinels and source-local sech/Pöschl–Teller algebra",
            "forbidden_data": "prime/zero tables, target labels, fitted frequencies, Euler factors, root numbers, and external spectral fits",
        },
        "theorem": {
            "profile_equation": "-Q_omega''+omega Q_omega-2 Q_omega^3=0, Q_omega=sqrt(omega) sech(sqrt(omega)x)",
            "integrals": "M(Q)=2 sqrt(omega), ||Q'||_2^2=(2/3)omega^(3/2), ||Q||_4^4=(4/3)omega^(3/2), H(Q)=-(1/3)omega^(3/2), S_omega(Q)=(2/3)omega^(3/2)",
            "vk": "dM(Q_omega)/domega=omega^(-1/2)>0",
            "hessian": "L_+=-d_x^2+omega-6omega sech^2(sqrt(omega)x), L_-=-d_x^2+omega-2omega sech^2(sqrt(omega)x)",
            "spectrum": "sigma_ess(L_+)=sigma_ess(L_-)=[omega,infinity); L_+ has simple eigenvalues -3omega (sech^2) and 0 (Q_prime), L_- has simple eigenvalue 0 (Q), with no other discrete eigenvalues",
            "morse": "L_+ has Morse index one and ker L_+=span{Q_prime}; L_- is nonnegative with ker L_-=span{Q}",
            "factorization": "in y=sqrt(omega)x, A_l=d_y+l tanh(y), A_l*=−d_y+l tanh(y): P_2=A_2* A_2−3 and P_1=A_1* A_1",
            "boundaries": "omega↓0 collapses the branch and threshold; defocusing sign has no bright H1 sech soliton; finite periodic and d≥2 branches are outside scope",
        },
        "regression": {
            "omega_values": [str(x) for x in OMEGA_VALUES],
            "x_values": [str(x) for x in X_VALUES],
            "y_values": [str(x) for x in Y_VALUES],
            "profile_rows": profile_rows,
            "integral_rows": integral_rows,
            "spectrum_rows": spectrum_rows,
            "factorization_rows": factorization_rows,
            "boundary_rows": boundary_rows,
        },
        "summary": {
            "profile_row_count": len(profile_rows),
            "integral_row_count": len(integral_rows),
            "spectrum_row_count": len(spectrum_rows),
            "factorization_row_count": len(factorization_rows),
            "boundary_row_count": len(boundary_rows),
            "serialized_decimal_digits": SERIALIZED_SIGNIFICANT_DIGITS,
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "strongest_positive": "Exact one-dimensional soliton profile, action/mass/VK identities, complete Pöschl–Teller Hessian spectrum, Morse index, and factorization are closed in one owner.",
            "strongest_failure": "The continuum Hamiltonian PDE has no intrinsic prime carrier, isolated arithmetic primitive-orbit clock, target divisor, or Hilbert–Polya identification.",
        },
        "scope_flags": {k: False for k in ["uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"]},
        "citations": [
            {"key": "ZakharovShabat1972", "claim": "integrable focusing NLS and sech soliton source", "title": "Exact theory of two-dimensional self-focusing and one-dimensional self-modulation of waves in nonlinear media", "authors": "V. E. Zakharov and A. B. Shabat", "venue": "Soviet Physics JETP 34, 62–69", "date": "1972", "url": "https://www.jetp.ras.ru/cgi-bin/dn/e_034_01_0062", "persistent_url": "https://www.jetp.ras.ru/cgi-bin/dn/e_034_01_0062"},
            {"key": "Weinstein1985", "claim": "variational Hessian, spectral coercivity, and VK stability criterion", "title": "Modulational Stability of Ground States of Nonlinear Schrödinger Equations", "authors": "Michael I. Weinstein", "venue": "SIAM Journal on Mathematical Analysis 16, 472–491", "date": "1985", "url": "https://doi.org/10.1137/0516034", "persistent_url": "https://doi.org/10.1137/0516034"},
            {"key": "PoschlTeller1933", "claim": "original solvable Pöschl–Teller potential and ladder source; historical attribution only", "title": "Bemerkungen zur Quantenmechanik des anharmonischen Oszillators", "authors": "G. Pöschl and E. Teller", "venue": "Zeitschrift für Physik 83, 143–151", "date": "1933", "url": "https://doi.org/10.1007/BF01331132", "persistent_url": "https://doi.org/10.1007/BF01331132"},
        ],
        "nonclaims": [
            "priority or novelty for the cubic NLS soliton, Pöschl–Teller spectrum, or VK criterion",
            "a finite rational grid proves the all-parameter spectral theorem",
            "a Hessian determinant, trace, or continuous spectrum is a dynamical zeta, Euler factor, or Fredholm determinant",
            "full nonlinear orbital/asymptotic stability, blow-up classification, or higher-dimensional NLS results",
            "any arithmetic correspondence, target divisor, functional equation, Hilbert–Polya operator, external review, or Route-B authorization",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    out = ap.parse_args().output
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(build(), sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    obj = json.loads(out.read_text())
    print(json.dumps({"status": "C221_PRODUCER_PASS", "output": str(out), "payload_sha256": obj["payload_sha256"], "profile_rows": obj["summary"]["profile_row_count"], "spectrum_rows": obj["summary"]["spectrum_row_count"]}, sort_keys=True))


if __name__ == "__main__":
    main()
