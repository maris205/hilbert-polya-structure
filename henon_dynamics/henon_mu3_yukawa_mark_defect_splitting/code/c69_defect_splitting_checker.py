#!/usr/bin/env python3
"""Independent exact checker for the C69 splitting certificate."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c69_defect_splitting_evidence.json"
SOURCE_PATHS = {
    "c64": ROOT / "henon_dynamics/henon_mu3_yukawa_burnside_marks/results/c64_mark_evidence.json",
    "c64_manifest": ROOT / "henon_dynamics/henon_mu3_yukawa_burnside_marks/C64_PREFREEZE_MANIFEST.json",
    "c65": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_defect/results/c65_defect_evidence.json",
    "c65_manifest": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_defect/C65_PREFREEZE_MANIFEST.json",
    "c66": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_cokernel/results/c66_mark_snf_evidence.json",
    "c66_manifest": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_cokernel/C66_PREFREEZE_MANIFEST.json",
    "c68": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_defect_duality/results/c68_defect_duality_evidence.json",
    "c68_manifest": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_defect_duality/C68_PREFREEZE_MANIFEST.json",
}
HASHES = {
    "c64": "7c4673e46f2b97ac03d4e331c762a47286058c36ea243fb20fc39543dd699212",
    "c64_manifest": "eb1d6a55cb81ccfc9b3041879cb913367a514f5c4cba50872d8b286c0ac095b6",
    "c65": "ebdd80fd2292225b98248aacd6b21bafab2987bdccb801c22c10adef7e7b4e4c",
    "c65_manifest": "f8709e490d0c077c6498ce96617d6711b58790d245e93e20124aa43b3dadc913",
    "c66": "ce74edeec04b245637e5b12165a7fcdeb42475b0dead7373b1bcf3e37f22beb1",
    "c66_manifest": "aa9a750fd87cfd09948167e0af93145823dff7d34c7bdb1ed13d1a8df493c626",
    "c68": "6d99afb5ec5e291f068f603060c79c72114e3fd2c26e0c9c21fdd5281add9ab9",
    "c68_manifest": "aab32e57216e091c2eeedc2486a6651d83bfac713ad6f290d9c1bb9b45a947bc",
}
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
EXPECTED_SNF = [1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 12, 144]


def canon(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def multiply(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def determinant(a0: list[list[int]]) -> int:
    a = [[Fraction(x) for x in row] for row in a0]
    value = Fraction(1)
    sign = 1
    for col in range(len(a)):
        pivot = next(r for r in range(col, len(a)) if a[r][col])
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            sign *= -1
        q = a[col][col]
        value *= q
        for r in range(col + 1, len(a)):
            if a[r][col]:
                t = a[r][col] / q
                a[r] = [x - t * y for x, y in zip(a[r], a[col])]
    assert value.denominator == 1
    return sign * value.numerator


def solve_left(b: list[list[int]], m: list[list[int]]) -> list[list[int]]:
    """Solve B*N=M by exact Gauss--Jordan elimination."""
    n = len(b)
    work = [[Fraction(x) for x in row] + [Fraction(x) for x in m[i]]
            for i, row in enumerate(b)]
    for col in range(n):
        pivot = next(r for r in range(col, n) if work[r][col])
        work[col], work[pivot] = work[pivot], work[col]
        q = work[col][col]
        work[col] = [x / q for x in work[col]]
        for r in range(n):
            if r != col and work[r][col]:
                q = work[r][col]
                work[r] = [x - q * y for x, y in zip(work[r], work[col])]
    right = [row[n:] for row in work]
    assert all(x.denominator == 1 for row in right for x in row)
    return [[int(x) for x in row] for row in right]


def smith(a0: list[list[int]]) -> list[int]:
    """Independent pivot/remainder Smith reduction."""
    a = [row[:] for row in a0]
    result: list[int] = []
    k = 0
    while k < len(a) and k < len(a[0]):
        candidates = [(abs(a[i][j]), i, j) for i in range(k, len(a))
                      for j in range(k, len(a[0])) if a[i][j]]
        if not candidates:
            break
        _, i, j = min(candidates)
        a[k], a[i] = a[i], a[k]
        for row in a:
            row[k], row[j] = row[j], row[k]
        while True:
            moved = False
            for i in range(k + 1, len(a)):
                if a[i][k]:
                    q, _ = divmod(a[i][k], a[k][k])
                    a[i] = [x - q * y for x, y in zip(a[i], a[k])]
                    if a[i][k] and abs(a[i][k]) < abs(a[k][k]):
                        a[k], a[i] = a[i], a[k]
                    moved = True
                    break
            if moved:
                continue
            for j in range(k + 1, len(a[0])):
                if a[k][j]:
                    q, _ = divmod(a[k][j], a[k][k])
                    for i in range(len(a)):
                        a[i][j] -= q * a[i][k]
                    if a[k][j] and abs(a[k][j]) < abs(a[k][k]):
                        for row in a:
                            row[k], row[j] = row[j], row[k]
                    moved = True
                    break
            if moved:
                continue
            bad = next(((i, j) for i in range(k + 1, len(a))
                        for j in range(k + 1, len(a[0]))
                        if a[i][j] % a[k][k]), None)
            if bad:
                i, _ = bad
                a[k] = [x + y for x, y in zip(a[k], a[i])]
                continue
            break
        if a[k][k] < 0:
            a[k] = [-x for x in a[k]]
        result.append(a[k][k])
        k += 1
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=EVIDENCE)
    args = parser.parse_args()
    raw = args.evidence.read_bytes()
    doc = json.loads(raw)
    assert raw == canon(doc)
    assert doc["schema_id"] == "hcs-c69-defect-splitting-prefreeze-v1"
    assert doc["status"] == "PREFREEZE_G3_PASS"
    assert doc["scope_literal"] == FIREWALL
    assert doc["type_order"] == [f"S{i}" for i in range(1, 17)]
    assert {name: digest(path.read_bytes()) for name, path in SOURCE_PATHS.items()} == HASHES
    c64 = json.loads(SOURCE_PATHS["c64"].read_text())
    c65 = json.loads(SOURCE_PATHS["c65"].read_text())
    c66 = json.loads(SOURCE_PATHS["c66"].read_text())
    c68 = json.loads(SOURCE_PATHS["c68"].read_text())
    assert doc["authority"] == {**HASHES, "c64_matrix_sha256": c64["matrix_sha256"]}
    assert c64["matrix_sha256"] == "4e57d980e774e14709d60feac0fff5af831b6496409d248f398a8a3e2796c307"
    assert c68["quotient_smith_invariants"] == EXPECTED_SNF

    M = c64["mark_matrix"]
    U = [[c65["all_saturation_basis"][f"u{j + 1}"][i] for j in range(3)]
         for i in range(16)]
    moduli = [8, 2, 2]
    expected_R = [[0] * 16 for _ in range(3)]
    expected_R[0][9] = 1
    expected_R[1][2] = 1
    expected_R[2][0] = expected_R[2][14] = 1
    assert doc["moduli"] == moduli
    assert doc["retraction_formula"] == ["x10 mod 8", "x3 mod 2", "x1+x15 mod 2"]
    assert doc["retraction_matrix"] == expected_R
    assert doc["retraction_matrix_sha256"] == digest(canon(expected_R))
    RM = multiply(expected_R, M)
    RU = multiply(expected_R, U)
    zero = [[RM[i][j] % moduli[i] for j in range(16)] for i in range(3)]
    identity = [[RU[i][j] % moduli[i] for j in range(3)] for i in range(3)]
    assert zero == doc["RM_residues"] == [[0] * 16 for _ in range(3)]
    assert RU == doc["RU_integer"] == [[1, 0, 0], [0, -1, 0], [0, 0, -1]]
    assert identity == doc["RU_residues"] == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    expected_B = [[int(i == j) for j in range(16)] for i in range(16)]
    expected_B[14][0] = -1
    expected_B[2][2] = 2
    expected_B[9][9] = 8
    expected_B[14][14] = 2
    assert doc["complement_basis"] == expected_B
    assert doc["complement_basis_sha256"] == digest(canon(expected_B))
    assert abs(determinant(expected_B)) == doc["complement_lattice_index"] == 32
    RB = multiply(expected_R, expected_B)
    assert all(RB[i][j] % moduli[i] == 0 for i in range(3) for j in range(16))
    N = solve_left(expected_B, M)
    assert N == doc["complement_presentation"]
    assert doc["complement_presentation_sha256"] == digest(canon(N))
    assert multiply(expected_B, N) == M
    assert doc["presentation_identity"] == "B*N=M"
    assert smith(N) == doc["complement_smith_invariants"] == EXPECTED_SNF
    order = 1
    for value in EXPECTED_SNF:
        order *= value
    assert order == doc["complement_order"] == c68["quotient_order"] == 7077888
    assert doc["defect_invariants"] == [2, 2, 8] and doc["defect_order"] == 32
    assert doc["ambient_order"] == abs(determinant(M)) == c66["mark_determinant"] == 226492416
    assert doc["direct_product_order_check"] == order * 32 == 226492416
    quotient_2_primary_orders = [2] * 8 + [4] * 3 + [16]
    assert doc["quotient_2_primary_orders"] == quotient_2_primary_orders
    target_exponents = [3, 1, 1]
    hom_exponents = [sum(min(q.bit_length() - 1, target)
                         for q in quotient_2_primary_orders)
                     for target in target_exponents]
    assert doc["hom_exponents_by_target"] == hom_exponents == [17, 12, 12]
    row_counts = [2 ** exponent for exponent in hom_exponents]
    assert doc["retraction_row_solution_counts"] == row_counts == [131072, 4096, 4096]
    assert doc["retraction_count"] == doc["complement_count"] == 2 ** 41 == 2199023255552
    assert doc["claims"] == {
        "actual_c68_embedding_splits": True,
        "all_complements_counted": True,
        "arithmetic_local_claimed": False,
        "canonical_smith_basis_claimed": False,
        "complement_canonical_claimed": False,
        "full_burnside_ring_claimed": False,
    }
    print(json.dumps({"status": "PASS", "retraction": "VERIFIED",
                      "complement_lattice_index": 32,
                      "complement_smith_invariants": EXPECTED_SNF,
                      "complement_order": order,
                      "complement_count": 2 ** 41}, sort_keys=True))


if __name__ == "__main__":
    main()
