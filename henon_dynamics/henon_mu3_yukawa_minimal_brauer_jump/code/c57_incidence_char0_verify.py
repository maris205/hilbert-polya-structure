#!/usr/bin/env python3
"""Fast exact FLINT replay of the packaged H10/Q17 incidence identity."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re

import flint
from flint import fmpq, fmpq_poly

from c57_exact import (
    canonical_leaf_bytes,
    deterministic_gzip,
    read_stable,
    reject_optimized_python,
    require_exact_keys,
    sha256_bytes,
    strict_gzip_json,
    strict_json_loads,
)


REPO = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
CERTIFICATE = REPO / "henon_dynamics/henon_mu3_yukawa_line_field/results/c56_certificate.json"
WITNESS = PROJECT / "results/incidence_char0_witness.json.gz"
EXPECTED_CERTIFICATE_SHA256 = "26739ce5aedb4a3467645f9c1b2036d4d3eec9ce4d0dbce23d67ea7b67e5fbc4"
EXPECTED_PAYLOAD_SHA256 = "5b17c9ed7bea60680556af70297199b653d51188bb30ce59f7c2c6bfbc94f661"
EXPECTED_WITNESS_GZIP_SHA256 = "4853641b143d3d7d0c2086fbee13f9d1f191bac960a989e8e85aede117cf8060"
EXPECTED_WITNESS_RAW_SHA256 = "2c42ac21f43e54870b030c71facff31b0b0b5a05da544b7455f960e47448a392"
EXPECTED_H_TEXT_SHA256 = "b0f02a13ae60b01f1ec3d781896c5393853a75ff5fb0be517ae4c337c5f7007f"
EXPECTED_Q_TEXT_SHA256 = "ebf57460f2349972e99ecd6a4739a1c0e11521a65201c72a0be6665d91038a47"
EXPECTED_WITNESS_KEYS = {
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
EXPECTED_SEMANTIC_KEYS = {
    "certificate_sha256",
    "eliminant_degree",
    "formula",
    "lex_shape_text_sha256",
    "neighbour_polynomial_bytes",
    "neighbour_polynomial_sha256",
    "payload_sha256",
    "quotient_polynomial_bytes",
    "quotient_polynomial_sha256",
    "raw_output_bytes",
    "raw_output_sha256",
    "singular_input_bytes",
    "singular_input_sha256",
    "singular_summary",
}


class GateError(ValueError):
    """An exact arithmetic or lineage gate failed."""


TERM = re.compile(r"([+-]?)([0-9]+)/([0-9]+)(?:x([0-9]*))?")


def parse_x_polynomial(text: str) -> fmpq_poly:
    coefficients: dict[int, fmpq] = {}
    position = 0
    while position < len(text):
        match = TERM.match(text, position)
        if match is None:
            raise GateError(f"unparsed x-polynomial byte at {position}")
        sign, numerator, denominator, exponent_token = match.groups()
        degree = (
            0
            if exponent_token is None
            else (1 if exponent_token == "" else int(exponent_token))
        )
        value = fmpq(("-" if sign == "-" else "") + numerator + "/" + denominator)
        if degree in coefficients:
            raise GateError("duplicate x degree in locked normal form")
        coefficients[degree] = value
        position = match.end()
    if not coefficients:
        return fmpq_poly()
    result = [fmpq(0)] * (max(coefficients) + 1)
    for degree, value in coefficients.items():
        result[degree] = value
    return fmpq_poly(result)


def parse_y_polynomial(text: str, expected_degree: int) -> list[fmpq_poly]:
    if not text.endswith("\n") or "\n" in text[:-1]:
        raise GateError("locked polynomial must have exactly one terminal newline")
    value = text[:-1]
    lead = "y" + (str(expected_degree) if expected_degree != 1 else "")
    if not value.startswith(lead):
        raise GateError("wrong monic y leading term")
    position = len(lead)
    result = [fmpq_poly() for _ in range(expected_degree + 1)]
    result[expected_degree] = fmpq_poly([1])
    seen: set[int] = {expected_degree}
    while position < len(value):
        if not value.startswith("+(", position):
            raise GateError(f"wrong locked y normal form at {position}")
        start = position + 2
        end = value.find(")", start)
        if end < 0:
            raise GateError("unterminated y coefficient")
        coefficient = parse_x_polynomial(value[start:end])
        position = end + 1
        if value.startswith("*y", position):
            position += 2
            start_degree = position
            while position < len(value) and value[position].isdigit():
                position += 1
            degree = 1 if start_degree == position else int(value[start_degree:position])
        else:
            degree = 0
        if degree in seen or degree < 0 or degree >= expected_degree:
            raise GateError("duplicate/out-of-range y degree")
        seen.add(degree)
        result[degree] = coefficient
    if seen != set(range(expected_degree + 1)):
        raise GateError("locked y polynomial is not dense in coefficient slots")
    return result


def trim(poly: list[fmpq_poly]) -> list[fmpq_poly]:
    result = list(poly)
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def locked_inputs(certificate_path: Path, witness_path: Path):
    certificate_raw, certificate_fingerprint = read_stable(
        certificate_path, max_bytes=2_000_000
    )
    if certificate_fingerprint.sha256 != EXPECTED_CERTIFICATE_SHA256:
        raise GateError("C56 certificate source-lock mismatch")
    certificate = strict_json_loads(certificate_raw, max_bytes=2_000_000)
    payload = certificate["payload"]
    if (
        certificate.get("payload_sha256") != EXPECTED_PAYLOAD_SHA256
        or sha256_bytes(canonical_leaf_bytes(payload)) != EXPECTED_PAYLOAD_SHA256
    ):
        raise GateError("C56 canonical payload source-lock mismatch")

    witness, witness_raw, compressed_fingerprint = strict_gzip_json(
        witness_path,
        max_compressed_bytes=3_000_000,
        max_decompressed_bytes=6_000_000,
    )
    if (
        compressed_fingerprint.sha256 != EXPECTED_WITNESS_GZIP_SHA256
        or sha256_bytes(witness_raw) != EXPECTED_WITNESS_RAW_SHA256
    ):
        raise GateError("incidence witness compressed/decompressed lock mismatch")
    compressed, _ = read_stable(witness_path, max_bytes=3_000_000)
    if compressed != deterministic_gzip(witness_raw):
        raise GateError("incidence witness gzip encoding is not deterministic")
    require_exact_keys(witness, EXPECTED_WITNESS_KEYS, "incidence witness")
    expected_lineage = {
        "authority": "sole direct characteristic-zero implementation",
        "original_report_sha256": "e78be348627e751ceccd09bcca7f1d7651d9fdd126c9130d76db395eb911310f",
        "raw_output_sha256": "67414cb2437a8521f87844fd994cefc81bd7384115cc441270ab1066847c65ae",
        "schema_id": "hcs-c57-char0-incidence-witness-v1",
        "singular_input_sha256": "f48b391ac59b5dc2d9ec2137b16107b87ac27404058796965790f46f17d8cbb2",
        "source_sha256": "e72f7cd671f309873e4e61c8c16f8beff137161f3cb10c970c3f27bb7aef2654",
        "status": "DIRECT_SINGULAR_PASS",
    }
    for key, expected in expected_lineage.items():
        if witness[key] != expected:
            raise GateError(f"incidence witness lineage mismatch: {key}")
    if witness["pari_direct_lane"] != {
        "certificate_dependency": False,
        "status": "TIMEOUT_NON_RESULT",
    }:
        raise GateError("PARI direct-lane NON-RESULT firewall changed")
    if (
        witness["H_text_sha256"] != EXPECTED_H_TEXT_SHA256
        or sha256_bytes(witness["H_text"].encode()) != EXPECTED_H_TEXT_SHA256
        or witness["Q_text_sha256"] != EXPECTED_Q_TEXT_SHA256
        or sha256_bytes(witness["Q_text"].encode()) != EXPECTED_Q_TEXT_SHA256
    ):
        raise GateError("H/Q text lock mismatch")
    semantic = witness["report_semantic"]
    require_exact_keys(semantic, EXPECTED_SEMANTIC_KEYS, "Singular semantic lineage")
    if (
        semantic["certificate_sha256"] != EXPECTED_CERTIFICATE_SHA256
        or semantic["payload_sha256"] != EXPECTED_PAYLOAD_SHA256
        or semantic["formula"] != "J=-Da*Ab*Ac-Db*Dc*Aa"
    ):
        raise GateError("Singular semantic lineage mismatch")
    return certificate, witness


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("witness", nargs="?", type=Path, default=WITNESS)
    parser.add_argument("--certificate", type=Path, default=CERTIFICATE)
    arguments = parser.parse_args()
    reject_optimized_python()
    certificate, witness = locked_inputs(arguments.certificate, arguments.witness)
    rows = {
        row["leading_variable"]: row
        for row in certificate["payload"]["grassmann_main_chart"]["lex_shape"]
    }
    if set(rows) != {"a", "b", "c", "d"}:
        raise GateError("C56 lex-shape key mismatch")
    theorem_gates = certificate["payload"].get("theorem_gates")
    if (
        type(theorem_gates) is not dict
        or theorem_gates.get("eliminant_irreducible_over_Q") is not True
    ):
        raise GateError("frozen C56 irreducibility field gate is absent")
    g_coefficients = rows["d"]["tail_coefficients_d_0_up"]
    if len(g_coefficients) != 28 or any(type(value) is not int for value in g_coefficients):
        raise GateError("bad C56 eliminant coefficients")
    g_lead = g_coefficients[-1]
    modulus = fmpq_poly([fmpq(value, g_lead) for value in g_coefficients])
    if modulus.degree() != 27 or modulus.leading_coefficient() != 1:
        raise GateError("bad monic C56 field modulus")
    h_poly = parse_y_polynomial(witness["H_text"], 10)
    q_poly = parse_y_polynomial(witness["Q_text"], 17)
    if any(coefficient.degree() >= 27 for coefficient in h_poly + q_poly):
        raise GateError("H/Q coefficient is not reduced modulo g")
    if h_poly[-1] != 1 or q_poly[-1] != 1:
        raise GateError("H/Q monicity mismatch")

    zero = fmpq_poly()
    one = fmpq_poly([1])

    def kreduce(value: fmpq_poly) -> fmpq_poly:
        return value % modulus

    def kmul(left: fmpq_poly, right: fmpq_poly) -> fmpq_poly:
        if left == 0 or right == 0:
            return zero
        return (left * right) % modulus

    def ymul(left: list[fmpq_poly], right: list[fmpq_poly]) -> list[fmpq_poly]:
        output = [zero for _ in range(len(left) + len(right) - 1)]
        for i, a in enumerate(left):
            if a == 0:
                continue
            for j, b in enumerate(right):
                if b != 0:
                    output[i + j] = output[i + j] + kmul(a, b)
        return trim(output)

    def monic_division(dividend, divisor):
        if divisor[-1] != one:
            raise GateError("division requires a monic divisor")
        remainder = trim(dividend)
        quotient = [zero for _ in range(max(1, len(remainder) - len(divisor) + 1))]
        divisor_degree = len(divisor) - 1
        while len(remainder) - 1 >= divisor_degree and remainder != [zero]:
            shift = len(remainder) - len(divisor)
            lead = remainder[-1]
            quotient[shift] = lead
            for index in range(divisor_degree):
                remainder[shift + index] = remainder[shift + index] - kmul(
                    lead, divisor[index]
                )
            remainder[-1] = zero
            remainder = trim(remainder)
        return trim(quotient), trim(remainder)

    gy = [fmpq_poly([fmpq(value, g_lead)]) for value in g_coefficients]
    if ymul(h_poly, q_poly) != gy:
        raise GateError("g != H*Q in Q[x]/g[y]")
    quotient, g_remainder = monic_division(gy, h_poly)
    if g_remainder != [zero] or quotient != q_poly:
        raise GateError("independent monic division did not recover Q")

    x_powers = [one]
    x_element = fmpq_poly([0, 1])
    for _ in range(25):
        x_powers.append(kmul(x_powers[-1], x_element))

    def divided_difference(coefficients):
        if len(coefficients) != 27 or any(type(value) is not int for value in coefficients):
            raise GateError("bad divided-difference coefficient vector")
        output = []
        for y_degree in range(26):
            coefficient = zero
            for source_degree in range(y_degree + 1, 27):
                coefficient = coefficient + (
                    x_powers[source_degree - 1 - y_degree]
                    * coefficients[source_degree]
                )
            output.append(kreduce(coefficient))
        return trim(output)

    da = divided_difference(rows["a"]["tail_coefficients_d_0_up"])
    db = divided_difference(rows["b"]["tail_coefficients_d_0_up"])
    dc = divided_difference(rows["c"]["tail_coefficients_d_0_up"])
    aa = rows["a"]["leading_coefficient"]
    ab = rows["b"]["leading_coefficient"]
    ac = rows["c"]["leading_coefficient"]
    if any(type(value) is not int for value in (aa, ab, ac)):
        raise GateError("noninteger lex leading coefficient")
    db_times_dc = ymul(db, dc)
    j_poly = [zero for _ in range(max(len(da), len(db_times_dc)))]
    for index in range(len(j_poly)):
        first = da[index] * (-ab * ac) if index < len(da) else zero
        second = db_times_dc[index] * (-aa) if index < len(db_times_dc) else zero
        j_poly[index] = kreduce(first + second)
    j_poly = trim(j_poly)
    _, j_remainder = monic_division(j_poly, h_poly)
    if j_remainder != [zero]:
        raise GateError("H does not divide J")

    diagonal = zero
    x_power = one
    for coefficient in h_poly:
        diagonal = kreduce(diagonal + kmul(coefficient, x_power))
        x_power = kmul(x_power, x_element)
    if diagonal == 0:
        raise GateError("H(y=x)=0: diagonal factor survived")

    report = {
        "status": "PASS",
        "backend": {"implementation": "python-flint", "version": flint.__version__},
        "field": "Q[x]/(g(x))",
        "frozen_C56_irreducibility_used_for_field_gate": True,
        "formula": "J=-Da*Ab*Ac-Db*Dc*Aa",
        "degree_H": len(h_poly) - 1,
        "degree_Q": len(q_poly) - 1,
        "degree_J": len(j_poly) - 1,
        "H_monic": True,
        "Q_monic": True,
        "H_divides_J": True,
        "g_equals_H_times_Q": True,
        "independent_monic_division_recovers_Q": True,
        "char0_common_factor_degree": 10,
        "char0_gcd_degree_lower_bound": 10,
        "diagonal_evaluation_nonzero": True,
        "diagonal_gcd_degree_zero_over_locked_field": True,
        "gcd_equality_requires_good_prime_rank_specialization_report": True,
        "H_text_sha256": EXPECTED_H_TEXT_SHA256,
        "Q_text_sha256": EXPECTED_Q_TEXT_SHA256,
        "diagonal_normal_form_sha256": sha256_bytes(str(diagonal).encode("ascii")),
        "g_coefficients_sha256": sha256_bytes(canonical_leaf_bytes(g_coefficients)),
        "certificate_sha256": EXPECTED_CERTIFICATE_SHA256,
        "payload_sha256": EXPECTED_PAYLOAD_SHA256,
        "witness_compressed_sha256": EXPECTED_WITNESS_GZIP_SHA256,
        "witness_decompressed_sha256": EXPECTED_WITNESS_RAW_SHA256,
        "original_Singular_direct_report_sha256": witness["original_report_sha256"],
        "original_Singular_raw_output_sha256": witness["raw_output_sha256"],
        "original_Singular_source_sha256": witness["source_sha256"],
        "original_Singular_is_lineage_not_runtime_backend": True,
    }
    raw = json.dumps(report, sort_keys=True, separators=(",", ":"))
    print(raw)
    print("report_sha256", hashlib.sha256(raw.encode()).hexdigest())


if __name__ == "__main__":
    main()
