from __future__ import annotations

from fractions import Fraction

from cat_torsion.algebra import CAT_MATRIX
from cat_torsion.clock import (
    every_order_witness,
    orbit_sum_monodromy_certificate,
    order_invariance_certificate,
    perturbation_witness,
)
from cat_torsion.proof_contract import (
    negative_trace_index,
    negative_trace_parity_contract,
    norm_determinant_contract,
    primitive_kernel_logic_contract,
)


def test_order_range_invariance_and_discontinuity_witnesses_are_exact():
    point = (Fraction(2, 9), Fraction(1, 6))
    assert order_invariance_certificate(CAT_MATRIX, point)["pass"] is True
    assert all(every_order_witness(order)["pass"] for order in (1, 2, 4, 9, 15))
    for index in (1, 3, 7, 20):
        witness = perturbation_witness(point, index)
        assert witness["pass"] is True
        assert witness["exact_perturbed_order"] == witness["expected_order"]


def test_point_sum_and_monodromy_dependencies_remain_separate():
    record = orbit_sum_monodromy_certificate(10, 5)
    assert record["pass"] is True
    assert record["orbit_sum"] == "10*log(5)"
    assert record["dependence_signature"]["native_monodromy"] == ["period"]


def test_negative_trace_three_branch_contract_and_forbidden_shortcut():
    assert negative_trace_index(13)["primitive_index"] == 26
    assert negative_trace_index(16)["primitive_index"] == 16
    assert negative_trace_index(14)["primitive_index"] == 7
    assert negative_trace_index(18)["imported_source"] == "FLATTERS_THEOREM_3_1_INDEX_7_9_11"
    assert negative_trace_index(26)["imported_source"] == "FLATTERS_THEOREM_1_4"
    assert negative_trace_parity_contract()["pass"] is True
    assert norm_determinant_contract()["pass"] is True
    assert primitive_kernel_logic_contract()["pass"] is True
