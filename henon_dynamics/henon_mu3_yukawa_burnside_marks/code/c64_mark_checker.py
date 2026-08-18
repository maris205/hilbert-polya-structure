#!/usr/bin/env python3
"""Independent checker/replay for the C64 table-of-marks evidence.

This file intentionally does not import ``c64_mark``.  It rebuilds the group,
the 16 subgroup representatives, and all 256 marks from the frozen source
bytes before comparing the submitted certificate.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c64_mark_evidence.json"
C61 = ROOT / "henon_dynamics/henon_mu3_yukawa_tensor_fourier_descent/results/c61_group_evidence.json"
ATLAS = ROOT / "henon_dynamics/henon_mu3_yukawa_lambda_square_shadow/results/c62_atlas_evidence.json"
DICTIONARY = ROOT / "henon_dynamics/henon_mu3_yukawa_lambda_square_shadow/results/c62_dictionary_evidence.json"
C63 = ROOT / "henon_dynamics/henon_mu3_yukawa_burnside_kernel_rank/results/c63_kernel_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
EXPECTED = {
    "c61": "f4be3a2c5990120a97264505ba9f21b55b8f8c330521044936a52f68e8cd89e9",
    "atlas": "3c40a674779a0e2d6d1c69b7c4ccc9115c4b9a2ba049684e8c5204b94b621c40",
    "dictionary": "85dc05d043e3781631330083303b98995201c7c30b53aae2901d5fd874b6cd5e",
    "c63": "38f439cfe6ed71616a7c74d68bd07da73f5680566ae16f8c557ab2b5d1d16e26",
}
TYPES = [f"S{i}" for i in range(1, 17)]
IDENTITY = tuple(range(27))


def canon(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(value: object) -> str:
    return hashlib.sha256(canon(value)).hexdigest()


def raw_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def product(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(a[b[i]] for i in range(len(a)))


def inverse(a: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * len(a)
    for i, j in enumerate(a):
        out[j] = i
    return tuple(out)


def permutations(rows: Iterable[Iterable[int]]) -> tuple[tuple[int, ...], ...]:
    return tuple(tuple(x - 1 for x in row) for row in rows)


def generate(generators: Iterable[tuple[int, ...]]) -> frozenset[tuple[int, ...]]:
    gs = tuple(generators)
    if not gs:
        raise ValueError("empty generators")
    seen = {tuple(range(len(gs[0])))}
    frontier = list(seen)
    while frontier:
        x = frontier.pop()
        for g in gs:
            y = product(g, x)
            if y not in seen:
                seen.add(y)
                frontier.append(y)
    return frozenset(seen)


def generators_of(group: frozenset[tuple[int, ...]]) -> tuple[tuple[int, ...], ...]:
    chosen: list[tuple[int, ...]] = []
    current = frozenset({IDENTITY})
    for x in sorted(group):
        if x in current:
            continue
        chosen.append(x)
        current = generate(chosen)
        if current == group:
            return tuple(chosen)
    raise AssertionError("could not recover subgroup generators")


def rank_q(matrix: list[list[int]]) -> int:
    a = [[Fraction(x) for x in row] for row in matrix]
    if not a:
        return 0
    rows, cols = len(a), len(a[0])
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        scale = a[pivot_row][col]
        a[pivot_row] = [x / scale for x in a[pivot_row]]
        for r in range(rows):
            if r != pivot_row and a[r][col]:
                scale = a[r][col]
                a[r] = [x - scale * y for x, y in zip(a[r], a[pivot_row])]
        pivot_row += 1
    return pivot_row


def determinant(matrix: list[list[int]]) -> int:
    a = [row[:] for row in matrix]
    n = len(a)
    sign = 1
    previous = 1
    for k in range(n - 1):
        pivot = next((r for r in range(k, n) if a[r][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign *= -1
        p = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * p - a[i][k] * a[k][j]) // previous
        previous = p
        for i in range(k + 1, n):
            a[i][k] = 0
    return sign * a[-1][-1]


def recover(c61: dict, atlas: dict, dictionary: dict) -> tuple[frozenset[tuple[int, ...]], tuple[frozenset[tuple[int, ...]], ...]]:
    ambient = generate(permutations(c61["python_projection"]["ambient"]["W_generators_one_based"]))
    assert len(ambient) == 51840
    by_digest: dict[str, frozenset[tuple[int, ...]]] = {}
    for table in atlas["atlases"].values():
        for row in table["rows"]:
            for side in ("plus", "minus"):
                item = row[side]
                subgroup = frozenset(permutations(item["stabilizer_elements_one_based"]))
                assert digest([[x + 1 for x in p] for p in sorted(subgroup)]) == item["stabilizer_sha256"]
                by_digest[item["stabilizer_sha256"]] = subgroup
    meta = {item["type_id"]: item for item in dictionary["types"]}
    subgroups = []
    for type_id in TYPES:
        item = meta[type_id]
        subgroup = by_digest[item["representative_sha256"]]
        assert len(subgroup) == item["order"]
        assert item["core_order"] == 1 and len(ambient) == item["field_degree"] * len(subgroup)
        subgroups.append(subgroup)
    return ambient, tuple(subgroups)


def recompute_marks(ambient: frozenset[tuple[int, ...]], subgroups: tuple[frozenset[tuple[int, ...]], ...]) -> list[list[int]]:
    inv = {x: inverse(x) for x in ambient}
    source_generators = [generators_of(s) for s in subgroups]
    matrix = []
    for gens in source_generators:
        row = []
        for target in subgroups:
            fixed_numer = 0
            for g in ambient:
                gi = inv[g]
                if all(product(product(gi, h), g) in target for h in gens):
                    fixed_numer += 1
            assert fixed_numer % len(target) == 0
            row.append(fixed_numer // len(target))
        matrix.append(row)
    return matrix


EXPECTED_MATRIX = [
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0], [2,0,0,2,0,0,0,0,0,0,0,0,0,0,2,2],
    [0,0,0,0,2,0,0,0,0,0,2,0,0,0,0,0], [0,0,0,0,0,2,0,0,0,0,0,4,0,0,0,0],
    [7,12,12,24,0,0,36,0,0,0,12,12,0,0,14,14], [6,12,14,2,0,0,0,6,0,0,2,4,0,0,8,4],
    [0,0,0,0,0,0,0,0,16,0,0,0,0,0,0,0], [0,0,0,0,0,8,0,0,0,8,0,8,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0],
    [0,4,0,0,0,0,0,0,0,0,0,0,2,0,0,0], [2,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=EVIDENCE)
    args = parser.parse_args()
    raw = args.evidence.read_bytes()
    doc = json.loads(raw)
    assert raw == canon(doc), "evidence is not canonical JSON"
    assert doc["schema_id"] == "hcs-c64-table-of-marks-prefreeze-v1"
    assert doc["status"] == "PREFREEZE_G3_PASS"
    assert doc["scope_literal"] == FIREWALL
    assert doc["claims"] == {"arithmetic_local_claimed": False, "full_burnside_ring_claimed": False, "restricted_16_type_burnside_injective": True}
    paths = {"c61": C61, "atlas": ATLAS, "dictionary": DICTIONARY, "c63": C63}
    assert {k: raw_hash(v) for k, v in paths.items()} == EXPECTED
    assert doc["authority"] == {**EXPECTED, "ambient_order": 51840, "type_count": 16}
    # Reject metadata and scalar tampering before the expensive source replay.
    assert doc["column_order"] == TYPES and doc["row_order"] == TYPES
    assert doc["subgroup_orders"] == [324,108,108,54,12,12,9,6,4,4,108,108,12,12,162,162]
    assert doc["core_orders"] == [1] * 16
    assert doc["matrix_sha256"] == "4e57d980e774e14709d60feac0fff5af831b6496409d248f398a8a3e2796c307"
    assert doc["rank_over_Q"] == 16 and doc["determinant"] == 226492416
    assert doc["r4_vector"] == [0,1,1,0,1,1,0,0,0,0,-1,-1,-1,-1,0,0]
    assert doc["r4_mark_vector"] == [0,4,2,0,0,-2,0,20,0,0,-2,-4,2,0,0,0]
    assert doc["mark_matrix"] == EXPECTED_MATRIX
    c61, atlas, dictionary = (json.loads(p.read_text()) for p in (C61, ATLAS, DICTIONARY))
    assert c61["semantic_firewall"] == FIREWALL
    assert atlas["scope_literal"] == dictionary["scope_literal"] == FIREWALL
    ambient, subgroups = recover(c61, atlas, dictionary)
    matrix = recompute_marks(ambient, subgroups)
    assert matrix == EXPECTED_MATRIX == doc["mark_matrix"]
    assert digest(matrix) == doc["matrix_sha256"]
    assert rank_q(matrix) == doc["rank_over_Q"] == 16
    assert determinant(matrix) == doc["determinant"] == 226492416
    assert doc["determinant_factorization"] == {"2": 23, "3": 3}
    r4 = [0,1,1,0,1,1,0,0,0,0,-1,-1,-1,-1,0,0]
    mark = [sum(matrix[i][j] * r4[j] for j in range(16)) for i in range(16)]
    assert doc["r4_vector"] == r4
    assert doc["r4_mark_vector"] == mark == [0,4,2,0,0,-2,0,20,0,0,-2,-4,2,0,0,0]
    assert doc["r4_mark_sha256"] == digest(mark)
    from math import gcd
    content = 0
    for value in mark:
        content = gcd(content, abs(value))
    assert doc["r4_mark_content"] == content == 2
    print(json.dumps({"status":"PASS", "ambient_order":len(ambient), "type_count":16, "rank":16, "determinant":226492416, "matrix_sha256":doc["matrix_sha256"], "r4_witness":mark[1]}, sort_keys=True))


if __name__ == "__main__":
    main()
