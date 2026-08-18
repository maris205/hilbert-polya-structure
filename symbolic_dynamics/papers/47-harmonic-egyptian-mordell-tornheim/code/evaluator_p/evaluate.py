#!/usr/bin/env python3
"""Standalone coprime-scale/divisor-row evaluator P; never uses D's predicate."""

from __future__ import annotations

import argparse
import json
import math
import os
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       separators=(",", ": ")) + "\n").encode("ascii")


def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in pairs:
        if key in out:
            raise ValueError("duplicate JSON key")
        out[key] = value
    return out


def load_json(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    value = json.loads(raw.decode("ascii"), object_pairs_hook=unique)
    if type(value) is not dict or raw != canonical(value):
        raise ValueError("noncanonical JSON")
    return value


def safe_root(text: str) -> Path:
    if type(text) is not str or not os.path.isabs(text):
        raise ValueError("root must be absolute")
    root = Path(text)
    if root.is_symlink() or not root.is_dir() or root.resolve(strict=True) != root:
        raise ValueError("unsafe root")
    for part in [root, *root.parents]:
        if part.is_symlink():
            raise ValueError("symlink root component")
    return root


def rational(value: Fraction) -> dict[str, int]:
    return {"denominator": value.denominator, "numerator": value.numerator}


def divisors(number: int) -> list[int]:
    low: list[int] = []
    high: list[int] = []
    cursor = 1
    while cursor * cursor <= number:
        if number % cursor == 0:
            low.append(cursor)
            if cursor * cursor != number:
                high.append(number // cursor)
        cursor += 1
    return low + list(reversed(high))


def parameter_support(nmax: int) -> tuple[list[list[int]], list[dict[str, int]]]:
    pairs: set[tuple[int, int]] = set()
    coordinates: list[dict[str, int]] = []
    for a in range(1, nmax + 1):
        for b in range(1, nmax + 1):
            if math.gcd(a, b) != 1:
                continue
            base_m = a * (a + b)
            base_n = b * (a + b)
            largest = max(base_m, base_n)
            if largest > nmax:
                continue
            for t in range(1, nmax // largest + 1):
                m, n = t * base_m, t * base_n
                pairs.add((m, n))
                coordinates.append({"a": a, "b": b, "m": m, "n": n,
                                    "quotient": t * a * b, "t": t})
    coordinates.sort(key=lambda row: (row["m"], row["n"], row["t"], row["a"], row["b"]))
    return [list(pair) for pair in sorted(pairs)], coordinates


def divisor_row(m: int) -> list[int]:
    # Independent harmonic-quotient elimination; no direct edge test occurs.
    return sorted((m * m) // d - m for d in divisors(m * m) if d < m)


def closed_walks(nmax: int, length: int, adjacency: dict[int, list[int]]) -> list[list[int]]:
    answer: list[list[int]] = []

    def extend(start: int, current: int, left: int, word: tuple[int, ...]) -> None:
        if left == 0:
            if current == start:
                answer.append(list(word[:-1]))
            return
        for nxt in adjacency[current]:
            extend(start, nxt, left - 1, (*word, nxt))

    for start in range(1, nmax + 1):
        extend(start, start, length, (start,))
    answer.sort()
    return answer


def harmonic(cutoff: int, exponent: int) -> Fraction:
    return sum((Fraction(1, t ** exponent) for t in range(1, cutoff + 1)), Fraction())


def trace_from_walks(words: list[list[int]], s: int) -> Fraction:
    result = Fraction()
    for word in words:
        denominator = math.prod(vertex ** s for vertex in word)
        result += Fraction(1, denominator)
    return result


def finite_scale_trace(nmax: int, s: int) -> Fraction:
    result = Fraction()
    for a in range(1, nmax + 1):
        for b in range(1, nmax + 1):
            if math.gcd(a, b) != 1:
                continue
            cutoff = nmax // ((a + b) * max(a, b))
            if cutoff:
                base = a * b * (a + b) ** 2
                result += Fraction(1, base ** s) * harmonic(cutoff, 2 * s)
    return result


def rectangular_control(bound: int, s: int) -> tuple[Fraction, Fraction]:
    unrestricted = sum(
        (Fraction(1, (p * q * (p + q) ** 2) ** s)
         for p in range(1, bound + 1) for q in range(1, bound + 1)), Fraction())
    primitive = Fraction()
    for u in range(1, bound + 1):
        for v in range(1, bound + 1):
            if math.gcd(u, v) == 1:
                scale = bound // max(u, v)
                primitive += Fraction(1, (u * v * (u + v) ** 2) ** s) * harmonic(scale, 4 * s)
    return unrestricted, primitive


def endpoint_controls() -> dict[str, Any]:
    grid = [(0, 1), (1, 4), (1, 2), (3, 4), (1, 1), (5, 4), (2, 1)]
    diagnostics = []
    for numerator, denominator in grid:
        diagnostics.append({
            "bounded_compact": numerator > 0,
            "det2": 2 * numerator > denominator,
            "diagnostic_kind": "PROOF_BACKED_EXACT_DOMAIN_DIAGNOSTIC",
            "hilbert_schmidt": 2 * numerator > denominator,
            "ordinary_determinant": numerator > denominator,
            "sigma": {"denominator": denominator, "numerator": numerator},
            "trace_class": numerator > denominator
        })
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    product = 1
    squarefree = []
    for count, prime in enumerate(primes, 1):
        product *= prime
        squarefree.append({"degree": (3 ** count - 1) // 2, "m": product,
                           "omega": count, "tau_m_squared": 3 ** count})
    return {
        "interval_diagnostics": diagnostics,
        "squarefree_degree_controls": squarefree,
        "strict_endpoint_witnesses": {
            "bounded_at_zero": "UNBOUNDED_SQUAREFREE_DEGREES",
            "hilbert_schmidt_at_one_half": "EVEN_LOOP_HARMONIC_SCALE_DIVERGENCE",
            "trace_class_at_one": "EVEN_DIAGONAL_HARMONIC_DIVERGENCE"
        }
    }


def reject(code: str) -> None:
    sys.stdout.buffer.write(canonical({
        "consumer": "P", "rejection_code": code,
        "schema": "paper47-mutation-rejection-v1", "status": "REJECT"
    }))
    raise SystemExit(2)


def validate_model(model: dict[str, Any]) -> None:
    expected_keys = {
        "bounded_domain", "candidate_id", "coprime_required", "determinant_domains",
        "edge_parameterization", "hilbert_schmidt_domain", "loops", "mixed_triangle",
        "mt_novelty_claimed", "operator_positive_semidefinite", "ordered_edge_multiplier",
        "primitive_mt_factor", "relation", "scale_factor", "temporal_primitive",
        "trace_class_domain"
    }
    if set(model) != expected_keys:
        reject("SCIENCE_MODEL_SHAPE_FAILURE")
    if model["relation"] != "m_plus_n_divides_m_times_n":
        reject("SOURCE_RELATION_CHANGED")
    if model["loops"] != "retain_even_exactly":
        reject("LOOP_CONVENTION_CHANGED")
    if type(model["coprime_required"]) is not bool or model["coprime_required"] is not True:
        reject("EDGE_PARAMETERIZATION_NONUNIQUE")
    if model["edge_parameterization"] != "g_equals_t_times_a_plus_b":
        reject("EDGE_PARAMETERIZATION_FALSE")
    if model["bounded_domain"] != "Re_s_gt_0":
        reject("UNBOUNDED_DEGREE_ENDPOINT")
    if model["hilbert_schmidt_domain"] != "Re_s_gt_one_half":
        reject("LOOP_SCALE_HS_DIVERGENCE")
    if model["trace_class_domain"] != "Re_s_gt_1":
        reject("EVEN_DIAGONAL_TRACE_DIVERGENCE")
    if model["scale_factor"] != "zeta_2s":
        reject("SECOND_TRACE_SCALE_FAILURE")
    if model["primitive_mt_factor"] != "divide_by_zeta_4s":
        reject("PRIMITIVE_MT_FACTOR_FAILURE")
    if type(model["ordered_edge_multiplier"]) is not int or model["ordered_edge_multiplier"] != 1:
        reject("ORDERED_EDGE_MULTIPLICITY_FAILURE")
    if type(model["mixed_triangle"]) is not list or model["mixed_triangle"] != [15, 30, 60] \
            or any(type(x) is not int for x in model["mixed_triangle"]):
        reject("SUPPORT_WITNESS_FAILURE")


def evaluate(root: Path) -> dict[str, Any]:
    cases = load_json(root / "contracts/CASE_REGISTRY.json")
    model = load_json(root / "contracts/SCIENCE_MODEL.json")
    validate_model(model)
    cutoff_records: list[dict[str, Any]] = []
    coordinates_by_n: list[dict[str, Any]] = []
    support_by_n: dict[int, list[list[int]]] = {}
    for nmax in cases["ordered_vertex_cutoffs"]:
        edges, coordinates = parameter_support(nmax)
        support_by_n[nmax] = edges
        coordinate_map = {(row["m"], row["n"]): row["quotient"] for row in coordinates}
        cutoff_records.append({
            "N": nmax,
            "loops": sorted(m for m, n in map(tuple, edges) if m == n),
            "ordered_edges": edges,
            "ordered_harmonic_quotients": [
                {"m": m, "n": n, "quotient": coordinate_map[(m, n)]} for m, n in map(tuple, edges)
            ]
        })
        coordinates_by_n.append({"N": nmax, "ordered_coordinates": coordinates})

    matrices: list[dict[str, Any]] = []
    walks_records: list[dict[str, Any]] = []
    trace_records: list[dict[str, Any]] = []
    for nmax in cases["closed_walk_cutoffs"]:
        edge_set = {tuple(pair) for pair in support_by_n[nmax]}
        adjacency = {m: sorted(n for x, n in edge_set if x == m) for m in range(1, nmax + 1)}
        matrices.append({
            "N": nmax,
            "entries": [[1 if (m, n) in edge_set else 0 for n in range(1, nmax + 1)]
                        for m in range(1, nmax + 1)]
        })
        for length in cases["closed_walk_lengths"]:
            words = closed_walks(nmax, length, adjacency)
            walks_records.append({"N": nmax, "length": length, "vertex_words": words})
            for s in cases["trace_parameters"]:
                trace_records.append({
                    "N": nmax, "method": "parameter_support_based_walk_enumeration",
                    "power": length, "s": s, "value": rational(trace_from_walks(words, s))
                })

    trace_summary: list[dict[str, Any]] = []
    for nmax in cases["ordered_vertex_cutoffs"]:
        edges = support_by_n[nmax]
        for s in cases["trace_parameters"]:
            first = Fraction(1, 2 ** s) * harmonic(nmax // 2, s)
            ordered = sum((Fraction(1, (m * n) ** s) for m, n in map(tuple, edges)), Fraction())
            scaled = finite_scale_trace(nmax, s)
            if ordered != scaled:
                raise ValueError("finite termwise scale trace mismatch")
            trace_summary.append({
                "N": nmax, "s": s,
                "trace_1_even_harmonic": rational(first),
                "trace_2_parameter_ordered_edges": rational(ordered),
                "trace_2_termwise_scale_cutoff": rational(scaled)
            })

    rectangular: list[dict[str, Any]] = []
    for bound in cases["rectangular_mt_cutoffs"]:
        for s in cases["trace_parameters"]:
            full, primitive = rectangular_control(bound, s)
            if full != primitive:
                raise ValueError("rectangular gcd extraction mismatch")
            rectangular.append({"B": bound, "domain": "rectangular_p_q_le_B", "s": s,
                                "unrestricted": rational(full), "primitive_scaled": rational(primitive)})

    payload = {
        "adjacency_matrices": matrices,
        "complex_phase_certificate": {
            "factorization": "E_sigma_plus_i_tau_equals_U_tau_E_sigma_U_tau",
            "nonreal_operator_hermitian": False,
            "singular_values_depend_only_on": "Re_s",
            "two_sided_unitary_invariance": True
        },
        "coordinates": coordinates_by_n,
        "cutoffs": cutoff_records,
        "endpoint_controls": endpoint_controls(),
        "evidence_class": cases["evidence_class"],
        "phase_certificate": {
            "bounded_compact": "Re_s_gt_0", "det2": "Re_s_gt_one_half",
            "hilbert_schmidt": "Re_s_gt_one_half", "ordinary_determinant": "Re_s_gt_1",
            "proof_owner": "preauthority/PROOF_PACKAGE.md", "trace_class": "Re_s_gt_1"
        },
        "rectangular_mt_controls": rectangular,
        "rows": [{"m": m, "neighbors": divisor_row(m)}
                 for m in range(1, cases["row_maximum"] + 1)],
        "trace_powers": trace_records,
        "trace_summary": trace_summary,
        "walks": walks_records
    }
    return {"candidate_id": "SD-C49", "payload": payload,
            "schema": "paper47-evaluator-p-v1", "status": "PASS"}


def main() -> None:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--root")
    modes.add_argument("--validate-model")
    arguments = parser.parse_args()
    try:
        if arguments.validate_model is not None:
            validate_model(load_json(Path(arguments.validate_model).resolve(strict=True)))
            sys.stdout.buffer.write(canonical({"consumer": "P", "schema": "paper47-model-accept-v1",
                                               "status": "PASS"}))
        else:
            sys.stdout.buffer.write(canonical(evaluate(safe_root(arguments.root))))
    except SystemExit:
        raise
    except Exception as exc:
        sys.stderr.write(f"P_ERROR:{type(exc).__name__}\n")
        raise SystemExit(3)


if __name__ == "__main__":
    main()
