"""Frozen controls for the PCF Markov--baker carrier."""

from __future__ import annotations

from dataclasses import dataclass
import math

from .model import (
    FACTOR_SIGNS,
    Edge,
    MarkovBakerModel,
    Point,
    Step,
)


ALL_POSITIVE_SIGNS = {edge: 1 for edge in FACTOR_SIGNS}


@dataclass(frozen=True)
class UnitPoint:
    """A point in the unit square used by binary baker controls."""

    x: float
    y: float


@dataclass(frozen=True)
class BinaryStep:
    """Image/preimage and the binary branch responsible for it."""

    point: UnitPoint
    branch: int


class BinaryBaker:
    """Unit-square binary baker with independently frozen branch signs.

    The dyadic control uses signs ``(+,+)`` on both branches.  The folded-tent
    control uses ``(+,+)`` on the increasing branch and ``(-,-)`` on the
    decreasing branch, so it stays symplectic while testing simultaneous
    reversal of stable and unstable coordinates.
    """

    def __init__(
        self,
        unstable_signs: tuple[int, int] = (1, 1),
        stable_signs: tuple[int, int] | None = None,
    ) -> None:
        if stable_signs is None:
            stable_signs = unstable_signs
        if len(unstable_signs) != 2 or len(stable_signs) != 2:
            raise ValueError("binary controls require exactly two signs")
        if any(sign not in (-1, 1) for sign in (*unstable_signs, *stable_signs)):
            raise ValueError("binary signs must be +1 or -1")
        self.unstable_signs = tuple(int(sign) for sign in unstable_signs)
        self.stable_signs = tuple(int(sign) for sign in stable_signs)
        if not self.is_symplectic():
            raise ValueError("binary control must reverse both coordinates together")

    def derivative(
        self, branch: int
    ) -> tuple[tuple[float, float], tuple[float, float]]:
        self._validate_branch(branch)
        return (
            (2.0 * self.unstable_signs[branch], 0.0),
            (0.0, 0.5 * self.stable_signs[branch]),
        )

    def determinant(self, branch: int) -> float:
        derivative = self.derivative(branch)
        return derivative[0][0] * derivative[1][1]

    def is_symplectic(self) -> bool:
        return all(
            math.isclose(
                2.0 * self.unstable_signs[branch]
                * 0.5
                * self.stable_signs[branch],
                1.0,
                rel_tol=0.0,
                abs_tol=0.0,
            )
            for branch in (0, 1)
        )

    def forward(self, point: UnitPoint) -> BinaryStep:
        self._validate_point(point)
        branch = 0 if point.x < 0.5 else 1
        local_x = point.x - 0.5 * branch
        if self.unstable_signs[branch] > 0:
            target_x = 2.0 * local_x
        else:
            target_x = 1.0 - 2.0 * local_x
        bottom = 0.5 * branch
        if self.stable_signs[branch] > 0:
            target_y = bottom + 0.5 * point.y
        else:
            target_y = bottom + 0.5 * (1.0 - point.y)
        return BinaryStep(UnitPoint(target_x, target_y), branch)

    def inverse(self, point: UnitPoint) -> BinaryStep:
        self._validate_point(point)
        branch = 0 if point.y < 0.5 else 1
        bottom = 0.5 * branch
        if self.unstable_signs[branch] > 0:
            source_x = 0.5 * branch + 0.5 * point.x
        else:
            source_x = 0.5 * branch + 0.5 * (1.0 - point.x)
        local_y = 2.0 * (point.y - bottom)
        if self.stable_signs[branch] > 0:
            source_y = local_y
        else:
            source_y = 1.0 - local_y
        return BinaryStep(UnitPoint(source_x, source_y), branch)

    @staticmethod
    def _validate_branch(branch: int) -> None:
        if branch not in (0, 1):
            raise ValueError("branch must be 0 or 1")

    @staticmethod
    def _validate_point(point: UnitPoint) -> None:
        if not isinstance(point, UnitPoint):
            raise TypeError("point must be a UnitPoint")
        if not math.isfinite(point.x) or not math.isfinite(point.y):
            raise ValueError("coordinates must be finite")
        if not (0.0 <= point.x <= 1.0 and 0.0 <= point.y <= 1.0):
            raise ValueError("unit-square coordinates must lie in [0, 1]")


@dataclass(frozen=True)
class FuturePoint:
    """One-sided future coordinate after stable/past information is erased."""

    label: int
    x: float


class LabelErasureControl:
    """Projection that deliberately forgets the stable past coordinate."""

    @staticmethod
    def project(point: Point) -> FuturePoint:
        return FuturePoint(point.label, point.x)

    @staticmethod
    def prehistory_witness(future: FuturePoint) -> tuple[Point, Point]:
        """Give two carrier points with the same one-sided projection."""

        height = MarkovBakerModel.heights[future.label]
        first = Point(future.label, future.x, 0.25 * height)
        second = Point(future.label, future.x, 0.75 * height)
        return first, second

    @classmethod
    def loses_unique_past(cls, future: FuturePoint) -> bool:
        first, second = cls.prehistory_witness(future)
        return first != second and cls.project(first) == cls.project(second)


def make_candidate() -> MarkovBakerModel:
    """Construct the frozen area-preserving PCF carrier."""

    return MarkovBakerModel()


def make_dyadic_baker() -> BinaryBaker:
    """Positive control with the full two-shift and no coordinate reversal."""

    return BinaryBaker((1, 1), (1, 1))


def make_folded_tent_baker() -> BinaryBaker:
    """Positive control for a decreasing branch lifted symplectically."""

    return BinaryBaker((1, -1), (1, -1))


def make_matched_dissipative(rho: float = 0.5) -> MarkovBakerModel:
    """Same Markov future code with determinant ``rho`` on every branch."""

    return MarkovBakerModel(rho=rho, require_symplectic=False)


def make_all_positive_sign_null() -> MarkovBakerModel:
    """Symplectic null with the same unsigned graph and all branch signs +1."""

    return MarkovBakerModel(
        unstable_signs=ALL_POSITIVE_SIGNS,
        stable_signs=ALL_POSITIVE_SIGNS,
    )


def make_anti_symplectic_control() -> MarkovBakerModel:
    """Attempt the single-coordinate reversal and reject it by construction."""

    return MarkovBakerModel(
        unstable_signs=FACTOR_SIGNS,
        stable_signs=ALL_POSITIVE_SIGNS,
        require_symplectic=True,
    )


def inspect_anti_symplectic_derivatives() -> dict[Edge, float]:
    """Expose the rejected determinants without accepting the bad carrier."""

    model = MarkovBakerModel(
        unstable_signs=FACTOR_SIGNS,
        stable_signs=ALL_POSITIVE_SIGNS,
        require_symplectic=False,
    )
    return {
        edge: model.determinant(edge.source, edge.target) for edge in model.edges
    }


def _mobius(n: int) -> int:
    remaining = n
    prime_factors = 0
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            remaining //= divisor
            if remaining % divisor == 0:
                return 0
            prime_factors += 1
            while remaining % divisor == 0:
                remaining //= divisor
        divisor += 1
    if remaining > 1:
        prime_factors += 1
    return -1 if prime_factors % 2 else 1


def binary_primitive_necklace_counts(max_period: int) -> tuple[int, ...]:
    """Exact primitive binary-necklace counts for periods ``1..max_period``."""

    if max_period < 0:
        raise ValueError("max_period must be nonnegative")
    counts = []
    for period in range(1, max_period + 1):
        primitive_words = sum(
            _mobius(divisor) * 2 ** (period // divisor)
            for divisor in range(1, period + 1)
            if period % divisor == 0
        )
        quotient, remainder = divmod(primitive_words, period)
        if remainder:
            raise ArithmeticError("primitive word count was not divisible by period")
        counts.append(quotient)
    return tuple(counts)
