#!/usr/bin/env python3
"""Exact SymPy identities for C262 transfer, trace, and iterates."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c262_hill_evidence.json"


def main() -> None:
    C1, C2, S1, S2, k1, k2, d = sp.symbols("C1 C2 S1 S2 k1 k2 d", real=True)
    checks = 0

    def ck(expr, label: str) -> None:
        nonlocal checks
        checks += 1
        out = sp.factor(sp.expand(expr))
        if out != 0:
            raise AssertionError(f"{label}: {out}")

    P1 = sp.Matrix([[C1, S1], [-k1*S1, C1]])
    P2 = sp.Matrix([[C2, S2], [-k2*S2, C2]])
    M = sp.expand(P2*P1)
    delta = 2*C1*C2-(k1+k2)*S1*S2
    rel1 = C1**2+k1*S1**2-1
    rel2 = C2**2+k2*S2**2-1
    ck(P1.det()-1-rel1, "segment one determinant")
    ck(P2.det()-1-rel2, "segment two determinant")
    ck(sp.trace(M)-delta, "closed discriminant")
    ck(sp.trace(P1*P2)-sp.trace(P2*P1), "order-invariant trace")
    det_reduced = sp.rem(sp.Poly(sp.expand(M.det()-1), C1), sp.Poly(rel1, C1)).as_expr()
    det_reduced = sp.rem(sp.Poly(det_reduced, C2), sp.Poly(rel2, C2)).as_expr()
    ck(det_reduced, "monodromy determinant modulo segment identities")

    a, b, c = sp.symbols("a b c")
    A = sp.Matrix([[a, b], [c, d]])
    tr = a+d
    det = a*d-b*c
    for i in range(2):
        for j in range(2):
            ck((A**2-tr*A+det*sp.eye(2))[i, j], "Cayley Hamilton")
    # With det=1, inductively verify the U recurrence through n=12.
    x = sp.symbols("x")
    U = [sp.Integer(1), 2*x]
    for n in range(2, 13):
        U.append(sp.expand(2*x*U[-1]-U[-2]))
    # Formal reduction A^2=(2x)A-I in coefficient pairs alpha*A+beta*I.
    alpha, beta = sp.Integer(0), sp.Integer(1)
    for n in range(1, 13):
        alpha, beta = sp.expand(2*x*alpha+beta), sp.expand(-alpha)
        ck(alpha-U[n-1], f"Chebyshev A coefficient n={n}")
        expected_beta = 0 if n == 1 else -U[n-2]
        ck(beta-expected_beta, f"Chebyshev I coefficient n={n}")

    # Entire power-series differential recurrence through order 24.
    z, k = sp.symbols("z k")
    C = sum((-k)**m*z**(2*m)/sp.factorial(2*m) for m in range(13))
    S = sum((-k)**m*z**(2*m+1)/sp.factorial(2*m+1) for m in range(12))
    ck(sp.series(sp.diff(C, z)+k*S, z, 0, 23).removeO(), "C'=-kS")
    ck(sp.series(sp.diff(S, z)-C, z, 0, 23).removeO(), "S'=C")
    ck(sp.series(C**2+k*S**2-1, z, 0, 23).removeO(), "entire determinant series")

    # Exact witnesses for all four parabolic cases and one hyperbolic face.
    witnesses = [
        (sp.eye(2), 2, "plus identity"),
        (-sp.eye(2), -2, "minus identity"),
        (sp.Matrix([[1,1],[0,1]]), 2, "plus Jordan"),
        (sp.Matrix([[-1,-1],[0,-1]]), -2, "minus Jordan"),
        (sp.Matrix([[sp.Rational(5,4),sp.Rational(3,4)],[sp.Rational(3,4),sp.Rational(5,4)]]), sp.Rational(5,2), "hyperbolic"),
    ]
    for matrix, trace, label in witnesses:
        ck(matrix.det()-1, label+" determinant")
        ck(sp.trace(matrix)-trace, label+" trace")
        for n in range(1, 13):
            Un1 = sp.chebyshevu(n-1, trace/2)
            Un2 = 0 if n == 1 else sp.chebyshevu(n-2, trace/2)
            diff = matrix**n-Un1*matrix+Un2*sp.eye(2)
            for value in diff:
                ck(value, label+" power")

    data = json.loads(EVIDENCE.read_text())
    formulas = {row["id"]: row["formula"] for row in data["exact_identities"]}
    expected = {
        "segment_identity": "C(k,t)^2+k*S(k,t)^2=1",
        "segment_matrix": "Phi(k,t)=[[C,S],[-k*S,C]]",
        "determinant": "det(Phi)=det(M)=1",
        "discriminant": "Delta=2*C1*C2-(k1+k2)*S1*S2",
        "characteristic": "M^2-Delta*M+I=0",
        "chebyshev": "M^n=U_{n-1}(Delta/2)*M-U_{n-2}(Delta/2)*I; U_{-1}=0,U_0=1",
        "parabolic_split": "Delta=+/-2 requires testing M=+/-I versus rank(M-/+I)=1",
        "order_trace": "tr(Phi2*Phi1)=tr(Phi1*Phi2)",
    }
    checks += 1
    if formulas != expected:
        raise AssertionError("evidence identities")
    checks += 1
    if data["route_a"]["tuple"] != ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]:
        raise AssertionError("route tuple")
    checks += 1
    if data["route_a"]["route_b_invocation_allowed"] is not False:
        raise AssertionError("Route B")
    print(f"C262_SYMPY_PASS ({checks} exact identities; segment determinant, trace, Cayley--Hamilton, Chebyshev and Jordan faces)")


if __name__ == "__main__":
    main()
