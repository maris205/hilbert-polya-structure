#!/usr/bin/env python3
"""Producer-independent checker for the C216 Kepler receipt.

This file intentionally repeats the algebra and the numerical quadratures
instead of importing the producer.  It is also used by the hostile mutation
harness, so every semantic field is checked after the payload hash is
repaired.
"""
from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
from hashlib import sha256
import json
import os
from math import isqrt
from pathlib import Path
import sys

import mpmath as mp


ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c216_kepler_evidence.json"
EXPECTED_COMMIT = "077a098ac5811e465b69db71b5e6031a4827eb55"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
FAST = os.environ.get("C216_MUTATION_FAST") == "1"


def F(text: str) -> Fraction:
    n, d = text.split("/")
    return Fraction(int(n), int(d))


def fs(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}"


def M(x: Fraction) -> mp.mpf:
    return mp.mpf(x.numerator) / x.denominator


def h(payload: dict) -> str:
    body = deepcopy(payload)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def close(text: str, value: mp.mpf, tol: str = "1e-54") -> bool:
    return abs(mp.mpf(text) - value) <= mp.mpf(tol) * max(1, abs(value))


def radius(q: tuple[Fraction, Fraction]) -> Fraction:
    n = q[0] * q[0] + q[1] * q[1]
    a, b = isqrt(n.numerator), isqrt(n.denominator)
    if a * a != n.numerator or b * b != n.denominator:
        raise AssertionError("probe radius is not an exact rational square")
    return Fraction(a, b)


def dot(x, y):
    return x[0] * y[0] + x[1] * y[1]


def norm2(x):
    return dot(x, x)


def energy(mu, q, p):
    return norm2(p) / 2 - mu / radius(q)


def angular(q, p):
    return q[0] * p[1] - q[1] * p[0]


def runge(mu, q, p):
    r = radius(q)
    return ((norm2(p) - mu / r) * q[0] - dot(q, p) * p[0],
            (norm2(p) - mu / r) * q[1] - dot(q, p) * p[1])


def period(mu, ee):
    return 2 * mp.pi * M(mu) / (-2 * M(ee)) ** mp.mpf("1.5")


def action_formula(mu, ee, ell):
    return M(mu) / mp.sqrt(-2 * M(ee)) - abs(M(ell))


def action_integral(mu, ee, ell):
    mm, e, ll = M(mu), M(ee), M(ell)
    aa = -mm / (2 * e)
    ecc = mp.sqrt(1 + 2 * e * ll * ll / (mm * mm))
    lo, hi = aa * (1 - ecc), aa * (1 + ecc)
    mid, half = (hi + lo) / 2, (hi - lo) / 2

    def f(theta):
        r = mid + half * mp.cos(theta)
        rad = 2 * (e + mm / r) - ll * ll / (r * r)
        if rad < 0 and abs(rad) < mp.mpf("1e-75"):
            rad = 0
        return half * mp.sin(theta) * mp.sqrt(max(rad, mp.mpf("0")))

    return mp.quad(f, [0, mp.pi]) / mp.pi


def scatter(mu, ee, ell):
    ecc = mp.sqrt(1 + 2 * M(ee) * M(ell) ** 2 / M(mu) ** 2)
    return 2 * mp.asin(1 / ecc)


def radial_collision(mu, ee, r0):
    mm, e, r = M(mu), M(ee), M(r0)
    if ee < 0:
        alpha = -e
        u = mp.asin(mp.sqrt(alpha * r / mm))
        return mm / (mp.sqrt(2) * alpha ** mp.mpf("1.5")) * (u - mp.sin(u) * mp.cos(u))
    if ee == 0:
        return 2 * r ** mp.mpf("1.5") / (3 * mp.sqrt(2 * mm))
    u = mp.asinh(mp.sqrt(e * r / mm))
    return mm / (mp.sqrt(2) * e ** mp.mpf("1.5")) * (mp.sinh(u) * mp.cosh(u) - u)


def expected_orbits():
    z = Fraction(0)
    return [
        ("elliptic_unit", Fraction(1), (Fraction(1), z), (z, Fraction(1, 2))),
        ("elliptic_large_radius", Fraction(3, 2), (Fraction(4), z), (Fraction(1, 2), Fraction(1, 2))),
        ("elliptic_oblique", Fraction(2), (Fraction(9, 4), z), (Fraction(1, 3), Fraction(2, 3))),
        ("elliptic_reverse_orientation", Fraction(2), (Fraction(1), z), (Fraction(1, 2), Fraction(-1, 2))),
        ("parabolic_unit", Fraction(1), (Fraction(1), z), (Fraction(1), Fraction(1))),
        ("parabolic_radius_four", Fraction(2), (Fraction(4), z), (z, Fraction(1))),
        ("hyperbolic_unit", Fraction(1), (Fraction(1), z), (Fraction(2), Fraction(1))),
        ("hyperbolic_radius_four", Fraction(2), (Fraction(4), z), (Fraction(1), Fraction(2))),
        ("hyperbolic_oblique", Fraction(3, 2), (Fraction(9, 4), z), (Fraction(1), Fraction(1))),
        ("hyperbolic_reverse", Fraction(1), (Fraction(4), z), (Fraction(-1), Fraction(1))),
    ]


def exact_keys(obj: dict, keys: set[str], where: str) -> None:
    if set(obj) != keys:
        raise AssertionError(f"{where} keys differ: {sorted(set(obj) ^ keys)}")


def check(path: Path) -> int:
    mp.mp.dps = 92
    d = json.loads(path.read_text())
    n = 0

    def req(condition: bool, message: str = ""):
        nonlocal n
        n += 1
        if not condition:
            raise AssertionError(f"assertion {n} failed {message}")

    exact_keys(d, {"schema", "metadata", "theorem", "orbit_rows", "radial_collision_rows", "levi_civita_rows", "fixed_set_rows", "route_a", "attribution", "nonclaims", "summary", "payload_sha256"}, "root")
    req(d["schema"] == "hcs-c216-planar-kepler-v1")
    req(d["payload_sha256"] == h(d))

    meta = d["metadata"]
    exact_keys(meta, {"candidate_id", "evaluation_date", "source_commit", "evaluator", "scope_literal", "precision", "training_data", "target_tables_used", "forbidden_data", "primary_sources"}, "metadata")
    req(meta["candidate_id"] == "HCS-C216")
    req(meta["evaluation_date"] == "2026-08-28")
    req(meta["source_commit"] == EXPECTED_COMMIT)
    req(meta["scope_literal"] == SCOPE)
    req(meta["training_data"] == "none")
    req(meta["target_tables_used"] == 0)
    req(meta["evaluator"] == {"name": "route-a-evaluator", "version": "0.2.0", "sha256": EVALUATOR_SHA256})
    req(len(meta["primary_sources"]) == 3)
    source_keys = {"key", "authors", "title", "doi", "role"}
    for i, src in enumerate(meta["primary_sources"]):
        exact_keys(src, source_keys, f"primary_sources[{i}]")
    req(meta["primary_sources"][0]["doi"] == "10.1007/BF02404404")
    req(meta["primary_sources"][1]["doi"] == "10.1002/cpa.3160230406")
    req(meta["primary_sources"][2]["doi"] == "10.1016/0034-4877(76)90061-6")

    theorem = d["theorem"]
    theorem_keys = {"phase_space", "equations", "invariants", "identities", "conic", "classification", "period", "radial_action", "scattering", "radial_boundary", "levi_civita", "collision_scope", "strobe"}
    exact_keys(theorem, theorem_keys, "theorem")
    req(theorem["phase_space"] == "(q,p) in (R^2\\{0}) x R^2 with H=|p|^2/2-mu/|q|, mu>0")
    req(theorem["equations"] == "qdot=p, pdot=-mu*q/|q|^3")
    req(theorem["identities"] == "A.q=L^2-mu*r and |A|^2=mu^2+2*E*L^2")
    req(theorem["classification"] == "E<0 ellipse, E=0 parabola, E>0 hyperbola")
    req(theorem["period"] == "T(E)=2*pi*mu*(-2E)^(-3/2) for E<0")
    req(theorem["radial_action"] == "J_r=(1/(2*pi))*closed_integral p_r dr=(1/pi)*integral_{r_-}^{r_+} p_r dr=mu/sqrt(-2E)-|L| for E<0")
    req(theorem["scattering"] == "chi=2 asin(1/e) for E>0")
    req(theorem["levi_civita"] == "q=u^2, dt=|u|^2 d tau; u''=(E/2)u and 2|u'|^2-E|u|^2=mu")

    orbit_keys = {"row_id", "mu", "q", "p", "radius", "energy", "angular_momentum", "runge_lenz", "runge_lenz_norm_square", "eccentricity_square", "energy_identity_residual", "conic_residual", "conic_type", "conic_equation", "negative_energy_period", "radial_action_formula", "radial_action_quadrature", "hyperbolic_scattering_angle"}
    req(len(d["orbit_rows"]) == 10)
    for row, (name, mu, q, p) in zip(d["orbit_rows"], expected_orbits()):
        exact_keys(row, orbit_keys, f"orbit {name}")
        req(row["row_id"] == name)
        req(F(row["mu"]) == mu and [F(x) for x in row["q"]] == list(q) and [F(x) for x in row["p"]] == list(p), name)
        r, ee, ell, aa = radius(q), energy(mu, q, p), angular(q, p), runge(mu, q, p)
        req(F(row["radius"]) == r and F(row["energy"]) == ee and F(row["angular_momentum"]) == ell, name)
        req([F(x) for x in row["runge_lenz"]] == list(aa), name)
        req(F(row["runge_lenz_norm_square"]) == norm2(aa), name)
        req(F(row["eccentricity_square"]) == norm2(aa) / (mu * mu), name)
        req(F(row["energy_identity_residual"]) == norm2(aa) - (mu * mu + 2 * ee * ell * ell), name)
        req(F(row["conic_residual"]) == mu * r + dot(aa, q) - ell * ell, name)
        kind = "ellipse" if ee < 0 else ("parabola" if ee == 0 else "hyperbola")
        req(row["conic_type"] == kind and row["conic_equation"] == "mu*|q| + A·q = L^2; r=(L^2/mu)/(1+e*cos(theta))", name)
        if kind == "ellipse":
            req(close(row["negative_energy_period"], period(mu, ee)), name)
            req(close(row["radial_action_formula"], action_formula(mu, ee, ell)), name)
            req(row["radial_action_quadrature"] == row["radial_action_formula"], name)
            if not FAST:
                req(close(row["radial_action_quadrature"], action_integral(mu, ee, ell)), name)
        else:
            req(row["negative_energy_period"] is None and row["radial_action_formula"] is None and row["radial_action_quadrature"] is None, name)
        if kind == "hyperbola":
            req(close(row["hyperbolic_scattering_angle"], scatter(mu, ee, ell)), name)
        else:
            req(row["hyperbolic_scattering_angle"] is None, name)

    radial_keys = {"row_id", "mu", "energy", "initial_radius", "initial_radial_velocity", "angular_momentum", "collision_integral", "collision_time", "finite_positive_time", "physical_flow_incomplete_at_collision"}
    radial_expected = [("bound_apocentre", Fraction(1), Fraction(-1, 2), Fraction(2), Fraction(0)), ("bound_apocentre_scaled", Fraction(2), Fraction(-1, 4), Fraction(8), Fraction(0)), ("parabolic_infall", Fraction(2), Fraction(0), Fraction(1), Fraction(-2)), ("hyperbolic_infall", Fraction(2), Fraction(5, 2), Fraction(1), Fraction(-3))]
    req(len(d["radial_collision_rows"]) == 4)
    for row, (name, mu, ee, r0, vr) in zip(d["radial_collision_rows"], radial_expected):
        exact_keys(row, radial_keys, f"radial {name}")
        req(row["row_id"] == name and F(row["mu"]) == mu and F(row["energy"]) == ee and F(row["initial_radius"]) == r0 and F(row["initial_radial_velocity"]) == vr, name)
        req(row["angular_momentum"] == "0/1" and row["collision_integral"] == "integral_0^r0 dr/sqrt(2*(E+mu/r))", name)
        req(row["finite_positive_time"] is True and row["physical_flow_incomplete_at_collision"] is True, name)
        req(close(row["collision_time"], radial_collision(mu, ee, r0)), name)

    lc_keys = {"row_id", "mu", "energy", "physical_q", "physical_p", "u", "u_prime", "u_double_prime", "constraint_residual", "angular_momentum_residual", "reconstructed_p", "equation", "time_change"}
    collision_lc_keys = {"row_id", "mu", "energy", "u", "u_prime", "u_double_prime", "constraint_residual", "configuration_point_is_collision", "regularized_tau_equation", "physical_q_map", "full_symplectomorphism_claim"}
    req(len(d["levi_civita_rows"]) == 12)
    for row in d["levi_civita_rows"][:9]:
        exact_keys(row, lc_keys, f"LC {row.get('row_id')}")
        name = row["row_id"]
        match = next((x for x in expected_orbits() if x[0] == name), None)
        req(match is not None, name)
        _, mu, q, p = match
        r, ee, ell = radius(q), energy(mu, q, p), angular(q, p)
        u = F(row["u"][0]); up = (F(row["u_prime"][0]), F(row["u_prime"][1]))
        req(F(row["mu"]) == mu and F(row["energy"]) == ee and [F(x) for x in row["physical_q"]] == list(q) and [F(x) for x in row["physical_p"]] == list(p), name)
        req(u * u == r and F(row["u"][1]) == 0, name)
        req(F(row["u_double_prime"][0]) == ee * u / 2 and F(row["u_double_prime"][1]) == 0, name)
        req(F(row["constraint_residual"]) == 2 * norm2(up) - ee * u * u - mu, name)
        req(F(row["angular_momentum_residual"]) == 2 * u * up[1] - ell, name)
        req([F(x) for x in row["reconstructed_p"]] == list(p), name)
        req(row["equation"] == "u''=(E/2)u; 2|u'|^2-E|u|^2=mu; L=2 Im(conj(u)u')" and row["time_change"] == "dt=|u|^2 d tau", name)
    for row, (name, ee) in zip(d["levi_civita_rows"][9:], (("collision_negative", Fraction(-1)), ("collision_zero", Fraction(0)), ("collision_positive", Fraction(1)))):
        exact_keys(row, collision_lc_keys, f"LC collision {name}")
        req(row["row_id"] == name and F(row["mu"]) == 2 and F(row["energy"]) == ee, name)
        req(row["u"] == ["0/1", "0/1"] and row["u_prime"] == ["1/1", "0/1"] and row["u_double_prime"] == ["0/1", "0/1"], name)
        req(row["constraint_residual"] == "0/1" and row["configuration_point_is_collision"] is True and row["full_symplectomorphism_claim"] is False, name)

    fixed_keys = {"row_id", "mu", "energy", "period", "strobe", "fixed_set_description", "fixed_set_dimension", "isolated_artin_mazur_count_defined", "reason"}
    req(len(d["fixed_set_rows"]) == 5)
    for row in d["fixed_set_rows"][:3]:
        exact_keys(row, fixed_keys, f"fixed {row.get('row_id')}")
        req(row["fixed_set_dimension"] == 3 and row["isolated_artin_mazur_count_defined"] is False, row["row_id"])
        req(row["strobe"] == "T=m*T(E), m>=1; n*tau=m*T(E) (integer strobe multiple)" and row["fixed_set_description"] == "{H=E, L != 0} (collision-free energy shell)", row["row_id"])
        req(close(row["period"], period(F(row["mu"]), F(row["energy"]))), row["row_id"])
    for row, name, ee in zip(d["fixed_set_rows"][3:], ("parabolic_boundary", "hyperbolic_boundary"), (Fraction(0), Fraction(1))):
        exact_keys(row, fixed_keys, f"fixed {name}")
        req(row["row_id"] == name and F(row["energy"]) == ee and row["period"] is None and row["fixed_set_dimension"] == 0, name)

    route = d["route_a"]
    exact_keys(route, {"tuple", "overall", "route_b_invocation_allowed", "qualification"}, "route_a")
    req(route["tuple"] == ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"])
    req(route["overall"] == "ROUTE_A_REJECTED" and route["route_b_invocation_allowed"] is False)
    attr = d["attribution"]
    exact_keys(attr, {"status", "classical_ownership", "package_contribution", "priority_claim"}, "attribution")
    req(attr["status"] == "SOURCE_ATTRIBUTED_SYNTHESIS" and attr["priority_claim"] is False)
    req(isinstance(d["nonclaims"], list) and len(d["nonclaims"]) == 5)
    summary = d["summary"]
    exact_keys(summary, {"orbit_row_count", "radial_collision_row_count", "levi_civita_row_count", "fixed_set_row_count", "exact_identity_cells", "all_parameter_theorem_status", "finite_rows_role"}, "summary")
    req(summary == {"orbit_row_count": 10, "radial_collision_row_count": 4, "levi_civita_row_count": 12, "fixed_set_row_count": 5, "exact_identity_cells": 58, "all_parameter_theorem_status": "PROVED_IN_THEOREM_PACKAGE", "finite_rows_role": "REGRESSION_ONLY"})
    return n


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    assertions = check(path)
    print(json.dumps({"status": "C216_CHECKER_PASS", "assertions": assertions, "evidence_sha256": sha256(path.read_bytes()).hexdigest()}, sort_keys=True))


if __name__ == "__main__":
    main()
