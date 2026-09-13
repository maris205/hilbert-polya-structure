"""Science-free normalization and exact Q/R/ledger comparison."""


def _keys(value, required, label):
    if type(value) is not dict or set(value) != set(required):
        raise ValueError("adjudicator keys: " + label)


def _exact(left, right):
    if type(left) is not type(right):
        return False
    if type(left) is dict:
        return set(left) == set(right) and all(_exact(left[key], right[key]) for key in left)
    if type(left) is list:
        return len(left) == len(right) and all(_exact(left[index], right[index]) for index in range(len(left)))
    return left == right


def _q_rational(value):
    _keys(value, {"denominator", "numerator"}, "Q rational")
    if (
        type(value["numerator"]) is not int
        or type(value["denominator"]) is not int
        or value["denominator"] <= 0
    ):
        raise TypeError("Q rational leaf")
    return [value["numerator"], value["denominator"]]


def _q_base_polynomial(value):
    if type(value) is not list:
        raise TypeError("Q polynomial")
    output = []
    for term in value:
        _keys(term, {"coefficient", "exponents_acz0z1"}, "Q term")
        exponents = term["exponents_acz0z1"]
        if (
            type(exponents) is not list
            or len(exponents) != 4
            or any(type(item) is not int or item < 0 for item in exponents)
            or not _exact(exponents[2:], [0, 0])
        ):
            raise ValueError("Q adjudicated polynomial is not in the base ring")
        output.append(
            {
                "a_power": exponents[0],
                "c_power": exponents[1],
                "coefficient": _q_rational(term["coefficient"]),
            }
        )
    return output


def _r_base_polynomial(value):
    if type(value) is not list:
        raise TypeError("R polynomial")
    output = []
    for term in value:
        _keys(term, {"coefficient", "exponents_acxy"}, "R term")
        exponents = term["exponents_acxy"]
        coefficient = term["coefficient"]
        if (
            type(exponents) is not list
            or len(exponents) != 4
            or any(type(item) is not int or item < 0 for item in exponents)
            or not _exact(exponents[2:], [0, 0])
            or type(coefficient) is not list
            or len(coefficient) != 2
            or type(coefficient[0]) is not int
            or type(coefficient[1]) is not int
            or coefficient[1] <= 0
        ):
            raise ValueError("R adjudicated polynomial is not in the base ring")
        output.append(
            {
                "a_power": exponents[0],
                "c_power": exponents[1],
                "coefficient": term["coefficient"],
            }
        )
    return output


def _zero_rational(value):
    return _exact(value, [0, 1])


def _matrix_is_zero(value):
    return (
        type(value) is list
        and len(value) == 2
        and all(type(row) is list and len(row) == 2 for row in value)
        and all(_zero_rational(entry) for row in value for entry in row)
    )


def _normalized_q(certificate):
    controls = certificate["controls"]
    return {
        "N1": {
            "dynatomic_value": _q_rational(controls["N1"]["dynatomic_at_point"]),
            "map_value": _q_rational(controls["N1"]["first_iterate_at_point"]),
            "multiplier": _q_rational(controls["N1"]["multiplier"]),
        },
        "N2": {
            "discriminant": _q_base_polynomial(controls["N2"]["generic_discriminant"]),
            "special_generator_nonzero": controls["N2"]["special_generator_nonzero"],
            "special_square_zero": controls["N2"]["special_nilpotent_square"] == [],
        },
        "N3": {
            "finite_module_exponents": controls["N3"]["finite_module_generator_exponents"],
            "fraction_exponents": controls["N3"]["fraction_exponent_identity"],
            "normalizer_in_semigroup": controls["N3"]["normalizer_exponent_in_subring_semigroup"],
        },
        "N4": {
            "characteristic_rho": [_q_base_polynomial(item) for item in controls["N4"]["characteristic_polynomial_rho"]],
            "characteristic_tau": [_q_base_polynomial(item) for item in controls["N4"]["characteristic_polynomial_tau"]],
            "cycle_product": _q_base_polynomial(controls["N4"]["cycle_product"]),
            "cycle_sum": _q_base_polynomial(controls["N4"]["cycle_sum"]),
            "degree_one_boundary": controls["N4"]["degree_one_boundary"],
            "nontrivial_monodromy_evidence": controls["N4"]["nontrivial_monodromy_evidence"],
            "nu": controls["N4"]["nu"],
            "rank": controls["N4"]["rank"],
            "return_trace": _q_base_polynomial(controls["N4"]["derivative_trace"]),
        },
    }


def _normalized_r(certificate):
    records = certificate["records"]
    return {
        "N1": {
            "dynatomic_value": records["N1"]["formal_dynatomic_value"],
            "map_value": records["N1"]["map_value"],
            "multiplier": records["N1"]["point_multiplier"],
        },
        "N2": {
            "discriminant": _r_base_polynomial(records["N2"]["generic_discriminant"]),
            "special_generator_nonzero": not _matrix_is_zero(records["N2"]["fitting_matrix"]),
            "special_square_zero": _matrix_is_zero(records["N2"]["fitting_square"]),
        },
        "N3": {
            "finite_module_exponents": records["N3"]["finite_module_exponents"],
            "fraction_exponents": records["N3"]["fraction_exponent_identity"],
            "normalizer_in_semigroup": records["N3"]["normalizer_in_semigroup"],
        },
        "N4": {
            "characteristic_rho": [_r_base_polynomial(item) for item in records["N4"]["characteristic_rho"]],
            "characteristic_tau": [_r_base_polynomial(item) for item in records["N4"]["characteristic_tau"]],
            "cycle_product": _r_base_polynomial(records["N4"]["cycle_product"]),
            "cycle_sum": _r_base_polynomial(records["N4"]["cycle_sum"]),
            "degree_one_boundary": records["N4"]["degree_one_boundary"],
            "nontrivial_monodromy_evidence": records["N4"]["nontrivial_monodromy_evidence"],
            "nu": records["N4"]["nu"],
            "rank": records["N4"]["rank"],
            "return_trace": _r_base_polynomial(records["N4"]["return_trace"]),
        },
    }


def _track_route_q(certificate):
    controls = certificate["controls"]
    return {
        "N2": {
            "generic_separable": controls["N2"]["generic_separable"],
            "special_basis_exponents": controls["N2"]["special_basis_exponents"],
            "special_generator_nonzero": controls["N2"]["special_generator_nonzero"],
            "special_nilpotent_square": controls["N2"]["special_nilpotent_square"],
        },
        "N4": {
            "reduction_probe": controls["N4"]["reduction_probe"],
            "reduction_step_count": controls["N4"]["reduction_step_count"],
            "reynolds_z0": controls["N4"]["reynolds_z0"],
            "standard_cycle_exponents": controls["N4"]["standard_cycle_exponents"],
        },
    }


def _track_route_r(certificate):
    records = certificate["records"]
    return {
        "N2": {
            "fitting_matrix": records["N2"]["fitting_matrix"],
            "fitting_square": records["N2"]["fitting_square"],
        },
        "N3": {
            "fraction_power": records["N3"]["fraction_power"],
            "presentation_t_power": records["N3"]["presentation_t_power"],
        },
        "N4": {
            "difference_product": records["N4"]["difference_product"],
            "fitting_rho_pivot_count": records["N4"]["fitting_rho_pivot_count"],
            "fitting_tau_pivot_count": records["N4"]["fitting_tau_pivot_count"],
            "primitive_factor": records["N4"]["primitive_factor"],
            "sylvester_pivot_count": records["N4"]["sylvester_pivot_count"],
        },
    }


def _attack_records_q(certificate):
    controls = certificate["controls"]
    return {key: controls[key] for key in ("N5", "N6", "N7", "N8")}


def _attack_records_r(certificate):
    records = certificate["records"]
    return {key: records[key] for key in ("N5", "N6", "N7", "N8")}


def _contract_presence(definitions, contract_ids):
    if not _exact(definitions.get("schema"), "P13_DEFINITIONS_AND_TYPES_V1"):
        raise ValueError("definitions schema")
    if not _exact(definitions.get("candidate_id"), "henon_primitive_cycle_cover_v1"):
        raise ValueError("definitions candidate")
    if not _exact(definitions.get("proof_contract_identifier_type"), "one of P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12"):
        raise ValueError("definitions contract identifier type")
    if not _exact(contract_ids, ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "P9", "P10", "P11", "P12"]):
        raise ValueError("contract identifier inventory")
    return [
        {"contract_id": identifier, "record_class": "DEFINITION_PRESENCE_RECORD"}
        for identifier in contract_ids
    ]


def _validate_governance(ledger, counters, definitions):
    _keys(ledger, {"attack_requirements", "boundary", "candidate_id", "control_requirements", "machine_authority", "proof_contract_ids", "required_counter_values", "schema", "track_route_requirements"}, "ledger")
    if not _exact(ledger["schema"], "P13_ADJUDICATOR_LEDGER_V1"):
        raise ValueError("ledger schema")
    if not _exact(ledger["candidate_id"], "henon_primitive_cycle_cover_v1"):
        raise ValueError("ledger candidate")
    if not _exact(ledger["machine_authority"], "BOUNDED_IMPLEMENTATION_CONSISTENCY_ONLY"):
        raise ValueError("ledger authority boundary")
    if not _exact(ledger["boundary"]["degree"], 2) or not _exact(ledger["boundary"]["period"], 2):
        raise ValueError("ledger boundary tuple")
    _keys(
        ledger["boundary"],
        {
            "characteristic_rho",
            "characteristic_tau",
            "cycle_product",
            "cycle_sum",
            "degree",
            "degree_one_boundary",
            "nontrivial_monodromy_evidence",
            "nu",
            "period",
            "rank",
            "return_trace",
        },
        "ledger boundary",
    )
    _keys(ledger["control_requirements"], {"N1", "N2", "N3"}, "ledger controls")
    _keys(ledger["track_route_requirements"], {"Q", "R"}, "ledger routes")
    _keys(ledger["attack_requirements"], {"Q", "R"}, "ledger attacks")
    expected_counter_keys = {
        "all_fibers_smooth_claim_count",
        "arbitrary_henon_scope_claim_count",
        "cross_track_scientific_read_count",
        "d_n_grid_scan_count",
        "definitions_only_shared_schema_count",
        "derivative_field_trace_confusion_count",
        "engine_acceptance_ledger_access_count",
        "engine_review_document_access_count",
        "engine_source_document_access_count",
        "exact_engine_count",
        "external_data_access_count",
        "filesystem_read_outside_allowlist_count",
        "filesystem_write_outside_allowlist_count",
        "floating_field_count",
        "formal_equals_actual_global_claim_count",
        "interpolation_count",
        "machine_source_proof_verdict_count",
        "modulus_scan_count",
        "neighbor_d_n_evaluation_count",
        "network_access_count",
        "numerical_root_solve_count",
        "parameter_scan_count",
        "post_result_retune_count",
        "prime_scan_count",
        "proof_audit_block_count",
        "random_seed_count",
        "registered_audit_count",
        "registered_candidate_id_count",
        "shared_arithmetic_helper_count",
        "shared_schema_scientific_field_count",
        "shared_scientific_implementation_count",
        "stored_exploratory_value_count",
        "third_engine_count",
    }
    if type(ledger["required_counter_values"]) is not dict or set(ledger["required_counter_values"]) != expected_counter_keys:
        raise ValueError("ledger exact counter-key inventory")
    if any(type(value) is not int or value < 0 for value in ledger["required_counter_values"].values()):
        raise TypeError("ledger counter values")
    if not _exact(counters, ledger["required_counter_values"]):
        raise ValueError("complete registered counter inventory")
    return _contract_presence(definitions, ledger["proof_contract_ids"])


def _validate_private_routes_and_attacks(q_certificate, r_certificate, ledger):
    if not _exact(_track_route_q(q_certificate), ledger["track_route_requirements"]["Q"]):
        raise ArithmeticError("Track Q private-route mismatch")
    if not _exact(_track_route_r(r_certificate), ledger["track_route_requirements"]["R"]):
        raise ArithmeticError("Track R private-route mismatch")
    if not _exact(_attack_records_q(q_certificate), ledger["attack_requirements"]["Q"]):
        raise ArithmeticError("Track Q attack-ledger mismatch")
    if not _exact(_attack_records_r(r_certificate), ledger["attack_requirements"]["R"]):
        raise ArithmeticError("Track R attack-ledger mismatch")


def adjudicate(q_certificate, r_certificate, ledger, counters, definitions):
    """Compare already validated records without recomputing scientific data."""
    contract_records = _validate_governance(ledger, counters, definitions)
    q_normalized = _normalized_q(q_certificate)
    r_normalized = _normalized_r(r_certificate)
    target = {
        key: ledger["control_requirements"][key]
        for key in ("N1", "N2", "N3")
    }
    target["N4"] = {
        key: ledger["boundary"][key]
        for key in (
            "characteristic_rho",
            "characteristic_tau",
            "cycle_product",
            "cycle_sum",
            "degree_one_boundary",
            "nontrivial_monodromy_evidence",
            "nu",
            "rank",
            "return_trace",
        )
    }
    if not _exact(q_normalized, target) or not _exact(r_normalized, target) or not _exact(q_normalized, r_normalized):
        raise ArithmeticError("bounded Q/R/ledger mismatch")
    _validate_private_routes_and_attacks(q_certificate, r_certificate, ledger)
    return {
        "candidate_id": ledger["candidate_id"],
        "comparison_class": "EXACT_IMPLEMENTATION_CONSISTENCY",
        "contract_presence_records": contract_records,
        "control_record_count": 8,
        "counter_record_count": len(counters),
        "exact_engine_count": 2,
        "machine_authority": ledger["machine_authority"],
        "schema": "P13_ADJUDICATED_CONSISTENCY_V1",
    }
