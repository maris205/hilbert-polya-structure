#!/usr/bin/python3
"""Two-reduction, full-factor multiply-back irreducibility certificate."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path
import sys

from cypari2 import Pari
from c57_exact import reject_optimized_python, strict_gzip_json


PRIMES = [
    100000000000000000000000000000000000000000000012537,
    100000000000000000000000000000000000000000000014181,
]


def multiply(left, right, prime):
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] = (result[i + j] + a * b) % prime
    return result


def proper_subset_degrees(degrees):
    values = set()
    for count in range(1, len(degrees)):
        for subset in itertools.combinations(degrees, count):
            values.add(sum(subset))
    return sorted(values)


def main():
    reject_optimized_python()
    parser = argparse.ArgumentParser()
    parser.add_argument("kind", choices=("theta", "delta"))
    parser.add_argument("transcript", type=Path)
    arguments = parser.parse_args()
    sys.set_int_max_str_digits(0)
    transcript, _, _ = strict_gzip_json(
        arguments.transcript,
        max_compressed_bytes=1_000_000,
        max_decompressed_bytes=1_000_000,
    )
    coefficients = transcript["coefficients"]
    expected = {
        "theta": (
            "hcs-c57-theta-crt-v1",
            "EXACT_FINITE_FIELD_DOUBLE_SIX_ORBIT_PRODUCTS_PLUS_CRT",
            "845a0cd703b3d5d7c8814f7339010601cc2a25293b6b1bfe792aff2c728e23ea",
        ),
        "delta": (
            "hcs-c57-delta-crt-v1",
            "EXACT_FINITE_FIELD_ORBIT_PRODUCTS_PLUS_CRT",
            "d0d90e4513feab467abbf948e39296f4a6cf01569890a55081494258058fecfb",
        ),
    }[arguments.kind]
    if transcript.get("schema_id") != expected[0] or transcript.get("method") != expected[1]:
        raise AssertionError("resolver kind/schema/method mismatch")
    if transcript.get("degree") != 36 or len(coefficients) != 37 or coefficients[-1] != 1:
        raise AssertionError("resolver is not monic of degree 36")
    if math.gcd(*coefficients) != 1:
        raise AssertionError("resolver is not primitive over Z")
    coefficient_hash = hashlib.sha256(
        json.dumps(coefficients, separators=(",", ":")).encode()
    ).hexdigest()
    if coefficient_hash != transcript["coefficients_sha256"]:
        raise AssertionError("resolver coefficient hash mismatch")
    if coefficient_hash != expected[2]:
        raise AssertionError("wrong resolver coefficients for requested kind")
    pari = Pari()
    polynomial = pari.Polrev(coefficients)
    records = []
    subset_sets = []
    for prime in PRIMES:
        if int(pari.isprime(prime)) != 1:
            raise AssertionError("not a proven prime")
        factorization = pari.factormod(polynomial, prime)
        factors = []
        product = [1]
        degrees = []
        for row in range(int(factorization.nrows())):
            factor = factorization[row, 0]
            multiplicity = int(factorization[row, 1])
            if multiplicity != 1 or int(pari.polisirreducible(factor)) != 1:
                raise AssertionError("factorization is not squarefree into irreducibles")
            values = [int(pari.lift(value)) % prime for value in reversed(list(pari.Vec(factor)))]
            if values[-1] != 1:
                raise AssertionError("nonmonic modular factor")
            degrees.append(len(values) - 1)
            factors.append({
                "degree": len(values) - 1,
                "multiplicity": multiplicity,
                "coefficients_low_to_high": values,
            })
            product = multiply(product, values, prime)
        if product != [value % prime for value in coefficients]:
            raise AssertionError("full modular factor multiply-back failed")
        subsets = proper_subset_degrees(degrees)
        subset_sets.append(set(subsets))
        records.append({
            "prime": prime,
            "proven_prime": True,
            "factor_degrees": degrees,
            "factors": factors,
            "multiply_back_exact": True,
            "proper_factor_degree_subset_sums": subsets,
        })
    intersection = sorted(subset_sets[0] & subset_sets[1])
    if intersection:
        raise AssertionError(("proper factor degree intersection nonempty", intersection))
    record_raw = json.dumps(records, separators=(",", ":")).encode()
    report = {
        "status": "PASS",
        "kind": arguments.kind,
        "resolver_coefficients_sha256": coefficient_hash,
        "records_sha256": hashlib.sha256(record_raw).hexdigest(),
        "records": records,
        "proper_degree_intersection": [],
        "irreducible_over_Q": True,
        "separable_over_Q": True,
        "monic_degree_36": True,
        "primitive_Gauss_gate": True,
    }
    raw = json.dumps(report, sort_keys=True, separators=(",", ":"))
    print(raw)
    print("report_sha256", hashlib.sha256(raw.encode()).hexdigest())


if __name__ == "__main__":
    main()
