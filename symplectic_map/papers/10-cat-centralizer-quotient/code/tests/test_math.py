from centralizer_q.constants import LEDGER_FIELDS, LOCKED_MODULI, LOCKED_PRIMES
from centralizer_q.finite_module import audit_modulus, expected_record, locked_modulus


def test_all_locked_rows_match_dual_engines_and_expected_ledger() -> None:
    rows = [audit_modulus(q) for q in LOCKED_MODULI]
    assert [row["q"] for row in rows] == list(LOCKED_MODULI)
    assert all(row["pass"] for row in rows)
    for row in rows:
        assert {key: row["ledger"][key] for key in LEDGER_FIELDS} == expected_record(row["q"])
        assert all(row["dual_checks"].values())
        direct = row["direct_engine"]
        assert set(direct["cyclic_locus"]).isdisjoint(direct["discarded_shell"])
        assert set(direct["cyclic_locus"]).union(direct["discarded_shell"]) == set(direct["exact_order_shell"])
        assert direct["full_quotient_transition"]["identity"]
        assert direct["symplectic_quotient_transition"]["identity"]
    assert [row["ledger"]["norm_image_size"] for row in rows] == [1, 2, 2, 6, 10, 2, 2, 6, 2]
    assert rows[2]["ledger"]["norm_image_size"] == 2
    assert rows[-1]["ledger"]["norm_image_size"] == 2
    assert all(row["direct_engine"]["reversing"] is None for row in rows[5:])


def test_forbidden_modulus_rejected() -> None:
    for value in (1, 8, 13, 15):
        try:
            locked_modulus(value)
        except ValueError:
            pass
        else:
            raise AssertionError("unlocked modulus accepted")


def test_prime_reversing_groups_are_exact_and_never_mix_strata() -> None:
    for q in LOCKED_PRIMES:
        record = audit_modulus(q)["direct_engine"]["reversing"]
        assert record is not None
        assert record["constructed_equals_brute"]
        assert record["group_closed"]
        assert record["reversor_relation"]
        assert not record["cyclic_noncyclic_mixing"]
