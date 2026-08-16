#!/usr/bin/python3
"""Finite-field bridge from the exact incidence carrier to C57 resolvents.

This script never sorts approximate complex residues.  It compares, at a good
prime, (i) the raw two-line determinant, (ii) its cleared divided-difference
polynomial J, and (iii) gcd(g,J_x) for every one of the 27 roots.  The graph
from J is then used to enumerate sixers/double-sixes and is checked against the
independent modular-resolvent implementation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from pathlib import Path
from itertools import combinations

from cypari2 import Pari
from c57_exact import (
    canonical_leaf_bytes,
    read_stable,
    reject_optimized_python,
    require_exact_keys,
    sha256_bytes,
    strict_gzip_json,
    strict_json_loads,
)


REPO = Path(__file__).resolve().parents[3]
CERT = str(
    REPO / "henon_dynamics/henon_mu3_yukawa_line_field/results/c56_certificate.json"
)
EXPECTED_CERTIFICATE_SHA256 = "26739ce5aedb4a3467645f9c1b2036d4d3eec9ce4d0dbce23d67ea7b67e5fbc4"
EXPECTED_PAYLOAD_SHA256 = "5b17c9ed7bea60680556af70297199b653d51188bb30ce59f7c2c6bfbc94f661"
EXPECTED_WITNESS_SHA256 = "2c42ac21f43e54870b030c71facff31b0b0b5a05da544b7455f960e47448a392"
EXPECTED_H_TEXT_SHA256 = "b0f02a13ae60b01f1ec3d781896c5393853a75ff5fb0be517ae4c337c5f7007f"
DEFAULT_WITNESS = (
    REPO
    / "henon_dynamics/henon_mu3_yukawa_minimal_brauer_jump/results"
    / "incidence_char0_witness.json.gz"
)
WITNESS_KEYS = {
    "H_text",
    "H_text_sha256",
    "Q_text",
    "Q_text_sha256",
    "authority",
    "original_report_sha256",
    "pari_direct_lane",
    "raw_output_sha256",
    "report_semantic",
    "runtime_milliseconds",
    "schema_id",
    "singular_input_sha256",
    "source_sha256",
    "status",
}
EXPECTED = {
    7: {
        "graph": "aaea1ca9c2fa5e0976583f3b8ae13d35b344623e637730ac3f85526ea7f3df38",
        "theta": "f1d7c83f82ba3936cbb7a8ed445028769b1ec4632be512f30f2e90b13f25aaa4",
        "oriented": "3d1cb6a947d7cd60e12da70da99f0f2af1eb51e9da91ca5cd97f9b6502ad780a",
        "delta": "4be9db739bc2581dac1641f6b19e0e46c5aa8c1d771ea1d1a5b54c7694a7782f",
    },
    37: {
        "graph": "72939b3118f6cc1d149340363bdbcbded623d3a900ab6c326dd6e72700bfe347",
        "theta": "9aa622e5c7ba83a91853915fbb1a38daebae84c202bb485c0bf22a1133145eed",
        "oriented": "1b4f132ee636d2c337157838c37cee1133995762791716658f42f77cfd32c1c8",
        "delta": "576e3bebfb5ef64309b154213eff372829b45388000062bd5b3499556484164b",
    },
    100000000000000000000000000000000000000000000012477: {
        "graph": "bf482b36a1f066939319b072d56d78bd511b1967b94550c8d709374ad1367bb8",
        "theta": "81ed199618ce5d4b6f988c81ef1f03bd53bad048bce90b54b14091728119bd81",
        "oriented": "d2b10380c703a421882319adacbd1aa2d255357b85fe53e7590f3443fce146d4",
        "delta": "eb0f5a21cc3846c949c5e09555bed763d21209020cdce839de215120d89be8ce",
    },
}


def digest(value) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def horner(coefficients, value):
    result = value * 0
    for coefficient in reversed(coefficients):
        result = result * value + coefficient
    return result


def quotient_at(coefficients, x):
    """Low-first coefficients of (p(T)-p(x))/(T-x)."""
    coefficients = list(coefficients)
    q = [x * 0] * (len(coefficients) - 1)
    q[-1] = coefficients[-1]
    for index in range(len(q) - 2, -1, -1):
        q[index] = coefficients[index + 1] + x * q[index + 1]
    return q


def add(left, right):
    zero = (left or right)[0] * 0
    out = [zero] * max(len(left), len(right))
    for index, value in enumerate(left):
        out[index] += value
    for index, value in enumerate(right):
        out[index] += value
    return out


def scale(coefficients, scalar):
    return [scalar * value for value in coefficients]


def multiply(left, right):
    zero = left[0] * 0
    out = [zero] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


TERM = re.compile(r"([+-]?)([0-9]+)(?:/([0-9]+))?(?:x([0-9]+)?)?")


def parse_h_coefficients(text):
    """Parse the frozen Singular H as low-first Q[x] coefficients by y-degree.

    The deliberately tiny grammar rejects whitespace, implicit parentheses,
    duplicate x powers, zero denominators, and every token except the exact
    output form emitted by the locked characteristic-zero computation.
    """
    if type(text) is not str or not text.endswith("\n"):
        raise ValueError("H text must have its frozen single trailing newline")
    source = text[:-1]
    if not source.startswith("y10+"):
        raise ValueError("H is not monic of y-degree ten")
    position = 4
    by_y = {10: [(1, 1)]}
    for y_degree in range(9, 0, -1):
        if position >= len(source) or source[position] != "(":
            raise ValueError("malformed H coefficient opening")
        y_token = "y" if y_degree == 1 else f"y{y_degree}"
        marker = f")*{y_token}+"
        end = source.find(marker, position)
        if end < 0:
            raise ValueError("malformed H coefficient delimiter")
        coefficient = source[position + 1 : end]
        position = end + len(marker)
        by_y[y_degree] = parse_x_coefficient(coefficient)
    if position >= len(source) or source[position] != "(" or not source.endswith(")"):
        raise ValueError("malformed H constant coefficient")
    by_y[0] = parse_x_coefficient(source[position + 1 : -1])
    return [by_y[degree] for degree in range(11)]


def parse_x_coefficient(source):
    if not source:
        raise ValueError("empty H coefficient")
    position = 0
    terms = {}
    while position < len(source):
        match = TERM.match(source, position)
        if match is None:
            raise ValueError("H coefficient is outside the frozen grammar")
        sign, numerator_text, denominator_text, exponent_text = match.groups()
        token = match.group(0)
        numerator = int(numerator_text)
        if sign == "-":
            numerator = -numerator
        denominator = int(denominator_text or "1")
        if denominator == 0:
            raise ValueError("zero denominator in H")
        has_x = "x" in token
        exponent = int(exponent_text or "1") if has_x else 0
        if exponent in terms:
            raise ValueError("duplicate x exponent in H coefficient")
        terms[exponent] = (numerator, denominator)
        position = match.end()
    if max(terms, default=-1) > 26:
        raise ValueError("H coefficient exceeds the field basis")
    return [terms.get(exponent, (0, 1)) for exponent in range(max(terms) + 1)]


def main():
    reject_optimized_python()
    parser = argparse.ArgumentParser()
    parser.add_argument("prime", nargs="?", type=int, default=7)
    parser.add_argument("--witness", type=Path, default=DEFAULT_WITNESS)
    args = parser.parse_args()
    prime = args.prime
    if prime not in EXPECTED:
        raise ValueError("prime is outside the frozen three-prime bridge")
    pari = Pari()
    if int(pari.isprime(prime)) != 1:
        raise ValueError("bridge modulus is not a proven prime")
    certificate_raw, certificate_fingerprint = read_stable(Path(CERT), max_bytes=2_000_000)
    if certificate_fingerprint.sha256 != EXPECTED_CERTIFICATE_SHA256:
        raise ValueError("C56 certificate source-lock mismatch")
    envelope = strict_json_loads(certificate_raw, max_bytes=2_000_000)
    payload = envelope["payload"]
    payload_hash = sha256_bytes(canonical_leaf_bytes(payload))
    if envelope.get("payload_sha256") != payload_hash or payload_hash != EXPECTED_PAYLOAD_SHA256:
        raise ValueError("C56 payload canonical digest mismatch")
    witness, witness_raw, _ = strict_gzip_json(
        args.witness,
        max_compressed_bytes=3_000_000,
        max_decompressed_bytes=6_000_000,
    )
    require_exact_keys(witness, WITNESS_KEYS, "characteristic-zero incidence witness")
    if sha256_bytes(witness_raw) != EXPECTED_WITNESS_SHA256:
        raise ValueError("characteristic-zero incidence witness source-lock mismatch")
    if witness["schema_id"] != "hcs-c57-char0-incidence-witness-v1":
        raise ValueError("wrong characteristic-zero incidence witness schema")
    if witness["H_text_sha256"] != EXPECTED_H_TEXT_SHA256:
        raise ValueError("H text digest mismatch")
    if sha256_bytes(witness["H_text"].encode()) != EXPECTED_H_TEXT_SHA256:
        raise ValueError("H text bytes mismatch")
    h_rational_coefficients = parse_h_coefficients(witness["H_text"])
    line_matrix = payload["we6"]["line_class_intersection_matrix"]
    if any(
        row.count(1) != 10 or row.count(0) != 16 or row.count(-1) != 1
        for row in line_matrix
    ):
        raise ValueError("frozen C56 line-class incidence is not 10/16/1")
    if sum(
        line_matrix[i][j] == 1
        for i in range(27) for j in range(i + 1, 27)
    ) != 135:
        raise ValueError("frozen C56 line-class incidence has wrong edge count")
    shape = payload["grassmann_main_chart"]["lex_shape"]
    rows = {row["leading_variable"]: row for row in shape}
    g_coefficients = rows["d"]["tail_coefficients_d_0_up"]
    if g_coefficients[-1] % prime == 0:
        raise ValueError("bad prime: eliminant leading coefficient vanishes")
    for variable in ("a", "b", "c"):
        if rows[variable]["leading_coefficient"] % prime == 0:
            raise ValueError(f"bad prime: {variable} denominator vanishes")

    g = pari.Polrev(g_coefficients)
    degree_rows = pari.factormod(g, prime, 1).python()
    extension_degree = 1
    for degree, multiplicity in degree_rows:
        if int(multiplicity) != 1:
            raise ValueError("bad prime: eliminant is inseparable")
        extension_degree = math.lcm(extension_degree, int(degree))
    z = pari("z")
    T = pari("T")
    generator = pari.ffgen(pari.ffinit(prime, extension_degree, z), z)
    roots = list(pari.polrootsmod(g, generator))
    if len(roots) != 27:
        raise ValueError(("wrong root count", len(roots)))

    parameters = []
    for root in roots:
        row = {"d": root}
        for variable in ("a", "b", "c"):
            shape_row = rows[variable]
            row[variable] = -horner(
                shape_row["tail_coefficients_d_0_up"], root
            ) / (shape_row["leading_coefficient"] % prime)
        parameters.append(row)

    determinant_edges = set()
    j_edges = set()
    for i, j in combinations(range(27), 2):
        left, right = parameters[i], parameters[j]
        determinant = (right["a"] - left["a"]) * (
            right["d"] - left["d"]
        ) - (right["b"] - left["b"]) * (
            right["c"] - left["c"]
        )
        if determinant == 0:
            determinant_edges.add((i, j))

        x, y = roots[i], roots[j]
        da = (
            horner(rows["a"]["tail_coefficients_d_0_up"], y)
            - horner(rows["a"]["tail_coefficients_d_0_up"], x)
        ) / (y - x)
        db = (
            horner(rows["b"]["tail_coefficients_d_0_up"], y)
            - horner(rows["b"]["tail_coefficients_d_0_up"], x)
        ) / (y - x)
        dc = (
            horner(rows["c"]["tail_coefficients_d_0_up"], y)
            - horner(rows["c"]["tail_coefficients_d_0_up"], x)
        ) / (y - x)
        aa = rows["a"]["leading_coefficient"] % prime
        ab = rows["b"]["leading_coefficient"] % prime
        ac = rows["c"]["leading_coefficient"] % prime
        j_value = -da * ab * ac - db * dc * aa
        if j_value == 0:
            j_edges.add((i, j))
    if determinant_edges != j_edges:
        raise ValueError("determinant and divided-difference graphs disagree")

    # For every root x, compute gcd(g(T),J_x(T)) over the splitting field.
    g_ff = pari.Polrev([generator * 0 + c for c in g_coefficients], T)
    gcd_degrees = []
    gcd_neighbour_sets = []
    diagonal_avoided = []
    h_specializations_equal_monic_gcd = []
    for i, x in enumerate(roots):
        da = quotient_at(rows["a"]["tail_coefficients_d_0_up"], x)
        db = quotient_at(rows["b"]["tail_coefficients_d_0_up"], x)
        dc = quotient_at(rows["c"]["tail_coefficients_d_0_up"], x)
        j_coefficients = add(
            scale(da, -(rows["b"]["leading_coefficient"] % prime)
                  * (rows["c"]["leading_coefficient"] % prime)),
            scale(multiply(db, dc),
                  -(rows["a"]["leading_coefficient"] % prime)),
        )
        j_poly = pari.Polrev(j_coefficients, T)
        gcd_poly = pari.gcd(g_ff, j_poly)
        gcd_degrees.append(int(pari.poldegree(gcd_poly)))
        gcd_poly = gcd_poly / pari.pollead(gcd_poly)
        h_y_coefficients = []
        for x_coefficients in h_rational_coefficients:
            reduced = []
            for numerator, denominator in x_coefficients:
                if denominator % prime == 0:
                    raise ValueError("H denominator is not a unit at bridge prime")
                reduced.append(
                    numerator % prime * pow(denominator % prime, -1, prime) % prime
                )
            h_y_coefficients.append(horner(reduced, x))
        h_mod_prime = pari.Polrev(h_y_coefficients, T)
        h_specializations_equal_monic_gcd.append(h_mod_prime == gcd_poly)
        diagonal_avoided.append(pari.subst(gcd_poly, T, x) != 0)
        neighbours = {
            j for j, y in enumerate(roots)
            if j != i and pari.subst(gcd_poly, T, y) == 0
        }
        gcd_neighbour_sets.append(neighbours)
        graph_neighbours = {
            j for j in range(27)
            if j != i and tuple(sorted((i, j))) in j_edges
        }
        if neighbours != graph_neighbours:
            raise ValueError(("gcd root set disagrees", i))

    degrees = [0] * 27
    for i, j in j_edges:
        degrees[i] += 1
        degrees[j] += 1
    if degrees != [10] * 27 or len(j_edges) != 135:
        raise ValueError(("not the Schlaefli meeting graph", degrees, len(j_edges)))
    if diagonal_avoided != [True] * 27:
        raise ValueError("the divided incidence carrier contains the diagonal")
    if h_specializations_equal_monic_gcd != [True] * 27:
        raise ValueError("packaged H does not equal the monic modular gcd")

    meeting = {frozenset(edge) for edge in j_edges}
    sixers = [
        frozenset(subset)
        for subset in combinations(range(27), 6)
        if all(frozenset((i, j)) not in meeting
               for i, j in combinations(subset, 2))
    ]
    double_sixes = set()
    for first in sixers:
        second = frozenset(
            i for i in range(27)
            if i not in first
            and sum(frozenset((i, j)) in meeting for j in first) == 5
        )
        if len(second) != 6:
            raise ValueError("wrong double-six complement")
        double_sixes.add(frozenset((first, second)))
    if len(sixers) != 72 or len(double_sixes) != 36:
        raise ValueError((len(sixers), len(double_sixes)))

    scale_alpha = g_coefficients[-1]
    zero = roots[0] * 0

    def orbit_product(values):
        coefficients = [generator**0]
        for value in values:
            product = [zero] * (len(coefficients) + 1)
            for index, coefficient in enumerate(coefficients):
                product[index] -= value * coefficient
                product[index + 1] += coefficient
            coefficients = product
        lifted = []
        for coefficient in coefficients:
            value = pari.lift(coefficient)
            if value == 0:
                lifted.append(0)
            else:
                if int(pari.poldegree(value)) > 0:
                    raise ValueError("independent orbit product did not descend")
                lifted.append(int(str(value)) % prime)
        return lifted

    theta_values = [
        sum(
            (scale_alpha * roots[index] for index in set().union(*double_six)),
            zero,
        )
        for double_six in double_sixes
    ]
    oriented_values = [
        sum((scale_alpha * roots[index] for index in sixer), zero)
        for sixer in sixers
    ]
    delta_values = []
    for double_six in double_sixes:
        first, second = tuple(double_six)
        beta = sum((scale_alpha * roots[index] for index in first), zero) - sum(
            (scale_alpha * roots[index] for index in second), zero
        )
        delta_values.append(beta**2)
    oriented_unique = []
    for value in oriented_values:
        if all(value != prior for prior in oriented_unique):
            oriented_unique.append(value)
    delta_unique = []
    for value in delta_values:
        if all(value != prior for prior in delta_unique):
            delta_unique.append(value)
    oriented_distinct_count = len(oriented_unique)
    delta_distinct_count = len(delta_unique)
    all_beta_nonzero = all(value != 0 for value in delta_values)
    independent_products = {
        "theta": orbit_product(theta_values),
        "oriented": orbit_product(oriented_values),
        "delta": orbit_product(delta_values),
    }

    graph_hash = digest(sorted(j_edges))
    observed = {
        "graph": graph_hash,
        "theta": digest(independent_products["theta"]),
        "oriented": digest(independent_products["oriented"]),
        "delta": digest(independent_products["delta"]),
    }
    if observed != EXPECTED[prime]:
        raise ValueError(("frozen bridge digest mismatch", observed))

    result = {
        "certificate_payload_sha256": envelope["payload_sha256"],
        "c56_line_class_intersection_matrix_sha256": (
            payload["we6"]["line_class_intersection_matrix_sha256"]
        ),
        "c56_line_class_degrees": [row.count(1) for row in line_matrix],
        "prime": prime,
        "prime_proven": True,
        "eliminant_leading_coefficient_nonzero": True,
        "shape_denominators_nonzero": True,
        "H_denominators_nonzero": True,
        "all_shape_denominators_units": True,
        "all_H_coefficient_denominators_units": True,
        "eliminant_squarefree": True,
        "g_squarefree_27_roots": True,
        "factor_degrees": degree_rows,
        "extension_degree": extension_degree,
        "root_count": len(roots),
        "determinant_equals_divided_J": True,
        "determinant_formula_equals_J": True,
        "meeting_count": len(j_edges),
        "meeting_graph_sha256": graph_hash,
        "line_degrees": degrees,
        "gcd_degrees": gcd_degrees,
        "gcd_root_sets_match_graph": True,
        "gcd_diagonal_avoided": True,
        "packaged_H_degree": 10,
        "packaged_H_monic": True,
        "packaged_H_mod_p_equals_monic_gcd_all_27": True,
        "rank_specialization_upper_bound_for_char0_gcd_degree": 10,
        "rank_specialization_direction": "degree_gcd_char0_le_degree_gcd_good_specialization",
        "incidence_witness_decompressed_sha256": sha256_bytes(witness_raw),
        "H_text_sha256": witness["H_text_sha256"],
        "sixer_count": len(sixers),
        "double_six_count": len(double_sixes),
        "oriented_sixer_distinct_values": oriented_distinct_count,
        "double_six_delta_distinct_values": delta_distinct_count,
        "all_36_beta_nonzero": all_beta_nonzero,
        "double_six_coefficients_sha256": digest(independent_products["theta"]),
        "oriented_sixer_coefficients_sha256": digest(independent_products["oriented"]),
        "orientation_square_coefficients_sha256": digest(independent_products["delta"]),
        "frozen_graph_digest_matches": True,
        "all_three_orbit_products_recomputed_independently": True,
        "orbit_products_bound_to_same_exact_graph_formula": True,
    }
    raw = json.dumps(result, sort_keys=True, separators=(",", ":"))
    print(raw)
    print("report_sha256", hashlib.sha256(raw.encode()).hexdigest())


if __name__ == "__main__":
    main()
