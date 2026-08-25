#!/usr/bin/env python3
"""Produce the exact HCS-C139 four-block marker suspension certificate."""
from __future__ import annotations

import argparse
from hashlib import sha256
import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c139_marker_evidence.json"
PREFIX = 12
STATES = tuple(itertools.product((0, 1), repeat=3))
STATE_INDEX = {state: index for index, state in enumerate(STATES)}
ZERO = (0, 0, 0, 0, 0)


def add(left, right):
    out = dict(left)
    for monomial, coefficient in right.items():
        out[monomial] = out.get(monomial, 0) + coefficient
    return {monomial: coefficient for monomial, coefficient in out.items() if coefficient}


def mul(left, right):
    out = {}
    for first, first_coefficient in left.items():
        for second, second_coefficient in right.items():
            monomial = tuple(a + b for a, b in zip(first, second))
            out[monomial] = out.get(monomial, 0) + first_coefficient * second_coefficient
    return {monomial: coefficient for monomial, coefficient in out.items() if coefficient}


def monomial(index, coefficient=1):
    exponent = [0, 0, 0, 0, 0]
    exponent[index] = 1
    return {tuple(exponent): coefficient}


def permutation_sign(permutation):
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(len(permutation))
        for j in range(i + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def formal_matrix():
    matrix = [[{} for _ in STATES] for _ in STATES]
    for source in STATES:
        a, b, c = source
        for d in (0, 1):
            target = (b, c, d)
            exponent = [0, 0, 0, 0, 0]
            exponent[2 * a + b] = 1
            exponent[4] = int((a, b, c, d) == (0, 0, 1, 1))
            matrix[STATE_INDEX[source]][STATE_INDEX[target]] = {tuple(exponent): 1}
    return matrix


def determinant_i_minus(matrix):
    size = len(matrix)
    shifted = [[dict(matrix[i][j]) for j in range(size)] for i in range(size)]
    for i in range(size):
        shifted[i][i] = add({ZERO: 1}, {m: -c for m, c in shifted[i][i].items()})
        for j in range(size):
            if i != j:
                shifted[i][j] = {m: -c for m, c in shifted[i][j].items()}
    total = {}
    for permutation in itertools.permutations(range(size)):
        term = {ZERO: permutation_sign(permutation)}
        for row, column in enumerate(permutation):
            if not shifted[row][column]:
                term = {}
                break
            term = mul(term, shifted[row][column])
        total = add(total, term)
    return total


def primitive(word):
    n = len(word)
    return not any(n % d == 0 and word == word[:d] * (n // d) for d in range(1, n))


def least_rotation(word):
    return min(word[k:] + word[:k] for k in range(len(word)))


def rotations(word):
    return [word[k:] + word[:k] for k in range(len(word))]


def block_counts(word, width):
    n = len(word)
    counts = [0] * (2 ** width)
    for start in range(n):
        index = 0
        for offset in range(width):
            index = 2 * index + word[(start + offset) % n]
        counts[index] += 1
    return tuple(counts)


def feature(word):
    edges = block_counts(word, 2)
    marker = block_counts(word, 4)[3]
    return edges + (marker,)


def feature_receipt(values):
    return ",".join(map(str, values))


def word_receipt(word):
    return {
        "word": "".join(map(str, word)),
        "primitive": primitive(word),
        "canonical_rotation": "".join(map(str, least_rotation(word))),
        "symbol_counts_0_1": list(block_counts(word, 1)),
        "edge_counts_00_01_10_11": list(block_counts(word, 2)),
        "trigram_counts_000_to_111": list(block_counts(word, 3)),
        "marker_count_0011": block_counts(word, 4)[3],
        "clock_basis_coefficients_1_sqrt2_sqrt3_sqrt6_sqrt5": list(feature(word)),
    }


def trace_histogram_from_states(n):
    total = {}
    transitions = []
    for source in STATES:
        a, b, c = source
        rows = []
        for d in (0, 1):
            exponent = [0, 0, 0, 0, 0]
            exponent[2 * a + b] = 1
            exponent[4] = int((a, b, c, d) == (0, 0, 1, 1))
            rows.append((STATE_INDEX[(b, c, d)], tuple(exponent)))
        transitions.append(rows)
    for start in range(len(STATES)):
        active = {(start, ZERO): 1}
        for _ in range(n):
            following = {}
            for (state, exponent), coefficient in active.items():
                for target, increment in transitions[state]:
                    combined = tuple(a + b for a, b in zip(exponent, increment))
                    key = (target, combined)
                    following[key] = following.get(key, 0) + coefficient
            active = following
        for (state, exponent), coefficient in active.items():
            if state == start:
                total[exponent] = total.get(exponent, 0) + coefficient
    return total


def payload_bytes(data):
    body = dict(data)
    body.pop("payload_sha256", None)
    return json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def build():
    determinant = determinant_i_minus(formal_matrix())
    expected_determinant = {
        ZERO: 1,
        (1, 0, 0, 0, 0): -1,
        (0, 0, 0, 1, 0): -1,
        (0, 1, 1, 0, 0): -1,
        (1, 0, 0, 1, 0): 1,
        (1, 1, 1, 1, 0): 1,
        (1, 1, 1, 1, 1): -1,
    }
    assert determinant == expected_determinant

    rows = []
    rooted_total = primitive_total = rooted_cells_total = primitive_cells_total = 0
    first_collision_period = None
    for n in range(1, PREFIX + 1):
        rooted = list(itertools.product((0, 1), repeat=n))
        rooted_histogram = {}
        for word in rooted:
            vector = feature(word)
            rooted_histogram[vector] = rooted_histogram.get(vector, 0) + 1
        assert rooted_histogram == trace_histogram_from_states(n)
        representatives = sorted({least_rotation(word) for word in rooted if primitive(word)})
        primitive_groups = {}
        for word in representatives:
            primitive_groups.setdefault(feature(word), []).append("".join(map(str, word)))
        collisions = {
            feature_receipt(vector): words
            for vector, words in sorted(primitive_groups.items())
            if len(words) > 1
        }
        if collisions and first_collision_period is None:
            first_collision_period = n
        rows.append({
            "period": n,
            "rooted_closed_words": len(rooted),
            "primitive_cycles": len(representatives),
            "feature_histogram_cells": len(rooted_histogram),
            "primitive_feature_cells": len(primitive_groups),
            "weighted_trace_coefficients": {
                feature_receipt(vector): coefficient
                for vector, coefficient in sorted(rooted_histogram.items())
            },
            "primitive_representatives": ["".join(map(str, word)) for word in representatives],
            "same_feature_primitive_groups": collisions,
        })
        rooted_total += len(rooted)
        primitive_total += len(representatives)
        rooted_cells_total += len(rooted_histogram)
        primitive_cells_total += len(primitive_groups)

    minimal_a = tuple(map(int, "001011"))
    minimal_b = tuple(map(int, "001101"))
    residual_a = tuple(map(int, "0101111"))
    residual_b = tuple(map(int, "0110111"))
    assert block_counts(minimal_a, 1) == block_counts(minimal_b, 1) == (3, 3)
    assert block_counts(minimal_a, 2) == block_counts(minimal_b, 2) == (1, 2, 2, 1)
    assert block_counts(minimal_a, 3) == block_counts(minimal_b, 3) == (0, 1, 1, 1, 1, 1, 1, 0)
    assert feature(minimal_a) == (1, 2, 2, 1, 0)
    assert feature(minimal_b) == (1, 2, 2, 1, 1)
    assert feature(residual_a) == feature(residual_b) == (0, 2, 2, 3, 0)
    assert residual_b not in rotations(residual_a)
    assert first_collision_period == 7
    assert (rooted_total, primitive_total, rooted_cells_total, primitive_cells_total) == (8190, 747, 258, 229)

    data = {
        "schema": "HCS-C139-v1",
        "candidate_id": "HCS-C139",
        "date_utc": "2026-08-25",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "source_lock": {
            "object": "two-sided full binary shift with the four-block marker roof r_eta(x)=tau_(x0,x1)+sqrt(5)*1_[x0x1x2x3=0011]",
            "base_edge_roof": [["1", "sqrt(2)"], ["sqrt(3)", "sqrt(6)"]],
            "marker": "0011",
            "eta": "sqrt(5)",
            "clock": "continuous suspension time, retaining the literal edge counts and cyclic 0011 count",
            "normalization": "one base transition per shift step; forward four-block occurrence counted at its initial coordinate",
            "determinant_convention": "Delta_139(x,y)=det(I-M_139(x,y)); zeta_139=1/Delta_139 after Laplace specialization",
            "precision": "exact integer vectors in the ordered basis (1,sqrt(2),sqrt(3),sqrt(6),sqrt(5))",
            "cutoff": "none in theorem; periods 1 through 12 are replay sentinels only",
            "forbidden_data": "external prime or zero tables, arithmetic/local factors, root numbers, automorphy claims, and Route-B inputs",
        },
        "frozen_model": {
            "states": ["".join(map(str, state)) for state in STATES],
            "transition_rule": "abc -> bcd has weight x_ab*y^(1_[abcd=0011]) for d in {0,1}",
            "formal_determinant": "Delta_139=1-x00-x11-x01*x10+x00*x11+(1-y)*x00*x01*x10*x11",
            "formal_determinant_receipt": {
                feature_receipt(vector): coefficient for vector, coefficient in sorted(determinant.items())
            },
            "edge_roof_specialization": "x_ab=z*exp(-s*tau_ab), y=exp(-sqrt(5)*s)",
            "clock_formula": "ell=N00+sqrt(2)N01+sqrt(3)N10+sqrt(6)N11+sqrt(5)N0011",
            "basis_independence": "1,sqrt(2),sqrt(3),sqrt(6),sqrt(5) are Q-linearly independent",
            "y_equals_one_reduction": "Delta_139(x,1)=1-x00-x11-x01*x10+x00*x11, the C135 edge determinant",
        },
        "all_period_identity": {
            "trace_formula": "Tr(M_139(x,y)^n)=sum_(rooted binary w,|w|=n) y^N0011(w)*product_ab x_ab^Nab(w)",
            "log_determinant": "-log Delta_139=sum_(n>=1) Tr(M_139^n)/n",
            "primitive_product": "Delta_139=product_[gamma primitive](1-y^N0011(gamma)*product_ab x_ab^Nab(gamma))",
            "suspension_product": "Delta_139(z,s)=product_[gamma primitive](1-z^|gamma|*exp(-s*ell(gamma)))",
            "convergence": "formal in total transition degree; absolutely after specialization whenever the nonnegative weighted matrix has spectral radius below one",
            "all_period": True,
            "replay_cutoff_is_not_theorem_cutoff": True,
        },
        "minimal_memory_theorem": {
            "statement": "the displayed period-six pair has equal cyclic k-block populations for k=1,2,3 but different cyclic 0011 counts, so no forward locally constant roof of memory at most three separates it while the frozen four-block roof does",
            "pair": ["001011", "001101"],
            "common_1_block_counts": [3, 3],
            "common_2_block_counts": [1, 2, 2, 1],
            "common_3_block_counts": [0, 1, 1, 1, 1, 1, 1, 0],
            "marker_counts": [0, 1],
            "clock_difference_second_minus_first": "sqrt(5)",
            "coding_boundary": "minimal memory is relative to the frozen forward binary coding and is not asserted cohomology invariant",
        },
        "controls": {
            "minimal_pair_receipts": [word_receipt(minimal_a), word_receipt(minimal_b)],
            "residual_collision_pair": ["0101111", "0110111"],
            "residual_pair_receipts": [word_receipt(residual_a), word_receipt(residual_b)],
            "residual_feature_vector": [0, 2, 2, 3, 0],
            "residual_pair_nonrotation": True,
            "first_same_feature_primitive_collision_period": first_collision_period,
            "nonlattice_witness": "fixed cycles [0] and [1] have lengths 1 and sqrt(6)",
            "no_imaginary_period": "at fixed z=1, an imaginary period would make both exp(-iT)=1 and exp(-iT*sqrt(6))=1, hence T=0",
        },
        "replay_prefix": {
            "period_limit": PREFIX,
            "rows": rows,
            "rooted_closed_words_total": rooted_total,
            "primitive_cycles_total": primitive_total,
            "rooted_feature_cells_total": rooted_cells_total,
            "primitive_feature_cells_total": primitive_cells_total,
        },
        "progress_and_boundary": {
            "progress_over_C135": "adds the smallest displayed forward four-block marker that separates a primitive pair indistinguishable by every one-, two-, and three-block population",
            "remaining_internal_obstruction": "distinct primitive period-seven necklaces still share the complete frozen five-component clock vector",
            "target_obstruction": "no target divisor, functional equation, counting law, arithmetic interpretation, or natural operator lift is compared",
        },
        "route_a": {
            "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "overall": "ROUTE_A_EXPLORATORY",
            "A1_qualification": "ALL_PERIOD_INTRINSIC_PRIMITIVE_SUSPENSION_ORBITS_WITH_A_STRICTLY_FINER_FROZEN_CLOCK_BUT_NO_PRIME_LIKE_TARGET_MAP",
            "A2_qualification": "EXACT_SOURCE_DETERMINANT_AND_PRIMITIVE_PRODUCT_WITHOUT_A_FROZEN_TARGET_DIVISOR_MATCH",
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
            "coding-independent or cohomology-invariant minimal memory",
            "primitive-orbit injectivity after adding the 0011 marker",
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
        "status": "C139_PRODUCER_PASS",
        "output": str(arguments.output),
        "payload_sha256": data["payload_sha256"],
        "rooted_words": data["replay_prefix"]["rooted_closed_words_total"],
        "primitive_cycles": data["replay_prefix"]["primitive_cycles_total"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
