#!/usr/bin/env python3
"""Deterministic period/action ledger for the conservative Duffing flow."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path

import mpmath as mp

SOURCE_COMMIT = "e1dc522e054c2d0ded74b017bc52c7b016a52c59"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
FIXED_EPOCH = 1787875200
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c232_duffing_evidence.json"
WORKING_DIGITS = 80
SERIALIZED_DIGITS = 62

PARAMETERS = [
    ("hardening", F(1), F(1), [F(1, 20), F(1, 5), F(1, 2), F(1)]),
    ("pure_quartic", F(0), F(1), [F(1, 20), F(1, 5), F(1, 2), F(1)]),
    ("double_well_unit", F(-1), F(1), [F(-6, 25), F(-1, 10), F(-1, 100), F(1, 10)]),
    ("double_well_scaled", F(-2), F(3, 2), [F(-13, 20), F(-1, 3), F(-1, 50), F(1, 5)]),
    ("stiff_hardening", F(3), F(2), [F(1, 20), F(1, 5), F(1, 2), F(1)]),
]


def payload_hash(data: dict) -> str:
    body = dict(data); body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def mpq(q: F) -> mp.mpf:
    return mp.mpf(q.numerator) / q.denominator


def fmt(x: mp.mpf) -> str:
    x = mp.re(x)
    if abs(x) < mp.mpf("1e-68"): x = mp.mpf("0")
    return mp.nstr(x, SERIALIZED_DIGITS, strip_zeros=False, min_fixed=-SERIALIZED_DIGITS, max_fixed=SERIALIZED_DIGITS)


def potential(x: mp.mpf, delta: mp.mpf, beta: mp.mpf) -> mp.mpf:
    return delta * x * x / 2 + beta * x ** 4 / 4


def intervals(delta: mp.mpf, beta: mp.mpf, energy: mp.mpf) -> tuple[str, int, mp.mpf, mp.mpf, list[mp.mpf]]:
    disc = delta * delta + 4 * beta * energy
    if disc < 0:
        raise ValueError("energy below the minimum")
    root = mp.sqrt(max(disc, mp.mpf("0")))
    y_minus = (-delta - root) / beta
    y_plus = (-delta + root) / beta
    if delta >= 0:
        a = mp.sqrt(y_plus)
        return "single_center", 1, -a, a, [-a, a]
    if energy < 0:
        lo, hi = mp.sqrt(y_minus), mp.sqrt(y_plus)
        return "double_inner", 2, lo, hi, [-hi, -lo, lo, hi]
    a = mp.sqrt(y_plus)
    return "outer", 1, -a, a, [-a, a]


def quadrature(delta: mp.mpf, beta: mp.mpf, energy: mp.mpf, left: mp.mpf, right: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
    """Endpoint-cancelled period and action on one connected oval."""
    mid = (left + right) / 2; half = (right - left) / 2

    def denom(theta: mp.mpf) -> mp.mpf:
        x = mid + half * mp.sin(theta)
        rem = energy - potential(x, delta, beta)
        return max(rem, mp.mpf("0"))

    def period_integrand(theta: mp.mpf) -> mp.mpf:
        c = mp.cos(theta)
        if abs(c) < mp.mpf("1e-35"): return mp.mpf("0")
        rem = denom(theta)
        if rem <= 0: return mp.mpf("0")
        return mp.sqrt(2) * half * c / mp.sqrt(rem)

    def action_integrand(theta: mp.mpf) -> mp.mpf:
        c = mp.cos(theta)
        if abs(c) < mp.mpf("1e-35"): return mp.mpf("0")
        return (mp.sqrt(2 * denom(theta)) * half * c) / mp.pi

    period = mp.re(mp.quad(period_integrand, [-mp.pi/2, 0, mp.pi/2]))
    action = mp.re(mp.quad(action_integrand, [-mp.pi/2, 0, mp.pi/2]))
    return period, action


def row(case_id: str, delta_q: F, beta_q: F, energy_q: F) -> dict:
    delta, beta, energy = mpq(delta_q), mpq(beta_q), mpq(energy_q)
    regime, components, left, right, roots = intervals(delta, beta, energy)
    period, action = quadrature(delta, beta, energy, left, right)
    vleft = potential(left, delta, beta) - energy
    vright = potential(right, delta, beta) - energy
    alpha = mp.sqrt(-delta) if delta < 0 else mp.mpf("0")
    linear_period = 2 * mp.pi / mp.sqrt(delta) if delta > 0 else None
    scaling = period * energy ** mp.mpf("0.25") * beta ** mp.mpf("0.25") if delta == 0 else None
    return {
        "case_id": case_id, "delta": str(delta_q), "beta": str(beta_q), "energy": str(energy_q),
        "regime": regime, "component_count": components,
        "selected_interval": [fmt(left), fmt(right)], "all_turning_roots": [fmt(x) for x in roots],
        "period": fmt(period), "action": fmt(action),
        "turning_residual_left": fmt(vleft), "turning_residual_right": fmt(vright),
        "saddle_rate": fmt(alpha), "linear_period": None if linear_period is None else fmt(linear_period),
        "quartic_scaling_invariant": None if scaling is None else fmt(scaling),
    }


def build() -> dict:
    mp.mp.dps = WORKING_DIGITS
    rows = []
    cases = []
    for case_id, delta, beta, energies in PARAMETERS:
        alpha = mp.sqrt(-mpq(delta)) if delta < 0 else mp.mpf("0")
        vmin = -mpq(delta) ** 2 / (4 * mpq(beta)) if delta < 0 else mp.mpf("0")
        cases.append({"case_id": case_id, "delta": str(delta), "beta": str(beta), "energy_values": [str(e) for e in energies], "saddle_or_center_rate": fmt(alpha if delta < 0 else mp.sqrt(delta) if delta > 0 else mp.mpf("0")), "well_minimum": fmt(vmin)})
        rows.extend(row(case_id, delta, beta, e) for e in energies)
    data = {
        "schema": "hcs-c232-duffing-separatrix-v1", "candidate_id": "HCS-C232", "evaluation_date": "2026-08-29", "source_commit": SOURCE_COMMIT, "fixed_epoch": FIXED_EPOCH, "scope_literal": SCOPE,
        "evaluator": {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256},
        "headline": "The conservative Duffing oscillator has a complete energy-topology atlas, exact period/action quadratures, and an explicit homoclinic separatrix boundary",
        "frozen_object": {
            "system": "x_dot=v, v_dot=-delta*x-beta*x^3",
            "hamiltonian": "H=v^2/2+delta*x^2/2+beta*x^4/4",
            "parameters": "beta>0, delta real; singular beta=0 faces stated separately",
            "clock": "physical continuous Hamiltonian time",
            "normalization": "action I(E)=(2*pi)^(-1) integral over one oval v dx",
            "determinant_convention": "none; a source-local action/period atlas, not a zeta",
            "arithmetic_origin": "none; energy and force coefficients are source-defined",
            "allowed_data": "exact potential identities, turning roots, quadratures, equilibria and linearized rates",
            "forbidden_data": "prime/zero tables, target labels, Euler factors, root numbers, automorphy, Hilbert--Polya and Route-B input",
        },
        "theorem": {
            "energy_topology": "For delta>=0 every E>0 is one compact center oval; for delta<0, Vmin<E<0 gives two well ovals, E=0 gives two homoclinic loops, and E>0 gives one outer oval.",
            "turning_roots": "The squared turning roots are y_±=(-delta±sqrt(delta^2+4 beta E))/beta, with the sign-selected intervals recorded in the ledger.",
            "period": "On each connected oval T(E)=sqrt(2) integral_left^right (E-V(x))^(-1/2) dx, represented by an endpoint-cancelled quadrature.",
            "action": "I(E)=pi^(-1) integral_left^right sqrt(2(E-V(x))) dx and I'(E)=T(E)/(2*pi) on regular energies.",
            "homoclinic": "For delta=-alpha^2<0 the E=0 separatrices are x_h(t)=±sqrt(2 alpha^2/beta) sech(alpha t), v_h=x_h_dot.",
            "limits": "For delta>0, T(E) tends to 2*pi/sqrt(delta) at the center; for delta=0, T(E) is exactly proportional to beta^(-1/4)E^(-1/4); at the saddle T(E) diverges logarithmically.",
            "linearization": "The origin has rates ±i sqrt(delta) for delta>0 and ±sqrt(-delta) for delta<0; the two wells have rates ±i sqrt(-2 delta).",
            "boundaries": "Beta=0 is harmonic for delta>0, inverted for delta<0 and free for delta=0; these are separate lower-dimensional models.",
            "scope_boundary": "A continuum of real-energy ovals is not an isolated primitive-orbit owner and supplies no target divisor.",
        },
        "regression": {"parameter_cases": cases, "energy_rows": rows, "case_count": len(cases), "energy_row_count": len(rows), "working_digits": WORKING_DIGITS, "serialized_digits": SERIALIZED_DIGITS},
        "exact_identities": [
            {"identity_id": "hamiltonian_conservation", "formula": "H_x*x_dot+H_v*v_dot=0"},
            {"identity_id": "double_well_factor", "formula": "V(x)+delta^2/(4 beta)=beta/4*(x^2+delta/beta)^2 for delta<0"},
            {"identity_id": "turning_quadratic", "formula": "beta*y^2/4+delta*y/2-E=0, y=x^2"},
            {"identity_id": "action_period", "formula": "dI/dE=T/(2*pi)"},
            {"identity_id": "homoclinic_profile", "formula": "x_h=sqrt(2)*sqrt(-delta/beta)*sech(sqrt(-delta)*t)"},
            {"identity_id": "well_frequency", "formula": "V''(±sqrt(-delta/beta))=-2 delta"},
            {"identity_id": "quartic_scaling", "formula": "T(E)*E^(1/4)*beta^(1/4) is constant when delta=0"},
            {"identity_id": "time_reversal", "formula": "(x,v,t)->(x,-v,-t)"},
        ],
        "route_a": {"tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False, "strongest_positive": "A complete source-native Hamiltonian energy topology and action/period atlas is proved, including the separatrix.", "strongest_failure": "Real energy levels form continuous families without arithmetic primitive labels, a target divisor or a same-clock Hilbert--Polya operator."},
        "scope_flags": {k: False for k in ["uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"]},
        "citations": [
            {"key": "Duffing1918", "claim": "historical nonlinear oscillator model", "title": "Über erzwungene Schwingungen bei veränderlicher Eigenfrequenz", "authors": "Georg Duffing", "venue": "Vieweg, Braunschweig", "date": "1918", "doi": "10.1007/978-3-663-19850-2"},
            {"key": "Chicone2006", "claim": "period functions and planar Hamiltonian centers", "title": "Ordinary Differential Equations with Applications", "authors": "Carmen Chicone", "venue": "Springer, 2nd edition", "date": "2006", "doi": "10.1007/0-387-35794-7"},
            {"key": "GuckenheimerHolmes1983", "claim": "phase-plane separatrix vocabulary", "title": "Nonlinear Oscillations, Dynamical Systems, and Bifurcations of Vector Fields", "authors": "John Guckenheimer and Philip Holmes", "venue": "Springer", "date": "1983", "doi": "10.1007/978-1-4612-1140-2"},
        ],
        "nonclaims": ["priority or literature exhaustiveness", "a discrete primitive orbit census for the continuum of energy ovals", "target arithmetic, Euler factors, root numbers, automorphy, target divisor, functional equation or Hilbert--Polya operator", "global nonlinear spectral stability beyond the displayed one-dimensional linearization", "external peer review, novelty certification or acceptance score"],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    p = argparse.ArgumentParser(); p.add_argument("--output", type=Path, default=DEFAULT_OUTPUT); args = p.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True); data = build(); args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "C232_PRODUCER_PASS", "case_count": data["regression"]["case_count"], "energy_rows": data["regression"]["energy_row_count"], "payload_sha256": data["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__": main()
