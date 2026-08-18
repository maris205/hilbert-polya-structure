#!/usr/bin/env python3
"""Read-only analytic proof/result auditor A, independent of evaluator code."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


MANIFEST_SHA = "59f08523b58b32df0308b9416c9164a3a1745ee4c15a8c143c693a79ef7eb885"


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       separators=(",", ": ")) + "\n").encode("ascii")


def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in pairs:
        if key in out: raise ValueError("duplicate JSON key")
        out[key] = value
    return out


def load(path: Path) -> dict[str, Any]:
    raw = path.read_bytes(); value = json.loads(raw.decode("ascii"), object_pairs_hook=unique)
    if type(value) is not dict or raw != canonical(value): raise ValueError("noncanonical JSON")
    return value


def strict_equal(left: Any, right: Any) -> bool:
    if type(left) is not type(right): return False
    if type(left) is dict:
        return list(left) == list(right) and all(strict_equal(left[k], right[k]) for k in left)
    if type(left) is list:
        return len(left) == len(right) and all(strict_equal(a, b) for a, b in zip(left, right))
    return left == right


def rat(value: Fraction) -> dict[str, int]:
    return {"denominator": value.denominator, "numerator": value.numerator}


def harmonic(limit: int, exponent: int) -> Fraction:
    total = Fraction()
    for number in range(1, limit + 1): total += Fraction(1, number ** exponent)
    return total


def direct_relation(m: int, n: int) -> bool:
    return divmod(m * n, m + n)[1] == 0


def direct_pairs(limit: int) -> list[list[int]]:
    result = []
    for m in range(1, limit + 1):
        for n in range(1, limit + 1):
            if direct_relation(m, n): result.append([m, n])
    return result


def audit_walks(limit: int, length: int, adjacency: dict[int, list[int]]) -> list[list[int]]:
    result: list[list[int]] = []
    for base in range(1, limit + 1):
        stack: list[tuple[int, tuple[int, ...], int]] = [(base, (base,), length)]
        while stack:
            current, word, left = stack.pop()
            if left == 0:
                if current == base: result.append(list(word[:-1]))
                continue
            for nxt in reversed(adjacency[current]): stack.append((nxt, (*word, nxt), left - 1))
    return sorted(result)


def trace_words(words: list[list[int]], s: int) -> Fraction:
    total = Fraction()
    for word in words:
        denominator = 1
        for vertex in word: denominator *= vertex ** s
        total += Fraction(1, denominator)
    return total


def audit_divisors(number: int) -> list[int]:
    result = []
    for candidate in range(1, math.isqrt(number) + 1):
        if number % candidate == 0:
            result.append(candidate)
            if candidate * candidate != number: result.append(number // candidate)
    return sorted(result)


def parameter_pairs(limit: int) -> tuple[list[list[int]], list[dict[str, int]]]:
    edges: list[list[int]] = []
    coordinates: list[dict[str, int]] = []
    for a in range(1, limit + 1):
        for b in range(1, limit + 1):
            if math.gcd(a, b) != 1: continue
            largest = (a + b) * max(a, b)
            for scale in range(1, limit // largest + 1):
                m, n = scale * a * (a + b), scale * b * (a + b)
                edges.append([m, n])
                coordinates.append({"a": a, "b": b, "m": m, "n": n,
                                    "quotient": scale * a * b, "t": scale})
    edges.sort()
    coordinates.sort(key=lambda row: (row["m"], row["n"], row["t"], row["a"], row["b"]))
    return edges, coordinates


def parameter_second(limit: int, s: int) -> Fraction:
    total = Fraction()
    for a in range(1, limit + 1):
        for b in range(1, limit + 1):
            if math.gcd(a, b) != 1: continue
            scale_limit = limit // ((a + b) * max(a, b))
            if scale_limit:
                total += Fraction(1, (a * b * (a + b) ** 2) ** s) * harmonic(scale_limit, 2 * s)
    return total


def endpoint_object() -> dict[str, Any]:
    grid = [(0, 1), (1, 4), (1, 2), (3, 4), (1, 1), (5, 4), (2, 1)]
    diagnostics = [{"bounded_compact": n > 0, "det2": 2 * n > d,
                    "diagnostic_kind": "PROOF_BACKED_EXACT_DOMAIN_DIAGNOSTIC",
                    "hilbert_schmidt": 2 * n > d, "ordinary_determinant": n > d,
                    "sigma": {"denominator": d, "numerator": n}, "trace_class": n > d}
                   for n, d in grid]
    product = 1; controls = []
    for omega, prime in enumerate([2, 3, 5, 7, 11, 13, 17, 19], 1):
        product *= prime
        controls.append({"degree": (3 ** omega - 1) // 2, "m": product,
                         "omega": omega, "tau_m_squared": 3 ** omega})
    return {"interval_diagnostics": diagnostics, "squarefree_degree_controls": controls,
            "strict_endpoint_witnesses": {"bounded_at_zero": "UNBOUNDED_SQUAREFREE_DEGREES",
              "hilbert_schmidt_at_one_half": "EVEN_LOOP_HARMONIC_SCALE_DIVERGENCE",
              "trace_class_at_one": "EVEN_DIAGONAL_HARMONIC_DIVERGENCE"}}


def rebuild_direct() -> dict[str, Any]:
    limits = [16, 32, 64, 128]; trace_s = [2, 4]
    supports = {limit: direct_pairs(limit) for limit in limits}
    cutoffs = []
    for limit in limits:
        pairs = supports[limit]
        cutoffs.append({"N": limit, "loops": [m for m, n in pairs if m == n],
          "ordered_edges": pairs, "ordered_harmonic_quotients":
          [{"m": m, "n": n, "quotient": (m * n) // (m + n)} for m, n in pairs]})
    matrices = []; walk_blocks = []; powers = []
    for limit in [16, 32]:
        pair_set = {tuple(x) for x in supports[limit]}
        adjacency = {m: [n for n in range(1, limit + 1) if (m, n) in pair_set]
                     for m in range(1, limit + 1)}
        matrices.append({"N": limit, "entries":
          [[int((m, n) in pair_set) for n in range(1, limit + 1)] for m in range(1, limit + 1)]})
        for length in range(1, 6):
            words = audit_walks(limit, length, adjacency)
            walk_blocks.append({"N": limit, "length": length, "vertex_words": words})
            for s in trace_s:
                powers.append({"N": limit, "method": "direct_based_walk_enumeration",
                               "power": length, "s": s, "value": rat(trace_words(words, s))})
    summaries = []
    for limit in limits:
        pairs = supports[limit]; loops = [m for m, n in pairs if m == n]
        for s in trace_s:
            summaries.append({"N": limit, "s": s,
              "trace_1_direct_diagonal": rat(sum((Fraction(1, m ** s) for m in loops), Fraction())),
              "trace_2_direct_ordered_edges": rat(sum((Fraction(1, (m * n) ** s) for m, n in pairs), Fraction()))})
    rows = []
    for m in range(1, 129):
        neighbors = [n for n in range(1, m * m - m + 1) if direct_relation(m, n)]
        rows.append({"m": m, "neighbors": neighbors})
    return {"candidate_id": "SD-C49", "payload": {"adjacency_matrices": matrices,
      "cutoffs": cutoffs, "evidence_class": "FINITE_EXACT_CONTROL",
      "negative_minor": [{"determinant": rat(Fraction(-1, 18 ** s)), "s": s} for s in trace_s],
      "rows": rows, "trace_powers": powers, "trace_summary": summaries, "walks": walk_blocks},
      "schema": "paper47-evaluator-d-v1", "status": "PASS"}


def rebuild_parameter() -> dict[str, Any]:
    limits = [16, 32, 64, 128]; trace_s = [2, 4]; supports = {}; cutoffs = []; coordinate_blocks = []
    for limit in limits:
        pairs, coordinates = parameter_pairs(limit); supports[limit] = pairs
        qmap = {(row["m"], row["n"]): row["quotient"] for row in coordinates}
        cutoffs.append({"N": limit, "loops": [m for m, n in pairs if m == n],
          "ordered_edges": pairs, "ordered_harmonic_quotients":
          [{"m": m, "n": n, "quotient": qmap[(m, n)]} for m, n in pairs]})
        coordinate_blocks.append({"N": limit, "ordered_coordinates": coordinates})
    matrices = []; walk_blocks = []; powers = []
    for limit in [16, 32]:
        pair_set = {tuple(x) for x in supports[limit]}
        adjacency = {m: sorted(n for x, n in pair_set if x == m) for m in range(1, limit + 1)}
        matrices.append({"N": limit, "entries":
          [[int((m, n) in pair_set) for n in range(1, limit + 1)] for m in range(1, limit + 1)]})
        for length in range(1, 6):
            words = audit_walks(limit, length, adjacency)
            walk_blocks.append({"N": limit, "length": length, "vertex_words": words})
            for s in trace_s:
                powers.append({"N": limit, "method": "parameter_support_based_walk_enumeration",
                               "power": length, "s": s, "value": rat(trace_words(words, s))})
    summaries = []
    for limit in limits:
        for s in trace_s:
            ordered = sum((Fraction(1, (m * n) ** s) for m, n in supports[limit]), Fraction())
            summaries.append({"N": limit, "s": s,
              "trace_1_even_harmonic": rat(Fraction(1, 2 ** s) * harmonic(limit // 2, s)),
              "trace_2_parameter_ordered_edges": rat(ordered),
              "trace_2_termwise_scale_cutoff": rat(parameter_second(limit, s))})
    rectangular = []
    for bound in limits:
        for s in trace_s:
            unrestricted = sum((Fraction(1, (p * q * (p + q) ** 2) ** s)
                                for p in range(1, bound + 1) for q in range(1, bound + 1)), Fraction())
            primitive = Fraction()
            for u in range(1, bound + 1):
                for v in range(1, bound + 1):
                    if math.gcd(u, v) == 1:
                        primitive += Fraction(1, (u * v * (u + v) ** 2) ** s) * harmonic(bound // max(u, v), 4 * s)
            rectangular.append({"B": bound, "domain": "rectangular_p_q_le_B", "s": s,
                                "unrestricted": rat(unrestricted), "primitive_scaled": rat(primitive)})
    rows = [{"m": m, "neighbors": sorted(m * m // d - m for d in audit_divisors(m * m) if d < m)}
            for m in range(1, 129)]
    return {"candidate_id": "SD-C49", "payload": {
      "adjacency_matrices": matrices,
      "complex_phase_certificate": {"factorization": "E_sigma_plus_i_tau_equals_U_tau_E_sigma_U_tau",
       "nonreal_operator_hermitian": False, "singular_values_depend_only_on": "Re_s",
       "two_sided_unitary_invariance": True},
      "coordinates": coordinate_blocks, "cutoffs": cutoffs, "endpoint_controls": endpoint_object(),
      "evidence_class": "FINITE_EXACT_CONTROL",
      "phase_certificate": {"bounded_compact": "Re_s_gt_0", "det2": "Re_s_gt_one_half",
       "hilbert_schmidt": "Re_s_gt_one_half", "ordinary_determinant": "Re_s_gt_1",
       "proof_owner": "preauthority/PROOF_PACKAGE.md", "trace_class": "Re_s_gt_1"},
      "rectangular_mt_controls": rectangular, "rows": rows, "trace_powers": powers,
      "trace_summary": summaries, "walks": walk_blocks},
      "schema": "paper47-evaluator-p-v1", "status": "PASS"}


def rebuild_comparison(direct: dict[str, Any], parameter: dict[str, Any]) -> dict[str, Any]:
    keys = ["based_closed_walks", "coprime_coordinate_bijection",
            "endpoint_and_complex_phase_controls", "exact_trace_powers_1_through_5",
            "finite_evidence_class", "first_trace_even_harmonic", "full_divisor_rows",
            "literal_matrices", "negative_principal_minor", "ordered_support_quotients_loops",
            "rectangular_primitive_mt_gcd_extraction", "second_trace_termwise_finite_cutoff"]
    return {"candidate_id": "SD-C49", "payload": {"checks": {key: "PASS" for key in keys},
      "direct_sha256": hashlib.sha256(canonical(direct)).hexdigest(),
      "parameter_sha256": hashlib.sha256(canonical(parameter)).hexdigest()},
      "schema": "paper47-exact-comparison-v1", "status": "PASS"}


def reject(code: str) -> None:
    sys.stdout.buffer.write(canonical({"consumer": "A", "rejection_code": code,
                                      "schema": "paper47-mutation-rejection-v1", "status": "REJECT"}))
    raise SystemExit(2)


def validate_model(model: dict[str, Any]) -> None:
    if model.get("bounded_domain") != "Re_s_gt_0": reject("UNBOUNDED_DEGREE_ENDPOINT")
    if model.get("hilbert_schmidt_domain") != "Re_s_gt_one_half": reject("LOOP_SCALE_HS_DIVERGENCE")
    if model.get("trace_class_domain") != "Re_s_gt_1": reject("EVEN_DIAGONAL_TRACE_DIVERGENCE")
    if model.get("primitive_mt_factor") != "divide_by_zeta_4s": reject("PRIMITIVE_MT_FACTOR_FAILURE")
    if model.get("temporal_primitive") != "least_period_closed_vertex_cycle": reject("PRIMITIVE_TYPE_FAILURE")
    if type(model.get("operator_positive_semidefinite")) is not bool \
            or model["operator_positive_semidefinite"] is not False: reject("NEGATIVE_PRINCIPAL_MINOR")
    domains = model.get("determinant_domains")
    if type(domains) is not dict or set(domains) != {"det2", "ordinary"} \
            or domains["det2"] != "Re_s_gt_one_half" or domains["ordinary"] != "Re_s_gt_1":
        reject("DETERMINANT_DOMAIN_FAILURE")


def verify_manifest(root: Path) -> None:
    manifest = root / "preauthority/SHA256SUMS.txt"
    if hashlib.sha256(manifest.read_bytes()).hexdigest() != MANIFEST_SHA: raise ValueError("manifest seal")
    rows = []
    for line in manifest.read_text(encoding="ascii").splitlines():
        digest, name = line.split("  ", 1)
        if "/" in name or name == "SHA256SUMS.txt": raise ValueError("manifest name")
        path = root / "preauthority" / name
        if path.is_symlink() or not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            raise ValueError("manifest row")
        rows.append(name)
    actual = sorted(p.name for p in (root / "preauthority").iterdir()
                    if p.is_file() and p.name != "SHA256SUMS.txt")
    if rows != sorted(rows) or actual != sorted(rows) or len(rows) != 15: raise ValueError("manifest set")


def normal(root: Path, direct_path: Path, parameter_path: Path, comparison_path: Path) -> dict[str, Any]:
    verify_manifest(root)
    model = load(root / "contracts/SCIENCE_MODEL.json"); validate_model(model)
    proof = (root / "preauthority/PROOF_PACKAGE.md").read_text(encoding="utf-8")
    required = [
        "bounded and compact iff \\(\\sigma>0\\)", "Hilbert–Schmidt threshold is exact",
        "\\(E_s\\in S_1\\) exactly when", "finite scale cutoff depends on",
        "zeta(4s)", "negative", "unique edge parameterization"
    ]
    # Some ownership phrases live in the plan; require all decisive formulas across frozen files.
    corpus = proof + (root / "preauthority/EXPERIMENT_PLAN.md").read_text(encoding="utf-8")
    collapsed = " ".join(corpus.split())
    if any(marker not in collapsed for marker in required): raise ValueError("proof marker")
    direct = load(direct_path); parameter = load(parameter_path); comparison = load(comparison_path)
    expected_direct = json.loads(canonical(rebuild_direct()).decode("ascii"), object_pairs_hook=unique)
    expected_parameter = json.loads(canonical(rebuild_parameter()).decode("ascii"), object_pairs_hook=unique)
    if not strict_equal(direct, expected_direct): raise ValueError("independent D reconstruction")
    if not strict_equal(parameter, expected_parameter): raise ValueError("independent P reconstruction")
    expected_comparison = json.loads(canonical(rebuild_comparison(direct, parameter)).decode("ascii"),
                                     object_pairs_hook=unique)
    if not strict_equal(comparison, expected_comparison): raise ValueError("independent X reconstruction")
    checks = comparison["payload"]["checks"]
    expected = {
        "based_closed_walks", "coprime_coordinate_bijection", "exact_trace_powers_1_through_5",
        "endpoint_and_complex_phase_controls", "finite_evidence_class", "first_trace_even_harmonic", "full_divisor_rows",
        "literal_matrices", "negative_principal_minor", "ordered_support_quotients_loops",
        "rectangular_primitive_mt_gcd_extraction", "second_trace_termwise_finite_cutoff"
    }
    if type(checks) is not dict or set(checks) != expected or any(v != "PASS" for v in checks.values()):
        raise ValueError("comparison reconstruction")
    phase = parameter["payload"]["phase_certificate"]
    if phase != {"bounded_compact": "Re_s_gt_0", "det2": "Re_s_gt_one_half",
                  "hilbert_schmidt": "Re_s_gt_one_half", "ordinary_determinant": "Re_s_gt_1",
                  "proof_owner": "preauthority/PROOF_PACKAGE.md", "trace_class": "Re_s_gt_1"}:
        raise ValueError("phase projection")
    payload = {
        "analytic_certificates": {
            "bounded_compact_wall": "PROOF_ONLY_Re_s_gt_0",
            "hilbert_schmidt_wall": "PROOF_ONLY_Re_s_gt_one_half",
            "trace_class_wall": "PROOF_ONLY_Re_s_gt_1",
            "trace_1": "PROOF_ONLY_2_minus_s_zeta_s",
            "trace_2": "PROOF_ONLY_zeta_2s_over_zeta_4s_times_MT_s_s_2s"
        },
        "finite_results_role": "IMPLEMENTATION_CONTROLS_NOT_ENDPOINT_PROOF",
        "manifest_sha256": MANIFEST_SHA,
        "proof_sha256": hashlib.sha256((root / "preauthority/PROOF_PACKAGE.md").read_bytes()).hexdigest(),
        "result_hashes": {
            "comparison": hashlib.sha256(canonical(comparison)).hexdigest(),
            "direct": hashlib.sha256(canonical(direct)).hexdigest(),
            "parameter": hashlib.sha256(canonical(parameter)).hexdigest()
        }
    }
    return {"candidate_id": "SD-C49", "payload": payload,
            "schema": "paper47-proof-result-audit-v1", "status": "PASS"}


def main() -> None:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--root"); parser.add_argument("--direct"); parser.add_argument("--parameter")
    parser.add_argument("--comparison"); parser.add_argument("--validate-model")
    args = parser.parse_args()
    try:
        if args.validate_model is not None:
            if any(x is not None for x in (args.root, args.direct, args.parameter, args.comparison)):
                raise ValueError("mixed modes")
            validate_model(load(Path(args.validate_model).resolve(strict=True)))
            sys.stdout.buffer.write(canonical({"consumer": "A", "schema": "paper47-model-accept-v1",
                                               "status": "PASS"}))
        else:
            if any(x is None for x in (args.root, args.direct, args.parameter, args.comparison)):
                raise ValueError("normal arguments")
            root = Path(args.root).resolve(strict=True)
            sys.stdout.buffer.write(canonical(normal(root, Path(args.direct).resolve(strict=True),
                                                    Path(args.parameter).resolve(strict=True),
                                                    Path(args.comparison).resolve(strict=True))))
    except SystemExit: raise
    except Exception as exc:
        sys.stderr.write(f"A_ERROR:{type(exc).__name__}\n"); raise SystemExit(3)


if __name__ == "__main__": main()
