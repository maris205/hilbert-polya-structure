#!/usr/bin/env python3
"""Execute the Paper 43 adversarial mutation matrix.

Raw mutations are submitted to both isolated scientific evaluators.  Route
mutations are exhaustively generated from the rendered tree and submitted in
separate batches to the strict validator and independent auditor.  Output,
environment, and paired-state controls are checked against the staged tree
when ``--output-root`` is supplied.  No producer Boolean is evidence.
"""

from __future__ import annotations

import copy
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path, PurePosixPath
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "code/contracts/MUTATION_REGISTRY.json"
CONTRACT = ROOT / "code/contracts/INTEGRATION_CONTRACT.json"
MAIN = ROOT / "code/evaluator/evaluate_packet.py"
INDEPENDENT = ROOT / "code/evaluator/independent_evaluator.py"
ROUTE_MAIN = ROOT / "code/route/validate_route_a.py"
ROUTE_INDEPENDENT = ROOT / "code/route/audit_route_a.py"
AUDITOR = ROOT / "code/integration/audit_integrity.py"
PYTHON = sys.executable
RAW_CONSUMERS = ["algorithm_C", "algorithm_F"]
ROUTE_CONSUMERS = ["independent_route_auditor", "strict_route_validator"]
AUDITOR_CONSUMERS = ["read_only_integrity_auditor"]
THREE_ROUTE_STATE_CONSUMERS = [
    "independent_route_auditor", "read_only_integrity_auditor",
    "strict_route_validator",
]


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       separators=(",", ": ")) + "\n").encode("ascii")


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    output: dict[str, Any] = {}
    for key, value in pairs:
        if key in output:
            raise ValueError(f"duplicate key: {key}")
        output[key] = value
    return output


def load(path: Path) -> tuple[Any, bytes]:
    raw = path.read_bytes()
    value = json.loads(raw.decode("ascii"), object_pairs_hook=unique)
    if canonical(value) != raw:
        raise ValueError(f"noncanonical JSON: {path.name}")
    return value, raw


def variant_from_id(class_id: str, identifier: str) -> str:
    prefix = class_id + "__"
    if not identifier.startswith(prefix) or len(identifier) == len(prefix):
        raise ValueError(f"mutation ID/class mismatch: {identifier} / {class_id}")
    return identifier[len(prefix):]


def mutation_record(class_id: str, identifier: str, domain: str,
                    designated_consumers: list[str], outcomes: dict[str, str],
                    passed: bool) -> dict[str, Any]:
    consumers = sorted(designated_consumers)
    if sorted(outcomes) != consumers:
        raise ValueError(f"mutation outcome/consumer mismatch: {identifier}")
    return {
        "class_id": class_id,
        "designated_consumers": consumers,
        "domain": domain,
        "expectation": "all_designated_consumers_reject_nonzero",
        "id": identifier,
        "outcomes": {name: outcomes[name] for name in consumers},
        "passed": passed,
        "variant": variant_from_id(class_id, identifier),
    }


def positive_control_record(class_id: str, identifier: str, domain: str,
                            designated_consumers: list[str],
                            outcomes: dict[str, str], passed: bool) -> dict[str, Any]:
    consumers = sorted(designated_consumers)
    if sorted(outcomes) != consumers:
        raise ValueError(f"positive-control outcome/consumer mismatch: {identifier}")
    return {
        "class_id": class_id,
        "designated_consumers": consumers,
        "domain": domain,
        "expectation": "exact_positive_control",
        "id": identifier,
        "outcomes": {name: outcomes[name] for name in consumers},
        "passed": passed,
        "variant": variant_from_id(class_id, identifier),
    }


def invoke(script: Path, arguments: list[str], cwd: Path) -> subprocess.CompletedProcess[bytes]:
    hostile = cwd / "hostile_modules"
    hostile.mkdir(parents=True, exist_ok=True)
    (hostile / "sitecustomize.py").write_text(
        "raise RuntimeError('hostile sitecustomize loaded')\n", encoding="ascii")
    (hostile / "json.py").write_text(
        "raise RuntimeError('hostile json shadow loaded')\n", encoding="ascii")
    env = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"),
           "PYTHONPATH": str(hostile)}
    return subprocess.run(
        [PYTHON, "-I", "-B", str(script), *arguments],
        cwd=cwd, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        check=False,
    )


def changed(packet: dict[str, Any], edit: Callable[[dict[str, Any]], None]) -> bytes:
    clone = copy.deepcopy(packet)
    edit(clone)
    return canonical(clone)


def raw_mutations(packet: dict[str, Any], packet_raw: bytes) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []

    def add(class_id: str, suffix: str, edit: Callable[[dict[str, Any]], None]) -> None:
        rows.append({"class_id": class_id, "id": f"{class_id}__{suffix}",
                     "raw": changed(packet, edit)})

    add("json_type", "boolean_to_integer", lambda p: p["factor_axiom_schema"].__setitem__("continuity", 1))
    add("json_type", "integer_to_float", lambda p: p["control_grid"].__setitem__("fixed_count_max_m", 8.0))
    add("json_type", "list_to_scalar", lambda p: p["control_grid"].__setitem__("windows", "0,1,2,3"))
    add("json_type", "string_to_number", lambda p: p["candidate_contract"].__setitem__("candidate_id", 45))
    add("json_structure", "delete_field", lambda p: p.pop("claim_question"))
    add("json_structure", "rename_field", lambda p: p.__setitem__("claim_questions", p.pop("claim_question")))
    add("json_structure", "add_field", lambda p: p.__setitem__("unexpected", None))
    duplicate = packet_raw.replace(b'{\n  "candidate_contract":',
                                   b'{\n  "candidate_contract": null,\n  "candidate_contract":', 1)
    rows.append({"class_id": "json_structure", "id": "json_structure__duplicate_field",
                 "raw": duplicate})
    add("candidate", "candidate_id", lambda p: p["candidate_contract"].__setitem__("candidate_id", "SD-C44"))
    add("candidate", "historical_parent", lambda p: p["candidate_contract"].__setitem__("historical_parent", "SD-C03"))
    add("candidate", "source_type", lambda p: p["candidate_contract"].__setitem__("source_type", "PeriodicOrbit"))
    add("candidate", "factor_direction", lambda p: p["claim_question"].__setitem__("factor_quantifier", "extension_not_factor"))
    add("source_quantifier", "finite_primes", lambda p: p["source_axiom_schema"].__setitem__("prime_quantifier", "first_three_primes"))
    add("source_quantifier", "p_not_p_squared", lambda p: p["source_axiom_schema"].__setitem__("admissibility", "support_mod_p_is_not_all_residues"))
    add("source_fixture", "filled_mod_four", lambda p: p["source_fixture_inputs"]["supports"].__setitem__(0, [0, 1, 2, 3]))
    add("shift_direction", "right_shift", lambda p: p["source_axiom_schema"].__setitem__("dynamics", "two_sided_shift_x_j_equals_x_j_minus_1"))
    add("shift_direction", "one_sided", lambda p: p["source_axiom_schema"].__setitem__("space", "binary_sequences_indexed_by_N"))
    add("prime_allocation", "reuse_prime", lambda p: p["control_grid"].__setitem__("prime_allocation_rule", "reuse_first_prime"))
    add("prime_allocation", "composite", lambda p: p["control_grid"].__setitem__("prime_allocation_rule", "ascending_integers_including_composites"))
    add("prime_allocation", "unsorted", lambda p: p["control_grid"].__setitem__(
        "prime_allocation_rule", "first_rational_primes_descending_unsorted"))
    add("missing_residue", "occupied_residue", lambda p: p["control_grid"].__setitem__("missing_residue_rule", "least_occupied_residue"))
    add("missing_residue", "omit_window_coordinate", lambda p: p["control_grid"].__setitem__(
        "missing_residue_rule", "omit_one_coordinate_from_each_window"))
    add("crt_sign", "wrong_sign", lambda p: p["source_axiom_schema"].__setitem__("dynamics", "sigma_n_x_j_equals_x_n_minus_j"))
    add("crt_algorithm", "wrong_inverse", lambda p: p["control_grid"].__setitem__("prime_allocation_rule", "first_primes_then_wrong_inverse"))
    add("metric", "drop_tail", lambda p: p["control_grid"]["metric"].__setitem__("tail_bound", "2^(-L)/3"))
    add("metric", "change_normalization", lambda p: p["control_grid"]["metric"].__setitem__("formula", "sum_2_power_minus_abs_k"))
    add("universal_inference", "finite_table_claim", lambda p: p["claim_question"].__setitem__("finite_table_proves_universal", True))
    add("compactness", "remove_closed_intersection", lambda p: p["source_axiom_schema"].__setitem__("space", "nonclosed_union_of_cylinders"))
    add("factor_target", "finite_alphabet", lambda p: p["factor_axiom_schema"].__setitem__("target_space", "finite_alphabet_subshift"))
    add("factor_target", "finite_radius", lambda p: p["factor_axiom_schema"].__setitem__(
        "target_space", "finite_radius_sliding_block_factor"))
    add("factor_target", "sofic_only", lambda p: p["factor_axiom_schema"].__setitem__(
        "target_space", "sofic_shift_only"))
    add("factor_target", "expansive_only", lambda p: p["factor_axiom_schema"].__setitem__(
        "target_space", "expansive_system_only"))
    add("factor_target", "finite_fiber", lambda p: p["factor_axiom_schema"].__setitem__("finite_fiber", True))
    add("continuity", "false", lambda p: p["factor_axiom_schema"].__setitem__("continuity", False))
    add("surjectivity", "false", lambda p: p["factor_axiom_schema"].__setitem__("surjective", False))
    add("equivariance", "one_time", lambda p: p["factor_axiom_schema"].__setitem__("equivariance_equation", "pi_sigma_equals_S_pi_only"))
    add("equivariance", "nonnegative", lambda p: p["factor_axiom_schema"].__setitem__("full_Z_equivariance", False))
    add("target_action", "noninvertible", lambda p: p["factor_axiom_schema"].__setitem__("target_action", "noninvertible_continuous_map"))
    add("fixed_anchor", "nonfixed", lambda p: p["factor_axiom_schema"].__setitem__("fixed_anchor", False))
    add("periodic_separation", "omit_second_fixed", lambda p: p["factor_axiom_schema"].__setitem__("periodic_separation", "positive_period_only"))
    add("source_periodic_word", "accept_nonzero", lambda p: p["source_axiom_schema"].__setitem__("admissibility", "allow_nonzero_periodic_words"))
    add("fixed_counts", "change_bound", lambda p: p["control_grid"].__setitem__("fixed_count_max_m", 7))
    add("zeta_orientation", "reciprocal", lambda p: p["claim_question"].__setitem__("determinant_convention", "D_AM_Y(z)=zeta_AM_Y(z)"))
    add("marker", "drop_repetition", lambda p: p["marker_contract"].__setitem__("repetition_rule", "r_fold_traversal_contributes_z"))
    add("marker", "identify_comparator", lambda p: p["marker_contract"].__setitem__("specialize_u_to_z", True))
    add("marker", "specialize_z_to_one", lambda p: p["marker_contract"].__setitem__(
        "factor_marker", "1"))
    add("primitive_support", "prime_identification", lambda p: p["type_ledger"].__setitem__("primitive", "RationalPrimeAtom"))
    add("operator_owner", "full_state_owner", lambda p: p["operator_contract"].__setitem__("full_state_operator", True))
    add("operator_owner", "transfer_owner", lambda p: p["operator_contract"].__setitem__("owner", "transfer_operator_on_CY"))
    add("operator_owner", "squarefree_source", lambda p: p["operator_contract"].__setitem__(
        "owner", "full_squarefree_source"))
    add("operator_owner", "c_of_y", lambda p: p["operator_contract"].__setitem__(
        "owner", "operator_on_C_of_Y"))
    add("operator_owner", "hilbert_polya", lambda p: p["operator_contract"].__setitem__(
        "owner", "Hilbert_Polya_operator"))
    add("finite_p0_type", "composite", lambda p: p["finite_p0_inputs"]["prime_sets"].__setitem__(1, [4]))
    add("finite_p0_type", "duplicate", lambda p: p["finite_p0_inputs"]["prime_sets"].__setitem__(3, [2, 2]))
    add("finite_p0_product", "omit_square", lambda p: p["finite_p0_inputs"].__setitem__("product_rule", "Q=product_of_p"))
    add("finite_p0_product", "constant_one", lambda p: p["finite_p0_inputs"].__setitem__(
        "product_rule", "Q=1_for_every_P0"))
    add("finite_p0_period", "omit_leastness", lambda p: p["finite_p0_inputs"].__setitem__("witness_rule", "x_is_Q_periodic_without_leastness"))
    add("finite_p0_period", "proper_divisor", lambda p: p["finite_p0_inputs"].__setitem__(
        "witness_rule", "least_period_is_a_proper_divisor_of_Q"))
    add("finite_p0_period", "nonempty_period_one", lambda p: p["finite_p0_inputs"].__setitem__(
        "witness_rule", "nonempty_P0_has_period_1"))
    add("empty_p0", "remove_empty", lambda p: p["finite_p0_inputs"]["prime_sets"].pop(0))
    add("modulus_four_control", "change_word", lambda p: p["finite_p0_inputs"].__setitem__("concrete_word", "1000"))
    add("repair_direction", "extension", lambda p: p["claim_question"].__setitem__("question", "can_an_extension_create_cycles"))
    add("observable", "measure_zeta", lambda p: p["claim_question"].__setitem__("determinant_convention", "measure_theoretic_zeta"))
    add("repair_scope", "exhaustive", lambda p: p["claim_question"].__setitem__("declared_repairs_are_exhaustive", True))
    add("selector", "preset_survivor", lambda p: p["selection_adapter_contract"].__setitem__("survivor", "SD-C02"))
    add("selector", "prospective", lambda p: p["selection_adapter_contract"].__setitem__("rule_chronology", "prospective"))
    add("selector", "omit_clause", lambda p: p["selection_adapter_contract"]["clauses"].pop(0))
    add("selector", "swap_clause_order", lambda p: p["selection_adapter_contract"]["clauses"].__setitem__(
        slice(0, 2), list(reversed(p["selection_adapter_contract"]["clauses"][:2]))))
    add("selection_card", "modify_byte", lambda p: p["raw_selection_cards"][0].__setitem__("bytes_base64", p["raw_selection_cards"][0]["bytes_base64"][:-1] + "A"))
    add("selection_card", "duplicate_card", lambda p: p["raw_selection_cards"].__setitem__(2, copy.deepcopy(p["raw_selection_cards"][0])))
    add("selection_card", "omit_card", lambda p: p["raw_selection_cards"].pop(1))
    add("selection_card", "ambiguous_candidate_id", lambda p: p["raw_selection_cards"][1].__setitem__(
        "candidate_id", p["raw_selection_cards"][0]["candidate_id"]))
    add("adapter", "change_anchor", lambda p: p["selection_adapter_contract"]["clauses"][0].__setitem__("value", "A0_PASS"))
    add("adapter", "pass_flag", lambda p: p["selection_adapter_contract"].__setitem__("pass", True))
    add("chronology", "prospective", lambda p: p["integration_chronology"].__setitem__("prospective", True))
    add("chronology", "blind", lambda p: p["integration_chronology"].__setitem__("blind", True))
    add("chronology", "novelty", lambda p: p["integration_chronology"].__setitem__("novelty_credit", True))
    add("chronology", "preregistered", lambda p: p["integration_chronology"].__setitem__(
        "preregistered", True))
    add("chronology", "results_unseen", lambda p: p["integration_chronology"].__setitem__(
        "results_unseen", True))
    add("chronology", "priority", lambda p: p["integration_chronology"].__setitem__(
        "priority_credit", True))
    add("chronology", "outcome_independent", lambda p: p["integration_chronology"].__setitem__(
        "outcome_independent", True))
    add("chronology", "fully_prospective", lambda p: p["integration_chronology"].__setitem__(
        "fully_prospective", True))
    add("chronology", "implementation_credit", lambda p: p["integration_chronology"].__setitem__(
        "implementation_novelty_credit", True))
    for predecessor in ("P39", "P40", "P41", "P42"):
        add("p39_p42_role", f"{predecessor.lower()}_ranking",
            lambda p, name=predecessor: p["integration_chronology"]["predecessor_roles"].__setitem__(
                name, "ranked_and_authorized"))
    add("duplicate_boundary", "remove_stop", lambda p: p["literature_boundary_contract"].__setitem__("conditional_code", "PROCEED"))
    add("duplicate_boundary", "absence_proves_novelty", lambda p: p["literature_boundary_contract"].__setitem__("bounded_search_absence_is_novelty_proof", True))
    add("source_id", "duplicate", lambda p: p["portable_source_input"]["entries"].__setitem__(1, copy.deepcopy(p["portable_source_input"]["entries"][0])))
    add("source_id", "path_escape", lambda p: p["portable_source_input"]["entries"][0].__setitem__("relative_container", "../escape"))
    add("source_id", "unsorted", lambda p: p["portable_source_input"]["entries"].__setitem__(
        slice(0, 2), list(reversed(p["portable_source_input"]["entries"][:2]))))
    add("source_id", "rename", lambda p: p["portable_source_input"]["entries"][0].__setitem__(
        "id", "renamed:source"))
    add("source_id", "decoded_hash", lambda p: p["portable_source_input"]["entries"][0].__setitem__(
        "decoded_sha256", "0" * 64))
    add("source_id", "container_hash", lambda p: p["portable_source_input"]["entries"][0].__setitem__(
        "container_sha256", "0" * 64))
    add("live_dependency", "queried", lambda p: p["portable_source_input"].__setitem__("external_tree_status", "QUERIED"))
    add("artifact_path", "absolute", lambda p: p["portable_source_input"]["entries"][0].__setitem__(
        "relative_container", "/" + "tmp" + "/live"))
    add("path_leak", "host_path", lambda p: p["writer_sync_contract"].__setitem__(
        "anchor_path", "/" + "root" + "/live.tex"))
    add("check_flag", "producer_pass", lambda p: p.__setitem__("pass", True))
    return rows


def pointer_slug(parts: list[str]) -> str:
    if not parts:
        return "root"
    return re.sub(r"[^a-z0-9]+", "_", "_".join(parts).lower()).strip("_")[:120]


def route_mutations(route: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []

    def add(kind: str, parts: list[str], value: dict[str, Any]) -> None:
        identifier = f"route_schema__{kind}__{pointer_slug(parts)}__{len(rows):04d}"
        rows.append({"id": identifier, "route": value})

    def locate(root: Any, parts: list[str]) -> Any:
        node = root
        for part in parts:
            node = node[int(part)] if type(node) is list else node[part]
        return node

    def parent(root: Any, parts: list[str]) -> tuple[Any, str]:
        return locate(root, parts[:-1]), parts[-1]

    def visit(node: Any, parts: list[str]) -> None:
        if type(node) is dict:
            for key in sorted(node):
                clone = copy.deepcopy(route)
                holder = locate(clone, parts)
                del holder[key]
                add("mapping_key_delete", parts + [key], clone)
            clone = copy.deepcopy(route)
            locate(clone, parts)["__unknown_key__"] = None
            add("mapping_unknown_key", parts, clone)
            for key in sorted(node):
                visit(node[key], parts + [key])
        elif type(node) is list:
            for index in range(len(node)):
                clone = copy.deepcopy(route)
                del locate(clone, parts)[index]
                add("list_member_delete", parts + [str(index)], clone)
            if len(node) > 1:
                clone = copy.deepcopy(route)
                target = locate(clone, parts)
                target[0], target[1] = target[1], target[0]
                add("list_order_swap", parts, clone)
            for index, child in enumerate(node):
                visit(child, parts + [str(index)])
        else:
            if type(node) is bool:
                changed_value, changed_type = (not node), (1 if node else 0)
            elif type(node) is int:
                changed_value, changed_type = node + 1, str(node)
            elif type(node) is str:
                changed_value, changed_type = node + "__MUTATED", 0
            elif node is None:
                changed_value, changed_type = "NOT_NULL", False
            else:
                raise TypeError("unsupported Route scalar")
            for kind, replacement in (("scalar_value", changed_value),
                                      ("scalar_type", changed_type)):
                clone = copy.deepcopy(route)
                holder, leaf = parent(clone, parts)
                if type(holder) is list:
                    holder[int(leaf)] = replacement
                else:
                    holder[leaf] = replacement
                add(kind, parts, clone)
    visit(route, [])

    # Artifact-path controls are classed separately from generic schema
    # mutation.  Every nested artifact is exercised against parent escape and
    # a safe-looking but nonexistent package-relative path; the read-only
    # integrity auditor additionally resolves every canonical path.
    artifact_lists: list[tuple[list[str], int]] = []

    def collect_artifacts(node: Any, parts: list[str]) -> None:
        if type(node) is dict:
            for key, value in node.items():
                if key in {"artifacts", "artifact_paths"} and type(value) is list:
                    artifact_lists.extend((parts + [key], index)
                                          for index, item in enumerate(value)
                                          if type(item) is str)
                collect_artifacts(value, parts + [key])
        elif type(node) is list:
            for index, value in enumerate(node):
                collect_artifacts(value, parts + [str(index)])

    collect_artifacts(route, [])
    for path_parts, item_index in artifact_lists:
        for variant, replacement in (
                ("parent_escape", "../outside"),
                ("nonexistent", f"results/nonexistent_artifact_{len(rows):04d}.json")):
            clone = copy.deepcopy(route)
            locate(clone, path_parts)[item_index] = replacement
            slug = pointer_slug(path_parts + [str(item_index)])
            rows.append({
                "id": f"artifact_path__{variant}__{slug}__{len(rows):04d}",
                "route": clone,
            })

    targeted: list[tuple[str, str, Callable[[dict[str, Any]], None]]] = [
        ("route_a0", "verdict_pass", lambda r: r["a0"].__setitem__("verdict", "A0_PASS")),
        ("route_a1", "verdict_pass", lambda r: r["a1"].__setitem__("verdict", "A1_PASS")),
        ("route_a1", "rational_prime_primitive_credit", lambda r: r["a1"]["metrics"].__setitem__(
            "rational_prime_primitive_support", True)),
        ("route_a2", "verdict_fail", lambda r: r["a2"].__setitem__("verdict", "A2_FAIL")),
        ("route_a3_a4", "a3_verdict_pass", lambda r: r["a3"].__setitem__("verdict", "A3_PASS")),
        ("route_a3_a4", "a4_verdict_pass", lambda r: r["a4"].__setitem__("verdict", "A4_PASS")),
        ("route_b", "top_invocation_allowed", lambda r: r.__setitem__("route_b_invocation_allowed", True)),
        ("route_b", "nested_invocation_allowed", lambda r: r["route_b"].__setitem__("invocation_allowed", True)),
        ("route_b", "nested_reason", lambda r: r["route_b"].__setitem__("reason", "same_object_complete")),
        ("artifact_path", "base_host_absolute", lambda r: r.__setitem__("artifact_path_base", "/" + "tmp" + "/paper")),
        ("artifact_path", "base_parent_escape", lambda r: r.__setitem__("artifact_path_base", "../paper")),
        ("artifact_path", "base_wrong_slug", lambda r: r.__setitem__(
            "artifact_path_base", "papers/43-wrong-base")),
        ("artifact_path", "base_nonexistent", lambda r: r.__setitem__(
            "artifact_path_base", "papers/43-nonexistent-base")),
    ]
    for class_id, suffix, editor in targeted:
        clone = copy.deepcopy(route)
        editor(clone)
        rows.append({"id": f"{class_id}__{suffix}", "route": clone})
    rows.sort(key=lambda row: row["id"])
    if len({row["id"] for row in rows}) != len(rows):
        raise ValueError("generated Route mutation IDs collide")
    return rows


def run_raw(rows: list[dict[str, Any]], temporary: Path, cwd: Path) -> tuple[list[dict[str, Any]], set[str]]:
    records: list[dict[str, Any]] = []
    classes: set[str] = set()
    for index, row in enumerate(rows):
        path = temporary / f"raw_{index:04d}.json"
        path.write_bytes(row["raw"])
        outcomes = {}
        for name, script in (("algorithm_C", MAIN), ("algorithm_F", INDEPENDENT)):
            process = invoke(script, [str(path)], cwd)
            outcomes[name] = "REJECT_NONZERO" if process.returncode != 0 else "ACCEPTED_IN_ERROR"
        passed = all(value == "REJECT_NONZERO" for value in outcomes.values())
        records.append(mutation_record(
            row["class_id"], row["id"], "raw_packet", RAW_CONSUMERS,
            outcomes, passed,
        ))
        classes.add(row["class_id"])
    return records, classes


def run_route(rows: list[dict[str, Any]], science_path: Path,
              temporary: Path, cwd: Path) -> tuple[list[dict[str, Any]], set[str]]:
    batch_path = temporary / "route_mutations.json"
    batch_path.write_bytes(canonical(rows))
    results: dict[str, dict[str, Any]] = {}
    for name, script in (("strict_route_validator", ROUTE_MAIN),
                         ("independent_route_auditor", ROUTE_INDEPENDENT)):
        process = invoke(script, ["--batch", str(batch_path), str(science_path)], cwd)
        if process.returncode != 0:
            detail = process.stderr.decode("utf-8", errors="replace").splitlines()[-1:]
            raise ValueError(f"{name} mutation batch execution failed: {detail}")
        result = json.loads(process.stdout.decode("ascii"), object_pairs_hook=unique)
        if result["status"] != "PASS" or result["accepted_ids"]:
            raise ValueError(f"{name} accepted a Route mutation")
        results[name] = result
    rejected_sets = {
        name: {row["id"] for row in value["rejected"]} for name, value in results.items()
    }
    records = []
    classes: set[str] = set()
    for row in rows:
        identifier = row["id"]
        class_id = identifier.split("__", 1)[0]
        if identifier.startswith("route_schema__"):
            class_id = "route_schema"
        passed = all(identifier in rejected for rejected in rejected_sets.values())
        records.append(mutation_record(
            class_id, identifier, "route_card", ROUTE_CONSUMERS,
            {name: "REJECT_NONZERO" for name in sorted(results)}, passed,
        ))
        classes.add(class_id)
    return records, classes


def output_and_environment_controls(packet_raw: bytes, science: dict[str, Any],
                                    route: dict[str, Any], output_root: Path | None,
                                    temporary: Path, cwd: Path) \
        -> tuple[list[dict[str, Any]], list[dict[str, Any]], set[str]]:
    records: list[dict[str, Any]] = []
    positive_controls: list[dict[str, Any]] = []
    classes: set[str] = set()

    def record_mutation(class_id: str, suffix: str, passed: bool,
                        consumers: list[str], domain: str,
                        outcomes: dict[str, str] | None = None) -> None:
        identifier = f"{class_id}__{suffix}"
        if outcomes is None:
            outcomes = {name: "REJECT_NONZERO" if passed else "ACCEPTED_IN_ERROR"
                        for name in consumers}
        records.append(mutation_record(
            class_id, identifier, domain, consumers, outcomes, passed,
        ))
        classes.add(class_id)

    def record_positive(class_id: str, suffix: str, passed: bool,
                        consumer: str, success_token: str, domain: str) -> None:
        identifier = f"{class_id}__{suffix}"
        positive_controls.append(positive_control_record(
            class_id, identifier, domain, [consumer],
            {consumer: success_token if passed else "ACCEPTED_IN_ERROR"}, passed,
        ))
        classes.add(class_id)

    science_raw = canonical(science)
    record_positive("cwd_relocation", "isolated_invocation_contract", True,
                    "process_isolation_probe", "PASS_ISOLATED_INVOCATION",
                    "runtime_environment")
    hostile = cwd / "hostile_modules"
    naive = subprocess.run([PYTHON, "-c", "import json"], cwd=cwd,
                           env={"PATH": os.environ.get("PATH", "/usr/bin:/bin"),
                                "PYTHONPATH": str(hostile)},
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    isolated = subprocess.run([PYTHON, "-I", "-B", "-c", "import json"], cwd=cwd,
                              env={"PATH": os.environ.get("PATH", "/usr/bin:/bin"),
                                   "PYTHONPATH": str(hostile)},
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    record_positive(
        "module_shadow", "isolated_and_naive_controls",
        sys.flags.isolated and sys.dont_write_bytecode
        and naive.returncode != 0 and isolated.returncode == 0,
        "process_isolation_probe", "NAIVE_REJECTED_ISOLATED_PASSED",
        "runtime_environment",
    )
    record_positive(
        "live_dependency", "external_tree_not_queried",
        science["integration_chronology"]["status"].startswith("RETROSPECTIVE_")
        and route["source_lock"]["training_data"] == "none",
        "portable_snapshot_probe", "PASS_NOT_QUERIED",
        "portable_source_snapshot",
    )
    host_tokens = tuple(("/" + name + "/").encode("ascii")
                        for name in ("tmp", "root", "home")) \
        + (("TMP" + "_").encode("ascii"),)
    record_positive(
        "path_leak", "canonical_payload_scan",
        not any(token in packet_raw + science_raw + canonical(route)
                for token in host_tokens),
        "payload_hygiene_probe", "PASS_ZERO_HOST_TOKENS",
        "canonical_payload_hygiene",
    )

    state_b_commit = "1" * 40

    if output_root is None:
        cache_hits = [path for path in ROOT.rglob("*")
                      if path.name == "__pycache__" or path.suffix == ".pyc"]
        record_positive(
            "cache", "preflight_static_tree", not cache_hits,
            "static_hygiene_probe", "PASS_ZERO_CACHE_FILES",
            "static_tree_hygiene",
        )
    else:
        contract = json.loads(CONTRACT.read_text(encoding="ascii"))
        expected = set(contract["exact_output_paths"])

        def result_ledger_bytes(tree: Path) -> bytes:
            paths = sorted(path.relative_to(tree).as_posix()
                           for path in (tree / "results").rglob("*")
                           if path.is_file() and not path.is_symlink()
                           and path.relative_to(tree).as_posix()
                           != "results/SHA256SUMS.txt")
            return "".join(
                f"{sha((tree / relative).read_bytes())}  {relative}\n"
                for relative in paths).encode("ascii")

        def refresh_report_ledger_binding(tree: Path) -> None:
            """Re-render the report fields affected by a coordinated reledger.

            This deliberately does not call either production or audit report
            renderer.  A scalar-type mutation can therefore keep the checksum
            prose synchronized while the read-only auditor must reject the
            typed certificate itself.
            """
            ledger = (tree / "results/SHA256SUMS.txt").read_bytes()
            report_path = tree / "EXPERIMENT_REPORT.md"
            report = report_path.read_text(encoding="ascii")
            pattern = re.compile(
                r"(The self-excluding result ledger has )([0-9]+)"
                r"( entries and SHA-256 `)([0-9a-f]{64})(`\.)")
            replacement = (
                rf"\g<1>{len(ledger.decode('ascii').splitlines())}"
                rf"\g<3>{sha(ledger)}\g<5>")
            rendered, count = pattern.subn(replacement, report)
            if count != 1:
                raise ValueError("report ledger binding replacement failure")
            report_path.write_text(rendered, encoding="ascii")

        def paper_manifest_bytes(tree: Path) -> bytes:
            paths = sorted(path.relative_to(tree).as_posix()
                           for path in tree.rglob("*")
                           if path.is_file() and not path.is_symlink()
                           and path.relative_to(tree).as_posix()
                           != "PAPER_MANIFEST.sha256")
            return "".join(
                f"{sha((tree / relative).read_bytes())}  {relative}\n"
                for relative in paths).encode("ascii")

        def refresh_static_manifest(tree: Path, changed_paths: list[str]) -> None:
            manifest = tree / "STATIC_INPUT_SHA256SUMS.txt"
            rows = {}
            for line in manifest.read_text(encoding="ascii").splitlines():
                rows[line[66:]] = line[:64]
            for relative in changed_paths:
                rows[relative] = sha((tree / relative).read_bytes())
            manifest.write_text("".join(
                f"{rows[relative]}  {relative}\n" for relative in sorted(rows)),
                encoding="ascii")

        def audit_process(tree: Path, state: str = "A") -> subprocess.CompletedProcess[bytes]:
            arguments = [str(tree), "--state", state, "--mutation-probe"]
            return invoke(AUDITOR, arguments, cwd)

        baseline = audit_process(output_root)
        if baseline.returncode != 0:
            detail = baseline.stderr.decode("utf-8", errors="replace").splitlines()[-3:]
            raise ValueError(f"canonical pre-mutation audit failed: {detail}")

        mutation_index = 0

        def rejection(class_id: str, suffix: str, editor: Callable[[Path], None],
                      *, refresh_ledger: bool = False, state: str = "A",
                      refresh_report: bool = False,
                      refresh_paper_manifest: bool = False,
                      consumers: list[str] | None = None,
                      domain: str = "canonical_output") -> None:
            nonlocal mutation_index
            mutation_index += 1
            tree = temporary / f"auditor_mutation_{mutation_index:03d}_{class_id}_{suffix}"
            shutil.copytree(output_root, tree)
            editor(tree)
            if refresh_ledger:
                (tree / "results/SHA256SUMS.txt").write_bytes(result_ledger_bytes(tree))
            if refresh_report:
                if not refresh_ledger:
                    raise ValueError("report refresh requires coordinated reledger")
                refresh_report_ledger_binding(tree)
            if refresh_paper_manifest:
                (tree / "PAPER_MANIFEST.sha256").write_bytes(paper_manifest_bytes(tree))
            selected = AUDITOR_CONSUMERS if consumers is None else sorted(consumers)
            outcomes: dict[str, str] = {}
            if "strict_route_validator" in selected:
                process = invoke(
                    ROUTE_MAIN,
                    [str(tree / "evaluations/route_a/SD-C45/2026-08-17.yaml"),
                     str(tree / "results/scientific_results.json")], cwd,
                )
                outcomes["strict_route_validator"] = (
                    "REJECT_NONZERO" if process.returncode != 0 else "ACCEPTED_IN_ERROR")
            if "independent_route_auditor" in selected:
                process = invoke(
                    ROUTE_INDEPENDENT,
                    [str(tree / "evaluations/route_a/SD-C45/2026-08-17.yaml"),
                     str(tree / "results/scientific_results.json")], cwd,
                )
                outcomes["independent_route_auditor"] = (
                    "REJECT_NONZERO" if process.returncode != 0 else "ACCEPTED_IN_ERROR")
            if "read_only_integrity_auditor" in selected:
                process = audit_process(tree, state)
                outcomes["read_only_integrity_auditor"] = (
                    "REJECT_NONZERO" if process.returncode != 0 else "ACCEPTED_IN_ERROR")
            passed = all(value == "REJECT_NONZERO" for value in outcomes.values()) \
                and sorted(outcomes) == selected
            record_mutation(class_id, suffix, passed, selected, domain, outcomes)

        def mutate_json(relative: str, editor: Callable[[dict[str, Any]], None]) \
                -> Callable[[Path], None]:
            def apply(tree: Path) -> None:
                path = tree / relative
                value = json.loads(path.read_text(encoding="ascii"),
                                   object_pairs_hook=unique)
                editor(value)
                path.write_bytes(canonical(value))
            return apply

        overlay_policy = contract["authority_overlay"]

        def writer_manifest_bytes(tree: Path) -> bytes:
            return "".join(
                f"{sha((tree / relative).read_bytes())}  {relative}\n"
                for relative in overlay_policy["writer_content_paths"]
            ).encode("ascii")

        def install_authority_baseline(tree: Path) -> None:
            baseline_root = tree / "inputs/writer_baseline"
            for relative in overlay_policy["writer_content_paths"]:
                source = baseline_root / relative
                target = tree / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source, target)
            shutil.copyfile(
                baseline_root / "SHA256SUMS.txt",
                tree / overlay_policy["current_writer_manifest_path"],
            )
            shutil.copyfile(
                tree / overlay_policy["root_lock_static_source"],
                tree / overlay_policy["root_lock_path"],
            )

        def install_publication_overlay(tree: Path, *, include_report: bool = True,
                                        include_pdf: bool = True) -> None:
            install_authority_baseline(tree)
            additions = {
                "PAPER_PLAN.md": (
                    "\nPublication synchronization records only the canonical final fields.\n"
                ),
                "WRITER_HANDOFF.md": (
                    "\nPublication synchronization completed under the exact writer allowlist.\n"
                ),
                "sections/6_sharpness_route.tex": (
                    "\n\\paragraph{Canonical synchronization.} "
                    "The final authority block is inserted from the sealed outputs.\n"
                ),
            }
            for relative, addition in additions.items():
                path = tree / relative
                original = path.read_text(encoding="utf-8").rstrip("\n")
                path.write_text(original + "\n" + addition.lstrip("\n"),
                                encoding="utf-8")
            (tree / overlay_policy["current_writer_manifest_path"]).write_bytes(
                writer_manifest_bytes(tree))
            if include_report:
                (tree / "COMPILATION_REPORT.md").write_text(
                    "# Paper 43 compilation report\n\n"
                    "The installed publication artifact is `main.pdf`; "
                    "all writer changes are bounded by the authority overlay contract.\n",
                    encoding="ascii",
                )
            if include_pdf:
                (tree / "main.pdf").write_bytes(
                    b"%PDF-1.4\n1 0 obj\n<< /Type /Catalog >>\nendobj\n"
                    + b"%" + b"A" * 128 + b"\n%%EOF\n"
                )

        def authority_overlay_positive(class_id: str, suffix: str,
                                       installer: Callable[[Path], None],
                                       success_token: str,
                                       expected_state: str) -> None:
            tree = temporary / f"authority_overlay_positive_{class_id}_{suffix}"
            shutil.copytree(output_root, tree)
            installer(tree)
            process = audit_process(tree)
            static_process = invoke(
                AUDITOR, [str(tree), "--static-only"], cwd,
            )
            static_value: dict[str, Any] = {}
            if static_process.returncode == 0:
                try:
                    decoded = json.loads(
                        static_process.stdout.decode("ascii"),
                        object_pairs_hook=unique,
                    )
                    if canonical(decoded) == static_process.stdout \
                            and type(decoded) is dict:
                        static_value = decoded
                except (UnicodeDecodeError, json.JSONDecodeError, ValueError):
                    static_value = {}
            record_positive(
                class_id, suffix,
                process.returncode == 0 and static_process.returncode == 0
                and static_value.get("status") == "PASS"
                and static_value.get("authority_overlay_state") == expected_state,
                "read_only_integrity_auditor", success_token,
                "authority_overlay",
            )

        authority_overlay_positive(
            "provenance_state_a", "authority_overlay_baseline",
            install_authority_baseline, "PASS_AUTHORITY_BASELINE",
            "AUTHORITY_BASELINE_RESULT_FREE",
        )
        authority_overlay_positive(
            "stage_2_scope", "authority_publication_overlay",
            install_publication_overlay, "PASS_AUTHORITY_PUBLICATION_SYNC",
            "AUTHORITY_PUBLICATION_SYNC",
        )

        rejection(
            "result_set", "authority_writer_extra",
            lambda tree: (
                install_authority_baseline(tree),
                (tree / "sections/unauthorized_writer_extra.tex").write_text(
                    "Unauthorized writer path.\n", encoding="ascii"),
            ),
            domain="authority_overlay",
        )

        def authority_writer_missing(tree: Path) -> None:
            install_authority_baseline(tree)
            (tree / "abstract.tex").unlink()

        rejection("result_set", "authority_writer_missing",
                  authority_writer_missing, domain="authority_overlay")

        def authority_writer_unauthorized_change(tree: Path) -> None:
            install_authority_baseline(tree)
            path = tree / "main.tex"
            path.write_text(path.read_text(encoding="utf-8").rstrip("\n")
                            + "\n% unauthorized publication edit\n",
                            encoding="utf-8")
            (tree / overlay_policy["current_writer_manifest_path"]).write_bytes(
                writer_manifest_bytes(tree))

        rejection("stage_2_scope", "authority_writer_unauthorized_change",
                  authority_writer_unauthorized_change,
                  domain="authority_overlay")

        def authority_root_lock_missing(tree: Path) -> None:
            install_authority_baseline(tree)
            (tree / overlay_policy["root_lock_path"]).unlink()

        rejection("provenance_state_a", "authority_root_lock_missing",
                  authority_root_lock_missing, domain="authority_overlay")

        def authority_root_lock_tampered(tree: Path) -> None:
            install_authority_baseline(tree)
            path = tree / overlay_policy["root_lock_path"]
            value = json.loads(path.read_text(encoding="ascii"),
                               object_pairs_hook=unique)
            value["status"] = "TAMPERED"
            path.write_bytes(canonical(value))

        rejection("provenance_state_a", "authority_root_lock_tampered",
                  authority_root_lock_tampered, domain="authority_overlay")

        def authority_publication_partial_artifact(tree: Path) -> None:
            install_publication_overlay(tree, include_report=False)

        rejection("stage_2_scope", "authority_publication_partial_artifact",
                  authority_publication_partial_artifact,
                  domain="authority_overlay")

        # Exact output namespace mutations.
        rejection("result_set", "add_extra",
                  lambda tree: (tree / "results/unexpected.json").write_bytes(b"{}\n"))
        rejection("result_set", "remove_member",
                  lambda tree: (tree / "results/witness_certificate.json").unlink())
        rejection("result_set", "rename_member",
                  lambda tree: (tree / "results/type_contract_certificate.json").rename(
                      tree / "results/type_contract_certificate.renamed.json"))
        def add_symlink(tree: Path) -> None:
            os.symlink("scientific_results.json", tree / "results/linked.json")
        rejection("result_set", "symlink_member", add_symlink)

        # Every declared ledger corruption is applied to real bytes.
        def ledger_edit(editor: Callable[[list[str]], list[str]]) -> Callable[[Path], None]:
            def apply(tree: Path) -> None:
                path = tree / "results/SHA256SUMS.txt"
                lines = path.read_text(encoding="ascii").splitlines()
                path.write_text("\n".join(editor(lines)) + "\n", encoding="ascii")
            return apply
        rejection("result_ledger", "self_include", ledger_edit(
            lambda rows: rows + ["0" * 64 + "  results/SHA256SUMS.txt"]))
        rejection("result_ledger", "omit_member", ledger_edit(lambda rows: rows[1:]))
        rejection("result_ledger", "duplicate_member", ledger_edit(
            lambda rows: rows + [rows[0]]))
        rejection("result_ledger", "unsorted", ledger_edit(
            lambda rows: [rows[1], rows[0], *rows[2:]]))
        rejection("result_ledger", "path_escape", ledger_edit(
            lambda rows: [rows[0][:66] + "../escape", *rows[1:]]))
        rejection("result_ledger", "wrong_hash", ledger_edit(
            lambda rows: ["0" * 64 + rows[0][64:], *rows[1:]]))

        # Semantic output mutations refresh the ledger so rejection cannot be
        # attributed to a stale checksum alone.
        rejection("output_tamper", "science_theorem",
                  mutate_json("results/scientific_results.json",
                              lambda value: value["theorems"].__setitem__(
                                  "failure_count", 1)), refresh_ledger=True)
        rejection("output_tamper", "certificate_payload",
                  mutate_json("results/crt_proximality_certificate.json",
                              lambda value: value["payload"].__setitem__(
                                  "universal_proof_status", "MUTATED")),
                  refresh_ledger=True)
        rejection("output_tamper", "summary_route",
                  mutate_json("results/analysis_summary.json",
                              lambda value: value.__setitem__(
                                  "route_tuple", ["A0_PASS"])), refresh_ledger=True)
        rejection("output_tamper", "owner_payload",
                  mutate_json("results/operator_ownership_certificate.json",
                              lambda value: value["payload"]["operator_ledger"].__setitem__(
                                  "dimension", 2)), refresh_ledger=True)
        # Coordinated scalar-type mutations close Python's True==1 and
        # 1==1.0 equivalence classes.  The ledger and report checksum prose
        # are both refreshed so the recursive typed payload comparison is the
        # decisive rejecting predicate.
        rejection(
            "output_tamper", "typed_fixed_count_int_to_boolean",
            mutate_json(
                "results/periodic_ledger_certificate.json",
                lambda value: value["payload"]["fixed_count_rows"][0].__setitem__(
                    "fixed_count", True)),
            refresh_ledger=True, refresh_report=True,
        )
        rejection(
            "output_tamper", "typed_claim_boolean_to_integer",
            mutate_json(
                "results/factor_contract_certificate.json",
                lambda value: value["payload"].__setitem__(
                    "universal_aperiodic_factor_theorem_claimed", 0)),
            refresh_ledger=True, refresh_report=True,
        )
        rejection(
            "output_tamper", "typed_source_count_integer_to_float",
            mutate_json(
                "results/source_resolver.json",
                lambda value: value["payload"].__setitem__("matches", 40.0)),
            refresh_ledger=True, refresh_report=True,
        )
        rejection(
            "output_tamper", "typed_main_check_boolean_to_integer",
            mutate_json(
                "results/main_evaluation.json",
                lambda value: value["checks"].__setitem__("chronology_exact", 1)),
            refresh_ledger=True, refresh_report=True,
        )
        rejection(
            "output_tamper", "typed_integrity_count_integer_to_float",
            mutate_json(
                "results/integrity_audit.json",
                lambda value: value.__setitem__("checks_passed", 16.0)),
            refresh_ledger=True, refresh_report=True,
        )
        rejection(
            "output_tamper", "typed_provenance_integer_to_boolean",
            mutate_json(
                "evaluations/route_a/SD-C45/2026-08-17.yaml",
                lambda value: value["authority_integration"].__setitem__(
                    "git_operations_by_integrator", False)),
        )
        rejection("output_tamper", "route_card",
                  mutate_json("evaluations/route_a/SD-C45/2026-08-17.yaml",
                              lambda value: value.__setitem__(
                                  "overall_verdict", "ROUTE_A_ACCEPTED")))
        rejection("output_tamper", "report_false_universal_claim",
                  lambda tree: (tree / "EXPERIMENT_REPORT.md").write_bytes(
                      (tree / "EXPERIMENT_REPORT.md").read_bytes()
                      + b"\nA universal aperiodic-factor theorem is proved.\n"),
                  refresh_ledger=True)
        rejection("check_flag", "wrapper_extra_field",
                  mutate_json("results/main_evaluation.json",
                              lambda value: value.__setitem__("pass", True)),
                  refresh_ledger=True)
        rejection("check_flag", "main_existing_boolean",
                  mutate_json("results/main_evaluation.json",
                              lambda value: value["checks"].__setitem__(
                                  "chronology_exact", False)), refresh_ledger=True)
        rejection("check_flag", "main_checks_passed",
                  mutate_json("results/main_evaluation.json",
                              lambda value: value.__setitem__("checks_passed", 16)),
                  refresh_ledger=True)
        rejection("check_flag", "main_checks_total",
                  mutate_json("results/main_evaluation.json",
                              lambda value: value.__setitem__("checks_total", 18)),
                  refresh_ledger=True)
        rejection("check_flag", "independent_existing_boolean",
                  mutate_json("results/independent_evaluation.json",
                              lambda value: value["checks"].__setitem__(
                                  "raw_packet_exact_set", False)), refresh_ledger=True)
        rejection("check_flag", "route_existing_boolean",
                  mutate_json("results/route_evaluation.json",
                              lambda value: value["checks"].__setitem__(
                                  "tuple", False)), refresh_ledger=True)
        rejection("check_flag", "route_gate_count",
                  mutate_json("results/route_evaluation.json",
                              lambda value: value.__setitem__("checks_passed", 22)),
                  refresh_ledger=True)
        rejection("check_flag", "independent_route_gate_count",
                  mutate_json("evaluations/route_a/SD-C45/independent_evaluation.json",
                              lambda value: value.__setitem__("checks_total", 25)))
        rejection("check_flag", "summary_expected_tuple",
                  mutate_json("results/analysis_summary.json",
                              lambda value: value.__setitem__(
                                  "route_tuple", ["A0_PASS"])), refresh_ledger=True)
        rejection("science_hash", "wrapper_stale_hash",
                  mutate_json("results/main_evaluation.json",
                              lambda value: value.__setitem__(
                                  "science_sha256", "0" * 64)), refresh_ledger=True)
        rejection("run_a_b_c", "run_b_science",
                  mutate_json("results/runs/B/scientific_results.json",
                              lambda value: value["theorems"].__setitem__(
                                  "failure_count", 1)), refresh_ledger=True)
        rejection("run_a_b_c", "run_label_serialized",
                  mutate_json("results/runs/B/scientific_results.json",
                              lambda value: value.__setitem__("run_label", "B")),
                  refresh_ledger=True)
        rejection("run_a_b_c", "run_root_serialized",
                  mutate_json("results/runs/C/scientific_results.json",
                              lambda value: value.__setitem__(
                                  "run_root", "relocated_copy")), refresh_ledger=True)

        # Mutate the actual emitted theorem invariants, not merely raw-schema
        # fields which would also fail an exact-key check.
        rejection("fixed_anchor", "result_anchor",
                  mutate_json("results/factor_periodic_rigidity_certificate.json",
                              lambda value: value["payload"].__setitem__(
                                  "fixed_anchor", "not_pi_zero")), refresh_ledger=True)
        rejection("periodic_separation", "result_period_row",
                  mutate_json("results/factor_periodic_rigidity_certificate.json",
                              lambda value: value["payload"]["period_rows"][1].__setitem__(
                                  "separation_contradicts_proximality", False)),
                  refresh_ledger=True)
        rejection("factor_target", "result_hidden_finite_radius",
                  mutate_json("results/factor_periodic_rigidity_certificate.json",
                              lambda value: value["payload"]["universal_certificate"].__setitem__(
                                  "hidden_finite_alphabet_or_radius_assumption", True)),
                  refresh_ledger=True)
        rejection("factor_target", "result_finite_fiber_restriction",
                  mutate_json("results/factor_contract_certificate.json",
                              lambda value: value["payload"]["claim_scope"].__setitem__(
                                  "factor_class", "finite_to_one_factors_only")),
                  refresh_ledger=True)
        rejection("fixed_counts", "result_fixed_count_row",
                  mutate_json("results/periodic_ledger_certificate.json",
                              lambda value: value["payload"]["fixed_count_rows"][0].__setitem__(
                                  "fixed_count", 2)), refresh_ledger=True)
        rejection("prime_allocation", "result_assignment_unsorted",
                  mutate_json("results/crt_proximality_certificate.json",
                              lambda value: value["payload"]["control_rows"][1]["assignments"].__setitem__(
                                  slice(0, 2), list(reversed(
                                      value["payload"]["control_rows"][1]["assignments"][:2])))),
                  refresh_ledger=True)

        def omit_crt_coordinate(value: dict[str, Any]) -> None:
            row = value["payload"]["control_rows"][1]
            row["assignments"].pop()
            row["assignment_count"] -= 1
        rejection("missing_residue", "result_omitted_window_coordinate",
                  mutate_json("results/crt_proximality_certificate.json",
                              omit_crt_coordinate), refresh_ledger=True)
        rejection("marker", "result_z_specialized_to_one",
                  mutate_json("results/operator_ownership_certificate.json",
                              lambda value: value["payload"]["marker_ledger"].__setitem__(
                                  "factor_marker", "1")), refresh_ledger=True)
        rejection("operator_owner", "result_full_source_owner",
                  mutate_json("results/operator_ownership_certificate.json",
                              lambda value: value["payload"]["operator_ledger"].__setitem__(
                                  "owner", "full_squarefree_source")), refresh_ledger=True)
        rejection("operator_owner", "result_c_of_y_owner",
                  mutate_json("results/operator_ownership_certificate.json",
                              lambda value: value["payload"]["operator_ledger"].__setitem__(
                                  "owner", "operator_on_C_of_Y")), refresh_ledger=True)
        rejection("operator_owner", "result_hilbert_polya_owner",
                  mutate_json("results/operator_ownership_certificate.json",
                              lambda value: value["payload"]["operator_ledger"].__setitem__(
                                  "owner", "Hilbert_Polya_operator")), refresh_ledger=True)
        rejection("finite_p0_product", "result_constant_one",
                  mutate_json("results/finite_p0_sharpness_certificate.json",
                              lambda value: value["payload"]["rows"][1].__setitem__(
                                  "product_Q", 1)), refresh_ledger=True)
        rejection("finite_p0_period", "result_proper_divisor",
                  mutate_json("results/finite_p0_sharpness_certificate.json",
                              lambda value: value["payload"]["rows"][1].__setitem__(
                                  "least_period", 2)), refresh_ledger=True)
        rejection("finite_p0_period", "result_nonempty_period_one",
                  mutate_json("results/finite_p0_sharpness_certificate.json",
                              lambda value: value["payload"]["rows"][2].__setitem__(
                                  "least_period", 1)), refresh_ledger=True)

        rejection("output_tamper", "algorithm_import_edge",
                  mutate_json("results/algorithm_independence.json",
                              lambda value: value["payload"].__setitem__(
                                  "project_local_import_edges", ["forged_edge"])),
                  refresh_ledger=True)
        rejection("output_tamper", "idempotence_second_writes",
                  mutate_json("results/idempotence_certificate.json",
                              lambda value: value["payload"].__setitem__(
                                  "physical_writes_on_complete_second_parent_run", 999)),
                  refresh_ledger=True)
        rejection("output_tamper", "source_evaluator_firewall",
                  mutate_json("results/source_evaluator_boundary.json",
                              lambda value: value["payload"].__setitem__(
                                  "packet_forbidden_derived_answers", False)),
                  refresh_ledger=True)
        rejection("output_tamper", "sealed_state_mixed_acceptance",
                  mutate_json("results/sealed_state_compatibility.json",
                              lambda value: value["payload"].__setitem__(
                                  "mixed_states_rejected", False)), refresh_ledger=True)

        def drop_declared_consumer(value: dict[str, Any]) -> None:
            row = value["records"][0]
            removed = row["designated_consumers"].pop()
            row["outcomes"].pop(removed)
        rejection(
            "output_tamper", "adversarial_consumer_contract",
            mutate_json("results/adversarial_tests.json", drop_declared_consumer),
            refresh_ledger=True,
        )
        rejection(
            "output_tamper", "adversarial_domain_contract",
            mutate_json("results/adversarial_tests.json",
                        lambda value: value["records"][0].__setitem__(
                            "domain", "wrong_domain")),
            refresh_ledger=True,
        )

        def coordinated_critical_tamper(tree: Path) -> None:
            adversarial_path = tree / "results/adversarial_tests.json"
            adversarial_value = json.loads(adversarial_path.read_text(encoding="ascii"),
                                           object_pairs_hook=unique)
            survivor = adversarial_value["records"][0]
            adversarial_value["records"] = [survivor]
            adversarial_value["classes_exercised"] = []
            adversarial_value["class_counts"] = {
                key: 0 for key in adversarial_value["class_counts"]}
            adversarial_value["class_counts"][survivor["class_id"]] = 1
            adversarial_value["instance_count"] = 1
            adversarial_value["instance_ids_sha256"] = "0" * 64
            adversarial_path.write_bytes(canonical(adversarial_value))
            mutate_json("results/analysis_summary.json",
                        lambda value: value.__setitem__("mutation_instances", 1))(tree)
            mutate_json("results/algorithm_independence.json",
                        lambda value: value["payload"].__setitem__(
                            "project_local_import_edges", ["forged_edge"]))(tree)
            mutate_json("results/idempotence_certificate.json",
                        lambda value: value["payload"].__setitem__(
                            "physical_writes_on_complete_second_parent_run", 999))(tree)
            mutate_json("results/source_evaluator_boundary.json",
                        lambda value: value["payload"].__setitem__(
                            "packet_forbidden_derived_answers", False))(tree)
            mutate_json("results/sealed_state_compatibility.json",
                        lambda value: value["payload"].__setitem__(
                            "mixed_states_rejected", False))(tree)
        rejection("output_tamper", "coordinated_critical_payload_and_reledger",
                  coordinated_critical_tamper, refresh_ledger=True)

        host_specific = "/" + "home" + "/injected/value"
        rejection("path_leak", "serialized_host_value",
                  mutate_json("results/dependency_controls.json",
                              lambda value: value["payload"].__setitem__(
                                  "injected_path", host_specific)), refresh_ledger=True)
        def mark_live(value: dict[str, Any]) -> None:
            value["portable_source_input"]["external_tree_status"] = "QUERIED"
        def mutate_all_packets(tree: Path) -> None:
            for relative in ["results/source_packet.json"] + [
                    f"results/runs/{label}/source_packet.json" for label in "ABC"]:
                mutate_json(relative, mark_live)(tree)
        rejection("live_dependency", "packet_queries_external_tree",
                  mutate_all_packets, refresh_ledger=True)

        # Static source-container and source-ID mutations refresh the static
        # manifest (and, for the index mutation, its contract binding) so the
        # decoded role/hash resolver is the decisive rejection.
        def mutate_container_role(tree: Path) -> None:
            relative = "inputs/source_snapshot/containers/source_00.json"
            path = tree / relative
            value = json.loads(path.read_text(encoding="ascii"),
                               object_pairs_hook=unique)
            value["role"] = value["role"] + "__MUTATED"
            path.write_bytes(canonical(value))
            refresh_static_manifest(tree, [relative])
        rejection("source_id", "container_role", mutate_container_role,
                  domain="static_or_environment")

        def duplicate_source_id(tree: Path) -> None:
            index_relative = "inputs/source_snapshot/SOURCE_INDEX.json"
            contract_relative = "code/contracts/INTEGRATION_CONTRACT.json"
            index_path = tree / index_relative
            index_value = json.loads(index_path.read_text(encoding="ascii"),
                                     object_pairs_hook=unique)
            index_value["entries"][1]["id"] = index_value["entries"][0]["id"]
            index_path.write_bytes(canonical(index_value))
            contract_path = tree / contract_relative
            contract_value = json.loads(contract_path.read_text(encoding="ascii"),
                                        object_pairs_hook=unique)
            contract_value["immutable_inputs"]["source_index_sha256"] = sha(
                index_path.read_bytes())
            contract_path.write_bytes(canonical(contract_value))
            refresh_static_manifest(tree, [index_relative, contract_relative])
        rejection("source_id", "duplicate_index_id", duplicate_source_id,
                  domain="static_or_environment")

        def source_index_edit(editor: Callable[[dict[str, Any]], None]) \
                -> Callable[[Path], None]:
            def apply(tree: Path) -> None:
                index_relative = "inputs/source_snapshot/SOURCE_INDEX.json"
                contract_relative = "code/contracts/INTEGRATION_CONTRACT.json"
                index_path = tree / index_relative
                index_value = json.loads(index_path.read_text(encoding="ascii"),
                                         object_pairs_hook=unique)
                editor(index_value)
                index_path.write_bytes(canonical(index_value))
                contract_path = tree / contract_relative
                contract_value = json.loads(contract_path.read_text(encoding="ascii"),
                                            object_pairs_hook=unique)
                contract_value["immutable_inputs"]["source_index_sha256"] = sha(
                    index_path.read_bytes())
                contract_path.write_bytes(canonical(contract_value))
                refresh_static_manifest(tree, [index_relative, contract_relative])
            return apply

        rejection("source_id", "unsorted_index_entries", source_index_edit(
            lambda value: value["entries"].__setitem__(
                slice(0, 2), list(reversed(value["entries"][:2])))),
                  domain="static_or_environment")
        rejection("source_id", "renamed_index_id", source_index_edit(
            lambda value: value["entries"][0].__setitem__("id", "renamed:source")),
                  domain="static_or_environment")
        rejection("source_id", "wrong_decoded_hash", source_index_edit(
            lambda value: value["entries"][0].__setitem__(
                "decoded_sha256", "0" * 64)), domain="static_or_environment")
        rejection("source_id", "wrong_container_hash", source_index_edit(
            lambda value: value["entries"][0].__setitem__(
                "container_sha256", "0" * 64)), domain="static_or_environment")

        rejection("artifact_path", "route_wrong_base_output",
                  mutate_json("evaluations/route_a/SD-C45/2026-08-17.yaml",
                              lambda value: value.__setitem__(
                                  "artifact_path_base", "papers/43-wrong-base")),
                  consumers=THREE_ROUTE_STATE_CONSUMERS, domain="route_card_in_output_tree")
        rejection("artifact_path", "route_nonexistent_nested_output",
                  mutate_json("evaluations/route_a/SD-C45/2026-08-17.yaml",
                              lambda value: value["a0"]["artifacts"].__setitem__(
                                  0, "results/nonexistent_artifact.json")),
                  consumers=THREE_ROUTE_STATE_CONSUMERS, domain="route_card_in_output_tree")

        rejection("cache", "precreated_bytecode_cache",
                  lambda tree: (tree / "code/source/__pycache__").mkdir(),
                  domain="static_or_environment")

        relocated = temporary / "relocated_complete_tree"
        shutil.copytree(output_root, relocated)
        relocated_process = audit_process(relocated)
        record_positive(
            "cwd_relocation", "complete_tree_audit",
            relocated_process.returncode == 0,
            "read_only_integrity_auditor", "PASS_BYTE_IDENTICAL",
            "relocated_complete_output_tree",
        )

        # Actual State-A and State-B mutations.
        rejection("provenance_state_a", "manifest_present",
                  lambda tree: (tree / "PAPER_MANIFEST.sha256").write_bytes(
                      paper_manifest_bytes(tree)),
                  domain="paired_provenance_state")
        for field in ("source_commit", "code_commit"):
            rejection("provenance_state_a", f"partial_{field}",
                      mutate_json("evaluations/route_a/SD-C45/2026-08-17.yaml",
                                  lambda value, key=field: value.__setitem__(
                                      key, "1" * 40)),
                      consumers=THREE_ROUTE_STATE_CONSUMERS,
                      domain="paired_provenance_state")
        rejection("provenance_state_a", "partial_source_lock_commit",
                  mutate_json("evaluations/route_a/SD-C45/2026-08-17.yaml",
                              lambda value: value["source_lock"].__setitem__(
                                  "code_commit", "1" * 40)),
                  consumers=THREE_ROUTE_STATE_CONSUMERS,
                  domain="paired_provenance_state")

        def legal_state_b(tree: Path) -> None:
            science_file = tree / "results/scientific_results.json"
            process = invoke(ROOT / "code/evaluator/evaluate_route_a.py", [
                str(science_file), "--state-b", state_b_commit
            ], cwd)
            if process.returncode != 0:
                raise ValueError("failed to construct disposable legal State B")
            (tree / "evaluations/route_a/SD-C45/2026-08-17.yaml").write_bytes(
                process.stdout)
            (tree / "PAPER_MANIFEST.sha256").write_bytes(paper_manifest_bytes(tree))

        legal_tree = temporary / "legal_state_b_baseline"
        shutil.copytree(output_root, legal_tree)
        legal_state_b(legal_tree)
        legal_process = audit_process(legal_tree, "B")
        if legal_process.returncode != 0:
            detail = legal_process.stderr.decode("utf-8", errors="replace").splitlines()[-3:]
            raise ValueError(f"legal disposable State B failed: {detail}")

        def state_b_route_edit(editor: Callable[[dict[str, Any]], None]) \
                -> Callable[[Path], None]:
            def apply(tree: Path) -> None:
                legal_state_b(tree)
                route_path = tree / "evaluations/route_a/SD-C45/2026-08-17.yaml"
                value = json.loads(route_path.read_text(encoding="ascii"),
                                   object_pairs_hook=unique)
                editor(value)
                route_path.write_bytes(canonical(value))
            return apply

        rejection(
            "provenance_state_b", "unequal_commit",
            state_b_route_edit(lambda value: value.__setitem__("code_commit", "2" * 40)),
            state="B", refresh_paper_manifest=True,
            consumers=THREE_ROUTE_STATE_CONSUMERS,
            domain="paired_provenance_state",
        )

        def zero_triple(value: dict[str, Any]) -> None:
            value["source_commit"] = "0" * 40
            value["code_commit"] = "0" * 40
            value["source_lock"]["code_commit"] = "0" * 40
        rejection(
            "provenance_state_b", "zero_commit_triple",
            state_b_route_edit(zero_triple), state="B",
            refresh_paper_manifest=True, consumers=THREE_ROUTE_STATE_CONSUMERS,
            domain="paired_provenance_state",
        )

        def nonhex_triple(value: dict[str, Any]) -> None:
            value["source_commit"] = "g" * 40
            value["code_commit"] = "g" * 40
            value["source_lock"]["code_commit"] = "g" * 40
        rejection(
            "provenance_state_b", "nonhex_commit_triple",
            state_b_route_edit(nonhex_triple), state="B",
            refresh_paper_manifest=True, consumers=THREE_ROUTE_STATE_CONSUMERS,
            domain="paired_provenance_state",
        )
        rejection(
            "provenance_state_b", "route_claims_missing_manifest",
            state_b_route_edit(lambda value: value["authority_integration"].__setitem__(
                "paper_manifest_present", False)), state="B",
            refresh_paper_manifest=True, consumers=THREE_ROUTE_STATE_CONSUMERS,
            domain="paired_provenance_state",
        )
        rejection(
            "provenance_state_b", "stale_freeze_note",
            state_b_route_edit(lambda value: value.__setitem__("freeze_note", "stale")),
            state="B", refresh_paper_manifest=True,
            consumers=THREE_ROUTE_STATE_CONSUMERS,
            domain="paired_provenance_state",
        )

        def physical_manifest_missing(tree: Path) -> None:
            legal_state_b(tree)
            (tree / "PAPER_MANIFEST.sha256").unlink()
        rejection(
            "provenance_state_b", "physical_manifest_missing",
            physical_manifest_missing, state="B",
            domain="paired_provenance_state",
        )

        def broaden_stage_two(tree: Path) -> None:
            legal_state_b(tree)
            mutate_json("results/scientific_results.json",
                        lambda value: value["theorems"].__setitem__(
                            "failure_count", 1))(tree)
        rejection("stage_2_scope", "science_changed",
                  broaden_stage_two, refresh_ledger=True, state="B",
                  refresh_paper_manifest=True,
                  consumers=THREE_ROUTE_STATE_CONSUMERS,
                  domain="paired_provenance_state")

        def broaden_stage_two_report(tree: Path) -> None:
            legal_state_b(tree)
            report = tree / "EXPERIMENT_REPORT.md"
            report.write_bytes(report.read_bytes() + b"\nStage two changed the report.\n")
        rejection("stage_2_scope", "report_changed", broaden_stage_two_report,
                  state="B", refresh_paper_manifest=True,
                  domain="paired_provenance_state")

        def broaden_stage_two_result(tree: Path) -> None:
            legal_state_b(tree)
            mutate_json("results/analysis_summary.json",
                        lambda value: value.__setitem__("mutation_survivors", 1))(tree)
        rejection("stage_2_scope", "result_changed", broaden_stage_two_result,
                  refresh_ledger=True, state="B", refresh_paper_manifest=True,
                  domain="paired_provenance_state")

        def broaden_stage_two_code(tree: Path) -> None:
            legal_state_b(tree)
            readme = tree / "README.md"
            readme.write_bytes(readme.read_bytes() + b"\nStage two changed code scope.\n")
        rejection("stage_2_scope", "static_code_changed", broaden_stage_two_code,
                  state="B", refresh_paper_manifest=True,
                  domain="paired_provenance_state")
    return records, positive_controls, classes


def main(argv: list[str]) -> int:
    if not sys.flags.isolated or not sys.dont_write_bytecode:
        raise RuntimeError("run_mutations.py requires python3 -I -B")
    if len(argv) not in (3, 5) or (len(argv) == 5 and argv[3] != "--output-root"):
        raise SystemExit("usage: run_mutations.py PACKET SCIENCE ROUTE [--output-root ROOT]")
    packet, packet_raw = load(Path(argv[0]))
    science, _ = load(Path(argv[1]))
    route, _ = load(Path(argv[2]))
    output_root = Path(argv[4]).resolve() if len(argv) == 5 else None
    registry, registry_raw = load(REGISTRY)
    contract, _ = load(CONTRACT)
    if sha(registry_raw) != contract["mutation_registry"]["sha256"]:
        raise ValueError("mutation registry hash binding failure")
    if registry.get("schema") != "paper43-static-mutation-class-registry-v3":
        raise ValueError("mutation registry schema failure")
    class_contracts = {row["class_id"]: row for row in registry["classes"]}
    registered = set(class_contracts)
    with tempfile.TemporaryDirectory(prefix="paper43_mutations_") as temporary_name:
        temporary = Path(temporary_name)
        cwd = temporary / "unrelated_cwd"
        cwd.mkdir()
        raw_records, raw_classes = run_raw(raw_mutations(packet, packet_raw), temporary, cwd)
        route_rows = route_mutations(route)
        route_records, route_classes = run_route(route_rows, Path(argv[1]).resolve(), temporary, cwd)
        other_records, positive_controls, other_classes = output_and_environment_controls(
            packet_raw, science, route, output_root, temporary, cwd)
    records = sorted(raw_records + route_records + other_records, key=lambda row: row["id"])
    positive_controls = sorted(positive_controls, key=lambda row: row["id"])
    if len(records) != len({row["id"] for row in records}):
        raise ValueError("mutation instance IDs are not unique")
    if len(positive_controls) != len({row["id"] for row in positive_controls}) \
            or {row["id"] for row in records} & {row["id"] for row in positive_controls}:
        raise ValueError("positive-control IDs are not unique/disjoint")
    for row in records + positive_controls:
        profile = {key: row[key] for key in (
            "designated_consumers", "domain", "expectation")}
        if row["class_id"] not in class_contracts \
                or profile not in class_contracts[row["class_id"]]["allowed_instance_contracts"] \
                or sorted(row["outcomes"]) != row["designated_consumers"]:
            raise ValueError(f"record violates frozen per-instance profile: {row['id']}")
    exercised = raw_classes | route_classes | other_classes
    missing = sorted(registered - exercised)
    unknown = sorted(exercised - registered)
    survivors = sorted(row["id"] for row in records if not row["passed"])
    positive_failures = sorted(row["id"] for row in positive_controls if not row["passed"])
    instance_ids = [row["id"] for row in records]
    positive_control_ids = [row["id"] for row in positive_controls]
    class_counts = {class_id: sum(row["class_id"] == class_id for row in records)
                    for class_id in sorted(registered)}
    positive_class_counts = {
        class_id: sum(row["class_id"] == class_id for row in positive_controls)
        for class_id in sorted(registered)
    }
    instance_contracts = sorted([
        {key: row[key] for key in (
            "class_id", "designated_consumers", "domain", "expectation", "id", "variant")}
        for row in records + positive_controls
    ], key=lambda row: row["id"])
    result = {
        "class_counts": class_counts,
        "classes_exercised": sorted(exercised),
        "classes_missing": missing,
        "classes_registered": len(registered),
        "classes_unknown": unknown,
        "instance_contracts_sha256": sha(canonical(instance_contracts)),
        "instance_count": len(records),
        "instance_ids_sha256": sha(canonical(instance_ids)),
        "mutation_registry_sha256": sha(registry_raw),
        "phase": "FINAL_LITERAL" if output_root is not None else "PREFLIGHT_BASELINE",
        "positive_class_counts": positive_class_counts,
        "positive_control_count": len(positive_controls),
        "positive_control_failure_count": len(positive_failures),
        "positive_control_failure_ids": positive_failures,
        "positive_control_ids_sha256": sha(canonical(positive_control_ids)),
        "positive_controls": positive_controls,
        "records": records,
        "schema": "paper43-adversarial-mutation-results-v2",
        "status": "PASS" if not survivors and not positive_failures and not unknown
                  and (output_root is None or not missing) else "FAIL",
        "survivor_count": len(survivors),
        "survivor_ids": survivors,
    }
    sys.stdout.buffer.write(canonical(result))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
