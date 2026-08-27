#!/usr/bin/env python3
"""Produce the exact HCS-C190 Bulgarian-solitaire recurrent certificate."""
from __future__ import annotations

import argparse
from itertools import combinations
from hashlib import sha256
import json
from math import comb, gcd
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c190_bulgarian_necklace_evidence.json"
SOURCE_COMMIT = "4d7b214759f7ff982c0b19e662918acd307e0f58"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
N_MIN = 1
N_MAX = 40
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"


SOURCE_LOCK = {
    "object": "noninvertible Bulgarian-solitaire map T_N on the integer partitions P(N)",
    "family": "every integer N>=1, uniquely N=binom(k,2)+r with 0<=r<k",
    "phase_space": "the full finite partition set P(N), with the Brandt recurrent subset marked inside it",
    "clock": "one Bulgarian move: remove one card from every pile and form a new pile from the removed cards",
    "measure": "counting measure on P(N), and counting measure on the recurrent subset",
    "recurrent_model": "length-k weight-r binary words; w maps to positive parts of (k-1,k-2,...,0)+w",
    "rotation_convention": "T_N corresponds to right rotation rho(w)_i=w_(i-1 mod k)",
    "operator": "full finite Koopman pullback U_N f=f composed with T_N and its recurrent permutation restriction",
    "determinant_convention": "Artin--Mazur zeta of the full finite map and reciprocal det(I-z U_N)",
    "cutoff": "all-N attributed recurrent theorem; exact finite regression only for 1<=N<=40",
    "allowed_data": "integer partitions, binary words, rotations, reflections, exact divisor sums, and partition numbers",
    "forbidden_data": "target zero or prime tables, arithmetic local data, Euler factors, root numbers, automorphy, Hilbert--Polya operators, and Route-B inputs",
}

ATTRIBUTION = {
    "status": "SOURCE_DERIVED_SYNTHESIS_NOT_NEW_THEOREM_CLAIM",
    "recurrent_owner": "Brandt 1982 owns the all-N characterization of cyclic partitions and its binary-necklace parametrization",
    "dynamical_background": "Akin and Davis 1985 give a classical treatment of Bulgarian solitaire and the recurrent classification",
    "package_increment": "source-locked closure of every iterate fixed count, Mobius least periods and cycles, full finite zeta, full Koopman algebraic spectrum, recurrent reflection reversal, and triangular boundary",
    "finite_evidence_role": "the N<=40 word and full-partition census is regression evidence only and does not prove the all-N recurrent theorem",
}

THEOREM = {
    "decomposition": "every N>=1 has unique N=binom(k,2)+r with integers k>=2 and 0<=r<k",
    "recurrent_bijection": "Brandt recurrent partitions are exactly phi(w)=positive parts of (k-1,...,0)+w for length-k weight-r binary words, and T_N phi=phi rho",
    "fixed_count": "with g=gcd(k,t), Fix(T_N^t)=binom(g,r*g/k) if k/g divides r and is zero otherwise",
    "exact_period": "for every d|k, P_d=sum_(e|d) mu(d/e) Fix(T_N^e) and C_d=P_d/d",
    "zeta": "zeta_T(z)=product_(d|k)(1-z^d)^(-C_d) for the full noninvertible finite map",
    "koopman": "det(I-z U_N)=product_(d|k)(1-z^d)^(C_d); zero has algebraic multiplicity p(N)-binom(k,r), and mult(exp(2*pi*i*j/k))=sum_(d|k,k|j*d) C_d",
    "trace": "Tr(U_N^t)=Fix(T_N^t) for every t>=1",
    "reversor": "on the recurrent core Q(w)_i=w_(-i mod k) is an involution with Q rho Q=rho^(-1); rho^a Q gives k phase-labelled reflection formulas, not necessarily distinct on a nonfaithful weight layer",
    "triangular_boundary": "if r=0 the recurrent core is the single staircase (k-1,...,1), with zeta (1-z)^(-1) and recurrent Koopman eigenvalue one",
}

PROGRESS_AND_BOUNDARY = {
    "progress": "one all-N theorem package closes the periodic core, every fixed iterate, primitive cycles, full finite zeta, algebraic Koopman spectrum, recurrent reflection reversal, and triangular family",
    "transient_boundary": "complete transient functional trees, exact hitting-time distributions, and nilpotent Jordan block sizes are outside the claim",
    "noninvertible_boundary": "T_N is not globally invertible in general, so reflection reversal is asserted only on the recurrent core",
    "proof_boundary": "Brandt's all-N recurrent characterization is imported with attribution; the finite census regression-tests consequences rather than proving it",
    "arithmetic_boundary": "deck size, pile sizes, word weights, rotations, and partition numbers have no intrinsic rational-prime or prime-power semantics",
    "operator_boundary": "the full Koopman map is finite and nonunitary; its recurrent unitary restriction is only a formal operator hint and no Hilbert--Polya claim",
}

ROUTE_A = {
    "tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
    "overall": "ROUTE_A_REJECTED",
    "A0_qualification": "PARTITIONS_AND_BINARY_NECKLACES_HAVE_NO_INTRINSIC_RATIONAL_PRIME_ORIGIN",
    "A1_qualification": "RECURRENT_PRIMITIVE_CYCLES_ARE_COMPLETE_BUT_CARRY_NO_A0_ARITHMETIC_PAYLOAD",
    "A2_qualification": "FINITE_SOURCE_ZETA_AND_KOOPMAN_DETERMINANT_HAVE_NO_TARGET_DIVISOR_MATCH",
    "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_CONTINUATION_OR_WEIL_COMPRESSION",
    "A4_qualification": "RECURRENT_FINITE_PERMUTATION_SPECTRUM_IS_A_FORMAL_HINT_ONLY_NOT_A_TARGET_QUANTIZATION",
    "route_b_invocation_allowed": False,
}

SCOPE_FLAGS = {
    "used_target_zero_table": False,
    "used_target_prime_table": False,
    "used_arithmetic_local_data": False,
    "claimed_target_divisor_match": False,
    "claimed_target_functional_equation": False,
    "claimed_hilbert_polya": False,
    "claimed_global_reversor": False,
    "claimed_complete_transient_classification": False,
    "claimed_global_novelty": False,
    "route_b_invocation_allowed": False,
}

SOURCE_REGISTRY = [
    {
        "key": "brandt_1982_cycles_partitions",
        "title": "Cycles of partitions",
        "authors": "Jorgen Brandt",
        "year": 1982,
        "journal": "Proceedings of the American Mathematical Society 85(3), 483--486",
        "doi": "10.1090/S0002-9939-1982-0656129-5",
        "role": "primary ownership for the cyclic-partition characterization and necklace model",
    },
    {
        "key": "akin_davis_1985_bulgarian_solitaire",
        "title": "Bulgarian Solitaire",
        "authors": "Ethan Akin and Morton Davis",
        "year": 1985,
        "journal": "The American Mathematical Monthly 92(4), 237--250",
        "doi": "10.1080/00029890.1985.11971590",
        "jstor_doi": "10.2307/2323643",
        "role": "classical dynamical treatment and recurrent-set background",
    },
]

NONCLAIMS = [
    "novelty or priority for Brandt's recurrent classification, necklace parametrization, or Bulgarian-solitaire convergence theory",
    "a complete classification of transient functional trees, hitting times, or nilpotent Koopman Jordan blocks",
    "a global reversor for the noninvertible map on all partitions",
    "rational-prime semantics for deck sizes, partitions, binary words, cycle lengths, or partition numbers",
    "a target divisor, functional equation, counting law, continuation theorem, or Weil compression",
    "a self-adjoint Hilbert--Polya operator, Route-B authorization, external peer review, or acceptance score",
]


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n: int) -> int:
    if n == 1:
        return 1
    answer = 1
    prime = 2
    value = n
    while prime * prime <= value:
        if value % prime == 0:
            value //= prime
            answer = -answer
            if value % prime == 0:
                return 0
            while value % prime == 0:
                value //= prime
        prime += 1
    if value > 1:
        answer = -answer
    return answer


def parameters(n: int) -> tuple[int, int]:
    k = 2
    while (k + 1) * k // 2 <= n:
        k += 1
    r = n - k * (k - 1) // 2
    assert 0 <= r < k
    return k, r


def partition_number(n: int) -> int:
    counts = [0] * (n + 1)
    counts[0] = 1
    for part in range(1, n + 1):
        for total in range(part, n + 1):
            counts[total] += counts[total - part]
    return counts[n]


def weight_words(k: int, r: int) -> list[str]:
    result: list[str] = []
    for positions in combinations(range(k), r):
        bits = ["0"] * k
        for position in positions:
            bits[position] = "1"
        result.append("".join(bits))
    return sorted(result)


def phi(word: str) -> list[int]:
    k = len(word)
    return [k - index - 1 + int(bit) for index, bit in enumerate(word) if k - index - 1 + int(bit) > 0]


def rotate_right(word: str, amount: int = 1) -> str:
    amount %= len(word)
    return word[-amount:] + word[:-amount] if amount else word


def reflect(word: str) -> str:
    return "".join(word[(-index) % len(word)] for index in range(len(word)))


def fixed_formula(k: int, r: int, iterate: int) -> int:
    g = gcd(k, iterate)
    block = k // g
    if r % block:
        return 0
    return comb(g, r // block)


def word_cycles(words: list[str]) -> list[dict]:
    remaining = set(words)
    cycles: list[dict] = []
    while remaining:
        seed = min(remaining)
        orbit: list[str] = []
        current = seed
        while current not in orbit:
            orbit.append(current)
            current = rotate_right(current)
        canonical = min(orbit)
        while orbit[0] != canonical:
            orbit = orbit[1:] + orbit[:1]
        remaining.difference_update(orbit)
        cycles.append({
            "canonical_word": canonical,
            "length": len(orbit),
            "words": orbit,
            "partitions": [phi(word) for word in orbit],
        })
    return sorted(cycles, key=lambda row: (row["length"], row["canonical_word"]))


def canonical_bytes(data: dict) -> bytes:
    body = dict(data)
    body.pop("payload_sha256", None)
    return json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def build() -> dict:
    rows: list[dict] = []
    total_words = 0
    total_fixed_rows = 0
    total_period_rows = 0
    total_spectral_rows = 0
    total_cycles = 0
    total_partitions = 0

    for n in range(N_MIN, N_MAX + 1):
        k, r = parameters(n)
        words = weight_words(k, r)
        recurrent_count = comb(k, r)
        assert len(words) == recurrent_count
        p_n = partition_number(n)
        total_partitions += p_n

        pairs = []
        for word in words:
            successor = rotate_right(word)
            mirror = reflect(word)
            pairs.append({
                "word": word,
                "partition": phi(word),
                "next_word": successor,
                "next_partition": phi(successor),
                "reflection_word": mirror,
                "reflection_partition": phi(mirror),
            })

        cycles = word_cycles(words)
        cycle_counter: dict[int, int] = {}
        for cycle in cycles:
            cycle_counter[cycle["length"]] = cycle_counter.get(cycle["length"], 0) + 1
        assert sum(length * count for length, count in cycle_counter.items()) == recurrent_count

        fixed_rows = []
        for iterate in range(k):
            formula = fixed_formula(k, r, iterate)
            enumeration = sum(rotate_right(word, iterate) == word for word in words)
            assert formula == enumeration
            fixed_rows.append({
                "iterate_mod_k": iterate,
                "positive_iterate_representative": k if iterate == 0 else iterate,
                "gcd_k_iterate": gcd(k, iterate),
                "fixed_count": formula,
            })

        period_rows = []
        for period in divisors(k):
            exact = sum(
                mobius(period // divisor) * fixed_formula(k, r, divisor)
                for divisor in divisors(period)
            )
            assert exact >= 0 and exact % period == 0
            cycle_count = exact // period
            assert cycle_count == cycle_counter.get(period, 0)
            period_rows.append({
                "period": period,
                "fixed_at_period": fixed_formula(k, r, period),
                "exact_period_count": exact,
                "cycle_count": cycle_count,
            })
        assert sum(row["exact_period_count"] for row in period_rows) == recurrent_count

        spectral_rows = []
        for exponent in range(k):
            multiplicity = sum(
                row["cycle_count"]
                for row in period_rows
                if (exponent * row["period"]) % k == 0
            )
            spectral_rows.append({
                "root_exponent_mod_k": exponent,
                "multiplicity": multiplicity,
            })
        assert sum(row["multiplicity"] for row in spectral_rows) == recurrent_count

        # The phase-zero reflection and each rho^a Q reverse rho.
        for word in words:
            assert reflect(reflect(word)) == word
            assert reflect(rotate_right(reflect(word))) == rotate_right(word, -1)
            for phase in range(k):
                q_word = rotate_right(reflect(word), phase)
                twice = rotate_right(reflect(q_word), phase)
                assert twice == word

        nonzero_periods = [row for row in period_rows if row["cycle_count"]]
        rows.append({
            "N": n,
            "k": k,
            "r": r,
            "triangular_base": k * (k - 1) // 2,
            "partition_number": p_n,
            "recurrent_count": recurrent_count,
            "transient_count": p_n - recurrent_count,
            "full_koopman_zero_algebraic_multiplicity": p_n - recurrent_count,
            "word_partition_pairs": pairs,
            "cycles": cycles,
            "fixed_rows": fixed_rows,
            "period_rows": period_rows,
            "spectral_rows": spectral_rows,
            "zeta_factors": [
                {"period": row["period"], "exponent": -row["cycle_count"]}
                for row in nonzero_periods
            ],
            "koopman_determinant_factors": [
                {"period": row["period"], "exponent": row["cycle_count"]}
                for row in nonzero_periods
            ],
            "phase_reflection_formula_count": k,
            "triangular_boundary": r == 0,
        })
        total_words += len(words)
        total_fixed_rows += len(fixed_rows)
        total_period_rows += len(period_rows)
        total_spectral_rows += len(spectral_rows)
        total_cycles += len(cycles)

    # Fixed negative/positive controls used by every validation path.
    sentinel = rows[7]
    assert (sentinel["N"], sentinel["k"], sentinel["r"]) == (8, 4, 2)
    assert [(row["period"], row["cycle_count"]) for row in sentinel["period_rows"] if row["cycle_count"]] == [(2, 1), (4, 1)]
    assert [row["fixed_count"] for row in sentinel["fixed_rows"]] == [6, 0, 2, 0]

    data = {
        "schema": "HCS-C190-v1",
        "candidate_id": "HCS-C190",
        "date_utc": "2026-08-27",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "evaluator": {
            "path": "flow_systems/skills/route-a-evaluator.md",
            "version": "0.2.0",
            "sha256": EVALUATOR_SHA256,
        },
        "source_lock": SOURCE_LOCK,
        "attribution": ATTRIBUTION,
        "theorem": THEOREM,
        "progress_and_boundary": PROGRESS_AND_BOUNDARY,
        "finite_replay": {
            "n_min": N_MIN,
            "n_max": N_MAX,
            "system_row_count": len(rows),
            "partition_population": total_partitions,
            "word_partition_pair_count": total_words,
            "cycle_row_count": total_cycles,
            "fixed_row_count": total_fixed_rows,
            "period_row_count": total_period_rows,
            "spectral_row_count": total_spectral_rows,
            "rows": rows,
        },
        "route_a": ROUTE_A,
        "scope_flags": SCOPE_FLAGS,
        "source_registry": SOURCE_REGISTRY,
        "nonclaims": NONCLAIMS,
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
    replay = data["finite_replay"]
    print(json.dumps({
        "status": "C190_PRODUCER_PASS",
        "systems": replay["system_row_count"],
        "partitions": replay["partition_population"],
        "recurrent_words": replay["word_partition_pair_count"],
        "cycles": replay["cycle_row_count"],
        "fixed_rows": replay["fixed_row_count"],
        "period_rows": replay["period_row_count"],
        "spectral_rows": replay["spectral_row_count"],
        "payload_sha256": data["payload_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
