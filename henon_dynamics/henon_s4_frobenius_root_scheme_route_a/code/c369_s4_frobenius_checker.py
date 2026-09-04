#!/usr/bin/env python3
"""Independent checker for HCS-C369; deliberately never imports the producer."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import yaml
from sympy import primerange
from sympy.polys.domains import ZZ
from sympy.polys.galoistools import gf_factor

ROOT = Path(__file__).resolve().parents[1]
EV = ROOT / "results/c369_s4_frobenius_evidence.json"
YML = ROOT / "evaluations/route_a/HCS-C369/2026-09-04.yaml"
RAW = "421a590612cbe66b3ba3dc7af6c8ee6bbca83a465343c9eb19b852e323d2cd13"
SEMANTIC = "36f2d0a42d65a3f1def14c18cf7fd5601c049c02477a7f4c5e89edae0369f731"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SOURCE = "c6553f02d928c6aa05400ded57746869a85f0238"
ROUTE = ["A0_STRUCTURAL_ARITHMETIC_RELATION", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"]
TOP = {
    "schema", "candidate_id", "obstruction_id", "evaluation_date", "source_commit", "fixed_epoch",
    "scope_literal", "evaluator", "route_a_yaml", "model", "galois_proof", "theorem_contract",
    "ownership_boundary", "finite_evidence_role", "class_witnesses", "ramified_boundary", "class_atlas", "prime_rows",
    "enumeration", "collision_boundary", "nonclaims", "references", "route_a", "scope_flags", "payload_sha256",
}
ROW_KEYS = {
    "p", "factor_degree_partition", "cycle_type", "s4_conjugacy_class_size", "chebotarev_density",
    "fixed_counts_r1_to_r12", "primitive_point_counts_r1_to_r12", "primitive_cycle_counts_r1_to_r12",
    "det_I_minus_uP_coefficients", "koopman_unitary", "koopman_self_adjoint",
}


class Loader(yaml.SafeLoader):
    pass


Loader.yaml_implicit_resolvers = {
    k: [(tag, regex) for tag, regex in values if tag != "tag:yaml.org,2002:timestamp"]
    for k, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def strict_mapping(loader, node, deep=False):
    out = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge key")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in out:
            raise ValueError("duplicate/non-string YAML key")
        out[key] = loader.construct_object(value_node, deep=deep)
    return out


Loader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, strict_mapping)


def strict_json(path):
    def unique(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError("duplicate JSON key")
            out[key] = value
        return out
    return json.loads(path.read_text(), object_pairs_hook=unique, parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))


def strict_yaml(path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML aliases forbidden")
    value = yaml.load(raw, Loader=Loader)
    if type(value) is not dict:
        raise TypeError("YAML root")
    return value


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def same(left, right):
    if type(left) is not type(right):
        return False
    if type(left) is dict:
        return set(left) == set(right) and all(same(left[key], right[key]) for key in left)
    if type(left) is list:
        return len(left) == len(right) and all(same(a, b) for a, b in zip(left, right))
    return left == right


def require_keys(value, expected):
    if type(value) is not dict or set(value) != set(expected):
        raise AssertionError(f"schema drift: {set(value) if type(value) is dict else type(value)}")


def partition_by_independent_factorization(p):
    unit, factors = gf_factor([1, 0, 0, -1, -1], p, ZZ)
    if unit % p != 1:
        raise AssertionError("unexpected factorization unit")
    return tuple(sorted(degree for coeffs, multiplicity in factors for degree in [len(coeffs) - 1] for _ in range(multiplicity)))


CLASS = {
    (1, 1, 1, 1): ("1+1+1+1", 1, "1/24"),
    (1, 1, 2): ("2+1+1", 6, "1/4"),
    (2, 2): ("2+2", 3, "1/8"),
    (1, 3): ("3+1", 8, "1/3"),
    (4,): ("4", 6, "1/4"),
}
OWNERSHIP_BOUNDARY = {
    "inherited_workspace_owner": "HCS-C12A owns the universal zero-dimensional Frobenius finite-permutation fixed-point and finite zeta/determinant mechanism",
    "c369_owner": "x^4-x-1 S4 Galois proof, five-class all-good-prime factor/fixed/primitive/density atlas, p=283 non-etale boundary, and convention-locked executable ledger",
    "nonownership": "HCS-C369 does not claim workspace ownership of the universal finite-permutation zeta/determinant mechanism",
}
COLLISION_BOUNDARY = {
    "nearest_C12A": "C12A owns the universal zero-dimensional Frobenius finite-permutation fixed-point and finite zeta/determinant mechanism; C369 owns only the x^4-x-1 S4 all-good-prime factor/fixed/primitive/density atlas, p=283 boundary, and convention-locked executable ledger",
    "nearest_C19": "period-seven Henon ordered-edge curve with a two-axis chronology/Frobenius problem; C369 is the autonomous Frobenius permutation on a quartic zero-dimensional root scheme",
    "nearest_C41": "a cubic CM elliptic Frobenius bridge with cohomological degree-two factors; C369 classifies four-point permutation fibers and primitive cycles",
    "nearest_C56": "a degree-27 finite-etale Fano line scheme with W(E6) normal-closure action and selected Frobenius witnesses; C369 gives the all-good-prime S4 atlas for one quartic root scheme",
    "nearest_C172": "a primitive finite-field multiplier on field elements with a fixed point and a large cycle; C369 instead varies S4 root fibers over rational primes",
    "nearest_C364": "a finite Gauss reduction permutation without rational-prime fibers; C369 has an intrinsic integral root scheme and Chebotarev classes",
}
NONCLAIMS = [
    "no workspace ownership of the universal zero-dimensional finite-permutation zeta/determinant mechanism already owned by C12A",
    "no single autonomous dynamical owner across primes",
    "no cross-prime Fredholm direct sum or trace-class statement",
    "no target Euler product or target arithmetic local factors",
    "no target continuation, functional equation, divisor, or zero fit",
    "no Hilbert-Polya operator; fiber Koopman operators are finite-dimensional permutation unitaries",
    "no priority claim for the classical Dedekind or Chebotarev theorems",
]
REFERENCES = [
    "J.-P. Serre, Topics in Galois Theory, second edition",
    "J. Neukirch, Algebraic Number Theory",
    "R. Lidl and H. Niederreiter, Finite Fields",
    "HCS-C12A, internal workspace ownership record for the universal zero-dimensional Frobenius finite-permutation mechanism",
]


def multiply(left, right):
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def denominator(partition):
    out = [1]
    for length in partition:
        factor = [0] * (length + 1)
        factor[0], factor[-1] = 1, -1
        out = multiply(out, factor)
    return out


def expected_row(p):
    partition = partition_by_independent_factorization(p)
    if partition not in CLASS:
        raise AssertionError(f"unexpected partition at p={p}: {partition}")
    label, class_size, density = CLASS[partition]
    fixed = [sum(length for length in partition if r % length == 0) for r in range(1, 13)]
    cycles = [partition.count(r) for r in range(1, 13)]
    points = [r * cycles[r - 1] for r in range(1, 13)]
    return {
        "p": p,
        "factor_degree_partition": list(partition),
        "cycle_type": label,
        "s4_conjugacy_class_size": class_size,
        "chebotarev_density": density,
        "fixed_counts_r1_to_r12": fixed,
        "primitive_point_counts_r1_to_r12": points,
        "primitive_cycle_counts_r1_to_r12": cycles,
        "det_I_minus_uP_coefficients": denominator(partition),
        "koopman_unitary": True,
        "koopman_self_adjoint": max(partition) <= 2,
    }


def check(evidence=EV, yaml_path=YML):
    checks = 0
    value = strict_json(evidence)
    require_keys(value, TOP)
    checks += 1
    claimed = value.pop("payload_sha256")
    if claimed != hashlib.sha256(canonical(value)).hexdigest():
        raise AssertionError("payload hash")
    value["payload_sha256"] = claimed
    checks += 1
    expected_meta = {
        "schema": "hcs-c369-s4-frobenius-root-scheme-evidence-v2",
        "candidate_id": "HCS-C369",
        "obstruction_id": "HEN-O353",
        "evaluation_date": "2026-09-04",
        "source_commit": SOURCE,
        "fixed_epoch": 1788480000,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
    }
    for key, expected in expected_meta.items():
        if not same(value[key], expected):
            raise AssertionError(f"metadata drift: {key}")
        checks += 1
    if not same(value["evaluator"], {"authority": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR}):
        raise AssertionError("evaluator drift")
    if not same(value["route_a_yaml"], {"relative_path": "evaluations/route_a/HCS-C369/2026-09-04.yaml", "raw_sha256": RAW, "semantic_sha256": SEMANTIC}):
        raise AssertionError("evaluator receipt drift")
    checks += 2

    yml = strict_yaml(yaml_path)
    if hashlib.sha256(yaml_path.read_bytes()).hexdigest() != RAW or hashlib.sha256(canonical(yml)).hexdigest() != SEMANTIC:
        raise AssertionError("YAML hash drift")
    checks += 2
    yml_keys = {
        "schema", "candidate_id", "title", "evaluation_date", "source_commit", "fixed_epoch", "scope_literal",
        "evaluator_authority", "evaluator_version", "evaluator_authority_sha256", "obstruction_id",
        "candidate_definition", "family", "phase_space", "dynamics", "parameters", "parameter_provenance",
        "arithmetic_origin", "clock", "normalization", "determinant_convention", "orbit_cutoff", "precision",
        "training_data", "forbidden_data", "artifact_paths", "a0", "a1", "a2", "a3", "a4", "tuple",
        "overall_verdict", "route_b_invocation_allowed", "route_b_lock_reason", "scope_flags", "theorem_status",
        "finite_evidence_role", "source_owner_tokens",
    }
    require_keys(yml, yml_keys)
    checks += 1
    if yml["candidate_id"] != "HCS-C369" or yml["obstruction_id"] != "HEN-O353" or yml["source_commit"] != SOURCE:
        raise AssertionError("YAML identity")
    if yml["fixed_epoch"] != 1788480000 or yml["scope_literal"] != "NO_BAD_EULER_OR_ROOT_NUMBER":
        raise AssertionError("YAML locks")
    if yml["tuple"] != ROUTE or yml["overall_verdict"] != "ROUTE_A_ARITHMETIC_CANDIDATE" or yml["route_b_invocation_allowed"] is not False:
        raise AssertionError("YAML route")
    checks += 6
    expected_gate_verdicts = {
        "a0": "A0_STRUCTURAL_ARITHMETIC_RELATION",
        "a1": "A1_PASS_ANALYTIC",
        "a2": "A2_FAIL",
        "a3": "A3_FAIL",
        "a4": "A4_NATURAL_QUANTIZATION",
    }
    for gate, verdict in expected_gate_verdicts.items():
        require_keys(yml[gate], {"verdict", "evidence_status", "strongest_evidence", "strongest_failure"})
        if yml[gate]["verdict"] != verdict or not yml[gate]["strongest_evidence"] or not yml[gate]["strongest_failure"]:
            raise AssertionError(f"bad gate {gate}")
        checks += 2
    if any(type(flag) is not bool or flag for flag in yml["scope_flags"].values()):
        raise AssertionError("YAML scope flag")
    checks += len(yml["scope_flags"])

    model = value["model"]
    if model["integral_polynomial"] != "x^4-x-1" or model["discriminant"] != -283 or model["good_prime_condition"] != "p != 283":
        raise AssertionError("model")
    if "arithmetic Frobenius" not in model["dynamics"] or "inverse" not in model["geometric_frobenius_convention"]:
        raise AssertionError("Frobenius convention")
    checks += 5
    proof = value["galois_proof"]
    require_keys(proof, {"irreducibility_witness", "four_cycle_witness", "three_cycle_witness", "discriminant", "conclusion"})
    if proof["discriminant"] != "disc(f)=-283 is not a square" or "S4" not in proof["conclusion"]:
        raise AssertionError("S4 proof receipt")
    checks += 3
    theorem = value["theorem_contract"]
    require_keys(theorem, {"factor_orbit_dictionary", "fixed_points", "primitive_points", "determinant", "density", "ramified_boundary"})
    for token in ("det(I-uP_p)^(-1)", "p=283", "Chebotarev"):
        if not any(token in text for text in theorem.values()):
            raise AssertionError(f"missing theorem token {token}")
        checks += 1
    if not same(value["ownership_boundary"], OWNERSHIP_BOUNDARY):
        raise AssertionError("ownership boundary")
    if value["finite_evidence_role"] != "all 1228 good primes at most 10000 and iterates through 12 are exact regression receipts; the quartic theorem covers all good primes and all iterates":
        raise AssertionError("finite evidence role")
    checks += 2

    good_primes = [int(p) for p in primerange(2, 10001) if p != 283]
    rows = value["prime_rows"]
    if type(rows) is not list or len(rows) != len(good_primes):
        raise AssertionError("prime row length")
    checks += 1
    class_counts = {info[0]: 0 for info in CLASS.values()}
    for p, row in zip(good_primes, rows):
        require_keys(row, ROW_KEYS)
        expected = expected_row(p)
        if not same(row, expected):
            raise AssertionError(f"row mismatch at p={p}")
        class_counts[row["cycle_type"]] += 1
        checks += 1
        for r, (fixed, points, cycles) in enumerate(zip(row["fixed_counts_r1_to_r12"], row["primitive_point_counts_r1_to_r12"], row["primitive_cycle_counts_r1_to_r12"]), 1):
            if points != r * cycles or fixed != sum(d * row["primitive_cycle_counts_r1_to_r12"][d - 1] for d in range(1, r + 1) if r % d == 0):
                raise AssertionError(f"orbit inversion mismatch p={p}, r={r}")
            checks += 1
    expected_counts = {"1+1+1+1": 43, "2+1+1": 306, "2+2": 147, "3+1": 411, "4": 321}
    if class_counts != expected_counts:
        raise AssertionError("class count regression")
    expected_enum = {
        "prime_bound": 10000, "all_primes": 1229, "good_primes": 1228, "ramified_primes": 1,
        "iterate_bound": 12, "prime_iterate_cells": 14736, "class_counts": expected_counts, "all_five_types_seen": True,
    }
    if not same(value["enumeration"], expected_enum):
        raise AssertionError("enumeration")
    checks += 2
    if not same(value["collision_boundary"], COLLISION_BOUNDARY):
        raise AssertionError("collision boundary")
    checks += 1

    expected_witnesses = [
        {"cycle_type": "4", "p": 2, "factorization_mod_p": "x^4+x+1", "s4_conjugacy_class_size": 6, "chebotarev_density": "1/4"},
        {"cycle_type": "3+1", "p": 7, "factorization_mod_p": "(x-3)(x^3+3x^2+2x-2)", "s4_conjugacy_class_size": 8, "chebotarev_density": "1/3"},
        {"cycle_type": "2+1+1", "p": 17, "factorization_mod_p": "(x+2)(x+5)(x^2-7x+5)", "s4_conjugacy_class_size": 6, "chebotarev_density": "1/4"},
        {"cycle_type": "2+2", "p": 71, "factorization_mod_p": "(x^2+15x-20)(x^2-15x+32)", "s4_conjugacy_class_size": 3, "chebotarev_density": "1/8"},
        {"cycle_type": "1+1+1+1", "p": 83, "factorization_mod_p": "(x+3)(x+7)(x+14)(x-24)", "s4_conjugacy_class_size": 1, "chebotarev_density": "1/24"},
    ]
    if not same(value["class_witnesses"], expected_witnesses):
        raise AssertionError("witnesses")
    for row in expected_witnesses:
        if expected_row(row["p"])["cycle_type"] != row["cycle_type"]:
            raise AssertionError("witness factor type")
        checks += 1
    boundary = value["ramified_boundary"]
    unit, factors = gf_factor([1, 0, 0, -1, -1], 283, ZZ)
    signature = sorted((len(coeffs) - 1, multiplicity) for coeffs, multiplicity in factors)
    if unit != 1 or signature != [(1, 1), (1, 1), (1, 2)] or boundary["repeated_root"] != 93 or boundary["gcd_f_fprime_coefficients_mod_p"] != [190, 1]:
        raise AssertionError("ramified boundary")
    checks += 4

    atlas = value["class_atlas"]
    if len(atlas) != 5:
        raise AssertionError("atlas length")
    for entry in atlas:
        partition = tuple(entry["partition"])
        label, size, density = CLASS[partition]
        expected = {
            "cycle_type": label, "partition": list(partition), "s4_conjugacy_class_size": size,
            "chebotarev_density": density, "det_I_minus_uP_coefficients": denominator(partition),
            "fixed_counts_r1_to_r12": [sum(d for d in partition if r % d == 0) for r in range(1, 13)],
        }
        if not same(entry, expected):
            raise AssertionError(f"atlas mismatch {label}")
        checks += 1
    if not same(value["route_a"], {"tuple": ROUTE, "overall": "ROUTE_A_ARITHMETIC_CANDIDATE", "route_b_invocation_allowed": False}):
        raise AssertionError("evidence route")
    if not same(value["scope_flags"], yml["scope_flags"]) or any(value["scope_flags"].values()):
        raise AssertionError("evidence scope")
    if not same(value["nonclaims"], NONCLAIMS):
        raise AssertionError("nonclaims")
    if not same(value["references"], REFERENCES):
        raise AssertionError("references")
    checks += 10
    return checks


def main():
    if sys.flags.optimize:
        raise RuntimeError("C369 checker refuses optimized Python")
    print(f"C369 independent checker: PASS ({check()} assertions)")


if __name__ == "__main__":
    main()
