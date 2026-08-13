#!/usr/bin/env python3
"""Independent, type-strict checker for the HCS-C44 certificate.

This file does not import the producer.  It rebuilds every finite-field
histogram with a separately written loop, verifies the moment witnesses and
Galois stabilizers, and checks the p=7 polynomial in Q[z]/Phi_7.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Callable


SCHEMA = "hcs-c44-certificate-v1"
CONTROL_BOUND = 499


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
            return n == divisor
    return True


def multiplicative_order(value: int, p: int) -> int:
    product = 1
    for exponent in range(1, p):
        product = product * value % p
        if product == 1:
            return exponent
    raise GateFailure("multiplicative order not found")


def least_primitive_root(p: int) -> int:
    for value in range(2, p):
        if multiplicative_order(value, p) == p - 1:
            return value
    raise GateFailure("primitive root not found")


def split_primes_through(bound: int) -> list[int]:
    return [p for p in range(5, bound + 1) if p % 3 == 1 and is_prime(p)]


def independently_count_phase(p: int, rho: int) -> list[int]:
    """Independent row-wise counter for the two-variable phase."""
    coefficient = (1 + rho) % p
    cubic = [(2 * pow(value, 3, p)) % p for value in range(p)]
    answer = [0] * p
    for x, x_term in enumerate(cubic):
        row = [
            (x_term + cubic[y] + coefficient * x * y) % p for y in range(p)
        ]
        for residue in row:
            answer[residue] += 1
    require(sum(answer) == p * p, "histogram mass mismatch")
    return answer


def paired(histogram: list[int]) -> list[int]:
    p = len(histogram)
    return [histogram[index] + histogram[(-index) % p] for index in range(p)]


def stabilizer(values: list[int]) -> list[int]:
    p = len(values)
    answer: list[int] = []
    for scalar in range(1, p):
        if all(values[(scalar * residue) % p] == values[residue] for residue in range(p)):
            answer.append(scalar)
    return answer


def moment(values: list[int], exponent: int) -> int:
    p = len(values)
    return sum(values[r] * pow(r, exponent, p) for r in range(p)) % p


def product_mod(integers: range, p: int) -> int:
    value = 1
    for integer in integers:
        value = value * integer % p
    return value


def witness_k0(p: int, m: int) -> int:
    fact_2m = product_mod(range(1, 2 * m + 1), p)
    fact_m = product_mod(range(1, m + 1), p)
    return 2 * fact_2m * pow(fact_m, -2, p) * pow(4, m, p) % p


def witness_k1(p: int, m: int, coefficient: int) -> int:
    fact_top = product_mod(range(1, 2 * m + 3), p)
    fact_lower = product_mod(range(1, m - 1), p)
    fact_six = product_mod(range(1, 7), p)
    return (
        2
        * fact_top
        * pow(fact_lower, -2, p)
        * pow(fact_six, -1, p)
        * pow(4, m - 2, p)
        * pow(coefficient, 6, p)
        % p
    )


def rebuild_control(p: int) -> dict[str, Any]:
    require(is_prime(p) and p % 3 == 1, "invalid split control prime")
    m = (p - 1) // 3
    generator = least_primitive_root(p)
    rho = pow(generator, m, p)
    coefficient = (1 + rho) % p
    require(rho != 1 and pow(rho, 3, p) == 1, "rho does not have order three")
    require(coefficient != 0, "one plus rho vanished")
    histogram = independently_count_phase(p, rho)
    values = paired(histogram)
    k0 = 2 * m
    direct0 = moment(values, k0)
    formula0 = witness_k0(p, m)
    require(direct0 == formula0 and direct0 != 0, "first witness mismatch")
    if p == 7:
        second = None
    else:
        k1 = k0 + 2
        direct1 = moment(values, k1)
        formula1 = witness_k1(p, m, coefficient)
        require(direct1 == formula1 and direct1 != 0, "second witness mismatch")
        second = {
            "exponent": k1,
            "direct_mod_p": direct1,
            "closed_formula_mod_p": formula1,
        }
    group = stabilizer(values)
    require(group == [1, p - 1], "paired histogram stabilizer is not plus/minus one")
    numerator = (p - 1) * values[0] - sum(values[1:])
    require(numerator % p == 0, "paired trace is not integral")
    field_trace = numerator // p
    require(histogram[0] == p - 3 and field_trace == -6, "C45 anchor mismatch")
    return {
        "prime": p,
        "m_equals_p_minus_1_over_3": m,
        "least_primitive_root": generator,
        "rho_order_3": rho,
        "one_plus_rho": coefficient,
        "phase_histogram": histogram,
        "paired_scaling_stabilizer": group,
        "first_nonzero_power_moment": {
            "exponent": k0,
            "direct_mod_p": direct0,
            "closed_formula_mod_p": formula0,
        },
        "second_nonzero_power_moment": second,
        "paired_moment_field_degree": (p - 1) // 2,
        "zero_fibre_count": histogram[0],
        "paired_moment_field_trace": field_trace,
    }


def polynomial_multiply(left: list[int], right: list[int]) -> list[int]:
    output = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            output[i + j] += a * b
    return output


def reduce_mod_phi_p(polynomial: list[int], p: int) -> list[int]:
    """Reduce low-to-high coefficients modulo Phi_p=1+...+z^(p-1)."""
    polynomial = polynomial[:]
    while len(polynomial) >= p:
        coefficient = polynomial[-1]
        degree = len(polynomial) - 1
        shift = degree - (p - 1)
        for index in range(p):
            polynomial[index + shift] -= coefficient
        while polynomial and polynomial[-1] == 0:
            polynomial.pop()
    polynomial += [0] * ((p - 1) - len(polynomial))
    return polynomial


def verify_p7_polynomial(histogram: list[int], coefficients_high: list[int]) -> None:
    require(coefficients_high == [7, 42, -168, -232], "unexpected p=7 polynomial")
    values = paired(histogram)
    # B=2P/7.  Clearing 49 from 7B^3+42B^2-168B-232 gives
    # 8P^3+168P^2-2352P-11368.
    p_poly = values
    p2 = polynomial_multiply(p_poly, p_poly)
    p3 = polynomial_multiply(p2, p_poly)
    relation = [0] * max(len(p3), len(p2), len(p_poly), 1)
    for index, value in enumerate(p3):
        relation[index] += 8 * value
    for index, value in enumerate(p2):
        relation[index] += 168 * value
    for index, value in enumerate(p_poly):
        relation[index] -= 2352 * value
    relation[0] -= 11368
    require(all(value == 0 for value in reduce_mod_phi_p(relation, 7)), "p=7 relation failed")

    # A primitive cubic is reducible over Q exactly when it has a rational
    # root.  Exhaust the rational-root candidates a/b with a|232 and b|7.
    numerators = [integer for integer in range(-232, 233) if integer and 232 % integer == 0]
    denominators = [1, 7]
    for numerator in numerators:
        for denominator in denominators:
            x = Fraction(numerator, denominator)
            value = 7 * x**3 + 42 * x**2 - 168 * x - 232
            require(value != 0, "p=7 polynomial has a rational root")


def expected_source_lock(project_root: Path) -> list[dict[str, str]]:
    source = (
        project_root.parent
        / "henon_mu3_augmented_euler_superproduct"
        / "results"
        / "c43_certificate.json"
    )
    return [
        {
            "path": "henon_dynamics/henon_mu3_augmented_euler_superproduct/results/c43_certificate.json",
            "sha256": sha256_file(source),
        }
    ]


def expected_payload(project_root: Path) -> dict[str, Any]:
    primes = split_primes_through(CONTROL_BOUND)
    controls = [rebuild_control(p) for p in primes]
    return {
        "material_passport": {
            "candidate_id": "HCS-C44",
            "project": "henon_mu3_fixed_coefficient_field_obstruction",
            "ai_assistance_disclosed": True,
            "evidence_policy": "all-prime proof plus exhaustive exact finite-field controls; no zero-table data",
        },
        "source_lock": expected_source_lock(project_root),
        "conventions": {
            "phase": "F_p(x,y)=2*x^3+2*y^3+(1+rho_p)*x*y",
            "rho": "rho_p has exact order 3 in F_p^*",
            "raw_histogram": "N_p(r)=#{(x,y) in F_p^2:F_p(x,y)=r}",
            "paired_histogram": "H_p(r)=N_p(r)+N_p(-r)",
            "paired_first_moment": "B_p=(2/p)*sum_r H_p(r)*zeta_p^r=A_p,1(psi)+A_p,1(psi^-1)",
            "split_prime_clock": "z_mathfrak_p=(Norm mathfrak_p)^(-s)=p^(-s)",
            "inert_prime_clock_if_extended": "z_mathfrak_p=(Norm mathfrak_p)^(-s)=p^(-2s); no p-average substitution",
        },
        "all_prime_theorem": {
            "scope": "every prime p=1 mod 3, p>3",
            "stabilizer": "Stab_Gal(B_p)={+1,-1}",
            "field_identity": "Q(B_p)=Q(zeta_p+zeta_p^(-1))",
            "degree": "[Q(B_p):Q]=(p-1)/2",
            "proof_witness_k0": "k0=2m; M_k0=2*(2m)!/(m!^2)*4^m mod p is nonzero",
            "proof_witness_k1": "for p>=13, k1=2m+2; M_k1=2*(2m+2)!/((m-2)!^2*6!)*4^(m-2)*(1+rho)^6 mod p is nonzero",
            "stabilizer_deduction": "a^k0=a^k1=1 gives a^2=1; for p=7, gcd(k0,p-1)=2",
            "fixed_coefficient_number_field": "IMPOSSIBLE",
        },
        "exact_controls": controls,
        "aggregate_control": {
            "bound_inclusive": CONTROL_BOUND,
            "control_primes": primes,
            "complete_split_prime_list_through_bound": True,
            "number_of_control_primes": len(primes),
            "all_stabilizers_plus_minus_one": True,
            "all_degrees_equal_p_minus_1_over_2": True,
            "all_zero_fibre_counts_equal_p_minus_3": True,
            "all_paired_field_traces_equal_minus_6": True,
            "maximum_certified_field_degree": max((p - 1) // 2 for p in primes),
        },
        "all_prime_zero_fibre_theorem": {
            "formula": "N_p(0)=p-3 for every split prime p>3",
            "paired_field_trace": "Tr_Q(B_p)/Q=-6",
            "status": "PROVED_ALL_SPLIT_PRIMES",
        },
        "p7_anchor": {
            "paired_moment_primitive_minimal_polynomial_high_to_low": [7, 42, -168, -232],
            "polynomial": "7*X^3+42*X^2-168*X-232",
            "irreducible_over_Q": True,
        },
        "decisions": {
            "conjugate_pairing_repairs_real_type": "YES_LOCALLY",
            "descent_to_one_fixed_number_field": "REFUTED_ALL_SPLIT_PRIMES",
            "uniform_fixed_rank_compatible_system": "STOP_BEFORE_HANKEL_GATE",
            "finite_tate_cm_repair": "CLOSED_BY_HCS_C42",
            "next_large_gate": "CANONICAL_RATIONAL_GALOIS_NORM_OR_TRACE_ASSEMBLY_WITH_TRUE_NORM_CLOCK",
        },
        "route_a": {
            "A1": "A1_WEAK",
            "A2": "A2_ANALYTIC_DETERMINANT",
            "A2_reason": "inherited from the C43 raw Euler germ",
            "A3": "A3_FAIL",
            "A3_reason": "paired moments have unbounded coefficient-field degree",
            "A4": "A4_NATURAL_QUANTIZATION",
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "scope": {
            "rh_proved": False,
            "hilbert_polya_operator_constructed": False,
            "global_meromorphic_continuation_claimed": False,
            "gamma_factor_claimed": False,
            "riemann_zero_data_used": False,
            "inert_prime_operator_constructed": False,
            "zero_fibre_formula_used_as_route_a_promotion": False,
        },
    }


def audit_certificate(certificate: Any, project_root: Path) -> tuple[list[dict[str, str]], bool]:
    gates: list[dict[str, str]] = []

    def run(name: str, check: Callable[[], None]) -> None:
        try:
            check()
        except GateFailure as exc:
            gates.append({"gate": name, "status": "FAIL", "detail": str(exc)})
        except Exception as exc:  # unexpected failures must be visible, never softened
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
        expected = hashlib.sha256(canonical_json(certificate["payload"])).hexdigest()
        require(certificate["payload_sha256"] == expected, "payload digest mismatch")

    def source_gate() -> None:
        require(
            strict_equal(certificate["payload"]["source_lock"], expected_source_lock(project_root)),
            "source lock mismatch",
        )

    def prime_scope_gate() -> None:
        payload = certificate["payload"]
        aggregate = payload["aggregate_control"]
        require(type(aggregate["bound_inclusive"]) is int, "bound must be an integer")
        require(aggregate["bound_inclusive"] == CONTROL_BOUND, "control bound mismatch")
        expected_primes = split_primes_through(CONTROL_BOUND)
        require(aggregate["control_primes"] == expected_primes, "control-prime ledger is incomplete")
        actual_primes = [row["prime"] for row in payload["exact_controls"]]
        require(all(type(p) is int for p in actual_primes), "prime/bool type confusion")
        require(actual_primes == expected_primes, "control rows do not match complete prime ledger")

    def histogram_gate() -> None:
        for row in certificate["payload"]["exact_controls"]:
            p = row["prime"]
            require(type(p) is int and is_prime(p), "histogram prime must be a prime integer")
            require(type(row["phase_histogram"]) is list, "histogram must be a list")
            expected = independently_count_phase(p, row["rho_order_3"])
            require(row["phase_histogram"] == expected, f"histogram mismatch at p={p}")

    def moment_gate() -> None:
        for row in certificate["payload"]["exact_controls"]:
            expected = rebuild_control(row["prime"])
            require(
                strict_equal(row["first_nonzero_power_moment"], expected["first_nonzero_power_moment"]),
                f"k0 witness mismatch at p={row['prime']}",
            )
            require(
                strict_equal(row["second_nonzero_power_moment"], expected["second_nonzero_power_moment"]),
                f"k1 witness mismatch at p={row['prime']}",
            )

    def stabilizer_degree_gate() -> None:
        for row in certificate["payload"]["exact_controls"]:
            p = row["prime"]
            require(type(p) is int and is_prime(p), "degree prime must be a prime integer")
            actual = stabilizer(paired(row["phase_histogram"]))
            require(row["paired_scaling_stabilizer"] == actual == [1, p - 1], f"stabilizer mismatch at p={p}")
            require(type(row["paired_moment_field_degree"]) is int, "degree must be integer")
            require(row["paired_moment_field_degree"] == (p - 1) // 2, f"degree mismatch at p={p}")

    def p7_gate() -> None:
        first = certificate["payload"]["exact_controls"][0]
        require(first["prime"] == 7, "first anchor is not p=7")
        anchor = certificate["payload"]["p7_anchor"]
        verify_p7_polynomial(
            first["phase_histogram"],
            anchor["paired_moment_primitive_minimal_polynomial_high_to_low"],
        )
        require(anchor["irreducible_over_Q"] is True, "irreducibility verdict changed")

    def trace_gate() -> None:
        for row in certificate["payload"]["exact_controls"]:
            p = row["prime"]
            require(type(p) is int and is_prime(p), "trace prime must be a prime integer")
            hist = row["phase_histogram"]
            values = paired(hist)
            trace = ((p - 1) * values[0] - sum(values[1:])) // p
            require(row["zero_fibre_count"] == hist[0] == p - 3, f"zero fibre mismatch at p={p}")
            require(row["paired_moment_field_trace"] == trace == -6, f"field trace mismatch at p={p}")
        theorem = certificate["payload"]["all_prime_zero_fibre_theorem"]
        require(theorem["status"] == "PROVED_ALL_SPLIT_PRIMES", "zero-fibre theorem status changed")

    def decision_gate() -> None:
        payload = certificate["payload"]
        require(payload["all_prime_theorem"]["fixed_coefficient_number_field"] == "IMPOSSIBLE", "theorem verdict changed")
        require(payload["decisions"]["descent_to_one_fixed_number_field"] == "REFUTED_ALL_SPLIT_PRIMES", "descent verdict changed")
        require(payload["decisions"]["uniform_fixed_rank_compatible_system"] == "STOP_BEFORE_HANKEL_GATE", "stop rule changed")

    def norm_clock_gate() -> None:
        conventions = certificate["payload"]["conventions"]
        require(conventions["split_prime_clock"] == "z_mathfrak_p=(Norm mathfrak_p)^(-s)=p^(-s)", "split norm clock changed")
        require(conventions["inert_prime_clock_if_extended"] == "z_mathfrak_p=(Norm mathfrak_p)^(-s)=p^(-2s); no p-average substitution", "inert norm clock changed")

    def scope_gate() -> None:
        scope = certificate["payload"]["scope"]
        require(all(type(value) is bool for value in scope.values()), "scope values must be booleans")
        require(not any(scope.values()), "a prohibited scope claim is true")
        require(certificate["payload"]["route_a"]["route_b_invocation_allowed"] is False, "Route B was improperly enabled")

    def full_payload_gate() -> None:
        require(strict_equal(certificate["payload"], expected_payload(project_root)), "full payload replay mismatch")

    run("G01_SCHEMA_AND_TYPES", schema_gate)
    run("G02_PAYLOAD_DIGEST", digest_gate)
    run("G03_SOURCE_LOCK", source_gate)
    run("G04_COMPLETE_SPLIT_PRIME_SCOPE", prime_scope_gate)
    run("G05_EXACT_PHASE_HISTOGRAMS", histogram_gate)
    run("G06_NONZERO_MOMENT_WITNESSES", moment_gate)
    run("G07_STABILIZER_AND_FIELD_DEGREE", stabilizer_degree_gate)
    run("G08_P7_MINIMAL_POLYNOMIAL", p7_gate)
    run("G09_ZERO_FIBRE_AND_FIELD_TRACE", trace_gate)
    run("G10_FIXED_FIELD_STOP_DECISION", decision_gate)
    run("G11_TRUE_NORM_CLOCK_AND_SCOPE", lambda: (norm_clock_gate(), scope_gate()))
    run("G12_FULL_PAYLOAD_REPLAY", full_payload_gate)
    passed = all(row["status"] == "PASS" for row in gates)
    return gates, passed


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
        "schema": "hcs-c44-independent-check-v1",
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
