#!/usr/bin/python3
"""Candidate-blind replay of the exact theta/delta orbit-product CRTs."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import sys

from c57_modular_resolvent import CERT as DEFAULT_CERT, modular_resolvent
from c57_exact import canonical_leaf_bytes, read_stable, reject_optimized_python, sha256_bytes, strict_gzip_json, strict_json_loads


def digest(value):
    return hashlib.sha256(
        json.dumps(value, separators=(",", ":"), sort_keys=False).encode()
    ).hexdigest()


def read_gzip_json(path):
    value, raw, _ = strict_gzip_json(
        path, max_compressed_bytes=1_000_000, max_decompressed_bytes=1_000_000
    )
    return raw, value


def bounds(kind, certificate):
    payload = certificate["payload"]
    rows = {
        row["leading_variable"]: row
        for row in payload["grassmann_main_chart"]["lex_shape"]
    }
    coefficients = rows["d"]["tail_coefficients_d_0_up"]
    alpha = abs(coefficients[-1]) + max(abs(value) for value in coefficients[:-1])
    root_bound = 12 * alpha if kind == "theta" else (12 * alpha) ** 2
    coefficient_bounds = [
        math.comb(36, 36 - power) * root_bound ** (36 - power)
        for power in range(37)
    ]
    return alpha, root_bound, coefficient_bounds


def replay(kind, transcript_path, certificate_path):
    sys.set_int_max_str_digits(0)
    _, transcript = read_gzip_json(transcript_path)
    certificate_raw, certificate_fingerprint = read_stable(certificate_path, max_bytes=2_000_000)
    if certificate_fingerprint.sha256 != "26739ce5aedb4a3467645f9c1b2036d4d3eec9ce4d0dbce23d67ea7b67e5fbc4":
        raise AssertionError("C56 certificate source-lock mismatch")
    certificate = strict_json_loads(certificate_raw, max_bytes=2_000_000)
    if sha256_bytes(canonical_leaf_bytes(certificate["payload"])) != "5b17c9ed7bea60680556af70297199b653d51188bb30ce59f7c2c6bfbc94f661":
        raise AssertionError("C56 payload canonical digest mismatch")
    alpha, root_bound, coefficient_bounds = bounds(kind, certificate)
    uniform_bound = max(coefficient_bounds)
    if transcript["candidate_input_used"] is not False:
        raise AssertionError("resolver transcript is not candidate-blind")
    if transcript["degree"] != 36 or transcript["prime_count"] != len(transcript["primes"]):
        raise AssertionError("malformed degree/prime count")
    if kind == "theta":
        if transcript.get("schema_id") != "hcs-c57-theta-crt-v1" or transcript.get("original_source_sha256") != "4b0e5e899b4d431765000ed76e46405b0e54e960a684b3250bfec12ffdefd2dd":
            raise AssertionError("theta transcript lineage mismatch")
        if transcript["method"] != "EXACT_FINITE_FIELD_DOUBLE_SIX_ORBIT_PRODUCTS_PLUS_CRT":
            raise AssertionError("wrong theta method")
        if transcript["theta_bound"] != root_bound:
            raise AssertionError("theta root bound mismatch")
        residue_key = "double_six_coefficients_mod_p"
    else:
        if transcript.get("schema_id") != "hcs-c57-delta-crt-v1" or transcript.get("original_source_sha256") != "9890dd6400a65684639e9f7c06933bac0425ff69e359f898254ab16df06e859c":
            raise AssertionError("delta transcript lineage mismatch")
        if transcript["method"] != "EXACT_FINITE_FIELD_ORBIT_PRODUCTS_PLUS_CRT":
            raise AssertionError("wrong delta method")
        if transcript["alpha_bound"] != alpha or transcript["delta_bound"] != root_bound:
            raise AssertionError("delta bound mismatch")
        residue_key = "orientation_square_coefficients_mod_p"
    if transcript["uniform_coefficient_bound"] != uniform_bound:
        raise AssertionError("uniform coefficient bound mismatch")
    if digest(transcript["primes"]) != transcript["primes_sha256"]:
        raise AssertionError("prime-list digest mismatch")

    modulus = 1
    residues = [0] * 37
    orientation_separator_primes = []
    for index, prime in enumerate(transcript["primes"]):
        record = modular_resolvent(prime)
        required = {
            "proven_prime": True,
            "g_squarefree": True,
            "shape_denominators_nonzero": True,
            "all_27_line_restrictions_zero": True,
            "line_carrier_good_specialization": True,
            "meeting_count": 135,
            "sixer_count": 72,
            "double_six_count": 36,
            "double_six_distinct_values": 36,
            "orientation_square_distinct_values": 36,
            "orientation_square_definition_replayed": True,
            "all_36_beta_squared_values_used_in_orbit_product": True,
            "same_double_six_pairing_for_theta_and_delta": True,
        }
        for key, expected in required.items():
            if record.get(key) != expected:
                raise AssertionError(("bad modular gate", index, prime, key, record.get(key)))
        if record["oriented_sixer_distinct_values"] == 72:
            if record["all_36_beta_nonzero"] is not True:
                raise AssertionError("orientation separator has zero beta")
            orientation_separator_primes.append(prime)
        new = record[residue_key]
        if len(new) != 37 or new[-1] != 1:
            raise AssertionError("malformed modular orbit product")
        inverse = pow(modulus % prime, -1, prime)
        for position, value in enumerate(new):
            correction = ((value - residues[position]) % prime) * inverse % prime
            residues[position] += modulus * correction
        modulus *= prime
    coefficients = [value if value <= modulus // 2 else value - modulus for value in residues]
    if modulus != transcript["modulus"]:
        raise AssertionError("CRT modulus mismatch")
    if not (modulus > 2 * uniform_bound and transcript["modulus_exceeds_twice_uniform_bound"] is True):
        raise AssertionError("CRT height uniqueness gate failed")
    if coefficients != transcript["coefficients"]:
        raise AssertionError("candidate-blind CRT coefficient mismatch")
    if any(abs(value) > coefficient_bounds[index] for index, value in enumerate(coefficients)):
        raise AssertionError("coefficient outside individual height bound")
    if digest(coefficients) != transcript["coefficients_sha256"]:
        raise AssertionError("coefficient digest mismatch")
    if not orientation_separator_primes:
        raise AssertionError("no good prime separates all 72 oriented sixers")
    return {
        "status": "PASS",
        "kind": kind,
        "candidate_input_used": False,
        "degree": 36,
        "prime_count": len(transcript["primes"]),
        "all_primes_proven_and_good": True,
        "all_36_beta_squared_values_replayed_per_prime": True,
        "same_double_six_pairing_replayed": True,
        "oriented_sixer_separator_prime": orientation_separator_primes[0],
        "oriented_sixer_distinct_values_at_separator": 72,
        "all_36_beta_nonzero_at_separator": True,
        "modulus_digits": len(str(modulus)),
        "twice_uniform_bound_digits": len(str(2 * uniform_bound)),
        "modulus_exceeds_twice_uniform_bound": True,
        "primes_sha256": transcript["primes_sha256"],
        "coefficients_sha256": transcript["coefficients_sha256"],
    }


def main():
    reject_optimized_python()
    parser = argparse.ArgumentParser()
    parser.add_argument("kind", choices=("theta", "delta"))
    parser.add_argument("transcript", type=Path)
    arguments = parser.parse_args()
    value = replay(arguments.kind, arguments.transcript, Path(DEFAULT_CERT))
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"))
    print(raw)
    print("report_sha256", hashlib.sha256(raw.encode()).hexdigest())


if __name__ == "__main__":
    main()
