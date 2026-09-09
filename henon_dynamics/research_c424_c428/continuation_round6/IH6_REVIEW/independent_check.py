"""Independent exact IH6 reconstruction; no imports from the author's package.

Small alphabets: alternating-extreme node order, closed Lagrange coefficient
rows, and exact congruences. Cycles: indegree peeling, not path/done tracing.
Large alphabets: identity graphs plus EVERY nonidentity integer edge root;
no output-range pruning and no numerical representative for the generic graph.
The separately reviewed all-diameter lemma is a mathematical prerequisite.
"""

from collections import deque
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
from math import lcm, prod
import json
import platform
import sys
import time


EXPECTED = {1: {1, 2, 3, 4, 6}, -1: {1, 2, 3, 4, 6, 8}}


def extreme_order(alphabet):
    remaining = deque(alphabet)
    ordered = []
    while remaining:
        ordered.append(remaining.popleft())
        if remaining:
            ordered.append(remaining.pop())
    return tuple(ordered)


def coefficient_rows(nodes):
    """Closed formula for the highest coefficient of each prefix interpolant."""
    rows = []
    for size in range(1, len(nodes) + 1):
        prefix = nodes[:size]
        weights = [Fraction(1, prod(x - y for j, y in enumerate(prefix) if j != i))
                   for i, x in enumerate(prefix)]
        denominator = lcm(*(w.denominator for w in weights))
        integers = tuple(w.numerator * (denominator // w.denominator) for w in weights)
        rows.append((denominator, integers))
    return rows


def integral_interpolation(nodes, values):
    return all(sum(c * v for c, v in zip(row, values)) % denominator == 0
               for denominator, row in coefficient_rows(nodes))


def value_tables(nodes, sign):
    outputs = tuple(sorted({x + sign * y for x in nodes for y in nodes}))
    rows = coefficient_rows(nodes)
    chosen = []

    def extend():
        size = len(chosen)
        if size == len(nodes):
            yield tuple(chosen)
            return
        denominator, row = rows[size]
        previous = sum(c * v for c, v in zip(row[:-1], chosen))
        for value in outputs:
            if (previous + row[-1] * value) % denominator == 0:
                chosen.append(value)
                yield from extend()
                chosen.pop()

    yield from extend()


def full_support_cycles(arrows, alphabet_size):
    """Kahn peeling leaves exactly the cycles of a finite partial function."""
    total = alphabet_size * alphabet_size
    assert len(arrows) == total
    indegree = [0] * total
    for target in arrows:
        if target is not None:
            indegree[target] += 1
    queue = deque(i for i, degree in enumerate(indegree) if degree == 0)
    removed = [False] * total
    while queue:
        vertex = queue.popleft()
        assert not removed[vertex]
        removed[vertex] = True
        target = arrows[vertex]
        if target is not None:
            indegree[target] -= 1
            if indegree[target] == 0:
                queue.append(target)
    seen = set()
    result = []
    for start in range(total):
        if removed[start] or start in seen:
            continue
        orbit = []
        vertex = start
        while vertex not in seen:
            assert not removed[vertex]
            seen.add(vertex)
            orbit.append(vertex)
            vertex = arrows[vertex]
            assert vertex is not None
        assert vertex == start
        support = {label for state in orbit for label in divmod(state, alphabet_size)}
        if len(support) == alphabet_size:
            result.append(tuple(orbit))
    return tuple(result)


def integer_arrows(nodes, values, sign):
    index = {x: i for i, x in enumerate(nodes)}
    assert len(index) == len(nodes)
    size = len(nodes)
    arrows = []
    for x in nodes:
        for j, value in enumerate(values):
            target = index.get(value - sign * x)
            arrows.append(None if target is None else j * size + target)
    return arrows


def controls():
    assert integral_interpolation((0, 1, 2), (0, 1, 4))
    assert integral_interpolation((4, 0, 2), (8, 0, 4))
    assert not integral_interpolation((0, 2), (0, 1))
    nodes, values = (0, 2, 4), (0, 0, 4)
    assert all((values[j] - values[i]) % (nodes[j] - nodes[i]) == 0
               for i, j in combinations(range(3), 2))
    assert not integral_interpolation(nodes, values)
    # State 0 exits; states 1 and 2 form a full-support 2-cycle; state 3 is fixed.
    assert full_support_cycles([None, 2, 1, 3], 2) == ((1, 2),)
    # The partial map has one path and no cycle.
    assert full_support_cycles([1, 2, 3, None], 2) == ()
    # A tail into a cycle tests the general peeling routine beyond injectivity.
    assert full_support_cycles([1, 2, 1, 0], 2) == ((1, 2),)
    return {"interpolation_controls": 4, "cycle_controls": 3,
            "pairwise_congruence_insufficient_control": True}


def small_certificate():
    cumulative = 0
    expected_counts = [2, 20, 168, 838, 2232, 4128, 6862, 11110, 19182, 35778]
    spectra = {sign: set() for sign in EXPECTED}
    rows = []
    digest = sha256()
    for diameter in range(10):
        counts = {sign: 0 for sign in EXPECTED}
        cycles_count = {sign: 0 for sign in EXPECTED}
        alphabets = [(0,)] if diameter == 0 else [
            (0,) + middle + (diameter,)
            for size in range(diameter)
            for middle in combinations(range(1, diameter), size)]
        for alphabet in alphabets:
            nodes = extreme_order(alphabet)
            for sign in EXPECTED:
                for values in value_tables(nodes, sign):
                    counts[sign] += 1
                    cycles = full_support_cycles(integer_arrows(nodes, values, sign), len(nodes))
                    for cycle in cycles:
                        spectra[sign].add(len(cycle))
                        cycles_count[sign] += 1
                        event = (diameter, sign, nodes, values, cycle)
                        digest.update((json.dumps(event, separators=(",", ":")) + "\n").encode())
        cumulative += sum(counts.values())
        assert cumulative == expected_counts[diameter], (diameter, cumulative)
        assert all(spectra[sign] <= EXPECTED[sign] for sign in EXPECTED)
        row = {"diameter": diameter, "alphabet_count": len(alphabets),
               "restrictions": counts, "cumulative_restrictions": cumulative,
               "full_support_cycles": cycles_count,
               "cumulative_spectra": {s: sorted(v) for s, v in spectra.items()}}
        rows.append(row)
        print(json.dumps({"small_progress": row}, sort_keys=True), flush=True)
    assert spectra == EXPECTED
    return {"diameter_scope": [0, 9], "rows": rows,
            "cycle_record_sha256": digest.hexdigest(),
            "restriction_total": cumulative,
            "spectra": {s: sorted(v) for s, v in spectra.items()}}


def plus(first, second, factor=1):
    return first[0] + factor * second[0], first[1] + factor * second[1]


def multiply(value, scalar):
    return scalar * value[0], scalar * value[1]


def all_subsets(items):
    for size in range(1, len(items) + 1):
        yield from combinations(items, size)


def end_models():
    for family in ("left", "right"):
        for distances in all_subsets((1, 2, 3)):
            choices = [(-2, -1, 0, 1, 2) if b == 1 else
                       (-1, 0, 1) if b == 2 else (0,) for b in distances]
            for remainders in product(*choices):
                if not any(remainders):
                    continue
                if any((remainders[j] - remainders[i]) % (distances[j] - distances[i])
                       for i, j in combinations(range(len(distances)), 2)):
                    continue
                interior = [(0, b) if family == "left" else (1, -b) for b in distances]
                yield family, ((0, 0), *interior, (1, 0)), (0, *remainders, 0)
    for left in all_subsets((1, 2)):
        for right in all_subsets((1, 2)):
            bound = min(2 if b == 1 else 1 for b in (*left, *right))
            for h in range(-bound, bound + 1):
                if h == 0:
                    continue
                nodes = ((0, 0), *((0, b) for b in left),
                         *((1, -b) for b in right), (1, 0))
                yield "both", nodes, (0, *((h,) * (len(nodes) - 2)), 0)


def identity_graph_and_roots(nodes, values, sign):
    index = {node: i for i, node in enumerate(nodes)}
    size = len(nodes)
    arrows = []
    roots = set()
    for x in nodes:
        for j, value in enumerate(values):
            next_coordinate = plus(value, x, -sign)
            target = index.get(next_coordinate)
            arrows.append(None if target is None else j * size + target)
            for z in nodes:
                slope, constant = plus(next_coordinate, z, -1)
                if slope and constant % slope == 0:
                    diameter = -constant // slope
                    if diameter >= 10:
                        roots.add(diameter)
    return arrows, roots


def large_certificate():
    stats = {sign: {family: {"templates": 0, "models": 0,
                            "generic_full_support_cycles": 0,
                            "generic_periods": set(), "root_models": 0,
                            "exceptional_graphs": 0, "critical_diameters": set(),
                            "exceptional_full_support_cycles": 0,
                            "exceptional_periods": set()}
                   for family in ("left", "right", "both")} for sign in EXPECTED}
    generic_witnesses = []
    for family, nodes, hvalues in end_models():
        for sign in EXPECTED:
            row = stats[sign][family]
            row["templates"] += 1
            intercepts = sorted({plus(x, y, sign) for x in nodes for y in nodes})
            for intercept in intercepts:
                for slope in (-2, -1, 0, 1, 2):
                    row["models"] += 1
                    values = []
                    for node, h in zip(nodes, hvalues):
                        distance = abs(node[1])
                        correction = (-distance * h, distance * distance * h)
                        values.append(plus(plus(intercept, multiply(node, slope)), correction))
                    arrows, roots = identity_graph_and_roots(nodes, values, sign)
                    cycles = full_support_cycles(arrows, len(nodes))
                    row["generic_full_support_cycles"] += len(cycles)
                    row["generic_periods"].update(map(len, cycles))
                    if cycles:
                        generic_witnesses.append({"sign": sign, "family": family,
                            "nodes": nodes, "h": hvalues, "intercept": intercept,
                            "slope": slope, "cycles": cycles})
                    row["root_models"] += bool(roots)
                    row["exceptional_graphs"] += len(roots)
                    row["critical_diameters"].update(roots)
                    for diameter in sorted(roots):
                        actual_nodes = [alpha * diameter + beta for alpha, beta in nodes]
                        actual_values = [alpha * diameter + beta for alpha, beta in values]
                        cycles = full_support_cycles(integer_arrows(actual_nodes, actual_values, sign), len(nodes))
                        row["exceptional_full_support_cycles"] += len(cycles)
                        row["exceptional_periods"].update(map(len, cycles))
    expected_models = {1: {"left": 1490, "right": 1490, "both": 1120},
                       -1: {"left": 1840, "right": 1840, "both": 1240}}
    for sign, families in stats.items():
        for family, row in families.items():
            assert row["templates"] == (20 if family == "both" else 32)
            assert row["models"] == expected_models[sign][family]
            expected_periods = {4} if sign == -1 and family == "both" else set()
            assert row["generic_periods"] == expected_periods, (sign, family, row)
            assert not row["exceptional_periods"], (sign, family, row)
    clean = {sign: {family: {k: sorted(v) if isinstance(v, set) else v
                           for k, v in row.items()}
                    for family, row in families.items()} for sign, families in stats.items()}
    return {"scope": "every integer D >= 10 after the reviewed three-class lemma",
            "method": "identity graph plus all edge roots; no output pruning",
            "statistics": clean, "generic_witnesses": generic_witnesses}


def verify_witnesses():
    # Coefficients ascending; words transcribed from the submitted theorem.
    witnesses = [
        (1, (0, 0, 1), (0,)),
        (1, (2, -3, 1), (0, 1)),
        (1, (1, -2, 1), (0, 0, 1)),
        (1, (1, -1, 1), (0, 0, 1, 1)),
        (1, (0, 0, 0, 1), (-1, -1, 0, 1, 1, 0)),
        (-1, (0, 0, 1), (0,)),
        (-1, (0, -1, 1), (0, 1)),
        (-1, (2, 0, -3), (-1, 0, 1)),
        (-1, (1, 0, -2), (-1, 0, 0, 1)),
        (-1, (-1, 0, 4, 0, -1), (-2, 1, 0, 0, -1, 2)),
        (-1, (0, -3, 0, 1), (-2, -1, 0, -1, 2, 1, 0, 1)),
    ]
    seen = {sign: set() for sign in EXPECTED}
    for sign, coefficients, word in witnesses:
        period = len(word)
        assert len(coefficients) >= 3 and coefficients[-1] != 0
        states = tuple((word[i], word[(i + 1) % period]) for i in range(period))
        assert len(set(states)) == period
        for i, value in enumerate(word):
            pvalue = sum(c * value ** j for j, c in enumerate(coefficients))
            assert pvalue == word[(i + 1) % period] + sign * word[(i - 1) % period]
        seen[sign].add(period)
    assert seen == EXPECTED
    return {"witness_count": len(witnesses), "all_native_minimal": True,
            "spectra": {sign: sorted(v) for sign, v in seen.items()}}


def main():
    started = time.monotonic()
    result = {"checker": "independent IH6 exact reconstruction",
              "environment": {"python": sys.version, "platform": platform.platform()},
              "controls": controls(), "witnesses": verify_witnesses()}
    result["small"] = small_certificate()
    result["large"] = large_certificate()
    result["elapsed_seconds"] = round(time.monotonic() - started, 6)
    result["status"] = "PASS"
    print(json.dumps(result, indent=2, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
