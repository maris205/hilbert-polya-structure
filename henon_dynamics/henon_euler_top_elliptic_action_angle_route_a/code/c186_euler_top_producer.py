#!/usr/bin/env python3
"""Produce the exact C186 Euler-top regression certificate."""
from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c186_euler_top_evidence.json"
SOURCE_COMMIT = "908a6818caedb0c46195a591873a2ac9c685b55e"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"

INERTIAS = [(1, 2, 3), (1, 3, 8), (2, 5, 9), (3, 4, 10), (4, 7, 11), (5, 9, 14)]
MOMENTA = [Fraction(1), Fraction(3, 2), Fraction(2)]
FRACTIONS = [Fraction(1, 20), Fraction(1, 5), Fraction(1, 2), Fraction(4, 5), Fraction(19, 20)]


def fs(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}"


def pf(text: str) -> Fraction:
    n, d = text.split("/")
    return Fraction(int(n), int(d))


def mpf(x: Fraction) -> mp.mpf:
    return mp.mpf(x.numerator) / x.denominator


def decimal(x: mp.mpf) -> str:
    return mp.nstr(x, 62, strip_zeros=False)


def canonical_payload(data: dict) -> bytes:
    body = deepcopy(data)
    body.pop("payload_sha256", None)
    return json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def payload_hash(data: dict) -> str:
    return sha256(canonical_payload(data)).hexdigest()


def serialize(data: dict) -> bytes:
    return (json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode()


def action_cap(a: Fraction, b: Fraction, c: Fraction, e: Fraction, regime: str) -> mp.mpf:
    aa, bb, cc, ee = map(mpf, (a, b, c, e))
    if regime == "low":
        def integrand(q: mp.mpf) -> mp.mpf:
            Aq = aa * mp.cos(q) ** 2 + bb * mp.sin(q) ** 2
            return mp.sqrt((Aq - ee) / (Aq - cc))
    else:
        def integrand(q: mp.mpf) -> mp.mpf:
            Bq = bb * mp.cos(q) ** 2 + cc * mp.sin(q) ** 2
            return mp.sqrt((ee - Bq) / (aa - Bq))
    average = 2 * mp.quad(integrand, [0, mp.pi / 2]) / mp.pi
    return 1 - average


def regular_row(I: tuple[int, int, int], G: Fraction, t: Fraction, regime: str) -> dict:
    I1, I2, I3 = map(Fraction, I)
    a, b, c = 1 / I1, 1 / I2, 1 / I3
    if regime == "low":
        e = c + t * (b - c)
        A2 = (e - c) / (a - c)
        B2 = (e - c) / (b - c)
        C2 = (a - e) / (a - c)
        k2 = (a - b) * (e - c) / ((b - c) * (a - e))
        omega2 = G * G * (b - c) * (a - e)
        sphere_constant = A2 + C2 - 1
        sphere_s2 = -A2 + B2 - C2 * k2
        energy_constant = a * A2 + c * C2 - e
        energy_s2 = -a * A2 + b * B2 - c * C2 * k2
        ode1 = omega2 * A2 - G * G * (b - c) ** 2 * B2 * C2
        ode2 = omega2 * B2 - G * G * (a - c) ** 2 * A2 * C2
        ode3 = omega2 * k2 * k2 * C2 - G * G * (a - b) ** 2 * A2 * B2
        chart = "(A cn(u,k), B sn(u,k), sigma C dn(u,k)); u=sigma Omega(t-t0)"
    elif regime == "high":
        e = b + t * (a - b)
        A2 = (e - c) / (a - c)
        B2 = (a - e) / (a - b)
        C2 = (a - e) / (a - c)
        k2 = (b - c) * (a - e) / ((a - b) * (e - c))
        omega2 = G * G * (a - b) * (e - c)
        sphere_constant = A2 + C2 - 1
        sphere_s2 = -A2 * k2 + B2 - C2
        energy_constant = a * A2 + c * C2 - e
        energy_s2 = -a * A2 * k2 + b * B2 - c * C2
        ode1 = omega2 * A2 * k2 * k2 - G * G * (b - c) ** 2 * B2 * C2
        ode2 = omega2 * B2 - G * G * (a - c) ** 2 * A2 * C2
        ode3 = omega2 * C2 - G * G * (a - b) ** 2 * A2 * B2
        chart = "(sigma A dn(u,k), B sn(u,k), C cn(u,k)); u=sigma Omega(t-t0)"
    else:
        raise ValueError(regime)
    period = 4 * mp.ellipk(mpf(k2)) / mp.sqrt(mpf(omega2))
    cap = action_cap(a, b, c, e, regime)
    residuals = [sphere_constant, sphere_s2, energy_constant, energy_s2, ode1, ode2, ode3]
    assert all(x == 0 for x in residuals)
    assert 0 < k2 < 1
    return {
        "row_id": f"I{I1}-{I2}-{I3}_G{fs(G)}_{regime}_t{fs(t)}",
        "inertia": [fs(I1), fs(I2), fs(I3)],
        "inverse_inertia": [fs(a), fs(b), fs(c)],
        "G": fs(G),
        "fraction_to_separatrix": fs(t),
        "regime": regime,
        "normalized_energy_e_equals_2E_over_G2": fs(e),
        "amplitude_squares": {"A2": fs(A2), "B2": fs(B2), "C2": fs(C2)},
        "modulus_square": fs(k2),
        "frequency_square": fs(omega2),
        "minimal_period": decimal(period),
        "normalized_kks_cap_action": decimal(cap),
        "component_count": 2,
        "elliptic_chart": chart,
        "exact_residuals": [fs(x) for x in residuals],
    }


def equilibrium_rows() -> list[dict]:
    rows = []
    for I in INERTIAS:
        a, b, c = (Fraction(1, I[0]), Fraction(1, I[1]), Fraction(1, I[2]))
        for G in MOMENTA:
            values = {
                1: (-G * G * (a - b) * (a - c), "elliptic_stable"),
                2: (G * G * (a - b) * (b - c), "hyperbolic_unstable"),
                3: (-G * G * (a - c) * (b - c), "elliptic_stable"),
            }
            for axis, (lambda_square, kind) in values.items():
                rows.append({
                    "inertia": [f"{x}/1" for x in I],
                    "G": fs(G),
                    "axis": axis,
                    "signs": [1, -1],
                    "tangent_rate_square": fs(lambda_square),
                    "classification": kind,
                })
    return rows


def separatrix_rows() -> list[dict]:
    rows = []
    for I in INERTIAS:
        a, b, c = (Fraction(1, I[0]), Fraction(1, I[1]), Fraction(1, I[2]))
        for G in MOMENTA:
            A2 = (b - c) / (a - c)
            C2 = (a - b) / (a - c)
            rate2 = G * G * (a - b) * (b - c)
            rows.append({
                "inertia": [f"{x}/1" for x in I],
                "G": fs(G),
                "normalized_energy": fs(b),
                "A2": fs(A2),
                "C2": fs(C2),
                "rate_square": fs(rate2),
                "formula": "m1=epsilon*A*sech(u), m2=tanh(u), m3=epsilon*sigma*C*sech(u), u=sigma*rho*(t-t0)",
                "heteroclinic_branches": 4,
                "endpoint_axes": ["+e2", "-e2"],
            })
    return rows


def divergence_rows() -> list[dict]:
    rows = []
    deltas = [Fraction(1, 10), Fraction(1, 100), Fraction(1, 1000), Fraction(1, 10000)]
    for I in INERTIAS:
        a, b, c = (Fraction(1, I[0]), Fraction(1, I[1]), Fraction(1, I[2]))
        G = Fraction(1)
        for regime in ("low", "high"):
            periods = []
            for delta in deltas:
                if regime == "low":
                    e = b - delta * (b - c)
                    k2 = (a - b) * (e - c) / ((b - c) * (a - e))
                    omega2 = G * G * (b - c) * (a - e)
                else:
                    e = b + delta * (a - b)
                    k2 = (b - c) * (a - e) / ((a - b) * (e - c))
                    omega2 = G * G * (a - b) * (e - c)
                periods.append(decimal(4 * mp.ellipk(mpf(k2)) / mp.sqrt(mpf(omega2))))
            rows.append({"inertia": [f"{x}/1" for x in I], "regime": regime, "relative_deltas": [fs(x) for x in deltas], "periods": periods})
    return rows


def build_evidence() -> dict:
    mp.mp.dps = 90
    regular = [regular_row(I, G, t, regime) for I in INERTIAS for G in MOMENTA for regime in ("low", "high") for t in FRACTIONS]
    equilibria = equilibrium_rows()
    separatrices = separatrix_rows()
    divergences = divergence_rows()
    data = {
        "schema": "hcs-c186-euler-top-v1",
        "metadata": {
            "candidate_id": "HCS-C186",
            "evaluation_date": "2026-08-26",
            "source_commit": SOURCE_COMMIT,
            "scope_literal": SCOPE,
            "precision": "exact rational identities plus 62-digit elliptic quadratures",
            "training_data": "none",
            "target_tables_used": 0,
            "primary_sources": [
                {"authors": "Celledoni--Fasso--Safstrom--Zanna", "doi": "10.1137/070704393", "role": "exact free-rigid-body elliptic solution"},
                {"authors": "Pina", "url": "https://arxiv.org/abs/1505.06186", "role": "Jacobi-coordinate solution and period conventions"},
            ],
        },
        "theorem": {
            "family": "all I1<I2<I3, all G>0, and the full normalized energy interval c<=e<=a",
            "equations": "Mdot=M cross I^{-1}M; G^2=sum M_i^2; 2E=sum M_i^2/I_i",
            "regular_energy_topology": "two periodic circles for c<e<b and two periodic circles for b<e<a",
            "endpoint_topology": "two stable fixed points at each of e=c and e=a",
            "separatrix_topology": "four heteroclinic branches joining the two hyperbolic e2-axis rotations at e=b",
            "poisson_convention": "{F,H}=-M dot (grad F cross grad H); Fdot={F,H}; Mdot=M cross grad H",
            "canonical_action_charts": "positive low: q=arg(M1+iM2), P3=G-M3, {q,P3}=1; positive high: q=arg(M2+iM3), P1=G-M1, {q,P1}=1",
            "action_angle": "Jacobi phase gives angle theta=pi*u/(2K(k)); KKS cap area divided by 2pi gives action and |dJ/dE|=T/(2pi)",
            "time_map_fixed_sets": "for tau>0, Phi_tau^n fixes a whole regular energy circle iff n*tau is an integer multiple of its minimal period; equilibria are always fixed and no heteroclinic interior point is fixed",
            "ordinary_zeta_boundary": "resonant fixed sets are positive-dimensional, so an isolated finite Artin--Mazur fixed-point count is not defined on the full sphere",
        },
        "regular_rows": regular,
        "equilibrium_rows": equilibria,
        "separatrix_rows": separatrices,
        "period_divergence_rows": divergences,
        "fixed_time_map": {
            "positive_time_assumption": True,
            "regular_condition": "n*tau=q*T(e) for an integer q>=1",
            "fixed_component_dimension": 1,
            "equilibrium_fixed_points": 6,
            "separatrix_interior_fixed_points": 0,
            "artin_mazur_finite_count_available": False,
        },
        "route_a": {
            "A0": "A0_FAIL",
            "A1": "A1_WEAK",
            "A2": "A2_FAIL",
            "A3": "A3_FAIL",
            "A4": "A4_NATURAL_QUANTIZATION",
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "qualification": "Hamiltonian KKS flow has a canonical unitary Koopman group, but no intrinsic rational-prime origin, logarithmic clock, or target divisor",
        },
        "summary": {
            "regular_rows": len(regular),
            "equilibrium_rows": len(equilibria),
            "separatrix_rows": len(separatrices),
            "divergence_rows": len(divergences),
            "exact_regular_residual_cells": 7 * len(regular),
            "all_parameter_theorem_status": "PROVED_IN_THEOREM_PACKAGE",
            "finite_rows_role": "REGRESSION_ONLY",
        },
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    data = build_evidence()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(serialize(data))
    print(json.dumps({
        "status": "C186_PRODUCER_PASS",
        "regular_rows": data["summary"]["regular_rows"],
        "exact_residual_cells": data["summary"]["exact_regular_residual_cells"],
        "payload_sha256": data["payload_sha256"],
        "evidence_sha256": sha256(OUTPUT.read_bytes()).hexdigest(),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
