#!/usr/bin/env python3
"""Produce the exact C192 finite-regression ledger for chamber walks.

The all-arrangement theorem is source-attributed.  This program only supplies
finite, exactly rational regression oracles for coordinate and braid
arrangements; it is not the proof of the general theorem.
"""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
from itertools import permutations, product
import json
import os
from pathlib import Path


Q = Fraction
Sign = tuple[int, ...]
ROOT = Path(__file__).resolve().parents[1]
OUTPUT = Path(os.environ.get("C192_OUTPUT", ROOT / "results/c192_hyperplane_evidence.json"))
SOURCE_COMMIT = "4d7b214759f7ff982c0b19e662918acd307e0f58"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"


def enc(q: Q) -> str:
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def enc_vec(v: list[Q] | tuple[Q, ...]) -> list[str]:
    return [enc(x) for x in v]


def enc_matrix(a: list[list[Q]]) -> list[list[str]]:
    return [enc_vec(row) for row in a]


def face_product(x: Sign, y: Sign) -> Sign:
    return tuple(a if a else b for a, b in zip(x, y))


def zero_set(x: Sign) -> frozenset[int]:
    return frozenset(i for i, value in enumerate(x) if value == 0)


def matmul(a: list[list[Q]], b: list[list[Q]]) -> list[list[Q]]:
    return [
        [sum((a[i][k] * b[k][j] for k in range(len(b))), Q(0)) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def identity(n: int) -> list[list[Q]]:
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def poly_mul(a: list[Q], b: list[Q]) -> list[Q]:
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def poly_power_linear(constant: Q, linear: Q, exponent: int) -> list[Q]:
    out = [Q(1)]
    for _ in range(exponent):
        out = poly_mul(out, [constant, linear])
    return out


def ordered_partitions(items: tuple[int, ...]):
    """Generate ordered set partitions, canonically and without duplicates."""
    if not items:
        yield tuple()
        return
    first = items[0]
    for tail in ordered_partitions(items[1:]):
        for position in range(len(tail) + 1):
            yield tail[:position] + ((first,),) + tail[position:]
        for position in range(len(tail)):
            block = tuple(sorted(tail[position] + (first,)))
            yield tail[:position] + (block,) + tail[position + 1:]


def coordinate_data(d: int) -> tuple[list[str], list[Sign], list[Sign]]:
    names = [f"x{i + 1}=0" for i in range(d)]
    faces = [tuple(v) for v in product((-1, 0, 1), repeat=d)]
    chambers = [x for x in faces if 0 not in x]
    return names, faces, chambers


def braid_sign(blocks: tuple[tuple[int, ...], ...], pairs: list[tuple[int, int]]) -> Sign:
    pos = {value: block_index for block_index, block in enumerate(blocks) for value in block}
    return tuple(0 if pos[i] == pos[j] else (1 if pos[i] < pos[j] else -1) for i, j in pairs)


def braid_data(n: int) -> tuple[list[str], list[Sign], list[Sign], dict[int, Sign]]:
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    names = [f"x{i + 1}=x{j + 1}" for i, j in pairs]
    blocks = sorted(set(ordered_partitions(tuple(range(n)))), key=lambda x: (len(x), x))
    faces = sorted({braid_sign(p, pairs) for p in blocks})
    chambers = sorted(x for x in faces if 0 not in x)
    tsetlin = {}
    for i in range(n):
        partition = ((i,), tuple(j for j in range(n) if j != i))
        tsetlin[i] = braid_sign(partition, pairs)
    return names, faces, chambers, tsetlin


def normalize_weight_rows(rows: list[tuple[Sign, int]]) -> list[tuple[Sign, Q]]:
    total = sum(value for _, value in rows)
    return [(face, Q(value, total)) for face, value in rows]


def catalog() -> list[dict]:
    cases: list[dict] = []

    def add_coordinate(name: str, d: int, support_rows: list[tuple[Sign, int]], tags: list[str]):
        hyperplanes, faces, chambers = coordinate_data(d)
        cases.append({
            "name": name, "family": "coordinate", "parameter": d,
            "hyperplanes": hyperplanes, "faces": faces, "chambers": chambers,
            "weights": normalize_weight_rows(support_rows), "tags": tags,
        })

    for d in (2, 3, 4):
        rows = []
        for i in range(d):
            for sign in (-1, 1):
                face = tuple(sign if j == i else 0 for j in range(d))
                rows.append((face, 2 * i + (1 if sign == -1 else 2)))
        add_coordinate(f"coordinate_B{d}_separating", d, rows, ["separating", "coordinate"])

    _, full_faces, _ = coordinate_data(2)
    add_coordinate(
        "coordinate_B2_full_support", 2,
        [(face, index + 1) for index, face in enumerate(full_faces)],
        ["separating", "full-face-support"],
    )
    add_coordinate(
        "coordinate_B3_nonseparating_H1", 3,
        [((0, -1, 0), 1), ((0, 1, 0), 2), ((0, 0, -1), 3), ((0, 0, 1), 4)],
        ["nonseparating", "component-simplex"],
    )

    for n, raw in ((3, [3, 2, 1]), (4, [4, 3, 2, 1])):
        hyperplanes, faces, chambers, tsetlin = braid_data(n)
        cases.append({
            "name": f"braid_A{n - 1}_tsetlin", "family": "braid", "parameter": n,
            "hyperplanes": hyperplanes, "faces": faces, "chambers": chambers,
            "weights": normalize_weight_rows([(tsetlin[i], raw[i]) for i in range(n)]),
            "tags": ["separating", "tsetlin-regression"],
        })

    n = 4
    hyperplanes, faces, chambers, tsetlin = braid_data(n)
    cases.append({
        "name": "braid_A3_nonseparating_H12", "family": "braid", "parameter": n,
        "hyperplanes": hyperplanes, "faces": faces, "chambers": chambers,
        "weights": normalize_weight_rows([(tsetlin[2], 2), (tsetlin[3], 3)]),
        "tags": ["nonseparating", "tsetlin-boundary", "component-simplex"],
    })
    return cases


def mobius_rows(faces: list[Sign], weights: dict[Sign, Q]) -> list[dict]:
    flats = sorted({zero_set(face) for face in faces}, key=lambda z: (len(z), tuple(sorted(z))))
    mu: dict[frozenset[int], int] = {}
    rank: dict[frozenset[int], int] = {}
    for z in flats:
        mu[z] = 1 if not z else -sum(mu[y] for y in flats if y < z)
        rank[z] = 0 if not z else 1 + max(rank[y] for y in flats if y < z)
    rows = []
    for z in flats:
        lam = sum((weight for face, weight in weights.items() if z <= zero_set(face)), Q(0))
        rows.append({
            "zero_hyperplane_indices": sorted(z),
            "codimension": rank[z],
            "mobius_to_ambient": mu[z],
            "multiplicity": abs(mu[z]),
            "lambda": enc(lam),
        })
    return rows


def transition(chambers: list[Sign], weights: dict[Sign, Q]) -> list[list[Q]]:
    index = {chamber: i for i, chamber in enumerate(chambers)}
    out = [[Q(0) for _ in chambers] for _ in chambers]
    for i, chamber in enumerate(chambers):
        for face, weight in weights.items():
            out[i][index[face_product(face, chamber)]] += weight
    return out


def weighted_without_replacement(weights: dict[Sign, Q]) -> dict[Sign, Q]:
    faces = sorted(weights)
    distribution: dict[Sign, Q] = {}
    for order in permutations(faces):
        remaining = Q(1)
        probability = Q(1)
        aggregate = tuple(0 for _ in order[0])
        for face in order:
            probability *= weights[face] / remaining
            remaining -= weights[face]
            aggregate = face_product(aggregate, face)
            if remaining == 0:
                break
        distribution[aggregate] = distribution.get(aggregate, Q(0)) + probability
    return distribution


def sequence_failure(weights: dict[Sign, Q], length: int) -> Q:
    faces = sorted(weights)
    result = Q(0)
    zero = tuple(0 for _ in faces[0])
    for sequence in product(faces, repeat=length):
        aggregate = zero
        probability = Q(1)
        for face in sequence:
            probability *= weights[face]
            aggregate = face_product(aggregate, face)
        if 0 in aggregate:
            result += probability
    return result


def analyze_case(case: dict) -> dict:
    hyperplanes: list[str] = case["hyperplanes"]
    faces: list[Sign] = case["faces"]
    chambers: list[Sign] = case["chambers"]
    weights = dict(case["weights"])
    assert set(weights) <= set(faces) and sum(weights.values(), Q(0)) == 1
    matrix = transition(chambers, weights)
    flats = mobius_rows(faces, weights)
    separating = all(any(face[h] != 0 and weight > 0 for face, weight in weights.items()) for h in range(len(hyperplanes)))
    a0 = [h for h in range(len(hyperplanes)) if all(face[h] == 0 for face in weights)]
    component_keys = sorted({tuple(chamber[h] for h in a0) for chamber in chambers})

    charpoly = [Q(1)]
    determinant = [Q(1)]
    for flat in flats:
        lam = Q(flat["lambda"])
        multiplicity = flat["multiplicity"]
        charpoly = poly_mul(charpoly, poly_power_linear(-lam, Q(1), multiplicity))
        determinant = poly_mul(determinant, poly_power_linear(Q(1), -lam, multiplicity))
    assert len(charpoly) == len(chambers) + 1
    assert len(determinant) == len(chambers) + 1

    powers = [identity(len(chambers))]
    for _ in range(5):
        powers.append(matmul(powers[-1], matrix))
    trace_rows = []
    for exponent, power_matrix in enumerate(powers):
        direct = sum((power_matrix[i][i] for i in range(len(chambers))), Q(0))
        spectral = sum((Q(row["multiplicity"]) * Q(row["lambda"]) ** exponent for row in flats), Q(0))
        assert direct == spectral
        trace_rows.append({"power": exponent, "direct": enc(direct), "spectral": enc(spectral)})

    sampler_rows = []
    mixing_rows = []
    if separating:
        sampler = weighted_without_replacement(weights)
        assert set(sampler) <= set(chambers) and sum(sampler.values(), Q(0)) == 1
        stationary = [sampler.get(chamber, Q(0)) for chamber in chambers]
        propagated = [sum((stationary[i] * matrix[i][j] for i in range(len(chambers))), Q(0)) for j in range(len(chambers))]
        assert propagated == stationary
        sampler_rows = [
            {"chamber": list(chamber), "probability": enc(probability)}
            for chamber, probability in sorted(sampler.items()) if probability
        ]
        for exponent in range(1, 5):
            failure = sequence_failure(weights, exponent)
            mobius_failure = -sum(
                (Q(row["mobius_to_ambient"]) * Q(row["lambda"]) ** exponent for row in flats if row["zero_hyperplane_indices"]),
                Q(0),
            )
            hyperplane_bound = sum((Q(flats_for_h["lambda"]) ** exponent for flats_for_h in flats if len(flats_for_h["zero_hyperplane_indices"]) == 1), Q(0))
            worst_tv = Q(0)
            power_matrix = powers[exponent]
            for row in power_matrix:
                tv = sum((abs(x - y) for x, y in zip(row, stationary)), Q(0)) / 2
                worst_tv = max(worst_tv, tv)
            assert failure == mobius_failure and worst_tv <= failure <= hyperplane_bound
            mixing_rows.append({
                "power": exponent,
                "worst_total_variation": enc(worst_tv),
                "exact_failure_probability": enc(failure),
                "mobius_failure_probability": enc(mobius_failure),
                "hyperplane_union_bound": enc(hyperplane_bound),
            })

    return {
        "name": case["name"], "family": case["family"], "parameter": case["parameter"], "tags": case["tags"],
        "hyperplanes": hyperplanes,
        "faces": [list(face) for face in faces],
        "chambers": [list(chamber) for chamber in chambers],
        "positive_weights": [{"face": list(face), "weight": enc(weight)} for face, weight in sorted(weights.items())],
        "separating": separating,
        "nonseparating_hyperplane_indices": a0,
        "component_keys": [list(key) for key in component_keys],
        "stationary_simplex_vertex_count": len(component_keys),
        "flats": flats,
        "transition_matrix": enc_matrix(matrix),
        "charpoly_ascending": enc_vec(charpoly),
        "det_I_minus_zK_ascending": enc_vec(determinant),
        "power_traces": trace_rows,
        "without_replacement_stationary": sampler_rows,
        "mixing": mixing_rows,
    }


def main() -> None:
    cases = [analyze_case(case) for case in catalog()]
    aggregate = {
        "case_count": len(cases),
        "separating_case_count": sum(case["separating"] for case in cases),
        "nonseparating_case_count": sum(not case["separating"] for case in cases),
        "face_count": sum(len(case["faces"]) for case in cases),
        "chamber_count": sum(len(case["chambers"]) for case in cases),
        "flat_count": sum(len(case["flats"]) for case in cases),
        "transition_cell_count": sum(len(case["chambers"]) ** 2 for case in cases),
        "stationary_probability_count": sum(len(case["without_replacement_stationary"]) for case in cases),
        "mixing_row_count": sum(len(case["mixing"]) for case in cases),
        "trace_row_count": sum(len(case["power_traces"]) for case in cases),
    }
    document = {
        "schema": "hcs-c192-evidence-v1",
        "candidate_id": "HCS-C192",
        "evaluation_date": "2026-08-27",
        "source_commit": SOURCE_COMMIT,
        "evaluator": {"version": "0.2.0", "path": "flow_systems/skills/route-a-evaluator.md", "sha256": EVALUATOR_SHA256},
        "scope_literal": SCOPE,
        "source_lock": {
            "primary": {
                "authors": "Kenneth S. Brown and Persi Diaconis",
                "title": "Random Walk and Hyperplane Arrangements",
                "journal": "The Annals of Probability 26(4), 1813--1854 (1998)",
                "doi": "10.1214/aop/1022855884",
                "theorem_locators": ["Theorem 1", "Theorem 2", "Theorem 3", "Section 4B", "Section 6"],
            },
            "oriented_matroid_ceiling": "Theorems 1 and 2 carry over to the covector face semigroup of an oriented matroid as stated in Section 6; no stronger affine or realization claim is imported.",
            "strict_sst_boundary": "The stopping sampler and coupling bound are source-supported; independence of the stopped chamber from the stopping time is not asserted and strict-SST terminology is rejected.",
        },
        "theorem_lock": {
            "domain": "Every finite real hyperplane arrangement with an arbitrary probability measure on its face semigroup.",
            "spectrum": "K is diagonalizable with flat-indexed eigenvalues lambda_W=sum_{F subset W} w(F) and multiplicities |mu(W,V)|.",
            "operator_corollaries": "The flat factorization gives the characteristic polynomial, det(I-zK), and every power trace exactly.",
            "stationarity": "The face measure is separating exactly when the chamber chain has a unique stationary distribution.",
            "sampler": "Under separation, weighted sampling without replacement gives an exact stationary chamber; the with-replacement chamber-hitting construction is a stationary stopping sampler and coupling, not a claimed strict strong stationary time.",
            "mixing": "For every start, total variation is bounded by the exact nonchamber probability -sum_{W != V} mu(W,V)lambda_W^ell and hence by sum_{H in A} lambda_H^ell.",
            "nonseparating": "If A0 is the set of hyperplanes containing the support of w, A0-chambers are closed components, each has one stationary law, and all stationary laws form the simplex on those components.",
        },
        "attribution": {
            "status": "CLASSICAL_THEOREM_SOURCE_LOCKED_FINITE_REGRESSION_ONLY",
            "all_family_proof_owner": "Brown--Diaconis (1998), Theorems 1--3 and Sections 4, 6",
            "code_role": "finite exact regression oracle only",
            "novelty_claimed": False,
            "external_review_claimed": False,
        },
        "finite_regression": aggregate,
        "cases": cases,
        "route_a": {
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
        },
        "forbidden_claims": {
            "bad_euler_or_root_number": False,
            "local_or_euler_factors": False,
            "root_numbers": False,
            "automorphy": False,
            "hilbert_polya_operator": False,
            "target_divisor_identified": False,
            "strict_strong_stationary_time": False,
            "global_novelty": False,
        },
    }
    payload = json.dumps(document, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    document["payload_sha256"] = sha256(payload).hexdigest()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(document, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "C192_PRODUCER_PASS", "payload_sha256": document["payload_sha256"], **aggregate}, sort_keys=True))


if __name__ == "__main__":
    main()
