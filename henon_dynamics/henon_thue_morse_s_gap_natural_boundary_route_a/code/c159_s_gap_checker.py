#!/usr/bin/env python3
"""Producer-independent standard-library checker for HCS-C159."""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c159_s_gap_evidence.json"
checks = 0


def require(condition: bool, message: str) -> None:
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)


def parity(n: int) -> int:
    result = 0
    while n:
        result ^= n & 1
        n >>= 1
    return result


def divisors(n: int) -> list[int]:
    result = []
    for d in range(1, n + 1):
        if n % d == 0:
            result.append(d)
    return result


def mu(n: int) -> int:
    sign = 1
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            n //= divisor
            sign = -sign
            if n % divisor == 0:
                return 0
            while n % divisor == 0:
                n //= divisor
        divisor += 1
    if n > 1:
        sign = -sign
    return sign


def cyclic_ok(word: tuple[int, ...]) -> bool:
    positions = [i for i, value in enumerate(word) if value]
    if not positions:
        return True
    for i, position in enumerate(positions):
        following = positions[(i + 1) % len(positions)]
        if parity((following - position - 1) % len(word)) == 0:
            return False
    return True


def independent_fixed(n: int) -> int:
    total = 0
    for encoded in range(2**n):
        word = tuple((encoded // (2**position)) % 2 for position in range(n))
        total += cyclic_ok(word)
    return total


def fraction(record: dict) -> Fraction:
    require(set(record) == {"numerator", "denominator"}, "bad fraction schema")
    return Fraction(record["numerator"], record["denominator"])


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    data = json.loads(path.read_text())
    body = dict(data)
    claimed = body.pop("payload_sha256")
    encoded = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    require(claimed == sha256(encoded).hexdigest(), "payload hash mismatch")
    require(set(data) == {"schema", "candidate_id", "date_utc", "source_commit", "scope_literal", "source_lock", "pivot_record", "renewal_dynamics_theorem", "exact_zeta_theorem", "natural_boundary_theorem", "finite_replay", "progress_and_boundary", "route_a", "scope_flags", "nonclaims", "payload_sha256"}, "top-level closure")
    require(data["schema"] == "HCS-C159-v1", "schema")
    require(data["candidate_id"] == "HCS-C159", "candidate")
    require(data["date_utc"] == "2026-08-25", "date")
    require(data["source_commit"] == "63f75cf476711de93e6096ef74ac16969e1127d0", "commit")
    require(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")

    lock = data["source_lock"]
    require(set(lock) == {"object", "family", "clock", "normalization", "cutoff", "precision", "allowed_data", "forbidden_data"}, "source lock closure")
    require("S-gap shift" in lock["object"] and "t_s=1" in lock["object"], "object")
    require("infinite synchronized renewal" in lock["family"], "family")
    require(lock["clock"] == "one left shift; primitive period is the least positive shift return", "clock")
    require("labeled fixed points" in lock["normalization"], "normalization")
    require("n<=18" in lock["cutoff"] and "degree<=48" in lock["cutoff"], "cutoff")
    require(lock["precision"].startswith("exact integers"), "precision")
    require("Thue--Morse" in lock["allowed_data"], "allowed")
    require("Route-B inputs" in lock["forbidden_data"], "forbidden")

    pivot = data["pivot_record"]
    require(set(pivot) == {"rejected_candidate", "reason", "replacement", "bug_or_failure_reframed_as_insight"}, "pivot closure")
    require(pivot["rejected_candidate"] == "q-clock-decorated Sturmian shift", "pivot candidate")
    require("C144" in pivot["reason"], "pivot reason")
    require("natural-boundary" in pivot["replacement"], "pivot replacement")
    require(pivot["bug_or_failure_reframed_as_insight"] is False, "pivot integrity")

    theorem = data["renewal_dynamics_theorem"]
    require(set(theorem) == {"gap_set", "code", "short_code_lengths", "unique_circular_parse", "mixing", "dense_periodic_points", "recurrent_progress"}, "renewal theorem closure")
    require(theorem["gap_set"] == "S={s>=0:t_s=1}", "gap set")
    require(theorem["code"] == "C={10^s:s in S}", "code")
    require(theorem["short_code_lengths"] == [2, 3], "short lengths")
    require("unique cyclic decomposition" in theorem["unique_circular_parse"], "parse")
    require("topologically mixing" in theorem["mixing"], "mixing")
    require("periodic concatenation" in theorem["dense_periodic_points"], "dense periodic")
    require("recurrent transitive points" in theorem["recurrent_progress"], "recurrence")

    replay = data["finite_replay"]
    require(set(replay) == {"tm_prefix_length", "tm_prefix", "s_prefix", "code_lengths_prefix", "period_limit", "fixed_rows", "series_limit", "P_coefficients", "renewal_coefficients", "zeta_coefficients", "denominator_coefficients", "dyadic_boundary_rows"}, "replay closure")
    require(replay["tm_prefix_length"] == 256, "prefix length")
    require(len(replay["tm_prefix"]) == 256, "prefix array length")
    for index, value in enumerate(replay["tm_prefix"]):
        require(value == parity(index), f"tm[{index}]")
    expected_s = [index for index in range(256) if parity(index)]
    require(replay["s_prefix"] == expected_s, "S prefix")
    require(replay["code_lengths_prefix"] == [value + 1 for value in expected_s], "code lengths")

    require(replay["period_limit"] == 18 and len(replay["fixed_rows"]) == 18, "period ledger extent")
    fixed = [0]
    for n, row in enumerate(replay["fixed_rows"], 1):
        require(set(row) == {"period_n", "fixed_points", "exact_period_points", "primitive_cycles"}, f"fixed row {n} closure")
        require(row["period_n"] == n, f"period row {n}")
        count = independent_fixed(n)
        require(row["fixed_points"] == count, f"fixed count {n}")
        fixed.append(count)
        exact = sum(mu(n // d) * fixed[d] for d in divisors(n))
        require(row["exact_period_points"] == exact, f"exact points {n}")
        require(row["primitive_cycles"] == exact // n and exact % n == 0, f"cycles {n}")

    limit = replay["series_limit"]
    require(limit == 48, "series limit")
    for key in ("P_coefficients", "renewal_coefficients", "zeta_coefficients", "denominator_coefficients"):
        require(len(replay[key]) == limit + 1, f"{key} length")
    product_coeffs = [0] * (limit + 1)
    product_coeffs[0] = 1
    exponent = 1
    while exponent <= limit:
        prior = product_coeffs[:]
        for n in range(exponent, limit + 1):
            product_coeffs[n] -= prior[n - exponent]
        exponent *= 2
    for n, value in enumerate(product_coeffs):
        require(value == 1 - 2 * parity(n), f"product identity {n}")
        require(replay["P_coefficients"][n] == value, f"P coeff {n}")

    renewal = [0] * (limit + 1)
    renewal[0] = 1
    for n in range(1, limit + 1):
        renewal[n] = sum(parity(k - 1) * renewal[n - k] for k in range(1, n + 1))
    zeta = []
    accumulator = 0
    for n, value in enumerate(renewal):
        accumulator += value
        zeta.append(accumulator)
        require(replay["renewal_coefficients"][n] == value, f"renewal {n}")
        require(replay["zeta_coefficients"][n] == accumulator, f"zeta {n}")
    denominator = [0] * (limit + 1)
    denominator[0] = 2
    denominator[1] = -3
    for n, value in enumerate(product_coeffs):
        if n + 1 <= limit:
            denominator[n + 1] += value
        if n + 2 <= limit:
            denominator[n + 2] -= value
    for n, value in enumerate(denominator):
        require(replay["denominator_coefficients"][n] == value, f"denominator {n}")
        convolution = sum(value2 * zeta[n - k] for k, value2 in enumerate(denominator[:n + 1]))
        require(convolution == (2 if n == 0 else 0), f"zeta inverse {n}")
    for n in range(1, 19):
        require(n * zeta[n] == sum(fixed[k] * zeta[n - k] for k in range(1, n + 1)), f"log derivative {n}")

    exact = data["exact_zeta_theorem"]
    require(set(exact) == {"T", "P", "relation", "renewal_series", "zeta_renewal", "zeta_product", "entropy", "entropy_root_bracket"}, "zeta theorem closure")
    require(exact["T"] == "T(z)=sum_{s>=0}t_s z^s", "T")
    require(exact["P"].startswith("P(z)=prod"), "P")
    require(exact["relation"] == "T(z)=(1/(1-z)-P(z))/2", "T relation")
    require(exact["renewal_series"].startswith("F(z)=zT(z)"), "F")
    require(exact["zeta_renewal"] == "zeta_X(z)=1/((1-z)(1-F(z)))", "renewal zeta")
    require(exact["zeta_product"] == "zeta_X(z)=2/(2-3z+z(1-z)P(z))", "product zeta")
    require("unique real solution" in exact["entropy"], "entropy statement")
    bracket = exact["entropy_root_bracket"]
    require(set(bracket) == {"lower", "upper", "tail_cutoff", "lower_F_upper_bound", "upper_F_lower_bound"}, "bracket closure")
    lower = fraction(bracket["lower"])
    upper = fraction(bracket["upper"])
    require(lower == Fraction(67633710444063914, 10**17), "lower endpoint")
    require(upper == Fraction(67633710444063915, 10**17), "upper endpoint")
    require(bracket["tail_cutoff"] == 256, "tail cutoff")
    lower_partial = sum(Fraction(parity(s)) * lower ** (s + 1) for s in range(257))
    lower_bound = lower_partial + lower ** 258 / (1 - lower)
    upper_partial = sum(Fraction(parity(s)) * upper ** (s + 1) for s in range(257))
    require(fraction(bracket["lower_F_upper_bound"]) == lower_bound < 1, "lower root certificate")
    require(fraction(bracket["upper_F_lower_bound"]) == upper_partial > 1, "upper root certificate")

    boundary = data["natural_boundary_theorem"]
    require(set(boundary) == {"radial_zero_set", "density", "identity_argument", "transfer_to_zeta", "conclusion"}, "boundary closure")
    require("dyadic root" in boundary["radial_zero_set"], "radial zeros")
    require(boundary["density"] == "dyadic roots of unity are dense on |z|=1", "density")
    require("isolated poles" in boundary["identity_argument"] and "identically zero" in boundary["identity_argument"], "identity proof")
    require("P=(2/zeta-2+3z)/(z(1-z))" in boundary["transfer_to_zeta"], "zeta transfer")
    require("unit circle is a natural boundary" in boundary["conclusion"], "boundary conclusion")
    require(len(replay["dyadic_boundary_rows"]) == 10, "dyadic rows")
    for level, row in enumerate(replay["dyadic_boundary_rows"], 1):
        require(row == {"level": level, "root_order": 2**level, "distinct_roots": 2**level, "vanishing_factor": f"1-z^{2**level}"}, f"dyadic row {level}")

    progress = data["progress_and_boundary"]
    require(set(progress) == {"progress", "route_a_obstruction"}, "progress closure")
    require("mixing recurrent" in progress["progress"] and "natural boundary" in progress["progress"], "clear progress")
    require("no target divisor" in progress["route_a_obstruction"], "obstruction")
    route = data["route_a"]
    require(route["tuple"] == ["A1_WEAK", "A2_FAIL", "A3_PARTIAL_ANALYTIC_STRUCTURE", "A4_FAIL"], "route tuple")
    require(route["overall"] == "ROUTE_A_EXPLORATORY", "overall")
    require(route["route_b_invocation_allowed"] is False, "route B")
    require(set(route) == {"tuple", "overall", "A1_qualification", "A2_qualification", "A3_qualification", "A4_qualification", "route_b_invocation_allowed"}, "route closure")
    flags = data["scope_flags"]
    require(flags == {"scope": "NO_BAD_EULER_OR_ROOT_NUMBER", "uses_prime_table": False, "uses_zero_table": False, "claims_arithmetic_euler_factors": False, "claims_root_number": False, "claims_automorphy": False, "claims_hilbert_polya": False, "uses_route_b_inputs": False}, "scope flags")
    require(data["nonclaims"] == [
        "that the source zeta natural boundary is a target critical line or target divisor",
        "an arithmetic Euler product or local factorization",
        "a target functional equation or counting-law match",
        "a natural self-adjoint Hilbert--Polya operator",
        "Route-B authorization or a solution of the larger program",
    ], "nonclaims exact boundary")
    print(json.dumps({"status": "C159_CHECKER_PASS", "assertions": checks, "payload_sha256": claimed}, sort_keys=True))


if __name__ == "__main__":
    main()
