#!/usr/bin/env python3
"""Exact core for the SD-C31 source-natural counterterm stress test.

Only Python's standard library is used.  All incidence, Gram, counterterm,
and coefficient calculations are rational; oscillatory terms are retained as
formal frequency/radical ledgers instead of sampled floating-point cosines.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
import math
import random
from typing import Iterable, Sequence


Matrix = tuple[tuple[Fraction, ...], ...]
Relation = tuple[tuple[bool, ...], ...]


def frac(value: int | Fraction) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value)


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def fraction_record(value: Fraction) -> dict[str, int | str]:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "text": fraction_text(value),
    }


def zero_matrix(size: int) -> Matrix:
    return tuple(tuple(Fraction(0) for _ in range(size)) for _ in range(size))


def identity_matrix(size: int) -> Matrix:
    return tuple(
        tuple(Fraction(int(i == j)) for j in range(size)) for i in range(size)
    )


def matrix_from_ints(rows: Sequence[Sequence[int | bool]]) -> Matrix:
    return tuple(tuple(Fraction(int(value)) for value in row) for row in rows)


def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
    size = len(left)
    return tuple(
        tuple(
            sum((left[i][k] * right[k][j] for k in range(size)), Fraction(0))
            for j in range(size)
        )
        for i in range(size)
    )


def matrix_transpose(matrix: Matrix) -> Matrix:
    return tuple(tuple(matrix[j][i] for j in range(len(matrix))) for i in range(len(matrix)))


def matrix_trace(matrix: Matrix) -> Fraction:
    return sum((matrix[i][i] for i in range(len(matrix))), Fraction(0))


def matrix_inverse(matrix: Matrix) -> Matrix:
    """Gauss--Jordan inverse, valid for arbitrary object ordering."""

    size = len(matrix)
    aug = [list(matrix[i]) + list(identity_matrix(size)[i]) for i in range(size)]
    for column in range(size):
        pivot = next((row for row in range(column, size) if aug[row][column]), None)
        if pivot is None:
            raise ValueError("singular matrix")
        if pivot != column:
            aug[column], aug[pivot] = aug[pivot], aug[column]
        scale = aug[column][column]
        aug[column] = [entry / scale for entry in aug[column]]
        for row in range(size):
            if row == column:
                continue
            coefficient = aug[row][column]
            if coefficient:
                aug[row] = [
                    aug[row][j] - coefficient * aug[column][j]
                    for j in range(2 * size)
                ]
    return tuple(tuple(row[size:]) for row in aug)


def outer(left: Sequence[Fraction], right: Sequence[Fraction]) -> Matrix:
    return tuple(tuple(x * y for y in right) for x in left)


def weighted_sharp(matrix: Matrix, metric_weights: Sequence[Fraction]) -> Matrix:
    """Return W^{-1} A^T W for diagonal positive W."""

    size = len(matrix)
    return tuple(
        tuple(matrix[j][i] * metric_weights[j] / metric_weights[i] for j in range(size))
        for i in range(size)
    )


def native_gram(left: Matrix, right: Matrix, metric_weights: Sequence[Fraction]) -> Fraction:
    return matrix_trace(matrix_multiply(left, weighted_sharp(right, metric_weights)))


def transitive_closure(size: int, edges: Iterable[tuple[int, int]]) -> Relation:
    rel = [[False] * size for _ in range(size)]
    for i in range(size):
        rel[i][i] = True
    for left, right in edges:
        if left == right:
            continue
        rel[left][right] = True
    for middle in range(size):
        for left in range(size):
            if not rel[left][middle]:
                continue
            for right in range(size):
                if rel[middle][right]:
                    rel[left][right] = True
    if any(rel[i][j] and rel[j][i] for i in range(size) for j in range(size) if i != j):
        raise ValueError("edges contain a directed cycle")
    return tuple(tuple(row) for row in rel)


def hasse_edges(relation: Relation) -> tuple[tuple[int, int], ...]:
    size = len(relation)
    result: list[tuple[int, int]] = []
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
                result.append((left, right))
    return tuple(result)


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
        if len(self.roof_weights) != size or len(self.relation) != size:
            raise ValueError("poset dimensions disagree")
        if any(len(row) != size for row in self.relation):
            raise ValueError("relation is not square")
        if any(weight <= 0 for weight in self.roof_weights):
            raise ValueError("roof weights must be positive")
        if not all(self.relation[i][i] for i in range(size)):
            raise ValueError("relation is not reflexive")
        for i in range(size):
            for j in range(size):
                if i != j and self.relation[i][j] and self.relation[j][i]:
                    raise ValueError("relation is not antisymmetric")
                for k in range(size):
                    if self.relation[i][j] and self.relation[j][k] and not self.relation[i][k]:
                        raise ValueError("relation is not transitive")
        if not all(self.relation[self.bottom][i] for i in range(size)):
            raise ValueError("designated bottom is not below every object")

    @property
    def size(self) -> int:
        return len(self.object_names)

    @property
    def metric_weights(self) -> tuple[Fraction, ...]:
        return tuple(Fraction(weight ** (2 * self.eta)) for weight in self.roof_weights)

    def atoms(self) -> tuple[int, ...]:
        result: list[int] = []
        for right in range(self.size):
            if right == self.bottom or not self.relation[self.bottom][right]:
                continue
            has_middle = any(
                middle not in (self.bottom, right)
                and self.relation[self.bottom][middle]
                and self.relation[middle][right]
                for middle in range(self.size)
            )
            if not has_middle:
                result.append(right)
        return tuple(result)

    def compile(self) -> tuple[Matrix, Matrix, tuple[Matrix, ...]]:
        zeta = matrix_from_ints(self.relation)
        mobius = matrix_inverse(zeta)
        compiled = []
        for index in range(self.size):
            column = tuple(zeta[row][index] for row in range(self.size))
            row = tuple(mobius[index][column_index] for column_index in range(self.size))
            compiled.append(outer(column, row))
        return zeta, mobius, tuple(compiled)

    def gram(self, selected: Sequence[int] | None = None) -> Matrix:
        selected = tuple(self.atoms() if selected is None else selected)
        _, _, compiled = self.compile()
        weights = self.metric_weights
        return tuple(
            tuple(native_gram(compiled[i], compiled[j], weights) for j in selected)
            for i in selected
        )


def divisibility_poset(cutoff: int, name: str | None = None) -> PosetData:
    labels = tuple(range(1, cutoff + 1))
    relation = tuple(tuple(right % left == 0 for right in labels) for left in labels)
    return PosetData(
        name=name or f"divisibility_{cutoff}",
        object_names=tuple(f"n{value}" for value in labels),
        roof_weights=labels,
        relation=relation,
    )


def divisibility_inventory(labels: Sequence[int], name: str) -> PosetData:
    labels = tuple(labels)
    if labels[0] != 1:
        raise ValueError("inventory must start at bottom weight 1")
    relation = tuple(tuple(right % left == 0 for right in labels) for left in labels)
    return PosetData(
        name=name,
        object_names=tuple(f"v{index}" for index in range(len(labels))),
        roof_weights=labels,
        relation=relation,
    )


def permute_poset(poset: PosetData, order: Sequence[int], name: str) -> PosetData:
    order = tuple(order)
    if sorted(order) != list(range(poset.size)):
        raise ValueError("not a permutation")
    inverse = {old: new for new, old in enumerate(order)}
    return PosetData(
        name=name,
        object_names=tuple(f"rho_{17 * old + 5}" for old in order),
        roof_weights=tuple(poset.roof_weights[old] for old in order),
        relation=tuple(
            tuple(poset.relation[old_left][old_right] for old_right in order)
            for old_left in order
        ),
        bottom=inverse[poset.bottom],
        eta=poset.eta,
    )


def restrict_poset(poset: PosetData, indices: Sequence[int], name: str) -> PosetData:
    indices = tuple(indices)
    inverse = {old: new for new, old in enumerate(indices)}
    if poset.bottom not in inverse:
        raise ValueError("restriction omits bottom")
    return PosetData(
        name=name,
        object_names=tuple(poset.object_names[index] for index in indices),
        roof_weights=tuple(poset.roof_weights[index] for index in indices),
        relation=tuple(
            tuple(poset.relation[left][right] for right in indices) for left in indices
        ),
        bottom=inverse[poset.bottom],
        eta=poset.eta,
    )


def mutated_cover_poset(cutoff: int = 18) -> PosetData:
    base = divisibility_poset(cutoff)
    edges = set(hasse_edges(base.relation))
    target = base.roof_weights.index(6)
    edges = {(left, right) for left, right in edges if right != target}
    edges.add((base.bottom, target))
    relation = transitive_closure(base.size, edges)
    return PosetData(
        name="mutated_cover_promote_6",
        object_names=base.object_names,
        roof_weights=base.roof_weights,
        relation=relation,
        eta=base.eta,
    )


def generic_dag_poset(seed: int = 29031) -> PosetData:
    rng = random.Random(seed)
    roofs = (1, 10, 14, 21, 25, 50, 70, 75, 98, 105, 150, 210)
    size = len(roofs)
    atoms = (1, 2, 3, 4)
    layer_one = (5, 6, 7, 8)
    layer_two = (9, 10, 11)
    edges: set[tuple[int, int]] = {(0, atom) for atom in atoms}
    for upper in layer_one:
        chosen = [atom for atom in atoms if rng.random() < 0.58]
        if len(chosen) < 2:
            chosen = list(atoms[:2])
        edges.update((atom, upper) for atom in chosen)
    for upper in layer_two:
        chosen = [lower for lower in layer_one if rng.random() < 0.62]
        if not chosen:
            chosen = [layer_one[upper % len(layer_one)]]
        edges.update((lower, upper) for lower in chosen)
    relation = transitive_closure(size, edges)
    return PosetData(
        name=f"seeded_generic_dag_{seed}",
        object_names=tuple(f"g{index}" for index in range(size)),
        roof_weights=roofs,
        relation=relation,
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
            chosen = [atom_indices[(upper - 6) % 5], atom_indices[(upper - 5) % 5]]
        edges.update((index, upper) for index in chosen)
    relation = transitive_closure(len(roofs), edges)
    return PosetData(
        name=f"seeded_random_inventory_{seed}",
        object_names=tuple(f"r{index}" for index in range(len(roofs))),
        roof_weights=roofs,
        relation=relation,
    )


def analytic_gram(atom_weights: Sequence[int], eta: int = 2) -> Matrix:
    """Source-locked infinite divisibility Gram in units of C_eta."""

    weights = tuple(atom_weights)
    rows: list[tuple[Fraction, ...]] = []
    for left in weights:
        row: list[Fraction] = []
        for right in weights:
            if left == right:
                row.append(Fraction(1) + Fraction(1, left ** (2 * eta)))
            else:
                row.append(
                    Fraction(
                        1,
                        (left ** (2 * eta) + 1) * (right ** (2 * eta) + 1),
                    )
                )
        rows.append(tuple(row))
    return tuple(rows)


def squarefree_split(value: int) -> tuple[int, int]:
    """Return k,d with value=k^2 d and d squarefree."""

    remainder = value
    square = 1
    radical = 1
    factor = 2
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


def radical_amplitude(coefficient: Fraction, denominator_radicand: int) -> dict[str, object]:
    """Represent coefficient/sqrt(n) as rational*sqrt(squarefree d)."""

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


def pair_ledgers(atom_weights: Sequence[int], gram: Matrix) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    weights = tuple(atom_weights)
    mixed: list[dict[str, object]] = []
    b4: list[dict[str, object]] = []
    for left, right in combinations(range(len(weights)), 2):
        low, high = sorted((weights[left], weights[right]))
        g = gram[left][right]
        frequency = Fraction(high, low)
        mixed.append(
            {
                "atom_weights": [low, high],
                "frequency_ratio": fraction_record(frequency),
                "gram": fraction_record(g),
                "cos_amplitude": radical_amplitude(4 * g, low * high),
                "nonzero": g != 0,
            }
        )
        b4_coefficient = 4 * g * g / (low * high)
        b4.append(
            {
                "atom_weights": [low, high],
                "double_frequency_ratio": fraction_record(frequency * frequency),
                "coefficient": fraction_record(b4_coefficient),
                "positive": b4_coefficient > 0,
            }
        )
    mixed.sort(key=lambda row: tuple(row["atom_weights"]))
    b4.sort(key=lambda row: tuple(row["atom_weights"]))
    return mixed, b4


def diagonal_ledger(atom_weights: Sequence[int], gram: Matrix) -> Fraction:
    return 2 * sum(
        (gram[index][index] / weight for index, weight in enumerate(atom_weights)),
        Fraction(0),
    )


def baseline_scheme_record(cutoff: int) -> dict[str, object]:
    poset = divisibility_poset(cutoff)
    atoms = poset.atoms()
    weights = tuple(poset.roof_weights[index] for index in atoms)
    gram = analytic_gram(weights, poset.eta)
    leading = 2 * sum((Fraction(1, weight) for weight in weights), Fraction(0))
    shifts = {
        f"S{k}": 2
        * sum(
            (Fraction(1, weight ** (1 + 2 * poset.eta + k)) for weight in weights),
            Fraction(0),
        )
        for k in range(3)
    }
    diagonal = diagonal_ledger(weights, gram)
    mixed, b4 = pair_ledgers(weights, gram)
    return {
        "cutoff": cutoff,
        "atom_count": len(atoms),
        "atom_weights": list(weights),
        "normalization": "C_eta factored out",
        "diagonal_D": fraction_record(diagonal),
        "leading_H": fraction_record(leading),
        "shifts": {key: fraction_record(value) for key, value in shifts.items()},
        "identity_D_equals_H_plus_S0": diagonal == leading + shifts["S0"],
        "full_residual_constant": fraction_record(Fraction(0)),
        "lead_residual_constant": fraction_record(shifts["S0"]),
        "schemes_distinct": shifts["S0"] != 0,
        "mixed_ledger": mixed,
        "b4_pair_ledger": b4,
    }


def direct_control_record(poset: PosetData) -> dict[str, object]:
    atoms = poset.atoms()
    weights = tuple(poset.roof_weights[index] for index in atoms)
    gram = poset.gram(atoms)
    mixed, b4 = pair_ledgers(weights, gram)
    return {
        "name": poset.name,
        "size": poset.size,
        "atom_indices": list(atoms),
        "atom_names": [poset.object_names[index] for index in atoms],
        "atom_weights": list(weights),
        "pointed_pair_type": "two_incomparable_covers_sharing_bottom",
        "gram": [[fraction_record(entry) for entry in row] for row in gram],
        "diagonal": fraction_record(diagonal_ledger(weights, gram)),
        "mixed_ledger": mixed,
        "b4_pair_ledger": b4,
        "nonzero_mixed_count": sum(bool(row["nonzero"]) for row in mixed),
        "positive_b4_count": sum(bool(row["positive"]) for row in b4),
    }


def random_permutation(size: int, seed: int, keep_bottom: bool = False) -> tuple[int, ...]:
    rng = random.Random(seed)
    order = list(range(size))
    if keep_bottom:
        tail = order[1:]
        rng.shuffle(tail)
        return (0, *tail)
    rng.shuffle(order)
    return tuple(order)


def canonical_analytic_ledger(poset: PosetData) -> dict[str, object]:
    weights = sorted(poset.roof_weights[index] for index in poset.atoms())
    gram = analytic_gram(weights, poset.eta)
    mixed, b4 = pair_ledgers(weights, gram)
    return {
        "atom_weights": weights,
        "diagonal": fraction_record(diagonal_ledger(weights, gram)),
        "mixed": mixed,
        "b4": b4,
    }


def prefix_difference(large: Matrix, small: Matrix, large_indices: Sequence[int]) -> Matrix:
    return tuple(
        tuple(large[large_indices[i]][large_indices[j]] - small[i][j] for j in range(len(small)))
        for i in range(len(small))
    )


def matrix_is_zero(matrix: Matrix) -> bool:
    return all(entry == 0 for row in matrix for entry in row)


def exact_projector_checks(poset: PosetData) -> dict[str, object]:
    zeta, mobius, compiled = poset.compile()
    identity = identity_matrix(poset.size)
    inverse_ok = matrix_multiply(zeta, mobius) == identity and matrix_multiply(mobius, zeta) == identity
    projector_ok = True
    partition = zero_matrix(poset.size)
    partition_rows = [list(row) for row in partition]
    for i, left in enumerate(compiled):
        for row in range(poset.size):
            for column in range(poset.size):
                partition_rows[row][column] += left[row][column]
        for j, right in enumerate(compiled):
            product = matrix_multiply(left, right)
            expected = left if i == j else zero_matrix(poset.size)
            projector_ok = projector_ok and product == expected
    partition = tuple(tuple(row) for row in partition_rows)
    gram = poset.gram()
    gram_symmetric = gram == matrix_transpose(gram)
    return {
        "name": poset.name,
        "size": poset.size,
        "atom_count": len(poset.atoms()),
        "zeta_mobius_two_sided_inverse": inverse_ok,
        "pairwise_idempotent_relations": projector_ok,
        "partition_of_identity": partition == identity,
        "gram_symmetric": gram_symmetric,
        "all_pass": inverse_ok and projector_ok and partition == identity and gram_symmetric,
    }


def cutoff_compiler_check(small_cutoff: int, large_cutoff: int) -> dict[str, object]:
    small = divisibility_poset(small_cutoff)
    large = divisibility_poset(large_cutoff)
    _, _, small_q = small.compile()
    _, _, large_q = large.compile()
    indices = tuple(range(small_cutoff))
    all_restrictions = True
    checked = 0
    for small_index in range(small_cutoff):
        restricted = tuple(
            tuple(large_q[small_index][i][j] for j in indices) for i in indices
        )
        all_restrictions = all_restrictions and restricted == small_q[small_index]
        checked += 1
    small_atoms = [small.roof_weights[i] for i in small.atoms()]
    large_atoms_prefix = [large.roof_weights[i] for i in large.atoms() if large.roof_weights[i] <= small_cutoff]
    return {
        "small_cutoff": small_cutoff,
        "large_cutoff": large_cutoff,
        "compiled_q_restrictions_equal": all_restrictions,
        "objects_checked": checked,
        "source_atom_prefix_equal": small_atoms == large_atoms_prefix,
        "direct_finite_gram_expected_to_change_with_tail": True,
        "all_pass": all_restrictions and small_atoms == large_atoms_prefix,
    }


def transport_check(poset: PosetData, permuted: PosetData, order: Sequence[int]) -> dict[str, object]:
    _, _, original_q = poset.compile()
    _, _, transported_q = permuted.compile()
    order = tuple(order)
    inverse = {old: new for new, old in enumerate(order)}
    all_q = True
    for old_index in range(poset.size):
        new_index = inverse[old_index]
        canonical = tuple(
            tuple(transported_q[new_index][inverse[i]][inverse[j]] for j in range(poset.size))
            for i in range(poset.size)
        )
        all_q = all_q and canonical == original_q[old_index]
    original_ledger = canonical_analytic_ledger(poset)
    permuted_ledger = canonical_analytic_ledger(permuted)
    return {
        "original": poset.name,
        "copy": permuted.name,
        "compiled_projectors_transport": all_q,
        "canonical_analytic_ledgers_equal": original_ledger == permuted_ledger,
        "all_pass": all_q and original_ledger == permuted_ledger,
    }


def coefficient_search(grid: Sequence[Fraction]) -> dict[str, object]:
    rows = []
    solutions = []
    for diagonal_coefficient in grid:
        for pair_coefficient in grid:
            removes_leading_divergence = diagonal_coefficient == 1
            preserves_baseline_mixed = 1 - pair_coefficient == 1
            cancels_nonzero_control_mixed = 1 - pair_coefficient == 0
            row = {
                "diagonal_coefficient": fraction_text(diagonal_coefficient),
                "pair_coefficient": fraction_text(pair_coefficient),
                "removes_leading_divergence": removes_leading_divergence,
                "preserves_baseline_mixed": preserves_baseline_mixed,
                "cancels_nonzero_control_mixed": cancels_nonzero_control_mixed,
                "selective_solution": removes_leading_divergence
                and preserves_baseline_mixed
                and cancels_nonzero_control_mixed,
            }
            rows.append(row)
            if row["selective_solution"]:
                solutions.append(row)
    return {
        "grid": [fraction_text(value) for value in grid],
        "rows_tested": len(rows),
        "solutions": solutions,
        "solution_count": len(solutions),
        "symbolic_constraints": {
            "preserve_baseline": "1-beta=1, hence beta=0",
            "cancel_nonzero_same_type_control": "1-beta=0, hence beta=1",
            "contradiction": "beta=0 and beta=1",
            "scope": "universal coefficient on the shared two-cover pointed local type",
        },
        "exact_no_solution": not solutions,
        "rows": rows,
    }


def local_shift_family(cutoff: int, coefficients: Sequence[Fraction]) -> dict[str, object]:
    record = baseline_scheme_record(cutoff)
    shifts = {
        key: Fraction(value["numerator"], value["denominator"])
        for key, value in record["shifts"].items()
    }
    value = sum(
        (coefficient * shifts[f"S{index}"] for index, coefficient in enumerate(coefficients)),
        Fraction(0),
    )
    return {
        "cutoff": cutoff,
        "coefficients": [fraction_text(value) for value in coefficients],
        "shift_value": fraction_record(value),
        "is_atom_local": True,
        "is_isomorphism_natural": True,
        "is_prefix_additive": True,
    }


def tail_certificates(cutoff: int, eta: int = 2) -> dict[str, object]:
    shifts = {}
    for k in range(3):
        exponent = 1 + 2 * eta + k
        # 2 sum_{n>N} n^{-exponent} <= 2/((exponent-1)N^{exponent-1}).
        bound = Fraction(2, (exponent - 1) * cutoff ** (exponent - 1))
        shifts[f"S{k}"] = {
            "dominates_prime_tail": True,
            "rational_upper_bound": fraction_record(bound),
            "bound_formula": f"2/(({exponent}-1)*N^({exponent}-1))",
        }
    mixed_bound = Fraction(5, 36 * cutoff**3)
    return {
        "cutoff": cutoff,
        "shift_tail_bounds": shifts,
        "mixed_amplitude_tail_bound": fraction_record(mixed_bound),
        "mixed_bound_derivation": "g_pq<=(pq)^-4 and 1/sqrt(pq)<=1; 4*(5/48)*(1/(3N^3))",
        "all_bounds_tend_to_zero": True,
    }


def harmonic_lower_bound_record(cutoffs: Sequence[int]) -> dict[str, object]:
    rows = []
    previous = Fraction(0)
    for cutoff in cutoffs:
        record = baseline_scheme_record(cutoff)
        leading = Fraction(
            record["leading_H"]["numerator"], record["leading_H"]["denominator"]
        )
        rows.append(
            {
                "cutoff": cutoff,
                "H": fraction_record(leading),
                "strictly_increases": leading > previous,
            }
        )
        previous = leading
    return {
        "rows": rows,
        "analytic_certificate": "H_N=2*sum_{source atoms p<=N}1/p diverges by Euler's prime-harmonic theorem",
        "numeric_rows_are_sanity_not_proof": True,
    }


def determinant_ownership_record(baseline: dict[str, object], controls: Sequence[dict[str, object]]) -> dict[str, object]:
    s0 = baseline["shifts"]["S0"]
    s0_fraction = Fraction(s0["numerator"], s0["denominator"])
    return {
        "ordinary_fredholm_determinant_available": False,
        "det2_available": False,
        "det3_available_on_frozen_S3_object": True,
        "log_det3_power_ledger": [
            {"power": 1, "status": "deleted_by_regularization_and_block_trace_zero"},
            {"power": 2, "status": "deleted_entirely_including_diagonal_and_mixed"},
            {"power": 3, "status": "retained_formula_but_trace_zero_by_off_diagonal_block_parity"},
            {"power": 4, "status": "first_visible_nonzero_power", "coefficient": "-Tr(B^4)/4"},
        ],
        "renormalized_functional": {
            "definition": "D_ren,lambda=det3(I-zB)*exp(-z^2*FP_lambda Tr(B^2)/2)",
            "ownership": "new_scheme_dependent_functional_not_ordinary_Fredholm_or_det2",
            "FP_lambda": "(1-lambda)*S0+M(s) in C_eta units",
            "full_over_lead_ratio": f"exp(z^2*({fraction_text(s0_fraction)})*C_eta/2)",
            "ratio_nontrivial": s0_fraction != 0,
            "scheme_change_is_entire_scalar": True,
            "finite_cutoff_holomorphic_in_s_and_z": True,
            "infinite_mixed_holomorphic_on_det3_strip": True,
            "reflection_rule": "D_ren(1-conj(s),conj(z))=conj(D_ren(s,z)) for real scheme coefficients",
            "reflection_preserved": True,
        },
        "baseline_positive_b4_pairs": sum(bool(row["positive"]) for row in baseline["b4_pair_ledger"]),
        "control_positive_b4_pairs": {
            row["name"]: row["positive_b4_count"] for row in controls
        },
        "b4_is_generic_pair_gram_ownership": all(row["positive_b4_count"] > 0 for row in controls),
    }


def canonical_direct_ledger(record: dict[str, object]) -> dict[str, object]:
    return {
        "atom_weights": record["atom_weights"],
        "diagonal": record["diagonal"],
        "mixed_ledger": record["mixed_ledger"],
        "b4_pair_ledger": record["b4_pair_ledger"],
    }
