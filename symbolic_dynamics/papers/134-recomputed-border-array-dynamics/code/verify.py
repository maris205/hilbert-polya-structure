#!/usr/bin/env python3
"""Paper-local exact audit for whole-array recomputed border dynamics.

The carrier is E_n = {e: 0 <= e_i <= i}.  One update regards the entire
integer array e as a word and recomputes its complete ordinary border array.
This file is self-contained and does not import the scouting verifier.
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


def carrier(n):
    return product(*(range(i + 1) for i in range(n)))


def border_array(word):
    """Linear Morris--Pratt border-array computation."""
    out = [0] * len(word)
    for i in range(1, len(word)):
        k = out[i - 1]
        while k and word[i] != word[k]:
            k = out[k - 1]
        if word[i] == word[k]:
            k += 1
        out[i] = k
    return tuple(out)


def literal_border_array(word):
    """Definition-level longest-prefix/longest-suffix comparison."""
    out = []
    for end in range(len(word)):
        prefix = word[: end + 1]
        best = 0
        for size in range(1, end + 1):
            if prefix[:size] == prefix[-size:]:
                best = size
        out.append(best)
    return tuple(out)


def standardize(word):
    names = {}
    out = []
    for letter in word:
        if letter not in names:
            names[letter] = len(names)
        out.append(names[letter])
    return tuple(out)


def a_template(n, r):
    return tuple(i if i <= r else 0 for i in range(n))


def b_template(n, k):
    return tuple(0 if i < k else 1 for i in range(n))


def recurrent_templates(n):
    if n == 1:
        return {(0,)}
    return {
        table
        for r in range(1, n)
        for table in (a_template(n, r), b_template(n, r + 1))
    }


def canonical_info(table):
    """Return (kind, parameter), template, and first mismatch index."""
    n = len(table)
    if n == 1:
        return ("S", 0), (0,), n
    if table[1] == 1:
        r = 1
        while r + 1 < n and table[r + 1] == r + 1:
            r += 1
        kind = ("A", r)
        template = a_template(n, r)
    else:
        k = next((i for i in range(1, n) if table[i] != 0), n)
        kind = ("B", k)
        template = b_template(n, k)
    mismatch = next(
        (i for i, (actual, expected) in enumerate(zip(table, template))
         if actual != expected),
        n,
    )
    return kind, template, mismatch


def graph_profile(states, successor):
    data = {}
    for start in states:
        if start in data:
            continue
        path = []
        position = {}
        current = start
        while current not in data and current not in position:
            position[current] = len(path)
            path.append(current)
            current = successor[current]
        if current in position:
            split = position[current]
            cycle = path[split:]
            for state in cycle:
                data[state] = (0, len(cycle))
            prefix = path[:split]
        else:
            prefix = path
        for state in reversed(prefix):
            tail, period = data[successor[state]]
            data[state] = (tail + 1, period)
    return data


def orbit_data(start):
    seen = {}
    current = start
    while current not in seen:
        seen[current] = len(seen)
        current = border_array(current)
    return seen[current], len(seen) - seen[current]


def sharp_valid(n):
    return (0, 0, 1) + (0,) * (n - 3)


def sharp_source(n):
    return (0, 1, 0, 2) + (1,) * (n - 4)


def x_state(n, j):
    return (0, 0) + (1,) * j + (2,) + (0,) * (n - j - 3)


def y_state(n, j):
    return (0, 1) + (0,) * (j + 1) + (1,) + (2,) * (n - j - 4)


def audit_standardization():
    cases = 0
    for n in range(1, 8):
        for word in product(range(3), repeat=n):
            normalized = standardize(word)
            check(all(0 <= normalized[i] <= i for i in range(n)),
                  f"standardization left E_{n}")
            check(border_array(word) == border_array(normalized),
                  f"standardization changed borders at n={n}")
            cases += 1
    return cases


def audit_length(n):
    states = list(carrier(n))
    successor = {}
    fibres = Counter()

    for state in states:
        image = border_array(state)
        successor[state] = image
        fibres[image] += 1
        check(len(image) == n, f"length changed at n={n}")
        check(all(0 <= image[i] <= i for i in range(n)),
              f"carrier closure failed at n={n}")
        if n <= 8:
            check(image == literal_border_array(state),
                  f"linear/literal disagreement at n={n}, state={state}")

    image = set(fibres)
    graph = graph_profile(states, successor)
    recurrent = recurrent_templates(n)

    check({state for state in states if graph[state][0] == 0} == recurrent,
          f"recurrent atlas failed at n={n}")

    if n == 1:
        check(successor[(0,)] == (0,), "length-one state is not fixed")
    else:
        for r in range(1, n):
            left = a_template(n, r)
            right = b_template(n, r + 1)
            check(successor[left] == right,
                  f"A_{r} did not map to B_{r+1} at n={n}")
            check(successor[right] == left,
                  f"B_{r+1} did not map to A_{r} at n={n}")
        for state in states:
            check(graph[state][1] == 2,
                  f"period other than two at n={n}, state={state}")

    # Indexed mismatch lemma on every valid table in the image.
    for table in image:
        if n == 1:
            continue
        kind, _, mismatch = canonical_info(table)
        target = border_array(table)
        next_kind, _, next_mismatch = canonical_info(target)
        partner = (("B", kind[1] + 1) if kind[0] == "A"
                   else ("A", kind[1] - 1))
        check(next_kind == partner,
              f"canonical partner changed at n={n}, table={table}")
        if mismatch == n:
            check(next_mismatch == n,
                  f"template left recurrent atlas at n={n}")
            continue
        check(n >= 4 and mismatch >= 3,
              f"short nonrecurrent canonical prefix at n={n}")
        actual = table[mismatch]
        if kind[0] == "A":
            check(actual == 1, f"A mismatch not A1 at n={n}")
            check(next_mismatch == mismatch and target[mismatch] == 2,
                  f"A1 did not become B2 at n={n}")
        elif actual == 0:
            check(next_mismatch == mismatch and target[mismatch] == 1,
                  f"B0 did not become A1 at n={n}")
        else:
            check(actual == 2, f"B mismatch outside B0/B2 at n={n}")
            check(next_mismatch > mismatch,
                  f"B2 did not extend at n={n}")
            if next_mismatch < n:
                check(next_kind[0] == "A" and target[next_mismatch] == 1,
                      f"post-extension mismatch not A1 at n={n}")

    maximum_tail = max(tail for tail, _ in graph.values())
    expected_tail = 0 if n <= 2 else (1 if n == 3 else 2 * n - 4)
    check(maximum_tail == expected_tail,
          f"sharp whole-carrier depth failed at n={n}")

    maximum_valid_tail = max(graph[table][0] for table in image)
    expected_valid_tail = 0 if n <= 3 else 2 * n - 5
    check(maximum_valid_tail == expected_valid_tail,
          f"sharp valid depth failed at n={n}")

    maximum_fibre = factorial(n - 1)
    expected_maximizers = ({(0,)} if n == 1 else
                           {(0,) * n, a_template(n, 1)})
    for target in states:
        size = fibres[target]
        check(size <= maximum_fibre,
              f"all-target fibre bound failed at n={n}, target={target}")
        if size == maximum_fibre:
            check(target in expected_maximizers,
                  f"unexpected factorial maximizer at n={n}, target={target}")
    check({target for target in states if fibres[target] == maximum_fibre}
          == expected_maximizers,
          f"factorial maximizer set failed at n={n}")

    if n >= 4:
        source = sharp_source(n)
        valid = sharp_valid(n)
        check(border_array(source) == valid,
              f"sharp source first image failed at n={n}")
        check(graph[source] == (2 * n - 4, 2),
              f"sharp source graph data failed at n={n}")
        check(graph[valid] == (2 * n - 5, 2),
              f"sharp valid graph data failed at n={n}")
        check(border_array(valid) == y_state(n, 0),
              f"sharp odd formula j=0 failed at n={n}")
        for j in range(1, n - 2):
            check(border_array(y_state(n, j - 1)) == x_state(n, j),
                  f"Y-to-X formula failed at n={n}, j={j}")
            if j < n - 3:
                check(border_array(x_state(n, j)) == y_state(n, j),
                      f"X-to-Y formula failed at n={n}, j={j}")
            else:
                check(border_array(x_state(n, j)) == a_template(n, 1),
                      f"sharp trajectory endpoint failed at n={n}")

    return {
        "states": len(states),
        "image": len(image),
        "recurrent": len(recurrent),
        "cycles": 1 if n == 1 else n - 1,
        "tail": maximum_tail,
        "valid_tail": maximum_valid_tail,
        "max_fibre": max(fibres.values()),
    }


def audit_large_witnesses():
    cases = 0
    for n in range(4, 33):
        valid = sharp_valid(n)
        source = sharp_source(n)
        check(border_array(source) == valid,
              f"large witness first image failed at n={n}")
        check(orbit_data(source) == (2 * n - 4, 2),
              f"large source depth failed at n={n}")
        check(orbit_data(valid) == (2 * n - 5, 2),
              f"large valid depth failed at n={n}")
        for j in range(0, n - 3):
            check(border_array(y_state(n, j)) == x_state(n, j + 1),
                  f"large Y-to-X formula failed at n={n}, j={j}")
        for j in range(1, n - 3):
            check(border_array(x_state(n, j)) == y_state(n, j),
                  f"large X-to-Y formula failed at n={n}, j={j}")
        check(border_array(x_state(n, n - 3)) == a_template(n, 1),
              f"large trajectory endpoint failed at n={n}")
        cases += 1
    return cases


def main():
    standardization_cases = audit_standardization()
    profiles = []
    total_states = 0
    total_targets = 0
    for n in range(1, 10):
        result = audit_length(n)
        total_states += result["states"]
        total_targets += result["states"]
        profiles.append(
            "n{n}:states{states}:image{image}:rec{recurrent}:cycles{cycles}:"
            "tail{tail}:validtail{valid_tail}:maxfib{max_fibre}".format(
                n=n, **result
            )
        )
    check(total_states == sum(factorial(n) for n in range(1, 10)),
          "global carrier census failed")
    witness_sizes = audit_large_witnesses()

    print("WHOLE-ARRAY RECOMPUTED BORDER DYNAMICS: PASS")
    print("exhaustive_range=n=1..9")
    print(f"states={total_states}")
    print(f"target_cells={total_targets}")
    print(f"standardization_cases={standardization_cases}")
    print(f"large_witness_sizes={witness_sizes}")
    print(f"assertions={ASSERTIONS}")
    print("profiles=" + ";".join(profiles))
    print("recurrent=n-1 exact two-cycles for n>=2; one fixed point for n=1")
    print("max_depth=0,0,1,2n-4 for n=1,2,3,n>=4")
    print("max_fibre=(n-1)! only at 0^n and 010^(n-2) for n>=2")
    print("scope=finite exact falsification; all-n claims require proof")
    print("external_status=HOLD_EXTERNAL")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
