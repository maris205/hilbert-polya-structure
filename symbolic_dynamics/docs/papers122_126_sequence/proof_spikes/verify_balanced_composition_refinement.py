#!/usr/bin/env python3
"""Exact controls for synchronous balanced refinement of compositions."""

from collections import Counter, defaultdict
from functools import lru_cache


ASSERTIONS = 0


def check(condition, message="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


@lru_cache(maxsize=None)
def compositions(n):
    if n == 0:
        return ((),)
    answer = []
    for first in range(1, n + 1):
        for tail in compositions(n - first):
            answer.append((first,) + tail)
    return tuple(answer)


def step(word):
    answer = []
    for value in word:
        if value == 1:
            answer.append(1)
        else:
            answer.extend((value // 2, (value + 1) // 2))
    return tuple(answer)


def iterate(word, times):
    for _ in range(times):
        word = step(word)
    return word


@lru_cache(maxsize=None)
def codeword(times, value):
    if times == 0 or value == 1:
        return (value,)
    return (codeword(times - 1, value // 2)
            + codeword(times - 1, (value + 1) // 2))


def fibre_dp(target, times):
    size = len(target)
    prefix_sum = [0]
    for value in target:
        prefix_sum.append(prefix_sum[-1] + value)
    dp = [0] * (size + 1)
    dp[0] = 1
    bound = 1 << times
    for end in range(1, size + 1):
        for start in range(max(0, end - bound), end):
            value = prefix_sum[end] - prefix_sum[start]
            if codeword(times, value) == target[start:end]:
                dp[end] += dp[start]
    return dp[-1]


def generalized_fibonacci(n, width):
    values = [0] * (n + 1)
    values[0] = 1
    for total in range(1, n + 1):
        values[total] = sum(values[max(0, total - width):total])
    return values[n]


def ceil_log2(value):
    if value <= 1:
        return 0
    return (value - 1).bit_length()


def depth(word):
    predicted = max((ceil_log2(value) for value in word), default=0)
    current = word
    for time in range(predicted):
        nxt = step(current)
        check(sum(nxt) == sum(current), "weight changed")
        check(len(nxt) > len(current), "length Lyapunov failed")
        current = nxt
        check(current == iterate(word, time + 1), "iterate mismatch")
    check(step(current) == current, "clock did not settle")
    return predicted


def one_step_image_recurrence(limit):
    # State (last, d_{j-1}, d_j) after a nonempty prefix.
    layers = [defaultdict(int) for _ in range(limit + 1)]
    for value in range(1, limit + 1):
        layers[value][(value, 1, int(value == 1))] += 1
    image = [1] + [0] * limit
    mass = [1] + [0] * limit
    for total in range(1, limit + 1):
        current_items = list(layers[total].items())
        image[total] = sum(count for (_, _, reachable), count in current_items
                           if reachable)
        mass[total] = sum(count for _, count in current_items)
        for (last, previous, reachable), count in current_items:
            for value in range(1, limit - total + 1):
                new_reachable = ((reachable and value == 1)
                                 or (previous and value in (last, last + 1)))
                layers[total + value][(value, reachable, int(new_reachable))] += count
    return image, mass


def literal_lane():
    image_rows = {}
    maximum_rows = {}
    for n in range(0, 19):
        states = compositions(n)
        check(len(states) == (1 if n == 0 else 1 << (n - 1)), "composition count")
        for word in states:
            target = step(word)
            check(target in states, "closure")
            check(sum(target) == n, "weight")
            check((target == word) == all(value == 1 for value in word), "fixed criterion")
            check(depth(word) == max((ceil_log2(value) for value in word), default=0),
                  "pointwise clock")
        maximum_depth = max((depth(word) for word in states), default=0)
        check(maximum_depth == ceil_log2(n), "global clock")
        maximum_rows[n] = maximum_depth
        image_rows[n] = len({step(word) for word in states})
    return image_rows, maximum_rows


def fibre_lane():
    fibre_sentinels = {}
    for times in range(0, 6):
        for n in range(0, 16):
            states = compositions(n)
            literal = Counter(iterate(source, times) for source in states)
            check(sum(literal.values()) == len(states), "fibre mass")
            predicted_maximum = generalized_fibonacci(n, 1 << times)
            check(literal[tuple([1] * n)] == predicted_maximum,
                  "all-ones extremizer")
            maximum = 0
            for target in states:
                predicted = fibre_dp(target, times)
                check(literal[target] == predicted,
                      f"iterated fibre n={n} t={times} target={target}")
                maximum = max(maximum, literal[target])
            check(maximum == predicted_maximum, "maximum iterated fibre")
            fibre_sentinels[(times, n)] = maximum
    return fibre_sentinels


def codeword_lane():
    for times in range(0, 9):
        for value in range(1, 257):
            word = codeword(times, value)
            check(word == iterate((value,), times), "codeword recursion")
            check(sum(word) == value, "codeword weight")
            check(len(word) <= 1 << times, "codeword length")
            check(max(word) == (value + (1 << times) - 1) // (1 << times),
                  "largest descendant")
            check((word == tuple([1] * value)) == (value <= 1 << times),
                  "all-one codeword threshold")


def aggregate_lane(image_rows):
    image, mass = one_step_image_recurrence(90)
    for n in range(0, 91):
        check(mass[n] == (1 if n == 0 else 1 << (n - 1)), "aggregate mass")
    for n in range(0, 19):
        check(image[n] == image_rows[n], "aggregate image count")
        literal_garden = (1 if n == 0 else 1 << (n - 1)) - image_rows[n]
        check(literal_garden >= 0, "garden sign")
    return image


def boundary_lane():
    for n in range(0, 21):
        fixed = tuple([1] * n)
        check(step(fixed) == fixed, "fixed boundary")
        for times in range(0, 7):
            check(fibre_dp(fixed, times) == generalized_fibonacci(n, 1 << times),
                  "fixed-target fibre recurrence")


def main():
    images, depths = literal_lane()
    fibres = fibre_lane()
    codeword_lane()
    aggregate = aggregate_lane(images)
    boundary_lane()
    print("balanced composition refinement verifier: PASS")
    print(f"exact assertions: {ASSERTIONS:,}")
    print("literal dynamics: all compositions n<=18")
    print("iterated fibres: all targets n<=15, t<=5")
    print("codewords: m<=256, t<=8")
    print("aggregate one-step image recurrence: n<=90")
    print("image n=0..18:", [images[n] for n in range(19)])
    print("garden n=0..18:", [(1 if n == 0 else 1 << (n - 1)) - images[n]
                               for n in range(19)])
    print("maximum depth n=0..18:", [depths[n] for n in range(19)])
    print("maximum one-step fibre n=0..15:", [fibres[(1, n)] for n in range(16)])
    print("maximum three-step fibre n=0..15:", [fibres[(3, n)] for n in range(16)])
    print("aggregate recurrence n=0..25:", aggregate[:26])
    print("scope sentinel: generic substitutions/divide-and-conquer splitting are zero-credit")
    print("scope sentinel: all-size theorems are symbolic; enumeration is falsification only")


if __name__ == "__main__":
    main()
