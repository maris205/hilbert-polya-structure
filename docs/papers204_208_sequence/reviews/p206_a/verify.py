#!/usr/bin/env python3
"""P206 A: independent literal/orbit/skyline/template audit, no file inputs.

Written for manuscript A without reading author or candidate checker bodies.
All imports are standard-library. Complete deterministic JSON is stdout.
The weak-template adapter is an adverse value test, not a novelty proof.
"""
from collections import Counter, defaultdict
from hashlib import sha256
from itertools import product
import json


CHECKS = 0
RECORDS = sha256()


def check(truth, label, context=None):
    global CHECKS
    CHECKS += 1
    if not truth:
        raise AssertionError((label, context))


def record(value):
    RECORDS.update((json.dumps(value, separators=(",", ":")) + "\n").encode())


def literal(word):
    n = len(word)
    out = []
    for start in range(n):
        ceiling = 0
        count = 0
        for step in range(n):
            value = word[(start + step) % n]
            if value > ceiling:
                ceiling = value
                count += 1
        out.append(count)
    return tuple(out)


def pointer_depth(word):
    n = len(word)
    pointers = []
    for start in range(n):
        pointers.append(next(((start + d) % n for d in range(1, n)
                              if word[(start + d) % n] > word[start]), None))
    result = []
    for start in range(n):
        depth = 1
        cursor = pointers[start]
        while cursor is not None:
            depth += 1
            cursor = pointers[cursor]
        result.append(depth)
    return tuple(result)


def image_predicate(word, symmetric=False):
    return min(word) == 1 and all(
        abs(a - b) <= 1 if symmetric else a - b <= 1
        for a, b in zip(word, word[1:] + word[:1]))


def orbit_atlas(successors):
    """Walk to an already classified vertex or detect a new local cycle."""
    heights, periods = {}, {}
    for start in successors:
        if start in heights:
            continue
        trail, positions = [], {}
        cursor = start
        while cursor not in heights and cursor not in positions:
            positions[cursor] = len(trail)
            trail.append(cursor)
            cursor = successors[cursor]
        if cursor in positions:
            entry = positions[cursor]
            cycle = trail[entry:]
            for vertex in cycle:
                heights[vertex] = 0
                periods[vertex] = len(cycle)
            prefix = trail[:entry]
        else:
            prefix = trail
        for vertex in reversed(prefix):
            heights[vertex] = heights[successors[vertex]] + 1
            periods[vertex] = periods[successors[vertex]]
    return heights, periods


def skyline_sources(target):
    """Whole-circle reverse transducer, with a fixed global-maximum anchor.

    A skyline is the increasing list of strict suffix-record VALUES.
    Prepending a gives output 1 + the number of skyline values greater
    than a; it replaces the skyline by a followed by those greater values.
    This does not split the input into the author's tail-count formula.
    """
    if 1 not in target:
        return set()
    n = len(target)
    anchor = target.index(1)
    positions = [(anchor - d) % n for d in range(1, n)]
    results = set()
    for maximum in (1, 2, 3):
        partial = [0] * n
        partial[anchor] = maximum

        def descend(depth, skyline):
            if depth == n - 1:
                results.add(tuple(partial))
                return
            position = positions[depth]
            for letter in range(1, maximum + 1):
                retained = tuple(v for v in skyline if v > letter)
                if 1 + len(retained) == target[position]:
                    partial[position] = letter
                    descend(depth + 1, (letter,) + retained)

        descend(0, (maximum,))
    return results


def root_runs(target):
    """Runs on original labelled positions, beginning after each root."""
    roots = [i for i, value in enumerate(target) if value == 1]
    if not roots:
        return None
    runs = []
    n = len(target)
    for root in roots:
        run = []
        position = (root + 1) % n
        while target[position] != 1:
            run.append(position)
            position = (position + 1) % n
        runs.append(tuple(run))
    return roots, runs


def binary_template_count(symbols):
    """[z^2] of Myers--Wilf Thm 6, equations (10),(13).

    Empty template has one empty word. A nonempty feasible template begins
    W, normalized to S because its first position is vacuously strong.
    For nonempty prefixes (f(1),f(2)), W:(a,b)->(a,a+b), O:(a,b)->(0,b-a).
    """
    if not symbols:
        return 1
    if symbols[0] == "O":
        return 0
    one, two = 1, 2
    for symbol in symbols[1:]:
        if symbol == "W":
            one, two = one, one + two
        else:
            one, two = 0, two - one
    return two


def binary_template_words(symbols):
    """Definition-level DFS; independent of the operator count."""
    words = []

    def descend(prefix, maximum):
        if len(prefix) == len(symbols):
            words.append(prefix)
            return
        for letter in (1, 2):
            weak = letter >= maximum
            if weak == (symbols[len(prefix)] == "W"):
                descend(prefix + (letter,), max(maximum, letter))

    descend((), 0)
    return words


def full_template_adapter(target):
    """Return exact reconstructed sets and counts, split by source maximum."""
    partition = root_runs(target)
    if partition is None:
        return set(), (0, 0, 0)
    roots, runs = partition
    choices, operator_product = [], 1
    for run in runs:
        symbols = tuple("W" if target[i] == 2 else "O" for i in reversed(run))
        words = binary_template_words(symbols)
        count = binary_template_count(symbols)
        check(len(words) == count, "template operator vs definition", symbols)
        choices.append(words)
        operator_product *= count
    maximum_three = set()
    for combination in product(*choices):
        source = [3] * len(target)
        for run, reverse_word in zip(runs, combination):
            for position, letter in zip(reversed(run), reverse_word):
                source[position] = letter
        maximum_three.add(tuple(source))
    check(len(maximum_three) == operator_product, "labelled product injective", target)
    maximum_two = {tuple(3 - value for value in target)} if 3 not in target else set()
    maximum_one = {(1,) * len(target)} if all(v == 1 for v in target) else set()
    return (maximum_one | maximum_two | maximum_three,
            (len(maximum_one), len(maximum_two), operator_product))


def stated_fibre(target):
    if not image_predicate(target):
        return 0
    _, runs = root_runs(target)
    result = 1
    for run in runs:
        values = tuple(target[i] for i in run)
        if 3 not in values:
            factor = len(values) + 1
        else:
            factor = 0
            for value in reversed(values):
                if value != 2:
                    break
                factor += 1
        result *= factor
    return result + int(3 not in target) + int(all(v == 1 for v in target))


def claimed_j(n):
    if n == 1:
        return 1
    quotient, residue = divmod(n, 3)
    if residue == 0:
        return 3 ** quotient
    if residue == 1:
        return 4 * 3 ** (quotient - 1)
    return 2 * 3 ** quotient


def equality_target(target):
    n = len(target)
    if n <= 2:
        return target in ({(1,)} if n == 1 else {(1, 1), (1, 2), (2, 1)})
    if 1 not in target or 3 in target or max(target) == 1:
        return False
    _, runs = root_runs(target)
    parts = sorted(len(run) + 1 for run in runs)
    if n % 3 == 0:
        return all(part == 3 for part in parts)
    if n % 3 == 1:
        return (parts.count(4) == 1 and all(p in (3, 4) for p in parts)) or (
            parts.count(2) == 2 and all(p in (2, 3) for p in parts))
    return parts.count(2) == 1 and all(p in (2, 3) for p in parts)


def main():
    boxes = []
    total_states = 0
    maximum_branch_checks = 0
    L, P = [2, 3], [2, 2]
    for n in range(2, 101):
        L.append(3 * L[-1] - L[-2])
        P.append(2 * P[-1] + P[-2])
    composition_dp = [1]
    for n in range(1, 101):
        composition_dp.append(max(part * composition_dp[n - part]
                                  for part in range(1, n + 1)))
        check(composition_dp[n] == claimed_j(n), "composition product", n)
    for n in range(1, 12):
        states = list(product((1, 2, 3), repeat=n))
        total_states += len(states)
        successors = {}
        inverse = defaultdict(set)
        for state in states:
            output = literal(state)
            successors[state] = output
            inverse[output].add(state)
            check(output == pointer_depth(state), "literal vs nearest-greater", state)
        heights, periods = orbit_atlas(successors)
        first = set(successors.values())
        second = {successors[y] for y in first}
        D = {state for state in states if image_predicate(state)}
        C = {state for state in states if image_predicate(state, True)}
        check(first == D, "first image", n)
        check(second == C, "second image", n)
        check(len(D) == L[n] - 2 ** n, "first-image count", n)
        check(len(C) == P[n] + 1 - 2 ** n, "core count", n)
        check({x for x in states if heights[x] == 0} == C, "exact recurrent set", n)
        check({x for x in states if successors[x] == x} == {(1,) * n}, "unique fixed", n)
        check(max(heights.values()) == (1 if n <= 2 else 2), "sharp height", n)
        maximum = max(map(len, inverse.values()))
        check(maximum == (3 if n <= 2 else 1 + claimed_j(n)), "uniform max", n)
        maximizing = set()
        zero_count = 0
        for target in states:
            sources = inverse.get(target, set())
            skyline = skyline_sources(target)
            adapted, branches = full_template_adapter(target)
            check(skyline == sources, "whole-circle skyline exact sources", target)
            check(adapted == sources, "full template exact sources", target)
            literal_branches = tuple(sum(max(x) == m for x in sources) for m in (1, 2, 3))
            check(branches == literal_branches, "source maximum branches", target)
            maximum_branch_checks += 3
            check(sum(branches) == stated_fibre(target) == len(sources), "full Psi", target)
            check((not sources) == (target not in D), "zero interface", target)
            zero_count += int(not sources)
            actual_max = len(sources) == maximum
            check(actual_max == equality_target(target), "all labelled equality targets", target)
            if actual_max:
                maximizing.add(target)
            R2 = successors[successors[target]]
            R4 = successors[successors[R2]]
            check(R4 == R2, "fourth equals second", target)
            check(periods[target] in (1, 2), "period spectrum", target)
            if target in C:
                check(successors[target] == tuple(max(target) + 1 - v for v in target),
                      "core reflection", target)
                check(periods[target] == (1 if target == (1,) * n else 2),
                      "strict core periods", target)
            if target in D:
                check(literal(tuple(4 - v for v in target)) == target,
                      "explicit first-image source", target)
            record([target, successors[target], heights[target], periods[target],
                    sorted(sources), list(branches), actual_max])
        witness = (2,) if n == 1 else ((2, 2) if n == 2 else (1,) * (n - 2) + (2, 3))
        check(heights[witness] == max(heights.values()), "sharp witness", n)
        boxes.append({"n": n, "states_and_targets": len(states), "image": len(D),
                      "core": len(C), "height": max(heights.values()),
                      "strict_two_cycles": (len(C) - 1) // 2, "zero_targets": zero_count,
                      "maximum_fibre": maximum, "maximizing_labelled_targets": len(maximizing),
                      "height_census": sorted(Counter(heights.values()).items())})
    template_boxes = []
    for length in range(0, 13):
        population = Counter()
        for word in product((1, 2), repeat=length):
            ceiling = 0
            symbols = []
            for letter in word:
                symbols.append("W" if letter >= ceiling else "O")
                ceiling = max(ceiling, letter)
            population[tuple(symbols)] += 1
        for symbols in product(("W", "O"), repeat=length):
            check(binary_template_count(symbols) == population[symbols],
                  "all binary template counts including initial O", symbols)
        template_boxes.append({"length": length, "words": 2 ** length,
                               "templates": 2 ** length})
    x, y = (1, 2, 3, 1, 2, 3), (1, 2, 3, 2, 1, 3)
    check(Counter(x) == Counter(y) and literal(x)[0] == literal(y)[0], "marginal control")
    check(literal(x) != literal(y), "marginal non-adapter control")
    output = {"status": "PASS", "review": "P206_A_INDEPENDENT",
              "bounds": "full ternary n=1..11; all binary templates lengths 0..12; integer products 1..100",
              "imports": "standard-library only; no file reads or author/gate imports",
              "assertions": CHECKS, "states_and_targets": total_states,
              "source_maximum_branch_comparisons": maximum_branch_checks,
              "full_source_sets": "literal inverse == reverse skyline == reversed weak-template product",
              "dynamic_boxes": boxes, "template_boxes": template_boxes,
              "control": {"x": x, "y": y, "Rx": literal(x), "Ry": literal(y)},
              "record_sha256": RECORDS.hexdigest(),
              "scope": "finite checks support, but do not replace, all-n proof and adverse adapter"}
    print(json.dumps(output, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
