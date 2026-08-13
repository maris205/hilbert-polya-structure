#!/usr/bin/env python3
"""Independent, fail-closed checker for HCS-C45.

No producer code is imported.  The checker independently enumerates the
one- and two-return chronological phase zeroes, reconstructs normalized
moments with exact fractions, and audits all virtual-degree inequalities.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
from typing import Any, Callable


SCHEMA = "hcs-c45-certificate-v1"
TRACE_CONTROL_BOUND = 499
N2_CONTROL_PRIMES = (7, 13, 19, 31, 37, 43, 61, 67, 73, 79, 97)
N2_EXPECTED_TRACES = (-6, -6, -6, -30, 18, -54, 18, 42, -30, 42, -30)
PREFIX_DEGREE_BUDGETS = (0, 2, 4, 6, 8, 16, 32)


class GateFailure(Exception):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise GateFailure(message)


def canonical_json(obj: Any) -> bytes:
    return json.dumps(
        obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def strict_equal(left: Any, right: Any) -> bool:
    if type(left) is not type(right):
        return False
    if isinstance(left, dict):
        return set(left) == set(right) and all(
            strict_equal(left[key], right[key]) for key in left
        )
    if isinstance(left, list):
        return len(left) == len(right) and all(
            strict_equal(a, b) for a, b in zip(left, right)
        )
    return left == right


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def is_prime(n: int) -> bool:
    if type(n) is not int or n < 2:
        return False
    for divisor in range(2, int(n**0.5) + 1):
        if n % divisor == 0:
            return False
    return True


def multiplicative_order(value: int, p: int) -> int:
    running = 1
    for exponent in range(1, p):
        running = running * value % p
        if running == 1:
            return exponent
    raise GateFailure("multiplicative order not found")


def least_primitive_root(p: int) -> int:
    for candidate in range(2, p):
        if multiplicative_order(candidate, p) == p - 1:
            return candidate
    raise GateFailure("primitive root not found")


def split_primes_through(bound: int) -> list[int]:
    return [p for p in range(5, bound + 1) if p % 3 == 1 and is_prime(p)]


def fraction_record(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def independently_count_n1(p: int, rho: int) -> int:
    count = 0
    coefficient = (rho + 1) % p
    for x in range(p):
        x_term = 2 * pow(x, 3, p)
        for y in range(p):
            phase = x_term + 2 * pow(y, 3, p) + coefficient * x * y
            count += phase % p == 0
    return count


def independently_count_n2(p: int, rho: int) -> int:
    """Separate exact implementation of the four-variable zero count."""
    # roots[(a,b)] counts t with 2t^3+a*t=b.  A dictionary layout and direct
    # prefix formula keep this implementation independent of the producer's
    # row-array code while retaining O(p^3) exact complexity.
    roots: dict[tuple[int, int], int] = {}
    for linear in range(p):
        for t in range(p):
            value = (2 * pow(t, 3, p) + linear * t) % p
            roots[(linear, value)] = roots.get((linear, value), 0) + 1
    count = 0
    cubic = [2 * pow(t, 3, p) % p for t in range(p)]
    for x0 in range(p):
        for x1 in range(p):
            for x2 in range(p):
                fixed = (
                    x0 * x1
                    + x1 * x2
                    + cubic[x0]
                    + cubic[x1]
                    + cubic[x2]
                ) % p
                linear = (x2 + rho * x0) % p
                count += roots.get((linear, (-fixed) % p), 0)
    return count


@lru_cache(maxsize=None)
def rebuild_trace_control(p: int) -> dict[str, Any]:
    require(type(p) is int and is_prime(p) and p % 3 == 1, "invalid trace prime")
    generator = least_primitive_root(p)
    rho = pow(generator, (p - 1) // 3, p)
    require(rho != 1 and pow(rho, 3, p) == 1, "rho order mismatch")
    zero_count = independently_count_n1(p, rho)
    require(zero_count == p - 3, "n=1 zero-fibre formula mismatch")
    trace = 2 * zero_count - 2 * p
    require(trace == -6, "first Galois trace mismatch")
    degree = (p - 1) // 2
    virtual_degree = 4 * degree
    return {
        "prime": p,
        "least_primitive_root": generator,
        "rho_order_3": rho,
        "real_cyclotomic_degree": degree,
        "chronological_n1_zero_count": zero_count,
        "ordinary_norm_first_log_moment_C_p_1": trace,
        "normalized_first_log_moment_c_p_1": fraction_record(Fraction(trace, degree)),
        "ordinary_norm_virtual_degree": virtual_degree,
        "prefactor_lower_bounds": [
            {
                "bounded_absolute_virtual_degree_M": budget,
                "triangle_inequality_rhs": virtual_degree - budget,
            }
            for budget in PREFIX_DEGREE_BUDGETS
        ],
    }


@lru_cache(maxsize=None)
def rebuild_n2_control(p: int) -> dict[str, Any]:
    require(p in N2_CONTROL_PRIMES, "unexpected n=2 control prime")
    generator = least_primitive_root(p)
    rho = pow(generator, (p - 1) // 3, p)
    zero_count = independently_count_n2(p, rho)
    require((2 * zero_count) % p == 0, "n=2 trace is not integral")
    trace = 2 * zero_count // p - 2 * p * p
    normalized = Fraction(trace, (p - 1) // 2)
    return {
        "prime": p,
        "rho_order_3": rho,
        "chronological_phase": "x0*x1+x1*x2+x2*x3+rho*x3*x0+2*(x0^3+x1^3+x2^3+x3^3)",
        "chronological_n2_zero_count": zero_count,
        "ordinary_norm_second_log_moment_C_p_2": trace,
        "normalized_second_log_moment_c_p_2": fraction_record(normalized),
        "after_multiply_by_one_minus_z_power_6_second_log_moment": trace + 6,
    }


def expected_source_lock(project_root: Path) -> list[dict[str, str]]:
    henon_root = project_root.parent
    relatives = (
        "henon_mu3_augmented_euler_superproduct/results/c43_certificate.json",
        "henon_mu3_fixed_coefficient_field_obstruction/results/c44_certificate.json",
    )
    return [
        {
            "path": f"henon_dynamics/{relative}",
            "sha256": sha256_file(henon_root / relative),
        }
        for relative in relatives
    ]


def expected_payload(project_root: Path) -> dict[str, Any]:
    trace_primes = split_primes_through(TRACE_CONTROL_BOUND)
    trace_controls = [rebuild_trace_control(p) for p in trace_primes]
    n2_controls = [rebuild_n2_control(p) for p in N2_CONTROL_PRIMES]
    require(
        tuple(row["ordinary_norm_second_log_moment_C_p_2"] for row in n2_controls)
        == N2_EXPECTED_TRACES,
        "frozen n=2 trace ledger mismatch",
    )
    return {
        "material_passport": {
            "candidate_id": "HCS-C45",
            "project": "henon_mu3_galois_norm_rank_obstruction",
            "ai_assistance_disclosed": True,
            "evidence_policy": "exact all-prime degree argument plus exact chronological finite controls; no zero-table data",
        },
        "source_lock": expected_source_lock(project_root),
        "definitions": {
            "coefficient_field": "L_p=Q(zeta_p)^+ with d_p=(p-1)/2",
            "paired_local_factor": "E_p(z)=D_p(z;psi)*D_p(z;psi^-1) in L_p(z)",
            "ordinary_galois_norm": "N_p(z)=Norm_(L_p/Q)(E_p(z)) in Q(z)",
            "ordinary_norm_log": "Log N_p(z)=-sum_(n>=1) C_p,n*z^n/n with C_p,n=Tr_(L_p/Q)(B_p,n)",
            "normalized_log_norm": "G_p(z)=exp((1/d_p)*Log_0 N_p(z)) near z=0",
            "normalized_log": "Log G_p(z)=-sum_(n>=1) c_p,n*z^n/n with c_p,n=C_p,n/d_p",
            "split_prime_clock": "z=p^(-s)=Norm(mathfrak_p)^(-s)",
            "chronology": "all B_p,n retain the rho-twisted ordered 2n-step Henon phase",
        },
        "all_prime_theorems": {
            "first_trace": "C_p,1=Tr_(L_p/Q)(B_p,1)=-6",
            "ordinary_norm_virtual_degree": "vdeg N_p=4*d_p=2*(p-1)",
            "ordinary_norm_leading_coefficient": "nonzero",
            "bounded_prefactor_no_go": "if Q_p in Q(z) and abs(vdeg Q_p)<=M independent of p, then abs(vdeg(Q_p*N_p))>=2*(p-1)-M",
            "fixed_rank_conclusion": "no uniformly bounded finite-rank graded determinant can realize Q_p*N_p",
            "ordinary_norm_euler_germ": "product_p N_p(p^(-s)) converges locally uniformly and is nonzero for Re(s)>1",
            "normalized_first_moment": "c_p,1=-12/(p-1)",
            "normalized_higher_moment_bound": "abs(c_p,n)<=4*4^n for n>=2",
            "normalized_euler_germ": "product_p G_p(p^(-s)) converges locally uniformly and is nonzero for Re(s)>1/2",
            "normalized_root_determinant_gate": "G_p is an ordinary rational determinant only if every divisor multiplicity of N_p is divisible by d_p",
        },
        "exact_trace_controls": trace_controls,
        "exact_chronological_n2_controls": n2_controls,
        "aggregate_control": {
            "trace_control_bound_inclusive": TRACE_CONTROL_BOUND,
            "trace_control_primes": trace_primes,
            "number_of_trace_controls": len(trace_controls),
            "all_n1_zero_counts_equal_p_minus_3": True,
            "all_first_traces_equal_minus_6": True,
            "all_norm_virtual_degrees_equal_2_times_p_minus_1": True,
            "maximum_certified_norm_virtual_degree": max(2 * (p - 1) for p in trace_primes),
            "n2_control_primes": list(N2_CONTROL_PRIMES),
            "n2_trace_ledger": [
                row["ordinary_norm_second_log_moment_C_p_2"] for row in n2_controls
            ],
            "normalized_n2_moments_are_not_constant": len(
                {
                    (
                        row["normalized_second_log_moment_c_p_2"]["numerator"],
                        row["normalized_second_log_moment_c_p_2"]["denominator"],
                    )
                    for row in n2_controls
                }
            )
            > 1,
            "one_minus_z_power_6_is_only_first_order_normalization": any(
                row["after_multiply_by_one_minus_z_power_6_second_log_moment"] != 0
                for row in n2_controls
            ),
        },
        "decisions": {
            "ordinary_galois_norm_rational_descent": "EXACT_BUT_UNBOUNDED_LOCAL_RANK",
            "bounded_degree_rational_prefactor_repair": "REFUTED_ALL_SPLIT_PRIMES",
            "normalized_log_norm_analytic_acceleration": "PROVED_RE_S_GREATER_THAN_ONE_HALF",
            "normalized_log_norm_as_rational_fredholm_determinant": "OPEN_DIVISOR_MULTIPLICITY_GATE",
            "one_minus_z_power_6_tate_cancellation": "NOT_CLAIMED_BEYOND_FIRST_LOG_COEFFICIENT",
            "next_large_gate": "TEST_DIVISOR_MULTIPLICITIES_OF_N_p_MOD_d_p_AND_LOCAL_MONODROMY",
        },
        "route_a": {
            "A1": "A1_WEAK",
            "A2": "A2_ANALYTIC_DETERMINANT",
            "A2_reason": "ordinary norm is rational and gives an Euler germ on Re(s)>1; normalized root improves to Re(s)>1/2 but is not yet an ordinary determinant",
            "A3": "A3_PARTIAL_ANALYTIC_STRUCTURE",
            "A3_reason": "normalized Log_0 norm reaches the critical-boundary half-plane, while continuation, functional equation, and divisor integrality remain open",
            "A4": "A4_NATURAL_QUANTIZATION",
            "overall": "ROUTE_A_EXPLORATORY",
            "scoped_status": "ROUTE_A_EXPLORATORY_CRITICAL_BOUNDARY_GERM",
            "route_b_invocation_allowed": False,
        },
        "scope": {
            "rh_proved": False,
            "hilbert_polya_operator_constructed": False,
            "global_meromorphic_continuation_claimed": False,
            "gamma_factor_claimed": False,
            "riemann_zero_data_used": False,
            "normalized_root_claimed_rational": False,
            "normalized_root_claimed_fredholm_determinant": False,
            "bounded_rank_claimed_for_ordinary_norm": False,
            "inert_prime_factor_constructed": False,
        },
    }


def audit_certificate(certificate: Any, project_root: Path) -> tuple[list[dict[str, str]], bool]:
    gates: list[dict[str, str]] = []

    def run(name: str, check: Callable[[], None]) -> None:
        try:
            check()
        except GateFailure as exc:
            gates.append({"gate": name, "status": "FAIL", "detail": str(exc)})
        except Exception as exc:
            gates.append(
                {
                    "gate": name,
                    "status": "ERROR",
                    "detail": f"{type(exc).__name__}: {exc}",
                }
            )
        else:
            gates.append({"gate": name, "status": "PASS", "detail": "verified"})

    def schema_gate() -> None:
        require(type(certificate) is dict, "certificate must be a dictionary")
        require(set(certificate) == {"schema", "payload", "payload_sha256"}, "top-level key mismatch")
        require(certificate["schema"] == SCHEMA, "schema mismatch")
        require(type(certificate["payload"]) is dict, "payload must be a dictionary")
        require(type(certificate["payload_sha256"]) is str, "digest must be a string")

    def digest_gate() -> None:
        digest = hashlib.sha256(canonical_json(certificate["payload"])).hexdigest()
        require(certificate["payload_sha256"] == digest, "payload digest mismatch")

    def source_gate() -> None:
        require(
            strict_equal(certificate["payload"]["source_lock"], expected_source_lock(project_root)),
            "source lock mismatch",
        )

    def prime_scope_gate() -> None:
        aggregate = certificate["payload"]["aggregate_control"]
        require(type(aggregate["trace_control_bound_inclusive"]) is int, "bound must be integer")
        require(aggregate["trace_control_bound_inclusive"] == TRACE_CONTROL_BOUND, "trace bound mismatch")
        expected = split_primes_through(TRACE_CONTROL_BOUND)
        require(aggregate["trace_control_primes"] == expected, "trace-prime ledger incomplete")
        actual = [row["prime"] for row in certificate["payload"]["exact_trace_controls"]]
        require(all(type(p) is int for p in actual), "prime/bool type confusion")
        require(actual == expected, "trace controls do not match prime ledger")
        require(aggregate["n2_control_primes"] == list(N2_CONTROL_PRIMES), "n=2 ledger mismatch")

    def trace_gate() -> None:
        for row in certificate["payload"]["exact_trace_controls"]:
            p = row["prime"]
            require(strict_equal(row, rebuild_trace_control(p)), f"trace control mismatch at p={p}")

    def virtual_degree_gate() -> None:
        for row in certificate["payload"]["exact_trace_controls"]:
            p = row["prime"]
            require(type(p) is int and is_prime(p), "virtual-degree prime must be a prime integer")
            degree = row["ordinary_norm_virtual_degree"]
            require(type(degree) is int, "virtual degree must be integer")
            require(degree == 2 * (p - 1), f"norm virtual degree mismatch at p={p}")
            for control in row["prefactor_lower_bounds"]:
                budget = control["bounded_absolute_virtual_degree_M"]
                require(type(budget) is int and budget >= 0, "prefactor budget invalid")
                require(
                    control["triangle_inequality_rhs"] == degree - budget,
                    f"triangle lower bound mismatch at p={p}, M={budget}",
                )

    def n2_gate() -> None:
        controls = certificate["payload"]["exact_chronological_n2_controls"]
        require([row["prime"] for row in controls] == list(N2_CONTROL_PRIMES), "n=2 row order mismatch")
        for row in controls:
            require(strict_equal(row, rebuild_n2_control(row["prime"])), f"n=2 control mismatch at p={row['prime']}")
        require(
            tuple(row["ordinary_norm_second_log_moment_C_p_2"] for row in controls)
            == N2_EXPECTED_TRACES,
            "frozen n=2 trace ledger mismatch",
        )

    def normalized_gate() -> None:
        for row in certificate["payload"]["exact_trace_controls"]:
            require(
                type(row["prime"]) is int and is_prime(row["prime"]),
                "normalized-moment prime must be a prime integer",
            )
            expected = Fraction(-12, row["prime"] - 1)
            actual = row["normalized_first_log_moment_c_p_1"]
            require(actual == fraction_record(expected), f"normalized first moment mismatch at p={row['prime']}")
        theorem = certificate["payload"]["all_prime_theorems"]
        require(theorem["normalized_higher_moment_bound"] == "abs(c_p,n)<=4*4^n for n>=2", "normalized bound changed")
        require(theorem["normalized_euler_germ"].endswith("Re(s)>1/2"), "normalized half-plane changed")

    def first_order_only_gate() -> None:
        controls = certificate["payload"]["exact_chronological_n2_controls"]
        corrected = [row["after_multiply_by_one_minus_z_power_6_second_log_moment"] for row in controls]
        require(any(value != 0 for value in corrected), "(1-z)^6 falsely cancels all second moments")
        require(certificate["payload"]["decisions"]["one_minus_z_power_6_tate_cancellation"] == "NOT_CLAIMED_BEYOND_FIRST_LOG_COEFFICIENT", "Tate scope changed")

    def decision_gate() -> None:
        decisions = certificate["payload"]["decisions"]
        require(decisions["ordinary_galois_norm_rational_descent"] == "EXACT_BUT_UNBOUNDED_LOCAL_RANK", "ordinary norm verdict changed")
        require(decisions["bounded_degree_rational_prefactor_repair"] == "REFUTED_ALL_SPLIT_PRIMES", "prefactor verdict changed")
        require(decisions["normalized_log_norm_analytic_acceleration"] == "PROVED_RE_S_GREATER_THAN_ONE_HALF", "normalized germ verdict changed")
        require(decisions["normalized_log_norm_as_rational_fredholm_determinant"] == "OPEN_DIVISOR_MULTIPLICITY_GATE", "root determinant gate changed")

    def route_scope_gate() -> None:
        route = certificate["payload"]["route_a"]
        require(route["A1"] == "A1_WEAK", "A1 label changed")
        require(route["A2"] == "A2_ANALYTIC_DETERMINANT", "A2 label changed")
        require(route["A3"] == "A3_PARTIAL_ANALYTIC_STRUCTURE", "A3 label changed")
        require(route["A4"] == "A4_NATURAL_QUANTIZATION", "A4 label changed")
        require(route["overall"] == "ROUTE_A_EXPLORATORY", "Route-A verdict changed")
        require(route["scoped_status"] == "ROUTE_A_EXPLORATORY_CRITICAL_BOUNDARY_GERM", "Route-A scoped status changed")
        require(route["route_b_invocation_allowed"] is False, "Route B improperly enabled")
        scope = certificate["payload"]["scope"]
        require(all(type(value) is bool for value in scope.values()), "scope values must be booleans")
        require(not any(scope.values()), "prohibited scope claim is true")

    def full_payload_gate() -> None:
        require(strict_equal(certificate["payload"], expected_payload(project_root)), "full payload replay mismatch")

    run("G01_SCHEMA_AND_TYPES", schema_gate)
    run("G02_PAYLOAD_DIGEST", digest_gate)
    run("G03_SOURCE_LOCK", source_gate)
    run("G04_COMPLETE_PRIME_SCOPE", prime_scope_gate)
    run("G05_EXACT_FIRST_TRACE_CONTROLS", trace_gate)
    run("G06_NORM_VIRTUAL_DEGREE_AND_PREFIX_NO_GO", virtual_degree_gate)
    run("G07_CHRONOLOGICAL_SECOND_MOMENTS", n2_gate)
    run("G08_NORMALIZED_LOG_NORM_MOMENTS", normalized_gate)
    run("G09_FIRST_ORDER_TATE_SCOPE", first_order_only_gate)
    run("G10_ORDINARY_AND_NORMALIZED_DECISIONS", decision_gate)
    run("G11_ROUTE_A_AND_SCOPE", route_scope_gate)
    run("G12_FULL_PAYLOAD_REPLAY", full_payload_gate)
    return gates, all(row["status"] == "PASS" for row in gates)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate")
    parser.add_argument("--output")
    arguments = parser.parse_args()
    certificate_path = Path(arguments.certificate)
    project_root = Path(__file__).resolve().parents[1]
    certificate = json.loads(certificate_path.read_text(encoding="utf-8"))
    gates, passed = audit_certificate(certificate, project_root)
    report = {
        "schema": "hcs-c45-independent-check-v1",
        "certificate_sha256": sha256_file(certificate_path),
        "gates": gates,
        "passed": passed,
    }
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if arguments.output:
        Path(arguments.output).write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
