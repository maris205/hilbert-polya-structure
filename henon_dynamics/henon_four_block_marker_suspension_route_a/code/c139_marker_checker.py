#!/usr/bin/env python3
"""Independent standard-library checker for C139; imports no producer code."""
from __future__ import annotations

from hashlib import sha256
import itertools
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c139_marker_evidence.json"
STATES = tuple(itertools.product((0, 1), repeat=3))
INDEX = {state: index for index, state in enumerate(STATES)}
ZERO = (0, 0, 0, 0, 0)


def primitive(word):
    return not any(len(word) % d == 0 and word == word[:d] * (len(word) // d) for d in range(1, len(word)))


def least(word):
    return min(word[k:] + word[:k] for k in range(len(word)))


def blocks(word, width):
    out = [0] * (2 ** width)
    for start in range(len(word)):
        value = 0
        for offset in range(width):
            value = 2 * value + word[(start + offset) % len(word)]
        out[value] += 1
    return tuple(out)


def feature(word):
    return blocks(word, 2) + (blocks(word, 4)[3],)


def key(vector):
    return ",".join(map(str, vector))


def payload_hash(data):
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def state_trace(n):
    total = {}
    for start in range(8):
        active = {(start, ZERO): 1}
        for _ in range(n):
            following = {}
            for (state_index, exponent), coefficient in active.items():
                a, b, c = STATES[state_index]
                for d in (0, 1):
                    increment = [0, 0, 0, 0, 0]
                    increment[2 * a + b] = 1
                    increment[4] = int((a, b, c, d) == (0, 0, 1, 1))
                    new_exponent = tuple(x + y for x, y in zip(exponent, increment))
                    target = INDEX[(b, c, d)]
                    following[(target, new_exponent)] = following.get((target, new_exponent), 0) + coefficient
            active = following
        for (state_index, exponent), coefficient in active.items():
            if state_index == start:
                total[exponent] = total.get(exponent, 0) + coefficient
    return total


def receipt(word):
    return {
        "word": "".join(map(str, word)),
        "primitive": primitive(word),
        "canonical_rotation": "".join(map(str, least(word))),
        "symbol_counts_0_1": list(blocks(word, 1)),
        "edge_counts_00_01_10_11": list(blocks(word, 2)),
        "trigram_counts_000_to_111": list(blocks(word, 3)),
        "marker_count_0011": blocks(word, 4)[3],
        "clock_basis_coefficients_1_sqrt2_sqrt3_sqrt6_sqrt5": list(feature(word)),
    }


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

    exact_keys(data, {"schema", "candidate_id", "date_utc", "scope_literal", "source_lock", "frozen_model", "all_period_identity", "minimal_memory_theorem", "controls", "replay_prefix", "progress_and_boundary", "route_a", "scope_flags", "nonclaims", "payload_sha256"}, "top keys")
    ck(data["schema"] == "HCS-C139-v1", "schema")
    ck(data["candidate_id"] == "HCS-C139", "candidate")
    ck(data["date_utc"] == "2026-08-25", "date")
    ck(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    ck(data["payload_sha256"] == payload_hash(data), "payload hash")

    lock = data["source_lock"]
    exact_keys(lock, {"object", "base_edge_roof", "marker", "eta", "clock", "normalization", "determinant_convention", "precision", "cutoff", "forbidden_data"}, "lock keys")
    ck(lock["base_edge_roof"] == [["1", "sqrt(2)"], ["sqrt(3)", "sqrt(6)"]], "edge roof")
    ck(lock["marker"] == "0011" and lock["eta"] == "sqrt(5)", "marker freeze")
    ck(lock["normalization"] == "one base transition per shift step; forward four-block occurrence counted at its initial coordinate", "normalization")
    ck(lock["determinant_convention"].startswith("Delta_139(x,y)=det(I-M_139(x,y))"), "det convention")
    ck("periods 1 through 12" in lock["cutoff"], "cutoff")
    ck("Route-B inputs" in lock["forbidden_data"], "forbidden")

    model = data["frozen_model"]
    exact_keys(model, {"states", "transition_rule", "formal_determinant", "formal_determinant_receipt", "edge_roof_specialization", "clock_formula", "basis_independence", "y_equals_one_reduction"}, "model keys")
    ck(model["states"] == ["".join(map(str, state)) for state in STATES], "states")
    ck(model["transition_rule"] == "abc -> bcd has weight x_ab*y^(1_[abcd=0011]) for d in {0,1}", "transition")
    ck(model["formal_determinant"] == "Delta_139=1-x00-x11-x01*x10+x00*x11+(1-y)*x00*x01*x10*x11", "determinant")
    expected_det = {
        "0,0,0,0,0": 1,
        "0,0,0,1,0": -1,
        "0,1,1,0,0": -1,
        "1,0,0,0,0": -1,
        "1,0,0,1,0": 1,
        "1,1,1,1,0": 1,
        "1,1,1,1,1": -1,
    }
    ck(model["formal_determinant_receipt"] == expected_det, "det receipt")
    ck(model["edge_roof_specialization"] == "x_ab=z*exp(-s*tau_ab), y=exp(-sqrt(5)*s)", "specialization")
    ck(model["clock_formula"] == "ell=N00+sqrt(2)N01+sqrt(3)N10+sqrt(6)N11+sqrt(5)N0011", "clock")
    ck(model["basis_independence"] == "1,sqrt(2),sqrt(3),sqrt(6),sqrt(5) are Q-linearly independent", "basis")
    ck(model["y_equals_one_reduction"].endswith("the C135 edge determinant"), "C135 reduction")
    collapsed = {}
    for exponent, coefficient in expected_det.items():
        vector = tuple(map(int, exponent.split(",")))
        reduced = vector[:4] + (0,)
        collapsed[key(reduced)] = collapsed.get(key(reduced), 0) + coefficient
    collapsed = {k: v for k, v in collapsed.items() if v}
    ck(collapsed == {"0,0,0,0,0": 1, "0,0,0,1,0": -1, "0,1,1,0,0": -1, "1,0,0,0,0": -1, "1,0,0,1,0": 1}, "computed reduction")

    identity = data["all_period_identity"]
    exact_keys(identity, {"trace_formula", "log_determinant", "primitive_product", "suspension_product", "convergence", "all_period", "replay_cutoff_is_not_theorem_cutoff"}, "identity keys")
    ck(identity["trace_formula"].startswith("Tr(M_139(x,y)^n)="), "trace formula")
    ck(identity["log_determinant"] == "-log Delta_139=sum_(n>=1) Tr(M_139^n)/n", "log determinant")
    ck(identity["primitive_product"].startswith("Delta_139=product_[gamma primitive]"), "primitive product")
    ck(identity["suspension_product"].startswith("Delta_139(z,s)=product_[gamma primitive]"), "suspension product")
    ck(identity["all_period"] is True and identity["replay_cutoff_is_not_theorem_cutoff"] is True, "all period flags")

    prefix = data["replay_prefix"]
    exact_keys(prefix, {"period_limit", "rows", "rooted_closed_words_total", "primitive_cycles_total", "rooted_feature_cells_total", "primitive_feature_cells_total"}, "prefix keys")
    ck(prefix["period_limit"] == 12 and len(prefix["rows"]) == 12, "period limit")
    rooted_total = primitive_total = rooted_cells_total = primitive_cells_total = 0
    first_collision = None
    rebuilt_rows = []
    for n in range(1, 13):
        words = list(itertools.product((0, 1), repeat=n))
        histogram = {}
        for word in words:
            vector = feature(word)
            ck(sum(vector[:4]) == n, f"edge total n={n} word={word}")
            ck(0 <= vector[4] <= n, f"marker range n={n} word={word}")
            histogram[vector] = histogram.get(vector, 0) + 1
        ck(histogram == state_trace(n), f"independent state trace n={n}")
        representatives = sorted({least(word) for word in words if primitive(word)})
        groups = {}
        for word in representatives:
            groups.setdefault(feature(word), []).append("".join(map(str, word)))
        collisions = {key(vector): members for vector, members in sorted(groups.items()) if len(members) > 1}
        if collisions and first_collision is None:
            first_collision = n
        rebuilt_rows.append({
            "period": n,
            "rooted_closed_words": len(words),
            "primitive_cycles": len(representatives),
            "feature_histogram_cells": len(histogram),
            "primitive_feature_cells": len(groups),
            "weighted_trace_coefficients": {key(vector): coefficient for vector, coefficient in sorted(histogram.items())},
            "primitive_representatives": ["".join(map(str, word)) for word in representatives],
            "same_feature_primitive_groups": collisions,
        })
        rooted_total += len(words)
        primitive_total += len(representatives)
        rooted_cells_total += len(histogram)
        primitive_cells_total += len(groups)
    ck(prefix["rows"] == rebuilt_rows, "all rows")
    ck(prefix["rooted_closed_words_total"] == rooted_total == 8190, "rooted total")
    ck(prefix["primitive_cycles_total"] == primitive_total == 747, "primitive total")
    ck(prefix["rooted_feature_cells_total"] == rooted_cells_total == 258, "rooted cells")
    ck(prefix["primitive_feature_cells_total"] == primitive_cells_total == 229, "primitive cells")

    theorem = data["minimal_memory_theorem"]
    exact_keys(theorem, {"statement", "pair", "common_1_block_counts", "common_2_block_counts", "common_3_block_counts", "marker_counts", "clock_difference_second_minus_first", "coding_boundary"}, "memory theorem keys")
    first = tuple(map(int, theorem["pair"][0]))
    second = tuple(map(int, theorem["pair"][1]))
    ck(theorem["pair"] == ["001011", "001101"], "memory pair")
    ck(list(blocks(first, 1)) == list(blocks(second, 1)) == theorem["common_1_block_counts"] == [3, 3], "one blocks")
    ck(list(blocks(first, 2)) == list(blocks(second, 2)) == theorem["common_2_block_counts"] == [1, 2, 2, 1], "two blocks")
    ck(list(blocks(first, 3)) == list(blocks(second, 3)) == theorem["common_3_block_counts"] == [0, 1, 1, 1, 1, 1, 1, 0], "three blocks")
    ck([blocks(first, 4)[3], blocks(second, 4)[3]] == theorem["marker_counts"] == [0, 1], "marker counts")
    ck(theorem["clock_difference_second_minus_first"] == "sqrt(5)", "clock difference")
    ck("not asserted cohomology invariant" in theorem["coding_boundary"], "coding boundary")

    controls = data["controls"]
    exact_keys(controls, {"minimal_pair_receipts", "residual_collision_pair", "residual_pair_receipts", "residual_feature_vector", "residual_pair_nonrotation", "first_same_feature_primitive_collision_period", "nonlattice_witness", "no_imaginary_period"}, "control keys")
    ck(controls["minimal_pair_receipts"] == [receipt(first), receipt(second)], "minimal receipts")
    residual_first = tuple(map(int, controls["residual_collision_pair"][0]))
    residual_second = tuple(map(int, controls["residual_collision_pair"][1]))
    ck(controls["residual_collision_pair"] == ["0101111", "0110111"], "residual pair")
    ck(controls["residual_pair_receipts"] == [receipt(residual_first), receipt(residual_second)], "residual receipts")
    ck(feature(residual_first) == feature(residual_second) == tuple(controls["residual_feature_vector"]) == (0, 2, 2, 3, 0), "residual vector")
    ck(residual_second not in [residual_first[k:] + residual_first[:k] for k in range(7)], "residual nonrotation recomputed")
    ck(controls["residual_pair_nonrotation"] is True, "residual nonrotation flag")
    ck(controls["first_same_feature_primitive_collision_period"] == first_collision == 7, "first collision")
    ck(controls["nonlattice_witness"] == "fixed cycles [0] and [1] have lengths 1 and sqrt(6)", "nonlattice")
    ck(controls["no_imaginary_period"].startswith("at fixed z=1") and controls["no_imaginary_period"].endswith("hence T=0"), "imaginary period")

    boundary = data["progress_and_boundary"]
    exact_keys(boundary, {"progress_over_C135", "remaining_internal_obstruction", "target_obstruction"}, "boundary keys")
    ck("one-, two-, and three-block" in boundary["progress_over_C135"], "progress")
    ck("period-seven" in boundary["remaining_internal_obstruction"], "internal obstruction")
    ck("no target divisor" in boundary["target_obstruction"], "target boundary")

    route = data["route_a"]
    exact_keys(route, {"tuple", "overall", "A1_qualification", "A2_qualification", "A3_qualification", "A4_qualification", "route_b_invocation_allowed"}, "route keys")
    ck(route["tuple"] == ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"], "tuple")
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
        "coding-independent or cohomology-invariant minimal memory",
        "primitive-orbit injectivity after adding the 0011 marker",
        "an arithmetic Euler product or local factorization",
        "a target zero or pole divisor match, functional equation, or counting law",
        "a natural self-adjoint Hilbert--Polya operator",
        "Route-B authorization or a solution of the larger program",
    ], "nonclaims")

    print(json.dumps({"status": "C139_CHECK_PASS", "checks": checks, "evidence": str(path)}, sort_keys=True))


if __name__ == "__main__":
    main()
