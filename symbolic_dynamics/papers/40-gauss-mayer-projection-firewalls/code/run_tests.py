#!/usr/bin/env python3
"""Execute the frozen adversarial registry against both direct evaluators."""

from __future__ import annotations

import copy
from concurrent.futures import ThreadPoolExecutor
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
from typing import Any, Callable

import yaml


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "code/contracts/MUTATION_REGISTRY.json"
MAIN = ROOT / "code/evaluator/evaluate_packet.py"
INDEPENDENT = ROOT / "code/evaluator/independent_evaluator.py"
ROUTE = ROOT / "code/evaluator/evaluate_route_a.py"


def canonical_bytes(value: Any) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode("ascii")


def compact_packet_bytes(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True) + "\n").encode("ascii")


def lcg(seed: int, count: int = 256) -> list[int]:
    state = seed
    output = []
    for _ in range(count):
        state = (1103515245 * state + 12345) % (2**31)
        output.append(state)
    return output


def mutate_card_missing_duplicate(packet: dict[str, Any]) -> None:
    records = [item for item in packet["route_card_bytes"] if item["card_id"] != "SD-C06"]
    records.append(copy.deepcopy(next(item for item in records if item["card_id"] == "SD-C05")))
    packet["route_card_bytes"] = records


def mutate_card_declared_hash(packet: dict[str, Any]) -> None:
    packet["route_card_bytes"][0]["historical_byte_sha256"] = "0" * 64


def mutate_card_raw_bytes(packet: dict[str, Any]) -> None:
    packet["route_card_bytes"][0]["raw_yaml_utf8"] += "# byte tamper\n"


def mutate_c02_zero_orbit(packet: dict[str, Any]) -> None:
    record = next(item for item in packet["route_card_bytes"] if item["card_id"] == "SD-C02")
    record["raw_yaml_utf8"] = record["raw_yaml_utf8"].replace(
        "one period-1 zero orbit", "no intrinsic orbit", 1
    )
    changed = sha256(record["raw_yaml_utf8"].encode("utf-8")).hexdigest()
    record["historical_byte_sha256"] = changed
    record["vendored_byte_sha256"] = changed


def mutate_selection_hidden_predicate(packet: dict[str, Any]) -> None:
    packet["selection_rule_schema"]["forbidden_predicates"] = ["preset_winner", "rank_from_candidate_id"]


def mutate_selection_tie_break(packet: dict[str, Any]) -> None:
    packet["selection_rule_schema"]["tie_break_order"] = ["A4", "A3"]


def mutate_type_space_swap(packet: dict[str, Any]) -> None:
    raw = packet["raw_type_input"]
    raw["digit_space_symbol"], raw["pair_space_symbol"] = raw["pair_space_symbol"], raw["digit_space_symbol"]


def mutate_type_digit_shift(packet: dict[str, Any]) -> None:
    packet["raw_type_input"]["digit_shift_symbol"] = "tau"


def mutate_type_pair_shift(packet: dict[str, Any]) -> None:
    packet["raw_type_input"]["pair_shift_symbol"] = "sigma^2"


def mutate_type_grouping_symbol(packet: dict[str, Any]) -> None:
    packet["raw_type_input"]["grouping_symbol"] = "identity"


def mutate_type_block_size(packet: dict[str, Any]) -> None:
    packet["raw_type_input"]["grouping_block_size"] = 1


def mutate_type_parent_symbols(packet: dict[str, Any]) -> None:
    packet["raw_type_input"]["parent_supplied_symbols"].append("RhoPrimitivePair")


def mutate_type_new_symbol(packet: dict[str, Any]) -> None:
    packet["raw_type_input"]["paper40_new_symbol"] = "L_s"


def mutate_type_return_fixture(packet: dict[str, Any]) -> None:
    packet["raw_type_input"]["return_map_digit_fixture"][1] = 9


def mutate_type_reversal_fixture(packet: dict[str, Any]) -> None:
    packet["raw_type_input"]["reversal_pair_fixture"].reverse()


def mutate_inventory_raw_word(packet: dict[str, Any]) -> None:
    packet["raw_primitive_inventories"][0]["raw_words"][0][0][0] += 1


def mutate_inventory_missing_record(packet: dict[str, Any]) -> None:
    packet["raw_primitive_inventories"].pop()


def mutate_inventory_reverse_order(packet: dict[str, Any]) -> None:
    packet["raw_primitive_inventories"].reverse()


def mutate_branch_A_template(packet: dict[str, Any]) -> None:
    packet["raw_branch_input"]["matrix_templates"]["A"][0][1] = 0


def mutate_branch_B_template(packet: dict[str, Any]) -> None:
    packet["raw_branch_input"]["matrix_templates"]["B"][0][0] = 1


def mutate_branch_J_template(packet: dict[str, Any]) -> None:
    packet["raw_branch_input"]["matrix_templates"]["J"][0][0] = 1


def mutate_branch_stored_digits(packet: dict[str, Any]) -> None:
    packet["raw_branch_input"]["stored_digits"][0] = 2


def mutate_branch_nesting(packet: dict[str, Any]) -> None:
    packet["raw_branch_input"]["raw_operator_nesting"] = "first_raw_branch_on_left"


def mutate_branch_evaluation_point(packet: dict[str, Any]) -> None:
    packet["raw_branch_input"]["evaluation_point"] = [1, 5]


def mutate_collision_W1_left_right_swap(packet: dict[str, Any]) -> None:
    item = packet["raw_collision_input"][0]
    item["left_word"], item["right_word"] = item["right_word"], item["left_word"]


def mutate_collision_W1_W2_payload_swap(packet: dict[str, Any]) -> None:
    left, right = packet["raw_collision_input"][0], packet["raw_collision_input"][1]
    left["left_word"], right["left_word"] = right["left_word"], left["left_word"]
    left["right_word"], right["right_word"] = right["right_word"], left["right_word"]


def mutate_collision_W3_relabel(packet: dict[str, Any]) -> None:
    packet["raw_collision_input"][2]["witness_id"] = "W2"


def mutate_projection_definition_swap(packet: dict[str, Any]) -> None:
    packet["projection_definition_input"][0]["definition"] = "matrix_trace_squared_minus_four"


def mutate_projection_minpoly(packet: dict[str, Any]) -> None:
    packet["projection_criterion_schema"]["norm_minimal_polynomial_template"] = "x^2-t*x+1"


def mutate_projection_root_selector(packet: dict[str, Any]) -> None:
    schema = packet["projection_criterion_schema"]
    schema["norm_root_selector"], schema["derivative_root_selector"] = schema["derivative_root_selector"], schema["norm_root_selector"]


def mutate_projection_clock_rule(packet: dict[str, Any]) -> None:
    packet["projection_criterion_schema"]["clock_marker_exponent_rule"] = "pair_length"


def mutate_projection_repetition_exponents(packet: dict[str, Any]) -> None:
    packet["projection_criterion_schema"]["repetition_exponents"] = [2, 3, 4, 5]


def mutate_control_seed_comutation(packet: dict[str, Any]) -> None:
    packet["raw_control_input"]["seeds"]["a0_shuffled_primes"] = 999
    packet["raw_control_input"]["lcg_sequences"]["a0_shuffled_primes"] = lcg(999)


def mutate_control_a0_family(packet: dict[str, Any]) -> None:
    packet["raw_control_input"]["a0_family_ids"][0] = "shuffled_claimed_primes"


def mutate_control_a1_family(packet: dict[str, Any]) -> None:
    packet["raw_control_input"]["a1_family_ids"][0] = "shuffled_digits"


def mutate_control_sequence_payload(packet: dict[str, Any]) -> None:
    packet["raw_control_input"]["lcg_sequences"]["a1_random_weights"][17] += 1


def mutate_control_grid(packet: dict[str, Any]) -> None:
    packet["raw_control_input"]["control_pair_lengths"] = [1, 2, 4]


def mutate_mayer_domain(packet: dict[str, Any]) -> None:
    packet["mayer_source_input"]["determinant_half_plane"] = "Re(s)>1"


def mutate_mayer_source_denominator(packet: dict[str, Any]) -> None:
    packet["mayer_source_input"]["source_log_coefficient_tokens"].remove("1-d_w^r")


def mutate_mayer_target_coefficient(packet: dict[str, Any]) -> None:
    packet["mayer_source_input"]["target_log_coefficient_tokens"][1] = "p^(-s)"


def mutate_ownership_selector_injection(packet: dict[str, Any]) -> None:
    packet["ownership_input"]["declared_untwisted_selector_symbols"] = ["chi_p"]


def mutate_route_skill_bytes(packet: dict[str, Any]) -> None:
    packet["route_schema_input"]["skill_utf8"] += "\nBYTE_SUBSTITUTION"


def mutate_route_skill_hash(packet: dict[str, Any]) -> None:
    packet["route_schema_input"]["skill_byte_sha256"] = "0" * 64


def mutate_route_skill_expected_hash(packet: dict[str, Any]) -> None:
    packet["route_schema_input"]["expected_skill_byte_sha256"] = "0" * 64


def mutate_route_skill_path(packet: dict[str, Any]) -> None:
    packet["route_schema_input"]["skill_artifact_path"] = "docs/inputs/substituted.md.b64"


def mutate_route_skill_encoding(packet: dict[str, Any]) -> None:
    packet["route_schema_input"]["skill_artifact_encoding"] = "utf-8"


def mutate_owner_control_role(packet: dict[str, Any]) -> None:
    packet["ownership_input"]["positive_control_owner"]["control_role"] = "SD_C42_OWNER"


def mutate_owner_operator(packet: dict[str, Any]) -> None:
    packet["ownership_input"]["positive_control_owner"]["operator_matrix"][0][0] = 5


def mutate_owner_full_marker_support(packet: dict[str, Any]) -> None:
    packet["ownership_input"]["positive_control_owner"]["operator_matrix"][1][1] = 0


def mutate_owner_projector_idempotence(packet: dict[str, Any]) -> None:
    packet["ownership_input"]["positive_control_owner"]["projector_matrix"][0][0] = 2


def mutate_owner_projector_commutation(packet: dict[str, Any]) -> None:
    packet["ownership_input"]["positive_control_owner"]["projector_matrix"] = [[1, 1], [0, 0]]


def mutate_owner_dimension(packet: dict[str, Any]) -> None:
    packet["ownership_input"]["positive_control_owner"]["operator_matrix"] = [[2, 0, 0], [0, 3, 0], [0, 0, 5]]


def mutate_owner_selected_indices(packet: dict[str, Any]) -> None:
    packet["ownership_input"]["positive_control_owner"]["selected_indices"] = [1]


def mutate_owner_multiplicity(packet: dict[str, Any]) -> None:
    packet["ownership_input"]["positive_control_owner"]["multiplicity"] = 2


def mutate_owner_marker_stride(packet: dict[str, Any]) -> None:
    packet["ownership_input"]["positive_control_owner"]["marker_stride"] = 4


def mutate_owner_repetitions(packet: dict[str, Any]) -> None:
    packet["ownership_input"]["positive_control_owner"]["repetitions"] = [1, 2, 3, 4, 5]


def mutate_scalar_inventory(packet: dict[str, Any]) -> None:
    packet["ownership_input"]["scalar_postselection"]["full_inventory"] = [3, 5]


def mutate_scalar_declared_projector(packet: dict[str, Any]) -> None:
    packet["ownership_input"]["scalar_postselection"]["declared_projector"] = "P_prime"


def mutate_row_orientation(packet: dict[str, Any]) -> None:
    packet["row_contract_input"]["orientation_equivalence"] = "rotation_and_reversal"


def mutate_row_reversal_metadata(packet: dict[str, Any]) -> None:
    packet["row_contract_input"]["reversal_metadata_fields"].pop()


def mutate_row_reverse_quotient(packet: dict[str, Any]) -> None:
    packet["row_contract_input"]["reverse_quotient_rule"] = "silently_quotient_reverse_class"


def mutate_row_multiplicity(packet: dict[str, Any]) -> None:
    packet["row_contract_input"]["source_multiplicity"] = 2


def mutate_row_sign(packet: dict[str, Any]) -> None:
    packet["row_contract_input"]["untwisted_sign"] = -1


def mutate_row_phase(packet: dict[str, Any]) -> None:
    packet["row_contract_input"]["phase_exponent"] = 1


def mutate_row_phase_modulus(packet: dict[str, Any]) -> None:
    packet["row_contract_input"]["phase_modulus"] = 96


def mutate_row_stability_denominator(packet: dict[str, Any]) -> None:
    packet["row_contract_input"]["stability_denominator_token"] = "1"


def mutate_chronology_prospective(packet: dict[str, Any]) -> None:
    packet["chronology_input"]["prospective_credit_allowed"] = True


def mutate_research_hash(packet: dict[str, Any]) -> None:
    packet["research_input"]["immutable_file_hashes"]["SOURCE_LOCK.md"] = "0" * 64


def mutate_known_output_hashes(packet: dict[str, Any]) -> None:
    packet["prototype_reproduction_input"]["known_output_hash_targets"] = {
        key: "0" * 64 for key in packet["prototype_reproduction_input"]["known_output_hash_targets"]
    }


def mutate_route_allowed_label(packet: dict[str, Any]) -> None:
    packet["route_schema_input"]["schema_fixture"]["verdict_labels"]["A1"][2] = "A1_PASS"


def mutate_route_target_metric(packet: dict[str, Any]) -> None:
    packet["route_schema_input"]["target_root_metric_keys"][0] = "bogus_metric"


def mutate_experiment_plan_path(packet: dict[str, Any]) -> None:
    packet["experiment_freeze_input"]["plan_path"] = "bogus/EXPERIMENT_PLAN.md"


def mutate_packet_extra_field(packet: dict[str, Any]) -> None:
    packet["unexpected_answer"] = "ROUTE_A_REJECTED"


def mutate_type_substitution(packet: dict[str, Any]) -> None:
    packet["raw_type_input"]["grouping_block_size"] = True


def mutate_inventory_type_substitution(packet: dict[str, Any]) -> None:
    packet["raw_primitive_inventories"][0]["raw_words"][0][0][0] = True


def mutate_claim_minimality(packet: dict[str, Any]) -> None:
    packet["claim_scope_input"]["forbidden_claim_tokens"].remove("minimal collision witness")


PACKET_MUTATORS: dict[str, Callable[[dict[str, Any]], None]] = {
    name.removeprefix("mutate_"): value
    for name, value in list(globals().items())
    if name.startswith("mutate_") and callable(value)
}


def indexed_family_mutator(family: str, index: int) -> Callable[[dict[str, Any]], None]:
    key = f"{family}_family_ids"

    def mutate(packet: dict[str, Any]) -> None:
        packet["raw_control_input"][key][index] = "tampered_" + packet["raw_control_input"][key][index]

    return mutate


def seed_mutator(seed_name: str) -> Callable[[dict[str, Any]], None]:
    def mutate(packet: dict[str, Any]) -> None:
        changed = packet["raw_control_input"]["seeds"][seed_name] + 1
        packet["raw_control_input"]["seeds"][seed_name] = changed
        packet["raw_control_input"]["lcg_sequences"][seed_name] = lcg(changed)

    return mutate


def payload_mutator(seed_name: str) -> Callable[[dict[str, Any]], None]:
    def mutate(packet: dict[str, Any]) -> None:
        packet["raw_control_input"]["lcg_sequences"][seed_name][0] += 1

    return mutate


for family, count in (("a0", 7), ("a1", 6)):
    for index in range(count):
        PACKET_MUTATORS[f"control_{family}_family_{index}"] = indexed_family_mutator(family, index)
for seed_name in (
    "a0_composites", "a0_matched_density", "a0_pseudoprimes",
    "a0_randomized_labels", "a0_shuffled_primes", "a1_random_phases",
    "a1_random_weights", "a1_same_density_lengths", "a1_shuffled_periods",
):
    family = seed_name.split("_", 1)[0]
    PACKET_MUTATORS[f"control_{family}_seed_{seed_name}"] = seed_mutator(seed_name)
    PACKET_MUTATORS[f"control_{family}_payload_{seed_name}"] = payload_mutator(seed_name)
for obsolete in (
    "card_missing_duplicate", "card_declared_hash", "card_raw_bytes",
    "inventory_raw_word", "inventory_missing_record", "control_seed_comutation",
    "control_a0_family", "control_a1_family", "control_sequence_payload",
):
    PACKET_MUTATORS.pop(obsolete, None)


def expanded_packet_mutators(registry: dict[str, Any]) -> dict[str, Callable[[dict[str, Any]], None]]:
    output = dict(PACKET_MUTATORS)
    expansion = registry["exhaustive_expansion_contract"]

    def card_mutator(card_id: str, kind: str) -> Callable[[dict[str, Any]], None]:
        def mutate(packet: dict[str, Any]) -> None:
            records = packet["route_card_bytes"]
            index = next(position for position, item in enumerate(records) if item["card_id"] == card_id)
            if kind == "declared_hash":
                records[index]["historical_byte_sha256"] = "0" * 64
            elif kind == "raw_bytes":
                records[index]["raw_yaml_utf8"] += "# exact per-card tamper\n"
            elif kind == "omit_duplicate":
                records.pop(index)
                records.append(copy.deepcopy(records[0]))
            else:
                raise KeyError(kind)

        return mutate

    def inventory_mutator(run_id: str, kind: str) -> Callable[[dict[str, Any]], None]:
        def mutate(packet: dict[str, Any]) -> None:
            records = packet["raw_primitive_inventories"]
            index = next(position for position, item in enumerate(records) if item["run_id"] == run_id)
            if kind == "tamper":
                records[index]["raw_words"][0][0][0] += 1
            elif kind == "omit":
                records.pop(index)
            else:
                raise KeyError(kind)

        return mutate

    for card_id in expansion["card_ids"]:
        for kind in expansion["card_case_kinds"]:
            output[f"card_{card_id}_{kind}"] = card_mutator(card_id, kind)
    for run_id in expansion["inventory_run_ids"]:
        for kind in expansion["inventory_case_kinds"]:
            output[f"inventory_{run_id}_{kind}"] = inventory_mutator(run_id, kind)
    return output


def route_mutation(route: dict[str, Any], mutation_id: str) -> bytes:
    mutated = copy.deepcopy(route)
    if mutation_id == "route_extra_top_key":
        mutated["legacy_extra"] = False
    elif mutation_id == "route_missing_nested_key":
        mutated["a2"]["metrics"].pop("zero_error_train")
    elif mutation_id == "route_wrong_scalar_type":
        mutated["route_b"]["B"] = 0
    elif mutation_id == "route_duplicate_control":
        mutated["a0"]["arithmetic_controls"][1] = mutated["a0"]["arithmetic_controls"][0]
    elif mutation_id == "route_wrong_target_key":
        mutated["target_and_root_metrics"]["bogus"] = mutated["target_and_root_metrics"].pop("correlation_metrics")
    elif mutation_id == "route_legacy_terminal":
        mutated["terminal_codes"][2] = "STOP_CLOCK_REPETITION_COMPATIBILITY"
    elif mutation_id == "route_tuple_change":
        mutated["route_tuple"][0] = "A0_FAIL"
    elif mutation_id == "route_projection_cell":
        mutated["projection_firewall"]["rows"][0]["clock"] = True
    elif mutation_id.startswith("route_projection_"):
        matched = False
        for row_index, projection_id in enumerate(("P_t", "P_Delta", "P_N")):
            prefix = f"route_projection_{projection_id}_"
            if mutation_id.startswith(prefix):
                field = mutation_id.removeprefix(prefix)
                if field == "projection":
                    mutated["projection_firewall"]["rows"][row_index][field] = projection_id + "_tampered"
                else:
                    mutated["projection_firewall"]["rows"][row_index][field] = not mutated["projection_firewall"]["rows"][row_index][field]
                matched = True
                break
        if not matched:
            raise KeyError(mutation_id)
    elif mutation_id == "route_pending_triple_mismatch":
        mutated["code_commit"] = "1" * 40
        mutated["source_commit"] = "2" * 40
    elif mutation_id == "route_duplicate_yaml_key":
        return yaml.safe_dump(route, sort_keys=False, allow_unicode=False).encode("ascii") + b"candidate_id: SD-C42\n"
    else:
        raise KeyError(mutation_id)
    return yaml.safe_dump(mutated, sort_keys=False, allow_unicode=False).encode("ascii")


def pointer_label(path: tuple[str | int, ...]) -> str:
    return "/" + "/".join(str(item).replace("~", "~0").replace("/", "~1") for item in path)


def route_recursive_cases(route: dict[str, Any]) -> list[tuple[str, bytes]]:
    specifications: list[tuple[str, tuple[str | int, ...]]] = []

    def visit(value: Any, path: tuple[str | int, ...]) -> None:
        if isinstance(value, dict):
            for key in sorted(value):
                specifications.append(("delete_key", path + (key,)))
                visit(value[key], path + (key,))
        elif isinstance(value, list):
            if len(value) >= 2 and list(reversed(value)) != value:
                specifications.append(("reverse_list", path))
            for index, item in enumerate(value):
                visit(item, path + (index,))
        else:
            specifications.append(("mutate_leaf", path))

    visit(route, ())
    cases = []
    for action, path in specifications:
        mutated = copy.deepcopy(route)
        parent: Any = mutated
        for token in path[:-1]:
            parent = parent[token]
        if action == "delete_key":
            del parent[path[-1]]
        elif action == "reverse_list":
            target: Any = mutated
            for token in path:
                target = target[token]
            target.reverse()
        else:
            target_value = parent[path[-1]]
            if type(target_value) is bool:
                parent[path[-1]] = not target_value
            elif type(target_value) is int:
                parent[path[-1]] = target_value + 1
            elif isinstance(target_value, str):
                parent[path[-1]] = target_value + "_MUTATED"
            elif target_value is None:
                parent[path[-1]] = "MUTATED_NONE"
            else:
                raise TypeError(f"unsupported Route leaf: {type(target_value).__name__}")
        case_id = f"route_recursive_{action}:{pointer_label(path)}"
        cases.append((case_id, yaml.safe_dump(mutated, sort_keys=False, allow_unicode=False).encode("ascii")))
    return cases


def invoke(script: Path, payload: bytes, suffix: str) -> tuple[int, dict[str, Any], str]:
    with tempfile.NamedTemporaryFile(prefix="paper40_mutation_", suffix=suffix, delete=False) as handle:
        handle.write(payload)
        temporary = Path(handle.name)
    env = os.environ.copy()
    env.update({"PYTHONDONTWRITEBYTECODE": "1", "PYTHONHASHSEED": "0"})
    try:
        completed = subprocess.run(
            [sys.executable, "-I", "-B", str(script), str(temporary)],
            cwd=ROOT,
            env=env,
            check=False,
            capture_output=True,
        )
    finally:
        temporary.unlink(missing_ok=True)
    try:
        result = json.loads(completed.stdout)
    except (json.JSONDecodeError, UnicodeDecodeError):
        result = {}
    return completed.returncode, result, completed.stderr.decode("utf-8", errors="replace")


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("usage: run_tests.py SOURCE_PACKET.json ROUTE.yaml")
    packet_raw = Path(sys.argv[1]).read_bytes()
    packet = json.loads(packet_raw)
    route_raw = Path(sys.argv[2]).read_bytes()
    route = yaml.safe_load(route_raw)
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    bindings = registry.get("result_id_bindings", {})

    def require_binding(name: str, ids: list[str]) -> None:
        binding = bindings.get(name, {})
        if binding != {
            "count": len(ids),
            "ordered_id_sha256": sha256(canonical_bytes(ids)).hexdigest(),
        }:
            raise RuntimeError(f"mutation result-ID binding differs: {name}")

    packet_mutators = expanded_packet_mutators(registry)
    declared_packet = [item["id"] for item in registry["packet_mutations"]]
    expansion = registry["exhaustive_expansion_contract"]
    declared_packet += [
        f"card_{card_id}_{kind}"
        for card_id in expansion["card_ids"] for kind in expansion["card_case_kinds"]
    ]
    declared_packet += [
        f"inventory_{run_id}_{kind}"
        for run_id in expansion["inventory_run_ids"] for kind in expansion["inventory_case_kinds"]
    ]
    if set(declared_packet) != set(packet_mutators) or len(declared_packet) != len(set(declared_packet)):
        raise RuntimeError("packet mutation registry and implementation differ")
    require_binding("expanded_packet", declared_packet)
    explicit_route_ids = [item["id"] for item in registry["route_mutations"]]
    static_ids = [item["id"] for item in registry["static_and_seal_mutations"]]
    require_binding("route_explicit", explicit_route_ids)
    require_binding("static_and_seal", static_ids)

    packet_rows = []
    for mutation_id in declared_packet:
        mutated = copy.deepcopy(packet)
        packet_mutators[mutation_id](mutated)
        raw = compact_packet_bytes(mutated)
        evaluations = {}
        evaluator_specs = (("main", MAIN), ("independent", INDEPENDENT))
        with ThreadPoolExecutor(max_workers=2) as pool:
            futures = {
                label: pool.submit(invoke, script, raw, ".json")
                for label, script in evaluator_specs
            }
        for label, _ in evaluator_specs:
            returncode, result, stderr = futures[label].result()
            rejected = (
                returncode == 1
                and not stderr
                and result.get("all_pass") is False
                and result.get("failure_count", 0) > 0
            )
            evaluations[label] = {
                "failure_checks": sorted(name for name, passed in result.get("checks", {}).items() if not passed),
                "rejected": rejected,
                "returncode": returncode,
            }
        packet_rows.append({"id": mutation_id, "evaluators": evaluations})

    route_rows = []
    route_payload_hashes: list[str] = []
    for item in registry["route_mutations"]:
        mutation_id = item["id"]
        raw = route_mutation(route, mutation_id)
        route_payload_hashes.append(sha256(raw).hexdigest())
        returncode, result, stderr = invoke(ROUTE, raw, ".yaml")
        route_rows.append({
            "id": mutation_id,
            "failure_checks": sorted(name for name, passed in result.get("checks", {}).items() if not passed),
            "rejected": returncode == 1 and not stderr and result.get("all_pass") is False,
            "returncode": returncode,
        })
    recursive_cases = route_recursive_cases(route)
    recursive_ids = [case_id for case_id, _ in recursive_cases]
    expected_recursive = registry["exhaustive_expansion_contract"]["route_recursive_policy"]
    if len(recursive_ids) != expected_recursive.get("expected_case_count"):
        raise RuntimeError("Route recursive mutation count differs from frozen registry")
    if sha256(canonical_bytes(recursive_ids)).hexdigest() != expected_recursive.get("expected_case_id_sha256"):
        raise RuntimeError("Route recursive mutation ID set differs from frozen registry")
    require_binding("route_recursive", recursive_ids)
    require_binding("route_full", explicit_route_ids + recursive_ids)
    for mutation_id, raw in recursive_cases:
        route_payload_hashes.append(sha256(raw).hexdigest())
        returncode, result, stderr = invoke(ROUTE, raw, ".yaml")
        route_rows.append({
            "id": mutation_id,
            "failure_checks": sorted(name for name, passed in result.get("checks", {}).items() if not passed),
            "rejected": returncode == 1 and not stderr and result.get("all_pass") is False,
            "returncode": returncode,
        })

    packet_all = all(
        row["evaluators"][label]["rejected"]
        for row in packet_rows for label in ("main", "independent")
    )
    route_all = all(row["rejected"] for row in route_rows)
    result = {
        "schema": "paper40-adversarial-test-results-v1",
        "registry_sha256": sha256(REGISTRY.read_bytes()).hexdigest(),
        "counts": {
            "packet_mutations": len(packet_rows),
            "main_rejections": sum(row["evaluators"]["main"]["rejected"] for row in packet_rows),
            "independent_rejections": sum(row["evaluators"]["independent"]["rejected"] for row in packet_rows),
            "route_mutations": len(route_rows),
            "route_explicit_mutations": len(registry["route_mutations"]),
            "route_recursive_mutations": len(recursive_cases),
            "route_distinct_payloads": len(set(route_payload_hashes)),
            "route_rejections": sum(row["rejected"] for row in route_rows),
        },
        "packet_results": packet_rows,
        "route_results": route_rows,
        "all_pass": packet_all and route_all,
    }
    sys.stdout.buffer.write(canonical_bytes(result))
    if not result["all_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
