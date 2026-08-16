#!/usr/bin/env python3
"""Build the staged HCS-C59 primitive-resolvent evidence.

This module consumes only explicit released/staged authority files supplied on
the command line.  In particular it never constructs H301 or H303 through a
fresh table-of-marks transport.  The characteristic-zero resolvents are
defined by finite orbit products; the coefficient arrays emitted here are
only their reductions modulo 692717.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import stat
import tempfile
import time
from collections import deque
from pathlib import Path
from typing import Any, Iterable, Sequence

import networkx as nx
from flint import nmod_poly
from sympy import isprime


SCHEMA_ID = "hcs-c59-resolvent-evidence-v1"
PRIME = 692717
DEGREE = 27
EXPECTED_W_ORDER = 51840
EXPECTED_H_ORDER = 162
EXPECTED_COEFFICIENT_HASHES = {
    301: "21b304679d3b77a7b1fae4182e203d8f2652588efffa4a160cccd98ac3e81257",
    303: "76fa8081c92e58839f60659fa7c9979d9b002fae5408cc30777341d21665acb2",
}
# These two embedded permutation groups are the durable C59 definitions of
# the field stabilizers.  ToM 301/303 and the SmallGroup identifiers are
# locators/invariants only; neither this producer nor its evidence consults a
# temporary transport file.  The released C56 certificate remains the sole
# source of the labelled W(E6) generators.
DURABLE_FIELD_SUBGROUPS = {
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
CERTIFICATE_PAYLOAD_KEYS = [
    "artifact_contract", "G0_released_authority_rebind", "G1_primitive_orbit_resolvents",
    "G2_gassmann_minimality", "G3_fixed_fields_and_zeta", "G4_global_arithmetic",
    "G5_tom140_local_algebra", "G6_tom206_local_algebra",
    "G7_independence_scope_release", "written_bridges", "backend_contract",
    "source_contract", "scope_nonclaims", "nonresults", "status",
]
SCOPE_NONCLAIM_KEYS = [
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
EVIDENCE_PAYLOAD_KEYS = [
    "G1_primitive_orbit_resolvents", "authority", "constants", "finite_field",
    "group_and_automorphisms", "integration_contract", "invariants",
    "line_configuration", "object_boundary", "scope_nonclaims", "status",
]
EVIDENCE_SCHEMA_DESCRIPTOR = {
    "document_keys": ["payload", "payload_sha256", "schema_id", "schema_sha256"],
    "payload_keys": EVIDENCE_PAYLOAD_KEYS,
    "scope_nonclaim_keys": sorted(SCOPE_NONCLAIM_KEYS),
    "schema_id": "hcs-c59-resolvent-evidence-source-schema-v1",
    "unknown_fields_rejected": True,
}

Permutation = tuple[int, ...]
Pair = tuple[int, int]
Support = tuple[Pair, ...]


def canonical_bytes(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def compact_bytes(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def compact_sha256(value: Any) -> str:
    return sha256_bytes(compact_bytes(value))


def require_exact_keys(record: dict[str, Any], expected: Iterable[str], label: str) -> None:
    actual = set(record)
    wanted = set(expected)
    if actual != wanted:
        raise ValueError(f"{label} keys differ: missing={sorted(wanted-actual)} extra={sorted(actual-wanted)}")


def evidence_schema_sha256() -> str:
    return compact_sha256(EVIDENCE_SCHEMA_DESCRIPTOR)


def validate_evidence_document(document: dict[str, Any]) -> None:
    """Validate the source-owned evidence envelope used by the top producer."""
    require_exact_keys(document, EVIDENCE_SCHEMA_DESCRIPTOR["document_keys"], "evidence document")
    if document["schema_id"] != SCHEMA_ID:
        raise ValueError("resolvent evidence schema id differs")
    if document["schema_sha256"] != evidence_schema_sha256():
        raise ValueError("resolvent source-owned schema descriptor digest differs")
    payload = document["payload"]
    require_exact_keys(payload, EVIDENCE_PAYLOAD_KEYS, "resolvent evidence payload")
    if document["payload_sha256"] != sha256_bytes(canonical_bytes(payload)):
        raise ValueError("resolvent evidence payload digest differs")
    require_exact_keys(
        payload["authority"],
        {
            "c56_certificate_payload_sha256", "c56_certificate_sha256",
            "c56_manifest_certificate_entry_sha256", "c56_manifest_line_count",
            "c56_manifest_sha256", "durable_field_subgroups_sha256",
            "durable_field_subgroups_source", "machine_contract_semantics_source_owned",
            "released_w_generators_read_from_c56",
        },
        "resolvent authority",
    )
    require_exact_keys(
        payload["integration_contract"],
        {
            "canonical_gate_key", "certificate_payload_keys",
            "live_code_results_entry_count", "planned_result_inventory",
            "planned_source_inventory", "scoped_manifest_entry_count",
        },
        "resolvent integration contract",
    )
    integration = payload["integration_contract"]
    if integration != {
        "canonical_gate_key": "G1_primitive_orbit_resolvents",
        "planned_source_inventory": SOURCE_INVENTORY,
        "planned_result_inventory": RESULT_INVENTORY,
        "certificate_payload_keys": CERTIFICATE_PAYLOAD_KEYS,
        "scoped_manifest_entry_count": 20,
        "live_code_results_entry_count": 21,
    }:
        raise ValueError("resolvent integration contract differs")
    require_exact_keys(payload["scope_nonclaims"], SCOPE_NONCLAIM_KEYS, "resolvent scope")
    if any(value is not False for value in payload["scope_nonclaims"].values()):
        raise ValueError("a resolvent scope nonclaim is not false")
    if payload["object_boundary"] != {
        "eta_is_scaled_integral_invariant": True,
        "exact_characteristic_zero_object": "unexpanded_orbit_product_definition_only",
        "modular_polynomial_claim_only": True,
        "semantic_firewall": "NO_BAD_EULER_OR_ROOT_NUMBER",
    }:
        raise ValueError("resolvent object boundary differs")
    if payload["status"] != {
        "gate": "G1_primitive_orbit_resolvents",
        "evidence_status": "PASS",
        "implementation_state": "EVIDENCE_REPLAY_PASS",
        "release_authorized": False,
    }:
        raise ValueError("resolvent evidence status differs")


def parse_manifest(data: bytes) -> dict[str, str]:
    entries: dict[str, str] = {}
    pattern = re.compile(r"^([0-9a-f]{64})  ([^\n]+)$")
    lines = data.decode().splitlines()
    if not lines:
        raise ValueError("empty C56 manifest")
    for line in lines:
        match = pattern.fullmatch(line)
        if match is None:
            raise ValueError(f"malformed manifest line: {line!r}")
        digest, relative_path = match.groups()
        if relative_path in entries:
            raise ValueError(f"duplicate manifest path: {relative_path}")
        entries[relative_path] = digest
    if list(entries) != sorted(entries):
        raise ValueError("C56 manifest is not path-sorted")
    return entries


def normalize_permutation(values: Sequence[int], one_based: bool) -> Permutation:
    shift = 1 if one_based else 0
    result = tuple(int(value) - shift for value in values)
    if len(result) != DEGREE or sorted(result) != list(range(DEGREE)):
        raise ValueError("invalid degree-27 permutation")
    return result


def compose(left: Permutation, right: Permutation) -> Permutation:
    """Return left after right."""
    return tuple(left[right[index]] for index in range(DEGREE))


def generated_group(generators: Sequence[Permutation]) -> tuple[Permutation, ...]:
    identity = tuple(range(DEGREE))
    seen = {identity}
    queue: deque[Permutation] = deque([identity])
    while queue:
        current = queue.popleft()
        for generator in generators:
            candidate = compose(current, generator)
            if candidate not in seen:
                seen.add(candidate)
                queue.append(candidate)
    return tuple(sorted(seen))


def polynomial_from_roots(roots: Sequence[int], prime: int) -> list[int]:
    coefficients = [1]
    for root in roots:
        updated = [0] * (len(coefficients) + 1)
        for index, coefficient in enumerate(coefficients):
            updated[index] = (updated[index] - root * coefficient) % prime
            updated[index + 1] = (updated[index + 1] + coefficient) % prime
        coefficients = updated
    return coefficients


def evaluate_polynomial(coefficients_low_to_high: Sequence[int], value: int, prime: int) -> int:
    result = 0
    for coefficient in reversed(coefficients_low_to_high):
        result = (result * value + coefficient) % prime
    return result


def sparse_equation_value(equation: list[dict[str, Any]], coordinates: Sequence[int], prime: int) -> int:
    total = 0
    for term in equation:
        monomial = int(term["coefficient"]) % prime
        exponents = term["exponents_abcd"]
        if len(exponents) != 4:
            raise ValueError("sparse equation term is not in a,b,c,d")
        for coordinate, exponent in zip(coordinates, exponents):
            monomial = monomial * pow(coordinate, int(exponent), prime) % prime
        total = (total + monomial) % prime
    return total


def graph_edges_from_lines(lines: Sequence[Sequence[int]], prime: int) -> list[list[int]]:
    edges: list[list[int]] = []
    for left, (a, b, c, d) in enumerate(lines):
        for right in range(left + 1, len(lines)):
            aa, bb, cc, dd = lines[right]
            if ((aa - a) * (dd - d) - (bb - b) * (cc - c)) % prime == 0:
                edges.append([left, right])
    return edges


def degree_multiset(edges: Sequence[Sequence[int]], vertex_count: int) -> list[int]:
    degrees = [0] * vertex_count
    for left, right in edges:
        degrees[left] += 1
        degrees[right] += 1
    return sorted(degrees)


def maps_edges(permutation: Permutation, edges: Sequence[Sequence[int]]) -> bool:
    edge_set = {tuple(edge) for edge in edges}
    return all(tuple(sorted((permutation[left], permutation[right]))) in edge_set for left, right in edges)


def stable_color_cells(adjacency: Sequence[Sequence[int]], fixed_base: Sequence[int]) -> list[list[int]]:
    vertex_count = len(adjacency)
    colors = [0] * vertex_count
    for color, vertex in enumerate(fixed_base, start=1):
        colors[vertex] = color
    while True:
        palette = sorted(set(colors))
        palette_index = {color: index for index, color in enumerate(palette)}
        signatures: list[tuple[int, tuple[int, ...]]] = []
        for vertex in range(vertex_count):
            counts = [0] * len(palette)
            for neighbor, incident in enumerate(adjacency[vertex]):
                if incident == 1:
                    counts[palette_index[colors[neighbor]]] += 1
            signatures.append((colors[vertex], tuple(counts)))
        signature_ids = {signature: index for index, signature in enumerate(sorted(set(signatures)))}
        refined = [signature_ids[signature] for signature in signatures]
        same_partition = all(
            (colors[left] == colors[right]) == (refined[left] == refined[right])
            for left in range(vertex_count)
            for right in range(vertex_count)
        )
        colors = refined
        if same_partition:
            break
    cells_by_color: dict[int, list[int]] = {}
    for vertex, color in enumerate(colors):
        cells_by_color.setdefault(color, []).append(vertex)
    return sorted((sorted(cell) for cell in cells_by_color.values()))


def automorphism_upper_bound_certificate(adjacency: Sequence[Sequence[int]]) -> dict[str, Any]:
    base = [0, 1, 2, 3, 4]
    steps: list[dict[str, Any]] = []
    chosen_cell_sizes: list[int] = []
    for depth in range(len(base) + 1):
        fixed = base[:depth]
        cells = stable_color_cells(adjacency, fixed)
        steps.append(
            {
                "fixed_base": fixed,
                "cells": cells,
                "cell_sizes": sorted(len(cell) for cell in cells),
            }
        )
        if depth < len(base):
            chosen = base[depth]
            chosen_cell = next(cell for cell in cells if chosen in cell)
            chosen_cell_sizes.append(len(chosen_cell))
    upper_bound = 1
    for size in chosen_cell_sizes:
        upper_bound *= size
    if chosen_cell_sizes != [27, 16, 10, 6, 2]:
        raise ValueError(f"unexpected Schlaefli refinement orbit bound: {chosen_cell_sizes}")
    if not all(len(cell) == 1 for cell in steps[-1]["cells"]):
        raise ValueError("Schlaefli refinement base does not make the final partition discrete")
    if upper_bound != EXPECTED_W_ORDER:
        raise ValueError("Schlaefli automorphism upper bound differs from W(E6) order")
    return {
        "method": "individualize_then_equitable_color_refinement_orbit_bound",
        "base": base,
        "chosen_cell_sizes": chosen_cell_sizes,
        "steps": steps,
        "upper_bound": upper_bound,
        "final_partition_discrete": True,
    }


def image_pair(permutation: Permutation, pair: Pair) -> Pair:
    return tuple(sorted((permutation[pair[0]], permutation[pair[1]])))  # type: ignore[return-value]


def image_support(permutation: Permutation, support: Support) -> Support:
    return tuple(sorted(image_pair(permutation, pair) for pair in support))


def orbit_of_pair(group: Sequence[Permutation], seed: Pair) -> Support:
    return tuple(sorted({image_pair(permutation, seed) for permutation in group}))


def support_family(group: Sequence[Permutation], support: Support) -> tuple[Support, ...]:
    return tuple(sorted({image_support(permutation, support) for permutation in group}))


def invariant_values(alpha_by_label: Sequence[int], families: Sequence[Support], prime: int) -> list[int]:
    return [
        sum(alpha_by_label[left] * alpha_by_label[right] for left, right in support) % prime
        for support in families
    ]


def lists_of_permutations(permutations: Sequence[Permutation]) -> list[list[int]]:
    return [list(permutation) for permutation in permutations]


def lists_of_support(support: Support) -> list[list[int]]:
    return [list(pair) for pair in support]


def lists_of_families(families: Sequence[Support]) -> list[list[list[int]]]:
    return [lists_of_support(support) for support in families]


def build_invariant_record(
    index: int,
    field_subgroups: dict[str, Any],
    w_elements: Sequence[Permutation],
    alpha_by_label: Sequence[int],
) -> dict[str, Any]:
    if index == 301:
        seeds: list[Pair] = [(0, 1), (0, 8)]
        expected_component_sizes = [27, 27]
        expected_support_size = 54
    elif index == 303:
        seeds = [(0, 1)]
        expected_component_sizes = [81]
        expected_support_size = 81
    else:
        raise ValueError("unsupported invariant index")

    subgroup = field_subgroups[str(index)]
    if subgroup["tom_locator"] != index:
        raise ValueError(f"H{index} durable locator differs")
    h_generators = tuple(
        normalize_permutation(row, one_based=True)
        for row in subgroup["generators"]
    )
    h_elements = generated_group(h_generators)
    if len(h_elements) != EXPECTED_H_ORDER:
        raise ValueError(f"H{index} order differs from 162")

    components = [orbit_of_pair(h_elements, seed) for seed in seeds]
    if [len(component) for component in components] != expected_component_sizes:
        raise ValueError(f"H{index} support component sizes differ")
    support = tuple(sorted({pair for component in components for pair in component}))
    if len(support) != expected_support_size or sum(map(len, components)) != len(support):
        raise ValueError(f"H{index} support components are not the required disjoint union")

    stabilizer = tuple(permutation for permutation in w_elements if image_support(permutation, support) == support)
    if len(stabilizer) != EXPECTED_H_ORDER or set(stabilizer) != set(h_elements):
        raise ValueError(f"H{index} is not the exact support stabilizer")

    families = support_family(w_elements, support)
    if len(families) != 320:
        raise ValueError(f"H{index} support orbit does not have size 320")
    values = invariant_values(alpha_by_label, families, PRIME)
    if len(set(values)) != 320:
        raise ValueError(f"H{index} modular invariant values collide")
    coefficients = polynomial_from_roots(values, PRIME)
    coefficient_hash = compact_sha256(coefficients)
    if coefficient_hash != EXPECTED_COEFFICIENT_HASHES[index]:
        raise ValueError(f"H{index} coefficient fingerprint differs: {coefficient_hash}")

    h_elements_lists = lists_of_permutations(h_elements)
    stabilizer_lists = lists_of_permutations(stabilizer)
    family_lists = lists_of_families(families)
    return {
        "tom_locator": index,
        "smallgroup_id": [int(value) for value in subgroup["smallgroup_id"]],
        "h_generators": lists_of_permutations(h_generators),
        "h_order": len(h_elements),
        "h_element_inventory_sha256": compact_sha256(h_elements_lists),
        "seed_pairs": [list(seed) for seed in seeds],
        "support_components": [lists_of_support(component) for component in components],
        "support_component_sizes": [len(component) for component in components],
        "support": lists_of_support(support),
        "support_size": len(support),
        "support_stabilizer_order": len(stabilizer),
        "support_stabilizer_equals_h": set(stabilizer) == set(h_elements),
        "support_stabilizer_elements": stabilizer_lists,
        "support_stabilizer_inventory_sha256": compact_sha256(stabilizer_lists),
        "families": family_lists,
        "family_count": len(families),
        "families_sha256": compact_sha256(family_lists),
        "conjugate_values_by_family_order": values,
        "distinct_value_count": len(set(values)),
        "values_sha256": compact_sha256(values),
        "sorted_values_sha256": compact_sha256(sorted(values)),
        "monic_coefficients_low_to_high": coefficients,
        "coefficient_count": len(coefficients),
        "monic_coefficients_sha256": coefficient_hash,
    }


def build_document(
    certificate_path: Path,
    manifest_path: Path,
) -> dict[str, Any]:
    certificate_bytes = certificate_path.read_bytes()
    manifest_bytes = manifest_path.read_bytes()

    certificate = json.loads(certificate_bytes)
    require_exact_keys(certificate, {"schema", "schema_sha256", "payload", "payload_sha256"}, "C56 certificate")
    certificate_payload = certificate["payload"]
    computed_c56_payload_hash = sha256_bytes(compact_bytes(certificate_payload))
    if computed_c56_payload_hash != certificate["payload_sha256"]:
        raise ValueError("C56 certificate payload digest mismatch")

    manifest = parse_manifest(manifest_bytes)
    certificate_entry = manifest.get("results/c56_certificate.json")
    certificate_hash = sha256_bytes(certificate_bytes)
    if certificate_entry != certificate_hash:
        raise ValueError("C56 full manifest does not bind the supplied certificate")

    payload = certificate_payload
    eliminant = [int(value) for value in payload["irreducibility"]["eliminant_coefficients_d_0_to_27"]]
    if len(eliminant) != 28 or eliminant[-1] == 0:
        raise ValueError("invalid C56 degree-27 eliminant")
    shapes = {row["leading_variable"]: row for row in payload["grassmann_main_chart"]["lex_shape"]}
    if set(shapes) != {"a", "b", "c", "d"}:
        raise ValueError("C56 lex shape does not have exactly a,b,c,d rows")
    line_equations = payload["grassmann_main_chart"]["line_equations_sparse"]
    if len(line_equations) != 4:
        raise ValueError("C56 chart does not have four sparse line equations")

    if not isprime(PRIME):
        raise ValueError("split witness is not prime")
    denominator_values = {"eliminant": eliminant[-1]}
    denominator_values.update({f"lex_{name}": int(shapes[name]["leading_coefficient"]) for name in "abcd"})
    denominator_residues = {name: value % PRIME for name, value in denominator_values.items()}
    if not all(denominator_residues.values()):
        raise ValueError("split witness meets the line-reconstruction denominator envelope")

    eliminant_mod = [coefficient % PRIME for coefficient in eliminant]
    polynomial = nmod_poly(eliminant_mod, PRIME)
    factorization = polynomial.factor()[1]
    degree_counts: dict[int, int] = {}
    roots: list[int] = []
    for factor, exponent in factorization:
        degree = factor.degree()
        degree_counts[degree] = degree_counts.get(degree, 0) + int(exponent)
        if degree == 1 and int(exponent) == 1:
            roots.append((-int(factor[0]) * pow(int(factor[1]), -1, PRIME)) % PRIME)
    roots.sort()
    factor_degrees = [[degree, degree_counts[degree]] for degree in sorted(degree_counts)]
    if factor_degrees != [[1, 27]] or len(roots) != 27 or len(set(roots)) != 27:
        raise ValueError("eliminant does not split squarefreely as 1^27")
    inverse_leading = pow(eliminant_mod[-1], -1, PRIME)
    normalized_eliminant = [(coefficient * inverse_leading) % PRIME for coefficient in eliminant_mod]
    multiplyback = polynomial_from_roots(roots, PRIME)
    if multiplyback != normalized_eliminant:
        raise ValueError("split factorization does not multiply back to the normalized eliminant")

    lines: list[list[int]] = []
    for d_coordinate in roots:
        coordinates: dict[str, int] = {"d": d_coordinate}
        for name in "abc":
            row = shapes[name]
            tail_value = evaluate_polynomial(row["tail_coefficients_d_0_up"], d_coordinate, PRIME)
            coordinates[name] = (-tail_value * pow(int(row["leading_coefficient"]) % PRIME, -1, PRIME)) % PRIME
        lines.append([coordinates[name] for name in "abcd"])
    equation_residues = [
        [sparse_equation_value(equation, coordinates, PRIME) for equation in line_equations]
        for coordinates in lines
    ]
    if any(value != 0 for row in equation_residues for value in row):
        raise ValueError("a reconstructed modular line fails a chart equation")

    actual_edges = graph_edges_from_lines(lines, PRIME)
    actual_degrees = degree_multiset(actual_edges, DEGREE)
    if len(actual_edges) != 135 or actual_degrees != [10] * DEGREE:
        raise ValueError("reconstructed line graph is not 135-edge 10-regular")
    standard_matrix = payload["we6"]["line_class_intersection_matrix"]
    if len(standard_matrix) != DEGREE or any(len(row) != DEGREE for row in standard_matrix):
        raise ValueError("invalid released line-incidence matrix")
    standard_edges = [
        [left, right]
        for left in range(DEGREE)
        for right in range(left + 1, DEGREE)
        if int(standard_matrix[left][right]) == 1
    ]
    if len(standard_edges) != 135 or degree_multiset(standard_edges, DEGREE) != [10] * DEGREE:
        raise ValueError("released Schlaefli graph is not 135-edge 10-regular")

    c56_w_generators = tuple(
        normalize_permutation(row, one_based=False)
        for row in payload["we6"]["simple_reflection_line_permutations"]
    )
    released_w_generators = c56_w_generators
    w_elements = generated_group(released_w_generators)
    if len(w_elements) != EXPECTED_W_ORDER:
        raise ValueError("released W generators do not generate order 51840")
    if not all(maps_edges(permutation, standard_edges) for permutation in w_elements):
        raise ValueError("a generated W element fails to preserve the released Schlaefli graph")

    actual_graph = nx.Graph()
    actual_graph.add_nodes_from(range(DEGREE))
    actual_graph.add_edges_from(tuple(edge) for edge in actual_edges)
    standard_graph = nx.Graph()
    standard_graph.add_nodes_from(range(DEGREE))
    standard_graph.add_edges_from(tuple(edge) for edge in standard_edges)
    matcher = nx.algorithms.isomorphism.GraphMatcher(actual_graph, standard_graph)
    raw_mapping_dict = next(matcher.isomorphisms_iter(), None)
    if raw_mapping_dict is None:
        raise ValueError("reconstructed line graph is not isomorphic to the released graph")
    raw_mapping = tuple(int(raw_mapping_dict[index]) for index in range(DEGREE))
    canonical_mapping = min(
        tuple(permutation[raw_mapping[index]] for index in range(DEGREE))
        for permutation in w_elements
    )
    if sorted(canonical_mapping) != list(range(DEGREE)):
        raise ValueError("graph mapping is not a permutation")
    actual_edge_set = {tuple(edge) for edge in actual_edges}
    standard_edge_set = {tuple(edge) for edge in standard_edges}
    if {
        tuple(sorted((canonical_mapping[left], canonical_mapping[right])))
        for left, right in actual_edge_set
    } != standard_edge_set:
        raise ValueError("canonical map is not a graph isomorphism")

    d_by_standard = [0] * DEGREE
    for actual_label, standard_label in enumerate(canonical_mapping):
        d_by_standard[standard_label] = roots[actual_label]
    leading_coefficient_mod_prime = eliminant[-1] % PRIME
    alpha_by_standard = [leading_coefficient_mod_prime * value % PRIME for value in d_by_standard]

    automorphism_certificate = automorphism_upper_bound_certificate(standard_matrix)
    if automorphism_certificate["upper_bound"] != len(w_elements):
        raise ValueError("W inclusion and color-refinement upper bound do not meet")

    w_generators_lists = lists_of_permutations(released_w_generators)
    w_elements_lists = lists_of_permutations(w_elements)
    line_record = {
        "line_coordinates_abcd_by_root_order": lines,
        "line_coordinates_sha256": compact_sha256(lines),
        "equation_residues_by_root_order": equation_residues,
        "all_equation_residues_zero": True,
        "actual_edges": actual_edges,
        "actual_edges_sha256": compact_sha256(actual_edges),
        "actual_degree_multiset": actual_degrees,
        "standard_edges": standard_edges,
        "standard_edges_sha256": compact_sha256(standard_edges),
        "actual_to_standard_label": list(canonical_mapping),
        "mapping_sha256": compact_sha256(list(canonical_mapping)),
        "mapping_is_graph_isomorphism": True,
        "d_by_standard_label": d_by_standard,
        "alpha_by_standard_label": alpha_by_standard,
    }

    invariant_records = {
        "301": build_invariant_record(301, DURABLE_FIELD_SUBGROUPS, w_elements, alpha_by_standard),
        "303": build_invariant_record(303, DURABLE_FIELD_SUBGROUPS, w_elements, alpha_by_standard),
    }
    evidence_payload = {
        "authority": {
            "c56_certificate_sha256": certificate_hash,
            "c56_certificate_payload_sha256": computed_c56_payload_hash,
            "c56_manifest_sha256": sha256_bytes(manifest_bytes),
            "c56_manifest_line_count": len(manifest),
            "c56_manifest_certificate_entry_sha256": certificate_entry,
            "durable_field_subgroups_sha256": compact_sha256(DURABLE_FIELD_SUBGROUPS),
            "durable_field_subgroups_source": "C59_SOURCE_OWNED_CONSTANTS",
            "machine_contract_semantics_source_owned": True,
            "released_w_generators_read_from_c56": True,
        },
        "integration_contract": {
            "canonical_gate_key": "G1_primitive_orbit_resolvents",
            "planned_source_inventory": SOURCE_INVENTORY,
            "planned_result_inventory": RESULT_INVENTORY,
            "certificate_payload_keys": CERTIFICATE_PAYLOAD_KEYS,
            "scoped_manifest_entry_count": 20,
            "live_code_results_entry_count": 21,
        },
        "G1_primitive_orbit_resolvents": {
            "frozen_w_h_arrays_bound": True,
            "support_component_sizes": {"301": [27, 27], "303": [81]},
            "integral_normalization": "alpha_i=L*d_i",
            "scaled_invariant_name": "eta",
            "split_prime": PRIME,
            "factor_degrees": [[1, 27]],
            "multiplyback_proven": True,
            "all_27_lines_all_4_equations": True,
            "schlaefli_graph_parameters": {"vertices": 27, "edges": 135, "degree": 10},
            "aut_graph_equals_released_w_permutation_set": True,
            "aut_graph_order": 51840,
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
            "prime": PRIME,
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
            "normalized_monic_eliminant_low_to_high": normalized_eliminant,
            "factor_degrees": factor_degrees,
            "roots_sorted": roots,
            "roots_sha256": compact_sha256(roots),
            "multiplyback_monic_low_to_high": multiplyback,
            "multiplyback_matches_normalized_eliminant": True,
        },
        "line_configuration": line_record,
        "group_and_automorphisms": {
            "w_generators": w_generators_lists,
            "w_generators_sha256": compact_sha256(w_generators_lists),
            "frozen_w_generators_match_c56": True,
            "w_order": len(w_elements),
            "w_element_inventory_sha256": compact_sha256(w_elements_lists),
            "all_w_elements_preserve_standard_graph": True,
            "automorphism_upper_bound_certificate": automorphism_certificate,
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
        "scope_nonclaims": {key: False for key in SCOPE_NONCLAIM_KEYS},
        "status": {
            "gate": "G1_primitive_orbit_resolvents",
            "evidence_status": "PASS",
            "implementation_state": "EVIDENCE_REPLAY_PASS",
            "release_authorized": False,
        },
    }
    document = {
        "schema_id": SCHEMA_ID,
        "schema_sha256": evidence_schema_sha256(),
        "payload_sha256": sha256_bytes(canonical_bytes(evidence_payload)),
        "payload": evidence_payload,
    }
    validate_evidence_document(document)
    return document


STAGE_NAME_PATTERN = re.compile(r"^\.c59-stage-[A-Za-z0-9]{8}$")
EVIDENCE_BASENAME = "c59_resolvent_evidence.json"


def staged_path(value: str, expected_basename: str) -> tuple[Path, Path, tuple[int, int]]:
    """Bind a fixed target in the runner-owned canonical results stage."""

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
        raise ValueError(
            "target must have its fixed basename directly under one real "
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
        raise ValueError("canonical results stage changed during resolvent replay")


def validate_existing_stage_file(path: Path) -> tuple[int, int, int, int]:
    if path.is_symlink() or not path.is_file():
        raise ValueError("existing stage target must be a regular non-symlink file")
    metadata = path.stat()
    if metadata.st_nlink != 1:
        raise ValueError("existing stage target must have link count one")
    return (metadata.st_dev, metadata.st_ino, metadata.st_size, metadata.st_mtime_ns)


def stable_file_bytes(path: Path) -> tuple[bytes, tuple[int, ...]]:
    if path.is_symlink() or not path.is_file():
        raise ValueError(f"authority must be a regular non-symlink file: {path}")
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
        raise ValueError(f"authority changed while being read: {path}")
    return data, identity


def atomic_write(path: Path, data: bytes) -> None:
    descriptor, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary_name, path)
    finally:
        if os.path.exists(temporary_name):
            os.unlink(temporary_name)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--certificate", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    destination = parser.add_mutually_exclusive_group(required=True)
    destination.add_argument("--output")
    destination.add_argument("--check-existing")
    arguments = parser.parse_args()

    selected = arguments.output if arguments.output is not None else arguments.check_existing
    target_path, stage_directory, stage_identity = staged_path(
        selected, EVIDENCE_BASENAME
    )
    existing_identity = None
    if arguments.check_existing is not None:
        existing_identity = validate_existing_stage_file(target_path)
    elif os.path.lexists(target_path):
        validate_existing_stage_file(target_path)

    certificate_path = arguments.certificate.resolve()
    manifest_path = arguments.manifest.resolve()
    certificate_before = stable_file_bytes(certificate_path)
    manifest_before = stable_file_bytes(manifest_path)
    evidence_before = (
        stable_file_bytes(target_path) if arguments.check_existing is not None else None
    )
    started = time.perf_counter()
    assert_stage_identity(stage_directory, stage_identity)
    document = build_document(
        certificate_path,
        manifest_path,
    )
    encoded = canonical_bytes(document)
    assert_stage_identity(stage_directory, stage_identity)
    if (
        stable_file_bytes(certificate_path) != certificate_before
        or stable_file_bytes(manifest_path) != manifest_before
    ):
        raise ValueError("released C56 authority changed during resolvent replay")
    if arguments.output is not None:
        atomic_write(target_path, encoded)
        mode = "write"
        target = target_path.name
    else:
        if validate_existing_stage_file(target_path) != existing_identity:
            raise ValueError("existing evidence identity changed during replay")
        rebound_evidence = stable_file_bytes(target_path)
        if rebound_evidence != evidence_before or rebound_evidence[0] != encoded:
            raise ValueError("existing evidence is not byte-identical to a fresh rebuild")
        mode = "replay"
        target = target_path.name
    summary = {
        "mode": mode,
        "status": "PASS",
        "target": target,
        "evidence_sha256": sha256_bytes(encoded),
        "payload_sha256": document["payload_sha256"],
        "bytes": len(encoded),
        "elapsed_seconds": round(time.perf_counter() - started, 6),
    }
    print(json.dumps(summary, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
