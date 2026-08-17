#!/usr/bin/env python3
"""Direct exact evaluator for the raw SD-C42 authority packet.

The evaluator reads packet bytes only. It does not import the source module or
execute any vendored producer or replay program.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from decimal import Decimal, localcontext
from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
import math
from pathlib import Path
import sys
from typing import Any, Iterable

import yaml


RESEARCH_LOCK_SHA256 = "530f8a989d1e0f29e4ca51342d121a4e358d60692e659b18d136b9236e95c55e"
RESEARCH_POINTER_SHA256 = "e985b438395225f454fc60e6e913e1e2b6f1fd6781c24bb3f703778e415fb4e5"
PREREG_SHA256 = "f1643899ea7ac62e916b24fc265a4ee2ce1d042e2e078d7b336662ab2a065908"
PLAN_SHA256 = "dbae7e5317bea10e623f957ee75389392de7cfd8d55b17965ce710ff78364b2d"
CONTROL_LOCK_SHA256 = "f19edfa13b4f4cd9511394563fc2d7f7d9c428e477ae39e1d248a821e86850d8"
ROUTE_SCHEMA_FIXTURE_SHA256 = "15e47752d6134ec7ddc8f36329a3f7139031122ead7a90af6b876840c1ac5bfa"
ROUTE_SKILL_SHA256 = "29bd6275aa0c80ecce9cca898f06687208475c0a9a40cf3b9592fde45951458a"
RESEARCH_FILES = {
    "COUNTEREXAMPLES.md": "b86a431c61ed11c409090c81bbb6660f16343cc9ee1ecbadd902e92d86b8fb5f",
    "DERIVATION_PACKAGE.md": "7f1f80637b8dbadf95461245419529180243faec08637e306b79da76389229ea",
    "LITERATURE_BOUNDARY_ADDENDUM.md": "fb2cdae0e4b1aa662a3426d7d569a926d94b5bf7b2b36b5de0e8bc77f6ffb9fb",
    "LITERATURE_NOVELTY_AUDIT.md": "79982d110318ca29a9f579d8498a4b110da742450f6e0011f2164067ac20a3e8",
    "MAYER_SOURCE_BOUNDARY.md": "a9dcbc922f8c47b0b845e7c6e76422aad3a0e744940a6529c2172176f5725bc5",
    "OBJECT_OWNERSHIP.md": "7cda0257d99547b8dd28f8c7e5fc0c315e34fcb0e2724f10d75a40dfd3553e7f",
    "PRIMITIVITY_TYPE_FIREWALL.md": "5280a3ef22fcfef0078ed4e162246aa6cc516135aece0a53f78ce8fad2ca18a8",
    "PROOF_PACKAGE.md": "9ae5b6220ba1fde93b4592e6ec1b1dd78289248f376b7ef395b96dc815e9aa8e",
    "ROUTE_STATUS_AUDIT.md": "4fb51559b79420f5515698b0f3b069d94c46736c9ef8e4f999041f2ed81a3c07",
    "SELECTION_AUDIT.md": "0739263b6da1795bfa693ba2600e92a87fd973d9af08398d505a8fa4afa3190c",
    "SOURCE_LOCK.md": "2269e06576dd20c513c5ca9482cb49d36678e07358aaf80f2f08b33806b87041",
}
DEPENDENT_SEALS = {
    "claim_boundary": "168c29620445002fdf0bdf9c49bd7792414fe5ef378c80615b115646db9214cb",
    "literature_audit": "79982d110318ca29a9f579d8498a4b110da742450f6e0011f2164067ac20a3e8",
    "literature_manifest": "28e2f95750b5ba4e76cf2e174eba9d9bc318e8b57c4c26345c9c6f14cc4d65ce",
    "outer_manifest": "5a258c18495056ce6ed9ec0bed4778ea1c5a548f7d8cf8592145a817aa904ee2",
    "independent_da": "f9e5f8c7b8cdc07aeeea18d48927fd7e07ac1da82dbef3c3daa10b102a9e2a7e",
}
KNOWN_OUTPUT_HASHES = {
    "control_reference": "d0be9630e4f0710c1f602e14e517939f6eef21c582934d79f795a9871f45a30f",
    "control_independent": "729287849f36046b8aa21d8dba615650f4289dd1d3202c1783cc41af207c4d92",
    "prototype_reference": "2fee7701a08ec4f7e019863c6e86bf6fb884bf0323e5593e4bf946ef35e7a995",
    "prototype_independent": "78a1846b19cffde3c21642e6220b893a82690adaee5314ff6be2b19e7265fe38",
}
SEEDS = {
    "a0_composites": 42003,
    "a0_matched_density": 42002,
    "a0_pseudoprimes": 42004,
    "a0_randomized_labels": 42005,
    "a0_shuffled_primes": 42001,
    "a1_random_phases": 42103,
    "a1_random_weights": 42102,
    "a1_same_density_lengths": 42104,
    "a1_shuffled_periods": 42101,
}
CARD_HASHES = {
    "SD-C01": "ee47a9c90c6bfbc54ba6b09b21f416dcece58b0d0ba9a391ca196d1b41d365a2",
    "SD-C02": "5b5e9a2fe33a0ba8d281cf59c8f5346b95033c655d258554c0f76f8cfa0a434f",
    "SD-C03": "2263b1c7bac4336628f444ded88e4e2ad98117f430113faf1ea5a91c16380328",
    "SD-C04": "0609076081ccd69e9ffa3e0f708d426a33f7d41e2884f90bb2792bbc90209a92",
    "SD-C05": "4a18295b1e20245c7196f21be4e4afc52857bf981efb461556720ab9e8ab5ed1",
    "SD-C06": "d93683662a0cbee8e07d79329477d8b60bb273fb72e4bd64c05847e09a576c1b",
}
ROUTE_TUPLE = {
    "A0": "A0_WEAK_ARITHMETIC_RELATION",
    "A1": "A1_PASS_ANALYTIC",
    "A2": "A2_ANALYTIC_DETERMINANT",
    "A3": "A3_PARTIAL_ANALYTIC_STRUCTURE",
    "A4": "A4_FORMAL_HINT",
}
TERMINALS = [
    "GO_MODULAR_PRIMITIVE_LEDGER",
    "GO_SAME_OBJECT_MAYER_DETERMINANT",
    "STOP_CANONICAL_INTEGER_PROJECTION",
    "STOP_RATIONAL_INTEGER_CLOCK_REPETITION_CONJUNCTION",
    "STOP_OPERATOR_VISIBLE_SELECTOR_NOT_OWNED",
    "ROUTE_A_REJECTED",
]
COLLISION_WITNESSES = {
    "W1": (((1, 2),), ((2, 1),), "TRACE4_REVERSAL"),
    "W2": (((1, 4),), ((2, 2),), "TRACE6_NONREVERSAL"),
    "W3": (((2, 4),), ((1, 1), (1, 2)), "TRACE10_CROSS_LENGTH_NONREVERSAL"),
}
INVENTORY_RECORD_HASHES = {
    "canonical_D2_k1": "5b68fcfe10854565eec66c5054d5ca8ae6f03ec2dd5822cb9d3beb06f4fce08d",
    "canonical_D2_k2": "84b895f73a1c356fa28b3e0a27f12589d691766c9505e5ae368e841c1eaa95e9",
    "canonical_D2_k3": "81b3f57c61538afe7dd9a243e6b3308ab1b0286e69495dba78c0d462ed27e3e9",
    "canonical_D2_k4": "04b6ed8d9661e5ddff8fc0cd17282b11d0acdab9e808414f221fe29eabc27d3b",
    "canonical_D3_k1": "a930517a62bd5ae7d0e789cacdbc7f053fc4d2cf580ca0421a0285aed036eccf",
    "canonical_D3_k2": "fd1556ee71a656a42e3e9ce1b06e07f04a93c59a4a4dfe136219f18557f63f7c",
    "canonical_D3_k3": "c1241202af08be224c5be501a58151b6b09938cf851f1a84f77fc8a2632a7d90",
    "canonical_D3_k4": "f337f003759ccd8cf34ce26fd4760b91f6edb5d0d080c3d2831202ceabc49633",
    "canonical_D4_k1": "62c185bfc8796bff9f01864ae30872230046014c557ad6b8047f8fd7913417fe",
    "canonical_D4_k2": "b6d05c491cf99fe4684b16119f94e49b90e08126f9414a9ff359c851becef442",
    "canonical_D4_k3": "96093e71c2e74ca19e615230d65d6f570ad02c54e7a68895dc4481230ac2e2aa",
    "canonical_D4_k4": "f2a53ade82fc99885351743639da43adab11883ce0cd893ba47bc7374bfbc17d",
    "neighboring_D2_k1": "cdbde09955fea21c305215afa01ed2c76d0b2f22a639581d829a6eae1995e42f",
    "neighboring_D2_k2": "9c5b2582d0499c6d6a2ae15f74bc2f2f0e938e8a4d7f45d97fe53d6c006a942a",
    "neighboring_D2_k3": "63f502b6201d1fe793e17d2df4806362ba9e6f78c20fa3acc5d347d4b592449d",
    "neighboring_D2_k4": "9a6514b9a0f6a6ef51b870c7d1fe6c08fd5573e0a2206c3eb8d36f23908de2aa",
    "neighboring_D3_k1": "f326b0e3a039ba78902571427c9b988dd6cb5f6cc7a2da013d7d5f631035cff6",
    "neighboring_D3_k2": "dfcf7dd883861f5b052e12176da4dfe2242609815f5304895b2b156c6364c599",
    "neighboring_D3_k3": "46e946962ad8f7d323815712383d2021b77c8825a5414331d4be0789da98bb19",
    "neighboring_D3_k4": "f58c5bfe2de3bbd4849bcfa0aeb6bba48892cef6d893e12aca77048cc8834b71",
    "neighboring_D4_k1": "2309dd94db8ac7d2d4ebc186b834a7aee56629de1c33da63fda53267f0409d3f",
    "neighboring_D4_k2": "a0caa16c4aa7f1d40dd971ae9be8173c39becbdeb40a322766b8ca2f6f40f8dd",
    "neighboring_D4_k3": "38c28b2531f2b7a52301ef482fa88aa8cc6b9741ddb183d06b3f7675046291a4",
    "neighboring_D4_k4": "fa304a6931b866a54d66cc7026409f4fe29656857b9819de3b946412a55919a0",
}

Matrix = tuple[int, int, int, int]
PairWord = tuple[tuple[int, int], ...]
IDENTITY: Matrix = (1, 0, 0, 1)


def canonical_bytes(value: Any) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode("ascii")


def fragment_digest(value: Any) -> str:
    raw = (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True) + "\n").encode("ascii")
    return sha256(raw).hexdigest()


def rotations(word: tuple[Any, ...]) -> tuple[tuple[Any, ...], ...]:
    return tuple(word[index:] + word[:index] for index in range(len(word)))


def canonical_rotation(word: tuple[Any, ...]) -> tuple[Any, ...]:
    return min(rotations(word))


def is_primitive(word: tuple[Any, ...]) -> bool:
    for period in range(1, len(word)):
        if len(word) % period == 0 and word == word[:period] * (len(word) // period):
            return False
    return True


def enumerate_necklaces(digits: tuple[int, ...], length: int) -> list[PairWord]:
    alphabet = tuple(product(digits, repeat=2))
    return [
        tuple(candidate)
        for candidate in product(alphabet, repeat=length)
        if is_primitive(tuple(candidate)) and tuple(candidate) == canonical_rotation(tuple(candidate))
    ]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    a, b, c, d = left
    e, f, g, h = right
    return (a * e + b * g, a * f + b * h, c * e + d * g, c * f + d * h)


def matpow(matrix: Matrix, exponent: int) -> Matrix:
    result = IDENTITY
    base = matrix
    power = exponent
    while power:
        if power & 1:
            result = matmul(result, base)
        base = matmul(base, base)
        power //= 2
    return result


def digit_matrix(digit: int) -> Matrix:
    return (digit, 1, 1, 0)


def branch_matrix(digit: int) -> Matrix:
    return (0, 1, 1, digit)


def word_matrix(word: PairWord) -> Matrix:
    result = IDENTITY
    for left, right in word:
        result = matmul(result, matmul(digit_matrix(left), digit_matrix(right)))
    return result


def branch_word_matrix(digits: tuple[int, ...]) -> Matrix:
    result = IDENTITY
    for digit in digits:
        result = matmul(result, branch_matrix(digit))
    return result


def determinant(matrix: Matrix) -> int:
    return matrix[0] * matrix[3] - matrix[1] * matrix[2]


def trace(matrix: Matrix) -> int:
    return matrix[0] + matrix[3]


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def reverse_pair_word(word: PairWord) -> PairWord:
    return tuple((right, left) for left, right in reversed(word))


def word_id(word: PairWord) -> str:
    return "|".join(f"{left},{right}" for left, right in word)


def lcg(seed: int, count: int) -> list[int]:
    state = seed % (2**31)
    output = []
    for _ in range(count):
        state = (1103515245 * state + 12345) % (2**31)
        output.append(state)
    return output


def fisher_yates(values: list[Any], raw: list[int]) -> list[Any]:
    output = list(values)
    cursor = 0
    for index in range(len(output) - 1, 0, -1):
        target = raw[cursor] % (index + 1)
        cursor += 1
        output[index], output[target] = output[target], output[index]
    if len(output) > 1 and output == values:
        output = output[1:] + output[:1]
    return output


def first_primes(count: int) -> list[int]:
    values = []
    candidate = 2
    while len(values) < count:
        if is_prime(candidate):
            values.append(candidate)
        candidate += 1
    return values


def first_base2_pseudoprimes(count: int) -> list[int]:
    values = []
    candidate = 3
    while len(values) < count:
        if not is_prime(candidate) and pow(2, candidate - 1, candidate) == 1:
            values.append(candidate)
        candidate += 2
    return values


def generated_by_primality(raw: list[int], count: int, want_prime: bool) -> list[int]:
    output: list[int] = []
    seen: set[int] = set()
    for state in raw:
        value = 2 + state % 9991
        if value not in seen and is_prime(value) is want_prime:
            seen.add(value)
            output.append(value)
            if len(output) == count:
                return output
    return output


def roof_string(tr: int) -> str:
    with localcontext() as context:
        context.prec = 70
        delta = Decimal(tr * tr - 4)
        lam = (Decimal(tr) + delta.sqrt()) / Decimal(2)
        return format(Decimal(2) * lam.ln(), ".60f")


def _path(mapping: dict[str, Any], dotted: str) -> Any:
    value: Any = mapping
    for key in dotted.split("."):
        value = value[key]
    return value


def _keys(value: Any, expected: set[str]) -> bool:
    return isinstance(value, dict) and set(value) == expected


def _strict_int(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def _list_of_strings(value: Any) -> bool:
    return isinstance(value, list) and all(isinstance(item, str) for item in value)


def validate_packet_shape(packet: Any) -> dict[str, bool]:
    top_keys = {
        "candidate_id", "chronology_input", "claim_scope_input",
        "experiment_freeze_input", "mayer_source_input", "ownership_input",
        "projection_criterion_schema", "projection_definition_input",
        "prototype_reproduction_input", "raw_branch_input", "raw_collision_input",
        "raw_control_input", "raw_primitive_inventories", "raw_type_input",
        "research_input", "route_card_bytes", "route_schema_input", "row_contract_input", "schema",
        "selection_rule_schema",
    }
    checks: dict[str, bool] = {"shape_top_level_exact": _keys(packet, top_keys)}
    if not checks["shape_top_level_exact"]:
        return checks
    keysets = {
        "chronology_input": {"authority_checker_inputs_precede_authority_run", "canonical_prototype_outputs_known", "classification", "control_lock_precedes_clean_replacement_rerun", "prospective_credit_allowed", "research_renderings_postdate_canonical_run", "v1_and_inflight_smoke_outputs_known"},
        "claim_scope_input": {"forbidden_claim_tokens", "scope_label"},
        "experiment_freeze_input": {"expected_plan_sha256", "expected_preregistration_sha256", "plan_path", "plan_sha256", "preregistration_path", "preregistration_sha256"},
        "mayer_source_input": {"continuation_domain", "determinant_half_plane", "disk_center_radius", "euler_product_initial_half_plane", "function_space_symbol", "local_u_domain", "selberg_identity_u_value", "source_log_coefficient_tokens", "target_log_coefficient_tokens"},
        "ownership_input": {"declared_object_symbols", "declared_untwisted_selector_symbols", "ownership_scope", "positive_control_owner", "scalar_postselection"},
        "projection_criterion_schema": {"clock_marker_exponent_rule", "criterion_ids", "derivative_root_selector", "norm_minimal_polynomial_template", "norm_root_selector", "repetition_exponents"},
        "prototype_reproduction_input": {"control_lock_path", "control_lock_sha256", "expected_control_lock_sha256", "known_output_hash_targets", "vendor_root"},
        "raw_branch_input": {"evaluation_point", "matrix_templates", "raw_operator_nesting", "stored_digits", "weight_exponent_s"},
        "raw_control_input": {"a0_family_ids", "a1_family_ids", "control_digits", "control_pair_lengths", "generator", "lcg_sequences", "neighboring_control_digits", "prototype_alphabet_sizes", "prototype_pair_lengths", "seeds"},
        "raw_type_input": {"digit_shift_symbol", "digit_space_symbol", "grouping_block_size", "grouping_symbol", "pair_shift_symbol", "pair_space_symbol", "paper40_new_symbol", "parent_supplied_symbols", "return_map_digit_fixture", "reversal_pair_fixture", "type_symbols"},
        "research_input": {"dependent_seal_hashes", "expected_immutable_file_hashes", "expected_manifest_sha256", "expected_pointer_sha256", "immutable_file_hashes", "manifest_path", "manifest_sha256", "pointer_path", "pointer_sha256"},
        "route_schema_input": {"candidate_id", "criterion_order", "evaluation_date", "expected_schema_fixture_sha256", "expected_skill_byte_sha256", "paired_provenance_fields", "required_a0_control_count", "required_a1_control_count", "schema_fixture", "schema_fixture_path", "schema_fixture_sha256", "skill", "skill_artifact_encoding", "skill_artifact_path", "skill_byte_sha256", "skill_utf8", "skill_version", "target_root_metric_keys"},
        "row_contract_input": {"orientation_equivalence", "phase_exponent", "phase_modulus", "reversal_metadata_fields", "reverse_quotient_rule", "source_multiplicity", "stability_denominator_token", "untwisted_sign"},
        "selection_rule_schema": {"card_ids", "forbidden_predicates", "nonempty_intrinsic_ledger_rule", "same_object_determinant_rule", "tie_break_order"},
    }
    for name, expected in keysets.items():
        checks[f"shape_{name}_keys"] = _keys(packet[name], expected)
    checks["shape_route_card_list"] = isinstance(packet["route_card_bytes"], list) and all(
        _keys(item, {"card_id", "historical_byte_sha256", "raw_yaml_utf8", "relative_path", "vendored_byte_sha256"})
        and all(isinstance(item[key], str) for key in item)
        for item in packet["route_card_bytes"]
    )
    checks["shape_projection_definition_list"] = isinstance(packet["projection_definition_input"], list) and all(
        _keys(item, {"definition", "projection_id"}) and all(isinstance(item[key], str) for key in item)
        for item in packet["projection_definition_input"]
    )
    checks["shape_collision_list"] = isinstance(packet["raw_collision_input"], list) and all(
        _keys(item, {"left_word", "right_word", "witness_id"})
        and isinstance(item["witness_id"], str)
        and all(isinstance(word, list) and word and all(isinstance(pair, list) and len(pair) == 2 and all(_strict_int(value) for value in pair) for pair in word) for word in (item["left_word"], item["right_word"]))
        for item in packet["raw_collision_input"]
    )
    inventories = packet["raw_primitive_inventories"]
    checks["shape_inventory_list"] = isinstance(inventories, list) and all(
        _keys(item, {"alphabet_size", "digits", "family", "pair_length", "raw_words", "run_id"})
        and isinstance(item["family"], str) and isinstance(item["run_id"], str)
        and _strict_int(item["alphabet_size"]) and _strict_int(item["pair_length"])
        and isinstance(item["digits"], list) and all(_strict_int(value) for value in item["digits"])
        and isinstance(item["raw_words"], list)
        and all(isinstance(word, list) and all(isinstance(pair, list) and len(pair) == 2 and all(_strict_int(value) for value in pair) for pair in word) for word in item["raw_words"])
        for item in inventories
    )
    raw_control = packet["raw_control_input"]
    checks["shape_control_generator"] = _keys(raw_control.get("generator"), {"increment", "modulus", "multiplier", "name", "sequence_length_per_seed"}) and isinstance(raw_control["generator"].get("name"), str) and all(_strict_int(raw_control["generator"].get(key)) for key in ("increment", "modulus", "multiplier", "sequence_length_per_seed"))
    checks["shape_seed_map"] = isinstance(raw_control.get("seeds"), dict) and all(isinstance(key, str) and _strict_int(value) for key, value in raw_control["seeds"].items())
    checks["shape_sequence_map"] = isinstance(raw_control.get("lcg_sequences"), dict) and all(isinstance(key, str) and isinstance(value, list) and all(_strict_int(item) for item in value) for key, value in raw_control["lcg_sequences"].items())
    checks["shape_control_lists"] = all(_list_of_strings(raw_control.get(name)) for name in ("a0_family_ids", "a1_family_ids")) and all(isinstance(raw_control.get(name), list) and all(_strict_int(value) for value in raw_control[name]) for name in ("control_digits", "control_pair_lengths", "neighboring_control_digits", "prototype_alphabet_sizes", "prototype_pair_lengths"))
    route_schema = packet["route_schema_input"]
    fixture = route_schema.get("schema_fixture")
    checks["shape_route_schema_fixture"] = (
        isinstance(fixture, dict)
        and isinstance(route_schema.get("schema_fixture_path"), str)
        and isinstance(route_schema.get("schema_fixture_sha256"), str)
        and isinstance(route_schema.get("expected_schema_fixture_sha256"), str)
    )
    checks["shape_route_lists"] = all(_list_of_strings(route_schema.get(name)) for name in ("criterion_order", "paired_provenance_fields", "target_root_metric_keys")) and _strict_int(route_schema.get("required_a0_control_count")) and _strict_int(route_schema.get("required_a1_control_count"))
    owner = packet["ownership_input"]
    checks["shape_positive_owner"] = (
        _keys(owner.get("positive_control_owner"), {"control_role", "marker_stride", "multiplicity", "operator_matrix", "projector_matrix", "repetitions", "selected_indices"})
        and _keys(owner.get("scalar_postselection"), {"declared_projector", "full_inventory"})
    )
    checks["shape_route_skill"] = all(
        isinstance(route_schema.get(name), str)
        for name in ("skill_artifact_encoding", "skill_artifact_path", "skill_byte_sha256", "expected_skill_byte_sha256", "skill_utf8")
    )
    checks["shape_research_maps"] = all(isinstance(packet["research_input"].get(name), dict) and all(isinstance(key, str) and isinstance(value, str) for key, value in packet["research_input"][name].items()) for name in ("dependent_seal_hashes", "expected_immutable_file_hashes", "immutable_file_hashes"))
    checks["shape_string_boundaries"] = isinstance(packet["schema"], str) and isinstance(packet["candidate_id"], str) and _list_of_strings(packet["claim_scope_input"].get("forbidden_claim_tokens"))
    return checks


def parse_and_select_cards(packet: dict[str, Any]) -> tuple[dict[str, Any], dict[str, bool]]:
    parsed: dict[str, dict[str, Any]] = {}
    checks: dict[str, bool] = {}
    records = packet.get("route_card_bytes", [])
    checks["six_card_record_count"] = len(records) == 6
    record_ids = [record.get("card_id") for record in records]
    checks["six_card_exact_unique_ordered_ids"] = (
        record_ids == sorted(CARD_HASHES) and len(set(record_ids)) == 6
    )
    for record in records:
        card_id = record.get("card_id")
        raw_text = record.get("raw_yaml_utf8")
        valid = isinstance(card_id, str) and card_id in CARD_HASHES and isinstance(raw_text, str)
        if valid:
            raw_hash = sha256(raw_text.encode("utf-8")).hexdigest()
            valid = (
                raw_hash == CARD_HASHES[card_id]
                and record.get("historical_byte_sha256") == raw_hash
                and record.get("vendored_byte_sha256") == raw_hash
                and record.get("relative_path") == f"inputs/route_cards/{card_id}.yaml"
            )
        try:
            card = yaml.safe_load(raw_text) if valid else None
        except yaml.YAMLError:
            card = None
        valid = valid and isinstance(card, dict) and card.get("candidate_id") == card_id
        checks[f"card_{card_id}_bytes_and_identity"] = bool(valid)
        if valid:
            parsed[card_id] = card
    rows = []
    for card_id in sorted(parsed):
        card = parsed[card_id]
        a1 = card["a1"]
        if card_id == "SD-C01":
            nonempty = a1.get("evidence_status") == "PROVED" and _path(a1, "metrics.formula_degree_cutoff") == 12
        elif card_id == "SD-C02":
            nonempty = _path(a1, "metrics.fixed_points_every_period") == 1 and _path(a1, "metrics.primitive_orbits") == "one period-1 zero orbit"
        elif card_id == "SD-C03":
            nonempty = a1.get("evidence_status") == "PROVED" and a1.get("verdict") == "A1_WEAK"
        elif card_id == "SD-C04":
            nonempty = _path(a1, "metrics.primitive_necklaces_max_cutoff") == 63319 and _path(a1, "metrics.repetition_matrix_failures") == 0
        elif card_id == "SD-C05":
            nonempty = _path(a1, "metrics.directed_cycles") != 0
        else:
            nonempty = a1.get("evidence_status") == "PROVED"
        a2 = card["a2"]
        same_object = a2.get("evidence_status") == "PROVED" and a2.get("verdict") == "A2_ANALYTIC_DETERMINANT"
        rows.append({
            "candidate_id": card_id,
            "nonempty_intrinsic_ledger": nonempty,
            "same_object_determinant": same_object,
            "survivor": nonempty and same_object,
            "A3": card["a3"]["verdict"],
            "A4": card["a4"]["verdict"],
        })
    survivors = [row["candidate_id"] for row in rows if row["survivor"]]
    a3_rank = {"A3_FAIL": 0, "A3_PARTIAL_ANALYTIC_STRUCTURE": 1, "A3_CONTROLLED_CONTINUATION": 2, "A3_EXACT_DIVISOR_MATCH": 3}
    a4_rank = {"A4_FAIL": 0, "A4_FORMAL_HINT": 1, "A4_NATURAL_QUANTIZATION": 2}
    winner = max(
        [row for row in rows if row["survivor"]],
        key=lambda row: (a3_rank.get(row["A3"], -1), a4_rank.get(row["A4"], -1)),
        default={"candidate_id": None},
    )["candidate_id"]
    checks["selection_survivor_derivation"] = survivors == ["SD-C01", "SD-C02", "SD-C04"]
    checks["selection_c02_zero_orbit_nonempty"] = any(row["candidate_id"] == "SD-C02" and row["nonempty_intrinsic_ledger"] for row in rows)
    checks["selection_a3_a4_winner"] = winner == "SD-C04"
    return {"rows": rows, "survivors": survivors, "winner": winner}, checks


def expected_raw_word_json(words: list[PairWord]) -> list[list[list[int]]]:
    return [[[left, right] for left, right in word] for word in words]


def run_summary(digits: tuple[int, ...], family: str, inventories: dict[int, list[PairWord]]) -> dict[str, Any]:
    orientation_ids = {word_id(word) for words in inventories.values() for word in words}
    rows = []
    failures: Counter[str] = Counter()
    trace_groups: defaultdict[int, int] = defaultdict(int)
    trace_prime = 0
    delta_prime = 0
    delta_nonboundary_prime = 0
    for length in (1, 2, 3, 4):
        for word in inventories[length]:
            matrix = word_matrix(word)
            det = determinant(matrix)
            tr = trace(matrix)
            delta = tr * tr - 4
            failures["determinant_one"] += int(det != 1)
            failures["trace_at_least_three"] += int(tr < 3)
            failures["order_discriminant_factorization"] += int(delta != (tr - 2) * (tr + 2))
            failures["nonsquare_interval"] += int(not ((tr - 1) ** 2 < delta < tr * tr))
            failures["order_discriminant_nonsquare"] += int(math.isqrt(delta) ** 2 == delta)
            failures["clock_strict_inequality_certificate"] += int(not (delta > (tr - 2) ** 2 and (tr - 1) ** 2 > tr))
            q_previous, q_current = 2, tr
            for exponent in range(2, 7):
                q_next = tr * q_current - q_previous
                failures["trace_power_recurrence"] += int(trace(matpow(matrix, exponent)) != q_next)
                q_previous, q_current = q_current, q_next
            failures["trace_square_mismatch"] += int(trace(matpow(matrix, 2)) == tr * tr)
            trace_prime += int(is_prime(tr))
            is_delta_prime = is_prime(delta)
            delta_prime += int(is_delta_prime)
            delta_nonboundary_prime += int(is_delta_prime and (tr, delta) != (3, 5))
            trace_groups[tr] += 1
            reverse = canonical_rotation(reverse_pair_word(word))
            orientation = word_id(word)
            reverse_orientation = word_id(reverse)
            rows.append({
                "delta_order": delta,
                "determinant": det,
                "matrix": list(matrix),
                "pair_length": length,
                "trace": tr,
                "word": [[a, b] for a, b in word],
                "orientation_id": orientation,
                "reverse_orientation_id": reverse_orientation,
                "reversal_orbit_id": min(orientation, reverse_orientation),
                "self_reversal": orientation == reverse_orientation,
                "reverse_class_present": reverse_orientation in orientation_ids,
                "source_multiplicity": 1,
                "untwisted_sign": 1,
                "phase_exponent_mod_97": 0,
                "expanding_eigenvalue_minpoly": [1, -tr, 1],
                "geodesic_norm_minpoly": [1, -(tr * tr - 2), 1],
                "derivative_multiplier_minpoly": [1, -(tr * tr - 2), 1],
                "norm_qsqrt_coefficients": [[tr * tr - 2, 2], [tr, 2]],
                "derivative_qsqrt_coefficients": [[tr * tr - 2, 2], [-tr, 2]],
                "marker_exponent_per_repetition": 2 * length,
            })
    rows.sort(key=lambda row: (row["pair_length"], row["word"], row["matrix"]))
    row_hash = sha256(json.dumps(rows, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("ascii")).hexdigest()
    nonzero_failures = {key: value for key, value in sorted(failures.items()) if value}
    collisions = [amount for amount in trace_groups.values() if amount > 1]
    return {
        "alphabet_label": f"{family}_D{len(digits)}",
        "digits": list(digits),
        "pair_alphabet_size": len(digits) ** 2,
        "primitive_pair_necklaces_by_length": {str(length): len(inventories[length]) for length in (1, 2, 3, 4)},
        "primitive_pair_necklaces_total": len(rows),
        "theorem_failures": nonzero_failures,
        "trace_prime_orbit_count": trace_prime,
        "trace_composite_orbit_count": len(rows) - trace_prime,
        "order_discriminant_prime_orbit_count": delta_prime,
        "order_discriminant_prime_nonboundary_count": delta_nonboundary_prime,
        "trace_collision_group_count": len(collisions),
        "trace_collision_orbit_excess": sum(value - 1 for value in collisions),
        "scientific_rows_sha256": row_hash,
    }


def verify_inventories(packet: dict[str, Any]) -> tuple[list[dict[str, Any]], dict[str, bool], dict[tuple[str, int], list[PairWord]]]:
    records = packet.get("raw_primitive_inventories", [])
    checks: dict[str, bool] = {"inventory_record_count": len(records) == 24}
    by_family: dict[tuple[str, int], dict[int, list[PairWord]]] = defaultdict(dict)
    flattened: dict[tuple[str, int], list[PairWord]] = {}
    for record in records:
        family = record.get("family")
        alphabet_size = record.get("alphabet_size")
        length = record.get("pair_length")
        digits = tuple(record.get("digits", []))
        key = (str(family), int(alphabet_size)) if isinstance(alphabet_size, int) else (str(family), -1)
        parsed_words = [tuple((int(pair[0]), int(pair[1])) for pair in word) for word in record.get("raw_words", [])]
        expected = enumerate_necklaces(digits, int(length)) if isinstance(length, int) else []
        expected_id = f"{family}_D{alphabet_size}_k{length}"
        checks[f"inventory_{expected_id}_schema"] = (
            record.get("run_id") == expected_id
            and family in {"canonical", "neighboring"}
            and alphabet_size in {2, 3, 4}
            and length in {1, 2, 3, 4}
            and digits == tuple(range(1 if family == "canonical" else 2, (1 if family == "canonical" else 2) + alphabet_size))
        )
        checks[f"inventory_{expected_id}_exact"] = parsed_words == expected
        if isinstance(length, int):
            by_family[key][length] = parsed_words
    summaries = []
    for key in sorted(by_family):
        family, alphabet_size = key
        inventories = by_family[key]
        digits = tuple(range(1 if family == "canonical" else 2, (1 if family == "canonical" else 2) + alphabet_size))
        complete = sorted(inventories) == [1, 2, 3, 4]
        checks[f"run_{family}_D{alphabet_size}_complete"] = complete
        if complete:
            summary = run_summary(digits, family, inventories)
            summaries.append(summary)
            checks[f"run_{family}_D{alphabet_size}_theorem"] = summary["theorem_failures"] == {}
            flattened[key] = [word for length in (1, 2, 3, 4) for word in inventories[length]]
    return summaries, checks, flattened


def derive_controls(packet: dict[str, Any], base_words: list[PairWord], neighboring_words: list[PairWord]) -> tuple[dict[str, Any], dict[str, bool]]:
    raw = packet.get("raw_control_input", {})
    seeds = raw.get("seeds", {})
    sequences = raw.get("lcg_sequences", {})
    checks: dict[str, bool] = {
        "control_generator_schema": raw.get("generator") == {
            "name": "LCG31", "modulus": 2**31, "multiplier": 1103515245,
            "increment": 12345, "sequence_length_per_seed": 256,
        },
        "a0_family_exact_set": raw.get("a0_family_ids") == [
            "shuffled_generated_primes", "matched_density_integers", "composites",
            "pseudoprimes", "randomized_labels", "neighboring_digits", "simpler_parent",
        ],
        "a1_family_exact_set": raw.get("a1_family_ids") == [
            "shuffled_periods", "random_weights", "random_phases", "same_density_lengths",
            "neighboring_digits", "simpler_parent",
        ],
        "control_seed_exact_map": seeds == SEEDS,
        "control_sequence_exact_keyset": sorted(sequences) == sorted(SEEDS),
        "control_grid_exact": (
            raw.get("control_digits") == [1, 2]
            and raw.get("neighboring_control_digits") == [2, 3]
            and raw.get("control_pair_lengths") == [1, 2, 3]
            and raw.get("prototype_alphabet_sizes") == [2, 3, 4]
            and raw.get("prototype_pair_lengths") == [1, 2, 3, 4]
        ),
    }
    for name, seed in sorted(seeds.items()):
        checks[f"lcg_{name}"] = sequences.get(name) == lcg(int(seed), 256)
    primes = first_primes(len(base_words))
    shuffled_primes = fisher_yates(primes, sequences["a0_shuffled_primes"])
    base_traces = [trace(word_matrix(word)) for word in base_words]
    prime_count = sum(is_prime(value) for value in base_traces)
    matched_primes = generated_by_primality(sequences["a0_matched_density"], prime_count, True)
    matched_composites = generated_by_primality(sequences["a0_composites"], len(base_words) - prime_count, False)
    matched = fisher_yates(matched_primes + matched_composites, sequences["a0_pseudoprimes"])
    composites = generated_by_primality(sequences["a0_composites"], len(base_words), False)
    pseudoprimes = fisher_yates(first_base2_pseudoprimes(30), sequences["a0_pseudoprimes"])
    labels = fisher_yates(base_traces, sequences["a0_randomized_labels"])
    periods = [roof_string(value) for value in base_traces]
    shuffled_periods = fisher_yates(periods, sequences["a1_shuffled_periods"])
    weights = []
    for value in sequences["a1_random_weights"][:len(base_words)]:
        numerator = value % 2001 - 1000
        weights.append(1 if numerator == 0 else numerator)
    phases = [1 + value % 96 for value in sequences["a1_random_phases"][:len(base_words)]]
    denominator = 1_000_003
    source_bins = [int(Decimal(period) // Decimal(2)) for period in periods]
    random_lengths = [
        (2 * bin_index * denominator + 1 + value % (2 * denominator - 1), denominator)
        for bin_index, value in zip(source_bins, sequences["a1_same_density_lengths"], strict=False)
    ][:len(base_words)]
    random_bins = [int(Fraction(numerator, den) // 2) for numerator, den in random_lengths]
    digit_parent = []
    for length in (1, 2, 3):
        for word in product((1, 2), repeat=length):
            if is_primitive(word) and word == canonical_rotation(word):
                digit_parent.append(word)
    a0 = {
        "shuffled_generated_primes": shuffled_primes != primes and all(is_prime(value) for value in shuffled_primes),
        "matched_density_integers": len(matched) == len(base_words) and sum(is_prime(value) for value in matched) == prime_count,
        "composites": len(composites) == 30 and not any(is_prime(value) for value in composites),
        "pseudoprimes": len(pseudoprimes) == 30 and all(not is_prime(value) and pow(2, value - 1, value) == 1 for value in pseudoprimes),
        "randomized_labels": labels != base_traces and Counter(labels) == Counter(base_traces),
        "neighboring_digits": len(neighboring_words) == len(base_words) and [trace(word_matrix(word)) for word in neighboring_words] != base_traces,
        "simpler_parent": len(digit_parent) > 0 and all(not isinstance(item[0], tuple) for item in digit_parent),
    }
    a1 = {
        "shuffled_periods": shuffled_periods != periods and Counter(shuffled_periods) == Counter(periods),
        "random_weights": len(weights) == len(base_words) and all(value != 1009 for value in weights),
        "random_phases": len(phases) == len(base_words) and all(1 <= value < 97 for value in phases) and len(set(phases)) > 1,
        "same_density_lengths": len(random_lengths) == len(base_words) and Counter(random_bins) == Counter(source_bins) and all(Fraction(numerator, den) > 0 for numerator, den in random_lengths),
        "neighboring_digits": len(neighboring_words) == len(base_words) and neighboring_words != base_words,
        "simpler_parent": len(digit_parent) > 0,
    }
    for name, value in a0.items():
        checks[f"a0_{name}"] = value
    for name, value in a1.items():
        checks[f"a1_{name}"] = value
    return {"A0": a0, "A1": a1}, checks


def derive_typed_bridge(packet: dict[str, Any], base_by_length: dict[int, list[PairWord]]) -> tuple[dict[str, Any], dict[str, bool]]:
    raw = packet.get("raw_type_input", {})
    fixture = tuple(raw.get("return_map_digit_fixture", []))
    grouped = tuple((fixture[index], fixture[index + 1]) for index in range(0, len(fixture), 2))
    rho_iota = grouped[1:]
    iota_sigma2 = tuple((fixture[index], fixture[index + 1]) for index in range(2, len(fixture), 2))
    wrong_pair_sigma2 = grouped[2:]
    pair_fixture = tuple(tuple(pair) for pair in raw.get("reversal_pair_fixture", []))
    raw_reverse_grouped = tuple((value, next_value) for value, next_value in zip(tuple(reversed(tuple(x for pair in pair_fixture for x in pair)))[::2], tuple(reversed(tuple(x for pair in pair_fixture for x in pair)))[1::2]))
    expected_reverse = reverse_pair_word(pair_fixture)
    digit_counts = {}
    for length in range(1, 7):
        digit_counts[length] = sum(1 for word in product((1, 2), repeat=length) if is_primitive(word) and word == canonical_rotation(word))
    pair_counts = {length: len(base_by_length[length]) for length in (1, 2, 3)}
    predicted = {length: 2 * digit_counts[2 * length] + (digit_counts[length] if length % 2 else 0) for length in (1, 2, 3)}
    checks = {
        "typed_schema": (
            raw.get("type_symbols") == ["SigmaPrimitiveDigit", "RhoPrimitivePair", "PrimitiveClosedGeodesic"]
            and raw.get("digit_space_symbol") == "X=N^N"
            and raw.get("digit_shift_symbol") == "sigma"
            and raw.get("pair_space_symbol") == "X2=(N^2)^N"
            and raw.get("pair_shift_symbol") == "rho"
            and raw.get("grouping_symbol") == "iota"
            and raw.get("grouping_block_size") == 2
            and raw.get("return_map_digit_fixture") == [1, 2, 3, 4, 5, 6, 7, 8]
            and raw.get("reversal_pair_fixture") == [[1, 2], [2, 3], [1, 4]]
            and raw.get("parent_supplied_symbols") == ["one_digit_gauss_branches", "L_s", "det(I-L_s^2)"]
            and raw.get("paper40_new_symbol") == "RhoPrimitivePair"
        ),
        "return_map_conjugacy": rho_iota == iota_sigma2 and wrong_pair_sigma2 != iota_sigma2,
        "reversal_bridge": raw_reverse_grouped == expected_reverse and is_primitive(pair_fixture) == is_primitive(expected_reverse),
        "splitting_formula": pair_counts == predicted == {1: 4, 2: 6, 3: 20},
        "flattened_22_firewall": is_primitive(((2, 2),)) and not is_primitive((2, 2)),
    }
    return {
        "digit_space": "X=N^N",
        "pair_space": "X2=(N^2)^N",
        "conjugacy": "rho(iota(x))=iota(sigma^2(x))",
        "return_map_typing_exact": checks["return_map_conjugacy"] and checks["reversal_bridge"],
        "pair_counts_D2_k1_to_k3": [pair_counts[index] for index in (1, 2, 3)],
        "splitting_exact": checks["splitting_formula"],
    }, checks


def derive_branch(packet: dict[str, Any]) -> tuple[dict[str, Any], dict[str, bool]]:
    raw = packet.get("raw_branch_input", {})
    stored = tuple(raw.get("stored_digits", []))
    raw_indices = tuple(reversed(stored))
    matrix = branch_word_matrix(stored)
    j: Matrix = (0, 1, 1, 0)
    a_matrix = IDENTITY
    for digit in stored:
        a_matrix = matmul(a_matrix, digit_matrix(digit))
    z = Fraction(*raw.get("evaluation_point", [0, 1]))
    point = z
    weight = Fraction(1)
    for digit in raw_indices:
        denominator = digit + point
        weight /= denominator**2
        point = 1 / denominator
    wrong_point = z
    wrong_weight = Fraction(1)
    for digit in stored:
        denominator = digit + wrong_point
        wrong_weight /= denominator**2
        wrong_point = 1 / denominator
    checks = {
        "branch_raw_input_schema": (
            raw.get("raw_operator_nesting") == "last_raw_branch_on_left"
            and raw.get("weight_exponent_s") == 1
            and raw.get("matrix_templates") == {
                "A": [["a", 1], [1, 0]],
                "B": [[0, 1], [1, "a"]],
                "J": [[0, 1], [1, 0]],
            }
            and raw.get("stored_digits") == [1, 2, 2, 3, 1, 4]
            and raw.get("evaluation_point") == [1, 4]
        ),
        "branch_A_B_J": a_matrix == matmul(matmul(j, matrix), j),
        "branch_stored_matrix": matrix == (22, 105, 31, 148),
        "branch_correct_value": point == Fraction(442, 623) and weight == Fraction(16, 388129),
        "branch_same_index_rejected": wrong_point == Fraction(146, 697) and wrong_weight == Fraction(16, 485809) and (wrong_point, wrong_weight) != (point, weight),
    }
    return {
        "branch_order_exact": all(checks.values()),
        "branch_value": [point.numerator, point.denominator],
        "branch_weight": [weight.numerator, weight.denominator],
        "wrong_same_index_value": [wrong_point.numerator, wrong_point.denominator],
        "wrong_same_index_weight": [wrong_weight.numerator, wrong_weight.denominator],
    }, checks


def derive_collisions(packet: dict[str, Any]) -> tuple[list[dict[str, Any]], dict[str, bool]]:
    output = []
    checks = {
        "collision_raw_record_count": len(packet.get("raw_collision_input", [])) == 3,
        "collision_witness_id_order": [item.get("witness_id") for item in packet.get("raw_collision_input", [])] == ["W1", "W2", "W3"],
    }
    for item in packet.get("raw_collision_input", []):
        witness_id = item.get("witness_id")
        left = tuple(tuple(pair) for pair in item.get("left_word", []))
        right = tuple(tuple(pair) for pair in item.get("right_word", []))
        left_matrix = word_matrix(left)
        right_matrix = word_matrix(right)
        left_trace = trace(left_matrix)
        right_trace = trace(right_matrix)
        reversal_related = canonical_rotation(reverse_pair_word(left)) == canonical_rotation(right)
        exact = (
            is_primitive(left) and is_primitive(right)
            and left == canonical_rotation(left) and right == canonical_rotation(right)
            and determinant(left_matrix) == determinant(right_matrix) == 1
            and left_trace == right_trace
            and word_id(left) != word_id(right)
        )
        identifier = {
            (4, False, True): "TRACE4_REVERSAL",
            (6, False, False): "TRACE6_NONREVERSAL",
            (10, True, False): "TRACE10_CROSS_LENGTH_NONREVERSAL",
        }.get((left_trace, len(left) != len(right), reversal_related))
        expected = COLLISION_WITNESSES.get(witness_id)
        checks[f"collision_{witness_id}_exact_raw_binding"] = (
            expected is not None and left == expected[0] and right == expected[1]
        )
        checks[f"collision_{witness_id}_derived_class"] = (
            exact and expected is not None and identifier == expected[2]
        )
        output.append({
            "id": identifier,
            "trace": left_trace,
            "cross_pair_length": len(left) != len(right),
            "digit_reversal_related": reversal_related,
        })
    return output, checks


def quadratic_multiply(
    left: tuple[Fraction, Fraction],
    right: tuple[Fraction, Fraction],
    radicand: int,
) -> tuple[Fraction, Fraction]:
    return (
        left[0] * right[0] + left[1] * right[1] * radicand,
        left[0] * right[1] + left[1] * right[0],
    )


def quadratic_power(
    value: tuple[Fraction, Fraction], exponent: int, radicand: int
) -> tuple[Fraction, Fraction]:
    result = (Fraction(1), Fraction(0))
    factor = value
    power_value = exponent
    while power_value:
        if power_value & 1:
            result = quadratic_multiply(result, factor, radicand)
        factor = quadratic_multiply(factor, factor, radicand)
        power_value //= 2
    return result


def derive_projections(all_words: list[PairWord], packet: dict[str, Any]) -> tuple[list[dict[str, Any]], dict[str, bool]]:
    definitions = packet.get("projection_definition_input", [])
    schema = packet.get("projection_criterion_schema", {})
    matrices = [word_matrix(word) for word in all_words]
    traces = [trace(matrix) for matrix in matrices]
    deltas = [value * value - 4 for value in traces]
    exponents = schema.get("repetition_exponents", [])
    trace_power_fail = all(
        trace(matpow(matrix, exponent)) != tr**exponent
        for matrix, tr in zip(matrices, traces, strict=True)
        for exponent in exponents
    )
    delta_power_fail = all(
        trace(matpow(matrix, exponent)) ** 2 - 4 != delta**exponent
        for matrix, delta in zip(matrices, deltas, strict=True)
        for exponent in exponents
    )
    norm_irrational = all(math.isqrt(delta) ** 2 != delta for delta in deltas)
    qsqrt_exact = True
    root_selectors = True
    norm_power_exact = True
    for matrix, tr, delta in zip(matrices, traces, deltas, strict=True):
        norm = (Fraction(tr * tr - 2, 2), Fraction(tr, 2))
        derivative = (norm[0], -norm[1])
        qsqrt_exact = qsqrt_exact and quadratic_multiply(norm, derivative, delta) == (Fraction(1), Fraction(0))
        root_selectors = root_selectors and delta > 0 and norm[0] > 1 and norm[1] > 0 and derivative[0] > 0 and derivative[1] < 0
        for exponent in exponents:
            powered_matrix = matpow(matrix, exponent)
            powered_trace = trace(powered_matrix)
            norm_power = quadratic_power(norm, exponent, delta)
            derivative_power = quadratic_power(derivative, exponent, delta)
            norm_power_exact = norm_power_exact and (
                quadratic_multiply(norm_power, derivative_power, delta)
                == (Fraction(1), Fraction(0))
                and norm_power[0] + derivative_power[0]
                == Fraction(powered_trace * powered_trace - 2)
                and norm_power[1] + derivative_power[1] == 0
            )
    norm_clock_exact = qsqrt_exact and root_selectors and all(len(word) >= 1 for word in all_words)
    rational_prime = {
        "P_t": all(is_prime(value) for value in traces) and len(set(traces)) == len(traces),
        "P_Delta": all(is_prime(value) for value in deltas) and len(set(deltas)) == len(deltas),
        "P_N": False,
    }
    rows = [
        {"projection": "P_t", "rational_integer_support": all(isinstance(value, int) for value in traces), "rational_prime_selectivity": rational_prime["P_t"], "clock": False if norm_irrational else True, "repetition": not trace_power_fail},
        {"projection": "P_Delta", "rational_integer_support": all(isinstance(value, int) for value in deltas), "rational_prime_selectivity": rational_prime["P_Delta"], "clock": False if norm_irrational else True, "repetition": not delta_power_fail},
        {"projection": "P_N", "rational_integer_support": not norm_irrational, "rational_prime_selectivity": rational_prime["P_N"], "clock": norm_clock_exact, "repetition": norm_power_exact},
    ]
    checks = {
        "projection_definition_exact_set": definitions == [
            {"projection_id": "P_t", "definition": "matrix_trace"},
            {"projection_id": "P_Delta", "definition": "matrix_trace_squared_minus_four"},
            {"projection_id": "P_N", "definition": "square_of_expanding_eigenvalue"},
        ],
        "projection_criterion_schema": (
            schema.get("criterion_ids") == ["rational_integer_support", "clock", "repetition"]
            and schema.get("norm_minimal_polynomial_template") == "x^2-(t^2-2)x+1"
            and schema.get("norm_root_selector") == "larger_positive_root"
            and schema.get("derivative_root_selector") == "smaller_positive_root"
            and schema.get("clock_marker_exponent_rule") == "2*pair_length"
            and exponents == [2, 3, 4, 5, 6]
        ),
        "projection_qsqrt_algebra": qsqrt_exact,
        "projection_root_selectors_and_positivity": root_selectors,
        "projection_norm_clock_T_equals_log_PN": norm_clock_exact,
        "projection_norm_all_matrix_powers": norm_power_exact,
        "projection_trace_all_power_failure": trace_power_fail,
        "projection_delta_all_power_failure": delta_power_fail,
        "projection_norm_irrational": norm_irrational,
        "projection_rational_prime_selectivity": not any(rational_prime.values()),
        "projection_truth_matrix": rows == [
            {"projection": "P_t", "rational_integer_support": True, "rational_prime_selectivity": False, "clock": False, "repetition": False},
            {"projection": "P_Delta", "rational_integer_support": True, "rational_prime_selectivity": False, "clock": False, "repetition": False},
            {"projection": "P_N", "rational_integer_support": False, "rational_prime_selectivity": False, "clock": True, "repetition": True},
        ],
    }
    return rows, checks


def derive_boundaries(packet: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any], dict[str, bool]]:
    mayer = packet.get("mayer_source_input", {})
    owner = packet.get("ownership_input", {})
    positive = owner.get("positive_control_owner", {})
    scalar = owner.get("scalar_postselection", {})
    row_contract = packet.get("row_contract_input", {})
    operator = positive.get("operator_matrix")
    projector = positive.get("projector_matrix")

    def square_integer_matrix(value: Any) -> bool:
        return (
            isinstance(value, list) and bool(value)
            and all(isinstance(row, list) and len(row) == len(value) for row in value)
            and all(_strict_int(entry) for row in value for entry in row)
        )

    def dense_product(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
        return [
            [sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right))]
            for i in range(len(left))
        ]

    def dense_power(matrix: list[list[int]], exponent: int) -> list[list[int]]:
        result = [[int(i == j) for j in range(len(matrix))] for i in range(len(matrix))]
        for _ in range(exponent):
            result = dense_product(result, matrix)
        return result

    selected = positive.get("selected_indices")
    repetitions = positive.get("repetitions")
    common_dimension = (
        square_integer_matrix(operator) and square_integer_matrix(projector)
        and len(operator) == len(projector)
        and isinstance(selected, list) and selected
        and all(_strict_int(index) and 0 <= index < len(operator) for index in selected)
        and isinstance(repetitions, list) and all(_strict_int(value) and value > 0 for value in repetitions)
    )
    idempotent = commutes = power_traces = marker_support = full_marker_support = repetition_markers = False
    full_traces: list[int] = []
    selected_traces: list[int] = []
    if common_dimension:
        idempotent = dense_product(projector, projector) == projector
        commutes = dense_product(projector, operator) == dense_product(operator, projector)
        for exponent in repetitions:
            powered = dense_power(operator, exponent)
            selected_traces.append(sum(dense_product(projector, powered)[i][i] for i in range(len(operator))))
            full_traces.append(sum(powered[i][i] for i in range(len(operator))))
        restricted_traces = [sum(dense_power(operator, exponent)[i][i] for i in selected) for exponent in repetitions]
        power_traces = selected_traces == restricted_traces == [2, 4, 8, 16, 32, 64]
        marker_stride = positive.get("marker_stride")
        determinant_coefficients = [1]
        for index in selected:
            eigenvalue = operator[index][index]
            determinant_coefficients = determinant_coefficients + [0]
            for degree in range(len(determinant_coefficients) - 1, 0, -1):
                determinant_coefficients[degree] -= eigenvalue * determinant_coefficients[degree - 1]
        marker_support = (
            _strict_int(marker_stride)
            and determinant_coefficients == [1, -2]
            and [marker_stride * degree for degree, coefficient in enumerate(determinant_coefficients) if coefficient] == [0, 2]
        )
        if len(operator) == 2:
            full_determinant_coefficients = [
                1,
                -(operator[0][0] + operator[1][1]),
                operator[0][0] * operator[1][1] - operator[0][1] * operator[1][0],
            ]
            full_marker_support = (
                _strict_int(marker_stride)
                and full_determinant_coefficients == [1, -5, 6]
                and [marker_stride * degree for degree, coefficient in enumerate(full_determinant_coefficients) if coefficient] == [0, 2, 4]
            )
        repetition_markers = _strict_int(marker_stride) and [marker_stride * exponent for exponent in repetitions] == [2, 4, 6, 8, 10, 12]
    scalar_inventory = scalar.get("full_inventory")
    scalar_valid = isinstance(scalar_inventory, list) and all(_strict_int(value) for value in scalar_inventory)
    selected_scalars = [value for value in scalar_inventory if is_prime(value)] if scalar_valid else []
    rejected_scalars = [value for value in scalar_inventory if not is_prime(value)] if scalar_valid else []
    checks = {
        "mayer_function_space": mayer.get("function_space_symbol") == "A_infinity(D)" and mayer.get("disk_center_radius") == [[1, 0], [3, 2]],
        "mayer_three_domains": mayer.get("determinant_half_plane") == "Re(s)>1/2" and mayer.get("euler_product_initial_half_plane") == "Re(s)>1" and mayer.get("continuation_domain") == "C",
        "mayer_local_u": mayer.get("local_u_domain") == "formal_or_small_abs_u" and mayer.get("selberg_identity_u_value") == 1,
        "mayer_coefficients": mayer.get("source_log_coefficient_tokens") == ["u^(2*k*r)", "d_w^(r*s)", "r", "1-d_w^r"] and mayer.get("target_log_coefficient_tokens") == ["u^(2*k*r)", "p^(-r*s)", "r"],
        "ownership_declared_symbols": owner.get("declared_object_symbols") == ["X", "X2", "sigma", "rho", "iota", "L_s", "det(I-L_s^2)"],
        "ownership_selector_absent": owner.get("declared_untwisted_selector_symbols") == [] and owner.get("ownership_scope") == "FROZEN_UNTWISTED_SCHEMA_ONLY",
        "owner_synthetic_control_role": positive.get("control_role") == "SYNTHETIC_POSITIVE_OWNER_CONTROL_NOT_SD_C42",
        "owner_common_dimension": common_dimension,
        "owner_projector_idempotent": idempotent,
        "owner_reducing_commutation": commutes,
        "owner_power_traces": power_traces and full_traces == [5, 13, 35, 97, 275, 793],
        "owner_multiplicity_one": positive.get("multiplicity") == len(selected or []) == 1,
        "owner_marker_support": marker_support,
        "owner_full_ledger_marker_support": full_marker_support,
        "owner_repetition_marker_degrees": repetition_markers,
        "scalar_postselection_computed": scalar_inventory == [3, 4] and selected_scalars == [3] and rejected_scalars == [4],
        "scalar_postselection_has_no_declared_projector": scalar.get("declared_projector") is None,
        "row_rotation_only": row_contract.get("orientation_equivalence") == "rotation_only",
        "row_reversal_metadata": row_contract.get("reversal_metadata_fields") == ["orientation_id", "reverse_orientation_id", "reversal_orbit_id", "self_reversal", "reverse_class_present"],
        "row_no_reverse_quotient": row_contract.get("reverse_quotient_rule") == "metadata_only_no_reversal_quotient",
        "row_source_multiplicity": row_contract.get("source_multiplicity") == 1,
        "row_untwisted_sign": row_contract.get("untwisted_sign") == 1,
        "row_untwisted_phase": row_contract.get("phase_modulus") == 97 and row_contract.get("phase_exponent") == 0,
        "row_stability_denominator": row_contract.get("stability_denominator_token") == "1-d_w^r" and "1-d_w^r" in mayer.get("source_log_coefficient_tokens", []),
    }
    return {
        "operator_domain": "D={z:|z-1|<3/2};A_infinity(D)",
        "determinant_domain": mayer.get("determinant_half_plane"),
        "euler_product_initial_domain": mayer.get("euler_product_initial_half_plane"),
        "meromorphic_continuation_domain": mayer.get("continuation_domain"),
        "local_u_scope": mayer.get("local_u_domain"),
        "selberg_identity_u": mayer.get("selberg_identity_u_value"),
        "source_log_coefficient": "u^(2*k*r)*d_w^(r*s)/(r*(1-d_w^r))",
        "target_log_coefficient": "u^(2*k*r)*p^(-r*s)/r",
    }, {
        "declared_selector_in_frozen_untwisted_schema": bool(owner.get("declared_untwisted_selector_symbols")),
        "universal_nonexistence_claim": False,
    }, checks


def validate_static(packet: dict[str, Any]) -> dict[str, bool]:
    chronology = packet.get("chronology_input", {})
    freeze = packet.get("experiment_freeze_input", {})
    research = packet.get("research_input", {})
    prototype = packet.get("prototype_reproduction_input", {})
    selection_schema = packet.get("selection_rule_schema", {})
    route_schema = packet.get("route_schema_input", {})
    claim = packet.get("claim_scope_input", {})
    return {
        "packet_schema": packet.get("schema") == "paper40-authority-raw-source-packet-v2",
        "candidate_id": packet.get("candidate_id") == "SD-C42",
        "chronology": chronology == {
            "classification": "RETROSPECTIVE_CHECKER_FROZEN_AUTHORITY_INTEGRATION",
            "v1_and_inflight_smoke_outputs_known": True,
            "canonical_prototype_outputs_known": True,
            "control_lock_precedes_clean_replacement_rerun": True,
            "research_renderings_postdate_canonical_run": True,
            "authority_checker_inputs_precede_authority_run": True,
            "prospective_credit_allowed": False,
        },
        "experiment_freeze": (
            freeze.get("preregistration_sha256") == freeze.get("expected_preregistration_sha256") == PREREG_SHA256
            and freeze.get("plan_sha256") == freeze.get("expected_plan_sha256") == PLAN_SHA256
            and freeze.get("preregistration_path") == "experiments/PREREGISTRATION.md"
            and freeze.get("plan_path") == "experiments/EXPERIMENT_PLAN.md"
        ),
        "research_lock": (
            research.get("manifest_sha256") == research.get("expected_manifest_sha256") == RESEARCH_LOCK_SHA256
            and research.get("pointer_sha256") == research.get("expected_pointer_sha256") == RESEARCH_POINTER_SHA256
            and research.get("immutable_file_hashes") == research.get("expected_immutable_file_hashes") == RESEARCH_FILES
            and research.get("dependent_seal_hashes") == DEPENDENT_SEALS
            and research.get("manifest_path") == "RESEARCH_LOCK.sha256"
            and research.get("pointer_path") == "RESEARCH_LOCK.json"
        ),
        "prototype_input": (
            prototype.get("control_lock_sha256") == prototype.get("expected_control_lock_sha256") == CONTROL_LOCK_SHA256
            and prototype.get("known_output_hash_targets") == KNOWN_OUTPUT_HASHES
            and prototype.get("vendor_root") == "docs/inputs/prototype_v3"
            and prototype.get("control_lock_path") == "docs/inputs/prototype_v3/CONTROL_LOCK.md"
        ),
        "selection_rule_schema": (
            selection_schema.get("card_ids") == sorted(CARD_HASHES)
            and selection_schema.get("nonempty_intrinsic_ledger_rule") == "candidate_specific_a1_source_anchor"
            and selection_schema.get("same_object_determinant_rule") == "a2.evidence_status=PROVED_and_a2.verdict=A2_ANALYTIC_DETERMINANT"
            and selection_schema.get("tie_break_order") == ["A3", "A4"]
            and selection_schema.get("forbidden_predicates") == ["nontrivial", "preset_winner", "rank_from_candidate_id"]
        ),
        "route_schema": (
            route_schema.get("skill") == "route-a-evaluator"
            and route_schema.get("skill_version") == "0.2.0"
            and route_schema.get("candidate_id") == "SD-C42"
            and route_schema.get("evaluation_date") == "2026-08-17"
            and route_schema.get("criterion_order") == ["A0", "A1", "A2", "A3", "A4"]
            and route_schema.get("schema_fixture_path") == "code/contracts/ROUTE_A_V0_2_SCHEMA.json"
            and route_schema.get("schema_fixture_sha256") == route_schema.get("expected_schema_fixture_sha256") == ROUTE_SCHEMA_FIXTURE_SHA256
            and isinstance(route_schema.get("schema_fixture"), dict)
            and sha256(canonical_bytes(route_schema["schema_fixture"])).hexdigest() == ROUTE_SCHEMA_FIXTURE_SHA256
            and route_schema["schema_fixture"].get("skill_sha256") == ROUTE_SKILL_SHA256
            and route_schema.get("skill_artifact_path") == "docs/inputs/route-a-evaluator-v0.2.0.md.b64"
            and route_schema.get("skill_artifact_encoding") == "base64-rfc4648"
            and route_schema.get("skill_byte_sha256") == route_schema.get("expected_skill_byte_sha256") == ROUTE_SKILL_SHA256
            and isinstance(route_schema.get("skill_utf8"), str)
            and sha256(route_schema["skill_utf8"].encode("utf-8")).hexdigest() == ROUTE_SKILL_SHA256
            and route_schema["schema_fixture"].get("evidence_status_labels") == [
                "PROVED", "CONDITIONAL_THEOREM", "NUMERICALLY_CERTIFIED",
                "NUMERICAL_OBSERVATION", "HEURISTIC", "MODELING_CHOICE",
                "FITTED_PARAMETER", "OPEN", "REFUTED", "NOT_TESTABLE", "STOP_SCOPED",
            ]
            and all(
                ROUTE_TUPLE[layer] in route_schema["schema_fixture"].get("verdict_labels", {}).get(layer, [])
                for layer in ("A0", "A1", "A2", "A3", "A4")
            )
            and "A3_EXACT_DIVISOR_CANDIDATE" in route_schema["schema_fixture"].get("verdict_labels", {}).get("A3", [])
            and "A3_EXACT_DIVISOR_MATCH" not in route_schema["schema_fixture"].get("verdict_labels", {}).get("A3", [])
            and route_schema.get("required_a0_control_count") == 7
            and route_schema.get("required_a1_control_count") == 6
            and route_schema.get("paired_provenance_fields") == ["source_commit", "code_commit", "source_lock.code_commit"]
            and route_schema.get("target_root_metric_keys") == [
                "correlation_metrics", "cutoff_drift", "eigenvalue_count", "extra_zero_count",
                "missing_zero_count", "precision_drift", "root_count_discrepancy", "root_location_error",
                "spacing_metrics", "spectral_fit", "target_coefficient_fit", "target_prime_data",
                "target_root_data", "target_zero_data", "unfolding_metrics", "zero_error_test",
                "zero_error_train", "zero_error_validation",
            ]
        ),
        "claim_scope": (
            claim.get("scope_label") == "FROZEN_FINITE_TYPED_PROJECTION_CONTRACT_ONLY"
            and claim.get("forbidden_claim_tokens") == [
                "universal projection impossibility",
                "universal selector nonexistence",
                "minimal collision witness",
                "prospective novelty credit",
                "cross-type primitive credit",
            ]
        ),
    }


def validate_raw_contract(packet: dict[str, Any]) -> dict[str, bool]:
    controls = packet.get("raw_control_input", {})
    inventories = packet.get("raw_primitive_inventories", [])
    inventory_hashes = {
        record.get("run_id"): fragment_digest(record)
        for record in inventories
        if isinstance(record, dict) and isinstance(record.get("run_id"), str)
    }
    expected_collisions = [
        {"witness_id": "W1", "left_word": [[1, 2]], "right_word": [[2, 1]]},
        {"witness_id": "W2", "left_word": [[1, 4]], "right_word": [[2, 2]]},
        {"witness_id": "W3", "left_word": [[2, 4]], "right_word": [[1, 1], [1, 2]]},
    ]
    return {
        "raw_inventory_exact_order_and_hashes": (
            [record.get("run_id") for record in inventories] == sorted(INVENTORY_RECORD_HASHES)
            and inventory_hashes == INVENTORY_RECORD_HASHES
        ),
        "raw_control_generator_exact": controls.get("generator") == {
            "name": "LCG31", "modulus": 2**31, "multiplier": 1103515245,
            "increment": 12345, "sequence_length_per_seed": 256,
        },
        "raw_control_seed_exact_map": controls.get("seeds") == SEEDS,
        "raw_control_sequences_exact": (
            set(controls.get("lcg_sequences", {})) == set(SEEDS)
            and all(controls["lcg_sequences"].get(name) == lcg(seed, 256) for name, seed in SEEDS.items())
        ),
        "raw_control_domains_exact": (
            controls.get("a0_family_ids") == [
                "shuffled_generated_primes", "matched_density_integers", "composites",
                "pseudoprimes", "randomized_labels", "neighboring_digits", "simpler_parent",
            ]
            and controls.get("a1_family_ids") == [
                "shuffled_periods", "random_weights", "random_phases",
                "same_density_lengths", "neighboring_digits", "simpler_parent",
            ]
            and controls.get("control_digits") == [1, 2]
            and controls.get("neighboring_control_digits") == [2, 3]
            and controls.get("control_pair_lengths") == [1, 2, 3]
            and controls.get("prototype_alphabet_sizes") == [2, 3, 4]
            and controls.get("prototype_pair_lengths") == [1, 2, 3, 4]
        ),
        "raw_type_contract_exact": packet.get("raw_type_input") == {
            "type_symbols": ["SigmaPrimitiveDigit", "RhoPrimitivePair", "PrimitiveClosedGeodesic"],
            "digit_space_symbol": "X=N^N", "digit_shift_symbol": "sigma",
            "pair_space_symbol": "X2=(N^2)^N", "pair_shift_symbol": "rho",
            "grouping_symbol": "iota", "grouping_block_size": 2,
            "return_map_digit_fixture": [1, 2, 3, 4, 5, 6, 7, 8],
            "reversal_pair_fixture": [[1, 2], [2, 3], [1, 4]],
            "parent_supplied_symbols": ["one_digit_gauss_branches", "L_s", "det(I-L_s^2)"],
            "paper40_new_symbol": "RhoPrimitivePair",
        },
        "raw_branch_contract_exact": packet.get("raw_branch_input") == {
            "matrix_templates": {"A": [["a", 1], [1, 0]], "B": [[0, 1], [1, "a"]], "J": [[0, 1], [1, 0]]},
            "stored_digits": [1, 2, 2, 3, 1, 4], "evaluation_point": [1, 4],
            "weight_exponent_s": 1, "raw_operator_nesting": "last_raw_branch_on_left",
        },
        "raw_collision_oriented_map_exact": packet.get("raw_collision_input") == expected_collisions,
        "raw_projection_contract_exact": (
            packet.get("projection_definition_input") == [
                {"projection_id": "P_t", "definition": "matrix_trace"},
                {"projection_id": "P_Delta", "definition": "matrix_trace_squared_minus_four"},
                {"projection_id": "P_N", "definition": "square_of_expanding_eigenvalue"},
            ]
            and packet.get("projection_criterion_schema") == {
                "criterion_ids": ["rational_integer_support", "clock", "repetition"],
                "norm_minimal_polynomial_template": "x^2-(t^2-2)x+1",
                "norm_root_selector": "larger_positive_root",
                "derivative_root_selector": "smaller_positive_root",
                "clock_marker_exponent_rule": "2*pair_length",
                "repetition_exponents": [2, 3, 4, 5, 6],
            }
        ),
        "raw_mayer_contract_exact": packet.get("mayer_source_input") == {
            "function_space_symbol": "A_infinity(D)", "disk_center_radius": [[1, 0], [3, 2]],
            "determinant_half_plane": "Re(s)>1/2", "euler_product_initial_half_plane": "Re(s)>1",
            "continuation_domain": "C", "local_u_domain": "formal_or_small_abs_u",
            "selberg_identity_u_value": 1,
            "source_log_coefficient_tokens": ["u^(2*k*r)", "d_w^(r*s)", "r", "1-d_w^r"],
            "target_log_coefficient_tokens": ["u^(2*k*r)", "p^(-r*s)", "r"],
        },
        "raw_ownership_contract_exact": packet.get("ownership_input") == {
            "declared_object_symbols": ["X", "X2", "sigma", "rho", "iota", "L_s", "det(I-L_s^2)"],
            "declared_untwisted_selector_symbols": [],
            "ownership_scope": "FROZEN_UNTWISTED_SCHEMA_ONLY",
            "positive_control_owner": {
                "control_role": "SYNTHETIC_POSITIVE_OWNER_CONTROL_NOT_SD_C42",
                "operator_matrix": [[2, 0], [0, 3]],
                "projector_matrix": [[1, 0], [0, 0]],
                "selected_indices": [0],
                "multiplicity": 1,
                "marker_stride": 2,
                "repetitions": [1, 2, 3, 4, 5, 6],
            },
            "scalar_postselection": {"full_inventory": [3, 4], "declared_projector": None},
        },
        "raw_row_contract_exact": packet.get("row_contract_input") == {
            "orientation_equivalence": "rotation_only",
            "reverse_quotient_rule": "metadata_only_no_reversal_quotient",
            "reversal_metadata_fields": [
                "orientation_id", "reverse_orientation_id", "reversal_orbit_id",
                "self_reversal", "reverse_class_present",
            ],
            "source_multiplicity": 1,
            "untwisted_sign": 1,
            "phase_modulus": 97,
            "phase_exponent": 0,
            "stability_denominator_token": "1-d_w^r",
        },
    }


def evaluate(packet: dict[str, Any], raw: bytes) -> dict[str, Any]:
    checks = validate_packet_shape(packet)
    if not all(checks.values()):
        return {
            "schema": "paper40-main-direct-evaluation-v2",
            "candidate_id": packet.get("candidate_id") if isinstance(packet, dict) else None,
            "source_packet_sha256": sha256(raw).hexdigest(),
            "algorithm": "RAW_WORD_ROTATION_FILTER_MATRIX_MULTIPLICATION_AND_DIRECT_CONTROLS",
            "reads_packet_bytes_only": True,
            "checks": dict(sorted(checks.items())),
            "check_count": len(checks),
            "failure_count": sum(not value for value in checks.values()),
            "all_pass": False,
            "science_projection": None,
        }
    checks.update(validate_static(packet))
    selection, extra = parse_and_select_cards(packet)
    checks.update(extra)
    checks.update(validate_raw_contract(packet))
    if not all(checks.values()):
        return {
            "schema": "paper40-main-direct-evaluation-v2",
            "candidate_id": packet.get("candidate_id"),
            "source_packet_sha256": sha256(raw).hexdigest(),
            "algorithm": "RAW_WORD_ROTATION_FILTER_MATRIX_MULTIPLICATION_AND_DIRECT_CONTROLS",
            "reads_packet_bytes_only": True,
            "checks": dict(sorted(checks.items())),
            "check_count": len(checks),
            "failure_count": sum(not value for value in checks.values()),
            "all_pass": False,
            "science_projection": None,
        }
    run_summaries, extra, inventories = verify_inventories(packet)
    checks.update(extra)
    base_by_length = {}
    for record in packet.get("raw_primitive_inventories", []):
        if record.get("run_id") in {"canonical_D2_k1", "canonical_D2_k2", "canonical_D2_k3", "canonical_D2_k4"}:
            base_by_length[int(record["pair_length"])] = [tuple(tuple(pair) for pair in word) for word in record["raw_words"]]
    base_words = inventories.get(("canonical", 2), [])
    neighbor_words = inventories.get(("neighboring", 2), [])
    controls, extra = derive_controls(packet, base_words[:30], neighbor_words[:30])
    checks.update(extra)
    typed, extra = derive_typed_bridge(packet, base_by_length)
    checks.update(extra)
    branch, extra = derive_branch(packet)
    checks.update(extra)
    typed.update(branch)
    collisions, extra = derive_collisions(packet)
    checks.update(extra)
    all_words = [word for key in sorted(inventories) for word in inventories[key]]
    projection_rows, extra = derive_projections(all_words, packet)
    checks.update(extra)
    mayer, ownership, extra = derive_boundaries(packet)
    checks.update(extra)
    registered_runs = len(run_summaries)
    scientific_rows = sum(run["primitive_pair_necklaces_total"] for run in run_summaries)
    theorem_failures = sum(sum(run["theorem_failures"].values()) for run in run_summaries)
    full_conjunction = any(row["rational_integer_support"] and row["clock"] and row["repetition"] for row in projection_rows)
    rational_prime_projection = any(row["rational_prime_selectivity"] for row in projection_rows)
    route_tuple = {
        "A0": "A0_WEAK_ARITHMETIC_RELATION" if all(controls["A0"].values()) else "A0_FAIL",
        "A1": "A1_PASS_ANALYTIC" if all(controls["A1"].values()) and typed["splitting_exact"] else "A1_FAIL",
        "A2": "A2_ANALYTIC_DETERMINANT" if checks["mayer_three_domains"] else "A2_FAIL",
        "A3": "A3_PARTIAL_ANALYTIC_STRUCTURE" if checks["mayer_local_u"] else "A3_FAIL",
        "A4": "A4_FORMAL_HINT" if any(row["projection"] == "P_N" and row["clock"] and row["repetition"] for row in projection_rows) else "A4_FAIL",
    }
    terminal_codes: list[str] = []
    if route_tuple["A1"] == "A1_PASS_ANALYTIC":
        terminal_codes.append("GO_MODULAR_PRIMITIVE_LEDGER")
    if route_tuple["A2"] == "A2_ANALYTIC_DETERMINANT":
        terminal_codes.append("GO_SAME_OBJECT_MAYER_DETERMINANT")
    if not rational_prime_projection:
        terminal_codes.append("STOP_CANONICAL_INTEGER_PROJECTION")
    if not full_conjunction:
        terminal_codes.append("STOP_RATIONAL_INTEGER_CLOCK_REPETITION_CONJUNCTION")
    if ownership["declared_selector_in_frozen_untwisted_schema"] is False:
        terminal_codes.append("STOP_OPERATOR_VISIBLE_SELECTOR_NOT_OWNED")
    overall = "ROUTE_A_REJECTED" if any(code.startswith("STOP_") for code in terminal_codes) else "ROUTE_A_ACCEPTED"
    if overall == "ROUTE_A_REJECTED":
        terminal_codes.append("ROUTE_A_REJECTED")
    checks.update({
        "registered_run_count": registered_runs == 6,
        "scientific_row_count": scientific_rows == 39622,
        "theorem_failure_count": theorem_failures == 0,
        "full_projection_conjunction_absent": full_conjunction is False,
        "route_tuple_derived": route_tuple == ROUTE_TUPLE,
        "terminal_set_derived": terminal_codes == TERMINALS,
        "overall_status_derived": overall == "ROUTE_A_REJECTED",
    })
    science = {
        "schema": "paper40-scientific-results-v2",
        "candidate_id": "SD-C42",
        "chronology": "RETROSPECTIVE_CHECKER_FROZEN_AUTHORITY_INTEGRATION",
        "selection": {
            "survivors": selection["survivors"],
            "selected": selection["winner"],
            "sd_c02_zero_orbit_counts_as_nonempty": True,
            "hidden_nontrivial_predicate": False,
        },
        "typed_bridge": typed,
        "collision_classes": collisions,
        "projection_rows": projection_rows,
        "full_projection_conjunction_exists": full_conjunction,
        "mayer_boundary": mayer,
        "ownership": ownership,
        "route": {"tuple": route_tuple, "overall": overall, "route_b_allowed": False, "terminal_codes": terminal_codes},
        "controls": {"a0": controls["A0"], "a1": controls["A1"], "a0_literal_families": 7, "a1_literal_families": 6},
        "prototype": {"runs": run_summaries, "registered_run_count": registered_runs, "scientific_row_count": scientific_rows, "theorem_failure_count": theorem_failures, "hard_status": "PASS" if registered_runs == 6 and scientific_rows == 39622 and theorem_failures == 0 else "FAIL"},
        "decision": {"route_a": "REJECTED" if overall == "ROUTE_A_REJECTED" else "ACCEPTED", "route_b": "LOCKED_NOT_INVOKED", "terminal": "STOP_RATIONAL_INTEGER_CLOCK_REPETITION_CONJUNCTION" if not full_conjunction else "NONE"},
        "claim_boundary": "FROZEN_FINITE_TYPED_PROJECTION_CONTRACT_ONLY",
    }
    result = {
        "schema": "paper40-main-direct-evaluation-v2",
        "candidate_id": "SD-C42",
        "source_packet_sha256": sha256(raw).hexdigest(),
        "algorithm": "RAW_WORD_ROTATION_FILTER_MATRIX_MULTIPLICATION_AND_DIRECT_CONTROLS",
        "reads_packet_bytes_only": True,
        "checks": dict(sorted(checks.items())),
        "check_count": len(checks),
        "failure_count": sum(not value for value in checks.values()),
        "all_pass": all(checks.values()),
        "science_projection": science,
    }
    return result


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: evaluate_packet.py SOURCE_PACKET.json")
    raw = Path(sys.argv[1]).read_bytes()
    packet = json.loads(raw)
    result = evaluate(packet, raw)
    sys.stdout.buffer.write(canonical_bytes(result))
    if not result["all_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
