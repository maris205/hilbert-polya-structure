#!/usr/bin/env python3
"""Independent symbolic checks for the constant-wind Zermelo atlas."""
from __future__ import annotations

import sympy as sp


def main() -> None:
    a, c, p, r2, t, w2, D = sp.symbols("a c p r2 t w2 D", real=True)
    checks = 0

    def zero(expr, label):
        nonlocal checks
        if sp.simplify(expr) != 0:
            raise AssertionError(label)
        checks += 1

    quadratic = a * t**2 - 2 * p * t + r2
    zero(quadratic - ((w2 - c**2) * t**2 - 2 * p * t + r2).subs(w2, a + c**2), "reachability quadratic")
    root_minus = (p - sp.sqrt(D)) / a
    root_plus = (p + sp.sqrt(D)) / a
    zero(quadratic.subs(t, root_minus).subs(r2, (p**2 - D) / a), "smaller root")
    zero(quadratic.subs(t, root_plus).subs(r2, (p**2 - D) / a), "larger root")
    zero(root_minus + root_plus - 2 * p / a, "root sum")
    zero(root_minus * root_plus - (p**2 - D) / a**2, "root product")

    b = sp.symbols("b", positive=True)
    weak = (sp.sqrt(p**2 + b * r2) - p) / b
    zero((-b * weak**2 - 2 * p * weak + r2), "weak root")
    critical = r2 / (2 * p)
    zero((-2 * p * critical + r2), "critical root")

    # Implicit-gradient HJB identity: q=y-WT, |q|=cT and denominator W.q+c^2T.
    Wq, qnorm = sp.symbols("Wq qnorm", real=True)
    denominator = Wq + c**2 * t
    zero(((Wq + c * qnorm) / denominator - 1).subs(qnorm, c * t), "HJB after qnorm=cT")

    lam, speed_scale = sp.symbols("lam speed_scale", positive=True)
    weak_scaled = (sp.sqrt((lam * p)**2 + b * lam**2 * r2) - lam * p) / b
    zero(weak_scaled - lam * weak, "target homogeneity weak")
    zero(
        (sp.sqrt((speed_scale * p)**2 + speed_scale**2 * b * r2) - speed_scale * p)
        / (speed_scale**2 * b) - weak / speed_scale,
        "velocity scaling weak",
    )
    zero((lam**2 * r2) / (2 * lam * p) - lam * critical, "target homogeneity critical")
    zero((r2 / (2 * speed_scale * p)) - critical / speed_scale, "velocity scaling critical")

    # Exact regression identities across all sign chambers and boundary roots.
    samples = [
        (-4, 0, 9), (-9, 0, 25), (-3, 3, 9), (-3, -3, 9),
        (-3, 0, 4), (-11, 11, 5), (0, 3, 9), (0, 1, 2),
        (3, 6, 9), (16, 20, 16), (16, 20, 25), (9, 15, 25),
    ]
    for av, pv, rv in samples:
        disc = pv * pv - av * rv
        if av < 0:
            value = (sp.sqrt(disc) - pv) / (-av)
        elif av == 0:
            value = sp.Rational(rv, 2 * pv)
        else:
            value = (pv - sp.sqrt(disc)) / av
        zero((av * t**2 - 2 * pv * t + rv).subs(t, value), "sample first-contact root")

    # Cone-boundary and zero-control identities.
    zero(20**2 - (5**2 - 3**2) * (4**2 + 3**2), "two-dimensional Mach boundary")
    zero(15**2 - (5**2 - 4**2) * (4**2 + 3**2), "three-dimensional Mach boundary")
    zero((2**2) * 2**2 - 2 * (2 * 4) * 2 + 4**2, "zero-control ray")

    print(f"C305 SymPy cross-check: PASS ({checks} symbolic identities)")


if __name__ == "__main__":
    main()
