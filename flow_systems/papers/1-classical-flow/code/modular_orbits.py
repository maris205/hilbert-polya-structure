#!/usr/bin/env python3
"""Deterministic PSL(2,Z) closed-geodesic ledger and arithmetic audit.

The program deliberately has two phases. ``enumerate`` uses no primality test
and freezes a checksum-protected orbit ledger. Only ``audit`` reads the frozen
ledger and introduces rational-prime controls. No Riemann-zero data are used.

We use PSL(2,Z) = <S,R | S^2=R^3=1>. A cyclically reduced hyperbolic class has
a representative S R^e1 ... S R^em, with ej in {1,2}. Cyclic rotations
implement conjugacy. Reversal followed by e -> 3-e implements orientation
reversal. The main ledger quotients cyclic rotations but retains inversion, so
it records the oriented conjugacy classes used by the flow/trace convention.
The cutoff is the number of S-R blocks, not a geometric-length cutoff.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import platform
import sys
from collections import Counter
from dataclasses import asdict, dataclass
from itertools import product
from pathlib import Path
from typing import Iterable, Iterator, Sequence


Matrix = tuple[tuple[int, int], tuple[int, int]]
IDENTITY: Matrix = ((1, 0), (0, 1))
S: Matrix = ((0, -1), (1, 0))
R: Matrix = ((0, -1), (1, 1))


def matmul(a: Matrix, b: Matrix) -> Matrix:
    return (
        (
            a[0][0] * b[0][0] + a[0][1] * b[1][0],
            a[0][0] * b[0][1] + a[0][1] * b[1][1],
        ),
        (
            a[1][0] * b[0][0] + a[1][1] * b[1][0],
            a[1][0] * b[0][1] + a[1][1] * b[1][1],
        ),
    )


def determinant(a: Matrix) -> int:
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def trace_abs(a: Matrix) -> int:
    return abs(a[0][0] + a[1][1])


def rotations(word: tuple[int, ...]) -> Iterator[tuple[int, ...]]:
    for offset in range(len(word)):
        yield word[offset:] + word[:offset]


def inverse_code(word: tuple[int, ...]) -> tuple[int, ...]:
    """Return a cyclic representative for the inverse PSL word."""
    return tuple(3 - exponent for exponent in reversed(word))


def oriented_canonical(word: tuple[int, ...]) -> tuple[int, ...]:
    return min(rotations(word))


def unoriented_canonical(word: tuple[int, ...]) -> tuple[int, ...]:
    return min((*rotations(word), *rotations(inverse_code(word))))


def is_primitive_word(word: Sequence[int]) -> bool:
    n = len(word)
    for period in range(1, n):
        if n % period == 0 and all(word[i] == word[i % period] for i in range(n)):
            return False
    return True


def word_matrix(word: Sequence[int]) -> Matrix:
    r2 = matmul(R, R)
    result = IDENTITY
    for exponent in word:
        result = matmul(result, matmul(S, R if exponent == 1 else r2))
    return result


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")


@dataclass(frozen=True)
class OrbitRow:
    orbit_id: str
    code: str
    sr_block_length: int
    inverse_class_code: str
    self_reverse: bool
    matrix_a: int
    matrix_b: int
    matrix_c: int
    matrix_d: int
    trace: int
    discriminant: int
    adjoint_trace_q: int
    geodesic_length: float
    norm: float
    stable_multiplier: float
    unstable_multiplier: float
    trace_multiplicity_within_block_cutoff: int


def enumerate_classes(max_blocks: int) -> tuple[list[OrbitRow], list[dict[str, int | float]]]:
    provisional: list[dict[str, object]] = []
    growth: list[dict[str, int | float]] = []

    for size in range(1, max_blocks + 1):
        oriented_count = 0
        unoriented_count = 0
        raw_hyperbolic = 0
        for code in product((1, 2), repeat=size):
            if not is_primitive_word(code):
                continue
            matrix = word_matrix(code)
            tr = trace_abs(matrix)
            if tr <= 2:
                continue
            raw_hyperbolic += 1
            if code == oriented_canonical(code):
                oriented_count += 1
            if code != oriented_canonical(code):
                continue

            if code == unoriented_canonical(code):
                unoriented_count += 1
            discriminant = tr * tr - 4
            q = tr * tr - 2
            length = 2.0 * math.acosh(tr / 2.0)
            norm = 0.5 * (q + tr * math.sqrt(discriminant))
            inv_oriented = oriented_canonical(inverse_code(code))
            provisional.append(
                {
                    "code": "".join(map(str, code)),
                    "sr_block_length": size,
                    "inverse_class_code": "".join(map(str, inv_oriented)),
                    "self_reverse": oriented_canonical(code) == inv_oriented,
                    "matrix": matrix,
                    "trace": tr,
                    "discriminant": discriminant,
                    "q": q,
                    "length": length,
                    "norm": norm,
                }
            )

        growth.append(
            {
                "sr_block_length": size,
                "raw_primitive_hyperbolic_words": raw_hyperbolic,
                "oriented_cyclic_classes": oriented_count,
                "unoriented_cyclic_classes": unoriented_count,
                "binary_necklace_scale": (2.0**size) / size,
                "unoriented_scale": (2.0 ** (size - 1)) / size,
            }
        )

    multiplicities = Counter(int(row["trace"]) for row in provisional)
    rows: list[OrbitRow] = []
    for index, item in enumerate(provisional, start=1):
        matrix = item["matrix"]
        assert isinstance(matrix, tuple)
        norm = float(item["norm"])
        rows.append(
            OrbitRow(
                orbit_id=f"MOD-{index:06d}",
                code=str(item["code"]),
                sr_block_length=int(item["sr_block_length"]),
                inverse_class_code=str(item["inverse_class_code"]),
                self_reverse=bool(item["self_reverse"]),
                matrix_a=matrix[0][0],
                matrix_b=matrix[0][1],
                matrix_c=matrix[1][0],
                matrix_d=matrix[1][1],
                trace=int(item["trace"]),
                discriminant=int(item["discriminant"]),
                adjoint_trace_q=int(item["q"]),
                geodesic_length=float(item["length"]),
                norm=norm,
                stable_multiplier=1.0 / norm,
                unstable_multiplier=norm,
                trace_multiplicity_within_block_cutoff=multiplicities[int(item["trace"])],
            )
        )
    return rows, growth


def write_csv(path: Path, rows: Iterable[dict[str, object]], fieldnames: Sequence[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def enumerate_phase(args: argparse.Namespace) -> None:
    output = Path(args.output_dir)
    output.mkdir(parents=True, exist_ok=True)
    ledger_path = output / "modular_orbit_ledger.csv"
    growth_path = output / "orbit_growth.csv"

    rows, growth = enumerate_classes(args.max_blocks)
    fieldnames = list(asdict(rows[0]).keys()) if rows else list(OrbitRow.__annotations__)
    write_csv(ledger_path, (asdict(row) for row in rows), fieldnames)
    write_csv(growth_path, growth, list(growth[0].keys()))

    codes = {row.code for row in rows}
    checks = {
        "all_matrices_determinant_one": all(
            row.matrix_a * row.matrix_d - row.matrix_b * row.matrix_c == 1 for row in rows
        ),
        "all_hyperbolic": all(row.trace > 2 for row in rows),
        "all_codes_primitive": all(is_primitive_word(tuple(map(int, row.code))) for row in rows),
        "all_codes_canonical_oriented": all(
            tuple(map(int, row.code)) == oriented_canonical(tuple(map(int, row.code)))
            for row in rows
        ),
        "all_inverse_classes_present": all(row.inverse_class_code in codes for row in rows),
        "orientation_quotient_count_identity": len(rows)
        == 2 * sum(int(item["unoriented_cyclic_classes"]) for item in growth)
        - sum(row.self_reverse for row in rows),
    }
    if not all(checks.values()):
        raise RuntimeError(f"enumeration invariant failed: {checks}")

    manifest = {
        "phase": "orbit_enumeration_frozen_before_arithmetic_audit",
        "candidate": "unit-speed geodesic flow on T1(PSL2Z\\H)",
        "clock": "hyperbolic arc length",
        "orientation_convention": "primitive cyclic conjugacy classes; inversion retained",
        "cutoff": {"type": "SR_block_length", "maximum": args.max_blocks},
        "completeness_boundary": (
            "Complete for the stated cyclic-word convention and S-R block cutoff; "
            "not certified complete below any geometric-length cutoff."
        ),
        "multiplicity_boundary": (
            "Every trace multiplicity is only the count within this block cutoff. "
            "It is a lower bound, not a complete class-number multiplicity."
        ),
        "analysis_freeze_scope": (
            "Local reproducibility freeze, not a third-party or immutable preregistration."
        ),
        "forbidden_data": ["Riemann zeros", "prime-fitted clocks", "prime-fitted parameters"],
        "rational_prime_operations_in_this_phase": False,
        "row_count": len(rows),
        "unique_trace_count": len({row.trace for row in rows}),
        "self_reverse_count": sum(row.self_reverse for row in rows),
        "invariant_checks": checks,
        "files": {
            ledger_path.name: sha256_file(ledger_path),
            growth_path.name: sha256_file(growth_path),
            "code/modular_orbits.py": sha256_file(Path(__file__).resolve()),
            "notes/research_protocol.md": sha256_file(
                Path(__file__).resolve().parents[1] / "notes" / "research_protocol.md"
            ),
        },
        "runtime": {"python": sys.version.split()[0], "platform": platform.platform()},
    }
    write_json(output / "orbit_ledger_manifest.json", manifest)
    print(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True))


def read_frozen_ledger(ledger_path: Path, manifest_path: Path) -> tuple[list[dict[str, str]], dict]:
    with manifest_path.open(encoding="utf-8") as handle:
        manifest = json.load(handle)
    expected = manifest["files"][ledger_path.name]
    actual = sha256_file(ledger_path)
    if expected != actual:
        raise RuntimeError(f"ledger checksum mismatch: expected {expected}, found {actual}")
    with ledger_path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    return rows, manifest


def prime_sieve(limit: int) -> bytearray:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
    return sieve


def linear_regression(xs: Sequence[float], ys: Sequence[float]) -> tuple[float, float]:
    if len(xs) != len(ys) or len(xs) < 2:
        return float("nan"), float("nan")
    xbar = math.fsum(xs) / len(xs)
    ybar = math.fsum(ys) / len(ys)
    denominator = math.fsum((x - xbar) ** 2 for x in xs)
    slope = math.fsum((x - xbar) * (y - ybar) for x, y in zip(xs, ys)) / denominator
    return slope, ybar - slope * xbar


def audit_phase(args: argparse.Namespace) -> None:
    output = Path(args.output_dir)
    ledger_path = Path(args.ledger)
    manifest_path = Path(args.manifest)
    rows, manifest = read_frozen_ledger(ledger_path, manifest_path)

    trace_scan_max = args.trace_scan_max
    maximum_ledger_trace = max(int(row["trace"]) for row in rows)
    if trace_scan_max < maximum_ledger_trace:
        raise RuntimeError(
            f"--trace-scan-max={trace_scan_max} does not cover ledger maximum trace "
            f"{maximum_ledger_trace}; primality status would be unknown"
        )
    sieve_limit = trace_scan_max * trace_scan_max - 2
    sieve = prime_sieve(sieve_limit)

    repetition_rows: list[dict[str, object]] = []
    unique_by_trace: dict[int, dict[str, str]] = {}
    max_norm_identity_error = 0.0
    max_length_identity_error = 0.0
    for row in rows:
        tr = int(row["trace"])
        unique_by_trace.setdefault(tr, row)
        length = float(row["geodesic_length"])
        norm = float(row["norm"])
        q = int(row["adjoint_trace_q"])
        max_norm_identity_error = max(max_norm_identity_error, abs((norm + 1.0 / norm) - q))
        max_length_identity_error = max(max_length_identity_error, abs(math.log(norm) - length))
        q_is_prime = bool(sieve[q])

        for repeat in range(1, args.repeat_max + 1):
            ruelle_at_half = length * math.exp(-0.5 * repeat * length)
            correction = 1.0 / (1.0 - math.exp(-repeat * length))
            selberg_direct = length / (2.0 * math.sinh(0.5 * repeat * length))
            target = math.log(q) * q ** (-0.5 * repeat) if q_is_prime else None
            repetition_rows.append(
                {
                    "orbit_id": row["orbit_id"],
                    "trace": tr,
                    "adjoint_trace_q": q,
                    "q_is_prime_control": q_is_prime,
                    "repeat": repeat,
                    "repeated_length": repeat * length,
                    "selberg_amplitude_direct": selberg_direct,
                    "ruelle_logderivative_amplitude_at_s_half": ruelle_at_half,
                    "selberg_to_ruelle_ratio": correction,
                    "identity_residual": abs(selberg_direct / ruelle_at_half - correction),
                    "q_prime_target_amplitude": target if target is not None else "",
                    "selberg_to_q_prime_target": selberg_direct / target if target is not None else "",
                    "ruelle_to_q_prime_target": ruelle_at_half / target if target is not None else "",
                }
            )

    repetition_path = output / "modular_repetition_ledger.csv"
    write_csv(repetition_path, repetition_rows, list(repetition_rows[0].keys()))

    trace_rows: list[dict[str, object]] = []
    log_norms: list[float] = []
    log_deltas: list[float] = []
    for tr in range(3, trace_scan_max + 1):
        q = tr * tr - 2
        if not sieve[q]:
            continue
        discriminant = tr * tr - 4
        norm = 0.5 * (q + tr * math.sqrt(discriminant))
        length = math.log(norm)
        delta = math.log1p(norm ** -2)
        trace_rows.append(
            {
                "trace": tr,
                "norm": norm,
                "adjoint_trace_q": q,
                "q_mod_8": q % 8,
                "geodesic_length": length,
                "log_q_minus_length": delta,
                "relative_period_error": delta / math.log(q),
                "represented_in_frozen_ledger": tr in unique_by_trace,
                "multiplicity_within_frozen_block_cutoff": int(
                    unique_by_trace[tr]["trace_multiplicity_within_block_cutoff"]
                )
                if tr in unique_by_trace
                else 0,
            }
        )
        log_norms.append(math.log(norm))
        log_deltas.append(math.log(delta))

    proxy_path = output / "near_prime_proxy_scan.csv"
    write_csv(proxy_path, trace_rows, list(trace_rows[0].keys()))
    slope, intercept = linear_regression(log_norms, log_deltas)
    proxy_examples = [row for row in trace_rows if int(row["trace"]) in (3, 5, 7, 9)]

    pi_limit = sum(sieve)
    unique_prime_q_in_ledger = {
        int(row["adjoint_trace_q"])
        for row in rows
        if int(row["adjoint_trace_q"]) <= sieve_limit and sieve[int(row["adjoint_trace_q"])]
    }
    summary = {
        "phase": "arithmetic_audit_after_local_checksum_freeze",
        "input_ledger_sha256": sha256_file(ledger_path),
        "configuration": {
            "repeat_max": args.repeat_max,
            "trace_scan_max": trace_scan_max,
            "rational_prime_sieve_limit": sieve_limit,
        },
        "theorem_level_results": {
            "exact_rational_norm_hits": 0,
            "exact_prime_power_support_collisions": 0,
            "basis": (
                "If N^r were rational, Galois conjugation N -> N^-1 would give "
                "N^r=N^-r, contradicting N>1. These zeros are theorem-derived, "
                "not floating-point observations."
            ),
        },
        "frozen_ledger": {
            "row_count": len(rows),
            "unique_trace_count": len(unique_by_trace),
            "unique_prime_adjoint_trace_proxies": len(unique_prime_q_in_ledger),
            "maximum_trace_multiplicity_within_block_cutoff": max(
                int(row["trace_multiplicity_within_block_cutoff"]) for row in rows
            ),
            "multiplicity_completeness": "lower_bounds_only",
            "max_norm_plus_inverse_identity_error": max_norm_identity_error,
            "max_log_norm_minus_length_error": max_length_identity_error,
        },
        "near_prime_proxy_control": {
            "form": "q=t^2-2=tr(gamma^2)=N+N^-1",
            "prime_q_count_for_integer_traces": len(trace_rows),
            "all_prime_q_have_q_mod_8_equal_7": all(int(row["q_mod_8"]) == 7 for row in trace_rows),
            "all_prime_q_have_odd_trace": all(int(row["trace"]) % 2 == 1 for row in trace_rows),
            "all_primes_up_to_scan_limit": pi_limit,
            "observed_prime_coverage_fraction": len(trace_rows) / pi_limit,
            "asymptotic_candidate_upper_bound": "O(sqrt(X)); relative coverage O(log(X)/sqrt(X))",
            "log_delta_vs_log_norm_slope": slope,
            "log_delta_vs_log_norm_intercept": intercept,
            "expected_slope": -2.0,
            "examples": proxy_examples,
            "warning": (
                "q can be prime and log(q)-ell is O(N^-2), but q is not the orbit norm. "
                "The constraint p+2=t^2 supplies only O(sqrt(X)) candidates up to X."
            ),
        },
        "amplitude_identity": {
            "formula": "A_Selberg=A_Ruelle_logderivative_at_s_half/(1-N^-r)",
            "verification": "direct sinh evaluation compared with independent exponential form",
            "maximum_recorded_residual": max(float(row["identity_residual"]) for row in repetition_rows),
        },
        "data_boundary": {
            "rational_primes_used_only_as_declared_post_freeze_control": True,
            "Riemann_zeros_used": False,
            "source_orbit_manifest": manifest_path.name,
        },
        "files": {
            repetition_path.name: sha256_file(repetition_path),
            proxy_path.name: sha256_file(proxy_path),
        },
    }
    write_json(output / "arithmetic_audit_summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    enum = subparsers.add_parser("enumerate", help="freeze the prime-free orbit ledger")
    enum.add_argument("--max-blocks", type=int, default=16)
    enum.add_argument("--output-dir", required=True)
    enum.set_defaults(func=enumerate_phase)

    audit = subparsers.add_parser("audit", help="audit a checksum-frozen ledger")
    audit.add_argument("--ledger", required=True)
    audit.add_argument("--manifest", required=True)
    audit.add_argument("--repeat-max", type=int, default=5)
    audit.add_argument("--trace-scan-max", type=int, default=5000)
    audit.add_argument("--output-dir", required=True)
    audit.set_defaults(func=audit_phase)
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    if args.command == "enumerate" and args.max_blocks < 2:
        parser.error("--max-blocks must be at least 2")
    if args.command == "audit" and args.repeat_max < 1:
        parser.error("--repeat-max must be positive")
    if args.command == "audit" and args.trace_scan_max < 3:
        parser.error("--trace-scan-max must be at least 3")
    args.func(args)


if __name__ == "__main__":
    main()
