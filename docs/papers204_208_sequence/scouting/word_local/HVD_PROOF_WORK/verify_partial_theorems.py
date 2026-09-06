#!/usr/bin/env python3
"""Proof-directed HVD audits in the original n=1..6 boxes, not an atlas.

No cycles, transient-height census, image census or all-target histogram is
computed. The only fibre evaluated is the proved weak-unimodal path fibre.
All output goes to stdout; no imports may write outside this directory.
"""
from itertools import product
from math import comb
from pathlib import Path
import json
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from visibility_local_pilot import visibility as literal_step


def graph(word):
    return {(i, j) for i in range(len(word)) for j in range(i + 1, len(word))
            if all(word[k] < min(word[i], word[j]) for k in range(i + 1, j))}


def degrees(word):
    edges = graph(word)
    return tuple(sum(i in edge for edge in edges) for i in range(len(word)))


def path_target(n):
    return (0,) if n == 1 else (1,) + (2,) * (n - 2) + (1,)


def unimodal(word):
    return any(all(word[i] <= word[i + 1] for i in range(peak))
               and all(word[i] >= word[i + 1] for i in range(peak, len(word) - 1))
               for peak in range(len(word)))


def path_fibre(n, alphabet):
    return sum(comb(2 * a + n - 1, n - 1) for a in range(alphabet))


def low_fixed_test(word):
    """Input has endpoints 1 and all interior entries in {2,3}."""
    high = [i for i, value in enumerate(word) if value == 3]
    if not high:
        return True
    return (len(high) % 2 == 0
            and all((high[j + 1] - high[j] >= 2) == (j % 2 == 0)
                    for j in range(len(high) - 1)))


def low_fixed_count(n):
    return 1 + sum(comb(n - 2 * q - 1, q + 1)
                   for q in range(1, (n - 2) // 3 + 1))


def expansion(word):
    result = [1]
    for i, value in enumerate(word):
        if i:
            result.append(2)
        result.append(value + 2)
    return tuple(result + [1])


def audit(n):
    counters = {name: 0 for name in (
        "words", "literal_matches", "path_equivalence", "image_bounds",
        "endpoint_erosion", "permanent_twos", "endpoint_clock",
        "reduction_inputs", "reduction_active_sites", "low_family_inputs",
        "low_family_fixed", "separated_reduction_inputs")}
    path_counts = {alphabet: 0 for alphabet in range(1, n + 1)}
    for word in product(range(n), repeat=n):
        counters["words"] += 1
        nxt = degrees(word)
        assert nxt == literal_step(word), ("literal", word, nxt)
        counters["literal_matches"] += 1
        is_path = nxt == path_target(n)
        assert is_path == unimodal(word), ("path", word, nxt)
        counters["path_equivalence"] += 1
        if is_path:
            for alphabet in range(max(word) + 1, n + 1):
                path_counts[alphabet] += 1

        if n == 1:
            assert nxt == (0,)
        else:
            assert 1 <= nxt[0] <= n - 1 and 1 <= nxt[-1] <= n - 1
            assert all(2 <= a <= n - 1 for a in nxt[1:-1])
        counters["image_bounds"] += 1

        twice = degrees(nxt)
        if n >= 3:
            assert twice[0] <= max(1, nxt[0] - 1)
            assert twice[-1] <= max(1, nxt[-1] - 1)
            counters["endpoint_erosion"] += 2
            for i in range(1, n - 1):
                if nxt[i] == 2:
                    assert twice[i] == 2, ("permanent_two", word, i)
                    counters["permanent_twos"] += 1
        state = word
        for _ in range(max(1, n - 1)):
            state = degrees(state)
        assert (state == (0,) if n == 1 else state[0] == state[-1] == 1)
        counters["endpoint_clock"] += 1

        if n >= 2 and word[0] == word[-1] == 1 and all(a >= 2 for a in word[1:-1]):
            counters["reduction_inputs"] += 1
            active = [i for i in range(1, n - 1) if word[i] > 2]
            active_set = set(active)
            reduced = tuple(word[i] for i in active)
            reduced_degree = degrees(reduced)
            offsets = []
            for j, i in enumerate(active):
                offset = int(i - 1 not in active_set) + int(i + 1 not in active_set)
                offsets.append(offset)
                assert nxt[i] == reduced_degree[j] + offset, ("reduction", word, i)
                counters["reduction_active_sites"] += 1
            assert all(nxt[i] == 2 for i in range(1, n - 1) if i not in active_set)
            assert nxt[0] == nxt[-1] == 1
            if len(active) >= 2 and all(b == 2 for b in offsets):
                shifted = tuple(word[i] - 2 for i in active)
                assert tuple(nxt[i] - 2 for i in active) == degrees(shifted)
                assert all(nxt[i] > 2 for i in active)
                counters["separated_reduction_inputs"] += 1

            if all(a in (2, 3) for a in word[1:-1]):
                counters["low_family_inputs"] += 1
                fixed = word == nxt
                assert fixed == low_fixed_test(word), ("low_fixed", word, nxt)
                counters["low_family_fixed"] += int(fixed)

    assert counters["words"] == n ** n
    for alphabet, count in path_counts.items():
        assert count == path_fibre(n, alphabet), ("fibre", n, alphabet, count)
    if n >= 2:
        assert counters["low_family_fixed"] == low_fixed_count(n)
    return {"n": n, "status": "PASS_PARTIAL_THEOREMS_ONLY", "checks": counters,
            "path_fibre_by_alphabet": path_counts,
            "proved_low_fixed_family_size": low_fixed_count(n)}


def main():
    records = [audit(n) for n in range(1, 7)]
    # A formula-derived single fixed point illustrates the embedding.
    # This is NOT a new full length-seven box.
    embedded = expansion((1, 2, 1))
    assert embedded == (1, 3, 2, 4, 2, 3, 1)
    assert degrees(embedded) == embedded
    print(json.dumps({"status": "PASS_BOUNDED_PARTIAL_PROOF_AUDIT",
                      "full_boxes": "original n=1..6 only",
                      "new_full_boxes": 0,
                      "not_computed": ["six_rule_atlas", "cycles", "global_height",
                                       "image_census", "all_target_fibre_histogram"],
                      "records": records,
                      "derived_embedding_single_sentinel": list(embedded)},
                     sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
