#!/usr/bin/env python3
"""Produce the exact HCS-C29 symmetric-groupoid certificate.

The producer source-locks C25, C26, and C28, constructs formal inverse darts,
and preserves later-on-the-left chronology.  It does not identify an inverse
dart with an antiparallel positive Rauzy arrow.  All arithmetic is exact and
uses only the Python standard library.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Iterable


PROJECT = Path(__file__).resolve().parents[1]
HENON_ROOT = PROJECT.parent
REPO_ROOT = HENON_ROOT.parent
PRODUCER_PATH = Path(__file__).resolve()
DEFAULT_OUTPUT = PROJECT / "results" / "c29_certificate.json"

SOURCE_PATHS = {
    "C25_certificate": HENON_ROOT
    / "agy_metaplectic_transfer_obstruction"
    / "results"
    / "c25_certificate.json",
    "C25_theorem": HENON_ROOT / "agy_metaplectic_transfer_obstruction" / "THEOREM_PACKAGE.md",
    "C26_certificate": HENON_ROOT
    / "agy_holomorphic_slice_obstruction"
    / "results"
    / "c26_certificate.json",
    "C26_theorem": HENON_ROOT / "agy_holomorphic_slice_obstruction" / "THEOREM_PACKAGE.md",
    "C28_certificate": HENON_ROOT
    / "agy_prime_direct_sum_determinant"
    / "results"
    / "c28_certificate.json",
    "C28_theorem": HENON_ROOT / "agy_prime_direct_sum_determinant" / "THEOREM_PACKAGE.md",
}

EXPECTED_SOURCE_HASHES = {
    "C25_certificate": "a35cee22714abbb9dc9aadcc165720d1ff77aff3b7f29071f53a1b451760bd12",
    "C25_theorem": "e1835d63bef914b355ceb4f64acc9043d11a842e9f4e59c7573c63ff66d03702",
    "C26_certificate": "1c0289b9b47e65e0603ea001be7cce263aea13d58c66e4609eac88edf8f7ce4a",
    "C26_theorem": "4e882cbc332711b4cd2f98e9530f89268c8fcf1712eb150aacfee968dcf50495",
    "C28_certificate": "98b9ed10433f5cc7eb56aa04f397caa1ebfbc03acc904552618bd06f30370a1e",
    "C28_theorem": "3de68629b3c59c958683d79d96fc90fde901efd878896d192595370d02df8a4c",
}

C1 = ["0t", "1b", "0t^-1", "0b", "3t", "0b^-1"]
C2 = ["4t", "6b^-1", "6t", "5b", "6t^-1", "6b"]
EXPECTED_C26_HOLONOMY_WORD = [
    "A^-1",
    "C",
    "B^-1",
    "C",
    "A^-1",
    "A^-1",
    "B",
    "A^-1",
    "A^-1",
    "C",
    "B^-1",
    "A",
    "A",
    "C^-1",
    "B",
    "C^-1",
    "A",
    "A",
    "B^-1",
    "A",
    "A",
    "C^-1",
    "B",
    "A^-1",
]


Matrix = list[list[int]]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_sha256(value: object) -> str:
    encoded = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def eye(n: int = 4) -> Matrix:
    return [[int(i == j) for j in range(n)] for i in range(n)]


def transpose(a: Matrix) -> Matrix:
    return [list(row) for row in zip(*a)]


def matmul(a: Matrix, b: Matrix) -> Matrix:
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def matsub(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def outer(column: list[int], row: list[int]) -> Matrix:
    return [[column[i] * row[j] for j in range(len(row))] for i in range(len(column))]


def dot(a: list[int], b: list[int]) -> int:
    return sum(a[index] * b[index] for index in range(len(a)))


def matpow(a: Matrix, exponent: int) -> Matrix:
    if exponent < 0:
        return matpow(inverse_unimodular(a), -exponent)
    result = eye(len(a))
    base = a
    power = exponent
    while power:
        if power & 1:
            result = matmul(result, base)
        base = matmul(base, base)
        power //= 2
    return result


def inverse_unimodular(a: Matrix) -> Matrix:
    n = len(a)
    augmented = [
        [Fraction(value) for value in a[i]]
        + [Fraction(int(i == j)) for j in range(n)]
        for i in range(n)
    ]
    for column in range(n):
        pivot = next((row for row in range(column, n) if augmented[row][column]), None)
        if pivot is None:
            raise AssertionError("singular matrix")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        value = augmented[column][column]
        augmented[column] = [entry / value for entry in augmented[column]]
        for row in range(n):
            if row == column:
                continue
            factor = augmented[row][column]
            if factor:
                augmented[row] = [
                    augmented[row][j] - factor * augmented[column][j]
                    for j in range(2 * n)
                ]
    right = [row[n:] for row in augmented]
    if any(value.denominator != 1 for row in right for value in row):
        raise AssertionError("matrix inverse is not integral")
    return [[int(value) for value in row] for row in right]


def matrix_product_left(word: Iterable[str], arrows: dict[str, dict[str, object]]) -> Matrix:
    product = eye()
    for token in word:
        product = matmul(arrows[token]["matrix"], product)
    return product


def matrix_product_written(word: Iterable[str], matrices: dict[str, Matrix]) -> Matrix:
    product = eye()
    for token in word:
        base = token.removesuffix("^-1")
        factor = matrices[base]
        if token.endswith("^-1"):
            factor = inverse_unimodular(factor)
        product = matmul(product, factor)
    return product


def matrix_product_chronological_symbols(
    path_order_word: Iterable[str], matrices: dict[str, Matrix]
) -> Matrix:
    product = eye()
    for token in path_order_word:
        base = token.removesuffix("^-1")
        factor = matrices[base]
        if token.endswith("^-1"):
            factor = inverse_unimodular(factor)
        product = matmul(factor, product)
    return product


def inverse_word(word: tuple[str, ...] | list[str], bars: dict[str, str]) -> tuple[str, ...]:
    return tuple(bars[token] for token in reversed(word))


def bar_symbol(token: str) -> str:
    return token.removesuffix("^-1") if token.endswith("^-1") else token + "^-1"


def inverse_symbol_word(word: Iterable[str]) -> list[str]:
    return [bar_symbol(token) for token in reversed(list(word))]


def free_reduce(word: Iterable[str]) -> list[str]:
    stack: list[str] = []
    for token in word:
        if stack and token == bar_symbol(stack[-1]):
            stack.pop()
        else:
            stack.append(token)
    return stack


def substitute_and_reduce(word: Iterable[str], substitutions: dict[str, list[str]]) -> list[str]:
    expanded: list[str] = []
    for token in word:
        base = token.removesuffix("^-1")
        replacement = substitutions[base]
        expanded.extend(inverse_symbol_word(replacement) if token.endswith("^-1") else replacement)
    return free_reduce(expanded)


def rotations(word: tuple[str, ...]) -> list[tuple[str, ...]]:
    return [word[index:] + word[:index] for index in range(len(word))]


def is_primitive_word(word: tuple[str, ...] | list[str]) -> bool:
    tokens = tuple(word)
    for period in range(1, len(tokens)):
        if len(tokens) % period == 0 and tokens == tokens[:period] * (len(tokens) // period):
            return False
    return True


def is_linearly_reduced(word: tuple[str, ...] | list[str], bars: dict[str, str]) -> bool:
    return all(word[index + 1] != bars[word[index]] for index in range(len(word) - 1))


def is_cyclically_reduced(word: tuple[str, ...] | list[str], bars: dict[str, str]) -> bool:
    return bool(word) and is_linearly_reduced(word, bars) and word[0] != bars[word[-1]]


def state_path(word: list[str], arrows: dict[str, dict[str, object]]) -> list[int]:
    states = [int(arrows[word[0]]["source"])]
    for index, token in enumerate(word):
        arrow = arrows[token]
        if states[-1] != int(arrow["source"]):
            raise AssertionError(f"state discontinuity at {index}: {token}")
        states.append(int(arrow["target"]))
    return states


def source_lock() -> tuple[
    dict[str, object], dict[str, object], dict[str, object], dict[str, object]
]:
    observed = {name: sha256(path) for name, path in SOURCE_PATHS.items()}
    if observed != EXPECTED_SOURCE_HASHES:
        raise AssertionError(f"source lock changed: {observed}")
    c25 = json.loads(SOURCE_PATHS["C25_certificate"].read_text(encoding="utf-8"))
    c26 = json.loads(SOURCE_PATHS["C26_certificate"].read_text(encoding="utf-8"))
    c28 = json.loads(SOURCE_PATHS["C28_certificate"].read_text(encoding="utf-8"))
    record = {
        "files": {
            name: {
                "path": str(path.relative_to(REPO_ROOT)),
                "sha256": observed[name],
            }
            for name, path in SOURCE_PATHS.items()
        },
        "chronology_id": "LATER_ON_LEFT_EXACT",
        "prime_scope": "odd primes only; fixed path length before the prime limit",
        "forbidden_data": "no prime table, Riemann-zero table, fitted clock, or averaged chronology",
    }
    return c25, c26, c28, record


def build_c25_arrows(c25: dict[str, object]) -> tuple[dict[str, dict[str, object]], dict[str, str]]:
    arrows: dict[str, dict[str, object]] = {}
    bars: dict[str, str] = {}
    frozen = c25["statewise_symplectic_trivialization"]["fixed_fiber_edges"]
    for row in frozen:
        token = f"{int(row['source'])}{row['type']}"
        inverse_token = f"{token}^-1"
        matrix = [[int(value) for value in values] for values in row["g_edge_equals_S_target_inverse_B_edge_S_source"]]
        source = int(row["source"])
        target = int(row["target"])
        arrows[token] = {
            "positive_edge_id": token,
            "orientation": 1,
            "source": source,
            "target": target,
            "matrix": matrix,
        }
        arrows[inverse_token] = {
            "positive_edge_id": token,
            "orientation": -1,
            "source": target,
            "target": source,
            "matrix": inverse_unimodular(matrix),
        }
        bars[token] = inverse_token
        bars[inverse_token] = token
    if len(arrows) != 28 or len(bars) != 28:
        raise AssertionError("C25 symmetric dart count changed")
    return arrows, bars


def witness_record(
    name: str,
    word: list[str],
    expected_states: list[int],
    arrows: dict[str, dict[str, object]],
    bars: dict[str, str],
) -> dict[str, object]:
    states = state_path(word, arrows)
    closed = states[0] == states[-1]
    product = matrix_product_left(word, arrows)
    token_tuple = tuple(word)
    record = {
        "id": name,
        "tokens_path_order": word,
        "states": states,
        "length": len(word),
        "closed": closed,
        "linear_nonbacktracking": is_linearly_reduced(word, bars),
        "cyclic_nonbacktracking": is_cyclically_reduced(word, bars),
        "primitive": is_primitive_word(word),
        "distinct_rotations": len(set(rotations(token_tuple))),
        "inverse_is_rotation": inverse_word(word, bars) in rotations(token_tuple),
        "chronological_holonomy": product,
        "identity_holonomy": product == eye(),
    }
    if states != expected_states or not all(
        [
            closed,
            record["linear_nonbacktracking"],
            record["cyclic_nonbacktracking"],
            record["primitive"],
            not record["inverse_is_rotation"],
            record["identity_holonomy"],
        ]
    ):
        raise AssertionError(f"{name} witness failed: {record}")
    return record


def c25_census(
    arrows: dict[str, dict[str, object]], bars: dict[str, str], max_length: int = 9
) -> dict[str, object]:
    outgoing: dict[int, list[str]] = defaultdict(list)
    for token, arrow in arrows.items():
        outgoing[int(arrow["source"])].append(token)
    for values in outgoing.values():
        values.sort()
    degree = {str(vertex): len(values) for vertex, values in sorted(outgoing.items())}
    if set(degree.values()) != {4}:
        raise AssertionError(f"unexpected symmetric degree: {degree}")
    successor_counts = {
        token: len(
            [candidate for candidate in outgoing[int(arrow["target"])] if candidate != bars[token]]
        )
        for token, arrow in arrows.items()
    }
    predecessor_counts = {
        token: sum(
            int(arrow["target"]) == int(arrows[token]["source"]) and token != bars[prior]
            for prior, arrow in arrows.items()
        )
        for token in arrows
    }
    if set(successor_counts.values()) != {3} or set(predecessor_counts.values()) != {3}:
        raise AssertionError("C25 Hashimoto transition degree changed")

    all_marked: list[int] = []
    primitive_marked: list[int] = []
    all_rotation_count: list[int] = []
    primitive_rotation_count: list[int] = []
    all_dihedral_count: list[int] = []
    primitive_dihedral_count: list[int] = []
    primitive_self_inverse_count: list[int] = []

    for length in range(1, max_length + 1):
        identities: list[tuple[str, ...]] = []

        def extend(first: str, word: tuple[str, ...], product: Matrix) -> None:
            if len(word) == length:
                if (
                    int(arrows[word[-1]]["target"]) == int(arrows[first]["source"])
                    and first != bars[word[-1]]
                    and product == eye()
                ):
                    identities.append(word)
                return
            vertex = int(arrows[word[-1]]["target"])
            for token in outgoing[vertex]:
                if token == bars[word[-1]]:
                    continue
                extend(token if not word else first, word + (token,), matmul(arrows[token]["matrix"], product))

        for first in sorted(arrows):
            extend(first, (first,), arrows[first]["matrix"])

        primitive_identities = [word for word in identities if is_primitive_word(word)]
        all_rotation_classes = {min(rotations(word)) for word in identities}
        primitive_rotation_classes = {min(rotations(word)) for word in primitive_identities}
        all_dihedral_classes = {
            min(min(rotations(word)), min(rotations(inverse_word(word, bars)))) for word in identities
        }
        primitive_dihedral_classes = {
            min(min(rotations(word)), min(rotations(inverse_word(word, bars))))
            for word in primitive_identities
        }
        primitive_self_inverse = {
            min(rotations(word))
            for word in primitive_identities
            if inverse_word(word, bars) in rotations(word)
        }
        all_marked.append(len(identities))
        primitive_marked.append(len(primitive_identities))
        all_rotation_count.append(len(all_rotation_classes))
        primitive_rotation_count.append(len(primitive_rotation_classes))
        all_dihedral_count.append(len(all_dihedral_classes))
        primitive_dihedral_count.append(len(primitive_dihedral_classes))
        primitive_self_inverse_count.append(len(primitive_self_inverse))

    expected = {
        "all_marked_identity": [0, 0, 0, 0, 0, 24, 0, 32, 144],
        "primitive_marked_identity": [0, 0, 0, 0, 0, 24, 0, 32, 144],
        "all_oriented_rotation_classes": [0, 0, 0, 0, 0, 4, 0, 4, 16],
        "primitive_oriented_rotation_classes": [0, 0, 0, 0, 0, 4, 0, 4, 16],
        "all_dihedral_classes": [0, 0, 0, 0, 0, 2, 0, 2, 8],
        "primitive_dihedral_classes": [0, 0, 0, 0, 0, 2, 0, 2, 8],
        "primitive_self_inverse_rotation_classes": [0, 0, 0, 0, 0, 0, 0, 0, 0],
    }
    observed = {
        "all_marked_identity": all_marked,
        "primitive_marked_identity": primitive_marked,
        "all_oriented_rotation_classes": all_rotation_count,
        "primitive_oriented_rotation_classes": primitive_rotation_count,
        "all_dihedral_classes": all_dihedral_count,
        "primitive_dihedral_classes": primitive_dihedral_count,
        "primitive_self_inverse_rotation_classes": primitive_self_inverse_count,
    }
    if observed != expected:
        raise AssertionError(f"C25 census changed: {observed}")
    return {
        "lengths": list(range(1, max_length + 1)),
        **observed,
        "determinant_moments_use": "all_marked_identity",
        "primitive_filter_is_not_used_for_N_n": True,
        "oriented_outdegree": degree,
        "hashimoto_successor_degree": sorted(set(successor_counts.values())),
        "hashimoto_predecessor_degree": sorted(set(predecessor_counts.values())),
        "hashimoto_row_and_column_degree": max(successor_counts.values()),
        "unitary_block_operator_norm_bound": max(successor_counts.values()),
        "exact_N6": 24,
        "exact_log_coefficient_u6": {"numerator": -4, "denominator": 1},
        "scope": "bounded exact regression census; nonconstancy is already proved by explicit witnesses",
    }


def gauge_control(
    c25: dict[str, object], arrows: dict[str, dict[str, object]], bars: dict[str, str]
) -> dict[str, object]:
    j0 = [[int(value) for value in row] for row in c25["statewise_symplectic_trivialization"]["base_form_J0"]]
    generator = arrows["3t"]["matrix"]
    if matmul(matmul(transpose(generator), j0), generator) != j0:
        raise AssertionError("gauge generator is not symplectic")
    gauges = {vertex: matpow(generator, vertex) for vertex in range(7)}
    gauge_symplectic = {
        str(vertex): matmul(matmul(transpose(matrix), j0), matrix) == j0
        for vertex, matrix in gauges.items()
    }
    if not all(gauge_symplectic.values()):
        raise AssertionError("a gauge matrix left the frozen symplectic form")
    transformed: dict[str, dict[str, object]] = {}
    for token, arrow in arrows.items():
        source = int(arrow["source"])
        target = int(arrow["target"])
        transformed[token] = {
            **arrow,
            "matrix": matmul(
                matmul(inverse_unimodular(gauges[target]), arrow["matrix"]), gauges[source]
            ),
        }
    formal_inverse_compatibility = all(
        transformed[bars[token]]["matrix"] == inverse_unimodular(transformed[token]["matrix"])
        for token in arrows
    )
    checks = {}
    for name, word in {"C1": C1, "C2": C2}.items():
        base = int(arrows[word[0]]["source"])
        original = matrix_product_left(word, arrows)
        transformed_product = matrix_product_left(word, transformed)
        expected = matmul(matmul(inverse_unimodular(gauges[base]), original), gauges[base])
        checks[name] = transformed_product == expected == eye()
    if not all(checks.values()):
        raise AssertionError(f"gauge control failed: {checks}")
    nonidentity_loop = ["4t"]
    base = int(arrows[nonidentity_loop[0]]["source"])
    original_nonidentity = matrix_product_left(nonidentity_loop, arrows)
    transformed_nonidentity = matrix_product_left(nonidentity_loop, transformed)
    nonidentity_conjugacy = (
        original_nonidentity != eye()
        and transformed_nonidentity
        == matmul(
            matmul(inverse_unimodular(gauges[base]), original_nonidentity), gauges[base]
        )
    )
    if not formal_inverse_compatibility or not nonidentity_conjugacy:
        raise AssertionError("gauge inverse/nonidentity control failed")
    return {
        "gauge_family": "h_v=(g_3t)^v, v=0,...,6",
        "source_derived_symplectic": True,
        "arrow_rule": "g'_e=h_target^-1*g_e*h_source",
        "closed_path_rule": "g'_C=h_base^-1*g_C*h_base",
        "all_h_v_preserve_J0": gauge_symplectic,
        "formal_inverse_compatibility": formal_inverse_compatibility,
        "identity_verdicts_preserved": checks,
        "nonidentity_closed_loop": "4t",
        "nonidentity_conjugacy_verified": nonidentity_conjugacy,
    }


def identity_repetition_record(
    arrows: dict[str, dict[str, object]], bars: dict[str, str]
) -> dict[str, object]:
    word = C1 + C1
    states = state_path(word, arrows)
    record = {
        "word": word,
        "length": len(word),
        "closed": states[0] == states[-1],
        "cyclic_nonbacktracking": is_cyclically_reduced(word, bars),
        "identity_holonomy": matrix_product_left(word, arrows) == eye(),
        "primitive": is_primitive_word(word),
        "enters_all_cycle_moment": True,
        "enters_primitive_census": False,
    }
    if not all(
        [
            record["closed"],
            record["cyclic_nonbacktracking"],
            record["identity_holonomy"],
            not record["primitive"],
        ]
    ):
        raise AssertionError(f"C1 repetition control failed: {record}")
    return record


def c26_record(c26: dict[str, object]) -> tuple[dict[str, object], dict[str, object]]:
    source = c26["source_locked_branch"]
    two = c26["scalar_periodic_trace_gate"]["chronological_two_return_witness"]
    three = c26["scalar_periodic_trace_gate"]["three_return_spectral_chronology_witness"]
    a = [[int(value) for value in row] for row in source["chronological_matrix_B"]]
    h = [[int(value) for value in row] for row in two["return_bridge_chronological_matrix_B"]]
    k = [[int(value) for value in row] for row in three["third_return_bridge_chronological_matrix_B"]]
    b = [[int(value) for value in row] for row in two["second_branch_chronological_matrix_B"]]
    c = [[int(value) for value in row] for row in three["third_branch_chronological_matrix_B"]]
    y = matmul(matmul(inverse_unimodular(h), k), h)
    delta_left = matmul(matmul(k, y), k)
    delta_right = matmul(matmul(y, k), y)
    matrices = {"A": a, "B": b, "C": c, "H": h, "K": k, "Y": y, "Delta": delta_left}
    factorization = b == matmul(matmul(a, h), a) and c == matmul(matmul(a, k), a)
    braid = delta_left == delta_right
    contractions = {
        "phiT_v": dot([1, 0, 0, 0], [0, 1, 1, 1]),
        "psiT_w": dot([1, 0, 0, 1], [-1, 1, 0, 1]),
        "phiT_w": dot([1, 0, 0, 0], [-1, 1, 0, 1]),
        "psiT_v": dot([1, 0, 0, 1], [0, 1, 1, 1]),
    }
    rank_one_checks = {
        "K_minus_I_equals_v_phiT": matsub(k, eye())
        == outer([0, 1, 1, 1], [1, 0, 0, 0]),
        "Y_minus_I_equals_w_psiT": matsub(y, eye())
        == outer([-1, 1, 0, 1], [1, 0, 0, 1]),
        "contractions_exact": contractions
        == {"phiT_v": 0, "psiT_w": 0, "phiT_w": -1, "psiT_v": 1},
    }
    exact_order_four = (
        delta_left != eye()
        and matpow(delta_left, 2) != eye()
        and matpow(delta_left, 4) == eye()
    )
    y_word = ["H^-1", "K", "H"]
    lhs_word = ["K", *y_word, "K"]
    rhs_word = [*y_word, "K", *y_word]
    hk_relation = free_reduce([*lhs_word, *inverse_symbol_word(rhs_word)])
    if len(hk_relation) != 12 or matrix_product_written(hk_relation, matrices) != eye():
        raise AssertionError("derived H,K braid relation failed")
    substitutions = {
        "H": ["A^-1", "B", "A^-1"],
        "K": ["A^-1", "C", "A^-1"],
    }
    derived_word = substitute_and_reduce(hk_relation, substitutions)
    if derived_word != EXPECTED_C26_HOLONOMY_WORD:
        raise AssertionError(f"derived C26 word changed: {derived_word}")
    path_order_word = list(reversed(derived_word))
    product = matrix_product_written(derived_word, matrices)
    path_product = matrix_product_chronological_symbols(path_order_word, matrices)
    bars = {
        token: (token.removesuffix("^-1") if token.endswith("^-1") else token + "^-1")
        for token in {"A", "A^-1", "B", "B^-1", "C", "C^-1"}
    }
    rose_symbols = sorted(bars)
    successor_counts = {
        token: len([candidate for candidate in rose_symbols if candidate != bars[token]])
        for token in rose_symbols
    }
    predecessor_counts = {
        token: len([prior for prior in rose_symbols if token != bars[prior]])
        for token in rose_symbols
    }
    if set(successor_counts.values()) != {5} or set(predecessor_counts.values()) != {5}:
        raise AssertionError("C26 rose Hashimoto degree changed")
    word_tuple = tuple(derived_word)
    word_checks = {
        "length": len(word_tuple),
        "linear_reduced": is_linearly_reduced(word_tuple, bars),
        "cyclically_reduced": is_cyclically_reduced(word_tuple, bars),
        "primitive": is_primitive_word(word_tuple),
        "distinct_rotations": len(set(rotations(word_tuple))),
        "inverse_is_rotation": inverse_word(word_tuple, bars) in rotations(word_tuple),
        "identity_product": product == eye(),
        "path_order_later_on_left_identity_product": path_product == eye(),
    }
    if not factorization or not braid or not all(rank_one_checks.values()) or not exact_order_four or not all(
        [
            word_checks["linear_reduced"],
            word_checks["cyclically_reduced"],
            word_checks["primitive"],
            word_checks["distinct_rotations"] == 24,
            not word_checks["inverse_is_rotation"],
            word_checks["identity_product"],
            word_checks["path_order_later_on_left_identity_product"],
        ]
    ):
        raise AssertionError("C26 exact relation failed")
    compact_hashes = {name: canonical_sha256(matrix) for name, matrix in matrices.items()}
    expected_hashes = {
        "A": "ab5d6fcbe0634cfcc7e9421314b8e80a2c82c7c9d01d51ba7dd7d1819ef0dfc4",
        "H": "8944734d9a6c4b0ba92fe3997bdca1dcf3a3243ddb80c612ab1de405ef5f4c81",
        "K": "f8fb365915111b6008aea42788276daab72d9d73bd28f466b5328d73e00fd782",
        "B": "e02c1f63a18cbb348a9daaed46996bf8e90f3f2056429109ff8312efdf1235c0",
        "C": "2821bf61e845923ede59b4f3a567ccb4735a239490bd5cefa8de0077777b8da5",
        "Y": "9b7919cd3235561829635b408df197543428dd3ccfc7ec9ed197156e377a8e05",
        "Delta": "487e65563ee01025dd9aef40b20ca7e854f669305353173e99298b76be5b73a2",
    }
    if compact_hashes != expected_hashes:
        raise AssertionError(f"C26 compact matrix sentinel changed: {compact_hashes}")
    record = {
        "elementary_words": {
            "A_gamma_star": source["gamma_star_compressed"],
            "A_length": int(source["gamma_star_length"]),
            "H_bridge": str(two["return_bridge_word"]),
            "H_length": len(str(two["return_bridge_word"])),
            "K_bridge": str(three["third_return_bridge_word"]),
            "K_length": len(str(three["third_return_bridge_word"])),
            "B_branch_length": len(str(two["second_branch_word"])),
            "C_branch_length": len(str(three["third_branch_word"])),
        },
        "matrices": matrices,
        "producer_regression_matrix_sha256": compact_hashes,
        "matrix_hash_role": "producer regression sentinels; not independent checker evidence",
        "factorization": {"B_equals_AHA": b == matmul(matmul(a, h), a), "C_equals_AKA": c == matmul(matmul(a, k), a)},
        "rank_one_braid": {
            "Y_definition": "H^-1*K*H",
            **rank_one_checks,
            "contractions": contractions,
            "KYK_equals_YKY": braid,
            "common_matrix": delta_left,
        },
        "word_derivation": {
            "Y_word": y_word,
            "KYK_word": lhs_word,
            "YKY_word": rhs_word,
            "free_reduced_HK_relation": hk_relation,
            "substitutions": substitutions,
            "derived_not_postulated": True,
        },
        "holonomy_order_word": derived_word,
        "later_on_left_path_order_word": path_order_word,
        "word_checks": word_checks,
        "marked_identity_lower_bound_N24": 48,
        "N24_C26_is_exact_total": False,
        "oriented_symbols": len(rose_symbols),
        "legal_successors_per_symbol": sorted(set(successor_counts.values())),
        "legal_predecessors_per_symbol": sorted(set(predecessor_counts.values())),
        "hashimoto_degree": max(successor_counts.values()),
        "unitary_block_operator_norm_bound": max(successor_counts.values()),
        "log_coefficient_u24_bound": "-N24/24 <= -2",
    }
    repetition = {
        "torsion_repetition": {
            "holonomy_name": "Delta=K*Y*K",
            "Delta_not_identity": delta_left != eye(),
            "Delta_squared_not_identity": matpow(delta_left, 2) != eye(),
            "Delta_fourth_power_identity": matpow(delta_left, 4) == eye(),
            "repetition_law": "THETA_OF_HOLONOMY_POWER_NOT_POWER_OF_CHARACTER",
            "correct_character_atom": "Theta_p(Delta^4)",
            "forbidden_replacement": "Theta_p(Delta)^4",
        },
    }
    return record, repetition


def build_payload() -> dict[str, object]:
    c25, c26, c28, locked = source_lock()
    arrows, bars = build_c25_arrows(c25)
    positive_arrows = [arrow for arrow in arrows.values() if int(arrow["orientation"]) == 1]
    observed_states = {
        int(endpoint)
        for arrow in positive_arrows
        for endpoint in (arrow["source"], arrow["target"])
    }
    identity_positive = sum(arrow["matrix"] == eye() for arrow in positive_arrows)
    if len(observed_states) != 7 or len(positive_arrows) != 14 or identity_positive != 6:
        raise AssertionError("C25 graph/fixed-frame count changed")
    witness_1 = witness_record("C1", C1, [0, 1, 1, 0, 3, 3, 0], arrows, bars)
    witness_2 = witness_record("C2", C2, [4, 4, 6, 5, 5, 6, 4], arrows, bars)
    if arrows["0b^-1"]["positive_edge_id"] != "0b" or arrows["0b^-1"]["matrix"] == arrows["3b"]["matrix"]:
        raise AssertionError("formal inverse/opposite-arrow sentinel failed")
    c1_tuple = tuple(C1)
    c2_tuple = tuple(C2)
    c1_dihedral = min(min(rotations(c1_tuple)), min(rotations(inverse_word(c1_tuple, bars))))
    c2_dihedral = min(min(rotations(c2_tuple)), min(rotations(inverse_word(c2_tuple, bars))))
    distinct_dihedral = c1_dihedral != c2_dihedral
    proof_lower_bound_n6 = sum(
        2 * int(record["distinct_rotations"])
        for record in (witness_1, witness_2)
        if not bool(record["inverse_is_rotation"])
    )
    if not distinct_dihedral or proof_lower_bound_n6 != 24:
        raise AssertionError("C25 proof-level marked lower bound failed")
    formal_backtracking_pairs = 0
    for token in sorted(arrows):
        pair = [token, bars[token]]
        states = state_path(pair, arrows)
        if states[0] == states[-1] and matrix_product_left(pair, arrows) == eye():
            formal_backtracking_pairs += 1
    if formal_backtracking_pairs != 28:
        raise AssertionError("formal backtracking-pair control failed")
    census = c25_census(arrows, bars)
    branch, repetition = c26_record(c26)
    repetition["identity_repetition"] = identity_repetition_record(arrows, bars)
    c28_limit = c28["normalized_character_limit_theorem"]
    return {
        "candidate_id": "HCS-C29",
        "candidate_name": "symmetric non-backtracking C26 return-matrix groupoid",
        "verification": {
            "status": "PRODUCER_ONLY_UNVERIFIED_UNTIL_INDEPENDENT_CHECKER",
            "independent_checker_required": True,
            "checker_must_not_import_producer": True,
        },
        "material_passport": {
            "schema": 9,
            "data_class": "frozen repository exact-integer artifacts",
            "analysis": "source-locked theorem-driven exact computation",
            "human_subjects": False,
            "AI_assistance_disclosure_required": True,
        },
        "source_lock": locked,
        "conventions": {
            "chronology_id": "LATER_ON_LEFT_EXACT",
            "formal_inverse_id": "SAME_LABELED_EDGE_FORMAL_INVERSE_EXACT",
            "inverse_word_id": "REVERSE_ORDER_THEN_FLIP_ORIENTATION",
            "formal_inverse_is_opposite_positive_arrow": False,
            "nonbacktracking": "forbid e followed by formal bar(e), including cyclic closure",
            "unit_marks": True,
        },
        "c25_graph_reconstruction": {
            "states": len(observed_states),
            "positive_arrows": len(positive_arrows),
            "oriented_darts": len(arrows),
            "base_state": int(c25["statewise_symplectic_trivialization"]["base_state"]),
            "identity_fixed_frame_edges": identity_positive,
            "nonidentity_fixed_frame_edges": len(positive_arrows) - identity_positive,
            "formal_inverse_opposite_arrow_sentinel": {
                "formal_inverse": "0b^-1",
                "positive_edge_id_retained": "0b",
                "antiparallel_positive_arrow": "3b",
                "matrices_are_distinct": arrows["0b^-1"]["matrix"] != arrows["3b"]["matrix"],
            },
            "formal_backtracking_pair_identities": formal_backtracking_pairs,
            "formal_backtracking_pair_scope": "the 28 marked pairs e*bar(e), not an unrestricted length-two census",
        },
        "c25_identity_witnesses": {
            "C1": witness_1,
            "C2": witness_2,
            "distinct_dihedral_classes": distinct_dihedral,
            "proof_level_marked_lower_bound_N6": proof_lower_bound_n6,
        },
        "c25_gauge_control": gauge_control(c25, arrows, bars),
        "c25_identity_census": census,
        "c26_branch_relation": branch,
        "repetition_controls": repetition,
        "natural_extension_control": {
            "result": "POSITIVE_PERIODIC_PRODUCT_GERM_ONE",
            "basis": "C25 all-length fixed-start positive-monoid freeness",
            "forward_products_unchanged_by_natural_extension": True,
            "two_sided_transfer_operator_constructed": False,
            "symmetric_object_scope": "NEW_SYMMETRIC_DYNAMICS_NOT_NATURAL_EXTENSION",
        },
        "finite_weil_limit": {
            "upstream_status": c28_limit["status"],
            "formula": "p^(-2)*Theta_p(g) -> 1 if g=I and 0 otherwise",
            "odd_primes_only": True,
            "fixed_length_before_prime_limit": True,
            "infinite_path_sum_interchange_claimed": False,
            "repetition_law": "THETA_OF_HOLONOMY_POWER_NOT_POWER_OF_CHARACTER",
        },
        "normalized_determinant_germ": {
            "normalization_id": "EXP_P_MINUS_2_LOG0_FINITE_DETERMINANT",
            "finite_prime_object": "exp[p^(-2) Log_0 det(I-u*B_p)]",
            "Log_0_definition": "unique analytic logarithm with Log_0 det(I)=0",
            "limit": "exp[-sum_(n>=1) N_n*u^n/n]",
            "N_n_definition": "all marked cyclically nonbacktracking closed paths with identity holonomy",
            "C25_norm_bound": 3,
            "C26_norm_bound": 5,
            "common_strict_disc": "|u|<1/5",
            "zero_free_reason": "norm(u*B_p)<1 on the strict common disc",
            "uniform_trace_majorant": "p^(-2)*abs(Tr(B_p^n)) <= |E|*M^n",
            "locally_uniform_on_smaller_discs": True,
            "C25_nonconstant": True,
            "C26_nonconstant": True,
            "ordinary_infinite_dimensional_Fredholm_claimed": False,
            "positive_Fuglede_Kadison_claimed": False,
            "finite_order_primitive_factor": {
                "z_P": "u^ell(P)*product_(e in P) x_e",
                "holonomy_order_m_factor": "(1-z_P^m)^(1/m)",
                "global_Euler_product_claimed": False,
            },
        },
        "scope_decisions": {
            "algebraic_reopening": "PASS_EXACT",
            "genuine_natural_extension_escape": "FAIL_GERM_EQUALS_ONE",
            "intrinsic_inverse_AGY_roof_constructed": False,
            "inverse_branches_use_C26_Bergman_nuclearity": False,
            "two_sided_trace_theorem": "OPEN",
            "geometric_orbit_interpretation": "OPEN",
            "route_A_promotion": "STOP_BEFORE_INTRINSIC_ROOF_AND_TWO_SIDED_TRACE_THEOREM",
            "route_B_authorized": False,
            "xi_divisor_or_RH_claimed": False,
            "next_big_gate": "derive an intrinsic positive reversible roof and a two-sided trace theorem, otherwise pivot system",
        },
        "runtime": {
            "producer_sha256": sha256(PRODUCER_PATH),
            "arithmetic": "Python integers and fractions; no floating point",
            "environment_fields_in_canonical_payload": False,
        },
    }


def run(output: Path | None = None) -> dict[str, object]:
    payload = build_payload()
    certificate = {
        "schema": "HCS-C29-EXACT-CERTIFICATE-v1",
        "payload": payload,
        "payload_sha256": canonical_sha256(payload),
    }
    if output is not None:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return certificate


def main() -> None:
    args = parse_args()
    report = run(args.output)
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
