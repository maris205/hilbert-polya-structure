#!/usr/bin/env python3
"""Deterministic exact scout for the P182--P186 combinatorial lane.

Only Python's standard library is used.  The large three controls (PDD,
RCS, and DSR) compare literal updates with separate closed descriptions;
the remaining nine systems are breadth falsifiers.  An ``assertion`` is one
call to Audit.check, not a state visit or an inferred formula.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
from itertools import combinations, permutations, product
from math import comb, factorial


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def check(self, condition: bool, message: str) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(message)


AUDIT = Audit()


def orbit_data(state, update):
    seen = {}
    value = state
    while value not in seen:
        seen[value] = len(seen)
        value = update(value)
    return seen[value], len(seen) - seen[value], value


def falling(n: int, k: int) -> int:
    answer = 1
    for value in range(n - k + 1, n + 1):
        answer *= value
    return answer


def fib(index: int) -> int:
    left, right = 0, 1
    for _ in range(index):
        left, right = right, left + right
    return left


def compositions(total: int):
    if total == 0:
        yield ()
        return
    for cuts in range(1 << (total - 1)):
        last = 0
        parts = []
        for position in range(1, total):
            if cuts >> (position - 1) & 1:
                parts.append(position - last)
                last = position
        parts.append(total - last)
        yield tuple(parts)


def rgfs(length: int):
    if length == 0:
        yield ()
        return
    word = [0] * length

    def visit(position: int, maximum: int):
        if position == length:
            yield tuple(word)
            return
        for letter in range(maximum + 2):
            word[position] = letter
            yield from visit(position + 1, max(maximum, letter))

    yield from visit(1, 0)


def pack_word(word):
    labels = {}
    packed = []
    for letter in word:
        if letter not in labels:
            labels[letter] = len(labels)
        packed.append(labels[letter])
    return tuple(packed)


def full_graph_stats(states, update):
    state_set = set(states)
    successors = {}
    fibres = Counter()
    for state in states:
        target = update(state)
        AUDIT.check(target in state_set, "update left its finite carrier")
        successors[state] = target
        fibres[target] += 1
    tails = Counter()
    periods = Counter()
    for state in states:
        tail, period, _ = orbit_data(state, update)
        AUDIT.check(period >= 1, "invalid eventual period")
        tails[tail] += 1
        periods[period] += 1
    return {
        "states": len(states),
        "image": len(fibres),
        "fixed": sum(successors[state] == state for state in states),
        "tail_hist": tuple(sorted(tails.items())),
        "period_hist": tuple(sorted(periods.items())),
        "periods": tuple(sorted(periods)),
        "max_tail": max(tails, default=0),
        "max_period": max(periods, default=1),
        "fibre_min": min(fibres.values(), default=0),
        "fibre_max": max(fibres.values(), default=0),
        "fibres": fibres,
    }


# ---------------------------------------------------------------------------
# C01 / PDD: prefix-diversity delay on words.


def prefix_diversity(word):
    seen = set()
    output = []
    for letter in word:
        output.append(len(seen))
        seen.add(letter)
    return tuple(output)


def pdd_closed_iterate(word, time: int):
    if time == 0:
        return tuple(word)
    first = prefix_diversity(word)
    shift = time - 1
    return tuple(
        position
        if position < shift
        else shift + first[position - shift]
        for position in range(len(word))
    )


def pdd_fibre_formula(target, time: int, alphabet: int) -> int:
    length = len(target)
    shift = time - 1
    first = tuple(
        target[position + shift] - shift
        for position in range(length - shift)
    )
    if len(first) == 1:
        return alphabet**length
    distinct = 1
    answer = alphabet
    # first[j+1]-first[j] records whether source position j is new.
    for position in range(1, length - time):
        is_new = first[position + 1] - first[position]
        AUDIT.check(is_new in (0, 1), "PDD target is not a novelty path")
        if is_new:
            answer *= alphabet - distinct
            distinct += 1
        else:
            answer *= distinct
    answer *= alphabet**time
    return answer


def probe_pdd():
    summaries = []
    for length in range(1, 8):
        fibres = {time: Counter() for time in range(1, max(length, 2))}
        tails = Counter()
        identity = tuple(range(length))
        state_count = length**length
        for word in product(range(length), repeat=length):
            value = tuple(word)
            first = prefix_diversity(value)
            AUDIT.check(first[0] == 0, "PDD first coordinate")
            if length > 1:
                AUDIT.check(first[1] == 1, "PDD forced second coordinate")
            for time in range(1, length):
                value = prefix_diversity(value)
                closed = pdd_closed_iterate(word, time)
                AUDIT.check(value == closed, "PDD closed iterate")
                fibres[time][value] += 1
            tail, period, endpoint = orbit_data(word, prefix_diversity)
            AUDIT.check(period == 1 and endpoint == identity, "PDD endpoint")
            AUDIT.check(tail <= max(length - 1, 0), "PDD sharp bound")
            tails[tail] += 1

        if length == 1:
            AUDIT.check(tails == Counter({0: 1}), "PDD singleton box")
            summaries.append((1, 1, 1, 0, ((0, 1),)))
            continue

        for time, observed in fibres.items():
            AUDIT.check(
                len(observed) == 2 ** max(length - time - 1, 0),
                "PDD all-time image size",
            )
            for target, count in observed.items():
                AUDIT.check(
                    count == pdd_fibre_formula(target, time, length),
                    "PDD every-target fibre",
                )
            AUDIT.check(sum(observed.values()) == state_count, "PDD fibre mass")
            cdf = sum(count for depth, count in tails.items() if depth <= time)
            AUDIT.check(
                cdf == falling(length, length - time) * length**time,
                "PDD exact depth CDF",
            )
        AUDIT.check(tails[length - 1] > 0, "PDD sharp clock witness")
        summaries.append(
            (
                length,
                state_count,
                len(fibres[1]),
                max(tails),
                tuple(sorted(tails.items())),
            )
        )
    return summaries


# ---------------------------------------------------------------------------
# C02 / RCS: rank-compression support on subsets.


def rank_compress(subset):
    return tuple(sorted({value - rank for rank, value in enumerate(subset)}))


def rcs_closed_iterate(subset, time: int):
    """Closed time-t state: subtract t from every old gap and delete zeros."""
    if not subset:
        return ()
    positive_gaps = [
        subset[index] - subset[index - 1] - time
        for index in range(1, len(subset))
        if subset[index] - subset[index - 1] > time
    ]
    answer = [subset[0]]
    for gap in positive_gaps:
        answer.append(answer[-1] + gap)
    return tuple(answer)


@lru_cache(maxsize=None)
def short_gap_slot_count(time: int, slots: int, budget: int) -> int:
    """Coefficient sum of (1-(z+...+z^time))^-slots through z^budget."""
    if budget < 0:
        return 0
    sequence = [0] * (budget + 1)
    sequence[0] = 1
    for weight in range(1, budget + 1):
        sequence[weight] = sum(
            sequence[weight - part] for part in range(1, min(time, weight) + 1)
        )
    polynomial = [1] + [0] * budget
    for _ in range(slots):
        updated = [0] * (budget + 1)
        for left, left_count in enumerate(polynomial):
            if left_count:
                for right, right_count in enumerate(sequence[: budget - left + 1]):
                    updated[left + right] += left_count * right_count
        polynomial = updated
    return sum(polynomial)


def rcs_time_fibre_formula(target, time: int, length: int) -> int:
    if not target:
        return 1
    long_count = len(target) - 1
    long_span = target[-1] - target[0] + time * long_count
    budget = length - 1 - target[0] - long_span
    return short_gap_slot_count(time, long_count + 1, budget)


def probe_rcs():
    summaries = []
    for length in range(1, 19):
        fibres = Counter()
        time_fibres = [Counter() for _ in range(length)]
        tails = Counter()
        endpoints = Counter()
        deepest = []
        image = set()
        for mask in range(1 << length):
            subset = tuple(i for i in range(length) if mask >> i & 1)
            target = rank_compress(subset)
            fibres[target] += 1
            image.add(target)
            AUDIT.check(all(0 <= x < length for x in target), "RCS range")
            AUDIT.check(len(target) <= len(subset), "RCS size monotonicity")
            if subset:
                AUDIT.check(target[0] == subset[0], "RCS minimum invariant")
                if len(subset) > 1:
                    AUDIT.check(
                        target[-1] == subset[-1] - len(subset) + 1,
                        "RCS maximum drop",
                    )
            tail, period, endpoint = orbit_data(subset, rank_compress)
            expected_endpoint = () if not subset else (subset[0],)
            AUDIT.check(period == 1 and endpoint == expected_endpoint, "RCS endpoint")
            AUDIT.check(tail <= length - 1, "RCS depth bound")
            gap_height = (
                0
                if len(subset) <= 1
                else max(subset[i] - subset[i - 1] for i in range(1, len(subset)))
            )
            AUDIT.check(tail == gap_height, "RCS pointwise maximum-gap clock")
            value = subset
            for time in range(1, length):
                value = rank_compress(value)
                closed = rcs_closed_iterate(subset, time)
                AUDIT.check(value == closed, "RCS closed all-time state")
                time_fibres[time][value] += 1
            tails[tail] += 1
            endpoints[endpoint] += 1
            if tail == length - 1:
                deepest.append(subset)

        predicted_image = {
            tuple(i for i in range(length) if mask >> i & 1)
            for mask in range(1 << length)
            if mask == 0
            or (
                max(i for i in range(length) if mask >> i & 1)
                + mask.bit_count()
                <= length
            )
        }
        AUDIT.check(image == predicted_image, "RCS image condition")
        AUDIT.check(len(image) == fib(length + 2), "RCS Fibonacci image")
        for target in predicted_image:
            predicted = (
                1
                if not target
                else comb(length - target[-1], len(target))
            )
            AUDIT.check(fibres[target] == predicted, "RCS every-target fibre")
        AUDIT.check(sum(fibres.values()) == 1 << length, "RCS fibre mass")
        AUDIT.check(
            endpoints[()] == 1,
            "RCS empty basin",
        )
        for minimum in range(length):
            AUDIT.check(
                endpoints[(minimum,)] == 2 ** (length - minimum - 1),
                "RCS singleton basin",
            )
        AUDIT.check(
            deepest == [(0, length - 1)] if length > 1 else deepest == [(), (0,)],
            "RCS unique sharp witness",
        )
        all_subsets = [
            tuple(i for i in range(length) if mask >> i & 1)
            for mask in range(1 << length)
        ]
        for time in range(1, length):
            predicted_time_image = {
                target
                for target in all_subsets
                if not target
                or target[-1] + time * (len(target) - 1) < length
            }
            AUDIT.check(
                set(time_fibres[time]) == predicted_time_image,
                "RCS all-time image condition",
            )
            for target in predicted_time_image:
                AUDIT.check(
                    time_fibres[time][target]
                    == rcs_time_fibre_formula(target, time, length),
                    "RCS all-time every-target fibre",
                )
            AUDIT.check(
                sum(time_fibres[time].values()) == 1 << length,
                "RCS all-time fibre mass",
            )
        summaries.append(
            (
                length,
                1 << length,
                len(image),
                length + 1,
                max(tails),
                max(fibres.values()),
                tuple(sorted(tails.items())),
            )
        )
    return summaries


# ---------------------------------------------------------------------------
# C03 / DSR: stable displacement ranking on permutations.


def stable_rank(values):
    order = sorted(range(len(values)), key=lambda i: (values[i], i))
    answer = [0] * len(values)
    for rank, position in enumerate(order):
        answer[position] = rank
    return tuple(answer)


def displacement_rank(permutation):
    return stable_rank(tuple(value - i for i, value in enumerate(permutation)))


def dsr_fixed_condition(permutation):
    inverse = [0] * len(permutation)
    for position, value in enumerate(permutation):
        inverse[value] = position
    return all(inverse[value + 1] <= inverse[value] + 1 for value in range(len(permutation) - 1))


def dsr_fixed_from_composition(parts):
    length = sum(parts)
    inverse = []
    right = length
    for part in parts:
        right -= part
        inverse.extend(range(right, right + part))
    permutation = [0] * length
    for value, position in enumerate(inverse):
        permutation[position] = value
    return tuple(permutation)


def probe_dsr():
    summaries = []
    for length in range(1, 10):
        states = list(permutations(range(length)))
        fibres = Counter()
        tails = Counter()
        fixed = set()
        for state in states:
            target = displacement_rank(state)
            AUDIT.check(tuple(sorted(target)) == tuple(range(length)), "DSR permutation range")
            fibres[target] += 1
            is_fixed = target == state
            AUDIT.check(is_fixed == dsr_fixed_condition(state), "DSR fixed criterion")
            if is_fixed:
                fixed.add(state)
            tail, period, endpoint = orbit_data(state, displacement_rank)
            AUDIT.check(period == 1, "DSR nontrivial recurrent cycle")
            AUDIT.check(displacement_rank(endpoint) == endpoint, "DSR terminal fixed point")
            tails[tail] += 1
        constructed = {dsr_fixed_from_composition(parts) for parts in compositions(length)}
        AUDIT.check(fixed == constructed, "DSR composition bijection")
        AUDIT.check(len(fixed) == 2 ** (length - 1), "DSR fixed count")
        AUDIT.check(sum(fibres.values()) == factorial(length), "DSR fibre mass")
        summaries.append(
            (
                length,
                factorial(length),
                len(fibres),
                len(fixed),
                max(tails),
                (min(fibres.values()), max(fibres.values())),
                tuple(sorted(tails.items())),
            )
        )
    return summaries


# ---------------------------------------------------------------------------
# C04 / BDS: distance-from-block-minimum slicing of set partitions.


def block_distance_slice(rgf):
    first = {}
    distances = []
    for position, block in enumerate(rgf):
        if block not in first:
            first[block] = position
        distances.append(position - first[block])
    return pack_word(distances)


def probe_bds():
    summaries = []
    for length in range(1, 11):
        states = list(rgfs(length))
        stats = full_graph_stats(states, block_distance_slice)
        if length == 1:
            AUDIT.check(stats["periods"] == (1,), "BDS singleton period")
        else:
            AUDIT.check(stats["periods"] == (2,), "BDS observed period-two core")
            AUDIT.check(stats["fixed"] == 0, "BDS unexpected fixed partition")
        summaries.append(
            (
                length,
                stats["states"],
                stats["image"],
                stats["fixed"],
                stats["max_tail"],
                stats["periods"],
                stats["tail_hist"],
            )
        )
    return summaries


# ---------------------------------------------------------------------------
# C05 / CAD: cyclic adjacent-difference ranking of permutations.


def cyclic_difference_rank(permutation):
    length = len(permutation)
    differences = tuple(
        permutation[(i + 1) % length] - permutation[i] for i in range(length)
    )
    return stable_rank(differences)


def probe_cad():
    summaries = []
    for length in range(1, 9):
        states = list(permutations(range(length)))
        stats = full_graph_stats(states, cyclic_difference_rank)
        summaries.append(
            (
                length,
                stats["states"],
                stats["image"],
                stats["fixed"],
                stats["max_tail"],
                stats["periods"],
            )
        )
    return summaries


# ---------------------------------------------------------------------------
# C06 / CGS: cyclic gap-support dynamics on subsets.


def cyclic_gap_support(subset, length: int):
    if not subset:
        return ()
    gaps = [subset[i + 1] - subset[i] for i in range(len(subset) - 1)]
    gaps.append(length + subset[0] - subset[-1])
    return tuple(sorted({gap % length for gap in gaps}))


def probe_cgs():
    summaries = []
    for length in range(1, 15):
        states = [
            tuple(i for i in range(length) if mask >> i & 1)
            for mask in range(1 << length)
        ]
        stats = full_graph_stats(states, lambda state, n=length: cyclic_gap_support(state, n))
        summaries.append(
            (
                length,
                stats["states"],
                stats["image"],
                stats["fixed"],
                stats["max_tail"],
                stats["periods"],
            )
        )
    return summaries


# ---------------------------------------------------------------------------
# C07 / IHM: interval-hull merging on set partitions.


def interval_hull_merge(rgf):
    block_count = max(rgf, default=-1) + 1
    mins = [len(rgf)] * block_count
    maxs = [-1] * block_count
    for position, block in enumerate(rgf):
        mins[block] = min(mins[block], position)
        maxs[block] = max(maxs[block], position)
    parent = list(range(block_count))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        x, y = find(x), find(y)
        if x != y:
            parent[y] = x

    for left in range(block_count):
        for right in range(left + 1, block_count):
            if max(mins[left], mins[right]) <= min(maxs[left], maxs[right]):
                union(left, right)
    return pack_word(tuple(find(block) for block in rgf))


def is_interval_partition(rgf):
    return all(rgf[i] <= rgf[i + 1] for i in range(len(rgf) - 1))


def probe_ihm():
    atomic = {length: 0 for length in range(1, 10)}
    for length in range(1, 10):
        one_block = (0,) * length
        atomic[length] = sum(interval_hull_merge(rgf) == one_block for rgf in rgfs(length))
    summaries = []
    for length in range(1, 10):
        states = list(rgfs(length))
        fibres = Counter(interval_hull_merge(state) for state in states)
        for state in states:
            target = interval_hull_merge(state)
            AUDIT.check(interval_hull_merge(target) == target, "IHM idempotence")
            AUDIT.check(is_interval_partition(target), "IHM target intervals")
        AUDIT.check(len(fibres) == 2 ** (length - 1), "IHM image size")
        for target, count in fibres.items():
            block_sizes = Counter(target).values()
            predicted = 1
            for size in block_sizes:
                predicted *= atomic[size]
            AUDIT.check(count == predicted, "IHM product fibre")
        summaries.append(
            (
                length,
                len(states),
                len(fibres),
                max(fibres.values()),
                tuple(atomic[i] for i in range(1, length + 1)),
            )
        )
    return summaries


# ---------------------------------------------------------------------------
# C08 / FPT: leftmost descent unit transfer on compositions.


def first_peak_transfer(parts):
    output = list(parts)
    for i in range(len(output) - 1):
        if output[i] > output[i + 1]:
            output[i] -= 1
            output[i + 1] += 1
            break
    return tuple(output)


def probe_fpt():
    summaries = []
    for total in range(1, 15):
        states = list(compositions(total))
        stats = full_graph_stats(states, first_peak_transfer)
        for state in states:
            target = first_peak_transfer(state)
            if target != state:
                old_weight = sum(i * value for i, value in enumerate(state))
                new_weight = sum(i * value for i, value in enumerate(target))
                AUDIT.check(new_weight == old_weight + 1, "FPT potential increment")
            else:
                AUDIT.check(
                    all(state[i] <= state[i + 1] for i in range(len(state) - 1)),
                    "FPT fixed composition",
                )
        AUDIT.check(stats["periods"] == (1,), "FPT nontrivial cycle")
        summaries.append(
            (total, len(states), stats["image"], stats["fixed"], stats["max_tail"])
        )
    return summaries


# ---------------------------------------------------------------------------
# C09 / FCR: rotate a composition by its first part modulo its length.


def first_part_rotation(parts):
    if not parts:
        return parts
    shift = parts[0] % len(parts)
    return tuple(parts[shift:] + parts[:shift])


def probe_fcr():
    summaries = []
    for total in range(1, 13):
        states = list(compositions(total))
        stats = full_graph_stats(states, first_part_rotation)
        summaries.append(
            (
                total,
                len(states),
                stats["image"],
                stats["fixed"],
                stats["max_tail"],
                stats["periods"],
            )
        )
    return summaries


# ---------------------------------------------------------------------------
# Graph helpers and C10/C11.


def graph_edges(order: int):
    return tuple(combinations(range(order), 2))


def graph_degrees(mask: int, order: int, edges):
    degrees = [0] * order
    for bit, (left, right) in enumerate(edges):
        if mask >> bit & 1:
            degrees[left] += 1
            degrees[right] += 1
    return degrees


def maximum_endpoint_projection(mask: int, order: int, edges):
    degrees = graph_degrees(mask, order, edges)
    maximum = max(degrees, default=0)
    output = 0
    for bit, (left, right) in enumerate(edges):
        if mask >> bit & 1 and (degrees[left] == maximum or degrees[right] == maximum):
            output |= 1 << bit
    return output


def degree_threshold_regeneration(mask: int, order: int, edges):
    degrees = graph_degrees(mask, order, edges)
    output = 0
    for bit, (left, right) in enumerate(edges):
        if degrees[left] + degrees[right] >= order:
            output |= 1 << bit
    return output


def probe_mep():
    summaries = []
    for order in range(1, 7):
        edges = graph_edges(order)
        states = list(range(1 << len(edges)))
        update = lambda state, n=order, es=edges: maximum_endpoint_projection(state, n, es)
        stats = full_graph_stats(states, update)
        for state in states:
            AUDIT.check(update(update(state)) == update(state), "MEP idempotence")
        summaries.append(
            (order, len(states), stats["image"], stats["fixed"], stats["fibre_max"])
        )
    return summaries


def probe_dtr():
    summaries = []
    for order in range(1, 7):
        edges = graph_edges(order)
        states = list(range(1 << len(edges)))
        update = lambda state, n=order, es=edges: degree_threshold_regeneration(state, n, es)
        stats = full_graph_stats(states, update)
        AUDIT.check(stats["periods"] == (1,), "DTR observed nonfixed cycle")
        summaries.append(
            (
                order,
                len(states),
                stats["image"],
                stats["fixed"],
                stats["max_tail"],
            )
        )
    return summaries


# ---------------------------------------------------------------------------
# C12 / HLC: replace a poset by the complete order of its height layers.


def labelled_posets(order: int):
    pairs = tuple(combinations(range(order), 2))
    for choices in product((0, 1, 2), repeat=len(pairs)):
        rows = [0] * order
        for choice, (left, right) in zip(choices, pairs):
            if choice == 1:
                rows[left] |= 1 << right
            elif choice == 2:
                rows[right] |= 1 << left
        transitive = True
        for left in range(order):
            for middle in range(order):
                if rows[left] >> middle & 1 and rows[middle] & ~rows[left]:
                    transitive = False
                    break
            if not transitive:
                break
        if transitive:
            yield tuple(rows)


def poset_heights(rows):
    order = len(rows)
    memo = {}

    def height(vertex):
        if vertex not in memo:
            predecessors = [u for u in range(order) if rows[u] >> vertex & 1]
            memo[vertex] = 0 if not predecessors else 1 + max(height(u) for u in predecessors)
        return memo[vertex]

    return tuple(height(vertex) for vertex in range(order))


def height_layer_completion(rows):
    heights = poset_heights(rows)
    order = len(rows)
    return tuple(
        sum(1 << right for right in range(order) if heights[left] < heights[right])
        for left in range(order)
    )


def stirling2(n: int, k: int) -> int:
    table = [[0] * (k + 1) for _ in range(n + 1)]
    table[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            table[i][j] = table[i - 1][j - 1] + j * table[i - 1][j]
    return table[n][k]


def fubini(n: int) -> int:
    return sum(factorial(k) * stirling2(n, k) for k in range(1, n + 1))


def probe_hlc():
    summaries = []
    for order in range(1, 6):
        states = list(labelled_posets(order))
        fibres = Counter(height_layer_completion(state) for state in states)
        for state in states:
            target = height_layer_completion(state)
            AUDIT.check(height_layer_completion(target) == target, "HLC idempotence")
        AUDIT.check(len(fibres) == fubini(order), "HLC ordered-partition image")
        summaries.append((order, len(states), len(fibres), max(fibres.values())))
    return summaries


def compact_last(rows):
    return rows[-1]


def main() -> None:
    start = AUDIT.assertions
    pdd = probe_pdd()
    pdd_count = AUDIT.assertions - start
    print(f"PDD PASS assertions={pdd_count} last={compact_last(pdd)}")

    start = AUDIT.assertions
    rcs = probe_rcs()
    rcs_count = AUDIT.assertions - start
    print(f"RCS PASS assertions={rcs_count} last={compact_last(rcs)}")

    start = AUDIT.assertions
    dsr = probe_dsr()
    dsr_count = AUDIT.assertions - start
    print(f"DSR PASS assertions={dsr_count} last={compact_last(dsr)}")

    start = AUDIT.assertions
    bds = probe_bds()
    print(f"BDS PASS assertions={AUDIT.assertions-start} last={compact_last(bds)}")

    start = AUDIT.assertions
    cad = probe_cad()
    print(f"CAD PASS assertions={AUDIT.assertions-start} last={compact_last(cad)}")

    start = AUDIT.assertions
    cgs = probe_cgs()
    print(f"CGS PASS assertions={AUDIT.assertions-start} last={compact_last(cgs)}")

    start = AUDIT.assertions
    ihm = probe_ihm()
    print(f"IHM PASS assertions={AUDIT.assertions-start} last={compact_last(ihm)}")

    start = AUDIT.assertions
    fpt = probe_fpt()
    print(f"FPT PASS assertions={AUDIT.assertions-start} last={compact_last(fpt)}")

    start = AUDIT.assertions
    fcr = probe_fcr()
    print(f"FCR PASS assertions={AUDIT.assertions-start} last={compact_last(fcr)}")

    start = AUDIT.assertions
    mep = probe_mep()
    print(f"MEP PASS assertions={AUDIT.assertions-start} last={compact_last(mep)}")

    start = AUDIT.assertions
    dtr = probe_dtr()
    print(f"DTR PASS assertions={AUDIT.assertions-start} last={compact_last(dtr)}")

    start = AUDIT.assertions
    hlc = probe_hlc()
    print(f"HLC PASS assertions={AUDIT.assertions-start} last={compact_last(hlc)}")

    AUDIT.check(len((pdd, rcs, dsr, bds, cad, cgs, ihm, fpt, fcr, mep, dtr, hlc)) == 12,
                "breadth denominator")
    print(f"TOTAL_ASSERTIONS={AUDIT.assertions}")
    print("BREADTH_LITERAL_SYSTEMS=12")
    print("RECOMMEND=PDD,RCS")
    print("RESERVE=DSR")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
