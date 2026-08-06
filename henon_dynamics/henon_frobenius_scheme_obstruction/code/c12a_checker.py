#!/usr/bin/env python3
"""Independent checker for the HCS-C12A exact certificate.

This module does not import c12a_producer.  Finite fields are implemented as
explicit polynomial quotients and the period-five marker is recomputed from
the scalar recurrence on the reversor line.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import itertools
import json
from pathlib import Path
from typing import Iterable

import sympy as sp


LEDGER: dict[tuple[int, int], tuple[int, ...]] = {
    (3, 2): (1, 0),
    (3, 3): (1, 0, 2),
    (3, 4): (1, 0, 1, 1),
    (5, 2): (1, 1),
    (5, 3): (1, 0, 1),
    (5, 4): (1, 0, 1, 1),
    (7, 2): (1, 0),
    (7, 3): (1, 0, 1),
    (7, 4): (1, 0, 0, 1),
    (11, 2): (1, 0),
    (11, 3): (1, 0, 4),
    (11, 4): (1, 0, 0, 4),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


class FiniteField:
    """Small exact F_p[t]/(m) implementation for the frozen grid."""

    def __init__(self, p: int, degree: int):
        self.p = p
        self.degree = degree
        self.modulus = LEDGER.get((p, degree)) if degree > 1 else None
        if degree > 1 and self.modulus is None:
            raise KeyError((p, degree))
        self.zero = (0,) * degree
        self.one = (1,) + (0,) * (degree - 1)
        self.size = p**degree

    def elements(self) -> Iterable[tuple[int, ...]]:
        return itertools.product(range(self.p), repeat=self.degree)

    def scalar(self, value: int) -> tuple[int, ...]:
        return (value % self.p,) + (0,) * (self.degree - 1)

    def add(self, left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
        return tuple((x + y) % self.p for x, y in zip(left, right))

    def neg(self, value: tuple[int, ...]) -> tuple[int, ...]:
        return tuple((-x) % self.p for x in value)

    def sub(self, left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
        return self.add(left, self.neg(right))

    def mul(self, left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
        if self.degree == 1:
            return ((left[0] * right[0]) % self.p,)
        work = [0] * (2 * self.degree - 1)
        for i, x in enumerate(left):
            for j, y in enumerate(right):
                work[i + j] = (work[i + j] + x * y) % self.p
        assert self.modulus is not None
        for power in range(2 * self.degree - 2, self.degree - 1, -1):
            coefficient = work[power] % self.p
            if coefficient:
                for i, modulus_coefficient in enumerate(self.modulus):
                    target = power - self.degree + i
                    work[target] = (work[target] - coefficient * modulus_coefficient) % self.p
        return tuple(value % self.p for value in work[: self.degree])

    def pow(self, base: tuple[int, ...], exponent: int) -> tuple[int, ...]:
        result = self.one
        value = base
        while exponent:
            if exponent & 1:
                result = self.mul(result, value)
            value = self.mul(value, value)
            exponent >>= 1
        return result

    def inv(self, value: tuple[int, ...]) -> tuple[int, ...]:
        if value == self.zero:
            raise ZeroDivisionError
        return self.pow(value, self.size - 2)

    def verify_field(self) -> bool:
        # A finite commutative ring is a field iff every nonzero element is a
        # unit.  The frozen sizes are small enough to check this directly.
        return all(value == self.zero or self.pow(value, self.size - 1) == self.one for value in self.elements())


def count_n1_n2(field: FiniteField, n: int) -> tuple[int, int]:
    a = field.scalar(6)
    one = field.one
    two = field.scalar(2)
    four = field.scalar(4)
    a2 = field.mul(a, a)
    count = 0
    singular = 0
    if n == 1:
        for q in field.elements():
            equation = field.sub(field.add(field.mul(a, field.mul(q, q)), field.mul(two, q)), one)
            if equation == field.zero:
                count += 1
                jacobian = field.add(field.mul(field.mul(two, a), q), two)
                singular += jacobian == field.zero
        return count, singular
    if n != 2:
        raise ValueError(n)
    inverse_two = field.inv(two)
    for q0 in field.elements():
        q1 = field.mul(field.sub(one, field.mul(a, field.mul(q0, q0))), inverse_two)
        equation = field.sub(field.add(field.mul(a, field.mul(q1, q1)), field.mul(two, q0)), one)
        if equation == field.zero:
            count += 1
            jacobian = field.sub(field.mul(field.mul(four, a2), field.mul(q0, q1)), four)
            singular += jacobian == field.zero
    return count, singular


def count_h0_four_fixed(field: FiniteField) -> int:
    """Directly count fixed points of the fourth degree-drop iterate."""
    one = field.one
    count = 0
    elements = tuple(field.elements())
    for q in elements:
        for p_coordinate in elements:
            x, y = q, p_coordinate
            for _ in range(4):
                x, y = field.sub(one, y), x
            count += x == q and y == p_coordinate
    return count


def ramified_extra_length(p: int, n: int) -> int:
    """Compute the support-to-length correction from exact factor exponents."""
    if p != 7:
        return 0
    z = sp.symbols("z")

    def repeated_degree(poly: sp.Expr) -> int:
        factors = sp.factor_list(sp.Poly(poly, z, modulus=p))[1]
        return sum(int(sp.degree(factor, z)) * (exponent - 1) for factor, exponent in factors)

    fixed_extra = repeated_degree(z**2 - 7)
    if n == 1:
        return fixed_extra
    if n == 2:
        primitive_extra = repeated_degree(z**2 - 3)
        return fixed_extra + primitive_extra
    raise ValueError(n)


ROW_FIELDS = (
    "a",
    "p",
    "r",
    "n",
    "prime_status",
    "support_count",
    "multiplicity_weighted_count",
    "fiber_scheme_length",
    "uniform_quadratic_length",
    "rational_singular_support_count",
)


def expected_row_keys() -> set[tuple[int, int, int]]:
    keys = {(p, r, n) for p in (3, 5, 7, 11) for r in range(1, 5) for n in (1, 2)}
    keys.update((3, r, 4) for r in range(1, 5))
    return keys


def expected_metadata(p: int, n: int) -> dict[str, object]:
    if p in (5, 11):
        return {
            "prime_status": "ETALE_GOOD",
            "fiber_scheme_length": 2**n,
            "uniform_quadratic_length": 2**n,
        }
    if p == 7:
        return {
            "prime_status": "DEGREE_GOOD_NONREDUCED",
            "fiber_scheme_length": 2**n,
            "uniform_quadratic_length": 2**n,
        }
    if n in (1, 2):
        return {
            "prime_status": "DEGREE_DROP",
            "fiber_scheme_length": 1,
            "uniform_quadratic_length": None,
        }
    return {
        "prime_status": "DEGREE_DROP_POSITIVE_DIMENSIONAL",
        "fiber_scheme_length": None,
        "uniform_quadratic_length": None,
    }


def csv_matches_rows(path: Path, rows: list[dict[str, object]]) -> bool:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if tuple(reader.fieldnames or ()) != ROW_FIELDS:
            return False
        csv_rows = list(reader)
    if len(csv_rows) != len(rows):
        return False
    for csv_row, json_row in zip(csv_rows, rows):
        if set(json_row) != set(ROW_FIELDS):
            return False
        for field in ROW_FIELDS:
            expected = "" if json_row[field] is None else str(json_row[field])
            if csv_row[field] != expected:
                return False
    return True


def independent_period_five() -> dict[str, object]:
    a, q, x = sp.symbols("a q x")
    previous, current = q, q
    values = [current]
    for _ in range(5):
        following = sp.expand(1 - a * current**2 - previous)
        previous, current = current, following
        values.append(current)
    # After five Hénon steps the state is (x_5,x_4); both must equal q.
    domain = sp.QQ.frac_field(a)
    equation5 = sp.Poly(values[5] - q, q, domain=domain)
    equation4 = sp.Poly(values[4] - q, q, domain=domain)
    common = sp.monic(sp.gcd(equation5, equation4)).as_expr()
    marker = sp.factor(sp.cancel(common * a**7 / (a * q**2 + 2 * q - 1)))
    marker6 = sp.Poly(sp.expand(marker.subs(a, 6)), q, domain=sp.ZZ)
    scaled = sp.Poly(sp.expand(marker6.as_expr().subs(q, x / 6)), x, domain=sp.QQ)
    discriminant = int(sp.discriminant(marker6.as_expr(), q))

    def integral_coefficients(poly: sp.Poly) -> list[int]:
        coefficients = poly.all_coeffs()
        if any(sp.denom(coefficient) != 1 for coefficient in coefficients):
            raise AssertionError(f"nonintegral coefficient in {poly.as_expr()}")
        return [int(coefficient) for coefficient in coefficients]

    def degrees(prime: int) -> list[int]:
        factors = sp.factor_list(sp.Poly(marker6.as_expr(), q, modulus=prime))[1]
        return sorted(
            [int(sp.degree(factor, q)) for factor, exponent in factors for _ in range(exponent)],
            reverse=True,
        )

    return {
        "generic_marker": sp.sstr(marker),
        "a6_q_coefficients": integral_coefficients(marker6),
        "scaled_x_coefficients": integral_coefficients(scaled),
        "discriminant": discriminant,
        "factor_degrees": {str(prime): degrees(prime) for prime in (37, 5, 157)},
    }


def independent_joint_control() -> dict[str, object]:
    states = tuple((epsilon, i) for epsilon in (-1, 1) for i in range(5))

    def h(state: tuple[int, int]) -> tuple[int, int]:
        epsilon, i = state
        return epsilon, (i + 1) % 5

    def h_inverse(state: tuple[int, int]) -> tuple[int, int]:
        epsilon, i = state
        return epsilon, (i - 1) % 5

    def reversor(state: tuple[int, int]) -> tuple[int, int]:
        epsilon, i = state
        return -epsilon, (-i) % 5

    def frobenius(rotation: int, state: tuple[int, int]) -> tuple[int, int]:
        epsilon, i = state
        return epsilon, (i + epsilon * rotation) % 5

    def fixed(rotation: int, r: int, s: int) -> int:
        return sum((i + epsilon * rotation * r - s) % 5 == i for epsilon, i in states)

    ordinary1 = [fixed(1, r, 0) for r in range(1, 11)]
    ordinary2 = [fixed(2, r, 0) for r in range(1, 11)]
    joint1 = [[fixed(1, r, s) for s in range(5)] for r in range(1, 6)]
    joint2 = [[fixed(2, r, s) for s in range(5)] for r in range(1, 6)]
    rhr_pass = all(reversor(h(reversor(state))) == h_inverse(state) for state in states)
    commute_pass = all(
        frobenius(rotation, h(state)) == h(frobenius(rotation, state))
        and frobenius(rotation, reversor(state)) == reversor(frobenius(rotation, state))
        for rotation in (1, 2)
        for state in states
    )
    return {
        "ordinary_sequences_equal": ordinary1 == ordinary2,
        "joint_characters_different": joint1 != joint2,
        "ordinary_F_c1": ordinary1,
        "ordinary_F_c2": ordinary2,
        "joint_F_c1": joint1,
        "joint_F_c2": joint2,
        "RHR_equals_H_inverse": rhr_pass,
        "F_commutes_with_H_and_R": commute_pass,
        "reversal_symmetry": all(
            fixed(c, r, s) == fixed(c, r, -s)
            for c in (1, 2) for r in range(1, 6) for s in range(5)
        ),
    }


def main() -> None:
    project = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--certificate", type=Path, default=project / "results" / "c12a_certificate.json")
    parser.add_argument("--counts-csv", type=Path, default=project / "results" / "c12a_low_period_counts.csv")
    parser.add_argument("--output", type=Path, default=project / "results" / "c12a_independent_check.json")
    args = parser.parse_args()

    with args.certificate.open(encoding="utf-8") as handle:
        certificate = json.load(handle)

    expected_top_keys = {
        "schema_version",
        "candidate_id",
        "map",
        "parameter_provenance",
        "chronology",
        "symbolic",
        "low_period_rows",
        "local_zeta_theorem",
        "joint_action_control",
        "period_five",
        "route_decision",
        "frozen_inputs",
    }
    top_schema_pass = set(certificate) == expected_top_keys
    top_metadata_pass = (
        certificate.get("schema_version") == "HCS-C12A-1"
        and certificate.get("candidate_id") == "HCS-C12A"
        and certificate.get("map") == "H_a(q,p)=(1-a*q^2-p,q)"
        and certificate.get("parameter_provenance")
        == "a=6 is an integral arithmetic specialization of the Paper-5 family, not a fitted critical parameter"
        and certificate.get("chronology")
        == {"r": "Frobenius extension degree", "n": "Hénon iterate", "merged": False}
    )
    rows = certificate.get("low_period_rows", [])
    actual_keys = [(int(row["p"]), int(row["r"]), int(row["n"])) for row in rows]
    row_schema_pass = (
        len(rows) == 36
        and len(set(actual_keys)) == 36
        and set(actual_keys) == expected_row_keys()
        and all(set(row) == set(ROW_FIELDS) and row["a"] == 6 for row in rows)
    )
    csv_pass = csv_matches_rows(args.counts_csv, rows) if row_schema_pass else False

    frozen = certificate.get("frozen_inputs", {})
    frozen_hash_pass = (
        set(frozen)
        == {
            "experiment_plan_sha256",
            "protocol_sha256",
            "counts_csv_sha256",
            "producer_sha256",
        }
        and frozen.get("experiment_plan_sha256") == sha256(project / "EXPERIMENT_PLAN.md")
        and frozen.get("protocol_sha256") == sha256(project / "code" / "PROTOCOL.md")
        and frozen.get("counts_csv_sha256") == sha256(args.counts_csv)
        and frozen.get("producer_sha256") == sha256(project / "code" / "c12a_producer.py")
    )

    symbolic = certificate.get("symbolic", {})
    symbolic_pass = (
        symbolic.get("D_a_1") == "-4*(a + 1)"
        and symbolic.get("D_a_2") == "256*(a - 3)**3*(a + 1)"
        and all(
            symbolic.get(key) is True
            for key in (
                "D_a_1_pass",
                "D_a_2_pass",
                "difference_factorization_pass",
                "fixed_branch_residual_pass",
                "primitive_branch_residual_pass",
                "n1_iterate_cyclic_ideal_pass",
                "n2_iterate_cyclic_ideal_pass",
                "generic_crt_comaximal_pass",
            )
        )
        and symbolic.get("period_two_splitting_scope")
        == "Q(A); equivalently after excluding the branch collision A=3"
        and symbolic.get("standard_monomial_count_formula") == "2^n"
    )
    local_zeta = certificate.get("local_zeta_theorem", {})
    local_zeta_schema_pass = local_zeta == {
        "formula": "Z_{a,p,n}(u)=det(I-u*Frob_p | Q_l[S_{a,p,n}])^-1",
        "scope": "finite_zero_dimensional_fibers_only",
        "eigenvalue_class": "roots_of_unity",
        "cohomological_degrees": [0],
        "nilpotents_visible": False,
        "length_weighted_count_definition": "sum of geometric local lengths over F_{p^r}-rational support points",
        "status": "PROVED_GENERAL_FINITE_SCHEME_FACT",
    }
    decision_schema_pass = certificate.get("route_decision") == {
        "registered_candidate": "C12A_NO_GO_ZERO_DIMENSIONAL_FROBENIUS_COLLAPSE",
        "period_five_reframe": "C12B_N5_PRIOR_WORK_COLLISION",
        "route_b_authorized": False,
    }

    ledger_pass: dict[str, bool] = {}
    count_checks: list[dict[str, object]] = []
    all_pass = all(
        (
            top_schema_pass,
            top_metadata_pass,
            row_schema_pass,
            csv_pass,
            frozen_hash_pass,
            symbolic_pass,
            local_zeta_schema_pass,
            decision_schema_pass,
        )
    )
    for p in (3, 5, 7, 11):
        for r in range(1, 5):
            field = FiniteField(p, r)
            field_pass = field.verify_field()
            ledger_pass[f"{p}^{r}"] = field_pass
            all_pass &= field_pass

    h0_four_identity_checks: dict[str, bool] = {}
    for row in rows:
        p, r, n = int(row["p"]), int(row["r"]), int(row["n"])
        field = FiniteField(p, r)
        if n in (1, 2):
            support, singular = count_n1_n2(field, n)
            weighted = support + ramified_extra_length(p, n)
        else:
            support = count_h0_four_fixed(field)
            h0_four_identity_checks[f"3^{r}"] = support == field.size**2
            singular, weighted = None, None
        metadata = expected_metadata(p, n)
        passed = (
            support == row["support_count"]
            and singular == row["rational_singular_support_count"]
            and weighted == row["multiplicity_weighted_count"]
            and row["prime_status"] == metadata["prime_status"]
            and row["fiber_scheme_length"] == metadata["fiber_scheme_length"]
            and row["uniform_quadratic_length"] == metadata["uniform_quadratic_length"]
        )
        all_pass &= passed
        count_checks.append(
            {
                "p": p,
                "r": r,
                "n": n,
                "support": support,
                "singular": singular,
                "weighted": weighted,
                "expected_metadata": metadata,
                "pass": passed,
            }
        )

    period5 = independent_period_five()
    producer5 = certificate["period_five"]
    expected_q_coefficients = [46656, 15552, -20736, -4752, 3060, 360, -151]
    expected_x_coefficients = [1, 2, -16, -22, 85, 60, -151]
    expected_discriminant = 2**36 * 3**30 * 31 * 241 * 389
    expected_factor_degrees = {"37": [6], "5": [5, 1], "157": [2, 1, 1, 1, 1]}
    period5_pass = (
        period5["generic_marker"] == producer5["generic_reversor_marker"]
        and period5["a6_q_coefficients"] == expected_q_coefficients
        and producer5["a6_q_coefficients"] == expected_q_coefficients
        and period5["scaled_x_coefficients"] == expected_x_coefficients
        and producer5["scaled_x_coefficients"] == expected_x_coefficients
        and producer5["published_brison_gallas_Z_coefficients"] == expected_x_coefficients
        and period5["discriminant"] == expected_discriminant
        and producer5["discriminant"] == expected_discriminant
        and period5["factor_degrees"] == expected_factor_degrees
        and producer5["factor_degrees"] == expected_factor_degrees
        and producer5["published_collision_pass"] is True
        and producer5["discriminant_pass"] is True
        and producer5["factor_degrees_pass"] is True
        and producer5["galois_group_certificate"]["pass"] is True
        and producer5["galois_group_certificate"]["conclusion"] == "S6"
        and producer5["novelty_status"] == "C12B_N5_PRIOR_WORK_COLLISION"
    )
    all_pass &= period5_pass

    joint = independent_joint_control()
    producer_joint = certificate["joint_action_control"]
    joint_pass = (
        joint["ordinary_sequences_equal"]
        and joint["joint_characters_different"]
        and joint["reversal_symmetry"]
        and joint["RHR_equals_H_inverse"]
        and joint["F_commutes_with_H_and_R"]
        and producer_joint["frobenius_convention"] == "arithmetic"
        and joint["ordinary_F_c1"] == producer_joint["ordinary_sequences"]["F_c1"]
        and joint["ordinary_F_c2"] == producer_joint["ordinary_sequences"]["F_c2"]
        and joint["joint_F_c1"] == producer_joint["joint_characters"]["F_c1"]
        and joint["joint_F_c2"] == producer_joint["joint_characters"]["F_c2"]
        and producer_joint["ordinary_collision_pass"] is True
        and producer_joint["joint_separation_pass"] is True
        and producer_joint["reversal_symmetry_pass"] is True
        and producer_joint["matched_reversibility"]
        == {
            "state_space": "{+1,-1} x Z/5Z",
            "H": "(epsilon,i)->(epsilon,i+1)",
            "R": "(epsilon,i)->(-epsilon,-i)",
            "F_c": "(epsilon,i)->(epsilon,i+epsilon*c)",
            "RHR_equals_H_inverse": True,
            "F_commutes_with_H_and_R": True,
        }
        and producer_joint["smallest_witness"]
        == {"r": 1, "s": 1, "trace_F_c1": 5, "trace_F_c2": 0}
    )
    all_pass &= joint_pass

    result = {
        "schema_version": "HCS-C12A-independent-1",
        "checker_sha256": sha256(Path(__file__).resolve()),
        "certificate_sha256": sha256(args.certificate),
        "top_schema_pass": top_schema_pass,
        "top_metadata_pass": top_metadata_pass,
        "row_schema_pass": row_schema_pass,
        "csv_sha256": sha256(args.counts_csv),
        "csv_canonical_match_pass": csv_pass,
        "frozen_hash_pass": frozen_hash_pass,
        "symbolic_pass": symbolic_pass,
        "local_zeta_schema_pass": local_zeta_schema_pass,
        "decision_schema_pass": decision_schema_pass,
        "irreducible_ledger_checks": ledger_pass,
        "h0_four_identity_checks": h0_four_identity_checks,
        "count_checks": count_checks,
        "period_five": period5,
        "period_five_pass": period5_pass,
        "joint_control": joint,
        "joint_control_pass": joint_pass,
        "all_pass": all_pass,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    print(json.dumps({"output": str(args.output), "sha256": sha256(args.output), "all_pass": all_pass}, indent=2))
    if not all_pass:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
