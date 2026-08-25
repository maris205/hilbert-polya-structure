#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C165."""
from __future__ import annotations

from hashlib import sha256
import json
from math import gcd
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c165_margolus_evidence.json"
checks = 0


def require(condition: bool, message: str) -> None:
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mu(n: int) -> int:
    result = 1
    trial = 2
    while trial * trial <= n:
        if n % trial == 0:
            n //= trial
            result = -result
            if n % trial == 0:
                return 0
            while n % trial == 0:
                n //= trial
        trial += 1
    return -result if n > 1 else result


def layer_a(size: int) -> list[int]:
    answer = []
    for i in range(size):
        answer.append(i + 1 if i % 2 == 0 else i - 1)
    return answer


def layer_b(size: int) -> list[int]:
    answer = []
    for i in range(size):
        answer.append((i + 1) % size if i % 2 else (i - 1) % size)
    return answer


def compose(left: list[int], right: list[int]) -> list[int]:
    return [left[right[i]] for i in range(len(left))]


def power(permutation: list[int], exponent: int) -> list[int]:
    result = list(range(len(permutation)))
    base = permutation[:]
    while exponent:
        if exponent & 1:
            result = compose(base, result)
        base = compose(base, base)
        exponent //= 2
    return result


def inverse(permutation: list[int]) -> list[int]:
    answer = [0] * len(permutation)
    for i, target in enumerate(permutation):
        answer[target] = i
    return answer


def cycle_count(permutation: list[int]) -> int:
    seen = set()
    count = 0
    for start in range(len(permutation)):
        if start in seen:
            continue
        count += 1
        current = start
        while current not in seen:
            seen.add(current)
            current = permutation[current]
    return count


def move_mask(mask: int, permutation: list[int]) -> int:
    answer = 0
    for i, target in enumerate(permutation):
        if mask & (1 << i):
            answer |= 1 << target
    return answer


def exact_period_counts_brute(m: int, permutation: list[int]) -> dict[int, int]:
    result = {d: 0 for d in divisors(m)}
    for initial in range(1 << (2 * m)):
        current = move_mask(initial, permutation)
        period = 1
        while current != initial:
            current = move_mask(current, permutation)
            period += 1
            if period > m:
                raise AssertionError("full tick did not close")
        if period not in result:
            raise AssertionError("period did not divide m")
        result[period] += 1
    return result


def exact_necklace(d: int) -> int:
    return sum(mu(d // e) * 4**e for e in divisors(d))


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    data = json.loads(path.read_text())
    body = dict(data)
    claimed = body.pop("payload_sha256")
    encoded = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    require(sha256(encoded).hexdigest() == claimed, "payload hash")
    require(set(data) == {
        "schema", "candidate_id", "date_utc", "source_commit", "scope_literal",
        "source_lock", "pivot_record", "site_permutation_theorem",
        "necklace_conjugacy_theorem", "period_theorem", "concentration_theorem",
        "reversibility_and_koopman", "finite_replay", "progress_and_boundary",
        "route_a", "scope_flags", "nonclaims", "payload_sha256",
    }, "top-level closure")
    require(data["schema"] == "HCS-C165-v1", "schema")
    require(data["candidate_id"] == "HCS-C165", "candidate")
    require(data["date_utc"] == "2026-08-25", "date")
    require(data["source_commit"] == "4342893ce5e2516924181744bfacc01c12e4959d", "commit")
    require(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")

    lock = data["source_lock"]
    require(set(lock) == {"object", "family", "clock", "normalization", "determinant_convention", "cutoff", "precision", "allowed_data", "forbidden_data"}, "lock closure")
    require("2m sites" in lock["object"] and "Margolus" in lock["object"], "object")
    require(lock["family"] == "every integer m>=1; finite exact replay uses 1<=m<=16", "family")
    require(lock["clock"] == "one full tick is T=B after A; neither A nor B alone is a full source clock", "clock")
    require("uniform labeled binary configurations" in lock["normalization"], "normalization")
    require("Koopman determinant" in lock["determinant_convention"], "determinant convention")
    require("every m>=1" in lock["cutoff"] and "m<=8" in lock["cutoff"], "cutoff")
    require(lock["precision"] == "exact permutations, integers, rational probabilities, and symbolic polynomials", "precision")
    require("two-layer local swap schedule" in lock["allowed_data"], "allowed")
    require("target zero or prime tables" in lock["forbidden_data"] and "Hilbert--Polya" in lock["forbidden_data"], "forbidden")

    pivot = data["pivot_record"]
    require(set(pivot) == {"rejected_candidate", "reason", "replacement", "failed_claim_reframed_as_progress"}, "pivot closure")
    require("Rule-90" in pivot["rejected_candidate"], "rejected lineage")
    require("no uniform elementary reduction" in pivot["reason"] and "three preceding rounds" in pivot["reason"], "pivot reason")
    require("reversible two-phase Margolus" in pivot["replacement"], "replacement")
    require(pivot["failed_claim_reframed_as_progress"] is False, "not reframed")

    site = data["site_permutation_theorem"]
    require(site == {
        "layers": "A swaps (0,1),(2,3),... and B swaps (1,2),(3,4),...,(2m-1,0)",
        "full_tick": "T=B after A",
        "cell_motion": "tau(i)=i+2 mod 2m for even i and tau(i)=i-2 mod 2m for odd i",
        "order": "tau^m=identity, including the m=1 identity boundary",
    }, "site theorem")
    necklace = data["necklace_conjugacy_theorem"]
    require(set(necklace) == {"pairing", "intertwining", "fixed_count", "complexity_boundary"}, "necklace closure")
    require(necklace["pairing"] == "Phi(x)_j=(x_(2j),x_(1-2j mod 2m)) in {0,1}^2", "pairing")
    require("cyclic rotation" in necklace["intertwining"] and "four-letter" in necklace["intertwining"], "intertwining")
    require(necklace["fixed_count"] == "#Fix(T^n)=4^gcd(m,n) for every m,n>=1", "fixed theorem")
    require("not claimed to be chaotic or interacting" in necklace["complexity_boundary"], "complexity boundary")
    period = data["period_theorem"]
    require(period == {
        "support": "every exact configuration period divides m",
        "exact_points": "P_m(d)=sum_(e|d) mu(d/e)4^e for d|m and P_m(d)=0 otherwise",
        "primitive_cycles": "C_m(d)=P_m(d)/d",
        "zeta": "zeta_T(z)=product_(d|m)(1-z^d)^(-C_m(d))",
    }, "period theorem")
    concentration = data["concentration_theorem"]
    require(concentration == {
        "short_bound": "Pr(period<m)<=m*4^(-m/2)=m/2^m for every m>=1",
        "full_bound": "Pr(period=m)>=1-m*4^(-m/2)",
        "proof_boundary": "the bound uses P_m(d)<=4^d, every proper divisor d<=m/2, and fewer than m proper divisors; it is deliberately coarse",
    }, "concentration theorem")
    owner = data["reversibility_and_koopman"]
    require(set(owner) == {"reflection", "koopman_space", "koopman", "antiunitary", "operator_boundary"}, "owner closure")
    require(owner["reflection"] == "r(i)=-i mod 2m satisfies r*tau*r=tau^(-1)", "reflection")
    require("counting measure" in owner["koopman_space"], "Koopman space")
    require("unitary" in owner["koopman"] and "det(I-zU_T)=zeta_T(z)^(-1)" in owner["koopman"], "Koopman identity")
    require("Theta*U_T*Theta=U_T^(-1)" in owner["antiunitary"], "antiunitary")
    require("self-adjoint exactly for m<=2" in owner["operator_boundary"] and "non-self-adjoint for m>=3" in owner["operator_boundary"] and "no uniform self-adjoint Hilbert--Polya realization" in owner["operator_boundary"], "owner boundary")

    replay = data["finite_replay"]
    require(set(replay) == {"m_min", "m_max", "brute_force_m_max", "family_rows", "fixed_cell_count", "period_cell_count", "directly_enumerated_configurations", "boundary_m1", "boundary_m2"}, "replay closure")
    require(replay["m_min"] == 1 and replay["m_max"] == 16 and replay["brute_force_m_max"] == 8, "ranges")
    require(len(replay["family_rows"]) == 16, "family length")
    fixed_cells = 0
    period_cells = 0
    brute_total = 0
    for m, row in enumerate(replay["family_rows"], 1):
        require(set(row) == {
            "half_ring_m", "site_count", "full_tick_site_permutation", "four_letter_pairing",
            "reflection_permutation", "fixed_rows", "period_rows", "short_period_configurations",
            "full_period_configurations", "total_configurations", "short_probability", "uniform_bound",
            "full_probability_lower_bound", "zeta_factors", "koopman_determinant_factors", "brute_force",
        }, f"row {m} closure")
        size = 2 * m
        a = layer_a(size)
        b = layer_b(size)
        tau = compose(b, a)
        require(row["half_ring_m"] == m and row["site_count"] == size, f"row {m} id")
        require(row["full_tick_site_permutation"] == tau, f"full tick {m}")
        require(tau == [(i + 2) % size if i % 2 == 0 else (i - 2) % size for i in range(size)], f"motion {m}")
        require(power(tau, m) == list(range(size)), f"order divides m {m}")
        pairs = [[2 * j, (1 - 2 * j) % size] for j in range(m)]
        require(row["four_letter_pairing"] == pairs, f"pairing {m}")
        for j, pair in enumerate(pairs):
            require([tau[pair[0]], tau[pair[1]]] == pairs[(j + 1) % m], f"intertwiner {m}:{j}")
        reflection = [(-i) % size for i in range(size)]
        require(row["reflection_permutation"] == reflection, f"reflection row {m}")
        require(compose(reflection, compose(tau, reflection)) == inverse(tau), f"reversal {m}")

        expected_fixed = []
        for n in range(1, m + 1):
            powered = power(tau, n)
            cycles = cycle_count(powered)
            require(cycles == 2 * gcd(m, n), f"site cycles {m}:{n}")
            expected_fixed.append({"time_n": n, "site_cycles": cycles, "fixed_configurations": 2**cycles, "closed_formula": 4 ** gcd(m, n)})
        require(row["fixed_rows"] == expected_fixed, f"fixed ledger {m}")
        fixed_cells += len(expected_fixed)

        expected_periods = []
        short = 0
        for d in divisors(m):
            points = exact_necklace(d)
            require(points >= 0 and points % d == 0, f"cycle divisibility {m}:{d}")
            expected_periods.append({"period_d": d, "exact_period_configurations": points, "primitive_cycles": points // d, "zeta_exponent": -(points // d)})
            if d < m:
                short += points
        require(row["period_rows"] == expected_periods, f"period ledger {m}")
        period_cells += len(expected_periods)
        require(sum(item["exact_period_configurations"] for item in expected_periods) == 4**m, f"period partition {m}")
        require(row["short_period_configurations"] == short, f"short count {m}")
        require(row["full_period_configurations"] == expected_periods[-1]["exact_period_configurations"], f"full count {m}")
        require(row["total_configurations"] == 4**m, f"total {m}")
        require(row["short_probability"] == {"numerator": short, "denominator": 4**m}, f"short probability {m}")
        require(short * 2**m <= m * 4**m, f"coarse bound {m}")
        require(row["uniform_bound"] == {"numerator": m, "denominator": 2**m, "formula": "m*4^(-m/2)=m/2^m"}, f"bound row {m}")
        require(row["full_probability_lower_bound"] == {"numerator": 2**m - m, "denominator": 2**m}, f"lower row {m}")
        require(row["zeta_factors"] == [f"(1-z^{item['period_d']})^({item['zeta_exponent']})" for item in expected_periods], f"zeta factors {m}")
        require(row["koopman_determinant_factors"] == [f"(1-z^{item['period_d']})^({-item['zeta_exponent']})" for item in expected_periods], f"det factors {m}")
        if m <= replay["brute_force_m_max"]:
            brute = exact_period_counts_brute(m, tau)
            brute_total += 4**m
            require(row["brute_force"] == {"enumerated_configurations": 4**m, "exact_period_counts": {str(d): brute[d] for d in sorted(brute)}, "matches_necklace_formula": True}, f"brute row {m}")
            require(brute == {item["period_d"]: item["exact_period_configurations"] for item in expected_periods}, f"brute formula {m}")
        else:
            require(row["brute_force"] is None, f"no brute row {m}")
    require(replay["fixed_cell_count"] == fixed_cells == 136, "fixed cells")
    require(replay["period_cell_count"] == period_cells, "period cells")
    require(replay["directly_enumerated_configurations"] == brute_total == sum(4**m for m in range(1, 9)), "brute total")
    require(replay["boundary_m1"] == {"total": 4, "exact_period_one": 4, "short": 0, "T_is_identity": True}, "m1")
    require(replay["boundary_m2"] == {"total": 16, "exact_period_one": 4, "exact_period_two": 12, "primitive_two_cycles": 6}, "m2")

    progress = data["progress_and_boundary"]
    require(set(progress) == {"progress", "route_a_obstruction"}, "progress closure")
    require("pivots from an overused Rule-90 lineage" in progress["progress"] and "Koopman determinant" in progress["progress"], "progress")
    require("no target divisor" in progress["route_a_obstruction"] and "not a Hilbert--Polya" in progress["route_a_obstruction"], "obstruction")
    route = data["route_a"]
    require(set(route) == {"tuple", "overall", "A1_qualification", "A2_qualification", "A3_qualification", "A4_qualification", "route_b_invocation_allowed"}, "route closure")
    require(route["tuple"] == ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"], "tuple")
    require(route["overall"] == "ROUTE_A_EXPLORATORY", "overall")
    require(route["A1_qualification"] == "ALL_M_EXACT_NECKLACE_PERIOD_LAW_FOR_A_REVERSIBLE_PARTITIONED_CA", "A1")
    require(route["A2_qualification"] == "EXACT_FINITE_SOURCE_ZETA_WITH_NO_TARGET_DIVISOR_COMPARISON", "A2")
    require(route["A3_qualification"] == "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_OR_CONTINUATION_COMPARISON", "A3")
    require(route["A4_qualification"] == "SAME_CLOCK_FINITE_KOOPMAN_UNITARY_WITH_EXPLICIT_ANTIUNITARY_REVERSAL", "A4")
    require(route["route_b_invocation_allowed"] is False, "Route B")
    require(data["scope_flags"] == {
        "scope": "NO_BAD_EULER_OR_ROOT_NUMBER", "uses_prime_table": False,
        "uses_zero_table": False, "claims_arithmetic_euler_factors": False,
        "claims_root_number": False, "claims_automorphy": False,
        "claims_hilbert_polya": False, "claims_chaos_or_interaction": False,
        "uses_route_b_inputs": False,
    }, "scope flags")
    require(data["nonclaims"] == [
        "chaos or interaction in a system conjugate to a four-letter rotation",
        "a target divisor, functional equation, or counting-law match",
        "arithmetic local factors, Euler factors, root numbers, or automorphy",
        "a uniform self-adjoint Hilbert--Polya realization across the family",
        "Route-B authorization or a solution of the larger program",
    ], "nonclaims")
    print(json.dumps({
        "status": "C165_CHECKER_PASS", "assertions": checks,
        "payload_sha256": claimed, "fixed_cells": fixed_cells,
        "period_cells": period_cells, "brute_configurations": brute_total,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
