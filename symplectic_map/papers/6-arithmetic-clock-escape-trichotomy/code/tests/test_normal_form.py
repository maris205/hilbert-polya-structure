from fractions import Fraction

from capacity_audit.normal_form import (
    CanonicalReadout,
    MultiplierLogTerm,
    audit_canonical_readout,
    audit_multiplier_closure,
    instantiate_outside_valuation_schema,
    select_one_certificate_per_distinct_hit,
)


def test_rational_multiplier_closure_handles_negative_and_root_powers():
    terms = (
        MultiplierLogTerm("MODULUS_A", Fraction(-2, 3), True, True, frozenset({"BAD_A"})),
        MultiplierLogTerm("MODULUS_B", Fraction(5, 2), True, True, frozenset()),
    )
    record = audit_multiplier_closure(terms, declared_support=frozenset({"BAD_A"}))
    assert record["pass"]
    assert record["common_denominator"] == 6
    assert record["integer_exponents_after_clearing"] == [-4, 15]
    assert record["negative_powers_use_unit_inversion"]
    assert record["positive_root_finite_extension_required"]
    assert record["certified_object"] == "q_squared"
    assert record["real_log_evaluated"] is False


def test_nonnumeric_formal_canonical_readout_passes():
    readout = CanonicalReadout(
        certificate_id="CERTIFICATE_ALPHA",
        v_coordinates=(Fraction(1, 3), Fraction(-2)),
        multiplier_terms=(
            MultiplierLogTerm("MODULUS_ALPHA", Fraction(1, 2), True, True, frozenset()),
        ),
        alpha_real_algebraic=True,
        target_independent=True,
        real_log_branch=True,
    )
    record = audit_canonical_readout(readout, dimension=2, declared_support=frozenset())
    assert record["pass"]
    assert record["target_value_inspected"] is False


def test_nonrational_coefficient_representation_fails_closed():
    term = MultiplierLogTerm("MODULUS_ALPHA", "IRRATIONAL_SCALE", True, True, frozenset())
    record = audit_multiplier_closure((term,), declared_support=frozenset())
    assert not record["pass"]
    assert record["coefficient_errors"] == ["MODULUS_ALPHA"]


def test_support_outside_fixed_set_fails_closed():
    term = MultiplierLogTerm("MODULUS_ALPHA", Fraction(1), True, True, frozenset({"UNDECLARED"}))
    record = audit_multiplier_closure((term,), declared_support=frozenset({"DECLARED"}))
    assert not record["pass"]
    assert record["support_errors"] == ["MODULUS_ALPHA"]


def test_repeated_hits_count_once_and_one_valid_certificate_is_selected():
    record = select_one_certificate_per_distinct_hit(
        [
            ("HIT_A", "CERT_A1", True),
            ("HIT_A", "CERT_A2", True),
            ("HIT_B", "CERT_B0", False),
            ("HIT_B", "CERT_B1", True),
        ]
    )
    assert record["pass"]
    assert record["distinct_hit_count"] == 2
    assert record["selected"] == {"HIT_A": "CERT_A1", "HIT_B": "CERT_B1"}
    assert record["numeric_target_values_inspected"] is False


def test_numeric_hit_label_is_rejected():
    record = select_one_certificate_per_distinct_hit([("17", "CERT", True)])
    assert not record["pass"]
    assert record["invalid_labels"] == ["17"]


def test_outside_valuation_schema_rejects_nonzero_relation_equations():
    record = instantiate_outside_valuation_schema([("OUT_A", 2), ("OUT_B", -1)])
    assert record["pass"]
    assert record["nonzero_relation_survives"]
    assert all(not equation["valuation_equation_zero_holds"] for equation in record["equations"])
    assert record["prime_values_generated_or_tested"] is False
