#!/usr/bin/env python3
"""Independent exact checker for the C68 defect--cokernel certificate."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c68_defect_duality_evidence.json"
C64 = ROOT / "henon_dynamics/henon_mu3_yukawa_burnside_marks/results/c64_mark_evidence.json"
C64M = ROOT / "henon_dynamics/henon_mu3_yukawa_burnside_marks/C64_PREFREEZE_MANIFEST.json"
C65 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_defect/results/c65_defect_evidence.json"
C65M = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_defect/C65_PREFREEZE_MANIFEST.json"
C66 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_cokernel/results/c66_mark_snf_evidence.json"
C66M = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_cokernel/C66_PREFREEZE_MANIFEST.json"
C67 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_coordinate_profile/results/c67_coordinate_profile_evidence.json"
C67M = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_coordinate_profile/C67_PREFREEZE_MANIFEST.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
HASHES = {
    "c64": "7c4673e46f2b97ac03d4e331c762a47286058c36ea243fb20fc39543dd699212",
    "c64_manifest": "eb1d6a55cb81ccfc9b3041879cb913367a514f5c4cba50872d8b286c0ac095b6",
    "c65": "ebdd80fd2292225b98248aacd6b21bafab2987bdccb801c22c10adef7e7b4e4c",
    "c65_manifest": "f8709e490d0c077c6498ce96617d6711b58790d245e93e20124aa43b3dadc913",
    "c66": "ce74edeec04b245637e5b12165a7fcdeb42475b0dead7373b1bcf3e37f22beb1",
    "c66_manifest": "aa9a750fd87cfd09948167e0af93145823dff7d34c7bdb1ed13d1a8df493c626",
    "c67": "357cd372b2341a36e483adcf771512d08d5207f71796550b6759c25813d3badd",
    "c67_manifest": "473cf1172f13bb3b61eb78c92de4026e552dd751549c4131cff904d4845a9cb8",
}
EXPECTED_Q = [1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 12, 144]
EXPECTED_RESIDUES = [[0,0,0],[0,1,0],[0,1,0],[0,0,0],[0,1,0],[0,1,0],
                     [0,0,0],[0,0,0],[7,0,0],[1,0,0],[0,1,0],[0,1,0],
                     [0,1,0],[0,1,0],[0,0,1],[0,0,1]]


def canon(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def matvec(a: list[list[int]], x: list[int]) -> list[int]:
    return [sum(v * w for v, w in zip(row, x)) for row in a]


def inverse(a: list[list[int]]) -> list[list[Fraction]]:
    n = len(a)
    b = [[Fraction(x) for x in row] + [Fraction(i == j) for j in range(n)]
         for i, row in enumerate(a)]
    for col in range(n):
        p = next(r for r in range(col, n) if b[r][col])
        b[col], b[p] = b[p], b[col]
        q = b[col][col]
        b[col] = [x / q for x in b[col]]
        for r in range(n):
            if r != col and b[r][col]:
                q = b[r][col]
                b[r] = [x - q * y for x, y in zip(b[r], b[col])]
    return [row[n:] for row in b]


def determinant(a0: list[list[int]]) -> int:
    a = [[Fraction(x) for x in row] for row in a0]
    out = Fraction(1)
    sign = 1
    for col in range(len(a)):
        p = next(r for r in range(col, len(a)) if a[r][col])
        if p != col:
            a[col], a[p] = a[p], a[col]
            sign *= -1
        pivot = a[col][col]
        out *= pivot
        for r in range(col + 1, len(a)):
            if not a[r][col]:
                continue
            q = a[r][col] / pivot
            a[r] = [x - q * y for x, y in zip(a[r], a[col])]
    assert out.denominator == 1
    return sign * out.numerator


def smith(a0: list[list[int]]) -> list[int]:
    """Independent pivot/remainder Smith reduction."""
    a = [row[:] for row in a0]
    m, n = len(a), len(a[0])
    result = []
    k = 0
    while k < m and k < n:
        nonzero = [(abs(a[i][j]), i, j) for i in range(k, m)
                   for j in range(k, n) if a[i][j]]
        if not nonzero:
            break
        _, i, j = min(nonzero)
        a[k], a[i] = a[i], a[k]
        for row in a:
            row[k], row[j] = row[j], row[k]
        while True:
            moved = False
            for i in range(k + 1, m):
                if a[i][k]:
                    q = a[i][k] // a[k][k]
                    a[i] = [x - q * y for x, y in zip(a[i], a[k])]
                    if a[i][k] and abs(a[i][k]) < abs(a[k][k]):
                        a[k], a[i] = a[i], a[k]
                    moved = True
                    break
            if moved:
                continue
            for j in range(k + 1, n):
                if a[k][j]:
                    q = a[k][j] // a[k][k]
                    for i in range(m):
                        a[i][j] -= q * a[i][k]
                    if a[k][j] and abs(a[k][j]) < abs(a[k][k]):
                        for row in a:
                            row[k], row[j] = row[j], row[k]
                    moved = True
                    break
            if moved:
                continue
            bad = next(((i, j) for i in range(k + 1, m)
                        for j in range(k + 1, n)
                        if a[i][j] % a[k][k]), None)
            if bad is not None:
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
    assert doc["schema_id"] == "hcs-c68-defect-duality-prefreeze-v1"
    assert doc["status"] == "PREFREEZE_G3_PASS"
    assert doc["scope_literal"] == FIREWALL
    assert doc["type_order"] == [f"S{i}" for i in range(1, 17)]
    assert doc["claims"] == {
        "arithmetic_local_claimed": False,
        "canonical_smith_basis_claimed": False,
        "full_burnside_ring_claimed": False,
        "restricted_defect_cokernel_duality_only": True,
    }
    source_paths = {"c64": C64, "c64_manifest": C64M, "c65": C65,
                    "c65_manifest": C65M, "c66": C66, "c66_manifest": C66M,
                    "c67": C67, "c67_manifest": C67M}
    assert {key: digest(path.read_bytes()) for key, path in source_paths.items()} == HASHES
    c64, c65, c66, c67 = [json.loads(path.read_text()) for path in
                           (C64, C65, C66, C67)]
    for src in (c64, c65, c66, c67):
        assert src["status"] == "PREFREEZE_G3_PASS"
        assert src["scope_literal"] == FIREWALL
    assert doc["authority"] == {**HASHES, "c64_matrix_sha256": c64["matrix_sha256"]}
    assert c64["matrix_sha256"] == "4e57d980e774e14709d60feac0fff5af831b6496409d248f398a8a3e2796c307"
    assert c66["smith_invariants"] == [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 24, 144]
    assert c67["global_inverse_denominator"] == 144

    M = c64["mark_matrix"]
    z = [c65["kernel_basis"][f"z{i}"] for i in (1, 2, 3)]
    u = [c65["all_saturation_basis"][f"u{i}"] for i in (1, 2, 3)]
    d = [8, 2, 2]
    assert all(matvec(M, z[i]) == [d[i] * x for x in u[i]] for i in range(3))
    U = [[u[j][i] for j in range(3)] for i in range(16)]
    assert doc["saturation_basis"] == {f"u{i}": u[i - 1] for i in (1, 2, 3)}
    assert doc["relations"] == {"d": d, "Mz_equals_dU": True}
    assert doc["saturation_basis_sha256"] == digest(canon(U)) == "36392b0a5f0a66ec6aeea821da362248a70ab99473c6f47617ad54d08fedfc74"
    assert doc["D_invariants"] == [2, 2, 8] and doc["D_order"] == 32
    Minv = inverse(M)
    coeff = [[sum(Minv[i][k] * U[k][j] for k in range(16))
              for j in range(3)] for i in range(16)]
    for j, order in enumerate(d):
        assert all((order * coeff[i][j]).denominator == 1 for i in range(16))
        assert any((n * coeff[i][j]).denominator != 1
                   for n in range(1, order) for i in range(16))
    for a1 in range(8):
        for a2 in range(2):
            for a3 in range(2):
                if (a1, a2, a3) == (0, 0, 0):
                    continue
                assert any((a1 * coeff[i][0] + a2 * coeff[i][1]
                            + a3 * coeff[i][2]).denominator != 1
                           for i in range(16))
    assert doc["quotient_smith_invariants"] == EXPECTED_Q
    assert doc["quotient_order"] == 7077888
    augmented = [M[i] + U[i] for i in range(16)]
    assert smith(augmented) == EXPECTED_Q
    assert doc["augmented_matrix_sha256"] == digest(canon(augmented))

    P = doc["row_lattice_basis"]
    assert len(P) == 16 and all(len(row) == 16 for row in P)
    assert doc["row_lattice_basis_determinant"] == 32
    expected_P = [[int(i == j) for j in range(16)] for i in range(16)]
    expected_P[9][8], expected_P[9][9] = 1, 8
    for j in (1, 2, 4, 5, 10, 11, 12):
        expected_P[13][j] = 1
    expected_P[13][13] = 2
    expected_P[15][14], expected_P[15][15] = 1, 2
    assert P == expected_P
    assert determinant(P) == 32
    assert all(sum(z[i][k] * P[k][j] for k in range(16)) % d[i] == 0
               for i in range(3) for j in range(16))
    assert any(row == [1, 0, 0] for row in EXPECTED_RESIDUES)
    assert any(row == [0, 1, 0] for row in EXPECTED_RESIDUES)
    assert any(row == [0, 0, 1] for row in EXPECTED_RESIDUES)
    Pinv = inverse(P)
    MT = [list(row) for row in zip(*M)]
    dual = [[sum(Pinv[i][k] * MT[k][j] for k in range(16))
             for j in range(16)] for i in range(16)]
    assert all(x.denominator == 1 for row in dual for x in row)
    dual_int = [[int(x) for x in row] for row in dual]
    assert smith(dual_int) == EXPECTED_Q
    assert doc["row_dual_map_smith_invariants"] == EXPECTED_Q
    assert doc["row_dual_quotient_order"] == 7077888
    assert doc["residue_table"] == EXPECTED_RESIDUES
    assert doc["residue_table_sha256"] == digest(canon(EXPECTED_RESIDUES))
    assert doc["annihilator_coordinate_types"] == [1, 4, 7, 8]
    assert all(sum(z[i][k] * M[k][j] for k in range(16)) % d[i] == 0
               for i in range(3) for j in range(16))
    print(json.dumps({"status": "PASS", "D_invariants": [2, 2, 8],
                      "quotient_smith_invariants": EXPECTED_Q,
                      "dual_smith_invariants": EXPECTED_Q,
                      "annihilator_coordinate_types": [1, 4, 7, 8]}, sort_keys=True))


if __name__ == "__main__":
    main()
