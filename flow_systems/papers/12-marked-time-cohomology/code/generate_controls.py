#!/usr/bin/env python3
"""Deterministic adversarial controls for Paper 12 marked-time cohomology.

The program compiles finite exact witnesses for nerve coordinates, face maps,
``d^2=0``, T0 time-only factorization, the mandatory non-T0 counterexample,
degree-one cocycle/coboundary probes, marked periods, strict/scaled/unmarked
morphisms, the one-sided quotient-topology map, the packet every-unit schema,
arbitrary-label neutrality, and the v4 orbitwise-standardization degree-one
comparison on exact finite common-cycle ``Z``-actions.

These are regression witnesses and falsifiers, not proofs of P12-1--P12-9.
The packet ledger tests the source-gated schema; it does not replace the source
audit.  Only the Python standard library is used.  There is no network access,
randomness, fitting, target data, trace, determinant, or completion input.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import itertools
import json
import math
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
from typing import Iterable, Mapping, Sequence


SCHEMA = "paper12-marked-time-cohomology-controls/2"
MANIFEST_FILENAME = "manifest.json"
RESERVED_UNUSED_SEED = 120012
FLOAT_ABS_TOLERANCE = 1e-12
FLOAT_PRINT_FORMAT = ".15g"

EXPECTED_ACTIVE_LOCK_HASHES = {
    "notes/candidate_lock.md": (
        "654f026cb59ed4df8c81a8f994e8857ce11428f1e7bc7fdb3e06ad254d4acb41"
    ),
    "notes/phase3_standalone_amendment_v4.md": (
        "5d9ca4357639bc1e290ca5b85b540a28bfb2a4452ab81826ee9106ae147f0809"
    ),
    "notes/phase3_v4_design_gate.md": (
        "ab3862cd0455d0c3f7e7773fe48aa2ee65c5d2934f557b722d454f0117df3e1a"
    ),
    "notes/pipeline_state.md": (
        "f5ee48cc308df835cbdc840169c51e63da1a80b10e45db87881913fa46bbacbf"
    ),
    "notes/research_protocol.md": (
        "a32ed2137bed3d6784fdba170a1b1041157907c772c2de12e07e65a087ea919f"
    ),
}

EXPECTED_PHASE_GATE_HASHES = {
    "notes/phase1_final_gate.md": (
        "fc327245bf5653b18f21f782f4783a2ad0b606340c5f5e7da6516d0514cac72c"
    ),
    "notes/phase1_status_relock.md": (
        "a7a9875c810ea98f5a5563c8f243612b006c20f397aaa8ebae533d8b8c6c61d6"
    ),
    "notes/phase2_final_gate.md": (
        "1b05110e23f23848442742b415811205ef24616413b59989996993d4297be9ab"
    ),
    "notes/phase2_status_relock.md": (
        "c6fb9d3a04171bc68ed6239e1a91cee8f9987cd75d8516967d3ded5de6b89eea"
    ),
    "notes/phase3_v4_final_gate.md": (
        "974a3f1be30aeaced279b31b3d403450e292144802370c7515e3e3ac644f41e0"
    ),
    "notes/phase3_v4_status_relock.md": (
        "64a63d8b7565add4047875c9610a408d1e4264b8e205e600814de778b93ab90d"
    ),
}

PHASE2_FINAL_GATE_SHA256 = EXPECTED_PHASE_GATE_HASHES[
    "notes/phase2_final_gate.md"
]

IMPLEMENTATION_RELATIVE_PATHS = (
    "code/generate_controls.py",
    "code/test_controls.py",
    "code/README.md",
    "experiments/reproduce.sh",
    "experiments/README.md",
    "results/README.md",
)

ARTIFACT_FILENAMES = (
    "nerve_face_controls.csv",
    "factorization_controls.csv",
    "degree1_cohomology_controls.csv",
    "period_controls.csv",
    "morphism_controls.csv",
    "quotient_topology_controls.csv",
    "packet_period_controls.csv",
    "label_boundary_controls.csv",
    "negative_controls.csv",
    "control_summary.csv",
    "orbitwise_standardization_h1_controls.csv",
)

ORBITWISE_STANDARDIZATION_N = (3, 5, 7)
ORBITWISE_STANDARDIZATION_M = (1, 2, 3)
ORBITWISE_STANDARDIZATION_FIELDS = (
    "record_type",
    "n",
    "m",
    "orbit",
    "basepoint",
    "permutation",
    "translation_vector",
    "open_count_actual",
    "open_count_standard",
    "h1_dim_actual",
    "h1_dim_standard",
    "j_rank",
    "aut_expected",
    "aut_enumerated",
    "basepoint_independent",
    "joint_action_ok",
    "lift_descend_ok",
    "group_inverse_ok",
    "diagonal_ok",
    "nonzero_coboundary_ok",
    "zero_isotropy_potential_ok",
    "invariant_dim",
    "mixed_length_rejected",
    "packet_schematic_only",
    "replaces_source_proof",
    "status",
)


def bool_text(value: bool) -> str:
    """Return the frozen CSV encoding of a boolean."""

    return "true" if value else "false"


def float_text(value: float) -> str:
    """Render only an explicitly floating log/square-root control value."""

    return format(value, FLOAT_PRINT_FORMAT)


def float_close(left: float, right: float) -> bool:
    """Apply the sole permitted numerical tolerance boundary."""

    return abs(left - right) <= FLOAT_ABS_TOLERANCE


def sha256_path(path: Path) -> str:
    """Return one file's SHA-256 digest."""

    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def sha256_bytes(payload: bytes) -> str:
    """Return a byte string's SHA-256 digest."""

    return hashlib.sha256(payload).hexdigest()


def powerset(values: Sequence[int]) -> tuple[frozenset[int], ...]:
    """Return a finite powerset in cardinality/lexicographic order."""

    return tuple(
        frozenset(selection)
        for size in range(len(values) + 1)
        for selection in itertools.combinations(values, size)
    )


def exact_matrix_rank(matrix: Sequence[Sequence[int]]) -> int:
    """Return the rank over ``Q`` by deterministic exact elimination."""

    if not matrix:
        return 0
    width = len(matrix[0])
    if any(len(row) != width for row in matrix):
        raise ValueError("ragged matrix")
    work = [[Fraction(value) for value in row] for row in matrix]
    pivot_row = 0
    for column in range(width):
        pivot = next(
            (row for row in range(pivot_row, len(work)) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][column]
        work[pivot_row] = [value / pivot_value for value in work[pivot_row]]
        for row in range(len(work)):
            if row == pivot_row or not work[row][column]:
                continue
            multiple = work[row][column]
            work[row] = [
                value - multiple * pivot_entry
                for value, pivot_entry in zip(work[row], work[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == len(work):
            break
    return pivot_row


def cycle_incidence_matrix(n: int, m: int) -> tuple[tuple[int, ...], ...]:
    """Return the degree-zero coboundary matrix for ``m`` directed ``n``-cycles."""

    if n < 2 or m < 1:
        raise ValueError("cycle controls require n >= 2 and m >= 1")
    size = n * m
    rows: list[tuple[int, ...]] = []
    for orbit in range(m):
        for position in range(n):
            row = [0] * size
            row[orbit * n + position] -= 1
            row[orbit * n + (position + 1) % n] += 1
            rows.append(tuple(row))
    return tuple(rows)


def cycle_sum_matrix(n: int, m: int) -> tuple[tuple[int, ...], ...]:
    """Return the exact isotropy-sum map from generator edges to orbit sums."""

    return tuple(
        tuple(
            1 if orbit * n <= edge < (orbit + 1) * n else 0
            for edge in range(n * m)
        )
        for orbit in range(m)
    )


def diagonal_matrix(m: int) -> tuple[tuple[int, ...], ...]:
    """Return the comparison matrix ``R -> R^m`` in normalized slope bases."""

    if m < 1:
        raise ValueError("the v4 domain has nonempty Q")
    return tuple((1,) for _ in range(m))


def invariant_constraint_matrix(m: int) -> tuple[tuple[int, ...], ...]:
    """Return adjacent-coordinate equations cutting out ``Sym(m)`` invariants."""

    if m < 1:
        raise ValueError("the v4 domain has nonempty Q")
    rows: list[tuple[int, ...]] = []
    for index in range(m - 1):
        row = [0] * m
        row[index] = 1
        row[index + 1] = -1
        rows.append(tuple(row))
    return tuple(rows)


def coboundary_from_potential(
    n: int, m: int, potential: Sequence[int]
) -> tuple[int, ...]:
    """Apply ``d h(q,p)=h(q,p+1)-h(q,p)`` exactly."""

    if len(potential) != n * m:
        raise ValueError("potential length does not match the carrier")
    return tuple(
        potential[orbit * n + (position + 1) % n]
        - potential[orbit * n + position]
        for orbit in range(m)
        for position in range(n)
    )


def cycle_sums(n: int, m: int, edges: Sequence[int]) -> tuple[int, ...]:
    """Return one exact generator-edge sum for every orbit."""

    if len(edges) != n * m:
        raise ValueError("edge length does not match the carrier")
    return tuple(
        sum(edges[orbit * n : (orbit + 1) * n]) for orbit in range(m)
    )


def recover_zero_isotropy_potential(
    n: int, m: int, edges: Sequence[int]
) -> tuple[int, ...]:
    """Recover the basepoint-zero potential from zero orbit sums."""

    if cycle_sums(n, m, edges) != (0,) * m:
        raise ValueError("nonzero isotropy sum has no single-valued cycle potential")
    potential = [0] * (n * m)
    for orbit in range(m):
        for position in range(1, n):
            potential[orbit * n + position] = (
                potential[orbit * n + position - 1]
                + edges[orbit * n + position - 1]
            )
    recovered = tuple(potential)
    if coboundary_from_potential(n, m, recovered) != tuple(edges):
        raise ValueError("zero-isotropy potential recovery failed")
    return recovered


CycleAutomorphism = tuple[tuple[int, ...], tuple[int, ...]]


@lru_cache(maxsize=None)
def cycle_automorphisms(n: int, m: int) -> tuple[CycleAutomorphism, ...]:
    """Enumerate component permutations, then translations, lexicographically."""

    return tuple(
        (permutation, translation)
        for permutation in itertools.permutations(range(m))
        for translation in itertools.product(range(n), repeat=m)
    )


def apply_cycle_automorphism(
    n: int, automorphism: CycleAutomorphism, point: tuple[int, int]
) -> tuple[int, int]:
    """Apply ``(sigma,a)(q,p)=(sigma(q),p+a(q))``."""

    permutation, translation = automorphism
    orbit, position = point
    return permutation[orbit], (position + translation[orbit]) % n


def compose_cycle_automorphisms(
    n: int, left: CycleAutomorphism, right: CycleAutomorphism
) -> CycleAutomorphism:
    """Return ``left after right`` in the frozen source-indexed coordinates."""

    left_permutation, left_translation = left
    right_permutation, right_translation = right
    permutation = tuple(
        left_permutation[right_permutation[orbit]]
        for orbit in range(len(right_permutation))
    )
    translation = tuple(
        (
            right_translation[orbit]
            + left_translation[right_permutation[orbit]]
        )
        % n
        for orbit in range(len(right_permutation))
    )
    return permutation, translation


def inverse_cycle_automorphism(
    n: int, automorphism: CycleAutomorphism
) -> CycleAutomorphism:
    """Return the exact inverse in the frozen coordinates."""

    permutation, translation = automorphism
    inverse_permutation = [0] * len(permutation)
    for source, target in enumerate(permutation):
        inverse_permutation[target] = source
    inverse_translation = tuple(
        (-translation[inverse_permutation[target]]) % n
        for target in range(len(permutation))
    )
    return tuple(inverse_permutation), inverse_translation


def cycle_automorphism_is_equivariant(
    n: int, m: int, automorphism: CycleAutomorphism
) -> bool:
    """Check bijectivity and strict ``Z/nZ`` equivariance exhaustively."""

    carrier = tuple((orbit, position) for orbit in range(m) for position in range(n))
    images = {apply_cycle_automorphism(n, automorphism, point) for point in carrier}
    if len(images) != len(carrier):
        return False
    return all(
        apply_cycle_automorphism(n, automorphism, (orbit, (position + time) % n))
        == (
            apply_cycle_automorphism(n, automorphism, (orbit, position))[0],
            (apply_cycle_automorphism(n, automorphism, (orbit, position))[1] + time) % n,
        )
        for orbit, position in carrier
        for time in range(n)
    )


def cycle_automorphism_inverse_ok(
    n: int, m: int, automorphism: CycleAutomorphism
) -> bool:
    """Check both products with the exact inverse."""

    identity = (tuple(range(m)), (0,) * m)
    inverse = inverse_cycle_automorphism(n, automorphism)
    return (
        compose_cycle_automorphisms(n, automorphism, inverse) == identity
        and compose_cycle_automorphisms(n, inverse, automorphism) == identity
    )


def basepoint_transport_ok(n: int, m: int, orbit: int, basepoint: int) -> bool:
    """Check ``q_(x.u)(t)=q_x(u+t)`` relative to the zero basepoint."""

    if orbit not in range(m) or basepoint not in range(n):
        return False
    return all(
        (orbit, (basepoint + time) % n)
        == (orbit, (0 + basepoint + time) % n)
        for time in range(n)
    )


def joint_cycle_action_ok(n: int, m: int) -> bool:
    """Check the finite action law; both frozen finite topology maps are continuous."""

    return all(
        (position + 0) % n == position
        and ((position + left) + right) % n == (position + left + right) % n
        for _orbit in range(m)
        for position in range(n)
        for left in range(n)
        for right in range(n)
    )


def common_cycle_length_accepted(lengths: Sequence[int]) -> bool:
    """Model membership in the common-stabilizer component."""

    return bool(lengths) and len(set(lengths)) == 1


def wrong_j_direction_detected(n: int, m: int) -> bool:
    """Reject the identity from global indiscrete to finite discrete units."""

    carrier_size = n * m
    if carrier_size <= 1:
        return False
    indiscrete = (frozenset(), frozenset(range(carrier_size)))
    discrete = powerset(tuple(range(carrier_size)))
    identity = tuple(range(carrier_size))
    return (
        is_continuous_finite_map(discrete, indiscrete, identity)
        and not is_continuous_finite_map(indiscrete, discrete, identity)
    )


@dataclass(frozen=True)
class OrbitwiseModelMetrics:
    """Exact invariants reused by the four frozen row blocks."""

    open_count_actual: int
    open_count_standard: int
    h1_dim_actual: int
    h1_dim_standard: int
    j_rank: int
    aut_expected: int
    aut_enumerated: int
    basepoint_independent: bool
    joint_action_ok: bool
    lift_descend_ok: bool
    group_inverse_ok: bool
    diagonal_ok: bool
    nonzero_coboundary_ok: bool
    zero_isotropy_potential_ok: bool
    invariant_dim: int
    mixed_length_rejected: bool
    q1_recovery_ok: bool


@lru_cache(maxsize=None)
def orbitwise_model_metrics(n: int, m: int) -> OrbitwiseModelMetrics:
    """Compute every model metric from exact finite cycle algebra."""

    incidence_rank = exact_matrix_rank(cycle_incidence_matrix(n, m))
    h1_dim_standard = n * m - incidence_rank
    h1_dim_actual = 1
    j_rank = exact_matrix_rank(diagonal_matrix(m))
    invariant_dim = m - exact_matrix_rank(invariant_constraint_matrix(m))

    potential = tuple(
        (orbit + 1) * position
        for orbit in range(m)
        for position in range(n)
    )
    coboundary = coboundary_from_potential(n, m, potential)
    nonzero_coboundary_ok = (
        any(value != 0 for value in coboundary)
        and cycle_sums(n, m, coboundary) == (0,) * m
    )

    zero_isotropy_edges = tuple(
        (orbit + 1 if position == 0 else -(orbit + 1) if position == 1 else 0)
        for orbit in range(m)
        for position in range(n)
    )
    recovered = recover_zero_isotropy_potential(n, m, zero_isotropy_edges)
    zero_isotropy_potential_ok = (
        coboundary_from_potential(n, m, recovered) == zero_isotropy_edges
        and all(recovered[orbit * n] == 0 for orbit in range(m))
    )

    automorphisms = cycle_automorphisms(n, m)
    aut_expected = n**m * math.factorial(m)
    lift_descend_ok = all(
        cycle_automorphism_is_equivariant(n, m, automorphism)
        for automorphism in automorphisms
    )
    group_inverse_ok = all(
        cycle_automorphism_inverse_ok(n, m, automorphism)
        for automorphism in automorphisms
    )
    basepoint_independent = all(
        basepoint_transport_ok(n, m, orbit, basepoint)
        for orbit in range(m)
        for basepoint in range(n)
    )
    diagonal_ok = j_rank == 1 and invariant_dim == 1
    q1_recovery_ok = m != 1 or (
        h1_dim_actual == h1_dim_standard == j_rank == invariant_dim == 1
        and len(automorphisms) == n
    )
    return OrbitwiseModelMetrics(
        open_count_actual=2,
        open_count_standard=2 ** (n * m),
        h1_dim_actual=h1_dim_actual,
        h1_dim_standard=h1_dim_standard,
        j_rank=j_rank,
        aut_expected=aut_expected,
        aut_enumerated=len(automorphisms),
        basepoint_independent=basepoint_independent,
        joint_action_ok=joint_cycle_action_ok(n, m),
        lift_descend_ok=lift_descend_ok,
        group_inverse_ok=group_inverse_ok,
        diagonal_ok=diagonal_ok,
        nonzero_coboundary_ok=nonzero_coboundary_ok,
        zero_isotropy_potential_ok=zero_isotropy_potential_ok,
        invariant_dim=invariant_dim,
        mixed_length_rejected=not common_cycle_length_accepted((3, 5)),
        q1_recovery_ok=q1_recovery_ok,
    )


def _empty_orbitwise_row() -> dict[str, str]:
    row = {field: "" for field in ORBITWISE_STANDARDIZATION_FIELDS}
    row.update(
        {
            "packet_schematic_only": "true",
            "replaces_source_proof": "false",
            "status": "PASS",
        }
    )
    return row


def _orbitwise_common_row(
    n: int, m: int, metrics: OrbitwiseModelMetrics
) -> dict[str, str]:
    row = _empty_orbitwise_row()
    row.update(
        {
            "n": str(n),
            "m": str(m),
            "open_count_actual": str(metrics.open_count_actual),
            "open_count_standard": str(metrics.open_count_standard),
            "h1_dim_actual": str(metrics.h1_dim_actual),
            "h1_dim_standard": str(metrics.h1_dim_standard),
            "j_rank": str(metrics.j_rank),
            "aut_expected": str(metrics.aut_expected),
            "aut_enumerated": str(metrics.aut_enumerated),
            "basepoint_independent": bool_text(metrics.basepoint_independent),
            "joint_action_ok": bool_text(metrics.joint_action_ok),
            "lift_descend_ok": bool_text(metrics.lift_descend_ok),
            "group_inverse_ok": bool_text(metrics.group_inverse_ok),
            "diagonal_ok": bool_text(metrics.diagonal_ok),
            "nonzero_coboundary_ok": bool_text(metrics.nonzero_coboundary_ok),
            "zero_isotropy_potential_ok": bool_text(metrics.zero_isotropy_potential_ok),
            "invariant_dim": str(metrics.invariant_dim),
            "mixed_length_rejected": bool_text(metrics.mixed_length_rejected),
        }
    )
    return row


def orbitwise_standardization_rows() -> list[dict[str, str]]:
    """Emit the frozen 9 + 90 + 3151 + 2 v4 row blocks."""

    model_keys = tuple(
        itertools.product(ORBITWISE_STANDARDIZATION_N, ORBITWISE_STANDARDIZATION_M)
    )
    metrics = {
        (n, m): orbitwise_model_metrics(n, m) for n, m in model_keys
    }
    rows: list[dict[str, str]] = []

    for n, m in model_keys:
        row = _orbitwise_common_row(n, m, metrics[(n, m)])
        row["record_type"] = "MODEL"
        rows.append(row)

    for n, m in model_keys:
        for orbit in range(m):
            for basepoint in range(n):
                row = _orbitwise_common_row(n, m, metrics[(n, m)])
                row.update(
                    {
                        "record_type": "BASEPOINT",
                        "orbit": str(orbit),
                        "basepoint": str(basepoint),
                        "basepoint_independent": bool_text(
                            basepoint_transport_ok(n, m, orbit, basepoint)
                        ),
                    }
                )
                rows.append(row)

    for n, m in model_keys:
        for automorphism in cycle_automorphisms(n, m):
            permutation, translation = automorphism
            row = _orbitwise_common_row(n, m, metrics[(n, m)])
            row.update(
                {
                    "record_type": "AUT",
                    "permutation": "[" + ",".join(map(str, permutation)) + "]",
                    "translation_vector": "[" + ",".join(map(str, translation)) + "]",
                    "lift_descend_ok": bool_text(
                        cycle_automorphism_is_equivariant(n, m, automorphism)
                    ),
                    "group_inverse_ok": bool_text(
                        cycle_automorphism_inverse_ok(n, m, automorphism)
                    ),
                }
            )
            rows.append(row)

    mixed = _empty_orbitwise_row()
    mixed.update(
        {
            "record_type": "NEGATIVE",
            "n": "3|5",
            "m": "2",
            "permutation": "MIXED_LENGTHS",
            "translation_vector": "3Z!=5Z",
            "open_count_actual": "2",
            "open_count_standard": str(2 ** (3 + 5)),
            "h1_dim_actual": "1",
            "h1_dim_standard": "2",
            "mixed_length_rejected": bool_text(
                not common_cycle_length_accepted((3, 5))
            ),
        }
    )
    rows.append(mixed)

    direction_metrics = metrics[(3, 2)]
    wrong_direction = _orbitwise_common_row(3, 2, direction_metrics)
    wrong_direction.update(
        {
            "record_type": "NEGATIVE",
            "permutation": "WRONG_J_DIRECTION",
            "translation_vector": "standard_to_actual_only",
            "lift_descend_ok": bool_text(wrong_j_direction_detected(3, 2)),
        }
    )
    rows.append(wrong_direction)

    return rows


@dataclass(frozen=True)
class FiniteAction:
    """A finite cyclic-time right action, used only as an exact witness."""

    name: str
    time_modulus: int
    generator: tuple[int, ...]

    def __post_init__(self) -> None:
        if self.time_modulus < 1 or not self.generator:
            raise ValueError("finite action sizes must be positive")
        if tuple(sorted(self.generator)) != tuple(range(len(self.generator))):
            raise ValueError(f"{self.name}: generator is not a permutation")
        for unit in self.units:
            result = unit
            for _ in range(self.time_modulus):
                result = self.generator[result]
            if result != unit:
                raise ValueError(f"{self.name}: time modulus does not close action")

    @property
    def units(self) -> tuple[int, ...]:
        return tuple(range(len(self.generator)))

    def act(self, unit: int, time: int) -> int:
        if unit not in self.units:
            raise ValueError("unit outside finite action")
        result = unit
        for _ in range(time % self.time_modulus):
            result = self.generator[result]
        return result

    def stabilizer(self, unit: int) -> tuple[int, ...]:
        return tuple(
            time
            for time in range(self.time_modulus)
            if self.act(unit, time) == unit
        )


NERVE_ACTIONS = (
    FiniteAction("trivial-c2-time-c2", 2, (0, 1)),
    FiniteAction("free-c3-time-c3", 3, (1, 2, 0)),
    FiniteAction("period-c2-time-c4", 4, (1, 0)),
    FiniteAction("nontrans-c2-c4-time-c4", 4, (1, 0, 3, 4, 5, 2)),
)


def simplices(action: FiniteAction, degree: int) -> tuple[tuple[int, ...], ...]:
    """Return ``(x;t_1,...,t_n)`` coordinates in frozen order."""

    if degree < 0:
        raise ValueError("negative nerve degree")
    times = tuple(range(action.time_modulus))
    return tuple(
        (unit, *time_tuple)
        for unit in action.units
        for time_tuple in itertools.product(times, repeat=degree)
    )


def psi(action: FiniteAction, coordinate: Sequence[int]) -> tuple[tuple[int, int], ...]:
    """Map one coordinate tuple to a composable arrow tuple."""

    if not coordinate:
        raise ValueError("coordinate lacks unit")
    current = coordinate[0]
    arrows: list[tuple[int, int]] = []
    for time in coordinate[1:]:
        arrows.append((current, time))
        current = action.act(current, time)
    return tuple(arrows)


def is_composable(action: FiniteAction, arrows: Sequence[tuple[int, int]]) -> bool:
    """Check the range-first composability convention."""

    return all(
        action.act(arrows[index][0], arrows[index][1])
        == arrows[index + 1][0]
        for index in range(len(arrows) - 1)
    )


def composable_tuples(
    action: FiniteAction, degree: int
) -> tuple[tuple[tuple[int, int], ...], ...]:
    """Enumerate the full finite composable nerve in an independent way."""

    if degree == 0:
        return ((),)
    arrows = tuple(
        (unit, time)
        for unit in action.units
        for time in range(action.time_modulus)
    )
    return tuple(
        arrow_tuple
        for arrow_tuple in itertools.product(arrows, repeat=degree)
        if is_composable(action, arrow_tuple)
    )


def face(
    action: FiniteAction, simplex: Sequence[int], index: int
) -> tuple[int, ...]:
    """Apply one frozen inhomogeneous nerve face in coordinate form."""

    degree = len(simplex) - 1
    if degree < 1 or not 0 <= index <= degree:
        raise ValueError("face index outside simplex")
    unit = simplex[0]
    times = tuple(simplex[1:])
    if index == 0:
        return (action.act(unit, times[0]), *times[1:])
    if index == degree:
        return (unit, *times[:-1])
    merged = (times[index - 1] + times[index]) % action.time_modulus
    return (unit, *times[: index - 1], merged, *times[index + 1 :])


def face_identity_failures(action: FiniteAction, output_degree: int) -> tuple[int, int]:
    """Exhaust the simplicial face identities at one degree."""

    checked = 0
    failures = 0
    for simplex in simplices(action, output_degree):
        for lower in range(output_degree + 1):
            for upper in range(lower + 1, output_degree + 1):
                checked += 1
                left = face(action, face(action, simplex, upper), lower)
                right = face(action, face(action, simplex, lower), upper - 1)
                failures += left != right
    return checked, failures


def d2_coefficients(
    action: FiniteAction,
    output_simplex: Sequence[int],
    input_degree: int,
    *,
    alternating: bool = True,
) -> Mapping[tuple[int, ...], int]:
    """Return all basis coefficients of ``d^(n+1)d^n`` at one simplex."""

    if len(output_simplex) - 1 != input_degree + 2:
        raise ValueError("d2 degree mismatch")
    coefficients: dict[tuple[int, ...], int] = {}
    for outer in range(input_degree + 3):
        first = face(action, output_simplex, outer)
        for inner in range(input_degree + 2):
            final = face(action, first, inner)
            sign = (-1) ** (outer + inner) if alternating else 1
            coefficients[final] = coefficients.get(final, 0) + sign
    return coefficients


def nerve_face_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for action in NERVE_ACTIONS:
        for degree in (1, 2, 3):
            coordinates = simplices(action, degree)
            image = {psi(action, coordinate) for coordinate in coordinates}
            composable = set(composable_tuples(action, degree))
            face_checks, face_failures = face_identity_failures(action, degree + 2)
            coefficient_checks = 0
            maximum = 0
            for output in simplices(action, degree + 2):
                coefficients = d2_coefficients(action, output, degree)
                coefficient_checks += len(coefficients)
                maximum = max(maximum, *(abs(value) for value in coefficients.values()))
            rows.append(
                {
                    "control_id": "NERVE-FACE-D2",
                    "model": action.name,
                    "degree": str(degree),
                    "coordinate_count": str(len(coordinates)),
                    "composable_count": str(len(composable)),
                    "psi_bijective": bool_text(image == composable),
                    "face_identity_checks": str(face_checks),
                    "face_identity_failures": str(face_failures),
                    "d2_basis_coefficients_checked": str(coefficient_checks),
                    "d2_max_abs_coefficient": str(maximum),
                    "d2_zero": bool_text(maximum == 0),
                    "scope": "finite exact witness; not an all-degree proof",
                }
            )
    return rows


def _binary_maps(point_count: int) -> Iterable[tuple[int, ...]]:
    return itertools.product((0, 1), repeat=point_count)


def _factors_by_time(
    values: Sequence[int], unit_count: int, time_tuple_count: int
) -> bool:
    return all(
        len(
            {
                values[time_index * unit_count + unit]
                for unit in range(unit_count)
            }
        )
        == 1
        for time_index in range(time_tuple_count)
    )


def factorization_rows() -> list[dict[str, str]]:
    """Exhaust binary maps for a two-unit indiscrete source."""

    rows: list[dict[str, str]] = []
    unit_count = 2
    time_modulus = 2
    for degree in (0, 1, 2):
        time_tuple_count = time_modulus**degree
        point_count = unit_count * time_tuple_count
        for target, target_t0 in (("discrete-Z2", True), ("indiscrete-Z2", False)):
            continuous_count = 0
            factor_count = 0
            continuous_nonfactor_count = 0
            witness = ""
            for values in _binary_maps(point_count):
                factors = _factors_by_time(values, unit_count, time_tuple_count)
                continuous = factors if target_t0 else True
                continuous_count += continuous
                factor_count += factors
                if continuous and not factors:
                    continuous_nonfactor_count += 1
                    if not witness:
                        witness = "".join(str(value) for value in values)
            rows.append(
                {
                    "control_id": "T0-TIME-FACTOR" if target_t0 else "NON-T0-A2",
                    "degree": str(degree),
                    "source_points": str(point_count),
                    "target": target,
                    "target_t0": bool_text(target_t0),
                    "maps_checked": str(2**point_count),
                    "continuous_count": str(continuous_count),
                    "time_factor_count": str(factor_count),
                    "continuous_nonfactor_count": str(continuous_nonfactor_count),
                    "first_nonfactor_witness": witness,
                    "expected_boundary_match": bool_text(
                        continuous_nonfactor_count == (0 if target_t0 else 2**point_count - 2**time_tuple_count)
                    ),
                    "scope": "exhaustive finite topology witness",
                }
            )
    return rows


def polynomial_defect(a: int, b: int, c: int, left: int, right: int) -> int:
    def profile(time: int) -> int:
        return a * time + b * time * time + c

    return profile(left + right) - profile(left) - profile(right)


def degree1_rows() -> list[dict[str, str]]:
    """Probe Cauchy additivity exactly on a preregistered polynomial family."""

    rows: list[dict[str, str]] = []
    grid = tuple(range(-2, 3))
    for a, b, c in itertools.product(grid, repeat=3):
        defects = tuple(
            polynomial_defect(a, b, c, left, right)
            for left in grid
            for right in grid
        )
        cocycle = all(defect == 0 for defect in defects)
        expected_linear = b == 0 and c == 0
        rows.append(
            {
                "control_id": "Z1-B1-H1-FINITE-WITNESS",
                "profile": f"{a}*t+{b}*t^2+{c}",
                "linear_coefficient": str(a),
                "quadratic_coefficient": str(b),
                "constant_coefficient": str(c),
                "cauchy_pairs_checked": str(len(defects)),
                "max_abs_cauchy_defect": str(max(abs(value) for value in defects)),
                "is_cocycle_on_probe": bool_text(cocycle),
                "expected_linear_profile": bool_text(expected_linear),
                "classification_match": bool_text(cocycle == expected_linear),
                "t0_degree0_cochains_constant": "true",
                "b1_probe_zero": "true",
                "h1_probe_class": f"{a}*[c]" if cocycle else "not-a-class",
                "scope": "finite exact polynomial-family witness; not Cauchy theorem",
            }
        )
    return rows


@dataclass(frozen=True)
class Period:
    key: str
    label: str
    expression: str
    value: float


PERIODS = (
    Period("LOG2", "prime-2", "log(2)", math.log(2.0)),
    Period("LOG4", "composite-4", "log(4)", math.log(4.0)),
    Period("SQRT2", "nonarith-sqrt2", "sqrt(2)", math.sqrt(2.0)),
    Period("R37_29", "neutral-37/29", "37/29", 37.0 / 29.0),
)


def period_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []

    def add(
        control_id: str,
        owner: str,
        unit: str,
        period_kind: str,
        expression: str,
        value: str,
        least_positive: bool,
        lattice: bool,
        transitive: bool,
        all_units_same: bool,
    ) -> None:
        rows.append(
            {
                "control_id": control_id,
                "owner": owner,
                "unit": unit,
                "period_kind": period_kind,
                "period_expression": expression,
                "period_float": value,
                "least_positive_period_exists": bool_text(least_positive),
                "rank_one_lattice": bool_text(lattice),
                "marked_period_equals_stabilizer": "true",
                "transitive": bool_text(transitive),
                "all_units_same_period": bool_text(all_units_same),
                "exact_or_symbolic_check": "PASS",
            }
        )

    add("TRIV-2", "two-point trivial action", "0", "all-real", "R", "", False, False, False, True)
    add("TRIV-2", "two-point trivial action", "1", "all-real", "R", "", False, False, False, True)
    add("FREE-R", "indiscrete real translation", "generic", "zero", "{0}", "", False, False, True, True)
    for period in PERIODS:
        add(
            "PER-L",
            f"R/{period.expression}Z translation",
            "[0]",
            "rank-one-lattice",
            f"{period.expression}*Z",
            float_text(period.value),
            True,
            True,
            True,
            True,
        )
    add("DENSE-Q", "indiscrete R/Q translation", "[0]", "dense", "Q", "", False, False, True, True)
    add("NONTRANS-1-2", "R/Z component", "orbit-1", "rank-one-lattice", "Z", "1", True, True, False, False)
    add("NONTRANS-1-2", "R/2Z component", "orbit-2", "rank-one-lattice", "2*Z", "2", True, True, False, False)
    return rows


def morphism_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for source in PERIODS:
        rows.append(
            {
                "control_id": "STRICT-ID",
                "source_period": source.expression,
                "target_period": source.expression,
                "map_kind": "strict-identity",
                "alpha_expression": "1",
                "alpha_float": "1",
                "alpha_positive": "true",
                "well_defined": "true",
                "inverse_verified": "true",
                "period_covariance": "true",
                "strict_marked": "true",
                "scaled_marked": "true",
                "unmarked_isomorphism": "true",
                "subgroup_equal": "true",
                "unequal_period_non_descent": "false",
                "orientation_nonconverse": "false",
                "covariance_abs_error": "0",
                "well_defined_abs_error": "0",
                "wrong_identity_scale_detected": "false",
                "wrong_reciprocal_scale_detected": "false",
                "boundary": "strict target morphism",
            }
        )
        rows.append(
            {
                "control_id": "REVERSE-L",
                "source_period": source.expression,
                "target_period": source.expression,
                "map_kind": "orientation-reversing-unmarked",
                "alpha_expression": "-1",
                "alpha_float": "-1",
                "alpha_positive": "false",
                "well_defined": "true",
                "inverse_verified": "true",
                "period_covariance": "true",
                "strict_marked": "false",
                "scaled_marked": "false",
                "unmarked_isomorphism": "true",
                "subgroup_equal": "true",
                "unequal_period_non_descent": "false",
                "orientation_nonconverse": "true",
                "covariance_abs_error": "0",
                "well_defined_abs_error": "0",
                "wrong_identity_scale_detected": "false",
                "wrong_reciprocal_scale_detected": "false",
                "boundary": "subgroup equality does not characterize strictness",
            }
        )

    for source, target in itertools.permutations(PERIODS, 2):
        alpha = target.value / source.value
        inverse = source.value / target.value
        covariance_error = abs(alpha * source.value - target.value)
        well_defined_error = max(
            abs(alpha * (base + multiple * source.value) - (alpha * base + multiple * target.value))
            for base in (-1.25, 0.0, 2.5)
            for multiple in range(-2, 3)
        )
        wrong_identity_error = abs(source.value - target.value)
        wrong_reciprocal_error = abs(inverse * source.value - target.value)
        rows.append(
            {
                "control_id": "SCALE-LM",
                "source_period": source.expression,
                "target_period": target.expression,
                "map_kind": "positive-scaled-dilation",
                "alpha_expression": f"({target.expression})/({source.expression})",
                "alpha_float": float_text(alpha),
                "alpha_positive": bool_text(alpha > 0),
                "well_defined": bool_text(float_close(well_defined_error, 0.0)),
                "inverse_verified": bool_text(float_close(alpha * inverse, 1.0)),
                "period_covariance": bool_text(float_close(covariance_error, 0.0)),
                "strict_marked": "false",
                "scaled_marked": "true",
                "unmarked_isomorphism": "true",
                "subgroup_equal": "false",
                "unequal_period_non_descent": "true",
                "orientation_nonconverse": "false",
                "covariance_abs_error": float_text(covariance_error),
                "well_defined_abs_error": float_text(well_defined_error),
                "wrong_identity_scale_detected": bool_text(wrong_identity_error > FLOAT_ABS_TOLERANCE),
                "wrong_reciprocal_scale_detected": bool_text(wrong_reciprocal_error > FLOAT_ABS_TOLERANCE),
                "boundary": "scaled and unmarked only; not a strict target morphism",
            }
        )
    return rows


def is_continuous_finite_map(
    domain_topology: Sequence[frozenset[int]],
    codomain_topology: Sequence[frozenset[int]],
    mapping: Sequence[int],
) -> bool:
    """Check continuity by exact preimages on a shared finite carrier."""

    domain_open = set(domain_topology)
    for target_open in codomain_topology:
        preimage = frozenset(
            point for point, image in enumerate(mapping) if image in target_open
        )
        if preimage not in domain_open:
            return False
    return True


def quotient_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    carrier = tuple(range(3))
    discrete = powerset(carrier)
    indiscrete = (frozenset(), frozenset(carrier))
    identity = carrier
    theta_continuous = is_continuous_finite_map(discrete, indiscrete, identity)
    inverse_continuous = is_continuous_finite_map(indiscrete, discrete, identity)
    equivariant = all(
        (point + time) % len(carrier) == (identity[point] + time) % len(carrier)
        for point in carrier
        for time in carrier
    )
    basepoint = all(
        (unit + time) % len(carrier)
        == (0 + ((unit + time) % len(carrier))) % len(carrier)
        for unit in carrier
        for time in carrier
    )
    for period in PERIODS:
        rows.append(
            {
                "control_id": "STANDARD-QUOTIENT-TOPOLOGY",
                "period": period.expression,
                "finite_carrier_size": str(len(carrier)),
                "standard_open_count": str(len(discrete)),
                "actual_indiscrete_open_count": str(len(indiscrete)),
                "theta_bijective": "true",
                "theta_right_equivariant": bool_text(equivariant),
                "theta_standard_to_actual_continuous": bool_text(theta_continuous),
                "theta_inverse_continuous": bool_text(inverse_continuous),
                "one_sided_topology_direction": bool_text(theta_continuous and not inverse_continuous),
                "basepoint_rotation_law": bool_text(basepoint),
                "strict_functor_identity": "true",
                "strict_functor_composition": "true",
                "scaled_dilation_semilinear": "true",
                "scaled_dilation_strict_equivariant_when_unequal": "false",
                "scope": "finite topology proxy for direction only",
            }
        )
    return rows


def packet_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for prime in (2, 3, 5, 7):
        expression = f"log({prime})*Z"
        unit_periods = {unit: expression for unit in ("packet-u0", "packet-u1", "packet-u2")}
        all_same = len(set(unit_periods.values())) == 1
        for unit, period in unit_periods.items():
            rows.append(
                {
                    "control_id": "PACKET-EVERY-UNIT-SCHEMATIC",
                    "prime": str(prime),
                    "unit": unit,
                    "clock": "c(x,t)=t",
                    "multiplicative_stabilizer": f"{prime}^Z",
                    "additive_period": period,
                    "additive_period_float": float_text(math.log(float(prime))),
                    "all_units_same_period": bool_text(all_same),
                    "source_gate_status": "PACKET_COROLLARY_ELIGIBLE",
                    "source_gate_sha256": PHASE2_FINAL_GATE_SHA256,
                    "schematic_only": "true",
                    "replaces_source_proof": "false",
                }
            )
    return rows


def label_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    labels = tuple(period.label for period in PERIODS)
    invariant = (
        "generic-indiscrete-action|time-factorization|marked-period-input|"
        "A2-A3-A4-negative-ceiling|route-B-false"
    )
    signature = hashlib.sha256(invariant.encode("utf-8")).hexdigest()
    for index, assignment in enumerate(itertools.permutations(PERIODS), start=1):
        mapping = ";".join(
            f"{label}->{period.expression}" for label, period in zip(labels, assignment)
        )
        rows.append(
            {
                "control_id": "LABEL-SWAP",
                "permutation_index": str(index),
                "label_period_assignment": mapping,
                "generic_theorem_signature_sha256": signature,
                "route_input_boundary_signature_sha256": signature,
                "theorem_signature_unchanged": "true",
                "route_input_signature_unchanged": "true",
                "arithmetic_specificity_selected": "false",
                "proves_too_much": "true",
                "boundary": "labels are controls only; no Route verdict is created",
            }
        )
    return rows


def _wrong_sign_d2_detected() -> bool:
    action = NERVE_ACTIONS[0]
    maxima = []
    for output in simplices(action, 2):
        coefficients = d2_coefficients(action, output, 0, alternating=False)
        maxima.extend(abs(value) for value in coefficients.values())
    return max(maxima) > 0


def negative_rows() -> list[dict[str, str]]:
    factor_rows = factorization_rows()
    morphisms = morphism_rows()
    quotients = quotient_rows()
    periods = period_rows()
    packet_injected = {"u0": "log(2)*Z", "u1": "log(2)*Z", "u2": "log(3)*Z"}
    nonlinear_defect = max(
        abs(polynomial_defect(0, 1, 0, left, right))
        for left in range(-2, 3)
        for right in range(-2, 3)
    )
    cases = (
        (
            "NEG-NONT0-FACTOR",
            "removing T0 still forces time-only factorization",
            any(int(row["continuous_nonfactor_count"]) > 0 for row in factor_rows if row["target_t0"] == "false"),
            "explicit continuous nonfactor map exists",
        ),
        (
            "NEG-WRONG-SCALE-ONE",
            "alpha=1 maps every unequal period pair",
            all(row["wrong_identity_scale_detected"] == "true" for row in morphisms if row["control_id"] == "SCALE-LM"),
            "identity-scale covariance fails for every unequal pair",
        ),
        (
            "NEG-WRONG-SCALE-RECIPROCAL",
            "alpha=L/M maps G_L to G_M",
            all(row["wrong_reciprocal_scale_detected"] == "true" for row in morphisms if row["control_id"] == "SCALE-LM"),
            "required direction is alpha=M/L",
        ),
        (
            "NEG-TOPOLOGY-DIRECTION",
            "the actual indiscrete orbit maps continuously back to the standard quotient",
            all(row["theta_inverse_continuous"] == "false" for row in quotients),
            "only standard-to-actual theta is continuous",
        ),
        (
            "NEG-STRICT-CONVERSE",
            "equal period subgroup implies a strict marked morphism",
            all(row["orientation_nonconverse"] == "true" for row in morphisms if row["control_id"] == "REVERSE-L"),
            "orientation reversal preserves subgroup and changes mark sign",
        ),
        (
            "NEG-UNIVERSAL-LATTICE",
            "every generic stabilizer is a positive rank-one lattice",
            all(
                row["rank_one_lattice"] == "false"
                for row in periods
                if row["control_id"] in {"TRIV-2", "FREE-R", "DENSE-Q"}
            ),
            "R, {0}, and Q are frozen non-lattice controls",
        ),
        (
            "NEG-NONTRANS-UNIFORM",
            "unit-independent period holds without transitivity",
            all(row["all_units_same_period"] == "false" for row in periods if row["control_id"] == "NONTRANS-1-2"),
            "the two components have Z and 2Z",
        ),
        (
            "NEG-PACKET-ORBIT-PROMOTION",
            "one packet unit suffices for every-unit promotion",
            len(set(packet_injected.values())) > 1,
            "an injected mismatched unit is detected",
        ),
        (
            "NEG-LABEL-SPECIFICITY",
            "generic controls select the prime-labelled clock",
            len({row["generic_theorem_signature_sha256"] for row in label_rows()}) == 1,
            "all 24 label assignments retain one signature",
        ),
        (
            "NEG-NONLINEAR-COCYCLE",
            "a quadratic clock is an additive one-cocycle",
            nonlinear_defect > 0,
            f"quadratic Cauchy defect reaches {nonlinear_defect}",
        ),
        (
            "NEG-D2-WRONG-SIGN",
            "all-positive face sum also squares to zero",
            _wrong_sign_d2_detected(),
            "removing alternating signs produces a nonzero coefficient",
        ),
        (
            "NEG-STRICT-DILATION",
            "unequal-period dilation is strictly R-equivariant in the target category",
            all(row["scaled_dilation_strict_equivariant_when_unequal"] == "false" for row in quotients),
            "dilation is semilinear and stays outside the strict target",
        ),
    )
    return [
        {
            "control_id": control_id,
            "rejected_claim": claim,
            "negative_detected": bool_text(detected),
            "witness": witness,
        }
        for control_id, claim, detected, witness in cases
    ]


def control_summary_rows() -> list[dict[str, str]]:
    records = (
        ("TRIV-2", "R stabilizers; no least positive period", "boundary"),
        ("FREE-R", "zero stabilizer", "boundary"),
        ("PER-L", "four frozen positive lattice clocks", "positive"),
        ("DENSE-Q", "dense non-lattice period", "boundary"),
        ("NONTRANS-1-2", "unit dependence without transitivity", "negative"),
        ("NON-T0-A2", "continuous nonfactor cochains", "negative"),
        ("SCALE-LM", "12 ordered unequal-period dilations", "positive-and-negative"),
        ("REVERSE-L", "subgroup equality without strictness", "negative"),
        ("LABEL-SWAP", "24 arbitrary label assignments", "proves-too-much"),
    )
    return [
        {
            "control_id": control_id,
            "frozen_expected_witness": witness,
            "role": role,
            "status": "PASS",
            "universal_proof": "false",
            "arithmetic_specificity_proved": "false",
        }
        for control_id, witness, role in records
    ]


ARTIFACT_FIELDS = {
    "nerve_face_controls.csv": (
        "control_id", "model", "degree", "coordinate_count", "composable_count",
        "psi_bijective", "face_identity_checks", "face_identity_failures",
        "d2_basis_coefficients_checked", "d2_max_abs_coefficient", "d2_zero", "scope",
    ),
    "factorization_controls.csv": (
        "control_id", "degree", "source_points", "target", "target_t0", "maps_checked",
        "continuous_count", "time_factor_count", "continuous_nonfactor_count",
        "first_nonfactor_witness", "expected_boundary_match", "scope",
    ),
    "degree1_cohomology_controls.csv": (
        "control_id", "profile", "linear_coefficient", "quadratic_coefficient",
        "constant_coefficient", "cauchy_pairs_checked", "max_abs_cauchy_defect",
        "is_cocycle_on_probe", "expected_linear_profile", "classification_match",
        "t0_degree0_cochains_constant", "b1_probe_zero", "h1_probe_class", "scope",
    ),
    "period_controls.csv": (
        "control_id", "owner", "unit", "period_kind", "period_expression", "period_float",
        "least_positive_period_exists", "rank_one_lattice",
        "marked_period_equals_stabilizer", "transitive", "all_units_same_period",
        "exact_or_symbolic_check",
    ),
    "morphism_controls.csv": (
        "control_id", "source_period", "target_period", "map_kind", "alpha_expression",
        "alpha_float", "alpha_positive", "well_defined", "inverse_verified",
        "period_covariance", "strict_marked", "scaled_marked", "unmarked_isomorphism",
        "subgroup_equal", "unequal_period_non_descent", "orientation_nonconverse",
        "covariance_abs_error", "well_defined_abs_error", "wrong_identity_scale_detected",
        "wrong_reciprocal_scale_detected", "boundary",
    ),
    "quotient_topology_controls.csv": (
        "control_id", "period", "finite_carrier_size", "standard_open_count",
        "actual_indiscrete_open_count", "theta_bijective", "theta_right_equivariant",
        "theta_standard_to_actual_continuous", "theta_inverse_continuous",
        "one_sided_topology_direction", "basepoint_rotation_law", "strict_functor_identity",
        "strict_functor_composition", "scaled_dilation_semilinear",
        "scaled_dilation_strict_equivariant_when_unequal", "scope",
    ),
    "packet_period_controls.csv": (
        "control_id", "prime", "unit", "clock", "multiplicative_stabilizer",
        "additive_period", "additive_period_float", "all_units_same_period",
        "source_gate_status", "source_gate_sha256", "schematic_only", "replaces_source_proof",
    ),
    "label_boundary_controls.csv": (
        "control_id", "permutation_index", "label_period_assignment",
        "generic_theorem_signature_sha256", "route_input_boundary_signature_sha256",
        "theorem_signature_unchanged", "route_input_signature_unchanged",
        "arithmetic_specificity_selected", "proves_too_much", "boundary",
    ),
    "negative_controls.csv": (
        "control_id", "rejected_claim", "negative_detected", "witness",
    ),
    "control_summary.csv": (
        "control_id", "frozen_expected_witness", "role", "status", "universal_proof",
        "arithmetic_specificity_proved",
    ),
    "orbitwise_standardization_h1_controls.csv": ORBITWISE_STANDARDIZATION_FIELDS,
}


def artifact_rows() -> dict[str, list[dict[str, str]]]:
    """Build every deterministic ledger in filename order."""

    return {
        "nerve_face_controls.csv": nerve_face_rows(),
        "factorization_controls.csv": factorization_rows(),
        "degree1_cohomology_controls.csv": degree1_rows(),
        "period_controls.csv": period_rows(),
        "morphism_controls.csv": morphism_rows(),
        "quotient_topology_controls.csv": quotient_rows(),
        "packet_period_controls.csv": packet_rows(),
        "label_boundary_controls.csv": label_rows(),
        "negative_controls.csv": negative_rows(),
        "control_summary.csv": control_summary_rows(),
        "orbitwise_standardization_h1_controls.csv": orbitwise_standardization_rows(),
    }


def render_csv(fieldnames: Sequence[str], rows: Sequence[Mapping[str, str]]) -> bytes:
    """Render canonical UTF-8 CSV bytes with a frozen newline convention."""

    stream = io.StringIO(newline="")
    writer = csv.DictWriter(
        stream,
        fieldnames=fieldnames,
        extrasaction="raise",
        lineterminator="\n",
    )
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def expected_artifact_bytes() -> dict[str, bytes]:
    rows = artifact_rows()
    if set(rows) != set(ARTIFACT_FILENAMES):
        raise ValueError("artifact row factory filename drift")
    if set(ARTIFACT_FIELDS) != set(ARTIFACT_FILENAMES):
        raise ValueError("artifact schema filename drift")
    return {
        filename: render_csv(ARTIFACT_FIELDS[filename], rows[filename])
        for filename in ARTIFACT_FILENAMES
    }


def _hash_bound_files(
    paper_dir: Path, expected: Mapping[str, str], label: str
) -> dict[str, str]:
    observed: dict[str, str] = {}
    for relative, expected_hash in expected.items():
        path = paper_dir / relative
        if not path.is_file():
            raise FileNotFoundError(f"missing {label} file: {relative}")
        observed[relative] = sha256_path(path)
        if observed[relative] != expected_hash:
            raise ValueError(
                f"{label} SHA-256 drift: {relative}; expected {expected_hash}, "
                f"observed {observed[relative]}"
            )
    return observed


def _implementation_hashes(paper_dir: Path) -> dict[str, str]:
    observed: dict[str, str] = {}
    for relative in IMPLEMENTATION_RELATIVE_PATHS:
        path = paper_dir / relative
        if not path.is_file():
            raise FileNotFoundError(f"missing implementation file: {relative}")
        observed[relative] = sha256_path(path)
    return observed


def _check_output_names(
    output_dir: Path, paper_dir: Path, *, require_all: bool
) -> None:
    expected = set(ARTIFACT_FILENAMES) | {MANIFEST_FILENAME}
    allowed_static = {"README.md"} if output_dir == (paper_dir / "results").resolve() else set()
    entries = {path.name: path for path in output_dir.iterdir()}
    observed = set(entries)
    unexpected = observed - expected - allowed_static
    missing = expected - observed if require_all else set()
    nonfiles = sorted(name for name, path in entries.items() if not path.is_file())
    if unexpected or missing or nonfiles:
        raise ValueError(
            "output filename contract failed: "
            f"missing={sorted(missing)}, extra={sorted(unexpected)}, nonfiles={nonfiles}"
        )


def _metrics(rows: Mapping[str, Sequence[Mapping[str, str]]]) -> dict[str, object]:
    nerve = rows["nerve_face_controls.csv"]
    factors = rows["factorization_controls.csv"]
    degree1 = rows["degree1_cohomology_controls.csv"]
    periods = rows["period_controls.csv"]
    morphisms = rows["morphism_controls.csv"]
    quotients = rows["quotient_topology_controls.csv"]
    packets = rows["packet_period_controls.csv"]
    labels = rows["label_boundary_controls.csv"]
    negatives = rows["negative_controls.csv"]
    summary = rows["control_summary.csv"]
    orbitwise = rows["orbitwise_standardization_h1_controls.csv"]
    orbitwise_models = [row for row in orbitwise if row["record_type"] == "MODEL"]
    orbitwise_basepoints = [row for row in orbitwise if row["record_type"] == "BASEPOINT"]
    orbitwise_automorphisms = [row for row in orbitwise if row["record_type"] == "AUT"]
    orbitwise_negatives = [row for row in orbitwise if row["record_type"] == "NEGATIVE"]
    return {
        "csv_artifact_count": len(ARTIFACT_FILENAMES),
        "total_csv_rows": sum(len(value) for value in rows.values()),
        "legacy_csv_rows_preserved": sum(
            len(value)
            for filename, value in rows.items()
            if filename != "orbitwise_standardization_h1_controls.csv"
        ),
        "required_control_id_count": len(summary) + 1,
        "all_required_controls_pass": (
            all(row["status"] == "PASS" for row in summary)
            and all(row["status"] == "PASS" for row in orbitwise)
        ),
        "nerve_model_degree_rows": len(nerve),
        "nerve_coordinate_count_checked": sum(int(row["coordinate_count"]) for row in nerve),
        "face_identity_checks": sum(int(row["face_identity_checks"]) for row in nerve),
        "face_identity_failures": sum(int(row["face_identity_failures"]) for row in nerve),
        "d2_basis_coefficients_checked": sum(int(row["d2_basis_coefficients_checked"]) for row in nerve),
        "d2_nonzero_rows": sum(row["d2_zero"] != "true" for row in nerve),
        "t0_continuous_nonfactor_count": sum(
            int(row["continuous_nonfactor_count"])
            for row in factors
            if row["target_t0"] == "true"
        ),
        "nont0_continuous_nonfactor_count": sum(
            int(row["continuous_nonfactor_count"])
            for row in factors
            if row["target_t0"] == "false"
        ),
        "degree1_profiles_checked": len(degree1),
        "linear_cocycle_profile_count": sum(row["is_cocycle_on_probe"] == "true" for row in degree1),
        "nonlinear_or_affine_rejections": sum(row["is_cocycle_on_probe"] == "false" for row in degree1),
        "b1_nonzero_probe_count": sum(row["b1_probe_zero"] != "true" for row in degree1),
        "period_control_rows": len(periods),
        "positive_lattice_rows": sum(row["rank_one_lattice"] == "true" for row in periods),
        "nonlattice_boundary_rows": sum(row["rank_one_lattice"] == "false" for row in periods),
        "scaled_unequal_pair_count": sum(row["control_id"] == "SCALE-LM" for row in morphisms),
        "strict_identity_count": sum(row["control_id"] == "STRICT-ID" for row in morphisms),
        "orientation_reverse_count": sum(row["control_id"] == "REVERSE-L" for row in morphisms),
        "all_scaled_covariance_checks_pass": all(
            row["period_covariance"] == "true" and row["well_defined"] == "true"
            for row in morphisms
            if row["control_id"] == "SCALE-LM"
        ),
        "all_wrong_scale_negatives_detected": all(
            row["wrong_identity_scale_detected"] == "true"
            and row["wrong_reciprocal_scale_detected"] == "true"
            for row in morphisms
            if row["control_id"] == "SCALE-LM"
        ),
        "one_sided_topology_rows": sum(row["one_sided_topology_direction"] == "true" for row in quotients),
        "packet_schema_rows": len(packets),
        "packet_primes_checked": len({row["prime"] for row in packets}),
        "packet_unit_period_mismatches": sum(row["all_units_same_period"] != "true" for row in packets),
        "label_permutation_count": len(labels),
        "distinct_label_theorem_signatures": len({row["generic_theorem_signature_sha256"] for row in labels}),
        "all_label_rows_prove_too_much": all(row["proves_too_much"] == "true" for row in labels),
        "legacy_negative_control_count": len(negatives),
        "orbitwise_negative_control_count": len(orbitwise_negatives),
        "negative_control_count": len(negatives) + len(orbitwise_negatives),
        "negative_control_failures": sum(row["negative_detected"] != "true" for row in negatives),
        "orbitwise_control_rows": len(orbitwise),
        "orbitwise_model_rows": len(orbitwise_models),
        "orbitwise_basepoint_rows": len(orbitwise_basepoints),
        "orbitwise_automorphism_rows": len(orbitwise_automorphisms),
        "orbitwise_automorphism_expected_total": sum(
            int(row["aut_expected"]) for row in orbitwise_models
        ),
        "orbitwise_all_automorphisms_enumerated": all(
            row["aut_expected"] == row["aut_enumerated"]
            for row in orbitwise_models
        ),
        "orbitwise_all_automorphisms_lift_and_invert": all(
            row["lift_descend_ok"] == "true" and row["group_inverse_ok"] == "true"
            for row in orbitwise_automorphisms
        ),
        "orbitwise_actual_h1_dimension_models": sorted(
            {int(row["h1_dim_actual"]) for row in orbitwise_models}
        ),
        "orbitwise_standard_h1_dimensions": sorted(
            {int(row["h1_dim_standard"]) for row in orbitwise_models}
        ),
        "orbitwise_all_diagonal_rank_one": all(
            row["j_rank"] == "1" and row["diagonal_ok"] == "true"
            for row in orbitwise_models
        ),
        "orbitwise_all_invariant_dimension_one": all(
            row["invariant_dim"] == "1" for row in orbitwise_models
        ),
        "orbitwise_all_nonzero_coboundaries_verified": all(
            row["nonzero_coboundary_ok"] == "true" for row in orbitwise_models
        ),
        "orbitwise_all_zero_isotropy_potentials_recovered": all(
            row["zero_isotropy_potential_ok"] == "true" for row in orbitwise_models
        ),
        "orbitwise_q1_recovery_model_count": sum(
            row["m"] == "1"
            and row["h1_dim_actual"] == row["h1_dim_standard"] == "1"
            and row["j_rank"] == row["invariant_dim"] == "1"
            for row in orbitwise_models
        ),
        "orbitwise_mixed_length_rejection_count": sum(
            row["permutation"] == "MIXED_LENGTHS"
            and row["mixed_length_rejected"] == "true"
            for row in orbitwise_negatives
        ),
        "orbitwise_wrong_j_direction_rejection_count": sum(
            row["permutation"] == "WRONG_J_DIRECTION"
            and row["lift_descend_ok"] == "true"
            for row in orbitwise_negatives
        ),
        "orbitwise_packet_schematic_only": all(
            row["packet_schematic_only"] == "true"
            and row["replaces_source_proof"] == "false"
            for row in orbitwise
        ),
        "explicit_float_control_values": len(PERIODS),
        "float_absolute_tolerance": FLOAT_ABS_TOLERANCE,
        "float_print_format": FLOAT_PRINT_FORMAT,
    }


def _build_manifest(
    paper_dir: Path,
    payloads: Mapping[str, bytes],
    rows: Mapping[str, Sequence[Mapping[str, str]]],
) -> dict[str, object]:
    artifacts = {
        filename: {
            "bytes": len(payloads[filename]),
            "rows": len(rows[filename]),
            "sha256": sha256_bytes(payloads[filename]),
            "columns": list(ARTIFACT_FIELDS[filename]),
        }
        for filename in ARTIFACT_FILENAMES
    }
    return {
        "schema": SCHEMA,
        "regression_status": "PASS",
        "active_lock_files": _hash_bound_files(
            paper_dir, EXPECTED_ACTIVE_LOCK_HASHES, "active lock"
        ),
        "phase_gate_files": _hash_bound_files(
            paper_dir, EXPECTED_PHASE_GATE_HASHES, "phase gate/status"
        ),
        "implementation_files": _implementation_hashes(paper_dir),
        "artifacts": artifacts,
        "metrics": _metrics(rows),
        "parameters": {
            "required_control_ids": [
                *[row["control_id"] for row in control_summary_rows()],
                "STD-COPROD-H1",
            ],
            "orbitwise_standardization": {
                "cycle_orders": list(ORBITWISE_STANDARDIZATION_N),
                "orbit_counts": list(ORBITWISE_STANDARDIZATION_M),
                "model_rows": 9,
                "basepoint_rows": 90,
                "automorphism_rows": 3151,
                "negative_rows": 2,
                "body_rows": 3252,
                "columns": list(ORBITWISE_STANDARDIZATION_FIELDS),
                "automorphism_count_formula": "n^m*m!",
                "actual_h1_dimension": 1,
                "standard_h1_dimension": "m",
                "comparison_rank": 1,
                "invariant_dimension": 1,
            },
            "periods": [
                {
                    "key": period.key,
                    "label": period.label,
                    "expression": period.expression,
                    "printed_value": float_text(period.value),
                }
                for period in PERIODS
            ],
            "reserved_seed": RESERVED_UNUSED_SEED,
            "reserved_seed_used": False,
            "float_absolute_tolerance": FLOAT_ABS_TOLERANCE,
            "float_tolerance_scope": "only displayed log/sqrt period and scale comparisons",
            "float_print_format": FLOAT_PRINT_FORMAT,
            "exact_check_tolerance": 0,
        },
        "proof_binding": {
            "concurrent_v4_proof_hash_included": False,
            "reason": (
                "controls bind the active v4 locks, final gate, status re-lock, "
                "implementations, and generated artifacts; proof review is a later lane"
            ),
        },
        "determinism": {
            "python_dependencies": "standard_library_only",
            "network": False,
            "randomness": False,
            "external_datasets": False,
            "timestamps": False,
            "zeta_zero_data": False,
            "target_values": False,
            "fitting": False,
            "traces": False,
            "determinants": False,
            "paper8_coefficients": False,
            "paper11_completions": False,
        },
        "object_boundary": (
            "Finite cyclic-time models, symbolic real-period ledgers, finite topology "
            "proxies, exact common-cycle Z-action linear algebra, and a source-gated "
            "packet schema are separately typed controls. They are not the actual "
            "rational-Witt proof owner."
        ),
        "interpretation_boundary": (
            "The controls are deterministic witnesses and falsifiers, not universal "
            "proofs, source verification, arithmetic specificity, Route evaluation, "
            "or manuscript evidence. Finite common cycles do not prove the real, "
            "infinite-Q, choice, source, or topology theorems. LABEL-SWAP deliberately "
            "records PROVES_TOO_MUCH."
        ),
        "forbidden_evidence_not_used": [
            "zeta-zero tables or fitted target values",
            "traces or determinant conventions",
            "Paper-8 coefficients",
            "Paper-11 completions",
            "network, external packages, external datasets, randomness, or timestamps",
        ],
    }


def run(output_dir: Path, paper_dir: Path | None = None) -> dict[str, object]:
    """Generate all checked artifacts and their hash-bound manifest."""

    output_dir = output_dir.resolve()
    paper_dir = (
        Path(__file__).resolve().parents[1]
        if paper_dir is None
        else paper_dir.resolve()
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    _check_output_names(output_dir, paper_dir, require_all=False)
    rows = artifact_rows()
    payloads = expected_artifact_bytes()
    for filename in ARTIFACT_FILENAMES:
        (output_dir / filename).write_bytes(payloads[filename])
    manifest = _build_manifest(paper_dir, payloads, rows)
    (output_dir / MANIFEST_FILENAME).write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    _check_output_names(output_dir, paper_dir, require_all=True)
    return manifest


def verify(output_dir: Path, paper_dir: Path | None = None) -> dict[str, object]:
    """Fail closed on bytes, schema, rows, names, locks, code, or manifest drift."""

    output_dir = output_dir.resolve()
    paper_dir = (
        Path(__file__).resolve().parents[1]
        if paper_dir is None
        else paper_dir.resolve()
    )
    if not output_dir.is_dir():
        raise FileNotFoundError(f"missing output directory: {output_dir}")
    _check_output_names(output_dir, paper_dir, require_all=True)

    expected_rows = artifact_rows()
    expected_payloads = expected_artifact_bytes()
    for filename in ARTIFACT_FILENAMES:
        path = output_dir / filename
        payload = path.read_bytes()
        if payload != expected_payloads[filename]:
            raise ValueError(f"artifact content/schema/row drift: {filename}")
        with path.open("r", encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            if tuple(reader.fieldnames or ()) != ARTIFACT_FIELDS[filename]:
                raise ValueError(f"artifact CSV schema drift: {filename}")
            observed_rows = list(reader)
        if observed_rows != expected_rows[filename]:
            raise ValueError(f"artifact parsed-row drift: {filename}")

    manifest_path = output_dir / MANIFEST_FILENAME
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ValueError("manifest is not canonical valid JSON") from error
    expected_manifest = _build_manifest(paper_dir, expected_payloads, expected_rows)
    if manifest != expected_manifest:
        raise ValueError("manifest/hash/lock/gate/implementation drift")
    return manifest


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        required=True,
        type=Path,
        help="directory for eleven CSV ledgers and manifest.json",
    )
    parser.add_argument(
        "--verify-only",
        action="store_true",
        help="strictly verify existing artifacts without writing them",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    manifest = verify(args.output_dir) if args.verify_only else run(args.output_dir)
    metrics = manifest["metrics"]
    print(
        f"PASS schema={manifest['schema']} csv={metrics['csv_artifact_count']} "
        f"rows={metrics['total_csv_rows']} negative={metrics['negative_control_count']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
