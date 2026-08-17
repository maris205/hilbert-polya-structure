#!/usr/bin/env python3
"""Render and semantically validate the strict SD-C42 Route-A v0.2 card."""

from __future__ import annotations

from base64 import b64decode
from hashlib import sha256
import json
from pathlib import Path
import re
import sys
from typing import Any

import yaml


PENDING = "PENDING_FIRST_ARTIFACT_COMMIT"
COMMIT_RE = re.compile(r"[0-9a-f]{40}")
ZERO_COMMIT = "0" * 40
ROOT = Path(__file__).resolve().parents[2]
ROUTE_SCHEMA_FIXTURE_REL = "code/contracts/ROUTE_A_V0_2_SCHEMA.json"
ROUTE_SCHEMA_FIXTURE_SHA256 = "15e47752d6134ec7ddc8f36329a3f7139031122ead7a90af6b876840c1ac5bfa"
ROUTE_SKILL_ARTIFACT_REL = "docs/inputs/route-a-evaluator-v0.2.0.md.b64"
ROUTE_SKILL_SHA256 = "29bd6275aa0c80ecce9cca898f06687208475c0a9a40cf3b9592fde45951458a"
EXPECTED_SCIENCE_SHA256 = "340aff6f08e7cf9360d57d34ff9c66e99f9322343b3069fe37e5acc2f55aa7c5"
EXPECTED_A0_CONTROLS = [
    "shuffled_generated_primes",
    "matched_density_integers",
    "composites",
    "pseudoprimes",
    "randomized_labels",
    "neighboring_digits",
    "simpler_parent",
]
EXPECTED_A1_CONTROLS = [
    "shuffled_periods",
    "random_weights",
    "random_phases",
    "same_density_lengths",
    "neighboring_digits",
    "simpler_parent",
]
EXPECTED_ADVERSARIAL_CONTROLS = [
    *("A0/" + item for item in EXPECTED_A0_CONTROLS),
    *("A1/" + item for item in EXPECTED_A1_CONTROLS),
]
EXPECTED_PROJECTION_ROWS = [
    {
        "projection": "P_t",
        "rational_integer_support": True,
        "rational_prime_selectivity": False,
        "clock": False,
        "repetition": False,
    },
    {
        "projection": "P_Delta",
        "rational_integer_support": True,
        "rational_prime_selectivity": False,
        "clock": False,
        "repetition": False,
    },
    {
        "projection": "P_N",
        "rational_integer_support": False,
        "rational_prime_selectivity": False,
        "clock": True,
        "repetition": True,
    },
]
EXPECTED_TERMINALS = [
    "GO_MODULAR_PRIMITIVE_LEDGER",
    "GO_SAME_OBJECT_MAYER_DETERMINANT",
    "STOP_CANONICAL_INTEGER_PROJECTION",
    "STOP_RATIONAL_INTEGER_CLOCK_REPETITION_CONJUNCTION",
    "STOP_OPERATOR_VISIBLE_SELECTOR_NOT_OWNED",
    "ROUTE_A_REJECTED",
]
STAGE1_NOTE = (
    "Stage 1 authority artifact has three PENDING_FIRST_ARTIFACT_COMMIT fields "
    "and no PAPER_MANIFEST.sha256. Stage 2 is metadata-only: it replaces "
    "source_commit, code_commit, and source_lock.code_commit with one identical "
    "lowercase nonzero 40-hex artifact commit and adds the sorted self-excluding "
    "PAPER_MANIFEST.sha256."
)


def load_schema_fixture() -> dict[str, Any]:
    raw = (ROOT / ROUTE_SCHEMA_FIXTURE_REL).read_bytes()
    if sha256(raw).hexdigest() != ROUTE_SCHEMA_FIXTURE_SHA256:
        raise RuntimeError("Route-A v0.2 schema fixture hash mismatch")
    fixture = json.loads(raw)
    encoded_skill = (ROOT / ROUTE_SKILL_ARTIFACT_REL).read_bytes()
    skill_bytes = b64decode(b"".join(encoded_skill.split()), validate=True)
    if sha256(skill_bytes).hexdigest() != ROUTE_SKILL_SHA256:
        raise RuntimeError("vendored Route-A v0.2 skill byte hash mismatch")
    if fixture.get("skill_sha256") != ROUTE_SKILL_SHA256:
        raise RuntimeError("Route-A v0.2 skill provenance mismatch")
    return fixture


ROUTE_SCHEMA_FIXTURE = load_schema_fixture()


def stage2_note(commit: str) -> str:
    return (
        f"Stage 1 artifact commit {commit} contained the three "
        "PENDING_FIRST_ARTIFACT_COMMIT fields and no PAPER_MANIFEST.sha256. "
        "Stage 2 is metadata-only: it seals source_commit, code_commit, and "
        "source_lock.code_commit to that same lowercase nonzero 40-hex artifact "
        "commit and adds the sorted self-excluding PAPER_MANIFEST.sha256."
    )


def canonical_json(value: Any) -> bytes:
    return (
        json.dumps(value, indent=2, sort_keys=True, ensure_ascii=True) + "\n"
    ).encode("ascii")


def _route_document(science: dict[str, Any], commit: str, sealed: bool) -> dict[str, Any]:
    note = stage2_note(commit) if sealed else STAGE1_NOTE
    return {
        "skill": "route-a-evaluator",
        "skill_version": "0.2.0",
        "candidate_id": "SD-C42",
        "source_commit": commit,
        "code_commit": commit,
        "evaluation_date": "2026-08-17",
        "artifact_path_base": "papers/40-gauss-mayer-projection-firewalls",
        "freeze_note": note,
        "source_lock": {
            "candidate_definition": (
                "Evaluate the frozen typed pair-shift RhoPrimitivePair built from two Gauss "
                "inverse branches per return, with inherited L_s and same-object det(I-L_s^2), "
                "under the exact scalar-projection, clock, repetition, ownership, and source boundaries."
            ),
            "object": (
                "X2=(N^2)^N with one-pair shift rho, primitive pair necklaces, digit marker "
                "exponent two per pair, and grouping bijection iota from X=N^N; pair, digit, "
                "and geodesic primitive types are not interchangeable."
            ),
            "family": "symbolic_dynamics",
            "phase_space": "X2=(N^2)^N",
            "dynamics": "rho_one_pair_shift",
            "parameters": "bounded exact D=2,3,4; pair lengths k=1,2,3,4",
            "parameter_provenance": (
                "Authority research lock 530f8a989d1e0f29e4ca51342d121a4e358d60692e659b18d136b9236e95c55e; "
                "retrospective CONTROL_LOCK f19edfa13b4f4cd9511394563fc2d7f7d9c428e477ae39e1d248a821e86850d8; "
                "Route-A evaluator v0.2.0 SHA 29bd6275aa0c80ecce9cca898f06687208475c0a9a40cf3b9592fde45951458a."
            ),
            "arithmetic_origin": "Exact traces and order discriminants of positive Gauss branch products; no prime or zero table is loaded.",
            "clock": "u^(2k) per primitive pair word of pair length k",
            "normalization": "rho(iota(x))=iota(sigma^2(x))",
            "determinant_convention": "D_42(s,u)=det(I-u^2 L_s^2)^(-1)",
            "regularization_order": "Mayer nuclear order zero on A_infinity(D)",
            "main_theorem_marker": "pair_marker_exponent_2k",
            "orbit_cutoff": "exact primitive pair lengths k<=4",
            "cutoff": "six registered canonical/neighboring runs; 39622 exact rows",
            "precision": "exact integers, rational numbers, and Q(sqrt(Delta)) root data",
            "training_data": "none",
            "allowed_data": [
                "frozen eleven-file authority research package",
                "locally vendored six-card Session-4 packet",
                "exact matrix and word inventories",
                "Mayer source theorem boundaries",
            ],
            "forbidden_data": [
                "prime tables or target zero tables",
                "cross-type primitive credit",
                "post-hoc operator-visible selector",
                "arbitrary-u Selberg semantics",
                "universal projection or selector no-go claim",
            ],
            "code_commit": commit,
            "artifact_paths": [
                "SOURCE_LOCK.md",
                "DERIVATION_PACKAGE.md",
                "PROOF_PACKAGE.md",
                "OBJECT_OWNERSHIP.md",
                "PRIMITIVITY_TYPE_FIREWALL.md",
            ],
        },
        "a0": {
            "verdict": "A0_WEAK_ARITHMETIC_RELATION",
            "evidence_status": "PROVED",
            "strongest_evidence": "Exact trace and order-discriminant arithmetic is recomputed from primitive pair matrices without a target table.",
            "strongest_failure": "All seven literal controls fail to establish a distinguished rational-prime arithmetic source.",
            "arithmetic_controls": EXPECTED_A0_CONTROLS,
            "artifacts": [
                "results/main_evaluation.json",
                "results/independent_evaluation.json",
                "ROUTE_STATUS_AUDIT.md",
            ],
        },
        "a1": {
            "verdict": "A1_PASS_ANALYTIC",
            "evidence_status": "PROVED",
            "strongest_evidence": "Primitive pair necklaces, splitting, orientation, completeness, multipliers, and repetition powers are recomputed exactly.",
            "strongest_failure": "Pair-ledger credit is new to Paper 40 and is not inherited from the digit shift or geodesic primitive type.",
            "metrics": {
                "primitive_type": "RhoPrimitivePair",
                "registered_runs": 6,
                "scientific_rows": 39622,
                "primitive_repetition_separated": True,
                "orientation_phase_multiplicity_recorded": True,
                "stability_multipliers_exact": True,
                "completeness_scope": "BOUNDED_D_2_3_4_K_1_2_3_4",
                "mandatory_controls": EXPECTED_A1_CONTROLS,
            },
            "artifacts": [
                "results/scientific_results.json",
                "results/main_evaluation.json",
                "results/independent_evaluation.json",
                "PRIMITIVITY_TYPE_FIREWALL.md",
            ],
        },
        "a2": {
            "verdict": "A2_ANALYTIC_DETERMINANT",
            "evidence_status": "PROVED",
            "strongest_evidence": "The SD-C04 parent supplies L_s and the same-object analytic identity det(I-L_s^2) on the frozen Mayer domain.",
            "strongest_failure": "This gives no prime Euler ledger, operator-visible selector, arbitrary-u Selberg identity, or target-root fit.",
            "metrics": {
                "zero_error_train": "NA",
                "zero_error_validation": "NA",
                "zero_error_test": "NA",
                "extra_zero_count": "NA",
                "missing_zero_count": "NA",
                "root_count_discrepancy": "NA",
                "cutoff_drift": "NA",
                "precision_drift": "NA",
                "control_margin": "NA",
            },
            "artifacts": [
                "MAYER_SOURCE_BOUNDARY.md",
                "PROOF_PACKAGE.md",
                "results/research_reproduction.json",
            ],
        },
        "a3": {
            "verdict": "A3_PARTIAL_ANALYTIC_STRUCTURE",
            "evidence_status": "PROVED",
            "strongest_evidence": "The Mayer determinant identity is analytic for Re(s)>1/2; the Selberg Euler product starts at Re(s)>1 and continues meromorphically.",
            "strongest_failure": "The Riemann Gamma/pole/trivial-zero ledger, counting law, target divisor, and same-clock Weil compression are absent.",
            "analytic_structure": {
                "conjugation_symmetry": "SOURCE_SUPPORTED_MODULAR_IDENTITY",
                "functional_equation": "MODULAR_SELBERG_ONLY_NOT_RIEMANN_TARGET",
                "gamma_trivial_zero_pole_ledger": "ABSENT_FOR_RIEMANN_TARGET",
                "counting_law": "ABSENT_FOR_RIEMANN_TARGET",
                "continuation": "MAYER_MEROMORPHIC_CONTINUATION_TO_C",
                "truncation_control": "ANALYTIC_THEOREM_NOT_NUMERIC_TRUNCATION",
                "hidden_zero_prefactor": "NONE_CLAIMED",
            },
            "weil_compression": {
                "natural_same_clock_object": "ABSENT",
                "dynamical_prime_power_dual_reading": "ABSENT",
                "trace_second_moment_inertia": "NA",
                "status": "OPEN_NOT_CONSTRUCTED",
            },
            "artifacts": [
                "MAYER_SOURCE_BOUNDARY.md",
                "ROUTE_STATUS_AUDIT.md",
                "LITERATURE_BOUNDARY_ADDENDUM.md",
            ],
        },
        "a4": {
            "verdict": "A4_FORMAL_HINT",
            "evidence_status": "PROVED",
            "strongest_evidence": "Known modular geometry supplies a formal spectral carrier and the exact geodesic norm preserves clock and repetition.",
            "strongest_failure": "No new quantum operator, domain, target multiplicity theorem, or same-clock rational-prime lift is defined.",
            "metrics": {
                "target_zero_data_used": False,
                "fixed_selfadjoint_operator": False,
                "zero_correspondence": False,
                "route_b_readiness": False,
            },
            "artifacts": [
                "OBJECT_OWNERSHIP.md",
                "ROUTE_STATUS_AUDIT.md",
            ],
        },
        "adversarial_controls": {
            "controls_used": EXPECTED_ADVERSARIAL_CONTROLS,
            "proves_too_much_risk": "CONTROLLED_BY_TYPED_FINITE_CONTRACT",
            "verdict": "STOP_SCOPED",
        },
        "typed_return_map": {
            "digit_space": "X=N^N",
            "pair_space": "X2=(N^2)^N",
            "grouping_bijection": "iota",
            "identity": "rho(iota(x))=iota(sigma^2(x))",
            "pair_digit_geodesic_types_separate": True,
            "inherited_a1_pair_credit": False,
        },
        "projection_firewall": {
            "rows": science["projection_rows"],
            "conjunction_exists": science["full_projection_conjunction_exists"],
            "terminal": "STOP_RATIONAL_INTEGER_CLOCK_REPETITION_CONJUNCTION",
            "old_overbroad_terminal_forbidden": True,
        },
        "terminal_codes": science["route"]["terminal_codes"],
        "route_tuple": [
            "A0_WEAK_ARITHMETIC_RELATION",
            "A1_PASS_ANALYTIC",
            "A2_ANALYTIC_DETERMINANT",
            "A3_PARTIAL_ANALYTIC_STRUCTURE",
            "A4_FORMAL_HINT",
        ],
        "overall_verdict": "ROUTE_A_REJECTED",
        "claim_boundary": "Exact bounded typed pair-ledger, Mayer-domain, scalar-projection, and frozen-schema ownership audit only. No universal projection, selector, Gauss-map, or dynamical-zeta impossibility is claimed.",
        "blocking_conditions": [
            "no scalar projection passes rational-integer support plus clock plus repetition",
            "no operator-visible selector is declared in the frozen untwisted schema",
            "target root and coefficient data are forbidden",
            "Route B remains locked",
        ],
        "next_smallest_test": "No post-result repair is authorized. A new selector or twist requires a separately source-locked object before any new evaluation.",
        "round2_clues": [
            "source-lock any new selector or twist as a distinct object before evaluation",
            "preserve pair digit and geodesic primitive type separation",
            "keep Route B locked unless A4_ROUTE_B_READY or explicit project-lead authorization is obtained",
        ],
        "branch_status": "CLOSE_FROZEN_SD_C42_PROJECTION_BRANCH",
        "route_b_invocation_allowed": False,
        "authority_integration": {
            "stage1_root_manifest": "ABSENT",
            "stage2_semantic_scope": "ROUTE_CARD_PLUS_SELF_EXCLUDING_ROOT_MANIFEST_ONLY",
            "scientific_results_sha256": sha256(canonical_json(science)).hexdigest(),
            "route_schema_fixture_sha256": ROUTE_SCHEMA_FIXTURE_SHA256,
            "registered_runs": 6,
            "scientific_rows": 39622,
            "theorem_failures": 0,
            "typed_cross_credit": False,
            "universal_no_go_claimed": False,
        },
        "target_and_root_metrics": {
            "correlation_metrics": "NA",
            "cutoff_drift": "NA",
            "eigenvalue_count": "NA",
            "extra_zero_count": "NA",
            "missing_zero_count": "NA",
            "precision_drift": "NA",
            "root_count_discrepancy": "NA",
            "root_location_error": "NA",
            "spacing_metrics": "NA",
            "spectral_fit": "NA",
            "target_coefficient_fit": "NA",
            "target_prime_data": "NA",
            "target_root_data": "NA",
            "target_zero_data": "NA",
            "unfolding_metrics": "NA",
            "zero_error_test": "NA",
            "zero_error_train": "NA",
            "zero_error_validation": "NA",
        },
        "route_b": {"B": False, "invoked": False, "invocation_allowed": False},
    }


def render_route(science: dict[str, Any], commit: str = PENDING, sealed: bool = False) -> bytes:
    if sealed:
        if not COMMIT_RE.fullmatch(commit) or commit == ZERO_COMMIT:
            raise ValueError("sealed state requires lowercase nonzero 40-hex commit")
    elif commit != PENDING:
        raise ValueError("Stage 1 requires PENDING_FIRST_ARTIFACT_COMMIT")
    document = _route_document(science, commit, sealed)
    return yaml.safe_dump(
        document,
        allow_unicode=False,
        default_flow_style=False,
        sort_keys=False,
        width=100,
    ).encode("ascii")


def parse_route(raw: bytes) -> dict[str, Any]:
    class DuplicateRejectingLoader(yaml.SafeLoader):
        pass

    def construct_mapping(loader: yaml.SafeLoader, node: yaml.MappingNode, deep: bool = False) -> dict[Any, Any]:
        mapping: dict[Any, Any] = {}
        for key_node, value_node in node.value:
            key = loader.construct_object(key_node, deep=deep)
            if key in mapping:
                raise ValueError(f"duplicate YAML key: {key!r}")
            mapping[key] = loader.construct_object(value_node, deep=deep)
        return mapping

    DuplicateRejectingLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        construct_mapping,
    )
    data = yaml.load(raw.decode("utf-8"), Loader=DuplicateRejectingLoader)
    if not isinstance(data, dict):
        raise ValueError("Route card must be a mapping")
    return data


def paired_state(route: dict[str, Any], manifest_present: bool) -> str:
    source_lock = route.get("source_lock") if isinstance(route.get("source_lock"), dict) else {}
    triple = [route.get("source_commit"), route.get("code_commit"), source_lock.get("code_commit")]
    if not manifest_present and triple == [PENDING, PENDING, PENDING] and route.get("freeze_note") == STAGE1_NOTE:
        return "VALID_PAIRED_STATE"
    if manifest_present and len(set(triple)) == 1 and isinstance(triple[0], str) and COMMIT_RE.fullmatch(triple[0]) and triple[0] != ZERO_COMMIT and route.get("freeze_note") == stage2_note(triple[0]):
        return "VALID_PAIRED_STATE"
    return "INVALID_MIXED_OR_UNSAFE_STATE"


def semantic_projection(route: dict[str, Any], manifest_present: bool) -> dict[str, Any]:
    route_b = route.get("route_b") if isinstance(route.get("route_b"), dict) else {}
    firewall = route.get("projection_firewall") if isinstance(route.get("projection_firewall"), dict) else {}
    typed = route.get("typed_return_map") if isinstance(route.get("typed_return_map"), dict) else {}
    metrics = route.get("target_and_root_metrics") if isinstance(route.get("target_and_root_metrics"), dict) else {}
    integration = route.get("authority_integration") if isinstance(route.get("authority_integration"), dict) else {}
    return {
        "schema": "paper40-route-evaluation-v1",
        "candidate_id": route.get("candidate_id"),
        "skill": route.get("skill"),
        "skill_version": route.get("skill_version"),
        "evaluation_date": route.get("evaluation_date"),
        "route_tuple": route.get("route_tuple"),
        "overall_verdict": route.get("overall_verdict"),
        "route_b": route_b,
        "route_b_invocation_allowed": route.get("route_b_invocation_allowed"),
        "terminal_codes": route.get("terminal_codes"),
        "projection_firewall": firewall,
        "typed_return_map": typed,
        "target_and_root_metrics": metrics,
        "paired_artifact_state": paired_state(route, manifest_present),
        "stage2_semantic_scope": integration.get("stage2_semantic_scope"),
        "claim_boundary": route.get("claim_boundary"),
    }


def _same_recursive_shape(value: Any, template: Any) -> bool:
    if type(value) is not type(template):
        return False
    if isinstance(template, dict):
        return set(value) == set(template) and all(
            _same_recursive_shape(value[key], template[key]) for key in template
        )
    if isinstance(template, list):
        return len(value) == len(template) and all(
            _same_recursive_shape(item, expected)
            for item, expected in zip(value, template, strict=True)
        )
    return True


def _expected_document(route: dict[str, Any], manifest_present: bool) -> dict[str, Any] | None:
    if paired_state(route, manifest_present) != "VALID_PAIRED_STATE":
        return None
    commit = route["source_commit"] if manifest_present else PENDING
    science = {
        "projection_rows": EXPECTED_PROJECTION_ROWS,
        "full_projection_conjunction_exists": False,
        "route": {"terminal_codes": EXPECTED_TERMINALS},
    }
    expected = _route_document(science, commit, sealed=manifest_present)
    expected["authority_integration"]["scientific_results_sha256"] = EXPECTED_SCIENCE_SHA256
    return expected


def _contains_legacy(value: Any) -> bool:
    if isinstance(value, dict):
        return any(_contains_legacy(key) or _contains_legacy(item) for key, item in value.items())
    if isinstance(value, list):
        return any(_contains_legacy(item) for item in value)
    return isinstance(value, str) and "STOP_CLOCK_REPETITION_COMPATIBILITY" in value


def live_schema_exact(route: dict[str, Any]) -> bool:
    fixture = ROUTE_SCHEMA_FIXTURE
    if set(route) != set(fixture["exact_top_level_keys"]):
        return False
    if not set(fixture["live_output_required_top_level_keys"]) <= set(route):
        return False
    source_lock = route.get("source_lock")
    if not isinstance(source_lock, dict) or set(source_lock) != set(fixture["exact_source_lock_keys"]):
        return False
    if not set(fixture["live_source_lock_required_keys"]) <= set(source_lock):
        return False
    for layer in ("a0", "a1", "a2", "a3", "a4"):
        value = route.get(layer)
        if not isinstance(value, dict) or set(value) != set(fixture["exact_layer_keys"][layer]):
            return False
        artifacts = value.get("artifacts")
        if not isinstance(artifacts, list) or not artifacts or not all(isinstance(item, str) and item for item in artifacts):
            return False
    controls = route.get("adversarial_controls")
    return (
        isinstance(controls, dict)
        and set(controls) == set(fixture["exact_adversarial_control_keys"])
        and isinstance(route.get("round2_clues"), list)
        and bool(route["round2_clues"])
        and all(isinstance(item, str) and item for item in route["round2_clues"])
    )


def closed_hierarchies(route: dict[str, Any]) -> bool:
    fixture = ROUTE_SCHEMA_FIXTURE
    evidence = fixture["evidence_status_labels"]
    verdicts = fixture["verdict_labels"]
    layers = ("a0", "a1", "a2", "a3", "a4")
    return (
        all(route[layer].get("evidence_status") in evidence for layer in layers)
        and all(route[layer].get("evidence_status") == "PROVED" for layer in layers)
        and all(route[layer].get("verdict") in verdicts[layer.upper()] for layer in layers)
        and route.get("overall_verdict") in fixture["overall_verdict_labels"]
        and route.get("adversarial_controls", {}).get("verdict") in evidence
        and "A3_EXACT_DIVISOR_CANDIDATE" in verdicts["A3"]
        and "A3_EXACT_DIVISOR_MATCH" not in verdicts["A3"]
    )


def validate_semantics(route: dict[str, Any], manifest_present: bool) -> dict[str, bool]:
    projection = semantic_projection(route, manifest_present)
    expected = _expected_document(route, manifest_present)
    shape_template = _route_document(
        {
            "projection_rows": EXPECTED_PROJECTION_ROWS,
            "full_projection_conjunction_exists": False,
            "route": {"terminal_codes": EXPECTED_TERMINALS},
        },
        PENDING,
        sealed=False,
    )
    return {
        "recursive_exact_schema_and_scalar_types": _same_recursive_shape(route, shape_template),
        "exact_route_document_for_paired_state": expected is not None and route == expected,
        "forbidden_legacy_fields_absent": not _contains_legacy(route),
        "strict_identity": (
            projection["skill"] == "route-a-evaluator"
            and projection["skill_version"] == "0.2.0"
            and projection["candidate_id"] == "SD-C42"
            and projection["evaluation_date"] == "2026-08-17"
        ),
        "literal_v0_2_schema": live_schema_exact(route),
        "closed_evidence_and_verdict_hierarchies": closed_hierarchies(route),
        "strict_tuple": projection["route_tuple"] == [
            "A0_WEAK_ARITHMETIC_RELATION",
            "A1_PASS_ANALYTIC",
            "A2_ANALYTIC_DETERMINANT",
            "A3_PARTIAL_ANALYTIC_STRUCTURE",
            "A4_FORMAL_HINT",
        ],
        "rejected_and_b_locked": (
            projection["overall_verdict"] == "ROUTE_A_REJECTED"
            and projection["route_b"] == {"B": False, "invoked": False, "invocation_allowed": False}
            and projection["route_b_invocation_allowed"] is False
        ),
        "mandatory_controls": (
            isinstance(route.get("a0"), dict)
            and isinstance(route.get("a1"), dict)
            and isinstance(route.get("adversarial_controls"), dict)
            and route["a0"].get("arithmetic_controls") == EXPECTED_A0_CONTROLS
            and route["a1"].get("metrics", {}).get("mandatory_controls") == EXPECTED_A1_CONTROLS
            and route["adversarial_controls"].get("controls_used") == EXPECTED_ADVERSARIAL_CONTROLS
            and len(set(EXPECTED_A0_CONTROLS)) == 7
            and len(set(EXPECTED_A1_CONTROLS)) == 6
        ),
        "full_layer_payloads": (
            set(route["a2"].get("metrics", {})) == {
                "zero_error_train", "zero_error_validation", "zero_error_test",
                "extra_zero_count", "missing_zero_count", "root_count_discrepancy",
                "cutoff_drift", "precision_drift", "control_margin",
            }
            and all(value == "NA" for value in route["a2"]["metrics"].values())
            and isinstance(route["a3"].get("analytic_structure"), dict)
            and set(route["a3"]["analytic_structure"]) == {
                "conjugation_symmetry", "functional_equation",
                "gamma_trivial_zero_pole_ledger", "counting_law", "continuation",
                "truncation_control", "hidden_zero_prefactor",
            }
            and isinstance(route["a3"].get("weil_compression"), dict)
            and set(route["a3"]["weil_compression"]) == {
                "natural_same_clock_object", "dynamical_prime_power_dual_reading",
                "trace_second_moment_inertia", "status",
            }
        ),
        "projection_matrix": projection["projection_firewall"] == {
            "rows": EXPECTED_PROJECTION_ROWS,
            "conjunction_exists": False,
            "terminal": "STOP_RATIONAL_INTEGER_CLOCK_REPETITION_CONJUNCTION",
            "old_overbroad_terminal_forbidden": True,
        },
        "narrow_terminals": (
            projection["terminal_codes"] == EXPECTED_TERMINALS
            and "STOP_CLOCK_REPETITION_COMPATIBILITY" not in projection["terminal_codes"]
        ),
        "typed_no_cross_credit": (
            projection["typed_return_map"].get("identity") == "rho(iota(x))=iota(sigma^2(x))"
            and projection["typed_return_map"].get("pair_digit_geodesic_types_separate") is True
            and projection["typed_return_map"].get("inherited_a1_pair_credit") is False
        ),
        "target_root_na": projection["target_and_root_metrics"] == {
            key: "NA"
            for key in [
                "correlation_metrics", "cutoff_drift", "eigenvalue_count",
                "extra_zero_count", "missing_zero_count", "precision_drift",
                "root_count_discrepancy", "root_location_error", "spacing_metrics",
                "spectral_fit", "target_coefficient_fit", "target_prime_data",
                "target_root_data", "target_zero_data", "unfolding_metrics",
                "zero_error_test", "zero_error_train", "zero_error_validation",
            ]
        },
        "paired_state": projection["paired_artifact_state"] == "VALID_PAIRED_STATE",
        "metadata_only_scope": projection["stage2_semantic_scope"] == "ROUTE_CARD_PLUS_SELF_EXCLUDING_ROOT_MANIFEST_ONLY",
        "schema_fixture_provenance": (
            route.get("authority_integration", {}).get("route_schema_fixture_sha256")
            == ROUTE_SCHEMA_FIXTURE_SHA256
        ),
        "claim_scope": "No universal projection" in projection["claim_boundary"],
    }


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: evaluate_route_a.py ROUTE.yaml")
    raw = Path(sys.argv[1]).read_bytes()
    try:
        route = parse_route(raw)
    except (UnicodeDecodeError, ValueError, yaml.YAMLError) as error:
        result = {
            "schema": "paper40-route-evaluation-v1",
            "candidate_id": None,
            "parse_error_class": type(error).__name__,
            "checks": {"strict_yaml_parse_and_unique_keys": False},
            "check_count": 1,
            "failure_count": 1,
            "all_pass": False,
        }
        sys.stdout.buffer.write(canonical_json(result))
        raise SystemExit(1)
    try:
        result = semantic_projection(route, manifest_present=False)
        checks = validate_semantics(route, manifest_present=False)
    except (AttributeError, KeyError, TypeError, ValueError) as error:
        result = {
            "schema": "paper40-route-evaluation-v1",
            "candidate_id": route.get("candidate_id"),
            "semantic_error_class": type(error).__name__,
            "checks": {"strict_recursive_semantics": False},
            "check_count": 1,
            "failure_count": 1,
            "all_pass": False,
        }
        sys.stdout.buffer.write(canonical_json(result))
        raise SystemExit(1)
    result["checks"] = dict(sorted(checks.items()))
    result["check_count"] = len(checks)
    result["failure_count"] = sum(not value for value in checks.values())
    result["all_pass"] = all(checks.values())
    sys.stdout.buffer.write(canonical_json(result))
    if not result["all_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
