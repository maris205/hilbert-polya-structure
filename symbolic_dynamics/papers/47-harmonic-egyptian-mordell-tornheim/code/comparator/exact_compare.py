#!/usr/bin/env python3
"""Strict, non-coercing D/P comparator and X semantic mutation consumer."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import sys
from pathlib import Path
from typing import Any


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       separators=(",", ": ")) + "\n").encode("ascii")


def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def load(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    value = json.loads(raw.decode("ascii"), object_pairs_hook=unique)
    if type(value) is not dict or raw != canonical(value):
        raise ValueError("noncanonical JSON")
    return value


def strict_equal(left: Any, right: Any) -> bool:
    if type(left) is not type(right):
        return False
    if type(left) is dict:
        return list(left.keys()) == list(right.keys()) and all(strict_equal(left[k], right[k]) for k in left)
    if type(left) is list:
        return len(left) == len(right) and all(strict_equal(a, b) for a, b in zip(left, right))
    return left == right


def exact_keys(value: Any, keys: set[str], label: str) -> None:
    if type(value) is not dict or set(value) != keys or any(type(k) is not str for k in value):
        raise ValueError(f"{label} shape")


def rational_shape(value: Any) -> None:
    exact_keys(value, {"denominator", "numerator"}, "rational")
    if type(value["denominator"]) is not int or type(value["numerator"]) is not int \
            or value["denominator"] <= 0:
        raise ValueError("rational types")
    if math.gcd(value["numerator"], value["denominator"]) != 1:
        raise ValueError("noncanonical rational")


def reject(code: str) -> None:
    sys.stdout.buffer.write(canonical({"consumer": "X", "rejection_code": code,
                                      "schema": "paper47-mutation-rejection-v1", "status": "REJECT"}))
    raise SystemExit(2)


def validate_model(model: dict[str, Any]) -> None:
    expected = {"bounded_domain", "candidate_id", "coprime_required", "determinant_domains",
                "edge_parameterization", "hilbert_schmidt_domain", "loops", "mixed_triangle",
                "mt_novelty_claimed", "operator_positive_semidefinite", "ordered_edge_multiplier",
                "primitive_mt_factor", "relation", "scale_factor", "temporal_primitive",
                "trace_class_domain"}
    if set(model) != expected:
        reject("SCIENCE_MODEL_SHAPE_FAILURE")
    if model["relation"] != "m_plus_n_divides_m_times_n": reject("SOURCE_RELATION_CHANGED")
    if model["loops"] != "retain_even_exactly": reject("LOOP_CONVENTION_CHANGED")
    if type(model["coprime_required"]) is not bool or model["coprime_required"] is not True:
        reject("EDGE_PARAMETERIZATION_NONUNIQUE")
    if model["edge_parameterization"] != "g_equals_t_times_a_plus_b":
        reject("EDGE_PARAMETERIZATION_FALSE")
    if model["scale_factor"] != "zeta_2s": reject("SECOND_TRACE_SCALE_FAILURE")
    if model["primitive_mt_factor"] != "divide_by_zeta_4s": reject("PRIMITIVE_MT_FACTOR_FAILURE")
    if type(model["ordered_edge_multiplier"]) is not int or model["ordered_edge_multiplier"] != 1:
        reject("ORDERED_EDGE_MULTIPLICITY_FAILURE")
    if type(model["mixed_triangle"]) is not list or model["mixed_triangle"] != [15, 30, 60] \
            or any(type(x) is not int for x in model["mixed_triangle"]):
        reject("SUPPORT_WITNESS_FAILURE")


def validate_top(obj: dict[str, Any], schema: str) -> dict[str, Any]:
    exact_keys(obj, {"candidate_id", "payload", "schema", "status"}, schema)
    if obj["candidate_id"] != "SD-C49" or obj["schema"] != schema or obj["status"] != "PASS" \
            or type(obj["payload"]) is not dict:
        raise ValueError("top contract")
    return obj["payload"]


def validate_common_projection(payload: dict[str, Any]) -> None:
    cutoffs = payload["cutoffs"]
    if type(cutoffs) is not list or [row.get("N") for row in cutoffs if type(row) is dict] != [16, 32, 64, 128]:
        raise ValueError("cutoff grid")
    for row in cutoffs:
        exact_keys(row, {"N", "loops", "ordered_edges", "ordered_harmonic_quotients"}, "cutoff")
        if type(row["N"]) is not int or type(row["loops"]) is not list \
                or any(type(x) is not int for x in row["loops"]):
            raise ValueError("cutoff scalar types")
        pairs: list[tuple[int, int]] = []
        for pair in row["ordered_edges"]:
            if type(pair) is not list or len(pair) != 2 or any(type(x) is not int for x in pair):
                raise ValueError("edge shape")
            pairs.append((pair[0], pair[1]))
        if pairs != sorted(set(pairs)) or any(not (1 <= m <= row["N"] and 1 <= n <= row["N"])
                                                for m, n in pairs):
            raise ValueError("edge ordering/domain")
        quotients = row["ordered_harmonic_quotients"]
        if type(quotients) is not list or len(quotients) != len(pairs):
            raise ValueError("quotient length")
        for pair, item in zip(pairs, quotients):
            exact_keys(item, {"m", "n", "quotient"}, "quotient")
            if any(type(item[k]) is not int for k in item) or (item["m"], item["n"]) != pair \
                    or item["quotient"] < 1 or item["quotient"] * (item["m"] + item["n"]) != item["m"] * item["n"]:
                raise ValueError("quotient identity")
        if row["loops"] != [m for m, n in pairs if m == n] \
                or row["loops"] != list(range(2, row["N"] + 1, 2)):
            raise ValueError("loop convention")

    matrices = payload["adjacency_matrices"]
    if type(matrices) is not list or [row.get("N") for row in matrices if type(row) is dict] != [16, 32]:
        raise ValueError("matrix grid")
    for row in matrices:
        exact_keys(row, {"N", "entries"}, "matrix")
        entries = row["entries"]
        if type(entries) is not list or len(entries) != row["N"]:
            raise ValueError("matrix rows")
        if any(type(line) is not list or len(line) != row["N"]
               or any(type(x) is not int or x not in (0, 1) for x in line) for line in entries):
            raise ValueError("matrix entry types")

    rows = payload["rows"]
    if type(rows) is not list or len(rows) != 128:
        raise ValueError("row grid")
    for expected_m, row in enumerate(rows, 1):
        exact_keys(row, {"m", "neighbors"}, "row")
        if type(row["m"]) is not int or row["m"] != expected_m or type(row["neighbors"]) is not list \
                or any(type(x) is not int or x < 1 for x in row["neighbors"]) \
                or row["neighbors"] != sorted(set(row["neighbors"])):
            raise ValueError("row types/order")

    walks = payload["walks"]
    grid = [(n, length) for n in (16, 32) for length in range(1, 6)]
    if type(walks) is not list or [(row.get("N"), row.get("length")) for row in walks
                                    if type(row) is dict] != grid:
        raise ValueError("walk grid")
    for row in walks:
        exact_keys(row, {"N", "length", "vertex_words"}, "walk block")
        words = row["vertex_words"]
        if type(row["N"]) is not int or type(row["length"]) is not int or type(words) is not list:
            raise ValueError("walk block types")
        if any(type(word) is not list or len(word) != row["length"]
               or any(type(v) is not int or not 1 <= v <= row["N"] for v in word) for word in words):
            raise ValueError("walk word types")
        if words != sorted(words):
            raise ValueError("walk ordering")


def compare(direct: dict[str, Any], parameter: dict[str, Any]) -> dict[str, Any]:
    d = validate_top(direct, "paper47-evaluator-d-v1")
    p = validate_top(parameter, "paper47-evaluator-p-v1")
    exact_keys(d, {"adjacency_matrices", "cutoffs", "evidence_class", "negative_minor", "rows",
                   "trace_powers", "trace_summary", "walks"}, "D payload")
    exact_keys(p, {"adjacency_matrices", "complex_phase_certificate", "coordinates", "cutoffs",
                   "endpoint_controls", "evidence_class", "phase_certificate",
                   "rectangular_mt_controls", "rows", "trace_powers", "trace_summary", "walks"},
               "P payload")
    validate_common_projection(d)
    validate_common_projection(p)
    checks: dict[str, str] = {}

    for key, label in [("cutoffs", "ordered_support_quotients_loops"),
                       ("adjacency_matrices", "literal_matrices"), ("rows", "full_divisor_rows"),
                       ("walks", "based_closed_walks")]:
        if not strict_equal(d[key], p[key]):
            raise ValueError(label)
        checks[label] = "PASS"
    if d["evidence_class"] != "FINITE_EXACT_CONTROL" or not strict_equal(d["evidence_class"], p["evidence_class"]):
        raise ValueError("evidence class")
    checks["finite_evidence_class"] = "PASS"

    def trace_map(records: list[Any]) -> dict[tuple[int, int, int], Any]:
        result = {}
        for row in records:
            exact_keys(row, {"N", "method", "power", "s", "value"}, "trace power")
            if any(type(row[k]) is not int for k in ("N", "power", "s")) or type(row["method"]) is not str:
                raise ValueError("trace types")
            rational_shape(row["value"])
            key = (row["N"], row["power"], row["s"])
            if key in result: raise ValueError("duplicate trace key")
            result[key] = row["value"]
        return result
    direct_trace_map = trace_map(d["trace_powers"])
    parameter_trace_map = trace_map(p["trace_powers"])
    expected_trace_grid = {(n, power, s) for n in (16, 32) for power in range(1, 6) for s in (2, 4)}
    if set(direct_trace_map) != expected_trace_grid or set(parameter_trace_map) != expected_trace_grid:
        raise ValueError("trace power grid")
    if not strict_equal(direct_trace_map, parameter_trace_map):
        raise ValueError("trace power mismatch")
    checks["exact_trace_powers_1_through_5"] = "PASS"

    dsum = {(row["N"], row["s"]): row for row in d["trace_summary"]}
    psum = {(row["N"], row["s"]): row for row in p["trace_summary"]}
    expected_summary_grid = {(n, s) for n in (16, 32, 64, 128) for s in (2, 4)}
    if set(dsum) != expected_summary_grid or set(psum) != expected_summary_grid:
        raise ValueError("trace grid")
    for key in sorted(dsum):
        dr, pr = dsum[key], psum[key]
        exact_keys(dr, {"N", "s", "trace_1_direct_diagonal", "trace_2_direct_ordered_edges"}, "D trace")
        exact_keys(pr, {"N", "s", "trace_1_even_harmonic", "trace_2_parameter_ordered_edges",
                        "trace_2_termwise_scale_cutoff"}, "P trace")
        for q in [dr["trace_1_direct_diagonal"], dr["trace_2_direct_ordered_edges"],
                  pr["trace_1_even_harmonic"], pr["trace_2_parameter_ordered_edges"],
                  pr["trace_2_termwise_scale_cutoff"]]: rational_shape(q)
        if not strict_equal(dr["trace_1_direct_diagonal"], pr["trace_1_even_harmonic"]):
            raise ValueError("first trace")
        if not strict_equal(dr["trace_2_direct_ordered_edges"], pr["trace_2_parameter_ordered_edges"]) \
                or not strict_equal(dr["trace_2_direct_ordered_edges"], pr["trace_2_termwise_scale_cutoff"]):
            raise ValueError("second trace")
    checks["first_trace_even_harmonic"] = "PASS"
    checks["second_trace_termwise_finite_cutoff"] = "PASS"

    cutoff_map = {row["N"]: {tuple(pair) for pair in row["ordered_edges"]} for row in p["cutoffs"]}
    for block in p["coordinates"]:
        exact_keys(block, {"N", "ordered_coordinates"}, "coordinate block")
        reconstructed: set[tuple[int, int]] = set()
        seen: set[tuple[int, int]] = set()
        for row in block["ordered_coordinates"]:
            exact_keys(row, {"a", "b", "m", "n", "quotient", "t"}, "coordinate")
            if any(type(row[k]) is not int or row[k] < 1 for k in row): raise ValueError("coordinate types")
            if math.gcd(row["a"], row["b"]) != 1 \
                    or row["m"] != row["t"] * row["a"] * (row["a"] + row["b"]) \
                    or row["n"] != row["t"] * row["b"] * (row["a"] + row["b"]) \
                    or row["quotient"] != row["t"] * row["a"] * row["b"]:
                raise ValueError("coordinate identity")
            pair = (row["m"], row["n"])
            if pair in seen: raise ValueError("nonunique coordinates")
            seen.add(pair); reconstructed.add(pair)
        if reconstructed != cutoff_map[block["N"]]: raise ValueError("coordinate support")
    checks["coprime_coordinate_bijection"] = "PASS"

    for row in p["rectangular_mt_controls"]:
        exact_keys(row, {"B", "domain", "primitive_scaled", "s", "unrestricted"}, "rectangular")
        rational_shape(row["primitive_scaled"]); rational_shape(row["unrestricted"])
        if row["domain"] != "rectangular_p_q_le_B" \
                or not strict_equal(row["primitive_scaled"], row["unrestricted"]):
            raise ValueError("rectangular control")
    if {(row["B"], row["s"]) for row in p["rectangular_mt_controls"]} \
            != {(bound, s) for bound in (16, 32, 64, 128) for s in (2, 4)}:
        raise ValueError("rectangular grid")
    checks["rectangular_primitive_mt_gcd_extraction"] = "PASS"

    for row in d["negative_minor"]:
        exact_keys(row, {"determinant", "s"}, "minor")
        rational_shape(row["determinant"])
        if row["determinant"]["numerator"] != -1 or row["determinant"]["denominator"] != 18 ** row["s"]:
            raise ValueError("negative minor")
    checks["negative_principal_minor"] = "PASS"
    endpoint = p["endpoint_controls"]
    exact_keys(endpoint, {"interval_diagnostics", "squarefree_degree_controls",
                          "strict_endpoint_witnesses"}, "endpoint controls")
    expected_grid = [(0, 1), (1, 4), (1, 2), (3, 4), (1, 1), (5, 4), (2, 1)]
    observed_grid = []
    for row in endpoint["interval_diagnostics"]:
        exact_keys(row, {"bounded_compact", "det2", "diagnostic_kind", "hilbert_schmidt",
                         "ordinary_determinant", "sigma", "trace_class"}, "sigma diagnostic")
        rational_shape(row["sigma"])
        pair = (row["sigma"]["numerator"], row["sigma"]["denominator"])
        observed_grid.append(pair)
        numerator, denominator = pair
        expected_flags = [numerator > 0, 2 * numerator > denominator,
                          2 * numerator > denominator, numerator > denominator,
                          numerator > denominator]
        observed_flags = [row["bounded_compact"], row["det2"], row["hilbert_schmidt"],
                          row["ordinary_determinant"], row["trace_class"]]
        if any(type(flag) is not bool for flag in observed_flags) or observed_flags != expected_flags \
                or row["diagnostic_kind"] != "PROOF_BACKED_EXACT_DOMAIN_DIAGNOSTIC":
            raise ValueError("endpoint diagnostic")
    if observed_grid != expected_grid:
        raise ValueError("endpoint grid")
    for index, row in enumerate(endpoint["squarefree_degree_controls"], 1):
        exact_keys(row, {"degree", "m", "omega", "tau_m_squared"}, "squarefree control")
        if row["omega"] != index or row["tau_m_squared"] != 3 ** index \
                or row["degree"] != (3 ** index - 1) // 2:
            raise ValueError("squarefree degree")
    phase = p["complex_phase_certificate"]
    if phase != {"factorization": "E_sigma_plus_i_tau_equals_U_tau_E_sigma_U_tau",
                 "nonreal_operator_hermitian": False, "singular_values_depend_only_on": "Re_s",
                 "two_sided_unitary_invariance": True}:
        raise ValueError("complex phase")
    checks["endpoint_and_complex_phase_controls"] = "PASS"
    if list(sorted(checks)) != list(checks):
        checks = {key: checks[key] for key in sorted(checks)}
    expected_check_keys = [
        "based_closed_walks", "coprime_coordinate_bijection", "endpoint_and_complex_phase_controls",
        "exact_trace_powers_1_through_5", "finite_evidence_class", "first_trace_even_harmonic", "full_divisor_rows",
        "literal_matrices", "negative_principal_minor", "ordered_support_quotients_loops",
        "rectangular_primitive_mt_gcd_extraction", "second_trace_termwise_finite_cutoff"
    ]
    if list(checks) != expected_check_keys or any(value != "PASS" for value in checks.values()):
        raise ValueError("check map")
    projection = {"checks": checks,
                  "direct_sha256": hashlib.sha256(canonical(direct)).hexdigest(),
                  "parameter_sha256": hashlib.sha256(canonical(parameter)).hexdigest()}
    return {"candidate_id": "SD-C49", "payload": projection,
            "schema": "paper47-exact-comparison-v1", "status": "PASS"}


def main() -> None:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--direct")
    parser.add_argument("--parameter")
    parser.add_argument("--validate-model")
    args = parser.parse_args()
    try:
        if args.validate_model is not None:
            if args.direct is not None or args.parameter is not None:
                raise ValueError("mixed modes")
            validate_model(load(Path(args.validate_model).resolve(strict=True)))
            sys.stdout.buffer.write(canonical({"consumer": "X", "schema": "paper47-model-accept-v1",
                                               "status": "PASS"}))
        else:
            if args.direct is None or args.parameter is None:
                raise ValueError("both evaluator paths required")
            sys.stdout.buffer.write(canonical(compare(load(Path(args.direct).resolve(strict=True)),
                                                       load(Path(args.parameter).resolve(strict=True)))))
    except SystemExit:
        raise
    except Exception as exc:
        sys.stderr.write(f"X_ERROR:{type(exc).__name__}\n")
        raise SystemExit(3)


if __name__ == "__main__":
    main()
