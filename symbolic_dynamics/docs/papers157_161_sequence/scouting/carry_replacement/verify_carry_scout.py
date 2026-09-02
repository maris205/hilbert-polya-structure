#!/usr/bin/env python3
"""Exact scout for synchronous radix-carry normalization.

This is a replacement candidate, not a paper verifier.  It checks the literal
weighted-composition carrier, all finite image layers, the sharp global clock,
and an every-target one-step fibre product.
"""

from __future__ import annotations

from collections import Counter
from functools import cache


ASSERTIONS = 0


def check(condition: bool, message: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def states(radix: int, width: int, mass: int) -> tuple[tuple[int, ...], ...]:
    """All (width+1)-digit nonnegative expansions of fixed weighted mass."""

    @cache
    def suffix(position: int, remaining: int) -> tuple[tuple[int, ...], ...]:
        if position == width:
            weight = radix**width
            if remaining % weight:
                return ()
            return ((remaining // weight,),)
        weight = radix**position
        rows: list[tuple[int, ...]] = []
        for digit in range(remaining // weight + 1):
            for tail in suffix(position + 1, remaining - digit * weight):
                rows.append((digit,) + tail)
        return tuple(rows)

    return suffix(0, mass)


def step(state: tuple[int, ...], radix: int) -> tuple[int, ...]:
    width = len(state) - 1
    target = [state[0] % radix]
    for position in range(1, width):
        target.append(
            state[position] % radix + state[position - 1] // radix
        )
    target.append(state[width] + state[width - 1] // radix)
    return tuple(target)


def iterate(state: tuple[int, ...], radix: int, time: int) -> tuple[int, ...]:
    for _ in range(time):
        state = step(state, radix)
    return state


def canonical(radix: int, width: int, mass: int) -> tuple[int, ...]:
    digits: list[int] = []
    remaining = mass
    for _ in range(width):
        digits.append(remaining % radix)
        remaining //= radix
    digits.append(remaining)
    return tuple(digits)


def predicted_one_step_fibre(target: tuple[int, ...], radix: int) -> int:
    width = len(target) - 1
    if target[0] >= radix:
        return 0
    answer = target[width] + 1
    for position in range(1, width):
        answer *= min(radix, target[position] + 1)
    return answer


def image_condition(
    target: tuple[int, ...], radix: int, time: int
) -> bool:
    width = len(target) - 1
    return all(
        target[position] < radix
        for position in range(min(time, width))
    )


def image_count_dp(radix: int, width: int, mass: int, time: int) -> int:
    """Coefficient of the frozen image-layer product."""

    @cache
    def count(position: int, remaining: int) -> int:
        if position == width:
            return int(remaining % (radix**width) == 0)
        weight = radix**position
        cap = remaining // weight
        if position < min(time, width):
            cap = min(cap, radix - 1)
        return sum(
            count(position + 1, remaining - digit * weight)
            for digit in range(cap + 1)
        )

    return count(0, mass)


def maximum_depth_formula(radix: int, width: int, mass: int) -> int:
    if mass == 0:
        return 0
    logarithm = 0
    power = 1
    while power * radix <= mass:
        power *= radix
        logarithm += 1
    return min(width, logarithm)


def verify_box(radix: int, width: int, mass: int) -> tuple[int, ...]:
    carrier = states(radix, width, mass)
    carrier_set = set(carrier)
    fixed = canonical(radix, width, mass)
    check(fixed in carrier_set, "canonical state missing")
    check(step(fixed, radix) == fixed, "canonical state is not fixed")

    one_step_fibres = Counter(step(source, radix) for source in carrier)
    for target in carrier:
        check(step(target, radix) in carrier_set, "carrier closure failed")
        check(
            one_step_fibres.get(target, 0)
            == predicted_one_step_fibre(target, radix),
            "one-step target fibre mismatch",
        )

    depth_histogram: Counter[int] = Counter()
    for source in carrier:
        current = source
        depth = 0
        while current != fixed:
            current = step(current, radix)
            depth += 1
            check(depth <= width, "width clock bound failed")
        depth_histogram[depth] += 1

    expected_maximum = maximum_depth_formula(radix, width, mass)
    check(max(depth_histogram) == expected_maximum, "sharp height mismatch")

    for time in range(width + 1):
        observed_image = {
            iterate(source, radix, time) for source in carrier
        }
        predicted_image = {
            target
            for target in carrier
            if image_condition(target, radix, time)
        }
        check(observed_image == predicted_image, "exact image layer mismatch")
        check(
            len(observed_image)
            == image_count_dp(radix, width, mass, time),
            "image generating-function coefficient mismatch",
        )
        if time == width:
            check(observed_image == {fixed}, "terminal image is not singleton")

    return (
        len(carrier),
        len(one_step_fibres),
        expected_maximum,
        max(one_step_fibres.values()),
        sum(depth * count for depth, count in depth_histogram.items()),
    )


def main() -> None:
    summary_cases = [
        (2, 4, 10),
        (2, 5, 31),
        (2, 5, 50),
        (3, 4, 20),
        (3, 5, 80),
        (4, 4, 70),
    ]
    summaries = {}
    for radix in (2, 3, 4):
        for width in range(1, 6):
            for mass in range(0, 41):
                verify_box(radix, width, mass)
    for case in summary_cases:
        summaries[case] = verify_box(*case)

    print("RADIX_CARRY_REPLACEMENT_SCOUT_V1")
    print("LITERAL maximal_parallel_carry_on_fixed_weighted_compositions")
    print("IMAGE first_min(t,n)_digits_are_canonical_radix_digits")
    print("FIBRE (top+1)*product_internal_min(radix,target_digit+1)")
    print("HEIGHT min(width,floor(log_radix(mass)))")
    for case in summary_cases:
        carrier, image, height, max_fibre, depth_sum = summaries[case]
        print(
            f"CASE radix={case[0]} width={case[1]} mass={case[2]}"
            f" states={carrier} image1={image} height={height}"
            f" max_fibre={max_fibre} depth_sum={depth_sum}"
        )
    print(f"ASSERTIONS={ASSERTIONS}")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
