#!/usr/bin/env python3
"""Exact W(E6), double-six stabilizer, orientation, core, and H1 replay."""

from __future__ import annotations

from collections import deque
from hashlib import sha256
from itertools import combinations
import json
import math

from sympy import Matrix, ZZ
from sympy.combinatorics import Permutation, PermutationGroup
from sympy.matrices.normalforms import smith_normal_decomp, smith_normal_form
from c57_exact import reject_optimized_python


def dot(left, right):
    return left[0] * right[0] - sum(a * b for a, b in zip(left[1:], right[1:]))


def add(left, right, scale=1):
    return tuple(a + scale * b for a, b in zip(left, right))


def reflect(vector, root):
    return add(vector, root, dot(vector, root))


def compose(left, right):
    return tuple(left[right[index]] for index in range(len(left)))


def picard_matrix(root):
    columns = [
        reflect(tuple(int(i == j) for i in range(7)), root) for j in range(7)
    ]
    return Matrix([[columns[column][row] for column in range(7)] for row in range(7)])


def apply_matrix(matrix, vector):
    result = matrix * Matrix(vector)
    return tuple(int(result[index, 0]) for index in range(7))


def line_configuration():
    exceptional = []
    for index in range(6):
        vector = [0] * 7
        vector[index + 1] = 1
        exceptional.append(tuple(vector))
    roots = [add(exceptional[i], exceptional[i + 1], -1) for i in range(5)]
    roots.append((1, -1, -1, -1, 0, 0, 0))
    lines = list(exceptional)
    for left, right in combinations(range(6), 2):
        vector = [1] + [0] * 6
        vector[left + 1] = vector[right + 1] = -1
        lines.append(tuple(vector))
    for omitted in range(6):
        vector = [2] + [-1] * 6
        vector[omitted + 1] = 0
        lines.append(tuple(vector))
    index = {line: position for position, line in enumerate(lines)}
    generators = [tuple(index[reflect(line, root)] for line in lines) for root in roots]
    incidence = [[dot(left, right) for right in lines] for left in lines]
    sixers = [
        frozenset(subset)
        for subset in combinations(range(27), 6)
        if all(incidence[i][j] == 0 for i, j in combinations(subset, 2))
    ]
    double_sixes = set()
    for first in sixers:
        second = frozenset(
            index
            for index in range(27)
            if index not in first
            and sum(incidence[index][other] for other in first) == 5
        )
        if len(second) != 6:
            raise AssertionError("malformed sixer complement")
        double_sixes.add(frozenset((first, second)))
    configurations = sorted(
        double_sixes,
        key=lambda value: tuple(sorted(tuple(sorted(row)) for row in value)),
    )
    return exceptional, roots, lines, generators, incidence, sixers, configurations


def act(permutation, value):
    if isinstance(value, int):
        return permutation[value]
    return frozenset(act(permutation, element) for element in value)


def relation_h1(generators: list[Matrix], coxeter: bool) -> list[int]:
    identity = Matrix.eye(7)
    blocks = []

    def word_block(word):
        block = Matrix.zeros(7, 7 * len(generators))
        prefix = identity
        for index in word:
            block[:, 7 * index : 7 * index + 7] += prefix
            prefix *= generators[index]
        if prefix != identity:
            raise AssertionError("relation word is not the identity")
        blocks.append(block)

    for index in range(len(generators)):
        word_block([index, index])
    if coxeter:
        for left in range(6):
            for right in range(left + 1, 6):
                order = 3 if (generators[left] * generators[right]) ** 3 == identity else 2
                word_block([left, right] * order)
    else:
        for left in range(5):
            for right in range(left + 1, 5):
                word_block([left, right] * (3 if right == left + 1 else 2))
        for index in range(5):
            word_block([5, index, 5, index])
    equations = Matrix.vstack(*blocks)
    diagonal, _, right = smith_normal_decomp(equations, domain=ZZ)
    rank = sum(
        diagonal[i, i] != 0 for i in range(min(diagonal.rows, diagonal.cols))
    )
    if rank != equations.rank():
        raise AssertionError("Smith rank mismatch")
    principal = Matrix.vstack(*(generator - identity for generator in generators))
    if equations * principal != Matrix.zeros(equations.rows, 7):
        raise AssertionError("principal cocycles do not satisfy relations")
    coordinates = right.inv() * principal
    if any(coordinates[i, j] != 0 for i in range(rank) for j in range(7)):
        raise AssertionError("principal cocycle is outside saturated kernel")
    kernel_coordinates = coordinates[rank:, :]
    smith = smith_normal_form(kernel_coordinates, domain=ZZ)
    smith_diagonal = [
        abs(int(smith[i, i]))
        for i in range(min(smith.rows, smith.cols))
        if smith[i, i] != 0
    ]
    return smith_diagonal, rank, equations.cols - rank


def report():
    exceptional, roots, lines, reflections, incidence, sixers, double_sixes = (
        line_configuration()
    )
    if len(lines) != 27 or len(sixers) != 72 or len(double_sixes) != 36:
        raise AssertionError("Schlaefli counts failed")
    identity = tuple(range(27))
    weyl = {identity}
    queue = deque([identity])
    while queue:
        value = queue.popleft()
        for generator in reflections:
            new = compose(generator, value)
            if new not in weyl:
                weyl.add(new)
                queue.append(new)
    if len(weyl) != 51840:
        raise AssertionError("wrong W(E6) order")

    double_index = {value: index for index, value in enumerate(double_sixes)}
    double_actions = [
        Permutation([double_index[act(generator, value)] for value in double_sixes])
        for generator in reflections
    ]
    image_order = int(PermutationGroup(double_actions).order())
    core_order = len(weyl) // image_order
    if core_order != 1:
        raise AssertionError("double-six stabilizer core is nontrivial")

    standard_first = frozenset(range(6))
    standard_second = frozenset(range(21, 27))
    chosen = frozenset((standard_first, standard_second))
    if chosen not in double_sixes:
        raise AssertionError("standard marked double-six is absent")
    stabilizer = [value for value in weyl if act(value, chosen) == chosen]
    if len(stabilizer) != 1440:
        raise AssertionError("wrong double-six stabilizer order")
    first, second = sorted(chosen, key=lambda value: tuple(sorted(value)))
    oriented = [value for value in stabilizer if act(value, first) == first]
    swaps = [value for value in stabilizer if act(value, first) == second]
    if len(oriented) != 720 or len(swaps) != 720:
        raise AssertionError("wrong orientation stabilizer/coset size")
    line_orbits = []
    remaining = set(range(27))
    while remaining:
        seed = min(remaining)
        orbit = {value[seed] for value in stabilizer}
        line_orbits.append(sorted(orbit))
        remaining -= orbit
    orbit_sizes = sorted(map(len, line_orbits))
    if orbit_sizes != [12, 15]:
        raise AssertionError("wrong U line orbits")
    u_fixed_double_sixes = [
        value
        for value in double_sixes
        if all(act(element, value) == value for element in stabilizer)
    ]
    if len(u_fixed_double_sixes) != 1:
        raise AssertionError("U fixes more than its defining double-six")
    # The map N_W(U)/U -> {U-fixed double-sixes}, nU |-> n(D), is bijective:
    # any U-fixed conjugate has a stabilizer containing U and both have order
    # 1440.  Thus this count is an exact self-normalizer certificate.
    normalizer_order = len(stabilizer) * len(u_fixed_double_sixes)

    # A standard marked-double-six presentation: adjacent S6 transpositions
    # and the central involution exchanging the two sixers.
    picard = [picard_matrix(root) for root in roots]
    standard_generators = picard[:5]
    switch_columns = [(5, -2, -2, -2, -2, -2, -2)]
    for index in range(6):
        column = [2] + [-1] * 6
        column[index + 1] = 0
        switch_columns.append(tuple(column))
    switch = Matrix(
        [[switch_columns[column][row] for column in range(7)] for row in range(7)]
    )
    if switch * switch != Matrix.eye(7):
        raise AssertionError("orientation switch is not an involution")
    if any(switch * value != value * switch for value in standard_generators):
        raise AssertionError("orientation switch is not central")
    line_index = {value: index for index, value in enumerate(lines)}
    s6_permutations = [Permutation(list(value)) for value in reflections[:5]]
    s6_group = PermutationGroup(s6_permutations)
    switch_permutation = Permutation(
        [line_index[apply_matrix(switch, value)] for value in lines]
    )
    full_stabilizer_group = PermutationGroup(s6_permutations + [switch_permutation])
    if int(s6_group.order()) != 720:
        raise AssertionError("adjacent-transposition subgroup is not S6")
    if switch_permutation.order() != 2 or switch_permutation.is_Identity:
        raise AssertionError("central switch is trivial or has wrong order")
    if s6_group.contains(switch_permutation):
        raise AssertionError("central switch lies in S6")
    if any(
        switch_permutation * value != value * switch_permutation
        for value in s6_permutations
    ):
        raise AssertionError("central switch fails to commute in line action")
    if int(full_stabilizer_group.order()) != 1440:
        raise AssertionError("S6 and central switch do not generate order 1440")
    switch_tuple = tuple(switch_permutation(index) for index in range(27))
    s6_fixes_both_sixers = all(
        act(generator, standard_first) == standard_first
        and act(generator, standard_second) == standard_second
        for generator in reflections[:5]
    )
    switch_exchanges_sixers = (
        act(switch_tuple, standard_first) == standard_second
        and act(switch_tuple, standard_second) == standard_first
    )
    generators_stabilize_chosen = s6_fixes_both_sixers and switch_exchanges_sixers
    if not generators_stabilize_chosen:
        raise AssertionError("standard generators do not stabilize/exchange the chosen sixers")
    # Generated subgroup is contained in the enumerated stabilizer by the
    # checks above and has the same order 1440; hence the groups are equal.
    generated_group_equals_enumerated_stabilizer = (
        int(full_stabilizer_group.order()) == len(stabilizer)
    )
    oriented_group_equals_S6 = int(s6_group.order()) == len(oriented)
    if not generated_group_equals_enumerated_stabilizer or not oriented_group_equals_S6:
        raise AssertionError("standard presentation does not equal the enumerated stabilizers")
    stabilizer_generators = standard_generators + [switch]
    h1_u, relation_rank_u, cocycle_kernel_rank_u = relation_h1(
        stabilizer_generators, coxeter=False
    )
    h1_w, relation_rank_w, cocycle_kernel_rank_w = relation_h1(
        picard, coxeter=True
    )
    if h1_u != [1, 1, 1, 1, 1, 2] or h1_w != [1, 1, 1, 1, 1, 1]:
        raise AssertionError("unexpected Picard H1 Smith diagonal")

    # Rebound the divisor-class calculation used after the determinant-defined
    # quartic is constructed.  For the adjacent S6 action, Pic^{S6} has the
    # saturated basis h and E=e1+...+e6.  The central switch acts by
    # h |-> 5h-2E and E |-> 12h-5E.
    h_class = Matrix([1, 0, 0, 0, 0, 0, 0])
    e_sum = Matrix([0, 1, 1, 1, 1, 1, 1])
    invariant_equations = Matrix.vstack(
        *(generator - Matrix.eye(7) for generator in standard_generators)
    )
    invariant_smith = smith_normal_form(invariant_equations, domain=ZZ)
    invariant_nonzero_smith = [
        abs(int(invariant_smith[i, i]))
        for i in range(min(invariant_smith.rows, invariant_smith.cols))
        if invariant_smith[i, i] != 0
    ]
    if invariant_equations.rank() != 5 or invariant_nonzero_smith != [1] * 5:
        raise AssertionError("S6 invariant lattice is not saturated of rank two")
    if invariant_equations * Matrix.hstack(h_class, e_sum) != Matrix.zeros(35, 2):
        raise AssertionError("h,E do not lie in Pic^S6")
    if switch * h_class != 5 * h_class - 2 * e_sum:
        raise AssertionError("wrong central action on h")
    if switch * e_sum != 12 * h_class - 5 * e_sum:
        raise AssertionError("wrong central action on E")
    hyperplane_class = 3 * h_class - e_sum
    d0 = e_sum - 2 * h_class
    divisor_class_a = e_sum - 2 * hyperplane_class
    if switch * d0 != -d0 or divisor_class_a != 3 * d0:
        raise AssertionError("anti-invariant divisor class identity failed")
    # In basis (h,E), columns of sigma-1 are -2*d0 and -6*d0,
    # hence the coboundary lattice is exactly 2 Z*d0.  Since a=3*d0,
    # its lattice class is nonzero modulo coboundaries.  The identification
    # of this lattice class with the cyclic-algebra residue class is a written
    # Hochschild--Serre bridge, not a machine-computed theorem.
    coboundary_multiples = [-2, -6]
    if abs(math.gcd(*coboundary_multiples)) != 2:
        raise AssertionError("wrong Pic^S6 coboundary lattice")
    class_a_nonzero_mod_coboundaries = 3 % 2 != 0

    canonical = {
        "status": "PASS",
        "W_E6_order": len(weyl),
        "double_six_action_image_order": image_order,
        "double_six_stabilizer_core_order": core_order,
        "double_six_count": len(double_sixes),
        "sixer_count": len(sixers),
        "stabilizer_order": len(stabilizer),
        "stabilizer_index": len(weyl) // len(stabilizer),
        "stabilizer_structure": "S6 x C2",
        "adjacent_S6_order": int(s6_group.order()),
        "central_swap_nontrivial": True,
        "central_swap_not_in_S6": True,
        "generated_S6_times_C2_order": int(full_stabilizer_group.order()),
        "standard_generators_stabilize_chosen_double_six": generators_stabilize_chosen,
        "adjacent_S6_fixes_each_sixer": s6_fixes_both_sixers,
        "central_swap_exchanges_the_two_sixers": switch_exchanges_sixers,
        "generated_group_equals_enumerated_stabilizer": generated_group_equals_enumerated_stabilizer,
        "oriented_group_equals_adjacent_S6": oriented_group_equals_S6,
        "U_fixed_double_six_count": len(u_fixed_double_sixes),
        "normalizer_order": normalizer_order,
        "self_normalizing": normalizer_order == len(stabilizer),
        "oriented_stabilizer_order": len(oriented),
        "orientation_swap_coset_size": len(swaps),
        "central_swap_order": 2,
        "central_swap_beta_sign": -1,
        "line_orbit_sizes": orbit_sizes,
        "H1_W_Pic_smith_diagonal": h1_w,
        "W_relation_rank": relation_rank_w,
        "W_cocycle_kernel_rank": cocycle_kernel_rank_w,
        "H1_W_Pic_torsion": [],
        "H1_U_Pic_smith_diagonal": h1_u,
        "U_relation_rank": relation_rank_u,
        "U_cocycle_kernel_rank": cocycle_kernel_rank_u,
        "H1_U_Pic_torsion": [2],
        "beta_definition": "sum_A(alpha)-sum_B(alpha)",
        "delta_definition": "beta^2",
        "beta_fixed_by_oriented_S6": s6_fixes_both_sixers,
        "beta_negated_by_central_swap": switch_exchanges_sixers,
        "same_double_six_coset_action": generated_group_equals_enumerated_stabilizer,
        "Pic_S6_invariant_basis": [
            [int(value) for value in h_class],
            [int(value) for value in e_sum],
        ],
        "Pic_S6_invariant_rank": 2,
        "Pic_S6_invariant_saturated": True,
        "central_swap_on_h_E_columns": [[5, -2], [12, -5]],
        "hyperplane_class_H_in_h_E": [3, -1],
        "anti_invariant_d0_in_h_E": [-2, 1],
        "central_swap_d0_sign": -1,
        "Pic_S6_coboundary_lattice": "2 Z*d0",
        "oriented_divisor_class_D_in_h_E": [-6, 3],
        "oriented_divisor_class_D_multiple_of_d0": 3,
        "oriented_divisor_class_D_nonzero_mod_coboundaries": class_a_nonzero_mod_coboundaries,
        "cyclic_class_map_proof_class": "WRITTEN_CLASS_MAP_BRIDGE_REQUIRED",
    }
    raw = json.dumps(canonical, sort_keys=True, separators=(",", ":")).encode()
    return canonical, sha256(raw).hexdigest()


def main() -> None:
    reject_optimized_python()
    value, digest = report()
    print(json.dumps(value, sort_keys=True, separators=(",", ":")))
    print("report_sha256", digest)


if __name__ == "__main__":
    main()
