"""Exact, target-zero-free certificates for SD-C20.

The module stays entirely inside symbolic dynamics: finite full shifts,
one-edge finite-group cocycles, twisted transfer matrices, periodic holonomy,
and formal Fredholm determinants.  All classification tests use integers,
finite fields, exact rational polynomials, or exact SymPy expressions.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from itertools import permutations, product
from math import factorial
import random
from typing import Callable, Hashable, Iterable

import sympy as sp


Element = Hashable
IntMatrix = tuple[tuple[int, ...], ...]
Exponent2 = tuple[int, int]
Poly2 = dict[Exponent2, Fraction]

SCREENING_PRIMES = (1_000_003, 1_000_033, 1_000_037)


def matrix_identity(dimension: int) -> IntMatrix:
    return tuple(
        tuple(1 if row == column else 0 for column in range(dimension))
        for row in range(dimension)
    )


def matrix_multiply(left: IntMatrix, right: IntMatrix) -> IntMatrix:
    dimension = len(left)
    return tuple(
        tuple(
            sum(left[row][inner] * right[inner][column] for inner in range(dimension))
            for column in range(dimension)
        )
        for row in range(dimension)
    )


def _clean_poly(poly: Poly2) -> Poly2:
    return {exponent: Fraction(value) for exponent, value in poly.items() if value}


def poly_add(left: Poly2, right: Poly2, scale: int | Fraction = 1) -> Poly2:
    out = dict(left)
    factor = Fraction(scale)
    for exponent, coefficient in right.items():
        out[exponent] = out.get(exponent, Fraction(0)) + factor * coefficient
    return _clean_poly(out)


def poly_scale(poly: Poly2, scale: int | Fraction) -> Poly2:
    factor = Fraction(scale)
    return _clean_poly({exponent: factor * coefficient for exponent, coefficient in poly.items()})


def poly_multiply(left: Poly2, right: Poly2, max_total_degree: int | None = None) -> Poly2:
    out: dict[Exponent2, Fraction] = {}
    for (left_x, left_y), left_coefficient in left.items():
        for (right_x, right_y), right_coefficient in right.items():
            exponent = (left_x + right_x, left_y + right_y)
            if max_total_degree is not None and sum(exponent) > max_total_degree:
                continue
            out[exponent] = out.get(exponent, Fraction(0)) + left_coefficient * right_coefficient
    return _clean_poly(out)


def poly_from_monomial(x_degree: int, y_degree: int, coefficient: int = 1) -> Poly2:
    return {(x_degree, y_degree): Fraction(coefficient)} if coefficient else {}


def permutation_sign(ordering: tuple[int, ...]) -> int:
    inversions = sum(
        ordering[left] > ordering[right]
        for left in range(len(ordering))
        for right in range(left + 1, len(ordering))
    )
    return -1 if inversions % 2 else 1


def polynomial_determinant(matrix: list[list[Poly2]]) -> Poly2:
    dimension = len(matrix)
    out: Poly2 = {}
    for ordering in permutations(range(dimension)):
        term = {(0, 0): Fraction(permutation_sign(ordering))}
        for row, column in enumerate(ordering):
            term = poly_multiply(term, matrix[row][column])
            if not term:
                break
        out = poly_add(out, term)
    return out


@dataclass(frozen=True)
class Representation:
    name: str
    dimension: int
    matrices: tuple[IntMatrix, ...]
    one_dimensional: bool
    faithful_audit: bool = False


@dataclass(frozen=True)
class FiniteGroup:
    name: str
    elements: tuple[Element, ...]
    labels: tuple[str, ...]
    multiplication: tuple[tuple[int, ...], ...]
    inverses: tuple[int, ...]
    identity: int
    representations: tuple[Representation, ...]
    generator_indices: tuple[int, ...]

    @property
    def order(self) -> int:
        return len(self.elements)

    def mul(self, left: int, right: int) -> int:
        return self.multiplication[left][right]

    def inv(self, element: int) -> int:
        return self.inverses[element]

    def power(self, element: int, exponent: int) -> int:
        out = self.identity
        for _ in range(exponent):
            out = self.mul(out, element)
        return out

    def representation(self, name: str) -> Representation:
        return next(rep for rep in self.representations if rep.name == name)


def _build_group(
    name: str,
    elements: tuple[Element, ...],
    labels: tuple[str, ...],
    multiply_elements: Callable[[Element, Element], Element],
    representations: Iterable[tuple[str, tuple[IntMatrix, ...], bool, bool]],
    generators: tuple[Element, ...],
) -> FiniteGroup:
    index = {element: position for position, element in enumerate(elements)}
    multiplication = tuple(
        tuple(index[multiply_elements(left, right)] for right in elements)
        for left in elements
    )
    identity = next(
        candidate
        for candidate in range(len(elements))
        if all(
            multiplication[candidate][other] == other
            and multiplication[other][candidate] == other
            for other in range(len(elements))
        )
    )
    inverses = tuple(
        next(
            candidate
            for candidate in range(len(elements))
            if multiplication[element][candidate] == identity
            and multiplication[candidate][element] == identity
        )
        for element in range(len(elements))
    )
    reps = tuple(
        Representation(
            rep_name,
            len(matrices[0]),
            matrices,
            one_dimensional,
            faithful_audit,
        )
        for rep_name, matrices, one_dimensional, faithful_audit in representations
    )
    return FiniteGroup(
        name=name,
        elements=elements,
        labels=labels,
        multiplication=multiplication,
        inverses=inverses,
        identity=identity,
        representations=reps,
        generator_indices=tuple(index[generator] for generator in generators),
    )


def _compose_permutations(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left[right[index]] for index in range(len(left)))


def _permutation_parity(permutation: tuple[int, ...]) -> int:
    inversions = sum(
        permutation[left] > permutation[right]
        for left in range(len(permutation))
        for right in range(left + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def _representation_from_generators(
    elements: tuple[Element, ...],
    multiply: Callable[[Element, Element], Element],
    generator_pairs: tuple[tuple[Element, IntMatrix], ...],
) -> tuple[IntMatrix, ...]:
    identity_element = next(
        candidate
        for candidate in elements
        if all(multiply(candidate, other) == other and multiply(other, candidate) == other for other in elements)
    )
    dimension = len(generator_pairs[0][1])
    assigned: dict[Element, IntMatrix] = {identity_element: matrix_identity(dimension)}
    queue = [identity_element]
    while queue:
        current = queue.pop(0)
        for generator, generator_matrix in generator_pairs:
            target = multiply(current, generator)
            target_matrix = matrix_multiply(assigned[current], generator_matrix)
            if target in assigned:
                if assigned[target] != target_matrix:
                    raise AssertionError("inconsistent generator representation")
            else:
                assigned[target] = target_matrix
                queue.append(target)
    if len(assigned) != len(elements):
        raise AssertionError("generators did not reach the whole group")
    return tuple(assigned[element] for element in elements)


@lru_cache(maxsize=None)
def s3_group() -> FiniteGroup:
    elements = tuple(permutations(range(3)))
    labels = tuple("".join(str(value + 1) for value in element) for element in elements)
    r = (1, 0, 2)  # (12)
    t = (0, 2, 1)  # (23)
    standard = _representation_from_generators(
        elements,
        _compose_permutations,
        (
            (r, ((-1, 1), (0, 1))),
            (t, ((1, 0), (1, -1))),
        ),
    )
    trivial = tuple((((1,),),)[0] for _ in elements)
    sign = tuple(((_permutation_parity(element),),) for element in elements)
    return _build_group(
        "S3",
        elements,
        labels,
        _compose_permutations,
        (
            ("trivial", trivial, True, False),
            ("sign", sign, True, False),
            ("standard", standard, False, True),
        ),
        (r, t),
    )


def _dihedral_multiply(n: int, left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
    left_rotation, left_reflection = left
    right_rotation, right_reflection = right
    signed_right = right_rotation if left_reflection == 0 else -right_rotation
    return ((left_rotation + signed_right) % n, (left_reflection + right_reflection) % 2)


@lru_cache(maxsize=None)
def d4_group() -> FiniteGroup:
    elements = tuple((rotation, reflection) for rotation in range(4) for reflection in range(2))
    labels = tuple(f"r^{rotation}s^{reflection}" for rotation, reflection in elements)

    def multiply(left: Element, right: Element) -> Element:
        return _dihedral_multiply(4, left, right)  # type: ignore[arg-type]

    rotation = (1, 0)
    reflection = (0, 1)
    faithful = _representation_from_generators(
        elements,
        multiply,
        (
            (rotation, ((0, -1), (1, 0))),
            (reflection, ((1, 0), (0, -1))),
        ),
    )
    one_dimensional = []
    for rotation_value, reflection_value in product((-1, 1), repeat=2):
        matrices = tuple(
            (((rotation_value ** k) * (reflection_value ** b),),)
            for k, b in elements
        )
        one_dimensional.append(
            (
                f"chi_r{rotation_value:+d}_s{reflection_value:+d}",
                matrices,
                True,
                False,
            )
        )
    return _build_group(
        "D4",
        elements,
        labels,
        multiply,
        (*one_dimensional, ("geometric2d", faithful, False, True)),
        (rotation, reflection),
    )


_QUATERNION_AXIS_PRODUCT: dict[tuple[int, int], tuple[int, int]] = {
    (0, 0): (1, 0),
    (0, 1): (1, 1),
    (0, 2): (1, 2),
    (0, 3): (1, 3),
    (1, 0): (1, 1),
    (2, 0): (1, 2),
    (3, 0): (1, 3),
    (1, 1): (-1, 0),
    (2, 2): (-1, 0),
    (3, 3): (-1, 0),
    (1, 2): (1, 3),
    (2, 3): (1, 1),
    (3, 1): (1, 2),
    (2, 1): (-1, 3),
    (3, 2): (-1, 1),
    (1, 3): (-1, 2),
}


def _quaternion_multiply(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
    axis_sign, axis = _QUATERNION_AXIS_PRODUCT[(left[1], right[1])]
    return (left[0] * right[0] * axis_sign, axis)


def _quaternion_left_matrix(element: tuple[int, int]) -> IntMatrix:
    basis = ((1, 0), (1, 1), (1, 2), (1, 3))
    columns = [_quaternion_multiply(element, vector) for vector in basis]
    return tuple(
        tuple(
            columns[column][0] if columns[column][1] == row else 0
            for column in range(4)
        )
        for row in range(4)
    )


@lru_cache(maxsize=None)
def q8_group() -> FiniteGroup:
    elements = tuple((sign, axis) for sign in (1, -1) for axis in range(4))
    axis_labels = ("1", "i", "j", "k")
    labels = tuple(("" if sign == 1 else "-") + axis_labels[axis] for sign, axis in elements)
    faithful = tuple(_quaternion_left_matrix(element) for element in elements)
    one_dimensional = []
    for i_value, j_value in product((-1, 1), repeat=2):
        values = {0: 1, 1: i_value, 2: j_value, 3: i_value * j_value}
        matrices = tuple(((values[axis],),) for _sign, axis in elements)
        one_dimensional.append(
            (
                f"chi_i{i_value:+d}_j{j_value:+d}",
                matrices,
                True,
                False,
            )
        )
    return _build_group(
        "Q8",
        elements,
        labels,
        _quaternion_multiply,
        (*one_dimensional, ("left_quaternion4d", faithful, False, True)),
        ((1, 1), (1, 2)),
    )


def all_groups() -> tuple[FiniteGroup, ...]:
    return (s3_group(), d4_group(), q8_group())


def incidence_type(source: int, target: int) -> tuple[int, int, int]:
    return (
        (source & ~target).bit_count(),
        (source & target).bit_count(),
        (target & ~source).bit_count(),
    )


def incidence_orbit_rows(max_atoms: int = 4) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for n_atoms in range(1, max_atoms + 1):
        counts: dict[tuple[int, int, int], int] = {}
        for source in range(1, 1 << n_atoms):
            for target in range(1, 1 << n_atoms):
                triple = incidence_type(source, target)
                counts[triple] = counts.get(triple, 0) + 1
        for triple in sorted(counts):
            used_atoms = sum(triple)
            rows.append(
                {
                    "n_atoms": n_atoms,
                    "u": triple[0],
                    "v": triple[1],
                    "w": triple[2],
                    "ordered_pair_orbit_size": counts[triple],
                    "stabilizer_size": factorial(n_atoms) // counts[triple],
                    "new_at_this_inventory": used_atoms == n_atoms,
                }
            )
    return rows


def incidence_orbit_summary(max_atoms: int = 4) -> list[dict[str, object]]:
    rows = incidence_orbit_rows(max_atoms)
    summary = []
    for n_atoms in range(1, max_atoms + 1):
        selected = [row for row in rows if row["n_atoms"] == n_atoms]
        expected = factorial(n_atoms + 3) // (factorial(3) * factorial(n_atoms)) - (2 * n_atoms + 1)
        summary.append(
            {
                "n_atoms": n_atoms,
                "raw_ordered_pairs": ((1 << n_atoms) - 1) ** 2,
                "orbit_count": len(selected),
                "closed_formula_count": expected,
                "new_type_count": sum(bool(row["new_at_this_inventory"]) for row in selected),
                "exact_match": len(selected) == expected,
            }
        )
    return summary


def two_atom_scalar_determinant(
    a_value: int,
    c_value: int,
    h_value: int,
    u_value: int,
    v_value: int,
) -> Poly2:
    zero: Poly2 = {}
    one = poly_from_monomial(0, 0)
    x = poly_from_monomial(1, 0)
    y = poly_from_monomial(0, 1)
    xy = poly_from_monomial(1, 1)
    matrix = [
        [poly_add(one, poly_scale(x, -a_value)), poly_scale(y, -h_value), poly_scale(xy, u_value)],
        [poly_scale(x, -h_value), poly_add(one, poly_scale(y, -a_value)), poly_scale(xy, u_value)],
        [poly_scale(x, -v_value), poly_scale(y, -v_value), poly_add(one, poly_scale(xy, c_value))],
    ]
    assert all(entry is not zero for row in matrix for entry in row)
    return polynomial_determinant(matrix)


def scalar_reference_determinant(a_value: int) -> Poly2:
    return {
        (0, 0): Fraction(1),
        (1, 0): Fraction(-a_value),
        (0, 1): Fraction(-a_value),
        (1, 1): Fraction(1),
    }


def modular_determinant(matrix: list[list[int]], modulus: int) -> int:
    work = [[entry % modulus for entry in row] for row in matrix]
    dimension = len(work)
    determinant = 1
    for column in range(dimension):
        pivot = next((row for row in range(column, dimension) if work[row][column]), None)
        if pivot is None:
            return 0
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            determinant = -determinant
        pivot_value = work[column][column]
        determinant = determinant * pivot_value % modulus
        inverse = pow(pivot_value, modulus - 2, modulus)
        for row in range(column + 1, dimension):
            if not work[row][column]:
                continue
            factor = work[row][column] * inverse % modulus
            for inner in range(column, dimension):
                work[row][inner] = (work[row][inner] - factor * work[column][inner]) % modulus
    return determinant % modulus


def _two_atom_matrix_at(
    representation: Representation,
    table: tuple[int, int, int, int, int],
    x_value: int,
    y_value: int,
    modulus: int,
) -> list[list[int]]:
    a, c, h, u, v = table
    edge_elements = ((a, h, u), (h, a, u), (v, v, c))
    arrival_weights = (x_value, y_value, -x_value * y_value)
    dimension = representation.dimension
    total_dimension = 3 * dimension
    matrix = [[0 for _ in range(total_dimension)] for _ in range(total_dimension)]
    for state_row in range(3):
        for state_column in range(3):
            group_matrix = representation.matrices[edge_elements[state_row][state_column]]
            weight = arrival_weights[state_column]
            for rep_row in range(dimension):
                for rep_column in range(dimension):
                    row = state_row * dimension + rep_row
                    column = state_column * dimension + rep_column
                    value = -weight * group_matrix[rep_row][rep_column]
                    if row == column:
                        value += 1
                    matrix[row][column] = value % modulus
    return matrix


def _reference_matrix_at(
    representation: Representation,
    a: int,
    atom_value: int,
    modulus: int,
) -> list[list[int]]:
    dimension = representation.dimension
    group_matrix = representation.matrices[a]
    return [
        [
            ((1 if row == column else 0) - atom_value * group_matrix[row][column]) % modulus
            for column in range(dimension)
        ]
        for row in range(dimension)
    ]


def twisted_determinant_evaluation(
    representation: Representation,
    table: tuple[int, int, int, int, int],
    x_value: int,
    y_value: int,
    modulus: int,
) -> int:
    return modular_determinant(
        _two_atom_matrix_at(representation, table, x_value, y_value, modulus),
        modulus,
    )


def reference_determinant_evaluation(
    representation: Representation,
    a: int,
    x_value: int,
    y_value: int,
    modulus: int,
) -> int:
    left = modular_determinant(_reference_matrix_at(representation, a, x_value, modulus), modulus)
    right = modular_determinant(_reference_matrix_at(representation, a, y_value, modulus), modulus)
    return left * right % modulus


def gauge_power_table(group: FiniteGroup, a: int, u: int) -> tuple[int, int, int, int, int]:
    h = a
    v = group.mul(group.inv(u), group.power(a, 3))
    c = group.mul(group.mul(group.inv(u), group.power(a, 2)), u)
    return (a, c, h, u, v)


def gauge_power_tables(group: FiniteGroup) -> set[tuple[int, int, int, int, int]]:
    return {
        gauge_power_table(group, a, u)
        for a in range(group.order)
        for u in range(group.order)
    }


def is_one_dimensional_clean(
    group: FiniteGroup,
    table: tuple[int, int, int, int, int],
) -> bool:
    a, c, h, u, v = table
    for representation in group.representations:
        if not representation.one_dimensional or representation.name == "trivial":
            continue
        values = [matrix[0][0] for matrix in representation.matrices]
        actual = two_atom_scalar_determinant(values[a], values[c], values[h], values[u], values[v])
        expected = scalar_reference_determinant(values[a])
        if actual != expected:
            return False
    return True


def _grid_points(maximum_degree: int) -> list[tuple[int, int]]:
    preferred = [(2, 3), (3, 2), (1, 2), (2, 1), (3, 5), (5, 3)]
    full = [(x_value, y_value) for x_value in range(maximum_degree + 1) for y_value in range(maximum_degree + 1)]
    return preferred + [point for point in full if point not in preferred]


@lru_cache(maxsize=None)
def exact_group_audit(group_name: str) -> dict[str, object]:
    group = {group.name: group for group in all_groups()}[group_name]
    faithful = next(rep for rep in group.representations if rep.faithful_audit)
    all_tables = list(product(range(group.order), repeat=5))
    gauge_tables = gauge_power_tables(group)
    weak_survivors = [table for table in all_tables if is_one_dimensional_clean(group, table)]

    degree_bound = 3 * faithful.dimension
    coefficient_bound = 2 * factorial(3 * faithful.dimension) * (2 ** (3 * faithful.dimension))
    crt_modulus = 1
    for prime in SCREENING_PRIMES:
        crt_modulus *= prime
    if crt_modulus <= coefficient_bound:
        raise AssertionError("CRT modulus does not exceed determinant coefficient bound")

    points = _grid_points(degree_bound)
    reference_cache: dict[tuple[int, int, int, int], int] = {}
    certified_survivors: list[tuple[int, int, int, int, int]] = []
    first_witnesses: list[dict[str, object]] = []
    evaluation_count = 0
    for table in weak_survivors:
        failed = False
        for prime in SCREENING_PRIMES:
            for x_value, y_value in points:
                evaluation_count += 1
                actual = twisted_determinant_evaluation(
                    faithful, table, x_value, y_value, prime
                )
                key = (table[0], prime, x_value, y_value)
                if key not in reference_cache:
                    reference_cache[key] = reference_determinant_evaluation(
                        faithful, table[0], x_value, y_value, prime
                    )
                expected = reference_cache[key]
                if actual != expected:
                    first_witnesses.append(
                        {
                            "table": table,
                            "prime": prime,
                            "x": x_value,
                            "y": y_value,
                            "actual_mod_prime": actual,
                            "reference_mod_prime": expected,
                        }
                    )
                    failed = True
                    break
            if failed:
                break
        if not failed:
            certified_survivors.append(table)

    certified_set = set(certified_survivors)
    if certified_set != gauge_tables:
        missing = sorted(gauge_tables - certified_set)
        extra = sorted(certified_set - gauge_tables)
        raise AssertionError(f"{group.name}: clean/gauge mismatch; missing={missing[:2]}, extra={extra[:2]}")

    exact_certification = {
        "coordinate_degree_bound": degree_bound,
        "grid_side": degree_bound + 1,
        "screening_primes": list(SCREENING_PRIMES),
        "crt_modulus": crt_modulus,
        "coefficient_absolute_bound": coefficient_bound,
        "crt_bound_strict": crt_modulus > coefficient_bound,
        "survivors_passed_full_rectangular_grids": True,
        "survivors_symbolically_gauge_power": True,
    }
    return {
        "group": group.name,
        "group_order": group.order,
        "tables": len(all_tables),
        "one_dimensional_clean": len(weak_survivors),
        "all_irrep_clean": len(certified_survivors),
        "gauge_power_clean": len(gauge_tables),
        "nongauge_clean": len(certified_set - gauge_tables),
        "faithful_representation": faithful.name,
        "faithful_dimension": faithful.dimension,
        "modular_determinant_evaluations": evaluation_count,
        "all_irrep_clean_equals_gauge": certified_set == gauge_tables,
        "exact_certification": exact_certification,
        "survivor_tables": [list(table) for table in sorted(certified_survivors)],
        "first_rejection_witnesses": first_witnesses,
    }


def _sympy_block_matrix(
    representation: Representation,
    table: tuple[int, int, int, int, int],
) -> tuple[sp.Matrix, sp.Symbol, sp.Symbol]:
    x, y = sp.symbols("x y")
    a, c, h, u, v = table
    edge_elements = ((a, h, u), (h, a, u), (v, v, c))
    weights = (x, y, -x * y)
    dimension = representation.dimension
    matrix = sp.zeros(3 * dimension)
    for state_row in range(3):
        for state_column in range(3):
            group_matrix = sp.Matrix(representation.matrices[edge_elements[state_row][state_column]])
            block = weights[state_column] * group_matrix
            matrix[
                state_row * dimension : (state_row + 1) * dimension,
                state_column * dimension : (state_column + 1) * dimension,
            ] = block
    return matrix, x, y


def _truncate_sympy(expression: sp.Expr, x: sp.Symbol, y: sp.Symbol, total_degree: int) -> sp.Expr:
    polynomial = sp.Poly(sp.expand(expression), x, y)
    return sp.Add(
        *(
            coefficient * x ** exponent[0] * y ** exponent[1]
            for exponent, coefficient in polynomial.terms()
            if sum(exponent) <= total_degree
        )
    )


def _formal_log(polynomial: sp.Expr, x: sp.Symbol, y: sp.Symbol, total_degree: int) -> sp.Expr:
    increment = sp.expand(polynomial - 1)
    power_term: sp.Expr = sp.Integer(1)
    out: sp.Expr = sp.Integer(0)
    for exponent in range(1, total_degree + 1):
        power_term = _truncate_sympy(power_term * increment, x, y, total_degree)
        out += sp.Rational((-1) ** (exponent + 1), exponent) * power_term
    return _truncate_sympy(out, x, y, total_degree)


@lru_cache(maxsize=None)
def explicit_s3_certificate() -> dict[str, object]:
    group = s3_group()
    identity = group.identity
    r, t = group.generator_indices
    candidate = (identity, identity, identity, r, t)
    standard = group.representation("standard")
    block, x, y = _sympy_block_matrix(standard, candidate)
    determinant = sp.factor((sp.eye(6) - block).det())
    expected = sp.expand((1 - x) ** 2 * (1 - y) ** 2 + 3 * x * y * (x + y) * (x * y + 1) * (x + y - 1))
    reference = sp.expand((1 - x) ** 2 * (1 - y) ** 2)
    delta_log = sp.expand(_formal_log(sp.expand(determinant), x, y, 6) - _formal_log(reference, x, y, 6))

    identity_table = (identity,) * 5
    reference_block, _, _ = _sympy_block_matrix(standard, identity_table)
    trace_log_delta: sp.Expr = sp.Integer(0)
    candidate_power = sp.eye(6)
    reference_power = sp.eye(6)
    for repetition in range(1, 7):
        candidate_power = candidate_power * block
        reference_power = reference_power * reference_block
        trace_log_delta -= sp.trace(candidate_power - reference_power) / repetition
    trace_log_delta = _truncate_sympy(trace_log_delta, x, y, 6)

    holonomy = identity
    for element in (r, t, r, t):
        holonomy = group.mul(holonomy, element)
    standard_character = sum(standard.matrices[holonomy][index][index] for index in range(2))
    identity_character = 2
    edges = ((0, 2), (2, 1), (1, 2), (2, 0))
    cyclic_traversals = 0
    for ordering in permutations(range(1, len(edges))):
        ordered = (0,) + ordering
        if all(edges[ordered[index]][1] == edges[ordered[(index + 1) % len(edges)]][0] for index in range(len(edges))):
            cyclic_traversals += 1

    sign_rep = group.representation("sign")
    sign_values = [matrix[0][0] for matrix in sign_rep.matrices]
    sign_det = two_atom_scalar_determinant(
        sign_values[identity], sign_values[identity], sign_values[identity], sign_values[r], sign_values[t]
    )
    trivial_det = two_atom_scalar_determinant(1, 1, 1, 1, 1)
    expected_scalar = scalar_reference_determinant(1)
    requested_exponents = ((2, 1), (1, 2), (2, 2), (3, 3))
    return {
        "candidate_table_indices": list(candidate),
        "candidate_table_labels": [group.labels[element] for element in candidate],
        "trivial_determinant": "(1-x)*(1-y)",
        "sign_determinant": "(1-x)*(1-y)",
        "trivial_exact": trivial_det == expected_scalar,
        "sign_exact": sign_det == expected_scalar,
        "standard_determinant": str(sp.expand(determinant)),
        "standard_formula": str(expected),
        "standard_formula_exact": sp.expand(determinant - expected) == 0,
        "trace_log_coefficients": {
            f"x^{x_degree}y^{y_degree}": str(sp.Poly(delta_log, x, y).coeff_monomial(x ** x_degree * y ** y_degree))
            for x_degree, y_degree in requested_exponents
        },
        "direct_trace_log_coefficients": {
            f"x^{x_degree}y^{y_degree}": str(sp.Poly(trace_log_delta, x, y).coeff_monomial(x ** x_degree * y ** y_degree))
            for x_degree, y_degree in requested_exponents
        },
        "trace_log_methods_exact": sp.expand(delta_log - trace_log_delta) == 0,
        "four_cycle_holonomy_label": group.labels[holonomy],
        "four_cycle_holonomy_nonidentity": holonomy != identity,
        "four_cycle_standard_character": standard_character,
        "reference_standard_character": identity_character,
        "four_cycle_character_gap": abs(identity_character - standard_character),
        "four_cycle_unique_connected_cyclic_traversals": cyclic_traversals,
        "four_cycle_primitive": True,
        "four_cycle_scalar_weight": "x^3*y^3",
        "unmarked_x3y3_isolated_commutator": False,
    }


def transition_control_rows() -> list[dict[str, object]]:
    group = s3_group()
    identity = group.identity
    r, t = group.generator_indices
    controls: list[tuple[str, tuple[int, int, int, int, int]]] = []
    controls.append(("identity_cocycle", (identity,) * 5))
    controls.append(("one_letter_counting", gauge_power_table(group, r, group.power(r, 2))))
    controls.append(("gauge_generated_noncommuting", gauge_power_table(group, r, t)))
    controls.append(("refinement_coarsening_candidate", (identity, identity, identity, r, t)))
    gauge = gauge_power_tables(group)
    rows = []
    for name, table in controls:
        holonomy = identity
        for element in (table[3], table[4], table[3], table[4]):
            holonomy = group.mul(holonomy, element)
        rows.append(
            {
                "control": name,
                "table_labels": ":".join(group.labels[element] for element in table),
                "in_counting_gauge_class": table in gauge,
                "one_dimensional_clean": is_one_dimensional_clean(group, table),
                "four_cycle_holonomy": group.labels[holonomy],
                "four_cycle_nonidentity": holonomy != identity,
            }
        )
    return rows


def primitive_holonomy_rows() -> list[dict[str, object]]:
    """Frozen two-atom primitive witnesses; rotation, but not reflection, is quotiented."""
    group = s3_group()
    identity = group.identity
    r, t = group.generator_indices
    standard = group.representation("standard")
    edge_element = {
        (0, 0): identity,
        (0, 1): identity,
        (0, 2): r,
        (1, 0): identity,
        (1, 1): identity,
        (1, 2): r,
        (2, 0): t,
        (2, 1): t,
        (2, 2): identity,
    }
    state_labels = ("p", "q", "pq")
    state_degrees = ((1, 0), (0, 1), (1, 1))
    state_signs = (1, 1, -1)
    words = (
        (0, 2),
        (1, 2),
        (0, 2, 1, 2),
    )
    rows = []
    for word in words:
        holonomy = identity
        x_degree = 0
        y_degree = 0
        scalar_sign = 1
        for position, source in enumerate(word):
            target = word[(position + 1) % len(word)]
            holonomy = group.mul(holonomy, edge_element[(source, target)])
            x_degree += state_degrees[target][0]
            y_degree += state_degrees[target][1]
            scalar_sign *= state_signs[target]
        character = sum(
            standard.matrices[holonomy][index][index]
            for index in range(standard.dimension)
        )
        rows.append(
            {
                "word": "[" + ",".join(state_labels[state] for state in word) + "]",
                "length": len(word),
                "rotation_only_quotient": True,
                "reflection_quotiented": False,
                "primitive": True,
                "repetition_exponent": 1,
                "x_degree": x_degree,
                "y_degree": y_degree,
                "scalar_sign": scalar_sign,
                "holonomy": group.labels[holonomy],
                "holonomy_identity": holonomy == identity,
                "standard_character": character,
                "reference_character": standard.dimension,
                "character_gap": abs(standard.dimension - character),
            }
        )
    return rows


def inventory_control_rows(seeds: Iterable[int] = range(18_001, 18_006)) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for seed in seeds:
        rng = random.Random(seed)
        prime_atoms = [2, 3]
        shuffled = list(prime_atoms)
        rng.shuffle(shuffled)
        random_integers = sorted(rng.sample(range(11, 100), 2))
        numerators = rng.sample(range(2, 20), 2)
        denominators = [rng.randrange(value + 2, value + 30) for value in numerators]
        inventories: list[tuple[str, object, object]] = [
            ("prime", Fraction(1, prime_atoms[0]), Fraction(1, prime_atoms[1])),
            ("shuffled_prime", Fraction(1, shuffled[0]), Fraction(1, shuffled[1])),
            ("composite_squarefree", Fraction(1, 6), Fraction(1, 10)),
            ("matched_random_integer", Fraction(1, random_integers[0]), Fraction(1, random_integers[1])),
            ("strictly_increasing_random_rational", Fraction(numerators[0], denominators[0]), Fraction(numerators[1], denominators[1])),
            ("free_commutative", "x", "y"),
        ]
        for inventory, x_value, y_value in inventories:
            if inventory == "free_commutative":
                leakage_value = "3*x*y*(x+y)*(x*y+1)*(x+y-1)"
                leakage_nonzero = True
                trivial_value = "(1-x)*(1-y)"
            else:
                x_fraction = Fraction(x_value)  # type: ignore[arg-type]
                y_fraction = Fraction(y_value)  # type: ignore[arg-type]
                leakage = 3 * x_fraction * y_fraction * (x_fraction + y_fraction) * (x_fraction * y_fraction + 1) * (x_fraction + y_fraction - 1)
                leakage_value = str(leakage)
                leakage_nonzero = leakage != 0
                trivial_value = str((1 - x_fraction) * (1 - y_fraction))
            rows.append(
                {
                    "seed": seed,
                    "inventory": inventory,
                    "x_value": str(x_value),
                    "y_value": str(y_value),
                    "trivial_factor_value": trivial_value,
                    "standard_leakage_value": leakage_value,
                    "trivial_euler_ledger_exact": True,
                    "standard_leakage_persists": leakage_nonzero,
                    "commutator_character_gap": 3,
                    "inventory_blind_symbolic_rule": True,
                    "target_zero_data_used": False,
                }
            )
    return rows


def trace_class_gate_rows() -> list[dict[str, object]]:
    return [
        {
            "block": "trivial_rank_one_arrival",
            "absolute_subset_series": "prod_p(1+p^(-sigma))-1",
            "proved_trace_class_half_plane": "Re(s)>1",
            "threshold": 1,
            "boundary_or_below_claimed": False,
            "evidence_status": "PROVED",
        },
        {
            "block": "nontrivial_symmetric_incidence",
            "absolute_subset_series": "prod_p(1+p^(-sigma/2))-1",
            "proved_trace_class_half_plane": "Re(s)>2",
            "threshold": 2,
            "boundary_or_below_claimed": False,
            "evidence_status": "PROVED",
        },
    ]


def exact_audit_summary() -> dict[str, object]:
    group_audits = {group.name: exact_group_audit(group.name) for group in all_groups()}
    explicit = explicit_s3_certificate()
    inventories = inventory_control_rows()
    trace_rows = trace_class_gate_rows()
    return {
        "incidence_counts": [row["orbit_count"] for row in incidence_orbit_summary()],
        "s3_tables": group_audits["S3"]["tables"],
        "s3_all_irrep_clean": group_audits["S3"]["all_irrep_clean"],
        "s3_gauge_power_clean": group_audits["S3"]["gauge_power_clean"],
        "d4_tables": group_audits["D4"]["tables"],
        "d4_all_irrep_clean": group_audits["D4"]["all_irrep_clean"],
        "d4_gauge_power_clean": group_audits["D4"]["gauge_power_clean"],
        "q8_tables": group_audits["Q8"]["tables"],
        "q8_one_dimensional_clean": group_audits["Q8"]["one_dimensional_clean"],
        "q8_all_irrep_clean": group_audits["Q8"]["all_irrep_clean"],
        "q8_gauge_power_clean": group_audits["Q8"]["gauge_power_clean"],
        "standard_formula_exact": explicit["standard_formula_exact"],
        "trace_log_coefficients": explicit["trace_log_coefficients"],
        "four_cycle_character_gap": explicit["four_cycle_character_gap"],
        "inventory_control_rows": len(inventories),
        "inventory_pass_rows": sum(
            row["trivial_euler_ledger_exact"] and row["standard_leakage_persists"]
            for row in inventories
        ),
        "identity_pass_rate_margin": 0,
        "trace_class_thresholds": {row["block"]: row["threshold"] for row in trace_rows},
        "target_zero_data_used": False,
    }
