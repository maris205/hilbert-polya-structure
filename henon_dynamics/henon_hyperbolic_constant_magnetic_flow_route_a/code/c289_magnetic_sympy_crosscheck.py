#!/usr/bin/env python3
"""Independent symbolic reconstruction of the C289 Lorentz-frame identities."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "results/c289_magnetic_evidence.json"


def main() -> None:
    data = json.loads(DATA.read_text())
    k, v, b = s.symbols("k v b", positive=True, real=True)
    lam = s.symbols("lambda")
    A = s.Matrix([[0, k*v, 0], [k*v, 0, -b], [0, b, 0]])
    eta = s.diag(-1, 1, 1)
    delta = b**2-k**2*v**2
    checks = [
        A.T*eta + eta*A == s.zeros(3),
        s.simplify(A**3 + delta*A) == s.zeros(3),
        s.expand(A.charpoly(lam).as_expr()-lam*(lam**2+delta)) == 0,
        A.det() == 0,
        A.trace() == 0,
        # coth(k rho)=b/(kv) implies sinh^2(k rho)=(kv)^2/delta;
        # squaring circumference/speed gives the advertised period.
        s.simplify((2*s.pi/k/v)**2*(k*v)**2/delta-(2*s.pi/s.sqrt(delta))**2) == 0,
    ]
    e0 = s.Matrix([1, 0, 0])
    checks.extend([
        (A*e0)[1] == k*v,
        (A**2*e0)[0] == k**2*v**2,
        (A**2*e0)[1] == 0,
    ])
    t = s.symbols("t", real=True)
    for critical_sign in (-1, 1):
        Ac = A.subs(b, critical_sign*k*v)
        critical = s.simplify(Ac**2)
        critical_base = s.simplify(e0+t*Ac*e0+t**2*Ac**2*e0/2)
        checks.extend([
            critical != s.zeros(3),
            s.simplify(Ac**3) == s.zeros(3),
            s.simplify(critical_base[1]-k*v*t) == 0,
        ])
    for row in data["orbit_cells"]:
        kk, vv, bb = map(s.Rational, (row["kappa"], row["speed"], row["field"]))
        dd = bb**2-kk**2*vv**2
        checks.append(s.Rational(row["discriminant"]) == dd)
        checks.append(s.Rational(row["geodesic_curvature"]) == bb/vv)
        if row["period_over_2pi_squared"] is not None:
            checks.append(s.Rational(row["period_over_2pi_squared"])*dd == 1)
    assert all(checks)
    print(f"C289_SYMPY_PASS ({len(checks)} symbolic checks; raw 3x3 and basepoint-return reconstruction)")


if __name__ == "__main__":
    main()
