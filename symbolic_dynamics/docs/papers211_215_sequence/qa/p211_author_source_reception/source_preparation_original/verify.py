"""Standalone P211 author verifier; no pilot/reviewer imports or file writes.

This source has no scientific top-level work. A separately authorized
recorded production may invoke main; the program does not create, adopt,
read or overwrite CANONICAL.json. Runtime provenance belongs to the outer
reviewed recorder, not to the deterministic mathematical stdout.
"""
import itertools
import json
import math
import sys


EXPECTED_PARAMETERS = {
    "schema": "p211-author-parameters-v1",
    "canonical_schema": "p211-author-kip-v1",
    "n_values": [1, 2, 3, 4, 5, 6, 7],
    "carrier": "all_nondecreasing_maps_[n]_to_[n]",
    "carrier_sizes": [1, 3, 10, 35, 126, 462, 1716],
    "total_states": 2353,
    "update": "T(f)=e_kernel_right_endpoints(f)_composed_with_e_(image(f)_union_{n})",
    "composition": "right_factor_first_supports_recomputed_each_epoch",
    "predicates": [
        "C1_literal_closure",
        "C2_recurrence_and_terminal",
        "C3_pointwise_and_sharp_height",
        "C4_complete_image",
        "C5_every_predecessor",
        "C6_laurent_fibres_and_mass",
        "C7_exact_endpoint_peeling",
    ],
    "ordering": "n_ascending_then_source_tuple_lexicographic_all_sets_and_predecessors_sorted",
    "serialization": "one_JSON_object_sort_keys_true_ensure_ascii_true_compact_separators_plus_LF",
    "excluded_claims": [
        "global_maximum_fibre_or_maximizers",
        "basin_counts",
        "all_time_inverse",
        "global_priority_or_no_factor_theorem",
    ],
}


def read_parameters():
    if len(sys.argv) != 3 or sys.argv[1] != "--parameters" or not sys.argv[2].startswith("/"):
        raise ValueError("use verify.py --parameters <absolute-parameter-file>")
    if not (sys.flags.isolated == 1 and sys.flags.no_site == 1
            and sys.flags.dont_write_bytecode == 1 and sys.flags.optimize == 0):
        raise RuntimeError("require system Python -I -S -B with optimization zero")
    with open(sys.argv[2], "r", encoding="utf-8") as stream:
        parameters = json.load(stream)
    if parameters != EXPECTED_PARAMETERS:
        raise ValueError("parameter document differs from the complete approved specification")
    return parameters


def endpoints_and_values(function):
    n = len(function)
    endpoints = tuple(i for i in range(1, n) if function[i - 1] != function[i]) + (n,)
    values = tuple(function[i - 1] for i in endpoints)
    return endpoints, values


def ceiling_values(sites, n):
    return tuple(next(site for site in sites if site >= i) for i in range(1, n + 1))


def literal_successor(function):
    n = len(function)
    endpoints, _ = endpoints_and_values(function)
    completed_image = tuple(sorted(set(function) | {n}))
    first = ceiling_values(completed_image, n)
    second = ceiling_values(endpoints, n)
    return tuple(second[value - 1] for value in first)


def from_coordinates(values, endpoints):
    output = []
    previous = 0
    for value, endpoint in zip(values, endpoints):
        output.extend([value] * (endpoint - previous))
        previous = endpoint
    return tuple(output)


def image_condition(function):
    endpoints, values = endpoints_and_values(function)
    n = len(function)
    return (values[-1] == endpoints[-1] == n
            and all(w <= z for w, z in zip(endpoints, values))
            and all(values[i] < endpoints[i + 1] for i in range(len(endpoints) - 1)))


def anchor_blocks(function):
    if not image_condition(function):
        raise ValueError("anchor blocks are defined only on the first image")
    endpoints, values = endpoints_and_values(function)
    blocks = []
    labels = []
    for endpoint, value in zip(endpoints, values):
        if endpoint == value:
            blocks.append({"anchor": endpoint, "endpoints": labels})
            labels = []
        else:
            labels.extend([endpoint, value])
    if labels:
        raise AssertionError("image target is missing its final anchor")
    return blocks


def remaining_clock(function):
    return max((len(block["endpoints"]) // 2 for block in anchor_blocks(function)), default=0)


def peeled_successor(function):
    new_endpoints = []
    new_values = []
    for block in anchor_blocks(function):
        interior = block["endpoints"][1:-1]
        new_endpoints.extend(interior[::2])
        new_values.extend(interior[1::2])
        new_endpoints.append(block["anchor"])
        new_values.append(block["anchor"])
    return from_coordinates(new_values, new_endpoints)


def finite_orbit(source, successors):
    path = []
    first_seen = {}
    current = source
    while current not in first_seen:
        if current not in successors:
            raise AssertionError("literal orbit left the enumerated carrier")
        first_seen[current] = len(path)
        path.append(current)
        current = successors[current]
    entry = first_seen[current]
    return path, entry, path[entry:]


def all_gap_choices(gap):
    choices = []
    for size in range(len(gap) + 1):
        for selected in itertools.combinations(gap, size):
            for split in range(size + 1):
                choices.append((selected[:split], selected[split:]))
    return choices


def decoded_predecessors(target):
    if not image_condition(target):
        return []
    endpoints, values = endpoints_and_values(target)
    previous_values = (0,) + values[:-1]
    gaps = [tuple(range(previous + 1, endpoint))
            for previous, endpoint in zip(previous_values, endpoints)]
    decoded = []
    for choices in itertools.product(*(all_gap_choices(gap) for gap in gaps)):
        source_endpoints = set(values)
        completed_image = set(endpoints)
        for extra_endpoints, extra_image in choices:
            source_endpoints.update(extra_endpoints)
            completed_image.update(extra_image)
        difference = len(completed_image) - len(source_endpoints)
        if difference not in (0, 1):
            continue
        source_image = completed_image if difference == 0 else completed_image - {len(target)}
        if len(source_image) != len(source_endpoints) or not source_image:
            raise AssertionError("decoded support-rank branch is invalid")
        decoded.append(from_coordinates(sorted(source_image), sorted(source_endpoints)))
    return sorted(decoded)


def laurent_polynomial(target):
    if not image_condition(target):
        return []
    endpoints, values = endpoints_and_values(target)
    polynomial = {0: 1}
    for previous, endpoint in zip((0,) + values[:-1], endpoints):
        d = endpoint - previous - 1
        factor = {}
        for a in range(d + 1):
            for b in range(d - a + 1):
                exponent = b - a
                factor[exponent] = factor.get(exponent, 0) + math.comb(d, a + b)
        updated = {}
        for left, multiplicity in sorted(polynomial.items()):
            for right, count in sorted(factor.items()):
                exponent = left + right
                updated[exponent] = updated.get(exponent, 0) + multiplicity * count
        polynomial = updated
    return [[exponent, coefficient] for exponent, coefficient in sorted(polynomial.items())]


def sharp_source(n):
    if n == 1:
        return (1,)
    if n % 2:
        endpoints = tuple(range(2, n, 2)) + (n,)
        values = tuple(range(1, n - 1, 2)) + (n,)
    else:
        endpoints = tuple(range(2, n + 1, 2))
        values = tuple(range(1, n, 2))
    return from_coordinates(values, endpoints)


def verify_box(n, declared_size, predicate_names):
    counts = {name: 0 for name in predicate_names}

    def check(index, condition, context):
        category = predicate_names[index - 1]
        if not condition:
            raise AssertionError((category, n, context))
        counts[category] += 1

    states = list(itertools.combinations_with_replacement(range(1, n + 1), n))
    state_set = set(states)
    check(1, len(states) == len(state_set) == declared_size == math.comb(2 * n - 1, n), "full carrier census")
    successors = {state: literal_successor(state) for state in states}
    for state in states:
        check(1, successors[state] in state_set, state)
    reverse = {state: [] for state in states}
    for state in states:
        reverse[successors[state]].append(state)
    orbit_data = {state: finite_orbit(state, successors) for state in states}
    records = []
    all_fixed = []
    all_recurrent = []
    for state in states:
        endpoints, values = endpoints_and_values(state)
        completed_image = tuple(sorted(set(values) | {n}))
        predicted_anchors = tuple(sorted(set(endpoints) & set(completed_image)))
        predicted_terminal = ceiling_values(predicted_anchors, n)
        path, entry, cycle = orbit_data[state]
        is_fixed = successors[state] == state
        if is_fixed:
            all_fixed.append(state)
        if entry == 0:
            all_recurrent.append(state)
        check(2, len(cycle) == 1 and cycle[0] == predicted_terminal
              and is_fixed == (endpoints == values), state)
        predicted_height = 0 if endpoints == values else 1 + remaining_clock(successors[state])
        check(3, entry == predicted_height, state)
        in_image = image_condition(state)
        check(4, bool(reverse[state]) == in_image, state)
        decoded = decoded_predecessors(state)
        check(5, decoded == reverse[state] and len(decoded) == len(set(decoded)), state)
        polynomial = laurent_polynomial(state)
        coefficients = dict(polynomial)
        formula_count = coefficients.get(0, 0) + coefficients.get(1, 0)
        check(6, formula_count == len(reverse[state]), state)
        blocks = anchor_blocks(state) if in_image else None
        peeled = peeled_successor(state) if in_image else None
        if in_image:
            next_blocks = anchor_blocks(successors[state])
            check(7, peeled == successors[state]
                  and [block["anchor"] for block in blocks] == [block["anchor"] for block in next_blocks]
                  and remaining_clock(successors[state]) == max(remaining_clock(state) - 1, 0), state)
        records.append({
            "source": list(state), "kernel_endpoints": list(endpoints),
            "image_values": list(values), "completed_image": list(completed_image),
            "successor": list(successors[state]), "fixed": is_fixed,
            "recurrent": entry == 0, "in_image": in_image,
            "orbit": [list(item) for item in path], "cycle_start": entry,
            "cycle": [list(item) for item in cycle], "terminal": list(cycle[0]),
            "predicted_terminal": list(predicted_terminal), "height": entry,
            "predicted_height": predicted_height,
            "predecessors": [list(item) for item in reverse[state]],
            "decoded_predecessors": [list(item) for item in decoded],
            "fibre_count": len(reverse[state]), "laurent_count": formula_count,
            "laurent_coefficients": polynomial, "anchor_blocks": blocks,
            "peeled_successor": list(peeled) if peeled is not None else None,
        })
    predicted_fixed = []
    for size in range(n):
        for subset in itertools.combinations(range(1, n), size):
            predicted_fixed.append(ceiling_values(subset + (n,), n))
    check(2, all_fixed == all_recurrent == sorted(predicted_fixed), "complete recurrent/fixed set")
    height = max(data[1] for data in orbit_data.values())
    theorem_height = 0 if n == 1 else (n + 1) // 2
    witness = sharp_source(n)
    check(3, witness in state_set and orbit_data[witness][1] == height == theorem_height, "sharp parity witness")
    inverse_mass = sum(row["laurent_count"] for row in records)
    check(6, inverse_mass == len(states), "complete inverse mass")
    return {
        "n": n, "carrier_size": len(states), "state_records": records,
        "image_count": sum(row["in_image"] for row in records),
        "fixed_count": len(all_fixed), "recurrent_count": len(all_recurrent),
        "maximum_height": height, "theorem_height": theorem_height,
        "sharp_witness": list(witness), "inverse_mass": inverse_mass,
        "assertions": counts,
    }


def main():
    parameters = read_parameters()
    names = parameters["predicates"]
    boxes = [verify_box(n, size, names)
             for n, size in zip(parameters["n_values"], parameters["carrier_sizes"])]
    totals = {name: sum(box["assertions"][name] for box in boxes) for name in names}
    total_states = sum(box["carrier_size"] for box in boxes)
    if total_states != parameters["total_states"]:
        raise AssertionError("complete state count disagrees with parameters")
    result = {
        "schema": parameters["canonical_schema"], "parameters": parameters,
        "box_count": len(boxes), "total_states": total_states,
        "assertions": totals, "checks": sum(totals.values()), "boxes": boxes,
    }
    sys.stdout.write(json.dumps(result, sort_keys=True, ensure_ascii=True, separators=(",", ":")) + "\n")


if __name__ == "__main__":
    main()
