#!/usr/bin/env python3
"""Produce exact evidence for the HCS-C148 open Walsh--baker gate."""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from math import gcd
from pathlib import Path


SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
K_VALUES = tuple(range(1, 6))
TRACE_SENTINEL = 12
PATH_K = 2
PATH_CUTOFF = 8


class QSI:
    """Exact a+b*sqrt(3)+c*i+d*sqrt(3)*i arithmetic."""

    __slots__ = ("v",)

    def __init__(self, a=0, b=0, c=0, d=0):
        self.v = tuple(Fraction(x) for x in (a, b, c, d))

    def __add__(self, other):
        other = other if isinstance(other, QSI) else QSI(other)
        return QSI(*(x + y for x, y in zip(self.v, other.v)))

    __radd__ = __add__

    def __neg__(self):
        return QSI(*(-x for x in self.v))

    def __sub__(self, other):
        return self + (-(other if isinstance(other, QSI) else QSI(other)))

    def __mul__(self, other):
        other = other if isinstance(other, QSI) else QSI(other)
        a, b, c, d = self.v
        e, f, g, h = other.v
        return QSI(
            a * e + 3 * b * f - c * g - 3 * d * h,
            a * f + b * e - c * h - d * g,
            a * g + 3 * b * h + c * e + 3 * d * f,
            a * h + b * g + c * f + d * e,
        )

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        scalar = Fraction(scalar)
        return QSI(*(x / scalar for x in self.v))

    def __pow__(self, exponent: int):
        if exponent < 0:
            raise ValueError("negative powers are not used")
        ans, base = QSI(1), self
        while exponent:
            if exponent & 1:
                ans = ans * base
            base = base * base
            exponent //= 2
        return ans

    def __eq__(self, other):
        other = other if isinstance(other, QSI) else QSI(other)
        return self.v == other.v

    def __bool__(self):
        return any(self.v)

    @staticmethod
    def _q(value: Fraction) -> str:
        return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"

    def receipt(self) -> list[str]:
        return [self._q(value) for value in self.v]


ZERO = QSI()
ONE = QSI(1)
SQRT3_OVER_3 = QSI(0, Fraction(1, 3))
TRACE_A = QSI(0, Fraction(1, 6), Fraction(-1, 2))
DET_NONZERO_A = QSI(Fraction(-1, 2), 0, 0, Fraction(-1, 6))


def one_qutrit_action(source: int) -> list[tuple[int, QSI]]:
    """Columns of A=F_3^* P, with P=diag(1,0,1)."""
    if source == 1:
        return []
    if source == 0:
        return [(target, SQRT3_OVER_3) for target in range(3)]
    return [
        (0, SQRT3_OVER_3),
        (1, QSI(0, Fraction(-1, 6), Fraction(1, 2))),
        (2, QSI(0, Fraction(-1, 6), Fraction(-1, 2))),
    ]


def states(k: int) -> list[tuple[int, ...]]:
    return list(product(range(3), repeat=k))


def gate_edges(state: tuple[int, ...]) -> list[tuple[tuple[int, ...], QSI]]:
    return [(state[1:] + (target,), weight) for target, weight in one_qutrit_action(state[0])]


def power_traces_a(limit: int) -> list[QSI]:
    """p_m=Tr(A^m); the two nonzero roots obey x^2-t*x+q=0."""
    values = [QSI(2), TRACE_A]
    for _ in range(2, limit + 1):
        values.append(TRACE_A * values[-1] - DET_NONZERO_A * values[-2])
    return values


def trace_formula(k: int, n: int, traces_a: list[QSI]) -> QSI:
    d = gcd(n, k)
    return traces_a[n // d] ** d


def secular_coefficients(k: int, traces_a: list[QSI]) -> list[QSI]:
    """Newton coefficients of D_k(z)=det(I-zB_k), through degree 2^k."""
    degree = 2**k
    traces = [trace_formula(k, n, traces_a) for n in range(1, degree + 1)]
    coeff = [ONE]
    for n in range(1, degree + 1):
        coeff.append(-sum((coeff[n - j] * traces[j - 1] for j in range(1, n + 1)), ZERO) / n)
    if not coeff[-1]:
        raise AssertionError("the advertised exact degree collapsed")
    return coeff


def direct_trace_rows(k: int, cutoff: int) -> list[dict]:
    """Direct sparse basis-state propagation; it does not use the gcd formula."""
    basis = states(k)
    rows = [{"n": n, "rooted_nonzero_closed_walks": 0, "trace_Bk_power": ZERO} for n in range(1, cutoff + 1)]
    for start in basis:
        current: dict[tuple[int, ...], tuple[int, QSI]] = {start: (1, ONE)}
        for n in range(1, cutoff + 1):
            nxt: dict[tuple[int, ...], tuple[int, QSI]] = {}
            for state, (count, amplitude) in current.items():
                for target, weight in gate_edges(state):
                    old_count, old_amplitude = nxt.get(target, (0, ZERO))
                    nxt[target] = (old_count + count, old_amplitude + amplitude * weight)
            current = nxt
            count, amplitude = current.get(start, (0, ZERO))
            rows[n - 1]["rooted_nonzero_closed_walks"] += count
            rows[n - 1]["trace_Bk_power"] = rows[n - 1]["trace_Bk_power"] + amplitude
    return [
        {
            "n": row["n"],
            "rooted_nonzero_closed_walks": row["rooted_nonzero_closed_walks"],
            "trace_Bk_power_q_sqrt3_i_sqrt3i": row["trace_Bk_power"].receipt(),
        }
        for row in rows
    ]


def rotations(word: tuple[int, ...]) -> list[tuple[int, ...]]:
    return [word[j:] + word[:j] for j in range(len(word))]


def primitive(word: tuple[int, ...]) -> bool:
    n = len(word)
    return all(n % d or word != word[:d] * (n // d) for d in range(1, n))


def primitive_path_ledger(k: int, cutoff: int) -> list[dict]:
    basis = states(k)
    index = {state: j for j, state in enumerate(basis)}
    adjacency = {
        index[state]: [(index[target], weight) for target, weight in gate_edges(state)]
        for state in basis
    }
    rows = []
    for length in range(1, cutoff + 1):
        rooted_count = 0
        amplitude_sum = ZERO
        primitive_cycles: dict[tuple[int, ...], QSI] = {}

        def walk(start: int, current: int, vertices: list[int], weight: QSI, remaining: int) -> None:
            nonlocal rooted_count, amplitude_sum
            if remaining == 0:
                if current == start:
                    rooted_count += 1
                    amplitude_sum = amplitude_sum + weight
                    cycle = tuple(vertices)
                    if primitive(cycle):
                        canonical = min(rotations(cycle))
                        previous = primitive_cycles.get(canonical)
                        if previous is not None and previous != weight:
                            raise AssertionError("rotation changed a cycle amplitude")
                        primitive_cycles[canonical] = weight
                return
            for target, edge_weight in adjacency[current]:
                walk(start, target, vertices if remaining == 1 else vertices + [target], weight * edge_weight, remaining - 1)

        for start in range(len(basis)):
            walk(start, start, [start], ONE, length)
        rows.append(
            {
                "n": length,
                "rooted_nonzero_closed_walks": rooted_count,
                "closed_walk_amplitude_sum_q_sqrt3_i_sqrt3i": amplitude_sum.receipt(),
                "primitive_cycle_count": len(primitive_cycles),
                "primitive_amplitude_sum_q_sqrt3_i_sqrt3i": sum(primitive_cycles.values(), ZERO).receipt(),
            }
        )
    return rows


def payload_hash(payload: dict) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def build_evidence() -> dict:
    traces_a = power_traces_a(max(TRACE_SENTINEL, 2 ** max(K_VALUES)))
    trace_ledgers = {}
    polynomial_ledgers = {}
    rank_ledgers = []
    for k in K_VALUES:
        direct = direct_trace_rows(k, TRACE_SENTINEL)
        for row in direct:
            if row["trace_Bk_power_q_sqrt3_i_sqrt3i"] != trace_formula(k, row["n"], traces_a).receipt():
                raise AssertionError(f"direct trace mismatch at k={k}, n={row['n']}")
        trace_ledgers[str(k)] = direct
        coeff = secular_coefficients(k, traces_a)
        polynomial_ledgers[str(k)] = {
            "matrix_dimension": 3**k,
            "secular_degree": 2**k,
            "zero_eigenvalue_algebraic_multiplicity": 3**k - 2**k,
            "coefficient_basis": "a+b*sqrt(3)+c*i+d*sqrt(3)*i",
            "secular_coefficients_ascending": [value.receipt() for value in coeff],
            "nonzero_coefficient_degrees": [j for j, value in enumerate(coeff) if value],
            "characteristic_polynomial": "chi_k(lambda)=lambda^(3^k-2^k)*sum_(j=0)^(2^k)c_(k,j)*lambda^(2^k-j)",
        }
        rank_ledgers.append(
            {
                "k": k,
                "dimension": 3**k,
                "rank_Bk": 2 * 3 ** (k - 1),
                "kernel_dimension_Bk": 3 ** (k - 1),
                "rank_Bk_power_k": 2**k,
                "kernel_dimension_Bk_power_k": 3**k - 2**k,
                "left_defect_rank": 3 ** (k - 1),
                "right_defect_rank": 3 ** (k - 1),
            }
        )

    payload = {
        "schema": "hcs-c148-open-walsh-baker-evidence-v1",
        "candidate_id": "HCS-C148",
        "evaluation_date": "2026-08-25",
        "scope_literal": SCOPE,
        "source_lock": {
            "object": "three-symbol Walsh open baker family B_k on H_k=(C^3)^(tensor k)",
            "basis_order": "lexicographic qutrit words 0,1,2 of length k",
            "omega": "exp(2*pi*i/3)=(-1+i*sqrt(3))/2",
            "fourier": "F3[j,l]=omega^(j*l)/sqrt(3), j,l in {0,1,2}",
            "projector": "P=diag(1,0,1)",
            "one_qutrit_gate": "A=F3^* P",
            "shift_gate": "B_k(v0 tensor ... tensor v_(k-1))=v1 tensor ... tensor v_(k-1) tensor A*v0",
            "clock": "one application of B_k",
            "normalization": "unitary normalized three-point DFT and no spectral rescaling",
            "determinant_convention": "D_k(z)=det(I_(3^k)-z*B_k)",
            "finite_polynomial_range": list(K_VALUES),
            "direct_trace_sentinel": TRACE_SENTINEL,
            "primitive_path_sentinel": {"k": PATH_K, "period": PATH_CUTOFF},
            "precision": "exact Q(sqrt(3),i) arithmetic represented in the ordered basis 1,sqrt(3),i,sqrt(3)*i",
            "allowed_data": "the frozen DFT, projector, tensor shift, and exact complex path amplitudes",
            "forbidden_data": "target zeros or divisors, prime or arithmetic local data, Euler factors, root numbers, automorphy, Hilbert--Polya, Route B",
        },
        "one_qutrit_receipt": {
            "matrix_columns": "A=(1/sqrt(3))*[[1,0,1],[1,0,omega],[1,0,omega^2]]",
            "trace_A_q_sqrt3_i_sqrt3i": TRACE_A.receipt(),
            "nonzero_eigenvalue_product_q_sqrt3_i_sqrt3i": DET_NONZERO_A.receipt(),
            "characteristic_polynomial": "lambda*(lambda^2-(sqrt(3)/6-i/2)*lambda-1/2-sqrt(3)*i/6)",
            "A_star_A": "P",
            "A_A_star": "F3^* P F3",
            "rank_A": 2,
            "operator_norm_A": "1",
        },
        "rank_correction_and_escape_ledger": {
            "rejected_statement": "rank(B_k)=2^k",
            "reason": "one step opens only the departing tensor factor",
            "correct_statement": "rank(B_k)=rank(A)*3^(k-1)=2*3^(k-1)",
            "k_step_statement": "B_k^k=A^(tensor k) and rank(B_k^k)=2^k",
            "algebraic_zero_multiplicity": "3^k-2^k",
            "rows": rank_ledgers,
        },
        "all_period_theorem": {
            "contraction": "B_k is a norm-one contraction",
            "k_step_identity": "B_k^k=A^(tensor k)",
            "trace_formula": "for d=gcd(n,k), Tr(B_k^n)=Tr(A^(n/d))^d for every n>=1",
            "trace_formula_proof_object": "cycle decomposition of the factor permutation induced by shift^n",
            "fredholm_identity": "D_k(z)=exp(-sum_(n>=1)Tr(B_k^n)z^n/n)",
            "closed_walk_identity": "Tr(B_k^n)=sum_(rooted nonzero length-n basis-state closed walks) amplitude(walk)",
            "primitive_product": "D_k(z)=product_[gamma primitive](1-z^|gamma|*amplitude(gamma))",
            "formal_status": "the logarithm and primitive product are formal at z=0; the raw path product is absolutely regroupable for |z|<1/sqrt(3)",
            "finite_dimension_status": "D_k is the exact secular polynomial; the series exponentiates to it near zero and then continues polynomially",
        },
        "subunitarity_defect": {
            "right_gram": "B_k^* B_k=P tensor I_(3^(k-1))",
            "right_defect": "I-B_k^*B_k=(I-P) tensor I_(3^(k-1))",
            "left_gram": "B_k B_k^*=I_(3^(k-1)) tensor F3^* P F3",
            "left_defect": "I-B_kB_k^*=I_(3^(k-1)) tensor F3^*(I-P)F3",
            "projection_status": "both defects are orthogonal projections",
            "rank_each": "3^(k-1)",
        },
        "trace_ledgers": trace_ledgers,
        "characteristic_polynomials_k1_to_k5": polynomial_ledgers,
        "primitive_path_ledger": {
            "k": PATH_K,
            "period_limit": PATH_CUTOFF,
            "rows": primitive_path_ledger(PATH_K, PATH_CUTOFF),
            "finite_prefix_is_not_theorem_cutoff": True,
        },
        "controls": {
            "closed_control": {
                "projector": "P_closed=I_3",
                "gate": "A_closed=F3^*",
                "result": "B_k,closed is unitary, has rank 3^k, and both defects vanish",
                "trace_A_closed_q_sqrt3_i_sqrt3i": QSI(0, 0, -1, 0).receipt(),
            },
            "projector_order_control": {
                "alternative": "A_right=P F3^*",
                "similarity": "A_right=F3 A F3^*",
                "spectral_result": "Tr(A_right^m)=Tr(A^m), hence every D_k is unchanged",
                "geometric_result": "the one-qutrit left and right Gram projections exchange their P and Fourier-conjugate placements",
            },
            "hole_position_control": {
                "alternative_projector": "P0=diag(0,1,1)",
                "trace_A0_q_sqrt3_i_sqrt3i": QSI(0, Fraction(-1, 3), -1, 0).receipt(),
                "frozen_linear_coefficient_q_sqrt3_i_sqrt3i": (-TRACE_A).receipt(),
                "alternative_linear_coefficient_q_sqrt3_i_sqrt3i": QSI(0, Fraction(1, 3), 1, 0).receipt(),
                "result": "opening rank is unchanged but the secular polynomial changes already at the coefficient of z",
            },
            "antiunitary_symmetry": "NOT_ASSERTED",
        },
        "route_a": {
            "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_UNITARY_OR_SCATTERING_CANDIDATE"],
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "claim_boundary": {
            "finite_k_scattering_gate_only": True,
            "self_adjoint_quantization": False,
            "semiclassical_target_matching": False,
            "target_divisor_matching": False,
            "target_functional_equation": False,
            "target_counting_law": False,
            "prime_like_correspondence": False,
            "arithmetic_local_data": False,
            "euler_factors": False,
            "root_numbers": False,
            "automorphy": False,
            "self_adjoint_hilbert_polya": False,
        },
        "nonclaims": [
            "rank(B_k)=2^k at one step",
            "a self-adjoint quantization or a semiclassical target match",
            "a target zero or divisor match, functional equation, or counting law",
            "prime-like information, arithmetic local data, Euler factors, root numbers, or automorphy",
            "an antiunitary symmetry, a Hilbert--Polya operator, or Route-B authorization",
        ],
    }
    payload["payload_sha256"] = payload_hash(payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "results/c148_walsh_baker_evidence.json",
    )
    args = parser.parse_args()
    payload = build_evidence()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "payload_sha256": payload["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
