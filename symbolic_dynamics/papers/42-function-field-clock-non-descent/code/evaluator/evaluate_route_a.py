#!/usr/bin/env python3
"""Deterministic strict Route-A v0.2 renderer/validator for Paper 42."""

from __future__ import annotations

import copy
import hashlib
import json
import re
import stat
import sys
from pathlib import Path, PurePosixPath
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[2]
PENDING = "PENDING_FIRST_ARTIFACT_COMMIT"
ZERO = "0" * 40
ROUTE_REL = "evaluations/route_a/SD-C44/2026-08-17.yaml"
MANIFEST_REL = "PAPER_MANIFEST.sha256"
STAGE1_NOTE = (
    "State A authority artifact has source_commit, code_commit, and "
    "source_lock.code_commit equal to PENDING_FIRST_ARTIFACT_COMMIT and no "
    "PAPER_MANIFEST.sha256. State B is metadata-only: one identical lowercase "
    "nonzero 40-hex State-A commit replaces those three fields and a C-sorted "
    "self-excluding PAPER_MANIFEST.sha256 is added."
)


class RouteReject(Exception):
    def __init__(self, code: str, detail: str | None = None) -> None:
        self.code = code
        self.detail = detail
        super().__init__(code)


def canonical_json(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True) + "\n").encode("ascii")


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def strict_equal(left: Any, right: Any) -> bool:
    if type(left) is not type(right):
        return False
    if type(left) is dict:
        return list(left) == list(right) and all(strict_equal(left[key], right[key]) for key in left)
    if type(left) is list:
        return len(left) == len(right) and all(strict_equal(a, b) for a, b in zip(left, right))
    return left == right


def duplicate_safe_mapping(loader: yaml.SafeLoader, node: yaml.MappingNode, deep: bool = False) -> dict[Any, Any]:
    result: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise RouteReject("DUPLICATE_YAML_KEY", str(key))
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


class StrictLoader(yaml.SafeLoader):
    pass


StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, duplicate_safe_mapping)


def load_json(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    value = json.loads(raw)
    if type(value) is not dict or canonical_json(value) != raw:
        raise RouteReject("NONCANONICAL_SCIENCE_JSON")
    return value


def sealed_note(commit: str) -> str:
    return (
        f"State A artifact commit {commit} contained the three "
        "PENDING_FIRST_ARTIFACT_COMMIT fields and no PAPER_MANIFEST.sha256. "
        "State B is metadata-only: source_commit, code_commit, and "
        "source_lock.code_commit are sealed to that same commit and the "
        "C-sorted self-excluding PAPER_MANIFEST.sha256 is added."
    )


def safe_path(value: Any) -> bool:
    if type(value) is not str or not value or "\\" in value or "\x00" in value:
        return False
    path = PurePosixPath(value)
    return not path.is_absolute() and all(part not in ("", ".", "..") for part in path.parts)


def artifact_owned_path(value: Any) -> bool:
    """Recognize the two renderer-owned artifact namespaces."""
    return safe_path(value) and (
        value.startswith("preauthority/") or value.startswith("results/")
    )


def contained_regular_file(root: Path, value: Any) -> bool:
    """Reject every symlink component before testing the final regular file."""
    if not safe_path(value):
        return False
    current = root
    parts = PurePosixPath(value).parts
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


def expected_route(science: dict[str, Any], commit: str, manifest_present: bool, root: Path = ROOT) -> dict[str, Any]:
    if science.get("schema") != "paper42-exact-science-projection-v1" or science.get("candidate_id") != "SD-C44":
        raise RouteReject("SCIENCE_CONTRACT_MISMATCH")
    if science.get("route", {}).get("route_tuple") != [
        "A0_WEAK_ARITHMETIC_RELATION", "A1_PASS_ANALYTIC",
        "A2_ANALYTIC_DETERMINANT", "A3_FAIL", "A4_FAIL",
    ]:
        raise RouteReject("SCIENCE_CONTRACT_MISMATCH")
    if commit == PENDING:
        if manifest_present:
            raise RouteReject("PAIRED_STATE_MISMATCH")
        state = "STATE_A"
        note = STAGE1_NOTE
    else:
        if re.fullmatch(r"[0-9a-f]{40}", commit) is None or commit == ZERO or not manifest_present:
            raise RouteReject("PAIRED_STATE_MISMATCH")
        state = "STATE_B"
        note = sealed_note(commit)
    template_path = root / "preauthority/ROUTE_EXPECTATION.yaml"
    try:
        template = yaml.load(template_path.read_bytes(), Loader=StrictLoader)
    except RouteReject:
        raise
    except Exception as exc:
        raise RouteReject("IMMUTABLE_ROUTE_EXPECTATION_PARSE_FAILURE") from exc
    route = copy.deepcopy(template)
    route["source_commit"] = commit
    route["code_commit"] = commit
    route["artifact_path_base"] = "papers/42-function-field-clock-non-descent"
    route["freeze_note"] = note
    route["source_lock"]["code_commit"] = commit
    route["source_lock"]["artifact_paths"] = [
        "preauthority/SOURCE_LOCK.md",
        "preauthority/OBJECT_MARKER_OPERATOR_CONTRACT.md",
        "preauthority/DERIVATION_PACKAGE.md",
        "preauthority/PROOF_PACKAGE.md",
        "preauthority/THEOREM_FALSIFIERS.md",
        "preauthority/EXACT_WITNESS_LEDGER.md",
        "preauthority/LITERATURE_NOVELTY_AUDIT.md",
        "preauthority/SELECTION_AND_PROVENANCE.md",
        "preauthority/ROUTE_RECORD_CENSUS.md",
        "preauthority/DA_HANDOFF.md",
        "preauthority/SOURCE_HASHES.sha256",
    ]
    layer_artifacts = {
        "a0": [
            "preauthority/SOURCE_LOCK.md", "preauthority/PROOF_PACKAGE.md",
            "preauthority/EXACT_WITNESS_LEDGER.md", "results/witness_certificate.json",
            "results/source_resolver.json",
        ],
        "a1": [
            "preauthority/DERIVATION_PACKAGE.md", "preauthority/PROOF_PACKAGE.md",
            "preauthority/OBJECT_MARKER_OPERATOR_CONTRACT.md",
            "results/function_field_positive_control.json", "results/selection_resolver.json",
        ],
        "a2": [
            "preauthority/OBJECT_MARKER_OPERATOR_CONTRACT.md", "preauthority/DERIVATION_PACKAGE.md",
            "preauthority/PROOF_PACKAGE.md", "results/determinant_coefficient_certificate.json",
            "results/operator_ownership_certificate.json",
        ],
        "a3": [
            "preauthority/DERIVATION_PACKAGE.md", "preauthority/LITERATURE_NOVELTY_AUDIT.md",
            "preauthority/SOURCE_HASHES.sha256", "results/scientific_results.json",
        ],
        "a4": [
            "preauthority/OBJECT_MARKER_OPERATOR_CONTRACT.md", "preauthority/THEOREM_FALSIFIERS.md",
            "preauthority/LITERATURE_NOVELTY_AUDIT.md", "results/operator_ownership_certificate.json",
            "results/algorithm_independence.json",
        ],
    }
    for layer, artifacts in layer_artifacts.items():
        route[layer]["artifacts"] = artifacts
        route[layer]["verdict"] = science["route"][layer + "_verdict"]
        route[layer]["evidence_status"] = science["route"][layer + "_evidence_status"]
    count_rows = science["necklace_census"]["rows"]
    by = {(row["q"], row["word_length"]): row["primitive_necklace_count"] for row in count_rows}
    route["a1"]["metrics"] = {
        "cyclic_invariance_failures": 0,
        "exact_primitive_witness": "[01]",
        "length_one_counts_q_2_3_5": [by[(q, 1)] for q in [2, 3, 5]],
        "length_two_counts_q_2_3_5": [by[(q, 2)] for q in [2, 3, 5]],
        "primitive_count_formula": "N_q_n_equals_one_over_n_sum_d_divides_n_mu_d_q_power_n_over_d",
        "rational_prime_clock_projection_failures": 1,
        "repetition_failures_on_source": 0,
        "target_multiplicity_failures": 1,
    }
    route["a2"]["metrics"] = {
        "control_margin": "first_marked_coefficient_analytic_mismatch",
        "cutoff_drift": "not_applicable_exact_theorem",
        "extra_zero_count": "not_applicable",
        "missing_zero_count": "not_applicable",
        "precision_drift": "zero_exact_arithmetic",
        "root_count_discrepancy": "not_applicable",
        "zero_error_test": "not_applicable",
        "zero_error_train": "not_applicable",
        "zero_error_validation": "not_applicable",
    }
    route["projection_firewall"]["declared_repairs_are_exhaustive"] = science["repair_classification"]["declared_repairs_are_exhaustive"]
    route["typed_return_map"]["same_type_identification_exists"] = False
    route["target_and_root_metrics"] = {
        "exact_witness_max_word_length": 2,
        "numerical_root_search_used": False,
        "source_fields_checked": [2, 3, 5],
        "target_zero_data_used": False,
    }
    contract_raw = (root / "code/contracts/INTEGRATION_CONTRACT.json").read_bytes()
    registry_raw = (root / "code/contracts/MUTATION_REGISTRY.json").read_bytes()
    science_raw = canonical_json(science)
    route["authority_integration"] = {
        "chronology_status": science["integration_chronology"]["status"],
        "integration_contract_sha256": digest(contract_raw),
        "mutation_registry_sha256": digest(registry_raw),
        "paired_state": state,
        "scientific_results_sha256": digest(science_raw),
        "status": "CANONICAL_PENDING_FIRST_ARTIFACT_COMMIT" if state == "STATE_A" else "SEALED_METADATA_ONLY_STATE_B",
    }
    route["terminal_codes"] = science["terminal_codes"]
    route["route_tuple"] = science["route"]["route_tuple"]
    route["overall_verdict"] = science["route"]["overall_verdict"]
    route["claim_boundary"] = science["claim_scope"]["scope"]
    route["route_b"] = {
        "invocation_allowed": False,
        "reason": "same_object_rational_prime_projection_and_global_structure_fail",
    }
    route["route_b_invocation_allowed"] = science["route"]["route_b_invocation_allowed"]
    route["branch_status"] = science["route"]["branch_status"]
    return route


class StableDumper(yaml.SafeDumper):
    pass


def render_route(science: dict[str, Any], commit: str = PENDING, manifest_present: bool = False, root: Path = ROOT) -> bytes:
    route = expected_route(science, commit, manifest_present, root)
    text = yaml.dump(
        route,
        Dumper=StableDumper,
        allow_unicode=False,
        default_flow_style=False,
        explicit_start=False,
        sort_keys=False,
        width=1000,
    )
    raw = text.encode("ascii")
    if not raw.endswith(b"\n"):
        raw += b"\n"
    return raw


def all_artifact_paths(route: dict[str, Any]) -> list[str]:
    source_lock = route.get("source_lock")
    if type(source_lock) is not dict or type(source_lock.get("artifact_paths")) is not list:
        raise RouteReject("ROUTE_CANONICAL_PAYLOAD_MISMATCH")
    paths = list(source_lock["artifact_paths"])
    for layer in ["a0", "a1", "a2", "a3", "a4"]:
        layer_value = route.get(layer)
        if type(layer_value) is not dict or type(layer_value.get("artifacts")) is not list:
            raise RouteReject("ROUTE_CANONICAL_PAYLOAD_MISMATCH")
        paths.extend(layer_value["artifacts"])
    return paths


def validate_route(raw: bytes, manifest_present: bool, root: Path = ROOT) -> dict[str, Any]:
    try:
        route = yaml.load(raw, Loader=StrictLoader)
    except RouteReject:
        raise
    except Exception as exc:
        raise RouteReject("INVALID_ROUTE_YAML", type(exc).__name__) from exc
    if type(route) is not dict:
        raise RouteReject("ROUTE_CANONICAL_PAYLOAD_MISMATCH", "top")
    source_lock = route.get("source_lock")
    if type(source_lock) is not dict:
        raise RouteReject("PAIRED_STATE_MISMATCH")
    commits = [route.get("source_commit"), route.get("code_commit"), source_lock.get("code_commit")]
    if commits == [PENDING, PENDING, PENDING] and not manifest_present:
        commit = PENDING
    elif len(set(commits)) == 1 and type(commits[0]) is str and re.fullmatch(r"[0-9a-f]{40}", commits[0]) and commits[0] != ZERO and manifest_present:
        commit = commits[0]
    else:
        raise RouteReject("PAIRED_STATE_MISMATCH")
    if route.get("artifact_path_base") != "papers/42-function-field-clock-non-descent":
        raise RouteReject("ARTIFACT_BASE_MISMATCH")
    paths = all_artifact_paths(route)
    if any(not safe_path(path) for path in paths):
        raise RouteReject("UNSAFE_ARTIFACT_PATH")
    if any(not artifact_owned_path(path) for path in paths):
        raise RouteReject("ARTIFACT_OWNERSHIP_MISMATCH")
    if any(not contained_regular_file(root, path) for path in paths):
        raise RouteReject("MISSING_ARTIFACT")
    schema = json.loads((root / "code/contracts/ROUTE_A_V0_2_SCHEMA.json").read_bytes())
    if set(route) == set(schema["exact_top_level_keys"]) \
            and list(route) != schema["ordered_top_level_keys"]:
        raise RouteReject("ROUTE_RAW_SERIALIZATION_MISMATCH")
    science = load_json(root / "results/scientific_results.json")
    expected = expected_route(science, commit, manifest_present, root)
    if not strict_equal(route, expected):
        raise RouteReject("ROUTE_CANONICAL_PAYLOAD_MISMATCH")
    if raw != render_route(science, commit, manifest_present, root):
        raise RouteReject("ROUTE_RAW_SERIALIZATION_MISMATCH")
    if list(route) != schema["ordered_top_level_keys"] or set(route) != set(schema["exact_top_level_keys"]):
        raise RouteReject("ROUTE_SCHEMA_MISMATCH")
    checks = {name: True for name in [
        "a0", "a1", "a2", "a3", "a4", "artifact_paths", "authority_integration",
        "canonical_payload", "claim_scope", "chronology", "evidence_statuses", "overall",
        "paired_state", "raw_serialization", "route_b", "route_tuple", "schema", "science_hash",
        "source_lock", "terminal_codes", "type_and_owner",
    ]}
    return {
        "check_count": len(checks),
        "checks": checks,
        "overall_verdict": route["overall_verdict"],
        "paired_state": "STATE_A" if commit == PENDING else "STATE_B",
        "route_b_invocation_allowed": route["route_b_invocation_allowed"],
        "route_tuple": route["route_tuple"],
        "schema": "paper42-route-evaluation-v1",
        "terminal_codes": route["terminal_codes"],
    }


def main(argv: list[str]) -> int:
    try:
        if len(argv) == 5 and argv[1] == "render":
            root = Path(argv[4])
            science = load_json(Path(argv[2]))
            commit = PENDING if argv[3] == "pending" else argv[3]
            sys.stdout.buffer.write(render_route(science, commit, commit != PENDING, root))
            return 0
        if len(argv) == 5 and argv[1] == "validate":
            if argv[3] not in {"absent", "present"}:
                raise RouteReject("ARGUMENT_CONTRACT")
            root = Path(argv[4])
            result = validate_route(Path(argv[2]).read_bytes(), argv[3] == "present", root)
            sys.stdout.buffer.write(canonical_json(result))
            return 0
        raise RouteReject("ARGUMENT_CONTRACT")
    except RouteReject as exc:
        suffix = "" if exc.detail is None else ":" + exc.detail
        sys.stderr.write(f"REJECT: {exc.code}{suffix}\n")
        return 2
    except Exception as exc:
        sys.stderr.write(f"REJECT: INTERNAL_ROUTE_ERROR:{type(exc).__name__}\n")
        return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
