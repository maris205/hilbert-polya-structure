#!/usr/bin/env python3
"""Independent exact checker for the HCS-C29 Phase-2 certificate.

This program deliberately does not import ``c29_producer`` or any C29 helper.
It rebuilds the Rauzy graph, state frames, formal inverse darts, exact identity
cycles, bounded census, C26 branch matrices, braid relation, and semantic
firewalls using a separate standard-library implementation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import deque
from fractions import Fraction
from pathlib import Path
from typing import Callable, Iterable, TypeVar


PROJECT = Path(__file__).resolve().parents[1]
HENON_ROOT = PROJECT.parent
REPO_ROOT = HENON_ROOT.parent
DEFAULT_CERTIFICATE = PROJECT / "results" / "c29_certificate.json"
DEFAULT_OUTPUT = PROJECT / "results" / "c29_independent_check.json"
PRODUCER_PATH = PROJECT / "code" / "c29_producer.py"

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

ALPHABET = (1, 2, 3, 4)
MOVE_TYPES = ("t", "b")
INITIAL = ((1, 2, 3, 4), (4, 3, 2, 1))
AGY_BASE = ((1, 3, 4, 2), (4, 3, 2, 1))
EXPECTED_STATES = (
    ((1, 2, 3, 4), (4, 1, 3, 2)),
    ((1, 2, 3, 4), (4, 2, 1, 3)),
    ((1, 2, 3, 4), (4, 3, 2, 1)),
    ((1, 2, 4, 3), (4, 1, 3, 2)),
    ((1, 3, 4, 2), (4, 3, 2, 1)),
    ((1, 4, 2, 3), (4, 3, 1, 2)),
    ((1, 4, 2, 3), (4, 3, 2, 1)),
)
EXPECTED_TARGETS = {
    "0t": 1,
    "0b": 3,
    "1t": 2,
    "1b": 1,
    "2t": 0,
    "2b": 6,
    "3t": 3,
    "3b": 0,
    "4t": 4,
    "4b": 2,
    "5t": 6,
    "5b": 5,
    "6t": 5,
    "6b": 4,
}

C1 = ("0t", "1b", "0t^-1", "0b", "3t", "0b^-1")
C2 = ("4t", "6b^-1", "6t", "5b", "6t^-1", "6b")
C1_STATES = [0, 1, 1, 0, 3, 3, 0]
C2_STATES = [4, 4, 6, 5, 5, 6, 4]

GAMMA_STAR = "t" * 64 + "tbttbtbb" * 8
H_BRIDGE = "bttbtbb"
K_BRIDGE = "bbb"
C26_HOLONOMY_WORD = (
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
)

EXPECTED_MATRIX_HASHES = {
    "A": "ab5d6fcbe0634cfcc7e9421314b8e80a2c82c7c9d01d51ba7dd7d1819ef0dfc4",
    "H": "8944734d9a6c4b0ba92fe3997bdca1dcf3a3243ddb80c612ab1de405ef5f4c81",
    "K": "f8fb365915111b6008aea42788276daab72d9d73bd28f466b5328d73e00fd782",
    "B": "e02c1f63a18cbb348a9daaed46996bf8e90f3f2056429109ff8312efdf1235c0",
    "C": "2821bf61e845923ede59b4f3a567ccb4735a239490bd5cefa8de0077777b8da5",
    "Y": "9b7919cd3235561829635b408df197543428dd3ccfc7ec9ed197156e377a8e05",
    "Delta": "487e65563ee01025dd9aef40b20ca7e854f669305353173e99298b76be5b73a2",
}

EXPECTED_CENSUS = {
    "all_marked_identity": [0, 0, 0, 0, 0, 24, 0, 32, 144],
    "primitive_marked_identity": [0, 0, 0, 0, 0, 24, 0, 32, 144],
    "all_oriented_rotation_classes": [0, 0, 0, 0, 0, 4, 0, 4, 16],
    "primitive_oriented_rotation_classes": [0, 0, 0, 0, 0, 4, 0, 4, 16],
    "all_dihedral_classes": [0, 0, 0, 0, 0, 2, 0, 2, 8],
    "primitive_dihedral_classes": [0, 0, 0, 0, 0, 2, 0, 2, 8],
    "primitive_self_inverse_rotation_classes": [0, 0, 0, 0, 0, 0, 0, 0, 0],
}

Permutation = tuple[tuple[int, ...], tuple[int, ...]]
Matrix = tuple[tuple[int, ...], ...]
T = TypeVar("T")


class GateFailure(AssertionError):
    """A fail-closed independent-check gate failed."""


class Audit:
    def __init__(self) -> None:
        self.gates: dict[str, str] = {}
        self.details: dict[str, object] = {}

    def gate(self, name: str, function: Callable[[], T]) -> T:
        try:
            value = function()
        except Exception as exc:
            self.gates[name] = "FAIL"
            self.details[name] = {"error": f"{type(exc).__name__}: {exc}"}
            setattr(exc, "audit_gates", sorted_gate_map(self.gates))
            setattr(
                exc,
                "audit_details",
                {gate: self.details[gate] for gate in sorted_gate_map(self.gates)},
            )
            raise
        self.gates[name] = "PASS"
        self.details[name] = value if isinstance(value, dict) else {"result": value}
        return value


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path, default=DEFAULT_CERTIFICATE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_sha256(value: object) -> str:
    data = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def expect(condition: bool, message: str) -> None:
    if not condition:
        raise GateFailure(message)


def type_strict_equal(observed: object, expected: object) -> bool:
    """Compare reconstructed data without JSON bool/int/float ambiguity."""

    if type(observed) is not type(expected):
        return False
    if isinstance(expected, dict):
        return (
            set(observed) == set(expected)  # type: ignore[arg-type]
            and all(
                type_strict_equal(observed[key], value)  # type: ignore[index]
                for key, value in expected.items()
            )
        )
    if isinstance(expected, (list, tuple)):
        return len(observed) == len(expected) and all(  # type: ignore[arg-type]
            type_strict_equal(left, right)
            for left, right in zip(observed, expected)  # type: ignore[arg-type]
        )
    return observed == expected


def expect_equal(observed: object, expected: object, label: str) -> None:
    if not type_strict_equal(observed, expected):
        observed_text = repr(observed)
        expected_text = repr(expected)
        if len(observed_text) > 600:
            observed_text = observed_text[:597] + "..."
        if len(expected_text) > 600:
            expected_text = expected_text[:597] + "..."
        raise GateFailure(f"{label}: observed {observed_text}, expected {expected_text}")


def as_matrix(value: object) -> Matrix:
    expect(isinstance(value, list), "matrix is not a list")
    rows = value
    expect(len(rows) == 4 and all(isinstance(row, list) and len(row) == 4 for row in rows), "matrix is not 4x4")
    return tuple(tuple(int(entry) for entry in row) for row in rows)


def matrix_json(matrix: Matrix) -> list[list[int]]:
    return [list(row) for row in matrix]


def eye(n: int = 4) -> Matrix:
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))


def transpose(matrix: Matrix) -> Matrix:
    return tuple(tuple(matrix[j][i] for j in range(len(matrix))) for i in range(len(matrix[0])))


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0])))
        for i in range(len(left))
    )


def matpow(matrix: Matrix, exponent: int) -> Matrix:
    if exponent < 0:
        return matpow(inverse_unimodular(matrix), -exponent)
    result = eye(len(matrix))
    base = matrix
    power = exponent
    while power:
        if power & 1:
            result = matmul(result, base)
        base = matmul(base, base)
        power //= 2
    return result


def inverse_unimodular(matrix: Matrix) -> Matrix:
    n = len(matrix)
    augmented = [
        [Fraction(matrix[i][j]) for j in range(n)]
        + [Fraction(int(i == j)) for j in range(n)]
        for i in range(n)
    ]
    for column in range(n):
        pivot = next((row for row in range(column, n) if augmented[row][column]), None)
        expect(pivot is not None, "singular matrix")
        assert pivot is not None
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        divisor = augmented[column][column]
        augmented[column] = [entry / divisor for entry in augmented[column]]
        for row in range(n):
            if row == column:
                continue
            factor = augmented[row][column]
            if factor:
                augmented[row] = [
                    augmented[row][index] - factor * augmented[column][index]
                    for index in range(2 * n)
                ]
    right = [row[n:] for row in augmented]
    expect(all(entry.denominator == 1 for row in right for entry in row), "inverse is not integral")
    return tuple(tuple(int(entry) for entry in row) for row in right)


def outer(column: tuple[int, ...], row: tuple[int, ...]) -> Matrix:
    return tuple(tuple(column[i] * row[j] for j in range(len(row))) for i in range(len(column)))


def matrix_add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(tuple(left[i][j] + right[i][j] for j in range(len(left[i]))) for i in range(len(left)))


def bar_token(token: str) -> str:
    return token.removesuffix("^-1") if token.endswith("^-1") else token + "^-1"


def inverse_word(word: tuple[str, ...] | list[str]) -> tuple[str, ...]:
    return tuple(bar_token(token) for token in reversed(word))


def free_reduce(word: Iterable[str]) -> tuple[str, ...]:
    stack: list[str] = []
    for token in word:
        if stack and token == bar_token(stack[-1]):
            stack.pop()
        else:
            stack.append(token)
    return tuple(stack)


def substitute_and_reduce(
    word: Iterable[str], substitutions: dict[str, tuple[str, ...]]
) -> tuple[str, ...]:
    expanded: list[str] = []
    for token in word:
        base = token.removesuffix("^-1")
        replacement = substitutions[base]
        expanded.extend(inverse_word(replacement) if token.endswith("^-1") else replacement)
    return free_reduce(expanded)


def rotations(word: tuple[str, ...]) -> list[tuple[str, ...]]:
    return [word[index:] + word[:index] for index in range(len(word))]


def primitive(word: tuple[str, ...] | list[str]) -> bool:
    tokens = tuple(word)
    return not any(
        len(tokens) % period == 0 and tokens == tokens[:period] * (len(tokens) // period)
        for period in range(1, len(tokens))
    )


def linearly_reduced(word: tuple[str, ...] | list[str]) -> bool:
    return all(word[index + 1] != bar_token(word[index]) for index in range(len(word) - 1))


def cyclically_reduced(word: tuple[str, ...] | list[str]) -> bool:
    return bool(word) and linearly_reduced(word) and word[0] != bar_token(word[-1])


def product_path_order(word: Iterable[str], darts: dict[str, dict[str, object]]) -> Matrix:
    product = eye()
    for token in word:
        product = matmul(darts[token]["matrix"], product)  # type: ignore[arg-type]
    return product


def product_written_order(word: Iterable[str], matrices: dict[str, Matrix]) -> Matrix:
    product = eye()
    for token in word:
        base = token.removesuffix("^-1")
        factor = matrices[base]
        if token.endswith("^-1"):
            factor = inverse_unimodular(factor)
        product = matmul(product, factor)
    return product


def elementary_matrix(winner: int, loser: int) -> Matrix:
    result = [list(row) for row in eye()]
    result[loser - 1][winner - 1] += 1
    return tuple(tuple(row) for row in result)


def crossing_form(permutation: Permutation) -> Matrix:
    top, bottom = permutation
    top_position = {letter: index for index, letter in enumerate(top)}
    bottom_position = {letter: index for index, letter in enumerate(bottom)}
    result = [[0] * 4 for _ in range(4)]
    for alpha in ALPHABET:
        for beta in ALPHABET:
            if top_position[alpha] < top_position[beta] and bottom_position[alpha] > bottom_position[beta]:
                result[alpha - 1][beta - 1] = 1
            elif top_position[alpha] > top_position[beta] and bottom_position[alpha] < bottom_position[beta]:
                result[alpha - 1][beta - 1] = -1
    return tuple(tuple(row) for row in result)


def rauzy_move(permutation: Permutation, move_type: str) -> tuple[Permutation, int, int, Matrix]:
    top, bottom = [list(row) for row in permutation]
    if move_type == "t":
        winner, loser = top[-1], bottom[-1]
        bottom.remove(loser)
        bottom.insert(bottom.index(winner) + 1, loser)
    elif move_type == "b":
        winner, loser = bottom[-1], top[-1]
        top.remove(loser)
        top.insert(top.index(winner) + 1, loser)
    else:
        raise GateFailure(f"unknown Rauzy move {move_type}")
    return (tuple(top), tuple(bottom)), winner, loser, elementary_matrix(winner, loser)


def reconstruct_graph() -> tuple[tuple[Permutation, ...], dict[str, dict[str, object]]]:
    discovered = {INITIAL}
    pending: deque[Permutation] = deque([INITIAL])
    while pending:
        source = pending.popleft()
        for move_type in MOVE_TYPES:
            target, _, _, _ = rauzy_move(source, move_type)
            if target not in discovered:
                discovered.add(target)
                pending.append(target)
    states = tuple(sorted(discovered))
    expect_equal(states, EXPECTED_STATES, "sorted Rauzy states")
    state_id = {state: index for index, state in enumerate(states)}
    edges: dict[str, dict[str, object]] = {}
    for source_id, source in enumerate(states):
        for move_type in MOVE_TYPES:
            target, winner, loser, matrix = rauzy_move(source, move_type)
            target_id = state_id[target]
            token = f"{source_id}{move_type}"
            expect_equal(target_id, EXPECTED_TARGETS[token], f"target of {token}")
            expect_equal(
                matmul(matmul(matrix, crossing_form(source)), transpose(matrix)),
                crossing_form(target),
                f"crossing-form transport for {token}",
            )
            edges[token] = {
                "source": source_id,
                "target": target_id,
                "type": move_type,
                "winner": winner,
                "loser": loser,
                "matrix": matrix,
            }
    expect_equal((len(states), len(edges)), (7, 14), "graph size")
    expect_equal(states.index(INITIAL), 2, "central state")
    expect_equal(states.index(AGY_BASE), 4, "AGY base state")
    return states, edges


def reconstruct_frames(
    states: tuple[Permutation, ...], edges: dict[str, dict[str, object]]
) -> tuple[dict[int, Matrix], dict[str, Matrix], Matrix, dict[int, tuple[int, str] | None]]:
    root = states.index(AGY_BASE)
    frames: dict[int, Matrix] = {root: eye()}
    parents: dict[int, tuple[int, str] | None] = {root: None}
    pending: deque[int] = deque([root])
    while pending:
        source = pending.popleft()
        for move_type in MOVE_TYPES:
            token = f"{source}{move_type}"
            edge = edges[token]
            target = int(edge["target"])
            if target in frames:
                continue
            frames[target] = matmul(edge["matrix"], frames[source])  # type: ignore[arg-type]
            parents[target] = (source, move_type)
            pending.append(target)
    expect_equal(set(frames), set(range(7)), "frame vertices")
    j0 = inverse_unimodular(crossing_form(states[root]))
    expected_j0 = (
        (0, -1, 0, 0),
        (1, 0, -1, 1),
        (0, 1, 0, -1),
        (0, -1, 1, 0),
    )
    expect_equal(j0, expected_j0, "base symplectic form J0")
    fixed: dict[str, Matrix] = {}
    for vertex, frame in frames.items():
        state_form = inverse_unimodular(crossing_form(states[vertex]))
        expect_equal(matmul(matmul(transpose(frame), state_form), frame), j0, f"frame identity at {vertex}")
    for token, edge in edges.items():
        source, target = int(edge["source"]), int(edge["target"])
        fixed[token] = matmul(
            matmul(inverse_unimodular(frames[target]), edge["matrix"]),  # type: ignore[arg-type]
            frames[source],
        )
        expect_equal(
            matmul(matmul(transpose(fixed[token]), j0), fixed[token]),
            j0,
            f"fixed-fibre symplectic identity for {token}",
        )
    return frames, fixed, j0, parents


def make_darts(edges: dict[str, dict[str, object]], matrices: dict[str, Matrix]) -> dict[str, dict[str, object]]:
    darts: dict[str, dict[str, object]] = {}
    for token in sorted(edges):
        edge = edges[token]
        source, target = int(edge["source"]), int(edge["target"])
        matrix = matrices[token]
        darts[token] = {
            "positive_edge_id": token,
            "orientation": 1,
            "source": source,
            "target": target,
            "matrix": matrix,
        }
        darts[token + "^-1"] = {
            "positive_edge_id": token,
            "orientation": -1,
            "source": target,
            "target": source,
            "matrix": inverse_unimodular(matrix),
        }
    return darts


def path_states(word: tuple[str, ...] | list[str], darts: dict[str, dict[str, object]]) -> list[int]:
    expect(bool(word), "empty path has no marked start")
    states = [int(darts[word[0]]["source"])]
    for index, token in enumerate(word):
        expect_equal(states[-1], int(darts[token]["source"]), f"state continuity at {index}:{token}")
        states.append(int(darts[token]["target"]))
    return states


def witness_record(word: tuple[str, ...], states: list[int], darts: dict[str, dict[str, object]]) -> dict[str, object]:
    observed_states = path_states(word, darts)
    expect_equal(observed_states, states, f"states for {word}")
    product = product_path_order(word, darts)
    return {
        "tokens_path_order": list(word),
        "states": observed_states,
        "length": len(word),
        "closed": observed_states[0] == observed_states[-1],
        "linear_nonbacktracking": linearly_reduced(word),
        "cyclic_nonbacktracking": cyclically_reduced(word),
        "primitive": primitive(word),
        "distinct_rotations": len(set(rotations(word))),
        "inverse_is_rotation": inverse_word(word) in rotations(word),
        "chronological_holonomy": matrix_json(product),
        "identity_holonomy": product == eye(),
    }


def exact_census(darts: dict[str, dict[str, object]], max_length: int = 9) -> dict[str, object]:
    outgoing: dict[int, list[str]] = {vertex: [] for vertex in range(7)}
    for token, dart in darts.items():
        outgoing[int(dart["source"])].append(token)
    for tokens in outgoing.values():
        tokens.sort()
    expect_equal({len(tokens) for tokens in outgoing.values()}, {4}, "oriented vertex degrees")
    successor_counts = {
        token: len(
            [
                candidate
                for candidate in outgoing[int(dart["target"])]
                if candidate != bar_token(token)
            ]
        )
        for token, dart in darts.items()
    }
    predecessor_counts = {
        token: sum(
            int(prior_dart["target"]) == int(darts[token]["source"])
            and token != bar_token(prior)
            for prior, prior_dart in darts.items()
        )
        for token in darts
    }
    expect_equal(set(successor_counts.values()), {3}, "Hashimoto successor degree")
    expect_equal(set(predecessor_counts.values()), {3}, "Hashimoto predecessor degree")

    observed = {key: [] for key in EXPECTED_CENSUS}
    for length in range(1, max_length + 1):
        identities: list[tuple[str, ...]] = []

        def extend(first: str, word: tuple[str, ...], product: Matrix) -> None:
            if len(word) == length:
                if (
                    int(darts[word[-1]]["target"]) == int(darts[first]["source"])
                    and first != bar_token(word[-1])
                    and product == eye()
                ):
                    identities.append(word)
                return
            vertex = int(darts[word[-1]]["target"])
            for token in outgoing[vertex]:
                if token == bar_token(word[-1]):
                    continue
                extend(first, word + (token,), matmul(darts[token]["matrix"], product))  # type: ignore[arg-type]

        for first in sorted(darts):
            extend(first, (first,), darts[first]["matrix"])  # type: ignore[arg-type]

        primitive_identities = [word for word in identities if primitive(word)]
        all_rotation_classes = {min(rotations(word)) for word in identities}
        primitive_rotation_classes = {min(rotations(word)) for word in primitive_identities}
        all_dihedral_classes = {
            min(min(rotations(word)), min(rotations(inverse_word(word)))) for word in identities
        }
        primitive_dihedral_classes = {
            min(min(rotations(word)), min(rotations(inverse_word(word))))
            for word in primitive_identities
        }
        primitive_self_inverse = {
            min(rotations(word))
            for word in primitive_identities
            if inverse_word(word) in rotations(word)
        }
        observed["all_marked_identity"].append(len(identities))
        observed["primitive_marked_identity"].append(len(primitive_identities))
        observed["all_oriented_rotation_classes"].append(len(all_rotation_classes))
        observed["primitive_oriented_rotation_classes"].append(len(primitive_rotation_classes))
        observed["all_dihedral_classes"].append(len(all_dihedral_classes))
        observed["primitive_dihedral_classes"].append(len(primitive_dihedral_classes))
        observed["primitive_self_inverse_rotation_classes"].append(len(primitive_self_inverse))

    expect_equal(observed, EXPECTED_CENSUS, "C25 identity census")
    return {
        "lengths": list(range(1, max_length + 1)),
        **observed,
        "determinant_moments_use": "all_marked_identity",
        "primitive_filter_is_not_used_for_N_n": True,
        "oriented_outdegree": {str(vertex): len(tokens) for vertex, tokens in sorted(outgoing.items())},
        "hashimoto_successor_degree": sorted(set(successor_counts.values())),
        "hashimoto_predecessor_degree": sorted(set(predecessor_counts.values())),
        "hashimoto_row_and_column_degree": max(successor_counts.values()),
        "unitary_block_operator_norm_bound": max(successor_counts.values()),
        "exact_N6": 24,
        "exact_log_coefficient_u6": {"numerator": -4, "denominator": 1},
        "scope": "bounded exact regression census; nonconstancy is already proved by explicit witnesses",
    }


def follow_elementary(
    start: int, word: str, edges: dict[str, dict[str, object]]
) -> tuple[int, Matrix, list[int]]:
    current = start
    product = eye()
    states = [start]
    for move_type in word:
        token = f"{current}{move_type}"
        edge = edges[token]
        product = matmul(edge["matrix"], product)  # type: ignore[arg-type]
        current = int(edge["target"])
        states.append(current)
    return current, product, states


def c26_exact_record(
    edges: dict[str, dict[str, object]], j0: Matrix
) -> tuple[dict[str, object], dict[str, object], dict[str, Matrix], dict[str, object]]:
    base = 4
    words = {
        "A": GAMMA_STAR,
        "H": H_BRIDGE,
        "K": K_BRIDGE,
        "B": GAMMA_STAR + H_BRIDGE + GAMMA_STAR,
        "C": GAMMA_STAR + K_BRIDGE + GAMMA_STAR,
    }
    matrices: dict[str, Matrix] = {}
    state_traces: dict[str, list[int]] = {}
    for name, word in words.items():
        end, matrix, states = follow_elementary(base, word, edges)
        expect_equal(end, base, f"C26 {name} loop endpoint")
        expect_equal(matmul(matmul(transpose(matrix), j0), matrix), j0, f"C26 {name} symplectic")
        matrices[name] = matrix
        state_traces[name] = states
    expect(4 not in state_traces["H"][1:-1], "H bridge has an internal state-4 return")
    expect(4 not in state_traces["K"][1:-1], "K bridge has an internal state-4 return")
    expect_equal(matrices["B"], matmul(matmul(matrices["A"], matrices["H"]), matrices["A"]), "B=AHA")
    expect_equal(matrices["C"], matmul(matmul(matrices["A"], matrices["K"]), matrices["A"]), "C=AKA")

    y = matmul(matmul(inverse_unimodular(matrices["H"]), matrices["K"]), matrices["H"])
    delta_left = matmul(matmul(matrices["K"], y), matrices["K"])
    delta_right = matmul(matmul(y, matrices["K"]), y)
    matrices["Y"] = y
    matrices["Delta"] = delta_left
    expect_equal(delta_left, delta_right, "KYK=YKY")

    v, phi = (0, 1, 1, 1), (1, 0, 0, 0)
    w, psi = (-1, 1, 0, 1), (1, 0, 0, 1)
    expect_equal(matrices["K"], matrix_add(eye(), outer(v, phi)), "rank-one factor for K")
    expect_equal(y, matrix_add(eye(), outer(w, psi)), "rank-one factor for Y")
    pairings = {
        "phiT_v": sum(phi[i] * v[i] for i in range(4)),
        "psiT_w": sum(psi[i] * w[i] for i in range(4)),
        "phiT_w": sum(phi[i] * w[i] for i in range(4)),
        "psiT_v": sum(psi[i] * v[i] for i in range(4)),
    }
    expect_equal(
        pairings,
        {"phiT_v": 0, "psiT_w": 0, "phiT_w": -1, "psiT_v": 1},
        "rank-one pairings",
    )
    rank_one_checks = {
        "K_minus_I_equals_v_phiT": matrices["K"] == matrix_add(eye(), outer(v, phi)),
        "Y_minus_I_equals_w_psiT": y == matrix_add(eye(), outer(w, psi)),
        "contractions_exact": pairings
        == {"phiT_v": 0, "psiT_w": 0, "phiT_w": -1, "psiT_v": 1},
    }

    matrix_hashes = {name: canonical_sha256(matrix_json(matrix)) for name, matrix in matrices.items()}
    expect_equal(matrix_hashes, EXPECTED_MATRIX_HASHES, "C26 compact matrix hashes")
    y_word = ("H^-1", "K", "H")
    lhs_word = ("K", *y_word, "K")
    rhs_word = (*y_word, "K", *y_word)
    hk_relation = free_reduce((*lhs_word, *inverse_word(rhs_word)))
    expect_equal(len(hk_relation), 12, "derived H,K relation length")
    expect_equal(product_written_order(hk_relation, matrices), eye(), "derived H,K relation")
    substitutions = {
        "H": ("A^-1", "B", "A^-1"),
        "K": ("A^-1", "C", "A^-1"),
    }
    derived_word = substitute_and_reduce(hk_relation, substitutions)
    expect_equal(derived_word, C26_HOLONOMY_WORD, "independently derived A,B,C relation")
    product = product_written_order(derived_word, matrices)
    path_word = tuple(reversed(derived_word))
    rose_darts: dict[str, dict[str, object]] = {}
    for name in ("A", "B", "C"):
        rose_darts[name] = {"matrix": matrices[name]}
        rose_darts[name + "^-1"] = {"matrix": inverse_unimodular(matrices[name])}
    path_product = product_path_order(path_word, rose_darts)
    forward_triple = matmul(matrices["C"], matmul(matrices["B"], matrices["A"]))
    reversed_triple = matmul(matrices["A"], matmul(matrices["B"], matrices["C"]))
    rose_symbols = tuple(sorted(rose_darts))
    successor_counts = {
        token: len([candidate for candidate in rose_symbols if candidate != bar_token(token)])
        for token in rose_symbols
    }
    predecessor_counts = {
        token: len([prior for prior in rose_symbols if token != bar_token(prior)])
        for token in rose_symbols
    }
    expect_equal(set(successor_counts.values()), {5}, "C26 rose successor degree")
    expect_equal(set(predecessor_counts.values()), {5}, "C26 rose predecessor degree")
    word_checks = {
        "length": len(derived_word),
        "linear_reduced": linearly_reduced(derived_word),
        "cyclically_reduced": cyclically_reduced(derived_word),
        "primitive": primitive(derived_word),
        "distinct_rotations": len(set(rotations(derived_word))),
        "inverse_is_rotation": inverse_word(derived_word) in rotations(derived_word),
        "identity_product": product == eye(),
        "path_order_later_on_left_identity_product": path_product == eye(),
    }
    expect(path_product == eye(), "C26 later-on-left path product is not identity")
    expect(forward_triple != reversed_triple, "C26 forward/reverse chronology sentinel collapsed")
    expect_equal(
        word_checks,
        {
            "length": 24,
            "linear_reduced": True,
            "cyclically_reduced": True,
            "primitive": True,
            "distinct_rotations": 24,
            "inverse_is_rotation": False,
            "identity_product": True,
            "path_order_later_on_left_identity_product": True,
        },
        "C26 expanded word checks",
    )
    record = {
        "elementary_words": {
            "A_gamma_star": "t^64 (tbttbtbb)^8",
            "A_length": 128,
            "H_bridge": H_BRIDGE,
            "H_length": 7,
            "K_bridge": K_BRIDGE,
            "K_length": 3,
            "B_branch_length": 263,
            "C_branch_length": 259,
        },
        "matrices": {name: matrix_json(matrix) for name, matrix in matrices.items()},
        "producer_regression_matrix_sha256": matrix_hashes,
        "matrix_hash_role": "producer regression sentinels; not independent checker evidence",
        "factorization": {"B_equals_AHA": True, "C_equals_AKA": True},
        "rank_one_braid": {
            "Y_definition": "H^-1*K*H",
            **rank_one_checks,
            "contractions": pairings,
            "KYK_equals_YKY": True,
            "common_matrix": matrix_json(delta_left),
        },
        "word_derivation": {
            "Y_word": list(y_word),
            "KYK_word": list(lhs_word),
            "YKY_word": list(rhs_word),
            "free_reduced_HK_relation": list(hk_relation),
            "substitutions": {name: list(word) for name, word in substitutions.items()},
            "derived_not_postulated": True,
        },
        "holonomy_order_word": list(derived_word),
        "later_on_left_path_order_word": list(path_word),
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
        "identity_repetition": {
            "word": list(C1 + C1),
            "length": 12,
            "closed": True,
            "cyclic_nonbacktracking": True,
            "identity_holonomy": True,
            "primitive": False,
            "enters_all_cycle_moment": True,
            "enters_primitive_census": False,
        },
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
    details = {
        "H_state_path": state_traces["H"],
        "K_state_path": state_traces["K"],
        "rank_one_pairings": pairings,
        "forward_reverse_triple_distinct": True,
    }
    return record, repetition, matrices, details


def sorted_gate_map(gates: dict[str, str]) -> dict[str, str]:
    def number(name: str) -> int:
        prefix = name.split("_", 1)[0]
        return int(prefix[1:]) if prefix.startswith("G") and prefix[1:].isdigit() else 999

    return dict(sorted(gates.items(), key=lambda item: (number(item[0]), item[0])))


def run(certificate_path: Path) -> dict[str, object]:
    audit = Audit()
    raw_certificate = certificate_path.read_bytes()
    certificate_sha = hashlib.sha256(raw_certificate).hexdigest()
    envelope = json.loads(raw_certificate)

    def gate_13() -> dict[str, object]:
        expect_equal(set(envelope), {"schema", "payload", "payload_sha256"}, "envelope keys")
        expect_equal(envelope["schema"], "HCS-C29-EXACT-CERTIFICATE-v1", "certificate schema")
        expect(isinstance(envelope["payload"], dict), "payload is not an object")
        digest = canonical_sha256(envelope["payload"])
        expect_equal(envelope["payload_sha256"], digest, "canonical payload digest")
        return {"schema": envelope["schema"], "payload_sha256": digest}

    audit.gate("G13_payload_envelope", gate_13)
    payload: dict[str, object] = envelope["payload"]

    sources: dict[str, object] = {}

    def gate_0() -> dict[str, object]:
        observed = {name: sha256(path) for name, path in SOURCE_PATHS.items()}
        expect_equal(observed, EXPECTED_SOURCE_HASHES, "upstream source hashes")
        expected_files = {
            name: {"path": str(path.relative_to(REPO_ROOT)), "sha256": observed[name]}
            for name, path in SOURCE_PATHS.items()
        }
        source_lock = payload["source_lock"]
        expect_equal(
            source_lock,
            {
                "files": expected_files,
                "chronology_id": "LATER_ON_LEFT_EXACT",
                "prime_scope": "odd primes only; fixed path length before the prime limit",
                "forbidden_data": "no prime table, Riemann-zero table, fitted clock, or averaged chronology",
            },
            "complete payload source lock",
        )
        sources["c25"] = json.loads(SOURCE_PATHS["C25_certificate"].read_text(encoding="utf-8"))
        sources["c26"] = json.loads(SOURCE_PATHS["C26_certificate"].read_text(encoding="utf-8"))
        sources["c28"] = json.loads(SOURCE_PATHS["C28_certificate"].read_text(encoding="utf-8"))
        return {"source_hashes": observed}

    audit.gate("G0_source_lock", gate_0)

    graph_context: dict[str, object] = {}

    def gate_1() -> dict[str, object]:
        states, edges = reconstruct_graph()
        c25 = sources["c25"]
        upstream_states = tuple(
            (tuple(row["top"]), tuple(row["bottom"])) for row in c25["graph"]["states"]  # type: ignore[index]
        )
        expect_equal(upstream_states, states, "C25 upstream states")
        upstream_edges = {(int(row["source"]), row["type"]): row for row in c25["graph"]["edges"]}  # type: ignore[index]
        for token, edge in edges.items():
            key = (int(edge["source"]), edge["type"])
            row = upstream_edges[key]
            expect_equal(int(row["target"]), edge["target"], f"upstream target {token}")
            expect_equal(as_matrix(row["chronological_matrix"]), edge["matrix"], f"upstream matrix {token}")
            expect_equal((int(row["winner"]), int(row["loser"])), (edge["winner"], edge["loser"]), f"winner/loser {token}")
        graph_context.update({"states": states, "edges": edges})
        return {
            "states": len(states),
            "positive_arrows": len(edges),
            "central_state": 2,
            "AGY_base_state": 4,
            "target_map": EXPECTED_TARGETS,
        }

    audit.gate("G1_exact_graph", gate_1)

    frame_context: dict[str, object] = {}

    def gate_2() -> dict[str, object]:
        states = graph_context["states"]
        edges = graph_context["edges"]
        frames, fixed, j0, parents = reconstruct_frames(states, edges)  # type: ignore[arg-type]
        c25 = sources["c25"]
        upstream_frames = {
            int(row["state"]): as_matrix(row["frame_S"])
            for row in c25["statewise_symplectic_trivialization"]["state_frames"]  # type: ignore[index]
        }
        expect_equal(upstream_frames, frames, "C25 upstream frames")
        upstream_fixed = {
            f"{int(row['source'])}{row['type']}": as_matrix(row["g_edge_equals_S_target_inverse_B_edge_S_source"])
            for row in c25["statewise_symplectic_trivialization"]["fixed_fiber_edges"]  # type: ignore[index]
        }
        expect_equal(upstream_fixed, fixed, "C25 upstream fixed-fibre matrices")
        expect_equal(
            as_matrix(c25["statewise_symplectic_trivialization"]["base_form_J0"]),  # type: ignore[index]
            j0,
            "C25 upstream J0",
        )
        identity_edges = sorted(token for token, matrix in fixed.items() if matrix == eye())
        expect_equal(identity_edges, ["0b", "0t", "2b", "2t", "4b", "6t"], "identity frame edges")
        graph_payload = payload["c25_graph_reconstruction"]
        expect_equal(graph_payload["states"], 7, "payload graph states")  # type: ignore[index]
        expect_equal(graph_payload["positive_arrows"], 14, "payload positive arrows")  # type: ignore[index]
        expect_equal(graph_payload["oriented_darts"], 28, "payload oriented darts")  # type: ignore[index]
        expect_equal(graph_payload["base_state"], 4, "payload base state")  # type: ignore[index]
        expect_equal(graph_payload["identity_fixed_frame_edges"], 6, "payload identity frame count")  # type: ignore[index]
        expect_equal(graph_payload["nonidentity_fixed_frame_edges"], 8, "payload nonidentity frame count")  # type: ignore[index]
        frame_context.update({"frames": frames, "fixed": fixed, "j0": j0, "parents": parents})
        return {"state_frames": 7, "identity_edges": identity_edges, "J0": matrix_json(j0)}

    audit.gate("G2_frames_and_fixed_fibre", gate_2)

    dart_context: dict[str, object] = {}

    def gate_3() -> dict[str, object]:
        edges = graph_context["edges"]
        fixed = frame_context["fixed"]
        raw = {token: edge["matrix"] for token, edge in edges.items()}  # type: ignore[union-attr]
        fixed_darts = make_darts(edges, fixed)  # type: ignore[arg-type]
        raw_darts = make_darts(edges, raw)  # type: ignore[arg-type]
        expect_equal(len(fixed_darts), 28, "formal dart count")
        for token, dart in fixed_darts.items():
            opposite = bar_token(token)
            expect_equal(dart["positive_edge_id"], fixed_darts[opposite]["positive_edge_id"], f"positive edge id {token}")
            expect_equal(dart["source"], fixed_darts[opposite]["target"], f"inverse source {token}")
            expect_equal(dart["target"], fixed_darts[opposite]["source"], f"inverse target {token}")
            expect_equal(matmul(dart["matrix"], fixed_darts[opposite]["matrix"]), eye(), f"inverse matrix {token}")  # type: ignore[arg-type]
        expect_equal(fixed_darts["0b^-1"]["positive_edge_id"], "0b", "0b inverse identity")
        expect(fixed_darts["0b^-1"]["matrix"] != fixed_darts["3b"]["matrix"], "0b^-1 collapsed to antiparallel 3b")
        expect(fixed_darts["6t^-1"]["matrix"] != fixed_darts["5t"]["matrix"], "6t^-1 collapsed to antiparallel 5t")
        sentinel = payload["c25_graph_reconstruction"]["formal_inverse_opposite_arrow_sentinel"]  # type: ignore[index]
        expect_equal(
            sentinel,
            {
                "formal_inverse": "0b^-1",
                "positive_edge_id_retained": "0b",
                "antiparallel_positive_arrow": "3b",
                "matrices_are_distinct": True,
            },
            "payload inverse/opposite sentinel",
        )
        expect_equal(payload["c25_graph_reconstruction"]["formal_backtracking_pair_identities"], 28, "marked formal backtracking pairs")  # type: ignore[index]
        expect_equal(
            payload["c25_graph_reconstruction"]["formal_backtracking_pair_scope"],  # type: ignore[index]
            "the 28 marked pairs e*bar(e), not an unrestricted length-two census",
            "formal backtracking scope",
        )
        expect_equal(
            set(payload["c25_graph_reconstruction"]),  # type: ignore[arg-type]
            {
                "states",
                "positive_arrows",
                "oriented_darts",
                "base_state",
                "identity_fixed_frame_edges",
                "nonidentity_fixed_frame_edges",
                "formal_inverse_opposite_arrow_sentinel",
                "formal_backtracking_pair_identities",
                "formal_backtracking_pair_scope",
            },
            "graph payload keys",
        )
        dart_context.update({"fixed": fixed_darts, "raw": raw_darts})
        return {
            "oriented_darts": 28,
            "0b_inverse_distinct_from_3b": True,
            "6t_inverse_distinct_from_5t": True,
        }

    audit.gate("G3_formal_inverse_semantics", gate_3)

    witness_context: dict[str, object] = {}

    def gate_4() -> dict[str, object]:
        fixed_darts = dart_context["fixed"]
        raw_darts = dart_context["raw"]
        c1_fixed = product_path_order(C1, fixed_darts)  # type: ignore[arg-type]
        c2_fixed = product_path_order(C2, fixed_darts)  # type: ignore[arg-type]
        c1_raw = product_path_order(C1, raw_darts)  # type: ignore[arg-type]
        c2_raw = product_path_order(C2, raw_darts)  # type: ignore[arg-type]
        expect_equal((c1_fixed, c2_fixed, c1_raw, c2_raw), (eye(), eye(), eye(), eye()), "C25 chronological holonomies")
        wrong_c2 = eye()
        for token in C2:
            wrong_c2 = matmul(wrong_c2, fixed_darts[token]["matrix"])  # type: ignore[index,arg-type]
        expect(wrong_c2 != eye(), "C2 wrong chronology unexpectedly retained identity")
        expect_equal(payload["conventions"]["chronology_id"], "LATER_ON_LEFT_EXACT", "payload chronology enum")  # type: ignore[index]
        witness_context.update({"C1_fixed": c1_fixed, "C2_fixed": c2_fixed})
        return {"C1_fixed_and_raw_identity": True, "C2_fixed_and_raw_identity": True, "wrong_C2_order_rejected": True}

    audit.gate("G4_chronology", gate_4)

    def gate_5() -> dict[str, object]:
        for name, word in {"C1": C1, "C2": C2}.items():
            expect(linearly_reduced(word), f"{name} is not linearly nonbacktracking")
            expect(cyclically_reduced(word), f"{name} is not cyclically nonbacktracking")
            expect(primitive(word), f"{name} is a proper power")
            expect_equal(len(set(rotations(word))), 6, f"{name} distinct rotations")
            expect(inverse_word(word) not in rotations(word), f"{name} is self-inverse up to rotation")
        c1_dihedral = min(min(rotations(C1)), min(rotations(inverse_word(C1))))
        c2_dihedral = min(min(rotations(C2)), min(rotations(inverse_word(C2))))
        expect(c1_dihedral != c2_dihedral, "C1 and C2 are dihedrally equivalent")
        cyclic_wrap_mutation = ("0t", "1b", "0t^-1")
        expect(linearly_reduced(cyclic_wrap_mutation), "cyclic-wrap mutation is not linearly reduced")
        expect(not cyclically_reduced(cyclic_wrap_mutation), "cyclic-wrap mutation was not rejected")
        return {"C1_C2_primitive": True, "inverse_classes_distinct": True, "dihedral_classes_distinct": True, "cyclic_wrap_checked": True}

    audit.gate("G5_primitive_and_inverse_rotation", gate_5)

    def gate_6() -> dict[str, object]:
        fixed_darts = dart_context["fixed"]
        expected_c1 = {"id": "C1", **witness_record(C1, C1_STATES, fixed_darts)}  # type: ignore[arg-type]
        expected_c2 = {"id": "C2", **witness_record(C2, C2_STATES, fixed_darts)}  # type: ignore[arg-type]
        witness_payload = payload["c25_identity_witnesses"]
        expect_equal(witness_payload["C1"], expected_c1, "payload C1 witness")  # type: ignore[index]
        expect_equal(witness_payload["C2"], expected_c2, "payload C2 witness")  # type: ignore[index]
        expect_equal(witness_payload["distinct_dihedral_classes"], True, "payload dihedral separation")  # type: ignore[index]
        expect_equal(witness_payload["proof_level_marked_lower_bound_N6"], 24, "payload N6 lower bound")  # type: ignore[index]
        expect_equal(
            set(witness_payload),  # type: ignore[arg-type]
            {"C1", "C2", "distinct_dihedral_classes", "proof_level_marked_lower_bound_N6"},
            "identity witness payload keys",
        )

        generator = fixed_darts["3t"]["matrix"]  # type: ignore[index]
        j0 = frame_context["j0"]
        expect_equal(matmul(matmul(transpose(generator), j0), generator), j0, "gauge generator symplectic")  # type: ignore[arg-type]
        gauges = {vertex: matpow(generator, vertex) for vertex in range(7)}  # type: ignore[arg-type]
        gauge_symplectic = {
            str(vertex): matmul(matmul(transpose(matrix), j0), matrix) == j0
            for vertex, matrix in gauges.items()
        }
        expect(all(gauge_symplectic.values()), "a gauge matrix does not preserve J0")
        transformed: dict[str, dict[str, object]] = {}
        for token, dart in fixed_darts.items():  # type: ignore[union-attr]
            source, target = int(dart["source"]), int(dart["target"])
            transformed[token] = {
                **dart,
                "matrix": matmul(matmul(inverse_unimodular(gauges[target]), dart["matrix"]), gauges[source]),  # type: ignore[arg-type]
            }
        formal_inverse_compatibility = all(
            transformed[bar_token(token)]["matrix"]
            == inverse_unimodular(transformed[token]["matrix"])  # type: ignore[arg-type]
            for token in transformed
        )
        expect(formal_inverse_compatibility, "gauge transform broke formal inverses")
        gauge_checks = {}
        for name, word in {"C1": C1, "C2": C2}.items():
            base = int(fixed_darts[word[0]]["source"])  # type: ignore[index]
            original = product_path_order(word, fixed_darts)  # type: ignore[arg-type]
            transformed_product = product_path_order(word, transformed)
            expected = matmul(matmul(inverse_unimodular(gauges[base]), original), gauges[base])
            gauge_checks[name] = transformed_product == expected == eye()
        expect_equal(gauge_checks, {"C1": True, "C2": True}, "gauge identity invariance")
        original_nonidentity = product_path_order(("4t",), fixed_darts)  # type: ignore[arg-type]
        transformed_nonidentity = product_path_order(("4t",), transformed)
        nonidentity_conjugacy = (
            original_nonidentity != eye()
            and transformed_nonidentity
            == matmul(
                matmul(inverse_unimodular(gauges[4]), original_nonidentity), gauges[4]
            )
        )
        expect(nonidentity_conjugacy, "nonidentity gauge-conjugacy sentinel failed")
        expect_equal(
            payload["c25_gauge_control"],
            {
                "gauge_family": "h_v=(g_3t)^v, v=0,...,6",
                "source_derived_symplectic": True,
                "arrow_rule": "g'_e=h_target^-1*g_e*h_source",
                "closed_path_rule": "g'_C=h_base^-1*g_C*h_base",
                "all_h_v_preserve_J0": gauge_symplectic,
                "formal_inverse_compatibility": formal_inverse_compatibility,
                "identity_verdicts_preserved": gauge_checks,
                "nonidentity_closed_loop": "4t",
                "nonidentity_conjugacy_verified": nonidentity_conjugacy,
            },
            "payload gauge control",
        )
        return {"witnesses": ["C1", "C2"], "marked_lower_bound_N6": 24, "gauge_invariant": True}

    audit.gate("G6_C25_exact_witnesses_and_gauge", gate_6)

    census_context: dict[str, object] = {}

    def gate_7() -> dict[str, object]:
        expected = exact_census(dart_context["fixed"])  # type: ignore[arg-type]
        expect_equal(payload["c25_identity_census"], expected, "payload exact C25 census")
        c1_squared = C1 + C1
        expect(cyclically_reduced(c1_squared), "C1^2 lost cyclic nonbacktracking")
        expect(not primitive(c1_squared), "C1^2 incorrectly classified primitive")
        expect_equal(product_path_order(c1_squared, dart_context["fixed"]), eye(), "C1^2 holonomy")  # type: ignore[arg-type]
        census_context.update(expected)
        return {
            "all_marked_identity": expected["all_marked_identity"],
            "primitive_marked_identity": expected["primitive_marked_identity"],
            "all_vs_primitive_schema_separate": True,
            "C1_squared_nonprimitive_identity": True,
        }

    audit.gate("G7_all_vs_primitive_census", gate_7)

    c26_context: dict[str, object] = {}

    def gate_8() -> dict[str, object]:
        record, repetition, matrices, details = c26_exact_record(graph_context["edges"], frame_context["j0"])  # type: ignore[arg-type]
        c26 = sources["c26"]
        source = c26["source_locked_branch"]  # type: ignore[index]
        two = c26["scalar_periodic_trace_gate"]["chronological_two_return_witness"]  # type: ignore[index]
        three = c26["scalar_periodic_trace_gate"]["three_return_spectral_chronology_witness"]  # type: ignore[index]
        upstream = {
            "A": as_matrix(source["chronological_matrix_B"]),
            "H": as_matrix(two["return_bridge_chronological_matrix_B"]),
            "K": as_matrix(three["third_return_bridge_chronological_matrix_B"]),
            "B": as_matrix(two["second_branch_chronological_matrix_B"]),
            "C": as_matrix(three["third_branch_chronological_matrix_B"]),
        }
        expect_equal({name: matrices[name] for name in upstream}, upstream, "C26 upstream matrices")
        expect_equal(source["gamma_star_word"], GAMMA_STAR, "C26 gamma_star word")
        expect_equal(two["return_bridge_word"], H_BRIDGE, "C26 H bridge word")
        expect_equal(three["third_return_bridge_word"], K_BRIDGE, "C26 K bridge word")
        expect_equal(payload["c26_branch_relation"], record, "payload C26 relation")
        c26_context.update({"record": record, "repetition": repetition, "matrices": matrices})
        return {
            "factorization": record["factorization"],
            "braid": record["rank_one_braid"]["KYK_equals_YKY"],  # type: ignore[index]
            "word_checks": record["word_checks"],
            "marked_lower_bound_N24": 48,
            **details,
        }

    audit.gate("G8_C26_braid_and_length24_relation", gate_8)

    def gate_9() -> dict[str, object]:
        expected = c26_context["repetition"]
        expect_equal(payload["repetition_controls"], expected, "payload repetition controls")
        identity_control = expected["identity_repetition"]  # type: ignore[index]
        torsion_control = expected["torsion_repetition"]  # type: ignore[index]
        expect(identity_control["enters_all_cycle_moment"] and not identity_control["enters_primitive_census"], "identity repetition bookkeeping")
        expect(torsion_control["Delta_fourth_power_identity"], "Delta fourth-power control")
        expect_equal(torsion_control["repetition_law"], "THETA_OF_HOLONOMY_POWER_NOT_POWER_OF_CHARACTER", "torsion character law")
        return {"C1_squared": "NONPRIMITIVE_IDENTITY_INCLUDED_IN_ALL_MOMENTS", "Delta_fourth_power": "IDENTITY", "character_atom": "Theta_p(Delta^4)"}

    audit.gate("G9_repetition_and_torsion", gate_9)

    def gate_10() -> dict[str, object]:
        c28_limit = sources["c28"]["normalized_character_limit_theorem"]  # type: ignore[index]
        expect_equal(c28_limit["pointwise_limit"], "Theta_p(h)/p^2 -> 1 if h=I and 0 otherwise", "C28 pointwise limit")
        expected = {
            "upstream_status": c28_limit["status"],
            "formula": "p^(-2)*Theta_p(g) -> 1 if g=I and 0 otherwise",
            "odd_primes_only": True,
            "fixed_length_before_prime_limit": True,
            "infinite_path_sum_interchange_claimed": False,
            "repetition_law": "THETA_OF_HOLONOMY_POWER_NOT_POWER_OF_CHARACTER",
        }
        expect_equal(payload["finite_weil_limit"], expected, "payload finite-Weil limit")
        return {"upstream_status": c28_limit["status"], "scope": "ODD_PRIMES_FIXED_G_FIXED_N", "termwise_limit_legal": True}

    audit.gate("G10_finite_weil_fixed_length_limit", gate_10)

    def gate_11() -> dict[str, object]:
        expected = {
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
        }
        expect_equal(payload["normalized_determinant_germ"], expected, "payload determinant germ")
        expect_equal(census_context["unitary_block_operator_norm_bound"], 3, "C25 norm bound")
        expect_equal(c26_context["record"]["unitary_block_operator_norm_bound"], 5, "C26 norm bound")  # type: ignore[index]
        expect_equal(c26_context["record"]["N24_C26_is_exact_total"], False, "N24 lower-bound scope")  # type: ignore[index]
        return {"C25_M": 3, "C26_M": 5, "common_Log0_disc": "|u|<1/5", "C25_log_u6": -4, "C26_log_u24": "<= -2"}

    audit.gate("G11_normalized_Log0_determinant", gate_11)

    def gate_12() -> dict[str, object]:
        expected_conventions = {
            "chronology_id": "LATER_ON_LEFT_EXACT",
            "formal_inverse_id": "SAME_LABELED_EDGE_FORMAL_INVERSE_EXACT",
            "inverse_word_id": "REVERSE_ORDER_THEN_FLIP_ORIENTATION",
            "formal_inverse_is_opposite_positive_arrow": False,
            "nonbacktracking": "forbid e followed by formal bar(e), including cyclic closure",
            "unit_marks": True,
        }
        expected_natural = {
            "result": "POSITIVE_PERIODIC_PRODUCT_GERM_ONE",
            "basis": "C25 all-length fixed-start positive-monoid freeness",
            "forward_products_unchanged_by_natural_extension": True,
            "two_sided_transfer_operator_constructed": False,
            "symmetric_object_scope": "NEW_SYMMETRIC_DYNAMICS_NOT_NATURAL_EXTENSION",
        }
        expected_scope = {
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
        }
        expect_equal(payload["conventions"], expected_conventions, "payload conventions")
        expect_equal(payload["natural_extension_control"], expected_natural, "payload natural-extension control")
        expect_equal(payload["scope_decisions"], expected_scope, "payload scope decisions")
        expect_equal(payload["candidate_id"], "HCS-C29", "candidate id")
        expect_equal(payload["candidate_name"], "symmetric non-backtracking C26 return-matrix groupoid", "candidate name")
        expect_equal(
            payload["verification"],
            {
                "status": "PRODUCER_ONLY_UNVERIFIED_UNTIL_INDEPENDENT_CHECKER",
                "independent_checker_required": True,
                "checker_must_not_import_producer": True,
            },
            "producer verification status",
        )
        expect_equal(
            payload["material_passport"],
            {
                "schema": 9,
                "data_class": "frozen repository exact-integer artifacts",
                "analysis": "source-locked theorem-driven exact computation",
                "human_subjects": False,
                "AI_assistance_disclosure_required": True,
            },
            "material passport",
        )
        expect_equal(
            payload["runtime"],
            {
                "producer_sha256": sha256(PRODUCER_PATH),
                "arithmetic": "Python integers and fractions; no floating point",
                "environment_fields_in_canonical_payload": False,
            },
            "complete runtime payload",
        )
        expected_payload_keys = {
            "candidate_id",
            "candidate_name",
            "verification",
            "material_passport",
            "source_lock",
            "conventions",
            "c25_graph_reconstruction",
            "c25_identity_witnesses",
            "c25_gauge_control",
            "c25_identity_census",
            "c26_branch_relation",
            "repetition_controls",
            "natural_extension_control",
            "finite_weil_limit",
            "normalized_determinant_germ",
            "scope_decisions",
            "runtime",
        }
        expect_equal(set(payload), expected_payload_keys, "payload top-level keys")
        return {"natural_extension": "NO_INVERSE_LETTERS_GERM_ONE", "symmetric_groupoid": "DECLARED_NEW_DYNAMICS", "Route_A": "STOP", "Route_B": False}

    audit.gate("G12_semantic_scope_firewalls", gate_12)

    ordered_gates = sorted_gate_map(audit.gates)
    ordered_details = {name: audit.details[name] for name in ordered_gates}
    return {
        "schema": "HCS-C29-INDEPENDENT-CHECK-v1",
        "certificate_sha256": certificate_sha,
        "payload_sha256": envelope["payload_sha256"],
        "all_pass": all(status == "PASS" for status in audit.gates.values()) and len(audit.gates) == 14,
        "gates": ordered_gates,
        "gate_details": ordered_details,
        "summary": {
            "exact_N6": 24,
            "C26_marked_N24_lower_bound": 48,
            "C25_norm_bound": 3,
            "C26_norm_bound": 5,
            "natural_extension_escape": "FAIL_GERM_EQUALS_ONE",
            "symmetric_groupoid_algebraic_reopening": "PASS_EXACT",
        },
    }


def main() -> None:
    args = parse_args()
    report: dict[str, object]
    try:
        report = run(args.certificate)
    except Exception as exc:
        report = {
            "schema": "HCS-C29-INDEPENDENT-CHECK-v1",
            "all_pass": False,
            "fatal_error": f"{type(exc).__name__}: {exc}",
            "gates": getattr(exc, "audit_gates", {}),
            "gate_details": getattr(exc, "audit_details", {}),
        }
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(json.dumps(report, indent=2, sort_keys=True))
        raise SystemExit(1) from exc
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))
    if not report["all_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
