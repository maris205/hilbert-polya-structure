#!/usr/bin/env python3
"""Produce the exact C68 defect--cokernel duality certificate."""

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
C67 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_coordinate_profile"
OUT = PROJECT / "results/c68_defect_duality_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
H64 = "7c4673e46f2b97ac03d4e331c762a47286058c36ea243fb20fc39543dd699212"
H64M = "eb1d6a55cb81ccfc9b3041879cb913367a514f5c4cba50872d8b286c0ac095b6"
H65 = "ebdd80fd2292225b98248aacd6b21bafab2987bdccb801c22c10adef7e7b4e4c"
H65M = "f8709e490d0c077c6498ce96617d6711b58790d245e93e20124aa43b3dadc913"
H66 = "ce74edeec04b245637e5b12165a7fcdeb42475b0dead7373b1bcf3e37f22beb1"
H66M = "aa9a750fd87cfd09948167e0af93145823dff7d34c7bdb1ed13d1a8df493c626"
H67 = "357cd372b2341a36e483adcf771512d08d5207f71796550b6759c25813d3badd"
H67M = "473cf1172f13bb3b61eb78c92de4026e552dd751549c4131cff904d4845a9cb8"
MATRIX_HASH = "4e57d980e774e14709d60feac0fff5af831b6496409d248f398a8a3e2796c307"


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def matvec(a: list[list[int]], x: list[int]) -> list[int]:
    return [sum(v * w for v, w in zip(row, x)) for row in a]


def transpose(a: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*a)]


def inverse(a: list[list[int]]) -> list[list[Fraction]]:
    n = len(a)
    b = [[Fraction(x) for x in row] + [Fraction(i == j) for j in range(n)]
         for i, row in enumerate(a)]
    for col in range(n):
        pivot = next(r for r in range(col, n) if b[r][col])
        b[col], b[pivot] = b[pivot], b[col]
        q = b[col][col]
        b[col] = [x / q for x in b[col]]
        for r in range(n):
            if r == col or not b[r][col]:
                continue
            q = b[r][col]
            b[r] = [x - q * y for x, y in zip(b[r], b[col])]
    return [row[n:] for row in b]


def smith_diagonal(matrix: list[list[int]]) -> list[int]:
    """Exact Euclidean Smith reduction, independent of the checker path."""
    a = [row[:] for row in matrix]
    m, n = len(a), len(a[0]) if a else 0
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
                    if abs(a[i][k]) < abs(a[k][k]) and a[i][k]:
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
                    if abs(a[k][j]) < abs(a[k][k]) and a[k][j]:
                        for row in a:
                            row[k], row[j] = row[j], row[k]
                    changed = True
                    break
            if changed:
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
        out.append(a[k][k])
        k += 1
    return out


def matrix_hash(a: list[list[int]]) -> str:
    return digest(canonical(a))


def main() -> None:
    paths = {
        "c64": C64 / "results/c64_mark_evidence.json",
        "c64_manifest": C64 / "C64_PREFREEZE_MANIFEST.json",
        "c65": C65 / "results/c65_defect_evidence.json",
        "c65_manifest": C65 / "C65_PREFREEZE_MANIFEST.json",
        "c66": C66 / "results/c66_mark_snf_evidence.json",
        "c66_manifest": C66 / "C66_PREFREEZE_MANIFEST.json",
        "c67": C67 / "results/c67_coordinate_profile_evidence.json",
        "c67_manifest": C67 / "C67_PREFREEZE_MANIFEST.json",
    }
    raw = {key: path.read_bytes() for key, path in paths.items()}
    hashes = {key: digest(value) for key, value in raw.items()}
    assert hashes == {"c64": H64, "c64_manifest": H64M, "c65": H65,
                      "c65_manifest": H65M, "c66": H66, "c66_manifest": H66M,
                      "c67": H67, "c67_manifest": H67M}
    c64, c65, c66, c67 = (json.loads(raw[key]) for key in ("c64", "c65", "c66", "c67"))
    for doc in (c64, c65, c66, c67):
        assert doc["scope_literal"] == FIREWALL
        assert doc["status"] == "PREFREEZE_G3_PASS"
    assert c64["matrix_sha256"] == MATRIX_HASH
    assert c66["smith_invariants"] == [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 24, 144]
    assert c67["coordinate_orders"] == [36, 12, 6, 6, 2, 2, 36, 6, 16, 8, 6, 12, 2, 2, 36, 36]

    M = c64["mark_matrix"]
    names = ("z1", "z2", "z3")
    z = [c65["kernel_basis"][name] for name in names]
    u = [c65["all_saturation_basis"][f"u{i}"] for i in (1, 2, 3)]
    d = [8, 2, 2]
    assert all(matvec(M, z[i]) == [d[i] * x for x in u[i]] for i in range(3))
    assert matrix_hash([[u[j][i] for j in range(3)] for i in range(16)]) == "36392b0a5f0a66ec6aeea821da362248a70ab99473c6f47617ad54d08fedfc74"

    Minv = inverse(M)
    U = [[u[j][i] for j in range(3)] for i in range(16)]
    coeff_inverse = [[sum(Minv[i][k] * U[k][j] for k in range(16))
                      for j in range(3)] for i in range(16)]
    expected_orders = d
    for j, order in enumerate(expected_orders):
        assert all((order * coeff_inverse[i][j]).denominator == 1 for i in range(16))
        assert any((n * coeff_inverse[i][j]).denominator != 1
                   for n in range(1, order) for i in range(16))
    for a1 in range(8):
        for a2 in range(2):
            for a3 in range(2):
                if (a1, a2, a3) == (0, 0, 0):
                    continue
                assert any((a1 * coeff_inverse[i][0] + a2 * coeff_inverse[i][1]
                            + a3 * coeff_inverse[i][2]).denominator != 1
                           for i in range(16))

    augmented = [M[i] + U[i] for i in range(16)]
    quotient_snf = smith_diagonal(augmented)
    expected_quotient = [1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 12, 144]
    assert quotient_snf == expected_quotient

    P = [
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,1,8,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
        [0,1,1,0,1,1,0,0,0,0,1,1,1,2,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2],
    ]
    P_inv = inverse(P)
    MT = transpose(M)
    dual_map = [[sum(P_inv[i][k] * MT[k][j] for k in range(16))
                 for j in range(16)] for i in range(16)]
    assert all(value.denominator == 1 for row in dual_map for value in row)
    dual_map_int = [[int(value) for value in row] for row in dual_map]
    dual_snf = smith_diagonal(dual_map_int)
    assert dual_snf == expected_quotient
    residues = [[z[i][j] % d[i] for i in range(3)] for j in range(16)]
    assert residues == [[0,0,0],[0,1,0],[0,1,0],[0,0,0],[0,1,0],[0,1,0],
                        [0,0,0],[0,0,0],[7,0,0],[1,0,0],[0,1,0],[0,1,0],
                        [0,1,0],[0,1,0],[0,0,1],[0,0,1]]
    assert [i + 1 for i, row in enumerate(residues) if row == [0, 0, 0]] == [1, 4, 7, 8]
    assert all(sum(z[i][k] * P[k][j] for k in range(16)) % d[i] == 0
               for i in range(3) for j in range(16))
    assert any(row == [1, 0, 0] for row in residues)
    assert any(row == [0, 1, 0] for row in residues)
    assert any(row == [0, 0, 1] for row in residues)
    assert all(sum(z[i][k] * M[k][j] for k in range(16)) % d[i] == 0
               for i in range(3) for j in range(16))

    result: dict[str, Any] = {
        "schema_id": "hcs-c68-defect-duality-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "authority": {**hashes, "c64_matrix_sha256": MATRIX_HASH},
        "type_order": [f"S{i}" for i in range(1, 17)],
        "relations": {"d": d, "Mz_equals_dU": True},
        "saturation_basis": {"u1": u[0], "u2": u[1], "u3": u[2]},
        "saturation_basis_sha256": matrix_hash(U),
        "D_invariants": [2, 2, 8],
        "D_order": 32,
        "augmented_matrix_sha256": matrix_hash(augmented),
        "quotient_smith_invariants": quotient_snf,
        "quotient_order": 7077888,
        "row_lattice_basis": P,
        "row_lattice_basis_determinant": 32,
        "row_dual_map_smith_invariants": dual_snf,
        "row_dual_quotient_order": 7077888,
        "residue_table": residues,
        "residue_table_sha256": digest(canonical(residues)),
        "annihilator_coordinate_types": [1, 4, 7, 8],
        "claims": {"restricted_defect_cokernel_duality_only": True,
                   "canonical_smith_basis_claimed": False,
                   "full_burnside_ring_claimed": False,
                   "arithmetic_local_claimed": False},
    }
    OUT.write_bytes(canonical(result))
    print(json.dumps({"status": result["status"], "D_invariants": result["D_invariants"],
                      "quotient_smith_invariants": quotient_snf,
                      "dual_smith_invariants": dual_snf,
                      "annihilator_coordinate_types": [1, 4, 7, 8]}, sort_keys=True))


if __name__ == "__main__":
    main()
