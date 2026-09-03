#!/usr/bin/env python3
"""Independent string-state hostile control for P181."""

from collections import Counter, defaultdict
from itertools import permutations
from math import factorial


assertions = 0


def test(value):
    global assertions
    assertions += 1
    if not value:
        raise AssertionError(f"review assertion {assertions} failed")


def fdr(word):
    for i in range(len(word) - 1):
        if word[i] > word[i + 1]:
            return word[:i + 2][::-1] + word[i + 2:]
    return word


def follower_to_front(word):
    for i in range(len(word) - 1):
        if word[i] > word[i + 1]:
            return word[i + 1] + word[:i + 1] + word[i + 2:]
    return word


def flip_prefix(word, k):
    return word[:k][::-1] + word[k:]


def first_bad(word):
    for i in range(len(word) - 1):
        if word[i] > word[i + 1]:
            return i
    return None


def orbit_type(word, arrows):
    seen = {}
    state = word
    while state not in seen:
        seen[state] = len(seen)
        state = arrows[state]
    return seen[state], len(seen) - seen[state]


def review_n(n):
    alphabet = "123456789"[:n]
    identity = alphabet
    states = tuple("".join(p) for p in permutations(alphabet))
    arrows = {state: fdr(state) for state in states}
    incoming = defaultdict(set)
    for source, target in arrows.items():
        incoming[target].add(source)
        descent = first_bad(source)
        if descent is None:
            test(source == identity == target)
        else:
            test(target == flip_prefix(source, descent + 2))
            test(target[0] < target[1])

    expected_image = {state for state in states if state[0] < state[1]}
    test(set(incoming) == expected_image)
    test(len(expected_image) == factorial(n) // 2)

    for target in states:
        if target not in expected_image:
            test(not incoming[target])
            continue
        run_positions = 1
        while run_positions + 1 < n and target[run_positions] > target[run_positions + 1]:
            run_positions += 1
        expected = {flip_prefix(target, k) for k in range(2, run_positions + 2)}
        if target == identity:
            expected.add(identity)
        test(incoming[target] == expected)
        test(len(incoming[target]) == run_positions + int(target == identity))
        for source in expected - {identity}:
            cut = first_bad(source)
            test(cut is not None)
            test(flip_prefix(source, cut + 2) == target)

    peaks = {state for state in states if state[0] < state[1] > state[2]}
    recurrent = {identity} | peaks
    test(len(peaks) == factorial(n) // 3)
    cycle_edges = set()
    tails = Counter()
    for state in states:
        tail, period = orbit_type(state, arrows)
        tails[tail] += 1
        test(tail <= 2)
        if state in recurrent:
            test(tail == 0)
            if state == identity:
                test(period == 1)
            else:
                test(period == 2)
                test(arrows[arrows[state]] == state)
                cycle_edges.add(tuple(sorted((state, arrows[state]))))
        else:
            test(tail > 0)
    test(len(cycle_edges) == factorial(n) // 6)
    expected_tails = Counter({0: factorial(n) // 3 + 1,
                              1: factorial(n) // 2,
                              2: factorial(n) // 6 - 1})
    test(tails == +expected_tails)

    max_fibre = max(len(incoming[state]) for state in states)
    maximizers = {state for state in states if len(incoming[state]) == max_fibre}
    long_tail = {state for state in states
                 if state[1] == alphabet[-1]
                 and all(state[i] > state[i + 1] for i in range(1, n - 1))}
    if n == 3:
        long_tail.add(identity)
    test(max_fibre == n - 1)
    test(maximizers == long_tail)
    test(len(maximizers) == (3 if n == 3 else n - 1))
    return len(states), len(expected_image), tuple(sorted(tails.items())), max_fibre, len(maximizers)


def main():
    one_arrows = {"1": fdr("1")}
    test(one_arrows["1"] == "1")
    test(first_bad("1") is None)
    test(set(one_arrows.values()) == {"1"})
    test(orbit_type("1", one_arrows) == (0, 1))
    test({source for source, target in one_arrows.items() if target == "1"} == {"1"})
    test(max(Counter(one_arrows.values()).values()) == 1)
    test(fdr("12") == "12" and fdr("21") == "12")
    test(fdr("1324") == "2314")
    test(follower_to_front("1324") == "2134")
    test(fdr("1324") != follower_to_front("1324"))
    rows = [(n, review_n(n)) for n in range(3, 9)]
    print("P181_HOSTILE_REVIEW_B_ROOT")
    print("n=2 arrows=12>12,21>12 max=2 maximizers=1 PASS")
    for n, (states, image, tails, maximum, maximizers) in rows:
        print(f"n={n} states={states} image={image} tails={tails} max={maximum} maximizers={maximizers}")
    print(f"ASSERTIONS={assertions}")
    print("REPRESENTATION=string-permutations/direct-incoming-sets/explicit-negative-control")
    print("RESULT=PASS")
    print("RELEASE_SENTINEL=REVIEW_ONLY/HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
