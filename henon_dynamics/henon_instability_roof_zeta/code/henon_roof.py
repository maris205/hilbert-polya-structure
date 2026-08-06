"""Core mathematics and numerics for the H6 instability-roof experiment.

The module is intentionally independent of the prior project's Python package.
It reads the prior period-12 catalogue only in an optional validation bridge.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from itertools import pairwise
from math import ceil, log
from pathlib import Path
from typing import Iterable, Sequence

import mpmath as mp
import numpy as np
from numpy.typing import NDArray
from scipy.optimize import linear_sum_assignment
import sympy as sp


STATE_NAMES: tuple[str, ...] = ("--", "-+", "+-", "++")
ADJACENCY: tuple[tuple[int, ...], ...] = (
    (1, 0, 1, 0),
    (1, 0, 0, 0),
    (0, 1, 0, 1),
    (0, 1, 0, 0),
)
FIXED_PROTOCOL_SEEDS: tuple[int, ...] = (20260805, 20260806, 20260807)


def contraction_lipschitz_bound(parameter: float | str | mp.mpf = 6) -> mp.mpf:
    """Common-box contraction bound, normalized to ``2/sqrt(17)`` at a=6.

    The neighboring-parameter catalogues reuse the a=6 state boxes only as
    numerical continuations.  On those boxes the square-root derivative bound
    scales by ``sqrt(6/a)``; using the a=6 constant for every neighbor would
    slightly understate the a=5.9 a-posteriori error.
    """

    a_value = mp.mpf(parameter)
    if a_value <= 0:
        raise ValueError("parameter must be positive")
    return (mp.mpf(2) / mp.sqrt(17)) * mp.sqrt(mp.mpf(6) / a_value)


@dataclass(frozen=True)
class OrbitRecord:
    """One primitive symbolic orbit and its high-precision Hénon invariants."""

    parameter: str
    period: int
    canonical_word: str
    sign_word: str
    coordinates: tuple[str, ...]
    contraction_iterations: int
    contraction_delta: str
    contraction_error_bound: str
    recurrence_residual: str
    monodromy_trace: str
    monodromy_determinant: str
    unstable_multiplier: str
    unstable_modulus: str
    orientation: int
    instability_length: str
    action: str

    def numeric_length(self) -> float:
        return float(self.instability_length)


@dataclass(frozen=True)
class WeightedOrbit:
    """Minimal orbit data entering one frozen determinant ledger."""

    period: int
    length: float
    length_text: str = ""
    orientation: int = 1
    amplitude: complex = 1.0 + 0.0j
    orbit_id: str = ""


@dataclass(frozen=True)
class Rectangle:
    real_min: float
    real_max: float
    imag_min: float
    imag_max: float

    def contains(self, value: complex, padding: float = 0.0) -> bool:
        return (
            self.real_min - padding <= value.real <= self.real_max + padding
            and self.imag_min - padding <= value.imag <= self.imag_max + padding
        )

    def boundary_distance(self, value: complex) -> float:
        if not self.contains(value):
            return -min(
                abs(value.real - self.real_min),
                abs(value.real - self.real_max),
                abs(value.imag - self.imag_min),
                abs(value.imag - self.imag_max),
            )
        return min(
            value.real - self.real_min,
            self.real_max - value.real,
            value.imag - self.imag_min,
            self.imag_max - value.imag,
        )


def _rotations(word: tuple[int, ...]) -> list[tuple[int, ...]]:
    return [word[index:] + word[:index] for index in range(len(word))]


def _is_primitive(word: tuple[int, ...]) -> bool:
    period = len(word)
    for divisor in range(1, period):
        if period % divisor == 0 and word == word[:divisor] * (period // divisor):
            return False
    return True


def primitive_state_cycles(period: int) -> list[tuple[int, ...]]:
    """Enumerate every primitive closed A-necklace once, in canonical rotation."""

    if period < 1:
        raise ValueError("period must be positive")
    cycles: set[tuple[int, ...]] = set()

    def extend(path: list[int]) -> None:
        if len(path) == period:
            word = tuple(path)
            if ADJACENCY[word[-1]][word[0]] and _is_primitive(word):
                cycles.add(min(_rotations(word)))
            return
        for target, allowed in enumerate(ADJACENCY[path[-1]]):
            if allowed:
                extend(path + [target])

    for start in range(len(STATE_NAMES)):
        extend([start])
    return sorted(cycles)


def primitive_counts(max_period: int) -> dict[int, int]:
    return {period: len(primitive_state_cycles(period)) for period in range(1, max_period + 1)}


def symbolic_fixed_point_counts(max_period: int) -> dict[int, int]:
    matrix = sp.Matrix(ADJACENCY)
    return {period: int(sp.trace(matrix**period)) for period in range(1, max_period + 1)}


def _mp_string(value: mp.mpf | mp.mpc, digits: int) -> str:
    if isinstance(value, mp.mpc):
        if abs(value.imag) > mp.mpf(10) ** (-(digits - 10)):
            return mp.nstr(value, digits)
        value = value.real
    return mp.nstr(value, digits)


def _signs_from_states(state_word: Sequence[int]) -> tuple[int, ...]:
    return tuple(1 if STATE_NAMES[state][0] == "+" else -1 for state in state_word)


def lift_cycle_by_contraction(
    state_word: Sequence[int],
    parameter: float | str | mp.mpf = 6,
    dps: int = 80,
    max_iterations: int = 2000,
) -> OrbitRecord:
    """Lift one symbolic necklace with the signed square-root contraction."""

    if not state_word:
        raise ValueError("state word must be nonempty")
    canonical = min(_rotations(tuple(int(value) for value in state_word)))
    if tuple(state_word) != canonical:
        raise ValueError("state word must use its canonical cyclic rotation")
    signs = _signs_from_states(canonical)
    period = len(signs)
    with mp.workdps(dps):
        a_value = mp.mpf(parameter)
        coordinates = [mp.mpf(sign) / 2 for sign in signs]
        tolerance = mp.mpf(10) ** (-(dps - 15))
        final_delta = mp.inf
        for iteration in range(1, max_iterations + 1):
            updated: list[mp.mpf] = []
            for index, sign in enumerate(signs):
                radicand = (
                    1 - coordinates[(index - 1) % period] - coordinates[(index + 1) % period]
                ) / a_value
                if radicand <= 0:
                    raise ArithmeticError(
                        f"nonpositive radicand {radicand} for {canonical} at a={a_value}"
                    )
                updated.append(mp.mpf(sign) * mp.sqrt(radicand))
            final_delta = max(abs(new - old) for new, old in zip(updated, coordinates, strict=True))
            coordinates = updated
            if final_delta < tolerance:
                break
        else:
            raise RuntimeError(f"contraction failed after {max_iterations} iterations")

        residuals = [
            coordinates[(index + 1) % period]
            - (1 - a_value * coordinates[index] ** 2 - coordinates[(index - 1) % period])
            for index in range(period)
        ]
        recurrence_residual = max(abs(value) for value in residuals)

        monodromy = mp.eye(2)
        for coordinate in coordinates:
            jacobian = mp.matrix([[-2 * a_value * coordinate, -1], [1, 0]])
            monodromy = jacobian * monodromy
        trace = monodromy[0, 0] + monodromy[1, 1]
        determinant = monodromy[0, 0] * monodromy[1, 1] - monodromy[0, 1] * monodromy[1, 0]
        discriminant = trace**2 - 4 * determinant
        if discriminant <= 0:
            raise ArithmeticError(f"cycle {canonical} is not real hyperbolic")
        eigenvalues = (
            (trace + mp.sqrt(discriminant)) / 2,
            (trace - mp.sqrt(discriminant)) / 2,
        )
        unstable = max(eigenvalues, key=lambda value: abs(value))
        unstable_modulus = abs(unstable)
        if unstable_modulus <= 1:
            raise ArithmeticError(f"cycle {canonical} lacks an unstable multiplier")
        orientation = 1 if unstable > 0 else -1
        instability_length = mp.log(unstable_modulus)

        action = mp.mpf(0)
        for index, coordinate in enumerate(coordinates):
            coordinate_next = coordinates[(index + 1) % period]
            action += coordinate * coordinate_next - coordinate + a_value * coordinate**3 / 3

        contraction_factor = contraction_lipschitz_bound(a_value)
        if contraction_factor >= 1:
            raise ArithmeticError(
                f"common-box contraction bound {contraction_factor} is not below one"
            )
        contraction_error_bound = final_delta / (1 - contraction_factor)

        word_text = "|".join(STATE_NAMES[state] for state in canonical)
        sign_text = "".join("+" if sign > 0 else "-" for sign in signs)
        return OrbitRecord(
            parameter=_mp_string(a_value, dps),
            period=period,
            canonical_word=word_text,
            sign_word=sign_text,
            coordinates=tuple(_mp_string(value, dps) for value in coordinates),
            contraction_iterations=iteration,
            contraction_delta=_mp_string(final_delta, dps),
            contraction_error_bound=_mp_string(contraction_error_bound, dps),
            recurrence_residual=_mp_string(recurrence_residual, dps),
            monodromy_trace=_mp_string(trace, dps),
            monodromy_determinant=_mp_string(determinant, dps),
            unstable_multiplier=_mp_string(unstable, dps),
            unstable_modulus=_mp_string(unstable_modulus, dps),
            orientation=orientation,
            instability_length=_mp_string(instability_length, dps),
            action=_mp_string(action, dps),
        )


def build_orbit_catalog(
    max_period: int,
    parameter: float | str | mp.mpf = 6,
    dps: int = 80,
) -> list[OrbitRecord]:
    records: list[OrbitRecord] = []
    for period in range(1, max_period + 1):
        for state_word in primitive_state_cycles(period):
            records.append(lift_cycle_by_contraction(state_word, parameter=parameter, dps=dps))
    return records


def serialize_catalog(records: Sequence[OrbitRecord]) -> list[dict[str, object]]:
    return [asdict(record) for record in records]


def weighted_orbits(records: Sequence[OrbitRecord]) -> list[WeightedOrbit]:
    return [
        WeightedOrbit(
            period=record.period,
            length=float(record.instability_length),
            length_text=record.instability_length,
            orientation=record.orientation,
            amplitude=1.0 + 0.0j,
            orbit_id=record.canonical_word,
        )
        for record in records
    ]


def exact_clock_audit() -> dict[str, object]:
    """Return exact algebra supporting positivity, action failure, and non-lattice time."""

    variable = sp.symbols("X")
    sqrt7 = sp.sqrt(7)
    fixed_trace = 2 + 2 * sqrt7
    fixed_multiplier = sp.simplify((fixed_trace + sp.sqrt(fixed_trace**2 - 4)) / 2)
    fixed_polynomial = sp.Poly(sp.minimal_polynomial(fixed_multiplier, variable), variable)

    sqrt145 = sp.sqrt(145)
    period4_multiplier = 289 + 24 * sqrt145
    period4_polynomial = sp.Poly(sp.minimal_polynomial(period4_multiplier, variable), variable)

    q = 1 / sp.sqrt(6)
    period4_coordinates = (-q, -q, q, q)
    period4_action = sp.simplify(
        sum(
            period4_coordinates[index] * period4_coordinates[(index + 1) % 4]
            - period4_coordinates[index]
            + 2 * period4_coordinates[index] ** 3
            for index in range(4)
        )
    )

    expansion_lower_bound = sp.Rational(4) - sp.Rational(123, 224)
    fixed_roots = [complex(root) for root in sp.nroots(fixed_polynomial.as_expr(), n=40)]
    root_moduli = sorted(abs(root) for root in fixed_roots)

    return {
        "normalized_unstable_expansion_lower_bound": str(expansion_lower_bound),
        "normalized_unstable_expansion_lower_bound_float": float(expansion_lower_bound),
        "roof_positive": bool(expansion_lower_bound > 1),
        "fixed_orbit_coordinate": str(-(1 + sqrt7) / 6),
        "fixed_orbit_trace": str(fixed_trace),
        "fixed_orbit_multiplier": str(fixed_multiplier),
        "fixed_orbit_multiplier_float": float(sp.N(fixed_multiplier, 18)),
        "fixed_orbit_multiplier_minimal_polynomial": str(fixed_polynomial.as_expr()),
        "fixed_multiplier_conjugate_moduli": root_moduli,
        "fixed_multiplier_all_conjugate_moduli_distinct": all(
            abs(left - right) > 1e-12 for left, right in pairwise(root_moduli)
        ),
        "period4_coordinates": [str(value) for value in period4_coordinates],
        "period4_action": str(period4_action),
        "period4_action_positive_roof": bool(period4_action > 0),
        "period4_multiplier": str(period4_multiplier),
        "period4_multiplier_float": float(sp.N(period4_multiplier, 18)),
        "period4_multiplier_minimal_polynomial": str(period4_polynomial.as_expr()),
        "nonlattice_proof": (
            "If log(L4)/log(L1)=m/n with m,n>0, then L1^m=L4^n. "
            "Every positive power of L1 has four distinct conjugates: its reciprocal pair "
            "and the distinct reciprocal pair arising from sqrt(7)->-sqrt(7). Hence "
            "[Q(L1^m):Q]=4. But L4^n lies in Q(sqrt(145)) and has degree at most 2, "
            "a contradiction. Thus the two periods have irrational ratio and the roof is non-lattice."
        ),
        "nonlattice_proof_inputs_pass": bool(
            fixed_polynomial.as_expr() == variable**4 - 4 * variable**3 - 22 * variable**2 - 4 * variable + 1
            and period4_polynomial.as_expr() == variable**2 - 578 * variable + 1
            and period4_action == 0
            and expansion_lower_bound == sp.Rational(773, 224)
        ),
        "unit_clock_determinant": "1 - exp(-s) - exp(-3*s) - exp(-4*s)",
        "unit_clock_periodicity": "2*pi*i",
        "orientation_twisted_unit_roof_determinant": "1 - exp(-s) + exp(-3*s) - exp(-4*s)",
        "orientation_twisted_factorization": "(1-exp(-2*s))*(1-exp(-s)+exp(-2*s))",
    }


class CycleSection:
    """Degree-N cycle section evaluated through fixed-point traces."""

    def __init__(self, orbits: Sequence[WeightedOrbit], cutoff: int, kappa: int = 0):
        if cutoff < 1:
            raise ValueError("cutoff must be positive")
        if kappa not in (0, 1):
            raise ValueError("kappa must be 0 or 1")
        self.cutoff = int(cutoff)
        self.kappa = int(kappa)
        self.orbits = tuple(orbit for orbit in orbits if orbit.period <= cutoff)
        self._trace_terms: list[tuple[NDArray[np.float64], NDArray[np.complex128]]] = [
            (np.empty(0, dtype=float), np.empty(0, dtype=np.complex128))
            for _ in range(cutoff + 1)
        ]
        for degree in range(1, cutoff + 1):
            lengths: list[float] = []
            coefficients: list[complex] = []
            for orbit in self.orbits:
                if degree % orbit.period:
                    continue
                repetition = degree // orbit.period
                signed_amplitude = orbit.amplitude * (orbit.orientation**kappa)
                lengths.append(repetition * orbit.length)
                coefficients.append(orbit.period * signed_amplitude**repetition)
            self._trace_terms[degree] = (
                np.asarray(lengths, dtype=float),
                np.asarray(coefficients, dtype=np.complex128),
            )

    def traces(self, spectral_values: NDArray[np.complex128]) -> list[NDArray[np.complex128]]:
        spectral = np.asarray(spectral_values, dtype=np.complex128).reshape(-1)
        traces = [np.zeros_like(spectral) for _ in range(self.cutoff + 1)]
        for degree in range(1, self.cutoff + 1):
            lengths, coefficients = self._trace_terms[degree]
            if lengths.size:
                traces[degree] = np.sum(
                    coefficients[:, None] * np.exp(-lengths[:, None] * spectral[None, :]),
                    axis=0,
                )
        return traces

    def _evaluate_flat(self, flat: NDArray[np.complex128]) -> NDArray[np.complex128]:
        traces = self.traces(flat)
        coefficients = [np.zeros_like(flat) for _ in range(self.cutoff + 1)]
        coefficients[0] = np.ones_like(flat)
        for degree in range(1, self.cutoff + 1):
            accumulator = np.zeros_like(flat)
            for index in range(1, degree + 1):
                accumulator += traces[index] * coefficients[degree - index]
            coefficients[degree] = -accumulator / degree
        return np.sum(coefficients, axis=0)

    def evaluate_many(
        self,
        spectral_values: NDArray[np.complex128],
        chunk_size: int = 4096,
    ) -> NDArray[np.complex128]:
        spectral = np.asarray(spectral_values, dtype=np.complex128)
        flat = spectral.reshape(-1)
        values = np.empty_like(flat)
        for start in range(0, flat.size, chunk_size):
            stop = min(start + chunk_size, flat.size)
            values[start:stop] = self._evaluate_flat(flat[start:stop])
        return values.reshape(spectral.shape)

    def evaluate(self, spectral_value: complex) -> complex:
        return complex(self.evaluate_many(np.asarray([spectral_value], dtype=np.complex128))[0])

    def evaluate_with_derivative(self, spectral_value: complex) -> tuple[complex, complex]:
        value = complex(spectral_value)
        traces = np.zeros(self.cutoff + 1, dtype=np.complex128)
        derivatives = np.zeros(self.cutoff + 1, dtype=np.complex128)
        for degree in range(1, self.cutoff + 1):
            lengths, coefficients = self._trace_terms[degree]
            exponentials = np.exp(-lengths * value)
            traces[degree] = np.sum(coefficients * exponentials)
            derivatives[degree] = -np.sum(lengths * coefficients * exponentials)
        cycle_coefficients = np.zeros(self.cutoff + 1, dtype=np.complex128)
        coefficient_derivatives = np.zeros(self.cutoff + 1, dtype=np.complex128)
        cycle_coefficients[0] = 1.0
        for degree in range(1, self.cutoff + 1):
            cycle_coefficients[degree] = -sum(
                traces[index] * cycle_coefficients[degree - index]
                for index in range(1, degree + 1)
            ) / degree
            coefficient_derivatives[degree] = -sum(
                derivatives[index] * cycle_coefficients[degree - index]
                + traces[index] * coefficient_derivatives[degree - index]
                for index in range(1, degree + 1)
            ) / degree
        return complex(np.sum(cycle_coefficients)), complex(np.sum(coefficient_derivatives))

    def product_coefficients(self, spectral_value: complex) -> NDArray[np.complex128]:
        """Independent primitive-factor multiplication implementation."""

        coefficients = np.zeros(self.cutoff + 1, dtype=np.complex128)
        coefficients[0] = 1.0
        for orbit in self.orbits:
            weight = (
                orbit.amplitude
                * (orbit.orientation**self.kappa)
                * np.exp(-complex(spectral_value) * orbit.length)
            )
            updated = coefficients.copy()
            updated[orbit.period :] -= weight * coefficients[: -orbit.period]
            coefficients = updated
        return coefficients

    def trace_coefficients(self, spectral_value: complex) -> NDArray[np.complex128]:
        traces = self.traces(np.asarray([spectral_value], dtype=np.complex128))
        coefficients = np.zeros(self.cutoff + 1, dtype=np.complex128)
        coefficients[0] = 1.0
        for degree in range(1, self.cutoff + 1):
            coefficients[degree] = -sum(
                traces[index][0] * coefficients[degree - index]
                for index in range(1, degree + 1)
            ) / degree
        return coefficients

    def implementation_discrepancy(self, spectral_value: complex) -> float:
        return float(
            np.max(
                np.abs(
                    self.product_coefficients(spectral_value)
                    - self.trace_coefficients(spectral_value)
                )
            )
        )


def mp_cycle_coefficients(
    orbits: Sequence[WeightedOrbit],
    cutoff: int,
    spectral_value: complex | mp.mpc,
    kappa: int,
    dps: int = 80,
    method: str = "product",
) -> list[mp.mpc]:
    """High-precision coefficient implementation for persisted-root checks."""

    with mp.workdps(dps):
        spectral = mp.mpc(spectral_value)
        selected = [orbit for orbit in orbits if orbit.period <= cutoff]
        if method == "product":
            coefficients = [mp.mpc(0) for _ in range(cutoff + 1)]
            coefficients[0] = mp.mpc(1)
            for orbit in selected:
                amplitude = mp.mpc(orbit.amplitude.real, orbit.amplitude.imag)
                length = mp.mpf(orbit.length_text) if orbit.length_text else mp.mpf(orbit.length)
                weight = amplitude * (orbit.orientation**kappa) * mp.exp(-spectral * length)
                updated = list(coefficients)
                for degree in range(orbit.period, cutoff + 1):
                    updated[degree] -= weight * coefficients[degree - orbit.period]
                coefficients = updated
            return coefficients
        if method != "trace":
            raise ValueError("method must be 'product' or 'trace'")
        traces = [mp.mpc(0) for _ in range(cutoff + 1)]
        for degree in range(1, cutoff + 1):
            for orbit in selected:
                if degree % orbit.period:
                    continue
                repetition = degree // orbit.period
                amplitude = mp.mpc(orbit.amplitude.real, orbit.amplitude.imag)
                weight = amplitude * (orbit.orientation**kappa)
                traces[degree] += (
                    orbit.period
                    * weight**repetition
                    * mp.exp(
                        -spectral
                        * repetition
                        * (mp.mpf(orbit.length_text) if orbit.length_text else mp.mpf(orbit.length))
                    )
                )
        coefficients = [mp.mpc(0) for _ in range(cutoff + 1)]
        coefficients[0] = mp.mpc(1)
        for degree in range(1, cutoff + 1):
            coefficients[degree] = -sum(
                traces[index] * coefficients[degree - index]
                for index in range(1, degree + 1)
            ) / degree
        return coefficients


def mp_determinant(
    orbits: Sequence[WeightedOrbit],
    cutoff: int,
    spectral_value: complex | mp.mpc,
    kappa: int,
    dps: int = 80,
    method: str = "product",
) -> mp.mpc:
    return sum(mp_cycle_coefficients(orbits, cutoff, spectral_value, kappa, dps, method))


def newton_refine(section: CycleSection, initial: complex, tolerance: float = 1e-13) -> complex | None:
    value = complex(initial)
    for _ in range(50):
        if not (-0.8 <= value.real <= 0.8 and abs(value.imag) <= 50):
            return None
        with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
            determinant, derivative = section.evaluate_with_derivative(value)
        if not (
            np.isfinite(determinant.real)
            and np.isfinite(determinant.imag)
            and np.isfinite(derivative.real)
            and np.isfinite(derivative.imag)
        ):
            return None
        if abs(derivative) < 1e-14:
            return None
        update = determinant / derivative
        if abs(update) > 0.25:
            update *= 0.25 / abs(update)
        value -= update
        if abs(update) < tolerance and abs(section.evaluate(value)) < 1e-9:
            return value
    return value if abs(section.evaluate(value)) < 1e-8 else None


def _deduplicate_roots(roots: Iterable[complex], tolerance: float = 2e-7) -> list[complex]:
    unique: list[complex] = []
    for root in sorted(roots, key=lambda value: (value.imag, value.real)):
        if all(abs(root - previous) > tolerance for previous in unique):
            unique.append(root)
    return unique


def discover_roots(
    section: CycleSection,
    rectangle: Rectangle,
    real_step: float = 0.01,
    imag_step: float = 0.025,
) -> list[complex]:
    """Discover roots from cell windings and local modulus minima, then Newton-refine."""

    real_count = int(ceil((rectangle.real_max - rectangle.real_min) / real_step)) + 1
    imag_count = int(ceil((rectangle.imag_max - rectangle.imag_min) / imag_step)) + 1
    real_axis = np.linspace(rectangle.real_min, rectangle.real_max, real_count)
    imag_axis = np.linspace(rectangle.imag_min, rectangle.imag_max, imag_count)
    grid = real_axis[:, None] + 1j * imag_axis[None, :]
    values = section.evaluate_many(grid)
    modulus = np.abs(values)

    seeds: list[complex] = []
    # A fine-grid cell winding catches roots even when the modulus minimum is not small.
    v00 = values[:-1, :-1]
    v10 = values[1:, :-1]
    v11 = values[1:, 1:]
    v01 = values[:-1, 1:]
    # A root may land exactly on a development grid point (the twisted sector
    # has the exact root s=0). Local minima catch it; invalid cell ratios are
    # ignored here without changing the redundant Newton seed path.
    with np.errstate(divide="ignore", invalid="ignore"):
        phase_sum = (
            np.angle(v10 / v00)
            + np.angle(v11 / v10)
            + np.angle(v01 / v11)
            + np.angle(v00 / v01)
        )
    winding_cells = np.argwhere(np.abs(np.rint(phase_sum / (2 * np.pi))) >= 1)
    for real_index, imag_index in winding_cells:
        seeds.append(
            complex(
                (real_axis[real_index] + real_axis[real_index + 1]) / 2,
                (imag_axis[imag_index] + imag_axis[imag_index + 1]) / 2,
            )
        )

    # Local minima are a redundant path and help when a phase change sits on a cell edge.
    center = modulus[1:-1, 1:-1]
    neighborhood_min = np.minimum.reduce(
        [
            modulus[row_slice, column_slice]
            for row_slice in (slice(None, -2), slice(1, -1), slice(2, None))
            for column_slice in (slice(None, -2), slice(1, -1), slice(2, None))
        ]
    )
    minima = np.argwhere((center <= neighborhood_min + 1e-15) & (center < 0.5))
    for real_index, imag_index in minima:
        seeds.append(complex(real_axis[real_index + 1], imag_axis[imag_index + 1]))

    roots: list[complex] = []
    for seed in seeds:
        refined = newton_refine(section, seed)
        if refined is None:
            continue
        if rectangle.contains(refined, padding=2e-8) and abs(section.evaluate(refined)) < 1e-7:
            roots.append(refined)
    return _deduplicate_roots(roots)


def contour_points(rectangle: Rectangle, samples: int) -> NDArray[np.complex128]:
    if samples < 64:
        raise ValueError("at least 64 contour samples are required")
    per_edge = samples // 4
    bottom = np.linspace(rectangle.real_min, rectangle.real_max, per_edge, endpoint=False) + 1j * rectangle.imag_min
    right = rectangle.real_max + 1j * np.linspace(rectangle.imag_min, rectangle.imag_max, per_edge, endpoint=False)
    top = np.linspace(rectangle.real_max, rectangle.real_min, per_edge, endpoint=False) + 1j * rectangle.imag_max
    left = rectangle.real_min + 1j * np.linspace(rectangle.imag_max, rectangle.imag_min, per_edge, endpoint=False)
    points = np.concatenate((bottom, right, top, left)).astype(np.complex128)
    return np.concatenate((points, points[:1]))


def argument_principle_count(
    section: CycleSection,
    rectangle: Rectangle,
    samples: int,
) -> dict[str, float | int]:
    points = contour_points(rectangle, samples)
    values = section.evaluate_many(points)
    phase_increments = np.angle(values[1:] / values[:-1])
    winding = int(np.rint(np.sum(phase_increments) / (2 * np.pi)))
    return {
        "samples": int(len(points) - 1),
        "root_count": winding,
        "minimum_boundary_modulus": float(np.min(np.abs(values))),
        "maximum_phase_step": float(np.max(np.abs(phase_increments))),
    }


def match_roots(
    source: Sequence[complex],
    target: Sequence[complex],
    tolerance: float,
) -> dict[str, object]:
    if not source:
        return {"matches": [], "missing_source_indices": [], "extra_target_indices": list(range(len(target)))}
    if not target:
        return {"matches": [], "missing_source_indices": list(range(len(source))), "extra_target_indices": []}
    distances = np.abs(np.asarray(source)[:, None] - np.asarray(target)[None, :])
    source_indices, target_indices = linear_sum_assignment(distances)
    matches: list[dict[str, float | int]] = []
    used_source: set[int] = set()
    used_target: set[int] = set()
    for source_index, target_index in zip(source_indices, target_indices, strict=True):
        distance = float(distances[source_index, target_index])
        if distance <= tolerance:
            used_source.add(int(source_index))
            used_target.add(int(target_index))
            matches.append(
                {
                    "source_index": int(source_index),
                    "target_index": int(target_index),
                    "distance": distance,
                }
            )
    return {
        "matches": matches,
        "missing_source_indices": sorted(set(range(len(source))) - used_source),
        "extra_target_indices": sorted(set(range(len(target))) - used_target),
    }


def root_drift_summary(match: dict[str, object], source_count: int) -> dict[str, float | int]:
    distances = np.asarray([row["distance"] for row in match["matches"]], dtype=float)
    return {
        "source_count": int(source_count),
        "matched_count": int(distances.size),
        "retained_fraction": float(distances.size / source_count) if source_count else 1.0,
        "median_drift": float(np.median(distances)) if distances.size else float("inf"),
        "p90_drift": float(np.quantile(distances, 0.9)) if distances.size else float("inf"),
        "maximum_drift": float(np.max(distances)) if distances.size else float("inf"),
        "missing_count": len(match["missing_source_indices"]),
        "extra_count": len(match["extra_target_indices"]),
    }


def make_control_orbits(
    orbits: Sequence[WeightedOrbit],
    control: str,
    seed: int,
    fixed_length: float,
) -> list[WeightedOrbit]:
    """Build a frozen adversarial control without modifying the source ledger."""

    rng = np.random.default_rng(seed)
    periods = np.asarray([orbit.period for orbit in orbits], dtype=int)
    lengths = np.asarray([orbit.length for orbit in orbits], dtype=float)
    orientations = np.asarray([orbit.orientation for orbit in orbits], dtype=int)
    amplitudes = np.ones(len(orbits), dtype=np.complex128)

    if control == "shuffled_periods":
        periods = rng.permutation(periods)
    elif control == "shuffled_lengths":
        lengths = rng.permutation(lengths)
    elif control == "same_density_random_lengths":
        per_step = lengths / periods
        generated = rng.normal(float(np.mean(per_step)), float(np.std(per_step)), size=len(orbits))
        generated = np.maximum(generated, 0.1 * float(np.mean(per_step)))
        lengths = periods * generated
    elif control == "positive_random_weights":
        raw = rng.normal(0.0, 0.35, size=len(orbits))
        raw -= float(np.mean(raw))
        amplitudes = np.exp(raw).astype(np.complex128)
    elif control == "random_phases":
        amplitudes = np.exp(2j * np.pi * rng.random(len(orbits)))
    elif control == "constant_roof_parent":
        lengths = periods * fixed_length
    else:
        raise ValueError(f"unknown control {control}")

    return [
        WeightedOrbit(
            period=int(periods[index]),
            length=float(lengths[index]),
            length_text="",
            orientation=int(orientations[index]),
            amplitude=complex(amplitudes[index]),
            orbit_id=orbits[index].orbit_id,
        )
        for index in range(len(orbits))
    ]


def compare_prior_catalog(records: Sequence[OrbitRecord], prior_path: Path) -> dict[str, object]:
    import json

    payload = json.loads(prior_path.read_text(encoding="utf-8"))
    prior_rows = {row["canonical_word"]: row for row in payload["selected_orbits"]}
    selected = [record for record in records if record.period <= 12]
    missing = sorted(set(prior_rows) - {record.canonical_word for record in selected})
    extra = sorted({record.canonical_word for record in selected} - set(prior_rows))
    discrepancies: list[dict[str, object]] = []
    with mp.workdps(110):
        for record in selected:
            if record.canonical_word not in prior_rows:
                continue
            prior = prior_rows[record.canonical_word]
            current_multiplier = mp.mpf(record.unstable_modulus)
            prior_multiplier = mp.mpf(prior["unstable_modulus"])
            discrepancies.append(
                {
                    "canonical_word": record.canonical_word,
                    "period": record.period,
                    "absolute_multiplier_difference": mp.nstr(
                        abs(current_multiplier - prior_multiplier), 30
                    ),
                    "relative_multiplier_difference": mp.nstr(
                        abs(current_multiplier - prior_multiplier) / prior_multiplier, 30
                    ),
                }
            )
        maximum_relative = max(
            (mp.mpf(row["relative_multiplier_difference"]) for row in discrepancies),
            default=mp.mpf(0),
        )
    return {
        "prior_path": str(prior_path),
        "prior_count": len(prior_rows),
        "current_count_through_12": len(selected),
        "missing_words": missing,
        "extra_words": extra,
        "maximum_relative_multiplier_difference": mp.nstr(maximum_relative, 30),
        "word_set_match": not missing and not extra,
        "rows": discrepancies,
    }


def nearest_real_root(section: CycleSection, left: float = -1.0, right: float = 1.0) -> list[float]:
    from scipy.optimize import brentq

    grid = np.linspace(left, right, 8001)
    values = section.evaluate_many(grid.astype(np.complex128)).real
    roots: list[float] = []
    for x_left, x_right, y_left, y_right in zip(
        grid[:-1], grid[1:], values[:-1], values[1:], strict=True
    ):
        if y_left == 0:
            roots.append(float(x_left))
        elif y_left * y_right < 0:
            scalar_left = section.evaluate(complex(x_left)).real
            scalar_right = section.evaluate(complex(x_right)).real
            if not np.isfinite(scalar_left) or not np.isfinite(scalar_right):
                continue
            if scalar_left * scalar_right >= 0:
                # At large negative real part, high-order cycle sections can
                # suffer severe float64 cancellation. The vector scan is only
                # a bracket proposal; reject it if scalar reevaluation does
                # not reproduce the sign change.
                continue
            try:
                root = brentq(
                    lambda value: section.evaluate(complex(value)).real,
                    x_left,
                    x_right,
                )
            except ValueError:
                continue
            if all(abs(root - previous) > 1e-9 for previous in roots):
                roots.append(float(root))
    return roots


def complex_pair(value: complex) -> list[float]:
    return [float(value.real), float(value.imag)]


def roots_from_pairs(rows: Sequence[Sequence[float]]) -> list[complex]:
    return [complex(float(row[0]), float(row[1])) for row in rows]


def log_derivative_prime_power_term(
    orbit: WeightedOrbit,
    repetition: int,
    spectral_value: complex,
    kappa: int,
) -> complex:
    if repetition < 1:
        raise ValueError("repetition must be positive")
    return (
        orbit.length
        * (orbit.orientation ** (kappa * repetition))
        * np.exp(-repetition * spectral_value * orbit.length)
    )


def pressure_root_constant_roof(fixed_length: float) -> float:
    """Exact parent pressure h=log(phi)/c for roof c per map step."""

    golden_ratio = (1 + np.sqrt(5.0)) / 2
    return float(log(golden_ratio) / fixed_length)
