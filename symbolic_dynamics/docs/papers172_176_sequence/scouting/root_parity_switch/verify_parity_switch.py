#!/usr/bin/env python3
"""Exact scout for odd-degree Seidel-switch feedback on labelled graphs."""

from __future__ import annotations

import hashlib
import json
import random
from collections import Counter, defaultdict
from functools import cache
from math import comb


ASSERTIONS = 0


def check(condition: bool, message: str = "") -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


@cache
def edge_list(n: int) -> tuple[tuple[int, int], ...]:
    return tuple((i, j) for i in range(n) for j in range(i + 1, n))


def degree_mask(n: int, graph: int) -> int:
    out = 0
    for bit, (i, j) in enumerate(edge_list(n)):
        if (graph >> bit) & 1:
            out ^= (1 << i) | (1 << j)
    return out


def cut_mask(n: int, vertices: int) -> int:
    out = 0
    for bit, (i, j) in enumerate(edge_list(n)):
        if ((vertices >> i) ^ (vertices >> j)) & 1:
            out |= 1 << bit
    return out


def step(n: int, graph: int) -> int:
    odd = degree_mask(n, graph)
    return graph ^ cut_mask(n, odd)


def iterate(n: int, graph: int, time: int) -> int:
    for _ in range(time):
        graph = step(n, graph)
    return graph


def fixed_formula(n: int) -> int:
    m = comb(n, 2)
    if n == 1:
        return 1
    cycle_space = 1 << (m - n + 1)
    return cycle_space if n % 2 else 2 * cycle_space


def fibre_formula(n: int, target: int, time: int) -> int:
    m = comb(n, 2)
    if time == 0:
        return 1
    if n % 2:
        return (1 << (n - 1)) if degree_mask(n, target) == 0 else 0
    return 1


def odd_marked_formula(n: int, target: int) -> Counter[int]:
    assert n % 2 == 1
    poly: Counter[int] = Counter()
    for vertices in range(1 << n):
        if vertices.bit_count() % 2 == 0:
            source = target ^ cut_mask(n, vertices)
            poly[source.bit_count()] += 1
            cut_edges = (target & cut_mask(n, vertices)).bit_count()
            predicted = (
                target.bit_count()
                + vertices.bit_count() * (n - vertices.bit_count())
                - 2 * cut_edges
            )
            check(source.bit_count() == predicted, "edge-weight exponent")
    return poly


def exhaustive() -> dict[str, object]:
    census: dict[str, object] = {}
    for n in range(1, 7):
        m = comb(n, 2)
        total = 1 << m
        fibres: dict[int, list[int]] = defaultdict(list)
        fixed = 0
        fixed_iterates = []

        for graph in range(total):
            image = step(n, graph)
            fibres[image].append(graph)
            odd = degree_mask(n, graph)
            image_odd = degree_mask(n, image)
            check(odd.bit_count() % 2 == 0, "handshake parity")
            if n % 2:
                check(step(n, image) == image, "odd-order idempotence")
                check(image_odd == 0, "odd-order Euler image")
                check((image == graph) == (odd == 0), "odd fixed criterion")
            else:
                check(step(n, image) == graph, "even-order involution")
                check(image_odd == odd, "even degree signature preserved")
                expected_fixed = odd in (0, (1 << n) - 1)
                check((image == graph) == expected_fixed, "even fixed criterion")
            fixed += image == graph

            for time in range(5):
                actual = iterate(n, graph, time)
                if n % 2 and time >= 1:
                    predicted = image
                elif n % 2 == 0 and time % 2:
                    predicted = image
                else:
                    predicted = graph
                check(actual == predicted, "all-time orbit formula")

        check(fixed == fixed_formula(n), "fixed census")
        time_fibres = [
            Counter(iterate(n, source, time) for source in range(total))
            for time in range(5)
        ]
        for target in range(total):
            check(len(fibres.get(target, [])) == fibre_formula(n, target, 1), "fibre")
            for time in range(5):
                count = time_fibres[time][target]
                check(count == fibre_formula(n, target, time), "all-time fibre")

        for time in range(1, 7):
            actual = sum(iterate(n, graph, time) == graph for graph in range(total))
            if n % 2:
                predicted = fixed
            else:
                predicted = fixed if time % 2 else total
            check(actual == predicted, "fixed-iterate/zeta census")
            fixed_iterates.append(actual)

        if n % 2 and n <= 5:
            for target in range(total):
                if degree_mask(n, target) != 0:
                    continue
                literal = Counter(source.bit_count() for source in fibres[target])
                formula = odd_marked_formula(n, target)
                check(literal == formula, "marked every-target fibre")
                check(sum(formula.values()) == 1 << (n - 1), "marked mass")
                constructed = {
                    target ^ cut_mask(n, vertices)
                    for vertices in range(1 << n)
                    if vertices.bit_count() % 2 == 0
                }
                check(len(constructed) == 1 << (n - 1), "even-set injectivity")
                check(constructed == set(fibres[target]), "preimage parametrization")

        if n % 2:
            periods = {1}
            height = 0 if n == 1 else 1
        else:
            periods = {1} if total == fixed else {1, 2}
            height = 0
        census[str(n)] = {
            "graphs": total,
            "fixed": fixed,
            "fixed_iterates_1_to_6": fixed_iterates,
            "height": height,
            "periods": sorted(periods),
            "image_size": len(fibres),
            "fibre_values": sorted({len(v) for v in fibres.values()}),
        }
    return census


def large_samples() -> dict[str, object]:
    rng = random.Random(172176)
    result: dict[str, object] = {}
    for n in (7, 8, 9, 10, 16, 25):
        m = comb(n, 2)
        trials = 4000 if n <= 10 else 1000
        fixed_hits = 0
        for _ in range(trials):
            graph = rng.getrandbits(m)
            image = step(n, graph)
            if n % 2:
                check(step(n, image) == image)
                check(degree_mask(n, image) == 0)
            else:
                check(step(n, image) == graph)
                check(degree_mask(n, image) == degree_mask(n, graph))
            fixed_hits += image == graph
        result[str(n)] = {"trials": trials, "fixed_hits": fixed_hits}
    return result


def linear_checks() -> dict[str, object]:
    rng = random.Random(314159)
    rows = []
    for n in range(1, 18):
        m = comb(n, 2)
        for _ in range(300):
            x = rng.getrandbits(m)
            y = rng.getrandbits(m)
            check(step(n, x ^ y) == (step(n, x) ^ step(n, y)), "linearity")
        rows.append({"n": n, "edge_dimension": m, "fixed_formula": fixed_formula(n)})
    return {"rows": rows}


def main() -> None:
    census = exhaustive()
    samples = large_samples()
    linear = linear_checks()
    payload = {
        "census": census,
        "samples": samples,
        "linear": linear,
        "theorem_signal": {
            "odd_n": "idempotent projection onto Eulerian graphs",
            "even_n": "involution; fixed iff all degrees have one parity",
            "odd_target_fibre": "even vertex subsets parameterize all preimages",
        },
    }
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    print("PARITY_SWITCH_SCOUT_PASS")
    print(f"assertions={ASSERTIONS}")
    print(f"payload_sha256={hashlib.sha256(encoded).hexdigest()}")
    print(json.dumps(payload, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
