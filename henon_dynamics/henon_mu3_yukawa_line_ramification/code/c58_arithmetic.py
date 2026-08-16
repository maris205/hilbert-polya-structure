#!/usr/bin/env python3
"""Exact producer-side PARI replay of the C58 degree-27 arithmetic carrier."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import math
from pathlib import Path
import sys
from typing import Any

from cypari2 import Pari

from c58_exact import (
    StrictDataError,
    canonical_leaf_bytes,
    deep_exact,
    read_stable,
    reject_optimized_python,
    require_canonical_compact_json,
    require_exact_keys,
    strict_gzip_json,
    strict_json_loads,
)


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

REPO = Path(__file__).resolve().parents[3]
C56_CERTIFICATE = (
    REPO / "henon_dynamics/henon_mu3_yukawa_line_field/results/c56_certificate.json"
)
C56_CERTIFICATE_SHA256 = (
    "26739ce5aedb4a3467645f9c1b2036d4d3eec9ce4d0dbce23d67ea7b67e5fbc4"
)
C57_RESULTS = REPO / "henon_dynamics/henon_mu3_yukawa_minimal_brauer_jump/results"
RESOLVER_ARTIFACTS = {
    "delta36": (
        C57_RESULTS / "delta_crt.json.gz",
        "4deead9914f31b0012afd91088339793330874a3b5156ceaeb1371fcb495f685",
        "61ead9febb5ee8295c75980b81ba1c73c2d9cdaebf9e87dd0d0e76da899999a9",
        "hcs-c57-delta-crt-v1",
    ),
    "theta36": (
        C57_RESULTS / "theta_crt.json.gz",
        "91181a525e0acb17e73d2e96fd4e7d5d7a25913784ef8ad9d3be59c430a4fadd",
        "5760dd3f4a1e07834f974e340f6cd488d9b793dab8efa0864505903cf9e1bcb3",
        "hcs-c57-theta-crt-v1",
    ),
}
SUPPORT = [
    2,
    3,
    5,
    181,
    283,
    997,
    1801,
    2346241,
    14932047182473291995860108491583652133938007263719,
]
EXPONENTS = [0, 46, 36, 18, 6, 18, 6, 18, 6]
DIRECT_PRIMES = [3, 5, 181, 997, 2346241]
EXPECTED_LOCAL_SUMMARIES = {
    "3": [[3, 1, 3], [6, 1, 7], [9, 1, 18], [9, 1, 18]],
    "5": [[1, 1, 0], [1, 1, 0], [5, 1, 7], [5, 1, 7], [5, 1, 7], [10, 1, 15]],
    "181": [[3, 1, 2], [3, 2, 2], [3, 6, 2]],
    "997": [[3, 1, 2], [3, 2, 2], [3, 6, 2]],
    "2346241": [[3, 1, 2], [3, 2, 2], [3, 6, 2]],
}
EXPECTED_LOCAL_DEGREES = {
    "3": [[3, 1], [6, 1], [9, 2]],
    "5": [[1, 2], [5, 3], [10, 1]],
    "181": [[3, 1], [6, 1], [18, 1]],
    "997": [[3, 1], [6, 1], [18, 1]],
    "2346241": [[3, 1], [6, 1], [18, 1]],
}
EXPECTED_DEGREE36_LOCAL_FACTORS = {
    carrier: {
        str(prime): {
            "authority_role": (
                "KRASNER_CERTIFIED_AUTHORITY"
                if carrier == "theta36"
                else "BOUNDED_NON_RESULT_NONDEPENDENCY"
            ),
            "authority_bound_satisfied": carrier == "theta36",
            "authority_precision": 40,
            "factor_krasner_bound_satisfied": carrier == "theta36",
            "factor_degree_multiplicities": [[3, 1], [6, 1], [9, 1], [18, 1]],
            "global_polynomial_discriminant_exponent": (
                24 if carrier == "theta36" else 840
            ),
            "local_rows": [
                {
                    "d": 2,
                    "e": 3,
                    "f": residue_degree,
                    "factor_degree": 3 * residue_degree,
                    "field_discriminant_contribution": 2 * residue_degree,
                    "polynomial_discriminant_exponent": (
                        2 * residue_degree
                        if carrier == "theta36"
                        else {1: 4, 2: 20, 3: 48, 6: 204}[residue_degree]
                    ),
                    "mod_p_irreducible_factor_degree": (
                        residue_degree if carrier == "theta36" else 1
                    ),
                    "mod_p_factor_exponent": (
                        3 if carrier == "theta36" else 3 * residue_degree
                    ),
                }
                for residue_degree in (1, 2, 3, 6)
            ],
            "stable_precisions": [20, 30, 40],
            "total_discriminant_exponent": 24,
            "resolver_separation_bound_satisfied": carrier == "theta36",
            "twice_max_polynomial_discriminant_exponent": (
                24 if carrier == "theta36" else 408
            ),
        }
        for prime in (181, 997, 2346241)
    }
    for carrier in ("delta36", "theta36")
}
EXPECTED_WILD_DEGREE36_THETA_AUTHORITY = {
    "authority_role": "KRASNER_CERTIFIED_AUTHORITY",
    "certified_precisions": [900, 950, 1000],
    "delta36_role": "BOUNDED_NON_RESULT_NONDEPENDENCY",
    "prime_records": {
        "3": {
            "all_factors_monic_simple": True,
            "authority_bound_satisfied": True,
            "factor_degree_multiplicities": [[3, 3], [9, 1], [18, 1]],
            "factor_krasner_bounds_satisfied": [True, True, True],
            "factor_rows": [
                {
                    "count": 3,
                    "factor_degree": 3,
                    "mod_p_factor_exponent": 3,
                    "mod_p_irreducible_factor_degree": 1,
                    "polynomial_discriminant_exponent": 11,
                },
                {
                    "count": 1,
                    "factor_degree": 9,
                    "mod_p_factor_exponent": 9,
                    "mod_p_irreducible_factor_degree": 1,
                    "polynomial_discriminant_exponent": 62,
                },
                {
                    "count": 1,
                    "factor_degree": 18,
                    "mod_p_factor_exponent": 18,
                    "mod_p_irreducible_factor_degree": 1,
                    "polynomial_discriminant_exponent": 269,
                },
            ],
            "factor_rows_stable_across_precisions": True,
            "global_polynomial_discriminant_exponent": 886,
            "minimum_multiplyback_valuations": [900, 950, 1000],
            "resolver_separation_bounds_satisfied": [True, True, True],
            "twice_max_polynomial_discriminant_exponent": 538,
        },
        "5": {
            "all_factors_monic_simple": True,
            "authority_bound_satisfied": True,
            "factor_degree_multiplicities": [[1, 1], [5, 1], [10, 3]],
            "factor_krasner_bounds_satisfied": [True, True, True],
            "factor_rows": [
                {
                    "count": 1,
                    "factor_degree": 1,
                    "mod_p_factor_exponent": 1,
                    "mod_p_irreducible_factor_degree": 1,
                    "polynomial_discriminant_exponent": 0,
                },
                {
                    "count": 1,
                    "factor_degree": 5,
                    "mod_p_factor_exponent": 5,
                    "mod_p_irreducible_factor_degree": 1,
                    "polynomial_discriminant_exponent": 27,
                },
                {
                    "count": 3,
                    "factor_degree": 10,
                    "mod_p_factor_exponent": 10,
                    "mod_p_irreducible_factor_degree": 1,
                    "polynomial_discriminant_exponent": 123,
                },
            ],
            "factor_rows_stable_across_precisions": True,
            "global_polynomial_discriminant_exponent": 746,
            "minimum_multiplyback_valuations": [900, 950, 1000],
            "resolver_separation_bounds_satisfied": [True, True, True],
            "twice_max_polynomial_discriminant_exponent": 246,
        },
    },
    "resolver": "theta36",
}


def sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def rational_pair(value: Any, label: str) -> tuple[int, int]:
    if (
        type(value) is not list
        or len(value) != 2
        or any(type(item) is not int for item in value)
    ):
        raise StrictDataError(f"{label} is not a rational pair")
    numerator, denominator = value
    if denominator <= 0 or math.gcd(numerator, denominator) != 1:
        raise StrictDataError(f"{label} is not normalized")
    return numerator, denominator


def pari_rational(pari: Pari, value: Any, label: str):
    numerator, denominator = rational_pair(value, label)
    return pari(numerator) / denominator


def polynomial_from_integers(pari: Pari, x: Any, values: Any, label: str):
    if type(values) is not list or not values or any(type(item) is not int for item in values):
        raise StrictDataError(f"{label} is not an integer coefficient vector")
    return sum(
        (pari(coefficient) * x**index for index, coefficient in enumerate(values)),
        pari(0),
    )


def polynomial_from_pairs(pari: Pari, x: Any, values: Any, label: str):
    if type(values) is not list or not values:
        raise StrictDataError(f"{label} is empty")
    return sum(
        (
            pari_rational(pari, value, f"{label}[{index}]") * x**index
            for index, value in enumerate(values)
        ),
        pari(0),
    )


def gen_pair(value: Any) -> list[int]:
    return [int(value.numerator()), int(value.denominator())]


def polynomial_pairs(pari: Pari, polynomial: Any, length: int) -> list[list[int]]:
    return [gen_pair(pari.polcoef(polynomial, index)) for index in range(length)]


def vector_ints(value: Any) -> list[int]:
    return [int(value[index]) for index in range(len(value))]


def matrix_rows(value: Any) -> list[list[int]]:
    return [
        [int(value[row, column]) for column in range(value.ncols())]
        for row in range(value.nrows())
    ]


def local_records(pari: Pari, nf: Any) -> tuple[dict[str, Any], dict[str, Any]]:
    different = nf.nf_get_diff()
    discriminant = int(nf[2])
    records = {}
    degree_records = {}
    for prime in DIRECT_PRIMES:
        ideals = []
        for ideal in pari.idealprimedec(nf, prime):
            generator = ideal.pr_get_gen()
            complement = ideal[4]
            if generator.type() not in ("t_COL", "t_VEC"):
                raise StrictDataError("prime generator is not a coordinate vector")
            if complement.type() != "t_MAT":
                raise StrictDataError("prime-vector complement is not a matrix")
            ideals.append(
                {
                    "different_exponent": int(pari.idealval(nf, different, ideal)),
                    "e": int(ideal.pr_get_e()),
                    "f": int(ideal.pr_get_f()),
                    "generator_coordinates": vector_ints(generator),
                    "hnf_rows": matrix_rows(pari.idealhnf(nf, ideal)),
                    "prime_vector_complement": matrix_rows(complement),
                }
            )
        ideals.sort(
            key=lambda row: (
                row["e"],
                row["f"],
                row["different_exponent"],
                row["generator_coordinates"],
                row["hnf_rows"],
                row["prime_vector_complement"],
            )
        )
        if sum(row["e"] * row["f"] for row in ideals) != 27:
            raise StrictDataError(f"local degree sum failed at {prime}")
        if sum(row["f"] * row["different_exponent"] for row in ideals) != int(
            pari.valuation(discriminant, prime)
        ):
            raise StrictDataError(f"local different sum failed at {prime}")
        records[str(prime)] = ideals
        degrees = Counter(row["e"] * row["f"] for row in ideals)
        degree_records[str(prime)] = [
            [degree, multiplicity] for degree, multiplicity in sorted(degrees.items())
        ]
    return records, degree_records


def load_degree36_resolvers():
    coefficients = {}
    source_locks = {}
    fingerprints = {}
    for name, (path, compressed_sha, decompressed_sha, schema_id) in sorted(
        RESOLVER_ARTIFACTS.items()
    ):
        value, raw, fingerprint = strict_gzip_json(
            path,
            max_compressed_bytes=1_000_000,
            max_decompressed_bytes=2_000_000,
        )
        require_canonical_compact_json(raw)
        if (
            fingerprint.sha256 != compressed_sha
            or sha256(raw) != decompressed_sha
            or value.get("schema_id") != schema_id
            or value.get("degree") != 36
        ):
            raise StrictDataError(f"frozen C57 {name} resolver source changed")
        row = value.get("coefficients")
        if (
            type(row) is not list
            or len(row) != 37
            or any(type(item) is not int for item in row)
            or row[-1] != 1
        ):
            raise StrictDataError(f"frozen C57 {name} coefficients are malformed")
        coefficients[name] = row
        fingerprints[name] = fingerprint
        source_locks[name] = {
            "compressed_sha256": compressed_sha,
            "decompressed_sha256": decompressed_sha,
        }
    return coefficients, source_locks, fingerprints


def degree36_local_replay(pari: Pari, x: Any, resolvers: dict[str, list[int]]):
    result = {}
    factor_degrees = {}
    hensel_product_congruences = {}
    for name in ("delta36", "theta36"):
        polynomial = polynomial_from_integers(
            pari, x, resolvers[name], f"{name} resolver"
        )
        if int(pari.poldegree(polynomial)) != 36 or int(pari.pollead(polynomial)) != 1:
            raise StrictDataError(f"{name} resolver is not monic of degree 36")
        per_prime = {}
        all_prime_factor_degrees = {}
        all_prime_hensel_products = {}
        for prime in DIRECT_PRIMES:
            global_polynomial_discriminant_exponent = int(
                pari.valuation(pari.poldisc(polynomial), prime)
            )
            signatures = []
            local_rows_at_precisions = []
            for precision in (20, 30, 40):
                factors = pari.factorpadic(polynomial, prime, precision)
                product_polynomial = pari(1)
                for row in range(factors.nrows()):
                    factor = factors[row, 0]
                    multiplicity = int(factors[row, 1])
                    if multiplicity != 1 or pari.pollead(factor) != 1:
                        raise StrictDataError(
                            f"{name} factor is not monic/simple at {prime}"
                        )
                    product_polynomial *= factor
                difference = product_polynomial - polynomial
                for coefficient_index in range(37):
                    coefficient = pari.polcoef(difference, coefficient_index)
                    if coefficient != 0 and int(pari.valuation(coefficient, prime)) < precision:
                        raise StrictDataError(
                            f"{name} factor multiply-back failed at {prime}"
                        )
                signature = sorted(
                    [
                        [int(pari.poldegree(factors[row, 0])), int(factors[row, 1])]
                        for row in range(factors.nrows())
                    ]
                )
                signatures.append(signature)
                local_rows = []
                if prime in (181, 997, 2346241):
                    for row in range(factors.nrows()):
                        lifted = pari.lift(factors[row, 0])
                        local_nf_raw = pari.nfinit([lifted, [prime]], 1)
                        if (
                            len(local_nf_raw) == 2
                            and local_nf_raw[0].type() == "t_VEC"
                            and len(local_nf_raw[0]) == 9
                        ):
                            local_nf = local_nf_raw[0]
                        else:
                            local_nf = local_nf_raw
                        ideals = list(pari.idealprimedec(local_nf, prime))
                        if len(ideals) != 1:
                            raise StrictDataError(
                                f"{name} lifted factor has multiple primes at {prime}"
                            )
                        ideal = ideals[0]
                        residue_degree = int(ideal.pr_get_f())
                        different_exponent = int(
                            pari.idealval(local_nf, local_nf.nf_get_diff(), ideal)
                        )
                        reduction = pari.factormod(lifted, prime)
                        if reduction.nrows() != 1:
                            raise StrictDataError(
                                f"{name} lifted factor reduction is not primary"
                            )
                        local_rows.append(
                            {
                                "d": different_exponent,
                                "e": int(ideal.pr_get_e()),
                                "f": residue_degree,
                                "factor_degree": int(pari.poldegree(lifted)),
                                "field_discriminant_contribution": residue_degree
                                * different_exponent,
                                "polynomial_discriminant_exponent": int(
                                    pari.valuation(pari.poldisc(lifted), prime)
                                ),
                                "mod_p_irreducible_factor_degree": int(
                                    pari.poldegree(reduction[0, 0])
                                ),
                                "mod_p_factor_exponent": int(reduction[0, 1]),
                            }
                        )
                    local_rows.sort(key=lambda item: item["factor_degree"])
                    local_rows_at_precisions.append(local_rows)
            if not signatures[0] == signatures[1] == signatures[2]:
                raise StrictDataError(f"{name} factor degrees are precision-unstable")
            all_prime_factor_degrees[str(prime)] = signatures[0]
            all_prime_hensel_products[str(prime)] = [20, 30, 40]
            if prime not in (181, 997, 2346241):
                continue
            if not (
                local_rows_at_precisions[0]
                == local_rows_at_precisions[1]
                == local_rows_at_precisions[2]
            ):
                raise StrictDataError(f"{name} local rows are precision-unstable")
            local_rows = local_rows_at_precisions[0]
            maximum_polynomial_discriminant_exponent = max(
                row["polynomial_discriminant_exponent"] for row in local_rows
            )
            factor_krasner_bound_satisfied = (
                40 > 2 * maximum_polynomial_discriminant_exponent
            )
            resolver_separation_bound_satisfied = (
                40 > global_polynomial_discriminant_exponent
            )
            authority_bound_satisfied = (
                factor_krasner_bound_satisfied
                and resolver_separation_bound_satisfied
            )
            per_prime[str(prime)] = {
                "authority_bound_satisfied": authority_bound_satisfied,
                "authority_precision": 40,
                "authority_role": (
                    "KRASNER_CERTIFIED_AUTHORITY"
                    if name == "theta36"
                    else "BOUNDED_NON_RESULT_NONDEPENDENCY"
                ),
                "factor_krasner_bound_satisfied": (
                    factor_krasner_bound_satisfied
                ),
                "factor_degree_multiplicities": signatures[0],
                "global_polynomial_discriminant_exponent": (
                    global_polynomial_discriminant_exponent
                ),
                "local_rows": local_rows,
                "resolver_separation_bound_satisfied": (
                    resolver_separation_bound_satisfied
                ),
                "stable_precisions": [20, 30, 40],
                "total_discriminant_exponent": sum(
                    row["field_discriminant_contribution"] for row in local_rows
                ),
                "twice_max_polynomial_discriminant_exponent": (
                    2 * maximum_polynomial_discriminant_exponent
                ),
            }
        result[name] = per_prime
        report_name = name.removesuffix("36")
        factor_degrees[report_name] = all_prime_factor_degrees
        hensel_product_congruences[report_name] = all_prime_hensel_products
    authority_maximum = max(
        row["polynomial_discriminant_exponent"]
        for local in result["theta36"].values()
        for row in local["local_rows"]
    )
    corroboration_maximum = max(
        row["polynomial_discriminant_exponent"]
        for local in result["delta36"].values()
        for row in local["local_rows"]
    )
    theta_global_maximum = max(
        local["global_polynomial_discriminant_exponent"]
        for local in result["theta36"].values()
    )
    delta_global_maximum = max(
        local["global_polynomial_discriminant_exponent"]
        for local in result["delta36"].values()
    )
    if (
        authority_maximum != 12
        or corroboration_maximum != 204
        or theta_global_maximum != 24
        or delta_global_maximum != 840
        or 40 <= theta_global_maximum
        or 40 > delta_global_maximum
    ):
        raise StrictDataError("degree-36 authority/nonresult precision roles changed")
    return (
        result,
        factor_degrees,
        hensel_product_congruences,
        authority_maximum,
        corroboration_maximum,
        theta_global_maximum,
        delta_global_maximum,
    )


def wild_theta_authority_replay(pari: Pari, polynomial: Any) -> dict[str, Any]:
    """Certify the wild theta36 factor patterns above conservative Krasner bounds."""

    if int(pari.poldegree(polynomial)) != 36 or int(pari.pollead(polynomial)) != 1:
        raise StrictDataError("theta36 resolver is not monic of degree 36")
    precisions = (900, 950, 1000)
    prime_records = {}
    for prime in (3, 5):
        global_exponent = int(pari.valuation(pari.poldisc(polynomial), prime))
        factor_rows_at_precisions = []
        degree_rows_at_precisions = []
        minimum_multiplyback_valuations = []
        for precision in precisions:
            factors = pari.factorpadic(polynomial, prime, precision)
            product_polynomial = pari(1)
            uncompressed_rows = []
            degree_counter: Counter[int] = Counter()
            for index in range(factors.nrows()):
                factor = factors[index, 0]
                multiplicity = int(factors[index, 1])
                if multiplicity != 1 or int(pari.pollead(factor)) != 1:
                    raise StrictDataError(
                        f"theta36 wild factor is not monic/simple at {prime}"
                    )
                product_polynomial *= factor
                lifted = pari.lift(factor)
                factor_degree = int(pari.poldegree(lifted))
                degree_counter[factor_degree] += 1
                reduction = pari.factormod(lifted, prime)
                if reduction.nrows() != 1:
                    raise StrictDataError(
                        f"theta36 wild factor reduction is not primary at {prime}"
                    )
                uncompressed_rows.append(
                    (
                        factor_degree,
                        int(pari.poldegree(reduction[0, 0])),
                        int(reduction[0, 1]),
                        int(pari.valuation(pari.poldisc(lifted), prime)),
                    )
                )
            row_counter = Counter(uncompressed_rows)
            factor_rows_at_precisions.append(
                [
                    {
                        "count": count,
                        "factor_degree": row[0],
                        "mod_p_factor_exponent": row[2],
                        "mod_p_irreducible_factor_degree": row[1],
                        "polynomial_discriminant_exponent": row[3],
                    }
                    for row, count in sorted(row_counter.items())
                ]
            )
            degree_rows_at_precisions.append(
                [[degree, count] for degree, count in sorted(degree_counter.items())]
            )
            difference = product_polynomial - polynomial
            valuations = []
            for coefficient_index in range(37):
                coefficient = pari.polcoef(difference, coefficient_index)
                if coefficient != 0:
                    valuations.append(int(pari.valuation(coefficient, prime)))
            minimum_valuation = min(valuations, default=precision)
            if minimum_valuation < precision:
                raise StrictDataError(
                    f"theta36 wild factor multiply-back failed at {prime}"
                )
            minimum_multiplyback_valuations.append(minimum_valuation)
        factor_rows_stable = all(
            rows == factor_rows_at_precisions[0]
            for rows in factor_rows_at_precisions[1:]
        )
        degree_rows_stable = all(
            rows == degree_rows_at_precisions[0]
            for rows in degree_rows_at_precisions[1:]
        )
        if not factor_rows_stable or not degree_rows_stable:
            raise StrictDataError(
                f"theta36 wild factors are precision-unstable at {prime}"
            )
        factor_rows = factor_rows_at_precisions[0]
        maximum_factor_exponent = max(
            row["polynomial_discriminant_exponent"] for row in factor_rows
        )
        twice_maximum = 2 * maximum_factor_exponent
        factor_bounds = [precision > twice_maximum for precision in precisions]
        resolver_bounds = [precision > global_exponent for precision in precisions]
        prime_records[str(prime)] = {
            "all_factors_monic_simple": True,
            "authority_bound_satisfied": all(factor_bounds) and all(resolver_bounds),
            "factor_degree_multiplicities": degree_rows_at_precisions[0],
            "factor_krasner_bounds_satisfied": factor_bounds,
            "factor_rows": factor_rows,
            "factor_rows_stable_across_precisions": factor_rows_stable,
            "global_polynomial_discriminant_exponent": global_exponent,
            "minimum_multiplyback_valuations": minimum_multiplyback_valuations,
            "resolver_separation_bounds_satisfied": resolver_bounds,
            "twice_max_polynomial_discriminant_exponent": twice_maximum,
        }
    return {
        "authority_role": "KRASNER_CERTIFIED_AUTHORITY",
        "certified_precisions": list(precisions),
        "delta36_role": "BOUNDED_NON_RESULT_NONDEPENDENCY",
        "prime_records": prime_records,
        "resolver": "theta36",
    }


def validate_top_level(evidence: Any) -> dict[str, Any]:
    evidence = require_exact_keys(
        evidence,
        {
            "archimedean",
            "cubic_terms",
            "degree36_local_factors",
            "field_discriminant",
            "field_isomorphism",
            "local_prime_ideals",
            "macaulay",
            "maximal_order",
            "padic_factor_degrees",
            "reflection_witnesses",
            "schema_id",
            "wild_degree36_theta_authority",
        },
        "arithmetic evidence",
    )
    if evidence["schema_id"] != "hcs-c58-arithmetic-evidence-v1":
        raise StrictDataError("arithmetic evidence schema changed")
    return evidence


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, required=True)
    arguments = parser.parse_args()
    reject_optimized_python()

    evidence, evidence_raw, evidence_fingerprint = strict_gzip_json(
        arguments.evidence,
        max_compressed_bytes=4_000_000,
        max_decompressed_bytes=8_000_000,
    )
    require_canonical_compact_json(evidence_raw)
    evidence = validate_top_level(evidence)

    c56_raw, c56_fingerprint = read_stable(C56_CERTIFICATE, max_bytes=10_000_000)
    if c56_fingerprint.sha256 != C56_CERTIFICATE_SHA256:
        raise StrictDataError("frozen C56 certificate SHA changed")
    c56 = strict_json_loads(c56_raw, max_bytes=10_000_000)
    try:
        original_coefficients = c56["payload"]["irreducibility"][
            "eliminant_coefficients_d_0_to_27"
        ]
        cubic_terms = [
            [row["coefficient"], row["exponents_u0_to_u3"]]
            for row in c56["payload"]["surface"]["primitive_coefficients"]
        ]
    except (KeyError, TypeError) as exc:
        raise StrictDataError("frozen C56 arithmetic carrier is incomplete") from exc
    if not deep_exact(cubic_terms, evidence["cubic_terms"]):
        raise StrictDataError("C56 cubic and arithmetic evidence differ")
    resolver_coefficients, resolver_source_locks, resolver_fingerprints = (
        load_degree36_resolvers()
    )

    maximal = evidence["maximal_order"]
    transformed_coefficients = maximal[
        "transformed_monic_polynomial_coefficients_low_to_high"
    ]
    basis_coefficients = maximal[
        "integral_basis_coefficients_low_to_high_as_num_den"
    ]
    if maximal["transformed_monic_polynomial_sha256"] != sha256(
        canonical_leaf_bytes(transformed_coefficients)
    ):
        raise StrictDataError("transformed-polynomial carrier digest changed")
    if maximal["integral_basis_canonical_sha256"] != sha256(
        canonical_leaf_bytes(basis_coefficients)
    ):
        raise StrictDataError("integral-basis carrier digest changed")

    pari = Pari()
    pari.allocatemem(2_000_000_000, silent=True)
    surface_bad_prime_envelope_isprime = [
        int(pari.isprime(prime)) == 1 for prime in SUPPORT
    ]
    if surface_bad_prime_envelope_isprime != [True] * len(SUPPORT):
        raise StrictDataError("surface bad-prime envelope contains a nonprime entry")
    x = pari("x")
    theta36 = polynomial_from_integers(
        pari, x, resolver_coefficients["theta36"], "theta36 resolver"
    )
    theta36_real_root_count = int(pari.polsturm(theta36))
    if theta36_real_root_count != 4:
        raise StrictDataError("theta36 real-root count changed")
    observed_wild_theta_authority = wild_theta_authority_replay(pari, theta36)
    if not deep_exact(
        observed_wild_theta_authority, EXPECTED_WILD_DEGREE36_THETA_AUTHORITY
    ):
        raise StrictDataError("theta36 wild high-precision authority replay changed")
    if not deep_exact(
        evidence["wild_degree36_theta_authority"],
        observed_wild_theta_authority,
    ):
        raise StrictDataError("theta36 wild high-precision evidence changed")
    original = polynomial_from_integers(
        pari, x, original_coefficients, "C56 eliminant"
    )
    transformed = polynomial_from_integers(
        pari, x, transformed_coefficients, "transformed polynomial"
    )
    if int(pari.poldegree(original)) != 27 or int(pari.poldegree(transformed)) != 27:
        raise StrictDataError("field polynomial degree changed")
    if int(pari.pollead(transformed)) != 1:
        raise StrictDataError("transformed polynomial is not monic")
    if int(pari.polisirreducible(original)) != 1 or int(pari.polisirreducible(transformed)) != 1:
        raise StrictDataError("field polynomial is not irreducible")
    if type(basis_coefficients) is not list or len(basis_coefficients) != 27:
        raise StrictDataError("integral basis length changed")
    basis = [
        polynomial_from_pairs(pari, x, row, f"basis[{index}]")
        for index, row in enumerate(basis_coefficients)
    ]
    nf = pari.nfinit([transformed, basis])
    if nf.nf_get_pol() != transformed or list(pari.nfcertify(nf)):
        raise StrictDataError("known-basis nf failed certification")
    observed_basis = [
        polynomial_pairs(pari, value, 27) for value in nf.nf_get_zk()
    ]
    if not deep_exact(observed_basis, basis_coefficients):
        raise StrictDataError("PARI did not retain the supplied basis")
    basis_text = str(nf.nf_get_zk()).encode("utf-8")
    if (
        sha256(basis_text) != maximal["integral_basis_pari_text_sha256"]
        or len(basis_text) != maximal["integral_basis_pari_text_size_bytes"]
        or maximal["nfcertify_unresolved"] != []
    ):
        raise StrictDataError("PARI integral-basis text binding changed")

    isomorphism = evidence["field_isomorphism"]
    require_exact_keys(
        isomorphism,
        {
            "orientation",
            "original_generator_image_canonical_sha256",
            "original_generator_image_common_denominator",
            "original_generator_image_numerators_low_to_high",
            "original_polynomial_degree",
        },
        "field isomorphism",
    )
    if isomorphism["orientation"] != (
        "original_C56_eliminant_generator_maps_to_polynomial_in_transformed_generator"
    ) or isomorphism["original_polynomial_degree"] != 27:
        raise StrictDataError("oriented field-isomorphism declaration changed")
    denominator = isomorphism["original_generator_image_common_denominator"]
    numerators = isomorphism["original_generator_image_numerators_low_to_high"]
    image_carrier = {
        "common_denominator": denominator,
        "numerators_low_to_high": numerators,
    }
    if isomorphism["original_generator_image_canonical_sha256"] != sha256(
        canonical_leaf_bytes(image_carrier)
    ):
        raise StrictDataError("oriented generator-image digest changed")
    if (
        type(denominator) is not int
        or denominator <= 0
        or type(numerators) is not list
        or not numerators
        or any(type(value) is not int for value in numerators)
        or math.gcd(denominator, *numerators) != 1
    ):
        raise StrictDataError("oriented generator image is noncanonical")
    image_polynomial = sum(
        (pari(value) * x**index for index, value in enumerate(numerators)),
        pari(0),
    ) / denominator
    image = pari.Mod(image_polynomial, transformed)
    value = pari.Mod(0, transformed)
    for coefficient in reversed(original_coefficients):
        value = value * image + coefficient
    if value != 0:
        raise StrictDataError("oriented image is not a root of the C56 eliminant")
    minimal = pari.minpoly(image)
    if minimal != original / pari.pollead(original):
        raise StrictDataError("oriented image has the wrong minimal polynomial")

    discriminant = int(nf[2])
    disc = require_exact_keys(
        evidence["field_discriminant"],
        {
            "decimal_newline_sha256",
            "digits",
            "exponents_on_surface_bad_prime_envelope",
            "positive",
            "ramified_support",
            "surface_bad_prime_envelope",
            "value",
        },
        "field discriminant",
    )
    if (
        discriminant != disc["value"]
        or discriminant <= 0
        or disc["positive"] is not True
        or disc["surface_bad_prime_envelope"] != SUPPORT
        or disc["ramified_support"] != SUPPORT[1:]
        or disc["exponents_on_surface_bad_prime_envelope"] != EXPONENTS
        or disc["digits"] != len(str(discriminant))
        or disc["decimal_newline_sha256"]
        != sha256((str(discriminant) + "\n").encode("ascii"))
    ):
        raise StrictDataError("field discriminant carrier changed")
    observed_exponents = [int(pari.valuation(discriminant, prime)) for prime in SUPPORT]
    if observed_exponents != EXPONENTS:
        raise StrictDataError("field discriminant support/exponents changed")

    observed_local, observed_degrees = local_records(pari, nf)
    if not deep_exact(observed_local, evidence["local_prime_ideals"]):
        raise StrictDataError("local prime-ideal carrier changed")
    if not deep_exact(observed_degrees, evidence["padic_factor_degrees"]):
        raise StrictDataError("local factor-degree carrier changed")
    summaries = {
        prime: sorted(
            [
                [row["e"], row["f"], row["different_exponent"]]
                for row in rows
            ]
        )
        for prime, rows in observed_local.items()
    }
    if summaries != EXPECTED_LOCAL_SUMMARIES or observed_degrees != EXPECTED_LOCAL_DEGREES:
        raise StrictDataError("direct p-maximal local summary changed")
    (
        observed_degree36,
        degree36_factor_degrees,
        degree36_hensel_product_congruences,
        theta_maximum_polynomial_discriminant_exponent,
        delta_maximum_polynomial_discriminant_exponent,
        theta_global_polynomial_discriminant_exponent,
        delta_global_polynomial_discriminant_exponent,
    ) = degree36_local_replay(pari, x, resolver_coefficients)
    if not deep_exact(observed_degree36, EXPECTED_DEGREE36_LOCAL_FACTORS):
        raise StrictDataError("direct degree-36 tame local replay changed")
    if not deep_exact(evidence["degree36_local_factors"], observed_degree36):
        raise StrictDataError("degree-36 tame local carrier changed")
    for name, carrier in EXPECTED_DEGREE36_LOCAL_FACTORS.items():
        for local in carrier.values():
            factor_bound_holds = (
                local["authority_precision"]
                > local["twice_max_polynomial_discriminant_exponent"]
            )
            resolver_bound_holds = (
                local["authority_precision"]
                > local["global_polynomial_discriminant_exponent"]
            )
            bound_holds = factor_bound_holds and resolver_bound_holds
            if factor_bound_holds != local["factor_krasner_bound_satisfied"]:
                raise StrictDataError("degree-36 factor Krasner gate changed")
            if resolver_bound_holds != local["resolver_separation_bound_satisfied"]:
                raise StrictDataError("degree-36 resolver separation gate changed")
            if bound_holds != local["authority_bound_satisfied"]:
                raise StrictDataError("degree-36 p-adic precision role changed")
            if (name == "theta36") != bound_holds:
                raise StrictDataError("only theta36 may be the Krasner authority")

    line_field_signature = list(map(int, nf.nf_get_sign()))
    if (
        line_field_signature != [3, 12]
        or line_field_signature[0] + 2 * line_field_signature[1] != 27
        or theta36_real_root_count < 0
        or theta36_real_root_count > 36
        or (36 - theta36_real_root_count) % 2
    ):
        raise StrictDataError("archimedean degree/signature carrier changed")
    archimedean = evidence["archimedean"]
    expected_archimedean = {
        "V20_signature": [11, 9],
        "V6_signature": [3, 3],
        "complex_conjugation_element_class_index": 17,
        "complex_conjugation_subgroup_tom_index": 5,
        "double_six_orbits_36": [1] * theta36_real_root_count
        + [2] * ((36 - theta36_real_root_count) // 2),
        "field_signature": line_field_signature,
        "line_orbits_27": [1] * line_field_signature[0]
        + [2] * line_field_signature[1],
    }
    if not deep_exact(archimedean, expected_archimedean):
        raise StrictDataError("archimedean cross-binding changed")

    _, c56_after = read_stable(C56_CERTIFICATE, max_bytes=10_000_000)
    _, evidence_after = read_stable(arguments.evidence, max_bytes=4_000_000)
    if c56_after != c56_fingerprint or evidence_after != evidence_fingerprint:
        raise StrictDataError("an arithmetic input changed during replay")
    for name, (path, _, _, _) in RESOLVER_ARTIFACTS.items():
        _, after = read_stable(path, max_bytes=1_000_000)
        if after != resolver_fingerprints[name]:
            raise StrictDataError(f"C57 {name} resolver changed during replay")

    recomputed_local = [
        {"prime": prime, "prime_ideals": observed_local[str(prime)]}
        for prime in DIRECT_PRIMES
    ]
    local_summary_rows = [
        {"prime": prime, "rows_e_f_d": summaries[str(prime)]}
        for prime in DIRECT_PRIMES
    ]
    report = {
        "basis_reused_exactly": True,
        "basis_pari_text_sha256": sha256(basis_text),
        "basis_pari_text_size_bytes": len(basis_text),
        "degree": 27,
        "degree36_factor_degrees": degree36_factor_degrees,
        "degree36_hensel_product_congruences": (
            degree36_hensel_product_congruences
        ),
        "degree36_local_factors": {
            "delta": observed_degree36["delta36"],
            "theta": observed_degree36["theta36"],
        },
        "degree36_precision_gate": {
            "authoritative_resolver": "theta",
            "authority_precision": 40,
            "delta_authority_bound_satisfied": False,
            "delta_max_factor_polynomial_discriminant_exponent": (
                delta_maximum_polynomial_discriminant_exponent
            ),
            "delta_precision_exceeds_global_polynomial_discriminant_exponent": False,
            "delta_precision_exceeds_twice_max_factor_discriminant_exponent": False,
            "delta_global_polynomial_discriminant_exponent": (
                delta_global_polynomial_discriminant_exponent
            ),
            "delta_role": "BOUNDED_NON_RESULT_NONDEPENDENCY",
            "delta_twice_max_factor_discriminant_exponent": 408,
            "selection_uses_delta_as_authority": False,
            "theta_authority_bound_satisfied": True,
            "theta_max_factor_polynomial_discriminant_exponent": (
                theta_maximum_polynomial_discriminant_exponent
            ),
            "theta_precision_exceeds_global_polynomial_discriminant_exponent": True,
            "theta_precision_exceeds_twice_max_factor_discriminant_exponent": True,
            "theta_global_polynomial_discriminant_exponent": (
                theta_global_polynomial_discriminant_exponent
            ),
            "theta_role": "KRASNER_CERTIFIED_AUTHORITY",
            "theta_twice_max_factor_discriminant_exponent": 24,
        },
        "field_discriminant_decimal_newline_sha256": disc[
            "decimal_newline_sha256"
        ],
        "field_discriminant_digits": disc["digits"],
        "field_discriminant_exponents_on_surface_bad_prime_envelope": observed_exponents,
        "field_discriminant_positive": True,
        "generator_image_minimal_polynomial_coefficients_sha256": sha256(
            canonical_leaf_bytes(polynomial_pairs(pari, minimal, 28))
        ),
        "generator_image_proves_oriented_field_identity": True,
        "local_prime_ideals_sha256": sha256(
            canonical_leaf_bytes(recomputed_local)
        ),
        "line_field_signature": line_field_signature,
        "local_summaries": local_summary_rows,
        "nfcertify_unresolved": [],
        "original_degree": int(pari.poldegree(original)),
        "original_irreducible": True,
        "padic_factor_degrees": observed_degrees,
        "schema_id": "hcs-c58-checker-pari-report-v1",
        "surface_bad_prime_envelope_isprime": (
            surface_bad_prime_envelope_isprime
        ),
        "theta36_real_root_count": theta36_real_root_count,
        "transformed_degree": int(pari.poldegree(transformed)),
        "transformed_irreducible": True,
        "wild_degree36_low_precision_role": (
            "BOUNDED_NON_RESULT_NONDEPENDENCY"
        ),
        "wild_degree36_theta_authority": observed_wild_theta_authority,
    }
    raw = canonical_leaf_bytes(report)
    print(raw.decode("utf-8"))
    print("report_sha256", sha256(raw))


if __name__ == "__main__":
    main()
