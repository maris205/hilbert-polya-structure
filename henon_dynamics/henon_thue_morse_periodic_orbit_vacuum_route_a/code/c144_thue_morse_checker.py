#!/usr/bin/env python3
"""Independent standard-library checker for C144; imports no producer code."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c144_thue_morse_evidence.json"


def bit(n: int) -> int:
    parity = 0
    while n:
        parity ^= n & 1
        n >>= 1
    return parity


def prefix(exponent: int) -> str:
    value = "0"
    table = str.maketrans("01", "10")
    for _ in range(exponent):
        value = value + value.translate(table)
    return value


def direct_language(width: int) -> set[str]:
    q = max(0, (width - 1).bit_length())
    sample = prefix(q + 4)
    return {sample[j : j + width] for j in range(len(sample) - width + 1)}


def divisor_period(value: str) -> int:
    n = len(value)
    for d in range(1, n + 1):
        if n % d == 0 and value == value[:d] * (n // d):
            return d
    raise AssertionError("unreachable")


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


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

    keys(data, {"schema", "candidate_id", "date_utc", "scope_literal", "source_lock", "structural_theorems", "aperiodicity_theorem", "language_prefix", "periodic_approximants", "periodic_orbit_vacuum", "progress_and_boundary", "route_a", "scope_flags", "nonclaims", "payload_sha256"}, "top keys")
    ck(data["schema"] == "HCS-C144-v1", "schema")
    ck(data["candidate_id"] == "HCS-C144", "candidate")
    ck(data["date_utc"] == "2026-08-25", "date")
    ck(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    ck(data["payload_sha256"] == payload_hash(data), "payload hash")

    lock = data["source_lock"]
    keys(lock, {"object", "clock", "normalization", "determinant_convention", "precision", "cutoff", "allowed_data", "forbidden_data"}, "lock keys")
    ck("sigma(0)=01" in lock["object"] and "sigma(1)=10" in lock["object"], "substitution")
    ck(lock["clock"] == "one left-shift iterate", "clock")
    ck(lock["normalization"].startswith("Fix(n) counts points"), "normalization")
    ck(lock["determinant_convention"].startswith("Artin--Mazur zeta"), "zeta convention")
    ck("none in theorems" in lock["cutoff"], "cutoff")
    ck("Route-B inputs" in lock["forbidden_data"], "forbidden")

    structure = data["structural_theorems"]
    keys(structure, {"fixed_point_recurrence", "dyadic_block_rule", "no_constant_triples", "uniform_recurrence", "minimality", "nonempty", "minimal"}, "structure keys")
    ck(structure["fixed_point_recurrence"] == "t_(2m)=t_m and t_(2m+1)=1-t_m, equivalently t_n is binary digit-sum parity", "recurrence wording")
    ck(structure["dyadic_block_rule"] == "t_(j*2^q+r)=t_j xor t_r for 0<=r<2^q", "dyadic wording")
    ck(structure["no_constant_triples"].startswith("each pair"), "triple wording")
    ck(structure["uniform_recurrence"].startswith("every factor u"), "uniform wording")
    ck(structure["minimality"].startswith("uniform recurrence implies"), "minimality wording")
    ck(structure["nonempty"] is True and structure["minimal"] is True, "structural flags")
    sample = prefix(15)
    for m in range(1 << 13):
        ck(int(sample[2 * m]) == int(sample[m]), f"even recurrence {m}")
        ck(int(sample[2 * m + 1]) == 1 - int(sample[m]), f"odd recurrence {m}")
    for start in range(len(sample) - 2):
        ck(sample[start : start + 3] not in {"000", "111"}, f"constant triple {start}")
    for q in range(0, 10):
        size = 1 << q
        for j in range(0, 16):
            for r in (0, size // 3, size - 1):
                ck(int(sample[j * size + r]) == (bit(j) ^ bit(r)), f"dyadic block q={q} j={j} r={r}")

    language_data = data["language_prefix"]
    keys(language_data, {"maximum_width", "rows", "language_capture"}, "language keys")
    ck(language_data["maximum_width"] == 16 and len(language_data["rows"]) == 16, "language range")
    rebuilt_languages = {}
    for row in language_data["rows"]:
        width = row["width"]
        blocks = direct_language(width)
        rebuilt_languages[width] = blocks
        ck(row["complexity"] == len(blocks), f"complexity {width}")
        ck(row["language_sha256"] == sha256("\n".join(sorted(blocks)).encode()).hexdigest(), f"language hash {width}")
        q = max(0, (width - 1).bit_length())
        w = prefix(q)
        c = w.translate(str.maketrans("01", "10"))
        pair_blocks = {pair[s : s + width] for pair in (w + w, w + c, c + w, c + c) for s in range(len(w)) if s + width <= 2 * len(w)}
        ck(blocks == pair_blocks, f"four-pair capture {width}")

    theorem = data["aperiodicity_theorem"]
    keys(theorem, {"statement", "multiple_construction", "popcount_identity", "window_argument", "orbit_closure_argument", "period_certificates", "all_positive_periods"}, "aperiodicity keys")
    ck(theorem["statement"] == "X_TM has no shift-periodic point", "statement")
    ck(theorem["all_positive_periods"] is True, "all periods")
    ck(len(theorem["period_certificates"]) == 32, "certificate count")
    for expected_p, receipt in enumerate(theorem["period_certificates"], 1):
        p = receipt["putative_period"]
        k = receipt["odd_exponent_k"]
        d = receipt["multiple_d"]
        b = receipt["aligned_block_exponent_b"]
        ck(p == expected_p, f"period order {p}")
        ck(k > p.bit_length() and k % 2 == 1, f"odd exponent {p}")
        ck(d == p * ((1 << k) - 1) and d % p == 0, f"multiple {p}")
        ck(d.bit_count() == k and bit(d) == 1, f"popcount {p}")
        ck(receipt["binary_digit_parity_of_d"] == 1, f"parity receipt {p}")
        ck(b == d.bit_length() and d < (1 << b), f"aligned exponent {p}")
        ck(receipt["forbidden_window_length"] == 1 << (b + 1), f"window bound {p}")
        w = prefix(b)
        ck(w[0] != w[d], f"aligned mismatch {p}")
        ck(str(1 - int(w[0])) != str(1 - int(w[d])), f"complement mismatch {p}")

    approx = data["periodic_approximants"]
    keys(approx, {"definition", "warning", "seam_bound", "stress_control", "rows", "defect_cells", "invalid_rooted_windows_total", "stress_invalid_rooted_windows_total"}, "approximant keys")
    ck("not a point of X_TM" in approx["warning"], "approximant warning")
    ck(len(approx["rows"]) == 11, "approximant count")
    cells = bad_total = stress_bad_total = 0
    for expected_k, row in enumerate(approx["rows"], 2):
        w = prefix(expected_k)
        n = len(w)
        ck(row["substitution_level"] == expected_k and row["length"] == n, f"level {expected_k}")
        ck(row["least_cyclic_period"] == divisor_period(w) == n, f"least period {expected_k}")
        ck(row["zero_count"] == row["one_count"] == n // 2, f"balance {expected_k}")
        ck(row["word_sha256"] == sha256(w.encode()).hexdigest(), f"word hash {expected_k}")
        for receipt in row["block_defects"]:
            width = receipt["width"]
            intrinsic = rebuilt_languages[width]
            circular = w + w[: width - 1]
            bad = []
            for start in range(n):
                block = circular[start : start + width]
                if block not in intrinsic:
                    bad.append(start)
                if start <= n - width:
                    ck(block in intrinsic, f"interior block k={expected_k} m={width} start={start}")
            ck(receipt["invalid_rooted_windows"] == len(bad), f"bad count k={expected_k} m={width}")
            ck(receipt["invalid_start_indices"] == bad, f"bad starts k={expected_k} m={width}")
            ck(all(start > n - width for start in bad), f"seam location k={expected_k} m={width}")
            ck(len(bad) <= receipt["upper_bound"] == width - 1, f"seam bound k={expected_k} m={width}")
            ck(receipt["defect_fraction_numerator"] == len(bad) and receipt["defect_fraction_denominator"] == n, f"fraction k={expected_k} m={width}")
            cells += 1
            bad_total += len(bad)
        stress = row["macroscopic_stress_defect"]
        if expected_k <= 9:
            ck(stress is not None, f"stress present {expected_k}")
            width = 2 * n + 1
            intrinsic = direct_language(width)
            repeated = w * 4
            bad = [start for start in range(n) if repeated[start : start + width] not in intrinsic]
            ck(stress["width"] == width, f"stress width {expected_k}")
            ck(stress["invalid_rooted_windows"] == len(bad) == n, f"stress count {expected_k}")
            ck(stress["invalid_start_indices"] == bad == list(range(n)), f"stress starts {expected_k}")
            ck(stress["defect_fraction_numerator"] == stress["defect_fraction_denominator"] == n, f"stress fraction {expected_k}")
            ck(stress["status"] == "EXACT_FINITE_CONTROL_NOT_ALL_K_THEOREM", f"stress status {expected_k}")
            stress_bad_total += len(bad)
        else:
            ck(stress is None, f"stress omitted {expected_k}")
    ck(approx["defect_cells"] == cells, "defect cells")
    ck(approx["invalid_rooted_windows_total"] == bad_total, "bad total")
    ck(approx["stress_invalid_rooted_windows_total"] == stress_bad_total, "stress bad total")

    vacuum = data["periodic_orbit_vacuum"]
    keys(vacuum, {"periodic_point_counts", "all_positive_period_counts", "artin_mazur_zeta", "zeta_coefficients_through_degree_32", "primitive_cycle_counts"}, "vacuum keys")
    ck(vacuum["periodic_point_counts"] == [{"period": n, "fixed_points": 0} for n in range(1, 33)], "fixed counts")
    ck(vacuum["artin_mazur_zeta"] == "zeta_TM(z)=1", "zeta")
    ck(vacuum["zeta_coefficients_through_degree_32"] == [1] + [0] * 32, "zeta coefficients")
    ck(vacuum["primitive_cycle_counts"] == "zero at every positive period", "primitive vacuum")

    boundary = data["progress_and_boundary"]
    keys(boundary, {"progress", "approximant_lesson", "route_a_obstruction"}, "boundary keys")
    ck("minimal uniformly recurrent" in boundary["progress"], "progress")
    ck("do not turn them" in boundary["approximant_lesson"], "approximant lesson")
    ck("do not imply" in boundary["route_a_obstruction"], "obstruction")

    route = data["route_a"]
    keys(route, {"tuple", "overall", "A1_qualification", "A2_qualification", "A3_qualification", "A4_qualification", "route_b_invocation_allowed"}, "route keys")
    ck(route["tuple"] == ["A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"], "tuple")
    ck(route["overall"] == "ROUTE_A_REJECTED", "overall")
    ck(route["route_b_invocation_allowed"] is False, "route B")
    ck(route["A1_qualification"].startswith("PROVED_PERIODIC_ORBIT_VACUUM"), "A1")
    ck(route["A2_qualification"].startswith("SOURCE_ARTIN_MAZUR_ZETA_IS_IDENTICALLY_ONE"), "A2")

    flags = data["scope_flags"]
    keys(flags, {"scope", "uses_prime_table", "uses_zero_table", "claims_arithmetic_euler_factors", "claims_root_number", "claims_automorphy", "claims_hilbert_polya", "uses_route_b_inputs"}, "scope flags")
    ck(flags["scope"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "flag scope")
    for name, value in flags.items():
        if name != "scope":
            ck(value is False, f"false flag {name}")
    ck(data["nonclaims"] == [
        "that periodic approximants belong to X_TM",
        "that absence of periodic points implies absence of invariant measures or recurrence",
        "an arithmetic Euler product or local factorization",
        "a target divisor, functional equation, or counting-law match",
        "a natural self-adjoint Hilbert--Polya operator",
        "Route-B authorization or a solution of the larger program",
    ], "nonclaims")

    print(json.dumps({"status": "C144_CHECK_PASS", "checks": checks, "evidence": str(path)}, sort_keys=True))


if __name__ == "__main__":
    main()
