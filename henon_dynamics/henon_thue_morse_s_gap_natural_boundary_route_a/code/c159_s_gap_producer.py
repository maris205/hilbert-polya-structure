#!/usr/bin/env python3
"""Produce the exact HCS-C159 Thue--Morse S-gap certificate."""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
from math import prod
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c159_s_gap_evidence.json"
SOURCE_COMMIT = "63f75cf476711de93e6096ef74ac16969e1127d0"
PERIOD_LIMIT = 18
SERIES_LIMIT = 48
ENTROPY_TAIL = 256


def thue_morse(n: int) -> int:
    return n.bit_count() & 1


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


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def valid_cyclic_word(mask: int, length: int) -> bool:
    ones = [j for j in range(length) if (mask >> j) & 1]
    if not ones:
        return True
    for index, left in enumerate(ones):
        right = ones[(index + 1) % len(ones)]
        gap = (right - left - 1) % length
        if thue_morse(gap) != 1:
            return False
    return True


def fixed_count(length: int) -> int:
    return sum(valid_cyclic_word(mask, length) for mask in range(1 << length))


def product_coefficients(limit: int) -> list[int]:
    coefficients = [0] * (limit + 1)
    coefficients[0] = 1
    power = 1
    while power <= limit:
        updated = coefficients[:]
        for degree in range(power, limit + 1):
            updated[degree] -= coefficients[degree - power]
        coefficients = updated
        power *= 2
    return coefficients


def renewal_and_zeta_coefficients(limit: int) -> tuple[list[int], list[int]]:
    renewal = [0] * (limit + 1)
    renewal[0] = 1
    for n in range(1, limit + 1):
        renewal[n] = sum(thue_morse(k - 1) * renewal[n - k] for k in range(1, n + 1))
    zeta = []
    running = 0
    for value in renewal:
        running += value
        zeta.append(running)
    return renewal, zeta


def f_bounds(value: Fraction, tail_start: int) -> tuple[Fraction, Fraction]:
    partial = sum(Fraction(thue_morse(s)) * value ** (s + 1) for s in range(tail_start + 1))
    tail = value ** (tail_start + 2) / (1 - value)
    return partial, partial + tail


def fraction_record(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def payload_bytes(data: dict) -> bytes:
    body = dict(data)
    body.pop("payload_sha256", None)
    return json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def build() -> dict:
    tm_prefix = [thue_morse(n) for n in range(256)]
    s_prefix = [n for n, bit in enumerate(tm_prefix) if bit]
    code_lengths = [s + 1 for s in s_prefix]
    assert 2 in code_lengths and 3 in code_lengths

    product_rows = product_coefficients(SERIES_LIMIT)
    signed_tm = [1 - 2 * thue_morse(n) for n in range(SERIES_LIMIT + 1)]
    assert product_rows == signed_tm
    renewal, zeta = renewal_and_zeta_coefficients(SERIES_LIMIT)

    fixed_rows = []
    fixed = [0]
    for n in range(1, PERIOD_LIMIT + 1):
        count = fixed_count(n)
        fixed.append(count)
        exact = sum(mobius(n // d) * fixed[d] for d in divisors(n))
        assert exact >= 0 and exact % n == 0
        fixed_rows.append({
            "period_n": n,
            "fixed_points": count,
            "exact_period_points": exact,
            "primitive_cycles": exact // n,
        })
    for n in range(1, PERIOD_LIMIT + 1):
        lhs = n * zeta[n]
        rhs = sum(fixed[k] * zeta[n - k] for k in range(1, n + 1))
        assert lhs == rhs

    denominator = [0] * (SERIES_LIMIT + 1)
    denominator[0] = 2
    if SERIES_LIMIT >= 1:
        denominator[1] = -3
    for n, coefficient in enumerate(product_rows):
        if n + 1 <= SERIES_LIMIT:
            denominator[n + 1] += coefficient
        if n + 2 <= SERIES_LIMIT:
            denominator[n + 2] -= coefficient
    convolution = [sum(denominator[k] * zeta[n - k] for k in range(n + 1)) for n in range(SERIES_LIMIT + 1)]
    assert convolution == [2] + [0] * SERIES_LIMIT

    lower = Fraction(67633710444063914, 10**17)
    upper = Fraction(67633710444063915, 10**17)
    lower_partial, lower_upper = f_bounds(lower, ENTROPY_TAIL)
    upper_partial, upper_upper = f_bounds(upper, ENTROPY_TAIL)
    assert lower_upper < 1 < upper_partial

    dyadic_levels = []
    for level in range(1, 11):
        order = 1 << level
        dyadic_levels.append({
            "level": level,
            "root_order": order,
            "distinct_roots": order,
            "vanishing_factor": f"1-z^{order}",
        })

    data = {
        "schema": "HCS-C159-v1",
        "candidate_id": "HCS-C159",
        "date_utc": "2026-08-25",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "source_lock": {
            "object": "the binary S-gap shift X_S with S={s>=0: t_s=1} and t_s the Thue--Morse digit-sum parity",
            "family": "one infinite synchronized renewal shift generated by code words 10^s, s in S, together with its all-zero limit point",
            "clock": "one left shift; primitive period is the least positive shift return",
            "normalization": "labeled fixed points, exact-period points, and geometric primitive cycles; Artin--Mazur zeta has constant term one",
            "cutoff": "all mixing, zeta, entropy-root, and natural-boundary statements are all-parameter theorems; finite fixed ledgers use n<=18 and formal series use degree<=48",
            "precision": "exact integers and rational entropy brackets; no floating-point input enters a theorem",
            "allowed_data": "the source-defined Thue--Morse parity sequence, its renewal code, and exact symbolic enumeration",
            "forbidden_data": "target zero or prime tables, arithmetic/local factors, root numbers, automorphy, Hilbert--Polya operators, and Route-B inputs",
        },
        "pivot_record": {
            "rejected_candidate": "q-clock-decorated Sturmian shift",
            "reason": "its periodic-point vacuum and zeta=1 duplicated the central C144 obstruction too closely",
            "replacement": "Thue--Morse S-gap renewal shift with recurrent mixing, nontrivial dense periodic structure, and an analytic natural-boundary theorem",
            "bug_or_failure_reframed_as_insight": False,
        },
        "renewal_dynamics_theorem": {
            "gap_set": "S={s>=0:t_s=1}",
            "code": "C={10^s:s in S}",
            "short_code_lengths": [2, 3],
            "unique_circular_parse": "every periodic point containing a 1 has a unique cyclic decomposition into words 10^s",
            "mixing": "code lengths 2 and 3 generate every sufficiently large connector length, so X_S is topologically mixing",
            "dense_periodic_points": "every cylinder is met by a periodic concatenation; arbitrarily long allowed gaps approximate the all-zero point",
            "recurrent_progress": "admissible interfaces recur inside periodic concatenations and the shift has recurrent transitive points",
        },
        "exact_zeta_theorem": {
            "T": "T(z)=sum_{s>=0}t_s z^s",
            "P": "P(z)=prod_{j>=0}(1-z^(2^j))=sum_{s>=0}(-1)^(t_s)z^s",
            "relation": "T(z)=(1/(1-z)-P(z))/2",
            "renewal_series": "F(z)=zT(z)=sum_{s in S}z^(s+1)",
            "zeta_renewal": "zeta_X(z)=1/((1-z)(1-F(z)))",
            "zeta_product": "zeta_X(z)=2/(2-3z+z(1-z)P(z))",
            "entropy": "h_top=-log R, where R in (0,1) is the unique real solution F(R)=1",
            "entropy_root_bracket": {"lower": fraction_record(lower), "upper": fraction_record(upper), "tail_cutoff": ENTROPY_TAIL, "lower_F_upper_bound": fraction_record(lower_upper), "upper_F_lower_bound": fraction_record(upper_partial)},
        },
        "natural_boundary_theorem": {
            "radial_zero_set": "P(r omega)->0 for every dyadic root of unity omega as r increases to 1",
            "density": "dyadic roots of unity are dense on |z|=1",
            "identity_argument": "a meromorphic continuation across an arc has isolated poles; radial zeros make each dyadic root there a zero or removable point, forcing P identically zero",
            "transfer_to_zeta": "a meromorphic continuation of zeta across an arc would give P=(2/zeta-2+3z)/(z(1-z)) on a subarc avoiding z=1",
            "conclusion": "the unit circle is a natural boundary for the source-defined meromorphic continuation of zeta_X",
        },
        "finite_replay": {
            "tm_prefix_length": len(tm_prefix),
            "tm_prefix": tm_prefix,
            "s_prefix": s_prefix,
            "code_lengths_prefix": code_lengths,
            "period_limit": PERIOD_LIMIT,
            "fixed_rows": fixed_rows,
            "series_limit": SERIES_LIMIT,
            "P_coefficients": product_rows,
            "renewal_coefficients": renewal,
            "zeta_coefficients": zeta,
            "denominator_coefficients": denominator,
            "dyadic_boundary_rows": dyadic_levels,
        },
        "progress_and_boundary": {
            "progress": "replaces a one-pass interface and an earlier periodic vacuum by a mixing recurrent symbolic system with exact nontrivial cycles, entropy, zeta, and a proved analytic natural boundary",
            "route_a_obstruction": "the natural boundary is a source obstruction and supplies no target divisor, arithmetic factorization, functional equation comparison, or operator lift",
        },
        "route_a": {
            "tuple": ["A1_WEAK", "A2_FAIL", "A3_PARTIAL_ANALYTIC_STRUCTURE", "A4_FAIL"],
            "overall": "ROUTE_A_EXPLORATORY",
            "A1_qualification": "RECURRENT_MIXING_RENEWAL_DYNAMICS_WITH_DENSE_NONTRIVIAL_PERIODIC_POINTS",
            "A2_qualification": "EXACT_SOURCE_ZETA_AND_ENTROPY_BUT_NO_TARGET_DIVISOR_COMPARISON",
            "A3_qualification": "PROVED_SOURCE_MEROMORPHIC_CONTINUATION_AND_UNIT_CIRCLE_NATURAL_BOUNDARY_WITH_NO_TARGET_GLOBAL_STRUCTURE_COMPARISON",
            "A4_qualification": "NO_NATURAL_UNITARY_SCATTERING_OR_HAMILTONIAN_LIFT",
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
            "uses_route_b_inputs": False,
        },
        "nonclaims": [
            "that the source zeta natural boundary is a target critical line or target divisor",
            "an arithmetic Euler product or local factorization",
            "a target functional equation or counting-law match",
            "a natural self-adjoint Hilbert--Polya operator",
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
    print(json.dumps({"status": "C159_PRODUCER_PASS", "output": str(args.output), "payload_sha256": data["payload_sha256"], "fixed_rows": PERIOD_LIMIT, "series_cells": SERIES_LIMIT + 1}, sort_keys=True))


if __name__ == "__main__":
    main()
