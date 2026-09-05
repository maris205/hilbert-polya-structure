#!/usr/bin/env python3
"""Independent inverse formulas and exact historical-literal comparison."""
from collections import Counter, deque
from functools import lru_cache
from itertools import permutations
from math import factorial
from pathlib import Path
import hashlib
import importlib.util
import json
from verify_breadth import (decreasing_run_front, insertion_tableau,
                           transpose_insertion_read, plane_words,
                           breadth_preorder, length_half_pair, matchings)


def inverse_run_count(target):
    """Admissible original descending-run cuts, with maximality boundaries."""
    n = len(target)
    @lru_cache(None)
    def rec(i, last):
        if i == n:
            return 1
        count = 0
        for j in range(i+1, n+1):
            block = target[i:j]
            source = block[1:] + block[:1]
            if all(source[k] > source[k+1] for k in range(len(source)-1)):
                if last < source[0]:
                    count += rec(j, source[-1])
        return count
    return rec(0, 0)


def tableau_number(shape):
    hooks = 1
    for i, row in enumerate(shape):
        for j in range(row):
            hooks *= row-j + sum(shape[k] > j for k in range(i+1, len(shape)))
    return factorial(sum(shape)) // hooks


def breadth_decode_preorder(word):
    children = [[] for _ in word]
    queue, pos = deque([0]), 1
    while queue:
        node = queue.popleft()
        children[node] = list(range(pos, pos+word[node]))
        queue.extend(children[node])
        pos += word[node]
    assert pos == len(word)
    result = []
    def visit(node):
        result.append(len(children[node]))
        for child in children[node]:
            visit(child)
    visit(0)
    return tuple(result)


def main():
    inverse_checks, tableau_checks, traversal_checks = 0, 0, 0
    identity_fibres = []
    for n in range(1, 8):
        states = tuple(permutations(range(1, n+1)))
        fibres = Counter(map(decreasing_run_front, states))
        for target in states:
            assert inverse_run_count(target) == fibres[target]
            inverse_checks += 1
        identity_fibres.append(fibres[tuple(range(1, n+1))])
    for n in range(1, 9):
        states = tuple(permutations(range(1, n+1)))
        fibres = Counter(map(transpose_insertion_read, states))
        for target in states:
            p = insertion_tableau(target)
            rowword = tuple(x for row in reversed(p) for x in row)
            expected = tableau_number(tuple(map(len, p))) if rowword == target else 0
            assert fibres[target] == expected
            tableau_checks += 1
    for n in range(1, 11):
        for word in plane_words(n):
            assert breadth_decode_preorder(breadth_preorder(word)) == word
            traversal_checks += 1
    old_path = Path(__file__).resolve().parents[3] / "papers172_176_sequence/scouting/combinatorial_crossdomain/focused_nonextractive/breadth2.py"
    spec = importlib.util.spec_from_file_location("old_matching_scout", old_path)
    old = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(old)
    collision = []
    for m in range(1, 7):
        count, unequal, witness = 0, 0, None
        for state in matchings(tuple(range(2*m))):
            a, b = length_half_pair(state), old.length_endpoint_weave(state)
            count += 1
            if a != b:
                unequal += 1
                if witness is None:
                    witness = {"source": state, "current": a, "old_LEW": b}
        if m % 2 == 0:
            assert unequal == 0
        collision.append({"edges": m, "states": count, "different": unequal, "witness": witness})
    print(json.dumps({"scope": "exact finite checks of stated formulas; no research acceptance status",
                      "run_inverse_checks": inverse_checks,
                      "identity_fibres_n1_to_n7": identity_fibres,
                      "tableau_fibre_checks": tableau_checks,
                      "traversal_inverse_checks": traversal_checks,
                      "old_source_root_relative": str(old_path.relative_to(Path.cwd())),
                      "old_source_sha256": hashlib.sha256(old_path.read_bytes()).hexdigest(),
                      "matching_collision": collision}, indent=2))


if __name__ == "__main__":
    main()
