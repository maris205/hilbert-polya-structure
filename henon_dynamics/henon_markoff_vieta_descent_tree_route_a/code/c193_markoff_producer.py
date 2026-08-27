#!/usr/bin/env python3
"""Produce the exact C193 Markoff--Vieta descent-tree ledger."""
from __future__ import annotations

from collections import deque
from hashlib import sha256
import json
import math
import os
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = Path(os.environ.get("C193_OUTPUT", ROOT / "results/c193_markoff_evidence.json"))
SOURCE_COMMIT = "4d7b214759f7ff982c0b19e662918acd307e0f58"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
ROOT_TRIPLE = (1, 1, 1)


def normalized(values: Iterable[int]) -> tuple[int, int, int]:
    triple = tuple(sorted(values))
    if len(triple) != 3:
        raise ValueError(triple)
    return triple  # type: ignore[return-value]


def is_markoff(triple: tuple[int, int, int]) -> bool:
    x, y, z = triple
    return x > 0 and x <= y <= z and x * x + y * y + z * z == 3 * x * y * z


def mutate(triple: tuple[int, int, int], coordinate: int) -> tuple[int, int, int]:
    values = list(triple)
    i, j = [index for index in range(3) if index != coordinate]
    values[coordinate] = 3 * values[i] * values[j] - values[coordinate]
    return normalized(values)


def descent_parent(triple: tuple[int, int, int]) -> tuple[int, int, int] | None:
    if triple == ROOT_TRIPLE:
        return None
    maximum = max(triple)
    if triple.count(maximum) != 1:
        raise AssertionError(f"non-root maximum is not unique: {triple}")
    coordinate = triple.index(maximum)
    parent = mutate(triple, coordinate)
    if not is_markoff(parent) or max(parent) >= maximum:
        raise AssertionError((triple, parent))
    return parent


def forward_children(triple: tuple[int, int, int]) -> list[tuple[int, int, int]]:
    children = set()
    height = max(triple)
    for coordinate in range(3):
        child = mutate(triple, coordinate)
        if min(child) > 0 and is_markoff(child) and max(child) > height:
            children.add(child)
    return sorted(children)


def triple_strings(triple: tuple[int, int, int] | None) -> list[str] | None:
    return None if triple is None else [str(value) for value in triple]


def bfs_depth(max_depth: int) -> tuple[list[dict[str, object]], dict[tuple[int, int, int], int]]:
    queue = deque([ROOT_TRIPLE])
    depth = {ROOT_TRIPLE: 0}
    parent: dict[tuple[int, int, int], tuple[int, int, int] | None] = {ROOT_TRIPLE: None}
    word = {ROOT_TRIPLE: ""}
    while queue:
        triple = queue.popleft()
        current_depth = depth[triple]
        if current_depth == max_depth:
            continue
        for branch, child in enumerate(forward_children(triple)):
            if child in depth:
                if parent[child] != triple:
                    raise AssertionError(f"two parents: {child}")
                continue
            check_parent = descent_parent(child)
            if check_parent != triple:
                raise AssertionError((triple, child, check_parent))
            depth[child] = current_depth + 1
            parent[child] = triple
            word[child] = word[triple] + str(branch)
            queue.append(child)
    rows = []
    for triple in sorted(depth, key=lambda item: (depth[item], item)):
        children = forward_children(triple)
        rows.append({
            "triple": triple_strings(triple),
            "depth": depth[triple],
            "local_child_rank_word": word[triple],
            "parent": triple_strings(parent[triple]),
            "children": [triple_strings(child) for child in children],
            "height": str(max(triple)),
            "coordinate_sum": str(sum(triple)),
            "unique_maximum": triple == ROOT_TRIPLE or triple.count(max(triple)) == 1,
        })
    return rows, depth


def brute_bounded(bound: int) -> list[tuple[int, int, int]]:
    solutions = set()
    for x in range(1, bound + 1):
        for y in range(x, bound + 1):
            discriminant = 9 * x * x * y * y - 4 * (x * x + y * y)
            if discriminant < 0:
                continue
            root = math.isqrt(discriminant)
            if root * root != discriminant:
                continue
            for sign in (-1, 1):
                numerator = 3 * x * y + sign * root
                if numerator % 2:
                    continue
                z = numerator // 2
                triple = (x, y, z)
                if y <= z <= bound and is_markoff(triple):
                    solutions.add(triple)
    return sorted(solutions)


def bfs_bounded(bound: int) -> list[tuple[int, int, int]]:
    queue = deque([ROOT_TRIPLE])
    seen = {ROOT_TRIPLE}
    while queue:
        triple = queue.popleft()
        for child in forward_children(triple):
            if max(child) <= bound and child not in seen:
                seen.add(child)
                queue.append(child)
    return sorted(seen)


def trace_to_root(triple: tuple[int, int, int]) -> list[tuple[int, int, int]]:
    trace = [triple]
    while trace[-1] != ROOT_TRIPLE:
        parent = descent_parent(trace[-1])
        assert parent is not None
        trace.append(parent)
    return trace


def payload_digest(data: dict[str, object]) -> str:
    raw = json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def main() -> None:
    max_depth = 10
    rows, depth_map = bfs_depth(max_depth)
    row_triples = [tuple(int(value) for value in row["triple"]) for row in rows]
    bound = 2000
    brute = brute_bounded(bound)
    generated = bfs_bounded(bound)
    if brute != generated:
        raise AssertionError("bounded brute/BFS mismatch")

    trace_seeds = []
    for depth in range(max_depth + 1):
        level = [triple for triple in row_triples if depth_map[triple] == depth]
        trace_seeds.extend(level[:1] + (level[-1:] if len(level) > 1 else []))
    traces = [
        {"seed": triple_strings(seed), "depth": depth_map[seed], "trace": [triple_strings(item) for item in trace_to_root(seed)]}
        for seed in trace_seeds
    ]
    involution_test_count = 0
    for triple in row_triples:
        for coordinate in range(3):
            child = mutate(triple, coordinate)
            if min(child) <= 0:
                continue
            assert is_markoff(child)
            # Coordinate labels are lost after sorting; polynomial involutivity
            # is reconstructed separately by SymPy.  This loop checks invariance.
            involution_test_count += 1

    data: dict[str, object] = {
        "schema": "hcs-c193-markoff-vieta-evidence-v1",
        "candidate_id": "HCS-C193",
        "date_utc": "2026-08-27",
        "source_commit": SOURCE_COMMIT,
        "evaluator": {"version": "0.2.0", "path": "flow_systems/skills/route-a-evaluator.md", "sha256": EVALUATOR_SHA256},
        "scope_literal": SCOPE,
        "source_lock": {
            "object": "sorted positive integer solutions of x^2+y^2+z^2=3xyz",
            "phase_space": "normalized Markoff triples x<=y<=z",
            "dynamics": "replace the unique largest coordinate by the other Vieta root and sort",
            "clock": "one strict Vieta descent",
            "normalization": "coordinate permutation quotient with positive sorted representative",
            "parameter_provenance": "the coefficient 3 and integer equation; never target tables",
            "determinant_convention": "none",
            "precision": "exact unbounded integer and SymPy polynomial arithmetic",
            "allowed_data": "positive Markoff triples, Vieta involutions, heights, paths and finite integer bounds",
            "forbidden_data": "mod-p graphs, prime or zero tables, arithmetic local data, Euler factors, root numbers, automorphy, Hilbert--Polya and Route B",
        },
        "attribution": {
            "markoff_owned": "the classical Diophantine equation and reduction genealogy",
            "bombieri_owned": "modern Markoff-tree and continued-fraction account",
            "bgs_owned": "the Vieta-involution orbit statement and explicit distinction from modular strong approximation",
            "package_derived": "a deterministic largest-coordinate descent formulation, exact termination certificate and executable tree/brute-force collision oracle",
        },
        "source_registry": [
            {
                "source_id": "M79",
                "authors": ["Andrey Markoff"],
                "title": "Sur les formes quadratiques binaires indefinies",
                "venue": "Mathematische Annalen 15, 381--406",
                "year": 1879,
                "doi": "10.1007/BF02086269",
                "role": "classical source of the equation and reduction theory",
            },
            {
                "source_id": "B07",
                "authors": ["Enrico Bombieri"],
                "title": "Continued fractions and the Markoff tree",
                "venue": "Expositiones Mathematicae 25(3), 187--213",
                "year": 2007,
                "doi": "10.1016/j.exmath.2006.10.002",
                "role": "modern source for the Markoff tree",
            },
            {
                "source_id": "BGS16",
                "authors": ["Jean Bourgain", "Alexander Gamburd", "Peter Sarnak"],
                "title": "Markoff triples and strong approximation",
                "venue": "Comptes Rendus Mathematique 354(2), 131--135",
                "year": 2016,
                "doi": "10.1016/j.crma.2015.12.006",
                "role": "Vieta orbit source and modular-boundary firewall",
            },
        ],
        "theorem": {
            "vieta_invariance": "each coordinate Vieta involution preserves the Markoff polynomial and positive integral solutions when the replacement is positive",
            "unique_largest": "every normalized positive solution other than (1,1,1) has a unique largest coordinate",
            "strict_parent": "replacing that largest coordinate by the other quadratic root yields a positive Markoff triple of strictly smaller height",
            "nonparent_edges": "before sorting, mutating either nonmaximal coordinate produces a positive solution of strictly larger height, so every Vieta edge is oriented by the parent rule",
            "termination": "integer height is a strict Lyapunov function, so every descent reaches (1,1,1) in finitely many steps",
            "generation": "reversing the parent edges generates every positive solution from the root",
            "tree": "after quotienting coordinate permutations, the positive-solution graph is a rooted tree with the descent map as unique parent",
            "recurrence_boundary": "the autonomous descent has no non-root periodic orbit; the three labelled coordinate Vieta generators before sorting and permutation quotient remain involutions",
        },
        "route_a": {
            "tuple": ["A0_WEAK_ARITHMETIC_RELATION", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "a0_reason": "the integer cubic and its Vieta dynamics are intrinsic Diophantine data, but they produce no rational-prime primitive carrier, prime-power repetition or logarithmic clock",
            "a1_reason": "strict descent terminates and has no nonconstant primitive periodic orbits",
            "a2_reason": "the rooted tree supplies no source-native dynamical determinant with a target divisor",
            "a3_reason": "no target continuation, functional equation, counting law or Weil compression follows",
            "a4_reason": "adjacency or Koopman operators on the tree are formal choices, not a target self-adjoint quantization",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": {
            "target_zero_table_used": False,
            "target_prime_table_used": False,
            "arithmetic_local_data_used": False,
            "mod_p_graph_used": False,
            "euler_factor_claimed": False,
            "root_number_claimed": False,
            "automorphy_claimed": False,
            "target_divisor_claimed": False,
            "target_functional_equation_claimed": False,
            "hilbert_polya_operator_claimed": False,
            "route_b_invoked": False,
        },
        "progress_and_boundary": {
            "explicit_progress": "the entire positive integer solution set receives a unique terminating parent map and rooted-tree certificate",
            "proof_boundary": "the bounded census is a regression oracle, not the proof of global descent or completeness",
            "arithmetic_boundary": "Diophantine origin earns only A0 weak because primes, powers and log p do not emerge",
            "uniqueness_boundary": "no claim is made that a largest Markoff number determines a unique unordered triple; that Frobenius problem remains open",
            "modular_boundary": "all reductions modulo primes and strong-approximation data are deliberately excluded",
            "frontier_boundary": "depth-ten rows retain every one-step child, including children at depth eleven outside the stored row population; the finite census is not a closed finite tree",
        },
        "finite_regression": {
            "max_depth": max_depth,
            "tree_rows": rows,
            "tree_row_count": len(rows),
            "level_counts": {str(depth): sum(1 for value in depth_map.values() if value == depth) for depth in range(max_depth + 1)},
            "children_are_one_step_complete": True,
            "frontier_child_count": sum(len(forward_children(triple)) for triple in row_triples if depth_map[triple] == max_depth),
            "word_semantics": "each digit is the local lexicographic rank among the normalized forward children; it is not a fixed labelled Vieta-generator word",
            "maximum_coordinate_digits": max(len(str(max(triple))) for triple in row_triples),
            "invariance_tests": involution_test_count,
            "brute_bound": bound,
            "brute_solutions": [triple_strings(triple) for triple in brute],
            "brute_solution_count": len(brute),
            "descent_traces": traces,
            "descent_trace_count": len(traces),
            "descent_steps_checked": sum(len(trace["trace"]) - 1 for trace in traces),
        },
        "nonclaims": [
            "priority for the Markoff equation, Vieta involutions, descent or tree theorem",
            "the Frobenius uniqueness conjecture for Markoff numbers",
            "any statement about Markoff graphs modulo a prime or strong approximation",
            "a rational-prime primitive orbit, prime-power repetition law or logarithmic clock",
            "a target divisor, target functional equation or Hilbert--Polya operator",
            "Route-B authorization, global literature priority, external peer review or an acceptance score",
        ],
    }
    data["payload_sha256"] = payload_digest(data)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C193_PRODUCER_PASS",
        "tree_rows": len(rows),
        "brute_solutions": len(brute),
        "descent_traces": len(traces),
        "payload_sha256": data["payload_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
