#!/usr/bin/python3
"""Independent finite-field double-six orbit product for one prime."""

import argparse
import hashlib
import json
import math
from pathlib import Path
from itertools import combinations

from cypari2 import Pari
from c57_exact import canonical_leaf_bytes, read_stable, reject_optimized_python, sha256_bytes, strict_json_loads


REPO = Path(__file__).resolve().parents[3]
CERT = str(
    REPO / "henon_dynamics/henon_mu3_yukawa_line_field/results/c56_certificate.json"
)
EXPECTED_CERTIFICATE_SHA256 = "26739ce5aedb4a3467645f9c1b2036d4d3eec9ce4d0dbce23d67ea7b67e5fbc4"
EXPECTED_PAYLOAD_SHA256 = "5b17c9ed7bea60680556af70297199b653d51188bb30ce59f7c2c6bfbc94f661"


def horner(coefficients, value):
    result = value * 0
    for coefficient in reversed(coefficients):
        result = result * value + coefficient
    return result


def restrict_surface_to_line(surface_rows, line):
    """Return coefficients of F(s,t,as+ct,bs+dt), low t-degree first."""
    a, b, c, d = (line[key] for key in ("a", "b", "c", "d"))
    zero = d * 0
    result = [zero for _ in range(4)]
    for row in surface_rows:
        coefficient = row["coefficient"]
        e0, e1, e2, e3 = row["exponents_u0_to_u3"]
        for i in range(e2 + 1):
            left = math.comb(e2, i) * a ** (e2 - i) * c**i
            for j in range(e3 + 1):
                t_degree = e1 + i + j
                result[t_degree] += (
                    coefficient
                    * left
                    * math.comb(e3, j)
                    * b ** (e3 - j)
                    * d**j
                )
    return result


def pairwise_distinct(values):
    return all(left != right for index, left in enumerate(values) for right in values[index + 1 :])


def digest(value):
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def modular_resolvent(prime):
    pari = Pari()
    if int(pari.isprime(prime)) != 1:
        raise ValueError("modulus is not a proven prime")
    certificate_raw, certificate_fingerprint = read_stable(Path(CERT), max_bytes=2_000_000)
    if certificate_fingerprint.sha256 != EXPECTED_CERTIFICATE_SHA256:
        raise ValueError("C56 certificate source-lock mismatch")
    envelope = strict_json_loads(certificate_raw, max_bytes=2_000_000)
    payload = envelope["payload"]
    payload_hash = sha256_bytes(canonical_leaf_bytes(payload))
    if envelope.get("payload_sha256") != payload_hash or payload_hash != EXPECTED_PAYLOAD_SHA256:
        raise ValueError("C56 payload canonical digest mismatch")
    if prime <= 3:
        raise ValueError("prime must exceed 3")
    shape = payload["grassmann_main_chart"]["lex_shape"]
    by_variable = {row["leading_variable"]: row for row in shape}
    g_coefficients = by_variable["d"]["tail_coefficients_d_0_up"]
    if g_coefficients[-1] % prime == 0:
        raise ValueError("leading coefficient vanishes")
    g = pari.Polrev(g_coefficients)
    degree_rows = pari.factormod(g, prime, 1).python()
    extension_degree = 1
    for row in degree_rows:
        degree = int(row[0])
        multiplicity = int(row[1])
        if multiplicity != 1:
            raise ValueError("inseparable eliminant")
        extension_degree = math.lcm(extension_degree, degree)
    z = pari("z")
    field_generator = pari.ffgen(
        pari.ffinit(prime, extension_degree, z), z
    )
    roots = list(pari.polrootsmod(g, field_generator))
    if len(roots) != 27:
        raise ValueError(("wrong root count", len(roots)))

    line_parameters = []
    for d in roots:
        values = {"d": d}
        for variable in ("a", "b", "c"):
            row = by_variable[variable]
            denominator = row["leading_coefficient"] % prime
            if denominator == 0:
                raise ValueError(("shape denominator vanishes", variable))
            values[variable] = -horner(
                row["tail_coefficients_d_0_up"], d
            ) / denominator
        line_parameters.append(values)
    if any(
        restrict_surface_to_line(
            payload["surface"]["primitive_coefficients"], line
        )
        != [roots[0] * 0] * 4
        for line in line_parameters
    ):
        raise ValueError("a reconstructed line does not lie on the cubic")

    meeting = set()
    for i, j in combinations(range(27), 2):
        left = line_parameters[i]
        right = line_parameters[j]
        residue = (left["a"] - right["a"]) * (
            left["d"] - right["d"]
        ) - (left["b"] - right["b"]) * (left["c"] - right["c"])
        if residue == 0:
            meeting.add(frozenset((i, j)))
    if len(meeting) != 135:
        raise ValueError(("wrong meeting count", len(meeting)))

    def skew(i, j):
        return frozenset((i, j)) not in meeting

    sixers = [
        frozenset(subset)
        for subset in combinations(range(27), 6)
        if all(skew(i, j) for i, j in combinations(subset, 2))
    ]
    if len(sixers) != 72:
        raise ValueError(("wrong sixer count", len(sixers)))
    double_sixes = set()
    for first in sixers:
        second = frozenset(
            i
            for i in range(27)
            if i not in first
            and sum(frozenset((i, j)) in meeting for j in first) == 5
        )
        if len(second) != 6:
            raise ValueError("wrong complement")
        double_sixes.add(frozenset((first, second)))
    if len(double_sixes) != 36:
        raise ValueError(("wrong double-six count", len(double_sixes)))

    scale = g_coefficients[-1]
    invariant_roots = []
    for double_six in double_sixes:
        indices = set().union(*double_six)
        invariant_roots.append(
            sum((scale * roots[index] for index in indices), roots[0] * 0)
        )
    double_six_distinct_values = 36 if pairwise_distinct(invariant_roots) else 0

    def orbit_product(root_values):
        coefficients = [field_generator**0]
        for invariant in root_values:
            product = [field_generator * 0] * (len(coefficients) + 1)
            for index, coefficient in enumerate(coefficients):
                product[index] -= invariant * coefficient
                product[index + 1] += coefficient
            coefficients = product
        lifted = []
        for coefficient in coefficients:
            value = pari.lift(coefficient)
            value_text = str(value)
            if value_text == "0":
                lifted.append(0)
                continue
            if int(pari.poldegree(value)) > 0:
                raise ValueError(("coefficient not in prime field", value))
            lifted.append(int(value_text) % prime)
        if lifted[-1] != 1:
            raise ValueError("nonmonic result")
        return lifted

    lifted = orbit_product(invariant_roots)
    oriented_invariant_roots = [
        sum((scale * roots[index] for index in sixer), roots[0] * 0)
        for sixer in sixers
    ]
    oriented_sixer_distinct_values = (
        len(oriented_invariant_roots) if pairwise_distinct(oriented_invariant_roots) else 0
    )
    oriented_lifted = orbit_product(oriented_invariant_roots)
    orientation_square_roots = []
    for double_six in double_sixes:
        first, second = tuple(double_six)
        first_sum = sum(
            (scale * roots[index] for index in first), roots[0] * 0
        )
        second_sum = sum(
            (scale * roots[index] for index in second), roots[0] * 0
        )
        orientation_square_roots.append((first_sum - second_sum) ** 2)
    orientation_square_distinct_values = (
        36 if pairwise_distinct(orientation_square_roots) else 0
    )
    all_beta_nonzero = all(value != 0 for value in orientation_square_roots)
    orientation_square_lifted = orbit_product(orientation_square_roots)
    if double_six_distinct_values != 36:
        raise ValueError(("theta values collide", double_six_distinct_values))
    return {
        "prime": prime,
        "proven_prime": True,
        "g_squarefree": True,
        "shape_denominators_nonzero": True,
        "all_27_line_restrictions_zero": True,
        "line_carrier_good_specialization": True,
        "extension_degree": extension_degree,
        "factor_degrees": degree_rows,
        "meeting_count": len(meeting),
        "meeting_graph_sha256": digest(
            sorted(tuple(sorted(edge)) for edge in meeting)
        ),
        "sixer_count": len(sixers),
        "double_six_count": len(double_sixes),
        "double_six_distinct_values": double_six_distinct_values,
        "oriented_sixer_distinct_values": oriented_sixer_distinct_values,
        "orientation_square_distinct_values": (
            orientation_square_distinct_values
        ),
        "all_36_beta_nonzero": all_beta_nonzero,
        "orientation_square_definition_replayed": True,
        "all_36_beta_squared_values_used_in_orbit_product": True,
        "same_double_six_pairing_for_theta_and_delta": True,
        "double_six_coefficients_mod_p": lifted,
        "oriented_sixer_coefficients_mod_p": oriented_lifted,
        "orientation_square_coefficients_mod_p": orientation_square_lifted,
    }


if __name__ == "__main__":
    reject_optimized_python()
    parser = argparse.ArgumentParser()
    parser.add_argument("prime", type=int)
    arguments = parser.parse_args()
    print(json.dumps(modular_resolvent(arguments.prime), separators=(",", ":")))
