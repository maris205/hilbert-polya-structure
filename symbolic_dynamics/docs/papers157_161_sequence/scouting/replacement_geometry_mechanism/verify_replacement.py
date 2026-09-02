#!/usr/bin/env python3
"""Exact breadth audit for replacement geometry/mechanism systems.

Every box enumerates its declared finite carrier.  Enumeration is bounded
counterexample pressure, not a proof or an ownership certificate.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations, permutations, product
from math import comb, factorial, gcd, lcm


class Audit:
    def __init__(self) -> None:
        self.assertions = 0
        self.boxes = 0

    def check(self, condition: bool, message: object = "") -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(message or f"assertion {self.assertions} failed")

    def box(self) -> None:
        self.boxes += 1


A = Audit()
LINES: list[str] = []
SINK = ("SINK",)


def emit(line: str) -> None:
    LINES.append(line)


@dataclass(frozen=True)
class GraphSummary:
    fixed: int
    periodic: int
    components: int
    max_tail: int
    cycle_hist: tuple[tuple[int, int], ...]
    indegree_hist: tuple[tuple[int, int], ...]
    edge_sha16: str
    successor: dict
    tail_cycle: dict
    indegrees: Counter


def graph_summary(states, successor) -> GraphSummary:
    states = tuple(states)
    state_set = set(states)
    A.check(len(state_set) == len(states), "duplicate carrier states")
    successor_map = {}
    indegrees = Counter()
    for state in states:
        target = successor(state)
        A.check(target in state_set, ("closure", state, target))
        successor_map[state] = target
        indegrees[target] += 1

    tail_cycle = {}
    cycle_hist: Counter[int] = Counter()
    for start in states:
        if start in tail_cycle:
            continue
        path = []
        local = {}
        cursor = start
        while cursor not in local and cursor not in tail_cycle:
            local[cursor] = len(path)
            path.append(cursor)
            cursor = successor_map[cursor]
        if cursor in local:
            cycle_start = local[cursor]
            period = len(path) - cycle_start
            cycle_hist[period] += 1
            for state in path[cycle_start:]:
                tail_cycle[state] = (0, period)
            distance = 0
            for state in reversed(path[:cycle_start]):
                distance += 1
                tail_cycle[state] = (distance, period)
        else:
            distance, period = tail_cycle[cursor]
            for state in reversed(path):
                distance += 1
                tail_cycle[state] = (distance, period)

    fixed = sum(successor_map[state] == state for state in states)
    periodic = sum(distance == 0 for distance, _ in tail_cycle.values())
    max_tail = max(distance for distance, _ in tail_cycle.values())
    indegree_hist = Counter(indegrees.get(state, 0) for state in states)
    payload = "\n".join(f"{state!r}->{successor_map[state]!r}" for state in states)
    return GraphSummary(
        fixed=fixed,
        periodic=periodic,
        components=sum(cycle_hist.values()),
        max_tail=max_tail,
        cycle_hist=tuple(sorted(cycle_hist.items())),
        indegree_hist=tuple(sorted(indegree_hist.items())),
        edge_sha16=sha256(payload.encode("utf-8")).hexdigest()[:16],
        successor=successor_map,
        tail_cycle=tail_cycle,
        indegrees=indegrees,
    )


def format_hist(hist) -> str:
    return "{" + ",".join(f"{key}:{value}" for key, value in hist) + "}"


def record(handle: str, params: str, states, summary: GraphSummary) -> None:
    emit(
        f"SIG {handle} {params} states={len(states)} fixed={summary.fixed} "
        f"periodic={summary.periodic} components={summary.components} "
        f"max_tail={summary.max_tail} cycles={format_hist(summary.cycle_hist)} "
        f"indegrees={format_hist(summary.indegree_hist)} "
        f"edge_sha16={summary.edge_sha16}"
    )
    A.box()


def phi(number: int) -> int:
    answer = number
    divisor = 2
    cursor = number
    while divisor * divisor <= cursor:
        if cursor % divisor == 0:
            answer -= answer // divisor
            while cursor % divisor == 0:
                cursor //= divisor
        divisor += 1
    if cursor > 1:
        answer -= answer // cursor
    return answer


def divisors(number: int):
    return tuple(value for value in range(1, number + 1) if number % value == 0)


def canonical_projective(vector, prime: int):
    vector = tuple(value % prime for value in vector)
    for value in vector:
        if value:
            inverse = pow(value, -1, prime)
            return tuple(entry * inverse % prime for entry in vector)
    raise ValueError("zero vector has no projective class")


def projective_points(dimension: int, prime: int):
    points = {
        canonical_projective(vector, prime)
        for vector in product(range(prime), repeat=dimension + 1)
        if any(vector)
    }
    return tuple(sorted(points))


# ---------------------------------------------------------------------------
# BST: binary-projective Steiner triangle collapse.


def steiner_star(left: int, right: int) -> int:
    return left if left == right else left ^ right


def bst_class(state) -> str:
    left, middle, right = state
    distinct = len({left, middle, right})
    if distinct == 1:
        return "diagonal"
    if distinct == 2:
        return "two_equal"
    return "block" if left ^ middle ^ right == 0 else "nonblock"


def run_bst(rank: int) -> None:
    points = tuple(range(1, 2 ** rank))
    states = tuple(product(points, repeat=3))

    def successor(state):
        left, middle, right = state
        return (
            steiner_star(middle, right),
            steiner_star(right, left),
            steiner_star(left, middle),
        )

    summary = graph_summary(states, successor)
    size = len(points)
    fixed = size ** 2
    three_cycles = size * (size - 1)
    transient = size * (size - 1) * (size - 3)
    expected_cycles = Counter({1: fixed, 3: three_cycles})
    expected_cycles = Counter({key: value for key, value in expected_cycles.items() if value})
    A.check(Counter(dict(summary.cycle_hist)) == expected_cycles)
    A.check(summary.fixed == fixed)
    A.check(summary.periodic == 4 * size * size - 3 * size)
    A.check(summary.max_tail == (1 if size > 3 else 0))
    A.check(len(states) - summary.periodic == transient)
    for state in states:
        kind = bst_class(state)
        expected_depth = 1 if kind == "nonblock" else 0
        A.check(summary.tail_cycle[state][0] == expected_depth, (rank, state, kind))
        if kind == "nonblock":
            A.check(bst_class(summary.successor[state]) == "block")
        expected_fibre = size - 2 if kind == "block" else (0 if kind == "nonblock" else 1)
        A.check(summary.indegrees.get(state, 0) == expected_fibre,
                ("BST fibre", rank, state, kind))
    record("BST", f"rank={rank} points={size}", states, summary)


# ---------------------------------------------------------------------------
# ORT: orthocenter sliding-window rotation with a singular sink.


def sub_point(left, right, prime: int):
    return ((left[0] - right[0]) % prime, (left[1] - right[1]) % prime)


def dot(left, right, prime: int) -> int:
    return (left[0] * right[0] + left[1] * right[1]) % prime


def area(left, middle, right, prime: int) -> int:
    u = sub_point(middle, left, prime)
    v = sub_point(right, left, prime)
    return (u[0] * v[1] - u[1] * v[0]) % prime


def orthocenter(left, middle, right, prime: int):
    u = sub_point(middle, right, prime)
    v = sub_point(left, right, prime)
    rhs_u = dot(left, u, prime)
    rhs_v = dot(middle, v, prime)
    determinant = (u[0] * v[1] - u[1] * v[0]) % prime
    A.check(determinant != 0, ("orthocenter determinant", left, middle, right))
    inverse = pow(determinant, -1, prime)
    x = (rhs_u * v[1] - u[1] * rhs_v) * inverse % prime
    y = (u[0] * rhs_v - rhs_u * v[0]) * inverse % prime
    return (x, y)


def right_vertex(triangle, prime: int):
    left, middle, right = triangle
    tests = (
        dot(sub_point(middle, left, prime), sub_point(right, left, prime), prime),
        dot(sub_point(left, middle, prime), sub_point(right, middle, prime), prime),
        dot(sub_point(left, right, prime), sub_point(middle, right, prime), prime),
    )
    zeros = [index for index, value in enumerate(tests) if value == 0]
    A.check(len(zeros) <= 1, ("multiple right angles", prime, triangle, tests))
    return zeros[0] if zeros else None


def run_ort(prime: int) -> None:
    A.check(prime % 4 == 3)
    points = tuple(product(range(prime), repeat=2))
    triangles = tuple(
        (left, middle, right)
        for left in points
        for middle in points
        for right in points
        if area(left, middle, right, prime) != 0
    )
    states = triangles + (SINK,)

    def successor(state):
        if state == SINK:
            return SINK
        left, middle, right = state
        height = orthocenter(left, middle, right, prime)
        target = (middle, right, height)
        return target if area(*target, prime) != 0 else SINK

    summary = graph_summary(states, successor)
    total = prime ** 2 * (prime ** 2 - 1) * (prime ** 2 - prime)
    right_each = prime ** 2 * (prime ** 2 - 1) * (prime - 1)
    nonright = total - 3 * right_each
    A.check(len(triangles) == total)
    expected_cycles = Counter({1: 1})
    if nonright:
        A.check(nonright % 4 == 0)
        expected_cycles[4] = nonright // 4
    A.check(Counter(dict(summary.cycle_hist)) == expected_cycles)
    A.check(summary.periodic == nonright + 1)
    A.check(summary.max_tail == 2)
    A.check(summary.indegrees[SINK] == 1 + 2 * right_each)
    for triangle in triangles:
        right_at = right_vertex(triangle, prime)
        expected_depth = 0 if right_at is None else (2 if right_at == 0 else 1)
        expected_fibre = 0 if right_at in (0, 1) else 1
        A.check(summary.tail_cycle[triangle][0] == expected_depth,
                ("ORT depth", prime, triangle, right_at))
        A.check(summary.indegrees.get(triangle, 0) == expected_fibre,
                ("ORT fibre", prime, triangle, right_at))
        if right_at is None:
            cursor = triangle
            for _ in range(4):
                cursor = summary.successor[cursor]
            A.check(cursor == triangle, ("ORT fourth iterate", prime, triangle))
    record("ORT", f"p={prime}", states, summary)


# ---------------------------------------------------------------------------
# CRE: totalized standard Cremona reciprocal on projective space.


def run_cre(prime: int, dimension: int) -> None:
    A.check(dimension >= 2)
    points = projective_points(dimension, prime)
    states = points + (SINK,)

    def successor(state):
        if state == SINK:
            return SINK
        support = sum(value != 0 for value in state)
        if support <= dimension - 1:
            return SINK
        output = []
        for omitted in range(dimension + 1):
            value = 1
            for index, entry in enumerate(state):
                if index != omitted:
                    value = value * entry % prime
            output.append(value)
        return canonical_projective(output, prime)

    summary = graph_summary(states, successor)
    low = sum(comb(dimension + 1, support) * (prime - 1) ** (support - 1)
              for support in range(1, dimension))
    hyperface = (dimension + 1) * (prime - 1) ** (dimension - 1)
    torus = (prime - 1) ** dimension
    root_two = gcd(2, prime - 1)
    fixed_torus = root_two ** dimension
    expected_cycles = Counter({1: 1 + fixed_torus})
    if torus > fixed_torus:
        expected_cycles[2] = (torus - fixed_torus) // 2
    A.check(Counter(dict(summary.cycle_hist)) == expected_cycles)
    A.check(summary.periodic == torus + 1)
    A.check(summary.max_tail == 2)
    for state in points:
        support = sum(value != 0 for value in state)
        expected_depth = 0 if support == dimension + 1 else (2 if support == dimension else 1)
        A.check(summary.tail_cycle[state][0] == expected_depth,
                ("CRE depth", prime, dimension, state))
        if support == dimension + 1:
            A.check(summary.successor[summary.successor[state]] == state)
        if support == 1:
            expected_fibre = (prime - 1) ** (dimension - 1)
        elif support == dimension + 1:
            expected_fibre = 1
        else:
            expected_fibre = 0
        A.check(summary.indegrees.get(state, 0) == expected_fibre,
                ("CRE fibre", prime, dimension, state))
    A.check(summary.indegrees[SINK] == 1 + low)
    A.check(len(states) == 1 + low + hyperface + torus)
    record("CRE", f"p={prime} d={dimension}", states, summary)


# ---------------------------------------------------------------------------
# REF: reflection billiard on the anisotropic unit conic.


def run_ref(prime: int) -> None:
    A.check(prime % 4 == 3)
    circle = tuple(
        point for point in product(range(prime), repeat=2)
        if dot(point, point, prime) == 1
    )
    states = tuple(product(circle, repeat=2))

    def successor(state):
        left, right = state
        scale = 2 * dot(left, right, prime) % prime
        reflected = (
            (scale * right[0] - left[0]) % prime,
            (scale * right[1] - left[1]) % prime,
        )
        return right, reflected

    summary = graph_summary(states, successor)
    order = prime + 1
    A.check(len(circle) == order)
    expected_cycles = Counter({period: phi(period) * order // period
                               for period in divisors(order)})
    A.check(Counter(dict(summary.cycle_hist)) == expected_cycles)
    A.check(summary.periodic == order ** 2)
    A.check(summary.max_tail == 0)
    A.check(summary.indegree_hist == ((1, order ** 2),))
    record("REF", f"p={prime} conic={order}", states, summary)


# ---------------------------------------------------------------------------
# QIV: quadratic inversion with the isotropic cone sent to a sink.


def run_qiv(prime: int) -> None:
    A.check(prime % 4 == 1)
    vectors = tuple(product(range(prime), repeat=2))
    states = vectors + (SINK,)

    def successor(state):
        if state == SINK:
            return SINK
        norm = dot(state, state, prime)
        if norm == 0:
            return SINK
        inverse = pow(norm, -1, prime)
        return state[0] * inverse % prime, state[1] * inverse % prime

    summary = graph_summary(states, successor)
    isotropic = 2 * prime - 1
    anisotropic = (prime - 1) ** 2
    unit = prime - 1
    expected_cycles = Counter({1: unit + 1, 2: (anisotropic - unit) // 2})
    A.check(Counter(dict(summary.cycle_hist)) == expected_cycles)
    A.check(summary.periodic == anisotropic + 1)
    A.check(summary.max_tail == 1)
    A.check(summary.indegrees[SINK] == isotropic + 1)
    for vector in vectors:
        norm = dot(vector, vector, prime)
        expected_depth = 1 if norm == 0 else 0
        expected_fibre = 0 if norm == 0 else 1
        A.check(summary.tail_cycle[vector][0] == expected_depth)
        A.check(summary.indegrees.get(vector, 0) == expected_fibre)
        if norm:
            A.check(summary.successor[summary.successor[vector]] == vector)
    record("QIV", f"p={prime}", states, summary)


# ---------------------------------------------------------------------------
# HUR: Hurwitz move on ordered pairs of transpositions.


def apply_transposition(transposition, value: int) -> int:
    left, right = transposition
    if value == left:
        return right
    if value == right:
        return left
    return value


def conjugate_transposition(moving, conjugator):
    return tuple(sorted((apply_transposition(conjugator, moving[0]),
                         apply_transposition(conjugator, moving[1]))))


def run_hur(size: int) -> None:
    transpositions = tuple(combinations(range(size), 2))
    states = tuple(product(transpositions, repeat=2))

    def successor(state):
        left, right = state
        return right, conjugate_transposition(left, right)

    summary = graph_summary(states, successor)
    count = comb(size, 2)
    expected_cycles = Counter({1: count})
    if size >= 4:
        expected_cycles[2] = 3 * comb(size, 4)
    if size >= 3:
        expected_cycles[3] = 2 * comb(size, 3)
    A.check(Counter(dict(summary.cycle_hist)) == expected_cycles)
    A.check(summary.periodic == count ** 2)
    A.check(summary.indegree_hist == ((1, count ** 2),))
    record("HUR", f"n={size} transpositions={count}", states, summary)


# ---------------------------------------------------------------------------
# HAR: harmonic conjugation on ordered triples of the projective line.


def projective_line(prime: int):
    return tuple((value, 1) for value in range(prime)) + ((1, 0),)


def bracket(left, right, prime: int) -> int:
    return (left[0] * right[1] - left[1] * right[0]) % prime


def harmonic_conjugate(left, right, point, prime: int):
    candidates = []
    for candidate in projective_line(prime):
        if candidate in (left, right):
            continue
        equation = (
            bracket(candidate, left, prime) * bracket(point, right, prime)
            + bracket(point, left, prime) * bracket(candidate, right, prime)
        ) % prime
        if equation == 0:
            candidates.append(candidate)
    A.check(len(candidates) == 1, ("harmonic uniqueness", left, right, point, candidates))
    return candidates[0]


def run_har(prime: int) -> None:
    A.check(prime % 2 == 1)
    line = projective_line(prime)
    states = tuple(
        (left, right, point)
        for left in line for right in line for point in line
        if left != right and point not in (left, right)
    )

    def successor(state):
        left, right, point = state
        return left, right, harmonic_conjugate(left, right, point, prime)

    summary = graph_summary(states, successor)
    total = prime * (prime ** 2 - 1)
    A.check(len(states) == total)
    A.check(summary.cycle_hist == ((2, total // 2),))
    A.check(summary.indegree_hist == ((1, total),))
    record("HAR", f"p={prime}", states, summary)


# ---------------------------------------------------------------------------
# POL: exchange of a point and a line under a fixed projective polarity.


def run_pol(prime: int) -> None:
    projective = projective_points(2, prime)
    states = tuple(product(projective, repeat=2))
    successor = lambda state: (state[1], state[0])
    summary = graph_summary(states, successor)
    count = prime ** 2 + prime + 1
    A.check(len(projective) == count)
    A.check(summary.cycle_hist == ((1, count), (2, (count ** 2 - count) // 2)))
    A.check(summary.indegree_hist == ((1, count ** 2),))
    record("POL", f"p={prime} points={count}", states, summary)


# ---------------------------------------------------------------------------
# VIE: Vieta mutation involution.


def run_vie(prime: int) -> None:
    A.check(prime % 2 == 1)
    states = tuple(product(range(prime), repeat=3))
    successor = lambda state: (state[0], state[1],
                               (state[0] * state[1] - state[2]) % prime)
    summary = graph_summary(states, successor)
    fixed = prime ** 2
    A.check(summary.cycle_hist == ((1, fixed), (2, (prime ** 3 - fixed) // 2)))
    A.check(summary.indegree_hist == ((1, prime ** 3),))
    record("VIE", f"p={prime}", states, summary)


# ---------------------------------------------------------------------------
# SFW: directed-facet walk around a simplex.


def run_sfw(dimension: int) -> None:
    vertices = tuple(range(dimension + 1))
    states = tuple(permutations(vertices, dimension))

    def successor(state):
        missing = next(vertex for vertex in vertices if vertex not in state)
        return state[1:] + (missing,)

    summary = graph_summary(states, successor)
    expected_cycles = ((dimension + 1, factorial(dimension)),)
    A.check(summary.cycle_hist == expected_cycles)
    A.check(summary.indegree_hist == ((1, factorial(dimension + 1)),))
    record("SFW", f"dimension={dimension}", states, summary)


# ---------------------------------------------------------------------------
# UAW: one-letter automaton execution with transition table retained.


def falling(number: int, length: int) -> int:
    answer = 1
    for offset in range(length):
        answer *= number - offset
    return answer


def run_uaw(size: int) -> None:
    functions = tuple(product(range(size), repeat=size))
    states = tuple((function, pointer) for function in functions for pointer in range(size))
    successor = lambda state: (state[0], state[0][state[1]])
    summary = graph_summary(states, successor)
    joint = Counter(summary.tail_cycle.values())
    expected_joint = Counter()
    for tail in range(size):
        for period in range(1, size - tail + 1):
            count = size * falling(size - 1, tail + period - 1) * size ** (size - tail - period)
            expected_joint[(tail, period)] = count
    A.check(joint == expected_joint, ("UAW joint", size, joint, expected_joint))
    expected_indegrees = Counter({
        degree: size * comb(size, degree) * (size - 1) ** (size - degree)
        for degree in range(size + 1)
    })
    expected_indegrees = Counter({key: value for key, value in expected_indegrees.items() if value})
    A.check(Counter(dict(summary.indegree_hist)) == expected_indegrees)
    A.check(summary.max_tail == size - 1)
    for state in states:
        function, target = state
        A.check(summary.indegrees.get(state, 0) == function.count(target))
    record("UAW", f"n={size}", states, summary)


# ---------------------------------------------------------------------------
# RCW: nonlinear rooted-permutation conjugation walker.


def compose(left, right):
    return tuple(left[right[index]] for index in range(len(left)))


def permutation_transposition(size: int, left: int, right: int):
    result = list(range(size))
    result[left], result[right] = result[right], result[left]
    return tuple(result)


def run_rcw(size: int) -> None:
    permutations_n = tuple(permutations(range(size)))
    states = tuple((permutation, pointer)
                   for permutation in permutations_n for pointer in range(size))

    def successor(state):
        permutation, pointer = state
        image = permutation[pointer]
        switch = permutation_transposition(size, pointer, image)
        conjugated = compose(compose(switch, permutation), switch)
        return conjugated, image

    summary = graph_summary(states, successor)
    fixed = factorial(size)
    total = size * factorial(size)
    A.check(summary.cycle_hist == ((1, fixed), (2, (total - fixed) // 2)))
    A.check(summary.indegree_hist == ((1, total),))
    for state in states:
        A.check(summary.successor[summary.successor[state]] == state)
    record("RCW", f"n={size}", states, summary)


# ---------------------------------------------------------------------------
# SYT: Schuetzenberger promotion on two-row rectangular tableaux.


def two_row_tableaux(width: int):
    tableaux = []
    for top in combinations(range(1, 2 * width + 1), width):
        top_set = set(top)
        top_count = 0
        bottom_count = 0
        valid = True
        for value in range(1, 2 * width + 1):
            if value in top_set:
                top_count += 1
            else:
                bottom_count += 1
            if bottom_count > top_count:
                valid = False
                break
        if valid:
            bottom = tuple(value for value in range(1, 2 * width + 1)
                           if value not in top_set)
            tableaux.append((tuple(top), bottom))
    return tuple(tableaux)


def promote_tableau(tableau):
    top, bottom = tableau
    width = len(top)
    grid = {(0, column): top[column] for column in range(width)}
    grid.update({(1, column): bottom[column] for column in range(width)})
    hole = min(grid, key=grid.get)
    A.check(grid[hole] == 1)
    del grid[hole]
    while True:
        row, column = hole
        candidates = []
        if column + 1 < width and (row, column + 1) in grid:
            candidates.append((grid[(row, column + 1)], (row, column + 1)))
        if row == 0 and (1, column) in grid:
            candidates.append((grid[(1, column)], (1, column)))
        if not candidates:
            break
        value, next_hole = min(candidates)
        grid[hole] = value
        del grid[next_hole]
        hole = next_hole
    grid = {position: value - 1 for position, value in grid.items()}
    grid[hole] = 2 * width
    return (
        tuple(grid[(0, column)] for column in range(width)),
        tuple(grid[(1, column)] for column in range(width)),
    )


def run_syt(width: int) -> None:
    states = two_row_tableaux(width)
    summary = graph_summary(states, promote_tableau)
    catalan = comb(2 * width, width) // (width + 1)
    A.check(len(states) == catalan)
    A.check(summary.periodic == catalan)
    A.check(summary.indegree_hist == ((1, catalan),))
    for state in states:
        cursor = state
        for _ in range(2 * width):
            cursor = summary.successor[cursor]
        A.check(cursor == state)
    global_order = 1
    for period, _ in summary.cycle_hist:
        global_order = lcm(global_order, period)
    expected_order = 1 if width == 1 else (2 if width == 2 else 2 * width)
    A.check(global_order == expected_order)
    record("SYT", f"shape=2x{width}", states, summary)


# ---------------------------------------------------------------------------
# CUB: complement-rotate on plane partitions in a box.


def plane_partitions(rows: int, columns: int, height: int):
    states = []
    for values in product(range(height + 1), repeat=rows * columns):
        row_ok = all(values[row * columns + column] >=
                     values[row * columns + column + 1]
                     for row in range(rows) for column in range(columns - 1))
        column_ok = all(values[row * columns + column] >=
                        values[(row + 1) * columns + column]
                        for row in range(rows - 1) for column in range(columns))
        if row_ok and column_ok:
            states.append(values)
    return tuple(states)


def run_cub(rows: int, columns: int, height: int) -> None:
    states = plane_partitions(rows, columns, height)

    def successor(state):
        return tuple(
            height - state[(rows - 1 - row) * columns + (columns - 1 - column)]
            for row in range(rows) for column in range(columns)
        )

    summary = graph_summary(states, successor)
    A.check(summary.periodic == len(states))
    A.check(summary.indegree_hist == ((1, len(states)),))
    for state in states:
        A.check(summary.successor[summary.successor[state]] == state)
    record("CUB", f"box={rows}x{columns}x{height}", states, summary)


# ---------------------------------------------------------------------------
# PDU: polar duality on ordered projective triangles.


def determinant3(columns, prime: int) -> int:
    left, middle, right = columns
    return (
        left[0] * (middle[1] * right[2] - middle[2] * right[1])
        - middle[0] * (left[1] * right[2] - left[2] * right[1])
        + right[0] * (left[1] * middle[2] - left[2] * middle[1])
    ) % prime


def cross3(left, right, prime: int):
    return canonical_projective((
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    ), prime)


def run_pdu(prime: int) -> None:
    points = projective_points(2, prime)
    states = tuple(
        triangle for triangle in permutations(points, 3)
        if determinant3(triangle, prime) != 0
    )

    def successor(state):
        left, middle, right = state
        return (cross3(middle, right, prime),
                cross3(right, left, prime),
                cross3(left, middle, prime))

    summary = graph_summary(states, successor)
    expected_size = (prime ** 2 + prime + 1) * (prime ** 2 + prime) * prime ** 2
    A.check(len(states) == expected_size)
    A.check(summary.periodic == len(states))
    A.check(summary.indegree_hist == ((1, len(states)),))
    for state in states:
        A.check(summary.successor[summary.successor[state]] == state)
    record("PDU", f"p={prime}", states, summary)


# ---------------------------------------------------------------------------
# GFR: cyclic rotation of a group-labelled oriented face with product one.


def inverse_permutation(permutation):
    inverse = [0] * len(permutation)
    for index, value in enumerate(permutation):
        inverse[value] = index
    return tuple(inverse)


def run_gfr(group_name: str, group) -> None:
    identity = tuple(range(len(group[0])))
    states = []
    for left in group:
        for middle in group:
            right = inverse_permutation(compose(left, middle))
            A.check(compose(compose(left, middle), right) == identity)
            states.append((left, middle, right))
    states = tuple(states)
    successor = lambda state: (state[1], state[2], state[0])
    summary = graph_summary(states, successor)
    cube_roots = sum(compose(compose(element, element), element) == identity
                     for element in group)
    total = len(group) ** 2
    A.check(summary.cycle_hist == ((1, cube_roots), (3, (total - cube_roots) // 3)))
    A.check(summary.indegree_hist == ((1, total),))
    record("GFR", f"group={group_name} order={len(group)}", states, summary)


def main() -> None:
    emit("P157_P161_REPLACEMENT_GEOMETRY_MECHANISM_BREADTH_AUDIT")
    emit("external_status=HOLD_EXTERNAL")
    emit("numbering_status=UNASSIGNED")
    emit("enumeration_role=BOUNDED_COUNTEREXAMPLE_PRESSURE_ONLY")

    for rank in (2, 3, 4):
        run_bst(rank)
    for prime in (3, 7):
        run_ort(prime)
    for prime, dimension in ((2, 2), (3, 2), (3, 3)):
        run_cre(prime, dimension)
    for prime in (3, 7):
        run_ref(prime)
    for prime in (5, 13):
        run_qiv(prime)
    for size in (4, 5):
        run_hur(size)
    for prime in (3, 5):
        run_har(prime)
    for prime in (2, 3):
        run_pol(prime)
    for prime in (3, 5):
        run_vie(prime)
    for dimension in (2, 3, 4):
        run_sfw(dimension)
    for size in (2, 3, 4):
        run_uaw(size)
    for size in (3, 4, 5):
        run_rcw(size)
    for width in (2, 3, 4, 5):
        run_syt(width)
    for box in ((2, 2, 1), (2, 2, 2), (2, 3, 2)):
        run_cub(*box)
    for prime in (2, 3):
        run_pdu(prime)

    symmetric_three = tuple(permutations(range(3)))
    cyclic_three = (
        (0, 1, 2),
        (1, 2, 0),
        (2, 0, 1),
    )
    run_gfr("C3", cyclic_three)
    run_gfr("S3", symmetric_three)

    emit("survivors=BST,ORT")
    emit("reserves=NONE")
    emit("killed=14")
    emit("systems=16")
    emit(f"boxes={A.boxes}")
    emit(f"assertions={A.assertions}")
    emit("status=PASS")
    print("\n".join(LINES))


if __name__ == "__main__":
    main()
