#!/usr/bin/env python3
"""Produce the exact C69 retraction and complement certificate."""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
C64 = ROOT / "henon_dynamics/henon_mu3_yukawa_burnside_marks"
C65 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_defect"
C66 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_cokernel"
C68 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_defect_duality"
OUT = PROJECT / "results/c69_defect_splitting_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
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
MATRIX_HASH = "4e57d980e774e14709d60feac0fff5af831b6496409d248f398a8a3e2796c307"
EXPECTED_SNF = [1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 12, 144]


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def matrix_hash(a: list[list[int]]) -> str:
    return digest(canonical(a))


def multiply(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def inverse(a: list[list[int]]) -> list[list[Fraction]]:
    n = len(a)
    work = [[Fraction(x) for x in row] + [Fraction(i == j) for j in range(n)]
            for i, row in enumerate(a)]
    for col in range(n):
        pivot = next(r for r in range(col, n) if work[r][col])
        work[col], work[pivot] = work[pivot], work[col]
        q = work[col][col]
        work[col] = [x / q for x in work[col]]
        for r in range(n):
            if r == col or not work[r][col]:
                continue
            q = work[r][col]
            work[r] = [x - q * y for x, y in zip(work[r], work[col])]
    return [row[n:] for row in work]


def determinant(a: list[list[int]]) -> int:
    work = [[Fraction(x) for x in row] for row in a]
    value = Fraction(1)
    sign = 1
    for col in range(len(work)):
        pivot = next(r for r in range(col, len(work)) if work[r][col])
        if pivot != col:
            work[col], work[pivot] = work[pivot], work[col]
            sign *= -1
        q = work[col][col]
        value *= q
        for r in range(col + 1, len(work)):
            if work[r][col]:
                t = work[r][col] / q
                work[r] = [x - t * y for x, y in zip(work[r], work[col])]
    assert value.denominator == 1
    return sign * value.numerator


def smith_diagonal(matrix: list[list[int]]) -> list[int]:
    """Exact Euclidean Smith reduction used by the producer path."""
    a = [row[:] for row in matrix]
    m, n = len(a), len(a[0])
    out: list[int] = []
    k = 0
    while k < m and k < n:
        choices = [(abs(a[i][j]), i, j) for i in range(k, m)
                   for j in range(k, n) if a[i][j]]
        if not choices:
            break
        _, i, j = min(choices)
        a[k], a[i] = a[i], a[k]
        for row in a:
            row[k], row[j] = row[j], row[k]
        while True:
            changed = False
            for i in range(k + 1, m):
                if a[i][k]:
                    q = a[i][k] // a[k][k]
                    a[i] = [x - q * y for x, y in zip(a[i], a[k])]
                    if a[i][k] and abs(a[i][k]) < abs(a[k][k]):
                        a[k], a[i] = a[i], a[k]
                    changed = True
                    break
            if changed:
                continue
            for j in range(k + 1, n):
                if a[k][j]:
                    q = a[k][j] // a[k][k]
                    for i in range(m):
                        a[i][j] -= q * a[i][k]
                    if a[k][j] and abs(a[k][j]) < abs(a[k][k]):
                        for row in a:
                            row[k], row[j] = row[j], row[k]
                    changed = True
                    break
            if changed:
                continue
            bad = next(((i, j) for i in range(k + 1, m)
                        for j in range(k + 1, n) if a[i][j] % a[k][k]), None)
            if bad is not None:
                i, _ = bad
                a[k] = [x + y for x, y in zip(a[k], a[i])]
                continue
            break
        if a[k][k] < 0:
            a[k] = [-x for x in a[k]]
        out.append(a[k][k])
        k += 1
    return out


def main() -> None:
    paths = {
        "c64": C64 / "results/c64_mark_evidence.json",
        "c64_manifest": C64 / "C64_PREFREEZE_MANIFEST.json",
        "c65": C65 / "results/c65_defect_evidence.json",
        "c65_manifest": C65 / "C65_PREFREEZE_MANIFEST.json",
        "c66": C66 / "results/c66_mark_snf_evidence.json",
        "c66_manifest": C66 / "C66_PREFREEZE_MANIFEST.json",
        "c68": C68 / "results/c68_defect_duality_evidence.json",
        "c68_manifest": C68 / "C68_PREFREEZE_MANIFEST.json",
    }
    raw = {name: path.read_bytes() for name, path in paths.items()}
    assert {name: digest(value) for name, value in raw.items()} == HASHES
    c64, c65, c66, c68 = (json.loads(raw[name]) for name in ("c64", "c65", "c66", "c68"))
    for doc in (c64, c65, c66, c68):
        assert doc["status"] == "PREFREEZE_G3_PASS"
        assert doc["scope_literal"] == FIREWALL
    assert c64["matrix_sha256"] == MATRIX_HASH
    assert c68["D_invariants"] == [2, 2, 8]
    assert c68["D_order"] == 32
    assert c68["quotient_smith_invariants"] == EXPECTED_SNF

    M = c64["mark_matrix"]
    u = [c65["all_saturation_basis"][f"u{i}"] for i in (1, 2, 3)]
    U = [[u[j][i] for j in range(3)] for i in range(16)]
    moduli = [8, 2, 2]
    R = [[0] * 16 for _ in range(3)]
    R[0][9] = 1
    R[1][2] = 1
    R[2][0] = 1
    R[2][14] = 1
    RM = multiply(R, M)
    RU = multiply(R, U)
    RM_residues = [[RM[i][j] % moduli[i] for j in range(16)] for i in range(3)]
    RU_residues = [[RU[i][j] % moduli[i] for j in range(3)] for i in range(3)]
    assert RM_residues == [[0] * 16 for _ in range(3)]
    assert RU_residues == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    B = [[int(i == j) for j in range(16)] for i in range(16)]
    B[14][0] = -1
    B[2][2] = 2
    B[9][9] = 8
    B[14][14] = 2
    assert determinant(B) == 32
    RB = multiply(R, B)
    assert all(RB[i][j] % moduli[i] == 0 for i in range(3) for j in range(16))
    Binv = inverse(B)
    Nq = [[sum(Binv[i][k] * M[k][j] for k in range(16))
           for j in range(16)] for i in range(16)]
    assert all(x.denominator == 1 for row in Nq for x in row)
    N = [[int(x) for x in row] for row in Nq]
    assert multiply(B, N) == M
    complement_snf = smith_diagonal(N)
    assert complement_snf == EXPECTED_SNF
    complement_order = 1
    for value in complement_snf:
        complement_order *= value
    assert complement_order == c68["quotient_order"] == 7077888
    assert complement_order * 32 == abs(determinant(M)) == c66["mark_determinant"]
    quotient_2_primary_orders = [2] * 8 + [4] * 3 + [16]
    target_2_exponents = [3, 1, 1]
    hom_exponents = [sum(min((order.bit_length() - 1), exponent)
                         for order in quotient_2_primary_orders)
                     for exponent in target_2_exponents]
    assert hom_exponents == [17, 12, 12]
    row_solution_counts = [2 ** exponent for exponent in hom_exponents]
    retraction_count = 1
    for count in row_solution_counts:
        retraction_count *= count
    assert retraction_count == 2 ** 41 == 2199023255552

    result: dict[str, Any] = {
        "schema_id": "hcs-c69-defect-splitting-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "authority": {**HASHES, "c64_matrix_sha256": MATRIX_HASH},
        "type_order": [f"S{i}" for i in range(1, 17)],
        "moduli": moduli,
        "retraction_formula": ["x10 mod 8", "x3 mod 2", "x1+x15 mod 2"],
        "retraction_matrix": R,
        "retraction_matrix_sha256": matrix_hash(R),
        "RM_residues": RM_residues,
        "RU_integer": RU,
        "RU_residues": RU_residues,
        "complement_congruences": ["x10=0 mod 8", "x3=0 mod 2", "x1+x15=0 mod 2"],
        "complement_basis": B,
        "complement_basis_sha256": matrix_hash(B),
        "complement_lattice_index": abs(determinant(B)),
        "complement_presentation": N,
        "complement_presentation_sha256": matrix_hash(N),
        "presentation_identity": "B*N=M",
        "complement_smith_invariants": complement_snf,
        "complement_order": complement_order,
        "defect_invariants": [2, 2, 8],
        "defect_order": 32,
        "ambient_order": abs(determinant(M)),
        "direct_product_order_check": complement_order * 32,
        "quotient_2_primary_orders": quotient_2_primary_orders,
        "hom_exponents_by_target": hom_exponents,
        "retraction_row_solution_counts": row_solution_counts,
        "retraction_count": retraction_count,
        "complement_count": retraction_count,
        "claims": {
            "actual_c68_embedding_splits": True,
            "all_complements_counted": True,
            "complement_canonical_claimed": False,
            "canonical_smith_basis_claimed": False,
            "full_burnside_ring_claimed": False,
            "arithmetic_local_claimed": False,
        },
    }
    OUT.write_bytes(canonical(result))
    print(json.dumps({"status": result["status"],
                      "retraction_matrix_sha256": result["retraction_matrix_sha256"],
                      "complement_lattice_index": result["complement_lattice_index"],
                      "complement_smith_invariants": complement_snf,
                      "complement_order": complement_order,
                      "complement_count": retraction_count}, sort_keys=True))


if __name__ == "__main__":
    main()
