from __future__ import annotations

import pytest

from prime_shell.constants import EXPECTED_LEDGER, LOCKED_PRIMES
from prime_shell.finite_field import (
    analytic_case_certificate,
    comparison_projection,
    direct_enumeration_certificate,
    expected_projection,
    locked_prime,
)
from prime_shell.protocol import canonical_json_bytes


def test_all_locked_rows_match_dual_engines_and_expected_ledger() -> None:
    for prime in LOCKED_PRIMES:
        analytic = analytic_case_certificate(prime)
        direct = direct_enumeration_certificate(prime)
        assert canonical_json_bytes(comparison_projection(analytic)) == canonical_json_bytes(
            comparison_projection(direct)
        )
        assert canonical_json_bytes(comparison_projection(direct)) == canonical_json_bytes(
            expected_projection(prime)
        )
        assert analytic["case"] == EXPECTED_LEDGER[prime]["case"]
        assert all(analytic["case_checks"].values())


def test_forbidden_modulus_rejected() -> None:
    for forbidden in (0, 1, 4, 13, True, "5"):
        with pytest.raises(ValueError):
            locked_prime(forbidden)  # type: ignore[arg-type]


def test_direct_cycles_are_canonical_disjoint_partitions() -> None:
    for prime in LOCKED_PRIMES:
        record = direct_enumeration_certificate(prime)
        cycles = record["canonical_cycles"]
        assert record["partition_exact"] is True
        assert len(cycles) == record["m_p"]
        assert all(cycle[0] == min(cycle) for cycle in cycles)
