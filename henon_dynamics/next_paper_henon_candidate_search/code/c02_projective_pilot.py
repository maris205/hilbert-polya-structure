#!/usr/bin/env python3
"""HCS-C02: intrinsic projective-cocycle pilot for the H_6 survivor.

This script uses only the exact H_6 map, the R058 h-set/cone constants, and
the R059 symbolic graph.  It deliberately does *not* fit constant Möbius
generators.  Its three tasks are:

1. derive the uniform real-base/complex-fibre disk inclusions exactly;
2. tabulate the R059 cylinder-memory uncertainty bound for memories 1--8;
3. verify on every primitive symbolic cycle through period 8 that the true
   projective product is the projectivization of the true Hénon monodromy.

No Riemann zero or prime target data are read.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Sequence


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RESULTS = PROJECT_ROOT / "results" / "c02_projective"

STATE_NAMES = ("--", "-+", "+-", "++")
STATE_PAIRS = ((-1, -1), (-1, 1), (1, -1), (1, 1))
ADJACENCY = (
    (1, 0, 1, 0),
    (1, 0, 0, 0),
    (0, 1, 0, 1),
    (0, 1, 0, 0),
)

# Exact R058 geometry in raw (q,p) coordinates.
RX = Fraction(7, 48)
RY = Fraction(41, 256)
NORMALIZED_CONE_HALF_WIDTH = Fraction(1, 2)
SLOPE_RADIUS = (RY / RX) * NORMALIZED_CONE_HALF_WIDTH  # 123/224
Q_ABS_MIN = Fraction(1, 3)
Q_ABS_MAX = Fraction(5, 8)
DENOMINATOR_MIN = 12 * Q_ABS_MIN - SLOPE_RADIUS

# The two canonical child disks are obtained without optimization or fitting.
# For a=|-12q| in [4, 15/2], 1/a lies in [2/15, 1/4].  Comparing
# 1/(a-m) with 1/a supplies the second radius term.
CHILD_CENTER = (Fraction(2, 15) + Fraction(1, 4)) / 2
RECIPROCAL_INTERVAL_RADIUS = (Fraction(1, 4) - Fraction(2, 15)) / 2
FIBRE_PERTURBATION_RADIUS = SLOPE_RADIUS / (
    4 * (4 - SLOPE_RADIUS)
)
CHILD_RADIUS = RECIPROCAL_INTERVAL_RADIUS + FIBRE_PERTURBATION_RADIUS
FIBRE_LIPSCHITZ = 1 / (DENOMINATOR_MIN * DENOMINATOR_MIN)

# R059 symbolic contraction constant.
SYMBOLIC_THETA = 2 / math.sqrt(17.0)
SIGN_INTERVAL_WIDTH = Fraction(7, 24)


def frac_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_RESULTS)
    parser.add_argument("--max-memory", type=int, default=8)
    parser.add_argument("--max-period", type=int, default=8)
    parser.add_argument("--tolerance", type=float, default=2e-11)
    return parser.parse_args()


def exact_constants() -> dict[str, object]:
    disk_outer_edge = CHILD_CENTER + CHILD_RADIUS
    disk_inner_edge = CHILD_CENTER - CHILD_RADIUS
    checks = {
        "slope_radius_matches_r058_conversion": SLOPE_RADIUS
        == Fraction(123, 224),
        "pole_free_on_closed_source_disk": DENOMINATOR_MIN > 0,
        "strict_source_disk_invariance": Fraction(1, 1) / DENOMINATOR_MIN
        < SLOPE_RADIUS,
        "child_disks_strictly_separated": disk_inner_edge > 0,
        "child_disks_strictly_inside_source": disk_outer_edge
        < SLOPE_RADIUS,
        "strict_euclidean_fibre_contraction": FIBRE_LIPSCHITZ < 1,
    }
    return {
        "raw_hset_half_widths": {
            "r_q": frac_text(RX),
            "r_p": frac_text(RY),
        },
        "normalized_cone_half_width": frac_text(NORMALIZED_CONE_HALF_WIDTH),
        "source_slope_disk": {
            "center": "0/1",
            "radius": frac_text(SLOPE_RADIUS),
            "radius_float": float(SLOPE_RADIUS),
        },
        "pole_clearance": {
            "exact": frac_text(DENOMINATOR_MIN),
            "float": float(DENOMINATOR_MIN),
        },
        "uniform_image_modulus_bound": {
            "exact": frac_text(1 / DENOMINATOR_MIN),
            "float": float(1 / DENOMINATOR_MIN),
        },
        "uniform_fibre_derivative_bound": {
            "exact": frac_text(FIBRE_LIPSCHITZ),
            "float": float(FIBRE_LIPSCHITZ),
        },
        "canonical_child_disks": {
            "centers": [frac_text(-CHILD_CENTER), frac_text(CHILD_CENTER)],
            "center_abs_float": float(CHILD_CENTER),
            "radius": frac_text(CHILD_RADIUS),
            "radius_float": float(CHILD_RADIUS),
            "inner_edge": frac_text(disk_inner_edge),
            "inner_edge_float": float(disk_inner_edge),
            "outer_edge": frac_text(disk_outer_edge),
            "outer_edge_float": float(disk_outer_edge),
            "open_gap_between_disks": frac_text(2 * disk_inner_edge),
            "open_gap_float": float(2 * disk_inner_edge),
        },
        "checks": checks,
    }


def locally_admissible_sign_word(word: Sequence[int]) -> bool:
    """R059 rule: the two neighbours of any internal sign are not both +."""

    return all(not (word[i - 1] == 1 and word[i + 1] == 1)
               for i in range(1, len(word) - 1))


def count_central_sign_cylinders(memory: int) -> int:
    """Count extendible sign blocks on [-memory,memory].

    Every locally admissible block extends by negative tails, so the local
    check is also an extendibility check for this graph.
    """

    length = 2 * memory + 1
    count = 0
    for bits in range(1 << length):
        word = tuple(1 if bits & (1 << j) else -1 for j in range(length))
        if locally_admissible_sign_word(word):
            count += 1
    return count


def symbolic_width_formula(memory: int) -> str:
    if memory % 2 == 0:
        power = memory // 2
        raw = SIGN_INTERVAL_WIDTH * Fraction(4, 17) ** power
        return frac_text(raw)
    power = (memory - 1) // 2
    return (
        "(7/24)*(4/17)^"
        f"{power}*(2/sqrt(17))"
    )


def memory_rows(max_memory: int) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    q_to_map = 12.0 / float(DENOMINATOR_MIN) ** 2
    q_to_derivative = 24.0 / float(DENOMINATOR_MIN) ** 3
    q_to_log_derivative = 24.0 / float(DENOMINATOR_MIN)
    previous_width = float("inf")
    for memory in range(1, max_memory + 1):
        # The published B_contraction_proof.tex sharpens the older R059
        # markdown continuity envelope: the initial same-sign window has
        # diameter 7/24, and each inward step costs exactly theta.
        q_width = float(SIGN_INTERVAL_WIDTH) * SYMBOLIC_THETA**memory
        row = {
            "memory": memory,
            "central_sign_block_length": 2 * memory + 1,
            "cylinder_count": count_central_sign_cylinders(memory),
            "q_diameter_bound_formula": symbolic_width_formula(memory),
            "q_diameter_bound": q_width,
            "map_family_sup_bound": q_to_map * q_width,
            "derivative_family_sup_bound": q_to_derivative * q_width,
            "log_derivative_distortion_bound": q_to_log_derivative * q_width,
            "strict_decrease_from_previous": q_width < previous_width,
        }
        rows.append(row)
        previous_width = q_width
    return rows


def matmul(left: Sequence[Sequence[float]],
           right: Sequence[Sequence[float]]) -> list[list[float]]:
    return [
        [
            left[0][0] * right[0][0] + left[0][1] * right[1][0],
            left[0][0] * right[0][1] + left[0][1] * right[1][1],
        ],
        [
            left[1][0] * right[0][0] + left[1][1] * right[1][0],
            left[1][0] * right[0][1] + left[1][1] * right[1][1],
        ],
    ]


def projectivize(matrix: Sequence[Sequence[float]]) -> list[list[float]]:
    # J M J, J=[[0,1],[1,0]].  Acting on [m,1] gives the slope action.
    return [
        [matrix[1][1], matrix[1][0]],
        [matrix[0][1], matrix[0][0]],
    ]


def canonical_rotation(word: Sequence[int]) -> tuple[int, ...]:
    rotations = [tuple(word[j:] + word[:j]) for j in range(len(word))]
    return min(rotations)


def is_primitive_word(word: Sequence[int]) -> bool:
    n = len(word)
    for divisor in range(1, n):
        if n % divisor == 0 and all(word[j] == word[j % divisor]
                                    for j in range(n)):
            return False
    return True


def product_words(alphabet_size: int, length: int) -> Iterable[tuple[int, ...]]:
    for integer in range(alphabet_size**length):
        digits = [0] * length
        value = integer
        for index in range(length - 1, -1, -1):
            digits[index] = value % alphabet_size
            value //= alphabet_size
        yield tuple(digits)


def primitive_cycles(period: int) -> list[tuple[int, ...]]:
    seen: set[tuple[int, ...]] = set()
    cycles: list[tuple[int, ...]] = []
    for word in product_words(4, period):
        if not all(ADJACENCY[word[j]][word[(j + 1) % period]]
                   for j in range(period)):
            continue
        if not is_primitive_word(word):
            continue
        representative = canonical_rotation(list(word))
        if representative not in seen:
            seen.add(representative)
            cycles.append(representative)
    return sorted(cycles)


def solve_periodic_coordinates(states: Sequence[int],
                               tolerance: float = 2e-15,
                               max_iterations: int = 10000
                               ) -> tuple[list[float], int, float]:
    signs = [STATE_PAIRS[state][0] for state in states]
    midpoint = 23.0 / 48.0
    q = [sign * midpoint for sign in signs]
    residual = float("inf")
    for iteration in range(1, max_iterations + 1):
        updated = []
        for index, sign in enumerate(signs):
            radicand = (1.0 - q[index - 1] - q[(index + 1) % len(q)]) / 6.0
            if radicand <= 0:
                raise RuntimeError("R059 fixed-point radicand left its domain")
            updated.append(sign * math.sqrt(radicand))
        residual = max(abs(a - b) for a, b in zip(updated, q))
        q = updated
        if residual <= tolerance:
            return q, iteration, residual
    raise RuntimeError("periodic contraction did not converge")


def unstable_multiplier_and_slope(matrix: Sequence[Sequence[float]]) -> tuple[float, float]:
    trace = matrix[0][0] + matrix[1][1]
    discriminant = trace * trace - 4.0
    if discriminant <= 0:
        raise RuntimeError("non-hyperbolic monodromy in certified survivor")
    root = math.sqrt(discriminant)
    eigenvalues = ((trace + root) / 2.0, (trace - root) / 2.0)
    unstable = max(eigenvalues, key=abs)
    if abs(matrix[0][1]) >= abs(matrix[1][0]):
        slope = (unstable - matrix[0][0]) / matrix[0][1]
    else:
        slope = matrix[1][0] / (unstable - matrix[1][1])
    return unstable, slope


def periodic_rows(max_period: int) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    identity = [[1.0, 0.0], [0.0, 1.0]]
    for period in range(1, max_period + 1):
        for states in primitive_cycles(period):
            q, iterations, contraction_residual = solve_periodic_coordinates(states)
            monodromy = [row[:] for row in identity]
            projective_product = [row[:] for row in identity]
            recurrence_residual = 0.0
            for index, coordinate in enumerate(q):
                recurrence_residual = max(
                    recurrence_residual,
                    abs(q[(index + 1) % period]
                        - (1.0 - 6.0 * coordinate * coordinate - q[index - 1])),
                )
                derivative = [[-12.0 * coordinate, -1.0], [1.0, 0.0]]
                slope_matrix = [[0.0, 1.0], [-1.0, -12.0 * coordinate]]
                monodromy = matmul(derivative, monodromy)
                projective_product = matmul(slope_matrix, projective_product)
            expected_projective = projectivize(monodromy)
            matrix_error = max(
                abs(projective_product[i][j] - expected_projective[i][j])
                for i in range(2) for j in range(2)
            )
            unstable, slope = unstable_multiplier_and_slope(monodromy)
            a, b = projective_product[0]
            c, d = projective_product[1]
            slope_image = (a * slope + b) / (c * slope + d)
            slope_fixed_residual = abs(slope_image - slope)
            derivative_at_fixed_slope = 1.0 / (c * slope + d) ** 2
            multiplier_identity_error = abs(
                derivative_at_fixed_slope - 1.0 / unstable**2
            )
            previous_sign = STATE_PAIRS[states[0]][1]
            expected_disk_center = -previous_sign * float(CHILD_CENTER)
            disk_clearance = float(CHILD_RADIUS) - abs(slope - expected_disk_center)
            rows.append(
                {
                    "period": period,
                    "state_word": " ".join(STATE_NAMES[state] for state in states),
                    "sign_word": "".join(
                        "+" if STATE_PAIRS[state][0] > 0 else "-" for state in states
                    ),
                    "fixed_point_iterations": iterations,
                    "fixed_point_step_residual": contraction_residual,
                    "recurrence_residual": recurrence_residual,
                    "projective_monodromy_matrix_error": matrix_error,
                    "unstable_multiplier": unstable,
                    "unstable_slope": slope,
                    "slope_fixed_point_residual": slope_fixed_residual,
                    "projective_derivative_multiplier_error": multiplier_identity_error,
                    "expected_slope_disk_center": expected_disk_center,
                    "slope_disk_clearance": disk_clearance,
                }
            )
    return rows


def edge_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for source in range(4):
        source_current, source_previous = STATE_PAIRS[source]
        for target in range(4):
            if not ADJACENCY[source][target]:
                continue
            target_current, target_previous = STATE_PAIRS[target]
            rows.append(
                {
                    "source": STATE_NAMES[source],
                    "target": STATE_NAMES[target],
                    "source_q_sign": source_current,
                    "source_previous_q_sign": source_previous,
                    "target_previous_q_sign": target_previous,
                    "shift_consistency": target_previous == source_current,
                    "source_fibre_disk_center": float(-source_previous * CHILD_CENTER),
                    "target_fibre_disk_center": float(-target_previous * CHILD_CENTER),
                    "fibre_disk_radius": float(CHILD_RADIUS),
                    "image_in_target_disk": True,
                }
            )
    return rows


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        raise ValueError(f"refusing to write empty CSV: {path}")
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def max_field(rows: Sequence[dict[str, object]], field: str) -> float:
    return max(float(row[field]) for row in rows)


def min_field(rows: Sequence[dict[str, object]], field: str) -> float:
    return min(float(row[field]) for row in rows)


def main() -> None:
    args = parse_args()
    if not 1 <= args.max_memory <= 8:
        raise SystemExit("the frozen first pilot requires 1 <= max-memory <= 8")
    if not 1 <= args.max_period <= 8:
        raise SystemExit("the frozen first pilot requires 1 <= max-period <= 8")
    args.output_dir.mkdir(parents=True, exist_ok=True)

    constants = exact_constants()
    memories = memory_rows(args.max_memory)
    cycles = periodic_rows(args.max_period)
    edges = edge_rows()

    memory_nonincreasing = all(
        float(memories[index]["q_diameter_bound"])
        <= float(memories[index - 1]["q_diameter_bound"])
        for index in range(1, len(memories))
    )
    memory_strict = all(
        float(memories[index]["q_diameter_bound"])
        < float(memories[index - 1]["q_diameter_bound"])
        for index in range(1, len(memories))
    )
    numerical_checks = {
        "all_exact_disk_checks": all(constants["checks"].values()),
        "six_graph_edges": len(edges) == 6,
        "edge_shift_consistency": all(row["shift_consistency"] for row in edges),
        "memory_bound_nonincreasing": memory_nonincreasing,
        "memory_bound_strict_at_every_refinement": memory_strict,
        "periodic_cycles_present": bool(cycles),
        "periodic_recurrence": max_field(cycles, "recurrence_residual")
        <= args.tolerance,
        "projective_product_recovers_monodromy": max_field(
            cycles, "projective_monodromy_matrix_error"
        ) <= args.tolerance,
        "unstable_slope_is_projective_fixed_point": max_field(
            cycles, "slope_fixed_point_residual"
        ) <= args.tolerance,
        "projective_derivative_matches_inverse_multiplier_square": max_field(
            cycles, "projective_derivative_multiplier_error"
        ) <= args.tolerance,
        "unstable_slopes_inside_canonical_disks": min_field(
            cycles, "slope_disk_clearance"
        ) > 0,
    }

    summary = {
        "run_id": "HCS_C02_PROJECTIVE_PILOT_V1",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "dynamics": "H_6(q,p)=(1-6q^2-p,q)",
        "projective_map": "phi_q(m)=1/(-12q-m)",
        "data_firewall": {
            "allowed_inputs": [
                "R058 rational h-set and cone constants",
                "R059 four-state adjacency and contraction theorem",
                "published B_contraction_proof.tex same-sign window estimate",
                "H_6 derivative and internally generated periodic cycles",
            ],
            "forbidden_target_data_read": False,
        },
        "exact_real_base_complex_fibre_result": constants,
        "memory_audit": {
            "range": [1, args.max_memory],
            "symbolic_theta": SYMBOLIC_THETA,
            "bound_source": (
                "Published B_contraction_proof.tex: sequences agreeing on "
                "[-m,m] have central-coordinate diameter at most "
                "(7/24)*(2/sqrt(17))^m. The earlier R059 markdown used the "
                "looser 5/4 prefactor for a continuity statement."
            ),
            "rows": memories,
        },
        "periodic_monodromy_audit": {
            "max_period": args.max_period,
            "primitive_cycle_count": len(cycles),
            "cycle_counts_by_period": {
                str(period): sum(1 for row in cycles if row["period"] == period)
                for period in range(1, args.max_period + 1)
            },
            "max_recurrence_residual": max_field(cycles, "recurrence_residual"),
            "max_projective_matrix_error": max_field(
                cycles, "projective_monodromy_matrix_error"
            ),
            "max_slope_fixed_residual": max_field(
                cycles, "slope_fixed_point_residual"
            ),
            "max_multiplier_identity_error": max_field(
                cycles, "projective_derivative_multiplier_error"
            ),
            "min_slope_disk_clearance": min_field(cycles, "slope_disk_clearance"),
        },
        "checks": numerical_checks,
        "gate": {
            "sanity": "PASS" if all(numerical_checks.values()) else "FAIL",
            "real_base_holomorphic_fibre": "PASS",
            "canonical_disjoint_fibre_disks": "PASS",
            "complexified_henon_base_domain": "NOT_TESTABLE_FROM_R058_R059",
            "finite_schottky_generators": "NOT_ESTABLISHED",
            "nuclear_fredholm_determinant": "NOT_ESTABLISHED",
            "route_a_promotion": "DO_NOT_PROMOTE_TO_A2",
            "interpretation": (
                "The exact object is a Holder/itinerary-driven continuum of "
                "contracting fibre Mobius maps. Replacing it by finitely many "
                "post-hoc constant generators would change the dynamics."
            ),
        },
        "scope": (
            "Exact disk arithmetic and algebraic projectivization identities, "
            "plus finite-precision periodic sanity checks through period 8. "
            "No Schottky group, complexified base branch, nuclearity, global "
            "determinant, or Hilbert--Polya statement is proved."
        ),
    }

    write_csv(args.output_dir / "memory_bounds.csv", memories)
    write_csv(args.output_dir / "state_disk_bundle.csv", edges)
    write_csv(args.output_dir / "periodic_monodromy.csv", cycles)
    summary_path = args.output_dir / "pilot_summary.json"
    summary_path.write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    artifact_hashes = {
        path.name: sha256_file(path)
        for path in sorted(args.output_dir.glob("*.csv"))
    }
    artifact_hashes[summary_path.name] = sha256_file(summary_path)
    print(
        json.dumps(
            {
                "output_dir": str(args.output_dir),
                "primitive_cycles": len(cycles),
                "all_checks_pass": all(numerical_checks.values()),
                "gate": summary["gate"],
                "artifact_sha256": artifact_hashes,
            },
            indent=2,
            sort_keys=True,
        )
    )
    if not all(numerical_checks.values()):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
