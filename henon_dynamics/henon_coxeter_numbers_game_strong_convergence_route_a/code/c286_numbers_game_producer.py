#!/usr/bin/env python3
"""Produce the deterministic HCS-C286 finite Weyl numbers-game receipt."""
from __future__ import annotations

import hashlib
import json
import os
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(os.environ.get("C286_EVIDENCE_OUT", ROOT / "results/c286_numbers_game_evidence.json"))
SOURCE = "3878fa5282ca89f75700b3ef9d623f54dcb7bcf9"
EVAL = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH = 1788307200


def irreducible_cartan(kind: str, rank: int) -> tuple[tuple[int, ...], ...]:
    """Bourbaki-style finite Cartan matrices, with A_ij=<alpha_j,alpha_i^vee>."""
    if kind == "A":
        assert rank >= 1
        matrix = [[2 if i == j else 0 for j in range(rank)] for i in range(rank)]
        for i in range(rank - 1):
            matrix[i][i + 1] = matrix[i + 1][i] = -1
    elif kind in {"B", "C"}:
        assert rank >= 2
        matrix = [[2 if i == j else 0 for j in range(rank)] for i in range(rank)]
        for i in range(rank - 1):
            matrix[i][i + 1] = matrix[i + 1][i] = -1
        if kind == "B":
            matrix[rank - 1][rank - 2] = -2
        else:
            matrix[rank - 2][rank - 1] = -2
    elif kind == "D":
        assert rank >= 4
        matrix = [[2 if i == j else 0 for j in range(rank)] for i in range(rank)]
        for i in range(rank - 3):
            matrix[i][i + 1] = matrix[i + 1][i] = -1
        matrix[rank - 3][rank - 2] = matrix[rank - 2][rank - 3] = -1
        matrix[rank - 3][rank - 1] = matrix[rank - 1][rank - 3] = -1
    elif kind == "G":
        assert rank == 2
        matrix = [[2, -1], [-3, 2]]
    else:
        raise ValueError(kind)
    return tuple(tuple(row) for row in matrix)


def block_cartan(components: tuple[tuple[str, int], ...]) -> tuple[tuple[int, ...], ...]:
    blocks = [irreducible_cartan(kind, rank) for kind, rank in components]
    size = sum(len(block) for block in blocks)
    answer = [[0] * size for _ in range(size)]
    offset = 0
    for block in blocks:
        for i, row in enumerate(block):
            for j, value in enumerate(row):
                answer[offset + i][offset + j] = value
        offset += len(block)
    return tuple(tuple(row) for row in answer)


CASES: dict[str, tuple[tuple[tuple[str, int], ...], tuple[int, ...]]] = {
    "a1_strict": ((('A', 1),), (3,)),
    "a1_zero": ((('A', 1),), (0,)),
    "a2_strict": ((('A', 2),), (1, 2)),
    "a2_wall": ((('A', 2),), (1, 0)),
    "a3_strict": ((('A', 3),), (1, 2, 3)),
    "a3_wall": ((('A', 3),), (1, 0, 2)),
    "a4_strict": ((('A', 4),), (1, 2, 1, 3)),
    "a4_wall": ((('A', 4),), (1, 0, 2, 0)),
    "b2_strict": ((('B', 2),), (1, 2)),
    "b2_wall": ((('B', 2),), (1, 0)),
    "b3_strict": ((('B', 3),), (1, 2, 1)),
    "b3_wall": ((('B', 3),), (0, 1, 0)),
    "c2_strict": ((('C', 2),), (1, 2)),
    "c2_wall": ((('C', 2),), (1, 0)),
    "c3_strict": ((('C', 3),), (1, 2, 1)),
    "c3_wall": ((('C', 3),), (0, 1, 0)),
    "d4_strict": ((('D', 4),), (1, 2, 1, 3)),
    "d4_wall": ((('D', 4),), (1, 0, 0, 2)),
    "g2_strict": ((('G', 2),), (1, 2)),
    "g2_wall": ((('G', 2),), (1, 0)),
    "a2_plus_a1_strict": ((('A', 2), ('A', 1)), (1, 2, 3)),
    "a2_plus_a1_wall": ((('A', 2), ('A', 1)), (1, 0, 2)),
    "a3_zero": ((('A', 3),), (0, 0, 0)),
}


def component_labels(components: tuple[tuple[str, int], ...]) -> list[str]:
    return [f"{kind}{rank}" for kind, rank in components]


def fire(state: tuple[int, ...], cartan: tuple[tuple[int, ...], ...], node: int) -> tuple[int, ...]:
    amplitude = state[node]
    assert amplitude > 0
    return tuple(state[j] - cartan[j][node] * amplitude for j in range(len(state)))


def all_legal_words(
    initial: tuple[int, ...], cartan: tuple[tuple[int, ...], ...]
) -> tuple[tuple[int, ...], ...]:
    """Enumerate every complete legal play; entries are zero-based nodes."""
    @lru_cache(maxsize=None)
    def suffixes(state: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
        legal = [i for i, coordinate in enumerate(state) if coordinate > 0]
        if not legal:
            return ((),)
        answer: list[tuple[int, ...]] = []
        for node in legal:
            for tail in suffixes(fire(state, cartan, node)):
                answer.append((node,) + tail)
        return tuple(answer)

    return suffixes(initial)


def replay(initial: tuple[int, ...], cartan: tuple[tuple[int, ...], ...], word: tuple[int, ...]) -> tuple[int, ...]:
    state = initial
    for node in word:
        state = fire(state, cartan, node)
    return state


def branch_digest(words: tuple[tuple[int, ...], ...]) -> str:
    payload = [[node + 1 for node in word] for word in sorted(words)]
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def level_ledger(
    name: str,
    initial: tuple[int, ...],
    cartan: tuple[tuple[int, ...], ...],
    words: tuple[tuple[int, ...], ...],
) -> list[dict]:
    length = len(words[0])
    rows = []
    for depth in range(length + 1):
        prefixes = {word[:depth] for word in words}
        states = {replay(initial, cartan, prefix) for prefix in prefixes}
        rows.append({
            "case": name,
            "depth": depth,
            "word_prefixes": len(prefixes),
            "distinct_states": len(states),
            "outgoing_legal_edges_from_states": sum(
                sum(coordinate > 0 for coordinate in state) for state in states
            ),
            "terminal_words": len(words) if depth == length else 0,
        })
    return rows


def payload_hash(data: dict) -> str:
    clean = dict(data)
    clean.pop("payload_sha256", None)
    raw = json.dumps(clean, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def build_regression() -> dict:
    case_rows: list[dict] = []
    branch_rows: list[dict] = []
    level_rows: list[dict] = []
    for name, (components, initial) in CASES.items():
        cartan = block_cartan(components)
        words = tuple(sorted(all_legal_words(initial, cartan)))
        lengths = {len(word) for word in words}
        terminals = {replay(initial, cartan, word) for word in words}
        assert len(lengths) == len(terminals) == 1
        length = next(iter(lengths))
        terminal = next(iter(terminals))
        zero_set = [i for i, coordinate in enumerate(initial) if coordinate == 0]
        case_rows.append({
            "case": name,
            "components": component_labels(components),
            "rank": len(initial),
            "cartan": [list(row) for row in cartan],
            "initial_coordinates": list(initial),
            "zero_set": zero_set,
            "strict_dominant": all(coordinate > 0 for coordinate in initial),
            "zero_vector": all(coordinate == 0 for coordinate in initial),
            "disconnected": len(components) > 1,
            "observed_length": length,
            "observed_terminal_coordinates": list(terminal),
            "complete_branch_count": len(words),
            "branch_sha256": branch_digest(words),
        })
        for branch_index, word in enumerate(words):
            branch_rows.append({
                "case": name,
                "branch_index": branch_index,
                "sequence": [node + 1 for node in word],
                "length": len(word),
                "terminal_coordinates": list(replay(initial, cartan, word)),
            })
        level_rows.extend(level_ledger(name, initial, cartan, words))

    boundary_rows = [
        {"face": "strict_dominant", "status": "J is empty; every play has length |Phi+| and cumulative element w0"},
        {"face": "wall_position", "status": "J is the zero-coordinate set; length loses exactly |Phi_J+|"},
        {"face": "zero_vector", "status": "J is all nodes; no legal firing, length zero, terminal zero"},
        {"face": "disconnected_system", "status": "component games interleave; lengths add and the terminal is the product anti-dominant point"},
        {"face": "rank_one_positive", "status": "type A1 fires once and sends x>0 to -x"},
        {"face": "rank_one_zero", "status": "type A1 at x=0 has no legal move"},
        {"face": "strict_positive_rule", "status": "a zero coordinate is never legal; replacing >0 by >=0 changes the game"},
        {"face": "scope_stop", "status": "only finite reduced crystallographic root systems are claimed; no affine or indefinite theorem is imported"},
    ]
    counts = {
        "case_rows": len(case_rows),
        "branch_rows": len(branch_rows),
        "level_rows": len(level_rows),
        "boundary_rows": len(boundary_rows),
    }
    return {
        "case_rows": case_rows,
        "branch_rows": branch_rows,
        "level_rows": level_rows,
        "boundary_rows": boundary_rows,
        "counts": counts,
    }


def main() -> None:
    data = {
        "schema": "hcs-c286-coxeter-numbers-game-v1",
        "candidate_id": "HCS-C286",
        "source_commit": SOURCE,
        "evaluation_date": "2026-09-02",
        "fixed_epoch": EPOCH,
        "evaluator": {"version": "0.2.0", "sha256": EVAL},
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "scope_flags": {
            "arithmetic_local_data": False,
            "euler_factors": False,
            "root_numbers": False,
            "automorphy": False,
            "target_divisor_or_counting_law": False,
            "target_functional_equation": False,
            "target_zero_match": False,
            "hilbert_polya_operator": False,
            "route_b_authorization": False,
        },
        "headline": (
            "For every dominant position in a finite crystallographic Weyl system, "
            "all legal positive-coordinate firing sequences terminate at the same "
            "anti-dominant point with the same parabolic-coset length."
        ),
        "model_contract": {
            "root_system": "finite reduced crystallographic root system Phi with chosen simple roots and coroots",
            "position": "dominant weight lambda with coordinates x_i=<lambda,alpha_i^vee> >= 0",
            "legal_move": "fire i only when x_i>0 and replace lambda by s_i lambda",
            "coordinate_update": "x'_j=x_j-A_{j i}x_i for A_{i j}=<alpha_j,alpha_i^vee>",
            "word_convention": "sequence i_1,...,i_m accumulates as s_{i_m}...s_{i_1}",
            "scope": "finite crystallographic systems only; affine and indefinite systems are stopping boundaries",
        },
        "theorem_contract": {
            "zero_set": "J={i:<lambda,alpha_i^vee>=0}; W_J fixes lambda",
            "terminal": "every legal play ends at w_0 lambda in the closed anti-dominant chamber",
            "length": "every play has |Phi+|-|Phi_J+| moves",
            "cumulative_element": "every complete play multiplies to the unique longest/minimal right-coset representative w_0 w_J in W^J",
            "strict_face": "J empty gives w_0 and |Phi+| moves",
            "zero_face": "lambda=0 gives w_0w_J=e and zero moves",
            "product_face": "disconnected components contribute additively and their legal plays interleave",
        },
        "proof_contract": {
            "status": "PROVABLE AS STATED",
            "scope": "all dominant positions in all finite reduced crystallographic root systems, including reducible systems",
            "mechanism": "legal firing is a left weak-order ascent inside W^J; the finite quotient has unique maximum w_0w_J",
            "finite_evidence_role": "complete small-type branch enumeration is regression evidence, not the all-system proof",
        },
        "analytic_proof_obligations": [
            "derive the coordinate reflection rule from the weight-coroot pairing",
            "identify the wall stabilizer W_J and minimal right-coset representatives W^J",
            "prove every legal firing is a strict left weak-order ascent remaining in W^J",
            "prove a play stops only at the unique anti-dominant orbit representative",
            "derive l(w_0w_J)=|Phi+|-|Phi_J+|",
            "close strict, wall, zero, disconnected, and rank-one faces",
            "stop explicitly at the finite crystallographic boundary",
        ],
        "collision_contract": {
            "registry_range": "HCS-C1 through HCS-C283 plus current frozen assignments",
            "closest_distinctions": [
                "C192 is a stochastic face-semigroup chamber walk, not legal Coxeter reflection reduction",
                "C185 is a continuous isospectral matrix-sorting flow, not a finite firing game",
                "C187 and C209 are finite cyclic-sieving permutations, not weak-order confluence",
                "C204 classifies finite-field linear endomorphisms, not real root-system chamber dynamics",
            ],
        },
        "nonclaims": [
            "The theorem and its strong-convergence mechanism are classical; no literature-priority claim is made.",
            "No affine, indefinite, Kac--Moody, noncrystallographic, or arbitrary generalized-Cartan extension is claimed.",
            "Reduced firing words are not relabelled as rational primes, periodic orbits, Euler factors, or target zeros.",
            "The natural reflection representation is not promoted to a same-clock Hilbert--Polya operator.",
            "Finite branch enumeration tests conventions but does not prove the all-system theorem.",
        ],
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "regression": build_regression(),
    }
    data["payload_sha256"] = payload_hash(data)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    counts = data["regression"]["counts"]
    print(json.dumps({
        "status": "C286_PRODUCER_PASS",
        "payload_sha256": data["payload_sha256"],
        "counts": counts,
        "bytes": OUT.stat().st_size,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
