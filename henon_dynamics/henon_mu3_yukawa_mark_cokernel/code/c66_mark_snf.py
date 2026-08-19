#!/usr/bin/env python3
"""C66 exact Smith form of the restricted C64 table-of-marks map."""

from __future__ import annotations

import hashlib
import json
from math import gcd
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
C64 = ROOT / "henon_dynamics/henon_mu3_yukawa_burnside_marks"
C65 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_defect"
INPUT_C64 = C64 / "results/c64_mark_evidence.json"
INPUT_C64_MANIFEST = C64 / "C64_PREFREEZE_MANIFEST.json"
INPUT_C65 = C65 / "results/c65_defect_evidence.json"
OUTPUT = PROJECT / "results/c66_mark_snf_evidence.json"

FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
EXPECTED_C64 = "7c4673e46f2b97ac03d4e331c762a47286058c36ea243fb20fc39543dd699212"
EXPECTED_C64_MANIFEST = "eb1d6a55cb81ccfc9b3041879cb913367a514f5c4cba50872d8b286c0ac095b6"
EXPECTED_C65 = "ebdd80fd2292225b98248aacd6b21bafab2987bdccb801c22c10adef7e7b4e4c"
EXPECTED_C64_MATRIX = "4e57d980e774e14709d60feac0fff5af831b6496409d248f398a8a3e2796c307"


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def rank_q(matrix: list[list[int]]) -> int:
    a = [[int(x) for x in row] for row in matrix]
    if not a:
        return 0
    rows, cols = len(a), len(a[0])
    rank = 0
    for col in range(cols):
        pivot = next((r for r in range(rank, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        p = a[rank][col]
        for r in range(rank + 1, rows):
            if not a[r][col]:
                continue
            q, rem = divmod(a[r][col], p)
            for c in range(col, cols):
                a[r][c] -= q * a[rank][c]
            if abs(a[r][col]) < abs(p) and a[r][col]:
                a[rank], a[r] = a[r], a[rank]
                p = a[rank][col]
        rank += 1
    return rank


def smith_diagonal(matrix: list[list[int]]) -> list[int]:
    """Exact Smith diagonal via Euclidean row/column reduction."""
    a = [list(map(int, row)) for row in matrix]
    m, n = len(a), len(a[0]) if a else 0
    out: list[int] = []
    k = 0
    while k < m and k < n:
        candidates = [(abs(a[i][j]), i, j) for i in range(k, m) for j in range(k, n) if a[i][j]]
        if not candidates:
            break
        _, i, j = min(candidates)
        a[k], a[i] = a[i], a[k]
        for row in a:
            row[k], row[j] = row[j], row[k]

        while True:
            changed = False
            # Euclidean reduction of the pivot column and row.
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
            # The pivot row and column are zero. If the pivot does not divide
            # the remaining block, add a violating row to the pivot row and
            # repeat Euclidean reduction.
            bad = next(((i, j) for i in range(k + 1, m) for j in range(k + 1, n)
                        if a[i][j] % a[k][k]), None)
            if bad is not None:
                i, _ = bad
                a[k] = [x + y for x, y in zip(a[k], a[i])]
                changed = True
                continue
            break
        if a[k][k] < 0:
            a[k] = [-x for x in a[k]]
        out.append(a[k][k])
        k += 1
    return out


def cumulative(values: list[int]) -> list[int]:
    out: list[int] = []
    p = 1
    for x in values:
        p *= x
        out.append(p)
    return out


def primary(values: list[int], prime: int) -> list[int]:
    out = []
    for value in values:
        x = value
        p = 1
        while x % prime == 0 and x > 1:
            x //= prime
            p *= prime
        if p > 1:
            out.append(p)
    return out


def main() -> None:
    raw64 = INPUT_C64.read_bytes()
    raw64m = INPUT_C64_MANIFEST.read_bytes()
    raw65 = INPUT_C65.read_bytes()
    hashes = {"c64": sha(raw64), "c64_manifest": sha(raw64m), "c65": sha(raw65)}
    assert hashes == {"c64": EXPECTED_C64, "c64_manifest": EXPECTED_C64_MANIFEST, "c65": EXPECTED_C65}
    c64 = json.loads(raw64)
    c64m = json.loads(raw64m)
    c65 = json.loads(raw65)
    assert c64["schema_id"] == "hcs-c64-table-of-marks-prefreeze-v1"
    assert c64["status"] == "PREFREEZE_G3_PASS"
    assert c64["scope_literal"] == FIREWALL
    assert c64m["scope_literal"] == FIREWALL
    assert c65["schema_id"] == "hcs-c65-mark-saturation-prefreeze-v1"
    assert c65["status"] == "PREFREEZE_G3_PASS"
    assert c65["scope_literal"] == FIREWALL
    assert c64["matrix_sha256"] == EXPECTED_C64_MATRIX
    assert c64["claims"]["full_burnside_ring_claimed"] is False
    assert c64["claims"]["arithmetic_local_claimed"] is False

    mark = c64["mark_matrix"]
    assert len(mark) == 16 and all(len(row) == 16 for row in mark)
    assert rank_q(mark) == 16
    diagonal = smith_diagonal(mark)
    assert diagonal == [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 24, 144]
    divisors = cumulative(diagonal)
    assert divisors[-1] == c64["determinant"] == 226492416
    assert primary(diagonal, 2) == [2] * 10 + [4] * 3 + [8, 16]
    assert primary(diagonal, 3) == [3, 9]
    assert c65["old_snf"] == [2, 8] and c65["all_snf"] == [2, 2, 8]
    assert c65["relative_jump"]["quotient_index"] == 2

    result: dict[str, Any] = {
        "schema_id": "hcs-c66-mark-snf-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "authority": {**hashes, "c64_matrix_sha256": c64["matrix_sha256"]},
        "type_order": [f"S{i}" for i in range(1, 17)],
        "mark_shape": [16, 16],
        "mark_rank": rank_q(mark),
        "mark_determinant": c64["determinant"],
        "smith_invariants": diagonal,
        "determinantal_divisors": divisors,
        "primary_invariants": {"2": primary(diagonal, 2), "3": primary(diagonal, 3)},
        "cokernel_decomposition": {
            "invariant_factor_form": "(Z/2)^10 + (Z/4)^3 + Z/24 + Z/144",
            "2_primary": "(Z/2)^10 + (Z/4)^3 + Z/8 + Z/16",
            "3_primary": "Z/3 + Z/9",
        },
        "c65_compatibility": {"old_snf": c65["old_snf"], "all_snf": c65["all_snf"], "relative_quotient": "Z/2"},
        "claims": {
            "restricted_16_type_mark_cokernel_only": True,
            "full_burnside_ring_claimed": False,
            "arithmetic_local_claimed": False,
        },
    }
    OUTPUT.write_bytes(canonical(result))
    print(json.dumps({"status": result["status"], "smith_invariants": diagonal,
                      "determinant": divisors[-1], "primary_2": primary(diagonal, 2),
                      "primary_3": primary(diagonal, 3)}, sort_keys=True))


if __name__ == "__main__":
    main()
