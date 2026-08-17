#!/usr/bin/env python3
"""Render the strict Paper 43 Route-A v0.2 card as canonical JSON-subset YAML."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
CONTRACT = ROOT / "code/contracts/INTEGRATION_CONTRACT.json"
SCHEMA = ROOT / "code/contracts/ROUTE_A_V0_2_SCHEMA.json"


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       separators=(",", ": ")) + "\n").encode("ascii")


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    output: dict[str, Any] = {}
    for key, value in pairs:
        if key in output:
            raise ValueError(f"duplicate key: {key}")
        output[key] = value
    return output


def read_json(path: Path) -> tuple[Any, bytes]:
    raw = path.read_bytes()
    value = json.loads(raw.decode("ascii"), object_pairs_hook=unique)
    if canonical(value) != raw:
        raise ValueError(f"noncanonical JSON: {path.name}")
    return value, raw


def provenance(contract: dict[str, Any], arguments: list[str]) -> dict[str, Any]:
    if not arguments:
        state = contract["provenance_states"]["state_a"]
        return {
            "code_commit": state["code_commit"],
            "freeze_note": state["freeze_note"],
            "manifest_present": False,
            "source_commit": state["source_commit"],
            "source_lock_code_commit": state["source_lock_code_commit"],
            "state": "A",
        }
    if len(arguments) != 2 or arguments[0] != "--state-b" \
            or re.fullmatch(r"[0-9a-f]{40}", arguments[1]) is None \
            or arguments[1] == "0" * 40:
        raise ValueError("illegal Route provenance arguments")
    commit = arguments[1]
    template = contract["provenance_states"]["state_b"]["freeze_note_template"]
    return {
        "code_commit": commit,
        "freeze_note": template.format(commit=commit),
        "manifest_present": True,
        "source_commit": commit,
        "source_lock_code_commit": commit,
        "state": "B",
    }


def build_route(science: dict[str, Any], science_raw: bytes,
                contract: dict[str, Any], state: dict[str, Any]) -> dict[str, Any]:
    if science.get("schema") != "paper43-squarefree-factor-science-projection-v1":
        raise ValueError("science schema mismatch")
    route_science = science["route"]
    if route_science["tuple"] != contract["route_contract"]["tuple"] \
            or route_science["overall_verdict"] != contract["route_contract"]["overall_verdict"]:
        raise ValueError("science Route facts disagree with integration contract")
    terminals = science["terminal_codes"]
    if terminals != contract["route_contract"]["terminal_codes"]:
        raise ValueError("science terminal mapping differs")
    science_hash = digest(science_raw)
    route = {
        "a0": {
            "arithmetic_controls": [
                "identity_factor_same_source_control",
                "one_point_factor_control",
                "arbitrary_finite_prime_set_changed_source_control",
                "external_periodic_extension_direction_control",
                "rational_prime_primitive_type_control",
            ],
            "artifacts": [
                "preauthority/SOURCE_LOCK.md",
                "preauthority/SELECTION_AND_PROVENANCE.md",
                "preauthority/PROOF_PACKAGE.md",
                "results/source_resolver.json",
            ],
            "evidence_status": "MODELING_CHOICE",
            "strongest_evidence": "The source is a classical exact arithmetic subshift with an all-prime-square admissibility grammar and no fitted numerical target.",
            "strongest_failure": "Every rational-prime-square exclusion is inserted directly into the grammar; the factor theorem preserves this source choice and supplies no endogenous rational-prime primitive emergence.",
            "verdict": route_science["tuple"][0],
        },
        "a1": {
            "artifacts": [
                "preauthority/PROOF_PACKAGE.md",
                "preauthority/EXACT_WITNESS_LEDGER.md",
                "results/factor_periodic_rigidity_certificate.json",
                "results/periodic_ledger_certificate.json",
            ],
            "evidence_status": "PROVED",
            "metrics": {
                "factor_class": science["claim_scope"]["factor_class"],
                "finite_to_one_required": False,
                "fixed_points_every_period": 1,
                "primitive_orbits": "one_period_one_factor_orbit",
                "rational_prime_primitive_support": False,
                "repetition_failures": 0,
                "target_expansive_required": False,
            },
            "strongest_evidence": "CRT proves source proximality, factor permanence transports it through every lawful factor, and finite-orbit separation leaves exactly one primitive fixed orbit.",
            "strongest_failure": "A singleton primitive ledger cannot be the infinite rational-prime ledger; z^r records repetition of the same orbit.",
            "verdict": route_science["tuple"][1],
        },
        "a2": {
            "artifacts": [
                "preauthority/OBJECT_MARKER_OPERATOR_CONTRACT.md",
                "preauthority/DERIVATION_PACKAGE.md",
                "results/operator_ownership_certificate.json",
                "results/scientific_results.json",
            ],
            "evidence_status": "PROVED",
            "metrics": {
                "control_margin": "every_finite_prime_set_has_an_exact_nonzero_periodic_witness",
                "cutoff_drift": "not_applicable_exact_theorem",
                "extra_zero_count": "not_applicable",
                "missing_zero_count": "not_applicable",
                "precision_drift": "zero_exact_arithmetic",
                "root_count_discrepancy": "not_applicable",
                "scientific_results_sha256": science_hash,
                "zero_error_test": "not_applicable",
                "zero_error_train": "not_applicable",
                "zero_error_validation": "not_applicable",
            },
            "strongest_evidence": "Every lawful factor has zeta_AM_Y(z)=1/(1-z), inverse determinant 1-z, and the rank-one periodic-core matrix [1] has the same ordinary determinant and traces.",
            "strongest_failure": "The determinant records one fixed orbit and has no nontrivial arithmetic divisor; [1] is not a full-state transfer operator.",
            "verdict": route_science["tuple"][2],
        },
        "a3": {
            "analytic_structure": {
                "completed_factor": False,
                "determinant": "one_minus_z",
                "divisor_growth": "constant",
                "gamma_factor": False,
                "rational_continuation": True,
                "rational_prime_support": False,
            },
            "artifacts": [
                "preauthority/DERIVATION_PACKAGE.md",
                "preauthority/LITERATURE_NOVELTY_AUDIT.md",
                "results/periodic_ledger_certificate.json",
            ],
            "evidence_status": "PROVED",
            "strongest_evidence": "The inverse determinant 1-z is an exact entire polynomial and its zeta is a rational function with known divisor.",
            "strongest_failure": "The divisor is trivial: there is no rational-prime Euler support, completed functional equation, gamma factor, T log T growth, explicit formula, or natural same-ledger Weil compression.",
            "verdict": route_science["tuple"][3],
            "weil_compression": {
                "evidence_status": "STOP_SCOPED",
                "status": "not_naturally_available_from_singleton_periodic_ledger",
            },
        },
        "a4": {
            "artifacts": [
                "preauthority/OBJECT_MARKER_OPERATOR_CONTRACT.md",
                "preauthority/THEOREM_FALSIFIERS.md",
                "results/operator_ownership_certificate.json",
            ],
            "evidence_status": "NOT_TESTABLE",
            "metrics": {
                "completed_target_divisor": False,
                "fixed_self_adjoint_hilbert_polya_operator_defined": False,
                "full_state_operator_named": False,
                "periodic_core_space_named": True,
                "route_b_readiness": False,
                "same_clock_rational_prime_trace_identity": False,
            },
            "strongest_evidence": "The periodic-core Hilbert space C and matrix [1] reproduce the fixed-point traces exactly.",
            "strongest_failure": "No full-state transfer family, fixed self-adjoint Hilbert-Polya operator, same-clock rational-prime trace identity, or completed target divisor is defined.",
            "verdict": route_science["tuple"][4],
        },
        "adversarial_controls": {
            "controls_used": [
                "identity_factor", "one_point_factor",
                "arbitrary_finite_prime_set_periodic_approximant",
                "external_periodic_product_extension", "nonfactor_map_scope_deletion",
                "changed_aperiodic_zeta_observable", "rational_prime_support_cardinality",
            ],
            "proves_too_much_risk": "The unrestricted statement for all aperiodic systems is false; this proof uses the frozen source's proximality and retains the finite-exclusion and extension controls.",
            "verdict": "STOP_SCOPED_EXACT_SQUAREFREE_FACTOR_PERIODIC_RIGIDITY",
        },
        "artifact_path_base": contract["artifact_path_base"],
        "authority_integration": {
            "git_operations_by_integrator": 0,
            "paper_manifest_present": state["manifest_present"],
            "state": state["state"],
            "status": "STATE_A_FIRST_ARTIFACT_PENDING_TRIPLE" if state["state"] == "A"
                      else "STATE_B_METADATA_ONLY_SEAL",
        },
        "blocking_conditions": [
            "rational_prime_squares_are_explicit_grammar_inputs",
            "every_lawful_factor_has_only_one_trivial_primitive_orbit",
            "inverse_determinant_is_one_minus_z_with_trivial_divisor",
            "no_completed_same_ledger_operator_lift",
            "external_novelty_is_at_most_minimal",
        ],
        "branch_status": route_science["branch_status"],
        "candidate_id": "SD-C45",
        "claim_boundary": "Exact periodic-ledger rigidity only for continuous surjective equivariant compact metrizable Z-factors of the frozen all-prime-square admissible shift, with unit marker and Artin-Mazur counts; no universal aperiodic-factor, changed-source, extension, completed-divisor, or full spectral-operator claim.",
        "code_commit": state["code_commit"],
        "evaluation_date": "2026-08-17",
        "freeze_note": state["freeze_note"],
        "next_smallest_test": "Retain the external source-only duplicate-publication boundary; no Route-B computation is authorized.",
        "overall_verdict": route_science["overall_verdict"],
        "projection_firewall": {
            "declared_repairs_are_exhaustive": False,
            "decisive_witnesses": {
                "factor_proximality": "uniform_continuity_on_compact_source",
                "periodic_rigidity": "finite_orbit_positive_separation",
                "primitive_support": "one_factor_primitive_versus_infinitely_many_primes",
                "source_proximality": "pair_window_prime_square_CRT",
            },
            "factor_type": "TopologicalFactorState",
            "primitive_type": "PeriodicOrbit_Y_S",
            "required_fields": [
                "continuous", "surjective", "Z_equivariant", "compact_metrizable_target",
                "unit_time_marker", "temporal_repetition", "Artin_Mazur_ownership",
            ],
            "source_type": "SquarefreeAdmissiblePoint",
            "target_comparator_type": "RationalPrimeAtom",
        },
        "round2_clues": [],
        "route_b": route_science["route_b"],
        "route_b_invocation_allowed": route_science["route_b_invocation_allowed"],
        "route_tuple": route_science["tuple"],
        "skill": "route-a-evaluator",
        "skill_version": "0.2.0",
        "source_commit": state["source_commit"],
        "source_lock": {
            "allowed_data": [
                "frozen_C02_C03_C05_cards_and_C02_source_proof",
                "rational_primes_prime_squares_missing_residues_and_exact_CRT",
                "compact_topological_dynamics_and_uniform_continuity",
                "exact_periodic_orbit_and_Artin_Mazur_definitions",
                "primary_literature_and_sealed_predecessor_collision_audits",
            ],
            "arithmetic_origin": "direct_rational_prime_square_exclusions",
            "artifact_paths": [
                "preauthority/SOURCE_LOCK.md", "preauthority/OBJECT_MARKER_OPERATOR_CONTRACT.md",
                "preauthority/DERIVATION_PACKAGE.md", "preauthority/PROOF_PACKAGE.md",
                "preauthority/THEOREM_FALSIFIERS.md", "preauthority/EXACT_WITNESS_LEDGER.md",
                "preauthority/LITERATURE_NOVELTY_AUDIT.md",
                "preauthority/SELECTION_AND_PROVENANCE.md",
                "preauthority/ROUTE_RECORD_CENSUS.md", "preauthority/DA_HANDOFF.md",
                "results/scientific_results.json",
            ],
            "candidate_definition": "Retain exact SD-C02 two-sided squarefree admissible shift, unit clock, periodic-orbit type, Artin-Mazur marker, and determinant convention; test lawful topological factors for new cycles.",
            "clock": "unit_discrete_time",
            "cocycle": "trivial",
            "code_commit": state["source_lock_code_commit"],
            "cutoff": "not_applicable_exact_topological_proof",
            "determinant_convention": "zeta_AM_Y(z)=exp(sum_m_ge_1 Fix(S^m)z^m/m)_and_D_AM_Y=zeta_inverse",
            "dynamics": "two_sided_left_shift",
            "family": "symbolic_dynamics",
            "forbidden_data": [
                "Riemann_zero_fitting_or_target_parameters",
                "finite_prime_square_approximation_as_infinite_source",
                "noncontinuous_nononto_or_nonequivariant_maps_called_factors",
                "extensions_products_or_induced_systems_called_repairs",
                "traversals_retyped_as_rational_prime_primitives",
                "rank_one_periodic_core_called_full_transfer_or_Hilbert_Polya_operator",
                "predecessor_ranking_authorization_novelty_or_priority_transfer",
            ],
            "function_space": "source_locally_constant_cylinder_algebra_and_separate_one_dimensional_periodic_core",
            "main_theorem_marker": "z_counts_one_original_unit_time_step",
            "normalization": "z_marks_factor_time_and_external_prime_comparator_uses_independent_u",
            "object": "X_sf_is_binary_two_sided_sequences_omitting_a_residue_mod_p_squared_for_every_rational_prime_p",
            "orbit_cutoff": "not_applicable_exact_all_period_theorem",
            "parameter_provenance": "frozen_Session_4_C02_grammar_no_fitted_prime_or_zero_data",
            "parameters": "all_rational_prime_square_exclusions_exact",
            "phase_space": "X_sf_subset_0_1_power_Z",
            "potential_function": "zero",
            "precision": "exact_integer_modular_arithmetic_and_symbolic_algebra",
            "regularization_order": "not_applicable_ordinary_Artin_Mazur_and_rank_one_determinant",
            "roof_function": "one",
            "training_data": "none",
        },
        "target_and_root_metrics": {
            "exact_period_quantifier": "all_m_ge_one",
            "exact_window_quantifier": "all_L_ge_zero",
            "factor_fiber_bound": "unrestricted",
            "numerical_root_search_used": False,
            "target_zero_data_used": False,
        },
        "terminal_codes": terminals,
        "typed_return_map": {
            "factor_marker": "z_power_time",
            "factor_primitive": "sole_fixed_orbit_pi_zero",
            "factor_repetition": "temporal_traversal",
            "rational_prime_marker": "independent_u",
            "rational_prime_same_type_identification_exists": False,
            "source_marker": "z_power_time",
            "source_primitive": "sole_fixed_orbit_after_source_theorem",
            "source_repetition": "temporal_traversal",
        },
    }
    if "STOP_DUPLICATE" in canonical(route).decode("ascii"):
        raise ValueError("external STOP_DUPLICATE leaked into strict Route")
    return route


def main(argv: list[str]) -> int:
    if not sys.flags.isolated or not sys.dont_write_bytecode:
        raise RuntimeError("evaluate_route_a.py requires python3 -I -B")
    if not argv:
        raise SystemExit("usage: evaluate_route_a.py SCIENCE.json [--state-b COMMIT]")
    science, science_raw = read_json(Path(argv[0]))
    contract, _ = read_json(CONTRACT)
    schema, _ = read_json(SCHEMA)
    state = provenance(contract, argv[1:])
    route = build_route(science, science_raw, contract, state)
    if set(route) != set(schema["required_top_level_keys"]):
        raise ValueError("Route top-level schema mismatch")
    for name, keys in schema["required_nested_keys"].items():
        if set(route[name]) != set(keys):
            raise ValueError(f"Route nested schema mismatch: {name}")
    sys.stdout.buffer.write(canonical(route))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
