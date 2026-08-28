#!/usr/bin/env python3
"""Exact controls for primitive-recurrence avoidance shifts.

The script uses only the Python standard library.  It constructs the actual
zero--one state adjacency matrix, independently constructs the dual Singer
orbit, computes the characteristic polynomial by the Faddeev--LeVerrier
algorithm over the integers, and checks periodic traces.  The field models are
prime fields and F_4 = F_2[u]/(u^2+u+1).
"""

from collections import deque
from itertools import product
from math import gcd


CHECKS = 0


def check(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


class FiniteField:
    """The fields used by the frozen exact controls."""

    def __init__(self, order):
        self.order = order
        if order == 4:
            self.characteristic = 2
            self.kind = "gf4"
        else:
            check(order >= 2, "field order is at least two")
            check(
                all(order % divisor for divisor in range(2, int(order**0.5) + 1)),
                f"{order} is prime",
            )
            self.characteristic = order
            self.kind = "prime"

    @property
    def elements(self):
        return range(self.order)

    def add(self, left, right):
        if self.kind == "prime":
            return (left + right) % self.order
        return left ^ right

    def mul(self, left, right):
        if self.kind == "prime":
            return (left * right) % self.order
        # Binary polynomial multiplication followed by u^2 = u + 1.
        raw = 0
        for bit in range(2):
            if (right >> bit) & 1:
                raw ^= left << bit
        for degree in range(3, 1, -1):
            if (raw >> degree) & 1:
                raw ^= 1 << degree
                raw ^= 1 << (degree - 1)
                raw ^= 1 << (degree - 2)
        return raw


def identity(size):
    return [[int(row == col) for col in range(size)] for row in range(size)]


def matmul_integer(left, right):
    rows = len(left)
    inner = len(right)
    cols = len(right[0])
    return [
        [
            sum(left[row][middle] * right[middle][col] for middle in range(inner))
            for col in range(cols)
        ]
        for row in range(rows)
    ]


def trace(matrix):
    return sum(matrix[index][index] for index in range(len(matrix)))


def characteristic_polynomial(matrix):
    """Return det(lambda I-A), with coefficients in descending order."""
    size = len(matrix)
    auxiliary = identity(size)
    coefficients = [1]
    for degree in range(1, size + 1):
        product_matrix = matmul_integer(matrix, auxiliary)
        numerator = -trace(product_matrix)
        check(numerator % degree == 0, "Faddeev--LeVerrier integrality")
        coefficient = numerator // degree
        coefficients.append(coefficient)
        auxiliary = [
            [
                product_matrix[row][col]
                + coefficient * int(row == col)
                for col in range(size)
            ]
            for row in range(size)
        ]
    return coefficients


def matrix_vector(field, matrix, vector):
    return tuple(
        sum_field(field, [field.mul(entry, value) for entry, value in zip(row, vector)])
        for row in matrix
    )


def sum_field(field, values):
    total = 0
    for value in values:
        total = field.add(total, value)
    return total


def transpose(matrix):
    return [list(column) for column in zip(*matrix)]


def companion(coefficients):
    """Companion for x_(n+r)=sum_j coefficients[j] x_(n+j)."""
    rank = len(coefficients)
    matrix = [[0 for _ in range(rank)] for _ in range(rank)]
    for index in range(rank - 1):
        matrix[index][index + 1] = 1
    matrix[-1] = list(coefficients)
    return matrix


def orbit(field, matrix, start):
    seen = []
    current = start
    while current not in seen:
        seen.append(current)
        current = matrix_vector(field, matrix, current)
    return seen, current


def primitive_coefficients(field, rank):
    length = field.order**rank - 1
    start = (1,) + (0,) * (rank - 1)
    for coefficients in product(field.elements, repeat=rank):
        if coefficients[0] == 0:
            continue
        matrix = companion(coefficients)
        candidate_orbit, return_state = orbit(field, matrix, start)
        if len(candidate_orbit) == length and return_state == start:
            return tuple(coefficients)
    raise AssertionError(f"no primitive companion found for q={field.order}, r={rank}")


def state_adjacency(field, coefficients):
    rank = len(coefficients)
    states = list(product(field.elements, repeat=rank))
    index = {state: position for position, state in enumerate(states)}
    matrix = [[0 for _ in states] for _ in states]
    transition = companion(coefficients)
    for state in states:
        deterministic = list(matrix_vector(field, transition, state))
        for error in field.elements:
            if error == 0:
                continue
            target = list(deterministic)
            target[-1] = field.add(target[-1], error)
            matrix[index[state]][index[tuple(target)]] = 1
    return states, matrix


def expected_charpoly(order, rank):
    length = order**rank - 1
    hyperplane_hits = order ** (rank - 1) - 1
    degree = length + 1
    weight = (order - 1) ** hyperplane_hits
    coefficients = [0] * (degree + 1)
    coefficients[0] = 1
    coefficients[1] = -(order - 1)
    coefficients[-2] = -weight
    coefficients[-1] = (order - 1) * weight
    return coefficients


def fixed_formula(order, rank, period):
    length = order**rank - 1
    hyperplane_hits = order ** (rank - 1) - 1
    base = (order - 1) ** period
    if period % length:
        return base
    return base + length * (order - 1) ** (hyperplane_hits * period // length)


def reachable(matrix, start, reverse=False):
    size = len(matrix)
    reached = {start}
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if reverse:
            neighbors = [row for row in range(size) if matrix[row][vertex]]
        else:
            neighbors = [col for col, value in enumerate(matrix[vertex]) if value]
        for neighbor in neighbors:
            if neighbor not in reached:
                reached.add(neighbor)
                queue.append(neighbor)
    return reached


def graph_period(matrix):
    """Period of a strongly connected digraph via level differences."""
    size = len(matrix)
    distance = [-1] * size
    distance[0] = 0
    queue = deque([0])
    while queue:
        vertex = queue.popleft()
        for neighbor, value in enumerate(matrix[vertex]):
            if value and distance[neighbor] < 0:
                distance[neighbor] = distance[vertex] + 1
                queue.append(neighbor)
    period = 0
    for source, row in enumerate(matrix):
        for target, value in enumerate(row):
            if value:
                period = gcd(period, distance[source] + 1 - distance[target])
    return abs(period)


def run_case(order, rank, expect_mixing=True):
    field = FiniteField(order)
    coefficients = primitive_coefficients(field, rank)
    transition = companion(coefficients)
    length = order**rank - 1
    hyperplane_hits = order ** (rank - 1) - 1

    nonzero_vectors = [
        vector
        for vector in product(field.elements, repeat=rank)
        if any(vector)
    ]
    primal_orbit, primal_return = orbit(
        field, transition, (1,) + (0,) * (rank - 1)
    )
    check(len(primal_orbit) == length, "companion is a Singer cycle")
    check(primal_return == primal_orbit[0], "Singer orbit closes")
    check(set(primal_orbit) == set(nonzero_vectors), "Singer orbit is transitive")

    dual_orbit, dual_return = orbit(
        field, transpose(transition), (1,) + (0,) * (rank - 1)
    )
    check(len(dual_orbit) == length, "transpose has one nonzero orbit")
    check(dual_return == dual_orbit[0], "dual Singer orbit closes")
    check(set(dual_orbit) == set(nonzero_vectors), "dual orbit is transitive")
    observed_hits = sum(vector[-1] == 0 for vector in dual_orbit)
    observed_nonhits = length - observed_hits
    check(observed_hits == hyperplane_hits, "dual hyperplane hit count")
    check(observed_nonhits == order ** (rank - 1) * (order - 1), "dual nonhit count")
    check(observed_nonhits % 2 == 0, "Fourier block has positive cycle weight")

    states, adjacency = state_adjacency(field, coefficients)
    check(len(states) == order**rank, "state-space cardinality")
    row_sums = [sum(row) for row in adjacency]
    col_sums = [sum(adjacency[row][col] for row in range(len(states))) for col in range(len(states))]
    check(set(row_sums) == {order - 1}, "constant outdegree")
    check(set(col_sums) == {order - 1}, "constant indegree")
    check(
        characteristic_polynomial(adjacency) == expected_charpoly(order, rank),
        "full characteristic polynomial",
    )

    if expect_mixing:
        check(len(reachable(adjacency, 0)) == len(states), "strong connectivity forward")
        check(
            len(reachable(adjacency, 0, reverse=True)) == len(states),
            "strong connectivity backward",
        )
        check(graph_period(adjacency) == 1, "aperiodicity")
    else:
        check(len(reachable(adjacency, 0)) < len(states), "binary boundary is reducible")

    matrix_power = identity(len(states))
    observed_fixed = []
    for period in range(1, length + 2):
        matrix_power = matmul_integer(matrix_power, adjacency)
        observed = trace(matrix_power)
        predicted = fixed_formula(order, rank, period)
        check(observed == predicted, f"fixed count at n={period}")
        observed_fixed.append(observed)
    first_anomaly = next(
        period
        for period, value in enumerate(observed_fixed, start=1)
        if value != (order - 1) ** period
    )
    check(first_anomaly == length, "first periodic anomaly is q^r-1")
    recovered_order = observed_fixed[0] + 1
    recovered_rank = 0
    power = 1
    while power < first_anomaly + 1:
        power *= recovered_order
        recovered_rank += 1
    check((recovered_order, recovered_rank) == (order, rank), "parameter recovery")

    anomaly = observed_fixed[length - 1] - (order - 1) ** length
    print(
        f"q={order}, r={rank}, coefficients={coefficients}, states={len(states)}, "
        f"degree={order - 1}, L={length}, H={hyperplane_hits}, "
        f"first_anomaly={first_anomaly}, anomaly_size={anomaly}, "
        f"mixing={'yes' if expect_mixing else 'no (q=2 boundary)'}"
    )


def main():
    run_case(2, 2, expect_mixing=False)
    for order, rank in [(3, 2), (3, 3), (4, 2), (5, 2)]:
        run_case(order, rank)
    print(f"PASS: {CHECKS} exact assertions")


if __name__ == "__main__":
    main()
