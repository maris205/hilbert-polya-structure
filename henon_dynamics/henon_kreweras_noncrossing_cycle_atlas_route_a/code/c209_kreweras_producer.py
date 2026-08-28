#!/usr/bin/env python3
"""Produce the source-locked HCS-C209 Kreweras cycle atlas.

The producer deliberately contains only closed finite combinatorics.  The
all-n fixed-point row is the type-A ordinary Kreweras CSP, while periods,
cycles, the finite zeta and the Koopman spectrum are exact consequences of
the fixed row.  No arithmetic target data are read.
"""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from math import comb, gcd
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c209_kreweras_evidence.json"
SOURCE_COMMIT = "e8054522273dbd545f9d406978e5d4648c627918"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
N_MAX = 24
QCAT_MAX = 12
DIRECT_N_MAX = 8


def divisors(n: int) -> list[int]:
    small: list[int] = []
    large: list[int] = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            small.append(d)
            if d * d != n:
                large.append(n // d)
        d += 1
    return small + large[::-1]


def mobius(n: int) -> int:
    """The square-free Mobius function, implemented without sympy."""
    if n == 1:
        return 1
    value = n
    sign = 1
    p = 2
    while p * p <= value:
        if value % p == 0:
            value //= p
            sign = -sign
            if value % p == 0:
                return 0
            while value % p == 0:
                value //= p
        p += 1
    if value > 1:
        sign = -sign
    return sign


def catalan(n: int) -> int:
    return comb(2 * n, n) // (n + 1)


def clock_order(n: int) -> int:
    # K^2 is one-step rotation.  n=1 is a singleton and n=2 is the
    # discrete/indiscrete transposition; these are the two degeneracies.
    return 1 if n == 1 else 2 if n == 2 else 2 * n


def csp_group_order(n: int) -> int:
    """Order of the abstract cyclic group used by the Kreweras CSP.

    For n=2 the action has a kernel of order two, so its permutation order
    is two although the standard order-2n CSP is evaluated at fourth roots.
    """
    return 1 if n == 1 else 2 * n


def fixed_formula(n: int, d: int) -> int:
    """Type-A ordinary Kreweras CSP fixed count for any integer d."""
    L = clock_order(n)
    d %= L
    if n == 1:
        return 1
    if d % 2 == 0:
        r = (d // 2) % n
        if r == 0:
            return catalan(n)
        g = gcd(n, r)
        return comb(2 * g, g)
    if n % 2 == 1 and d == n:
        return comb(n, (n - 1) // 2)
    return 0


def exact_periods(n: int) -> dict[int, int]:
    L = clock_order(n)
    result: dict[int, int] = {}
    for ell in divisors(L):
        value = sum(mobius(ell // d) * fixed_formula(n, d) for d in divisors(ell))
        if value < 0 or value % ell:
            raise AssertionError(f"invalid Mobius inversion n={n}, ell={ell}: {value}")
        result[ell] = value
    if sum(result.values()) != catalan(n):
        raise AssertionError("period populations do not sum to Catalan cardinality")
    return result


def qtrim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def qmul(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return qtrim(out)


def qdiv_exact(numerator: list[int], denominator: list[int]) -> list[int]:
    work = qtrim(numerator[:])
    denominator = qtrim(denominator[:])
    if denominator[-1] not in (1, -1):
        raise AssertionError("q-division requires unit leading coefficient")
    quotient = [0] * max(1, (len(work) - len(denominator) + 1))
    while work != [0] and len(work) >= len(denominator):
        shift = len(work) - len(denominator)
        lead = work[-1] // denominator[-1]
        quotient[shift] += lead
        for i, b in enumerate(denominator):
            work[i + shift] -= lead * b
        qtrim(work)
    if any(work):
        raise AssertionError("non-exact q-polynomial quotient")
    return qtrim(quotient)


def qint(n: int) -> list[int]:
    return [1] * n


def qfactorial(n: int) -> list[int]:
    out = [1]
    for j in range(1, n + 1):
        out = qmul(out, qint(j))
    return out


def q_catalan(n: int) -> list[int]:
    if n == 1:
        return [1]
    return qdiv_exact(qfactorial(2 * n), qmul(qfactorial(n), qfactorial(n + 1)))


def coefficient_hash(coefficients: list[int]) -> str:
    return sha256(json.dumps(coefficients, separators=(",", ":")).encode()).hexdigest()


def canonical_bytes(data: dict) -> bytes:
    body = dict(data)
    body.pop("payload_sha256", None)
    return json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def build() -> dict:
    n_rows: list[dict] = []
    fixed_rows: list[dict] = []
    period_rows: list[dict] = []
    spectral_rows: list[dict] = []
    rank_rows: list[dict] = []
    q_rows: list[dict] = []
    structural_rows: list[dict] = []

    for n in range(1, N_MAX + 1):
        L = clock_order(n)
        cat = catalan(n)
        periods = exact_periods(n)
        cycles = {str(ell): periods[ell] // ell for ell in periods}
        nonzero = [ell for ell in periods if periods[ell]]
        spectrum: list[int] = []
        for d in range(L):
            fixed_rows.append({
                "n": n,
                "iterate": d,
                "iterate_mod_order": d,
                "gcd_n_half_iterate": gcd(n, d // 2) if d % 2 == 0 else None,
                "parity": "even" if d % 2 == 0 else "odd",
                "fixed_count": fixed_formula(n, d),
            })
        for ell in divisors(L):
            period_rows.append({
                "n": n,
                "period": ell,
                "fixed_at_period": fixed_formula(n, ell),
                "exact_period_population": periods[ell],
                "cycle_count": periods[ell] // ell,
            })
        for k in range(L):
            multiplicity = sum(
                periods[ell] // ell
                for ell in periods
                if (k * ell) % L == 0
            )
            spectrum.append(multiplicity)
            spectral_rows.append({
                "n": n,
                "clock_order": L,
                "root_exponent": k,
                "multiplicity": multiplicity,
            })
        if sum(spectrum) != cat:
            raise AssertionError("spectral multiplicities do not sum to Cat_n")

        # Narayana rank ledger: rank r=n-b has N(n,b) elements.  It is
        # included as a structural control for the order-reversing property,
        # not as a second dynamical model.
        ranks: list[dict] = []
        for blocks in range(1, n + 1):
            count = comb(n, blocks) * comb(n, blocks - 1) // n
            rank = n - blocks
            ranks.append({"blocks": blocks, "rank": rank, "count": count})
            rank_rows.append({"n": n, "blocks": blocks, "rank": rank, "count": count})

        q_info = None
        if n <= QCAT_MAX:
            coeffs = q_catalan(n)
            if sum(coeffs) != cat:
                raise AssertionError("q-Catalan evaluation at one failed")
            q_info = {
                "coefficients": coeffs,
                "degree": len(coeffs) - 1,
                "sha256": coefficient_hash(coeffs),
                "convention": "Cat_n(q)=[2n]_q!/[n]_q![n+1]_q!",
                "csp_group_order": csp_group_order(n),
            }
            q_rows.append({"n": n, **q_info})

        structural_rows.append({
            "n": n,
            "actual_order": L,
            "csp_group_order": csp_group_order(n),
            "square_rotation_offset": 0 if n == 1 else -1,
            "rank_reversal": "blocks(K(pi))=n+1-blocks(pi)",
            "reflection_relation": "R_j K R_j=K^(-1) for j=0,...,n-1",
            "reflection_count": n,
            "direct_structural_check_selected": n <= DIRECT_N_MAX,
            "boundary": "singleton" if n == 1 else "two_point_kernel" if n == 2 else "generic_2n",
        })

        n_rows.append({
            "n": n,
            "catalan": cat,
            "clock_order": L,
            "csp_group_order": csp_group_order(n),
            "order_statement": "1" if n == 1 else "2" if n == 2 else "2n",
            "fixed_count_rows": L,
            "period_divisors": divisors(L),
            "nonzero_periods": nonzero,
            "cycle_count_total": sum(periods[ell] // ell for ell in periods),
            "cycle_ledger": [
                {"period": ell, "exact_period_population": periods[ell], "cycles": periods[ell] // ell}
                for ell in periods
            ],
            "zeta_factors": [{"period": ell, "exponent": -(periods[ell] // ell)} for ell in nonzero],
            "koopman_determinant_factors": [{"period": ell, "exponent": periods[ell] // ell} for ell in nonzero],
            "rank_ledger": ranks,
            "q_catalan": q_info,
            "direct_enumeration_selected": n <= DIRECT_N_MAX,
        })

    data = {
        "schema": "HCS-C209-v1",
        "candidate_id": "HCS-C209",
        "date_utc": "2026-08-28",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "evaluator": {
            "path": "flow_systems/skills/route-a-evaluator.md",
            "version": "0.2.0",
            "sha256": EVALUATOR_SHA256,
        },
        "source_lock": {
            "object": "ordinary noncrossing partitions NC(n) of a labelled n-gon",
            "family": "all integers n>=1",
            "phase_space": "the finite Catalan set NC(n), with refinement rank n minus number of blocks",
            "clock": "one application of K(pi)=cycles(p_pi^{-1} c), where c=(0 1 ... n-1) and p_pi cycles each block in increasing circular order; K^2 is relabelling i -> i-1",
            "measure": "counting measure on NC(n)",
            "operator": "finite Koopman permutation U_n f=f composed with K on ell2(NC(n))",
            "polynomial": "Cat_n(q)=[2n]_q!/[n]_q![n+1]_q!, the unshifted q-Catalan polynomial",
            "determinant_convention": "finite Artin--Mazur zeta of K and reciprocal finite Koopman determinant",
            "cutoff": "all-n source theorem; exact formula rows n<=24, q-polynomial rows n<=12, direct partition enumeration n<=8",
            "allowed_data": "set-partition incidences, Catalan/Narayana integers, binomial coefficients, roots of unity and finite permutation cycles",
            "forbidden_data": "target zero or prime tables, arithmetic local data, Euler factors, root numbers, automorphy, Hilbert--Polya operators, target divisors, and Route-B inputs",
        },
        "attribution": {
            "status": "SOURCE_DERIVED_SYNTHESIS_NOT_NEW_THEOREM_CLAIM",
            "nc_owner": "Kreweras 1972 owns ordinary noncrossing partitions and the complement construction",
            "rotation_csp_owner": "Reiner--Stanton--White 2004 prove the type-A rotation q-Catalan CSP",
            "kreweras_csp_owner": "The type-A order-2n Kreweras-complement CSP was verified by Dennis White (reported in Bessis--Reiner 2011; preprint 2007); this package does not claim priority",
            "package_increment": "source-locked all-n fixed ledger for K, exact-period/cycle/zeta/Koopman/reversor synthesis, with independent finite enumeration and symbolic checks",
            "finite_evidence_role": "enumeration is regression evidence and cannot prove the all-n source theorem",
        },
        "theorem": {
            "cardinality": "|NC(n)|=Cat_n=binom(2n,n)/(n+1)",
            "complement_definition": "K(pi) is the cycle partition of p_pi^{-1}c; K reverses refinement and blocks(K(pi))=n+1-blocks(pi)",
            "square": "K^2=rotation by -1; hence K commutes with rotation",
            "clock_order": "order(K)=1 for n=1, 2 for n=2, and 2n for every n>=3",
            "fixed_count": "For n>=2 and d modulo L_n (L_2=2, L_n=2n for n>=3): even d=2r gives Cat_n if r=0 and binom(2g,g) if g=gcd(n,r)>0; odd d gives binom(n,(n-1)/2) exactly when n is odd and d=n, otherwise 0",
            "csp": "Fix(K^d)=Cat_n(zeta_{2n}^d) under the ordinary type-A Kreweras CSP, with the n=1,2 action kernels treated separately",
            "exact_period": "P_{n,ell}=sum_{d|ell} mu(ell/d) Fix(K^d), ell|L_n",
            "cycle_count": "C_{n,ell}=P_{n,ell}/ell and sum_ell P_{n,ell}=Cat_n",
            "zeta": "zeta_{K,n}(z)=product_{ell|L_n}(1-z^ell)^(-C_{n,ell})",
            "koopman_determinant": "det(I-zU_n)=product_{ell|L_n}(1-z^ell)^(C_{n,ell})=zeta_{K,n}(z)^(-1)",
            "spectrum": "Spec(U_n) consists of L_n-th roots; mult(exp(2pi i k/L_n))=sum_{ell|L_n, L_n|k ell} C_{n,ell}, and Tr(U_n^d)=Fix(K^d)",
            "reversor": "polygon reflection R_j(i)=j-i satisfies R_j K R_j=K^{-1}; Jf=conjugate(f composed with R_j) is an antiunitary reversor",
            "rank_duality": "rank(K(pi))=n-1-rank(pi), with Narayana rank counts N(n,b)=binom(n,b)binom(n,b-1)/n",
        },
        "finite_replay": {
            "n_min": 1,
            "n_max": N_MAX,
            "q_catalan_max": QCAT_MAX,
            "direct_enumeration_n_max": DIRECT_N_MAX,
            "n_rows": n_rows,
            "fixed_rows": fixed_rows,
            "period_rows": period_rows,
            "spectral_rows": spectral_rows,
            "rank_rows": rank_rows,
            "q_catalan_rows": q_rows,
            "structural_rows": structural_rows,
            "n_row_count": len(n_rows),
            "fixed_row_count": len(fixed_rows),
            "period_row_count": len(period_rows),
            "spectral_row_count": len(spectral_rows),
            "rank_row_count": len(rank_rows),
            "q_catalan_row_count": len(q_rows),
            "structural_row_count": len(structural_rows),
        },
        "progress_and_boundary": {
            "progress": "one closed theorem package gives every iterate fixed count, exact periods/cycles, finite zeta, finite Koopman determinant/spectrum, rank duality and a dihedral reversor for ordinary NC(n)",
            "order_boundary": "the order is 1, 2, or 2n according to n; n=1 and n=2 are explicit degeneracies, so no blind uniform 2n assertion is made",
            "proof_boundary": "the all-n Kreweras CSP is imported with attribution; direct n<=8 enumeration and q-polynomial rows are regression checks only",
            "arithmetic_boundary": "n, Catalan/Narayana numbers and roots of unity are intrinsic combinatorial data with no rational-prime semantics",
            "operator_boundary": "the only operator is the finite Koopman permutation and its antiunitary reflection; no self-adjoint Hilbert--Polya conclusion is asserted",
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
            "overall": "ROUTE_A_REJECTED",
            "A0_qualification": "CATALAN_CLOCK_HAS_NO_INTRINSIC_RATIONAL_PRIME_ORIGIN",
            "A1_qualification": "FINITE_KREWERAS_CYCLES_ARE_INTRINSIC_BUT_NOT_PRIME_LIKE",
            "A2_qualification": "FINITE_ZETA_AND_KOOPMAN_DETERMINANT_HAVE_NO_TARGET_DIVISOR_MATCH",
            "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_CONTINUATION_OR_WEIL_COMPRESSION",
            "A4_qualification": "SOURCE_NATIVE_FINITE_KOOPMAN_PERMUTATION_UNITARY_SAME_CLOCK_COUNTING_NORMALIZATION_AND_REFLECTION_ANTIUNITARY_REVERSOR;_NON_SELF_ADJOINT_NO_ARITHMETIC_PHASE_OR_WEIGHT_NOT_HILBERT_POLYA",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": {
            "used_target_zero_table": False,
            "used_target_prime_table": False,
            "used_arithmetic_local_data": False,
            "claimed_target_divisor_match": False,
            "claimed_target_functional_equation": False,
            "claimed_hilbert_polya": False,
            "claimed_exact_order_n_uniformly": False,
            "claimed_global_novelty": False,
            "route_b_invocation_allowed": False,
        },
        "source_registry": [
            {
                "key": "kreweras_1972",
                "title": "Sur les partitions non croisées d'un cycle",
                "authors": "Germain Kreweras",
                "year": 1972,
                "journal": "Discrete Mathematics 1, 333--350",
                "doi": "10.1016/0012-365X(72)90041-6",
                "role": "original ordinary noncrossing-partition and complement source",
            },
            {
                "key": "reiner_stanton_white_2004",
                "title": "The cyclic sieving phenomenon",
                "authors": "Victor Reiner, Dennis Stanton, Dennis White",
                "year": 2004,
                "journal": "Journal of Combinatorial Theory, Series A 108, 17--50",
                "doi": "10.1016/j.jcta.2004.04.009",
                "role": "type-A rotation q-Catalan CSP and root-of-unity fixed-count calculations",
            },
            {
                "key": "bessis_reiner_2011_white_report",
                "title": "Cyclic sieving of noncrossing partitions for complex reflection groups",
                "authors": "David Bessis, Victor Reiner",
                "year": 2011,
                "journal": "Annals of Combinatorics 15(2), 197--222",
                "doi": "10.1007/s00026-011-0090-9",
                "arxiv": "math/0701792 (preprint 2007)",
                "role": "formal publication records the order-2n Kreweras-complement CSP as type-A m=1 and reports White's direct verification; used as attribution, not a novelty claim",
            },
        ],
        "nonclaims": [
            "priority for the Kreweras complement, q-Catalan CSP, Catalan/Narayana formulas, or dihedral action",
            "a proof of the all-n CSP from the finite n<=8 enumeration",
            "a uniform exact order 2n statement at n=1 or n=2",
            "rational-prime semantics, local arithmetic data, Euler factors, root numbers, or automorphy",
            "a target divisor, functional equation, continuation theorem, counting law, or Weil compression",
            "a self-adjoint Hilbert--Polya operator, Route-B authorization, external peer-review score, or acceptance claim",
        ],
    }
    data["payload_sha256"] = sha256(canonical_bytes(data)).hexdigest()
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    finite = data["finite_replay"]
    print(json.dumps({
        "status": "C209_PRODUCER_PASS",
        "n_rows": finite["n_row_count"],
        "fixed_rows": finite["fixed_row_count"],
        "period_rows": finite["period_row_count"],
        "spectral_rows": finite["spectral_row_count"],
        "rank_rows": finite["rank_row_count"],
        "q_catalan_rows": finite["q_catalan_row_count"],
        "structural_rows": finite["structural_row_count"],
        "payload_sha256": data["payload_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
