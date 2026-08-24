#!/usr/bin/env python3
"""Fresh SymPy reconstruction of the C124 analytic and finite-section data."""
from __future__ import annotations

import json
from pathlib import Path
import sys

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c124_hardy_evidence.json"


def s(value: sp.Expr) -> str:
    value = sp.factor(value)
    return str(value.p) if isinstance(value, sp.Rational) and value.q == 1 else f"{value.p}/{value.q}" if isinstance(value, sp.Rational) else str(value)


def mstrings(matrix: sp.Matrix) -> list[list[str]]:
    return [[s(matrix[i, j]) for j in range(matrix.cols)] for i in range(matrix.rows)]


def finite_polynomial_operator(degree: int, A: sp.Matrix, translations: list[sp.Rational], B: sp.Matrix, weights: list[sp.Rational]) -> sp.Matrix:
    x, y = sp.symbols("x y")
    basis = [(a, b) for total in range(degree + 1) for a in range(total + 1) for b in [total - a]]
    index = {(component, exponent): component * len(basis) + k for component in range(3) for k, exponent in enumerate(basis)}
    matrix = sp.zeros(3 * len(basis))
    for source_component in range(3):
        xp = A[0, 0] * x + A[0, 1] * y + translations[source_component]
        yp = A[1, 0] * x + A[1, 1] * y
        for k, (a, b) in enumerate(basis):
            column = source_component * len(basis) + k
            polynomial = sp.Poly(sp.expand(xp**a * yp**b), x, y)
            for output_component in range(3):
                if not B[output_component, source_component]:
                    continue
                for (u, v), coefficient in polynomial.terms():
                    row = index[(output_component, (u, v))]
                    matrix[row, column] += weights[source_component] * coefficient
    return matrix


def compose(A: sp.Matrix, translations: list[sp.Rational], word: tuple[int, ...]) -> tuple[sp.Matrix, list[sp.Matrix]]:
    linear = sp.eye(2)
    shift = sp.zeros(2, 1)
    for symbol in word:
        shift = A * shift + sp.Matrix([translations[symbol], 0])
        linear = A * linear
    fixed = (sp.eye(2) - linear).inv() * shift
    phases = []
    point = fixed
    for symbol in word:
        phases.append(point)
        point = A * point + sp.Matrix([translations[symbol], 0])
    assert sp.simplify(point - fixed) == sp.zeros(2, 1)
    return linear, phases


def main() -> None:
    evidence_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_EVIDENCE
    data = json.loads(evidence_path.read_text())
    checks = 0

    def ck(condition: bool, label: str) -> None:
        nonlocal checks
        if not condition:
            raise AssertionError(label)
        checks += 1

    A = sp.Matrix([[sp.Rational(3, 16), sp.Rational(-1, 32)], [sp.Rational(1, 4), 0]])
    translations = [sp.Rational(-2), 0, sp.Rational(2)]
    control = [sp.Rational(-3, 2), 0, sp.Rational(3, 2)]
    B = sp.Matrix([[1, 1, 0], [1, 0, 1], [1, 0, 0]])
    weights = [sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(1, 5)]
    W = B * sp.diag(*weights)
    lam, z = sp.symbols("lam z")

    ck(sp.expand(A.charpoly(lam).as_expr() - (lam - sp.Rational(1, 8)) * (lam - sp.Rational(1, 16))) == 0, "A charpoly")
    ck(A.det() == sp.Rational(1, 128), "A determinant")
    ck(max(sum(abs(A[i, j]) for j in range(2)) for i in range(2)) == sp.Rational(1, 4), "contraction")
    ck(sp.expand((sp.eye(3) - z * W).det() - (1 - z / 2 - z**2 / 6 - z**3 / 30)) == 0, "symbolic determinant")
    ck(data["frozen_model"]["W" if "W" in data["frozen_model"] else "weighted_adjacency_W_equals_B_diag_c"] == mstrings(W), "evidence W")

    symbolic_traces = {}
    hardy_traces = {}
    for n in range(1, 9):
        symbolic_traces[n] = sp.factor(sp.trace(W**n))
        hardy_traces[n] = sp.factor(symbolic_traces[n] / ((1 - sp.Rational(1, 8) ** n) * (1 - sp.Rational(1, 16) ** n)))
    ck(data["hardy_operator"]["symbolic_trace_powers_n1_to_8"] == {str(n): s(symbolic_traces[n]) for n in range(1, 9)}, "symbolic trace evidence")
    ck(data["hardy_operator"]["hardy_trace_powers_n1_to_8"] == {str(n): s(hardy_traces[n]) for n in range(1, 9)}, "Hardy trace evidence")

    coefficients = [sp.Integer(1)]
    for n in range(1, 9):
        coefficients.append(sp.factor(-sum(hardy_traces[k] * coefficients[n - k] for k in range(1, n + 1)) / n))
    ck(data["fredholm_and_primitive_identity"]["taylor_coefficients_ascending_z0_to_z8"] == [s(value) for value in coefficients], "coefficient evidence")

    for degree in (1, 2, 3):
        finite = finite_polynomial_operator(degree, A, translations, B, weights)
        ck(finite.rows == 3 * (degree + 1) * (degree + 2) // 2, f"finite dimension M={degree}")
        for n in range(1, 5):
            partial = sum(
                sp.Rational(1, 8) ** (r * n) * sp.Rational(1, 16) ** (q * n)
                for r in range(degree + 1)
                for q in range(degree + 1 - r)
            )
            ck(sp.factor(sp.trace(finite**n) - symbolic_traces[n] * partial) == 0, f"finite trace M={degree},n={n}")

    monodromy, phases = compose(A, translations, (0, 1, 2))
    control_monodromy, control_phases = compose(A, control, (0, 1, 2))
    ck(monodromy == A**3 == control_monodromy, "monodromy")
    ck(data["periodic_orbits"]["example_monodromy_A_cubed"] == mstrings(monodromy), "monodromy evidence")
    ck(data["periodic_orbits"]["example_fixed_phase_points"] == [[s(v) for v in point] for point in phases], "phase evidence")
    ck(data["translation_blindness_control"]["control_example_fixed_phase_points"] == [[s(v) for v in point] for point in control_phases], "control phase evidence")
    ck(phases != control_phases, "translation changes geometry")
    ck((sp.eye(2) - A**3).det() == sp.Rational(2092545, 2097152), "cycle determinant")
    ck(data["verdict"]["route_b_invocation_allowed"] is False, "route B off")
    ck(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")

    print(json.dumps({"status": "C124_SYMPY_CROSSCHECK_PASS", "symbolic_checks": checks, "finite_matrix_max_dimension": 30}, sort_keys=True))


if __name__ == "__main__":
    main()
