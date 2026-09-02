#!/usr/bin/env python3
"""Deterministic exact controls for P155.

The program enumerates literal finite permutation maps and independently
checks the image, section, fibre, and recurrent-state formulae used in the
paper.  Enumeration is counterexample pressure, not an all-parameter proof,
an ownership search, or a novelty certificate.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
from itertools import permutations
from math import factorial


class Audit:
    def __init__(self) -> None:
        self.assertions = 0
        self.boxes = 0

    def check(self, condition: bool, message: object = "") -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(message or f"assertion {self.assertions} failed")

    def box(self) -> None:
        self.boxes += 1


A = Audit()


def identity(n: int) -> tuple[int, ...]:
    return tuple(range(1, n + 1))


def standardize(values) -> tuple[int, ...]:
    values = tuple(values)
    rank = {value: i + 1 for i, value in enumerate(sorted(values))}
    return tuple(rank[value] for value in values)


def cycle_supports(p: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    seen: set[int] = set()
    blocks: list[tuple[int, ...]] = []
    for start in range(1, len(p) + 1):
        if start in seen:
            continue
        block: list[int] = []
        value = start
        while value not in seen:
            seen.add(value)
            block.append(value)
            value = p[value - 1]
        blocks.append(tuple(sorted(block)))
    blocks.sort(key=lambda block: block[0])
    return tuple(blocks)


def cme(p: tuple[int, ...]) -> tuple[int, ...]:
    return standardize(max(block) for block in cycle_supports(p))


@lru_cache(None)
def tail(p: tuple[int, ...]) -> int:
    q = cme(p)
    if q == p:
        A.check(p == identity(len(p)), ("nonidentity fixed point", p))
        return 0
    return 1 + tail(q)


def right_to_left_minima(sigma: tuple[int, ...]) -> tuple[int, ...]:
    minimum = len(sigma) + 1
    positions: list[int] = []
    for i in range(len(sigma) - 1, -1, -1):
        if sigma[i] < minimum:
            minimum = sigma[i]
            positions.append(i)
    return tuple(reversed(positions))


def minimum_source_rank(sigma: tuple[int, ...]) -> int:
    return 2 * len(sigma) - len(right_to_left_minima(sigma))


@lru_cache(None)
def endpoint_dp(sigma: tuple[int, ...]) -> int:
    """Independent shortest O/K/S schedule dynamic program."""
    m = len(sigma)
    inverse = [0] * m
    for i, value in enumerate(sigma):
        inverse[value - 1] = i

    @lru_cache(None)
    def solve(i: int, j: int) -> int:
        if i == m and j == m:
            return 0
        choices: list[int] = []
        if i < m:
            choices.append(1 + solve(i + 1, j))
        if j < m and inverse[j] < i:
            choices.append(1 + solve(i, j + 1))
        if i < m and j < m and inverse[j] == i:
            choices.append(1 + solve(i + 1, j + 1))
        return min(choices)

    return solve(0, 0)


def minimum_endpoint_events(sigma: tuple[int, ...]):
    """Greedy minimum schedule, identifying exactly the RTL-minimum pairs."""
    m = len(sigma)
    inverse = [0] * m
    for i, value in enumerate(sigma):
        inverse[value - 1] = i
    rtl = set(right_to_left_minima(sigma))
    events: list[tuple[str, int]] = []
    i = j = 0
    while i < m or j < m:
        if i < m and i in rtl and j == sigma[i] - 1:
            events.append(("S", i))
            i += 1
            j += 1
        elif j < m and inverse[j] < i:
            events.append(("K", inverse[j]))
            j += 1
        else:
            A.check(i < m, ("stuck endpoint schedule", sigma, i, j))
            events.append(("O", i))
            i += 1
    return events


def support_section(sigma: tuple[int, ...], n: int):
    """Deterministic ordered supports at every admissible source rank."""
    events = minimum_endpoint_events(sigma)
    A.check(len(events) == minimum_source_rank(sigma))
    extra = n - len(events)
    A.check(extra >= 0, (sigma, n, len(events)))

    # Splitting S into adjacent O,K adds one coordinate without changing any
    # endpoint order.  Every permutation has at least one RTL minimum.
    expanded: list[tuple[str, int]] = []
    for event, block in events:
        if event == "S" and extra:
            expanded.extend((("O", block), ("K", block)))
            extra -= 1
        else:
            expanded.append((event, block))
    events = expanded

    # Once every S has been split, block zero is non-singleton.  Extra
    # coordinates may be inserted in its interior.
    if extra:
        close = next(i for i, item in enumerate(events) if item == ("K", 0))
        events[close:close] = [("I", 0)] * extra

    blocks: list[list[int]] = [[] for _ in sigma]
    for coordinate, (_, block) in enumerate(events, 1):
        blocks[block].append(coordinate)
    answer = tuple(tuple(block) for block in blocks)
    A.check(sum(map(len, answer)) == n)
    A.check(tuple(sorted(min(block) for block in answer)) ==
            tuple(min(block) for block in answer))
    A.check(standardize(max(block) for block in answer) == sigma)
    return answer


def permutation_from_supports(blocks) -> tuple[int, ...]:
    n = sum(map(len, blocks))
    p = [0] * n
    for block in blocks:
        for source, target in zip(block, block[1:] + block[:1]):
            p[source - 1] = target
    return tuple(p)


def rgs_words(n: int):
    """Restricted-growth words, hence set partitions ordered by minima."""
    def visit(prefix: list[int], maximum: int):
        if len(prefix) == n:
            yield tuple(prefix)
            return
        for value in range(maximum + 2):
            prefix.append(value)
            yield from visit(prefix, max(maximum, value))
            prefix.pop()

    yield from visit([0], 0)


def blocks_from_rgs(word: tuple[int, ...]):
    blocks: list[list[int]] = [[] for _ in range(max(word) + 1)]
    for coordinate, block in enumerate(word, 1):
        blocks[block].append(coordinate)
    return tuple(tuple(block) for block in blocks)


def support_fibres(n: int):
    answer: Counter[tuple[int, ...]] = Counter()
    terms = 0
    for word in rgs_words(n):
        blocks = blocks_from_rgs(word)
        sigma = standardize(max(block) for block in blocks)
        weight = 1
        for block in blocks:
            weight *= factorial(len(block) - 1)
        answer[sigma] += weight
        terms += 1
    return answer, terms


def main() -> None:
    literal_images: dict[int, set[tuple[int, ...]]] = {}
    literal_fibres: dict[int, Counter[tuple[int, ...]]] = {}
    maxima: list[int] = []
    censuses: list[dict[int, int]] = []
    image_counts: list[int] = []
    states = 0

    for n in range(1, 11):
        A.box()
        fibres: Counter[tuple[int, ...]] = Counter()
        census: Counter[int] = Counter()
        fixed = 0
        for p in permutations(range(1, n + 1)):
            states += 1
            q = cme(p)
            A.check(sorted(q) == list(range(1, len(q) + 1)))
            A.check(len(q) == len(cycle_supports(p)))
            A.check(len(q) <= n)
            if q == p:
                fixed += 1
                A.check(p == identity(n))
            else:
                A.check(len(q) < n)
            fibres[q] += 1
            census[tail(p)] += 1
        A.check(fixed == 1, ("fixed count", n, fixed))
        A.check(sum(fibres.values()) == factorial(n))
        literal_images[n] = set(fibres)
        if n <= 8:
            literal_fibres[n] = fibres
        maxima.append(max(census))
        censuses.append(dict(sorted(census.items())))
        image_counts.append(len(fibres))

    A.check(maxima == [0, 1, 2, 2, 3, 3, 3, 3, 4, 4], maxima)

    target_checks = 0
    section_checks = 0
    for m in range(1, 9):
        A.box()
        for sigma in permutations(range(1, m + 1)):
            threshold = minimum_source_rank(sigma)
            A.check(endpoint_dp(sigma) == threshold,
                    ("endpoint formula", sigma, endpoint_dp(sigma), threshold))
            A.check(m <= threshold <= 2 * m - 1)
            for n in range(m, 11):
                expected = n >= threshold
                A.check((sigma in literal_images[n]) == expected,
                        ("image", sigma, n, threshold))
                target_checks += 1
                if expected:
                    blocks = support_section(sigma, n)
                    source = permutation_from_supports(blocks)
                    A.check(sorted(source) == list(range(1, n + 1)))
                    A.check(cme(source) == sigma, ("section", sigma, n, source))
                    section_checks += 1

    fibre_checks = 0
    support_terms = 0
    for n in range(1, 9):
        A.box()
        formula, terms = support_fibres(n)
        support_terms += terms
        A.check(formula == literal_fibres[n], ("fibre dictionary", n))
        A.check(sum(formula.values()) == factorial(n))
        for m in range(1, n + 1):
            for sigma in permutations(range(1, m + 1)):
                A.check(formula.get(sigma, 0) == literal_fibres[n].get(sigma, 0))
                fibre_checks += 1

    print("P155_CYCLE_MAXIMUM_EXTRACTION_EXACT_CONTROL")
    print("external_status=HOLD_EXTERNAL")
    print(f"literal_states_through_rank_10={states}")
    print(f"max_tail_ranks_1_to_10={maxima}")
    print(f"tail_censuses={censuses}")
    print(f"image_counts_ranks_1_to_10={image_counts}")
    print(f"image_target_rank_cells={target_checks}")
    print(f"constructive_section_cells={section_checks}")
    print(f"endpoint_dp_targets={sum(factorial(m) for m in range(1, 9))}")
    print(f"every_target_fibre_cells={fibre_checks}")
    print(f"ordered_support_terms={support_terms}")
    print("power_of_two_clock=NOT_CLAIMED")
    print("enumeration_role=COUNTEREXAMPLE_PRESSURE_ONLY")
    print(f"boxes={A.boxes}")
    print(f"assertions={A.assertions}")
    print("status=PASS")


if __name__ == "__main__":
    main()
