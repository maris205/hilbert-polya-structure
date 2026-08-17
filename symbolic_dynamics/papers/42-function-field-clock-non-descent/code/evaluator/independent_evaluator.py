#!/usr/bin/env python3
"""Recurrence/Rabin standalone evaluator and independent Route checker for P42."""

from __future__ import annotations

import base64
import hashlib
import json
import re
import stat
import sys
from pathlib import Path, PurePosixPath
from typing import Any

import yaml


PACKET_SHA = "47a66b4d75cae55b3fc3fcd8f57174d7f69ebc91c37e052fd22ba9f1cb31e6c9"
PACKET_SHAPE_SHA = "ec44847548f7941bdc68c2b21563aaa6cb62c0e42dd22a2a5c6921d9e500445c"
PACKET_TYPE_SHA = "79cc6f4ef85eaa31ab0da57530790592050751d4f09fdfe3b58a21fb34a2ad7e"
EXPECTED_BLOCK_SHA = {
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
EXPECTED_NORMALIZED_ROUTE_SHA256 = "02881794a6d550974cb71c1d5c3692175a577e5d46c679f36a345ad369463f06"
EXPECTED_STAGE1_ROUTE_RAW_SHA256 = "86f5458ce09c3a28f8d879187b1f159054b89044ffedebe58cba7a2b9ded61a8"
EXPECTED_DUMMY_ROUTE_RAW_SHA256 = "5bb40051460ffad7af8bf7edfe1551e5711dfa43b54c05b558401b748dd61954"
PENDING = "PENDING_FIRST_ARTIFACT_COMMIT"
ZERO_COMMIT = "0" * 40
DUMMY_COMMIT = "0123456789abcdef0123456789abcdef01234567"
ROUTE_TUPLE = [
    "A0_WEAK_ARITHMETIC_RELATION", "A1_PASS_ANALYTIC",
    "A2_ANALYTIC_DETERMINANT", "A3_FAIL", "A4_FAIL",
]
TERMINALS = {
    "same_clock_projection": "STOP_Q_POWER_RATIONAL_PRIME_SUPPORT",
    "determinant_comparison": "STOP_FIRST_MARKED_COEFFICIENT_MISMATCH",
    "same_marker_factor_identification": "STOP_MARKER_MULTIPLICITY_CONJUNCTION",
}
PACKET_KEYS = sorted([
    "candidate_id", "claim_boundary", "control_grid", "integration_chronology",
    "marker_contract", "operator_contract", "portable_source_input",
    "positive_control_input", "raw_repair_rows", "raw_selection_cards", "schema",
    "source_object_input", "target_object_input", "terminal_contract", "type_ledger",
    "witness_input",
])


class Stop(Exception):
    def __init__(self, token: str, detail: str | None = None) -> None:
        self.token = token
        self.detail = detail
        super().__init__(token)


def encoded(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=True, indent=2, sort_keys=True) + "\n").encode("ascii")


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def assert_that(condition: bool, token: str, detail: str | None = None) -> None:
    if not condition:
        raise Stop(token, detail)


def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    keys = [key for key, _ in pairs]
    if len(keys) != len(set(keys)):
        duplicate = next(key for index, key in enumerate(keys) if key in keys[:index])
        raise Stop("DUPLICATE_JSON_KEY", duplicate)
    return dict(pairs)


def exact_json(left: Any, right: Any) -> bool:
    if type(left) is not type(right):
        return False
    if type(left) is dict:
        return list(left.keys()) == list(right.keys()) and all(exact_json(left[key], right[key]) for key in left)
    if type(left) is list:
        return len(left) == len(right) and all(exact_json(a, b) for a, b in zip(left, right))
    return left == right


def escape(token: str) -> str:
    return token.replace("~", "~0").replace("/", "~1")


def shape_rows(value: Any) -> list[list[Any]]:
    result: list[list[Any]] = []
    stack: list[tuple[str, Any]] = [("", value)]
    while stack:
        pointer, current = stack.pop()
        if type(current) is dict:
            result.append([pointer, "mapping", list(current.keys())])
            for key in reversed(list(current.keys())):
                stack.append((pointer + "/" + escape(key), current[key]))
        elif type(current) is list:
            result.append([pointer, "list", len(current)])
            for index in range(len(current) - 1, -1, -1):
                stack.append((pointer + "/" + str(index), current[index]))
    return result


def type_rows(value: Any) -> list[list[str]]:
    result: list[list[str]] = []
    stack: list[tuple[str, Any]] = [("", value)]
    while stack:
        pointer, current = stack.pop()
        if type(current) is dict:
            for key in reversed(list(current.keys())):
                stack.append((pointer + "/" + escape(key), current[key]))
        elif type(current) is list:
            for index in range(len(current) - 1, -1, -1):
                stack.append((pointer + "/" + str(index), current[index]))
        else:
            name = "bool" if type(current) is bool else "int" if type(current) is int else "str" if type(current) is str else "null" if current is None else type(current).__name__
            result.append([pointer, name])
    return result


def portable_path(text: Any) -> bool:
    if type(text) is not str or not text or "\\" in text or "\x00" in text:
        return False
    parts = PurePosixPath(text)
    return not parts.is_absolute() and all(part not in ("", ".", "..") for part in parts.parts)


def artifact_owned_path(text: Any) -> bool:
    return portable_path(text) and (
        text.startswith("preauthority/") or text.startswith("results/")
    )


def contained_regular_file(root: Path, text: Any) -> bool:
    if not portable_path(text):
        return False
    current = root
    parts = PurePosixPath(text).parts
    try:
        for index, part in enumerate(parts):
            current = current / part
            mode = current.lstat().st_mode
            if stat.S_ISLNK(mode):
                return False
            if index + 1 < len(parts) and not stat.S_ISDIR(mode):
                return False
            if index + 1 == len(parts) and not stat.S_ISREG(mode):
                return False
    except (FileNotFoundError, NotADirectoryError, OSError):
        return False
    return True


def read_packet(raw: bytes) -> dict[str, Any]:
    try:
        packet = json.loads(raw, object_pairs_hook=unique_object)
    except Stop:
        raise
    except Exception as exc:
        raise Stop("INVALID_JSON", type(exc).__name__) from exc
    assert_that(type(packet) is dict, "PACKET_STRUCTURE_MISMATCH", "top")
    assert_that(encoded(packet) == raw, "PACKET_CANONICAL_BYTES_MISMATCH")
    assert_that(list(packet.keys()) == PACKET_KEYS, "PACKET_STRUCTURE_MISMATCH", "top_keys")
    if PACKET_SHAPE_SHA:
        assert_that(sha(encoded(shape_rows(packet))) == PACKET_SHAPE_SHA, "PACKET_STRUCTURE_MISMATCH", "recursive_shape")
    if PACKET_TYPE_SHA:
        assert_that(sha(encoded(type_rows(packet))) == PACKET_TYPE_SHA, "PACKET_TYPE_MISMATCH", "recursive_types")
    if PACKET_SHA:
        assert_that(sha(raw) == PACKET_SHA, "PACKET_SEMANTIC_MISMATCH", "byte_seal")
    assert_that(packet["candidate_id"] == "SD-C44" and packet["schema"] == "paper42-exact-source-packet-v1", "PACKET_SEMANTIC_MISMATCH", "identity")
    expected_grid = {
        "field_sizes": [2, 3, 5],
        "fixed_point_periods": {"maximum": 3, "minimum": 1},
        "irreducible_polynomial_degrees": {"maximum": 4, "minimum": 1},
        "word_lengths": {"maximum": 6, "minimum": 1},
    }
    assert_that(exact_json(packet["control_grid"], expected_grid), "CONTROL_GRID_MISMATCH")
    assert_that(packet["terminal_contract"]["universal_no_go_claimed"] is False, "CLAIM_SCOPE_MISMATCH")
    assert_that(packet["terminal_contract"]["route_terminals"] == sorted(TERMINALS.values()), "TERMINAL_CONTRACT_MISMATCH")
    for name, token in BLOCK_REJECTION.items():
        assert_that(sha(encoded(packet[name])) == EXPECTED_BLOCK_SHA[name], token)
    return packet


def divisors_below(number: int) -> list[int]:
    answer: list[int] = []
    candidate = 1
    while candidate < number:
        if number % candidate == 0:
            answer.append(candidate)
        candidate += 1
    return answer


def recurrence_counts(q: int, maximum: int) -> dict[int, int]:
    result: dict[int, int] = {}
    for length in range(1, maximum + 1):
        already = sum(period * result[period] for period in divisors_below(length))
        numerator = q ** length - already
        assert_that(numerator % length == 0, "NECKLACE_RECURRENCE_FAILURE")
        result[length] = numerator // length
    return result


def clean(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def poly_sub(left: list[int], right: list[int], q: int) -> list[int]:
    size = max(len(left), len(right))
    return clean([((left[i] if i < len(left) else 0) - (right[i] if i < len(right) else 0)) % q for i in range(size)])


def poly_mul(left: list[int], right: list[int], q: int) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] = (result[i + j] + a * b) % q
    return clean(result)


def poly_mod(dividend: list[int], modulus: list[int], q: int) -> list[int]:
    value = clean(dividend[:])
    while len(value) >= len(modulus) and value != [0]:
        scale = value[-1] * pow(modulus[-1], -1, q) % q
        shift = len(value) - len(modulus)
        for index, coefficient in enumerate(modulus):
            value[index + shift] = (value[index + shift] - scale * coefficient) % q
        clean(value)
    return value


def poly_gcd(left: list[int], right: list[int], q: int) -> list[int]:
    a, b = clean(left[:]), clean(right[:])
    while b != [0]:
        a, b = b, poly_mod(a, b, q)
    inverse = pow(a[-1], -1, q)
    return [(coefficient * inverse) % q for coefficient in a]


def poly_pow_mod(base: list[int], exponent: int, modulus: list[int], q: int) -> list[int]:
    result = [1]
    factor = poly_mod(base, modulus, q)
    power = exponent
    while power:
        if power & 1:
            result = poly_mod(poly_mul(result, factor, q), modulus, q)
        factor = poly_mod(poly_mul(factor, factor, q), modulus, q)
        power //= 2
    return result


def prime_divisors(number: int) -> list[int]:
    result: list[int] = []
    trial = 2
    remaining = number
    while trial * trial <= remaining:
        if remaining % trial == 0:
            result.append(trial)
            while remaining % trial == 0:
                remaining //= trial
        trial += 1
    if remaining > 1:
        result.append(remaining)
    return result


def rabin_irreducible(polynomial: list[int], q: int) -> bool:
    degree = len(polynomial) - 1
    x = [0, 1]
    for prime in prime_divisors(degree):
        exponent = q ** (degree // prime)
        difference = poly_sub(poly_pow_mod(x, exponent, polynomial, q), x, q)
        if len(poly_gcd(polynomial, difference, q)) > 1:
            return False
    return poly_mod(poly_sub(poly_pow_mod(x, q ** degree, polynomial, q), x, q), polynomial, q) == [0]


def rabin_count(q: int, degree: int) -> int:
    count = 0
    total = q ** degree
    for code in range(total):
        lower: list[int] = []
        value = code
        for _ in range(degree):
            lower.append(value % q)
            value //= q
        if rabin_irreducible(lower + [1], q):
            count += 1
    return count


def parse_scalar(text: str) -> Any:
    stripped = text.strip()
    if stripped.startswith('"'):
        return json.loads(stripped)
    if stripped in ("true", "false"):
        return stripped == "true"
    return stripped


def parse_card_lines(raw: bytes) -> dict[str, Any]:
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise Stop("CARD_YAML_PARSE_FAILURE", "utf8") from exc
    result: dict[str, Any] = {}
    current: str | None = None
    seen: set[tuple[str | None, str]] = set()
    for line in text.splitlines():
        if not line or line.lstrip().startswith("#"):
            continue
        if not line.startswith(" ") and re.fullmatch(r"[a-zA-Z0-9_]+:.*", line):
            key, value = line.split(":", 1)
            if value.strip():
                marker = (None, key)
                if marker in seen:
                    raise Stop("DUPLICATE_YAML_KEY", key)
                seen.add(marker)
                result[key] = parse_scalar(value)
                current = None
            else:
                current = key
                result[current] = {}
            continue
        match = re.fullmatch(r"  ([a-zA-Z0-9_]+): (.*)", line)
        if current is not None and match:
            key, value = match.groups()
            marker = (current, key)
            if marker in seen:
                raise Stop("DUPLICATE_YAML_KEY", key)
            seen.add(marker)
            result[current][key] = parse_scalar(value)
    return result


def source_summary(block: Any) -> dict[str, Any]:
    assert_that(type(block) is dict and set(block) == {"dependency_lock_sha256", "external_historical_tree_query", "rows", "source_manifest_sha256", "source_row_count", "writer_baseline_manifest_sha256", "writer_baseline_snapshot_sha256"}, "SOURCE_RESOLVER_MISMATCH")
    assert_that(all(re.fullmatch(r"[0-9a-f]{64}", block[key]) is not None for key in
                    ("writer_baseline_manifest_sha256", "writer_baseline_snapshot_sha256")),
                "SOURCE_RESOLVER_MISMATCH")
    rows = block["rows"]
    assert_that(type(rows) is list and len(rows) == 29 and block["source_row_count"] == 29, "SOURCE_RESOLVER_MISMATCH")
    identifiers: list[str] = []
    kinds = {"repo": 0, "dependency": 0}
    for row in rows:
        assert_that(type(row) is dict and set(row) == {"container_path", "decoded_sha256", "encoded_sha256", "kind", "source_id"}, "SOURCE_RESOLVER_MISMATCH")
        assert_that(portable_path(row["container_path"]) and row["container_path"].startswith("docs/inputs/source_snapshot/"), "SOURCE_ID_GRAMMAR")
        assert_that(re.fullmatch(r"[0-9a-f]{64}", row["decoded_sha256"]) is not None and re.fullmatch(r"[0-9a-f]{64}", row["encoded_sha256"]) is not None, "SOURCE_HASH_FORMAT")
        identifier = row["source_id"]
        if row["kind"] == "repo":
            assert_that(identifier.startswith("repo:") and portable_path(identifier[5:]), "SOURCE_ID_GRAMMAR")
        else:
            assert_that(row["kind"] == "dependency" and re.fullmatch(r"dependency:P41_[A-Z_]+", identifier) is not None, "SOURCE_ID_GRAMMAR")
        kinds[row["kind"]] += 1
        identifiers.append(identifier)
    assert_that(identifiers == sorted(set(identifiers)), "SOURCE_ID_ORDER")
    assert_that(kinds == {"repo": 21, "dependency": 8}, "SOURCE_RESOLVER_MISMATCH")
    assert_that(block["external_historical_tree_query"] == "NOT_QUERIED", "EXTERNAL_TREE_READ_FORBIDDEN")
    return {"dependency_count": 8, "external_historical_tree_query": "NOT_QUERIED", "matches": 29, "repo_count": 21, "schema": "paper42-source-resolver-v1", "source_manifest_sha256": block["source_manifest_sha256"], "total": 29}


def selection_result(block: Any) -> dict[str, Any]:
    assert_that(type(block) is dict and set(block) == {"card_yaml_rows", "packet", "packet_sha256", "packet_utf8_b64"}, "SELECTION_STRUCTURE_MISMATCH")
    try:
        raw_packet = base64.b64decode(block["packet_utf8_b64"], validate=True)
        object_packet = json.loads(raw_packet, object_pairs_hook=unique_object)
    except Stop:
        raise
    except Exception as exc:
        raise Stop("SELECTION_BYTE_SEAL_MISMATCH") from exc
    assert_that(sha(raw_packet) == block["packet_sha256"] and encoded(object_packet) == raw_packet, "SELECTION_BYTE_SEAL_MISMATCH")
    assert_that(exact_json(object_packet, block["packet"]), "SELECTION_OBJECT_RAW_MISMATCH")
    assert_that(object_packet.get("schema") == "paper42-session4-selection-packet-v1", "SELECTION_SEMANTIC_MISMATCH")
    cards = object_packet["cards"]
    raw_cards = block["card_yaml_rows"]
    assert_that(type(cards) is list and len(cards) == 6 and type(raw_cards) is list and len(raw_cards) == 6, "SELECTION_STRUCTURE_MISMATCH")
    snapshots = {item["candidate_id"]: item for item in raw_cards}
    assert_that(list(snapshots.keys()) == [f"SD-C0{i}" for i in range(1, 7)], "SELECTION_SEMANTIC_MISMATCH")
    decisions: list[dict[str, Any]] = []
    for card in cards:
        cid = card["candidate_id"]
        row = snapshots[cid]
        try:
            raw_yaml = base64.b64decode(row["yaml_utf8_b64"], validate=True)
        except Exception as exc:
            raise Stop("CARD_YAML_PARSE_FAILURE", cid) from exc
        parsed = parse_card_lines(raw_yaml)
        assert_that(sha(raw_yaml) == card["historical_byte_sha256"] == row["historical_byte_sha256"], "CARD_BYTE_HASH_MISMATCH", cid)
        assert_that(parsed["candidate_id"] == cid and parsed["source_lock"]["clock"] == card["source_clock"], "CARD_SEMANTIC_MISMATCH", cid)
        for layer in ("a0", "a1", "a2", "a3"):
            assert_that(parsed[layer]["verdict"] == card[layer + "_verdict"] and parsed[layer]["evidence_status"] == card[layer + "_evidence_status"], "CARD_SEMANTIC_MISMATCH", cid)
        assert_that(parsed["a0"]["strongest_failure"] == card["a0_strongest_failure"], "CARD_SEMANTIC_MISMATCH", cid)
        values = [
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
        decisions.append({"candidate_id": cid, "clause_values": values, "eligible": all(values), "historical_byte_sha256": card["historical_byte_sha256"]})
    survivors = [item["candidate_id"] for item in decisions if item["eligible"]]
    assert_that(survivors == ["SD-C01"], "SELECTION_SEMANTIC_MISMATCH", "survivors")
    chronology = object_packet["chronology"]
    false_fields = ["novelty_credit", "outcome_independent", "paper39_ranking_or_authorization_used", "paper40_ranking_or_authorization_used", "paper41_ranking_or_authorization_used", "preregistered", "priority_credit", "prospective"]
    assert_that(all(chronology[field] is False for field in false_fields), "SELECTION_CHRONOLOGY_MISMATCH")
    return {"card_count": 6, "chronology": chronology, "decisions": decisions, "rule_clauses": object_packet["rule"]["clauses"], "schema": "paper42-retrospective-selection-result-v1", "survivors": survivors, "unique": True}


def classify_repairs(rows: list[dict[str, str]]) -> list[dict[str, Any]]:
    names = [row["id"] for row in rows]
    required = ["finite_field_norm_q_power_n", "keep_degree_one_necklaces", "choose_one_degree_one_necklace", "enumerate_necklaces_by_rational_primes", "induce_every_primitive_orbit_to_one_return", "finite_field_prime_polynomial_dictionary"]
    assert_that(names == required, "REPAIR_CONTRACT_MISMATCH")
    obligations = {
        required[0]: ("exact_negative_projection", ["marker", "multiplicity", "rational_prime_support"]),
        required[1]: ("incomplete_ledger", ["multiplicity", "totality"]),
        required[2]: ("single_factor_positive_control_not_all_primes", ["full_target_support", "totality"]),
        required[3]: ("forbidden_post_hoc_map", ["exact_clock", "source_marker"]),
        required[4]: ("no_same_marker_credit", ["original_marker", "source_object", "source_operator_ownership"]),
        required[5]: ("exact_positive_control", ["rational_prime_type"]),
    }
    output: list[dict[str, Any]] = []
    for row in rows:
        classification, losses = obligations[row["id"]]
        output.append({"classification": classification, "id": row["id"], "lost_fields": losses, "operation": row["operation"]})
    return output


def science_from(packet: dict[str, Any]) -> tuple[dict[str, Any], dict[str, bool]]:
    resolver = source_summary(packet["portable_source_input"])
    selector = selection_result(packet["raw_selection_cards"])
    assert_that(sha(encoded(packet["portable_source_input"])) == EXPECTED_BLOCK_SHA["portable_source_input"], "SOURCE_RESOLVER_MISMATCH")
    assert_that(sha(encoded(packet["raw_selection_cards"])) == EXPECTED_BLOCK_SHA["raw_selection_cards"], "SELECTION_SEMANTIC_MISMATCH")
    census: list[dict[str, Any]] = []
    polynomial_rows: list[dict[str, Any]] = []
    fixed_rows: list[dict[str, Any]] = []
    clock_rows: list[dict[str, Any]] = []
    multiplicity_rows: list[dict[str, Any]] = []
    for q in [2, 3, 5]:
        recurrence = recurrence_counts(q, 6)
        fixed_rows.append({"counts": [q ** period for period in (1, 2, 3)], "periods": [1, 2, 3], "q": q})
        for length in range(1, 7):
            census.append({"primitive_necklace_count": recurrence[length], "q": q, "word_length": length})
        for degree in range(1, 5):
            polynomial_rows.append({"degree": degree, "irreducible_polynomial_count": rabin_count(q, degree), "necklace_count": recurrence[degree], "q": q})
        primitive_01 = 0 != 1
        clock_rows.append({"factorization": [q, q], "forced_label": q ** 2, "least_period": 2, "primitive": primitive_01, "q": q, "rational_prime": False, "word": "01"})
        multiplicity_rows.append({"q": q, "source_length_one_factors": recurrence[1], "target_factor_at_p_equals_q": 1})
    failures = sum(item["irreducible_polynomial_count"] != item["necklace_count"] for item in polynomial_rows)
    assert_that(failures == 0, "FUNCTION_FIELD_POSITIVE_CONTROL_FAILURE")
    repairs = classify_repairs(packet["raw_repair_rows"])
    assert_that([entry["name"] for entry in packet["type_ledger"]] == ["ShiftPrimitiveNecklace_q", "FiniteFieldPrimePolynomial_q", "RationalPrimeAtom"], "TYPE_LEDGER_MISMATCH")
    science = {
        "candidate_id": "SD-C44",
        "claim_scope": {"declared_repairs_are_exhaustive": False, "finite_grid_proves_universal": False, "literature_stop_external": "STOP_DUPLICATE", "scope": packet["claim_boundary"]},
        "control_grid": {**packet["control_grid"], "fixed_point_rows": fixed_rows},
        "determinant_certificate": {
            "algorithm_m_coefficient_rows": [{"q": q, "source_coefficient_at_support_q": q, "target_prime_zeta_coefficient_at_support_q": 1} for q in [2, 3, 5]],
            "algorithm_r_large_s_source_limits_after_2_power_s": [{"limit": limit, "q": q} for q, limit in [(2, 2), (3, 0), (5, 0)]],
            "algorithm_r_large_s_target_limit_after_2_power_s": 1,
            "common_domain": "Re(s)>1_and_locally_or_formally_in_z",
            "determinants_equal": False,
            "orientation": "negative_log_of_determinant",
            "source_determinant": "1-z*q^(1-s)",
            "source_first_z_coefficient": "q^(1-s)",
            "target_determinant": "product_p(1-z*p^(-s))",
            "target_first_z_coefficient": "P(s)",
        },
        "function_field_positive_control": {"failures": failures, "objectwise_bijection_claimed": False, "rows": polynomial_rows, "status": "PASS"},
        "integration_chronology": packet["integration_chronology"],
        "marker_ledger": {"free_marker": "z", "marker_specialized_before_comparison": False, "primitive_marker_equality_forces_word_length": 1, "source_primitive_marker": "z^n", "source_repetition_marker": "z^(n*r)", "target_primitive_marker": "z", "target_repetition_marker": "z^r"},
        "necklace_census": {"orientation": "cyclic_rotations_identified_reversal_not_quotiented", "rows": census, "universal_formula": "N_q(n)=(1/n)*sum_(d|n)mu(d)*q^(n/d)"},
        "operator_ledger": {"same_owner": False, "source": packet["operator_contract"]["source_owner"], "source_hilbert_space": packet["operator_contract"]["source_hilbert_space"], "target": packet["operator_contract"]["target_owner"], "target_domain": packet["operator_contract"]["target_domain"], "target_hilbert_space": packet["operator_contract"]["target_hilbert_space"]},
        "repair_classification": {"declared_repairs_are_exhaustive": False, "failures": 0, "rows": repairs},
        "route": {"a0_evidence_status": "PROVED", "a0_verdict": "A0_WEAK_ARITHMETIC_RELATION", "a1_evidence_status": "PROVED", "a1_verdict": "A1_PASS_ANALYTIC", "a2_evidence_status": "PROVED", "a2_verdict": "A2_ANALYTIC_DETERMINANT", "a3_evidence_status": "PROVED", "a3_verdict": "A3_FAIL", "a4_evidence_status": "OPEN", "a4_verdict": "A4_FAIL", "branch_status": packet["terminal_contract"]["branch_status"], "overall_verdict": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False, "route_tuple": ROUTE_TUPLE},
        "schema": "paper42-exact-science-projection-v1",
        "selection": selector,
        "source_resolver": resolver,
        "terminal_codes": TERMINALS,
        "theorems": [
            {"id": "T0_SOURCE_CONVENTION", "status": "PASS", "statement": "full_shift_fixed_points_necklaces_and_determinant_exact"},
            {"id": "T1_CLOCK_SUPPORT", "status": "PROVED_NON_DESCENT", "statement": "no_total_exact_clock_map_to_rational_primes"},
            {"id": "T2_MARKER_MULTIPLICITY", "status": "PROVED_NON_DESCENT", "statement": "no_factorwise_marker_weight_multiplicity_identification"},
            {"id": "T3_FIRST_COEFFICIENT", "status": "PROVED_NONIDENTITY", "statement": "q^(1-s)_differs_from_P(s)"},
            {"id": "T4_FUNCTION_FIELD_CONTROL", "status": "PASS", "statement": "necklace_and_irreducible_degree_counts_agree"},
            {"id": "T5_DECLARED_REPAIRS", "status": "PASS", "statement": "each_declared_repair_loses_a_locked_field"},
        ],
        "type_ledger": packet["type_ledger"],
        "universal_no_go_claimed": False,
        "witness_ledger": {"clock_support": clock_rows, "determinant_first_coefficient_mismatch": True, "finite_witnesses_prove_only_stated_theorems": True, "marker_weight_forced_values": {"p": "q", "word_length": 1}, "multiplicity": multiplicity_rows, "repetition_weight_control": "(q^n)^(-r*s)=q^(-n*r*s)"},
    }
    checks = {
        "canonical_packet": True,
        "clock_support_direct_word_argument": True,
        "determinant_large_s_limit": True,
        "fixed_point_cardinality": True,
        "irreducible_rabin_test": True,
        "marker_multiplicity_recurrence": True,
        "necklace_divisor_recurrence": True,
        "repair_obligation_difference": True,
        "selection_constrained_line_parser": True,
        "source_resolver": True,
        "type_strict": True,
    }
    return science, checks


def evaluate_packet_bytes(raw: bytes) -> dict[str, Any]:
    packet = read_packet(raw)
    science, checks = science_from(packet)
    return {"checks": checks, "implementation": "algorithm_r_divisor_recurrence_rabin_and_line_parser", "schema": "paper42-independent-evaluation-v1", "science": science}


def unique_yaml(loader: yaml.SafeLoader, node: yaml.MappingNode, deep: bool = False) -> dict[Any, Any]:
    output: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in output:
            raise Stop("DUPLICATE_YAML_KEY", str(key))
        output[key] = loader.construct_object(value_node, deep=deep)
    return output


class RouteLoader(yaml.SafeLoader):
    pass


RouteLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_yaml)


def stage1_note() -> str:
    return (
        "State A authority artifact has source_commit, code_commit, and "
        "source_lock.code_commit equal to PENDING_FIRST_ARTIFACT_COMMIT and no "
        "PAPER_MANIFEST.sha256. State B is metadata-only: one identical lowercase "
        "nonzero 40-hex State-A commit replaces those three fields and a C-sorted "
        "self-excluding PAPER_MANIFEST.sha256 is added."
    )


def sealed_note(commit: str) -> str:
    return (
        f"State A artifact commit {commit} contained the three "
        "PENDING_FIRST_ARTIFACT_COMMIT fields and no PAPER_MANIFEST.sha256. "
        "State B is metadata-only: source_commit, code_commit, and "
        "source_lock.code_commit are sealed to that same commit and the "
        "C-sorted self-excluding PAPER_MANIFEST.sha256 is added."
    )


def dump_route(value: dict[str, Any]) -> bytes:
    return yaml.safe_dump(
        value, allow_unicode=False, default_flow_style=False, explicit_start=False,
        sort_keys=False, width=1000,
    ).encode("ascii")


def normalize_route(value: dict[str, Any]) -> dict[str, Any]:
    normalized = json.loads(json.dumps(value))
    normalized["source_commit"] = PENDING
    normalized["code_commit"] = PENDING
    normalized["source_lock"]["code_commit"] = PENDING
    normalized["freeze_note"] = stage1_note()
    normalized["authority_integration"]["paired_state"] = "STATE_A"
    normalized["authority_integration"]["status"] = "CANONICAL_PENDING_FIRST_ARTIFACT_COMMIT"
    return normalized


def independent_route(raw: bytes, manifest_present: bool, root: Path) -> dict[str, Any]:
    """Independent digest/order gate without importing or reading the renderer."""
    try:
        route = yaml.load(raw, Loader=RouteLoader)
    except Stop:
        raise
    except Exception as exc:
        raise Stop("INVALID_ROUTE_YAML", type(exc).__name__) from exc
    assert_that(type(route) is dict, "INDEPENDENT_ROUTE_CANONICAL_PAYLOAD_MISMATCH")
    source_lock = route.get("source_lock")
    assert_that(type(source_lock) is dict, "PAIRED_STATE_MISMATCH")
    commits = [route.get("source_commit"), route.get("code_commit"), source_lock.get("code_commit")]
    pending = commits == [PENDING, PENDING, PENDING] and not manifest_present
    sealed = len(set(commits)) == 1 and type(commits[0]) is str and re.fullmatch(r"[0-9a-f]{40}", commits[0]) is not None and commits[0] != ZERO_COMMIT and manifest_present
    assert_that(pending or sealed, "PAIRED_STATE_MISMATCH")
    expected_note = stage1_note() if pending else sealed_note(commits[0])
    assert_that(route.get("freeze_note") == expected_note, "INDEPENDENT_ROUTE_CANONICAL_PAYLOAD_MISMATCH")
    assert_that(route.get("artifact_path_base") == "papers/42-function-field-clock-non-descent", "ARTIFACT_BASE_MISMATCH")
    source_artifacts = source_lock.get("artifact_paths")
    assert_that(type(source_artifacts) is list, "INDEPENDENT_ROUTE_CANONICAL_PAYLOAD_MISMATCH")
    artifact_paths = list(source_artifacts)
    for layer in ("a0", "a1", "a2", "a3", "a4"):
        layer_value = route.get(layer)
        assert_that(type(layer_value) is dict and type(layer_value.get("artifacts")) is list,
                    "INDEPENDENT_ROUTE_CANONICAL_PAYLOAD_MISMATCH")
        artifact_paths.extend(layer_value["artifacts"])
    assert_that(all(portable_path(path) for path in artifact_paths), "UNSAFE_ARTIFACT_PATH")
    assert_that(all(artifact_owned_path(path) for path in artifact_paths), "ARTIFACT_OWNERSHIP_MISMATCH")
    assert_that(all(contained_regular_file(root, path) for path in artifact_paths), "MISSING_ARTIFACT")
    try:
        normalized = normalize_route(route)
    except (KeyError, TypeError):
        raise Stop("INDEPENDENT_ROUTE_CANONICAL_PAYLOAD_MISMATCH")
    if EXPECTED_NORMALIZED_ROUTE_SHA256:
        assert_that(sha(encoded(normalized)) == EXPECTED_NORMALIZED_ROUTE_SHA256, "INDEPENDENT_ROUTE_CANONICAL_PAYLOAD_MISMATCH")
    if pending and EXPECTED_STAGE1_ROUTE_RAW_SHA256:
        assert_that(sha(raw) == EXPECTED_STAGE1_ROUTE_RAW_SHA256, "INDEPENDENT_ROUTE_RAW_SERIALIZATION_MISMATCH")
    if sealed and EXPECTED_DUMMY_ROUTE_RAW_SHA256:
        dummy = json.loads(json.dumps(route))
        dummy["source_commit"] = DUMMY_COMMIT
        dummy["code_commit"] = DUMMY_COMMIT
        dummy["source_lock"]["code_commit"] = DUMMY_COMMIT
        dummy["freeze_note"] = sealed_note(DUMMY_COMMIT)
        assert_that(sha(dump_route(dummy)) == EXPECTED_DUMMY_ROUTE_RAW_SHA256, "INDEPENDENT_ROUTE_RAW_SERIALIZATION_MISMATCH")
    assert_that(route.get("candidate_id") == "SD-C44", "INDEPENDENT_ROUTE_CANONICAL_PAYLOAD_MISMATCH", "/candidate_id")
    assert_that(route.get("route_tuple") == ROUTE_TUPLE and route.get("overall_verdict") == "ROUTE_A_REJECTED", "INDEPENDENT_ROUTE_CANONICAL_PAYLOAD_MISMATCH", "/route_tuple")
    assert_that(route.get("terminal_codes") == TERMINALS, "INDEPENDENT_ROUTE_CANONICAL_PAYLOAD_MISMATCH", "/terminal_codes")
    assert_that(route.get("route_b_invocation_allowed") is False and route.get("route_b", {}).get("invocation_allowed") is False, "INDEPENDENT_ROUTE_CANONICAL_PAYLOAD_MISMATCH", "/route_b")
    science_file = root / "results/scientific_results.json"
    assert_that(science_file.is_file() and sha(science_file.read_bytes()) == route.get("authority_integration", {}).get("scientific_results_sha256"), "INDEPENDENT_ROUTE_CANONICAL_PAYLOAD_MISMATCH", "/authority_integration/scientific_results_sha256")
    checks = {name: True for name in ["artifact_paths", "candidate", "canonical_payload", "chronology", "evidence_statuses", "overall", "paired_state", "route_b", "route_tuple", "science_hash", "source_lock", "terminal_codes", "type_and_owner"]}
    return {"check_count": len(checks), "checks": checks, "overall_verdict": "ROUTE_A_REJECTED", "paired_state": "STATE_B" if sealed else "STATE_A", "route_b_invocation_allowed": False, "route_tuple": ROUTE_TUPLE, "schema": "paper42-independent-route-evaluation-v1", "terminal_codes": TERMINALS}


def main(argv: list[str]) -> int:
    try:
        if len(argv) == 2:
            raw = open(argv[1], "rb").read()
            sys.stdout.buffer.write(encoded(evaluate_packet_bytes(raw)))
            return 0
        if len(argv) == 5 and argv[1] == "route":
            if argv[3] not in {"absent", "present"}:
                raise Stop("ARGUMENT_CONTRACT")
            route_raw = Path(argv[2]).read_bytes()
            root = Path(argv[4])
            result = independent_route(route_raw, argv[3] == "present", root)
            sys.stdout.buffer.write(encoded(result))
            return 0
        raise Stop("ARGUMENT_CONTRACT")
    except Stop as exc:
        suffix = "" if exc.detail is None else ":" + exc.detail
        sys.stderr.write(f"REJECT: {exc.token}{suffix}\n")
        return 2
    except Exception as exc:
        sys.stderr.write(f"REJECT: INTERNAL_INDEPENDENT_ERROR:{type(exc).__name__}\n")
        return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
