from henon_audit.controls import (
    determinant_scope_control,
    integral_negative_control,
    planted_bad_prime_control,
    run_controls,
)


def test_planted_denominator_control_finds_two_and_one_half():
    record = planted_bad_prime_control()
    assert record["coefficient_bad_prime_support_frozen_before_multiplier_access"] == [2]
    assert set(record["multipliers"]) == {"1/2", "2"}
    assert record["generic_exact_modulus_pipeline"]["rational_modulus_values"] == ["1/2", "2"]
    assert record["pass"]


def test_integral_control_has_only_unit_rational_modulus():
    record = integral_negative_control()
    assert record["exact_rational_modulus_values"] == ["1"]
    assert record["exact_rational_multiplier_values"] == []
    assert record["unresolved_modulus_classifications"] == []
    assert record["modulus_records"][3]["rational_modulus_values"] == []
    assert record["pass"]


def test_nonunit_jacobian_requires_predeclared_bad_support():
    record = determinant_scope_control()
    assert record["gate_without_declared_bad_primes"] == "REFUSED_DETERMINANT_NOT_DECLARED_S_UNIT"
    assert record["gate_with_bad_prime_2_declared_before_multiplier_access"] == "ALLOWED_WITH_BAD_PRIME_2_TRACKED"
    assert record["pass"]


def test_all_frozen_controls_pass():
    assert run_controls()["pass"]
