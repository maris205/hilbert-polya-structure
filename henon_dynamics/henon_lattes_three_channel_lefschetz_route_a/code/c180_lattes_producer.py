#!/usr/bin/env python3
"""Produce exact C180 evidence for the multiplication Lattes family."""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
from math import gcd
from pathlib import Path


SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
SOURCE_COMMIT = "bbb809ee198bc9ad5f196383baab1e3d9de38e43"
EVALUATOR_PATH = "flow_systems/skills/route-a-evaluator.md"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
M_MIN, M_MAX, N_MAX = 2, 10, 12
TORSION_M_MAX, TORSION_A_MAX = 6, 80
WOLD_M_MIN, WOLD_M_MAX, WOLD_BOX = 2, 8, 20


def canonical_hash(payload: dict) -> str:
    work = dict(payload)
    work.pop("payload_sha256", None)
    raw = json.dumps(work, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def digest_rows(rows: list[str]) -> str:
    return sha256(("\n".join(rows) + "\n").encode()).hexdigest()


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n: int) -> int:
    value, primes, p = n, 0, 2
    while p * p <= value:
        if value % p == 0:
            value //= p
            primes += 1
            if value % p == 0:
                return 0
            while value % p == 0:
                value //= p
        p += 1
    if value > 1:
        primes += 1
    return -1 if primes & 1 else 1


def channel_data(a: int) -> tuple[int, int, int, int]:
    branch = 1 if a % 2 == 0 else 4
    plus = ((a - 1) ** 2 - branch) // 2
    minus = ((a + 1) ** 2 - branch) // 2
    return plus, minus, branch, a * a + 1


def formula_rows() -> list[dict]:
    rows: list[dict] = []
    for m in range(M_MIN, M_MAX + 1):
        for n in range(1, N_MAX + 1):
            a = m**n
            plus, minus, branch, total = channel_data(a)
            lef = Fraction(plus, 1 - a) + Fraction(minus, 1 + a) + Fraction(branch, 1 - a * a)
            exact = sum(mobius(n // d) * (m ** (2 * d) + 1) for d in divisors(n))
            assert lef == 1 and exact % n == 0
            rows.append(
                {
                    "m": m,
                    "n": n,
                    "a": a,
                    "parity": "even" if a % 2 == 0 else "odd",
                    "plus_regular_count": plus,
                    "minus_regular_count": minus,
                    "branch_count": branch,
                    "plus_multiplier": a,
                    "minus_multiplier": -a,
                    "branch_multiplier": a * a,
                    "fixed_point_total": total,
                    "lefschetz_sum": f"{lef.numerator}/{lef.denominator}",
                    "exact_period_points": exact,
                    "primitive_cycles": exact // n,
                }
            )
    return rows


def torsion_points(q: int) -> set[tuple[Fraction, Fraction]]:
    return {(Fraction(i, q), Fraction(j, q)) for i in range(q) for j in range(q)}


def neg(point: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return tuple(Fraction(0) if x == 0 else 1 - x for x in point)  # type: ignore[return-value]


def canonical_sign(point: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    opposite = neg(point)
    return min(point, opposite)


def point_text(point: tuple[Fraction, Fraction]) -> str:
    def f(x: Fraction) -> str:
        return f"{x.numerator}/{x.denominator}"

    return f"{f(point[0])},{f(point[1])}"


def torsion_rows() -> list[dict]:
    rows: list[dict] = []
    for m in range(M_MIN, TORSION_M_MAX + 1):
        for n in range(1, N_MAX + 1):
            a = m**n
            if a > TORSION_A_MAX:
                continue
            plus_raw, minus_raw = torsion_points(a - 1), torsion_points(a + 1)
            overlap = plus_raw & minus_raw
            plus_classes = {canonical_sign(x) for x in plus_raw - overlap}
            minus_classes = {canonical_sign(x) for x in minus_raw - overlap}
            branch_classes = {canonical_sign(x) for x in overlap}
            all_classes = plus_classes | minus_classes | branch_classes
            encoded = [
                *(f"+:{point_text(x)}" for x in sorted(plus_classes)),
                *(f"-:{point_text(x)}" for x in sorted(minus_classes)),
                *(f"b:{point_text(x)}" for x in sorted(branch_classes)),
            ]
            expected = channel_data(a)
            observed = (len(plus_classes), len(minus_classes), len(branch_classes), len(all_classes))
            assert observed == expected
            rows.append(
                {
                    "m": m,
                    "n": n,
                    "a": a,
                    "plus_torsion_order": a - 1,
                    "minus_torsion_order": a + 1,
                    "gcd_orders": gcd(a - 1, a + 1),
                    "intersection_size": len(overlap),
                    "plus_regular_classes": len(plus_classes),
                    "minus_regular_classes": len(minus_classes),
                    "branch_classes": len(branch_classes),
                    "union_quotient_classes": len(all_classes),
                    "class_digest": digest_rows(encoded),
                }
            )
    return rows


def canonical_vector(k: tuple[int, int]) -> tuple[int, int]:
    return min(k, (-k[0], -k[1]))


def wold_rows() -> list[dict]:
    reps = sorted(
        {
            canonical_vector((x, y))
            for x in range(-WOLD_BOX, WOLD_BOX + 1)
            for y in range(-WOLD_BOX, WOLD_BOX + 1)
            if (x, y) != (0, 0)
        }
    )
    rows: list[dict] = []
    for m in range(WOLD_M_MIN, WOLD_M_MAX + 1):
        for k in reps:
            root = k
            depth = 0
            while root[0] % m == 0 and root[1] % m == 0:
                root = (root[0] // m, root[1] // m)
                depth += 1
            assert (root[0] * m**depth, root[1] * m**depth) == k
            rows.append(
                {
                    "m": m,
                    "k": [k[0], k[1]],
                    "root": [root[0], root[1]],
                    "depth": depth,
                    "root_is_primitive": not (root[0] % m == 0 and root[1] % m == 0),
                    "shifted_k": [m * k[0], m * k[1]],
                    "adjoint_preimage_exists": k[0] % m == 0 and k[1] % m == 0,
                }
            )
    return rows


def build_evidence() -> dict:
    formulas = formula_rows()
    torsion = torsion_rows()
    wold = wold_rows()
    payload = {
        "schema": "hcs-c180-lattes-three-channel-lefschetz-v1",
        "candidate_id": "HCS-C180",
        "evaluation_date": "2026-08-26",
        "scope_literal": SCOPE,
        "source_commit": SOURCE_COMMIT,
        "evaluator": {
            "skill_version": "0.2.0",
            "authority_path": EVALUATOR_PATH,
            "authority_sha256": EVALUATOR_SHA256,
        },
        "artifact_path_base": "henon_dynamics/henon_lattes_three_channel_lefschetz_route_a",
        "source_lock": {
            "family": "all complex elliptic curves E_tau and every integer multiplication factor m>=2",
            "map": "f_{m,tau} o pi = pi o [m] on E_tau/{+/-1}=P^1",
            "arithmetic_origin": "elliptic torsion geometry only; no rational-prime or prime-power orbit correspondence is intrinsic",
            "clock": "one application of f_{m,tau}",
            "normalization": "unweighted fixed classes, separately resolved by multiplier channel",
            "determinant_convention": "Artin--Mazur exponential only; ordinary Fredholm determinant of Koopman is unavailable",
            "precision": "exact integer, rational, finite torsion, and symbolic formal-series arithmetic",
            "forbidden_data": "prime tables, target zeros or divisors, arithmetic local factors, Euler factors, root numbers, automorphy, Hilbert--Polya, and Route B",
        },
        "theorem": {
            "fixed_class_set": "Fix(f_{m,tau}^n)=(E_tau[m^n-1] union E_tau[m^n+1])/{+/-1}",
            "intersection": "E_tau[gcd(m^n-1,m^n+1)] has h=1 for m^n even and h=4 for m^n odd",
            "channels": "N_+=((a-1)^2-h)/2 at multiplier +a; N_-=((a+1)^2-h)/2 at multiplier -a; N_br=h at multiplier a^2",
            "lefschetz": "N_+/(1-a)+N_-/(1+a)+N_br/(1-a^2)=1",
            "fixed_total": "#Fix(f^n)=m^(2n)+1",
            "artin_mazur_zeta": "1/((1-z)(1-m^2*z))",
            "exact_period": "P_m(n)=sum_{d|n} mu(n/d)(m^(2d)+1)",
            "wold": "U_m on L2(P1,pi_*Haar) is 1 direct_sum S^(aleph_0) on even Fourier modes",
        },
        "formula_rows": formulas,
        "torsion_enumeration_rows": torsion,
        "wold_rows": wold,
        "counts": {
            "parameter_pairs_m_n": len(formulas),
            "formula_scalar_assertions": 12 * len(formulas),
            "torsion_enumerations": len(torsion),
            "torsion_points_materialized": sum((row["a"] - 1) ** 2 + (row["a"] + 1) ** 2 for row in torsion),
            "wold_mode_rows": len(wold),
            "wold_roots_per_m": len(wold) // (WOLD_M_MAX - WOLD_M_MIN + 1),
            "tau_moduli_covered": "all tau in the upper half-plane modulo elliptic-curve isomorphism",
            "multiplication_factors_covered": "all integers m>=2",
        },
        "route_a_verdict": {
            "A0": "A0_FAIL",
            "A1": "A1_WEAK",
            "A2": "A2_FAIL",
            "A3": "A3_FAIL",
            "A4": "A4_FORMAL_HINT",
            "overall": "ROUTE_A_REJECTED",
            "a0_failure_forces_rejection": True,
            "route_b_invocation_allowed": False,
        },
        "nonclaims": [
            "novelty of Lattes maps, torsion fixed-point descriptions, holomorphic Lefschetz, or Wold decomposition",
            "a rational-prime or prime-power orbit correspondence",
            "an arithmetic local factor, Euler factor, or root number",
            "automorphy, a Hilbert--Polya operator, or Route-B authorization",
            "an ordinary Fredholm determinant for the noncompact Koopman isometry",
        ],
        "integrity": {
            "finite_ledgers_are_proof": False,
            "external_reviewer_simulated": False,
            "acceptance_rate_reported": False,
            "citation_population": 1,
        },
    }
    payload["payload_sha256"] = canonical_hash(payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "results/c180_lattes_evidence.json",
    )
    args = parser.parse_args()
    payload = build_evidence()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(
        json.dumps(
            {
                "status": "C180_PRODUCER_PASS",
                "formula_rows": len(payload["formula_rows"]),
                "torsion_rows": len(payload["torsion_enumeration_rows"]),
                "wold_rows": len(payload["wold_rows"]),
                "payload_sha256": payload["payload_sha256"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
