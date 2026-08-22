#!/usr/bin/env python3
"""Independent SymPy cross-check for the C111 identities and mode polynomial."""
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c111_three_site_evidence.json"


def frac(d: dict[str, int]) -> sp.Rational:
    return sp.Rational(d["numerator"], d["denominator"])


def main() -> None:
    a, k, z = sp.symbols("a k z")
    q = sp.Matrix(sp.symbols("q1:4"))
    p = sp.Matrix(sp.symbols("p1:4"))
    L = sp.Matrix([[2, -1, -1], [-1, 2, -1], [-1, -1, 2]])
    g = a * q - sp.Matrix([q[i] ** 2 for i in range(3)]) - k * L * q
    state = q.col_join(p)
    mapped = (g - p).col_join(q)
    jac = mapped.jacobian(state)
    omega = sp.zeros(6)
    omega[:3, 3:] = sp.eye(3)
    omega[3:, :3] = -sp.eye(3)
    assert sp.simplify(jac.T * omega * jac - omega) == sp.zeros(6)
    assert sp.factor(jac.det()) == 1

    # Reversor and exact primitive identities.
    swapped = p.col_join(q)
    fr = mapped.subs(dict(zip(list(q) + list(p), list(p) + list(q))), simultaneous=True)
    rfr = fr[3:, :].col_join(fr[:3, :]) if False else sp.Matrix(list(fr[3:]) + list(fr[:3]))
    inv = p.col_join(g.subs(dict(zip(q, p)), simultaneous=True) - q)
    assert all(sp.expand(rfr[i] - inv[i]) == 0 for i in range(6))
    U = sum(a * qi ** 2 / 2 - qi ** 3 / 3 for qi in q) - k * ((q[0] - q[1]) ** 2 + (q[1] - q[2]) ** 2 + (q[2] - q[0]) ** 2) / 2
    S = U - (p.dot(q))
    pullback_minus = (g - p).col_join(-q)
    assert all(sp.expand(sp.diff(S, var) - pullback_minus[i]) == 0 for i, var in enumerate(list(q) + list(p)))

    subs = {a: 7, k: sp.Rational(1, 5)}
    q3 = sp.Matrix([3, 3, 3]); q6 = sp.Matrix([6, 6, 6])
    j3 = jac.subs({**subs, **dict(zip(q, q3)), **dict(zip(p, q6))})
    j6 = jac.subs({**subs, **dict(zip(q, q6)), **dict(zip(p, q3))})
    mono = j6 * j3
    poly = sp.Poly((sp.eye(6) - z * mono).det(), z)
    assert poly.all_coeffs() == [1, sp.Rational(387, 25), sp.Rational(50211, 625), sp.Rational(98002, 625), sp.Rational(50211, 625), sp.Rational(387, 25), 1]
    assert sp.trace(mono) == -sp.Rational(387, 25)
    # Fourier-mode factors: lambda(L) = 0,3,3.
    mode_traces = [((7 - 12) - sp.Rational(1, 5) * lam) * ((7 - 6) - sp.Rational(1, 5) * lam) - 2 for lam in (0, 3, 3)]
    assert mode_traces == [-7, -sp.Rational(106, 25), -sp.Rational(106, 25)]
    reconstructed = sp.prod(1 - t * z + z ** 2 for t in mode_traces)
    assert sp.expand(reconstructed) == poly.as_expr()

    unc_j3 = jac.subs({**subs, k: 0, **dict(zip(q, q3)), **dict(zip(p, q6))})
    unc_j6 = jac.subs({**subs, k: 0, **dict(zip(q, q6)), **dict(zip(p, q3))})
    unc = unc_j6 * unc_j3
    unc_poly = sp.Poly((sp.eye(6) - z * unc).det(), z)
    assert unc_poly.all_coeffs() == [1, 21, 150, 385, 150, 21, 1]
    assert sp.trace(mono) - sp.trace(unc) == sp.Rational(138, 25)

    # Exact orbit equations.
    assert mapped.subs({**subs, **dict(zip(q, q3)), **dict(zip(p, q6))}) == q6.col_join(q3)
    assert mapped.subs({**subs, **dict(zip(q, q6)), **dict(zip(p, q3))}) == q3.col_join(q6)
    assert g.subs({**subs, **dict(zip(q, sp.zeros(3, 1)))}) == sp.zeros(3, 1)
    assert g.subs({**subs, **dict(zip(q, sp.Matrix([5, 5, 5])))}) == sp.Matrix([10, 10, 10])

    observed = json.loads(EVIDENCE.read_text())["fourier_mode_witness"]["reconstructed_full_det_I_minus_z"]
    assert [frac(v) for v in observed] == [sp.Rational(1), sp.Rational(387, 25), sp.Rational(50211, 625), sp.Rational(98002, 625), sp.Rational(50211, 625), sp.Rational(387, 25), sp.Rational(1)]
    print(json.dumps({"status": "C111_SYMPY_CROSSCHECK_PASS", "identities": 11, "full_period_two_polynomial": "1+387/25 z+50211/625 z^2+98002/625 z^3+..."}, sort_keys=True))


if __name__ == "__main__":
    main()
