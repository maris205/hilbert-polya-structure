#!/usr/bin/env python3
"""Producer-independent checker for the C239 perfect-shuffle receipt."""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "results/c239_shuffle_evidence.json"
SOURCE_COMMIT = "489506cf92bfed721f94f22dd0444a60427f90a5"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"

TOP_KEYS = {"schema", "candidate_id", "evaluation_date", "source_commit", "scope_literal", "evaluator", "headline", "frozen_object", "theorem", "regression", "exact_identities", "route_a", "scope_flags", "citations", "nonclaims", "payload_sha256"}
FROZEN_KEYS = {"definition", "parameters", "phase_space", "map", "invariant", "clock", "primitive_periodic_orbit", "out_shuffle_boundary", "forbidden_data"}
THEOREM_KEYS = {"permutation", "packet_interleave_equivalence", "fixed_points", "position_period", "primitive_points", "global_order", "zeta", "koopman", "cross_parameter", "completeness", "scope"}
REG_KEYS = {"atlas_rows", "position_rows", "spectral_rows", "representative_cycles", "parameter_grid", "row_counts", "integer_arithmetic_only"}
ATLAS_KEYS = {"k", "n", "modulus_M", "domain_size", "global_order", "fixed_counts_1_to_order", "exact_period_counts_1_to_order", "cycle_counts_1_to_order", "cycle_count_total", "direct_cycle_lengths"}
POSITION_KEYS = {"k", "n", "position_i", "gcd_i_M", "reduced_modulus", "position_period"}
SPECTRAL_KEYS = {"k", "n", "modulus_M", "domain_size", "zeta_factor_exponents", "koopman_characteristic_factor_exponents", "zeta_denominator_coefficients_low_to_high", "koopman_coefficients_low_to_high", "zeta_degree", "koopman_degree"}
REP_KEYS = {"representative", "period", "members_forward"}
ROUTE_KEYS = {"tuple", "overall", "route_b_invocation_allowed", "strongest_positive", "strongest_failure"}
SCOPE_KEYS = {"uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"}


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def divisors(value: int) -> list[int]:
    ans: list[int] = []
    for d in range(1, math.isqrt(value) + 1):
        if value % d == 0:
            ans.append(d)
            if d * d != value:
                ans.append(value // d)
    return sorted(ans)


def mobius(value: int) -> int:
    if value == 1:
        return 1
    x, sign, p = value, 1, 2
    while p * p <= x:
        if x % p == 0:
            x //= p
            sign = -sign
            if x % p == 0:
                return 0
            while x % p == 0:
                x //= p
        p += 1 if p == 2 else 2
    if x > 1:
        sign = -sign
    return sign


def phi(value: int) -> int:
    result, x, p = value, value, 2
    while p * p <= x:
        if x % p == 0:
            result -= result // p
            while x % p == 0:
                x //= p
        p += 1 if p == 2 else 2
    if x > 1:
        result -= result // x
    return result


def order_mod(k: int, modulus: int) -> int:
    assert modulus > 1 and math.gcd(k, modulus) == 1
    for d in divisors(phi(modulus)):
        if pow(k, d, modulus) == 1:
            return d
    raise AssertionError("order missing")


def fixed(k: int, modulus: int, r: int) -> int:
    return math.gcd(pow(k, r) - 1, modulus) - 1


def cycles_independent(k: int, n: int) -> list[list[int]]:
    modulus = k * n + 1
    mapping = [(k * i) % modulus for i in range(modulus)]
    assert mapping[0] == 0
    assert sorted(mapping[1:]) == list(range(1, modulus))
    seen = [False] * modulus
    ans: list[list[int]] = []
    for i in range(1, modulus):
        if seen[i]:
            continue
        cyc: list[int] = []
        x = i
        while not seen[x]:
            seen[x] = True
            cyc.append(x)
            x = mapping[x]
        assert x == i
        pivot = min(cyc)
        j = cyc.index(pivot)
        ans.append(cyc[j:] + cyc[:j])
    return sorted(ans, key=lambda c: c[0])


def packet_interleave(k: int, n: int, position: int) -> int:
    """Literal packet operation, independent of modular multiplication.

    Piles are indexed top-to-bottom by j=0,...,k-1.  The perfect interleave
    takes the first card of the last pile, then the first of the previous pile,
    and so on, hence the new one-based position is k*r-j.
    """
    assert 1 <= position <= k * n
    j, r0 = divmod(position - 1, n)
    r = r0 + 1
    return k * r - j


def polynomial(factors: list[list[int]]) -> list[int]:
    coeff = [1]
    for degree, sign, power in factors:
        assert sign in (-1, 1) and power >= 0
        for _ in range(power):
            nxt = [0] * (len(coeff) + degree)
            for j, value in enumerate(coeff):
                nxt[j] += value
                nxt[j + degree] += sign * value
            coeff = nxt
    return coeff


def check_keys(obj: dict, expected: set[str], where: str) -> int:
    assert set(obj) == expected, f"{where} key mismatch: {sorted(set(obj) ^ expected)}"
    return 1


def validate(data: dict) -> int:
    count = 0
    count += check_keys(data, TOP_KEYS, "top")
    for key, value in (("schema", "hcs-c239-multiway-perfect-shuffle-v1"), ("candidate_id", "HCS-C239"), ("evaluation_date", "2026-08-30"), ("source_commit", SOURCE_COMMIT), ("scope_literal", SCOPE)):
        assert data[key] == value, (key, data[key]); count += 1
    assert data["payload_sha256"] == payload_hash(data); count += 1
    ev = data["evaluator"]
    assert set(ev) == {"path", "version", "sha256"}; count += 1
    assert ev == {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256}; count += 1

    frozen = data["frozen_object"]
    count += check_keys(frozen, FROZEN_KEYS, "frozen")
    expected_frozen = {
        "definition": "rho_{k,n}(i)=k*i mod M on D_M={1,...,M-1}",
        "parameters": "integers k>=2 and n>=1; M=k*n+1",
        "phase_space": "nonzero residue positions D_M={1,...,M-1}, representing a k-way deck of kn cards",
        "map": "rho(i)=(k i) mod M",
        "invariant": "gcd(i,M) is preserved",
        "clock": "one exact shuffle application; orientation is the forward residue direction",
        "primitive_periodic_orbit": "least period under the positional permutation, modulo cyclic phase",
        "out_shuffle_boundary": "the 2-way out-shuffle is the endpoint-fixed M=2n-1 conjugate; this receipt freezes the in/multiway M=kn+1 convention",
        "forbidden_data": "target primes/zeros, arithmetic local data, Euler factors, root numbers, automorphy, target divisors, Hilbert-Polya operators",
    }
    for key, value in expected_frozen.items():
        assert frozen[key] == value, key; count += 1

    theorem = data["theorem"]
    count += check_keys(theorem, THEOREM_KEYS, "theorem")
    expected_fragments = {
        "permutation": "gcd(k,M)=1",
        "packet_interleave_equivalence": "literal reverse-pile interleaving",
        "fixed_points": "gcd(k^r-1,M)-1",
        "position_period": "ord_{M/gcd(i,M)}(k)",
        "primitive_points": "E_r=sum_{d|r} mu(r/d) Fix(rho^d)",
        "global_order": "ord_M(k)",
        "zeta": "prod_{r>=1}(1-z^r)^(-C_r)",
        "koopman": "det(lambda I-U)=prod_{r>=1}(lambda^r-1)^{C_r}",
        "cross_parameter": "every integer pair (k,n)",
        "completeness": "direct atlas exhausts D_M",
        "scope": "not matched to a target arithmetic divisor",
    }
    for key, fragment in expected_fragments.items():
        assert fragment.lower() in theorem[key].lower(), (key, fragment); count += 1

    reg = data["regression"]
    count += check_keys(reg, REG_KEYS, "regression")
    assert reg["integer_arithmetic_only"] is True; count += 1
    expected_grid = [{"k": k, "n": n} for k in range(2, 7) for n in range(1, 11)]
    assert reg["parameter_grid"] == expected_grid; count += 1
    assert reg["row_counts"] == {"atlas": 50, "position": 74, "spectral": 6, "representative_cycles": 1, "packet_interleave_checks": 1100}; count += 1

    atlas = reg["atlas_rows"]
    assert len(atlas) == 50; count += 1
    for index, row in enumerate(atlas):
        count += check_keys(row, ATLAS_KEYS, "atlas row")
        k, n, modulus = row["k"], row["n"], row["modulus_M"]
        assert {"k": k, "n": n} == expected_grid[index], (index, k, n); count += 1
        assert isinstance(k, int) and isinstance(n, int) and k >= 2 and n >= 1; count += 1
        assert modulus == k * n + 1 and row["domain_size"] == modulus - 1; count += 1
        assert math.gcd(k, modulus) == 1; count += 1
        q = order_mod(k, modulus)
        assert row["global_order"] == q; count += 1
        fixed_counts = [fixed(k, modulus, r) for r in range(1, q + 1)]
        assert row["fixed_counts_1_to_order"] == fixed_counts; count += 1
        exact = [sum(mobius(r // d) * fixed(k, modulus, d) for d in divisors(r)) for r in range(1, q + 1)]
        assert row["exact_period_counts_1_to_order"] == exact; count += 1
        cycles = cycles_independent(k, n)
        direct_counts = [sum(1 for c in cycles if len(c) == r) for r in range(1, q + 1)]
        assert row["cycle_counts_1_to_order"] == direct_counts; count += 1
        assert row["direct_cycle_lengths"] == sorted(len(c) for c in cycles); count += 1
        assert row["cycle_count_total"] == len(cycles); count += 1
        assert sum(exact) == modulus - 1 and all(exact[r - 1] == r * direct_counts[r - 1] for r in range(1, q + 1)); count += 1
        assert fixed(k, modulus, q + 1) == fixed_counts[0] and fixed(k, modulus, q + 2) == fixed_counts[1 % q]; count += 1
        for position in range(1, modulus):
            assert packet_interleave(k, n, position) == (k * position) % modulus, (k, n, position)
            count += 1

    positions = reg["position_rows"]
    assert len(positions) == 74; count += 1
    expected_position_pairs = {(2, 3), (2, 5), (3, 2), (3, 4), (4, 3), (5, 2), (6, 3)}
    assert {(r["k"], r["n"]) for r in positions} == expected_position_pairs; count += 1
    for row in positions:
        count += check_keys(row, POSITION_KEYS, "position row")
        k, n, i = row["k"], row["n"], row["position_i"]
        modulus = k * n + 1
        assert 1 <= i < modulus; count += 1
        g = math.gcd(i, modulus)
        reduced = modulus // g
        assert row["gcd_i_M"] == g and row["reduced_modulus"] == reduced; count += 1
        assert row["position_period"] == order_mod(k, reduced); count += 1
        assert pow(k, row["position_period"], reduced) == 1; count += 1
        assert all(pow(k, d, reduced) != 1 for d in divisors(row["position_period"]) if d < row["position_period"]); count += 1

    spectral = reg["spectral_rows"]
    assert len(spectral) == 6; count += 1
    expected_spectral = {(2, 2), (2, 5), (3, 3), (4, 2), (5, 2), (6, 1)}
    assert {(r["k"], r["n"]) for r in spectral} == expected_spectral; count += 1
    for row in spectral:
        count += check_keys(row, SPECTRAL_KEYS, "spectral row")
        k, n = row["k"], row["n"]
        base = next(a for a in atlas if a["k"] == k and a["n"] == n)
        expected_factors = [[r, -1, c] for r, c in enumerate(base["cycle_counts_1_to_order"], 1) if c]
        assert row["modulus_M"] == base["modulus_M"] and row["domain_size"] == base["domain_size"]; count += 1
        assert row["zeta_factor_exponents"] == expected_factors and row["koopman_characteristic_factor_exponents"] == expected_factors; count += 1
        assert row["zeta_degree"] == row["koopman_degree"] == row["domain_size"]; count += 1
        if row["domain_size"] <= 30:
            assert row["zeta_denominator_coefficients_low_to_high"] == polynomial(expected_factors); count += 1
            raw = polynomial(expected_factors)
            sign = (-1) ** sum(c for _, _, c in expected_factors)
            assert row["koopman_coefficients_low_to_high"] == [sign * x for x in raw]; count += 1
        else:
            assert row["zeta_denominator_coefficients_low_to_high"] == [] and row["koopman_coefficients_low_to_high"] == []; count += 1

    reps = reg["representative_cycles"]
    assert len(reps) == 1; count += 1
    expected_cycles = cycles_independent(2, 5)
    assert [{"representative": c[0], "period": len(c), "members_forward": c} for c in expected_cycles] == reps; count += 1
    for row in reps:
        count += check_keys(row, REP_KEYS, "representative cycle")
        assert row["members_forward"][0] == row["representative"] and len(row["members_forward"]) == row["period"]; count += 1

    ids = data["exact_identities"]
    assert len(ids) == 9 and all(set(item) == {"name", "formula"} for item in ids); count += 1
    assert {item["name"] for item in ids} == {"modulus", "coprime_multiplier", "fixed_count", "gcd_stratum", "position_order", "mobius_inversion", "cycle_count", "zeta_factorization", "koopman_factorization"}; count += 1
    expected_formulas = {"modulus": "M=k*n+1", "coprime_multiplier": "gcd(k,M)=1", "fixed_count": "Fix(r)=gcd(k^r-1,M)-1", "gcd_stratum": "gcd(rho(i),M)=gcd(i,M)", "position_order": "period(i)=ord_{M/gcd(i,M)}(k)", "mobius_inversion": "E_r=sum_{d|r}mu(r/d)Fix(d)", "cycle_count": "C_r=E_r/r", "zeta_factorization": "Z=prod_r(1-z^r)^(-C_r)", "koopman_factorization": "det(lambda I-U)=prod_r(lambda^r-1)^(C_r)"}
    for item in ids:
        assert item["formula"] == expected_formulas[item["name"]]; count += 1

    route = data["route_a"]
    count += check_keys(route, ROUTE_KEYS, "route")
    assert route["tuple"] == ["A0_FAIL", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"]; count += 1
    assert route["overall"] == "ROUTE_A_REJECTED" and route["route_b_invocation_allowed"] is False; count += 1
    assert "no intrinsic rational-prime" in route["strongest_failure"]; count += 1
    flags = data["scope_flags"]
    count += check_keys(flags, SCOPE_KEYS, "scope")
    assert all(value is False for value in flags.values()); count += 1
    citations = data["citations"]
    assert len(citations) == 2; count += 1
    expected_citations = {
        "EllisFanShallit2002": {"title": "The Cycles of the Multiway Perfect Shuffle Permutation", "authors": "John Ellis, Hongbing Fan, Jeffrey Shallit", "venue": "Discrete Mathematics & Theoretical Computer Science 5", "year": 2002, "doi": "10.46298/dmtcs.308", "url": "https://dmtcs.episciences.org/308", "role": "primary definition and cycle-structure theorem for rho_{k,n}"},
        "Packard1994": {"title": "The Order of a Perfect k-Shuffle", "authors": "Robert W. Packard and Erik S. Packard", "venue": "The Fibonacci Quarterly 32(2), 136--144", "year": 1994, "doi": "10.1080/00150517.1994.12429237", "url": "https://doi.org/10.1080/00150517.1994.12429237", "role": "order and cycle-length arithmetic for perfect k-shuffles"},
    }
    for item in citations:
        assert set(item) == {"id", "title", "authors", "venue", "year", "doi", "url", "role"}; count += 1
        assert item["id"] in expected_citations and {k: item[k] for k in expected_citations[item["id"]]} == expected_citations[item["id"]]; count += 1
    assert len(data["nonclaims"]) == 5; count += 1
    text = json.dumps(data, ensure_ascii=False).lower()
    for phrase in ("target primes", "euler factors", "root numbers", "hilbert-polya", "route-b", "not matched"):
        assert phrase in text; count += 1
    return count


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    args = parser.parse_args()
    assertions = validate(json.loads(args.input.read_text()))
    print(f"C239 independent checker: PASS ({assertions} assertions)")


if __name__ == "__main__":
    main()
