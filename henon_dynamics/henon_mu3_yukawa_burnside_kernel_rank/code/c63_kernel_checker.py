#!/usr/bin/env python3
"""Independent structural checker for C63 kernel evidence."""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

EVIDENCE = Path(__file__).resolve().parents[1] / "results/c63_kernel_evidence.json"
C61 = EVIDENCE.parents[2] / "henon_mu3_yukawa_tensor_fourier_descent/results/c61_group_evidence.json"
ATLAS = EVIDENCE.parents[2] / "henon_mu3_yukawa_lambda_square_shadow/results/c62_atlas_evidence.json"
DICTIONARY = EVIDENCE.parents[2] / "henon_mu3_yukawa_lambda_square_shadow/results/c62_dictionary_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def rank_q(matrix: list[list[int]]) -> int:
    a = [[Fraction(x) for x in row] for row in matrix]
    rows, cols = len(a), len(a[0]) if a else 0
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        q = a[r][c]
        a[r] = [x / q for x in a[r]]
        for i in range(rows):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [x - q * y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def mat_vec(matrix: list[list[int]], vector: list[int]) -> list[int]:
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=EVIDENCE)
    args = parser.parse_args()
    doc = json.loads(args.evidence.read_text())
    assert doc["schema_id"] == "hcs-c63-burnside-kernel-prefreeze-v1"
    assert doc["status"] == "PREFREEZE_G3_PASS"
    assert doc["scope_literal"] == FIREWALL
    assert doc["authority"] == {
        "ambient_order": 51840,
        "class_count": 25,
        "type_count": 16,
        "c61_group_evidence_sha256": sha256(C61.read_bytes()),
        "c62_atlas_evidence_sha256": sha256(ATLAS.read_bytes()),
        "c62_dictionary_evidence_sha256": sha256(DICTIONARY.read_bytes()),
    }
    assert doc["claims"] == {
        "arithmetic_local_claimed": False,
        "full_burnside_ring_kernel_claimed": False,
        "restricted_16_type_kernel_only": True,
    }
    assert doc["column_order"] == [f"S{i}" for i in range(1, 17)]
    assert len(doc["types"]) == 16
    assert len(doc["conjugacy_classes"]) == 25
    assert sum(row["size"] for row in doc["conjugacy_classes"]) == 51840
    assert all(row["centralizer_order"] * row["size"] == 51840 for row in doc["conjugacy_classes"])

    matrix = doc["character_matrix"]
    assert len(matrix) == 25 and all(len(row) == 16 for row in matrix)
    assert all(type(x) is int and x >= 0 for row in matrix for x in row)
    assert sha256(canonical(matrix)) == doc["matrix_sha256"]
    assert rank_q(matrix) == doc["rank_over_Q"] == 13
    assert doc["nullity_over_Q"] == 3

    def v(**entries: int) -> list[int]:
        return [entries.get(f"S{i}", 0) for i in range(1, 17)]

    expected_basis = {
        "z1": v(S10=1, S9=-1),
        "z2": v(S2=-1, S3=-1, S5=-1, S6=-1, S11=1, S12=1, S13=1, S14=1),
        "z3": v(S16=1, S15=-1),
    }
    assert doc["nullspace_basis"] == expected_basis
    assert all(mat_vec(matrix, x) == [0] * 25 for x in expected_basis.values())
    assert rank_q(list(expected_basis.values())) == 3

    expected_relations = {
        "r_c61": v(S15=1, S16=-1),
        "q_exterior": v(S2=1, S3=1, S5=1, S6=1, S11=-1, S12=-1, S13=-1, S14=-1),
    }
    expected_relations["q_symmetric"] = [a + b for a, b in zip(expected_relations["q_exterior"], expected_relations["r_c61"])]
    assert doc["relation_vectors"] == expected_relations
    assert all(mat_vec(matrix, x) == [0] * 25 for x in expected_relations.values())
    assert doc["hplus_type"] == "S15"
    assert doc["hminus_type"] == "S16"
    assert doc["common_hplus_hminus_character"] == [matrix[i][14] for i in range(25)]
    assert doc["common_hplus_hminus_character"] == [matrix[i][15] for i in range(25)]

    # The headline R4 has eight nonzero terms and its support-restricted
    # character matrix has one-dimensional kernel, so no proper support can
    # carry a nonzero relation (all eight coefficients are nonzero).
    q = expected_relations["q_exterior"]
    assert sum(abs(x) for x in q) == 8
    support = [i for i, x in enumerate(q) if x]
    primitive = doc["primitive_support"]
    assert primitive["type_ids"] == [doc["column_order"][i] for i in support]
    assert primitive["support_size"] == 8
    assert primitive["restricted_rank_over_Q"] == 7
    assert primitive["restricted_nullity_over_Q"] == 1
    assert len(primitive["exterior_pairing"]) == 10
    assert sum(row["nonconjugate_type_pair"] for row in primitive["exterior_pairing"]) == 4
    assert all(row["plus_type"] != row["minus_type"] for row in primitive["exterior_pairing"] if row["nonconjugate_type_pair"])
    assert [(row["orbit_size"], row["plus_type"], row["minus_type"])
            for row in primitive["exterior_pairing"] if row["nonconjugate_type_pair"]] == [
                (480, "S2", "S11"), (480, "S3", "S12"),
                (4320, "S5", "S13"), (4320, "S6", "S14")]
    assert set(support) == {1, 2, 4, 5, 10, 11, 12, 13}

    print(json.dumps({
        "status": "PASS",
        "ambient_order": 51840,
        "class_count": 25,
        "type_count": 16,
        "rank_over_Q": 13,
        "nullity_over_Q": 3,
        "primitive_four_term_support": 8,
        "primitive_restricted_rank": 7,
        "matrix_sha256": doc["matrix_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
