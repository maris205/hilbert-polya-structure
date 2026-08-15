from __future__ import annotations

from prime_shell.constants import LOCKED_PRIMES
from prime_shell.finite_field import direct_enumeration_certificate
from prime_shell.mechanisms import mechanism_audit, symbolic_composite_control


def test_equal_weight_repetition_and_fractional_identity() -> None:
    for prime in LOCKED_PRIMES:
        audit = mechanism_audit(direct_enumeration_certificate(prime))
        powers = audit["equal_weight_control"]["power_sums"]
        assert powers[0]["matches_target"] is True
        if prime != 2:
            assert powers[1]["matches_target"] is False
            assert powers[2]["matches_target"] is False
        assert audit["fractional_shell_normalization"]["sum"] == "1"
        assert audit["fractional_shell_normalization"]["equals_one"] is True
        assert audit["fractional_shell_normalization"]["classification"] == (
            "GLOBAL_NORMALIZED_COUNTING"
        )


def test_symbolic_composite_control_never_selects_q() -> None:
    control = symbolic_composite_control()
    assert control["q_value"] is None
    assert control["q_is_symbolic"] is True
    assert control["composite_shells_enumerated"] == 0
    assert "prime ell|q" in control["shell_cardinality"]


def test_zero_weight_boundary_records_discard_cost() -> None:
    audit = mechanism_audit(direct_enumeration_certificate(11))
    boundary = audit["pure_scalar_denominator"]["zero_weight_boundary"]
    assert boundary["retained_weight_one_count"] == 1
    assert boundary["zero_weight_count_required"] == 23
    assert audit["one_orbit_selector"]["discarded_cycle_count"] == 23
