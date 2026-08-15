from equivariant_clock.constants import EXPECTED_LEDGER, LOCKED_MODULI
from equivariant_clock.finite_module import locked_modulus, reconstruct_regular_torsor
from copy import deepcopy

from equivariant_clock.invariants import (
    audit_modulus,
    engine_pair_validation,
    enumeration_engine,
    formula_engine,
)


def test_all_locked_rows_reconstruct_regular_torsors() -> None:
    rows = [reconstruct_regular_torsor(q) for q in LOCKED_MODULI]
    assert [row["q"] for row in rows] == list(LOCKED_MODULI)
    assert all(row["pass"] for row in rows)
    for row in rows:
        assert (row["n"], row["r"], row["m"]) == EXPECTED_LEDGER[row["q"]]
        assert row["direct_group"] == row["algebra_group"]
        assert row["direct_cyclic_locus"] == row["algebra_torsor_image"]
        assert all(row["checks"].values())


def test_definition_separated_invariants_match_dual_engines() -> None:
    rows = [audit_modulus(q) for q in LOCKED_MODULI]
    assert all(row["pass"] for row in rows)
    for row in rows:
        enum = row["enumeration_engine"]
        formula = row["formula_engine"]
        assert row["checks"]["dual_invariant_engines_match"]
        assert enum["point_burnside"]["construction"] != enum["orbit_burnside"]["construction"]
        assert enum["point_burnside"]["exact_period_classes"][0]["support"] == row["torsor"]["r"]
        assert enum["orbit_burnside"]["exact_period_classes"][0]["support"] == 1
        assert enum["g_permutation"]["triple"]["alpha"] == row["torsor"]["cat_matrix_inverse"]
        assert enum["enhanced"]["tuple"]["return_twist"] == row["torsor"]["cat_matrix"]
        assert enum["action_groupoid"]["induced_period"] == 1
        assert enum["generator_ambiguity"]["same_point_fixed_signature"]
        assert enum["generator_ambiguity"]["labelled_twists_distinct"]
        assert set(enum).difference({"engine"}) == set(formula).difference({"engine"})


def test_one_sided_engine_mutations_are_detected() -> None:
    torsor = reconstruct_regular_torsor(3)
    enumeration = enumeration_engine(torsor)
    formula = formula_engine(torsor)
    assert engine_pair_validation(enumeration, formula)["pass"]

    def mutate_support(record):
        record["source_dynamics"]["ordinary_zeta_factors"][0]["support"] += 1

    def mutate_sign(record):
        record["point_burnside"]["zeta_factors"][0]["inverse_power_sign"] = 1

    def mutate_exponent(record):
        record["orbifold"]["point_orbifold_factors"][0]["exponent"] = {
            "numerator": 1,
            "denominator": 5,
        }

    def mutate_twist(record):
        record["g_permutation"]["triple"]["alpha"] = torsor["cat_matrix"]

    def mutate_sector(record):
        record["orbifold"]["nonidentity_nonempty_sector_count"] = 1

    def mutate_period(record):
        record["action_groupoid"]["induced_period"] = 2

    for mutation in (
        mutate_support,
        mutate_sign,
        mutate_exponent,
        mutate_twist,
        mutate_sector,
        mutate_period,
    ):
        changed_enumeration = deepcopy(enumeration)
        mutation(changed_enumeration)
        assert not engine_pair_validation(changed_enumeration, formula)["pass"]
        changed_formula = deepcopy(formula)
        mutation(changed_formula)
        assert not engine_pair_validation(enumeration, changed_formula)["pass"]


def test_forbidden_modulus_and_structural_namespace_rejected() -> None:
    for value in (1, 8, 12, 13):
        try:
            locked_modulus(value)
        except ValueError:
            pass
        else:
            raise AssertionError("unlocked modulus accepted")
    try:
        locked_modulus(6.0)  # type: ignore[arg-type]
    except ValueError:
        pass
    else:
        raise AssertionError("floating modulus accepted")
