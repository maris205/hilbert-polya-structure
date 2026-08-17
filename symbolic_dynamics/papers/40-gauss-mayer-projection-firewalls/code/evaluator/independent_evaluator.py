#!/usr/bin/env python3
"""Independent FKM/continuant evaluator for the raw SD-C42 packet.

No source, main-evaluator, packet-adapter, Route-renderer, or vendored
prototype module is imported or executed.
"""

from __future__ import annotations

from collections import Counter
from decimal import Decimal, localcontext
from fractions import Fraction
from hashlib import sha256
import itertools
import json
import math
from pathlib import Path
import sys
from typing import Any, Iterator

import yaml


ROUTE_SCHEMA_FIXTURE_SHA256 = "15e47752d6134ec7ddc8f36329a3f7139031122ead7a90af6b876840c1ac5bfa"
ROUTE_SKILL_SHA256 = "29bd6275aa0c80ecce9cca898f06687208475c0a9a40cf3b9592fde45951458a"
CARD_HASHES = {
    "SD-C01": "ee47a9c90c6bfbc54ba6b09b21f416dcece58b0d0ba9a391ca196d1b41d365a2",
    "SD-C02": "5b5e9a2fe33a0ba8d281cf59c8f5346b95033c655d258554c0f76f8cfa0a434f",
    "SD-C03": "2263b1c7bac4336628f444ded88e4e2ad98117f430113faf1ea5a91c16380328",
    "SD-C04": "0609076081ccd69e9ffa3e0f708d426a33f7d41e2884f90bb2792bbc90209a92",
    "SD-C05": "4a18295b1e20245c7196f21be4e4afc52857bf981efb461556720ab9e8ab5ed1",
    "SD-C06": "d93683662a0cbee8e07d79329477d8b60bb273fb72e4bd64c05847e09a576c1b",
}
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


def canonical_bytes(value: Any) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode("ascii")


def fragment_digest(value: Any) -> str:
    raw = (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True) + "\n").encode("ascii")
    return sha256(raw).hexdigest()


def aperiodic_necklace_indices(radix: int, size: int) -> Iterator[tuple[int, ...]]:
    digits = [0] * (size + 1)

    def visit(position: int, period: int) -> Iterator[tuple[int, ...]]:
        if position > size:
            if period == size:
                yield tuple(digits[1:])
            return
        digits[position] = digits[position - period]
        yield from visit(position + 1, period)
        for symbol in range(digits[position - period] + 1, radix):
            digits[position] = symbol
            yield from visit(position + 1, position)

    yield from visit(1, 1)


def independent_necklaces(digits: tuple[int, ...], length: int) -> list[PairWord]:
    alphabet = tuple(itertools.product(digits, repeat=2))
    return [tuple(alphabet[index] for index in indices) for indices in aperiodic_necklace_indices(len(alphabet), length)]


def primitive_word(word: tuple[Any, ...]) -> bool:
    return all(not (len(word) % period == 0 and word == word[:period] * (len(word) // period)) for period in range(1, len(word)))


def rotate_min(word: tuple[Any, ...]) -> tuple[Any, ...]:
    return min(word[index:] + word[:index] for index in range(len(word)))


def continuant(sequence: tuple[int, ...]) -> int:
    if not sequence:
        return 1
    old, current = 1, sequence[0]
    for value in sequence[1:]:
        old, current = current, value * current + old
    return current


def matrix_from_flat(flat: tuple[int, ...]) -> Matrix:
    if len(flat) == 1:
        return (flat[0], 1, 1, 0)
    return (continuant(flat), continuant(flat[:-1]), continuant(flat[1:]), continuant(flat[1:-1]))


def matrix_for_pairs(word: PairWord) -> Matrix:
    return matrix_from_flat(tuple(value for pair in word for value in pair))


def multiply(left: Matrix, right: Matrix) -> Matrix:
    return (
        left[0] * right[0] + left[1] * right[2],
        left[0] * right[1] + left[1] * right[3],
        left[2] * right[0] + left[3] * right[2],
        left[2] * right[1] + left[3] * right[3],
    )


def power(matrix: Matrix, exponent: int) -> Matrix:
    accumulator: Matrix = (1, 0, 0, 1)
    factor = matrix
    while exponent:
        if exponent & 1:
            accumulator = multiply(accumulator, factor)
        factor = multiply(factor, factor)
        exponent >>= 1
    return accumulator


def trial_prime(value: int) -> bool:
    if value <= 3:
        return value >= 2
    if value % 2 == 0 or value % 3 == 0:
        return False
    divisor = 5
    while divisor * divisor <= value:
        if value % divisor == 0 or value % (divisor + 2) == 0:
            return False
        divisor += 6
    return True


def pair_reverse(word: PairWord) -> PairWord:
    return tuple((right, left) for left, right in reversed(word))


def orientation(word: PairWord) -> str:
    return "|".join(f"{left},{right}" for left, right in word)


def verify_lcg(seed: int, sequence: list[int]) -> bool:
    state = seed % (2**31)
    for observed in sequence:
        state = (1103515245 * state + 12345) & ((1 << 31) - 1)
        if observed != state:
            return False
    return len(sequence) == 256


def permute(values: list[Any], sequence: list[int]) -> list[Any]:
    result = list(values)
    for cursor, index in enumerate(range(len(result) - 1, 0, -1)):
        target = sequence[cursor] % (index + 1)
        result[index], result[target] = result[target], result[index]
    if result == values and len(result) > 1:
        result = result[1:] + result[:1]
    return result


def generate_primes(amount: int) -> list[int]:
    result = []
    value = 2
    while len(result) < amount:
        if trial_prime(value):
            result.append(value)
        value += 1
    return result


def generate_pseudoprimes(amount: int) -> list[int]:
    result = []
    value = 3
    while len(result) < amount:
        if not trial_prime(value) and pow(2, value - 1, value) == 1:
            result.append(value)
        value += 2
    return result


def conditioned_numbers(sequence: list[int], amount: int, want_prime: bool) -> list[int]:
    output = []
    seen: set[int] = set()
    for state in sequence:
        value = 2 + state % 9991
        if value not in seen and trial_prime(value) is want_prime:
            seen.add(value)
            output.append(value)
            if len(output) == amount:
                return output
    return output


def exact_roof(tr: int) -> str:
    with localcontext() as context:
        context.prec = 70
        discriminant = Decimal(tr * tr - 4)
        expanding = (Decimal(tr) + discriminant.sqrt()) / Decimal(2)
        return format(Decimal(2) * expanding.ln(), ".60f")


def nested(mapping: dict[str, Any], *path: str) -> Any:
    value: Any = mapping
    for key in path:
        value = value[key]
    return value


def exact_keys(value: Any, expected: set[str]) -> bool:
    return isinstance(value, dict) and set(value) == expected


def exact_int(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def string_list(value: Any) -> bool:
    return isinstance(value, list) and all(isinstance(item, str) for item in value)


def independent_shape(packet: Any) -> dict[str, bool]:
    top = {
        "candidate_id", "chronology_input", "claim_scope_input", "experiment_freeze_input",
        "mayer_source_input", "ownership_input", "projection_criterion_schema",
        "projection_definition_input", "prototype_reproduction_input", "raw_branch_input",
        "raw_collision_input", "raw_control_input", "raw_primitive_inventories",
        "raw_type_input", "research_input", "route_card_bytes", "route_schema_input", "row_contract_input",
        "schema", "selection_rule_schema",
    }
    checks = {"shape_top_exact": exact_keys(packet, top)}
    if not checks["shape_top_exact"]:
        return checks
    expected_nested = {
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
    checks.update({f"shape_{name}": exact_keys(packet[name], keys) for name, keys in expected_nested.items()})
    checks["shape_cards"] = isinstance(packet["route_card_bytes"], list) and all(exact_keys(item, {"card_id", "historical_byte_sha256", "raw_yaml_utf8", "relative_path", "vendored_byte_sha256"}) and all(isinstance(value, str) for value in item.values()) for item in packet["route_card_bytes"])
    checks["shape_projection_definitions"] = isinstance(packet["projection_definition_input"], list) and all(exact_keys(item, {"definition", "projection_id"}) and all(isinstance(value, str) for value in item.values()) for item in packet["projection_definition_input"])
    checks["shape_collisions"] = isinstance(packet["raw_collision_input"], list) and all(exact_keys(item, {"left_word", "right_word", "witness_id"}) and isinstance(item["witness_id"], str) and all(isinstance(word, list) and word and all(isinstance(pair, list) and len(pair) == 2 and all(exact_int(value) for value in pair) for pair in word) for word in (item["left_word"], item["right_word"])) for item in packet["raw_collision_input"])
    checks["shape_inventories"] = isinstance(packet["raw_primitive_inventories"], list) and all(
        exact_keys(item, {"alphabet_size", "digits", "family", "pair_length", "raw_words", "run_id"})
        and exact_int(item["alphabet_size"]) and exact_int(item["pair_length"])
        and isinstance(item["family"], str) and isinstance(item["run_id"], str)
        and isinstance(item["digits"], list) and all(exact_int(value) for value in item["digits"])
        and isinstance(item["raw_words"], list) and all(isinstance(word, list) and all(isinstance(pair, list) and len(pair) == 2 and all(exact_int(value) for value in pair) for pair in word) for word in item["raw_words"])
        for item in packet["raw_primitive_inventories"]
    )
    controls = packet["raw_control_input"]
    checks["shape_generator"] = exact_keys(controls.get("generator"), {"increment", "modulus", "multiplier", "name", "sequence_length_per_seed"}) and isinstance(controls["generator"].get("name"), str) and all(exact_int(controls["generator"].get(key)) for key in ("increment", "modulus", "multiplier", "sequence_length_per_seed"))
    checks["shape_seeds"] = isinstance(controls.get("seeds"), dict) and all(isinstance(key, str) and exact_int(value) for key, value in controls["seeds"].items())
    checks["shape_sequences"] = isinstance(controls.get("lcg_sequences"), dict) and all(isinstance(key, str) and isinstance(values, list) and all(exact_int(value) for value in values) for key, values in controls["lcg_sequences"].items())
    checks["shape_control_lists"] = all(string_list(controls.get(name)) for name in ("a0_family_ids", "a1_family_ids")) and all(isinstance(controls.get(name), list) and all(exact_int(value) for value in controls[name]) for name in ("control_digits", "control_pair_lengths", "neighboring_control_digits", "prototype_alphabet_sizes", "prototype_pair_lengths"))
    route = packet["route_schema_input"]
    checks["shape_route_schema_fixture"] = (
        isinstance(route.get("schema_fixture"), dict)
        and isinstance(route.get("schema_fixture_path"), str)
        and isinstance(route.get("schema_fixture_sha256"), str)
        and isinstance(route.get("expected_schema_fixture_sha256"), str)
    )
    checks["shape_route_lists"] = all(string_list(route.get(name)) for name in ("criterion_order", "paired_provenance_fields", "target_root_metric_keys")) and exact_int(route.get("required_a0_control_count")) and exact_int(route.get("required_a1_control_count"))
    owner = packet["ownership_input"]
    checks["shape_positive_owner"] = (
        exact_keys(owner.get("positive_control_owner"), {"control_role", "marker_stride", "multiplicity", "operator_matrix", "projector_matrix", "repetitions", "selected_indices"})
        and exact_keys(owner.get("scalar_postselection"), {"declared_projector", "full_inventory"})
    )
    checks["shape_route_skill"] = all(
        isinstance(route.get(name), str)
        for name in ("skill_artifact_encoding", "skill_artifact_path", "skill_byte_sha256", "expected_skill_byte_sha256", "skill_utf8")
    )
    checks["shape_research_maps"] = all(isinstance(packet["research_input"].get(name), dict) and all(isinstance(key, str) and isinstance(value, str) for key, value in packet["research_input"][name].items()) for name in ("dependent_seal_hashes", "expected_immutable_file_hashes", "immutable_file_hashes"))
    return checks


def independent_selection(packet: dict[str, Any]) -> tuple[dict[str, Any], dict[str, bool]]:
    checks = {"card_record_count": len(packet.get("route_card_bytes", [])) == 6}
    record_ids = [record.get("card_id") for record in packet.get("route_card_bytes", [])]
    checks["card_exact_unique_order"] = record_ids == sorted(CARD_HASHES) and len(set(record_ids)) == 6
    cards: dict[str, dict[str, Any]] = {}
    for record in packet.get("route_card_bytes", []):
        card_id = record.get("card_id")
        text = record.get("raw_yaml_utf8")
        valid = card_id in CARD_HASHES and isinstance(text, str)
        if valid:
            raw_hash = sha256(text.encode()).hexdigest()
            valid = raw_hash == CARD_HASHES[card_id] == record.get("historical_byte_sha256") == record.get("vendored_byte_sha256")
        try:
            parsed = yaml.safe_load(text) if valid else None
        except yaml.YAMLError:
            parsed = None
        valid = valid and isinstance(parsed, dict) and parsed.get("candidate_id") == card_id
        checks[f"card_{card_id}"] = bool(valid)
        if valid:
            cards[card_id] = parsed
    rows = []
    for card_id in sorted(cards):
        card = cards[card_id]
        if card_id == "SD-C01":
            nonempty = nested(card, "a1", "metrics", "all_repetition_checks_pass") is True
        elif card_id == "SD-C02":
            nonempty = nested(card, "a1", "metrics", "fixed_points_every_period") == 1 and "one period-1 zero orbit" == nested(card, "a1", "metrics", "primitive_orbits")
        elif card_id == "SD-C03":
            nonempty = nested(card, "a1", "strongest_evidence") == "The renewal graph has an exact primitive-necklace and repetition expansion for its own return atoms."
        elif card_id == "SD-C04":
            nonempty = nested(card, "a1", "metrics", "primitive_necklaces_max_cutoff") == 63319
        elif card_id == "SD-C05":
            nonempty = nested(card, "a1", "metrics", "directed_cycles") > 0
        else:
            nonempty = nested(card, "a1", "evidence_status") == "PROVED"
        a2 = card["a2"]
        determinant_ok = a2["evidence_status"] == "PROVED" and a2["verdict"] == "A2_ANALYTIC_DETERMINANT"
        rows.append({
            "candidate_id": card_id,
            "nonempty_intrinsic_ledger": nonempty,
            "same_object_determinant": determinant_ok,
            "survivor": nonempty and determinant_ok,
            "A3": card["a3"]["verdict"],
            "A4": card["a4"]["verdict"],
        })
    survivors = [row["candidate_id"] for row in rows if row["survivor"]]
    ranks3 = {"A3_FAIL": 0, "A3_PARTIAL_ANALYTIC_STRUCTURE": 1, "A3_CONTROLLED_CONTINUATION": 2, "A3_EXACT_DIVISOR_MATCH": 3}
    ranks4 = {"A4_FAIL": 0, "A4_FORMAL_HINT": 1, "A4_NATURAL_QUANTIZATION": 2}
    winner = sorted(
        [row for row in rows if row["survivor"]],
        key=lambda row: (ranks3.get(row["A3"], -1), ranks4.get(row["A4"], -1)),
        reverse=True,
    )[0]["candidate_id"] if survivors else None
    checks["survivors"] = survivors == ["SD-C01", "SD-C02", "SD-C04"]
    checks["c02_nonempty"] = any(row["candidate_id"] == "SD-C02" and row["nonempty_intrinsic_ledger"] for row in rows)
    checks["winner"] = winner == "SD-C04"
    return {"rows": rows, "survivors": survivors, "winner": winner}, checks


def decode_inventories(packet: dict[str, Any]) -> tuple[dict[tuple[str, int], dict[int, list[PairWord]]], dict[str, bool]]:
    checks = {"inventory_count": len(packet.get("raw_primitive_inventories", [])) == 24}
    grouped: dict[tuple[str, int], dict[int, list[PairWord]]] = {}
    for record in packet.get("raw_primitive_inventories", []):
        family = record.get("family")
        size = record.get("alphabet_size")
        length = record.get("pair_length")
        digits = tuple(record.get("digits", []))
        key = (family, size)
        expected_digits = tuple(range(1 if family == "canonical" else 2, (1 if family == "canonical" else 2) + size)) if family in {"canonical", "neighboring"} and isinstance(size, int) else ()
        words = [tuple(tuple(pair) for pair in word) for word in record.get("raw_words", [])]
        expected = independent_necklaces(digits, length) if isinstance(length, int) else []
        run_id = f"{family}_D{size}_k{length}"
        checks[f"inventory_{run_id}_schema"] = record.get("run_id") == run_id and digits == expected_digits and length in {1, 2, 3, 4}
        checks[f"inventory_{run_id}_fkm_exact"] = words == expected
        grouped.setdefault(key, {})[length] = words
    return grouped, checks


def independent_run(digits: tuple[int, ...], family: str, inventories: dict[int, list[PairWord]]) -> dict[str, Any]:
    all_words = [word for length in (1, 2, 3, 4) for word in inventories[length]]
    orientation_ids = {orientation(word) for word in all_words}
    failures: Counter[str] = Counter()
    trace_sizes: Counter[int] = Counter()
    trace_prime = 0
    delta_prime = 0
    delta_nonboundary = 0
    rows = []
    for length in (1, 2, 3, 4):
        for word in inventories[length]:
            matrix = matrix_for_pairs(word)
            tr = matrix[0] + matrix[3]
            det = matrix[0] * matrix[3] - matrix[1] * matrix[2]
            delta = tr * tr - 4
            failures["determinant_one"] += int(det != 1)
            failures["trace_at_least_three"] += int(tr < 3)
            failures["order_discriminant_factorization"] += int(delta != (tr - 2) * (tr + 2))
            failures["nonsquare_interval"] += int(not ((tr - 1) ** 2 < delta < tr * tr))
            failures["order_discriminant_nonsquare"] += int(math.isqrt(delta) ** 2 == delta)
            failures["clock_strict_inequality_certificate"] += int(not (delta > (tr - 2) ** 2 and (tr - 1) ** 2 > tr))
            previous, current = 2, tr
            for exponent in range(2, 7):
                expected = tr * current - previous
                powered = power(matrix, exponent)
                failures["trace_power_recurrence"] += int(powered[0] + powered[3] != expected)
                previous, current = current, expected
            square = power(matrix, 2)
            failures["trace_square_mismatch"] += int(square[0] + square[3] == tr * tr)
            trace_prime += int(trial_prime(tr))
            prime_delta = trial_prime(delta)
            delta_prime += int(prime_delta)
            delta_nonboundary += int(prime_delta and (tr, delta) != (3, 5))
            trace_sizes[tr] += 1
            reverse = rotate_min(pair_reverse(word))
            own = orientation(word)
            reverse_id = orientation(reverse)
            rows.append({
                "delta_order": delta, "determinant": det, "matrix": list(matrix),
                "pair_length": length, "trace": tr, "word": [[a, b] for a, b in word],
                "orientation_id": own, "reverse_orientation_id": reverse_id,
                "reversal_orbit_id": min(own, reverse_id), "self_reversal": own == reverse_id,
                "reverse_class_present": reverse_id in orientation_ids, "source_multiplicity": 1,
                "untwisted_sign": 1, "phase_exponent_mod_97": 0,
                "expanding_eigenvalue_minpoly": [1, -tr, 1],
                "geodesic_norm_minpoly": [1, -(tr * tr - 2), 1],
                "derivative_multiplier_minpoly": [1, -(tr * tr - 2), 1],
                "norm_qsqrt_coefficients": [[tr * tr - 2, 2], [tr, 2]],
                "derivative_qsqrt_coefficients": [[tr * tr - 2, 2], [-tr, 2]],
                "marker_exponent_per_repetition": 2 * length,
            })
    rows.sort(key=lambda row: (row["pair_length"], row["word"], row["matrix"]))
    row_hash = sha256(json.dumps(rows, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("ascii")).hexdigest()
    collisions = [amount for amount in trace_sizes.values() if amount > 1]
    return {
        "alphabet_label": f"{family}_D{len(digits)}", "digits": list(digits),
        "pair_alphabet_size": len(digits) ** 2,
        "primitive_pair_necklaces_by_length": {str(length): len(inventories[length]) for length in (1, 2, 3, 4)},
        "primitive_pair_necklaces_total": len(rows),
        "theorem_failures": {key: value for key, value in sorted(failures.items()) if value},
        "trace_prime_orbit_count": trace_prime, "trace_composite_orbit_count": len(rows) - trace_prime,
        "order_discriminant_prime_orbit_count": delta_prime,
        "order_discriminant_prime_nonboundary_count": delta_nonboundary,
        "trace_collision_group_count": len(collisions),
        "trace_collision_orbit_excess": sum(amount - 1 for amount in collisions),
        "scientific_rows_sha256": row_hash,
    }


def independent_controls(packet: dict[str, Any], base: list[PairWord], neighbor: list[PairWord]) -> tuple[dict[str, Any], dict[str, bool]]:
    raw = packet.get("raw_control_input", {})
    sequences = raw.get("lcg_sequences", {})
    seeds = raw.get("seeds", {})
    checks = {
        "control_schema": raw.get("generator") == {"name": "LCG31", "modulus": 2**31, "multiplier": 1103515245, "increment": 12345, "sequence_length_per_seed": 256},
        "a0_names": raw.get("a0_family_ids") == ["shuffled_generated_primes", "matched_density_integers", "composites", "pseudoprimes", "randomized_labels", "neighboring_digits", "simpler_parent"],
        "a1_names": raw.get("a1_family_ids") == ["shuffled_periods", "random_weights", "random_phases", "same_density_lengths", "neighboring_digits", "simpler_parent"],
        "seed_map": seeds == SEEDS,
        "sequence_keyset": sorted(sequences) == sorted(SEEDS),
        "grid": raw.get("control_digits") == [1, 2] and raw.get("neighboring_control_digits") == [2, 3] and raw.get("control_pair_lengths") == [1, 2, 3] and raw.get("prototype_alphabet_sizes") == [2, 3, 4] and raw.get("prototype_pair_lengths") == [1, 2, 3, 4],
    }
    for name, seed in seeds.items():
        checks[f"sequence_{name}"] = verify_lcg(seed, sequences.get(name, []))
    primes = generate_primes(30)
    shuffled = permute(primes, sequences["a0_shuffled_primes"])
    base_traces = [matrix_for_pairs(word)[0] + matrix_for_pairs(word)[3] for word in base]
    prime_count = sum(trial_prime(value) for value in base_traces)
    matched = permute(
        conditioned_numbers(sequences["a0_matched_density"], prime_count, True)
        + conditioned_numbers(sequences["a0_composites"], len(base) - prime_count, False),
        sequences["a0_pseudoprimes"],
    )
    composites = conditioned_numbers(sequences["a0_composites"], len(base), False)
    pseudos = permute(generate_pseudoprimes(30), sequences["a0_pseudoprimes"])
    randomized = permute(base_traces, sequences["a0_randomized_labels"])
    periods = [exact_roof(value) for value in base_traces]
    shuffled_periods = permute(periods, sequences["a1_shuffled_periods"])
    weights = []
    for value in sequences["a1_random_weights"][:len(base)]:
        numerator = value % 2001 - 1000
        weights.append(1 if numerator == 0 else numerator)
    phases = [1 + value % 96 for value in sequences["a1_random_phases"][:len(base)]]
    denominator = 1_000_003
    source_bins = [int(Decimal(period) // Decimal(2)) for period in periods]
    lengths = [
        (2 * bin_index * denominator + 1 + value % (2 * denominator - 1), denominator)
        for bin_index, value in zip(source_bins, sequences["a1_same_density_lengths"], strict=False)
    ][:len(base)]
    random_bins = [int(Fraction(numerator, den) // 2) for numerator, den in lengths]
    parent = []
    for length in (1, 2, 3):
        parent.extend(tuple(word) for word in itertools.product((1, 2), repeat=length) if primitive_word(tuple(word)) and tuple(word) == rotate_min(tuple(word)))
    a0 = {
        "shuffled_generated_primes": shuffled != primes and all(trial_prime(value) for value in shuffled),
        "matched_density_integers": len(matched) == len(base) and sum(trial_prime(value) for value in matched) == prime_count,
        "composites": len(composites) == 30 and not any(trial_prime(value) for value in composites),
        "pseudoprimes": len(pseudos) == 30 and all(not trial_prime(value) and pow(2, value - 1, value) == 1 for value in pseudos),
        "randomized_labels": randomized != base_traces and Counter(randomized) == Counter(base_traces),
        "neighboring_digits": len(neighbor) == len(base) and [sum((lambda matrix: (matrix[0], matrix[3]))(matrix_for_pairs(word))) for word in neighbor] != base_traces,
        "simpler_parent": len(parent) > 0 and all(not isinstance(word[0], tuple) for word in parent),
    }
    a1 = {
        "shuffled_periods": shuffled_periods != periods and Counter(shuffled_periods) == Counter(periods),
        "random_weights": len(weights) == len(base) and all(value != 1009 for value in weights),
        "random_phases": len(phases) == len(base) and all(1 <= value < 97 for value in phases) and len(set(phases)) > 1,
        "same_density_lengths": len(lengths) == len(base) and Counter(random_bins) == Counter(source_bins) and all(Fraction(numerator, den) > 0 for numerator, den in lengths),
        "neighboring_digits": len(neighbor) == len(base) and neighbor != base,
        "simpler_parent": len(parent) > 0,
    }
    checks.update({f"a0_{key}": value for key, value in a0.items()})
    checks.update({f"a1_{key}": value for key, value in a1.items()})
    return {"A0": a0, "A1": a1}, checks


def independent_type_branch(packet: dict[str, Any], base: dict[int, list[PairWord]]) -> tuple[dict[str, Any], dict[str, bool]]:
    raw_type = packet.get("raw_type_input", {})
    digits = tuple(raw_type.get("return_map_digit_fixture", []))
    grouped = tuple(zip(digits[::2], digits[1::2]))
    conjugacy = grouped[1:] == tuple(zip(digits[2::2], digits[3::2]))
    wrong_shift = grouped[2:] != grouped[1:]
    pair_fixture = tuple(tuple(pair) for pair in raw_type.get("reversal_pair_fixture", []))
    reverse_flat = tuple(reversed(tuple(value for pair in pair_fixture for value in pair)))
    reverse_regrouped = tuple(zip(reverse_flat[::2], reverse_flat[1::2]))
    reversal_ok = reverse_regrouped == pair_reverse(pair_fixture)
    digit_counts = {length: len(tuple(aperiodic_necklace_indices(2, length))) for length in range(1, 7)}
    pair_counts = {length: len(base[length]) for length in (1, 2, 3)}
    predicted = {length: 2 * digit_counts[2 * length] + (digit_counts[length] if length & 1 else 0) for length in (1, 2, 3)}
    raw_branch = packet.get("raw_branch_input", {})
    stored = tuple(raw_branch.get("stored_digits", []))
    branch_b = lambda digit: (0, 1, 1, digit)
    matrix: Matrix = (1, 0, 0, 1)
    for digit in stored:
        matrix = multiply(matrix, branch_b(digit))
    matrix_a = matrix_from_flat(stored)
    j: Matrix = (0, 1, 1, 0)
    z = Fraction(*raw_branch.get("evaluation_point", [0, 1]))
    def nested_branch(indices: tuple[int, ...]) -> tuple[Fraction, Fraction]:
        point = z
        weight = Fraction(1)
        for digit in indices:
            denominator = digit + point
            point = 1 / denominator
            weight /= denominator**2
        return point, weight
    correct = nested_branch(tuple(reversed(stored)))
    wrong = nested_branch(stored)
    checks = {
        "type_schema": (
            raw_type.get("type_symbols") == ["SigmaPrimitiveDigit", "RhoPrimitivePair", "PrimitiveClosedGeodesic"]
            and raw_type.get("digit_space_symbol") == "X=N^N" and raw_type.get("digit_shift_symbol") == "sigma"
            and raw_type.get("pair_space_symbol") == "X2=(N^2)^N" and raw_type.get("pair_shift_symbol") == "rho"
            and raw_type.get("grouping_symbol") == "iota" and raw_type.get("grouping_block_size") == 2
            and raw_type.get("return_map_digit_fixture") == [1, 2, 3, 4, 5, 6, 7, 8]
            and raw_type.get("reversal_pair_fixture") == [[1, 2], [2, 3], [1, 4]]
            and raw_type.get("parent_supplied_symbols") == ["one_digit_gauss_branches", "L_s", "det(I-L_s^2)"]
            and raw_type.get("paper40_new_symbol") == "RhoPrimitivePair"
        ),
        "grouping_conjugacy": conjugacy and wrong_shift,
        "reversal": reversal_ok and primitive_word(pair_fixture) == primitive_word(pair_reverse(pair_fixture)),
        "splitting": pair_counts == predicted == {1: 4, 2: 6, 3: 20},
        "flattened_22": primitive_word(((2, 2),)) and not primitive_word((2, 2)),
        "branch_schema": (
            raw_branch.get("raw_operator_nesting") == "last_raw_branch_on_left"
            and raw_branch.get("weight_exponent_s") == 1
            and raw_branch.get("matrix_templates") == {"A": [["a", 1], [1, 0]], "B": [[0, 1], [1, "a"]], "J": [[0, 1], [1, 0]]}
            and raw_branch.get("stored_digits") == [1, 2, 2, 3, 1, 4]
            and raw_branch.get("evaluation_point") == [1, 4]
        ),
        "branch_conjugacy": matrix_a == multiply(multiply(j, matrix), j),
        "branch_matrix": matrix == (22, 105, 31, 148),
        "branch_value_weight": correct == (Fraction(442, 623), Fraction(16, 388129)),
        "wrong_order_rejected": wrong == (Fraction(146, 697), Fraction(16, 485809)) and wrong != correct,
    }
    return {
        "digit_space": "X=N^N", "pair_space": "X2=(N^2)^N",
        "conjugacy": "rho(iota(x))=iota(sigma^2(x))",
        "return_map_typing_exact": conjugacy and reversal_ok,
        "pair_counts_D2_k1_to_k3": [pair_counts[index] for index in (1, 2, 3)],
        "splitting_exact": pair_counts == predicted,
        "branch_order_exact": correct != wrong and checks["branch_conjugacy"],
        "branch_value": [correct[0].numerator, correct[0].denominator],
        "branch_weight": [correct[1].numerator, correct[1].denominator],
        "wrong_same_index_value": [wrong[0].numerator, wrong[0].denominator],
        "wrong_same_index_weight": [wrong[1].numerator, wrong[1].denominator],
    }, checks


def independent_collisions(packet: dict[str, Any]) -> tuple[list[dict[str, Any]], dict[str, bool]]:
    output = []
    checks = {
        "collision_count": len(packet.get("raw_collision_input", [])) == 3,
        "collision_id_order": [item.get("witness_id") for item in packet.get("raw_collision_input", [])] == ["W1", "W2", "W3"],
    }
    mapping = {(4, False, True): "TRACE4_REVERSAL", (6, False, False): "TRACE6_NONREVERSAL", (10, True, False): "TRACE10_CROSS_LENGTH_NONREVERSAL"}
    for item in packet.get("raw_collision_input", []):
        left = tuple(tuple(pair) for pair in item.get("left_word", []))
        right = tuple(tuple(pair) for pair in item.get("right_word", []))
        lm, rm = matrix_for_pairs(left), matrix_for_pairs(right)
        lt, rt = lm[0] + lm[3], rm[0] + rm[3]
        reverse = rotate_min(pair_reverse(left)) == rotate_min(right)
        key = (lt, len(left) != len(right), reverse)
        exact = primitive_word(left) and primitive_word(right) and rotate_min(left) == left and rotate_min(right) == right and lt == rt and lm[0] * lm[3] - lm[1] * lm[2] == rm[0] * rm[3] - rm[1] * rm[2] == 1 and orientation(left) != orientation(right)
        witness_id = item.get("witness_id")
        expected = COLLISION_WITNESSES.get(witness_id)
        checks[f"collision_{witness_id}_exact_raw_binding"] = (
            expected is not None and left == expected[0] and right == expected[1]
        )
        checks[f"collision_{witness_id}_derived_class"] = (
            exact and expected is not None and mapping.get(key) == expected[2]
        )
        output.append({"id": mapping.get(key), "trace": lt, "cross_pair_length": key[1], "digit_reversal_related": reverse})
    return output, checks


def qmultiply(left: tuple[Fraction, Fraction], right: tuple[Fraction, Fraction], radicand: int) -> tuple[Fraction, Fraction]:
    return (left[0] * right[0] + left[1] * right[1] * radicand, left[0] * right[1] + left[1] * right[0])


def qpower(value: tuple[Fraction, Fraction], exponent: int, radicand: int) -> tuple[Fraction, Fraction]:
    result = (Fraction(1), Fraction(0))
    factor = value
    while exponent:
        if exponent & 1:
            result = qmultiply(result, factor, radicand)
        factor = qmultiply(factor, factor, radicand)
        exponent >>= 1
    return result


def independent_projections(words: list[PairWord], packet: dict[str, Any]) -> tuple[list[dict[str, Any]], dict[str, bool]]:
    matrices = [matrix_for_pairs(word) for word in words]
    traces = [matrix[0] + matrix[3] for matrix in matrices]
    deltas = [tr * tr - 4 for tr in traces]
    schema = packet.get("projection_criterion_schema", {})
    exponents = schema.get("repetition_exponents", [])
    trace_power_failure = all((lambda p, t, e: p[0] + p[3] != t**e)(power(matrix, exponent), tr, exponent) for matrix, tr in zip(matrices, traces, strict=True) for exponent in exponents)
    delta_power_failure = all((lambda p, d, e: (p[0] + p[3]) ** 2 - 4 != d**e)(power(matrix, exponent), delta, exponent) for matrix, delta in zip(matrices, deltas, strict=True) for exponent in exponents)
    nonsquare = all(math.isqrt(delta) ** 2 != delta for delta in deltas)
    algebra = True
    selectors = True
    norm_powers = True
    for matrix, tr, delta in zip(matrices, traces, deltas, strict=True):
        norm = (Fraction(tr * tr - 2, 2), Fraction(tr, 2))
        reciprocal = (norm[0], -norm[1])
        algebra = algebra and qmultiply(norm, reciprocal, delta) == (Fraction(1), Fraction(0))
        selectors = selectors and delta > 0 and norm[0] > 1 and norm[1] > 0 and reciprocal[0] > 0 and reciprocal[1] < 0
        for exponent in exponents:
            norm_power = qpower(norm, exponent, delta)
            reciprocal_power = qpower(reciprocal, exponent, delta)
            powered = power(matrix, exponent)
            powered_trace = powered[0] + powered[3]
            norm_powers = norm_powers and qmultiply(norm_power, reciprocal_power, delta) == (Fraction(1), Fraction(0)) and norm_power[0] + reciprocal_power[0] == Fraction(powered_trace * powered_trace - 2) and norm_power[1] + reciprocal_power[1] == 0
    clock_norm = algebra and selectors
    prime_selectivity = {
        "P_t": all(trial_prime(value) for value in traces) and len(set(traces)) == len(traces),
        "P_Delta": all(trial_prime(value) for value in deltas) and len(set(deltas)) == len(deltas),
        "P_N": False,
    }
    rows = [
        {"projection": "P_t", "rational_integer_support": True, "rational_prime_selectivity": prime_selectivity["P_t"], "clock": False if nonsquare else True, "repetition": not trace_power_failure},
        {"projection": "P_Delta", "rational_integer_support": True, "rational_prime_selectivity": prime_selectivity["P_Delta"], "clock": False if nonsquare else True, "repetition": not delta_power_failure},
        {"projection": "P_N", "rational_integer_support": not nonsquare, "rational_prime_selectivity": prime_selectivity["P_N"], "clock": clock_norm, "repetition": norm_powers},
    ]
    checks = {
        "projection_definitions": packet.get("projection_definition_input") == [
            {"projection_id": "P_t", "definition": "matrix_trace"},
            {"projection_id": "P_Delta", "definition": "matrix_trace_squared_minus_four"},
            {"projection_id": "P_N", "definition": "square_of_expanding_eigenvalue"},
        ],
        "projection_schema": schema.get("criterion_ids") == ["rational_integer_support", "clock", "repetition"] and schema.get("norm_minimal_polynomial_template") == "x^2-(t^2-2)x+1" and schema.get("norm_root_selector") == "larger_positive_root" and schema.get("derivative_root_selector") == "smaller_positive_root" and schema.get("clock_marker_exponent_rule") == "2*pair_length" and exponents == [2, 3, 4, 5, 6],
        "trace_power_failure": trace_power_failure, "delta_power_failure": delta_power_failure,
        "norm_irrational": nonsquare, "qsqrt_algebra": algebra,
        "root_selectors": selectors, "clock_T_log_PN": clock_norm, "norm_matrix_powers": norm_powers,
        "rational_prime_selectivity": not any(prime_selectivity.values()),
        "truth_matrix": rows == [
            {"projection": "P_t", "rational_integer_support": True, "rational_prime_selectivity": False, "clock": False, "repetition": False},
            {"projection": "P_Delta", "rational_integer_support": True, "rational_prime_selectivity": False, "clock": False, "repetition": False},
            {"projection": "P_N", "rational_integer_support": False, "rational_prime_selectivity": False, "clock": True, "repetition": True},
        ],
    }
    return rows, checks


def independent_boundaries(packet: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any], dict[str, bool]]:
    mayer = packet.get("mayer_source_input", {})
    owner = packet.get("ownership_input", {})
    positive = owner.get("positive_control_owner", {})
    scalar = owner.get("scalar_postselection", {})
    rows = packet.get("row_contract_input", {})
    operator = positive.get("operator_matrix")
    projector = positive.get("projector_matrix")

    def valid_matrix(value: Any) -> bool:
        if not isinstance(value, list) or not value:
            return False
        width = len(value)
        return all(
            isinstance(line, list) and len(line) == width
            and all(exact_int(entry) for entry in line)
            for line in value
        )

    def independent_product(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
        columns = list(zip(*right))
        return [[sum(a * b for a, b in zip(line, column)) for column in columns] for line in left]

    selected = positive.get("selected_indices")
    repetitions = positive.get("repetitions")
    dimensions = (
        valid_matrix(operator) and valid_matrix(projector) and len(operator) == len(projector)
        and isinstance(selected, list) and bool(selected)
        and all(exact_int(index) and index in range(len(operator)) for index in selected)
        and isinstance(repetitions, list) and repetitions == [1, 2, 3, 4, 5, 6]
    )
    projector_square = commuting = trace_identity = marker_identity = full_marker_identity = repeated_markers = False
    selected_trace_values: list[int] = []
    full_trace_values: list[int] = []
    if dimensions:
        projector_square = independent_product(projector, projector) == projector
        commuting = independent_product(projector, operator) == independent_product(operator, projector)
        running = [[int(i == j) for j in range(len(operator))] for i in range(len(operator))]
        restricted_values: list[int] = []
        for exponent in repetitions:
            running = independent_product(running, operator)
            projected = independent_product(projector, running)
            selected_trace_values.append(sum(projected[index][index] for index in range(len(operator))))
            restricted_values.append(sum(running[index][index] for index in selected))
            full_trace_values.append(sum(running[index][index] for index in range(len(operator))))
        trace_identity = selected_trace_values == restricted_values == [2 ** exponent for exponent in repetitions]
        stride = positive.get("marker_stride")
        restricted_operator = [[operator[i][j] for j in selected] for i in selected]
        marker_coefficients = [1, -restricted_operator[0][0]] if len(restricted_operator) == 1 else []
        marker_identity = (
            exact_int(stride) and marker_coefficients == [1, -2]
            and {stride * degree for degree, coefficient in enumerate(marker_coefficients) if coefficient} == {0, 2}
        )
        if len(operator) == 2:
            full_coefficients = [
                1,
                -(operator[0][0] + operator[1][1]),
                operator[0][0] * operator[1][1] - operator[0][1] * operator[1][0],
            ]
            full_marker_identity = (
                exact_int(stride)
                and full_coefficients == [1, -5, 6]
                and {stride * degree for degree, coefficient in enumerate(full_coefficients) if coefficient} == {0, 2, 4}
            )
        repeated_markers = exact_int(stride) and [stride * exponent for exponent in repetitions] == [2, 4, 6, 8, 10, 12]
    scalar_inventory = scalar.get("full_inventory")
    scalar_shape = isinstance(scalar_inventory, list) and all(exact_int(value) for value in scalar_inventory)
    scalar_yes = [value for value in scalar_inventory if trial_prime(value)] if scalar_shape else []
    scalar_no = [value for value in scalar_inventory if not trial_prime(value)] if scalar_shape else []
    checks = {
        "mayer_space": mayer.get("function_space_symbol") == "A_infinity(D)" and mayer.get("disk_center_radius") == [[1, 0], [3, 2]],
        "mayer_domains": mayer.get("determinant_half_plane") == "Re(s)>1/2" and mayer.get("euler_product_initial_half_plane") == "Re(s)>1" and mayer.get("continuation_domain") == "C",
        "local_u": mayer.get("local_u_domain") == "formal_or_small_abs_u" and mayer.get("selberg_identity_u_value") == 1,
        "coefficient_tokens": mayer.get("source_log_coefficient_tokens") == ["u^(2*k*r)", "d_w^(r*s)", "r", "1-d_w^r"] and mayer.get("target_log_coefficient_tokens") == ["u^(2*k*r)", "p^(-r*s)", "r"],
        "ownership_symbols": owner.get("declared_object_symbols") == ["X", "X2", "sigma", "rho", "iota", "L_s", "det(I-L_s^2)"],
        "selector_absent": owner.get("declared_untwisted_selector_symbols") == [] and owner.get("ownership_scope") == "FROZEN_UNTWISTED_SCHEMA_ONLY",
        "positive_owner_is_synthetic_control": positive.get("control_role") == "SYNTHETIC_POSITIVE_OWNER_CONTROL_NOT_SD_C42",
        "positive_owner_dimensions": dimensions,
        "positive_owner_idempotence": projector_square,
        "positive_owner_commutation": commuting,
        "positive_owner_trace_identity": trace_identity and full_trace_values == [5, 13, 35, 97, 275, 793],
        "positive_owner_multiplicity": positive.get("multiplicity") == 1 == len(selected or []),
        "positive_owner_marker_degrees": marker_identity,
        "positive_owner_full_marker_degrees": full_marker_identity,
        "positive_owner_repetition_markers": repeated_markers,
        "scalar_partition_recomputed": scalar_inventory == [3, 4] and scalar_yes == [3] and scalar_no == [4],
        "scalar_projector_undeclared": scalar.get("declared_projector") is None,
        "baseline_orientation_rule": rows.get("orientation_equivalence") == "rotation_only",
        "baseline_reversal_metadata": rows.get("reversal_metadata_fields") == ["orientation_id", "reverse_orientation_id", "reversal_orbit_id", "self_reversal", "reverse_class_present"],
        "baseline_reverse_not_quotiented": rows.get("reverse_quotient_rule") == "metadata_only_no_reversal_quotient",
        "baseline_multiplicity_one": rows.get("source_multiplicity") == 1,
        "baseline_positive_sign": rows.get("untwisted_sign") == 1,
        "baseline_zero_phase": rows.get("phase_modulus") == 97 and rows.get("phase_exponent") == 0,
        "baseline_stability_denominator": rows.get("stability_denominator_token") == "1-d_w^r" and "1-d_w^r" in mayer.get("source_log_coefficient_tokens", []),
    }
    return {
        "operator_domain": "D={z:|z-1|<3/2};A_infinity(D)", "determinant_domain": mayer.get("determinant_half_plane"),
        "euler_product_initial_domain": mayer.get("euler_product_initial_half_plane"), "meromorphic_continuation_domain": mayer.get("continuation_domain"),
        "local_u_scope": mayer.get("local_u_domain"), "selberg_identity_u": mayer.get("selberg_identity_u_value"),
        "source_log_coefficient": "u^(2*k*r)*d_w^(r*s)/(r*(1-d_w^r))", "target_log_coefficient": "u^(2*k*r)*p^(-r*s)/r",
    }, {"declared_selector_in_frozen_untwisted_schema": bool(owner.get("declared_untwisted_selector_symbols")), "universal_nonexistence_claim": False}, checks


def route_schema_check(route: dict[str, Any]) -> bool:
    fixture = route.get("schema_fixture")
    if not isinstance(fixture, dict):
        return False
    verdicts = fixture.get("verdict_labels", {})
    return (
        route.get("skill") == "route-a-evaluator"
        and route.get("skill_version") == "0.2.0"
        and route.get("candidate_id") == "SD-C42"
        and route.get("evaluation_date") == "2026-08-17"
        and route.get("criterion_order") == ["A0", "A1", "A2", "A3", "A4"]
        and route.get("schema_fixture_path") == "code/contracts/ROUTE_A_V0_2_SCHEMA.json"
        and route.get("schema_fixture_sha256") == route.get("expected_schema_fixture_sha256") == ROUTE_SCHEMA_FIXTURE_SHA256
        and sha256(canonical_bytes(fixture)).hexdigest() == ROUTE_SCHEMA_FIXTURE_SHA256
        and fixture.get("skill_sha256") == ROUTE_SKILL_SHA256
        and route.get("skill_artifact_path") == "docs/inputs/route-a-evaluator-v0.2.0.md.b64"
        and route.get("skill_artifact_encoding") == "base64-rfc4648"
        and route.get("skill_byte_sha256") == route.get("expected_skill_byte_sha256") == ROUTE_SKILL_SHA256
        and isinstance(route.get("skill_utf8"), str)
        and sha256(route["skill_utf8"].encode("utf-8")).hexdigest() == ROUTE_SKILL_SHA256
        and fixture.get("evidence_status_labels") == [
            "PROVED", "CONDITIONAL_THEOREM", "NUMERICALLY_CERTIFIED",
            "NUMERICAL_OBSERVATION", "HEURISTIC", "MODELING_CHOICE",
            "FITTED_PARAMETER", "OPEN", "REFUTED", "NOT_TESTABLE", "STOP_SCOPED",
        ]
        and all(ROUTE_TUPLE[layer] in verdicts.get(layer, []) for layer in ("A0", "A1", "A2", "A3", "A4"))
        and "A3_EXACT_DIVISOR_CANDIDATE" in verdicts.get("A3", [])
        and "A3_EXACT_DIVISOR_MATCH" not in verdicts.get("A3", [])
        and route.get("required_a0_control_count") == 7
        and route.get("required_a1_control_count") == 6
        and route.get("paired_provenance_fields") == ["source_commit", "code_commit", "source_lock.code_commit"]
        and route.get("target_root_metric_keys") == [
            "correlation_metrics", "cutoff_drift", "eigenvalue_count", "extra_zero_count",
            "missing_zero_count", "precision_drift", "root_count_discrepancy", "root_location_error",
            "spacing_metrics", "spectral_fit", "target_coefficient_fit", "target_prime_data",
            "target_root_data", "target_zero_data", "unfolding_metrics", "zero_error_test",
            "zero_error_train", "zero_error_validation",
        ]
    )


def static_checks(packet: dict[str, Any]) -> dict[str, bool]:
    chronology = packet.get("chronology_input", {})
    freeze = packet.get("experiment_freeze_input", {})
    research = packet.get("research_input", {})
    prototype = packet.get("prototype_reproduction_input", {})
    selection = packet.get("selection_rule_schema", {})
    route = packet.get("route_schema_input", {})
    scope = packet.get("claim_scope_input", {})
    return {
        "schema": packet.get("schema") == "paper40-authority-raw-source-packet-v2" and packet.get("candidate_id") == "SD-C42",
        "chronology": chronology == {"classification": "RETROSPECTIVE_CHECKER_FROZEN_AUTHORITY_INTEGRATION", "v1_and_inflight_smoke_outputs_known": True, "canonical_prototype_outputs_known": True, "control_lock_precedes_clean_replacement_rerun": True, "research_renderings_postdate_canonical_run": True, "authority_checker_inputs_precede_authority_run": True, "prospective_credit_allowed": False},
        "experiment_freeze": freeze.get("preregistration_sha256") == freeze.get("expected_preregistration_sha256") == "f1643899ea7ac62e916b24fc265a4ee2ce1d042e2e078d7b336662ab2a065908" and freeze.get("plan_sha256") == freeze.get("expected_plan_sha256") == "dbae7e5317bea10e623f957ee75389392de7cfd8d55b17965ce710ff78364b2d" and freeze.get("preregistration_path") == "experiments/PREREGISTRATION.md" and freeze.get("plan_path") == "experiments/EXPERIMENT_PLAN.md",
        "research": research.get("manifest_sha256") == research.get("expected_manifest_sha256") == "530f8a989d1e0f29e4ca51342d121a4e358d60692e659b18d136b9236e95c55e" and research.get("pointer_sha256") == research.get("expected_pointer_sha256") == "e985b438395225f454fc60e6e913e1e2b6f1fd6781c24bb3f703778e415fb4e5" and research.get("immutable_file_hashes") == research.get("expected_immutable_file_hashes") == RESEARCH_FILES and research.get("dependent_seal_hashes") == DEPENDENT_SEALS and research.get("manifest_path") == "RESEARCH_LOCK.sha256" and research.get("pointer_path") == "RESEARCH_LOCK.json",
        "prototype_targets": prototype.get("control_lock_sha256") == prototype.get("expected_control_lock_sha256") == "f19edfa13b4f4cd9511394563fc2d7f7d9c428e477ae39e1d248a821e86850d8" and prototype.get("known_output_hash_targets") == KNOWN_OUTPUT_HASHES and prototype.get("vendor_root") == "docs/inputs/prototype_v3" and prototype.get("control_lock_path") == "docs/inputs/prototype_v3/CONTROL_LOCK.md",
        "selection_schema": selection.get("card_ids") == sorted(CARD_HASHES) and selection.get("nonempty_intrinsic_ledger_rule") == "candidate_specific_a1_source_anchor" and selection.get("same_object_determinant_rule") == "a2.evidence_status=PROVED_and_a2.verdict=A2_ANALYTIC_DETERMINANT" and selection.get("tie_break_order") == ["A3", "A4"] and selection.get("forbidden_predicates") == ["nontrivial", "preset_winner", "rank_from_candidate_id"],
        "route_schema": route_schema_check(route),
        "claim_scope": scope.get("scope_label") == "FROZEN_FINITE_TYPED_PROJECTION_CONTRACT_ONLY" and scope.get("forbidden_claim_tokens") == ["universal projection impossibility", "universal selector nonexistence", "minimal collision witness", "prospective novelty credit", "cross-type primitive credit"],
    }


def independent_raw_contract(packet: dict[str, Any]) -> dict[str, bool]:
    controls = packet.get("raw_control_input", {})
    inventories = packet.get("raw_primitive_inventories", [])
    inventory_hashes = {
        record.get("run_id"): fragment_digest(record)
        for record in inventories
        if isinstance(record, dict) and isinstance(record.get("run_id"), str)
    }
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
            and all(verify_lcg(seed, controls["lcg_sequences"].get(name, [])) for name, seed in SEEDS.items())
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
        "raw_collision_oriented_map_exact": packet.get("raw_collision_input") == [
            {"witness_id": "W1", "left_word": [[1, 2]], "right_word": [[2, 1]]},
            {"witness_id": "W2", "left_word": [[1, 4]], "right_word": [[2, 2]]},
            {"witness_id": "W3", "left_word": [[2, 4]], "right_word": [[1, 1], [1, 2]]},
        ],
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
    checks = independent_shape(packet)
    if not all(checks.values()):
        return {
            "schema": "paper40-independent-direct-evaluation-v2",
            "candidate_id": packet.get("candidate_id") if isinstance(packet, dict) else None,
            "source_packet_sha256": sha256(raw).hexdigest(),
            "algorithm": "FKM_APERIODIC_NECKLACES_CONTINUANTS_AND_INDEPENDENT_CONTROLS",
            "no_source_main_adapter_route_or_vendor_import": True,
            "checks": dict(sorted(checks.items())),
            "check_count": len(checks),
            "failure_count": sum(not value for value in checks.values()),
            "all_pass": False,
            "science_projection": None,
        }
    checks.update(static_checks(packet))
    selection, added = independent_selection(packet); checks.update(added)
    checks.update(independent_raw_contract(packet))
    if not all(checks.values()):
        return {
            "schema": "paper40-independent-direct-evaluation-v2",
            "candidate_id": packet.get("candidate_id"),
            "source_packet_sha256": sha256(raw).hexdigest(),
            "algorithm": "FKM_APERIODIC_NECKLACES_CONTINUANTS_AND_INDEPENDENT_CONTROLS",
            "no_source_main_adapter_route_or_vendor_import": True,
            "checks": dict(sorted(checks.items())),
            "check_count": len(checks),
            "failure_count": sum(not value for value in checks.values()),
            "all_pass": False,
            "science_projection": None,
        }
    grouped, added = decode_inventories(packet); checks.update(added)
    summaries = []
    for family, size in sorted(grouped):
        inventories = grouped[(family, size)]
        complete = sorted(inventories) == [1, 2, 3, 4]
        checks[f"run_{family}_D{size}_complete"] = complete
        if complete:
            digits = tuple(range(1 if family == "canonical" else 2, (1 if family == "canonical" else 2) + size))
            summary = independent_run(digits, family, inventories)
            summaries.append(summary)
            checks[f"run_{family}_D{size}_theorem"] = summary["theorem_failures"] == {}
    base = [word for length in (1, 2, 3, 4) for word in grouped[("canonical", 2)][length]]
    neighbor = [word for length in (1, 2, 3, 4) for word in grouped[("neighboring", 2)][length]]
    controls, added = independent_controls(packet, base[:30], neighbor[:30]); checks.update(added)
    typed, added = independent_type_branch(packet, grouped[("canonical", 2)]); checks.update(added)
    collisions, added = independent_collisions(packet); checks.update(added)
    every_word = [word for key in sorted(grouped) for length in (1, 2, 3, 4) for word in grouped[key][length]]
    projection_rows, added = independent_projections(every_word, packet); checks.update(added)
    mayer, ownership, added = independent_boundaries(packet); checks.update(added)
    registered = len(summaries)
    row_count = sum(item["primitive_pair_necklaces_total"] for item in summaries)
    failures = sum(sum(item["theorem_failures"].values()) for item in summaries)
    conjunction = any(item["rational_integer_support"] and item["clock"] and item["repetition"] for item in projection_rows)
    rational_prime_projection = any(item["rational_prime_selectivity"] for item in projection_rows)
    tuple_value = {
        "A0": "A0_WEAK_ARITHMETIC_RELATION" if all(controls["A0"].values()) else "A0_FAIL",
        "A1": "A1_PASS_ANALYTIC" if all(controls["A1"].values()) and typed["splitting_exact"] else "A1_FAIL",
        "A2": "A2_ANALYTIC_DETERMINANT" if checks["mayer_domains"] else "A2_FAIL",
        "A3": "A3_PARTIAL_ANALYTIC_STRUCTURE" if checks["local_u"] else "A3_FAIL",
        "A4": "A4_FORMAL_HINT" if any(item["projection"] == "P_N" and item["clock"] and item["repetition"] for item in projection_rows) else "A4_FAIL",
    }
    terminal_codes: list[str] = []
    if tuple_value["A1"] == "A1_PASS_ANALYTIC": terminal_codes.append("GO_MODULAR_PRIMITIVE_LEDGER")
    if tuple_value["A2"] == "A2_ANALYTIC_DETERMINANT": terminal_codes.append("GO_SAME_OBJECT_MAYER_DETERMINANT")
    if not rational_prime_projection: terminal_codes.append("STOP_CANONICAL_INTEGER_PROJECTION")
    if not conjunction: terminal_codes.append("STOP_RATIONAL_INTEGER_CLOCK_REPETITION_CONJUNCTION")
    if not ownership["declared_selector_in_frozen_untwisted_schema"]: terminal_codes.append("STOP_OPERATOR_VISIBLE_SELECTOR_NOT_OWNED")
    overall = "ROUTE_A_REJECTED" if any(code.startswith("STOP_") for code in terminal_codes) else "ROUTE_A_ACCEPTED"
    if overall == "ROUTE_A_REJECTED": terminal_codes.append("ROUTE_A_REJECTED")
    checks.update({"registered_runs": registered == 6, "scientific_rows": row_count == 39622, "theorem_failures": failures == 0, "no_full_projection": conjunction is False, "route_tuple": tuple_value == ROUTE_TUPLE, "terminal_derivation": terminal_codes == TERMINALS, "overall_derivation": overall == "ROUTE_A_REJECTED"})
    science = {
        "schema": "paper40-scientific-results-v2", "candidate_id": "SD-C42",
        "chronology": "RETROSPECTIVE_CHECKER_FROZEN_AUTHORITY_INTEGRATION",
        "selection": {"survivors": selection["survivors"], "selected": selection["winner"], "sd_c02_zero_orbit_counts_as_nonempty": True, "hidden_nontrivial_predicate": False},
        "typed_bridge": typed, "collision_classes": collisions, "projection_rows": projection_rows,
        "full_projection_conjunction_exists": conjunction, "mayer_boundary": mayer, "ownership": ownership,
        "route": {"tuple": tuple_value, "overall": overall, "route_b_allowed": False, "terminal_codes": terminal_codes},
        "controls": {"a0": controls["A0"], "a1": controls["A1"], "a0_literal_families": 7, "a1_literal_families": 6},
        "prototype": {"runs": summaries, "registered_run_count": registered, "scientific_row_count": row_count, "theorem_failure_count": failures, "hard_status": "PASS" if registered == 6 and row_count == 39622 and failures == 0 else "FAIL"},
        "decision": {"route_a": "REJECTED" if overall == "ROUTE_A_REJECTED" else "ACCEPTED", "route_b": "LOCKED_NOT_INVOKED", "terminal": "STOP_RATIONAL_INTEGER_CLOCK_REPETITION_CONJUNCTION" if not conjunction else "NONE"},
        "claim_boundary": "FROZEN_FINITE_TYPED_PROJECTION_CONTRACT_ONLY",
    }
    return {
        "schema": "paper40-independent-direct-evaluation-v2", "candidate_id": "SD-C42",
        "source_packet_sha256": sha256(raw).hexdigest(),
        "algorithm": "FKM_APERIODIC_NECKLACES_CONTINUANTS_AND_INDEPENDENT_CONTROLS",
        "no_source_main_adapter_route_or_vendor_import": True,
        "checks": dict(sorted(checks.items())), "check_count": len(checks),
        "failure_count": sum(not value for value in checks.values()), "all_pass": all(checks.values()),
        "science_projection": science,
    }


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: independent_evaluator.py SOURCE_PACKET.json")
    raw = Path(sys.argv[1]).read_bytes()
    result = evaluate(json.loads(raw), raw)
    sys.stdout.buffer.write(canonical_bytes(result))
    if not result["all_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
