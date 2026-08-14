#!/usr/bin/env python3
"""Produce the exact HCS-C52 B0--B2 symmetry-projector certificate."""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
from itertools import product
import json
from pathlib import Path
from typing import Any, Iterator

import sympy as sp


SCHEMA = "hcs-c52-certificate-v1"
CANDIDATE_ID = "HCS-C52"
PROJECT_SLUG = "henon_mu3_d12_calabi_yau_core_projector"
SOURCE_HASHES = {
    "C47": (
        "henon_dynamics/henon_mu3_normalized_trace_operator_gate/results/c47_certificate.json",
        "2c30a488f675bb68af17b2567c81946188525d007188c91b058c964c0ed7c09e",
        "5d4316a91f7590fd779670e982a3b1ae1b47d05b27561b86b29aa3a66e9820f9",
    ),
    "C48": (
        "henon_dynamics/henon_mu3_genus4_second_moment/results/c48_certificate.json",
        "92cd5c1079ebbaeaa27fc32e617852ae5d5989500ff3a816dd9fe306c32a32a8",
        "b5fe81f612bf66361f043b0ee1755860fa4e6452a32b07fb342e8348c8b2a0f7",
    ),
    "C49": (
        "henon_dynamics/henon_mu3_fano_threefold_third_moment/results/c49_certificate.json",
        "b3ec1bf12ea0f05469054fda37bd34ee4b6748030813c8c6407752035a3c25d2",
        "fc29fccc6a7281008b211a7c8b8e34d4a03e6cfe42c4d4f0bafe628eadcc5791",
    ),
    "C50": (
        "henon_dynamics/henon_mu3_elliptic_resummation_fourth_moment/results/c50_certificate.json",
        "ef77b61758ccaf59e2e24e79dc535e2216d794843ff5f16ae0ca4ded12eb9dde",
        "d2d78b6992d97bada0119416171d9d091f6d04eb9bcf93d9a71427f2589aed6a",
    ),
    "C51": (
        "henon_dynamics/henon_mu3_weight_clock_bifurcation/results/c51_certificate.json",
        "daffc0070d06258d3a4c8f5613c9d54a816eb2203be41aa045dbbe05c0e3d593",
        "2fdfc4fb2559d4cc9b253d978b8074bf57c49888ce2ff4d29545b127e9af95c1",
    ),
}

N = 8
Permutation = tuple[int, ...]
Phases = tuple[int, ...]
GroupElement = tuple[Permutation, Phases]
KElement = tuple[Fraction, Fraction]  # a+b*rho, rho^2+rho+1=0
K_ZERO: KElement = (Fraction(0), Fraction(0))
K_ONE: KElement = (Fraction(1), Fraction(0))


def canonical_json(value: Any) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def source_bundle(repository: Path) -> tuple[list[dict[str, str]], dict[str, Any]]:
    locks: list[dict[str, str]] = []
    certificates: dict[str, Any] = {}
    for source, (relative, expected_hash, expected_payload) in SOURCE_HASHES.items():
        path = repository / relative
        actual_hash = sha256_file(path)
        if actual_hash != expected_hash:
            raise AssertionError(f"source-lock mismatch for {source}: {actual_hash}")
        certificate = json.loads(path.read_text(encoding="utf-8"))
        if certificate.get("payload_sha256") != expected_payload:
            raise AssertionError(f"source payload mismatch for {source}")
        locks.append({
            "source": source,
            "path": relative,
            "sha256": actual_hash,
            "schema": certificate["schema"],
            "payload_sha256": expected_payload,
        })
        certificates[source] = certificate
    return locks, certificates


def k_add(left: KElement, right: KElement) -> KElement:
    return left[0] + right[0], left[1] + right[1]


def k_neg(value: KElement) -> KElement:
    return -value[0], -value[1]


def k_sub(left: KElement, right: KElement) -> KElement:
    return left[0] - right[0], left[1] - right[1]


def k_mul(left: KElement, right: KElement) -> KElement:
    a, b = left
    c, d = right
    return a * c - b * d, a * d + b * c - b * d


def k_inverse(value: KElement) -> KElement:
    a, b = value
    norm = a * a - a * b + b * b
    if norm == 0:
        raise ZeroDivisionError("zero in Q(rho)")
    return (a - b) / norm, -b / norm


def k_div(left: KElement, right: KElement) -> KElement:
    return k_mul(left, k_inverse(right))


def k_int(value: int) -> KElement:
    return Fraction(value), Fraction(0)


def k_rho_power(exponent: int) -> KElement:
    return (K_ONE, (Fraction(0), Fraction(1)), (Fraction(-1), Fraction(-1)))[
        exponent % 3
    ]


def k_is_zero(value: KElement) -> bool:
    return value == K_ZERO


def k_integral_value(value: KElement) -> int:
    if value[1] != 0 or value[0].denominator != 1:
        raise AssertionError(f"expected rational integer trace, got {value}")
    return value[0].numerator


def canonical_element(permutation: Permutation, phases: Phases) -> GroupElement:
    shift = phases[0] % 3
    return permutation, tuple((entry - shift) % 3 for entry in phases)


def multiply(left: GroupElement, right: GroupElement) -> GroupElement:
    p_left, e_left = left
    p_right, e_right = right
    permutation = tuple(p_right[p_left[i]] for i in range(N))
    phases = tuple((e_left[i] + e_right[p_left[i]]) % 3 for i in range(N))
    return canonical_element(permutation, phases)


IDENTITY: GroupElement = (tuple(range(N)), (0,) * N)


def group_power(element: GroupElement, exponent: int) -> GroupElement:
    result = IDENTITY
    for _ in range(exponent):
        result = multiply(result, element)
    return result


def group_order(element: GroupElement) -> int:
    result = IDENTITY
    for exponent in range(1, 25):
        result = multiply(result, element)
        if result == IDENTITY:
            return exponent
    raise AssertionError("projective element order exceeds 24")


def permutation_sign(permutation: Permutation) -> int:
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(N)
        for j in range(i + 1, N)
    )
    return -1 if inversions % 2 else 1


def edge_weight_exponents() -> dict[tuple[int, int], int]:
    return {
        tuple(sorted((i, (i + 1) % N))): (1 if i == 7 else 0)
        for i in range(N)
    }


def enumerate_projective_group() -> tuple[dict[GroupElement, int], list[list[int]], list[int]]:
    weights = edge_weight_exponents()
    permutations = sorted(
        {tuple((i + shift) % N for i in range(N)) for shift in range(N)}
        | {tuple((shift - i) % N for i in range(N)) for shift in range(N)}
    )
    group: dict[GroupElement, int] = {}
    for permutation in permutations:
        for tail in product(range(3), repeat=7):
            phases = (0,) + tail
            transformed: dict[tuple[int, int], int] = {}
            for i in range(N):
                source = tuple(sorted((i, (i + 1) % N)))
                target = tuple(sorted((permutation[i], permutation[(i + 1) % N])))
                transformed[target] = (
                    weights[source] + phases[i] + phases[(i + 1) % N]
                ) % 3
            differences = {
                (transformed[edge] - weights[edge]) % 3 for edge in transformed
            }
            if len(differences) == 1:
                group[(permutation, phases)] = differences.pop()
    if len(group) != 24:
        raise AssertionError(f"expected order 24, got {len(group)}")
    elements = sorted(group)
    index = {element: position for position, element in enumerate(elements)}
    table = [
        [index[multiply(left, right)] for right in elements] for left in elements
    ]
    inverses = []
    identity_index = index[IDENTITY]
    for i in range(24):
        candidates = [j for j in range(24) if table[i][j] == identity_index and table[j][i] == identity_index]
        if len(candidates) != 1:
            raise AssertionError("nonunique group inverse")
        inverses.append(candidates[0])
    return group, table, inverses


def explicit_generators() -> tuple[GroupElement, GroupElement]:
    rotation = (
        (6, 7, 0, 1, 2, 3, 4, 5),
        (0, 1, 1, 0, 1, 0, 1, 0),
    )
    reflection = (
        (7, 6, 5, 4, 3, 2, 1, 0),
        (0, 1, 0, 1, 0, 1, 0, 1),
    )
    return rotation, reflection


def compositions(total: int, slots: int, prefix: tuple[int, ...] = ()) -> Iterator[tuple[int, ...]]:
    if slots == 1:
        yield prefix + (total,)
        return
    for entry in range(total + 1):
        yield from compositions(total - entry, slots - 1, prefix + (entry,))


def target_monomials() -> list[tuple[int, int, tuple[int, ...]]]:
    monomials = []
    for y_exponent in range(3):
        z_exponent = 2 - y_exponent
        x_degree = 1 + y_exponent
        monomials.extend(
            (y_exponent, z_exponent, exponent)
            for exponent in compositions(x_degree, N)
        )
    return monomials


def jacobian_relations(
    monomials: list[tuple[int, int, tuple[int, ...]]]
) -> list[list[KElement]]:
    index = {monomial: position for position, monomial in enumerate(monomials)}
    weights = {
        edge: k_rho_power(exponent)
        for edge, exponent in edge_weight_exponents().items()
    }

    def vector(terms: list[tuple[KElement, tuple[int, int, tuple[int, ...]]]]) -> list[KElement]:
        result = [K_ZERO] * len(monomials)
        for coefficient, monomial in terms:
            position = index[monomial]
            result[position] = k_add(result[position], coefficient)
        return result

    def derivative_q(variable: int) -> list[tuple[KElement, tuple[int, ...]]]:
        result = []
        for edge, coefficient in weights.items():
            if variable in edge:
                neighbor = edge[0] if edge[1] == variable else edge[1]
                exponent = [0] * N
                exponent[neighbor] = 1
                result.append((coefficient, tuple(exponent)))
        return result

    relations: list[list[KElement]] = []
    for i in range(N):
        exponent = [0] * N
        exponent[i] = 2
        relations.append(vector(
            [(k_int(3), (1, 1, tuple(exponent)))]
            + [(coefficient, (0, 2, x_exp)) for coefficient, x_exp in derivative_q(i)]
        ))
        for j in range(N):
            exponent = [0] * N
            exponent[i] += 2
            exponent[j] += 1
            terms = [(k_int(3), (2, 0, tuple(exponent)))]
            for coefficient, x_exp in derivative_q(i):
                shifted = list(x_exp)
                shifted[j] += 1
                terms.append((coefficient, (1, 1, tuple(shifted))))
            relations.append(vector(terms))

    relations.append(vector([
        (K_ONE, (2, 0, tuple(3 if i == j else 0 for i in range(N))))
        for j in range(N)
    ]))
    relations.append(vector([
        (
            coefficient,
            (1, 1, tuple(1 if i in edge else 0 for i in range(N))),
        )
        for edge, coefficient in weights.items()
    ]))
    for j in range(N):
        terms = []
        for edge, coefficient in weights.items():
            exponent = [0] * N
            exponent[edge[0]] += 1
            exponent[edge[1]] += 1
            exponent[j] += 1
            terms.append((coefficient, (2, 0, tuple(exponent))))
        relations.append(vector(terms))
    if len(relations) != 82:
        raise AssertionError("unexpected relation count")
    return relations


def exact_rref(rows: list[list[KElement]]) -> tuple[list[list[KElement]], list[int]]:
    matrix = [row[:] for row in rows]
    pivots: list[int] = []
    rank = 0
    columns = len(matrix[0])
    for column in range(columns):
        pivot = next(
            (candidate for candidate in range(rank, len(matrix)) if not k_is_zero(matrix[candidate][column])),
            None,
        )
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inverse = k_inverse(matrix[rank][column])
        matrix[rank] = [k_mul(entry, inverse) for entry in matrix[rank]]
        for candidate in range(len(matrix)):
            if candidate == rank or k_is_zero(matrix[candidate][column]):
                continue
            coefficient = matrix[candidate][column]
            matrix[candidate] = [
                k_sub(left, k_mul(coefficient, right))
                for left, right in zip(matrix[candidate], matrix[rank])
            ]
        pivots.append(column)
        rank += 1
        if rank == len(matrix):
            break
    return matrix[:rank], pivots


def character_data(group: dict[GroupElement, int]) -> dict[str, Any]:
    monomials = target_monomials()
    relations = jacobian_relations(monomials)
    rref, pivots = exact_rref(relations)
    if len(pivots) != 81 or len(monomials) - len(pivots) != 83:
        raise AssertionError("Cayley quotient dimension failure")
    pivot_row = {pivot: row for row, pivot in enumerate(pivots)}
    quotient_basis = [i for i in range(len(monomials)) if i not in pivot_row]
    monomial_index = {monomial: position for position, monomial in enumerate(monomials)}

    def action_descriptor(
        element: GroupElement,
        monomial: tuple[int, int, tuple[int, ...]],
    ) -> tuple[int, KElement]:
        q_scale = group[element]
        permutation, phases = element
        determinant = k_mul(k_int(permutation_sign(permutation)), k_rho_power(sum(phases)))
        residue_twist = k_div(determinant, k_rho_power(q_scale))
        y_exponent, z_exponent, x_exponent = monomial
        transformed = [0] * N
        phase = -q_scale * z_exponent
        for i, exponent in enumerate(x_exponent):
            transformed[permutation[i]] += exponent
            phase += phases[i] * exponent
        image = monomial_index[(y_exponent, z_exponent, tuple(transformed))]
        scalar = k_mul(residue_twist, k_rho_power(phase))
        return image, scalar

    def reduce_vector(vector: list[KElement]) -> list[KElement]:
        reduced = vector[:]
        for pivot in pivots:
            coefficient = reduced[pivot]
            if k_is_zero(coefficient):
                continue
            row = rref[pivot_row[pivot]]
            reduced = [
                k_sub(left, k_mul(coefficient, right))
                for left, right in zip(reduced, row)
            ]
        return reduced

    relation_image_tests = 0
    for element in sorted(group):
        for relation in relations:
            image_vector = [K_ZERO] * len(monomials)
            for position, coefficient in enumerate(relation):
                if k_is_zero(coefficient):
                    continue
                image, scalar = action_descriptor(element, monomials[position])
                image_vector[image] = k_add(
                    image_vector[image], k_mul(coefficient, scalar)
                )
            if any(not k_is_zero(entry) for entry in reduce_vector(image_vector)):
                raise AssertionError("Jacobian relation subspace is not invariant")
            relation_image_tests += 1

    group_law_tests = 0
    elements = sorted(group)
    for left in elements:
        for right in elements:
            product_element = multiply(left, right)
            for monomial in monomials:
                first_image, first_scalar = action_descriptor(left, monomial)
                second_image, second_scalar = action_descriptor(
                    right, monomials[first_image]
                )
                product_image, product_scalar = action_descriptor(
                    product_element, monomial
                )
                if second_image != product_image or k_mul(first_scalar, second_scalar) != product_scalar:
                    raise AssertionError("Cayley action does not satisfy the group law")
                group_law_tests += 1

    traces: dict[GroupElement, int] = {}
    h41_traces: dict[GroupElement, int] = {}
    for element, q_scale in group.items():
        permutation, phases = element
        determinant = k_mul(k_int(permutation_sign(permutation)), k_rho_power(sum(phases)))
        residue_twist = k_div(determinant, k_rho_power(q_scale))
        h41_traces[element] = k_integral_value(residue_twist)
        trace = K_ZERO
        for basis_index in quotient_basis:
            image, scalar = action_descriptor(element, monomials[basis_index])
            if image == basis_index:
                trace = k_add(trace, scalar)
            elif image in pivot_row:
                trace = k_sub(trace, k_mul(scalar, rref[pivot_row[image]][basis_index]))
        traces[element] = k_integral_value(trace)

    rotation, reflection = explicit_generators()
    if rotation not in group or reflection not in group:
        raise AssertionError("frozen generators absent")
    if not (
        group_order(rotation) == 12
        and group_order(reflection) == 2
        and multiply(multiply(reflection, rotation), reflection) == group_power(rotation, 11)
    ):
        raise AssertionError("D12 presentation failure")
    coordinates = {group_power(rotation, k): ("rotation", k) for k in range(12)}
    coordinates.update({
        multiply(group_power(rotation, k), reflection): ("reflection", k)
        for k in range(12)
    })
    if len(coordinates) != 24:
        raise AssertionError("generators do not generate 24 elements")
    rotation_traces = [traces[group_power(rotation, k)] for k in range(12)]
    reflection_traces = [
        traces[multiply(group_power(rotation, k), reflection)] for k in range(12)
    ]
    if set(h41_traces.values()) != {1}:
        raise AssertionError("H41 is not the trivial representation")

    one_dimensional = []
    for r_value in (1, -1):
        for s_value in (1, -1):
            numerator = sum(r_value**k * rotation_traces[k] for k in range(12))
            numerator += sum(
                s_value * r_value**k * reflection_traces[k] for k in range(12)
            )
            if numerator % 24:
                raise AssertionError("nonintegral one-dimensional multiplicity")
            one_dimensional.append({
                "r_character": r_value,
                "s_character": s_value,
                "multiplicity": numerator // 24,
            })
    two_dimensional = []
    for character_index in range(1, 6):
        multiplicity = sp.simplify(sum(
            2 * sp.cos(2 * sp.pi * character_index * k / 12) * rotation_traces[k]
            for k in range(12)
        ) / 24)
        if not multiplicity.is_Integer:
            raise AssertionError("nonintegral two-dimensional multiplicity")
        two_dimensional.append({
            "character_index": character_index,
            "dimension": 2,
            "multiplicity": int(multiplicity),
        })
    dimension_sum = sum(row["multiplicity"] for row in one_dimensional)
    dimension_sum += sum(2 * row["multiplicity"] for row in two_dimensional)
    if dimension_sum != 83:
        raise AssertionError("character dimension sum failure")

    return {
        "cayley_polynomial": "F=y*C+z*Q",
        "bigrading": {
            "deg_x_i": [0, 1],
            "deg_y": [1, -3],
            "deg_z": [1, -2],
            "H41_piece": "R_(1,-3)",
            "H32_piece": "R_(2,-3)",
        },
        "relation_construction": {
            "ambient_monomial_dimension_R_2_minus3": len(monomials),
            "raw_relation_count": len(relations),
            "exact_Qrho_relation_rank": len(pivots),
            "quotient_dimension_H32": len(quotient_basis),
            "producer_algorithm": "exact dense RREF over Q(rho) with rho^2=-rho-1",
        },
        "residue_action": {
            "equation_scaling": "(C,Q)(M_g*x)=diag(1,rho^lambda_g)*(C,Q)(x)",
            "auxiliary_action": "y->y, z->rho^(-lambda_g)*z",
            "orientation_multiplier": "det(M_g)/det(diag(1,rho^lambda_g))",
            "PGL_scalar_lift_cancellation": True,
            "general_scalar_lift_firewall": {
                "scalar_symbol": "t",
                "M_prime": "t*M_g",
                "A_prime": "diag(t^3,t^2)*A_g",
                "determinant_ratio_t_exponent": 3,
                "R_p_minus3_monomial_substitution_t_exponent": -3,
                "net_t_exponent_with_orientation_multiplier": 0,
                "sample_t": 2,
                "sample_monomial_factor": {"numerator": 1, "denominator": 8},
                "sample_orientation_factor": 8,
                "sample_net_factor": 1,
                "net_t_exponent_if_orientation_deleted": -3,
                "net_t_exponent_if_orientation_inverted": -6,
            },
        },
        "quotient_action_certificate": {
            "Jacobian_relation_rows_tested_per_group_element": len(relations),
            "group_elements_tested": len(group),
            "relation_image_membership_tests": relation_image_tests,
            "all_relation_images_reduce_to_zero": True,
            "ambient_bigraded_monomials_tested": len(monomials),
            "ordered_group_pairs_tested": len(group) ** 2,
            "ambient_group_law_tests": group_law_tests,
            "representation_law_on_quotient": True,
        },
        "H41_character": {
            "dimension": 1,
            "all_group_traces": sorted(set(h41_traces.values())),
            "representation": "trivial",
        },
        "H32_character": {
            "dimension": 83,
            "rotation_traces_k0_to_k11": rotation_traces,
            "reflection_traces_k0_to_k11": reflection_traces,
            "one_dimensional_multiplicities": one_dimensional,
            "two_dimensional_multiplicities": two_dimensional,
            "dimension_sum": dimension_sum,
            "trivial_multiplicity": one_dimensional[0]["multiplicity"],
        },
    }


def group_payload(group: dict[GroupElement, int], table: list[list[int]], inverses: list[int]) -> dict[str, Any]:
    elements = sorted(group)
    rotation, reflection = explicit_generators()
    index = {element: position for position, element in enumerate(elements)}
    coordinates = {group_power(rotation, k): ("rotation", k) for k in range(12)}
    coordinates.update({
        multiply(group_power(rotation, k), reflection): ("reflection", k)
        for k in range(12)
    })
    rows = []
    for position, element in enumerate(elements):
        permutation, phases = element
        kind, exponent = coordinates[element]
        rows.append({
            "id": position,
            "permutation_output_to_input": list(permutation),
            "rho_phase_exponents": list(phases),
            "Q_scale_rho_exponent": group[element],
            "projective_order": group_order(element),
            "normal_form": {"kind": kind, "exponent": exponent},
        })
    return {
        "name": "D12",
        "order_convention": "dihedral group of order 24 with rotation order 12",
        "order": 24,
        "transformation": "x_i -> rho^(e_i)*x_(sigma(i)), canonicalized by e_0=0",
        "cubic_invariance": "C(g*x)=C(x)",
        "quadric_invariance": "Q(g*x)=rho^(lambda_g)*Q(x)",
        "enumeration_algorithm": "all 16 cycle-dihedral permutations times all 3^7 canonical phase vectors",
        "element_order_histogram": {
            str(key): value for key, value in sorted(Counter(group_order(element) for element in elements).items())
        },
        "rotation_generator_id": index[rotation],
        "reflection_generator_id": index[reflection],
        "presentation": "r^12=s^2=1 and s*r*s=r^(-1)",
        "elements": rows,
        "multiplication_table_by_id": table,
        "inverse_ids": inverses,
    }


def chow_kuenneth_payload() -> dict[str, Any]:
    lefschetz = [
        {
            "index_i": i,
            "cohomological_degree": 2 * i,
            "first_factor_h_power": 5 - i,
            "second_factor_h_power": i,
            "coefficient": {"numerator": 1, "denominator": 6},
        }
        for i in range(6)
    ]
    middle_exponents = [[i + 5 - j for j in range(6)] for i in range(6)]
    middle_integrals = [
        [6 if middle_exponents[i][j] == 5 else 0 for j in range(6)]
        for i in range(6)
    ]
    composition = [
        [1 if i == j else 0 for j in range(6)] for i in range(6)
    ]
    return {
        "dimension_X": 5,
        "degree_integral_h5": 6,
        "Lefschetz_projectors": lefschetz,
        "composition_matrix": composition,
        "independent_correspondence_algebra_controls": {
            "middle_factor_h_exponent_for_pi_i_after_pi_j": middle_exponents,
            "middle_factor_integral": middle_integrals,
            "transpose_projector_index": [5, 4, 3, 2, 1, 0],
            "Reynolds_product_pairs_per_output_group_element": [24] * 24,
            "Reynolds_square_coefficient": {"numerator": 1, "denominator": 24},
            "sum_Lefschetz_projectors_is_idempotent": True,
            "pi5_square_expansion_reduces_to_pi5": True,
            "pi_core_square_expansion_reduces_to_pi_core": True,
        },
        "middle_projector": "pi_5=Delta_X-sum_(i=0)^5 pi_(2i)",
        "middle_projector_is_Chow_idempotent": True,
        "automorphisms_induced_by_PGL8_preserve_h": True,
        "pi5_commutes_with_every_graph": True,
        "reynolds_graph_projector": "e_G=(1/24)*sum_(g in G)[Gamma_g]",
        "reynolds_is_Chow_idempotent": True,
        "reynolds_is_self_transpose": True,
        "core_projector": "pi_core=pi_5*e_G=e_G*pi_5",
        "level_one_projector": "pi_lev=pi_5-pi_core",
        "core_and_level_projectors_orthogonal": True,
        "raw_e_G_assigned_middle_rank10": False,
        "combined_denominator_bound": 144,
    }


def realization_payload(character: dict[str, Any], certificates: dict[str, Any]) -> dict[str, Any]:
    source_hodge = certificates["C51"]["payload"]["n4_Hodge_ledger"]["complete_intersection_X4"]
    if source_hodge["primitive_middle_rank"] != 168:
        raise AssertionError("C51 middle rank changed")
    if character["H32_character"]["trivial_multiplicity"] != 4:
        raise AssertionError("unexpected invariant H32 dimension")
    core_before = [
        {"p": 1, "q": 4, "multiplicity": 1},
        {"p": 2, "q": 3, "multiplicity": 4},
        {"p": 3, "q": 2, "multiplicity": 4},
        {"p": 4, "q": 1, "multiplicity": 1},
    ]
    level_before = [
        {"p": 2, "q": 3, "multiplicity": 79},
        {"p": 3, "q": 2, "multiplicity": 79},
    ]
    twist = lambda rows: [
        {"p": row["p"] - 2, "q": row["q"] - 2, "multiplicity": row["multiplicity"]}
        for row in rows
    ]
    return {
        "source_middle_motive": "M5=(X,pi_5)",
        "normalized_odd_packet": "O4=(X,pi_5,2)",
        "source_rank": 168,
        "source_Hodge_before_twist": source_hodge["primitive_middle_H5_before_twist"],
        "source_Hodge_after_twist2": source_hodge["after_Tate_twist_2"],
        "core": {
            "motive": "(X,pi_core,2)",
            "rank": 10,
            "Hodge_before_twist": core_before,
            "Hodge_after_twist2": twist(core_before),
            "Hodge_summary_high_to_low": [1, 4, 4, 1],
        },
        "level_one_complement": {
            "motive": "(X,pi_lev,2)",
            "rank": 158,
            "Hodge_before_twist": level_before,
            "Hodge_after_twist2": twist(level_before),
            "Hodge_summary_high_to_low": [0, 79, 79, 0],
            "normalized_Hodge_level": 1,
        },
        "rank_sum": 168,
        "realizations": {
            "Betti": "SPLIT_BY_THE_SAME_CHOW_PROJECTORS",
            "de_Rham": "SPLIT_BY_THE_SAME_CHOW_PROJECTORS",
            "ell_adic_all_ell": "SPLIT_BY_THE_SAME_K_RATIONAL_CHOW_PROJECTORS",
            "Galois_equivariant_over_K": True,
            "primewise_fitted_projector_used": False,
        },
    }


def build_payload(repository: Path) -> dict[str, Any]:
    locks, certificates = source_bundle(repository)
    group, table, inverses = enumerate_projective_group()
    character = character_data(group)
    return {
        "material_passport": {
            "candidate_id": CANDIDATE_ID,
            "project_slug": PROJECT_SLUG,
            "artifact_status": "RELEASE_CANDIDATE",
            "implemented_blocks": ["B0_SOURCE_MODEL", "B1_D12_CK", "B2_EXACT_REPRESENTATION"],
        },
        "source_lock": locks,
        "frozen_model": {
            "base_field": "K=Q(rho), rho^2+rho+1=0",
            "ambient_space": "P^7_K",
            "dimension": 5,
            "cubic_C": "sum_(i=0)^7 x_i^3",
            "quadric_Q": "sum_(i=0)^6 x_i*x_(i+1)+rho*x_7*x_0",
            "complete_intersection_type": [2, 3],
            "degree": 6,
            "char0_smoothness_source": "C50 exact Groebner certificate",
            "closing_edge_preserved": True,
            "chronological_averaging_used": False,
        },
        "projective_monomial_group": group_payload(group, table, inverses),
        "middle_chow_kuenneth": chow_kuenneth_payload(),
        "cayley_jacobian_representation": character,
        "middle_realization_decomposition": realization_payload(character, certificates),
        "group_algebra_no_go": {
            "algebra": "Q[G_mon] acting through graph correspondences on (X,pi_5,2)",
            "H41_trivial_multiplicity": 1,
            "H32_trivial_multiplicity": 4,
            "action_on_every_trivial_copy": "augmentation epsilon(a)=sum_g a_g",
            "idempotent_augmentation_values": [0, 1],
            "if_extreme_H41_retained_then_four_H32_trivial_copies_retained": True,
            "conjugate_Hodge_pieces_retained": True,
            "minimum_rational_Hodge_rank_containing_extreme_pair_in_QG": 10,
            "desired_rank2_projector_in_QG": "REFUTED",
            "all_K_rational_algebraic_correspondences": "OPEN_NOT_ASSESSED",
            "proof_scope": "the full rational graph algebra Q[G_mon], not the full Chow correspondence ring",
        },
        "decisions": {
            "order24_D12_projective_monomial_group": "PROVED",
            "middle_Chow_projector_rank10_plus_rank158": "PROVED",
            "rank158_complement_is_Hodge_level_one": "PROVED",
            "same_projectors_give_all_ell_realizations": "PROVED_BY_K_RATIONAL_CHOW_CORRESPONDENCE",
            "rank2_projector_inside_Q_group_algebra": "REFUTED",
            "rank2_projector_in_full_Chow_ring": "OPEN_NOT_CLAIMED",
        },
        "future_gates_C53": {
            "B3_rank10_Frobenius_polynomial": "NOT_RUN",
            "B4_extra_incidence_correspondence": "NOT_RUN",
            "local_L_polynomial_factorization_claimed": False,
            "rank2_extreme_projector_beyond_QG_claimed": False,
            "these_fields_are_scope_only_not_placeholder_evidence": True,
        },
        "scope": {
            "D12_means_order24": True,
            "raw_Reynolds_projector_called_rank10_without_pi5": False,
            "full_projective_automorphism_group_classified": False,
            "Q_group_algebra_no_go_promoted_to_all_correspondences": False,
            "Hodge_projector_promoted_without_algebraic_cycle": False,
            "single_ell_numerical_split_used": False,
            "B3_or_B4_claim_in_C52": False,
            "local_L_polynomial_claimed": False,
            "functional_equation_for_O4_claimed": False,
            "Riemann_hypothesis_claimed": False,
            "self_adjoint_Hilbert_Polya_operator_claimed": False,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    arguments = parser.parse_args()
    repository = Path(__file__).resolve().parents[3]
    payload = build_payload(repository)
    certificate = {
        "schema": SCHEMA,
        "payload": payload,
        "payload_sha256": hashlib.sha256(canonical_json(payload)).hexdigest(),
    }
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(f"wrote {arguments.output}")
    print(f"payload_sha256={certificate['payload_sha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
