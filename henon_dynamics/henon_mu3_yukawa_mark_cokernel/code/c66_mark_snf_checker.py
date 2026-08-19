#!/usr/bin/env python3
"""Independent checker for the C66 restricted mark-map Smith certificate."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c66_mark_snf_evidence.json"
C64 = ROOT / "henon_dynamics/henon_mu3_yukawa_burnside_marks/results/c64_mark_evidence.json"
C64M = ROOT / "henon_dynamics/henon_mu3_yukawa_burnside_marks/C64_PREFREEZE_MANIFEST.json"
C65 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_defect/results/c65_defect_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
H64 = "7c4673e46f2b97ac03d4e331c762a47286058c36ea243fb20fc39543dd699212"
H64M = "eb1d6a55cb81ccfc9b3041879cb913367a514f5c4cba50872d8b286c0ac095b6"
H65 = "ebdd80fd2292225b98248aacd6b21bafab2987bdccb801c22c10adef7e7b4e4c"
HM = "4e57d980e774e14709d60feac0fff5af831b6496409d248f398a8a3e2796c307"


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def smith(matrix: list[list[int]]) -> list[int]:
    # This is a separate Euclidean implementation from the producer: all
    # pivot reductions are performed by explicit row/column operations.
    a = [list(map(int, row)) for row in matrix]
    m, n = len(a), len(a[0]) if a else 0
    result = []
    k = 0
    while k < m and k < n:
        nonzero = [(abs(a[i][j]), i, j) for i in range(k, m) for j in range(k, n) if a[i][j]]
        if not nonzero:
            break
        _, i, j = min(nonzero)
        a[k], a[i] = a[i], a[k]
        for row in a:
            row[k], row[j] = row[j], row[k]
        while True:
            moved = False
            pivot = a[k][k]
            for i in range(k + 1, m):
                if not a[i][k]:
                    continue
                q = a[i][k] // pivot
                for j in range(n):
                    a[i][j] -= q * a[k][j]
                if a[i][k] and abs(a[i][k]) < abs(a[k][k]):
                    a[k], a[i] = a[i], a[k]
                moved = True
                break
            if moved:
                continue
            pivot = a[k][k]
            for j in range(k + 1, n):
                if not a[k][j]:
                    continue
                q = a[k][j] // pivot
                for i in range(m):
                    a[i][j] -= q * a[i][k]
                if a[k][j] and abs(a[k][j]) < abs(a[k][k]):
                    for row in a:
                        row[k], row[j] = row[j], row[k]
                moved = True
                break
            if moved:
                continue
            pivot = a[k][k]
            bad = None
            for i in range(k + 1, m):
                for j in range(k + 1, n):
                    if a[i][j] % pivot:
                        bad = i
                        break
                if bad is not None:
                    break
            if bad is None:
                break
            a[k] = [x + y for x, y in zip(a[k], a[bad])]
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
    assert raw == canonical(doc)
    assert doc["schema_id"] == "hcs-c66-mark-snf-prefreeze-v1"
    assert doc["status"] == "PREFREEZE_G3_PASS"
    assert doc["scope_literal"] == FIREWALL
    assert doc["claims"] == {"arithmetic_local_claimed": False, "full_burnside_ring_claimed": False, "restricted_16_type_mark_cokernel_only": True}
    raw64, raw64m, raw65 = C64.read_bytes(), C64M.read_bytes(), C65.read_bytes()
    assert digest(raw64) == H64 and digest(raw64m) == H64M and digest(raw65) == H65
    c64, c65 = json.loads(raw64), json.loads(raw65)
    assert c64["schema_id"] == "hcs-c64-table-of-marks-prefreeze-v1"
    assert c64["status"] == "PREFREEZE_G3_PASS" and c64["scope_literal"] == FIREWALL
    assert c64["matrix_sha256"] == HM
    assert c65["schema_id"] == "hcs-c65-mark-saturation-prefreeze-v1"
    assert c65["status"] == "PREFREEZE_G3_PASS" and c65["scope_literal"] == FIREWALL
    assert doc["authority"] == {"c64": H64, "c64_manifest": H64M, "c65": H65, "c64_matrix_sha256": HM}

    matrix = c64["mark_matrix"]
    assert len(matrix) == 16 and all(len(row) == 16 for row in matrix)
    values = smith(matrix)
    expected = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 24, 144]
    assert values == expected == doc["smith_invariants"]
    d = []
    p = 1
    for x in values:
        p *= x
        d.append(p)
    assert d == doc["determinantal_divisors"]
    assert d[-1] == 226492416 == c64["determinant"] == doc["mark_determinant"]
    assert doc["mark_shape"] == [16, 16] and doc["mark_rank"] == 16
    assert doc["primary_invariants"] == {"2": [2] * 10 + [4] * 3 + [8, 16], "3": [3, 9]}
    assert c65["old_snf"] == [2, 8] and c65["all_snf"] == [2, 2, 8]
    assert c65["relative_jump"] == {"old_index": 16, "all_index": 32, "quotient_index": 2, "generator": "u2=m(z2)/2=-m(R4)/2", "order": 2}
    print(json.dumps({"status": "PASS", "smith_invariants": values,
                      "determinant": d[-1], "primary_2": doc["primary_invariants"]["2"],
                      "primary_3": doc["primary_invariants"]["3"]}, sort_keys=True))


if __name__ == "__main__":
    main()
