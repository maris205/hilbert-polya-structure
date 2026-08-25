#!/usr/bin/env python3
"""Producer-independent finite-map checker for HCS-C149."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c149_skeleton_evidence.json"
LENGTHS = (1, 2, 3, 5)


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def number_theoretic_mu(value: int) -> int:
    trial = 2
    signs = 0
    n = value
    while trial * trial <= n:
        exponent = 0
        while n % trial == 0:
            n //= trial
            exponent += 1
        if exponent > 1:
            return 0
        if exponent == 1:
            signs += 1
        trial += 1
    if n > 1:
        signs += 1
    return -1 if signs % 2 else 1


def iterate(table: dict[str, str], point: str, steps: int) -> str:
    for _ in range(steps):
        point = table[point]
    return point


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_EVIDENCE
    data = json.loads(path.read_text())
    checks = 0

    def ck(condition: bool, label: str) -> None:
        nonlocal checks
        if not condition:
            raise AssertionError(label)
        checks += 1

    def exact_keys(value: dict, expected: set[str], label: str) -> None:
        ck(set(value) == expected, label)

    exact_keys(data, {"schema", "candidate_id", "date_utc", "source_commit", "scope_literal", "source_lock", "thue_morse_component", "finite_skeleton", "all_period_theorem", "finite_replay", "progress_and_boundary", "route_a", "scope_flags", "nonclaims", "payload_sha256"}, "top-level keys")
    ck(data["schema"] == "HCS-C149-v1", "schema")
    ck(data["candidate_id"] == "HCS-C149", "candidate")
    ck(data["date_utc"] == "2026-08-25", "date")
    ck(data["source_commit"] == "2d4e6211a254ef49d87718569d23466f4c6dcf4c", "source commit")
    ck(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    ck(data["payload_sha256"] == payload_hash(data), "payload hash")

    lock = data["source_lock"]
    exact_keys(lock, {"object", "map", "clock", "normalization", "zeta_convention", "cutoff", "allowed_data", "forbidden_data"}, "lock keys")
    ck(lock["object"] == "compact topological disjoint union Y=X_TM sqcup C_1 sqcup C_2 sqcup C_3 sqcup C_5 with tagged finite cycles", "object")
    ck(lock["map"].startswith("the shift on X_TM"), "map")
    ck(lock["clock"] == "one iterate of the componentwise map", "clock")
    ck("primitive cycles" in lock["normalization"], "normalization")
    ck(lock["zeta_convention"].startswith("zeta_Y(z)=exp"), "zeta convention")
    ck(lock["cutoff"].endswith("zeta degree<=30"), "cutoff")
    ck("1,2,3,5" in lock["allowed_data"], "allowed data")
    ck("Route-B inputs" in lock["forbidden_data"], "forbidden data")

    tm = data["thue_morse_component"]
    exact_keys(tm, {"substitution", "status", "periodic_points", "all_positive_fixed_counts_zero", "proof_certificate", "period_certificate_limit", "period_certificates"}, "TM keys")
    ck(tm["substitution"] == {"0": "01", "1": "10"}, "substitution")
    ck(tm["status"] == "NONEMPTY_MINIMAL_UNIFORMLY_RECURRENT_APERIODIC_COMPONENT", "TM status")
    ck(tm["periodic_points"] == 0 and tm["all_positive_fixed_counts_zero"] is True, "TM vacuum")
    ck(tm["proof_certificate"] == "for each p choose odd k>bit_length(p), d=p(2^k-1), and b=bit_length(d); popcount(d)=k, and every length-2^(b+1) interval contains a full b-aligned block whose offsets 0,d are p-congruent and have opposite Thue--Morse bits", "proof certificate")
    ck(tm["period_certificate_limit"] == len(tm["period_certificates"]) == 32, "certificate limit")
    for p, receipt in enumerate(tm["period_certificates"], 1):
        exact_keys(receipt, {"putative_period", "odd_exponent_k", "multiple_d", "popcount_d", "tm_bit_at_zero", "tm_bit_at_d", "forbidden_window_length"}, f"certificate keys p={p}")
        k = p.bit_length() + 1
        if k % 2 == 0:
            k += 1
        d = p * ((1 << k) - 1)
        ck(receipt == {"putative_period": p, "odd_exponent_k": k, "multiple_d": d, "popcount_d": d.bit_count(), "tm_bit_at_zero": 0, "tm_bit_at_d": d.bit_count() & 1, "forbidden_window_length": 1 << (d.bit_length() + 1)}, f"certificate p={p}")
        ck(d % p == 0 and d.bit_count() == k and k & 1, f"certificate arithmetic p={p}")

    skeleton = data["finite_skeleton"]
    exact_keys(skeleton, {"cycle_lengths", "total_points", "cycle_rows", "successor_table", "topology"}, "skeleton keys")
    ck(skeleton["cycle_lengths"] == list(LENGTHS), "lengths")
    ck(skeleton["total_points"] == 11, "point count")
    ck(skeleton["topology"] == "finite tagged discrete union, disjoint from X_TM", "topology")
    table = skeleton["successor_table"]
    ck(len(table) == 11 and set(table) == set(table.values()), "successor permutation")
    all_points = []
    for row, length in zip(skeleton["cycle_rows"], LENGTHS):
        labels = [f"tag_{length}:{j}" for j in range(length)]
        ck(row == {"length": length, "tag": f"tag_{length}", "point_labels": labels, "least_periods": [length] * length, "primitive_cycles": 1}, f"cycle row {length}")
        for j, point in enumerate(labels):
            ck(table[point] == labels[(j + 1) % length], f"successor {point}")
            ck(iterate(table, point, length) == point, f"period divides {length} for {point}")
            for smaller in range(1, length):
                ck(iterate(table, point, smaller) != point, f"least period {point}/{smaller}")
        all_points.extend(labels)
    ck(set(all_points) == set(table), "point closure")

    replay = data["finite_replay"]
    exact_keys(replay, {"period_limit", "rows", "fixed_count_sum", "exact_period_point_sum", "primitive_cycle_sum", "zeta_degree_limit", "zeta_coefficients"}, "replay keys")
    ck(replay["period_limit"] == len(replay["rows"]) == 60, "period limit")
    rebuilt = []
    fixed_counts = {}
    for n in range(1, 61):
        labels = [point for point in all_points if iterate(table, point, n) == point]
        fixed_counts[n] = len(labels)
        exact = sum(number_theoretic_mu(n // d) * fixed_counts[d] for d in range(1, n + 1) if n % d == 0)
        expected = {"period_n": n, "fixed_points": len(labels), "fixed_point_labels": labels, "exact_period_points": exact, "primitive_cycles": exact // n}
        ck(replay["rows"][n - 1] == expected, f"ledger n={n}")
        ck(len(labels) == sum(length for length in LENGTHS if n % length == 0), f"fixed formula n={n}")
        ck(exact >= 0 and exact % n == 0, f"exact integrality n={n}")
        rebuilt.append(expected)
    ck(replay["fixed_count_sum"] == sum(row["fixed_points"] for row in rebuilt), "fixed sum")
    ck(replay["exact_period_point_sum"] == sum(row["exact_period_points"] for row in rebuilt), "exact sum")
    ck(replay["primitive_cycle_sum"] == sum(row["primitive_cycles"] for row in rebuilt), "cycle sum")

    ck(replay["zeta_degree_limit"] == 30 and len(replay["zeta_coefficients"]) == 31, "zeta limit")
    brute_coefficients = []
    for degree in range(31):
        representations = 0
        for a in range(degree + 1):
            for b in range(degree // 2 + 1):
                for c in range(degree // 3 + 1):
                    remaining = degree - a - 2 * b - 3 * c
                    representations += remaining >= 0 and remaining % 5 == 0
        brute_coefficients.append(representations)
    ck(replay["zeta_coefficients"] == brute_coefficients, "zeta coefficients")

    theorem = data["all_period_theorem"]
    exact_keys(theorem, {"fixed_count_formula", "primitive_skeleton", "no_other_primitive_cycles", "artin_mazur_zeta", "formal_derivation", "minimality_obstruction", "general_finite_attachment_statement"}, "theorem keys")
    ck(theorem["fixed_count_formula"] == "Fix_Y(n)=sum_(ell in {1,2,3,5}, ell|n) ell for every n>=1", "fixed theorem")
    ck(theorem["primitive_skeleton"] == [{"least_period": length, "primitive_cycles": 1} for length in LENGTHS], "primitive theorem")
    ck(theorem["no_other_primitive_cycles"] is True, "no other cycles")
    ck(theorem["artin_mazur_zeta"] == "1/((1-z)(1-z^2)(1-z^3)(1-z^5))", "zeta theorem")
    ck(theorem["formal_derivation"].endswith("-sum_ell log(1-z^ell)"), "formal derivation")
    ck("proper closed invariant subset" in theorem["minimality_obstruction"], "minimality obstruction")
    ck(theorem["general_finite_attachment_statement"].endswith("destroys minimality"), "general attachment theorem")

    progress = data["progress_and_boundary"]
    exact_keys(progress, {"progress", "structural_cost", "route_a_obstruction"}, "progress keys")
    ck("controlled nonempty finite primitive skeleton" in progress["progress"], "progress")
    ck("destroys minimality" in progress["structural_cost"], "cost")
    ck("no target divisor" in progress["route_a_obstruction"], "boundary")

    route = data["route_a"]
    exact_keys(route, {"tuple", "overall", "A1_qualification", "A2_qualification", "A3_qualification", "A4_qualification", "route_b_invocation_allowed"}, "route keys")
    ck(route["tuple"] == ["A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"], "tuple")
    ck(route["overall"] == "ROUTE_A_REJECTED", "overall")
    ck(route["A1_qualification"] == "DECLARED_FINITE_DISJOINT_ATTACHMENT_NOT_INTRINSIC_TO_THE_MINIMAL_THUE_MORSE_COMPONENT", "A1")
    ck(route["A2_qualification"] == "ELEMENTARY_FINITE_RATIONAL_SOURCE_ZETA_WITH_NO_TARGET_DIVISOR_COMPARISON", "A2")
    ck(route["A3_qualification"] == "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_OR_CONTINUATION_COMPARISON", "A3")
    ck(route["A4_qualification"] == "NO_NATURAL_UNITARY_SCATTERING_OR_HAMILTONIAN_LIFT", "A4")
    ck(route["route_b_invocation_allowed"] is False, "Route B")

    flags = data["scope_flags"]
    exact_keys(flags, {"scope", "uses_prime_table", "uses_zero_table", "claims_arithmetic_euler_factors", "claims_root_number", "claims_automorphy", "claims_hilbert_polya", "uses_route_b_inputs"}, "flag keys")
    ck(flags["scope"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "flag scope")
    for key, value in flags.items():
        if key != "scope":
            ck(value is False, f"false flag {key}")
    ck(data["nonclaims"] == [
        "that the attached periodic cycles belong to the Thue--Morse subshift",
        "that the disjoint union remains minimal or almost minimal",
        "an arithmetic Euler product or local factorization",
        "a target divisor, functional equation, or counting-law match",
        "a natural self-adjoint Hilbert--Polya operator",
        "Route-B authorization or a solution of the larger program",
    ], "nonclaims")

    print(json.dumps({"status": "C149_CHECK_PASS", "checks": checks, "evidence": str(path)}, sort_keys=True))


if __name__ == "__main__":
    main()
