#!/usr/bin/env python3
"""Produce the exact HCS-C165 Margolus necklace certificate."""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from math import gcd
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c165_margolus_evidence.json"
SOURCE_COMMIT = "4342893ce5e2516924181744bfacc01c12e4959d"
MAX_M = 16
BRUTE_MAX_M = 8


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n: int) -> int:
    sign = 0
    p = 2
    while p * p <= n:
        exponent = 0
        while n % p == 0:
            n //= p
            exponent += 1
        if exponent > 1:
            return 0
        sign += exponent
        p += 1
    if n > 1:
        sign += 1
    return -1 if sign & 1 else 1


def block_a(site: int, size: int) -> int:
    return (site + 1) % size if site % 2 == 0 else site - 1


def block_b(site: int, size: int) -> int:
    return (site + 1) % size if site % 2 else (site - 1) % size


def site_permutation(m: int) -> list[int]:
    size = 2 * m
    return [block_b(block_a(site, size), size) for site in range(size)]


def permute_mask(mask: int, permutation: list[int]) -> int:
    result = 0
    for site, target in enumerate(permutation):
        if (mask >> site) & 1:
            result |= 1 << target
    return result


def brute_exact_period_counts(m: int, permutation: list[int]) -> dict[int, int]:
    counts = {d: 0 for d in divisors(m)}
    for mask in range(1 << (2 * m)):
        current = mask
        for time in divisors(m):
            probe = mask
            for _ in range(time):
                probe = permute_mask(probe, permutation)
            if probe == mask:
                counts[time] += 1
                break
        else:
            raise AssertionError("configuration did not return by the full clock")
    return counts


def exact_period(d: int) -> int:
    return sum(mobius(d // e) * 4**e for e in divisors(d))


def payload_bytes(data: dict) -> bytes:
    body = dict(data)
    body.pop("payload_sha256", None)
    return json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def build() -> dict:
    family_rows = []
    fixed_cells = 0
    period_cells = 0
    brute_configurations = 0
    for m in range(1, MAX_M + 1):
        permutation = site_permutation(m)
        expected = [
            (site + 2) % (2 * m) if site % 2 == 0 else (site - 2) % (2 * m)
            for site in range(2 * m)
        ]
        assert permutation == expected
        reflection = [(-site) % (2 * m) for site in range(2 * m)]
        assert [reflection[permutation[reflection[site]]] for site in range(2 * m)] == [
            permutation.index(site) for site in range(2 * m)
        ]

        pairs = [[2 * j, (1 - 2 * j) % (2 * m)] for j in range(m)]
        for j, (even, odd) in enumerate(pairs):
            assert permutation[even] == pairs[(j + 1) % m][0]
            assert permutation[odd] == pairs[(j + 1) % m][1]

        fixed_rows = []
        for n in range(1, m + 1):
            cycles = 2 * gcd(m, n)
            fixed_rows.append({
                "time_n": n,
                "site_cycles": cycles,
                "fixed_configurations": 2**cycles,
                "closed_formula": 4 ** gcd(m, n),
            })
        fixed_cells += len(fixed_rows)

        period_rows = []
        short = 0
        for d in divisors(m):
            points = exact_period(d)
            assert points >= 0 and points % d == 0
            if d < m:
                short += points
            period_rows.append({
                "period_d": d,
                "exact_period_configurations": points,
                "primitive_cycles": points // d,
                "zeta_exponent": -(points // d),
            })
        period_cells += len(period_rows)
        assert sum(row["exact_period_configurations"] for row in period_rows) == 4**m
        full = period_rows[-1]["exact_period_configurations"]
        assert short + full == 4**m
        assert short * (2**m) <= m * (4**m)

        brute = None
        if m <= BRUTE_MAX_M:
            counts = brute_exact_period_counts(m, permutation)
            brute_configurations += 4**m
            assert counts == {row["period_d"]: row["exact_period_configurations"] for row in period_rows}
            brute = {
                "enumerated_configurations": 4**m,
                "exact_period_counts": {str(d): counts[d] for d in sorted(counts)},
                "matches_necklace_formula": True,
            }

        family_rows.append({
            "half_ring_m": m,
            "site_count": 2 * m,
            "full_tick_site_permutation": permutation,
            "four_letter_pairing": pairs,
            "reflection_permutation": reflection,
            "fixed_rows": fixed_rows,
            "period_rows": period_rows,
            "short_period_configurations": short,
            "full_period_configurations": full,
            "total_configurations": 4**m,
            "short_probability": {"numerator": short, "denominator": 4**m},
            "uniform_bound": {"numerator": m, "denominator": 2**m, "formula": "m*4^(-m/2)=m/2^m"},
            "full_probability_lower_bound": {"numerator": 2**m - m, "denominator": 2**m},
            "zeta_factors": [f"(1-z^{row['period_d']})^({row['zeta_exponent']})" for row in period_rows],
            "koopman_determinant_factors": [f"(1-z^{row['period_d']})^({-row['zeta_exponent']})" for row in period_rows],
            "brute_force": brute,
        })

    data = {
        "schema": "HCS-C165-v1",
        "candidate_id": "HCS-C165",
        "date_utc": "2026-08-25",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "source_lock": {
            "object": "binary configurations on a ring of 2m sites with two staggered Margolus swap layers A and B",
            "family": "every integer m>=1; finite exact replay uses 1<=m<=16",
            "clock": "one full tick is T=B after A; neither A nor B alone is a full source clock",
            "normalization": "uniform labeled binary configurations, exact least full-tick periods, then geometric cycles",
            "determinant_convention": "finite Artin--Mazur zeta and the same-clock Koopman determinant det(I-zU_T)",
            "cutoff": "all formulas hold for every m>=1; finite ledgers use m<=16 and direct state enumeration uses m<=8",
            "precision": "exact permutations, integers, rational probabilities, and symbolic polynomials",
            "allowed_data": "the frozen two-layer local swap schedule and source-derived finite clocks only",
            "forbidden_data": "target zero or prime tables, arithmetic local factors, Euler factors, root numbers, automorphy, Hilbert--Polya operators, and Route-B inputs",
        },
        "pivot_record": {
            "rejected_candidate": "a fourth consecutive broad composite-clock Rule-90 closed-law paper",
            "reason": "the general Rule-90 trace-zero count has no uniform elementary reduction and three preceding rounds already occupy that lineage",
            "replacement": "a reversible two-phase Margolus block cellular automaton with an exact four-letter necklace conjugacy",
            "failed_claim_reframed_as_progress": False,
        },
        "site_permutation_theorem": {
            "layers": "A swaps (0,1),(2,3),... and B swaps (1,2),(3,4),...,(2m-1,0)",
            "full_tick": "T=B after A",
            "cell_motion": "tau(i)=i+2 mod 2m for even i and tau(i)=i-2 mod 2m for odd i",
            "order": "tau^m=identity, including the m=1 identity boundary",
        },
        "necklace_conjugacy_theorem": {
            "pairing": "Phi(x)_j=(x_(2j),x_(1-2j mod 2m)) in {0,1}^2",
            "intertwining": "Phi conjugates one full Margolus tick to one cyclic rotation of an m-letter word over the four-letter alphabet {0,1}^2",
            "fixed_count": "#Fix(T^n)=4^gcd(m,n) for every m,n>=1",
            "complexity_boundary": "the conjugate necklace system is reversible and exactly solvable; it is not claimed to be chaotic or interacting",
        },
        "period_theorem": {
            "support": "every exact configuration period divides m",
            "exact_points": "P_m(d)=sum_(e|d) mu(d/e)4^e for d|m and P_m(d)=0 otherwise",
            "primitive_cycles": "C_m(d)=P_m(d)/d",
            "zeta": "zeta_T(z)=product_(d|m)(1-z^d)^(-C_m(d))",
        },
        "concentration_theorem": {
            "short_bound": "Pr(period<m)<=m*4^(-m/2)=m/2^m for every m>=1",
            "full_bound": "Pr(period=m)>=1-m*4^(-m/2)",
            "proof_boundary": "the bound uses P_m(d)<=4^d, every proper divisor d<=m/2, and fewer than m proper divisors; it is deliberately coarse",
        },
        "reversibility_and_koopman": {
            "reflection": "r(i)=-i mod 2m satisfies r*tau*r=tau^(-1)",
            "koopman_space": "l2 of the finite configuration set with counting measure",
            "koopman": "(U_T f)(x)=f(T^(-1)x) is unitary and det(I-zU_T)=zeta_T(z)^(-1)",
            "antiunitary": "Theta f(x)=conjugate(f(Rx)) is involutive and Theta*U_T*Theta=U_T^(-1)",
            "operator_boundary": "the finite same-clock Koopman lift is self-adjoint exactly for m<=2 and non-self-adjoint for m>=3; no uniform self-adjoint Hilbert--Polya realization is claimed",
        },
        "finite_replay": {
            "m_min": 1,
            "m_max": MAX_M,
            "brute_force_m_max": BRUTE_MAX_M,
            "family_rows": family_rows,
            "fixed_cell_count": fixed_cells,
            "period_cell_count": period_cells,
            "directly_enumerated_configurations": brute_configurations,
            "boundary_m1": {"total": 4, "exact_period_one": 4, "short": 0, "T_is_identity": True},
            "boundary_m2": {"total": 16, "exact_period_one": 4, "exact_period_two": 12, "primitive_two_cycles": 6},
        },
        "progress_and_boundary": {
            "progress": "pivots from an overused Rule-90 lineage to a two-phase partitioned cellular automaton and proves a full all-size conjugacy, period law, concentration estimate, reversor, and Koopman determinant",
            "route_a_obstruction": "the exact finite source determinant has no target divisor or global target-analytic comparison and the finite Koopman lift is not a Hilbert--Polya construction",
        },
        "route_a": {
            "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
            "overall": "ROUTE_A_EXPLORATORY",
            "A1_qualification": "ALL_M_EXACT_NECKLACE_PERIOD_LAW_FOR_A_REVERSIBLE_PARTITIONED_CA",
            "A2_qualification": "EXACT_FINITE_SOURCE_ZETA_WITH_NO_TARGET_DIVISOR_COMPARISON",
            "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_OR_CONTINUATION_COMPARISON",
            "A4_qualification": "SAME_CLOCK_FINITE_KOOPMAN_UNITARY_WITH_EXPLICIT_ANTIUNITARY_REVERSAL",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": {
            "scope": "NO_BAD_EULER_OR_ROOT_NUMBER",
            "uses_prime_table": False,
            "uses_zero_table": False,
            "claims_arithmetic_euler_factors": False,
            "claims_root_number": False,
            "claims_automorphy": False,
            "claims_hilbert_polya": False,
            "claims_chaos_or_interaction": False,
            "uses_route_b_inputs": False,
        },
        "nonclaims": [
            "chaos or interaction in a system conjugate to a four-letter rotation",
            "a target divisor, functional equation, or counting-law match",
            "arithmetic local factors, Euler factors, root numbers, or automorphy",
            "a uniform self-adjoint Hilbert--Polya realization across the family",
            "Route-B authorization or a solution of the larger program",
        ],
    }
    data["payload_sha256"] = sha256(payload_bytes(data)).hexdigest()
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    replay = data["finite_replay"]
    print(json.dumps({
        "status": "C165_PRODUCER_PASS",
        "output": str(args.output),
        "payload_sha256": data["payload_sha256"],
        "family_rows": len(replay["family_rows"]),
        "fixed_cells": replay["fixed_cell_count"],
        "period_cells": replay["period_cell_count"],
        "brute_configurations": replay["directly_enumerated_configurations"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
