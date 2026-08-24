#!/usr/bin/env python3
"""Exact finite sign-itinerary pilot for the frozen Lozi map (C116)."""
from __future__ import annotations

import itertools
import json
from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results/c116_lozi_evidence.json"
NMAX = 8
A = Q(2)
BETA = Q(1, 2)
RHO = (Q(1, 2), Q(2, 3))
BRANCH = (
    ((A, BETA), (Q(1), Q(0))),
    ((-A, BETA), (Q(1), Q(0))),
)
SHIFT = (Q(1), Q(0))


def mm(left, right):
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )


def mv(matrix, vector):
    return tuple(sum(matrix[i][j] * vector[j] for j in range(2)) for i in range(2))


def add(left, right):
    return tuple(x + y for x, y in zip(left, right))


def det(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def identity():
    return ((Q(1), Q(0)), (Q(0), Q(1)))


def qstr(value):
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def qvec(vector):
    return [qstr(value) for value in vector]


def qmat(matrix):
    return [[qstr(value) for value in row] for row in matrix]


def rotations(word):
    return [tuple(word[i:] + word[:i]) for i in range(len(word))]


def canonical(word):
    return min(rotations(list(word)))


def primitive(word):
    n = len(word)
    return all(
        tuple(word) != tuple(word[:d] * (n // d))
        for d in range(1, n)
        if n % d == 0
    )


def affine_candidate(word):
    matrix, translation = identity(), (Q(0), Q(0))
    for symbol in word:
        matrix, translation = (
            mm(BRANCH[symbol], matrix),
            add(mv(BRANCH[symbol], translation), SHIFT),
        )
    lhs = (
        (Q(1) - matrix[0][0], -matrix[0][1]),
        (-matrix[1][0], Q(1) - matrix[1][1]),
    )
    denominator = det(lhs)
    if denominator == 0:
        return matrix, translation, None
    point = (
        (translation[0] * lhs[1][1] - lhs[0][1] * translation[1]) / denominator,
        (lhs[0][0] * translation[1] - translation[0] * lhs[1][0]) / denominator,
    )
    return matrix, translation, point


def classify(word):
    matrix, translation, point = affine_candidate(word)
    if point is None:
        return {
            "status": "singular_return",
            "return_matrix": qmat(matrix),
            "return_translation": qvec(translation),
        }
    current = point
    orbit = []
    for phase, symbol in enumerate(word):
        orbit.append(current)
        if current[0] == 0:
            return {
                "status": "border_hit",
                "affine_candidate": qvec(point),
                "failure_phase": phase,
                "failure_x": "0",
                "declared_symbol": symbol,
            }
        if (current[0] < 0) != (symbol == 0):
            return {
                "status": "sign_mismatch",
                "affine_candidate": qvec(point),
                "failure_phase": phase,
                "failure_x": qstr(current[0]),
                "declared_symbol": symbol,
            }
        current = add(mv(BRANCH[symbol], current), SHIFT)
    if current != point:
        raise AssertionError((word, point, current))
    return {
        "status": "admissible_strict",
        "affine_candidate": qvec(point),
        "strict_x_margin": qstr(min(abs(p[0]) for p in orbit)),
        "orbit_points": [qvec(p) for p in orbit],
        "return_matrix": qmat(matrix),
    }


def full_primitive_necklace_counts():
    counts = {}
    for n in range(1, NMAX + 1):
        necklaces = {
            canonical(list(word))
            for word in itertools.product((0, 1), repeat=n)
            if primitive(list(word))
        }
        counts[str(n)] = len(necklaces)
    return counts


def build_ledger():
    word_status_rows = []
    classifications = {}
    strict_words = {}
    for n in range(1, NMAX + 1):
        counter = Counter()
        strict_words[n] = []
        for word in itertools.product((0, 1), repeat=n):
            result = classify(word)
            counter[result["status"]] += 1
            if result["status"] == "admissible_strict":
                strict_words[n].append(tuple(word))
            word_status_rows.append(
                {
                    "length": n,
                    "word": "".join(map(str, word)),
                    **{key: value for key, value in result.items() if key != "orbit_points" and key != "return_matrix"},
                }
            )
        classifications[str(n)] = {
            "total_words": 2**n,
            "admissible_strict": counter["admissible_strict"],
            "sign_mismatch": counter["sign_mismatch"],
            "border_hit": counter["border_hit"],
            "singular_return": counter["singular_return"],
        }

    primitive_rows = []
    primitive_counts = {}
    for n in range(1, NMAX + 1):
        seen = set()
        for word in strict_words[n]:
            if not primitive(list(word)):
                continue
            representative = canonical(list(word))
            if representative in seen:
                continue
            seen.add(representative)
            result = classify(representative)
            matrix = tuple(tuple(Q(value) for value in row) for row in result["return_matrix"])
            weight = Q(1)
            for symbol in representative:
                weight *= RHO[symbol]
            lam = sp.Symbol("lambda")
            sym_matrix = sp.Matrix([[sp.Rational(value.numerator, value.denominator) for value in row] for row in matrix])
            characteristic = sp.factor(sym_matrix.charpoly(lam).as_expr())
            primitive_rows.append(
                {
                    "length": n,
                    "word": "".join(map(str, representative)),
                    "symbols": list(representative),
                    "fixed_point": result["affine_candidate"],
                    "orbit_points": result["orbit_points"],
                    "strict_x_margin": result["strict_x_margin"],
                    "monodromy": result["return_matrix"],
                    "monodromy_trace": qstr(matrix[0][0] + matrix[1][1]),
                    "monodromy_determinant": qstr(det(matrix)),
                    "monodromy_characteristic": str(characteristic),
                    "branch_weight": qstr(weight),
                    "negative_visits": representative.count(0),
                    "positive_visits": representative.count(1),
                    "rooted_start_multiplicity": n,
                    "cyclic_stabilizer_size": 1,
                    "domain_check": "strict_pass",
                }
            )
        primitive_counts[str(n)] = len(seen)
    return word_status_rows, classifications, primitive_rows, primitive_counts


def cycle_atlas_operator(primitive_rows):
    blocks = []
    sparse_edges = []
    offset = 0
    factor_counter = Counter()
    for row in primitive_rows:
        n = row["length"]
        symbols = row["symbols"]
        edge_weights = [RHO[symbol] for symbol in symbols]
        product_weight = Q(1)
        for value in edge_weights:
            product_weight *= value
        blocks.append(
            {
                "word": row["word"],
                "state_offset": offset,
                "size": n,
                "edge_weights": [qstr(value) for value in edge_weights],
                "cycle_weight": qstr(product_weight),
            }
        )
        for phase, (symbol, value) in enumerate(zip(symbols, edge_weights)):
            sparse_edges.append(
                {
                    "source": offset + phase,
                    "target": offset + ((phase + 1) % n),
                    "weight": qstr(value),
                    "symbol": symbol,
                    "cycle_word": row["word"],
                    "phase": phase,
                }
            )
        factor_counter[(n, product_weight)] += 1
        offset += n

    traces = {}
    unweighted = {}
    for power in range(1, NMAX + 1):
        weighted_trace = Q(0)
        unweighted_trace = 0
        for row in primitive_rows:
            n = row["length"]
            if power % n:
                continue
            weight = Q(row["branch_weight"])
            weighted_trace += n * weight ** (power // n)
            unweighted_trace += n
        traces[str(power)] = qstr(weighted_trace)
        unweighted[str(power)] = unweighted_trace

    factor_ledger = [
        {"length": n, "cycle_weight": qstr(weight), "multiplicity": multiplicity}
        for (n, weight), multiplicity in sorted(factor_counter.items())
    ]
    return {
        "construction": "direct sum of one weighted cyclic block per certified primitive itinerary",
        "dimension": offset,
        "block_count": len(blocks),
        "weight_convention": "the edge at phase k carries rho_{word[k]}",
        "blocks": blocks,
        "sparse_edges": sparse_edges,
        "determinant_factor_ledger": factor_ledger,
        "determinant_factorization": "product over ledger entries of (1-cycle_weight*z^length)^multiplicity",
        "weighted_trace_prefix": traces,
        "unweighted_trace_prefix": unweighted,
        "certified_through_power": NMAX,
        "qualification": "finite cycle-atlas operator only; not a global Markov matrix or Fredholm owner",
    }


def main():
    word_rows, classifications, primitive_rows, primitive_counts = build_ledger()
    full_counts = full_primitive_necklace_counts()
    pruned_counts = {
        str(n): full_counts[str(n)] - primitive_counts[str(n)]
        for n in range(1, NMAX + 1)
    }
    rooted_counts = {
        str(n): classifications[str(n)]["admissible_strict"]
        for n in range(1, NMAX + 1)
    }
    operator = cycle_atlas_operator(primitive_rows)
    assert operator["unweighted_trace_prefix"] == rooted_counts
    assert len(primitive_rows) == 37 and operator["dimension"] == 240
    assert sum(row["length"] for row in primitive_rows) == 240
    assert all(classifications[str(n)]["border_hit"] == 0 for n in range(1, NMAX + 1))
    assert all(classifications[str(n)]["singular_return"] == 0 for n in range(1, NMAX + 1))

    payload = {
        "schema": "hcs-c116-lozi-nonsmooth-route-a-v1",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "source_model": {
            "map": "L(x,y)=(1-2*abs(x)+(1/2)*y,x)",
            "parameters": {"a": "2", "b": "1/2"},
            "branch_domains": {"0": "x<0", "1": "x>0"},
            "branch_matrices": [qmat(matrix) for matrix in BRANCH],
            "translation": qvec(SHIFT),
            "border": "x=0 excluded before enumeration",
            "diagnostic_branch_weights": [qstr(value) for value in RHO],
            "max_period": NMAX,
            "parameter_choice": "preferred small rational pilot retained because exact pruning is already nondegenerate from period 3",
        },
        "word_classification_counts": classifications,
        "word_status_rows": word_rows,
        "rooted_admissible_counts": rooted_counts,
        "full_binary_primitive_necklace_counts": full_counts,
        "primitive_necklace_counts": primitive_counts,
        "pruned_primitive_necklace_counts": pruned_counts,
        "primitive_rows": primitive_rows,
        "finite_cycle_atlas_operator": operator,
        "verdict": {
            "A1": "A1_PARTIAL_CERTIFIED",
            "A2": "A2_CERTIFIED_PREFIX",
            "A3": "A3_NOT_ADDRESSED",
            "A4": "A4_FAIL",
            "qualification": "strict finite sign-itinerary and cycle-atlas prefix only",
        },
        "nonclaims": [
            "complete Lozi invariant set",
            "global Markov partition",
            "analytic Fredholm determinant",
            "arithmetic data",
            "Route B",
        ],
    }
    raw = json.dumps(payload, sort_keys=True, indent=2) + "\n"
    OUT.write_text(raw)
    print(
        json.dumps(
            {
                "evidence_sha256": sha256(raw.encode()).hexdigest(),
                "primitive_necklaces": len(primitive_rows),
                "operator_dimension": operator["dimension"],
                "rooted_counts": rooted_counts,
                "status": "C116_PREFREEZE_G3_PASS",
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
