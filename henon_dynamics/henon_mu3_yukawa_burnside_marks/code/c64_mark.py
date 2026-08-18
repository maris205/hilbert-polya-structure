#!/usr/bin/env python3
"""Produce the exact 16-type table-of-marks certificate for HCS-C64.

The producer deliberately rebinds the C61 group and C62 subgroup elements.
The C63 character certificate is used only for the named relation and its
source digest; the mark matrix is recomputed from subgroup containment.
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
C61 = ROOT / "henon_dynamics/henon_mu3_yukawa_tensor_fourier_descent"
C62 = ROOT / "henon_dynamics/henon_mu3_yukawa_lambda_square_shadow"
C63 = ROOT / "henon_dynamics/henon_mu3_yukawa_burnside_kernel_rank"
INPUT_C61 = C61 / "results/c61_group_evidence.json"
INPUT_ATLAS = C62 / "results/c62_atlas_evidence.json"
INPUT_DICT = C62 / "results/c62_dictionary_evidence.json"
INPUT_C63 = C63 / "results/c63_kernel_evidence.json"
OUTPUT = PROJECT / "results/c64_mark_evidence.json"

FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
EXPECTED = {
    "c61": "f4be3a2c5990120a97264505ba9f21b55b8f8c330521044936a52f68e8cd89e9",
    "atlas": "3c40a674779a0e2d6d1c69b7c4ccc9115c4b9a2ba049684e8c5204b94b621c40",
    "dictionary": "85dc05d043e3781631330083303b98995201c7c30b53aae2901d5fd874b6cd5e",
    "c63": "38f439cfe6ed71616a7c74d68bd07da73f5680566ae16f8c557ab2b5d1d16e26",
}
Perm = tuple[int, ...]


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def compose(left: Perm, right: Perm) -> Perm:
    return tuple(left[right[i]] for i in range(len(left)))


def inverse(p: Perm) -> Perm:
    out = [0] * len(p)
    for i, j in enumerate(p):
        out[j] = i
    return tuple(out)


def from_one(rows: Iterable[Iterable[int]]) -> tuple[Perm, ...]:
    return tuple(tuple(x - 1 for x in row) for row in rows)


def closure(generators: Iterable[Perm]) -> frozenset[Perm]:
    gens = tuple(generators)
    if not gens:
        raise ValueError("empty generator list")
    identity = tuple(range(len(gens[0])))
    out = {identity}
    stack = [identity]
    while stack:
        x = stack.pop()
        for g in gens:
            y = compose(g, x)
            if y not in out:
                out.add(y)
                stack.append(y)
    return frozenset(out)


def subgroup_generators(group: frozenset[Perm]) -> tuple[Perm, ...]:
    """Find a small deterministic generating set by greedy closure."""
    identity = tuple(range(len(next(iter(group)))))
    chosen: list[Perm] = []
    current = frozenset({identity})
    for g in sorted(group):
        if g in current:
            continue
        chosen.append(g)
        current = closure(chosen)
        if current == group:
            return tuple(chosen)
    raise RuntimeError("failed to generate subgroup")


def group_digest(group: frozenset[Perm]) -> str:
    return sha(canonical([[x + 1 for x in p] for p in sorted(group)]))


def bareiss_det(matrix: list[list[int]]) -> int:
    """Fraction-free determinant, with no floating-point arithmetic."""
    a = [row[:] for row in matrix]
    n = len(a)
    if n == 0:
        return 1
    sign = 1
    previous = 1
    for k in range(n - 1):
        pivot = next((r for r in range(k, n) if a[r][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        pivot_value = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * pivot_value - a[i][k] * a[k][j]) // previous
        for i in range(k + 1, n):
            a[i][k] = 0
        previous = pivot_value
    return sign * a[-1][-1]


def rank_q(matrix: list[list[int]]) -> int:
    a = [[Fraction(x) for x in row] for row in matrix]
    if not a:
        return 0
    rows, cols = len(a), len(a[0])
    rank = 0
    for col in range(cols):
        pivot = next((r for r in range(rank, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        scale = a[rank][col]
        a[rank] = [x / scale for x in a[rank]]
        for r in range(rows):
            if r == rank or not a[r][col]:
                continue
            scale = a[r][col]
            a[r] = [x - scale * y for x, y in zip(a[r], a[rank])]
        rank += 1
    return rank


def load_inputs() -> tuple[dict, dict, dict, dict, dict[str, str]]:
    paths = {"c61": INPUT_C61, "atlas": INPUT_ATLAS, "dictionary": INPUT_DICT, "c63": INPUT_C63}
    raws = {key: path.read_bytes() for key, path in paths.items()}
    hashes = {key: sha(raw) for key, raw in raws.items()}
    assert hashes == EXPECTED, hashes
    c61, atlas, dictionary, c63 = (json.loads(raws[key]) for key in ("c61", "atlas", "dictionary", "c63"))
    assert atlas["schema_id"] == "hcs-c62-complete-atlas-prefreeze-v1"
    assert dictionary["schema_id"] == "hcs-c62-fixed-field-dictionary-prefreeze-v1"
    assert c63["schema_id"] == "hcs-c63-burnside-kernel-prefreeze-v1"
    assert c61["semantic_firewall"] == FIREWALL
    for data in (atlas, dictionary, c63):
        assert data["scope_literal"] == FIREWALL
    assert c63["status"] == "PREFREEZE_G3_PASS"
    return c61, atlas, dictionary, c63, hashes


def recover_types(c61: dict, atlas: dict, dictionary: dict) -> tuple[frozenset[Perm], ...]:
    ambient_data = c61["python_projection"]["ambient"]
    ambient = closure(from_one(ambient_data["W_generators_one_based"]))
    assert len(ambient) == 51840
    by_digest: dict[str, frozenset[Perm]] = {}
    for table in atlas["atlases"].values():
        for row in table["rows"]:
            for side in ("plus", "minus"):
                item = row[side]
                subgroup = frozenset(from_one(item["stabilizer_elements_one_based"]))
                assert group_digest(subgroup) == item["stabilizer_sha256"]
                by_digest[item["stabilizer_sha256"]] = subgroup
    types = sorted(dictionary["types"], key=lambda item: int(item["type_id"][1:]))
    assert [item["type_id"] for item in types] == [f"S{i}" for i in range(1, 17)]
    out = []
    for item in types:
        subgroup = by_digest[item["representative_sha256"]]
        assert len(subgroup) == item["order"]
        assert item["core_order"] == 1
        assert len(ambient) == item["field_degree"] * item["order"]
        out.append(subgroup)
    return tuple(out)


def marks(ambient: frozenset[Perm], subgroups: tuple[frozenset[Perm], ...]) -> list[list[int]]:
    """Directly count fixed cosets using subgroup generators.

    For left cosets, a coset gS_j is fixed by S_i exactly when
    g^{-1} S_i g is contained in S_j.  Testing a generating set is enough,
    but the resulting count is still over every element of the frozen group.
    """
    inverses = {g: inverse(g) for g in ambient}
    generators = [subgroup_generators(s) for s in subgroups]
    result: list[list[int]] = []
    for source, gens in enumerate(generators):
        row: list[int] = []
        for target in subgroups:
            count = 0
            target_order = len(target)
            for g in ambient:
                gi = inverses[g]
                if all(compose(compose(gi, h), g) in target for h in gens):
                    count += 1
            assert count % target_order == 0
            row.append(count // target_order)
        result.append(row)
    return result


def main() -> None:
    c61, atlas, dictionary, c63, source_hashes = load_inputs()
    ambient_data = c61["python_projection"]["ambient"]
    ambient = closure(from_one(ambient_data["W_generators_one_based"]))
    subgroups = recover_types(c61, atlas, dictionary)
    matrix = marks(ambient, subgroups)
    expected_r4 = [0, 1, 1, 0, 1, 1, 0, 0, 0, 0, -1, -1, -1, -1, 0, 0]
    mark_r4 = [sum(matrix[i][j] * expected_r4[j] for j in range(16)) for i in range(16)]
    determinant = bareiss_det(matrix)
    matrix_hash = sha(canonical(matrix))
    r4_hash = sha(canonical(mark_r4))
    assert matrix == [
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [2,0,0,2,0,0,0,0,0,0,0,0,0,0,2,2],
        [0,0,0,0,2,0,0,0,0,0,2,0,0,0,0,0],
        [0,0,0,0,0,2,0,0,0,0,0,4,0,0,0,0],
        [7,12,12,24,0,0,36,0,0,0,12,12,0,0,14,14],
        [6,12,14,2,0,0,0,6,0,0,2,4,0,0,8,4],
        [0,0,0,0,0,0,0,0,16,0,0,0,0,0,0,0],
        [0,0,0,0,0,8,0,0,0,8,0,8,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0],
        [0,4,0,0,0,0,0,0,0,0,0,0,2,0,0,0],
        [2,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
    ]
    assert determinant == 226492416
    assert rank_q(matrix) == 16
    assert mark_r4 == [0,4,2,0,0,-2,0,20,0,0,-2,-4,2,0,0,0]
    assert any(mark_r4)
    content = 0
    from math import gcd
    for value in mark_r4:
        content = gcd(content, abs(value))
    assert content == 2
    result = {
        "schema_id": "hcs-c64-table-of-marks-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "authority": {**source_hashes, "ambient_order": len(ambient), "type_count": 16},
        "column_order": [f"S{i}" for i in range(1,17)],
        "row_order": [f"S{i}" for i in range(1,17)],
        "subgroup_orders": [len(s) for s in subgroups],
        "core_orders": [1 for _ in subgroups],
        "mark_matrix": matrix,
        "matrix_sha256": matrix_hash,
        "rank_over_Q": rank_q(matrix),
        "determinant": determinant,
        "determinant_factorization": {"2": 23, "3": 3},
        "r4_vector": expected_r4,
        "r4_mark_vector": mark_r4,
        "r4_mark_sha256": r4_hash,
        "r4_mark_content": content,
        "claims": {
            "restricted_16_type_burnside_injective": True,
            "full_burnside_ring_claimed": False,
            "arithmetic_local_claimed": False,
        },
    }
    OUTPUT.write_bytes(canonical(result))
    print(json.dumps({"status": result["status"], "rank": result["rank_over_Q"], "determinant": determinant, "matrix_sha256": matrix_hash, "r4_mark_sha256": r4_hash}, sort_keys=True))


if __name__ == "__main__":
    main()
