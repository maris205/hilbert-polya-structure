#!/usr/bin/env python3
"""Independent symbolic block checks for HCS-C333."""
from __future__ import annotations

import itertools
import sys

import sympy as sp


CHECKS = 0


def need(condition: bool, label: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)


def pair_matrix(n, eta, i, j):
    d = sp.zeros(n, 1)
    d[i], d[j] = 1, -1
    return sp.eye(n) - eta * d * d.T


def transfer(a, eta):
    n = a.rows
    edges = list(itertools.combinations(range(n), 2))
    return sp.simplify(sum((pair_matrix(n, eta, i, j) * a * pair_matrix(n, eta, i, j)
                           for i, j in edges), sp.zeros(n)) / len(edges))


def centered_zero_diagonal_basis(n):
    pairs = list(itertools.combinations(range(n), 2))
    constraints = sp.zeros(n, len(pairs))
    for column, (i, j) in enumerate(pairs):
        constraints[i, column] = 1
        constraints[j, column] = 1
    basis = []
    for vector in constraints.nullspace():
        matrix = sp.zeros(n)
        for coefficient, (i, j) in zip(vector, pairs):
            matrix[i, j] = coefficient
            matrix[j, i] = coefficient
        basis.append(matrix)
    return basis


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C333 SymPy lane refuses optimized Python")

    eta, n = sp.symbols("eta n", real=True)
    d = sp.Matrix([1, -1])
    w = sp.eye(2) - eta * d * d.T
    need(sp.simplify(w.T - w) == sp.zeros(2), "pair symmetry")
    need(sp.simplify(w * sp.ones(2, 1) - sp.ones(2, 1)) == sp.zeros(2, 1), "pair mean")
    need(sp.factor(w.det() - (1 - 2 * eta)) == 0, "pair determinant")
    need(sp.simplify(w**2 - (sp.eye(2) - 2 * eta * (1 - eta) * d * d.T)) == sp.zeros(2), "energy identity")

    lam0 = 1 - 4 * eta * (1 - eta) / (n - 1)
    lam1 = 1 - (4 * eta - 2 * eta**2) / (n - 1)
    lam2 = 1 - 4 * eta / (n - 1) + 4 * eta**2 / (n * (n - 1))
    need(sp.factor(lam0.subs(eta, 0) - 1) == 0, "eta zero energy")
    need(sp.factor(lam0.subs(eta, 1) - 1) == 0, "eta one energy")
    need(sp.factor(lam0.subs(eta, sp.Rational(1, 2)) - (n - 2)/(n - 1)) == 0, "half averaging")
    need(sp.factor(lam0 - (1 - 4 * eta * (1 - eta)/(n - 1))) == 0, "lambda zero algebra")
    need(sp.factor(lam1 - (1 - 4*eta/(n-1) + 2*eta**2/(n-1))) == 0, "lambda one algebra")
    need(sp.factor(lam2 - (1 - 4*eta/(n-1) + 4*eta**2/(n*(n-1)))) == 0, "lambda two algebra")

    eta_values = (sp.Rational(0), sp.Rational(1, 3), sp.Rational(1, 2), sp.Rational(1))
    for size in range(2, 8):
        p = sp.eye(size) - sp.ones(size)/size
        edges = list(itertools.combinations(range(size), 2))
        laplacian = sp.zeros(size)
        average_w = sp.zeros(size)
        for i, j in edges:
            difference = sp.zeros(size, 1)
            difference[i], difference[j] = 1, -1
            laplacian += difference * difference.T
        need(laplacian == size * p, "complete graph Laplacian")
        for value in eta_values:
            for i, j in edges:
                average_w += pair_matrix(size, value, i, j)
            average_w /= len(edges)
            expected_mean = sp.eye(size) - 2 * value * p / (size - 1)
            need(sp.simplify(average_w - expected_mean) == sp.zeros(size), "first moment matrix")
            average_w = sp.zeros(size)

            value_lam0 = sp.simplify(lam0.subs({n: size, eta: value}))
            need(sp.simplify(transfer(p, value) - value_lam0*p) == sp.zeros(size), "scalar block")

            if size >= 3:
                value_lam1 = sp.simplify(lam1.subs({n: size, eta: value}))
                standard = []
                for k in range(size - 1):
                    u = sp.zeros(size, 1)
                    u[k], u[size - 1] = 1, -1
                    block = p * sp.diag(*list(u)) * p
                    standard.append(block)
                    need(sp.simplify(transfer(block, value) - value_lam1*block) == sp.zeros(size), "standard block")
                need(len(standard) == size - 1, "standard dimension")

            zero_diagonal = centered_zero_diagonal_basis(size)
            need(len(zero_diagonal) == (size * (size - 3)//2 if size >= 3 else 0), "two-row dimension")
            if size >= 4:
                value_lam2 = sp.simplify(lam2.subs({n: size, eta: value}))
                for block in zero_diagonal:
                    need(sp.simplify(transfer(block, value) - value_lam2*block) == sp.zeros(size), "zero-diagonal block")

        total = 1 + (size - 1 if size >= 3 else 0) + (size*(size-3)//2 if size >= 4 else 0)
        need(total == size*(size-1)//2, "multiplicity closure")

    # Projector identities on independent rational test matrices.
    for size in range(3, 9):
        p = sp.eye(size) - sp.ones(size)/size
        raw = sp.Matrix(size, size, lambda i, j: (i-j)**2 + (i+1 if i == j else 0))
        raw = (raw + raw.T)/2
        a = sp.simplify(p*raw*p)
        pi0 = sp.trace(a)*p/(size-1)
        residual = a-pi0
        u = size*sp.Matrix([residual[i, i] for i in range(size)])/(size-2)
        pi1 = sp.simplify(p*sp.diag(*list(u))*p)
        pi2 = sp.simplify(a-pi0-pi1)
        need(sp.simplify(pi0+pi1+pi2-a) == sp.zeros(size), "projector sum")
        need(sp.trace(pi1) == 0 and sp.trace(pi2) == 0, "trace split")
        need(all(pi2[i, i] == 0 for i in range(size)), "zero diagonal")
        need(sp.simplify(pi2*sp.ones(size, 1)) == sp.zeros(size, 1), "zero row sum")
        need(sp.trace(pi0.T*pi1) == sp.trace(pi0.T*pi2) == sp.trace(pi1.T*pi2) == 0, "Frobenius orthogonality")
        need((pi2 == sp.zeros(size)) is (size == 3), "N three collapse")

    print(f"C333 SymPy cross-check: PASS {CHECKS} exact identities")


if __name__ == "__main__":
    main()
