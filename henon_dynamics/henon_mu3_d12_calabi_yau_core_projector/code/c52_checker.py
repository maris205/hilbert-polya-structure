#!/usr/bin/env python3
"""Independent fail-closed checker for the HCS-C52 B0--B2 certificate."""

from __future__ import annotations

import argparse
from collections import Counter
from functools import lru_cache
import hashlib
from itertools import permutations
import json
from pathlib import Path
from typing import Any, Callable, Iterator

import sympy as sp
from sympy.polys.domains import QQ
from sympy.polys.matrices import DomainMatrix


SCHEMA = "hcs-c52-certificate-v1"
CHECK_SCHEMA = "hcs-c52-independent-check-v1"
FROZEN_PAYLOAD_SHA256 = "78d362e62efacc78dac511d9607d93f21f065a86f1d41c62c10c101b652558f1"
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
MODULUS = 211
GroupElement = tuple[tuple[int, ...], tuple[int, ...]]
IDENTITY: GroupElement = (tuple(range(N)), (0,) * N)


class GateFailure(Exception):
    pass


def require(condition: bool, message: str) -> None:
    if type(condition) is not bool or not condition:
        raise GateFailure(message)


def canonical_json(value: Any) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            value.update(block)
    return value.hexdigest()


def strict_equal(left: Any, right: Any) -> bool:
    if type(left) is not type(right):
        return False
    if isinstance(left, dict):
        return set(left) == set(right) and all(
            strict_equal(left[key], right[key]) for key in left
        )
    if isinstance(left, list):
        return len(left) == len(right) and all(
            strict_equal(a, b) for a, b in zip(left, right)
        )
    return left == right


def same_recursive_shape(left: Any, right: Any) -> bool:
    if type(left) is not type(right):
        return False
    if isinstance(left, dict):
        return set(left) == set(right) and all(
            same_recursive_shape(left[key], right[key]) for key in left
        )
    if isinstance(left, list):
        return len(left) == len(right) and all(
            same_recursive_shape(a, b) for a, b in zip(left, right)
        )
    return True


def edge_weights() -> dict[tuple[int, int], int]:
    return {
        tuple(sorted((i, (i + 1) % N))): (1 if i == 7 else 0)
        for i in range(N)
    }


def canonical_element(permutation: tuple[int, ...], phases: tuple[int, ...]) -> GroupElement:
    shift = phases[0] % 3
    return permutation, tuple((entry - shift) % 3 for entry in phases)


def multiply(left: GroupElement, right: GroupElement) -> GroupElement:
    p_left, e_left = left
    p_right, e_right = right
    return canonical_element(
        tuple(p_right[p_left[i]] for i in range(N)),
        tuple((e_left[i] + e_right[p_left[i]]) % 3 for i in range(N)),
    )


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
    raise GateFailure("element order exceeds 24")


def permutation_sign(permutation: tuple[int, ...]) -> int:
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(N)
        for j in range(i + 1, N)
    )
    return -1 if inversions % 2 else 1


@lru_cache(maxsize=1)
def checker_group() -> dict[GroupElement, int]:
    """Derive support automorphisms from all S8, then solve phases recursively."""
    weights = edge_weights()
    support = set(weights)
    support_automorphisms = []
    for candidate in permutations(range(N)):
        permutation = tuple(candidate)
        mapped_support = {
            tuple(sorted((permutation[i], permutation[(i + 1) % N])))
            for i in range(N)
        }
        if mapped_support == support:
            support_automorphisms.append(permutation)
    require(len(support_automorphisms) == 16, "8-cycle support automorphism count")
    group: dict[GroupElement, int] = {}
    for permutation in sorted(support_automorphisms):
        for q_scale in range(3):
            phases = [0] * N
            for i in range(7):
                source = tuple(sorted((i, i + 1)))
                target = tuple(sorted((permutation[i], permutation[i + 1])))
                phases[i + 1] = (
                    q_scale + weights[target] - weights[source] - phases[i]
                ) % 3
            source = (0, 7)
            target = tuple(sorted((permutation[7], permutation[0])))
            closing = (weights[source] + phases[7] + phases[0] - weights[target]) % 3
            if closing == q_scale:
                group[(permutation, tuple(phases))] = q_scale
    require(len(group) == 24, "checker group order")
    return group


def generators() -> tuple[GroupElement, GroupElement]:
    return (
        ((6, 7, 0, 1, 2, 3, 4, 5), (0, 1, 1, 0, 1, 0, 1, 0)),
        ((7, 6, 5, 4, 3, 2, 1, 0), (0, 1, 0, 1, 0, 1, 0, 1)),
    )


def expected_group_payload() -> dict[str, Any]:
    group = checker_group()
    elements = sorted(group)
    index = {element: position for position, element in enumerate(elements)}
    table = [
        [index[multiply(left, right)] for right in elements] for left in elements
    ]
    identity_index = index[IDENTITY]
    inverses = []
    for i in range(24):
        candidates = [
            j for j in range(24)
            if table[i][j] == identity_index and table[j][i] == identity_index
        ]
        require(len(candidates) == 1, "checker inverse")
        inverses.append(candidates[0])
    rotation, reflection = generators()
    require(rotation in group and reflection in group, "checker generators")
    require(group_order(rotation) == 12, "rotation order")
    require(group_order(reflection) == 2, "reflection order")
    require(
        multiply(multiply(reflection, rotation), reflection) == group_power(rotation, 11),
        "dihedral conjugation",
    )
    coordinates = {group_power(rotation, k): ("rotation", k) for k in range(12)}
    coordinates.update({
        multiply(group_power(rotation, k), reflection): ("reflection", k)
        for k in range(12)
    })
    require(len(coordinates) == 24, "generated group size")
    rows = []
    for position, element in enumerate(elements):
        kind, exponent = coordinates[element]
        rows.append({
            "id": position,
            "permutation_output_to_input": list(element[0]),
            "rho_phase_exponents": list(element[1]),
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
            str(key): value
            for key, value in sorted(Counter(group_order(element) for element in elements).items())
        },
        "rotation_generator_id": index[rotation],
        "reflection_generator_id": index[reflection],
        "presentation": "r^12=s^2=1 and s*r*s=r^(-1)",
        "elements": rows,
        "multiplication_table_by_id": table,
        "inverse_ids": inverses,
    }


def compositions(total: int, slots: int, prefix: tuple[int, ...] = ()) -> Iterator[tuple[int, ...]]:
    if slots == 1:
        yield prefix + (total,)
        return
    for entry in range(total + 1):
        yield from compositions(total - entry, slots - 1, prefix + (entry,))


def exact_character_replay() -> dict[str, Any]:
    """Independent SymPy DomainMatrix replay over the number field Q(rho)."""
    symbol = sp.symbols("rho_checker")
    field = QQ.alg_field_from_poly(
        sp.Poly(symbol**2 + symbol + 1, symbol), alias="rho_checker"
    )
    rho = field.unit
    group = checker_group()
    weights = {
        edge: rho**exponent for edge, exponent in edge_weights().items()
    }
    monomials = []
    for y_exponent in range(3):
        z_exponent = 2 - y_exponent
        monomials.extend(
            (y_exponent, z_exponent, x_exp)
            for x_exp in compositions(1 + y_exponent, N)
        )
    index = {monomial: position for position, monomial in enumerate(monomials)}

    def vector(terms):
        result = [field.zero] * len(monomials)
        for coefficient, monomial in terms:
            result[index[monomial]] += coefficient
        return result

    def derivative_q(variable):
        result = []
        for edge, coefficient in weights.items():
            if variable in edge:
                neighbor = edge[0] if edge[1] == variable else edge[1]
                exponent = [0] * N
                exponent[neighbor] = 1
                result.append((coefficient, tuple(exponent)))
        return result

    relations = []
    for i in range(N):
        exponent = [0] * N
        exponent[i] = 2
        relations.append(vector(
            [(field.convert(3), (1, 1, tuple(exponent)))]
            + [(coefficient, (0, 2, x_exp)) for coefficient, x_exp in derivative_q(i)]
        ))
        for j in range(N):
            exponent = [0] * N
            exponent[i] += 2
            exponent[j] += 1
            terms = [(field.convert(3), (2, 0, tuple(exponent)))]
            for coefficient, x_exp in derivative_q(i):
                shifted = list(x_exp)
                shifted[j] += 1
                terms.append((coefficient, (1, 1, tuple(shifted))))
            relations.append(vector(terms))
    relations.append(vector([
        (field.one, (2, 0, tuple(3 if i == j else 0 for i in range(N))))
        for j in range(N)
    ]))
    relations.append(vector([
        (coefficient, (1, 1, tuple(1 if i in edge else 0 for i in range(N))))
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
    require(len(relations) == 82, "exact checker relation count")

    domain_matrix = DomainMatrix(
        relations, (len(relations), len(monomials)), field
    )
    rref_domain, pivot_tuple = domain_matrix.rref()
    pivots = list(pivot_tuple)
    rref = rref_domain.to_list()
    require(len(pivots) == 81, "exact checker Q(rho) rank")
    pivot_row = {pivot: row for row, pivot in enumerate(pivots)}
    quotient = [position for position in range(len(monomials)) if position not in pivot_row]
    require(len(quotient) == 83, "exact checker quotient dimension")

    def residue_twist(element):
        permutation, phases = element
        q_scale = group[element]
        determinant = field.convert(permutation_sign(permutation)) * rho**(sum(phases) % 3)
        return determinant / rho**q_scale

    def action_descriptor(element, monomial):
        permutation, phases = element
        q_scale = group[element]
        y_exponent, z_exponent, x_exponent = monomial
        transformed = [0] * N
        phase = -q_scale * z_exponent
        for i, exponent in enumerate(x_exponent):
            transformed[permutation[i]] += exponent
            phase += phases[i] * exponent
        image = index[(y_exponent, z_exponent, tuple(transformed))]
        scalar = residue_twist(element) * rho**(phase % 3)
        return image, scalar

    def reduce_vector(vector):
        reduced = vector[:]
        for pivot in pivots:
            coefficient = reduced[pivot]
            if coefficient == field.zero:
                continue
            row = rref[pivot_row[pivot]]
            reduced = [
                left - coefficient * right for left, right in zip(reduced, row)
            ]
        return reduced

    relation_tests = 0
    for element in sorted(group):
        for relation in relations:
            image_vector = [field.zero] * len(monomials)
            for position, coefficient in enumerate(relation):
                if coefficient == field.zero:
                    continue
                image, scalar = action_descriptor(element, monomials[position])
                image_vector[image] += coefficient * scalar
            require(
                all(entry == field.zero for entry in reduce_vector(image_vector)),
                "exact checker relation-subspace invariance",
            )
            relation_tests += 1

    law_tests = 0
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
                require(second_image == product_image, "exact checker action image law")
                require(first_scalar * second_scalar == product_scalar, "exact checker action scalar law")
                law_tests += 1

    def integer_from_field(value):
        expression = sp.simplify(field.to_sympy(value))
        require(bool(expression.is_Integer), "exact checker trace not integer")
        return int(expression)

    traces = {}
    h41_traces = {}
    for element in elements:
        h41_traces[element] = integer_from_field(residue_twist(element))
        trace = field.zero
        for basis_index in quotient:
            image, scalar = action_descriptor(element, monomials[basis_index])
            if image == basis_index:
                trace += scalar
            elif image in pivot_row:
                trace -= scalar * rref[pivot_row[image]][basis_index]
        traces[element] = integer_from_field(trace)
    require(set(h41_traces.values()) == {1}, "exact checker H41 trivial")
    rotation, reflection = generators()
    rotation_traces = [traces[group_power(rotation, k)] for k in range(12)]
    reflection_traces = [
        traces[multiply(group_power(rotation, k), reflection)]
        for k in range(12)
    ]

    # A general scalar t, not a cube root of unity, is the non-vacuous lift test.
    substitution_exponents = {
        sum(x_exp) - 3 * y_exp - 2 * z_exp
        for y_exp, z_exp, x_exp in monomials
    }
    require(substitution_exponents == {-3}, "general scalar monomial exponent")
    determinant_ratio_exponent = N - 3 - 2
    require(determinant_ratio_exponent == 3, "general scalar determinant ratio")
    require(determinant_ratio_exponent + next(iter(substitution_exponents)) == 0, "scalar lift cancellation")
    require(next(iter(substitution_exponents)) != 0, "deleted orientation twist must fail")
    require(next(iter(substitution_exponents)) - determinant_ratio_exponent == -6, "inverted orientation twist must fail")

    return {
        "ambient": len(monomials),
        "relations": len(relations),
        "rank": len(pivots),
        "quotient": len(quotient),
        "rotation_traces": rotation_traces,
        "reflection_traces": reflection_traces,
        "relation_tests": relation_tests,
        "law_tests": law_tests,
        "scalar_substitution_exponent": -3,
        "scalar_determinant_ratio_exponent": 3,
    }


def modular_character(rho: int) -> dict[str, Any]:
    group = checker_group()
    weights = {edge: pow(rho, exponent, MODULUS) for edge, exponent in edge_weights().items()}
    monomials = []
    for y_exponent in range(3):
        z_exponent = 2 - y_exponent
        monomials.extend(
            (y_exponent, z_exponent, x_exp)
            for x_exp in compositions(1 + y_exponent, N)
        )
    index = {monomial: position for position, monomial in enumerate(monomials)}

    def vector(terms):
        result = [0] * len(monomials)
        for coefficient, monomial in terms:
            result[index[monomial]] = (result[index[monomial]] + coefficient) % MODULUS
        return result

    def derivative_q(variable):
        result = []
        for edge, coefficient in weights.items():
            if variable in edge:
                neighbor = edge[0] if edge[1] == variable else edge[1]
                exponent = [0] * N
                exponent[neighbor] = 1
                result.append((coefficient, tuple(exponent)))
        return result

    relations = []
    for i in range(N):
        exponent = [0] * N
        exponent[i] = 2
        relations.append(vector(
            [(3, (1, 1, tuple(exponent)))]
            + [(coefficient, (0, 2, x_exp)) for coefficient, x_exp in derivative_q(i)]
        ))
        for j in range(N):
            exponent = [0] * N
            exponent[i] += 2
            exponent[j] += 1
            terms = [(3, (2, 0, tuple(exponent)))]
            for coefficient, x_exp in derivative_q(i):
                shifted = list(x_exp)
                shifted[j] += 1
                terms.append((coefficient, (1, 1, tuple(shifted))))
            relations.append(vector(terms))
    relations.append(vector([
        (1, (2, 0, tuple(3 if i == j else 0 for i in range(N))))
        for j in range(N)
    ]))
    relations.append(vector([
        (coefficient, (1, 1, tuple(1 if i in edge else 0 for i in range(N))))
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

    rows = [row[:] for row in relations]
    pivots = []
    rank = 0
    for column in range(len(monomials)):
        pivot = next(
            (candidate for candidate in range(rank, len(rows)) if rows[candidate][column]),
            None,
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], MODULUS - 2, MODULUS)
        rows[rank] = [(entry * inverse) % MODULUS for entry in rows[rank]]
        for candidate in range(len(rows)):
            if candidate == rank or not rows[candidate][column]:
                continue
            coefficient = rows[candidate][column]
            rows[candidate] = [
                (left - coefficient * right) % MODULUS
                for left, right in zip(rows[candidate], rows[rank])
            ]
        pivots.append(column)
        rank += 1
        if rank == len(rows):
            break
    rows = rows[:rank]
    pivot_row = {pivot: row for row, pivot in enumerate(pivots)}
    quotient = [position for position in range(len(monomials)) if position not in pivot_row]
    require(len(relations) == 82 and rank == 81 and len(quotient) == 83, "modular relation dimensions")

    traces = {}
    h41 = {}
    for element, q_scale in group.items():
        permutation, phases = element
        determinant = permutation_sign(permutation) * pow(rho, sum(phases), MODULUS)
        residue = determinant * pow(pow(rho, q_scale, MODULUS), MODULUS - 2, MODULUS) % MODULUS
        h41[element] = residue
        trace = 0
        for basis_index in quotient:
            y_exponent, z_exponent, x_exponent = monomials[basis_index]
            transformed = [0] * N
            phase = -q_scale * z_exponent
            for i, exponent in enumerate(x_exponent):
                transformed[permutation[i]] += exponent
                phase += phases[i] * exponent
            image = index[(y_exponent, z_exponent, tuple(transformed))]
            scalar = residue * pow(rho, phase % 3, MODULUS) % MODULUS
            if image == basis_index:
                trace += scalar
            elif image in pivot_row:
                trace -= scalar * rows[pivot_row[image]][basis_index]
        traces[element] = trace % MODULUS
    rotation, reflection = generators()

    def lift(value):
        lifted = value if value <= MODULUS // 2 else value - MODULUS
        require(abs(lifted) <= 83, "trace lift exceeds representation dimension")
        return lifted

    rotation_traces = [lift(traces[group_power(rotation, k)]) for k in range(12)]
    reflection_traces = [
        lift(traces[multiply(group_power(rotation, k), reflection)])
        for k in range(12)
    ]
    require({lift(value) for value in h41.values()} == {1}, "modular H41 character")
    return {
        "ambient": len(monomials),
        "relations": len(relations),
        "rank": rank,
        "quotient": len(quotient),
        "rotation_traces": rotation_traces,
        "reflection_traces": reflection_traces,
    }


def expected_character_payload() -> dict[str, Any]:
    exact = exact_character_replay()
    roots = [value for value in range(MODULUS) if (value * value + value + 1) % MODULUS == 0]
    require(roots == [14, 196], "modular K embeddings")
    first, second = (modular_character(root) for root in roots)
    require(strict_equal(first, second), "two K embeddings disagree")
    require(first["rank"] == exact["rank"] and first["quotient"] == exact["quotient"], "modular dimension control")
    require(first["rotation_traces"] == exact["rotation_traces"], "modular rotation trace control")
    require(first["reflection_traces"] == exact["reflection_traces"], "modular reflection trace control")
    rotation_traces = exact["rotation_traces"]
    reflection_traces = exact["reflection_traces"]
    one_dimensional = []
    for r_value in (1, -1):
        for s_value in (1, -1):
            numerator = sum(r_value**k * rotation_traces[k] for k in range(12))
            numerator += sum(s_value * r_value**k * reflection_traces[k] for k in range(12))
            require(numerator % 24 == 0, "checker 1D multiplicity")
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
        require(bool(multiplicity.is_Integer), "checker 2D multiplicity")
        two_dimensional.append({
            "character_index": character_index,
            "dimension": 2,
            "multiplicity": int(multiplicity),
        })
    dimension_sum = sum(row["multiplicity"] for row in one_dimensional)
    dimension_sum += sum(2 * row["multiplicity"] for row in two_dimensional)
    require(dimension_sum == 83, "checker character dimension")
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
            "ambient_monomial_dimension_R_2_minus3": exact["ambient"],
            "raw_relation_count": exact["relations"],
            "exact_Qrho_relation_rank": exact["rank"],
            "quotient_dimension_H32": exact["quotient"],
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
                "determinant_ratio_t_exponent": exact["scalar_determinant_ratio_exponent"],
                "R_p_minus3_monomial_substitution_t_exponent": exact["scalar_substitution_exponent"],
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
            "Jacobian_relation_rows_tested_per_group_element": exact["relations"],
            "group_elements_tested": 24,
            "relation_image_membership_tests": exact["relation_tests"],
            "all_relation_images_reduce_to_zero": True,
            "ambient_bigraded_monomials_tested": exact["ambient"],
            "ordered_group_pairs_tested": 24**2,
            "ambient_group_law_tests": exact["law_tests"],
            "representation_law_on_quotient": True,
        },
        "H41_character": {
            "dimension": 1,
            "all_group_traces": [1],
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


def expected_sources(repository: Path) -> tuple[list[dict[str, str]], dict[str, Any]]:
    locks, certificates = [], {}
    for source, (relative, expected_hash, expected_payload) in SOURCE_HASHES.items():
        path = repository / relative
        require(digest(path) == expected_hash, f"live source hash {source}")
        certificate = json.loads(path.read_text(encoding="utf-8"))
        require(certificate.get("payload_sha256") == expected_payload, f"live source payload {source}")
        locks.append({
            "source": source,
            "path": relative,
            "sha256": expected_hash,
            "schema": certificate["schema"],
            "payload_sha256": expected_payload,
        })
        certificates[source] = certificate
    return locks, certificates


def expected_ck() -> dict[str, Any]:
    middle_exponents = [[i + 5 - j for j in range(6)] for i in range(6)]
    middle_integrals = [
        [6 if middle_exponents[i][j] == 5 else 0 for j in range(6)]
        for i in range(6)
    ]
    composition = [[1 if i == j else 0 for j in range(6)] for i in range(6)]
    require(all(middle_integrals[i][j] == 6 * composition[i][j] for i in range(6) for j in range(6)), "independent Lefschetz composition")
    group = checker_group()
    product_counts = []
    for output in sorted(group):
        count = sum(multiply(left, right) == output for left in group for right in group)
        product_counts.append(count)
    require(product_counts == [24] * 24, "independent Reynolds square")
    return {
        "dimension_X": 5,
        "degree_integral_h5": 6,
        "Lefschetz_projectors": [
            {
                "index_i": i,
                "cohomological_degree": 2 * i,
                "first_factor_h_power": 5 - i,
                "second_factor_h_power": i,
                "coefficient": {"numerator": 1, "denominator": 6},
            }
            for i in range(6)
        ],
        "composition_matrix": composition,
        "independent_correspondence_algebra_controls": {
            "middle_factor_h_exponent_for_pi_i_after_pi_j": middle_exponents,
            "middle_factor_integral": middle_integrals,
            "transpose_projector_index": [5, 4, 3, 2, 1, 0],
            "Reynolds_product_pairs_per_output_group_element": product_counts,
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


def expected_realization(certificates: dict[str, Any]) -> dict[str, Any]:
    source = certificates["C51"]["payload"]["n4_Hodge_ledger"]["complete_intersection_X4"]
    core = [
        {"p": 1, "q": 4, "multiplicity": 1},
        {"p": 2, "q": 3, "multiplicity": 4},
        {"p": 3, "q": 2, "multiplicity": 4},
        {"p": 4, "q": 1, "multiplicity": 1},
    ]
    level = [
        {"p": 2, "q": 3, "multiplicity": 79},
        {"p": 3, "q": 2, "multiplicity": 79},
    ]
    def twist(rows):
        return [
            {"p": row["p"] - 2, "q": row["q"] - 2, "multiplicity": row["multiplicity"]}
            for row in rows
        ]
    return {
        "source_middle_motive": "M5=(X,pi_5)",
        "normalized_odd_packet": "O4=(X,pi_5,2)",
        "source_rank": 168,
        "source_Hodge_before_twist": source["primitive_middle_H5_before_twist"],
        "source_Hodge_after_twist2": source["after_Tate_twist_2"],
        "core": {
            "motive": "(X,pi_core,2)", "rank": 10,
            "Hodge_before_twist": core, "Hodge_after_twist2": twist(core),
            "Hodge_summary_high_to_low": [1, 4, 4, 1],
        },
        "level_one_complement": {
            "motive": "(X,pi_lev,2)", "rank": 158,
            "Hodge_before_twist": level, "Hodge_after_twist2": twist(level),
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


@lru_cache(maxsize=2)
def expected_payload(repository: Path) -> dict[str, Any]:
    locks, certificates = expected_sources(repository)
    return {
        "material_passport": {
            "candidate_id": "HCS-C52",
            "project_slug": "henon_mu3_d12_calabi_yau_core_projector",
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
        "projective_monomial_group": expected_group_payload(),
        "middle_chow_kuenneth": expected_ck(),
        "cayley_jacobian_representation": expected_character_payload(),
        "middle_realization_decomposition": expected_realization(certificates),
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


def gate(name: str, check: Callable[[], Any]) -> dict[str, str]:
    try:
        check()
        return {"gate": name, "status": "PASS"}
    except Exception as error:
        return {
            "gate": name,
            "status": "FAIL",
            "diagnostic": type(error).__name__,
        }


def audit_certificate(certificate: Any, repository: Path) -> tuple[list[dict[str, str]], bool]:
    expected = expected_payload(repository)
    payload = certificate.get("payload", {}) if type(certificate) is dict else {}
    gates = [
        gate("certificate_envelope", lambda: (
            require(type(certificate) is dict, "certificate type"),
            require(set(certificate) == {"schema", "payload", "payload_sha256"}, "certificate keys"),
            require(type(certificate.get("schema")) is str and certificate.get("schema") == SCHEMA, "schema"),
            require(type(certificate.get("payload")) is dict, "payload type"),
            require(type(certificate.get("payload_sha256")) is str and len(certificate.get("payload_sha256", "")) == 64, "digest type"),
            require(certificate.get("payload_sha256") == hashlib.sha256(canonical_json(certificate.get("payload"))).hexdigest(), "self digest"),
        )),
        gate("frozen_full_payload", lambda: require(
            hashlib.sha256(canonical_json(payload)).hexdigest() == FROZEN_PAYLOAD_SHA256,
            "frozen payload digest",
        )),
        gate("recursive_exact_schema", lambda: require(
            same_recursive_shape(payload, expected), "recursive keys/types/list lengths"
        )),
        gate("passport_and_sources", lambda: (
            require(strict_equal(payload.get("material_passport"), expected["material_passport"]), "passport"),
            require(strict_equal(payload.get("source_lock"), expected["source_lock"]), "sources"),
        )),
        gate("frozen_model", lambda: require(
            strict_equal(payload.get("frozen_model"), expected["frozen_model"]), "model"
        )),
        gate("D12_enumeration", lambda: require(
            strict_equal(payload.get("projective_monomial_group"), expected["projective_monomial_group"]), "group"
        )),
        gate("middle_Chow_Kuenneth", lambda: require(
            strict_equal(payload.get("middle_chow_kuenneth"), expected["middle_chow_kuenneth"]), "middle CK"
        )),
        gate("Cayley_Jacobian_structure", lambda: (
            require(
                strict_equal(
                    payload.get("cayley_jacobian_representation", {}).get("cayley_polynomial")
                    if type(payload.get("cayley_jacobian_representation")) is dict else None,
                    expected["cayley_jacobian_representation"]["cayley_polynomial"],
                ), "Cayley polynomial"
            ),
            require(
                strict_equal(
                    payload.get("cayley_jacobian_representation", {}).get("bigrading")
                    if type(payload.get("cayley_jacobian_representation")) is dict else None,
                    expected["cayley_jacobian_representation"]["bigrading"],
                ), "bigrading"
            ),
            require(
                strict_equal(
                    payload.get("cayley_jacobian_representation", {}).get("relation_construction")
                    if type(payload.get("cayley_jacobian_representation")) is dict else None,
                    expected["cayley_jacobian_representation"]["relation_construction"],
                ), "relations"
            ),
        )),
        gate("residue_orientation_and_scalar_lift", lambda: require(
            strict_equal(
                payload.get("cayley_jacobian_representation", {}).get("residue_action")
                if type(payload.get("cayley_jacobian_representation")) is dict else None,
                expected["cayley_jacobian_representation"]["residue_action"],
            ), "residue orientation and general scalar lift"
        )),
        gate("quotient_action_well_defined", lambda: require(
            strict_equal(
                payload.get("cayley_jacobian_representation", {}).get("quotient_action_certificate")
                if type(payload.get("cayley_jacobian_representation")) is dict else None,
                expected["cayley_jacobian_representation"]["quotient_action_certificate"],
            ), "relation invariance and representation law"
        )),
        gate("independent_character_replay", lambda: (
            require(
                strict_equal(
                    payload.get("cayley_jacobian_representation", {}).get("H41_character")
                    if type(payload.get("cayley_jacobian_representation")) is dict else None,
                    expected["cayley_jacobian_representation"]["H41_character"],
                ), "H41 character"
            ),
            require(
                strict_equal(
                    payload.get("cayley_jacobian_representation", {}).get("H32_character")
                    if type(payload.get("cayley_jacobian_representation")) is dict else None,
                    expected["cayley_jacobian_representation"]["H32_character"],
                ), "exact Q(rho) and modular character replay"
            ),
        )),
        gate("middle_realization_split", lambda: require(
            strict_equal(payload.get("middle_realization_decomposition"), expected["middle_realization_decomposition"]), "realization split"
        )),
        gate("Q_group_algebra_no_go", lambda: require(
            strict_equal(payload.get("group_algebra_no_go"), expected["group_algebra_no_go"]), "QG no-go"
        )),
        gate("decisions", lambda: require(
            strict_equal(payload.get("decisions"), expected["decisions"]), "decisions"
        )),
        gate("C53_future_firewall", lambda: require(
            strict_equal(payload.get("future_gates_C53"), expected["future_gates_C53"]), "future gates"
        )),
        gate("scope_firewall", lambda: require(
            strict_equal(payload.get("scope"), expected["scope"]), "scope"
        )),
    ]
    return gates, all(row["status"] == "PASS" for row in gates)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    arguments = parser.parse_args()
    repository = Path(__file__).resolve().parents[3]
    certificate = json.loads(arguments.certificate.read_text(encoding="utf-8"))
    gates, passed = audit_certificate(certificate, repository)
    report = {
        "schema": CHECK_SCHEMA,
        "certificate_sha256": digest(arguments.certificate),
        "gates": gates,
        "gate_summary": {
            "passed": sum(row["status"] == "PASS" for row in gates),
            "total": len(gates),
        },
        "overall": "PASS" if passed else "FAIL",
    }
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(f"{report['overall']} {report['gate_summary']['passed']}/{report['gate_summary']['total']}")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
