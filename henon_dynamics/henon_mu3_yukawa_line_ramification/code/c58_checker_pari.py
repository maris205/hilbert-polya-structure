#!/usr/bin/env python3
"""Checker-only PARI replay for the HCS-C58 degree-27 line field.

The parent checker writes a small canonical request assembled from immutable
raw evidence and the frozen C56 eliminant.  This process constructs an nf from
the supplied *known integral basis*, certifies it, proves the specified image
of the original generator, and recomputes every requested prime ideal and
different exponent.  It imports no producer module.
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import sys
from typing import Any

from cypari2 import Pari


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


class ReplayError(ValueError):
    pass


def unique_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ReplayError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def reject_float(_: str) -> None:
    raise ReplayError("floating-point JSON is forbidden")


def canonical(value: Any) -> bytes:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")


def sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def exact_keys(value: Any, keys: set[str], label: str) -> dict[str, Any]:
    if type(value) is not dict or set(value) != keys:
        raise ReplayError(f"{label} keys mismatch")
    return value


def integer(value: Any, label: str) -> int:
    if type(value) is not int:
        raise ReplayError(f"{label} is not an integer")
    return value


def rational_pair(value: Any, label: str) -> tuple[int, int]:
    if (
        type(value) is not list
        or len(value) != 2
        or any(type(item) is not int for item in value)
    ):
        raise ReplayError(f"{label} is not an integer numerator/denominator pair")
    numerator, denominator = value
    if denominator <= 0 or math.gcd(numerator, denominator) != 1:
        raise ReplayError(f"{label} is not a normalized rational pair")
    return numerator, denominator


def pari_rational(pari: Pari, pair: Any, label: str):
    numerator, denominator = rational_pair(pair, label)
    return pari(numerator) / denominator


def polynomial_from_integer_coefficients(pari: Pari, x: Any, values: Any, label: str):
    if type(values) is not list or not values or any(type(item) is not int for item in values):
        raise ReplayError(f"{label} must be a nonempty integer coefficient list")
    return sum((pari(value) * x**index for index, value in enumerate(values)), pari(0))


def polynomial_from_pairs(pari: Pari, x: Any, values: Any, label: str):
    if type(values) is not list or not values:
        raise ReplayError(f"{label} must be a nonempty rational coefficient list")
    return sum(
        (
            pari_rational(pari, pair, f"{label}[{index}]") * x**index
            for index, pair in enumerate(values)
        ),
        pari(0),
    )


def gen_rational_pair(value: Any) -> list[int]:
    return [int(value.numerator()), int(value.denominator())]


def polynomial_pairs(pari: Pari, polynomial: Any, length: int) -> list[list[int]]:
    return [gen_rational_pair(pari.polcoef(polynomial, index)) for index in range(length)]


def vector_ints(value: Any) -> list[int]:
    return [int(value[index]) for index in range(len(value))]


def matrix_rows(value: Any) -> list[list[int]]:
    return [
        [int(value[row, column]) for column in range(value.ncols())]
        for row in range(value.nrows())
    ]


def local_records(pari: Pari, nf: Any, primes: list[int]) -> list[dict[str, Any]]:
    different = nf.nf_get_diff()
    records: list[dict[str, Any]] = []
    degree = int(pari.poldegree(nf.nf_get_pol()))
    discriminant = int(nf[2])
    for prime in primes:
        ideals: list[dict[str, Any]] = []
        for ideal in pari.idealprimedec(nf, prime):
            generator = ideal.pr_get_gen()
            complement = ideal[4]
            if generator.type() not in ("t_COL", "t_VEC"):
                raise ReplayError("prime generator is not a coordinate vector")
            if complement.type() != "t_MAT":
                raise ReplayError("prime-vector complement is not a matrix")
            ideals.append(
                {
                    "different_exponent": int(pari.idealval(nf, different, ideal)),
                    "e": int(ideal.pr_get_e()),
                    "f": int(ideal.pr_get_f()),
                    "generator_coordinates": vector_ints(generator),
                    "hnf_rows": matrix_rows(pari.idealhnf(nf, ideal)),
                    # PARI's fifth pr record component is the multiplication
                    # matrix for the prime-vector complement.  The historical
                    # carrier key is retained, but its value is a 27x27 matrix.
                    "prime_vector_complement": matrix_rows(complement),
                }
            )
        ideals.sort(
            key=lambda item: (
                item["e"],
                item["f"],
                item["different_exponent"],
                item["generator_coordinates"],
            )
        )
        if sum(row["e"] * row["f"] for row in ideals) != degree:
            raise ReplayError(f"local degree sum failed at {prime}")
        if sum(row["f"] * row["different_exponent"] for row in ideals) != int(
            pari.valuation(discriminant, prime)
        ):
            raise ReplayError(f"local different sum failed at {prime}")
        records.append({"prime": prime, "prime_ideals": ideals})
    return records


def main() -> int:
    if len(sys.argv) != 2:
        raise ReplayError("usage: c58_checker_pari.py REQUEST.json")
    raw = Path(sys.argv[1]).read_bytes()
    try:
        request = json.loads(
            raw.decode("utf-8", errors="strict"),
            object_pairs_hook=unique_pairs,
            parse_float=reject_float,
            parse_constant=reject_float,
        )
    except (UnicodeDecodeError, json.JSONDecodeError, ValueError) as exc:
        raise ReplayError("invalid replay request") from exc
    if raw != canonical(request) + b"\n":
        raise ReplayError("replay request is not canonical compact JSON")
    exact_keys(
        request,
        {
            "direct_primes",
            "degree36_resolvers",
            "expected_degree36_local_factors",
            "expected_local_prime_ideals",
            "expected_padic_factor_degrees",
            "integral_basis_coefficients_low_to_high_as_num_den",
            "original_generator_image_coefficients_low_to_high_as_num_den",
            "original_polynomial_coefficients_low_to_high",
            "schema_id",
            "surface_bad_prime_envelope",
            "transformed_monic_polynomial_coefficients_low_to_high",
        },
        "PARI request",
    )
    if request["schema_id"] != "hcs-c58-checker-pari-request-v1":
        raise ReplayError("PARI request schema mismatch")
    direct_primes = request["direct_primes"]
    support = request["surface_bad_prime_envelope"]
    if (
        type(direct_primes) is not list
        or type(support) is not list
        or any(type(prime) is not int or prime <= 1 for prime in direct_primes + support)
        or len(set(direct_primes)) != len(direct_primes)
        or len(set(support)) != len(support)
        or not set(direct_primes) <= set(support)
    ):
        raise ReplayError("invalid prime lists")

    pari = Pari()
    pari.allocatemem(2_000_000_000, silent=True)
    x = pari("x")
    original = polynomial_from_integer_coefficients(
        pari,
        x,
        request["original_polynomial_coefficients_low_to_high"],
        "original polynomial",
    )
    transformed = polynomial_from_integer_coefficients(
        pari,
        x,
        request["transformed_monic_polynomial_coefficients_low_to_high"],
        "transformed polynomial",
    )
    degree = int(pari.poldegree(transformed))
    if degree != 27 or int(pari.pollead(transformed)) != 1:
        raise ReplayError("transformed polynomial is not monic of degree 27")
    if int(pari.poldegree(original)) != 27 or int(pari.polisirreducible(original)) != 1:
        raise ReplayError("original eliminant is not irreducible of degree 27")
    if int(pari.polisirreducible(transformed)) != 1:
        raise ReplayError("transformed polynomial is not irreducible")

    basis_values = request["integral_basis_coefficients_low_to_high_as_num_den"]
    if type(basis_values) is not list or len(basis_values) != degree:
        raise ReplayError("integral basis must contain 27 elements")
    basis = [
        polynomial_from_pairs(pari, x, row, f"basis[{index}]")
        for index, row in enumerate(basis_values)
    ]
    nf = pari.nfinit([transformed, basis])
    if int(pari.poldegree(nf.nf_get_pol())) != degree or nf.nf_get_pol() != transformed:
        raise ReplayError("known-basis nf changed the transformed polynomial")
    unresolved = list(pari.nfcertify(nf))
    if unresolved:
        raise ReplayError("known-basis nf failed unconditional certification")
    observed_basis = [polynomial_pairs(pari, value, degree) for value in nf.nf_get_zk()]
    if observed_basis != basis_values:
        raise ReplayError("PARI did not retain the supplied integral basis")
    basis_pari_text = str(nf.nf_get_zk()).encode("utf-8")
    field_signature = [int(value) for value in nf.nf_get_sign()]
    if (
        len(field_signature) != 2
        or field_signature[0] < 0
        or field_signature[1] < 0
        or field_signature[0] + 2 * field_signature[1] != degree
    ):
        raise ReplayError("PARI returned an invalid degree-27 field signature")

    image_coefficients = request[
        "original_generator_image_coefficients_low_to_high_as_num_den"
    ]
    if type(image_coefficients) is not list or not image_coefficients:
        raise ReplayError("missing original-generator image")
    image_polynomial = polynomial_from_pairs(
        pari, x, image_coefficients, "original generator image"
    )
    image = pari.Mod(image_polynomial, transformed)
    value = pari.Mod(0, transformed)
    for coefficient in reversed(request["original_polynomial_coefficients_low_to_high"]):
        value = value * image + coefficient
    if value != 0:
        raise ReplayError("specified generator image is not a root of the original eliminant")
    minimal = pari.minpoly(image)
    if int(pari.poldegree(minimal)) != degree:
        raise ReplayError("specified generator image does not generate the degree-27 field")
    original_monic = original / pari.pollead(original)
    if minimal != original_monic:
        raise ReplayError("specified generator image has the wrong oriented minimal polynomial")

    recomputed_local = local_records(pari, nf, direct_primes)
    if recomputed_local != request["expected_local_prime_ideals"]:
        raise ReplayError("raw local prime-ideal carrier disagrees with independent PARI replay")
    discriminant = int(nf[2])
    exponent_vector = [int(pari.valuation(discriminant, prime)) for prime in support]
    prime_envelope_isprime = [int(pari.isprime(prime)) == 1 for prime in support]
    if prime_envelope_isprime != [True] * len(support):
        raise ReplayError("surface bad-prime envelope contains a composite")
    factor_degrees = {}
    for record in recomputed_local:
        counts: dict[int, int] = {}
        for ideal in record["prime_ideals"]:
            local_degree = ideal["e"] * ideal["f"]
            counts[local_degree] = counts.get(local_degree, 0) + 1
        factor_degrees[str(record["prime"])] = [
            [degree_value, counts[degree_value]] for degree_value in sorted(counts)
        ]
    if factor_degrees != request["expected_padic_factor_degrees"]:
        raise ReplayError("raw p-adic factor-degree carrier disagrees with PARI replay")
    resolver_input = exact_keys(
        request["degree36_resolvers"], {"delta", "theta"}, "degree-36 resolver input"
    )
    resolver_expected = exact_keys(
        request["expected_degree36_local_factors"],
        {"delta", "theta"},
        "degree-36 resolver expected tame local factors",
    )
    resolver_factors: dict[str, dict[str, list[list[int]]]] = {}
    resolver_tame_local: dict[str, dict[str, dict[str, Any]]] = {}
    resolver_hensel_congruences: dict[str, dict[str, list[int]]] = {}
    theta36_real_root_count: int | None = None
    wild_theta_authority: dict[str, dict[str, Any]] = {}
    for name in ("delta", "theta"):
        resolver = polynomial_from_integer_coefficients(
            pari, x, resolver_input[name], f"{name} degree-36 resolver"
        )
        if int(pari.poldegree(resolver)) != 36 or int(pari.pollead(resolver)) != 1:
            raise ReplayError(f"{name} resolver is not monic of degree 36")
        if name == "theta":
            theta36_real_root_count = int(pari.polsturm(resolver))
            if not 0 <= theta36_real_root_count <= 36:
                raise ReplayError("theta36 real-root count is outside degree bounds")
        global_polynomial_discriminant = int(pari.poldisc(resolver))
        per_prime: dict[str, list[list[int]]] = {}
        per_tame_prime: dict[str, dict[str, Any]] = {}
        per_prime_hensel: dict[str, list[int]] = {}
        for prime in direct_primes:
            signatures = []
            tame_rows_at_precisions: list[list[list[int]]] = []
            authority_polynomial_exponents: dict[int, int] = {}
            authority_reduction_patterns: dict[int, tuple[int, int]] = {}
            verified_product_precisions: list[int] = []
            for precision in (20, 30, 40):
                factors = pari.factorpadic(resolver, prime, precision)
                product_padic = pari(1)
                for row in range(factors.nrows()):
                    factor = factors[row, 0]
                    multiplicity = int(factors[row, 1])
                    factor_degree = int(pari.poldegree(factor))
                    if multiplicity != 1 or pari.polcoef(factor, factor_degree) != 1:
                        raise ReplayError(
                            f"{name} factorpadic returned nonmonic/non-simple factor at {prime}"
                        )
                    product_padic *= factor ** multiplicity
                difference = product_padic - resolver
                for coefficient_index in range(37):
                    coefficient = pari.polcoef(difference, coefficient_index)
                    if coefficient != 0 and pari.valuation(coefficient, prime) < precision:
                        raise ReplayError(
                            f"{name} Hensel product congruence failed at {prime}/{precision}"
                        )
                verified_product_precisions.append(precision)
                signatures.append(
                    sorted(
                    [
                        [int(pari.poldegree(factors[row, 0])), int(factors[row, 1])]
                        for row in range(factors.nrows())
                    ]
                    )
                )
                if prime in (181, 997, 2346241):
                    tame_rows = []
                    for row in range(factors.nrows()):
                        lifted = pari.lift(factors[row, 0])
                        local_nf = pari.nfinit([lifted, [prime]], 1)
                        prime_ideals = list(pari.idealprimedec(local_nf, prime))
                        if len(prime_ideals) != 1:
                            raise ReplayError(
                                f"{name} lifted local factor has multiple primes at {prime}"
                            )
                        ideal = prime_ideals[0]
                        polynomial_discriminant_exponent = int(
                            pari.valuation(pari.poldisc(lifted), prime)
                        )
                        tame_rows.append(
                            [
                                int(pari.poldegree(lifted)),
                                int(ideal.pr_get_e()),
                                int(ideal.pr_get_f()),
                                int(
                                    pari.idealval(
                                        local_nf, local_nf.nf_get_diff(), ideal
                                    )
                                ),
                            ]
                        )
                        if precision == 40:
                            factor_degree = int(pari.poldegree(lifted))
                            if factor_degree in authority_polynomial_exponents:
                                raise ReplayError(
                                    f"{name} repeated authority factor degree at {prime}"
                                )
                            authority_polynomial_exponents[factor_degree] = (
                                polynomial_discriminant_exponent
                            )
                            reduced = pari.factormod(lifted, prime)
                            if reduced.nrows() != 1:
                                raise ReplayError(
                                    f"{name} authority factor has non-primary reduction at {prime}"
                                )
                            authority_reduction_patterns[factor_degree] = (
                                int(pari.poldegree(reduced[0, 0])),
                                int(reduced[0, 1]),
                            )
                    tame_rows_at_precisions.append(sorted(tame_rows))
            if not signatures[0] == signatures[1] == signatures[2]:
                raise ReplayError(f"{name} factorpadic degrees are precision-unstable at {prime}")
            if tame_rows_at_precisions:
                if not (
                    tame_rows_at_precisions[0]
                    == tame_rows_at_precisions[1]
                    == tame_rows_at_precisions[2]
                ):
                    raise ReplayError(
                        f"{name} lifted local rows are precision-unstable at {prime}"
                    )
                tame_rows = tame_rows_at_precisions[0]
                local_rows = [
                    {
                        "d": row[3],
                        "e": row[1],
                        "f": row[2],
                        "factor_degree": row[0],
                        "field_discriminant_contribution": row[2] * row[3],
                        "mod_p_factor_exponent": authority_reduction_patterns[row[0]][1],
                        "mod_p_irreducible_factor_degree": authority_reduction_patterns[row[0]][0],
                        "polynomial_discriminant_exponent": authority_polynomial_exponents[
                            row[0]
                        ],
                    }
                    for row in tame_rows
                ]
                local_rows.sort(key=lambda row: (row["factor_degree"], row["e"], row["f"], row["d"]))
                global_polynomial_discriminant_exponent = int(
                    pari.valuation(global_polynomial_discriminant, prime)
                )
                twice_max_factor_discriminant_exponent = 2 * max(
                    row["polynomial_discriminant_exponent"] for row in local_rows
                )
                factor_krasner_bound_satisfied = (
                    40 > twice_max_factor_discriminant_exponent
                )
                resolver_separation_bound_satisfied = (
                    40 > global_polynomial_discriminant_exponent
                )
                bound_satisfied = (
                    factor_krasner_bound_satisfied
                    and resolver_separation_bound_satisfied
                )
                authority_role = (
                    "KRASNER_CERTIFIED_AUTHORITY"
                    if name == "theta"
                    else "BOUNDED_NON_RESULT_NONDEPENDENCY"
                )
                if (name == "theta") is not bound_satisfied:
                    raise ReplayError(f"{name} authority-role/Krasner-bound mismatch at {prime}")
                per_tame_prime[str(prime)] = {
                    "authority_bound_satisfied": bound_satisfied,
                    "authority_precision": 40,
                    "authority_role": authority_role,
                    "factor_degree_multiplicities": signatures[0],
                    "factor_krasner_bound_satisfied": factor_krasner_bound_satisfied,
                    "local_rows": local_rows,
                    "global_polynomial_discriminant_exponent": (
                        global_polynomial_discriminant_exponent
                    ),
                    "stable_precisions": [20, 30, 40],
                    "resolver_separation_bound_satisfied": (
                        resolver_separation_bound_satisfied
                    ),
                    "total_discriminant_exponent": sum(
                        row["field_discriminant_contribution"] for row in local_rows
                    ),
                    "twice_max_polynomial_discriminant_exponent": (
                        twice_max_factor_discriminant_exponent
                    ),
                }
            per_prime[str(prime)] = signatures[0]
            per_prime_hensel[str(prime)] = verified_product_precisions
            if name == "theta" and prime in (3, 5):
                certified_precisions = (900, 950, 1000)
                factor_rows_at_precisions = []
                signatures_at_precisions = []
                minimum_multiplyback_valuations = []
                for authority_precision in certified_precisions:
                    authority_factors = pari.factorpadic(
                        resolver, prime, authority_precision
                    )
                    authority_product = pari(1)
                    uncompressed_rows = []
                    degree_counts: dict[int, int] = {}
                    for row in range(authority_factors.nrows()):
                        factor = authority_factors[row, 0]
                        multiplicity = int(authority_factors[row, 1])
                        factor_degree = int(pari.poldegree(factor))
                        if (
                            multiplicity != 1
                            or pari.polcoef(factor, factor_degree) != 1
                        ):
                            raise ReplayError(
                                f"theta authority factor is nonmonic/nonsimple at {prime}"
                            )
                        authority_product *= factor
                        degree_counts[factor_degree] = (
                            degree_counts.get(factor_degree, 0) + 1
                        )
                        lifted = pari.lift(factor)
                        reduced = pari.factormod(lifted, prime)
                        if reduced.nrows() != 1:
                            raise ReplayError(
                                f"theta authority factor has non-primary reduction at {prime}"
                            )
                        uncompressed_rows.append(
                            (
                                factor_degree,
                                int(pari.poldegree(reduced[0, 0])),
                                int(reduced[0, 1]),
                                int(pari.valuation(pari.poldisc(lifted), prime)),
                            )
                        )
                    compressed_rows = []
                    for row_value in sorted(set(uncompressed_rows)):
                        compressed_rows.append(
                            {
                                "count": uncompressed_rows.count(row_value),
                                "factor_degree": row_value[0],
                                "mod_p_factor_exponent": row_value[2],
                                "mod_p_irreducible_factor_degree": row_value[1],
                                "polynomial_discriminant_exponent": row_value[3],
                            }
                        )
                    factor_rows_at_precisions.append(compressed_rows)
                    signatures_at_precisions.append(
                        [
                            [factor_degree, degree_counts[factor_degree]]
                            for factor_degree in sorted(degree_counts)
                        ]
                    )
                    authority_difference = authority_product - resolver
                    coefficient_valuations = []
                    for coefficient_index in range(37):
                        coefficient = pari.polcoef(
                            authority_difference, coefficient_index
                        )
                        valuation = (
                            authority_precision
                            if coefficient == 0
                            else int(pari.valuation(coefficient, prime))
                        )
                        if valuation < authority_precision:
                            raise ReplayError(
                                f"theta authority multiplyback failed at {prime}"
                            )
                        coefficient_valuations.append(valuation)
                    minimum_multiplyback_valuations.append(
                        min(coefficient_valuations)
                    )
                if (
                    len({canonical(rows) for rows in factor_rows_at_precisions}) != 1
                    or len({canonical(rows) for rows in signatures_at_precisions}) != 1
                ):
                    raise ReplayError(
                        f"theta wild factor rows are precision-unstable at {prime}"
                    )
                authority_rows = factor_rows_at_precisions[0]
                authority_signature = signatures_at_precisions[0]
                global_exponent = int(
                    pari.valuation(global_polynomial_discriminant, prime)
                )
                twice_max_factor_exponent = 2 * max(
                    row["polynomial_discriminant_exponent"]
                    for row in authority_rows
                )
                factor_bounds = [
                    precision > twice_max_factor_exponent
                    for precision in certified_precisions
                ]
                resolver_bounds = [
                    precision > global_exponent
                    for precision in certified_precisions
                ]
                if not all(factor_bounds) or not all(resolver_bounds):
                    raise ReplayError(
                        f"theta certified precisions are nonauthoritative at {prime}"
                    )
                wild_theta_authority[str(prime)] = {
                    "all_factors_monic_simple": True,
                    "authority_bound_satisfied": True,
                    "factor_degree_multiplicities": authority_signature,
                    "factor_krasner_bounds_satisfied": factor_bounds,
                    "factor_rows": authority_rows,
                    "factor_rows_stable_across_precisions": True,
                    "global_polynomial_discriminant_exponent": global_exponent,
                    "minimum_multiplyback_valuations": (
                        minimum_multiplyback_valuations
                    ),
                    "resolver_separation_bounds_satisfied": resolver_bounds,
                    "twice_max_polynomial_discriminant_exponent": (
                        twice_max_factor_exponent
                    ),
                }
        resolver_factors[name] = per_prime
        resolver_tame_local[name] = per_tame_prime
        resolver_hensel_congruences[name] = per_prime_hensel
    if resolver_tame_local != resolver_expected:
        raise ReplayError("degree-36 resolver tame local-factor carrier mismatch")
    theta_bounds = {
        record["global_polynomial_discriminant_exponent"]
        for record in resolver_tame_local["theta"].values()
    }
    delta_bounds = {
        record["global_polynomial_discriminant_exponent"]
        for record in resolver_tame_local["delta"].values()
    }
    if theta_bounds != {24} or delta_bounds != {840}:
        raise ReplayError("degree-36 polynomial discriminant bounds changed")
    theta_factor_bounds = {
        2 * max(row["polynomial_discriminant_exponent"] for row in record["local_rows"])
        for record in resolver_tame_local["theta"].values()
    }
    delta_factor_bounds = {
        2 * max(row["polynomial_discriminant_exponent"] for row in record["local_rows"])
        for record in resolver_tame_local["delta"].values()
    }
    if theta_factor_bounds != {24} or delta_factor_bounds != {408}:
        raise ReplayError("degree-36 factor polynomial discriminant bounds changed")
    if theta36_real_root_count is None or set(wild_theta_authority) != {"3", "5"}:
        raise ReplayError("theta36 archimedean/wild authority replay is incomplete")
    wild_degree36_theta_authority = {
        "authority_role": "KRASNER_CERTIFIED_AUTHORITY",
        "certified_precisions": [900, 950, 1000],
        "delta36_role": "BOUNDED_NON_RESULT_NONDEPENDENCY",
        "prime_records": wild_theta_authority,
        "resolver": "theta36",
    }
    local_summaries = [
        {
            "prime": record["prime"],
            "rows_e_f_d": [
                [row["e"], row["f"], row["different_exponent"]]
                for row in record["prime_ideals"]
            ],
        }
        for record in recomputed_local
    ]
    report = {
        "basis_reused_exactly": True,
        "basis_pari_text_sha256": sha256(basis_pari_text),
        "basis_pari_text_size_bytes": len(basis_pari_text),
        "degree": degree,
        "degree36_factor_degrees": resolver_factors,
        "degree36_local_factors": resolver_tame_local,
        "degree36_precision_gate": {
            "authoritative_resolver": "theta",
            "authority_precision": 40,
            "delta_authority_bound_satisfied": False,
            "delta_max_factor_polynomial_discriminant_exponent": 204,
            "delta_precision_exceeds_global_polynomial_discriminant_exponent": False,
            "delta_precision_exceeds_twice_max_factor_discriminant_exponent": False,
            "delta_global_polynomial_discriminant_exponent": 840,
            "delta_role": "BOUNDED_NON_RESULT_NONDEPENDENCY",
            "delta_twice_max_factor_discriminant_exponent": 408,
            "selection_uses_delta_as_authority": False,
            "theta_authority_bound_satisfied": True,
            "theta_max_factor_polynomial_discriminant_exponent": 12,
            "theta_precision_exceeds_global_polynomial_discriminant_exponent": True,
            "theta_precision_exceeds_twice_max_factor_discriminant_exponent": True,
            "theta_global_polynomial_discriminant_exponent": 24,
            "theta_role": "KRASNER_CERTIFIED_AUTHORITY",
            "theta_twice_max_factor_discriminant_exponent": 24,
        },
        "degree36_hensel_product_congruences": resolver_hensel_congruences,
        "field_discriminant_decimal_newline_sha256": sha256(
            (str(discriminant) + "\n").encode("ascii")
        ),
        "field_discriminant_digits": len(str(abs(discriminant))),
        "field_discriminant_exponents_on_surface_bad_prime_envelope": exponent_vector,
        "field_discriminant_positive": discriminant > 0,
        "field_signature": field_signature,
        "generator_image_minimal_polynomial_coefficients_sha256": sha256(
            canonical(polynomial_pairs(pari, minimal, degree + 1))
        ),
        "generator_image_proves_oriented_field_identity": True,
        "local_prime_ideals_sha256": sha256(canonical(recomputed_local)),
        "local_summaries": local_summaries,
        "nfcertify_unresolved": [],
        "original_degree": int(pari.poldegree(original)),
        "original_irreducible": True,
        "padic_factor_degrees": factor_degrees,
        "schema_id": "hcs-c58-checker-pari-report-v1",
        "surface_bad_prime_envelope_isprime": prime_envelope_isprime,
        "theta36_real_root_count": theta36_real_root_count,
        "transformed_degree": degree,
        "transformed_irreducible": True,
        "wild_degree36_theta_authority": wild_degree36_theta_authority,
    }
    report_raw = canonical(report)
    sys.stdout.buffer.write(report_raw + b"\n")
    sys.stdout.buffer.write(f"report_sha256 {sha256(report_raw)}\n".encode("ascii"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
