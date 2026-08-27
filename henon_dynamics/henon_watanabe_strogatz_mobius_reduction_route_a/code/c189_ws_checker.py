#!/usr/bin/env python3
"""Producer-independent exact checker for C189."""
from __future__ import annotations

from collections import Counter
from copy import deepcopy
from fractions import Fraction
from hashlib import sha256
from math import isqrt
import json
from pathlib import Path
import sys

DEFAULT = Path(__file__).resolve().parents[1] / "results/c189_ws_evidence.json"
EXPECTED_COMMIT = "4d7b214759f7ff982c0b19e662918acd307e0f58"

C = tuple[Fraction, Fraction]
CZ: C = (Fraction(0), Fraction(0))
CO: C = (Fraction(1), Fraction(0))
CI: C = (Fraction(0), Fraction(1))


def frac(text: str) -> Fraction:
    numerator, denominator = text.split("/")
    return Fraction(int(numerator), int(denominator))


def cs(value: C) -> list[str]:
    return [f"{value[0].numerator}/{value[0].denominator}", f"{value[1].numerator}/{value[1].denominator}"]


def cp(value: list[str]) -> C:
    return frac(value[0]), frac(value[1])


def c(re: int | Fraction = 0, im: int | Fraction = 0) -> C:
    return Fraction(re), Fraction(im)


def plus(x: C, y: C) -> C:
    return x[0] + y[0], x[1] + y[1]


def minus(x: C, y: C) -> C:
    return x[0] - y[0], x[1] - y[1]


def times(x: C, y: C) -> C:
    return x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0]


def star(x: C) -> C:
    return x[0], -x[1]


def norm2(x: C) -> Fraction:
    return x[0] ** 2 + x[1] ** 2


def over(x: C, y: C) -> C:
    denominator = norm2(y)
    if denominator == 0:
        raise ZeroDivisionError
    numerator = times(x, star(y))
    return numerator[0] / denominator, numerator[1] / denominator


def scaled(scalar: Fraction, x: C) -> C:
    return scalar * x[0], scalar * x[1]


def circle(parameter: Fraction) -> C:
    denominator = 1 + parameter * parameter
    return (1 - parameter * parameter) / denominator, 2 * parameter / denominator


def transform(z: C, alpha: C, rotation: C) -> C:
    return over(times(rotation, plus(z, alpha)), plus(CO, times(star(alpha), z)))


def ratio(a: C, b: C, cc: C, d: C) -> C:
    return over(times(minus(a, cc), minus(b, d)), times(minus(a, d), minus(b, cc)))


def first_unique(points: list[C]) -> list[C]:
    result: list[C] = []
    for point in points:
        if point not in result:
            result.append(point)
    return result


def multiplicities(points: list[C]) -> list[int]:
    return sorted(Counter(points).values(), reverse=True)


def payload_hash(data: dict) -> str:
    body = deepcopy(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def solve_three(inputs: list[C], outputs: list[C]) -> list[C]:
    """Solve a*z+b-c*w*z=w with d normalized to one."""
    matrix: list[list[C]] = []
    for z, w in zip(inputs, outputs, strict=True):
        matrix.append([z, CO, scaled(Fraction(-1), times(w, z)), w])
    for column in range(3):
        pivot = next((row for row in range(column, 3) if matrix[row][column] != CZ), None)
        if pivot is None:
            raise AssertionError("singular landmark system")
        matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
        divisor = matrix[column][column]
        matrix[column] = [over(entry, divisor) for entry in matrix[column]]
        for row in range(3):
            if row == column:
                continue
            coefficient = matrix[row][column]
            matrix[row] = [minus(matrix[row][j], times(coefficient, matrix[column][j])) for j in range(4)]
    return [matrix[row][3] for row in range(3)] + [CO]


PARAMETERS = [
    Fraction(-4), Fraction(-2), Fraction(-1), Fraction(-1, 2),
    Fraction(0), Fraction(1, 3), Fraction(2, 3), Fraction(1),
    Fraction(3, 2), Fraction(3), Fraction(5),
]
BASE_POINTS = [circle(value) for value in PARAMETERS]
MAPS = [
    (c(0, 0), circle(Fraction(0))),
    (c(Fraction(1, 3), Fraction(1, 5)), circle(Fraction(1, 2))),
    (c(Fraction(-1, 4), Fraction(1, 6)), circle(Fraction(-2, 3))),
    (c(Fraction(2, 7), Fraction(-1, 7)), circle(Fraction(3, 4))),
]


def expected_actions() -> dict[str, tuple[str, list[C], C, C]]:
    expected: dict[str, tuple[str, list[C], C, C]] = {}
    stratum_counts = {
        "sync": [8],
        "two_cluster": [4, 4],
        "three_cluster": [3, 3, 2],
        "four_cluster": [3, 2, 2, 1],
        "six_cluster": [2, 2, 1, 1, 1, 1],
    }
    for map_index, (alpha, rotation) in enumerate(MAPS):
        for n in range(4, 11):
            expected[f"generic_N{n}_map{map_index}"] = ("generic", BASE_POINTS[:n], alpha, rotation)
        for name, counts in stratum_counts.items():
            points = [BASE_POINTS[index] for index, count in enumerate(counts) for _ in range(count)]
            expected[f"stratum_{name}_map{map_index}"] = ("collision_stratum", points, alpha, rotation)
    return expected


CONSTANTS = [
    ("identity", Fraction(0), c(0, 0)),
    ("elliptic_real", Fraction(5), c(3, 0)),
    ("elliptic_complex_positive", Fraction(13), c(3, 4)),
    ("elliptic_complex_negative", Fraction(-13), c(3, 4)),
    ("parabolic_positive", Fraction(5), c(3, 4)),
    ("parabolic_negative", Fraction(-5), c(3, 4)),
    ("hyperbolic_real", Fraction(3), c(5, 0)),
    ("hyperbolic_complex", Fraction(-3), c(4, 3)),
]


def square_root(value: Fraction) -> Fraction:
    numerator, denominator = isqrt(value.numerator), isqrt(value.denominator)
    if numerator * numerator != value.numerator or denominator * denominator != value.denominator:
        raise AssertionError("non-square sentinel")
    return Fraction(numerator, denominator)


def check(path: Path) -> int:
    data = json.loads(path.read_text())
    assertions = 0

    def require(condition: bool) -> None:
        nonlocal assertions
        assertions += 1
        if not condition:
            raise AssertionError(f"assertion {assertions} failed")

    require(data["schema"] == "hcs-c189-ws-mobius-v1")
    require(data["payload_sha256"] == payload_hash(data))
    metadata = data["metadata"]
    require(metadata["candidate_id"] == "HCS-C189")
    require(metadata["evaluation_date"] == "2026-08-27")
    require(metadata["source_commit"] == EXPECTED_COMMIT)
    require(metadata["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER")
    require(metadata["target_tables_used"] == 0)
    require([source.get("doi") for source in metadata["primary_sources"]] == [
        "10.1016/0167-2789(94)90196-1", "10.1063/1.3247089", "10.1103/PhysRevLett.101.264103"
    ])

    frequencies = [Fraction(-3), Fraction(0), Fraction(5, 2)]
    forcings = [c(0, 0), c(1, 2), c(Fraction(-3, 2), Fraction(1, 3)), c(Fraction(5, 4), Fraction(-2, 3))]
    expected_local = {
        f"f{fi}_H{hi}_z{zi}": (frequency, forcing, BASE_POINTS[zi])
        for fi, frequency in enumerate(frequencies)
        for hi, forcing in enumerate(forcings)
        for zi in range(8)
    }
    require(len(data["local_riccati_rows"]) == 96)
    seen_local: set[str] = set()
    for row in data["local_riccati_rows"]:
        row_id = row["row_id"]
        require(row_id in expected_local and row_id not in seen_local)
        seen_local.add(row_id)
        frequency, forcing, z = expected_local[row_id]
        require(frac(row["frequency_f"]) == frequency)
        require(cp(row["forcing_H"]) == forcing)
        require(cp(row["circle_point_z"]) == z)
        velocity = frequency + times(forcing, star(z))[1]
        riccati = plus(scaled(frequency, times(CI, z)), scaled(Fraction(1, 2), minus(forcing, times(star(forcing), times(z, z)))))
        phase_form = times(CI, scaled(velocity, z))
        tangent = plus(times(star(z), riccati), times(z, star(riccati)))[0]
        require(frac(row["phase_velocity"]) == velocity)
        require(cp(row["riccati_velocity"]) == riccati)
        require(cp(row["phase_to_riccati_residual"]) == minus(phase_form, riccati) == CZ)
        require(frac(row["circle_tangent_residual"]) == tangent == 0)
        require(frac(row["circle_equation_residual"]) == norm2(z) - 1 == 0)
    require(seen_local == set(expected_local))

    expected_action = expected_actions()
    require(len(data["mobius_action_rows"]) == 48)
    seen_action: set[str] = set()
    cross_ratio_cells = 0
    reconstruction_rows = 0
    circle_cells = 0
    for row in data["mobius_action_rows"]:
        row_id = row["row_id"]
        require(row_id in expected_action and row_id not in seen_action)
        seen_action.add(row_id)
        kind, points, alpha, rotation = expected_action[row_id]
        images = [transform(point, alpha, rotation) for point in points]
        reps = first_unique(points)
        image_reps = [transform(point, alpha, rotation) for point in reps]
        require(row["kind"] == kind)
        require(row["N"] == len(points))
        require(cp(row["alpha"]) == alpha)
        require(cp(row["rotation"]) == rotation)
        require(frac(row["alpha_disk_margin"]) == 1 - norm2(alpha) > 0)
        expected_coefficients = [rotation, times(rotation, alpha), star(alpha), CO]
        require([cp(value) for value in row["projective_coefficients_a_b_c_d"]] == expected_coefficients)
        stored_points = [cp(value) for value in row["initial_points"]]
        stored_images = [cp(value) for value in row["image_points"]]
        require(stored_points == points)
        require(stored_images == images)
        require([frac(value) for value in row["initial_circle_residuals"]] == [0] * len(points))
        require([frac(value) for value in row["image_circle_residuals"]] == [0] * len(points))
        require(all(norm2(value) == 1 for value in points + images))
        require(row["initial_collision_partition"] == multiplicities(points))
        require(row["image_collision_partition"] == multiplicities(images) == multiplicities(points))
        require(row["distinct_clusters"] == len(reps))
        require(row["group_orbit_dimension"] == min(len(reps), 3))
        require(row["quotient_invariant_count"] == max(len(reps) - 3, 0))
        expected_indices = [points.index(rep) for rep in reps[:3]] if len(reps) >= 3 else []
        require(row["landmark_indices"] == expected_indices)
        require(row["three_landmark_reconstruction"] is (len(reps) >= 3))
        expected_invariants = []
        for cluster_index in range(3, len(reps)):
            initial = ratio(reps[cluster_index], reps[0], reps[1], reps[2])
            image = ratio(image_reps[cluster_index], image_reps[0], image_reps[1], image_reps[2])
            expected_invariants.append((cluster_index, initial, image))
        require(len(row["cross_ratio_invariants"]) == len(expected_invariants))
        for stored, (cluster_index, initial, image) in zip(row["cross_ratio_invariants"], expected_invariants, strict=True):
            require(stored["cluster_index"] == cluster_index)
            require(frac(stored["initial_value"]) == initial[0])
            require(frac(stored["image_value"]) == image[0] == initial[0])
            require(frac(stored["initial_imaginary_residual"]) == initial[1] == 0)
            require(frac(stored["image_imaginary_residual"]) == image[1] == 0)
        cross_ratio_cells += len(expected_invariants)
        circle_cells += 2 * len(points)
        if len(reps) >= 3:
            reconstruction_rows += 1
            recovered = solve_three(reps[:3], image_reps[:3])
            require(recovered == expected_coefficients)
    require(seen_action == set(expected_action))

    require(len(data["constant_generator_rows"]) == 8)
    rows_by_id = {row["case_id"]: row for row in data["constant_generator_rows"]}
    require(len(rows_by_id) == 8)
    for case_id, omega, forcing in CONSTANTS:
        require(case_id in rows_by_id)
        row = rows_by_id[case_id]
        delta = omega * omega - norm2(forcing)
        require(frac(row["omega"]) == omega)
        require(cp(row["H"]) == forcing)
        require(frac(row["delta_equals_omega2_minus_absH2"]) == delta)
        require(frac(row["generator_square_scalar"]) == -delta / 4)
        if omega == 0 and forcing == CZ:
            kind, roots, boundary, period = "identity", [], "all", None
        elif delta > 0:
            nu = square_root(delta)
            kind = "elliptic"
            roots = [over(c(0, omega + sign * nu), star(forcing)) for sign in (1, -1)]
            boundary, period = 0, Fraction(2, 1) / nu
        elif delta == 0:
            kind = "parabolic"
            roots = [over(c(0, omega), star(forcing))]
            boundary, period = 1, None
        else:
            kappa = square_root(-delta)
            kind = "hyperbolic"
            roots = [over(c(sign * kappa, omega), star(forcing)) for sign in (1, -1)]
            boundary, period = 2, None
        require(row["classification"] == kind)
        require(row["boundary_fixed_point_count"] == boundary)
        require((frac(row["elliptic_projective_period_pi_coefficient"]) if row["elliptic_projective_period_pi_coefficient"] is not None else None) == period)
        require(len(row["fixed_roots"]) == len(roots))
        for stored, root in zip(row["fixed_roots"], roots, strict=True):
            polynomial = minus(minus(times(star(forcing), times(root, root)), scaled(2 * omega, times(CI, root))), forcing)
            require(cp(stored["z"]) == root)
            require(frac(stored["modulus_square"]) == norm2(root))
            require(cp(stored["fixed_polynomial_residual"]) == polynomial == CZ)
        if kind == "elliptic":
            require(all(norm2(root) != 1 for root in roots))
        elif kind in {"parabolic", "hyperbolic"}:
            require(all(norm2(root) == 1 for root in roots))

    require(data["theorem"]["family"] == "all N>=3 and all continuous common f:I->R, H:I->C")
    require(data["theorem"]["elliptic_projective_period"] == "2*pi/sqrt(omega^2-|H|^2)")
    require(data["route_a"] == {
        "A0": "A0_FAIL", "A1": "A1_WEAK", "A2": "A2_FAIL", "A3": "A3_FAIL", "A4": "A4_FORMAL_HINT",
        "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False,
        "qualification": "exact PSU(1,1) reduction and clean periodic families have no intrinsic rational-prime origin, logarithmic prime clock, or target divisor",
    })
    summary = data["summary"]
    require(summary["local_riccati_rows"] == 96)
    require(summary["mobius_action_rows"] == 48)
    require(summary["generic_configuration_rows"] == 28)
    require(summary["collision_stratum_rows"] == 20)
    require(summary["cross_ratio_cells"] == cross_ratio_cells)
    require(summary["three_landmark_reconstruction_rows"] == reconstruction_rows)
    require(summary["circle_residual_cells"] == circle_cells)
    require(summary["constant_generator_rows"] == 8)
    require(summary["all_parameter_theorem_status"] == "PROVED_IN_THEOREM_PACKAGE")
    require(summary["finite_rows_role"] == "REGRESSION_ONLY")
    return assertions


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    assertions = check(path)
    print(json.dumps({
        "status": "C189_CHECKER_PASS",
        "assertions": assertions,
        "evidence_sha256": sha256(path.read_bytes()).hexdigest(),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
