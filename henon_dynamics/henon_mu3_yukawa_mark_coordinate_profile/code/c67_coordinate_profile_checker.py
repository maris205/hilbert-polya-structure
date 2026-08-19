#!/usr/bin/env python3
"""Independent checker for the C67 coordinate-profile certificate."""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c67_coordinate_profile_evidence.json"
C64 = ROOT / "henon_dynamics/henon_mu3_yukawa_burnside_marks/results/c64_mark_evidence.json"
C64M = ROOT / "henon_dynamics/henon_mu3_yukawa_burnside_marks/C64_PREFREEZE_MANIFEST.json"
C66 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_cokernel/results/c66_mark_snf_evidence.json"
C66M = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_cokernel/C66_PREFREEZE_MANIFEST.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
H64 = "7c4673e46f2b97ac03d4e331c762a47286058c36ea243fb20fc39543dd699212"
H64M = "eb1d6a55cb81ccfc9b3041879cb913367a514f5c4cba50872d8b286c0ac095b6"
H66 = "ce74edeec04b245637e5b12165a7fcdeb42475b0dead7373b1bcf3e37f22beb1"
H66M = "aa9a750fd87cfd09948167e0af93145823dff7d34c7bdb1ed13d1a8df493c626"
HM = "4e57d980e774e14709d60feac0fff5af831b6496409d248f398a8a3e2796c307"


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def inverse(matrix: list[list[int]]) -> list[list[Fraction]]:
    """Fraction-free-style elimination with last-nonzero pivot selection."""
    n = len(matrix)
    a = [
        [Fraction(x) for x in row]
        + [Fraction(int(i == j)) for j in range(n)]
        for i, row in enumerate(matrix)
    ]
    for col in range(n):
        pivot = next((r for r in range(n - 1, col - 1, -1) if a[r][col]), None)
        if pivot is None:
            raise AssertionError("singular matrix")
        a[col], a[pivot] = a[pivot], a[col]
        pivot_value = a[col][col]
        for row in range(col, n * 2):
            a[col][row] /= pivot_value
        for row in range(n):
            if row == col:
                continue
            factor = a[row][col]
            if factor:
                for entry in range(col, n * 2):
                    a[row][entry] -= factor * a[col][entry]
    return [row[n:] for row in a]


def lcm(a: int, b: int) -> int:
    return abs(a * b) // gcd(a, b) if a and b else 0


def order(values: list[Fraction]) -> int:
    result = 1
    for value in values:
        result = lcm(result, value.denominator)
    return result


def identity(left: list[list[int]], right: list[list[Fraction]]) -> bool:
    n = len(left)
    return all(
        sum(Fraction(left[i][k]) * right[k][j] for k in range(n))
        == (1 if i == j else 0)
        for i in range(n)
        for j in range(n)
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=EVIDENCE)
    args = parser.parse_args()
    raw = args.evidence.read_bytes()
    doc = json.loads(raw)
    assert raw == canonical(doc)
    assert doc["schema_id"] == "hcs-c67-coordinate-profile-prefreeze-v1"
    assert doc["status"] == "PREFREEZE_G3_PASS"
    assert doc["scope_literal"] == FIREWALL
    assert doc["claims"] == {
        "arithmetic_local_claimed": False,
        "canonical_smith_basis_claimed": False,
        "full_burnside_ring_claimed": False,
        "restricted_16_type_coordinate_profile_only": True,
    }

    raw64, raw64m = C64.read_bytes(), C64M.read_bytes()
    raw66, raw66m = C66.read_bytes(), C66M.read_bytes()
    assert digest(raw64) == H64 and digest(raw64m) == H64M
    assert digest(raw66) == H66 and digest(raw66m) == H66M
    c64, c66 = json.loads(raw64), json.loads(raw66)
    assert c64["schema_id"] == "hcs-c64-table-of-marks-prefreeze-v1"
    assert c64["status"] == "PREFREEZE_G3_PASS"
    assert c64["scope_literal"] == FIREWALL
    assert c64["matrix_sha256"] == HM
    assert c66["schema_id"] == "hcs-c66-mark-snf-prefreeze-v1"
    assert c66["status"] == "PREFREEZE_G3_PASS"
    assert c66["scope_literal"] == FIREWALL
    assert doc["authority"] == {
        "c64": H64,
        "c64_manifest": H64M,
        "c64_matrix_sha256": HM,
        "c66": H66,
        "c66_manifest": H66M,
    }
    assert doc["type_order"] == [f"S{i}" for i in range(1, 17)]

    matrix = c64["mark_matrix"]
    assert len(matrix) == 16 and all(len(row) == 16 for row in matrix)
    inv = inverse(matrix)
    transposed = [list(row) for row in zip(*matrix)]
    inv_t = inverse(transposed)
    assert identity(matrix, inv)
    assert identity(transposed, inv_t)
    columns = [order([inv[i][j] for i in range(16)]) for j in range(16)]
    rows = [order(inv[i]) for i in range(16)]
    denominator = 1
    for row in inv:
        for value in row:
            denominator = lcm(denominator, value.denominator)
    denominator_t = 1
    for row in inv_t:
        for value in row:
            denominator_t = lcm(denominator_t, value.denominator)
    nonzero = sum(value != 0 for row in inv for value in row)
    assert columns == doc["coordinate_orders"] == [36, 12, 6, 6, 2, 2, 36, 6, 16, 8, 6, 12, 2, 2, 36, 36]
    assert rows == doc["dual_coordinate_orders"] == [1, 4, 2, 2, 2, 2, 36, 6, 16, 8, 2, 4, 2, 2, 2, 2]
    assert denominator == denominator_t == 144
    assert doc["coordinate_lcm"] == doc["dual_coordinate_lcm"] == 144
    assert doc["global_inverse_denominator"] == doc["dual_global_inverse_denominator"] == 144
    assert doc["inverse_nonzero_count"] == nonzero == 43
    assert doc["mark_shape"] == [16, 16]
    assert doc["mark_determinant"] == 226492416 == c66["mark_determinant"]
    assert doc["c66_compatibility"] == {
        "smith_invariants": [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 24, 144],
        "cokernel": "(Z/2)^10 + (Z/4)^3 + Z/24 + Z/144",
    }
    print(
        json.dumps(
            {
                "status": "PASS",
                "coordinate_orders": columns,
                "dual_coordinate_orders": rows,
                "global_denominator": denominator,
                "inverse_nonzero_count": nonzero,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
