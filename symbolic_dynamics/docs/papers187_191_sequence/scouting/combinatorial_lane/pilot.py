#!/usr/bin/env python3
"""Deterministic exact breadth pilot for the P187--P191 combinatorial lane.

Standard library only.  The program enumerates complete finite carriers,
builds every transition, decomposes every functional graph, and then applies
candidate-specific falsifiers.  Finite output is evidence against conjectures,
not a proof or an ownership/novelty certificate.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, permutations, product
from math import comb, factorial, gcd
from typing import Callable, Hashable, Iterable


State = Hashable


class Audit:
    def __init__(self) -> None:
        self.assertions = 0
        self.transitions = 0
        self.digest = sha256()
        self.signals: list[str] = []

    def check(self, condition: bool, message: object) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(message)

    def bind_transition(self, candidate: str, parameter: int, source: State, target: State) -> None:
        self.transitions += 1
        self.digest.update(
            f"{candidate}|{parameter}|{source!r}->{target!r}\n".encode("utf-8")
        )

    def signal(self, candidate: str, name: str) -> None:
        token = f"{candidate}:{name}"
        self.check(token not in self.signals, ("duplicate signal", token))
        self.signals.append(token)


AUDIT = Audit()


@dataclass
class Box:
    states: tuple[State, ...]
    nxt: dict[State, State]
    tails: dict[State, int]
    periods: dict[State, int]
    fibres: Counter[State]

    @property
    def image(self) -> int:
        return len(self.fibres)

    @property
    def fixed(self) -> int:
        return sum(self.nxt[x] == x for x in self.states)

    @property
    def recurrent(self) -> int:
        return sum(self.tails[x] == 0 for x in self.states)

    @property
    def max_tail(self) -> int:
        return max(self.tails.values(), default=0)


def advance(nxt: dict[State, State], state: State, steps: int) -> State:
    for _ in range(steps):
        state = nxt[state]
    return state


def exact_box(
    candidate: str,
    parameter: int,
    states: Iterable[State],
    update: Callable[[State], State],
) -> Box:
    states = tuple(states)
    state_set = set(states)
    AUDIT.check(len(state_set) == len(states), (candidate, parameter, "duplicate state"))
    nxt: dict[State, State] = {}
    for state in states:
        target = update(state)
        AUDIT.check(target in state_set, (candidate, parameter, "closure", state, target))
        nxt[state] = target
        AUDIT.bind_transition(candidate, parameter, state, target)

    tails: dict[State, int] = {}
    periods_: dict[State, int] = {}
    for start in states:
        if start in tails:
            continue
        path: list[State] = []
        position: dict[State, int] = {}
        current = start
        while current not in tails and current not in position:
            position[current] = len(path)
            path.append(current)
            current = nxt[current]
        if current in position:
            cycle_start = position[current]
            cycle_length = len(path) - cycle_start
            for state in path[cycle_start:]:
                tails[state] = 0
                periods_[state] = cycle_length
            for state in reversed(path[:cycle_start]):
                tails[state] = tails[nxt[state]] + 1
                periods_[state] = cycle_length
        else:
            for state in reversed(path):
                tails[state] = tails[nxt[state]] + 1
                periods_[state] = periods_[nxt[state]]

    fibres = Counter(nxt.values())
    AUDIT.check(sum(fibres.values()) == len(states), (candidate, parameter, "fibre mass"))
    AUDIT.check(len(fibres) == len(set(nxt.values())), (candidate, parameter, "image"))
    for state in states:
        AUDIT.check(state in tails and state in periods_, (candidate, parameter, "classification"))
        recurrent = advance(nxt, state, tails[state])
        AUDIT.check(tails[recurrent] == 0, (candidate, parameter, "tail endpoint"))
        AUDIT.check(
            advance(nxt, recurrent, periods_[state]) == recurrent,
            (candidate, parameter, "period endpoint"),
        )
        AUDIT.check(periods_[state] >= 1, (candidate, parameter, "positive period"))
    return Box(states, nxt, tails, periods_, fibres)


def summary(candidate: str, parameter_name: str, parameter: int, box: Box) -> str:
    period_set = sorted({box.periods[x] for x in box.states if box.tails[x] == 0})
    max_fibre = max(box.fibres.values(), default=0)
    min_fibre = min(box.fibres.values(), default=0)
    deepest = sum(value == box.max_tail for value in box.tails.values())
    fibre_hist_digest = sha256(
        repr(sorted(Counter(box.fibres.values()).items())).encode("utf-8")
    ).hexdigest()[:16]
    return (
        f"{candidate} {parameter_name}={parameter} states={len(box.states)} "
        f"image={box.image} fixed={box.fixed} recurrent={box.recurrent} "
        f"periods={','.join(map(str, period_set))} max_tail={box.max_tail} "
        f"deepest={deepest} positive_fibre_min={min_fibre} "
        f"fibre_max={max_fibre} fibre_value_count={len(set(box.fibres.values()))} "
        f"fibre_hist_digest={fibre_hist_digest}"
    )


# ---------------------------------------------------------------------------
# Permutations


def cycles_of(pi: tuple[int, ...]) -> list[list[int]]:
    seen: set[int] = set()
    answer: list[list[int]] = []
    for seed in range(len(pi)):
        if seed in seen:
            continue
        cycle = []
        current = seed
        while current not in seen:
            seen.add(current)
            cycle.append(current)
            current = pi[current]
        answer.append(cycle)
    return answer


def anchored_cycle_tail_rotation(pi: tuple[int, ...]) -> tuple[int, ...]:
    out = list(range(len(pi)))
    for support in cycles_of(pi):
        anchor = min(support)
        orbit = [anchor]
        while pi[orbit[-1]] != anchor:
            orbit.append(pi[orbit[-1]])
        if len(orbit) >= 3:
            orbit = [orbit[0], *orbit[2:], orbit[1]]
        for left, right in zip(orbit, orbit[1:] + orbit[:1]):
            out[left] = right
    return tuple(out)


def minimum_cycle_powering(pi: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * len(pi)
    for support in cycles_of(pi):
        exponent = 1 + min(support)
        for value in support:
            target = value
            for _ in range(exponent):
                target = pi[target]
            out[value] = target
    return tuple(out)


def interior_peak_fall(pi: tuple[int, ...]) -> tuple[int, ...]:
    out = list(pi)
    peaks = [
        index for index in range(1, len(pi) - 1)
        if pi[index - 1] < pi[index] > pi[index + 1]
    ]
    for index in peaks:
        out[index], out[index + 1] = out[index + 1], out[index]
    return tuple(out)


def displacement_rank_assignment(pi: tuple[int, ...]) -> tuple[int, ...]:
    """Rank positions by (absolute displacement, old value)."""
    keys = [(abs(value - index), value, index) for index, value in enumerate(pi)]
    ordered = sorted(keys)
    rank = {index: position for position, (_, _, index) in enumerate(ordered)}
    return tuple(rank[index] for index in range(len(pi)))


# ---------------------------------------------------------------------------
# Words


def positional_multiplicity_echo(word: tuple[int, ...]) -> tuple[int, ...]:
    counts = Counter(word)
    return tuple(counts[value] - 1 for value in word)


def run_length_feedback(word: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * len(word)
    start = 0
    while start < len(word):
        end = start + 1
        while end < len(word) and word[end] == word[start]:
            end += 1
        for index in range(start, end):
            out[index] = end - start - 1
        start = end
    return tuple(out)


def interval_hull_coverage(word: tuple[int, ...]) -> tuple[int, ...]:
    first: dict[int, int] = {}
    last: dict[int, int] = {}
    for index, value in enumerate(word):
        first.setdefault(value, index)
        last[value] = index
    return tuple(
        sum(first[value] <= index <= last[value] for value in first) - 1
        for index in range(len(word))
    )


def prefix_bigram_diversity(word: tuple[int, ...]) -> tuple[int, ...]:
    out = []
    seen: set[tuple[int, int]] = set()
    for index in range(len(word)):
        if index >= 2:
            seen.add((word[index - 2], word[index - 1]))
        out.append(len(seen))
    return tuple(out)


def interval_span_echo(word: tuple[int, ...]) -> tuple[int, ...]:
    first: dict[int, int] = {}
    last: dict[int, int] = {}
    for index, value in enumerate(word):
        first.setdefault(value, index)
        last[value] = index
    return tuple(last[value] - first[value] for value in word)


def multiplicity_image_fibre(target: tuple[int, ...]) -> int:
    n = len(target)
    counts = Counter(target)
    blocks = 0
    positional_partitions = 1
    for value, count in counts.items():
        block_size = value + 1
        if count % block_size:
            return 0
        multiplicity = count // block_size
        blocks += multiplicity
        positional_partitions *= factorial(count) // (
            factorial(block_size) ** multiplicity * factorial(multiplicity)
        )
    falling = factorial(n) // factorial(n - blocks)
    return falling * positional_partitions


def multiplicity_clock(word: tuple[int, ...]) -> int:
    if positional_multiplicity_echo(word) == word:
        return 0
    sizes = sorted(Counter(word).values())
    merging_rounds = 0
    while len(sizes) != len(set(sizes)):
        counts = Counter(sizes)
        sizes = sorted(size * multiplicity for size, multiplicity in counts.items())
        merging_rounds += 1
    return 1 + merging_rounds


def validate_pme(n: int, box: Box) -> None:
    fixed_formula = 0
    for mask in range(1 << n):
        sizes = [size for size in range(1, n + 1) if mask >> (size - 1) & 1]
        if sum(sizes) == n:
            term = factorial(n)
            for size in sizes:
                term //= factorial(size)
            fixed_formula += term
    AUDIT.check(box.fixed == fixed_formula, ("PME", n, "fixed formula"))
    for state in box.states:
        AUDIT.check(box.tails[state] == multiplicity_clock(state), ("PME", n, "clock", state))
        AUDIT.check(
            box.fibres.get(state, 0) == multiplicity_image_fibre(state),
            ("PME", n, "every-target fibre", state),
        )


# ---------------------------------------------------------------------------
# Set partitions


Partition = tuple[tuple[int, ...], ...]


def canonical_partition(blocks: Iterable[Iterable[int]]) -> Partition:
    cleaned = [tuple(sorted(block)) for block in blocks if tuple(block)]
    return tuple(sorted(cleaned, key=lambda block: block[0]))


@lru_cache(maxsize=None)
def set_partitions(n: int) -> tuple[Partition, ...]:
    if n == 0:
        return ((),)
    result: set[Partition] = set()
    for partition in set_partitions(n - 1):
        for index in range(len(partition)):
            blocks = [list(block) for block in partition]
            blocks[index].append(n - 1)
            result.add(canonical_partition(blocks))
        result.add(canonical_partition([*partition, (n - 1,)]))
    return tuple(sorted(result))


def parallel_block_minimum_peeling(partition: Partition) -> Partition:
    blocks: list[tuple[int, ...]] = []
    for block in partition:
        if len(block) == 1:
            blocks.append(block)
        else:
            blocks.append((block[0],))
            blocks.append(block[1:])
    return canonical_partition(blocks)


def cyclic_shift_meet(partition: Partition) -> Partition:
    n = sum(map(len, partition))
    owner = {}
    for block_index, block in enumerate(partition):
        for value in block:
            owner[value] = block_index
    groups: dict[tuple[int, int], list[int]] = defaultdict(list)
    for value in range(n):
        groups[(owner[value], owner[(value - 1) % n])].append(value)
    return canonical_partition(groups.values())


def cyclic_shift_meet_formula(partition: Partition, time: int) -> Partition:
    n = sum(map(len, partition))
    owner = {}
    for block_index, block in enumerate(partition):
        for value in block:
            owner[value] = block_index
    groups: dict[tuple[int, ...], list[int]] = defaultdict(list)
    for value in range(n):
        groups[tuple(owner[(value - shift) % n] for shift in range(time + 1))].append(value)
    return canonical_partition(groups.values())


def minima_reservoir_collection(partition: Partition) -> Partition:
    minima = tuple(block[0] for block in partition)
    residuals = [block[1:] for block in partition if len(block) >= 2]
    return canonical_partition([minima, *residuals])


def crossing_component_merge(partition: Partition) -> Partition:
    count = len(partition)
    parent = list(range(count))

    def find(index: int) -> int:
        while parent[index] != index:
            parent[index] = parent[parent[index]]
            index = parent[index]
        return index

    def union(left: int, right: int) -> None:
        left, right = find(left), find(right)
        if left != right:
            parent[right] = left

    for i, j in combinations(range(count), 2):
        a, b = partition[i][0], partition[i][-1]
        c, d = partition[j][0], partition[j][-1]
        if (a < c < b < d) or (c < a < d < b):
            union(i, j)
    groups: dict[int, list[int]] = defaultdict(list)
    for index, block in enumerate(partition):
        groups[find(index)].extend(block)
    return canonical_partition(groups.values())


def maximum_gap_split_block(block: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    if len(block) <= 1:
        return (block,)
    gaps = tuple(block[index + 1] - block[index] for index in range(len(block) - 1))
    cut = gaps.index(max(gaps)) + 1  # the leftmost maximum gap
    return (block[:cut], block[cut:])


def maximum_gap_block_fission(partition: Partition) -> Partition:
    return canonical_partition(
        piece for block in partition for piece in maximum_gap_split_block(block)
    )


@lru_cache(maxsize=None)
def maximum_gap_height(block: tuple[int, ...]) -> int:
    if len(block) <= 1:
        return 0
    left, right = maximum_gap_split_block(block)
    return 1 + max(maximum_gap_height(left), maximum_gap_height(right))


@lru_cache(maxsize=None)
def maximum_gap_level(block: tuple[int, ...], time: int) -> tuple[tuple[int, ...], ...]:
    if time == 0 or len(block) <= 1:
        return (block,)
    left, right = maximum_gap_split_block(block)
    return maximum_gap_level(left, time - 1) + maximum_gap_level(right, time - 1)


def maximum_gap_formula(partition: Partition, time: int) -> Partition:
    return canonical_partition(
        piece for block in partition for piece in maximum_gap_level(block, time)
    )


def internal_maximum_gap(block: tuple[int, ...]) -> int:
    return max(
        (block[index + 1] - block[index] for index in range(len(block) - 1)),
        default=0,
    )


def maximum_gap_compatible(left: tuple[int, ...], right: tuple[int, ...]) -> bool:
    if max(left) >= min(right):
        return False
    boundary = min(right) - max(left)
    # A left internal tie would precede the boundary; a right tie follows it.
    return internal_maximum_gap(left) < boundary and internal_maximum_gap(right) <= boundary


def maximum_gap_fibre_formula(target: Partition) -> int:
    count = len(target)

    @lru_cache(maxsize=None)
    def visit(mask: int) -> int:
        if mask == 0:
            return 1
        first = (mask & -mask).bit_length() - 1
        remaining = mask ^ (1 << first)
        answer = visit(remaining) if len(target[first]) == 1 else 0
        for second in range(first + 1, count):
            if not (remaining >> second) & 1:
                continue
            a, b = target[first], target[second]
            compatible = maximum_gap_compatible(a, b) or maximum_gap_compatible(b, a)
            if compatible:
                answer += visit(remaining ^ (1 << second))
        return answer

    return visit((1 << count) - 1)


def validate_mgbf(n: int, box: Box) -> None:
    for state in box.states:
        height = max((maximum_gap_height(block) for block in state), default=0)
        AUDIT.check(box.tails[state] == height, ("MGBF", n, "tree clock", state))
        AUDIT.check(box.periods[state] == 1, ("MGBF", n, "fixed recurrence", state))
        for time in range(n + 1):
            AUDIT.check(
                advance(box.nxt, state, time) == maximum_gap_formula(state, time),
                ("MGBF", n, "tree level", time, state),
            )
        AUDIT.check(
            box.fibres.get(state, 0) == maximum_gap_fibre_formula(state),
            ("MGBF", n, "every-target matching fibre", state),
        )
    AUDIT.check(box.fixed == 1, ("MGBF", n, "unique discrete fixed point"))
    AUDIT.check(box.max_tail == n - 1, ("MGBF", n, "sharp global clock"))
    AUDIT.check(
        sum(value == box.max_tail for value in box.tails.values()) == 1,
        ("MGBF", n, "unique deepest indiscrete partition"),
    )


@lru_cache(maxsize=None)
def restricted_bell(size: int, maximum_block: int) -> int:
    if size == 0:
        return 1
    return sum(
        comb(size - 1, block_size - 1)
        * restricted_bell(size - block_size, maximum_block)
        for block_size in range(1, min(size, maximum_block) + 1)
    )


def peeling_attachment_count(
    singleton_labels: tuple[int, ...],
    residual_blocks: tuple[tuple[int, ...], ...],
    time: int,
) -> int:
    ordered = tuple(sorted(residual_blocks, key=lambda block: block[0]))

    @lru_cache(maxsize=None)
    def visit(index: int, available: tuple[int, ...]) -> int:
        if index == len(ordered):
            return restricted_bell(len(available), time + 1)
        eligible = tuple(value for value in available if value < ordered[index][0])
        if len(eligible) < time:
            return 0
        answer = 0
        for chosen in combinations(eligible, time):
            chosen_set = set(chosen)
            answer += visit(index + 1, tuple(x for x in available if x not in chosen_set))
        return answer

    return visit(0, singleton_labels)


def peeling_fibre_formula(target: Partition, time: int) -> int:
    singletons = tuple(block[0] for block in target if len(block) == 1)
    residuals = tuple(block for block in target if len(block) >= 2)
    return peeling_attachment_count(singletons, residuals, time)


def validate_pbmp(n: int, box: Box) -> None:
    for state in box.states:
        expected_tail = max((len(block) - 1 for block in state), default=0)
        AUDIT.check(box.tails[state] == expected_tail, ("PBMP", n, "clock", state))
    current = {state: state for state in box.states}
    for time in range(n):
        actual = Counter(current.values())
        for target in box.states:
            AUDIT.check(
                actual.get(target, 0) == peeling_fibre_formula(target, time),
                ("PBMP", n, "time fibre", time, target),
            )
        current = {state: box.nxt[current[state]] for state in box.states}


def validate_csm(n: int, box: Box) -> None:
    for state in box.states:
        current = state
        for time in range(n + 1):
            AUDIT.check(
                current == cyclic_shift_meet_formula(state, time),
                ("CSM", n, "iterate", time, state),
            )
            current = box.nxt[current]
        AUDIT.check(box.periods[state] == 1, ("CSM", n, "fixed recurrence"))


# ---------------------------------------------------------------------------
# Posets, stored as strict-relation bitmasks on ordered pairs.


@lru_cache(maxsize=None)
def labelled_posets(n: int) -> tuple[int, ...]:
    pairs = tuple(combinations(range(n), 2))
    states = []
    for code in range(3 ** len(pairs)):
        rows = [0] * n
        work = code
        for left, right in pairs:
            choice = work % 3
            work //= 3
            if choice == 1:
                rows[left] |= 1 << right
            elif choice == 2:
                rows[right] |= 1 << left
        transitive = True
        for left in range(n):
            for middle in range(n):
                if rows[left] >> middle & 1 and rows[middle] & ~rows[left]:
                    transitive = False
                    break
            if not transitive:
                break
        if transitive:
            mask = sum(rows[left] << (left * n) for left in range(n))
            states.append(mask)
    return tuple(states)


def poset_rows(mask: int, n: int) -> list[int]:
    row_mask = (1 << n) - 1
    return [(mask >> (left * n)) & row_mask for left in range(n)]


def rows_mask(rows: list[int], n: int) -> int:
    return sum(rows[left] << (left * n) for left in range(n))


def relational_power_erosion(mask: int, n: int) -> int:
    rows = poset_rows(mask, n)
    out = [0] * n
    for left in range(n):
        for middle in range(n):
            if rows[left] >> middle & 1:
                out[left] |= rows[middle]
    return rows_mask(out, n)


def cyclic_shift_relation_intersection(mask: int, n: int) -> int:
    rows = poset_rows(mask, n)
    out = [0] * n
    for left in range(n):
        for right in range(n):
            if (rows[left] >> right & 1) and (rows[(left + 1) % n] >> ((right + 1) % n) & 1):
                out[left] |= 1 << right
    return rows_mask(out, n)


def minimal_layer_isolation(mask: int, n: int) -> int:
    rows = poset_rows(mask, n)
    incoming = [0] * n
    for left in range(n):
        for right in range(n):
            if rows[left] >> right & 1:
                incoming[right] |= 1 << left
    out = [0 if incoming[left] == 0 else rows[left] for left in range(n)]
    return rows_mask(out, n)


def poset_down_heights(mask: int, n: int) -> tuple[int, ...]:
    rows = poset_rows(mask, n)

    @lru_cache(maxsize=None)
    def down_height(vertex: int) -> int:
        predecessors = [left for left in range(n) if rows[left] >> vertex & 1]
        return max((1 + down_height(left) for left in predecessors), default=0)

    return tuple(down_height(vertex) for vertex in range(n))


def minimal_layer_formula(mask: int, n: int, time: int) -> int:
    rows = poset_rows(mask, n)
    heights = poset_down_heights(mask, n)
    return rows_mask(
        [rows[left] if heights[left] >= time else 0 for left in range(n)], n
    )


def validate_mli(n: int, box: Box) -> None:
    for state in box.states:
        AUDIT.check(
            box.tails[state] == poset_height_edges(state, n),
            ("MLI", n, "height clock", state),
        )
        AUDIT.check(box.periods[state] == 1, ("MLI", n, "fixed recurrence", state))
        for time in range(n + 1):
            AUDIT.check(
                advance(box.nxt, state, time) == minimal_layer_formula(state, n, time),
                ("MLI", n, "layer formula", time, state),
            )
    AUDIT.check(box.fixed == 1, ("MLI", n, "unique antichain"))
    AUDIT.check(box.max_tail == n - 1, ("MLI", n, "sharp height"))
    AUDIT.check(
        sum(value == box.max_tail for value in box.tails.values()) == factorial(n),
        ("MLI", n, "labelled total orders are deepest"),
    )


def poset_height_edges(mask: int, n: int) -> int:
    rows = poset_rows(mask, n)

    @lru_cache(maxsize=None)
    def height(left: int) -> int:
        successors = [right for right in range(n) if rows[left] >> right & 1]
        return max((1 + height(right) for right in successors), default=0)

    return max((height(left) for left in range(n)), default=0)


def cyclic_relation_run(mask: int, n: int) -> int:
    rows = poset_rows(mask, n)
    best = 0
    for difference in range(1, n):
        bits = [
            (rows[left] >> ((left + difference) % n)) & 1
            for left in range(n)
        ]
        AUDIT.check(not all(bits), ("CSR", n, "cyclic order contradiction", difference))
        run = 0
        for bit in bits + bits:
            run = run + 1 if bit else 0
            best = max(best, min(run, n))
    return best


def cyclic_relation_formula(mask: int, n: int, time: int) -> int:
    rows = poset_rows(mask, n)
    out = [0] * n
    for left in range(n):
        for right in range(n):
            if all(
                rows[(left + shift) % n] >> ((right + shift) % n) & 1
                for shift in range(time + 1)
            ):
                out[left] |= 1 << right
    return rows_mask(out, n)


def validate_rpe(n: int, box: Box) -> None:
    for state in box.states:
        expected = poset_height_edges(state, n).bit_length()
        AUDIT.check(box.tails[state] == expected, ("RPE", n, "clock", state))
        AUDIT.check(box.periods[state] == 1, ("RPE", n, "fixed recurrence", state))
    AUDIT.check(box.fixed == 1, ("RPE", n, "unique antichain"))


def validate_csr(n: int, box: Box) -> None:
    for state in box.states:
        AUDIT.check(box.tails[state] == cyclic_relation_run(state, n), ("CSR", n, "clock", state))
        current = state
        for time in range(n + 1):
            AUDIT.check(current == cyclic_relation_formula(state, n, time), ("CSR", n, time, state))
            current = box.nxt[current]
        AUDIT.check(box.periods[state] == 1, ("CSR", n, "fixed recurrence"))
    AUDIT.check(box.fixed == 1, ("CSR", n, "unique antichain"))


# ---------------------------------------------------------------------------
# Compositions


def compositions(total: int) -> tuple[tuple[int, ...], ...]:
    answer = []
    for cuts in range(1 << max(total - 1, 0)):
        parts = []
        previous = 0
        for position in range(1, total):
            if cuts >> (position - 1) & 1:
                parts.append(position - previous)
                previous = position
        parts.append(total - previous)
        answer.append(tuple(parts))
    return tuple(answer)


@lru_cache(maxsize=None)
def integer_partitions(total: int, ceiling: int = -1) -> tuple[tuple[int, ...], ...]:
    if total == 0:
        return ((),)
    if ceiling < 0:
        ceiling = total
    answer = []
    for first in range(min(total, ceiling), 0, -1):
        for suffix in integer_partitions(total - first, first):
            answer.append((first, *suffix))
    return tuple(answer)


def top_row_reservoir(partition: tuple[int, ...]) -> tuple[int, ...]:
    if len(partition) == 1:
        return partition
    return (
        partition[0] + len(partition) - 1,
        *(value - 1 for value in partition[1:] if value >= 2),
    )


def top_row_formula(partition: tuple[int, ...], time: int) -> tuple[int, ...]:
    return (
        partition[0] + sum(min(time, value) for value in partition[1:]),
        *(value - time for value in partition[1:] if value > time),
    )


def top_row_fibre_formula(target: tuple[int, ...]) -> int:
    length = len(target)
    lower_bound = target[1] + 1 if length >= 2 else 1
    return max(0, target[0] - length + 2 - lower_bound)


def validate_trr(total: int, box: Box) -> None:
    for state in box.states:
        expected_tail = state[1] if len(state) >= 2 else 0
        AUDIT.check(box.tails[state] == expected_tail, ("TRR", total, "second-row clock", state))
        AUDIT.check(box.periods[state] == 1, ("TRR", total, "fixed recurrence", state))
        for time in range(total + 1):
            AUDIT.check(
                advance(box.nxt, state, time) == top_row_formula(state, time),
                ("TRR", total, "all-time formula", time, state),
            )
        AUDIT.check(
            box.fibres.get(state, 0) == top_row_fibre_formula(state),
            ("TRR", total, "every-target fibre", state),
        )
    AUDIT.check(box.fixed == 1, ("TRR", total, "unique one-row fixed point"))
    AUDIT.check(box.max_tail == total // 2, ("TRR", total, "sharp clock"))
    expected_deepest = 1 if total % 2 == 0 else (1 if total == 1 else 2)
    AUDIT.check(
        sum(value == box.max_tail for value in box.tails.values()) == expected_deepest,
        ("TRR", total, "strict extremizers"),
    )


def prefix_divisibility_cut_filter(parts: tuple[int, ...]) -> tuple[int, ...]:
    total = sum(parts)
    retained = []
    prefix = 0
    for value in parts[:-1]:
        prefix += value
        if prefix % value == 0:
            retained.append(prefix)
    retained.append(total)
    previous = 0
    out = []
    for cut in retained:
        out.append(cut - previous)
        previous = cut
    return tuple(out)


def prefix_divisibility_fixed(parts: tuple[int, ...]) -> bool:
    prefix = 0
    for value in parts[:-1]:
        prefix += value
        if prefix % value:
            return False
    return True


def prefix_divisibility_fibre_formula(target: tuple[int, ...]) -> int:
    total = sum(target)
    target_cuts = set()
    prefix = 0
    for value in target[:-1]:
        prefix += value
        target_cuts.add(prefix)
    dp = [0] * (total + 1)
    dp[0] = 1
    for endpoint in range(1, total + 1):
        for previous in range(endpoint):
            if dp[previous] == 0:
                continue
            if any(previous < cut < endpoint for cut in target_cuts):
                continue
            if endpoint < total:
                retained = endpoint % (endpoint - previous) == 0
                if retained != (endpoint in target_cuts):
                    continue
            dp[endpoint] += dp[previous]
    return dp[total]


def prefix_divisibility_fixed_count(total: int) -> int:
    paths = [0] * total
    paths[0] = 1
    for endpoint in range(1, total):
        paths[endpoint] = sum(
            paths[previous]
            for previous in range(endpoint)
            if endpoint % (endpoint - previous) == 0
        )
    return sum(paths)


def validate_pdcf(total: int, box: Box) -> None:
    fibre_mass = 0
    for state in box.states:
        AUDIT.check(
            (box.nxt[state] == state) == prefix_divisibility_fixed(state),
            ("PDCF", total, "fixed characterization", state),
        )
        AUDIT.check(box.periods[state] == 1, ("PDCF", total, "fixed recurrence", state))
        formula = prefix_divisibility_fibre_formula(state)
        AUDIT.check(
            box.fibres.get(state, 0) == formula,
            ("PDCF", total, "every-target path fibre", state),
        )
        fibre_mass += formula
    AUDIT.check(fibre_mass == len(box.states), ("PDCF", total, "DP mass conservation"))
    AUDIT.check(
        box.fixed == prefix_divisibility_fixed_count(total),
        ("PDCF", total, "fixed path recurrence"),
    )
    sharp = max(0, total - 3)
    AUDIT.check(box.max_tail == sharp, ("PDCF", total, "sharp global clock"))
    if total >= 4:
        witness = (1, 2, *(1 for _ in range(total - 3)))
        AUDIT.check(box.tails[witness] == total - 3, ("PDCF", total, "deepest witness"))
        for time in range(total - 2):
            expected = (1, 2 + time, *(1 for _ in range(total - 3 - time)))
            AUDIT.check(
                advance(box.nxt, witness, time) == expected,
                ("PDCF", total, "witness trajectory", time),
            )
        AUDIT.check(
            sum(value == box.max_tail for value in box.tails.values()) == 1,
            ("PDCF", total, "unique deepest state"),
        )


def equal_value_aggregation(parts: tuple[int, ...]) -> tuple[int, ...]:
    counts = Counter(parts)
    seen: set[int] = set()
    out = []
    for value in parts:
        if value not in seen:
            seen.add(value)
            out.append(value * counts[value])
    return tuple(out)


def even_halving_split(parts: tuple[int, ...]) -> tuple[int, ...]:
    out = []
    for value in parts:
        if value % 2:
            out.append(value)
        else:
            out.extend((value // 2, value // 2))
    return tuple(out)


@lru_cache(maxsize=None)
def divisors(value: int) -> tuple[int, ...]:
    return tuple(divisor for divisor in range(1, value + 1) if value % divisor == 0)


@lru_cache(maxsize=None)
def first_occurrence_words(multiplicities: tuple[int, ...], introduced: int = 0) -> int:
    if not any(multiplicities):
        return 1
    answer = 0
    for index in range(introduced):
        if multiplicities[index]:
            remaining = list(multiplicities)
            remaining[index] -= 1
            answer += first_occurrence_words(tuple(remaining), introduced)
    if introduced < len(multiplicities) and multiplicities[introduced]:
        remaining = list(multiplicities)
        remaining[introduced] -= 1
        answer += first_occurrence_words(tuple(remaining), introduced + 1)
    return answer


def aggregation_fibre_formula(target: tuple[int, ...]) -> int:
    answer = 0
    choices = [divisors(value) for value in target]
    for multiplicities in product(*choices):
        source_values = tuple(
            target[index] // multiplicities[index] for index in range(len(target))
        )
        if len(set(source_values)) != len(source_values):
            continue
        answer += first_occurrence_words(tuple(multiplicities), 0)
    return answer


def validate_eva(total: int, box: Box) -> None:
    for state in box.states:
        fixed = len(set(state)) == len(state)
        AUDIT.check((box.nxt[state] == state) == fixed, ("EVA", total, "fixed", state))
        AUDIT.check(box.periods[state] == 1, ("EVA", total, "fixed recurrence", state))
        AUDIT.check(box.tails[state] <= len(state) - 1, ("EVA", total, "length clock", state))
        AUDIT.check(
            box.fibres.get(state, 0) == aggregation_fibre_formula(state),
            ("EVA", total, "every-target fibre", state),
        )


def valuation_two(value: int) -> int:
    answer = 0
    while value % 2 == 0:
        value //= 2
        answer += 1
    return answer


def halving_fibre_formula(target: tuple[int, ...], time: int) -> int:
    length = len(target)
    dp = [0] * (length + 1)
    dp[length] = 1
    for index in range(length - 1, -1, -1):
        value = target[index]
        for exponent in range(time + 1):
            block_length = 1 << exponent
            if index + block_length > length:
                continue
            if any(target[j] != value for j in range(index, index + block_length)):
                continue
            if exponent < time and value % 2 == 0:
                continue
            dp[index] += dp[index + block_length]
    return dp[0]


def validate_ehs(total: int, box: Box) -> None:
    for state in box.states:
        expected_tail = max(map(valuation_two, state), default=0)
        AUDIT.check(box.tails[state] == expected_tail, ("EHS", total, "valuation clock", state))
        AUDIT.check(box.periods[state] == 1, ("EHS", total, "fixed recurrence", state))
    current = {state: state for state in box.states}
    for time in range(total.bit_length() + 1):
        actual = Counter(current.values())
        for target in box.states:
            AUDIT.check(
                actual.get(target, 0) == halving_fibre_formula(target, time),
                ("EHS", total, "time fibre", time, target),
            )
        current = {state: box.nxt[current[state]] for state in box.states}


# ---------------------------------------------------------------------------
# Driver


def run_family(
    candidate: str,
    parameter_name: str,
    parameters: Iterable[int],
    state_factory: Callable[[int], Iterable[State]],
    update_factory: Callable[[int], Callable[[State], State]],
    validator: Callable[[int, Box], None] | None = None,
) -> None:
    rows = []
    images = []
    fixed = []
    tails = []
    spectra = []
    for parameter in parameters:
        box = exact_box(candidate, parameter, state_factory(parameter), update_factory(parameter))
        if validator is not None:
            validator(parameter, box)
        rows.append((parameter, box))
        images.append(box.image)
        fixed.append(box.fixed)
        tails.append(box.max_tail)
        spectra.append(".".join(map(str, sorted({box.periods[x] for x in box.states if box.tails[x] == 0}))))
    parameter, box = rows[-1]
    print(summary(candidate, parameter_name, parameter, box))
    print(
        f"{candidate}_sequences image={','.join(map(str, images))} "
        f"fixed={','.join(map(str, fixed))} max_tail={','.join(map(str, tails))} "
        f"period_spectra={'/'.join(spectra)}"
    )


def main() -> None:
    print("P187_191_COMBINATORIAL_BREADTH_EXACT_V2")
    print("denominator=21")
    print("classes=permutations,words,set_partitions,posets,compositions,integer_partitions")

    permutation_states = lambda n: permutations(range(n))
    run_family("C01_ACTR", "n", range(1, 8), permutation_states, lambda _: anchored_cycle_tail_rotation)
    run_family("C02_MCP", "n", range(1, 8), permutation_states, lambda _: minimum_cycle_powering)
    run_family("C03_IPF", "n", range(1, 8), permutation_states, lambda _: interior_peak_fall)
    run_family("C20_DRA", "n", range(1, 9), permutation_states, lambda _: displacement_rank_assignment)

    word_states = lambda n: product(range(n), repeat=n)
    run_family("C04_PME", "n", range(1, 7), word_states, lambda _: positional_multiplicity_echo, validate_pme)
    AUDIT.signal("C04_PME", "pointwise_merger_clock")
    AUDIT.signal("C04_PME", "every_target_fibre_product")
    run_family("C05_RLF", "n", range(1, 7), word_states, lambda _: run_length_feedback)
    run_family("C06_IHC", "n", range(1, 7), word_states, lambda _: interval_hull_coverage)
    run_family("C07_PBD", "n", range(1, 7), word_states, lambda _: prefix_bigram_diversity)
    run_family("C19_ISE", "n", range(1, 7), word_states, lambda _: interval_span_echo)

    partition_states = lambda n: set_partitions(n)
    run_family("C08_PBMP", "n", range(1, 9), partition_states, lambda _: parallel_block_minimum_peeling, validate_pbmp)
    AUDIT.signal("C08_PBMP", "pointwise_block_clock")
    AUDIT.signal("C08_PBMP", "all_time_every_target_fibres")
    run_family("C09_CSM", "n", range(1, 9), partition_states, lambda _: cyclic_shift_meet, validate_csm)
    AUDIT.signal("C09_CSM", "closed_semilattice_iterate")
    run_family("C10_MRC", "n", range(1, 9), partition_states, lambda _: minima_reservoir_collection)
    run_family("C11_XCM", "n", range(1, 9), partition_states, lambda _: crossing_component_merge)
    run_family("C16_MGBF", "n", range(1, 10), partition_states, lambda _: maximum_gap_block_fission, validate_mgbf)
    AUDIT.signal("C16_MGBF", "cartesian_split_tree_clock")
    AUDIT.signal("C16_MGBF", "every_target_matching_fibres")

    poset_states = lambda n: labelled_posets(n)
    run_family("C12_RPE", "n", range(1, 6), poset_states, lambda n: lambda state: relational_power_erosion(state, n), validate_rpe)
    AUDIT.signal("C12_RPE", "logarithmic_height_clock")
    run_family("C13_CSR", "n", range(1, 6), poset_states, lambda n: lambda state: cyclic_shift_relation_intersection(state, n), validate_csr)
    AUDIT.signal("C13_CSR", "closed_shift_intersection_iterate")
    AUDIT.signal("C13_CSR", "cyclic_run_clock")
    run_family("C18_MLI", "n", range(1, 6), poset_states, lambda n: lambda state: minimal_layer_isolation(state, n), validate_mli)
    AUDIT.signal("C18_MLI", "minimal_layer_height_clock")

    composition_states = lambda total: compositions(total)
    run_family("C14_EVA", "N", range(1, 13), composition_states, lambda _: equal_value_aggregation, validate_eva)
    AUDIT.signal("C14_EVA", "strict_length_clock_bound")
    AUDIT.signal("C14_EVA", "every_target_divisor_fibre")
    run_family("C15_EHS", "N", range(1, 15), composition_states, lambda _: even_halving_split, validate_ehs)
    AUDIT.signal("C15_EHS", "pointwise_valuation_clock")
    AUDIT.signal("C15_EHS", "all_time_tiling_fibres")
    run_family("C21_PDCF", "N", range(1, 16), composition_states, lambda _: prefix_divisibility_cut_filter, validate_pdcf)
    AUDIT.signal("C21_PDCF", "sharp_global_cut_clock")
    AUDIT.signal("C21_PDCF", "every_target_path_fibres")

    integer_partition_states = lambda total: integer_partitions(total)
    run_family("C17_TRR", "N", range(1, 26), integer_partition_states, lambda _: top_row_reservoir, validate_trr)
    AUDIT.signal("C17_TRR", "pointwise_second_row_clock")
    AUDIT.signal("C17_TRR", "every_target_linear_fibres")

    print(f"signal_count={len(AUDIT.signals)}")
    print("signals=" + ",".join(AUDIT.signals))
    print(f"transitions={AUDIT.transitions}")
    print(f"exact_assertions={AUDIT.assertions}")
    print(f"transition_digest={AUDIT.digest.hexdigest()}")
    print("status=PASS")


if __name__ == "__main__":
    main()
