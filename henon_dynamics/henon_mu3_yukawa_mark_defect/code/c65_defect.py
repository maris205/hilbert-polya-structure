#!/usr/bin/env python3
"""Produce the exact integral mark-saturation certificate for HCS-C65."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
import hashlib
import json
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
C63 = ROOT / "henon_dynamics/henon_mu3_yukawa_burnside_kernel_rank"
C64 = ROOT / "henon_dynamics/henon_mu3_yukawa_burnside_marks"
INPUT_C63 = C63 / "results/c63_kernel_evidence.json"
INPUT_C64 = C64 / "results/c64_mark_evidence.json"
INPUT_C64_MANIFEST = C64 / "C64_PREFREEZE_MANIFEST.json"
OUTPUT = PROJECT / "results/c65_defect_evidence.json"

FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
EXPECTED_C63 = "38f439cfe6ed71616a7c74d68bd07da73f5680566ae16f8c557ab2b5d1d16e26"
EXPECTED_C64 = "7c4673e46f2b97ac03d4e331c762a47286058c36ea243fb20fc39543dd699212"
EXPECTED_C64_MANIFEST = "eb1d6a55cb81ccfc9b3041879cb913367a514f5c4cba50872d8b286c0ac095b6"


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def rank_q(matrix: list[list[int]]) -> int:
    a = [[Fraction(x) for x in row] for row in matrix]
    if not a:
        return 0
    rows, cols = len(a), len(a[0])
    pivot = 0
    for col in range(cols):
        row = next((r for r in range(pivot, rows) if a[r][col]), None)
        if row is None:
            continue
        a[pivot], a[row] = a[row], a[pivot]
        q = a[pivot][col]
        a[pivot] = [x / q for x in a[pivot]]
        for r in range(rows):
            if r != pivot and a[r][col]:
                q = a[r][col]
                a[r] = [x - q * y for x, y in zip(a[r], a[pivot])]
        pivot += 1
    return pivot


def det_small(a: list[list[int]]) -> int:
    n = len(a)
    if n == 0:
        return 1
    if n == 1:
        return a[0][0]
    if n == 2:
        return a[0][0] * a[1][1] - a[0][1] * a[1][0]
    if n == 3:
        return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
                - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
                + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))
    # Bareiss for the optional full-rank small minors.
    b = [row[:] for row in a]
    previous = 1
    sign = 1
    for k in range(n - 1):
        p = next((r for r in range(k, n) if b[r][k]), None)
        if p is None:
            return 0
        if p != k:
            b[k], b[p] = b[p], b[k]
            sign *= -1
        pivot = b[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                b[i][j] = (b[i][j] * pivot - b[i][k] * b[k][j]) // previous
        for i in range(k + 1, n):
            b[i][k] = 0
        previous = pivot
    return sign * b[-1][-1]


def determinantal_divisor(matrix: list[list[int]], rank: int) -> int:
    """GCD of all rank-by-rank minors; this is the lattice index in saturation."""
    if rank == 0:
        return 1
    rows = len(matrix)
    cols = len(matrix[0])
    value = 0
    for row_ids in combinations(range(rows), rank):
        sub = [[matrix[i][j] for j in range(cols)] for i in row_ids]
        for col_ids in combinations(range(cols), rank):
            minor = [[sub[i][j] for j in col_ids] for i in range(rank)]
            value = gcd(value, abs(det_small(minor)))
            if value == 1:
                return 1
    return value


def matrix_vector(matrix: list[list[int]], vector: list[int]) -> list[int]:
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]


def gcd_entries(vector: list[int]) -> int:
    value = 0
    for x in vector:
        value = gcd(value, abs(x))
    return value


def divide(vector: list[int], factor: int) -> list[int]:
    assert factor > 0 and all(x % factor == 0 for x in vector)
    return [x // factor for x in vector]


def snf_invariants(matrix: list[list[int]]) -> tuple[list[int], list[int]]:
    rank = rank_q(matrix)
    divisors = [determinantal_divisor(matrix, k) for k in range(1, rank + 1)]
    inv = []
    previous = 1
    for d in divisors:
        assert d % previous == 0
        inv.append(d // previous)
        previous = d
    return inv, divisors


def main() -> None:
    raw63 = INPUT_C63.read_bytes()
    raw64 = INPUT_C64.read_bytes()
    raw64m = INPUT_C64_MANIFEST.read_bytes()
    hashes = {"c63": sha(raw63), "c64": sha(raw64), "c64_manifest": sha(raw64m)}
    assert hashes == {"c63": EXPECTED_C63, "c64": EXPECTED_C64, "c64_manifest": EXPECTED_C64_MANIFEST}
    c63 = json.loads(raw63)
    c64 = json.loads(raw64)
    assert c63["schema_id"] == "hcs-c63-burnside-kernel-prefreeze-v1"
    assert c64["schema_id"] == "hcs-c64-table-of-marks-prefreeze-v1"
    assert c63["scope_literal"] == c64["scope_literal"] == FIREWALL
    assert c64["status"] == "PREFREEZE_G3_PASS"

    character = c63["character_matrix"]
    mark = c64["mark_matrix"]
    assert len(character) == 25 and all(len(row) == 16 for row in character)
    assert len(mark) == 16 and all(len(row) == 16 for row in mark)
    assert rank_q(character) == 13 and rank_q(mark) == 16

    types = [f"S{i}" for i in range(1, 17)]
    expected = {
        "z1": [0,0,0,0,0,0,0,0,-1,1,0,0,0,0,0,0],
        "z2": [0,-1,-1,0,-1,-1,0,0,0,0,1,1,1,1,0,0],
        "z3": [0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,1],
    }
    assert c63["nullspace_basis"] == expected
    assert all(matrix_vector(character, expected[name]) == [0] * 25 for name in types[:0] or expected)
    assert rank_q([expected["z1"], expected["z2"], expected["z3"]]) == 3
    # A gcd-one maximal minor certifies that the displayed integer kernel basis
    # is saturated in Z^16, not merely a rational basis.
    kernel_rows = [[expected[name][j] for name in ("z1", "z2", "z3")] for j in range(16)]
    kernel_minor_gcd = determinantal_divisor(kernel_rows, 3)
    assert kernel_minor_gcd == 1

    z1, z2, z3 = (expected[name] for name in ("z1", "z2", "z3"))
    v1, v2, v3 = (matrix_vector(mark, v) for v in (z1, z2, z3))
    old = [[v1[i], v3[i]] for i in range(16)]
    all_kernel = [[v1[i], v2[i], v3[i]] for i in range(16)]
    old_snf, old_divisors = snf_invariants(old)
    all_snf, all_divisors = snf_invariants(all_kernel)
    assert old_snf == [2, 8] and old_divisors == [2, 16]
    assert all_snf == [2, 2, 8] and all_divisors == [2, 4, 32]

    u1, u2, u3 = divide(v1, 8), divide(v2, 2), divide(v3, 2)
    old_sat = [[u1[i], u3[i]] for i in range(16)]
    all_sat = [[u1[i], u2[i], u3[i]] for i in range(16)]
    assert determinantal_divisor(old_sat, 2) == 1
    assert determinantal_divisor(all_sat, 3) == 1
    assert gcd_entries(v1) == 8 and gcd_entries(v2) == 2 and gcd_entries(v3) == 2
    r4 = [0,1,1,0,1,1,0,0,0,0,-1,-1,-1,-1,0,0]
    vr4 = matrix_vector(mark, r4)
    assert vr4 == [-x for x in v2]
    assert divide(vr4, 2) == [-x for x in u2]

    result = {
        "schema_id": "hcs-c65-mark-saturation-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "authority": {**hashes, "c63_matrix_sha256": c63["matrix_sha256"], "c64_matrix_sha256": c64["matrix_sha256"]},
        "type_order": types,
        "character_rank": rank_q(character),
        "kernel_basis": expected,
        "kernel_basis_minor_gcd": kernel_minor_gcd,
        "mark_matrix_rank": rank_q(mark),
        "mark_matrix_determinant": c64["determinant"],
        "old_kernel_names": ["z1", "z3"],
        "all_kernel_names": ["z1", "z2", "z3"],
        "mark_vectors": {"z1": v1, "z2": v2, "z3": v3, "r4": vr4},
        "old_snf": old_snf,
        "old_determinantal_divisors": old_divisors,
        "all_snf": all_snf,
        "all_determinantal_divisors": all_divisors,
        "old_saturation_basis": {"u1": u1, "u3": u3},
        "all_saturation_basis": {"u1": u1, "u2": u2, "u3": u3},
        "old_saturation_minor_gcd": 1,
        "all_saturation_minor_gcd": 1,
        "mark_contents": {"z1": gcd_entries(v1), "z2": gcd_entries(v2), "z3": gcd_entries(v3), "r4": gcd_entries(vr4)},
        "relative_jump": {
            "old_index": 16,
            "all_index": 32,
            "quotient_index": 2,
            "generator": "u2=m(z2)/2=-m(R4)/2",
            "order": 2,
        },
        "claims": {
            "integer_kernel_basis_saturated": True,
            "restricted_mark_saturation_only": True,
            "full_burnside_ring_claimed": False,
            "arithmetic_local_claimed": False,
        },
    }
    OUTPUT.write_bytes(canonical(result))
    print(json.dumps({"status": result["status"], "old_snf": old_snf, "all_snf": all_snf, "old_index": 16, "all_index": 32, "relative_jump": 2}, sort_keys=True))


if __name__ == "__main__":
    main()
