#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C156."""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
import json
from math import gcd, lcm
from pathlib import Path


def canonical_payload_hash(data):
    work = dict(data)
    work.pop("payload_sha256", None)
    raw = json.dumps(work, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def multiply(left, right):
    return [[sum(left[i][k] * right[k][j] for k in range(2))
             for j in range(2)] for i in range(2)]


def power_by_iteration(matrix, n):
    out = [[1, 0], [0, 1]]
    for _ in range(n):
        out = multiply(out, matrix)
    return out


def determinant(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def bezout(a, b):
    if b == 0:
        return abs(a), 1 if a >= 0 else -1, 0
    quotient, remainder = divmod(a, b)
    g, s, t = bezout(b, remainder)
    return g, t, s - quotient * t


def hnf_and_reduce(matrix):
    order = abs(determinant(matrix))
    bottom, s, t = bezout(matrix[1][0], matrix[1][1])
    top = order // bottom
    skew = (s * matrix[0][0] + t * matrix[0][1]) % top
    return [[top, skew], [0, bottom]]


def reduce_shift(shift, hnf):
    first, second = shift
    quotient = second // hnf[1][1]
    return ((first - quotient * hnf[0][1]) % hnf[0][0], second % hnf[1][1])


def fib(n):
    values = [0, 1]
    while len(values) <= n:
        values.append(values[-1] + values[-2])
    return values[n]


def luc(n):
    return 2 if n == 0 else fib(n - 1) + fib(n + 1)


def factors(value):
    result = []
    candidate = 2
    while candidate * candidate <= value:
        count = 0
        while value % candidate == 0:
            value //= candidate
            count += 1
        if count:
            result.append((candidate, count))
        candidate += 1
    if value > 1:
        result.append((value, 1))
    return result


def valuation(value, prime):
    result = 0
    while value % prime == 0:
        value //= prime
        result += 1
    return result


def q_one(value):
    x, y = value
    return x * (x - 1) + x * y + Fraction(y * (y - 1), 2)


def qn_direct_integer(n, value):
    x, y = value
    total = Fraction(0)
    for _ in range(n):
        total += q_one((x, y))
        x, y = 2 * x + y, x + y
    return total


def independently_solve_coefficients(n):
    p10 = qn_direct_integer(n, (1, 0))
    p20 = qn_direct_integer(n, (2, 0))
    p01 = qn_direct_integer(n, (0, 1))
    p02 = qn_direct_integer(n, (0, 2))
    a = (p20 - 2 * p10) / 2
    d = p10 - a
    c = (p02 - 2 * p01) / 2
    e = p01 - c
    b = qn_direct_integer(n, (1, 1)) - a - c - d - e
    return a, b, c, d, e


def direct_rotation(matrix, shift, n):
    """Iterate q on integer numerators over the fixed denominator det(M)."""
    first, second = shift
    denominator = determinant(matrix)
    xnum = matrix[1][1] * first - matrix[0][1] * second
    ynum = -matrix[1][0] * first + matrix[0][0] * second
    total_numerator = 0
    for _ in range(n):
        total_numerator += (2 * xnum * xnum + 2 * xnum * ynum + ynum * ynum
                            - 2 * xnum * denominator - ynum * denominator)
        xnum, ynum = 2 * xnum + ynum, xnum + ynum
    initial_ynum = -matrix[1][0] * first + matrix[0][0] * second
    total_numerator -= 2 * first * initial_ynum * denominator
    return Fraction(total_numerator, 2 * denominator * denominator) % 1


def parse(value):
    return Fraction(str(value))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence", nargs="?", type=Path,
                        default=Path(__file__).resolve().parents[1] /
                        "results/c156_primary_module_evidence.json")
    parser.add_argument("--quick", action="store_true",
                        help="skip full local re-enumeration; retain all closure checks")
    args = parser.parse_args()
    data = json.loads(args.evidence.read_text())
    checks = 0

    def check(condition, message):
        nonlocal checks
        checks += 1
        if not condition:
            raise AssertionError(message)

    expected_top = {
        "schema", "candidate_id", "evaluation_date", "scope_literal", "source_commit",
        "source_lock", "matrix_power_factorization", "canonical_cocycle_and_denominator",
        "primary_decomposition_theorem", "iterate_ledger", "formal_lift_hint", "route_a",
        "claim_boundary", "payload_sha256",
    }
    check(set(data) == expected_top, "top-level closure")
    check(data["schema"] == "hcs-c156-heisenberg-primary-quadratic-module-evidence-v1", "schema")
    check(data["candidate_id"] == "HCS-C156", "candidate")
    check(data["evaluation_date"] == "2026-08-25", "date")
    check(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    check(data["source_commit"] == "506dead810d67fa58fa7c42b2d9a09bfae161059", "commit")
    check(data["payload_sha256"] == canonical_payload_hash(data), "payload hash")
    lock = data["source_lock"]
    check(lock["matrix_A"] == [[2, 1], [1, 1]], "matrix lock")
    check(lock["cutoff"] == {"exact_primary_component_enumeration": 14}, "cutoff")
    check(lock["precision"] == "exact integer and rational arithmetic", "precision")
    check(lock["upstream_c151_evidence_sha256"] ==
          "5fe26d210e6c848789ee769f9f0fbaa0ba67baef06cb93cb3d2f2d403ef18419", "upstream")
    check("arithmetic local or Euler factors" in lock["forbidden_data"], "forbidden data")

    factorization = data["matrix_power_factorization"]
    check(factorization["all_iterates"] is True, "all-n factorization")
    check(factorization["odd_smith_type"] == "Z/L_n Z times Z/L_n Z", "odd Smith")
    check(factorization["even_smith_type"] == "Z/F_n Z times Z/(5F_n) Z", "even Smith")
    denominator_theorem = data["canonical_cocycle_and_denominator"]
    check(denominator_theorem["sharpness_claimed_all_n"] is False, "no all-n sharpness")
    check(denominator_theorem["uniform_bound"].startswith("h_n*rho_n is integral"), "uniform denominator")
    check(denominator_theorem["actual_iterate"].startswith("q_n=q_(A^n)+ell_n"), "linear drift retained")
    primary_theorem = data["primary_decomposition_theorem"]
    check(primary_theorem["orthogonal_split"].startswith("G_n is the orthogonal direct sum"), "orthogonal theorem")
    check(primary_theorem["polarization"] ==
          "beta_n([m],[u])=v_1*u_2-u_1*v_2+m_1*u_2 mod 1 for v=M^-1*m and w=M^-1*u",
          "polarization theorem")
    check(primary_theorem["terminology_boundary"].startswith("primary means group-theoretic"), "terminology")

    A = [[2, 1], [1, 1]]
    expected_counts = [1, 1, 4, 1, 21, 4, 57, 1, 148, 105, 397, 144, 1041, 57]
    observed_counts = []
    for n, row in enumerate(data["iterate_ledger"], 1):
        power = power_by_iteration(A, n)
        matrix = [[power[0][0] - 1, power[0][1]], [power[1][0], power[1][1] - 1]]
        order = abs(determinant(matrix))
        hnf = hnf_and_reduce(matrix)
        if n % 2:
            scalar = luc(n)
            cofactor = [[fib(n + 1), fib(n)], [fib(n), fib(n - 1)]]
            branch = "ODD_LUCAS_UNIMODULAR"
            cofactor_det = -1
            smith = [scalar, scalar]
            exponent = scalar
        else:
            scalar = fib(n)
            cofactor = [[luc(n + 1), luc(n)], [luc(n), luc(n - 1)]]
            branch = "EVEN_FIBONACCI_DET_MINUS_FIVE"
            cofactor_det = -5
            smith = [scalar, 5 * scalar]
            exponent = 5 * scalar
        check(row["n"] == n, f"n {n}")
        check(row["A_power"] == power, f"power {n}")
        check(row["M=A_power-I"] == matrix, f"M {n}")
        check(row["factorization_branch"] == branch, f"branch {n}")
        check(row["factor_scalar"] == scalar, f"scalar {n}")
        check(row["cofactor_matrix"] == cofactor, f"cofactor {n}")
        check(row["cofactor_determinant"] == determinant(cofactor) == cofactor_det, f"cofactor det {n}")
        check([[scalar * entry for entry in vector] for vector in cofactor] == matrix, f"factorization {n}")
        first_smith = gcd(gcd(abs(matrix[0][0]), abs(matrix[0][1])),
                          gcd(abs(matrix[1][0]), abs(matrix[1][1])))
        check(row["smith_invariants"] == smith == [first_smith, order // first_smith], f"Smith {n}")
        check(row["horizontal_group_order"] == order == smith[0] * smith[1], f"order {n}")
        check(row["horizontal_group_exponent_h"] == exponent == smith[1], f"exponent {n}")
        check(row["column_hnf"] == hnf, f"HNF {n}")

        solved = independently_solve_coefficients(n)
        a, b = power[0]
        c, d = power[1]
        canonical = (Fraction(a * c, 2), Fraction(b * c), Fraction(b * d, 2),
                     Fraction(-a * c, 2), Fraction(-b * d, 2))
        drift = tuple(left - right for left, right in zip(solved, canonical))
        frozen_canonical = [parse(value) for value in row["canonical_q_B_coefficients"]]
        check(frozen_canonical == list(canonical), f"canonical qB {n}")
        check(drift[:3] == (0, 0, 0), f"linear drift degree {n}")
        check(row["iterate_linear_drift"] == [int(drift[3]), int(drift[4])], f"drift {n}")

        # A nontrivial per-iterate sentinel checks the stated polarization
        # formula against the definition rho(x+y)-rho(x)-rho(y).
        left = reduce_shift((1, 0), hnf)
        right = reduce_shift((0, 1), hnf)
        total = reduce_shift((left[0] + right[0], left[1] + right[1]), hnf)
        denominator = determinant(matrix)
        v = (Fraction(matrix[1][1] * left[0] - matrix[0][1] * left[1], denominator),
             Fraction(-matrix[1][0] * left[0] + matrix[0][0] * left[1], denominator))
        beta_formula = (v[0] * right[1] - right[0] * v[1] + left[0] * right[1]) % 1
        beta_direct = (direct_rotation(matrix, total, n) - direct_rotation(matrix, left, n)
                       - direct_rotation(matrix, right, n)) % 1
        check(beta_direct == beta_formula, f"polarization sentinel {n}")

        expected_primes = factors(exponent)
        check([component["prime"] for component in row["primary_components"]] ==
              [prime for prime, _ in expected_primes], f"primary primes {n}")
        product_zero = 1
        component_denominator = 1
        component_sets = []
        for component, (prime, exponent_power) in zip(row["primary_components"], expected_primes):
            prime_power = prime ** exponent_power
            complementary = exponent // prime_power
            idempotent = 1 if complementary == 1 else (
                complementary * pow(complementary, -1, prime_power)) % exponent
            group_order = prime ** sum(valuation(invariant, prime) for invariant in smith)
            frozen_hist = {parse(item["rotation"]): item["multiplicity"]
                           for item in component["histogram"]}
            check(len(frozen_hist) == len(component["histogram"]), f"unique histogram {n},{prime}")
            check(all(multiplicity > 0 for multiplicity in frozen_hist.values()), f"positive mass {n},{prime}")
            frozen_lcm = 1
            for residue in frozen_hist:
                frozen_lcm = lcm(frozen_lcm, residue.denominator)
                check((residue * prime_power).denominator == 1, f"local denominator {n},{prime}")
            check(component["prime"] == prime, f"prime {n},{prime}")
            check(component["exponent_power"] == exponent_power, f"valuation {n},{prime}")
            check(component["cyclic_projector_order"] == prime_power, f"projector order {n},{prime}")
            check(component["crt_idempotent_mod_h"] == idempotent, f"idempotent {n},{prime}")
            check(component["group_order"] == group_order, f"local group order {n},{prime}")
            check(component["enumerated_element_count"] == group_order, f"element count {n},{prime}")
            check(sum(frozen_hist.values()) == group_order, f"local mass {n},{prime}")
            check(component["rotation_support_size"] == len(frozen_hist), f"support {n},{prime}")
            check(component["observed_denominator_lcm"] == frozen_lcm, f"local lcm {n},{prime}")
            check(component["zero_count"] == frozen_hist.get(Fraction(0), 0), f"zero {n},{prime}")
            check(component["root_of_unity_projector_numerator"] ==
                  prime_power * component["zero_count"], f"projector numerator {n},{prime}")
            product_zero *= component["zero_count"]
            component_denominator = lcm(component_denominator, frozen_lcm)

            if not args.quick:
                shifts = sorted({
                    reduce_shift((idempotent * first, idempotent * second), hnf)
                    for first in range(prime_power) for second in range(prime_power)
                })
                check(len(shifts) == group_order, f"independent subgroup size {n},{prime}")
                exact_hist = Counter()
                for shift in shifts:
                    residue = direct_rotation(matrix, shift, n)
                    check((residue * prime_power).denominator == 1,
                          f"direct p-primary denominator {n},{prime},{shift}")
                    exact_hist[residue] += 1
                check(exact_hist == frozen_hist, f"independent histogram {n},{prime}")
                component_sets.append((prime, shifts))

        if order == 1:
            product_zero = component_denominator = 1
        check(row["fixed_circle_component_count"] == product_zero, f"zero product {n}")
        check(row["global_denominator_lcm_from_components"] == component_denominator, f"global lcm {n}")
        check(row["zero_count_product_verified"] is True, f"product flag {n}")
        if n >= 2:
            check(component_denominator == exponent, f"finite sharpness {n}")

        if not args.quick:
            orthogonality_checks = 0
            for left_index, (_, left_set) in enumerate(component_sets):
                for _, right_set in component_sets[left_index + 1:]:
                    for left in left_set:
                        left_rho = direct_rotation(matrix, left, n)
                        for right in right_set:
                            total = reduce_shift((left[0] + right[0], left[1] + right[1]), hnf)
                            polarization = (direct_rotation(matrix, total, n) - left_rho
                                            - direct_rotation(matrix, right, n)) % 1
                            check(polarization == 0, f"orthogonality {n},{left},{right}")
                            orthogonality_checks += 1
            check(row["orthogonality_pair_checks"] == orthogonality_checks,
                  f"orthogonality receipt {n}")
        else:
            group_orders = [component["group_order"] for component in row["primary_components"]]
            expected_pairs = sum(group_orders[left] * group_orders[right]
                                 for left in range(len(group_orders))
                                 for right in range(left + 1, len(group_orders)))
            check(row["orthogonality_pair_checks"] == expected_pairs,
                  f"orthogonality count {n}")
        observed_counts.append(product_zero)

    check(observed_counts == expected_counts, "certified zero-count sequence")
    check(data["formal_lift_hint"] == {
        "operator": "the frozen Haar Koopman unitary from C151",
        "unitary": True,
        "primary_projector_is_operator_trace_formula": False,
        "status": "FORMAL_HINT_ONLY",
    }, "formal lift")
    check(data["route_a"] == {
        "tuple": ["A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
        "overall": "ROUTE_A_EXPLORATORY", "route_b_invocation_allowed": False,
    }, "Route A tuple")
    check(all(value is False for value in data["claim_boundary"].values()), "claim boundary")
    print(json.dumps({
        "status": "C156_CHECKER_PASS",
        "mode": "quick" if args.quick else "full",
        "assertions": checks,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
