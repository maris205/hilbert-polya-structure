#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C151."""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
import json
from math import lcm
from pathlib import Path


def canon_hash(data):
    work = dict(data)
    work.pop("payload_sha256", None)
    return sha256(json.dumps(work, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def multiply(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def power(a, n):
    out = [[1, 0], [0, 1]]
    for _ in range(n):
        out = multiply(out, a)
    return out


def det(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def bezout(a, b):
    def rec(x, y):
        if y == 0:
            return x, 1, 0
        g, s, t = rec(y, x % y)
        return g, t, s - (x // y) * t
    aa, bb = abs(a), abs(b)
    g, s, t = rec(aa, bb)
    return g, s * (1 if a >= 0 else -1), t * (1 if b >= 0 else -1)


def reps_and_hnf(matrix):
    total = abs(det(matrix))
    bottom, u, v = bezout(matrix[1][0], matrix[1][1])
    top = total // bottom
    skew = (u * matrix[0][0] + v * matrix[0][1]) % top
    return [(i, j) for j in range(bottom) for i in range(top)], [[top, skew], [0, bottom]]


def q(x, y):
    return x * (x - 1) + x * y + Fraction(y * (y - 1), 2)


def qn(v, n):
    x, y = v
    total = Fraction(0)
    for _ in range(n):
        total += q(x, y)
        x, y = 2 * x + y, x + y
    return total


def qn_coefficients(n):
    # Independent recurrence for the five polynomial coefficients.  If
    # p(x,y)=a x^2+b xy+c y^2+d x+e y, then add q(A^j(x,y)).
    A = [[2, 1], [1, 1]]
    B = [[1, 0], [0, 1]]
    out = [Fraction(0) for _ in range(5)]
    for _ in range(n):
        p, r = B[0]
        s, u = B[1]
        add = [p*p+p*s+Fraction(s*s,2), 2*p*r+p*u+r*s+s*u,
               r*r+r*u+Fraction(u*u,2), -p-Fraction(s,2), -r-Fraction(u,2)]
        out = [left+right for left,right in zip(out,add)]
        B = multiply(A, B)
    return out


def eval_qn(coefficients, v):
    a,b,c,d,e = coefficients; x,y = v
    return a*x*x+b*x*y+c*y*y+d*x+e*y


def direct_rotation(matrix, shift, n):
    """Direct cocycle iteration on a common denominator (no coefficient path)."""
    first, second = shift
    denominator = det(matrix)
    xnum = matrix[1][1] * first - matrix[0][1] * second
    ynum = -matrix[1][0] * first + matrix[0][0] * second
    total_numerator = 0
    for _ in range(n):
        # q(x/d,y/d), written over the common denominator 2*d^2.
        total_numerator += (2*xnum*xnum + 2*xnum*ynum + ynum*ynum
                            - 2*xnum*denominator - ynum*denominator)
        xnum, ynum = 2*xnum + ynum, xnum + ynum
    total_numerator -= 2 * first * (-matrix[1][0] * first + matrix[0][0] * second) * denominator
    return Fraction(total_numerator, 2 * denominator * denominator) % 1


def parse(value):
    return Fraction(value)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence", nargs="?", type=Path, default=Path(__file__).resolve().parents[1] / "results/c151_heisenberg_fibre_evidence.json")
    args = parser.parse_args()
    data = json.loads(args.evidence.read_text())
    checks = 0

    def check(condition, message):
        nonlocal checks
        checks += 1
        if not condition:
            raise AssertionError(message)

    expected_top = {"schema", "candidate_id", "evaluation_date", "scope_literal", "source_commit", "source_lock", "fibre_rotation_theorem", "central_root_of_unity_projector", "rotation_ledger", "discarded_pattern", "formal_lift_hint", "route_a", "claim_boundary", "payload_sha256"}
    check(set(data) == expected_top, "top-level closure")
    check(data["schema"] == "hcs-c151-heisenberg-character-fibre-evidence-v1", "schema")
    check(data["candidate_id"] == "HCS-C151", "candidate")
    check(data["evaluation_date"] == "2026-08-25", "date")
    check(data["source_commit"] == "2d4e6211a254ef49d87718569d23466f4c6dcf4c", "commit")
    check(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    check(data["payload_sha256"] == canon_hash(data), "hash")
    lock = data["source_lock"]
    check(lock["matrix_A"] == [[2, 1], [1, 1]], "matrix")
    check(lock["cutoff"] == {"exact_rotation_histogram": 12}, "cutoff")
    check(lock["precision"] == "exact integer and rational arithmetic", "precision")
    check(lock["quotient_convention"] == "left quotient Gamma\\H", "quotient")
    A = [[2, 1], [1, 1]]
    all_counts = []
    for n, row in enumerate(data["rotation_ledger"], 1):
        an = power(A, n)
        matrix = [[an[0][0] - 1, an[0][1]], [an[1][0], an[1][1] - 1]]
        determinant = det(matrix)
        order = abs(determinant)
        reps, hnf = reps_and_hnf(matrix)
        coefficients = qn_coefficients(n)
        histogram = Counter()
        for first, second in reps:
            v = (
                Fraction(matrix[1][1] * first - matrix[0][1] * second, determinant),
                Fraction(-matrix[1][0] * first + matrix[0][0] * second, determinant),
            )
            rotation = direct_rotation(matrix, (first, second), n)
            check((rotation * (2 * order * order)).denominator == 1, f"denominator {n},{first},{second}")
            histogram[rotation] += 1
        frozen = {parse(item["rotation"]): item["multiplicity"] for item in row["histogram"]}
        denom_lcm = 1
        for residue in histogram:
            denom_lcm = lcm(denom_lcm, residue.denominator)
        check(row["n"] == n, f"n {n}")
        check(row["A_power"] == an, f"power {n}")
        check(row["M=A_power-I"] == matrix, f"M {n}")
        check(row["det_M"] == determinant, f"det {n}")
        check(row["horizontal_fixed_class_count"] == order == len(reps), f"order {n}")
        check(row["column_hnf"] == hnf, f"HNF {n}")
        check(row["universal_projector_order_Q"] == 2 * order * order, f"Q {n}")
        check(row["observed_denominator_lcm"] == denom_lcm, f"lcm {n}")
        check(row["rotation_support_size"] == len(histogram), f"support {n}")
        check(row["fixed_circle_component_count"] == histogram[Fraction(0)], f"zero {n}")
        check(frozen == histogram, f"histogram {n}")
        check(sum(frozen.values()) == order, f"mass {n}")
        if reps:
            sample = reps[len(reps)//2]
            sv = (Fraction(matrix[1][1]*sample[0]-matrix[0][1]*sample[1], determinant),
                  Fraction(-matrix[1][0]*sample[0]+matrix[0][0]*sample[1], determinant))
            check(direct_rotation(matrix, sample, n) == (eval_qn(coefficients, sv)-sample[0]*sv[1]) % 1,
                  f"direct/coefficient sentinel {n}")
        all_counts.append(histogram[Fraction(0)])

        # The same horizontal class represented after integral translation
        # must have the same rotation modulo one.
        for first, second in reps[: min(7, len(reps))]:
            v0 = (
                Fraction(matrix[1][1] * first - matrix[0][1] * second, determinant),
                Fraction(-matrix[1][0] * first + matrix[0][0] * second, determinant),
            )
            rho0 = (eval_qn(coefficients, v0) - first * v0[1]) % 1
            for r1, r2 in ((1, 0), (0, 1), (-1, 2)):
                vp = (v0[0] + r1, v0[1] + r2)
                mp1 = first + matrix[0][0] * r1 + matrix[0][1] * r2
                rhop = (eval_qn(coefficients, vp) - mp1 * vp[1]) % 1
                check(rhop == rho0, f"representative invariance {n}")

    theorem = data["fibre_rotation_theorem"]
    check(theorem["fixed_fibre_iff"] == "rho_n(v)=0 mod 1", "fixed iff")
    check(theorem["representative_invariance"] == "rho_n(v+r)-rho_n(v) is integral for every r in Z^2", "invariance theorem")
    check("area preservation" in theorem["representative_invariance_proof_key"], "proof key")
    check(theorem["clean_kernel"].startswith("along a fixed fibre"), "clean kernel")
    projector = data["central_root_of_unity_projector"]
    check(projector["denominator_bound"] == "rho_n belongs to (1/Q_n)Z/Z for Q_n=2*D_n^2", "denominator theorem")
    check(projector["rho_is_horizontal_group_homomorphism"] is False and projector["terminology_boundary"].startswith("central cyclic"), "projector terminology")
    check(projector["all_iterates"] is True, "all-n projector")
    rejected = data["discarded_pattern"]
    check(rejected["status"] == "FINITE_PATTERN_REJECTED_NOT_EXTRAPOLATED", "pattern status")
    check(rejected["witnesses"] == {"n10_fixed_circles": 105, "n12_fixed_circles": 144}, "pattern witnesses")
    check(rejected["all_n_closed_form_claimed"] is False, "no extrapolation")
    check(all_counts == [1, 1, 4, 1, 21, 4, 57, 1, 148, 105, 397, 144], "certified zero sequence")
    lift = data["formal_lift_hint"]
    check(lift["unitary"] is True and lift["iterate_clock_preserved"] is True, "Koopman")
    check(lift["character_filter_is_trace_formula"] is False and lift["isolated_orbit_weight_bridge_constructed"] is False, "no bridge")
    check(data["route_a"] == {"tuple": ["A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "overall": "ROUTE_A_EXPLORATORY", "route_b_invocation_allowed": False}, "route tuple")
    check(all(value is False for value in data["claim_boundary"].values()), "claim boundary")
    print(json.dumps({"status": "C151_CHECKER_PASS", "assertions": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
