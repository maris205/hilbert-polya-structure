#!/usr/bin/env python3
"""Exact pilot for the P182--P186 algebra breadth lane.

This is a standard-library-only, deterministic verifier.  It independently
enumerates three literal systems selected from a fifteen-system breadth
ledger.  Enumeration is falsification pressure, not an all-parameter proof
and not evidence of novelty, ownership, or release clearance.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
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
BOXES = 0
TRANSITIONS_BY_TAG: Counter[str] = Counter()


def digest_edge(tag: str, box: tuple[int, ...], source: int, target: int) -> None:
    global TRANSITIONS
    TRANSITIONS += 1
    TRANSITIONS_BY_TAG[tag] += 1
    DIGEST.update(f"{tag}|{box}|{source}|{target}\n".encode())


def compact_counter(counter: Counter[int]) -> str:
    return ",".join(f"{key}:{counter[key]}" for key in sorted(counter))


def gaussian(n: int, k: int, q: int) -> int:
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)
    numerator = 1
    denominator = 1
    for j in range(k):
        numerator *= q ** (n - j) - 1
        denominator *= q ** (k - j) - 1
    AUDIT.check(numerator % denominator == 0, "nonintegral Gaussian coefficient")
    return numerator // denominator


def galois_number(n: int, q: int) -> int:
    return sum(gaussian(n, k, q) for k in range(n + 1))


def encode_vector(vector: tuple[int, ...], q: int) -> int:
    value = 0
    scale = 1
    for coordinate in vector:
        value += coordinate * scale
        scale *= q
    return value


def decode_vector(value: int, q: int, dimension: int) -> tuple[int, ...]:
    out = []
    for _ in range(dimension):
        out.append(value % q)
        value //= q
    return tuple(out)


def rref_basis(
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
    rows.sort(key=lambda row: next(index for index, entry in enumerate(row) if entry))
    return tuple(tuple(entry % q for entry in row) for row in rows)


def span_elements(
    basis: tuple[tuple[int, ...], ...], q: int, dimension: int
) -> frozenset[int]:
    elements = set()
    for coefficients in product(range(q), repeat=len(basis)):
        vector = tuple(
            sum(coefficient * row[column] for coefficient, row in zip(coefficients, basis))
            % q
            for column in range(dimension)
        )
        elements.add(encode_vector(vector, q))
    AUDIT.check(len(elements) == q ** len(basis), "basis did not span expected size")
    return frozenset(elements)


@dataclass(frozen=True)
class Subspace:
    basis: tuple[tuple[int, ...], ...]
    elements: frozenset[int]

    @property
    def dimension(self) -> int:
        return len(self.basis)


def enumerate_subspaces(q: int, dimension: int) -> list[Subspace]:
    spaces: list[Subspace] = []
    for rank in range(dimension + 1):
        for pivots in combinations(range(dimension), rank):
            free_positions = [
                (row, column)
                for row, pivot in enumerate(pivots)
                for column in range(pivot + 1, dimension)
                if column not in pivots
            ]
            for values in product(range(q), repeat=len(free_positions)):
                rows = [[0] * dimension for _ in range(rank)]
                for row, pivot in enumerate(pivots):
                    rows[row][pivot] = 1
                for (row, column), value in zip(free_positions, values):
                    rows[row][column] = value
                basis = tuple(tuple(row) for row in rows)
                AUDIT.check(
                    rref_basis(basis, q, dimension) == basis,
                    "enumerated basis was not canonical RREF",
                )
                spaces.append(Subspace(basis, span_elements(basis, q, dimension)))
    expected = galois_number(dimension, q)
    AUDIT.check(len(spaces) == expected, "wrong number of subspaces")
    AUDIT.check(len({space.basis for space in spaces}) == expected, "duplicate RREF basis")
    AUDIT.check(
        len({space.elements for space in spaces}) == expected,
        "duplicate extensional subspace",
    )
    return spaces


def graph_stats(successor: list[int]) -> dict[str, object]:
    size = len(successor)
    incoming = Counter(successor)
    depth: list[int | None] = [None] * size
    period: list[int | None] = [None] * size
    cycles: Counter[int] = Counter()
    for start in range(size):
        if depth[start] is not None:
            continue
        path: list[int] = []
        position: dict[int, int] = {}
        current = start
        while depth[current] is None and current not in position:
            position[current] = len(path)
            path.append(current)
            current = successor[current]
        if depth[current] is None:
            split = position[current]
            cycle_length = len(path) - split
            cycles[cycle_length] += 1
            for vertex in path[split:]:
                depth[vertex] = 0
                period[vertex] = cycle_length
            for vertex in reversed(path[:split]):
                depth[vertex] = depth[successor[vertex]] + 1  # type: ignore[operator]
                period[vertex] = cycle_length
        else:
            for vertex in reversed(path):
                depth[vertex] = depth[successor[vertex]] + 1  # type: ignore[operator]
                period[vertex] = period[successor[vertex]]
    AUDIT.check(all(value is not None for value in depth), "unassigned graph depth")
    AUDIT.check(all(value is not None for value in period), "unassigned graph period")
    for source, target in enumerate(successor):
        AUDIT.check(0 <= target < size, "successor outside carrier")
        if depth[source] == 0:
            AUDIT.check(depth[target] == 0, "recurrent state left recurrent core")
        else:
            AUDIT.check(depth[target] == depth[source] - 1, "graph depth did not drop")
    return {
        "image": len(incoming),
        "cycles": cycles,
        "depths": Counter(depth),
        "height": max(depth),
        "fibres": Counter(incoming.get(target, 0) for target in range(size)),
    }


def precompute_lattice(
    spaces: list[Subspace], q: int, dimension: int
) -> tuple[list[list[int]], list[list[int]]]:
    index = {space.basis: i for i, space in enumerate(spaces)}
    meet = [[0] * len(spaces) for _ in spaces]
    join = [[0] * len(spaces) for _ in spaces]
    for i, left in enumerate(spaces):
        for j, right in enumerate(spaces):
            intersection_vectors = [
                decode_vector(value, q, dimension)
                for value in left.elements & right.elements
            ]
            meet_basis = rref_basis(intersection_vectors, q, dimension)
            join_basis = rref_basis(list(left.basis + right.basis), q, dimension)
            meet[i][j] = index[meet_basis]
            join[i][j] = index[join_basis]
            AUDIT.check(
                spaces[meet[i][j]].elements == left.elements & right.elements,
                "meet table mismatch",
            )
            AUDIT.check(
                left.elements <= spaces[join[i][j]].elements
                and right.elements <= spaces[join[i][j]].elements,
                "join table containment mismatch",
            )
            AUDIT.check(
                spaces[join[i][j]].dimension
                == left.dimension + right.dimension - spaces[meet[i][j]].dimension,
                "modular dimension identity mismatch",
            )
    return meet, join


def complementary_pair_count(rank: int, q: int) -> int:
    return sum(gaussian(rank, a, q) * q ** (a * (rank - a)) for a in range(rank + 1))


def check_cyclic_lattice_comparator() -> list[str]:
    """A01/CLC: (A,B,C) -> (C,A meet B,A join B)."""
    global BOXES
    rows = []
    for q, dimensions in ((2, range(1, 5)), (3, range(1, 4))):
        for dimension in dimensions:
            BOXES += 1
            spaces = enumerate_subspaces(q, dimension)
            count = len(spaces)
            meet, join = precompute_lattice(spaces, q, dimension)
            size = count**3

            def state_index(a: int, b: int, c: int) -> int:
                return (a * count + b) * count + c

            def state_tuple(value: int) -> tuple[int, int, int]:
                c = value % count
                value //= count
                b = value % count
                return value // count, b, c

            successor = [0] * size
            depth_formula = Counter()
            recurrent_formula = 0
            fixed_formula = 0
            for source in range(size):
                a, b, c = state_tuple(source)
                target = state_index(c, meet[a][b], join[a][b])
                successor[source] = target
                digest_edge("CLC", (q, dimension), source, target)
                recurrent = meet[a][b] == b and meet[b][c] == b
                fixed = recurrent and a == c
                if recurrent:
                    depth = 0
                    recurrent_formula += 1
                    fixed_formula += int(fixed)
                elif meet[meet[a][b]][c] == meet[a][b]:
                    depth = 1
                else:
                    depth = 2
                depth_formula[depth] += 1

            for source in range(size):
                a, b, c = state_tuple(source)
                second = successor[successor[source]]
                expected_second = state_index(
                    join[a][b], meet[c][meet[a][b]], join[c][meet[a][b]]
                )
                AUDIT.check(second == expected_second, "CLC square identity failed")
                AUDIT.check(
                    successor[successor[second]] == second,
                    "CLC fourth iterate did not equal square",
                )

            incoming = Counter(successor)
            fibre_sizes = [complementary_pair_count(rank, q) for rank in range(dimension + 1)]
            AUDIT.check(
                len(set(fibre_sizes)) == len(fibre_sizes),
                "CLC complementary-pair fibre sizes unexpectedly collided",
            )
            for target in range(size):
                _c, middle, top = state_tuple(target)
                if meet[middle][top] == middle:
                    rank = spaces[top].dimension - spaces[middle].dimension
                    expected = fibre_sizes[rank]
                else:
                    expected = 0
                AUDIT.check(incoming.get(target, 0) == expected, "CLC target fibre mismatch")

            galois = galois_number(dimension, q)
            comparable = sum(
                gaussian(dimension, rank, q) * galois_number(dimension - rank, q)
                for rank in range(dimension + 1)
            )
            recurrent_count = sum(
                gaussian(dimension, rank, q)
                * galois_number(dimension - rank, q) ** 2
                for rank in range(dimension + 1)
            )
            AUDIT.check(count == galois, "CLC Galois-number mismatch")
            AUDIT.check(fixed_formula == comparable, "CLC fixed-count formula mismatch")
            AUDIT.check(recurrent_formula == recurrent_count, "CLC recurrent-count mismatch")
            stats = graph_stats(successor)
            AUDIT.check(stats["height"] == 2, "CLC sharp height failed")
            AUDIT.check(stats["depths"] == depth_formula, "CLC depth census mismatch")
            AUDIT.check(stats["image"] == count * comparable, "CLC image count mismatch")
            AUDIT.check(
                stats["cycles"]
                == Counter({1: comparable, 2: (recurrent_count - comparable) // 2}),
                "CLC recurrent cycle census mismatch",
            )
            rows.append(
                f"q={q} d={dimension} L={count} N={size} image={stats['image']} "
                f"cycles={compact_counter(stats['cycles'])} "
                f"depths={compact_counter(stats['depths'])} "
                f"fibres={compact_counter(stats['fibres'])}"
            )
    return rows


def matrix_product(
    left: tuple[int, int, int, int],
    right: tuple[int, int, int, int],
    q: int,
) -> tuple[int, int, int, int]:
    a, b, c, d = left
    e, f, g, h = right
    return (
        (a * e + b * g) % q,
        (a * f + b * h) % q,
        (c * e + d * g) % q,
        (c * f + d * h) % q,
    )


def vector_subtract(
    left: tuple[int, ...], right: tuple[int, ...], q: int
) -> tuple[int, ...]:
    return tuple((a - b) % q for a, b in zip(left, right))


def central_extension_count(central_dimension: int, projected_rank: int, q: int) -> int:
    """Number of U <= Z + P which project onto a fixed P along Z."""
    return sum(
        gaussian(central_dimension, kernel_rank, q)
        * q ** (projected_rank * (central_dimension - kernel_rank))
        for kernel_rank in range(central_dimension + 1)
    )


def sl2_bracket(
    left: tuple[int, ...], right: tuple[int, ...], q: int, central_dimension: int
) -> tuple[int, ...]:
    """Bracket on the central thickening F_q^z + sl_2(F_q)."""
    h, e, f = left[central_dimension:]
    hh, ee, ff = right[central_dimension:]
    return (0,) * central_dimension + (
        (e * ff - f * ee) % q,
        (2 * (h * ee - e * hh)) % q,
        (2 * (f * hh - h * ff)) % q,
    )


def check_lie_derived_subspaces() -> list[str]:
    """A02/LDS: U -> [U,U] on F_q^z + sl_2(F_q), q odd."""
    global BOXES
    rows = []
    for q, central_dimensions in ((3, (0, 1, 2)), (5, (0, 1))):
        for central_dimension in central_dimensions:
            ambient_dimension = central_dimension + 3
            BOXES += 1
            spaces = enumerate_subspaces(q, ambient_dimension)
            index = {space.basis: i for i, space in enumerate(spaces)}
            zero = index[tuple()]
            sl2_basis = tuple(
                (0,) * central_dimension
                + tuple(int(column == row) for column in range(3))
                for row in range(3)
            )
            sl2 = index[sl2_basis]
            successor = [0] * len(spaces)
            projection_sources: defaultdict[tuple[tuple[int, ...], ...], list[int]] = defaultdict(list)
            plane_to_line: dict[tuple[tuple[int, ...], ...], tuple[tuple[int, ...], ...]] = {}
            for source, space in enumerate(spaces):
                commutators = []
                for i, left in enumerate(space.basis):
                    for right in space.basis[i + 1 :]:
                        commutators.append(
                            sl2_bracket(left, right, q, central_dimension)
                        )
                target_basis = rref_basis(commutators, q, ambient_dimension)
                target = index[target_basis]
                successor[source] = target
                digest_edge("LDS", (q, central_dimension), source, target)

                projection_basis = rref_basis(
                    [row[central_dimension:] for row in space.basis], q, 3
                )
                projection_sources[projection_basis].append(source)
                projected_rank = len(projection_basis)
                expected_rank = 0 if projected_rank <= 1 else (1 if projected_rank == 2 else 3)
                AUDIT.check(len(target_basis) == expected_rank, "LDS image-rank trichotomy failed")
                if projected_rank == 2:
                    projected_target = rref_basis(
                        [row[central_dimension:] for row in target_basis], q, 3
                    )
                    if projection_basis in plane_to_line:
                        AUDIT.check(
                            plane_to_line[projection_basis] == projected_target,
                            "LDS plane had two bracket lines",
                        )
                    plane_to_line[projection_basis] = projected_target

            for projection, sources in projection_sources.items():
                AUDIT.check(
                    len(sources)
                    == central_extension_count(
                        central_dimension, len(projection), q
                    ),
                    "LDS central-extension source count mismatch",
                )
            lines = gaussian(3, 1, q)
            AUDIT.check(len(plane_to_line) == lines, "LDS did not see every sl2 plane")
            AUDIT.check(
                len(set(plane_to_line.values())) == lines,
                "LDS bracket polarity was not bijective",
            )
            for line in plane_to_line.values():
                AUDIT.check(line, "LDS plane bracket vanished")

            embedded_line_indices = {
                index[
                    tuple(
                        (0,) * central_dimension + row
                        for row in line
                    )
                ]
                for line in plane_to_line.values()
            }
            incoming = Counter(successor)
            zero_fibre = central_extension_count(central_dimension, 0, q) + lines * central_extension_count(central_dimension, 1, q)
            sl2_fibre = central_extension_count(central_dimension, 3, q)
            line_fibre = central_extension_count(central_dimension, 2, q)
            AUDIT.check(incoming[zero] == zero_fibre, "LDS zero fibre mismatch")
            AUDIT.check(incoming[sl2] == sl2_fibre, "LDS sl2 fibre mismatch")
            for target in range(len(spaces)):
                expected = (
                    zero_fibre
                    if target == zero
                    else sl2_fibre
                    if target == sl2
                    else line_fibre
                    if target in embedded_line_indices
                    else 0
                )
                AUDIT.check(incoming.get(target, 0) == expected, "LDS full fibre atlas mismatch")
            for source in range(len(spaces)):
                second = successor[successor[source]]
                AUDIT.check(second in (zero, sl2), "LDS square missed recurrent core")
                AUDIT.check(successor[second] == second, "LDS cube did not equal square")

            stats = graph_stats(successor)
            expected_depths = Counter(
                {
                    0: 2,
                    2: lines * line_fibre,
                    1: len(spaces) - 2 - lines * line_fibre,
                }
            )
            AUDIT.check(stats["image"] == lines + 2, "LDS image size mismatch")
            AUDIT.check(stats["cycles"] == Counter({1: 2}), "LDS recurrent census mismatch")
            AUDIT.check(stats["depths"] == expected_depths, "LDS depth census mismatch")
            AUDIT.check(stats["height"] == 2, "LDS sharp height failed")
            rows.append(
                f"q={q} z={central_dimension} N={len(spaces)} image={stats['image']} "
                f"cycles={compact_counter(stats['cycles'])} "
                f"depths={compact_counter(stats['depths'])} "
                f"fibres={compact_counter(stats['fibres'])}"
            )
    return rows


def transpose(matrix: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    a, b, c, d = matrix
    return a, c, b, d


def check_transpose_commutator() -> list[str]:
    """A03/TCC: A -> A A^T - A^T A on M_2(F_q), q odd."""
    global BOXES
    rows = []
    for q in (3, 5, 7):
        BOXES += 1
        size = q**4
        successor = [0] * size
        for source in range(size):
            matrix = decode_vector(source, q, 4)
            transposed = transpose(matrix)  # type: ignore[arg-type]
            target_matrix = vector_subtract(
                matrix_product(matrix, transposed, q),  # type: ignore[arg-type]
                matrix_product(transposed, matrix, q),  # type: ignore[arg-type]
                q,
            )
            target = encode_vector(target_matrix, q)
            successor[source] = target
            digest_edge("TCC", (q,), source, target)
            a, b, c, d = matrix
            u = (b - c) % q
            v = (b + c) % q
            w = (d - a) % q
            AUDIT.check(
                target_matrix == (u * v % q, u * w % q, u * w % q, -u * v % q),
                "TCC rank-one factorization failed",
            )
            AUDIT.check(
                target_matrix[1] == target_matrix[2]
                and (target_matrix[0] + target_matrix[3]) % q == 0,
                "TCC image escaped trace-zero symmetric plane",
            )

        incoming = Counter(successor)
        zero_fibre = q**3 + q * (q - 1)
        image_targets = {
            encode_vector((x, y, y, -x % q), q)
            for x in range(q)
            for y in range(q)
        }
        AUDIT.check(len(image_targets) == q**2, "TCC image parametrization collided")
        for target in range(size):
            expected = (
                zero_fibre
                if target == 0
                else q * (q - 1)
                if target in image_targets
                else 0
            )
            AUDIT.check(incoming.get(target, 0) == expected, "TCC fibre formula mismatch")
        for source in range(size):
            AUDIT.check(successor[successor[source]] == 0, "TCC square-zero identity failed")

        stats = graph_stats(successor)
        expected_depths = Counter({0: 1, 1: zero_fibre - 1, 2: size - zero_fibre})
        AUDIT.check(stats["image"] == q**2, "TCC image size mismatch")
        AUDIT.check(stats["cycles"] == Counter({1: 1}), "TCC recurrent census mismatch")
        AUDIT.check(stats["depths"] == expected_depths, "TCC depth census mismatch")
        AUDIT.check(stats["height"] == 2, "TCC sharp height failed")
        rows.append(
            f"q={q} N={size} image={stats['image']} "
            f"cycles={compact_counter(stats['cycles'])} "
            f"depths={compact_counter(stats['depths'])} "
            f"fibres={compact_counter(stats['fibres'])}"
        )
    return rows


def main() -> None:
    print("P182_P186_ALGEBRA_LANE_EXACT_PILOT_V1")
    print("SYSTEM=A01_CYCLIC_LATTICE_COMPARATOR")
    for row in check_cyclic_lattice_comparator():
        print(row)
    print("SYSTEM=A02_LIE_DERIVED_SUBSPACES")
    for row in check_lie_derived_subspaces():
        print(row)
    print("SYSTEM=A03_TRANSPOSE_COMMUTATOR_COLLAPSE")
    for row in check_transpose_commutator():
        print(row)
    print("RAW_CANDIDATES=15")
    print("CONSERVATIVE_DISTINCT_LITERAL_SYSTEMS=15")
    print("PILOTED_CANDIDATES=3")
    print(f"BOXES={BOXES}")
    print(f"TRANSITIONS={TRANSITIONS}")
    print(f"TRANSITIONS_CLC={TRANSITIONS_BY_TAG['CLC']}")
    print(f"TRANSITIONS_LDS={TRANSITIONS_BY_TAG['LDS']}")
    print(f"TRANSITIONS_TCC={TRANSITIONS_BY_TAG['TCC']}")
    print(f"ASSERTIONS={AUDIT.assertions}")
    print(f"TRANSITION_DIGEST={DIGEST.hexdigest()}")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
