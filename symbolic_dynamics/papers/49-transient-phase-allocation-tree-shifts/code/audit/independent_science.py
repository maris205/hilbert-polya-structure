#!/usr/bin/env python3
"""No-production-import exact science auditor for P49 State A.

This implementation is intentionally self-contained.  It uses a different
factor loop, direct tree-level prefix loops, and independently written form
and composition routines.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable, Iterator, Sequence


Vector = dict[int, Fraction]
SLUG = "49-transient-phase-allocation-tree-shifts"


def encoded(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=True, indent=2, sort_keys=True) + "\n").encode("ascii")


def fail(code: str) -> int:
    sys.stdout.buffer.write(encoded({"payload": {"code": code}, "schema": "stage0-error-v1", "status": "REJECT"}))
    return 2


def read_unique(path: Path) -> Any:
    def hook(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        if len({key for key, _ in pairs}) != len(pairs):
            raise ValueError("duplicate")
        return dict(pairs)
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


def prime_powers(number: int) -> dict[int, int]:
    if type(number) is not int or number <= 0:
        raise ValueError("positive exact integer")
    result: dict[int, int] = {}
    candidate = 2
    remaining = number
    while candidate <= remaining // candidate:
        if remaining % candidate:
            candidate += 1
        else:
            result[candidate] = result.get(candidate, 0) + 1
            remaining //= candidate
    if remaining != 1:
        result[remaining] = result.get(remaining, 0) + 1
    return result


def normalized(vector: Vector) -> Vector:
    return {key: Fraction(value) for key, value in vector.items() if value != 0}


def combine(items: Iterable[tuple[Fraction | int, Vector]]) -> Vector:
    result: Vector = {}
    for multiplier, vector in items:
        multiplier = Fraction(multiplier)
        for prime, coefficient in vector.items():
            result[prime] = result.get(prime, Fraction(0)) + multiplier * coefficient
    return normalized(result)


def integer_log(number: int) -> Vector:
    return {prime: Fraction(power) for prime, power in prime_powers(number).items()}


def order(left: Vector, right: Vector) -> int:
    difference = combine(((1, left), (-1, right)))
    if not difference:
        return 0
    multiple = 1
    for coefficient in difference.values():
        multiple = math.lcm(multiple, coefficient.denominator)
    above = 1
    below = 1
    for prime, coefficient in difference.items():
        power = coefficient.numerator * (multiple // coefficient.denominator)
        if power > 0:
            above *= prime**power
        if power < 0:
            below *= prime ** (-power)
    return (above > below) - (above < below)


def terms(vector: Vector) -> list[dict[str, int]]:
    return [
        {"denominator": coefficient.denominator, "numerator": coefficient.numerator, "prime": prime}
        for prime, coefficient in sorted(normalized(vector).items())
    ]


def integer_terms(vector: dict[int, int]) -> list[dict[str, int]]:
    return [{"exponent": exponent, "prime": prime} for prime, exponent in sorted(vector.items()) if exponent]


def check_tree(d: int, a: Sequence[int], m: Sequence[int] | None = None, total: int | None = None) -> None:
    if type(d) is not int or d < 2 or len(a) == 0 or any(type(x) is not int or x <= 0 for x in a):
        raise ValueError("tree domain")
    if m is not None:
        required = d if total is None else total
        if len(m) != len(a) or any(type(x) is not int or x < 0 for x in m) or sum(m) != required:
            raise ValueError("composition domain")


def periodic_limits(d: int, a: Sequence[int]) -> list[Vector]:
    check_tree(d, a)
    p = len(a)
    phase_logs = [integer_log(value) for value in a]
    answer: list[Vector] = []
    normalizer = d**p - 1
    for terminal_phase in range(p):
        pieces: list[tuple[Fraction, Vector]] = []
        power = d ** (p - 1)
        for backwards in range(p):
            pieces.append((Fraction((d - 1) * power, normalizer), phase_logs[(terminal_phase - backwards) % p]))
            power //= d
        answer.append(combine(pieces))
    return answer


def allocated_limits(d: int, a: Sequence[int], m: Sequence[int], denominator: int) -> list[Vector]:
    check_tree(d, a, m, denominator)
    base = periodic_limits(d, a)
    p = len(a)
    return [
        combine((Fraction(m[s], denominator), base[(s + residue) % p]) for s in range(p))
        for residue in range(p)
    ]


def least(vectors: Sequence[Vector]) -> tuple[int, Vector]:
    winner = 0
    for index in range(1, len(vectors)):
        if order(vectors[index], vectors[winner]) < 0:
            winner = index
    return winner, vectors[winner]


def weak_compositions(total: int, length: int) -> Iterator[tuple[int, ...]]:
    if length == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for suffix in weak_compositions(total - first, length - 1):
                yield (first,) + suffix


def direct_core_levels(d: int, a: Sequence[int], root: int, depth: int) -> dict[int, int]:
    exponents: dict[int, int] = {}
    vertices = 1
    for level in range(depth + 1):
        for prime, power in prime_powers(a[(root + level) % len(a)]).items():
            exponents[prime] = exponents.get(prime, 0) + vertices * power
        vertices *= d
    return exponents


def direct_feeder_levels(d: int, a: Sequence[int], m: Sequence[int], depth: int) -> dict[int, int]:
    check_tree(d, a, m, d)
    exponents: dict[int, int] = {}
    if depth < 1:
        return exponents
    for phase, leaves in enumerate(m):
        vertices = leaves
        for level in range(depth):
            for prime, power in prime_powers(a[(phase + level) % len(a)]).items():
                exponents[prime] = exponents.get(prime, 0) + vertices * power
            vertices *= d
    return exponents


def optimize(d: int, a: Sequence[int], level: int) -> tuple[tuple[int, ...], Vector, list[Vector]]:
    total = d**level
    chosen_m: tuple[int, ...] | None = None
    chosen_dimension: Vector | None = None
    chosen_residues: list[Vector] | None = None
    for m in weak_compositions(total, len(a)):
        residues = allocated_limits(d, a, m, total)
        _, dimension = least(residues)
        if chosen_dimension is None or order(dimension, chosen_dimension) > 0:
            chosen_m = m
            chosen_dimension = dimension
            chosen_residues = residues
    assert chosen_m is not None and chosen_dimension is not None and chosen_residues is not None
    return chosen_m, chosen_dimension, chosen_residues


def audit_mutation(record: dict[str, Any]) -> str:
    kind = record["kind"]
    payload = record["payload"]
    if kind == "unconditional_divisibility_necessity":
        d, a, m = payload["d"], tuple(payload["a"]), tuple(payload["m"])
        residues = allocated_limits(d, a, m, d)
        if all(normalized(vector) == normalized(residues[0]) for vector in residues[1:]) and d % len(a) != 0:
            return "REJECT_FALSE_DIVISIBILITY_NECESSITY"
    elif kind == "missing_complete_block_edge":
        sizes = tuple(payload["phase_sizes"])
        removed = tuple(tuple(vertex) for vertex in payload["removed_edge"])
        expected = set()
        for phase in range(len(sizes)):
            for source in range(sizes[phase]):
                for target in range(sizes[(phase + 1) % len(sizes)]):
                    expected.add(((phase, source), ((phase + 1) % len(sizes), target)))
        observed = {edge for edge in expected if edge != removed}
        if removed in expected and len(observed) + 1 == len(expected):
            return "REJECT_INCOMPLETE_CORE"
    elif kind == "core_to_feeder_return":
        adjacency = payload["adjacency"]
        possible = {0}
        returned_at = []
        for step in range(1, payload["depth"] + 1):
            following = set()
            for source in possible:
                for target in range(len(adjacency[source])):
                    if adjacency[source][target] == 1:
                        following.add(target)
            possible = following
            if 0 in possible:
                returned_at.append(step)
        if returned_at and returned_at[-1] == payload["depth"]:
            return "REJECT_NONTRANSIENT"
    elif kind == "incomplete_feeder_row":
        p, d = payload["p"], payload["d"]
        allowed = set(payload["allowed_child_phases"])
        all_compositions = list(weak_compositions(d, p))
        admitted = [m for m in all_compositions if all(m[index] == 0 for index in range(p) if index not in allowed)]
        if len(admitted) < len(all_compositions):
            return "REJECT_UNRESTRICTED_PHASE_ACCESS"
    elif kind == "invalid_d_phase_size_and_composition":
        outcomes = []
        for case in payload["invalid_cases"]:
            try:
                check_tree(case["d"], tuple(case["a"]), tuple(case["m"]), case["d"])
            except ValueError:
                outcomes.append(False)
            else:
                outcomes.append(True)
        if outcomes == [False] * len(outcomes):
            return "REJECT_TYPED_BOUNDARIES"
    elif kind == "four_state_max_scc_formula":
        d, a, m = payload["d"], tuple(payload["a"]), tuple(payload["m"])
        _, core = least(periodic_limits(d, a))
        _, feeder = least(allocated_limits(d, a, m, d))
        if order(feeder, core) > 0:
            return "REJECT_ARBITRARY_MAX_SCC"
    raise ValueError("mutation survived")


def audit_case(case: dict[str, Any]) -> dict[str, Any]:
    name = case["case_id"]
    kind = case["kind"]
    if kind == "four_state_strict_scc":
        d, a, m = case["d"], tuple(case["a"]), tuple(case["m"])
        core = periodic_limits(d, a)
        feeder = allocated_limits(d, a, m, d)
        core_index, core_dim = least(core)
        feeder_index, feeder_dim = least(feeder)
        result = {
            "component_dimension": terms(core_dim),
            "component_min_residue": core_index,
            "component_residues": [terms(vector) for vector in core],
            "feeder_dimension": terms(feeder_dim),
            "feeder_min_residue": feeder_index,
            "feeder_residues": [terms(vector) for vector in feeder],
            "full_strictly_exceeds_component": order(feeder_dim, core_dim) > 0,
            "prefix_exponents": [
                {
                    "component_root0": integer_terms(direct_core_levels(d, a, 0, depth)),
                    "depth": depth,
                    "feeder": integer_terms(direct_feeder_levels(d, a, m, depth)),
                }
                for depth in case["prefix_depths"]
            ],
        }
    elif kind == "nondivisible_saturation":
        d, a, m = case["d"], tuple(case["a"]), tuple(case["m"])
        residues = allocated_limits(d, a, m, d)
        products = []
        for shift in range(len(a)):
            value = 1
            for phase, multiplicity in enumerate(m):
                value *= a[(phase + shift) % len(a)] ** multiplicity
            products.append(value)
        result = {
            "p_divides_d": d % len(a) == 0,
            "residue_forms": [terms(vector) for vector in residues],
            "saturates": all(normalized(vector) == normalized(residues[0]) for vector in residues[1:]),
            "shifted_products": products,
        }
    elif kind == "p2_odd_optimizer":
        d, a = case["d"], tuple(case["a"])
        core_index, core_dim = least(periodic_limits(d, a))
        rows = []
        selected_m: tuple[int, ...] | None = None
        selected: Vector | None = None
        for k in range(d + 1):
            m = (k, d - k)
            _, dimension = least(allocated_limits(d, a, m, d))
            rows.append({"dimension": terms(dimension), "m": list(m)})
            if selected is None or order(dimension, selected) > 0:
                selected_m, selected = m, dimension
        assert selected_m is not None and selected is not None
        mean = combine((Fraction(1, 2), integer_log(value)) for value in a)
        result = {
            "component_dimension": terms(core_dim),
            "component_min_residue": core_index,
            "fixed_compositions": rows,
            "mean": terms(mean),
            "optimum_composition": list(selected_m),
            "optimum_dimension": terms(selected),
            "optimum_saturates": normalized(selected) == normalized(mean),
            "strictly_exceeds_component": order(selected, core_dim) > 0,
        }
    elif kind == "level_optimizer":
        d, a = case["d"], tuple(case["a"])
        level, next_level = case["level"], case["next_level"]
        if type(level) is not int or type(next_level) is not int or level < 1 or next_level != level + 1:
            raise ValueError("level domain")
        m_l, dimension_l, residues_l = optimize(d, a, level)
        m_next, dimension_next, residues_next = optimize(d, a, next_level)
        embedded = tuple(d * value for value in m_l)
        _, embedded_dimension = least(allocated_limits(d, a, embedded, d**next_level))
        result = {
            "embedded_composition": list(embedded),
            "embedded_dimension": terms(embedded_dimension),
            "level": level,
            "level_dimension": terms(dimension_l),
            "level_optimizer": list(m_l),
            "level_residues": [terms(vector) for vector in residues_l],
            "next_dimension": terms(dimension_next),
            "next_level": next_level,
            "next_optimizer": list(m_next),
            "next_residues": [terms(vector) for vector in residues_next],
            "optimized_monotone": order(dimension_next, dimension_l) >= 0,
        }
    else:
        raise ValueError("case kind")
    return {"case_id": name, "kind": kind, "result": result}


def main() -> int:
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--root")
    parser.add_argument("--state")
    parser.add_argument("--mutation")
    try:
        args = parser.parse_args()
    except SystemExit:
        return fail("REJECT_ARGUMENTS")
    if args.state != "A":
        return fail("REJECT_STATE")
    try:
        root = Path(args.root)
        if not root.is_absolute() or root.is_symlink() or not root.is_dir() or root.resolve(strict=True) != root:
            return fail("REJECT_ROOT")
        if args.mutation is not None:
            registry = read_unique(root / "contracts" / "MUTATION_REGISTRY.json")
            matches = [record for record in registry["mutations"] if record["id"] == args.mutation]
            if len(matches) != 1:
                return fail("REJECT_MUTATION_ID")
            return fail(audit_mutation(matches[0]))
        specification = read_unique(root / "contracts" / "STATE_A_CASES.json")
        if specification.get("project_slug") != SLUG or specification.get("state") != "A" or type(specification.get("cases")) is not list:
            return fail("REJECT_CASE_CONTRACT")
        output = {
            "payload": {
                "cases": [audit_case(case) for case in specification["cases"]],
                "evidence_class": "FINITE_EXACT_FALSIFICATION_ONLY",
                "project_slug": SLUG,
                "state": "A",
            },
            "schema": "p49-stage0-science-v1",
            "status": "PASS",
        }
        sys.stdout.buffer.write(encoded(output))
        return 0
    except (AssertionError, KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
        return fail("REJECT_CASE_CONTRACT")


if __name__ == "__main__":
    raise SystemExit(main())
