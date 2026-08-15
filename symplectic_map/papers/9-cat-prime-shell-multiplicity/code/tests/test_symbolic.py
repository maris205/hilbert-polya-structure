from __future__ import annotations

from prime_shell.finite_field import direct_enumeration_certificate
from prime_shell.symbolic import symbolic_product_audit


def test_raw_and_label_ledgers_remain_distinct_at_ramified_five() -> None:
    audit = symbolic_product_audit(direct_enumeration_certificate(5))
    assert audit["semantics_separated"] is True
    assert audit["raw_return"]["factors"] == [
        {
            "formal_base": "5^(-s*2)",
            "orbit_length": 2,
            "denominator_multiplicity": 2,
        },
        {
            "formal_base": "5^(-s*10)",
            "orbit_length": 10,
            "denominator_multiplicity": 2,
        },
    ]
    assert audit["orbit_label"]["formal_base"] == "5^(-s)"
    assert audit["orbit_label"]["denominator_degree"] == 4


def test_repeat_coefficients_are_exact_rational_strings() -> None:
    audit = symbolic_product_audit(direct_enumeration_certificate(3))
    assert [item["orbit_label_coefficient"] for item in audit["formal_repeats"]] == [
        "2",
        "1",
        "2/3",
    ]
    assert audit["numeric_s_evaluations"] == 0
    assert audit["numeric_log_evaluations"] == 0
