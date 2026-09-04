#!/usr/bin/env python3
"""Exact paper-local verifier for P182.

The program uses only the Python standard library.  It enumerates subspaces
over the prime fields in the frozen box, builds the literal map

    (A,B,C) -> (C, A intersect B, A+B),

and independently checks the iterate identities, functional graph, closed
counts, and every target fibre.  Finite enumeration is falsification pressure,
not the proof of the all-prime-power theorem and not owner evidence.
"""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
from itertools import combinations, product


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def check(self, condition: bool, message: str) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(message)


AUDIT = Audit()
DIGEST = sha256()
TRANSITIONS = 0


def gaussian(n: int, k: int, q: int) -> int:
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator *= q ** (n - i) - 1
        denominator *= q ** (k - i) - 1
    AUDIT.check(numerator % denominator == 0, "nonintegral Gaussian coefficient")
    return numerator // denominator


def galois_number(n: int, q: int) -> int:
    return sum(gaussian(n, k, q) for k in range(n + 1))


def encode(vector: tuple[int, ...], q: int) -> int:
    value = 0
    scale = 1
    for coordinate in vector:
        value += coordinate * scale
        scale *= q
    return value


def decode(value: int, q: int, dimension: int) -> tuple[int, ...]:
    coordinates = []
    for _ in range(dimension):
        coordinates.append(value % q)
        value //= q
    return tuple(coordinates)


def rref(
    vectors: list[tuple[int, ...]] | tuple[tuple[int, ...], ...],
    q: int,
    dimension: int,
) -> tuple[tuple[int, ...], ...]:
    rows = [list(vector) for vector in vectors if any(vector)]
    pivot_row = 0
    for column in range(dimension):
        pivot = next(
            (row for row in range(pivot_row, len(rows)) if rows[row][column] % q),
            None,
        )
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        inverse = pow(rows[pivot_row][column] % q, -1, q)
        rows[pivot_row] = [(entry * inverse) % q for entry in rows[pivot_row]]
        for row in range(len(rows)):
            if row == pivot_row:
                continue
            scale = rows[row][column] % q
            if scale:
                rows[row] = [
                    (entry - scale * pivot_entry) % q
                    for entry, pivot_entry in zip(rows[row], rows[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == len(rows):
            break
    rows = [row for row in rows if any(row)]
    rows.sort(key=lambda row: next(i for i, entry in enumerate(row) if entry))
    return tuple(tuple(entry % q for entry in row) for row in rows)


def span(
    basis: tuple[tuple[int, ...], ...], q: int, dimension: int
) -> frozenset[int]:
    elements = set()
    for coefficients in product(range(q), repeat=len(basis)):
        vector = tuple(
            sum(coefficient * row[column] for coefficient, row in zip(coefficients, basis))
            % q
            for column in range(dimension)
        )
        elements.add(encode(vector, q))
    AUDIT.check(len(elements) == q ** len(basis), "basis span has wrong size")
    return frozenset(elements)


def subspaces(q: int, dimension: int) -> list[tuple[tuple[tuple[int, ...], ...], frozenset[int]]]:
    answer = []
    for rank in range(dimension + 1):
        for pivots in combinations(range(dimension), rank):
            free = [
                (row, column)
                for row, pivot in enumerate(pivots)
                for column in range(pivot + 1, dimension)
                if column not in pivots
            ]
            for values in product(range(q), repeat=len(free)):
                rows = [[0] * dimension for _ in range(rank)]
                for row, pivot in enumerate(pivots):
                    rows[row][pivot] = 1
                for (row, column), value in zip(free, values):
                    rows[row][column] = value
                basis = tuple(tuple(row) for row in rows)
                AUDIT.check(rref(basis, q, dimension) == basis, "noncanonical RREF")
                answer.append((basis, span(basis, q, dimension)))
    expected = galois_number(dimension, q)
    AUDIT.check(len(answer) == expected, "wrong subspace count")
    AUDIT.check(len({basis for basis, _ in answer}) == expected, "duplicate basis")
    AUDIT.check(len({elements for _, elements in answer}) == expected, "duplicate subspace")
    return answer


def lattice_tables(
    spaces: list[tuple[tuple[tuple[int, ...], ...], frozenset[int]]],
    q: int,
    dimension: int,
) -> tuple[list[list[int]], list[list[int]]]:
    index = {basis: i for i, (basis, _elements) in enumerate(spaces)}
    meet = [[0] * len(spaces) for _ in spaces]
    join = [[0] * len(spaces) for _ in spaces]
    for i, (left_basis, left) in enumerate(spaces):
        for j, (right_basis, right) in enumerate(spaces):
            meet_basis = rref(
                [decode(value, q, dimension) for value in left & right], q, dimension
            )
            join_basis = rref(list(left_basis + right_basis), q, dimension)
            meet[i][j] = index[meet_basis]
            join[i][j] = index[join_basis]
            AUDIT.check(spaces[meet[i][j]][1] == left & right, "meet mismatch")
            AUDIT.check(left <= spaces[join[i][j]][1], "left escaped join")
            AUDIT.check(right <= spaces[join[i][j]][1], "right escaped join")
            AUDIT.check(
                len(spaces[join[i][j]][0])
                == len(left_basis) + len(right_basis) - len(spaces[meet[i][j]][0]),
                "modular dimension identity failed",
            )
    return meet, join


def graph_stats(successor: list[int]) -> tuple[int, Counter[int], Counter[int], Counter[int]]:
    incoming = Counter(successor)
    depth: list[int | None] = [None] * len(successor)
    cycles: Counter[int] = Counter()
    for start in range(len(successor)):
        if depth[start] is not None:
            continue
        path = []
        position = {}
        current = start
        while depth[current] is None and current not in position:
            position[current] = len(path)
            path.append(current)
            current = successor[current]
        if depth[current] is None:
            split = position[current]
            period = len(path) - split
            cycles[period] += 1
            for vertex in path[split:]:
                depth[vertex] = 0
            for vertex in reversed(path[:split]):
                depth[vertex] = depth[successor[vertex]] + 1  # type: ignore[operator]
        else:
            for vertex in reversed(path):
                depth[vertex] = depth[successor[vertex]] + 1  # type: ignore[operator]
    AUDIT.check(all(value is not None for value in depth), "unassigned depth")
    for source, target in enumerate(successor):
        AUDIT.check(0 <= target < len(successor), "successor outside carrier")
        if depth[source] == 0:
            AUDIT.check(depth[target] == 0, "cycle escaped recurrent set")
        else:
            AUDIT.check(depth[target] == depth[source] - 1, "depth did not decrease")
    fibres = Counter(incoming.get(target, 0) for target in range(len(successor)))
    return len(incoming), cycles, Counter(depth), fibres


def compact(counter: Counter[int]) -> str:
    return ",".join(f"{key}:{counter[key]}" for key in sorted(counter))


def complement_pairs(rank: int, q: int) -> int:
    return sum(gaussian(rank, a, q) * q ** (a * (rank - a)) for a in range(rank + 1))


def disjoint_pairs(rank: int, q: int) -> int:
    return sum(
        gaussian(rank, a, q)
        * gaussian(rank - a, b, q)
        * q ** (a * b)
        for a in range(rank + 1)
        for b in range(rank - a + 1)
    )


def check_box(q: int, dimension: int) -> str:
    global TRANSITIONS
    spaces = subspaces(q, dimension)
    lattice_size = len(spaces)
    meet, join = lattice_tables(spaces, q, dimension)
    carrier = lattice_size**3

    def pack(a: int, b: int, c: int) -> int:
        return (a * lattice_size + b) * lattice_size + c

    def unpack(value: int) -> tuple[int, int, int]:
        c = value % lattice_size
        value //= lattice_size
        b = value % lattice_size
        return value // lattice_size, b, c

    successor = [0] * carrier
    predicted_depths: Counter[int] = Counter()
    fixed = 0
    recurrent = 0
    for source in range(carrier):
        a, b, c = unpack(source)
        target = pack(c, meet[a][b], join[a][b])
        successor[source] = target
        DIGEST.update(f"{q}|{dimension}|{source}|{target}\n".encode())
        TRANSITIONS += 1
        is_recurrent = meet[a][b] == b and meet[b][c] == b
        is_fixed = is_recurrent and a == c
        if is_recurrent:
            predicted_depths[0] += 1
            recurrent += 1
            fixed += int(is_fixed)
        elif meet[meet[a][b]][c] == meet[a][b]:
            predicted_depths[1] += 1
        else:
            predicted_depths[2] += 1

    for source in range(carrier):
        a, b, c = unpack(source)
        square = successor[successor[source]]
        expected = pack(join[a][b], meet[c][meet[a][b]], join[c][meet[a][b]])
        AUDIT.check(square == expected, "square formula failed")
        AUDIT.check(successor[successor[square]] == square, "T^4 != T^2")

    incoming = Counter(successor)
    fibre_values = [complement_pairs(k, q) for k in range(dimension + 1)]
    AUDIT.check(
        all(fibre_values[k] < fibre_values[k + 1] for k in range(dimension)),
        "fibre values did not increase",
    )
    for target in range(carrier):
        _c, middle, top = unpack(target)
        if meet[middle][top] == middle:
            quotient_rank = len(spaces[top][0]) - len(spaces[middle][0])
            expected = fibre_values[quotient_rank]
        else:
            expected = 0
        AUDIT.check(incoming.get(target, 0) == expected, "target fibre mismatch")

    galois = galois_number(dimension, q)
    intervals = sum(
        gaussian(dimension, b, q) * galois_number(dimension - b, q)
        for b in range(dimension + 1)
    )
    recurrent_formula = sum(
        gaussian(dimension, b, q) * galois_number(dimension - b, q) ** 2
        for b in range(dimension + 1)
    )
    depth_at_most_one = sum(
        gaussian(dimension, m, q)
        * disjoint_pairs(dimension - m, q)
        * galois_number(dimension - m, q)
        for m in range(dimension + 1)
    )
    closed_depths = Counter(
        {
            0: recurrent_formula,
            1: depth_at_most_one - recurrent_formula,
            2: carrier - depth_at_most_one,
        }
    )
    closed_depths += Counter()  # discard any zero entries canonically
    image, cycles, depths, fibres = graph_stats(successor)
    AUDIT.check(lattice_size == galois, "Galois number mismatch")
    AUDIT.check(fixed == intervals, "fixed-point formula mismatch")
    AUDIT.check(recurrent == recurrent_formula, "recurrent formula mismatch")
    AUDIT.check(image == lattice_size * intervals, "image formula mismatch")
    AUDIT.check(
        cycles == Counter({1: intervals, 2: (recurrent_formula - intervals) // 2}),
        "cycle formula mismatch",
    )
    AUDIT.check(depths == closed_depths, "depth formula mismatch")
    AUDIT.check(sum(incoming.values()) == carrier, "fibre mass mismatch")
    if dimension == 0:
        AUDIT.check(max(depths) == 0, "zero-dimensional boundary failed")
    else:
        AUDIT.check(depths[2] > 0, "height two was not sharp")

    return (
        f"q={q} d={dimension} L={lattice_size} states={carrier} image={image} "
        f"cycles={compact(cycles)} depths={compact(depths)} fibres={compact(fibres)}"
    )


def main() -> None:
    boxes = [
        *((2, d) for d in range(5)),
        *((3, d) for d in range(4)),
        *((5, d) for d in range(3)),
        *((7, d) for d in range(3)),
    ]
    print("P182_CYCLIC_SUBSPACE_LATTICE_COMPARATOR_EXACT_V1")
    print("map=(A,B,C)->(C,A_intersect_B,A_plus_B)")
    for q, dimension in boxes:
        print(check_box(q, dimension))
    print(f"boxes={len(boxes)}")
    print(f"transitions={TRANSITIONS}")
    print(f"exact_assertions={AUDIT.assertions}")
    print(f"transition_digest={DIGEST.hexdigest()}")
    print("status=PASS")
    print("external_status=HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
