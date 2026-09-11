"""Prepared, unexecuted author pilot for four closed-pointer carriers.

No import, syntax compilation, scientific snippet or invocation is authorized
by this file's existence. Root must inspect and separately bind the exact run.
The program reads one exact parameter file, writes JSON to stdout, and creates
no files. It has no cutoff, subset, random, replay, or parameter-extension mode.
"""

import json
import sys
from collections import Counter
from fractions import Fraction
from itertools import product
from math import factorial


EXPECTED_PARAMETERS = {
    "schema_version": "finite-pointer-parameters-v1",
    "role": "single-bounded-author-pilot",
    "label_convention": "one_based",
    "state_order": "lexicographic_(u,v,f(1),...,f(n))",
    "boxes": [
        {"n": 1, "state_count": 1},
        {"n": 2, "state_count": 16},
        {"n": 3, "state_count": 243},
        {"n": 4, "state_count": 4096},
    ],
    "box_count": 4,
    "total_state_count": 4356,
    "allow_box_extension": False,
}


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key: " + key)
        result[key] = value
    return result


def reject_constant(value):
    raise ValueError("nonfinite JSON constant: " + value)


def read_parameters(path):
    with open(path, "rb") as stream:
        raw = stream.read()
    value = json.loads(
        raw.decode("utf-8"), object_pairs_hook=unique_object,
        parse_constant=reject_constant,
    )
    # JSON equality alone would identify True with 1; canonical re-encoding
    # also rejects booleans/floats in integer positions and extra fields.
    if json.dumps(value, sort_keys=True) != json.dumps(EXPECTED_PARAMETERS, sort_keys=True):
        raise ValueError("parameters differ from the four-box preparation")
    return value


def literal_successor(state):
    """Only direct old-state reads and the single literal assignment."""
    previous, current = state[0], state[1]
    memory = state[2:]
    old_next = memory[current - 1]
    new_memory = list(memory)
    new_memory[current - 1] = previous
    return (current, old_next, *new_memory)


def literal_inverse(target):
    """A separately written formula, never used for cycle discovery."""
    a, b = target[0], target[1]
    g = target[2:]
    restored = list(g)
    restored[a - 1] = b
    return (g[a - 1], a, *restored)


def discover_cycles(next_ids):
    """Functional-graph traversal using successor IDs only, no theorem data.

    Tails are retained if unexpectedly present; they are not silently dropped
    by assuming the map is a permutation. Cycles start at their least ID and
    are ordered by that ID. State IDs are box-local and zero based.
    """
    count = len(next_ids)
    orbit_of = [-1] * count
    depth = [-1] * count
    position = [None] * count
    cycles = []
    for start in range(count):
        if orbit_of[start] != -1:
            continue
        path = []
        local_position = {}
        cursor = start
        while orbit_of[cursor] == -1 and cursor not in local_position:
            local_position[cursor] = len(path)
            path.append(cursor)
            cursor = next_ids[cursor]
        if cursor in local_position:
            cycle_start = local_position[cursor]
            cycle = path[cycle_start:]
            least_position = cycle.index(min(cycle))
            cycle = cycle[least_position:] + cycle[:least_position]
            old_orbit_id = len(cycles)
            cycles.append(cycle)
            for offset, vertex in enumerate(cycle):
                orbit_of[vertex] = old_orbit_id
                depth[vertex] = 0
                position[vertex] = offset
            prefix = path[:cycle_start]
        else:
            prefix = path
        for vertex in reversed(prefix):
            successor = next_ids[vertex]
            orbit_of[vertex] = orbit_of[successor]
            depth[vertex] = depth[successor] + 1
    order = sorted(range(len(cycles)), key=lambda index: cycles[index][0])
    old_to_new = {old: new for new, old in enumerate(order)}
    cycles = [cycles[old] for old in order]
    orbit_of = [old_to_new[old] for old in orbit_of]
    return cycles, orbit_of, depth, position


def graph_multiset(state):
    """All f-edges plus the location edge, with loops and multiplicity."""
    memory = state[2:]
    edges = [tuple(sorted((vertex, image))) for vertex, image in enumerate(memory, 1)]
    edges.append(tuple(sorted(state[:2])))
    multiplicity = Counter(edges)
    return [[a, b, multiplicity[(a, b)]] for a, b in sorted(multiplicity)]


def require_shape(condition, message):
    if not condition:
        raise ValueError(message)


def core_shape(vertices, edge_ids, expanded_edges, degree):
    """Classify an undirected core, with no access to states or orbits.

    Temporary edge IDs distinguish occurrences solely for graph traversal.
    They are not labels in the dynamical carrier or orbit decorations.
    """
    branches = sorted(vertex for vertex in vertices if degree[vertex] > 2)
    require_shape(len(edge_ids) == len(vertices) + 1, "core excess is not one")
    require_shape(all(degree[vertex] >= 2 for vertex in vertices), "core degree below two")
    require_shape(
        (len(branches) == 1 and degree[branches[0]] == 4)
        or (len(branches) == 2 and all(degree[vertex] == 3 for vertex in branches)),
        "core branch-degree pattern is not bicyclic",
    )
    adjacency = {vertex: [] for vertex in vertices}
    for edge_id in edge_ids:
        a, b = expanded_edges[edge_id]
        adjacency[a].append(edge_id)
        adjacency[b].append(edge_id)  # A loop contributes degree two.
    used = set()
    chains = []
    branch_set = set(branches)
    for branch in branches:
        for first_edge in sorted(set(adjacency[branch])):
            if first_edge in used:
                continue
            walk = [branch]
            traversed = []
            vertex = branch
            edge_id = first_edge
            while True:
                require_shape(edge_id not in used, "chain revisits an edge")
                used.add(edge_id)
                traversed.append(edge_id)
                a, b = expanded_edges[edge_id]
                require_shape(vertex == a or vertex == b, "nonincident chain edge")
                following = b if vertex == a else a
                walk.append(following)
                if following in branch_set:
                    break
                options = sorted(set(adjacency[following]) - {edge_id})
                require_shape(len(options) == 1, "degree-two chain is not forced")
                vertex = following
                edge_id = options[0]
            reverse_walk = list(reversed(walk))
            if tuple(reverse_walk) < tuple(walk):
                walk = reverse_walk
                traversed = list(reversed(traversed))
            chains.append({"vertices": walk, "edge_ids": traversed, "length": len(traversed)})
    require_shape(used == set(edge_ids), "core edge not in a branch chain")
    chains.sort(key=lambda chain: (tuple(chain["vertices"]), tuple(chain["edge_ids"])))
    closed = [chain for chain in chains if chain["vertices"][0] == chain["vertices"][-1]]
    joining = [chain for chain in chains if chain["vertices"][0] != chain["vertices"][-1]]
    if len(branches) == 1:
        require_shape(len(closed) == 2 and not joining, "invalid figure-eight chains")
        a, b = sorted(chain["length"] for chain in closed)
        period = 1 if a == b == 1 else (a + b if max(a, b) <= 2 else 2 * (a + b))
        kind = "figure_eight"
        parameters = {"a": a, "b": b}
        orbit_count = 2 if min(a, b) >= 3 else 1
    elif len(joining) == 3 and not closed:
        a, b, c = sorted(chain["length"] for chain in joining)
        period = 2 if a == b == c == 1 else 2 * (a + b + c)
        kind = "theta"
        parameters = {"a": a, "b": b, "c": c}
        orbit_count = 1 if [a, b, c].count(1) >= 2 else 2
    else:
        require_shape(len(closed) == 2 and len(joining) == 1, "invalid barbell chains")
        by_endpoint = {chain["vertices"][0]: chain["length"] for chain in closed}
        require_shape(set(by_endpoint) == branch_set, "barbell cycles do not occupy both branches")
        a, b = by_endpoint[branches[0]], by_endpoint[branches[1]]
        c = joining[0]["length"]
        half_block = a + b + 2 * c
        period = half_block if max(a, b) <= 2 else 2 * half_block
        kind = "barbell"
        parameters = {"a": a, "b": b, "c": c}
        orbit_count = 2 if min(a, b) >= 3 else 1
    return {
        "kind": kind, "parameters": parameters, "branches": branches,
        "chains": chains, "predicted_period": period,
        "predicted_orbit_count": orbit_count, "error": None,
    }


def classify_state(state):
    """Build/prune the multigraph independently of successor-cycle discovery."""
    n = len(state) - 2
    multiset = graph_multiset(state)
    expanded = []
    for a, b, multiplicity in multiset:
        expanded.extend([(a, b)] * multiplicity)
    adjacency = {vertex: set() for vertex in range(1, n + 1)}
    for a, b in expanded:
        adjacency[a].add(b)
        adjacency[b].add(a)
    component = {state[0]}
    pending = [state[0]]
    while pending:
        vertex = pending.pop()
        for neighbour in sorted(adjacency[vertex]):
            if neighbour not in component:
                component.add(neighbour)
                pending.append(neighbour)
    core_vertices = set(component)
    while True:
        degree = {vertex: 0 for vertex in core_vertices}
        core_ids = []
        for edge_id, (a, b) in enumerate(expanded):
            if a in core_vertices and b in core_vertices:
                core_ids.append(edge_id)
                degree[a] += 1
                degree[b] += 1
        leaves = {vertex for vertex in core_vertices if degree[vertex] < 2}
        if not leaves:
            break
        core_vertices -= leaves
    core_edges = [row for row in multiset if row[0] in core_vertices and row[1] in core_vertices]
    frozen = [[vertex, state[vertex + 1]] for vertex in range(1, n + 1) if vertex not in core_vertices]
    core_key_object = {"vertices": sorted(core_vertices), "edges": core_edges}
    core_key = json.dumps(core_key_object, sort_keys=True, separators=(",", ":"))
    group_key = json.dumps(
        {"core": core_key_object, "frozen_arrows": frozen},
        sort_keys=True, separators=(",", ":"),
    )
    try:
        shape = core_shape(core_vertices, core_ids, expanded, degree)
    except ValueError as error:
        shape = {
            "kind": "invalid", "parameters": {}, "branches": [], "chains": [],
            "predicted_period": None, "predicted_orbit_count": None, "error": str(error),
        }
    return {
        "graph_multiset": multiset,
        "active_component": sorted(component),
        "attached_tree_vertices": sorted(component - core_vertices),
        "inactive_vertices": sorted(set(range(1, n + 1)) - component),
        "core": {
            **core_key_object, "edge_count": len(core_ids),
            "degrees": [[vertex, degree[vertex]] for vertex in sorted(core_vertices)],
            **shape,
        },
        "frozen_arrows": frozen, "core_key": core_key, "group_key": group_key,
    }


def polynomial_add(*terms):
    result = {}
    for term in terms:
        for key, coefficient in term.items():
            result[key] = result.get(key, Fraction(0)) + coefficient
    return {key: value for key, value in result.items() if value}


def polynomial_scale(term, coefficient):
    return {key: value * coefficient for key, value in term.items() if value * coefficient}


def polynomial_multiply(left, right, maximum_degree):
    result = {}
    for (s1, p1), c1 in left.items():
        for (s2, p2), c2 in right.items():
            if s1 + s2 <= maximum_degree:
                key = (s1 + s2, p1 + p2)
                result[key] = result.get(key, Fraction(0)) + c1 * c2
    return {key: value for key, value in result.items() if value}


def core_orbit_series(maximum_degree):
    """Exact expansion of the written rational EGF, not graph enumeration.

    Sparse keys are (t degree, q degree). Only t degree is truncated, never
    q degree; unexpected periods therefore cannot be hidden by a period cap.
    No successor, orbit, core classifier or empirical count is consumed.
    """
    one = {(0, 0): Fraction(1)}
    x = {(1, 2): Fraction(1)}
    geometric2 = {(k, 2 * k): Fraction(1) for k in range(maximum_degree + 1)}
    geometric4 = {(k, 4 * k): Fraction(1) for k in range(maximum_degree + 1)}
    square_inverse = {(k, 2 * k): Fraction(k + 1) for k in range(maximum_degree + 1)}
    short_square = polynomial_multiply(polynomial_add(one, x), polynomial_add(one, x), maximum_degree)
    difference = polynomial_add(square_inverse, polynomial_scale(short_square, Fraction(-1)))
    q_series = polynomial_add(geometric2, polynomial_scale(one, Fraction(-1)))
    q_square = polynomial_multiply(q_series, q_series, maximum_degree)
    q_cube = polynomial_multiply(q_square, q_series, maximum_degree)
    figure_eight = polynomial_add(
        {(1, 1): Fraction(1), (2, 3): Fraction(1), (3, 4): Fraction(1, 2)},
        polynomial_multiply({(1, 4): Fraction(1, 4)}, difference, maximum_degree),
    )
    short_cycles = polynomial_add(one, {(1, 1): Fraction(1)})
    short_barbell = polynomial_multiply(
        {(2, 4): Fraction(1, 2)},
        polynomial_multiply(
            polynomial_multiply(short_cycles, short_cycles, maximum_degree),
            geometric2, maximum_degree,
        ), maximum_degree,
    )
    long_barbell = polynomial_multiply(
        {(2, 8): Fraction(1, 4)},
        polynomial_multiply(difference, geometric4, maximum_degree), maximum_degree,
    )
    theta = polynomial_add(
        {(2, 2): Fraction(1, 2)},
        polynomial_multiply(
            {(2, 6): Fraction(1, 2)},
            polynomial_add(q_series, q_square, polynomial_scale(q_cube, Fraction(1, 3))),
            maximum_degree,
        ),
    )
    pieces = {"figure_eight": figure_eight, "barbell": polynomial_add(short_barbell, long_barbell), "theta": theta}
    pieces = {name: {key: value for key, value in piece.items() if key[0] <= maximum_degree} for name, piece in pieces.items()}
    total = polynomial_add(*pieces.values())
    return pieces, total


def ratio(value):
    value = Fraction(value)
    return {"numerator": value.numerator, "denominator": value.denominator}


def integer_or_ratio(value):
    value = Fraction(value)
    return value.numerator if value.denominator == 1 else ratio(value)


def coefficient_rows(series):
    return [{"s": s, "p": p, "coefficient": ratio(value)} for (s, p), value in sorted(series.items()) if value]


def period_count_rows(counts):
    return [{"p": p, "count": integer_or_ratio(value)} for p, value in sorted(counts.items()) if value]


def core_period_count_rows(counts):
    return [{"s": s, "p": p, "count": integer_or_ratio(value)} for (s, p), value in sorted(counts.items()) if value]


def check(records, identifier, observed, expected):
    records.append({"id": identifier, "observed": observed, "expected": expected, "pass": observed == expected})


def total_core_coefficient(size):
    if size == 1:
        return Fraction(1)
    if size == 2:
        return Fraction(2)
    return Fraction(5 * size * size + size + 24, 24)


def expected_periods(n):
    if n == 1:
        return [1]
    return list(range(1, 2 * n + 1)) + list(range(2 * n + 2, 4 * n - 3, 2))


def build_box(n, declared_size, series):
    prefix = "n" + str(n)
    checks = []
    labels = range(1, n + 1)
    states = list(product(labels, repeat=n + 2))
    state_index = {state: index for index, state in enumerate(states)}
    successors = [literal_successor(state) for state in states]
    next_ids = [state_index[target] for target in successors]
    predecessors = [[] for _ in states]
    for index, target in enumerate(next_ids):
        predecessors[target].append(index)
    cycles, orbit_of, depth, positions = discover_cycles(next_ids)
    classifications = [classify_state(state) for state in states]
    all_groups = sorted({entry["group_key"] for entry in classifications})
    group_index = {key: index for index, key in enumerate(all_groups)}
    all_cores = sorted({entry["core_key"] for entry in classifications})
    core_index = {key: index for index, key in enumerate(all_cores)}
    records = []
    group_members = {key: [] for key in all_groups}
    for state_id, (state, classification) in enumerate(zip(states, classifications)):
        core = classification["core"]
        period = len(cycles[orbit_of[state_id]])
        inverse_id = state_index[literal_inverse(state)]
        record = {
            "id": state_id, "u": state[0], "v": state[1], "f": list(state[2:]),
            "next": next_ids[state_id], "predecessors": predecessors[state_id],
            "inverse_formula_state_id": inverse_id,
            "orbit_id": orbit_of[state_id], "orbit_position": positions[state_id],
            "preperiod": depth[state_id], "observed_period": period,
            "core_id": core_index[classification["core_key"]],
            "group_id": group_index[classification["group_key"]],
            **classification,
        }
        records.append(record)
        group_members[classification["group_key"]].append(state_id)
        state_prefix = prefix + ".state" + str(state_id)
        check(checks, state_prefix + ".S01_successor_closed", next_ids[state_id] in range(len(states)), True)
        check(checks, state_prefix + ".S02_inverse_forward", literal_successor(literal_inverse(state)), state)
        check(checks, state_prefix + ".S03_inverse_backward", literal_inverse(successors[state_id]), state)
        check(checks, state_prefix + ".S04_indegree", len(predecessors[state_id]), 1)
        check(checks, state_prefix + ".S05_preperiod", depth[state_id], 0)
        after = classifications[next_ids[state_id]]
        check(checks, state_prefix + ".S06_multiset_invariant", after["graph_multiset"], classification["graph_multiset"])
        check(checks, state_prefix + ".S07_core_frozen_invariant", after["group_key"], classification["group_key"])
        core_vertices = set(core["vertices"])
        check(
            checks, state_prefix + ".S08_core_closed",
            state[0] in core_vertices and state[1] in core_vertices
            and all(state[vertex + 1] in core_vertices for vertex in core_vertices), True,
        )
        check(checks, state_prefix + ".S09_core_valid", core["kind"] in {"figure_eight", "barbell", "theta"}, True)
        check(checks, state_prefix + ".S10_period", period, core["predicted_period"])
    orbit_records = []
    observed_period_counts = Counter()
    observed_core_period_counts = Counter()
    for orbit_id, cycle in enumerate(cycles):
        first = classifications[cycle[0]]
        period = len(cycle)
        member_groups = sorted({group_index[classifications[index]["group_key"]] for index in cycle})
        core_sizes = sorted({len(classifications[index]["core"]["vertices"]) for index in cycle})
        orbit_records.append({
            "id": orbit_id, "states": cycle, "period": period,
            "group_ids": member_groups, "core_sizes": core_sizes,
        })
        observed_period_counts[period] += 1
        observed_core_period_counts[(len(first["core"]["vertices"]), period)] += 1
        orbit_prefix = prefix + ".orbit" + str(orbit_id)
        check(checks, orbit_prefix + ".O01_edges", [next_ids[index] for index in cycle], cycle[1:] + cycle[:1])
        check(checks, orbit_prefix + ".O02_unique_members", len(set(cycle)), period)
        check(checks, orbit_prefix + ".O03_one_group", len(member_groups), 1)
    groups = []
    for key in all_groups:
        members = group_members[key]
        first = classifications[members[0]]
        orbit_ids = sorted({orbit_of[index] for index in members})
        periods = sorted({len(cycles[index]) for index in orbit_ids})
        predicted_period = first["core"]["predicted_period"]
        predicted_count = first["core"]["predicted_orbit_count"]
        group_id = group_index[key]
        groups.append({
            "id": group_id, "key": key, "core_id": core_index[first["core_key"]],
            "core": first["core"], "frozen_arrows": first["frozen_arrows"],
            "state_ids": members, "orbit_ids": orbit_ids,
            "observed_periods": periods, "predicted_period": predicted_period,
            "observed_orbit_count": len(orbit_ids), "predicted_orbit_count": predicted_count,
        })
        group_prefix = prefix + ".group" + str(group_id)
        check(checks, group_prefix + ".G01_orbit_count", len(orbit_ids), predicted_count)
        check(checks, group_prefix + ".G02_periods", periods, [predicted_period])
        covered = sorted(index for orbit_id in orbit_ids for index in cycles[orbit_id])
        check(checks, group_prefix + ".G03_exact_cover", covered, members)
    core_catalog = []
    for key in all_cores:
        first = next(entry for entry in classifications if entry["core_key"] == key)
        core_catalog.append({
            "id": core_index[key], "key": key, "core": first["core"],
            "group_ids": [group["id"] for group in groups if group["core_id"] == core_index[key]],
        })
    expected_core_period_counts = {}
    expected_period_counts = {}
    extension_terms = []
    for (size, period), coefficient in sorted(series.items()):
        if size > n:
            continue
        multiplier = factorial(n) // factorial(n - size) * n ** (n - size)
        contribution = coefficient * multiplier
        expected_core_period_counts[(size, period)] = contribution
        expected_period_counts[period] = expected_period_counts.get(period, Fraction(0)) + contribution
        extension_terms.append({
            "s": size, "p": period, "core_coefficient": ratio(coefficient),
            "label_and_frozen_multiplier": multiplier, "contribution": ratio(contribution),
        })
        check(checks, prefix + ".E01_integral_s" + str(size) + "_p" + str(period), contribution.denominator, 1)
    total_terms = []
    for size in range(1, n + 1):
        coefficient = total_core_coefficient(size)
        multiplier = factorial(n) // factorial(n - size) * n ** (n - size)
        total_terms.append({"s": size, "coefficient": ratio(coefficient), "multiplier": multiplier, "contribution": ratio(coefficient * multiplier)})
    expected_total = sum(
        total_core_coefficient(size) * (factorial(n) // factorial(n - size)) * n ** (n - size)
        for size in range(1, n + 1)
    )
    periods = sorted(observed_period_counts)
    maximum = max(periods)
    check(checks, prefix + ".B01_carrier_count", len(states), declared_size)
    check(checks, prefix + ".B02_cardinality_formula", len(states), n ** (n + 2))
    check(checks, prefix + ".B03_edge_count", len(next_ids), declared_size)
    check(checks, prefix + ".B04_cycle_cover", sorted(index for cycle in cycles for index in cycle), list(range(len(states))))
    check(checks, prefix + ".B05_period_set", periods, expected_periods(n))
    check(checks, prefix + ".B06_maximum_period", maximum, 1 if n == 1 else 4 * n - 4)
    check(checks, prefix + ".B07_period_egf", period_count_rows(observed_period_counts), period_count_rows(expected_period_counts))
    check(checks, prefix + ".B08_core_period_egf", core_period_count_rows(observed_core_period_counts), core_period_count_rows(expected_core_period_counts))
    check(checks, prefix + ".B09_total_orbits", len(cycles), integer_or_ratio(expected_total))
    check(checks, prefix + ".B10_fixed_states", sum(next_ids[index] == index for index in range(len(states))), n ** n)
    check(checks, prefix + ".B11_weighted_cycle_cover", sum(period * count for period, count in observed_period_counts.items()), len(states))
    return {
        "n": n, "declared_state_count": declared_size, "state_count": len(states),
        "states": records, "edges": [[index, target] for index, target in enumerate(next_ids)],
        "orbits": orbit_records, "groups": groups, "core_catalog": core_catalog,
        "observed_periods": periods, "expected_periods": expected_periods(n),
        "observed_maximum_period": maximum, "expected_maximum_period": 1 if n == 1 else 4 * n - 4,
        "observed_period_orbit_counts": period_count_rows(observed_period_counts),
        "expected_period_orbit_counts": period_count_rows(expected_period_counts),
        "observed_core_period_orbit_counts": core_period_count_rows(observed_core_period_counts),
        "expected_core_period_orbit_counts": core_period_count_rows(expected_core_period_counts),
        "egf_extension_terms": extension_terms, "total_orbit_formula_terms": total_terms,
        "observed_total_orbits": len(cycles), "expected_total_orbits": integer_or_ratio(expected_total),
        "checks": checks,
    }


def build_report(parameters):
    pieces, series = core_orbit_series(4)
    checks = []
    for (size, period), coefficient in sorted(series.items()):
        check(checks, "series.C01_nonnegative_s" + str(size) + "_p" + str(period), coefficient >= 0, True)
    for size in range(1, 5):
        coefficient = sum(value for (s, _), value in series.items() if s == size)
        state_coefficient = sum(period * value for (s, period), value in series.items() if s == size)
        check(checks, "series.C02_total_s" + str(size), ratio(coefficient), ratio(total_core_coefficient(size)))
        check(checks, "series.C03_state_weight_s" + str(size), ratio(state_coefficient), ratio(Fraction(size * size * (size + 1), 2)))
    boxes = [build_box(box["n"], box["state_count"], series) for box in parameters["boxes"]]
    check(checks, "global.T01_four_boxes", [box["n"] for box in boxes], [1, 2, 3, 4])
    check(checks, "global.T02_total_states", sum(box["state_count"] for box in boxes), 4356)
    all_checks = checks + [record for box in boxes for record in box["checks"]]
    identifiers = [record["id"] for record in all_checks]
    check(checks, "global.T03_unique_check_ids", len(set(identifiers + ["global.T03_unique_check_ids"])), len(identifiers) + 1)
    all_checks = checks + [record for box in boxes for record in box["checks"]]
    failed_ids = [record["id"] for record in all_checks if not record["pass"]]
    return {
        "schema_version": "finite-pointer-pilot-output-v1",
        "role": "bounded-author-evidence-not-admission",
        "parameters": parameters,
        "coefficient_arithmetic": "fractions.Fraction; t-degree <= 4; q-degree uncapped",
        "core_series": {"pieces": {name: coefficient_rows(piece) for name, piece in sorted(pieces.items())}, "total": coefficient_rows(series)},
        "boxes": boxes, "checks": checks,
        "summary": {"check_count": len(all_checks), "failed_count": len(failed_ids), "failed_ids": failed_ids, "status": "PASS" if not failed_ids else "FAIL"},
    }


def main(argv):
    if len(argv) != 2:
        raise ValueError("usage: pointer_pilot.py EXACT_PARAMETERS_JSON")
    parameters = read_parameters(argv[1])
    report = build_report(parameters)
    payload = json.dumps(report, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False)
    sys.stdout.write(payload + "\n")
    return 0 if report["summary"]["failed_count"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
