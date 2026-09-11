#!/usr/bin/env python3
"""Independent exact scout for the P197--P201 word/poset lane.

The script uses only the Python standard library.  It does not import any
author verifier or any earlier scouting implementation.  Its principal job
is to attack the ternary cyclic sign derivative (TCSD); the remaining maps
are denominator controls used by the kill ledger.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
from itertools import combinations, combinations_with_replacement, product
from math import comb


ASSERTIONS = 0


def check(condition: bool, label: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def iterate(step, state, times: int):
    for _ in range(times):
        state = step(state)
    return state


def functional_stats(states, step):
    states = list(states)
    state_set = set(states)
    depth = {}
    period = {}
    cycles = Counter()
    for start in states:
        if start in depth:
            continue
        path = []
        index = {}
        state = start
        while state not in depth and state not in index:
            check(state in state_set, "self-map closure")
            index[state] = len(path)
            path.append(state)
            state = step(state)
        if state in depth:
            value = depth[state]
            cycle_length = period[state]
            for vertex in reversed(path):
                value += 1
                depth[vertex] = value
                period[vertex] = cycle_length
        else:
            first = index[state]
            cycle_length = len(path) - first
            cycles[cycle_length] += 1
            for vertex in path[first:]:
                depth[vertex] = 0
                period[vertex] = cycle_length
            value = 0
            for vertex in reversed(path[:first]):
                value += 1
                depth[vertex] = value
                period[vertex] = cycle_length
    fibres = Counter(step(state) for state in states)
    maximum_fibre = max(fibres.values())
    return {
        "states": len(states),
        "image": len(fibres),
        "fixed": sum(step(state) == state for state in states),
        "recurrent": sum(value == 0 for value in depth.values()),
        "max_tail": max(depth.values()),
        "periods": tuple(sorted(cycles)),
        "cycles": tuple(sorted(cycles.items())),
        "max_fibre": maximum_fibre,
        "max_fibre_targets": sum(value == maximum_fibre for value in fibres.values()),
        "depth_hist": tuple(sorted(Counter(depth.values()).items())),
        "depth": depth,
        "fibres": fibres,
    }


# -------------------------------------------------------------------------
# C01: ternary cyclic sign derivative


ALPHABET = (-1, 0, 1)


def sign(value: int) -> int:
    return (value > 0) - (value < 0)


def open_difference(word):
    return tuple(sign(word[i + 1] - word[i]) for i in range(len(word) - 1))


def open_iterate(word, times: int):
    for _ in range(times):
        word = open_difference(word)
    return word


def tcsd(word):
    length = len(word)
    return tuple(sign(word[(i + 1) % length] - word[i]) for i in range(length))


def rotate_left(word, amount: int):
    amount %= len(word)
    return word[amount:] + word[:amount]


def in_tcsd_core(word) -> bool:
    return iterate(tcsd, word, 4) == rotate_left(word, 2)


def maximum_cyclic_run(word) -> int:
    length = len(word)
    if len(set(word)) == 1:
        return length
    best = 1
    for start in range(length):
        run = 1
        while run < length and word[(start + run) % length] == word[start]:
            run += 1
        best = max(best, run)
    return best


def tcsd_image_condition(word) -> bool:
    skeleton = tuple(value for value in word if value)
    if not skeleton:
        return True
    if len(set(skeleton)) == 1:
        return False
    length = len(skeleton)
    return not any(
        skeleton[i] == skeleton[(i + 1) % length] == skeleton[(i + 2) % length]
        for i in range(length)
    )


def tcsd_fibre_trace(target) -> int:
    """Trace of the product of the strict-lower/I/strict-upper matrices."""
    total = 0
    for first in ALPHABET:
        row = {first: 1}
        for relation in target:
            new = Counter()
            for left, count in row.items():
                for right in ALPHABET:
                    if sign(right - left) == relation:
                        new[right] += count
            row = new
        total += row.get(first, 0)
    return total


def lucas(index: int) -> int:
    if index == 0:
        return 2
    if index == 1:
        return 1
    left, right = 2, 1
    for _ in range(2, index + 1):
        left, right = right, left + right
    return right


TCSD_EXPECTED = {
    1: (1, 1, 1, (1,), 3, 1),
    2: (3, 3, 1, (1, 2), 3, 3),
    3: (13, 13, 1, (1, 12), 3, 7),
    4: (43, 27, 3, (1, 2, 8), 7, 2),
    5: (121, 41, 3, (1, 20), 7, 10),
    6: (321, 93, 5, (1, 2, 3, 12), 18, 2),
    7: (841, 225, 5, (1, 28), 18, 14),
    8: (2203, 459, 7, (1, 2, 8, 16), 47, 2),
    9: (5773, 949, 7, (1, 12, 36), 47, 18),
    10: (15123, 2093, 9, (1, 2, 5, 10, 20), 123, 2),
    11: (39601, 4533, 9, (1, 44), 123, 22),
    12: (103681, 9621, 11, (1, 2, 3, 8, 12, 24), 322, 2),
}


def verify_tcsd_local_certificate() -> None:
    # Run-one subcase: 96 length-six words have no equal adjacent pair.
    run_one_words = []
    for word in product(ALPHABET, repeat=6):
        if any(word[i] == word[i + 1] for i in range(5)):
            continue
        run_one_words.append(word)
        check(
            open_iterate(word, 5)[0] == open_difference(word[2:4])[0],
            "TCSD length-six run-one identity",
        )
    check(len(run_one_words) == 96, "TCSD run-one certificate population")
    run_one_representatives = {
        (-1, 0): (4, 16, 1),
        (-1, 1): (2, 16, 1),
    }
    run_one_total = 0
    for centre, (orbit_size, expected_extensions, expected_value) in run_one_representatives.items():
        outputs = []
        for prefix in product(ALPHABET, repeat=2):
            for suffix in product(ALPHABET, repeat=2):
                word = prefix + centre + suffix
                if any(word[i] == word[i + 1] for i in range(5)):
                    continue
                outputs.append(open_iterate(word, 5)[0])
        check(len(outputs) == expected_extensions, "TCSD run-one extension count")
        check(set(outputs) == {expected_value}, "TCSD run-one constant output")
        run_one_total += orbit_size * expected_extensions
    check(run_one_total == 96, "TCSD run-one two-class coverage")

    # Lemma 2 is a genuinely finite local identity.  There are 1,344
    # length-seven words with no constant length-three factor.
    admissible = []
    for word in product(ALPHABET, repeat=7):
        if any(word[i] == word[i + 1] == word[i + 2] for i in range(5)):
            continue
        admissible.append(word)
        check(
            open_iterate(word, 6)[0] == open_iterate(word[2:5], 2)[0],
            "TCSD length-seven local identity",
        )
    check(len(admissible) == 1344, "TCSD local-certificate population")

    # Eight central-triple classes modulo order duality and reversal.  The
    # extension counts, multiplied by orbit sizes, exhaust all 1,344 cases.
    representatives = {
        (-1, -1, 0): (4, 48, 1),
        (-1, -1, 1): (4, 48, 1),
        (-1, 0, -1): (2, 64, -1),
        (-1, 0, 0): (4, 48, -1),
        (-1, 0, 1): (2, 64, 0),
        (-1, 1, -1): (2, 64, -1),
        (-1, 1, 0): (4, 64, -1),
        (0, -1, 0): (2, 64, 1),
    }
    weighted_total = 0
    for centre, (orbit_size, expected_extensions, expected_value) in representatives.items():
        outputs = []
        for prefix in product(ALPHABET, repeat=2):
            for suffix in product(ALPHABET, repeat=2):
                word = prefix + centre + suffix
                if any(word[i] == word[i + 1] == word[i + 2] for i in range(5)):
                    continue
                outputs.append(open_iterate(word, 6)[0])
        check(len(outputs) == expected_extensions, "TCSD symmetry-class extension count")
        check(set(outputs) == {expected_value}, "TCSD symmetry-class constant output")
        check(open_iterate(centre, 2)[0] == expected_value, "TCSD centre value")
        weighted_total += orbit_size * expected_extensions
    check(weighted_total == 1344, "TCSD eight-class certificate coverage")

    allowed_five_blocks = 0
    for word in product(ALPHABET, repeat=5):
        allowed_five_blocks += open_iterate(word, 4)[0] == word[2]
    check(allowed_five_blocks == 165, "TCSD core has 165 allowed five-blocks")


def verify_tcsd() -> None:
    verify_tcsd_local_certificate()
    recurrent_counts = []
    for length in range(1, 13):
        states = list(product(ALPHABET, repeat=length))
        stats = functional_stats(states, tcsd)
        expected = TCSD_EXPECTED[length]
        observed = (
            stats["image"],
            stats["recurrent"],
            stats["max_tail"],
            stats["periods"],
            stats["max_fibre"],
            stats["max_fibre_targets"],
        )
        check(observed == expected, f"TCSD full box n={length}")
        recurrent_counts.append(stats["recurrent"])

        image = set(stats["fibres"])
        for target in states:
            check((target in image) == tcsd_image_condition(target), "TCSD image language")
            check((stats["depth"][target] == 0) == in_tcsd_core(target), "TCSD core equality")
            order_bound = 4 * length // __import__("math").gcd(length, 2)
            if stats["depth"][target] == 0:
                check(iterate(tcsd, target, order_bound) == target, "TCSD core order bound")

            if length <= 10 and len(set(target)) != 1:
                run = maximum_cyclic_run(target)
                check(
                    maximum_cyclic_run(tcsd(target)) <= max(run - 1, 2),
                    "TCSD run contraction",
                )
                if run == 1:
                    check(in_tcsd_core(tcsd(target)), "TCSD run-one entry")
                if run <= 2:
                    check(in_tcsd_core(iterate(tcsd, target, 2)), "TCSD run-two entry")

        if length <= 9:
            for target, direct_count in stats["fibres"].items():
                check(tcsd_fibre_trace(target) == direct_count, "TCSD every-target trace")

        if length >= 2:
            check(
                stats["max_fibre"] == lucas(2 * (length // 2)),
                "TCSD Lucas maximum fibre",
            )
            expected_maximizers = 2 if length % 2 == 0 and length >= 4 else 2 * length
            if length == 2:
                expected_maximizers = 3
            if length == 3:
                expected_maximizers = 7
            check(stats["max_fibre_targets"] == expected_maximizers, "TCSD fibre maximizers")

        expected_tail = 1 if length == 1 else (length - 1 if length % 2 == 0 else length - 2)
        check(stats["max_tail"] == expected_tail, "TCSD parity-sharp tail")

    # Nonzero characteristic factor
    # (z-1)(z^3-z^2-2z-1)(z^3+z^2+2z+1) gives this order-seven trace recurrence.
    for index in range(7, len(recurrent_counts)):
        rhs = (
            recurrent_counts[index - 1]
            + recurrent_counts[index - 2]
            + 3 * recurrent_counts[index - 3]
            + 2 * recurrent_counts[index - 4]
            - 2 * recurrent_counts[index - 5]
            - 3 * recurrent_counts[index - 6]
            - recurrent_counts[index - 7]
        )
        check(recurrent_counts[index] == rhs, "TCSD recurrent trace recurrence")


# -------------------------------------------------------------------------
# C02: Zadeh implication on cyclic finite-chain words


def zadeh_step(word, maximum: int):
    length = len(word)
    return tuple(
        max(maximum - word[i], min(word[i], word[(i + 1) % length]))
        for i in range(length)
    )


def independent_cycle_count(length: int) -> int:
    # Lucas number L_n for n >= 2.
    return lucas(length)


def in_zadeh_core(word, maximum: int) -> bool:
    centred = tuple(2 * value - maximum for value in word)
    if maximum % 2 == 0 and all(value == 0 for value in centred):
        return True
    absolute_values = {abs(value) for value in centred}
    if len(absolute_values) != 1 or 0 in absolute_values:
        return False
    negative = {i for i, value in enumerate(centred) if value < 0}
    length = len(word)
    return all((i + 1) % length not in negative for i in negative)


ZADEH_EXPECTED = {
    2: {
        3: (5, 3, 4), 4: (8, 4, 7), 5: (12, 5, 11),
        6: (19, 6, 18), 7: (30, 7, 29), 8: (48, 8, 47),
    },
    3: {
        3: (8, 3, 5), 4: (14, 4, 10), 5: (22, 5, 18),
        6: (36, 6, 31), 7: (58, 7, 52), 8: (94, 8, 100),
    },
}


def verify_zadeh() -> None:
    for maximum in (2, 3):
        recurrent_multiplier = (maximum + 1) // 2
        epsilon = int(maximum % 2 == 0)
        for length in range(3, 9):
            states = list(product(range(maximum + 1), repeat=length))
            step = lambda word, maximum=maximum: zadeh_step(word, maximum)
            stats = functional_stats(states, step)
            expected_recurrent, expected_tail, expected_fibre = ZADEH_EXPECTED[maximum][length]
            check(stats["recurrent"] == expected_recurrent, "Zadeh recurrent box")
            check(stats["max_tail"] == expected_tail, "Zadeh sharp tail")
            check(stats["max_fibre"] == expected_fibre, "Zadeh maximum fibre box")
            check(
                expected_recurrent == recurrent_multiplier * independent_cycle_count(length) + epsilon,
                "Zadeh recurrent formula",
            )
            core = {state for state in states if in_zadeh_core(state, maximum)}
            for state in states:
                check((stats["depth"][state] == 0) == (state in core), "Zadeh core")
                check(iterate(step, state, length) in core, "Zadeh m-step attraction")


# -------------------------------------------------------------------------
# Composition controls C03 and C04


def compositions(total: int):
    if total == 0:
        yield ()
        return
    for mask in range(1 << (total - 1)):
        result = []
        previous = 0
        for cut in range(1, total):
            if mask & (1 << (cut - 1)):
                result.append(cut - previous)
                previous = cut
        result.append(total - previous)
        yield tuple(result)


def merge_marked_boundaries(parts, deleted):
    if not parts:
        return parts
    output = []
    running = parts[0]
    for boundary in range(1, len(parts)):
        if boundary in deleted:
            running += parts[boundary]
        else:
            output.append(running)
            running = parts[boundary]
    output.append(running)
    return tuple(output)


def descent_coalescence(parts):
    deleted = {i + 1 for i in range(len(parts) - 1) if parts[i] > parts[i + 1]}
    return merge_marked_boundaries(parts, deleted)


def peak_coalescence(parts):
    deleted = {
        i + 1 for i in range(1, len(parts) - 1)
        if parts[i - 1] < parts[i] > parts[i + 1]
    }
    return merge_marked_boundaries(parts, deleted)


@lru_cache(None)
def strict_decreasing_compositions(total: int):
    return tuple(parts for parts in compositions(total)
                 if all(parts[i] > parts[i + 1] for i in range(len(parts) - 1)))


def descent_fibre_formula(target) -> int:
    choices = [strict_decreasing_compositions(part) for part in target]
    count = 0

    def extend(index, previous_last):
        nonlocal count
        if index == len(choices):
            count += 1
            return
        for refinement in choices[index]:
            if previous_last is None or previous_last <= refinement[0]:
                extend(index + 1, refinement[-1])

    extend(0, None)
    return count


PDM_N16_DEPTH = (
    (0, 231), (1, 2374), (2, 6845), (3, 9095), (4, 6883),
    (5, 3946), (6, 1903), (7, 858), (8, 378), (9, 155),
    (10, 63), (11, 24), (12, 9), (13, 3), (14, 1),
)


def partition_number(total: int) -> int:
    values = [0] * (total + 1)
    values[0] = 1
    for part in range(1, total + 1):
        for value in range(part, total + 1):
            values[value] += values[value - part]
    return values[total]


def verify_composition_controls() -> None:
    for total in range(1, 17):
        states = list(compositions(total))
        stats = functional_stats(states, descent_coalescence)
        check(stats["fixed"] == partition_number(total), "PDM partition fixed count")
        check(stats["periods"] == (1,), "PDM fixed-only recurrence")
        check(stats["max_tail"] == max(0, total - 2), "PDM sharp clock")
        if total >= 3:
            deepest = [state for state, depth in stats["depth"].items() if depth == total - 2]
            check(deepest == [(2,) + (1,) * (total - 2)], "PDM unique deepest state")
        if total <= 12:
            for target, count in stats["fibres"].items():
                check(descent_fibre_formula(target) == count, "PDM every-target refinement formula")
        if total == 16:
            check(stats["image"] == 10747, "PDM N=16 image")
            check(stats["depth_hist"] == PDM_N16_DEPTH, "PDM N=16 depth histogram")
            check(stats["max_fibre"] == 37, "PDM N=16 maximum fibre")

    for total in range(3, 19):
        states = list(compositions(total))
        stats = functional_stats(states, peak_coalescence)
        check(stats["periods"] == (1,), "peak coalescence fixed-only")
        check(stats["max_tail"] == max(0, total - 3), "peak coalescence clock")
        if total >= 4:
            deepest = [state for state, depth in stats["depth"].items() if depth == total - 3]
            check(deepest == [(1, 2) + (1,) * (total - 3)], "peak unique deepest state")
        if total == 18:
            check((stats["image"], stats["fixed"], stats["max_fibre"]) == (54100, 9167, 26),
                  "peak N=18 terminal box")


# -------------------------------------------------------------------------
# C05: least row-reading descent swap on all standard Young tableaux


def standard_young_tableaux(size: int):
    level = [((), ())]
    for _label in range(1, size + 1):
        next_level = []
        for shape, cells in level:
            for row in range(len(shape) + 1):
                if row == len(shape):
                    next_level.append((shape + (1,), cells + ((row, 0),)))
                elif row == 0 or shape[row] < shape[row - 1]:
                    new_shape = list(shape)
                    cell = (row, new_shape[row])
                    new_shape[row] += 1
                    next_level.append((tuple(new_shape), cells + (cell,)))
        level = next_level
    return [cells for _shape, cells in level]


def tableau_descent_swap(cells):
    cells = list(cells)
    for index in range(len(cells) - 1):
        left, right = cells[index], cells[index + 1]
        comparable = ((left[0] <= right[0] and left[1] <= right[1]) or
                      (right[0] <= left[0] and right[1] <= left[1]))
        if not comparable and left > right:
            cells[index], cells[index + 1] = cells[index + 1], cells[index]
            break
    return tuple(cells)


def verify_tableau_control() -> None:
    expected = {
        6: (76, 52, 11, 6, 3),
        7: (232, 158, 15, 9, 4),
        8: (764, 518, 22, 13, 4),
        9: (2620, 1772, 30, 17, 5),
        10: (9496, 6408, 42, 22, 5),
    }
    for size in range(1, 11):
        states = standard_young_tableaux(size)
        stats = functional_stats(states, tableau_descent_swap)
        check(stats["periods"] == (1,), "tableau sorter fixed-only")
        if size in expected:
            check((stats["states"], stats["image"], stats["fixed"],
                   stats["max_tail"], stats["max_fibre"]) == expected[size],
                  "tableau terminal boxes")


# -------------------------------------------------------------------------
# C06/C07/C08: finite Heyting-lattice controls


def fence_ideals(size: int):
    down = []
    for vertex in range(size):
        mask = 1 << vertex
        if vertex % 2 == 1:
            mask |= 1 << (vertex - 1)
            if vertex + 1 < size:
                mask |= 1 << (vertex + 1)
        down.append(mask)
    ideals = [
        mask for mask in range(1 << size)
        if all(not (mask >> vertex) & 1 or not (down[vertex] & ~mask)
               for vertex in range(size))
    ]
    return ideals, down


def fence_negation(mask: int, down, size: int) -> int:
    return sum(1 << vertex for vertex in range(size) if not (down[vertex] & mask))


def star_ideals(leaves: int):
    return [0] + [1 | (subset << 1) for subset in range(1 << leaves)]


def star_implication(left: int, right: int, leaves: int) -> int:
    output = 0
    for vertex in range(leaves + 1):
        down = 1 if vertex == 0 else 1 | (1 << vertex)
        if not ((down & left) & ~right):
            output |= 1 << vertex
    return output


def verify_lattice_controls() -> None:
    ideals, down = fence_ideals(20)
    step = lambda mask: fence_negation(mask, down, 20)
    stats = functional_stats(ideals, step)
    check((stats["states"], stats["image"], stats["recurrent"], stats["max_tail"],
           stats["periods"], stats["max_fibre"]) == (17711, 1024, 1024, 1, (2,), 1024),
          "fence pseudocomplement n=20")
    for mask in ideals:
        check(iterate(step, mask, 3) == step(mask), "Heyting negation cube identity")

    leaves, length = 3, 4
    ideals = star_ideals(leaves)
    states = list(product(ideals, repeat=length))
    implication_step = lambda word: tuple(
        star_implication(word[i], word[(i + 1) % length], leaves) for i in range(length)
    )
    stats = functional_stats(states, implication_step)
    check((stats["states"], stats["image"], stats["recurrent"], stats["max_tail"],
           stats["cycles"], stats["max_fibre"]) ==
          (6561, 453, 453, 1, ((1, 1), (2, 14), (4, 106)), 99),
          "star-Heyting cyclic implication")
    for state in states:
        check(iterate(implication_step, state, 2) == rotate_left(implication_step(state), 1),
              "star-Heyting T2=shift T")

    leaves = 4
    ideals = star_ideals(leaves)
    states = list(product(ideals, repeat=2))
    pair_step = lambda pair: (
        pair[0] & pair[1], star_implication(pair[0], pair[1], leaves)
    )
    stats = functional_stats(states, pair_step)
    check((stats["states"], stats["image"], stats["fixed"], stats["max_tail"],
           stats["max_fibre"]) == (289, 83, 17, 2, 17),
          "Heyting meet-residuum pair")
    top = (1 << (leaves + 1)) - 1
    for pair in states:
        check(iterate(pair_step, pair, 2) == (pair[0] & pair[1], top),
              "Heyting pair square normal form")


# -------------------------------------------------------------------------
# C09: Boolean elementary-symmetric tuple normal form


def elementary_symmetric_tuple(word, width: int):
    length = len(word)
    output = []
    for degree in range(1, length + 1):
        value = 0
        for bit in range(width):
            weight = sum((entry >> bit) & 1 for entry in word)
            if comb(weight, degree) & 1:
                value |= 1 << bit
        output.append(value)
    return tuple(output)


def verify_elementary_symmetric_control() -> None:
    length, width = 5, 2
    states = list(product(range(1 << width), repeat=length))
    step = lambda word: elementary_symmetric_tuple(word, width)
    stats = functional_stats(states, step)
    check((stats["states"], stats["image"], stats["fixed"], stats["max_tail"],
           stats["depth_hist"], stats["max_fibre"]) ==
          (1024, 36, 9, 2, ((0, 9), (1, 247), (2, 768)), 100),
          "Boolean elementary-symmetric tuple")


# -------------------------------------------------------------------------
# C10: Kleene--Dienes cyclic implication


def kleene_dienes_step(word, maximum: int):
    length = len(word)
    return tuple(max(maximum - word[i], word[(i + 1) % length]) for i in range(length))


def verify_kleene_dienes_control() -> None:
    maximum, length = 3, 5
    states = list(product(range(maximum + 1), repeat=length))
    step = lambda word: kleene_dienes_step(word, maximum)
    stats = functional_stats(states, step)
    check((stats["states"], stats["image"], stats["recurrent"], stats["max_tail"],
           stats["cycles"], stats["max_fibre"]) ==
          (1024, 197, 197, 1, ((1, 2), (5, 39)), 10),
          "Kleene-Dienes chain word")
    for state in states:
        check(iterate(step, state, 2) == rotate_left(step(state), 1), "KD T2=shift T")


# -------------------------------------------------------------------------
# C11: strict-lower-set inclusion on labelled posets


def labelled_posets(size: int):
    pairs = list(combinations(range(size), 2))
    for choices in product((-1, 0, 1), repeat=len(pairs)):
        down = [0] * size
        for (left, right), choice in zip(pairs, choices):
            if choice == 0:
                down[right] |= 1 << left
            elif choice == 1:
                down[left] |= 1 << right
        if all(not ((down[upper] >> lower) & 1) or not (down[lower] & ~down[upper])
               for upper in range(size) for lower in range(size)):
            yield tuple(down)


def lower_set_inclusion(poset):
    size = len(poset)
    output = [0] * size
    for upper in range(size):
        for lower in range(size):
            if lower != upper and poset[lower] != poset[upper] and not (poset[lower] & ~poset[upper]):
                output[upper] |= 1 << lower
    return tuple(output)


def verify_poset_control() -> None:
    expected = {
        1: (1, 1, 1, 0, 1),
        2: (3, 3, 3, 0, 1),
        3: (19, 13, 13, 1, 3),
        4: (219, 75, 75, 1, 7),
        5: (4231, 601, 541, 2, 31),
    }
    for size in range(1, 6):
        states = list(labelled_posets(size))
        stats = functional_stats(states, lower_set_inclusion)
        check((stats["states"], stats["image"], stats["recurrent"],
               stats["max_tail"], stats["max_fibre"]) == expected[size],
              "lower-set inclusion poset box")


# -------------------------------------------------------------------------
# C12: complement after column erosion in a partition box


def boxed_partitions(rows: int, columns: int):
    return [tuple(reversed(parts))
            for parts in combinations_with_replacement(range(columns + 1), rows)]


def complement_after_erosion(partition, columns: int):
    eroded = tuple(max(part - 1, 0) for part in partition)
    return tuple(columns - eroded[-1 - i] for i in range(len(partition)))


def verify_boxed_partition_control() -> None:
    rows = columns = 5
    states = boxed_partitions(rows, columns)
    step = lambda partition: complement_after_erosion(partition, columns)
    stats = functional_stats(states, step)
    check((stats["states"], stats["image"], stats["recurrent"], stats["max_tail"],
           stats["periods"], stats["max_fibre"]) == (252, 126, 126, 1, (1, 2), 6),
          "boxed partition complement erosion")


def main() -> None:
    verify_tcsd()
    verify_zadeh()
    verify_composition_controls()
    verify_tableau_control()
    verify_lattice_controls()
    verify_elementary_symmetric_control()
    verify_kleene_dienes_control()
    verify_poset_control()
    verify_boxed_partition_control()
    print("WORD_POSET_LANE_OK")
    print(f"assertions={ASSERTIONS}")
    print("ranked_candidates=12")
    print("recommendations=1")
    print("recommendation_1=TCSD_PROMOTE_SPIKE_OWNER_AMBER_HOLD_EXTERNAL")
    print("reserve_1=ZADEH_RESERVE_OWNER_RED_AMBER_HOLD_EXTERNAL")
    print("composition_disposition=KILL_SORTING_COALESCENCE")


if __name__ == "__main__":
    main()
