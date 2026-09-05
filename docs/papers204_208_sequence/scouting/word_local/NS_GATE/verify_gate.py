#!/usr/bin/env python3
"""Independent NS candidate checks, with no author/historical imports.

Literal updates scan all earlier positions; recurrence is detected by orbit
walking; core words are generated recursively; fibre counting uses a
last-value dynamic program separately from the author's cut expression.
"""

from collections import Counter
from functools import lru_cache
from itertools import permutations, product
from math import comb, factorial
import hashlib
import json


CHECKS = Counter()


def require(statement, label, witness=None):
    CHECKS[label] += 1
    if not statement:
        raise AssertionError((label, witness))


def literal(word, weak=False):
    answer = []
    for i, value in enumerate(word):
        smaller = [j for j in range(i)
                   if (word[j] <= value if weak else word[j] < value)]
        answer.append(i-max(smaller) if smaller else 0)
    return tuple(answer)


def generate_core(n):
    prefixes = [((0,), 0)]
    for i in range(1, n):
        updated = []
        for prefix, barrier in prefixes:
            updated.append((prefix+(0,), i))
            for value in sorted({1, i-barrier}):
                updated.append((prefix+(value,), barrier))
        prefixes = updated
    return {word for word, _ in prefixes}


def locate_blocks(word):
    zero_positions = [i for i, value in enumerate(word) if value == 0]
    endpoints = zero_positions[1:]+[len(word)]
    return [(r, end-r-1) for r, end in zip(zero_positions, endpoints)
            if end > r+1]


def decoded_endpoint(word):
    barrier = 0
    output = []
    for i, value in enumerate(word):
        if value == 0:
            barrier = i
            output.append(0)
        else:
            output.append(i-barrier if word[i-1] < value else 1)
    return tuple(output)


def flip_core(word):
    result = list(word)
    for r, length in locate_blocks(word):
        for j in range(2, length+1):
            result[r+j] = j+1-word[r+j]
    return tuple(result)


@lru_cache(maxsize=None)
def last_value_dp(r, length, mask):
    if length == 0:
        return 1
    counts = {v: 1 for v in range(1, r+2)}
    for j in range(2, length+1):
        ascending = bool(mask & (1 << (j-2)))
        counts = {v: sum(number for old, number in counts.items()
                         if (old < v) == ascending)
                  for v in range(1, r+j+1)}
    return sum(counts.values())


@lru_cache(maxsize=None)
def cut_expression(r, length, mask):
    total = 0
    allowed = [j for j in range(2, length+1) if mask & (1 << (j-2))]
    for flags in product((0, 1), repeat=len(allowed)):
        cut_starts = [1]+[j for j, bit in zip(allowed, flags) if bit]+[length+1]
        factor = 1
        for start, end in zip(cut_starts, cut_starts[1:]):
            factor *= comb(r+end-1, end-start)
        total += (-1)**(len(allowed)-sum(flags))*factor
    return total


def target_count(word, time, core, counter):
    if word not in core:
        return 0
    answer = 1
    for r, length in locate_blocks(word):
        mask = 0
        for j in range(2, length+1):
            ascent = word[r+j] == (j if time % 2 == 0 else 1)
            mask |= int(ascent) << (j-2)
        answer *= counter(r, length, mask)
    return answer


def walk_orbit(start, arrows):
    visited = {}
    point = start
    while point not in visited:
        visited[point] = len(visited)
        point = arrows[point]
    return visited[point], len(visited)-visited[point]


def fibonacci(index):
    values = [0, 1]
    for _ in range(index-1):
        values.append(values[-1]+values[-2])
    return values[index]


def dynamical_lane(digest):
    records = []
    for n in range(1, 9):
        states = tuple(product(*(range(i+1) for i in range(n))))
        arrows = {x: literal(x) for x in states}
        core = generate_core(n)
        actual_core = set()
        heights = Counter()
        fibres = {t: Counter() for t in range(2, 6)}
        fixed = 0
        for x in states:
            h, period = walk_orbit(x, arrows)
            heights[h] += 1
            require(period in (1, 2), "literal_orbit_period")
            if h == 0:
                actual_core.add(x)
            fixed += arrows[x] == x
            y = arrows[x]
            require(tuple(i for i, v in enumerate(x) if v == 0) ==
                    tuple(i for i, v in enumerate(y) if v == 0), "zero_barriers")
            for r, length in locate_blocks(y):
                for j in range(2, length+1):
                    require(y[r+j] == 1 or y[r+j] >= y[r+j-1]+1,
                            "first_image_one_or_rise")
            z = arrows[y]
            require(z == decoded_endpoint(x), "exact_two_step_ascent_decoder")
            if x in core:
                require(arrows[x] == flip_core(x), "core_bit_complement")
            current = z
            for time in range(2, 6):
                fibres[time][current] += 1
                current = arrows[current]
            digest.update(repr((n, x, y, z, h, period)).encode("ascii"))
        require(actual_core == core, "generated_core_equals_actual_recurrence")
        require(set(arrows[arrows[x]] for x in states) == core,
                "second_image_equals_generated_core")
        require(len(core) == fibonacci(2*n-1), "fibonacci_recurrent_count")
        require(fixed == fibonacci(n+1), "fibonacci_fixed_count")
        require(max(heights) == (0 if n <= 2 else 1 if n == 3 else 2),
                "sharp_global_height")
        for time, counts in fibres.items():
            for target in states:
                expected = target_count(target, time, core, last_value_dp)
                formula = target_count(target, time, core, cut_expression)
                require(counts[target] == expected, "every_target_vs_last_value_dp")
                require(expected == formula, "last_value_dp_vs_cut_formula")
            require(sum(counts.values()) == factorial(n), "fibre_mass")
        records.append({"n": n, "states": len(states),
                        "image": len(set(arrows.values())), "core": len(core),
                        "fixed": fixed, "depths": dict(sorted(heights.items()))})
    return records


def static_lane(digest):
    block_patterns = direct_words = 0
    for r in range(5):
        for length in range(1, 7):
            for mask in range(1 << (length-1)):
                block_patterns += 1
                actual = last_value_dp(r, length, mask)
                expected = cut_expression(r, length, mask)
                require(actual == expected, "flagged_block_dp_vs_cut")
                digest.update(repr((r, length, mask, actual)).encode("ascii"))
    for r in range(4):
        for length in range(1, 6):
            counts = Counter()
            for word in product(*(range(1, r+j+1) for j in range(1, length+1))):
                direct_words += 1
                mask = sum(int(a < b) << j
                           for j, (a, b) in enumerate(zip(word, word[1:])))
                counts[mask] += 1
            for mask in range(1 << (length-1)):
                require(counts[mask] == last_value_dp(r, length, mask),
                        "flagged_direct_words_vs_dp")
    require(last_value_dp(0, 2, 1) == 1 and last_value_dp(1, 2, 1) == 3,
            "global_flag_offset_matters")
    return {"flagged_block_patterns": block_patterns,
            "flagged_direct_words": direct_words}


def permutation_adapter_lane():
    total = 0
    for n in range(1, 8):
        observed_codes = set()
        for pi in permutations(range(1, n+1)):
            total += 1
            code = tuple(sum(pi[j] > pi[i] for j in range(i)) for i in range(n))
            observed_codes.add(code)
            ascents = {i for i in range(n-1) if code[i] < code[i+1]}
            descents = {i for i in range(n-1) if pi[i] > pi[i+1]}
            zeroes = {i for i, value in enumerate(code) if value == 0}
            records = {i for i in range(n) if all(pi[j] < pi[i] for j in range(i))}
            require(ascents == descents, "classical_code_ascent_descent_adapter")
            require(zeroes == records, "classical_code_zero_record_adapter")
        require(len(observed_codes) == factorial(n), "classical_code_bijection")
    # The weak and strict nearest-predecessor conventions differ literally.
    require(literal((0, 1, 1)) == (0, 1, 2), "strict_tie_boundary")
    require(literal((0, 1, 1), weak=True) == (0, 1, 1), "weak_pd_tie_boundary")
    return total


def main():
    digest = hashlib.sha256()
    dynamics = dynamical_lane(digest)
    static = static_lane(digest)
    permutations_checked = permutation_adapter_lane()
    print(json.dumps({"scope": "INDEPENDENT_NS_CANDIDATE_GATE_NOT_PAPER_REVIEW",
                      "dynamics": dynamics, **static,
                      "permutations_checked": permutations_checked,
                      "checks": dict(sorted(CHECKS.items())),
                      "total_checks": sum(CHECKS.values()),
                      "enumeration_sha256": digest.hexdigest(),
                      "result": "PASS_BOUNDED_MATH_AND_STATIC_ADAPTER_ONLY",
                      "owner_status": "NOT_DECIDED_BY_ENUMERATION",
                      "external_status": "HOLD_EXTERNAL"},
                     sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
