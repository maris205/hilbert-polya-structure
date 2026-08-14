#!/usr/bin/env python3
"""Exact source-global coherence core for SD-C32.

The candidate selects atoms only as bottom covers.  Numeric roof marks are
transported decorations used after selection.  Claim-bearing values are
Fractions or formal rational-times-square-root ledgers.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, permutations, product
import math
import random
from typing import Iterable, Sequence


Matrix = tuple[tuple[Fraction, ...], ...]
Relation = tuple[tuple[bool, ...], ...]
PREDICATES = ("UJ", "BI", "MU", "RM", "TA")


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def fraction_record(value: Fraction) -> dict[str, int | str]:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "text": fraction_text(value),
    }


def identity_matrix(size: int) -> Matrix:
    return tuple(
        tuple(Fraction(int(i == j)) for j in range(size)) for i in range(size)
    )


def zero_matrix(size: int) -> Matrix:
    return tuple(tuple(Fraction(0) for _ in range(size)) for _ in range(size))


def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
    size = len(left)
    return tuple(
        tuple(
            sum((left[i][k] * right[k][j] for k in range(size)), Fraction(0))
            for j in range(size)
        )
        for i in range(size)
    )


def matrix_inverse(matrix: Matrix) -> Matrix:
    size = len(matrix)
    aug = [
        list(matrix[i])
        + [Fraction(int(i == j)) for j in range(size)]
        for i in range(size)
    ]
    for column in range(size):
        pivot = next((row for row in range(column, size) if aug[row][column]), None)
        if pivot is None:
            raise ValueError("singular incidence matrix")
        if pivot != column:
            aug[column], aug[pivot] = aug[pivot], aug[column]
        scale = aug[column][column]
        aug[column] = [value / scale for value in aug[column]]
        for row in range(size):
            if row == column or not aug[row][column]:
                continue
            coefficient = aug[row][column]
            aug[row] = [
                aug[row][j] - coefficient * aug[column][j]
                for j in range(2 * size)
            ]
    return tuple(tuple(row[size:]) for row in aug)


def outer(left: Sequence[Fraction], right: Sequence[Fraction]) -> Matrix:
    return tuple(tuple(x * y for y in right) for x in left)


def weighted_sharp(matrix: Matrix, weights: Sequence[Fraction]) -> Matrix:
    size = len(matrix)
    return tuple(
        tuple(matrix[j][i] * weights[j] / weights[i] for j in range(size))
        for i in range(size)
    )


def matrix_trace(matrix: Matrix) -> Fraction:
    return sum((matrix[i][i] for i in range(len(matrix))), Fraction(0))


def native_gram(left: Matrix, right: Matrix, weights: Sequence[Fraction]) -> Fraction:
    return matrix_trace(matrix_multiply(left, weighted_sharp(right, weights)))


def transitive_closure(size: int, edges: Iterable[tuple[int, int]]) -> Relation:
    relation = [[False] * size for _ in range(size)]
    for index in range(size):
        relation[index][index] = True
    for left, right in edges:
        if left != right:
            relation[left][right] = True
    for middle in range(size):
        for left in range(size):
            if relation[left][middle]:
                for right in range(size):
                    if relation[middle][right]:
                        relation[left][right] = True
    if any(
        relation[i][j] and relation[j][i]
        for i in range(size)
        for j in range(size)
        if i != j
    ):
        raise ValueError("directed cycle")
    return tuple(tuple(row) for row in relation)


def hasse_edges(relation: Relation) -> tuple[tuple[int, int], ...]:
    size = len(relation)
    rows = []
    for left in range(size):
        for right in range(size):
            if left == right or not relation[left][right]:
                continue
            if not any(
                middle not in (left, right)
                and relation[left][middle]
                and relation[middle][right]
                for middle in range(size)
            ):
                rows.append((left, right))
    return tuple(rows)


@dataclass(frozen=True)
class PosetData:
    name: str
    object_names: tuple[str, ...]
    roof_weights: tuple[int, ...]
    relation: Relation
    bottom: int = 0
    eta: int = 2

    def __post_init__(self) -> None:
        size = len(self.object_names)
        if size != len(self.roof_weights) or size != len(self.relation):
            raise ValueError("dimension mismatch")
        if any(len(row) != size for row in self.relation):
            raise ValueError("relation not square")
        if not all(self.relation[i][i] for i in range(size)):
            raise ValueError("not reflexive")
        if not all(self.relation[self.bottom][i] for i in range(size)):
            raise ValueError("bottom not least")
        for i in range(size):
            for j in range(size):
                if i != j and self.relation[i][j] and self.relation[j][i]:
                    raise ValueError("not antisymmetric")
                for k in range(size):
                    if self.relation[i][j] and self.relation[j][k] and not self.relation[i][k]:
                        raise ValueError("not transitive")

    @property
    def size(self) -> int:
        return len(self.object_names)

    @property
    def metric_weights(self) -> tuple[Fraction, ...]:
        return tuple(Fraction(value ** (2 * self.eta)) for value in self.roof_weights)

    def atoms(self) -> tuple[int, ...]:
        result = []
        for right in range(self.size):
            if right == self.bottom or not self.relation[self.bottom][right]:
                continue
            if not any(
                middle not in (self.bottom, right)
                and self.relation[self.bottom][middle]
                and self.relation[middle][right]
                for middle in range(self.size)
            ):
                result.append(right)
        return tuple(result)

    def compile(self) -> tuple[Matrix, Matrix, tuple[Matrix, ...]]:
        zeta = tuple(
            tuple(Fraction(int(value)) for value in row) for row in self.relation
        )
        mobius = matrix_inverse(zeta)
        projectors = []
        for index in range(self.size):
            column = tuple(zeta[row][index] for row in range(self.size))
            row = tuple(mobius[index][column] for column in range(self.size))
            projectors.append(outer(column, row))
        return zeta, mobius, tuple(projectors)

    def gram(self, atoms: Sequence[int] | None = None) -> Matrix:
        selected = tuple(self.atoms() if atoms is None else atoms)
        _, _, projectors = self.compile()
        return tuple(
            tuple(
                native_gram(projectors[left], projectors[right], self.metric_weights)
                for right in selected
            )
            for left in selected
        )


def divisibility_poset(cutoff: int, name: str | None = None) -> PosetData:
    values = tuple(range(1, cutoff + 1))
    relation = tuple(
        tuple(right % left == 0 for right in values) for left in values
    )
    return PosetData(
        name=name or f"divisibility_{cutoff}",
        object_names=tuple(f"n{value}" for value in values),
        roof_weights=values,
        relation=relation,
    )


def divisibility_inventory(values: Sequence[int], name: str) -> PosetData:
    values = tuple(values)
    relation = tuple(
        tuple(right % left == 0 for right in values) for left in values
    )
    return PosetData(
        name=name,
        object_names=tuple(f"v{index}" for index in range(len(values))),
        roof_weights=values,
        relation=relation,
    )


def mutated_cover_poset(cutoff: int = 18) -> PosetData:
    base = divisibility_poset(cutoff)
    edges = set(hasse_edges(base.relation))
    target = base.roof_weights.index(6)
    edges = {(left, right) for left, right in edges if right != target}
    edges.add((base.bottom, target))
    return PosetData(
        name="mutated_cover_promote_6",
        object_names=base.object_names,
        roof_weights=base.roof_weights,
        relation=transitive_closure(base.size, edges),
    )


def generic_dag_poset(seed: int = 29031) -> PosetData:
    rng = random.Random(seed)
    roofs = (1, 10, 14, 21, 25, 50, 70, 75, 98, 105, 150, 210)
    atoms = (1, 2, 3, 4)
    lower = (5, 6, 7, 8)
    upper = (9, 10, 11)
    edges: set[tuple[int, int]] = {(0, atom) for atom in atoms}
    for node in lower:
        chosen = [atom for atom in atoms if rng.random() < 0.58]
        if len(chosen) < 2:
            chosen = list(atoms[:2])
        edges.update((atom, node) for atom in chosen)
    for node in upper:
        chosen = [item for item in lower if rng.random() < 0.62]
        if not chosen:
            chosen = [lower[node % len(lower)]]
        edges.update((item, node) for item in chosen)
    return PosetData(
        name=f"seeded_generic_dag_{seed}",
        object_names=tuple(f"g{index}" for index in range(len(roofs))),
        roof_weights=roofs,
        relation=transitive_closure(len(roofs), edges),
    )


def random_inventory_poset(seed: int = 29032) -> PosetData:
    rng = random.Random(seed)
    pool = list(range(11, 140))
    rng.shuffle(pool)
    atom_roofs = tuple(sorted(pool[:5]))
    upper_roofs = tuple(sorted(pool[5:9]))
    roofs = (1,) + atom_roofs + upper_roofs
    atom_indices = tuple(range(1, 6))
    upper_indices = tuple(range(6, 10))
    edges: set[tuple[int, int]] = {(0, index) for index in atom_indices}
    for upper in upper_indices:
        chosen = [index for index in atom_indices if rng.random() < 0.55]
        if len(chosen) < 2:
            chosen = [
                atom_indices[(upper - 6) % 5],
                atom_indices[(upper - 5) % 5],
            ]
        edges.update((index, upper) for index in chosen)
    return PosetData(
        name=f"seeded_random_inventory_{seed}",
        object_names=tuple(f"r{index}" for index in range(len(roofs))),
        roof_weights=roofs,
        relation=transitive_closure(len(roofs), edges),
    )


def permute_poset(poset: PosetData, order: Sequence[int], name: str) -> PosetData:
    order = tuple(order)
    if sorted(order) != list(range(poset.size)):
        raise ValueError("not a permutation")
    inverse = {old: new for new, old in enumerate(order)}
    return PosetData(
        name=name,
        object_names=tuple(f"rho_{31 * old + 7}" for old in order),
        roof_weights=tuple(poset.roof_weights[old] for old in order),
        relation=tuple(
            tuple(poset.relation[left][right] for right in order) for left in order
        ),
        bottom=inverse[poset.bottom],
        eta=poset.eta,
    )


def random_permutation(size: int, seed: int) -> tuple[int, ...]:
    order = list(range(size))
    random.Random(seed).shuffle(order)
    return tuple(order)


def least_upper_bound(poset: PosetData, elements: Sequence[int]) -> int | None:
    upper = [
        candidate
        for candidate in range(poset.size)
        if all(poset.relation[element][candidate] for element in elements)
    ]
    minimal = [
        candidate
        for candidate in upper
        if not any(
            other != candidate and poset.relation[other][candidate]
            for other in upper
        )
    ]
    return minimal[0] if len(minimal) == 1 else None


def boolean_interval(poset: PosetData, atoms: Sequence[int], join: int | None) -> bool:
    if join is None:
        return False
    atoms = tuple(atoms)
    interval = [
        element
        for element in range(poset.size)
        if poset.relation[poset.bottom][element] and poset.relation[element][join]
    ]
    masks: dict[tuple[int, ...], int] = {}
    for element in interval:
        mask = tuple(index for index, atom in enumerate(atoms) if poset.relation[atom][element])
        if mask in masks:
            return False
        masks[mask] = element
    expected = {
        tuple(index for index in range(len(atoms)) if bits & (1 << index))
        for bits in range(1 << len(atoms))
    }
    if set(masks) != expected:
        return False
    for left_mask, left in masks.items():
        for right_mask, right in masks.items():
            if poset.relation[left][right] != set(left_mask).issubset(right_mask):
                return False
    return True


def tensor_associative(poset: PosetData, atoms: Sequence[int], join: int | None) -> bool:
    if join is None:
        return False
    atoms = tuple(atoms)
    if len(atoms) == 2:
        return least_upper_bound(poset, atoms) == join
    for ordering in permutations(atoms):
        current = ordering[0]
        for atom in ordering[1:]:
            next_join = least_upper_bound(poset, (current, atom))
            if next_join is None:
                return False
            current = next_join
        if current != join:
            return False
    return True


def finite_coherence(poset: PosetData, atoms: Sequence[int]) -> dict[str, object]:
    atoms = tuple(atoms)
    join = least_upper_bound(poset, atoms)
    _, mobius, _ = poset.compile()
    uj = join is not None
    bi = boolean_interval(poset, atoms, join)
    mu_value = mobius[poset.bottom][join] if join is not None else Fraction(0)
    mu = uj and mu_value == (-1) ** len(atoms)
    expected_roof = math.prod(poset.roof_weights[atom] for atom in atoms)
    rm = uj and poset.roof_weights[join] == expected_roof
    ta = tensor_associative(poset, atoms, join)
    predicates = {"UJ": uj, "BI": bi, "MU": mu, "RM": rm, "TA": ta}
    return {
        "predicates": predicates,
        "full": all(predicates.values()),
        "join_index": join,
        "join_name": None if join is None else poset.object_names[join],
        "join_roof": None if join is None else poset.roof_weights[join],
        "expected_roof": expected_roof,
        "mobius_bottom_join": fraction_record(mu_value),
    }


def divisors(value: int) -> tuple[int, ...]:
    return tuple(candidate for candidate in range(1, value + 1) if value % candidate == 0)


def mobius_interval_top(value: int) -> int:
    values = divisors(value)
    mu: dict[int, int] = {1: 1}
    for right in values[1:]:
        mu[right] = -sum(mu[left] for left in values if left < right and right % left == 0)
    return mu[value]


def divisibility_ambient_coherence(atom_weights: Sequence[int]) -> dict[str, object]:
    weights = tuple(atom_weights)
    join = math.lcm(*weights)
    interval = divisors(join)
    masks: dict[tuple[int, ...], int] = {}
    collision = False
    for value in interval:
        mask = tuple(index for index, atom in enumerate(weights) if value % atom == 0)
        if mask in masks:
            collision = True
        masks[mask] = value
    expected_masks = {
        tuple(index for index in range(len(weights)) if bits & (1 << index))
        for bits in range(1 << len(weights))
    }
    uj = True
    bi = not collision and set(masks) == expected_masks
    mu_value = mobius_interval_top(join)
    mu = mu_value == (-1) ** len(weights)
    expected_roof = math.prod(weights)
    rm = join == expected_roof
    ta = all(
        math.lcm(math.lcm(ordering[0], ordering[1]), *ordering[2:]) == join
        for ordering in permutations(weights)
    )
    predicates = {"UJ": uj, "BI": bi, "MU": mu, "RM": rm, "TA": ta}
    return {
        "predicates": predicates,
        "full": all(predicates.values()),
        "join_roof": join,
        "expected_roof": expected_roof,
        "interval_size": len(interval),
        "mobius_bottom_join": fraction_record(Fraction(mu_value)),
    }


@dataclass(frozen=True)
class FreeCommutativeMonoid:
    name: str
    generator_names: tuple[str, ...]
    generator_weights: tuple[int, ...]
    exponent_cap: int
    alias: str = "free_commutative"

    @property
    def rank(self) -> int:
        return len(self.generator_names)

    @property
    def element_count(self) -> int:
        return (self.exponent_cap + 1) ** self.rank

    def atom(self, index: int) -> tuple[int, ...]:
        return tuple(int(position == index) for position in range(self.rank))

    def join(self, elements: Sequence[Sequence[int]]) -> tuple[int, ...]:
        return tuple(max(element[index] for element in elements) for index in range(self.rank))

    def roof(self, element: Sequence[int]) -> int:
        return math.prod(
            weight ** exponent
            for weight, exponent in zip(self.generator_weights, element)
        )

    def mobius_from_bottom(self, element: Sequence[int]) -> int:
        if any(exponent > 1 for exponent in element):
            return 0
        return (-1) ** sum(element)

    def coherence(self, atom_indices: Sequence[int]) -> dict[str, object]:
        atom_indices = tuple(atom_indices)
        atoms = tuple(self.atom(index) for index in atom_indices)
        join = self.join(atoms)
        support = tuple(index for index, exponent in enumerate(join) if exponent)
        uj = True
        bi = all(exponent in (0, 1) for exponent in join) and len(support) == len(atom_indices)
        mu_value = self.mobius_from_bottom(join)
        mu = mu_value == (-1) ** len(atom_indices)
        join_roof = self.roof(join)
        expected_roof = math.prod(self.generator_weights[index] for index in atom_indices)
        rm = join_roof == expected_roof
        ta = all(
            self.join((self.join((atoms[0], atoms[1])), *atoms[2:])) == join
            for _ in (0,)
        )
        predicates = {"UJ": uj, "BI": bi, "MU": mu, "RM": rm, "TA": ta}
        return {
            "predicates": predicates,
            "full": all(predicates.values()),
            "join_exponents": list(join),
            "join_roof": join_roof,
            "expected_roof": expected_roof,
            "interval_size": 2 ** len(atom_indices),
            "mobius_bottom_join": fraction_record(Fraction(mu_value)),
        }


def analytic_gram(atom_weights: Sequence[int], eta: int = 2) -> Matrix:
    weights = tuple(atom_weights)
    return tuple(
        tuple(
            Fraction(1) + Fraction(1, left ** (2 * eta))
            if left == right
            else Fraction(
                1,
                (left ** (2 * eta) + 1) * (right ** (2 * eta) + 1),
            )
            for right in weights
        )
        for left in weights
    )


def squarefree_split(value: int) -> tuple[int, int]:
    square = 1
    radical = 1
    factor = 2
    remainder = value
    while factor * factor <= remainder:
        exponent = 0
        while remainder % factor == 0:
            remainder //= factor
            exponent += 1
        square *= factor ** (exponent // 2)
        if exponent % 2:
            radical *= factor
        factor += 1
    if remainder > 1:
        radical *= remainder
    return square, radical


def radical_record(coefficient: Fraction, denominator_radicand: int) -> dict[str, object]:
    square, radical = squarefree_split(denominator_radicand)
    rational = coefficient / (square * radical)
    return {
        "rational_coefficient": fraction_record(rational),
        "squarefree_radicand": radical,
        "display": (
            fraction_text(rational)
            if radical == 1
            else f"{fraction_text(rational)}*sqrt({radical})"
        ),
    }


def gamma_length(value: int) -> int:
    return 2 * (value.bit_length() - 1) + 1


def statistic_record(
    source_name: str,
    atom_names: Sequence[str],
    atom_weights: Sequence[int],
    gram: Matrix,
    coherence_function,
) -> dict[str, object]:
    names = tuple(atom_names)
    weights = tuple(atom_weights)
    pair_rows = []
    pair_full: dict[tuple[int, int], bool] = {}
    gram_by_pair: dict[tuple[int, int], Fraction] = {}
    for left, right in combinations(range(len(weights)), 2):
        coherence = coherence_function((left, right))
        g = gram[left][right]
        key = (left, right)
        pair_full[key] = bool(coherence["full"])
        gram_by_pair[key] = g
        h_squared = g * g / (weights[left] * weights[right])
        pair_rows.append(
            {
                "atom_names": [names[left], names[right]],
                "atom_weights": [weights[left], weights[right]],
                "coherence": coherence,
                "gram": fraction_record(g),
                "filtered": bool(coherence["full"]),
                "C2_cos_amplitude": radical_record(
                    4 * g if coherence["full"] else Fraction(0),
                    weights[left] * weights[right],
                ),
                "H_squared": fraction_record(
                    h_squared if coherence["full"] else Fraction(0)
                ),
                "marker_exponent": gamma_length(weights[left])
                + gamma_length(weights[right]),
            }
        )
    triple_rows = []
    theta3 = Fraction(0)
    auxiliary_e3 = Fraction(0)
    for left, middle, right in combinations(range(len(weights)), 3):
        coherence = coherence_function((left, middle, right))
        product_coefficient = (
            2
            * gram_by_pair[(left, middle)]
            * gram_by_pair[(middle, right)]
            * gram_by_pair[(left, right)]
            / (weights[left] * weights[middle] * weights[right])
        )
        filtered_theta = product_coefficient if coherence["full"] else Fraction(0)
        pair_cycle = (
            pair_full[(left, middle)]
            and pair_full[(middle, right)]
            and pair_full[(left, right)]
        )
        filtered_auxiliary = product_coefficient if pair_cycle else Fraction(0)
        theta3 += filtered_theta
        auxiliary_e3 += filtered_auxiliary
        triple_rows.append(
            {
                "atom_names": [names[left], names[middle], names[right]],
                "atom_weights": [weights[left], weights[middle], weights[right]],
                "coherence": coherence,
                "connected_coefficient": fraction_record(filtered_theta),
                "auxiliary_e3_coefficient": fraction_record(filtered_auxiliary),
                "marker_exponent": 2
                * (
                    gamma_length(weights[left])
                    + gamma_length(weights[middle])
                    + gamma_length(weights[right])
                ),
            }
        )
    e2 = -sum(
        (
            Fraction(row["H_squared"]["numerator"], row["H_squared"]["denominator"])
            for row in pair_rows
        ),
        Fraction(0),
    )
    return {
        "source": source_name,
        "atom_count": len(weights),
        "atom_names": list(names),
        "atom_weights": list(weights),
        "pair_rows": pair_rows,
        "triple_rows": triple_rows,
        "qualified_pairs": sum(bool(row["filtered"]) for row in pair_rows),
        "qualified_triples": sum(bool(row["coherence"]["full"]) for row in triple_rows),
        "C2_nonzero": any(
            row["filtered"]
            and Fraction(row["gram"]["numerator"], row["gram"]["denominator"]) != 0
            for row in pair_rows
        ),
        "theta3": fraction_record(theta3),
        "auxiliary_det_e2": fraction_record(e2),
        "auxiliary_det_e3": fraction_record(auxiliary_e3),
        "theta3_nonzero": theta3 != 0,
        "auxiliary_e3_nonzero": auxiliary_e3 != 0,
    }


def canonical_statistic(record: dict[str, object]) -> dict[str, object]:
    pairs = []
    for row in record["pair_rows"]:
        pairs.append(
            {
                "atom_weights": sorted(row["atom_weights"]),
                "predicates": row["coherence"]["predicates"],
                "full": row["coherence"]["full"],
                "gram": row["gram"],
                "C2_cos_amplitude": row["C2_cos_amplitude"],
                "H_squared": row["H_squared"],
                "marker_exponent": row["marker_exponent"],
            }
        )
    triples = []
    for row in record["triple_rows"]:
        triples.append(
            {
                "atom_weights": sorted(row["atom_weights"]),
                "predicates": row["coherence"]["predicates"],
                "full": row["coherence"]["full"],
                "connected_coefficient": row["connected_coefficient"],
                "auxiliary_e3_coefficient": row["auxiliary_e3_coefficient"],
                "marker_exponent": row["marker_exponent"],
            }
        )
    pairs.sort(key=lambda row: tuple(row["atom_weights"]))
    triples.sort(key=lambda row: tuple(row["atom_weights"]))
    return {
        "atom_weights": sorted(record["atom_weights"]),
        "pairs": pairs,
        "triples": triples,
        "qualified_pairs": record["qualified_pairs"],
        "qualified_triples": record["qualified_triples"],
        "theta3": record["theta3"],
        "auxiliary_det_e2": record["auxiliary_det_e2"],
        "auxiliary_det_e3": record["auxiliary_det_e3"],
    }


def formal_divisibility_record(cutoff: int, source_name: str | None = None) -> dict[str, object]:
    poset = divisibility_poset(cutoff)
    atom_indices = poset.atoms()
    weights = tuple(poset.roof_weights[index] for index in atom_indices)
    names = tuple(poset.object_names[index] for index in atom_indices)
    gram = analytic_gram(weights)
    return statistic_record(
        source_name or f"integer_divisibility_active_{cutoff}",
        names,
        weights,
        gram,
        lambda subset: divisibility_ambient_coherence(
            tuple(weights[index] for index in subset)
        ),
    )


def formal_free_record(
    weights: Sequence[int],
    source_name: str,
    alias: str = "free_commutative",
    relabel_seed: int | None = None,
) -> dict[str, object]:
    weights = tuple(weights)
    names = [f"x{index}" if alias == "free_commutative" else f"X_{index}" for index in range(len(weights))]
    order = list(range(len(weights)))
    if relabel_seed is not None:
        random.Random(relabel_seed).shuffle(order)
    transported_weights = tuple(weights[index] for index in order)
    transported_names = tuple(names[index] for index in order)
    monoid = FreeCommutativeMonoid(
        name=source_name,
        generator_names=transported_names,
        generator_weights=transported_weights,
        exponent_cap=2,
        alias=alias,
    )
    gram = analytic_gram(transported_weights)
    return statistic_record(
        source_name,
        transported_names,
        transported_weights,
        gram,
        monoid.coherence,
    )


def finite_poset_record(poset: PosetData) -> dict[str, object]:
    atoms = poset.atoms()
    names = tuple(poset.object_names[index] for index in atoms)
    weights = tuple(poset.roof_weights[index] for index in atoms)
    gram = poset.gram(atoms)
    return statistic_record(
        poset.name,
        names,
        weights,
        gram,
        lambda subset: finite_coherence(poset, tuple(atoms[index] for index in subset)),
    )


def mask_qualifies(coherence: dict[str, object], mask: int) -> bool:
    return all(
        bool(coherence["predicates"][name])
        for index, name in enumerate(PREDICATES)
        if mask & (1 << index)
    )


def predicate_mask_rows(records: Sequence[dict[str, object]]) -> list[dict[str, object]]:
    rows = []
    for mask in range(1, 1 << len(PREDICATES)):
        names = [name for index, name in enumerate(PREDICATES) if mask & (1 << index)]
        for record in records:
            rows.append(
                {
                    "mask": mask,
                    "predicates": names,
                    "source": record["source"],
                    "qualified_pairs": sum(
                        mask_qualifies(row["coherence"], mask) for row in record["pair_rows"]
                    ),
                    "qualified_triples": sum(
                        mask_qualifies(row["coherence"], mask) for row in record["triple_rows"]
                    ),
                    "is_frozen_full_selector": mask == (1 << len(PREDICATES)) - 1,
                }
            )
    return rows


def exact_projector_checks(poset: PosetData) -> dict[str, object]:
    zeta, mobius, projectors = poset.compile()
    identity = identity_matrix(poset.size)
    inverse = matrix_multiply(zeta, mobius) == identity and matrix_multiply(mobius, zeta) == identity
    orthogonal = True
    total = [[Fraction(0) for _ in range(poset.size)] for _ in range(poset.size)]
    for i, left in enumerate(projectors):
        for row in range(poset.size):
            for column in range(poset.size):
                total[row][column] += left[row][column]
        for j, right in enumerate(projectors):
            expected = left if i == j else zero_matrix(poset.size)
            orthogonal = orthogonal and matrix_multiply(left, right) == expected
    partition = tuple(tuple(row) for row in total) == identity
    gram = poset.gram()
    symmetric = all(gram[i][j] == gram[j][i] for i in range(len(gram)) for j in range(len(gram)))
    return {
        "source": poset.name,
        "zeta_mobius_inverse": inverse,
        "primitive_relations": orthogonal,
        "partition_identity": partition,
        "gram_symmetric": symmetric,
        "all_pass": inverse and orthogonal and partition and symmetric,
    }


def tail_certificates(cutoff: int) -> dict[str, object]:
    pair_bound = Fraction(5, 36 * cutoff**3)
    triangle_bound = Fraction(25, 16_777_216 * cutoff**8)
    return {
        "cutoff": cutoff,
        "C2_absolute_tail_bound_over_C_eta": fraction_record(pair_bound),
        "triangle_absolute_tail_bound_over_C_eta_cubed": fraction_record(triangle_bound),
        "bounds_tend_to_zero": True,
        "C2_derivation": "g_ab<=(ab)^-4; 4*(sum n^-4)*(tail n^-4) <= 5/(36N^3)",
        "triangle_derivation": "2*g_ab*g_bc*g_ca/(abc)<=2*(abc)^-9; integer-sum bound",
    }


def free_control_rows(
    transported_weights: Sequence[int],
    generic_weights: Sequence[int],
) -> list[dict[str, object]]:
    rows = []
    for rank in range(2, 7):
        for cap in range(1, 4):
            for alias, weights in (
                ("free_commutative", tuple(transported_weights[:rank])),
                ("polynomial_UFD_monomials", tuple(transported_weights[:rank])),
                ("generic_weight_free_commutative", tuple(generic_weights[:rank])),
            ):
                monoid = FreeCommutativeMonoid(
                    name=f"{alias}_r{rank}_cap{cap}",
                    generator_names=tuple(f"g{index}" for index in range(rank)),
                    generator_weights=weights,
                    exponent_cap=cap,
                    alias=alias,
                )
                pair_results = [
                    monoid.coherence(subset) for subset in combinations(range(rank), 2)
                ]
                triple_results = [
                    monoid.coherence(subset) for subset in combinations(range(rank), 3)
                ]
                rows.append(
                    {
                        "name": monoid.name,
                        "alias": alias,
                        "rank": rank,
                        "exponent_cap": cap,
                        "element_count": monoid.element_count,
                        "generator_weights": list(weights),
                        "pair_count": len(pair_results),
                        "triple_count": len(triple_results),
                        "all_pairs_fully_coherent": all(row["full"] for row in pair_results),
                        "all_triples_fully_coherent": all(row["full"] for row in triple_results),
                        "cap_independent_local_intervals": cap >= 1,
                    }
                )
    return rows
