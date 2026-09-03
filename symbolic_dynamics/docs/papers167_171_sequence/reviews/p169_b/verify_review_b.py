#!/usr/bin/env python3
"""Independent exact control for P169 Hostile Review B.

The verifier is reviewer-owned and standard-library only.  It imports no
author or scouting module.  Its carrier is generated directly as canonical
tuples of blocks; restricted-growth words are used only as a separately
computed coordinate view.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
from collections import Counter, defaultdict
from pathlib import Path


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def check(self, condition: bool, label: str) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(label)

    def equal(self, left, right, label: str) -> None:
        self.assertions += 1
        if left != right:
            raise AssertionError(f"{label}: {left!r} != {right!r}")


A = Audit()


def canonical_partitions(n: int) -> tuple[tuple[tuple[int, ...], ...], ...]:
    """Generate each set partition once, ordered by increasing block minima."""
    if n == 0:
        return ((),)
    current = [((0,),)]
    for label in range(1, n):
        following = []
        for partition in current:
            for index in range(len(partition)):
                blocks = list(partition)
                blocks[index] = blocks[index] + (label,)
                following.append(tuple(blocks))
            following.append(partition + ((label,),))
        current = following
    return tuple(current)


def encode(partition: tuple[tuple[int, ...], ...]) -> tuple[int, ...]:
    word = [0] * sum(map(len, partition))
    for block_index, block in enumerate(partition):
        for label in block:
            word[label] = block_index
    return tuple(word)


def decode(word: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    block_count = max(word) + 1
    return tuple(tuple(i for i, value in enumerate(word) if value == block)
                 for block in range(block_count))


def is_restricted_growth(word: tuple[int, ...]) -> bool:
    if not word or word[0] != 0:
        return False
    seen_maximum = 0
    for value in word[1:]:
        if value > seen_maximum + 1:
            return False
        seen_maximum = max(seen_maximum, value)
    return True


def transfer(partition: tuple[tuple[int, ...], ...]) -> tuple[tuple[int, ...], ...]:
    """Literal simultaneous maximum donation on block tuples."""
    block_count = len(partition)
    donors = [block[-1] if len(block) > 1 else None for block in partition]
    output = []
    for index, block in enumerate(partition):
        retained = list(block[:-1] if donors[index] is not None else block)
        incoming = donors[index - 1]
        if incoming is not None:
            retained.append(incoming)
        output.append(tuple(sorted(retained)))
    return tuple(output)


def last_occurrence_step(word: tuple[int, ...]) -> tuple[int, ...]:
    """Independent RGF-coordinate implementation of the claimed update."""
    block_count = max(word) + 1
    counts = Counter(word)
    final = {value: max(i for i, x in enumerate(word) if x == value)
             for value in range(block_count)}
    output = list(word)
    for value in range(block_count):
        if counts[value] > 1:
            output[final[value]] = (value + 1) % block_count
    return tuple(output)


def iterate(partition: tuple[tuple[int, ...], ...], steps: int):
    for _ in range(steps):
        partition = transfer(partition)
    return partition


def orbit_data(partition: tuple[tuple[int, ...], ...]) -> tuple[int, int]:
    first_time = {}
    time = 0
    while partition not in first_time:
        first_time[partition] = time
        partition = transfer(partition)
        time += 1
    return first_time[partition], time - first_time[partition]


def load(partition: tuple[tuple[int, ...], ...]) -> tuple[int, ...]:
    return tuple(len(block) - 1 for block in partition)


def recurrent_normal_form(partition: tuple[tuple[int, ...], ...]) -> bool:
    word = encode(partition)
    n = len(word)
    k = len(partition)
    if k in (1, n):
        return True
    excess = n - k
    if excess >= k:
        return (len(set(word[:excess])) == k
                and set(word[-k:]) == set(range(k)))
    return (word[:k] == tuple(range(k))
            and len(set(word[-excess:])) == excess)


def stirling_second(n: int, k: int) -> int:
    row = [1] + [0] * k
    for _ in range(n):
        row = [0] + [j * row[j] + row[j - 1]
                     for j in range(1, k + 1)]
    return row[k]


def falling(k: int, m: int) -> int:
    return math.factorial(k) // math.factorial(k - m)


def bell_numbers(limit: int) -> list[int]:
    values = [1]
    for n in range(limit):
        values.append(sum(math.comb(n, j) * values[j]
                          for j in range(n + 1)))
    return values


def queue_step(state: tuple[int, ...]) -> tuple[int, ...]:
    fired = tuple(value > 0 for value in state)
    return tuple(state[i] - int(fired[i]) + int(fired[i - 1])
                 for i in range(len(state)))


def weak_compositions(total: int, length: int):
    if length == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in weak_compositions(total - first, length - 1):
            yield (first,) + rest


def lifted_height(state: tuple[int, ...], index: int) -> int:
    period = len(state)
    quotient, remainder = divmod(index, period)
    return quotient * sum(state) + sum(state[:remainder + 1])


def maxplus_height(state: tuple[int, ...], time: int, index: int) -> int:
    return max(lifted_height(state, index - delay) - (time - delay)
               for delay in range(time + 1))


def check_maxplus_cones() -> int:
    load_vectors = 0
    for k in range(1, 9):
        for mass in range(1, 13):
            for initial in weak_compositions(mass, k):
                load_vectors += 1
                for i in range(-1, k + 1):
                    A.equal(lifted_height(initial, i)
                            - lifted_height(initial, i - 1),
                            initial[i % k], f"height lift k={k},m={mass}")

                current = initial
                for time in range(k):
                    recovered = tuple(
                        maxplus_height(initial, time, i)
                        - maxplus_height(initial, time, i - 1)
                        for i in range(k)
                    )
                    A.equal(recovered, current,
                            f"max-plus solution k={k},m={mass},t={time}")
                    for i, value in enumerate(current):
                        cone_mass = sum(initial[(i - r) % k]
                                        for r in range(time + 1))
                        if value == 0:
                            A.check(cone_mass <= time,
                                    f"zero cone k={k},m={mass},t={time}")
                        if value >= 2:
                            A.check(cone_mass >= time + 2,
                                    f"high cone k={k},m={mass},t={time}")
                    current = queue_step(current)

                horizon = mass - 1 if mass <= k else k - 1
                smoothed = initial
                for _ in range(horizon):
                    smoothed = queue_step(smoothed)
                if mass <= k:
                    A.check(max(smoothed) <= 1,
                            f"sparse smoothing k={k},m={mass}")
                    A.equal(queue_step(smoothed),
                            smoothed[-1:] + smoothed[:-1],
                            f"binary rotation k={k},m={mass}")
                if mass >= k:
                    A.check(min(smoothed) >= 1,
                            f"dense smoothing k={k},m={mass}")
                    A.equal(queue_step(smoothed), smoothed,
                            f"positive fixed load k={k},m={mass}")
    return load_vectors


def edge_digest(edges) -> str:
    digest = hashlib.sha256()
    for source in sorted(edges, key=encode):
        digest.update(bytes(encode(source)))
        digest.update(b">")
        digest.update(bytes(encode(edges[source])))
        digest.update(b"\n")
    return digest.hexdigest()


def check_temporal_carriers(maximum_n: int = 9):
    bells = bell_numbers(maximum_n)
    rows = {}
    cached = {}
    for n in range(1, maximum_n + 1):
        states = canonical_partitions(n)
        cached[n] = states
        A.equal(len(states), bells[n], f"Bell carrier n={n}")
        by_k_tails = defaultdict(list)
        recurrent_counts = Counter()
        period_counts = Counter()
        edges = {}

        for state in states:
            word = encode(state)
            A.check(is_restricted_growth(word), f"canonical RGF n={n}")
            target = transfer(state)
            edges[state] = target
            target_word = encode(target)
            A.check(all(target[i][0] < target[i + 1][0]
                        for i in range(len(target) - 1)),
                    f"canonical order preserved n={n}")
            A.equal(decode(target_word), target,
                    f"target block/RGF round trip n={n}")
            A.equal(target_word, last_occurrence_step(word),
                    f"literal/RGF update equivalence n={n}")
            A.equal(len(target), len(state), f"block count invariant n={n}")

            tail, period = orbit_data(state)
            k = len(state)
            m = n - k
            by_k_tails[k].append(tail)
            A.equal(tail == 0, recurrent_normal_form(state),
                    f"recurrent normal form n={n},k={k}")
            if tail == 0:
                recurrent_counts[k] += 1
                period_counts[period] += 1
                A.equal(period, 1 if k in (1, n) else k,
                        f"exact recurrent period n={n},k={k}")

            if 1 < k < n:
                load_time = m - 1 if m <= k else k - 1
                smoothed = iterate(state, load_time)
                if m <= k:
                    A.check(max(load(smoothed)) <= 1,
                            f"partition sparse load window n={n},k={k}")
                if m >= k:
                    A.check(min(load(smoothed)) >= 1,
                            f"partition dense load window n={n},k={k}")
                windowed = iterate(smoothed, k - 1)
                window_word = encode(windowed)
                if m <= k:
                    A.equal(window_word[:k], tuple(range(k)),
                            f"sparse canonical prefix n={n},k={k}")
                if m >= k:
                    A.equal(set(window_word[-k:]), set(range(k)),
                            f"dense terminal permutation n={n},k={k}")

        for k in range(1, n + 1):
            expected_height = (0 if k in (1, n)
                               else min(n - 2, 2 * k - 2))
            A.equal(max(by_k_tails[k]), expected_height,
                    f"sharp stratum height n={n},k={k}")
            if k in (1, n):
                expected_recurrent = 1
            else:
                m = n - k
                expected_recurrent = (math.factorial(k)
                                      * stirling_second(m, k)
                                      if m >= k else falling(k, m))
            A.equal(recurrent_counts[k], expected_recurrent,
                    f"recurrent count n={n},k={k}")

        expected_global = 0 if n <= 2 else n - 2
        A.equal(max(max(values) for values in by_k_tails.values()),
                expected_global, f"global sharp height n={n}")
        expected_periods = ({1} if n <= 2 else set(range(1, n)))
        A.equal(set(period_counts), expected_periods,
                f"possible periods n={n}")
        rows[str(n)] = {
            "states": len(states),
            "image": len(set(edges.values())),
            "global_height": expected_global,
            "period_point_counts": dict(sorted(period_counts.items())),
            "edge_sha256": edge_digest(edges),
        }
    return rows, cached


# Five token types in the manuscript's printed order.
ABSENT, SOLE, MINIMUM, MAXIMUM, INTERIOR = range(5)
TYPE_NAMES = ("absent", "sole", "minimum", "maximum", "interior")


def choices(block: tuple[int, ...], token_type: int):
    if token_type == ABSENT:
        return (None,)
    if token_type == SOLE:
        return block if len(block) == 1 else ()
    if token_type == MINIMUM:
        return block[:1] if len(block) >= 2 else ()
    if token_type == MAXIMUM:
        return block[-1:] if len(block) >= 2 else ()
    return block[1:-1] if len(block) >= 3 else ()


def retained_for_type(block: tuple[int, ...], token_type: int):
    possible = choices(block, token_type)
    if not possible:
        return None
    if token_type == ABSENT:
        return block
    representative = possible[0]
    return tuple(value for value in block if value != representative)


def local_matrix(target, index: int, false_wrap_comparison: bool = False):
    k = len(target)
    current = target[index]
    following = target[(index + 1) % k]
    matrix = [[0] * 5 for _ in range(5)]
    for incoming_type in range(5):
        retained = retained_for_type(current, incoming_type)
        if retained is None or not retained:
            continue
        for outgoing_type in range(5):
            following_retained = retained_for_type(following, outgoing_type)
            impose_order = index < k - 1 or false_wrap_comparison
            if impose_order:
                if (following_retained is None or not following_retained
                        or min(retained) >= min(following_retained)):
                    continue
            for selected in choices(following, outgoing_type):
                if selected is None:
                    if len(retained) == 1:
                        matrix[incoming_type][outgoing_type] += 1
                elif selected > max(retained):
                    matrix[incoming_type][outgoing_type] += 1
    return matrix


def matrix_product(left, right):
    return [[sum(left[i][h] * right[h][j] for h in range(5))
             for j in range(5)] for i in range(5)]


def trace_formula(target, false_wrap_comparison: bool = False) -> int:
    if len(target) == 1:
        return 1
    product_matrix = [[int(i == j) for j in range(5)] for i in range(5)]
    for index in range(len(target)):
        product_matrix = matrix_product(
            product_matrix,
            local_matrix(target, index, false_wrap_comparison)
        )
    return sum(product_matrix[i][i] for i in range(5))


def token_predecessors(target):
    """Direct cyclic-token reconstruction, without five-state compression."""
    k = len(target)
    if k == 1:
        return {target}
    link_choices = [((None,) + target[(i + 1) % k]) for i in range(k)]
    predecessors = set()
    for tokens in itertools.product(*link_choices):
        source = []
        admissible = True
        for i in range(k):
            incoming = tokens[i - 1]
            outgoing = tokens[i]
            retained = list(target[i])
            if incoming is not None:
                retained.remove(incoming)
            if outgoing is None:
                if len(retained) != 1:
                    admissible = False
                    break
            else:
                if not retained or outgoing <= max(retained):
                    admissible = False
                    break
                retained.append(outgoing)
            source.append(tuple(sorted(retained)))
        if not admissible:
            continue
        source_tuple = tuple(source)
        if not all(source_tuple[i][0] < source_tuple[i + 1][0]
                   for i in range(k - 1)):
            continue
        A.equal(transfer(source_tuple), target,
                "direct token reconstruction returns target")
        predecessors.add(source_tuple)
    return predecessors


def partition_text(partition) -> str:
    return "|".join("".join(map(str, block)) for block in partition)


def check_fibres(cached, maximum_n: int = 8):
    rows = {}
    wrap_witness = None
    for n in range(1, maximum_n + 1):
        states = cached[n]
        literal_sources = defaultdict(set)
        for source in states:
            literal_sources[transfer(source)].add(source)
        literal = Counter({target: len(sources)
                           for target, sources in literal_sources.items()})
        image = 0
        maximum = 0
        for target in states:
            trace = trace_formula(target)
            direct = token_predecessors(target)
            A.equal(trace, literal[target], f"trace/literal fibre n={n}")
            A.equal(len(direct), literal[target],
                    f"token/literal fibre n={n}")
            A.equal(set(direct), literal_sources.get(target, set()),
                    f"every predecessor reconstructed n={n}")
            A.equal(trace > 0, target in literal,
                    f"trace image test n={n}")
            image += trace > 0
            maximum = max(maximum, trace)

            for index, block in enumerate(target):
                if len(block) == 1 and len(target) > 1:
                    A.equal(local_matrix(target, index)[SOLE], [0] * 5,
                            f"singleton deletion row n={n},i={index}")

            false_trace = trace_formula(target, false_wrap_comparison=True)
            if wrap_witness is None and false_trace != trace:
                wrap_witness = {
                    "target": partition_text(target),
                    "correct_trace": trace,
                    "false_wrap_trace": false_trace,
                }

        A.equal(image, len(literal), f"fibre image size n={n}")
        rows[str(n)] = {
            "targets": len(states),
            "image": image,
            "maximum_fibre": maximum,
        }

    A.check(wrap_witness is not None,
            "a false last-to-first order comparison changes a fibre")

    target_a = ((0, 2, 5), (1, 3, 4))
    target_d = ((0, 3, 5), (1, 2, 4))
    expected_a = (
        [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
         [0, 0, 0, 1, 1], [0, 0, 0, 0, 0]],
        [[0, 0, 0, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0],
         [0, 0, 0, 1, 0], [0, 0, 0, 1, 0]],
    )
    expected_d = (
        [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0], [0, 0, 0, 0, 0]],
        [[0, 0, 0, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0],
         [0, 0, 0, 1, 1], [0, 0, 0, 1, 0]],
    )
    matrices_a = tuple(local_matrix(target_a, i) for i in range(2))
    matrices_d = tuple(local_matrix(target_d, i) for i in range(2))
    A.equal(matrices_a, expected_a, "printed matrices for 025|134")
    A.equal(matrices_d, expected_d, "printed matrices for 035|124")
    A.equal(tuple((len(b), b[0], b[-1]) for b in target_a),
            tuple((len(b), b[0], b[-1]) for b in target_d),
            "interlacing pair has equal coarse data")
    predecessors_a = token_predecessors(target_a)
    predecessors_d = token_predecessors(target_d)
    A.equal({partition_text(p) for p in predecessors_a},
            {"023|145", "024|135"}, "predecessors for 025|134")
    A.equal({partition_text(p) for p in predecessors_d},
            {"034|125"}, "predecessors for 035|124")
    A.equal(trace_formula(target_a), 2, "interlacing fibre two")
    A.equal(trace_formula(target_d), 1, "interlacing fibre one")

    return rows, wrap_witness, {
        "025|134": {
            "matrices": matrices_a,
            "predecessors": sorted(partition_text(p) for p in predecessors_a),
            "fibre": 2,
        },
        "035|124": {
            "matrices": matrices_d,
            "predecessors": sorted(partition_text(p) for p in predecessors_d),
            "fibre": 1,
        },
    }


def check_sharp_witness(limit: int = 60) -> int:
    strata = 0
    for n in range(3, limit + 1):
        for k in range(2, n):
            strata += 1
            m = n - k
            word = (0,) * (m + 1) + tuple(range(1, k))
            state = decode(word)
            tail, period = orbit_data(state)
            A.equal(tail, min(n - 2, 2 * k - 2),
                    f"sharp witness tail n={n},k={k}")
            A.equal(period, k, f"sharp witness period n={n},k={k}")

            for time in range(min(m - 1, k - 1) + 1):
                expected = ((0,) * (m + 1 - time)
                            + tuple(value
                                    for value in range(1, time + 1)
                                    for _ in range(2))
                            + tuple(range(time + 1, k)))
                A.equal(encode(iterate(state, time)), expected,
                        f"load witness formula n={n},k={k},t={time}")

            load_time = m - 1 if m <= k else k - 1
            load_end = iterate(state, load_time)
            if m <= k:
                r = min(m, k // 2)
                prefix = encode(load_end)[:k]
                occupancy = tuple(prefix.count(value) for value in range(k))
                A.equal(occupancy, (2,) * r + (1,) * (k - 2 * r)
                        + (0,) * r,
                        f"sparse witness prefix n={n},k={k}")
                current = load_end
                for time in range(k):
                    q = tuple(encode(current)[:k].count(value)
                              for value in range(k))
                    if time < k - 1:
                        A.equal(q[-1], 0,
                                f"sparse phase not early n={n},k={k},t={time}")
                    else:
                        A.equal(q, (1,) * k,
                                f"sparse phase endpoint n={n},k={k}")
                    current = transfer(current)

            if m >= k:
                d = m - k
                for step in range(1, k):
                    expected = ((0,) * (d + 1)
                                + tuple(range(1, step))
                                + tuple(value
                                        for value in range(step, k)
                                        for _ in range(2))
                                + (0,) + tuple(range(1, step)))
                    A.equal(encode(iterate(state, k - 1 + step)), expected,
                            f"dense witness formula n={n},k={k},s={step}")
    return strata


def main() -> None:
    load_vectors = check_maxplus_cones()
    temporal_rows, cached = check_temporal_carriers()
    fibre_rows, wrap_witness, interlacing = check_fibres(cached)
    witness_strata = check_sharp_witness()
    result = {
        "decision": "REVIEW_B_INDEPENDENT_CONTROL_PASS",
        "external_status": "HOLD_EXTERNAL",
        "assertions": A.assertions,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope": {
            "carrier_representation": "canonical tuples of blocks",
            "complete_temporal_carriers": "n=1..9",
            "complete_fibres_three_ways": "n=1..8",
            "maxplus_load_vectors": load_vectors,
            "sharp_witness_strata": witness_strata,
            "sharp_witness_limit": 60,
        },
        "state_order": TYPE_NAMES,
        "temporal_n_1_to_9": temporal_rows,
        "fibres_n_1_to_8": fibre_rows,
        "wrap_orientation_witness": wrap_witness,
        "interlacing": interlacing,
    }
    print(json.dumps(result, indent=2, sort_keys=True, separators=(",", ": ")))


if __name__ == "__main__":
    main()
