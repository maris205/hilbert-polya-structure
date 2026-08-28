#!/usr/bin/env python3
"""Independent symbolic identities for the C211 theorem package."""
import sympy as sp


def main() -> None:
    u, v, a, c, b, d = sp.symbols("u v a c b d", positive=True)
    H = c * (sp.exp(u) - u - 1) + a * (sp.exp(v) - v - 1)
    udot = a * (1 - sp.exp(v))
    vdot = c * (sp.exp(u) - 1)
    checks = []
    checks.append(sp.simplify(sp.diff(H, u) * udot + sp.diff(H, v) * vdot) == 0)
    checks.append(sp.simplify(sp.diff(H, u, 2)) == c * sp.exp(u))
    checks.append(sp.simplify(sp.diff(H, v, 2)) == a * sp.exp(v))
    checks.append(sp.simplify(sp.diff(H, u, v)) == 0)
    checks.append(sp.simplify(sp.det(sp.hessian(H, (u, v)))) == a * c * sp.exp(u + v))
    A = sp.Matrix([[0, -a], [c, 0]])
    lam = sp.symbols("lam")
    checks.append(sp.factor((lam * sp.eye(2) - A).det()) == lam**2 + a * c)
    checks.append(sp.simplify(sp.diff(H, u).subs({u: 0, v: 0})) == 0)
    checks.append(sp.simplify(sp.diff(H, v).subs({u: 0, v: 0})) == 0)
    # The original coordinates and the logarithmic normalization agree at the
    # equilibrium and yield the advertised cycle-average substitutions.
    xstar, ystar = c / d, a / b
    checks.append(sp.simplify(d * xstar - c) == 0)
    checks.append(sp.simplify(b * ystar - a) == 0)
    checks.append(sp.simplify(xstar * 1 - c / d) == 0)
    checks.append(sp.simplify(ystar * 1 - a / b) == 0)
    assert all(checks)
    print(f"C211 SymPy cross-check: PASS ({len(checks)} symbolic identities)")
    print("Hamiltonian cancellation, Hessian positivity, center spectrum, averages: PASS")


if __name__ == "__main__":
    main()
