#!/usr/bin/env python3
"""Produce exact periodic data for the one-vertex N-loop edge-type Dyck shift."""
from __future__ import annotations

import hashlib
import itertools
import json
import math
import os
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(os.environ.get("C205_OUTPUT", ROOT / "results" / "c205_dyck_shift_evidence.json"))
N_VALUES = range(1, 7)
MAX_PERIOD = 24
DIRECT_LIMITS = {1: 10, 2: 7, 3: 5, 4: 4, 5: 4, 6: 3}


def divisors(n: int) -> list[int]: return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n: int) -> int:
    m, primes, p = n, 0, 2
    while p * p <= m:
        if m % p == 0:
            m //= p; primes += 1
            if m % p == 0: return 0
            while m % p == 0: m //= p
        p += 1
    if m > 1: primes += 1
    return -1 if primes % 2 else 1


def fixed_formula(N: int, n: int) -> int:
    """Krieger--Matsumoto coefficient formula for origin-marked points."""
    if n % 2:
        cutoff = (n - 1) // 2
        return 2 * ((N + 1) ** n - sum(math.comb(n, j) * N ** j for j in range(cutoff + 1)))
    cutoff = n // 2
    return (2 * ((N + 1) ** n - sum(math.comb(n, j) * N ** j for j in range(cutoff + 1)))
            + math.comb(n, cutoff) * N ** cutoff)


def reduction_nonzero(word: tuple[tuple[int, int], ...] | list[tuple[int, int]]) -> bool:
    """Dyck inverse-monoid reduction: open_i close_j=delta_ij."""
    stack: list[tuple[int, int]] = []
    for sign, colour in word:
        if sign == 1 and stack and stack[-1][0] == 0:
            if stack[-1][1] != colour:
                return False
            stack.pop()
        else:
            stack.append((sign, colour))
    return True


def periodic_word_admissible(word: tuple[tuple[int, int], ...]) -> bool:
    """Audit every cyclic factor through length 2n in the periodic extension."""
    n = len(word); extension = word * 3
    return all(reduction_nonzero(extension[start:start + length])
               for start in range(n) for length in range(1, 2 * n + 1))


def direct_fixed(N: int, n: int) -> int:
    alphabet = tuple((sign, colour) for sign in (0, 1) for colour in range(N))
    return sum(periodic_word_admissible(word) for word in itertools.product(alphabet, repeat=n))


def record(N: int) -> dict:
    fixed = {str(n): fixed_formula(N, n) for n in range(1, MAX_PERIOD + 1)}
    primitive, cycles = {}, {}
    for n in range(1, MAX_PERIOD + 1):
        p = sum(mobius(n // d) * fixed[str(d)] for d in divisors(n))
        assert p >= 0 and p % n == 0
        primitive[str(n)], cycles[str(n)] = p, p // n
    direct = {}
    for n in range(1, DIRECT_LIMITS[N] + 1):
        value = direct_fixed(N, n)
        assert value == fixed[str(n)]
        direct[str(n)] = value
    if N == 1:
        assert all(fixed[str(n)] == 2 ** n for n in range(1, MAX_PERIOD + 1))
        singularity = {
            "boundary_case": "zeta_1(z)=1/(1-2z), the full two-shift zeta",
            "dominant_pole": "1/2",
            "pole_order": 1,
            "branchpoints_cancel": True,
        }
    else:
        r = Fraction(1, N + 1)
        singularity = {
            "dominant_pole": f"{r.numerator}/{r.denominator}",
            "pole_order": 2,
            "square_root_at_pole": f"{N-1}/{N+1}",
            "branchpoints": [f"-1/(2*sqrt({N}))", f"1/(2*sqrt({N}))"],
            "dominance_gap": f"{N+1}>2*sqrt({N})",
            "nonrational": True,
            "fixed_asymptotic": f"Fix_n=2*{N+1}^n+O((2*sqrt({N}))^n/sqrt(n))",
            "primitive_cycle_asymptotic": f"C_n~2*{N+1}^n/n",
        }
    return {
        "N": N,
        "topological_entropy": f"log({N+1})",
        "periodic_point_exponential_growth": f"lim_(n->infinity) log(Fix_n)/n=log({N+1})",
        "entropy_source_lock": "Krieger--Matsumoto Proposition 3.1 identifies entropy with periodic-point growth for Markov-Dyck shifts",
        "fixed_points": fixed,
        "primitive_points": primitive,
        "primitive_orbits": cycles,
        "direct_periodic_word_audit": direct,
        "singularity_and_asymptotic": singularity,
    }


def main() -> None:
    records = [record(N) for N in N_VALUES]
    payload = {
        "schema": "hcs-c205-edge-dyck-v1",
        "package_id": "HCS-C205",
        "generated_utc": "2026-08-27T00:00:00Z",
        "source_commit": "d108ef46fea7a8f62490a69071a83fcbda7c113b",
        "evaluator_sha256": "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c",
        "scope_guard": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "source_records": [
            {
                "authors": "W. Krieger and K. Matsumoto",
                "title": "Zeta functions and topological entropy of the Markov-Dyck shifts",
                "journal": "Muenster Journal of Mathematics",
                "volume": 4,
                "year": 2011,
                "pages": "171-184",
                "arxiv": "0706.3262",
                "official_pdf": "https://www.uni-muenster.de/FB10/mjm/vol_4/mjm_vol_4_10.pdf",
                "pagination_note": "official Muenster volume PDF controls; an arXiv journal-reference entry reports 171-185",
                "role": "source theorem and one-vertex specialization",
            },
            {
                "author": "G. Keller",
                "title": "Circular codes, loop counting, and zeta-functions",
                "journal": "Journal of Combinatorial Theory, Series A",
                "volume": 56,
                "issue": 1,
                "year": 1991,
                "pages": "75-83",
                "doi": "10.1016/0097-3165(91)90023-A",
                "role": "primary circular-code context",
            },
        ],
        "model_convention": {
            "system": "edge-type Dyck shift of the one-vertex graph with N loop edges",
            "alphabet": "open_i,close_i for 1<=i<=N",
            "relation": "open_i close_j = identity if i=j and zero otherwise",
            "fixed_point_convention": "Fix(sigma^n) counts origin-marked n-periodic bi-infinite sequences, equivalently admissible length-n periodic words",
            "orbit_convention": "primitive origin-marked words are divided by n only after Mobius inversion",
            "finite_audit_rule": "by periodic normal-form reduction, w^infinity is admissible iff all cyclic factors of lengths 1..2n reduce nonzero",
        },
        "theorem_contract": {
            "circular_code_equation": "g_N(z)=N*z^2/(1-g_N(z))",
            "catalan_series": "g_N(z)=(1-sqrt(1-4*N*z^2))/2",
            "circular_code_zeta": "zeta_N(z)=(1-g_N(z))/(1-N*z-g_N(z))^2",
            "zeta": "zeta_N(z)=2*(1+sqrt(1-4*N*z^2))/(1+sqrt(1-4*N*z^2)-2*N*z)^2",
            "odd_fixed": "2*((N+1)^n-sum_{j=0}^{(n-1)/2} binom(n,j)N^j)",
            "even_fixed": "2*((N+1)^n-sum_{j=0}^{n/2} binom(n,j)N^j)+binom(n,n/2)N^(n/2)",
            "primitive_points": "P_n=sum_{d|n}mu(n/d)Fix_d",
            "primitive_orbits": "C_n=P_n/n",
            "topological_entropy": "h_top(D_N^E)=log(N+1), using Krieger--Matsumoto Proposition 3.1 and periodic-point growth",
        },
        "coverage": {
            "N_range": [1, 6],
            "period_range": [1, MAX_PERIOD],
            "formula_cells": len(records) * MAX_PERIOD,
            "direct_audit_cells": sum(DIRECT_LIMITS.values()),
            "entropy_cells": len(records),
        },
        "records": records,
        "route_a": {
            "tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "reason": "The algebraic symbolic zeta has no certified identification with target local arithmetic or a Hilbert--Polya operator.",
        },
        "claim_flags": {
            "target_local_factors_computed": False,
            "target_root_numbers_computed": False,
            "automorphy_claimed": False,
            "hilbert_polya_operator_claimed": False,
            "literature_priority_claimed": False,
        },
    }
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["semantic_payload_sha256"] = hashlib.sha256(raw).hexdigest()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {OUT}")
    print(f"semantic_payload_sha256={payload['semantic_payload_sha256']}")
    print(f"formula_cells={len(records)*MAX_PERIOD} direct_cells={sum(DIRECT_LIMITS.values())}")


if __name__ == "__main__": main()
