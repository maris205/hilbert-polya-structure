#!/usr/bin/env python3
"""Standalone direct evaluator D for Paper 47; no project-local imports."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import stat
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


def edge(m: int, n: int) -> bool:
    """The sole D support constructor."""
    return (m * n) % (m + n) == 0


def support(nmax: int) -> list[list[int]]:
    return [[m, n] for m in range(1, nmax + 1) for n in range(1, nmax + 1)
            if edge(m, n)]


def full_row(m: int) -> list[int]:
    # If n is adjacent then n=m^2/d-m for 1<=d<m, hence n<=m^2-m.
    # D uses only this exhaustive integer range and its literal predicate.
    return [n for n in range(1, m * m - m + 1) if edge(m, n)]


def closed_walks(nmax: int, length: int, adjacency: dict[int, list[int]]) -> list[list[int]]:
    answer: list[list[int]] = []

    def visit(start: int, current: int, left: int, word: list[int]) -> None:
        if left == 0:
            if current == start:
                answer.append(word[:-1])
            return
        for nxt in adjacency[current]:
            visit(start, nxt, left - 1, [*word, nxt])

    for start in range(1, nmax + 1):
        visit(start, start, length, [start])
    answer.sort()
    return answer


def exact_trace(words: list[list[int]], s: int) -> Fraction:
    total = Fraction(0, 1)
    for word in words:
        denominator = 1
        for vertex in word:
            denominator *= vertex ** s
        total += Fraction(1, denominator)
    return total


def reject(code: str) -> None:
    sys.stdout.buffer.write(canonical({
        "consumer": "D", "rejection_code": code,
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
    if model["scale_factor"] != "zeta_2s":
        reject("SECOND_TRACE_SCALE_FAILURE")
    if type(model["ordered_edge_multiplier"]) is not int or model["ordered_edge_multiplier"] != 1:
        reject("ORDERED_EDGE_MULTIPLICITY_FAILURE")
    if type(model["operator_positive_semidefinite"]) is not bool \
            or model["operator_positive_semidefinite"] is not False:
        reject("NEGATIVE_PRINCIPAL_MINOR")
    if type(model["mixed_triangle"]) is not list or model["mixed_triangle"] != [15, 30, 60] \
            or any(type(x) is not int for x in model["mixed_triangle"]):
        reject("SUPPORT_WITNESS_FAILURE")


def evaluate(root: Path) -> dict[str, Any]:
    cases = load_json(root / "contracts/CASE_REGISTRY.json")
    model = load_json(root / "contracts/SCIENCE_MODEL.json")
    validate_model(model)
    cutoff_records: list[dict[str, Any]] = []
    support_by_n: dict[int, list[list[int]]] = {}
    for nmax in cases["ordered_vertex_cutoffs"]:
        edges = support(nmax)
        support_by_n[nmax] = edges
        cutoff_records.append({
            "N": nmax,
            "loops": [m for m in range(1, nmax + 1) if edge(m, m)],
            "ordered_edges": edges,
            "ordered_harmonic_quotients": [
                {"m": m, "n": n, "quotient": (m * n) // (m + n)} for m, n in edges
            ]
        })

    matrices: list[dict[str, Any]] = []
    walk_records: list[dict[str, Any]] = []
    trace_records: list[dict[str, Any]] = []
    for nmax in cases["closed_walk_cutoffs"]:
        edge_set = {tuple(pair) for pair in support_by_n[nmax]}
        adjacency = {m: [n for n in range(1, nmax + 1) if (m, n) in edge_set]
                     for m in range(1, nmax + 1)}
        matrices.append({
            "N": nmax,
            "entries": [[1 if (m, n) in edge_set else 0 for n in range(1, nmax + 1)]
                        for m in range(1, nmax + 1)]
        })
        for length in cases["closed_walk_lengths"]:
            words = closed_walks(nmax, length, adjacency)
            walk_records.append({"N": nmax, "length": length, "vertex_words": words})
            for s in cases["trace_parameters"]:
                trace_records.append({
                    "N": nmax, "method": "direct_based_walk_enumeration", "power": length,
                    "s": s, "value": rational(exact_trace(words, s))
                })

    first_second: list[dict[str, Any]] = []
    for nmax, edges in sorted(support_by_n.items()):
        loops = [m for m in range(1, nmax + 1) if edge(m, m)]
        for s in cases["trace_parameters"]:
            tr1 = sum((Fraction(1, m ** s) for m in loops), Fraction())
            tr2 = sum((Fraction(1, (m * n) ** s) for m, n in edges), Fraction())
            first_second.append({
                "N": nmax, "s": s,
                "trace_1_direct_diagonal": rational(tr1),
                "trace_2_direct_ordered_edges": rational(tr2)
            })

    rows = [{"m": m, "neighbors": full_row(m)} for m in range(1, cases["row_maximum"] + 1)]
    payload = {
        "adjacency_matrices": matrices,
        "cutoffs": cutoff_records,
        "evidence_class": cases["evidence_class"],
        "negative_minor": [
            {"determinant": rational(Fraction(-1, 18 ** s)), "s": s}
            for s in cases["trace_parameters"]
        ],
        "rows": rows,
        "trace_powers": trace_records,
        "trace_summary": first_second,
        "walks": walk_records
    }
    return {"candidate_id": "SD-C49", "payload": payload,
            "schema": "paper47-evaluator-d-v1", "status": "PASS"}


def main() -> None:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--root")
    modes.add_argument("--validate-model")
    arguments = parser.parse_args()
    try:
        if arguments.validate_model is not None:
            validate_model(load_json(Path(arguments.validate_model).resolve(strict=True)))
            sys.stdout.buffer.write(canonical({"consumer": "D", "schema": "paper47-model-accept-v1",
                                               "status": "PASS"}))
        else:
            sys.stdout.buffer.write(canonical(evaluate(safe_root(arguments.root))))
    except SystemExit:
        raise
    except Exception as exc:
        sys.stderr.write(f"D_ERROR:{type(exc).__name__}\n")
        raise SystemExit(3)


if __name__ == "__main__":
    main()
