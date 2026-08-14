"""Piecewise-affine carrier for the three-state PCF Markov factor.

The public implementation uses local coordinates on each labelled rectangle.
Branch selection is deterministic: strips are left closed and right open,
except that the last strip also contains the outer right endpoint.  The map is
one-to-one off the strip boundaries.  ``forward_relation`` and
``inverse_relation`` retain the corresponding closed-boundary relation.

Nothing in this module implements the nonlinear quadratic parent's metric
derivative.  The slopes are the source-locked Parry-affine slopes.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Iterable, Mapping, Sequence


SQRT_TWO = math.sqrt(2.0)
PF_VECTOR = (0.5, 0.5, 1.0 / SQRT_TWO)
RECTANGLE_AREAS = (0.25, 0.25, 0.5)
ADJACENCY = (
    (0, 0, 1),
    (0, 0, 1),
    (1, 1, 0),
)
FACTOR_SIGNS = {
    (0, 2): 1,
    (1, 2): -1,
    (2, 0): -1,
    (2, 1): -1,
}


class CoordinateError(ValueError):
    """Raised when a point is outside its labelled rectangle."""


class ImageError(ValueError):
    """Raised when an inverse is requested outside the map image."""


class SymplecticityError(ValueError):
    """Raised when a requested carrier has a non-symplectic branch."""


@dataclass(frozen=True, order=True)
class Edge:
    """A directed Markov edge."""

    source: int
    target: int


@dataclass(frozen=True)
class Point:
    """Local coordinates in one labelled rectangle."""

    label: int
    x: float
    y: float


@dataclass(frozen=True)
class Step:
    """A point together with the forward edge used to obtain it."""

    point: Point
    edge: Edge


def _coerce_sign(value: int, *, name: str) -> int:
    if value not in (-1, 1):
        raise ValueError(f"{name} must be +1 or -1, got {value!r}")
    return int(value)


class MarkovBakerModel:
    """Three-rectangle Parry-affine Markov--baker map.

    Parameters
    ----------
    rho:
        Stable-direction contraction relative to the area-preserving model.
        ``rho=1`` is the candidate; ``rho=1/2`` is the frozen dissipative
        control.
    unstable_signs, stable_signs:
        Optional signs on the four allowed edges.  The candidate uses the
        same factor-orientation sign in both coordinates.  Keeping the two
        mappings separate makes the anti-symplectic negative control
        explicit rather than silently correcting it.
    require_symplectic:
        If true, reject every branch whose determinant differs from one.
    """

    adjacency = ADJACENCY
    widths = PF_VECTOR
    heights = PF_VECTOR
    areas = RECTANGLE_AREAS
    expansion = SQRT_TWO

    def __init__(
        self,
        *,
        rho: float = 1.0,
        unstable_signs: Mapping[tuple[int, int], int] | None = None,
        stable_signs: Mapping[tuple[int, int], int] | None = None,
        require_symplectic: bool = True,
    ) -> None:
        rho = float(rho)
        if not math.isfinite(rho) or not (0.0 < rho <= 1.0):
            raise ValueError("rho must be finite and lie in (0, 1]")
        self.rho = rho
        self.edges = tuple(
            Edge(i, j)
            for i, row in enumerate(self.adjacency)
            for j, allowed in enumerate(row)
            if allowed
        )
        edge_keys = {(edge.source, edge.target) for edge in self.edges}

        raw_unstable = FACTOR_SIGNS if unstable_signs is None else unstable_signs
        raw_stable = raw_unstable if stable_signs is None else stable_signs
        if set(raw_unstable) != edge_keys:
            raise ValueError("unstable_signs must specify exactly the allowed edges")
        if set(raw_stable) != edge_keys:
            raise ValueError("stable_signs must specify exactly the allowed edges")
        self.unstable_signs = {
            key: _coerce_sign(raw_unstable[key], name=f"unstable sign {key}")
            for key in sorted(edge_keys)
        }
        self.stable_signs = {
            key: _coerce_sign(raw_stable[key], name=f"stable sign {key}")
            for key in sorted(edge_keys)
        }

        self._source_bounds: dict[Edge, tuple[float, float]] = {}
        for source in range(3):
            cursor = 0.0
            outgoing = [edge for edge in self.edges if edge.source == source]
            for index, edge in enumerate(outgoing):
                strip_width = self.widths[edge.target] / self.expansion
                high = (
                    self.widths[source]
                    if index == len(outgoing) - 1
                    else cursor + strip_width
                )
                self._source_bounds[edge] = (cursor, high)
                cursor = high
            if not math.isclose(cursor, self.widths[source], abs_tol=2e-15):
                raise AssertionError("right PF vector does not tile a source rectangle")

        self._destination_bounds: dict[Edge, tuple[float, float]] = {}
        for target in range(3):
            cursor = 0.0
            incoming = [edge for edge in self.edges if edge.target == target]
            for index, edge in enumerate(incoming):
                strip_height = self.heights[edge.source] / self.expansion
                high = (
                    self.heights[target]
                    if index == len(incoming) - 1
                    else cursor + strip_height
                )
                self._destination_bounds[edge] = (cursor, high)
                cursor = high
            if not math.isclose(cursor, self.heights[target], abs_tol=2e-15):
                raise AssertionError("left PF vector does not tile a destination rectangle")

        if require_symplectic:
            self.assert_symplectic()

    def is_allowed(self, source: int, target: int) -> bool:
        """Return whether ``source -> target`` is an allowed Markov edge."""

        return (
            0 <= source < len(self.adjacency)
            and 0 <= target < len(self.adjacency)
            and bool(self.adjacency[source][target])
        )

    def source_strip(self, edge: Edge | tuple[int, int]) -> tuple[float, float]:
        """Closed geometric bounds of an edge's source vertical strip."""

        return self._source_bounds[self._edge(edge)]

    def destination_strip(
        self, edge: Edge | tuple[int, int]
    ) -> tuple[float, float]:
        """Closed bounds of the full allocated destination horizontal strip."""

        return self._destination_bounds[self._edge(edge)]

    def destination_image(
        self, edge: Edge | tuple[int, int]
    ) -> tuple[float, float]:
        """Closed vertical image bounds, including dissipative gaps."""

        edge = self._edge(edge)
        low, high = self._destination_bounds[edge]
        return low, low + self.rho * (high - low)

    def branch_derivative(
        self, source: int, target: int
    ) -> tuple[tuple[float, float], tuple[float, float]]:
        """Return the diagonal derivative on one allowed branch."""

        edge = self._edge((source, target))
        key = (edge.source, edge.target)
        return (
            (self.unstable_signs[key] * self.expansion, 0.0),
            (0.0, self.stable_signs[key] * self.rho / self.expansion),
        )

    def determinant(self, source: int, target: int) -> float:
        derivative = self.branch_derivative(source, target)
        return derivative[0][0] * derivative[1][1]

    def is_symplectic(self, *, atol: float = 2e-15) -> bool:
        """Check ``J.T @ Omega @ J == Omega`` on every branch.

        For a two-dimensional diagonal matrix this is exactly the
        determinant-one condition.
        """

        return all(
            math.isclose(
                self.determinant(edge.source, edge.target),
                1.0,
                rel_tol=0.0,
                abs_tol=atol,
            )
            for edge in self.edges
        )

    def assert_symplectic(self, *, atol: float = 2e-15) -> None:
        bad = [
            (edge, self.determinant(edge.source, edge.target))
            for edge in self.edges
            if not math.isclose(
                self.determinant(edge.source, edge.target),
                1.0,
                rel_tol=0.0,
                abs_tol=atol,
            )
        ]
        if bad:
            detail = ", ".join(
                f"{edge.source}->{edge.target}: det={determinant:g}"
                for edge, determinant in bad
            )
            raise SymplecticityError(f"non-symplectic branch derivative(s): {detail}")

    def forward(self, point: Point) -> Step:
        """Apply the deterministic half-open forward implementation."""

        self._validate_point(point)
        edge = self._select_outgoing(point.label, point.x)
        return self._forward_on_edge(point, edge)

    def inverse(self, point: Point) -> Step:
        """Invert a point in the image using destination horizontal strips."""

        self._validate_point(point)
        edge = self._select_incoming(point.label, point.y)
        return self._inverse_on_edge(point, edge)

    def forward_relation(self, point: Point, *, atol: float = 0.0) -> tuple[Step, ...]:
        """Return every closed-boundary forward image compatible with ``point``."""

        self._validate_point(point, atol=atol)
        steps = []
        for edge in self.edges:
            if edge.source != point.label:
                continue
            low, high = self._source_bounds[edge]
            if low - atol <= point.x <= high + atol:
                steps.append(self._forward_on_edge(point, edge))
        return tuple(steps)

    def inverse_relation(self, point: Point, *, atol: float = 0.0) -> tuple[Step, ...]:
        """Return every closed-boundary inverse compatible with an image point."""

        self._validate_point(point, atol=atol)
        steps = []
        for edge in self.edges:
            if edge.target != point.label:
                continue
            low, high = self.destination_image(edge)
            if low - atol <= point.y <= high + atol:
                steps.append(self._inverse_on_edge(point, edge))
        return tuple(steps)

    def sample(self, rng: object, n: int, *, margin: float = 0.0) -> list[Point]:
        """Draw area-distributed local points with a supplied random generator.

        ``rng`` only needs a scalar ``random()`` method (both ``random.Random``
        and NumPy generators satisfy this).  A fractional margin may be used
        to avoid the outer rectangle boundaries in stress tests.
        """

        if n < 0:
            raise ValueError("n must be nonnegative")
        if not (0.0 <= margin < 0.5):
            raise ValueError("margin must lie in [0, 1/2)")
        random_method = getattr(rng, "random", None)
        if random_method is None:
            raise TypeError("rng must provide a scalar random() method")
        cumulative = (
            self.areas[0],
            self.areas[0] + self.areas[1],
            sum(self.areas),
        )
        points: list[Point] = []
        scale = 1.0 - 2.0 * margin
        for _ in range(n):
            selector = float(random_method())
            if selector < cumulative[0]:
                label = 0
            elif selector < cumulative[1]:
                label = 1
            else:
                label = 2
            x = (margin + scale * float(random_method())) * self.widths[label]
            y = (margin + scale * float(random_method())) * self.heights[label]
            points.append(Point(label, x, y))
        return points

    def _edge(self, edge: Edge | tuple[int, int]) -> Edge:
        if not isinstance(edge, Edge):
            try:
                edge = Edge(int(edge[0]), int(edge[1]))
            except (TypeError, ValueError, IndexError) as exc:
                raise ValueError(f"invalid edge {edge!r}") from exc
        if edge not in self._source_bounds:
            raise ValueError(f"edge {edge.source}->{edge.target} is not allowed")
        return edge

    def _validate_point(self, point: Point, *, atol: float = 0.0) -> None:
        if not isinstance(point, Point):
            raise TypeError("point must be a Point")
        if not 0 <= point.label < 3:
            raise CoordinateError(f"invalid rectangle label {point.label!r}")
        if not math.isfinite(point.x) or not math.isfinite(point.y):
            raise CoordinateError("coordinates must be finite")
        width = self.widths[point.label]
        height = self.heights[point.label]
        if not (-atol <= point.x <= width + atol):
            raise CoordinateError(f"x={point.x!r} outside [0, {width!r}]")
        if not (-atol <= point.y <= height + atol):
            raise CoordinateError(f"y={point.y!r} outside [0, {height!r}]")

    @staticmethod
    def _choose_half_open(
        value: float,
        entries: Sequence[tuple[Edge, float, float]],
    ) -> Edge | None:
        for index, (edge, low, high) in enumerate(entries):
            is_last = index == len(entries) - 1
            if low <= value < high or (is_last and value == high):
                return edge
        return None

    def _select_outgoing(self, source: int, x: float) -> Edge:
        entries = [
            (edge, *self._source_bounds[edge])
            for edge in self.edges
            if edge.source == source
        ]
        edge = self._choose_half_open(x, entries)
        if edge is None:
            raise CoordinateError(f"x={x!r} is not in a source strip of R_{source}")
        return edge

    def _select_incoming(self, target: int, y: float) -> Edge:
        entries = [
            (edge, *self.destination_image(edge))
            for edge in self.edges
            if edge.target == target
        ]
        # Choose the later strip at a shared boundary.  If dissipation opens a
        # gap after an image component, that component keeps its upper endpoint.
        closed_matches = [
            edge for edge, low, high in entries if low <= y <= high
        ]
        if closed_matches:
            return closed_matches[-1]
        raise ImageError(f"point at y={y!r} in R_{target} is outside the map image")

    def _forward_on_edge(self, point: Point, edge: Edge) -> Step:
        source, target = edge.source, edge.target
        key = (source, target)
        left, _ = self._source_bounds[edge]
        bottom, _ = self._destination_bounds[edge]
        local_x = point.x - left
        if self.unstable_signs[key] > 0:
            target_x = self.expansion * local_x
        else:
            target_x = self.widths[target] - self.expansion * local_x
        if self.stable_signs[key] > 0:
            target_y = bottom + self.rho * point.y / self.expansion
        else:
            target_y = bottom + self.rho * (
                self.heights[source] - point.y
            ) / self.expansion
        target_x = self._snap_outside_roundoff(
            target_x, 0.0, self.widths[target]
        )
        image_low, image_high = self.destination_image(edge)
        target_y = self._snap_outside_roundoff(
            target_y, image_low, image_high
        )
        return Step(Point(target, target_x, target_y), edge)

    def _inverse_on_edge(self, point: Point, edge: Edge) -> Step:
        source, target = edge.source, edge.target
        key = (source, target)
        left, _ = self._source_bounds[edge]
        bottom, _ = self._destination_bounds[edge]
        if self.unstable_signs[key] > 0:
            source_x = left + point.x / self.expansion
        else:
            source_x = left + (self.widths[target] - point.x) / self.expansion
        image_y = (point.y - bottom) * self.expansion / self.rho
        if self.stable_signs[key] > 0:
            source_y = image_y
        else:
            source_y = self.heights[source] - image_y
        source_low, source_high = self._source_bounds[edge]
        source_x = self._snap_outside_roundoff(
            source_x, source_low, source_high
        )
        source_y = self._snap_outside_roundoff(
            source_y, 0.0, self.heights[source]
        )
        return Step(Point(source, source_x, source_y), edge)

    @staticmethod
    def _snap_outside_roundoff(value: float, low: float, high: float) -> float:
        """Snap only an ulp-scale excursion outside a declared closed bound."""

        tolerance = 16.0 * math.ulp(max(1.0, abs(low), abs(high)))
        if value < low and value >= low - tolerance:
            return low
        if value > high and value <= high + tolerance:
            return high
        return value


def closed_rectangle_area(points: Iterable[Point], model: MarkovBakerModel) -> float:
    """Return the sum of areas of labels represented in ``points``.

    This small diagnostic is intentionally label-aware: repeated labels count
    once, and erasing the label cannot be mistaken for an area computation.
    """

    labels = {point.label for point in points}
    if any(label not in (0, 1, 2) for label in labels):
        raise CoordinateError("invalid label in points")
    return sum(model.areas[label] for label in labels)
