#!/usr/bin/env python3
"""Exact verifier for C02 multipartite synchronous-mex fibres.

For K_{a_1,...,a_k}, a colouring uses the palette {0,...,q-1}, where
q >= Delta+1.  One synchronous open-neighbourhood mex round collapses each
part to one value y_i.  This script independently computes every one-step
fibre in three ways:

1. brute force over vertex colourings;
2. inclusion-exclusion over missing lower-colour witnesses;
3. support enumeration with onto-function weights.

It also verifies the recurrent-target product formulas, the two-round global
collapse, exact depth layers, quotient preimage descriptions, and basin
counts.  Only Python's standard library is used.
"""

from collections import Counter, defaultdict
from itertools import permutations, product
from math import comb, factorial, prod


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def mex(values):
    values = set(values)
    value = 0
    while value in values:
        value += 1
    return value


def canonical_palette_size(sizes):
    """Return Delta(K_{a_1,...,a_k})+1."""
    return sum(sizes) - min(sizes) + 1


def blocks_and_outsides(sizes):
    blocks = []
    start = 0
    for size in sizes:
        block = tuple(range(start, start + size))
        blocks.append(block)
        start += size
    all_vertices = set(range(start))
    outsides = [tuple(sorted(all_vertices.difference(block))) for block in blocks]
    return tuple(blocks), tuple(outsides)


def graph_target(colouring, outsides):
    """Identify the part-monochromatic graph image with its k-vector."""
    return tuple(mex(colouring[v] for v in outside) for outside in outsides)


def quotient_step(state):
    return tuple(
        mex(state[j] for j in range(len(state)) if j != i)
        for i in range(len(state))
    )


def part_state_if_monochromatic(colouring, blocks):
    values = []
    for block in blocks:
        block_values = {colouring[v] for v in block}
        if len(block_values) != 1:
            return None
        values.append(next(iter(block_values)))
    return tuple(values)


def recurrent_records(k):
    fixed = tuple(permutations(range(k)))
    two_cycles = []
    state_to_orbit = {}

    for state in fixed:
        key = ("fixed", state)
        state_to_orbit[state] = key

    for m in range(max(0, k - 1)):
        for low_parts in permutations(range(k), m):
            minus = [m] * k
            plus = [m + 1] * k
            for colour, part in enumerate(low_parts):
                minus[part] = colour
                plus[part] = colour
            minus = tuple(minus)
            plus = tuple(plus)
            key = ("two", m, low_parts)
            check(minus not in state_to_orbit, f"duplicate recurrent state {minus}")
            check(plus not in state_to_orbit, f"duplicate recurrent state {plus}")
            state_to_orbit[minus] = key
            state_to_orbit[plus] = key
            two_cycles.append((m, low_parts, minus, plus, key))

    return fixed, tuple(two_cycles), state_to_orbit


def fibre_inclusion_exclusion(sizes, q, target):
    """Exact formula from the bad events 'r is absent outside part i'."""
    k = len(sizes)
    required = tuple(
        (i, colour)
        for i, value in enumerate(target)
        for colour in range(value)
    )
    base = [
        {target[i] for i in range(k) if i != part}
        for part in range(k)
    ]
    total = 0
    for mask in range(1 << len(required)):
        forbidden = [set(values) for values in base]
        parity = 0
        for bit, (part, colour) in enumerate(required):
            if mask & (1 << bit):
                parity ^= 1
                for other_part in range(k):
                    if other_part != part:
                        forbidden[other_part].add(colour)
        term = prod(
            (q - len(forbidden[part])) ** sizes[part]
            for part in range(k)
        )
        total += -term if parity else term
    return total


def onto_count(objects, labelled_boxes):
    if labelled_boxes == 0:
        return int(objects == 0)
    if labelled_boxes > objects:
        return 0
    return sum(
        (-1) ** omitted
        * comb(labelled_boxes, omitted)
        * (labelled_boxes - omitted) ** objects
        for omitted in range(labelled_boxes + 1)
    )


def support_weighted_fibres(sizes, q):
    """Second exact route: enumerate colour supports and weight by surjections."""
    k = len(sizes)
    all_parts_mask = (1 << k) - 1
    result = Counter()
    support_choices = range(1 << k)

    for supports in product(support_choices, repeat=q):
        active_counts = [
            sum(bool(mask & (1 << part)) for mask in supports)
            for part in range(k)
        ]
        weights = [
            onto_count(sizes[part], active_counts[part])
            for part in range(k)
        ]
        if not all(weights):
            continue

        target = []
        for part in range(k):
            outside_mask = all_parts_mask ^ (1 << part)
            for colour, support in enumerate(supports):
                if not support & outside_mask:
                    target.append(colour)
                    break
            else:
                raise AssertionError(
                    "positive support weight covered the whole q-palette outside a part"
                )
        result[tuple(target)] += prod(weights)
    return result


def brute_case(sizes, q):
    blocks, outsides = blocks_and_outsides(sizes)
    fixed, two_cycles, state_to_orbit = recurrent_records(len(sizes))
    recurrent = set(state_to_orbit)
    fibres = Counter()
    depths = Counter()
    basin_depths = Counter()

    for colouring in product(range(q), repeat=sum(sizes)):
        target = graph_target(colouring, outsides)
        fibres[target] += 1
        check(all(0 <= value < q for value in target), "graph mex escaped palette")

        if len(sizes) >= 2:
            multiplicities = Counter(target)
            repeated = {value for value, count in multiplicities.items() if count >= 2}
            check(
                not repeated or repeated == {max(target)},
                f"repeated nonmaximum output: sizes={sizes}, target={target}",
            )

        second = quotient_step(target)
        check(
            second in recurrent,
            f"two-round collapse failed: sizes={sizes}, target={target}, T(target)={second}",
        )
        orbit = state_to_orbit[second]
        part_state = part_state_if_monochromatic(colouring, blocks)
        if part_state in recurrent:
            depth = 0
        elif target in recurrent:
            depth = 1
        else:
            depth = 2
        depths[depth] += 1
        basin_depths[(orbit, depth)] += 1

    return {
        "fibres": fibres,
        "depths": depths,
        "basin_depths": basin_depths,
        "fixed": fixed,
        "two_cycles": two_cycles,
        "state_to_orbit": state_to_orbit,
    }


def fixed_fibre_formula(sizes, q, state):
    k = len(sizes)
    check(tuple(sorted(state)) == tuple(range(k)), f"not a fixed permutation: {state}")
    part_for_colour = tuple(state.index(colour) for colour in range(k))
    high = q - k
    value = 1
    for colour in range(k - 1):
        size = sizes[part_for_colour[colour]]
        value *= (high + 1) ** size - high**size
    value *= (high + 1) ** sizes[part_for_colour[k - 1]]
    return value


def minus_fibre_formula(sizes, q, m, low_parts):
    low_parts = tuple(low_parts)
    remaining = set(range(len(sizes))).difference(low_parts)
    high = q - m - 1
    value = prod(
        (high + 1) ** sizes[part] - high ** sizes[part]
        for part in low_parts
    )
    value *= high ** sum(sizes[part] for part in remaining)
    return value


def plus_fibre_formula(sizes, q, m, low_parts):
    low_parts = tuple(low_parts)
    remaining = tuple(sorted(set(range(len(sizes))).difference(low_parts)))
    high = q - m - 2
    remaining_size = sum(sizes[part] for part in remaining)

    low_allow_m = prod(
        (high + 2) ** sizes[part] - (high + 1) ** sizes[part]
        for part in low_parts
    )
    low_exclude_m = prod(
        (high + 1) ** sizes[part] - high ** sizes[part]
        for part in low_parts
    )
    remaining_any = (high + 1) ** remaining_size
    remaining_spans_two = remaining_any - high**remaining_size
    remaining_spans_two -= sum(
        ((high + 1) ** sizes[part] - high ** sizes[part])
        * high ** (remaining_size - sizes[part])
        for part in remaining
    )
    return (
        (low_allow_m - low_exclude_m) * remaining_any
        + low_exclude_m * remaining_spans_two
    )


def fixed_preimages(state, q):
    k = len(state)
    max_part = state.index(k - 1)
    answer = set()
    for replacement in range(k - 1, q):
        target = list(state)
        target[max_part] = replacement
        answer.add(tuple(target))
    return answer


def minus_preimages(k, q, m, low_parts):
    low_parts = tuple(low_parts)
    remaining = tuple(sorted(set(range(k)).difference(low_parts)))
    answer = set()
    for values in product(range(m + 1, q), repeat=len(remaining)):
        target = [None] * k
        for colour, part in enumerate(low_parts):
            target[part] = colour
        for part, value in zip(remaining, values):
            target[part] = value
        answer.add(tuple(target))
    return answer


def plus_preimages(k, q, m, low_parts):
    low_parts = tuple(low_parts)
    remaining = tuple(sorted(set(range(k)).difference(low_parts)))
    choices = (m,) + tuple(range(m + 2, q))
    answer = set()
    for values in product(choices, repeat=len(remaining)):
        if values.count(m) < 2:
            continue
        target = [None] * k
        for colour, part in enumerate(low_parts):
            target[part] = colour
        for part, value in zip(remaining, values):
            target[part] = value
        answer.add(tuple(target))
    return answer


def verify_case(sizes, q):
    canonical = canonical_palette_size(sizes)
    check(q >= canonical, f"palette q={q} is below Delta+1={canonical}")
    data = brute_case(sizes, q)
    fibres = data["fibres"]
    support_fibres = support_weighted_fibres(sizes, q)
    k = len(sizes)

    for target in product(range(q), repeat=k):
        brute = fibres[target]
        ie = fibre_inclusion_exclusion(sizes, q, target)
        support = support_fibres[target]
        check(
            brute == ie,
            f"IE fibre mismatch: sizes={sizes}, q={q}, y={target}: {brute}!={ie}",
        )
        check(
            brute == support,
            f"support fibre mismatch: sizes={sizes}, q={q}, y={target}: "
            f"{brute}!={support}",
        )

    all_quotient_states = tuple(product(range(q), repeat=k))
    h_values = {}
    orbit_states = defaultdict(list)

    for state in data["fixed"]:
        explicit = fixed_fibre_formula(sizes, q, state)
        check(
            fibres[state] == explicit,
            f"fixed fibre formula failed: sizes={sizes}, q={q}, state={state}",
        )
        expected = fixed_preimages(state, q)
        actual = {target for target in all_quotient_states if quotient_step(target) == state}
        check(
            actual == expected,
            f"fixed quotient preimages failed: sizes={sizes}, q={q}, state={state}",
        )
        h_values[state] = sum(fibres[target] for target in expected)
        orbit_states[data["state_to_orbit"][state]].append(state)

    for m, low_parts, minus, plus, orbit in data["two_cycles"]:
        explicit_minus = minus_fibre_formula(sizes, q, m, low_parts)
        explicit_plus = plus_fibre_formula(sizes, q, m, low_parts)
        check(
            fibres[minus] == explicit_minus,
            f"minus fibre formula failed: sizes={sizes}, q={q}, state={minus}",
        )
        check(
            fibres[plus] == explicit_plus,
            f"plus fibre formula failed: sizes={sizes}, q={q}, state={plus}",
        )

        expected_minus = minus_preimages(k, q, m, low_parts)
        expected_plus = plus_preimages(k, q, m, low_parts)
        actual_minus = {
            target for target in all_quotient_states if quotient_step(target) == minus
        }
        actual_plus = {
            target for target in all_quotient_states if quotient_step(target) == plus
        }
        check(
            actual_minus == expected_minus,
            f"minus quotient preimages failed: sizes={sizes}, q={q}, state={minus}",
        )
        check(
            actual_plus == expected_plus,
            f"plus quotient preimages failed: sizes={sizes}, q={q}, state={plus}",
        )
        h_values[minus] = sum(fibres[target] for target in expected_minus)
        h_values[plus] = sum(fibres[target] for target in expected_plus)
        orbit_states[orbit].extend((minus, plus))

    recurrent = set(data["state_to_orbit"])
    expected_recurrent_count = factorial(k) + 2 * sum(
        factorial(k) // factorial(k - m)
        for m in range(max(0, k - 1))
    )
    check(
        len(recurrent) == expected_recurrent_count,
        f"recurrent count failed at k={k}",
    )

    recurrent_fibre_mass = sum(fibres[state] for state in recurrent)
    explicit_recurrent_mass = sum(
        fixed_fibre_formula(sizes, q, state) for state in data["fixed"]
    )
    explicit_recurrent_mass += sum(
        minus_fibre_formula(sizes, q, m, low_parts)
        + plus_fibre_formula(sizes, q, m, low_parts)
        for m, low_parts, _minus, _plus, _orbit in data["two_cycles"]
    )
    check(
        recurrent_fibre_mass == explicit_recurrent_mass,
        f"explicit recurrent mass failed: sizes={sizes}, q={q}",
    )
    expected_depths = Counter(
        {
            0: len(recurrent),
            1: recurrent_fibre_mass - len(recurrent),
            2: q ** sum(sizes) - recurrent_fibre_mass,
        }
    )
    check(
        data["depths"] == expected_depths,
        f"depth law failed: sizes={sizes}, q={q}: "
        f"{data['depths']}!={expected_depths}",
    )

    for orbit, states in orbit_states.items():
        basin = sum(h_values[state] for state in states)
        direct_fibre_mass = sum(fibres[state] for state in states)
        expected_layers = {
            0: len(states),
            1: direct_fibre_mass - len(states),
            2: basin - direct_fibre_mass,
        }
        for depth, expected in expected_layers.items():
            check(
                data["basin_depths"][(orbit, depth)] == expected,
                f"basin layer failed: sizes={sizes}, q={q}, "
                f"orbit={orbit}, depth={depth}",
            )

    check(
        sum(data["basin_depths"].values()) == q ** sum(sizes),
        f"basins do not partition phase space: sizes={sizes}, q={q}",
    )
    return {
        "sizes": sizes,
        "q": q,
        "states": q ** sum(sizes),
        "nonzero_fibres": len(fibres),
        "recurrent_states": len(recurrent),
        "depths": tuple(data["depths"][depth] for depth in range(3)),
        "orbit_count": len(orbit_states),
        "fibres": fibres,
        "h_values": h_values,
        "orbit_states": orbit_states,
    }


def main():
    cases = (
        ((1,), 1),
        ((2,), 1),
        ((2,), 3),
        ((1, 1), 2),
        ((1, 1), 4),
        ((1, 2), 3),
        ((1, 2), 4),
        ((2, 2), 3),
        ((2, 2), 4),
        ((1, 1, 1), 3),
        ((1, 1, 2), 4),
        ((1, 2, 2), 5),
        ((2, 2, 2), 5),
        ((1, 2, 3), 6),
        ((1, 1, 1, 1), 4),
    )
    results = [verify_case(sizes, q) for sizes, q in cases]

    print("C02 MULTIPARTITE SYNCHRONOUS-MEX FIBRES")
    for result in results:
        print(
            "parts={sizes} q={q} states={states} nonzero_fibres={nonzero_fibres} "
            "recurrent_states={recurrent_states} depths={depths} "
            "basins={orbit_count}".format(**result)
        )

    example = next(
        result
        for result in results
        if result["sizes"] == (1, 2) and result["q"] == 3
    )
    fibres = example["fibres"]
    h_values = example["h_values"]
    cycle_basin = h_values[(0, 0)] + h_values[(1, 1)]
    print(
        "K_(1,2)_q3 recurrent_fibres="
        f"00:{fibres[(0, 0)]},11:{fibres[(1, 1)]},"
        f"01:{fibres[(0, 1)]},10:{fibres[(1, 0)]}"
    )
    print(
        "K_(1,2)_q3 basin_sizes="
        f"fixed01:{h_values[(0, 1)]},fixed10:{h_values[(1, 0)]},"
        f"uniform_two_cycle:{cycle_basin}"
    )
    print(f"assertions={ASSERTIONS}")


if __name__ == "__main__":
    main()
