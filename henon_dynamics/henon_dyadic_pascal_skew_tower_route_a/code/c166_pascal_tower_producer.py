#!/usr/bin/env python3
"""Produce exact finite sentinels for the HCS-C166 Pascal skew tower."""
from __future__ import annotations

import argparse
from hashlib import sha256
from itertools import product
import json
from math import comb
from pathlib import Path


R_MAX = 6
D_MAX = 16
DIRECT_STATE_LIMIT = 4096
SOURCE_COMMIT = "4342893ce5e2516924181744bfacc01c12e4959d"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"


def canonical_hash(payload):
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"),
                     ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def floor_log2(value):
    return value.bit_length() - 1


def tower_step(state, modulus):
    return tuple((state[i] + state[i + 1]) % modulus
                 for i in range(len(state) - 1)) + ((state[-1] + 1) % modulus,)


def fixed_by_coefficients(modulus, dimension, iterate):
    return all(comb(iterate, k) % modulus == 0
               for k in range(1, dimension + 1))


def matrix_multiply(left, right, modulus):
    size = len(left)
    return [[sum(left[i][k] * right[k][j] for k in range(size)) % modulus
             for j in range(size)] for i in range(size)]


def identity(size):
    return [[int(i == j) for j in range(size)] for i in range(size)]


def polynomial_multiply(left, right, modulus):
    size = len(left)
    out = [0] * size
    for i, a in enumerate(left):
        for j, b in enumerate(right[:size - i]):
            out[i + j] = (out[i + j] + a * b) % modulus
    return out


def substitution_matrix(modulus, dimension):
    """Matrix of p(t) -> p(-t/(1+t)), built by truncated multiplication."""
    size = dimension + 1
    image_t = [0] + [(-1) ** degree % modulus for degree in range(1, size)]
    powers = [[1] + [0] * dimension]
    for _ in range(dimension):
        powers.append(polynomial_multiply(powers[-1], image_t, modulus))
    return [[powers[column][row] for column in range(size)] for row in range(size)]


def multiplier_matrices(modulus, dimension):
    size = dimension + 1
    forward = identity(size)
    inverse = identity(size)
    for row in range(1, size):
        forward[row][row - 1] = 1
        for column in range(row):
            inverse[row][column] = (-1) ** (row - column) % modulus
    return forward, inverse


def direct_period_certificate(modulus, dimension, expected_period):
    checked = 0
    for state in product(range(modulus), repeat=dimension):
        current = state
        first_return = None
        for iterate in range(1, expected_period + 1):
            current = tower_step(current, modulus)
            if current == state:
                first_return = iterate
                break
        assert first_return == expected_period
        checked += 1
    return checked


def build_validation():
    coefficient_cases = 0
    direct_states = 0
    direct_rows = 0
    reversor_matrix_rows = 0
    sentinels = []
    selected = {(1, 2), (1, 3), (1, 4), (2, 2), (2, 5),
                (3, 2), (3, 8), (4, 3), (5, 9), (6, 16)}
    for r in range(1, R_MAX + 1):
        modulus = 1 << r
        for dimension in range(2, D_MAX + 1):
            exponent_jump = floor_log2(dimension)
            period = 1 << (r + exponent_jump)
            for iterate in range(1, 2 * period + 1):
                assert fixed_by_coefficients(modulus, dimension, iterate) == (iterate % period == 0)
                coefficient_cases += 1

            forward, inverse = multiplier_matrices(modulus, dimension)
            reversor = substitution_matrix(modulus, dimension)
            assert matrix_multiply(reversor, reversor, modulus) == identity(dimension + 1)
            assert matrix_multiply(matrix_multiply(reversor, forward, modulus),
                                   reversor, modulus) == inverse
            reversor_matrix_rows += 1

            if modulus ** dimension <= DIRECT_STATE_LIMIT:
                direct_states += direct_period_certificate(modulus, dimension, period)
                direct_rows += 1

            if (r, dimension) in selected:
                witness_iterate = period // 2
                witness_k = 1 << exponent_jump
                witness_value = comb(witness_iterate, witness_k)
                assert witness_value % modulus != 0
                sentinels.append({
                    "r": r,
                    "d": dimension,
                    "q": modulus,
                    "a_floor_log2_d": exponent_jump,
                    "M": period,
                    "state_count": modulus ** dimension,
                    "primitive_cycle_count": modulus ** dimension // period,
                    "half_clock_witness": {
                        "n": witness_iterate,
                        "k": witness_k,
                        "binomial_mod_q": witness_value % modulus,
                    },
                    "coefficient_residues_at_M": [comb(period, k) % modulus
                                                   for k in range(1, dimension + 1)],
                    "fixed_count_at_half_M": 0,
                    "fixed_count_at_M": modulus ** dimension,
                    "fixed_count_at_twice_M": modulus ** dimension,
                    "reversor_matrix_sha256": canonical_hash(reversor),
                })
    return {
        "parameter_rows": R_MAX * (D_MAX - 1),
        "coefficient_clock_cases": coefficient_cases,
        "direct_parameter_rows": direct_rows,
        "direct_state_period_cases": direct_states,
        "reversor_matrix_rows": reversor_matrix_rows,
        "r_max": R_MAX,
        "d_max": D_MAX,
        "direct_state_limit_per_row": DIRECT_STATE_LIMIT,
    }, sentinels


def build_evidence():
    validation, sentinels = build_validation()
    payload = {
        "schema": "hcs-c166-dyadic-pascal-skew-tower-evidence-v1",
        "candidate_id": "HCS-C166",
        "evaluation_date": "2026-08-25",
        "scope_literal": SCOPE,
        "source_commit": SOURCE_COMMIT,
        "source_lock": {
            "object": "T(x_1,...,x_d)=(x_1+x_2,...,x_(d-1)+x_d,x_d+1) on (Z/2^r Z)^d, r>=1 and d>=2",
            "clock": "the exact iterate n>=1 with M=2^(r+floor(log_2 d))",
            "normalization": "unweighted fixed-point count, Artin--Mazur zeta, and finite Koopman determinant",
            "determinant_convention": "det(I-z U_T)=zeta_T(z)^(-1) for the finite Koopman permutation",
            "cutoff": {"all_parameter_theorem": True, "sentinel_r_max": R_MAX,
                       "sentinel_d_max": D_MAX, "direct_state_limit_per_row": DIRECT_STATE_LIMIT},
            "precision": "exact integer, modular, polynomial-ring, and finite-permutation arithmetic",
            "training_data": "none",
            "forbidden_data": "target zero/prime tables, target divisors/counting laws, arithmetic local or Euler data, root numbers, automorphy, Hilbert--Polya, Route B",
        },
        "hard_gate": {
            "required": "a genuinely higher-dimensional all-parameter dynamics theorem rather than another one-dimensional rotation observable",
            "rejected_candidate": "the standalone two-dimensional affine shear",
            "rejection_reason": "its odd-modulus branch is conjugate to a product rotation and its even branch is exactly the d=2 member of the Pascal tower",
            "pivot": "the full dyadic Pascal skew tower for every r>=1 and d>=2",
            "status": "PASS_BY_DIMENSIONAL_MODEL_EXTENSION",
            "complexity_claimed": False,
        },
        "pascal_theorem": {
            "iterate_coefficients": "in augmented polynomial coordinates, T^n multiplies by (1+t)^n, so the kth displacement coefficient is binom(n,k)",
            "fixed_point_criterion": "Fix(T^n) is all q^d states iff q divides binom(n,k) for every 1<=k<=d, and is empty otherwise",
            "clock_formula": "with a=floor(log_2 d), M=2^(r+a), the coefficient criterion holds iff M divides n",
            "sufficiency": "if v_2(n)>=r+a then v_2(binomial(n,k))>=v_2(n)-v_2(k)>=r for every k<=d",
            "necessity": "if q divides n but M does not, write v_2(n)=r+b with 0<=b<a and choose k=2^(b+1)<=d; then v_2(binomial(n,k))=r-1",
            "least_period": "every state has exact least period M",
            "primitive_cycles": "q^d/M",
            "zeta": "zeta_T(z)=(1-z^M)^(-q^d/M)",
            "koopman_determinant": "det(I-z U_T)=(1-z^M)^(q^d/M)",
        },
        "reversor_theorem": {
            "truncated_ring": "R=(Z/qZ)[t]/(t^(d+1)) and p(t)=1+x_d*t+...+x_1*t^d",
            "forward_map": "T is multiplication by 1+t on the affine constant-term-one hyperplane",
            "substitution": "sigma(t)=-t/(1+t)=-t+t^2-...+(-1)^d*t^d",
            "involution": "sigma(sigma(t))=t in the truncated ring",
            "reversal": "sigma composed with multiplication by (1+t) composed with sigma is multiplication by (1+t)^(-1)",
            "antiunitary": "Theta=P_sigma J on ell^2(X) is involutive and Theta U_T Theta^(-1)=U_T^(-1)",
            "finite_dimensional_unitary": True,
            "target_operator_claimed": False,
        },
        "exact_validation": validation,
        "sentinels": sentinels,
        "route_a": {
            "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "claim_boundary": {
            "target_trace_identity": False,
            "target_divisor_matching": False,
            "target_functional_equation": False,
            "target_counting_law": False,
            "arithmetic_local_data": False,
            "euler_factors": False,
            "root_numbers": False,
            "automorphy": False,
            "hilbert_polya_operator": False,
            "cross_candidate_coordinate_combination": False,
        },
    }
    payload["payload_sha256"] = canonical_hash(payload)
    return payload


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path,
                        default=root / "results/c166_pascal_tower_evidence.json")
    args = parser.parse_args()
    payload = build_evidence()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps({"status": "C166_PRODUCER_PASS",
                      "payload_sha256": payload["payload_sha256"],
                      **payload["exact_validation"]}, sort_keys=True))


if __name__ == "__main__":
    main()
