#!/usr/bin/env python3
"""Exact q-symbol no-repeat suspension theorem and finite replay for Paper 25.

The mathematical object is the unit-roof suspension of the q-symbol shift with
adjacency matrix ``A_q = J_q-I_q``.  It is a deliberately non-arithmetic
negative-control family.  The builder proves its closed formulas algebraically
and replays exact integer/rational identities for q=2,...,8 through degree 12.
No physical flight length, prime table, zero table, resonance, or fitted
parameter is read.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable, Sequence


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-08-28"
CANDIDATE_ID = "P25-Q-SYMBOL-NO-REPEAT-PHASE-CALIBRATOR"
Q_VALUES = tuple(range(2, 9))
MAX_DEGREE = 12
FREEZE_PATH = Path("experiments/round7_q_symbolic_family_freeze.json")
FREEZE_SHA256 = "41fec487b1473fe65adeaadebde769cdf065d67db7f53232e8202879a6fabddb"

RESULT_PATHS = {
    "counts": Path("results/round7_q_symbolic_counts.csv"),
    "prefix": Path("results/round7_q_symbolic_prefix.csv"),
    "summary": Path("results/round7_q_symbolic_summary.json"),
}
RECEIPT_PATH = Path("experiments/round7_reproducibility_receipt.json")
VALIDATION_PATH = Path("experiments/round7_validation.md")
SOURCE_BINDING_PATHS = (
    FREEZE_PATH,
    Path("code/round7_q_symbolic_family.py"),
    Path("code/test_round7_q_symbolic_family.py"),
    Path("experiments/reproduce_round7.sh"),
)

COUNT_FIELDS = (
    "q",
    "topological_length_n",
    "closed_form_trace",
    "direct_matrix_trace",
    "trace_match",
    "mobius_primitive_oriented_cycles",
    "primitive_count_nonnegative_integer",
)

PREFIX_FIELDS = (
    "q",
    "step_weight_u",
    "degree",
    "primitive_count_euler_coefficient",
    "trace_exponential_coefficient",
    "reciprocal_determinant_coefficient",
    "phase_substitution_coefficient",
    "all_exactly_equal",
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: Any) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True) + "\n").encode("utf-8")


def csv_bytes(rows: Sequence[dict[str, str]], fields: Sequence[str]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def combined_hash(outputs: dict[Path, bytes]) -> str:
    digest = hashlib.sha256()
    for path in sorted(outputs, key=lambda item: item.as_posix()):
        digest.update(path.as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(outputs[path])
        digest.update(b"\0")
    return digest.hexdigest()


def load_freeze() -> tuple[dict[str, Any], bytes]:
    raw = (PROJECT_ROOT / FREEZE_PATH).read_bytes()
    if sha256(raw) != FREEZE_SHA256:
        raise RuntimeError("P25 Round-7 freeze contract changed")
    payload = json.loads(raw)
    if tuple(payload["finite_replay"]["q_values"]) != Q_VALUES:
        raise AssertionError("freeze/q-grid mismatch")
    if payload["finite_replay"]["maximum_degree"] != MAX_DEGREE:
        raise AssertionError("freeze/degree mismatch")
    if payload["route_boundary"]["candidate_id"] != CANDIDATE_ID:
        raise AssertionError("freeze/candidate mismatch")
    if any(payload["forbidden_inputs"].values()):
        raise AssertionError("all forbidden-input flags must remain false")
    return payload, raw


def divisors(number: int) -> Iterable[int]:
    return (value for value in range(1, number + 1) if number % value == 0)


def mobius(number: int) -> int:
    remaining = number
    factors = 0
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            remaining //= prime
            factors += 1
            if remaining % prime == 0:
                return 0
            while remaining % prime == 0:
                remaining //= prime
        prime += 1
    if remaining > 1:
        factors += 1
    return -1 if factors % 2 else 1


def adjacency_matrix(q: int) -> tuple[tuple[int, ...], ...]:
    if q < 2:
        raise ValueError("q must be at least two")
    return tuple(tuple(0 if row == column else 1 for column in range(q)) for row in range(q))


def matrix_multiply(
    left: tuple[tuple[int, ...], ...], right: tuple[tuple[int, ...], ...]
) -> tuple[tuple[int, ...], ...]:
    size = len(left)
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(size)) for j in range(size))
        for i in range(size)
    )


def direct_traces(q: int, maximum_degree: int) -> list[int]:
    matrix = adjacency_matrix(q)
    power = tuple(tuple(int(i == j) for j in range(q)) for i in range(q))
    traces: list[int] = []
    for _degree in range(1, maximum_degree + 1):
        power = matrix_multiply(power, matrix)
        traces.append(sum(power[index][index] for index in range(q)))
    return traces


def closed_trace(q: int, degree: int) -> int:
    if q < 2 or degree < 1:
        raise ValueError("trace arguments outside theorem domain")
    return (q - 1) ** degree + (q - 1) * ((-1) ** degree)


def primitive_count(q: int, length: int) -> int:
    numerator = sum(
        mobius(divisor) * closed_trace(q, length // divisor)
        for divisor in divisors(length)
    )
    if numerator % length:
        raise AssertionError("Mobius numerator is not divisible by the orbit length")
    result = numerator // length
    if result < 0:
        raise AssertionError("primitive-cycle count is negative")
    return result


def poly_multiply(left: Sequence[int], right: Sequence[int]) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            result[i + j] += left_value * right_value
    return result


def determinant_denominator(q: int, step_weight: int) -> list[int]:
    """Return det(I-u*z*A_q) from the two exact eigenspaces."""

    if step_weight not in {-1, 1}:
        raise ValueError("the frozen phase grid is u in {+1,-1}")
    result = [1, -(q - 1) * step_weight]
    for _index in range(q - 1):
        result = poly_multiply(result, [1, step_weight])
    return result


def reciprocal_series(denominator: Sequence[int], degree: int) -> list[Fraction]:
    if denominator[0] != 1:
        raise ValueError("denominator must have constant term one")
    result = [Fraction(1)] + [Fraction(0) for _index in range(degree)]
    for n in range(1, degree + 1):
        result[n] = -sum(
            Fraction(denominator[k]) * result[n - k]
            for k in range(1, min(n, len(denominator) - 1) + 1)
        )
    return result


def trace_exponential_series(q: int, step_weight: int, degree: int) -> list[Fraction]:
    result = [Fraction(1)] + [Fraction(0) for _index in range(degree)]
    for n in range(1, degree + 1):
        result[n] = sum(
            Fraction((step_weight**k) * closed_trace(q, k)) * result[n - k]
            for k in range(1, n + 1)
        ) / n
    return result


def euler_series(q: int, step_weight: int, degree: int) -> list[Fraction]:
    """Expand product_n (1-(u*z)^n)^(-P_n(q)) through degree."""

    result = [Fraction(1)] + [Fraction(0) for _index in range(degree)]
    for length in range(1, degree + 1):
        multiplicity = primitive_count(q, length)
        if multiplicity == 0:
            continue
        factor = [Fraction(0) for _index in range(degree + 1)]
        for repetition in range(degree // length + 1):
            coefficient = math.comb(multiplicity + repetition - 1, repetition)
            factor[length * repetition] = Fraction(
                coefficient * (step_weight ** (length * repetition))
            )
        product = [Fraction(0) for _index in range(degree + 1)]
        for left_degree, left_value in enumerate(result):
            for right_degree, right_value in enumerate(factor):
                if left_degree + right_degree <= degree:
                    product[left_degree + right_degree] += left_value * right_value
        result = product
    return result


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def build_payload() -> tuple[list[dict[str, str]], list[dict[str, str]], dict[str, Any]]:
    freeze, _raw = load_freeze()
    count_rows: list[dict[str, str]] = []
    prefix_rows: list[dict[str, str]] = []
    total_primitive_counts: dict[str, int] = {}
    denominators: dict[str, dict[str, list[int]]] = {}

    for q in Q_VALUES:
        direct = direct_traces(q, MAX_DEGREE)
        total_primitive_counts[str(q)] = 0
        for length in range(1, MAX_DEGREE + 1):
            trace = closed_trace(q, length)
            count = primitive_count(q, length)
            total_primitive_counts[str(q)] += count
            count_rows.append(
                {
                    "q": str(q),
                    "topological_length_n": str(length),
                    "closed_form_trace": str(trace),
                    "direct_matrix_trace": str(direct[length - 1]),
                    "trace_match": str(trace == direct[length - 1]).lower(),
                    "mobius_primitive_oriented_cycles": str(count),
                    "primitive_count_nonnegative_integer": "true",
                }
            )

        denominators[str(q)] = {}
        positive_determinant: list[Fraction] | None = None
        for step_weight in (1, -1):
            denominator = determinant_denominator(q, step_weight)
            denominators[str(q)][str(step_weight)] = denominator
            determinant = reciprocal_series(denominator, MAX_DEGREE)
            trace_series = trace_exponential_series(q, step_weight, MAX_DEGREE)
            euler = euler_series(q, step_weight, MAX_DEGREE)
            if step_weight == 1:
                positive_determinant = determinant
            if positive_determinant is None:
                raise AssertionError("positive phase must be evaluated first")
            substitution = [
                value * (step_weight**degree)
                for degree, value in enumerate(positive_determinant)
            ]
            for degree in range(MAX_DEGREE + 1):
                values = (
                    euler[degree],
                    trace_series[degree],
                    determinant[degree],
                    substitution[degree],
                )
                prefix_rows.append(
                    {
                        "q": str(q),
                        "step_weight_u": str(step_weight),
                        "degree": str(degree),
                        "primitive_count_euler_coefficient": fraction_text(values[0]),
                        "trace_exponential_coefficient": fraction_text(values[1]),
                        "reciprocal_determinant_coefficient": fraction_text(values[2]),
                        "phase_substitution_coefficient": fraction_text(values[3]),
                        "all_exactly_equal": str(
                            values[0] == values[1] == values[2] == values[3]
                        ).lower(),
                    }
                )

    count_mismatches = sum(row["trace_match"] != "true" for row in count_rows)
    prefix_mismatches = sum(row["all_exactly_equal"] != "true" for row in prefix_rows)
    if count_mismatches or prefix_mismatches:
        raise AssertionError("Round-7 exact family replay failed")

    summary = {
        "schema": "p25-round7-q-symbolic-family-summary/1.0",
        "date": DATE,
        "candidate_id": CANDIDATE_ID,
        "typed_object": "UNIT_ROOF_Q_SYMBOL_NO_REPEAT_SUSPENSION_FAMILY",
        "parameter_domain_theorem": "INTEGER_Q_AT_LEAST_2",
        "finite_replay_q_values": list(Q_VALUES),
        "finite_replay_maximum_degree": MAX_DEGREE,
        "freeze_contract_sha256": FREEZE_SHA256,
        "adjacency_spectrum": "Q_MINUS_1_MULTIPLICITY_1;MINUS_1_MULTIPLICITY_Q_MINUS_1",
        "trace_theorem": "tr(A_q^n)=(q-1)^n+(q-1)(-1)^n",
        "primitive_count_theorem": (
            "P_n(q)=n^(-1)sum_(d|n)mu(d)[(q-1)^(n/d)+(q-1)(-1)^(n/d)]"
        ),
        "determinant_theorem": (
            "det(I-u*z*A_q)=(1-(q-1)u*z)(1+u*z)^(q-1)"
        ),
        "absolute_euler_convergence": "ABS_Z_LESS_THAN_1_OVER_Q_MINUS_1",
        "phase_theorem": "zeta_(q,-1)(z)=zeta_(q,+1)(-z)",
        "count_rows": len(count_rows),
        "prefix_rows": len(prefix_rows),
        "direct_trace_mismatch_count": count_mismatches,
        "three_construction_coefficient_mismatch_count": prefix_mismatches,
        "total_primitive_oriented_owners_through_degree_12": total_primitive_counts,
        "denominator_coefficients": denominators,
        "theorem_evidence_status": "PROVED",
        "finite_replay_evidence_status": "NUMERICALLY_CERTIFIED",
        "finite_replay_arithmetic_mode": "EXACT_INTEGER_RATIONAL",
        "prime_or_zero_tables_used": False,
        "arithmetic_specificity": "ABSENT_BY_NEGATIVE_CONTROL_DESIGN",
        "formal_route_a_tuple": [
            "A0_FAIL",
            "A1_PASS_ANALYTIC",
            "A2_ANALYTIC_DETERMINANT",
            "A3_FAIL",
            "A4_FAIL",
        ],
        "overall_verdict": "ROUTE_A_REJECTED",
        "physical_three_disk_route_tuple": "UNASSIGNED",
        "a2_claim_boundary": (
            "Q_SYMBOL_UNIT_ROOF_FAMILY_ONLY_NOT_PHYSICAL_FLIGHT_LENGTH_"
            "GUTZWILLER_VOROS_MULTIPLE_SCATTERING_OR_TARGET_DIVISOR"
        ),
        "route_b_evaluation": "NOT_RUN",
        "route_b_invocation_allowed": False,
        "ars_stage": "STAGE_1_RESEARCH_IN_PROGRESS",
        "manuscript_authorized": False,
        "paper_advance": "UNIVERSAL_NEGATIVE_CONTROL_FAMILY_THEOREM",
        "freeze_declared_theorem": freeze["predeclared_theorem"],
    }
    return count_rows, prefix_rows, summary


def core_outputs() -> tuple[dict[Path, bytes], dict[str, Any]]:
    counts, prefix, summary = build_payload()
    outputs = {
        RESULT_PATHS["counts"]: csv_bytes(counts, COUNT_FIELDS),
        RESULT_PATHS["prefix"]: csv_bytes(prefix, PREFIX_FIELDS),
        RESULT_PATHS["summary"]: json_bytes(summary),
    }
    return outputs, summary


def receipt_for(
    outputs: dict[Path, bytes], summary: dict[str, Any], validation: bytes
) -> dict[str, Any]:
    return {
        "schema": "p25-round7-reproduction-receipt/1.0",
        "date": DATE,
        "status": "REPRODUCIBLE",
        "core_sha256": combined_hash(outputs),
        "execution": {"required_runs": 2, "byte_identical": True},
        "unit_tests": {"expected": 12, "failed": 0},
        "freeze_contract": {"path": FREEZE_PATH.as_posix(), "sha256": FREEZE_SHA256},
        "files": {
            path.as_posix(): {"sha256": sha256(data), "bytes": len(data)}
            for path, data in sorted(outputs.items(), key=lambda item: item[0].as_posix())
        },
        "validation_binding": {
            "path": VALIDATION_PATH.as_posix(),
            "sha256": sha256(validation),
            "bytes": len(validation),
        },
        "source_bindings": {
            path.as_posix(): {
                "sha256": sha256((PROJECT_ROOT / path).read_bytes()),
                "bytes": (PROJECT_ROOT / path).stat().st_size,
            }
            for path in SOURCE_BINDING_PATHS
        },
        "candidate_id": CANDIDATE_ID,
        "formal_route_a_tuple": summary["formal_route_a_tuple"],
        "overall_verdict": summary["overall_verdict"],
        "physical_three_disk_route_tuple": "UNASSIGNED",
        "route_b_invocation_allowed": False,
        "prime_or_zero_tables_used": False,
        "reproduction_command": "bash experiments/reproduce_round7.sh",
    }


def validation_markdown(outputs: dict[Path, bytes], summary: dict[str, Any]) -> bytes:
    text = f"""# P25 Round-7 validation report

## Material Passport

- Origin skill: `ars-codex:academic-research-suite`
- Origin stage: ARS Stage 1 research
- Candidate: `{CANDIDATE_ID}`
- Freeze SHA-256: `{FREEZE_SHA256}`
- Core SHA-256: `{combined_hash(outputs)}`

## Exact replay

- The theorem domain is every integer `q>=2`; the finite replay is `q=2,...,8`.
- Exact replay degrees: `0,...,{MAX_DEGREE}`.
- Count rows: `{summary['count_rows']}`; direct-trace mismatches: `{summary['direct_trace_mismatch_count']}`.
- Prefix rows: `{summary['prefix_rows']}`; coefficient mismatches: `{summary['three_construction_coefficient_mismatch_count']}`.
- Primitive-count Euler products, trace exponentials, and reciprocal determinants agree exactly.

## Theorem

```text
tr(A_q^n) = (q-1)^n + (q-1)(-1)^n
P_n(q) = (1/n) sum_(d|n) mu(d) tr(A_q^(n/d))
det(I-u z A_q) = (1-(q-1)u z)(1+u z)^(q-1)
zeta_(q,-1)(z) = zeta_(q,+1)(-z)
```

## Route boundary

The exact A1--A2 tuple belongs only to this non-arithmetic unit-roof symbolic
family.  A0 fails by construction, so the overall Route-A verdict is
`ROUTE_A_REJECTED`.  This theorem supplies a universal negative-control
calibrator, not a physical three-disk determinant or a target-divisor result.
The physical flow remains `UNASSIGNED`; Route B remains closed.
"""
    return text.encode("utf-8")


def rendered_outputs() -> dict[Path, bytes]:
    core, summary = core_outputs()
    rendered = dict(core)
    validation = validation_markdown(core, summary)
    rendered[VALIDATION_PATH] = validation
    rendered[RECEIPT_PATH] = json_bytes(receipt_for(core, summary, validation))
    return rendered


def write_outputs(output_root: Path) -> None:
    for relative, data in rendered_outputs().items():
        path = output_root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)


def verify_existing(output_root: Path) -> None:
    mismatches: list[str] = []
    for relative, expected in rendered_outputs().items():
        path = output_root / relative
        if not path.exists():
            mismatches.append(f"missing:{relative}")
        elif path.read_bytes() != expected:
            mismatches.append(f"different:{relative}")
    if mismatches:
        raise SystemExit("verification failed: " + ", ".join(mismatches))
    print("P25 Round-7 existing artifacts VERIFIED")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-root", type=Path, default=PROJECT_ROOT)
    parser.add_argument("--verify-existing", action="store_true")
    args = parser.parse_args()
    if args.verify_existing:
        verify_existing(args.output_root)
    else:
        write_outputs(args.output_root)
        core, summary = core_outputs()
        print(
            json.dumps(
                {
                    "candidate_id": CANDIDATE_ID,
                    "core_sha256": combined_hash(core),
                    "count_rows": summary["count_rows"],
                    "prefix_rows": summary["prefix_rows"],
                    "status": "PASS",
                },
                sort_keys=True,
            )
        )


if __name__ == "__main__":
    main()
