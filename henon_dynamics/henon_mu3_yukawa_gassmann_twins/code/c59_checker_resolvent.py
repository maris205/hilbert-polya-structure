#!/usr/bin/env python3
"""Independent checker for staged HCS-C59 primitive-resolvent evidence.

The checker does not import c59_resolvent.py and does not use its finite-field
or graph libraries.  It finds all roots by direct evaluation in F_p, rebuilds
the permutation groups and supports from explicit arrays, validates the graph
map and color-refinement automorphism bound, and reconstructs the complete
expected evidence payload before exact comparison.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import os
import re
import stat
import tempfile
import time
from pathlib import Path
from typing import Any, Callable, Iterable, Sequence

EVIDENCE_SCHEMA_ID = "hcs-c59-resolvent-evidence-v1"
REPORT_SCHEMA_ID = "hcs-c59-resolvent-check-report-v1"
P = 692717
N = 27
W_ORDER = 51840
H_ORDER = 162
KNOWN_POLYNOMIAL_DIGESTS = {
    "301": "21b304679d3b77a7b1fae4182e203d8f2652588efffa4a160cccd98ac3e81257",
    "303": "76fa8081c92e58839f60659fa7c9979d9b002fae5408cc30777341d21665acb2",
}
# Checker-owned literals.  They are intentionally repeated here instead of
# importing c59_group or c59_resolvent, so a producer-side transport or
# constant mutation cannot silently redefine the field stabilizers.
CHECKER_FIELD_SUBGROUPS = {
    "301": {
        "generators": [
            [1,2,19,21,20,3,24,11,9,10,23,15,13,14,22,5,4,18,6,16,17,12,8,27,25,26,7],
            [16,27,13,12,22,26,15,25,24,7,14,18,20,5,1,23,8,17,9,19,6,2,10,3,4,21,11],
            [26,13,22,20,24,15,21,3,14,1,19,11,25,18,23,7,5,9,12,27,16,8,6,17,2,10,4],
        ],
        "smallgroup_id": [162, 11],
        "tom_locator": 301,
    },
    "303": {
        "generators": [
            [5,1,6,2,3,4,10,21,14,17,19,11,7,8,9,15,18,20,12,13,16,26,22,27,23,24,25],
            [7,15,13,12,26,5,16,18,20,1,22,8,9,6,27,11,4,25,3,24,14,10,21,19,17,23,2],
            [16,23,9,8,26,27,7,25,24,10,11,12,13,6,5,22,17,18,19,20,2,1,21,3,4,15,14],
        ],
        "smallgroup_id": [162, 19],
        "tom_locator": 303,
    },
}
SOURCE_INVENTORY = [
    "README.md", "c59_atomic_promote.py", "c59_checker.py", "c59_checker_group.g",
    "c59_checker_resolvent.py", "c59_exact.py", "c59_group.py", "c59_hash_manifest.py",
    "c59_pipeline.py", "c59_producer.py", "c59_resolvent.py", "run_all.sh", "test_c59.py",
]
RESULT_INVENTORY = [
    "RESULTS.md", "TEST_REPORT.md", "c59_certificate.json", "c59_check_report.json",
    "c59_group_evidence.json", "c59_resolvent_evidence.json", "c59_schema.json",
    "scoped_hash_manifest.json",
]
CERTIFICATE_KEYS = [
    "artifact_contract", "G0_released_authority_rebind", "G1_primitive_orbit_resolvents",
    "G2_gassmann_minimality", "G3_fixed_fields_and_zeta", "G4_global_arithmetic",
    "G5_tom140_local_algebra", "G6_tom206_local_algebra",
    "G7_independence_scope_release", "written_bridges", "backend_contract",
    "source_contract", "scope_nonclaims", "nonresults", "status",
]
FALSE_SCOPE_LEAVES = [
    "integral_permutation_equivalence_claimed", "rings_of_integers_isomorphic_claimed",
    "class_number_equality_claimed", "idele_group_isomorphism_claimed",
    "local_equivalence_claimed", "adelic_equivalence_claimed", "d3_branch_selected",
    "local_fields_classified_by_nefd_rows", "expanded_characteristic_zero_resolvent_claimed",
    "characteristic_zero_coefficient_hash_claimed", "integral_basis_claimed",
    "maximal_order_claimed", "monogenicity_claimed",
    "polynomial_discriminant_equals_field_discriminant_claimed",
    "decomposition_frobenius_claimed", "bad_artin_euler_claimed",
    "local_epsilon_factor_claimed", "local_root_number_claimed",
    "global_root_number_claimed", "artin_holomorphy_claimed", "automorphy_claimed",
    "rational_point_claimed", "hasse_principle_claimed", "weak_approximation_claimed",
    "brauer_manin_claimed", "motive_claimed", "rh_claimed",
    "hilbert_polya_operator_claimed", "paper_complete_claimed", "release_claimed",
]
CHECKER_EVIDENCE_PAYLOAD_KEYS = [
    "G1_primitive_orbit_resolvents", "authority", "constants", "finite_field",
    "group_and_automorphisms", "integration_contract", "invariants",
    "line_configuration", "object_boundary", "scope_nonclaims", "status",
]
CHECKER_EVIDENCE_SCHEMA_DESCRIPTOR = {
    "document_keys": ["payload", "payload_sha256", "schema_id", "schema_sha256"],
    "payload_keys": CHECKER_EVIDENCE_PAYLOAD_KEYS,
    "scope_nonclaim_keys": sorted(FALSE_SCOPE_LEAVES),
    "schema_id": "hcs-c59-resolvent-evidence-source-schema-v1",
    "unknown_fields_rejected": True,
}

Perm = tuple[int, ...]
Edge = tuple[int, int]
Pair = tuple[int, int]
PairSet = tuple[Pair, ...]


class CheckFailure(RuntimeError):
    pass


def encoded(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def packed(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def packed_digest(value: Any) -> str:
    return digest(packed(value))


def exact_keys(obj: dict[str, Any], names: Iterable[str], context: str) -> None:
    have = set(obj)
    need = set(names)
    if have != need:
        raise CheckFailure(f"{context}: missing={sorted(need-have)} extra={sorted(have-need)}")


def read_manifest(blob: bytes) -> dict[str, str]:
    answer: dict[str, str] = {}
    rows = blob.decode().splitlines()
    for row in rows:
        match = re.match(r"\A([0-9a-f]{64})  (.+)\Z", row)
        if match is None:
            raise CheckFailure("malformed predecessor manifest")
        checksum, name = match.group(1), match.group(2)
        if name in answer:
            raise CheckFailure("duplicate predecessor manifest member")
        answer[name] = checksum
    if not answer or tuple(answer) != tuple(sorted(answer)):
        raise CheckFailure("predecessor manifest is empty or not sorted")
    return answer


def as_perm(row: Sequence[int], origin: int) -> Perm:
    candidate = tuple(int(item) - origin for item in row)
    if len(candidate) != N or set(candidate) != set(range(N)):
        raise CheckFailure("malformed degree-27 permutation")
    return candidate


def multiply_perms(first: Perm, second: Perm) -> Perm:
    return tuple(first[second[position]] for position in range(N))


def close_group(generators: Sequence[Perm]) -> tuple[Perm, ...]:
    identity = tuple(range(N))
    known: set[Perm] = {identity}
    pending: list[Perm] = [identity]
    cursor = 0
    while cursor < len(pending):
        element = pending[cursor]
        cursor += 1
        for generator in generators:
            new_element = multiply_perms(generator, element)
            if new_element not in known:
                known.add(new_element)
                pending.append(new_element)
    return tuple(sorted(known))


def elementary_prime_test(number: int) -> bool:
    if number < 2:
        return False
    if number % 2 == 0:
        return number == 2
    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2
    return True


def horner(coefficients: Sequence[int], argument: int) -> int:
    result = 0
    for coefficient in reversed(coefficients):
        result = (result * argument + coefficient) % P
    return result


def roots_by_exhaustion(coefficients: Sequence[int]) -> list[int]:
    roots: list[int] = []
    reversed_coefficients = tuple(reversed(tuple(coefficient % P for coefficient in coefficients)))
    for argument in range(P):
        result = 0
        for coefficient in reversed_coefficients:
            result = (result * argument + coefficient) % P
        if result == 0:
            roots.append(argument)
    return roots


def multiply_linear_factors(roots: Sequence[int]) -> list[int]:
    current = [1]
    for root in roots:
        following = [0] * (len(current) + 1)
        for position in range(len(current)):
            following[position] = (following[position] - root * current[position]) % P
            following[position + 1] = (following[position + 1] + current[position]) % P
        current = following
    return current


def equation_residue(terms: Sequence[dict[str, Any]], point: Sequence[int]) -> int:
    answer = 0
    for term in terms:
        product = int(term["coefficient"]) % P
        powers = term["exponents_abcd"]
        if len(powers) != 4:
            raise CheckFailure("chart equation exponent vector is not four-dimensional")
        for coordinate, power in zip(point, powers):
            product = product * pow(coordinate, int(power), P) % P
        answer = (answer + product) % P
    return answer


def meeting_edges(points: Sequence[Sequence[int]]) -> list[list[int]]:
    result: list[list[int]] = []
    for i in range(N):
        a, b, c, d = points[i]
        for j in range(i + 1, N):
            aa, bb, cc, dd = points[j]
            determinant = ((aa - a) * (dd - d) - (bb - b) * (cc - c)) % P
            if determinant == 0:
                result.append([i, j])
    return result


def sorted_degrees(edges: Sequence[Sequence[int]]) -> list[int]:
    counts = [0 for _ in range(N)]
    for left, right in edges:
        counts[left] += 1
        counts[right] += 1
    counts.sort()
    return counts


def edge_preserved(permutation: Perm, edge_set: set[Edge]) -> bool:
    for left, right in edge_set:
        image = tuple(sorted((permutation[left], permutation[right])))
        if image not in edge_set:
            return False
    return True


def equitable_cells(matrix: Sequence[Sequence[int]], individualized: Sequence[int]) -> list[list[int]]:
    colors = [0 for _ in range(N)]
    for position, vertex in enumerate(individualized):
        colors[vertex] = position + 1
    while True:
        color_names = sorted(set(colors))
        slot = {color: place for place, color in enumerate(color_names)}
        descriptors: list[tuple[int, tuple[int, ...]]] = []
        for vertex in range(N):
            neighbor_counts = [0] * len(color_names)
            for other in range(N):
                if int(matrix[vertex][other]) == 1:
                    neighbor_counts[slot[colors[other]]] += 1
            descriptors.append((colors[vertex], tuple(neighbor_counts)))
        descriptor_names = sorted(set(descriptors))
        name_to_color = {descriptor: number for number, descriptor in enumerate(descriptor_names)}
        new_colors = [name_to_color[descriptor] for descriptor in descriptors]
        unchanged = True
        for left in range(N):
            for right in range(N):
                if (colors[left] == colors[right]) != (new_colors[left] == new_colors[right]):
                    unchanged = False
                    break
            if not unchanged:
                break
        colors = new_colors
        if unchanged:
            break
    blocks: dict[int, list[int]] = {}
    for vertex, color in enumerate(colors):
        blocks.setdefault(color, []).append(vertex)
    return sorted(sorted(block) for block in blocks.values())


def refinement_proof(matrix: Sequence[Sequence[int]]) -> dict[str, Any]:
    base = [0, 1, 2, 3, 4]
    steps: list[dict[str, Any]] = []
    factors: list[int] = []
    for depth in range(6):
        fixed = base[:depth]
        blocks = equitable_cells(matrix, fixed)
        steps.append({
            "fixed_base": fixed,
            "cells": blocks,
            "cell_sizes": sorted(len(block) for block in blocks),
        })
        if depth != 5:
            chosen = base[depth]
            factors.append(len(next(block for block in blocks if chosen in block)))
    if factors != [27, 16, 10, 6, 2] or math.prod(factors) != W_ORDER:
        raise CheckFailure("equitable-refinement automorphism bound is not 51840")
    if any(len(block) != 1 for block in steps[-1]["cells"]):
        raise CheckFailure("individualized refinement does not end discretely")
    return {
        "method": "individualize_then_equitable_color_refinement_orbit_bound",
        "base": base,
        "chosen_cell_sizes": factors,
        "steps": steps,
        "upper_bound": math.prod(factors),
        "final_partition_discrete": True,
    }


def pair_image(permutation: Perm, pair: Pair) -> Pair:
    left, right = permutation[pair[0]], permutation[pair[1]]
    return (left, right) if left < right else (right, left)


def set_image(permutation: Perm, pairs: PairSet) -> PairSet:
    return tuple(sorted(pair_image(permutation, pair) for pair in pairs))


def pair_orbit(elements: Sequence[Perm], seed: Pair) -> PairSet:
    images = {pair_image(element, seed) for element in elements}
    return tuple(sorted(images))


def all_support_images(elements: Sequence[Perm], support: PairSet) -> tuple[PairSet, ...]:
    images = {set_image(element, support) for element in elements}
    return tuple(sorted(images))


def values_of_supports(alpha: Sequence[int], supports: Sequence[PairSet]) -> list[int]:
    answer: list[int] = []
    for support in supports:
        value = 0
        for left, right in support:
            value = (value + alpha[left] * alpha[right]) % P
        answer.append(value)
    return answer


def perm_lists(elements: Sequence[Perm]) -> list[list[int]]:
    return [list(element) for element in elements]


def pair_lists(pairs: PairSet) -> list[list[int]]:
    return [list(pair) for pair in pairs]


def support_lists(families: Sequence[PairSet]) -> list[list[list[int]]]:
    return [pair_lists(family) for family in families]


def invariant_payload(
    label: str,
    field_subgroups: dict[str, Any],
    w_elements: Sequence[Perm],
    alpha: Sequence[int],
) -> dict[str, Any]:
    if label == "301":
        seeds: list[Pair] = [(0, 1), (0, 8)]
        wanted_parts, wanted_size = [27, 27], 54
    elif label == "303":
        seeds = [(0, 1)]
        wanted_parts, wanted_size = [81], 81
    else:
        raise CheckFailure("unknown invariant label")
    subgroup = field_subgroups[label]
    if subgroup["tom_locator"] != int(label):
        raise CheckFailure(f"H{label} durable locator differs")
    h_generators = tuple(as_perm(row, 1) for row in subgroup["generators"])
    h_elements = close_group(h_generators)
    if len(h_elements) != H_ORDER:
        raise CheckFailure(f"H{label} does not have order 162")
    components = [pair_orbit(h_elements, seed) for seed in seeds]
    if [len(part) for part in components] != wanted_parts:
        raise CheckFailure(f"H{label} support component sizes differ")
    support = tuple(sorted({pair for part in components for pair in part}))
    if len(support) != wanted_size or len(support) != sum(map(len, components)):
        raise CheckFailure(f"H{label} support union is not disjoint with the required size")
    stabilizer = tuple(element for element in w_elements if set_image(element, support) == support)
    if len(stabilizer) != H_ORDER or set(stabilizer) != set(h_elements):
        raise CheckFailure(f"H{label} is not the exact support stabilizer")
    families = all_support_images(w_elements, support)
    if len(families) != 320:
        raise CheckFailure(f"H{label} support orbit is not degree 320")
    values = values_of_supports(alpha, families)
    if len(set(values)) != 320:
        raise CheckFailure(f"H{label} invariant has colliding values")
    coefficients = multiply_linear_factors(values)
    coefficient_digest = packed_digest(coefficients)
    if coefficient_digest != KNOWN_POLYNOMIAL_DIGESTS[label]:
        raise CheckFailure(f"H{label} modular polynomial hash differs")

    h_element_lists = perm_lists(h_elements)
    stabilizer_lists = perm_lists(stabilizer)
    family_lists = support_lists(families)
    return {
        "tom_locator": int(label),
        "smallgroup_id": [int(value) for value in subgroup["smallgroup_id"]],
        "h_generators": perm_lists(h_generators),
        "h_order": len(h_elements),
        "h_element_inventory_sha256": packed_digest(h_element_lists),
        "seed_pairs": [list(seed) for seed in seeds],
        "support_components": [pair_lists(part) for part in components],
        "support_component_sizes": [len(part) for part in components],
        "support": pair_lists(support),
        "support_size": len(support),
        "support_stabilizer_order": len(stabilizer),
        "support_stabilizer_equals_h": set(stabilizer) == set(h_elements),
        "support_stabilizer_elements": stabilizer_lists,
        "support_stabilizer_inventory_sha256": packed_digest(stabilizer_lists),
        "families": family_lists,
        "family_count": len(families),
        "families_sha256": packed_digest(family_lists),
        "conjugate_values_by_family_order": values,
        "distinct_value_count": len(set(values)),
        "values_sha256": packed_digest(values),
        "sorted_values_sha256": packed_digest(sorted(values)),
        "monic_coefficients_low_to_high": coefficients,
        "coefficient_count": len(coefficients),
        "monic_coefficients_sha256": coefficient_digest,
    }


def reconstruct_payload(
    certificate_path: Path,
    manifest_path: Path,
    supplied_payload: dict[str, Any],
) -> dict[str, Any]:
    certificate_blob = certificate_path.read_bytes()
    manifest_blob = manifest_path.read_bytes()
    certificate = json.loads(certificate_blob)
    exact_keys(certificate, {"schema", "schema_sha256", "payload", "payload_sha256"}, "C56 certificate")
    c56_payload = certificate["payload"]
    c56_payload_digest = digest(packed(c56_payload))
    if c56_payload_digest != certificate["payload_sha256"]:
        raise CheckFailure("C56 certificate payload digest fails")
    manifest = read_manifest(manifest_blob)
    certificate_digest = digest(certificate_blob)
    if manifest.get("results/c56_certificate.json") != certificate_digest:
        raise CheckFailure("C56 manifest does not bind certificate")
    eliminant = [int(value) for value in c56_payload["irreducibility"]["eliminant_coefficients_d_0_to_27"]]
    if len(eliminant) != 28:
        raise CheckFailure("eliminant length differs from 28")
    shapes = {row["leading_variable"]: row for row in c56_payload["grassmann_main_chart"]["lex_shape"]}
    if set(shapes) != set("abcd"):
        raise CheckFailure("lex shape variable set differs")
    equations = c56_payload["grassmann_main_chart"]["line_equations_sparse"]
    if len(equations) != 4 or not elementary_prime_test(P):
        raise CheckFailure("equation count or prime proof fails")

    denominator_values = {"eliminant": eliminant[-1]}
    for name in "abcd":
        denominator_values[f"lex_{name}"] = int(shapes[name]["leading_coefficient"])
    denominator_residues = {name: value % P for name, value in denominator_values.items()}
    if 0 in denominator_residues.values():
        raise CheckFailure("prime belongs to denominator envelope")

    eliminant_mod = [coefficient % P for coefficient in eliminant]
    roots = roots_by_exhaustion(eliminant_mod)
    if len(roots) != 27 or len(set(roots)) != 27:
        raise CheckFailure("direct root scan does not give 27 distinct roots")
    roots.sort()
    inverse_leading = pow(eliminant_mod[-1], -1, P)
    normalized = [(coefficient * inverse_leading) % P for coefficient in eliminant_mod]
    multiplyback = multiply_linear_factors(roots)
    if multiplyback != normalized:
        raise CheckFailure("direct roots do not multiply back")

    points: list[list[int]] = []
    for d_value in roots:
        point: dict[str, int] = {"d": d_value}
        for name in "abc":
            shape = shapes[name]
            tail = horner(shape["tail_coefficients_d_0_up"], d_value)
            point[name] = -tail * pow(int(shape["leading_coefficient"]) % P, -1, P) % P
        points.append([point[name] for name in "abcd"])
    residues = [[equation_residue(equation, point) for equation in equations] for point in points]
    if any(entry for row in residues for entry in row):
        raise CheckFailure("line resubstitution fails")
    actual_edges = meeting_edges(points)
    actual_degrees = sorted_degrees(actual_edges)
    if len(actual_edges) != 135 or actual_degrees != [10] * N:
        raise CheckFailure("actual graph shape fails")

    incidence = c56_payload["we6"]["line_class_intersection_matrix"]
    if len(incidence) != N or any(len(row) != N for row in incidence):
        raise CheckFailure("standard incidence matrix shape fails")
    standard_edges = [
        [left, right]
        for left in range(N)
        for right in range(left + 1, N)
        if int(incidence[left][right]) == 1
    ]
    standard_edge_set: set[Edge] = {tuple(edge) for edge in standard_edges}
    if len(standard_edges) != 135 or sorted_degrees(standard_edges) != [10] * N:
        raise CheckFailure("standard graph shape fails")

    c56_generators = tuple(as_perm(row, 0) for row in c56_payload["we6"]["simple_reflection_line_permutations"])
    released_generators = c56_generators
    w_elements = close_group(released_generators)
    if len(w_elements) != W_ORDER:
        raise CheckFailure("W closure order fails")
    if any(not edge_preserved(element, standard_edge_set) for element in w_elements):
        raise CheckFailure("W closure is not contained in graph automorphisms")
    refinement = refinement_proof(incidence)
    if refinement["upper_bound"] != len(w_elements):
        raise CheckFailure("graph automorphism upper and lower bounds differ")

    line_data = supplied_payload.get("line_configuration")
    if not isinstance(line_data, dict):
        raise CheckFailure("supplied line configuration missing")
    mapping = as_perm(line_data.get("actual_to_standard_label", []), 0)
    actual_edge_set = {tuple(edge) for edge in actual_edges}
    mapped_edges = {
        tuple(sorted((mapping[left], mapping[right])))
        for left, right in actual_edge_set
    }
    if mapped_edges != standard_edge_set:
        raise CheckFailure("supplied actual-to-standard map is not an isomorphism")
    canonical_mapping = min(
        tuple(element[mapping[index]] for index in range(N))
        for element in w_elements
    )
    if mapping != canonical_mapping:
        raise CheckFailure("supplied graph map is not the canonical W-orbit minimum")

    d_by_standard = [0] * N
    for actual_index, standard_index in enumerate(mapping):
        d_by_standard[standard_index] = roots[actual_index]
    alpha = [eliminant[-1] % P * value % P for value in d_by_standard]

    w_generator_lists = perm_lists(released_generators)
    w_element_lists = perm_lists(w_elements)
    invariant_records = {
        "301": invariant_payload("301", CHECKER_FIELD_SUBGROUPS, w_elements, alpha),
        "303": invariant_payload("303", CHECKER_FIELD_SUBGROUPS, w_elements, alpha),
    }
    return {
        "authority": {
            "c56_certificate_sha256": certificate_digest,
            "c56_certificate_payload_sha256": c56_payload_digest,
            "c56_manifest_sha256": digest(manifest_blob),
            "c56_manifest_line_count": len(manifest),
            "c56_manifest_certificate_entry_sha256": manifest["results/c56_certificate.json"],
            "durable_field_subgroups_sha256": packed_digest(CHECKER_FIELD_SUBGROUPS),
            "durable_field_subgroups_source": "C59_SOURCE_OWNED_CONSTANTS",
            "machine_contract_semantics_source_owned": True,
            "released_w_generators_read_from_c56": True,
        },
        "integration_contract": {
            "canonical_gate_key": "G1_primitive_orbit_resolvents",
            "planned_source_inventory": SOURCE_INVENTORY,
            "planned_result_inventory": RESULT_INVENTORY,
            "certificate_payload_keys": CERTIFICATE_KEYS,
            "scoped_manifest_entry_count": 20,
            "live_code_results_entry_count": 21,
        },
        "G1_primitive_orbit_resolvents": {
            "frozen_w_h_arrays_bound": True,
            "support_component_sizes": {"301": [27, 27], "303": [81]},
            "integral_normalization": "alpha_i=L*d_i",
            "scaled_invariant_name": "eta",
            "split_prime": P,
            "factor_degrees": [[1, 27]],
            "multiplyback_proven": True,
            "all_27_lines_all_4_equations": True,
            "schlaefli_graph_parameters": {"vertices": 27, "edges": 135, "degree": 10},
            "aut_graph_equals_released_w_permutation_set": True,
            "aut_graph_order": W_ORDER,
            "support_stabilizers_exact": {"301": True, "303": True},
            "orbit_sizes": {"301": 320, "303": 320},
            "distinct_values": {"301": 320, "303": 320},
            "modular_polynomials": {
                label: {
                    "coefficient_count": invariant_records[label]["coefficient_count"],
                    "sha256": invariant_records[label]["monic_coefficients_sha256"],
                }
                for label in ("301", "303")
            },
        },
        "constants": {
            "indexing": "zero_based",
            "prime": P,
            "integral_root_definition": "alpha_i=L*d_i",
            "invariant_definition": "eta_H=sum_{pair in support_H} alpha_i*alpha_j",
            "modular_coefficients_only": True,
        },
        "finite_field": {
            "prime_proven": True,
            "denominator_envelope": {
                "integer_values": denominator_values,
                "residues_mod_prime": denominator_residues,
                "all_nonzero": True,
            },
            "eliminant_coefficients_low_to_high_mod_prime": eliminant_mod,
            "normalized_monic_eliminant_low_to_high": normalized,
            "factor_degrees": [[1, 27]],
            "roots_sorted": roots,
            "roots_sha256": packed_digest(roots),
            "multiplyback_monic_low_to_high": multiplyback,
            "multiplyback_matches_normalized_eliminant": True,
        },
        "line_configuration": {
            "line_coordinates_abcd_by_root_order": points,
            "line_coordinates_sha256": packed_digest(points),
            "equation_residues_by_root_order": residues,
            "all_equation_residues_zero": True,
            "actual_edges": actual_edges,
            "actual_edges_sha256": packed_digest(actual_edges),
            "actual_degree_multiset": actual_degrees,
            "standard_edges": standard_edges,
            "standard_edges_sha256": packed_digest(standard_edges),
            "actual_to_standard_label": list(mapping),
            "mapping_sha256": packed_digest(list(mapping)),
            "mapping_is_graph_isomorphism": True,
            "d_by_standard_label": d_by_standard,
            "alpha_by_standard_label": alpha,
        },
        "group_and_automorphisms": {
            "w_generators": w_generator_lists,
            "w_generators_sha256": packed_digest(w_generator_lists),
            "frozen_w_generators_match_c56": True,
            "w_order": len(w_elements),
            "w_element_inventory_sha256": packed_digest(w_element_lists),
            "all_w_elements_preserve_standard_graph": True,
            "automorphism_upper_bound_certificate": refinement,
            "aut_graph_order": len(w_elements),
            "aut_graph_equals_released_w": True,
        },
        "invariants": invariant_records,
        "object_boundary": {
            "eta_is_scaled_integral_invariant": True,
            "exact_characteristic_zero_object": "unexpanded_orbit_product_definition_only",
            "modular_polynomial_claim_only": True,
            "semantic_firewall": "NO_BAD_EULER_OR_ROOT_NUMBER",
        },
        "scope_nonclaims": {leaf: False for leaf in FALSE_SCOPE_LEAVES},
        "status": {
            "gate": "G1_primitive_orbit_resolvents",
            "evidence_status": "PASS",
            "implementation_state": "EVIDENCE_REPLAY_PASS",
            "release_authorized": False,
        },
    }


def document_guard(
    document: dict[str, Any],
    expected_payload: dict[str, Any],
) -> None:
    exact_keys(document, CHECKER_EVIDENCE_SCHEMA_DESCRIPTOR["document_keys"], "evidence document")
    schema_digest = packed_digest(CHECKER_EVIDENCE_SCHEMA_DESCRIPTOR)
    if document["schema_id"] != EVIDENCE_SCHEMA_ID or document["schema_sha256"] != schema_digest:
        raise CheckFailure("schema id/hash mismatch")
    exact_keys(document["payload"], CHECKER_EVIDENCE_PAYLOAD_KEYS, "evidence payload")
    exact_keys(document["payload"]["scope_nonclaims"], FALSE_SCOPE_LEAVES, "scope nonclaims")
    if any(value is not False for value in document["payload"]["scope_nonclaims"].values()):
        raise CheckFailure("a scope nonclaim is not false")
    if document["payload_sha256"] != digest(encoded(document["payload"])):
        raise CheckFailure("evidence payload digest mismatch")
    if encoded(document["payload"]) != encoded(expected_payload):
        raise CheckFailure("evidence payload differs from independent reconstruction")


def make_mutations(document: dict[str, Any]) -> list[tuple[str, Callable[[dict[str, Any]], None]]]:
    def alter_inventory(candidate: dict[str, Any]) -> None:
        candidate["payload"]["integration_contract"]["planned_source_inventory"][0] = "WRONG.md"

    def alter_prime(candidate: dict[str, Any]) -> None:
        candidate["payload"]["constants"]["prime"] += 2

    def zero_denominator(candidate: dict[str, Any]) -> None:
        candidate["payload"]["finite_field"]["denominator_envelope"]["residues_mod_prime"]["lex_a"] = 0

    def duplicate_root(candidate: dict[str, Any]) -> None:
        roots = candidate["payload"]["finite_field"]["roots_sorted"]
        roots[1] = roots[0]

    def alter_line(candidate: dict[str, Any]) -> None:
        points = candidate["payload"]["line_configuration"]["line_coordinates_abcd_by_root_order"]
        points[0][0] = (points[0][0] + 1) % P

    def alter_residue(candidate: dict[str, Any]) -> None:
        candidate["payload"]["line_configuration"]["equation_residues_by_root_order"][0][0] = 1

    def delete_edge(candidate: dict[str, Any]) -> None:
        candidate["payload"]["line_configuration"]["actual_edges"].pop()

    def swap_mapping(candidate: dict[str, Any]) -> None:
        mapping = candidate["payload"]["line_configuration"]["actual_to_standard_label"]
        mapping[0], mapping[1] = mapping[1], mapping[0]

    def alter_w_generator(candidate: dict[str, Any]) -> None:
        generator = candidate["payload"]["group_and_automorphisms"]["w_generators"][0]
        generator[0], generator[1] = generator[1], generator[0]

    def alter_aut_bound(candidate: dict[str, Any]) -> None:
        certificate = candidate["payload"]["group_and_automorphisms"]["automorphism_upper_bound_certificate"]
        certificate["chosen_cell_sizes"][-1] = 3

    def delete_support_pair(candidate: dict[str, Any]) -> None:
        candidate["payload"]["invariants"]["301"]["support"].pop()

    def delete_family_pair(candidate: dict[str, Any]) -> None:
        candidate["payload"]["invariants"]["303"]["families"][0].pop()

    def alter_value(candidate: dict[str, Any]) -> None:
        values = candidate["payload"]["invariants"]["303"]["conjugate_values_by_family_order"]
        values[0] = (values[0] + 1) % P

    def alter_coefficient(candidate: dict[str, Any]) -> None:
        coefficients = candidate["payload"]["invariants"]["301"]["monic_coefficients_low_to_high"]
        coefficients[0] = (coefficients[0] + 1) % P

    def assert_char0_expansion(candidate: dict[str, Any]) -> None:
        candidate["payload"]["scope_nonclaims"]["expanded_characteristic_zero_resolvent_claimed"] = True

    def alter_authority(candidate: dict[str, Any]) -> None:
        candidate["payload"]["authority"]["durable_field_subgroups_sha256"] = "0" * 64

    return [
        ("contract_inventory", alter_inventory),
        ("prime", alter_prime),
        ("denominator_envelope", zero_denominator),
        ("duplicate_root", duplicate_root),
        ("line_coordinate", alter_line),
        ("equation_residue", alter_residue),
        ("edge_inventory", delete_edge),
        ("graph_mapping", swap_mapping),
        ("w_generator", alter_w_generator),
        ("automorphism_bound", alter_aut_bound),
        ("support", delete_support_pair),
        ("support_family", delete_family_pair),
        ("invariant_value", alter_value),
        ("modular_coefficient", alter_coefficient),
        ("char0_scope", assert_char0_expansion),
        ("authority_hash", alter_authority),
    ]


def run_mutations(
    document: dict[str, Any],
    expected_payload: dict[str, Any],
) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for name, mutate in make_mutations(document):
        candidate = copy.deepcopy(document)
        mutate(candidate)
        candidate["payload_sha256"] = digest(encoded(candidate["payload"]))
        caught = False
        reason = ""
        try:
            document_guard(candidate, expected_payload)
        except (CheckFailure, ValueError, TypeError, KeyError) as error:
            caught = True
            reason = type(error).__name__
        results.append({"name": name, "caught": caught, "failure_class": reason})
    if not all(result["caught"] for result in results):
        raise CheckFailure("one or more evidence mutations survived")
    return results


STAGE_NAME_PATTERN = re.compile(r"^\.c59-stage-[A-Za-z0-9]{8}$")
EVIDENCE_BASENAME = "c59_resolvent_evidence.json"
REPORT_BASENAME = "c59_resolvent_check_report.json"


def path_in_stage(
    value: str, expected_basename: str
) -> tuple[Path, Path, tuple[int, int]]:
    path = Path(value).absolute()
    code = Path(__file__).resolve().parent
    project = code.parent
    results = (project / "results").resolve(strict=True)
    stage = path.parent
    if (
        path.name != expected_basename
        or not STAGE_NAME_PATTERN.fullmatch(stage.name)
        or stage.parent != results
        or not stage.is_dir()
        or stage.is_symlink()
        or stage.resolve(strict=True) != stage
    ):
        raise CheckFailure(
            "checker target must have its fixed basename directly under one real "
            "PROJECT/results/.c59-stage-[A-Za-z0-9]{8} directory"
        )
    metadata = stage.stat()
    return path, stage, (metadata.st_dev, metadata.st_ino)


def assert_stage_identity(stage: Path, identity: tuple[int, int]) -> None:
    metadata = stage.stat()
    if (
        stage.is_symlink()
        or not stat.S_ISDIR(metadata.st_mode)
        or stage.resolve(strict=True) != stage
        or (metadata.st_dev, metadata.st_ino) != identity
    ):
        raise CheckFailure("canonical results stage changed during checker replay")


def existing_file_identity(path: Path) -> tuple[int, int, int, int]:
    if path.is_symlink() or not path.is_file():
        raise CheckFailure("checker stage input must be a regular non-symlink file")
    metadata = path.stat()
    if metadata.st_nlink != 1:
        raise CheckFailure("checker stage input must have link count one")
    return (metadata.st_dev, metadata.st_ino, metadata.st_size, metadata.st_mtime_ns)


def stable_file_bytes(path: Path) -> tuple[bytes, tuple[int, ...]]:
    if path.is_symlink() or not path.is_file():
        raise CheckFailure(f"authority must be a regular non-symlink file: {path}")
    before = path.stat()
    data = path.read_bytes()
    after = path.stat()
    identity = (
        after.st_dev, after.st_ino, after.st_size, after.st_mode,
        after.st_mtime_ns, after.st_ctime_ns, after.st_nlink,
    )
    if identity != (
        before.st_dev, before.st_ino, before.st_size, before.st_mode,
        before.st_mtime_ns, before.st_ctime_ns, before.st_nlink,
    ) or len(data) != after.st_size:
        raise CheckFailure(f"authority changed while being read: {path}")
    return data, identity


def safe_write(path: Path, data: bytes) -> None:
    descriptor, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--certificate", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--evidence", required=True)
    destination = parser.add_mutually_exclusive_group(required=True)
    destination.add_argument("--report")
    destination.add_argument("--check-existing-report")
    args = parser.parse_args()

    evidence_path, stage, stage_identity = path_in_stage(
        args.evidence, EVIDENCE_BASENAME
    )
    selected_report = args.report if args.report is not None else args.check_existing_report
    report_path, report_stage, report_stage_identity = path_in_stage(
        selected_report, REPORT_BASENAME
    )
    if report_stage != stage or report_stage_identity != stage_identity:
        raise CheckFailure("checker evidence and report must share one canonical stage")
    evidence_identity = existing_file_identity(evidence_path)
    report_identity = None
    if args.check_existing_report is not None:
        report_identity = existing_file_identity(report_path)
    elif os.path.lexists(report_path):
        existing_file_identity(report_path)
    if evidence_path == report_path:
        raise CheckFailure("checker evidence and report paths alias")

    certificate_path = args.certificate.resolve()
    manifest_path = args.manifest.resolve()
    certificate_before = stable_file_bytes(certificate_path)
    manifest_before = stable_file_bytes(manifest_path)
    evidence_before = stable_file_bytes(evidence_path)
    started = time.perf_counter()
    assert_stage_identity(stage, stage_identity)
    evidence_blob = evidence_before[0]
    document = json.loads(evidence_blob)
    schema_digest = packed_digest(CHECKER_EVIDENCE_SCHEMA_DESCRIPTOR)
    expected_payload = reconstruct_payload(
        args.certificate.resolve(),
        args.manifest.resolve(),
        document.get("payload", {}),
    )
    document_guard(document, expected_payload)
    mutation_results = run_mutations(document, expected_payload)

    report = {
        "schema_id": REPORT_SCHEMA_ID,
        "status": "PASS",
        "evidence_sha256": digest(evidence_blob),
        "evidence_payload_sha256": document["payload_sha256"],
        "schema_sha256": schema_digest,
        "checker_sha256": digest(Path(__file__).read_bytes()),
        "authority_sha256": {
            "c56_certificate": digest(args.certificate.read_bytes()),
            "c56_manifest": digest(args.manifest.read_bytes()),
            "durable_field_subgroups": packed_digest(CHECKER_FIELD_SUBGROUPS),
        },
        "checks": [
            "source_owned_exact_evidence_schema",
            "canonical_payload_hash",
            "c56_manifest_certificate_bind",
            "source_owned_machine_contract_13_8_15_bind",
            "released_w_and_checker_owned_h_input_bind",
            "elementary_primality",
            "denominator_envelope",
            "direct_1_to_27_root_scan",
            "eliminant_multiplyback",
            "all_27_lines_all_4_equations",
            "135_edge_10_regular_graph",
            "canonical_graph_mapping",
            "w_order_and_graph_inclusion",
            "equitable_refinement_aut_upper_bound",
            "aut_graph_equals_w_51840",
            "support_27_plus_27_and_81",
            "exact_support_stabilizers",
            "320_distinct_values_each",
            "two_321_coefficient_polynomials_and_hashes",
            "characteristic_zero_scope_firewall"
        ],
        "mutations": mutation_results,
        "all_mutations_caught": True,
        "expanded_characteristic_zero_resolvent_claimed": False,
    }
    report_blob = encoded(report)
    assert_stage_identity(stage, stage_identity)
    if existing_file_identity(evidence_path) != evidence_identity:
        raise CheckFailure("resolver evidence identity changed during checker replay")
    if (
        stable_file_bytes(evidence_path) != evidence_before
        or stable_file_bytes(certificate_path) != certificate_before
        or stable_file_bytes(manifest_path) != manifest_before
    ):
        raise CheckFailure("resolver/C56 authority bytes changed during checker replay")
    if args.report is not None:
        safe_write(report_path, report_blob)
        mode = "write"
        target = report_path.name
    else:
        if existing_file_identity(report_path) != report_identity:
            raise CheckFailure("existing checker report identity changed during replay")
        if report_path.read_bytes() != report_blob:
            raise CheckFailure("existing checker report is not byte-identical to a fresh replay")
        mode = "replay"
        target = report_path.name
    summary = {
        "mode": mode,
        "status": "PASS",
        "target": target,
        "report_sha256": digest(report_blob),
        "evidence_sha256": digest(evidence_blob),
        "mutations": len(mutation_results),
        "elapsed_seconds": round(time.perf_counter() - started, 6),
    }
    print(json.dumps(summary, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
