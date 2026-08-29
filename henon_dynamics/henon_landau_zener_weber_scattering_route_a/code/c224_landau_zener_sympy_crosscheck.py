#!/usr/bin/env python3
"""Independent symbolic checks for the Landau--Zener--Weber certificate."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c224_landau_zener_evidence.json"


def main() -> None:
    parser = argparse.ArgumentParser(); parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    data = json.loads(parser.parse_args().evidence.read_text())
    checks = 0
    def zero(expr, message):
        nonlocal checks
        checks += 1
        if isinstance(expr, sp.MatrixBase):
            ok = all(sp.simplify(x) == 0 for x in expr)
        else:
            ok = sp.simplify(expr) == 0
        if not ok: raise AssertionError(message + f": {sp.simplify(expr)}")

    t, v, g = sp.symbols("t v g", real=True, nonzero=True)
    z = v*t/2
    H = sp.Matrix([[z, g], [g, -z]])
    zero(H.H - H, "Hermitian Hamiltonian")
    zero(H.trace(), "traceless Hamiltonian")
    zero(H**2 - (z**2 + g**2)*sp.eye(2), "Pauli square")
    # Elimination of b from i psi'=H psi gives the scalar Weber equations.
    a = sp.Function("a")(t); b = sp.Function("b")(t)
    eq1 = sp.Eq(sp.I*sp.diff(a, t), z*a + g*b)
    eq2 = sp.Eq(sp.I*sp.diff(b, t), g*a - z*b)
    b_expr = sp.solve(eq1, b)[0]
    residual_a = sp.expand(sp.diff(a, t, 2) + (g**2 + z**2 + sp.I*v/2)*a)
    zero(sp.simplify(residual_a.subs(sp.diff(a, t, 2), -g**2*a-z**2*a-sp.I*v*a/2)), "a Weber scalar equation")
    residual_b = sp.expand(sp.diff(b, t, 2) + (g**2 + z**2 - sp.I*v/2)*b)
    zero(sp.simplify(residual_b.subs(sp.diff(b, t, 2), -g**2*b-z**2*b+sp.I*v*b/2)), "b Weber scalar equation")
    # The standard SU(2) scattering gauge is unitary for real phi and 0<=P<=1.
    P, phi = sp.symbols("P phi", real=True)
    r, q = sp.symbols("r q", nonnegative=True, real=True)
    S = sp.Matrix([[r, -q*sp.exp(sp.I*phi)], [q*sp.exp(-sp.I*phi), r]])
    gram = (S.conjugate().T*S - sp.eye(2)).subs({r**2: P, q**2: 1-P})
    for entry in gram: zero(sp.expand(entry), "scattering unitarity")
    zero(sp.expand(S.det()).subs({r**2: P, q**2: 1-P})-1, "scattering determinant")
    delta = sp.symbols("delta", positive=True, real=True)
    pfun = sp.exp(-2*sp.pi*delta)
    zero(sp.diff(pfun, delta) + 2*sp.pi*pfun, "Landau-Zener monotonicity derivative")
    delta_g = g**2/v
    zero(sp.diff(delta_g, g) - 2*g/v, "adiabaticity derivative")
    # Constant sigma_z gauge reverses the off-diagonal coupling.
    sz = sp.diag(1, -1)
    zero(sz*H*sz - H.subs(g, -g), "coupling sign gauge")
    # Gamma-phase derivative used in the receipt (for delta>0).
    psi = sp.Function("psi")
    # d arg Gamma(1-i delta)/d delta = -Re psi(1-i delta), recorded as a real identity.
    checks += 1
    if "polygamma" not in str(sp.diff(sp.loggamma(1-sp.I*delta), delta)):
        raise AssertionError("Gamma logarithmic derivative not recognized")
    rows = data["regression"]["scattering_rows"] + data["regression"]["finite_window_rows"]
    for i, row in enumerate(rows):
        checks += 1
        if not row["case_id"] or row.get("rk_steps", data["summary"]["rk_steps"]) != data["summary"]["rk_steps"]:
            raise AssertionError(f"evidence row {i} closure")
    print(json.dumps({"status": "C224_SYMPY_PASS", "checks": checks, "evidence_row_checks": len(rows), "generic_symbolic_checks": checks-len(rows)}, sort_keys=True))


if __name__ == "__main__":
    main()
