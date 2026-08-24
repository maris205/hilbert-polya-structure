#!/usr/bin/env python3
"""Produce the exact C123 additive-noise Hénon certificate."""
from __future__ import annotations

import argparse
from hashlib import sha256
from itertools import product
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results" / "c123_noise_evidence.json"
A = sp.Matrix([[sp.Rational(1, 2), sp.Rational(-1, 4)], [sp.Rational(1, 4), 0]])


def ss(v: sp.Expr) -> str:
    return sp.sstr(sp.factor(v))


def vec(v: sp.Matrix) -> list[str]:
    return [ss(x) for x in v]


def mat(M: sp.Matrix) -> list[list[str]]:
    return [[ss(M[i, j]) for j in range(M.cols)] for i in range(M.rows)]


def step(v: sp.Matrix, symbol: int) -> sp.Matrix:
    return A * v + sp.Matrix([sp.Rational(symbol, 2), 0])


def min_rotation(word: tuple[int, ...]) -> tuple[int, ...]:
    return min(word[i:] + word[:i] for i in range(len(word)))


def primitive(word: tuple[int, ...]) -> bool:
    n = len(word)
    return all(word != word[:d] * (n // d) for d in range(1, n) if n % d == 0)


def cycle_for_word(word: tuple[int, ...]) -> list[sp.Matrix]:
    C = sp.eye(2)
    t = sp.zeros(2, 1)
    for symbol in word:
        t = A * t + sp.Matrix([sp.Rational(symbol, 2), 0])
        C = A * C
    p = (sp.eye(2) - C).inv() * t
    states = [sp.simplify(p)]
    for symbol in word[:-1]:
        states.append(sp.simplify(step(states[-1], symbol)))
    assert sp.simplify(step(states[-1], word[-1]) - states[0]) == sp.zeros(2, 1)
    return states


def polynomial_markov_operator():
    x, y, z = sp.symbols("x y z")
    basis, exponents = [], []
    for degree in range(5):
        for i in range(degree, -1, -1):
            j = degree - i
            basis.append(x**i * y**j)
            exponents.append((i, j))
    linear_x = A[0, 0] * x + A[0, 1] * y
    linear_y = A[1, 0] * x
    K = sp.zeros(15)
    for col, (i, j) in enumerate(exponents):
        image = sp.expand(((linear_x + sp.Rational(1, 2)) ** i * linear_y**j + (linear_x - sp.Rational(1, 2)) ** i * linear_y**j) / 2)
        poly = sp.Poly(image, x, y)
        for row, monomial in enumerate(basis):
            K[row, col] = poly.coeff_monomial(monomial)
    det_poly = sp.Poly((sp.eye(15) - z * K).det(), z)
    moments = sp.symbols("m0:15")
    solution = sp.solve(list((K.T - sp.eye(15)) * sp.Matrix(moments)) + [moments[0] - 1], moments, dict=True)[0]
    mu = sp.Matrix([solution[m] for m in moments])
    return basis, K, [sp.factor(c) for c in reversed(det_poly.all_coeffs())], mu


def build() -> dict:
    rows, counts = [], {}
    for n in range(1, 7):
        words = [w for w in product((-1, 1), repeat=n) if primitive(w) and w == min_rotation(w)]
        counts[str(n)] = len(words)
        for word in words:
            states = cycle_for_word(word)
            rows.append({
                "period": n,
                "canonical_word": ["-" if s < 0 else "+" for s in word],
                "states": [vec(v) for v in states],
                "primitive": True,
                "cycle_closes": True,
                "chosen_rooted_block_probability": ss(sp.Rational(1, 2) ** n),
                "composition_linear_part": mat(A**n),
                "composition_determinant": ss(A.det() ** n),
            })

    basis, K, det_coeffs, mu = polynomial_markov_operator()
    Sigma = sp.Matrix([[mu[3], mu[4]], [mu[4], mu[5]]])
    Q = sp.diag(sp.Rational(1, 4), 0)
    AtA = A.T * A
    return {
        "schema_id": "hcs-c123-additive-noise-henon-moment-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "source_model": {
            "random_map": "F_sigma(x,y)=(x/2-y/4+sigma/2,x/4), sigma in {-1,+1} iid uniform",
            "linear_part": mat(A),
            "noise_support": ["-1/2", "1/2"],
            "noise_probabilities": ["1/2", "1/2"],
            "linear_eigenvalues": ["1/4", "1/4"],
            "linear_determinant": "1/16",
            "singular_value_squares": [ss(v) for v in sorted(AtA.eigenvals(), key=sp.default_sort_key)],
        },
        "periodic_noise_word_atlas": {
            "maximum_period": 6,
            "rooted_words_tested": sum(2**n for n in range(1, 7)),
            "primitive_necklace_counts": counts,
            "primitive_necklace_total": len(rows),
            "row_probability_semantics": "chosen rooted length-n block probability under the iid law; not necklace total mass; not infinite periodic-orbit probability",
            "rows": rows,
        },
        "degree_four_markov_operator": {
            "basis": [sp.sstr(b) for b in basis],
            "orientation": "column j contains coefficients of P(basis_j) in the displayed basis",
            "dimension": 15,
            "matrix": mat(K),
            "trace": ss(sp.trace(K)),
            "determinant": ss(K.det()),
            "det_I_minus_z": [ss(c) for c in det_coeffs],
        },
        "stationary_moments_through_degree_four": {
            "basis": [sp.sstr(b) for b in basis],
            "moments": vec(mu),
            "covariance": mat(Sigma),
            "covariance_determinant": ss(Sigma.det()),
            "lyapunov_residual": mat(sp.simplify(Sigma - A * Sigma * A.T - Q)),
            "x_fourth_cumulant": ss(sp.factor(mu[10] - 3 * mu[3] ** 2)),
            "noise_ablated_stationary_covariance": [["0", "0"], ["0", "0"]],
        },
        "route_a_verdict": {
            "A1": "A1_WEAK",
            "A1_qualification": "EXACT_INTRINSIC_NOISE_WORD_PREFIX_BUT_NO_PRIME_LIKE_TARGET_CORRESPONDENCE",
            "A2": "A2_FAIL",
            "A2_qualification": "DEGREE_FOUR_MARKOV_DETERMINANT_HAS_NO_TARGET_DIVISOR_MATCH_OR_ANALYTIC_BRIDGE",
            "A3": "A3_FAIL",
            "A3_qualification": "NO_GLOBAL_ANALYTIC_STRUCTURE_OR_CONTINUATION_THEOREM",
            "A4": "A4_FAIL", "overall": "ROUTE_A_EXPLORATORY",
        },
        "claims": {
            "exact_random_affine_henon_system": True,
            "exact_periodic_noise_word_prefix": True,
            "exact_degree_four_markov_operator": True,
            "exact_stationary_moments_through_degree_four": True,
            "complete_random_orbit_atlas": False,
            "global_nuclear_or_fredholm_owner": False,
            "prime_like_target_correspondence": False,
            "target_divisor_match": False,
            "analytic_bridge": False,
            "arithmetic_local_data": False, "euler_factors": False, "root_numbers": False,
            "automorphy": False, "hilbert_polya_operator": False, "route_b_authorized": False,
        },
        "reproducibility": {"number_system": "Q(sqrt(2))", "randomness": "model law only; enumeration is exhaustive and deterministic", "producer": "code/c123_noise_producer.py"},
    }


def canonical_bytes(data: dict) -> bytes:
    return (json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = canonical_bytes(build())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(payload)
    print(json.dumps({"status": "C123_PREFREEZE_G3_PASS", "evidence_sha256": sha256(payload).hexdigest(), "primitive_necklaces": 23, "markov_dimension": 15}, sort_keys=True))


if __name__ == "__main__":
    main()
