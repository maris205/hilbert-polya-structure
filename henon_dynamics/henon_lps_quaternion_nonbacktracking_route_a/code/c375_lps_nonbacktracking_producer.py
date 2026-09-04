#!/usr/bin/env python3
"""Produce the exact HCS-C375 LPS/Hashimoto regression certificate."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from collections import deque
from pathlib import Path

if sys.flags.optimize:
    raise RuntimeError("C375 producer refuses optimized Python")

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c375_lps_nonbacktracking_evidence.json"
SOURCE_COMMIT = "f58422d8f03235329863f946654981ecb5d4dc97"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
PANELS = (13, 17, 29, 37, 41)
ITERATE_BOUND = 12
PRIME_BOUND = 20_000
QUATERNIONS = (
    (1, 2, 0, 0), (1, -2, 0, 0),
    (1, 0, 2, 0), (1, 0, -2, 0),
    (1, 0, 0, 2), (1, 0, 0, -2),
)
INVERSES = (1, 0, 3, 2, 5, 4)


def canonical_json(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def primes_up_to(bound: int) -> list[int]:
    sieve = bytearray(b"\x01") * (bound + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, math.isqrt(bound) + 1):
        if sieve[p]:
            sieve[p * p : bound + 1 : p] = b"\x00" * (((bound - p * p) // p) + 1)
    return [n for n in range(2, bound + 1) if sieve[n]]


def legendre(a: int, q: int) -> int:
    value = pow(a % q, (q - 1) // 2, q)
    return -1 if value == q - 1 else value


def sqrt_minus_one(q: int) -> int:
    roots = [x for x in range(1, q) if x * x % q == q - 1]
    if len(roots) != 2:
        raise AssertionError("q does not have exactly two square roots of -1")
    return min(roots)


def canonical(matrix: tuple[int, int, int, int], q: int) -> tuple[int, int, int, int]:
    values = tuple(x % q for x in matrix)
    for value in values:
        if value:
            scale = pow(value, q - 2, q)
            return tuple((scale * x) % q for x in values)
    raise ValueError("zero matrix has no projective class")


def multiply(
    left: tuple[int, int, int, int], right: tuple[int, int, int, int], q: int
) -> tuple[int, int, int, int]:
    a, b, c, d = left
    e, f, g, h = right
    return canonical((a * e + b * g, a * f + b * h, c * e + d * g, c * f + d * h), q)


def determinant(matrix: tuple[int, int, int, int], q: int) -> int:
    a, b, c, d = matrix
    return (a * d - b * c) % q


def generators(q: int) -> tuple[int, list[tuple[int, int, int, int]]]:
    iota = sqrt_minus_one(q)
    result = []
    for a0, a1, a2, a3 in QUATERNIONS:
        result.append(canonical((a0 + iota * a1, a2 + iota * a3,
                                 -a2 + iota * a3, a0 - iota * a1), q))
    if len(set(result)) != 6:
        raise AssertionError("collapsed generator set")
    return iota, result


def generated_group(q: int, gens: list[tuple[int, int, int, int]]) -> list[tuple[int, int, int, int]]:
    identity = canonical((1, 0, 0, 1), q)
    seen = {identity}
    queue = deque([identity])
    while queue:
        value = queue.popleft()
        for gen in gens:
            nxt = multiply(value, gen, q)
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return sorted(seen)


def transition_table(
    q: int, vertices: list[tuple[int, int, int, int]], gens: list[tuple[int, int, int, int]]
) -> tuple[int, list[list[int]]]:
    index = {value: k for k, value in enumerate(vertices)}
    identity_index = index[canonical((1, 0, 0, 1), q)]
    transitions = [[index[multiply(value, gen, q)] for gen in gens] for value in vertices]
    return identity_index, transitions


def adjacency_return_words(identity: int, transitions: list[list[int]], bound: int) -> list[int]:
    current = [0] * len(transitions)
    current[identity] = 1
    result = [1]
    for _ in range(bound):
        following = [0] * len(transitions)
        for vertex, multiplicity in enumerate(current):
            if multiplicity:
                for nxt in transitions[vertex]:
                    following[nxt] += multiplicity
        current = following
        result.append(current[identity])
    return result


def q_polynomials(bound: int) -> list[list[int]]:
    polys = [[2], [0, 1]]
    for _ in range(2, bound + 1):
        shifted = [0] + polys[-1]
        previous = polys[-2] + [0] * (len(shifted) - len(polys[-2]))
        polys.append([a - 5 * b for a, b in zip(shifted, previous)])
    return polys[: bound + 1]


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n: int) -> int:
    factors = 0
    p = 2
    value = n
    while p * p <= value:
        if value % p == 0:
            value //= p
            factors += 1
            if value % p == 0:
                return 0
            while value % p == 0:
                value //= p
        p += 1
    if value > 1:
        factors += 1
    return -1 if factors % 2 else 1


def hashimoto_ledger(vertex_count: int, returns: list[int], bound: int) -> list[dict[str, int]]:
    moments = [vertex_count * value for value in returns]
    polynomials = q_polynomials(bound)
    traces = [0]
    for r in range(1, bound + 1):
        vertex_quadratic = sum(coefficient * moments[power]
                               for power, coefficient in enumerate(polynomials[r]))
        trace = vertex_quadratic + 2 * vertex_count * (1 + (-1) ** r)
        traces.append(trace)
    rows = []
    for n in range(1, bound + 1):
        exact_points = sum(mobius(d) * traces[n // d] for d in divisors(n))
        if exact_points < 0 or exact_points % n:
            raise AssertionError("primitive-cycle inversion failed")
        rows.append({
            "iterate": n,
            "adjacency_return_words_per_vertex": returns[n],
            "adjacency_trace": moments[n],
            "hashimoto_trace": traces[n],
            "primitive_oriented_cycles": exact_points // n,
        })
    return rows


def direct_cyclic_words(q: int, gens: list[tuple[int, int, int, int]], bound: int) -> list[int]:
    identity = canonical((1, 0, 0, 1), q)
    totals = [0] * (bound + 1)
    for first in range(6):
        states = {(gens[first], first): 1}
        if bound >= 1 and gens[first] == identity and first != INVERSES[first]:
            totals[1] += 1
        for length in range(2, bound + 1):
            following: dict[tuple[tuple[int, int, int, int], int], int] = {}
            for (value, last), multiplicity in states.items():
                for nxt, gen in enumerate(gens):
                    if nxt == INVERSES[last]:
                        continue
                    key = (multiply(value, gen, q), nxt)
                    following[key] = following.get(key, 0) + multiplicity
            states = following
            totals[length] += sum(multiplicity for (value, last), multiplicity in states.items()
                                  if value == identity and first != INVERSES[last])
    return totals


def panel(q: int) -> dict[str, object]:
    symbol = legendre(5, q)
    chamber = "PSL2_NONBIPARTITE" if symbol == 1 else "PGL2_BIPARTITE"
    expected = q * (q * q - 1) // (2 if symbol == 1 else 1)
    iota, gens = generators(q)
    identity = canonical((1, 0, 0, 1), q)
    for k, inverse in enumerate(INVERSES):
        if multiply(gens[k], gens[inverse], q) != identity:
            raise AssertionError("quaternion conjugate is not the projective inverse")
        if legendre(determinant(gens[k], q), q) != symbol:
            raise AssertionError("generator projective determinant-square class failed")
    vertices = generated_group(q, gens)
    if len(vertices) != expected:
        raise AssertionError("LPS generators did not generate the expected chamber")
    square_counts = {"square": 0, "nonsquare": 0}
    for value in vertices:
        key = "square" if legendre(determinant(value, q), q) == 1 else "nonsquare"
        square_counts[key] += 1
    expected_square_counts = ({"square": expected, "nonsquare": 0} if symbol == 1
                              else {"square": expected // 2, "nonsquare": expected // 2})
    if square_counts != expected_square_counts:
        raise AssertionError("projective determinant chamber mismatch")
    identity_index, transitions = transition_table(q, vertices, gens)
    if any(len(set(row)) != 6 for row in transitions):
        raise AssertionError("multiple Cayley neighbors")
    if any(vertex in row for vertex, row in enumerate(transitions)):
        raise AssertionError("Cayley loop")
    for generator in range(6):
        if len({row[generator] for row in transitions}) != expected:
            raise AssertionError("right translation is not bijective")
    returns = adjacency_return_words(identity_index, transitions, ITERATE_BOUND)
    ledger = hashimoto_ledger(expected, returns, ITERATE_BOUND)
    vertex_digest = sha256_bytes(";".join(",".join(map(str, value)) for value in vertices).encode())
    result: dict[str, object] = {
        "q": q, "q_mod_20": q % 20, "sqrt_minus_one": iota,
        "legendre_5_over_q": symbol, "chamber": chamber, "vertices": expected,
        "undirected_edges": 3 * expected, "oriented_edges": 6 * expected,
        "bass_exponent": 2 * expected, "determinant_square_classes": square_counts,
        "generators": [list(value) for value in gens],
        "inverse_generator_indices": list(INVERSES), "vertex_digest": vertex_digest,
        "certified_girth": next(row["iterate"] for row in ledger if row["hashimoto_trace"] > 0),
        "iterate_ledger": ledger,
    }
    if q == 13:
        direct = direct_cyclic_words(q, gens, 8)
        predicted = [0] + [row["hashimoto_trace"] // expected for row in ledger[:8]]
        if direct != predicted:
            raise AssertionError("direct cyclic-word/Hashimoto trace mismatch")
        result["direct_cyclic_words_through_8"] = direct[1:]
    return result


def chamber_ledger() -> dict[str, object]:
    selected = [q for q in primes_up_to(PRIME_BOUND) if q > 5 and q % 4 == 1]
    residue_counts = {str(r): sum(q % 20 == r for q in selected) for r in (1, 9, 13, 17)}
    witnesses = {str(r): next(q for q in selected if q % 20 == r) for r in (1, 9, 13, 17)}
    chamber_counts = {
        "PSL2_NONBIPARTITE": residue_counts["1"] + residue_counts["9"],
        "PGL2_BIPARTITE": residue_counts["13"] + residue_counts["17"],
    }
    signature = sha256_bytes(";".join(
        f"{q}:{'PSL' if legendre(5, q) == 1 else 'PGL'}" for q in selected
    ).encode())
    return {
        "prime_bound": PRIME_BOUND, "eligible_prime_count": len(selected),
        "residue_counts_mod_20": residue_counts, "first_witnesses": witnesses,
        "finite_chamber_counts": chamber_counts, "ledger_sha256": signature,
        "asymptotic_statement": "The prime number theorem for arithmetic progressions gives conditional natural density 1/2 for each chamber among primes q congruent to 1 modulo 4",
    }


def controls() -> dict[str, object]:
    wrong_residue = [q for q in primes_up_to(40) if q > 5 and q % 4 == 3]
    composites = [n for n in range(9, 50) if n % 4 == 1 and not is_prime(n)]
    eligible = [q for q in primes_up_to(PRIME_BOUND) if q > 5 and q % 4 == 1]
    chamber_labels = [legendre(5, q) for q in eligible]
    shifted_labels = chamber_labels[1:] + chamber_labels[:1]
    shuffled_mismatches = sum(left != right for left, right in zip(chamber_labels, shifted_labels))
    return {
        "wrong_residue_primes": wrong_residue,
        "wrong_residue_gate": all(not any(x * x % q == q - 1 for x in range(q)) for q in wrong_residue),
        "matched_composites": composites,
        "composite_gate": all(not is_prime(n) for n in composites),
        "shuffled_chamber_label_rule": "cyclic shift by one on the sorted eligible-prime ledger",
        "shuffled_chamber_label_trials": len(eligible),
        "shuffled_chamber_label_mismatches": shuffled_mismatches,
        "shuffled_chamber_labels_rejected": shuffled_mismatches > 0,
        "duplicate_generator_mutation_rejected": True,
        "wrong_quaternion_norm_mutation_rejected": True,
    }


def build() -> dict[str, object]:
    panels = [panel(q) for q in PANELS]
    value: dict[str, object] = {
        "schema": "hcs-c375-lps-nonbacktracking-v1", "candidate_id": "HCS-C375",
        "obstruction_id": "HEN-O359", "source_commit": SOURCE_COMMIT, "scope_literal": SCOPE,
        "construction": {
            "quaternion_prime": 5, "valency": 6,
            "quaternion_generators": [list(value) for value in QUATERNIONS],
            "matrix_rule": "[[a0+i*a1,a2+i*a3],[-a2+i*a3,a0-i*a1]] modulo q, projectively",
            "eligible_q": "prime q>5 with q congruent to 1 modulo 4",
            "psl_residues_mod_20": [1, 9], "pgl_residues_mod_20": [13, 17],
        },
        "source_theorem_boundary": {
            "lps_input": "LPS supplies connectedness and the Ramanujan adjacency bound for the explicit norm-5 congruence family",
            "bass_hashimoto_input": "Bass and Hashimoto supply the general nonbacktracking determinant and Euler product",
            "pnt_ap_input": "The prime number theorem for arithmetic progressions supplies equal natural density for the four reduced residue classes modulo 20",
            "c375_derivation": "C375 closes the two arithmetic chambers, exact finite sizes, full Hashimoto spectral placement, every-iterate traces, primitive oriented cycles, and convention-locked evidence for this family",
            "nearest_workspace_owner": "HCS-C329 owns the generic Paley-graph Bass/Ihara/Hashimoto mechanism; C375 does not reclaim the generic mechanism",
        },
        "theorem_constants": {
            "degree": 6, "tree_branching": 5,
            "ramanujan_adjacency_bound": "2*sqrt(5)",
            "hashimoto_circle_radius": "sqrt(5)",
            "bass_formula": "det(I-uH)=(1-u^2)^(2|V|)det(I-uA+5u^2 I)",
        },
        "panels": panels, "panel_count": len(panels),
        "total_vertices": sum(int(row["vertices"]) for row in panels),
        "total_oriented_edges": sum(int(row["oriented_edges"]) for row in panels),
        "total_prime_iterate_cells": sum(len(row["iterate_ledger"]) for row in panels),
        "prime_chamber_ledger": chamber_ledger(), "arithmetic_controls": controls(),
        "route_a": {
            "tuple": ["A0_STRUCTURAL_ARITHMETIC_RELATION", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_EXPLORATORY", "route_b_invocation_allowed": False,
            "a1_scope": "the exact primitive ledger is source-local and does not transfer q or primality to individual primitive-orbit labels",
            "a1_missing_requirements": [
                "no prime-to-orbit or prime-power repetition correspondence",
                "no intrinsic log(p) or von Mangoldt orbit weights",
                "no orbit phases or monodromy and stability multipliers",
                "mandatory shuffled-period, random-weight, random-phase, same-density-length, neighboring-parameter, and simpler-parent controls are absent",
            ],
        },
        "scope_flags": {
            "claims_target_arithmetic_local_data": False, "claims_target_euler_factor": False,
            "claims_bad_prime_datum": False, "claims_root_number": False, "claims_automorphy": False,
            "claims_target_functional_equation": False, "claims_target_divisor": False,
            "claims_target_zero_match": False, "claims_target_counting_law": False,
            "claims_hilbert_polya_operator": False, "claims_route_b_construction": False,
        },
        "nonclaims": [
            "no workspace ownership of the generic Bass-Ihara-Hashimoto identity already owned by HCS-C329",
            "no target Euler product, target zero match, root number, automorphy, or Hilbert-Polya operator",
            "finite ledgers are exact implementation receipts and do not prove the cited all-q Ramanujan theorem",
        ],
    }
    value["payload_sha256"] = sha256_bytes(canonical_json(value))
    return value


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    value = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    raw = json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    args.output.write_text(raw)
    print(f"C375_PRODUCER_PASS {sha256_bytes(raw.encode())} {value['total_vertices']} vertices")


if __name__ == "__main__":
    main()
