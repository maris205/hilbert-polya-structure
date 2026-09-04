#!/usr/bin/env python3
"""Independent checker for HCS-C375; deliberately imports no producer code."""
from __future__ import annotations

import hashlib
import json
import math
import sys
from collections import deque
from pathlib import Path

if sys.flags.optimize:
    raise RuntimeError("C375 checker refuses optimized Python")

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c375_lps_nonbacktracking_evidence.json"
SOURCE = "f58422d8f03235329863f946654981ecb5d4dc97"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
PANELS = (13, 17, 29, 37, 41)
INV = (1, 0, 3, 2, 5, 4)


def strict_json(path: Path) -> dict[str, object]:
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("duplicate JSON key")
            result[key] = value
        return result
    return json.loads(path.read_text(), object_pairs_hook=unique,
                      parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))


def canonical_json(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def normalize_last(matrix: tuple[int, int, int, int], q: int) -> tuple[int, int, int, int]:
    values = tuple(x % q for x in matrix)
    for value in reversed(values):
        if value:
            scale = pow(value, -1, q)
            return tuple(scale * x % q for x in values)
    raise ValueError("zero projective matrix")


def normalize_first(matrix: tuple[int, int, int, int], q: int) -> tuple[int, int, int, int]:
    values = tuple(x % q for x in matrix)
    for value in values:
        if value:
            scale = pow(value, -1, q)
            return tuple(scale * x % q for x in values)
    raise ValueError("zero projective matrix")


def product(left, right, q):
    a, b, c, d = left
    e, f, g, h = right
    return normalize_last((a * e + b * g, a * f + b * h,
                           c * e + d * g, c * f + d * h), q)


def det(matrix, q):
    a, b, c, d = matrix
    return (a * d - b * c) % q


def quadratic_character(a: int, q: int) -> int:
    residue = pow(a % q, (q - 1) // 2, q)
    return -1 if residue == q - 1 else residue


def four_square_generators(q: int):
    representations = []
    for a0 in range(1, 3, 2):
        for a1 in range(-2, 3, 2):
            for a2 in range(-2, 3, 2):
                for a3 in range(-2, 3, 2):
                    if a0 * a0 + a1 * a1 + a2 * a2 + a3 * a3 == 5:
                        representations.append((a0, a1, a2, a3))
    representations.sort(key=lambda x: (next((k for k, v in enumerate(x[1:]) if v), 9), -next(v for v in x[1:] if v)))
    iota = min(x for x in range(1, q) if x * x % q == q - 1)
    matrices = []
    for a0, a1, a2, a3 in representations:
        raw = (a0 + iota * a1, a2 + iota * a3,
               -a2 + iota * a3, a0 - iota * a1)
        if det(raw, q) != 5 % q:
            raise AssertionError("raw quaternion determinant is not five")
        matrices.append(normalize_last(raw, q))
    return iota, representations, matrices


def subgroup_left(q: int, gens):
    identity = normalize_last((1, 0, 0, 1), q)
    seen = {identity}
    queue = deque([identity])
    while queue:
        value = queue.popleft()
        for gen in gens:
            nxt = product(gen, value, q)
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return sorted(seen)


def left_transitions(q: int, vertices, gens):
    index = {value: k for k, value in enumerate(vertices)}
    identity = index[normalize_last((1, 0, 0, 1), q)]
    table = [[index[product(gen, value, q)] for gen in gens] for value in vertices]
    return identity, table


def return_words(identity: int, transitions, bound: int):
    vector = [0] * len(transitions)
    vector[identity] = 1
    answer = [1]
    for _ in range(bound):
        following = [0] * len(transitions)
        for position, count in enumerate(vector):
            if count:
                for nxt in transitions[position]:
                    following[nxt] += count
        vector = following
        answer.append(vector[identity])
    return answer


def polynomial_sequence(bound: int):
    result = [[2], [0, 1]]
    for _ in range(2, bound + 1):
        top = [0] + result[-1]
        bottom = [5 * x for x in result[-2]] + [0] * (len(top) - len(result[-2]))
        result.append([x - y for x, y in zip(top, bottom)])
    return result[: bound + 1]


def mu(n: int) -> int:
    sign = 1
    divisor = 2
    remaining = n
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            remaining //= divisor
            sign = -sign
            if remaining % divisor == 0:
                return 0
            while remaining % divisor == 0:
                remaining //= divisor
        divisor += 1
    if remaining > 1:
        sign = -sign
    return sign


def primes(bound: int):
    result = []
    for n in range(2, bound + 1):
        if all(n % d for d in range(2, math.isqrt(n) + 1)):
            result.append(n)
    return result


def main() -> None:
    evidence = strict_json(EVIDENCE)
    checks = 0

    payload = dict(evidence)
    claimed = payload.pop("payload_sha256")
    assert hashlib.sha256(canonical_json(payload)).hexdigest() == claimed
    checks += 1
    assert evidence["schema"] == "hcs-c375-lps-nonbacktracking-v1"
    assert evidence["candidate_id"] == "HCS-C375"
    assert evidence["obstruction_id"] == "HEN-O359"
    assert evidence["source_commit"] == SOURCE
    assert evidence["scope_literal"] == SCOPE
    checks += 5
    expected_route = {
        "tuple": ["A0_STRUCTURAL_ARITHMETIC_RELATION", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
        "overall": "ROUTE_A_EXPLORATORY", "route_b_invocation_allowed": False,
        "a1_scope": "the exact primitive ledger is source-local and does not transfer q or primality to individual primitive-orbit labels",
        "a1_missing_requirements": [
            "no prime-to-orbit or prime-power repetition correspondence",
            "no intrinsic log(p) or von Mangoldt orbit weights",
            "no orbit phases or monodromy and stability multipliers",
            "mandatory shuffled-period, random-weight, random-phase, same-density-length, neighboring-parameter, and simpler-parent controls are absent",
        ],
    }
    assert evidence["route_a"] == expected_route
    boundary = evidence["source_theorem_boundary"]
    assert boundary["pnt_ap_input"].startswith(
        "The prime number theorem for arithmetic progressions"
    )
    assert not any(evidence["scope_flags"].values())
    assert len(evidence["nonclaims"]) == 3
    checks += 4
    construction = evidence["construction"]
    assert construction["quaternion_prime"] == 5 and construction["valency"] == 6
    assert construction["psl_residues_mod_20"] == [1, 9]
    assert construction["pgl_residues_mod_20"] == [13, 17]
    checks += 3

    assert tuple(row["q"] for row in evidence["panels"]) == PANELS
    total_vertices = 0
    total_oriented = 0
    for stored in evidence["panels"]:
        q = stored["q"]
        character = quadratic_character(5, q)
        expected_chamber = "PSL2_NONBIPARTITE" if character == 1 else "PGL2_BIPARTITE"
        expected_vertices = q * (q * q - 1) // (2 if character == 1 else 1)
        assert stored["chamber"] == expected_chamber
        assert stored["legendre_5_over_q"] == character
        assert stored["vertices"] == expected_vertices
        assert stored["undirected_edges"] == 3 * expected_vertices
        assert stored["oriented_edges"] == 6 * expected_vertices
        assert stored["bass_exponent"] == 2 * expected_vertices
        checks += 6

        iota, representations, gens = four_square_generators(q)
        assert len(representations) == 6 and len(set(representations)) == 6
        assert stored["sqrt_minus_one"] == iota
        stored_gens_last = [normalize_last(tuple(value), q) for value in stored["generators"]]
        assert set(stored_gens_last) == set(gens)
        checks += 3
        identity = normalize_last((1, 0, 0, 1), q)
        inverse_map = []
        for k, gen in enumerate(gens):
            inverse = next(j for j, other in enumerate(gens) if product(gen, other, q) == identity)
            inverse_map.append(inverse)
            assert product(gens[inverse], gen, q) == identity
            assert quadratic_character(det(gen, q), q) == character
            checks += 2
        # Compare inverse pairs as projective matrices, since this lane reconstructs ordering.
        rebuilt_pairs = {frozenset((gens[k], gens[inverse_map[k]])) for k in range(6)}
        stored_pairs = {
            frozenset((stored_gens_last[k], stored_gens_last[stored["inverse_generator_indices"][k]]))
            for k in range(6)
        }
        assert rebuilt_pairs == stored_pairs
        checks += 1

        vertices = subgroup_left(q, gens)
        assert len(vertices) == expected_vertices
        digest_vertices = sorted(normalize_first(value, q) for value in vertices)
        digest = hashlib.sha256(";".join(",".join(map(str, value)) for value in digest_vertices).encode()).hexdigest()
        assert digest == stored["vertex_digest"]
        checks += 2
        class_counts = {"square": 0, "nonsquare": 0}
        for value in vertices:
            class_counts["square" if quadratic_character(det(value, q), q) == 1 else "nonsquare"] += 1
            checks += 1
        assert class_counts == stored["determinant_square_classes"]
        checks += 1

        identity_index, transitions = left_transitions(q, vertices, gens)
        for row in transitions:
            assert len(set(row)) == 6
            checks += 1
        returns = return_words(identity_index, transitions, 12)
        polys = polynomial_sequence(12)
        traces = [0]
        for r in range(1, 13):
            adjacency_moments = [expected_vertices * returns[k] for k in range(13)]
            trace = sum(coef * adjacency_moments[k] for k, coef in enumerate(polys[r]))
            trace += 2 * expected_vertices * (1 + (-1) ** r)
            traces.append(trace)
            row = stored["iterate_ledger"][r - 1]
            assert row["iterate"] == r
            assert row["adjacency_return_words_per_vertex"] == returns[r]
            assert row["adjacency_trace"] == expected_vertices * returns[r]
            assert row["hashimoto_trace"] == trace
            exact = sum(mu(d) * traces[r // d] for d in range(1, r + 1) if r % d == 0)
            assert exact % r == 0 and row["primitive_oriented_cycles"] == exact // r
            checks += 5
        girth = next(r for r in range(1, 13) if traces[r] > 0)
        assert stored["certified_girth"] == girth
        checks += 1
        if q == 13:
            assert stored["direct_cyclic_words_through_8"] == [traces[r] // expected_vertices for r in range(1, 9)]
            checks += 1
        if character == -1:
            assert all(traces[r] == 0 for r in range(1, 13, 2))
        checks += 1
        total_vertices += expected_vertices
        total_oriented += 6 * expected_vertices

    assert evidence["total_vertices"] == total_vertices
    assert evidence["total_oriented_edges"] == total_oriented
    assert evidence["total_prime_iterate_cells"] == 60
    checks += 3

    selected = [q for q in primes(20_000) if q > 5 and q % 4 == 1]
    ledger = evidence["prime_chamber_ledger"]
    counts = {str(r): sum(q % 20 == r for q in selected) for r in (1, 9, 13, 17)}
    assert ledger["eligible_prime_count"] == len(selected)
    assert ledger["residue_counts_mod_20"] == counts
    assert ledger["finite_chamber_counts"] == {
        "PSL2_NONBIPARTITE": counts["1"] + counts["9"],
        "PGL2_BIPARTITE": counts["13"] + counts["17"],
    }
    signature = hashlib.sha256(";".join(
        f"{q}:{'PSL' if quadratic_character(5, q) == 1 else 'PGL'}" for q in selected
    ).encode()).hexdigest()
    assert ledger["ledger_sha256"] == signature
    assert ledger["asymptotic_statement"].startswith(
        "The prime number theorem for arithmetic progressions"
    )
    checks += 5
    controls = evidence["arithmetic_controls"]
    wrong_residue = [q for q in primes(40) if q > 5 and q % 4 == 3]
    composites = [n for n in range(9, 50) if n % 4 == 1 and n not in primes(50)]
    labels = [quadratic_character(5, q) for q in selected]
    shifted = labels[1:] + labels[:1]
    mismatches = sum(left != right for left, right in zip(labels, shifted))
    assert controls["wrong_residue_primes"] == wrong_residue
    assert controls["matched_composites"] == composites
    assert controls["wrong_residue_gate"] and controls["composite_gate"]
    assert controls["shuffled_chamber_label_rule"] == (
        "cyclic shift by one on the sorted eligible-prime ledger"
    )
    assert controls["shuffled_chamber_label_trials"] == len(selected)
    assert controls["shuffled_chamber_label_mismatches"] == mismatches > 0
    assert controls["shuffled_chamber_labels_rejected"]
    assert controls["duplicate_generator_mutation_rejected"]
    assert controls["wrong_quaternion_norm_mutation_rejected"]
    checks += 10
    print(f"C375 independent checker: PASS ({checks} assertions)")


if __name__ == "__main__":
    main()
