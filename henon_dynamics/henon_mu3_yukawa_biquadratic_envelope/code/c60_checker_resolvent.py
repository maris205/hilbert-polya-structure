#!/usr/bin/env python3
"""Independent checker for HCS-C60 primitive-resolvent evidence.

The reconstruction callable takes explicit paths, contains its own group and
polynomial algorithms, and never imports the C60 producer or an external module.
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


SCHEMA_ID = "hcs-c60-resolvent-evidence-v1"
SCOPE_LITERAL = "NO_BAD_EULER_OR_ROOT_NUMBER"
PRIME = 692717
DEGREE = 27
W_ORDER = 51840
EXPECTED_GROUP_ORDERS = [162, 162, 162, 162, 324, 81]
EXPECTED_DEGREES = {"M": 160, "F0": 320, "L": 640}
EXPECTED_COEFFICIENT_HASHES = {
    "M": "b8818888c1ceb83e05d2f2df045e9d6e418f1ea18a5f019d1398e4cd0a59ef6b",
    "F0": "ffe9439cd390729bbb0dd7ffa4c6a1045c7fbc9c645e0f37e75c71d1e786e10d",
    "L": "c82feda40496156b7d006de4e47a1b808b3cf3ffffe4a386652d3e3fa77861f1",
}
EXPECTED_INPUT_HASHES = {
    "c59_resolvent_module": "d4f70749054680487fdf2a2d41d11f4cbf184d03a4084c445d2d49837b5b712b",
    "c59_resolvent_evidence": "667e0eeb04e5724b620bf513f9556a321dfd39f9215396ed1840ca83879ec6a6",
    "c59_full_manifest": "4d756452d5b6d981e5fe4de3991cf6b7838f74fb8c411027a91dc2cf89a8d1a4",
    "c59_route": "fab227cc8e83155e39793d665ea721e46522d5beee77a113a19379b64b2130c5",
}
EXPECTED_C59_PAYLOAD_HASH = "3d6a4d8018ce15ea07d64ffa5c955af7ad4c60b041aa2e1884617648cfe20cdc"
EXPECTED_C59_IMPLEMENTATION_COMMIT = "6c806120f17dab2e7b0bca37fcc156dfc459a4b7"
EXPECTED_C59_RELEASE_COMMIT = "961c45f4b0c66ec94d2f069fd9ecc9d4b529d03a"

# Independently duplicated C60 durable definitions; do not import producer.
H0_GENERATORS_ONE_BASED = [
    [2,18,23,21,20,11,24,15,26,25,22,3,9,10,19,5,4,1,8,16,17,6,12,27,14,13,7],
    [13,9,6,16,27,19,17,23,10,2,8,22,14,1,12,24,20,26,3,7,5,15,11,4,18,25,21],
    [15,12,4,14,25,7,10,27,8,6,17,24,11,3,21,26,13,22,5,18,1,20,16,2,19,23,9],
    [1,2,19,21,20,3,24,11,9,10,23,15,13,14,22,5,4,18,6,16,17,12,8,27,25,26,7],
    [20,5,3,2,9,11,10,8,7,4,6,23,24,21,19,26,18,16,15,13,1,22,12,14,17,27,25],
]
N_GENERATORS_ONE_BASED = [
    [1,18,22,16,17,12,27,8,25,26,23,6,14,13,19,4,5,2,15,21,20,3,11,24,9,10,7],
    [15,12,4,14,25,7,10,27,8,6,17,24,11,3,21,26,13,22,5,18,1,20,16,2,19,23,9],
    [1,2,19,21,20,3,24,11,9,10,23,15,13,14,22,5,4,18,6,16,17,12,8,27,25,26,7],
    [14,10,3,7,4,6,5,8,2,9,11,12,1,13,15,17,27,25,19,21,24,22,23,20,26,18,16],
    [18,1,15,4,5,12,7,6,13,14,3,8,26,25,11,16,17,2,22,20,21,23,19,24,10,9,27],
    [1,13,16,12,6,5,8,7,9,26,27,4,2,18,17,3,15,14,20,19,22,21,24,23,25,10,11],
]
J_GENERATORS_ONE_BASED = [
    [1,2,6,17,16,19,27,23,9,10,8,22,13,14,12,20,21,18,3,5,4,15,11,7,25,26,24],
    [2,18,11,4,5,8,7,12,26,25,15,6,9,10,3,16,17,1,23,20,21,19,22,24,14,13,27],
    [3,6,5,2,1,4,18,17,12,8,16,21,15,11,20,14,10,19,7,13,9,24,27,26,23,22,25],
]
TRANSPORT_X_ONE_BASED = [1,15,14,13,22,12,27,26,25,7,24,16,17,6,19,18,5,20,4,21,3,2,11,10,9,23,8]
F0_CUBIC_SUPPORT = [
    [0,1,8],[0,12,17],[0,13,24],[1,9,13],[1,17,25],[2,5,11],[2,10,22],
    [2,14,18],[3,4,20],[3,6,23],[3,15,16],[4,6,19],[4,15,26],[5,7,10],
    [5,18,21],[6,16,26],[7,11,14],[7,18,22],[8,9,12],[8,24,25],[9,17,24],
    [10,14,21],[11,21,22],[12,13,25],[15,19,23],[16,19,20],[20,23,26],
]
DURABLE_GROUP_LITERALS = {
    "H0_generators_one_based": H0_GENERATORS_ONE_BASED,
    "J_generators_one_based": J_GENERATORS_ONE_BASED,
    "N_generators_one_based": N_GENERATORS_ONE_BASED,
    "transport_x_one_based": TRANSPORT_X_ONE_BASED,
}
DURABLE_CARRIER_LITERALS = {
    "F0_cubic_support": F0_CUBIC_SUPPORT,
    "Hplus_support_seeds_zero_based": [[0, 1], [0, 8]],
    "Hminus_support_seed_zero_based": [0, 1],
    "L_support_weights_Hplus_H3": [1, 2],
}

DOCUMENT_KEYS = ["payload", "payload_sha256", "schema_id", "schema_sha256"]
PAYLOAD_KEYS = [
    "authority", "carriers", "constants", "fixed_field_bridge", "groups",
    "invariant_degree_obstruction", "replay_contract", "scope", "status", "transport",
]
AUTHORITY_KEYS = [
    "c60_durable_carrier_literals_sha256", "c60_durable_group_literals_sha256",
    "c59_full_manifest_entry_count", "c59_full_manifest_sha256",
    "c59_implementation_commit", "c59_release_commit",
    "c59_resolvent_evidence_sha256", "c59_resolvent_module_sha256",
    "c59_resolvent_payload_sha256", "c59_route_archive_sha256",
    "c59_route_sha256", "released_c59_rebound",
]
CONSTANT_KEYS = ["degree", "expected_coefficient_hashes", "expected_orbit_degrees", "prime", "scope_literal", "w_order"]
TRANSPORT_KEYS = [
    "H301_intersection_H3_order", "H3_contained_in_N",
    "H3_equals_transported_support_stabilizer", "H3_order", "convention",
    "label_permutation_one_based", "transported_support_stabilizer_order",
]
GROUP_KEYS = [
    "H0_generators_sha256", "H3_generators_sha256", "Hminus_generators_sha256",
    "Hplus_generators_sha256", "J_generators_sha256", "N_generators_sha256",
    "orders_Hplus_H0_Hminus_H3_N_J",
]
CARRIER_KEYS = [
    "carrier", "carrier_sha256", "label", "modular_polynomial", "monomial_degree",
    "nonzero_monomial_count", "orbit_size", "stabilizer_equals_expected",
    "stabilizer_order", "weight_histogram",
]
POLYNOMIAL_KEYS = ["coefficient_count", "coefficient_sha256", "distinct_value_count", "sorted_values_sha256", "value_count", "values_sha256"]
OBSTRUCTION_KEYS = [
    "H0_and_N_point_partitions_equal", "H0_and_N_unordered_pair_partitions_equal",
    "H0_pair_orbit_sizes", "H0_pair_partition_sha256", "H0_point_orbit_sizes",
    "H0_point_partition_sha256", "formal_polynomial_scope", "selected_cubic_orbit_size",
    "selected_cubic_support_sha256",
]
BRIDGE_KEYS = [
    "K_completely_split_witness", "c59_all_27_line_equations_zero", "c59_factor_degrees",
    "c59_label_map_is_graph_isomorphism", "c59_split_roots_distinct",
    "characteristic_zero_orbit_values_distinct", "fixed_field_identities",
    "fixed_field_reason", "labelled_W_action_faithful",
    "modular_distinct_value_counts", "prime_unramified",
    "support_stabilizers_exact_on_Z_labelled_carrier",
]
REPLAY_KEYS = ["builder_basename", "canonical_stage_pattern", "checker_basename", "durable_literals_source", "evidence_basename", "group_evidence_policy", "schema_basename"]
SCOPE_KEYS = [
    "bad_artin_euler_claimed", "bad_euler_or_root_number_claimed",
    "characteristic_zero_coefficients_claimed", "class_number_claimed",
    "decomposition_frobenius_claimed", "local_fields_classified_by_tuples",
    "maximal_orders_claimed", "target_selection_or_unpromoted_aids_are_authority",
    "root_number_claimed", "scope_literal",
]
TRANSPORT_CONVENTION = "left label-map action: Stab(x*Sminus)=x*Hminus*x^-1=GAP(Hminus^x)"
FIXED_FIELD_REASON = "the released squarefree 1^27 labelled split and 51840 distinct labelled W(E6) permutations prove faithful action and Frobenius identity in K; pairwise-distinct good reductions force characteristic-zero orbit values distinct, so orbit-stabilizer and Galois correspondence identify each generated field"
EXPECTED_CARRIER_LABELS = {
    "F0": "F0=K^H0 cubic carrier",
    "L": "L=K^J colored carrier",
    "M": "M=K^N trace carrier",
}
EXPECTED_MONOMIAL_DEGREES = {"F0": 3, "L": 2, "M": 2}
EXPECTED_STABILIZER_ORDERS = {"F0": 162, "L": 81, "M": 324}
EXPECTED_FIXED_FIELD_IDENTITIES = {
    "F0": "Q(xi0)=K^H0", "L": "Q(lambda)=K^J", "M": "Q(mu)=K^N",
}
EXPECTED_REPLAY_CONTRACT = {
    "builder_basename": "c60_resolvent.py",
    "canonical_stage_pattern": ".c60-stage-XXXXXXXX",
    "checker_basename": "c60_checker_resolvent.py",
    "durable_literals_source": "C60_SOURCE_OWNED_CONSTANTS",
    "evidence_basename": "c60_resolvent_evidence.json",
    "group_evidence_policy": "C60_GROUP_EVIDENCE_G3_CROSS_CHECK_REQUIRED",
    "schema_basename": "c60_resolvent_schema.json",
}
EXPECTED_STATUS = {
    "evidence_status": "PASS",
    "implementation_state": "EVIDENCE_REPLAY_PASS",
    "release_authorized": False,
}
SCHEMA_DESCRIPTOR = {
    "schema_id": SCHEMA_ID,
    "document_keys": DOCUMENT_KEYS,
    "payload_keys": PAYLOAD_KEYS,
    "authority_keys": AUTHORITY_KEYS,
    "constant_keys": CONSTANT_KEYS,
    "transport_keys": TRANSPORT_KEYS,
    "group_keys": GROUP_KEYS,
    "carrier_names": ["F0", "L", "M"],
    "carrier_keys": CARRIER_KEYS,
    "polynomial_keys": POLYNOMIAL_KEYS,
    "obstruction_keys": OBSTRUCTION_KEYS,
    "fixed_field_bridge_keys": BRIDGE_KEYS,
    "replay_keys": REPLAY_KEYS,
    "scope_keys": SCOPE_KEYS,
    "status_keys": ["evidence_status", "implementation_state", "release_authorized"],
    "strict_builtin_types": True,
    "unknown_fields_rejected": True,
}

Permutation = tuple[int, ...]
Monomial = tuple[int, ...]
Carrier = tuple[tuple[Monomial, int], ...]


def canonical_bytes(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def compact_bytes(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def compact_sha256(value: Any) -> str:
    return sha256_bytes(compact_bytes(value))


def stable_file_bytes(path: Path) -> tuple[bytes, tuple[int, ...]]:
    before = os.lstat(path)
    if not stat.S_ISREG(before.st_mode) or before.st_nlink != 1:
        raise ValueError(f"authority must be one regular non-symlink file: {path}")
    data = path.read_bytes()
    after = os.lstat(path)
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


def file_sha256(path: Path) -> str:
    return sha256_bytes(stable_file_bytes(path)[0])


def exact_keys(value: Any, expected: Iterable[str], label: str) -> None:
    if type(value) is not dict:
        raise ValueError(f"{label}: expected built-in dict")
    actual, wanted = set(value), set(expected)
    if actual != wanted:
        raise ValueError(f"{label}: key mismatch missing={sorted(wanted-actual)} extra={sorted(actual-wanted)}")


def exact_type(value: Any, expected: type, label: str) -> None:
    if type(value) is not expected:
        raise ValueError(f"{label}: expected exact {expected.__name__}")


def digest(value: Any, label: str) -> None:
    exact_type(value, str, label)
    if re.fullmatch(r"[0-9a-f]{64}", value) is None:
        raise ValueError(f"{label}: malformed SHA-256")


def validate_schema(schema: Any) -> None:
    if schema != SCHEMA_DESCRIPTOR:
        raise ValueError("schema descriptor differs from checker-owned contract")


def validate_document_shape(document: Any) -> None:
    exact_keys(document, DOCUMENT_KEYS, "document")
    if document["schema_id"] != SCHEMA_ID or document["schema_sha256"] != compact_sha256(SCHEMA_DESCRIPTOR):
        raise ValueError("document schema binding differs")
    digest(document["payload_sha256"], "payload_sha256")
    payload = document["payload"]
    exact_keys(payload, PAYLOAD_KEYS, "payload")
    if document["payload_sha256"] != sha256_bytes(canonical_bytes(payload)):
        raise ValueError("payload digest differs")
    exact_keys(payload["authority"], AUTHORITY_KEYS, "authority")
    exact_keys(payload["constants"], CONSTANT_KEYS, "constants")
    exact_keys(payload["transport"], TRANSPORT_KEYS, "transport")
    exact_keys(payload["groups"], GROUP_KEYS, "groups")
    exact_keys(payload["carriers"], ["F0", "L", "M"], "carriers")
    exact_keys(payload["fixed_field_bridge"], BRIDGE_KEYS, "fixed_field_bridge")
    exact_keys(payload["invariant_degree_obstruction"], OBSTRUCTION_KEYS, "obstruction")
    exact_keys(payload["replay_contract"], REPLAY_KEYS, "replay_contract")
    exact_keys(payload["scope"], SCOPE_KEYS, "scope")

    authority = payload["authority"]
    for key, value in authority.items():
        if key.endswith("sha256"):
            digest(value, f"authority.{key}")
    for key in ["c59_implementation_commit", "c59_release_commit"]:
        exact_type(authority[key], str, f"authority.{key}")
        if re.fullmatch(r"[0-9a-f]{40}", authority[key]) is None:
            raise ValueError(f"authority.{key}: malformed commit")
    exact_type(authority["c59_full_manifest_entry_count"], int, "manifest count")
    exact_type(authority["released_c59_rebound"], bool, "authority.released_c59_rebound")
    if not authority["released_c59_rebound"]:
        raise ValueError("authority firewall differs")
    if authority["c60_durable_group_literals_sha256"] != compact_sha256(DURABLE_GROUP_LITERALS):
        raise ValueError("durable group literal digest differs")
    if authority["c60_durable_carrier_literals_sha256"] != compact_sha256(DURABLE_CARRIER_LITERALS):
        raise ValueError("durable carrier literal digest differs")

    expected_constants = {
        "degree": DEGREE, "prime": PRIME, "w_order": W_ORDER,
        "expected_orbit_degrees": EXPECTED_DEGREES,
        "expected_coefficient_hashes": EXPECTED_COEFFICIENT_HASHES,
        "scope_literal": SCOPE_LITERAL,
    }
    if payload["constants"] != expected_constants:
        raise ValueError("constants differ")

    transport = payload["transport"]
    exact_type(transport["convention"], str, "transport convention")
    exact_type(transport["label_permutation_one_based"], list, "transport permutation")
    for position, label in enumerate(transport["label_permutation_one_based"]):
        exact_type(label, int, f"transport permutation[{position}]")
    if sorted(transport["label_permutation_one_based"]) != list(range(1, 28)):
        raise ValueError("transport permutation invalid")
    for key in ["H3_contained_in_N", "H3_equals_transported_support_stabilizer"]:
        exact_type(transport[key], bool, f"transport.{key}")
        if not transport[key]:
            raise ValueError(f"transport.{key} false")
    for key in ["H301_intersection_H3_order", "H3_order", "transported_support_stabilizer_order"]:
        exact_type(transport[key], int, f"transport.{key}")
    if transport != {
        "H301_intersection_H3_order": 81,
        "H3_contained_in_N": True,
        "H3_equals_transported_support_stabilizer": True,
        "H3_order": 162,
        "convention": TRANSPORT_CONVENTION,
        "label_permutation_one_based": TRANSPORT_X_ONE_BASED,
        "transported_support_stabilizer_order": 162,
    }:
        raise ValueError("transport record differs from checker durable literals")

    groups = payload["groups"]
    for key, value in groups.items():
        if key.endswith("sha256"):
            digest(value, f"groups.{key}")
    exact_type(groups["orders_Hplus_H0_Hminus_H3_N_J"], list, "group order vector")
    for position, order in enumerate(groups["orders_Hplus_H0_Hminus_H3_N_J"]):
        exact_type(order, int, f"group order vector[{position}]")
    if groups["orders_Hplus_H0_Hminus_H3_N_J"] != EXPECTED_GROUP_ORDERS:
        raise ValueError("group order vector differs")

    for name, record in payload["carriers"].items():
        exact_keys(record, CARRIER_KEYS, f"carrier {name}")
        exact_type(record["label"], str, f"carrier {name}.label")
        digest(record["carrier_sha256"], f"carrier {name}.carrier_sha256")
        exact_type(record["carrier"], list, f"carrier {name}.carrier")
        for key in ["monomial_degree", "nonzero_monomial_count", "orbit_size", "stabilizer_order"]:
            exact_type(record[key], int, f"carrier {name}.{key}")
        exact_type(record["stabilizer_equals_expected"], bool, f"carrier {name}.stabilizer flag")
        exact_keys(record["weight_histogram"], ["1", "2"], f"carrier {name}.weight histogram")
        for count in record["weight_histogram"].values():
            exact_type(count, int, f"carrier {name}.weight count")
        for term in record["carrier"]:
            exact_type(term, list, f"carrier {name}.term")
            if len(term) != 2:
                raise ValueError(f"carrier {name}: malformed term")
            monomial, coefficient = term
            exact_type(monomial, list, f"carrier {name}.monomial")
            exact_type(coefficient, int, f"carrier {name}.coefficient")
            if len(monomial) != record["monomial_degree"] or monomial != sorted(set(monomial)) or coefficient not in {1, 2}:
                raise ValueError(f"carrier {name}: invalid monomial/coefficient")
            if any(type(index) is not int or not 0 <= index < DEGREE for index in monomial):
                raise ValueError(f"carrier {name}: invalid label")
        polynomial = record["modular_polynomial"]
        exact_keys(polynomial, POLYNOMIAL_KEYS, f"carrier {name}.polynomial")
        for key in ["coefficient_count", "distinct_value_count", "value_count"]:
            exact_type(polynomial[key], int, f"carrier {name}.polynomial.{key}")
        for key in ["coefficient_sha256", "sorted_values_sha256", "values_sha256"]:
            digest(polynomial[key], f"carrier {name}.polynomial.{key}")
        expected_histogram = {"1": 0, "2": 0}
        for _, coefficient in record["carrier"]:
            expected_histogram[str(coefficient)] += 1
        if (
            record["label"] != EXPECTED_CARRIER_LABELS[name]
            or record["monomial_degree"] != EXPECTED_MONOMIAL_DEGREES[name]
            or record["nonzero_monomial_count"] != len(record["carrier"])
            or record["weight_histogram"] != expected_histogram
            or record["stabilizer_order"] != EXPECTED_STABILIZER_ORDERS[name]
            or not record["stabilizer_equals_expected"]
            or record["orbit_size"] != EXPECTED_DEGREES[name]
        ):
            raise ValueError(f"carrier {name}: metadata differs")

    obstruction = payload["invariant_degree_obstruction"]
    for key in ["H0_and_N_point_partitions_equal", "H0_and_N_unordered_pair_partitions_equal"]:
        exact_type(obstruction[key], bool, f"obstruction.{key}")
        if not obstruction[key]:
            raise ValueError(f"obstruction.{key} false")
    for key in ["H0_pair_partition_sha256", "H0_point_partition_sha256", "selected_cubic_support_sha256"]:
        digest(obstruction[key], f"obstruction.{key}")
    if obstruction["H0_point_orbit_sizes"] != [27] or obstruction["H0_pair_orbit_sizes"] != [27, 27, 54, 81, 162] or obstruction["selected_cubic_orbit_size"] != 27:
        raise ValueError("obstruction scalar contract differs")
    exact_type(obstruction["formal_polynomial_scope"], str, "formal scope")

    bridge = payload["fixed_field_bridge"]
    for key in ["K_completely_split_witness", "c59_all_27_line_equations_zero", "c59_label_map_is_graph_isomorphism", "c59_split_roots_distinct", "characteristic_zero_orbit_values_distinct", "labelled_W_action_faithful", "prime_unramified"]:
        exact_type(bridge[key], bool, f"bridge.{key}")
        if not bridge[key]:
            raise ValueError(f"bridge.{key} false")
    exact_type(bridge["c59_factor_degrees"], list, "bridge factor degrees")
    for position, row in enumerate(bridge["c59_factor_degrees"]):
        exact_type(row, list, f"bridge factor degrees[{position}]")
        for inner, scalar in enumerate(row):
            exact_type(scalar, int, f"bridge factor degrees[{position}][{inner}]")
    exact_type(bridge["modular_distinct_value_counts"], dict, "bridge modular counts")
    for name, count in bridge["modular_distinct_value_counts"].items():
        exact_type(count, int, f"bridge modular count {name}")
    if bridge["c59_factor_degrees"] != [[1, 27]] or bridge["modular_distinct_value_counts"] != EXPECTED_DEGREES:
        raise ValueError("bridge split/count contract differs")
    exact_type(bridge["support_stabilizers_exact_on_Z_labelled_carrier"], dict, "bridge stabilizers")
    for name, flag in bridge["support_stabilizers_exact_on_Z_labelled_carrier"].items():
        exact_type(flag, bool, f"bridge stabilizer {name}")
    if bridge["support_stabilizers_exact_on_Z_labelled_carrier"] != {"F0": True, "L": True, "M": True}:
        raise ValueError("bridge formal stabilizers differ")
    exact_type(bridge["fixed_field_identities"], dict, "bridge identities")
    for name, identity in bridge["fixed_field_identities"].items():
        exact_type(identity, str, f"bridge identity {name}")
    if bridge["fixed_field_identities"] != EXPECTED_FIXED_FIELD_IDENTITIES:
        raise ValueError("bridge field identities differ")
    exact_type(bridge["fixed_field_reason"], str, "bridge reason")
    if bridge["fixed_field_reason"] != FIXED_FIELD_REASON:
        raise ValueError("bridge reason differs")

    replay = payload["replay_contract"]
    for key, value in replay.items():
        exact_type(value, str, f"replay.{key}")
    if replay != EXPECTED_REPLAY_CONTRACT:
        raise ValueError("replay contract differs")

    scope = payload["scope"]
    for key, value in scope.items():
        exact_type(value, str if key == "scope_literal" else bool, f"scope.{key}")
        if key != "scope_literal" and value:
            raise ValueError(f"forbidden scope claim {key}")
    exact_keys(payload["status"], ["evidence_status", "implementation_state", "release_authorized"], "status")
    exact_type(payload["status"]["evidence_status"], str, "status.evidence_status")
    exact_type(payload["status"]["implementation_state"], str, "status.implementation_state")
    exact_type(payload["status"]["release_authorized"], bool, "status.release_authorized")
    if scope["scope_literal"] != SCOPE_LITERAL or payload["status"] != EXPECTED_STATUS:
        raise ValueError("scope/status literal differs")


def normalize(values: Sequence[int], one_based: bool) -> Permutation:
    shift = 1 if one_based else 0
    result = tuple(int(value) - shift for value in values)
    if len(result) != DEGREE or sorted(result) != list(range(DEGREE)):
        raise ValueError("invalid permutation")
    return result


def compose(left: Permutation, right: Permutation) -> Permutation:
    return tuple(left[right[index]] for index in range(DEGREE))


def inverse(permutation: Permutation) -> Permutation:
    result = [0] * DEGREE
    for source, target in enumerate(permutation):
        result[target] = source
    return tuple(result)


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


def image_monomial(permutation: Permutation, monomial: Monomial) -> Monomial:
    return tuple(sorted(permutation[index] for index in monomial))


def orbit_of_monomial(group: Sequence[Permutation], monomial: Monomial) -> tuple[Monomial, ...]:
    return tuple(sorted({image_monomial(element, monomial) for element in group}))


def image_carrier(permutation: Permutation, carrier: Carrier) -> Carrier:
    return tuple(sorted((image_monomial(permutation, monomial), coefficient) for monomial, coefficient in carrier))


def weighted(items: Sequence[tuple[Sequence[Monomial], int]]) -> Carrier:
    totals: dict[Monomial, int] = {}
    for support, coefficient in items:
        for monomial in support:
            totals[monomial] = totals.get(monomial, 0) + coefficient
    return tuple(sorted((monomial, coefficient) for monomial, coefficient in totals.items() if coefficient))


def stabilizer(group: Sequence[Permutation], carrier: Carrier) -> tuple[Permutation, ...]:
    return tuple(element for element in group if image_carrier(element, carrier) == carrier)


def family(group: Sequence[Permutation], carrier: Carrier) -> tuple[Carrier, ...]:
    return tuple(sorted({image_carrier(element, carrier) for element in group}))


def carrier_value(alpha: Sequence[int], carrier: Carrier) -> int:
    total = 0
    for monomial, coefficient in carrier:
        term = coefficient
        for index in monomial:
            term *= alpha[index]
        total += term
    return total % PRIME


def polynomial_from_roots(roots: Sequence[int]) -> list[int]:
    coefficients = [1]
    for root in roots:
        updated = [0] * (len(coefficients) + 1)
        for index, coefficient in enumerate(coefficients):
            updated[index] = (updated[index] - root * coefficient) % PRIME
            updated[index + 1] = (updated[index + 1] + coefficient) % PRIME
        coefficients = updated
    return coefficients


def carrier_fingerprint(w: Sequence[Permutation], alpha: Sequence[int], carrier: Carrier) -> tuple[int, int, dict[str, Any]]:
    exact_stabilizer = stabilizer(w, carrier)
    orbit = family(w, carrier)
    values = [carrier_value(alpha, item) for item in orbit]
    coefficients = polynomial_from_roots(values)
    return len(exact_stabilizer), len(orbit), {
        "coefficient_count": len(coefficients),
        "coefficient_sha256": compact_sha256(coefficients),
        "distinct_value_count": len(set(values)),
        "sorted_values_sha256": compact_sha256(sorted(values)),
        "value_count": len(values),
        "values_sha256": compact_sha256(values),
    }


def parse_manifest(data: bytes) -> dict[str, str]:
    entries: dict[str, str] = {}
    for line in data.decode().splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  ([^\n]+)", line)
        if match is None:
            raise ValueError("malformed manifest")
        digest_value, relative = match.groups()
        if relative in entries:
            raise ValueError("duplicate manifest path")
        entries[relative] = digest_value
    if list(entries) != sorted(entries) or len(entries) != 63:
        raise ValueError("manifest order/count differs")
    return entries


def carrier_from_json(value: list[Any]) -> Carrier:
    return tuple((tuple(term[0]), int(term[1])) for term in value)


def reconstruct_and_validate(
    evidence_document: dict[str, Any],
    schema_document: dict[str, Any],
    *,
    c59_resolvent_module: Path,
    c59_resolvent_evidence: Path,
    c59_full_manifest: Path,
    c59_route: Path,
    c59_route_archive: Path,
) -> dict[str, Any]:
    """Checker-owned reconstruction with explicit inputs and no producer import."""

    validate_schema(schema_document)
    validate_document_shape(evidence_document)
    payload = evidence_document["payload"]
    input_paths = {
        "c59_resolvent_module": c59_resolvent_module,
        "c59_resolvent_evidence": c59_resolvent_evidence,
        "c59_full_manifest": c59_full_manifest,
        "c59_route": c59_route,
        "c59_route_archive": c59_route_archive,
    }
    input_snapshots = {name: stable_file_bytes(path) for name, path in input_paths.items()}
    actual_hashes = {
        name: sha256_bytes(input_snapshots[name][0]) for name in EXPECTED_INPUT_HASHES
    }
    if actual_hashes != EXPECTED_INPUT_HASHES:
        raise ValueError("checker frozen input hash drift")
    route_archive_hash = sha256_bytes(input_snapshots["c59_route_archive"][0])
    if route_archive_hash != actual_hashes["c59_route"] or input_snapshots["c59_route"][0] != input_snapshots["c59_route_archive"][0]:
        raise ValueError("checker Route archive identity differs")
    manifest = parse_manifest(input_snapshots["c59_full_manifest"][0])
    for relative, expected in {
        "code/c59_resolvent.py": actual_hashes["c59_resolvent_module"],
        "results/c59_resolvent_evidence.json": actual_hashes["c59_resolvent_evidence"],
        "route_a_evaluation.yaml": actual_hashes["c59_route"],
        "evaluations/route_a/HCS-C59/20260816T000000Z.yaml": route_archive_hash,
    }.items():
        if manifest.get(relative) != expected:
            raise ValueError(f"manifest binding differs: {relative}")

    authority_expected = {
        "c59_implementation_commit": EXPECTED_C59_IMPLEMENTATION_COMMIT,
        "c59_release_commit": EXPECTED_C59_RELEASE_COMMIT,
        "c59_full_manifest_sha256": actual_hashes["c59_full_manifest"],
        "c59_full_manifest_entry_count": len(manifest),
        "c59_route_sha256": actual_hashes["c59_route"],
        "c59_route_archive_sha256": route_archive_hash,
        "c59_resolvent_module_sha256": actual_hashes["c59_resolvent_module"],
        "c59_resolvent_evidence_sha256": actual_hashes["c59_resolvent_evidence"],
        "c59_resolvent_payload_sha256": EXPECTED_C59_PAYLOAD_HASH,
        "c60_durable_group_literals_sha256": compact_sha256(DURABLE_GROUP_LITERALS),
        "c60_durable_carrier_literals_sha256": compact_sha256(DURABLE_CARRIER_LITERALS),
        "released_c59_rebound": True,
    }
    if payload["authority"] != authority_expected:
        raise ValueError("evidence authority record differs from checker rebound")

    source_document = json.loads(input_snapshots["c59_resolvent_evidence"][0])
    exact_keys(source_document, ["payload", "payload_sha256", "schema_id", "schema_sha256"], "C59 source document")
    if source_document["payload_sha256"] != EXPECTED_C59_PAYLOAD_HASH or source_document["payload_sha256"] != sha256_bytes(canonical_bytes(source_document["payload"])):
        raise ValueError("C59 source payload digest differs")
    source = source_document["payload"]
    finite = source["finite_field"]
    lines = source["line_configuration"]
    if finite["factor_degrees"] != [[1, 27]] or not finite["prime_proven"] or not finite["multiplyback_matches_normalized_eliminant"] or not finite["denominator_envelope"]["all_nonzero"]:
        raise ValueError("C59 split witness differs")
    if len(finite["roots_sorted"]) != 27 or len(set(finite["roots_sorted"])) != 27 or not lines["mapping_is_graph_isomorphism"] or not lines["all_equation_residues_zero"]:
        raise ValueError("C59 labelled split witness differs")
    alpha = [int(value) for value in lines["alpha_by_standard_label"]]

    w_generators = tuple(normalize(row, False) for row in source["group_and_automorphisms"]["w_generators"])
    hplus_generators = tuple(normalize(row, False) for row in source["invariants"]["301"]["h_generators"])
    hminus_generators = tuple(normalize(row, False) for row in source["invariants"]["303"]["h_generators"])
    hzero_generators = tuple(normalize(row, True) for row in H0_GENERATORS_ONE_BASED)
    n_generators = tuple(normalize(row, True) for row in N_GENERATORS_ONE_BASED)
    j_generators = tuple(normalize(row, True) for row in J_GENERATORS_ONE_BASED)
    x = normalize(TRANSPORT_X_ONE_BASED, True)
    w = generated_group(w_generators)
    hplus = generated_group(hplus_generators)
    hzero = generated_group(hzero_generators)
    hminus = generated_group(hminus_generators)
    n_group = generated_group(n_generators)
    j_group = generated_group(j_generators)
    xi = inverse(x)
    hthree_generators = tuple(compose(compose(x, h), xi) for h in hminus_generators)
    hthree = generated_group(hthree_generators)
    orders = [len(hplus), len(hzero), len(hminus), len(hthree), len(n_group), len(j_group)]
    labelled_w_action_faithful = (
        len(w) == len(set(w)) == W_ORDER
        and all(len(element) == DEGREE and sorted(element) == list(range(DEGREE)) for element in w)
    )
    if not labelled_w_action_faithful or orders != EXPECTED_GROUP_ORDERS:
        raise ValueError("checker group orders differ")

    splus = tuple(sorted({pair for seed in [(0, 1), (0, 8)] for pair in orbit_of_monomial(hplus, seed)}))
    sminus = orbit_of_monomial(hminus, (0, 1))
    sthree = tuple(sorted(image_monomial(x, pair) for pair in sminus))
    hthree_support = tuple(element for element in w if tuple(sorted(image_monomial(element, pair) for pair in sthree)) == sthree)
    if set(hthree_support) != set(hthree) or not set(hthree).issubset(set(n_group)) or set(hplus).intersection(hthree) != set(j_group):
        raise ValueError("checker left transport/Stab(xSminus)=H3 subset N/J differs")
    outside = min(set(n_group) - set(hplus))
    m_carrier = weighted([(splus, 1), (tuple(sorted(image_monomial(outside, pair) for pair in splus)), 1)])

    pairs = [(left, right) for left in range(DEGREE) for right in range(left + 1, DEGREE)]
    pair_h0 = sorted({orbit_of_monomial(hzero, pair) for pair in pairs}, key=lambda item: (len(item), item))
    pair_n = sorted({orbit_of_monomial(n_group, pair) for pair in pairs}, key=lambda item: (len(item), item))
    point_h0 = sorted({tuple(sorted({element[index] for element in hzero})) for index in range(DEGREE)})
    point_n = sorted({tuple(sorted({element[index] for element in n_group})) for index in range(DEGREE)})
    if pair_h0 != pair_n or point_h0 != point_n:
        raise ValueError("checker degree-two obstruction differs")
    fzero_support = tuple(tuple(item) for item in F0_CUBIC_SUPPORT)
    if orbit_of_monomial(hzero, fzero_support[0]) != fzero_support:
        raise ValueError("checker source-owned cubic orbit differs")
    fzero_carrier = weighted([(fzero_support, 1)])
    if len(fzero_carrier) != 27 or set(stabilizer(w, fzero_carrier)) != set(hzero):
        raise ValueError("checker source-owned cubic escape differs")
    l_carrier = weighted([(splus, 1), (sthree, 2)])
    expected_carriers = {"M": m_carrier, "F0": fzero_carrier, "L": l_carrier}
    expected_groups = {"M": n_group, "F0": hzero, "L": j_group}

    for name in ["M", "F0", "L"]:
        record = payload["carriers"][name]
        carrier = expected_carriers[name]
        if carrier_from_json(record["carrier"]) != carrier or record["carrier_sha256"] != compact_sha256(record["carrier"]):
            raise ValueError(f"checker carrier bytes differ for {name}")
        stabilizer_order, orbit_size, polynomial = carrier_fingerprint(w, alpha, carrier)
        if stabilizer_order != len(expected_groups[name]) or set(stabilizer(w, carrier)) != set(expected_groups[name]):
            raise ValueError(f"checker exact Z-carrier stabilizer differs for {name}")
        expected_record = {
            "carrier": record["carrier"],
            "carrier_sha256": compact_sha256(record["carrier"]),
            "label": EXPECTED_CARRIER_LABELS[name],
            "modular_polynomial": polynomial,
            "monomial_degree": EXPECTED_MONOMIAL_DEGREES[name],
            "nonzero_monomial_count": len(carrier),
            "orbit_size": orbit_size,
            "stabilizer_equals_expected": True,
            "stabilizer_order": stabilizer_order,
            "weight_histogram": {
                "1": sum(coefficient == 1 for _, coefficient in carrier),
                "2": sum(coefficient == 2 for _, coefficient in carrier),
            },
        }
        if record != expected_record:
            raise ValueError(f"checker full carrier record differs for {name}")
        if orbit_size != EXPECTED_DEGREES[name]:
            raise ValueError(f"checker orbit/modular polynomial differs for {name}")
        if polynomial["distinct_value_count"] != EXPECTED_DEGREES[name] or polynomial["coefficient_sha256"] != EXPECTED_COEFFICIENT_HASHES[name]:
            raise ValueError(f"checker distinct split values/coefficient digest differs for {name}")

    group_hashes = {
        "orders_Hplus_H0_Hminus_H3_N_J": orders,
        "Hplus_generators_sha256": compact_sha256([[item + 1 for item in row] for row in hplus_generators]),
        "H0_generators_sha256": compact_sha256([[item + 1 for item in row] for row in hzero_generators]),
        "Hminus_generators_sha256": compact_sha256([[item + 1 for item in row] for row in hminus_generators]),
        "H3_generators_sha256": compact_sha256([[item + 1 for item in row] for row in hthree_generators]),
        "N_generators_sha256": compact_sha256([[item + 1 for item in row] for row in n_generators]),
        "J_generators_sha256": compact_sha256([[item + 1 for item in row] for row in j_generators]),
    }
    if payload["groups"] != group_hashes:
        raise ValueError("checker group generator digests differ")
    obstruction_expected = {
        "H0_and_N_point_partitions_equal": True,
        "H0_and_N_unordered_pair_partitions_equal": True,
        "H0_point_orbit_sizes": [len(item) for item in point_h0],
        "H0_pair_orbit_sizes": [len(item) for item in pair_h0],
        "H0_point_partition_sha256": compact_sha256(point_h0),
        "H0_pair_partition_sha256": compact_sha256(pair_h0),
        "selected_cubic_orbit_size": len(fzero_carrier),
        "selected_cubic_support_sha256": payload["carriers"]["F0"]["carrier_sha256"],
        "formal_polynomial_scope": "commutative Q-coefficient formal polynomials in 27 independent labelled variables",
    }
    if payload["invariant_degree_obstruction"] != obstruction_expected:
        raise ValueError("checker invariant obstruction record differs")

    bridge_expected = {
        "K_completely_split_witness": labelled_w_action_faithful,
        "c59_all_27_line_equations_zero": lines["all_equation_residues_zero"],
        "c59_factor_degrees": finite["factor_degrees"],
        "c59_label_map_is_graph_isomorphism": lines["mapping_is_graph_isomorphism"],
        "c59_split_roots_distinct": len(set(finite["roots_sorted"])) == DEGREE,
        "characteristic_zero_orbit_values_distinct": True,
        "fixed_field_identities": EXPECTED_FIXED_FIELD_IDENTITIES,
        "fixed_field_reason": FIXED_FIELD_REASON,
        "labelled_W_action_faithful": labelled_w_action_faithful,
        "modular_distinct_value_counts": {
            name: payload["carriers"][name]["modular_polynomial"]["distinct_value_count"]
            for name in ["M", "F0", "L"]
        },
        "prime_unramified": finite["denominator_envelope"]["all_nonzero"] and finite["multiplyback_matches_normalized_eliminant"],
        "support_stabilizers_exact_on_Z_labelled_carrier": {
            name: payload["carriers"][name]["stabilizer_equals_expected"]
            for name in ["M", "F0", "L"]
        },
    }
    if payload["fixed_field_bridge"] != bridge_expected:
        raise ValueError("checker characteristic-zero/fixed-field bridge differs")

    checks = {
        "authority_rebound": True,
        "c59_labelled_complete_split_rebound": True,
        "labelled_W_action_faithful": True,
        "left_transport_exact": True,
        "group_orders_exact": True,
        "formal_stabilizers_N_H0_J_exact": True,
        "orbits_160_320_640_exact": True,
        "split_values_pairwise_distinct": True,
        "coefficient_hashes_exact": True,
        "characteristic_zero_fixed_field_bridge": True,
        "degree_two_obstruction_cross_checked": True,
        "scope_firewall_closed": True,
    }
    result = {
        "checks": checks,
        "evidence_payload_sha256": evidence_document["payload_sha256"],
        "scope_literal": SCOPE_LITERAL,
        "status": EXPECTED_STATUS,
    }
    if any(stable_file_bytes(path) != input_snapshots[name] for name, path in input_paths.items()):
        raise ValueError("released C59 authority changed during independent reconstruction")
    return result


STAGE_PATTERN = re.compile(r"^\.c60-stage-[A-Za-z0-9]{8}$")
EVIDENCE_BASENAME = "c60_resolvent_evidence.json"
SCHEMA_BASENAME = "c60_resolvent_schema.json"
REPORT_BASENAME = "c60_resolvent_check_report.json"


def staged_path(value: str, expected_basename: str) -> tuple[Path, Path, tuple[int, int]]:
    path = Path(value).absolute()
    project = Path(__file__).resolve().parent.parent
    results = (project / "results").resolve(strict=True)
    stage = path.parent
    if path.name != expected_basename or STAGE_PATTERN.fullmatch(stage.name) is None or stage.parent != results or not stage.is_dir() or stage.is_symlink() or stage.resolve(strict=True) != stage:
        raise ValueError("path must be fixed basename under PROJECT/results/.c60-stage-XXXXXXXX")
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
        raise ValueError("canonical C60 results stage changed during checker replay")


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
    parser.add_argument("--evidence", required=True)
    parser.add_argument("--schema", required=True)
    destination = parser.add_mutually_exclusive_group(required=True)
    destination.add_argument("--report")
    destination.add_argument("--check-existing-report")
    parser.add_argument("--c59-resolvent-module", type=Path, required=True)
    parser.add_argument("--c59-resolvent-evidence", type=Path, required=True)
    parser.add_argument("--c59-full-manifest", type=Path, required=True)
    parser.add_argument("--c59-route", type=Path, required=True)
    parser.add_argument("--c59-route-archive", type=Path, required=True)
    arguments = parser.parse_args()
    selected_report = arguments.report if arguments.report is not None else arguments.check_existing_report
    writing = arguments.report is not None
    evidence_path, stage, identity = staged_path(arguments.evidence, EVIDENCE_BASENAME)
    schema_path, schema_stage, schema_identity = staged_path(arguments.schema, SCHEMA_BASENAME)
    report_path, report_stage, report_identity = staged_path(selected_report, REPORT_BASENAME)
    if len({stage, schema_stage, report_stage}) != 1 or len({identity, schema_identity, report_identity}) != 1:
        raise ValueError("checker files must share one canonical stage")
    if len({evidence_path, schema_path, report_path}) != 3:
        raise ValueError("checker evidence, schema, and report paths must not alias")
    evidence_before = stable_file_bytes(evidence_path)
    schema_before = stable_file_bytes(schema_path)
    report_before = stable_file_bytes(report_path) if not writing else None
    if writing and os.path.lexists(report_path):
        stable_file_bytes(report_path)
    c59_inputs = {
        "c59_resolvent_module": arguments.c59_resolvent_module.resolve(strict=True),
        "c59_resolvent_evidence": arguments.c59_resolvent_evidence.resolve(strict=True),
        "c59_full_manifest": arguments.c59_full_manifest.resolve(strict=True),
        "c59_route": arguments.c59_route.resolve(strict=True),
        "c59_route_archive": arguments.c59_route_archive.resolve(strict=True),
    }
    c59_before = {name: stable_file_bytes(path) for name, path in c59_inputs.items()}
    checker_source = stable_file_bytes(Path(__file__).resolve(strict=True))
    started = time.perf_counter()
    assert_stage_identity(stage, identity)
    evidence = json.loads(evidence_before[0])
    schema = json.loads(schema_before[0])
    result = reconstruct_and_validate(
        evidence, schema,
        **c59_inputs,
    )
    report = {
        "checker_source_sha256": sha256_bytes(checker_source[0]),
        "evidence_sha256": sha256_bytes(evidence_before[0]),
        "payload": result,
        "payload_sha256": sha256_bytes(canonical_bytes(result)),
        "schema_file_sha256": sha256_bytes(schema_before[0]),
        "schema_id": "hcs-c60-resolvent-check-report-v1",
    }
    report_bytes = canonical_bytes(report)
    assert_stage_identity(stage, identity)
    if stable_file_bytes(evidence_path) != evidence_before or stable_file_bytes(schema_path) != schema_before:
        raise ValueError("C60 evidence/schema changed during checker replay")
    if any(stable_file_bytes(path) != c59_before[name] for name, path in c59_inputs.items()):
        raise ValueError("released C59 authority changed during checker CLI replay")
    if stable_file_bytes(Path(__file__).resolve(strict=True)) != checker_source:
        raise ValueError("checker source changed during replay")
    if writing:
        atomic_write(report_path, report_bytes)
        assert_stage_identity(stage, identity)
        if stable_file_bytes(report_path)[0] != report_bytes:
            raise ValueError("checker report write did not rebind to intended bytes")
        mode = "write"
    else:
        assert report_before is not None
        report_after = stable_file_bytes(report_path)
        if report_after != report_before or report_after[0] != report_bytes:
            raise ValueError("existing checker report changed or is not byte-identical to fresh replay")
        mode = "replay"
    assert_stage_identity(stage, identity)
    print(json.dumps({
        "elapsed_seconds": round(time.perf_counter() - started, 6),
        "evidence_sha256": report["evidence_sha256"],
        "mode": mode,
        "report_sha256": sha256_bytes(report_bytes),
        "status": "PASS",
        "target": REPORT_BASENAME,
    }, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
