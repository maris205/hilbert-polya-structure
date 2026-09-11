"""Review A: complete literal functional graphs, with no author-code imports.

Preparation only until root separately reviews and binds this exact capsule.
Scientific output is emitted once, to stdout; this file never writes canonical.
"""

import itertools
import json
import math
import sys


EXPECTED_PARAMETERS = {
    "schema": "p211-a-parameters-v1",
    "n_values": [1, 2, 3, 4, 5, 6, 7],
    "expected_total_vertices": 2353,
    "carrier": "all_nondecreasing_maps_on_1_to_n",
    "ordering": "lexicographic_value_tuples_zero_based_vertex_ids",
    "graph_method": "indegree_pruning_cycles_reverse_breadth_first_distances",
    "inverse_method": "ordered_ternary_gap_words_and_full_reverse_adjacency",
    "output_schema": "p211-a-complete-graph-v1",
}


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def coordinates(values):
    """Extract run ends and distinct values by scanning the whole function."""
    ends = []
    outputs = []
    for offset, value in enumerate(values):
        if offset + 1 == len(values) or values[offset + 1] != value:
            ends.append(offset + 1)
            outputs.append(value)
    return tuple(ends), tuple(outputs)


def projection(support, n):
    """A literal ceiling table, independently evaluated at each domain point."""
    return tuple(min(label for label in support if label >= i)
                 for i in range(1, n + 1))


def literal_successor(values):
    n = len(values)
    ends, outputs = coordinates(values)
    first = projection(set(outputs) | {n}, n)
    second = projection(ends, n)
    return tuple(second[first[i] - 1] for i in range(n))


def from_coordinates(ends, outputs, n):
    require(len(ends) == len(outputs) > 0, "invalid reconstruction ranks")
    require(ends[-1] == n, "reconstruction missing terminal kernel end")
    require(tuple(sorted(set(ends))) == tuple(ends), "unordered kernel ends")
    require(tuple(sorted(set(outputs))) == tuple(outputs), "unordered image")
    values = []
    previous = 0
    for end, output in zip(ends, outputs):
        values.extend([output] * (end - previous))
        previous = end
    return tuple(values)


def image_condition(ends, outputs, n):
    return (ends[-1] == outputs[-1] == n
            and all(w <= z for w, z in zip(ends, outputs))
            and all(outputs[j] < ends[j + 1]
                    for j in range(len(ends) - 1)))


def image_intervals(ends, outputs):
    """Include every anchor interval, including intervals with no strict pair."""
    intervals = []
    labels = []
    for end, output in zip(ends, outputs):
        if end == output:
            intervals.append({"anchor": end, "strict_labels": labels})
            labels = []
        else:
            labels.extend([end, output])
    require(not labels, "image interval has no final anchor")
    return intervals


def interval_peel(intervals, n):
    ends = []
    outputs = []
    for interval in intervals:
        labels = interval["strict_labels"]
        middle = labels[1:-1] if labels else []
        for offset in range(0, len(middle), 2):
            ends.append(middle[offset])
            outputs.append(middle[offset + 1])
        ends.append(interval["anchor"])
        outputs.append(interval["anchor"])
    return from_coordinates(tuple(ends), tuple(outputs), n)


def graph_decomposition(successors, reverse):
    """Discover recurrent cycles before consulting any dynamical formula."""
    remaining_indegree = [len(incoming) for incoming in reverse]
    pruning_order = [v for v, degree in enumerate(remaining_indegree) if degree == 0]
    cursor = 0
    while cursor < len(pruning_order):
        vertex = pruning_order[cursor]
        cursor += 1
        target = successors[vertex]
        remaining_indegree[target] -= 1
        if remaining_indegree[target] == 0:
            pruning_order.append(target)

    cycles = []
    seen = set()
    for vertex, degree in enumerate(remaining_indegree):
        if degree == 0 or vertex in seen:
            continue
        cycle = []
        current = vertex
        while current not in seen:
            seen.add(current)
            cycle.append(current)
            current = successors[current]
        require(current == vertex, "pruned remainder is not disjoint cycles")
        require(vertex == min(cycle), "cycle start is not canonical minimum")
        cycles.append(cycle)

    distances = [None] * len(successors)
    cycle_index = [None] * len(successors)
    queue = []
    for number, cycle in enumerate(cycles):
        for vertex in cycle:
            distances[vertex] = 0
            cycle_index[vertex] = number
            queue.append(vertex)
    cursor = 0
    while cursor < len(queue):
        target = queue[cursor]
        cursor += 1
        for source in reverse[target]:
            if distances[source] is None:
                distances[source] = distances[target] + 1
                cycle_index[source] = cycle_index[target]
                queue.append(source)
    require(all(d is not None for d in distances), "unclassified graph vertices")
    require(len(queue) == len(successors), "reverse propagation lost vertices")
    return cycles, distances, cycle_index, pruning_order, queue


def polynomial_for_gap(length):
    coefficients = {}
    for selected in range(length + 1):
        multiplicity = math.comb(length, selected)
        for count_x in range(selected + 1):
            exponent = selected - 2 * count_x
            coefficients[exponent] = coefficients.get(exponent, 0) + multiplicity
    return coefficients


def multiply(left, right):
    result = {}
    for a, x in left.items():
        for b, y in right.items():
            result[a + b] = result.get(a + b, 0) + x * y
    return result


def coefficient_rows(coefficients):
    return [[exponent, coefficients[exponent]] for exponent in sorted(coefficients)]


def gap_words(sites):
    result = []
    for word in itertools.product((0, 1, 2), repeat=len(sites)):
        seen_a = False
        valid = True
        for colour in word:
            if colour == 2:
                seen_a = True
            elif colour == 1 and seen_a:
                valid = False
                break
        if valid:
            result.append(word)
    return result


def inverse_atlas(ends, outputs, n, vertex_id):
    """Target-only decoder: no literal successor or graph lookup in its rule."""
    gaps = []
    previous_value = 0
    for end, output in zip(ends, outputs):
        gaps.append(list(range(previous_value + 1, end)))
        previous_value = output
    polynomials = [polynomial_for_gap(len(gap)) for gap in gaps]
    product = {0: 1}
    for factor in polynomials:
        product = multiply(product, factor)
    descriptions = []
    for words in itertools.product(*(gap_words(gap) for gap in gaps)):
        x_sites = set(outputs)
        a_sites = set(ends)
        for gap, word in zip(gaps, words):
            for site, colour in zip(gap, word):
                if colour == 1:
                    x_sites.add(site)
                elif colour == 2:
                    a_sites.add(site)
        balance = len(a_sites) - len(x_sites)
        if balance not in (0, 1):
            continue
        y_sites = a_sites if balance == 0 else a_sites - {n}
        x_tuple = tuple(sorted(x_sites))
        y_tuple = tuple(sorted(y_sites))
        source = from_coordinates(x_tuple, y_tuple, n)
        require(source in vertex_id, "decoder produced a noncarrier source")
        descriptions.append({
            "source_id": vertex_id[source],
            "gap_words": [list(word) for word in words],
            "X": list(x_tuple),
            "A": sorted(a_sites),
            "Y": list(y_tuple),
            "balance": balance,
        })
    descriptions.sort(key=lambda item: item["source_id"])
    return {
        "gaps": gaps,
        "gap_polynomials": [coefficient_rows(p) for p in polynomials],
        "product_polynomial": coefficient_rows(product),
        "balance_counts": [product.get(0, 0), product.get(1, 0)],
        "predicted_count": product.get(0, 0) + product.get(1, 0),
        "descriptions": descriptions,
    }


def analyse_carrier(n):
    states = list(itertools.combinations_with_replacement(range(1, n + 1), n))
    vertex_id = {state: number for number, state in enumerate(states)}
    successors = []
    reverse = [[] for state in states]
    checks = {}

    def check(name, condition, detail):
        require(condition, "n=" + str(n) + ": " + name + ": " + str(detail))
        checks[name] = checks.get(name, 0) + 1

    check("carrier_size", len(states) == math.comb(2 * n - 1, n), n)
    check("unique_lexicographic_states", states == sorted(set(states)), n)
    for source, state in enumerate(states):
        target_state = literal_successor(state)
        check("literal_closure", target_state in vertex_id, source)
        target = vertex_id[target_state]
        successors.append(target)
        reverse[target].append(source)
    cycles, depths, cycle_indices, pruning, reverse_order = graph_decomposition(successors, reverse)
    check("only_fixed_cycles", all(len(cycle) == 1 for cycle in cycles), cycles)
    cycle_vertices = sorted(vertex for cycle in cycles for vertex in cycle)
    projection_ids = sorted(vertex_id[projection(set(selection) | {n}, n)]
                            for bits in itertools.product((0, 1), repeat=n - 1)
                            for selection in [[i + 1 for i, bit in enumerate(bits) if bit]])
    check("complete_recurrent_projections", cycle_vertices == projection_ids, cycle_vertices)
    check("fixed_projection_census", len(cycle_vertices) == 2 ** (n - 1), n)
    check("edge_mass", sum(len(incoming) for incoming in reverse) == len(states), n)

    rows = []
    for number, state in enumerate(states):
        ends, outputs = coordinates(state)
        a_sites = set(outputs) | {n}
        check("support_reconstruction", from_coordinates(ends, outputs, n) == state, number)
        image_predicted = image_condition(ends, outputs, n)
        check("image_iff", bool(reverse[number]) == image_predicted, number)
        next_ends, next_outputs = coordinates(states[successors[number]])
        check("product_support_containments",
              set(next_ends) <= a_sites and set(next_outputs) <= set(ends), number)
        check("product_common_anchor_identity",
              set(next_ends) & set(next_outputs) == set(ends) & a_sites, number)
        check("first_image_extensive_top_fixing",
              states[successors[number]][-1] == n
              and all(value >= i + 1 for i, value in enumerate(states[successors[number]])), number)

        recurrent = cycles[cycle_indices[number]][0]
        terminal_support = sorted(set(ends) & a_sites)
        terminal_predicted = vertex_id[projection(terminal_support, n)]
        check("terminal_formula", recurrent == terminal_predicted, number)
        successor_intervals = image_intervals(next_ends, next_outputs)
        successor_radius = max(len(item["strict_labels"]) // 2 for item in successor_intervals)
        time_predicted = 0 if successors[number] == number else 1 + successor_radius
        check("full_carrier_time", depths[number] == time_predicted, number)

        orbit = []
        positions = {}
        current = number
        while current not in positions:
            positions[current] = len(orbit)
            orbit.append(current)
            current = successors[current]
        repeated_at = positions[current]
        orbit.append(current)
        check("orbit_graph_tail_agreement", repeated_at == depths[number], number)
        check("orbit_graph_period_agreement", len(orbit) - 1 - repeated_at == 1, number)
        check("orbit_graph_terminal_agreement", current == recurrent, number)

        intervals = None
        image_radius = None
        peeled_id = None
        atlas = None
        if image_predicted:
            intervals = image_intervals(ends, outputs)
            image_radius = max(len(item["strict_labels"]) // 2 for item in intervals)
            peeled_id = vertex_id[interval_peel(intervals, n)]
            check("labelled_endpoint_peeling", peeled_id == successors[number], number)
            check("image_exact_time", image_radius == depths[number], number)
            check("image_label_budget", image_radius <= (n - 1) // 2, number)
            exchanged_source = from_coordinates(outputs, ends, n)
            check("constructive_image_sufficiency",
                  successors[vertex_id[exchanged_source]] == number, number)
            atlas = inverse_atlas(ends, outputs, n, vertex_id)
            decoded = [item["source_id"] for item in atlas["descriptions"]]
            check("decoder_injective", len(decoded) == len(set(decoded)), number)
            check("complete_inverse_atlas", decoded == reverse[number], number)
            check("laurent_fibre_count", atlas["predicted_count"] == len(reverse[number]), number)
            branch_counts = [sum(item["balance"] == branch for item in atlas["descriptions"])
                             for branch in (0, 1)]
            check("laurent_rank_branch_counts", branch_counts == atlas["balance_counts"], number)
        else:
            check("zero_fibre", reverse[number] == [], number)
        rows.append({
            "id": number, "values": list(state),
            "kernel_ends": list(ends), "image_values": list(outputs),
            "successor_id": successors[number], "predecessor_ids": reverse[number],
            "cycle_index": cycle_indices[number], "graph_depth": depths[number],
            "orbit_with_repeated_terminal": orbit,
            "terminal_id": recurrent, "terminal_support_prediction": terminal_support,
            "image_criterion": image_predicted,
            "time_prediction": time_predicted,
            "image_intervals": intervals, "image_radius": image_radius,
            "peeled_successor_id": peeled_id, "inverse_atlas": atlas,
        })

    expected_height = 0 if n == 1 else (n + 1) // 2
    check("sharp_full_height", max(depths) == expected_height, n)
    maximum_vertices = [v for v, depth in enumerate(depths) if depth == expected_height]
    if n == 1:
        witness_ends, witness_image = (1,), (1,)
    elif n % 2:
        witness_ends = tuple(range(2, n, 2)) + (n,)
        witness_image = tuple(range(1, n - 1, 2)) + (n,)
    else:
        witness_ends = tuple(range(2, n + 1, 2))
        witness_image = tuple(range(1, n, 2))
    witness = vertex_id[from_coordinates(witness_ends, witness_image, n)]
    check("parity_witness_attains_height", depths[witness] == expected_height, witness)
    if n > 1:
        check("parity_witness_initial_change",
              states[witness][0] == 1 and states[successors[witness]][0] == 2, witness)
    check("complete_target_rows", len(rows) == len(states), n)
    check("decoded_total_mass",
          sum(0 if row["inverse_atlas"] is None else row["inverse_atlas"]["predicted_count"]
              for row in rows) == len(states), n)
    return {
        "n": n, "vertex_count": len(states), "rows": rows,
        "cycles": cycles, "indegree_pruning_order": pruning,
        "reverse_breadth_first_order": reverse_order,
        "image_vertex_ids": [v for v in range(len(states)) if reverse[v]],
        "zero_fibre_vertex_ids": [v for v in range(len(states)) if not reverse[v]],
        "height": max(depths), "height_prediction": expected_height,
        "height_attaining_vertex_ids": maximum_vertices,
        "specified_parity_witness_id": witness,
        "check_counts": checks, "check_total": sum(checks.values()),
    }


def main():
    require(len(sys.argv) == 3 and sys.argv[1] == "--parameters", "expected --parameters ABS_PATH")
    require(sys.argv[2].startswith("/"), "parameter path must be absolute")
    with open(sys.argv[2], "r", encoding="utf-8") as handle:
        parameters = json.load(handle)
    require(type(parameters) is dict, "parameters must be one object")
    require(parameters == EXPECTED_PARAMETERS, "parameter object differs from exact approved specification")
    require(type(parameters["expected_total_vertices"]) is int, "total vertex count must be integer")
    require(type(parameters["n_values"]) is list
            and all(type(n) is int for n in parameters["n_values"]), "n values must be integers")
    carriers = [analyse_carrier(n) for n in parameters["n_values"]]
    total = sum(carrier["vertex_count"] for carrier in carriers)
    require(total == parameters["expected_total_vertices"], "wrong total source-state coverage")
    transcript = {
        "schema": parameters["output_schema"], "role": "P211_REVIEW_A",
        "parameters": parameters, "carriers": carriers,
        "total_vertices": total,
        "total_targets": sum(len(carrier["rows"]) for carrier in carriers),
        "total_edges": sum(carrier["vertex_count"] for carrier in carriers),
        "check_total": sum(carrier["check_total"] for carrier in carriers),
        "verdict": "FINITE_GRAPH_CHECKS_PASS",
        "scope": "n=1..7 finite counterexample pressure only; not an all-n proof or manuscript acceptance",
    }
    sys.stdout.write(json.dumps(transcript, sort_keys=True, separators=(",", ":"), ensure_ascii=True) + "\n")


if __name__ == "__main__":
    main()
