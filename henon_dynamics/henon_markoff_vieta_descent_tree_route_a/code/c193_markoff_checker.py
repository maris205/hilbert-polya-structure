#!/usr/bin/env python3
"""Independent integer/tree checker for the C193 Markoff evidence."""
from __future__ import annotations

from collections import deque
from hashlib import sha256
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c193_markoff_evidence.json"
SOURCE_COMMIT = "4d7b214759f7ff982c0b19e662918acd307e0f58"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
ORIGIN = (1, 1, 1)
CHECKS = 0
_BOUNDED_CACHE: dict[int, list[tuple[int, int, int]]] = {}


def check(condition: bool, message: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def triple(values: list[str] | None) -> tuple[int, int, int] | None:
    if values is None:
        return None
    result = tuple(int(value) for value in values)
    if len(result) != 3:
        raise AssertionError(values)
    return result  # type: ignore[return-value]


def markoff(values: tuple[int, int, int]) -> bool:
    x, y, z = values
    return 0 < x <= y <= z and x * x + y * y + z * z == 3 * x * y * z


def replace(values: tuple[int, int, int], coordinate: int) -> tuple[int, int, int]:
    mutable = list(values)
    other = [index for index in range(3) if index != coordinate]
    mutable[coordinate] = 3 * mutable[other[0]] * mutable[other[1]] - mutable[coordinate]
    return tuple(sorted(mutable))  # type: ignore[return-value]


def parent(values: tuple[int, int, int]) -> tuple[int, int, int] | None:
    if values == ORIGIN:
        return None
    maximum = values[2]
    if values.count(maximum) != 1:
        raise AssertionError("tied non-root maximum")
    candidate = tuple(sorted((values[0], values[1], 3 * values[0] * values[1] - values[2])))
    if not markoff(candidate) or candidate[2] >= maximum:
        raise AssertionError("invalid descent")
    return candidate  # type: ignore[return-value]


def children(values: tuple[int, int, int]) -> list[tuple[int, int, int]]:
    result = set()
    for coordinate in range(3):
        candidate = replace(values, coordinate)
        if candidate[0] > 0 and markoff(candidate) and candidate[2] > values[2]:
            result.add(candidate)
    return sorted(result)


def independent_tree(max_depth: int) -> tuple[list[tuple[int, int, int]], dict[tuple[int, int, int], int], dict[tuple[int, int, int], tuple[int, int, int] | None], dict[tuple[int, int, int], str]]:
    levels: list[set[tuple[int, int, int]]] = [{ORIGIN}]
    parents: dict[tuple[int, int, int], tuple[int, int, int] | None] = {ORIGIN: None}
    words = {ORIGIN: ""}
    for depth in range(max_depth):
        next_level: set[tuple[int, int, int]] = set()
        for node in sorted(levels[depth]):
            for branch, child in enumerate(children(node)):
                check_parent = parent(child)
                if check_parent != node:
                    raise AssertionError((node, child, check_parent))
                if child in parents and parents[child] != node:
                    raise AssertionError("two parents")
                parents[child] = node
                words.setdefault(child, words[node] + str(branch))
                next_level.add(child)
        levels.append(next_level)
    depths = {node: depth for depth, level in enumerate(levels) for node in level}
    ordered = sorted(depths, key=lambda node: (depths[node], node))
    return ordered, depths, parents, words


def bounded_by_alternate_quadratic(bound: int) -> list[tuple[int, int, int]]:
    if bound in _BOUNDED_CACHE:
        return _BOUNDED_CACHE[bound]
    solutions = set()
    # The producer solves for z at fixed (x,y).  This checker instead solves
    # the quadratic in y at fixed (x,z), an independent loop ordering.
    for x in range(1, bound + 1):
        for z in range(x, bound + 1):
            discriminant = 9 * x * x * z * z - 4 * (x * x + z * z)
            if discriminant < 0:
                continue
            root = math.isqrt(discriminant)
            if root * root != discriminant:
                continue
            for signed_root in (-root, root):
                numerator = 3 * x * z + signed_root
                if numerator % 2:
                    continue
                y = numerator // 2
                candidate = (x, y, z)
                if x <= y <= z and markoff(candidate):
                    solutions.add(candidate)
    result = sorted(solutions)
    _BOUNDED_CACHE[bound] = result
    return result


def canonical_hash(data: dict[str, Any]) -> str:
    copy = dict(data)
    copy.pop("payload_sha256", None)
    raw = json.dumps(copy, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def verify(data: dict[str, Any]) -> int:
    global CHECKS
    CHECKS = 0
    check(data["payload_sha256"] == canonical_hash(data), "payload hash")
    check(data["schema"] == "hcs-c193-markoff-vieta-evidence-v1", "schema")
    check(data["candidate_id"] == "HCS-C193", "candidate")
    check(data["date_utc"] == "2026-08-27", "date")
    check(data["source_commit"] == SOURCE_COMMIT, "commit")
    check(data["evaluator"] == {"version": "0.2.0", "path": "flow_systems/skills/route-a-evaluator.md", "sha256": EVALUATOR_SHA256}, "evaluator")
    check(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    expected_lock = {
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
    }
    check(data["source_lock"] == expected_lock, "source lock")
    expected_attribution = {
        "markoff_owned": "the classical Diophantine equation and reduction genealogy",
        "bombieri_owned": "modern Markoff-tree and continued-fraction account",
        "bgs_owned": "the Vieta-involution orbit statement and explicit distinction from modular strong approximation",
        "package_derived": "a deterministic largest-coordinate descent formulation, exact termination certificate and executable tree/brute-force collision oracle",
    }
    check(data["attribution"] == expected_attribution, "attribution")
    expected_sources = [
        {"source_id": "M79", "authors": ["Andrey Markoff"], "title": "Sur les formes quadratiques binaires indefinies", "venue": "Mathematische Annalen 15, 381--406", "year": 1879, "doi": "10.1007/BF02086269", "role": "classical source of the equation and reduction theory"},
        {"source_id": "B07", "authors": ["Enrico Bombieri"], "title": "Continued fractions and the Markoff tree", "venue": "Expositiones Mathematicae 25(3), 187--213", "year": 2007, "doi": "10.1016/j.exmath.2006.10.002", "role": "modern source for the Markoff tree"},
        {"source_id": "BGS16", "authors": ["Jean Bourgain", "Alexander Gamburd", "Peter Sarnak"], "title": "Markoff triples and strong approximation", "venue": "Comptes Rendus Mathematique 354(2), 131--135", "year": 2016, "doi": "10.1016/j.crma.2015.12.006", "role": "Vieta orbit source and modular-boundary firewall"},
    ]
    check(data["source_registry"] == expected_sources, "sources")
    expected_theorem = {
        "vieta_invariance": "each coordinate Vieta involution preserves the Markoff polynomial and positive integral solutions when the replacement is positive",
        "unique_largest": "every normalized positive solution other than (1,1,1) has a unique largest coordinate",
        "strict_parent": "replacing that largest coordinate by the other quadratic root yields a positive Markoff triple of strictly smaller height",
        "nonparent_edges": "before sorting, mutating either nonmaximal coordinate produces a positive solution of strictly larger height, so every Vieta edge is oriented by the parent rule",
        "termination": "integer height is a strict Lyapunov function, so every descent reaches (1,1,1) in finitely many steps",
        "generation": "reversing the parent edges generates every positive solution from the root",
        "tree": "after quotienting coordinate permutations, the positive-solution graph is a rooted tree with the descent map as unique parent",
        "recurrence_boundary": "the autonomous descent has no non-root periodic orbit; the three labelled coordinate Vieta generators before sorting and permutation quotient remain involutions",
    }
    check(data["theorem"] == expected_theorem, "theorem")
    expected_route = {
        "tuple": ["A0_WEAK_ARITHMETIC_RELATION", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
        "overall": "ROUTE_A_REJECTED",
        "a0_reason": "the integer cubic and its Vieta dynamics are intrinsic Diophantine data, but they produce no rational-prime primitive carrier, prime-power repetition or logarithmic clock",
        "a1_reason": "strict descent terminates and has no nonconstant primitive periodic orbits",
        "a2_reason": "the rooted tree supplies no source-native dynamical determinant with a target divisor",
        "a3_reason": "no target continuation, functional equation, counting law or Weil compression follows",
        "a4_reason": "adjacency or Koopman operators on the tree are formal choices, not a target self-adjoint quantization",
        "route_b_invocation_allowed": False,
    }
    check(data["route_a"] == expected_route, "route")
    expected_flags = {
        "target_zero_table_used": False, "target_prime_table_used": False,
        "arithmetic_local_data_used": False, "mod_p_graph_used": False,
        "euler_factor_claimed": False, "root_number_claimed": False,
        "automorphy_claimed": False, "target_divisor_claimed": False,
        "target_functional_equation_claimed": False,
        "hilbert_polya_operator_claimed": False, "route_b_invoked": False,
    }
    check(data["scope_flags"] == expected_flags, "flags")
    expected_progress = {
        "explicit_progress": "the entire positive integer solution set receives a unique terminating parent map and rooted-tree certificate",
        "proof_boundary": "the bounded census is a regression oracle, not the proof of global descent or completeness",
        "arithmetic_boundary": "Diophantine origin earns only A0 weak because primes, powers and log p do not emerge",
        "uniqueness_boundary": "no claim is made that a largest Markoff number determines a unique unordered triple; that Frobenius problem remains open",
        "modular_boundary": "all reductions modulo primes and strong-approximation data are deliberately excluded",
        "frontier_boundary": "depth-ten rows retain every one-step child, including children at depth eleven outside the stored row population; the finite census is not a closed finite tree",
    }
    check(data["progress_and_boundary"] == expected_progress, "progress")
    expected_nonclaims = [
        "priority for the Markoff equation, Vieta involutions, descent or tree theorem",
        "the Frobenius uniqueness conjecture for Markoff numbers",
        "any statement about Markoff graphs modulo a prime or strong approximation",
        "a rational-prime primitive orbit, prime-power repetition law or logarithmic clock",
        "a target divisor, target functional equation or Hilbert--Polya operator",
        "Route-B authorization, global literature priority, external peer review or an acceptance score",
    ]
    check(data["nonclaims"] == expected_nonclaims, "nonclaims")

    finite = data["finite_regression"]
    max_depth = finite["max_depth"]
    check(max_depth == 10, "frozen depth")
    ordered, depths, parents, words = independent_tree(max_depth)
    rows = finite["tree_rows"]
    check(len(rows) == len(ordered) == finite["tree_row_count"], "tree population")
    for row, node in zip(rows, ordered):
        check(triple(row["triple"]) == node, "row node")
        check(row["depth"] == depths[node], "row depth")
        check(row["local_child_rank_word"] == words[node], "row word")
        check(triple(row["parent"]) == parents[node], "row parent")
        check([triple(value) for value in row["children"]] == children(node), "row children")
        check(int(row["height"]) == node[2], "row height")
        check(int(row["coordinate_sum"]) == sum(node), "row sum")
        check(row["unique_maximum"] is (node == ORIGIN or node.count(node[2]) == 1), "unique maximum")
        check(markoff(node), "Markoff equation")
        if node != ORIGIN:
            downward = parent(node)
            check(downward == parents[node], "unique descent")
            check(downward is not None and downward[2] < node[2], "height descent")
            check(replace(node, 0)[2] > node[2], "first nonmaximum mutation ascends")
            check(replace(node, 1)[2] > node[2], "second nonmaximum mutation ascends")
        for coordinate in range(3):
            image = replace(node, coordinate)
            if image[0] > 0:
                check(markoff(image), "Vieta invariance")
    expected_levels = {str(depth): sum(1 for value in depths.values() if value == depth) for depth in range(max_depth + 1)}
    check(finite["level_counts"] == expected_levels, "levels")
    check(finite["children_are_one_step_complete"] is True, "one-step children declaration")
    check(finite["frontier_child_count"] == sum(len(children(node)) for node in ordered if depths[node] == max_depth), "frontier children")
    check(finite["word_semantics"] == "each digit is the local lexicographic rank among the normalized forward children; it is not a fixed labelled Vieta-generator word", "word semantics")
    check(finite["maximum_coordinate_digits"] == max(len(str(node[2])) for node in ordered), "digits")
    check(finite["invariance_tests"] == sum(1 for node in ordered for coordinate in range(3) if replace(node, coordinate)[0] > 0), "invariance count")

    bound = finite["brute_bound"]
    check(bound == 2000, "frozen brute bound")
    bounded = bounded_by_alternate_quadratic(bound)
    check([triple(value) for value in finite["brute_solutions"]] == bounded, "brute solutions")
    check(finite["brute_solution_count"] == len(bounded), "brute count")
    check(all(node[2] <= bound for node in bounded), "brute bound")
    check(all(parent(node) in bounded for node in bounded if node != ORIGIN), "bounded parent closure")

    traces = finite["descent_traces"]
    check(finite["descent_trace_count"] == len(traces), "trace count")
    total_steps = 0
    for record in traces:
        seed = triple(record["seed"])
        trace_nodes = [triple(value) for value in record["trace"]]
        check(seed is not None and trace_nodes[0] == seed, "trace seed")
        check(record["depth"] == depths[seed], "trace depth")
        check(trace_nodes[-1] == ORIGIN, "trace root")
        check(len(trace_nodes) == record["depth"] + 1, "trace length")
        for child, ancestor in zip(trace_nodes, trace_nodes[1:]):
            check(child is not None and parent(child) == ancestor, "trace edge")
        total_steps += len(trace_nodes) - 1
    check(finite["descent_steps_checked"] == total_steps, "step total")
    return CHECKS


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    assertions = verify(data)
    print(json.dumps({
        "status": "C193_CHECKER_PASS",
        "assertions": assertions,
        "tree_rows": data["finite_regression"]["tree_row_count"],
        "brute_solutions": data["finite_regression"]["brute_solution_count"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
