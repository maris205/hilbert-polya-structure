#!/usr/bin/env python3
"""Nested-hole/recursive no-production-import auditor for P50 State A."""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Any


SLUG = "50-affine-divisibility-toeplitz-factor-posets"


def bytes_for(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=True, indent=2, sort_keys=True) + "\n").encode("ascii")


def fail(code: str) -> int:
    sys.stdout.buffer.write(bytes_for({"payload": {"code": code}, "schema": "stage0-error-v1", "status": "REJECT"}))
    return 2


def read_json(path: Path) -> Any:
    def hook(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        answer: dict[str, Any] = {}
        for key, value in pairs:
            if key in answer:
                raise ValueError("duplicate")
            answer[key] = value
        return answer
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


def exponent(p: int, integer: int) -> int:
    if type(p) is not int or p < 3 or type(integer) is not int or integer == 0:
        raise ValueError("divisibility domain")
    integer = abs(integer)
    answer = 0
    while integer % p == 0:
        integer //= p
        answer += 1
    return answer


def nested(p: int, directive: tuple[int, ...], k: int) -> int:
    if p < 3 or not directive:
        raise ValueError("nested domain")
    hole = 0
    modulus = 1
    level = 0
    while True:
        next_hole = hole + modulus
        next_modulus = modulus * p
        if k % next_modulus != next_hole % next_modulus:
            return directive[level % len(directive)]
        hole, modulus, level = next_hole, next_modulus, level + 1


def recurrent_center(p: int, n: int) -> int:
    answer = 0
    power = 1
    for _ in range(n):
        answer += power
        power *= p
    return answer


def canonical_labels(word: tuple[int, ...]) -> tuple[int, ...]:
    lookup: dict[int, int] = {}
    result = []
    for item in word:
        if item not in lookup:
            lookup[item] = len(lookup)
        result.append(lookup[item])
    return tuple(result)


def recursive_partitions(n: int) -> list[tuple[int, ...]]:
    output: list[tuple[int, ...]] = []

    def place(vertex: int, blocks: list[list[int]]) -> None:
        if vertex == n:
            labels = [0] * n
            for label, block in enumerate(blocks):
                for item in block:
                    labels[item] = label
            output.append(tuple(labels))
            return
        for block in blocks:
            block.append(vertex)
            place(vertex + 1, blocks)
            block.pop()
        blocks.append([vertex])
        place(vertex + 1, blocks)
        blocks.pop()

    place(1, [[0]])
    return sorted(set(output), key=lambda part: (max(part), part))


def graph_edges(directive: tuple[int, ...]) -> list[tuple[int, int]]:
    found = set()
    for index, letter in enumerate(directive):
        other = directive[(index + 1) % len(directive)]
        found.add((letter, other) if letter < other else (other, letter))
    return sorted(found)


def is_admissible(directive: tuple[int, ...], part: tuple[int, ...]) -> bool:
    for left, right in graph_edges(directive):
        if part[left] == part[right]:
            return False
    return True


def is_refinement(fine: tuple[int, ...], coarse: tuple[int, ...]) -> bool:
    induced: dict[int, int] = {}
    for vertex in range(len(fine)):
        if fine[vertex] in induced and induced[fine[vertex]] != coarse[vertex]:
            return False
        induced[fine[vertex]] = coarse[vertex]
    return True


def recursive_color_count(directive: tuple[int, ...], colors: int) -> int:
    graph = graph_edges(directive)
    assigned = [-1] * (max(directive) + 1)
    total = 0

    def extend(vertex: int) -> None:
        nonlocal total
        if vertex == len(assigned):
            if all(assigned[a] != assigned[b] for a, b in graph):
                total += 1
            return
        for color in range(colors):
            assigned[vertex] = color
            extend(vertex + 1)
        assigned[vertex] = -1

    extend(0)
    return total


def falling(q: int, count: int) -> int:
    answer = 1
    for index in range(count):
        answer *= q - index
    return answer


def directive_quotient(source: tuple[int, ...], target: tuple[int, ...]) -> bool:
    horizon = math.lcm(len(source), len(target))
    mapping: dict[int, int] = {}
    for index in range(horizon):
        source_letter = source[index % len(source)]
        target_letter = target[index % len(target)]
        if source_letter in mapping and mapping[source_letter] != target_letter:
            return False
        mapping[source_letter] = target_letter
    return set(mapping) == set(source) and set(mapping.values()) == set(target)


def nested_local(p: int, source: tuple[int, ...], target: tuple[int, ...], radius: int, low: int, high: int) -> dict[str, Any]:
    rule: dict[tuple[int, ...], int] = {}
    consistent = True
    for position in range(low, high + 1):
        window = tuple(nested(p, source, position + offset) for offset in range(-radius, radius + 1))
        output = nested(p, target, position)
        if window in rule and rule[window] != output:
            consistent = False
            break
        rule[window] = output
    return {"consistent": consistent, "is_surjective_letter_quotient": directive_quotient(source, target), "observed_window_count": len(rule), "target": list(target)}


def least_prime_factor(number: int) -> int:
    candidate = 2
    while candidate <= math.isqrt(number):
        if number % candidate == 0:
            return candidate
        candidate += 1
    return number


def audit_mutation(record: dict[str, Any]) -> str:
    """Independently execute each registry mutation on recursive primitives."""
    kind = record["kind"]
    payload = record["payload"]
    if kind == "nonsurjective_letter_map":
        images = set()
        domain = set()
        for pair in payload["letter_map"]:
            if type(pair) is not list or len(pair) != 2:
                raise ValueError("letter map")
            domain.add(pair[0])
            images.add(pair[1])
        if len(domain) == len(payload["letter_map"]) and images != set(payload["declared_target"]):
            return "REJECT_LETTER_MAP_NOT_SURJECTIVE"
    elif kind == "adjacent_letter_merge":
        directive = tuple(payload["directive"])
        partition = tuple(payload["partition"])
        merged_edges = [(left, right) for left, right in graph_edges(directive) if partition[left] == partition[right]]
        if len(partition) == max(directive) + 1 and merged_edges:
            return "REJECT_ADJACENT_MERGE"
    elif kind == "wrong_base":
        source_p, target_p = payload["source_p"], payload["target_p"]
        directive = tuple(payload["directive"])
        observations = []
        for position in range(-32, 33):
            observations.append((nested(source_p, directive, position), nested(target_p, directive, position)))
        if source_p != target_p and len(observations) == 65:
            return "REJECT_WRONG_BASE_OUT_OF_SCOPE"
    elif kind == "nonpointed_shift":
        p = payload["p"]
        directive = tuple(payload["directive"])
        shift = payload["shift"]
        if type(shift) is int and shift and nested(p, directive, 0) != nested(p, directive, shift):
            return "REJECT_NONPOINTED_OUT_OF_SCOPE"
    elif kind == "composite_called_constructive":
        p, n, q = payload["p"], payload["N"], payload["q"]
        directive = tuple(payload["directive"])
        divisor = least_prime_factor(p)
        comparisons = []
        for position in range(p**n):
            baseline = nested(p, directive, position)
            for translate in range(-p, p + 1):
                comparisons.append(nested(p, directive, position + translate * q) == baseline)
        if divisor != p and q == divisor * p**n and q < p ** (n + 1) and all(comparisons):
            return "REJECT_ALL_BASE_CONSTRUCTIVENESS"
    raise ValueError("mutation survived")


def audit(case: dict[str, Any]) -> dict[str, Any]:
    case_id, kind = case["case_id"], case["kind"]
    if kind == "point_values":
        rows = []
        for p in case["p_values"]:
            for raw in case["directives"]:
                directive = tuple(raw)
                rows.append({"directive": list(directive), "p": p, "values": [{"k": k, "value": nested(p, directive, k)} for k in case["positions"]]})
        result: dict[str, Any] = {"records": rows}
    elif kind == "skeleton_high_center":
        p, directive = case["p"], tuple(case["directive"])
        skeletons = []
        for n in case["levels"]:
            modulus, hole = p**n, recurrent_center(p, n)
            periodic = 0
            equalities = 0
            for residue in range(modulus):
                if residue == hole:
                    continue
                expected = nested(p, directive, residue)
                for translate in range(-2, 3):
                    if nested(p, directive, residue + translate * modulus) != expected:
                        raise AssertionError("skeleton")
                    equalities += 1
                periodic += 1
            if nested(p, directive, hole) == nested(p, directive, recurrent_center(p, n + 1)):
                raise AssertionError("hole")
            skeletons.append({"N": n, "hole": hole, "modulus": modulus, "periodic_equalities": equalities, "periodic_residues": periodic})
        high = []
        for offset in case["offsets"]:
            e = exponent(p, offset)
            n = e + 4
            observed = exponent(p, p**n + (p - 1) * offset)
            if observed != e:
                raise AssertionError("high")
            high.append({"exponent": observed, "n": n, "offset": offset, "value": nested(p, directive, recurrent_center(p, n) + offset)})
        result = {"high_centers": high, "skeletons": skeletons}
    elif kind == "prime_constructive":
        p, n, directive = case["p"], case["N"], tuple(case["directive"])
        if least_prime_factor(p) != p:
            raise ValueError("prime")
        witnesses = []
        for q in range(1, p ** (n + 1)):
            level = exponent(p, q)
            unit = q // p**level
            solutions = [t for t in range(p * p) if (1 + (p - 1) * unit * t - p) % (p * p) == 0]
            if len(solutions) != 1:
                raise AssertionError("solution")
            multiplier = solutions[0]
            c = recurrent_center(p, level)
            before = exponent(p, (p - 1) * c + 1)
            after = exponent(p, (p - 1) * (c + multiplier * q) + 1)
            if (before, after) != (level, level + 1) or nested(p, directive, c) == nested(p, directive, c + multiplier * q):
                raise AssertionError("witness")
            witnesses.append({"center": c, "level": level, "multiplier": multiplier, "q": q})
        result = {"common_period": p ** (n + 1), "rejected_count": len(witnesses), "witnesses": witnesses}
    elif kind == "composite_counterperiod":
        p, n, directive = case["p"], case["N"], tuple(case["directive"])
        ell = least_prime_factor(p)
        if ell == p:
            raise ValueError("composite")
        q = ell * p**n
        equalities = 0
        for position in range(p**n):
            expected = nested(p, directive, position)
            for translate in range(case["translate_min"], case["translate_max"] + 1):
                if nested(p, directive, position + translate * q) != expected:
                    raise AssertionError("counterperiod")
                equalities += 1
        result = {"checked_equalities": equalities, "counterperiod": q, "prime_divisor": ell, "strictly_below_next_power": q < p ** (n + 1)}
    elif kind == "partition_poset":
        directive = tuple(case["directive"])
        good = [part for part in recursive_partitions(max(directive) + 1) if is_admissible(directive, part)]
        counts: dict[int, int] = {}
        for part in good:
            blocks = max(part) + 1
            counts[blocks] = counts.get(blocks, 0) + 1
        refinement_edges = [[list(fine), list(coarse)] for fine in good for coarse in good if is_refinement(fine, coarse)]
        values = []
        for q in case["q_values"]:
            direct = recursive_color_count(directive, q)
            expanded = sum(count * falling(q, blocks) for blocks, count in counts.items())
            if direct != expanded:
                raise AssertionError("color")
            values.append({"count": direct, "q": q})
        result = {"admissible_partitions": [list(part) for part in good], "chromatic_values": values, "graphical_stirling": [{"blocks": blocks, "count": count} for blocks, count in sorted(counts.items())], "refinement_edges": refinement_edges}
    elif kind == "bounded_local_falsifier":
        source = tuple(case["source"])
        low, high = case["positions"]
        result = {"records": [nested_local(case["p"], source, tuple(target), case["radius"], low, high) for target in case["targets"]]}
    else:
        raise ValueError("kind")
    return {"case_id": case_id, "kind": kind, "result": result}


def main() -> int:
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--root")
    parser.add_argument("--state")
    parser.add_argument("--mutation")
    try:
        arguments = parser.parse_args()
    except SystemExit:
        return fail("REJECT_ARGUMENTS")
    if arguments.state != "A":
        return fail("REJECT_STATE")
    try:
        root = Path(arguments.root)
        if not root.is_absolute() or root.is_symlink() or not root.is_dir() or root.resolve(strict=True) != root:
            return fail("REJECT_ROOT")
        if arguments.mutation is not None:
            registry = read_json(root / "contracts" / "MUTATION_REGISTRY.json")
            matches = [record for record in registry["mutations"] if record["id"] == arguments.mutation]
            if len(matches) != 1:
                return fail("REJECT_MUTATION_ID")
            return fail(audit_mutation(matches[0]))
        specification = read_json(root / "contracts" / "STATE_A_CASES.json")
        if specification.get("project_slug") != SLUG or specification.get("state") != "A" or type(specification.get("cases")) is not list:
            return fail("REJECT_CASE_CONTRACT")
        output = {"payload": {"cases": [audit(case) for case in specification["cases"]], "evidence_class": "FINITE_EXACT_FALSIFICATION_ONLY", "project_slug": SLUG, "state": "A"}, "schema": "p50-stage0-science-v1", "status": "PASS"}
        sys.stdout.buffer.write(bytes_for(output))
        return 0
    except (AssertionError, KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
        return fail("REJECT_CASE_CONTRACT")


if __name__ == "__main__":
    raise SystemExit(main())
