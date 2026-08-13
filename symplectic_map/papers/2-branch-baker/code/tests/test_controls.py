import pytest
import sympy as sp

from branch_baker.controls import (
    ALL_POSITIVE_SIGNS,
    FuturePoint,
    LabelErasureControl,
    UnitPoint,
    binary_primitive_necklace_counts,
    inspect_anti_symplectic_derivatives,
    make_all_positive_sign_null,
    make_anti_symplectic_control,
    make_candidate,
    make_dyadic_baker,
    make_folded_tent_baker,
    make_matched_dissipative,
)
from branch_baker.model import (
    FACTOR_SIGNS,
    Edge,
    ImageError,
    Point,
    SymplecticityError,
)


def assert_unit_point_close(actual: UnitPoint, expected: UnitPoint) -> None:
    assert actual.x == pytest.approx(expected.x, rel=0.0, abs=2e-15)
    assert actual.y == pytest.approx(expected.y, rel=0.0, abs=2e-15)


def test_candidate_factory_retains_frozen_factor_signs() -> None:
    candidate = make_candidate()

    assert candidate.rho == 1.0
    assert candidate.unstable_signs == FACTOR_SIGNS
    assert candidate.stable_signs == FACTOR_SIGNS
    assert candidate.is_symplectic()


@pytest.mark.parametrize(
    ("point", "expected_branch"),
    ((UnitPoint(0.2, 0.7), 0), (UnitPoint(0.8, 0.3), 1)),
)
def test_dyadic_baker_is_an_invertible_symplectic_positive_control(
    point: UnitPoint, expected_branch: int
) -> None:
    baker = make_dyadic_baker()

    forward = baker.forward(point)
    backward = baker.inverse(forward.point)

    assert baker.is_symplectic()
    assert baker.determinant(0) == 1.0
    assert baker.determinant(1) == 1.0
    assert forward.branch == expected_branch
    assert backward.branch == expected_branch
    assert_unit_point_close(backward.point, point)


def test_folded_tent_reverses_both_coordinates_on_decreasing_branch() -> None:
    baker = make_folded_tent_baker()
    point = UnitPoint(0.8, 0.3)

    forward = baker.forward(point)

    assert baker.derivative(0) == ((2.0, 0.0), (0.0, 0.5))
    assert baker.derivative(1) == ((-2.0, 0.0), (0.0, -0.5))
    assert baker.determinant(1) == 1.0
    assert forward.branch == 1
    assert_unit_point_close(forward.point, UnitPoint(0.4, 0.85))
    assert_unit_point_close(baker.inverse(forward.point).point, point)


def test_matched_dissipative_has_same_future_edge_and_half_area_jacobian() -> None:
    candidate = make_candidate()
    dissipative = make_matched_dissipative()
    point = Point(2, 0.47, 0.23)

    candidate_step = candidate.forward(point)
    dissipative_step = dissipative.forward(point)

    assert dissipative.rho == 0.5
    assert candidate_step.edge == dissipative_step.edge
    assert candidate_step.point.label == dissipative_step.point.label
    assert candidate_step.point.x == pytest.approx(dissipative_step.point.x)
    assert not dissipative.is_symplectic()
    for edge in dissipative.edges:
        assert dissipative.determinant(edge.source, edge.target) == pytest.approx(0.5)


def test_matched_dissipative_image_is_not_surjective() -> None:
    dissipative = make_matched_dissipative()
    allocated = dissipative.destination_strip(Edge(2, 0))
    image = dissipative.destination_image(Edge(2, 0))
    assert image[0] == allocated[0]
    assert image[1] < allocated[1]

    with pytest.raises(ImageError):
        dissipative.inverse(Point(0, 0.2, 0.75 * dissipative.heights[0]))


def test_label_erasure_exhibits_two_distinct_pasts_with_one_future() -> None:
    projection = LabelErasureControl()
    future = FuturePoint(2, 0.3)
    first, second = projection.prehistory_witness(future)

    assert first != second
    assert projection.project(first) == future
    assert projection.project(second) == future
    assert projection.loses_unique_past(future)


def test_single_coordinate_reversal_is_rejected_as_anti_symplectic() -> None:
    determinants = inspect_anti_symplectic_derivatives()

    assert determinants[Edge(0, 2)] == 1.0
    assert determinants[Edge(1, 2)] == -1.0
    assert determinants[Edge(2, 0)] == -1.0
    assert determinants[Edge(2, 1)] == -1.0
    with pytest.raises(SymplecticityError, match="det=-1"):
        make_anti_symplectic_control()


def test_all_positive_sign_null_preserves_unsigned_carrier_data() -> None:
    candidate = make_candidate()
    phase_null = make_all_positive_sign_null()

    assert phase_null.adjacency == candidate.adjacency
    assert phase_null.widths == candidate.widths
    assert phase_null.heights == candidate.heights
    assert phase_null.areas == candidate.areas
    assert phase_null.edges == candidate.edges
    assert phase_null.unstable_signs == ALL_POSITIVE_SIGNS
    assert phase_null.stable_signs == ALL_POSITIVE_SIGNS
    assert phase_null.is_symplectic()
    assert phase_null.unstable_signs != candidate.unstable_signs
    positive_weight_matrix = sp.Matrix(
        [
            [
                phase_null.unstable_signs.get((source, target), 0)
                if phase_null.adjacency[source][target]
                else 0
                for target in range(3)
            ]
            for source in range(3)
        ]
    )
    z = sp.Symbol("z")
    assert positive_weight_matrix == sp.Matrix(candidate.adjacency)
    assert sp.factor((sp.eye(3) - z * positive_weight_matrix).det()) == 1 - 2 * z**2


def test_dyadic_primitive_necklace_ledger_through_period_twelve() -> None:
    counts = binary_primitive_necklace_counts(12)

    assert counts == (2, 1, 2, 3, 6, 9, 18, 30, 56, 99, 186, 335)
    assert sum(counts) == 747


def test_binary_necklace_api_handles_empty_and_rejects_negative_period() -> None:
    assert binary_primitive_necklace_counts(0) == ()
    with pytest.raises(ValueError):
        binary_primitive_necklace_counts(-1)
