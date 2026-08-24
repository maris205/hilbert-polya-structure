#!/usr/bin/env python3
"""Independent SymPy reconstruction for the C129 phase-holonomy package."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import sys

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c129_phase_evidence.json"

u = sp.symbols("u")


def reduce5(expr):
    # ``EX`` keeps any auxiliary indeterminates (notably the Fredholm
    # variable z) in the coefficient field while reducing only in u.
    return sp.Poly(sp.expand(expr), u, domain="EX").rem(sp.Poly(u**5 - 1, u, domain="EX")).as_expr()


def qstr(value):
    value = sp.Rational(value)
    return str(value.p) if value.q == 1 else f"{value.p}/{value.q}"


def receipt(expr):
    reduced = sp.Poly(reduce5(expr), u, domain=sp.QQ)
    group = [reduced.nth(k) for k in range(5)]
    cyclo_poly = sp.Poly(reduced.as_expr(), u, domain=sp.QQ).rem(sp.Poly(u**4 + u**3 + u**2 + u + 1, u, domain=sp.QQ))
    return {
        "group_ring_Z5_e0_to_e4": [qstr(value) for value in group],
        "primitive_zeta5_basis_1_zeta_zeta2_zeta3": [qstr(cyclo_poly.nth(k)) for k in range(4)],
        "trivial_character_augmentation": qstr(reduced.as_expr().subs(u, 1)),
    }


def finite_operator(degree, A, translations, B, weights, exponents):
    x, y = sp.symbols("x y")
    basis = [(a, total - a) for total in range(degree + 1) for a in range(total + 1)]
    idx = {(component, power): component * len(basis) + k for component in range(3) for k, power in enumerate(basis)}
    M = sp.zeros(3 * len(basis))
    for source in range(3):
        xp = A[0, 0] * x + A[0, 1] * y + translations[source]
        yp = A[1, 0] * x
        for k, (a, b) in enumerate(basis):
            poly = sp.Poly(sp.expand(xp**a * yp**b), x, y)
            col = source * len(basis) + k
            for target in range(3):
                if not B[target, source]:
                    continue
                phase_weight = weights[source] * u ** exponents[source]
                for powers, coefficient in poly.terms():
                    M[idx[(target, powers)], col] += phase_weight * coefficient
    return M


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_EVIDENCE
    data = json.loads(path.read_text())
    claims = data["claims"]
    checks = 0

    def ck(condition, label):
        nonlocal checks
        if not condition:
            raise AssertionError(label)
        checks += 1

    raw = json.dumps(claims, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ck(sha256(raw).hexdigest() == data["claims_sha256"], "claim hash")
    ck(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")

    A = sp.Matrix([[sp.Rational(3, 16), sp.Rational(-1, 32)], [sp.Rational(1, 4), 0]])
    B = sp.Matrix([[1, 1, 0], [1, 0, 1], [1, 0, 0]])
    weights = [sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(1, 5)]
    translations = [-2, 0, 2]
    control_translations = [0, -2, 2]
    exponents = [3, 0, 2]
    control_exponents = [0, 3, 2]
    W = B * sp.diag(*[weights[j] * u ** exponents[j] for j in range(3)])
    Wc = B * sp.diag(*[weights[j] * u ** control_exponents[j] for j in range(3)])
    z, lam = sp.symbols("z lam")

    ck(sp.expand(A.charpoly(lam).as_expr() - (lam - sp.Rational(1, 8)) * (lam - sp.Rational(1, 16))) == 0, "A spectrum")
    ck(max(sum(abs(A[i, j]) for j in range(2)) for i in range(2)) == sp.Rational(1, 4), "contraction")
    delta = [1, -u**3 / 2, -u**3 / 6, -sp.Rational(1, 30)]
    deltac = [1, -sp.Rational(1, 2), -u**3 / 6, -sp.Rational(1, 30)]
    ck(reduce5((sp.eye(3) - z * W).det() - sum(delta[k] * z**k for k in range(4))) == 0, "delta original")
    ck(reduce5((sp.eye(3) - z * Wc).det() - sum(deltac[k] * z**k for k in range(4))) == 0, "delta control")
    tf = claims["trace_and_fredholm"]
    ck(tf["symbolic_delta_original_z0_to_z3"] == [receipt(value) for value in delta], "delta evidence")
    ck(claims["controls"]["twisted_symbolic_delta_control_z0_to_z3"] == [receipt(value) for value in deltac], "control delta evidence")

    traces = {}
    tracesc = {}
    for n in range(1, 9):
        den = (1 - sp.Rational(1, 8) ** n) * (1 - sp.Rational(1, 16) ** n)
        traces[n] = reduce5(sp.trace(W**n) / den)
        tracesc[n] = reduce5(sp.trace(Wc**n) / den)
    ck(tf["power_traces_original_n1_to_8"] == {str(n): receipt(traces[n]) for n in range(1, 9)}, "trace evidence")
    ck(claims["controls"]["power_traces_control_n1_to_8"] == {str(n): receipt(tracesc[n]) for n in range(1, 9)}, "control trace evidence")

    ds = [sp.Integer(1)]
    dsc = [sp.Integer(1)]
    for n in range(1, 9):
        ds.append(reduce5(-sum(traces[k] * ds[n - k] for k in range(1, n + 1)) / n))
        dsc.append(reduce5(-sum(tracesc[k] * dsc[n - k] for k in range(1, n + 1)) / n))
    ck(tf["fredholm_coefficients_original_z0_to_z8"] == [receipt(value) for value in ds], "coefficient evidence")
    ck(claims["controls"]["fredholm_coefficients_control_z0_to_z8"] == [receipt(value) for value in dsc], "control coefficient evidence")
    ck(reduce5(ds[1] + sp.Rational(64, 105) * u**3) == 0, "linear coefficient original")
    ck(reduce5(dsc[1] + sp.Rational(64, 105)) == 0, "linear coefficient control")
    for n in range(1, 9):
        ck(sp.expand(traces[n].subs(u, 1) - tracesc[n].subs(u, 1)) == 0, f"trivial trace n={n}")
    for n in range(9):
        ck(sp.expand(ds[n].subs(u, 1) - dsc[n].subs(u, 1)) == 0, f"trivial coefficient n={n}")

    for degree in (1, 2, 3):
        finite = finite_operator(degree, A, translations, B, weights, exponents)
        ck(finite.rows == 3 * (degree + 1) * (degree + 2) // 2, f"dimension {degree}")
        for n in range(1, 4):
            partial = sum(sp.Rational(1, 8) ** (r * n) * sp.Rational(1, 16) ** (s * n) for r in range(degree + 1) for s in range(degree + 1 - r))
            ck(reduce5(sp.trace(finite**n) - sp.trace(W**n) * partial) == 0, f"finite trace M={degree},n={n}")

    def cycle(ts):
        M = sp.eye(2)
        b = sp.zeros(2, 1)
        for symbol in (0, 1, 2):
            b = A * b + sp.Matrix([ts[symbol], 0])
            M = A * M
        p = (sp.eye(2) - M).inv() * b
        pts = []
        for symbol in (0, 1, 2):
            pts.append(p)
            p = A * p + sp.Matrix([ts[symbol], 0])
        return M, pts

    M, pts = cycle(translations)
    Mc, ptsc = cycle(control_translations)
    ck(M == Mc == A**3, "monodromy")
    ck(claims["periodic_orbits"]["example_phase_points"] == [[qstr(v) for v in p] for p in pts], "points")
    ck(claims["controls"]["control_example_phase_points"] == [[qstr(v) for v in p] for p in ptsc], "control points")
    ck(pts != ptsc, "geometry changes")
    ck(claims["verdict"]["A4"] == "A4_FORMAL_HINT", "A4")
    ck(claims["verdict"]["route_b_invocation_allowed"] is False, "route B")

    print(json.dumps({"status": "C129_SYMPY_CROSSCHECK_PASS", "symbolic_checks": checks, "finite_matrix_max_dimension": 30}, sort_keys=True))


if __name__ == "__main__":
    main()
