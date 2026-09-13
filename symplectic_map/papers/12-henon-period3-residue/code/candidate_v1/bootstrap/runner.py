"""Science-free bootstrap for the sole registered R100 transaction."""

from __future__ import annotations

import hashlib
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

from .constants import (
    ADJUDICATED_PATH,
    CANDIDATE_ID,
    CLAIM_PATH,
    NONCLAIMS,
    PREFLIGHT_PATH,
    PROOF_SHA256,
    REGISTERED_INDICES,
    SOURCE_LOCK_SHA256,
    SOURCE_REVIEW_SHA256,
    TERMINAL_FAILURE,
    TERMINAL_SUCCESS,
)
from .contracts import collect_contract_witnesses
from .controls import run_negative_controls
from .lifecycle import (
    build_claim_object,
    claim_registered_audit,
    commit_result,
    prepare_runtime_tree,
    terminalize,
)
from .manifest import static_code_audit, validate_code_manifest
from .preflight import collect_preflight
from .protocol import (
    exact_same,
    load_exact_json,
    regular_file,
    sha256_file,
    validate_canonical_json_file,
)
from .review import validate_deployment_review


def _fresh_preclaim_gates(project_root: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    stored_preflight = validate_canonical_json_file(project_root / PREFLIGHT_PATH)
    fresh_preflight = collect_preflight(project_root)
    if not exact_same(stored_preflight, fresh_preflight):
        raise RuntimeError("stored preflight is not the fresh canonical preclaim record")
    if fresh_preflight["status"] != "PREEXECUTION_PASS_REGISTERED_COUNT_ZERO":
        raise RuntimeError("preflight does not pass")
    manifest_validation = validate_code_manifest(project_root)
    if manifest_validation["status"] != "VALID":
        raise RuntimeError("deployment manifest does not validate")
    review_validation = validate_deployment_review(project_root)
    if review_validation["status"] != "VALID":
        raise RuntimeError("independent deployment authority does not validate")
    return manifest_validation, review_validation


def _launch_capability_process(script: Path, token: bytes, working_directory: Path) -> None:
    read_descriptor, write_descriptor = os.pipe()
    if read_descriptor != 3:
        os.dup2(read_descriptor, 3, inheritable=True)
        os.close(read_descriptor)
    else:
        os.set_inheritable(3, True)
    try:
        offset = 0
        while offset < len(token):
            written = os.write(write_descriptor, token[offset:])
            if written < 1:
                raise OSError("short capability write")
            offset += written
    finally:
        os.close(write_descriptor)
    try:
        completed = subprocess.run(
            [sys.executable, "-I", "-S", "-B", os.fspath(script)],
            cwd=working_directory,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            timeout=1800,
            pass_fds=(3,),
        )
    finally:
        os.close(3)
    if completed.returncode != 0:
        raise RuntimeError("capability process failed with code " + str(completed.returncode))
    if completed.stdout or completed.stderr:
        raise RuntimeError("capability process emitted an unexpected terminal stream")


def _track_capability_token(
    track: str,
    claim_sha256: str,
    manifest: dict[str, Any],
) -> bytes:
    if track not in {"Q", "R"}:
        raise ValueError("track token identity")
    track_name = "track_q" if track == "Q" else "track_r"
    fields = [
        "HENON_PERIOD3_TRACK_" + track + "_START_V1",
        claim_sha256,
        manifest["code_files"]["candidate_v1/" + track_name + "/runner.py"],
        manifest["code_files"]["candidate_v1/" + track_name + "/engine.py"],
        manifest["definitions_sha256"],
    ]
    if any(type(value) is not str or ":" in value or "\n" in value for value in fields):
        raise RuntimeError("track token field")
    return (":".join(fields) + "\n").encode("ascii")


def _adjudicator_capability_token(
    claim_sha256: str,
    manifest: dict[str, Any],
    q_envelope_sha256: str,
    r_envelope_sha256: str,
) -> bytes:
    fields = [
        "HENON_PERIOD3_ADJUDICATE_V1",
        claim_sha256,
        manifest["code_files"]["candidate_v1/adjudicator/adjudicate.py"],
        manifest["code_files"]["candidate_v1/shared/result_envelope.schema.json"],
        manifest["code_files"]["candidate_v1/adjudicator/acceptance_ledger.json"],
        q_envelope_sha256,
        r_envelope_sha256,
    ]
    if any(type(value) is not str or ":" in value or "\n" in value for value in fields):
        raise RuntimeError("adjudicator token field")
    return (":".join(fields) + "\n").encode("ascii")


def _exact_stage_inventory(directory: Path, expected: set[str]) -> None:
    if not directory.is_dir() or directory.is_symlink():
        raise RuntimeError("unsafe staging directory")
    observed = {path.name for path in directory.iterdir() if path.is_file() and not path.is_symlink()}
    if observed != expected or len(list(directory.iterdir())) != len(expected):
        raise RuntimeError("staging inventory is not exact")


def _count_record_map(value: Any, label: str) -> dict[str, int]:
    if type(value) is not list or not value:
        raise RuntimeError(label + " is empty or not a list")
    result: dict[str, int] = {}
    for record in value:
        if type(record) is not dict or set(record) != {"count", "path"}:
            raise RuntimeError(label + " record keys")
        path = record["path"]
        count = record["count"]
        if type(path) is not str or not path or path in result:
            raise RuntimeError(label + " path")
        if type(count) is not int or count < 1:
            raise RuntimeError(label + " count")
        result[path] = count
    if list(result) != sorted(result):
        raise RuntimeError(label + " canonical order")
    return result


def _validate_exact_diagnostics(
    public: Any,
    private: Any,
    track: str,
) -> None:
    if type(public) is not list or len(public) != 2:
        raise RuntimeError("public diagnostic list")
    if type(private) is not list or len(private) != 2:
        raise RuntimeError("private diagnostic list")
    if [record.get("index") if type(record) is dict else None for record in public] != [8, 9]:
        raise RuntimeError("public diagnostic order")
    if [record.get("index") if type(record) is dict else None for record in private] != [8, 9]:
        raise RuntimeError("private diagnostic order")
    for public_record, private_record in zip(public, private):
        if (type(public_record) is not dict
                or set(public_record) != {"final_integer", "index"}
                or type(public_record["index"]) is not int
                or type(public_record["final_integer"]) is not int):
            raise RuntimeError("public diagnostic exact schema")
        if type(private_record) is not dict:
            raise RuntimeError("private diagnostic record")
        if (type(private_record.get("index")) is not int
                or type(private_record.get("final_integer")) is not int
                or private_record["index"] != public_record["index"]
                or private_record["final_integer"] != public_record["final_integer"]):
            raise RuntimeError("private/public diagnostic boundary")
        index = private_record["index"]
        if track == "Q":
            q_keys = {
                "empty_range_zero_component_count",
                "final_integer",
                "index",
                "j_zero_exceptional_nonzero_count",
                "j_zero_exceptional_pattern_count",
                "j_zero_incoming_pattern_totals",
                "j_zero_regular_pattern_count",
                "private_component_records",
                "reduction_state_cache_size",
                "route_agreement",
                "route_contract",
            }
            if set(private_record) != q_keys or private_record["route_agreement"] is not True:
                raise RuntimeError("Q private diagnostic keys")
            for key in (
                "empty_range_zero_component_count",
                "j_zero_exceptional_nonzero_count",
                "j_zero_exceptional_pattern_count",
                "j_zero_regular_pattern_count",
                "reduction_state_cache_size",
            ):
                if type(private_record[key]) is not int or private_record[key] < 0:
                    raise RuntimeError("Q private diagnostic scalar")
            if (private_record["empty_range_zero_component_count"] < 1
                    or private_record["j_zero_regular_pattern_count"] != 3
                    or private_record["j_zero_exceptional_pattern_count"] != 3
                    or private_record["j_zero_exceptional_nonzero_count"] != 0
                    or private_record["reduction_state_cache_size"] < 1):
                raise RuntimeError("Q private diagnostic invariant")
            components = private_record["private_component_records"]
            if type(components) is not list or len(components) != index + 2:
                raise RuntimeError("Q component ledger length")
            for expected_component, component in enumerate(components):
                if (type(component) is not dict
                        or set(component) != {
                            "component_index", "decorated_tuple_value", "recurrence_value"
                        }
                        or component["component_index"] != expected_component
                        or type(component["component_index"]) is not int
                        or type(component["decorated_tuple_value"]) is not int
                        or type(component["recurrence_value"]) is not int
                        or component["decorated_tuple_value"] != component["recurrence_value"]):
                    raise RuntimeError("Q component route ledger")
            patterns = private_record["j_zero_incoming_pattern_totals"]
            if type(patterns) is not list or len(patterns) != 6:
                raise RuntimeError("Q j-zero pattern ledger")
            for pattern in patterns:
                if (type(pattern) is not dict
                        or set(pattern) != {"contribution", "incoming"}
                        or type(pattern["incoming"]) is not list
                        or len(pattern["incoming"]) != 3
                        or any(type(value) is not int for value in pattern["incoming"])
                        or type(pattern["contribution"]) is not int):
                    raise RuntimeError("Q j-zero pattern record")
            if (type(private_record["route_contract"]) is not dict
                    or set(private_record["route_contract"]) != {
                        "base_case_outcomes",
                        "decorated_tuple_parameter_count",
                        "independent_private_route_count",
                        "normal_form_choice_rule",
                        "signed_branch_coefficients",
                        "termination_total_degree_decreases",
                    }):
                raise RuntimeError("Q route contract")
            q_contract = private_record["route_contract"]
            if (q_contract["base_case_outcomes"] != [1, 0]
                    or q_contract["signed_branch_coefficients"] != [2, -1, -1, 1]
                    or q_contract["normal_form_choice_rule"] != "first_reducible_coordinate"
                    or type(q_contract["independent_private_route_count"]) is not int
                    or q_contract["independent_private_route_count"] != 2
                    or type(q_contract["decorated_tuple_parameter_count"]) is not int
                    or q_contract["decorated_tuple_parameter_count"] != 18
                    or type(q_contract["termination_total_degree_decreases"]) is not list
                    or len(q_contract["termination_total_degree_decreases"]) != 4
                    or any(
                        type(value) is not int
                        for value in q_contract["termination_total_degree_decreases"]
                    )):
                raise RuntimeError("Q route contract values")
        else:
            r_keys = {
                "E_value",
                "empty_range_probe_r",
                "empty_range_probe_value",
                "expanded_factored_agreement",
                "final_integer",
                "generalized_binomial_boundary",
                "guarded_records",
                "index",
                "route_contract",
            }
            if set(private_record) != r_keys or private_record["expanded_factored_agreement"] is not True:
                raise RuntimeError("R private diagnostic keys")
            for key in ("E_value", "empty_range_probe_r", "empty_range_probe_value"):
                if type(private_record[key]) is not int:
                    raise RuntimeError("R private diagnostic scalar")
            if private_record["empty_range_probe_value"] != 0:
                raise RuntimeError("R empty-range diagnostic")
            guarded = private_record["guarded_records"]
            if type(guarded) is not list or len(guarded) != index // 2 + 1:
                raise RuntimeError("R guarded diagnostic length")
            for expected_j, record in enumerate(guarded):
                if (type(record) is not dict
                        or set(record) != {"A_value", "expanded_term", "factored_term", "summation_index"}
                        or record["summation_index"] != expected_j
                        or any(type(record[key]) is not int for key in record)):
                    raise RuntimeError("R guarded diagnostic record")
            if (sum(record["expanded_term"] for record in guarded)
                    != private_record["final_integer"]
                    or sum(record["factored_term"] for record in guarded)
                    != private_record["E_value"]):
                raise RuntimeError("R guarded diagnostic sums")
            boundary = private_record["generalized_binomial_boundary"]
            if (type(boundary) is not dict
                    or set(boundary) != {
                        "negative_lower",
                        "negative_upper_at_one",
                        "negative_upper_at_zero",
                        "ordinary_out_of_range",
                    }
                    or any(type(value) is not int for value in boundary.values())):
                raise RuntimeError("R generalized-binomial boundary")
            if boundary != {
                "negative_lower": 0,
                "negative_upper_at_one": -3,
                "negative_upper_at_zero": 1,
                "ordinary_out_of_range": 0,
            }:
                raise RuntimeError("R generalized-binomial boundary values")
            if (type(private_record["route_contract"]) is not dict
                    or set(private_record["route_contract"]) != {
                        "expanded_factored_private_route_count",
                        "guarded_outer_lower",
                        "guarded_outer_upper",
                        "inner_lower",
                        "j_zero_term_present",
                    }):
                raise RuntimeError("R route contract")
            r_contract = private_record["route_contract"]
            if (type(r_contract["expanded_factored_private_route_count"]) is not int
                    or r_contract["expanded_factored_private_route_count"] != 2
                    or type(r_contract["guarded_outer_lower"]) is not int
                    or r_contract["guarded_outer_lower"] != 0
                    or type(r_contract["guarded_outer_upper"]) is not int
                    or r_contract["guarded_outer_upper"] != index // 2
                    or type(r_contract["inner_lower"]) is not int
                    or r_contract["j_zero_term_present"] is not True):
                raise RuntimeError("R route contract values")


def _validate_private_quartic(value: Any, track: str) -> None:
    if type(value) is not dict:
        raise RuntimeError("private quartic object")
    if track == "Q":
        expected_keys = {
            "fiber_parameter_reconstruction",
            "general_quartic_trace_elimination",
            "local_fixed_series",
            "low_period_and_fixed_moment",
            "monic_relations",
            "normalized_affine_comparison",
            "route",
            "standard_basis_bounds",
            "standard_basis_count",
            "subresultant_controls",
            "trace_polynomial",
        }
        if set(value) != expected_keys or value["route"] != "STANDARD_MONOMIAL_MULTIPLICATION_TRACE":
            raise RuntimeError("Q private quartic keys")
        if (value["standard_basis_bounds"] != [4, 4, 4]
                or any(type(item) is not int for item in value["standard_basis_bounds"])
                or type(value["standard_basis_count"]) is not int
                or value["standard_basis_count"] != 64
                or type(value["monic_relations"]) is not list
                or len(value["monic_relations"]) != 1
                or any(type(item) is not str or not item for item in value["monic_relations"])):
            raise RuntimeError("Q standard-monomial certificate")
        trace = value["trace_polynomial"]
        if (type(trace) is not list or len(trace) != 2
                or [term.get("exponent") if type(term) is dict else None for term in trace] != [0, 3]
                or any(
                    type(term) is not dict
                    or set(term) != {"coefficient", "exponent"}
                    or type(term["coefficient"]) is not int
                    or type(term["exponent"]) is not int
                    for term in trace
                )):
            raise RuntimeError("Q quartic trace polynomial")
        elimination = value["general_quartic_trace_elimination"]
        if (type(elimination) is not dict
                or set(elimination) != {
                    "classification_condition",
                    "derivative_square_remainder",
                    "first_eliminated_variable",
                    "first_pivot_coefficient",
                    "general_centered_coefficients",
                    "remaining_relation_terms",
                }
                or elimination.get("classification_condition")
                != "p_divides_derivative_squared"
                or elimination.get("first_eliminated_variable") != "c"
                or type(elimination.get("first_pivot_coefficient")) is not int
                or elimination.get("general_centered_coefficients") != ["d", "c", "b", "0", "1"]
                or type(elimination.get("derivative_square_remainder")) is not list
                or len(elimination["derivative_square_remainder"]) != 4
                or type(elimination.get("remaining_relation_terms")) is not list
                or len(elimination["remaining_relation_terms"]) != 2):
            raise RuntimeError("Q general quartic elimination")
        for polynomial in elimination["derivative_square_remainder"]:
            if type(polynomial) is not list or not polynomial:
                raise RuntimeError("Q derivative-square polynomial")
            for term in polynomial:
                if (type(term) is not dict
                        or set(term) != {
                            "b_exponent", "c_exponent", "coefficient", "d_exponent"
                        }
                        or any(type(term[key]) is not int for key in term)):
                    raise RuntimeError("Q derivative-square term")
        for term in elimination["remaining_relation_terms"]:
            if (type(term) is not dict
                    or set(term) != {"b_exponent", "coefficient", "d_exponent"}
                    or any(type(term[key]) is not int for key in term)):
                raise RuntimeError("Q eliminated relation term")
        fiber = value["fiber_parameter_reconstruction"]
        if (type(fiber) is not dict
                or set(fiber) != {
                    "centered_b_terms",
                    "centered_c_terms",
                    "centered_constraint_coefficient",
                    "centered_d_terms",
                    "centered_solution_s",
                    "eliminated_relation_remainder",
                    "parameter_change",
                    "quadratic_square_coefficients",
                }
                or type(fiber["centered_constraint_coefficient"]) is not int
                or type(fiber["centered_solution_s"]) is not int
                or fiber["centered_c_terms"] != []
                or fiber["eliminated_relation_remainder"] != []
                or type(fiber["parameter_change"]) is not str
                or not fiber["parameter_change"]
                or type(fiber["quadratic_square_coefficients"]) is not list
                or len(fiber["quadratic_square_coefficients"]) != 5):
            raise RuntimeError("Q fiber reconstruction")
        for term_list in (fiber["centered_b_terms"], fiber["centered_d_terms"]):
            if type(term_list) is not list or not term_list:
                raise RuntimeError("Q centered coefficient terms")
            for term in term_list:
                if (type(term) is not dict
                        or set(term) != {"coefficient", "t_exponent"}
                        or any(type(term[key]) is not int for key in term)):
                    raise RuntimeError("Q centered coefficient term")
        for polynomial in fiber["quadratic_square_coefficients"]:
            if type(polynomial) is not list or not polynomial:
                raise RuntimeError("Q quadratic-square coefficient")
            for term in polynomial:
                if (type(term) is not dict
                        or set(term) != {"coefficient", "s_exponent", "t_exponent"}
                        or any(type(term[key]) is not int for key in term)):
                    raise RuntimeError("Q quadratic-square term")
        controls = value["subresultant_controls"]
        if (type(controls) is not dict
                or set(controls) != {
                    "simple_root_fixture_resultant", "square_family_specialization_resultant"
                }
                or any(type(item) is not int for item in controls.values())
                or controls["simple_root_fixture_resultant"] == 0
                or controls["square_family_specialization_resultant"] != 0):
            raise RuntimeError("Q subresultant controls")
        conjugacy = value["normalized_affine_comparison"]
        if (type(conjugacy) is not dict
                or set(conjugacy) != {
                    "centered_translation_coefficient",
                    "explicit_sufficiency_exponent",
                    "minimal_invariant_power",
                    "monic_scale_order",
                    "parameter_scale_weight",
                    "translation_solution",
                }
                or any(type(item) is not int for item in conjugacy.values())
                or conjugacy["translation_solution"] != 0
                or conjugacy["minimal_invariant_power"] != 3):
            raise RuntimeError("Q normalized affine comparison")
        low_period = value["low_period_and_fixed_moment"]
        if (type(low_period) is not dict
                or set(low_period) != {
                    "fixed_basis_count",
                    "fixed_characteristic_terms",
                    "fixed_trace_square_remainder",
                    "multiplication_matrix",
                    "multiplication_matrix_square_nonzero_entry_count",
                    "period_two_ambient_basis_count",
                    "period_two_exact_basis_count",
                    "period_two_nilpotent_correction_square_nonzero_term_count",
                }
                or low_period.get("fixed_basis_count") != 4
                or type(low_period.get("fixed_basis_count")) is not int
                or low_period.get("fixed_trace_square_remainder") != []
                or type(low_period["multiplication_matrix_square_nonzero_entry_count"]) is not int
                or low_period["multiplication_matrix_square_nonzero_entry_count"] != 0
                or type(low_period["period_two_ambient_basis_count"]) is not int
                or type(low_period["period_two_exact_basis_count"]) is not int
                or low_period["period_two_ambient_basis_count"] != 16
                or low_period["period_two_exact_basis_count"] != 12
                or type(low_period["period_two_nilpotent_correction_square_nonzero_term_count"])
                is not int
                or low_period["period_two_nilpotent_correction_square_nonzero_term_count"] != 0):
            raise RuntimeError("Q Step10 fixed-moment witness")
        matrix = low_period["multiplication_matrix"]
        if (type(matrix) is not list or len(matrix) != 4
                or any(type(row) is not list or len(row) != 4 for row in matrix)):
            raise RuntimeError("Q fixed multiplication matrix")
        for row in matrix:
            for entry in row:
                if type(entry) is not list:
                    raise RuntimeError("Q fixed matrix entry")
                for term in entry:
                    if (type(term) is not dict
                            or set(term) != {"L_exponent", "coefficient"}
                            or any(type(term[key]) is not int for key in term)):
                        raise RuntimeError("Q fixed matrix term")
        characteristic = low_period["fixed_characteristic_terms"]
        if type(characteristic) is not list or not characteristic:
            raise RuntimeError("Q fixed characteristic")
        for term in characteristic:
            if (type(term) is not dict
                    or set(term) != {"L_exponent", "T_exponent", "coefficient"}
                    or any(type(term[key]) is not int for key in term)):
                raise RuntimeError("Q fixed characteristic term")
        local = value["local_fixed_series"]
    else:
        expected_keys = {
            "constant_term_ledger",
            "constant_top_coefficient",
            "direct_slope",
            "fixed_moment",
            "local_fixed_orders",
            "low_period",
            "normalized_scaling",
            "root_partition_fiber",
            "route",
            "tensor_laurent_components",
        }
        if set(value) != expected_keys or value["route"] != "NORMALIZED_GLOBAL_RESIDUE_AND_ROOT_PARTITIONS":
            raise RuntimeError("R private quartic keys")
        root_fiber = value["root_partition_fiber"]
        if (type(root_fiber) is not dict
                or set(root_fiber) != {
                    "parameter_alpha_exponent",
                    "partition_2_plus_2_expansion",
                    "partition_4_centered_root_coefficient",
                    "partition_4_centering_coefficient",
                    "partitions_with_every_part_at_least_two",
                    "simple_root_fixture",
                }
                or root_fiber["partitions_with_every_part_at_least_two"] != [[4], [2, 2]]
                or type(root_fiber["parameter_alpha_exponent"]) is not int
                or type(root_fiber["partition_4_centered_root_coefficient"]) is not int
                or type(root_fiber["partition_4_centering_coefficient"]) is not int):
            raise RuntimeError("R root-partition fiber")
        expansion = root_fiber["partition_2_plus_2_expansion"]
        if type(expansion) is not list or not expansion:
            raise RuntimeError("R partition expansion")
        for term in expansion:
            if (type(term) is not dict
                    or set(term) != {"alpha_exponent", "coefficient", "x_exponent"}
                    or any(type(term[key]) is not int for key in term)):
                raise RuntimeError("R partition expansion term")
        fixture = root_fiber["simple_root_fixture"]
        if (type(fixture) is not dict
                or set(fixture) != {"derivative_at_zero", "rejected", "zero_is_root"}
                or type(fixture["derivative_at_zero"]) is not int
                or fixture["zero_is_root"] is not True
                or fixture["rejected"] is not True):
            raise RuntimeError("R simple-root negative fixture")
        scaling = value["normalized_scaling"]
        if (type(scaling) is not dict
                or set(scaling) != {
                    "explicit_conjugator_exponent",
                    "minimal_invariant_power",
                    "parameter_weight",
                    "root_of_unity_group_order",
                }
                or any(type(item) is not int for item in scaling.values())
                or scaling["minimal_invariant_power"] != 3):
            raise RuntimeError("R normalized scaling")
        tensor = value["tensor_laurent_components"]
        if (type(tensor) is not list or len(tensor) != 3
                or [term.get("component_index") for term in tensor] != [0, 1, 2]):
            raise RuntimeError("R tensor components")
        for term in tensor:
            if (type(term) is not dict
                    or set(term) != {"coefficient", "component_index"}
                    or any(type(term[key]) is not int for key in term)):
                raise RuntimeError("R tensor component")
        if (type(value["constant_top_coefficient"]) is not int
                or type(value["direct_slope"]) is not int):
            raise RuntimeError("R quartic coefficient types")
        constant_ledger = value["constant_term_ledger"]
        if type(constant_ledger) is not list or not constant_ledger:
            raise RuntimeError("R constant coefficient ledger")
        for term in constant_ledger:
            if (type(term) is not dict
                    or set(term) != {
                        "contribution", "exponents", "source_coefficient", "top_coefficient"
                    }
                    or type(term["exponents"]) is not list
                    or len(term["exponents"]) != 3
                    or any(type(item) is not int for item in term["exponents"])
                    or any(
                        type(term[key]) is not int
                        for key in ("contribution", "source_coefficient", "top_coefficient")
                    )):
                raise RuntimeError("R constant ledger term")
        fixed = value["fixed_moment"]
        if (type(fixed) is not dict
                or set(fixed) != {
                    "fixed_moment",
                    "q_square_factorization_remainder",
                    "q_square_quotient_factor",
                    "trace_square_factorization_remainder",
                }
                or fixed.get("fixed_moment") != 0
                or type(fixed.get("fixed_moment")) is not int
                or fixed.get("trace_square_factorization_remainder") != []
                or fixed.get("q_square_factorization_remainder") != []
                or type(fixed.get("q_square_quotient_factor")) is not list
                or len(fixed["q_square_quotient_factor"]) != 1):
            raise RuntimeError("R Step10 fixed-moment witness")
        for term in fixed["q_square_quotient_factor"]:
            if (type(term) is not dict
                    or set(term) != {"L_exponent", "coefficient", "x_exponent"}
                    or any(type(term[key]) is not int for key in term)):
                raise RuntimeError("R q-square quotient term")
        low_period = value["low_period"]
        if (type(low_period) is not dict
                or set(low_period) != {
                    "factor_h_terms",
                    "fixed_formal_zero_count",
                    "fixed_length",
                    "p_minus_h_square_remainder",
                    "partition_cases",
                    "period_two_ambient_length",
                    "period_two_exact_length",
                    "period_two_support_trace",
                    "q_minus_4x_h_remainder",
                }
                or low_period.get("fixed_length") != 4
                or type(low_period.get("fixed_formal_zero_count")) is not int
                or low_period.get("fixed_formal_zero_count") != 4
                or low_period.get("p_minus_h_square_remainder") != []
                or low_period.get("q_minus_4x_h_remainder") != []
                or type(low_period.get("period_two_support_trace")) is not int
                or type(low_period.get("period_two_ambient_length")) is not int
                or low_period.get("period_two_ambient_length") != 16
                or type(low_period.get("period_two_exact_length")) is not int
                or low_period.get("period_two_exact_length") != 12
                or type(low_period.get("partition_cases")) is not list
                or [case.get("root_partition") for case in low_period["partition_cases"]]
                != [[2, 2], [4]]):
            raise RuntimeError("R symbolic low-period partitions")
        factor_terms = low_period["factor_h_terms"]
        if type(factor_terms) is not list or not factor_terms:
            raise RuntimeError("R symbolic factor terms")
        for term in factor_terms:
            if (type(term) is not dict
                    or set(term) != {"L_exponent", "coefficient", "x_exponent"}
                    or any(type(term[key]) is not int for key in term)):
                raise RuntimeError("R symbolic factor term")
        for case in low_period["partition_cases"]:
            if (type(case) is not dict
                    or set(case) != {
                        "fixed_formal_values",
                        "fixed_length",
                        "period_two_ambient_length",
                        "period_two_exact_length",
                        "period_two_support_values",
                        "root_partition",
                        "support_parameter_labels",
                        "support_q_remainders",
                        "symbolic_root_relation",
                    }
                    or type(case["symbolic_root_relation"]) is not str
                    or not case["symbolic_root_relation"]
                    or type(case["support_parameter_labels"]) is not list
                    or any(type(item) is not int for item in case["support_parameter_labels"])
                    or type(case["support_q_remainders"]) is not list
                    or len(case["support_q_remainders"]) != len(case["root_partition"])
                    or any(remainder != [] for remainder in case["support_q_remainders"])
                    or type(case["fixed_formal_values"]) is not list
                    or len(case["fixed_formal_values"]) != 4
                    or any(type(item) is not int for item in case["fixed_formal_values"])
                    or type(case["fixed_length"]) is not int
                    or case["fixed_length"] != 4
                    or type(case["period_two_support_values"]) is not list
                    or len(case["period_two_support_values"]) != 16
                    or any(type(item) is not int for item in case["period_two_support_values"])
                    or type(case["period_two_ambient_length"]) is not int
                    or case["period_two_ambient_length"] != 16
                    or type(case["period_two_exact_length"]) is not int
                    or case["period_two_exact_length"] != 12):
                raise RuntimeError("R low-period partition case")
        local = value["local_fixed_orders"]
    if (type(local) is not list or len(local) != 2
            or [record.get("root_multiplicity") if type(record) is dict else None for record in local]
            != [2, 4]):
        raise RuntimeError("Step13 local multiplicity branches")
    for record in local:
        local_keys = {
            "remaining_leading_coefficient",
            "remaining_order",
            "root_multiplicity",
            "truncation_degree",
            "u_terms",
            "v_terms",
        }
        if track == "R":
            local_keys.add("transverse_jacobian_determinant")
        if type(record) is not dict or set(record) != local_keys:
            raise RuntimeError("Step13 local record keys")
        if (type(record.get("remaining_order")) is not int
                or record["remaining_order"] != record["root_multiplicity"]
                or type(record["root_multiplicity"]) is not int
                or type(record["truncation_degree"]) is not int
                or type(record.get("remaining_leading_coefficient")) is not int
                or record["remaining_leading_coefficient"] != 3):
            raise RuntimeError("Step13 local multiplicity order")
        if track == "R" and (
            type(record["transverse_jacobian_determinant"]) is not int
            or record["transverse_jacobian_determinant"] != 1
        ):
            raise RuntimeError("Step13 transverse Jacobian")
        for term_list_name in ("u_terms", "v_terms"):
            terms = record[term_list_name]
            if type(terms) is not list or not terms:
                raise RuntimeError("Step13 local series terms")
            for term in terms:
                if (type(term) is not dict
                        or set(term) != {"coefficient", "exponent"}
                        or any(type(term[key]) is not int for key in term)):
                    raise RuntimeError("Step13 local series term")


def _validate_exact_private_tree(value: Any) -> None:
    if type(value) is dict:
        if not value or any(type(key) is not str or not key for key in value):
            raise RuntimeError("private witness hollow dictionary")
        for child in value.values():
            _validate_exact_private_tree(child)
        return
    if type(value) is list:
        for child in value:
            _validate_exact_private_tree(child)
        return
    if type(value) is str:
        if not value:
            raise RuntimeError("private witness empty string")
        return
    if type(value) in {bool, int}:
        return
    raise RuntimeError("private witness non-exact or null leaf")


def _validate_private_witness(witness: Any, envelope: dict[str, Any], track: str) -> None:
    route_count_key = (
        "full_high_degree_quotient_count" if track == "Q" else "full_high_degree_residue_count"
    )
    required = {
        "coefficient_diagnostics",
        route_count_key,
        "historical_result_access_count",
        "quartic",
        "registered_engine_index_evaluation_count",
        "schema",
        "track",
    }
    if type(witness) is not dict or set(witness) != required:
        raise RuntimeError("private witness keys")
    _validate_exact_private_tree(witness)
    if (witness["schema"] != "HENON_PERIOD3_TRACK_" + track + "_PRIVATE_WITNESS_V1"
            or witness["track"] != track):
        raise RuntimeError("private witness identity")
    for key, expected in (
        ("registered_engine_index_evaluation_count", 2),
        (route_count_key, 0),
        ("historical_result_access_count", 0),
    ):
        if type(witness[key]) is not int or witness[key] != expected:
            raise RuntimeError("private witness counter")
    _validate_private_quartic(witness["quartic"], track)
    _validate_exact_diagnostics(
        envelope["coefficient_diagnostics"], witness["coefficient_diagnostics"], track
    )


def _validate_track_stage(
    project_root: Path,
    track: str,
    manifest: dict[str, Any],
    claim_sha256: str,
) -> dict[str, Any]:
    track_name = "track_q" if track == "Q" else "track_r"
    stage = project_root / "runtime/candidate_v1/staging" / track_name
    _exact_stage_inventory(stage, {"private_witness.json", "sealed_envelope.json", "access_log.json"})
    witness = validate_canonical_json_file(stage / "private_witness.json")
    envelope = validate_canonical_json_file(stage / "sealed_envelope.json")
    access_log = validate_canonical_json_file(stage / "access_log.json")
    envelope_keys = {
        "candidate_id",
        "coefficient_diagnostics",
        "definitions_sha256",
        "private_witness_sha256",
        "quartic",
        "schema",
        "track",
    }
    if type(envelope) is not dict or set(envelope) != envelope_keys:
        raise RuntimeError("track envelope keys")
    if (envelope["schema"] != "HENON_PERIOD3_TRACK_OUTPUT_V1"
            or envelope["candidate_id"] != CANDIDATE_ID):
        raise RuntimeError("track envelope identity")
    if envelope.get("track") != track or witness.get("track") != track:
        raise RuntimeError("track identity mismatch")
    if envelope.get("definitions_sha256") != manifest["definitions_sha256"]:
        raise RuntimeError("track definitions digest mismatch")
    if sha256_file(stage / "private_witness.json") != envelope.get("private_witness_sha256"):
        raise RuntimeError("private witness digest mismatch")
    _validate_private_witness(witness, envelope, track)
    if len(envelope.get("coefficient_diagnostics", [])) != 2:
        raise RuntimeError("track coefficient diagnostic count")
    if [record.get("index") for record in envelope["coefficient_diagnostics"]] != [8, 9]:
        raise RuntimeError("track coefficient diagnostic order")
    zero_access_fields = (
        "read_outside_allowlist_count",
        "write_outside_allowlist_count",
        "network_access_count",
        "process_access_count",
        "dynamic_loader_access_count",
        "source_document_access_count",
        "acceptance_ledger_access_count",
        "historical_result_access_count",
        "cross_track_scientific_read_count",
    )
    if any(type(access_log.get(key)) is not int or access_log.get(key) != 0 for key in zero_access_fields):
        raise RuntimeError("track provenance access counter")
    log_keys = {
        "schema",
        "claim_sha256",
        "allowlisted_reads",
        "allowlisted_writes",
        "observed_reads",
        "observed_writes",
        "observed_directories",
        "observed_imports",
        *zero_access_fields,
    }
    if type(access_log) is not dict or set(access_log) != log_keys:
        raise RuntimeError("track provenance log keys")
    expected_reads = sorted(
        [
            "runtime/candidate_v1/official/durable_claim.json",
            "code/candidate_v1/shared/definitions.json",
            "code/candidate_v1/" + track_name + "/engine.py",
            "code/candidate_v1/" + track_name + "/runner.py",
        ]
    )
    expected_writes = sorted(
        [
            "runtime/candidate_v1/staging/" + track_name + "/private_witness.json",
            "runtime/candidate_v1/staging/" + track_name + "/sealed_envelope.json",
            "runtime/candidate_v1/staging/" + track_name + "/access_log.json",
        ]
    )
    expected_schema = "HENON_PERIOD3_TRACK_" + track + "_PROVENANCE_ACCESS_LOG_V1"
    if (access_log["schema"] != expected_schema
            or access_log["claim_sha256"] != claim_sha256
            or access_log["allowlisted_reads"] != expected_reads
            or access_log["allowlisted_writes"] != expected_writes):
        raise RuntimeError("track provenance bindings")
    observed_reads = _count_record_map(access_log["observed_reads"], "track observed reads")
    observed_writes = _count_record_map(access_log["observed_writes"], "track observed writes")
    observed_directories = _count_record_map(
        access_log["observed_directories"], "track observed directories"
    )
    observed_imports = _count_record_map(access_log["observed_imports"], "track observed imports")
    if set(observed_reads) != set(expected_reads):
        raise RuntimeError("track actual read provenance")
    if observed_writes != {path: 1 for path in expected_writes}:
        raise RuntimeError("track actual write provenance")
    if set(observed_directories).difference(
        {
            "runtime/candidate_v1/staging/" + track_name,
            "code/candidate_v1/" + track_name,
        }
    ):
        raise RuntimeError("track directory provenance")
    if observed_imports != {"engine": observed_imports.get("engine", 0)}:
        raise RuntimeError("track import provenance")
    return {
        "witness": witness,
        "envelope": envelope,
        "envelope_sha256": sha256_file(stage / "sealed_envelope.json"),
        "witness_sha256": sha256_file(stage / "private_witness.json"),
        "access_log": access_log,
        "access_log_sha256": sha256_file(stage / "access_log.json"),
    }


def _derive_counters(
    project_root: Path,
    q_record: dict[str, Any],
    r_record: dict[str, Any],
    controls: list[dict[str, Any]],
) -> dict[str, Any]:
    static = static_code_audit(project_root / "code")
    if static["status"] != "CLEAN":
        raise RuntimeError("counter derivation requires a clean static audit")
    q_diagnostics = q_record["envelope"]["coefficient_diagnostics"]
    r_diagnostics = r_record["envelope"]["coefficient_diagnostics"]
    order = [record["index"] for record in q_diagnostics]
    if order != [8, 9] or [record["index"] for record in r_diagnostics] != order:
        raise RuntimeError("dispatch-derived registered order")
    all_access = [q_record["access_log"], r_record["access_log"]]
    read_outside = sum(record["read_outside_allowlist_count"] for record in all_access)
    write_outside = sum(record["write_outside_allowlist_count"] for record in all_access)
    source_access = sum(record["source_document_access_count"] for record in all_access)
    ledger_access = sum(record["acceptance_ledger_access_count"] for record in all_access)
    history_access = sum(record["historical_result_access_count"] for record in all_access)
    cross_access = sum(record["cross_track_scientific_read_count"] for record in all_access)
    network_access = sum(record["network_access_count"] for record in all_access)
    counters = {
        "registered_audit_count": 1,
        "registered_candidate_id_count": 1,
        "exact_engine_count": 2,
        "definitions_only_shared_schema_count": 1,
        "shared_schema_scientific_field_count": 0,
        "shared_scientific_implementation_count": static["shared_python_implementation_count"],
        "shared_arithmetic_helper_count": 0,
        "shared_binomial_implementation_count": 0,
        "shared_generalized_binomial_implementation_count": 0,
        "shared_H_A_implementation_count": 0,
        "cross_track_scientific_read_count": cross_access,
        "track_q_collapsed_formula_access_count": 0,
        "track_r_precollapse_formula_access_count": 0,
        "engine_acceptance_ledger_access_count": ledger_access,
        "engine_source_document_access_count": source_access,
        "filesystem_read_outside_allowlist_count": read_outside,
        "filesystem_write_outside_allowlist_count": write_outside,
        "machine_source_proof_verdict_count": 0,
        "floating_field_count": static["science_capability_category_counts"]["floating"],
        "random_seed_count": 0,
        "network_access_count": network_access + static["science_capability_category_counts"]["network"],
        "external_prime_data_access_count": 0,
        "external_zero_data_access_count": 0,
        "external_modulus_data_access_count": 0,
        "new_modulus_scan_count": 0,
        "degree_parameter_scan_count": 0,
        "registered_coefficient_check_count": len(q_diagnostics),
        "registered_coefficient_check_order": order,
        "registered_engine_index_evaluation_count": len(q_diagnostics) + len(r_diagnostics),
        "full_quotient_residue_at_registered_tuple_count": 0,
        "coefficient_check_outside_registered_tuple_count": 0,
        "stored_D8_D9_expected_value_count": 0,
        "stored_expected_E8_E9_count": 0,
        "historical_m2_m7_result_access_count": history_access,
        "historical_source_stage_diagnostic_used_as_evidence_count": 0,
        "numerical_root_solve_count": 0,
        "interpolation_count": 0,
        "post_result_retune_count": 0,
        "universal_Dm_nonvanishing_claim_count": 0,
        "period3_all_m_separation_claim_count": 0,
        "global_quartic_or_conjugacy_claim_count": 0,
    }
    if len(controls) != 8 or any(record["scientific_engine_dispatch_count"] for record in controls):
        raise RuntimeError("counter derivation negative controls")
    ledger = load_exact_json(project_root / "code/candidate_v1/adjudicator/acceptance_ledger.json")
    expected = ledger["counter_expectations"]
    if not exact_same(counters, expected):
        raise RuntimeError("dispatch-derived counter ledger differs from private acceptance ledger")
    return counters


def _validate_adjudicated_stage(
    project_root: Path,
    manifest: dict[str, Any],
    q_record: dict[str, Any],
    r_record: dict[str, Any],
) -> dict[str, Any]:
    final_stage = project_root / "runtime/candidate_v1/staging/final"
    _exact_stage_inventory(final_stage, {"adjudicated_science.json", "access_log.json"})
    adjudicated = validate_canonical_json_file(project_root / ADJUDICATED_PATH)
    access_log = validate_canonical_json_file(final_stage / "access_log.json")
    required = {
        "acceptance_status",
        "candidate_id",
        "coefficient_diagnostics",
        "comparison_only",
        "definitions_sha256",
        "input_sha256",
        "quartic",
        "schema",
        "source_theorem_verdict_emitted",
    }
    if type(adjudicated) is not dict or set(adjudicated) != required:
        raise RuntimeError("adjudicated record keys")
    if (adjudicated["schema"] != "HENON_PERIOD3_NONCOMPUTING_ADJUDICATION_V1"
            or adjudicated["candidate_id"] != CANDIDATE_ID
            or adjudicated["acceptance_status"] != "EXACT_IMPLEMENTATION_AGREEMENT"
            or adjudicated["comparison_only"] is not True
            or adjudicated["source_theorem_verdict_emitted"] is not False):
        raise RuntimeError("adjudicated record identity")
    if adjudicated["definitions_sha256"] != manifest["definitions_sha256"]:
        raise RuntimeError("adjudicated definitions binding")
    if (not exact_same(adjudicated["quartic"], q_record["envelope"]["quartic"])
            or not exact_same(adjudicated["quartic"], r_record["envelope"]["quartic"])
            or not exact_same(
                adjudicated["coefficient_diagnostics"],
                q_record["envelope"]["coefficient_diagnostics"],
            )
            or not exact_same(
                adjudicated["coefficient_diagnostics"],
                r_record["envelope"]["coefficient_diagnostics"],
            )):
        raise RuntimeError("adjudicated scientific boundary mismatch")
    expected_inputs = {
        "track_q_envelope": q_record["envelope_sha256"],
        "track_r_envelope": r_record["envelope_sha256"],
        "types_only_schema": manifest["code_files"][
            "candidate_v1/shared/result_envelope.schema.json"
        ],
        "private_acceptance_ledger": manifest["code_files"][
            "candidate_v1/adjudicator/acceptance_ledger.json"
        ],
    }
    if not exact_same(adjudicated["input_sha256"], expected_inputs):
        raise RuntimeError("adjudicated input digest binding")
    expected_reads = [
        "runtime/candidate_v1/official/durable_claim.json",
        "code/candidate_v1/adjudicator/adjudicate.py",
        "code/candidate_v1/shared/result_envelope.schema.json",
        "runtime/candidate_v1/staging/track_q/sealed_envelope.json",
        "runtime/candidate_v1/staging/track_r/sealed_envelope.json",
        "code/candidate_v1/adjudicator/acceptance_ledger.json",
    ]
    expected_writes = [
        "runtime/candidate_v1/staging/final/adjudicated_science.json",
        "runtime/candidate_v1/staging/final/access_log.json",
    ]
    if (type(access_log) is not dict
            or set(access_log) != {"reads", "schema", "writes"}
            or access_log["schema"] != "HENON_PERIOD3_ADJUDICATOR_LOGICAL_ACCESS_LOG_V1"
            or access_log["reads"] != expected_reads
            or access_log["writes"] != expected_writes):
        raise RuntimeError("adjudicator access provenance")
    return {
        "adjudicated": adjudicated,
        "adjudicated_sha256": sha256_file(project_root / ADJUDICATED_PATH),
        "access_log_sha256": sha256_file(final_stage / "access_log.json"),
    }


def run_registered_audit(project_root: Path) -> None:
    manifest_validation, review_validation = _fresh_preclaim_gates(project_root)
    manifest = manifest_validation["manifest"]
    review_sha256 = review_validation["review_sha256"]
    prepare_runtime_tree(project_root)
    expected_claim = build_claim_object(
        manifest,
        review_sha256,
        manifest_validation["manifest_sha256"],
    )
    claim = None
    try:
        claim = claim_registered_audit(project_root, expected_claim)
        controls = run_negative_controls()
        code_paths = set(manifest["code_files"])
        contract_witnesses = collect_contract_witnesses(project_root, code_paths)
        q_script = project_root / "code/candidate_v1/track_q/runner.py"
        _launch_capability_process(
            q_script,
            _track_capability_token("Q", claim["claim_sha256"], manifest),
            q_script.parent,
        )
        q_record = _validate_track_stage(
            project_root, "Q", manifest, claim["claim_sha256"]
        )
        q_binding = {
            "envelope_sha256": q_record["envelope_sha256"],
            "witness_sha256": q_record["witness_sha256"],
            "access_log_sha256": q_record["access_log_sha256"],
        }
        del q_record
        r_script = project_root / "code/candidate_v1/track_r/runner.py"
        _launch_capability_process(
            r_script,
            _track_capability_token("R", claim["claim_sha256"], manifest),
            r_script.parent,
        )
        r_record = _validate_track_stage(
            project_root, "R", manifest, claim["claim_sha256"]
        )
        q_record = _validate_track_stage(
            project_root, "Q", manifest, claim["claim_sha256"]
        )
        if {
            "envelope_sha256": q_record["envelope_sha256"],
            "witness_sha256": q_record["witness_sha256"],
            "access_log_sha256": q_record["access_log_sha256"],
        } != q_binding:
            raise RuntimeError("Q artifacts changed while R executed")
        adjudicator_script = project_root / "code/candidate_v1/adjudicator/adjudicate.py"
        _launch_capability_process(
            adjudicator_script,
            _adjudicator_capability_token(
                claim["claim_sha256"],
                manifest,
                q_record["envelope_sha256"],
                r_record["envelope_sha256"],
            ),
            adjudicator_script.parent,
        )
        adjudication_record = _validate_adjudicated_stage(
            project_root, manifest, q_record, r_record
        )
        adjudicated = adjudication_record["adjudicated"]
        counters = _derive_counters(project_root, q_record, r_record, controls)
        final_manifest_validation = validate_code_manifest(project_root)
        if (final_manifest_validation["status"] != "VALID"
                or final_manifest_validation["manifest_sha256"]
                != manifest_validation["manifest_sha256"]
                or not exact_same(final_manifest_validation["manifest"], manifest)):
            raise RuntimeError("post-science frozen manifest drift")
        result = {
            "schema": "HENON_PERIOD3_REGISTERED_EXACT_AUDIT_V1",
            "candidate_id": CANDIDATE_ID,
            "run_id": "R100",
            "source_lock_sha256": SOURCE_LOCK_SHA256,
            "source_review_sha256": SOURCE_REVIEW_SHA256,
            "proof_sha256": PROOF_SHA256,
            "code_tree_sha256": manifest["code_tree_sha256"],
            "code_manifest_sha256": manifest_validation["manifest_sha256"],
            "deployment_review_sha256": review_sha256,
            "durable_claim_sha256": claim["claim_sha256"],
            "contract_witnesses": contract_witnesses,
            "negative_controls": controls,
            "track_artifacts": {
                "track_q": q_binding,
                "track_r": {
                    "envelope_sha256": r_record["envelope_sha256"],
                    "witness_sha256": r_record["witness_sha256"],
                    "access_log_sha256": r_record["access_log_sha256"],
                },
                "adjudicated_science_sha256": adjudication_record["adjudicated_sha256"],
                "adjudicator_access_log_sha256": adjudication_record["access_log_sha256"],
            },
            "track_certificates": {
                "track_q": q_record["witness"],
                "track_r": r_record["witness"],
            },
            "audit": adjudicated,
            "counters": counters,
            "registered_coefficient_indices": list(REGISTERED_INDICES),
            "nonclaims": list(NONCLAIMS),
            "source_stage_diagnostic_disclosure": {
                "historical_indices": [2, 3, 4, 5, 6, 7],
                "registered": False,
                "evidentiary": False,
                "values_retained": False,
                "candidate_runtime_access_count": counters["historical_m2_m7_result_access_count"],
            },
            "implementation_audit_status": "EXACT_AGREEMENT_WITH_SOURCE_PROOF_AUTHORITY_EXTERNAL",
        }
        final_review_validation = validate_deployment_review(project_root)
        if (final_review_validation["status"] != "VALID"
                or final_review_validation["review_sha256"] != review_sha256
                or final_review_validation["code_manifest_sha256"]
                != review_validation["code_manifest_sha256"]
                or not exact_same(
                    final_review_validation["review"], review_validation["review"]
                )):
            raise RuntimeError("post-science deployment review drift")
        final_q_record = _validate_track_stage(
            project_root, "Q", manifest, claim["claim_sha256"]
        )
        final_r_record = _validate_track_stage(
            project_root, "R", manifest, claim["claim_sha256"]
        )
        final_adjudication_record = _validate_adjudicated_stage(
            project_root, manifest, final_q_record, final_r_record
        )
        if ({
            "envelope_sha256": final_q_record["envelope_sha256"],
            "witness_sha256": final_q_record["witness_sha256"],
            "access_log_sha256": final_q_record["access_log_sha256"],
        } != q_binding or {
            "envelope_sha256": final_r_record["envelope_sha256"],
            "witness_sha256": final_r_record["witness_sha256"],
            "access_log_sha256": final_r_record["access_log_sha256"],
        } != result["track_artifacts"]["track_r"]
                or final_adjudication_record["adjudicated_sha256"]
                != adjudication_record["adjudicated_sha256"]
                or final_adjudication_record["access_log_sha256"]
                != adjudication_record["access_log_sha256"]):
            raise RuntimeError("post-validation stage artifact drift")
        commit_result(project_root, result)
        terminalize(
            project_root,
            manifest,
            review_sha256,
            expected_claim,
            state=TERMINAL_SUCCESS,
            failure_code=None,
        )
    except BaseException as exc:
        if regular_file(project_root / CLAIM_PATH):
            failure_code = "POST_CLAIM_" + type(exc).__name__.upper()
            terminalize(
                project_root,
                manifest,
                review_sha256,
                expected_claim,
                state=TERMINAL_FAILURE,
                failure_code=failure_code,
            )
        raise


def main() -> None:
    if len(sys.argv) != 1:
        raise RuntimeError("registered audit accepts no arguments")
    project_root = Path(__file__).absolute().parents[3]
    run_registered_audit(project_root)
