#!/usr/bin/env python3
"""Exact/symbolic producer for HCS-C19.

The certified object is the genus-three scalar curve of a period-seven
carrier.  A companion exact subresultant certificate reconstructs its generic
Hénon seven-cycle and ordered-edge chronological lift; finite-prime good
reduction and Hilbert--Pólya claims remain outside this producer.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path

import galois
import numpy as np
import sympy as sp


SCHEMA = "HCS-C19-producer-1"
PRIMES = (5, 11, 13)


def orbit_polynomial() -> tuple[sp.Symbol, sp.Symbol, sp.Expr, sp.Expr]:
    """Return (x, sigma, a, P) without importing any stored result."""
    x, sigma = sp.symbols("x sigma")
    a = sigma**2 - 2 * sigma
    p = (
        x**7
        - sigma * x**6
        - (3 * a - 2 * sigma) * x**5
        - (2 * a - (3 * a - 4) * sigma - 4) * x**4
        + (3 * a**2 - 2 * (2 * a - 1) * sigma + 1) * x**3
        + (
            4 * a**2
            - 10 * a
            - (3 * a**2 - 8 * a + 1) * sigma
            - 2
        )
        * x**2
        - (a - 1) * (a**2 - 2 * a * sigma + a + 2) * x
        - 2 * a**3
        + 6 * a**2
        + 2 * a
        + 3
        + (a**3 - 4 * a**2 + a - 2) * sigma
    )
    return x, sigma, a, sp.expand(p)


def weighted_initial_form(
    expr: sp.Expr,
    variables: tuple[sp.Symbol, sp.Symbol],
    weights: tuple[int, int],
) -> sp.Expr:
    poly = sp.Poly(sp.expand(expr), *variables)
    terms = poly.terms()
    minimum = min(sum(e * w for e, w in zip(exponents, weights)) for exponents, _ in terms)
    return sp.factor(
        sum(
            coefficient
            * sp.prod(v**e for v, e in zip(variables, exponents))
            for exponents, coefficient in terms
            if sum(e * w for e, w in zip(exponents, weights)) == minimum
        )
    )


def symbolic_certificate() -> dict:
    x, sigma, a, p = orbit_polynomial()
    correction_block = a**3 - 4 * a**2 + a - 2
    printed_p = sp.expand(p - (3 + correction_block * sigma) + 3 * correction_block * sigma)
    q6 = (
        64 * sigma**6
        - 448 * sigma**5
        + 848 * sigma**4
        + 80 * sigma**3
        - 1048 * sigma**2
        + 152 * sigma
        - 151
    )
    discriminant = sp.factor(sp.discriminant(p, x))
    expected_discriminant = (4 * sigma - 9) ** 2 * q6**3
    if sp.expand(discriminant - expected_discriminant) != 0:
        raise AssertionError("period-seven discriminant identity failed")

    # A single irreducible specialization proves generic irreducibility,
    # because P is monic in x.  The displayed F_2 polynomial is recorded.
    specialization = sp.Poly(p.subs(sigma, -3), x, modulus=2)
    if not specialization.is_irreducible:
        raise AssertionError("irreducibility witness failed")

    q6_disc = sp.factor(sp.discriminant(q6, sigma))
    if q6_disc != 2**63 * 97:
        raise AssertionError("unexpected branch-polynomial discriminant")
    if not sp.Poly(q6, sigma, domain=sp.QQ).is_irreducible:
        raise AssertionError("Q6 is not irreducible over Q")

    # At each Q6-root the gcd of P and P_x has degree three.  P_s does not
    # vanish there, hence these are three smooth simple ramification points.
    subresultants = sp.subresultants(p, sp.diff(p, x), x)
    qpoly = sp.Poly(q6, sigma, domain=sp.QQ)
    degrees_vanishing_mod_q6: list[int] = []
    last_nonzero_degree = None
    for sub in subresultants:
        coefficients = sp.Poly(sub, x).all_coeffs()
        reduced = [sp.Poly(c, sigma, domain=sp.QQ).rem(qpoly).as_expr() for c in coefficients]
        if all(c == 0 for c in reduced):
            degrees_vanishing_mod_q6.append(int(sp.degree(sub, x)))
        else:
            last_nonzero_degree = int(sp.degree(sub, x))
    if last_nonzero_degree != 3 or degrees_vanishing_mod_q6 != [2, 1, 0]:
        raise AssertionError("Q6 subresultant pattern failed")

    resultant_sigma = sp.factor(sp.resultant(p, sp.diff(p, sigma), x))
    singular_projection_gcd = sp.factor(
        sp.gcd(
            sp.Poly(discriminant, sigma, domain=sp.QQ),
            sp.Poly(resultant_sigma, sigma, domain=sp.QQ),
        ).as_expr()
    )
    if sp.expand(16 * singular_projection_gcd - (4 * sigma - 9) ** 2) != 0:
        raise AssertionError("finite singularity projection changed")

    # The exceptional finite discriminant value is an ordinary node.  Its
    # two tangent slopes are defined over Q(sqrt(-7)); the base parameter is
    # a uniformizer on both normalization branches, so it is not ramified.
    t, y = sp.symbols("t y")
    node_local = sp.expand(p.subs({sigma: t + sp.Rational(9, 4), x: y + sp.Rational(1, 4)}))
    tangent_cone = weighted_initial_form(node_local, (t, y), (1, 1))
    expected_tangent = -(137 * t**2 - 10 * t * y + y**2) / 8
    if sp.expand(tangent_cone - expected_tangent) != 0:
        raise AssertionError("node tangent cone failed")
    tangent_discriminant = sp.factor(sp.discriminant(sp.Poly(tangent_cone, y), y))
    if tangent_discriminant != -7 * t**2:
        raise AssertionError("node tangent discriminant failed")

    # Infinity chart: t=1/sigma, y=x/sigma.  Blow-up initial forms exhibit
    # seven distinct formal branches, each with t as a uniformizer.
    infinity = sp.cancel(t**7 * p.subs({sigma: 1 / t, x: y / t}))
    infinity_fibre = sp.factor(infinity.subs(t, 0))
    if infinity_fibre != (y - 1) ** 4 * (y + 1) ** 3:
        raise AssertionError("infinity fibre failed")
    z, w = sp.symbols("z w")
    plus_initial = weighted_initial_form(infinity.subs(y, 1 + z), (t, z), (1, 1))
    minus_initial = weighted_initial_form(infinity.subs(y, -1 + z), (t, z), (1, 1))
    plus_double_initial = weighted_initial_form(
        infinity.subs(y, 1 - t + w), (t, w), (1, 2)
    )
    minus_double_initial = weighted_initial_form(
        infinity.subs(y, -1 + t + w), (t, w), (1, 2)
    )
    expected_initials = {
        "plus": 8 * z * (t + z) ** 2 * (2 * t + z),
        "minus": 16 * (-2 * t + z) * (-t + z) ** 2,
        "plus_double": -4 * t**2 * w * (t**2 + 2 * w),
        "minus_double": -8 * t * (t**2 - 2 * w) * (t**2 - w),
    }
    actual_initials = {
        "plus": plus_initial,
        "minus": minus_initial,
        "plus_double": plus_double_initial,
        "minus_double": minus_double_initial,
    }
    for key in expected_initials:
        if sp.expand(actual_initials[key] - expected_initials[key]) != 0:
            raise AssertionError(f"infinity initial form failed: {key}")

    infinity_discriminant = sp.factor(sp.discriminant(infinity, y))
    infinity_discriminant_order = sp.Poly(infinity_discriminant, t).terms()[-1][0][0]
    if infinity_discriminant_order != 22:
        raise AssertionError("infinity discriminant order failed")

    degree = 7
    finite_ramification = 6 * 3
    twice_genus_minus_two = -2 * degree + finite_ramification
    genus = (twice_genus_minus_two + 2) // 2
    if genus != 3:
        raise AssertionError("Riemann-Hurwitz genus failed")
    arithmetic_genus = (7 - 1) * (7 - 2) // 2
    node_delta = 1
    infinity_delta = infinity_discriminant_order // 2
    if arithmetic_genus - node_delta - infinity_delta != genus:
        raise AssertionError("plane-septic delta cross-check failed")

    # The printed Eq. (16) has 3 multiplying the final parenthesis.  That
    # literal reading is inconsistent with an exact a=6 modular orbit audit.
    # The corrected constant used above passes it.  This is a source-correction
    # certificate, not a claim that the journal has issued an erratum.
    printed_discriminant = sp.factor(sp.discriminant(printed_p, x))
    if sp.degree(printed_discriminant, sigma) != 42:
        raise AssertionError("literal printed discriminant degree changed")
    modulus = 103
    fixed_a = 6
    fixed_sigma = 26
    expected_coordinates = {10, 17, 31, 54, 58, 67, 98}
    corrected_roots = {
        value
        for value in range(modulus)
        if int(p.subs({sigma: fixed_sigma, x: value})) % modulus == 0
    }
    printed_roots = {
        value
        for value in range(modulus)
        if int(printed_p.subs({sigma: fixed_sigma, x: value})) % modulus == 0
    }
    cycles = [
        [(10, 54), (58, 10), (31, 58), (17, 31), (98, 17), (67, 98), (54, 67)],
        [(10, 58), (54, 10), (67, 54), (98, 67), (17, 98), (31, 17), (58, 31)],
    ]

    def henon(state: tuple[int, int]) -> tuple[int, int]:
        q, previous = state
        return ((fixed_a - q * q - previous) % modulus, q)

    if (fixed_sigma**2 - 2 * fixed_sigma) % modulus != fixed_a:
        raise AssertionError("modular chiral relation failed")
    for cycle in cycles:
        if any(henon(cycle[index]) != cycle[(index + 1) % 7] for index in range(7)):
            raise AssertionError("modular Hénon cycle failed")
        if sum(q for q, _ in cycle) % modulus != fixed_sigma:
            raise AssertionError("modular orbit sum failed")
    if corrected_roots != expected_coordinates or printed_roots == expected_coordinates:
        raise AssertionError("source correction witness failed")
    if set(cycles[1]) != {(previous, q) for q, previous in cycles[0]}:
        raise AssertionError("modular reversal pair failed")

    return {
        "parameter_relation": "a = sigma^2 - 2*sigma",
        "orbit_polynomial": str(p),
        "source_correction": {
            "status": "EXACT_SPECIALIZATION_CERTIFIED_APPARENT_PRINT_ERROR",
            "printed_equation_literal_constant": "-2*a^3 + 6*a^2 + 2*a + 3*(a^3 - 4*a^2 + a - 2)*sigma",
            "adopted_dynamical_constant": "-2*a^3 + 6*a^2 + 2*a + 3 + (a^3 - 4*a^2 + a - 2)*sigma",
            "printed_discriminant_degree_in_sigma": 42,
            "exact_witness": {
                "field": "F_103",
                "a": fixed_a,
                "sigma": fixed_sigma,
                "cycles": cycles,
                "corrected_coordinate_roots": sorted(corrected_roots),
                "literal_printed_roots": sorted(printed_roots),
                "cycles_are_reversal_pair": True,
            },
            "journal_erratum_claimed": False,
        },
        "degree_over_sigma_line": degree,
        "generic_irreducibility": {
            "status": "PROVED",
            "specialization_sigma": -3,
            "modulus": 2,
            "polynomial": str(specialization.as_expr()),
            "irreducible": True,
        },
        "discriminant_x": str(discriminant),
        "branch_polynomial_q6": str(q6),
        "branch_polynomial_discriminant": str(q6_disc),
        "q6_irreducible": True,
        "q6_ramification": {
            "branch_values": 6,
            "ramification_points_per_value": 3,
            "ramification_index": 2,
            "smoothness": "P_sigma is nonzero at the repeated roots",
            "subresultant_last_nonzero_degree": last_nonzero_degree,
        },
        "finite_node": {
            "sigma": "9/4",
            "x": "1/4",
            "tangent_cone": str(tangent_cone),
            "tangent_discriminant": str(tangent_discriminant),
            "type": "ordinary node",
            "ramification_after_normalization": 0,
        },
        "infinity": {
            "special_fibre": str(infinity_fibre),
            "formal_branch_count": 7,
            "rational_branches": True,
            "ramification": 0,
            "discriminant_order": infinity_discriminant_order,
            "total_delta_invariant": infinity_delta,
            "initial_forms": {key: str(value) for key, value in actual_initials.items()},
        },
        "riemann_hurwitz": {
            "degree": degree,
            "total_ramification": finite_ramification,
            "twice_genus_minus_two": twice_genus_minus_two,
            "genus": genus,
        },
        "plane_genus_cross_check": {
            "arithmetic_genus": arithmetic_genus,
            "finite_node_delta": node_delta,
            "infinity_delta": infinity_delta,
            "geometric_genus": genus,
        },
        "orientation_boundary": {
            "full_chronology_claimed": False,
            "reason": "Henon time is constructed on the companion ordered-edge cover but does not act on this scalar quotient",
        },
    }


def coefficients(field, sigma):
    """Coefficients of P in descending x-degree over a galois field."""
    p = field.characteristic
    c = lambda n: field(n % p)
    a = sigma * sigma - c(2) * sigma
    return (
        c(1),
        -sigma,
        -(c(3) * a - c(2) * sigma),
        -(c(2) * a - (c(3) * a - c(4)) * sigma - c(4)),
        c(3) * a**2 - c(2) * (c(2) * a - c(1)) * sigma + c(1),
        c(4) * a**2
        - c(10) * a
        - (c(3) * a**2 - c(8) * a + c(1)) * sigma
        - c(2),
        -(a - c(1)) * (a**2 - c(2) * a * sigma + a + c(2)),
        -c(2) * a**3
        + c(6) * a**2
        + c(2) * a
        + c(3)
        + (a**3 - c(4) * a**2 + a - c(2)) * sigma,
    )


def affine_count(p: int, extension_degree: int) -> tuple[int, bool]:
    field = galois.GF(p**extension_degree)
    xs = field.elements
    total = 0
    for sigma in xs:
        coeffs = coefficients(field, sigma)
        values = field.Zeros(xs.shape) + coeffs[0]
        for coefficient in coeffs[1:]:
            values = values * xs + coefficient
        total += int(np.count_nonzero(values == 0))
    minus_seven = field((-7) % p)
    node_splits = bool(minus_seven ** ((field.order - 1) // 2) == 1)
    return total, node_splits


def l_polynomial(p: int, counts: list[int]) -> tuple[list[int], list[int]]:
    power_sums = [p**r + 1 - counts[r - 1] for r in (1, 2, 3)]
    s1, s2, s3 = power_sums
    e1 = s1
    e2 = (e1 * s1 - s2) // 2
    e3 = (s3 - e1 * s2 + e2 * s1) // 3
    coeffs = [1, -e1, e2, -e3, p * e2, p**2 * (-e1), p**3]
    return power_sums, coeffs


def predicted_counts(p: int, coeffs: list[int], maximum_degree: int = 6) -> list[int]:
    """Use Newton identities for L(T)=prod(1-alpha_i*T)."""
    power_sums: list[int] = []
    degree = len(coeffs) - 1
    for k in range(1, maximum_degree + 1):
        convolution = sum(coeffs[j] * power_sums[k - j - 1] for j in range(1, k))
        if k <= degree:
            value = -(convolution + k * coeffs[k])
        else:
            value = -sum(coeffs[j] * power_sums[k - j - 1] for j in range(1, degree + 1))
        power_sums.append(value)
    return [p**r + 1 - power_sums[r - 1] for r in range(1, maximum_degree + 1)]


def frobenius_certificate() -> list[dict]:
    t = sp.symbols("T")
    x_symbol, sigma_symbol, _, p_symbol = orbit_polynomial()
    q6_symbol = (
        64 * sigma_symbol**6
        - 448 * sigma_symbol**5
        + 848 * sigma_symbol**4
        + 80 * sigma_symbol**3
        - 1048 * sigma_symbol**2
        + 152 * sigma_symbol
        - 151
    )
    discriminant_symbol = sp.discriminant(p_symbol, x_symbol)
    resultant_sigma_symbol = sp.resultant(p_symbol, sp.diff(p_symbol, sigma_symbol), x_symbol)
    rows = []
    for p in PRIMES:
        q_mod = sp.Poly(q6_symbol, sigma_symbol, modulus=p)
        q6_squarefree = sp.gcd(q_mod, q_mod.diff()).degree() == 0
        node_disjoint = int(q_mod.eval((9 * pow(4, -1, p)) % p)) % p != 0
        singular_gcd = sp.gcd(
            sp.Poly(discriminant_symbol, sigma_symbol, modulus=p),
            sp.Poly(resultant_sigma_symbol, sigma_symbol, modulus=p),
        )
        expected_node = sp.Poly((4 * sigma_symbol - 9) ** 2, sigma_symbol, modulus=p).monic()
        only_expected_affine_node = singular_gcd.monic() == expected_node
        if not (q6_squarefree and node_disjoint and only_expected_affine_node):
            raise AssertionError(f"normalization-model screen failed at p={p}")
        affine_counts: list[int] = []
        normalized_counts: list[int] = []
        node_splitting: list[bool] = []
        for r in (1, 2, 3):
            affine, splits = affine_count(p, r)
            # Seven rational normalization branches lie above infinity.  The
            # rational node is replaced by 2 rational points if split and by
            # 0 rational points if nonsplit.
            normalized = affine + 7 + (1 if splits else -1)
            affine_counts.append(affine)
            normalized_counts.append(normalized)
            node_splitting.append(splits)
        power_sums, coeffs = l_polynomial(p, normalized_counts)
        counts_r1_r6 = predicted_counts(p, coeffs)
        if counts_r1_r6[:3] != normalized_counts:
            raise AssertionError("Newton reconstruction changed input counts")
        poly = sp.Poly(sum(c * t**i for i, c in enumerate(coeffs)), t, domain=sp.ZZ)
        reciprocal_roots = np.roots(list(reversed(coeffs)))
        target_modulus = 1 / math.sqrt(p)
        weil_error = max(abs(abs(root) - target_modulus) for root in reciprocal_roots)
        if coeffs[4] != p * coeffs[2] or coeffs[5] != p**2 * coeffs[1] or coeffs[6] != p**3:
            raise AssertionError("functional equation symmetry failed")
        if weil_error > 1e-10:
            raise AssertionError("numerical Weil-circle check failed")
        if not poly.is_irreducible:
            raise AssertionError(f"Frobenius polynomial unexpectedly reducible at p={p}")
        rows.append(
            {
                "prime": p,
                "frozen_model_screen": {
                    "exceptional_primes_visible_in_branch_data": [2, 7, 97],
                    "q6_squarefree_mod_p": q6_squarefree,
                    "node_disjoint_from_q6": node_disjoint,
                    "only_expected_affine_node": only_expected_affine_node,
                    "infinity_blowup_coefficients_are_units": p not in (2, 3),
                    "complete_good_reduction_theorem_claimed": False,
                },
                "affine_counts_r1_r3": affine_counts,
                "node_splits_r1_r3": node_splitting,
                "normalization_counts_r1_r3": normalized_counts,
                "frobenius_power_sums_r1_r3": power_sums,
                "l_polynomial_coefficients_ascending": coeffs,
                "l_polynomial": str(poly.as_expr()),
                "irreducible_over_q": True,
                "predicted_normalization_counts_r1_r6": counts_r1_r6,
                "maximum_reciprocal_root_modulus_error": float(weil_error),
            }
        )
    return rows


def write_results(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    symbolic = symbolic_certificate()
    frobenius = frobenius_certificate()
    payload = {
        "schema_version": SCHEMA,
        "candidate_id": "HCS-C19",
        "object": "genus-three scalar quotient control of the generically certified period-seven Henon carrier",
        "symbolic": symbolic,
        "frobenius": frobenius,
        "route_scope": {
            "arithmetic_structure": "positive genus-three curve with point-count-derived candidate Frobenius factors",
            "chronological_time_character": "constructed on companion ordered-edge cover; absent on scalar quotient",
            "riemann_divisor_claimed": False,
            "hilbert_polya_operator_claimed": False,
        },
    }
    with (output_dir / "c19_certificate.json").open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True, allow_nan=False)
        handle.write("\n")
    with (output_dir / "frobenius_counts.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(
            [
                "prime",
                "extension_degree",
                "affine_count",
                "node_splits",
                "normalization_count",
                "frobenius_power_sum",
            ]
        )
        for row in frobenius:
            for index, r in enumerate((1, 2, 3)):
                writer.writerow(
                    [
                        row["prime"],
                        r,
                        row["affine_counts_r1_r3"][index],
                        int(row["node_splits_r1_r3"][index]),
                        row["normalization_counts_r1_r3"][index],
                        row["frobenius_power_sums_r1_r3"][index],
                    ]
                )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1] / "results")
    args = parser.parse_args()
    write_results(args.output)


if __name__ == "__main__":
    main()
