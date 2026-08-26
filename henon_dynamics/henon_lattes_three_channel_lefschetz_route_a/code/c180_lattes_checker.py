#!/usr/bin/env python3
"""Independent exact checker for C180; deliberately imports no producer code."""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
from math import gcd
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c180_lattes_evidence.json"
EXPECTED_SOURCE = "bbb809ee198bc9ad5f196383baab1e3d9de38e43"
EXPECTED_EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"


def canonical_hash(payload: dict) -> str:
    work = dict(payload)
    work.pop("payload_sha256", None)
    return sha256(
        json.dumps(work, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def digest_rows(rows: list[str]) -> str:
    return sha256(("\n".join(rows) + "\n").encode()).hexdigest()


def mu(n: int) -> int:
    ans, p, x = 1, 2, n
    while p * p <= x:
        if x % p == 0:
            x //= p
            ans = -ans
            if x % p == 0:
                return 0
            while x % p == 0:
                x //= p
        p += 1
    return -ans if x > 1 else ans


def divs(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if not n % d]


def neg(p: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return tuple(Fraction(0) if x == 0 else 1 - x for x in p)  # type: ignore[return-value]


def canon_point(p: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return min(p, neg(p))


def point_text(point: tuple[Fraction, Fraction]) -> str:
    return ",".join(f"{x.numerator}/{x.denominator}" for x in point)


def require(condition: bool, message: str, counter: list[int]) -> None:
    counter[0] += 1
    if not condition:
        raise AssertionError(message)


def validate(payload: dict) -> int:
    checks = [0]
    require(payload.get("payload_sha256") == canonical_hash(payload), "payload hash mismatch", checks)
    require(payload.get("schema") == "hcs-c180-lattes-three-channel-lefschetz-v1", "schema", checks)
    require(payload.get("candidate_id") == "HCS-C180", "candidate", checks)
    require(payload.get("evaluation_date") == "2026-08-26", "date", checks)
    require(payload.get("scope_literal") == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope", checks)
    require(payload.get("source_commit") == EXPECTED_SOURCE, "source commit", checks)
    require(payload["evaluator"]["authority_sha256"] == EXPECTED_EVALUATOR, "evaluator hash", checks)
    require(payload["evaluator"]["skill_version"] == "0.2.0", "evaluator version", checks)
    require(payload["artifact_path_base"].endswith("henon_lattes_three_channel_lefschetz_route_a"), "path", checks)
    require("all complex elliptic curves" in payload["source_lock"]["family"], "all tau lock", checks)
    require("every integer multiplication factor m>=2" in payload["source_lock"]["family"], "all m lock", checks)
    require(
        payload["source_lock"]["arithmetic_origin"]
        == "elliptic torsion geometry only; no rational-prime or prime-power orbit correspondence is intrinsic",
        "arithmetic-origin lock",
        checks,
    )
    require(payload["route_a_verdict"] == {
        "A0": "A0_FAIL", "A1": "A1_WEAK", "A2": "A2_FAIL", "A3": "A3_FAIL",
        "A4": "A4_FORMAL_HINT", "overall": "ROUTE_A_REJECTED",
        "a0_failure_forces_rejection": True, "route_b_invocation_allowed": False,
    }, "route tuple", checks)
    require(len(payload["nonclaims"]) == 5, "nonclaims", checks)

    rows = payload["formula_rows"]
    require(len(rows) == 108, "formula row count", checks)
    cursor = 0
    for m in range(2, 11):
        for n in range(1, 13):
            row = rows[cursor]
            cursor += 1
            a = m**n
            h = 1 if a % 2 == 0 else 4
            plus = ((a - 1) ** 2 - h) // 2
            minus = ((a + 1) ** 2 - h) // 2
            lef = Fraction(plus, 1 - a) + Fraction(minus, 1 + a) + Fraction(h, 1 - a * a)
            exact = sum(mu(n // d) * (m ** (2 * d) + 1) for d in divs(n))
            expected = {
                "m": m, "n": n, "a": a, "parity": "even" if a % 2 == 0 else "odd",
                "plus_regular_count": plus, "minus_regular_count": minus, "branch_count": h,
                "plus_multiplier": a, "minus_multiplier": -a, "branch_multiplier": a * a,
                "fixed_point_total": a * a + 1,
                "lefschetz_sum": f"{lef.numerator}/{lef.denominator}",
                "exact_period_points": exact, "primitive_cycles": exact // n,
            }
            for key, value in expected.items():
                require(row.get(key) == value, f"formula {m},{n}:{key}", checks)
            require(plus + minus + h == a * a + 1, "channel total", checks)
            require(lef == 1, "Lefschetz", checks)
            require(exact % n == 0 and exact >= 0, "primitive integrality", checks)

    torsion_rows = payload["torsion_enumeration_rows"]
    require(len(torsion_rows) == 16, "torsion row count", checks)
    expected_torsion_keys: list[tuple[int, int]] = []
    for m in range(2, 7):
        for n in range(1, 13):
            if m**n <= 80:
                expected_torsion_keys.append((m, n))
    require([(r["m"], r["n"]) for r in torsion_rows] == expected_torsion_keys, "torsion key set", checks)
    point_total = 0
    for row in torsion_rows:
        m, n, a = row["m"], row["n"], row["a"]
        require(a == m**n, "torsion power", checks)
        plus_raw = {(Fraction(i, a - 1), Fraction(j, a - 1)) for i in range(a - 1) for j in range(a - 1)}
        minus_raw = {(Fraction(i, a + 1), Fraction(j, a + 1)) for i in range(a + 1) for j in range(a + 1)}
        overlap = plus_raw & minus_raw
        pcls = {canon_point(x) for x in plus_raw - overlap}
        mcls = {canon_point(x) for x in minus_raw - overlap}
        bcls = {canon_point(x) for x in overlap}
        encoded = [
            *(f"+:{point_text(x)}" for x in sorted(pcls)),
            *(f"-:{point_text(x)}" for x in sorted(mcls)),
            *(f"b:{point_text(x)}" for x in sorted(bcls)),
        ]
        expected = {
            "plus_torsion_order": a - 1, "minus_torsion_order": a + 1,
            "gcd_orders": gcd(a - 1, a + 1), "intersection_size": len(overlap),
            "plus_regular_classes": len(pcls), "minus_regular_classes": len(mcls),
            "branch_classes": len(bcls), "union_quotient_classes": len(pcls | mcls | bcls),
            "class_digest": digest_rows(encoded),
        }
        for key, value in expected.items():
            require(row.get(key) == value, f"torsion {m},{n}:{key}", checks)
        point_total += (a - 1) ** 2 + (a + 1) ** 2

    reps = sorted({min((x, y), (-x, -y)) for x in range(-20, 21) for y in range(-20, 21) if (x, y) != (0, 0)})
    wold = payload["wold_rows"]
    require(len(reps) == 840, "mode reps", checks)
    require(len(wold) == 5880, "wold row count", checks)
    cursor = 0
    for m in range(2, 9):
        for k in reps:
            row = wold[cursor]
            cursor += 1
            root, depth = k, 0
            while root[0] % m == 0 and root[1] % m == 0:
                root = (root[0] // m, root[1] // m)
                depth += 1
            expected = {
                "m": m, "k": list(k), "root": list(root), "depth": depth,
                "root_is_primitive": True, "shifted_k": [m * k[0], m * k[1]],
                "adjoint_preimage_exists": k[0] % m == 0 and k[1] % m == 0,
            }
            for key, value in expected.items():
                require(row.get(key) == value, f"Wold {m},{k}:{key}", checks)

    counts = payload["counts"]
    require(counts["parameter_pairs_m_n"] == 108, "count formula", checks)
    require(counts["formula_scalar_assertions"] == 1296, "count scalar", checks)
    require(counts["torsion_enumerations"] == 16, "count torsion", checks)
    require(counts["torsion_points_materialized"] == point_total, "count points", checks)
    require(counts["wold_mode_rows"] == 5880, "count wold", checks)
    require(counts["wold_roots_per_m"] == 840, "count reps", checks)
    require(payload["theorem"]["lefschetz"].endswith("=1"), "theorem lefschetz", checks)
    require(payload["theorem"]["artin_mazur_zeta"] == "1/((1-z)(1-m^2*z))", "AM zeta", checks)
    require("S^(aleph_0)" in payload["theorem"]["wold"], "Wold theorem", checks)
    return checks[0]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence", nargs="?", type=Path, default=DEFAULT_EVIDENCE)
    args = parser.parse_args()
    payload = json.loads(args.evidence.read_text())
    checks = validate(payload)
    print(json.dumps({"status": "C180_CHECKER_PASS", "assertions": checks, "payload_sha256": payload["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
