#!/usr/bin/env python3
"""Process-separated exact control for P194 hostile Review B.

This verifier imports neither the author implementation nor Review A.  Its
deliberately different finite models are:

* literal adjacent ``+- -> empty`` rewriting, rather than a stack or prefix
  record minima, for every crystal signature;
* Fomin matrix-growth local rules, rather than row insertion or Greene
  invariants, for the reverse-word RSK shape;
* Gelfand--Tsetlin interlacing/GL branching, rather than SSYT enumeration or
  Jacobi--Trudi, for principal Schur specializations;
* cyclotomic factor accounting for the hook-content product;
* direct linear-extension orders of the Young cell poset for ``f^lambda``;
* direct matching generation of involutions, rather than scanning S_n.

Finite checks are counterexample pressure, not proof, novelty evidence, or
owner clearance.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from functools import cache
from hashlib import sha256
from itertools import permutations, product
from math import factorial


ASSERTIONS = 0
SIGNATURE_REWRITES = 0
REWRITE_DELETIONS = 0
GROWTH_CALLS = 0
LINEAR_ORDERS_SCANNED = 0
TRANSITIONS = 0
TARGETS = 0
COMPONENTS = 0


def require(condition: bool, message: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def replace_letter(word: tuple[int, ...], position: int, value: int) -> tuple[int, ...]:
    return word[:position] + (value,) + word[position + 1 :]


def reduced_signature(
    word: tuple[int, ...], color: int
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Reduce the literal sign word by repeated adjacent ``+-`` deletion."""
    global SIGNATURE_REWRITES, REWRITE_DELETIONS
    SIGNATURE_REWRITES += 1
    tokens = [
        (1 if letter == color else -1, position)
        for position, letter in enumerate(word)
        if letter == color or letter == color + 1
    ]
    while True:
        pair = next(
            (
                index
                for index in range(len(tokens) - 1)
                if tokens[index][0] == 1 and tokens[index + 1][0] == -1
            ),
            None,
        )
        if pair is None:
            break
        del tokens[pair : pair + 2]
        REWRITE_DELETIONS += 1
    require(
        all(tokens[index][0] <= tokens[index + 1][0]
            for index in range(len(tokens) - 1)),
        f"signature did not reach -...-+...+ normal form: {word}, {color}, {tokens}",
    )
    minus = tuple(position for sign, position in tokens if sign == -1)
    plus = tuple(position for sign, position in tokens if sign == 1)
    return minus, plus


def raising(word: tuple[int, ...], color: int) -> tuple[int, ...] | None:
    minus, _ = reduced_signature(word, color)
    if not minus:
        return None
    return replace_letter(word, minus[-1], color)


def lowering(word: tuple[int, ...], color: int) -> tuple[int, ...] | None:
    _, plus = reduced_signature(word, color)
    if not plus:
        return None
    return replace_letter(word, plus[0], color + 1)


def scheduled_step(
    word: tuple[int, ...], alphabet: int
) -> tuple[tuple[int, ...], int | None]:
    candidates = [
        (color, candidate)
        for color in range(1, alphabet)
        if (candidate := raising(word, color)) is not None
    ]
    if not candidates:
        return word, None
    color, candidate = min(candidates, key=lambda item: item[0])
    return candidate, color


def available_colors(word: tuple[int, ...], alphabet: int) -> tuple[int, ...]:
    return tuple(
        color
        for color in range(1, alphabet)
        if raising(word, color) is not None
    )


def is_highest(word: tuple[int, ...], alphabet: int) -> bool:
    return not available_colors(word, alphabet)


def is_ballot(word: tuple[int, ...], alphabet: int) -> bool:
    counts = [0] * (alphabet + 1)
    for letter in word:
        counts[letter] += 1
        if any(counts[color] < counts[color + 1]
               for color in range(1, alphabet)):
            return False
    return True


def part_at(shape: tuple[int, ...], index: int) -> int:
    return shape[index] if index < len(shape) else 0


def growth_shape(sequence: tuple[int, ...], alphabet: int) -> tuple[int, ...]:
    """RSK shape from the matrix-growth local rule, with no insertion."""
    global GROWTH_CALLS
    GROWTH_CALLS += 1
    columns = len(sequence)
    grid: list[list[tuple[int, ...]]] = [
        [() for _ in range(columns + 1)] for _ in range(alphabet + 1)
    ]
    for row in range(1, alphabet + 1):
        for column in range(1, columns + 1):
            northwest = grid[row - 1][column - 1]
            north = grid[row - 1][column]
            west = grid[row][column - 1]
            entry = int(sequence[column - 1] == row)
            southeast = [max(part_at(north, 0), part_at(west, 0)) + entry]
            limit = max(len(north), len(west)) + 1
            for index in range(1, limit):
                value = (
                    max(part_at(north, index), part_at(west, index))
                    + min(part_at(north, index - 1), part_at(west, index - 1))
                    - part_at(northwest, index - 1)
                )
                southeast.append(value)
            while southeast and southeast[-1] == 0:
                southeast.pop()
            shape = tuple(southeast)
            require(all(value > 0 for value in shape),
                    f"nonpositive growth part: {sequence}, {row}, {column}, {shape}")
            require(all(shape[index] >= shape[index + 1]
                        for index in range(len(shape) - 1)),
                    f"growth output is not a partition: {sequence}, {shape}")
            grid[row][column] = shape
    shape = grid[alphabet][columns]
    require(sum(shape) == columns, f"growth diagram lost boxes: {sequence}, {shape}")
    return shape


def component_shape(word: tuple[int, ...], alphabet: int) -> tuple[int, ...]:
    return growth_shape(tuple(reversed(word)), alphabet)


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def poly_add(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * max(len(left), len(right))
    for index, value in enumerate(left):
        out[index] += value
    for index, value in enumerate(right):
        out[index] += value
    return tuple(trim(out))


def poly_shift(poly: tuple[int, ...], amount: int) -> tuple[int, ...]:
    return (0,) * amount + poly


def poly_multiply(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * (len(left) + len(right) - 1)
    for left_degree, left_value in enumerate(left):
        for right_degree, right_value in enumerate(right):
            out[left_degree + right_degree] += left_value * right_value
    return tuple(trim(out))


def poly_power(poly: tuple[int, ...], exponent: int) -> tuple[int, ...]:
    out = (1,)
    base = poly
    power = exponent
    while power:
        if power & 1:
            out = poly_multiply(out, base)
        base = poly_multiply(base, base)
        power //= 2
    return out


def poly_divide_monic(
    numerator: tuple[int, ...], denominator: tuple[int, ...]
) -> tuple[int, ...]:
    require(denominator[-1] == 1, f"divisor is not monic: {denominator}")
    work = list(numerator)
    degree = len(numerator) - len(denominator)
    require(degree >= 0, f"negative quotient degree: {numerator}, {denominator}")
    quotient = [0] * (degree + 1)
    for shift in range(degree, -1, -1):
        coefficient = work[shift + len(denominator) - 1]
        quotient[shift] = coefficient
        for index, value in enumerate(denominator):
            work[shift + index] -= coefficient * value
    require(all(value == 0 for value in work),
            f"nonexact monic division: {numerator}, {denominator}")
    return tuple(trim(quotient))


def positive_divisors(number: int) -> tuple[int, ...]:
    return tuple(divisor for divisor in range(1, number + 1) if number % divisor == 0)


@cache
def cyclotomic(index: int) -> tuple[int, ...]:
    polynomial = tuple([-1] + [0] * (index - 1) + [1])
    for divisor in positive_divisors(index):
        if divisor < index:
            polynomial = poly_divide_monic(polynomial, cyclotomic(divisor))
    return polynomial


def cells(shape: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    return tuple(
        (row, column)
        for row, row_length in enumerate(shape)
        for column in range(row_length)
    )


def hook_at(shape: tuple[int, ...], row: int, column: int) -> int:
    return (
        shape[row] - column
        + sum(shape[lower_row] > column
              for lower_row in range(row + 1, len(shape)))
    )


def hook_product_cyclotomic(
    shape: tuple[int, ...], alphabet: int
) -> tuple[int, ...]:
    exponents: Counter[int] = Counter()
    for row, column in cells(shape):
        numerator = alphabet + column - row
        denominator = hook_at(shape, row, column)
        require(numerator >= 1 and denominator >= 1,
                f"invalid hook-content exponent: {shape}, {alphabet}")
        exponents.update(positive_divisors(numerator))
        exponents.subtract(positive_divisors(denominator))
    require(all(value >= 0 for value in exponents.values()),
            f"negative cyclotomic multiplicity: {shape}, {alphabet}, {exponents}")
    polynomial = (1,)
    for index in sorted(exponents):
        polynomial = poly_multiply(
            polynomial, poly_power(cyclotomic(index), exponents[index])
        )
    require(all(value >= 0 for value in polynomial),
            f"hook-content expansion has negative coefficient: {shape}, {alphabet}")
    return polynomial


def interlacing_shapes(
    shape: tuple[int, ...], alphabet: int
) -> tuple[tuple[int, ...], ...]:
    padded = shape + (0,) * (alphabet - len(shape))
    ranges = [range(padded[index + 1], padded[index] + 1)
              for index in range(alphabet - 1)]
    out = []
    for entries in product(*ranges):
        candidate = tuple(entries)
        while candidate and candidate[-1] == 0:
            candidate = candidate[:-1]
        out.append(candidate)
    return tuple(out)


@cache
def schur_branching(
    shape: tuple[int, ...], alphabet: int
) -> tuple[int, ...]:
    """s_shape(1,q,...,q^(alphabet-1)) by GL branching."""
    require(len(shape) <= alphabet, f"shape exceeds alphabet: {shape}, {alphabet}")
    if not shape:
        return (1,)
    if alphabet == 1:
        require(len(shape) == 1, f"nonrow shape at alphabet one: {shape}")
        return (1,)
    result = (0,)
    size = sum(shape)
    for lower in interlacing_shapes(shape, alphabet):
        term = poly_shift(
            schur_branching(lower, alphabet - 1),
            (alphabet - 1) * (size - sum(lower)),
        )
        result = poly_add(result, term)
    return result


def normalized_branching(
    shape: tuple[int, ...], alphabet: int
) -> tuple[int, ...]:
    raw = schur_branching(shape, alphabet)
    shift = sum(row * row_length for row, row_length in enumerate(shape))
    require(all(value == 0 for value in raw[:shift]),
            f"branching polynomial begins below n(lambda): {shape}, {alphabet}")
    normalized = tuple(trim(list(raw[shift:] or (0,))))
    require(all(value >= 0 for value in normalized),
            f"negative normalized branching coefficient: {shape}, {alphabet}")
    return normalized


def partitions(total: int, ceiling: int | None = None):
    if total == 0:
        yield ()
        return
    if ceiling is None or ceiling > total:
        ceiling = total
    for first in range(ceiling, 0, -1):
        for tail in partitions(total - first, first):
            yield (first,) + tail


@cache
def young_linear_extensions(shape: tuple[int, ...]) -> int:
    """Count SYT as literal linear orders of the Young cell poset."""
    global LINEAR_ORDERS_SCANNED
    diagram = cells(shape)
    index = {cell: position for position, cell in enumerate(diagram)}
    prerequisites = [0] * len(diagram)
    for position, (row, column) in enumerate(diagram):
        if column:
            prerequisites[position] |= 1 << index[(row, column - 1)]
        if row and column < shape[row - 1]:
            prerequisites[position] |= 1 << index[(row - 1, column)]
    count = 0
    for order in permutations(range(len(diagram))):
        LINEAR_ORDERS_SCANNED += 1
        used = 0
        valid = True
        for position in order:
            if prerequisites[position] & ~used:
                valid = False
                break
            used |= 1 << position
        count += int(valid)
    return count


def generate_involutions(size: int):
    permutation = [-1] * size

    def visit():
        first = next((index for index, value in enumerate(permutation) if value < 0), None)
        if first is None:
            yield tuple(value + 1 for value in permutation)
            return
        permutation[first] = first
        yield from visit()
        permutation[first] = -1
        for partner in range(first + 1, size):
            if permutation[partner] < 0:
                permutation[first] = partner
                permutation[partner] = first
                yield from visit()
                permutation[first] = -1
                permutation[partner] = -1

    yield from visit()


def longest_decreasing_subsequence(permutation: tuple[int, ...]) -> int:
    lengths = [1] * len(permutation)
    for right in range(len(permutation)):
        lengths[right] = 1 + max(
            (lengths[left] for left in range(right)
             if permutation[left] > permutation[right]),
            default=0,
        )
    return max(lengths, default=0)


def telephone_number(size: int) -> int:
    previous, current = 1, 1
    for index in range(2, size + 1):
        previous, current = current, current + (index - 1) * previous
    return current if size else previous


@cache
def involution_shape_counts(size: int) -> tuple[tuple[tuple[int, ...], int], ...]:
    counts: Counter[tuple[int, ...]] = Counter()
    for permutation in generate_involutions(size):
        shape = growth_shape(permutation, size)
        require(len(shape) == longest_decreasing_subsequence(permutation),
                f"growth height/LDS mismatch: {permutation}, {shape}")
        counts[shape] += 1
    require(sum(counts.values()) == telephone_number(size),
            f"matching/telephone mismatch at n={size}")
    return tuple(sorted(counts.items()))


def predicted_predecessors(
    target: tuple[int, ...], alphabet: int
) -> set[tuple[int, ...]]:
    candidates: set[tuple[int, ...]] = set()
    if is_highest(target, alphabet):
        candidates.add(target)
    for color in range(1, alphabet):
        source = lowering(target, color)
        if source is not None and all(
            raising(source, lower_color) is None
            for lower_color in range(1, color)
        ):
            candidates.add(source)
    return candidates


class DisjointSet:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, item: int) -> int:
        while self.parent[item] != item:
            self.parent[item] = self.parent[self.parent[item]]
            item = self.parent[item]
        return item

    def union(self, left: int, right: int) -> None:
        left_root = self.find(left)
        right_root = self.find(right)
        if left_root == right_root:
            return
        if self.rank[left_root] < self.rank[right_root]:
            left_root, right_root = right_root, left_root
        self.parent[right_root] = left_root
        if self.rank[left_root] == self.rank[right_root]:
            self.rank[left_root] += 1


def counter_from_poly(poly: tuple[int, ...]) -> Counter[int]:
    return Counter({degree: value for degree, value in enumerate(poly) if value})


def add_scaled(target: Counter[int], poly: tuple[int, ...], scale: int) -> None:
    for degree, value in enumerate(poly):
        if value:
            target[degree] += scale * value


def verify_signature_and_boundaries(digest) -> dict[str, int | str]:
    require(raising((2, 1), 1) == (1, 1), "e_1 orientation witness failed")
    require(lowering((1, 1), 1) == (2, 1), "f_1 orientation witness failed")
    require(raising((1, 2), 1) is None, "cancelled +- should have no raising")
    require(lowering((1, 2), 1) is None, "cancelled +- should have no lowering")
    require(growth_shape((2, 1), 2) == (1, 1), "ordinary shape witness failed")
    require(growth_shape((1, 1), 2) == (2,), "ordinary target shape failed")
    require(component_shape((2, 1), 2) == (2,), "reverse source shape failed")
    require(component_shape((1, 1), 2) == (2,), "reverse target shape failed")

    require(available_colors((3, 2, 1), 3) == (1, 2),
            "multiple-colour availability witness failed")
    require(scheduled_step((3, 2, 1), 3) == ((3, 1, 1), 1),
            "least-colour selection failed")

    word = (3, 3, 3)
    orbit = [word]
    colors = []
    while True:
        successor, color = scheduled_step(word, 3)
        if color is None:
            break
        colors.append(color)
        orbit.append(successor)
        word = successor
    require(
        orbit == [
            (3, 3, 3), (3, 3, 2), (3, 3, 1), (3, 2, 1),
            (3, 1, 1), (2, 1, 1), (1, 1, 1),
        ],
        f"sample orbit mismatch: {orbit}",
    )
    require(colors == [2, 1, 2, 1, 2, 1], f"sample colors mismatch: {colors}")

    boundary_checks = 0
    for alphabet in range(1, 15):
        for letter in range(1, alphabet + 1):
            word = (letter,)
            depth = 0
            while True:
                successor, color = scheduled_step(word, alphabet)
                if color is None:
                    break
                require(color == word[0] - 1, f"n=1 color mismatch: {word}, {color}")
                word = successor
                depth += 1
            require(word == (1,) and depth == letter - 1,
                    f"n=1 clock mismatch: k={alphabet}, a={letter}")
            boundary_checks += 1
    for length in range(1, 15):
        word = (1,) * length
        require(scheduled_step(word, 1) == (word, None), "k=1 step failed")
        require(predicted_predecessors(word, 1) == {word}, "k=1 fibre failed")
        require(component_shape(word, 1) == (length,), "k=1 shape failed")
        boundary_checks += 1
    digest.update(f"BOUNDARY|{orbit}|{colors}|{boundary_checks}\n".encode())
    return {
        "boundary_checks": boundary_checks,
        "sample_steps": len(colors),
        "tensor_witness": "21_to_11_reverse_2_to_2_ordinary_11_to_2",
    }


def verify_complete_boxes(digest) -> dict[str, int | str]:
    global TRANSITIONS, TARGETS, COMPONENTS
    totals: dict[str, int | str] = {
        "boxes": 0,
        "states": 0,
        "fixed": 0,
        "components": 0,
        "empty_fibres": 0,
        "full_fibres": 0,
        "max_fibre": 0,
        "branching_checks": 0,
        "cyclotomic_checks": 0,
        "linear_extension_checks": 0,
        "depth_maxima_checksum": 0,
        "last_box": "",
    }
    for alphabet in range(1, 8):
        for length in range(1, 6):
            universe = list(product(range(1, alphabet + 1), repeat=length))
            index = {word: position for position, word in enumerate(universe)}
            disjoint = DisjointSet(len(universe))
            transitions: dict[tuple[int, ...], tuple[int, ...]] = {}
            selected_colors: dict[tuple[int, ...], int | None] = {}
            incoming: dict[tuple[int, ...], set[tuple[int, ...]]] = defaultdict(set)
            shapes: dict[tuple[int, ...], tuple[int, ...]] = {}

            for word in universe:
                shape = component_shape(word, alphabet)
                shapes[word] = shape
                successor, selected = scheduled_step(word, alphabet)
                transitions[word] = successor
                selected_colors[word] = selected
                incoming[successor].add(word)
                TRANSITIONS += 1
                require(successor in index, f"step left carrier: {word}, {successor}")
                require((selected is None) == (successor == word),
                        f"hold/selection mismatch: {word}, {selected}, {successor}")
                require(is_highest(word, alphabet) == is_ballot(word, alphabet),
                        f"highest/ballot mismatch: {word}")
                if selected is None:
                    require(is_highest(word, alphabet), f"nonhighest hold: {word}")
                else:
                    require(sum(successor) == sum(word) - 1,
                            f"energy did not fall by one: {word}, {successor}")
                    require(lowering(successor, selected) == word,
                            f"selected edge does not invert: {word}, {selected}")
                for color in range(1, alphabet):
                    raised = raising(word, color)
                    if raised is not None:
                        require(lowering(raised, color) == word,
                                f"colour edge inversion failed: {word}, {color}")
                        disjoint.union(index[word], index[raised])
                        require(component_shape(raised, alphabet) == shape,
                                f"growth shape changes on edge: {word}, {color}")
                digest.update(f"T|{alphabet}|{length}|{word}|{selected}|{successor}|{shape}\n".encode())

            depths: dict[tuple[int, ...], int] = {}
            endpoints: dict[tuple[int, ...], tuple[int, ...]] = {}
            for word in sorted(universe, key=lambda item: (sum(item), item)):
                successor = transitions[word]
                if successor == word:
                    depths[word] = 0
                    endpoints[word] = word
                else:
                    require(successor in depths,
                            f"energy order did not resolve successor: {word}, {successor}")
                    depths[word] = depths[successor] + 1
                    endpoints[word] = endpoints[successor]
                endpoint = endpoints[word]
                require(is_highest(endpoint, alphabet), f"endpoint not highest: {word}")
                content = tuple(endpoint.count(letter)
                                for letter in range(1, alphabet + 1))
                while content and content[-1] == 0:
                    content = content[:-1]
                require(content == shapes[word],
                        f"endpoint content/growth shape mismatch: {word}, {content}, {shapes[word]}")
                baseline = sum((row + 1) * row_length
                               for row, row_length in enumerate(shapes[word]))
                require(depths[word] == sum(word) - baseline,
                        f"clock mismatch: {word}, {depths[word]}, {baseline}")

            maximum_depth = max(depths.values())
            maximizers = {word for word in universe if depths[word] == maximum_depth}
            require(maximum_depth == length * (alphabet - 1),
                    f"sharp depth mismatch: {(length, alphabet)}, {maximum_depth}")
            require(maximizers == {(alphabet,) * length},
                    f"deepest word not unique: {(length, alphabet)}, {maximizers}")

            box_empty = 0
            box_full = 0
            box_max_fibre = 0
            for target in universe:
                actual = incoming.get(target, set())
                predicted = predicted_predecessors(target, alphabet)
                TARGETS += 1
                require(actual == predicted,
                        f"exact fibre mismatch: {(length, alphabet, target)}, {actual}, {predicted}")
                require((target in actual) == is_highest(target, alphabet),
                        f"self-source boundary mismatch: {target}")
                require(len(actual) <= alphabet,
                        f"uniform fibre bound failed: {(length, alphabet, target)}")
                require(all(
                    source == target
                    or sum(left != right for left, right in zip(source, target)) == 1
                    for source in actual
                ), f"fibre contains nonlocal source: {target}, {actual}")
                box_empty += int(not actual)
                box_full += int(len(actual) == alphabet)
                box_max_fibre = max(box_max_fibre, len(actual))
                digest.update(
                    f"F|{alphabet}|{length}|{target}|{tuple(sorted(actual))}\n".encode()
                )
            require(sum(len(incoming.get(target, set())) for target in universe) == len(universe),
                    f"fibre mass failed: {(length, alphabet)}")
            expected_full = alphabet == 1 or length >= alphabet * (alphabet - 1) // 2
            require((box_max_fibre == alphabet) == expected_full,
                    f"stable threshold mismatch: {(length, alphabet)}, {box_max_fibre}")

            grouped: dict[int, list[tuple[int, ...]]] = defaultdict(list)
            for word in universe:
                grouped[disjoint.find(index[word])].append(word)
            COMPONENTS += len(grouped)
            components_by_shape: Counter[tuple[int, ...]] = Counter()
            component_polys: dict[tuple[int, ...], Counter[int]] = {}
            for component in grouped.values():
                component_shapes = {shapes[word] for word in component}
                component_highest = {word for word in component if is_highest(word, alphabet)}
                component_endpoints = {endpoints[word] for word in component}
                require(len(component_shapes) == 1,
                        f"component has multiple growth shapes: {(length, alphabet)}")
                require(len(component_highest) == 1 and component_endpoints == component_highest,
                        f"component does not have one scheduled sink: {(length, alphabet)}")
                shape = next(iter(component_shapes))
                histogram = Counter(depths[word] for word in component)
                expected_poly = normalized_branching(shape, alphabet)
                require(histogram == counter_from_poly(expected_poly),
                        f"component/Gelfand--Tsetlin layer mismatch: {shape}, {alphabet}")
                if shape in component_polys:
                    require(component_polys[shape] == histogram,
                            f"same-shape components have different layers: {shape}, {alphabet}")
                component_polys[shape] = histogram
                components_by_shape[shape] += 1

            global_expected: Counter[int] = Counter()
            fixed_expected = 0
            for shape in partitions(length):
                if len(shape) > alphabet:
                    continue
                branching = normalized_branching(shape, alphabet)
                cyclotomic_product = hook_product_cyclotomic(shape, alphabet)
                require(branching == cyclotomic_product,
                        f"branching/hook-content mismatch: {shape}, {alphabet}")
                multiplicity = young_linear_extensions(shape)
                require(components_by_shape[shape] == multiplicity,
                        f"component/Young-poset multiplicity mismatch: {shape}, {alphabet}")
                add_scaled(global_expected, branching, multiplicity)
                fixed_expected += multiplicity
                totals["branching_checks"] = int(totals["branching_checks"]) + 1
                totals["cyclotomic_checks"] = int(totals["cyclotomic_checks"]) + 1
                totals["linear_extension_checks"] = int(totals["linear_extension_checks"]) + 1
                digest.update(
                    f"P|{alphabet}|{length}|{shape}|{branching}|{multiplicity}\n".encode()
                )
            actual_global = Counter(depths.values())
            require(actual_global == global_expected,
                    f"global layer polynomial mismatch: {(length, alphabet)}")
            require(sum(global_expected.values()) == alphabet ** length,
                    f"global polynomial mass mismatch: {(length, alphabet)}")
            fixed_actual = sum(depth == 0 for depth in depths.values())
            require(fixed_actual == fixed_expected,
                    f"fixed component census mismatch: {(length, alphabet)}")
            involution_counts = Counter(dict(involution_shape_counts(length)))
            bounded_involutions = sum(
                count for shape, count in involution_counts.items()
                if len(shape) <= alphabet
            )
            require(bounded_involutions == fixed_actual,
                    f"fixed/involution specialization mismatch: {(length, alphabet)}")
            if alphabet >= length:
                require(fixed_actual == telephone_number(length),
                        f"stable telephone mismatch: {(length, alphabet)}")

            totals["boxes"] = int(totals["boxes"]) + 1
            totals["states"] = int(totals["states"]) + len(universe)
            totals["fixed"] = int(totals["fixed"]) + fixed_actual
            totals["components"] = int(totals["components"]) + len(grouped)
            totals["empty_fibres"] = int(totals["empty_fibres"]) + box_empty
            totals["full_fibres"] = int(totals["full_fibres"]) + box_full
            totals["max_fibre"] = max(int(totals["max_fibre"]), box_max_fibre)
            totals["depth_maxima_checksum"] = (
                int(totals["depth_maxima_checksum"]) + maximum_depth
            )
            totals["last_box"] = (
                f"k{alphabet}_n{length}_states{len(universe)}_fixed{fixed_actual}_"
                f"maxdepth{maximum_depth}_maxfibre{box_max_fibre}_"
                f"empty{box_empty}_full{box_full}"
            )
    return totals


def verify_involution_specialization(digest, maximum_size: int = 8) -> dict[str, int]:
    totals = {"involutions": 0, "shape_checks": 0, "height_checks": 0}
    for size in range(1, maximum_size + 1):
        counts = Counter(dict(involution_shape_counts(size)))
        require(sum(counts.values()) == telephone_number(size),
                f"involution total mismatch at n={size}")
        for shape in partitions(size):
            require(counts[shape] == young_linear_extensions(shape),
                    f"matching involutions/linear extensions mismatch: {size}, {shape}")
            totals["shape_checks"] += 1
        for alphabet in range(1, size + 2):
            bounded = sum(count for shape, count in counts.items()
                          if len(shape) <= alphabet)
            expected = sum(young_linear_extensions(shape) for shape in partitions(size)
                           if len(shape) <= alphabet)
            require(bounded == expected,
                    f"bounded involution specialization mismatch: {size}, {alphabet}")
            if alphabet >= size:
                require(bounded == telephone_number(size),
                        f"telephone stable range mismatch: {size}, {alphabet}")
            totals["height_checks"] += 1
        totals["involutions"] += sum(counts.values())
        digest.update(f"I|{size}|{tuple(sorted(counts.items()))}\n".encode())
    return totals


def staircase_target(alphabet: int, surplus: int) -> tuple[int, ...]:
    return tuple(
        letter
        for letter in range(1, alphabet)
        for _ in range(alphabet - letter + (surplus if letter == 1 else 0))
    )


def verify_stable_threshold(digest) -> dict[str, int]:
    witnesses = 0
    subthreshold_partition_checks = 0
    for length in range(1, 5):
        target = (1,) * length
        require(predicted_predecessors(target, 1) == {target},
                f"k=1 stable fibre failed at n={length}")
        witnesses += 1
    for alphabet in range(2, 13):
        threshold = alphabet * (alphabet - 1) // 2
        for surplus in range(4):
            target = staircase_target(alphabet, surplus)
            require(len(target) == threshold + surplus,
                    f"staircase length mismatch: {alphabet}, {surplus}")
            require(is_highest(target, alphabet),
                    f"staircase not highest: {alphabet}, {surplus}")
            predecessors = predicted_predecessors(target, alphabet)
            require(len(predecessors) == alphabet,
                    f"staircase fibre not full: {alphabet}, {surplus}")
            for source in predecessors:
                require(scheduled_step(source, alphabet)[0] == target,
                        f"staircase candidate is not literal source: {alphabet}, {surplus}")
            digest.update(
                f"S|{alphabet}|{surplus}|{target}|{tuple(sorted(predecessors))}\n".encode()
            )
            witnesses += 1
        for length in range(max(1, threshold - 3), threshold):
            for shape in partitions(length):
                padded = shape + (0,) * (alphabet - len(shape))
                require(not all(padded[index] > padded[index + 1]
                                for index in range(alphabet - 1)),
                        f"subthreshold strict partition exists: {alphabet}, {length}, {shape}")
                subthreshold_partition_checks += 1
    return {
        "witnesses": witnesses,
        "subthreshold_partition_checks": subthreshold_partition_checks,
    }


def main() -> None:
    digest = sha256()
    boundary = verify_signature_and_boundaries(digest)
    boxes = verify_complete_boxes(digest)
    involutions = verify_involution_specialization(digest)
    stable = verify_stable_threshold(digest)

    print("P194_HOSTILE_REVIEW_B_EXACT_CONTROL")
    print("REPRESENTATION=sign_rewrite_growth_diagram_gt_branching_cyclotomic_young_poset_matchings")
    print("AUTHOR_CODE_IMPORTED=false")
    print("REVIEW_A_CODE_IMPORTED=false")
    print("WORD_BOXES=k1..7_n1..5")
    print(f"BOX_COUNT={boxes['boxes']}")
    print(f"STATES={boxes['states']}")
    print(f"TRANSITIONS={TRANSITIONS}")
    print(f"TARGETS={TARGETS}")
    print(f"FIXED_STATES={boxes['fixed']}")
    print(f"CRYSTAL_COMPONENTS={boxes['components']}")
    print(f"EMPTY_FIBRES={boxes['empty_fibres']}")
    print(f"FULL_FIBRES={boxes['full_fibres']}")
    print(f"LARGEST_OBSERVED_FIBRE={boxes['max_fibre']}")
    print(f"DEPTH_MAXIMA_CHECKSUM={boxes['depth_maxima_checksum']}")
    print(f"LAST_BOX={boxes['last_box']}")
    print(f"SIGNATURE_REWRITES={SIGNATURE_REWRITES}")
    print(f"REWRITE_DELETIONS={REWRITE_DELETIONS}")
    print(f"GROWTH_DIAGRAM_CALLS={GROWTH_CALLS}")
    print(f"BRANCHING_CHECKS={boxes['branching_checks']}")
    print(f"CYCLOTOMIC_PRODUCT_CHECKS={boxes['cyclotomic_checks']}")
    print(f"YOUNG_LINEAR_EXTENSION_CHECKS={boxes['linear_extension_checks']}")
    print(f"LINEAR_ORDERS_SCANNED={LINEAR_ORDERS_SCANNED}")
    print(f"INVOLUTIONS_N1_TO_8={involutions['involutions']}")
    print(f"INVOLUTION_SHAPE_CHECKS={involutions['shape_checks']}")
    print(f"INVOLUTION_HEIGHT_CHECKS={involutions['height_checks']}")
    print(f"STABLE_WITNESSES={stable['witnesses']}")
    print(f"SUBTHRESHOLD_PARTITION_CHECKS={stable['subthreshold_partition_checks']}")
    print(f"BOUNDARY_CHECKS={boundary['boundary_checks']}")
    print(f"SAMPLE_333_STEPS={boundary['sample_steps']}")
    print(f"TENSOR_WITNESS={boundary['tensor_witness']}")
    print(f"ASSERTIONS={ASSERTIONS}")
    print(f"CONTROL_DIGEST={digest.hexdigest()}")
    print("HISTORICAL_FINDINGS=0C_1M_0m_ALL_RESOLVED")
    print("CRITICAL_FINDINGS=0")
    print("MAJOR_FINDINGS=0")
    print("MINOR_FINDINGS=0")
    print("VERDICT=PROVABLE_AS_STATED_AFTER_ACCEPTED_SOURCE_REPAIR")
    print("OWNER_GATE=OWNER_AMBER")
    print("EXTERNAL_STATE=HOLD_EXTERNAL")
    print("FINITE_CONTROL_IS_NOT_PROOF_OR_NOVELTY=true")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
