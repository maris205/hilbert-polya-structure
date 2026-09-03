#!/usr/bin/env python3
"""Independent exact controls for Boolean-Gram dynamics.

The carrier is the set of n by n zero-one matrices and multiplication is
over the Boolean semiring.  This file uses only the Python standard library
and imports no scouting or paper module.  Exhaustive checks through n=4 are
finite falsification controls; the uniform arguments are in main.tex.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache


ASSERTIONS = 0


def check(condition: bool, message: str = "check failed") -> None:
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


def boolean_product(left: int, right: int, n: int) -> int:
    left_rows = rows(left, n)
    right_rows = rows(right, n)
    answer = []
    for left_row in left_rows:
        row = 0
        for middle in range(n):
            if (left_row >> middle) & 1:
                row |= right_rows[middle]
        answer.append(row)
    return pack(tuple(answer), n)


def boolean_square(state: int, n: int) -> int:
    return boolean_product(state, state, n)


def boolean_power(state: int, exponent: int, n: int) -> int:
    identity = pack(tuple(1 << i for i in range(n)), n)
    answer = identity
    base = state
    while exponent:
        if exponent & 1:
            answer = boolean_product(answer, base, n)
        exponent >>= 1
        if exponent:
            base = boolean_square(base, n)
    return answer


def iterate(state: int, n: int, time: int) -> int:
    for _ in range(time):
        state = boolean_gram(state, n)
    return state


def is_compatible_target(state: int, n: int) -> bool:
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
    return is_compatible_target(state, n) and boolean_square(state, n) == state


def depth(state: int, n: int) -> int:
    current = state
    for step in range(n + 3):
        following = boolean_gram(current, n)
        if following == current:
            return step
        current = following
    raise AssertionError(f"depth guard failed at n={n}, state={state}")


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
        best = max(best, max(distances.values(), default=0))
    return best


def ceil_log2(value: int) -> int:
    return 0 if value <= 1 else (value - 1).bit_length()


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
    if not is_compatible_target(state, n):
        return 0
    atoms = requirements(state, n)
    columns = allowed_column_supports(state, n)
    total = 0
    for selected in range(1 << len(atoms)):
        missed = tuple(
            atoms[j] for j in range(len(atoms)) if (selected >> j) & 1
        )
        choices = sum(
            all(column & atom != atom for atom in missed)
            for column in columns
        )
        sign = -1 if selected.bit_count() & 1 else 1
        total += sign * choices**n
    return total


def cover_exists(state: int, n: int) -> bool:
    """Whether at most n nonempty allowed cliques cover all requirements."""
    if not is_compatible_target(state, n):
        return False
    atoms = requirements(state, n)
    if not atoms:
        return True
    full = (1 << len(atoms)) - 1
    masks = []
    for column in allowed_column_supports(state, n):
        if column == 0:
            continue
        mask = 0
        for j, atom in enumerate(atoms):
            if column & atom == atom:
                mask |= 1 << j
        masks.append(mask)
    reachable = {0}
    for _ in range(n):
        reachable |= {covered | mask for covered in tuple(reachable) for mask in masks}
    return full in reachable


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
    k = min(k, n - k)
    answer = 1
    for j in range(1, k + 1):
        answer = answer * (n - k + j) // j
    return answer


def fixed_count_formula(n: int) -> int:
    bells = bell_numbers_through(n + 1)
    partial = sum(binomial(n, k) * bells[k] for k in range(n + 1))
    check(partial == bells[n + 1], f"Bell transform failed at n={n}")
    return partial


def path_incidence(n: int) -> int:
    path_rows = []
    for vertex in range(n):
        support = 0
        if vertex > 0:
            support |= 1 << (vertex - 1)
        if vertex + 1 < n:
            support |= 1 << vertex
        path_rows.append(support)
    return pack(tuple(path_rows), n)


def verify_size(n: int) -> dict[str, object]:
    universe = 1 << (n * n)
    image: set[int] = set()
    fibres: Counter[int] = Counter()
    depth_histogram: Counter[int] = Counter()
    fixed = 0

    for state in range(universe):
        first = boolean_gram(state, n)
        check(is_compatible_target(first, n), f"bad Gram target n={n}")
        check(boolean_gram(first, n) == boolean_square(first, n),
              f"Gram/square mismatch n={n}")
        for time in range(1, 5):
            expected = boolean_power(first, 1 << (time - 1), n)
            check(iterate(state, n, time) == expected,
                  f"orbit identity failed n={n}, t={time}")
        image.add(first)
        fibres[first] += 1

        actual_depth = depth(state, n)
        depth_histogram[actual_depth] += 1
        diameter = component_diameter(first, n)
        predicted = (0 if is_partial_equivalence(state, n)
                     else 1 + ceil_log2(diameter))
        check(actual_depth == predicted, f"clock mismatch n={n}")
        endpoint = iterate(state, n, actual_depth)
        check(is_partial_equivalence(endpoint, n), f"bad endpoint n={n}")

    for target in range(universe):
        if is_partial_equivalence(target, n):
            fixed += 1
            check(boolean_gram(target, n) == target,
                  f"fixed classification failed n={n}")
        if is_compatible_target(target, n):
            formula = fibre_formula(target, n)
            check(formula == fibres[target], f"fibre mismatch n={n}")
            check((formula > 0) == cover_exists(target, n),
                  f"image criterion mismatch n={n}")
        else:
            check(fibres[target] == 0 and fibre_formula(target, n) == 0,
                  f"invalid target has a source n={n}")

    check(fixed == fixed_count_formula(n), f"fixed census mismatch n={n}")
    check(sum(fibres.values()) == universe, f"fibre mass mismatch n={n}")
    expected_max = 0 if n == 1 else 1 + ceil_log2(n - 1)
    check(max(depth_histogram) == expected_max, f"height mismatch n={n}")
    if n >= 2:
        check(depth(path_incidence(n), n) == expected_max,
              f"path witness failed n={n}")

    return {
        "n": n,
        "states": universe,
        "image": len(image),
        "fixed": fixed,
        "max_depth": max(depth_histogram),
        "depth_histogram": dict(sorted(depth_histogram.items())),
        "compatible_targets": sum(
            is_compatible_target(target, n) for target in range(universe)
        ),
        "max_fibre": max(fibres.values()),
    }


def boundary_controls() -> None:
    # n=1, zero, D<=1, a lone loop, and an edge with missing endpoint loops.
    check(boolean_gram(0, 1) == 0 and depth(0, 1) == 0, "n=1 zero")
    check(boolean_gram(1, 1) == 1 and depth(1, 1) == 0, "n=1 one")
    for n in range(1, 9):
        zero = 0
        check(fibre_formula(zero, n) == 1, f"empty-column boundary n={n}")
        lone_loop = 1
        check(is_compatible_target(lone_loop, n), f"lone loop n={n}")
        check(fibre_formula(lone_loop, n) == (2**n - 1),
              f"isolated loop fibre n={n}")
        if n >= 2:
            invalid_edge = (1 << 1) | (1 << n)
            check(not is_compatible_target(invalid_edge, n),
                  f"unlooped edge accepted n={n}")
            check(fibre_formula(invalid_edge, n) == 0,
                  f"unlooped edge fibre n={n}")
    for n in range(2, 65):
        witness = path_incidence(n)
        check(depth(witness, n) == 1 + ceil_log2(n - 1),
              f"large path clock n={n}")
    # The first useful compatibility/image distinction: the fully looped
    # K_{2,3} has six edge atoms and only edges/singletons as allowed cliques,
    # so five labelled columns cannot cover it.
    n = 5
    bipartite_rows = []
    for vertex in range(n):
        row = 1 << vertex
        opposite = range(2, 5) if vertex < 2 else range(0, 2)
        for neighbor in opposite:
            row |= 1 << neighbor
        bipartite_rows.append(row)
    looped_k23 = pack(tuple(bipartite_rows), n)
    check(is_compatible_target(looped_k23, n), "looped K23 compatibility")
    check(not cover_exists(looped_k23, n), "looped K23 cover obstruction")
    check(fibre_formula(looped_k23, n) == 0, "looped K23 fibre obstruction")
    for n in range(0, 16):
        fixed_count_formula(n)


def main() -> None:
    expected_image = {1: 2, 2: 5, 3: 18, 4: 113}
    expected_fixed = {1: 2, 2: 5, 3: 15, 4: 52}
    print("BOOLEAN-GRAM FINITE DYNAMICS / ROUND-0 AUTHOR CONTROL")
    print("map: Gamma_n(A)=A A^T over the Boolean semiring")
    print("exhaustive carrier and codomain audit: 1 <= n <= 4")
    for n in range(1, 5):
        result = verify_size(n)
        check(result["image"] == expected_image[n], f"image census n={n}")
        check(result["fixed"] == expected_fixed[n], f"fixed census n={n}")
        print(result)
    boundary_controls()
    print("path sharpness replayed through n=64")
    print("boundary controls: n=1; zero; D<=1; lone loops; invalid edges; empty columns; looped K2,3")
    print(f"assertions={ASSERTIONS}")
    print("AUTHOR_ROUND0_PASS")
    print("EXTERNAL_STATUS=HOLD_EXTERNAL_OWNER_THIN")


if __name__ == "__main__":
    main()
