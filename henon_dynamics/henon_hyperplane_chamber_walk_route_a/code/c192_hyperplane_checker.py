#!/usr/bin/env python3
"""Independent exact checker for the C192 evidence artifact.

This file deliberately imports no producer code.  It reconstructs the face
product, support lattice, Möbius values, matrices, samplers, and bounds from the
serialized sign vectors using algorithms different from the producer's loops.
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
import json
import sys
from pathlib import Path


Q = Fraction
ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c192_hyperplane_evidence.json"
SOURCE_COMMIT = "4d7b214759f7ff982c0b19e662918acd307e0f58"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
COUNT = 0


def ck(condition: bool, message: str) -> None:
    global COUNT
    COUNT += 1
    if not condition:
        raise AssertionError(message)


def q(value: str | int) -> Q:
    return Q(value)


def compose(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(r if l == 0 else l for l, r in zip(left, right))


def zeros(face: tuple[int, ...]) -> frozenset[int]:
    return frozenset(index for index, sign in enumerate(face) if sign == 0)


def mm(a: list[list[Q]], b: list[list[Q]]) -> list[list[Q]]:
    rows = len(a)
    inner = len(b)
    cols = len(b[0])
    answer = [[Q(0) for _ in range(cols)] for _ in range(rows)]
    for k in range(inner):
        for i in range(rows):
            if a[i][k]:
                for j in range(cols):
                    answer[i][j] += a[i][k] * b[k][j]
    return answer


def eye(n: int) -> list[list[Q]]:
    answer = [[Q(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        answer[i][i] = Q(1)
    return answer


def pmul(a: list[Q], b: list[Q]) -> list[Q]:
    answer = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            answer[i + j] += x * y
    return answer


def expected_metadata() -> dict:
    return {
        "schema": "hcs-c192-evidence-v1",
        "candidate_id": "HCS-C192",
        "evaluation_date": "2026-08-27",
        "source_commit": SOURCE_COMMIT,
        "evaluator": {"version": "0.2.0", "path": "flow_systems/skills/route-a-evaluator.md", "sha256": EVALUATOR_SHA256},
        "scope_literal": SCOPE,
    }


def expected_source_lock() -> dict:
    return {
        "primary": {
            "authors": "Kenneth S. Brown and Persi Diaconis",
            "title": "Random Walk and Hyperplane Arrangements",
            "journal": "The Annals of Probability 26(4), 1813--1854 (1998)",
            "doi": "10.1214/aop/1022855884",
            "theorem_locators": ["Theorem 1", "Theorem 2", "Theorem 3", "Section 4B", "Section 6"],
        },
        "oriented_matroid_ceiling": "Theorems 1 and 2 carry over to the covector face semigroup of an oriented matroid as stated in Section 6; no stronger affine or realization claim is imported.",
        "strict_sst_boundary": "The stopping sampler and coupling bound are source-supported; independence of the stopped chamber from the stopping time is not asserted and strict-SST terminology is rejected.",
    }


def expected_theorem_lock() -> dict:
    return {
        "domain": "Every finite real hyperplane arrangement with an arbitrary probability measure on its face semigroup.",
        "spectrum": "K is diagonalizable with flat-indexed eigenvalues lambda_W=sum_{F subset W} w(F) and multiplicities |mu(W,V)|.",
        "operator_corollaries": "The flat factorization gives the characteristic polynomial, det(I-zK), and every power trace exactly.",
        "stationarity": "The face measure is separating exactly when the chamber chain has a unique stationary distribution.",
        "sampler": "Under separation, weighted sampling without replacement gives an exact stationary chamber; the with-replacement chamber-hitting construction is a stationary stopping sampler and coupling, not a claimed strict strong stationary time.",
        "mixing": "For every start, total variation is bounded by the exact nonchamber probability -sum_{W != V} mu(W,V)lambda_W^ell and hence by sum_{H in A} lambda_H^ell.",
        "nonseparating": "If A0 is the set of hyperplanes containing the support of w, A0-chambers are closed components, each has one stationary law, and all stationary laws form the simplex on those components.",
    }


def expected_attribution() -> dict:
    return {
        "status": "CLASSICAL_THEOREM_SOURCE_LOCKED_FINITE_REGRESSION_ONLY",
        "all_family_proof_owner": "Brown--Diaconis (1998), Theorems 1--3 and Sections 4, 6",
        "code_role": "finite exact regression oracle only",
        "novelty_claimed": False,
        "external_review_claimed": False,
    }


def expected_route() -> dict:
    return {
        "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
        "qualifications": {
            "A0": "No intrinsic rational-prime or target-zero indexing is present.",
            "A1": "The chamber spectrum does not recover target arithmetic data.",
            "A2": "No target functional equation or continuation is produced.",
            "A3": "Finite-state mixing bounds are not target counting laws.",
            "A4": "The exact finite operator determinant is only a formal operator hint, with no target divisor identification.",
        },
        "overall": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
    }


def weighted_order_dp(weight_items: list[tuple[tuple[int, ...], Q]]) -> dict[tuple[int, ...], Q]:
    size = len(weight_items)
    dimension = len(weight_items[0][0])
    states: dict[tuple[int, tuple[int, ...]], Q] = {(0, (0,) * dimension): Q(1)}
    for _ in range(size):
        new: defaultdict[tuple[int, tuple[int, ...]], Q] = defaultdict(Q)
        for (mask, aggregate), probability in states.items():
            remaining = sum((weight_items[i][1] for i in range(size) if not (mask >> i) & 1), Q(0))
            for i, (face, weight) in enumerate(weight_items):
                if not (mask >> i) & 1:
                    new[(mask | (1 << i), compose(aggregate, face))] += probability * weight / remaining
        states = dict(new)
    answer: defaultdict[tuple[int, ...], Q] = defaultdict(Q)
    for (_, aggregate), probability in states.items():
        answer[aggregate] += probability
    return dict(answer)


def failure_dp(weight_items: list[tuple[tuple[int, ...], Q]], length: int) -> Q:
    dimension = len(weight_items[0][0])
    distribution: dict[tuple[int, ...], Q] = {(0,) * dimension: Q(1)}
    for _ in range(length):
        nxt: defaultdict[tuple[int, ...], Q] = defaultdict(Q)
        for aggregate, probability in distribution.items():
            for face, weight in weight_items:
                nxt[compose(aggregate, face)] += probability * weight
        distribution = dict(nxt)
    return sum((probability for aggregate, probability in distribution.items() if 0 in aggregate), Q(0))


def check_case(case: dict) -> dict:
    required = {
        "name", "family", "parameter", "tags", "hyperplanes", "faces", "chambers", "positive_weights",
        "separating", "nonseparating_hyperplane_indices", "component_keys", "stationary_simplex_vertex_count",
        "flats", "transition_matrix", "charpoly_ascending", "det_I_minus_zK_ascending", "power_traces",
        "without_replacement_stationary", "mixing",
    }
    ck(set(case) == required, f"case keys: {case.get('name')}")
    profiles = {
        "coordinate_B2_separating": ("coordinate", 2, ["separating", "coordinate"]),
        "coordinate_B3_separating": ("coordinate", 3, ["separating", "coordinate"]),
        "coordinate_B4_separating": ("coordinate", 4, ["separating", "coordinate"]),
        "coordinate_B2_full_support": ("coordinate", 2, ["separating", "full-face-support"]),
        "coordinate_B3_nonseparating_H1": ("coordinate", 3, ["nonseparating", "component-simplex"]),
        "braid_A2_tsetlin": ("braid", 3, ["separating", "tsetlin-regression"]),
        "braid_A3_tsetlin": ("braid", 4, ["separating", "tsetlin-regression"]),
        "braid_A3_nonseparating_H12": ("braid", 4, ["nonseparating", "tsetlin-boundary", "component-simplex"]),
    }
    ck(case["name"] in profiles, "case name")
    ck((case["family"], case["parameter"], case["tags"]) == profiles[case["name"]], "case profile")
    if case["family"] == "coordinate":
        expected_hyperplanes = [f"x{i + 1}=0" for i in range(case["parameter"])]
    else:
        expected_hyperplanes = [
            f"x{i + 1}=x{j + 1}"
            for i in range(case["parameter"])
            for j in range(i + 1, case["parameter"])
        ]
    ck(case["hyperplanes"] == expected_hyperplanes, "hyperplane labels")
    dimension = len(case["hyperplanes"])
    faces = [tuple(row) for row in case["faces"]]
    chambers = [tuple(row) for row in case["chambers"]]
    face_set = set(faces)
    chamber_set = set(chambers)
    ck(len(faces) == len(face_set), "duplicate faces")
    ck(len(chambers) == len(chamber_set), "duplicate chambers")
    for face in faces:
        ck(len(face) == dimension and set(face) <= {-1, 0, 1}, "invalid covector")
    for chamber in chambers:
        ck(chamber in face_set and 0 not in chamber, "invalid chamber")
    ck(chamber_set == {face for face in faces if 0 not in face}, "chamber census")
    for left in faces:
        for right in faces:
            ck(compose(left, right) in face_set, "face semigroup not closed")

    weight_items = [(tuple(row["face"]), q(row["weight"])) for row in case["positive_weights"]]
    weights = dict(weight_items)
    ck(len(weights) == len(weight_items), "duplicate positive-weight face")
    ck(set(weights) <= face_set and all(value > 0 for value in weights.values()), "weight support")
    ck(sum(weights.values(), Q(0)) == 1, "weights normalize")

    separating = all(any(face[h] != 0 for face in weights) for h in range(dimension))
    a0 = [h for h in range(dimension) if all(face[h] == 0 for face in weights)]
    keys = sorted({tuple(chamber[h] for h in a0) for chamber in chambers})
    ck(case["separating"] is separating, "separation flag")
    ck(case["nonseparating_hyperplane_indices"] == a0, "A0 hyperplanes")
    ck(case["component_keys"] == [list(key) for key in keys], "component keys")
    ck(case["stationary_simplex_vertex_count"] == len(keys), "stationary simplex vertices")

    flat_sets = sorted({zeros(face) for face in faces}, key=lambda z: (len(z), tuple(sorted(z))))
    mu: dict[frozenset[int], int] = {frozenset(): 1}
    rank: dict[frozenset[int], int] = {frozenset(): 0}
    for flat in flat_sets[1:]:
        mu[flat] = -sum(value for lower, value in mu.items() if lower < flat)
        rank[flat] = 1 + max(value for lower, value in rank.items() if lower < flat)
    expected_flats = []
    for flat in flat_sets:
        eigenvalue = sum((value for face, value in weights.items() if flat <= zeros(face)), Q(0))
        expected_flats.append((sorted(flat), rank[flat], mu[flat], abs(mu[flat]), eigenvalue))
    ck(len(case["flats"]) == len(expected_flats), "flat count")
    for observed, expected in zip(case["flats"], expected_flats):
        ck(set(observed) == {"zero_hyperplane_indices", "codimension", "mobius_to_ambient", "multiplicity", "lambda"}, "flat keys")
        ck((observed["zero_hyperplane_indices"], observed["codimension"], observed["mobius_to_ambient"], observed["multiplicity"], q(observed["lambda"])) == expected, "flat data")
    ck(sum(abs(value) for value in mu.values()) == len(chambers), "Zaslavsky chamber sum")

    chamber_index = {chamber: i for i, chamber in enumerate(chambers)}
    matrix = [[Q(0) for _ in chambers] for _ in chambers]
    for source, chamber in enumerate(chambers):
        for face, weight in weight_items:
            matrix[source][chamber_index[compose(face, chamber)]] += weight
    observed_matrix = [[q(value) for value in row] for row in case["transition_matrix"]]
    ck(observed_matrix == matrix, "transition matrix")
    for row in matrix:
        ck(sum(row, Q(0)) == 1, "row stochastic")

    charpoly = [Q(1)]
    determinant = [Q(1)]
    for _, _, _, multiplicity, eigenvalue in expected_flats:
        for _ in range(multiplicity):
            charpoly = pmul(charpoly, [-eigenvalue, Q(1)])
            determinant = pmul(determinant, [Q(1), -eigenvalue])
    ck([q(value) for value in case["charpoly_ascending"]] == charpoly, "characteristic polynomial")
    ck([q(value) for value in case["det_I_minus_zK_ascending"]] == determinant, "operator determinant")

    powers = [eye(len(chambers))]
    for _ in range(5):
        powers.append(mm(powers[-1], matrix))
    ck(len(case["power_traces"]) == 6, "trace row count")
    for exponent, row in enumerate(case["power_traces"]):
        direct = sum((powers[exponent][i][i] for i in range(len(chambers))), Q(0))
        spectral = sum((Q(multiplicity) * eigenvalue ** exponent for _, _, _, multiplicity, eigenvalue in expected_flats), Q(0))
        ck(row == {"power": exponent, "direct": str(direct), "spectral": str(spectral)}, "power trace")

    if separating:
        sampler = weighted_order_dp(weight_items)
        observed_sampler = {tuple(row["chamber"]): q(row["probability"]) for row in case["without_replacement_stationary"]}
        sampler = {key: value for key, value in sampler.items() if value}
        ck(observed_sampler == sampler, "without-replacement sampler")
        stationary = [sampler.get(chamber, Q(0)) for chamber in chambers]
        ck(sum(stationary, Q(0)) == 1, "stationary sum")
        for target in range(len(chambers)):
            ck(sum((stationary[source] * matrix[source][target] for source in range(len(chambers))), Q(0)) == stationary[target], "stationary equation")
        ck(len(case["mixing"]) == 4, "mixing row count")
        for exponent, row in enumerate(case["mixing"], start=1):
            failure = failure_dp(weight_items, exponent)
            mobius_failure = -sum((Q(mu[flat]) * eigenvalue ** exponent for flat, (_, _, _, _, eigenvalue) in zip(flat_sets, expected_flats) if flat), Q(0))
            hyperplane_bound = sum((eigenvalue ** exponent for flat, (_, _, _, _, eigenvalue) in zip(flat_sets, expected_flats) if len(flat) == 1), Q(0))
            worst = Q(0)
            for state_row in powers[exponent]:
                worst = max(worst, sum((abs(x - y) for x, y in zip(state_row, stationary)), Q(0)) / 2)
            ck(row == {"power": exponent, "worst_total_variation": str(worst), "exact_failure_probability": str(failure), "mobius_failure_probability": str(mobius_failure), "hyperplane_union_bound": str(hyperplane_bound)}, "mixing ledger")
            ck(worst <= failure <= hyperplane_bound and failure == mobius_failure, "mixing inequalities")
    else:
        ck(case["without_replacement_stationary"] == [], "nonseparating sampler must be empty")
        ck(case["mixing"] == [], "nonseparating mixing rows must be empty")

    return {
        "faces": len(faces), "chambers": len(chambers), "flats": len(flat_sets),
        "cells": len(chambers) ** 2, "sampler": len(case["without_replacement_stationary"]),
        "mixing": len(case["mixing"]), "traces": len(case["power_traces"]), "separating": separating,
    }


def validate(path: Path) -> dict:
    global COUNT
    COUNT = 0
    document = json.loads(path.read_text())
    ck(set(document) == {
        "schema", "candidate_id", "evaluation_date", "source_commit", "evaluator", "scope_literal",
        "source_lock", "theorem_lock", "attribution", "finite_regression", "cases", "route_a",
        "forbidden_claims", "payload_sha256",
    }, "top-level keys")
    for key, value in expected_metadata().items():
        ck(document[key] == value, f"metadata {key}")
    ck(document["source_lock"] == expected_source_lock(), "source lock exact map")
    ck(document["theorem_lock"] == expected_theorem_lock(), "theorem lock exact map")
    ck(document["attribution"] == expected_attribution(), "attribution exact map")
    ck(document["route_a"] == expected_route(), "Route-A exact map")
    ck(document["forbidden_claims"] == {
        "bad_euler_or_root_number": False, "local_or_euler_factors": False, "root_numbers": False,
        "automorphy": False, "hilbert_polya_operator": False, "target_divisor_identified": False,
        "strict_strong_stationary_time": False, "global_novelty": False,
    }, "forbidden claims exact map")
    payload = dict(document)
    recorded = payload.pop("payload_sha256")
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ck(recorded == sha256(canonical).hexdigest(), "payload hash")

    summaries = [check_case(case) for case in document["cases"]]
    ck([case["name"] for case in document["cases"]] == [
        "coordinate_B2_separating", "coordinate_B3_separating", "coordinate_B4_separating",
        "coordinate_B2_full_support", "coordinate_B3_nonseparating_H1", "braid_A2_tsetlin",
        "braid_A3_tsetlin", "braid_A3_nonseparating_H12",
    ], "case order and coverage")
    aggregate = {
        "case_count": len(summaries),
        "separating_case_count": sum(row["separating"] for row in summaries),
        "nonseparating_case_count": sum(not row["separating"] for row in summaries),
        "face_count": sum(row["faces"] for row in summaries),
        "chamber_count": sum(row["chambers"] for row in summaries),
        "flat_count": sum(row["flats"] for row in summaries),
        "transition_cell_count": sum(row["cells"] for row in summaries),
        "stationary_probability_count": sum(row["sampler"] for row in summaries),
        "mixing_row_count": sum(row["mixing"] for row in summaries),
        "trace_row_count": sum(row["traces"] for row in summaries),
    }
    ck(document["finite_regression"] == aggregate, "aggregate exact map")
    return {"status": "C192_CHECKER_PASS", "assertions": COUNT, **aggregate}


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    print(json.dumps(validate(path), sort_keys=True))


if __name__ == "__main__":
    main()
