#!/usr/bin/env python3
"""Independent checker for HCS-C294; deliberately imports no producer code."""
from __future__ import annotations

import argparse
import ast
import hashlib
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import yaml

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "f8d3ad9a8940b54e82854b2924be353575ed8fcb"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
TUPLE = ["A0_FAIL", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"]
MODEL = {
    "obstacles": "three closed radius-r disks at the vertices of an equilateral triangle of side d",
    "domain": "Euclidean plane minus the obstacle interiors",
    "parameter_chamber": "r>0 and d>4r/sqrt(3)",
    "clock": "one specular collision",
    "orientation": "oriented rays; time reversal reverses the cyclic word",
    "no_eclipse_gap": "sqrt(3)d/2-2r",
}
THEOREM = {
    "coding": "cyclically reduced cyclic classes correspond bijectively to periodic-ray iterates",
    "iterate_convention": "a periodic-ray iterate is a primitive oriented geometric ray paired with a positive traversal multiplicity",
    "primitive_coding": "primitive cyclic classes correspond bijectively to primitive oriented geometric rays",
    "geometry": "each coded iterate has a unique non-grazing, isolated, dispersing-hyperbolic geometric support",
    "fixed_count": "F_n=2^n+2(-1)^n",
    "primitive_ledger": "P_n=sum_{e|n}mu(e)F_{n/e}; O_n=P_n/n",
    "collision_zeta": "1/((1-2z)(1+z)^2)",
    "length_bounds": "n(d-2r)<=L_w<=n(d+2r)",
    "reversal": "[w] maps to [reverse(w)] without automatic division by two",
}
PROOF = {
    "existence": "compact minimization of polygonal length over the product of closed disks",
    "boundary": "no-eclipse excludes an interior minimizing vertex",
    "uniqueness": "convexity plus strict convexity of every disk excludes two distinct minimizers",
    "reflection": "the constrained first variation gives specular reflection and excludes grazing",
    "hyperbolicity": "positive free-flight and defocusing optical matrices have determinant one and trace greater than two",
    "finite_role": "finite words and optical grids audit conventions only; they do not prove geometric coding",
}
FLAGS = {
    "claims_target_arithmetic_local_data": False,
    "claims_target_euler_factors": False,
    "claims_root_number": False,
    "claims_automorphy": False,
    "claims_target_divisor_or_counting_law": False,
    "claims_target_functional_equation": False,
    "claims_target_zero_match": False,
    "claims_hilbert_polya_operator": False,
    "invokes_route_b": False,
}
NONCLAIMS = [
    "No target arithmetic local datum, Euler factor, root number, automorphy, divisor, functional equation, or zero match is asserted.",
    "The collision-code zeta is source-local and uses bounce count rather than geometric length.",
    "The exterior Dirichlet Laplacian is only the natural quantization of the billiard geometry, not a Hilbert--Polya operator.",
    "No literary priority is claimed for classical open-billiard coding or dispersing hyperbolicity.",
]
EVIDENCE_KEYS = {
    "schema", "candidate_id", "obstruction_id", "evaluation_date", "fixed_epoch", "source_commit", "scope_literal",
    "evaluator", "model", "theorem_contract", "proof_contract", "enumeration", "route_a",
    "scope_flags", "nonclaims", "references", "payload_sha256",
}
MODEL_KEYS = {"obstacles", "domain", "parameter_chamber", "clock", "orientation", "no_eclipse_gap"}
THEOREM_KEYS = {
    "coding", "iterate_convention", "primitive_coding", "geometry", "fixed_count",
    "primitive_ledger", "collision_zeta", "length_bounds", "reversal",
}
PROOF_KEYS = {"existence", "boundary", "uniqueness", "reflection", "hyperbolicity", "finite_role"}
ENUM_KEYS = {"count_rows", "direct_rows", "zeta_coefficients_0_to_16", "optical_rows", "geometry_rows", "symmetric_orbits", "count_cell_count", "optical_cell_count", "geometry_cell_count"}
YAML_KEYS = {
    "schema", "candidate_id", "title", "evaluation_date", "source_commit", "fixed_epoch",
    "scope_literal", "evaluator_authority", "evaluator_version", "evaluator_authority_sha256",
    "obstruction_id", "candidate_definition", "family", "phase_space", "dynamics", "parameters",
    "parameter_provenance", "arithmetic_origin", "clock", "normalization", "determinant_convention",
    "orbit_cutoff", "precision", "training_data", "forbidden_data", "artifact_paths", "a0", "a1",
    "a2", "a3", "a4", "tuple", "overall_verdict", "route_b_invocation_allowed",
    "route_b_lock_reason", "scope_flags", "theorem_status", "finite_evidence_role", "source_owner_tokens",
}


def reject_duplicates(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def reject_nonfinite(value):
    raise ValueError(f"non-finite JSON constant: {value}")


class UniqueYAMLLoader(yaml.SafeLoader):
    pass


def construct_unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError(f"duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueYAMLLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_unique_mapping)


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def mobius(n: int) -> int:
    primes = 0
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            primes += 1
            if n % p == 0:
                return 0
            while n % p == 0:
                n //= p
        p += 1
    return -1 if (primes + (n > 1)) % 2 else 1


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def parse_fraction(value: str) -> Fraction:
    return Fraction(value)


def exact_tree_equal(actual, expected) -> bool:
    if type(actual) is not type(expected):
        return False
    if type(expected) is dict:
        return set(actual) == set(expected) and all(
            exact_tree_equal(actual[key], expected[key]) for key in expected
        )
    if type(expected) is list:
        return len(actual) == len(expected) and all(
            exact_tree_equal(left, right) for left, right in zip(actual, expected)
        )
    return actual == expected


def matmul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def matpow(a, n):
    result = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))
    for _ in range(n):
        result = matmul(result, a)
    return result


def least_period(word):
    n = len(word)
    for d in divisors(n):
        if all(word[j] == word[j % d] for j in range(n)):
            return d
    raise AssertionError


def check_all(data: dict, route_yaml: dict) -> int:
    count = 0

    def check(condition, label):
        nonlocal count
        count += 1
        if not condition:
            raise AssertionError(label)

    check(type(data) is dict and set(data) == EVIDENCE_KEYS, "evidence keys")
    check(data["payload_sha256"] == payload_hash(data), "payload hash")
    check(data["schema"] == "hcs-c294-three-disk-open-billiard-v1", "schema")
    check(data["candidate_id"] == "HCS-C294", "candidate")
    check(data["obstruction_id"] == "HEN-O278", "obstruction")
    check(data["evaluation_date"] == "2026-09-02", "date")
    check(type(data["fixed_epoch"]) is int and data["fixed_epoch"] == 1788307200, "epoch")
    check(data["source_commit"] == SOURCE, "source")
    check(data["scope_literal"] == SCOPE, "scope")
    check(data["evaluator"] == {"version": "0.2.0", "sha256": EVALUATOR}, "evaluator")
    check(type(data["model"]) is dict and set(data["model"]) == MODEL_KEYS, "model keys")
    check(data["model"] == MODEL, "model contract")
    check(type(data["theorem_contract"]) is dict and set(data["theorem_contract"]) == THEOREM_KEYS, "theorem keys")
    check(data["theorem_contract"] == THEOREM, "theorem contract")
    check(type(data["proof_contract"]) is dict and set(data["proof_contract"]) == PROOF_KEYS, "proof keys")
    check(data["proof_contract"] == PROOF, "proof contract")
    check(type(data["enumeration"]) is dict and set(data["enumeration"]) == ENUM_KEYS, "enumeration keys")
    check(exact_tree_equal(data["route_a"], {
        "tuple": TUPLE, "overall": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
    }), "route tuple and exact types")
    check(data["scope_flags"] == FLAGS, "scope flags")
    check(len(data["scope_flags"]) == 9, "scope flag count")
    for key, value in data["scope_flags"].items():
        check(type(key) is str and type(value) is bool and value is False, f"scope {key}")
    check(exact_tree_equal(data["nonclaims"], NONCLAIMS), "canonical nonclaims and scope polarity")
    check(data["references"] == [
        {"identifier": "10.1070/RM1970v025n02ABEH003794", "role": "dispersing-billiard lineage"},
        {"identifier": "10.5802/aif.1137", "role": "several-convex-obstacle and no-eclipse lineage"},
        {"identifier": "10.1063/1.456019", "role": "three-hard-disk scattering owner"},
    ], "references")

    rows = data["enumeration"]["count_rows"]
    check(len(rows) == 16, "count row length")
    row_map = {row["n"]: row for row in rows}
    check(len(row_map) == 16, "unique count n")
    for n in range(1, 17):
        row = row_map[n]
        check(set(row) == {"n", "fixed_rooted_words", "exact_period_rooted_words", "primitive_orbits"}, f"count keys {n}")
        fixed = 2**n + 2 * ((-1) ** n)
        primitive = sum(mobius(e) * (2 ** (n // e) + 2 * ((-1) ** (n // e))) for e in divisors(n))
        check(exact_tree_equal(row, {
            "n": n, "fixed_rooted_words": fixed,
            "exact_period_rooted_words": primitive, "primitive_orbits": primitive // n,
        }), f"count exact tree {n}")
        check(row["fixed_rooted_words"] == fixed, f"fixed formula {n}")
        check(row["exact_period_rooted_words"] == primitive, f"primitive formula {n}")
        check(row["primitive_orbits"] == primitive // n and primitive % n == 0, f"orbits {n}")

    direct = {row["n"]: row for row in data["enumeration"]["direct_rows"]}
    check(len(direct) == 10, "direct length")
    for n in range(1, 11):
        check(set(direct[n]) == {"n", "fixed_rooted_words", "exact_period_rooted_words", "reversal_symmetric_rooted_words"}, f"direct keys {n}")
        fixed = primitive = reversal = 0
        for word in itertools.product(range(3), repeat=n):
            ok = all(word[j] != word[(j + 1) % n] for j in range(n))
            check(type(ok) is bool, f"word predicate {n}:{word}")
            if not ok:
                continue
            fixed += 1
            lp = least_period(word)
            check(n % lp == 0, f"least divides {n}:{word}")
            primitive += lp == n
            rev = tuple(reversed(word))
            reversal += any(rev == word[k:] + word[:k] for k in range(n))
        check(exact_tree_equal(direct[n], {
            "n": n, "fixed_rooted_words": fixed,
            "exact_period_rooted_words": primitive,
            "reversal_symmetric_rooted_words": reversal,
        }), f"direct exact tree {n}")
        check(direct[n]["fixed_rooted_words"] == fixed == row_map[n]["fixed_rooted_words"], f"direct fixed {n}")
        check(direct[n]["exact_period_rooted_words"] == primitive == row_map[n]["exact_period_rooted_words"], f"direct primitive {n}")
        check(direct[n]["reversal_symmetric_rooted_words"] == reversal, f"direct reversal {n}")

    coeffs = data["enumeration"]["zeta_coefficients_0_to_16"]
    check(len(coeffs) == 17 and coeffs[0] == 1 and all(type(value) is int for value in coeffs), "zeta coefficients exact integer types")
    for n in range(1, 17):
        rhs = (3 * coeffs[n - 2] if n >= 2 else 0) + (2 * coeffs[n - 3] if n >= 3 else 0)
        check(coeffs[n] == rhs, f"zeta recurrence {n}")

    optical = data["enumeration"]["optical_rows"]
    check(len(optical) == 175, "optical length")
    expected_optical_grid = [
        (a, ell, n)
        for a in (Fraction(1, 3), Fraction(1, 2), Fraction(1), Fraction(2), Fraction(5, 2))
        for ell in (Fraction(1, 4), Fraction(1, 2), Fraction(1), Fraction(3, 2), Fraction(3))
        for n in range(2, 9)
    ]
    for index, row in enumerate(optical):
        check(set(row) == {"a", "ell", "n", "matrix", "determinant", "trace", "hyperbolic"}, f"optical keys {index}")
        check(
            type(row["a"]) is str and type(row["ell"]) is str and type(row["n"]) is int
            and type(row["matrix"]) is list and len(row["matrix"]) == 2
            and all(type(line) is list and len(line) == 2 and all(type(value) is str for value in line) for line in row["matrix"])
            and type(row["determinant"]) is str and type(row["trace"]) is str
            and type(row["hyperbolic"]) is bool,
            f"optical exact types {index}",
        )
        a, ell, n = parse_fraction(row["a"]), parse_fraction(row["ell"]), row["n"]
        check((a, ell, n) == expected_optical_grid[index], f"optical frozen grid {index}")
        check(a > 0 and ell > 0 and type(n) is int and 2 <= n <= 8, f"optical inputs {index}")
        block = ((Fraction(1), ell), (a, Fraction(1) + a * ell))
        m = matpow(block, n)
        recorded = tuple(tuple(parse_fraction(x) for x in line) for line in row["matrix"])
        check(recorded == m, f"optical matrix {index}")
        det = m[0][0] * m[1][1] - m[0][1] * m[1][0]
        trace = m[0][0] + m[1][1]
        check(parse_fraction(row["determinant"]) == det == 1, f"optical det {index}")
        check(parse_fraction(row["trace"]) == trace and trace > 2, f"optical trace {index}")
        check(row["hyperbolic"] is True, f"optical boolean {index}")

    geometry = data["enumeration"]["geometry_rows"]
    check(len(geometry) == 6, "geometry rows")
    expected_geometry_grid = [(1, 3), (2, 5), (3, 7), (5, 12), (7, 17), (11, 27)]
    mp.mp.dps = 80
    for index, row in enumerate(geometry):
        check(set(row) == {"r", "d", "pair_gap", "no_eclipse_gap_60_digits", "no_eclipse"}, f"geometry keys {index}")
        r, d = row["r"], row["d"]
        value = mp.sqrt(3) * d / 2 - 2 * r
        check(
            type(r) is int and type(d) is int and type(row["pair_gap"]) is int
            and type(row["no_eclipse_gap_60_digits"]) is str
            and type(row["no_eclipse"]) is bool and r > 0 and d > 0,
            f"geometry exact types {index}",
        )
        check((r, d) == expected_geometry_grid[index], f"geometry frozen grid {index}")
        check(row["pair_gap"] == d - 2 * r > 0, f"pair gap {index}")
        check(abs(mp.mpf(row["no_eclipse_gap_60_digits"]) - value) < mp.mpf("1e-59"), f"no eclipse numeric {index}")
        check(row["no_eclipse"] is (value > 0), f"no eclipse bool {index}")

    symmetric = data["enumeration"]["symmetric_orbits"]
    check(len(symmetric) == 2 and symmetric[0]["word"] == "01" and symmetric[1]["word"] == "012", "symmetric words")
    p2 = symmetric[0]
    check(exact_tree_equal(p2, {
        "word": "01", "r": 1, "d": 3, "flight_length": "1",
        "total_length": "2", "incidence_cosine": "1",
        "monodromy": [["3", "4"], ["8", "11"]],
        "monodromy_trace": "14", "monodromy_determinant": "1",
    }), "p2 exact tree")
    check(p2["monodromy"] == [["3", "4"], ["8", "11"]], "p2 matrix")
    check(p2["monodromy_trace"] == "14" and p2["monodromy_determinant"] == "1", "p2 invariants")
    ell3 = mp.mpf(3) - mp.sqrt(3)
    a3 = 4 / mp.sqrt(3)
    b3 = mp.matrix([[1, ell3], [a3, 1 + a3 * ell3]])
    m3 = b3**3
    check(exact_tree_equal(set(symmetric[1]), {
        "word", "r", "d", "flight_length_exact", "total_length_exact",
        "incidence_cosine_exact", "defocusing_kick_exact",
        "monodromy_trace_60_digits", "monodromy_determinant_60_digits",
    }), "p3 exact keys")
    check(all(type(value) is str for value in symmetric[1].values()), "p3 exact string types")
    check(symmetric[1]["r"] == "1" and symmetric[1]["d"] == "3"
          and symmetric[1]["flight_length_exact"] == "3-sqrt(3)"
          and symmetric[1]["total_length_exact"] == "9-3*sqrt(3)"
          and symmetric[1]["incidence_cosine_exact"] == "sqrt(3)/2"
          and symmetric[1]["defocusing_kick_exact"] == "4/sqrt(3)", "p3 exact geometry")
    check(abs(mp.mpf(symmetric[1]["monodromy_trace_60_digits"]) - (m3[0, 0] + m3[1, 1])) < mp.mpf("1e-59"), "p3 trace")
    check(abs(mp.mpf(symmetric[1]["monodromy_determinant_60_digits"]) - 1) < mp.mpf("1e-59"), "p3 determinant")
    check(type(data["enumeration"]["count_cell_count"]) is int and data["enumeration"]["count_cell_count"] == 26, "count cells")
    check(type(data["enumeration"]["optical_cell_count"]) is int and data["enumeration"]["optical_cell_count"] == 175, "optical cells")
    check(type(data["enumeration"]["geometry_cell_count"]) is int and data["enumeration"]["geometry_cell_count"] == 8, "geometry cells")

    check(type(route_yaml) is dict and set(route_yaml) == YAML_KEYS, "yaml keys")
    check(route_yaml["schema"] == "route-a-evaluation-v0.2.0", "yaml schema")
    check(route_yaml["candidate_id"] == "HCS-C294" and route_yaml["obstruction_id"] == "HEN-O278", "yaml identity")
    check(route_yaml["source_commit"] == SOURCE and route_yaml["fixed_epoch"] == 1788307200, "yaml source")
    check(route_yaml["scope_literal"] == SCOPE and route_yaml["evaluator_authority_sha256"] == EVALUATOR, "yaml authority")
    check(route_yaml["tuple"] == TUPLE and route_yaml["overall_verdict"] == "ROUTE_A_REJECTED", "yaml tuple")
    check(route_yaml["route_b_invocation_allowed"] is False, "yaml route b")
    check(route_yaml["theorem_status"] == "PROVABLE_AS_STATED", "yaml theorem status")
    check(route_yaml["a1"]["verdict"] == "A1_PASS_ANALYTIC", "yaml a1")
    check(route_yaml["a4"]["verdict"] == "A4_NATURAL_QUANTIZATION", "yaml a4")
    check(route_yaml["scope_flags"] == data["scope_flags"], "yaml flags")
    check(all(type(value) is bool and value is False for value in route_yaml["scope_flags"].values()), "yaml flag bool types")
    semantic = json.dumps(route_yaml, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    check(hashlib.sha256(semantic.encode()).hexdigest() == "832f2efec20b72d69ea1be577a6fc38168b09625a2804dbb03cc9ff7fad91f4b", "yaml exact semantic tree")
    for axis in ["a0", "a1", "a2", "a3", "a4"]:
        check(type(route_yaml[axis]) is dict and set(route_yaml[axis]) == {"verdict", "evidence_status", "strongest_evidence", "strongest_failure", "artifacts"}, f"yaml {axis}")

    producer_tree = ast.parse((ROOT / "code/c294_three_disk_checker.py").read_text())
    imports = []
    for node in ast.walk(producer_tree):
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module or "")
    check(not any("producer" in name for name in imports), "checker independence")

    for relative, tokens in {
        "THEOREM_PACKAGE.md": ["PROVABLE AS STATED", "strict convexity", "Finite evidence is regression evidence only", "HEN-O278"],
        "SOURCE_AUDIT.md": ["10.1070/RM1970v025n02ABEH003794", "10.5802/aif.1137", "10.1063/1.456019", "no literature-priority claim"],
        "paper/main.tex": ["Convex variational coding", "No-eclipse", "collision-code zeta", "AI-use statement"],
    }.items():
        joined = " ".join((ROOT / relative).read_text().split())
        for token in tokens:
            check(token in joined, f"document token {relative}:{token}")
    return count


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=ROOT / "results/c294_three_disk_evidence.json")
    parser.add_argument("--yaml", type=Path, default=ROOT / "evaluations/route_a/HCS-C294/2026-09-02.yaml")
    args = parser.parse_args()
    data = json.loads(args.evidence.read_text(), object_pairs_hook=reject_duplicates, parse_constant=reject_nonfinite)
    route_yaml = yaml.load(args.yaml.read_text(), Loader=UniqueYAMLLoader)
    count = check_all(data, route_yaml)
    print(f"C294 independent checker: PASS ({count} assertions; producer import forbidden)")


if __name__ == "__main__":
    main()
