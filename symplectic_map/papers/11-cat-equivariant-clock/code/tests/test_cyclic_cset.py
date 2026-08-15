from equivariant_clock.cyclic_cset import (
    comparable_projection,
    enumeration_cyclic_cset,
    formula_cyclic_cset,
    structural_unit_control,
)


def test_general_cyclic_cset_engines_match_structural_control() -> None:
    formula = formula_cyclic_cset(6, ((2, 1), (3, 1)), 1)
    enumeration = enumeration_cyclic_cset(6, ((2, 1), (3, 1)), 1)
    assert comparable_projection(formula) == comparable_projection(enumeration)
    assert formula["point_exact_classes"] == (
        {"support": 2, "basis": ({"subgroup_order": 3, "coefficient": 1},)},
        {"support": 3, "basis": ({"subgroup_order": 2, "coefficient": 1},)},
    )
    assert formula["g_permutation_recovered_a_coset"] == (1,)


def test_structural_C6_control_is_effective_without_period_six() -> None:
    record = structural_unit_control()
    assert record["namespace"] == "structural_unit_control"
    assert record["is_arithmetic_modulus_row"] is False
    assert "q" not in record
    assert record["pass"]
    assert all(record["checks"].values())
    assert record["formula_engine"]["source_factors"] == (
        {"support": 2, "exponent": 1},
        {"support": 3, "exponent": 1},
    )
    assert record["formula_engine"]["static_inertia_sector_count"] == 5
