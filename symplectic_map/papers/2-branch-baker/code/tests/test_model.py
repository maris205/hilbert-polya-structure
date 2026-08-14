import math
import random

import pytest

from branch_baker.model import (
    ADJACENCY,
    FACTOR_SIGNS,
    PF_VECTOR,
    RECTANGLE_AREAS,
    SQRT_TWO,
    CoordinateError,
    Edge,
    ImageError,
    MarkovBakerModel,
    Point,
)


EXPECTED_EDGES = (
    Edge(0, 2),
    Edge(1, 2),
    Edge(2, 0),
    Edge(2, 1),
)


def assert_point_close(actual: Point, expected: Point, atol: float = 2e-15) -> None:
    assert actual.label == expected.label
    assert actual.x == pytest.approx(expected.x, rel=0.0, abs=atol)
    assert actual.y == pytest.approx(expected.y, rel=0.0, abs=atol)


def test_frozen_graph_pf_geometry_and_area_tiling() -> None:
    model = MarkovBakerModel()

    assert model.adjacency == ADJACENCY
    assert model.edges == EXPECTED_EDGES
    assert model.widths == PF_VECTOR
    assert model.heights == PF_VECTOR
    assert model.areas == RECTANGLE_AREAS
    assert sum(model.areas) == pytest.approx(1.0)
    assert tuple(w * h for w, h in zip(model.widths, model.heights)) == pytest.approx(
        model.areas
    )

    for source in range(3):
        outgoing = [edge for edge in model.edges if edge.source == source]
        total_width = sum(
            model.source_strip(edge)[1] - model.source_strip(edge)[0]
            for edge in outgoing
        )
        assert total_width == pytest.approx(model.widths[source], abs=2e-15)
    for target in range(3):
        incoming = [edge for edge in model.edges if edge.target == target]
        total_height = sum(
            model.destination_strip(edge)[1] - model.destination_strip(edge)[0]
            for edge in incoming
        )
        assert total_height == pytest.approx(model.heights[target], abs=2e-15)


def test_branch_derivatives_are_frozen_and_symplectic() -> None:
    model = MarkovBakerModel()

    assert model.is_symplectic()
    for edge in model.edges:
        sign = FACTOR_SIGNS[(edge.source, edge.target)]
        derivative = model.branch_derivative(edge.source, edge.target)
        assert derivative == (
            (sign * SQRT_TWO, 0.0),
            (0.0, sign / SQRT_TWO),
        )
        assert model.determinant(edge.source, edge.target) == pytest.approx(1.0)
        # For diagonal J in two dimensions, J^T Omega J has off-diagonal
        # coefficient det(J); spell it out so this is not only an API test.
        a, d = derivative[0][0], derivative[1][1]
        assert a * d == pytest.approx(1.0)
        assert -a * d == pytest.approx(-1.0)


@pytest.mark.parametrize("edge", EXPECTED_EDGES)
def test_forward_inverse_on_every_branch_interior(edge: Edge) -> None:
    model = MarkovBakerModel()
    left, right = model.source_strip(edge)
    source = Point(
        edge.source,
        left + 0.37 * (right - left),
        0.41 * model.heights[edge.source],
    )

    forward = model.forward(source)
    backward = model.inverse(forward.point)

    assert forward.edge == edge
    assert backward.edge == edge
    assert_point_close(backward.point, source)


def test_forward_formula_on_positive_and_reversing_branches() -> None:
    model = MarkovBakerModel()

    positive = Point(0, 0.125, 0.2)
    positive_image = model.forward(positive)
    assert positive_image.edge == Edge(0, 2)
    assert_point_close(
        positive_image.point,
        Point(2, SQRT_TWO * 0.125, 0.2 / SQRT_TWO),
    )

    reversing = Point(1, 0.125, 0.2)
    reversing_image = model.forward(reversing)
    assert reversing_image.edge == Edge(1, 2)
    assert_point_close(
        reversing_image.point,
        Point(
            2,
            model.widths[2] - SQRT_TWO * 0.125,
            model.destination_strip(Edge(1, 2))[0]
            + (model.heights[1] - 0.2) / SQRT_TWO,
        ),
    )


def test_half_open_forward_boundary_and_closed_relation_are_separate() -> None:
    model = MarkovBakerModel()
    split = model.source_strip(Edge(2, 0))[1]
    boundary = Point(2, split, 0.31 * model.heights[2])

    deterministic = model.forward(boundary)
    relation = model.forward_relation(boundary)

    assert deterministic.edge == Edge(2, 1)
    assert tuple(step.edge for step in relation) == (Edge(2, 0), Edge(2, 1))


def test_half_open_inverse_boundary_and_closed_relation_are_separate() -> None:
    model = MarkovBakerModel()
    split = model.destination_strip(Edge(0, 2))[1]
    boundary = Point(2, 0.23 * model.widths[2], split)

    deterministic = model.inverse(boundary)
    relation = model.inverse_relation(boundary)

    assert deterministic.edge == Edge(1, 2)
    assert tuple(step.edge for step in relation) == (Edge(0, 2), Edge(1, 2))


@pytest.mark.parametrize("label", (0, 1, 2))
@pytest.mark.parametrize("x_side", (0.0, 1.0))
@pytest.mark.parametrize("y_side", (0.0, 1.0))
def test_all_outer_rectangle_corners_have_forward_images(
    label: int, x_side: float, y_side: float
) -> None:
    model = MarkovBakerModel()
    source = Point(
        label,
        x_side * model.widths[label],
        y_side * model.heights[label],
    )
    step = model.forward(source)
    assert 0.0 <= step.point.x <= model.widths[step.point.label]
    assert 0.0 <= step.point.y <= model.heights[step.point.label]
    relation = model.forward_relation(source)
    assert step.edge in tuple(item.edge for item in relation)


@pytest.mark.parametrize("label", (0, 1, 2))
@pytest.mark.parametrize("x_side", (0.0, 1.0))
@pytest.mark.parametrize("y_side", (0.0, 1.0))
def test_all_outer_rectangle_corners_have_inverse_relations(
    label: int, x_side: float, y_side: float
) -> None:
    model = MarkovBakerModel()
    target = Point(
        label,
        x_side * model.widths[label],
        y_side * model.heights[label],
    )
    relation = model.inverse_relation(target)
    assert relation
    for step in relation:
        assert 0.0 <= step.point.x <= model.widths[step.point.label]
        assert 0.0 <= step.point.y <= model.heights[step.point.label]


def test_point_validation_and_forbidden_edges() -> None:
    model = MarkovBakerModel()

    with pytest.raises(CoordinateError):
        model.forward(Point(3, 0.0, 0.0))
    with pytest.raises(CoordinateError):
        model.forward(Point(0, model.widths[0] + 1e-6, 0.0))
    with pytest.raises(CoordinateError):
        model.forward(Point(0, math.nan, 0.0))
    with pytest.raises(ValueError, match="not allowed"):
        model.branch_derivative(0, 0)


def test_sampling_is_area_weighted_and_stays_strictly_inside_with_margin() -> None:
    model = MarkovBakerModel()
    points = model.sample(random.Random(811), 200, margin=1e-6)

    assert len(points) == 200
    for point in points:
        assert 0.0 < point.x < model.widths[point.label]
        assert 0.0 < point.y < model.heights[point.label]


def test_inverse_rejects_points_outside_a_dissipative_image_gap() -> None:
    model = MarkovBakerModel(rho=0.5, require_symplectic=False)
    edge = Edge(0, 2)
    image_top = model.destination_image(edge)[1]
    allocation_top = model.destination_strip(edge)[1]
    gap_point = Point(2, 0.2, (image_top + allocation_top) / 2.0)

    with pytest.raises(ImageError, match="outside the map image"):
        model.inverse(gap_point)

    # Unlike a shared conservative boundary, an isolated dissipative image
    # endpoint remains part of that image component.
    endpoint = Point(2, 0.2, image_top)
    assert model.inverse(endpoint).edge == edge
