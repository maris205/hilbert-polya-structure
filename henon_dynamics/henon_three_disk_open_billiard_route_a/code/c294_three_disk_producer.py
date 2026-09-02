#!/usr/bin/env python3
"""Produce deterministic exact evidence for HCS-C294."""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c294_three_disk_evidence.json"
SOURCE = "f8d3ad9a8940b54e82854b2924be353575ed8fcb"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788307200


def canonical_payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def mobius(n: int) -> int:
    value = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            value = -value
            if n % p == 0:
                return 0
            while n % p == 0:
                n //= p
        p += 1
    return -value if n > 1 else value


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def admissible(word: tuple[int, ...]) -> bool:
    return bool(word) and all(word[j] != word[(j + 1) % len(word)] for j in range(len(word)))


def least_period(word: tuple[int, ...]) -> int:
    n = len(word)
    for d in divisors(n):
        if all(word[j] == word[j % d] for j in range(n)):
            return d
    raise AssertionError("unreachable")


def matmul(a: tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]],
           b: tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]):
    return (
        (a[0][0] * b[0][0] + a[0][1] * b[1][0],
         a[0][0] * b[0][1] + a[0][1] * b[1][1]),
        (a[1][0] * b[0][0] + a[1][1] * b[1][0],
         a[1][0] * b[0][1] + a[1][1] * b[1][1]),
    )


def matpow(a, n: int):
    result = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))
    for _ in range(n):
        result = matmul(result, a)
    return result


def q(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def matrix_strings(a) -> list[list[str]]:
    return [[q(a[i][j]) for j in range(2)] for i in range(2)]


def build() -> dict:
    mp.mp.dps = 80
    count_rows = []
    for n in range(1, 17):
        fixed = 2**n + 2 * ((-1) ** n)
        primitive_rooted = sum(mobius(e) * (2 ** (n // e) + 2 * ((-1) ** (n // e))) for e in divisors(n))
        assert primitive_rooted % n == 0
        count_rows.append({
            "n": n,
            "fixed_rooted_words": fixed,
            "exact_period_rooted_words": primitive_rooted,
            "primitive_orbits": primitive_rooted // n,
        })

    direct_rows = []
    for n in range(1, 11):
        fixed = 0
        primitive = 0
        reversal_fixed_rooted = 0
        for word in itertools.product(range(3), repeat=n):
            if not admissible(word):
                continue
            fixed += 1
            primitive += least_period(word) == n
            reverse = tuple(reversed(word))
            reversal_fixed_rooted += any(reverse == word[k:] + word[:k] for k in range(n))
        direct_rows.append({
            "n": n,
            "fixed_rooted_words": fixed,
            "exact_period_rooted_words": primitive,
            "reversal_symmetric_rooted_words": reversal_fixed_rooted,
        })

    zeta_coefficients = [1]
    for n in range(1, 17):
        zeta_coefficients.append(
            (3 * zeta_coefficients[n - 2] if n >= 2 else 0)
            + (2 * zeta_coefficients[n - 3] if n >= 3 else 0)
        )

    geometry_rows = []
    for r, d in [(1, 3), (2, 5), (3, 7), (5, 12), (7, 17), (11, 27)]:
        gap = mp.sqrt(3) * d / 2 - 2 * r
        geometry_rows.append({
            "r": r,
            "d": d,
            "pair_gap": d - 2 * r,
            "no_eclipse_gap_60_digits": mp.nstr(gap, 61),
            "no_eclipse": bool(gap > 0),
        })

    optical_rows = []
    for a in [Fraction(1, 3), Fraction(1, 2), Fraction(1), Fraction(2), Fraction(5, 2)]:
        for ell in [Fraction(1, 4), Fraction(1, 2), Fraction(1), Fraction(3, 2), Fraction(3)]:
            block = ((Fraction(1), ell), (a, Fraction(1) + a * ell))
            for n in range(2, 9):
                monodromy = matpow(block, n)
                det = monodromy[0][0] * monodromy[1][1] - monodromy[0][1] * monodromy[1][0]
                trace = monodromy[0][0] + monodromy[1][1]
                optical_rows.append({
                    "a": q(a), "ell": q(ell), "n": n,
                    "matrix": matrix_strings(monodromy),
                    "determinant": q(det), "trace": q(trace),
                    "hyperbolic": det == 1 and trace > 2,
                })

    r = mp.mpf(1)
    d = mp.mpf(3)
    ell3 = d - mp.sqrt(3) * r
    a3 = 4 / (mp.sqrt(3) * r)
    block3 = mp.matrix([[1, ell3], [a3, 1 + a3 * ell3]])
    mon3 = block3**3
    period_three = {
        "word": "012",
        "r": "1",
        "d": "3",
        "flight_length_exact": "3-sqrt(3)",
        "total_length_exact": "9-3*sqrt(3)",
        "incidence_cosine_exact": "sqrt(3)/2",
        "defocusing_kick_exact": "4/sqrt(3)",
        "monodromy_trace_60_digits": mp.nstr(mon3[0, 0] + mon3[1, 1], 61),
        "monodromy_determinant_60_digits": mp.nstr(mp.det(mon3), 61),
    }
    ell2 = Fraction(1)
    a2 = Fraction(2)
    mon2 = matpow(((Fraction(1), ell2), (a2, Fraction(1) + a2 * ell2)), 2)
    period_two = {
        "word": "01", "r": 1, "d": 3,
        "flight_length": "1", "total_length": "2", "incidence_cosine": "1",
        "monodromy": matrix_strings(mon2),
        "monodromy_trace": q(mon2[0][0] + mon2[1][1]),
        "monodromy_determinant": q(mon2[0][0] * mon2[1][1] - mon2[0][1] * mon2[1][0]),
    }

    flags = {
        "claims_target_arithmetic_local_data": False,
        "claims_target_euler_factors": False,
        "claims_root_number": False,
        "claims_automorphy": False,
        "claims_target_divisor_or_counting_law": False,
        "claims_target_functional_equation": False,
        "claims_target_zero_match": False,
        "claims_hilbert_polya_operator": False,
        "invokes_route_b": False,
    }
    data = {
        "schema": "hcs-c294-three-disk-open-billiard-v1",
        "candidate_id": "HCS-C294",
        "obstruction_id": "HEN-O278",
        "evaluation_date": "2026-09-02",
        "fixed_epoch": EPOCH,
        "source_commit": SOURCE,
        "scope_literal": SCOPE,
        "evaluator": {"version": "0.2.0", "sha256": EVALUATOR},
        "model": {
            "obstacles": "three closed radius-r disks at the vertices of an equilateral triangle of side d",
            "domain": "Euclidean plane minus the obstacle interiors",
            "parameter_chamber": "r>0 and d>4r/sqrt(3)",
            "clock": "one specular collision",
            "orientation": "oriented rays; time reversal reverses the cyclic word",
            "no_eclipse_gap": "sqrt(3)d/2-2r",
        },
        "theorem_contract": {
            "coding": "cyclically reduced cyclic classes correspond bijectively to periodic-ray iterates",
            "iterate_convention": "a periodic-ray iterate is a primitive oriented geometric ray paired with a positive traversal multiplicity",
            "primitive_coding": "primitive cyclic classes correspond bijectively to primitive oriented geometric rays",
            "geometry": "each coded iterate has a unique non-grazing, isolated, dispersing-hyperbolic geometric support",
            "fixed_count": "F_n=2^n+2(-1)^n",
            "primitive_ledger": "P_n=sum_{e|n}mu(e)F_{n/e}; O_n=P_n/n",
            "collision_zeta": "1/((1-2z)(1+z)^2)",
            "length_bounds": "n(d-2r)<=L_w<=n(d+2r)",
            "reversal": "[w] maps to [reverse(w)] without automatic division by two",
        },
        "proof_contract": {
            "existence": "compact minimization of polygonal length over the product of closed disks",
            "boundary": "no-eclipse excludes an interior minimizing vertex",
            "uniqueness": "convexity plus strict convexity of every disk excludes two distinct minimizers",
            "reflection": "the constrained first variation gives specular reflection and excludes grazing",
            "hyperbolicity": "positive free-flight and defocusing optical matrices have determinant one and trace greater than two",
            "finite_role": "finite words and optical grids audit conventions only; they do not prove geometric coding",
        },
        "enumeration": {
            "count_rows": count_rows,
            "direct_rows": direct_rows,
            "zeta_coefficients_0_to_16": zeta_coefficients,
            "optical_rows": optical_rows,
            "geometry_rows": geometry_rows,
            "symmetric_orbits": [period_two, period_three],
            "count_cell_count": len(count_rows) + len(direct_rows),
            "optical_cell_count": len(optical_rows),
            "geometry_cell_count": len(geometry_rows) + 2,
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": flags,
        "nonclaims": [
            "No target arithmetic local datum, Euler factor, root number, automorphy, divisor, functional equation, or zero match is asserted.",
            "The collision-code zeta is source-local and uses bounce count rather than geometric length.",
            "The exterior Dirichlet Laplacian is only the natural quantization of the billiard geometry, not a Hilbert--Polya operator.",
            "No literary priority is claimed for classical open-billiard coding or dispersing hyperbolicity.",
        ],
        "references": [
            {"identifier": "10.1070/RM1970v025n02ABEH003794", "role": "dispersing-billiard lineage"},
            {"identifier": "10.5802/aif.1137", "role": "several-convex-obstacle and no-eclipse lineage"},
            {"identifier": "10.1063/1.456019", "role": "three-hard-disk scattering owner"},
        ],
    }
    data["payload_sha256"] = canonical_payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C294_PRODUCER_PASS",
        "output": str(args.output),
        "payload_sha256": data["payload_sha256"],
        "count_cells": data["enumeration"]["count_cell_count"],
        "optical_cells": data["enumeration"]["optical_cell_count"],
        "geometry_cells": data["enumeration"]["geometry_cell_count"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
