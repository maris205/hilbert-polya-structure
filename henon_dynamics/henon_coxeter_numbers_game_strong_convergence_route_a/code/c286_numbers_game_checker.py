#!/usr/bin/env python3
"""Producer-independent root/inversion/coset checker for HCS-C286."""
from __future__ import annotations

import hashlib
import json
import os
import re
from collections import defaultdict, deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = Path(os.environ.get("C286_EVIDENCE", ROOT / "results/c286_numbers_game_evidence.json"))
SOURCE = "3878fa5282ca89f75700b3ef9d623f54dcb7bcf9"
EVAL = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH = 1788307200
checks = 0

EXPECTED_CASES: dict[str, tuple[tuple[str, ...], tuple[int, ...]]] = {
    "a1_strict": (("A1",), (3,)),
    "a1_zero": (("A1",), (0,)),
    "a2_strict": (("A2",), (1, 2)),
    "a2_wall": (("A2",), (1, 0)),
    "a3_strict": (("A3",), (1, 2, 3)),
    "a3_wall": (("A3",), (1, 0, 2)),
    "a4_strict": (("A4",), (1, 2, 1, 3)),
    "a4_wall": (("A4",), (1, 0, 2, 0)),
    "b2_strict": (("B2",), (1, 2)),
    "b2_wall": (("B2",), (1, 0)),
    "b3_strict": (("B3",), (1, 2, 1)),
    "b3_wall": (("B3",), (0, 1, 0)),
    "c2_strict": (("C2",), (1, 2)),
    "c2_wall": (("C2",), (1, 0)),
    "c3_strict": (("C3",), (1, 2, 1)),
    "c3_wall": (("C3",), (0, 1, 0)),
    "d4_strict": (("D4",), (1, 2, 1, 3)),
    "d4_wall": (("D4",), (1, 0, 0, 2)),
    "g2_strict": (("G2",), (1, 2)),
    "g2_wall": (("G2",), (1, 0)),
    "a2_plus_a1_strict": (("A2", "A1"), (1, 2, 3)),
    "a2_plus_a1_wall": (("A2", "A1"), (1, 0, 2)),
    "a3_zero": (("A3",), (0, 0, 0)),
}

TOP_KEYS = {
    "analytic_proof_obligations", "candidate_id", "collision_contract",
    "evaluation_date", "evaluator", "fixed_epoch", "headline",
    "model_contract", "nonclaims", "payload_sha256", "proof_contract",
    "regression", "route_a", "schema", "scope_flags", "scope_literal",
    "source_commit", "theorem_contract",
}
REGRESSION_KEYS = {"case_rows", "branch_rows", "level_rows", "boundary_rows", "counts"}
CASE_KEYS = {
    "case", "components", "rank", "cartan", "initial_coordinates", "zero_set",
    "strict_dominant", "zero_vector", "disconnected", "observed_length",
    "observed_terminal_coordinates", "complete_branch_count", "branch_sha256",
}
BRANCH_KEYS = {"case", "branch_index", "sequence", "length", "terminal_coordinates"}
LEVEL_KEYS = {
    "case", "depth", "word_prefixes", "distinct_states",
    "outgoing_legal_edges_from_states", "terminal_words",
}
BOUNDARY_KEYS = {"face", "status"}

EXPECTED_MODEL = {
    "root_system": "finite reduced crystallographic root system Phi with chosen simple roots and coroots",
    "position": "dominant weight lambda with coordinates x_i=<lambda,alpha_i^vee> >= 0",
    "legal_move": "fire i only when x_i>0 and replace lambda by s_i lambda",
    "coordinate_update": "x'_j=x_j-A_{j i}x_i for A_{i j}=<alpha_j,alpha_i^vee>",
    "word_convention": "sequence i_1,...,i_m accumulates as s_{i_m}...s_{i_1}",
    "scope": "finite crystallographic systems only; affine and indefinite systems are stopping boundaries",
}
EXPECTED_THEOREM = {
    "zero_set": "J={i:<lambda,alpha_i^vee>=0}; W_J fixes lambda",
    "terminal": "every legal play ends at w_0 lambda in the closed anti-dominant chamber",
    "length": "every play has |Phi+|-|Phi_J+| moves",
    "cumulative_element": "every complete play multiplies to the unique longest/minimal right-coset representative w_0 w_J in W^J",
    "strict_face": "J empty gives w_0 and |Phi+| moves",
    "zero_face": "lambda=0 gives w_0w_J=e and zero moves",
    "product_face": "disconnected components contribute additively and their legal plays interleave",
}
EXPECTED_BOUNDARIES = {
    "strict_dominant": "J is empty; every play has length |Phi+| and cumulative element w0",
    "wall_position": "J is the zero-coordinate set; length loses exactly |Phi_J+|",
    "zero_vector": "J is all nodes; no legal firing, length zero, terminal zero",
    "disconnected_system": "component games interleave; lengths add and the terminal is the product anti-dominant point",
    "rank_one_positive": "type A1 fires once and sends x>0 to -x",
    "rank_one_zero": "type A1 at x=0 has no legal move",
    "strict_positive_rule": "a zero coordinate is never legal; replacing >0 by >=0 changes the game",
    "scope_stop": "only finite reduced crystallographic root systems are claimed; no affine or indefinite theorem is imported",
}
EXPECTED_SCOPE_FLAGS = {
    "arithmetic_local_data": False,
    "euler_factors": False,
    "root_numbers": False,
    "automorphy": False,
    "target_divisor_or_counting_law": False,
    "target_functional_equation": False,
    "target_zero_match": False,
    "hilbert_polya_operator": False,
    "route_b_authorization": False,
}
EXPECTED_HEADLINE = (
    "For every dominant position in a finite crystallographic Weyl system, "
    "all legal positive-coordinate firing sequences terminate at the same "
    "anti-dominant point with the same parabolic-coset length."
)
EXPECTED_PROOF = {
    "status": "PROVABLE AS STATED",
    "scope": "all dominant positions in all finite reduced crystallographic root systems, including reducible systems",
    "mechanism": "legal firing is a left weak-order ascent inside W^J; the finite quotient has unique maximum w_0w_J",
    "finite_evidence_role": "complete small-type branch enumeration is regression evidence, not the all-system proof",
}
EXPECTED_ANALYTIC_OBLIGATIONS = [
    "derive the coordinate reflection rule from the weight-coroot pairing",
    "identify the wall stabilizer W_J and minimal right-coset representatives W^J",
    "prove every legal firing is a strict left weak-order ascent remaining in W^J",
    "prove a play stops only at the unique anti-dominant orbit representative",
    "derive l(w_0w_J)=|Phi+|-|Phi_J+|",
    "close strict, wall, zero, disconnected, and rank-one faces",
    "stop explicitly at the finite crystallographic boundary",
]
EXPECTED_COLLISION = {
    "registry_range": "HCS-C1 through HCS-C283 plus current frozen assignments",
    "closest_distinctions": [
        "C192 is a stochastic face-semigroup chamber walk, not legal Coxeter reflection reduction",
        "C185 is a continuous isospectral matrix-sorting flow, not a finite firing game",
        "C187 and C209 are finite cyclic-sieving permutations, not weak-order confluence",
        "C204 classifies finite-field linear endomorphisms, not real root-system chamber dynamics",
    ],
}
EXPECTED_NONCLAIMS = [
    "The theorem and its strong-convergence mechanism are classical; no literature-priority claim is made.",
    "No affine, indefinite, Kac--Moody, noncrystallographic, or arbitrary generalized-Cartan extension is claimed.",
    "Reduced firing words are not relabelled as rational primes, periodic orbits, Euler factors, or target zeros.",
    "The natural reflection representation is not promoted to a same-clock Hilbert--Polya operator.",
    "Finite branch enumeration tests conventions but does not prove the all-system theorem.",
]
EXPECTED_ROUTE = {
    "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
    "overall": "ROUTE_A_REJECTED",
    "route_b_invocation_allowed": False,
}


def claim(condition: bool) -> None:
    global checks
    assert condition
    checks += 1


def reject_duplicate_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    """Construct one JSON object while rejecting duplicate keys at any depth."""
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key!r}")
        result[key] = value
    return result


def load_unique_json(path: Path) -> dict:
    data = json.loads(path.read_text(), object_pairs_hook=reject_duplicate_object)
    if type(data) is not dict:
        raise ValueError("top-level JSON value must be an object")
    return data


def strict_int(value: object) -> bool:
    """JSON booleans compare equal to 0/1, so exact integer gates need this."""
    return type(value) is int


def payload_hash(data: dict) -> str:
    clean = dict(data)
    clean.pop("payload_sha256", None)
    raw = json.dumps(clean, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def irreducible_cartan(label: str) -> tuple[tuple[int, ...], ...]:
    kind, rank = label[0], int(label[1:])
    if kind == "A":
        claim(rank >= 1)
        matrix = [[2 if i == j else 0 for j in range(rank)] for i in range(rank)]
        for i in range(rank - 1):
            matrix[i][i + 1] = matrix[i + 1][i] = -1
    elif kind in {"B", "C"}:
        claim(rank >= 2)
        matrix = [[2 if i == j else 0 for j in range(rank)] for i in range(rank)]
        for i in range(rank - 1):
            matrix[i][i + 1] = matrix[i + 1][i] = -1
        matrix[rank - 1][rank - 2] = -2 if kind == "B" else -1
        matrix[rank - 2][rank - 1] = -1 if kind == "B" else -2
    elif kind == "D":
        claim(rank >= 4)
        matrix = [[2 if i == j else 0 for j in range(rank)] for i in range(rank)]
        for i in range(rank - 3):
            matrix[i][i + 1] = matrix[i + 1][i] = -1
        matrix[rank - 3][rank - 2] = matrix[rank - 2][rank - 3] = -1
        matrix[rank - 3][rank - 1] = matrix[rank - 1][rank - 3] = -1
    elif kind == "G":
        claim(rank == 2)
        matrix = [[2, -1], [-3, 2]]
    else:
        raise AssertionError(label)
    return tuple(tuple(row) for row in matrix)


def block_cartan(labels: tuple[str, ...]) -> tuple[tuple[int, ...], ...]:
    blocks = [irreducible_cartan(label) for label in labels]
    rank = sum(len(block) for block in blocks)
    answer = [[0] * rank for _ in range(rank)]
    offset = 0
    for block in blocks:
        for i, row in enumerate(block):
            for j, value in enumerate(row):
                answer[offset + i][offset + j] = value
        offset += len(block)
    return tuple(tuple(row) for row in answer)


Matrix = tuple[tuple[int, ...], ...]
Vector = tuple[int, ...]


def identity(rank: int) -> Matrix:
    return tuple(tuple(int(i == j) for j in range(rank)) for i in range(rank))


def matmul(left: Matrix, right: Matrix) -> Matrix:
    rank = len(left)
    return tuple(tuple(sum(left[i][k] * right[k][j] for k in range(rank)) for j in range(rank)) for i in range(rank))


def matvec(matrix: Matrix, vector: Vector) -> Vector:
    return tuple(sum(a * b for a, b in zip(row, vector)) for row in matrix)


def root_reflection(cartan: Matrix, node: int) -> Matrix:
    matrix = [list(row) for row in identity(len(cartan))]
    for column in range(len(cartan)):
        matrix[node][column] -= cartan[node][column]
    return tuple(tuple(row) for row in matrix)


def weight_reflection(cartan: Matrix, node: int) -> Matrix:
    matrix = [list(row) for row in identity(len(cartan))]
    for row in range(len(cartan)):
        matrix[row][node] -= cartan[row][node]
    return tuple(tuple(row) for row in matrix)


def is_positive(root: Vector) -> bool:
    return any(root) and all(coefficient >= 0 for coefficient in root)


def is_negative(root: Vector) -> bool:
    return any(root) and all(coefficient <= 0 for coefficient in root)


def root_system(cartan: Matrix) -> tuple[set[Vector], tuple[Vector, ...]]:
    rank = len(cartan)
    reflections = [root_reflection(cartan, node) for node in range(rank)]
    roots: set[Vector] = set()
    queue: deque[Vector] = deque()
    for node in range(rank):
        for sign in (-1, 1):
            root = tuple(sign * int(node == j) for j in range(rank))
            roots.add(root)
            queue.append(root)
    while queue:
        root = queue.popleft()
        for reflection in reflections:
            image = matvec(reflection, root)
            if image not in roots:
                roots.add(image)
                queue.append(image)
                claim(len(roots) < 10000)
    claim(all(is_positive(root) or is_negative(root) for root in roots))
    positive = tuple(sorted(root for root in roots if is_positive(root)))
    claim(len(roots) == 2 * len(positive))
    return roots, positive


def weyl_group(cartan: Matrix, generators: tuple[int, ...]) -> set[Matrix]:
    reflections = [root_reflection(cartan, node) for node in range(len(cartan))]
    unit = identity(len(cartan))
    group = {unit}
    queue = deque([unit])
    while queue:
        element = queue.popleft()
        for node in generators:
            image = matmul(reflections[node], element)
            if image not in group:
                group.add(image)
                queue.append(image)
                claim(len(group) < 100000)
    return group


def inversion_length(element: Matrix, positive_roots: tuple[Vector, ...]) -> int:
    return sum(is_negative(matvec(element, root)) for root in positive_roots)


def branch_digest(words: tuple[tuple[int, ...], ...]) -> str:
    payload = [[node + 1 for node in word] for word in sorted(words)]
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def apply_weight_word(cartan: Matrix, initial: Vector, word: tuple[int, ...]) -> Vector:
    action = identity(len(cartan))
    for node in word:
        action = matmul(weight_reflection(cartan, node), action)
    return matvec(action, initial)


def group_reconstruction(cartan: Matrix, zero_set: tuple[int, ...]) -> dict:
    rank = len(cartan)
    simple = [tuple(int(i == j) for i in range(rank)) for j in range(rank)]
    reflections = [root_reflection(cartan, node) for node in range(rank)]
    _, positive = root_system(cartan)
    group = weyl_group(cartan, tuple(range(rank)))
    lengths = {element: inversion_length(element, positive) for element in group}
    longest_length = max(lengths.values())
    longest = [element for element, length in lengths.items() if length == longest_length]
    claim(len(longest) == 1)
    w0 = longest[0]
    parabolic = weyl_group(cartan, zero_set)
    parabolic_lengths = {element: inversion_length(element, positive) for element in parabolic}
    wj_length = max(parabolic_lengths.values())
    wj_candidates = [element for element, length in parabolic_lengths.items() if length == wj_length]
    claim(len(wj_candidates) == 1)
    wj = wj_candidates[0]
    target = matmul(w0, wj)
    target_length = lengths[target]
    parabolic_positive = tuple(root for root in positive if all(root[i] == 0 for i in range(rank) if i not in zero_set))
    claim(longest_length == len(positive))
    claim(wj_length == len(parabolic_positive))
    claim(target_length == len(positive) - len(parabolic_positive))

    minimal_reps = {
        element for element in group
        if all(is_positive(matvec(element, simple[node])) for node in zero_set)
    }
    claim(target in minimal_reps)
    claim(max(lengths[element] for element in minimal_reps) == target_length)
    claim(sum(lengths[element] == target_length for element in minimal_reps) == 1)

    current: dict[Matrix, tuple[tuple[int, ...], ...]] = {identity(rank): ((),)}
    levels: list[dict] = []
    for depth in range(target_length + 1):
        claim(all(lengths[element] == depth for element in current))
        outgoing = 0
        next_level: dict[Matrix, list[tuple[int, ...]]] = defaultdict(list)
        if depth < target_length:
            for element, words in current.items():
                for node, reflection in enumerate(reflections):
                    image = matmul(reflection, element)
                    if image in minimal_reps and lengths[image] == depth + 1:
                        outgoing += 1
                        next_level[image].extend(word + (node,) for word in words)
        levels.append({
            "depth": depth,
            "word_prefixes": sum(len(words) for words in current.values()),
            "distinct_states": len(current),
            "outgoing_legal_edges_from_states": outgoing,
            "terminal_words": sum(len(words) for words in current.values()) if depth == target_length else 0,
        })
        if depth < target_length:
            current = {element: tuple(words) for element, words in next_level.items()}
    claim(set(current) == {target})
    words = tuple(sorted(current[target]))
    for word in words:
        product = identity(rank)
        for node in word:
            product = matmul(reflections[node], product)
        claim(product == target)
    return {
        "positive_root_count": len(positive),
        "parabolic_positive_count": len(parabolic_positive),
        "weyl_order": len(group),
        "parabolic_order": len(parabolic),
        "target_length": target_length,
        "target": target,
        "words": words,
        "levels": levels,
    }


def main() -> None:
    data = load_unique_json(EVIDENCE)
    claim(type(data) is dict)
    claim(set(data) == TOP_KEYS)
    claim(data["payload_sha256"] == payload_hash(data))
    claim(data["schema"] == "hcs-c286-coxeter-numbers-game-v1")
    claim(data["candidate_id"] == "HCS-C286")
    claim(data["source_commit"] == SOURCE)
    claim(data["evaluation_date"] == "2026-09-02")
    claim(strict_int(data["fixed_epoch"]) and data["fixed_epoch"] == EPOCH)
    claim(type(data["evaluator"]) is dict and set(data["evaluator"]) == {"version", "sha256"})
    claim(data["evaluator"] == {"version": "0.2.0", "sha256": EVAL})
    claim(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER")
    claim(data["headline"] == EXPECTED_HEADLINE)
    claim(data["scope_flags"] == EXPECTED_SCOPE_FLAGS)
    claim(type(data["scope_flags"]) is dict)
    claim(all(type(value) is bool for value in data["scope_flags"].values()))
    claim(data["model_contract"] == EXPECTED_MODEL)
    claim(data["theorem_contract"] == EXPECTED_THEOREM)
    claim(data["proof_contract"] == EXPECTED_PROOF)
    claim(data["analytic_proof_obligations"] == EXPECTED_ANALYTIC_OBLIGATIONS)
    claim(data["collision_contract"] == EXPECTED_COLLISION)
    claim(data["nonclaims"] == EXPECTED_NONCLAIMS)
    claim(data["route_a"] == EXPECTED_ROUTE)
    claim(type(data["route_a"]) is dict and set(data["route_a"]) == {"tuple", "overall", "route_b_invocation_allowed"})
    claim(type(data["route_a"]["tuple"]) is list and all(type(value) is str for value in data["route_a"]["tuple"]))
    claim(type(data["route_a"]["route_b_invocation_allowed"]) is bool)
    claim(type(data["model_contract"]) is dict and set(data["model_contract"]) == set(EXPECTED_MODEL))
    claim(type(data["theorem_contract"]) is dict and set(data["theorem_contract"]) == set(EXPECTED_THEOREM))
    claim(type(data["proof_contract"]) is dict and set(data["proof_contract"]) == set(EXPECTED_PROOF))
    claim(type(data["analytic_proof_obligations"]) is list and all(type(value) is str for value in data["analytic_proof_obligations"]))
    claim(type(data["collision_contract"]) is dict and set(data["collision_contract"]) == {"registry_range", "closest_distinctions"})
    claim(type(data["collision_contract"]["closest_distinctions"]) is list and all(type(value) is str for value in data["collision_contract"]["closest_distinctions"]))
    claim(type(data["nonclaims"]) is list and all(type(value) is str for value in data["nonclaims"]))

    regression = data["regression"]
    claim(type(regression) is dict)
    claim(set(regression) == REGRESSION_KEYS)
    case_rows = regression["case_rows"]
    branch_rows = regression["branch_rows"]
    level_rows = regression["level_rows"]
    boundary_rows = regression["boundary_rows"]
    claim(regression["counts"] == {
        "case_rows": len(case_rows), "branch_rows": len(branch_rows),
        "level_rows": len(level_rows), "boundary_rows": len(boundary_rows),
    })
    claim(type(regression["counts"]) is dict and set(regression["counts"]) == {"case_rows", "branch_rows", "level_rows", "boundary_rows"})
    claim(all(strict_int(value) for value in regression["counts"].values()))
    claim(all(type(rows) is list for rows in (case_rows, branch_rows, level_rows, boundary_rows)))
    claim(len(case_rows) == len(EXPECTED_CASES) == 23)
    claim(len(branch_rows) == 3332)
    claim(len(level_rows) == 143)
    claim(len(boundary_rows) == 8)
    claim(all(type(row) is dict and set(row) == CASE_KEYS for row in case_rows))
    claim(all(type(row) is dict and set(row) == BRANCH_KEYS for row in branch_rows))
    claim(all(type(row) is dict and set(row) == LEVEL_KEYS for row in level_rows))
    claim(all(type(row) is dict and set(row) == BOUNDARY_KEYS for row in boundary_rows))
    claim(all(
        type(row["case"]) is str
        and type(row["components"]) is list
        and row["components"]
        and all(type(value) is str for value in row["components"])
        and strict_int(row["rank"])
        and row["rank"] > 0
        and type(row["cartan"]) is list
        and len(row["cartan"]) == row["rank"]
        and all(type(line) is list and len(line) == row["rank"] and all(strict_int(value) for value in line) for line in row["cartan"])
        and type(row["initial_coordinates"]) is list
        and len(row["initial_coordinates"]) == row["rank"]
        and all(strict_int(value) for value in row["initial_coordinates"])
        and type(row["zero_set"]) is list
        and all(strict_int(value) for value in row["zero_set"])
        and type(row["strict_dominant"]) is bool
        and type(row["zero_vector"]) is bool
        and type(row["disconnected"]) is bool
        and strict_int(row["observed_length"])
        and row["observed_length"] >= 0
        and type(row["observed_terminal_coordinates"]) is list
        and len(row["observed_terminal_coordinates"]) == row["rank"]
        and all(strict_int(value) for value in row["observed_terminal_coordinates"])
        and strict_int(row["complete_branch_count"])
        and row["complete_branch_count"] >= 1
        and type(row["branch_sha256"]) is str
        and re.fullmatch(r"[0-9a-f]{64}", row["branch_sha256"]) is not None
        for row in case_rows
    ))
    claim(all(
        type(row["case"]) is str
        and strict_int(row["branch_index"])
        and row["branch_index"] >= 0
        and type(row["sequence"]) is list
        and all(strict_int(value) for value in row["sequence"])
        and strict_int(row["length"])
        and row["length"] >= 0
        and type(row["terminal_coordinates"]) is list
        and all(strict_int(value) for value in row["terminal_coordinates"])
        for row in branch_rows
    ))
    claim(all(
        type(row["case"]) is str
        and all(strict_int(row[key]) and row[key] >= 0 for key in LEVEL_KEYS - {"case"})
        for row in level_rows
    ))
    claim(all(type(row["face"]) is str and type(row["status"]) is str for row in boundary_rows))
    case_order = {name: index for index, name in enumerate(EXPECTED_CASES)}
    claim([case_order[row["case"]] for row in branch_rows] == sorted(case_order[row["case"]] for row in branch_rows))
    claim([case_order[row["case"]] for row in level_rows] == sorted(case_order[row["case"]] for row in level_rows))

    case_map = {row["case"]: row for row in case_rows}
    claim(len(case_map) == len(case_rows))
    claim(tuple(case_map) == tuple(EXPECTED_CASES))
    branches_by_case: dict[str, list[dict]] = defaultdict(list)
    levels_by_case: dict[str, list[dict]] = defaultdict(list)
    branch_keys = [(row["case"], row["branch_index"]) for row in branch_rows]
    level_keys = [(row["case"], row["depth"]) for row in level_rows]
    claim(len(branch_keys) == len(set(branch_keys)))
    claim(len(level_keys) == len(set(level_keys)))
    for row in branch_rows:
        claim(row["case"] in EXPECTED_CASES)
        branches_by_case[row["case"]].append(row)
    for row in level_rows:
        claim(row["case"] in EXPECTED_CASES)
        levels_by_case[row["case"]].append(row)

    expected_branch_keys: set[tuple[str, int]] = set()
    expected_level_keys: set[tuple[str, int]] = set()
    for name, (labels, initial) in EXPECTED_CASES.items():
        row = case_map[name]
        cartan = block_cartan(labels)
        zero_set = tuple(i for i, coordinate in enumerate(initial) if coordinate == 0)
        claim(row["components"] == list(labels))
        claim(row["rank"] == len(initial))
        claim(row["cartan"] == [list(line) for line in cartan])
        claim(row["initial_coordinates"] == list(initial))
        claim(row["zero_set"] == list(zero_set))
        claim(row["strict_dominant"] is all(coordinate > 0 for coordinate in initial))
        claim(row["zero_vector"] is all(coordinate == 0 for coordinate in initial))
        claim(row["disconnected"] is (len(labels) > 1))

        reconstructed = group_reconstruction(cartan, zero_set)
        words = reconstructed["words"]
        expected_branch_keys.update((name, index) for index in range(len(words)))
        expected_level_keys.update((name, depth) for depth in range(reconstructed["target_length"] + 1))
        claim(row["observed_length"] == reconstructed["target_length"])
        claim(row["complete_branch_count"] == len(words))
        claim(row["branch_sha256"] == branch_digest(words))
        expected_terminal = apply_weight_word(cartan, initial, words[0])
        claim(all(coordinate <= 0 for coordinate in expected_terminal))
        claim(row["observed_terminal_coordinates"] == list(expected_terminal))

        stored_branches = branches_by_case[name]
        claim(len(stored_branches) == len(words))
        claim([branch["branch_index"] for branch in stored_branches] == list(range(len(words))))
        stored_words = tuple(tuple(node - 1 for node in branch["sequence"]) for branch in stored_branches)
        claim(len(set(stored_words)) == len(stored_words))
        claim(stored_words == words)
        for branch, word in zip(stored_branches, words):
            claim(all(0 <= node < len(initial) for node in word))
            claim(branch["length"] == reconstructed["target_length"] == len(word))
            claim(branch["terminal_coordinates"] == list(expected_terminal))

        stored_levels = levels_by_case[name]
        claim(len(stored_levels) == reconstructed["target_length"] + 1)
        claim([level["depth"] for level in stored_levels] == list(range(len(stored_levels))))
        for stored, expected in zip(stored_levels, reconstructed["levels"]):
            claim({key: stored[key] for key in expected} == expected)

        if not zero_set:
            claim(row["observed_length"] == reconstructed["positive_root_count"])
        if len(zero_set) == len(initial):
            claim(row["observed_length"] == 0 and expected_terminal == initial)

    claim(set(branch_keys) == expected_branch_keys)
    claim(set(level_keys) == expected_level_keys)

    boundary_map = {row["face"]: row["status"] for row in boundary_rows}
    claim(len(boundary_map) == len(boundary_rows))
    claim(tuple(boundary_map) == tuple(EXPECTED_BOUNDARIES))
    claim(boundary_map == EXPECTED_BOUNDARIES)

    # Explicit semantic sentinels for the mandated faces.
    claim(case_map["a1_strict"]["observed_length"] == 1)
    claim(case_map["a1_strict"]["observed_terminal_coordinates"] == [-3])
    claim(case_map["a1_zero"]["observed_length"] == 0)
    claim(case_map["a3_zero"]["complete_branch_count"] == 1)
    claim(case_map["a4_strict"]["observed_length"] == 10)
    claim(case_map["b3_strict"]["observed_length"] == 9)
    claim(case_map["c3_strict"]["observed_length"] == 9)
    claim(case_map["d4_strict"]["observed_length"] == 12)
    claim(case_map["g2_strict"]["observed_length"] == 6)
    claim(case_map["a2_plus_a1_strict"]["observed_length"] == 4)
    claim(case_map["a2_plus_a1_strict"]["complete_branch_count"] == 8)

    print(f"C286 independent checker: PASS ({checks} assertions; positive-root/inversion/coset reconstruction)")


if __name__ == "__main__":
    main()
