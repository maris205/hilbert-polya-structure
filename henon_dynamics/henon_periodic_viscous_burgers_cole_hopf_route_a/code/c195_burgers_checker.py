#!/usr/bin/env python3
"""Producer-independent exact checker for the C195 Burgers certificate."""
from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import sys

DEFAULT = Path(__file__).resolve().parents[1] / "results/c195_burgers_evidence.json"
EXPECTED_COMMIT = "c3a5b9bbb3b6d0881f395abe4a01accd322f69cb"
EXPECTED_EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"

Z = tuple[Fraction, Fraction]
Series = dict[int, Z]
ZZ: Z = (Fraction(0), Fraction(0))
ZU: Z = (Fraction(1), Fraction(0))


def f(text: str) -> Fraction:
    numerator, denominator = text.split("/")
    return Fraction(int(numerator), int(denominator))


def z(re: int | Fraction = 0, im: int | Fraction = 0) -> Z:
    return Fraction(re), Fraction(im)


def parse_z(value: list[str]) -> Z:
    return f(value[0]), f(value[1])


def zsum(left: Z, right: Z) -> Z:
    return left[0] + right[0], left[1] + right[1]


def zprod(left: Z, right: Z) -> Z:
    return left[0] * right[0] - left[1] * right[1], left[0] * right[1] + left[1] * right[0]


def zbar(value: Z) -> Z:
    return value[0], -value[1]


def ztimes(scalar: Fraction, value: Z) -> Z:
    return scalar * value[0], scalar * value[1]


def zpower(value: Z, exponent: int) -> Z:
    if exponent < 0:
        return zpower(zbar(value), -exponent)
    result = ZU
    for _ in range(exponent):
        result = zprod(result, value)
    return result


def rational_circle(parameter: Fraction) -> Z:
    denominator = 1 + parameter * parameter
    return (1 - parameter * parameter) / denominator, 2 * parameter / denominator


def compact(series: Series) -> Series:
    return {mode: value for mode, value in series.items() if value != ZZ}


def series_sum(left: Series, right: Series) -> Series:
    result = dict(left)
    for mode, value in right.items():
        result[mode] = zsum(result.get(mode, ZZ), value)
    return compact(result)


def series_times_scalar(series: Series, scalar: Fraction) -> Series:
    return compact({mode: ztimes(scalar, value) for mode, value in series.items()})


def convolution(left: Series, right: Series) -> Series:
    result: Series = {}
    for p, left_value in left.items():
        for q, right_value in right.items():
            result[p + q] = zsum(result.get(p + q, ZZ), zprod(left_value, right_value))
    return compact(result)


def dx(series: Series) -> Series:
    return compact({mode: zprod(z(0, mode), value) for mode, value in series.items()})


def difference(left: Series, right: Series) -> Series:
    return series_sum(left, series_times_scalar(right, Fraction(-1)))


def parse_series(rows: list[dict]) -> Series:
    modes = [row["mode"] for row in rows]
    if len(modes) != len(set(modes)) or modes != sorted(modes):
        raise AssertionError("series modes must be unique and sorted")
    return compact({row["mode"]: parse_z(row["coefficient"]) for row in rows})


def exact_generator_residual(w: Series, viscosity: Fraction, mean: Fraction) -> Series:
    a = dx(w)
    b = dx(a)
    cc = dx(b)
    wt = series_sum(series_times_scalar(b, viscosity), series_times_scalar(a, -mean))
    at = dx(wt)
    time_part = series_times_scalar(convolution(difference(convolution(at, w), convolution(a, wt)), w), -2 * viscosity)
    u_numerator = series_sum(series_times_scalar(w, mean), series_times_scalar(a, -2 * viscosity))
    ux_core = difference(convolution(b, w), convolution(a, a))
    transport_part = series_times_scalar(convolution(u_numerator, ux_core), -2 * viscosity)
    uxx_core = series_sum(
        difference(convolution(convolution(cc, w), w), series_times_scalar(convolution(convolution(a, b), w), 3)),
        series_times_scalar(convolution(convolution(a, a), a), 2),
    )
    viscous_part = series_times_scalar(uxx_core, 2 * viscosity * viscosity)
    return series_sum(series_sum(time_part, transport_part), viscous_part)


def evolve(w: Series, rho: Fraction, rotation: Z) -> Series:
    result: Series = {}
    for mode, value in w.items():
        result[mode] = ztimes(rho ** (mode * mode), zprod(zpower(rotation, mode), value))
    return compact(result)


def positivity_bound(w: Series) -> Fraction:
    return w[0][0] - sum(abs(value[0]) + abs(value[1]) for mode, value in w.items() if mode)


def expected_case(index: int) -> tuple[Fraction, Fraction, Series]:
    viscosity_options = tuple(map(Fraction, (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), 1, Fraction(3, 2), 2)))
    mean_options = tuple(map(Fraction, (-2, -1, 0, Fraction(1, 2), Fraction(3, 2), 3)))
    viscosity = viscosity_options[index % 6]
    mean = mean_options[(5 * index + 1) % 6]
    r = 1 + index % 4
    modes = (r, r + 2) if index % 2 == 0 else (r, r + 1, r + 3)
    w: Series = {0: z(5 + index % 4)}
    for slot, mode in enumerate(modes):
        coefficient = z(
            Fraction(1 + (index + 2 * slot) % 4, 20 + mode + index % 3),
            Fraction(((index + mode + slot) % 5) - 2, 31 + mode + slot),
        )
        w[mode] = coefficient
        w[-mode] = zbar(coefficient)
    return viscosity, mean, w


def content_hash(data: dict) -> str:
    body = deepcopy(data)
    body.pop("payload_sha256", None)
    encoded = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(encoded).hexdigest()


def check(path: Path) -> int:
    data = json.loads(path.read_text())
    assertions = 0

    def require(condition: bool) -> None:
        nonlocal assertions
        assertions += 1
        if not condition:
            raise AssertionError(f"C195 independent assertion {assertions} failed")

    require(data["schema"] == "hcs-c195-periodic-burgers-v1")
    require(data["payload_sha256"] == content_hash(data))
    metadata = data["metadata"]
    require(metadata["candidate_id"] == "HCS-C195")
    require(metadata["evaluation_date"] == "2026-08-27")
    require(metadata["source_commit"] == EXPECTED_COMMIT)
    require(metadata["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER")
    require(metadata["evaluator_sha256"] == EXPECTED_EVALUATOR)
    require(metadata["target_tables_used"] == 0)
    require(len(metadata["primary_sources"]) == 2)
    require(metadata["primary_sources"][0]["doi"] == "10.1002/cpa.3160030302")
    require(metadata["primary_sources"][1]["jstor"] == "43633894")

    theorem = data["theorem"]
    require("s>3/2" in theorem["phase_leaf"] and "nu>0" in theorem["phase_leaf"] and "L>0" in theorem["phase_leaf"])
    require("min(w)>0" in theorem["positive_projective_cone"])
    require(theorem["cole_hopf_map"] == "Phi_m([w])=m-2*nu*d_x(log w)")
    require("mean(V)=0" in theorem["inverse"])
    require("nu*d_x^2-m*d_x" in theorem["autonomous_conjugacy"])
    require("x-m*t" in theorem["galilean_heat_relation"])
    require("universal two-parameter heat/translation multiplier" in theorem["algebraic_snapshot_oracle"])
    require("rational sentinel need not lie on that curve" in theorem["algebraic_snapshot_oracle"])
    require("2*pi*r/L" in theorem["asymptotic_exponent"])
    require("lambda_k=-nu*(2*pi*k/L)^2-i*m*(2*pi*k/L)" in theorem["linearized_spectrum"])
    require("only equilibrium, periodic point, or recurrent point" in theorem["recurrence"])

    rows = data["regression_rows"]
    require(len(rows) == 24)
    require([row["case_id"] for row in rows] == [f"trig_{index:02d}" for index in range(24)])
    reality_cells = 0
    spectrum_cells = 0
    for index, row in enumerate(rows):
        viscosity, mean, expected_w = expected_case(index)
        require(row["normalization"] == "L=2*pi; Fourier basis exp(i*k*x)")
        require(f(row["nu"]) == viscosity > 0)
        require(f(row["mean_m"]) == mean)
        stored_w = parse_series(row["initial_coefficients"])
        require(stored_w == expected_w)
        active = sorted(mode for mode in expected_w if mode > 0)
        require([parse_z(value) for value in row["reality_residual_cells"]] == [ZZ] * len(active))
        for mode in active:
            require(expected_w[-mode] == zbar(expected_w[mode]))
        reality_cells += len(active)
        margin = positivity_bound(expected_w)
        require(f(row["strict_positive_l1_margin"]) == margin > 0)

        stored_residual = parse_series(row["generator_residual_coefficients"])
        recomputed_residual = exact_generator_residual(expected_w, viscosity, mean)
        require(stored_residual == recomputed_residual == {})

        rho = f(row["snapshot_parameters"]["rho"])
        rotation = parse_z(row["snapshot_parameters"]["rotation"])
        require(0 < rho < 1)
        require(zprod(rotation, zbar(rotation)) == ZU)
        expected_snapshot = evolve(expected_w, rho, rotation)
        require(parse_series(row["snapshot_coefficients"]) == expected_snapshot)
        snapshot_margin = positivity_bound(expected_snapshot)
        require(f(row["snapshot_strict_positive_l1_margin"]) == snapshot_margin > 0)

        rho_second = f(row["second_snapshot_parameters"]["rho"])
        rotation_second = parse_z(row["second_snapshot_parameters"]["rotation"])
        require(0 < rho_second < 1)
        require(zprod(rotation_second, zbar(rotation_second)) == ZU)
        composed = evolve(expected_snapshot, rho_second, rotation_second)
        direct = evolve(expected_w, rho * rho_second, zprod(rotation, rotation_second))
        require(composed == direct)
        require(parse_series(row["composed_snapshot_coefficients"]) == composed)
        require(parse_series(row["direct_composed_snapshot_coefficients"]) == direct)
        require(parse_series(row["semigroup_composition_residual_coefficients"]) == {})

        first_mode, next_mode = active[:2]
        require(row["first_active_mode"] == first_mode)
        require(row["next_active_mode"] == next_mode)
        leading: Series = {}
        for mode in (-first_mode, first_mode):
            leading[mode] = ztimes(-2 * viscosity / expected_w[0][0], zprod(z(0, mode), expected_w[mode]))
        require(parse_series(row["leading_u_minus_m_coefficients"]) == leading)
        require(f(row["exact_decay_exponent"]) == viscosity * first_mode * first_mode)
        remainder = min(2 * viscosity * first_mode * first_mode, viscosity * next_mode * next_mode)
        require(f(row["certified_remainder_exponent"]) == remainder > viscosity * first_mode * first_mode)

        spectrum = row["linearized_spectrum"]
        require(len(spectrum) == 17)
        require([item["mode"] for item in spectrum] == list(range(-8, 9)))
        for item in spectrum:
            mode = item["mode"]
            require(parse_z(item["eigenvalue"]) == z(-viscosity * mode * mode, -mean * mode))
            require(item["fixed_mean_leaf"] is (mode != 0))
        spectrum_cells += len(spectrum)

    route = data["route_a"]
    require([route[key] for key in ("A0", "A1", "A2", "A3", "A4")] == [
        "A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"
    ])
    require(route["overall"] == "ROUTE_A_REJECTED")
    require(route["route_b_invocation_allowed"] is False)
    require("no intrinsic rational-prime carrier" in route["qualification"])

    summary = data["summary"]
    require(summary["regression_cases"] == 24)
    require(summary["generator_residual_rows"] == 24)
    require(summary["reality_residual_cells"] == reality_cells == 60)
    require(summary["positive_margin_rows"] == 24)
    require(summary["snapshot_positive_margin_rows"] == 24)
    require(summary["semigroup_identity_rows"] == 24)
    require(summary["leading_mode_rows"] == 24)
    require(summary["linear_spectrum_cells"] == spectrum_cells == 408)
    require(summary["all_parameter_theorem_status"] == "PROVED_IN_THEOREM_PACKAGE")
    require(summary["finite_rows_role"] == "REGRESSION_ONLY_NOT_PROOF")
    return assertions


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    assertions = check(path)
    print(json.dumps({"status": "C195_CHECKER_PASS", "assertions": assertions, "path": str(path)}, sort_keys=True))


if __name__ == "__main__":
    main()
