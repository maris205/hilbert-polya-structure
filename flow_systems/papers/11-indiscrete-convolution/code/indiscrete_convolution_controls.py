#!/usr/bin/env python3
"""Deterministic finite controls for Paper 11 indiscrete convolution.

The module builds exact finite analogues of an indiscrete unit space crossed
with a finite cyclic time group.  It checks topology, T0 and measurable
factorization, support projection, convolution, involution, convention
negatives, unit regular matrices, the Hausdorff-open diagnostic, proxy
strictness, action blindness, and independent label/period controls.

These controls are finite regression and falsification witnesses only.  They
do not prove a ``P11-*`` theorem or define a standard groupoid C*-algebra.
Only the Python standard library is used.  There is no network access,
randomness, external dataset, target-zero table, fitting, or timestamp.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import itertools
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable, Sequence


SCHEMA = "paper11-indiscrete-convolution-controls/1"
MANIFEST_FILENAME = "indiscrete_convolution_controls_manifest.json"

EXPECTED_ACTIVE_LOCK_HASHES = {
    "notes/candidate_lock.md": (
        "a97e9c30bca6bf9cee3e5543b5d83b72ab7291e5485fa9604811dfa3ce4c8012"
    ),
    "notes/phase1_design_amendment.md": (
        "e3124bddd6fb9bd9661c6104137086f87ca1a6e2b4fbae212a65b40304aa9572"
    ),
    "notes/phase1_final_gate.md": (
        "ac26f72f9ff1c5eb935903c20518a43aa043feb8d1572a920bfad471ca47d85f"
    ),
    "notes/pipeline_state.md": (
        "317ab9e8b3082b2d8bc75590618a6e86ca742bb8c23a899c3b612ea6304125e6"
    ),
    "notes/research_protocol.md": (
        "27c0ffd9c233301528e36f401e9cdf3f4030d65cea8002aafcf6fb97e557f860"
    ),
}

EXPECTED_PHASE_GATE_HASHES = {
    "notes/phase2_final_review.md": (
        "9607ec7eab0a947bf7de14d2c8a4233185c4e94994e19821d16b3f41b7c2638d"
    ),
}

IMPLEMENTATION_RELATIVE_PATHS = (
    "code/indiscrete_convolution_controls.py",
    "code/test_indiscrete_convolution_controls.py",
    "code/README.md",
    "experiments/reproduce.sh",
    "experiments/README.md",
    "results/README.md",
)

ARTIFACT_FILENAMES = (
    "arrow_topology_controls.csv",
    "t0_time_factorization_controls.csv",
    "measurable_time_factorization_controls.csv",
    "support_projection_controls.csv",
    "convolution_controls.csv",
    "involution_controls.csv",
    "convention_negative_controls.csv",
    "unit_regular_controls.csv",
    "hopen_zero_controls.csv",
    "proxy_strictness_controls.csv",
    "action_blind_controls.csv",
    "label_period_independence_controls.csv",
)

TOPOLOGY_MODELS = ((2, 3), (2, 4), (3, 3), (3, 4), (4, 3), (4, 4))
FACTORIZATION_MODELS = ((2, 2), (2, 3))
SUPPORT_MODELS = ((2, 3), (3, 4), (4, 4))
PROXY_MODELS = TOPOLOGY_MODELS
LABEL_PERIODS = (3, 4, 6)


Gaussian = tuple[int, int]
Arrow = tuple[int, int]


def sha256(path: Path) -> str:
    """Return the SHA-256 digest of one file."""

    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def text_sha256(text: str) -> str:
    """Return a stable SHA-256 digest for UTF-8 text."""

    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def bool_text(value: bool) -> str:
    """Encode booleans consistently in CSV outputs."""

    return "true" if value else "false"


def powerset(values: Sequence[int]) -> tuple[frozenset[int], ...]:
    """Return a finite powerset in cardinality/lexicographic order."""

    materialized = tuple(values)
    return tuple(
        frozenset(selection)
        for size in range(len(materialized) + 1)
        for selection in itertools.combinations(materialized, size)
    )


def encode_int_set(values: Iterable[int]) -> str:
    """Encode a finite integer set deterministically."""

    return "{" + ",".join(str(value) for value in sorted(values)) + "}"


def encode_arrows(values: Iterable[Arrow]) -> str:
    """Encode a finite arrow subset deterministically."""

    return "{" + ",".join(
        f"{x}@{t}" for x, t in sorted(values, key=lambda item: (item[1], item[0]))
    ) + "}"


def encode_mapping(values: Sequence[int]) -> str:
    """Encode a finite mapping in the module's fixed arrow order."""

    return ",".join(str(value) for value in values)


def gaussian_add(left: Gaussian, right: Gaussian) -> Gaussian:
    return (left[0] + right[0], left[1] + right[1])


def gaussian_mul(left: Gaussian, right: Gaussian) -> Gaussian:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def gaussian_conj(value: Gaussian) -> Gaussian:
    return (value[0], -value[1])


def gaussian_sum(values: Iterable[Gaussian]) -> Gaussian:
    total = (0, 0)
    for value in values:
        total = gaussian_add(total, value)
    return total


def encode_gaussian(value: Gaussian) -> str:
    real, imag = value
    sign = "+" if imag >= 0 else "-"
    return f"{real}{sign}{abs(imag)}i"


def encode_gaussian_vector(values: Sequence[Gaussian]) -> str:
    return "|".join(encode_gaussian(value) for value in values)


def encode_gaussian_matrix(rows: Sequence[Sequence[Gaussian]]) -> str:
    return ";".join(encode_gaussian_vector(row) for row in rows)


@dataclass(frozen=True)
class FiniteAction:
    """A right action of a finite cyclic group through one permutation."""

    name: str
    unit_size: int
    period: int
    generator: tuple[int, ...]

    def __post_init__(self) -> None:
        if self.unit_size < 1 or self.period < 1:
            raise ValueError("finite action sizes must be positive")
        if tuple(sorted(self.generator)) != tuple(range(self.unit_size)):
            raise ValueError(f"{self.name}: generator is not a permutation")
        for x in range(self.unit_size):
            if self.act(x, self.period) != x:
                raise ValueError(f"{self.name}: generator order does not divide period")

    def act(self, x: int, time: int) -> int:
        """Return ``x dot time`` for the cyclic right action."""

        if not 0 <= x < self.unit_size:
            raise ValueError("unit outside action")
        result = x
        for _ in range(time % self.period):
            result = self.generator[result]
        return result

    def orbit_partition(self) -> tuple[tuple[int, ...], ...]:
        remaining = set(range(self.unit_size))
        orbits: list[tuple[int, ...]] = []
        while remaining:
            start = min(remaining)
            orbit = tuple(sorted({self.act(start, t) for t in range(self.period)}))
            orbits.append(orbit)
            remaining.difference_update(orbit)
        return tuple(orbits)

    def stabilizer_sizes(self) -> tuple[int, ...]:
        return tuple(
            sum(self.act(x, t) == x for t in range(self.period))
            for x in range(self.unit_size)
        )


ACTION_MODELS = (
    FiniteAction("trivial", 4, 4, (0, 1, 2, 3)),
    FiniteAction("transitive", 4, 4, (1, 2, 3, 0)),
    FiniteAction("nontransitive", 4, 4, (1, 0, 3, 2)),
)


def arrow_points(unit_size: int, period: int) -> tuple[Arrow, ...]:
    """Return arrows in time-major, then unit-major order."""

    return tuple((x, t) for t in range(period) for x in range(unit_size))


def arrow_topology_indices(
    unit_size: int, period: int
) -> tuple[frozenset[int], ...]:
    """Return the topology of indiscrete ``X`` times discrete ``C_period``."""

    return tuple(
        frozenset(
            t * unit_size + x
            for t in time_subset
            for x in range(unit_size)
        )
        for time_subset in powerset(tuple(range(period)))
    )


def inverse_image(mapping: Sequence[int], target_open: frozenset[int]) -> frozenset[int]:
    return frozenset(
        index for index, value in enumerate(mapping) if value in target_open
    )


def is_continuous_mapping(
    mapping: Sequence[int],
    source_topology: Sequence[frozenset[int]],
    target_topology: Sequence[frozenset[int]],
) -> bool:
    source_opens = set(source_topology)
    return all(inverse_image(mapping, opened) in source_opens for opened in target_topology)


def is_measurable_mapping(
    mapping: Sequence[int],
    source_sigma: Sequence[frozenset[int]],
    target_sigma: Sequence[frozenset[int]],
) -> bool:
    source_events = set(source_sigma)
    return all(inverse_image(mapping, event) in source_events for event in target_sigma)


def is_t0_space(size: int, topology: Sequence[frozenset[int]]) -> bool:
    for left in range(size):
        for right in range(left + 1, size):
            if not any((left in opened) != (right in opened) for opened in topology):
                return False
    return True


def is_hausdorff_subspace(
    subset: frozenset[int], topology: Sequence[frozenset[int]]
) -> bool:
    subspace_opens = tuple(frozenset(opened & subset) for opened in topology)
    for left in sorted(subset):
        for right in sorted(subset):
            if left >= right:
                continue
            separated = any(
                left in left_open
                and right in right_open
                and not left_open.intersection(right_open)
                for left_open in subspace_opens
                for right_open in subspace_opens
            )
            if not separated:
                return False
    return True


def closure_indices(
    subset: frozenset[int],
    topology: Sequence[frozenset[int]],
    universe: frozenset[int],
) -> frozenset[int]:
    closed_sets = tuple(universe.difference(opened) for opened in topology)
    supersets = tuple(closed for closed in closed_sets if subset <= closed)
    if not supersets:
        raise ValueError("finite topology has no closed superset")
    result = universe
    for closed in supersets:
        result = frozenset(result.intersection(closed))
    return result


def factors_through_time(
    mapping: Sequence[int], unit_size: int, period: int
) -> tuple[bool, tuple[int, ...]]:
    factor: list[int] = []
    for time in range(period):
        values = {
            mapping[time * unit_size + x]
            for x in range(unit_size)
        }
        if len(values) != 1:
            return False, ()
        factor.append(next(iter(values)))
    return True, tuple(factor)


def support_profiles(period: int) -> tuple[tuple[str, tuple[int, ...]], ...]:
    profiles = (
        ("empty", tuple(0 for _ in range(period))),
        ("time_zero", tuple(1 if t == 0 else 0 for t in range(period))),
        ("two_times", tuple(1 if t in {0, period - 1} else 0 for t in range(period))),
        ("alternating_full", tuple(1 if t % 2 == 0 else -1 for t in range(period))),
        ("middle_signed", tuple((t - 1) if t in {1, 2} else 0 for t in range(period))),
    )
    return profiles


def gaussian_profile(name: str, period: int) -> tuple[Gaussian, ...]:
    if name == "delta_zero":
        return tuple((1, 0) if t == 0 else (0, 0) for t in range(period))
    if name == "delta_shift":
        return tuple((1, 0) if t == 1 % period else (0, 0) for t in range(period))
    if name == "dense_a":
        return tuple((t + 1, (t % 3) - 1) for t in range(period))
    if name == "dense_b":
        return tuple((1 if t % 2 == 0 else -1, 2 - t) for t in range(period))
    if name == "sparse_signed":
        return tuple(
            (2, 1) if t == 0 else ((-1, 2) if t == period - 1 else (0, 0))
            for t in range(period)
        )
    raise ValueError(f"unknown Gaussian profile: {name}")


CONVOLUTION_PROFILE_PAIRS = (
    ("delta_shift", "delta_zero"),
    ("dense_a", "dense_b"),
    ("sparse_signed", "dense_b"),
)
INVOLUTION_PROFILES = ("delta_shift", "dense_a", "sparse_signed")
REGULAR_PROFILES = ("delta_shift", "dense_a", "sparse_signed")


def phi_value(values: Sequence[Gaussian], _unit: int, time: int) -> Gaussian:
    return values[time % len(values)]


def group_convolution(
    left: Sequence[Gaussian], right: Sequence[Gaussian]
) -> tuple[Gaussian, ...]:
    if len(left) != len(right):
        raise ValueError("cyclic profiles must have equal periods")
    period = len(left)
    return tuple(
        gaussian_sum(
            gaussian_mul(left[u], right[(time - u) % period])
            for u in range(period)
        )
        for time in range(period)
    )


def actual_global_convolution(
    action: FiniteAction,
    left: Sequence[Gaussian],
    right: Sequence[Gaussian],
    unit: int,
    time: int,
) -> Gaussian:
    return gaussian_sum(
        gaussian_mul(
            phi_value(left, unit, u),
            phi_value(right, action.act(unit, u), time - u),
        )
        for u in range(action.period)
    )


def wrong_sign_global_convolution(
    action: FiniteAction,
    left: Sequence[Gaussian],
    right: Sequence[Gaussian],
    unit: int,
    time: int,
) -> Gaussian:
    return gaussian_sum(
        gaussian_mul(
            phi_value(left, unit, u),
            phi_value(right, action.act(unit, u), time + u),
        )
        for u in range(action.period)
    )


def group_involution(values: Sequence[Gaussian]) -> tuple[Gaussian, ...]:
    period = len(values)
    return tuple(gaussian_conj(values[-time % period]) for time in range(period))


def actual_global_involution(
    action: FiniteAction,
    values: Sequence[Gaussian],
    unit: int,
    time: int,
) -> Gaussian:
    return gaussian_conj(
        phi_value(values, action.act(unit, time), -time)
    )


def raw_probe_left(_unit: int, time: int, period: int) -> Gaussian:
    return (1, 0) if time % period == 1 % period else (0, 0)


def raw_probe_right(unit: int, time: int, period: int) -> Gaussian:
    return (unit + 1, 0) if time % period == 0 else (0, 0)


def raw_convolution(
    action: FiniteAction,
    unit: int,
    time: int,
    *,
    shift_unit: bool,
) -> Gaussian:
    terms: list[Gaussian] = []
    for u in range(action.period):
        right_unit = action.act(unit, u) if shift_unit else unit
        terms.append(
            gaussian_mul(
                raw_probe_left(unit, u, action.period),
                raw_probe_right(right_unit, time - u, action.period),
            )
        )
    return gaussian_sum(terms)


def arrow_source(action: FiniteAction, arrow: Arrow) -> int:
    return action.act(arrow[0], arrow[1])


def inverse_arrow(action: FiniteAction, arrow: Arrow) -> Arrow:
    return (arrow_source(action, arrow), (-arrow[1]) % action.period)


def multiply_arrows(action: FiniteAction, left: Arrow, right: Arrow) -> Arrow:
    if arrow_source(action, left) != right[0]:
        raise ValueError("arrows are not composable in range-first convention")
    return (left[0], (left[1] + right[1]) % action.period)


def source_fibre_arrow(action: FiniteAction, base_unit: int, time: int) -> Arrow:
    return (action.act(base_unit, -time), time % action.period)


def regular_matrix_actual(
    action: FiniteAction, values: Sequence[Gaussian], base_unit: int
) -> tuple[tuple[Gaussian, ...], ...]:
    rows: list[tuple[Gaussian, ...]] = []
    for time in range(action.period):
        gamma = source_fibre_arrow(action, base_unit, time)
        row: list[Gaussian] = []
        for u in range(action.period):
            eta = source_fibre_arrow(action, base_unit, u)
            product = multiply_arrows(action, gamma, inverse_arrow(action, eta))
            row.append(phi_value(values, product[0], product[1]))
        rows.append(tuple(row))
    return tuple(rows)


def regular_matrix_group(
    values: Sequence[Gaussian],
) -> tuple[tuple[Gaussian, ...], ...]:
    period = len(values)
    return tuple(
        tuple(values[(time - u) % period] for u in range(period))
        for time in range(period)
    )


def encode_partition(partition: Sequence[Sequence[int]]) -> str:
    return "|".join(encode_int_set(group) for group in partition)


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    for divisor in range(2, int(value**0.5) + 1):
        if value % divisor == 0:
            return False
    return True


def _arrow_topology_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for unit_size, period in TOPOLOGY_MODELS:
        points = arrow_points(unit_size, period)
        topology = arrow_topology_indices(unit_size, period)
        arrow_t0 = is_t0_space(len(points), topology)
        for time_subset in powerset(tuple(range(period))):
            indices = frozenset(
                time * unit_size + unit
                for time in time_subset
                for unit in range(unit_size)
            )
            arrow_subset = frozenset(points[index] for index in indices)
            hausdorff = is_hausdorff_subspace(indices, topology)
            expected = not indices
            rows.append(
                {
                    "unit_size": unit_size,
                    "period": period,
                    "time_subset": encode_int_set(time_subset),
                    "arrow_open": encode_arrows(arrow_subset),
                    "open_cardinality": len(indices),
                    "nonempty": bool_text(bool(indices)),
                    "hausdorff_subspace": bool_text(hausdorff),
                    "expected_hausdorff": bool_text(expected),
                    "expectation_match": bool_text(hausdorff == expected),
                    "topology_open_count": len(topology),
                    "arrow_t0": bool_text(arrow_t0),
                    "scope": "finite indiscrete-unit x discrete cyclic-time topology only",
                }
            )
    return rows


def _t0_factorization_rows() -> list[dict[str, object]]:
    targets = (
        ("discrete_2", powerset((0, 1)), True),
        ("sierpinski_2", (frozenset(), frozenset({1}), frozenset({0, 1})), True),
        ("indiscrete_2_negative", (frozenset(), frozenset({0, 1})), False),
    )
    rows: list[dict[str, object]] = []
    for unit_size, period in FACTORIZATION_MODELS:
        source_topology = arrow_topology_indices(unit_size, period)
        arrow_count = unit_size * period
        for target_name, target_topology, target_t0 in targets:
            for mapping in itertools.product((0, 1), repeat=arrow_count):
                continuous = is_continuous_mapping(
                    mapping, source_topology, target_topology
                )
                factors, factor = factors_through_time(mapping, unit_size, period)
                reconstruction = tuple(
                    factor[time] for time in range(period) for _ in range(unit_size)
                ) if factors else ()
                required_implication = (not continuous) or factors
                rows.append(
                    {
                        "unit_size": unit_size,
                        "period": period,
                        "target": target_name,
                        "target_t0": bool_text(target_t0),
                        "map_values": encode_mapping(mapping),
                        "continuous": bool_text(continuous),
                        "factors_through_time": bool_text(factors),
                        "factor_values": encode_mapping(factor) if factors else "",
                        "reconstruction_match": bool_text(
                            factors and reconstruction == tuple(mapping)
                        ),
                        "t0_implication_match": bool_text(
                            required_implication if target_t0 else True
                        ),
                        "negative_nonfactor_continuous": bool_text(
                            continuous and not factors and not target_t0
                        ),
                        "scope": "exhaustive finite T0 factorization control",
                    }
                )
    return rows


def _measurable_factorization_rows() -> list[dict[str, object]]:
    targets = (
        ("discrete_2", powerset((0, 1)), True),
        ("indiscrete_sigma_2_negative", (frozenset(), frozenset({0, 1})), False),
    )
    rows: list[dict[str, object]] = []
    for unit_size, period in FACTORIZATION_MODELS:
        source_sigma = arrow_topology_indices(unit_size, period)
        arrow_count = unit_size * period
        for target_name, target_sigma, countably_separated in targets:
            for mapping in itertools.product((0, 1), repeat=arrow_count):
                measurable = is_measurable_mapping(mapping, source_sigma, target_sigma)
                factors, factor = factors_through_time(mapping, unit_size, period)
                required_implication = (not measurable) or factors
                rows.append(
                    {
                        "unit_size": unit_size,
                        "period": period,
                        "source_sigma_cardinality": len(source_sigma),
                        "target": target_name,
                        "target_countably_separated": bool_text(countably_separated),
                        "map_values": encode_mapping(mapping),
                        "measurable": bool_text(measurable),
                        "factors_through_time": bool_text(factors),
                        "factor_values": encode_mapping(factor) if factors else "",
                        "separated_implication_match": bool_text(
                            required_implication if countably_separated else True
                        ),
                        "negative_nonfactor_measurable": bool_text(
                            measurable and not factors and not countably_separated
                        ),
                        "scope": "exhaustive finite countably-separated measurable control",
                    }
                )
    return rows


def _support_projection_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for unit_size, period in SUPPORT_MODELS:
        points = arrow_points(unit_size, period)
        topology = arrow_topology_indices(unit_size, period)
        universe = frozenset(range(len(points)))
        for profile_name, values in support_profiles(period):
            nonzero_times = frozenset(
                time for time, value in enumerate(values) if value != 0
            )
            nonzero_indices = frozenset(
                time * unit_size + unit
                for time in nonzero_times
                for unit in range(unit_size)
            )
            support = closure_indices(nonzero_indices, topology, universe)
            projected_times = frozenset(
                points[index][1] for index in support
            )
            expected_support = frozenset(
                time * unit_size + unit
                for time in nonzero_times
                for unit in range(unit_size)
            )
            rows.append(
                {
                    "unit_size": unit_size,
                    "period": period,
                    "profile": profile_name,
                    "time_values": ",".join(str(value) for value in values),
                    "nonzero_time_projection": encode_int_set(nonzero_times),
                    "ambient_support": encode_arrows(points[index] for index in support),
                    "support_time_projection": encode_int_set(projected_times),
                    "support_equals_x_times_projection": bool_text(
                        support == expected_support
                    ),
                    "projection_matches_group_support": bool_text(
                        projected_times == nonzero_times
                    ),
                    "finite_quasi_compact": "true",
                    "scope": "finite ambient-closure and support-projection witness",
                }
            )
    return rows


def _convolution_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for action in ACTION_MODELS:
        for left_name, right_name in CONVOLUTION_PROFILE_PAIRS:
            left = gaussian_profile(left_name, action.period)
            right = gaussian_profile(right_name, action.period)
            group_values = group_convolution(left, right)
            for time in range(action.period):
                actual_by_unit = tuple(
                    actual_global_convolution(action, left, right, unit, time)
                    for unit in range(action.unit_size)
                )
                rows.append(
                    {
                        "action": action.name,
                        "unit_size": action.unit_size,
                        "period": action.period,
                        "orbit_count": len(action.orbit_partition()),
                        "left_profile": left_name,
                        "right_profile": right_name,
                        "time": time,
                        "group_convolution": encode_gaussian(group_values[time]),
                        "actual_values_by_unit": encode_gaussian_vector(actual_by_unit),
                        "all_units_match_group": bool_text(
                            all(value == group_values[time] for value in actual_by_unit)
                        ),
                        "unit_coordinate_erased": bool_text(
                            len(set(actual_by_unit)) == 1
                        ),
                        "scope": "finite counting-measure convolution witness",
                    }
                )
    return rows


def _involution_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for action in ACTION_MODELS:
        for profile_name in INVOLUTION_PROFILES:
            values = gaussian_profile(profile_name, action.period)
            group_values = group_involution(values)
            for time in range(action.period):
                actual_by_unit = tuple(
                    actual_global_involution(action, values, unit, time)
                    for unit in range(action.unit_size)
                )
                rows.append(
                    {
                        "action": action.name,
                        "unit_size": action.unit_size,
                        "period": action.period,
                        "profile": profile_name,
                        "time": time,
                        "group_involution": encode_gaussian(group_values[time]),
                        "actual_values_by_unit": encode_gaussian_vector(actual_by_unit),
                        "all_units_match_group": bool_text(
                            all(value == group_values[time] for value in actual_by_unit)
                        ),
                        "unit_coordinate_erased": bool_text(
                            len(set(actual_by_unit)) == 1
                        ),
                        "scope": "finite right-action involution witness",
                    }
                )
    return rows


def _convention_negative_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for action in ACTION_MODELS:
        left = gaussian_profile("delta_shift", action.period)
        right = gaussian_profile("delta_zero", action.period)
        mismatches: list[tuple[int, int, Gaussian, Gaussian]] = []
        for unit in range(action.unit_size):
            for time in range(action.period):
                correct = actual_global_convolution(action, left, right, unit, time)
                wrong = wrong_sign_global_convolution(action, left, right, unit, time)
                if correct != wrong:
                    mismatches.append((unit, time, correct, wrong))
        witness = mismatches[0]
        rows.append(
            {
                "action": action.name,
                "negative_kind": "wrong_time_sign_t_plus_u",
                "probe_domain": "licensed_global_profiles",
                "mismatch_count": len(mismatches),
                "witness_unit": witness[0],
                "witness_time": witness[1],
                "correct_value": encode_gaussian(witness[2]),
                "wrong_value": encode_gaussian(witness[3]),
                "negative_detected": "true",
                "scope": "intentional sign error must fail",
            }
        )

    for action in ACTION_MODELS:
        if action.name == "trivial":
            continue
        mismatches = []
        for unit in range(action.unit_size):
            for time in range(action.period):
                correct = raw_convolution(action, unit, time, shift_unit=True)
                wrong = raw_convolution(action, unit, time, shift_unit=False)
                if correct != wrong:
                    mismatches.append((unit, time, correct, wrong))
        witness = mismatches[0]
        rows.append(
            {
                "action": action.name,
                "negative_kind": "wrong_source_range_no_unit_shift",
                "probe_domain": "raw_x_dependent_probe_outside_global_algebra",
                "mismatch_count": len(mismatches),
                "witness_unit": witness[0],
                "witness_time": witness[1],
                "correct_value": encode_gaussian(witness[2]),
                "wrong_value": encode_gaussian(witness[3]),
                "negative_detected": "true",
                "scope": "raw probe detects convention only; no licensed-domain claim",
            }
        )
    return rows


def _unit_regular_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for action in ACTION_MODELS:
        for profile_name in REGULAR_PROFILES:
            values = gaussian_profile(profile_name, action.period)
            group_matrix = regular_matrix_group(values)
            group_encoding = encode_gaussian_matrix(group_matrix)
            for base_unit in range(action.unit_size):
                actual_matrix = regular_matrix_actual(action, values, base_unit)
                actual_encoding = encode_gaussian_matrix(actual_matrix)
                rows.append(
                    {
                        "action": action.name,
                        "unit_size": action.unit_size,
                        "period": action.period,
                        "profile": profile_name,
                        "base_unit": base_unit,
                        "source_fibre_parameterization": "vartheta_x(t)=(x dot (-t),t)",
                        "actual_matrix": actual_encoding,
                        "group_left_regular_matrix": group_encoding,
                        "matrix_sha256": text_sha256(actual_encoding),
                        "matches_group_matrix": bool_text(actual_matrix == group_matrix),
                        "scope": "finite counting-measure regular-matrix witness",
                    }
                )
    return rows


def _hopen_zero_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for unit_size, period in TOPOLOGY_MODELS:
        topology = arrow_topology_indices(unit_size, period)
        nonempty_hausdorff = [
            opened
            for opened in topology
            if opened and is_hausdorff_subspace(opened, topology)
        ]
        rows.append(
            {
                "unit_size": unit_size,
                "period": period,
                "open_count": len(topology),
                "nonempty_open_count": len(topology) - 1,
                "nonempty_hausdorff_open_count": len(nonempty_hausdorff),
                "legal_patch_generator_count": len(nonempty_hausdorff),
                "hopen_span_dimension": 0 if not nonempty_hausdorff else "uncomputed",
                "hopen_span_zero": bool_text(not nonempty_hausdorff),
                "framework_credit": "diagnostic_only",
                "scope": "finite HOpen analogue; not a standard groupoid completion",
            }
        )
    return rows


def _proxy_strictness_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for unit_size, period in PROXY_MODELS:
        arrow_count = unit_size * period
        witness = tuple(
            1 if index == 0 else 0 for index in range(arrow_count)
        )
        factors, _ = factors_through_time(witness, unit_size, period)
        rows.append(
            {
                "unit_size": unit_size,
                "period": period,
                "actual_arrow_topology": "indiscrete_unit_x_discrete_time",
                "proxy_arrow_topology": "fully_discrete",
                "actual_to_proxy_identity_continuous": bool_text(unit_size == 1),
                "proxy_to_actual_identity_continuous": "true",
                "actual_global_dimension": period,
                "proxy_function_dimension": arrow_count,
                "dimension_gap": arrow_count - period,
                "witness_proxy_delta": encode_mapping(witness),
                "witness_proxy_continuous": "true",
                "witness_actual_continuous": bool_text(factors),
                "strict_extra_proxy_function": bool_text(not factors),
                "scope": "finite discrete proxy is a separate finer modeling choice",
            }
        )
    return rows


def _action_blind_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    left = gaussian_profile("dense_a", 4)
    right = gaussian_profile("dense_b", 4)
    group_conv_encoding = encode_gaussian_vector(group_convolution(left, right))
    regular_encoding = encode_gaussian_matrix(regular_matrix_group(left))
    signature = text_sha256(
        f"C_4|dim=4|conv={group_conv_encoding}|regular={regular_encoding}"
    )
    for action in ACTION_MODELS:
        rows.append(
            {
                "action": action.name,
                "generator": encode_mapping(action.generator),
                "orbit_partition": encode_partition(action.orbit_partition()),
                "orbit_count": len(action.orbit_partition()),
                "stabilizer_sizes": encode_mapping(action.stabilizer_sizes()),
                "global_function_dimension": action.period,
                "global_convolution_sha256": text_sha256(group_conv_encoding),
                "regular_matrix_sha256": text_sha256(regular_encoding),
                "global_signature": signature,
                "action_visible_in_global_signature": "false",
                "scope": "finite action-blindness control, not arithmetic credit",
            }
        )
    return rows


def _label_period_rows() -> list[dict[str, object]]:
    label_families = (
        ("prime", ("2", "3", "5")),
        ("composite", ("4", "6", "8")),
        ("arbitrary", ("alpha", "clock-q", "label_17")),
    )
    rows: list[dict[str, object]] = []
    for family, labels in label_families:
        for label in labels:
            numeric = int(label) if label.isdigit() else None
            if family == "prime" and not is_prime(int(label)):
                raise ValueError("prime control label is not prime")
            if family == "composite" and (
                is_prime(int(label)) or int(label) < 4
            ):
                raise ValueError("composite control label is not composite")
            for period in LABEL_PERIODS:
                profile = gaussian_profile("dense_a", period)
                signature = text_sha256(
                    f"C_{period}|dim={period}|regular="
                    f"{encode_gaussian_matrix(regular_matrix_group(profile))}"
                )
                rows.append(
                    {
                        "label_family": family,
                        "label": label,
                        "numeric_label": "" if numeric is None else numeric,
                        "period": period,
                        "label_period_pair": f"{label}@{period}",
                        "period_varied_independently": "true",
                        "label_determines_period": "false",
                        "global_dimension": period,
                        "period_signature": signature,
                        "structure_depends_on_label": "false",
                        "arithmetic_credit": "false",
                        "scope": "prime/composite/arbitrary label-period cross-control",
                    }
                )
    return rows


def write_csv(
    path: Path, fieldnames: Sequence[str], rows: Sequence[dict[str, object]]
) -> int:
    """Write a deterministic UTF-8 CSV and return its body-row count."""

    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=fieldnames,
            extrasaction="raise",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)


def _artifact_specs() -> tuple[
    tuple[str, Sequence[str], Callable[[], list[dict[str, object]]]], ...
]:
    return (
        (
            "arrow_topology_controls.csv",
            (
                "unit_size", "period", "time_subset", "arrow_open",
                "open_cardinality", "nonempty", "hausdorff_subspace",
                "expected_hausdorff", "expectation_match",
                "topology_open_count", "arrow_t0", "scope",
            ),
            _arrow_topology_rows,
        ),
        (
            "t0_time_factorization_controls.csv",
            (
                "unit_size", "period", "target", "target_t0", "map_values",
                "continuous", "factors_through_time", "factor_values",
                "reconstruction_match", "t0_implication_match",
                "negative_nonfactor_continuous", "scope",
            ),
            _t0_factorization_rows,
        ),
        (
            "measurable_time_factorization_controls.csv",
            (
                "unit_size", "period", "source_sigma_cardinality", "target",
                "target_countably_separated", "map_values", "measurable",
                "factors_through_time", "factor_values",
                "separated_implication_match", "negative_nonfactor_measurable",
                "scope",
            ),
            _measurable_factorization_rows,
        ),
        (
            "support_projection_controls.csv",
            (
                "unit_size", "period", "profile", "time_values",
                "nonzero_time_projection", "ambient_support",
                "support_time_projection", "support_equals_x_times_projection",
                "projection_matches_group_support", "finite_quasi_compact", "scope",
            ),
            _support_projection_rows,
        ),
        (
            "convolution_controls.csv",
            (
                "action", "unit_size", "period", "orbit_count", "left_profile",
                "right_profile", "time", "group_convolution",
                "actual_values_by_unit", "all_units_match_group",
                "unit_coordinate_erased", "scope",
            ),
            _convolution_rows,
        ),
        (
            "involution_controls.csv",
            (
                "action", "unit_size", "period", "profile", "time",
                "group_involution", "actual_values_by_unit",
                "all_units_match_group", "unit_coordinate_erased", "scope",
            ),
            _involution_rows,
        ),
        (
            "convention_negative_controls.csv",
            (
                "action", "negative_kind", "probe_domain", "mismatch_count",
                "witness_unit", "witness_time", "correct_value", "wrong_value",
                "negative_detected", "scope",
            ),
            _convention_negative_rows,
        ),
        (
            "unit_regular_controls.csv",
            (
                "action", "unit_size", "period", "profile", "base_unit",
                "source_fibre_parameterization", "actual_matrix",
                "group_left_regular_matrix", "matrix_sha256",
                "matches_group_matrix", "scope",
            ),
            _unit_regular_rows,
        ),
        (
            "hopen_zero_controls.csv",
            (
                "unit_size", "period", "open_count", "nonempty_open_count",
                "nonempty_hausdorff_open_count", "legal_patch_generator_count",
                "hopen_span_dimension", "hopen_span_zero", "framework_credit", "scope",
            ),
            _hopen_zero_rows,
        ),
        (
            "proxy_strictness_controls.csv",
            (
                "unit_size", "period", "actual_arrow_topology",
                "proxy_arrow_topology", "actual_to_proxy_identity_continuous",
                "proxy_to_actual_identity_continuous", "actual_global_dimension",
                "proxy_function_dimension", "dimension_gap", "witness_proxy_delta",
                "witness_proxy_continuous", "witness_actual_continuous",
                "strict_extra_proxy_function", "scope",
            ),
            _proxy_strictness_rows,
        ),
        (
            "action_blind_controls.csv",
            (
                "action", "generator", "orbit_partition", "orbit_count",
                "stabilizer_sizes", "global_function_dimension",
                "global_convolution_sha256", "regular_matrix_sha256",
                "global_signature", "action_visible_in_global_signature", "scope",
            ),
            _action_blind_rows,
        ),
        (
            "label_period_independence_controls.csv",
            (
                "label_family", "label", "numeric_label", "period",
                "label_period_pair", "period_varied_independently",
                "label_determines_period", "global_dimension", "period_signature",
                "structure_depends_on_label", "arithmetic_credit", "scope",
            ),
            _label_period_rows,
        ),
    )


def _hash_bound_files(
    paper_dir: Path, expected: dict[str, str], label: str
) -> dict[str, str]:
    observed: dict[str, str] = {}
    for relative, expected_hash in expected.items():
        path = paper_dir / relative
        if not path.is_file():
            raise FileNotFoundError(f"missing {label} file: {relative}")
        observed[relative] = sha256(path)
        if observed[relative] != expected_hash:
            raise ValueError(
                f"{label} SHA-256 mismatch: {relative}: "
                f"expected {expected_hash}, observed {observed[relative]}"
            )
    return observed


def _implementation_hashes(paper_dir: Path) -> dict[str, str]:
    hashes: dict[str, str] = {}
    for relative in IMPLEMENTATION_RELATIVE_PATHS:
        path = paper_dir / relative
        if not path.is_file():
            raise FileNotFoundError(f"missing implementation file: {relative}")
        hashes[relative] = sha256(path)
    return hashes


def _check_output_names(
    output_dir: Path, paper_dir: Path, *, require_all: bool
) -> None:
    generated = set(ARTIFACT_FILENAMES) | {MANIFEST_FILENAME}
    observed = {entry.name for entry in output_dir.iterdir()}
    allowed_static = (
        {"README.md"}
        if output_dir == (paper_dir / "results").resolve()
        else set()
    )
    unexpected = observed - generated - allowed_static
    missing = generated - observed if require_all else set()
    nonfiles = {
        entry.name
        for entry in output_dir.iterdir()
        if entry.name in generated and not entry.is_file()
    }
    if missing or unexpected or nonfiles:
        raise ValueError(
            "output artifact set mismatch: "
            f"missing={sorted(missing)}, extra={sorted(unexpected)}, "
            f"nonfiles={sorted(nonfiles)}"
        )


def _build_manifest(
    output_dir: Path,
    row_counts: dict[str, int],
    paper_dir: Path,
) -> dict[str, object]:
    artifacts = {
        filename: {
            "bytes": (output_dir / filename).stat().st_size,
            "rows": row_counts[filename],
            "sha256": sha256(output_dir / filename),
        }
        for filename in ARTIFACT_FILENAMES
    }

    topology_rows = _arrow_topology_rows()
    t0_rows = _t0_factorization_rows()
    measurable_rows = _measurable_factorization_rows()
    support_rows = _support_projection_rows()
    convolution_rows = _convolution_rows()
    involution_rows = _involution_rows()
    negative_rows = _convention_negative_rows()
    regular_rows = _unit_regular_rows()
    hopen_rows = _hopen_zero_rows()
    proxy_rows = _proxy_strictness_rows()
    action_rows = _action_blind_rows()
    label_rows = _label_period_rows()

    return {
        "schema": SCHEMA,
        "regression_status": "PASS",
        "active_lock_files": _hash_bound_files(
            paper_dir, EXPECTED_ACTIVE_LOCK_HASHES, "active lock"
        ),
        "phase_gate_files": _hash_bound_files(
            paper_dir, EXPECTED_PHASE_GATE_HASHES, "Phase-2 gate"
        ),
        "implementation_files": _implementation_hashes(paper_dir),
        "artifacts": artifacts,
        "parameters": {
            "topology_models": [list(model) for model in TOPOLOGY_MODELS],
            "factorization_models": [list(model) for model in FACTORIZATION_MODELS],
            "support_models": [list(model) for model in SUPPORT_MODELS],
            "action_models": [action.name for action in ACTION_MODELS],
            "label_periods": list(LABEL_PERIODS),
            "convolution_profile_pairs": [
                list(pair) for pair in CONVOLUTION_PROFILE_PAIRS
            ],
        },
        "metrics": {
            "csv_artifact_count": len(ARTIFACT_FILENAMES),
            "total_csv_rows": sum(row_counts.values()),
            "all_topology_expectations_match": all(
                row["expectation_match"] == "true" for row in topology_rows
            ),
            "nonempty_hausdorff_open_count": sum(
                row["nonempty"] == "true"
                and row["hausdorff_subspace"] == "true"
                for row in topology_rows
            ),
            "t0_continuous_nonfactor_count": sum(
                row["target_t0"] == "true"
                and row["continuous"] == "true"
                and row["factors_through_time"] == "false"
                for row in t0_rows
            ),
            "nont0_continuous_nonfactor_negative_count": sum(
                row["negative_nonfactor_continuous"] == "true" for row in t0_rows
            ),
            "separated_measurable_nonfactor_count": sum(
                row["target_countably_separated"] == "true"
                and row["measurable"] == "true"
                and row["factors_through_time"] == "false"
                for row in measurable_rows
            ),
            "nonseparated_measurable_nonfactor_negative_count": sum(
                row["negative_nonfactor_measurable"] == "true"
                for row in measurable_rows
            ),
            "all_support_projection_checks_pass": all(
                row["support_equals_x_times_projection"] == "true"
                and row["projection_matches_group_support"] == "true"
                for row in support_rows
            ),
            "all_convolution_rows_match_group": all(
                row["all_units_match_group"] == "true" for row in convolution_rows
            ),
            "all_involution_rows_match_group": all(
                row["all_units_match_group"] == "true" for row in involution_rows
            ),
            "all_negative_controls_detected": all(
                row["negative_detected"] == "true" for row in negative_rows
            ),
            "negative_control_count": len(negative_rows),
            "all_regular_matrices_match_group": all(
                row["matches_group_matrix"] == "true" for row in regular_rows
            ),
            "all_hopen_spans_zero": all(
                row["hopen_span_zero"] == "true" for row in hopen_rows
            ),
            "all_proxy_models_strict": all(
                row["strict_extra_proxy_function"] == "true" for row in proxy_rows
            ),
            "action_orbit_counts": {
                row["action"]: row["orbit_count"] for row in action_rows
            },
            "distinct_global_action_signatures": len(
                {row["global_signature"] for row in action_rows}
            ),
            "label_family_count": len({row["label_family"] for row in label_rows}),
            "label_period_pair_count": len(label_rows),
            "all_labels_cross_all_periods": all(
                {
                    int(row["period"])
                    for row in label_rows
                    if row["label"] == label
                }
                == set(LABEL_PERIODS)
                for label in {row["label"] for row in label_rows}
            ),
        },
        "determinism": {
            "python_dependencies": "standard_library_only",
            "network": False,
            "randomness": False,
            "external_datasets": False,
            "target_zero_data": False,
            "fitting": False,
            "timestamps": False,
            "arithmetic_labels_are_controls_only": True,
        },
        "object_boundary": (
            "Finite indiscrete-unit/cyclic-time transformation groupoids, "
            "finite T0 or measurable targets, raw convention probes, and the "
            "fully discrete proxy are separately typed controls. No proxy or "
            "raw-probe result is promoted to the actual rational-Witt owner."
        ),
        "interpretation_boundary": (
            "These finite exact controls are witnesses, not proofs of P11-1--"
            "P11-10, infinite or continuous convolution, a published Haar "
            "system, a standard actual-groupoid completion, arithmetic "
            "relevance, a Route verdict, or a standalone-paper claim."
        ),
        "forbidden_evidence_not_used": [
            "Riemann-zero tables or target-zero values",
            "target fitting or fitted parameters",
            "network or external package data",
            "random or stochastic search",
        ],
    }


def run(output_dir: Path, paper_dir: Path | None = None) -> dict[str, object]:
    """Generate all CSV artifacts and the hash-bound manifest."""

    output_dir = output_dir.resolve()
    paper_dir = (
        Path(__file__).resolve().parents[1]
        if paper_dir is None
        else paper_dir.resolve()
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    _check_output_names(output_dir, paper_dir, require_all=False)

    row_counts: dict[str, int] = {}
    for filename, fieldnames, row_factory in _artifact_specs():
        row_counts[filename] = write_csv(
            output_dir / filename, fieldnames, row_factory()
        )
    manifest = _build_manifest(output_dir, row_counts, paper_dir)
    (output_dir / MANIFEST_FILENAME).write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    _check_output_names(output_dir, paper_dir, require_all=True)
    return manifest


def verify(output_dir: Path, paper_dir: Path | None = None) -> dict[str, object]:
    """Strictly verify bytes, rows, locks, implementation, metrics, and names."""

    output_dir = output_dir.resolve()
    paper_dir = (
        Path(__file__).resolve().parents[1]
        if paper_dir is None
        else paper_dir.resolve()
    )
    if not output_dir.is_dir():
        raise FileNotFoundError(f"missing output directory: {output_dir}")
    _check_output_names(output_dir, paper_dir, require_all=True)

    manifest_path = output_dir / MANIFEST_FILENAME
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("schema") != SCHEMA:
        raise ValueError("manifest schema mismatch")
    if manifest.get("regression_status") != "PASS":
        raise ValueError("manifest regression status is not PASS")

    active_locks = _hash_bound_files(
        paper_dir, EXPECTED_ACTIVE_LOCK_HASHES, "active lock"
    )
    if manifest.get("active_lock_files") != active_locks:
        raise ValueError("manifest active-lock ledger mismatch")
    phase_gates = _hash_bound_files(
        paper_dir, EXPECTED_PHASE_GATE_HASHES, "Phase-2 gate"
    )
    if manifest.get("phase_gate_files") != phase_gates:
        raise ValueError("manifest Phase-2 gate ledger mismatch")
    implementation = _implementation_hashes(paper_dir)
    if manifest.get("implementation_files") != implementation:
        raise ValueError("implementation SHA-256 mismatch")

    artifacts = manifest.get("artifacts")
    if not isinstance(artifacts, dict) or set(artifacts) != set(ARTIFACT_FILENAMES):
        raise ValueError("manifest artifact filename ledger mismatch")

    row_counts: dict[str, int] = {}
    for filename in ARTIFACT_FILENAMES:
        path = output_dir / filename
        record = artifacts[filename]
        if not isinstance(record, dict):
            raise ValueError(f"invalid artifact record: {filename}")
        if sha256(path) != record.get("sha256"):
            raise ValueError(f"artifact SHA-256 mismatch: {filename}")
        if path.stat().st_size != record.get("bytes"):
            raise ValueError(f"artifact byte-size mismatch: {filename}")
        with path.open("r", encoding="utf-8", newline="") as handle:
            row_count = sum(1 for _ in csv.DictReader(handle))
        if row_count != record.get("rows"):
            raise ValueError(f"artifact row-count mismatch: {filename}")
        row_counts[filename] = row_count

    expected_manifest = _build_manifest(output_dir, row_counts, paper_dir)
    if manifest != expected_manifest:
        raise ValueError("manifest metric or metadata ledger mismatch")
    return manifest


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        required=True,
        help="directory for the twelve CSV artifacts and manifest",
    )
    parser.add_argument(
        "--verify-only",
        action="store_true",
        help="strictly verify existing outputs without rewriting any file",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    manifest = verify(args.output_dir) if args.verify_only else run(args.output_dir)
    print(
        f"PASS schema={manifest['schema']} "
        f"rows={manifest['metrics']['total_csv_rows']} "
        f"csv={manifest['metrics']['csv_artifact_count']} "
        f"negative={manifest['metrics']['negative_control_count']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
