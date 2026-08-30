#!/usr/bin/env python3
"""Independent exact verifier for the C6 cross-colon proof dossier.

The program deliberately does not import the scouting pilot.  It compares
three descriptions of the map (literal monomial arithmetic, staircase
coordinates, and diagonal path automata), exhausts every ideal in all boxes
1 <= a,b <= 9, and separately exhausts the path lemmas through length 14.
"""

from collections import Counter
from itertools import combinations_with_replacement, product


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def orbit_data(start, step):
    seen = {}
    state = start
    while state not in seen:
        seen[state] = len(seen)
        state = step(state)
    return seen[state], len(seen) - seen[state]


def staircase_states(a, b):
    """All b >= h_0 >= ... >= h_(a-1) >= 0."""
    for increasing in combinations_with_replacement(range(b + 1), a):
        yield tuple(reversed(increasing))


def staircase_mask(h, a, b):
    answer = 0
    for i in range(a):
        for j in range(h[i], b):
            answer |= 1 << (i * b + j)
    return answer


def mask_staircase(mask, a, b):
    return tuple(
        next((j for j in range(b) if mask & (1 << (i * b + j))), b)
        for i in range(a)
    )


def literal_multiply(mask, a, b, di, dj):
    answer = 0
    for i in range(a):
        for j in range(b):
            if mask & (1 << (i * b + j)):
                if i + di < a and j + dj < b:
                    answer |= 1 << ((i + di) * b + j + dj)
    return answer


def literal_colon(mask, a, b, di, dj):
    answer = 0
    for i in range(a):
        for j in range(b):
            ni, nj = i + di, j + dj
            if ni >= a or nj >= b or mask & (1 << (ni * b + nj)):
                answer |= 1 << (i * b + j)
    return answer


def literal_step(mask, a, b):
    left = literal_multiply(literal_colon(mask, a, b, 0, 1), a, b, 1, 0)
    right = literal_multiply(literal_colon(mask, a, b, 1, 0), a, b, 0, 1)
    return left | right


def staircase_step(h, b):
    a = len(h)
    if a == 1:
        return (1,)
    answer = [min(b, h[1] + 1)]
    for i in range(1, a - 1):
        answer.append(min(max(0, h[i - 1] - 1), h[i + 1] + 1))
    answer.append(min(max(0, h[a - 2] - 1), 1))
    return tuple(answer)


def diagonal_step(mask, a, b):
    answer = 0
    for d in range(a + b - 1):
        lower = max(0, d - b + 1)
        upper = min(a - 1, d)
        left_source = int(d >= b)
        right_source = int(d >= a)
        word = [int(bool(mask & (1 << (i * b + d - i)))) for i in range(lower, upper + 1)]
        for offset, i in enumerate(range(lower, upper + 1)):
            left = left_source if offset == 0 else word[offset - 1]
            right = right_source if offset + 1 == len(word) else word[offset + 1]
            if left or right:
                answer |= 1 << (i * b + d - i)
    return answer


def path_step(word, left_source, right_source):
    n = len(word)
    return tuple(
        (left_source if i == 0 else word[i - 1])
        or (right_source if i == n - 1 else word[i + 1])
        for i in range(n)
    )


def predicted_path_recurrent(n, left_source, right_source):
    if left_source or right_source:
        return {(1,) * n}
    if n == 1:
        return {(0,)}
    return {
        tuple(value_by_parity[i % 2] for i in range(n))
        for value_by_parity in product((0, 1), repeat=2)
    }


def check_path_lemma():
    states_checked = 0
    for n in range(1, 15):
        for sources in ((0, 0), (1, 0), (0, 1), (1, 1)):
            left_source, right_source = sources
            recurrent = predicted_path_recurrent(n, *sources)
            maximum = -1
            depth_hist = Counter()
            for word in product((0, 1), repeat=n):
                depth, cycle = orbit_data(
                    word, lambda w, l=left_source, r=right_source: path_step(w, l, r)
                )
                states_checked += 1
                depth_hist[depth] += 1
                maximum = max(maximum, depth)
                check((depth == 0) == (word in recurrent), (n, sources, word, depth))
                check(cycle in (1, 2), (n, sources, word, cycle))
                if sources != (0, 0):
                    check(cycle == 1, (n, sources, word, cycle))
            if sources == (0, 0):
                predicted_maximum = 1 if n == 1 else max(0, n - 2)
            elif sources == (1, 1):
                predicted_maximum = (n + 1) // 2
            else:
                predicted_maximum = n
            check(maximum == predicted_maximum, (n, sources, maximum, depth_hist))
    return states_checked


def degree_cut_mask(a, b, r):
    answer = 0
    for i in range(a):
        for j in range(b):
            if i + j >= r:
                answer |= 1 << (i * b + j)
    return answer


def checker_cut_mask(a, b, r, parity):
    answer = 0
    for i in range(a):
        for j in range(b):
            if i + j > r or (i + j == r and i % 2 == parity):
                answer |= 1 << (i * b + j)
    return answer


def check_rectangles():
    boxes = 0
    ideals_checked = 0
    global_depth_hist = Counter()
    for a in range(1, 10):
        for b in range(1, 10):
            boxes += 1
            m = min(a, b)
            states = tuple(staircase_states(a, b))
            masks = tuple(staircase_mask(h, a, b) for h in states)
            state_set = set(masks)
            transitions = {}

            for h, mask in zip(states, masks):
                ideals_checked += 1
                literal = literal_step(mask, a, b)
                by_staircase = staircase_mask(staircase_step(h, b), a, b)
                by_diagonals = diagonal_step(mask, a, b)
                check(literal == by_staircase, (a, b, h, "staircase"))
                check(literal == by_diagonals, (a, b, h, "diagonal"))
                check(literal in state_set, (a, b, h, "closure"))
                check(mask_staircase(literal, a, b) == staircase_step(h, b), (a, b, h))
                transitions[mask] = literal

            fixed_family = {degree_cut_mask(a, b, r) for r in range(1, m + 1)}
            checker_family = {
                checker_cut_mask(a, b, r, parity)
                for r in range(1, m)
                for parity in (0, 1)
            }
            predicted_recurrent = fixed_family | checker_family
            check(len(fixed_family) == m, (a, b, "fixed family"))
            check(len(checker_family) == 2 * (m - 1), (a, b, "checker family"))

            maximum = -1
            fixed = set()
            recurrent = set()
            cycle_states = set()
            for mask in masks:
                depth, cycle = orbit_data(mask, transitions.__getitem__)
                global_depth_hist[depth] += 1
                maximum = max(maximum, depth)
                check(cycle in (1, 2), (a, b, mask, depth, cycle))
                check((depth == 0) == (mask in predicted_recurrent), (a, b, mask, depth))
                if depth == 0:
                    recurrent.add(mask)
                if transitions[mask] == mask:
                    fixed.add(mask)
                if transitions[transitions[mask]] == mask and transitions[mask] != mask:
                    cycle_states.add(mask)

            check(fixed == fixed_family, (a, b, "fixed classification"))
            check(recurrent == predicted_recurrent, (a, b, "recurrent classification"))
            check(cycle_states == checker_family, (a, b, "two-cycle classification"))
            for r in range(1, m):
                even = checker_cut_mask(a, b, r, 0)
                odd = checker_cut_mask(a, b, r, 1)
                check(transitions[even] == odd and transitions[odd] == even, (a, b, r))

            predicted_maximum = m if a != b else max(1, m - 2)
            check(maximum == predicted_maximum, (a, b, maximum, predicted_maximum))
            if a != b:
                witness = 0
            elif m == 1:
                witness = 1
            elif m == 2:
                witness = 0
            else:
                witness = staircase_mask((m - 1,) * m, m, m)
            witness_depth, _ = orbit_data(witness, transitions.__getitem__)
            check(witness_depth == predicted_maximum, (a, b, "witness", witness_depth))

    return boxes, ideals_checked, global_depth_hist


def main():
    path_states = check_path_lemma()
    boxes, ideals, depth_hist = check_rectangles()
    print("cross-colon monomial-ideal dynamics independent control: PASS")
    print(f"assertions={ASSERTIONS}")
    print(f"path_words={path_states}; path_lengths=1..14; source_types=00,10,01,11")
    print(f"rectangles={boxes}; parameter_grid=a,b=1..9; ideals={ideals}")
    print("literal_vs_staircase_vs_diagonal=PASS")
    print("fixed_two_cycle_recurrent_classification=PASS")
    print("sharp_depth_and_witnesses=PASS")
    print("global_depth_hist=" + repr(dict(sorted(depth_hist.items()))))


if __name__ == "__main__":
    main()
