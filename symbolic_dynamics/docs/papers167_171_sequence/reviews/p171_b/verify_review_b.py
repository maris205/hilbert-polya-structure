#!/usr/bin/env python3
"""Reviewer-owned exact control for P171 Hostile Review B.

This program does not import the author verifier, scouting code, or Review A.
Matrices are ordered tuples of column-support frozensets, while relations are
frozensets of ordered pairs.  Temporal predictions are built from independent
shortest-path balls.  Fibres are reconstructed three ways: literal source
histograms, ordered coverage dynamic programming, and atomwise
inclusion--exclusion.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from hashlib import sha256
from itertools import combinations, product
from math import comb, factorial


class ReviewLedger:
    def __init__(self) -> None:
        self.assertions = 0
        self.sections: Counter[str] = Counter()
        self.fingerprint = sha256()
        self.rows = 0

    def equal(self, section: str, got, expected, label: str) -> None:
        self.assertions += 1
        self.sections[section] += 1
        if got != expected:
            raise AssertionError(f"{label}: got {got!r}, expected {expected!r}")

    def true(self, section: str, condition: bool, label: str) -> None:
        self.equal(section, bool(condition), True, label)

    def record(self, *items) -> None:
        line = "|".join(str(item) for item in items) + "\n"
        self.fingerprint.update(line.encode("ascii"))
        self.rows += 1


R = ReviewLedger()


def powerset(n: int) -> tuple[frozenset[int], ...]:
    return tuple(
        frozenset(i for i in range(n) if mask & (1 << i))
        for mask in range(1 << n)
    )


def matrix_from_columns(columns: tuple[frozenset[int], ...]):
    return frozenset((row, column) for column, support in enumerate(columns) for row in support)


def rows_of(relation: frozenset[tuple[int, int]], n: int):
    return tuple(frozenset(j for j in range(n) if (i, j) in relation) for i in range(n))


def literal_gram(relation: frozenset[tuple[int, int]], n: int):
    row_sets = rows_of(relation, n)
    return frozenset(
        (i, j) for i in range(n) for j in range(n) if row_sets[i] & row_sets[j]
    )


def gram_from_columns(columns: tuple[frozenset[int], ...]):
    return frozenset(
        (left, right)
        for support in columns
        for left in support
        for right in support
    )


def iterate(relation: frozenset[tuple[int, int]], n: int, time: int):
    for _ in range(time):
        relation = literal_gram(relation, n)
    return relation


def compatible(relation: frozenset[tuple[int, int]], n: int) -> bool:
    for i in range(n):
        for j in range(n):
            if ((i, j) in relation) != ((j, i) in relation):
                return False
            if (i, j) in relation and ((i, i) not in relation or (j, j) not in relation):
                return False
    return True


def partial_equivalence_form(relation: frozenset[tuple[int, int]], n: int) -> bool:
    if not compatible(relation, n):
        return False
    for i in range(n):
        for j in range(n):
            if (i, j) not in relation:
                continue
            for k in range(n):
                if (j, k) in relation and (i, k) not in relation:
                    return False
    return True


def active_distances(graph: frozenset[tuple[int, int]], n: int, source: int):
    distance = {source: 0}
    frontier = [source]
    while frontier:
        vertex = frontier.pop(0)
        for neighbor in range(n):
            if neighbor not in distance and (vertex, neighbor) in graph:
                distance[neighbor] = distance[vertex] + 1
                frontier.append(neighbor)
    return distance


def distance_ball(graph: frozenset[tuple[int, int]], n: int, radius: int):
    active = [i for i in range(n) if (i, i) in graph]
    result = set()
    for source in active:
        for target, distance in active_distances(graph, n, source).items():
            if distance <= radius:
                result.add((source, target))
    return frozenset(result)


def completion(graph: frozenset[tuple[int, int]], n: int):
    return distance_ball(graph, n, max(1, n - 1))


def diameter(graph: frozenset[tuple[int, int]], n: int) -> int:
    active = [i for i in range(n) if (i, i) in graph]
    answer = 0
    for source in active:
        values = active_distances(graph, n, source).values()
        answer = max(answer, max(values, default=0))
    return answer


def ceil_log2(value: int) -> int:
    return 0 if value <= 1 else (value - 1).bit_length()


def direct_depth(relation: frozenset[tuple[int, int]], n: int):
    for time in range(n + 4):
        following = literal_gram(relation, n)
        if following == relation:
            return time
        relation = following
    raise AssertionError("depth guard")


def relation_from_code(code: int, n: int):
    return frozenset(
        (i, j) for i in range(n) for j in range(n) if code & (1 << (i * n + j))
    )


def target_atoms(target: frozenset[tuple[int, int]], n: int):
    atoms: list[frozenset[int]] = []
    for i in range(n):
        if (i, i) in target:
            atoms.append(frozenset((i,)))
    for i, j in combinations(range(n), 2):
        if (i, j) in target:
            atoms.append(frozenset((i, j)))
    return tuple(atoms)


def allowed_supports(target: frozenset[tuple[int, int]], n: int):
    return tuple(
        support
        for support in powerset(n)
        if all((i, j) in target for i in support for j in support)
    )


def coverage_data(target: frozenset[tuple[int, int]], n: int):
    atoms = target_atoms(target, n)
    supports = allowed_supports(target, n)
    coverage = tuple(
        sum(1 << index for index, atom in enumerate(atoms) if atom <= support)
        for support in supports
    )
    return atoms, supports, coverage


def ordered_coverage_count(target: frozenset[tuple[int, int]], n: int) -> int:
    atoms, _supports, coverage = coverage_data(target, n)
    full = (1 << len(atoms)) - 1
    ways = {0: 1}
    for _ in range(n):
        following: defaultdict[int, int] = defaultdict(int)
        for old, multiplicity in ways.items():
            for mask in coverage:
                following[old | mask] += multiplicity
        ways = dict(following)
    return ways.get(full, 0)


def inclusion_exclusion_count(target: frozenset[tuple[int, int]], n: int) -> int:
    atoms, _supports, coverage = coverage_data(target, n)
    answer = 0
    for missed in range(1 << len(atoms)):
        choices = sum((mask & missed) == 0 for mask in coverage)
        answer += (-1 if missed.bit_count() & 1 else 1) * choices**n
    return answer


def nondominated_cover_masks(target: frozenset[tuple[int, int]], n: int):
    _atoms, _supports, coverage = coverage_data(target, n)
    values = sorted(set(coverage) - {0}, key=lambda x: (x.bit_count(), x), reverse=True)
    return tuple(value for value in values if not any(value != other and value & ~other == 0 for other in values))


def minimum_cover(target: frozenset[tuple[int, int]], n: int):
    atoms = target_atoms(target, n)
    full = (1 << len(atoms)) - 1
    if full == 0:
        return 0
    masks = nondominated_cover_masks(target, n)
    reachable = {0}
    for number in range(1, len(atoms) + 1):
        reachable |= {old | mask for old in tuple(reachable) for mask in masks}
        if full in reachable:
            return number
    return None


def bell_by_stirling(limit: int):
    triangle = [[1]]
    bells = [1]
    for n in range(1, limit + 1):
        previous = triangle[-1]
        row = [0] * (n + 1)
        for k in range(1, n + 1):
            row[k] = (previous[k - 1] if k - 1 < len(previous) else 0) + (
                k * previous[k] if k < len(previous) else 0
            )
        triangle.append(row)
        bells.append(sum(row))
    return bells


def verify_carriers(maximum_n: int = 4):
    summaries = []
    bells = bell_by_stirling(22)
    for n in range(1, maximum_n + 1):
        subsets = powerset(n)
        fibres: Counter[frozenset[tuple[int, int]]] = Counter()
        depths: Counter[int] = Counter()
        fixed = 0
        periodic = Counter()
        sources = 0
        for columns in product(subsets, repeat=n):
            sources += 1
            source = matrix_from_columns(columns)
            first = gram_from_columns(columns)
            R.equal("temporal", literal_gram(source, n), first, "row/column Gram")
            R.true("temporal", compatible(first, n), "Gram compatibility")
            fibres[first] += 1
            for time in range(1, 6):
                direct = iterate(source, n, time)
                prediction = distance_ball(first, n, 1 << (time - 1))
                R.equal("temporal", direct, prediction, f"distance clock n={n},t={time}")
                if direct == source:
                    periodic[time] += 1
            endpoint = completion(first, n)
            R.true("temporal", partial_equivalence_form(endpoint, n), "endpoint form")
            actual_depth = direct_depth(source, n)
            predicted_depth = (
                0
                if partial_equivalence_form(source, n)
                else 1 + ceil_log2(diameter(first, n))
            )
            R.equal("clock", actual_depth, predicted_depth, f"depth n={n}")
            R.equal("clock", iterate(source, n, actual_depth), endpoint, "endpoint at depth")
            depths[actual_depth] += 1
            if partial_equivalence_form(source, n):
                fixed += 1
                R.equal("census", literal_gram(source, n), source, "partial equivalence fixed")
            R.record("edge", n, tuple(sorted(tuple(sorted(c)) for c in columns)), tuple(sorted(first)))

        compatible_targets = 0
        for code in range(1 << (n * n)):
            target = relation_from_code(code, n)
            literal = fibres[target]
            if not compatible(target, n):
                R.equal("fibre", literal, 0, "invalid target fibre")
                continue
            compatible_targets += 1
            dynamic = ordered_coverage_count(target, n)
            alternating = inclusion_exclusion_count(target, n)
            cover = minimum_cover(target, n)
            R.equal("fibre", dynamic, literal, f"coverage/literal n={n}")
            R.equal("fibre", alternating, literal, f"IE/literal n={n}")
            R.equal("cover", dynamic > 0, cover is not None and cover <= n, "ordered-cover criterion")
            R.record("target", n, code, literal, cover)

        expected_height = 0 if n == 1 else 1 + ceil_log2(n - 1)
        R.equal("clock", max(depths), expected_height, f"height n={n}")
        R.equal("census", fixed, bells[n + 1], f"Bell fixed census n={n}")
        for time in range(1, 6):
            R.equal("census", periodic[time], fixed, f"fixed iterate n={n},t={time}")
        R.equal("fibre", sum(fibres.values()), sources, "fibre mass")
        summaries.append((n, sources, len(fibres), fixed, dict(sorted(depths.items())), max(fibres.values()), compatible_targets))

    for n in range(0, 21):
        transformed = sum(comb(n, k) * bells[k] for k in range(n + 1))
        R.equal("census", transformed, bells[n + 1], f"Bell transform n={n}")
        R.record("bell", n, bells[n], transformed)
    return summaries


def path_source(n: int):
    columns = []
    for edge in range(n - 1):
        columns.append(frozenset((edge, edge + 1)))
    columns.append(frozenset())
    return tuple(columns)


def target_from_graph(n: int, edges):
    relation = {(i, i) for i in range(n)}
    for i, j in edges:
        relation.add((i, j))
        relation.add((j, i))
    return frozenset(relation)


def verify_boundaries():
    for n in range(2, 65):
        columns = path_source(n)
        source = matrix_from_columns(columns)
        graph = gram_from_columns(columns)
        expected_graph = target_from_graph(n, ((i, i + 1) for i in range(n - 1)))
        R.equal("sharpness", graph, expected_graph, f"path incidence graph n={n}")
        R.true("sharpness", not partial_equivalence_form(source, n), f"path source nonfixed n={n}")
        R.equal("sharpness", diameter(graph, n), n - 1, f"path diameter n={n}")
        R.equal("sharpness", 1 + ceil_log2(diameter(graph, n)), 1 + ceil_log2(n - 1), "height witness")
        if n <= 18:
            R.equal("sharpness", direct_depth(source, n), 1 + ceil_log2(n - 1), "literal path depth")

    # Zero graph, a nonfixed source with D=0, and one with D=1.
    for n in range(1, 13):
        zero = frozenset()
        R.equal("boundary", direct_depth(zero, n), 0, "zero fixed")
        lone_column = (frozenset((0,)),) + (frozenset(),) * (n - 1)
        lone_source = matrix_from_columns(lone_column)
        lone_graph = gram_from_columns(lone_column)
        if n > 1:
            R.equal("boundary", diameter(lone_graph, n), 0, "D=0")
        expected_depth = 0 if partial_equivalence_form(lone_source, n) else 1
        R.equal("boundary", direct_depth(lone_source, n), expected_depth, "D=0 convention")
        R.equal("boundary", ordered_coverage_count(frozenset(), n), 1, "zero target")
        R.equal(
            "boundary",
            ordered_coverage_count(frozenset(((0, 0),)), n),
            2**n - 1,
            "isolated loop fibre",
        )

    R.equal("boundary", ordered_coverage_count(target_from_graph(3, ()), 3), factorial(3), "I3 fibre")
    path3 = target_from_graph(3, ((0, 1), (1, 2)))
    complete3 = target_from_graph(3, combinations(range(3), 2))
    R.equal("boundary", ordered_coverage_count(path3, 3), 30, "looped P3 fibre")
    R.equal("boundary", ordered_coverage_count(complete3, 3), 175, "J3 fibre")

    invalid = frozenset(((0, 1), (1, 0)))
    R.true("boundary", not compatible(invalid, 2), "unlooped edge invalid")

    k23_edges = tuple((left, right) for left in range(2) for right in range(2, 5))
    k23 = target_from_graph(5, k23_edges)
    R.true("k23", compatible(k23, 5), "K23 compatible")
    R.equal("k23", minimum_cover(k23, 5), 6, "K23 exact cover")
    R.equal("k23", ordered_coverage_count(k23, 5), 0, "K23 dynamic fibre")
    R.equal("k23", inclusion_exclusion_count(k23, 5), 0, "K23 IE fibre")

    # Exhaust every fully looped graph on five vertices under the <=5 cover
    # criterion.  This is beyond the author's n<=4 complete codomain box.
    edges = tuple(combinations(range(5), 2))
    nonimages = []
    cover_histogram: Counter[int] = Counter()
    for edge_code in range(1 << len(edges)):
        chosen = tuple(edge for bit, edge in enumerate(edges) if edge_code & (1 << bit))
        target = target_from_graph(5, chosen)
        cover = minimum_cover(target, 5)
        R.true("n5_cover", cover is not None, "full-loop graph cover exists")
        cover_histogram[cover] += 1
        if cover > 5:
            nonimages.append(edge_code)
        R.equal("n5_cover", cover <= 5, ordered_coverage_count(target, 5) > 0, "n=5 cover/fibre existence")
        R.record("n5", edge_code, cover)
    R.equal("n5_cover", len(nonimages), 10, "ten labelled K23 obstructions")
    for code in nonimages:
        chosen = tuple(edge for bit, edge in enumerate(edges) if code & (1 << bit))
        degrees = sorted(sum(vertex in edge for edge in chosen) for vertex in range(5))
        triangles = sum(
            all(tuple(sorted(edge)) in chosen for edge in combinations(triple, 2))
            for triple in combinations(range(5), 3)
        )
        R.equal("n5_cover", degrees, [2, 2, 2, 3, 3], "K23 degree sequence")
        R.equal("n5_cover", triangles, 0, "K23 triangle-free")
    R.true("n5_cover", any(target_from_graph(5, tuple(edge for bit, edge in enumerate(edges) if code & (1 << bit))) == k23 for code in nonimages), "chosen K23 appears among n=5 obstructions")
    return len(nonimages), dict(sorted(cover_histogram.items()))


def main() -> None:
    summaries = verify_carriers()
    nonimages, cover_histogram = verify_boundaries()
    print("P171_HOSTILE_REVIEW_B_INDEPENDENT_CONTROL_V1")
    for summary in summaries:
        print(
            "n=%d sources=%d image=%d fixed=%d depth=%s max_fibre=%d compatible=%d"
            % summary
        )
    print(f"full_loop_n5_nonimages={nonimages}")
    print(f"full_loop_n5_cover_histogram={cover_histogram}")
    print("looped_K23_minimum_cover=6")
    for section in sorted(R.sections):
        print(f"{section}_assertions={R.sections[section]}")
    print(f"fingerprint_rows={R.rows}")
    print(f"payload_sha256={R.fingerprint.hexdigest()}")
    print(f"assertions={R.assertions}")
    print("decision=REVIEW_B_INDEPENDENT_CONTROL_PASS")
    print("external_status=HOLD_EXTERNAL_OWNER_THIN")


if __name__ == "__main__":
    main()
