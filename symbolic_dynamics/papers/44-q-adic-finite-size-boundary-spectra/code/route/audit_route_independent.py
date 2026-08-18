#!/usr/bin/env python3
"""Physically separate Route verifier that reconstructs the complete card."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import stat
import sys
from pathlib import Path, PurePosixPath
from typing import Any


EVIDENCE = (
    "outputs/audits/external_auditor_mutations.json", "outputs/audits/independence_audit.json",
    "outputs/audits/proof_audit.json", "outputs/audits/source_audit.json",
    "outputs/audits/type_audit.json", "outputs/data/source_packet.json",
    "outputs/results/evaluator_a.json", "outputs/results/evaluator_b.json",
    "outputs/results/exact_comparison.json", "outputs/tests/mutation_results.json",
)


def encode(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=True, indent=2, sort_keys=True,
                       separators=(",", ": ")) + "\n").encode("ascii")


def reject_duplicate(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for name, value in pairs:
        if name in result: raise ValueError("duplicate JSON member")
        result[name] = value
    return result


def same_type_value(a: Any, b: Any) -> bool:
    if type(a) is not type(b): return False
    if isinstance(a, dict):
        return set(a.keys()) == set(b.keys()) and all(same_type_value(a[k], b[k]) for k in a)
    if isinstance(a, list):
        return len(a) == len(b) and all(same_type_value(x, y) for x, y in zip(a, b))
    return a == b


def load_regular_below(base: Path, text: str) -> tuple[dict[str, Any], bytes]:
    candidate = Path(text)
    if not base.is_absolute() or not base.is_dir() or base.is_symlink() or not candidate.is_absolute():
        raise ValueError("bad root or argument")
    root_real = base.resolve(strict=True)
    walker = candidate
    while walker != base:
        if walker == walker.parent or walker.is_symlink(): raise ValueError("symlink or escape")
        walker = walker.parent
    item = candidate.resolve(strict=True)
    metadata = os.lstat(item)
    if root_real not in item.parents or not stat.S_ISREG(metadata.st_mode): raise ValueError("not contained regular")
    raw = item.read_bytes()
    value = json.loads(raw.decode("ascii"), object_pairs_hook=reject_duplicate)
    if type(value) is not dict or raw != encode(value): raise ValueError("not canonical object")
    return value, raw


def collect_evidence(root: Path) -> list[dict[str, Any]]:
    answer = []
    for name in EVIDENCE:
        pure = PurePosixPath(name)
        if pure.is_absolute() or "\\" in name or any(part in ("", ".", "..") for part in pure.parts):
            raise ValueError("nonportable artifact")
        item = root.joinpath(*pure.parts)
        parent = item
        while parent != root:
            if parent.is_symlink(): raise ValueError("artifact symlink")
            parent = parent.parent
        resolved = item.resolve(strict=True)
        mode = os.lstat(resolved).st_mode
        if root.resolve(strict=True) not in resolved.parents or not stat.S_ISREG(mode) \
                or stat.S_IMODE(mode) != 0o644:
            raise ValueError("artifact physical contract")
        answer.append({"kind": "regular", "mode": "0644", "path": name,
                       "sha256": hashlib.sha256(resolved.read_bytes()).hexdigest()})
    return answer


def make_expected(root: Path, science: bytes, state: str, requested_commit: str | None) -> dict[str, Any]:
    if state == "A":
        if requested_commit is not None: raise ValueError("commit forbidden in A")
        src, code, locked, has_manifest = "PREAUTHORITY_NO_COMMIT", "NONE", "NONE", False
    else:
        if type(requested_commit) is not str or re.fullmatch("[0-9a-f]{40}", requested_commit) is None \
                or requested_commit == "0" * 40:
            raise ValueError("exact B commit absent")
        src = code = locked = requested_commit
        has_manifest = True
    result: dict[str, Any] = {}
    result["a0"] = {"arithmetic_controls": ["one_symbol_zero_boundary", "full_shift_zero_boundary", "composite_q_control"], "evidence_status": "MODELING_CHOICE", "verdict": "A0_FAIL"}
    result["a1"] = {"evidence_status": "NOT_TESTABLE", "periodic_orbit_ledger": False, "rational_prime_primitive_support": False, "verdict": "A1_FAIL"}
    result["a2"] = {"determinant_defined": False, "evidence_status": "NOT_TESTABLE", "ordinary_cutoff_generating_function": True, "target_divisor_comparison": False, "trace_family_defined": False, "verdict": "A2_FAIL"}
    result["a3"] = {"evidence_status": "PROVED", "meromorphic_continuation": False, "unit_circle_natural_boundary": "golden_control_only", "verdict": "A3_PARTIAL_ANALYTIC_STRUCTURE", "weil_compression": {"evidence_status": "NOT_TESTABLE", "status": "not_available_no_same_ledger_target_divisor"}}
    result["a4"] = {"evidence_status": "NOT_TESTABLE", "fixed_self_adjoint_hilbert_polya_operator_defined": False, "route_b_readiness": False, "verdict": "A4_FAIL"}
    result["artifact_bindings"] = collect_evidence(root)
    result["artifact_path_base"] = "."
    result["artifact_paths"] = list(EVIDENCE)
    result["authority_integration"] = {"authority_writes": 0, "git_operations": 0, "paper_manifest_present": has_manifest, "state": state}
    result["candidate_id"] = "SD-C46"
    result["claim_boundary"] = "Exact q-adic order-one prefix remainder and complete accumulation image; golden Cantor image and dense radial singularities only. No leading-result novelty, ordinary Minkowski content, determinant, completed divisor, or spectral-operator claim."
    result["code_commit"] = code
    result["evaluation_date"] = "2026-08-18"
    result["external_literature_disposition"] = {"exact_source_collision": "STOP_DUPLICATE_LIVE_CONDITIONAL", "owner": "literature_and_publication_review_not_route_terminal"}
    result["finite_evidence_boundary"] = "FINITE_RESULTS_DO_NOT_PROVE_INFINITE_THEOREMS"
    result["overall_verdict"] = "ROUTE_A_REJECTED"
    result["projection_firewall"] = {"boundary_state_type": "qAdicInverseLimitState", "boundary_value_type": "RealOrderOneRemainder", "cutoff_type": "PositivePrefixCutoff", "marker_type": "OrdinaryPrefixGeneratingMarker", "source_type": "OneSidedMultiplicativeSFT"}
    result["round2_clues"] = []
    result["route_b"] = {"invocation_allowed": False, "reason": "no_same_object_primitive_ledger_completed_divisor_or_operator"}
    result["route_tuple"] = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_PARTIAL_ANALYTIC_STRUCTURE", "A4_FAIL"]
    result["schema"] = "paper44-route-a-v0.3"
    result["science_sha256"] = hashlib.sha256(science).hexdigest()
    result["skill"] = "route-a-evaluator"
    result["skill_version"] = "0.3.0"
    result["source_commit"] = src
    result["source_lock"] = {"code_commit": locked, "object": "multiplicative_shift_of_finite_type_X_A_q", "parameters": "explicit_integer_q_and_primitive_zero_one_A"}
    result["terminal_codes"] = {"determinant_or_zeta_retyping": "TYPE_OWNER_ERROR", "nonprimitive_extension": "STOP_SCOPED", "ordinary_content_claim": "NOT_CURRENTLY_JUSTIFIED", "theorem_counterexample": "THEOREM_STOP"}
    return result


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", required=True); ap.add_argument("--route", required=True)
    ap.add_argument("--comparison", required=True); ap.add_argument("--state", choices=("A", "B"), required=True)
    ap.add_argument("--commit")
    ns = ap.parse_args()
    stage = Path(ns.stage)
    route, route_bytes = load_regular_below(stage, ns.route)
    comparison, comparison_bytes = load_regular_below(stage, ns.comparison)
    expected_comparison_envelope = set(comparison) == {"payload", "schema", "status"} \
        and comparison["schema"] == "paper44-exact-comparison-v1" and comparison["status"] == "PASS"
    if not expected_comparison_envelope: raise ValueError("science envelope")
    independently_built = make_expected(stage, comparison_bytes, ns.state, ns.commit)
    if not same_type_value(route, independently_built): raise ValueError("complete Route object mismatch")
    checks = {
        "all_artifacts_physical_and_hash_bound": True,
        "commit_and_manifest_phase_exact": True,
        "no_unrecognized_nested_or_top_level_members": True,
        "publication_and_external_boundaries_exact": True,
        "route_terminal_vocabulary_exact": True,
        "zero_authority_and_git_effects_exact": True,
    }
    sys.stdout.buffer.write(encode({
        "payload": {"checks": checks, "checks_passed": len(checks), "checks_total": len(checks),
                    "route_sha256": hashlib.sha256(route_bytes).hexdigest(), "state": ns.state},
        "schema": "paper44-route-independent-audit-v2", "status": "PASS",
    }))
    return 0


if __name__ == "__main__": raise SystemExit(main())
