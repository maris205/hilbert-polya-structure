#!/usr/bin/env python3
"""Produce the C67 coordinate-wise mark-integrality certificate."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from math import gcd
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
C64_DIR = ROOT / "henon_dynamics/henon_mu3_yukawa_burnside_marks"
C66_DIR = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_cokernel"
C64_EVIDENCE = C64_DIR / "results/c64_mark_evidence.json"
C64_MANIFEST = C64_DIR / "C64_PREFREEZE_MANIFEST.json"
C66_EVIDENCE = C66_DIR / "results/c66_mark_snf_evidence.json"
C66_MANIFEST = C66_DIR / "C66_PREFREEZE_MANIFEST.json"
OUTPUT = PROJECT / "results/c67_coordinate_profile_evidence.json"

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
    """Exact Gauss-Jordan inverse with a deterministic first-nonzero pivot."""
    n = len(matrix)
    a = [
        [Fraction(x) for x in row]
        + [Fraction(int(i == j)) for j in range(n)]
        for i, row in enumerate(matrix)
    ]
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col]), None)
        if pivot is None:
            raise ValueError("singular matrix")
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
        scale = a[col][col]
        a[col] = [x / scale for x in a[col]]
        for row in range(n):
            if row == col or not a[row][col]:
                continue
            scale = a[row][col]
            a[row] = [x - scale * y for x, y in zip(a[row], a[col])]
    return [row[n:] for row in a]


def lcm(a: int, b: int) -> int:
    return abs(a * b) // gcd(a, b) if a and b else 0


def denominator_order(values: list[Fraction]) -> int:
    value = 1
    for item in values:
        value = lcm(value, item.denominator)
    return value


def product_identity(
    left: list[list[int]], right: list[list[Fraction]]
) -> bool:
    n = len(left)
    for i in range(n):
        for j in range(n):
            value = sum(Fraction(left[i][k]) * right[k][j] for k in range(n))
            if value != (1 if i == j else 0):
                return False
    return True


def main() -> None:
    raw64 = C64_EVIDENCE.read_bytes()
    raw64m = C64_MANIFEST.read_bytes()
    raw66 = C66_EVIDENCE.read_bytes()
    raw66m = C66_MANIFEST.read_bytes()
    hashes = {
        "c64": digest(raw64),
        "c64_manifest": digest(raw64m),
        "c66": digest(raw66),
        "c66_manifest": digest(raw66m),
    }
    assert hashes == {
        "c64": H64,
        "c64_manifest": H64M,
        "c66": H66,
        "c66_manifest": H66M,
    }
    c64 = json.loads(raw64)
    c64m = json.loads(raw64m)
    c66 = json.loads(raw66)
    c66m = json.loads(raw66m)
    assert c64["schema_id"] == "hcs-c64-table-of-marks-prefreeze-v1"
    assert c64["status"] == "PREFREEZE_G3_PASS"
    assert c64["scope_literal"] == FIREWALL
    assert c64m["scope_literal"] == FIREWALL
    assert c64["matrix_sha256"] == HM
    assert c66["schema_id"] == "hcs-c66-mark-snf-prefreeze-v1"
    assert c66["status"] == "PREFREEZE_G3_PASS"
    assert c66["scope_literal"] == FIREWALL
    assert c66m["scope_literal"] == FIREWALL
    assert c66["authority"]["c64"] == H64
    assert c66["authority"]["c64_manifest"] == H64M

    mark = c64["mark_matrix"]
    assert len(mark) == 16 and all(len(row) == 16 for row in mark)
    inv = inverse(mark)
    assert product_identity(mark, inv)
    transpose = [list(row) for row in zip(*mark)]
    inv_transpose = inverse(transpose)
    assert product_identity(transpose, inv_transpose)

    coordinate_orders = [
        denominator_order([inv[i][j] for i in range(16)]) for j in range(16)
    ]
    dual_orders = [denominator_order(inv[i]) for i in range(16)]
    global_denominator = 1
    for row in inv:
        for value in row:
            global_denominator = lcm(global_denominator, value.denominator)
    dual_global_denominator = 1
    for row in inv_transpose:
        for value in row:
            dual_global_denominator = lcm(
                dual_global_denominator, value.denominator
            )
    nonzero = sum(value != 0 for row in inv for value in row)
    assert coordinate_orders == [36, 12, 6, 6, 2, 2, 36, 6, 16, 8, 6, 12, 2, 2, 36, 36]
    assert dual_orders == [1, 4, 2, 2, 2, 2, 36, 6, 16, 8, 2, 4, 2, 2, 2, 2]
    assert global_denominator == dual_global_denominator == 144
    assert nonzero == 43
    assert c66["smith_invariants"] == [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 24, 144]
    assert c66["mark_determinant"] == 226492416

    result: dict[str, Any] = {
        "schema_id": "hcs-c67-coordinate-profile-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "authority": {**hashes, "c64_matrix_sha256": HM},
        "type_order": [f"S{i}" for i in range(1, 17)],
        "mark_shape": [16, 16],
        "mark_determinant": 226492416,
        "coordinate_orders": coordinate_orders,
        "dual_coordinate_orders": dual_orders,
        "coordinate_lcm": 144,
        "dual_coordinate_lcm": 144,
        "global_inverse_denominator": 144,
        "dual_global_inverse_denominator": 144,
        "inverse_nonzero_count": nonzero,
        "c66_compatibility": {
            "smith_invariants": c66["smith_invariants"],
            "cokernel": c66["cokernel_decomposition"]["invariant_factor_form"],
        },
        "claims": {
            "restricted_16_type_coordinate_profile_only": True,
            "canonical_smith_basis_claimed": False,
            "full_burnside_ring_claimed": False,
            "arithmetic_local_claimed": False,
        },
    }
    OUTPUT.write_bytes(canonical(result))
    print(
        json.dumps(
            {
                "status": result["status"],
                "coordinate_orders": coordinate_orders,
                "dual_coordinate_orders": dual_orders,
                "global_denominator": global_denominator,
                "inverse_nonzero_count": nonzero,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
