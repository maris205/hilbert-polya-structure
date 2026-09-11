#!/usr/bin/env python3
"""Independent CRC3 gate: first occurrences, orbit walks, record-set language.

No imports from the author's verifier. Full source sets are compared for
every target through n=10, not only their cardinalities. Standard library only.
"""
from collections import Counter
from functools import lru_cache
from hashlib import sha256
from itertools import product
import json
from math import prod


checks = 0
digest = sha256()


def require(condition):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(checks)


def records_first_occurrence(word):
    n = len(word)
    result = []
    for start in range(n):
        positions = [n] * 4
        for offset in range(n):
            letter = word[(start + offset) % n]
            positions[letter] = min(positions[letter], offset)
        result.append(sum(positions[v] < min(positions[v + 1:] + [n])
                          for v in range(1, 4)))
    return tuple(result)


def records_literal(word):
    n = len(word)
    return tuple(sum(all(word[(i + j) % n] > word[(i + k) % n]
                         for k in range(j)) for j in range(n))
                 for i in range(n))


def in_image(word):
    return min(word) == 1 and all(word[i] - word[(i + 1) % len(word)] <= 1
                                  for i in range(len(word)))


def in_core(word):
    return min(word) == 1 and all(abs(word[i] - word[(i + 1) % len(word)]) <= 1
                                  for i in range(len(word)))


def target_runs(target):
    roots = [i for i, value in enumerate(target) if value == 1]
    if not roots:
        return None
    n = len(target)
    runs = []
    for k, root in enumerate(roots):
        previous = roots[k - 1]
        positions = []
        j = (previous + 1) % n
        while j != root:
            positions.append(j)
            j = (j + 1) % n
        runs.append((root, tuple(positions)))
    return runs


@lru_cache(maxsize=None)
def record_language(target_run, maximum):
    """Prepend letters to the SET of suffix record values, then accept size.

    The terminal maximum is not part of the returned run word. This does not
    use the author's last-3 position or terminal-2-run decoder.
    """
    states = {(1 << maximum, ())}
    for required in reversed(target_run):
        following = set()
        for suffix_records, suffix_word in states:
            for letter in range(1, maximum):
                bigger = suffix_records & ~((1 << (letter + 1)) - 1)
                new_records = bigger | (1 << letter)
                if new_records.bit_count() == required:
                    following.add((new_records, (letter,) + suffix_word))
        states = following
    return tuple(sorted(word for _, word in states))


def inverse_language(target):
    runs = target_runs(target)
    if runs is None:
        return set()
    sources = set()
    for maximum in range(1, 4):
        choices = [record_language(tuple(target[i] for i in positions), maximum)
                   for _, positions in runs]
        for selected in product(*choices):
            word = [0] * len(target)
            for (root, positions), values in zip(runs, selected):
                word[root] = maximum
                for position, value in zip(positions, values):
                    word[position] = value
            sources.add(tuple(word))
    return sources


def proposed_fibre(target):
    if not in_image(target):
        return 0
    factors = []
    for _, positions in target_runs(target):
        run = tuple(target[i] for i in positions)
        if 3 not in run:
            factors.append(len(run) + 1)
        else:
            last_three = max(i for i, v in enumerate(run) if v == 3)
            factors.append(len(run) - last_three - 1)
    return prod(factors) + int(3 not in target) + int(max(target) == 1)


@lru_cache(maxsize=None)
def compositions(n):
    if n == 0:
        return ((),)
    return tuple((first,) + rest for first in range(1, n + 1)
                 for rest in compositions(n - first))


def expected_optimal_parts(n):
    if n == 1:
        return {(1,)}
    a, r = divmod(n, 3)
    if r == 0:
        return {(3,) * a}
    if r == 1:
        return {tuple(sorted((4,) + (3,) * (a - 1))),
                (2, 2) + (3,) * (a - 1)}
    return {(2,) + (3,) * a}


def integer_break(n):
    if n == 1:
        return 1
    a, r = divmod(n, 3)
    return 3 ** a if r == 0 else 4 * 3 ** (a - 1) if r == 1 else 2 * 3 ** a


def expected_maximizer(target, optimal_parts):
    n = len(target)
    if n == 1:
        return target == (1,)
    if n == 2:
        return target in {(1, 1), (1, 2), (2, 1)}
    if 3 in target or 1 not in target or 2 not in target:
        return False
    parts = tuple(sorted(len(positions) + 1 for _, positions in target_runs(target)))
    return parts in optimal_parts


def main():
    optimum_by_n = {}
    for n in range(1, 15):
        values = [(parts, prod(parts)) for parts in compositions(n)]
        greatest = max(value for _, value in values)
        optimal = {tuple(sorted(parts)) for parts, value in values if value == greatest}
        require(greatest == integer_break(n))
        require(optimal == expected_optimal_parts(n))
        optimum_by_n[n] = optimal

    rows = []
    total_sources = 0
    full_source_set_targets = 0
    lucas_previous, lucas_current = 2, 3
    pell_previous, pell_current = 2, 2
    for n in range(1, 11):
        words = list(product((1, 2, 3), repeat=n))
        forward = {word: records_first_occurrence(word) for word in words}
        actual_inverse = {}
        for word, target in forward.items():
            actual_inverse.setdefault(target, set()).add(word)
            if n <= 7:
                require(target == records_literal(word))
        image = set(forward.values())
        second_image = {forward[word] for word in image}
        require(image == {word for word in words if in_image(word)})
        require(second_image == {word for word in words if in_core(word)})
        require(len(image) == lucas_current - 2 ** n)
        require(len(second_image) == pell_current + 1 - 2 ** n)
        tails = Counter()
        periods = Counter()
        maximum_fibre = max(map(len, actual_inverse.values()))
        expected_maximum = 3 if n <= 2 else 1 + integer_break(n)
        require(maximum_fibre == expected_maximum)
        maximizers = []
        for word in words:
            seen = {}
            current = word
            while current not in seen:
                seen[current] = len(seen)
                current = forward[current]
            tail = seen[current]
            period = len(seen) - tail
            tails[tail] += 1
            periods[period] += 1
            require(tail <= (1 if n <= 2 else 2))
            require((tail == 0) == in_core(word))
            require(period == (1 if forward[current] == current else 2))
            require(forward[forward[forward[forward[word]]]] == forward[forward[word]])
            if in_core(word):
                require(forward[word] == tuple(max(word) + 1 - letter for letter in word))
            require((forward[word] == word) == (word == (1,) * n))
            reconstructed = inverse_language(word)
            actual = actual_inverse.get(word, set())
            require(reconstructed == actual)
            require(len(reconstructed) == proposed_fibre(word))
            is_maximum = len(actual) == maximum_fibre
            require(is_maximum == expected_maximizer(word, optimum_by_n[n]))
            if is_maximum:
                maximizers.append(word)
            digest.update(json.dumps([word, forward[word], tail, period, len(actual)],
                                     separators=(",", ":")).encode())
            digest.update(b"\n")
        require(max(tails) == (1 if n <= 2 else 2))
        sharp = (2,) if n == 1 else (2, 2) if n == 2 else (1,) * (n - 2) + (2, 3)
        sharp_seen = {}
        current = sharp
        while current not in sharp_seen:
            sharp_seen[current] = len(sharp_seen)
            current = forward[current]
        require(sharp_seen[current] == (1 if n <= 2 else 2))
        rows.append({"n": n, "sources": len(words), "image": len(image),
                     "core": len(second_image), "fixed": 1,
                     "strict_two_cycles": (len(second_image) - 1) // 2,
                     "tail_counts": dict(sorted(tails.items())),
                     "maximum_fibre": maximum_fibre,
                     "maximizing_targets": len(maximizers)})
        total_sources += len(words)
        full_source_set_targets += len(words)
        lucas_previous, lucas_current = lucas_current, 3 * lucas_current - lucas_previous
        pell_previous, pell_current = pell_current, 2 * pell_current + pell_previous
    print(json.dumps({"status": "PASS", "representation": "first-occurrence-records / direct-orbit-walk / suffix-record-set-language",
                      "full_source_set_target_comparisons": full_source_set_targets,
                      "total_sources": total_sources,
                      "literal_forward_cutoff": 7,
                      "full_carrier_cutoff": 10,
                      "integer_composition_cutoff": 14,
                      "assertions": checks, "enumeration_sha256": digest.hexdigest(),
                      "profiles": rows}, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
