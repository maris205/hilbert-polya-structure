#!/usr/bin/env python3
"""Independent binary-matrix checker for HCS-C150."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c150_rule90_mersenne_evidence.json"


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
    rows = []
    for i in range(length):
        row = 0
        row ^= 1 << ((i - 1) % length)
        row ^= 1 << ((i + 1) % length)
        rows.append(row)
    return rows


def gf2_rank(rows: list[int], columns: int | None = None) -> int:
    work = rows[:]
    if columns is None:
        columns = len(rows)
    pivot = 0
    for column in range(columns):
        selected = next((j for j in range(pivot, len(work)) if (work[j] >> column) & 1), None)
        if selected is None:
            continue
        work[pivot], work[selected] = work[selected], work[pivot]
        for j in range(len(work)):
            if j != pivot and ((work[j] >> column) & 1):
                work[j] ^= work[pivot]
        pivot += 1
    return pivot


def kernel_dimension_of_power_minus_identity(matrix: list[int], time: int) -> int:
    powered = matrix_power(matrix, time)
    difference = [row ^ (1 << i) for i, row in enumerate(powered)]
    return len(matrix) - gf2_rank(difference)


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mu(n: int) -> int:
    factors = 0
    p = 2
    while p * p <= n:
        exponent = 0
        while n % p == 0:
            n //= p
            exponent += 1
        if exponent > 1:
            return 0
        factors += exponent
        p += 1
    if n > 1:
        factors += 1
    return -1 if factors & 1 else 1


def apply(matrix: list[int], state: int) -> int:
    out = 0
    for i, row in enumerate(matrix):
        if (row & state).bit_count() & 1:
            out |= 1 << i
    return out


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

    keys(data, {"schema", "candidate_id", "date_utc", "source_commit", "scope_literal", "source_lock", "mersenne_theorem", "fixed_and_primitive_formula", "mersenne_replay", "power_of_two_negative_control", "progress_and_boundary", "route_a", "scope_flags", "nonclaims", "payload_sha256"}, "top keys")
    ck(data["schema"] == "HCS-C150-v1", "schema")
    ck(data["candidate_id"] == "HCS-C150", "candidate")
    ck(data["date_utc"] == "2026-08-25", "date")
    ck(data["source_commit"] == "2d4e6211a254ef49d87718569d23466f4c6dcf4c", "commit")
    ck(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    ck(data["payload_sha256"] == payload_hash(data), "payload hash")

    lock = data["source_lock"]
    keys(lock, {"object", "family", "clock", "normalization", "cutoff", "precision", "allowed_data", "forbidden_data"}, "lock keys")
    ck(lock["object"].startswith("Rule 90, multiplication by a=x+x^{-1}"), "object")
    ck(lock["family"] == "Mersenne circumferences L_r=2^r-1 for every r>=1", "family")
    ck(lock["clock"].startswith("one Rule-90 update"), "clock")
    ck("Mobius" in lock["normalization"], "normalization")
    ck(lock["cutoff"].endswith("1<=s<=8"), "cutoff")
    ck(lock["precision"] == "exact F_2 polynomial arithmetic and exact integers", "precision")
    ck("Rule-90 local rule" in lock["allowed_data"], "allowed")
    ck("Route-B inputs" in lock["forbidden_data"], "forbidden")

    theorem = data["mersenne_theorem"]
    keys(theorem, {"frobenius_identity", "equivalent_identity", "kernel_statement", "kernel_proof", "image_periodicity", "eventual_image", "periodic_set_equals_image", "periodic_fraction", "all_cycle_periods_divide_L"}, "theorem keys")
    ck(theorem["frobenius_identity"] == "a^(2^r)=x^(2^r)+x^(-2^r)=x+x^(-1)=a in R_(2^r-1)", "Frobenius")
    ck(theorem["equivalent_identity"] == "a^(L_r+1)=a", "equivalent identity")
    ck(theorem["kernel_statement"] == "ker(a) has dimension one and im(a) has dimension L_r-1", "kernel")
    ck("simple factor" in theorem["kernel_proof"], "kernel proof")
    ck(theorem["image_periodicity"].startswith("for y=a u"), "image periodicity")
    ck(theorem["eventual_image"].startswith("every state enters"), "entry")
    ck(theorem["periodic_set_equals_image"] is True, "periodic=image")
    ck(theorem["periodic_fraction"] == "exactly 1/2 for every r>=1", "fraction")
    ck(theorem["all_cycle_periods_divide_L"] is True, "period support")

    formula = data["fixed_and_primitive_formula"]
    keys(formula, {"fixed_count", "exact_period", "primitive_cycles", "support"}, "formula keys")
    ck(formula["fixed_count"] == "Fix_L(n)=2^deg(gcd(x^L+1,(x^2+1)^n+x^n))", "fixed formula")
    ck(formula["exact_period"].startswith("P_L(n)=sum_"), "exact formula")
    ck(formula["primitive_cycles"] == "C_L(n)=P_L(n)/n", "cycle formula")
    ck(formula["support"].endswith("for L=2^r-1"), "support")

    replay = data["mersenne_replay"]
    keys(replay, {"r_limit", "family_rows", "divisor_period_cell_count", "periodic_point_sum", "primitive_cycle_sum"}, "replay keys")
    ck(replay["r_limit"] == len(replay["family_rows"]) == 8, "r limit")
    rebuilt_cell_count = 0
    periodic_sum = primitive_sum = 0
    for r, receipt in enumerate(replay["family_rows"], 1):
        length = (1 << r) - 1
        matrix = rule90(length)
        image_rank = gf2_rank(matrix)
        ck(matrix_power(matrix, length + 1) == matrix, f"a^(L+1)=a r={r}")
        ck(image_rank == length - 1, f"image rank r={r}")
        expected_rows = []
        fixed_lookup = {}
        for n in divisors(length):
            dimension = kernel_dimension_of_power_minus_identity(matrix, n)
            fixed_lookup[n] = 1 << dimension
        for n in divisors(length):
            fixed = fixed_lookup[n]
            exact = sum(mu(n // d) * fixed_lookup[d] for d in divisors(n))
            expected_rows.append({"period_n": n, "gcd_degree": fixed.bit_length() - 1, "fixed_points": fixed, "exact_period_points": exact, "primitive_cycles": exact // n})
            ck(exact >= 0 and exact % n == 0, f"integrality r={r} n={n}")
        expected = {
            "exponent_r": r, "ring_length_L": length, "state_space_size": 1 << length,
            "kernel_dimension": 1, "image_dimension": length - 1,
            "periodic_points": 1 << (length - 1), "periodic_fraction_numerator": 1,
            "periodic_fraction_denominator": 2, "transient_points": 1 << (length - 1),
            "entry_time_bound": 1, "restriction_order_divides": length,
            "divisor_period_rows": expected_rows,
        }
        ck(receipt == expected, f"family row r={r}")
        ck(sum(row["exact_period_points"] for row in expected_rows) == 1 << (length - 1), f"periodic partition r={r}")
        if length <= 15:
            image = {apply(matrix, state) for state in range(1 << length)}
            periodic = set()
            for state in range(1 << length):
                current = apply(matrix, state)
                for _ in range(length - 1):
                    current = apply(matrix, current)
                if current == state:
                    periodic.add(state)
            ck(len(image) == 1 << (length - 1), f"brute image r={r}")
            ck(periodic == image, f"brute periodic=image r={r}")
        rebuilt_cell_count += len(expected_rows)
        periodic_sum += expected["periodic_points"]
        primitive_sum += sum(row["primitive_cycles"] for row in expected_rows)
    ck(replay["divisor_period_cell_count"] == rebuilt_cell_count, "cell count")
    ck(replay["periodic_point_sum"] == periodic_sum, "periodic sum")
    ck(replay["primitive_cycle_sum"] == primitive_sum, "primitive sum")

    control = data["power_of_two_negative_control"]
    keys(control, {"statement", "proof", "rows"}, "control keys")
    ck(control["statement"] == "for L=2^s, a^(2^(s-1))=0, so Rule 90 is nilpotent and zero is its only periodic state", "control theorem")
    ck(control["proof"].startswith("Frobenius gives"), "control proof")
    ck(len(control["rows"]) == 8, "control rows")
    for s, receipt in enumerate(control["rows"], 1):
        length = 1 << s
        matrix = rule90(length)
        exponent = length // 2
        ck(matrix_power(matrix, exponent) == [0] * length, f"nilpotent s={s}")
        fixed = [1 << kernel_dimension_of_power_minus_identity(matrix, n) for n in range(1, 17)]
        expected = {"exponent_s": s, "ring_length_L": length, "annihilating_iterate": exponent, "identity": f"a^(2^{s-1})=x^(2^{s-1})+x^(-2^{s-1})=0 modulo x^{length}-1", "only_periodic_state": "zero", "fixed_counts_period_1_through_16": fixed}
        ck(receipt == expected, f"control row s={s}")
        ck(fixed == [1] * 16, f"only zero fixed s={s}")

    progress = data["progress_and_boundary"]
    keys(progress, {"progress", "matched_control", "route_a_obstruction"}, "progress keys")
    ck("all-r Mersenne scaling theorem" in progress["progress"], "progress")
    ck("power-of-two scaling family is nilpotent" in progress["matched_control"], "control boundary")
    ck("no frozen target divisor" in progress["route_a_obstruction"], "route boundary")

    route = data["route_a"]
    keys(route, {"tuple", "overall", "A1_qualification", "A2_qualification", "A3_qualification", "A4_qualification", "route_b_invocation_allowed"}, "route keys")
    ck(route["tuple"] == ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"], "tuple")
    ck(route["overall"] == "ROUTE_A_EXPLORATORY", "overall")
    ck(route["A1_qualification"] == "ALL_R_EXACT_MERSENNE_PERIODIC_IMAGE_WITH_DIVISOR_RESOLVED_PRIMITIVE_CYCLES", "A1")
    ck(route["A2_qualification"] == "SCALING_FAMILY_OF_FINITE_POLYNOMIAL_COUNTS_WITH_NO_TARGET_DIVISOR_COMPARISON", "A2")
    ck(route["A3_qualification"] == "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_OR_CONTINUATION_COMPARISON", "A3")
    ck(route["A4_qualification"] == "NO_NATURAL_UNITARY_SCATTERING_OR_HAMILTONIAN_LIFT", "A4")
    ck(route["route_b_invocation_allowed"] is False, "Route B")

    flags = data["scope_flags"]
    keys(flags, {"scope", "uses_prime_table", "uses_zero_table", "claims_arithmetic_euler_factors", "claims_root_number", "claims_automorphy", "claims_hilbert_polya", "uses_route_b_inputs"}, "flags")
    ck(flags["scope"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "flag scope")
    for key, value in flags.items():
        if key != "scope":
            ck(value is False, f"false flag {key}")
    ck(data["nonclaims"] == [
        "that every divisor of L occurs as a cycle period",
        "an infinite-volume determinant or thermodynamic limit",
        "an arithmetic Euler product or local factorization",
        "a target divisor, functional equation, or counting-law match",
        "a natural self-adjoint Hilbert--Polya operator",
        "Route-B authorization or a solution of the larger program",
    ], "nonclaims")

    print(json.dumps({"status": "C150_CHECK_PASS", "checks": checks, "evidence": str(path)}, sort_keys=True))


if __name__ == "__main__":
    main()
