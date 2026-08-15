#!/usr/bin/env python3
"""Exact FLINT replay of g=A12*B15 over Q(theta)."""

from fractions import Fraction
import argparse
import hashlib
import json
from pathlib import Path
import sys

from flint import fmpq, fmpq_poly
from c57_exact import reject_optimized_python, read_stable, sha256_bytes, strict_gzip_json, strict_json_loads


REPO = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
CERT = REPO / "henon_dynamics/henon_mu3_yukawa_line_field/results/c56_certificate.json"
CANDIDATE = PROJECT / "results/a12_table.json.gz"
THETA_TRANSCRIPT = PROJECT / "results/theta_crt.json.gz"
EXPECTED_CERT_SHA256 = "26739ce5aedb4a3467645f9c1b2036d4d3eec9ce4d0dbce23d67ea7b67e5fbc4"
EXPECTED_PAYLOAD_SHA256 = "5b17c9ed7bea60680556af70297199b653d51188bb30ce59f7c2c6bfbc94f661"
EXPECTED_CANDIDATE_SHA256 = "9dd43ebbdd61873dae3f6437c160a0dfbc389934a62a38057b915955c117c3cc"
EXPECTED_ORIGINAL_CANDIDATE_SHA256 = "810ca69f08dae07b2978f6cc9d441638e6c79a8bcfd6a771c4a895f6b0d1b17d"
EXPECTED_TABLE_SHA256 = "72d4aef5120926ec09904b08219cba7cf2b49323bd085d05274e5c17e1ed90a1"
EXPECTED_THETA_SHA256 = "845a0cd703b3d5d7c8814f7339010601cc2a25293b6b1bfe792aff2c728e23ea"


def gzip_json(path, compressed_limit, decompressed_limit):
    value, raw, _ = strict_gzip_json(
        path,
        max_compressed_bytes=compressed_limit,
        max_decompressed_bytes=decompressed_limit,
    )
    return raw, value


def qpoly_from_pairs(row):
    return fmpq_poly([fmpq(int(numerator), int(denominator)) for numerator, denominator in row])


def qpoly_constant(value):
    if isinstance(value, Fraction):
        return fmpq_poly([fmpq(value.numerator, value.denominator)])
    return fmpq_poly([value])


def canonical_field_element(value, degree):
    coefficients = value.coeffs()
    coefficients.extend([fmpq(0)] * (degree - len(coefficients)))
    if len(coefficients) != degree:
        raise ValueError(("bad reduced field-element degree", len(coefficients), degree))
    return [[int(coefficient.p), int(coefficient.q)] for coefficient in coefficients]


def main():
    reject_optimized_python()
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path, default=CERT)
    parser.add_argument("--candidate", type=Path, default=CANDIDATE)
    parser.add_argument("--theta-transcript", type=Path, default=THETA_TRANSCRIPT)
    arguments = parser.parse_args()
    sys.set_int_max_str_digits(0)
    candidate_raw, candidate = gzip_json(arguments.candidate, 40_000_000, 40_000_000)
    _, theta_transcript = gzip_json(arguments.theta_transcript, 1_000_000, 1_000_000)
    certificate_raw, certificate_fingerprint = read_stable(
        arguments.certificate, max_bytes=2_000_000
    )
    envelope = strict_json_loads(certificate_raw, max_bytes=2_000_000)
    locks = {
        "certificate": certificate_fingerprint.sha256,
        "candidate": sha256_bytes(candidate_raw),
    }
    if locks["certificate"] != EXPECTED_CERT_SHA256:
        raise ValueError(("certificate source-lock mismatch", locks["certificate"]))
    if locks["candidate"] != EXPECTED_CANDIDATE_SHA256:
        raise ValueError(("candidate source-lock mismatch", locks["candidate"]))
    if candidate.get("original_source_sha256") != EXPECTED_ORIGINAL_CANDIDATE_SHA256:
        raise ValueError("original candidate lineage mismatch")

    if envelope["payload_sha256"] != EXPECTED_PAYLOAD_SHA256:
        raise ValueError("payload source-lock mismatch")
    table = candidate["coefficient_table_fractions"]
    table_hash = hashlib.sha256(
        json.dumps(table, separators=(",", ":")).encode()
    ).hexdigest()
    if table_hash != EXPECTED_TABLE_SHA256:
        raise ValueError(("candidate table hash mismatch", table_hash))
    if len(table) != 13 or any(len(row) != 36 for row in table):
        raise ValueError("candidate carrier table is not 13 by 36")

    theta_coefficients = theta_transcript["coefficients"]
    theta_hash = hashlib.sha256(
        json.dumps(theta_coefficients, separators=(",", ":")).encode()
    ).hexdigest()
    if theta_hash != EXPECTED_THETA_SHA256:
        raise ValueError(("theta polynomial hash mismatch", theta_hash))
    modulus = fmpq_poly(theta_coefficients)
    if modulus.degree() != 36 or modulus.leading_coefficient() != 1:
        raise ValueError("bad theta modulus")

    shape = envelope["payload"]["grassmann_main_chart"]["lex_shape"]
    g_coefficients = next(
        row["tail_coefficients_d_0_up"]
        for row in shape
        if row["leading_variable"] == "d"
    )
    scale = int(g_coefficients[-1])
    if len(g_coefficients) != 28 or not scale:
        raise ValueError("bad degree-27 eliminant")
    carrier = [qpoly_from_pairs(row) % modulus for row in table]
    zero = fmpq_poly()
    one = fmpq_poly([1])
    theta = fmpq_poly([0, 1])
    if carrier[-1] != one:
        raise ValueError("carrier is not monic")
    if carrier[-2] != (-theta / scale):
        raise ValueError("carrier subtop coefficient is not -theta/leading(g)")

    def multiply(left, right):
        return (left * right) % modulus

    work = [qpoly_constant(Fraction(int(value), scale)) for value in g_coefficients]
    complement = [zero for _ in range(16)]
    multiplication_count = 0
    division_multiplication_count = 0
    for top_degree in range(27, 11, -1):
        quotient_degree = top_degree - 12
        quotient_coefficient = work[top_degree]
        complement[quotient_degree] = quotient_coefficient
        for carrier_degree, carrier_coefficient in enumerate(carrier):
            work[quotient_degree + carrier_degree] -= multiply(
                quotient_coefficient, carrier_coefficient
            )
            multiplication_count += 1
            division_multiplication_count += 1
        if work[top_degree] != zero:
            raise ValueError(("long-division top did not cancel", top_degree))
        print("division_step", top_degree, flush=True)

    nonzero_remainder = [index for index, value in enumerate(work) if value != zero]
    if nonzero_remainder:
        raise ValueError(("carrier does not divide eliminant", nonzero_remainder))
    if complement[-1] != one:
        raise ValueError("complement is not monic")

    # Independent forward multiplication, not merely trusting the division work array.
    product = [zero for _ in range(28)]
    forward_multiplication_count = 0
    for left_degree, left in enumerate(carrier):
        for right_degree, right in enumerate(complement):
            product[left_degree + right_degree] += multiply(left, right)
            multiplication_count += 1
            forward_multiplication_count += 1
    monic_g = [qpoly_constant(Fraction(int(value), scale)) for value in g_coefficients]
    mismatch = [index for index, (left, right) in enumerate(zip(product, monic_g)) if left != right]
    if mismatch:
        raise ValueError(("forward multiply-back mismatch", mismatch))

    complement_table = [canonical_field_element(value, 36) for value in complement]
    complement_hash = hashlib.sha256(
        json.dumps(complement_table, separators=(",", ":")).encode()
    ).hexdigest()
    report = {
        "status": "PASS",
        "certificate_sha256": locks["certificate"],
        "payload_sha256": EXPECTED_PAYLOAD_SHA256,
        "candidate_decompressed_sha256": locks["candidate"],
        "carrier_table_sha256": table_hash,
        "theta_coefficients_sha256": theta_hash,
        "theta_degree": modulus.degree(),
        "carrier_degree": len(carrier) - 1,
        "complement_degree": len(complement) - 1,
        "carrier_monic": True,
        "carrier_subtop_is_minus_theta_over_leading_g": True,
        "remainder_zero_count": len(work),
        "forward_multiply_back_count": len(product),
        "field_multiplication_count": multiplication_count,
        "division_field_multiplication_count": division_multiplication_count,
        "forward_convolution_field_multiplication_count": forward_multiplication_count,
        "complement_table_sha256": complement_hash,
    }
    report_text = json.dumps(report, sort_keys=True, separators=(",", ":"))
    print(report_text)
    print("report_sha256", hashlib.sha256(report_text.encode()).hexdigest())


if __name__ == "__main__":
    main()
