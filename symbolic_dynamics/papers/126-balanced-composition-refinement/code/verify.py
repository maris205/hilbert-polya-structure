#!/usr/bin/env python3
"""Exact controls for synchronous balanced refinement of integer compositions."""

from collections import Counter
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


def normal_form(word, times):
    width = 1 << times
    answer = []
    for value in word:
        if value <= width:
            answer.extend([1] * value)
        else:
            answer.append(value)
    return tuple(answer)


def suffix_decode(target, times):
    """Return the unique normal-form source, or None off the iterated image."""
    width = 1 << times
    position = len(target)
    reverse_source = []
    while position:
        if target[position - 1] == 1:
            reverse_source.append(1)
            position -= 1
            continue
        if position < width:
            return None
        block = target[position - width:position]
        value = sum(block)
        if value <= width or codeword(times, value) != block:
            return None
        reverse_source.append(value)
        position -= width
    return tuple(reversed(reverse_source))


def fibre_dp(target, times):
    size = len(target)
    prefix_sum = [0]
    for value in target:
        prefix_sum.append(prefix_sum[-1] + value)
    dp = [0] * (size + 1)
    dp[0] = 1
    width = 1 << times
    for end in range(1, size + 1):
        for start in range(max(0, end - width), end):
            value = prefix_sum[end] - prefix_sum[start]
            if codeword(times, value) == target[start:end]:
                dp[end] += dp[start]
    return dp[-1]


def restricted_count(n, width):
    """Compositions of n with parts at most width; empty count is one."""
    values = [0] * (n + 1)
    values[0] = 1
    for total in range(1, n + 1):
        values[total] = sum(values[max(0, total - width):total])
    return values[n]


def fibre_from_normal(normal, times):
    width = 1 << times
    answer = 1
    run = 0
    for value in normal + (0,):
        if value == 1:
            run += 1
        else:
            answer *= restricted_count(run, width)
            run = 0
            if value:
                check(value > width, "normal alphabet")
    return answer


def image_counts(limit, width):
    """Compositions whose parts lie in {1} union {width+1,width+2,...}."""
    values = [0] * (limit + 1)
    values[0] = 1
    for total in range(1, limit + 1):
        values[total] = values[total - 1]
        values[total] += sum(values[total - part]
                             for part in range(width + 1, total + 1))
    return values


def rational_image_counts(limit, width):
    """Coefficients of (1-x)/(1-2x+x^2-x^(width+1))."""
    values = [0] * (limit + 1)
    values[0] = 1
    if limit:
        values[1] = 1
    for n in range(2, limit + 1):
        values[n] = 2 * values[n - 1] - values[n - 2]
        if n >= width + 1:
            values[n] += values[n - width - 1]
    return values


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


def literal_clock_lane():
    maximum_depth = {}
    for n in range(19):
        states = compositions(n)
        check(len(states) == (1 if n == 0 else 1 << (n - 1)),
              "composition count")
        for word in states:
            target = step(word)
            check(target in states, "closure")
            check(sum(target) == n, "weight")
            check((target == word) == all(value == 1 for value in word),
                  "fixed criterion")
            check(depth(word) == max((ceil_log2(value) for value in word),
                                     default=0),
                  "pointwise clock")
        observed = max((depth(word) for word in states), default=0)
        check(observed == ceil_log2(n), "global clock")
        maximum_depth[n] = observed
    return maximum_depth


def kernel_fibre_lane():
    image_rows = {}
    maximum_rows = {}
    for times in range(6):
        width = 1 << times
        predicted_images = image_counts(15, width)
        for n in range(16):
            states = compositions(n)
            literal = Counter(iterate(source, times) for source in states)
            normal_to_image = {}
            image_to_normal = {}
            for source in states:
                image = iterate(source, times)
                normal = normal_form(source, times)
                check(iterate(normal, times) == image,
                      (n, times, source, "normal congruence"))
                check(normal_to_image.setdefault(normal, image) == image,
                      (n, times, source, "normal implies image"))
                check(image_to_normal.setdefault(image, normal) == normal,
                      (n, times, source, "image implies normal"))
                check(suffix_decode(image, times) == normal,
                      (n, times, source, "suffix decoder"))
            check(len(literal) == len(normal_to_image) == len(image_to_normal),
                  (n, times, "kernel cardinality"))
            check(len(literal) == predicted_images[n],
                  (n, times, "image census"))
            check(sum(literal.values()) == len(states), "fibre mass")

            maximum = 0
            for target in states:
                decoded = suffix_decode(target, times)
                predicted = (0 if decoded is None
                             else fibre_from_normal(decoded, times))
                check(literal[target] == predicted,
                      (n, times, target, "normal fibre product"))
                check(fibre_dp(target, times) == predicted,
                      (n, times, target, "independent factorization DP"))
                maximum = max(maximum, literal[target])
            check(maximum == restricted_count(n, width),
                  (n, times, "maximum fibre"))
            check(literal[tuple([1] * n)] == restricted_count(n, width),
                  (n, times, "all-one extremizer"))
            image_rows[(times, n)] = len(literal)
            maximum_rows[(times, n)] = maximum
    return image_rows, maximum_rows


def code_lane():
    for times in range(9):
        width = 1 << times
        seen_long = {}
        for value in range(1, 257):
            word = codeword(times, value)
            check(word == iterate((value,), times), "codeword recursion")
            check(sum(word) == value, "codeword weight")
            check(len(word) <= width, "codeword length")
            check(max(word) == (value + width - 1) // width,
                  "largest descendant")
            check((word == tuple([1] * value)) == (value <= width),
                  "complete split threshold")
            if value > width:
                check(len(word) == width, "long codeword length")
                check(word[-1] == (value + width - 1) // width > 1,
                      "suffix marker")
                check(seen_long.setdefault(word, value) == value,
                      "long code injectivity")
                check(suffix_decode(word, times) == (value,),
                      "single-codeword decoder")


def image_ogf_lane(image_rows):
    sentinels = {}
    for times in range(9):
        width = 1 << times
        direct = image_counts(90, width)
        rational = rational_image_counts(90, width)
        check(direct == rational, (times, "rational OGF"))
        for n in range(16):
            check(direct[n] == image_rows[(min(times, 5), n)]
                  if times <= 5 else direct[n] == 1,
                  (times, n, "image boundary"))
        if times >= 5:
            for n in range(16):
                check(direct[n] == 1, (times, n, "stabilized image"))
        sentinels[times] = direct
    return sentinels


def depth_census_lane():
    for n in range(19):
        states = compositions(n)
        literal = Counter(depth(word) for word in states)
        for times in range(7):
            width = 1 << times
            observed = sum(count for level, count in literal.items()
                           if level <= times)
            check(observed == restricted_count(n, width),
                  (n, times, "cumulative depth census"))


def boundary_lane():
    for n in range(21):
        fixed = tuple([1] * n)
        check(step(fixed) == fixed, "fixed boundary")
        for times in range(7):
            width = 1 << times
            check(fibre_dp(fixed, times) == restricted_count(n, width),
                  "fixed-target fibre recurrence")
            check(normal_form(fixed, times) == fixed, "fixed normal form")
            check(suffix_decode(fixed, times) == fixed, "fixed decoder")


def main():
    depths = literal_clock_lane()
    images, maxima = kernel_fibre_lane()
    code_lane()
    ogf = image_ogf_lane(images)
    depth_census_lane()
    boundary_lane()
    print("balanced composition refinement exact control: PASS")
    print(f"assertions={ASSERTIONS}")
    print("literal dynamics: all compositions n<=18")
    print("kernel/fibres: all sources and targets n<=15, t<=5")
    print("code/suffix decoder: source letters m<=256, t<=8")
    print("all-iterate image OGF recurrence: n<=90, t<=8")
    print("maximum depth n=0..18", [depths[n] for n in range(19)])
    for times in (1, 2, 3):
        print(f"image t={times} n=0..18", ogf[times][:19])
    print("maximum fibre t=1 n=0..15",
          [maxima[(1, n)] for n in range(16)])
    print("maximum fibre t=3 n=0..15",
          [maxima[(3, n)] for n in range(16)])
    print("scope: restricted-composition enumeration and suffix-code theory are zero-credit")
    print("scope: finite enumeration is falsification evidence, not an all-size proof")


if __name__ == "__main__":
    main()
