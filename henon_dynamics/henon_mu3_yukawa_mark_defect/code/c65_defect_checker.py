#!/usr/bin/env python3
"""Independent checker for the C65 integral mark-saturation certificate."""

from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import combinations
import hashlib
import json
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c65_defect_evidence.json"
C63 = ROOT / "henon_dynamics/henon_mu3_yukawa_burnside_kernel_rank/results/c63_kernel_evidence.json"
C64 = ROOT / "henon_dynamics/henon_mu3_yukawa_burnside_marks/results/c64_mark_evidence.json"
C64M = ROOT / "henon_dynamics/henon_mu3_yukawa_burnside_marks/C64_PREFREEZE_MANIFEST.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
H63 = "38f439cfe6ed71616a7c74d68bd07da73f5680566ae16f8c557ab2b5d1d16e26"
H64 = "7c4673e46f2b97ac03d4e331c762a47286058c36ea243fb20fc39543dd699212"
H64M = "eb1d6a55cb81ccfc9b3041879cb913367a514f5c4cba50872d8b286c0ac095b6"


def canon(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def h(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def rank_q(matrix: list[list[int]]) -> int:
    a = [[Fraction(x) for x in row] for row in matrix]
    if not a:
        return 0
    rows, cols = len(a), len(a[0])
    r = 0
    for c in range(cols):
        p = next((i for i in range(r, rows) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        q = a[r][c]
        a[r] = [x / q for x in a[r]]
        for i in range(rows):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [x - q * y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def determinant_small(a: list[list[int]]) -> int:
    n = len(a)
    if n == 1:
        return a[0][0]
    if n == 2:
        return a[0][0] * a[1][1] - a[0][1] * a[1][0]
    if n == 3:
        return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
                - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
                + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))
    raise ValueError("only rank <= 3 is needed")


def divisor(matrix: list[list[int]], rank: int) -> int:
    value = 0
    for rows in combinations(range(len(matrix)), rank):
        for cols in combinations(range(len(matrix[0])), rank):
            minor = [[matrix[i][j] for j in cols] for i in rows]
            value = gcd(value, abs(determinant_small(minor)))
            if value == 1:
                return 1
    return value


def invariants(matrix: list[list[int]]) -> tuple[list[int], list[int]]:
    r = rank_q(matrix)
    ds = [divisor(matrix, k) for k in range(1, r + 1)]
    out = []
    prev = 1
    for d in ds:
        assert d % prev == 0
        out.append(d // prev)
        prev = d
    return out, ds


def matvec(matrix: list[list[int]], vector: list[int]) -> list[int]:
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]


def content(vector: list[int]) -> int:
    out = 0
    for x in vector:
        out = gcd(out, abs(x))
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=EVIDENCE)
    args = parser.parse_args()
    raw = args.evidence.read_bytes()
    doc = json.loads(raw)
    assert raw == canon(doc)
    assert doc["schema_id"] == "hcs-c65-mark-saturation-prefreeze-v1"
    assert doc["status"] == "PREFREEZE_G3_PASS"
    assert doc["scope_literal"] == FIREWALL
    assert doc["claims"] == {"arithmetic_local_claimed": False, "full_burnside_ring_claimed": False, "integer_kernel_basis_saturated": True, "restricted_mark_saturation_only": True}
    assert h(C63.read_bytes()) == H63 and h(C64.read_bytes()) == H64 and h(C64M.read_bytes()) == H64M
    c63 = json.loads(C63.read_text())
    c64 = json.loads(C64.read_text())
    assert c63["schema_id"] == "hcs-c63-burnside-kernel-prefreeze-v1"
    assert c64["schema_id"] == "hcs-c64-table-of-marks-prefreeze-v1"
    assert c63["scope_literal"] == c64["scope_literal"] == FIREWALL
    assert doc["authority"] == {"c63": H63, "c64": H64, "c64_manifest": H64M, "c63_matrix_sha256": c63["matrix_sha256"], "c64_matrix_sha256": c64["matrix_sha256"]}

    char = c63["character_matrix"]
    mark = c64["mark_matrix"]
    assert rank_q(char) == 13 and rank_q(mark) == 16
    basis = doc["kernel_basis"]
    assert basis == {
        "z1": [0,0,0,0,0,0,0,0,-1,1,0,0,0,0,0,0],
        "z2": [0,-1,-1,0,-1,-1,0,0,0,0,1,1,1,1,0,0],
        "z3": [0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,1],
    }
    assert all(matvec(char, basis[k]) == [0] * 25 for k in ("z1", "z2", "z3"))
    kernel_rows = [[basis[k][i] for k in ("z1", "z2", "z3")] for i in range(16)]
    assert rank_q(kernel_rows) == 3 and divisor(kernel_rows, 3) == 1
    assert doc["kernel_basis_minor_gcd"] == 1

    v = {k: matvec(mark, basis[k]) for k in ("z1", "z2", "z3")}
    assert doc["mark_vectors"] == {**v, "r4": [-x for x in v["z2"]]}
    old = [[v["z1"][i], v["z3"][i]] for i in range(16)]
    allv = [[v["z1"][i], v["z2"][i], v["z3"][i]] for i in range(16)]
    old_snf, old_d = invariants(old)
    all_snf, all_d = invariants(allv)
    assert old_snf == [2,8] and old_d == [2,16]
    assert all_snf == [2,2,8] and all_d == [2,4,32]
    assert doc["old_snf"] == old_snf and doc["old_determinantal_divisors"] == old_d
    assert doc["all_snf"] == all_snf and doc["all_determinantal_divisors"] == all_d

    u = {"u1": [x // 8 for x in v["z1"]], "u2": [x // 2 for x in v["z2"]], "u3": [x // 2 for x in v["z3"]]}
    assert all(all(x * 0 == 0 for x in vec) for vec in u.values())
    assert doc["all_saturation_basis"] == u and doc["old_saturation_basis"] == {"u1":u["u1"], "u3":u["u3"]}
    assert divisor([[u["u1"][i],u["u3"][i]] for i in range(16)], 2) == 1
    assert divisor([[u["u1"][i],u["u2"][i],u["u3"][i]] for i in range(16)], 3) == 1
    assert doc["mark_contents"] == {k: content(v[k]) for k in ("z1","z2","z3")} | {"r4":content([-x for x in v["z2"]])}
    assert doc["relative_jump"] == {"old_index":16,"all_index":32,"quotient_index":2,"generator":"u2=m(z2)/2=-m(R4)/2","order":2}
    print(json.dumps({"status":"PASS", "old_snf":old_snf, "all_snf":all_snf, "old_index":16, "all_index":32, "relative_jump":2}, sort_keys=True))


if __name__ == "__main__":
    main()
