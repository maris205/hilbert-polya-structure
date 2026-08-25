#!/usr/bin/env python3
"""Independent exact checker for HCS-C147; imports no producer code."""
from __future__ import annotations

import argparse
from collections import defaultdict
from hashlib import sha256
import json
from math import gcd
from pathlib import Path


def canonical_hash(data):
    work = dict(data)
    work.pop("payload_sha256", None)
    return sha256(json.dumps(work, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def mu(n):
    primes = 0
    candidate = 2
    rest = n
    while candidate * candidate <= rest:
        if rest % candidate == 0:
            rest //= candidate
            primes += 1
            if rest % candidate == 0:
                return 0
            while rest % candidate == 0:
                rest //= candidate
        candidate += 1
    if rest > 1:
        primes += 1
    return -1 if primes & 1 else 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence", nargs="?", type=Path, default=Path(__file__).resolve().parents[1] / "results/c147_billiard_evidence.json")
    args = parser.parse_args()
    data = json.loads(args.evidence.read_text())
    checks = 0

    def check(condition, message):
        nonlocal checks
        checks += 1
        if not condition:
            raise AssertionError(message)

    check(data["schema"] == "hcs-c147-square-billiard-family-evidence-v1", "schema")
    check(data["candidate_id"] == "HCS-C147", "candidate")
    check(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    check(data["payload_sha256"] == canonical_hash(data), "hash")
    check(set(data) == {"schema", "candidate_id", "evaluation_date", "scope_literal", "source_lock", "family_theorem", "count_certificate", "primitive_direction_ledger", "length_square_degeneracy_groups", "symmetry_reduced_degeneracy_groups", "minimal_nontrivial_collision", "aspect_ratio_control", "natural_quantization", "route_a", "claim_boundary", "payload_sha256"}, "top-level schema closure")
    lock = data["source_lock"]
    check(lock["primitive_direction"] == "ordered positive absolute representative (m,n) with gcd(m,n)=1; four signed unfolded sectors, two after time reversal; coordinate swap retained", "orientation")
    check(lock["axis_boundary_classes"] == "(1,0) horizontal and (0,1) vertical are two time-reversal-quotiented classes, separately recorded and excluded from the positive ledger", "axes")
    check(lock["clock"] == "geometric billiard length L_(m,n)=2*sqrt(m^2+n^2)" and lock["determinant_convention"] == "ordinary isolated-orbit factor det(I-DP_gamma) for the full reduced Poincare linearization, tested only as an obstruction", "clock and determinant convention")
    check(lock["cutoff"] == {"m_max": 40, "n_max": 40}, "cutoff")
    check(lock["precision"] == "exact integer arithmetic with symbolic square roots", "precision")

    expected = []
    groups = defaultdict(list)
    symmetry = defaultdict(set)
    for m in range(1, 41):
        for n in range(1, 41):
            if gcd(m, n) != 1:
                continue
            square = m * m + n * n
            row = {
                "m": m, "n": n, "gcd": 1,
                "unfolded_displacement": [2 * m, 2 * n],
                "length": f"2*sqrt({square})", "length_squared": 4 * square,
                "wall_reflections": 2 * (m + n), "dirichlet_reflection_phase": 1,
                "orientation_convention": "ABSOLUTE_REPRESENTATIVE_WITH_SIGNED_SECTOR_MULTIPLICITIES",
                "signed_unfolded_sector_multiplicity": 4,
                "time_reversal_quotient_sector_multiplicity": 2,
                "family_dimension": 1, "family_tangent_multiplier": 1,
            }
            expected.append(row)
            groups[square].append([m, n])
            symmetry[square].add(tuple(sorted((m, n))))
    ledger = data["primitive_direction_ledger"]
    check(len(ledger) == len(expected), "ledger length")
    for index, (observed, wanted) in enumerate(zip(ledger, expected)):
        check(observed == wanted, f"direction row {index}")

    degeneracies = [{"m2_plus_n2": q, "ordered_multiplicity": len(pairs), "directions": pairs} for q, pairs in sorted(groups.items()) if len(pairs) > 1]
    check(data["length_square_degeneracy_groups"] == degeneracies, "ordered degeneracies")
    reduced = [{"m2_plus_n2": q, "symmetry_reduced_multiplicity": len(pairs), "representatives": [list(pair) for pair in sorted(pairs)]} for q, pairs in sorted(symmetry.items()) if len(pairs) > 1]
    check(data["symmetry_reduced_degeneracy_groups"] == reduced, "reduced degeneracies")
    check(reduced[0] == {"m2_plus_n2": 65, "symmetry_reduced_multiplicity": 2, "representatives": [[1, 8], [4, 7]]}, "minimal inequivalent collision")
    collision = data["minimal_nontrivial_collision"]
    check(collision["m2_plus_n2"] == 65, "collision square")
    check(collision["witness"] == [[1, 8], [4, 7]], "collision witness")
    check(1 * 1 + 8 * 8 == 4 * 4 + 7 * 7 == 65, "collision equality")
    for square in range(1, 65):
        reps = {tuple(sorted((m, n))) for m in range(1, 41) for n in range(1, 41) if gcd(m, n) == 1 and m * m + n * n == square}
        check(len(reps) <= 1, f"minimality q={square}")

    count = data["count_certificate"]
    mobius_count = sum(mu(d) * (40 // d) ** 2 for d in range(1, 41))
    check(count["positive_primitive_direction_count"] == len(expected), "primitive count")
    check(count["mobius_formula_value"] == mobius_count == len(expected), "Mobius formula")
    check(count["axis_boundary_class_count"] == 2, "axis count")
    check(count["full_signed_oriented_sector_count"] == 4 * len(expected), "signed oriented count")
    check(count["full_signed_time_reversal_quotient_sector_count"] == 2 * len(expected), "time-reversal quotient count")

    theorem = data["family_theorem"]
    check(theorem["transverse_parameter"] == "a one-dimensional transverse circle minus finitely many vertex-hitting offsets, decomposing into open cylinders", "transverse decomposition")
    check(theorem["positive_transverse_length"] is True, "positive transverse length")
    check(theorem["ambient_liouville_positive_measure"] is False, "zero ambient directional measure")
    check(theorem["local_section_coordinates"] == "s transverse to the primitive vector and theta angular deviation" and theorem["local_reduced_return"] == "P(s,theta)=(s+L*tan(theta),theta)" and theorem["poincare_return_on_fixed_curve"] == "identity" and theorem["family_tangent_multiplier"] == 1, "local fixed-curve return")
    check(theorem["linearization_at_family"] == "DP(s,0)=[[1,L],[0,1]]" and theorem["full_reduced_poincare_statement"] == "ker(I-DP_gamma) is exactly the fixed-family tangent" and theorem["ordinary_isolated_denominator"] == "det(I-DP_gamma)=0 because L>0", "full reduced Poincare clean kernel and determinant")
    check(theorem["reflection_count"] == "2(m+n)" and theorem["dirichlet_reflection_phase"] == "+1", "reflection phase")

    aspect = data["aspect_ratio_control"]
    check(aspect["height_squared"] == "sqrt(2)", "aspect basis")
    check(aspect["distinct_positive_direction_collisions"] == 0, "aspect collision")
    # The exact coefficient pair (m^2,n^2) in the Q-basis (1,sqrt(2))
    # uniquely identifies each positive ordered direction.
    coefficient_pairs = {(row["m"] ** 2, row["n"] ** 2) for row in ledger}
    check(len(coefficient_pairs) == len(ledger), "irrational aspect injectivity")

    quant = data["natural_quantization"]
    check(quant["operator"] == "positive Dirichlet half-wave H=sqrt(-Delta_D) on the unit square" and quant["underlying_laplacian"] == "-Delta_D with domain H^2 intersect H_0^1" and quant["hilbert_space"] == "L2 of the unit square" and quant["domain"] == "H_0^1, the form domain of -Delta_D", "quantization object and domain")
    check(quant["self_adjoint"] is True and quant["unitary_group"] == "U(t)=exp(-itH)" and quant["principal_symbol_and_clock"] == "|p|, giving the unit-speed billiard length clock on |p|=1" and quant["status"] == "NATURAL_INTEGRABLE_QUANTIZATION", "unitary clock-matched quantization")
    check(quant["antiunitary_time_reversal"] == "K is complex conjugation, K^2=I and K U(t) K=U(-t)" and quant["dirichlet_phase_bridge"] == "phase -1 per regular reflection and +1 over 2(m+n) reflections" and quant["clean_family_trace_bridge_constructed"] is False and quant["target_matching"] is False, "time reversal, reflection phase, and nonclaim")
    check(set(data["route_a"]) == {"tuple", "overall", "route_b_invocation_allowed"}, "Route-A schema closure")
    check(data["route_a"]["tuple"] == ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"], "tuple")
    check(data["route_a"]["overall"] == "ROUTE_A_EXPLORATORY", "overall")
    check(data["route_a"]["route_b_invocation_allowed"] is False, "Route B")
    check(all(value is False for value in data["claim_boundary"].values()), "boundary")
    print(json.dumps({"status": "C147_CHECKER_PASS", "assertions": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
