#!/usr/bin/env python3
"""Paper-local exact falsifier for P181.

The program rebuilds the deterministic map and its complete inverse table
directly on symmetric groups.  It imports no scouting or prior-paper code.
Finite enumeration is counterexample pressure, not a proof or owner search.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import permutations
from math import factorial


ASSERTIONS = 0


def check(condition: bool, label: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def identity(n: int) -> tuple[int, ...]:
    return tuple(range(1, n + 1))


def reverse_prefix(word: tuple[int, ...], length: int) -> tuple[int, ...]:
    check(1 <= length <= len(word), f"legal reversal length={length}")
    return word[:length][::-1] + word[length:]


def first_descent(word: tuple[int, ...]) -> int | None:
    """Return the first descent position in one-based indexing."""
    for position in range(1, len(word)):
        if word[position - 1] > word[position]:
            return position
    return None


def first_descent_reversal(word: tuple[int, ...]) -> tuple[int, ...]:
    descent = first_descent(word)
    if descent is None:
        return word
    return reverse_prefix(word, descent + 1)


def in_image(word: tuple[int, ...]) -> bool:
    return len(word) >= 2 and word[0] < word[1]


def peak_at_two(word: tuple[int, ...]) -> bool:
    return len(word) >= 3 and word[0] < word[1] > word[2]


def decreasing_run_from_two(word: tuple[int, ...]) -> int:
    """Length of the maximal strict decreasing run starting at position 2."""
    check(len(word) >= 2, "run requires n>=2")
    run = 1
    while run + 1 < len(word) and word[run] > word[run + 1]:
        run += 1
    return run


def predicted_predecessors(target: tuple[int, ...]) -> set[tuple[int, ...]]:
    if not in_image(target):
        return set()
    run = decreasing_run_from_two(target)
    predecessors = {
        reverse_prefix(target, length) for length in range(2, run + 2)
    }
    if target == identity(len(target)):
        predecessors.add(target)
    return predecessors


def orbit_coordinates(
    start: tuple[int, ...],
    transition: dict[tuple[int, ...], tuple[int, ...]],
) -> tuple[int, int]:
    seen: dict[tuple[int, ...], int] = {}
    state = start
    while state not in seen:
        seen[state] = len(seen)
        state = transition[state]
    return seen[state], len(seen) - seen[state]


def predicted_maximizers(n: int) -> set[tuple[int, ...]]:
    if n == 2:
        return {identity(2)}
    targets = {
        word for word in permutations(range(1, n + 1))
        if word[1] == n
        and all(word[j] > word[j + 1] for j in range(1, n - 1))
    }
    if n == 3:
        targets.add(identity(3))
    return targets


def audit_group(n: int) -> tuple[int, int, Counter, int, int]:
    states = tuple(permutations(range(1, n + 1)))
    transition = {word: first_descent_reversal(word) for word in states}
    incoming: dict[tuple[int, ...], set[tuple[int, ...]]] = defaultdict(set)
    for source, target in transition.items():
        incoming[target].add(source)
        descent = first_descent(source)
        if descent is None:
            check(source == identity(n) and target == source,
                  f"only increasing state fixed n={n} source={source}")
        else:
            check(target[0] < target[1],
                  f"literal output has ascent n={n} source={source}")
            check(target == reverse_prefix(source, descent + 1),
                  f"literal chosen prefix n={n} source={source}")

    actual_image = set(incoming)
    expected_image = {word for word in states if in_image(word)}
    check(actual_image == expected_image, f"exact image n={n}")
    check(len(actual_image) == factorial(n) // 2, f"half image n={n}")

    for target in states:
        expected = predicted_predecessors(target)
        actual = incoming.get(target, set())
        check(actual == expected, f"complete fibre n={n} target={target}")
        expected_size = (
            decreasing_run_from_two(target) + int(target == identity(n))
            if in_image(target) else 0
        )
        check(len(actual) == expected_size,
              f"fibre size n={n} target={target}")
        if in_image(target):
            run = decreasing_run_from_two(target)
            check(1 <= run <= n - 1, f"run boundary n={n} target={target}")
            for length in range(2, run + 2):
                source = reverse_prefix(target, length)
                check(first_descent(source) == length - 1,
                      f"inverse first descent n={n} target={target} k={length}")
                check(transition[source] == target,
                      f"inverse returns target n={n} target={target} k={length}")

    tails = Counter()
    recurrent = set()
    periods = {}
    for word in states:
        tail, period = orbit_coordinates(word, transition)
        tails[tail] += 1
        periods[word] = period
        if tail == 0:
            recurrent.add(word)
        check(tail <= (1 if n == 2 else 2), f"depth bound n={n} word={word}")
        check(period in (1, 2), f"period set n={n} word={word}")

    if n == 2:
        expected_recurrent = {identity(2)}
        expected_tails = Counter({0: 1, 1: 1})
    else:
        expected_recurrent = {identity(n)} | {
            word for word in states if peak_at_two(word)
        }
        expected_tails = Counter({
            0: factorial(n) // 3 + 1,
            1: factorial(n) // 2,
            2: factorial(n) // 6 - 1,
        })
        expected_tails = +expected_tails

    check(recurrent == expected_recurrent, f"recurrent core n={n}")
    check(tails == expected_tails, f"tail census n={n}")
    check(periods[identity(n)] == 1, f"identity period n={n}")

    cycle_pairs = set()
    for word in recurrent - {identity(n)}:
        partner = transition[word]
        check(peak_at_two(word), f"recurrent peak n={n} word={word}")
        check(partner != word and transition[partner] == word,
              f"peak two-cycle n={n} word={word}")
        check(peak_at_two(partner), f"partner peak n={n} word={word}")
        cycle_pairs.add(tuple(sorted((word, partner))))
    expected_cycles = 0 if n == 2 else factorial(n) // 6
    check(len(cycle_pairs) == expected_cycles, f"two-cycle count n={n}")

    # Every image state outside the recurrent core has its unique predecessor
    # outside the image, which gives the sharp depth-two bijection.
    if n >= 3:
        image_noncore = actual_image - recurrent
        depth_two = {word for word in states if orbit_coordinates(word, transition)[0] == 2}
        paired = {reverse_prefix(target, 2): target for target in image_noncore}
        check(set(paired) == depth_two, f"depth-two sources n={n}")
        check(set(paired.values()) == image_noncore,
              f"depth-two target bijection n={n}")
        for source, target in paired.items():
            check(not in_image(source) and transition[source] == target,
                  f"depth-two literal pair n={n} source={source}")

    maximum = max(len(incoming.get(word, set())) for word in states)
    maximizers = {
        word for word in states if len(incoming.get(word, set())) == maximum
    }
    expected_maximum = 2 if n == 2 else n - 1
    expected_maximizers = predicted_maximizers(n)
    check(maximum == expected_maximum, f"maximum fibre n={n}")
    check(maximizers == expected_maximizers, f"all maximizers n={n}")
    if n >= 4:
        check(len(maximizers) == n - 1, f"maximizer count n={n}")

    return len(states), len(actual_image), tails, maximum, len(maximizers)


def audit_n1_atlas() -> None:
    word = identity(1)
    transition = {word: first_descent_reversal(word)}
    incoming = {word: {word}}
    check(word == (1,), "n=1 unique permutation")
    check(first_descent(word) is None, "n=1 has no descent")
    check(transition[word] == word, "n=1 fixed arrow")
    check(set(transition.values()) == {word}, "n=1 image")
    check({state for state in transition if transition[state] == state} == {word},
          "n=1 recurrent core")
    check(orbit_coordinates(word, transition) == (0, 1),
          "n=1 depth and period")
    check(incoming[word] == {word}, "n=1 predecessor fibre")
    check(len(incoming[word]) == 1, "n=1 maximum fibre")


def main() -> None:
    print("P181 PAPER-LOCAL EXACT CONTROL")
    print("lifecycle=HOLD_EXTERNAL owner=OWNER_AMBER")
    for n in range(2, 10):
        states, image, tails, maximum, maximizers = audit_group(n)
        tail_text = ",".join(f"{depth}:{count}" for depth, count in sorted(tails.items()))
        print(
            f"n={n} states={states} image={image} tails={tail_text} "
            f"max_fibre={maximum} maximizers={maximizers} PASS"
        )
    audit_n1_atlas()
    print("theorem=exact_half_image PASS")
    print("theorem=identity_plus_peak_two_cycle_core PASS")
    print("theorem=depth_zero_one_two_census PASS")
    print("theorem=decreasing_run_target_fibres PASS")
    print("theorem=sharp_maximum_and_all_maximizers PASS")
    print("boundaries=n1_n2_n3 PASS")
    print(f"exact_assertions={ASSERTIONS}")
    print("status=PASS")
    print("external_status=HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
