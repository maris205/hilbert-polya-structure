#!/usr/bin/env python3
"""Deterministic exact checks for P165.

The program starts from the literal padded-shortening map.  It imports no
scout code and uses no third-party package, randomness, floating point,
network, or clock.  Binary subspaces are enumerated through length seven.
Separate tuple implementations enumerate subspaces over F_3, F_4, and F_5.
"""

from collections import Counter, deque
from itertools import product
from math import factorial
from pathlib import Path


ASSERTIONS = 0


def check(condition, label):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def iterate(step, state, time):
    for _ in range(time):
        state = step(state)
    return state


def falling(value, length):
    answer = 1
    for offset in range(length):
        answer *= value - offset
    return answer


def extreme_count(zero_coordinates, time, q):
    active = (1 << time) - 1
    if zero_coordinates < active:
        return 0
    denominator = 1
    for index in range(time):
        denominator *= factorial(1 << index)
    return (
        falling(zero_coordinates, active)
        // denominator
        * (q - 1) ** (active - time)
    )


# -------------------------------------------------------------------------
# Fast independent binary implementation.


def binary_subspaces(n):
    zero = frozenset((0,))
    seen = {zero}
    queue = deque((zero,))
    while queue:
        space = queue.popleft()
        for vector in range(1, 1 << n):
            if vector not in space:
                extension = frozenset(set(space) | {x ^ vector for x in space})
                if extension not in seen:
                    seen.add(extension)
                    queue.append(extension)
    return seen


def binary_distance(code):
    return min((word.bit_count() for word in code if word), default=10**9)


def binary_support(code):
    support = 0
    for word in code:
        support |= word
    return support


def binary_purge(code, weak=False):
    if len(code) == 1:
        return 0
    distance = binary_distance(code)
    purge = 0
    for word in code:
        if word and (
            word.bit_count() <= 2 * distance
            if weak
            else word.bit_count() < 2 * distance
        ):
            purge |= word
    return purge


def binary_step(code):
    purge = binary_purge(code)
    return frozenset(word for word in code if word & purge == 0)


def binary_weak_step(code):
    purge = binary_purge(code, weak=True)
    return frozenset(word for word in code if word & purge == 0)


def binary_depth(code):
    depth = 0
    while len(code) > 1:
        code = binary_step(code)
        depth += 1
    return depth


def check_binary_extreme_structure(source, target, time):
    current = source
    blocks = []
    for index in range(time):
        purge = binary_purge(current)
        nxt = binary_step(current)
        check(purge.bit_count() == 1 << index,
              ("F2 extreme block size", time, index, source))
        check(purge in current,
              ("F2 pure minimum word", time, index, source))
        reconstructed = frozenset(
            set(nxt) | {word ^ purge for word in nxt}
        )
        check(reconstructed == current,
              ("F2 direct sum layer", time, index, source))
        blocks.append(purge)
        current = nxt
    check(current == target, ("F2 extreme endpoint", source, target, time))
    union = 0
    for block in blocks:
        check(union & block == 0, ("F2 extreme disjoint", source, time))
        union |= block
    check(
        union == (binary_support(source) & ~binary_support(target)),
        ("F2 extreme support union", source, target, time),
    )


def binary_audit():
    expected_states = [1, 2, 5, 16, 67, 374, 2825, 29212]
    rows = []
    for n in range(8):
        spaces = binary_subspaces(n)
        check(len(spaces) == expected_states[n], ("F2 state census", n))
        depth_hist = Counter()
        for code in spaces:
            nxt = binary_step(code)
            check(nxt in spaces, ("F2 closure", n, code))
            check(nxt <= code, ("F2 descending", n, code))
            if len(code) == 1:
                check(nxt == code, ("F2 zero fixed", n))
            else:
                check(nxt != code, ("F2 proper", n, code))
                if len(nxt) > 1:
                    check(
                        binary_distance(nxt) >= 2 * binary_distance(code),
                        ("F2 distance doubling", n, code),
                    )
            depth = binary_depth(code)
            check(depth <= (n + 1).bit_length() - 1,
                  ("F2 height upper", n, code))
            check(len(code).bit_length() - 1 >= depth,
                  ("F2 zero-target dimension bound", n, code))
            check(binary_support(code).bit_count() >= (1 << depth) - 1,
                  ("F2 zero-target support bound", n, code))
            depth_hist[depth] += 1

        height = (n + 1).bit_length() - 1
        check(max(depth_hist) == height, ("F2 sharp height", n))

        images = set(spaces)
        image_sizes = []
        for time in range(5):
            image_sizes.append(len(images))
            threshold = 1 << time
            required = threshold - 1
            predicted = {
                target
                for target in spaces
                if len(target) == 1
                or (
                    binary_distance(target) >= threshold
                    and n - binary_support(target).bit_count() >= required
                )
            }
            check(images == predicted, ("F2 every-target image", n, time))

            observed_extreme = Counter()
            for source in spaces:
                target = iterate(binary_step, source, time)
                if len(target) > 1:
                    dimension_gap = (
                        len(source).bit_length() - len(target).bit_length()
                    )
                    support_gap = (
                        binary_support(source) & ~binary_support(target)
                    ).bit_count()
                    check(dimension_gap >= time,
                          ("F2 target dimension bound", n, time, source))
                    check(support_gap >= required,
                          ("F2 target support bound", n, time, source))
                    if dimension_gap == time and support_gap == required:
                        observed_extreme[target] += 1
                        check_binary_extreme_structure(source, target, time)

            for target in spaces:
                if len(target) == 1:
                    continue
                zeros = n - binary_support(target).bit_count()
                wanted = (
                    extreme_count(zeros, time, 2)
                    if binary_distance(target) >= threshold
                    else 0
                )
                check(observed_extreme[target] == wanted,
                      ("F2 extremal fibre", n, time, target))

            if time > 0:
                exact_minimal = sum(
                    binary_depth(source) == time
                    and len(source).bit_length() - 1 == time
                    and binary_support(source).bit_count() == required
                    for source in spaces
                )
                check(exact_minimal == extreme_count(n, time, 2),
                      ("F2 zero exact-depth extremizers", n, time))
            images = {binary_step(code) for code in images}

        rows.append(
            f"n={n}: states={len(spaces)}, max_depth={max(depth_hist)}, "
            f"depth_hist={dict(sorted(depth_hist.items()))}, "
            f"image_sizes_t0..4={image_sizes}"
        )
    return rows


# -------------------------------------------------------------------------
# Tuple implementation over prime fields and the nonprime field F_4.


def field_operations(q):
    if q in (3, 5):
        return (
            lambda left, right: (left + right) % q,
            lambda left, right: (left * right) % q,
        )
    if q == 4:
        multiplication = (
            (0, 0, 0, 0),
            (0, 1, 2, 3),
            (0, 2, 3, 1),
            (0, 3, 1, 2),
        )
        return (lambda left, right: left ^ right,
                lambda left, right: multiplication[left][right])
    raise ValueError(q)


def vector_add(left, right, add):
    return tuple(add(x, y) for x, y in zip(left, right))


def scalar_multiple(scalar, vector, multiply):
    return tuple(multiply(scalar, value) for value in vector)


def field_subspaces(q, n):
    add, multiply = field_operations(q)
    zero_vector = (0,) * n
    zero = frozenset((zero_vector,))
    vectors = tuple(product(range(q), repeat=n))
    seen = {zero}
    queue = deque((zero,))
    while queue:
        space = queue.popleft()
        for vector in vectors:
            if vector not in space:
                extension = frozenset(
                    vector_add(word, scalar_multiple(scalar, vector, multiply), add)
                    for word in space
                    for scalar in range(q)
                )
                if extension not in seen:
                    seen.add(extension)
                    queue.append(extension)
    return seen


def word_support(word):
    return frozenset(index for index, value in enumerate(word) if value)


def field_support(code):
    return frozenset().union(*(word_support(word) for word in code))


def field_distance(code):
    return min((len(word_support(word)) for word in code if any(word)),
               default=10**9)


def field_purge(code):
    if len(code) == 1:
        return frozenset()
    distance = field_distance(code)
    return frozenset().union(*(
        word_support(word)
        for word in code
        if any(word) and len(word_support(word)) < 2 * distance
    ))


def field_step(code):
    purge = field_purge(code)
    return frozenset(
        word for word in code
        if all(word[index] == 0 for index in purge)
    )


def field_dimension(code, q):
    size = len(code)
    dimension = 0
    while size > 1:
        check(size % q == 0, ("field dimension", q, len(code)))
        size //= q
        dimension += 1
    check(size == 1, ("field dimension terminal", q, len(code)))
    return dimension


def field_depth(code):
    depth = 0
    while len(code) > 1:
        code = field_step(code)
        depth += 1
    return depth


def check_field_extreme_structure(source, target, time, q):
    add, multiply = field_operations(q)
    current = source
    union = frozenset()
    for index in range(time):
        purge = field_purge(current)
        nxt = field_step(current)
        check(len(purge) == 1 << index,
              ("Fq extreme block size", q, time, index, source))
        pure = [
            word for word in current
            if any(word) and word_support(word) == purge
        ]
        check(len(pure) == q - 1,
              ("Fq pure line census", q, time, index, source))
        generator = pure[0]
        reconstructed = frozenset(
            vector_add(word, scalar_multiple(scalar, generator, multiply), add)
            for word in nxt
            for scalar in range(q)
        )
        check(reconstructed == current,
              ("Fq direct sum layer", q, time, index, source))
        check(not (union & purge),
              ("Fq extreme disjoint", q, time, index, source))
        union |= purge
        current = nxt
    check(current == target, ("Fq extreme endpoint", q, source, target, time))
    check(union == field_support(source) - field_support(target),
          ("Fq extreme support union", q, source, target, time))


def field_audit(q, maximum_n, maximum_time, expected_states):
    rows = []
    for n in range(maximum_n + 1):
        spaces = field_subspaces(q, n)
        check(len(spaces) == expected_states[n], ("Fq state census", q, n))
        depths = Counter()
        dimensions = {code: field_dimension(code, q) for code in spaces}
        for code in spaces:
            nxt = field_step(code)
            check(nxt in spaces, ("Fq closure", q, n, code))
            check(nxt <= code, ("Fq descending", q, n, code))
            if len(code) == 1:
                check(nxt == code, ("Fq zero fixed", q, n))
            else:
                check(nxt != code, ("Fq proper", q, n, code))
                if len(nxt) > 1:
                    check(field_distance(nxt) >= 2 * field_distance(code),
                          ("Fq distance doubling", q, n, code))
            depth = field_depth(code)
            check(depth <= (n + 1).bit_length() - 1,
                  ("Fq height upper", q, n, code))
            check(dimensions[code] >= depth,
                  ("Fq zero-target dimension bound", q, n, code))
            check(len(field_support(code)) >= (1 << depth) - 1,
                  ("Fq zero-target support bound", q, n, code))
            depths[depth] += 1
        check(max(depths) == (n + 1).bit_length() - 1,
              ("Fq sharp height", q, n))

        images = set(spaces)
        image_sizes = []
        for time in range(maximum_time + 1):
            image_sizes.append(len(images))
            threshold = 1 << time
            required = threshold - 1
            predicted = {
                target
                for target in spaces
                if len(target) == 1
                or (
                    field_distance(target) >= threshold
                    and n - len(field_support(target)) >= required
                )
            }
            check(images == predicted,
                  ("Fq every-target image", q, n, time))

            observed_extreme = Counter()
            for source in spaces:
                target = iterate(field_step, source, time)
                if len(target) > 1:
                    dimension_gap = dimensions[source] - dimensions[target]
                    support_gap = len(field_support(source) - field_support(target))
                    check(dimension_gap >= time,
                          ("Fq target dimension bound", q, n, time, source))
                    check(support_gap >= required,
                          ("Fq target support bound", q, n, time, source))
                    if dimension_gap == time and support_gap == required:
                        observed_extreme[target] += 1
                        check_field_extreme_structure(source, target, time, q)

            for target in spaces:
                if len(target) == 1:
                    continue
                zeros = n - len(field_support(target))
                wanted = (
                    extreme_count(zeros, time, q)
                    if field_distance(target) >= threshold
                    else 0
                )
                check(observed_extreme[target] == wanted,
                      ("Fq extremal fibre", q, n, time, target))

            if time > 0:
                exact_minimal = sum(
                    field_depth(source) == time
                    and dimensions[source] == time
                    and len(field_support(source)) == required
                    for source in spaces
                )
                check(exact_minimal == extreme_count(n, time, q),
                      ("Fq zero exact-depth extremizers", q, n, time))
            images = {field_step(code) for code in images}

        rows.append(
            f"q={q}, n={n}: states={len(spaces)}, max_depth={max(depths)}, "
            f"depth_hist={dict(sorted(depths.items()))}, "
            f"image_sizes={image_sizes}"
        )
    return rows


# -------------------------------------------------------------------------
# Theorem-statement boundary sentinels.


def boundary_sentinels():
    check(((0 + 1).bit_length() - 1) == 0, "n=0 height sentinel")
    for q in (2, 3, 4, 5):
        check(extreme_count(7, 0, q) == 1, ("t=0 empty product", q))

    spaces2 = binary_subspaces(2)
    zero2 = frozenset((0,))
    zero_fibre = [code for code in spaces2 if binary_step(code) == zero2]
    minimal_zero_slice = [
        code for code in zero_fibre
        if binary_depth(code) == 1
        and len(code).bit_length() - 1 == 1
        and binary_support(code).bit_count() == 1
    ]
    check(len(zero_fibre) == 5, "zero complete fibre sentinel")
    check(len(minimal_zero_slice) == 2, "zero extremal slice sentinel")
    check(len(zero_fibre) != len(minimal_zero_slice),
          "zero fibre is not extremal slice")

    full_support_target = frozenset((0, 0b111))
    spaces3 = binary_subspaces(3)
    check(full_support_target not in {binary_step(code) for code in spaces3},
          "full-support target sentinel")
    check({iterate(binary_step, code, 2) for code in binary_subspaces(2)} == {zero2},
          "exhausted capacity sentinel")

    strict_witness = frozenset((0, 0b001, 0b110, 0b111))
    check(binary_step(strict_witness) == frozenset((0, 0b110)),
          "strict threshold keeps double block")
    check(binary_weak_step(strict_witness) == frozenset((0,)),
          "weak threshold changes atlas")
    check(max((word.bit_length() for word in binary_step(strict_witness)), default=0) <= 3,
          "padded ambient sentinel")

    main_text = Path(__file__).resolve().parents[1].joinpath("main.tex").read_text()
    normalized_main = " ".join(main_text.split())
    required_text = (
        r"\documentclass[a4paper,10pt]{amsart}",
        r"\author{Anonymous}",
        "padded shortening self-map",
        "The strict inequality",
        r"Let $D\ne0$ and $t\geq0$",
        "Formula \\eqref{eq:count} is not a formula for the complete fibre",
        "The zero target belongs to every time image",
        "This exact-depth statement is not the full fibre",
        r"If $n=0$",
        "nonzero full-support target",
        r"If $2^t-1>n$",
        "include nonprime prime powers",
        r"\texttt{HOLD\_EXTERNAL}",
        "JibrilEtAl2013",
    )
    for phrase in required_text:
        check(phrase in normalized_main,
              ("main theorem-statement sentinel", phrase))


def main():
    print("P165_LOW_WEIGHT_SUPPORT_SHORTENING_EXACT_AUDIT")
    print("BINARY_LINEAR_CODES")
    for row in binary_audit():
        print(row)
    print("TERNARY_LINEAR_CODES")
    for row in field_audit(3, 4, 3, [1, 2, 6, 28, 212]):
        print(row)
    print("QUATERNARY_LINEAR_CODES")
    for row in field_audit(4, 3, 3, [1, 2, 7, 44]):
        print(row)
    print("QUINARY_LINEAR_CODES")
    for row in field_audit(5, 3, 3, [1, 2, 8, 64]):
        print(row)
    boundary_sentinels()
    print("BOUNDARY_SENTINELS PASS")
    print(f"ASSERTIONS {ASSERTIONS}")
    print("RESULT PASS")


if __name__ == "__main__":
    main()
