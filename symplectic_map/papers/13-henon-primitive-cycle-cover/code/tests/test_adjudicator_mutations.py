from copy import deepcopy
import json

import pytest
from jsonschema import Draft202012Validator

from candidate_v1.adjudicator.adjudicate import adjudicate
from candidate_v1.bootstrap import lifecycle
from candidate_v1.bootstrap.canonical import canonical_bytes, sha256_bytes, strict_canonical_load
from candidate_v1.bootstrap.canonical import write_bytes_exclusive
from candidate_v1.bootstrap.constants import (
    CLAIM_RELATIVE,
    EXECUTION_STAGE_RELATIVE,
    Q_STAGE_RELATIVE,
    R_STAGE_RELATIVE,
    RAW_RESULT_RELATIVE,
    RESULT_MANIFEST_RELATIVE,
    TERMINAL_RELATIVE,
)


HEX_A = "a" * 64
HEX_B = "b" * 64
HEX_C = "c" * 64
HEX_D = "d" * 64
TEST_MANIFEST_BYTES = canonical_bytes({"schema": "P13_TEST_MANIFEST_HANDLE"})


def _q_rational(pair):
    return {"denominator": pair[1], "numerator": pair[0]}


def _q_polynomial(polynomial):
    return [
        {
            "coefficient": _q_rational(term["coefficient"]),
            "exponents_acz0z1": [term["a_power"], term["c_power"], 0, 0],
        }
        for term in polynomial
    ]


def _r_polynomial(polynomial):
    return [
        {
            "coefficient": term["coefficient"],
            "exponents_acxy": [term["a_power"], term["c_power"], 0, 0],
        }
        for term in polynomial
    ]


def _certificates(ledger):
    boundary = ledger["boundary"]
    controls = ledger["control_requirements"]
    q_route = ledger["track_route_requirements"]["Q"]
    r_route = ledger["track_route_requirements"]["R"]
    q = {
        "candidate_id": ledger["candidate_id"],
        "certificate_kind": "BOUNDED_EXACT_CONSISTENCY_RECORD",
        "controls": {
            "N1": {
                "dynatomic_at_point": _q_rational(controls["N1"]["dynatomic_value"]),
                "first_iterate_at_point": _q_rational(controls["N1"]["map_value"]),
                "multiplier": _q_rational(controls["N1"]["multiplier"]),
                "unsafe_inference": "REJECTED_FORMAL_TO_ACTUAL",
            },
            "N2": {
                "generic_discriminant": _q_polynomial(controls["N2"]["discriminant"]),
                "generic_separable": q_route["N2"]["generic_separable"],
                "special_basis_exponents": q_route["N2"]["special_basis_exponents"],
                "special_generator_nonzero": q_route["N2"]["special_generator_nonzero"],
                "special_nilpotent_square": q_route["N2"]["special_nilpotent_square"],
                "unsafe_inference": "REJECTED_GENERIC_TO_ALL_FIBERS",
            },
            "N3": {
                "finite_module_generator_exponents": controls["N3"]["finite_module_exponents"],
                "fraction_exponent_identity": controls["N3"]["fraction_exponents"],
                "normalizer_exponent_in_subring_semigroup": controls["N3"]["normalizer_in_semigroup"],
                "unsafe_inference": "REJECTED_BIRATIONAL_TO_NORMAL_EQUALITY",
            },
            "N4": {
                "characteristic_polynomial_rho": [_q_polynomial(value) for value in boundary["characteristic_rho"]],
                "characteristic_polynomial_tau": [_q_polynomial(value) for value in boundary["characteristic_tau"]],
                "cycle_product": _q_polynomial(boundary["cycle_product"]),
                "cycle_sum": _q_polynomial(boundary["cycle_sum"]),
                "degree_one_boundary": boundary["degree_one_boundary"],
                "derivative_trace": _q_polynomial(boundary["return_trace"]),
                "nontrivial_monodromy_evidence": boundary["nontrivial_monodromy_evidence"],
                "nu": boundary["nu"],
                "rank": boundary["rank"],
                "reduction_probe": q_route["N4"]["reduction_probe"],
                "reduction_step_count": q_route["N4"]["reduction_step_count"],
                "reynolds_z0": q_route["N4"]["reynolds_z0"],
                "standard_cycle_exponents": q_route["N4"]["standard_cycle_exponents"],
            },
            **deepcopy(ledger["attack_requirements"]["Q"]),
        },
        "route": "CYCLIC_QUOTIENT_REDUCTION",
        "schema": "P13_Q_EXACT_CERTIFICATE_V1",
        "track": "Q",
    }
    r = {
        "candidate": ledger["candidate_id"],
        "certificate_class": "BOUNDED_EXACT_CONSISTENCY_RECORD",
        "records": {
            "N1": {
                "formal_dynatomic_value": controls["N1"]["dynatomic_value"],
                "map_value": controls["N1"]["map_value"],
                "point_multiplier": controls["N1"]["multiplier"],
                "unsafe_step": "REJECTED_FORMAL_TO_ACTUAL",
            },
            "N2": {
                "fitting_matrix": r_route["N2"]["fitting_matrix"],
                "fitting_square": r_route["N2"]["fitting_square"],
                "generic_discriminant": _r_polynomial(controls["N2"]["discriminant"]),
                "unsafe_step": "REJECTED_GENERIC_TO_ALL_FIBERS",
            },
            "N3": {
                "finite_module_exponents": controls["N3"]["finite_module_exponents"],
                "fraction_exponent_identity": controls["N3"]["fraction_exponents"],
                "fraction_power": r_route["N3"]["fraction_power"],
                "normalizer_in_semigroup": controls["N3"]["normalizer_in_semigroup"],
                "presentation_t_power": r_route["N3"]["presentation_t_power"],
                "unsafe_step": "REJECTED_BIRATIONAL_TO_NORMAL_EQUALITY",
            },
            "N4": {
                "characteristic_rho": [_r_polynomial(value) for value in boundary["characteristic_rho"]],
                "characteristic_tau": [_r_polynomial(value) for value in boundary["characteristic_tau"]],
                "cycle_product": _r_polynomial(boundary["cycle_product"]),
                "cycle_sum": _r_polynomial(boundary["cycle_sum"]),
                "degree_one_boundary": boundary["degree_one_boundary"],
                "difference_product": r_route["N4"]["difference_product"],
                "fitting_rho_pivot_count": r_route["N4"]["fitting_rho_pivot_count"],
                "fitting_tau_pivot_count": r_route["N4"]["fitting_tau_pivot_count"],
                "nontrivial_monodromy_evidence": boundary["nontrivial_monodromy_evidence"],
                "nu": boundary["nu"],
                "primitive_factor": r_route["N4"]["primitive_factor"],
                "rank": boundary["rank"],
                "return_trace": _r_polynomial(boundary["return_trace"]),
                "sylvester_pivot_count": r_route["N4"]["sylvester_pivot_count"],
            },
            **deepcopy(ledger["attack_requirements"]["R"]),
        },
        "route": "SYLVESTER_FITTING_EXTERIOR",
        "schema": "P13_R_EXACT_CERTIFICATE_V1",
        "track": "R",
    }
    return q, r


def _record_fields(prefix, value):
    encoded = canonical_bytes(value)
    return {
        prefix + "_canonical_json": encoded.decode("ascii"),
        prefix + "_sha256": sha256_bytes(encoded),
    }


def _synthetic_registered_payload(paper_root):
    ledger_bytes = (paper_root / "code/candidate_v1/adjudicator/acceptance_ledger.json").read_bytes()
    definitions_bytes = (paper_root / "code/candidate_v1/shared/definitions.json").read_bytes()
    ledger = strict_canonical_load(ledger_bytes)
    definitions = strict_canonical_load(definitions_bytes)
    q_certificate, r_certificate = _certificates(ledger)
    claim = lifecycle.build_claim(
        acceptance_ledger_sha256=sha256_bytes(ledger_bytes),
        code_manifest_sha256=sha256_bytes(TEST_MANIFEST_BYTES),
        code_tree_sha256=HEX_B,
        deployment_review_sha256=HEX_C,
        definitions_sha256=sha256_bytes(definitions_bytes),
        track_bindings={
            "Q": {"engine_sha256": HEX_A, "fixture_sha256": HEX_B, "runner_sha256": HEX_C},
            "R": {"engine_sha256": HEX_D, "fixture_sha256": HEX_A, "runner_sha256": HEX_B},
        },
    )
    claim_bytes = canonical_bytes(claim)
    receipt = {
        "claim": claim,
        "claim_bytes": claim_bytes,
        "claim_sha256": sha256_bytes(claim_bytes),
        "official": paper_root / "runtime/candidate_v1/official",
    }

    def capability(track):
        binding = claim["track_bindings"][track]
        value = {
            "candidate_id": claim["candidate_id"],
            "claim_sha256": receipt["claim_sha256"],
            "definitions_sha256": claim["definitions_sha256"],
            "engine_sha256": binding["engine_sha256"],
            "fixture_sha256": binding["fixture_sha256"],
            "purpose": "REGISTERED_R100",
            "runner_sha256": binding["runner_sha256"],
            "schema": "P13_TRACK_CAPABILITY_V1",
            "track": track,
        }
        value["nonce"] = lifecycle._registered_capability_nonce(
            track,
            value["claim_sha256"],
            value["runner_sha256"],
            value["engine_sha256"],
            value["fixture_sha256"],
            value["definitions_sha256"],
        )
        return value

    q_capability = capability("Q")
    r_capability = capability("R")

    def envelope(track, certificate, capability_value):
        track_name = "track_q" if track == "Q" else "track_r"
        access = {
            "allowed_read_counts": {
                "code/candidate_v1/shared/definitions.json": 1,
                "code/candidate_v1/" + track_name + "/engine.py": 1,
                "code/candidate_v1/" + track_name + "/private_fixture.json": 1,
                "code/candidate_v1/" + track_name + "/runner.py": 0,
            },
            "purpose": "REGISTERED_R100",
            "schema": "P13_TRACK_ACCESS_LOG_V1",
            "track": track,
        }
        access_bytes = canonical_bytes(access)
        certificate_bytes = canonical_bytes(certificate)
        binding = claim["track_bindings"][track]
        return {
            "access_counters": deepcopy(lifecycle.REGISTERED_ACCESS_COUNTERS),
            "access_log_canonical_json": access_bytes.decode("ascii"),
            "access_log_sha256": sha256_bytes(access_bytes),
            "candidate_id": claim["candidate_id"],
            "capability_sha256": sha256_bytes(canonical_bytes(capability_value)),
            "certificate_canonical_json": certificate_bytes.decode("ascii"),
            "certificate_sha256": sha256_bytes(certificate_bytes),
            "claim_sha256": receipt["claim_sha256"],
            "definitions_sha256": claim["definitions_sha256"],
            "engine_sha256": binding["engine_sha256"],
            "fixture_sha256": binding["fixture_sha256"],
            "runner_sha256": binding["runner_sha256"],
            "schema": "P13_BOUNDED_EXACT_TRACK_ENVELOPE_V1",
            "track": track,
        }

    q_envelope = envelope("Q", q_certificate, q_capability)
    r_envelope = envelope("R", r_certificate, r_capability)
    counters = deepcopy(lifecycle.REGISTERED_COUNTER_VALUES)
    adjudication = adjudicate(q_certificate, r_certificate, ledger, counters, definitions)
    payload = {
        "anti_claims": deepcopy(lifecycle.REGISTERED_ANTI_CLAIMS),
        "candidate_id": claim["candidate_id"],
        "claim_sha256": receipt["claim_sha256"],
        "code_manifest_sha256": claim["code_manifest_sha256"],
        "code_tree_sha256": claim["code_tree_sha256"],
        "definitions_sha256": claim["definitions_sha256"],
        "deployment_review_sha256": claim["deployment_review_sha256"],
        "run_id": "R100",
        "same_family_review_limitation": deepcopy(lifecycle.REGISTERED_SAME_FAMILY_REVIEW_LIMITATION),
        "schema": "P13_REGISTERED_AUDIT_PAYLOAD_V1",
        "source_lock_sha256": lifecycle.SOURCE_LOCK_SHA256,
        "source_review_sha256": lifecycle.SOURCE_REVIEW_SHA256,
    }
    for prefix, value in (
        ("acceptance_ledger", ledger),
        ("adjudication", adjudication),
        ("contract_presence", adjudication["contract_presence_records"]),
        ("definitions", definitions),
        ("q_capability", q_capability),
        ("q_envelope", q_envelope),
        ("r_capability", r_capability),
        ("r_envelope", r_envelope),
        ("registered_counters", counters),
    ):
        payload.update(_record_fields(prefix, value))
    return payload, receipt


def _mutate_embedded(payload, prefix, mutation):
    changed = deepcopy(payload)
    value = strict_canonical_load(changed[prefix + "_canonical_json"].encode("ascii"))
    mutation(value)
    changed.update(_record_fields(prefix, value))
    return changed


def _mutate_certificate(payload, envelope_prefix, mutation):
    changed = deepcopy(payload)
    envelope = strict_canonical_load(
        changed[envelope_prefix + "_canonical_json"].encode("ascii")
    )
    certificate = strict_canonical_load(
        envelope["certificate_canonical_json"].encode("ascii")
    )
    mutation(certificate)
    certificate_bytes = canonical_bytes(certificate)
    envelope["certificate_canonical_json"] = certificate_bytes.decode("ascii")
    envelope["certificate_sha256"] = sha256_bytes(certificate_bytes)
    changed.update(_record_fields(envelope_prefix, envelope))
    return changed


def _replace_boolean_with_equal_integer(container, key):
    original = container[key]
    assert type(original) is bool
    container[key] = 1 if original else 0


def test_adjudicator_route_attack_counter_and_contract_mutations_fail_without_science(
    paper_root, tmp_path
):
    payload, receipt = _synthetic_registered_payload(paper_root)
    lifecycle._validate_registered_payload(payload, receipt)

    sealed_root = tmp_path / "production-shaped-seal"
    durable_receipt = lifecycle.create_claim(sealed_root, receipt["claim"])
    operation_calls = []

    def synthetic_operation():
        operation_calls.append(1)
        write_bytes_exclusive(
            sealed_root / Q_STAGE_RELATIVE,
            payload["q_envelope_canonical_json"].encode("ascii"),
        )
        write_bytes_exclusive(
            sealed_root / R_STAGE_RELATIVE,
            payload["r_envelope_canonical_json"].encode("ascii"),
        )
        return payload

    assert lifecycle.run_after_claim(
        sealed_root,
        durable_receipt,
        synthetic_operation,
        lambda: {
            "acceptance_ledger_sha256": durable_receipt["claim"]["acceptance_ledger_sha256"],
            "candidate_id": durable_receipt["claim"]["candidate_id"],
            "candidate_version": durable_receipt["claim"]["candidate_version"],
            "claim_sha256": durable_receipt["claim_sha256"],
            "code_manifest_sha256": durable_receipt["claim"]["code_manifest_sha256"],
            "code_tree_sha256": durable_receipt["claim"]["code_tree_sha256"],
            "definitions_sha256": durable_receipt["claim"]["definitions_sha256"],
            "deployment_review_sha256": durable_receipt["claim"]["deployment_review_sha256"],
            "run_id": durable_receipt["claim"]["run_id"],
            "schema": "P13_FINAL_INBOUND_REVALIDATION_V1",
            "source_lock_sha256": durable_receipt["claim"]["source_lock_sha256"],
            "source_review_sha256": durable_receipt["claim"]["source_review_sha256"],
            "track_bindings": durable_receipt["claim"]["track_bindings"],
        },
    ) == payload
    assert operation_calls == [1]

    q_capability = strict_canonical_load(payload["q_capability_canonical_json"].encode("ascii"))
    r_capability = strict_canonical_load(payload["r_capability_canonical_json"].encode("ascii"))
    q_envelope = strict_canonical_load(payload["q_envelope_canonical_json"].encode("ascii"))
    r_envelope = strict_canonical_load(payload["r_envelope_canonical_json"].encode("ascii"))
    q_certificate = strict_canonical_load(q_envelope["certificate_canonical_json"].encode("ascii"))
    r_certificate = strict_canonical_load(r_envelope["certificate_canonical_json"].encode("ascii"))
    schema_objects = [
        ("code/candidate_v1/shared/durable_claim.schema.json", strict_canonical_load((sealed_root / CLAIM_RELATIVE).read_bytes())),
        ("code/candidate_v1/shared/execution_stage.schema.json", strict_canonical_load((sealed_root / EXECUTION_STAGE_RELATIVE).read_bytes())),
        ("code/candidate_v1/shared/raw_result.schema.json", strict_canonical_load((sealed_root / RAW_RESULT_RELATIVE).read_bytes())),
        ("code/candidate_v1/shared/result_manifest.schema.json", strict_canonical_load((sealed_root / RESULT_MANIFEST_RELATIVE).read_bytes())),
        ("code/candidate_v1/shared/terminal.schema.json", strict_canonical_load((sealed_root / TERMINAL_RELATIVE).read_bytes())),
        ("code/candidate_v1/shared/capability.schema.json", q_capability),
        ("code/candidate_v1/shared/track_envelope.schema.json", q_envelope),
        ("code/candidate_v1/track_q/certificate.schema.json", q_certificate),
        ("code/candidate_v1/shared/capability.schema.json", r_capability),
        ("code/candidate_v1/shared/track_envelope.schema.json", r_envelope),
        ("code/candidate_v1/track_r/certificate.schema.json", r_certificate),
    ]
    assert len(schema_objects) == 11
    for relative, value in schema_objects:
        schema = json.loads((paper_root / relative).read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        Draft202012Validator(schema).validate(value)

    mutations = [
        _mutate_embedded(payload, "q_envelope", lambda value: value["access_counters"].__setitem__("run_science_call_count", True)),
        _mutate_embedded(payload, "q_capability", lambda value: value.__setitem__("nonce", "0" * 32)),
        _mutate_embedded(payload, "registered_counters", lambda value: value.__setitem__("registered_audit_count", True)),
        _mutate_embedded(payload, "acceptance_ledger", lambda value: value["boundary"].__setitem__("rank", True)),
        _mutate_certificate(payload, "q_envelope", lambda value: value["controls"]["N4"].__setitem__("nu", True)),
        _mutate_certificate(payload, "q_envelope", lambda value: value["controls"]["N4"].__setitem__("reduction_step_count", 3)),
        _mutate_certificate(payload, "r_envelope", lambda value: value["records"]["N4"].__setitem__("sylvester_pivot_count", 2)),
        _mutate_certificate(payload, "r_envelope", lambda value: value["records"]["N8"][0].__setitem__("kind", "field_trace")),
        _mutate_embedded(payload, "adjudication", lambda value: value.__setitem__("proof_verdict", "PASS")),
        _mutate_embedded(payload, "adjudication", lambda value: value.__setitem__("machine_source_verdict", "PASS")),
        _mutate_certificate(payload, "q_envelope", lambda value: _replace_boolean_with_equal_integer(value["controls"]["N2"], "generic_separable")),
        _mutate_certificate(payload, "q_envelope", lambda value: _replace_boolean_with_equal_integer(value["controls"]["N2"], "special_generator_nonzero")),
        _mutate_certificate(payload, "q_envelope", lambda value: _replace_boolean_with_equal_integer(value["controls"]["N3"], "normalizer_exponent_in_subring_semigroup")),
        _mutate_certificate(payload, "r_envelope", lambda value: _replace_boolean_with_equal_integer(value["records"]["N3"], "normalizer_in_semigroup")),
        _mutate_certificate(payload, "q_envelope", lambda value: _replace_boolean_with_equal_integer(value["controls"]["N4"], "degree_one_boundary")),
        _mutate_certificate(payload, "q_envelope", lambda value: _replace_boolean_with_equal_integer(value["controls"]["N4"], "nontrivial_monodromy_evidence")),
        _mutate_certificate(payload, "r_envelope", lambda value: _replace_boolean_with_equal_integer(value["records"]["N4"], "degree_one_boundary")),
        _mutate_certificate(payload, "r_envelope", lambda value: _replace_boolean_with_equal_integer(value["records"]["N4"], "nontrivial_monodromy_evidence")),
    ]
    for changed in mutations:
        with pytest.raises((ArithmeticError, TypeError, ValueError)):
            lifecycle._validate_registered_payload(changed, receipt)

    swapped = deepcopy(payload)
    q_capability = strict_canonical_load(swapped["q_capability_canonical_json"].encode("ascii"))
    r_capability = strict_canonical_load(swapped["r_capability_canonical_json"].encode("ascii"))
    q_capability["nonce"] = r_capability["nonce"]
    swapped.update(_record_fields("q_capability", q_capability))
    with pytest.raises(ValueError):
        lifecycle._validate_registered_payload(swapped, receipt)

    ledger = strict_canonical_load(payload["acceptance_ledger_canonical_json"].encode("ascii"))
    counters = strict_canonical_load(payload["registered_counters_canonical_json"].encode("ascii"))
    definitions = strict_canonical_load(payload["definitions_canonical_json"].encode("ascii"))
    q_envelope = strict_canonical_load(payload["q_envelope_canonical_json"].encode("ascii"))
    r_envelope = strict_canonical_load(payload["r_envelope_canonical_json"].encode("ascii"))
    q_certificate = strict_canonical_load(q_envelope["certificate_canonical_json"].encode("ascii"))
    r_certificate = strict_canonical_load(r_envelope["certificate_canonical_json"].encode("ascii"))
    ledger_boolean_paths = [
        ("boundary", "degree_one_boundary"),
        ("boundary", "nontrivial_monodromy_evidence"),
        ("control_requirements", "N2", "special_generator_nonzero"),
        ("control_requirements", "N2", "special_square_zero"),
        ("control_requirements", "N3", "normalizer_in_semigroup"),
        ("track_route_requirements", "Q", "N2", "generic_separable"),
        ("track_route_requirements", "Q", "N2", "special_generator_nonzero"),
    ]
    for path in ledger_boolean_paths:
        changed_ledger = deepcopy(ledger)
        container = changed_ledger
        for key in path[:-1]:
            container = container[key]
        _replace_boolean_with_equal_integer(container, path[-1])
        with pytest.raises((ArithmeticError, TypeError, ValueError)):
            adjudicate(
                q_certificate,
                r_certificate,
                changed_ledger,
                counters,
                definitions,
            )
    changed_counter_expectation = deepcopy(ledger)
    changed_counter_expectation["required_counter_values"]["parameter_scan_count"] = 1
    with pytest.raises((ArithmeticError, ValueError)):
        adjudicate(
            q_certificate,
            r_certificate,
            changed_counter_expectation,
            counters,
            definitions,
        )
