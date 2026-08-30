#!/usr/bin/env python3
"""Exact five-bit transfer recurrence for record-reversal image sizes."""

from collections import Counter
from itertools import permutations
from math import factorial


ASSERTIONS = 0


def check(statement, context):
    global ASSERTIONS
    ASSERTIONS += 1
    if not statement:
        raise AssertionError(context)


def transition(state, j, is_record):
    even, odd, qbit, last_parity, previous = state
    parity = j & 1
    if is_record:
        last_parity = parity
        qbit = previous
        available = odd if parity else even
        current = previous or available
    else:
        current = qbit and parity == last_parity
    if current:
        if parity:
            odd = 1
        else:
            even = 1
    return (int(even), int(odd), int(qbit), int(last_parity), int(current))


def image_counts(maximum):
    # Before position 1: d_0=1 is an even reachable cut.  Position 1 is a
    # forced record.
    state0 = (1, 0, 1, 0, 1)
    vector = Counter({transition(state0, 1, True): 1})
    answer = [1, sum(weight for state, weight in vector.items() if state[-1])]
    check(sum(vector.values()) == 1, "n=1 mass")
    for j in range(2, maximum + 1):
        nxt = Counter()
        for state, weight in vector.items():
            nxt[transition(state, j, True)] += weight
            nxt[transition(state, j, False)] += (j - 1) * weight
        vector = nxt
        check(sum(vector.values()) == factorial(j), (j, "factorial mass"))
        answer.append(sum(weight for state, weight in vector.items() if state[-1]))
    return answer


def record_blocks(word):
    if not word:
        return ()
    starts = []
    maximum = -1
    for index, value in enumerate(word):
        if value > maximum:
            starts.append(index)
            maximum = value
    starts.append(len(word))
    return tuple(word[starts[i] : starts[i + 1]] for i in range(len(starts) - 1))


def step(word):
    result = []
    for block in record_blocks(word):
        result.extend(reversed(block) if len(block) % 2 == 0 else block)
    return tuple(result)


def record_set(word):
    maximum = -1
    result = set()
    for j, value in enumerate(word, 1):
        if value > maximum:
            maximum = value
            result.add(j)
    return frozenset(result)


def main():
    maximum = 30
    recurrence = image_counts(maximum)
    literal = []
    for n in range(10):
        universe = tuple(permutations(range(n)))
        images = {step(word) for word in universe}
        literal.append(len(images))
        check(len(images) == recurrence[n], (n, len(images), recurrence[n]))
        if n:
            record_multiplicity = Counter(record_set(word) for word in universe)
            for positions, count in record_multiplicity.items():
                predicted = 1
                for j in range(2, n + 1):
                    if j not in positions:
                        predicted *= j - 1
                check(count == predicted, (n, positions, count, predicted))
    print("record-block image automaton: PASS")
    print(f"assertions={ASSERTIONS}")
    print("literal_n0_to_n9", literal)
    print("image_n0_to_n30", recurrence)
    print("garden_n0_to_n15", [factorial(n) - recurrence[n] for n in range(16)])


if __name__ == "__main__":
    main()
