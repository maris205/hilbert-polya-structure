"""The single predeclared B1 diagnostic; exact integers, no period cutoff.

Output is a generated audit artifact, not an all-parameter theorem.
"""

from collections import Counter
from math import isqrt
from pathlib import Path
import json


def graph_cycles(successor):
    done = set()
    cycles = []
    for start in successor:
        if start in done:
            continue
        trail = []
        position = {}
        state = start
        while state in successor and state not in done and state not in position:
            position[state] = len(trail)
            trail.append(state)
            state = successor[state]
        if state in position:
            word = tuple(x for x, _ in trail[position[state]:])
            word = min(word[j:] + word[:j] for j in range(len(word)))
            cycles.append(word)
        done.update(trail)
    return sorted(cycles)


def hv_cycles(c):
    positive = [r for r in range(1, isqrt(c) + 1) if c % (r * r) == 0]
    digits = sorted(positive + [-r for r in positive])
    allowed = set(digits)
    successor = {}
    for x in digits:
        for y in digits:
            z = -x + y + c // (y * y)
            if z in allowed:
                successor[x, y] = (y, z)
    cycles = graph_cycles(successor)
    for word in cycles:
        n = len(word)
        assert all(word[(i - 1) % n] + word[(i + 1) % n]
                   == word[i] + c // (word[i] ** 2) for i in range(n))
        assert all(c % (r * r) == 0 for r in word)
    return digits, successor, cycles


def main():
    histogram = Counter()
    found = []
    vertices = edges = 0
    for c in range(1, 513):
        digits, successor, cycles = hv_cycles(c)
        vertices += len(digits) ** 2
        edges += len(successor)
        for word in cycles:
            histogram[len(word)] += 1
            found.append({"c": c, "native_period": len(word), "word": word})
    result = {
        "status": "EXACT_FINITE_DIAGNOSTIC_ONLY",
        "sample": "Every integer c with 1 <= c <= 512, exactly once",
        "domain": "Nonzero ordinary integral periodic orbits; all cyclic coordinates nonzero",
        "finite_completeness": "Each c uses all signed r with r*r dividing c, all ordered pairs, all graph cycles",
        "vertices_examined": vertices,
        "retained_edges": edges,
        "cycles_by_native_period": dict(sorted(histogram.items())),
        "fixed_only_guess_survives_sample": all(row["native_period"] == 1 for row in found),
        "all_cycles_in_sample": found,
        "global_claim": "NONE: a finite sample does not settle arbitrary c",
    }
    output = json.dumps(result, indent=2)
    Path(__file__).with_name("B1_EXACT_PROBE_OUTPUT.json").write_text(output + "\n")
    print(output)


if __name__ == "__main__":
    main()
