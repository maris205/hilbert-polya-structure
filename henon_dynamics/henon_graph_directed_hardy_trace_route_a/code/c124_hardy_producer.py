#!/usr/bin/env python3
"""Produce the exact C124 graph-directed Hardy/Fredholm certificate.

The source is a frozen three-state graph-directed affine Henon contraction.
No external zero, arithmetic, or local-factor data enter this computation.
"""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import itertools
import json
from pathlib import Path
import sys

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "results/c124_hardy_evidence.json"


def frac(value: Fraction | int | sp.Rational) -> str:
    value = Fraction(int(sp.numer(value)), int(sp.denom(value))) if isinstance(value, sp.Basic) else Fraction(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def matrix_strings(matrix: sp.Matrix) -> list[list[str]]:
    return [[frac(matrix[i, j]) for j in range(matrix.cols)] for i in range(matrix.rows)]


def determinant_coefficients(traces: dict[int, Fraction], degree: int) -> list[Fraction]:
    coefficients = [Fraction(1)]
    for n in range(1, degree + 1):
        coefficients.append(-sum(traces[k] * coefficients[n - k] for k in range(1, n + 1)) / n)
    return coefficients


def admissible(word: tuple[int, ...], adjacency: list[list[int]]) -> bool:
    return all(adjacency[word[k]][word[(k + 1) % len(word)]] for k in range(len(word)))


def primitive(word: tuple[int, ...]) -> bool:
    n = len(word)
    return not any(n % d == 0 and word == word[:d] * (n // d) for d in range(1, n))


def least_rotation(word: tuple[int, ...]) -> tuple[int, ...]:
    return min(word[k:] + word[:k] for k in range(len(word)))


def compose_word(A: sp.Matrix, translations: list[sp.Rational], word: tuple[int, ...]) -> tuple[sp.Matrix, sp.Matrix, sp.Matrix, list[sp.Matrix]]:
    linear = sp.eye(2)
    shift = sp.zeros(2, 1)
    for symbol in word:
        shift = A * shift + sp.Matrix([translations[symbol], 0])
        linear = A * linear
    fixed = (sp.eye(2) - linear).inv() * shift
    phases: list[sp.Matrix] = []
    point = fixed
    for symbol in word:
        phases.append(point)
        point = A * point + sp.Matrix([translations[symbol], 0])
    assert sp.simplify(point - fixed) == sp.zeros(2, 1)
    return linear, shift, fixed, phases


def main() -> None:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUT

    A = sp.Matrix([[sp.Rational(3, 16), sp.Rational(-1, 32)], [sp.Rational(1, 4), 0]])
    translations = [sp.Rational(-2), sp.Rational(0), sp.Rational(2)]
    control_translations = [sp.Rational(-3, 2), sp.Rational(0), sp.Rational(3, 2)]
    B = sp.Matrix([[1, 1, 0], [1, 0, 1], [1, 0, 0]])
    weights = [sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(1, 5)]
    W = B * sp.diag(*weights)
    adjacency = [[int(B[i, j]) for j in range(3)] for i in range(3)]

    lam, z = sp.symbols("lam z")
    assert sp.expand(A.charpoly(lam).as_expr() - (lam - sp.Rational(1, 8)) * (lam - sp.Rational(1, 16))) == 0
    assert sp.expand((sp.eye(3) - z * W).det() - (1 - z / 2 - z**2 / 6 - z**3 / 30)) == 0
    row_norms = [sum(abs(A[i, j]) for j in range(2)) for i in range(2)]
    assert max(row_norms) == sp.Rational(1, 4)
    first_radius = 3 * sum(abs(A[0, j]) for j in range(2))
    second_radius = 3 * sum(abs(A[1, j]) for j in range(2))
    original_gap = min(translations[j + 1] - translations[j] for j in range(2)) - 2 * first_radius
    control_gap = min(control_translations[j + 1] - control_translations[j] for j in range(2)) - 2 * first_radius
    assert first_radius == sp.Rational(21, 32)
    assert second_radius == sp.Rational(3, 4)
    assert original_gap == sp.Rational(11, 16) > 0
    assert control_gap == sp.Rational(3, 16) > 0
    assert max(abs(t) + first_radius for t in translations) == sp.Rational(85, 32) < 3

    rooted_counts: dict[int, int] = {}
    primitive_representatives: dict[int, list[str]] = {}
    for n in range(1, 9):
        rooted = [word for word in itertools.product(range(3), repeat=n) if admissible(word, adjacency)]
        primitive_words = sorted({least_rotation(word) for word in rooted if primitive(word)})
        rooted_counts[n] = len(rooted)
        primitive_representatives[n] = ["".join(str(symbol) for symbol in word) for word in primitive_words]
        assert rooted_counts[n] == int(sp.trace(B**n))

    word = (0, 1, 2)
    assert admissible(word, adjacency) and primitive(word)
    monodromy, shift, fixed, phases = compose_word(A, translations, word)
    control_monodromy, control_shift, control_fixed, control_phases = compose_word(A, control_translations, word)
    assert monodromy == control_monodromy == A**3
    assert fixed != control_fixed

    symbolic_traces: dict[int, Fraction] = {}
    hardy_traces: dict[int, Fraction] = {}
    for n in range(1, 9):
        symbolic = sp.trace(W**n)
        denominator = (1 - sp.Rational(1, 8) ** n) * (1 - sp.Rational(1, 16) ** n)
        hardy = sp.factor(symbolic / denominator)
        symbolic_traces[n] = Fraction(int(sp.numer(symbolic)), int(sp.denom(symbolic)))
        hardy_traces[n] = Fraction(int(sp.numer(hardy)), int(sp.denom(hardy)))
    coefficients = determinant_coefficients(hardy_traces, 8)

    polynomial_cutoff_traces: dict[str, dict[str, str]] = {}
    for degree in range(0, 6):
        row: dict[str, str] = {}
        for n in range(1, 4):
            monomial_sum = sum(
                sp.Rational(1, 8) ** (r * n) * sp.Rational(1, 16) ** (s * n)
                for r in range(degree + 1)
                for s in range(degree + 1 - r)
            )
            row[str(n)] = frac(sp.factor(sp.trace(W**n) * monomial_sum))
        polynomial_cutoff_traces[str(degree)] = row

    payload = {
        "schema": "hcs-c124-graph-directed-hardy-trace-v1",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "source_lock": {
            "candidate_id": "HCS-C124",
            "phase_space": "three graph-directed copies of D_3^2",
            "clock": "one admissible graph edge per iterate",
            "normalization": "unscaled affine coordinates and edge weights c=(1/2,1/3,1/5)",
            "determinant_convention": "D_H(z)=det(I-z*L)",
            "orbit_cutoff": "none in the theorem; n<=8 is only the exact replay prefix",
            "precision": "exact rational and symbolic arithmetic",
            "allowed_data": "frozen matrices, translations, graph, and weights only",
            "forbidden_data": "external zero tables, prime tables, arithmetic/local factors, and Route-B inputs",
        },
        "frozen_model": {
            "A": matrix_strings(A),
            "A_characteristic_polynomial": "(lam-1/8)*(lam-1/16)",
            "A_eigenvalues": ["1/8", "1/16"],
            "translations": [frac(t) for t in translations],
            "branch_formula": "phi_j(x,y)=((3/16)x-(1/32)y+t_j,(1/4)x)",
            "adjacency_B": matrix_strings(B),
            "edge_weights_c": [frac(c) for c in weights],
            "weighted_adjacency_W_equals_B_diag_c": matrix_strings(W),
            "symbolic_determinant": "Delta(z)=det(I-zW)=1-z/2-z^2/6-z^3/30",
        },
        "strong_separation": {
            "polydisc_radius": "3",
            "A_infinity_row_norms": [frac(v) for v in row_norms],
            "A_infinity_norm": "1/4",
            "first_coordinate_image_radius": frac(first_radius),
            "second_coordinate_image_radius": frac(second_radius),
            "largest_first_coordinate_extent": "85/32",
            "strict_interior_margin_first_coordinate": "11/32",
            "original_pairwise_first_coordinate_gap": frac(original_gap),
            "strong_separation_proved": True,
            "coding_consequence": "admissible primitive cyclic words own distinct primitive geometric cycles modulo phase",
        },
        "periodic_orbits": {
            "all_period_theorem": "every admissible cyclic word has one fixed point of its affine composition; strong separation makes primitive coding injective modulo cyclic rotation",
            "rooted_closed_word_counts_n1_to_8": {str(n): rooted_counts[n] for n in range(1, 9)},
            "primitive_cycle_counts_n1_to_8": {str(n): len(primitive_representatives[n]) for n in range(1, 9)},
            "primitive_representatives_n1_to_8": {str(n): primitive_representatives[n] for n in range(1, 9)},
            "example_word": "012",
            "example_weight": "1/30",
            "example_monodromy_A_cubed": matrix_strings(monodromy),
            "example_composition_shift": matrix_strings(shift),
            "example_det_I_minus_monodromy": frac((sp.eye(2) - monodromy).det()),
            "example_fixed_phase_points": [[frac(v) for v in point] for point in phases],
        },
        "hardy_operator": {
            "space": "H=direct_sum_{i=0}^2 H^2(D_3^2)",
            "definition": "(L f)_i(z)=sum_j B_ij*c_j*f_j(phi_j(z))",
            "trace_class": True,
            "trace_class_reason": "each affine branch maps the closed radius-3 polydisc strictly inside it, giving a nuclear composition block; the graph sum is finite",
            "affine_composition_trace": "Tr(C_phi_word)=1/det(I-A^n)",
            "all_order_trace_formula": "Tr(L^n)=Tr(W^n)/((1-8^(-n))*(1-16^(-n)))",
            "symbolic_trace_powers_n1_to_8": {str(n): frac(symbolic_traces[n]) for n in range(1, 9)},
            "hardy_trace_powers_n1_to_8": {str(n): frac(hardy_traces[n]) for n in range(1, 9)},
            "polynomial_cutoff_trace_M0_to_M5_n1_to_n3": polynomial_cutoff_traces,
        },
        "fredholm_and_primitive_identity": {
            "fredholm_definition": "D_H(z)=det(I-z*L)",
            "entire": True,
            "lattice_product": "product_{r,s>=0} det(I-z*8^(-r)*16^(-s)*W)",
            "primitive_log_expansion": "log D_H=-sum_[gamma] sum_{m>=1} (c_gamma*z^ell_gamma)^m/(m*det(I-A^(m*ell_gamma)))",
            "taylor_coefficients_ascending_z0_to_z8": [frac(value) for value in coefficients],
            "coefficient_recurrence": "n*d_n=-sum_{k=1}^n Tr(L^k)*d_(n-k)",
            "owner_statement": "the same graph-directed source owns the primitive cycles, trace law, and Fredholm determinant",
        },
        "translation_blindness_control": {
            "control_translations": [frac(t) for t in control_translations],
            "control_pairwise_first_coordinate_gap": frac(control_gap),
            "control_still_strongly_separated": True,
            "same_A_B_c_W": True,
            "same_all_power_traces_and_fredholm_determinant": True,
            "control_example_composition_shift": matrix_strings(control_shift),
            "control_example_fixed_phase_points": [[frac(v) for v in point] for point in control_phases],
            "geometry_changed": True,
            "negative_conclusion": "the determinant detects symbolic weights and common stability but is blind to branch translations and orbit locations",
        },
        "progress_over_prior_gate": {
            "over_C119": "adds infinitely many nontrivial primitive graph-directed cycles and makes the global determinant orbit-owned",
            "over_C123": "replaces a degree-four finite moment prefix and period-six word cutoff by an all-period nuclear trace/Fredholm theorem",
            "remaining_obstruction": "no target divisor, functional equation, counting law, or arithmetic correspondence is tested",
        },
        "verdict": {
            "A1": "A1_WEAK",
            "A1_qualification": "ALL_PERIOD_INTRINSIC_PRIMITIVE_ORBITS_WITH_NO_PRIME_LIKE_TARGET_CORRESPONDENCE",
            "A2": "A2_FAIL",
            "A2_qualification": "EXACT_SOURCE_FREDHOLM_DETERMINANT_BUT_NO_FROZEN_TARGET_DIVISOR_MATCH",
            "A3": "A3_FAIL",
            "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_GAMMA_FACTOR_COUNTING_LAW_OR_CONTINUATION_COMPARISON",
            "A4": "A4_FAIL",
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "nonclaims": [
            "a target-facing zero or divisor match",
            "prime-like information or arithmetic/local data",
            "Euler factors, root numbers, automorphy, or a Riemann-zero correspondence",
            "a self-adjoint Hilbert--Polya operator or natural quantization",
            "Route-B authorization or a solution of the larger program",
            "determinant sensitivity to affine branch translations",
        ],
    }
    raw = json.dumps(payload, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(raw)
    print(json.dumps({
        "status": "C124_EXACT_EVIDENCE_PASS",
        "evidence_sha256": sha256(raw.encode()).hexdigest(),
        "rooted_words_through_8": sum(rooted_counts.values()),
        "primitive_cycles_through_8": sum(len(v) for v in primitive_representatives.values()),
        "trace_prefix": len(hardy_traces),
        "determinant_degree": len(coefficients) - 1,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
