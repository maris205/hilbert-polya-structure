#!/usr/bin/env python3
"""Independent standard-library checker for HCS-C146."""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path


def canon_hash(data):
    work = dict(data)
    work.pop("payload_sha256", None)
    return sha256(json.dumps(work, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def power(a, n):
    out = [[1, 0], [0, 1]]
    for _ in range(n):
        out = mul(out, a)
    return out


def det(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def lucas(n):
    previous, current = 2, 1
    if n == 0:
        return previous
    for _ in range(1, n):
        previous, current = current, previous + current
    return current


def q(v):
    x, y = v
    return x * (x - 1) + x * y + Fraction(1, 2) * y * (y - 1)


def grp(g, h):
    x, y, z = g
    X, Y, Z = h
    return x + X, y + Y, z + Z + x * Y


def phi(g):
    x, y, z = g
    return 2 * x + y, x + y, z + q((x, y))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence", nargs="?", type=Path, default=Path(__file__).resolve().parents[1] / "results/c146_heisenberg_evidence.json")
    args = parser.parse_args()
    data = json.loads(args.evidence.read_text())
    checks = 0

    def check(condition, message):
        nonlocal checks
        checks += 1
        if not condition:
            raise AssertionError(message)

    check(data["schema"] == "hcs-c146-heisenberg-clean-fixed-evidence-v1", "schema")
    check(data["candidate_id"] == "HCS-C146", "candidate")
    check(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    check(data["payload_sha256"] == canon_hash(data), "hash")
    check(set(data) == {"schema", "candidate_id", "evaluation_date", "scope_literal", "source_lock", "lattice_automorphism_theorem", "clean_fixed_circle_theorem", "iterate_ledger", "horizontal_torus_negative_control", "rejected_naive_component_lift", "formal_lift_hint", "route_a", "claim_boundary", "payload_sha256"}, "top-level schema closure")
    lock = data["source_lock"]
    check(lock["matrix_A"] == [[2, 1], [1, 1]] and det(lock["matrix_A"]) == 1, "matrix and volume determinant")
    check(lock["group_law"] == "(x,y,z)*(X,Y,Z)=(x+X,y+Y,z+Z+xY)", "group law")
    check(lock["cutoff"] == {"iterate_ledger": 20}, "cutoff")
    check(lock["precision"] == "exact integer and rational arithmetic", "precision")

    # Exact homomorphism checks over a grid.  The identity is quadratic, and
    # the separate polarization equality below checks its coefficients.
    samples = [Fraction(-2), Fraction(-1, 2), Fraction(0), Fraction(1, 3), Fraction(2)]
    for x in samples:
        for y in samples:
            check(q((x, y)) - (x * (x - 1) + x * y + Fraction(1, 2) * y * (y - 1)) == 0, f"q formula {x},{y}")
    for x in samples[:3]:
        for y in samples[:3]:
            for X in samples[2:]:
                for Y in samples[2:]:
                    left = q((x + X, y + Y)) - q((x, y)) - q((X, Y))
                    right = 2 * x * X + x * Y + X * y + y * Y
                    check(left == right, f"polarization {x},{y},{X},{Y}")
                    g, h = (x, y, Fraction(2, 5)), (X, Y, Fraction(-3, 7))
                    check(phi(grp(g, h)) == grp(phi(g), phi(h)), "homomorphism")
    for x in range(-8, 9):
        for y in range(-8, 9):
            check(q((Fraction(x), Fraction(y))).denominator == 1, f"integer q {x},{y}")

    A = [[2, 1], [1, 1]]
    rows = data["iterate_ledger"]
    check(len(rows) == 20, "ledger length")
    for n, row in enumerate(rows, 1):
        an = power(A, n)
        shifted = [[an[0][0] - 1, an[0][1]], [an[1][0], an[1][1] - 1]]
        determinant = det(shifted)
        trace = an[0][0] + an[1][1]
        check(row["n"] == n, f"n {n}")
        check(row["A_power"] == an, f"power {n}")
        check(row["trace"] == trace == lucas(2 * n), f"trace Lucas {n}")
        check(row["lucas_L_2n"] == lucas(2 * n), f"Lucas field {n}")
        check(row["det_A_power_minus_I"] == determinant == 2 - trace, f"det {n}")
        check(row["toral_isolated_fixed_points"] == abs(determinant) == lucas(2 * n) - 2, f"toral count {n}")
        check(row["certified_nilmanifold_fixed_circle_lower_bound"] == 1, f"circle lower bound {n}")
        check(row["central_multiplier"] == 1 and row["ordinary_isolated_denominator"] == "0", f"singularity {n}")
        check(row["lefschetz_number"] == 0, f"Lefschetz {n}")

    theorem = data["clean_fixed_circle_theorem"]
    check(theorem["fixed_by_every_positive_iterate"] is True, "fixed circle")
    check(theorem["fixed_set_is_never_discrete"] is True and theorem["clean_kernel_identity"] == "ker(I-DPhi_A^n)=T C along C because I-A^n is invertible", "nondiscrete clean kernel")
    check(theorem["isolated_stability_denominator_all_iterates"] == "det(I-DPhi_A^n)=det(I-A^n)*(1-1)=0", "factor")
    check(theorem["lefschetz_number_all_iterates"] == "1-tr(A^n)+tr(A^n)-1=0", "Lefschetz formula")

    # Independently replay the period-two cocycle obstruction.
    v = (Fraction(1, 5), Fraction(2, 5), Fraction(0))
    a2v = phi(phi(v))
    kx, ky = a2v[0] - v[0], a2v[1] - v[1]
    obstruction = a2v[2] - kx * v[1]
    rejected = data["rejected_naive_component_lift"]
    check((kx, ky) == (2, 1), "horizontal fixed class")
    check(obstruction == Fraction(-4, 5), "vertical obstruction")
    check(rejected["horizontal_class"] == ["1/5", "2/5"], "witness class")
    check(rejected["A2v_minus_v"] == ["2", "1"], "witness shift")
    check(rejected["q2_value"] == "0", "q2")
    check(rejected["left_quotient_vertical_fixed_condition_value"] == "-4/5", "condition value")
    check(rejected["condition_holds"] is False, "condition rejection")
    check(rejected["full_nilmanifold_component_count_through_20"] == "NOT_ASSERTED", "no count overclaim")

    lift = data["formal_lift_hint"]
    check(lift["operator"] == "Koopman U_Phi f=f composed with Phi on L2(N,Haar)", "Koopman operator")
    check(lift["domain"] == "all of L2(N,Haar); U_Phi is bounded", "Koopman domain")
    check(lift["unitary"] is True and lift["iterate_clock_preserved"] is True and lift["reason"] == "Phi is a Haar-volume-preserving nilmanifold automorphism", "Koopman unitarity, Haar reason, and clock")
    check(lift["isolated_orbit_weight_bridge_constructed"] is False and lift["status"] == "FORMAL_HINT_ONLY", "formal-only boundary")

    check(set(data["route_a"]) == {"tuple", "overall", "route_b_invocation_allowed"}, "Route-A schema closure")
    check(data["route_a"]["tuple"] == ["A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "tuple")
    check(data["route_a"]["overall"] == "ROUTE_A_EXPLORATORY", "overall")
    check(data["route_a"]["route_b_invocation_allowed"] is False, "Route B")
    check(all(value is False for value in data["claim_boundary"].values()), "claim boundary")
    print(json.dumps({"status": "C146_CHECKER_PASS", "assertions": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
