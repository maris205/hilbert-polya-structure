#!/usr/bin/env python3
"""Producer-independent checker for the HCS-C160 Rule-90 sieve."""
from __future__ import annotations

from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c160_rule90_sieve_evidence.json"
checks = 0


def require(condition: bool, message: str) -> None:
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)


def poly_degree(value: int) -> int:
    return value.bit_length() - 1


def poly_product(a: int, b: int) -> int:
    answer = 0
    shift = 0
    while b:
        if b % 2:
            answer ^= a << shift
        shift += 1
        b //= 2
    return answer


def poly_power(base: int, exponent: int) -> int:
    answer = 1
    while exponent:
        if exponent % 2:
            answer = poly_product(answer, base)
        base = poly_product(base, base)
        exponent //= 2
    return answer


def poly_mod(a: int, b: int) -> int:
    while a and poly_degree(a) >= poly_degree(b):
        a ^= b << (poly_degree(a) - poly_degree(b))
    return a


def poly_gcd(a: int, b: int) -> int:
    while b:
        a, b = b, poly_mod(a, b)
    return a


def dimension(length: int, time: int) -> int:
    spatial = (1 << length) + 1
    temporal = poly_power(5, time) ^ (1 << time)
    return poly_degree(poly_gcd(spatial, temporal))


def factor_set(n: int) -> list[int]:
    answer = []
    trial = 2
    while trial * trial <= n:
        if n % trial == 0:
            answer.append(trial)
            while n % trial == 0:
                n //= trial
        trial += 1
    if n > 1:
        answer.append(n)
    return answer


def all_divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mu(n: int) -> int:
    sign = 1
    trial = 2
    while trial * trial <= n:
        if n % trial == 0:
            n //= trial
            sign = -sign
            if n % trial == 0:
                return 0
            while n % trial == 0:
                n //= trial
        trial += 1
    if n > 1:
        sign = -sign
    return sign


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    data = json.loads(path.read_text())
    body = dict(data)
    claimed = body.pop("payload_sha256")
    encoded = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    require(sha256(encoded).hexdigest() == claimed, "payload hash")
    require(set(data) == {"schema", "candidate_id", "date_utc", "source_commit", "scope_literal", "source_lock", "hard_gate_record", "periodic_image_theorem", "maximal_subgroup_sieve_theorem", "mersenne_prime_cycle_theorem", "finite_replay", "progress_and_boundary", "route_a", "scope_flags", "nonclaims", "payload_sha256"}, "top-level closure")
    require(data["schema"] == "HCS-C160-v1", "schema")
    require(data["candidate_id"] == "HCS-C160", "candidate")
    require(data["date_utc"] == "2026-08-25", "date")
    require(data["source_commit"] == "63f75cf476711de93e6096ef74ac16969e1127d0", "commit")
    require(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")

    lock = data["source_lock"]
    require(set(lock) == {"object", "family", "clock", "normalization", "cutoff", "precision", "allowed_data", "forbidden_data"}, "lock closure")
    require("Rule 90" in lock["object"] and "x+x^(-1)" in lock["object"], "object")
    require("every Mersenne circumference" in lock["family"] and "every such L>3" in lock["family"], "family")
    require("periodic image im(a)" in lock["clock"], "clock")
    require("uniform labeled states" in lock["normalization"], "normalization")
    require("all-r" in lock["cutoff"] and "2<=r<=10" in lock["cutoff"], "cutoff")
    require(lock["precision"] == "exact F_2 polynomial arithmetic and arbitrary-precision integers", "precision")
    require("source-derived factorization" in lock["allowed_data"], "allowed")
    require("external target prime or zero tables" in lock["forbidden_data"], "forbidden")

    gate = data["hard_gate_record"]
    require(set(gate) == {"requested_advance", "passed_by", "model_pivot_required", "no_infinitude_claim"}, "hard gate closure")
    require("beyond the C155" in gate["requested_advance"], "requested advance")
    require("exact maximal-subgroup" in gate["passed_by"] and "Mersenne-prime" in gate["passed_by"], "passed gate")
    require(gate["model_pivot_required"] is False, "no pivot")
    require("does not assert infinitely many" in gate["no_infinitude_claim"], "no infinitude")

    image = data["periodic_image_theorem"]
    require(image == {
        "identity": "a^(L+1)=a and im(a) is the complete periodic set of dimension L-1",
        "restriction": "g=a|_im(a) satisfies g^L=I, so every exact period divides L",
        "fixed_dimension": "D_L(d)=deg gcd(x^L+1,(x^2+1)^d+x^d)",
        "fixed_count": "|Fix(g^d)|=2^(D_L(d))",
    }, "periodic image theorem")
    sieve = data["maximal_subgroup_sieve_theorem"]
    require(set(sieve) == {"prime_set", "nonfull_union", "intersection", "exact_formula", "bonferroni", "source_only_factorization"}, "sieve theorem closure")
    require("distinct ordinary integer prime divisors" in sieve["prime_set"], "prime set")
    require(sieve["nonfull_union"] == "{v:per(v)<L}=union_{p in P(L)} Fix(g^(L/p))", "nonfull union")
    require("intersection_{p in Q}" in sieve["intersection"] and "product_{p in Q}p" in sieve["intersection"], "intersection")
    require("empty!=Q subset P(L)" in sieve["exact_formula"], "exact formula")
    require("<= N_<L <=" in sieve["bonferroni"], "Bonferroni")
    require("not target arithmetic-local data" in sieve["source_only_factorization"], "factor boundary")
    prime_theorem = data["mersenne_prime_cycle_theorem"]
    require(set(prime_theorem) == {"range", "period_support", "fixed_one_proof", "exact_counts", "cycle_count", "short_probability", "finite_zeta"}, "prime theorem closure")
    require("no infinitude" in prime_theorem["range"], "range")
    require(prime_theorem["period_support"] == [1, "L"], "period support")
    require("x^2+x+1=0" in prime_theorem["fixed_one_proof"] and "order 3" in prime_theorem["fixed_one_proof"], "fixed-one proof")
    require(prime_theorem["exact_counts"] == "P_L(1)=1 and P_L(L)=2^(L-1)-1", "exact counts")
    require(prime_theorem["cycle_count"] == "C_L(L)=(2^(L-1)-1)/L", "cycle count")
    require(prime_theorem["short_probability"] == "Pr(period<L)=2^(-(L-1)) exactly", "probability")
    require(prime_theorem["finite_zeta"] == "zeta_g(z)=1/((1-z)(1-z^L)^((2^(L-1)-1)/L))", "finite zeta")

    replay = data["finite_replay"]
    require(set(replay) == {"r_min", "r_max", "family_rows", "maximal_subgroup_subset_cell_count", "divisor_cell_count", "mersenne_prime_rows", "L3_exception"}, "replay closure")
    require(replay["r_min"] == 2 and replay["r_max"] == 10, "r range")
    require(len(replay["family_rows"]) == 9, "family row count")
    subset_total = 0
    divisor_total = 0
    expected_prime_rows = []
    for r, row in zip(range(2, 11), replay["family_rows"]):
        length = 2**r - 1
        primes = factor_set(length)
        require(set(row) == {"exponent_r", "ring_length_L", "distinct_source_length_prime_factors", "periodic_image_dimension", "periodic_image_points", "maximal_subgroup_rows", "divisor_rows", "nonfull_periodic_points", "full_period_points", "singleton_bonferroni_upper", "singleton_minus_pair_lower", "exact_sieve_matches_mobius"}, f"row {r} closure")
        require(row["exponent_r"] == r and row["ring_length_L"] == length, f"row {r} id")
        require(row["distinct_source_length_prime_factors"] == primes, f"factors {r}")
        require(row["periodic_image_dimension"] == length - 1, f"image dimension {r}")
        periodic = 2**(length - 1)
        require(row["periodic_image_points"] == periodic, f"image points {r}")
        expected_subsets = []
        nonfull = 0
        singleton = 0
        pairs = 0
        for size in range(1, len(primes) + 1):
            for chosen in combinations(primes, size):
                product = 1
                for factor in chosen:
                    product *= factor
                time = length // product
                dim = dimension(length, time)
                points = 2**dim
                sign = 1 if size % 2 else -1
                expected_subsets.append({"prime_subset": list(chosen), "subset_size": size, "intersection_time": time, "fixed_dimension": dim, "fixed_points": points, "inclusion_exclusion_sign": sign, "signed_term": sign * points})
                nonfull += sign * points
                if size == 1:
                    singleton += points
                elif size == 2:
                    pairs += points
        require(row["maximal_subgroup_rows"] == expected_subsets, f"subset ledger {r}")
        subset_total += len(expected_subsets)
        require(row["nonfull_periodic_points"] == nonfull, f"nonfull {r}")
        require(row["full_period_points"] == periodic - nonfull, f"full {r}")
        require(row["singleton_bonferroni_upper"] == singleton, f"upper {r}")
        require(row["singleton_minus_pair_lower"] == singleton - pairs, f"lower {r}")
        require(singleton - pairs <= nonfull <= singleton, f"Bonferroni order {r}")
        expected_divisors = []
        exact = 0
        for d in all_divisors(length):
            dim = dimension(length, d)
            fixed = 2**dim
            weight = mu(length // d)
            expected_divisors.append({"divisor": d, "fixed_dimension": dim, "fixed_points": fixed, "mobius_weight_for_full_period": weight})
            exact += weight * fixed
        require(row["divisor_rows"] == expected_divisors, f"divisor ledger {r}")
        divisor_total += len(expected_divisors)
        require(exact == periodic - nonfull, f"Mobius equality {r}")
        require(row["exact_sieve_matches_mobius"] is True, f"match flag {r}")
        if primes == [length] and length > 3:
            require(dimension(length, 1) == 0 and nonfull == 1, f"prime fixed set {r}")
            cycles = (periodic - 1) // length
            require(cycles * length == periodic - 1, f"cycle divisibility {r}")
            expected_prime_rows.append({"exponent_r": r, "mersenne_prime_L": length, "fixed_points_at_time_one": 1, "exact_period_one_points": 1, "exact_period_L_points": periodic - 1, "primitive_L_cycles": cycles, "short_period_probability": {"numerator": 1, "denominator": periodic}, "finite_zeta": f"1/((1-z)(1-z^{length})^{cycles})"})
    require(replay["maximal_subgroup_subset_cell_count"] == subset_total == 27, "subset cells")
    require(replay["divisor_cell_count"] == divisor_total, "divisor cells")
    require(replay["mersenne_prime_rows"] == expected_prime_rows, "prime rows")
    require([row["mersenne_prime_L"] for row in expected_prime_rows] == [7, 31, 127], "finite prime sentinels")
    require(replay["L3_exception"] == {"L": 3, "fixed_dimension_at_one": 2, "fixed_points_at_one": 4, "reason": "3 divides L, so the order-three roots occur and g is the identity on im(a)"}, "L3 exception")

    progress = data["progress_and_boundary"]
    require(set(progress) == {"progress", "route_a_obstruction"}, "progress closure")
    require("upgrades C155" in progress["progress"] and "closed two-period cycle law" in progress["progress"], "progress")
    require("no target divisor" in progress["route_a_obstruction"], "obstruction")
    route = data["route_a"]
    require(set(route) == {"tuple", "overall", "A1_qualification", "A2_qualification", "A3_qualification", "A4_qualification", "route_b_invocation_allowed"}, "route closure")
    require(route["tuple"] == ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"], "route tuple")
    require(route["overall"] == "ROUTE_A_EXPLORATORY", "overall")
    require(route["route_b_invocation_allowed"] is False, "route B")
    require(data["scope_flags"] == {"scope": "NO_BAD_EULER_OR_ROOT_NUMBER", "uses_prime_table": False, "uses_zero_table": False, "claims_arithmetic_euler_factors": False, "claims_root_number": False, "claims_automorphy": False, "claims_hilbert_polya": False, "uses_route_b_inputs": False}, "scope flags")
    require(data["nonclaims"] == ["that infinitely many Mersenne primes exist", "that the ordinary divisors of L are arithmetic local factors or an Euler product", "a target divisor, functional equation, or counting-law match", "a natural self-adjoint Hilbert--Polya operator", "Route-B authorization or a solution of the larger program"], "nonclaims")
    print(json.dumps({"status": "C160_CHECKER_PASS", "assertions": checks, "payload_sha256": claimed, "subset_cells": subset_total, "divisor_cells": divisor_total}, sort_keys=True))


if __name__ == "__main__":
    main()
