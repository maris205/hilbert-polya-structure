#!/usr/bin/env python3
"""Independent fail-closed checker for the HCS-C55 exact certificate.

The producer reuses the frozen C52 exact backend and Singular's ``wp`` order.
This checker instead reconstructs the quotient/action with its own arithmetic
and uses Singular's distinct ``Wp`` order.  Agreement is required only after
projective rational normalization of the Yukawa tensor.
"""

from __future__ import annotations

import argparse
from collections import Counter
import copy
from fractions import Fraction
from functools import reduce
import hashlib
from itertools import combinations_with_replacement, product
import json
import math
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from typing import Any

import sympy as sp


PROJECT = Path(__file__).resolve().parents[1]
REPOSITORY = Path(__file__).resolve().parents[3]
EXPECTED_PAYLOAD_SHA256 = "6afc529d2ab9e849592d9eba7b76324cc7a840670f50c669f90fdd079c0b4323"
EXPECTED_SCHEMA_SHA256 = "2961eb6b5b4aefa0e12ffcb59c9e1095b14f0309e2045fd6d8a7f636dc6dca53"
EXPECTED_PRIMITIVE_SHA256 = "1c7065d5644c44bba80658dee5d0704c371e9f446c8c3c6ac29f9590d0831b9e"
EXPECTED_CENTRAL_PATHS_SHA256 = "f17a32b6eade7f081a90aa8fc09a15a5a6488780f5d92493297f854a75a29b2d"
EXPECTED_CENTRAL_PROJECTION_SHA256 = "aa69291cba3bbd8f3ad7c363498e9b130d8f909a8c8293509f28f987ba2f88a0"
EXPECTED_TOTAL_SCALAR_LEAVES = 1589
EXPECTED_CENTRAL_SCALAR_LEAVES = 292
EXPECTED_DERIVED_SCALAR_LEAVES = 1296

EXPECTED_RELEASES = {
    "C52": {
        "project": "henon_dynamics/henon_mu3_d12_calabi_yau_core_projector",
        "implementation": "208feef86365cd92ace8dad02904acff6623eeec",
        "provenance": "a411b8d2626190a9ca941e55d15826db0dedc417",
        "payload": "78d362e62efacc78dac511d9607d93f21f065a86f1d41c62c10c101b652558f1",
        "files": {
            "results/c52_certificate.json": "a2b0b281bfb311f979c7ed65e441a184ebe338b05f5fec8a60768610965c9c94",
            "results/independent_check.json": "a4a0180a3e40a8eb82159fcea474221dafabddd728ebf1c2112435b21ad5c6f1",
            "results/ARTIFACT_HASHES.sha256": "3e0b3d1fa0f371ddffe5eba9a379018d72ee1f2059863245a741da899ec9fd30",
            "THEOREM_PACKAGE.md": "376c6444481b5766d05a4f23757217496402de12507e2303d2c1a25ced8e469a",
            "route_a_evaluation.yaml": "312d4701adb82e30224749ba682474ab66a921222f584d8e6e1d9743a4d64653",
            "evaluations/route_a/HCS-C52/20260814T100000Z.yaml": "312d4701adb82e30224749ba682474ab66a921222f584d8e6e1d9743a4d64653",
            "INTEGRITY_REPORT.md": "e7224410769e3e5dfb66a3ecacb64a6d061d28394cefd2e5ac446027729125db",
            "code/c52_producer.py": "69cf4d7571bf6a8ca6dfc972c57c5f0fa6b2b06f02ac8d583c56d233e81a3eed",
        },
    },
    "C53": {
        "project": "henon_dynamics/henon_mu3_dihedral_core_rational_descent",
        "implementation": "0a7f0fdb8290eab4aa92ed5ade432401c40c22cf",
        "provenance": "9d509d3b3826b7bfbdb38ed9fe4dac9297f5dbdf",
        "payload": "8064224eda63fa9d890efd26ec9aa167c7cd9458662620be3135196a09494d41",
        "files": {
            "results/c53_certificate.json": "f4325a5987933e2acf81656389d46701d82d38912c546d1e5996123f617f6e79",
            "results/independent_check.json": "0d38643ded626c2a5e1536c8a4df9c56ae98c4fda01e1d15660996ea8c495e67",
            "results/ARTIFACT_HASHES.sha256": "2b4fc3e3bf3dedba175d40756421ae3433eddc2b7c7272983cf644d6034091b3",
            "THEOREM_PACKAGE.md": "e474d938c02d1d9e39e510dfd77ffcdd6383e5dcc8a8442b5b19465be82dbebe",
            "route_a_evaluation.yaml": "ae508e6e41523559f014f6fbcd0c4c199229f221fe6ac915a75cd27b02e73719",
            "evaluations/route_a/HCS-C53/20260814T150000Z.yaml": "ae508e6e41523559f014f6fbcd0c4c199229f221fe6ac915a75cd27b02e73719",
            "INTEGRITY_REPORT.md": "da3f6caec587b56871ac01cc7db1364cc45f3ec99e684dc263332fb9f2585ae2",
        },
    },
    "C54": {
        "project": "henon_dynamics/henon_mu3_universal_dihedral_denominator_rigidity",
        "implementation": "f2fee2f9844b84aa31e076aabe9d4bb88fbd3618",
        "provenance": "eba8a1e76c0486b72e595f4baddd00d11ae81309",
        "payload": "f068d5e11ea8e6245e04bd3a30e77140267f835c4e07412ce2009c7fb04ceae1",
        "files": {
            "results/c54_certificate.json": "780cc9f249e836d3fa5b51a00fd2cdb9af0eac595d929cd1be4d728df1921846",
            "results/independent_check.json": "160b3a9d11354b41404642a3dd22d6e43f2ce576126acb21eb0133e552fc0c0a",
            "results/CODE_RESULTS_HASHES.sha256": "62f67e6d4929496974020febab3bc0e2cff45ed153b0cef51937031863d866ba",
            "results/ARTIFACT_HASHES.sha256": "92e1950c787ac1625ad9edaf448e54a1fe63162344c79748970bbcfa3dcf7065",
            "THEOREM_PACKAGE.md": "d234f078cb415db8394fdcece124068cad90dbdf12b82941207105ecd24088b4",
            "route_a_evaluation.yaml": "bcc5609b0131444f9321b8c2a79f8480508af84c20cd9933dc993a804fc8c5ed",
            "evaluations/route_a/HCS-C54/20260814T134920Z.yaml": "bcc5609b0131444f9321b8c2a79f8480508af84c20cd9933dc993a804fc8c5ed",
            "INTEGRITY_REPORT.md": "e4683fd0fe5e7529f196c7eb8fbeaa859e1ccd1a46f78d6de447251d7d7cba4f",
        },
    },
}

EXPECTED_FROZEN_UPSTREAM = [
    {
        "name": "C52_certificate",
        "path": "henon_dynamics/henon_mu3_d12_calabi_yau_core_projector/results/c52_certificate.json",
        "sha256": "a2b0b281bfb311f979c7ed65e441a184ebe338b05f5fec8a60768610965c9c94",
        "payload_sha256": "78d362e62efacc78dac511d9607d93f21f065a86f1d41c62c10c101b652558f1",
        "schema": "hcs-c52-certificate-v1",
    },
    {
        "name": "C52_theorem",
        "path": "henon_dynamics/henon_mu3_d12_calabi_yau_core_projector/THEOREM_PACKAGE.md",
        "sha256": "376c6444481b5766d05a4f23757217496402de12507e2303d2c1a25ced8e469a",
    },
    {
        "name": "C52_exact_backend",
        "path": "henon_dynamics/henon_mu3_d12_calabi_yau_core_projector/code/c52_producer.py",
        "sha256": "69cf4d7571bf6a8ca6dfc972c57c5f0fa6b2b06f02ac8d583c56d233e81a3eed",
    },
    {
        "name": "C53_certificate",
        "path": "henon_dynamics/henon_mu3_dihedral_core_rational_descent/results/c53_certificate.json",
        "sha256": "f4325a5987933e2acf81656389d46701d82d38912c546d1e5996123f617f6e79",
        "payload_sha256": "8064224eda63fa9d890efd26ec9aa167c7cd9458662620be3135196a09494d41",
        "schema": "hcs-c53-certificate-v1",
    },
    {
        "name": "C53_theorem",
        "path": "henon_dynamics/henon_mu3_dihedral_core_rational_descent/THEOREM_PACKAGE.md",
        "sha256": "e474d938c02d1d9e39e510dfd77ffcdd6383e5dcc8a8442b5b19465be82dbebe",
    },
    {
        "name": "C54_certificate",
        "path": "henon_dynamics/henon_mu3_universal_dihedral_denominator_rigidity/results/c54_certificate.json",
        "sha256": "780cc9f249e836d3fa5b51a00fd2cdb9af0eac595d929cd1be4d728df1921846",
        "payload_sha256": "f068d5e11ea8e6245e04bd3a30e77140267f835c4e07412ce2009c7fb04ceae1",
        "schema": "hcs-c54-certificate-v1",
    },
    {
        "name": "C54_theorem",
        "path": "henon_dynamics/henon_mu3_universal_dihedral_denominator_rigidity/THEOREM_PACKAGE.md",
        "sha256": "d234f078cb415db8394fdcece124068cad90dbdf12b82941207105ecd24088b4",
    },
]

N = 8
K = tuple[Fraction, Fraction]
ZERO: K = (Fraction(0), Fraction(0))
ONE: K = (Fraction(1), Fraction(0))
IDENTITY = (tuple(range(N)), (0,) * N)
SEEDS = (
    (0, 0, 0, 1, 0, 1, 0, 1),
    (0, 0, 0, 2, 0, 1, 0, 0),
    (0, 0, 2, 0, 0, 0, 1, 0),
    (0, 0, 2, 0, 1, 0, 0, 0),
)
DIRECT_CUBE_POINTS = (
    (1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1),
    (0, 0, 1, 1), (0, 0, 1, 2), (0, 1, 0, 1), (0, 1, 0, 2),
    (0, 1, 1, 0), (0, 1, 1, 1), (0, 1, 2, 0), (1, 0, 0, 1),
    (1, 0, 0, 2), (1, 0, 1, 0), (1, 0, 1, 1), (1, 0, 2, 0),
    (1, 1, 0, 0), (1, 1, 0, 1), (1, 1, 1, 0), (1, 2, 0, 0),
)


def canonical_json(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def strict_load(raw: bytes) -> dict[str, Any]:
    def pairs_hook(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate JSON key: {key}")
            result[key] = value
        return result

    value = json.loads(raw, object_pairs_hook=pairs_hook)
    if type(value) is not dict:
        raise AssertionError("certificate root must be object")
    return value


def schema_descriptor(value: Any) -> Any:
    if type(value) is dict:
        return {key: schema_descriptor(child) for key, child in sorted(value.items())}
    if type(value) is list:
        return [schema_descriptor(child) for child in value]
    if type(value) is bool:
        return "bool"
    if type(value) is int:
        return "int"
    if type(value) is str:
        return "str"
    if value is None:
        return "null"
    raise AssertionError(f"unsupported JSON scalar type: {type(value)}")


def at_path(root: Any, path: tuple[str | int, ...]) -> Any:
    value = root
    for component in path:
        value = value[component]
    return value


def exact_json(left: Any, right: Any) -> bool:
    if type(left) is not type(right):
        return False
    if type(left) is dict:
        return set(left) == set(right) and all(
            exact_json(left[key], right[key]) for key in left
        )
    if type(left) is list:
        return len(left) == len(right) and all(
            exact_json(a, b) for a, b in zip(left, right)
        )
    return left == right


ScalarPath = tuple[str | int, ...]


def scalar_leaves(value: Any, path: ScalarPath = ()):
    """Yield every JSON scalar with an exact dictionary/list path."""
    if type(value) is dict:
        for key, child in value.items():
            yield from scalar_leaves(child, path + (key,))
        return
    if type(value) is list:
        for index, child in enumerate(value):
            yield from scalar_leaves(child, path + (index,))
        return
    if type(value) not in {bool, int, str} and value is not None:
        raise AssertionError(f"non-JSON scalar at {path}: {type(value).__name__}")
    yield path, value


# Every scalar below one of these deliberately narrow prefixes is checked by
# an exact recomputation or by a complete algebraic reconstruction in
# verify().  Narrative and scope fields are intentionally excluded.
DERIVED_SCALAR_PREFIXES: tuple[ScalarPath, ...] = (
    ("source_lock", "frozen_upstream_artifacts"),
    ("source_lock", "committed_release_provenance"),
    ("equivariant_tangent", "Reynolds_seed_x_exponents"),
    ("equivariant_tangent", "Reynolds_basis_sparse_y2_p_i"),
    ("equivariant_tangent", "semilinear_descent_matrix_columns"),
    ("equivariant_tangent", "fixed_Q_basis_columns_in_e_basis"),
    ("equivariant_tangent", "tangent_operator_component"),
    ("cayley_Yukawa", "symmetric_traces_in_e_basis"),
    ("cayley_Yukawa", "producer_direct_cube"),
    ("rational_cubic_surface", "primitive_integral_coefficients"),
    ("rational_cubic_surface", "common_K_trace_scale"),
    ("rational_cubic_surface", "factorization_over_Q"),
    ("rational_cubic_surface", "producer_smoothness_backend"),
)


# This is the only chronology-only scalar.  Its enclosing status and both
# negative evidence flags remain central semantic leaves.
NONSEMANTIC_ALLOWLIST: dict[ScalarPath, str] = {
    ("pre_release_chronology", "architecture_report_sha256"): (
        "unpackaged chronology only; never a theorem or gate input"
    ),
}


def is_derived_scalar_path(path: ScalarPath) -> bool:
    return any(path[: len(prefix)] == prefix for prefix in DERIVED_SCALAR_PREFIXES)


def scalar_type_name(value: Any) -> str:
    if type(value) is bool:
        return "bool"
    if type(value) is int:
        return "int"
    if type(value) is str:
        return "str"
    if value is None:
        return "null"
    raise AssertionError(f"unsupported scalar type {type(value).__name__}")


def central_inventory_rows(payload: dict[str, Any]):
    leaves = dict(scalar_leaves(payload))
    nonsemantic = set(NONSEMANTIC_ALLOWLIST)
    if not nonsemantic <= set(leaves):
        raise AssertionError("chronology allowlist path missing")
    derived = {path for path in leaves if is_derived_scalar_path(path)}
    if derived & nonsemantic:
        raise AssertionError("derived/nonsemantic scalar classification overlap")
    central = set(leaves) - derived - nonsemantic
    path_rows = [
        [list(path), scalar_type_name(leaves[path])]
        for path in sorted(central, key=repr)
    ]
    projection_rows = [
        [list(path), scalar_type_name(leaves[path]), leaves[path]]
        for path in sorted(central, key=repr)
    ]
    return leaves, central, derived, nonsemantic, path_rows, projection_rows


def validate_scalar_inventory(payload: dict[str, Any]) -> dict[str, int]:
    """Close the scalar universe under central, derived, and chronology lanes."""
    leaves, central, derived, nonsemantic, path_rows, projection_rows = (
        central_inventory_rows(payload)
    )
    if len(leaves) != len(central) + len(derived) + len(nonsemantic):
        raise AssertionError("scalar classification count identity failure")
    chronology_value = at_path(
        payload, ("pre_release_chronology", "architecture_report_sha256")
    )
    if (
        type(chronology_value) is not str
        or re.fullmatch(r"[0-9a-f]{64}", chronology_value) is None
    ):
        raise AssertionError("chronology-only hash shape mutation")
    counts = (len(leaves), len(central), len(derived), len(nonsemantic))
    expected_counts = (
        EXPECTED_TOTAL_SCALAR_LEAVES,
        EXPECTED_CENTRAL_SCALAR_LEAVES,
        EXPECTED_DERIVED_SCALAR_LEAVES,
        len(NONSEMANTIC_ALLOWLIST),
    )
    if EXPECTED_TOTAL_SCALAR_LEAVES >= 0 and counts != expected_counts:
        raise AssertionError(f"scalar classification count drift {counts}")
    paths_sha = hashlib.sha256(canonical_json(path_rows)).hexdigest()
    projection_sha = hashlib.sha256(canonical_json(projection_rows)).hexdigest()
    if (
        EXPECTED_CENTRAL_PATHS_SHA256 != "TO_BE_LOCKED"
        and paths_sha != EXPECTED_CENTRAL_PATHS_SHA256
    ):
        raise AssertionError("central semantic path/type inventory mismatch")
    if (
        EXPECTED_CENTRAL_PROJECTION_SHA256 != "TO_BE_LOCKED"
        and projection_sha != EXPECTED_CENTRAL_PROJECTION_SHA256
    ):
        raise AssertionError("central semantic projection mismatch")
    return {
        "total": len(leaves),
        "central": len(central),
        "derived": len(derived),
        "nonsemantic": len(nonsemantic),
    }


def add(left: K, right: K) -> K:
    return left[0] + right[0], left[1] + right[1]


def neg(value: K) -> K:
    return -value[0], -value[1]


def sub(left: K, right: K) -> K:
    return left[0] - right[0], left[1] - right[1]


def mul(left: K, right: K) -> K:
    a, b = left
    c, d = right
    return a * c - b * d, a * d + b * c - b * d


def inv(value: K) -> K:
    a, b = value
    norm = a * a - a * b + b * b
    if norm == 0:
        raise ZeroDivisionError
    return (a - b) / norm, -b / norm


def div(left: K, right: K) -> K:
    return mul(left, inv(right))


def kint(value: int) -> K:
    return Fraction(value), Fraction(0)


def rho_power(exponent: int) -> K:
    return (ONE, (Fraction(0), Fraction(1)), (Fraction(-1), Fraction(-1)))[exponent % 3]


def tau(value: K) -> K:
    return value[0] - value[1], -value[1]


def parse_fraction(value: Any) -> Fraction:
    if type(value) is not list or len(value) != 2 or any(type(entry) is not int for entry in value):
        raise AssertionError("invalid rational pair")
    if value[1] <= 0:
        raise AssertionError("nonpositive rational denominator")
    result = Fraction(value[0], value[1])
    if [result.numerator, result.denominator] != value:
        raise AssertionError("noncanonical rational pair")
    return result


def parse_k(value: Any) -> K:
    if type(value) is not dict or set(value) != {"a", "b"}:
        raise AssertionError("invalid K scalar")
    return parse_fraction(value["a"]), parse_fraction(value["b"])


def canonical_element(permutation, phases):
    shift = phases[0] % 3
    return tuple(permutation), tuple((entry - shift) % 3 for entry in phases)


def group_multiply(left, right):
    p_left, e_left = left
    p_right, e_right = right
    return canonical_element(
        tuple(p_right[p_left[index]] for index in range(N)),
        tuple((e_left[index] + e_right[p_left[index]]) % 3 for index in range(N)),
    )


def group_inverse(element):
    permutation, phases = element
    inverse_permutation = [0] * N
    for index, image in enumerate(permutation):
        inverse_permutation[image] = index
    inverse_phases = [(-phases[inverse_permutation[image]]) % 3 for image in range(N)]
    return canonical_element(tuple(inverse_permutation), tuple(inverse_phases))


def permutation_sign(permutation) -> int:
    inversions = sum(
        permutation[i] > permutation[j] for i in range(N) for j in range(i + 1, N)
    )
    return -1 if inversions % 2 else 1


def compositions(total: int, slots: int, prefix=()):
    if slots == 1:
        yield prefix + (total,)
        return
    for entry in range(total + 1):
        yield from compositions(total - entry, slots - 1, prefix + (entry,))


def target_monomials():
    result = []
    for y_exponent in range(3):
        z_exponent = 2 - y_exponent
        x_degree = 1 + y_exponent
        result.extend(
            (y_exponent, z_exponent, exponent)
            for exponent in compositions(x_degree, N)
        )
    return result


def relation_matrix(monomials):
    index = {monomial: position for position, monomial in enumerate(monomials)}
    edge_weights = {
        tuple(sorted((i, (i + 1) % N))): rho_power(1 if i == 7 else 0)
        for i in range(N)
    }

    def vector(terms):
        result = [ZERO] * len(monomials)
        for coefficient, monomial in terms:
            result[index[monomial]] = add(result[index[monomial]], coefficient)
        return result

    def derivative_q(variable):
        terms = []
        for edge, coefficient in edge_weights.items():
            if variable in edge:
                neighbor = edge[0] if edge[1] == variable else edge[1]
                exponent = [0] * N
                exponent[neighbor] = 1
                terms.append((coefficient, tuple(exponent)))
        return terms

    rows = []
    for i in range(N):
        exponent = [0] * N
        exponent[i] = 2
        rows.append(vector(
            [(kint(3), (1, 1, tuple(exponent)))]
            + [(coefficient, (0, 2, x_exp)) for coefficient, x_exp in derivative_q(i)]
        ))
        for j in range(N):
            exponent = [0] * N
            exponent[i] += 2
            exponent[j] += 1
            terms = [(kint(3), (2, 0, tuple(exponent)))]
            for coefficient, x_exp in derivative_q(i):
                shifted = list(x_exp)
                shifted[j] += 1
                terms.append((coefficient, (1, 1, tuple(shifted))))
            rows.append(vector(terms))
    rows.append(vector([
        (ONE, (2, 0, tuple(3 if i == j else 0 for i in range(N))))
        for j in range(N)
    ]))
    rows.append(vector([
        (coefficient, (1, 1, tuple(1 if i in edge else 0 for i in range(N))))
        for edge, coefficient in edge_weights.items()
    ]))
    for j in range(N):
        terms = []
        for edge, coefficient in edge_weights.items():
            exponent = [0] * N
            exponent[edge[0]] += 1
            exponent[edge[1]] += 1
            exponent[j] += 1
            terms.append((coefficient, (2, 0, tuple(exponent))))
        rows.append(vector(terms))
    if len(rows) != 82:
        raise AssertionError("relation construction drifted")
    return rows


def rref(rows):
    matrix = [row[:] for row in rows]
    pivots = []
    rank = 0
    for column in range(len(matrix[0])):
        pivot = next((i for i in range(rank, len(matrix)) if matrix[i][column] != ZERO), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inverse = inv(matrix[rank][column])
        matrix[rank] = [mul(entry, inverse) for entry in matrix[rank]]
        for i in range(len(matrix)):
            if i == rank or matrix[i][column] == ZERO:
                continue
            scalar = matrix[i][column]
            matrix[i] = [sub(left, mul(scalar, right)) for left, right in zip(matrix[i], matrix[rank])]
        pivots.append(column)
        rank += 1
        if rank == len(matrix):
            break
    return matrix[:rank], pivots


def matrix_rank(rows):
    if not rows:
        return 0
    return len(rref(rows)[1])


def git_blob(commit: str, relative: str) -> bytes:
    process = subprocess.run(
        ["git", "show", f"{commit}:{relative}"], cwd=REPOSITORY,
        capture_output=True, timeout=60, check=False,
    )
    if process.returncode != 0:
        raise AssertionError(f"missing committed blob {commit}:{relative}")
    return process.stdout


def verify_provenance(payload):
    frozen_rows = payload["source_lock"]["frozen_upstream_artifacts"]
    if not exact_json(frozen_rows, EXPECTED_FROZEN_UPSTREAM):
        raise AssertionError("frozen upstream artifact inventory mutation")
    for expected in EXPECTED_FROZEN_UPSTREAM:
        raw = (REPOSITORY / expected["path"]).read_bytes()
        if hashlib.sha256(raw).hexdigest() != expected["sha256"]:
            raise AssertionError("frozen upstream live hash mismatch: " + expected["name"])
        if "payload_sha256" in expected:
            upstream = strict_load(raw)
            if (
                upstream.get("schema") != expected["schema"]
                or upstream.get("payload_sha256") != expected["payload_sha256"]
            ):
                raise AssertionError("frozen upstream certificate envelope mismatch")

    rows = payload["source_lock"]["committed_release_provenance"]
    if type(rows) is not list or len(rows) != 3:
        raise AssertionError("release provenance row count")
    by_source = {row["source"]: row for row in rows}
    if set(by_source) != set(EXPECTED_RELEASES):
        raise AssertionError("release provenance source set")
    for label, expected in EXPECTED_RELEASES.items():
        row = by_source[label]
        if row["implementation_commit"] != expected["implementation"]:
            raise AssertionError("implementation commit mutation")
        if row["provenance_commit"] != expected["provenance"]:
            raise AssertionError("provenance commit mutation")
        if row["payload_sha256"] != expected["payload"]:
            raise AssertionError("upstream payload mutation")

        expected_committed_files = [
            {
                "path": f"{expected['project']}/{relative}",
                "sha256": sha,
                "live_equals_provenance_blob": True,
            }
            for relative, sha in expected["files"].items()
        ]
        historical = {
            "C52": None,
            "C53": "b62f353d119d6c8565f513dad771a047a5e6343411d08ad2e91562fe84923480",
            "C54": "62f67e6d4929496974020febab3bc0e2cff45ed153b0cef51937031863d866ba",
        }[label]
        tuple_authority = (
            "committed Route-A release tuple"
            if label in {"C53", "C54"}
            else "committed Route-A code commit plus committed integrity hash tuple"
        )
        certificate_relative = next(
            relative for relative in expected["files"] if relative.endswith("_certificate.json")
        )
        expected_row = {
            "source": label,
            "implementation_commit": expected["implementation"],
            "provenance_commit": expected["provenance"],
            "implementation_is_ancestor_of_provenance": True,
            "tuple_authority": tuple_authority,
            "certificate_sha256": expected["files"][certificate_relative],
            "payload_sha256": expected["payload"],
            "independent_check_sha256": expected["files"]["results/independent_check.json"],
            "historical_code_results_manifest_sha256": historical,
            "committed_files": expected_committed_files,
            "commit_lock_status": "VERIFIED_GIT_OBJECTS_AND_LIVE_BYTE_IDENTITY",
        }
        if not exact_json(row, expected_row):
            raise AssertionError("complete committed release tuple mutation: " + label)
        ancestry = subprocess.run(
            ["git", "merge-base", "--is-ancestor", expected["implementation"], expected["provenance"]],
            cwd=REPOSITORY, capture_output=True, timeout=30, check=False,
        )
        if ancestry.returncode != 0:
            raise AssertionError("release ancestry failure")
        committed_rows = {item["path"]: item for item in row["committed_files"]}
        expected_paths = {
            f"{expected['project']}/{relative}": sha
            for relative, sha in expected["files"].items()
        }
        if set(committed_rows) != set(expected_paths):
            raise AssertionError("committed file inventory mutation")
        for path, expected_sha in expected_paths.items():
            committed = git_blob(expected["provenance"], path)
            live = (REPOSITORY / path).read_bytes()
            if live != committed:
                raise AssertionError("live/committed byte mismatch")
            actual_sha = hashlib.sha256(committed).hexdigest()
            if actual_sha != expected_sha or committed_rows[path]["sha256"] != expected_sha:
                raise AssertionError("committed source digest mismatch")
            if committed_rows[path]["live_equals_provenance_blob"] is not True:
                raise AssertionError("live-byte identity flag mutation")
        route = git_blob(
            expected["provenance"], f"{expected['project']}/route_a_evaluation.yaml"
        ).decode()
        if f"code_commit: {expected['implementation']}" not in route:
            raise AssertionError("committed route implementation mismatch")
        certificate_path = next(path for path in expected_paths if path.endswith("_certificate.json"))
        upstream = strict_load((REPOSITORY / certificate_path).read_bytes())
        if upstream["payload_sha256"] != expected["payload"]:
            raise AssertionError("upstream certificate payload mismatch")
    c52_path = (
        REPOSITORY
        / "henon_dynamics/henon_mu3_d12_calabi_yau_core_projector/results/c52_certificate.json"
    )
    return strict_load(c52_path.read_bytes())["payload"]


def group_from_c52(c52_payload):
    group_payload = c52_payload["projective_monomial_group"]
    rows = group_payload["elements"]
    if len(rows) != 24 or [row["id"] for row in rows] != list(range(24)):
        raise AssertionError("C52 group IDs drifted")
    elements = []
    q_scales = {}
    for row in rows:
        element = (
            tuple(row["permutation_output_to_input"]),
            tuple(row["rho_phase_exponents"]),
        )
        elements.append(element)
        q_scales[element] = row["Q_scale_rho_exponent"]
    table = group_payload["multiplication_table_by_id"]
    index = {element: i for i, element in enumerate(elements)}
    for i, left in enumerate(elements):
        for j, right in enumerate(elements):
            if index[group_multiply(left, right)] != table[i][j]:
                raise AssertionError("independent group multiplication mismatch")
    return elements, q_scales, table, group_payload["inverse_ids"]


def parse_basis(payload, monomials):
    monomial_index = {monomial: i for i, monomial in enumerate(monomials)}
    rows = payload["equivariant_tangent"]["Reynolds_basis_sparse_y2_p_i"]
    if type(rows) is not list or len(rows) != 4:
        raise AssertionError("basis row count")
    basis = []
    for sparse in rows:
        vector = [ZERO] * len(monomials)
        seen = set()
        for term in sparse:
            if set(term) != {"monomial", "coefficient"}:
                raise AssertionError("basis term schema")
            mon = term["monomial"]
            if type(mon) is not list or len(mon) != 3 or type(mon[2]) is not list:
                raise AssertionError("basis monomial schema")
            monomial = (mon[0], mon[1], tuple(mon[2]))
            if monomial in seen or monomial not in monomial_index:
                raise AssertionError("basis monomial duplicate/out of range")
            seen.add(monomial)
            vector[monomial_index[monomial]] = parse_k(term["coefficient"])
        basis.append(vector)
    return basis


def verify_tangent(payload, c52_payload):
    elements, q_scales, table, inverse_ids = group_from_c52(c52_payload)

    cubic_source = {
        tuple(3 if index == variable else 0 for index in range(N)): ONE
        for variable in range(N)
    }
    quadratic_source = {
        tuple(1 if index in edge else 0 for index in range(N)): coefficient
        for edge, coefficient in (
            [((index, index + 1), ONE) for index in range(N - 1)]
            + [((0, 7), rho_power(1))]
        )
    }

    def linear_pullback(terms, element):
        permutation, phases = element
        result = {}
        for exponent, coefficient in terms.items():
            transformed = [0] * N
            phase = 0
            for index, power in enumerate(exponent):
                transformed[permutation[index]] += power
                phase += phases[index] * power
            key = tuple(transformed)
            result[key] = add(
                result.get(key, ZERO), mul(coefficient, rho_power(phase))
            )
        return {key: value for key, value in result.items() if value != ZERO}

    covariance_tests = 0
    for element in elements:
        if linear_pullback(cubic_source, element) != cubic_source:
            raise AssertionError("independent split C covariance failure")
        covariance_tests += 1
        expected_q = {
            exponent: mul(rho_power(q_scales[element]), coefficient)
            for exponent, coefficient in quadratic_source.items()
        }
        if linear_pullback(quadratic_source, element) != expected_q:
            raise AssertionError("independent split Q covariance failure")
        covariance_tests += 1
    if payload["ambient_group_action_descent"].get(
        "split_equation_line_covariance_tests"
    ) != covariance_tests:
        raise AssertionError("split equation covariance count mutation")

    monomials = target_monomials()
    relations = relation_matrix(monomials)
    reduced_rows, pivots = rref(relations)
    if len(monomials) != 164 or len(pivots) != 81:
        raise AssertionError("independent Cayley quotient dimensions")
    pivot_row = {pivot: row for row, pivot in enumerate(pivots)}
    quotient_basis = [i for i in range(len(monomials)) if i not in pivot_row]
    monomial_index = {monomial: i for i, monomial in enumerate(monomials)}

    def reduce_vector(vector):
        result = vector[:]
        for pivot in pivots:
            coefficient = result[pivot]
            if coefficient == ZERO:
                continue
            result = [
                sub(left, mul(coefficient, right))
                for left, right in zip(result, reduced_rows[pivot_row[pivot]])
            ]
        return result

    def action(element, vector):
        q_scale = q_scales[element]
        permutation, phases = element
        determinant = mul(kint(permutation_sign(permutation)), rho_power(sum(phases)))
        residue = div(determinant, rho_power(q_scale))
        result = [ZERO] * len(monomials)
        for position, coefficient in enumerate(vector):
            if coefficient == ZERO:
                continue
            y_exp, z_exp, x_exp = monomials[position]
            transformed = [0] * N
            phase = -q_scale * z_exp
            for index, exponent in enumerate(x_exp):
                transformed[permutation[index]] += exponent
                phase += phases[index] * exponent
            image = monomial_index[(y_exp, z_exp, tuple(transformed))]
            result[image] = add(
                result[image], mul(coefficient, mul(residue, rho_power(phase)))
            )
        return reduce_vector(result)

    if payload["equivariant_tangent"]["Reynolds_seed_x_exponents"] != [
        list(seed) for seed in SEEDS
    ]:
        raise AssertionError("Reynolds seed gauge mutation")
    basis = parse_basis(payload, monomials)
    for vector in basis:
        if vector != reduce_vector(vector):
            raise AssertionError("certificate basis is not reduced")
    if matrix_rank([[vector[position] for position in quotient_basis] for vector in basis]) != 4:
        raise AssertionError("certificate basis is dependent")
    for vector in basis:
        for element in elements:
            if action(element, vector) != vector:
                raise AssertionError("certificate basis is not invariant")
    independent_basis = []
    for seed_x, expected in zip(SEEDS, basis):
        unit = [ZERO] * len(monomials)
        unit[monomial_index[(2, 0, seed_x)]] = ONE
        total = [ZERO] * len(monomials)
        for element in elements:
            image = action(element, unit)
            total = [add(left, right) for left, right in zip(total, image)]
        reynolds = [div(value, kint(24)) for value in total]
        if reynolds != expected:
            raise AssertionError("basis does not equal the frozen Reynolds seed")
        independent_basis.append(reynolds)
    expected_sparse = []
    for vector in independent_basis:
        sparse = []
        for position, coefficient in enumerate(vector):
            if coefficient == ZERO:
                continue
            y_exp, z_exp, x_exp = monomials[position]
            sparse.append({
                "monomial": [y_exp, z_exp, list(x_exp)],
                "coefficient": {
                    "a": [coefficient[0].numerator, coefficient[0].denominator],
                    "b": [coefficient[1].numerator, coefficient[1].denominator],
                },
            })
        expected_sparse.append(sparse)
    if not exact_json(
        payload["equivariant_tangent"]["Reynolds_basis_sparse_y2_p_i"],
        expected_sparse,
    ):
        raise AssertionError("noncanonical sparse Reynolds basis mutation")

    sigma = tuple((-index) % N for index in range(N))
    m_phases = tuple(1 if index and index % 2 == 0 else 0 for index in range(N))

    def descent(vector):
        result = [ZERO] * len(monomials)
        for position, coefficient in enumerate(vector):
            if coefficient == ZERO:
                continue
            y_exp, z_exp, x_exp = monomials[position]
            if z_exp:
                raise AssertionError("descent left cubic-only slice")
            transformed = [0] * N
            phase = 0
            for index, exponent in enumerate(x_exp):
                transformed[sigma[index]] += exponent
                phase += 2 * m_phases[index] * exponent
            image = monomial_index[(y_exp, z_exp, tuple(transformed))]
            result[image] = add(result[image], mul(tau(coefficient), rho_power(phase)))
        return reduce_vector(result)

    descent_columns = [
        [parse_k(value) for value in column]
        for column in payload["equivariant_tangent"]["semilinear_descent_matrix_columns"]
    ]
    if len(descent_columns) != 4 or any(len(column) != 4 for column in descent_columns):
        raise AssertionError("descent matrix shape")
    for source, column in zip(basis, descent_columns):
        expected = [ZERO] * len(monomials)
        for coefficient, vector in zip(column, basis):
            expected = [add(left, mul(coefficient, right)) for left, right in zip(expected, vector)]
        if descent(source) != expected:
            raise AssertionError("semilinear descent matrix mutation")
    for i in range(4):
        for j in range(4):
            value = ZERO
            for k in range(4):
                value = add(value, mul(descent_columns[k][i], tau(descent_columns[j][k])))
            if value != (ONE if i == j else ZERO):
                raise AssertionError("A*tau(A) failure")

    q_basis = [
        [parse_k(value) for value in column]
        for column in payload["equivariant_tangent"]["fixed_Q_basis_columns_in_e_basis"]
    ]
    expected_q_basis = [
        [ONE, ZERO, ZERO, ZERO],
        [ZERO, ONE, ZERO, ONE],
        [ZERO, (Fraction(1), Fraction(2)), ZERO, (Fraction(-1), Fraction(-2))],
        [ZERO, ZERO, (Fraction(0), Fraction(-1)), ZERO],
    ]
    if q_basis != expected_q_basis:
        raise AssertionError("canonical Q basis mutation (q0 must equal e0, not 2e0)")
    if matrix_rank([[q_basis[column][row] for column in range(4)] for row in range(4)]) != 4:
        raise AssertionError("fixed Q basis rank")
    for vector in q_basis:
        image = [ZERO] * 4
        for coefficient, column in zip(vector, descent_columns):
            for row in range(4):
                image[row] = add(image[row], mul(tau(coefficient), column[row]))
        if image != vector:
            raise AssertionError("claimed Q basis is not fixed")

    # Ambient nonconstant group action descent, independent of the producer.
    m_element = (sigma, m_phases)
    if group_multiply(m_element, canonical_element(sigma, tuple((-v) % 3 for v in m_phases))) != IDENTITY:
        raise AssertionError("M*tau(M) cocycle")
    m_inverse = group_inverse(m_element)

    # Independently replay the extension of the coordinate descent to the
    # Cayley ring.  This gate is essential because the Wp top gauge has z^3,
    # which is insensitive to confusing rho with rho^2.
    inverse_permutation, inverse_phases = m_inverse

    def descend_x_polynomial(terms):
        result = {}
        for exponent, coefficient in terms.items():
            transformed = [0] * N
            phase = 0
            for index, power in enumerate(exponent):
                transformed[inverse_permutation[index]] += power
                phase += inverse_phases[index] * power
            key = tuple(transformed)
            descended = mul(tau(coefficient), rho_power(phase))
            result[key] = add(result.get(key, ZERO), descended)
        return {key: value for key, value in result.items() if value != ZERO}

    cubic_terms = {
        tuple(3 if index == variable else 0 for index in range(N)): ONE
        for variable in range(N)
    }
    quadratic_terms = {}
    for edge, coefficient in {
        **{(index, index + 1): ONE for index in range(N - 1)},
        (0, 7): rho_power(1),
    }.items():
        quadratic_terms[tuple(1 if index in edge else 0 for index in range(N))] = coefficient
    if descend_x_polynomial(cubic_terms) != cubic_terms:
        raise AssertionError("independent D(C)=C failure")
    expected_dq = {
        exponent: mul(rho_power(2), coefficient)
        for exponent, coefficient in quadratic_terms.items()
    }
    if descend_x_polynomial(quadratic_terms) != expected_dq:
        raise AssertionError("independent D(Q)=rho^2 Q failure")
    if mul(rho_power(1), rho_power(2)) != ONE:
        raise AssertionError("independent D(F)=F failure")
    cayley_extension = payload["ambient_group_action_descent"]["Cayley_extension"]
    expected_extension = {
        "D_formula": "D(f)(x)=tau(f)(M^(-1)x)",
        "D_C_equals_C": True,
        "D_Q_equals_rho2_Q": True,
        "D_y": "y",
        "D_z": "rho*z",
        "D_F_equals_F": True,
        "quadratic_monomials_compared": 8,
        "cubic_monomials_compared": 8,
    }
    if cayley_extension != expected_extension:
        raise AssertionError("Cayley descent extension mutation")

    element_index = {element: i for i, element in enumerate(elements)}
    alpha = []
    for element in elements:
        tau_element = canonical_element(element[0], tuple((-v) % 3 for v in element[1]))
        image = group_multiply(group_multiply(m_element, tau_element), m_inverse)
        if image not in element_index:
            raise AssertionError("ambient descent transport left the group")
        alpha.append(element_index[image])
    if alpha != payload["ambient_group_action_descent"]["transported_element_ids"]:
        raise AssertionError("ambient alpha mutation")
    for left in range(24):
        for right in range(24):
            if alpha[table[left][right]] != table[alpha[left]][alpha[right]]:
                raise AssertionError("alpha not a group automorphism")
    if [i for i, image in enumerate(alpha) if i == image] != [0, 13]:
        raise AssertionError("ambient fixed geometric points")
    return {
        "basis": basis,
        "monomials": monomials,
        "q_basis": q_basis,
        "quotient_dimension": len(quotient_basis),
        "group_order": len(elements),
        "alpha": alpha,
        "inverse_ids": inverse_ids,
    }


def verify_tangent_operator_component(payload, tangent):
    source_monomials = [
        (1, 0, exponent) for exponent in compositions(3, N)
    ] + [
        (0, 1, exponent) for exponent in compositions(2, N)
    ]
    source_index = {monomial: i for i, monomial in enumerate(source_monomials)}
    edge_weights = {
        tuple(sorted((i, (i + 1) % N))): rho_power(1 if i == 7 else 0)
        for i in range(N)
    }

    def vector(terms):
        result = [ZERO] * len(source_monomials)
        for coefficient, monomial in terms:
            result[source_index[monomial]] = add(result[source_index[monomial]], coefficient)
        return result

    def dq(variable):
        terms = []
        for edge, coefficient in edge_weights.items():
            if variable in edge:
                neighbor = edge[0] if edge[1] == variable else edge[1]
                exponent = [0] * N
                exponent[neighbor] = 1
                terms.append((coefficient, tuple(exponent)))
        return terms

    relations = []
    for variable in range(N):
        for multiplier in range(N):
            exponent = [0] * N
            exponent[variable] += 2
            exponent[multiplier] += 1
            terms = [(kint(3), (1, 0, tuple(exponent)))]
            for coefficient, x_exponent in dq(variable):
                shifted = list(x_exponent)
                shifted[multiplier] += 1
                terms.append((coefficient, (0, 1, tuple(shifted))))
            relations.append(vector(terms))
    relations.append(vector([
        (ONE, (1, 0, tuple(3 if i == j else 0 for i in range(N))))
        for j in range(N)
    ]))
    relations.append(vector([
        (coefficient, (0, 1, tuple(1 if i in edge else 0 for i in range(N))))
        for edge, coefficient in edge_weights.items()
    ]))
    for multiplier in range(N):
        terms = []
        for edge, coefficient in edge_weights.items():
            exponent = [0] * N
            exponent[edge[0]] += 1
            exponent[edge[1]] += 1
            exponent[multiplier] += 1
            terms.append((coefficient, (1, 0, tuple(exponent))))
        relations.append(vector(terms))
    source_rref, source_pivots = rref(relations)
    if len(source_monomials) != 156 or len(relations) != 74 or len(source_pivots) != 73:
        raise AssertionError("independent R_(1,0) quotient failure")
    source_basis = [i for i in range(156) if i not in set(source_pivots)]

    target_monomials = tangent["monomials"]
    target_rref, target_pivots = rref(relation_matrix(target_monomials))
    target_pivot_row = {pivot: row for row, pivot in enumerate(target_pivots)}
    target_basis = [i for i in range(len(target_monomials)) if i not in target_pivot_row]
    target_index = {monomial: i for i, monomial in enumerate(target_monomials)}

    def reduce_target(value):
        result = value[:]
        for pivot in target_pivots:
            coefficient = result[pivot]
            if coefficient == ZERO:
                continue
            result = [
                sub(left, mul(coefficient, right))
                for left, right in zip(result, target_rref[target_pivot_row[pivot]])
            ]
        return result

    def times_y(value):
        result = [ZERO] * len(target_monomials)
        for position, coefficient in enumerate(value):
            if coefficient == ZERO:
                continue
            y_exp, z_exp, x_exp = source_monomials[position]
            result[target_index[(y_exp + 1, z_exp, x_exp)]] = add(
                result[target_index[(y_exp + 1, z_exp, x_exp)]], coefficient
            )
        return reduce_target(result)

    for relation in relations:
        if any(value != ZERO for value in times_y(relation)):
            raise AssertionError("times-y map is not quotient-well-defined")
    map_rows = []
    for position in source_basis:
        unit = [ZERO] * len(source_monomials)
        unit[position] = ONE
        image = times_y(unit)
        map_rows.append([image[target] for target in target_basis])
    if len(source_basis) != 83 or len(target_basis) != 83 or matrix_rank(map_rows) != 83:
        raise AssertionError("independent times-y map is not an isomorphism")
    for target_vector in tangent["basis"]:
        source = [ZERO] * len(source_monomials)
        for position, coefficient in enumerate(target_vector):
            if coefficient == ZERO:
                continue
            y_exp, z_exp, x_exp = target_monomials[position]
            if (y_exp, z_exp) != (2, 0):
                raise AssertionError("frozen H32 basis role mutation")
            source[source_index[(1, 0, x_exp)]] = coefficient
        if times_y(source) != target_vector:
            raise AssertionError("[yp_i] lift does not map to [y^2p_i]")
    claimed = payload["equivariant_tangent"]["tangent_operator_component"]
    expected_claims = {
        "ambient_piece": "S_(1,0)",
        "ambient_decomposition": {
            "y_times_cubics": 120,
            "z_times_quadrics": 36,
        },
        "ambient_dimension": 156,
        "Jacobian_relation_rows": 74,
        "Jacobian_relation_rank": 73,
        "quotient_piece": "R_(1,0)",
        "quotient_dimension": 83,
        "relation_images_under_multiply_y_tested": 74,
        "multiplication_map": "times y: R_(1,0) -> R_(2,-3)",
        "multiplication_matrix_shape": [83, 83],
        "multiplication_matrix_rank": 83,
        "multiplication_isomorphism": True,
        "frozen_operator_lift_tests": 4,
        "operator_classes": "[y*p_i]",
        "first_variation_images": "[y^2*p_i]",
    }
    if not exact_json(claimed, expected_claims):
        raise AssertionError("complete tangent operator certificate mutation")
    return {
        "ambient_dimension": 156,
        "relation_rank": 73,
        "quotient_dimension": 83,
        "times_y_rank": 83,
        "frozen_lifts": 4,
    }


def verify_infinitesimal_stabilizer():
    quadratic = list(combinations_with_replacement(range(8), 2))
    cubic = list(combinations_with_replacement(range(8), 3))
    qi = {monomial: i for i, monomial in enumerate(quadratic)}
    ci = {monomial: i for i, monomial in enumerate(cubic)}
    q_terms = [((i, i + 1), ONE) for i in range(7)] + [((0, 7), rho_power(1))]
    columns = 74
    rows2 = [[ZERO] * columns for _ in quadratic]
    for (left, right), coefficient in q_terms:
        for variable in range(8):
            row = rows2[qi[tuple(sorted((right, variable)))]]
            row[8 * left + variable] = add(row[8 * left + variable], coefficient)
            row = rows2[qi[tuple(sorted((left, variable)))]]
            row[8 * right + variable] = add(row[8 * right + variable], coefficient)
        rows2[qi[(left, right)]][64] = sub(rows2[qi[(left, right)]][64], coefficient)
    rows3 = [[ZERO] * columns for _ in cubic]
    for i in range(8):
        for variable in range(8):
            row = rows3[ci[tuple(sorted((i, i, variable)))]]
            row[8 * i + variable] = add(row[8 * i + variable], kint(3))
        rows3[ci[(i, i, i)]][65] = sub(rows3[ci[(i, i, i)]][65], ONE)
    for l_index in range(8):
        for (left, right), coefficient in q_terms:
            row = rows3[ci[tuple(sorted((l_index, left, right)))]]
            row[66 + l_index] = sub(row[66 + l_index], coefficient)
    rows = rows2 + rows3
    if matrix_rank(rows) != 73:
        raise AssertionError("independent Lie stabilizer rank")
    scalar_kernel = [ZERO] * columns
    for index in range(8):
        scalar_kernel[8 * index + index] = ONE
    scalar_kernel[64] = kint(2)
    scalar_kernel[65] = kint(3)
    for row in rows:
        value = ZERO
        for coefficient, coordinate in zip(row, scalar_kernel):
            value = add(value, mul(coefficient, coordinate))
        if value != ZERO:
            raise AssertionError("(I8,2,3,0) is not the Lie kernel generator")
    # Rank 73 in 74 variables plus this nonzero kernel vector proves that the
    # entire kernel is its one-dimensional span.
    return {
        "matrix_shape": [156, 74],
        "rank": 73,
        "kernel_dimension": 1,
        "kernel_generator": "lambda*(I8,2,3,0)",
        "projective_nullity": 0,
    }


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"({value.numerator}/{value.denominator})"


def k_text(value: K) -> str:
    a, b = value
    if b == 0:
        return fraction_text(a)
    if a == 0:
        return f"({fraction_text(b)})*rho"
    return f"({fraction_text(a)}+({fraction_text(b)})*rho)"


def x_monomial(exponents) -> str:
    factors = []
    for index, exponent in enumerate(exponents):
        if exponent == 1:
            factors.append(f"x{index}")
        elif exponent:
            factors.append(f"x{index}^{exponent}")
    return "*".join(factors) if factors else "1"


def p_text(vector, monomials) -> str:
    terms = []
    for position, coefficient in enumerate(vector):
        if coefficient == ZERO:
            continue
        y_exp, z_exp, x_exp = monomials[position]
        if (y_exp, z_exp, sum(x_exp)) != (2, 0, 3):
            raise AssertionError("basis y degree mutation")
        terms.append(f"({k_text(coefficient)})*{x_monomial(x_exp)}")
    return "+".join(terms).replace("+-", "-")


def independent_semilinear_raw_top(source_x, y_exponent, z_exponent):
    """Compute D of a raw top monomial from the inverse cocycle arithmetic."""
    sigma = tuple((-index) % N for index in range(N))
    m_phases = tuple(1 if index and index % 2 == 0 else 0 for index in range(N))
    inverse_permutation, inverse_phases = group_inverse((sigma, m_phases))
    image_x = [0] * N
    x_phase_exponent = 0
    for index, power in enumerate(source_x):
        image_x[inverse_permutation[index]] += power
        x_phase_exponent += inverse_phases[index] * power
    x_prefactor = rho_power(x_phase_exponent)
    z_prefactor = rho_power(z_exponent)  # Independently use D(z)=rho*z.
    return {
        "image_x": tuple(image_x),
        "image_y": y_exponent,
        "image_z": z_exponent,
        "x_prefactor": x_prefactor,
        "z_prefactor": z_prefactor,
        "total_prefactor": mul(x_prefactor, z_prefactor),
    }


def independent_raw_top_text(raw) -> str:
    factors = [x_monomial(raw["image_x"])]
    if raw["image_y"]:
        factors.append("y" if raw["image_y"] == 1 else f"y^{raw['image_y']}")
    if raw["image_z"]:
        factors.append("z" if raw["image_z"] == 1 else f"z^{raw['image_z']}")
    return f"({k_text(raw['total_prefactor'])})*" + "*".join(factors)


def parse_singular_k(text: str) -> K:
    rho = sp.Symbol("rho")
    expression = sp.expand(sp.sympify(text.replace("^", "**"), locals={"rho": rho}))
    polynomial = sp.Poly(expression, rho, domain=sp.QQ)
    if polynomial.degree() > 1:
        raise AssertionError("Singular K number not reduced")
    a = polynomial.coeff_monomial(1)
    b = polynomial.coeff_monomial(rho)
    return Fraction(int(a.p), int(a.q)), Fraction(int(b.p), int(b.q))


def run_Wp_yukawa(tangent):
    source_x = (0, 0, 0, 0, 0, 0, 0, 6)
    raw_top = independent_semilinear_raw_top(source_x, 2, 3)
    if raw_top != {
        "image_x": (0, 6, 0, 0, 0, 0, 0, 0),
        "image_y": 2,
        "image_z": 3,
        "x_prefactor": ONE,
        "z_prefactor": ONE,
        "total_prefactor": ONE,
    }:
        raise AssertionError("programmatic Wp raw top descent drifted")
    lines = [
        "ring r=(0,rho),(x0,x1,x2,x3,x4,x5,x6,x7,y,z),Wp(1,1,1,1,1,1,1,1,1,2);",
        "minpoly=rho^2+rho+1;",
        "option(redSB);",
        "poly C=x0^3+x1^3+x2^3+x3^3+x4^3+x5^3+x6^3+x7^3;",
        "poly Q=x0*x1+x1*x2+x2*x3+x3*x4+x4*x5+x5*x6+x6*x7+rho*x7*x0;",
        "poly F=y*C+z*Q;",
        "ideal J=jacob(F);",
        "ideal JR=J[10],J[9],J[8],J[7],J[6],J[5],J[4],J[3],J[2],J[1];",
        "ideal G=std(JR);",
        '"GSIZE",size(G);',
    ]
    for index, vector in enumerate(tangent["basis"]):
        lines.append(f"poly p{index}={p_text(vector, tangent['monomials'])};")
    lines.extend([
        f"poly DTOP=reduce({independent_raw_top_text(raw_top)},G);",
        '"DTOPC",leadcoef(DTOP);',
        '"DTOPE",leadexp(DTOP);',
    ])
    for i, j, k in combinations_with_replacement(range(4), 3):
        label = f"{i}{j}{k}"
        lines.extend([
            f"poly T{label}=reduce(y^5*p{i}*p{j}*p{k},G);",
            f'"T{label}",leadcoef(T{label});',
            f'"E{label}",leadexp(T{label});',
        ])
    lines.append("quit;")
    with tempfile.TemporaryDirectory(prefix="c55-check-Wp-") as temporary:
        script = Path(temporary) / "checker.sing"
        script.write_text("\n".join(lines) + "\n", encoding="utf-8")
        process = subprocess.run(
            ["Singular", "-q", str(script)], capture_output=True, text=True,
            timeout=180, check=False,
        )
    if process.returncode != 0 or re.search(r"^\s*\?", process.stdout, re.MULTILINE):
        raise AssertionError("independent Wp backend failed: " + process.stderr[-2000:])
    match = re.search(r"^GSIZE\s+(\d+)\s*$", process.stdout, re.MULTILINE)
    if match is None or int(match.group(1)) != 329:
        raise AssertionError("independent Wp Groebner size")
    traces = {}
    exponents = set()
    for triple in combinations_with_replacement(range(4), 3):
        label = "".join(map(str, triple))
        coefficient = re.search(rf"^T{label}\s+(.+?)\s*$", process.stdout, re.MULTILINE)
        exponent = re.search(rf"^E{label}\s+([0-9,]+)\s*$", process.stdout, re.MULTILINE)
        if coefficient is None or exponent is None:
            raise AssertionError("independent Wp trace missing")
        traces[triple] = parse_singular_k(coefficient.group(1))
        exponents.add(tuple(int(value) for value in exponent.group(1).split(",")))
    expected_top = (0, 0, 0, 0, 0, 0, 0, 6, 2, 3)
    if exponents != {expected_top}:
        raise AssertionError("independent Wp top trace gauge")
    descent_coefficient = re.search(
        r"^DTOPC\s+(.+?)\s*$", process.stdout, re.MULTILINE
    )
    descent_exponent = re.search(
        r"^DTOPE\s+([0-9,]+)\s*$", process.stdout, re.MULTILINE
    )
    if descent_coefficient is None or descent_exponent is None:
        raise AssertionError("independent Wp top descent missing")
    if tuple(int(value) for value in descent_exponent.group(1).split(",")) != expected_top:
        raise AssertionError("independent top descent left Wp gauge")
    descent_scalar = parse_singular_k(descent_coefficient.group(1))
    if mul(descent_scalar, tau(descent_scalar)) != ONE:
        raise AssertionError("independent top descent cocycle")
    return traces, descent_scalar, {
        "ordering": "Wp(1,1,1,1,1,1,1,1,1,2)",
        "reversed_Jacobian_generator_order": True,
        "Groebner_basis_size": 329,
        "top_trace_monomial": "x7^6*y^2*z^3",
        "top_descent_raw_image_before_quotient": "x1^6*y^2*z^3",
        "top_descent_scalar": {
            "a": [descent_scalar[0].numerator, descent_scalar[0].denominator],
            "b": [descent_scalar[1].numerator, descent_scalar[1].denominator],
        },
        "top_descent_cocycle": True,
        "stdout_sha256": hashlib.sha256(process.stdout.encode()).hexdigest(),
    }


def multinomial(triple):
    counts = Counter(triple)
    denominator = reduce(lambda a, b: a * math.factorial(b), counts.values(), 1)
    return math.factorial(3) // denominator


def normalized_primitive(traces, q_basis):
    coefficients = {
        tuple(exponents): ZERO
        for exponents in product(range(4), repeat=4)
        if sum(exponents) == 3
    }
    for triple, trace in traces.items():
        tensor_coefficient = mul(kint(multinomial(triple)), trace)
        for a, b, c in product(range(4), repeat=3):
            change = mul(q_basis[a][triple[0]], mul(q_basis[b][triple[1]], q_basis[c][triple[2]]))
            if change == ZERO:
                continue
            exponent = [0, 0, 0, 0]
            exponent[a] += 1
            exponent[b] += 1
            exponent[c] += 1
            key = tuple(exponent)
            coefficients[key] = add(coefficients[key], mul(tensor_coefficient, change))
    base = coefficients[(3, 0, 0, 0)]
    ratios = {}
    for exponent, coefficient in coefficients.items():
        ratio = div(coefficient, base)
        if ratio[1] != 0:
            raise AssertionError("independent Q descent failed")
        ratios[exponent] = ratio[0]
    common_denominator = math.lcm(*(value.denominator for value in ratios.values()))
    integers = {key: int(value * common_denominator) for key, value in ratios.items()}
    divisor = math.gcd(*(abs(value) for value in integers.values()))
    primitive = {key: value // divisor for key, value in integers.items()}
    if primitive[(3, 0, 0, 0)] < 0:
        primitive = {key: -value for key, value in primitive.items()}
    return primitive, base


def primitive_from_payload(payload):
    rows = payload["rational_cubic_surface"]["primitive_integral_coefficients"]
    result = {}
    for row in rows:
        if set(row) != {"exponents_u0_to_u3", "coefficient"}:
            raise AssertionError("primitive row schema")
        exponent = row["exponents_u0_to_u3"]
        coefficient = row["coefficient"]
        if type(exponent) is not list or len(exponent) != 4 or any(type(value) is not int or value < 0 for value in exponent):
            raise AssertionError("primitive exponent type")
        if sum(exponent) != 3 or type(coefficient) is not int:
            raise AssertionError("primitive homogeneous/type mutation")
        key = tuple(exponent)
        if key in result:
            raise AssertionError("duplicate primitive monomial")
        result[key] = coefficient
    if len(result) != 20 or any(value == 0 for value in result.values()):
        raise AssertionError("primitive support mutation")
    canonical_rows = [
        {"exponents_u0_to_u3": list(exponent), "coefficient": result[exponent]}
        for exponent in sorted(result, reverse=True)
    ]
    if hashlib.sha256(canonical_json(canonical_rows)).hexdigest() != EXPECTED_PRIMITIVE_SHA256:
        raise AssertionError("primitive coefficient hash")
    return result


def cubic_text(primitive):
    terms = []
    for exponent in sorted(primitive, reverse=True):
        factors = []
        for index, power in enumerate(exponent):
            if power == 1:
                factors.append(f"u{index}")
            elif power:
                factors.append(f"u{index}^{power}")
        terms.append(f"({primitive[exponent]})*{'*'.join(factors)}")
    return "+".join(terms).replace("+-", "-")


def independent_smoothness(primitive):
    script_text = "\n".join([
        "ring q=0,(u3,u2,u1,u0),Dp;",
        f"poly Y={cubic_text(primitive)};",
        "ideal D=jacob(Y);",
        "ideal DR=D[4],D[3],D[2],D[1];",
        "ideal G=std(DR);",
        '"VDIM",vdim(G);',
        '"GSIZE",size(G);',
        '"HILB";',
        "hilb(G,1);",
        "quit;",
    ]) + "\n"
    with tempfile.TemporaryDirectory(prefix="c55-check-smooth-") as temporary:
        script = Path(temporary) / "smooth.sing"
        script.write_text(script_text, encoding="utf-8")
        process = subprocess.run(
            ["Singular", "-q", str(script)], capture_output=True, text=True,
            timeout=90, check=False,
        )
    if process.returncode != 0 or re.search(r"^\s*\?", process.stdout, re.MULTILINE):
        raise AssertionError("independent smoothness backend failed: " + process.stderr[-2000:])
    vdim = re.search(r"^VDIM\s+(\d+)\s*$", process.stdout, re.MULTILINE)
    size = re.search(r"^GSIZE\s+(\d+)\s*$", process.stdout, re.MULTILINE)
    hilbert = re.search(r"^HILB\s*\n([^\n]+)", process.stdout, re.MULTILINE)
    if vdim is None or size is None or hilbert is None:
        raise AssertionError("independent smoothness output missing")
    numerator = [int(value) for value in hilbert.group(1).split(",")]
    if int(vdim.group(1)) != 16 or numerator != [1, 0, -4, 0, 6, 0, -4, 0, 1, 0]:
        raise AssertionError("independent Jacobian length/Hilbert failure")
    variables = sp.symbols("u0:4")
    expression = 0
    for exponent, coefficient in primitive.items():
        term = coefficient
        for variable, power in zip(variables, exponent):
            term *= variable**power
        expression += term
    content, factors = sp.factor_list(expression, *variables)
    if abs(int(content)) != 1 or len(factors) != 1 or factors[0][1] != 1:
        raise AssertionError("independent Q irreducibility failure")
    return {
        "ordering": "Dp with reversed variable and Jacobian-generator order",
        "Jacobian_quotient_length": 16,
        "Jacobian_Groebner_basis_size": int(size.group(1)),
        "Hilbert_numerator": numerator,
        "factor_degrees_over_Q": [sp.Poly(factors[0][0], *variables).total_degree()],
        "homogeneous_Jacobian_ideal_zero_dimensional": True,
        "projective_singular_locus_empty": True,
        "stdout_sha256": hashlib.sha256(process.stdout.encode()).hexdigest(),
    }


GATE_NAMES = (
    "G00_ENVELOPE_PAYLOAD_SCHEMA_DIGESTS",
    "G01_COMPLETE_SCALAR_CLASSIFICATION",
    "G02_COMMITTED_UPSTREAM_PROVENANCE",
    "G03_COMPLETE_INTERSECTION_AND_LIE_STABILIZER",
    "G04_EQUIVARIANT_CAYLEY_TANGENT",
    "G05_R10_TIMES_Y_ISOMORPHISM",
    "G06_AMBIENT_GROUP_AND_CAYLEY_DESCENT",
    "G07_DIRECT_CUBE_INTERPOLATION_AND_MULTINOMIALS",
    "G08_TOP_LINE_SEMILINEAR_Q_GENERATOR",
    "G09_INDEPENDENT_WP_RAW_TRACE_GAUGE",
    "G10_PRIMITIVE_RATIONAL_CUBIC",
    "G11_SMOOTH_GEOMETRICALLY_IRREDUCIBLE_SURFACE",
    "G12_REALIZATION_AND_ROLE_FIREWALLS",
)


def verify(certificate: dict[str, Any], raw: bytes) -> dict[str, Any]:
    passed_gates: set[str] = set()
    if set(certificate) != {"schema", "payload_sha256", "payload"}:
        raise AssertionError("certificate envelope keys")
    if certificate["schema"] != "hcs-c55-certificate-v1":
        raise AssertionError("certificate schema")
    payload = certificate["payload"]
    if type(payload) is not dict:
        raise AssertionError("payload type")
    actual_payload_sha = hashlib.sha256(canonical_json(payload)).hexdigest()
    if certificate["payload_sha256"] != actual_payload_sha:
        raise AssertionError("internal payload digest")
    if actual_payload_sha != EXPECTED_PAYLOAD_SHA256:
        raise AssertionError("immutable payload digest")
    actual_schema_sha = hashlib.sha256(canonical_json(schema_descriptor(payload))).hexdigest()
    if EXPECTED_SCHEMA_SHA256 != "TO_BE_LOCKED" and actual_schema_sha != EXPECTED_SCHEMA_SHA256:
        raise AssertionError("immutable schema descriptor")
    passed_gates.add("G00_ENVELOPE_PAYLOAD_SCHEMA_DIGESTS")
    scalar_inventory = validate_scalar_inventory(payload)
    passed_gates.add("G01_COMPLETE_SCALAR_CLASSIFICATION")
    c52_payload = verify_provenance(payload)
    passed_gates.add("G02_COMMITTED_UPSTREAM_PROVENANCE")
    tangent = verify_tangent(payload, c52_payload)
    passed_gates.add("G04_EQUIVARIANT_CAYLEY_TANGENT")
    passed_gates.add("G06_AMBIENT_GROUP_AND_CAYLEY_DESCENT")
    tangent_operator = verify_tangent_operator_component(payload, tangent)
    passed_gates.add("G05_R10_TIMES_Y_ISOMORPHISM")
    lie = verify_infinitesimal_stabilizer()
    passed_gates.add("G03_COMPLETE_INTERSECTION_AND_LIE_STABILIZER")

    triple_rows = payload["cayley_Yukawa"]["symmetric_traces_in_e_basis"]
    if len(triple_rows) != 20:
        raise AssertionError("symmetric trace row count")
    seen_triples = set()
    certificate_traces = {}
    expected_triple_order = list(combinations_with_replacement(range(4), 3))
    for expected_triple, row in zip(expected_triple_order, triple_rows):
        if type(row) is not dict or set(row) != {
            "indices", "trace_coefficient", "polynomial_multiplicity"
        }:
            raise AssertionError("trace row schema mutation")
        triple = tuple(row["indices"])
        if triple != expected_triple:
            raise AssertionError("noncanonical symmetric trace row order")
        if triple not in combinations_with_replacement(range(4), 3):
            raise AssertionError("trace index mutation")
        if triple in seen_triples:
            raise AssertionError("duplicate trace")
        seen_triples.add(triple)
        certificate_traces[triple] = parse_k(row["trace_coefficient"])
        if row["polynomial_multiplicity"] != multinomial(triple):
            raise AssertionError("mixed-term multinomial mutation")

    direct = payload["cayley_Yukawa"]["producer_direct_cube"]
    expected_direct_metadata = {
        "expression": "y^5*(a0*p0+a1*p1+a2*p2+a3*p3)^3",
        "direct_reductions": 20,
        "evaluation_matrix_rank": 20,
        "interpolation_monomial_count": 20,
        "unordered_traces_derived_by_dividing_mixed_coefficients_by_1_3_6": True,
        "generic_parameter_Groebner_backend_used": False,
    }
    for key, expected in expected_direct_metadata.items():
        if key not in direct or not exact_json(direct[key], expected):
            raise AssertionError("direct-cube metadata mutation: " + key)
    if set(direct) != {
        "expression",
        "evaluation_points",
        "evaluation_values_in_producer_top_gauge",
        "direct_reductions",
        "evaluation_matrix_rank",
        "interpolation_monomial_count",
        "unordered_traces_derived_by_dividing_mixed_coefficients_by_1_3_6",
        "generic_parameter_Groebner_backend_used",
    }:
        raise AssertionError("direct-cube subtree schema mutation")
    points = tuple(tuple(point) for point in direct["evaluation_points"])
    if points != DIRECT_CUBE_POINTS:
        raise AssertionError("direct-cube point gauge mutation")
    direct_values = [parse_k(value) for value in direct["evaluation_values_in_producer_top_gauge"]]
    if len(direct_values) != 20:
        raise AssertionError("direct-cube value count")
    for point, direct_value in zip(points, direct_values):
        reconstructed = ZERO
        for triple, trace in certificate_traces.items():
            point_monomial = math.prod(point[index] for index in triple)
            reconstructed = add(
                reconstructed,
                mul(kint(multinomial(triple) * point_monomial), trace),
            )
        if reconstructed != direct_value:
            raise AssertionError("direct-cube value does not reconstruct from 1/3/6 tensor")
    evaluation_matrix = [
        [
            kint(math.prod(point[index] ** exponent for index, exponent in enumerate(monomial)))
            for monomial in sorted(
                (
                    (a, b, c, 3 - a - b - c)
                    for a in range(4)
                    for b in range(4 - a)
                    for c in range(4 - a - b)
                ),
                reverse=True,
            )
        ]
        for point in points
    ]
    if matrix_rank(evaluation_matrix) != 20:
        raise AssertionError("direct-cube interpolation matrix rank")
    passed_gates.add("G07_DIRECT_CUBE_INTERPOLATION_AND_MULTINOMIALS")

    producer_top = payload["cayley_Yukawa"]["top_line_semilinear_descent"]
    producer_source_x = (0, 0, 0, 0, 0, 0, 2, 2)
    producer_raw_top = independent_semilinear_raw_top(producer_source_x, 0, 5)
    if producer_raw_top != {
        "image_x": (0, 2, 2, 0, 0, 0, 0, 0),
        "image_y": 0,
        "image_z": 5,
        "x_prefactor": rho_power(1),
        "z_prefactor": rho_power(2),
        "total_prefactor": ONE,
    }:
        raise AssertionError("independent programmatic wp raw-image arithmetic")
    expected_top_descent_strings = {
        "ring_descent": "tau on K, x maps by M^(-1), y maps to y, z maps to rho*z",
        "compatibility_identity": "Q_(rho^2)(M^(-1)x)=rho^2*Q_rho(x), hence D(z)=rho*z; raw x6^2*x7^2 -> rho*x1^2*x2^2, z^5 -> rho^2*z^5, total prefactor 1 before quotient",
        "producer_top_gauge": "x6^2*x7^2*z^5",
    }
    for key, expected in expected_top_descent_strings.items():
        if producer_top.get(key) != expected:
            raise AssertionError("producer raw top descent mutation: " + key)
    producer_d = parse_k(producer_top["raw_image_quotient_reduction_scalar"])
    producer_fixed_scale = parse_k(producer_top["fixed_Q_generator_coefficient"])
    rational_common_scale = parse_k(
        payload["rational_cubic_surface"]["common_K_trace_scale"]
    )
    if rational_common_scale != producer_fixed_scale:
        raise AssertionError("rational cubic common scale/top fixed generator mismatch")
    if mul(producer_d, tau(producer_d)) != ONE:
        raise AssertionError("producer top-line cocycle mutation")
    if producer_d != div(producer_fixed_scale, tau(producer_fixed_scale)):
        raise AssertionError("producer fixed top generator mutation")
    passed_gates.add("G08_TOP_LINE_SEMILINEAR_Q_GENERATOR")

    independent_traces, independent_top_d, Wp_report = run_Wp_yukawa(tangent)
    common_ratios = {
        div(independent_traces[triple], certificate_traces[triple])
        for triple in certificate_traces
    }
    if len(common_ratios) != 1 or ZERO in common_ratios:
        raise AssertionError("raw 20-trace tensors differ by more than one K* gauge")
    passed_gates.add("G09_INDEPENDENT_WP_RAW_TRACE_GAUGE")
    independent_primitive, independent_base = normalized_primitive(
        independent_traces, tangent["q_basis"]
    )
    if independent_top_d != div(independent_base, tau(independent_base)):
        raise AssertionError("independent Wp top descent/rational scale mismatch")
    certificate_primitive = primitive_from_payload(payload)
    if independent_primitive != certificate_primitive:
        raise AssertionError("independent Wp projective cubic mismatch")
    passed_gates.add("G10_PRIMITIVE_RATIONAL_CUBIC")
    smoothness = independent_smoothness(certificate_primitive)
    expected_factorization = [{"degree": 3, "multiplicity": 1}]
    if not exact_json(
        payload["rational_cubic_surface"]["factorization_over_Q"],
        expected_factorization,
    ):
        raise AssertionError("producer Q-factorization certificate mutation")
    expected_producer_smoothness = {
        "ordering": "dp",
        "jacobian_quotient_length": 16,
        "jacobian_groebner_size": 12,
        "hilbert_numerator": [1, 0, -4, 0, 6, 0, -4, 0, 1, 0],
        "expected_complete_intersection_length": 16,
        "projective_singular_locus_empty": True,
    }
    if not exact_json(
        payload["rational_cubic_surface"]["producer_smoothness_backend"],
        expected_producer_smoothness,
    ):
        raise AssertionError("producer smoothness subtree mutation")
    passed_gates.add("G11_SMOOTH_GEOMETRICALLY_IRREDUCIBLE_SURFACE")

    expected_firewalls = {
        "equal_Hodge_numbers_imply_VHS": False,
        "projective_Yukawa_match_sufficient_for_VHS": False,
        "projective_Yukawa_mismatch_obstructs_pointed_polarized_VHS_isomorphism": (
            "written theorem, not CAS output"
        ),
        "finite_prime_matches_prove_motive": False,
        "algebraic_correspondence_constructed": False,
        "honest_CY3_realization_claimed": False,
        "motive_isomorphism_claimed": False,
    }
    if not exact_json(payload["realization_firewalls"], expected_firewalls):
        raise AssertionError("realization firewall mutation")
    if payload["artifact_status"] != "RELEASE_CANDIDATE":
        raise AssertionError("artifact status mutation or release rollback")
    role_firewall = payload["equivariant_tangent"]["class_role_firewall"]
    if (
        role_firewall.get("direct_multiplication_of_contracted_R_2_minus3_classes_used")
        is not False
        or role_firewall.get("four_y_degree_layers_are_distinct") is not True
        or role_firewall.get("not_a_literal_linear_equivariant_family") is not True
    ):
        raise AssertionError("Cayley/VHS class-role firewall mutation")
    passed_gates.add("G12_REALIZATION_AND_ROLE_FIREWALLS")
    if passed_gates != set(GATE_NAMES):
        missing = sorted(set(GATE_NAMES) - passed_gates)
        extra = sorted(passed_gates - set(GATE_NAMES))
        raise AssertionError(f"gate execution mismatch missing={missing} extra={extra}")
    return {
        "schema": "hcs-c55-independent-check-v1",
        "result": "PASS",
        "certificate_sha256": hashlib.sha256(raw).hexdigest(),
        "payload_sha256": actual_payload_sha,
        "schema_descriptor_sha256": actual_schema_sha,
        "semantic_gate_count": len(GATE_NAMES),
        "executed_gate_names": list(GATE_NAMES),
        "central_semantic_leaf_count": scalar_inventory["central"],
        "derived_scalar_leaf_count": scalar_inventory["derived"],
        "nonsemantic_allowlist_count": scalar_inventory["nonsemantic"],
        "total_scalar_leaf_count": scalar_inventory["total"],
        "committed_upstream_release_count": 3,
        "independent_tangent": {
            "Cayley_quotient_dimension": tangent["quotient_dimension"],
            "Reynolds_basis_dimension": 4,
            "semilinear_fixed_Q_dimension": 4,
            "ambient_group_order": tangent["group_order"],
            "ambient_descent_automorphism_tests": 576,
            "tangent_operator_component": tangent_operator,
        },
        "independent_infinitesimal_stabilizer": lie,
        "independent_Yukawa_backend": Wp_report,
        "independent_rational_cubic": {
            "coefficient_count": len(certificate_primitive),
            "coefficient_gcd": math.gcd(*(abs(value) for value in certificate_primitive.values())),
            "primitive_coefficients_sha256": EXPECTED_PRIMITIVE_SHA256,
            "mixed_multinomial_factors_verified": True,
            "producer_direct_cube_evaluations_reconstructed": 20,
            "raw_trace_common_Kstar_gauge_verified": True,
            "top_line_semilinear_Q_generator_verified_in_both_orders": True,
            "q0_equals_e0_not_2e0": True,
        },
        "independent_smoothness": smoothness,
        "firewalls": {
            "direct_R_2_minus3_multiplication_rejected": True,
            "third_variation_y4_then_pairing_y5": True,
            "smoothness_not_inferred_from_Q_factorization_alone": True,
            "Yukawa_match_not_promoted_to_VHS_or_motive": True,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    arguments = parser.parse_args()
    if arguments.output.exists():
        arguments.output.unlink()
    if sys.flags.optimize:
        raise SystemExit("optimized Python is forbidden for certificate checking")
    try:
        raw = arguments.certificate.read_bytes()
        certificate = strict_load(raw)
        report = verify(certificate, raw)
    except Exception as error:
        print(f"C55 CHECK FAIL: {error}", file=sys.stderr)
        return 1
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print("C55 CHECK PASS")
    print(f"semantic_gates={report['semantic_gate_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
