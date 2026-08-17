#!/usr/bin/env python3
"""Emit only raw, hash-bound inputs for the SD-C42 authority evaluators."""

from __future__ import annotations

from base64 import b64decode
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
from typing import Any, Iterable


EXPERIMENT_PREREG_SHA256 = "f1643899ea7ac62e916b24fc265a4ee2ce1d042e2e078d7b336662ab2a065908"
EXPERIMENT_PLAN_SHA256 = "dbae7e5317bea10e623f957ee75389392de7cfd8d55b17965ce710ff78364b2d"
RESEARCH_LOCK_SHA256 = "530f8a989d1e0f29e4ca51342d121a4e358d60692e659b18d136b9236e95c55e"
RESEARCH_POINTER_SHA256 = "e985b438395225f454fc60e6e913e1e2b6f1fd6781c24bb3f703778e415fb4e5"
CONTROL_LOCK_SHA256 = "f19edfa13b4f4cd9511394563fc2d7f7d9c428e477ae39e1d248a821e86850d8"
ROUTE_SCHEMA_FIXTURE_SHA256 = "15e47752d6134ec7ddc8f36329a3f7139031122ead7a90af6b876840c1ac5bfa"
ROUTE_SKILL_SHA256 = "29bd6275aa0c80ecce9cca898f06687208475c0a9a40cf3b9592fde45951458a"
ROUTE_SKILL_REL = "docs/inputs/route-a-evaluator-v0.2.0.md.b64"

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

CARD_HASHES = {
    "SD-C01": "ee47a9c90c6bfbc54ba6b09b21f416dcece58b0d0ba9a391ca196d1b41d365a2",
    "SD-C02": "5b5e9a2fe33a0ba8d281cf59c8f5346b95033c655d258554c0f76f8cfa0a434f",
    "SD-C03": "2263b1c7bac4336628f444ded88e4e2ad98117f430113faf1ea5a91c16380328",
    "SD-C04": "0609076081ccd69e9ffa3e0f708d426a33f7d41e2884f90bb2792bbc90209a92",
    "SD-C05": "4a18295b1e20245c7196f21be4e4afc52857bf981efb461556720ab9e8ab5ed1",
    "SD-C06": "d93683662a0cbee8e07d79329477d8b60bb273fb72e4bd64c05847e09a576c1b",
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

KNOWN_REPRODUCTION_HASHES = {
    "control_reference": "d0be9630e4f0710c1f602e14e517939f6eef21c582934d79f795a9871f45a30f",
    "control_independent": "729287849f36046b8aa21d8dba615650f4289dd1d3202c1783cc41af207c4d92",
    "prototype_reference": "2fee7701a08ec4f7e019863c6e86bf6fb884bf0323e5593e4bf946ef35e7a995",
    "prototype_independent": "78a1846b19cffde3c21642e6220b893a82690adaee5314ff6be2b19e7265fe38",
}


def project_root() -> Path:
    return Path(__file__).resolve().parents[2]


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def canonical_bytes(value: Any) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode("ascii")


def rotations(word: tuple[Any, ...]) -> Iterable[tuple[Any, ...]]:
    for index in range(len(word)):
        yield word[index:] + word[:index]


def is_primitive(word: tuple[Any, ...]) -> bool:
    for period in range(1, len(word)):
        if len(word) % period == 0 and word == word[:period] * (len(word) // period):
            return False
    return True


def raw_primitive_inventory(digits: tuple[int, ...], length: int) -> list[list[list[int]]]:
    alphabet = tuple(product(digits, repeat=2))
    words: list[list[list[int]]] = []
    for candidate in product(alphabet, repeat=length):
        word = tuple(candidate)
        if is_primitive(word) and word == min(rotations(word)):
            words.append([[left, right] for left, right in word])
    return words


def lcg_sequence(seed: int, count: int) -> list[int]:
    state = seed % (2**31)
    output = []
    for _ in range(count):
        state = (1103515245 * state + 12345) % (2**31)
        output.append(state)
    return output


def _research(root: Path) -> dict[str, Any]:
    return {
        "manifest_path": "RESEARCH_LOCK.sha256",
        "manifest_sha256": digest(root / "RESEARCH_LOCK.sha256"),
        "pointer_path": "RESEARCH_LOCK.json",
        "pointer_sha256": digest(root / "RESEARCH_LOCK.json"),
        "immutable_file_hashes": {name: digest(root / name) for name in sorted(RESEARCH_FILES)},
        "expected_manifest_sha256": RESEARCH_LOCK_SHA256,
        "expected_pointer_sha256": RESEARCH_POINTER_SHA256,
        "expected_immutable_file_hashes": dict(sorted(RESEARCH_FILES.items())),
        "dependent_seal_hashes": {
            "claim_boundary": "168c29620445002fdf0bdf9c49bd7792414fe5ef378c80615b115646db9214cb",
            "literature_audit": "79982d110318ca29a9f579d8498a4b110da742450f6e0011f2164067ac20a3e8",
            "literature_manifest": "28e2f95750b5ba4e76cf2e174eba9d9bc318e8b57c4c26345c9c6f14cc4d65ce",
            "outer_manifest": "5a258c18495056ce6ed9ec0bed4778ea1c5a548f7d8cf8592145a817aa904ee2",
            "independent_da": "f9e5f8c7b8cdc07aeeea18d48927fd7e07ac1da82dbef3c3daa10b102a9e2a7e",
        },
    }


def _route_cards(vendor: Path) -> list[dict[str, Any]]:
    output = []
    for card_id, expected_hash in sorted(CARD_HASHES.items()):
        relative = f"inputs/route_cards/{card_id}.yaml"
        raw = (vendor / relative).read_bytes()
        output.append({
            "card_id": card_id,
            "relative_path": relative,
            "historical_byte_sha256": expected_hash,
            "vendored_byte_sha256": sha256(raw).hexdigest(),
            "raw_yaml_utf8": raw.decode("utf-8"),
        })
    return output


def _route_schema(root: Path) -> dict[str, Any]:
    relative = "code/contracts/ROUTE_A_V0_2_SCHEMA.json"
    raw = (root / relative).read_bytes()
    skill_encoded = (root / ROUTE_SKILL_REL).read_bytes()
    skill_raw = b64decode(b"".join(skill_encoded.split()), validate=True)
    return {
        "schema_fixture_path": relative,
        "schema_fixture_sha256": sha256(raw).hexdigest(),
        "expected_schema_fixture_sha256": ROUTE_SCHEMA_FIXTURE_SHA256,
        "schema_fixture": json.loads(raw),
        "skill_artifact_path": ROUTE_SKILL_REL,
        "skill_artifact_encoding": "base64-rfc4648",
        "skill_byte_sha256": sha256(skill_raw).hexdigest(),
        "expected_skill_byte_sha256": ROUTE_SKILL_SHA256,
        "skill_utf8": skill_raw.decode("utf-8"),
        "skill": "route-a-evaluator",
        "skill_version": "0.2.0",
        "candidate_id": "SD-C42",
        "evaluation_date": "2026-08-17",
        "criterion_order": ["A0", "A1", "A2", "A3", "A4"],
        "required_a0_control_count": 7,
        "required_a1_control_count": 6,
        "paired_provenance_fields": ["source_commit", "code_commit", "source_lock.code_commit"],
        "target_root_metric_keys": [
            "correlation_metrics", "cutoff_drift", "eigenvalue_count", "extra_zero_count",
            "missing_zero_count", "precision_drift", "root_count_discrepancy", "root_location_error",
            "spacing_metrics", "spectral_fit", "target_coefficient_fit", "target_prime_data",
            "target_root_data", "target_zero_data", "unfolding_metrics", "zero_error_test",
            "zero_error_train", "zero_error_validation",
        ],
    }


def _primitive_inventories() -> list[dict[str, Any]]:
    records = []
    for family, start in (("canonical", 1), ("neighboring", 2)):
        for alphabet_size in (2, 3, 4):
            digits = tuple(range(start, start + alphabet_size))
            for length in (1, 2, 3, 4):
                records.append({
                    "run_id": f"{family}_D{alphabet_size}_k{length}",
                    "family": family,
                    "alphabet_size": alphabet_size,
                    "digits": list(digits),
                    "pair_length": length,
                    "raw_words": raw_primitive_inventory(digits, length),
                })
    return records


def build_source_packet(root: Path | None = None) -> dict[str, Any]:
    root = root or project_root()
    vendor = root / "docs/inputs/prototype_v3"
    return {
        "schema": "paper40-authority-raw-source-packet-v2",
        "candidate_id": "SD-C42",
        "chronology_input": {
            "classification": "RETROSPECTIVE_CHECKER_FROZEN_AUTHORITY_INTEGRATION",
            "v1_and_inflight_smoke_outputs_known": True,
            "canonical_prototype_outputs_known": True,
            "control_lock_precedes_clean_replacement_rerun": True,
            "research_renderings_postdate_canonical_run": True,
            "authority_checker_inputs_precede_authority_run": True,
            "prospective_credit_allowed": False,
        },
        "experiment_freeze_input": {
            "preregistration_path": "experiments/PREREGISTRATION.md",
            "preregistration_sha256": digest(root / "experiments/PREREGISTRATION.md"),
            "expected_preregistration_sha256": EXPERIMENT_PREREG_SHA256,
            "plan_path": "experiments/EXPERIMENT_PLAN.md",
            "plan_sha256": digest(root / "experiments/EXPERIMENT_PLAN.md"),
            "expected_plan_sha256": EXPERIMENT_PLAN_SHA256,
        },
        "research_input": _research(root),
        "prototype_reproduction_input": {
            "vendor_root": "docs/inputs/prototype_v3",
            "control_lock_path": "docs/inputs/prototype_v3/CONTROL_LOCK.md",
            "control_lock_sha256": digest(vendor / "CONTROL_LOCK.md"),
            "expected_control_lock_sha256": CONTROL_LOCK_SHA256,
            "known_output_hash_targets": dict(sorted(KNOWN_REPRODUCTION_HASHES.items())),
        },
        "route_card_bytes": _route_cards(vendor),
        "selection_rule_schema": {
            "card_ids": sorted(CARD_HASHES),
            "nonempty_intrinsic_ledger_rule": "candidate_specific_a1_source_anchor",
            "same_object_determinant_rule": "a2.evidence_status=PROVED_and_a2.verdict=A2_ANALYTIC_DETERMINANT",
            "tie_break_order": ["A3", "A4"],
            "forbidden_predicates": ["nontrivial", "preset_winner", "rank_from_candidate_id"],
        },
        "raw_control_input": {
            "generator": {
                "name": "LCG31",
                "modulus": 2**31,
                "multiplier": 1103515245,
                "increment": 12345,
                "sequence_length_per_seed": 256,
            },
            "seeds": dict(sorted(SEEDS.items())),
            "lcg_sequences": {name: lcg_sequence(seed, 256) for name, seed in sorted(SEEDS.items())},
            "a0_family_ids": [
                "shuffled_generated_primes",
                "matched_density_integers",
                "composites",
                "pseudoprimes",
                "randomized_labels",
                "neighboring_digits",
                "simpler_parent",
            ],
            "a1_family_ids": [
                "shuffled_periods",
                "random_weights",
                "random_phases",
                "same_density_lengths",
                "neighboring_digits",
                "simpler_parent",
            ],
            "control_digits": [1, 2],
            "neighboring_control_digits": [2, 3],
            "control_pair_lengths": [1, 2, 3],
            "prototype_alphabet_sizes": [2, 3, 4],
            "prototype_pair_lengths": [1, 2, 3, 4],
        },
        "raw_primitive_inventories": _primitive_inventories(),
        "raw_type_input": {
            "type_symbols": [
                "SigmaPrimitiveDigit",
                "RhoPrimitivePair",
                "PrimitiveClosedGeodesic",
            ],
            "digit_space_symbol": "X=N^N",
            "digit_shift_symbol": "sigma",
            "pair_space_symbol": "X2=(N^2)^N",
            "pair_shift_symbol": "rho",
            "grouping_symbol": "iota",
            "grouping_block_size": 2,
            "return_map_digit_fixture": [1, 2, 3, 4, 5, 6, 7, 8],
            "reversal_pair_fixture": [[1, 2], [2, 3], [1, 4]],
            "parent_supplied_symbols": ["one_digit_gauss_branches", "L_s", "det(I-L_s^2)"],
            "paper40_new_symbol": "RhoPrimitivePair",
        },
        "raw_branch_input": {
            "matrix_templates": {
                "A": [["a", 1], [1, 0]],
                "B": [[0, 1], [1, "a"]],
                "J": [[0, 1], [1, 0]],
            },
            "stored_digits": [1, 2, 2, 3, 1, 4],
            "evaluation_point": [1, 4],
            "weight_exponent_s": 1,
            "raw_operator_nesting": "last_raw_branch_on_left",
        },
        "raw_collision_input": [
            {"witness_id": "W1", "left_word": [[1, 2]], "right_word": [[2, 1]]},
            {"witness_id": "W2", "left_word": [[1, 4]], "right_word": [[2, 2]]},
            {"witness_id": "W3", "left_word": [[2, 4]], "right_word": [[1, 1], [1, 2]]},
        ],
        "projection_definition_input": [
            {"projection_id": "P_t", "definition": "matrix_trace"},
            {"projection_id": "P_Delta", "definition": "matrix_trace_squared_minus_four"},
            {"projection_id": "P_N", "definition": "square_of_expanding_eigenvalue"},
        ],
        "projection_criterion_schema": {
            "criterion_ids": ["rational_integer_support", "clock", "repetition"],
            "norm_minimal_polynomial_template": "x^2-(t^2-2)x+1",
            "norm_root_selector": "larger_positive_root",
            "derivative_root_selector": "smaller_positive_root",
            "clock_marker_exponent_rule": "2*pair_length",
            "repetition_exponents": [2, 3, 4, 5, 6],
        },
        "mayer_source_input": {
            "function_space_symbol": "A_infinity(D)",
            "disk_center_radius": [[1, 0], [3, 2]],
            "determinant_half_plane": "Re(s)>1/2",
            "euler_product_initial_half_plane": "Re(s)>1",
            "continuation_domain": "C",
            "local_u_domain": "formal_or_small_abs_u",
            "selberg_identity_u_value": 1,
            "source_log_coefficient_tokens": ["u^(2*k*r)", "d_w^(r*s)", "r", "1-d_w^r"],
            "target_log_coefficient_tokens": ["u^(2*k*r)", "p^(-r*s)", "r"],
        },
        "ownership_input": {
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
            "scalar_postselection": {
                "full_inventory": [3, 4],
                "declared_projector": None,
            },
        },
        "row_contract_input": {
            "orientation_equivalence": "rotation_only",
            "reverse_quotient_rule": "metadata_only_no_reversal_quotient",
            "reversal_metadata_fields": [
                "orientation_id",
                "reverse_orientation_id",
                "reversal_orbit_id",
                "self_reversal",
                "reverse_class_present",
            ],
            "source_multiplicity": 1,
            "untwisted_sign": 1,
            "phase_modulus": 97,
            "phase_exponent": 0,
            "stability_denominator_token": "1-d_w^r",
        },
        "route_schema_input": _route_schema(root),
        "claim_scope_input": {
            "scope_label": "FROZEN_FINITE_TYPED_PROJECTION_CONTRACT_ONLY",
            "forbidden_claim_tokens": [
                "universal projection impossibility",
                "universal selector nonexistence",
                "minimal collision witness",
                "prospective novelty credit",
                "cross-type primitive credit",
            ],
        },
    }


def packet_bytes(root: Path | None = None) -> bytes:
    return canonical_bytes(build_source_packet(root))
