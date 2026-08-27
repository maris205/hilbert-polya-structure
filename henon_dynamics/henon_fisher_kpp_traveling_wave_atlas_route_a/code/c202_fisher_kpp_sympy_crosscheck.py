#!/usr/bin/env python3
"""Separate symbolic reconstruction for HCS-C202."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c202_fisher_kpp_evidence.json"
EXPECTED_PAYLOAD = "f02781c209fe741b81985cde6999aa0b1af727793461b4ee0082693226218b5e"


def canonical_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def rat(value: str | int) -> sp.Rational:
    return sp.Rational(value)


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    assert data["payload_sha256"] == canonical_hash(data) == EXPECTED_PAYLOAD
    checks = 2

    U, V, speed = sp.symbols("U V s", real=True)
    vector = sp.Matrix([V, -speed * V - U * (1 - U)])
    jacobian = vector.jacobian([U, V])
    assert sp.trace(jacobian) == -speed
    assert jacobian.subs({U: 0, V: 0}).charpoly().as_expr() == sp.Symbol("lambda")**2 + speed * sp.Symbol("lambda") + 1
    assert jacobian.subs({U: 1, V: 0}).charpoly().as_expr() == sp.Symbol("lambda")**2 + speed * sp.Symbol("lambda") - 1
    checks += 3

    energy = V**2 / 2 + U**2 / 2 - U**3 / 3
    energy_derivative = sp.diff(energy, U) * vector[0] + sp.diff(energy, V) * vector[1]
    assert sp.expand(energy_derivative) == -speed * V**2
    assert energy.subs({U: 1, V: 0}) == sp.Rational(1, 6)
    assert energy.subs({U: 0, V: 0}) == 0
    checks += 3

    q = sp.symbols("q", positive=True)
    boundary_v = -q * U
    g_prime = vector[1].subs(V, boundary_v) + q * vector[0].subs(V, boundary_v)
    reduced = sp.factor(g_prime.subs(speed, (q**2 + 1) / q))
    assert reduced == U**2
    checks += 1

    # Scaling from physical z to xi.
    D, r, c = sp.symbols("D r c", positive=True, real=True)
    Up, Upp = sp.symbols("U_p U_pp", real=True)
    kappa = sp.sqrt(r / D)
    physical = D * kappa**2 * Upp + c * kappa * Up + r * U * (1 - U)
    normalized = sp.factor(physical / r)
    assert sp.simplify(normalized - (U*(1 - U) + Up*c/(sp.sqrt(D)*sp.sqrt(r)) + Upp)) == 0
    checks += 1

    # Ablowitz--Zeppetella exact solution in y=exp(xi/sqrt(6)).
    xi = sp.symbols("xi", real=True)
    y = sp.exp(xi / sp.sqrt(6))
    profile = (1 + y) ** -2
    az_residual = sp.simplify(sp.diff(profile, xi, 2) + 5 / sp.sqrt(6) * sp.diff(profile, xi) + profile * (1 - profile))
    assert az_residual == 0
    checks += 1

    # Reflection identity at the differential-expression level.
    u0, u1, u2 = sp.symbols("u_0 u_1 u_2", real=True)
    positive_expression = u2 + speed * u1 + u0 * (1 - u0)
    reflected_expression = u2 + (-speed) * (-u1) + u0 * (1 - u0)
    assert sp.expand(positive_expression - reflected_expression) == 0
    checks += 1

    # Exact reconstruction of all rational finite rows.
    for row in data["finite_regression"]["phase_rows"]:
        s_value, u_value, v_value = rat(row["speed"]), rat(row["U"]), rat(row["V"])
        observed = vector.subs({speed: s_value, U: u_value, V: v_value})
        assert observed[0] == rat(row["U_prime"])
        assert observed[1] == rat(row["V_prime"])
        assert energy_derivative.subs({speed: s_value, U: u_value, V: v_value}) == rat(row["energy_derivative"])
        assert sp.trace(jacobian).subs(speed, s_value) == rat(row["divergence"])
        checks += 4

    for row in data["finite_regression"]["az_rows"]:
        y_value = rat(row["exponential_coordinate_y"])
        expected_profile = 1 / (1 + y_value)**2
        first_coefficient = -2*y_value/(1+y_value)**3
        second = -y_value*(1-2*y_value)/(3*(1+y_value)**4)
        speed_first = -5*y_value/(3*(1+y_value)**3)
        reaction = expected_profile*(1-expected_profile)
        assert expected_profile == rat(row["U"])
        assert first_coefficient == rat(row["U_xi_coefficient_over_sqrt6"])
        assert second == rat(row["U_xixi"])
        assert speed_first == rat(row["speed_times_U_xi"])
        assert reaction == rat(row["reaction_U_one_minus_U"])
        assert second + speed_first + reaction == rat(row["ode_residual"]) == 0
        checks += 6

    for row in data["finite_regression"]["trapping_rows"]:
        u_value = rat(row["U"])
        assert rat(row["boundary_G_prime"]) == u_value**2
        checks += 1

    # The level h<1/6 has a bounded oval component around the center: the
    # cubic has one root in each of (-infty,0), (0,1), and (1,infty).
    x, h = sp.symbols("x h", real=True)
    potential = x**2 / 2 - x**3 / 3
    assert sp.expand(sp.diff(potential, x) - x * (1 - x)) == 0
    assert potential.subs(x, 0) == 0 and potential.subs(x, 1) == sp.Rational(1, 6)
    checks += 2
    for row in data["finite_regression"]["hamiltonian_oval_rows"]:
        h_value = rat(row["energy"])
        assert 0 < h_value < sp.Rational(1, 6)
        polynomial = sp.Poly(sp.together(potential - h_value), x)
        roots = sorted([complex(root) for root in sp.nroots(polynomial, n=60)], key=lambda root: root.real)
        assert max(abs(root.imag) for root in roots) < 1e-50
        assert roots[0].real < 0 < roots[1].real < 1 < roots[2].real
        checks += 4

    for row in data["finite_regression"]["speed_rows"]:
        s_value = rat(row["dimensionless_speed"])
        discriminant = s_value**2 - 4
        assert discriminant == rat(row["tail_discriminant"])
        assert rat(row["divergence"]) == -s_value
        checks += 2

    print(json.dumps({"status": "C202_SYMPY_PASS", "checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
