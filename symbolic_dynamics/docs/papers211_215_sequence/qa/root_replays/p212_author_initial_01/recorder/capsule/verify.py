#!/usr/bin/env python3
"""P212 author verifier, newly written from the admitted theorem.

SOURCE_ONLY preparation: this file has not been imported, compiled, parsed
as Python, or executed by its author. Execution needs separate root approval.
No old scientific implementation is read or imported. Only the standard
library is used. The single explicit data input is PARAMETERS.json.

Observed side: literal complete state graph and its actual cyclic orbits.
Expected side: unlabeled-edge multiplicity matrices, constructed observable
anchor states, and exact rational power-series arithmetic. An orbit-class
comparison is never replaced by a quotient of total states by a period.
"""

import itertools
import json
import math
import sys
from fractions import Fraction


PARAMETERS = {
    "schema": "p212-parameters-v1",
    "carrier_sizes": [1, 2, 3, 4],
    "label_base": 1,
    "carrier": "[n]^2 x [n]^[n]",
    "state_order": "lexicographic (u,v,f(1),...,f(n))",
    "update": "R(u,v,f)=(v,f(v),f[v:=u]); simultaneous old-state RHS",
    "edge_identity": "none; undirected multiplicities only",
    "loop_degree": 2,
    "series_max_core_size": 4,
    "fixed_iterates": "all integers 1 through the predicted maximum period in each carrier",
    "expected_state_counts": [1, 16, 243, 4096],
    "expected_total_states": 4356,
    "unobserved_core_first_sizes": [5, 6, 5],
    "output_schema": "p212-full-output-v1",
}
FAMILIES = ("figure_eight", "barbell", "theta")
ROWS = (
    "figure_eight_double_loop",
    "figure_eight_short_nontrivial",
    "figure_eight_long",
    "barbell_short",
    "barbell_long",
    "theta_triple_direct",
    "theta_other",
)
ROW_FIRST_SIZES = (1, 2, 3, 2, 4, 2, 3)
LIMITS = (
    ("figure_eight_both_cycles_long", 5),
    ("barbell_both_cycles_long", 6),
    ("theta_all_paths_nondirect", 5),
)
PREDICATES = (
    "carrier_size", "successor_in_carrier", "inverse_in_carrier",
    "inverse_after_forward", "forward_after_inverse", "unit_fibre",
    "invariant_matrix", "active_component_bicyclic", "registers_in_core",
    "core_bicyclic", "core_minimum_degree", "core_stored_arrows_internal",
    "frozen_complement", "core_key_invariant", "pruned_arrows_toward_core",
    "orbit_closure", "orbit_no_preperiod", "orbit_partition",
    "orbit_exact_period", "orbit_group_constant", "orbit_anchor_nonempty",
    "group_catalogue_complete", "group_anchor_states", "group_decoration_classes",
    "group_orbit_decoration_bijection", "group_orbit_count", "group_periods",
    "core_catalogue_graph_count", "core_catalogue_orbit_census",
    "core_series_family", "core_series_total", "core_series_hand_control",
    "univariate_rational_identity", "univariate_closed_coefficient",
    "period_weighted_core_identity", "carrier_period_polynomial",
    "carrier_hand_control", "carrier_orbit_total", "carrier_weighted_total",
    "carrier_period_set", "carrier_maximum_period", "carrier_fixed_states",
    "fixed_iterate_count", "seven_row_coverage", "finite_coverage_limits",
    "total_carrier_states",
)
EXCLUDED_CLAIMS = (
    "No finite computation proves the all-n theorem.",
    "No finite observation of the three first-size 5/6/5 families is claimed.",
    "No independent manuscript review, global novelty, priority, or publication acceptance is claimed.",
    "Known kernel, inverse, zero preperiod, unit fibres, invariant, and standard counting are not new axes.",
)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=True, allow_nan=False)


def reject_pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key: " + key)
        result[key] = value
    return result


def reject_number(value):
    raise ValueError("noninteger JSON number: " + value)


def read_parameters(path):
    with open(path, "r", encoding="utf-8") as stream:
        value = json.load(stream, object_pairs_hook=reject_pairs,
                          parse_float=reject_number, parse_constant=reject_number)
    if canonical(value) != canonical(PARAMETERS):
        raise ValueError("PARAMETERS.json must equal the complete fixed contract")
    return value


class Ledger:
    def __init__(self):
        self.records = []

    def check(self, name, scope, observed, expected):
        if name not in PREDICATES:
            raise ValueError("undeclared predicate " + name)
        passed = canonical(observed) == canonical(expected)
        self.records.append({"id": len(self.records), "name": name,
                             "scope": scope, "observed": observed,
                             "expected": expected, "passed": passed})
        return passed

    def census(self):
        return [{"name": name,
                 "checks": sum(r["name"] == name for r in self.records),
                 "failures": sum(r["name"] == name and not r["passed"]
                                 for r in self.records)} for name in PREDICATES]


def state_json(state):
    return {"u": state[0], "v": state[1], "f": list(state[2:])}


def forward(state):
    u, v = state[:2]
    old_f = state[2:]
    changed = list(old_f)
    changed[v - 1] = u
    return (v, old_f[v - 1], *changed)


def inverse(state):
    a, b = state[:2]
    old_g = state[2:]
    changed = list(old_g)
    changed[a - 1] = b
    return (old_g[a - 1], a, *changed)


def blank_matrix(n):
    return [[0 for _ in range(n)] for _ in range(n)]


def change_edge(matrix, a, b, delta):
    matrix[a - 1][b - 1] += delta
    if a != b:
        matrix[b - 1][a - 1] += delta


def matrix_of_state(state):
    n = len(state) - 2
    matrix = blank_matrix(n)
    for a, b in enumerate(state[2:], 1):
        change_edge(matrix, a, b, 1)
    change_edge(matrix, state[0], state[1], 1)
    return matrix


def degree(matrix, vertex, vertices):
    return sum(matrix[vertex - 1][v - 1] for v in vertices) + matrix[vertex - 1][vertex - 1]


def component(matrix, start, allowed):
    reached = {start}
    todo = [start]
    while todo:
        a = todo.pop()
        for b in sorted(allowed):
            if matrix[a - 1][b - 1] and b not in reached:
                reached.add(b)
                todo.append(b)
    return sorted(reached)


def edge_count(matrix, vertices):
    return sum(matrix[a - 1][b - 1] for a in vertices for b in vertices if a <= b)


def upper(matrix, vertices):
    return tuple(matrix[a - 1][b - 1] for a in vertices for b in vertices if a <= b)


def restrict_matrix(matrix, vertices):
    return [[matrix[a - 1][b - 1] for b in vertices] for a in vertices]


def structural_state(state):
    matrix = matrix_of_state(state)
    n = len(matrix)
    active = component(matrix, state[0], range(1, n + 1))
    alive = set(active)
    pruning = []
    while True:
        leaves = [a for a in sorted(alive) if degree(matrix, a, alive) == 1]
        if not leaves:
            break
        a = leaves[0]
        neighbours = [b for b in sorted(alive) if matrix[a - 1][b - 1]]
        pruning.append([a, neighbours[0]])
        alive.remove(a)
    vertices = sorted(alive)
    outside = [a for a in range(1, n + 1) if a not in alive]
    frozen = [[a, state[a + 1]] for a in outside]
    key = (tuple(vertices), upper(matrix, vertices), tuple(state[a + 1] for a in outside))
    return {"matrix": matrix, "active_vertices": active,
            "inactive_vertices": [a for a in range(1, n + 1) if a not in active],
            "pruning": pruning, "core_vertices": vertices,
            "core_matrix": restrict_matrix(matrix, vertices),
            "core_degrees": [degree(matrix, a, vertices) for a in vertices],
            "frozen_complement": frozen, "key": key}


def compositions(total, slots):
    if slots == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for rest in compositions(total - first, slots - 1):
                yield (first, *rest)


def matrix_catalogue(s):
    """Enumerate matrices directly, never by collecting state observations."""
    vertices = list(range(1, s + 1))
    pairs = [(a, b) for a in vertices for b in vertices if a <= b]
    for weights in compositions(s + 1, len(pairs)):
        matrix = blank_matrix(s)
        for (a, b), multiplicity in zip(pairs, weights):
            change_edge(matrix, a, b, multiplicity)
        if all(degree(matrix, a, vertices) >= 2 for a in vertices):
            if component(matrix, 1, vertices) == vertices:
                yield matrix


def classify(matrix, vertices):
    """Consume multiplicities; repeated direct paths stay identical tuples."""
    branches = [a for a in vertices if degree(matrix, a, vertices) > 2]
    residual = [row[:] for row in matrix]
    chains = []
    for start in branches:
        while True:
            neighbours = [b for b in vertices if residual[start - 1][b - 1] > 0]
            if not neighbours:
                break
            nxt = neighbours[0]
            change_edge(residual, start, nxt, -1)
            path = [start, nxt]
            while nxt not in branches:
                candidates = [b for b in vertices if residual[nxt - 1][b - 1] > 0]
                if len(candidates) != 1:
                    raise ValueError("degree-two chain does not have one remaining neighbour")
                following = candidates[0]
                change_edge(residual, nxt, following, -1)
                path.append(following)
                nxt = following
            path = tuple(path)
            chains.append(min(path, path[::-1]))
    if any(residual[a - 1][b - 1] for a in vertices for b in vertices):
        raise ValueError("unconsumed core multiplicity")
    chains.sort()
    if len(branches) == 1 and degree(matrix, branches[0], vertices) == 4:
        if len(chains) != 2 or any(p[0] != p[-1] for p in chains):
            raise ValueError("invalid figure-eight chains")
        family = "figure_eight"
        paths = chains
        lengths = [len(p) - 1 for p in paths]
        a, b = lengths
        if a == b == 1:
            row, period = ROWS[0], 1
        elif max(a, b) <= 2:
            row, period = ROWS[1], a + b
        else:
            row, period = ROWS[2], 2 * (a + b)
        orbit_count = 2 if min(a, b) >= 3 else 1
    elif len(branches) == 2 and all(degree(matrix, a, vertices) == 3 for a in branches):
        closed = [p for p in chains if p[0] == p[-1]]
        joined = [p for p in chains if p[0] != p[-1]]
        if len(closed) == 2 and len(joined) == 1:
            family = "barbell"
            by_root = {p[0]: p for p in closed}
            paths = [by_root[branches[0]], by_root[branches[1]], joined[0]]
            lengths = [len(p) - 1 for p in paths]
            a, b, c = lengths
            row = ROWS[3] if max(a, b) <= 2 else ROWS[4]
            period = (a + b + 2 * c) * (1 if max(a, b) <= 2 else 2)
            orbit_count = 2 if min(a, b) >= 3 else 1
        elif not closed and len(joined) == 3:
            family = "theta"
            paths = sorted(joined)
            lengths = [len(p) - 1 for p in paths]
            direct = sum(length == 1 for length in lengths)
            row = ROWS[5] if direct == 3 else ROWS[6]
            period = 2 if direct == 3 else 2 * sum(lengths)
            orbit_count = 1 if direct >= 2 else 2
        else:
            raise ValueError("invalid degree-three chain pattern")
    else:
        raise ValueError("invalid bicyclic branch degrees")
    return {"family": family, "row": row, "branches": branches,
            "paths": [list(p) for p in paths], "lengths": lengths,
            "predicted_period": period, "predicted_orbit_count": orbit_count}


def rotations(triple):
    return tuple(min(triple[i:] + triple[:i] for i in range(3)))


def cycle_class(bits, lengths):
    reverse = tuple(1 - bit if length >= 3 else 0
                    for bit, length in zip(bits, lengths))
    return min(tuple(bits), reverse)


def signature_json(signature):
    if signature[0] == "cycles":
        return {"kind": "cycle_orientation_class", "value": list(signature[1])}
    return {"kind": "theta_cyclic_order", "value": [list(t) for t in signature[1]]}


def expected_anchors(n, description, frozen):
    """Construct literal anchor states from graph orientations, without R."""
    paths = [tuple(p) for p in description["paths"]]
    family = description["family"]
    anchors = {}

    def finish(pointers, u, v, raw, signature):
        if sorted(pointers) != list(range(1, n + 1)):
            raise ValueError("anchor construction leaves a pointer unspecified")
        state = (u, v, *(pointers[a] for a in range(1, n + 1)))
        value = {"raw": raw, "signature": signature}
        if state in anchors and anchors[state] != value:
            raise ValueError("hidden edge identity changed a literal anchor decoration")
        anchors[state] = value

    def point_interior(pointers, path):
        for a, b in zip(path[1:-1], path[2:]):
            pointers[a] = b

    if family != "theta":
        lengths = description["lengths"][:2]
        possibilities = [range(2) if length >= 3 else range(1) for length in lengths]
        for bits in itertools.product(*possibilities):
            oriented = [p[::-1] if bit else p for p, bit in zip(paths[:2], bits)]
            pointers = dict(frozen)
            for p in oriented:
                point_interior(pointers, p)
            a = description["branches"][0]
            if family == "figure_eight":
                pointers[a] = oriented[1][1]
                v = oriented[0][1]
            else:
                b = description["branches"][1]
                pointers[a] = oriented[0][1]
                pointers[b] = oriented[1][1]
                point_interior(pointers, paths[2])
                v = paths[2][1]
            finish(pointers, a, v, list(bits), ("cycles", cycle_class(bits, lengths)))
    else:
        a, b = description["branches"]
        tokens = [p[1:-1] for p in paths]
        token_path = {p[1:-1]: p for p in paths}
        for roles in sorted(set(itertools.permutations(tokens))):
            extra, stored, incoming = [token_path[token] for token in roles]
            pointers = dict(frozen)
            point_interior(pointers, extra)
            point_interior(pointers, stored)
            point_interior(pointers, incoming[::-1])
            pointers[a] = stored[1]
            pointers[b] = incoming[-2]
            finish(pointers, a, extra[1], [list(t) for t in roles],
                   ("theta", rotations(roles)))
    return anchors


def observed_anchor(state, description):
    """Decode only observable registers/destinations at the chosen anchor."""
    u, v = state[:2]
    f = state[2:]
    paths = [tuple(p) for p in description["paths"]]
    a = description["branches"][0]
    if u != a:
        return None
    family = description["family"]
    if family == "theta":
        tokens = [p[1:-1] for p in paths]
        remaining = list(tokens)
        roles = []
        for destination in (v, f[a - 1]):
            choices = sorted(set(p[1:-1] for p in paths
                                 if p[1] == destination and p[1:-1] in remaining))
            if len(choices) != 1:
                raise ValueError("theta role not identifiable from actual destination")
            token = choices[0]
            remaining.remove(token)
            roles.append(token)
        if len(remaining) != 1:
            raise ValueError("theta incoming role is not determined")
        roles.append(remaining[0])
        return {"raw": [list(t) for t in roles],
                "signature": ("theta", rotations(tuple(roles)))}
    if family == "figure_eight":
        if v not in (paths[0][1], paths[0][-2]):
            return None
        starts = [v, f[a - 1]]
    else:
        if v != paths[2][1]:
            return None
        starts = [f[root - 1] for root in description["branches"]]
    bits = []
    for p, start in zip(paths[:2], starts):
        if start == p[1]:
            bits.append(0)
        elif len(p) - 1 >= 3 and start == p[-2]:
            bits.append(1)
        else:
            raise ValueError("cycle orientation not identifiable from actual destination")
    return {"raw": bits,
            "signature": ("cycles", cycle_class(bits, description["lengths"][:2]))}


def term(s, p, value=1):
    return {(s, p): Fraction(value)} if s <= 4 and value else {}


def add(*series):
    result = {}
    for source in series:
        for key, value in source.items():
            result[key] = result.get(key, Fraction(0)) + value
    return {key: value for key, value in result.items() if value}


def scale(series, factor):
    return {key: value * factor for key, value in series.items() if value * factor}


def multiply(left, right):
    result = {}
    for (s1, p1), a in left.items():
        for (s2, p2), b in right.items():
            if s1 + s2 <= 4:
                key = (s1 + s2, p1 + p2)
                result[key] = result.get(key, Fraction(0)) + a * b
    return {key: value for key, value in result.items() if value}


def power(series, exponent):
    result = term(0, 0)
    for _ in range(exponent):
        result = multiply(result, series)
    return result


def geometric(q_step):
    return {(s, q_step * s): Fraction(1) for s in range(5)}


def rational_series():
    x = term(1, 2)
    one = term(0, 0)
    g2 = geometric(2)
    q_series = multiply(x, g2)
    d_series = add(power(g2, 2), scale(power(add(one, x), 2), -1))
    figure = add(term(1, 1), term(2, 3), term(3, 4, Fraction(1, 2)),
                 scale(multiply(term(1, 4), d_series), Fraction(1, 4)))
    barbell = add(scale(multiply(multiply(term(2, 4),
                                        power(add(one, term(1, 1)), 2)), g2), Fraction(1, 2)),
                  scale(multiply(multiply(term(2, 8), d_series), geometric(4)), Fraction(1, 4)))
    theta = add(term(2, 2, Fraction(1, 2)),
                scale(multiply(term(2, 6), add(q_series, power(q_series, 2),
                                               scale(power(q_series, 3), Fraction(1, 3)))),
                      Fraction(1, 2)))
    pieces = {"figure_eight": figure, "barbell": barbell, "theta": theta}
    return pieces, add(*pieces.values())


def fraction_json(value):
    value = Fraction(value)
    return [value.numerator, value.denominator]


def polynomial_json(poly):
    return [[p, *fraction_json(value)] for p, value in sorted(poly.items()) if value]


def series_json(series):
    return [[s, p, *fraction_json(value)] for (s, p), value in sorted(series.items()) if value]


def by_size(series, s):
    return {p: value for (size, p), value in series.items() if size == s}


def count_periods(periods):
    result = {}
    for p in periods:
        result[p] = result.get(p, 0) + 1
    return result


def predicted_period_set(n):
    return [1] if n == 1 else list(range(1, 2 * n + 1)) + list(range(2 * n + 2, 4 * n - 3, 2))


CORE_CONTROLS = {
    1: {1: Fraction(1)},
    2: {2: Fraction(1, 2), 3: Fraction(1), 4: Fraction(1, 2)},
    3: {4: Fraction(1, 2), 5: Fraction(1), 6: Fraction(1, 2), 8: Fraction(1)},
    4: {6: Fraction(1, 2), 7: Fraction(1), 8: Fraction(1, 2), 10: Fraction(2), 12: Fraction(1, 2)},
}
CARRIER_CONTROLS = {
    1: {1: 1},
    2: {1: 4, 2: 1, 3: 2, 4: 1},
    3: {1: 27, 2: 9, 3: 18, 4: 12, 5: 6, 6: 3, 8: 6},
    4: {1: 256, 2: 96, 3: 192, 4: 144, 5: 96, 6: 60, 7: 24, 8: 108, 10: 48, 12: 12},
}


def core_catalogues():
    result = {}
    for s in range(1, 5):
        entries = []
        for matrix in matrix_catalogue(s):
            description = classify(matrix, list(range(1, s + 1)))
            entries.append({"catalogue_id": len(entries), "s": s,
                            "matrix": matrix, "upper": list(upper(matrix, range(1, s + 1))),
                            "description": description})
        result[s] = entries
    return result


def relabel_description(description, vertices):
    result = dict(description)
    result["branches"] = [vertices[a - 1] for a in description["branches"]]
    result["paths"] = [[vertices[a - 1] for a in p] for p in description["paths"]]
    return result


def expected_groups(n, catalogues):
    groups = []
    for s in range(1, n + 1):
        for vertices in itertools.combinations(range(1, n + 1), s):
            outside = [a for a in range(1, n + 1) if a not in vertices]
            for entry in catalogues[s]:
                description = relabel_description(entry["description"], vertices)
                for targets in itertools.product(range(1, n + 1), repeat=n - s):
                    frozen = list(zip(outside, targets))
                    key = (vertices, tuple(entry["upper"]), targets)
                    groups.append({"id": len(groups), "key": key, "core_vertices": list(vertices),
                                   "catalogue_id": entry["catalogue_id"], "s": s,
                                   "core_matrix": entry["matrix"], "description": description,
                                   "frozen_complement": [list(pair) for pair in frozen],
                                   "expected_anchors": expected_anchors(n, description, frozen)})
    return groups


def verify_carrier(n, catalogues, total_series, ledger):
    scope = "n=" + str(n)
    states = list(itertools.product(range(1, n + 1), repeat=n + 2))
    index = {state: i for i, state in enumerate(states)}
    successors = [index[forward(state)] for state in states]
    inverses = [index[inverse(state)] for state in states]
    structural = [structural_state(state) for state in states]
    groups = expected_groups(n, catalogues)
    group_by_key = {group["key"]: group for group in groups}
    observed_group_keys = set(item["key"] for item in structural)
    expected_group_keys = set(group_by_key)
    ledger.check("carrier_size", scope, len(states), n ** (n + 2))
    ledger.check("group_catalogue_complete", scope,
                 sorted(observed_group_keys), sorted(expected_group_keys))
    if observed_group_keys != expected_group_keys:
        raise ValueError("actual core/complement catalogue differs; in-memory predicate is not emitted")
    fibres = [[] for _ in states]
    for source, target in enumerate(successors):
        fibres[target].append(source)
    orbit_for = [None for _ in states]
    orbits = []
    for seed in range(len(states)):
        if orbit_for[seed] is not None:
            continue
        cycle = []
        local = {}
        current = seed
        while current not in local and orbit_for[current] is None:
            local[current] = len(cycle)
            cycle.append(current)
            current = successors[current]
        orbit_id = len(orbits)
        oscope = scope + "/orbit=" + str(orbit_id)
        ledger.check("orbit_closure", oscope, current, seed)
        ledger.check("orbit_no_preperiod", oscope, local.get(current), 0)
        if current != seed:
            raise ValueError("literal graph is not a disjoint union of cycles")
        for state_id in cycle:
            orbit_for[state_id] = orbit_id
        group = group_by_key[structural[seed]["key"]]
        description = group["description"]
        ledger.check("orbit_exact_period", oscope, len(cycle), description["predicted_period"])
        ledger.check("orbit_group_constant", oscope,
                     sorted(set(structural[i]["key"] for i in cycle)), [group["key"]])
        anchors = []
        for phase, state_id in enumerate(cycle):
            decoded = observed_anchor(states[state_id], description)
            if decoded is not None:
                anchors.append({"phase": phase, "state_id": state_id,
                                "raw_decoration": decoded["raw"],
                                "class": signature_json(decoded["signature"])})
        ledger.check("orbit_anchor_nonempty", oscope, bool(anchors), True)
        orbits.append({"id": orbit_id, "representative_state_id": seed,
                       "state_ids_in_time_order": cycle, "preperiod": 0,
                       "period": len(cycle), "group_id": group["id"], "anchors": anchors})
    ledger.check("orbit_partition", scope,
                 sorted(i for orbit in orbits for i in orbit["state_ids_in_time_order"]),
                 list(range(len(states))))
    state_rows = []
    grouped_states = {group["id"]: [] for group in groups}
    for state_id, state in enumerate(states):
        sscope = scope + "/state=" + str(state_id)
        data = structural[state_id]
        next_data = structural[successors[state_id]]
        group_id = group_by_key[data["key"]]["id"]
        grouped_states[group_id].append(state_id)
        ledger.check("successor_in_carrier", sscope, forward(state) in index, True)
        ledger.check("inverse_in_carrier", sscope, inverse(state) in index, True)
        ledger.check("inverse_after_forward", sscope, inverse(forward(state)), state)
        ledger.check("forward_after_inverse", sscope, forward(inverse(state)), state)
        ledger.check("unit_fibre", sscope, fibres[state_id], [inverses[state_id]])
        ledger.check("invariant_matrix", sscope, next_data["matrix"], data["matrix"])
        ledger.check("active_component_bicyclic", sscope,
                     edge_count(data["matrix"], data["active_vertices"]), len(data["active_vertices"]) + 1)
        ledger.check("registers_in_core", sscope,
                     [state[0] in data["core_vertices"], state[1] in data["core_vertices"]], [True, True])
        ledger.check("core_bicyclic", sscope,
                     edge_count(data["matrix"], data["core_vertices"]), len(data["core_vertices"]) + 1)
        ledger.check("core_minimum_degree", sscope, min(data["core_degrees"]) >= 2, True)
        ledger.check("core_stored_arrows_internal", sscope,
                     [state[a + 1] in data["core_vertices"] for a in data["core_vertices"]],
                     [True for _ in data["core_vertices"]])
        ledger.check("frozen_complement", sscope, next_data["frozen_complement"], data["frozen_complement"])
        ledger.check("core_key_invariant", sscope, next_data["key"], data["key"])
        ledger.check("pruned_arrows_toward_core", sscope,
                     [[a, state[a + 1]] for a, _ in data["pruning"]], data["pruning"])
        state_rows.append({"id": state_id, "state": state_json(state),
                           "successor_id": successors[state_id], "inverse_id": inverses[state_id],
                           "inverse_state": state_json(inverse(state)), "preimage_ids": fibres[state_id],
                           "orbit_id": orbit_for[state_id], "group_id": group_id,
                           "invariant": {k: v for k, v in data.items() if k != "key"}})
    group_rows = []
    for group in groups:
        group_id = group["id"]
        gscope = scope + "/group=" + str(group_id)
        state_ids = grouped_states[group_id]
        orbit_ids = sorted(set(orbit_for[i] for i in state_ids))
        description = group["description"]
        actual_anchors = {}
        class_to_orbits = {}
        for state_id in state_ids:
            decoded = observed_anchor(states[state_id], description)
            if decoded is not None:
                actual_anchors[states[state_id]] = decoded
                class_to_orbits.setdefault(decoded["signature"], set()).add(orbit_for[state_id])
        expected_anchor_map = group["expected_anchors"]
        expected_classes = sorted(set(item["signature"] for item in expected_anchor_map.values()))
        actual_classes = sorted(class_to_orbits)
        ledger.check("group_anchor_states", gscope,
                     [[state, item["raw"], signature_json(item["signature"])]
                      for state, item in sorted(actual_anchors.items())],
                     [[state, item["raw"], signature_json(item["signature"])]
                      for state, item in sorted(expected_anchor_map.items())])
        ledger.check("group_decoration_classes", gscope,
                     [signature_json(s) for s in actual_classes],
                     [signature_json(s) for s in expected_classes])
        class_partition = [sorted(class_to_orbits[s]) for s in actual_classes]
        ledger.check("group_orbit_decoration_bijection", gscope,
                     sorted(class_partition), [[i] for i in orbit_ids])
        ledger.check("group_orbit_count", gscope, len(orbit_ids), description["predicted_orbit_count"])
        ledger.check("group_periods", gscope,
                     [orbits[i]["period"] for i in orbit_ids],
                     [description["predicted_period"] for _ in orbit_ids])
        group_rows.append({"id": group_id, "s": group["s"],
                           "catalogue_id": group["catalogue_id"],
                           "core_vertices": group["core_vertices"], "core_matrix": group["core_matrix"],
                           "description": description, "frozen_complement": group["frozen_complement"],
                           "state_ids": state_ids, "orbit_ids": orbit_ids,
                           "expected_anchors": [{"state": state_json(state), "state_id": index[state],
                                                 "raw_decoration": item["raw"],
                                                 "class": signature_json(item["signature"])}
                                                for state, item in sorted(expected_anchor_map.items())],
                           "observed_anchor_state_ids": [index[state] for state in sorted(actual_anchors)],
                           "expected_classes": [signature_json(s) for s in expected_classes],
                           "observed_classes": [{"class": signature_json(s),
                                                 "orbit_ids": sorted(class_to_orbits[s])}
                                                for s in actual_classes]})
    observed_poly = count_periods(orbit["period"] for orbit in orbits)
    contributions = []
    expected_poly = {}
    for s in range(1, n + 1):
        multiplier = math.factorial(n) // math.factorial(n - s) * n ** (n - s)
        core_poly = by_size(total_series, s)
        piece = {p: value * multiplier for p, value in core_poly.items()}
        for p, value in piece.items():
            expected_poly[p] = expected_poly.get(p, Fraction(0)) + value
        contributions.append({"s": s, "falling_factorial": math.factorial(n) // math.factorial(n - s),
                              "complement_map_count": n ** (n - s),
                              "multiplier": multiplier, "core_coefficients": polynomial_json(core_poly),
                              "contribution": polynomial_json(piece)})
    ledger.check("carrier_period_polynomial", scope, polynomial_json(observed_poly), polynomial_json(expected_poly))
    ledger.check("carrier_hand_control", scope, polynomial_json(observed_poly), polynomial_json(CARRIER_CONTROLS[n]))
    ledger.check("carrier_orbit_total", scope, len(orbits), sum(CARRIER_CONTROLS[n].values()))
    ledger.check("carrier_weighted_total", scope, sum(p * c for p, c in observed_poly.items()), len(states))
    ledger.check("carrier_period_set", scope, sorted(observed_poly), predicted_period_set(n))
    ledger.check("carrier_maximum_period", scope, max(observed_poly), 1 if n == 1 else 4 * n - 4)
    fixed_ids = [i for i, target in enumerate(successors) if i == target]
    ledger.check("carrier_fixed_states", scope, len(fixed_ids), n ** n)
    fixed_iterates = []
    iterate_targets = list(range(len(states)))
    for k in range(1, max(predicted_period_set(n)) + 1):
        iterate_targets = [successors[i] for i in iterate_targets]
        fixed = [i for i, target in enumerate(iterate_targets) if i == target]
        expected = sum(p * c for p, c in expected_poly.items() if k % p == 0)
        ledger.check("fixed_iterate_count", scope + "/k=" + str(k),
                     fraction_json(len(fixed)), fraction_json(expected))
        fixed_iterates.append({"k": k, "fixed_state_ids": fixed, "observed_count": len(fixed),
                               "expected_count": fraction_json(expected)})
    row_coverage = []
    for row, first_size in zip(ROWS, ROW_FIRST_SIZES):
        matching = [g for g in group_rows if g["description"]["row"] == row]
        ledger.check("seven_row_coverage", scope + "/row=" + row, bool(matching), n >= first_size)
        row_coverage.append({"row": row, "group_ids": [g["id"] for g in matching],
                             "first_core_size": first_size,
                             "observed_present": bool(matching), "expected_present": n >= first_size,
                             "group_count": len(matching),
                             "orbit_count": sum(len(g["orbit_ids"]) for g in matching),
                             "state_count": sum(len(g["state_ids"]) for g in matching)})
    ledger.check("seven_row_coverage", scope, sum(r["state_count"] for r in row_coverage), len(states))
    return {"n": n, "state_count": len(states), "states": state_rows,
            "orbits": orbits, "groups": group_rows, "row_coverage": row_coverage,
            "period_polynomial_observed": polynomial_json(observed_poly),
            "period_polynomial_expected": polynomial_json(expected_poly),
            "extension_contributions": contributions, "orbit_count": len(orbits),
            "period_set": sorted(observed_poly), "maximum_period": max(observed_poly),
            "fixed_state_ids": fixed_ids, "fixed_iterates": fixed_iterates}


def verify_series(catalogues, carriers, pieces, total, ledger):
    records = []
    numerator = add(term(1, 0), term(2, 0, -1), term(4, 0, Fraction(1, 2)),
                    term(5, 0, Fraction(-1, 12)))
    univariate = multiply(numerator, power(geometric(0), 3))
    for s in range(1, 5):
        scope = "core_size=" + str(s)
        carrier = carriers[s - 1]
        pure_groups = [g for g in carrier["groups"] if g["s"] == s]
        ledger.check("core_catalogue_graph_count", scope, len(pure_groups), len(catalogues[s]))
        family_records = []
        total_observed = {}
        for family in FAMILIES:
            observed = {}
            for group in pure_groups:
                if group["description"]["family"] != family:
                    continue
                periods = [carrier["orbits"][i]["period"] for i in group["orbit_ids"]]
                for p, count in count_periods(periods).items():
                    observed[p] = observed.get(p, Fraction(0)) + Fraction(count, math.factorial(s))
            expected = by_size(pieces[family], s)
            ledger.check("core_series_family", scope + "/" + family,
                         polynomial_json(observed), polynomial_json(expected))
            for p, count in observed.items():
                total_observed[p] = total_observed.get(p, Fraction(0)) + count
            family_records.append({"family": family,
                                   "observed_coefficients": polynomial_json(observed),
                                   "expected_coefficients": polynomial_json(expected)})
        for entry, group in zip(catalogues[s], pure_groups):
            observed_count = len(group["orbit_ids"])
            ledger.check("core_catalogue_orbit_census", scope + "/catalogue=" + str(entry["catalogue_id"]),
                         observed_count, entry["description"]["predicted_orbit_count"])
        expected_total = by_size(total, s)
        ledger.check("core_series_total", scope, polynomial_json(total_observed), polynomial_json(expected_total))
        ledger.check("core_series_hand_control", scope, polynomial_json(expected_total), polynomial_json(CORE_CONTROLS[s]))
        coefficient = sum(expected_total.values(), Fraction(0))
        closed = Fraction(1) if s == 1 else Fraction(2) if s == 2 else Fraction(5 * s * s + s + 24, 24)
        weighted = sum(p * c for p, c in expected_total.items())
        ledger.check("univariate_rational_identity", scope, fraction_json(coefficient), fraction_json(univariate.get((s, 0), 0)))
        ledger.check("univariate_closed_coefficient", scope, fraction_json(coefficient), fraction_json(closed))
        ledger.check("period_weighted_core_identity", scope, fraction_json(weighted), fraction_json(Fraction(s * s * (s + 1), 2)))
        records.append({"s": s, "families": family_records,
                        "observed_coefficients": polynomial_json(total_observed),
                        "expected_coefficients": polynomial_json(expected_total),
                        "hand_control": polynomial_json(CORE_CONTROLS[s]),
                        "univariate_coefficient": fraction_json(coefficient),
                        "closed_coefficient": fraction_json(closed),
                        "period_weighted_coefficient": fraction_json(weighted),
                        "labelled_orbit_counts": polynomial_json({p: c * math.factorial(s) for p, c in total_observed.items()})})
    return {"max_core_size": 4,
            "pieces": [{"family": name, "terms": series_json(pieces[name])} for name in FAMILIES],
            "total_terms": series_json(total), "coefficient_checks": records,
            "control_provenance": "Deductive rational expansions in the admitted MATHEMATICAL_AUDIT.md; not prior executed results."}


def coverage(carriers, ledger):
    results = []
    for name, first_size in LIMITS:
        witnesses = []
        for carrier in carriers:
            for group in carrier["groups"]:
                d = group["description"]
                match = ((name == LIMITS[0][0] and d["family"] == "figure_eight" and min(d["lengths"]) >= 3)
                         or (name == LIMITS[1][0] and d["family"] == "barbell" and min(d["lengths"][:2]) >= 3)
                         or (name == LIMITS[2][0] and d["family"] == "theta" and min(d["lengths"]) >= 2))
                if match:
                    witnesses.append([carrier["n"], group["id"]])
        ledger.check("finite_coverage_limits", name, witnesses, [])
        results.append({"family": name, "first_core_size": first_size,
                        "observed_group_references": witnesses,
                        "finite_status": "not_exercised_in_n_1_2_3_4",
                        "theorem_status": "deductively_covered_by_all_parameter_anchor_argument"})
    return results


def main():
    if len(sys.argv) != 3 or sys.argv[1] != "--parameters":
        raise ValueError("exact interface: verify.py --parameters ABSOLUTE_PARAMETERS_JSON")
    if not sys.argv[2].startswith("/"):
        raise ValueError("parameter input must be an explicit absolute path")
    parameters = read_parameters(sys.argv[2])
    ledger = Ledger()
    catalogues = core_catalogues()
    pieces, total_series = rational_series()
    carriers = [verify_carrier(n, catalogues, total_series, ledger) for n in parameters["carrier_sizes"]]
    series_record = verify_series(catalogues, carriers, pieces, total_series, ledger)
    limits = coverage(carriers, ledger)
    ledger.check("total_carrier_states", "all_carriers", sum(c["state_count"] for c in carriers), 4356)
    failures = [record["id"] for record in ledger.records if not record["passed"]]
    output = {"schema": "p212-full-output-v1", "parameters": parameters,
              "role": "author_verifier_not_independent_review",
              "method": "literal_state_graph_vs_multiplicity_catalogue_observable_anchors_and_Fraction_series",
              "excluded_claims": list(EXCLUDED_CLAIMS),
              "core_catalogues": [{"s": s, "entries": catalogues[s]} for s in range(1, 5)],
              "carriers": carriers, "series": series_record, "coverage_limits": limits,
              "predicates": ledger.records, "predicate_census": ledger.census(),
              "summary": {"carrier_sizes": [1, 2, 3, 4], "state_count": sum(c["state_count"] for c in carriers),
                          "orbit_counts": [c["orbit_count"] for c in carriers],
                          "predicate_count": len(ledger.records), "failure_ids": failures,
                          "passed": not failures}}
    encoded = (canonical(output) + "\n").encode("ascii")
    sys.stdout.buffer.write(encoded)
    sys.stdout.buffer.flush()
    return 0 if not failures else 1


if __name__ == "__main__":
    try:
        code = main()
    except Exception as error:
        sys.stderr.write("P212 verifier failure: " + type(error).__name__ + ": " + str(error) + "\n")
        code = 2
    raise SystemExit(code)
