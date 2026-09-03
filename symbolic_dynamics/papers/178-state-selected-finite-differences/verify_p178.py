#!/usr/bin/env python3
"""Paper-local author-side exact controls for state-selected finite differences.

The literal carrier is represented by tuples of values, not by the integer
encoding used in the discovery scout.  Three prime boxes are exhausted
target by target.  A separate matrix certificate checks the cyclic
difference filtration and the anchored-lift ranks at larger primes.  Only
the Python standard library is imported; no project or scouting code is
loaded.  Finite checks are falsification evidence, not a proof or an owner
certificate.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from hashlib import sha256
from itertools import product
from math import comb


ASSERTIONS = 0
EDGE_DIGEST = sha256()
LITERAL_EDGES = 0


def require(condition: bool, message: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def difference(function: tuple[int, ...], step: int, prime: int) -> tuple[int, ...]:
    return tuple(
        (function[(point + step) % prime] - function[point]) % prime
        for point in range(prime)
    )


def update(function: tuple[int, ...], prime: int) -> tuple[int, ...]:
    return difference(function, function[0], prime)


def unit_power(function: tuple[int, ...], time: int, prime: int) -> tuple[int, ...]:
    state = function
    for _ in range(time):
        state = difference(state, 1, prime)
    return state


def binomial_function(degree: int, prime: int) -> tuple[int, ...]:
    return tuple(comb(point, degree) % prime for point in range(prime))


def compact(counter: Counter[int]) -> str:
    return ",".join(f"{key}:{counter[key]}" for key in sorted(counter))


def zero_block_inventory(prime: int) -> Counter[int]:
    blocks = Counter(
        {
            size: (prime - 1) ** 2 * prime ** (prime - size - 1)
            for size in range(1, prime)
        }
    )
    blocks[prime] = prime - 1
    return blocks


def exhaustive_literal_box(prime: int) -> None:
    global LITERAL_EDGES
    states = tuple(product(range(prime), repeat=prime))
    state_set = set(states)
    zero = (0,) * prime
    size = len(states)

    arrows: dict[tuple[int, ...], tuple[int, ...]] = {}
    for source in states:
        target = update(source, prime)
        require(target in state_set, f"closure failed at p={prime}")
        arrows[source] = target
        LITERAL_EDGES += 1
        EDGE_DIGEST.update(f"p={prime}|{source}|{target}\n".encode("ascii"))

    # Build the nonlinear powers literally and the fixed unit-difference
    # filtration independently.
    endpoint = {source: source for source in states}
    image_sizes: list[int] = []
    zero_fibres: list[int] = []
    filtration: list[set[tuple[int, ...]]] = []
    all_fibres: list[Counter[tuple[int, ...]]] = []
    for time in range(prime + 1):
        fibres = Counter(endpoint.values())
        ideal_layer = {unit_power(source, time, prime) for source in states}
        all_fibres.append(fibres)
        filtration.append(ideal_layer)
        image_sizes.append(len(fibres))
        zero_fibres.append(fibres.get(zero, 0))

        require(set(fibres) == ideal_layer, f"image layer failed p={prime} t={time}")
        require(
            len(ideal_layer) == prime ** (prime - time),
            f"filtration size failed p={prime} t={time}",
        )
        for target in states:
            observed = fibres.get(target, 0)
            if time == 0:
                expected = 1
            elif time < prime and target == zero:
                expected = size - (prime ** (prime - time) - 1) * (prime - 1) ** time
            elif time < prime and target in ideal_layer:
                expected = (prime - 1) ** time
            elif time >= prime and target == zero:
                expected = size
            else:
                expected = 0
            require(
                observed == expected,
                f"target fibre failed p={prime} t={time} target={target}",
            )
        require(sum(fibres.values()) == size, f"fibre mass failed p={prime} t={time}")
        if time < prime:
            endpoint = {source: arrows[target] for source, target in endpoint.items()}

    # Recover the nonzero direction word from every trajectory.  The key
    # (terminal target, direction word) must occur exactly once.
    word_lifts: list[Counter[tuple[tuple[int, ...], tuple[int, ...]]]] = [
        Counter() for _ in range(prime)
    ]
    for source in states:
        current = source
        word: list[int] = []
        for time in range(1, prime):
            word.append(current[0])
            current = arrows[current]
            if current != zero:
                require(
                    all(letter != 0 for letter in word),
                    f"nonzero endpoint has a zero direction p={prime} t={time}",
                )
                word_lifts[time][(current, tuple(word))] += 1

    for time in range(1, prime):
        expected_keys = 0
        for target in filtration[time]:
            if target == zero:
                continue
            for word in product(range(1, prime), repeat=time):
                expected_keys += 1
                require(
                    word_lifts[time].get((target, word), 0) == 1,
                    f"anchored word lift failed p={prime} t={time}",
                )
        require(
            len(word_lifts[time]) == expected_keys,
            f"extra anchored word lift p={prime} t={time}",
        )

    depths = Counter()
    for source in states:
        current = source
        depth = 0
        while current != zero and depth <= prime:
            current = arrows[current]
            depth += 1
        require(current == zero and depth <= prime, f"clock failed p={prime}")
        depths[depth] += 1
    predicted_depths = Counter({0: 1})
    for depth in range(1, prime + 1):
        predicted_depths[depth] = (prime - 1) ** (depth - 1) * (
            prime ** (prime - depth) + prime - 2
        )
    require(depths == predicted_depths, f"depth census failed p={prime}")

    indegrees = all_fibres[1]
    kernel = size - (prime ** (prime - 1) - 1) * (prime - 1)
    require(indegrees[zero] == kernel, f"root indegree failed p={prime}")
    for target in states:
        expected = (
            kernel
            if target == zero
            else prime - 1
            if target in filtration[1]
            else 0
        )
        require(indegrees.get(target, 0) == expected, f"branching failed p={prime}")

    witness = tuple(
        sum(comb(point, degree) for degree in range(prime)) % prime
        for point in range(prime)
    )
    current = witness
    directions = []
    for _ in range(prime):
        directions.append(current[0])
        current = arrows[current]
    require(directions == [1] * prime, f"sharp witness directions p={prime}")
    require(current == zero, f"sharp witness endpoint p={prime}")

    blocks = zero_block_inventory(prime)
    require(
        sum(block_size * count for block_size, count in blocks.items()) == size - 1,
        f"Jordan dimension failed p={prime}",
    )
    for time in range(prime + 1):
        rank_from_blocks = sum(
            max(block_size - time, 0) * count
            for block_size, count in blocks.items()
        )
        require(
            rank_from_blocks == prime ** (prime - time) - 1,
            f"Jordan rank sequence failed p={prime} t={time}",
        )

    print(
        f"LITERAL p={prime} states={size} "
        f"images={'/'.join(map(str, image_sizes))} "
        f"zero_fibres={'/'.join(map(str, zero_fibres))} "
        f"depths={compact(depths)} J0={compact(blocks)} witness=PASS"
    )


def matrix_product(
    left: list[list[int]], right: list[list[int]], prime: int
) -> list[list[int]]:
    rows = len(left)
    middle = len(right)
    columns = len(right[0]) if right else 0
    require(
        all(len(row) == middle for row in left),
        "matrix-product left shape failure",
    )
    return [
        [
            sum(left[i][k] * right[k][j] for k in range(middle)) % prime
            for j in range(columns)
        ]
        for i in range(rows)
    ]


def matrix_vector(
    matrix: list[list[int]], vector: tuple[int, ...], prime: int
) -> tuple[int, ...]:
    return tuple(sum(a * b for a, b in zip(row, vector)) % prime for row in matrix)


def rank_mod(matrix: list[list[int]], prime: int) -> int:
    if not matrix:
        return 0
    work = [row[:] for row in matrix]
    rows = len(work)
    columns = len(work[0])
    pivot_row = 0
    for column in range(columns):
        pivot = next(
            (row for row in range(pivot_row, rows) if work[row][column] % prime),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        inverse = pow(work[pivot_row][column] % prime, -1, prime)
        work[pivot_row] = [(entry * inverse) % prime for entry in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row:
                continue
            scale = work[row][column] % prime
            if scale:
                work[row] = [
                    (a - scale * b) % prime
                    for a, b in zip(work[row], work[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def columns_as_matrix(columns: list[tuple[int, ...]]) -> list[list[int]]:
    if not columns:
        return []
    return [[column[row] for column in columns] for row in range(len(columns[0]))]


def module_certificate(prime: int) -> None:
    identity = [[int(i == j) for j in range(prime)] for i in range(prime)]
    shift = [[int(j == (i + 1) % prime) for j in range(prime)] for i in range(prime)]
    nilpotent = [
        [(shift[i][j] - identity[i][j]) % prime for j in range(prime)]
        for i in range(prime)
    ]

    basis = [binomial_function(degree, prime) for degree in range(prime)]
    require(
        rank_mod(columns_as_matrix(basis), prime) == prime,
        f"binomial basis failed p={prime}",
    )
    for degree, vector in enumerate(basis):
        observed = matrix_vector(nilpotent, vector, prime)
        expected = (0,) * prime if degree == 0 else basis[degree - 1]
        require(observed == expected, f"Pascal ladder failed p={prime} j={degree}")

    power = identity
    ranks = []
    for time in range(prime + 1):
        ranks.append(rank_mod(power, prime))
        require(
            ranks[-1] == prime - time,
            f"difference rank failed p={prime} t={time}",
        )
        if time < prime:
            power = matrix_product(nilpotent, power, prime)

    for step in range(1, prime):
        translation = [
            [int(j == (i + step) % prime) for j in range(prime)]
            for i in range(prime)
        ]
        directed = [
            [(translation[i][j] - identity[i][j]) % prime for j in range(prime)]
            for i in range(prime)
        ]
        for layer in range(prime):
            layer_basis = basis[: prime - layer]
            images = [matrix_vector(directed, vector, prime) for vector in layer_basis]
            require(
                rank_mod(columns_as_matrix(images), prime) == prime - layer - 1,
                f"directed layer rank failed p={prime} a={step} i={layer}",
            )
            anchored_columns = [
                image + (vector[0],) for image, vector in zip(images, layer_basis)
            ]
            require(
                rank_mod(columns_as_matrix(anchored_columns), prime)
                == prime - layer,
                f"anchor injectivity failed p={prime} a={step} i={layer}",
            )

    print(
        f"MODULE p={prime} ranks={'/'.join(map(str, ranks))} "
        f"directions={prime - 1} anchored_layers={prime} PASS"
    )


def main() -> None:
    print("P178_STATE_SELECTED_FINITE_DIFFERENCES")
    print("status=HOLD_EXTERNAL evidence=exact_falsification_not_proof")
    for prime in (2, 3, 5):
        exhaustive_literal_box(prime)
    for prime in (2, 3, 5, 7, 11, 13, 17, 19):
        module_certificate(prime)
    print(f"LITERAL_EDGES={LITERAL_EDGES}")
    print(f"EDGE_DIGEST={EDGE_DIGEST.hexdigest()}")
    print(f"ASSERTIONS={ASSERTIONS}")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
