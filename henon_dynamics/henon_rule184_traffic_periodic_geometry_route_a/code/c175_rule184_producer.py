#!/usr/bin/env python3
"""Produce the exact HCS-C175 cyclic Rule-184 certificate."""
from __future__ import annotations

import argparse
from hashlib import sha256
from itertools import product
import json
from math import comb, gcd
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c175_rule184_evidence.json"
SOURCE_COMMIT = "100e5f601a0196710d53784bdeef40d2bff89fa8"
N_MAX = 12


def canonical_bytes(data: dict) -> bytes:
    body = dict(data)
    body.pop("payload_sha256", None)
    return json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def step(word: tuple[int, ...]) -> tuple[int, ...]:
    n = len(word)
    return tuple(
        word[(i - 1) % n] * (1 - word[i]) + word[i] * word[(i + 1) % n]
        for i in range(n)
    )


def iterate(word: tuple[int, ...], n: int) -> tuple[int, ...]:
    out = word
    for _ in range(n):
        out = step(out)
    return out


def no_adjacent(word: tuple[int, ...], symbol: int) -> bool:
    n = len(word)
    return all(not (word[i] == symbol and word[(i + 1) % n] == symbol) for i in range(n))


def in_periodic_core(word: tuple[int, ...]) -> bool:
    n = len(word)
    k = sum(word)
    if 2 * k <= n:
        return no_adjacent(word, 1)
    return no_adjacent(word, 0)


def core_entry_time(word: tuple[int, ...]) -> int:
    out = word
    for t in range(len(word) * len(word) + 1):
        if in_periodic_core(out):
            return t
        out = step(out)
    raise AssertionError("finite-attraction sentinel exceeded N^2")


def independent_cycle_count(n: int, r: int) -> int:
    if r == 0:
        return 1
    if r < 0 or r > n // 2:
        return 0
    return n * comb(n - r, r) // (n - r)


def fixed_formula(n_sites: int, particles: int, iterate_n: int) -> int:
    minority = min(particles, n_sites - particles)
    g = gcd(n_sites, iterate_n)
    q = n_sites // g
    if minority % q:
        return 0
    return independent_cycle_count(g, minority // q)


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n: int) -> int:
    value = n
    primes = 0
    p = 2
    while p * p <= value:
        if value % p == 0:
            value //= p
            if value % p == 0:
                return 0
            primes += 1
            while value % p == 0:
                value //= p
        p += 1
    if value > 1:
        primes += 1
    return -1 if primes % 2 else 1


def exact_period(word: tuple[int, ...]) -> int | None:
    if not in_periodic_core(word):
        return None
    out = word
    for period in range(1, len(word) + 1):
        out = step(out)
        if out == word:
            return period
    raise AssertionError("core rotation did not close by N")


def branch(n: int, k: int) -> str:
    if k == 0 or k == n:
        return "uniform_fixed"
    if 2 * k < n:
        return "low_density_no_11_right_rotation"
    if 2 * k > n:
        return "high_density_no_00_left_rotation"
    return "balanced_two_alternating_states"


def build() -> dict:
    sector_rows: list[dict] = []
    fixed_rows: list[dict] = []
    primitive_rows: list[dict] = []
    classified_words = 0
    fixed_word_iterate_checks = 0
    maximum_observed_entry_time = 0

    for n_sites in range(1, N_MAX + 1):
        words_by_k = {k: [] for k in range(n_sites + 1)}
        for word in product((0, 1), repeat=n_sites):
            words_by_k[sum(word)].append(word)
        for particles in range(n_sites + 1):
            words = words_by_k[particles]
            minority = min(particles, n_sites - particles)
            core_words = [word for word in words if in_periodic_core(word)]
            entry_times = [core_entry_time(word) for word in words]
            maximum_observed_entry_time = max(maximum_observed_entry_time, max(entry_times))
            classified_words += len(words)
            core_formula = independent_cycle_count(n_sites, minority)
            assert len(core_words) == core_formula
            assert max(entry_times) <= minority * minority
            sector_rows.append({
                "N": n_sites,
                "k": particles,
                "minority_m": minority,
                "branch": branch(n_sites, particles),
                "sector_state_count": len(words),
                "periodic_core_count": len(core_words),
                "periodic_core_formula": core_formula,
                "transient_state_count": len(words) - len(core_words),
                "max_core_entry_time": max(entry_times),
                "proved_entry_bound_m_squared": minority * minority,
                "full_sector_bijective": minority <= 1,
            })

            fixed_by_n: dict[int, int] = {}
            for iterate_n in range(1, 2 * n_sites + 3):
                observed = sum(iterate(word, iterate_n) == word for word in words)
                formula = fixed_formula(n_sites, particles, iterate_n)
                assert observed == formula
                fixed_by_n[iterate_n] = formula
                fixed_word_iterate_checks += len(words)
                fixed_rows.append({
                    "N": n_sites,
                    "k": particles,
                    "n": iterate_n,
                    "gcd_N_n": gcd(n_sites, iterate_n),
                    "repetition_q": n_sites // gcd(n_sites, iterate_n),
                    "fixed_count_formula": formula,
                    "fixed_count_enumerated": observed,
                })

            observed_periods: dict[int, int] = {d: 0 for d in divisors(n_sites)}
            for word in core_words:
                period = exact_period(word)
                assert period is not None and n_sites % period == 0
                observed_periods[period] += 1
            for d in divisors(n_sites):
                exact_points = sum(mobius(d // e) * fixed_by_n[e] for e in divisors(d))
                assert exact_points == observed_periods[d]
                assert exact_points % d == 0
                primitive_rows.append({
                    "N": n_sites,
                    "k": particles,
                    "period_d": d,
                    "exact_periodic_points": exact_points,
                    "primitive_cycles": exact_points // d,
                    "enumerated_exact_periodic_points": observed_periods[d],
                })

    data = {
        "schema": "HCS-C175-v1",
        "candidate_id": "HCS-C175",
        "date_utc": "2026-08-26",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "source_lock": {
            "object": "cyclic elementary cellular automaton Rule 184 on binary words of length N",
            "family": "every N>=1 and every fixed particle sector 0<=k<=N",
            "arithmetic_origin": "none; particle number and traffic motion have no intrinsic prime or prime-power semantics",
            "clock": "one simultaneous Rule-184 update",
            "normalization": "labelled cyclic sites; right shift has (rho x)_i=x_(i-1)",
            "determinant_convention": "Artin--Mazur zeta of the finite sector and the finite periodic-core Koopman determinant",
            "cutoff": "all-parameter proof; exhaustive regression for 1<=N<=12 and 1<=n<=2N+2",
            "precision": "exact binary states and integer counts",
            "allowed_data": "the frozen local rule, N, k, cyclic adjacency, gcd, binomial and Mobius arithmetic",
            "forbidden_data": "target zero or prime tables, arithmetic local data, Euler factors, root numbers, automorphy, Hilbert--Polya operators, and Route-B inputs",
        },
        "classification_theorem": {
            "local_rule": "F(x)_i=x_(i-1)*(1-x_i)+x_i*x_(i+1), equivalently simultaneous 10->01",
            "low_density": "if k<=N/2, a state is periodic iff it has no cyclic 11; on that core F is right rotation",
            "high_density": "if k>=N/2, a state is periodic iff it has no cyclic 00; on that core F is left rotation",
            "balanced": "if N is even and k=N/2, the periodic core is exactly the two alternating states, both of period two",
            "uniform": "k=0 and k=N each contain one fixed uniform state",
            "period_divisibility": "every temporal least period divides N and equals the least cyclic rotation period",
        },
        "finite_attraction_theorem": {
            "gap_update": "for minority gaps g_i, g_i'=g_i-1_(g_i>0)+1_(g_(i+1)>0)",
            "zero_marker_rule": "a zero gap shifts one index backward unless its predecessor is at least two, in which case that zero is absorbed",
            "lyapunov": "the number of zero minority gaps never increases and, while positive, decreases within at most m updates",
            "bound": "every state reaches the isolated-minority periodic core in at most m^2 updates",
            "duality": "the high-density proof exchanges particles with left-moving holes",
        },
        "fixed_and_primitive_theorem": {
            "independent_cycle_count": "I(g,0)=1; I(g,r)=g/(g-r)*binom(g-r,r) for 1<=r<=floor(g/2), and zero otherwise",
            "fixed_count": "with m=min(k,N-k), g=gcd(N,n), q=N/g: #Fix(F^n|X_(N,k))=I(g,m/q) if q divides m, and zero otherwise",
            "exact_points": "E_(N,k)(d)=sum_(e|d) mu(d/e)*#Fix(F^e) for d|N",
            "primitive_cycles": "P_(N,k)(d)=E_(N,k)(d)/d",
            "zeta": "zeta_(N,k)(z)=product_(d|N) (1-z^d)^(-P_(N,k)(d))",
            "core_determinant": "det(I-z*U_core)=product_(d|N) (1-z^d)^(P_(N,k)(d))=1/zeta_(N,k)(z)",
        },
        "koopman_boundary": {
            "whole_sector": "the whole-sector map is bijective exactly when m<=1; then it is a cyclic rotation",
            "transient_boundary": "when m>=2 the sector contains transient states, so the whole-sector uniform Koopman composition operator is not unitary",
            "periodic_core": "restriction to the canonical periodic core is a finite rotation permutation and has a natural unitary Koopman operator",
            "reversal": "spatial reflection reverses the core rotation, but the core restriction discards full-system transients",
        },
        "finite_replay": {
            "N_max": N_MAX,
            "iterate_n_rule": "1<=n<=2N+2",
            "sector_rows": sector_rows,
            "fixed_rows": fixed_rows,
            "primitive_rows": primitive_rows,
            "sector_row_count": len(sector_rows),
            "fixed_row_count": len(fixed_rows),
            "primitive_row_count": len(primitive_rows),
            "classified_word_count": classified_words,
            "fixed_word_iterate_checks": fixed_word_iterate_checks,
            "maximum_observed_core_entry_time": maximum_observed_entry_time,
        },
        "progress_and_boundary": {
            "progress": "proves the all-N all-density periodic-core classification, finite attraction, every iterate fixed count, primitive-cycle product, and exact full-versus-core Koopman boundary",
            "route_a_obstruction": "the cycles are intrinsic but carry no arithmetic semantics, target divisor comparison, or target global analytic structure",
            "sentinel_boundary": "finite enumeration regression-tests formulas proved combinatorially and does not extrapolate the infinite family",
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "A0_qualification": "NO_INTRINSIC_ARITHMETIC_ORIGIN_OR_PRIME_CORRESPONDENCE",
            "A1_qualification": "COMPLETE_INTRINSIC_PRIMITIVE_CYCLES_WITHOUT_ARITHMETIC_INFORMATION",
            "A2_qualification": "EXACT_SOURCE_ZETA_WITH_NO_TARGET_DIVISOR_COMPARISON",
            "A3_qualification": "FINITE_RATIONAL_SOURCE_STRUCTURE_WITH_NO_TARGET_GLOBAL_ANALYTIC_COMPARISON",
            "A4_qualification": "NATURAL_UNITARY_ONLY_ON_FULL_SECTORS_WITH_M_AT_MOST_ONE_OR_ON_THE_PERIODIC_CORE_THAT_DISCARDS_TRANSIENTS",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": {
            "used_target_zero_table": False,
            "used_target_prime_table": False,
            "used_arithmetic_local_data": False,
            "claimed_target_divisor_match": False,
            "claimed_target_functional_equation": False,
            "claimed_hilbert_polya": False,
            "route_b_invocation_allowed": False,
        },
        "nonclaims": [
            "external novelty or priority for the classical Rule-184 facts",
            "prime semantics for traffic cycles or their repetitions",
            "unitarity of the full sector when transient states are present",
            "a target divisor, functional equation, counting law, continuation, or Weil compression",
            "arithmetic local factors, Euler factors, root numbers, automorphy, a Hilbert--Polya operator, Route-B authorization, or external peer review",
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
    replay = data["finite_replay"]
    print(json.dumps({
        "status": "C175_PRODUCER_PASS",
        "sector_rows": replay["sector_row_count"],
        "fixed_rows": replay["fixed_row_count"],
        "primitive_rows": replay["primitive_row_count"],
        "classified_words": replay["classified_word_count"],
        "payload_sha256": data["payload_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
