#!/usr/bin/env python3
"""Produce the exact HCS-C144 Thue--Morse periodic-orbit-vacuum certificate."""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c144_thue_morse_evidence.json"
MAX_BLOCK = 16
MAX_APPROXIMANT = 12
MAX_TEST_PERIOD = 32


def tm_bit(n: int) -> int:
    return n.bit_count() & 1


def word(k: int) -> str:
    return "".join(str(tm_bit(n)) for n in range(1 << k))


def complement(value: str) -> str:
    return value.translate(str.maketrans("01", "10"))


def language(width: int) -> set[str]:
    q = max(0, (width - 1).bit_length())
    w = word(q)
    c = complement(w)
    return {
        pair[start : start + width]
        for pair in (w + w, w + c, c + w, c + c)
        for start in range(len(w))
        if start + width <= 2 * len(w)
    }


def cyclic_blocks(value: str, width: int) -> list[str]:
    repeated = value * (width // len(value) + 3)
    return [repeated[start : start + width] for start in range(len(value))]


def least_period(value: str) -> int:
    n = len(value)
    for d in range(1, n + 1):
        if n % d == 0 and all(value[j] == value[(j + d) % n] for j in range(n)):
            return d
    raise AssertionError("unreachable")


def payload_bytes(data: dict) -> bytes:
    body = dict(data)
    body.pop("payload_sha256", None)
    return json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def build() -> dict:
    complexities = []
    for width in range(1, MAX_BLOCK + 1):
        blocks = sorted(language(width))
        complexities.append({
            "width": width,
            "complexity": len(blocks),
            "language_sha256": sha256("\n".join(blocks).encode()).hexdigest(),
        })

    approximants = []
    defect_cells = 0
    invalid_windows = 0
    stress_invalid_windows = 0
    for k in range(2, MAX_APPROXIMANT + 1):
        w = word(k)
        assert w[: len(w) // 2] == word(k - 1)
        assert w[len(w) // 2 :] == complement(word(k - 1))
        assert least_period(w) == len(w)
        rows = []
        for width in range(2, min(MAX_BLOCK, len(w)) + 1):
            intrinsic = language(width)
            cyclic = cyclic_blocks(w, width)
            bad = [start for start, block in enumerate(cyclic) if block not in intrinsic]
            assert all(start > len(w) - width for start in bad)
            assert len(bad) <= width - 1
            rows.append({
                "width": width,
                "invalid_rooted_windows": len(bad),
                "invalid_start_indices": bad,
                "upper_bound": width - 1,
                "defect_fraction_numerator": len(bad),
                "defect_fraction_denominator": len(w),
            })
            defect_cells += 1
            invalid_windows += len(bad)
        stress = None
        if k <= 9:
            stress_width = 2 * len(w) + 1
            intrinsic = language(stress_width)
            cyclic = cyclic_blocks(w, stress_width)
            stress_bad = [start for start, block in enumerate(cyclic) if block not in intrinsic]
            assert len(stress_bad) == len(w)
            stress = {
                "width": stress_width,
                "invalid_rooted_windows": len(stress_bad),
                "invalid_start_indices": stress_bad,
                "defect_fraction_numerator": len(stress_bad),
                "defect_fraction_denominator": len(w),
                "status": "EXACT_FINITE_CONTROL_NOT_ALL_K_THEOREM",
            }
            stress_invalid_windows += len(stress_bad)
        approximants.append({
            "substitution_level": k,
            "length": len(w),
            "least_cyclic_period": least_period(w),
            "zero_count": w.count("0"),
            "one_count": w.count("1"),
            "word_sha256": sha256(w.encode()).hexdigest(),
            "block_defects": rows,
            "macroscopic_stress_defect": stress,
        })

    certificates = []
    for period in range(1, MAX_TEST_PERIOD + 1):
        odd_k = period.bit_length() + 1
        if odd_k % 2 == 0:
            odd_k += 1
        d = period * ((1 << odd_k) - 1)
        b = d.bit_length()
        assert d % period == 0
        assert tm_bit(d) == 1
        assert d < (1 << b)
        certificates.append({
            "putative_period": period,
            "odd_exponent_k": odd_k,
            "multiple_d": d,
            "binary_digit_parity_of_d": tm_bit(d),
            "aligned_block_exponent_b": b,
            "forbidden_window_length": 1 << (b + 1),
        })

    periodic_counts = [{"period": n, "fixed_points": 0} for n in range(1, MAX_TEST_PERIOD + 1)]
    data = {
        "schema": "HCS-C144-v1",
        "candidate_id": "HCS-C144",
        "date_utc": "2026-08-25",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "source_lock": {
            "object": "the two-sided Thue--Morse substitution subshift X_TM generated by sigma(0)=01 and sigma(1)=10",
            "clock": "one left-shift iterate",
            "normalization": "Fix(n) counts points fixed by the nth power of the left shift; primitive cycles are geometric shift orbits",
            "determinant_convention": "Artin--Mazur zeta zeta_TM(z)=exp(sum_(n>=1) Fix(n) z^n/n)",
            "precision": "exact binary words and exact integer counts",
            "cutoff": "none in theorems; block widths <=16, approximants k<=12, and periods <=32 are replay sentinels",
            "allowed_data": "the frozen substitution and computations derived from it",
            "forbidden_data": "external prime or zero tables, arithmetic/local factors, root numbers, automorphy claims, and Route-B inputs",
        },
        "structural_theorems": {
            "fixed_point_recurrence": "t_(2m)=t_m and t_(2m+1)=1-t_m, equivalently t_n is binary digit-sum parity",
            "dyadic_block_rule": "t_(j*2^q+r)=t_j xor t_r for 0<=r<2^q",
            "no_constant_triples": "each pair t_(2m),t_(2m+1) is complementary, hence neither 000 nor 111 occurs",
            "uniform_recurrence": "every factor u contained in w_q occurs in every t-window of length at least 4*2^q; aligned q-blocks are w_q or complement(w_q), and among any three types at least one is w_q",
            "minimality": "uniform recurrence implies every point of X_TM has the complete Thue--Morse language, so every shift orbit meets every nonempty cylinder",
            "nonempty": True,
            "minimal": True,
        },
        "aperiodicity_theorem": {
            "statement": "X_TM has no shift-periodic point",
            "multiple_construction": "for odd k>bit_length(p), d=p(2^k-1) has odd binary digit sum and is a multiple of p",
            "popcount_identity": "popcount(p(2^k-1))=k because p(2^k-1)=(p-1)2^k+(2^k-p) and the low k bits are the complement of p-1",
            "window_argument": "every interval of length 2^(b+1) contains a complete b-aligned block; its offsets 0 and d differ but are congruent modulo p",
            "orbit_closure_argument": "a p-periodic point in X_TM would contribute such a forbidden p-periodic window to the Thue--Morse language",
            "period_certificates": certificates,
            "all_positive_periods": True,
        },
        "language_prefix": {
            "maximum_width": MAX_BLOCK,
            "rows": complexities,
            "language_capture": "for 2^q>=m, every length-m factor lies in one of the four concatenations w_qw_q, w_q complement(w_q), complement(w_q)w_q, complement(w_q)complement(w_q)",
        },
        "periodic_approximants": {
            "definition": "c_k is the bi-infinite repetition of w_k=t_[0,2^k)",
            "warning": "c_k is a finite periodic control and is not a point of X_TM",
            "seam_bound": "for a width-m window with m<=2^k, only the m-1 seam-crossing starts can be extrinsic, so the invalid rooted fraction is at most (m-1)/2^k",
            "stress_control": "for 2<=k<=9 every rooted window of width 2^(k+1)+1 in c_k is absent from the intrinsic language; this is an exact finite ledger, not an all-k theorem",
            "rows": approximants,
            "defect_cells": defect_cells,
            "invalid_rooted_windows_total": invalid_windows,
            "stress_invalid_rooted_windows_total": stress_invalid_windows,
        },
        "periodic_orbit_vacuum": {
            "periodic_point_counts": periodic_counts,
            "all_positive_period_counts": "Fix(sigma^n|X_TM)=0 for every n>=1",
            "artin_mazur_zeta": "zeta_TM(z)=1",
            "zeta_coefficients_through_degree_32": [1] + [0] * MAX_TEST_PERIOD,
            "primitive_cycle_counts": "zero at every positive period",
        },
        "progress_and_boundary": {
            "progress": "isolates a minimal uniformly recurrent nonperiodic system whose rich finite language supplies no primitive periodic-orbit source at all",
            "approximant_lesson": "periodic substitution approximants have exact finite cycles, but their seam defects do not turn them into periodic points of X_TM",
            "route_a_obstruction": "recurrence and finite-language richness alone do not imply an intrinsic primitive-orbit layer",
        },
        "route_a": {
            "tuple": ["A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "overall": "ROUTE_A_REJECTED",
            "A1_qualification": "PROVED_PERIODIC_ORBIT_VACUUM_DESPITE_MINIMAL_UNIFORM_RECURRENCE",
            "A2_qualification": "SOURCE_ARTIN_MAZUR_ZETA_IS_IDENTICALLY_ONE_WITH_NO_FROZEN_TARGET_COMPARISON",
            "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_OR_CONTINUATION_COMPARISON",
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
            "that periodic approximants belong to X_TM",
            "that absence of periodic points implies absence of invariant measures or recurrence",
            "an arithmetic Euler product or local factorization",
            "a target divisor, functional equation, or counting-law match",
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
    print(json.dumps({
        "status": "C144_PRODUCER_PASS",
        "output": str(args.output),
        "payload_sha256": data["payload_sha256"],
        "defect_cells": data["periodic_approximants"]["defect_cells"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
