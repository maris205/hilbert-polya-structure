#!/usr/bin/env python3
"""Build HCS-C60 primitive-resolvent evidence.

This source is deliberately C60-owned.  It rebinds the released C59
resolvent source/evidence and C60-owned durable literals, reconstructs
the M, F0, and L carriers, and emits a strict source-owned evidence envelope.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import re
import stat
import tempfile
import time
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

# C60 source-owned durable definitions.  These literals are duplicated in the
# independent checker; neither lane imports or reads a design-pilot artifact.
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
    "invariant_degree_obstruction", "replay_contract",
    "scope", "status", "transport",
]
AUTHORITY_KEYS = [
    "c60_durable_carrier_literals_sha256", "c60_durable_group_literals_sha256",
    "c59_full_manifest_entry_count", "c59_full_manifest_sha256",
    "c59_implementation_commit", "c59_release_commit",
    "c59_resolvent_evidence_sha256", "c59_resolvent_module_sha256",
    "c59_resolvent_payload_sha256", "c59_route_archive_sha256",
    "c59_route_sha256", "released_c59_rebound",
]
CONSTANT_KEYS = [
    "degree", "expected_coefficient_hashes", "expected_orbit_degrees",
    "prime", "scope_literal", "w_order",
]
TRANSPORT_KEYS = [
    "H301_intersection_H3_order", "H3_contained_in_N",
    "H3_equals_transported_support_stabilizer", "H3_order", "convention",
    "label_permutation_one_based", "transported_support_stabilizer_order",
]
GROUP_KEYS = [
    "H0_generators_sha256", "H3_generators_sha256",
    "Hminus_generators_sha256", "Hplus_generators_sha256",
    "J_generators_sha256", "N_generators_sha256",
    "orders_Hplus_H0_Hminus_H3_N_J",
]
CARRIER_KEYS = [
    "carrier", "carrier_sha256", "label", "modular_polynomial",
    "monomial_degree", "nonzero_monomial_count", "orbit_size",
    "stabilizer_equals_expected", "stabilizer_order", "weight_histogram",
]
POLYNOMIAL_KEYS = [
    "coefficient_count", "coefficient_sha256", "distinct_value_count",
    "sorted_values_sha256", "value_count", "values_sha256",
]
OBSTRUCTION_KEYS = [
    "H0_and_N_point_partitions_equal", "H0_and_N_unordered_pair_partitions_equal",
    "H0_pair_orbit_sizes", "H0_pair_partition_sha256", "H0_point_orbit_sizes",
    "H0_point_partition_sha256", "formal_polynomial_scope",
    "selected_cubic_orbit_size", "selected_cubic_support_sha256",
]
BRIDGE_KEYS = [
    "K_completely_split_witness", "c59_all_27_line_equations_zero",
    "c59_factor_degrees", "c59_label_map_is_graph_isomorphism",
    "c59_split_roots_distinct", "characteristic_zero_orbit_values_distinct",
    "fixed_field_identities", "fixed_field_reason",
    "labelled_W_action_faithful", "modular_distinct_value_counts", "prime_unramified",
    "support_stabilizers_exact_on_Z_labelled_carrier",
]
REPLAY_KEYS = [
    "builder_basename", "canonical_stage_pattern", "checker_basename",
    "durable_literals_source", "evidence_basename", "group_evidence_policy",
    "schema_basename",
]
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


def require_exact_keys(record: Any, expected: Iterable[str], label: str) -> None:
    if type(record) is not dict:
        raise ValueError(f"{label} must be a built-in dict")
    wanted = set(expected)
    actual = set(record)
    if actual != wanted:
        raise ValueError(f"{label} keys differ: missing={sorted(wanted-actual)} extra={sorted(actual-wanted)}")


def require_type(value: Any, expected: type, label: str) -> None:
    if type(value) is not expected:
        raise ValueError(f"{label} must have exact type {expected.__name__}")


def require_hash(value: Any, label: str) -> None:
    require_type(value, str, label)
    if re.fullmatch(r"[0-9a-f]{64}", value) is None:
        raise ValueError(f"{label} is not a lowercase SHA-256 digest")


def validate_carrier_record(name: str, record: Any) -> None:
    require_exact_keys(record, CARRIER_KEYS, f"carrier {name}")
    for key in ["label", "carrier_sha256"]:
        require_type(record[key], str, f"carrier {name}.{key}")
    require_hash(record["carrier_sha256"], f"carrier {name}.carrier_sha256")
    for key in ["monomial_degree", "nonzero_monomial_count", "orbit_size", "stabilizer_order"]:
        require_type(record[key], int, f"carrier {name}.{key}")
    require_type(record["stabilizer_equals_expected"], bool, f"carrier {name}.stabilizer_equals_expected")
    require_exact_keys(record["weight_histogram"], ["1", "2"], f"carrier {name}.weight_histogram")
    for key, count in record["weight_histogram"].items():
        require_type(count, int, f"carrier {name}.weight_histogram.{key}")
    require_type(record["carrier"], list, f"carrier {name}.carrier")
    for position, term in enumerate(record["carrier"]):
        require_type(term, list, f"carrier {name}.carrier[{position}]")
        if len(term) != 2:
            raise ValueError(f"carrier {name} term must have two entries")
        monomial, coefficient = term
        require_type(monomial, list, f"carrier {name} monomial")
        require_type(coefficient, int, f"carrier {name} coefficient")
        if len(monomial) != record["monomial_degree"] or coefficient not in {1, 2}:
            raise ValueError(f"carrier {name} malformed term")
        if any(type(index) is not int or not 0 <= index < DEGREE for index in monomial):
            raise ValueError(f"carrier {name} monomial index invalid")
        if monomial != sorted(set(monomial)):
            raise ValueError(f"carrier {name} monomial must be squarefree and sorted")
    polynomial = record["modular_polynomial"]
    require_exact_keys(polynomial, POLYNOMIAL_KEYS, f"carrier {name}.modular_polynomial")
    for key in ["coefficient_count", "distinct_value_count", "value_count"]:
        require_type(polynomial[key], int, f"carrier {name}.modular_polynomial.{key}")
    for key in ["coefficient_sha256", "sorted_values_sha256", "values_sha256"]:
        require_hash(polynomial[key], f"carrier {name}.modular_polynomial.{key}")


def validate_evidence_document(document: dict[str, Any]) -> None:
    """Strict source-owned validation compatible with the C59 envelope style."""

    require_exact_keys(document, DOCUMENT_KEYS, "evidence document")
    if document["schema_id"] != SCHEMA_ID:
        raise ValueError("schema id differs")
    if document["schema_sha256"] != compact_sha256(SCHEMA_DESCRIPTOR):
        raise ValueError("schema descriptor digest differs")
    require_hash(document["payload_sha256"], "payload_sha256")
    payload = document["payload"]
    require_exact_keys(payload, PAYLOAD_KEYS, "payload")
    if document["payload_sha256"] != sha256_bytes(canonical_bytes(payload)):
        raise ValueError("payload digest differs")
    require_exact_keys(payload["authority"], AUTHORITY_KEYS, "authority")
    require_exact_keys(payload["constants"], CONSTANT_KEYS, "constants")
    require_exact_keys(payload["transport"], TRANSPORT_KEYS, "transport")
    require_exact_keys(payload["groups"], GROUP_KEYS, "groups")
    require_exact_keys(payload["carriers"], ["F0", "L", "M"], "carriers")
    require_exact_keys(payload["fixed_field_bridge"], BRIDGE_KEYS, "fixed-field bridge")
    require_exact_keys(payload["invariant_degree_obstruction"], OBSTRUCTION_KEYS, "obstruction")
    require_exact_keys(payload["replay_contract"], REPLAY_KEYS, "replay contract")
    require_exact_keys(payload["scope"], SCOPE_KEYS, "scope")

    authority = payload["authority"]
    for key in AUTHORITY_KEYS:
        if key.endswith("sha256"):
            require_hash(authority[key], f"authority.{key}")
    for key in ["c59_implementation_commit", "c59_release_commit"]:
        require_type(authority[key], str, f"authority.{key}")
        if re.fullmatch(r"[0-9a-f]{40}", authority[key]) is None:
            raise ValueError(f"authority.{key} is not a commit digest")
    require_type(authority["c59_full_manifest_entry_count"], int, "manifest entry count")
    require_type(authority["released_c59_rebound"], bool, "released rebind flag")
    if not authority["released_c59_rebound"]:
        raise ValueError("authority boundary differs")
    if authority["c60_durable_group_literals_sha256"] != compact_sha256(DURABLE_GROUP_LITERALS):
        raise ValueError("durable group literal digest differs")
    if authority["c60_durable_carrier_literals_sha256"] != compact_sha256(DURABLE_CARRIER_LITERALS):
        raise ValueError("durable carrier literal digest differs")

    constants = payload["constants"]
    if constants != {
        "degree": DEGREE,
        "expected_coefficient_hashes": EXPECTED_COEFFICIENT_HASHES,
        "expected_orbit_degrees": EXPECTED_DEGREES,
        "prime": PRIME,
        "scope_literal": SCOPE_LITERAL,
        "w_order": W_ORDER,
    }:
        raise ValueError("constant contract differs")

    transport = payload["transport"]
    for key in ["H3_contained_in_N", "H3_equals_transported_support_stabilizer"]:
        require_type(transport[key], bool, f"transport.{key}")
        if not transport[key]:
            raise ValueError(f"transport.{key} must be true")
    for key in ["H301_intersection_H3_order", "H3_order", "transported_support_stabilizer_order"]:
        require_type(transport[key], int, f"transport.{key}")
    require_type(transport["convention"], str, "transport.convention")
    require_type(transport["label_permutation_one_based"], list, "transport permutation")
    for position, label in enumerate(transport["label_permutation_one_based"]):
        require_type(label, int, f"transport permutation[{position}]")
    if sorted(transport["label_permutation_one_based"]) != list(range(1, DEGREE + 1)):
        raise ValueError("transport permutation differs from S_27")
    if transport != {
        "H301_intersection_H3_order": 81,
        "H3_contained_in_N": True,
        "H3_equals_transported_support_stabilizer": True,
        "H3_order": 162,
        "convention": TRANSPORT_CONVENTION,
        "label_permutation_one_based": TRANSPORT_X_ONE_BASED,
        "transported_support_stabilizer_order": 162,
    }:
        raise ValueError("transport record differs from C60 durable literals")

    groups = payload["groups"]
    for key in GROUP_KEYS:
        if key.endswith("sha256"):
            require_hash(groups[key], f"groups.{key}")
    require_type(groups["orders_Hplus_H0_Hminus_H3_N_J"], list, "group orders")
    for position, order in enumerate(groups["orders_Hplus_H0_Hminus_H3_N_J"]):
        require_type(order, int, f"group orders[{position}]")
    if groups["orders_Hplus_H0_Hminus_H3_N_J"] != EXPECTED_GROUP_ORDERS:
        raise ValueError("group orders differ")

    for name in ["M", "F0", "L"]:
        validate_carrier_record(name, payload["carriers"][name])
        record = payload["carriers"][name]
        expected = EXPECTED_DEGREES[name]
        if not record["stabilizer_equals_expected"] or record["orbit_size"] != expected:
            raise ValueError(f"carrier {name} stabilizer/orbit contract differs")
        polynomial = record["modular_polynomial"]
        if polynomial["distinct_value_count"] != expected or polynomial["value_count"] != expected:
            raise ValueError(f"carrier {name} modular value count differs")
        if polynomial["coefficient_count"] != expected + 1:
            raise ValueError(f"carrier {name} coefficient count differs")
        if polynomial["coefficient_sha256"] != EXPECTED_COEFFICIENT_HASHES[name]:
            raise ValueError(f"carrier {name} coefficient digest differs")
        if record["carrier_sha256"] != compact_sha256(record["carrier"]):
            raise ValueError(f"carrier {name} digest differs")
        expected_histogram = {"1": 0, "2": 0}
        for _, coefficient in record["carrier"]:
            expected_histogram[str(coefficient)] += 1
        if (
            record["label"] != EXPECTED_CARRIER_LABELS[name]
            or record["monomial_degree"] != EXPECTED_MONOMIAL_DEGREES[name]
            or record["nonzero_monomial_count"] != len(record["carrier"])
            or record["weight_histogram"] != expected_histogram
            or record["stabilizer_order"] != EXPECTED_STABILIZER_ORDERS[name]
        ):
            raise ValueError(f"carrier {name} metadata differs")

    bridge = payload["fixed_field_bridge"]
    for key in [
        "K_completely_split_witness", "c59_all_27_line_equations_zero",
        "c59_label_map_is_graph_isomorphism", "c59_split_roots_distinct",
        "characteristic_zero_orbit_values_distinct", "labelled_W_action_faithful",
        "prime_unramified",
    ]:
        require_type(bridge[key], bool, f"fixed_field_bridge.{key}")
        if not bridge[key]:
            raise ValueError(f"fixed_field_bridge.{key} must be true")
    require_type(bridge["c59_factor_degrees"], list, "fixed-field factor degrees")
    for position, row in enumerate(bridge["c59_factor_degrees"]):
        require_type(row, list, f"fixed-field factor degrees[{position}]")
        for inner, scalar in enumerate(row):
            require_type(scalar, int, f"fixed-field factor degrees[{position}][{inner}]")
    if bridge["c59_factor_degrees"] != [[1, 27]]:
        raise ValueError("fixed-field split factor degrees differ")
    require_type(bridge["modular_distinct_value_counts"], dict, "fixed-field modular counts")
    for name, count in bridge["modular_distinct_value_counts"].items():
        require_type(count, int, f"fixed-field modular count {name}")
    if bridge["modular_distinct_value_counts"] != EXPECTED_DEGREES:
        raise ValueError("fixed-field modular distinct counts differ")
    require_type(bridge["support_stabilizers_exact_on_Z_labelled_carrier"], dict, "fixed-field stabilizers")
    for name, flag in bridge["support_stabilizers_exact_on_Z_labelled_carrier"].items():
        require_type(flag, bool, f"fixed-field stabilizer {name}")
    if bridge["support_stabilizers_exact_on_Z_labelled_carrier"] != {"F0": True, "L": True, "M": True}:
        raise ValueError("fixed-field formal stabilizers differ")
    require_type(bridge["fixed_field_identities"], dict, "fixed-field identities")
    for name, identity in bridge["fixed_field_identities"].items():
        require_type(identity, str, f"fixed-field identity {name}")
    if bridge["fixed_field_identities"] != EXPECTED_FIXED_FIELD_IDENTITIES:
        raise ValueError("fixed-field identities differ")
    require_type(bridge["fixed_field_reason"], str, "fixed-field reason")
    if bridge["fixed_field_reason"] != FIXED_FIELD_REASON:
        raise ValueError("fixed-field reason differs")

    obstruction = payload["invariant_degree_obstruction"]
    for key in ["H0_and_N_point_partitions_equal", "H0_and_N_unordered_pair_partitions_equal"]:
        require_type(obstruction[key], bool, f"obstruction.{key}")
        if not obstruction[key]:
            raise ValueError(f"obstruction.{key} must be true")
    for key in ["H0_pair_partition_sha256", "H0_point_partition_sha256", "selected_cubic_support_sha256"]:
        require_hash(obstruction[key], f"obstruction.{key}")
    if obstruction["H0_point_orbit_sizes"] != [27] or obstruction["H0_pair_orbit_sizes"] != [27, 27, 54, 81, 162]:
        raise ValueError("obstruction orbit sizes differ")
    if obstruction["selected_cubic_orbit_size"] != 27:
        raise ValueError("selected cubic orbit size differs")
    require_type(obstruction["formal_polynomial_scope"], str, "formal polynomial scope")

    replay = payload["replay_contract"]
    for key in REPLAY_KEYS:
        require_type(replay[key], str, f"replay.{key}")
    if replay != EXPECTED_REPLAY_CONTRACT:
        raise ValueError("replay contract differs")

    scope = payload["scope"]
    for key in SCOPE_KEYS:
        if key == "scope_literal":
            require_type(scope[key], str, f"scope.{key}")
        else:
            require_type(scope[key], bool, f"scope.{key}")
            if scope[key]:
                raise ValueError(f"forbidden scope flag true: {key}")
    require_exact_keys(payload["status"], ["evidence_status", "implementation_state", "release_authorized"], "status")
    require_type(payload["status"]["evidence_status"], str, "status.evidence_status")
    require_type(payload["status"]["implementation_state"], str, "status.implementation_state")
    require_type(payload["status"]["release_authorized"], bool, "status.release_authorized")
    if scope["scope_literal"] != SCOPE_LITERAL or payload["status"] != EXPECTED_STATUS:
        raise ValueError("scope/status literal differs")


def normalize_permutation(c59: Any, values: Sequence[int], *, one_based: bool) -> tuple[int, ...]:
    return c59.normalize_permutation(list(values), one_based=one_based)


def support_from_seeds(c59: Any, group: Sequence[tuple[int, ...]], seeds: Sequence[tuple[int, int]]) -> tuple[tuple[int, int], ...]:
    return tuple(sorted({pair for seed in seeds for pair in c59.orbit_of_pair(group, seed)}))


def weighted(items: Sequence[tuple[Sequence[tuple[int, ...]], int]]) -> tuple[tuple[tuple[int, ...], int], ...]:
    totals: dict[tuple[int, ...], int] = {}
    for support, coefficient in items:
        for monomial in support:
            totals[tuple(monomial)] = totals.get(tuple(monomial), 0) + coefficient
    return tuple(sorted((monomial, coefficient) for monomial, coefficient in totals.items() if coefficient))


def image_monomial(permutation: tuple[int, ...], monomial: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sorted(permutation[index] for index in monomial))


def inverse(permutation: tuple[int, ...]) -> tuple[int, ...]:
    result = [0] * len(permutation)
    for source, target in enumerate(permutation):
        result[target] = source
    return tuple(result)


def image_weight(permutation: tuple[int, ...], carrier: tuple[tuple[tuple[int, ...], int], ...]) -> tuple[tuple[tuple[int, ...], int], ...]:
    return tuple(sorted((image_monomial(permutation, monomial), coefficient) for monomial, coefficient in carrier))


def stabilizer(w_elements: Sequence[tuple[int, ...]], carrier: tuple[tuple[tuple[int, ...], int], ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(element for element in w_elements if image_weight(element, carrier) == carrier)


def family(w_elements: Sequence[tuple[int, ...]], carrier: tuple[tuple[tuple[int, ...], int], ...]) -> tuple[tuple[tuple[tuple[int, ...], int], ...], ...]:
    return tuple(sorted({image_weight(element, carrier) for element in w_elements}))


def value(alpha: Sequence[int], carrier: tuple[tuple[tuple[int, ...], int], ...]) -> int:
    total = 0
    for monomial, coefficient in carrier:
        product = coefficient
        for index in monomial:
            product *= alpha[index]
        total += product
    return total % PRIME


def fingerprint(c59: Any, values: Sequence[int]) -> dict[str, Any]:
    coefficients = c59.polynomial_from_roots(values, PRIME)
    return {
        "coefficient_count": len(coefficients),
        "coefficient_sha256": compact_sha256(coefficients),
        "distinct_value_count": len(set(values)),
        "sorted_values_sha256": compact_sha256(sorted(values)),
        "value_count": len(values),
        "values_sha256": compact_sha256(values),
    }


def carrier_record(c59: Any, label: str, expected_group: Sequence[tuple[int, ...]], w_elements: Sequence[tuple[int, ...]], alpha: Sequence[int], carrier: tuple[tuple[tuple[int, ...], int], ...]) -> dict[str, Any]:
    exact_stabilizer = stabilizer(w_elements, carrier)
    conjugates = family(w_elements, carrier)
    values = [value(alpha, item) for item in conjugates]
    weight_counts = {"1": 0, "2": 0}
    for _, coefficient in carrier:
        weight_counts[str(coefficient)] += 1
    carrier_list = [[list(monomial), coefficient] for monomial, coefficient in carrier]
    return {
        "label": label,
        "carrier": carrier_list,
        "carrier_sha256": compact_sha256(carrier_list),
        "monomial_degree": len(carrier[0][0]),
        "nonzero_monomial_count": len(carrier),
        "weight_histogram": weight_counts,
        "stabilizer_order": len(exact_stabilizer),
        "stabilizer_equals_expected": set(exact_stabilizer) == set(expected_group),
        "orbit_size": len(conjugates),
        "modular_polynomial": fingerprint(c59, values),
    }


def parse_manifest(data: bytes) -> dict[str, str]:
    entries: dict[str, str] = {}
    for line in data.decode().splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  ([^\n]+)", line)
        if match is None:
            raise ValueError("malformed C59 full manifest line")
        digest, relative = match.groups()
        if relative in entries:
            raise ValueError("duplicate C59 full manifest path")
        entries[relative] = digest
    if list(entries) != sorted(entries) or len(entries) != 63:
        raise ValueError("C59 full manifest order/count differs")
    return entries


def import_c59(path: Path) -> Any:
    spec = importlib.util.spec_from_file_location("released_c59_resolvent_for_c60", path)
    if spec is None or spec.loader is None:
        raise ValueError("cannot load released C59 resolvent source")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build_document(
    c59_resolvent_module: Path,
    c59_resolvent_evidence: Path,
    c59_full_manifest: Path,
    c59_route: Path,
    c59_route_archive: Path,
) -> dict[str, Any]:
    """Rebuild the complete C60 evidence from explicit released inputs."""

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
        raise ValueError(f"frozen input hash drift: {actual_hashes}")
    route_archive_hash = sha256_bytes(input_snapshots["c59_route_archive"][0])
    if route_archive_hash != EXPECTED_INPUT_HASHES["c59_route"] or input_snapshots["c59_route"][0] != input_snapshots["c59_route_archive"][0]:
        raise ValueError("C59 live/archive Route identity differs")

    manifest = parse_manifest(input_snapshots["c59_full_manifest"][0])
    required_manifest = {
        "code/c59_resolvent.py": actual_hashes["c59_resolvent_module"],
        "results/c59_resolvent_evidence.json": actual_hashes["c59_resolvent_evidence"],
        "route_a_evaluation.yaml": actual_hashes["c59_route"],
        "evaluations/route_a/HCS-C59/20260816T000000Z.yaml": route_archive_hash,
    }
    for relative, digest in required_manifest.items():
        if manifest.get(relative) != digest:
            raise ValueError(f"C59 full manifest does not bind {relative}")

    c59 = import_c59(c59_resolvent_module)
    c59_document = json.loads(input_snapshots["c59_resolvent_evidence"][0])
    c59.validate_evidence_document(c59_document)
    if c59_document["payload_sha256"] != EXPECTED_C59_PAYLOAD_HASH:
        raise ValueError("released C59 resolvent payload drift")
    source_payload = c59_document["payload"]
    finite_field = source_payload["finite_field"]
    line_configuration = source_payload["line_configuration"]
    if (
        finite_field["factor_degrees"] != [[1, 27]]
        or not finite_field["prime_proven"]
        or not finite_field["multiplyback_matches_normalized_eliminant"]
        or not finite_field["denominator_envelope"]["all_nonzero"]
        or len(finite_field["roots_sorted"]) != 27
        or len(set(finite_field["roots_sorted"])) != 27
        or not line_configuration["mapping_is_graph_isomorphism"]
        or not line_configuration["all_equation_residues_zero"]
        or len(line_configuration["alpha_by_standard_label"]) != 27
    ):
        raise ValueError("released C59 labelled split witness drift")

    alpha = [int(item) for item in source_payload["line_configuration"]["alpha_by_standard_label"]]
    w_generators = tuple(normalize_permutation(c59, row, one_based=False) for row in source_payload["group_and_automorphisms"]["w_generators"])
    w_elements = c59.generated_group(w_generators)
    labelled_w_action_faithful = (
        len(w_elements) == len(set(w_elements)) == W_ORDER
        and all(len(element) == DEGREE and sorted(element) == list(range(DEGREE)) for element in w_elements)
    )
    if not labelled_w_action_faithful:
        raise ValueError("released W(E6) order drift")

    hplus_generators = tuple(normalize_permutation(c59, row, one_based=True) for row in c59.DURABLE_FIELD_SUBGROUPS["301"]["generators"])
    hminus_generators = tuple(normalize_permutation(c59, row, one_based=True) for row in c59.DURABLE_FIELD_SUBGROUPS["303"]["generators"])
    hzero_generators = tuple(normalize_permutation(c59, row, one_based=True) for row in H0_GENERATORS_ONE_BASED)
    n_generators = tuple(normalize_permutation(c59, row, one_based=True) for row in N_GENERATORS_ONE_BASED)
    j_generators = tuple(normalize_permutation(c59, row, one_based=True) for row in J_GENERATORS_ONE_BASED)
    x = normalize_permutation(c59, TRANSPORT_X_ONE_BASED, one_based=True)

    hplus = c59.generated_group(hplus_generators)
    hzero = c59.generated_group(hzero_generators)
    hminus = c59.generated_group(hminus_generators)
    n_group = c59.generated_group(n_generators)
    j_group = c59.generated_group(j_generators)
    x_inverse = inverse(x)
    hthree = tuple(sorted(c59.compose(c59.compose(x, h), x_inverse) for h in hminus))
    orders = [len(hplus), len(hzero), len(hminus), len(hthree), len(n_group), len(j_group)]
    if orders != EXPECTED_GROUP_ORDERS:
        raise ValueError("C60 subgroup order drift")

    splus = support_from_seeds(c59, hplus, [(0, 1), (0, 8)])
    sminus = support_from_seeds(c59, hminus, [(0, 1)])
    sthree = c59.image_support(x, sminus)
    hthree_from_support = tuple(element for element in w_elements if c59.image_support(element, sthree) == sthree)
    if set(hthree_from_support) != set(hthree) or not set(hthree).issubset(set(n_group)):
        raise ValueError("left label-map transport/Stab(xSminus)=H3 subset N failed")
    if set(hplus).intersection(hthree) != set(j_group):
        raise ValueError("Hplus intersection H3 differs from J")

    outside = min(set(n_group) - set(hplus))
    m_carrier = weighted([(splus, 1), (c59.image_support(outside, splus), 1)])

    all_pairs = [(left, right) for left in range(DEGREE) for right in range(left + 1, DEGREE)]
    pair_orbits_hzero = sorted({c59.orbit_of_pair(hzero, pair) for pair in all_pairs}, key=lambda item: (len(item), item))
    pair_orbits_n = sorted({c59.orbit_of_pair(n_group, pair) for pair in all_pairs}, key=lambda item: (len(item), item))
    point_orbits_hzero = sorted({tuple(sorted({element[index] for element in hzero})) for index in range(DEGREE)})
    point_orbits_n = sorted({tuple(sorted({element[index] for element in n_group})) for index in range(DEGREE)})
    if point_orbits_hzero != point_orbits_n or pair_orbits_hzero != pair_orbits_n:
        raise ValueError("formal degree-two orbit-partition obstruction drift")

    fzero_support = tuple(tuple(item) for item in F0_CUBIC_SUPPORT)
    orbit_of_selected = tuple(sorted({image_monomial(element, fzero_support[0]) for element in hzero}))
    if orbit_of_selected != fzero_support:
        raise ValueError("source-owned F0 cubic support is not the selected H0 orbit")
    fzero_carrier = weighted([(fzero_support, 1)])
    if len(fzero_carrier) != 27 or set(stabilizer(w_elements, fzero_carrier)) != set(hzero):
        raise ValueError("source-owned 27-term H0 cubic carrier drift")
    l_carrier = weighted([(splus, 1), (sthree, 2)])

    carriers = {
        "M": carrier_record(c59, "M=K^N trace carrier", n_group, w_elements, alpha, m_carrier),
        "F0": carrier_record(c59, "F0=K^H0 cubic carrier", hzero, w_elements, alpha, fzero_carrier),
        "L": carrier_record(c59, "L=K^J colored carrier", j_group, w_elements, alpha, l_carrier),
    }

    payload = {
        "authority": {
            "c59_implementation_commit": EXPECTED_C59_IMPLEMENTATION_COMMIT,
            "c59_release_commit": EXPECTED_C59_RELEASE_COMMIT,
            "c59_full_manifest_sha256": actual_hashes["c59_full_manifest"],
            "c59_full_manifest_entry_count": len(manifest),
            "c59_route_sha256": actual_hashes["c59_route"],
            "c59_route_archive_sha256": route_archive_hash,
            "c59_resolvent_module_sha256": actual_hashes["c59_resolvent_module"],
            "c59_resolvent_evidence_sha256": actual_hashes["c59_resolvent_evidence"],
            "c59_resolvent_payload_sha256": c59_document["payload_sha256"],
            "c60_durable_group_literals_sha256": compact_sha256(DURABLE_GROUP_LITERALS),
            "c60_durable_carrier_literals_sha256": compact_sha256(DURABLE_CARRIER_LITERALS),
            "released_c59_rebound": True,
        },
        "constants": {
            "degree": DEGREE,
            "prime": PRIME,
            "w_order": W_ORDER,
            "expected_orbit_degrees": EXPECTED_DEGREES,
            "expected_coefficient_hashes": EXPECTED_COEFFICIENT_HASHES,
            "scope_literal": SCOPE_LITERAL,
        },
        "transport": {
            "convention": TRANSPORT_CONVENTION,
            "label_permutation_one_based": [item + 1 for item in x],
            "H3_order": len(hthree),
            "transported_support_stabilizer_order": len(hthree_from_support),
            "H3_equals_transported_support_stabilizer": set(hthree) == set(hthree_from_support),
            "H3_contained_in_N": set(hthree).issubset(set(n_group)),
            "H301_intersection_H3_order": len(set(hplus).intersection(hthree)),
        },
        "groups": {
            "orders_Hplus_H0_Hminus_H3_N_J": orders,
            "Hplus_generators_sha256": compact_sha256([[item + 1 for item in row] for row in hplus_generators]),
            "H0_generators_sha256": compact_sha256([[item + 1 for item in row] for row in hzero_generators]),
            "Hminus_generators_sha256": compact_sha256([[item + 1 for item in row] for row in hminus_generators]),
            "H3_generators_sha256": compact_sha256([[item + 1 for item in row] for row in [c59.compose(c59.compose(x, h), x_inverse) for h in hminus_generators]]),
            "N_generators_sha256": compact_sha256([[item + 1 for item in row] for row in n_generators]),
            "J_generators_sha256": compact_sha256([[item + 1 for item in row] for row in j_generators]),
        },
        "carriers": carriers,
        "fixed_field_bridge": {
            "c59_factor_degrees": finite_field["factor_degrees"],
            "c59_split_roots_distinct": len(set(finite_field["roots_sorted"])) == 27,
            "c59_label_map_is_graph_isomorphism": line_configuration["mapping_is_graph_isomorphism"],
            "c59_all_27_line_equations_zero": line_configuration["all_equation_residues_zero"],
            "prime_unramified": finite_field["denominator_envelope"]["all_nonzero"] and finite_field["multiplyback_matches_normalized_eliminant"],
            "labelled_W_action_faithful": labelled_w_action_faithful,
            "K_completely_split_witness": labelled_w_action_faithful,
            "support_stabilizers_exact_on_Z_labelled_carrier": {
                name: carriers[name]["stabilizer_equals_expected"] for name in ["M", "F0", "L"]
            },
            "modular_distinct_value_counts": {
                name: carriers[name]["modular_polynomial"]["distinct_value_count"] for name in ["M", "F0", "L"]
            },
            "characteristic_zero_orbit_values_distinct": True,
            "fixed_field_identities": EXPECTED_FIXED_FIELD_IDENTITIES,
            "fixed_field_reason": FIXED_FIELD_REASON,
        },
        "invariant_degree_obstruction": {
            "H0_and_N_point_partitions_equal": point_orbits_hzero == point_orbits_n,
            "H0_and_N_unordered_pair_partitions_equal": pair_orbits_hzero == pair_orbits_n,
            "H0_point_orbit_sizes": [len(item) for item in point_orbits_hzero],
            "H0_pair_orbit_sizes": [len(item) for item in pair_orbits_hzero],
            "H0_point_partition_sha256": compact_sha256(point_orbits_hzero),
            "H0_pair_partition_sha256": compact_sha256(pair_orbits_hzero),
            "selected_cubic_orbit_size": len(fzero_carrier),
            "selected_cubic_support_sha256": carriers["F0"]["carrier_sha256"],
            "formal_polynomial_scope": "commutative Q-coefficient formal polynomials in 27 independent labelled variables",
        },
        "replay_contract": EXPECTED_REPLAY_CONTRACT,
        "scope": {
            "scope_literal": SCOPE_LITERAL,
            "bad_artin_euler_claimed": False,
            "bad_euler_or_root_number_claimed": False,
            "characteristic_zero_coefficients_claimed": False,
            "class_number_claimed": False,
            "decomposition_frobenius_claimed": False,
            "local_fields_classified_by_tuples": False,
            "maximal_orders_claimed": False,
            "target_selection_or_unpromoted_aids_are_authority": False,
            "root_number_claimed": False,
        },
        "status": EXPECTED_STATUS,
    }
    document = {
        "schema_id": SCHEMA_ID,
        "schema_sha256": compact_sha256(SCHEMA_DESCRIPTOR),
        "payload_sha256": sha256_bytes(canonical_bytes(payload)),
        "payload": payload,
    }
    validate_evidence_document(document)
    if any(stable_file_bytes(path) != input_snapshots[name] for name, path in input_paths.items()):
        raise ValueError("released C59 authority changed during C60 evidence reconstruction")
    return document


STAGE_PATTERN = re.compile(r"^\.c60-stage-[A-Za-z0-9]{8}$")
EVIDENCE_BASENAME = "c60_resolvent_evidence.json"
SCHEMA_BASENAME = "c60_resolvent_schema.json"


def staged_path(value: str, expected_basename: str) -> tuple[Path, Path, tuple[int, int]]:
    path = Path(value).absolute()
    project = Path(__file__).resolve().parent.parent
    results = (project / "results").resolve(strict=True)
    stage = path.parent
    if (
        path.name != expected_basename
        or STAGE_PATTERN.fullmatch(stage.name) is None
        or stage.parent != results
        or not stage.is_dir()
        or stage.is_symlink()
        or stage.resolve(strict=True) != stage
    ):
        raise ValueError("target must be fixed basename under PROJECT/results/.c60-stage-XXXXXXXX")
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
        raise ValueError("canonical C60 results stage changed during replay")


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
    parser.add_argument("--c59-resolvent-module", type=Path, required=True)
    parser.add_argument("--c59-resolvent-evidence", type=Path, required=True)
    parser.add_argument("--c59-full-manifest", type=Path, required=True)
    parser.add_argument("--c59-route", type=Path, required=True)
    parser.add_argument("--c59-route-archive", type=Path, required=True)
    evidence_destination = parser.add_mutually_exclusive_group(required=True)
    evidence_destination.add_argument("--output")
    evidence_destination.add_argument("--check-existing")
    schema_destination = parser.add_mutually_exclusive_group(required=True)
    schema_destination.add_argument("--schema-output")
    schema_destination.add_argument("--check-existing-schema")
    arguments = parser.parse_args()

    writing = arguments.output is not None
    if writing != (arguments.schema_output is not None):
        raise ValueError("evidence and schema destinations must both write or both replay")
    selected_evidence = arguments.output if writing else arguments.check_existing
    selected_schema = arguments.schema_output if writing else arguments.check_existing_schema
    evidence_path, stage, identity = staged_path(selected_evidence, EVIDENCE_BASENAME)
    schema_path, schema_stage, schema_identity = staged_path(selected_schema, SCHEMA_BASENAME)
    if stage != schema_stage or identity != schema_identity:
        raise ValueError("schema and evidence must share one canonical stage")
    if evidence_path == schema_path:
        raise ValueError("schema and evidence paths must not alias")
    evidence_before = stable_file_bytes(evidence_path) if not writing else None
    schema_before = stable_file_bytes(schema_path) if not writing else None
    if writing:
        for path in [evidence_path, schema_path]:
            if os.path.lexists(path):
                stable_file_bytes(path)

    c59_inputs = {
        "c59_resolvent_module": arguments.c59_resolvent_module.resolve(strict=True),
        "c59_resolvent_evidence": arguments.c59_resolvent_evidence.resolve(strict=True),
        "c59_full_manifest": arguments.c59_full_manifest.resolve(strict=True),
        "c59_route": arguments.c59_route.resolve(strict=True),
        "c59_route_archive": arguments.c59_route_archive.resolve(strict=True),
    }
    c59_before = {name: stable_file_bytes(path) for name, path in c59_inputs.items()}
    started = time.perf_counter()
    assert_stage_identity(stage, identity)
    document = build_document(
        **c59_inputs,
    )
    evidence_bytes = canonical_bytes(document)
    schema_bytes = canonical_bytes(SCHEMA_DESCRIPTOR)
    assert_stage_identity(stage, identity)
    if any(stable_file_bytes(path) != c59_before[name] for name, path in c59_inputs.items()):
        raise ValueError("released C59 authority changed during CLI replay")
    if writing:
        atomic_write(schema_path, schema_bytes)
        assert_stage_identity(stage, identity)
        if stable_file_bytes(schema_path)[0] != schema_bytes:
            raise ValueError("schema write did not rebind to intended bytes")
        atomic_write(evidence_path, evidence_bytes)
        assert_stage_identity(stage, identity)
        if stable_file_bytes(evidence_path)[0] != evidence_bytes:
            raise ValueError("evidence write did not rebind to intended bytes")
        mode = "write"
    else:
        assert evidence_before is not None and schema_before is not None
        evidence_after = stable_file_bytes(evidence_path)
        schema_after = stable_file_bytes(schema_path)
        if evidence_after != evidence_before or evidence_after[0] != evidence_bytes:
            raise ValueError("existing evidence changed or is not byte-identical to fresh replay")
        if schema_after != schema_before or schema_after[0] != schema_bytes:
            raise ValueError("existing schema changed or is not byte-identical to fresh replay")
        mode = "replay"
    assert_stage_identity(stage, identity)
    print(json.dumps({
        "bytes": len(evidence_bytes),
        "elapsed_seconds": round(time.perf_counter() - started, 6),
        "evidence_sha256": sha256_bytes(evidence_bytes),
        "mode": mode,
        "payload_sha256": document["payload_sha256"],
        "schema_sha256": sha256_bytes(schema_bytes),
        "status": "PASS",
        "target": EVIDENCE_BASENAME,
    }, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
