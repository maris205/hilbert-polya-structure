#!/usr/bin/env python3
"""Independent SymPy verification of the C106 variational identities."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c106_variational_lattice_evidence.json"


def frac(d: dict[str, int]) -> sp.Rational:
    return sp.Rational(d["numerator"], d["denominator"])


def main() -> None:
    a, k, x, y, u, v = sp.symbols("a k x y u v")
    grad = sp.Matrix([a * x - x**2 - k * (x - y), a * y - y**2 + k * (x - y)])
    q = sp.Matrix([x, y])
    state = sp.Matrix([x, y, u, v])
    mapped = sp.Matrix([grad[0] - u, grad[1] - v, x, y])
    jac = mapped.jacobian(state)
    omega = sp.zeros(4)
    omega[:2, 2:] = sp.eye(2)
    omega[2:, :2] = -sp.eye(2)
    assert sp.simplify(jac.T * omega * jac - omega) == sp.zeros(4)
    assert sp.factor(jac.det()) == 1

    # R F R = F^{-1} as a polynomial identity.
    R = sp.Matrix([u, v, x, y])
    fr = mapped.subs({x: u, y: v, u: x, v: y}, simultaneous=True)
    rfr = sp.Matrix([fr[2], fr[3], fr[0], fr[1]])
    inv = sp.Matrix([u, v, a * u - u**2 - k * (u - v) - x, a * v - v**2 + k * (u - v) - y])
    assert all(sp.expand(rfr[i] - inv[i]) == 0 for i in range(4))
    # For lambda=q dot dp, the primitive difference is
    # F^*lambda-lambda=d(U(q)-p dot q).
    potential = a * (x**2 + y**2) / 2 - (x**3 + y**3) / 3 - k * (x - y) ** 2 / 2
    S = potential - u * x - v * y
    pullback_minus = sp.Matrix([grad[0] - u, grad[1] - v, -x, -y])
    assert all(sp.expand(sp.diff(S, variable) - pullback_minus[i]) == 0 for i, variable in enumerate((x, y, u, v)))

    subs = {a: 7, k: sp.Rational(1, 4)}
    j0 = jac.subs({**subs, x: 3, y: 3, u: 6, v: 6})
    j1 = jac.subs({**subs, x: 6, y: 6, u: 3, v: 3})
    mono = j1 * j0
    z = sp.symbols("z")
    polynomial = sp.Poly((sp.eye(4) - z * mono).det(), z)
    assert polynomial.all_coeffs() == [1, sp.Rational(47, 4), sp.Rational(141, 4), sp.Rational(47, 4), 1]
    assert mono.trace() == -sp.Rational(47, 4)
    uncoupled = (jac.subs({**subs, k: 0, x: 6, y: 6}) * jac.subs({**subs, k: 0, x: 3, y: 3}))
    unc_poly = sp.Poly((sp.eye(4) - z * uncoupled).det(), z)
    assert unc_poly.all_coeffs() == [1, 14, 51, 14, 1]
    assert mono.trace() - uncoupled.trace() == sp.Rational(9, 4)

    # Fixed/period-two equations in the exact chosen model.
    assert grad.subs({**subs, k: sp.Rational(1, 4), x: 0, y: 0}) == sp.Matrix([0, 0])
    assert grad.subs({**subs, k: sp.Rational(1, 4), x: 5, y: 5}) == sp.Matrix([10, 10])
    assert mapped.subs({**subs, x: 3, y: 3, u: 6, v: 6}) == sp.Matrix([6, 6, 3, 3])
    assert mapped.subs({**subs, x: 6, y: 6, u: 3, v: 3}) == sp.Matrix([3, 3, 6, 6])

    evidence = json.loads(EVIDENCE.read_text())
    observed = evidence["controls"]["coupled_det_I_minus_z"]
    low_first = [frac(item) for item in observed]
    assert low_first == [sp.Rational(1), sp.Rational(47, 4), sp.Rational(141, 4), sp.Rational(47, 4), sp.Rational(1)]
    print(json.dumps({"status": "C106_SYMPY_CROSSCHECK_PASS", "identities": 9, "period_two_polynomial": "1+47/4 z+141/4 z^2+47/4 z^3+z^4"}, sort_keys=True))


if __name__ == "__main__":
    main()
