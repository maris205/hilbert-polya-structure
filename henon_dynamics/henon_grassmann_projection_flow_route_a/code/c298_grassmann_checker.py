#!/usr/bin/env python3
"""Independent exact checker for HCS-C298; imports no producer code."""
from __future__ import annotations

import argparse
import ast
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "f8d3ad9a8940b54e82854b2924be353575ed8fcb"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
TUPLE = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]
EVIDENCE_KEYS = {
    "schema", "candidate_id", "obstruction_id", "evaluation_date", "fixed_epoch", "source_commit",
    "scope_literal", "evaluator", "model", "theorem_contract", "proof_contract",
    "enumeration", "route_a", "scope_flags", "nonclaims", "collision_boundary",
    "references", "payload_sha256",
}
ENUM_KEYS = {
    "simple_cases", "repeated_cases", "morse_bott_atlases", "simple_case_count",
    "repeated_case_count", "simple_plucker_support_cells",
    "repeated_plucker_support_cells", "linear_mode_cells",
    "morse_bott_component_rows", "audited_cell_count",
}
YAML_KEYS = {
    "schema", "candidate_id", "title", "evaluation_date", "source_commit", "fixed_epoch",
    "scope_literal", "evaluator_authority", "evaluator_version", "evaluator_authority_sha256",
    "obstruction_id", "candidate_definition", "family", "phase_space", "dynamics", "parameters",
    "parameter_provenance", "arithmetic_origin", "clock", "normalization", "determinant_convention",
    "orbit_cutoff", "precision", "training_data", "forbidden_data", "artifact_paths", "a0", "a1",
    "a2", "a3", "a4", "tuple", "overall_verdict", "route_b_invocation_allowed",
    "route_b_lock_reason", "scope_flags", "theorem_status", "finite_evidence_role",
    "source_owner_tokens",
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
EXPECTED_EVALUATION = {
    "schema": "route-a-evaluation-v0.2.0",
    "candidate_id": "HCS-C298",
    "title": "Exact Grassmann projection flow and Schubert--Morse--Bott atlas",
    "evaluation_date": "2026-09-02",
    "source_commit": SOURCE,
    "fixed_epoch": 1788307200,
    "scope_literal": SCOPE,
    "evaluator_authority": "route-a-evaluator",
    "evaluator_version": "0.2.0",
    "evaluator_authority_sha256": EVALUATOR,
    "obstruction_id": "HEN-O282",
    "candidate_definition": "Rank-k real orthogonal projections evolving by dot(P)=[P,[P,A]] for a fixed real symmetric matrix A.",
    "family": "Grassmann gradient and continuous subspace power flow",
    "phase_space": "real Grassmannian Gr(k,n) represented by rank-k orthogonal projections",
    "dynamics": "positive gradient flow of P maps to Tr(AP)",
    "parameters": "n>=2; 1<=k<=n-1; A=A^T real",
    "parameter_provenance": "all finite dimensions and both simple and repeated spectra are covered",
    "arithmetic_origin": "none; eigenvalue and Plucker weights are source-linear-algebra data",
    "clock": "continuous real time t",
    "normalization": "orthogonal projection represents an unoriented subspace",
    "determinant_convention": "Plucker coordinates are projective and defined up to one common nonzero scale",
    "orbit_cutoff": "global exact theorem; finite cases are regression evidence only",
    "precision": "exact integers and rationals in evidence; symbolic identities in SymPy",
    "training_data": "none",
    "forbidden_data": "target arithmetic local data, Euler factors, root numbers, automorphy, target divisor laws, target functional equations, target zeros, and Hilbert--Polya operators",
    "artifact_paths": [
        "results/c298_grassmann_evidence.json",
        "THEOREM_PACKAGE.md",
        "paper/main.pdf",
    ],
    "a0": {
        "verdict": "A0_FAIL",
        "evidence_status": "exact negative classification",
        "strongest_evidence": "the flow has finite-dimensional eigenvalue and Plucker weights",
        "strongest_failure": "no arithmetic local datum or target Euler factor is constructed",
        "artifacts": ["THEOREM_PACKAGE.md", "SOURCE_AUDIT.md"],
    },
    "a1": {
        "verdict": "A1_FAIL",
        "evidence_status": "strict Lyapunov obstruction",
        "strongest_evidence": "every orbit has an exact invariant-subspace limit",
        "strongest_failure": "nonconstant recurrence and primitive periodic-orbit repetition are absent",
        "artifacts": ["THEOREM_PACKAGE.md", "paper/main.pdf"],
    },
    "a2": {
        "verdict": "A2_FAIL",
        "evidence_status": "exact negative classification",
        "strongest_evidence": "continuous time gives explicit exponential weights",
        "strongest_failure": "time is not an arithmetic clock or logarithmic prime norm",
        "artifacts": ["THEOREM_PACKAGE.md"],
    },
    "a3": {
        "verdict": "A3_FAIL",
        "evidence_status": "exact negative classification",
        "strongest_evidence": "exterior-power coordinates give finite exponential sums",
        "strongest_failure": "no target completed function or target functional equation is present",
        "artifacts": ["THEOREM_PACKAGE.md", "results/c298_grassmann_evidence.json"],
    },
    "a4": {
        "verdict": "A4_FORMAL_HINT",
        "evidence_status": "analogy only",
        "strongest_evidence": "a fixed symmetric generator orders subspaces by its eigenspaces",
        "strongest_failure": "the flow is dissipative gradient dynamics and A is not a certified Hilbert--Polya operator",
        "artifacts": ["SOURCE_AUDIT.md", "paper/main.pdf"],
    },
    "tuple": TUPLE,
    "overall_verdict": "ROUTE_A_REJECTED",
    "route_b_invocation_allowed": False,
    "route_b_lock_reason": "no bad-prime, Euler-factor, or root-number datum exists under the frozen scope",
    "scope_flags": FLAGS,
    "theorem_status": "PROVABLE_AS_STATED",
    "finite_evidence_role": "regression evidence only; global solution, limits, and Morse--Bott structure are analytic",
    "source_owner_tokens": [
        "10.1007/BF00275687",
        "10.1016/0024-3795(91)90021-N",
        "hdl:2078.5/90452",
    ],
}
MODEL = {
    "state": "rank-k real orthogonal projection P",
    "generator": "real symmetric n-by-n matrix A",
    "flow": "dot(P)=[P,[P,A]]",
    "exact_range": "Ran(P(t))=exp(tA)Ran(P0)",
    "clock": "continuous real time t",
    "normalization": "orthogonal projector represents an unoriented k-plane",
}
THEOREM = {
    "global_solution": "P(t)=Y(t)(Y(t)^T Y(t))^(-1)Y(t)^T with Y(t)=exp(tA)Q0",
    "plucker": "p_I(t) is projectively exp(t sum_{i in I}lambda_i)p_I(0)",
    "simple_limit": "each eigenflag Schubert cell converges to its greedy coordinate k-plane",
    "simple_rate": "the actual second nonzero Plucker weight determines the exact exponential rate",
    "equilibria": "all and only A-invariant rank-k orthogonal projections",
    "linearization": "mode Hom(e_i,e_j) has rate lambda_j-lambda_i",
    "repeated_spectrum": "critical sets are product-Grassmann Morse-Bott manifolds and every orbit has an associated-graded limit",
    "recurrence": "Tr(AP) is strict off equilibria, excluding nonconstant recurrence",
}
PROOF = {
    "quotient_flow": "differentiate the orthogonal projector onto exp(tA)Ran(P0)",
    "matroid_guard": "nonzero Plucker indices are bases of a representable matroid; distinct element weights give a unique greedy maximum",
    "tie_guard": "arbitrary subset sums may tie and are never assumed distinct",
    "rate_guard": "the gap is defined from actual nonzero Plucker support, not from the ambient subset list",
    "degenerate_limit": "an eigenflag-adapted basis yields the associated graded subspace",
    "morse_bott": "within-block modes are tangent and cross-block modes have nonzero eigenvalue differences",
    "finite_role": "finite cases audit formulas and edge conventions but do not prove the global theorem",
}
NONCLAIMS = [
    "No target arithmetic local datum, Euler factor, root number, automorphy, divisor law, functional equation, or zero match is asserted.",
    "Plucker weights are finite-dimensional source exponents, not prime norms or target spectral zeros.",
    "The symmetric generator A is not asserted to be a Hilbert--Polya operator.",
    "No literary priority is claimed for Oja, Brockett, Grassmann power-flow, Schubert, or Morse--Bott mechanisms.",
]
COLLISION_BOUNDARY = {
    "C185": "C185 evolves a full symmetric matrix on a fixed isospectral orbit toward a separate diagonal target; C298 fixes A and evolves a rank-k projection/subspace under the induced linear action.",
    "subset_sum_warning": "simple eigenvalues need not have distinct k-fold subset sums; uniqueness uses the representable-matroid greedy basis on actual support.",
}
SIMPLE_DEFINITIONS = [
    ("S1-rank-one-sparse", [-3, -1, 2, 5], [[1], [2], [0], [3]]),
    ("S2-subset-sum-tie", [0, 1, 3, 4], [[1, 0], [1, 1], [1, 2], [1, 3]]),
    ("S3-generic-two-plane", [-4, -1, 0, 3, 7], [[1, -2], [1, -1], [1, 0], [1, 1], [1, 3]]),
    ("S4-generic-three-plane-ties", [-3, -2, 0, 2, 3], [[1, 0, 0], [1, 1, 1], [1, 2, 4], [1, 3, 9], [1, 4, 16]]),
    ("S5-proper-schubert-cell", [0, 2, 5, 9, 14], [[1, 0], [1, 1], [1, 2], [1, 4], [0, 0]]),
    ("S6-generic-six-by-three", [-5, -2, 0, 1, 4, 8], [[1, -2, 4], [1, -1, 1], [1, 0, 0], [1, 1, 1], [1, 2, 4], [1, 4, 16]]),
    ("S7-sparse-six-by-two", [-4, -1, 2, 6, 7, 11], [[1, 0], [0, 1], [1, 1], [2, 1], [0, 0], [1, 3]]),
    ("S8-generic-six-by-four", [-7, -3, -1, 2, 5, 9], [[1, 0, 0, 0], [1, 1, 1, 1], [1, 2, 4, 8], [1, 3, 9, 27], [1, 4, 16, 64], [1, 5, 25, 125]]),
]
REPEATED_DEFINITIONS = [
    ("R1-mixed-two-block", [0, 0, 2, 2], [[1, 0], [0, 1], [1, 2], [0, 0]]),
    ("R2-top-eigenspace", [0, 0, 2, 2], [[1, 0], [0, 1], [1, 1], [1, 2]]),
    ("R3-two-block-multiplicity", [-2, -2, 1, 1, 1], [[1, 0], [0, 1], [1, 1], [2, 2], [0, 0]]),
    ("R4-three-block-associated-grade", [-3, 0, 0, 4, 4], [[1, 0, 0], [0, 1, 0], [0, 2, 1], [0, 0, 1], [0, 0, 1]]),
    ("R5-three-block-six-dimensional", [0, 0, 0, 5, 5, 9], [[1, 0, 0], [1, 0, 1], [0, 1, 0], [0, 1, 0], [0, 1, 1], [0, 0, 1]]),
    ("R6-middle-plus-top", [-1, -1, 3, 3, 3, 8], [[0, 0], [0, 0], [1, 0], [1, 0], [0, 1], [1, 2]]),
]
MORSE_DEFINITIONS = [
    ("M1", [-1, 2], [2, 2], 2),
    ("M2", [-2, 0, 5], [1, 3, 2], 3),
    ("M3", [0, 4, 9], [3, 2, 1], 2),
    ("M4", [-3, 1, 6], [2, 3, 2], 3),
]


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


UniqueYAMLLoader.yaml_implicit_resolvers = {
    key: [(tag, pattern) for tag, pattern in resolvers if tag != "tag:yaml.org,2002:timestamp"]
    for key, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def construct_unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge keys are forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str:
            raise TypeError("YAML keys must be strings")
        if key in result:
            raise ValueError(f"duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueYAMLLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_unique_mapping)


def load_yaml(path: Path) -> dict:
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML anchors and aliases are forbidden")
    value = yaml.load(raw, Loader=UniqueYAMLLoader)
    if type(value) is not dict:
        raise TypeError("YAML top level")
    return value


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def exact_tree_equal(actual, expected) -> bool:
    """Compare semantic trees without Python's bool/int equality loophole."""
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


def permutation_sign(values) -> int:
    inversions = sum(values[i] > values[j] for i in range(len(values)) for j in range(i + 1, len(values)))
    return -1 if inversions % 2 else 1


def determinant(matrix) -> int:
    n = len(matrix)
    return sum(
        permutation_sign(perm) * __import__("math").prod(matrix[i][perm[i]] for i in range(n))
        for perm in itertools.permutations(range(n))
    )


def rank(matrix) -> int:
    if not matrix:
        return 0
    work = [[Fraction(x) for x in row] for row in matrix]
    rows, cols = len(work), len(work[0])
    pivot = 0
    for col in range(cols):
        selected = next((r for r in range(pivot, rows) if work[r][col]), None)
        if selected is None:
            continue
        work[pivot], work[selected] = work[selected], work[pivot]
        scale = work[pivot][col]
        work[pivot] = [x / scale for x in work[pivot]]
        for r in range(pivot + 1, rows):
            if work[r][col]:
                scale = work[r][col]
                work[r] = [x - scale * y for x, y in zip(work[r], work[pivot])]
        pivot += 1
        if pivot == rows:
            break
    return pivot


def matmul(left, right):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*right)] for row in left]


def parse_projection(record, frame, eigenvalues, check) -> None:
    required = {"initial_projection", "trace_A_P0", "commutator_frobenius_square", "strict_lyapunov_at_t0"}
    check(type(record) is dict and set(record) == required, "initial data keys")
    check(
        type(record["initial_projection"]) is list
        and all(type(row) is list and all(type(item) is str for item in row) for row in record["initial_projection"]),
        "projection entries are exact rational strings",
    )
    check(type(record["trace_A_P0"]) is str, "Lyapunov value is an exact rational string")
    check(type(record["commutator_frobenius_square"]) is str, "Lyapunov derivative is an exact rational string")
    check(type(record["strict_lyapunov_at_t0"]) is bool, "Lyapunov strictness is an exact Boolean")
    p = [[Fraction(x) for x in row] for row in record["initial_projection"]]
    n, k = len(frame), len(frame[0])
    check(len(p) == n and all(len(row) == n for row in p), "projection shape")
    for i in range(n):
        for j in range(n):
            check(p[i][j] == p[j][i], f"projection symmetric {i}:{j}")
    check(matmul(p, p) == p, "projection idempotent")
    check(sum(p[i][i] for i in range(n)) == k, "projection trace rank")
    check(matmul(p, [[Fraction(x) for x in row] for row in frame]) == [[Fraction(x) for x in row] for row in frame], "projection range")
    value = sum(Fraction(eigenvalues[i]) * p[i][i] for i in range(n))
    comm = [[p[i][j] * (eigenvalues[j] - eigenvalues[i]) for j in range(n)] for i in range(n)]
    derivative = sum(x * x for row in comm for x in row)
    check(Fraction(record["trace_A_P0"]) == value, "initial Lyapunov value")
    check(Fraction(record["commutator_frobenius_square"]) == derivative, "initial Lyapunov derivative")
    check(record["strict_lyapunov_at_t0"] is (derivative > 0), "initial Lyapunov strictness")


def expected_support(eigenvalues, frame):
    k = len(frame[0])
    rows = []
    for subset in itertools.combinations(range(len(frame)), k):
        minor = determinant([[frame[i][j] for j in range(k)] for i in subset])
        if minor:
            rows.append({"subset": [i + 1 for i in subset], "minor": minor, "weight": sum(eigenvalues[i] for i in subset)})
    return rows


def expected_ties(eigenvalues, k):
    groups = {}
    for subset in itertools.combinations(range(len(eigenvalues)), k):
        weight = sum(eigenvalues[i] for i in subset)
        groups.setdefault(weight, []).append([i + 1 for i in subset])
    return [{"weight": w, "subsets": s} for w, s in sorted(groups.items()) if len(s) > 1]


def check_basis_exchange(support, check, label):
    bases = {tuple(row["subset"]) for row in support}
    for left in bases:
        for right in bases:
            for element in set(left) - set(right):
                exchanged = any(
                    tuple(sorted((set(left) - {element}) | {replacement})) in bases
                    for replacement in set(right) - set(left)
                )
                check(exchanged, f"basis exchange {label}:{left}:{right}:{element}")


def block_data(eigenvalues):
    values, multiplicities, cumulative = [], [], []
    for value, group in itertools.groupby(eigenvalues):
        values.append(value)
        multiplicities.append(len(list(group)))
        cumulative.append(sum(multiplicities))
    return values, multiplicities, cumulative


def filtration_dims(frame, cumulative):
    n, k = len(frame), len(frame[0])
    output = []
    for cutoff in cumulative:
        augmented = [frame[i][:] + [int(i == j) for j in range(cutoff)] for i in range(n)]
        output.append(k + cutoff - rank(augmented))
    return output


def occupancy_vectors(multiplicities, k):
    for occupancy in itertools.product(*[range(m + 1) for m in multiplicities]):
        if sum(occupancy) == k:
            yield list(occupancy)


def check_all(data: dict, route_yaml: dict) -> int:
    assertions = 0

    def check(condition, label):
        nonlocal assertions
        assertions += 1
        if not condition:
            raise AssertionError(label)

    check(type(data) is dict and set(data) == EVIDENCE_KEYS, "evidence keys")
    check(data["payload_sha256"] == payload_hash(data), "payload hash")
    check(data["schema"] == "hcs-c298-grassmann-projection-flow-v1", "schema")
    check(data["candidate_id"] == "HCS-C298", "candidate")
    check(data["obstruction_id"] == "HEN-O282", "obstruction")
    check(data["evaluation_date"] == "2026-09-02", "date")
    check(type(data["fixed_epoch"]) is int and data["fixed_epoch"] == 1788307200, "epoch")
    check(data["source_commit"] == SOURCE and data["scope_literal"] == SCOPE, "source scope")
    check(exact_tree_equal(data["evaluator"], {"version": "0.2.0", "sha256": EVALUATOR}), "evaluator and exact types")
    check(exact_tree_equal(data["model"], MODEL), "model and exact types")
    check(exact_tree_equal(data["theorem_contract"], THEOREM), "theorem contract and exact types")
    check(exact_tree_equal(data["proof_contract"], PROOF), "proof contract and exact types")
    check(type(data["enumeration"]) is dict and set(data["enumeration"]) == ENUM_KEYS, "enumeration keys")
    check(exact_tree_equal(data["route_a"], {"tuple": TUPLE, "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}), "route tuple and exact types")
    check(exact_tree_equal(data["scope_flags"], FLAGS), "scope flags and exact Boolean types")
    check(exact_tree_equal(data["nonclaims"], NONCLAIMS), "canonical nonclaims and exact types")
    check(exact_tree_equal(data["collision_boundary"], COLLISION_BOUNDARY), "canonical collision boundary and exact types")
    check("full symmetric matrix" in data["collision_boundary"]["C185"] and "rank-k projection" in data["collision_boundary"]["C185"], "C185 distinction")
    check(exact_tree_equal(data["references"], [
        {"identifier": "10.1007/BF00275687", "role": "Oja principal-component-flow lineage"},
        {"identifier": "10.1016/0024-3795(91)90021-N", "role": "Brockett double-bracket lineage"},
        {"identifier": "hdl:2078.5/90452", "role": "direct continuous-time Grassmann subspace-flow owner"},
    ]), "references and exact types")

    enumeration = data["enumeration"]
    check(exact_tree_equal(enumeration["simple_case_count"], len(SIMPLE_DEFINITIONS)) and len(SIMPLE_DEFINITIONS) == 8, "simple case count and exact type")
    check(len(enumeration["simple_cases"]) == 8, "simple rows")
    simple_support_cells = linear_mode_cells = 0
    for row, definition in zip(enumeration["simple_cases"], SIMPLE_DEFINITIONS):
        case_id, eigenvalues, frame = definition
        required = {
            "case_id", "n", "k", "eigenvalues_strictly_increasing", "integer_frame",
            "plucker_support", "support_size", "ambient_subset_weight_ties",
            "support_tied_nonleading_weight_groups", "greedy_leading_subset", "leading_weight",
            "second_nonzero_weight", "exact_rate_gap", "linear_modes", "stable_dimension",
            "unstable_dimension", "grassmann_dimension", "rational_initial_data",
        }
        check(set(row) == required, f"simple keys {case_id}")
        check(
            exact_tree_equal(row["case_id"], case_id)
            and exact_tree_equal(row["eigenvalues_strictly_increasing"], eigenvalues)
            and exact_tree_equal(row["integer_frame"], frame),
            f"simple definition and exact types {case_id}",
        )
        n, k = len(frame), len(frame[0])
        check(exact_tree_equal(row["n"], n) and exact_tree_equal(row["k"], k) and all(eigenvalues[i] < eigenvalues[i + 1] for i in range(n - 1)), f"simple dimensions and exact types {case_id}")
        check(rank(frame) == k, f"frame rank {case_id}")
        support = expected_support(eigenvalues, frame)
        check(exact_tree_equal(row["plucker_support"], support), f"support and exact types {case_id}")
        check(exact_tree_equal(row["support_size"], len(support)), f"support size and exact type {case_id}")
        for item in support:
            check(set(item) == {"subset", "minor", "weight"}, f"support item keys {case_id}")
            check(item["minor"] != 0 and len(item["subset"]) == k, f"support nonzero {case_id}")
        check_basis_exchange(support, check, case_id)
        check(exact_tree_equal(row["ambient_subset_weight_ties"], expected_ties(eigenvalues, k)), f"ambient ties and exact types {case_id}")
        weights = {}
        for item in support:
            weights.setdefault(item["weight"], 0)
            weights[item["weight"]] += 1
        maximum = max(weights)
        check(weights[maximum] == 1, f"unique greedy maximum {case_id}")
        leader = next(item for item in support if item["weight"] == maximum)
        check(tuple(leader["subset"]) == max(tuple(item["subset"]) for item in support), f"lexicographic greedy {case_id}")
        ordered_weights = sorted((item["weight"] for item in support), reverse=True)
        second = ordered_weights[1]
        check(exact_tree_equal(row["greedy_leading_subset"], leader["subset"]), f"leader and exact types {case_id}")
        check(exact_tree_equal(row["leading_weight"], maximum) and exact_tree_equal(row["second_nonzero_weight"], second), f"leading weights and exact types {case_id}")
        check(exact_tree_equal(row["exact_rate_gap"], maximum - second) and maximum - second > 0, f"rate gap and exact type {case_id}")
        tied_nonleading = [{"weight": w, "multiplicity": m} for w, m in sorted(weights.items()) if m > 1 and w < maximum]
        check(exact_tree_equal(row["support_tied_nonleading_weight_groups"], tied_nonleading), f"support ties and exact types {case_id}")
        selected = {i - 1 for i in leader["subset"]}
        modes = []
        stable = unstable = 0
        for i in sorted(selected):
            for j in range(n):
                if j in selected:
                    continue
                rate = eigenvalues[j] - eigenvalues[i]
                stable += rate < 0
                unstable += rate > 0
                modes.append({"selected_i": i + 1, "unselected_j": j + 1, "rate_lambda_j_minus_lambda_i": rate, "type": "stable" if rate < 0 else "unstable"})
        check(exact_tree_equal(row["linear_modes"], modes), f"modes and exact types {case_id}")
        check(exact_tree_equal(row["stable_dimension"], stable) and stable == sum(index - position for position, index in enumerate(leader["subset"], 1)), f"stable and exact type {case_id}")
        check(exact_tree_equal(row["unstable_dimension"], unstable) and stable + unstable == k * (n - k), f"unstable and exact type {case_id}")
        check(exact_tree_equal(row["grassmann_dimension"], k * (n - k)), f"Grassmann dimension and exact type {case_id}")
        parse_projection(row["rational_initial_data"], frame, eigenvalues, check)
        simple_support_cells += len(support)
        linear_mode_cells += len(modes)

    check(exact_tree_equal(enumeration["repeated_case_count"], len(REPEATED_DEFINITIONS)) and len(REPEATED_DEFINITIONS) == 6, "repeated case count and exact type")
    check(len(enumeration["repeated_cases"]) == 6, "repeated rows")
    repeated_support_cells = 0
    multi_top_cases = 0
    for row, definition in zip(enumeration["repeated_cases"], REPEATED_DEFINITIONS):
        case_id, eigenvalues, frame = definition
        required = {
            "case_id", "n", "k", "eigenvalues_nondecreasing", "eigenvalue_blocks",
            "integer_frame", "filtration_intersection_dimensions", "associated_graded_occupancies",
            "top_plucker_weight", "top_weight_plucker_coordinates", "top_weight_coordinate_count",
            "next_distinct_nonzero_weight", "plucker_weight_gap", "plucker_support", "support_size",
            "rational_initial_data",
        }
        check(set(row) == required, f"repeated keys {case_id}")
        n, k = len(frame), len(frame[0])
        check(exact_tree_equal(row["case_id"], case_id) and exact_tree_equal(row["n"], n) and exact_tree_equal(row["k"], k), f"repeated identity and exact types {case_id}")
        check(exact_tree_equal(row["eigenvalues_nondecreasing"], eigenvalues) and exact_tree_equal(row["integer_frame"], frame), f"repeated definition and exact types {case_id}")
        check(all(eigenvalues[i] <= eigenvalues[i + 1] for i in range(n - 1)) and len(set(eigenvalues)) < n, f"repeated ordering {case_id}")
        check(rank(frame) == k, f"repeated frame rank {case_id}")
        values, multiplicities, cumulative = block_data(eigenvalues)
        blocks = [{"value": v, "multiplicity": m, "cumulative_dimension": c} for v, m, c in zip(values, multiplicities, cumulative)]
        check(exact_tree_equal(row["eigenvalue_blocks"], blocks), f"blocks and exact types {case_id}")
        dims = filtration_dims(frame, cumulative)
        occupancy = [dims[0]] + [dims[i] - dims[i - 1] for i in range(1, len(dims))]
        check(exact_tree_equal(row["filtration_intersection_dimensions"], dims), f"filtration and exact types {case_id}")
        check(exact_tree_equal(row["associated_graded_occupancies"], occupancy), f"occupancy and exact types {case_id}")
        check(sum(occupancy) == k and all(0 <= x <= m for x, m in zip(occupancy, multiplicities)), f"occupancy capacity {case_id}")
        support = expected_support(eigenvalues, frame)
        check(exact_tree_equal(row["plucker_support"], support) and exact_tree_equal(row["support_size"], len(support)), f"repeated support and exact types {case_id}")
        check_basis_exchange(support, check, case_id)
        top_weight = max(item["weight"] for item in support)
        top = [item for item in support if item["weight"] == top_weight]
        lower = sorted({item["weight"] for item in support if item["weight"] < top_weight}, reverse=True)
        check(exact_tree_equal(row["top_plucker_weight"], top_weight) and top_weight == sum(v * x for v, x in zip(values, occupancy)), f"top weight and exact type {case_id}")
        check(exact_tree_equal(row["top_weight_plucker_coordinates"], top) and exact_tree_equal(row["top_weight_coordinate_count"], len(top)), f"top component and exact types {case_id}")
        check(exact_tree_equal(row["next_distinct_nonzero_weight"], lower[0] if lower else None), f"next weight and exact type {case_id}")
        check(exact_tree_equal(row["plucker_weight_gap"], top_weight - lower[0] if lower else None), f"repeated gap and exact type {case_id}")
        parse_projection(row["rational_initial_data"], frame, eigenvalues, check)
        multi_top_cases += len(top) > 1
        repeated_support_cells += len(support)
    check(multi_top_cases >= 5, "multiple tied top components exercised")

    check(len(enumeration["morse_bott_atlases"]) == len(MORSE_DEFINITIONS) == 4, "Morse atlas count")
    morse_rows = 0
    for atlas, definition in zip(enumeration["morse_bott_atlases"], MORSE_DEFINITIONS):
        config_id, values, multiplicities, k = definition
        required = {"config_id", "eigenvalue_values", "multiplicities", "n", "k", "grassmann_dimension", "component_count", "components"}
        check(set(atlas) == required, f"Morse keys {config_id}")
        n = sum(multiplicities)
        check(exact_tree_equal(atlas["config_id"], config_id) and exact_tree_equal(atlas["eigenvalue_values"], values) and exact_tree_equal(atlas["multiplicities"], multiplicities), f"Morse definition and exact types {config_id}")
        check(exact_tree_equal(atlas["n"], n) and exact_tree_equal(atlas["k"], k) and exact_tree_equal(atlas["grassmann_dimension"], k * (n - k)), f"Morse dimensions and exact types {config_id}")
        expected_rows = []
        for occupancy in occupancy_vectors(multiplicities, k):
            tangent = sum(x * (m - x) for x, m in zip(occupancy, multiplicities))
            stable = sum(occupancy[a] * (multiplicities[b] - occupancy[b]) for a in range(len(values)) for b in range(a))
            unstable = sum(occupancy[a] * (multiplicities[b] - occupancy[b]) for a in range(len(values)) for b in range(a + 1, len(values)))
            check(tangent + stable + unstable == k * (n - k), f"Morse closure {config_id}:{occupancy}")
            expected_rows.append({
                "occupancy": occupancy,
                "critical_value_trace_A_P": sum(x * value for x, value in zip(occupancy, values)),
                "critical_manifold_dimension": tangent,
                "stable_normal_dimension": stable,
                "unstable_normal_dimension": unstable,
                "dimension_closure": tangent + stable + unstable,
            })
        check(exact_tree_equal(atlas["components"], expected_rows) and exact_tree_equal(atlas["component_count"], len(expected_rows)), f"Morse rows and exact types {config_id}")
        morse_rows += len(expected_rows)

    check(exact_tree_equal(enumeration["simple_plucker_support_cells"], simple_support_cells) and simple_support_cells == 80, "simple support cells and exact type")
    check(exact_tree_equal(enumeration["repeated_plucker_support_cells"], repeated_support_cells) and repeated_support_cells == 37, "repeated support cells and exact type")
    check(exact_tree_equal(enumeration["linear_mode_cells"], linear_mode_cells) and linear_mode_cells == 50, "mode cells and exact type")
    check(exact_tree_equal(enumeration["morse_bott_component_rows"], morse_rows) and morse_rows == 22, "Morse rows and exact type")
    check(exact_tree_equal(enumeration["audited_cell_count"], simple_support_cells + repeated_support_cells + linear_mode_cells + morse_rows) and simple_support_cells + repeated_support_cells + linear_mode_cells + morse_rows == 189, "audited cells and exact type")

    check(type(route_yaml) is dict and set(route_yaml) == YAML_KEYS, "YAML keys")
    check(exact_tree_equal(route_yaml, EXPECTED_EVALUATION), "YAML complete exact semantic tree and types")
    check(route_yaml["schema"] == "route-a-evaluation-v0.2.0", "YAML schema")
    check(route_yaml["candidate_id"] == "HCS-C298" and route_yaml["obstruction_id"] == "HEN-O282", "YAML identity")
    check(route_yaml["evaluation_date"] == "2026-09-02", "YAML date")
    check(route_yaml["source_commit"] == SOURCE and type(route_yaml["fixed_epoch"]) is int and route_yaml["fixed_epoch"] == 1788307200, "YAML source epoch")
    check(route_yaml["scope_literal"] == SCOPE and route_yaml["evaluator_authority_sha256"] == EVALUATOR, "YAML scope authority")
    check(route_yaml["tuple"] == TUPLE and route_yaml["overall_verdict"] == "ROUTE_A_REJECTED", "YAML tuple")
    check(route_yaml["route_b_invocation_allowed"] is False, "YAML Route B")
    check(route_yaml["scope_flags"] == FLAGS, "YAML flags")
    check(route_yaml["theorem_status"] == "PROVABLE_AS_STATED", "YAML theorem status")
    check(route_yaml["source_owner_tokens"] == ["10.1007/BF00275687", "10.1016/0024-3795(91)90021-N", "hdl:2078.5/90452"], "YAML sources")
    for axis, verdict in zip(("a0", "a1", "a2", "a3", "a4"), TUPLE):
        check(type(route_yaml[axis]) is dict and set(route_yaml[axis]) == {"verdict", "evidence_status", "strongest_evidence", "strongest_failure", "artifacts"}, f"YAML {axis} keys")
        check(route_yaml[axis]["verdict"] == verdict, f"YAML {axis} verdict")

    checker_tree = ast.parse((ROOT / "code/c298_grassmann_checker.py").read_text())
    imports = []
    for node in ast.walk(checker_tree):
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module or "")
    check(not any("producer" in name for name in imports), "checker independence")

    for relative, tokens in {
        "THEOREM_PACKAGE.md": ["PROVABLE AS STATED", "strong basis exchange", "associated-graded subspace", "HEN-O282", "actual second nonzero Plücker weight"],
        "SOURCE_AUDIT.md": ["10.1007/BF00275687", "10.1016/0024-3795(91)90021-N", "hdl:2078.5/90452", "C185 is not being relabeled"],
        "paper/main.tex": ["Global exact projector", "Matroid guard", "Morse--Bott", "AI-use statement"],
    }.items():
        joined = " ".join((ROOT / relative).read_text().split())
        for token in tokens:
            check(token in joined, f"document token {relative}:{token}")
    return assertions


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=ROOT / "results/c298_grassmann_evidence.json")
    parser.add_argument("--yaml", type=Path, default=ROOT / "evaluations/route_a/HCS-C298/2026-09-02.yaml")
    args = parser.parse_args()
    data = json.loads(args.evidence.read_text(), object_pairs_hook=reject_duplicates, parse_constant=reject_nonfinite)
    route_yaml = load_yaml(args.yaml)
    count = check_all(data, route_yaml)
    print(f"C298 independent Grassmann checker: PASS ({count} assertions; producer import forbidden; subset-sum ties retained)")


if __name__ == "__main__":
    main()
