#!/usr/bin/python3
"""Exact finite-field rank/pivot certificate for the canonical 60x31 Q matrix."""

import argparse
import hashlib
import json
import math
from pathlib import Path
import sys
from itertools import combinations

from cypari2 import Pari
from c57_exact import reject_optimized_python, read_stable, sha256_bytes, strict_gzip_json, strict_json_loads


REPO = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
CERT = REPO / "henon_dynamics/henon_mu3_yukawa_line_field/results/c56_certificate.json"
CANDIDATE = PROJECT / "results/a12_table.json.gz"
THETA_TRANSCRIPT = PROJECT / "results/theta_crt.json.gz"
EXPECTED_CERT = "26739ce5aedb4a3467645f9c1b2036d4d3eec9ce4d0dbce23d67ea7b67e5fbc4"
EXPECTED_PAYLOAD = "5b17c9ed7bea60680556af70297199b653d51188bb30ce59f7c2c6bfbc94f661"
EXPECTED_CANDIDATE = "9dd43ebbdd61873dae3f6437c160a0dfbc389934a62a38057b915955c117c3cc"
EXPECTED_ORIGINAL_CANDIDATE = "810ca69f08dae07b2978f6cc9d441638e6c79a8bcfd6a771c4a895f6b0d1b17d"
EXPECTED_TABLE = "72d4aef5120926ec09904b08219cba7cf2b49323bd085d05274e5c17e1ed90a1"
EXPECTED_THETA = "845a0cd703b3d5d7c8814f7339010601cc2a25293b6b1bfe792aff2c728e23ea"


def gzip_json(path, compressed_limit, decompressed_limit):
    value, raw, _ = strict_gzip_json(
        path,
        max_compressed_bytes=compressed_limit,
        max_decompressed_bytes=decompressed_limit,
    )
    return raw, value


def horner(coefficients, value):
    result = value * 0
    for coefficient in reversed(coefficients):
        result = result * value + coefficient
    return result


def orbit_product(roots, zero, one):
    coefficients = [one]
    for root in roots:
        product = [zero for _ in range(len(coefficients) + 1)]
        for index, coefficient in enumerate(coefficients):
            product[index] -= root * coefficient
            product[index + 1] += coefficient
        coefficients = product
    return coefficients


def degree_four_monomials():
    rows = []
    for e0 in range(4, -1, -1):
        for e1 in range(4 - e0, -1, -1):
            for e2 in range(4 - e0 - e1, -1, -1):
                rows.append((e0, e1, e2, 4 - e0 - e1 - e2))
    return rows


GAUGE = {(4, 0, 0, 0), (3, 1, 0, 0), (3, 0, 1, 0), (3, 0, 0, 1)}
MONOMIALS = [row for row in degree_four_monomials() if row not in GAUGE]


def main():
    reject_optimized_python()
    parser = argparse.ArgumentParser()
    parser.add_argument("prime", type=int)
    parser.add_argument("--certificate", type=Path, default=CERT)
    parser.add_argument("--candidate", type=Path, default=CANDIDATE)
    parser.add_argument("--theta-transcript", type=Path, default=THETA_TRANSCRIPT)
    args = parser.parse_args()
    prime = args.prime
    sys.set_int_max_str_digits(0)
    pari = Pari()
    if int(pari.isprime(prime)) != 1:
        raise ValueError("modulus is not a proven prime")

    candidate_raw, candidate = gzip_json(args.candidate, 40_000_000, 40_000_000)
    _, theta_transcript = gzip_json(args.theta_transcript, 1_000_000, 1_000_000)
    certificate_raw, certificate_fingerprint = read_stable(
        args.certificate, max_bytes=2_000_000
    )
    envelope = strict_json_loads(certificate_raw, max_bytes=2_000_000)
    locks = {
        "certificate": certificate_fingerprint.sha256,
        "candidate": sha256_bytes(candidate_raw),
    }
    if locks != {"certificate": EXPECTED_CERT, "candidate": EXPECTED_CANDIDATE}:
        raise ValueError(("source-lock mismatch", locks))
    if candidate.get("original_source_sha256") != EXPECTED_ORIGINAL_CANDIDATE:
        raise ValueError("original candidate lineage mismatch")
    if envelope["payload_sha256"] != EXPECTED_PAYLOAD:
        raise ValueError("payload hash mismatch")
    payload = envelope["payload"]
    surface_coefficients = {
        tuple(row["exponents_u0_to_u3"]): row["coefficient"]
        for row in payload["surface"]["primitive_coefficients"]
    }
    c = surface_coefficients.get((3, 0, 0, 0), 0)
    a = surface_coefficients.get((2, 1, 0, 0), 0)
    b = surface_coefficients.get((2, 0, 1, 0), 0)
    d = surface_coefficients.get((2, 0, 0, 1), 0)
    gauge_block = [
        [c, 0, 0, 0],
        [a, c, 0, 0],
        [b, 0, c, 0],
        [d, 0, 0, c],
    ]
    expected_gauge_block = [
        [75081586157, 0, 0, 0],
        [-28576620789, 75081586157, 0, 0],
        [-122000922135, 0, 75081586157, 0],
        [-5364921951, 0, 0, 75081586157],
    ]
    gauge_determinant = c**4
    if gauge_block != expected_gauge_block:
        raise ValueError(("C56-derived quartic gauge block mismatch", gauge_block))
    if gauge_determinant != 31778526453059635681033276764499400992765201:
        raise ValueError("quartic gauge determinant mismatch")
    candidate_table = candidate["coefficient_table_fractions"]
    candidate_table_hash = hashlib.sha256(
        json.dumps(candidate_table, separators=(",", ":")).encode()
    ).hexdigest()
    if candidate_table_hash != EXPECTED_TABLE:
        raise ValueError("candidate table hash mismatch")
    candidate_mod_prime = []
    for row in candidate_table:
        reduced = []
        for numerator, denominator in row:
            denominator_mod = denominator % prime
            if denominator_mod == 0:
                raise ValueError("candidate denominator is not a prime unit")
            reduced.append(numerator % prime * pow(denominator_mod, -1, prime) % prime)
        candidate_mod_prime.append(reduced)

    theta_coefficients = theta_transcript["coefficients"]
    theta_hash = hashlib.sha256(
        json.dumps(theta_coefficients, separators=(",", ":")).encode()
    ).hexdigest()
    if theta_hash != EXPECTED_THETA:
        raise ValueError("theta hash mismatch")
    shape = payload["grassmann_main_chart"]["lex_shape"]
    by_variable = {row["leading_variable"]: row for row in shape}
    g_coefficients = by_variable["d"]["tail_coefficients_d_0_up"]
    if g_coefficients[-1] % prime == 0:
        raise ValueError("eliminant leading coefficient is not a unit")
    for variable in ("a", "b", "c"):
        if by_variable[variable]["leading_coefficient"] % prime == 0:
            raise ValueError(("shape denominator is not a unit", variable))

    z, x = pari("z"), pari("x")
    g = pari.Polrev(g_coefficients, x)
    factor_rows = pari.factormod(g, prime, 1).python()
    extension_degree = 1
    for degree, multiplicity in factor_rows:
        if int(multiplicity) != 1:
            raise ValueError("inseparable eliminant")
        extension_degree = math.lcm(extension_degree, int(degree))
    generator = pari.ffgen(pari.ffinit(prime, extension_degree, z), z)
    roots = list(pari.polrootsmod(g, generator))
    if len(roots) != 27:
        raise ValueError("wrong root count")
    zero, one = roots[0] * 0, generator**0

    lines = []
    for d in roots:
        line = {"d": d}
        for variable in ("a", "b", "c"):
            row = by_variable[variable]
            line[variable] = -horner(row["tail_coefficients_d_0_up"], d) / row[
                "leading_coefficient"
            ]
        lines.append(line)
    meeting = set()
    for i, j in combinations(range(27), 2):
        left, right = lines[i], lines[j]
        residue = (left["a"] - right["a"]) * (left["d"] - right["d"]) - (
            left["b"] - right["b"]
        ) * (left["c"] - right["c"])
        if residue == 0:
            meeting.add(frozenset((i, j)))
    if len(meeting) != 135:
        raise ValueError("wrong incidence count")
    sixers = [
        frozenset(subset)
        for subset in combinations(range(27), 6)
        if all(frozenset((i, j)) not in meeting for i, j in combinations(subset, 2))
    ]
    if len(sixers) != 72:
        raise ValueError("wrong sixer count")
    double_sixes = set()
    for first in sixers:
        second = frozenset(
            i
            for i in range(27)
            if i not in first
            and sum(frozenset((i, j)) in meeting for j in first) == 5
        )
        double_sixes.add(frozenset((first, second)))
    if len(double_sixes) != 36:
        raise ValueError("wrong double-six count")
    configurations = sorted(
        double_sixes,
        key=lambda ds: tuple(sorted(tuple(sorted(row)) for row in ds)),
    )
    if any(len(set().union(*configuration)) != 12 for configuration in configurations):
        raise ValueError("a double-six carrier does not contain 12 distinct lines")
    # Every reconstructed line is in the U01 chart
    # (u0,u1,u2,u3)=(s,t,a*s+c*t,b*s+d*t), so u0=s is not identically zero.
    u0_avoids_every_carrier_line = True

    def rem(poly, carrier):
        return pari.divrem(poly, carrier)[1]

    def build_matrix(configuration):
        indices = sorted(set().union(*configuration))
        carrier = pari.Polrev(
            orbit_product([roots[index] for index in indices], zero, one), x
        )
        theta_value = sum(
            (g_coefficients[-1] * roots[index] for index in indices), zero
        )
        expected_carrier = [horner(row, theta_value) for row in candidate_mod_prime]
        actual_carrier = [pari.polcoef(carrier, degree, x) for degree in range(13)]
        if expected_carrier != actual_carrier:
            raise ValueError("candidate carrier specialization mismatch")
        line_polynomials = {"d": x}
        for variable in ("a", "b", "c"):
            row = by_variable[variable]
            line_polynomials[variable] = rem(
                -pari.Polrev(row["tail_coefficients_d_0_up"], x)
                / row["leading_coefficient"],
                carrier,
            )
        powers = {}
        for variable in ("a", "b", "c", "d"):
            powers[(variable, 0)] = pari(1)
            for exponent in range(1, 5):
                powers[(variable, exponent)] = rem(
                    powers[(variable, exponent - 1)] * line_polynomials[variable],
                    carrier,
                )
        columns = []
        for e0, e1, e2, e3 in MONOMIALS:
            coefficients = [pari(0) for _ in range(5)]
            for i in range(e2 + 1):
                for j in range(e3 + 1):
                    coefficients[e1 + i + j] += rem(
                        math.comb(e2, i)
                        * math.comb(e3, j)
                        * powers[("a", e2 - i)]
                        * powers[("c", i)]
                        * powers[("b", e3 - j)]
                        * powers[("d", j)],
                        carrier,
                    )
            columns.append([rem(value, carrier) for value in coefficients])
        entries = []
        for t_degree in range(5):
            for d_degree in range(12):
                for column in columns:
                    entries.append(pari.polcoef(column[t_degree], d_degree, x))
        return pari.matrix(60, 31, entries), theta_value

    first_matrix, first_theta = build_matrix(configurations[0])
    without_q0 = pari.matrix(
        60, 30, [first_matrix[row, column] for row in range(60) for column in range(1, 31)]
    )
    rank_profile = pari.matindexrank(without_q0)
    pivot_rows = [int(value) - 1 for value in list(rank_profile[0])]
    pivot_columns = [int(value) - 1 for value in list(rank_profile[1])]
    if len(pivot_rows) != 30 or pivot_columns != list(range(30)):
        raise ValueError(("wrong rank profile", pivot_rows, pivot_columns))

    determinant_values = []
    theta_values = []
    canonical_solution = None
    for configuration_index, configuration in enumerate(configurations):
        matrix, theta_value = (
            (first_matrix, first_theta)
            if configuration_index == 0
            else build_matrix(configuration)
        )
        minor = pari.matrix(
            30,
            30,
            [matrix[row, column] for row in pivot_rows for column in range(1, 31)],
        )
        determinant = pari.matdet(minor)
        if determinant == 0:
            raise ValueError(("pivot determinant vanished", configuration_index))
        right = pari.Col([-matrix[row, 0] for row in pivot_rows])
        rest = pari.matsolve(minor, right)
        solution = pari.Col([one] + [rest[index] for index in range(30)])
        replay = matrix * solution
        if any(replay[row] != 0 for row in range(60)):
            raise ValueError(("all-60 replay failed", configuration_index))
        if canonical_solution is None:
            canonical_solution = list(solution)
        determinant_values.append(determinant)
        theta_values.append(theta_value)

    if not all(
        left != right
        for index, left in enumerate(theta_values)
        for right in theta_values[index + 1 :]
    ):
        raise ValueError("theta does not separate all 36 double-sixes")
    theta_mod_prime = [value % prime for value in theta_coefficients]
    if any(horner(theta_mod_prime, value) != zero for value in theta_values):
        raise ValueError("R_theta(theta_D) failed at a paired double-six")
    theta_orbit_product = orbit_product(theta_values, zero, one)
    if any(
        actual != (expected * one)
        for actual, expected in zip(theta_orbit_product, theta_mod_prime)
    ):
        raise ValueError("theta orbit product does not equal R_theta modulo p")

    vandermonde = pari.matrix(
        36,
        36,
        [theta_value**power for theta_value in theta_values for power in range(36)],
    )
    determinant_column = pari.matrix(36, 1, determinant_values)
    determinant_interpolation = pari.matsolve(vandermonde, determinant_column)

    def prime_field_scalar(value):
        if value == 0:
            return 0
        if value**prime != value:
            raise ValueError("value does not descend to prime field")
        text = str(value)
        try:
            return int(text) % prime
        except ValueError:
            polynomial = pari(text)
            degree = int(pari.poldegree(polynomial, z))
            coefficients = [
                int(str(pari.polcoef(polynomial, exponent, z))) % prime
                for exponent in range(degree + 1)
            ]
            if any(coefficients[1:]):
                raise ValueError("prime-field lift has nonconstant residue")
            return coefficients[0]

    determinant_theta_coefficients = [
        prime_field_scalar(determinant_interpolation[power, 0]) for power in range(36)
    ]
    for theta_value, determinant in zip(theta_values, determinant_values):
        if horner(determinant_theta_coefficients, theta_value) != determinant:
            raise ValueError("determinant interpolation replay failed")
    determinant_norm = one
    for determinant in determinant_values:
        determinant_norm *= determinant
    determinant_norm_scalar = prime_field_scalar(determinant_norm)
    if determinant_norm_scalar == 0:
        raise ValueError("determinant norm vanished")

    def ff_vector(value):
        polynomial = pari(str(value))
        degree = max(0, int(pari.poldegree(polynomial, z)))
        coefficients = [
            int(str(pari.polcoef(polynomial, exponent, z))) % prime
            for exponent in range(degree + 1)
        ]
        coefficients.extend([0] * (extension_degree - len(coefficients)))
        if len(coefficients) != extension_degree:
            raise ValueError("bad finite-field vector length")
        return coefficients

    solution_vectors = [ff_vector(value) for value in canonical_solution]
    determinant_vectors = [ff_vector(value) for value in determinant_values]
    determinant_text = json.dumps(determinant_theta_coefficients, separators=(",", ":"))
    solution_text = json.dumps(solution_vectors, separators=(",", ":"))
    report = {
        "status": "PASS",
        "certificate_sha256": locks["certificate"],
        "payload_sha256": EXPECTED_PAYLOAD,
        "carrier_candidate_decompressed_sha256": locks["candidate"],
        "carrier_table_sha256": candidate_table_hash,
        "theta_coefficients_sha256": theta_hash,
        "prime": prime,
        "prime_proven": True,
        "all_denominators_units": True,
        "factor_degrees": factor_rows,
        "extension_degree": extension_degree,
        "meeting_count": len(meeting),
        "sixer_count": len(sixers),
        "double_six_count": len(configurations),
        "all_36_theta_values_distinct": True,
        "all_36_R_theta_at_theta_D_zero": True,
        "theta_orbit_product_equals_R_theta": True,
        "matrix_shape": [60, 31],
        "gauge_removed_monomials": sorted(map(list, GAUGE), reverse=True),
        "gauge_block_from_C56_cubic": gauge_block,
        "gauge_determinant": gauge_determinant,
        "gauge_invertible_over_Q": True,
        "row_order": "row=12*t_degree+d_degree, t_degree=0..4, d_degree=0..11",
        "column_order": MONOMIALS,
        "normalization_column": 0,
        "normalization_monomial": MONOMIALS[0],
        "normalization_q0_value": 1,
        "normalization_q0_nonzero": True,
        "pivot_rows_zero_based": pivot_rows,
        "pivot_columns_after_deleting_q0_zero_based": pivot_columns,
        "pivot_minor_rank": 30,
        "all_36_pivot_determinants_nonzero": True,
        "determinant_values_extension_vectors": determinant_vectors,
        "determinant_theta_coefficients_mod_p": determinant_theta_coefficients,
        "determinant_theta_coefficients_sha256": hashlib.sha256(
            determinant_text.encode()
        ).hexdigest(),
        "determinant_norm_mod_p": determinant_norm_scalar,
        "canonical_q_solution_extension_vectors": solution_vectors,
        "canonical_q_solution_sha256": hashlib.sha256(solution_text.encode()).hexdigest(),
        "all_36_times_60_replay_zero": True,
        "carrier_line_count_per_double_six": 12,
        "all_12_carrier_lines_distinct_per_double_six": True,
        "u0_hyperplane_contains_no_carrier_line": u0_avoids_every_carrier_line,
        "quartic_restriction_equation_count_per_double_six": 60,
    }
    report_text = json.dumps(report, sort_keys=True, separators=(",", ":"))
    print(report_text)
    print("report_sha256", hashlib.sha256(report_text.encode()).hexdigest())


if __name__ == "__main__":
    main()
