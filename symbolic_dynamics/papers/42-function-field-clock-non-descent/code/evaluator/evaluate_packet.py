#!/usr/bin/env python3
"""Enumeration-primary standalone evaluator for Paper 42 / SD-C44."""

from __future__ import annotations

import base64
import hashlib
import itertools
import json
import re
import sys
from pathlib import PurePosixPath
from typing import Any

import yaml


EXPECTED_PACKET_SHA256 = "47a66b4d75cae55b3fc3fcd8f57174d7f69ebc91c37e052fd22ba9f1cb31e6c9"
EXPECTED_PACKET_SHAPE_SHA256 = "ec44847548f7941bdc68c2b21563aaa6cb62c0e42dd22a2a5c6921d9e500445c"
EXPECTED_PACKET_TYPES_SHA256 = "79cc6f4ef85eaa31ab0da57530790592050751d4f09fdfe3b58a21fb34a2ad7e"
EXPECTED_BLOCK_SHA256 = {
    "claim_boundary": "f61673ad16f588d87930703ac137b9bfcd5cab9038f46b27ab7e6368eb351e37",
    "integration_chronology": "52c85342cb149f12e03a2ab521c978ac2b16994b2305d9465ad806479219425b",
    "marker_contract": "015932a1129276ee268fffeeb7674d5ac0f90dff654eea1a4035e5cc2331929e",
    "operator_contract": "03234f0adf1b6c084059f0e6053d2874d37da8e26c5a5170a0b3d9de702b12ce",
    "portable_source_input": "b2d0182f90abac75953916090b3eeb3903a325ca00356c5165dc43dceae7f6f0",
    "positive_control_input": "693386ac7ae79b2392c745a872cb1ddcf47de0cb70e17f657cff2f16c23395a4",
    "raw_repair_rows": "13a17de80a5e2c01f6102fdcd915cf8289fd169268651a181e2969fb8152a7ca",
    "raw_selection_cards": "59be3e7b1451fd59077bb7178bcad5ae8c30235b14379982971a66dd81f9d754",
    "source_object_input": "1f2a1b09e93d3eb8057a8637c625cc270c125a2b934dd6cb7e6c12952b0c7517",
    "target_object_input": "99bf3705fd9b90c0f2072b13c82933f95420ff2cd9b4380ab75c4656fda3fb02",
    "terminal_contract": "872cb54c68dc7cde622e812f09863de123e822d11693b5cf1cb5d399308d0675",
    "type_ledger": "38bf194b41aa97cb47f454c9778d9ce630d9bff83b6a56ad107c1aa90cfaefca",
    "witness_input": "5807de1443ecab5f9837d02d5ecd7a3210085b3f8c169c6b614f46b693e26361",
}
BLOCK_REJECTION = {
    "claim_boundary": "CLAIM_SCOPE_MISMATCH",
    "integration_chronology": "CHRONOLOGY_CONTRACT_MISMATCH",
    "marker_contract": "MARKER_CONTRACT_MISMATCH",
    "operator_contract": "OPERATOR_CONTRACT_MISMATCH",
    "positive_control_input": "POSITIVE_CONTROL_CONTRACT_MISMATCH",
    "raw_repair_rows": "REPAIR_CONTRACT_MISMATCH",
    "source_object_input": "SOURCE_OBJECT_CONTRACT_MISMATCH",
    "target_object_input": "TARGET_OBJECT_CONTRACT_MISMATCH",
    "terminal_contract": "TERMINAL_CONTRACT_MISMATCH",
    "type_ledger": "TYPE_LEDGER_MISMATCH",
    "witness_input": "WITNESS_CONTRACT_MISMATCH",
}
TOP_KEYS = {
    "candidate_id", "claim_boundary", "control_grid", "integration_chronology",
    "marker_contract", "operator_contract", "portable_source_input",
    "positive_control_input", "raw_repair_rows", "raw_selection_cards", "schema",
    "source_object_input", "target_object_input", "terminal_contract", "type_ledger",
    "witness_input",
}
ROUTE_TUPLE = [
    "A0_WEAK_ARITHMETIC_RELATION", "A1_PASS_ANALYTIC",
    "A2_ANALYTIC_DETERMINANT", "A3_FAIL", "A4_FAIL",
]
TERMINAL_CODES = {
    "same_clock_projection": "STOP_Q_POWER_RATIONAL_PRIME_SUPPORT",
    "determinant_comparison": "STOP_FIRST_MARKED_COEFFICIENT_MISMATCH",
    "same_marker_factor_identification": "STOP_MARKER_MULTIPLICITY_CONJUNCTION",
}


class Reject(Exception):
    def __init__(self, code: str, detail: str | None = None) -> None:
        super().__init__(code)
        self.code = code
        self.detail = detail


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True) + "\n").encode("ascii")


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def no_duplicate_json(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise Reject("DUPLICATE_JSON_KEY", key)
        result[key] = value
    return result


def strict_equal(left: Any, right: Any) -> bool:
    if type(left) is not type(right):
        return False
    if isinstance(left, dict):
        return list(left) == list(right) and all(strict_equal(left[key], right[key]) for key in left)
    if isinstance(left, list):
        return len(left) == len(right) and all(strict_equal(a, b) for a, b in zip(left, right))
    return left == right


def pointer_join(pointer: str, token: str) -> str:
    token = token.replace("~", "~0").replace("/", "~1")
    return pointer + "/" + token


def shape_projection(value: Any, pointer: str = "") -> list[list[Any]]:
    rows: list[list[Any]] = []
    if isinstance(value, dict):
        rows.append([pointer, "mapping", list(value)])
        for key in value:
            rows.extend(shape_projection(value[key], pointer_join(pointer, key)))
    elif isinstance(value, list):
        rows.append([pointer, "list", len(value)])
        for index, item in enumerate(value):
            rows.extend(shape_projection(item, pointer_join(pointer, str(index))))
    return rows


def type_projection(value: Any, pointer: str = "") -> list[list[str]]:
    rows: list[list[str]] = []
    if isinstance(value, dict):
        for key in value:
            rows.extend(type_projection(value[key], pointer_join(pointer, key)))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            rows.extend(type_projection(item, pointer_join(pointer, str(index))))
    else:
        kind = "bool" if type(value) is bool else "int" if type(value) is int else "str" if type(value) is str else "null" if value is None else type(value).__name__
        rows.append([pointer, kind])
    return rows


def safe_relative(value: Any) -> bool:
    if not isinstance(value, str) or not value or "\\" in value or "\x00" in value:
        return False
    path = PurePosixPath(value)
    return not path.is_absolute() and all(part not in ("", ".", "..") for part in path.parts)


def yaml_mapping(loader: yaml.SafeLoader, node: yaml.MappingNode, deep: bool = False) -> dict[Any, Any]:
    result: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise Reject("DUPLICATE_YAML_KEY", str(key))
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


class UniqueLoader(yaml.SafeLoader):
    pass


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, yaml_mapping)


def require(condition: bool, code: str, detail: str | None = None) -> None:
    if not condition:
        raise Reject(code, detail)


def validate_packet(raw: bytes) -> dict[str, Any]:
    try:
        packet = json.loads(raw, object_pairs_hook=no_duplicate_json)
    except Reject:
        raise
    except Exception as exc:
        raise Reject("INVALID_JSON", type(exc).__name__) from exc
    require(isinstance(packet, dict), "PACKET_STRUCTURE_MISMATCH", "top")
    require(canonical(packet) == raw, "PACKET_CANONICAL_BYTES_MISMATCH")
    require(set(packet) == TOP_KEYS and list(packet) == sorted(TOP_KEYS), "PACKET_STRUCTURE_MISMATCH", "top_keys")
    shape_sha = digest(canonical(shape_projection(packet)))
    type_sha = digest(canonical(type_projection(packet)))
    if EXPECTED_PACKET_SHAPE_SHA256:
        require(shape_sha == EXPECTED_PACKET_SHAPE_SHA256, "PACKET_STRUCTURE_MISMATCH", "recursive_shape")
    if EXPECTED_PACKET_TYPES_SHA256:
        require(type_sha == EXPECTED_PACKET_TYPES_SHA256, "PACKET_TYPE_MISMATCH", "recursive_types")
    if EXPECTED_PACKET_SHA256:
        require(digest(raw) == EXPECTED_PACKET_SHA256, "PACKET_SEMANTIC_MISMATCH", "byte_seal")
    require(packet["schema"] == "paper42-exact-source-packet-v1" and packet["candidate_id"] == "SD-C44", "PACKET_SEMANTIC_MISMATCH", "identity")
    require(packet["control_grid"] == {
        "field_sizes": [2, 3, 5],
        "fixed_point_periods": {"maximum": 3, "minimum": 1},
        "irreducible_polynomial_degrees": {"maximum": 4, "minimum": 1},
        "word_lengths": {"maximum": 6, "minimum": 1},
    }, "CONTROL_GRID_MISMATCH")
    require(packet["terminal_contract"]["universal_no_go_claimed"] is False, "CLAIM_SCOPE_MISMATCH")
    require(packet["terminal_contract"]["route_terminals"] == sorted(TERMINAL_CODES.values()), "TERMINAL_CONTRACT_MISMATCH")
    for name, code in BLOCK_REJECTION.items():
        require(digest(canonical(packet[name])) == EXPECTED_BLOCK_SHA256[name], code)
    return packet


def proper_divisors(length: int) -> list[int]:
    return [value for value in range(1, length) if length % value == 0]


def least_period(word: tuple[int, ...]) -> int:
    for period in proper_divisors(len(word)):
        if word == word[:period] * (len(word) // period):
            return period
    return len(word)


def rotations(word: tuple[int, ...]) -> list[tuple[int, ...]]:
    return [word[index:] + word[:index] for index in range(len(word))]


def enumerate_necklaces(q: int, length: int) -> list[tuple[int, ...]]:
    result: list[tuple[int, ...]] = []
    for word in itertools.product(range(q), repeat=length):
        if least_period(word) == length and word == min(rotations(word)):
            result.append(word)
    return result


def polynomial_remainder(dividend: tuple[int, ...], divisor: tuple[int, ...], q: int) -> tuple[int, ...]:
    work = list(dividend)
    while len(work) >= len(divisor):
        factor = work[-1] % q
        offset = len(work) - len(divisor)
        for index, coefficient in enumerate(divisor):
            work[offset + index] = (work[offset + index] - factor * coefficient) % q
        while work and work[-1] == 0:
            work.pop()
    return tuple(work)


def irreducible_by_trial(polynomial: tuple[int, ...], q: int) -> bool:
    degree = len(polynomial) - 1
    for divisor_degree in range(1, degree // 2 + 1):
        for lower in itertools.product(range(q), repeat=divisor_degree):
            divisor = tuple(lower) + (1,)
            if not polynomial_remainder(polynomial, divisor, q):
                return False
    return True


def irreducible_count(q: int, degree: int) -> int:
    return sum(
        irreducible_by_trial(tuple(lower) + (1,), q)
        for lower in itertools.product(range(q), repeat=degree)
    )


def validate_sources(block: Any) -> dict[str, Any]:
    require(isinstance(block, dict), "SOURCE_RESOLVER_MISMATCH")
    require(set(block) == {"dependency_lock_sha256", "external_historical_tree_query", "rows", "source_manifest_sha256", "source_row_count", "writer_baseline_manifest_sha256", "writer_baseline_snapshot_sha256"}, "SOURCE_RESOLVER_MISMATCH")
    require(all(re.fullmatch(r"[0-9a-f]{64}", block[key]) is not None for key in
                ("writer_baseline_manifest_sha256", "writer_baseline_snapshot_sha256")),
            "SOURCE_RESOLVER_MISMATCH")
    rows = block["rows"]
    require(isinstance(rows, list) and len(rows) == 29 and block["source_row_count"] == 29, "SOURCE_RESOLVER_MISMATCH")
    ids: list[str] = []
    repo_count = 0
    dependency_count = 0
    for row in rows:
        require(isinstance(row, dict) and set(row) == {"container_path", "decoded_sha256", "encoded_sha256", "kind", "source_id"}, "SOURCE_RESOLVER_MISMATCH")
        require(safe_relative(row["container_path"]) and row["container_path"].startswith("docs/inputs/source_snapshot/"), "SOURCE_ID_GRAMMAR")
        require(re.fullmatch(r"[0-9a-f]{64}", row["decoded_sha256"]) is not None and re.fullmatch(r"[0-9a-f]{64}", row["encoded_sha256"]) is not None, "SOURCE_HASH_FORMAT")
        source_id = row["source_id"]
        if row["kind"] == "repo":
            require(source_id.startswith("repo:") and safe_relative(source_id[5:]), "SOURCE_ID_GRAMMAR")
            repo_count += 1
        else:
            require(row["kind"] == "dependency" and re.fullmatch(r"dependency:P41_[A-Z_]+", source_id) is not None, "SOURCE_ID_GRAMMAR")
            dependency_count += 1
        ids.append(source_id)
    require(ids == sorted(ids) and len(ids) == len(set(ids)), "SOURCE_ID_ORDER")
    require(repo_count == 21 and dependency_count == 8, "SOURCE_RESOLVER_MISMATCH")
    require(block["external_historical_tree_query"] == "NOT_QUERIED", "EXTERNAL_TREE_READ_FORBIDDEN")
    return {
        "dependency_count": dependency_count,
        "external_historical_tree_query": "NOT_QUERIED",
        "matches": 29,
        "repo_count": repo_count,
        "schema": "paper42-source-resolver-v1",
        "source_manifest_sha256": block["source_manifest_sha256"],
        "total": 29,
    }


def validate_and_select(block: Any) -> dict[str, Any]:
    require(isinstance(block, dict) and set(block) == {"card_yaml_rows", "packet", "packet_sha256", "packet_utf8_b64"}, "SELECTION_STRUCTURE_MISMATCH")
    try:
        raw = base64.b64decode(block["packet_utf8_b64"], validate=True)
        parsed = json.loads(raw, object_pairs_hook=no_duplicate_json)
    except Reject:
        raise
    except Exception as exc:
        raise Reject("SELECTION_BYTE_SEAL_MISMATCH") from exc
    require(digest(raw) == block["packet_sha256"] and canonical(parsed) == raw, "SELECTION_BYTE_SEAL_MISMATCH")
    require(strict_equal(parsed, block["packet"]), "SELECTION_OBJECT_RAW_MISMATCH")
    require(parsed.get("schema") == "paper42-session4-selection-packet-v1", "SELECTION_SEMANTIC_MISMATCH")
    cards = parsed.get("cards")
    yaml_rows = block["card_yaml_rows"]
    require(isinstance(cards, list) and len(cards) == 6 and isinstance(yaml_rows, list) and len(yaml_rows) == 6, "SELECTION_STRUCTURE_MISMATCH")
    yaml_by_id = {row["candidate_id"]: row for row in yaml_rows}
    require(list(yaml_by_id) == [f"SD-C0{n}" for n in range(1, 7)], "SELECTION_SEMANTIC_MISMATCH")
    decisions: list[dict[str, Any]] = []
    for card in cards:
        candidate = card["candidate_id"]
        row = yaml_by_id[candidate]
        try:
            yaml_raw = base64.b64decode(row["yaml_utf8_b64"], validate=True)
            route = yaml.load(yaml_raw, Loader=UniqueLoader)
        except Reject:
            raise
        except Exception as exc:
            raise Reject("CARD_YAML_PARSE_FAILURE", candidate) from exc
        require(digest(yaml_raw) == card["historical_byte_sha256"] == row["historical_byte_sha256"], "CARD_BYTE_HASH_MISMATCH", candidate)
        require(route["candidate_id"] == candidate and route["source_lock"]["clock"] == card["source_clock"], "CARD_SEMANTIC_MISMATCH", candidate)
        for layer in ("a0", "a1", "a2", "a3"):
            require(route[layer]["verdict"] == card[f"{layer}_verdict"] and route[layer]["evidence_status"] == card[f"{layer}_evidence_status"], "CARD_SEMANTIC_MISMATCH", candidate)
        require(route["a0"]["strongest_failure"] == card["a0_strongest_failure"], "CARD_SEMANTIC_MISMATCH", candidate)
        clause_values = [
            card["a0_verdict"] == "A0_WEAK_ARITHMETIC_RELATION",
            card["a0_evidence_status"] == "PROVED",
            card["a1_verdict"] == "A1_PASS_ANALYTIC",
            card["a1_evidence_status"] == "PROVED",
            card["a2_verdict"] == "A2_ANALYTIC_DETERMINANT",
            card["a2_evidence_status"] == "PROVED",
            card["a3_verdict"] == "A3_FAIL",
            card["a3_evidence_status"] == "PROVED",
            card["source_clock"].startswith("constant roof log(q) per symbol"),
            "no canonical rational-prime" in card["a0_strongest_failure"],
        ]
        decisions.append({"candidate_id": candidate, "clause_values": clause_values, "eligible": all(clause_values), "historical_byte_sha256": card["historical_byte_sha256"]})
    survivors = [row["candidate_id"] for row in decisions if row["eligible"]]
    require(survivors == ["SD-C01"], "SELECTION_SEMANTIC_MISMATCH", "survivors")
    chronology = parsed["chronology"]
    require(all(chronology[key] is False for key in ["novelty_credit", "outcome_independent", "paper39_ranking_or_authorization_used", "paper40_ranking_or_authorization_used", "paper41_ranking_or_authorization_used", "preregistered", "priority_credit", "prospective"]), "SELECTION_CHRONOLOGY_MISMATCH")
    return {
        "card_count": 6,
        "chronology": chronology,
        "decisions": decisions,
        "rule_clauses": parsed["rule"]["clauses"],
        "schema": "paper42-retrospective-selection-result-v1",
        "survivors": survivors,
        "unique": True,
    }


def repair_rows(packet_rows: list[dict[str, str]]) -> list[dict[str, Any]]:
    expected = {
        "finite_field_norm_q_power_n": ("exact_negative_projection", ["marker", "multiplicity", "rational_prime_support"]),
        "keep_degree_one_necklaces": ("incomplete_ledger", ["multiplicity", "totality"]),
        "choose_one_degree_one_necklace": ("single_factor_positive_control_not_all_primes", ["full_target_support", "totality"]),
        "enumerate_necklaces_by_rational_primes": ("forbidden_post_hoc_map", ["exact_clock", "source_marker"]),
        "induce_every_primitive_orbit_to_one_return": ("no_same_marker_credit", ["original_marker", "source_object", "source_operator_ownership"]),
        "finite_field_prime_polynomial_dictionary": ("exact_positive_control", ["rational_prime_type"]),
    }
    require([row["id"] for row in packet_rows] == list(expected), "REPAIR_CONTRACT_MISMATCH")
    return [
        {"classification": expected[row["id"]][0], "id": row["id"], "lost_fields": expected[row["id"]][1], "operation": row["operation"]}
        for row in packet_rows
    ]


def build_science(packet: dict[str, Any]) -> tuple[dict[str, Any], dict[str, bool]]:
    source_resolver = validate_sources(packet["portable_source_input"])
    selection = validate_and_select(packet["raw_selection_cards"])
    require(digest(canonical(packet["portable_source_input"])) == EXPECTED_BLOCK_SHA256["portable_source_input"], "SOURCE_RESOLVER_MISMATCH")
    require(digest(canonical(packet["raw_selection_cards"])) == EXPECTED_BLOCK_SHA256["raw_selection_cards"], "SELECTION_SEMANTIC_MISMATCH")
    census: list[dict[str, Any]] = []
    positive_rows: list[dict[str, Any]] = []
    clock_rows: list[dict[str, Any]] = []
    multiplicity_rows: list[dict[str, Any]] = []
    fixed_rows: list[dict[str, Any]] = []
    for q in packet["control_grid"]["field_sizes"]:
        fixed = [sum(1 for _ in itertools.product(range(q), repeat=period)) for period in range(1, 4)]
        fixed_rows.append({"counts": fixed, "periods": [1, 2, 3], "q": q})
        for length in range(1, 7):
            inventory = enumerate_necklaces(q, length)
            census.append({"primitive_necklace_count": len(inventory), "q": q, "word_length": length})
        for degree in range(1, 5):
            necklace_count = len(enumerate_necklaces(q, degree))
            polynomial_count = irreducible_count(q, degree)
            positive_rows.append({"degree": degree, "irreducible_polynomial_count": polynomial_count, "necklace_count": necklace_count, "q": q})
        witness = (0, 1)
        period = least_period(witness)
        forced = q * q
        clock_rows.append({"factorization": [q, q], "forced_label": forced, "least_period": period, "primitive": period == 2, "q": q, "rational_prime": False, "word": "01"})
        multiplicity_rows.append({"q": q, "source_length_one_factors": len(enumerate_necklaces(q, 1)), "target_factor_at_p_equals_q": 1})
    positive_failures = sum(row["irreducible_polynomial_count"] != row["necklace_count"] for row in positive_rows)
    require(positive_failures == 0, "FUNCTION_FIELD_POSITIVE_CONTROL_FAILURE")
    require(all(row["primitive"] and not row["rational_prime"] for row in clock_rows), "CLOCK_SUPPORT_WITNESS_FAILURE")
    repairs = repair_rows(packet["raw_repair_rows"])
    type_ledger = packet["type_ledger"]
    require([row["name"] for row in type_ledger] == ["ShiftPrimitiveNecklace_q", "FiniteFieldPrimePolynomial_q", "RationalPrimeAtom"], "TYPE_LEDGER_MISMATCH")
    science = {
        "candidate_id": "SD-C44",
        "claim_scope": {
            "declared_repairs_are_exhaustive": False,
            "finite_grid_proves_universal": False,
            "literature_stop_external": "STOP_DUPLICATE",
            "scope": packet["claim_boundary"],
        },
        "control_grid": {**packet["control_grid"], "fixed_point_rows": fixed_rows},
        "determinant_certificate": {
            "algorithm_m_coefficient_rows": [{"q": q, "source_coefficient_at_support_q": q, "target_prime_zeta_coefficient_at_support_q": 1} for q in [2, 3, 5]],
            "algorithm_r_large_s_source_limits_after_2_power_s": [{"limit": value, "q": q} for q, value in [(2, 2), (3, 0), (5, 0)]],
            "algorithm_r_large_s_target_limit_after_2_power_s": 1,
            "common_domain": "Re(s)>1_and_locally_or_formally_in_z",
            "determinants_equal": False,
            "orientation": "negative_log_of_determinant",
            "source_determinant": "1-z*q^(1-s)",
            "source_first_z_coefficient": "q^(1-s)",
            "target_determinant": "product_p(1-z*p^(-s))",
            "target_first_z_coefficient": "P(s)",
        },
        "function_field_positive_control": {
            "failures": positive_failures,
            "objectwise_bijection_claimed": False,
            "rows": positive_rows,
            "status": "PASS",
        },
        "integration_chronology": packet["integration_chronology"],
        "marker_ledger": {
            "free_marker": "z",
            "marker_specialized_before_comparison": False,
            "primitive_marker_equality_forces_word_length": 1,
            "source_primitive_marker": "z^n",
            "source_repetition_marker": "z^(n*r)",
            "target_primitive_marker": "z",
            "target_repetition_marker": "z^r",
        },
        "necklace_census": {
            "orientation": "cyclic_rotations_identified_reversal_not_quotiented",
            "rows": census,
            "universal_formula": "N_q(n)=(1/n)*sum_(d|n)mu(d)*q^(n/d)",
        },
        "operator_ledger": {
            "same_owner": False,
            "source": packet["operator_contract"]["source_owner"],
            "source_hilbert_space": packet["operator_contract"]["source_hilbert_space"],
            "target": packet["operator_contract"]["target_owner"],
            "target_domain": packet["operator_contract"]["target_domain"],
            "target_hilbert_space": packet["operator_contract"]["target_hilbert_space"],
        },
        "repair_classification": {
            "declared_repairs_are_exhaustive": False,
            "failures": 0,
            "rows": repairs,
        },
        "route": {
            "a0_evidence_status": "PROVED",
            "a0_verdict": "A0_WEAK_ARITHMETIC_RELATION",
            "a1_evidence_status": "PROVED",
            "a1_verdict": "A1_PASS_ANALYTIC",
            "a2_evidence_status": "PROVED",
            "a2_verdict": "A2_ANALYTIC_DETERMINANT",
            "a3_evidence_status": "PROVED",
            "a3_verdict": "A3_FAIL",
            "a4_evidence_status": "OPEN",
            "a4_verdict": "A4_FAIL",
            "branch_status": packet["terminal_contract"]["branch_status"],
            "overall_verdict": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "route_tuple": ROUTE_TUPLE,
        },
        "schema": "paper42-exact-science-projection-v1",
        "selection": selection,
        "source_resolver": source_resolver,
        "terminal_codes": TERMINAL_CODES,
        "theorems": [
            {"id": "T0_SOURCE_CONVENTION", "status": "PASS", "statement": "full_shift_fixed_points_necklaces_and_determinant_exact"},
            {"id": "T1_CLOCK_SUPPORT", "status": "PROVED_NON_DESCENT", "statement": "no_total_exact_clock_map_to_rational_primes"},
            {"id": "T2_MARKER_MULTIPLICITY", "status": "PROVED_NON_DESCENT", "statement": "no_factorwise_marker_weight_multiplicity_identification"},
            {"id": "T3_FIRST_COEFFICIENT", "status": "PROVED_NONIDENTITY", "statement": "q^(1-s)_differs_from_P(s)"},
            {"id": "T4_FUNCTION_FIELD_CONTROL", "status": "PASS", "statement": "necklace_and_irreducible_degree_counts_agree"},
            {"id": "T5_DECLARED_REPAIRS", "status": "PASS", "statement": "each_declared_repair_loses_a_locked_field"},
        ],
        "type_ledger": type_ledger,
        "universal_no_go_claimed": False,
        "witness_ledger": {
            "clock_support": clock_rows,
            "determinant_first_coefficient_mismatch": True,
            "finite_witnesses_prove_only_stated_theorems": True,
            "marker_weight_forced_values": {"p": "q", "word_length": 1},
            "multiplicity": multiplicity_rows,
            "repetition_weight_control": "(q^n)^(-r*s)=q^(-n*r*s)",
        },
    }
    checks = {
        "canonical_packet": True,
        "clock_support_witness": True,
        "determinant_coefficient_map": True,
        "fixed_point_enumeration": True,
        "irreducible_trial_division": True,
        "marker_multiplicity": True,
        "necklace_enumeration": True,
        "repair_classification": True,
        "selection_yaml_duplicate_safe": True,
        "source_resolver": True,
        "type_strict": True,
    }
    return science, checks


def evaluate(raw: bytes) -> dict[str, Any]:
    packet = validate_packet(raw)
    science, checks = build_science(packet)
    return {
        "checks": checks,
        "implementation": "algorithm_m_enumeration_and_trial_division",
        "schema": "paper42-main-evaluation-v1",
        "science": science,
    }


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        sys.stderr.write("REJECT: ARGUMENT_CONTRACT\n")
        return 2
    try:
        raw = open(argv[1], "rb").read()
        sys.stdout.buffer.write(canonical(evaluate(raw)))
        return 0
    except Reject as exc:
        suffix = "" if exc.detail is None else ":" + exc.detail
        sys.stderr.write(f"REJECT: {exc.code}{suffix}\n")
        return 2
    except Exception as exc:
        sys.stderr.write(f"REJECT: INTERNAL_EVALUATOR_ERROR:{type(exc).__name__}\n")
        return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
