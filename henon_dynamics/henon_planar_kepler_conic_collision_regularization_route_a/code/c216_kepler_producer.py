#!/usr/bin/env python3
"""Produce the exact C216 planar Kepler theorem/evidence receipt.

The machine-readable payload is deliberately a regression oracle.  The
all-parameter statements live in ``THEOREM_PACKAGE.md`` and the manuscript;
the finite rows exercise every sign and boundary convention used there.
"""
from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
from hashlib import sha256
import argparse
import json
from math import isqrt
from pathlib import Path

import mpmath as mp


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c216_kepler_evidence.json"
SOURCE_COMMIT = "077a098ac5811e465b69db71b5e6031a4827eb55"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"


def fs(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}"


def ff(text: str) -> Fraction:
    n, d = text.split("/")
    return Fraction(int(n), int(d))


def mpm(x: Fraction) -> mp.mpf:
    return mp.mpf(x.numerator) / x.denominator


def dec(x: mp.mpf, digits: int = 68) -> str:
    return mp.nstr(x, digits, strip_zeros=False)


def canonical_hash(data: dict) -> str:
    body = deepcopy(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def serialize(data: dict) -> bytes:
    return (json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode()


def vec_norm_sq(v: tuple[Fraction, Fraction]) -> Fraction:
    return v[0] * v[0] + v[1] * v[1]


def dot(a: tuple[Fraction, Fraction], b: tuple[Fraction, Fraction]) -> Fraction:
    return a[0] * b[0] + a[1] * b[1]


def angular(q: tuple[Fraction, Fraction], p: tuple[Fraction, Fraction]) -> Fraction:
    return q[0] * p[1] - q[1] * p[0]


def runge_lenz(mu: Fraction, q: tuple[Fraction, Fraction], p: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    r2 = vec_norm_sq(q)
    # All released probes have rational r; this keeps the receipt exact.
    r = Fraction(isqrt(r2.numerator), isqrt(r2.denominator))
    assert r * r == r2
    pp = vec_norm_sq(p)
    qp = dot(q, p)
    return ((pp - mu / r) * q[0] - qp * p[0],
            (pp - mu / r) * q[1] - qp * p[1])


def energy(mu: Fraction, q: tuple[Fraction, Fraction], p: tuple[Fraction, Fraction]) -> Fraction:
    r2 = vec_norm_sq(q)
    r = Fraction(isqrt(r2.numerator), isqrt(r2.denominator))
    assert r * r == r2
    return vec_norm_sq(p) / 2 - mu / r


def radius(q: tuple[Fraction, Fraction]) -> Fraction:
    r2 = vec_norm_sq(q)
    r = Fraction(isqrt(r2.numerator), isqrt(r2.denominator))
    assert r * r == r2
    return r


def radial_action_numeric(mu: Fraction, e: Fraction, ell: Fraction) -> mp.mpf:
    """Independent quadrature for (1/pi) integral p_r dr on an ellipse."""
    mm, ee, ll = map(mpm, (mu, e, ell))
    aa = -mm / (2 * ee)
    ecc2 = 1 + 2 * ee * ll * ll / (mm * mm)
    ecc = mp.sqrt(ecc2)
    lo, hi = aa * (1 - ecc), aa * (1 + ecc)
    half, mid = (hi - lo) / 2, (hi + lo) / 2

    def integrand(theta: mp.mpf) -> mp.mpf:
        r = mid + half * mp.cos(theta)
        rad = 2 * (ee + mm / r) - ll * ll / (r * r)
        if rad < 0 and abs(rad) < mp.mpf("1e-75"):
            rad = mp.mpf("0")
        return half * mp.sin(theta) * mp.sqrt(max(rad, mp.mpf("0")))

    return mp.quad(integrand, [0, mp.pi]) / mp.pi


def orbital_period(mu: Fraction, e: Fraction) -> mp.mpf:
    mm, ee = mpm(mu), mpm(e)
    return 2 * mp.pi * mm / (-2 * ee) ** mp.mpf("1.5")


def radial_action_formula(mu: Fraction, e: Fraction, ell: Fraction) -> mp.mpf:
    return mpm(mu) / mp.sqrt(-2 * mpm(e)) - abs(mpm(ell))


def scattering_angle(mu: Fraction, e: Fraction, ell: Fraction) -> mp.mpf:
    # e here is the energy; eccentricity is reconstructed from the identity.
    ecc2 = 1 + 2 * mpm(e) * mpm(ell) ** 2 / mpm(mu) ** 2
    return 2 * mp.asin(1 / mp.sqrt(ecc2))


def orbit_samples() -> list[tuple[str, Fraction, tuple[Fraction, Fraction], tuple[Fraction, Fraction]]]:
    # q=(r,0), with every r a rational square so the Levi--Civita lift is exact.
    return [
        ("elliptic_unit", Fraction(1), (Fraction(1), Fraction(0)), (Fraction(0), Fraction(1, 2))),
        ("elliptic_large_radius", Fraction(3, 2), (Fraction(4), Fraction(0)), (Fraction(1, 2), Fraction(1, 2))),
        ("elliptic_oblique", Fraction(2), (Fraction(9, 4), Fraction(0)), (Fraction(1, 3), Fraction(2, 3))),
        ("elliptic_reverse_orientation", Fraction(2), (Fraction(1), Fraction(0)), (Fraction(1, 2), Fraction(-1, 2))),
        ("parabolic_unit", Fraction(1), (Fraction(1), Fraction(0)), (Fraction(1), Fraction(1))),
        ("parabolic_radius_four", Fraction(2), (Fraction(4), Fraction(0)), (Fraction(0), Fraction(1))),
        ("hyperbolic_unit", Fraction(1), (Fraction(1), Fraction(0)), (Fraction(2), Fraction(1))),
        ("hyperbolic_radius_four", Fraction(2), (Fraction(4), Fraction(0)), (Fraction(1), Fraction(2))),
        ("hyperbolic_oblique", Fraction(3, 2), (Fraction(9, 4), Fraction(0)), (Fraction(1), Fraction(1))),
        ("hyperbolic_reverse", Fraction(1), (Fraction(4), Fraction(0)), (Fraction(-1), Fraction(1))),
    ]


def orbit_row(name: str, mu: Fraction, q: tuple[Fraction, Fraction], p: tuple[Fraction, Fraction]) -> dict:
    r = radius(q)
    ee = energy(mu, q, p)
    ell = angular(q, p)
    aa = runge_lenz(mu, q, p)
    aa2 = vec_norm_sq(aa)
    ecc2 = aa2 / (mu * mu)
    identity = aa2 - (mu * mu + 2 * ee * ell * ell)
    conic = mu * r + dot(aa, q) - ell * ell
    if ee < 0:
        kind = "ellipse"
    elif ee == 0:
        kind = "parabola"
    else:
        kind = "hyperbola"
    row = {
        "row_id": name,
        "mu": fs(mu),
        "q": [fs(q[0]), fs(q[1])],
        "p": [fs(p[0]), fs(p[1])],
        "radius": fs(r),
        "energy": fs(ee),
        "angular_momentum": fs(ell),
        "runge_lenz": [fs(aa[0]), fs(aa[1])],
        "runge_lenz_norm_square": fs(aa2),
        "eccentricity_square": fs(ecc2),
        "energy_identity_residual": fs(identity),
        "conic_residual": fs(conic),
        "conic_type": kind,
        "conic_equation": "mu*|q| + A·q = L^2; r=(L^2/mu)/(1+e*cos(theta))",
        "negative_energy_period": None,
        "radial_action_formula": None,
        "radial_action_quadrature": None,
        "hyperbolic_scattering_angle": None,
    }
    if kind == "ellipse":
        period = orbital_period(mu, ee)
        action = radial_action_formula(mu, ee, ell)
        quadrature = radial_action_numeric(mu, ee, ell)
        row["negative_energy_period"] = dec(period)
        row["radial_action_formula"] = dec(action)
        row["radial_action_quadrature"] = dec(quadrature)
    elif kind == "hyperbola":
        row["hyperbolic_scattering_angle"] = dec(scattering_angle(mu, ee, ell))
    return row


def collision_time(mu: Fraction, ee: Fraction, r0: Fraction) -> mp.mpf:
    """Time integral from r0 to collision on the inward radial branch."""
    mm, e, r = mpm(mu), mpm(ee), mpm(r0)
    if ee < 0:
        alpha = -e
        # r0 is the apocentre in the released negative-energy rows.
        u = mp.asin(mp.sqrt(alpha * r / mm))
        return mm / (mp.sqrt(2) * alpha ** mp.mpf("1.5")) * (u - mp.sin(u) * mp.cos(u))
    if ee == 0:
        return 2 * r ** mp.mpf("1.5") / (3 * mp.sqrt(2 * mm))
    u = mp.asinh(mp.sqrt(e * r / mm))
    return mm / (mp.sqrt(2) * e ** mp.mpf("1.5")) * (mp.sinh(u) * mp.cosh(u) - u)


def radial_rows() -> list[dict]:
    data = [
        ("bound_apocentre", Fraction(1), Fraction(-1, 2), Fraction(2), Fraction(0)),
        ("bound_apocentre_scaled", Fraction(2), Fraction(-1, 4), Fraction(8), Fraction(0)),
        ("parabolic_infall", Fraction(2), Fraction(0), Fraction(1), Fraction(-2)),
        ("hyperbolic_infall", Fraction(2), Fraction(5, 2), Fraction(1), Fraction(-3)),
    ]
    rows = []
    for name, mu, ee, r0, vr in data:
        t = collision_time(mu, ee, r0)
        rows.append({
            "row_id": name,
            "mu": fs(mu),
            "energy": fs(ee),
            "initial_radius": fs(r0),
            "initial_radial_velocity": fs(vr),
            "angular_momentum": "0/1",
            "collision_integral": "integral_0^r0 dr/sqrt(2*(E+mu/r))",
            "collision_time": dec(t),
            "finite_positive_time": True,
            "physical_flow_incomplete_at_collision": True,
        })
    return rows


def square_root_fraction(x: Fraction) -> Fraction:
    n, d = isqrt(x.numerator), isqrt(x.denominator)
    assert n * n == x.numerator and d * d == x.denominator
    return Fraction(n, d)


def lc_row(name: str, mu: Fraction, q: tuple[Fraction, Fraction], p: tuple[Fraction, Fraction]) -> dict:
    r = radius(q)
    assert q[1] == 0 and q[0] > 0
    u = square_root_fraction(r)
    ee = energy(mu, q, p)
    ell = angular(q, p)
    # z=u^2 and dt=|u|^2 d tau; with u real at the probe,
    # p_complex = 2 u'/conj(u).
    up = (p[0] * u / 2, p[1] * u / 2)
    upp = (ee * u / 2, Fraction(0))
    constraint = 2 * vec_norm_sq(up) - ee * u * u - mu
    lift_l = 2 * u * up[1]
    rec_p = (2 * up[0] / u, 2 * up[1] / u)
    return {
        "row_id": name,
        "mu": fs(mu),
        "energy": fs(ee),
        "physical_q": [fs(q[0]), fs(q[1])],
        "physical_p": [fs(p[0]), fs(p[1])],
        "u": [fs(u), "0/1"],
        "u_prime": [fs(up[0]), fs(up[1])],
        "u_double_prime": [fs(upp[0]), fs(upp[1])],
        "constraint_residual": fs(constraint),
        "angular_momentum_residual": fs(lift_l - ell),
        "reconstructed_p": [fs(rec_p[0]), fs(rec_p[1])],
        "equation": "u''=(E/2)u; 2|u'|^2-E|u|^2=mu; L=2 Im(conj(u)u')",
        "time_change": "dt=|u|^2 d tau",
    }


def collision_lc_rows() -> list[dict]:
    rows = []
    for name, ee in (("collision_negative", Fraction(-1)), ("collision_zero", Fraction(0)), ("collision_positive", Fraction(1))):
        mu = Fraction(2)
        u = (Fraction(0), Fraction(0))
        up = (Fraction(1), Fraction(0))
        constraint = 2 * vec_norm_sq(up) - ee * vec_norm_sq(u) - mu
        rows.append({
            "row_id": name,
            "mu": fs(mu),
            "energy": fs(ee),
            "u": ["0/1", "0/1"],
            "u_prime": ["1/1", "0/1"],
            "u_double_prime": ["0/1", "0/1"],
            "constraint_residual": fs(constraint),
            "configuration_point_is_collision": True,
            "regularized_tau_equation": "u''=(E/2)u is smooth through u=0",
            "physical_q_map": "q=u^2; physical time density dt/dtau=|u|^2 vanishes",
            "full_symplectomorphism_claim": False,
        })
    return rows


def fixed_rows() -> list[dict]:
    rows = []
    for name, mu, ee in (("negative_shell_1", Fraction(1), Fraction(-1, 2)),
                         ("negative_shell_2", Fraction(3, 2), Fraction(-1, 8)),
                         ("negative_shell_3", Fraction(2), Fraction(-1, 4))):
        period = orbital_period(mu, ee)
        rows.append({
            "row_id": name,
            "mu": fs(mu),
            "energy": fs(ee),
            "period": dec(period),
            "strobe": "T=m*T(E), m>=1; n*tau=m*T(E) (integer strobe multiple)",
            "fixed_set_description": "{H=E, L != 0} (collision-free energy shell)",
            "fixed_set_dimension": 3,
            "isolated_artin_mazur_count_defined": False,
            "reason": "Kepler period depends only on E, so the whole negative-energy shell resonates",
        })
    for name, ee in (("parabolic_boundary", Fraction(0)), ("hyperbolic_boundary", Fraction(1))):
        rows.append({
            "row_id": name,
            "mu": "1/1",
            "energy": fs(ee),
            "period": None,
            "strobe": "any positive tau",
            "fixed_set_description": "no noncollision periodic orbit",
            "fixed_set_dimension": 0,
            "isolated_artin_mazur_count_defined": False,
            "reason": "parabolic/hyperbolic trajectories escape and have no finite period",
        })
    return rows


def build() -> dict:
    mp.mp.dps = 100
    orbits = [orbit_row(*item) for item in orbit_samples()]
    lc = [lc_row(*item) for item in orbit_samples()[:9]] + collision_lc_rows()
    radial = radial_rows()
    fixed = fixed_rows()
    data = {
        "schema": "hcs-c216-planar-kepler-v1",
        "metadata": {
            "candidate_id": "HCS-C216",
            "evaluation_date": "2026-08-28",
            "source_commit": SOURCE_COMMIT,
            "evaluator": {"name": "route-a-evaluator", "version": "0.2.0", "sha256": EVALUATOR_SHA256},
            "scope_literal": SCOPE,
            "precision": "exact rational identities plus 68-digit mpmath quadratures",
            "training_data": "none",
            "target_tables_used": 0,
            "forbidden_data": ["prime tables", "Riemann-zero tables", "Euler factors", "root numbers", "fitted target clocks"],
            "primary_sources": [
                {"key": "LC1920", "authors": "Tullio Levi-Civita", "title": "Sur la régularisation du problème des trois corps", "doi": "10.1007/BF02404404", "role": "historical collision regularization"},
                {"key": "MOS70", "authors": "Jürgen Moser", "title": "Regularization of Kepler's problem and the averaging method on a manifold", "doi": "10.1002/cpa.3160230406", "role": "fixed-energy regularization and global geometry"},
                {"key": "LS76", "authors": "Thomas Ligon and Manfred Schaaf", "title": "On the global symmetry of the classical Kepler problem", "doi": "10.1016/0034-4877(76)90061-6", "role": "global Runge–Lenz symmetry context"},
            ],
        },
        "theorem": {
            "phase_space": "(q,p) in (R^2\\{0}) x R^2 with H=|p|^2/2-mu/|q|, mu>0",
            "equations": "qdot=p, pdot=-mu*q/|q|^3",
            "invariants": "E=H; L=q1*p2-q2*p1; A=(|p|^2-mu/r)q-(q.p)p",
            "identities": "A.q=L^2-mu*r and |A|^2=mu^2+2*E*L^2",
            "conic": "for L!=0, r=(L^2/mu)/(1+e cos(theta)), e=|A|/mu",
            "classification": "E<0 ellipse, E=0 parabola, E>0 hyperbola",
            "period": "T(E)=2*pi*mu*(-2E)^(-3/2) for E<0",
            "radial_action": "J_r=(1/(2*pi))*closed_integral p_r dr=(1/pi)*integral_{r_-}^{r_+} p_r dr=mu/sqrt(-2E)-|L| for E<0",
            "scattering": "chi=2 asin(1/e) for E>0",
            "radial_boundary": "L=0 has finite inward collision time integral and the physical flow is incomplete at q=0",
            "levi_civita": "q=u^2, dt=|u|^2 d tau; u''=(E/2)u and 2|u'|^2-E|u|^2=mu",
            "collision_scope": "the configuration collision is smoothly represented in the tau equation; no full Ligon--Schaaf symplectomorphism is claimed",
            "strobe": "for a time-T map, fixed points on E<0 include the collision-free shell whenever T=m*T(E), m>=1; this is a positive-dimensional continuum, so ordinary isolated-orbit Artin--Mazur counting stops",
        },
        "orbit_rows": orbits,
        "radial_collision_rows": radial,
        "levi_civita_rows": lc,
        "fixed_set_rows": fixed,
        "route_a": {
            "tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "qualification": "The Coulomb Hamiltonian and Levi--Civita oscillator give a natural classical quantization hint, but no intrinsic prime carrier, logarithmic clock, target divisor, or Hilbert--Polya operator is constructed.",
        },
        "attribution": {
            "status": "SOURCE_ATTRIBUTED_SYNTHESIS",
            "classical_ownership": "Levi-Civita, Moser, and Ligon--Schaaf retain ownership of the classical regularization/symmetry results",
            "package_contribution": "convention-locked planar all-energy conic, collision, action, scattering, and strobe-boundary ledger with independent executable checks",
            "priority_claim": False,
        },
        "nonclaims": [
            "a priority claim for the Kepler problem, Levi--Civita regularization, Moser regularization, or Ligon--Schaaf symmetry",
            "a full global Ligon--Schaaf symplectomorphism or a three-dimensional regularization theorem",
            "a target prime correspondence, Euler product, root number, automorphy, functional equation, or Riemann-zero match",
            "an isolated primitive-orbit zeta on resonant negative-energy shells",
            "a Hilbert--Pólya operator, Route-B authorization, external peer review, or acceptance score",
        ],
        "summary": {
            "orbit_row_count": len(orbits),
            "radial_collision_row_count": len(radial),
            "levi_civita_row_count": len(lc),
            "fixed_set_row_count": len(fixed),
            "exact_identity_cells": 3 * len(orbits) + 2 * len(lc) + len(radial),
            "all_parameter_theorem_status": "PROVED_IN_THEOREM_PACKAGE",
            "finite_rows_role": "REGRESSION_ONLY",
        },
    }
    data["payload_sha256"] = canonical_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(serialize(data))
    print(json.dumps({
        "status": "C216_PRODUCER_PASS",
        "orbit_rows": data["summary"]["orbit_row_count"],
        "radial_rows": data["summary"]["radial_collision_row_count"],
        "levi_civita_rows": data["summary"]["levi_civita_row_count"],
        "fixed_rows": data["summary"]["fixed_set_row_count"],
        "payload_sha256": data["payload_sha256"],
        "evidence_sha256": sha256(args.output.read_bytes()).hexdigest(),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
