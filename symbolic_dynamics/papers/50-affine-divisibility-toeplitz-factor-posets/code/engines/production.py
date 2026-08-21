#!/usr/bin/env python3
"""Direct affine/product exact engine for P50 State A."""

from __future__ import annotations

import argparse
import itertools
import json
import math
import sys
from pathlib import Path
from typing import Any, Iterable


SLUG = "50-affine-divisibility-toeplitz-factor-posets"


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True) + "\n").encode("ascii")


def reject(code: str) -> int:
    sys.stdout.buffer.write(canonical({"payload": {"code": code}, "schema": "stage0-error-v1", "status": "REJECT"}))
    return 2


def unique_json(path: Path) -> Any:
    def hook(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        if len(pairs) != len({key for key, _ in pairs}):
            raise ValueError("duplicate key")
        return dict(pairs)
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


def check_p(p: int) -> None:
    if type(p) is not int or p < 3:
        raise ValueError("integer base >=3 required")


def divexp(p: int, number: int) -> int:
    check_p(p)
    if type(number) is not int or number == 0:
        raise ValueError("nonzero integer required")
    remaining = abs(number)
    exponent = 0
    while remaining % p == 0:
        remaining //= p
        exponent += 1
    return exponent


def value(p: int, directive: tuple[int, ...], k: int) -> int:
    if not directive or any(type(letter) is not int or letter < 0 for letter in directive):
        raise ValueError("directive")
    affine = (p - 1) * k + 1
    return directive[divexp(p, affine) % len(directive)]


def center(p: int, n: int) -> int:
    check_p(p)
    if type(n) is not int or n < 0:
        raise ValueError("level")
    return (p**n - 1) // (p - 1)


def least_period(word: tuple[int, ...]) -> int:
    for period in range(1, len(word) + 1):
        if len(word) % period == 0 and all(word[index] == word[index % period] for index in range(len(word))):
            return period
    raise AssertionError("no period")


def canonicalize(word: Iterable[int]) -> tuple[int, ...]:
    labels: dict[int, int] = {}
    output = []
    for letter in word:
        if letter not in labels:
            labels[letter] = len(labels)
        output.append(labels[letter])
    return tuple(output)


def partitions(n: int) -> list[tuple[int, ...]]:
    answer = set()
    for raw in itertools.product(range(n), repeat=n):
        if raw[0] == 0 and canonicalize(raw) == raw:
            answer.add(raw)
    return sorted(answer, key=lambda part: (max(part), part))


def edges(directive: tuple[int, ...]) -> list[tuple[int, int]]:
    return sorted({tuple(sorted((directive[i], directive[(i + 1) % len(directive)]))) for i in range(len(directive))})


def admissible(directive: tuple[int, ...], part: tuple[int, ...]) -> bool:
    return all(part[a] != part[b] for a, b in edges(directive))


def refines(fine: tuple[int, ...], coarse: tuple[int, ...]) -> bool:
    return all(fine[a] != fine[b] or coarse[a] == coarse[b] for a in range(len(fine)) for b in range(len(fine)))


def falling(q: int, k: int) -> int:
    result = 1
    for offset in range(k):
        result *= q - offset
    return result


def direct_colorings(directive: tuple[int, ...], q: int) -> int:
    graph = edges(directive)
    vertices = max(directive) + 1
    return sum(all(coloring[a] != coloring[b] for a, b in graph) for coloring in itertools.product(range(q), repeat=vertices))


def letter_quotient(source: tuple[int, ...], target: tuple[int, ...]) -> bool:
    horizon = math.lcm(len(source), len(target))
    mapping: dict[int, int] = {}
    for index in range(horizon):
        a, b = source[index % len(source)], target[index % len(target)]
        if a in mapping and mapping[a] != b:
            return False
        mapping[a] = b
    return set(mapping) == set(source) and set(mapping.values()) == set(target)


def local_check(p: int, source: tuple[int, ...], target: tuple[int, ...], radius: int, low: int, high: int) -> dict[str, Any]:
    table: dict[tuple[int, ...], int] = {}
    consistent = True
    for k in range(low, high + 1):
        window = tuple(value(p, source, k + offset) for offset in range(-radius, radius + 1))
        output = value(p, target, k)
        if window in table and table[window] != output:
            consistent = False
            break
        table[window] = output
    return {
        "consistent": consistent,
        "is_surjective_letter_quotient": letter_quotient(source, target),
        "observed_window_count": len(table),
        "target": list(target),
    }


def smallest_prime_divisor(number: int) -> int:
    for divisor in range(2, math.isqrt(number) + 1):
        if number % divisor == 0:
            return divisor
    return number


def evaluate_mutation(record: dict[str, Any]) -> str:
    """Drive every locked falsifier through production science primitives."""
    kind = record["kind"]
    payload = record["payload"]
    if kind == "nonsurjective_letter_map":
        mapping = {source: target for source, target in payload["letter_map"]}
        declared = set(payload["declared_target"])
        if len(mapping) == len(payload["letter_map"]) and set(mapping.values()) != declared:
            return "REJECT_LETTER_MAP_NOT_SURJECTIVE"
    elif kind == "adjacent_letter_merge":
        directive = tuple(payload["directive"])
        partition = tuple(payload["partition"])
        if len(partition) == max(directive) + 1 and not admissible(directive, partition):
            return "REJECT_ADJACENT_MERGE"
    elif kind == "wrong_base":
        source_p, target_p = payload["source_p"], payload["target_p"]
        directive = tuple(payload["directive"])
        check_p(source_p)
        check_p(target_p)
        samples = [(value(source_p, directive, k), value(target_p, directive, k)) for k in range(-32, 33)]
        if source_p != target_p and len(samples) == 65:
            return "REJECT_WRONG_BASE_OUT_OF_SCOPE"
    elif kind == "nonpointed_shift":
        p, directive, shift = payload["p"], tuple(payload["directive"]), payload["shift"]
        if type(shift) is int and shift != 0 and value(p, directive, 0) != value(p, directive, shift):
            return "REJECT_NONPOINTED_OUT_OF_SCOPE"
    elif kind == "composite_called_constructive":
        p, n, q = payload["p"], payload["N"], payload["q"]
        directive = tuple(payload["directive"])
        ell = smallest_prime_divisor(p)
        equality = all(
            value(p, directive, k + translate * q) == value(p, directive, k)
            for k in range(p**n)
            for translate in range(-p, p + 1)
        )
        if ell < p and q == ell * p**n and q < p ** (n + 1) and equality:
            return "REJECT_ALL_BASE_CONSTRUCTIVENESS"
    raise ValueError("mutation survived")


def evaluate(case: dict[str, Any]) -> dict[str, Any]:
    case_id, kind = case["case_id"], case["kind"]
    if kind == "point_values":
        rows = []
        for p in case["p_values"]:
            for raw in case["directives"]:
                directive = tuple(raw)
                rows.append({
                    "directive": list(directive),
                    "p": p,
                    "values": [{"k": k, "value": value(p, directive, k)} for k in case["positions"]],
                })
        result: dict[str, Any] = {"records": rows}
    elif kind == "skeleton_high_center":
        p, directive = case["p"], tuple(case["directive"])
        skeletons = []
        for n in case["levels"]:
            modulus = p**n
            hole = center(p, n)
            periodic = 0
            equalities = 0
            for residue in range(modulus):
                if residue == hole:
                    continue
                expected = value(p, directive, residue)
                for t in range(-2, 3):
                    if value(p, directive, residue + t * modulus) != expected:
                        raise AssertionError("skeleton")
                    equalities += 1
                periodic += 1
            if value(p, directive, hole) == value(p, directive, center(p, n + 1)):
                raise AssertionError("hole")
            skeletons.append({"N": n, "hole": hole, "modulus": modulus, "periodic_equalities": equalities, "periodic_residues": periodic})
        high = []
        for offset in case["offsets"]:
            e = divexp(p, offset)
            n = e + 4
            observed = divexp(p, p**n + (p - 1) * offset)
            if observed != e:
                raise AssertionError("high center")
            high.append({"exponent": observed, "n": n, "offset": offset, "value": value(p, directive, center(p, n) + offset)})
        result = {"high_centers": high, "skeletons": skeletons}
    elif kind == "prime_constructive":
        p, n, directive = case["p"], case["N"], tuple(case["directive"])
        if smallest_prime_divisor(p) != p:
            raise ValueError("prime lane")
        witnesses = []
        for q in range(1, p ** (n + 1)):
            level = divexp(p, q)
            unit = q // p**level
            multiplier = ((p - 1) * pow((p - 1) * unit, -1, p * p)) % (p * p)
            c = center(p, level)
            before = divexp(p, (p - 1) * c + 1)
            after = divexp(p, (p - 1) * (c + multiplier * q) + 1)
            if (before, after) != (level, level + 1) or value(p, directive, c) == value(p, directive, c + multiplier * q):
                raise AssertionError("prime witness")
            witnesses.append({"center": c, "level": level, "multiplier": multiplier, "q": q})
        result = {"common_period": p ** (n + 1), "rejected_count": len(witnesses), "witnesses": witnesses}
    elif kind == "composite_counterperiod":
        p, n, directive = case["p"], case["N"], tuple(case["directive"])
        ell = smallest_prime_divisor(p)
        if ell == p:
            raise ValueError("composite lane")
        q = ell * p**n
        equalities = 0
        for k in range(p**n):
            expected = value(p, directive, k)
            for t in range(case["translate_min"], case["translate_max"] + 1):
                if value(p, directive, k + t * q) != expected:
                    raise AssertionError("counterperiod")
                equalities += 1
        result = {"checked_equalities": equalities, "counterperiod": q, "prime_divisor": ell, "strictly_below_next_power": q < p ** (n + 1)}
    elif kind == "partition_poset":
        directive = tuple(case["directive"])
        good = [part for part in partitions(max(directive) + 1) if admissible(directive, part)]
        counts: dict[int, int] = {}
        for part in good:
            blocks = max(part) + 1
            counts[blocks] = counts.get(blocks, 0) + 1
        refinement_edges = [[list(fine), list(coarse)] for fine in good for coarse in good if refines(fine, coarse)]
        chromatic_values = []
        for q in case["q_values"]:
            direct = direct_colorings(directive, q)
            expanded = sum(count * falling(q, blocks) for blocks, count in counts.items())
            if direct != expanded:
                raise AssertionError("chromatic")
            chromatic_values.append({"count": direct, "q": q})
        result = {
            "admissible_partitions": [list(part) for part in good],
            "chromatic_values": chromatic_values,
            "graphical_stirling": [{"blocks": blocks, "count": count} for blocks, count in sorted(counts.items())],
            "refinement_edges": refinement_edges,
        }
    elif kind == "bounded_local_falsifier":
        source = tuple(case["source"])
        low, high = case["positions"]
        result = {"records": [local_check(case["p"], source, tuple(target), case["radius"], low, high) for target in case["targets"]]}
    else:
        raise ValueError("unknown kind")
    return {"case_id": case_id, "kind": kind, "result": result}


def main() -> int:
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--root")
    parser.add_argument("--state")
    parser.add_argument("--mutation")
    try:
        args = parser.parse_args()
    except SystemExit:
        return reject("REJECT_ARGUMENTS")
    if args.state != "A":
        return reject("REJECT_STATE")
    try:
        root = Path(args.root)
        if not root.is_absolute() or root.is_symlink() or not root.is_dir() or root.resolve(strict=True) != root:
            return reject("REJECT_ROOT")
        if args.mutation is not None:
            registry = unique_json(root / "contracts" / "MUTATION_REGISTRY.json")
            matches = [record for record in registry["mutations"] if record["id"] == args.mutation]
            if len(matches) != 1:
                return reject("REJECT_MUTATION_ID")
            return reject(evaluate_mutation(matches[0]))
        spec = unique_json(root / "contracts" / "STATE_A_CASES.json")
        if spec.get("project_slug") != SLUG or spec.get("state") != "A" or type(spec.get("cases")) is not list:
            return reject("REJECT_CASE_CONTRACT")
        envelope = {
            "payload": {"cases": [evaluate(case) for case in spec["cases"]], "evidence_class": "FINITE_EXACT_FALSIFICATION_ONLY", "project_slug": SLUG, "state": "A"},
            "schema": "p50-stage0-science-v1",
            "status": "PASS",
        }
        sys.stdout.buffer.write(canonical(envelope))
        return 0
    except (AssertionError, KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
        return reject("REJECT_CASE_CONTRACT")


if __name__ == "__main__":
    raise SystemExit(main())
