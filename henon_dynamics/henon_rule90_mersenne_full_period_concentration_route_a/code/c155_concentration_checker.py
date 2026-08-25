#!/usr/bin/env python3
"""Independent binary-matrix checker for HCS-C155."""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c155_rule90_concentration_evidence.json"
SOURCE_COMMIT = "506dead810d67fa58fa7c42b2d9a09bfae161059"


def matrix_multiply(left: list[int], right: list[int]) -> list[int]:
    output = []
    for row in left:
        value = 0
        bits = row
        while bits:
            low = bits & -bits
            value ^= right[low.bit_length() - 1]
            bits ^= low
        output.append(value)
    return output


def matrix_power(base: list[int], exponent: int) -> list[int]:
    result = [1 << i for i in range(len(base))]
    while exponent:
        if exponent & 1:
            result = matrix_multiply(result, base)
        base = matrix_multiply(base, base)
        exponent >>= 1
    return result


def rule90(length: int) -> list[int]:
    return [(1 << ((i - 1) % length)) ^ (1 << ((i + 1) % length)) for i in range(length)]


def gf2_rank(rows: list[int]) -> int:
    work = rows[:]
    pivot = 0
    for column in range(len(rows)):
        selected = next((j for j in range(pivot, len(work)) if (work[j] >> column) & 1), None)
        if selected is None:
            continue
        work[pivot], work[selected] = work[selected], work[pivot]
        for j in range(len(work)):
            if j != pivot and ((work[j] >> column) & 1):
                work[j] ^= work[pivot]
        pivot += 1
    return pivot


def fixed_dimension(matrix: list[int], time: int) -> int:
    powered = matrix_power(matrix, time)
    return len(matrix) - gf2_rank([row ^ (1 << i) for i, row in enumerate(powered)])


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mu(n: int) -> int:
    signs = 0
    p = 2
    while p * p <= n:
        exponent = 0
        while n % p == 0:
            n //= p
            exponent += 1
        if exponent > 1:
            return 0
        signs += exponent
        p += 1
    if n > 1:
        signs += 1
    return -1 if signs & 1 else 1


def fraction_record(numerator: int, denominator: int) -> dict:
    value = Fraction(numerator, denominator)
    return {"numerator": value.numerator, "denominator": value.denominator}


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


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

    keys(data, {"schema", "candidate_id", "date_utc", "source_commit", "scope_literal", "source_lock", "periodic_image_theorem", "full_period_concentration_theorem", "finite_replay", "power_of_two_negative_control", "progress_and_boundary", "route_a", "scope_flags", "nonclaims", "payload_sha256"}, "top keys")
    ck(data["schema"] == "HCS-C155-v1", "schema")
    ck(data["candidate_id"] == "HCS-C155", "candidate")
    ck(data["date_utc"] == "2026-08-25", "date")
    ck(data["source_commit"] == SOURCE_COMMIT, "commit")
    ck(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    ck(data["payload_sha256"] == payload_hash(data), "payload hash")

    lock = data["source_lock"]
    keys(lock, {"object", "family", "clock", "normalization", "cutoff", "precision", "allowed_data", "forbidden_data"}, "lock keys")
    ck(lock["object"].startswith("Rule 90, multiplication by a=x+x^{-1}"), "object")
    ck(lock["family"] == "Mersenne circumferences L=2^r-1 for every r>=2", "family")
    ck("periodic image" in lock["clock"], "clock")
    ck(lock["normalization"].startswith("uniform probability on im(a)"), "normalization")
    ck(lock["cutoff"].endswith("2<=s<=8"), "cutoff")
    ck(lock["precision"] == "exact F_2 polynomial arithmetic, integers, and reduced rational numbers", "precision")
    ck("Mersenne/power-of-two" in lock["allowed_data"], "allowed")
    ck("Route-B inputs" in lock["forbidden_data"], "forbidden")

    image_theorem = data["periodic_image_theorem"]
    keys(image_theorem, {"frobenius_identity", "periodic_set", "restriction_identity", "period_support", "fixed_count", "mobius_ledger"}, "image theorem keys")
    ck(image_theorem["frobenius_identity"] == "a^(L+1)=a for L=2^r-1", "Frobenius")
    ck(image_theorem["periodic_set"] == "im(a), of dimension L-1 and cardinality 2^(L-1)", "image")
    ck(image_theorem["restriction_identity"] == "g=a|_im(a) satisfies g^L=I", "restriction")
    ck(image_theorem["period_support"] == "every exact cycle period divides L", "support")
    ck(image_theorem["fixed_count"].startswith("Fix_L(n)=2^deg(gcd"), "fixed formula")
    ck(image_theorem["mobius_ledger"].startswith("P_L(n)=sum_"), "Mobius")

    concentration = data["full_period_concentration_theorem"]
    keys(concentration, {"gcd_dependence", "bezout_proof", "dimension_bound", "proper_divisor_reason", "nonfull_state_bound", "full_period_limit", "burnside_formula", "cycle_count_bound", "mean_period_limit", "mean_definition"}, "concentration keys")
    ck(concentration["gcd_dependence"] == "for 1<=j<L and d=gcd(j,L), ker(g^j-I)=ker(g^d-I)", "gcd dependence")
    ck("Bezout" in concentration["bezout_proof"], "Bezout")
    ck(concentration["dimension_bound"] == "dim ker(g^j-I)<=2d<=2L/3 for every 1<=j<L", "dimension bound")
    ck(concentration["proper_divisor_reason"].endswith("d<=L/3"), "proper divisor")
    ck(concentration["nonfull_state_bound"] == "Pr_im(a)[exact period < L] <= 2L*2^(-L/3)", "state bound")
    ck(concentration["full_period_limit"].endswith("infinity"), "state limit")
    ck(concentration["burnside_formula"].startswith("C_L=(1/L)sum_"), "Burnside")
    ck(concentration["cycle_count_bound"] == "abs(L*C_L/2^(L-1)-1)<=2L*2^(-L/3)", "cycle bound")
    ck(concentration["mean_period_limit"].endswith("tends to 1"), "mean limit")
    ck(concentration["mean_definition"].startswith("mean primitive-cycle length="), "mean definition")

    replay = data["finite_replay"]
    keys(replay, {"r_min", "r_max", "family_rows", "divisor_period_cell_count", "proper_time_cell_count"}, "replay keys")
    ck(replay["r_min"] == 2 and replay["r_max"] == 8 and len(replay["family_rows"]) == 7, "r range")
    divisor_cells = proper_cells = 0
    for r, row in zip(range(2, 9), replay["family_rows"]):
        length = (1 << r) - 1
        periodic_points = 1 << (length - 1)
        matrix = rule90(length)
        ck(matrix_power(matrix, length + 1) == matrix, f"a^(L+1)=a r={r}")
        ck(gf2_rank(matrix) == length - 1, f"image rank r={r}")
        ck(matrix_multiply(matrix_power(matrix, length), matrix) == matrix, f"restriction identity r={r}")

        fixed_lookup = {}
        expected_period_rows = []
        for n in divisors(length):
            dimension = fixed_dimension(matrix, n)
            fixed_lookup[n] = 1 << dimension
        for n in divisors(length):
            exact = sum(mu(n // d) * fixed_lookup[d] for d in divisors(n))
            expected_period_rows.append({"period_n": n, "gcd_degree": fixed_lookup[n].bit_length() - 1, "fixed_points": fixed_lookup[n], "exact_period_points": exact, "primitive_cycles": exact // n})
            ck(exact >= 0 and exact % n == 0, f"period integrality r={r} n={n}")
        ck(row["divisor_period_rows"] == expected_period_rows, f"period rows r={r}")
        ck(sum(cell["exact_period_points"] for cell in expected_period_rows) == periodic_points, f"period partition r={r}")
        divisor_cells += len(expected_period_rows)

        dimension_rows = row["proper_time_dimension_rows"]
        ck(len(dimension_rows) == length - 1, f"proper rows r={r}")
        spectrum = Counter()
        union_bound = 0
        for time, receipt in enumerate(dimension_rows, 1):
            d = gcd(time, length)
            ck(receipt["time_j"] == time and receipt["gcd_j_L"] == d, f"proper index r={r} j={time}")
            ck(receipt["fixed_dimension"] == receipt["divisor_fixed_dimension"], f"gcd dimension r={r} j={time}")
            ck(receipt["two_d_bound"] == 2 * d and receipt["fixed_dimension"] <= 2 * d, f"2d bound r={r} j={time}")
            ck(receipt["divisor_fixed_dimension"] == fixed_lookup[d].bit_length() - 1, f"divisor lookup r={r} j={time}")
            if length <= 63:
                ck(receipt["fixed_dimension"] == fixed_dimension(matrix, time), f"matrix proper dimension r={r} j={time}")
            spectrum[receipt["fixed_dimension"]] += 1
            union_bound += 1 << receipt["fixed_dimension"]
        proper_cells += len(dimension_rows)
        ck(row["fixed_dimension_spectrum"] == [{"dimension": dimension, "proper_times": count} for dimension, count in sorted(spectrum.items())], f"spectrum r={r}")
        largest = divisors(length)[-2]
        max_dimension = max(receipt["fixed_dimension"] for receipt in dimension_rows)
        crude = (length - 1) * (1 << (2 * largest))
        full = expected_period_rows[-1]["exact_period_points"]
        nonfull = periodic_points - full
        cycles = sum(cell["primitive_cycles"] for cell in expected_period_rows)
        burnside = periodic_points + union_bound
        expected_summary = {
            "exponent_r": r, "ring_length_L": length, "periodic_image_points": periodic_points,
            "image_dimension": length - 1, "restriction_order_divides_L": True,
            "divisor_period_rows": expected_period_rows, "proper_time_dimension_rows": dimension_rows,
            "fixed_dimension_spectrum": [{"dimension": dimension, "proper_times": count} for dimension, count in sorted(spectrum.items())],
            "largest_proper_divisor": largest, "maximum_proper_fixed_dimension": max_dimension,
            "uniform_dimension_bound": 2 * largest, "full_period_points": full,
            "nonfull_periodic_points": nonfull, "full_period_state_probability": fraction_record(full, periodic_points),
            "proper_fixed_union_bound_points": union_bound, "crude_union_bound_points": crude,
            "total_periodic_cycles": cycles, "burnside_fixed_sum": burnside,
            "normalized_cycle_excess": fraction_record(length * cycles - periodic_points, periodic_points),
            "mean_cycle_length": fraction_record(periodic_points, cycles),
            "mean_cycle_length_over_L": fraction_record(periodic_points, length * cycles),
        }
        ck(row == expected_summary, f"complete family row r={r}")
        ck(largest * 3 <= length and max_dimension <= 2 * largest, f"uniform dimension r={r}")
        ck(nonfull <= union_bound <= crude, f"union bound r={r}")
        ck(burnside == length * cycles, f"Burnside r={r}")
        ck(Fraction(length * cycles - periodic_points, periodic_points) <= Fraction(2 * (length - 1), 1 << ((length + 2) // 3)), f"integer concentration bound r={r}")
        ck(Fraction(nonfull, periodic_points) <= Fraction(2 * (length - 1), 1 << ((length + 2) // 3)), f"state concentration bound r={r}")
    ck(replay["divisor_period_cell_count"] == divisor_cells, "divisor cells")
    ck(replay["proper_time_cell_count"] == proper_cells, "proper cells")

    control = data["power_of_two_negative_control"]
    keys(control, {"statement", "rows"}, "control keys")
    ck(control["statement"] == "for L=2^s, a^(L/2)=0, so zero is the only periodic state", "control theorem")
    ck(len(control["rows"]) == 7, "control count")
    for s, receipt in zip(range(2, 9), control["rows"]):
        length = 1 << s
        matrix = rule90(length)
        ck(matrix_power(matrix, length // 2) == [0] * length, f"nilpotent s={s}")
        fixed = [1 << fixed_dimension(matrix, n) for n in range(1, 17)]
        ck(receipt == {"exponent_s": s, "ring_length_L": length, "annihilating_iterate": length // 2, "only_periodic_state": "zero", "fixed_counts_period_1_through_16": fixed}, f"control row s={s}")
        ck(fixed == [1] * 16, f"control fixed s={s}")

    progress = data["progress_and_boundary"]
    keys(progress, {"progress", "matched_control", "route_a_obstruction"}, "progress keys")
    ck("all-r concentration theorem" in progress["progress"], "progress")
    ck("power-of-two family remains nilpotent" in progress["matched_control"], "control")
    ck("no frozen target divisor" in progress["route_a_obstruction"], "boundary")
    route = data["route_a"]
    keys(route, {"tuple", "overall", "A1_qualification", "A2_qualification", "A3_qualification", "A4_qualification", "route_b_invocation_allowed"}, "route keys")
    ck(route["tuple"] == ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"], "tuple")
    ck(route["overall"] == "ROUTE_A_EXPLORATORY", "overall")
    ck(route["A1_qualification"] == "ALL_R_FULL_PERIOD_CONCENTRATION_AND_CYCLE_AVERAGE_SCALING_ON_MERSENNE_RULE90_IMAGES", "A1")
    ck(route["A2_qualification"] == "FINITE_VOLUME_NORMALIZED_ORBIT_STATISTICS_WITH_NO_TARGET_DIVISOR_COMPARISON", "A2")
    ck(route["A3_qualification"] == "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_OR_CONTINUATION_COMPARISON", "A3")
    ck(route["A4_qualification"] == "NO_NATURAL_UNITARY_SCATTERING_OR_HAMILTONIAN_LIFT", "A4")
    ck(route["route_b_invocation_allowed"] is False, "Route B")
    flags = data["scope_flags"]
    keys(flags, {"scope", "uses_prime_table", "uses_zero_table", "claims_arithmetic_euler_factors", "claims_root_number", "claims_automorphy", "claims_hilbert_polya", "uses_route_b_inputs"}, "flags")
    ck(flags["scope"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "flag scope")
    for key, value in flags.items():
        if key != "scope":
            ck(value is False, f"false flag {key}")
    ck(data["nonclaims"] == ["that every divisor of L occurs as an exact period", "an infinite-volume determinant or thermodynamic orbit measure", "an arithmetic Euler product or local factorization", "a target divisor, functional equation, or counting-law match", "a natural self-adjoint Hilbert--Polya operator", "Route-B authorization or a solution of the larger program"], "nonclaims")
    print(json.dumps({"status": "C155_CHECK_PASS", "checks": checks, "evidence": str(path)}, sort_keys=True))


if __name__ == "__main__":
    main()
