#!/usr/bin/env python3
"""Produce the exact HCS-C140 mod-three sofic suspension certificate."""
from __future__ import annotations

import argparse
from hashlib import sha256
import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c140_sofic_evidence.json"
PREFIX = 15
ZERO = (0, 0)


def add(left, right):
    out = dict(left)
    for monomial, coefficient in right.items():
        out[monomial] = out.get(monomial, 0) + coefficient
    return {monomial: coefficient for monomial, coefficient in out.items() if coefficient}


def mul(left, right):
    out = {}
    for first, first_coefficient in left.items():
        for second, second_coefficient in right.items():
            monomial = (first[0] + second[0], first[1] + second[1])
            out[monomial] = out.get(monomial, 0) + first_coefficient * second_coefficient
    return {monomial: coefficient for monomial, coefficient in out.items() if coefficient}


def matrix_multiply(left, right):
    result = [[{} for _ in range(len(right[0]))] for _ in range(len(left))]
    for i in range(len(left)):
        for j in range(len(right[0])):
            value = {}
            for k in range(len(right)):
                value = add(value, mul(left[i][k], right[k][j]))
            result[i][j] = value
    return result


def matrix_power(matrix, exponent):
    identity = [[{ZERO: 1} if i == j else {} for j in range(len(matrix))] for i in range(len(matrix))]
    result = identity
    base = matrix
    while exponent:
        if exponent & 1:
            result = matrix_multiply(result, base)
        base = matrix_multiply(base, base)
        exponent //= 2
    return result


def matrix_trace(matrix):
    value = {}
    for i in range(len(matrix)):
        value = add(value, matrix[i][i])
    return value


def cover_matrix():
    u = {(1, 0): 1}
    v = {(0, 1): 1}
    return [[u, v, {}], [{}, {}, v], [v, {}, {}]]


def admissible(word):
    if 1 not in word:
        return True
    ones = [index for index, symbol in enumerate(word) if symbol == 1]
    n = len(word)
    return all((ones[(k + 1) % len(ones)] - ones[k] - 1) % n % 3 == 0 for k in range(len(ones)))


def primitive(word):
    return not any(len(word) % d == 0 and word == word[:d] * (len(word) // d) for d in range(1, len(word)))


def least_rotation(word):
    return min(word[k:] + word[:k] for k in range(len(word)))


def feature(word):
    return (word.count(1), word.count(0))


def receipt(poly):
    return {f"{monomial[0]},{monomial[1]}": coefficient for monomial, coefficient in sorted(poly.items())}


def payload_bytes(data):
    body = dict(data)
    body.pop("payload_sha256", None)
    return json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def build():
    matrix = cover_matrix()
    rows = []
    rooted_total = primitive_total = rooted_cells_total = primitive_cells_total = 0
    cover_fixed_sequence = []
    label_fixed_sequence = []
    for n in range(1, PREFIX + 1):
        cover_trace = matrix_trace(matrix_power(matrix, n))
        correction = 1 - 3 * int(n % 3 == 0)
        intrinsic = add(cover_trace, {(0, n): correction})
        words = [word for word in itertools.product((0, 1), repeat=n) if admissible(word)]
        histogram = {}
        for word in words:
            vector = feature(word)
            histogram[vector] = histogram.get(vector, 0) + 1
        assert intrinsic == histogram
        representatives = sorted({least_rotation(word) for word in words if primitive(word)})
        groups = {}
        for word in representatives:
            groups.setdefault(feature(word), []).append("".join(map(str, word)))
        rows.append({
            "period": n,
            "cover_fixed_points": sum(cover_trace.values()),
            "label_fixed_points": len(words),
            "all_zero_correction_coefficient": correction,
            "cover_weighted_trace_coefficients": receipt(cover_trace),
            "intrinsic_weighted_fixed_coefficients": receipt(intrinsic),
            "rooted_feature_cells": len(histogram),
            "primitive_label_cycles": len(representatives),
            "primitive_feature_cells": len(groups),
            "primitive_representatives": ["".join(map(str, word)) for word in representatives],
            "same_feature_primitive_groups": {
                f"{vector[0]},{vector[1]}": members
                for vector, members in sorted(groups.items()) if len(members) > 1
            },
        })
        cover_fixed_sequence.append(sum(cover_trace.values()))
        label_fixed_sequence.append(len(words))
        rooted_total += len(words)
        primitive_total += len(representatives)
        rooted_cells_total += len(histogram)
        primitive_cells_total += len(groups)
    assert cover_fixed_sequence == [1, 1, 4, 5, 6, 10, 15, 21, 31, 46, 67, 98, 144, 211, 309]
    assert label_fixed_sequence == [2, 2, 2, 6, 7, 8, 16, 22, 29, 47, 68, 96, 145, 212, 307]
    assert (rooted_total, primitive_total, rooted_cells_total, primitive_cells_total) == (969, 74, 60, 32)

    data = {
        "schema": "HCS-C140-v1",
        "candidate_id": "HCS-C140",
        "date_utc": "2026-08-25",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "source_lock": {
            "object": "the binary mod-three gap shift X3: every finite zero run between consecutive ones has length in 3*Z_ge_0, with the all-zero point included",
            "presentation": "right-resolving residue graph 0--1-->0, 0--0-->1, 1--0-->2, 2--0-->0",
            "roof": {"label_1": "1", "label_0": "sqrt(2)"},
            "clock": "continuous label-roof suspension time ell=N1+sqrt(2)*N0",
            "normalization": "each intrinsic label periodic point is counted once; the all-zero point is not counted with cover multiplicity",
            "determinant_convention": "D_cov=det(I-B); D_140=Z_140^(-1) is the intrinsic label inverse zeta after the exceptional-orbit correction",
            "precision": "exact integer label-count vectors (N1,N0) and exact rational formal functions in (u,v)",
            "cutoff": "none in theorem; periods 1 through 15 are replay sentinels only",
            "forbidden_data": "external prime or zero tables, arithmetic/local factors, root numbers, automorphy claims, and Route-B inputs",
        },
        "frozen_model": {
            "states": [0, 1, 2],
            "labeled_transitions": [[0, 0, "1"], [0, 1, "0"], [1, 2, "0"], [2, 0, "0"]],
            "cover_matrix": [["u", "v", "0"], ["0", "0", "v"], ["v", "0", "0"]],
            "cover_determinant": "D_cov(u,v)=1-u-v^3",
            "cover_zeta": "Z_cov(u,v)=1/(1-u-v^3)",
            "intrinsic_zeta": "Z_140(u,v)=(1+v+v^2)/(1-u-v^3)",
            "intrinsic_inverse_zeta": "D_140(u,v)=(1-u-v^3)/(1+v+v^2)=D_cov(u,v)*(1-v)/(1-v^3)",
            "laplace_specialization": "u=z*exp(-s), v=z*exp(-sqrt(2)*s)",
            "entropy_characterization": "h is the unique positive solution 1-exp(-h)-exp(-3*sqrt(2)*h)=0",
        },
        "sofic_theorem": {
            "strictly_sofic": "X3 is not an SFT: for every local memory L a periodic gap 3m+1>2L is globally forbidden although each of its length-(L+1) blocks occurs in X3",
            "three_follower_sets": "residue states 0,1,2 have distinct futures; respectively the shortest next-one words are 1,001,01",
            "minimal_cover": "the displayed follower-separated right-resolving three-state graph is the minimal right Fischer cover",
            "unique_lift_off_exception": "every bi-infinite label sequence containing a 1 has a unique cover lift",
            "exceptional_point": "the all-zero label fixed point has three cover lifts forming one cover orbit of least period three",
        },
        "all_period_identity": {
            "weighted_fixed_formula": "F_n(u,v)=Tr(B(u,v)^n)+(1-3*1_[3|n])*v^n for every n>=1",
            "correction_log": "sum_(n>=1)(1-3*1_[3|n])*v^n/n=log(1+v+v^2)",
            "log_zeta": "log Z_140=sum_(n>=1)F_n(u,v)/n=-log(1-u-v^3)+log(1+v+v^2)",
            "primitive_product": "D_140(u,v)=product_[gamma primitive label orbit](1-u^N1(gamma)*v^N0(gamma))",
            "suspension_product": "D_140(z,s)=product_[gamma primitive label orbit](1-z^|gamma|*exp(-s*ell(gamma)))",
            "convergence": "formal in total label degree; absolutely after specialization in any domain where the corresponding fixed-point logarithmic series converges",
            "all_period": True,
            "replay_cutoff_is_not_theorem_cutoff": True,
        },
        "controls": {
            "cover_fixed_counts_periods_1_to_15": cover_fixed_sequence,
            "label_fixed_counts_periods_1_to_15": label_fixed_sequence,
            "period_1_cover_to_label_correction": 1,
            "period_3_cover_to_label_correction": -2,
            "all_zero_label_point_least_period": 1,
            "all_zero_cover_orbit_least_period": 3,
            "nonlattice_witness": "label fixed cycles [1] and [0] have suspension lengths 1 and sqrt(2)",
            "no_imaginary_period": "at fixed z=1, the two fixed label cycles force exp(-iT)=exp(-iT*sqrt(2))=1, hence T=0",
        },
        "replay_prefix": {
            "period_limit": PREFIX,
            "rows": rows,
            "admissible_rooted_points_total": rooted_total,
            "primitive_label_cycles_total": primitive_total,
            "rooted_feature_cells_total": rooted_cells_total,
            "primitive_feature_cells_total": primitive_cells_total,
        },
        "progress_and_boundary": {
            "progress_over_full_shift_suspensions": "moves Route A to a strictly sofic source and proves the exact finite-to-one exceptional-orbit correction from its minimal three-state cover",
            "remaining_internal_obstruction": "the intrinsic inverse zeta is a rational correction rather than the determinant of a separately constructed natural Fredholm operator on label space",
            "target_obstruction": "no target divisor, functional equation, counting law, arithmetic interpretation, or natural operator lift is compared",
        },
        "route_a": {
            "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "overall": "ROUTE_A_EXPLORATORY",
            "A1_qualification": "ALL_PERIOD_INTRINSIC_PRIMITIVE_ORBITS_OF_A_STRICTLY_SOFIC_SUSPENSION_WITHOUT_A_PRIME_LIKE_TARGET_MAP",
            "A2_qualification": "EXACT_INTRINSIC_RATIONAL_ZETA_AND_COVER_CORRECTION_WITHOUT_A_FROZEN_TARGET_DIVISOR_MATCH",
            "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_GAMMA_FACTOR_COUNTING_LAW_OR_CONTINUATION_COMPARISON",
            "A4_qualification": "NO_NATURAL_SELF_ADJOINT_UNITARY_SCATTERING_OR_HAMILTONIAN_LIFT",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": {
            "scope": "NO_BAD_EULER_OR_ROOT_NUMBER",
            "uses_prime_table": False,
            "uses_zero_table": False,
            "claims_arithmetic_euler_factors": False,
            "claims_root_number": False,
            "claims_automorphy": False,
            "claims_hilbert_polya": False,
            "uses_route_b_inputs": False,
        },
        "nonclaims": [
            "that the three-state cover trace already equals the intrinsic label fixed-point trace",
            "a natural Fredholm determinant owner for the corrected rational inverse zeta",
            "an arithmetic Euler product or local factorization",
            "a target zero or pole divisor match, functional equation, or counting law",
            "a natural self-adjoint Hilbert--Polya operator",
            "Route-B authorization or a solution of the larger program",
        ],
    }
    data["payload_sha256"] = sha256(payload_bytes(data)).hexdigest()
    return data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    arguments = parser.parse_args()
    data = build()
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C140_PRODUCER_PASS",
        "output": str(arguments.output),
        "payload_sha256": data["payload_sha256"],
        "admissible_rooted_points": data["replay_prefix"]["admissible_rooted_points_total"],
        "primitive_label_cycles": data["replay_prefix"]["primitive_label_cycles_total"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
