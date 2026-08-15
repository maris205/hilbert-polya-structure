#!/usr/bin/python3
"""Replay every A12 CRT/rational-reconstruction congruence and height gate."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import sys

from cypari2 import Pari

from c57_exact import reject_optimized_python, require_exact_keys, strict_gzip_json


CANDIDATE_KEYS = {
    "all_congruences_replayed",
    "all_denominators_units_mod_modulus",
    "all_entries_nonempty",
    "all_entries_within_symmetric_bound",
    "coefficient_table_fractions",
    "coefficient_table_sha256",
    "max_denominator_digits",
    "max_numerator_digits",
    "method",
    "modulus_digits",
    "parameter",
    "prime_count",
    "reconstruction_bound_digits",
    "schema_id",
    "original_source_sha256",
    "state_sha256",
    "table_kind",
}
TRANSCRIPT_KEYS = {
    "accepted_primes",
    "candidate_input_used",
    "collector_source_sha256",
    "failures",
    "method",
    "modular_generator_source_sha256",
    "modulus",
    "next_candidate",
    "original_trusted_pickle_sha256",
    "parameter",
    "prime_count",
    "prior_hash",
    "residues",
    "schema_id",
    "source_acceptance_contract",
    "stability_counter",
    "table_kind",
}


def main():
    reject_optimized_python()
    parser = argparse.ArgumentParser()
    parser.add_argument("candidate", type=Path)
    parser.add_argument("transcript", type=Path)
    arguments = parser.parse_args()
    sys.set_int_max_str_digits(0)
    candidate, candidate_raw, _ = strict_gzip_json(
        arguments.candidate,
        max_compressed_bytes=40_000_000,
        max_decompressed_bytes=40_000_000,
    )
    transcript, transcript_raw, _ = strict_gzip_json(
        arguments.transcript,
        max_compressed_bytes=25_000_000,
        max_decompressed_bytes=50_000_000,
    )
    require_exact_keys(candidate, CANDIDATE_KEYS, "A12 candidate")
    require_exact_keys(transcript, TRANSCRIPT_KEYS, "A12 CRT transcript")
    if candidate["method"] != "PARI_BESTAPPR_FROM_EXACT_MODULAR_CRT_THEN_EXACT_IDENTITY_REQUIRED":
        raise AssertionError("wrong reconstruction method")
    if candidate["schema_id"] != "hcs-c57-a12-table-v1":
        raise AssertionError("wrong candidate schema")
    if candidate["original_source_sha256"] != "810ca69f08dae07b2978f6cc9d441638e6c79a8bcfd6a771c4a895f6b0d1b17d":
        raise AssertionError("original candidate lineage mismatch")
    if transcript["method"] != "CANDIDATE_BLIND_FINITE_FIELD_CARRIER_TABLE_PLUS_CRT":
        raise AssertionError("wrong transcript method")
    if transcript["candidate_input_used"] is not False:
        raise AssertionError("CRT transcript was not candidate-blind")
    if candidate["parameter"] != transcript["parameter"] or candidate["parameter"] != "theta":
        raise AssertionError("wrong A12 parameter")
    if candidate["table_kind"] != transcript["table_kind"] or candidate["table_kind"] != "carrier":
        raise AssertionError("wrong A12 table kind")
    if transcript["schema_id"] != "hcs-c57-a12-crt-transcript-v1":
        raise AssertionError("wrong transcript schema")
    if transcript["prior_hash"] is not None or transcript["stability_counter"] != 0:
        raise AssertionError("transcript must honestly record no stability hit")
    if transcript["failures"] != []:
        raise AssertionError("accepted transcript contains modular failures")
    if candidate["state_sha256"] != transcript["original_trusted_pickle_sha256"]:
        raise AssertionError("candidate/transcript source-state mismatch")
    if transcript["modular_generator_source_sha256"] != "8832df1e0041b41b84e872fb717895f11da55f80247d112918ab07de08eea99d":
        raise AssertionError("modular generator source-lock mismatch")
    if transcript["collector_source_sha256"] != "b2f0a12c0ffb0431e93e6e3f35cfa51d2f8638bf6417ae0c508163a8b7f79282":
        raise AssertionError("CRT collector source-lock mismatch")

    primes = transcript["accepted_primes"]
    if len(primes) != transcript["prime_count"] or len(primes) != candidate["prime_count"]:
        raise AssertionError("prime count mismatch")
    if any(type(value) is not int for value in primes):
        raise AssertionError("noninteger accepted prime")
    if primes != sorted(set(primes)) or not primes or transcript["next_candidate"] <= primes[-1]:
        raise AssertionError("accepted prime sequence is not canonical")
    pari = Pari()
    if any(int(pari.isprime(value)) != 1 for value in primes):
        raise AssertionError("accepted list contains a non-proven prime")
    modulus = math.prod(primes)
    if modulus != transcript["modulus"]:
        raise AssertionError("accepted-prime product is not the CRT modulus")
    if len(str(modulus)) != candidate["modulus_digits"]:
        raise AssertionError("modulus digit count mismatch")
    bound = math.isqrt(modulus // 2)
    if len(str(bound)) != candidate["reconstruction_bound_digits"]:
        raise AssertionError("rational reconstruction bound mismatch")

    residues = transcript["residues"]
    table = candidate["coefficient_table_fractions"]
    if len(residues) != 13 or len(table) != 13:
        raise AssertionError("A12 table row count is not 13")
    if any(len(row) != 36 for row in residues) or any(len(row) != 36 for row in table):
        raise AssertionError("A12 table is not 13 by 36")
    max_numerator_digits = 0
    max_denominator_digits = 0
    for row_index in range(13):
        for column_index in range(36):
            residue = residues[row_index][column_index]
            pair = table[row_index][column_index]
            if type(residue) is not int or type(pair) is not list or len(pair) != 2:
                raise AssertionError("malformed residue/fraction cell")
            numerator, denominator = pair
            if type(numerator) is not int or type(denominator) is not int:
                raise AssertionError("noninteger rational cell")
            if not (abs(numerator) < bound and 0 < denominator < bound):
                raise AssertionError(("fraction outside symmetric bound", row_index, column_index))
            if math.gcd(denominator, modulus) != 1:
                raise AssertionError(("nonunit denominator", row_index, column_index))
            if (residue * denominator - numerator) % modulus:
                raise AssertionError(("CRT congruence mismatch", row_index, column_index))
            max_numerator_digits = max(max_numerator_digits, len(str(abs(numerator))))
            max_denominator_digits = max(max_denominator_digits, len(str(denominator)))
    table_raw = json.dumps(table, separators=(",", ":")).encode()
    table_hash = hashlib.sha256(table_raw).hexdigest()
    if table_hash != candidate["coefficient_table_sha256"]:
        raise AssertionError("canonical A12 table digest mismatch")
    if max_numerator_digits != candidate["max_numerator_digits"]:
        raise AssertionError("max numerator digit count mismatch")
    if max_denominator_digits != candidate["max_denominator_digits"]:
        raise AssertionError("max denominator digit count mismatch")
    for key in (
        "all_congruences_replayed",
        "all_denominators_units_mod_modulus",
        "all_entries_nonempty",
        "all_entries_within_symmetric_bound",
    ):
        if candidate[key] is not True:
            raise AssertionError(f"candidate Boolean gate false: {key}")
    report = {
        "status": "PASS",
        "candidate_decompressed_sha256": hashlib.sha256(candidate_raw).hexdigest(),
        "transcript_decompressed_sha256": hashlib.sha256(transcript_raw).hexdigest(),
        "carrier_table_sha256": table_hash,
        "shape": [13, 36],
        "fraction_count": 468,
        "prime_count": len(primes),
        "all_primes_proven": True,
        "prime_product_equals_modulus": True,
        "modulus_digits": len(str(modulus)),
        "reconstruction_bound_digits": len(str(bound)),
        "all_468_congruences_replayed": True,
        "all_468_height_bounds_replayed": True,
        "all_468_denominators_units": True,
        "stability_not_claimed_or_used": True,
        "exact_FLINT_identity_required_for_authority": True,
    }
    raw = json.dumps(report, sort_keys=True, separators=(",", ":"))
    print(raw)
    print("report_sha256", hashlib.sha256(raw.encode()).hexdigest())


if __name__ == "__main__":
    main()
