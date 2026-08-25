#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C166."""
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


def payload_hash(data):
    clean = dict(data)
    clean.pop("payload_sha256")
    return sha256(json.dumps(clean, sort_keys=True, separators=(",", ":"),
                             ensure_ascii=False).encode()).hexdigest()


def digest_object(value):
    return sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                             ensure_ascii=False).encode()).hexdigest()


def v2(value):
    exponent = 0
    while value and value % 2 == 0:
        value //= 2
        exponent += 1
    return exponent


def matmul(left, right, modulus):
    size = len(left)
    return [[sum(left[i][k] * right[k][j] for k in range(size)) % modulus
             for j in range(size)] for i in range(size)]


def eye(size):
    return [[int(i == j) for j in range(size)] for i in range(size)]


def closed_reversor(modulus, dimension):
    size = dimension + 1
    matrix = [[0] * size for _ in range(size)]
    matrix[0][0] = 1
    for row in range(1, size):
        for column in range(1, row + 1):
            matrix[row][column] = ((-1) ** row * comb(row - 1, column - 1)) % modulus
    return matrix


def forward_inverse(modulus, dimension):
    size = dimension + 1
    forward = eye(size)
    inverse = eye(size)
    for row in range(1, size):
        forward[row][row - 1] = 1
        for column in range(row):
            inverse[row][column] = (-1) ** (row - column) % modulus
    return forward, inverse


def step(state, modulus):
    out = []
    for left, right in zip(state[:-1], state[1:]):
        out.append((left + right) % modulus)
    out.append((state[-1] + 1) % modulus)
    return tuple(out)


def direct_periods(modulus, dimension, period):
    checked = 0
    for state in product(range(modulus), repeat=dimension):
        current = state
        returned = 0
        for n in range(1, period + 1):
            current = step(current, modulus)
            if current == state:
                returned = n
                break
        assert returned == period
        checked += 1
    return checked


def strict_metadata(data):
    assertions = 0
    assert set(data) == {"schema", "candidate_id", "evaluation_date", "scope_literal",
                         "source_commit", "source_lock", "hard_gate", "pascal_theorem",
                         "reversor_theorem", "exact_validation", "sentinels", "route_a",
                         "claim_boundary", "payload_sha256"}; assertions += 1
    assert set(data["source_lock"]) == {"object", "clock", "normalization",
                                        "determinant_convention", "cutoff", "precision",
                                        "training_data", "forbidden_data"}; assertions += 1
    assert set(data["hard_gate"]) == {"required", "rejected_candidate", "rejection_reason",
                                      "pivot", "status", "complexity_claimed"}; assertions += 1
    assert set(data["pascal_theorem"]) == {"iterate_coefficients", "fixed_point_criterion",
                                           "clock_formula", "sufficiency", "necessity",
                                           "least_period", "primitive_cycles", "zeta",
                                           "koopman_determinant"}; assertions += 1
    assert set(data["reversor_theorem"]) == {"truncated_ring", "forward_map", "substitution",
                                             "involution", "reversal", "antiunitary",
                                             "finite_dimensional_unitary", "target_operator_claimed"}; assertions += 1
    assert set(data["exact_validation"]) == {"parameter_rows", "coefficient_clock_cases",
                                              "direct_parameter_rows", "direct_state_period_cases",
                                              "reversor_matrix_rows", "r_max", "d_max",
                                              "direct_state_limit_per_row"}; assertions += 1
    assert set(data["route_a"]) == {"tuple", "overall", "route_b_invocation_allowed"}; assertions += 1
    assert set(data["claim_boundary"]) == {"target_trace_identity", "target_divisor_matching",
                                            "target_functional_equation", "target_counting_law",
                                            "arithmetic_local_data", "euler_factors", "root_numbers",
                                            "automorphy", "hilbert_polya_operator",
                                            "cross_candidate_coordinate_combination"}; assertions += 1
    assert data["payload_sha256"] == payload_hash(data); assertions += 1
    assert data["schema"] == "hcs-c166-dyadic-pascal-skew-tower-evidence-v1"; assertions += 1
    assert data["candidate_id"] == "HCS-C166"; assertions += 1
    assert data["evaluation_date"] == "2026-08-25"; assertions += 1
    assert data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"; assertions += 1
    assert data["source_commit"] == "4342893ce5e2516924181744bfacc01c12e4959d"; assertions += 1
    assert data["source_lock"] == {
        "object": "T(x_1,...,x_d)=(x_1+x_2,...,x_(d-1)+x_d,x_d+1) on (Z/2^r Z)^d, r>=1 and d>=2",
        "clock": "the exact iterate n>=1 with M=2^(r+floor(log_2 d))",
        "normalization": "unweighted fixed-point count, Artin--Mazur zeta, and finite Koopman determinant",
        "determinant_convention": "det(I-z U_T)=zeta_T(z)^(-1) for the finite Koopman permutation",
        "cutoff": {"all_parameter_theorem": True, "sentinel_r_max": 6,
                   "sentinel_d_max": 16, "direct_state_limit_per_row": 4096},
        "precision": "exact integer, modular, polynomial-ring, and finite-permutation arithmetic",
        "training_data": "none",
        "forbidden_data": "target zero/prime tables, target divisors/counting laws, arithmetic local or Euler data, root numbers, automorphy, Hilbert--Polya, Route B",
    }; assertions += 1
    assert data["hard_gate"] == {
        "required": "a genuinely higher-dimensional all-parameter dynamics theorem rather than another one-dimensional rotation observable",
        "rejected_candidate": "the standalone two-dimensional affine shear",
        "rejection_reason": "its odd-modulus branch is conjugate to a product rotation and its even branch is exactly the d=2 member of the Pascal tower",
        "pivot": "the full dyadic Pascal skew tower for every r>=1 and d>=2",
        "status": "PASS_BY_DIMENSIONAL_MODEL_EXTENSION", "complexity_claimed": False,
    }; assertions += 1
    assert data["pascal_theorem"] == {
        "iterate_coefficients": "in augmented polynomial coordinates, T^n multiplies by (1+t)^n, so the kth displacement coefficient is binom(n,k)",
        "fixed_point_criterion": "Fix(T^n) is all q^d states iff q divides binom(n,k) for every 1<=k<=d, and is empty otherwise",
        "clock_formula": "with a=floor(log_2 d), M=2^(r+a), the coefficient criterion holds iff M divides n",
        "sufficiency": "if v_2(n)>=r+a then v_2(binomial(n,k))>=v_2(n)-v_2(k)>=r for every k<=d",
        "necessity": "if q divides n but M does not, write v_2(n)=r+b with 0<=b<a and choose k=2^(b+1)<=d; then v_2(binomial(n,k))=r-1",
        "least_period": "every state has exact least period M",
        "primitive_cycles": "q^d/M",
        "zeta": "zeta_T(z)=(1-z^M)^(-q^d/M)",
        "koopman_determinant": "det(I-z U_T)=(1-z^M)^(q^d/M)",
    }; assertions += 1
    assert data["reversor_theorem"] == {
        "truncated_ring": "R=(Z/qZ)[t]/(t^(d+1)) and p(t)=1+x_d*t+...+x_1*t^d",
        "forward_map": "T is multiplication by 1+t on the affine constant-term-one hyperplane",
        "substitution": "sigma(t)=-t/(1+t)=-t+t^2-...+(-1)^d*t^d",
        "involution": "sigma(sigma(t))=t in the truncated ring",
        "reversal": "sigma composed with multiplication by (1+t) composed with sigma is multiplication by (1+t)^(-1)",
        "antiunitary": "Theta=P_sigma J on ell^2(X) is involutive and Theta U_T Theta^(-1)=U_T^(-1)",
        "finite_dimensional_unitary": True,
        "target_operator_claimed": False,
    }; assertions += 1
    assert data["exact_validation"] == {
        "parameter_rows": 90, "coefficient_clock_cases": 25200,
        "direct_parameter_rows": 23, "direct_state_period_cases": 27788,
        "reversor_matrix_rows": 90, "r_max": 6, "d_max": 16,
        "direct_state_limit_per_row": 4096,
    }; assertions += 1
    assert data["route_a"] == {"tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL",
                                           "A4_NATURAL_QUANTIZATION"],
                                "overall": "ROUTE_A_EXPLORATORY",
                                "route_b_invocation_allowed": False}; assertions += 3
    assert not any(data["claim_boundary"].values()); assertions += len(data["claim_boundary"])
    return assertions


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path,
                        default=root / "results/c166_pascal_tower_evidence.json")
    parser.add_argument("--mutation-fast", action="store_true")
    args = parser.parse_args()
    data = json.loads(args.evidence.read_text())
    assertions = strict_metadata(data)

    coefficient_cases = 0
    direct_states = 0
    direct_rows = 0
    matrix_rows = 0
    if not args.mutation_fast:
        for r in range(1, R_MAX + 1):
            modulus = 1 << r
            for dimension in range(2, D_MAX + 1):
                a = dimension.bit_length() - 1
                period = 1 << (r + a)
                row = [1] + [0] * dimension
                for n in range(1, 2 * period + 1):
                    for k in range(min(n, dimension), 0, -1):
                        row[k] += row[k - 1]
                    fixed = all(value % modulus == 0 for value in row[1:])
                    assert fixed == (n % period == 0); assertions += 1
                    coefficient_cases += 1
                forward, inverse = forward_inverse(modulus, dimension)
                reversor = closed_reversor(modulus, dimension)
                assert matmul(reversor, reversor, modulus) == eye(dimension + 1); assertions += 1
                assert matmul(matmul(reversor, forward, modulus), reversor, modulus) == inverse; assertions += 1
                matrix_rows += 1
                if modulus ** dimension <= DIRECT_STATE_LIMIT:
                    direct_states += direct_periods(modulus, dimension, period)
                    direct_rows += 1
                    assertions += modulus ** dimension

    validation = data["exact_validation"]
    assert validation["parameter_rows"] == 90; assertions += 1
    assert validation["r_max"] == R_MAX and validation["d_max"] == D_MAX; assertions += 2
    assert validation["direct_state_limit_per_row"] == DIRECT_STATE_LIMIT; assertions += 1
    if not args.mutation_fast:
        assert validation["coefficient_clock_cases"] == coefficient_cases; assertions += 1
        assert validation["direct_parameter_rows"] == direct_rows; assertions += 1
        assert validation["direct_state_period_cases"] == direct_states; assertions += 1
        assert validation["reversor_matrix_rows"] == matrix_rows; assertions += 1

    for item in data["sentinels"]:
        assert set(item) == {"r", "d", "q", "a_floor_log2_d", "M", "state_count",
                             "primitive_cycle_count", "half_clock_witness",
                             "coefficient_residues_at_M", "fixed_count_at_half_M",
                             "fixed_count_at_M", "fixed_count_at_twice_M",
                             "reversor_matrix_sha256"}; assertions += 1
        r, dimension = item["r"], item["d"]
        modulus = 1 << r
        a = dimension.bit_length() - 1
        period = 1 << (r + a)
        assert (item["q"], item["a_floor_log2_d"], item["M"]) == (modulus, a, period); assertions += 3
        assert item["state_count"] == modulus ** dimension; assertions += 1
        assert item["primitive_cycle_count"] == modulus ** dimension // period; assertions += 1
        witness = item["half_clock_witness"]
        assert witness == {"n": period // 2, "k": 1 << a,
                           "binomial_mod_q": comb(period // 2, 1 << a) % modulus}; assertions += 1
        assert witness["binomial_mod_q"] != 0; assertions += 1
        assert v2(comb(witness["n"], witness["k"])) == r - 1; assertions += 1
        assert item["coefficient_residues_at_M"] == [comb(period, k) % modulus
                                                      for k in range(1, dimension + 1)]; assertions += 1
        assert item["fixed_count_at_half_M"] == 0; assertions += 1
        assert item["fixed_count_at_M"] == item["fixed_count_at_twice_M"] == modulus ** dimension; assertions += 2
        assert item["reversor_matrix_sha256"] == digest_object(closed_reversor(modulus, dimension)); assertions += 1

    print(json.dumps({"status": "C166_INDEPENDENT_CHECK_PASS",
                      "assertions": assertions,
                      "coefficient_clock_cases": coefficient_cases,
                      "direct_state_period_cases": direct_states,
                      "reversor_matrix_rows": matrix_rows}, sort_keys=True))


if __name__ == "__main__":
    main()
