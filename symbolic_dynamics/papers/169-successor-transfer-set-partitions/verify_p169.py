#!/usr/bin/env python3
"""Exact controls for successor transfer on canonical set partitions.

The program has no third-party dependencies and imports no scouting or paper
module.  Finite enumeration is used only as a falsification control; the
uniform statements in the manuscript are proved there.  In particular, this
script compares the five-state trace with literal predecessor enumeration for
every target through n=9.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import product
from math import factorial


ASSERTIONS = 0


def check(test: bool) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not test:
        raise AssertionError


def rgs_words(n: int):
    """Yield all restricted-growth words of length n in lexical order."""
    if n == 0:
        yield ()
        return

    def rec(prefix, maximum):
        if len(prefix) == n:
            yield tuple(prefix)
            return
        for letter in range(maximum + 2):
            prefix.append(letter)
            yield from rec(prefix, max(maximum, letter))
            prefix.pop()

    yield from rec([0], 0)


def is_rgs(word) -> bool:
    if not word:
        return True
    if word[0] != 0:
        return False
    maximum = 0
    for letter in word[1:]:
        if letter > maximum + 1:
            return False
        maximum = max(maximum, letter)
    return True


def successor_transfer(word):
    """Increment the final occurrence of every repeated letter, cyclically."""
    if not word:
        return word
    block_count = max(word) + 1
    if block_count == 1:
        return word
    counts = [0] * block_count
    lasts = [0] * block_count
    for position, letter in enumerate(word):
        counts[letter] += 1
        lasts[letter] = position
    answer = list(word)
    for letter in range(block_count):
        if counts[letter] >= 2:
            answer[lasts[letter]] = (letter + 1) % block_count
    return tuple(answer)


def is_recurrent_form(word) -> bool:
    if len(word) <= 1:
        return True
    block_count = max(word) + 1
    if block_count in (1, len(word)):
        return True
    excess = len(word) - block_count
    if excess >= block_count:
        return (len(set(word[:excess])) == block_count
                and len(set(word[-block_count:])) == block_count)
    return (word[:block_count] == tuple(range(block_count))
            and len(set(word[-excess:])) == excess)


def tail_and_period(word):
    seen = {}
    current = word
    while current not in seen:
        seen[current] = len(seen)
        current = successor_transfer(current)
    return seen[current], len(seen) - seen[current]


def stirling_second(n: int, k: int) -> int:
    row = [1] + [0] * k
    for _ in range(n):
        row = [0] + [j * row[j] + row[j - 1] for j in range(1, k + 1)]
    return row[k]


def falling(k: int, m: int) -> int:
    return factorial(k) // factorial(k - m)


# A state records the chosen incoming element relative to its target block.
NONE, SINGLETON, MINIMUM, MAXIMUM, INTERIOR = range(5)
STATE_NAMES = ("none", "singleton", "minimum", "maximum", "interior")
STATE_COUNT = 5


def category_values(block, state):
    if state == NONE:
        return (None,)
    if state == SINGLETON:
        return tuple(block) if len(block) == 1 else ()
    if state == MINIMUM:
        return (block[0],) if len(block) >= 2 else ()
    if state == MAXIMUM:
        return (block[-1],) if len(block) >= 2 else ()
    return tuple(block[1:-1]) if len(block) >= 3 else ()


def retained_extrema(block, incoming_state):
    """Return (size, minimum, maximum) after encoded incoming deletion."""
    if incoming_state == NONE:
        return len(block), block[0], block[-1]
    choices = category_values(block, incoming_state)
    if not choices:
        return None
    size = len(block) - 1
    if size == 0:
        return 0, None, None
    if incoming_state in (SINGLETON, MINIMUM):
        minimum = block[1]
    else:
        minimum = block[0]
    if incoming_state in (SINGLETON, MAXIMUM):
        maximum = block[-2]
    else:
        maximum = block[-1]
    return size, minimum, maximum


def blocks(word):
    block_count = max(word) + 1
    return tuple(
        tuple(position for position, letter in enumerate(word) if letter == i)
        for i in range(block_count)
    )


def local_matrix(target_blocks, index):
    """Return the explicit five-state inverse matrix M_index."""
    block_count = len(target_blocks)
    current = target_blocks[index]
    following = target_blocks[(index + 1) % block_count]
    matrix = [[0] * STATE_COUNT for _ in range(STATE_COUNT)]
    for incoming in range(STATE_COUNT):
        retained = retained_extrema(current, incoming)
        if retained is None:
            continue
        retained_size, retained_minimum, retained_maximum = retained
        for outgoing in range(STATE_COUNT):
            for selected in category_values(following, outgoing):
                # No selected maximum means an inactive singleton source.
                # A selected maximum requires a nonempty retained part and a
                # strict inequality above its retained maximum.
                if outgoing == NONE:
                    if retained_size != 1:
                        continue
                elif retained_size == 0 or selected <= retained_maximum:
                    continue

                # Canonical source order is linear.  In particular, there is
                # deliberately no minimum comparison after the last block.
                if index < block_count - 1:
                    following_retained = retained_extrema(following, outgoing)
                    if (following_retained is None
                            or following_retained[0] == 0
                            or retained_size == 0
                            or retained_minimum >= following_retained[1]):
                        continue
                matrix[incoming][outgoing] += 1
    return matrix


def matrix_multiply(left, right):
    return [
        [sum(left[i][h] * right[h][j] for h in range(STATE_COUNT))
         for j in range(STATE_COUNT)]
        for i in range(STATE_COUNT)
    ]


def fibre_formula(target):
    target_blocks = blocks(target)
    accumulator = [
        [int(i == j) for j in range(STATE_COUNT)]
        for i in range(STATE_COUNT)
    ]
    for index in range(len(target_blocks)):
        accumulator = matrix_multiply(
            accumulator, local_matrix(target_blocks, index)
        )
    return sum(accumulator[i][i] for i in range(STATE_COUNT))


def queue_step(load):
    fired = [int(value > 0) for value in load]
    return tuple(
        load[i] - fired[i] + fired[i - 1] for i in range(len(load))
    )


def cone_height(load, time, index):
    """Evaluate the periodic max-plus height solution H_index(time)."""
    block_count = len(load)

    def height(lifted_index):
        quotient, remainder = divmod(lifted_index, block_count)
        return quotient * sum(load) + sum(load[:remainder + 1])

    return max(
        height(index - offset) - (time - offset)
        for offset in range(time + 1)
    )


def verify_queue_cones():
    cases = 0
    for block_count in range(1, 8):
        for load in product(range(4), repeat=block_count):
            if sum(load) > 10:
                continue
            current = load
            for time in range(block_count):
                for index in range(block_count):
                    recovered = (
                        cone_height(load, time, index)
                        - cone_height(load, time, index - 1)
                    )
                    check(recovered == current[index])
                    cone_mass = sum(
                        load[(index - offset) % block_count]
                        for offset in range(time + 1)
                    )
                    if current[index] == 0:
                        check(cone_mass <= time)
                    if current[index] >= 2:
                        check(cone_mass >= time + 2)
                    cases += 1
                current = queue_step(current)

            mass = sum(load)
            if mass == 0:
                continue
            current = load
            horizon = min(mass, block_count) - 1
            for _ in range(horizon):
                current = queue_step(current)
            if mass <= block_count:
                check(max(current) <= 1)
            if mass >= block_count:
                check(min(current) >= 1)
    return cases


def verify_carriers(maximum_n=10):
    rows = []
    for n in range(1, maximum_n + 1):
        states = tuple(rgs_words(n))
        by_blocks = defaultdict(list)
        recurrent = Counter()
        period_counts = Counter()
        maximum_tail = 0
        witness = None
        for word in states:
            image = successor_transfer(word)
            check(is_rgs(image))
            check(max(image) == max(word))
            tail, period = tail_and_period(word)
            if tail >= maximum_tail:
                maximum_tail = tail
                witness = word
            block_count = max(word) + 1
            by_blocks[block_count].append(tail)
            check((tail == 0) == is_recurrent_form(word))
            if tail == 0:
                recurrent[block_count] += 1
                period_counts[period] += 1
                expected_period = 1 if block_count in (1, n) else block_count
                check(period == expected_period)

        check(maximum_tail == (0 if n == 1 else n - 2))
        for block_count in range(1, n + 1):
            expected_clock = (
                0 if block_count in (1, n)
                else min(n - 2, 2 * block_count - 2)
            )
            check(max(by_blocks[block_count]) == expected_clock)
            if block_count in (1, n):
                expected_recurrent = 1
            else:
                excess = n - block_count
                expected_recurrent = (
                    factorial(block_count)
                    * stirling_second(excess, block_count)
                    if excess >= block_count
                    else falling(block_count, excess)
                )
            check(recurrent[block_count] == expected_recurrent)
        rows.append((n, len(states), maximum_tail,
                     dict(sorted(period_counts.items())), witness))
    return rows


def verify_fibres(maximum_n=9):
    rows = []
    targets_checked = 0
    for n in range(1, maximum_n + 1):
        states = tuple(rgs_words(n))
        literal = Counter(successor_transfer(word) for word in states)
        image_size = 0
        maximum_fibre = 0
        for target in states:
            formula = fibre_formula(target)
            check(formula == literal[target])
            image_size += formula > 0
            maximum_fibre = max(maximum_fibre, formula)
            targets_checked += 1
        rows.append((n, len(states), image_size, maximum_fibre))

    # Same ordered (size, minimum, maximum) data, different labelled fibres.
    target_a = (0, 1, 0, 1, 1, 0)  # 025|134
    target_b = (0, 1, 1, 0, 1, 0)  # 035|124
    expected_a = (
        [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
         [0, 0, 0, 1, 1], [0, 0, 0, 0, 0]],
        [[0, 0, 0, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0],
         [0, 0, 0, 1, 0], [0, 0, 0, 1, 0]],
    )
    expected_b = (
        [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0], [0, 0, 0, 0, 0]],
        [[0, 0, 0, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0],
         [0, 0, 0, 1, 1], [0, 0, 0, 1, 0]],
    )
    check(tuple((len(block), block[0], block[-1]) for block in blocks(target_a))
          == tuple((len(block), block[0], block[-1])
                   for block in blocks(target_b)))
    check(tuple(local_matrix(blocks(target_a), i) for i in range(2))
          == expected_a)
    check(tuple(local_matrix(blocks(target_b), i) for i in range(2))
          == expected_b)
    check(fibre_formula(target_a) == 2)
    check(fibre_formula(target_b) == 1)
    return rows, targets_checked, expected_a, expected_b


def verify_sharp_family(limit=50):
    for n in range(2, limit + 1):
        for block_count in range(2, n):
            word = ((0,) * (n - block_count + 1)
                    + tuple(range(1, block_count)))
            tail, period = tail_and_period(word)
            check(tail == min(n - 2, 2 * block_count - 2))
            check(period == block_count)


def main():
    print("P169_SUCCESSOR_TRANSFER_EXACT_AUDIT_R0")
    queue_cases = verify_queue_cones()
    carrier_rows = verify_carriers()
    fibre_rows, targets, matrices_a, matrices_b = verify_fibres()
    verify_sharp_family()
    print("STATE_ORDER", STATE_NAMES)
    print("QUEUE_CONE_CASES", queue_cases)
    for row in carrier_rows:
        print("CARRIER", row)
    for row in fibre_rows:
        print("FIBRE", row)
    print("FIBRE_TARGETS", targets)
    print("INTERLACING_A", "025|134", "MATRICES", matrices_a, "FIBRE", 2)
    print("INTERLACING_B", "035|124", "MATRICES", matrices_b, "FIBRE", 1)
    print("STRATUM_CLOCK", "min(n-2,2k-2)", "VERIFIED_N_LE_10")
    print("SHARP_WITNESS", "0^(n-k+1)12...(k-1)", "VERIFIED_N_LE_50")
    print("BOUNDARIES", "n=1 k=1 k=n n=2k singleton wrap INCLUDED")
    print("FIBRE_FORMULA", "TRACE_OF_EXPLICIT_5_STATE_LOCAL_PRODUCT")
    print("ASSERTIONS", ASSERTIONS)
    print("DECISION AUTHOR_ROUND0_PASS")
    print("EXTERNAL_STATUS HOLD_EXTERNAL_OWNER_THIN")


if __name__ == "__main__":
    main()
