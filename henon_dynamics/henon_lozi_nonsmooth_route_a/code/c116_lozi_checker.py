#!/usr/bin/env python3
"""Independent exact checker for C116; it does not import the producer."""
from __future__ import annotations

import itertools
import json
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "results/c116_lozi_evidence.json").read_text())
NMAX = 8
MATS = (
    ((Q(2), Q(1, 2)), (Q(1), Q(0))),
    ((Q(-2), Q(1, 2)), (Q(1), Q(0))),
)
SHIFT = (Q(1), Q(0))
WEIGHTS = (Q(1, 2), Q(2, 3))


def mm(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def mv(a, v):
    return tuple(sum(a[i][j] * v[j] for j in range(2)) for i in range(2))


def determinant(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def fmt(value):
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def primitive(word):
    return all(tuple(word) != tuple(word[:d] * (len(word) // d)) for d in range(1, len(word)) if len(word) % d == 0)


def canonical(word):
    return min(tuple(word[i:] + word[:i]) for i in range(len(word)))


def solve(word):
    monodromy = ((Q(1), Q(0)), (Q(0), Q(1)))
    shift = (Q(0), Q(0))
    for symbol in word:
        old_shift = shift
        monodromy = mm(MATS[symbol], monodromy)
        image = mv(MATS[symbol], old_shift)
        shift = (image[0] + 1, image[1])
    lhs = ((1 - monodromy[0][0], -monodromy[0][1]), (-monodromy[1][0], 1 - monodromy[1][1]))
    divisor = determinant(lhs)
    if divisor == 0:
        return "singular_return", None, None, monodromy, None
    point = (
        (shift[0] * lhs[1][1] - lhs[0][1] * shift[1]) / divisor,
        (lhs[0][0] * shift[1] - shift[0] * lhs[1][0]) / divisor,
    )
    current = point
    orbit = []
    failure_phase = None
    status = "admissible_strict"
    for phase, symbol in enumerate(word):
        orbit.append(current)
        if current[0] == 0:
            status, failure_phase = "border_hit", phase
            break
        if (current[0] < 0) != (symbol == 0):
            status, failure_phase = "sign_mismatch", phase
            break
        image = mv(MATS[symbol], current)
        current = (image[0] + 1, image[1])
    if status == "admissible_strict":
        assert current == point
    return status, point, orbit, monodromy, failure_phase


assert DATA["schema"] == "hcs-c116-lozi-nonsmooth-route-a-v1"
assert DATA["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
assert DATA["source_model"]["parameters"] == {"a": "2", "b": "1/2"}
assert DATA["source_model"]["border"] == "x=0 excluded before enumeration"

status_rows = {(row["length"], row["word"]): row for row in DATA["word_status_rows"]}
primitive_rows = {(row["length"], row["word"]): row for row in DATA["primitive_rows"]}
computed_counts = {}
computed_primitive = {}
computed_full = {}
for n in range(1, NMAX + 1):
    statuses = Counter()
    primitive_admissible = set()
    primitive_full = set()
    for word_tuple in itertools.product((0, 1), repeat=n):
        word = list(word_tuple)
        status, point, orbit, monodromy, phase = solve(word)
        statuses[status] += 1
        key = (n, "".join(map(str, word)))
        receipt = status_rows[key]
        assert receipt["status"] == status
        if point is not None:
            assert receipt["affine_candidate"] == [fmt(value) for value in point]
        if status in {"sign_mismatch", "border_hit"}:
            assert receipt["failure_phase"] == phase
        if primitive(word):
            representative = canonical(word)
            primitive_full.add(representative)
            if status == "admissible_strict":
                primitive_admissible.add(representative)
        if status == "admissible_strict" and primitive(word) and tuple(word) == canonical(word):
            row = primitive_rows[(n, key[1])]
            assert row["fixed_point"] == [fmt(value) for value in point]
            assert row["orbit_points"] == [[fmt(value) for value in p] for p in orbit]
            assert row["strict_x_margin"] == fmt(min(abs(p[0]) for p in orbit))
            assert row["monodromy"] == [[fmt(value) for value in matrix_row] for matrix_row in monodromy]
            assert row["monodromy_determinant"] == fmt(determinant(monodromy))
            weight = Q(1)
            for symbol in word:
                weight *= WEIGHTS[symbol]
            assert row["branch_weight"] == fmt(weight)
    computed_counts[str(n)] = {
        "total_words": 2**n,
        "admissible_strict": statuses["admissible_strict"],
        "sign_mismatch": statuses["sign_mismatch"],
        "border_hit": statuses["border_hit"],
        "singular_return": statuses["singular_return"],
    }
    computed_primitive[str(n)] = len(primitive_admissible)
    computed_full[str(n)] = len(primitive_full)

assert computed_counts == DATA["word_classification_counts"]
assert {key: value["admissible_strict"] for key, value in computed_counts.items()} == DATA["rooted_admissible_counts"]
assert computed_primitive == DATA["primitive_necklace_counts"]
assert computed_full == DATA["full_binary_primitive_necklace_counts"]
assert {key: computed_full[key] - computed_primitive[key] for key in computed_full} == DATA["pruned_primitive_necklace_counts"]

operator = DATA["finite_cycle_atlas_operator"]
assert operator["block_count"] == len(primitive_rows) == 37
assert operator["dimension"] == sum(row["length"] for row in DATA["primitive_rows"]) == 240
assert len(operator["sparse_edges"]) == 240
for power in range(1, NMAX + 1):
    weighted = Q(0)
    unweighted = 0
    for row in DATA["primitive_rows"]:
        n = row["length"]
        if power % n == 0:
            weighted += n * Q(row["branch_weight"]) ** (power // n)
            unweighted += n
    assert operator["weighted_trace_prefix"][str(power)] == fmt(weighted)
    assert operator["unweighted_trace_prefix"][str(power)] == unweighted
    assert unweighted == DATA["rooted_admissible_counts"][str(power)]

assert DATA["verdict"] == {
    "A1": "A1_PARTIAL_CERTIFIED",
    "A2": "A2_CERTIFIED_PREFIX",
    "A3": "A3_NOT_ADDRESSED",
    "A4": "A4_FAIL",
    "qualification": "strict finite sign-itinerary and cycle-atlas prefix only",
}
print("C116_CHECK_PASS", len(status_rows), len(primitive_rows), operator["dimension"])
