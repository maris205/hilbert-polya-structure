from pathlib import Path

from base2_clock.finite_field import (
    frobenius_reduction_audit,
    irreducible_monic_binary,
    polynomial_string,
    two_coefficient_filter_audit,
)
from base2_clock.proof_contract import (
    audit_proof_contract,
    cycle_polynomial_identity_audit,
    frobenius_hensel_norm_audit,
    parameter_and_pcf_audit,
    symbolic_local_contract_audit,
)


PROJECT_ROOT = Path(__file__).absolute().parents[2]


def test_parameter_pcf_and_local_contracts_pass_exactly():
    assert parameter_and_pcf_audit()["pass"] is True
    assert symbolic_local_contract_audit()["pass"] is True
    assert cycle_polynomial_identity_audit()["pass"] is True


def test_frobenius_reduction_is_squarefree_through_frozen_diagnostic_range():
    record = frobenius_reduction_audit(maximum_period=7)
    assert record["pass"] is True
    assert [item["degree"] for item in record["periods"]] == [2, 4, 8, 16, 32, 64, 128]


def test_binary_irreducible_lists_and_n4_witness_are_exact():
    assert [polynomial_string(item) for item in irreducible_monic_binary(2)] == ["T^2+T+1"]
    assert {polynomial_string(item) for item in irreducible_monic_binary(3)} == {
        "T^3+T+1",
        "T^3+T^2+1",
    }
    record = two_coefficient_filter_audit()
    assert record["n2_n3_obstructed"] is True
    assert record["degree_four_filter_insufficient"] is True
    assert record["all_period_inference_allowed"] is False


def test_hensel_norm_repeat_contract_preserves_open_boundary():
    record = frobenius_hensel_norm_audit()
    assert record["pass"] is True
    assert record["logic_checks"]["repeat_does_not_reclassify_exact_period"] is True
    proof = audit_proof_contract(PROJECT_ROOT)
    assert proof["pass"] is True
    assert proof["scientific_boundary"]["base2_equality_all_periods_n_ge_4"] == "OPEN"
