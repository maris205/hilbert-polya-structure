#!/usr/bin/env python3
"""Render and validate the strict Paper 41 Route-A v0.2 authority card."""

from __future__ import annotations

from base64 import b64decode
from hashlib import sha256
import json
from pathlib import Path, PurePosixPath
import re
import sys
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[2]
CONTRACT_REL = "code/contracts/INTEGRATION_CONTRACT.json"
SCHEMA_REL = "code/contracts/ROUTE_A_V0_2_SCHEMA.json"
SKILL_REL = "docs/inputs/route-a-evaluator-v0.2.0.md.b64"
CONTRACT_SHA256 = "2f0bbcf5dd2d2ff725edcb961f94d45c11351ed1c89fe30af803f6ee1aa07bbc"
SCHEMA_SHA256 = "ee1c1fa578afd3f266d164465227afe27c95b0b03d83c619260e9bdc19304ea2"
SKILL_SHA256 = "29bd6275aa0c80ecce9cca898f06687208475c0a9a40cf3b9592fde45951458a"
PENDING = "PENDING_FIRST_ARTIFACT_COMMIT"
ZERO_COMMIT = "0" * 40
COMMIT_RE = re.compile(r"[0-9a-f]{40}")
ROUTE_TUPLE = [
    "A0_ANALYTIC_ARITHMETIC_ORIGIN", "A1_FAIL", "A2_FAIL",
    "A3_PARTIAL_ANALYTIC_STRUCTURE", "A4_FAIL",
]
A0_CONTROLS = [
    "inherited_unsigned_observable", "inherited_Liouville_observable",
    "inherited_Moebius_control", "inherited_symbolic_parity_control",
    "exact_composite_and_rotation_witnesses",
]
A1_CONTROLS = [
    "shuffled_periods", "random_weights", "random_phases", "same_density_random_lengths",
    "neighboring_candidate_parameters", "simpler_parent_candidate",
]
TERMINALS = [
    "GO_SOURCE_PARTITION_TRACE_IDENTITY",
    "STOP_DIRECT_LIMIT_RIGHT_ACTION_NON_DESCENT",
    "STOP_INVENTORY_TRACE_PRIMITIVE_DETERMINANT_IDENTIFICATION",
    "STOP_LIOUVILLE_ORBIT_CHARACTER",
    "STOP_ROOTED_CLOCK_CYCLIC_DESCENT",
    "STOP_ROOTED_CLOCK_TEMPORAL_POWERS",
    "ROUTE_A_REJECTED",
]
ARTIFACT_PATHS = [
    "preauthority/SOURCE_LOCK.md",
    "preauthority/OBJECT_MARKER_OPERATOR_CONTRACT.md",
    "preauthority/DERIVATION_PACKAGE.md",
    "preauthority/PROOF_PACKAGE.md",
    "preauthority/THEOREM_FALSIFIERS.md",
    "preauthority/LITERATURE_NOVELTY_AUDIT.md",
    "experiments/PREREGISTRATION.md",
    "experiments/EXPERIMENT_PLAN.md",
    "results/scientific_results.json",
    "results/main_evaluation.json",
    "results/independent_evaluation.json",
]
STAGE1_NOTE = (
    "Stage 1 authority artifact has three PENDING_FIRST_ARTIFACT_COMMIT fields and no "
    "PAPER_MANIFEST.sha256. Stage 2 is metadata-only: it replaces source_commit, code_commit, "
    "and source_lock.code_commit with one identical lowercase nonzero 40-hex artifact commit "
    "and adds the sorted self-excluding PAPER_MANIFEST.sha256."
)
ADVERSARIAL = [
    "cyclic_positive_control_tr_Muv_equals_tr_Mvu",
    "matrix_power_positive_control",
    "exact_recurrence_convention_control_through_length_3",
    "diagonal_trace_class_positive_control",
    "Liouville_cyclic_and_power_negative_controls",
    *["A0/" + item for item in A0_CONTROLS],
    *["A1/" + item for item in A1_CONTROLS],
]


def canonical_json(value: Any) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode("ascii")


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def load_contract() -> dict[str, Any]:
    raw = (ROOT / CONTRACT_REL).read_bytes()
    if digest(raw) != CONTRACT_SHA256:
        raise ValueError("integration contract changed")
    return json.loads(raw)


def load_schema() -> dict[str, Any]:
    raw = (ROOT / SCHEMA_REL).read_bytes()
    if digest(raw) != SCHEMA_SHA256:
        raise ValueError("Route schema changed")
    schema = json.loads(raw)
    encoded = (ROOT / SKILL_REL).read_bytes()
    decoded = b64decode(b"".join(encoded.split()), validate=True)
    if digest(decoded) != SKILL_SHA256 or schema.get("skill_sha256") != SKILL_SHA256:
        raise ValueError("vendored Route skill provenance changed")
    return schema


def stage2_note(commit: str) -> str:
    return (
        f"Stage 1 artifact commit {commit} contained the three PENDING_FIRST_ARTIFACT_COMMIT "
        "fields and no PAPER_MANIFEST.sha256. Stage 2 is metadata-only: it seals source_commit, "
        "code_commit, and source_lock.code_commit to that same lowercase nonzero 40-hex artifact "
        "commit and adds the sorted self-excluding PAPER_MANIFEST.sha256."
    )


def route_document(science: dict[str, Any], commit: str, sealed: bool) -> dict[str, Any]:
    if sealed:
        if COMMIT_RE.fullmatch(commit) is None or commit == ZERO_COMMIT:
            raise ValueError("sealed Route state requires lowercase nonzero 40-hex commit")
        note = stage2_note(commit)
    else:
        if commit != PENDING:
            raise ValueError("Stage 1 Route state requires pending provenance")
        note = STAGE1_NOTE
    if science.get("schema") != "paper41-exact-science-projection-v1":
        raise ValueError("science projection schema changed")
    if science.get("route", {}).get("route_tuple") != ROUTE_TUPLE:
        raise ValueError("science Route tuple changed")
    if science.get("terminal_codes") != TERMINALS:
        raise ValueError("science terminal ledger changed")
    science_hash = digest(canonical_json(science))
    return {
        "skill": "route-a-evaluator",
        "skill_version": "0.2.0",
        "candidate_id": "SD-C43",
        "source_commit": commit,
        "code_commit": commit,
        "evaluation_date": "2026-08-17",
        "artifact_path_base": "papers/41-knauf-rooted-clock-non-descent",
        "freeze_note": note,
        "source_lock": {
            "candidate_definition": (
                "Test whether the exact rooted Knauf h label, trailing-zero direct limit, ordinary "
                "cyclic quotient and word powers, and literal Liouville observable descend to a "
                "canonical scalar primitive/repetition ledger; separately type the diagonal inventory."
            ),
            "object": "Knauf rooted binary words with M_0=L, M_1=R, h(w)=one^T M_w e_1, and the direct limit under w->w0.",
            "family": "symbolic_dynamics",
            "phase_space": "Finite rooted layers and their trailing-zero colimit; necklaces and trace-word models are changed comparison types.",
            "dynamics": "Source binary refinement only; right append-one does not descend to the stable-state quotient.",
            "parameters": "exact words of length at most three plus an exact finite diagonal consistency control",
            "parameter_provenance": "Retrospective closure after all six cards, results, and witnesses were known; no prospective or outcome-independent claim.",
            "arithmetic_origin": "Source-proved stable multiplicities phi(n) give zeta(s-1)/zeta(s) on Re(s)>2 without a prime table.",
            "clock": "log(h(w)) on rooted words only",
            "normalization": "none",
            "determinant_convention": "det(I-uQ_s) belongs to diagonal state inventory and is not promoted to a primitive-return determinant.",
            "roof_function": "log(h(w)) on rooted words only",
            "potential_function": "unsigned_unit_weight",
            "cocycle": "No endogenous scalar cocycle; lambda(h(w)) is external and fails cyclic and power descent.",
            "cutoff": "not_applicable_exact_finite_witness_theorems",
            "precision": "exact integer and rational arithmetic",
            "orbit_cutoff": "not_applicable_no_intrinsic_periodic_orbit_ledger",
            "training_data": "none",
            "allowed_data": [
                "frozen authority research release and independent DA",
                "locally vendored six-card packet and portable source bytes",
                "exact L/R matrix products and generated Liouville values",
                "standard trace-class diagonal Fredholm identities",
            ],
            "forbidden_data": [
                "Riemann zero tables or fitting",
                "external prime-indexed components",
                "changed trace or Gauss/Mayer models credited to SD-C06",
                "prospective or outcome-independent selection claims",
                "universal Knauf/Farey/Gauss no-go claims",
            ],
            "code_commit": commit,
            "artifact_paths": ARTIFACT_PATHS,
        },
        "a0": {
            "verdict": "A0_ANALYTIC_ARITHMETIC_ORIGIN",
            "evidence_status": "PROVED",
            "strongest_evidence": "Source-owned exact stable multiplicities phi(n) yield zeta(s-1)/zeta(s) on Re(s)>2 without a prime table.",
            "strongest_failure": "The arithmetic partition identity supplies no rational-prime primitive orbit ledger or endogenous Liouville cocycle.",
            "arithmetic_controls": A0_CONTROLS,
            "artifacts": ["preauthority/SOURCE_LOCK.md", "preauthority/DERIVATION_PACKAGE.md", "results/source_resolver.json"],
        },
        "a1": {
            "verdict": "A1_FAIL",
            "evidence_status": "PROVED",
            "strongest_evidence": "The recurrence, exact witnesses, and changed-clock positive controls are independently recomputed.",
            "strongest_failure": "Append-one fails on the stable quotient; h is not cyclic or power-compatible; the literal Liouville phase also fails both laws.",
            "metrics": {
                "cyclic_clock_failures": 1,
                "exact_witness_word_length_max": 3,
                "mandatory_controls": A1_CONTROLS,
                "primitive_orbit_count": "NA_NO_INTRINSIC_LEDGER",
                "scalar_sign_cyclic_failures": 1,
                "scalar_sign_power_failures": 1,
                "temporal_power_failures": 1,
            },
            "artifacts": ["preauthority/PROOF_PACKAGE.md", "preauthority/THEOREM_FALSIFIERS.md", "results/scientific_results.json"],
        },
        "a2": {
            "verdict": "A2_FAIL",
            "evidence_status": "PROVED",
            "strongest_evidence": "The diagonal Q_s is trace class on Re(s)>2 and owns an ordinary determinant entire in u.",
            "strongest_failure": "That determinant counts inventory powers, not binary primitive returns; the rooted clock has no required cycles.",
            "metrics": {
                "zero_error_train": "NA_STRUCTURAL_REJECTION",
                "zero_error_validation": "NA_STRUCTURAL_REJECTION",
                "zero_error_test": "NA_STRUCTURAL_REJECTION",
                "extra_zero_count": "NA_STRUCTURAL_REJECTION",
                "missing_zero_count": "NA_STRUCTURAL_REJECTION",
                "root_count_discrepancy": "NA_STRUCTURAL_REJECTION",
                "cutoff_drift": "NA_EXACT_THEOREM",
                "precision_drift": "ZERO_EXACT_ARITHMETIC",
                "control_margin": "NA_STRUCTURAL_REJECTION",
            },
            "artifacts": ["preauthority/OBJECT_MARKER_OPERATOR_CONTRACT.md", "preauthority/DERIVATION_PACKAGE.md", "results/scientific_results.json"],
        },
        "a3": {
            "verdict": "A3_PARTIAL_ANALYTIC_STRUCTURE",
            "evidence_status": "PROVED",
            "strongest_evidence": "The unsigned partition trace has the inherited zeta quotient and displayed meromorphic continuation.",
            "strongest_failure": "No completed-xi divisor, same-object functional equation, target multiplicity ledger, or same-clock Weil compression is derived.",
            "analytic_structure": {
                "completed_factor": False,
                "displayed_zeta_ratio_meromorphic_continuation": "PROVED",
                "functional_equation_for_same_object_determinant": False,
                "signed_critical_half_plane_convergence": "OPEN",
                "unsigned_limit_Re_gt_2": "PROVED_IN_PRIMARY_SOURCE",
            },
            "weil_compression": {
                "evidence_status": "STOP_SCOPED",
                "status": "NO_NATURAL_COMPRESSION_FROM_A_PRIMITIVE_ORBIT_LEDGER",
            },
            "artifacts": ["preauthority/DERIVATION_PACKAGE.md", "preauthority/LITERATURE_NOVELTY_AUDIT.md", "preauthority/SOURCE_LOCK.md"],
        },
        "a4": {
            "verdict": "A4_FAIL",
            "evidence_status": "OPEN",
            "strongest_evidence": "A parameter-dependent diagonal trace-class operator realizes the partition trace on Re(s)>2.",
            "strongest_failure": "It is not a fixed self-adjoint Hilbert-Polya operator and owns no same-clock binary return trace or multiplicity theorem.",
            "metrics": {
                "fixed_self_adjoint_operator_defined": False,
                "hilbert_space_named": True,
                "same_clock_trace_identity": False,
                "target_multiplicity_theorem": False,
            },
            "artifacts": ["preauthority/OBJECT_MARKER_OPERATOR_CONTRACT.md", "preauthority/THEOREM_FALSIFIERS.md", "preauthority/LITERATURE_NOVELTY_AUDIT.md"],
        },
        "adversarial_controls": {
            "controls_used": ADVERSARIAL,
            "proves_too_much_risk": "Controlled by the exact rooted-h claim boundary and changed-object positive controls.",
            "verdict": "STOP_SCOPED",
        },
        "route_tuple": ROUTE_TUPLE,
        "overall_verdict": "ROUTE_A_REJECTED",
        "claim_boundary": "Exact no-go only for frozen rooted h, trailing-zero colimit, ordinary word powers, literal lambda(h), and diagonal inventory comparison; no universal changed-model no-go.",
        "blocking_conditions": [
            "no canonical primitive/repetition ledger for the frozen rooted clock",
            "no endogenous scalar Liouville orbit character",
            "no same-object dynamical Fredholm determinant",
            "no fixed self-adjoint operator realization",
        ],
        "next_smallest_test": "No post-result in-place repair is authorized; any enlarged state, trace clock, or cocycle requires a new source lock and Route evaluation.",
        "round2_clues": [
            "A full-matrix or trace-model extension is a changed object.",
            "Any new selector or cocycle must be source locked before evaluation.",
        ],
        "route_b_invocation_allowed": False,
        "route_b": {"B": False, "invocation_allowed": False, "invoked": False},
        "terminal_codes": TERMINALS,
        "authority_integration": {
            "chronology": "RETROSPECTIVE_CORRECTIVE_RESEAL_AFTER_FAILED_OUTPUTS_AND_AUDIT_FINDINGS",
            "package_manifest_sha256": "55214e6af4457ba22ea41d406524d6e94f7fe99c7274c08644822fe7505d41bb",
            "route_schema_sha256": SCHEMA_SHA256,
            "scientific_results_sha256": science_hash,
            "source_resolver_matches": 22,
            "stage1_root_manifest": "ABSENT",
            "theorem_failures": 0,
            "universal_no_go_claimed": False,
        },
        "target_and_root_metrics": {
            "correlation_metrics": "NA",
            "eigenvalue_count": "NA",
            "root_location_error": "NA",
            "spacing_metrics": "NA",
            "target_coefficient_fit": "NA",
            "target_data_used": False,
            "target_prime_data": "NA",
            "target_root_data": "NA",
            "target_zero_data": "NA",
            "unfolding_metrics": "NA",
        },
    }


def render_route(science: dict[str, Any], commit: str = PENDING, sealed: bool = False) -> bytes:
    document = route_document(science, commit, sealed)
    return yaml.safe_dump(document, allow_unicode=False, default_flow_style=False,
                          sort_keys=False, width=100).encode("ascii")


class DuplicateRejectingLoader(yaml.SafeLoader):
    pass


def _construct_mapping(loader: yaml.SafeLoader, node: yaml.MappingNode, deep: bool = False) -> dict[Any, Any]:
    mapping: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise ValueError(f"DUPLICATE_YAML_KEY:{key!r}")
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


DuplicateRejectingLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_mapping)


def parse_route(raw: bytes) -> dict[str, Any]:
    value = yaml.load(raw.decode("ascii"), Loader=DuplicateRejectingLoader)
    if not isinstance(value, dict):
        raise ValueError("Route card must be a mapping")
    return value


def safe_relative(path: str) -> bool:
    if not isinstance(path, str) or not path or path.startswith("/") or "\\" in path:
        return False
    parts = PurePosixPath(path).parts
    return all(part not in ("", ".", "..") for part in parts) and PurePosixPath(path).as_posix() == path


def paired_state(route: dict[str, Any], manifest_present: bool) -> str:
    source = route.get("source_lock") if isinstance(route.get("source_lock"), dict) else {}
    triple = [route.get("source_commit"), route.get("code_commit"), source.get("code_commit")]
    if not manifest_present and triple == [PENDING, PENDING, PENDING] and route.get("freeze_note") == STAGE1_NOTE:
        return "VALID_STAGE1"
    if manifest_present and len(set(triple)) == 1 and isinstance(triple[0], str):
        commit = triple[0]
        if COMMIT_RE.fullmatch(commit) and commit != ZERO_COMMIT and route.get("freeze_note") == stage2_note(commit):
            return "VALID_STAGE2"
    return "INVALID_MIXED_OR_UNSAFE_STATE"


def enforce_paired_state(route: dict[str, Any], manifest_present: bool) -> str:
    source = route.get("source_lock") if isinstance(route.get("source_lock"), dict) else {}
    triple = [route.get("source_commit"), route.get("code_commit"), source.get("code_commit")]
    if not manifest_present:
        if triple != [PENDING, PENDING, PENDING]:
            raise ValueError("PAIRED_STATE_MISMATCH")
        if route.get("freeze_note") != STAGE1_NOTE:
            raise ValueError("STALE_FREEZE_NOTE")
        return "VALID_STAGE1"
    if not all(isinstance(item, str) and COMMIT_RE.fullmatch(item) and item != ZERO_COMMIT for item in triple):
        raise ValueError("INVALID_COMMIT_FORMAT")
    if len(set(triple)) != 1:
        raise ValueError("PAIRED_STATE_MISMATCH")
    if route.get("freeze_note") != stage2_note(triple[0]):
        raise ValueError("STALE_FREEZE_NOTE")
    return "VALID_STAGE2"


def validate_route(route: dict[str, Any], manifest_present: bool, root: Path = ROOT) -> dict[str, Any]:
    schema = load_schema()
    contract = load_contract()
    checks: dict[str, bool] = {}

    def check(name: str, value: bool) -> None:
        checks[name] = bool(value)

    check("top_exact_keys", set(route) == set(schema["exact_top_level_keys"]))
    check("live_top_keys", set(schema["live_output_required_top_level_keys"]).issubset(route))
    check("identity", route.get("skill") == "route-a-evaluator" and route.get("skill_version") == "0.2.0"
          and route.get("candidate_id") == "SD-C43" and route.get("evaluation_date") == "2026-08-17")
    check("artifact_base", route.get("artifact_path_base") == contract["artifact_path_base"])
    source = route.get("source_lock") if isinstance(route.get("source_lock"), dict) else {}
    check("source_exact_keys", set(source) == set(schema["exact_source_lock_keys"]))
    check("live_source_keys", set(schema["live_source_lock_required_keys"]).issubset(source))
    artifact_lists: list[list[str]] = []
    if isinstance(source.get("artifact_paths"), list):
        artifact_lists.append(source["artifact_paths"])
    for layer in ("a0", "a1", "a2", "a3", "a4"):
        block = route.get(layer) if isinstance(route.get(layer), dict) else {}
        check(f"{layer}_exact_keys", set(block) == set(schema["exact_layer_keys"][layer]))
        label_key = layer.upper()
        check(f"{layer}_verdict_label", block.get("verdict") in schema["verdict_labels"][label_key])
        check(f"{layer}_evidence_label", block.get("evidence_status") in schema["evidence_status_labels"])
        expected_status = {"a0": "PROVED", "a1": "PROVED", "a2": "PROVED", "a3": "PROVED", "a4": "OPEN"}[layer]
        check(f"{layer}_evidence_exact", block.get("evidence_status") == expected_status)
        if isinstance(block.get("artifacts"), list):
            artifact_lists.append(block["artifacts"])
    all_artifacts = [item for group in artifact_lists for item in group]
    check("artifact_lists_nonempty", len(artifact_lists) == 6 and all(group for group in artifact_lists))
    check("artifact_lists_distinct", all(len(group) == len(set(group)) for group in artifact_lists))
    artifacts_safe = all(safe_relative(item) for item in all_artifacts)
    check("artifact_paths_safe", artifacts_safe)
    check("artifact_paths_exist", artifacts_safe and all(
        (root / item).is_file() and not (root / item).is_symlink() for item in all_artifacts
    ))
    check("source_artifact_exact_set", source.get("artifact_paths") == ARTIFACT_PATHS)

    if not checks["artifact_paths_safe"]:
        raise ValueError("UNSAFE_ARTIFACT_PATH")
    if not checks["artifact_paths_exist"]:
        raise ValueError("MISSING_ARTIFACT")

    science_path = root / "results/scientific_results.json"
    if not science_path.is_file():
        raise ValueError("MISSING_SCIENCE_PROJECTION")
    science = json.loads(science_path.read_text(encoding="ascii"))
    normalized = json.loads(json.dumps(route))
    if "source_commit" in normalized:
        normalized["source_commit"] = PENDING
    if "code_commit" in normalized:
        normalized["code_commit"] = PENDING
    if isinstance(normalized.get("source_lock"), dict) and "code_commit" in normalized["source_lock"]:
        normalized["source_lock"]["code_commit"] = PENDING
    if "freeze_note" in normalized:
        normalized["freeze_note"] = STAGE1_NOTE
    if normalized != route_document(science, PENDING, False):
        raise ValueError("ROUTE_CANONICAL_PAYLOAD_MISMATCH")

    state = enforce_paired_state(route, manifest_present)
    check("paired_state", True)
    check("manifest_pair", True)

    layer_tuple = [route.get(layer, {}).get("verdict") if isinstance(route.get(layer), dict) else None
                   for layer in ("a0", "a1", "a2", "a3", "a4")]
    check("route_tuple", route.get("route_tuple") == ROUTE_TUPLE and layer_tuple == ROUTE_TUPLE)
    check("overall", route.get("overall_verdict") == "ROUTE_A_REJECTED"
          and route.get("overall_verdict") in schema["overall_verdict_labels"])
    route_b = route.get("route_b") if isinstance(route.get("route_b"), dict) else {}
    check("route_b_lock", route.get("route_b_invocation_allowed") is False
          and route_b == {"B": False, "invocation_allowed": False, "invoked": False})
    check("terminal_exact_set", route.get("terminal_codes") == TERMINALS)
    check("a0_controls", route.get("a0", {}).get("arithmetic_controls") == A0_CONTROLS)
    check("a1_controls", route.get("a1", {}).get("metrics", {}).get("mandatory_controls") == A1_CONTROLS)
    check("adversarial_exact_keys", set(route.get("adversarial_controls", {})) == set(schema["exact_adversarial_control_keys"]))
    check("adversarial_controls", route.get("adversarial_controls", {}).get("controls_used") == ADVERSARIAL)
    check("a2_metric_exact_set", set(route.get("a2", {}).get("metrics", {})) == set(schema["required_a2_metric_keys"]))
    target = route.get("target_and_root_metrics") if isinstance(route.get("target_and_root_metrics"), dict) else {}
    check("target_data_forbidden", target.get("target_data_used") is False
          and target.get("target_prime_data") == "NA" and target.get("target_root_data") == "NA"
          and target.get("target_zero_data") == "NA")
    integration = route.get("authority_integration") if isinstance(route.get("authority_integration"), dict) else {}
    check("science_hash_format", re.fullmatch(r"[0-9a-f]{64}", str(integration.get("scientific_results_sha256"))) is not None)
    check("science_hash_matches", science_path.is_file() and digest(science_path.read_bytes()) == integration.get("scientific_results_sha256"))
    check("integration_counts", integration.get("source_resolver_matches") == 22 and integration.get("theorem_failures") == 0)
    check("chronology", integration.get("chronology") ==
          "RETROSPECTIVE_CORRECTIVE_RESEAL_AFTER_FAILED_OUTPUTS_AND_AUDIT_FINDINGS")
    check("scope", integration.get("universal_no_go_claimed") is False and "no universal changed-model no-go" in str(route.get("claim_boundary")))
    check("blocking_nonempty", isinstance(route.get("blocking_conditions"), list) and len(route["blocking_conditions"]) == 4)
    check("round2_nonempty", isinstance(route.get("round2_clues"), list) and len(route["round2_clues"]) == 2)
    check("source_data_lists", isinstance(source.get("allowed_data"), list) and len(source["allowed_data"]) == 4
          and isinstance(source.get("forbidden_data"), list) and len(source["forbidden_data"]) == 5)

    failed = sorted(name for name, passed in checks.items() if not passed)
    if failed:
        raise ValueError("Route validation failed: " + ", ".join(failed))
    return {
        "check_count": len(checks),
        "checks": dict(sorted(checks.items())),
        "overall_verdict": route["overall_verdict"],
        "paired_state": paired_state(route, manifest_present),
        "route_b_invocation_allowed": False,
        "route_tuple": ROUTE_TUPLE,
        "schema": "paper41-route-evaluation-v1",
        "terminal_codes": TERMINALS,
    }


def main(argv: list[str]) -> int:
    try:
        if len(argv) == 3 and argv[1] == "render":
            science = json.loads(Path(argv[2]).read_text(encoding="ascii"))
            sys.stdout.buffer.write(render_route(science))
            return 0
        if len(argv) == 4 and argv[1] == "validate" and argv[3] in ("absent", "present"):
            raw = Path(argv[2]).read_bytes()
            route = parse_route(raw)
            manifest_present = argv[3] == "present"
            result = validate_route(route, manifest_present)
            science = json.loads((ROOT / "results/scientific_results.json").read_text(encoding="ascii"))
            commit = route["source_commit"] if manifest_present else PENDING
            if raw != render_route(science, commit, manifest_present):
                raise ValueError("RAW_ROUTE_RENDERER_BYTES_MISMATCH")
            sys.stdout.buffer.write(canonical_json(result))
            return 0
        print("usage: evaluate_route_a.py render SCIENCE.json | validate ROUTE.yaml absent|present", file=sys.stderr)
        return 2
    except Exception as error:
        print(f"REJECT: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
