#!/usr/bin/env python3
"""Exact checks for A -> A A^T over the Boolean semiring.

The carrier is the set of n x n Boolean matrices.  The first image is the
intersection graph of the row supports (with loops on nonempty rows), and
later iterates are repeated graph squaring.  The script also verifies the
every-target clique-cover inclusion--exclusion formula.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache


ASSERTIONS = 0


def check(condition: bool, message: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def rows(state: int, n: int) -> tuple[int, ...]:
    mask = (1 << n) - 1
    return tuple((state >> (n * i)) & mask for i in range(n))


def pack(row_tuple: tuple[int, ...], n: int) -> int:
    return sum(row << (n * i) for i, row in enumerate(row_tuple))


def boolean_gram(state: int, n: int) -> int:
    support = rows(state, n)
    answer = []
    for left in support:
        row = 0
        for j, right in enumerate(support):
            if left & right:
                row |= 1 << j
        answer.append(row)
    return pack(tuple(answer), n)


def boolean_square(state: int, n: int) -> int:
    relation = rows(state, n)
    answer = []
    for i in range(n):
        row = 0
        for middle in range(n):
            if (relation[i] >> middle) & 1:
                row |= relation[middle]
        answer.append(row)
    return pack(tuple(answer), n)


def is_loop_compatible_graph(state: int, n: int) -> bool:
    relation = rows(state, n)
    for i in range(n):
        for j in range(n):
            if ((relation[i] >> j) & 1) != ((relation[j] >> i) & 1):
                return False
            if (relation[i] >> j) & 1:
                if not ((relation[i] >> i) & 1 and (relation[j] >> j) & 1):
                    return False
    return True


def is_partial_equivalence(state: int, n: int) -> bool:
    return is_loop_compatible_graph(state, n) and boolean_square(state, n) == state


def closure(state: int, n: int) -> int:
    current = state
    while True:
        following = boolean_square(current, n)
        if following == current:
            return current
        current = following


def depth(state: int, n: int) -> int:
    current = state
    for step in range(n + 3):
        following = boolean_gram(current, n)
        if following == current:
            return step
        current = following
    raise AssertionError(f"depth guard failed for n={n}, state={state}")


def component_diameter(state: int, n: int) -> int:
    relation = rows(state, n)
    active = [i for i in range(n) if (relation[i] >> i) & 1]
    best = 0
    for source in active:
        distances = {source: 0}
        frontier = [source]
        while frontier:
            vertex = frontier.pop(0)
            for target in active:
                if ((relation[vertex] >> target) & 1) and target not in distances:
                    distances[target] = distances[vertex] + 1
                    frontier.append(target)
        if distances:
            best = max(best, max(distances.values()))
    return best


def ceil_log2(value: int) -> int:
    if value <= 1:
        return 0
    return (value - 1).bit_length()


def requirements(state: int, n: int) -> tuple[int, ...]:
    relation = rows(state, n)
    atoms = []
    for i in range(n):
        if (relation[i] >> i) & 1:
            atoms.append(1 << i)
        for j in range(i + 1, n):
            if (relation[i] >> j) & 1:
                atoms.append((1 << i) | (1 << j))
    return tuple(atoms)


@lru_cache(maxsize=None)
def allowed_column_supports(state: int, n: int) -> tuple[int, ...]:
    relation = rows(state, n)
    allowed = []
    for subset in range(1 << n):
        vertices = [i for i in range(n) if (subset >> i) & 1]
        if all((relation[i] >> j) & 1 for i in vertices for j in vertices):
            allowed.append(subset)
    return tuple(allowed)


def fibre_formula(state: int, n: int) -> int:
    if not is_loop_compatible_graph(state, n):
        return 0
    atoms = requirements(state, n)
    allowed = allowed_column_supports(state, n)
    total = 0
    for selected in range(1 << len(atoms)):
        forbidden = tuple(atoms[j] for j in range(len(atoms)) if (selected >> j) & 1)
        choices = sum(all(column & atom != atom for atom in forbidden) for column in allowed)
        total += (-1 if selected.bit_count() & 1 else 1) * choices**n
    return total


def bell_numbers_through(n: int) -> list[int]:
    triangle = [[1]]
    bells = [1]
    for r in range(1, n + 1):
        previous = triangle[-1]
        line = [previous[-1]]
        for k in range(1, r + 1):
            line.append(line[-1] + previous[k - 1])
        triangle.append(line)
        bells.append(line[0])
    return bells


def binomial(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)
    answer = 1
    for j in range(1, k + 1):
        answer = answer * (n - k + j) // j
    return answer


def expected_fixed_count(n: int) -> int:
    bells = bell_numbers_through(n)
    return sum(binomial(n, k) * bells[k] for k in range(n + 1))


def verify_size(n: int) -> dict[str, object]:
    universe = 1 << (n * n)
    image: set[int] = set()
    fibres: Counter[int] = Counter()
    depth_histogram: Counter[int] = Counter()
    fixed = 0

    for state in range(universe):
        first = boolean_gram(state, n)
        check(is_loop_compatible_graph(first, n), f"invalid Gram graph n={n}, state={state}")
        check(boolean_gram(first, n) == boolean_square(first, n), f"Gram/square mismatch n={n}")
        image.add(first)
        fibres[first] += 1

        d = depth(state, n)
        depth_histogram[d] += 1
        final = state
        for _ in range(d):
            final = boolean_gram(final, n)
        check(is_partial_equivalence(final, n), f"non-equivalence endpoint n={n}, state={state}")
        check(boolean_gram(final, n) == final, f"endpoint not fixed n={n}, state={state}")

        graph = first
        diameter = component_diameter(graph, n)
        predicted = 0 if is_partial_equivalence(state, n) else 1 + ceil_log2(diameter)
        check(d == predicted, f"diameter clock mismatch n={n}, state={state}")

    for state in range(universe):
        if is_partial_equivalence(state, n):
            fixed += 1
            check(boolean_gram(state, n) == state, f"partial equivalence not fixed n={n}")
        if state not in image:
            check(fibres[state] == 0, f"mass outside image n={n}")

    check(fixed == expected_fixed_count(n), f"fixed census mismatch n={n}")
    check(sum(fibres.values()) == universe, f"fibre mass mismatch n={n}")

    formula_checks = 0
    for target in range(universe):
        if is_loop_compatible_graph(target, n):
            check(fibre_formula(target, n) == fibres[target], f"fibre formula mismatch n={n}, target={target}")
            formula_checks += 1

    # Incidence rows of the path 0--1--...--(n-1), using columns 0,...,n-2.
    if n >= 2:
        path_incidence_rows = []
        for vertex in range(n):
            support = 0
            if vertex > 0:
                support |= 1 << (vertex - 1)
            if vertex + 1 < n:
                support |= 1 << vertex
            path_incidence_rows.append(support)
        witness = pack(tuple(path_incidence_rows), n)
        expected_max = 1 + ceil_log2(n - 1)
        check(depth(witness, n) == expected_max, f"path witness not sharp n={n}")
    else:
        expected_max = 0

    check(max(depth_histogram) == expected_max, f"maximum depth mismatch n={n}")
    return {
        "n": n,
        "states": universe,
        "image_graphs": len(image),
        "fixed_partial_equivalences": fixed,
        "max_depth": max(depth_histogram),
        "depth_histogram": dict(sorted(depth_histogram.items())),
        "fibre_formula_targets": formula_checks,
        "fibre_min_on_image": min(fibres.values()),
        "fibre_max": max(fibres.values()),
    }


def main() -> None:
    expected_images = {1: 2, 2: 5, 3: 18, 4: 113}
    expected_fixed = {1: 2, 2: 5, 3: 15, 4: 52}
    print("BOOLEAN GRAM / ROW-INTERSECTION DYNAMICS")
    print("map: G(A)=A A^T over the Boolean semiring")
    print("scope: exhaustive over every n x n Boolean matrix for 1 <= n <= 4")
    for n in range(1, 5):
        result = verify_size(n)
        check(result["image_graphs"] == expected_images[n], f"image count mismatch n={n}")
        check(result["fixed_partial_equivalences"] == expected_fixed[n], f"fixed count mismatch n={n}")
        print(result)
    print(f"assertions={ASSERTIONS}")
    print("THEOREM_CHECKS_PASS")


if __name__ == "__main__":
    main()
