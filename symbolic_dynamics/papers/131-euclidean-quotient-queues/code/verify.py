#!/usr/bin/env python3
"""Exact deterministic control for P131.

The digit dynamics, rational-pair subtraction, and literal normalized-path
self-map are separate.  Every canonical state of weight 2 <= N <= 18 is
exhausted.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from math import comb, gcd


ASSERTIONS = 0


def check(condition: bool, message: str = "") -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message or f"assertion {ASSERTIONS} failed")


def compositions(n: int):
    if n == 0:
        yield ()
        return
    for first in range(1, n + 1):
        for rest in compositions(n - first):
            yield (first,) + rest


def states(n: int):
    return tuple(word for word in compositions(n) if word and word[-1] >= 2)


def update(word):
    if len(word) == 1:
        return word
    if word[0] > 1:
        return word[1:] + word[:1]
    return word[1:-1] + (word[-1] + 1,)


def rational_value(word) -> Fraction:
    tail = Fraction(word[-1], 1)
    for digit in reversed(word[:-1]):
        tail = digit + Fraction(1, tail)
    return Fraction(1, tail)


def subtractive_path(value: Fraction) -> str:
    u, v = value.numerator, value.denominator
    check(0 < u < v and gcd(u, v) == 1)
    letters = []
    last = None
    while u and v:
        if u < v:
            v -= u
            last = "L"
        elif u > v:
            u -= v
            last = "R"
        else:
            check(last is not None)
            if last == "L":
                v -= u
            else:
                u -= v
        letters.append(last)
    check((u, v) in ((0, 1), (1, 0)))
    return "".join(letters)


def run_lengths(path: str):
    answer = []
    for letter in path:
        if not answer or answer[-1][0] != letter:
            answer.append([letter, 1])
        else:
            answer[-1][1] += 1
    return tuple(length for _letter, length in answer)


def flip_path(path: str) -> str:
    """Exchange L and R without changing any block boundary."""
    return path.translate(str.maketrans("LR", "RL"))


def block_spans(path: str):
    """Return half-open spans of maximal constant blocks."""
    answer = []
    start = 0
    for i in range(1, len(path) + 1):
        if i == len(path) or path[i] != path[start]:
            answer.append((start, i))
            start = i
    return tuple(answer)


def normalized_path(path: str) -> bool:
    if not path:
        return False
    spans = block_spans(path)
    return path[0] == "L" and spans[-1][1] - spans[-1][0] >= 2


def raw_path_update(path: str) -> str:
    """Literal normalized-string map Psi, without a run-length round trip."""
    check(normalized_path(path))
    first_end = block_spans(path)[0][1]
    if first_end == len(path):
        return path
    first_size = first_end
    normalized_tail = flip_path(path[first_end:])
    if first_size == 1:
        return normalized_tail + normalized_tail[-1]
    final_letter = "R" if normalized_tail[-1] == "L" else "L"
    return normalized_tail + final_letter * first_size


def raw_path_depth(path: str) -> int:
    """Index of the last singleton block, counted from one."""
    return max(
        (i for i, (start, end) in enumerate(block_spans(path), start=1)
         if end - start == 1),
        default=0,
    )


def raw_path_preimages(target: str):
    """The two possible predecessors derived directly as strings."""
    check(normalized_path(target))
    spans = block_spans(target)
    answer = []
    if len(spans) == 1:
        answer.append(target)
    else:
        last_start, last_end = spans[-1]
        penultimate_start, penultimate_end = spans[-2]
        if penultimate_end - penultimate_start >= 2:
            terminal_size = last_end - last_start
            answer.append("L" * terminal_size + flip_path(target[:last_start]))
    last_start, last_end = spans[-1]
    if last_end - last_start >= 3:
        answer.append("L" + flip_path(target[:-1]))
    return tuple(answer)


def tail_formula(word) -> int:
    return max((i + 1 for i, part in enumerate(word) if part == 1), default=0)


def terminal_core(word):
    if 1 not in word:
        return word
    size = len(word)
    nonones = [i for i, part in enumerate(word) if part > 1]
    contracted = {}
    for i in nonones:
        added = 0
        j = (i + 1) % size
        while word[j] == 1:
            added += 1
            j = (j + 1) % size
        contracted[i] = word[i] + added
    last_one = max(i for i, part in enumerate(word) if part == 1)
    order = [i for i in nonones if i > last_one] + [i for i in nonones if i <= last_one]
    return tuple(contracted[i] for i in order)


def primitive_period(word) -> int:
    for period in range(1, len(word) + 1):
        if len(word) % period == 0 and word == word[period:] + word[:period]:
            return period
    raise AssertionError("unreachable")


def orbit(word):
    seen = {}
    value = word
    while value not in seen:
        seen[value] = len(seen)
        value = update(value)
    return seen[value], len(seen) - seen[value], value


def fibonacci(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def depth_count(n: int, depth: int) -> int:
    if depth == 0:
        return fibonacci(n - 1)
    residual = n - depth - 2
    if residual < 0:
        return 0
    if depth == 1:
        return fibonacci(residual + 1)
    return sum(
        comb(j + depth - 2, depth - 2) * fibonacci(residual - j + 1)
        for j in range(residual + 1)
    )


def euler_phi(n: int) -> int:
    answer = n
    factor = 2
    remaining = n
    while factor * factor <= remaining:
        if remaining % factor == 0:
            answer -= answer // factor
            while remaining % factor == 0:
                remaining //= factor
        factor += 1
    if remaining > 1:
        answer -= answer // remaining
    return answer


def recurrent_cycles(n: int) -> int:
    total = 0
    for length in range(1, n // 2 + 1):
        fixed_sum = 0
        for divisor in range(1, gcd(n, length) + 1):
            if n % divisor or length % divisor:
                continue
            reduced_n = n // divisor
            reduced_length = length // divisor
            linear = comb(reduced_n - reduced_length - 1, reduced_length - 1)
            fixed_sum += euler_phi(divisor) * linear
        check(fixed_sum % length == 0)
        total += fixed_sum // length
    return total


def predicted_preimages(target):
    answer = []
    if len(target) == 1:
        answer.append(target)
    elif target[-2] >= 2:
        answer.append((target[-1],) + target[:-1])
    if target[-1] >= 3:
        answer.append((1,) + target[:-1] + (target[-1] - 1,))
    return tuple(answer)


def main() -> None:
    print("P131_EUCLIDEAN_QUOTIENT_QUEUE_EXACT_CONTROL")
    print(
        "engines=canonical digits + exact Fraction subtraction + "
        "literal normalized LR-string map"
    )
    for n in range(2, 19):
        carrier = states(n)
        carrier_set = set(carrier)
        fibres = Counter()
        depths = Counter()

        for word in carrier:
            value = rational_value(word)
            path = subtractive_path(value)
            check(len(path) == n)
            check(path[0] == "L")
            check(run_lengths(path) == word)
            check(normalized_path(path))

            next_path = raw_path_update(path)
            expected_next_path = subtractive_path(rational_value(update(word)))
            check(next_path == expected_next_path)
            check(normalized_path(next_path))
            check(run_lengths(next_path) == update(word))

            image = update(word)
            check(image in carrier_set)
            fibres[image] += 1
            tail, period, repeated = orbit(word)
            core = terminal_core(word)
            check(tail == tail_formula(word))
            check(raw_path_depth(path) == tail)
            check(period == primitive_period(core))
            iterate = word
            path_iterate = path
            for _ in range(tail):
                iterate = update(iterate)
                path_iterate = raw_path_update(path_iterate)
            check(iterate == core)
            check(path_iterate == subtractive_path(rational_value(core)))
            check(repeated in {core[i:] + core[:i] for i in range(len(core))})
            depths[tail] += 1

        gardens = 0
        for target in carrier:
            literal = predicted_preimages(target)
            target_path = subtractive_path(rational_value(target))
            path_literal = raw_path_preimages(target_path)
            expected_path_literal = tuple(
                subtractive_path(rational_value(source)) for source in literal
            )
            check(path_literal == expected_path_literal)
            check(len(set(path_literal)) == len(path_literal))
            for source_path in path_literal:
                check(normalized_path(source_path))
                check(raw_path_update(source_path) == target_path)
            check(len(set(literal)) == len(literal))
            for source in literal:
                check(source in carrier_set)
                check(update(source) == target)
            check(fibres[target] == len(literal))
            gardens += not literal

        for depth in range(n - 1):
            check(depths[depth] == depth_count(n, depth))
        check(max(depths) == n - 2)
        check(sum(depths.values()) == 1 << (n - 2))

        recurrent = {word for word in carrier if 1 not in word}
        unseen = set(recurrent)
        cycles = 0
        while unseen:
            word = min(unseen)
            cycle = {word[i:] + word[:i] for i in range(len(word))} & recurrent
            unseen -= cycle
            cycles += 1
        check(cycles == recurrent_cycles(n))

        image_formula = 1 if n <= 3 else 3 * (1 << (n - 4))
        garden_formula = 0 if n == 2 else (1 if n == 3 else 1 << (n - 4))
        check(len(fibres) == image_formula)
        check(gardens == garden_formula)
        check(max(fibres.values()) <= 2)
        fixed = sum(update(word) == word for word in carrier)
        check(fixed == sum(n % divisor == 0 for divisor in range(2, n + 1)))

        print(
            f"N={n} states={len(carrier)} image={len(fibres)} gardens={gardens} "
            f"recurrent={len(recurrent)} max_depth={max(depths)} cycles={cycles} "
            f"fixed={fixed} max_fibre={max(fibres.values())}"
        )

    print(f"ASSERTIONS={ASSERTIONS}")
    print("STATUS=PASS")
    print("scope_sentinel=finite exhaustion is falsification evidence, never proof")
    print("release_sentinel=bounded owner non-hit is not novelty; external HOLD")


if __name__ == "__main__":
    main()
