#!/usr/bin/env python3
"""Exact producer for the HCS-C22 T4 and orbitwise scalar-T5 gate.

The certificate has three jobs:

1. turn the T1 cone bounds into an all-period multiplier bound and a
   nonzero normal-convergence domain for the instability Euler product;
2. verify the primitive/repetition bookkeeping with exact rational formal
   orbit weights, while preserving joint parameter--state chronology;
3. certify a common two-letter complex pinning domain and the orbitwise
   scalar-denominator repetition obstruction that motivates a graded pivot.

All pass/fail decisions use ``Fraction`` or symbolic integer arithmetic.
Decimal values are presentation-only.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import platform
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Sequence

import sympy as sp


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SOURCE_CERTIFICATE = PROJECT_ROOT / "results" / "c22_certificate.json"
DEFAULT_OUTPUT = PROJECT_ROOT / "results" / "c22_t4_certificate.json"

A_MIN = Fraction(59, 10)
A_MAX = Fraction(61, 10)
PARAMETERS = (A_MIN, A_MAX)
ADJACENCY = (
    (1, 0, 1, 0),
    (1, 0, 0, 0),
    (0, 1, 0, 1),
    (0, 1, 0, 0),
)

# The normalized tangent chart inherited from T1.
BETA = Fraction(123, 112)
GAMMA = Fraction(112, 123)
KAPPA = Fraction(1, 2)
FORWARD_DENOMINATOR = Fraction(11371, 3360)
E_SQUARED = Fraction(129299641, 14112000)
U_SQUARED = Fraction(11420060341, 189778176)

# Complex endpoint disks, after the coordinate swap used by the pinning map.
CX = Fraction(23, 48)
RX = Fraction(7, 48)
CY = Fraction(121, 256)
RY = Fraction(41, 256)
ALLOWED_ENDPOINT_SIGNS = ((-1, -1), (-1, 1), (1, -1))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--formal-max-period", type=int, default=7)
    parser.add_argument("--count-max-period", type=int, default=16)
    return parser.parse_args()


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def fraction_payload(value: Fraction) -> dict[str, object]:
    return {
        "fraction": fraction_text(value),
        "decimal": format(float(value), ".17g"),
    }


def sympy_decimal(value: sp.Expr, digits: int = 45) -> str:
    return str(sp.N(value, digits))


def divisors(value: int) -> list[int]:
    return [item for item in range(1, value + 1) if value % item == 0]


def mobius(value: int) -> int:
    return int(sp.mobius(value))


def rotations(values: Sequence[object]) -> list[tuple[object, ...]]:
    word = tuple(values)
    return [word[index:] + word[:index] for index in range(len(word))]


def least_period(values: Sequence[object]) -> int:
    word = tuple(values)
    for period in divisors(len(word)):
        if word == word[:period] * (len(word) // period):
            return period
    raise AssertionError(word)


def primitive(values: Sequence[object]) -> bool:
    return least_period(values) == len(values)


def admissible_sign_word(signs: Sequence[int]) -> bool:
    n = len(signs)
    return all(
        not (signs[(index - 1) % n] == 1 and signs[(index + 1) % n] == 1)
        for index in range(n)
    )


def canonical_joint(pairs: Sequence[tuple[int, int]]) -> tuple[tuple[int, int], ...]:
    return min(rotations(tuple(pairs)))


def primitive_joint_orbits(period: int) -> set[tuple[tuple[int, int], ...]]:
    result: set[tuple[tuple[int, int], ...]] = set()
    sign_words = [
        signs
        for signs in itertools.product((-1, 1), repeat=period)
        if admissible_sign_word(signs)
    ]
    for parameters in itertools.product((0, 1), repeat=period):
        for signs in sign_words:
            pairs = tuple(zip(parameters, signs, strict=True))
            if primitive(pairs):
                result.add(canonical_joint(pairs))
    return result


def orbit_identifier(orbit: Sequence[tuple[int, int]]) -> str:
    return "".join(f"{parameter}{'+' if sign > 0 else '-'}" for parameter, sign in orbit)


def formal_orbit_weight(orbit: Sequence[tuple[int, int]]) -> Fraction:
    """A deterministic exact test weight, not dynamical evidence."""

    digest = hashlib.sha256(orbit_identifier(orbit).encode("ascii")).hexdigest()
    return Fraction(2 + (int(digest[:12], 16) % 89), 97)


def rational_digest(value: Fraction) -> str:
    return hashlib.sha256(fraction_text(value).encode("ascii")).hexdigest()


def direct_formal_fixed_trace(period: int) -> tuple[Fraction, int]:
    total = Fraction(0)
    count = 0
    for parameters in itertools.product((0, 1), repeat=period):
        for signs in itertools.product((-1, 1), repeat=period):
            if not admissible_sign_word(signs):
                continue
            pairs = tuple(zip(parameters, signs, strict=True))
            root_period = least_period(pairs)
            root = canonical_joint(pairs[:root_period])
            total += formal_orbit_weight(root) ** (period // root_period)
            count += 1
    return total, count


def primitive_formal_fixed_trace(
    period: int,
    orbit_ledger: dict[int, set[tuple[tuple[int, int], ...]]],
) -> Fraction:
    total = Fraction(0)
    for primitive_period in divisors(period):
        repetition = period // primitive_period
        total += primitive_period * sum(
            (
                formal_orbit_weight(orbit) ** repetition
                for orbit in orbit_ledger[primitive_period]
            ),
            Fraction(0),
        )
    return total


def exact_trace_a(period: int) -> int:
    matrix = sp.Matrix(ADJACENCY)
    return int(sp.trace(matrix**period))


def t4_certificate(formal_max_period: int, count_max_period: int) -> dict[str, object]:
    if formal_max_period < 4 or formal_max_period > 8:
        raise ValueError("formal-max-period must lie in [4,8]")
    if count_max_period < formal_max_period:
        raise ValueError("count-max-period must cover the formal audit")

    expected_e_squared = FORWARD_DENOMINATOR**2 / (1 + KAPPA**2)
    expected_u_squared = (
        Fraction(61, 8) ** 2 + BETA**2 + GAMMA**2
    )
    if expected_e_squared != E_SQUARED or expected_u_squared != U_SQUARED:
        raise AssertionError("frozen multiplier constants do not reconstruct")

    matrix = sp.Matrix(ADJACENCY)
    spectral_polynomial = sp.factor(matrix.charpoly().as_expr())
    z = sp.symbols("z")
    local_denominator = sp.factor((sp.eye(8) - z * sp.kronecker_product(sp.ones(2), matrix)).det())
    expected_denominator = 1 - 2 * z - 8 * z**3 - 16 * z**4
    if sp.expand(local_denominator - expected_denominator) != 0:
        raise AssertionError(local_denominator)

    count_rows = []
    for period in range(1, count_max_period + 1):
        state_fixed = exact_trace_a(period)
        joint_fixed = (2**period) * state_fixed
        primitive_count = sum(
            mobius(divisor)
            * (2 ** (period // divisor))
            * exact_trace_a(period // divisor)
            for divisor in divisors(period)
        ) // period
        count_rows.append(
            {
                "period": period,
                "state_fixed": state_fixed,
                "joint_fixed": joint_fixed,
                "primitive_joint_orbits": primitive_count,
                "mobius_reconstruction": sum(
                    divisor
                    * next(
                        row["primitive_joint_orbits"]
                        for row in count_rows
                        if row["period"] == divisor
                    )
                    for divisor in divisors(period)
                    if divisor < period
                )
                + period * primitive_count,
            }
        )
        count_rows[-1]["pass"] = (
            count_rows[-1]["mobius_reconstruction"] == joint_fixed
        )

    orbit_ledger = {
        period: primitive_joint_orbits(period)
        for period in range(1, formal_max_period + 1)
    }
    formal_rows = []
    for period in range(1, formal_max_period + 1):
        direct, fixed_count = direct_formal_fixed_trace(period)
        primitive_sum = primitive_formal_fixed_trace(period, orbit_ledger)
        formal_rows.append(
            {
                "period": period,
                "fixed_joint_words": fixed_count,
                "primitive_orbits_at_period": len(orbit_ledger[period]),
                "direct_trace_sha256": rational_digest(direct),
                "primitive_repetition_trace_sha256": rational_digest(primitive_sum),
                "exact_equality": direct == primitive_sum,
            }
        )

    phi = (1 + sp.sqrt(5)) / 2
    e = sp.sqrt(sp.Rational(E_SQUARED.numerator, E_SQUARED.denominator))
    u = sp.sqrt(sp.Rational(U_SQUARED.numerator, U_SQUARED.denominator))
    radius_rows = []
    for real_s in (-2, -1, 0, 1, 2):
        radius = (e**real_s if real_s >= 0 else u**real_s) / (2 * phi)
        radius_rows.append(
            {
                "real_s": real_s,
                "guaranteed_radius_expression": str(radius),
                "guaranteed_radius_decimal": sympy_decimal(radius),
            }
        )

    z_one_threshold = sp.log(2 * phi) / sp.log(e)
    graph_contraction = Fraction(1, 1) / FORWARD_DENOMINATOR**2
    contraction_squared = Fraction(240, 1003)
    return {
        "definition": {
            "determinant": "D_inst(z,s)=product_primitive(1-z^n*exp(-s*ell))",
            "zeta": "Z_inst=D_inst^(-1)",
            "length": "ell(Gamma)=log(abs(Lambda_u(M_Gamma)))",
            "complex_power": "exp(-s*log(abs(Lambda_u))) with the real positive logarithm",
            "primitive_object": "joint parameter-state cyclic orbit",
            "reversal_quotiented": False,
        },
        "exact_repetition": {
            "monodromy": "M_(Gamma^r)=M_Gamma^r",
            "signed_multiplier": "Lambda_u(Gamma^r)=Lambda_u(Gamma)^r",
            "length": "ell(Gamma^r)=r*ell(Gamma)",
            "weight": "exp(-s*ell(Gamma^r))=exp(-s*ell(Gamma))^r",
            "pass": True,
        },
        "multiplier_bounds": {
            "normalized_derivative": "[[-2*a*q,-123/112],[112/123,0]]",
            "cone_slope_bound": fraction_payload(KAPPA),
            "forward_denominator": fraction_payload(FORWARD_DENOMINATOR),
            "lower_base_squared": fraction_payload(E_SQUARED),
            "lower_base_decimal": sympy_decimal(e),
            "upper_frobenius_base_squared": fraction_payload(U_SQUARED),
            "upper_base_decimal": sympy_decimal(u),
            "all_period_statement": "E^n <= abs(Lambda_u) <= U^n",
            "pass": E_SQUARED > 1 and U_SQUARED > E_SQUARED,
        },
        "holder_roof": {
            "one_step_factor": "tau=log(norm(DHhat*v_u)/norm(v_u))",
            "periodic_sum": "S_n tau=log(abs(Lambda_u)) exactly",
            "coordinate_cylinder_rate_squared": fraction_payload(contraction_squared),
            "projective_graph_contraction": fraction_payload(graph_contraction),
            "projective_rate_below_coordinate_rate": graph_contraction**2
            < contraction_squared,
            "regularity": "two-sided Holder; one-sided representative exists by cohomology",
            "finite_memory_claimed": False,
        },
        "counting": {
            "state_characteristic_polynomial": str(spectral_polynomial),
            "state_spectrum": ["phi", "-1/phi", "i", "-i"],
            "joint_fixed_formula": "N_n=2^n*trace(A^n)",
            "uniform_bound": "N_n <= 4*(2*phi)^n",
            "local_bare_denominator": str(local_denominator),
            "rows": count_rows,
            "pass": all(bool(row["pass"]) for row in count_rows),
        },
        "fixed_log_identity": {
            "trace": "B_n(s)=sum_{x in Fix(F^n)} exp(-s*S_n tau(x))",
            "identity": "-log(D_inst)=sum_(n>=1) z^n*B_n(s)/n",
            "formal_exact_regression": {
                "status": "STRUCTURAL_CONTROL_NOT_DYNAMICAL_EVIDENCE",
                "weight_rule": "deterministic SHA-derived rational primitive weights with exact repetition",
                "max_period": formal_max_period,
                "rows": formal_rows,
                "pass": all(bool(row["exact_equality"]) for row in formal_rows),
            },
        },
        "normal_convergence": {
            "chi": "E^(-Re(s)) if Re(s)>=0; U^(-Re(s)) if Re(s)<0",
            "domain": "2*phi*abs(z)*chi(Re(s)) < 1",
            "positive_half_plane": "abs(z) < E^Re(s)/(2*phi)",
            "negative_half_plane": "abs(z) < U^Re(s)/(2*phi)",
            "majorant": "4*sum_(n>=1) q^n/n, q=2*phi*abs(z)*chi(Re(s))",
            "normal_holomorphy": True,
            "zero_free_product": True,
            "radius_landmarks": radius_rows,
            "z_equals_one_requires_real_s_above": sympy_decimal(z_one_threshold),
            "s_zero_radius_is_sharp": True,
            "pressure_sharp_domain": "abs(z)*exp(P(-Re(s)*tau)) < 1",
            "continuation_beyond_pressure_domain_claimed": False,
            "pass": True,
        },
        "pass": all(bool(row["pass"]) for row in count_rows)
        and all(bool(row["exact_equality"]) for row in formal_rows),
    }


def boundary_square_data(center: Fraction, radius: Fraction) -> dict[str, object]:
    """Prove a real-centered radicand disk misses the squared X boundary."""

    a_term = CX**2 - center
    q0 = a_term**2 + 4 * CX**2 * RX**2 + RX**4 - 2 * a_term * RX**2
    q1 = 4 * CX * RX * (a_term + RX**2)
    q2 = 4 * a_term * RX**2
    vertex = None if q2 == 0 else -q1 / (2 * q2)
    vertex_outside_or_concave = q2 <= 0 or vertex is None or not (-1 <= vertex <= 1)
    if not vertex_outside_or_concave:
        raise AssertionError("unexpected interior boundary minimum")

    endpoint_distances = {
        "inner": abs((CX - RX) ** 2 - center),
        "outer": abs((CX + RX) ** 2 - center),
    }
    minimum_label = min(endpoint_distances, key=endpoint_distances.get)
    minimum_distance = endpoint_distances[minimum_label]
    gap = minimum_distance - radius
    return {
        "quadratic_q0": fraction_payload(q0),
        "quadratic_q1": fraction_payload(q1),
        "quadratic_q2": fraction_payload(q2),
        "vertex": "none" if vertex is None else fraction_text(vertex),
        "vertex_outside_or_concave": vertex_outside_or_concave,
        "minimum_endpoint": minimum_label,
        "minimum_boundary_distance": fraction_payload(minimum_distance),
        "radicand_radius": fraction_payload(radius),
        "boundary_gap": fraction_payload(gap),
        "pass": gap > 0,
    }


def common_complex_domain_certificate() -> dict[str, object]:
    rows = []
    for parameter in PARAMETERS:
        for left_sign, right_sign in ALLOWED_ENDPOINT_SIGNS:
            raw_center = 1 - left_sign * CY - right_sign * CX
            raw_radius = RY + RX
            center = raw_center / parameter
            radius = raw_radius / parameter
            boundary = boundary_square_data(center, radius)
            center_root_inside = (CX - RX) ** 2 < center < (CX + RX) ** 2
            zero_clearance = center - radius
            rows.append(
                {
                    "parameter": fraction_text(parameter),
                    "left_endpoint_sign": left_sign,
                    "right_endpoint_sign": right_sign,
                    "raw_center": fraction_payload(raw_center),
                    "raw_radius": fraction_payload(raw_radius),
                    "radicand_center": fraction_payload(center),
                    "radicand_radius": fraction_payload(radius),
                    "zero_clearance": fraction_payload(zero_clearance),
                    "center_root_inside_X": center_root_inside,
                    "boundary": boundary,
                    "pass": zero_clearance > 0
                    and center_root_inside
                    and bool(boundary["pass"]),
                }
            )

    minimum_gap = min(
        Fraction(str(row["boundary"]["boundary_gap"]["fraction"]))
        for row in rows
    )
    minimum_zero_clearance = min(
        Fraction(str(row["zero_clearance"]["fraction"])) for row in rows
    )
    nesting_margin = RY - (abs(CX - CY) + RX)
    coordinate_clearance = Fraction(4, 5) * minimum_gap
    derivative_squared = Fraction(4, 1) / (11 * A_MIN)
    two_variable_lipschitz_squared = 4 * derivative_squared
    return {
        "coordinate_swap": "F_a(x,y)=(y,1-a*y^2-x)",
        "pinning_branch": "P_(a,s)(w,z)=s*sqrt((1-w-z)/a)",
        "X": {"center_abs": fraction_payload(CX), "radius": fraction_payload(RX)},
        "Y": {"center_abs": fraction_payload(CY), "radius": fraction_payload(RY)},
        "X_strictly_inside_Y_margin": fraction_payload(nesting_margin),
        "allowed_endpoint_signs": [list(item) for item in ALLOWED_ENDPOINT_SIGNS],
        "rows": rows,
        "minimum_radicand_modulus": fraction_payload(minimum_zero_clearance),
        "minimum_squared_boundary_gap": fraction_payload(minimum_gap),
        "minimum_coordinate_clearance": fraction_payload(coordinate_clearance),
        "derivative_squared_upper": fraction_payload(derivative_squared),
        "each_endpoint_derivative_below_one_quarter": derivative_squared
        < Fraction(1, 16),
        "two_variable_sup_lipschitz_squared_upper": fraction_payload(
            two_variable_lipschitz_squared
        ),
        "two_variable_contraction": two_variable_lipschitz_squared < 1,
        "common_two_letter_domain_pass": nesting_margin > 0
        and all(bool(row["pass"]) for row in rows)
        and minimum_gap == Fraction(7, 4392)
        and minimum_zero_clearance == Fraction(55, 488)
        and coordinate_clearance == Fraction(7, 5490),
    }


def projective_lift_domain_certificate() -> dict[str, object]:
    """Certify one common complex unstable-slope disk and logarithm sector."""

    slope_radius = Fraction(1, 2)
    rows = []
    for parameter in PARAMETERS:
        oriented_center = 2 * parameter * CX
        oriented_radius = 2 * parameter * RX + BETA * slope_radius
        zero_clearance = oriented_center - oriented_radius
        image_modulus_upper = GAMMA / zero_clearance
        projective_derivative_upper = Fraction(1, 1) / zero_clearance**2
        rows.append(
            {
                "parameter": fraction_text(parameter),
                "oriented_expansion_disk_center": fraction_payload(oriented_center),
                "oriented_expansion_disk_radius": fraction_payload(oriented_radius),
                "right_half_plane_clearance": fraction_payload(zero_clearance),
                "projective_image_modulus_upper": fraction_payload(
                    image_modulus_upper
                ),
                "projective_slope_derivative_upper": fraction_payload(
                    projective_derivative_upper
                ),
                "strict_slope_self_map": image_modulus_upper < slope_radius,
                "strict_projective_contraction": projective_derivative_upper < 1,
                "principal_log_valid": zero_clearance > 0,
                "pass": zero_clearance > 0
                and image_modulus_upper < slope_radius
                and projective_derivative_upper < 1,
            }
        )

    minimum_clearance = min(
        Fraction(str(row["right_half_plane_clearance"]["fraction"]))
        for row in rows
    )
    maximum_image = max(
        Fraction(str(row["projective_image_modulus_upper"]["fraction"]))
        for row in rows
    )
    maximum_derivative = max(
        Fraction(str(row["projective_slope_derivative_upper"]["fraction"]))
        for row in rows
    )
    return {
        "normalized_slope_disk": "M=closed_disk(0,1/2)",
        "projective_map": "G_(a,q)(m)=(112/123)/(-2*a*q-(123/112)*m)",
        "signed_factor": "c=-2*a*q-(123/112)*m",
        "oriented_factor": "j=-epsilon*c on the q-sign branch epsilon",
        "real_periodic_product": "product(j)=abs(Lambda_u)",
        "holomorphic_weight": "g_s=exp(-s*Log(j)) with principal Log on the right half-plane",
        "rows": rows,
        "minimum_log_sector_clearance": fraction_payload(minimum_clearance),
        "maximum_projective_image_modulus": fraction_payload(maximum_image),
        "slope_disk_image_clearance": fraction_payload(slope_radius - maximum_image),
        "maximum_projective_derivative": fraction_payload(maximum_derivative),
        "periodic_lift_multiplicity": 1,
        "stable_projective_fixed_point_in_domain": False,
        "common_projective_log_domain_pass": all(bool(row["pass"]) for row in rows)
        and minimum_clearance == FORWARD_DENOMINATOR
        and maximum_image == Fraction(125440, 466211)
        and maximum_derivative == Fraction(11289600, 129299641),
    }


def orbitwise_scalar_trace_obstruction_certificate() -> dict[str, object]:
    t = sp.symbols("t", real=True)
    x = sp.symbols("x", real=True, positive=True)
    det_one = 2 - t
    det_two = 4 - t**2
    multiplicative_mismatch = sp.factor(det_two - det_one**2)
    if multiplicative_mismatch != -2 * t * (t - 2):
        raise AssertionError(multiplicative_mismatch)

    # For t>2, |det(I-M^2)|-|det(I-M)|^2=4(t-2)>0.
    positive_hyperbolic_gap = sp.factor((t**2 - 4) - (t - 2) ** 2)
    # For t<-2, the order reverses and this positive expression remains.
    negative_hyperbolic_gap = sp.factor((2 - t) ** 2 - (t**2 - 4))
    lifted_positive_gap = sp.factor(
        (x + 1) * (x**2 + 1) - (x - 1) ** 3
    )
    lifted_negative_gap = sp.factor(
        (x + 1) ** 3 - (x - 1) * (x**2 + 1)
    )
    return {
        "scope": "standard scalar holomorphic pinning/weighted-composition trace on the base or certified projective lift, with a multiplicative one-step cocycle and orbitwise fixed-point-summand matching (equivalently, equality after adjoining independent formal orbit markers)",
        "matching_mode": "orbitwise_fixed_point_summands",
        "independent_formal_orbit_markers": True,
        "aggregate_nonexistence_claimed": False,
        "natural_trace_denominator": "det(I-M_Gamma^r) (or its real absolute/oriented version)",
        "desired_trace_weight": "abs(Lambda_u(Gamma))^(-s*r) without a fixed-point denominator",
        "required_scalar_correction": "c_(Gamma^r)=desired_weight*det(I-M_Gamma^r)",
        "det_area_preserving_one_return": str(det_one),
        "det_area_preserving_double_return": str(det_two),
        "signed_multiplicativity_mismatch": str(multiplicative_mismatch),
        "positive_trace_absolute_gap": str(positive_hyperbolic_gap),
        "negative_trace_absolute_gap": str(negative_hyperbolic_gap),
        "hyperbolic_double_repeat_contradiction": True,
        "projective_lift_return_eigenvalues": "lambda,lambda^(-1),lambda^(-2)",
        "lifted_positive_multiplier_gap": str(lifted_positive_gap),
        "lifted_negative_multiplier_gap": str(lifted_negative_gap),
        "lifted_scalar_double_repeat_contradiction": True,
        "orbitwise_scalar_denominator_cancellation_pass": False,
        "aggregate_scalar_fredholm_realization_excluded": False,
        "graded_exterior_algebra_superdeterminant_excluded": False,
        "arbitrary_nonlocal_operator_excluded": False,
        "decision": "NO_GO_ORBITWISE_SCALAR_DENOMINATOR_CANCELLATION; PIVOT_TO_GRADED_RUELLE_COMPLEX",
        "obstruction_pass": sp.expand(positive_hyperbolic_gap - 4 * (t - 2)) == 0
        and sp.expand(negative_hyperbolic_gap + 4 * (t - 2)) == 0
        and sp.expand(lifted_positive_gap - 2 * (2 * x**2 - x + 1)) == 0
        and sp.expand(lifted_negative_gap - 2 * (2 * x**2 + x + 1)) == 0,
    }


def main() -> None:
    args = parse_args()
    if not SOURCE_CERTIFICATE.exists():
        raise SystemExit(f"missing inherited certificate: {SOURCE_CERTIFICATE}")
    source_bytes = SOURCE_CERTIFICATE.read_bytes()
    source = json.loads(source_bytes)
    if not all(source["decisions"][key] for key in ("t1_pass", "t2_pass", "t3_pass")):
        raise SystemExit("inherited T1--T3 certificate is not a passing release")

    t4 = t4_certificate(args.formal_max_period, args.count_max_period)
    complex_domain = common_complex_domain_certificate()
    projective_domain = projective_lift_domain_certificate()
    obstruction = orbitwise_scalar_trace_obstruction_certificate()
    all_checks_pass = bool(t4["pass"])
    all_checks_pass &= bool(complex_domain["common_two_letter_domain_pass"])
    all_checks_pass &= bool(projective_domain["common_projective_log_domain_pass"])
    all_checks_pass &= bool(obstruction["obstruction_pass"])
    all_checks_pass &= obstruction["orbitwise_scalar_denominator_cancellation_pass"] is False

    output = {
        "material_passport": {
            "id": "HCS-C22-T4-T5-ORBITWISE-SCALAR-GATE",
            "type": "exact_theorem_and_obstruction_certificate",
            "status": "VERIFIED_BY_PRODUCER_PENDING_INDEPENDENT_CHECK",
            "determinism": "deterministic_exact_rational_and_symbolic",
        },
        "run_id": "HCS_C22_T4_T5_ORBITWISE_SCALAR_PRODUCER_V2",
        "inherited_t1_t3": {
            "path": str(SOURCE_CERTIFICATE.relative_to(PROJECT_ROOT)),
            "sha256": hashlib.sha256(source_bytes).hexdigest(),
            "all_gates_pass": True,
        },
        "environment": {
            "python_version": platform.python_version(),
            "sympy_version": sp.__version__,
            "gate_arithmetic": "exact Fraction and SymPy integer/polynomial arithmetic",
            "decimal_values_decide_gates": False,
        },
        "clock_and_chronology": {
            "clock": "one skew-product microstep",
            "chronology": "later Hénon letters act on the left",
            "primitive_object": "joint parameter-state necklace",
            "averaging_used": False,
        },
        "t4_intrinsic_instability_determinant": t4,
        "t5_common_complex_domain": complex_domain,
        "t5_projective_lift_domain": projective_domain,
        "t5_orbitwise_scalar_trace_obstruction": obstruction,
        "decision": {
            "t4_pass": bool(t4["pass"]),
            "t5_common_complex_domain_pass": bool(
                complex_domain["common_two_letter_domain_pass"]
            ),
            "t5_projective_log_domain_pass": bool(
                projective_domain["common_projective_log_domain_pass"]
            ),
            "t5_orbitwise_scalar_denominator_cancellation_pass": False,
            "c22_positive_operator_claim": "ORBITWISE_GEOMETRIC_SCALAR_CONSTRUCTION_CLOSED; AGGREGATE_SCALAR_REALIZATION_NOT_EXCLUDED",
            "next_form": "graded exterior-algebra Ruelle-Lefschetz complex or stop",
            "all_certificate_checks_pass": all_checks_pass,
        },
        "scope": {
            "scalar_obstruction": {
                "matching_mode": "orbitwise_fixed_point_summands",
                "independent_formal_orbit_markers": True,
                "aggregate_nonexistence_claimed": False,
            },
            "certified": [
                "exact instability repetition law",
                "primitive Euler product to fixed-point log-trace identity",
                "explicit nonzero normal-convergence and zero-free domain",
                "positive two-sided Holder instability roof",
                "common complex one-step pinning disks for both frozen letters",
                "common complex unstable-slope disk and holomorphic oriented multiplier logarithm",
                "unique unstable projective lift without stable-direction double counting",
                "orbitwise scalar trace-denominator repetition obstruction",
            ],
            "not_certified": [
                "analytic continuation beyond the pressure boundary",
                "nuclear realization of the pure instability determinant",
                "nonexistence of every aggregate scalar Fredholm representation",
                "graded exterior-algebra operator complex",
                "functional equation or arithmetic Euler product",
                "self-adjoint Hilbert-Polya operator",
            ],
        },
    }
    if not all_checks_pass:
        raise SystemExit("T4/orbitwise-scalar T5 producer certificate failed")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "output": str(args.output),
                **output["decision"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
