#!/usr/bin/env python3
"""Independent matrix checker for C145; imports no producer code."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c145_rule90_evidence.json"


def matrix_multiply(left: list[int], right: list[int]) -> list[int]:
    out = []
    for row in left:
        value = 0
        bits = row
        while bits:
            lowest = bits & -bits
            value ^= right[lowest.bit_length() - 1]
            bits ^= lowest
        out.append(value)
    return out


def matrix_power(base: list[int], exponent: int) -> list[int]:
    result = [1 << i for i in range(len(base))]
    while exponent:
        if exponent & 1:
            result = matrix_multiply(result, base)
        base = matrix_multiply(base, base)
        exponent >>= 1
    return result


def rule90_matrix(length: int) -> list[int]:
    rows = []
    for i in range(length):
        row = 0
        row ^= 1 << ((i - 1) % length)
        row ^= 1 << ((i + 1) % length)
        rows.append(row)
    return rows


def rank(rows: list[int]) -> int:
    work = rows[:]
    pivot_row = 0
    columns = len(rows)
    for column in range(columns):
        pivot = next((r for r in range(pivot_row, len(work)) if (work[r] >> column) & 1), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        for r in range(len(work)):
            if r != pivot_row and ((work[r] >> column) & 1):
                work[r] ^= work[pivot_row]
        pivot_row += 1
    return pivot_row


def kernel_dimension(length: int, time: int) -> int:
    powered = matrix_power(rule90_matrix(length), time)
    difference = [row ^ (1 << i) for i, row in enumerate(powered)]
    return length - rank(difference)


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mu(n: int) -> int:
    count = 0
    divisor = 2
    value = n
    while divisor * divisor <= value:
        exponent = 0
        while value % divisor == 0:
            value //= divisor
            exponent += 1
        if exponent > 1:
            return 0
        if exponent == 1:
            count += 1
        divisor += 1
    if value > 1:
        count += 1
    return -1 if count & 1 else 1


def expected_row(length: int, time: int, fixed_lookup: dict[tuple[int, int], int] | None = None) -> dict:
    fixed = 1 << kernel_dimension(length, time)
    if fixed_lookup is None:
        fixed_lookup = {(length, d): 1 << kernel_dimension(length, d) for d in divisors(time)}
    exact = sum(mu(time // d) * fixed_lookup[(length, d)] for d in divisors(time))
    return {
        "spatial_length_L": length,
        "temporal_period_n": time,
        "area_Ln": length * time,
        "gcd_degree": kernel_dimension(length, time),
        "fixed_points": fixed,
        "exact_temporal_period_points": exact,
        "primitive_temporal_cycles": exact // time,
    }


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_EVIDENCE
    data = json.loads(path.read_text())
    checks = 0

    def ck(condition: bool, label: str) -> None:
        nonlocal checks
        if not condition:
            raise AssertionError(label)
        checks += 1

    def keys(mapping: dict, expected: set[str], label: str) -> None:
        ck(set(mapping) == expected, label)

    keys(data, {"schema", "candidate_id", "date_utc", "scope_literal", "source_lock", "kernel_gcd_theorem", "mobius_orbit_theorem", "two_clock_table", "spatiotemporal_torus", "aspect_ratio_witnesses", "even_length_control", "progress_and_boundary", "route_a", "scope_flags", "nonclaims", "payload_sha256"}, "top keys")
    ck(data["schema"] == "HCS-C145-v1", "schema")
    ck(data["candidate_id"] == "HCS-C145", "candidate")
    ck(data["date_utc"] == "2026-08-25", "date")
    ck(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    ck(data["payload_sha256"] == payload_hash(data), "payload hash")

    lock = data["source_lock"]
    keys(lock, {"object", "clock", "normalization", "determinant_convention", "precision", "cutoff", "allowed_data", "forbidden_data"}, "lock keys")
    ck("Rule-90" in lock["object"] and "x+x^{-1}" in lock["object"], "object")
    ck(lock["clock"] == "the ordered pair (spatial circumference L, temporal iterate n)", "clock")
    ck(lock["normalization"].startswith("Fix(L,n) counts labeled"), "normalization")
    ck(lock["determinant_convention"].startswith("no single-variable determinant"), "determinant boundary")
    ck(lock["cutoff"].endswith("1<=L,n<=24"), "cutoff")
    ck("Route-B inputs" in lock["forbidden_data"], "forbidden")

    theorem = data["kernel_gcd_theorem"]
    keys(theorem, {"statement", "laurent_clearance", "kernel_lemma", "kernel_proof", "non_squarefree_scope", "all_positive_lengths_and_times"}, "kernel theorem keys")
    ck(theorem["statement"] == "#Fix(F_L^n)=2^deg(gcd(x^L+1,(x^2+1)^n+x^n)) for all L,n>=1 over F_2", "theorem statement")
    ck(theorem["laurent_clearance"].startswith("x^n((x+x^{-1})^n-1)="), "clearance")
    ck(theorem["kernel_lemma"].startswith("for monic f and h"), "kernel lemma")
    ck("f_1|q" in theorem["kernel_proof"], "kernel proof")
    ck("not distinct roots" in theorem["non_squarefree_scope"], "non-squarefree scope")
    ck(theorem["all_positive_lengths_and_times"] is True, "all sizes")

    table = data["two_clock_table"]
    keys(table, {"spatial_limit", "temporal_limit", "cell_count", "rows", "fixed_point_sum", "exact_period_point_sum", "primitive_cycle_sum"}, "table keys")
    ck(table["spatial_limit"] == table["temporal_limit"] == 24, "limits")
    ck(table["cell_count"] == len(table["rows"]) == 576, "cells")
    fixed_lookup = {}
    for length in range(1, 25):
        for time in range(1, 25):
            fixed_lookup[(length, time)] = 1 << kernel_dimension(length, time)
    rebuilt = []
    fixed_sum = exact_sum = cycle_sum = 0
    for index, receipt in enumerate(table["rows"]):
        length = index // 24 + 1
        time = index % 24 + 1
        expected = expected_row(length, time, fixed_lookup)
        ck(receipt == expected, f"matrix row L={length} n={time}")
        ck(receipt["fixed_points"] == 1 << receipt["gcd_degree"], f"power of two L={length} n={time}")
        ck(receipt["exact_temporal_period_points"] >= 0, f"nonnegative exact L={length} n={time}")
        ck(receipt["exact_temporal_period_points"] % time == 0, f"cycle divisibility L={length} n={time}")
        if length <= 8 and time <= 8:
            matrix = matrix_power(rule90_matrix(length), time)
            brute = 0
            for state in range(1 << length):
                image = 0
                for i, row in enumerate(matrix):
                    if (row & state).bit_count() & 1:
                        image |= 1 << i
                ck(0 <= image < (1 << length), f"image range L={length} n={time} state={state}")
                brute += image == state
            ck(brute == receipt["fixed_points"], f"brute fixed L={length} n={time}")
        rebuilt.append(expected)
        fixed_sum += expected["fixed_points"]
        exact_sum += expected["exact_temporal_period_points"]
        cycle_sum += expected["primitive_temporal_cycles"]
    ck(table["rows"] == rebuilt, "all rebuilt rows")
    ck(table["fixed_point_sum"] == fixed_sum, "fixed sum")
    ck(table["exact_period_point_sum"] == exact_sum, "exact sum")
    ck(table["primitive_cycle_sum"] == cycle_sum, "cycle sum")

    mobius = data["mobius_orbit_theorem"]
    keys(mobius, {"exact_period_formula", "cycle_formula", "integrality_reason", "point_cycle_boundary"}, "mobius keys")
    ck(mobius["exact_period_formula"] == "P_L(n)=sum_(d|n) mu(n/d) Fix(L,d)", "Mobius formula")
    ck(mobius["cycle_formula"] == "C_L(n)=P_L(n)/n", "cycle formula")
    ck("partitioned" in mobius["integrality_reason"], "integrality")
    ck("distinct quantities" in mobius["point_cycle_boundary"], "quantity boundary")

    torus = data["spatiotemporal_torus"]
    keys(torus, {"equations", "bijection", "torus_count"}, "torus keys")
    ck(torus["equations"].startswith("u_(i,j+1)="), "torus equation")
    ck("uniquely determined" in torus["bijection"], "torus bijection")
    ck(torus["torus_count"].endswith("Fix(L,n)"), "torus count")

    witnesses = data["aspect_ratio_witnesses"]
    keys(witnesses, {"global_positive_domain", "nondegenerate_domain", "nonzero_exact_period_domain", "same_fixed_count_different_primitive_structure", "conclusion"}, "witness keys")
    rows = table["rows"]
    def first_area(nondegenerate: bool, require_nonzero: bool = False) -> dict:
        selected = [r for r in rows if not nondegenerate or (r["spatial_length_L"] >= 2 and r["temporal_period_n"] >= 2)]
        for area in range(1, 577):
            group = [r for r in selected if r["area_Ln"] == area]
            if len({r["fixed_points"] for r in group}) > 1 and (not require_nonzero or any(r["exact_temporal_period_points"] > 0 for r in group)):
                return {"area": area, "cells": group}
        raise AssertionError("missing area witness")
    ck(witnesses["global_positive_domain"]["minimal_same_area_with_different_fixed_counts"] == first_area(False), "global area witness")
    ck(witnesses["global_positive_domain"]["minimal_same_area_with_different_fixed_counts"]["area"] == 3, "global minimum area")
    ck(witnesses["nondegenerate_domain"]["minimal_same_area_with_different_fixed_counts"] == first_area(True), "nondegenerate area witness")
    ck(witnesses["nondegenerate_domain"]["minimal_same_area_with_different_fixed_counts"]["area"] == 6, "nondegenerate minimum area")
    ck(witnesses["nonzero_exact_period_domain"]["minimal_same_area_with_different_fixed_counts"] == first_area(True, True), "nonzero area witness")
    ck(witnesses["nonzero_exact_period_domain"]["minimal_same_area_with_different_fixed_counts"]["area"] == 12, "nonzero minimum area")
    control = witnesses["same_fixed_count_different_primitive_structure"]
    ck(control["first_cell"] == rebuilt[(5 - 1) * 24 + 2], "control first")
    ck(control["second_cell"] == rebuilt[(5 - 1) * 24 + 5], "control second")
    ck(control["first_cell"]["fixed_points"] == control["second_cell"]["fixed_points"] == 16, "same fixed count")
    ck(control["first_cell"]["exact_temporal_period_points"] == 15 and control["second_cell"]["exact_temporal_period_points"] == 0, "different primitive content")
    ck(witnesses["conclusion"].startswith("area Ln and a single fixed-point count"), "witness conclusion")

    even = data["even_length_control"]
    keys(even, {"cell", "factorization", "purpose"}, "even keys")
    ck(even["cell"] == rebuilt[(6 - 1) * 24 + 1], "even cell")
    ck(even["factorization"] == "x^6+1=(x^3+1)^2 over F_2", "even factorization")
    ck("non-squarefree" in even["purpose"], "even purpose")

    boundary = data["progress_and_boundary"]
    keys(boundary, {"progress", "two_clock_obstruction", "route_a_obstruction"}, "boundary keys")
    ck("all-size exact" in boundary["progress"], "progress")
    ck("aspect ratio" in boundary["two_clock_obstruction"], "two-clock obstruction")
    ck("no single frozen" in boundary["route_a_obstruction"], "route obstruction")

    route = data["route_a"]
    keys(route, {"tuple", "overall", "A1_qualification", "A2_qualification", "A3_qualification", "A4_qualification", "route_b_invocation_allowed"}, "route keys")
    ck(route["tuple"] == ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"], "tuple")
    ck(route["overall"] == "ROUTE_A_EXPLORATORY", "overall")
    ck(route["route_b_invocation_allowed"] is False, "Route B")
    ck(route["A1_qualification"].startswith("EXACT_INTRINSIC_FINITE_VOLUME"), "A1")
    ck(route["A2_qualification"] == "NO_SINGLE_FROZEN_CLOCK_OR_TARGET_DIVISOR_DETERMINANT", "A2")

    flags = data["scope_flags"]
    keys(flags, {"scope", "uses_prime_table", "uses_zero_table", "claims_arithmetic_euler_factors", "claims_root_number", "claims_automorphy", "claims_hilbert_polya", "uses_route_b_inputs"}, "flags")
    ck(flags["scope"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "flag scope")
    for name, value in flags.items():
        if name != "scope":
            ck(value is False, f"false flag {name}")
    ck(data["nonclaims"] == [
        "a thermodynamic or infinite-volume limit of the two-clock table",
        "that area alone determines spatiotemporal periodic geometry",
        "an arithmetic Euler product or local factorization",
        "a target divisor, functional equation, or counting-law match",
        "a natural self-adjoint Hilbert--Polya operator",
        "Route-B authorization or a solution of the larger program",
    ], "nonclaims")

    print(json.dumps({"status": "C145_CHECK_PASS", "checks": checks, "evidence": str(path)}, sort_keys=True))


if __name__ == "__main__":
    main()
