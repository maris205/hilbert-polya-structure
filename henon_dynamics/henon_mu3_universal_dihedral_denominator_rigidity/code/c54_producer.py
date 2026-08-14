#!/usr/bin/env python3
"""Produce the exact HCS-C54 universal-symmetry/rigidity certificate.

The computation has no floating-point or fixed-Frobenius input.  It combines
symbolic all-n formulae with finite exact mutation guards and an exact
Q(rho)-linear Cayley--Jacobian calculation at n=3.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
from itertools import combinations, product
import json
import os
from pathlib import Path
import subprocess
import sys


PROJECT = Path(__file__).resolve().parents[1]
REPO = Path(__file__).resolve().parents[3]
C53_RELATIVE = (
    "henon_dynamics/henon_mu3_dihedral_core_rational_descent/"
    "results/c53_certificate.json"
)
C53_ROUTE_RELATIVE = (
    "henon_dynamics/henon_mu3_dihedral_core_rational_descent/"
    "route_a_evaluation.yaml"
)
C53_PATH = REPO / C53_RELATIVE
C53_CERTIFICATE_SHA256 = (
    "f4325a5987933e2acf81656389d46701d82d38912c546d1e5996123f617f6e79"
)
C53_PAYLOAD_SHA256 = (
    "8064224eda63fa9d890efd26ec9aa167c7cd9458662620be3135196a09494d41"
)
C53_IMPLEMENTATION_COMMIT = "0a7f0fdb8290eab4aa92ed5ade432401c40c22cf"
C53_PROVENANCE_COMMIT = "9d509d3b3826b7bfbdb38ed9fe4dac9297f5dbdf"
C53_ROUTE_SHA256 = "ae508e6e41523559f014f6fbcd0c4c199229f221fe6ac915a75cd27b02e73719"
C53_INDEPENDENT_CHECK_SHA256 = (
    "0d38643ded626c2a5e1536c8a4df9c56ae98c4fda01e1d15660996ea8c495e67"
)
C53_CODE_RESULTS_MANIFEST_SHA256 = (
    "b62f353d119d6c8565f513dad771a047a5e6343411d08ad2e91562fe84923480"
)


def canonical_json(value) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def parse_c53_route_release_tuple(raw: bytes) -> dict[str, str]:
    """Parse the exact top-level/release hash keys needed for the C53 lock."""
    text = raw.decode("utf-8")
    top_level: dict[str, str] = {}
    release_hashes: dict[str, str] = {}
    parent = None
    for line_number, line in enumerate(text.splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if "\t" in line[: len(line) - len(line.lstrip())]:
            raise AssertionError(f"tab indentation in C53 Route line {line_number}")
        indent = len(line) - len(line.lstrip(" "))
        stripped = line.strip()
        if indent == 0:
            key, separator, value = stripped.partition(":")
            if not separator or not key:
                raise AssertionError(f"malformed C53 Route line {line_number}")
            if key in top_level:
                raise AssertionError(f"duplicate C53 Route top-level key: {key}")
            top_level[key] = value.strip()
            parent = key if not value.strip() else None
        elif indent == 2 and parent == "release_candidate_hashes":
            key, separator, value = stripped.partition(":")
            if not separator or not key or not value.strip():
                raise AssertionError(f"malformed C53 release hash line {line_number}")
            if key in release_hashes:
                raise AssertionError(f"duplicate C53 release hash key: {key}")
            release_hashes[key] = value.strip()

    assert top_level["candidate_id"] == "HCS-C53"
    assert top_level["documentation_status"] == "DOCS_FINAL_NO_MORE_EDITS"
    assert top_level["code_results_status"] == "RELEASE_CANDIDATE"
    assert set(release_hashes) == {
        "certificate",
        "payload",
        "independent_check",
        "code_results_manifest",
    }
    return {
        "implementation_commit": top_level["code_commit"],
        "certificate_sha256": release_hashes["certificate"],
        "payload_sha256": release_hashes["payload"],
        "independent_check_sha256": release_hashes["independent_check"],
        "code_results_manifest_sha256": release_hashes["code_results_manifest"],
    }


def strict_source_lock() -> dict:
    raw = C53_PATH.read_bytes()
    assert sha256_bytes(raw) == C53_CERTIFICATE_SHA256
    certificate = json.loads(raw)
    assert set(certificate) == {"schema", "payload", "payload_sha256"}
    assert certificate["schema"] == "hcs-c53-certificate-v1"
    assert certificate["payload_sha256"] == C53_PAYLOAD_SHA256
    assert sha256_bytes(canonical_json(certificate["payload"]).encode()) == C53_PAYLOAD_SHA256
    passport = certificate["payload"]["material_passport"]
    assert passport["candidate_id"] == "HCS-C53"
    assert passport["artifact_status"] == "RELEASE_CANDIDATE"
    committed_certificate = subprocess.run(
        ["git", "show", f"{C53_IMPLEMENTATION_COMMIT}:{C53_RELATIVE}"],
        cwd=REPO,
        check=True,
        capture_output=True,
    ).stdout
    assert sha256_bytes(committed_certificate) == C53_CERTIFICATE_SHA256
    subprocess.run(
        ["git", "cat-file", "-e", f"{C53_PROVENANCE_COMMIT}^{{commit}}"],
        cwd=REPO,
        check=True,
        capture_output=True,
    )
    subprocess.run(
        ["git", "merge-base", "--is-ancestor", C53_IMPLEMENTATION_COMMIT, C53_PROVENANCE_COMMIT],
        cwd=REPO,
        check=True,
        capture_output=True,
    )
    committed_route = subprocess.run(
        ["git", "show", f"{C53_PROVENANCE_COMMIT}:{C53_ROUTE_RELATIVE}"],
        cwd=REPO,
        check=True,
        capture_output=True,
    ).stdout
    assert sha256_bytes(committed_route) == C53_ROUTE_SHA256
    route_release_tuple = parse_c53_route_release_tuple(committed_route)
    assert route_release_tuple == {
        "implementation_commit": C53_IMPLEMENTATION_COMMIT,
        "certificate_sha256": C53_CERTIFICATE_SHA256,
        "payload_sha256": C53_PAYLOAD_SHA256,
        "independent_check_sha256": C53_INDEPENDENT_CHECK_SHA256,
        "code_results_manifest_sha256": C53_CODE_RESULTS_MANIFEST_SHA256,
    }
    return {
        "candidate_id": "HCS-C53",
        "path": C53_RELATIVE,
        "schema": certificate["schema"],
        "certificate_sha256": C53_CERTIFICATE_SHA256,
        "payload_sha256": C53_PAYLOAD_SHA256,
        "artifact_status": passport["artifact_status"],
        "semisimplicity_certified_by_C53": False,
        "implementation_commit": C53_IMPLEMENTATION_COMMIT,
        "provenance_commit": C53_PROVENANCE_COMMIT,
        "route_path": C53_ROUTE_RELATIVE,
        "route_sha256": C53_ROUTE_SHA256,
        "route_release_tuple": route_release_tuple,
        "commit_lock_status": "VERIFIED_GIT_OBJECT_CERTIFICATE_AND_COMMITTED_ROUTE_TUPLE",
    }


# Projective monomial maps are output-coordinate substitutions
# x_i -> rho^e_i x_{p_i}, normalized by e_0=0.
Map = tuple[tuple[int, ...], tuple[int, ...]]


def normalize_map(item: Map) -> Map:
    permutation, phases = item
    scalar = phases[0]
    return permutation, tuple((phase - scalar) % 3 for phase in phases)


def compose(left: Map, right: Map) -> Map:
    pl, el = left
    pr, er = right
    return normalize_map(
        (
            tuple(pr[pl[i]] for i in range(len(pl))),
            tuple((el[i] + er[pl[i]]) % 3 for i in range(len(pl))),
        )
    )


def inverse(item: Map) -> Map:
    permutation, phases = item
    inverse_permutation = [0] * len(permutation)
    for index, image in enumerate(permutation):
        inverse_permutation[image] = index
    return normalize_map(
        (
            tuple(inverse_permutation),
            tuple((-phases[inverse_permutation[index]]) % 3 for index in range(len(permutation))),
        )
    )


def power(item: Map, exponent: int) -> Map:
    identity = (tuple(range(len(item[0]))), (0,) * len(item[0]))
    result = identity
    for _ in range(exponent):
        result = compose(result, item)
    return result


def map_order(item: Map, bound: int) -> int:
    identity = (tuple(range(len(item[0]))), (0,) * len(item[0]))
    result = identity
    for exponent in range(1, bound + 1):
        result = compose(result, item)
        if result == identity:
            return exponent
    raise AssertionError("order bound exhausted")


def support_permutation(n: int, kind: str, shift: int) -> tuple[int, ...]:
    N = 2 * n
    if kind == "rotation":
        return tuple((i + shift) % N for i in range(N))
    assert kind == "reflection"
    return tuple((shift - i) % N for i in range(N))


def edge_lift(n: int, kind: str, shift: int, q: int) -> Map | None:
    """Solve the phase recurrence, returning None exactly on nonclosure."""
    N = 2 * n
    closing = [0] * N
    closing[-1] = 1
    permutation = support_permutation(n, kind, shift)
    phases = [0] * N
    for edge in range(N):
        a = permutation[edge]
        b = permutation[(edge + 1) % N]
        target_edge = a if (a + 1) % N == b else b
        next_phase = (q + closing[target_edge] - closing[edge] - phases[edge]) % 3
        if edge < N - 1:
            phases[edge + 1] = next_phase
        elif next_phase != phases[0]:
            return None
    return normalize_map((permutation, tuple(phases)))


def quadric_scale(item: Map) -> int | None:
    permutation, phases = item
    N = len(permutation)
    closing = {tuple(sorted((i, (i + 1) % N))): int(i == N - 1) for i in range(N)}
    transformed: dict[tuple[int, int], int] = {}
    for edge in range(N):
        target = tuple(sorted((permutation[edge], permutation[(edge + 1) % N])))
        transformed[target] = (int(edge == N - 1) + phases[edge] + phases[(edge + 1) % N]) % 3
    differences = {(transformed[edge] - value) % 3 for edge, value in closing.items()}
    return differences.pop() if len(differences) == 1 else None


def recurrence_group(n: int) -> tuple[dict[Map, int], dict[str, int]]:
    N = 2 * n
    group: dict[Map, int] = {}
    support_counts = {"rotation": 0, "reflection": 0}
    for kind in ("rotation", "reflection"):
        for shift in range(N):
            lifts = []
            for q in range(3):
                item = edge_lift(n, kind, shift, q)
                if item is not None:
                    lifts.append((item, q))
            if lifts:
                assert len(lifts) == 3
                assert (shift % 2 == 0) if kind == "rotation" else (shift % 2 == 1)
                support_counts[kind] += 1
                for item, q in lifts:
                    assert quadric_scale(item) == q
                    group[item] = q
    assert support_counts == {"rotation": n, "reflection": n}
    assert len(group) == 6 * n
    return group, support_counts


def brute_force_group(n: int) -> dict[Map, int]:
    N = 2 * n
    result: dict[Map, int] = {}
    supports = {
        support_permutation(n, kind, shift)
        for kind in ("rotation", "reflection")
        for shift in range(N)
    }
    for permutation in supports:
        for tail in product(range(3), repeat=N - 1):
            item = (permutation, (0,) + tail)
            q = quadric_scale(item)
            if q is not None:
                result[item] = q
    return result


def generators(n: int) -> tuple[Map, Map]:
    N = 2 * n
    r = normalize_map(
        (
            tuple((i + 2) % N for i in range(N)),
            tuple(1 if i == N - 2 else 2 if i == N - 1 else 0 for i in range(N)),
        )
    )
    s = normalize_map(
        (
            tuple((1 - i) % N for i in range(N)),
            tuple(1 if i == 1 or (i >= 2 and i % 2 == 0) else 0 for i in range(N)),
        )
    )
    return r, s


def group_control(n: int) -> dict:
    group, support_counts = recurrence_group(n)
    r, s = generators(n)
    identity = (tuple(range(2 * n)), (0,) * (2 * n))
    assert r in group and s in group
    assert quadric_scale(r) == 0 and quadric_scale(s) == 1
    assert map_order(r, 3 * n) == 3 * n
    assert power(s, 2) == identity
    assert compose(compose(s, r), s) == inverse(r)
    generated = {power(r, k) for k in range(3 * n)} | {
        compose(power(r, k), s) for k in range(3 * n)
    }
    assert generated == set(group)
    rn = power(r, n)
    assert rn[0] == tuple(range(2 * n))
    assert rn[1] == tuple(i % 2 for i in range(2 * n))
    return {
        "n": n,
        "N": 2 * n,
        "order": len(group),
        "support_counts": support_counts,
        "lifts_per_surviving_support": 3,
        "rotation_generator_order": map_order(r, 3 * n),
        "reflection_generator_order": map_order(s, 2),
        "dihedral_relation": True,
        "generated_equals_exhaustive_list": True,
        "r_power_n_alternating_kernel": True,
    }


def tau_map(item: Map) -> Map:
    return item[0], tuple((-phase) % 3 for phase in item[1])


def descent_map(n: int) -> Map:
    N = 2 * n
    return normalize_map(
        (
            tuple((-i) % N for i in range(N)),
            tuple(1 if i != 0 and i % 2 == 0 else 0 for i in range(N)),
        )
    )


def delta(n: int, item: Map) -> Map:
    M = descent_map(n)
    return compose(compose(M, tau_map(item)), inverse(M))


def fixed_elements(n: int) -> list[str]:
    modulus = 3 * n
    rotations = [k for k in range(modulus) if 2 * k % modulus == 0]
    reflections = [k for k in range(modulus) if (2 * k - 1) % modulus == 0]
    labels = ["1" if k == 0 else f"r^{k}" for k in rotations]
    labels.extend(f"r^{k}*s" for k in reflections)
    return labels


def rational_form_control(n: int) -> dict:
    r, s = generators(n)
    assert delta(n, r) == inverse(r)
    assert delta(n, s) == compose(r, s)
    assert delta(n, delta(n, r)) == r
    assert delta(n, delta(n, s)) == s
    # The normal forms r^k and r^k s turn the full fixed-point enumeration
    # into the two exact congruences below.  This avoids using a finite scan
    # as a surrogate for the all-n proof.
    modulus = 3 * n
    actual_fixed_count = sum(2 * k % modulus == 0 for k in range(modulus))
    actual_fixed_count += sum((2 * k - 1) % modulus == 0 for k in range(modulus))
    assert actual_fixed_count == 2
    expected = fixed_elements(n)
    expected_labels = (
        ["1", f"r^{3*n//2}"]
        if n % 2 == 0
        else ["1", f"r^{(3*n+1)//2}*s"]
    )
    assert expected == expected_labels
    return {
        "n": n,
        "geometric_rank": 6 * n,
        "fixed_geometric_elements": expected,
        "fixed_count": actual_fixed_count,
        "nonconstant": actual_fixed_count < 6 * n,
        "delta_involution_from_generator_presentation": True,
    }


def packet_ranks(n: int) -> tuple[int, int]:
    e = (4**n + 5) // 3
    o = 2 * (4**n - 4) // 3
    assert o == 2 * (e - 3)
    return e, o


def divisor_row(n: int) -> dict:
    e, o = packet_ranks(n)
    return {
        "n": n,
        "e_n": e,
        "o_n": o,
        "4e_mod_n": 4 * e % n,
        "4o_mod_n": 4 * o % n,
        "both_rails_integral": 4 * e % n == 0 and 4 * o % n == 0,
    }


# Exact arithmetic in Q(rho), rho^2+rho+1=0.
Pair = tuple[Fraction, Fraction]
K_ZERO: Pair = (Fraction(0), Fraction(0))
K_ONE: Pair = (Fraction(1), Fraction(0))


def k_add(x: Pair, y: Pair) -> Pair:
    return x[0] + y[0], x[1] + y[1]


def k_sub(x: Pair, y: Pair) -> Pair:
    return x[0] - y[0], x[1] - y[1]


def k_mul(x: Pair, y: Pair) -> Pair:
    a, b = x
    c, d = y
    return a * c - b * d, a * d + b * c - b * d


def k_inv(x: Pair) -> Pair:
    a, b = x
    norm = a * a - a * b + b * b
    if norm == 0:
        raise ZeroDivisionError
    return (a - b) / norm, -b / norm


def k_div(x: Pair, y: Pair) -> Pair:
    return k_mul(x, k_inv(y))


def k_int(value: int) -> Pair:
    return Fraction(value), Fraction(0)


def k_rho(exponent: int) -> Pair:
    return (K_ONE, (Fraction(0), Fraction(1)), (Fraction(-1), Fraction(-1)))[
        exponent % 3
    ]


def permutation_sign(permutation: tuple[int, ...]) -> int:
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(len(permutation))
        for j in range(i + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def compositions(total: int, slots: int, prefix: tuple[int, ...] = ()):
    if slots == 1:
        yield prefix + (total,)
        return
    for value in range(total + 1):
        yield from compositions(total - value, slots - 1, prefix + (value,))


def cayley_monomials() -> list[tuple[int, int, tuple[int, ...]]]:
    rows = []
    for a in range(2):
        rows.extend((a, 1 - a, exponent) for exponent in compositions(a + 1, 6))
    assert len(rows) == 27
    return rows


def rref(rows: list[list[Pair]]) -> tuple[list[list[Pair]], list[int]]:
    matrix = [row[:] for row in rows]
    pivots: list[int] = []
    rank = 0
    for column in range(len(matrix[0])):
        pivot = next((row for row in range(rank, len(matrix)) if matrix[row][column] != K_ZERO), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inverse_pivot = k_inv(matrix[rank][column])
        matrix[rank] = [k_mul(value, inverse_pivot) for value in matrix[rank]]
        for row in range(len(matrix)):
            if row == rank or matrix[row][column] == K_ZERO:
                continue
            scalar = matrix[row][column]
            matrix[row] = [
                k_sub(left, k_mul(scalar, right))
                for left, right in zip(matrix[row], matrix[rank])
            ]
        pivots.append(column)
        rank += 1
    return matrix[:rank], pivots


def cayley_relations(monomials) -> list[list[Pair]]:
    index = {monomial: position for position, monomial in enumerate(monomials)}
    edge_weights = {
        tuple(sorted((i, (i + 1) % 6))): k_rho(int(i == 5)) for i in range(6)
    }

    def vector(terms):
        result = [K_ZERO] * len(monomials)
        for coefficient, monomial in terms:
            position = index[monomial]
            result[position] = k_add(result[position], coefficient)
        return result

    rows = []
    for i in range(6):
        exponent = [0] * 6
        exponent[i] = 2
        terms = [(k_int(3), (1, 0, tuple(exponent)))]
        for edge, coefficient in edge_weights.items():
            if i in edge:
                other = edge[0] if edge[1] == i else edge[1]
                exponent = [0] * 6
                exponent[other] = 1
                terms.append((coefficient, (0, 1, tuple(exponent))))
        rows.append(vector(terms))
    terms = []
    for edge, coefficient in edge_weights.items():
        exponent = [0] * 6
        exponent[edge[0]] += 1
        exponent[edge[1]] += 1
        terms.append((coefficient, (1, 0, tuple(exponent))))
    rows.append(vector(terms))
    return rows


def n3_exact_character() -> dict:
    q_by_element, _ = recurrence_group(3)
    group = q_by_element
    r, s = generators(3)
    elements = [power(r, k) for k in range(9)] + [compose(power(r, k), s) for k in range(9)]
    assert len(set(elements)) == 18 and set(elements) == set(group)
    monomials = cayley_monomials()
    monomial_index = {monomial: index for index, monomial in enumerate(monomials)}
    relations = cayley_relations(monomials)
    reduced_relations, pivots = rref(relations)
    assert len(relations) == len(pivots) == 7
    pivot_row = {pivot: row for row, pivot in enumerate(pivots)}
    basis = [index for index in range(27) if index not in pivot_row]
    assert len(basis) == 20

    def descriptor_raw(
        permutation: tuple[int, ...], phases: tuple[int, ...], q: int, monomial
    ) -> tuple[int, Pair]:
        determinant = k_mul(k_int(permutation_sign(permutation)), k_rho(sum(phases)))
        residue_factor = k_div(determinant, k_rho(q))
        a, b, exponent = monomial
        target_exponent = [0] * 6
        phase = -q * b
        for i, multiplicity in enumerate(exponent):
            target_exponent[permutation[i]] += multiplicity
            phase += phases[i] * multiplicity
        target = monomial_index[(a, b, tuple(target_exponent))]
        return target, k_mul(residue_factor, k_rho(phase))

    def descriptor(item: Map, monomial) -> tuple[int, Pair]:
        return descriptor_raw(item[0], item[1], q_by_element[item], monomial)

    def reduce_vector(vector: list[Pair]) -> list[Pair]:
        result = vector[:]
        for pivot in pivots:
            if result[pivot] != K_ZERO:
                scalar = result[pivot]
                result = [
                    k_sub(left, k_mul(scalar, right))
                    for left, right in zip(result, reduced_relations[pivot_row[pivot]])
                ]
        return result

    relation_image_tests = 0
    for item in elements:
        for relation in relations:
            image = [K_ZERO] * 27
            for index, coefficient in enumerate(relation):
                if coefficient != K_ZERO:
                    target, scalar = descriptor(item, monomials[index])
                    image[target] = k_add(image[target], k_mul(coefficient, scalar))
            assert all(value == K_ZERO for value in reduce_vector(image))
            relation_image_tests += 1

    group_law_tests = 0
    for left in elements:
        for right in elements:
            composed = compose(left, right)
            for monomial in monomials:
                middle, a = descriptor(left, monomial)
                target, b = descriptor(right, monomials[middle])
                expected_target, c = descriptor(composed, monomial)
                assert target == expected_target and k_mul(a, b) == c
                group_law_tests += 1

    scalar_lift_tests = 0
    for item in elements:
        q = q_by_element[item]
        for lift in (1, 2):
            phases = tuple((phase + lift) % 3 for phase in item[1])
            lifted_q = (q + 2 * lift) % 3
            for monomial in monomials:
                assert descriptor(item, monomial) == descriptor_raw(
                    item[0], phases, lifted_q, monomial
                )
                scalar_lift_tests += 1

    def trace(item: Map) -> int:
        value = K_ZERO
        for basis_index in basis:
            target, scalar = descriptor(item, monomials[basis_index])
            if target == basis_index:
                value = k_add(value, scalar)
            elif target in pivot_row:
                value = k_sub(
                    value,
                    k_mul(scalar, reduced_relations[pivot_row[target]][basis_index]),
                )
        assert value[1] == 0 and value[0].denominator == 1
        return int(value[0])

    h21_rotation = [trace(power(r, k)) for k in range(9)]
    h21_reflection = [trace(compose(power(r, k), s)) for k in range(9)]

    def fermat_trace(item: Map) -> int:
        permutation, phases = item
        determinant = k_mul(k_int(permutation_sign(permutation)), k_rho(sum(phases)))
        value = K_ONE  # extra trivial line
        for degree in (0, 3, 6):
            for subset in combinations(range(6), degree):
                if {permutation[i] for i in subset} == set(subset):
                    value = k_add(
                        value,
                        k_mul(determinant, k_rho(sum(phases[i] for i in subset))),
                    )
        assert value[1] == 0 and value[0].denominator == 1
        return int(value[0])

    e3_rotation = [fermat_trace(power(r, k)) for k in range(9)]
    e3_reflection = [fermat_trace(compose(power(r, k), s)) for k in range(9)]

    def zeta9_vector(exponent: int) -> list[int]:
        exponent %= 9
        vector = [0] * 6
        if exponent < 6:
            vector[exponent] = 1
        else:
            vector[exponent - 6] = -1
            vector[exponent - 3] = -1
        return vector

    def decompose(rotation: list[int], reflection: list[int]) -> dict[str, int]:
        answer = {
            "trivial": (sum(rotation) + sum(reflection)) // 18,
            "epsilon": (sum(rotation) - sum(reflection)) // 18,
        }
        for j in range(1, 5):
            numerator = [0] * 6
            for k in range(9):
                for character_term in (zeta9_vector(j * k), zeta9_vector(-j * k)):
                    numerator = [
                        old + rotation[k] * term
                        for old, term in zip(numerator, character_term)
                    ]
            assert numerator[1:] == [0] * 5 and numerator[0] % 18 == 0
            answer[f"U{j}"] = numerator[0] // 18
        return answer

    h21_decomposition = decompose(h21_rotation, h21_reflection)
    e3_decomposition = decompose(e3_rotation, e3_reflection)
    assert h21_decomposition == {
        "trivial": 0,
        "epsilon": 2,
        "U1": 2,
        "U2": 2,
        "U3": 3,
        "U4": 2,
    }
    assert e3_decomposition == {
        "trivial": 1,
        "epsilon": 2,
        "U1": 3,
        "U2": 3,
        "U3": 1,
        "U4": 3,
    }
    o3_decomposition = {
        key: 2 * multiplicity for key, multiplicity in h21_decomposition.items()
    }
    sector_pairs = [
        {
            "sector": sector,
            "E3_multiplicity": e3_decomposition[sector],
            "O3_multiplicity": o3_decomposition[sector],
            "both_divisible_by_3": (
                e3_decomposition[sector] % 3 == 0
                and o3_decomposition[sector] % 3 == 0
            ),
        }
        for sector in ("trivial", "epsilon", "U1", "U2", "U3", "U4")
    ]
    assert not any(row["both_divisible_by_3"] for row in sector_pairs)
    orders: dict[int, int] = {}
    for item in elements:
        order = map_order(item, 18)
        orders[order] = orders.get(order, 0) + 1
    assert orders == {1: 1, 9: 6, 3: 2, 2: 9}
    return {
        "group": "Dih(C9)",
        "group_order": 18,
        "element_order_counts": {str(key): orders[key] for key in sorted(orders)},
        "cayley_jacobian": {
            "bidegree": "R_(1,-1)",
            "ambient_monomials": 27,
            "jacobian_generators": 7,
            "jacobian_relation_rank": len(pivots),
            "quotient_dimension_H21": len(basis),
            "residue_action_factor": "det(M_g)/det(A_g)",
            "residue_factor_orientation": "NUMERATOR_VARIABLE_MATRIX_OVER_DENOMINATOR_EQUATION_MATRIX",
            "relation_image_tests": relation_image_tests,
            "group_law_monomial_tests": group_law_tests,
            "scalar_lift_exponents_tested": [1, 2],
            "scalar_lift_descriptor_tests": scalar_lift_tests,
            "projective_scalar_lift_invariant": True,
        },
        "H21_character": {
            "rotation_traces_k0_to_k8": h21_rotation,
            "reflection_traces_k0_to_k8": h21_reflection,
            "irreducible_multiplicities": h21_decomposition,
            "dimension": 20,
        },
        "O3_character": {
            "construction": "H21_plus_complex_conjugate_H12",
            "irreducible_multiplicities": o3_decomposition,
            "dimension": 40,
            "real_character_double": True,
        },
        "E3_character": {
            "includes_extra_trivial_line": True,
            "rotation_traces_k0_to_k8": e3_rotation,
            "reflection_traces_k0_to_k8": e3_reflection,
            "irreducible_multiplicities": e3_decomposition,
            "dimension": 23,
        },
        "central_sector_test": {
            "scaling": "4/3",
            "integrality_criterion": "each selected rail multiplicity divisible by 3",
            "sector_pairs": sector_pairs,
            "nonzero_common_integral_sector_exists": False,
            "Reynolds_invariant_ranks": {"E3": 1, "O3": 0},
        },
        "coefficient_field_orbit_blocks": [
            {
                "sectors": ["trivial"],
                "E3_multiplicity": 1,
                "O3_multiplicity": 0,
            },
            {"sectors": ["epsilon"], "E3_multiplicity": 2, "O3_multiplicity": 4},
            {
                "sectors": ["U1", "U2", "U4"],
                "E3_multiplicity": 3,
                "O3_multiplicity": 4,
            },
            {"sectors": ["U3"], "E3_multiplicity": 1, "O3_multiplicity": 6},
        ],
        "rational_form_caveat": {
            "common_character_theorem_field": "K=Q(rho)",
            "Fermat_standard_Q_form_equals_M3_twisted_form_claimed": False,
            "M3_twist_available_for_common_group_scheme_wording": True,
            "split_traces_unchanged_by_twist": True,
            "inert_traces_may_change": True,
        },
    }


def build_payload() -> dict:
    source_lock = strict_source_lock()
    group_controls = [group_control(n) for n in range(2, 65)]
    brute_controls = []
    for n in (2, 3, 4):
        recurrence, _ = recurrence_group(n)
        brute = brute_force_group(n)
        assert brute == recurrence
        brute_controls.append(
            {
                "n": n,
                "normalized_phase_assignments_scanned": (4 * n) * 3 ** (2 * n - 1),
                "stabilizers_found": len(brute),
                "matches_recurrence_list": True,
            }
        )
    rational_controls = [rational_form_control(n) for n in range(2, 257)]
    divisor_table = [divisor_row(n) for n in (2, 3, 4, 6, 8, 12, 24)]
    finite_scan = [
        n
        for n in range(2, 513)
        if (4 * packet_ranks(n)[0]) % n == 0 and (4 * packet_ranks(n)[1]) % n == 0
    ]
    assert finite_scan == [2, 4]
    n3 = n3_exact_character()
    return {
        "schema_version": "c54-v1",
        "claim_scope": {
            "candidate_id": "HCS-C54",
            "title": "Universal Dihedral Symmetry and Split-Denominator Rigidity in a Cubic--Quadric Source Tower",
            "all_n_equation_theorem": True,
            "all_n_equation_theorem_category": "full projective monomial stabilizer of the homogeneous ideal",
            "packet_admissibility_definition": "actual rational compatible realizations E_n,O_n pure of weights 0,1 with the frozen ranks; no semisimplicity hypothesis",
            "certified_packet_rows": [2, 3, 4],
            "conditional_packet_rows": "n>=5 only under explicit packet-admissibility hypothesis",
            "C53_semisimplicity_claimed": False,
            "proof_semisimplicity_passage": "fix one coefficient prime and apply semisimplification before Chebotarev--Brauer--Nesbitt",
            "ordinary_meaning": "actual finite-rank Q-compatible realization matching every good split-prime trace/factor as specified",
            "fixed_prime_input_used": False,
        },
        "source_family": {
            "base_field": "K=Q(rho)",
            "rho_relation": "rho^2+rho+1=0",
            "n_range": "every integer n>=2",
            "N": "2n",
            "C_n": "sum_(i=0)^(2n-1) x_i^3",
            "Q_n_rho": "sum_(i=0)^(2n-2) x_i*x_(i+1)+rho*x_(2n-1)*x_0",
            "closing_edge_coefficient": "rho",
            "stabilizer_definition": "PGL_(2n)(K) monomial classes stabilizing the homogeneous ideal (C_n,Q_n_rho)",
            "full_PGL_automorphism_group_claimed": False,
            "C53_source_lock": source_lock,
        },
        "full_projective_monomial_group": {
            "theorem_range": "every integer n>=2",
            "isomorphism": "PMonStab(C_n,Q_n_rho)=Dih(C_(3n))",
            "order": "6n",
            "presentation": "<r,s | r^(3n)=s^2=1, s*r*s=r^(-1)>",
            "support_exact_sequence": "1 -> C3 -> G_n -> Dih(C_n) -> 1",
            "support_image": "even rotations and odd reflections of the 2n-cycle",
            "phase_normalization": "e_i in F3 and e_0=0",
            "phase_and_scale_derivation": {
                "projective_scalar_normalization": "lambda_0=1",
                "cubic_line_coefficient_step": "lambda_i^3=1 for every i",
                "coordinate_phases_in_mu3": True,
                "quadric_edge_ratio_step": "the quadric scale is lambda_i*lambda_j times a ratio of source/target edge coefficients, all in mu3",
                "quadric_scale_in_mu3": True,
                "q_definition": "quadric scale=rho^q with q in F3",
            },
            "ideal_to_equation_lines": {
                "degree_two_ideal_piece": "K*Q_n_rho",
                "degree_three_form": "g^*C_n=a*C_n+L*Q_n_rho",
                "pure_cube_comparison": "L*Q has no pure cubes, so g^*C_n=a*C_n and L*Q=0",
                "domain_step": "polynomial ring is a domain and Q is nonzero, hence L=0",
                "both_equation_lines_preserved": True,
            },
            "edge_recurrence": "e_(j+1)=q+c_(sigma(E_j))-c_j-e_j mod 3",
            "closing_edge_indicator": "c_(2n-1)=1 and all other c_j=0",
            "closure_condition": "inverse image of the closing edge has odd edge index",
            "rotation_support_condition": "sigma(i)=i+k survives iff k is even",
            "reflection_support_condition": "sigma(i)=k-i survives iff k is odd",
            "surviving_support_counts": {"rotations": "n", "reflections": "n"},
            "normalized_lifts_per_support": 3,
            "generators": {
                "r_support": "i -> i+2 mod 2n",
                "r_phases": "a_(2n-2)=1,a_(2n-1)=2,otherwise 0",
                "r_quadric_scale": "1",
                "r_power_n": "diag(1,rho,1,rho,...,1,rho) projectively",
                "r_exact_order": "3n",
                "s_support": "i -> 1-i mod 2n",
                "s_phases": "b_i=1 iff i=1 or i>=2 is even",
                "s_quadric_scale": "rho",
                "s_exact_order": 2,
                "srs": "r^(-1)",
            },
            "symbolic_fullness_proof": "recurrence exhausts exactly 6n stabilizers; r has order 3n and s has reflection support outside <r>, so <r,s> has 6n distinct two-coset elements and equals the exhaustive list",
            "finite_exact_controls_n2_to_n64": group_controls,
            "finite_controls_sha256": sha256_bytes(canonical_json(group_controls).encode()),
            "independent_bruteforce_controls": brute_controls,
            "finite_controls_role": "mutation guards, not the universal proof",
            "nonmonomial_automorphisms_classified": False,
        },
        "rational_group_form": {
            "tau": "tau(rho)=rho^2",
            "descent_reversal": "M_n: sigma(i)=-i; e_0=0 and e_i=1 exactly for nonzero even i",
            "transport_definition": "delta(g)=M_n*tau(g)*M_n^(-1)",
            "delta_r": "r^(-1)",
            "delta_s": "r*s=s*r^(-1)",
            "delta_square": "identity",
            "group_scheme": "finite etale nonconstant Q-form mathscrG_n split by K",
            "geometric_rank": "6n",
            "Q_rational_points_group": "C2",
            "Q_rational_point_count": 2,
            "fixed_congruences": {"rotations": "2k=0 mod 3n", "reflections": "2k=1 mod 3n"},
            "fixed_elements_even_n": ["1", "r^(3n/2)"],
            "fixed_elements_odd_n": ["1", "r^((3n+1)/2)*s"],
            "all_geometric_elements_individually_Q_rational_claimed": False,
            "finite_exact_control_range": [2, 256],
            "finite_exact_controls_sha256": sha256_bytes(canonical_json(rational_controls).encode()),
            "every_control_has_two_fixed_points": all(row["fixed_count"] == 2 for row in rational_controls),
            "Reynolds": {
                "smooth_packet_row_scope": True,
                "geometric_average": "(1/(6n))*sum_(g in G_n) Gamma_g",
                "graphs_used": "all 6n geometric graphs",
                "denominator": "6n",
            },
            "quadratic_transfer": {
                "formula": "e_mathscrG=(1/2)q_*e_G and q^*e_mathscrG=e_G",
                "denominator": 2,
                "distinct_from_Reynolds_denominator": True,
            },
            "all_n_Chow_projector_claimed": False,
        },
        "split_denominator_rigidity": {
            "theorem_scope": "every packet-admissible n>=2",
            "packet_weights": {"E_n": 0, "O_n": 1},
            "packet_ranks": {
                "e_n": "(4^n+5)/3",
                "o_n": "2*(4^n-4)/3",
                "relation": "o_n=2*(e_n-3)",
            },
            "split_exponent_after_Q_descent": "4/n",
            "ordinary_split_trace_identity": "Tr(F_p|V_n)=(4/n)*Tr(F_p|E_n direct_sum O_n) at every good split p",
            "ordinary_split_factor_identity": "Log_0 L_p(V_n,u)=(4/n)*Log_0 L_p(E_n direct_sum O_n,u)",
            "restriction_argument": {
                "degree_one_K_primes": "density one after excluding finitely many places",
                "fixed_coefficient_prime": True,
                "semisimplification_passage": "replace each fixed-ell realization by its semisimplification; traces and ranks are unchanged",
                "semisimple_theorem": "Chebotarev plus Brauer--Nesbitt applied only after semisimplification",
                "K0_identity": "n*[(Res V_n,ell)^ss]=4*[(Res E_n,ell)^ss]+4*[(Res O_n,ell)^ss]",
                "pure_weight_separation": True,
                "source_semisimplicity_assumed": False,
                "necessary_divisibilities": ["n divides 4e_n", "n divides 4o_n"],
                "reduction": "o_n=2(e_n-3) implies n divides 24",
            },
            "divisors_of_24_table": divisor_table,
            "surviving_rows": [2, 4],
            "classification": "ordinary split-trace realization iff n divides 4",
            "strong_factor_classification_same": True,
            "converse": "V_n=E_n^(direct sum 4/n) direct_sum O_n^(direct sum 4/n)",
            "converse_matches_every_power_trace": True,
            "finite_scan_range": [2, 512],
            "finite_scan_survivors": finite_scan,
            "total_rank_trap_n3": {
                "e_3": 23,
                "o_3": 40,
                "total_rank": 63,
                "scaled_total_rank": 84,
                "scaled_E3_rank": "92/3",
                "scaled_O3_rank": "160/3",
                "total_rank_only_would_falsely_accept": True,
                "proof_route_accepted": False,
            },
            "both_pure_rails_essential": True,
            "certified_unconditional_rows": [2, 3, 4],
            "n_ge_5_packet_status": "CONDITIONAL_NOT_CONSTRUCTED",
            "inert_identity": "P_K,v(U^2)=P_Q,p(U)*P_Q,p(-U)",
            "inert_factor_generally_square_claimed": False,
            "global_fractional_root_claimed": False,
        },
        "n3_equivariant_character": n3,
        "counterpacket_firewall": {
            "restriction_map": "Res:K0_ss(G_Q)->K0_ss(G_K)",
            "K0_ss_category": "classes of fixed-ell finite-dimensional continuous semisimple ell-adic representations arising from the compatible systems in scope, unramified outside one common finite set; not arbitrary G_Q representations",
            "Q_split_primes_absolute_density": "1/2",
            "trace_zero_hypothesis_density": "relative density one within the good split rational primes",
            "lifted_K_degree_one_prime_density": "density one among primes of K after finitely many exclusions",
            "trace_zero_conclusion": "Res(D)=0",
            "actual_invisible_counterpacket": "only zero",
            "virtual_restriction_injective_claimed": False,
            "virtual_kernel_example": "1-chi_(K/Q)",
            "example_nonzero_virtual_class": True,
            "example_split_invisible": True,
            "example_restriction_zero": True,
            "every_kernel_class_rank": 0,
            "kernel_can_change_K_rail_rank": False,
            "kernel_can_change_K_source_isotypic_multiplicity": False,
            "rational_extension_unique_from_split_traces_claimed": False,
            "quadratic_twist_may_change_inert_traces": True,
            "different_split_trace_or_prime_organization_is_different_Euler_object": True,
        },
        "primary_source_controls": {
            "reproducible_certificate_evidence": {
                "producer": "code/c54_producer.py",
                "checker": "code/c54_checker.py",
                "formal_proof": "THEOREM_PACKAGE.md and PROOF_PACKAGE.md",
                "bibliographic_locators": "SOURCE_AUDIT.md",
            },
            "primary_locators_duplicated_in_certificate": False,
            "pre_c54_reconnaissance": {
                "status": "UNPACKAGED_NOT_REPLAYED_NOT_THEOREM_INPUT",
                "chronology_note_only": True,
                "counts_as_source_or_semantic_proof_gate": False,
                "historical_sha256": {
                    "theorem_planning_note": "f0a00d9862309272b3de30fa37a95c516b551875236ee18628fb180981fad5ed",
                    "architecture_planning_note": "3a77c384993d3bf7e11d529638c56771874ebadc14f38d052812d423b21a21eb",
                    "general_group_exploration": "3419e68fe4282b575fcc086772be8c32877fce8292ba7c7cabf4bbdf9437632c",
                    "n3_exploration": "1798f348c7df79f35b69fb0234bac025af3f0f1a60b6ae53d5963a196f897559",
                },
            },
            "Brunjes_scope": "Fermat monomial group/character sectors only; not the simultaneous cubic-quadric theorem",
            "Serre_scope": "Chebotarev density input",
            "Brauer_Nesbitt_scope": "semisimple character equality input",
            "Favero_Iliev_Katzarkov_scope": "Cayley-Jacobian model background",
            "novelty_search_exhaustive_claimed": False,
        },
        "exclusions": {
            "full_PGL_automorphism_group": False,
            "smoothness_all_n": False,
            "compatible_packets_all_n": False,
            "Chow_motive_all_n": False,
            "all_6n_individual_Q_automorphisms": False,
            "rotations_only_Reynolds_average": False,
            "global_fractional_Euler_root": False,
            "inert_fractional_Euler_root": False,
            "unique_Q_extension_from_split_traces": False,
            "automorphy": False,
            "meromorphic_continuation": False,
            "functional_equation": False,
            "Riemann_hypothesis": False,
            "fixed_Frobenius_prime_theorem_input": False,
        },
        "artifact_status": "RELEASE_CANDIDATE",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    arguments = parser.parse_args()
    output = arguments.output
    if output.exists():
        if not output.is_file():
            print(f"PRODUCER FAILED: output exists and is not a file: {output}", file=sys.stderr)
            return 1
        output.unlink()
    if not __debug__:
        print("PRODUCER FAILED: optimized Python disables certificate assertions", file=sys.stderr)
        return 1
    temporary = output.with_name(f".{output.name}.{os.getpid()}.new")
    try:
        payload = build_payload()
        certificate = {
            "schema": "hcs-c54-certificate-v1",
            "payload": payload,
            "payload_sha256": sha256_bytes(canonical_json(payload).encode()),
        }
        encoded = json.dumps(certificate, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
        output.parent.mkdir(parents=True, exist_ok=True)
        temporary.write_text(encoded, encoding="utf-8")
        temporary.replace(output)
    except Exception as error:
        if temporary.is_file():
            temporary.unlink()
        print(f"PRODUCER FAILED: {type(error).__name__}: {error}", file=sys.stderr)
        return 1
    print(
        f"wrote {output} payload_sha256={certificate['payload_sha256']} "
        f"certificate_sha256={sha256_bytes(encoded.encode())}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
