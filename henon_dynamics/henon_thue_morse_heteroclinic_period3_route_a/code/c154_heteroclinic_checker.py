#!/usr/bin/env python3
"""Producer-independent reconstruction of HCS-C154."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c154_heteroclinic_evidence.json"
SOURCE_COMMIT = "506dead810d67fa58fa7c42b2d9a09bfae161059"


def tm(n: int) -> int:
    return n.bit_count() % 2


def periodic(n: int) -> int:
    return (2, 3, 4)[n % 3]


def symbol(shift: int, coordinate: int) -> int:
    index = shift + coordinate
    return periodic(index) if index < 0 else tm(index)


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def mu(n: int) -> int:
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


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else EVIDENCE
    data = json.loads(path.read_text())
    checks = 0

    def ck(condition: bool, label: str) -> None:
        nonlocal checks
        if not condition:
            raise AssertionError(label)
        checks += 1

    def keys(mapping: dict, expected: set[str], label: str) -> None:
        ck(set(mapping) == expected, label)

    keys(data, {"schema", "candidate_id", "date_utc", "source_commit", "scope_literal", "source_lock", "frozen_configuration", "orbit_closure_theorem", "periodic_orbit_theorem", "finite_replay", "progress_and_boundary", "route_a", "scope_flags", "nonclaims", "payload_sha256"}, "top keys")
    ck(data["schema"] == "HCS-C154-v1", "schema")
    ck(data["candidate_id"] == "HCS-C154", "candidate")
    ck(data["date_utc"] == "2026-08-25", "date")
    ck(data["source_commit"] == SOURCE_COMMIT, "commit")
    ck(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    ck(data["payload_sha256"] == payload_hash(data), "payload hash")

    lock = data["source_lock"]
    keys(lock, {"object", "map", "clock", "normalization", "zeta_convention", "cutoff", "allowed_data", "forbidden_data"}, "lock keys")
    ck(lock["object"].startswith("X=closure of the two-sided shift orbit"), "object")
    ck(lock["map"] == "the left shift sigma, (sigma x)_j=x_(j+1)", "map")
    ck(lock["clock"] == "one symbolic shift", "clock")
    ck("exact-period points" in lock["normalization"], "normalization")
    ck(lock["zeta_convention"].startswith("zeta_X(z)=exp"), "zeta convention")
    ck("all-period theorems" in lock["cutoff"] and "<=36" in lock["cutoff"], "cutoff")
    ck("single frozen interface" in lock["allowed_data"], "allowed")
    ck("Route-B inputs" in lock["forbidden_data"], "forbidden")

    frozen = data["frozen_configuration"]
    keys(frozen, {"alphabet", "thue_morse_alphabet", "periodic_alphabet", "periodic_background", "interface_rule", "interface_pair", "orbit_is_injective", "interface_cylinder_isolates_each_orbit_point", "tm_period_certificate_limit", "tm_period_certificates"}, "frozen keys")
    ck(frozen["alphabet"] == [0, 1, 2, 3, 4], "alphabet")
    ck(frozen["thue_morse_alphabet"] == [0, 1] and frozen["periodic_alphabet"] == [2, 3, 4], "disjoint alphabets")
    ck(frozen["periodic_background"] == "y_j=(2,3,4)_[j mod 3]", "background")
    ck(frozen["interface_rule"] == "x_j=y_j for j<0 and x_j=t_j for j>=0", "interface")
    ck(frozen["interface_pair"] == [4, 0], "pair")
    ck(frozen["orbit_is_injective"] is True and frozen["interface_cylinder_isolates_each_orbit_point"] is True, "isolated injective orbit")
    ck(frozen["tm_period_certificate_limit"] == len(frozen["tm_period_certificates"]) == 32, "certificate count")
    for p, row in enumerate(frozen["tm_period_certificates"], 1):
        keys(row, {"putative_period", "odd_exponent_k", "multiple_d", "popcount_d", "tm_bit_at_zero", "tm_bit_at_d", "forbidden_window_length"}, f"certificate keys p={p}")
        k = p.bit_length() + 1
        if k % 2 == 0:
            k += 1
        d = p * ((1 << k) - 1)
        expected = {"putative_period": p, "odd_exponent_k": k, "multiple_d": d, "popcount_d": d.bit_count(), "tm_bit_at_zero": 0, "tm_bit_at_d": tm(d), "forbidden_window_length": 1 << (d.bit_length() + 1)}
        ck(row == expected, f"certificate p={p}")
        ck(d % p == 0 and tm(d) == 1 and d.bit_count() == k, f"certificate arithmetic p={p}")

    theorem = data["orbit_closure_theorem"]
    keys(theorem, {"exact_decomposition", "positive_escape", "negative_escape", "no_other_limits", "dense_full_orbit", "forward_transitivity_failure", "not_minimal", "wandering_interface", "nonwandering_set"}, "closure keys")
    ck(theorem["exact_decomposition"] == "X=X_TM disjoint_union Orbit_sigma(x) disjoint_union Orbit_sigma(y)", "decomposition")
    ck("every point of X_TM" in theorem["positive_escape"], "positive limits")
    ck("three phases" in theorem["negative_escape"] and "modulo 3" in theorem["negative_escape"], "negative limits")
    ck(theorem["no_other_limits"].endswith("exhaust it"), "limit exhaustion")
    ck(theorem["dense_full_orbit"] == "the full two-sided Z-orbit Orbit_sigma(x) is dense in X by definition", "dense full orbit")
    ck("standard n>=0 topological transitivity fails" in theorem["forward_transitivity_failure"] and "U={sigma x}" in theorem["forward_transitivity_failure"], "forward transitivity boundary")
    ck("proper closed invariant" in theorem["not_minimal"], "not minimal")
    ck("unique cross-alphabet pair 40" in theorem["wandering_interface"], "wandering")
    ck(theorem["nonwandering_set"] == "Omega(sigma)=X_TM disjoint_union Orbit_sigma(y)", "nonwandering")

    periodic_theorem = data["periodic_orbit_theorem"]
    keys(periodic_theorem, {"tm_periodic_points", "interface_orbit_periodic_points", "periodic_points_exactly", "fixed_count", "exact_period_points", "primitive_cycles", "artin_mazur_zeta", "formal_derivation"}, "periodic keys")
    ck(periodic_theorem["tm_periodic_points"] == 0, "TM periodic vacuum")
    ck(periodic_theorem["interface_orbit_periodic_points"] == 0, "interface aperiodic")
    ck(periodic_theorem["periodic_points_exactly"] == "the three phases of y", "periodic classification")
    ck(periodic_theorem["fixed_count"] == "Fix_X(n)=3 if 3 divides n, and Fix_X(n)=0 otherwise, for every n>=1", "fixed theorem")
    ck(periodic_theorem["exact_period_points"] == "P_X(3)=3 and P_X(n)=0 for n!=3", "exact theorem")
    ck(periodic_theorem["primitive_cycles"] == [{"least_period": 3, "primitive_cycles": 1}], "primitive theorem")
    ck(periodic_theorem["artin_mazur_zeta"] == "1/(1-z^3)", "zeta")
    ck(periodic_theorem["formal_derivation"].endswith("-log(1-z^3)"), "zeta derivation")

    replay = data["finite_replay"]
    keys(replay, {"interface_rows", "positive_shift_windows", "negative_shift_windows", "period_limit", "fixed_rows", "fixed_count_sum", "zeta_degree_limit", "zeta_coefficients"}, "replay keys")
    ck(len(replay["interface_rows"]) == 73, "interface row count")
    for shift, row in zip(range(-36, 37), replay["interface_rows"]):
        left, right = -shift - 1, -shift
        expected = {"shift": shift, "interface_left_coordinate": left, "interface_right_coordinate": right, "interface_pair": [symbol(shift, left), symbol(shift, right)], "window_radius_4": [symbol(shift, j) for j in range(left - 3, right + 4)]}
        ck(row == expected, f"interface row {shift}")
        ck(row["interface_pair"] == [4, 0], f"unique pair {shift}")
        ck(sum(1 for j in range(left - 20, right + 20) if symbol(shift, j) in (2, 3, 4) and symbol(shift, j + 1) in (0, 1)) == 1, f"single transition {shift}")

    ck(len(replay["positive_shift_windows"]) == 7, "positive rows")
    for row in replay["positive_shift_windows"]:
        shift, radius = row["shift"], row["radius"]
        expected_word = [symbol(shift, j) for j in range(-radius, radius + 1)]
        ck(row["central_word"] == expected_word, f"positive word {shift}")
        ck(row["all_symbols_binary"] is (shift >= radius), f"positive binary {shift}")

    ck(len(replay["negative_shift_windows"]) == 9, "negative rows")
    for row in replay["negative_shift_windows"]:
        shift, radius = row["shift"], row["radius"]
        word = [symbol(shift, j) for j in range(-radius, radius + 1)]
        ck(row["minus_shift_mod_3"] == (-shift) % 3, f"negative residue {shift}")
        ck(row["central_word"] == word, f"negative word {shift}")
        ck(row["period_three_check"] is True and all(word[q] == word[q + 3] for q in range(len(word) - 3)), f"negative periodic {shift}")

    ck(replay["period_limit"] == len(replay["fixed_rows"]) == 60, "period count")
    exact_lookup = {}
    for n, row in enumerate(replay["fixed_rows"], 1):
        fixed = 3 if n % 3 == 0 else 0
        exact = sum(mu(n // d) * (3 if d % 3 == 0 else 0) for d in divisors(n))
        expected = {"period_n": n, "fixed_points": fixed, "fixed_labels": [f"y_phase_{j}" for j in range(3)] if fixed else [], "exact_period_points": exact, "primitive_cycles": exact // n}
        ck(row == expected, f"fixed row n={n}")
        ck(exact >= 0 and exact % n == 0, f"integrality n={n}")
        exact_lookup[n] = exact
    ck(exact_lookup[3] == 3 and sum(exact_lookup.values()) == 3, "unique primitive support")
    ck(replay["fixed_count_sum"] == 60, "fixed sum")
    ck(replay["zeta_degree_limit"] == 36 and replay["zeta_coefficients"] == [1 if n % 3 == 0 else 0 for n in range(37)], "zeta coefficients")

    progress = data["progress_and_boundary"]
    keys(progress, {"progress", "structural_cost", "route_a_obstruction"}, "progress keys")
    ck("dense two-sided heteroclinic Z-orbit" in progress["progress"], "progress")
    ck("forward topological transitivity" in progress["structural_cost"] and "wandering" in progress["structural_cost"], "cost")
    ck("no frozen target divisor" in progress["route_a_obstruction"], "boundary")
    route = data["route_a"]
    keys(route, {"tuple", "overall", "A1_qualification", "A2_qualification", "A3_qualification", "A4_qualification", "route_b_invocation_allowed"}, "route keys")
    ck(route["tuple"] == ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"], "tuple")
    ck(route["overall"] == "ROUTE_A_EXPLORATORY", "overall")
    ck(route["A1_qualification"] == "INTRINSIC_PERIOD_THREE_SKELETON_IN_ONE_DENSE_TWO_SIDED_HETEROCLINIC_ORBIT_CLOSURE", "A1")
    ck(route["A2_qualification"] == "ELEMENTARY_SINGLE_FACTOR_SOURCE_ZETA_WITH_NO_TARGET_DIVISOR_COMPARISON", "A2")
    ck(route["A3_qualification"] == "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_OR_CONTINUATION_COMPARISON", "A3")
    ck(route["A4_qualification"] == "NO_NATURAL_UNITARY_SCATTERING_OR_HAMILTONIAN_LIFT", "A4")
    ck(route["route_b_invocation_allowed"] is False, "Route B")
    flags = data["scope_flags"]
    keys(flags, {"scope", "uses_prime_table", "uses_zero_table", "claims_arithmetic_euler_factors", "claims_root_number", "claims_automorphy", "claims_hilbert_polya", "uses_route_b_inputs"}, "flags")
    ck(flags["scope"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "flag scope")
    for key, value in flags.items():
        if key != "scope":
            ck(value is False, f"false flag {key}")
    ck(data["nonclaims"] == ["that X is minimal or almost minimal", "that the interface orbit contributes recurrent or periodic points", "an arithmetic Euler product or local factorization", "a target divisor, functional equation, or counting-law match", "a natural self-adjoint Hilbert--Polya operator", "Route-B authorization or a solution of the larger program"], "nonclaims")
    print(json.dumps({"status": "C154_CHECK_PASS", "checks": checks, "evidence": str(path)}, sort_keys=True))


if __name__ == "__main__":
    main()
