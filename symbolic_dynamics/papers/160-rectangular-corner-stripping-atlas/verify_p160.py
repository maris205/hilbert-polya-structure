#!/usr/bin/env python3
"""Paper-local exact falsifier for P160 rectangular-corner stripping."""

from __future__ import annotations

from collections import Counter


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def check(self, condition: bool, label: object) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(label)


A = Audit()
MAX_WEIGHT = 32
TARGET_WEIGHT = 9
TIMES = range(6)
PARAMETERS = ((1, 1), (2, 1), (1, 3), (2, 2), (3, 2))


def partitions(total: int, cap: int | None = None):
    if total == 0:
        yield ()
        return
    cap = min(total, total if cap is None else cap)
    for first in range(cap, 0, -1):
        for tail in partitions(total - first, first):
            yield (first,) + tail


def strip(partition: tuple[int, ...], a: int, b: int, time: int = 1):
    height, width = a * time, b * time
    return tuple(value - width for value in partition[height:] if value > width)


def repeated_strip(partition: tuple[int, ...], a: int, b: int, time: int):
    for _ in range(time):
        partition = strip(partition, a, b)
    return partition


def conjugate(partition: tuple[int, ...]):
    if not partition:
        return ()
    return tuple(sum(value >= column for value in partition) for column in range(1, partition[0] + 1))


def inv_pochhammer(order: int, degree: int):
    coefficients = [1] + [0] * degree
    for part in range(1, order + 1):
        for index in range(part, degree + 1):
            coefficients[index] += coefficients[index - part]
    return coefficients


def convolution(left, right, degree: int):
    coefficients = [0] * (degree + 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            if i + j <= degree:
                coefficients[i + j] += x * y
    return coefficients


def empty_series(height: int, width: int, degree: int):
    coefficients = [0] * (degree + 1)
    top = inv_pochhammer(height, degree)
    for boundary in range(width + 1):
        bottom = inv_pochhammer(boundary, degree)
        shift = boundary * (height + 1)
        for i, x in enumerate(top):
            for j, y in enumerate(bottom):
                if shift + i + j <= degree:
                    coefficients[shift + i + j] += x * y
    return coefficients


def minimum_source(target: tuple[int, ...], height: int, width: int):
    return sum(target) + height * (target[0] + width) + width * len(target)


def entry_time(partition: tuple[int, ...], a: int, b: int):
    time = 0
    while partition:
        partition = strip(partition, a, b)
        time += 1
    return time


def sharp_height(cap: int, a: int, b: int):
    time = 0
    while (a * time + 1) * (b * time + 1) <= cap:
        time += 1
    return time


def main() -> None:
    by_weight = {weight: tuple(partitions(weight)) for weight in range(MAX_WEIGHT + 1)}
    states = tuple(partition for weight in range(MAX_WEIGHT + 1) for partition in by_weight[weight])
    targets = tuple(partition for weight in range(TARGET_WEIGHT + 1) for partition in by_weight[weight])

    for a, b in PARAMETERS:
        clocks = {partition: entry_time(partition, a, b) for partition in states}
        for partition, clock in clocks.items():
            A.check(strip(partition, a, b, clock) == (), ("clock terminal", a, b, partition))
            if partition:
                A.check(strip(partition, a, b, clock - 1) != (), ("clock sharp", a, b, partition))
            A.check(
                strip(conjugate(partition), b, a) == conjugate(strip(partition, a, b)),
                ("conjugation", a, b, partition),
            )

        for cap in range(MAX_WEIGHT + 1):
            observed = max(clocks[partition] for weight in range(cap + 1) for partition in by_weight[weight])
            A.check(observed == sharp_height(cap, a, b), ("height", a, b, cap, observed))

        cell, row, column = (1,), (2,), (1, 1)
        m_cell = minimum_source(cell, a, b)
        m_row = minimum_source(row, a, b)
        m_column = minimum_source(column, a, b)
        A.check(m_cell == (a + 1) * (b + 1), ("cell threshold", a, b))
        A.check(m_row - m_cell - 1 == a, ("recover a", a, b))
        A.check(m_column - m_cell - 1 == b, ("recover b", a, b))

        for time in TIMES:
            height, width = a * time, b * time
            fibres = Counter((strip(partition, a, b, time), sum(partition)) for partition in states)
            denominator = convolution(
                inv_pochhammer(height, MAX_WEIGHT),
                inv_pochhammer(width, MAX_WEIGHT),
                MAX_WEIGHT,
            )
            empty = empty_series(height, width, MAX_WEIGHT)

            for partition in states:
                A.check(
                    strip(partition, a, b, time) == repeated_strip(partition, a, b, time),
                    ("iterate", a, b, time, partition),
                )
                A.check(sum(strip(partition, a, b, time)) <= sum(partition), ("closure", partition))

            for source_weight in range(MAX_WEIGHT + 1):
                A.check(fibres[((), source_weight)] == empty[source_weight], ("empty", a, b, time, source_weight))
                A.check(
                    sum(count for (target, weight), count in fibres.items() if weight == source_weight)
                    == len(by_weight[source_weight]),
                    ("mass", a, b, time, source_weight),
                )

            for target in targets:
                if not target:
                    continue
                minimum = minimum_source(target, height, width)
                for source_weight in range(MAX_WEIGHT + 1):
                    expected = denominator[source_weight - minimum] if source_weight >= minimum else 0
                    A.check(
                        fibres[(target, source_weight)] == expected,
                        ("target fibre", a, b, time, target, source_weight),
                    )
                    if time >= 1:
                        A.check(
                            (fibres[(target, source_weight)] > 0) == (source_weight >= minimum),
                            ("image threshold", a, b, time, target, source_weight),
                        )

    print(f"RCS VERIFY parameters={PARAMETERS}")
    print(f"EXHAUSTIVE source_weight<=${MAX_WEIGHT} target_weight<=${TARGET_WEIGHT} times=0..5".replace("$", ""))
    print(f"ASSERTIONS {A.assertions}")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
