#!/usr/bin/env python3
"""Exact and sparse utilities for frozen candidate SD-C24.

The graph constructor uses only successor, divisibility, and the exposed
integer quotient. Atomicity tests and target comparisons belong to separate
post-freeze evaluation code.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import cos, exp, factorial, isqrt, log, pi, sin, sqrt
from typing import Callable, Iterable, Iterator, Mapping, Sequence


CANDIDATE_ID = "SD-C24"
SOURCE_AUDIT_CUTOFF = 4096
SIMPLE_CYCLE_CUTOFFS = (12, 20, 30)
ROOTED_MAX_POWER = 8
GROUP_MAX_POWER = 10
TRACE_INTEGER_S_VALUES = (1, 2)
TRACE_DIAGNOSTIC_CUTOFFS = (32, 64, 128, 256, 512, 1024, 2048)
TRACE_PARAMETER_POINTS = (
    (0.60, 0.00, "trace_class"),
    (0.51, 0.01, "trace_class"),
    (0.60, -0.20, "unbounded_fixed_row"),
    (0.49, 0.20, "not_trace_class_successor"),
    (0.75, -0.20, "trace_class"),
    (0.00, 1.50, "bounded_control_noncompact"),
    (0.50, 0.25, "not_trace_class_successor_boundary"),
    (0.75, -0.25, "unbounded_fixed_row_boundary"),
)


def positive_divisors(value: int) -> tuple[int, ...]:
    """Return all positive divisors without using any arithmetic oracle."""

    if value < 1:
        raise ValueError("value must be positive")
    divisors: set[int] = set()
    for candidate in range(1, isqrt(value) + 1):
        if value % candidate == 0:
            divisors.add(candidate)
            divisors.add(value // candidate)
    return tuple(sorted(divisors))


def edge_quotient(source: int, target: int) -> int:
    """Return q=(source+1)/target after checking the frozen edge identity."""

    if source < 2 or target < 2 or (source + 1) % target:
        raise ValueError(f"not a successor-divisor edge: {source}->{target}")
    return (source + 1) // target


def edges_from(source: int, cutoff: int | None = None) -> tuple[tuple[int, int], ...]:
    """Return sorted (target, quotient) pairs for the frozen graph."""

    if source < 2:
        raise ValueError("source must be at least two")
    upper = source + 1 if cutoff is None else min(source + 1, cutoff)
    return tuple(
        (target, (source + 1) // target)
        for target in positive_divisors(source + 1)
        if 2 <= target <= upper
    )


def induced_adjacency(cutoff: int) -> dict[int, tuple[tuple[int, int], ...]]:
    """Return the sparse graph induced on vertices 2,...,cutoff."""

    if cutoff < 2:
        return {}
    return {
        source: edges_from(source, cutoff=cutoff)
        for source in range(2, cutoff + 1)
    }


def edge_identity_audit(cutoff: int) -> dict[str, int | bool | str]:
    """Audit every source edge through a deterministic finite cutoff."""

    edge_count = 0
    successor_count = 0
    quotient_mismatches = 0
    loop_count = 0
    min_quotient = None
    max_quotient = 0
    for source in range(2, cutoff + 1):
        for target, quotient in edges_from(source):
            edge_count += 1
            quotient_mismatches += int(source + 1 != target * quotient)
            successor_count += int(quotient == 1)
            loop_count += int(source == target)
            min_quotient = quotient if min_quotient is None else min(
                min_quotient, quotient
            )
            max_quotient = max(max_quotient, quotient)
    return {
        "candidate_id": CANDIDATE_ID,
        "cutoff": cutoff,
        "edge_count": edge_count,
        "successor_edge_count": successor_count,
        "quotient_identity_mismatches": quotient_mismatches,
        "loop_count": loop_count,
        "min_quotient": min_quotient or 0,
        "max_quotient": max_quotient,
        "graph_rule": "target>=2 and target divides source+1",
        "quotient_rule": "q=(source+1)//target",
        "prime_table_used": False,
        "target_feedback_used": False,
        "riemann_zero_data_used": False,
    }


def canonical_rotation(word: Sequence[int]) -> tuple[int, ...]:
    """Canonicalize a directed cyclic word by rotation, never reflection."""

    values = tuple(word)
    if not values:
        return values
    return min(values[index:] + values[:index] for index in range(len(values)))


def rotations(word: Sequence[int]) -> tuple[tuple[int, ...], ...]:
    values = tuple(word)
    return tuple(
        values[index:] + values[:index] for index in range(len(values))
    )


def minimal_temporal_period(word: Sequence[int]) -> int:
    """Return the primitive temporal period of a rooted closed word."""

    values = tuple(word)
    length = len(values)
    for period in range(1, length + 1):
        if length % period == 0 and values == values[:period] * (length // period):
            return period
    raise AssertionError("unreachable")


def canonical_primitive_root(word: Sequence[int]) -> tuple[int, ...]:
    values = tuple(word)
    period = minimal_temporal_period(values)
    return canonical_rotation(values[:period])


def is_rotation_of(left: Sequence[int], right: Sequence[int]) -> bool:
    return len(left) == len(right) and tuple(left) in rotations(tuple(right))


def enumerate_simple_cycles(cutoff: int) -> tuple[tuple[int, ...], ...]:
    """Enumerate simple directed cycles once modulo rotation.

    Each cycle is started at its unique minimum vertex. This sparse DFS never
    forms the Cartesian product of the vertex set.
    """

    adjacency = induced_adjacency(cutoff)
    found: list[tuple[int, ...]] = []
    for start in range(2, cutoff + 1):
        path = [start]
        visited = {start}

        def visit(current: int) -> None:
            for target, _quotient in adjacency[current]:
                if target < start:
                    continue
                if target == start:
                    if len(path) >= 2:
                        found.append(tuple(path))
                    continue
                if target in visited:
                    continue
                visited.add(target)
                path.append(target)
                visit(target)
                path.pop()
                visited.remove(target)

        visit(start)
    canonical = tuple(sorted(set(map(canonical_rotation, found)), key=lambda w: (len(w), w)))
    if len(canonical) != len(found):
        raise AssertionError("simple-cycle canonicalization was not unique")
    return canonical


def cofactor_word(cycle: Sequence[int]) -> tuple[int, ...]:
    values = tuple(cycle)
    if not values:
        return ()
    return tuple(
        edge_quotient(values[index], values[(index + 1) % len(values)])
        for index in range(len(values))
    )


def cycle_holonomy(cycle: Sequence[int]) -> int:
    result = 1
    for quotient in cofactor_word(cycle):
        result *= quotient
    return result


def telescoping_holonomy(cycle: Sequence[int]) -> Fraction:
    result = Fraction(1, 1)
    for vertex in cycle:
        result *= Fraction(vertex + 1, vertex)
    return result


def cycle_mass(cycle: Sequence[int]) -> int:
    result = 1
    for vertex in cycle:
        result *= vertex
    return result


def atomic_family_cycle(k: int, atom: int) -> tuple[int, ...]:
    """Return C_(k,atom) without testing whether atom is irreducible."""

    if k < 2 or atom < 2:
        raise ValueError("k and atom must be at least two")
    return tuple(range(k, atom * k))


def atomic_family_mass(k: int, atom: int) -> int:
    if k < 2 or atom < 2:
        raise ValueError("k and atom must be at least two")
    return factorial(atom * k - 1) // factorial(k - 1)


def canonical_cycle(k: int) -> tuple[int, ...]:
    return atomic_family_cycle(k, 2)


def enumerate_rooted_closed_walks(length: int) -> tuple[tuple[int, ...], ...]:
    """Enumerate actual rooted closed paths at a theorem-certified cutoff."""

    if length < 1:
        raise ValueError("length must be positive")
    cutoff = 2 * length - 1
    adjacency = induced_adjacency(cutoff)
    closed: list[tuple[int, ...]] = []
    for start in range(2, cutoff + 1):
        path = [start]

        def advance(current: int, remaining: int) -> None:
            for target, _quotient in adjacency[current]:
                if remaining == 1:
                    if target == start:
                        closed.append(tuple(path))
                    continue
                path.append(target)
                advance(target, remaining - 1)
                path.pop()

        advance(start, length)
    return tuple(closed)


def edge_weight_fraction(source: int, target: int, s_integer: int, u_integer: int = 0) -> Fraction:
    if s_integer < 0:
        raise ValueError("exact experiment uses nonnegative integer s")
    quotient = edge_quotient(source, target)
    endpoint = Fraction(1, (source * target) ** s_integer)
    cofactor = (
        Fraction(1, quotient**u_integer)
        if u_integer >= 0
        else Fraction(quotient ** (-u_integer), 1)
    )
    return endpoint * cofactor


def sparse_group_trace(power: int, s_integer: int) -> dict[int, Fraction]:
    """Compute the exact group-algebra trace by sparse dynamic programming."""

    if power < 1:
        raise ValueError("power must be positive")
    cutoff = 2 * power - 1
    adjacency = induced_adjacency(cutoff)
    result: defaultdict[int, Fraction] = defaultdict(Fraction)
    for start in range(2, cutoff + 1):
        states: dict[tuple[int, int], Fraction] = {(start, 1): Fraction(1)}
        for _step in range(power):
            following: defaultdict[tuple[int, int], Fraction] = defaultdict(Fraction)
            for (current, holonomy), weight in states.items():
                for target, quotient in adjacency[current]:
                    following[(target, holonomy * quotient)] += (
                        weight
                        * edge_weight_fraction(current, target, s_integer, 0)
                    )
            states = dict(following)
        for (current, holonomy), weight in states.items():
            if current == start:
                result[holonomy] += weight
    return dict(sorted(result.items()))


def expected_atomic_trace(power: int, s_integer: int, atom: int) -> Fraction:
    """Closed formula for the connected rooted coefficient at atomic label."""

    step = atom - 1
    if power % step:
        return Fraction(0)
    k = power // step
    if k < 2:
        return Fraction(0)
    mass = atomic_family_mass(k, atom)
    return Fraction(power, mass ** (2 * s_integer))


def trace_class_membership(sigma: float, a: float) -> bool:
    return sigma > 0.5 and sigma + a > 0.5


def trace_class_failure_mode(sigma: float, a: float) -> str:
    if sigma + a <= 0.5:
        return "unbounded_fixed_row"
    if sigma <= 0.5:
        return "not_trace_class_successor"
    return "trace_class"


def row_nuclear_prefix(cutoff: int, sigma: float, a: float) -> float:
    total = 0.0
    for target in range(2, cutoff + 1):
        inner = 0.0
        q0 = 2 if target == 2 else 1
        max_q = (cutoff + 1) // target
        for quotient in range(q0, max_q + 1):
            source = target * quotient - 1
            inner += (
                target ** (-2.0 * sigma)
                * source ** (-2.0 * sigma)
                * quotient ** (-2.0 * a)
            )
        total += sqrt(inner)
    return total


def fixed_row_squared_prefix(
    target: int, max_quotient: int, sigma: float, a: float
) -> float:
    q0 = 2 if target == 2 else 1
    return sum(
        target ** (-2.0 * sigma)
        * (target * quotient - 1) ** (-2.0 * sigma)
        * quotient ** (-2.0 * a)
        for quotient in range(q0, max_quotient + 1)
    )


def successor_trace_prefix(cutoff: int, sigma: float) -> float:
    return sum(
        (source * (source + 1)) ** (-sigma)
        for source in range(2, cutoff + 1)
    )


def inventory_value(name: str, vertex: int) -> Fraction:
    if vertex < 2:
        raise ValueError("vertex must be at least two")
    if name == "native_integer":
        return Fraction(vertex)
    if name == "shifted":
        return Fraction(vertex + 1)
    if name == "composite_polynomial":
        return Fraction(vertex * vertex + vertex)
    if name == "quadratic_generic":
        return Fraction(vertex * vertex + 1)
    if name == "exponential":
        return Fraction(2**vertex)
    if name == "deterministic_perturbed":
        offset = 1 + ((37 * vertex + 11) % 97)
        return Fraction(97 * vertex + offset, 97)
    raise KeyError(name)


INVENTORY_NAMES = (
    "native_integer",
    "shifted",
    "composite_polynomial",
    "quadratic_generic",
    "exponential",
    "deterministic_perturbed",
)


def inventory_cycle_product(name: str, cycle: Sequence[int]) -> Fraction:
    value = Fraction(1)
    for vertex in cycle:
        value *= inventory_value(name, vertex)
    return value


def transported_vertex(vertex: int) -> int:
    """A fixed involutive relabeling of V used only as presentation control."""

    if vertex < 2:
        raise ValueError("vertex must be at least two")
    return vertex + 1 if vertex % 2 == 0 else vertex - 1


def transported_cycle(cycle: Sequence[int]) -> tuple[int, ...]:
    return tuple(transported_vertex(vertex) for vertex in cycle)


def fraction_matrix(
    cutoff: int, s_integer: int, u_integer: int
) -> list[list[Fraction]]:
    size = cutoff - 1
    matrix = [[Fraction(0) for _ in range(size)] for _ in range(size)]
    for source in range(2, cutoff + 1):
        for target, _quotient in edges_from(source, cutoff=cutoff):
            matrix[target - 2][source - 2] = edge_weight_fraction(
                source, target, s_integer, u_integer
            )
    return matrix


def matrix_multiply(
    left: Sequence[Sequence[Fraction]], right: Sequence[Sequence[Fraction]]
) -> list[list[Fraction]]:
    size = len(left)
    output = [[Fraction(0) for _ in range(size)] for _ in range(size)]
    for row in range(size):
        for pivot in range(size):
            coefficient = left[row][pivot]
            if coefficient == 0:
                continue
            for column in range(size):
                if right[pivot][column]:
                    output[row][column] += coefficient * right[pivot][column]
    return output


def finite_trace_powers(
    matrix: Sequence[Sequence[Fraction]], max_power: int
) -> list[Fraction]:
    size = len(matrix)
    power_matrix = [list(row) for row in matrix]
    traces: list[Fraction] = []
    for power in range(1, max_power + 1):
        traces.append(sum(power_matrix[index][index] for index in range(size)))
        if power != max_power:
            power_matrix = matrix_multiply(power_matrix, matrix)
    return traces


def newton_determinant_coefficients(
    traces: Sequence[Fraction],
) -> list[Fraction]:
    coefficients = [Fraction(1)]
    for degree in range(1, len(traces) + 1):
        value = -sum(
            traces[power - 1] * coefficients[degree - power]
            for power in range(1, degree + 1)
        ) / degree
        coefficients.append(value)
    return coefficients


def polynomial_value(
    coefficients: Sequence[Fraction], value: Fraction
) -> Fraction:
    result = Fraction(0)
    for coefficient in reversed(coefficients):
        result = result * value + coefficient
    return result


def fraction_determinant(matrix: Sequence[Sequence[Fraction]]) -> Fraction:
    values = [list(row) for row in matrix]
    size = len(values)
    determinant = Fraction(1)
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if values[row][column]),
            None,
        )
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            values[column], values[pivot] = values[pivot], values[column]
            determinant = -determinant
        pivot_value = values[column][column]
        determinant *= pivot_value
        for row in range(column + 1, size):
            if values[row][column] == 0:
                continue
            factor = values[row][column] / pivot_value
            values[row][column] = Fraction(0)
            for inner_column in range(column + 1, size):
                values[row][inner_column] -= factor * values[column][inner_column]
    return determinant


def identity_minus_scaled(
    matrix: Sequence[Sequence[Fraction]], value: Fraction
) -> list[list[Fraction]]:
    size = len(matrix)
    return [
        [
            (Fraction(1) if row == column else Fraction(0))
            - value * matrix[row][column]
            for column in range(size)
        ]
        for row in range(size)
    ]


def complex_character_matrix(
    cutoff: int, s_integer: int, t: float
) -> list[list[complex]]:
    size = cutoff - 1
    matrix = [[0j for _ in range(size)] for _ in range(size)]
    for source in range(2, cutoff + 1):
        for target, quotient in edges_from(source, cutoff=cutoff):
            phase = complex(cos(-t * log(quotient)), sin(-t * log(quotient)))
            matrix[target - 2][source - 2] = (
                (source * target) ** (-s_integer) * phase
            )
    return matrix


def complex_source_gauge_matrix(
    cutoff: int, s_integer: int, t: float
) -> list[list[complex]]:
    size = cutoff - 1
    matrix = [[0j for _ in range(size)] for _ in range(size)]
    for source in range(2, cutoff + 1):
        source_phase = complex(
            cos(-t * log(1.0 + 1.0 / source)),
            sin(-t * log(1.0 + 1.0 / source)),
        )
        for target, _quotient in edges_from(source, cutoff=cutoff):
            matrix[target - 2][source - 2] = (
                (source * target) ** (-s_integer) * source_phase
            )
    return matrix


def diagonal_gauge_conjugate(
    matrix: Sequence[Sequence[complex]], t: float
) -> list[list[complex]]:
    size = len(matrix)
    output = [[0j for _ in range(size)] for _ in range(size)]
    for row in range(size):
        target = row + 2
        left = complex(cos(-t * log(target)), sin(-t * log(target)))
        for column in range(size):
            source = column + 2
            right = complex(cos(t * log(source)), sin(t * log(source)))
            output[row][column] = left * matrix[row][column] * right
    return output


def complex_determinant(matrix: Sequence[Sequence[complex]]) -> complex:
    values = [list(row) for row in matrix]
    size = len(values)
    determinant = 1.0 + 0.0j
    for column in range(size):
        pivot = max(range(column, size), key=lambda row: abs(values[row][column]))
        if abs(values[pivot][column]) < 1e-30:
            return 0j
        if pivot != column:
            values[column], values[pivot] = values[pivot], values[column]
            determinant = -determinant
        pivot_value = values[column][column]
        determinant *= pivot_value
        for row in range(column + 1, size):
            if values[row][column] == 0:
                continue
            factor = values[row][column] / pivot_value
            for inner_column in range(column + 1, size):
                values[row][inner_column] -= factor * values[column][inner_column]
            values[row][column] = 0j
    return determinant


def complex_identity_minus_scaled(
    matrix: Sequence[Sequence[complex]], value: complex
) -> list[list[complex]]:
    size = len(matrix)
    return [
        [
            (1.0 if row == column else 0.0) - value * matrix[row][column]
            for column in range(size)
        ]
        for row in range(size)
    ]


def factor_exponents(value: int) -> dict[int, int]:
    """Return the multiplicative-generator exponent dictionary."""

    if value < 1:
        raise ValueError("value must be positive")
    remainder = value
    factors: dict[int, int] = {}
    candidate = 2
    while candidate * candidate <= remainder:
        while remainder % candidate == 0:
            factors[candidate] = factors.get(candidate, 0) + 1
            remainder //= candidate
        candidate += 1
    if remainder > 1:
        factors[remainder] = factors.get(remainder, 0) + 1
    return factors


def character_fourier_reconstruction(
    coefficients: Mapping[int, Fraction],
) -> tuple[list[dict[str, object]], int]:
    """Reconstruct finite group coefficients on an alias-free character grid."""

    generators = sorted(
        {
            generator
            for label in coefficients
            for generator in factor_exponents(label)
        }
    )
    exponent_vectors = {
        label: tuple(factor_exponents(label).get(generator, 0) for generator in generators)
        for label in coefficients
    }
    moduli = tuple(
        2 + max(vector[index] for vector in exponent_vectors.values())
        for index in range(len(generators))
    )
    grid = tuple(product(*(range(modulus) for modulus in moduli))) if moduli else ((),)
    character_values: dict[tuple[int, ...], complex] = {}
    for coordinate in grid:
        value = 0j
        for label, coefficient in coefficients.items():
            vector = exponent_vectors[label]
            angle = 2.0 * pi * sum(
                vector[index] * coordinate[index] / moduli[index]
                for index in range(len(generators))
            )
            value += float(coefficient) * complex(cos(angle), sin(angle))
        character_values[coordinate] = value

    rows: list[dict[str, object]] = []
    for label, exact in coefficients.items():
        target = exponent_vectors[label]
        recovered = 0j
        for coordinate, value in character_values.items():
            angle = -2.0 * pi * sum(
                target[index] * coordinate[index] / moduli[index]
                for index in range(len(generators))
            )
            recovered += value * complex(cos(angle), sin(angle))
        recovered /= len(grid)
        rows.append(
            {
                "holonomy": label,
                "exact": str(exact),
                "recovered_real": format(recovered.real, ".17g"),
                "recovered_imag": format(recovered.imag, ".17g"),
                "absolute_error": format(abs(recovered - float(exact)), ".17g"),
                "generators": ",".join(map(str, generators)),
                "moduli": ",".join(map(str, moduli)),
                "grid_size": len(grid),
                "alias_free": True,
            }
        )
    return rows, len(grid)


def max_entry_difference(
    left: Sequence[Sequence[complex]], right: Sequence[Sequence[complex]]
) -> float:
    return max(
        (
            abs(left[row][column] - right[row][column])
            for row in range(len(left))
            for column in range(len(left))
        ),
        default=0.0,
    )


def fraction_fields(value: Fraction) -> dict[str, object]:
    return {
        "value": str(value),
        "numerator": value.numerator,
        "denominator": value.denominator,
    }


def word_text(word: Iterable[int]) -> str:
    return "-".join(map(str, word))
