#!/usr/bin/env python3
"""Exact audit for repeated Morris--Pratt prefix-function dynamics.

The carrier E_n consists of inversion sequences e=(e_0,...,e_{n-1}) with
0 <= e_i <= i.  The update regards e as an integer word and returns its
ordinary border/prefix-function array.  All calculations are exact and use
only the Python standard library.
"""

from collections import Counter
from itertools import product
from math import factorial


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def inversion_sequences(n):
    return product(*(range(i + 1) for i in range(n)))


def prefix_function(word):
    answer = [0] * len(word)
    for i in range(1, len(word)):
        border = answer[i - 1]
        while border and word[i] != word[border]:
            border = answer[border - 1]
        if word[i] == word[border]:
            border += 1
        answer[i] = border
    return tuple(answer)


def prefix_function_naive(word):
    answer = []
    for end in range(len(word)):
        value = 0
        for size in range(1, end + 1):
            if word[:size] == word[end - size + 1 : end + 1]:
                value = size
        answer.append(value)
    return tuple(answer)


def a_template(n, r):
    """A_r=(0,1,...,r,0,...,0), 1 <= r < n."""
    return tuple(i if i <= r else 0 for i in range(n))


def b_template(n, k):
    """B_k=(0,...,0,1,...,1), 2 <= k <= n."""
    return tuple(0 if i < k else 1 for i in range(n))


def canonical_info(array):
    """Return the canonical A/B template and first disagreement."""
    n = len(array)
    if n == 1:
        return ("S", 0), (0,), 1
    if array[1] == 1:
        r = 1
        while r + 1 < n and array[r + 1] == r + 1:
            r += 1
        template = a_template(n, r)
        kind = ("A", r)
    else:
        k = next((i for i in range(1, n) if array[i] > 0), n)
        template = b_template(n, k)
        kind = ("B", k)
    agreement = next(
        (i for i, (left, right) in enumerate(zip(array, template)) if left != right),
        n,
    )
    return kind, template, agreement


def graph_data(states, next_map):
    memo = {}
    for start in states:
        if start in memo:
            continue
        path = []
        positions = {}
        current = start
        while current not in memo and current not in positions:
            positions[current] = len(path)
            path.append(current)
            current = next_map[current]
        if current in positions:
            split = positions[current]
            cycle = path[split:]
            period = len(cycle)
            for state in cycle:
                memo[state] = (0, period)
            prefix = path[:split]
        else:
            prefix = path
        for state in reversed(prefix):
            successor_tail, successor_period = memo[next_map[state]]
            memo[state] = (successor_tail + 1, successor_period)
    return memo


def expected_recurrent(n):
    if n == 1:
        return {(0,)}
    return {
        template
        for r in range(1, n)
        for template in (a_template(n, r), b_template(n, r + 1))
    }


def audit_length(n):
    states = list(inversion_sequences(n))
    next_map = {}
    fibres = Counter()
    for state in states:
        image = prefix_function(state)
        next_map[state] = image
        fibres[image] += 1
        check(len(image) == n, "prefix function changed length")
        check(all(0 <= image[i] <= i for i in range(n)), "carrier closure failed")
        if n <= 8:
            check(image == prefix_function_naive(state), "fast/naive prefix mismatch")

    image = set(fibres)
    data = graph_data(states, next_map)
    recurrent = expected_recurrent(n)
    check({state for state in states if data[state][0] == 0} == recurrent,
          "recurrent atlas differs from the A/B templates")

    if n == 1:
        check(next_map[(0,)] == (0,), "length-one state is not fixed")
    else:
        for r in range(1, n):
            left = a_template(n, r)
            right = b_template(n, r + 1)
            check(next_map[left] == right, "A_r did not map to B_(r+1)")
            check(next_map[right] == left, "B_(r+1) did not map to A_r")
        check(all(data[state][1] == 2 for state in states),
              "a nontrivial period other than two appeared")

    # The local mismatch automaton is checked on every realizable prefix table.
    for table in image:
        if n == 1:
            continue
        kind, _, agreement = canonical_info(table)
        successor = prefix_function(table)
        next_kind, _, next_agreement = canonical_info(successor)
        expected_kind = (
            ("B", kind[1] + 1) if kind[0] == "A" else ("A", kind[1] - 1)
        )
        check(next_kind == expected_kind, "canonical A/B partner changed")
        if agreement == n:
            check(next_agreement == n, "recurrent template left the atlas")
            continue
        check(n >= 4 and agreement >= 3, "nonrecurrent valid table has a short core")
        actual = table[agreement]
        next_actual = successor[next_agreement] if next_agreement < n else None
        if kind[0] == "A":
            check(actual == 1, "valid A-type mismatch was not state A1")
            check(next_agreement == agreement and next_actual == 2,
                  "A1 did not transition to B2")
        elif actual == 0:
            check(next_agreement == agreement and next_actual == 1,
                  "B0 did not transition to A1")
        else:
            check(actual == 2, "valid B-type mismatch was neither B0 nor B2")
            check(next_agreement > agreement, "B2 did not extend the canonical prefix")
            if next_agreement < n:
                check(next_kind[0] == "A" and successor[next_agreement] == 1,
                      "post-extension mismatch was not A1")

    observed_max_tail = max(tail for tail, _ in data.values())
    expected_max_tail = 0 if n <= 2 else (1 if n == 3 else 2 * n - 4)
    check(observed_max_tail == expected_max_tail, "sharp global tail failed")

    image_max_tail = max(data[state][0] for state in image)
    expected_image_tail = 0 if n <= 3 else 2 * n - 5
    check(image_max_tail == expected_image_tail, "valid-table tail bound failed")

    maximum_fibre = max(fibres.values())
    expected_maximum = factorial(n - 1)
    check(maximum_fibre == expected_maximum, "maximum one-step fibre failed")
    maximizers = {target for target, size in fibres.items() if size == maximum_fibre}
    expected_maximizers = {(0,)} if n == 1 else {
        b_template(n, n),
        a_template(n, 1),
    }
    check(maximizers == expected_maximizers, "maximum-fibre targets changed")

    if n >= 4:
        witness = (0, 1, 0, 2) + (1,) * (n - 4)
        first_image = (0, 0, 1) + (0,) * (n - 3)
        check(prefix_function(witness) == first_image, "sharp witness first image failed")
        check(data[witness][0] == 2 * n - 4, "sharp witness lost its depth")
        check(data[first_image][0] == 2 * n - 5,
              "valid sharp witness lost its depth")

        # Exact displayed orbit of the valid witness.
        current = first_image
        for j in range(1, n - 2):
            current = prefix_function(prefix_function(current))
            expected_even = (
                (0, 0) + (1,) * j + (2,) + (0,) * (n - j - 3)
            )
            check(current == expected_even, "sharp even-iterate formula failed")
        check(prefix_function(current) == a_template(n, 1),
              "sharp orbit did not enter A_1 at time 2n-5")

    return {
        "states": len(states),
        "image": len(image),
        "recurrent": len(recurrent),
        "cycles": 1 if n == 1 else n - 1,
        "max_tail": observed_max_tail,
        "image_max_tail": image_max_tail,
        "max_fibre": maximum_fibre,
    }


def main():
    total_states = 0
    profiles = []
    for n in range(1, 10):
        result = audit_length(n)
        total_states += result["states"]
        profiles.append(
            "n{n}:states{states}:image{image}:rec{recurrent}:cycles{cycles}:"
            "tail{max_tail}:validtail{image_max_tail}:maxfib{max_fibre}".format(
                n=n, **result
            )
        )

    check(total_states == sum(factorial(n) for n in range(1, 10)),
          "global state census failed")
    print("prefix-function inversion-sequence dynamics: PASS")
    print("range=n=1..9")
    print(f"states={total_states}")
    print(f"assertions={ASSERTIONS}")
    print("profiles=" + ";".join(profiles))
    print("theorem=recurrent A_r/B_(r+1) two-cycles; sharp tail 2n-4 for n>=4")
    print("fibre=max (n-1)! attained only by 0^n and 010^(n-2) for n>=2")
    print("scope=finite enumeration is falsification evidence, not proof")
    print("novelty=bounded owner non-hit is not novelty or priority")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
