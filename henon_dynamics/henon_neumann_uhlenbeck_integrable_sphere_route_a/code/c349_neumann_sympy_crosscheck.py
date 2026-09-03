#!/usr/bin/env python3
"""Independent symbolic identities for the Neumann--Uhlenbeck theorem."""
from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c349_neumann_evidence.json"
CHECKS = 0


def need(condition: bool, label: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)


def qr(value: str) -> sp.Rational:
    item = Fraction(value)
    return sp.Rational(item.numerator, item.denominator)


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C349 SymPy lane refuses optimized Python")

    x = sp.symbols("x0:3", real=True)
    p = sp.symbols("p0:3", real=True)
    a = sp.symbols("a0:3", real=True)
    lam = sp.symbols("lambda", real=True)
    normx = sum(z*z for z in x)
    tangent = sum(x[i]*p[i] for i in range(3))
    normp = sum(z*z for z in p)
    potential = sum(a[i]*x[i]**2 for i in range(3))
    alpha = potential-normp
    xdot = p
    pdot = tuple((alpha-a[i])*x[i] for i in range(3))

    def dt(expression):
        return sp.expand(sum(sp.diff(expression, x[i])*xdot[i]
                             + sp.diff(expression, p[i])*pdot[i]
                             for i in range(3)))

    def lij(i, j):
        return x[i]*p[j]-x[j]*p[i]

    fs = []
    for i in range(3):
        fs.append(x[i]**2+sum(lij(i, j)**2/(a[i]-a[j])
                              for j in range(3) if j != i))

    need(sp.expand(dt(normx)-2*tangent) == 0, "sphere derivative")
    need(sp.expand(dt(tangent)-(1-normx)*(normp-potential)) == 0,
         "tangent derivative modulo sphere")
    hamiltonian = (normp+potential)/2
    need(sp.expand(dt(hamiltonian)-alpha*tangent) == 0,
         "Hamiltonian conservation modulo tangency")
    for i in range(3):
        for j in range(i+1, 3):
            need(sp.expand(dt(lij(i, j))-(a[i]-a[j])*x[i]*x[j]) == 0,
                 f"angular derivative {i}{j}")
    for i, value in enumerate(fs):
        # The derivative is proportional to the two constraints.  Reducing by
        # x.p=0 and |x|^2=1 gives zero without numerical substitution.
        reduced = sp.expand(dt(value).subs(p[2], -(x[0]*p[0]+x[1]*p[1])/x[2]))
        reduced = sp.factor(reduced.subs(x[2]**2, 1-x[0]**2-x[1]**2))
        need(reduced == 0, f"Uhlenbeck conservation {i}")
    need(sp.cancel(sum(fs)-normx) == 0, "sum F")
    weighted = sp.cancel(sum(a[i]*fs[i] for i in range(3)))
    gram = normx*normp-tangent**2
    need(sp.cancel(weighted-(potential+gram)) == 0, "weighted F Gram identity")

    def dirac(f, g):
        fx = [sp.diff(f, z) for z in x]
        fp = [sp.diff(f, z) for z in p]
        gx = [sp.diff(g, z) for z in x]
        gp = [sp.diff(g, z) for z in p]
        dot = lambda left, right: sum(left[k]*right[k] for k in range(3))
        return sp.cancel(dot(fx, gp)-dot(fp, gx)
                         -dot(fx, x)*dot(x, gp)+dot(fp, x)*dot(x, gx)
                         +dot(fp, p)*dot(gp, x)-dot(fp, x)*dot(gp, p))

    for i in range(3):
        for j in range(i+1, 3):
            bracket = dirac(fs[i], fs[j])
            reduced = bracket.subs(p[2], -(x[0]*p[0]+x[1]*p[1])/x[2])
            reduced = sp.cancel(reduced.subs(x[2]**2, 1-x[0]**2-x[1]**2))
            need(reduced == 0, f"Dirac involution {i}{j}")

    inv = [1/(lam-a[i]) for i in range(3)]
    U = sum(x[i]**2*inv[i] for i in range(3))
    V = sum(x[i]*p[i]*inv[i] for i in range(3))
    W = 1+sum(p[i]**2*inv[i] for i in range(3))
    need(sp.cancel(dt(U)-2*V) == 0, "Lax U equation")
    need(sp.cancel(dt(V)-(W+(alpha-lam)*U)-(normx-1)) == 0,
         "Lax V equation modulo sphere")
    need(sp.cancel(dt(W)-2*(alpha-lam)*V-2*tangent) == 0,
         "Lax W equation modulo tangency")
    L = sp.Matrix([[V, U], [-W, -V]])
    M = sp.Matrix([[0, 1], [alpha-lam, 0]])
    Ldot = L.applyfunc(dt)
    for item in (Ldot-(L*M-M*L)):
        reduced = sp.cancel(item.subs(p[2], -(x[0]*p[0]+x[1]*p[1])/x[2]))
        reduced = sp.cancel(reduced.subs(x[2]**2, 1-x[0]**2-x[1]**2))
        need(reduced == 0, "matrix Lax entry modulo constraints")
    determinant_gap = U*W-V**2-sum(fs[i]*inv[i] for i in range(3))
    determinant_gap = sp.cancel(determinant_gap.subs(
        p[2], -(x[0]*p[0]+x[1]*p[1])/x[2]))
    determinant_gap = sp.cancel(determinant_gap.subs(
        x[2]**2, 1-x[0]**2-x[1]**2))
    need(determinant_gap == 0,
         "resolvent residue identity")

    # Linearization and all declared algebraic boundary faces.
    for axis in range(3):
        for j in range(3):
            if j != axis:
                need(sp.expand(-(a[j]-a[axis])) == a[axis]-a[j],
                     f"axis frequency square {axis}{j}")
    for missing in range(3):
        need(xdot[missing].subs({x[missing]: 0, p[missing]: 0}) == 0,
             f"coordinate x invariance {missing}")
        need(pdot[missing].subs({x[missing]: 0, p[missing]: 0}) == 0,
             f"coordinate p invariance {missing}")
    for i, j in ((0, 1), (0, 2), (1, 2)):
        need(sp.expand(dt(lij(i, j)).subs(a[j], a[i])) == 0,
             f"repeated-spectrum Noether momentum {i}{j}")
        simple = next(k for k in range(3) if k not in (i, j))
        repeated_bracket = sp.cancel(dirac(lij(i, j), fs[simple]).subs(a[j], a[i]))
        repeated_bracket = repeated_bracket.subs(
            p[2], -(x[0]*p[0]+x[1]*p[1])/x[2])
        repeated_bracket = sp.cancel(repeated_bracket.subs(
            x[2]**2, 1-x[0]**2-x[1]**2))
        need(repeated_bracket == 0,
             f"repeated-spectrum commuting pair {i}{j}")
        energy_gap = sp.cancel(
            2*hamiltonian-a[i]-lij(i, j)**2
            -(a[simple]-a[i])*fs[simple]).subs(a[j], a[i])
        constraint_form = (normx-1)*(a[i]-normp)+tangent**2
        need(sp.cancel(energy_gap-constraint_form) == 0,
             f"repeated-spectrum energy identity {i}{j}")

    witness_t = sp.symbols("witness_t", positive=True)
    witness = {
        x[0]: sp.Rational(3, 5), x[1]: 0, x[2]: sp.Rational(4, 5),
        p[0]: 0, p[1]: witness_t, p[2]: 0, a[1]: a[0],
    }
    directions = [
        ((-sp.Rational(4, 5), 0, sp.Rational(3, 5)), (0, 0, 0)),
        ((0, 0, 0), (0, 1, 0)),
    ]

    def directional(expression, direction):
        direction_x, direction_p = direction
        return sp.expand(sum(sp.diff(expression, x[k])*direction_x[k]
                             + sp.diff(expression, p[k])*direction_p[k]
                             for k in range(3))).subs(witness)

    witness_matrix = sp.Matrix([
        [directional(lij(0, 1), direction) for direction in directions],
        [directional(fs[2], direction) for direction in directions],
    ])
    witness_formula = -8*(9*(a[2]-a[0])+25*witness_t**2)/(125*(a[2]-a[0]))
    need(sp.cancel(witness_matrix.det()-witness_formula) == 0,
         "repeated-spectrum independence witness")
    speed2 = normp
    isotropic_pdot = [sp.expand(pdot[i].subs({a[0]: 0, a[1]: 0, a[2]: 0}))
                      for i in range(3)]
    for i in range(3):
        need(sp.expand(isotropic_pdot[i]+speed2*x[i]) == 0,
             f"isotropic oscillator {i}")

    # Evidence-facing exact symbolic receipts are independently parsed here.
    data = json.loads(EVIDENCE.read_text())
    for row in data["state_rows"]:
        av = [qr(z) for z in row["a"]]
        xv = [qr(z) for z in row["x"]]
        pv = [qr(z) for z in row["p"]]
        need(sum(z*z for z in xv) == 1, "evidence sphere")
        need(sum(xv[i]*pv[i] for i in range(3)) == 0, "evidence tangent")
        fvals = [qr(z) for z in row["F"]]
        need(sum(fvals) == 1, "evidence sum F")
        need(sum(av[i]*fvals[i] for i in range(3)) == 2*qr(row["energy"]),
             "evidence weighted F")
        for probe in row["lax_probes"]:
            need(qr(probe["determinant"]) == qr(probe["residue_sum"]),
                 "evidence determinant")
            need(qr(probe["direct_U_dot"]) == qr(probe["lax_U_dot"]),
                 "evidence U dot")
            need(qr(probe["direct_V_dot"]) == qr(probe["lax_V_dot"]),
                 "evidence V dot")
            need(qr(probe["direct_W_dot"]) == qr(probe["lax_W_dot"]),
                 "evidence W dot")

    print(f"C349 SymPy cross-check: PASS {CHECKS} exact identities")


if __name__ == "__main__":
    main()
