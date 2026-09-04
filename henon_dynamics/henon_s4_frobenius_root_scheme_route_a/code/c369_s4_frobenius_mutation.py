#!/usr/bin/env python3
"""Hostile repaired-hash mutation suite for HCS-C369."""
from __future__ import annotations

import copy
import hashlib
import json
import sys
import tempfile
from pathlib import Path

from c369_s4_frobenius_checker import EV, YML, check


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def repaired(value):
    value = copy.deepcopy(value)
    value.pop("payload_sha256", None)
    value["payload_sha256"] = hashlib.sha256(canonical(value)).hexdigest()
    return value


def expect_reject_json(value, label, raw=False):
    with tempfile.TemporaryDirectory(prefix="c369-mutation-") as directory:
        path = Path(directory) / "mutant.json"
        if raw:
            path.write_text(value)
        else:
            path.write_text(json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
        try:
            check(path, YML)
        except Exception:
            return
    raise AssertionError(f"surviving JSON mutation: {label}")


def expect_reject_yaml(raw, label):
    with tempfile.TemporaryDirectory(prefix="c369-yaml-") as directory:
        path = Path(directory) / "mutant.yaml"
        path.write_text(raw)
        try:
            check(EV, path)
        except Exception:
            return
    raise AssertionError(f"surviving YAML mutation: {label}")


def path_mutation(base, path, replacement):
    value = copy.deepcopy(base)
    cursor = value
    for key in path[:-1]:
        cursor = cursor[key]
    cursor[path[-1]] = replacement
    return repaired(value)


def main():
    if sys.flags.optimize:
        raise RuntimeError("C369 mutation suite refuses optimized Python")
    base = json.loads(EV.read_text())
    attacks = [
        (("candidate_id",), "HCS-C000", "candidate id"),
        (("obstruction_id",), "HEN-O000", "obstruction id"),
        (("source_commit",), "0" * 40, "source commit"),
        (("fixed_epoch",), 0, "epoch"),
        (("scope_literal",), "OPEN", "scope literal"),
        (("evaluator", "sha256"), "0" * 64, "evaluator hash"),
        (("route_a_yaml", "raw_sha256"), "0" * 64, "yaml raw receipt"),
        (("model", "integral_polynomial"), "x^4+x+1", "model polynomial"),
        (("model", "discriminant"), 283, "discriminant sign"),
        (("model", "good_prime_condition"), "all p", "good prime condition"),
        (("model", "dynamics"), "geometric Frobenius", "Frobenius convention"),
        (("model", "geometric_frobenius_convention"), "same map", "inverse convention"),
        (("galois_proof", "discriminant"), "disc(f)=283", "Galois discriminant"),
        (("galois_proof", "conclusion"), "Gal(f/Q)=A4", "Galois conclusion"),
        (("theorem_contract", "determinant"), "no determinant", "determinant theorem"),
        (("theorem_contract", "ramified_boundary"), "no exceptional prime", "ramified theorem"),
        (("theorem_contract", "density"), "finite frequencies only", "Chebotarev theorem"),
        (("ownership_boundary", "inherited_workspace_owner"), "HCS-C369 owns the universal mechanism", "inherited C12A ownership"),
        (("ownership_boundary", "c369_owner"), "all zero-dimensional Frobenius determinants", "restricted C369 ownership"),
        (("ownership_boundary", "nonownership"), "HCS-C369 claims universal ownership", "universal-mechanism nonownership"),
        (("collision_boundary", "nearest_C12A"), "no collision", "C12A collision boundary"),
        (("class_witnesses", 0, "p"), 3, "first witness prime"),
        (("class_witnesses", 1, "factorization_mod_p"), "x^4-x-1", "witness factorization"),
        (("ramified_boundary", "repeated_root"), 94, "repeated root"),
        (("ramified_boundary", "gcd_f_fprime_coefficients_mod_p"), [189, 1], "ramified gcd"),
        (("class_atlas", 0, "s4_conjugacy_class_size"), 2, "class size"),
        (("class_atlas", 4, "det_I_minus_uP_coefficients"), [1, -1], "atlas determinant"),
        (("prime_rows", 0, "factor_degree_partition"), [1, 3], "prime partition"),
        (("prime_rows", 1, "fixed_counts_r1_to_r12"), [0] * 12, "fixed ledger"),
        (("prime_rows", 2, "primitive_cycle_counts_r1_to_r12"), [1] * 12, "primitive ledger"),
        (("prime_rows", 3, "koopman_unitary"), False, "unitarity"),
        (("prime_rows", 4, "koopman_self_adjoint"), True, "self-adjoint boundary"),
        (("enumeration", "good_primes"), 1229, "good count"),
        (("enumeration", "class_counts", "4"), 320, "class count"),
        (("route_a", "tuple"), ["A0_FAIL"] * 5, "route tuple"),
        (("route_a", "overall"), "ROUTE_A_REJECTED", "route verdict"),
        (("route_a", "route_b_invocation_allowed"), True, "route B"),
        (("scope_flags", "claims_target_euler_factors"), True, "forbidden flag"),
    ]
    count = 0
    for path, replacement, label in attacks:
        expect_reject_json(path_mutation(base, path, replacement), label)
        count += 1

    deleted = copy.deepcopy(base)
    del deleted["model"]
    expect_reject_json(repaired(deleted), "deleted top-level key")
    count += 1
    extra = copy.deepcopy(base)
    extra["surprise"] = 1
    expect_reject_json(repaired(extra), "extra top-level key")
    count += 1
    truncated = copy.deepcopy(base)
    truncated["prime_rows"] = truncated["prime_rows"][:-1]
    expect_reject_json(repaired(truncated), "truncated prime ledger")
    count += 1
    reordered = copy.deepcopy(base)
    reordered["prime_rows"][0], reordered["prime_rows"][1] = reordered["prime_rows"][1], reordered["prime_rows"][0]
    expect_reject_json(repaired(reordered), "reordered prime ledger")
    count += 1
    stale = copy.deepcopy(base)
    stale["candidate_id"] = "HCS-C000"
    expect_reject_json(stale, "stale outer hash")
    count += 1
    expect_reject_json('{"candidate_id":"a","candidate_id":"b"}', "duplicate JSON key", raw=True)
    count += 1
    expect_reject_json('{"payload_sha256":NaN}', "nonfinite JSON", raw=True)
    count += 1
    expect_reject_json('[]', "nonmapping JSON root", raw=True)
    count += 1

    yraw = YML.read_text()
    expect_reject_yaml(yraw + "candidate_id: duplicate\n", "duplicate YAML key")
    count += 1
    expect_reject_yaml("base: &b {x: 1}\ncopy: *b\n", "YAML alias")
    count += 1
    expect_reject_yaml(yraw.replace("A2_FAIL", "A2_PASS_ANALYTIC", 1), "YAML route gate")
    count += 1
    expect_reject_yaml(yraw.replace("claims_target_zero_match: false", "claims_target_zero_match: true"), "YAML forbidden flag")
    count += 1
    expect_reject_yaml("- not\n- a\n- mapping\n", "YAML root")
    count += 1
    print(f"C369 hostile mutation suite: PASS ({count} attacks)")


if __name__ == "__main__":
    main()
