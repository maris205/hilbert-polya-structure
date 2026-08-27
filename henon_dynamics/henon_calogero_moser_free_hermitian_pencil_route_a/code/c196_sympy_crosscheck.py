#!/usr/bin/env python3
"""Separate exact SymPy reconstruction for HCS-C196."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c196_calogero_moser_evidence.json"
EXPECTED_PAYLOAD = "6269e5194aa8c5b69bb2d8786efc2ca70935261b10e8e78def7c006ae53e2545"


def canonical_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def rat(text: str) -> sp.Rational:
    return sp.Rational(text)


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    assert data["payload_sha256"] == canonical_hash(data) == EXPECTED_PAYLOAD
    checks = 2
    spectral_variable = sp.symbols("zeta", real=True)

    for row in data["finite_regression"]["rows"]:
        size = row["N"]
        q = [rat(value) for value in row["q"]]
        p = [rat(value) for value in row["p"]]
        coupling = rat(row["g"])
        Q = sp.diag(*q)
        L = sp.Matrix(size, size, lambda j, k:
            p[j] if j == k else sp.I * coupling / (q[j] - q[k]))

        for j in range(size):
            for k in range(size):
                assert sp.simplify(L[j, k] - sp.conjugate(L[k, j])) == 0
                checks += 1
                expected = sp.I * coupling if j != k else 0
                assert sp.simplify((Q * L - L * Q)[j, k] - expected) == 0
                checks += 1

        energy = sp.Rational(1, 2) * sum(value**2 for value in p)
        energy += sum(
            coupling**2 / (q[j] - q[k])**2
            for j in range(size) for k in range(j + 1, size)
        )
        assert energy == rat(row["hamiltonian"])
        checks += 1
        assert sp.trace(L**2) == 2 * energy == rat(row["trace_L2_equals_2H"])
        checks += 1
        for exponent, expected in enumerate(row["trace_invariants"], start=1):
            assert sp.simplify(sp.trace(L**exponent) - rat(expected)) == 0
            checks += 1

        polynomial = L.charpoly(spectral_variable).as_poly()
        assert polynomial.degree() == size
        checks += 1
        assert polynomial.LC() == 1
        checks += 1
        for coefficient in polynomial.all_coeffs():
            assert sp.im(sp.expand_complex(coefficient)) == 0
            checks += 1

        # Exact Newton coefficient at the initial diagonalization Q(0)=Q_0.
        for j in range(size):
            perturbation = sum(
                2 * (L[k, j] * sp.conjugate(L[k, j])) / (q[j] - q[k])
                for k in range(size) if k != j
            )
            force = sum(
                2 * coupling**2 / (q[j] - q[k])**3
                for k in range(size) if k != j
            )
            assert sp.simplify(perturbation - force) == 0
            checks += 1

    # A symbolic three-particle convention sentinel.  It checks the signs and
    # factor without specializing the initial data.
    q1, q2, q3 = sp.symbols("q_1 q_2 q_3", real=True, distinct=True)
    p1, p2, p3 = sp.symbols("p_1 p_2 p_3", real=True)
    g = sp.symbols("g", positive=True, real=True)
    symbolic_q = [q1, q2, q3]
    symbolic_p = [p1, p2, p3]
    Q3 = sp.diag(*symbolic_q)
    L3 = sp.Matrix(3, 3, lambda j, k:
        symbolic_p[j] if j == k else sp.I * g / (symbolic_q[j] - symbolic_q[k]))
    J3 = sp.ones(3)
    assert sp.simplify(Q3 * L3 - L3 * Q3 - sp.I * g * (J3 - sp.eye(3))) == sp.zeros(3)
    checks += 9
    H3 = sp.Rational(1, 2) * sum(value**2 for value in symbolic_p)
    H3 += sum(g**2 / (symbolic_q[j] - symbolic_q[k])**2 for j in range(3) for k in range(j + 1, 3))
    assert sp.simplify(sp.trace(L3**2) - 2 * H3) == 0
    checks += 1
    for j in range(3):
        left = sum(
            2 * L3[k, j] * sp.conjugate(L3[k, j]) / (symbolic_q[j] - symbolic_q[k])
            for k in range(3) if k != j
        )
        right = sum(2 * g**2 / (symbolic_q[j] - symbolic_q[k])**3 for k in range(3) if k != j)
        assert sp.simplify(left - right) == 0
        checks += 1

    # Independent symbolic check of the inverse spectral-atlas sign.
    lam1, lam2, lam3 = sp.symbols("lambda_1 lambda_2 lambda_3", real=True)
    a1, a2, a3 = sp.symbols("a_1 a_2 a_3", real=True)
    lambdas = [lam1, lam2, lam3]
    intercepts = [a1, a2, a3]
    Lambda = sp.diag(*lambdas)
    Qtilde = sp.Matrix(3, 3, lambda a, b:
        intercepts[a] if a == b else sp.I * g / (lambdas[b] - lambdas[a]))
    for a in range(3):
        for b in range(3):
            assert sp.simplify(Qtilde[a, b] - sp.conjugate(Qtilde[b, a])) == 0
            checks += 1
    assert sp.simplify(Qtilde * Lambda - Lambda * Qtilde - sp.I * g * (J3 - sp.eye(3))) == sp.zeros(3)
    checks += 9

    print(json.dumps({"status": "C196_SYMPY_PASS", "checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
