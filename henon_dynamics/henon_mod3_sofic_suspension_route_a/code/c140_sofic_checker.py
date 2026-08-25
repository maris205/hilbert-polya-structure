#!/usr/bin/env python3
"""Independent standard-library checker for C140; imports no producer code."""
from __future__ import annotations

from hashlib import sha256
import itertools
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c140_sofic_evidence.json"
ZERO = (0, 0)


def add(a, b):
    result = dict(a)
    for exponent, coefficient in b.items():
        result[exponent] = result.get(exponent, 0) + coefficient
    return {exponent: coefficient for exponent, coefficient in result.items() if coefficient}


def mul(a, b):
    result = {}
    for first, first_coefficient in a.items():
        for second, second_coefficient in b.items():
            exponent = (first[0] + second[0], first[1] + second[1])
            result[exponent] = result.get(exponent, 0) + first_coefficient * second_coefficient
    return {exponent: coefficient for exponent, coefficient in result.items() if coefficient}


def mmul(a, b):
    result = [[{} for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] = add(result[i][j], mul(a[i][k], b[k][j]))
    return result


def mpow(matrix, n):
    result = [[{ZERO: 1} if i == j else {} for j in range(len(matrix))] for i in range(len(matrix))]
    base = matrix
    while n:
        if n & 1:
            result = mmul(result, base)
        base = mmul(base, base)
        n //= 2
    return result


def trace(matrix):
    result = {}
    for i in range(len(matrix)):
        result = add(result, matrix[i][i])
    return result


def admissible(word):
    if not any(word):
        return True
    positions = [i for i, value in enumerate(word) if value]
    n = len(word)
    for i, position in enumerate(positions):
        gap = (positions[(i + 1) % len(positions)] - position - 1) % n
        if gap % 3:
            return False
    return True


def primitive(word):
    return not any(len(word) % d == 0 and word == word[:d] * (len(word) // d) for d in range(1, len(word)))


def least(word):
    return min(word[k:] + word[:k] for k in range(len(word)))


def feature(word):
    return (sum(word), len(word) - sum(word))


def receipt(poly):
    return {f"{exponent[0]},{exponent[1]}": coefficient for exponent, coefficient in sorted(poly.items())}


def payload_hash(data):
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_EVIDENCE
    data = json.loads(path.read_text())
    checks = 0

    def ck(condition, label):
        nonlocal checks
        if not condition:
            raise AssertionError(label)
        checks += 1

    def exact_keys(mapping, expected, label):
        ck(set(mapping) == set(expected), label)

    exact_keys(data, {"schema", "candidate_id", "date_utc", "scope_literal", "source_lock", "frozen_model", "sofic_theorem", "all_period_identity", "controls", "replay_prefix", "progress_and_boundary", "route_a", "scope_flags", "nonclaims", "payload_sha256"}, "top keys")
    ck(data["schema"] == "HCS-C140-v1", "schema")
    ck(data["candidate_id"] == "HCS-C140", "candidate")
    ck(data["date_utc"] == "2026-08-25", "date")
    ck(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    ck(data["payload_sha256"] == payload_hash(data), "payload hash")

    lock = data["source_lock"]
    exact_keys(lock, {"object", "presentation", "roof", "clock", "normalization", "determinant_convention", "precision", "cutoff", "forbidden_data"}, "lock keys")
    ck(lock["object"].startswith("the binary mod-three gap shift X3"), "object")
    ck(lock["presentation"] == "right-resolving residue graph 0--1-->0, 0--0-->1, 1--0-->2, 2--0-->0", "presentation")
    ck(lock["roof"] == {"label_1": "1", "label_0": "sqrt(2)"}, "roof")
    ck(lock["clock"] == "continuous label-roof suspension time ell=N1+sqrt(2)*N0", "clock")
    ck(lock["normalization"] == "each intrinsic label periodic point is counted once; the all-zero point is not counted with cover multiplicity", "normalization")
    ck(lock["determinant_convention"].startswith("D_cov=det(I-B); D_140=Z_140^(-1)"), "det convention")
    ck("periods 1 through 15" in lock["cutoff"], "cutoff")
    ck("Route-B inputs" in lock["forbidden_data"], "forbidden")

    model = data["frozen_model"]
    exact_keys(model, {"states", "labeled_transitions", "cover_matrix", "cover_determinant", "cover_zeta", "intrinsic_zeta", "intrinsic_inverse_zeta", "laplace_specialization", "entropy_characterization"}, "model keys")
    ck(model["states"] == [0, 1, 2], "states")
    ck(model["labeled_transitions"] == [[0, 0, "1"], [0, 1, "0"], [1, 2, "0"], [2, 0, "0"]], "transitions")
    ck(model["cover_matrix"] == [["u", "v", "0"], ["0", "0", "v"], ["v", "0", "0"]], "matrix")
    ck(model["cover_determinant"] == "D_cov(u,v)=1-u-v^3", "cover determinant")
    ck(model["cover_zeta"] == "Z_cov(u,v)=1/(1-u-v^3)", "cover zeta")
    ck(model["intrinsic_zeta"] == "Z_140(u,v)=(1+v+v^2)/(1-u-v^3)", "intrinsic zeta")
    ck(model["intrinsic_inverse_zeta"] == "D_140(u,v)=(1-u-v^3)/(1+v+v^2)=D_cov(u,v)*(1-v)/(1-v^3)", "inverse zeta")
    ck(model["laplace_specialization"] == "u=z*exp(-s), v=z*exp(-sqrt(2)*s)", "specialization")
    ck(model["entropy_characterization"] == "h is the unique positive solution 1-exp(-h)-exp(-3*sqrt(2)*h)=0", "entropy")

    theorem = data["sofic_theorem"]
    exact_keys(theorem, {"strictly_sofic", "three_follower_sets", "minimal_cover", "unique_lift_off_exception", "exceptional_point"}, "sofic keys")
    ck("not an SFT" in theorem["strictly_sofic"] and "3m+1>2L" in theorem["strictly_sofic"], "not SFT")
    ck(theorem["three_follower_sets"].endswith("1,001,01"), "followers")
    ck("minimal right Fischer cover" in theorem["minimal_cover"], "minimal cover")
    ck(theorem["unique_lift_off_exception"] == "every bi-infinite label sequence containing a 1 has a unique cover lift", "unique lift")
    ck(theorem["exceptional_point"].endswith("least period three"), "exception")

    identity = data["all_period_identity"]
    exact_keys(identity, {"weighted_fixed_formula", "correction_log", "log_zeta", "primitive_product", "suspension_product", "convergence", "all_period", "replay_cutoff_is_not_theorem_cutoff"}, "identity keys")
    ck(identity["weighted_fixed_formula"] == "F_n(u,v)=Tr(B(u,v)^n)+(1-3*1_[3|n])*v^n for every n>=1", "fixed formula")
    ck(identity["correction_log"] == "sum_(n>=1)(1-3*1_[3|n])*v^n/n=log(1+v+v^2)", "correction log")
    ck(identity["log_zeta"].endswith("+log(1+v+v^2)"), "log zeta")
    ck(identity["primitive_product"].startswith("D_140(u,v)=product_[gamma primitive label orbit]"), "product")
    ck(identity["suspension_product"].startswith("D_140(z,s)=product_[gamma primitive label orbit]"), "suspension")
    ck(identity["all_period"] is True and identity["replay_cutoff_is_not_theorem_cutoff"] is True, "all period")

    matrix = [[{(1, 0): 1}, {(0, 1): 1}, {}], [{}, {}, {(0, 1): 1}], [{(0, 1): 1}, {}, {}]]
    prefix = data["replay_prefix"]
    exact_keys(prefix, {"period_limit", "rows", "admissible_rooted_points_total", "primitive_label_cycles_total", "rooted_feature_cells_total", "primitive_feature_cells_total"}, "prefix keys")
    ck(prefix["period_limit"] == 15 and len(prefix["rows"]) == 15, "period limit")
    rows = []
    cover_sequence = []
    label_sequence = []
    rooted_total = primitive_total = rooted_cells_total = primitive_cells_total = 0
    for n in range(1, 16):
        cover_trace = trace(mpow(matrix, n))
        correction = 1 - 3 * int(n % 3 == 0)
        intrinsic = add(cover_trace, {(0, n): correction})
        words = [word for word in itertools.product((0, 1), repeat=n) if admissible(word)]
        histogram = {}
        for word in words:
            ck(admissible(word), f"admissible n={n} word={word}")
            vector = feature(word)
            ck(vector[0] + vector[1] == n, f"feature total n={n} word={word}")
            histogram[vector] = histogram.get(vector, 0) + 1
        ck(intrinsic == histogram, f"intrinsic correction n={n}")
        representatives = sorted({least(word) for word in words if primitive(word)})
        groups = {}
        for word in representatives:
            groups.setdefault(feature(word), []).append("".join(map(str, word)))
        rows.append({
            "period": n,
            "cover_fixed_points": sum(cover_trace.values()),
            "label_fixed_points": len(words),
            "all_zero_correction_coefficient": correction,
            "cover_weighted_trace_coefficients": receipt(cover_trace),
            "intrinsic_weighted_fixed_coefficients": receipt(intrinsic),
            "rooted_feature_cells": len(histogram),
            "primitive_label_cycles": len(representatives),
            "primitive_feature_cells": len(groups),
            "primitive_representatives": ["".join(map(str, word)) for word in representatives],
            "same_feature_primitive_groups": {f"{vector[0]},{vector[1]}": members for vector, members in sorted(groups.items()) if len(members) > 1},
        })
        cover_sequence.append(sum(cover_trace.values()))
        label_sequence.append(len(words))
        rooted_total += len(words)
        primitive_total += len(representatives)
        rooted_cells_total += len(histogram)
        primitive_cells_total += len(groups)
    ck(prefix["rows"] == rows, "all rows")
    ck(prefix["admissible_rooted_points_total"] == rooted_total == 969, "rooted total")
    ck(prefix["primitive_label_cycles_total"] == primitive_total == 74, "primitive total")
    ck(prefix["rooted_feature_cells_total"] == rooted_cells_total == 60, "rooted cells")
    ck(prefix["primitive_feature_cells_total"] == primitive_cells_total == 32, "primitive cells")

    controls = data["controls"]
    exact_keys(controls, {"cover_fixed_counts_periods_1_to_15", "label_fixed_counts_periods_1_to_15", "period_1_cover_to_label_correction", "period_3_cover_to_label_correction", "all_zero_label_point_least_period", "all_zero_cover_orbit_least_period", "nonlattice_witness", "no_imaginary_period"}, "control keys")
    ck(controls["cover_fixed_counts_periods_1_to_15"] == cover_sequence == [1, 1, 4, 5, 6, 10, 15, 21, 31, 46, 67, 98, 144, 211, 309], "cover sequence")
    ck(controls["label_fixed_counts_periods_1_to_15"] == label_sequence == [2, 2, 2, 6, 7, 8, 16, 22, 29, 47, 68, 96, 145, 212, 307], "label sequence")
    ck(controls["period_1_cover_to_label_correction"] == 1, "period1 correction")
    ck(controls["period_3_cover_to_label_correction"] == -2, "period3 correction")
    ck(controls["all_zero_label_point_least_period"] == 1, "label zero period")
    ck(controls["all_zero_cover_orbit_least_period"] == 3, "cover zero period")
    ck(controls["nonlattice_witness"] == "label fixed cycles [1] and [0] have suspension lengths 1 and sqrt(2)", "nonlattice")
    ck(controls["no_imaginary_period"].startswith("at fixed z=1") and controls["no_imaginary_period"].endswith("hence T=0"), "imaginary period")

    boundary = data["progress_and_boundary"]
    exact_keys(boundary, {"progress_over_full_shift_suspensions", "remaining_internal_obstruction", "target_obstruction"}, "boundary keys")
    ck("strictly sofic" in boundary["progress_over_full_shift_suspensions"], "progress")
    ck("rational correction" in boundary["remaining_internal_obstruction"], "owner boundary")
    ck("no target divisor" in boundary["target_obstruction"], "target boundary")

    route = data["route_a"]
    exact_keys(route, {"tuple", "overall", "A1_qualification", "A2_qualification", "A3_qualification", "A4_qualification", "route_b_invocation_allowed"}, "route keys")
    ck(route["tuple"] == ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"], "route tuple")
    ck(route["overall"] == "ROUTE_A_EXPLORATORY", "overall")
    ck(route["route_b_invocation_allowed"] is False, "route B")
    ck("WITHOUT_A_FROZEN_TARGET_DIVISOR_MATCH" in route["A2_qualification"], "A2 boundary")
    ck(route["A3_qualification"].startswith("NO_TARGET_FUNCTIONAL_EQUATION"), "A3 boundary")
    ck(route["A4_qualification"].startswith("NO_NATURAL_SELF_ADJOINT"), "A4 boundary")

    flags = data["scope_flags"]
    exact_keys(flags, {"scope", "uses_prime_table", "uses_zero_table", "claims_arithmetic_euler_factors", "claims_root_number", "claims_automorphy", "claims_hilbert_polya", "uses_route_b_inputs"}, "flag keys")
    ck(flags["scope"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "flag scope")
    for name, value in flags.items():
        if name != "scope":
            ck(value is False, f"false flag {name}")
    ck(data["nonclaims"] == [
        "that the three-state cover trace already equals the intrinsic label fixed-point trace",
        "a natural Fredholm determinant owner for the corrected rational inverse zeta",
        "an arithmetic Euler product or local factorization",
        "a target zero or pole divisor match, functional equation, or counting law",
        "a natural self-adjoint Hilbert--Polya operator",
        "Route-B authorization or a solution of the larger program",
    ], "nonclaims")

    print(json.dumps({"status": "C140_CHECK_PASS", "checks": checks, "evidence": str(path)}, sort_keys=True))


if __name__ == "__main__":
    main()
