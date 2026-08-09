#!/usr/bin/env python3
"""Nonimporting checker for the HCS-C22 T4/orbitwise-scalar certificate."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path
from typing import Sequence

import sympy as sp


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CERTIFICATE = PROJECT_ROOT / "results" / "c22_t4_certificate.json"
DEFAULT_OUTPUT = PROJECT_ROOT / "results" / "c22_t4_independent_check.json"
SOURCE_CERTIFICATE = PROJECT_ROOT / "results" / "c22_certificate.json"

ADJACENCY = (
    (1, 0, 1, 0),
    (1, 0, 0, 0),
    (0, 1, 0, 1),
    (0, 1, 0, 0),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", nargs="?", type=Path, default=DEFAULT_CERTIFICATE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def parse_fraction(value: object) -> Fraction:
    if isinstance(value, dict):
        value = value["fraction"]
    return Fraction(str(value))


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def divisors(value: int) -> list[int]:
    return [item for item in range(1, value + 1) if value % item == 0]


def rotations(values: Sequence[object]) -> list[tuple[object, ...]]:
    word = tuple(values)
    return [word[index:] + word[:index] for index in range(len(word))]


def least_period(values: Sequence[object]) -> int:
    word = tuple(values)
    for period in divisors(len(word)):
        if word == word[:period] * (len(word) // period):
            return period
    raise AssertionError(word)


def admissible(signs: Sequence[int]) -> bool:
    return all(
        not (signs[(index - 1) % len(signs)] == 1 and signs[(index + 1) % len(signs)] == 1)
        for index in range(len(signs))
    )


def canonical(pairs: Sequence[tuple[int, int]]) -> tuple[tuple[int, int], ...]:
    return min(rotations(tuple(pairs)))


def primitive_orbits(period: int) -> set[tuple[tuple[int, int], ...]]:
    found: set[tuple[tuple[int, int], ...]] = set()
    for parameters in itertools.product((0, 1), repeat=period):
        for signs in itertools.product((-1, 1), repeat=period):
            if not admissible(signs):
                continue
            pairs = tuple(zip(parameters, signs, strict=True))
            if least_period(pairs) == period:
                found.add(canonical(pairs))
    return found


def identifier(orbit: Sequence[tuple[int, int]]) -> str:
    return "".join(f"{parameter}{'+' if sign > 0 else '-'}" for parameter, sign in orbit)


def formal_weight(orbit: Sequence[tuple[int, int]]) -> Fraction:
    digest = hashlib.sha256(identifier(orbit).encode("ascii")).hexdigest()
    return Fraction(2 + int(digest[:12], 16) % 89, 97)


def value_digest(value: Fraction) -> str:
    return hashlib.sha256(fraction_text(value).encode("ascii")).hexdigest()


def reconstruct_formal_row(
    period: int,
    ledger: dict[int, set[tuple[tuple[int, int], ...]]],
) -> dict[str, object]:
    direct = Fraction(0)
    fixed_count = 0
    for parameters in itertools.product((0, 1), repeat=period):
        for signs in itertools.product((-1, 1), repeat=period):
            if not admissible(signs):
                continue
            pairs = tuple(zip(parameters, signs, strict=True))
            root_period = least_period(pairs)
            root = canonical(pairs[:root_period])
            direct += formal_weight(root) ** (period // root_period)
            fixed_count += 1

    primitive_sum = Fraction(0)
    for primitive_period in divisors(period):
        repetition = period // primitive_period
        primitive_sum += primitive_period * sum(
            (formal_weight(orbit) ** repetition for orbit in ledger[primitive_period]),
            Fraction(0),
        )
    return {
        "period": period,
        "fixed_joint_words": fixed_count,
        "primitive_orbits_at_period": len(ledger[period]),
        "direct_trace_sha256": value_digest(direct),
        "primitive_repetition_trace_sha256": value_digest(primitive_sum),
        "exact_equality": direct == primitive_sum,
    }


def check_source_binding(certificate: dict[str, object]) -> dict[str, bool]:
    inherited = certificate.get("inherited_t1_t3", {})
    source_exists = SOURCE_CERTIFICATE.exists()
    source_hash = hashlib.sha256(SOURCE_CERTIFICATE.read_bytes()).hexdigest() if source_exists else ""
    source_pass = False
    if source_exists:
        source = json.loads(SOURCE_CERTIFICATE.read_text(encoding="utf-8"))
        source_pass = all(source["decisions"].get(key) is True for key in ("t1_pass", "t2_pass", "t3_pass"))
    return {
        "source_exists": source_exists,
        "source_sha256": inherited.get("sha256") == source_hash,
        "source_declared_path": inherited.get("path") == "results/c22_certificate.json",
        "source_t1_t3_pass": source_pass and inherited.get("all_gates_pass") is True,
    }


def check_t4(certificate: dict[str, object]) -> dict[str, bool]:
    t4 = certificate.get("t4_intrinsic_instability_determinant", {})
    multiplier = t4.get("multiplier_bounds", {})
    holder = t4.get("holder_roof", {})
    counting = t4.get("counting", {})
    fixed_log = t4.get("fixed_log_identity", {})
    formal = fixed_log.get("formal_exact_regression", {})
    convergence = t4.get("normal_convergence", {})

    a_min = Fraction(59, 10)
    a_max = Fraction(61, 10)
    beta = Fraction(123, 112)
    gamma = Fraction(112, 123)
    kappa = Fraction(1, 2)
    denominator = 2 * a_min * Fraction(1, 3) - beta * kappa
    e_squared = denominator**2 / (1 + kappa**2)
    u_squared = (2 * a_max * Fraction(5, 8)) ** 2 + beta**2 + gamma**2
    graph_contraction = denominator ** -2
    coordinate_rate_squared = Fraction(240, 1003)

    matrix = sp.Matrix(ADJACENCY)
    z = sp.symbols("z")
    bare = sp.factor((sp.eye(8) - z * sp.kronecker_product(sp.ones(2), matrix)).det())
    charpoly = str(sp.factor(matrix.charpoly().as_expr()))

    rows = counting.get("rows", [])
    count_coverage = bool(rows) and [int(row["period"]) for row in rows] == list(range(1, len(rows) + 1))
    count_values = count_coverage
    primitive_counts: dict[int, int] = {}
    if count_coverage:
        for row in rows:
            n = int(row["period"])
            state_fixed = int(sp.trace(matrix**n))
            joint_fixed = (2**n) * state_fixed
            primitive_count = sum(
                int(sp.mobius(divisor))
                * (2 ** (n // divisor))
                * int(sp.trace(matrix ** (n // divisor)))
                for divisor in divisors(n)
            ) // n
            primitive_counts[n] = primitive_count
            reconstructed = sum(divisor * primitive_counts[divisor] for divisor in divisors(n))
            count_values &= (
                int(row["state_fixed"]) == state_fixed
                and int(row["joint_fixed"]) == joint_fixed
                and int(row["primitive_joint_orbits"]) == primitive_count
                and int(row["mobius_reconstruction"]) == reconstructed
                and row.get("pass") is True
            )

    formal_rows = formal.get("rows", [])
    formal_max = int(formal.get("max_period", 0))
    formal_coverage = formal_max >= 4 and [int(row["period"]) for row in formal_rows] == list(range(1, formal_max + 1))
    formal_values = formal_coverage
    if formal_coverage:
        ledger = {period: primitive_orbits(period) for period in range(1, formal_max + 1)}
        expected_rows = [reconstruct_formal_row(period, ledger) for period in range(1, formal_max + 1)]
        formal_values = formal_rows == expected_rows

    phi = (1 + sp.sqrt(5)) / 2
    e = sp.sqrt(sp.Rational(e_squared.numerator, e_squared.denominator))
    u = sp.sqrt(sp.Rational(u_squared.numerator, u_squared.denominator))
    radius_rows = convergence.get("radius_landmarks", [])
    expected_radius_rows = []
    for real_s in (-2, -1, 0, 1, 2):
        radius = (e**real_s if real_s >= 0 else u**real_s) / (2 * phi)
        expected_radius_rows.append(
            {
                "real_s": real_s,
                "guaranteed_radius_expression": str(radius),
                "guaranteed_radius_decimal": str(sp.N(radius, 45)),
            }
        )
    threshold = str(sp.N(sp.log(2 * phi) / sp.log(e), 45))

    return {
        "definition_and_repetition": t4.get("definition", {}).get("primitive_object") == "joint parameter-state cyclic orbit"
        and t4.get("definition", {}).get("reversal_quotiented") is False
        and t4.get("exact_repetition", {}).get("pass") is True,
        "multiplier_lower_exact": parse_fraction(multiplier.get("forward_denominator")) == denominator
        and parse_fraction(multiplier.get("lower_base_squared")) == e_squared
        and e_squared == Fraction(129299641, 14112000),
        "multiplier_upper_exact": parse_fraction(multiplier.get("upper_frobenius_base_squared")) == u_squared
        and u_squared == Fraction(11420060341, 189778176),
        "holder_rate_exact": parse_fraction(holder.get("projective_graph_contraction")) == graph_contraction
        and parse_fraction(holder.get("coordinate_cylinder_rate_squared")) == coordinate_rate_squared
        and graph_contraction**2 < coordinate_rate_squared
        and holder.get("projective_rate_below_coordinate_rate") is True
        and holder.get("finite_memory_claimed") is False,
        "count_coverage": count_coverage,
        "count_values": count_values,
        "spectral_polynomial": counting.get("state_characteristic_polynomial") == charpoly,
        "bare_s_zero_control": counting.get("local_bare_denominator") == str(bare)
        and sp.expand(bare - (1 - 2 * z - 8 * z**3 - 16 * z**4)) == 0,
        "formal_trace_coverage": formal_coverage,
        "formal_trace_values": formal_values and formal.get("pass") is True,
        "convergence_domain": convergence.get("domain") == "2*phi*abs(z)*chi(Re(s)) < 1"
        and convergence.get("normal_holomorphy") is True
        and convergence.get("zero_free_product") is True
        and convergence.get("continuation_beyond_pressure_domain_claimed") is False,
        "convergence_landmarks": radius_rows == expected_radius_rows
        and convergence.get("z_equals_one_requires_real_s_above") == threshold,
        "declared_t4_pass": t4.get("pass") is True,
    }


def expected_boundary(center: Fraction, radius: Fraction) -> dict[str, object]:
    cx, rx = Fraction(23, 48), Fraction(7, 48)
    a_term = cx**2 - center
    q0 = a_term**2 + 4 * cx**2 * rx**2 + rx**4 - 2 * a_term * rx**2
    q1 = 4 * cx * rx * (a_term + rx**2)
    q2 = 4 * a_term * rx**2
    vertex = None if q2 == 0 else -q1 / (2 * q2)
    outside = q2 <= 0 or vertex is None or not (-1 <= vertex <= 1)
    distances = {
        "inner": abs((cx - rx) ** 2 - center),
        "outer": abs((cx + rx) ** 2 - center),
    }
    label = min(distances, key=distances.get)
    return {
        "q0": q0,
        "q1": q1,
        "q2": q2,
        "vertex": "none" if vertex is None else fraction_text(vertex),
        "outside": outside,
        "label": label,
        "distance": distances[label],
        "gap": distances[label] - radius,
    }


def check_complex_domain(certificate: dict[str, object]) -> dict[str, bool]:
    domain = certificate.get("t5_common_complex_domain", {})
    cx, rx = Fraction(23, 48), Fraction(7, 48)
    cy, ry = Fraction(121, 256), Fraction(41, 256)
    expected_keys = {
        (Fraction(59, 10), -1, -1),
        (Fraction(59, 10), -1, 1),
        (Fraction(59, 10), 1, -1),
        (Fraction(61, 10), -1, -1),
        (Fraction(61, 10), -1, 1),
        (Fraction(61, 10), 1, -1),
    }
    rows = domain.get("rows", [])
    actual_keys = {
        (Fraction(str(row["parameter"])), int(row["left_endpoint_sign"]), int(row["right_endpoint_sign"]))
        for row in rows
    }
    row_values = actual_keys == expected_keys and len(rows) == 6
    gaps = []
    zero_clearances = []
    if row_values:
        for row in rows:
            parameter = Fraction(str(row["parameter"]))
            left = int(row["left_endpoint_sign"])
            right = int(row["right_endpoint_sign"])
            raw_center = 1 - left * cy - right * cx
            raw_radius = ry + rx
            center = raw_center / parameter
            radius = raw_radius / parameter
            boundary = expected_boundary(center, radius)
            declared_boundary = row["boundary"]
            correct = (
                parse_fraction(row["raw_center"]) == raw_center
                and parse_fraction(row["raw_radius"]) == raw_radius
                and parse_fraction(row["radicand_center"]) == center
                and parse_fraction(row["radicand_radius"]) == radius
                and parse_fraction(row["zero_clearance"]) == center - radius
                and row["center_root_inside_X"] is True
                and parse_fraction(declared_boundary["quadratic_q0"]) == boundary["q0"]
                and parse_fraction(declared_boundary["quadratic_q1"]) == boundary["q1"]
                and parse_fraction(declared_boundary["quadratic_q2"]) == boundary["q2"]
                and declared_boundary["vertex"] == boundary["vertex"]
                and declared_boundary["vertex_outside_or_concave"] == boundary["outside"]
                and declared_boundary["minimum_endpoint"] == boundary["label"]
                and parse_fraction(declared_boundary["minimum_boundary_distance"]) == boundary["distance"]
                and parse_fraction(declared_boundary["boundary_gap"]) == boundary["gap"]
                and boundary["gap"] > 0
                and row["pass"] is True
            )
            row_values &= correct
            gaps.append(boundary["gap"])
            zero_clearances.append(center - radius)

    minimum_gap = min(gaps) if gaps else Fraction(0)
    minimum_zero_clearance = min(zero_clearances) if zero_clearances else Fraction(0)
    nesting = ry - (abs(cx - cy) + rx)
    clearance = Fraction(4, 5) * minimum_gap
    derivative_squared = Fraction(4, 1) / (11 * Fraction(59, 10))
    two_variable_lipschitz_squared = 4 * derivative_squared
    return {
        "row_coverage": actual_keys == expected_keys and len(rows) == 6,
        "row_values": row_values,
        "nesting_margin": parse_fraction(domain.get("X_strictly_inside_Y_margin")) == nesting == Fraction(1, 128),
        "minimum_gap": parse_fraction(domain.get("minimum_squared_boundary_gap")) == minimum_gap == Fraction(7, 4392),
        "minimum_radicand_modulus": parse_fraction(domain.get("minimum_radicand_modulus"))
        == minimum_zero_clearance
        == Fraction(55, 488),
        "coordinate_clearance": parse_fraction(domain.get("minimum_coordinate_clearance")) == clearance == Fraction(7, 5490),
        "derivative_bound": parse_fraction(domain.get("derivative_squared_upper")) == derivative_squared == Fraction(40, 649)
        and derivative_squared < Fraction(1, 16)
        and domain.get("each_endpoint_derivative_below_one_quarter") is True
        and parse_fraction(domain.get("two_variable_sup_lipschitz_squared_upper"))
        == two_variable_lipschitz_squared
        == Fraction(160, 649)
        and domain.get("two_variable_contraction") is True,
        "declared_domain_pass": domain.get("common_two_letter_domain_pass") is True,
    }


def check_obstruction(certificate: dict[str, object]) -> dict[str, bool]:
    item = certificate.get("t5_orbitwise_scalar_trace_obstruction", {})
    t = sp.symbols("t", real=True)
    x = sp.symbols("x", real=True, positive=True)
    signed = sp.factor((4 - t**2) - (2 - t) ** 2)
    positive = sp.factor((t**2 - 4) - (t - 2) ** 2)
    negative = sp.factor((2 - t) ** 2 - (t**2 - 4))
    lifted_positive = sp.factor((x + 1) * (x**2 + 1) - (x - 1) ** 3)
    lifted_negative = sp.factor((x + 1) ** 3 - (x - 1) * (x**2 + 1))
    return {
        "signed_formula": item.get("signed_multiplicativity_mismatch") == str(signed)
        and sp.expand(signed + 2 * t * (t - 2)) == 0,
        "absolute_formula": item.get("positive_trace_absolute_gap") == str(positive)
        and item.get("negative_trace_absolute_gap") == str(negative)
        and sp.expand(positive - 4 * (t - 2)) == 0
        and sp.expand(negative + 4 * (t - 2)) == 0,
        "lifted_scalar_formula": item.get("projective_lift_return_eigenvalues")
        == "lambda,lambda^(-1),lambda^(-2)"
        and item.get("lifted_positive_multiplier_gap") == str(lifted_positive)
        and item.get("lifted_negative_multiplier_gap") == str(lifted_negative)
        and sp.expand(lifted_positive - 2 * (2 * x**2 - x + 1)) == 0
        and sp.expand(lifted_negative - 2 * (2 * x**2 + x + 1)) == 0
        and item.get("lifted_scalar_double_repeat_contradiction") is True,
        "structured_scope": item.get("matching_mode")
        == "orbitwise_fixed_point_summands"
        and item.get("independent_formal_orbit_markers") is True
        and item.get("aggregate_nonexistence_claimed") is False,
        "scoped_claim": item.get("orbitwise_scalar_denominator_cancellation_pass") is False
        and item.get("aggregate_scalar_fredholm_realization_excluded") is False
        and item.get("graded_exterior_algebra_superdeterminant_excluded") is False
        and item.get("arbitrary_nonlocal_operator_excluded") is False,
        "decision": item.get("decision") == "NO_GO_ORBITWISE_SCALAR_DENOMINATOR_CANCELLATION; PIVOT_TO_GRADED_RUELLE_COMPLEX",
        "declared_obstruction_pass": item.get("obstruction_pass") is True,
    }


def check_projective_domain(certificate: dict[str, object]) -> dict[str, bool]:
    item = certificate.get("t5_projective_lift_domain", {})
    cx, rx = Fraction(23, 48), Fraction(7, 48)
    beta, gamma = Fraction(123, 112), Fraction(112, 123)
    slope_radius = Fraction(1, 2)
    expected_parameters = (Fraction(59, 10), Fraction(61, 10))
    rows = item.get("rows", [])
    coverage = len(rows) == 2 and tuple(Fraction(str(row["parameter"])) for row in rows) == expected_parameters
    values = coverage
    clearances = []
    images = []
    derivatives = []
    if coverage:
        for row, parameter in zip(rows, expected_parameters, strict=True):
            center = 2 * parameter * cx
            radius = 2 * parameter * rx + beta * slope_radius
            clearance = center - radius
            image = gamma / clearance
            derivative = clearance ** -2
            values &= (
                parse_fraction(row["oriented_expansion_disk_center"]) == center
                and parse_fraction(row["oriented_expansion_disk_radius"]) == radius
                and parse_fraction(row["right_half_plane_clearance"]) == clearance
                and parse_fraction(row["projective_image_modulus_upper"]) == image
                and parse_fraction(row["projective_slope_derivative_upper"]) == derivative
                and row["strict_slope_self_map"] is True
                and row["strict_projective_contraction"] is True
                and row["principal_log_valid"] is True
                and row["pass"] is True
            )
            clearances.append(clearance)
            images.append(image)
            derivatives.append(derivative)
    minimum_clearance = min(clearances) if clearances else Fraction(0)
    maximum_image = max(images) if images else Fraction(0)
    maximum_derivative = max(derivatives) if derivatives else Fraction(0)
    return {
        "row_coverage": coverage,
        "row_values": values,
        "minimum_log_clearance": parse_fraction(item.get("minimum_log_sector_clearance"))
        == minimum_clearance
        == Fraction(11371, 3360),
        "image_and_clearance": parse_fraction(item.get("maximum_projective_image_modulus"))
        == maximum_image
        == Fraction(125440, 466211)
        and parse_fraction(item.get("slope_disk_image_clearance"))
        == slope_radius - maximum_image
        == Fraction(215331, 932422),
        "derivative_contraction": parse_fraction(item.get("maximum_projective_derivative"))
        == maximum_derivative
        == Fraction(11289600, 129299641),
        "unique_unstable_lift": item.get("periodic_lift_multiplicity") == 1
        and item.get("stable_projective_fixed_point_in_domain") is False,
        "holomorphic_log_convention": item.get("oriented_factor")
        == "j=-epsilon*c on the q-sign branch epsilon"
        and item.get("holomorphic_weight")
        == "g_s=exp(-s*Log(j)) with principal Log on the right half-plane",
        "declared_projective_pass": item.get("common_projective_log_domain_pass") is True,
    }


def check_decision(certificate: dict[str, object]) -> dict[str, bool]:
    decision = certificate.get("decision", {})
    return {
        "t4_pass": decision.get("t4_pass") is True,
        "common_domain_pass": decision.get("t5_common_complex_domain_pass") is True,
        "orbitwise_scalar_cancellation_fails": decision.get(
            "t5_orbitwise_scalar_denominator_cancellation_pass"
        )
        is False,
        "operator_claim_scoped": decision.get("c22_positive_operator_claim")
        == "ORBITWISE_GEOMETRIC_SCALAR_CONSTRUCTION_CLOSED; AGGREGATE_SCALAR_REALIZATION_NOT_EXCLUDED",
        "projective_log_domain_pass": decision.get("t5_projective_log_domain_pass") is True,
        "all_checks_declared": decision.get("all_certificate_checks_pass") is True,
        "graded_pivot": decision.get("next_form")
        == "graded exterior-algebra Ruelle-Lefschetz complex or stop",
    }


def check_declared_scope(certificate: dict[str, object]) -> dict[str, bool]:
    declared_scope = certificate.get("scope", {})
    expected_certified = [
        "exact instability repetition law",
        "primitive Euler product to fixed-point log-trace identity",
        "explicit nonzero normal-convergence and zero-free domain",
        "positive two-sided Holder instability roof",
        "common complex one-step pinning disks for both frozen letters",
        "common complex unstable-slope disk and holomorphic oriented multiplier logarithm",
        "unique unstable projective lift without stable-direction double counting",
        "orbitwise scalar trace-denominator repetition obstruction",
    ]
    expected_not_certified = [
        "analytic continuation beyond the pressure boundary",
        "nuclear realization of the pure instability determinant",
        "nonexistence of every aggregate scalar Fredholm representation",
        "graded exterior-algebra operator complex",
        "functional equation or arithmetic Euler product",
        "self-adjoint Hilbert-Polya operator",
    ]
    return {
        "structured_top_scope": declared_scope.get("scalar_obstruction")
        == {
            "matching_mode": "orbitwise_fixed_point_summands",
            "independent_formal_orbit_markers": True,
            "aggregate_nonexistence_claimed": False,
        },
        "exact_certified_scope": declared_scope.get("certified")
        == expected_certified,
        "exact_not_certified_scope": declared_scope.get("not_certified")
        == expected_not_certified,
    }


def main() -> None:
    args = parse_args()
    certificate_bytes = args.certificate.read_bytes()
    certificate = json.loads(certificate_bytes)
    source_checks = check_source_binding(certificate)
    t4_checks = check_t4(certificate)
    domain_checks = check_complex_domain(certificate)
    projective_checks = check_projective_domain(certificate)
    obstruction_checks = check_obstruction(certificate)
    decision_checks = check_decision(certificate)
    scope_checks = check_declared_scope(certificate)
    all_checks = {
        "source": source_checks,
        "t4": t4_checks,
        "common_complex_domain": domain_checks,
        "projective_lift_domain": projective_checks,
        "scalar_trace_obstruction": obstruction_checks,
        "decision": decision_checks,
        "scope": scope_checks,
    }
    passed = all(value for group in all_checks.values() for value in group.values())
    output = {
        "run_id": "HCS_C22_T4_T5_ORBITWISE_SCALAR_INDEPENDENT_CHECK_V2",
        "producer_path": str(args.certificate.relative_to(PROJECT_ROOT)),
        "producer_sha256": hashlib.sha256(certificate_bytes).hexdigest(),
        "checks": all_checks,
        "pass": passed,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "pass": passed}, indent=2))
    if not passed:
        raise SystemExit("independent T4/orbitwise-scalar T5 check failed")


if __name__ == "__main__":
    main()
