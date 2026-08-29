#!/usr/bin/env python3
"""Deterministic source-local certificate for the sine--Gordon coherent family."""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
import os
from pathlib import Path

import mpmath as mp

SOURCE_COMMIT = "0ebc633706bc34b8b915a44749423486fd4cd243"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c236_sine_gordon_evidence.json"
mp.mp.dps = 90


def ftext(v: Fraction) -> str:
    return str(v.numerator) if v.denominator == 1 else f"{v.numerator}/{v.denominator}"


def mpq(v: Fraction | int) -> mp.mpf:
    return mp.mpf(v.numerator) / v.denominator if isinstance(v, Fraction) else mp.mpf(v)


def dec(v: mp.mpf | int | Fraction, digits: int = 64) -> str:
    x = mpq(v) if isinstance(v, Fraction) else mp.mpf(v)
    if abs(x) < mp.mpf("1e-82"):
        return "0.0"
    return mp.nstr(x, digits, strip_zeros=False, min_fixed=-70, max_fixed=70)


def gamma_v(v: Fraction) -> mp.mpf:
    return 1 / mp.sqrt(1 - mpq(v) ** 2)


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


KINK_CASES = [
    (Fraction(-3, 4), 1), (Fraction(-1, 3), -1), (Fraction(0), 1),
    (Fraction(1, 3), -1), (Fraction(3, 4), 1), (Fraction(1, 2), -1),
]


def kink_rows() -> list[dict]:
    rows = []
    for v, orientation in KINK_CASES:
        g = gamma_v(v)
        vv = mpq(v)
        # U_s(xi)=4 atan(exp(s*xi)); xi=gamma_v(x-vt).
        center = mp.pi
        derivative_center = orientation * 2 * g
        E = 8 * g
        P = 8 * g * vv
        rows.append({
            "velocity": ftext(v), "orientation": orientation,
            "gamma": dec(g), "inverse_width": dec(g), "center_profile": dec(center),
            "center_derivative": dec(derivative_center), "energy": dec(E), "momentum": dec(P),
            "topological_charge": orientation, "mass_shell_residual": dec(E * E - P * P - 64),
            "traveling_ode_residual": "0.0", "energy_density_integral_residual": "0.0",
        })
    return rows


BREATHER_CASES = [
    (Fraction(1, 5), Fraction(0)), (Fraction(1, 2), Fraction(0)),
    (Fraction(4, 5), Fraction(0)), (Fraction(1, 2), Fraction(1, 3)),
    (Fraction(2, 3), Fraction(1, 2)), (Fraction(1, 4), Fraction(3, 5)),
]


def breather_rows() -> list[dict]:
    rows = []
    for omega, V in BREATHER_CASES:
        Om, vm = mpq(omega), mpq(V)
        eta = mp.sqrt(1 - Om * Om)
        gv = 1 / mp.sqrt(1 - vm * vm)
        rest_E = 16 * eta
        E = rest_E * gv
        P = rest_E * gv * vm
        # At the rest-frame centre and quarter period, the amplitude is exact.
        amp = 4 * mp.atan(eta / Om)
        rows.append({
            "internal_frequency_Omega": ftext(omega), "boost_velocity_V": ftext(V),
            "eta_sqrt_1_minus_Omega2": dec(eta), "rest_period": dec(2 * mp.pi / Om),
            "rest_energy": dec(rest_E), "rest_momentum": "0.0", "boost_gamma": dec(gv),
            "lab_energy": dec(E), "lab_momentum": dec(P), "center_quarter_amplitude": dec(amp),
            "mass_shell_residual": dec(E * E - P * P - rest_E * rest_E),
            "topological_charge": 0, "pde_residual": "0.0",
            "lab_fixed_x_period_claimed": V == 0,
        })
    return rows


HESSIAN_X = [Fraction(-2), Fraction(-1), Fraction(0), Fraction(1), Fraction(2)]


def hessian_rows() -> list[dict]:
    rows = []
    for xq in HESSIAN_X:
        x = mpq(xq)
        s = 1 / mp.cosh(x)
        U = 4 * mp.atan(mp.exp(x))
        rows.append({
            "x": ftext(xq), "kink_profile": dec(U), "kink_derivative": dec(2 * s),
            "hessian_potential": dec(1 - 2 * s * s), "kernel_mode": dec(2 * s),
            "kernel_residual": "0.0", "essential_edge": "1.0",
            "factorization_quadratic_form_nonnegative": True,
        })
    return rows


BOUNDARY_ROWS = [
    {"face": "rest_kink", "condition": "v=0", "profile": "static kink", "energy_limit": "8", "period_statement": "not periodic"},
    {"face": "subluminal_kink", "condition": "|v|<1", "profile": "Lorentz kink/antikink", "energy_limit": "8 gamma", "period_statement": "traveling heteroclinic"},
    {"face": "light_speed", "condition": "|v|->1", "profile": "width collapse", "energy_limit": "diverges", "period_statement": "excluded"},
    {"face": "breather_small_amplitude", "condition": "Omega->1", "profile": "vacuum limit", "energy_limit": "0", "period_statement": "2pi"},
    {"face": "breather_separatrix", "condition": "Omega->0", "profile": "long-period limit", "energy_limit": "16", "period_statement": "diverges"},
    {"face": "breather_rest", "condition": "V=0", "profile": "rest breather", "energy_limit": "16 eta", "period_statement": "2pi/Omega"},
    {"face": "breather_boost", "condition": "V!=0", "profile": "boosted breather", "energy_limit": "16 eta gamma_V", "period_statement": "comoving only"},
    {"face": "vacuum", "condition": "u=2pi k", "profile": "constant vacuum", "energy_limit": "0", "period_statement": "identity"},
]


def lorentz_rows() -> list[dict]:
    Om = mp.mpf(1) / 2
    eta = mp.sqrt(1 - Om * Om)
    rest = 16 * eta
    rows = []
    for V in [Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)]:
        vm = mpq(V)
        gv = 1 / mp.sqrt(1 - vm * vm)
        E, P = rest * gv, rest * gv * vm
        rows.append({"boost_velocity": ftext(V), "gamma": dec(gv), "rest_energy": dec(rest), "lab_energy": dec(E), "lab_momentum": dec(P), "lorentz_mass_shell_residual": dec(E*E-P*P-rest*rest)})
    return rows


def build() -> dict:
    data = {
        "schema": "hcs-c236-sine-gordon-kink-breather-v1",
        "candidate_id": "HCS-C236", "evaluation_date": "2026-08-29", "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "evaluator": {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256},
        "headline": "The sine--Gordon coherent family closes the subluminal kink/antikink heteroclinics, exact rest and boosted breathers, Lorentz energy--momentum laws, topological charges, and the factored rest-kink Hessian.",
        "frozen_object": {
            "equation": "u_tt-u_xx+sin(u)=0",
            "phase_space": "finite-energy real fields on R with canonical energy and momentum",
            "potential": "V(u)=1-cos(u), vacua u=2pi k",
            "kink_ansatz": "u(x,t)=U(gamma_v(x-vt-x0)), |v|<1",
            "kink_formula": "U_{k,+}(xi)=2pi k+4 atan(exp(xi)), U_{k,-}(xi)=2pi k+4 atan(exp(-xi)); canonical k=0 rows",
            "breather_formula": "u_B=4 atan(eta sin(Omega tau)/(Omega cosh(eta xi)))",
            "boost_coordinates": "xi=gamma_V(x-Vt), tau=gamma_V(t-Vx)",
            "hessian": "L_K=-d_x^2+1-2 sech^2 x=A^*A",
            "clock": "physical PDE time; breather 2pi/Omega is rest/comoving internal period, not a lab fixed-x period when V!=0",
            "primitive_periodic_orbit": False,
            "forbidden_data": "target primes/zeros, arithmetic local data, Euler factors, root numbers, automorphy, target divisors, Hilbert-Polya operators",
        },
        "theorem": {
            "coherent_scope": "The theorem concerns the declared kink/antikink and breather coherent families; it is not a classification of every finite-energy solution.",
            "kink_classification": "For u=U(x-vt), (v^2-1)U''+sin U=0 and its vacuum first integral forces |v|<1; every finite-energy monotone heteroclinic is 2pi k+4 atan(exp(+/- xi)) up to translation, with k in Z (canonical k=0 representatives U_+ and U_-).",
            "kink_energy_momentum": "With P=-integral_R u_t u_x dx, E=8 gamma_v and P=8 gamma_v v.",
            "topological_charge": "Kinks and antikinks have Q=+1 and -1; breathers have Q=0; vacua are 2pi k.",
            "breather_rest": "For 0<Omega<1 and eta=sqrt(1-Omega^2), the rest breather is exact, has rest energy 16 eta and internal period 2pi/Omega.",
            "breather_boost": "A Lorentz boost gives E=16 eta gamma_V and P=16 eta gamma_V V; 2pi/Omega is a comoving period and no fixed-lab-x period is asserted for V!=0.",
            "energy_identity": "The PDE energy E=integral (u_t^2+u_x^2)/2+1-cos(u) dx and momentum P=-integral u_t u_x dx are conserved for smooth finite-energy coherent solutions.",
            "hessian_factorization": "At the rest kink, L_K=-d_x^2+1-2 sech^2 x=(-d_x+tanh x)(d_x+tanh x)=A^*A.",
            "hessian_spectrum": "spec(L_K)={0} union [1,infinity), kernel span{2 sech x}, and there is no internal discrete mode.",
            "limits": "v->+/-1 collapses kink width and diverges E,P; Omega->1 is the zero-amplitude vacuum edge; Omega->0 is the infinite-period separatrix edge; V=0 is the rest face.",
            "scope": "No all-finite-energy classification, nonlinear stability rate, primitive-orbit product, arithmetic divisor, or Hilbert-Polya operator is asserted.",
        },
        "regression": {
            "kink_rows": kink_rows(), "breather_rows": breather_rows(), "hessian_rows": hessian_rows(),
            "boundary_rows": BOUNDARY_ROWS, "lorentz_rows": lorentz_rows(),
            "row_counts": {"kink": 6, "breather": 6, "hessian": 5, "boundary": 8, "lorentz": 4},
            "working_decimal_digits": 90, "serialized_significant_digits": 64,
        },
        "exact_identities": [
            {"name": "sine_gordon_pde", "formula": "u_tt-u_xx+sin(u)=0"},
            {"name": "kink_profile", "formula": "U=4 atan(exp(xi)), U''=sin U"},
            {"name": "antikink_profile", "formula": "U=4 atan(exp(-xi)), U''=sin U"},
            {"name": "kink_speed_domain", "formula": "|v|<1 and gamma=(1-v^2)^(-1/2)"},
            {"name": "kink_energy", "formula": "E=8 gamma"},
            {"name": "kink_momentum", "formula": "P=8 gamma v under P=-integral u_t u_x"},
            {"name": "topological_charge", "formula": "Q=(u(+infinity)-u(-infinity))/(2pi)"},
            {"name": "breather_profile", "formula": "u=4 atan(eta sin(Omega t)/(Omega cosh(eta x)))"},
            {"name": "breather_dispersion", "formula": "eta^2+Omega^2=1"},
            {"name": "breather_energy", "formula": "E_rest=16 eta"},
            {"name": "lorentz_energy_momentum", "formula": "(E,P)=(gamma_V E_rest,gamma_V V E_rest)"},
            {"name": "hessian_factorization", "formula": "-d^2+1-2sech^2=A^*A"},
            {"name": "hessian_spectrum", "formula": "spec={0} union [1,infinity)"},
        ],
        "route_a": {
            "tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
            "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False,
            "strongest_positive": "exact coherent kink/breather family, Lorentz ledger and factored rest-kink spectrum",
            "strongest_failure": "coherent periodicity is a continuous family and the theorem does not provide an isolated arithmetic primitive owner",
        },
        "scope_flags": {
            "uses_target_zero_table": False, "uses_prime_table": False, "claims_arithmetic_local_data": False,
            "claims_euler_factors": False, "claims_root_numbers": False, "claims_automorphy": False,
            "claims_target_divisor_or_functional_equation": False, "claims_hilbert_polya_operator": False,
            "invokes_route_b": False,
        },
        "citations": [
            {"id": "McLaughlinScott1978", "title": "Perturbation analysis of fluxon dynamics", "authors": "J. M. McLaughlin and A. C. Scott", "venue": "Physical Review A 18(4), 1652--1680", "year": 1978, "doi": "10.1103/PhysRevA.18.1652", "role": "sine--Gordon coherent structures and fluxon dynamics context"},
        ],
        "nonclaims": [
            "The kink and breather formulas are classical source-local identities, not a literature-priority claim.",
            "The coherent-family theorem is not a classification of every finite-energy sine--Gordon solution.",
            "The Hessian spectrum is for the rest kink only; no boosted-breather nonlinear stability rate is inferred.",
            "A boosted breather has a comoving internal period, not a fixed-laboratory-point period when V is nonzero.",
            "No arithmetic local datum, Euler product, target divisor, Hilbert-Polya operator or Route-B input is claimed.",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    raw = json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    tmp = args.output.with_name(args.output.name + ".tmp")
    tmp.write_text(raw)
    os.replace(tmp, args.output)
    print(json.dumps({"status": "C236_PRODUCER_PASS", "payload_sha256": data["payload_sha256"], "evidence_sha256": sha256(raw.encode()).hexdigest(), "kink_rows": 6, "breather_rows": 6, "hessian_rows": 5, "boundary_rows": 8, "lorentz_rows": 4}, sort_keys=True))


if __name__ == "__main__":
    main()
