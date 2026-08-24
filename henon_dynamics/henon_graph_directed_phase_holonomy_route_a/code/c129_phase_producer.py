#!/usr/bin/env python3
"""Produce the exact C129 Z/5 holonomy Hardy/Fredholm certificate."""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
import itertools
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "results/c129_phase_evidence.json"


def fs(value: Fraction | int) -> str:
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


@dataclass(frozen=True)
class G5:
    """Exact rational group ring Q[Z/5], basis e_0,...,e_4."""

    c: tuple[Fraction, Fraction, Fraction, Fraction, Fraction]

    @staticmethod
    def zero() -> "G5":
        return G5((Fraction(0),) * 5)

    @staticmethod
    def scalar(value: Fraction | int) -> "G5":
        return G5((Fraction(value), Fraction(0), Fraction(0), Fraction(0), Fraction(0)))

    @staticmethod
    def monomial(exponent: int, coefficient: Fraction | int = 1) -> "G5":
        row = [Fraction(0)] * 5
        row[exponent % 5] = Fraction(coefficient)
        return G5(tuple(row))  # type: ignore[arg-type]

    def __add__(self, other: "G5") -> "G5":
        return G5(tuple(a + b for a, b in zip(self.c, other.c)))  # type: ignore[arg-type]

    def __neg__(self) -> "G5":
        return G5(tuple(-a for a in self.c))  # type: ignore[arg-type]

    def __sub__(self, other: "G5") -> "G5":
        return self + (-other)

    def __mul__(self, other: "G5") -> "G5":
        row = [Fraction(0)] * 5
        for i, a in enumerate(self.c):
            for j, b in enumerate(other.c):
                row[(i + j) % 5] += a * b
        return G5(tuple(row))  # type: ignore[arg-type]

    def scale(self, value: Fraction | int) -> "G5":
        return G5(tuple(Fraction(value) * a for a in self.c))  # type: ignore[arg-type]

    def augmentation(self) -> Fraction:
        return sum(self.c)

    def cyclotomic_vector(self) -> tuple[Fraction, Fraction, Fraction, Fraction]:
        # Evaluate e_k at zeta_5^k and use zeta_5^4=-(1+zeta+zeta^2+zeta^3).
        return tuple(self.c[k] - self.c[4] for k in range(4))  # type: ignore[return-value]

    def strings(self) -> list[str]:
        return [fs(value) for value in self.c]

    def cyclotomic_strings(self) -> list[str]:
        return [fs(value) for value in self.cyclotomic_vector()]


def eye(n: int) -> list[list[G5]]:
    return [[G5.scalar(i == j) for j in range(n)] for i in range(n)]


def mmul(left: list[list[G5]], right: list[list[G5]]) -> list[list[G5]]:
    return [[sum((left[i][k] * right[k][j] for k in range(len(right))), G5.zero()) for j in range(len(right[0]))] for i in range(len(left))]


def mpow(matrix: list[list[G5]], n: int) -> list[list[G5]]:
    result = eye(len(matrix))
    base = matrix
    while n:
        if n & 1:
            result = mmul(result, base)
        base = mmul(base, base)
        n //= 2
    return result


def mtrace(matrix: list[list[G5]]) -> G5:
    return sum((matrix[i][i] for i in range(len(matrix))), G5.zero())


def weighted_matrix(B: list[list[int]], weights: list[Fraction], exponents: list[int]) -> list[list[G5]]:
    return [[G5.monomial(exponents[j], weights[j] * B[i][j]) for j in range(3)] for i in range(3)]


def determinant_coefficients(traces: dict[int, G5], degree: int) -> list[G5]:
    coefficients = [G5.scalar(1)]
    for n in range(1, degree + 1):
        total = sum((traces[k] * coefficients[n - k] for k in range(1, n + 1)), G5.zero())
        coefficients.append((-total).scale(Fraction(1, n)))
    return coefficients


def admissible(word: tuple[int, ...], B: list[list[int]]) -> bool:
    return all(B[word[k]][word[(k + 1) % len(word)]] for k in range(len(word)))


def primitive(word: tuple[int, ...]) -> bool:
    n = len(word)
    return not any(n % d == 0 and word == word[:d] * (n // d) for d in range(1, n))


def least_rotation(word: tuple[int, ...]) -> tuple[int, ...]:
    return min(word[k:] + word[:k] for k in range(len(word)))


def matmul2(left: list[list[Fraction]], right: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[sum(left[i][k] * right[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def matvec2(matrix: list[list[Fraction]], vector: list[Fraction]) -> list[Fraction]:
    return [sum(matrix[i][j] * vector[j] for j in range(2)) for i in range(2)]


def solve2(matrix: list[list[Fraction]], rhs: list[Fraction]) -> list[Fraction]:
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return [
        (rhs[0] * matrix[1][1] - matrix[0][1] * rhs[1]) / determinant,
        (matrix[0][0] * rhs[1] - rhs[0] * matrix[1][0]) / determinant,
    ]


def compose_cycle(A: list[list[Fraction]], translations: list[int], word: tuple[int, ...]) -> tuple[list[list[Fraction]], list[list[Fraction]]]:
    linear = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]
    shift = [Fraction(0), Fraction(0)]
    for symbol in word:
        shift = [v + w for v, w in zip(matvec2(A, shift), [Fraction(translations[symbol]), Fraction(0)])]
        linear = matmul2(A, linear)
    fixed = solve2([[Fraction(i == j) - linear[i][j] for j in range(2)] for i in range(2)], shift)
    phases = []
    point = fixed
    for symbol in word:
        phases.append(point)
        point = [v + w for v, w in zip(matvec2(A, point), [Fraction(translations[symbol]), Fraction(0)])]
    assert point == fixed
    return linear, phases


def canonical_hash(claims: dict) -> str:
    raw = json.dumps(claims, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def main() -> None:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUT
    A = [[Fraction(3, 16), Fraction(-1, 32)], [Fraction(1, 4), Fraction(0)]]
    B = [[1, 1, 0], [1, 0, 1], [1, 0, 0]]
    weights = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 5)]
    translations = [-2, 0, 2]
    control_translations = [0, -2, 2]
    exponents = [value % 5 for value in translations]
    control_exponents = [value % 5 for value in control_translations]
    W = weighted_matrix(B, weights, exponents)
    W_control = weighted_matrix(B, weights, control_exponents)

    original_delta = [G5.scalar(1), -G5.monomial(3, Fraction(1, 2)), -G5.monomial(3, Fraction(1, 6)), -G5.scalar(Fraction(1, 30))]
    control_delta = [G5.scalar(1), -G5.scalar(Fraction(1, 2)), -G5.monomial(3, Fraction(1, 6)), -G5.scalar(Fraction(1, 30))]

    original_symbolic: dict[int, G5] = {}
    control_symbolic: dict[int, G5] = {}
    original_hardy: dict[int, G5] = {}
    control_hardy: dict[int, G5] = {}
    for n in range(1, 9):
        denominator = (1 - Fraction(1, 8) ** n) * (1 - Fraction(1, 16) ** n)
        original_symbolic[n] = mtrace(mpow(W, n))
        control_symbolic[n] = mtrace(mpow(W_control, n))
        original_hardy[n] = original_symbolic[n].scale(1 / denominator)
        control_hardy[n] = control_symbolic[n].scale(1 / denominator)
    original_coefficients = determinant_coefficients(original_hardy, 8)
    control_coefficients = determinant_coefficients(control_hardy, 8)

    rooted_counts = {}
    primitive_reps = {}
    original_histograms = {}
    control_histograms = {}
    for n in range(1, 9):
        rooted = [word for word in itertools.product(range(3), repeat=n) if admissible(word, B)]
        reps = sorted({least_rotation(word) for word in rooted if primitive(word)})
        rooted_counts[str(n)] = len(rooted)
        primitive_reps[str(n)] = ["".join(map(str, word)) for word in reps]
        oh = [0] * 5
        ch = [0] * 5
        for word in reps:
            oh[sum(exponents[j] for j in word) % 5] += 1
            ch[sum(control_exponents[j] for j in word) % 5] += 1
        original_histograms[str(n)] = oh
        control_histograms[str(n)] = ch

    monodromy, phases = compose_cycle(A, translations, (0, 1, 2))
    control_monodromy, control_phases = compose_cycle(A, control_translations, (0, 1, 2))
    assert monodromy == control_monodromy
    assert original_hardy[1] != control_hardy[1]
    assert all(original_hardy[n].augmentation() == control_hardy[n].augmentation() for n in range(1, 9))
    assert all(original_coefficients[n].augmentation() == control_coefficients[n].augmentation() for n in range(9))

    def receipt(element: G5) -> dict:
        return {
            "group_ring_Z5_e0_to_e4": element.strings(),
            "primitive_zeta5_basis_1_zeta_zeta2_zeta3": element.cyclotomic_strings(),
            "trivial_character_augmentation": fs(element.augmentation()),
        }

    claims = {
        "source_lock": {
            "candidate_id": "HCS-C129",
            "phase_space": "three graph-directed copies of D_3^2 with a frozen flat Z/5 character",
            "clock": "one admissible graph edge per iterate",
            "normalization": "C124 affine coordinates, c=(1/2,1/3,1/5), chi(m)=zeta_5^m",
            "determinant_convention": "D_chi(z)=det(I-z*L_chi)",
            "orbit_cutoff": "none in theorem; periods 1 through 8 are exact replay only",
            "precision": "exact Q[Z/5], rational, and cyclotomic arithmetic",
            "forbidden_data": "external zero or prime tables, arithmetic/local factors, and Route-B inputs",
        },
        "frozen_model": {
            "A": [[fs(value) for value in row] for row in A],
            "A_eigenvalues": ["1/8", "1/16"],
            "B": [[str(value) for value in row] for row in B],
            "weights": [fs(value) for value in weights],
            "translations": [str(value) for value in translations],
            "holonomy_exponents_mod5": exponents,
            "character": "chi(m)=zeta_5^m with zeta_5 primitive",
            "operator": "(L_chi f)_i=sum_j B_ij*c_j*zeta_5^(t_j)*f_j(phi_j(z))",
        },
        "geometry": {
            "A_infinity_norm": "1/4",
            "first_coordinate_radius": "21/32",
            "second_coordinate_radius": "3/4",
            "pairwise_gap": "11/16",
            "strict_interior": True,
            "strong_separation": True,
        },
        "periodic_orbits": {
            "all_period_primitive_coding": True,
            "rooted_counts_n1_to_8": rooted_counts,
            "primitive_representatives_n1_to_8": primitive_reps,
            "primitive_holonomy_histogram_original_n1_to_8": original_histograms,
            "primitive_holonomy_histogram_control_n1_to_8": control_histograms,
            "example_word": "012",
            "example_holonomy_original": "zeta_5^0=1",
            "example_monodromy": [[fs(value) for value in row] for row in monodromy],
            "example_phase_points": [[fs(value) for value in point] for point in phases],
        },
        "trace_and_fredholm": {
            "trace_class": True,
            "all_order_trace_formula": "Tr(L_chi^n)=Tr(W_chi^n)/((1-8^(-n))*(1-16^(-n)))",
            "all_order_lattice_product": "D_chi(z)=product_{r,s>=0} det(I-z*8^(-r)*16^(-s)*W_chi)",
            "primitive_product": "log D_chi=-sum_[gamma]sum_m (c_gamma*chi(M_gamma)*z^ell)^m/(m*det(I-A^(m*ell)))",
            "symbolic_delta_original_z0_to_z3": [receipt(value) for value in original_delta],
            "power_traces_original_n1_to_8": {str(n): receipt(original_hardy[n]) for n in range(1, 9)},
            "fredholm_coefficients_original_z0_to_z8": [receipt(value) for value in original_coefficients],
        },
        "controls": {
            "control_translations": [str(value) for value in control_translations],
            "control_holonomy_exponents_mod5": control_exponents,
            "same_unordered_image_centers": True,
            "same_strong_separation": True,
            "same_untwisted_all_order_trace_and_determinant": True,
            "twisted_symbolic_delta_control_z0_to_z3": [receipt(value) for value in control_delta],
            "power_traces_control_n1_to_8": {str(n): receipt(control_hardy[n]) for n in range(1, 9)},
            "fredholm_coefficients_control_z0_to_z8": [receipt(value) for value in control_coefficients],
            "control_example_phase_points": [[fs(value) for value in point] for point in control_phases],
            "positive_control": "the primitive-zeta_5 linear Fredholm coefficient changes from -(64/105)zeta_5^3 to -64/105",
            "negative_control": "the trivial-character augmentation of every checked trace and coefficient agrees exactly",
            "trivial_character_degenerates_to_C124": True,
            "sensitivity_boundary": "position-sensitive only through the frozen translation-lattice character and branch assignment; no complete geometry recovery",
        },
        "progress_over_prior_gate": {
            "over_C124": "restores exact phase sensitivity to translation residues and branch assignment while retaining the same all-period nuclear owner",
            "remaining_obstruction": "the character sees only one finite quotient of the translation lattice and no target divisor is compared",
        },
        "verdict": {
            "A1": "A1_WEAK",
            "A2": "A2_FAIL",
            "A3": "A3_FAIL",
            "A4": "A4_FORMAL_HINT",
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "nonclaims": [
            "complete geometric recovery from holonomy",
            "a target-facing zero or divisor match",
            "prime-like information, arithmetic/local data, Euler factors, root numbers, or automorphy",
            "a self-adjoint Hilbert--Polya operator or Riemann-zero correspondence",
            "a unitary quantization or Route-B authorization",
        ],
    }
    payload = {
        "schema": "hcs-c129-phase-holonomy-v1",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "claims_sha256": canonical_hash(claims),
        "claims": claims,
    }
    raw = json.dumps(payload, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(raw)
    print(json.dumps({
        "status": "C129_EXACT_EVIDENCE_PASS",
        "evidence_sha256": sha256(raw.encode()).hexdigest(),
        "claims_sha256": payload["claims_sha256"],
        "rooted_words_through_8": sum(rooted_counts.values()),
        "primitive_cycles_through_8": sum(len(value) for value in primitive_reps.values()),
        "trace_prefix": 8,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
