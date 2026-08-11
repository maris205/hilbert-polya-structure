#!/usr/bin/env python3
"""Produce the exact HCS-C30 chronology and trace-obstruction certificate.

Three actions are kept separate throughout:

* the covariant raw-homology zigzag ``v <- B(t)v``;
* the genuine forward length action ``lambda <- B(t)^(-T)lambda``;
* the transfer inverse-branch action, which reverses the raw path and applies
  ``x <- B(t)^T x``.

Every cyclic phase of the C25 and C26 identity words is checked with exact
integer/rational arithmetic.  Infeasibility records contain canonical Farkas
certificates; no numerical LP solver is used.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Callable, Iterable


PROJECT = Path(__file__).resolve().parents[1]
HENON_ROOT = PROJECT.parent
REPO_ROOT = HENON_ROOT.parent
DEFAULT_OUTPUT = PROJECT / "results" / "c30_certificate.json"

SOURCE_PATHS = {
    "C25_certificate": HENON_ROOT
    / "agy_metaplectic_transfer_obstruction"
    / "results"
    / "c25_certificate.json",
    "C25_theorem": HENON_ROOT
    / "agy_metaplectic_transfer_obstruction"
    / "THEOREM_PACKAGE.md",
    "C26_certificate": HENON_ROOT
    / "agy_holomorphic_slice_obstruction"
    / "results"
    / "c26_certificate.json",
    "C26_theorem": HENON_ROOT
    / "agy_holomorphic_slice_obstruction"
    / "THEOREM_PACKAGE.md",
    "C29_certificate": HENON_ROOT
    / "rauzy_groupoid_identity_determinant"
    / "results"
    / "c29_certificate.json",
    "C29_theorem": HENON_ROOT
    / "rauzy_groupoid_identity_determinant"
    / "THEOREM_PACKAGE.md",
}

EXPECTED_SOURCE_HASHES = {
    "C25_certificate": "a35cee22714abbb9dc9aadcc165720d1ff77aff3b7f29071f53a1b451760bd12",
    "C25_theorem": "e1835d63bef914b355ceb4f64acc9043d11a842e9f4e59c7573c63ff66d03702",
    "C26_certificate": "1c0289b9b47e65e0603ea001be7cce263aea13d58c66e4609eac88edf8f7ce4a",
    "C26_theorem": "4e882cbc332711b4cd2f98e9530f89268c8fcf1712eb150aacfee968dcf50495",
    "C29_certificate": "412840c37d2e474462b39ce7072614323023ac8e3f968bc16a9219cc3a0c0cca",
    "C29_theorem": "9b53a2d2971f9b3ac7e43193860345d83bfd2343cbcf4fe94acdd47aed3824cc",
}

Matrix = list[list[int]]
Vector = list[int]
PrefixAction = Callable[[Iterable[str], dict[str, Matrix]], list[Matrix]]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_sha256(value: object) -> str:
    data = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def eye(n: int = 4) -> Matrix:
    return [[int(i == j) for j in range(n)] for i in range(n)]


def transpose(a: Matrix) -> Matrix:
    return [list(row) for row in zip(*a)]


def matmul(a: Matrix, b: Matrix) -> Matrix:
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def matvec(a: Matrix, vector: Vector) -> Vector:
    return [sum(a[i][j] * vector[j] for j in range(len(vector))) for i in range(len(a))]


def inverse_unimodular(a: Matrix) -> Matrix:
    n = len(a)
    augmented = [
        [Fraction(value) for value in a[i]]
        + [Fraction(int(i == j)) for j in range(n)]
        for i in range(n)
    ]
    for column in range(n):
        pivot = next(
            (row for row in range(column, n) if augmented[row][column]), None
        )
        if pivot is None:
            raise AssertionError("singular source matrix")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        pivot_value = augmented[column][column]
        augmented[column] = [value / pivot_value for value in augmented[column]]
        for row in range(n):
            if row == column:
                continue
            factor = augmented[row][column]
            if factor:
                augmented[row] = [
                    augmented[row][j] - factor * augmented[column][j]
                    for j in range(2 * n)
                ]
    right = [row[n:] for row in augmented]
    if any(value.denominator != 1 for row in right for value in row):
        raise AssertionError("source matrix is not unimodular")
    return [[int(value) for value in row] for row in right]


def symbol_base(token: str) -> str:
    return token.removesuffix("^-1")


def symbol_matrix(token: str, matrices: dict[str, Matrix]) -> Matrix:
    base = matrices[symbol_base(token)]
    return inverse_unimodular(base) if token.endswith("^-1") else base


def later_on_left_product(word: Iterable[str], matrices: dict[str, Matrix]) -> Matrix:
    product = eye()
    for token in word:
        product = matmul(symbol_matrix(token, matrices), product)
    return product


def written_product(word: Iterable[str], matrices: dict[str, Matrix]) -> Matrix:
    product = eye()
    for token in word:
        product = matmul(product, symbol_matrix(token, matrices))
    return product


def rotations(word: list[str]) -> list[list[str]]:
    return [word[index:] + word[:index] for index in range(len(word))]


def signed_abelianization(word: Iterable[str], generators: Iterable[str]) -> dict[str, int]:
    counts = {generator: 0 for generator in generators}
    for token in word:
        base = symbol_base(token)
        if base not in counts:
            raise AssertionError(f"unknown abelianization generator {base}")
        counts[base] += -1 if token.endswith("^-1") else 1
    return counts


def freely_reduce(word: Iterable[str]) -> list[str]:
    stack: list[str] = []
    for token in word:
        inverse = (
            symbol_base(token) if token.endswith("^-1") else f"{token}^-1"
        )
        if stack and stack[-1] == inverse:
            stack.pop()
        else:
            stack.append(token)
    return stack


def raw_homology_prefixes(
    sequence: Iterable[str], matrices: dict[str, Matrix]
) -> list[Matrix]:
    """Covariant raw-homology action P_k=B(t_k)P_(k-1)."""

    prefixes: list[Matrix] = []
    product = eye()
    for token in sequence:
        product = matmul(symbol_matrix(token, matrices), product)
        prefixes.append(product)
    return prefixes


def forward_length_prefixes(
    sequence: Iterable[str], matrices: dict[str, Matrix]
) -> list[Matrix]:
    """Genuine forward length action P_k=B(t_k)^(-T)P_(k-1)."""

    prefixes: list[Matrix] = []
    product = eye()
    for token in sequence:
        action = transpose(inverse_unimodular(symbol_matrix(token, matrices)))
        product = matmul(action, product)
        prefixes.append(product)
    return prefixes


def transfer_prefixes(
    reversed_path_sequence: Iterable[str], matrices: dict[str, Matrix]
) -> list[Matrix]:
    """Transfer inverse-branch action Q_k=B(t_k)^T Q_(k-1)."""

    prefixes: list[Matrix] = []
    product = eye()
    for token in reversed_path_sequence:
        product = matmul(transpose(symbol_matrix(token, matrices)), product)
        prefixes.append(product)
    return prefixes


def required_rows(prefixes: list[Matrix]) -> list[dict[str, object]]:
    """All strict-positive coordinate forms, sorted by (step, coordinate)."""

    rows: list[dict[str, object]] = []
    for coordinate, row in enumerate(eye()):
        rows.append(
            {
                "kind": "initial",
                "step": 0,
                "coordinate": coordinate,
                "linear_form": row,
            }
        )
    for step, prefix in enumerate(prefixes, start=1):
        for coordinate, row in enumerate(prefix):
            rows.append(
                {
                    "kind": "prefix",
                    "step": step,
                    "coordinate": coordinate,
                    "linear_form": row,
                }
            )
    return rows


def primitive_positive_null_vector(rows: list[Vector]) -> list[int] | None:
    """Return the primitive positive generator when the nullspace is one-dimensional.

    The equations are ``sum_i c_i rows[i] = 0``.  Minimal-support positive
    dependences have one-dimensional nullspace, so scanning supports in
    increasing cardinality is complete for dependences of size at most five.
    """

    q = len(rows)
    system = [
        [Fraction(rows[column][coordinate]) for column in range(q)]
        for coordinate in range(4)
    ]
    pivot_columns: list[int] = []
    pivot_row = 0
    for column in range(q):
        pivot = next(
            (row for row in range(pivot_row, 4) if system[row][column]), None
        )
        if pivot is None:
            continue
        system[pivot_row], system[pivot] = system[pivot], system[pivot_row]
        scale = system[pivot_row][column]
        system[pivot_row] = [value / scale for value in system[pivot_row]]
        for row in range(4):
            if row == pivot_row:
                continue
            scale = system[row][column]
            if scale:
                system[row] = [
                    system[row][j] - scale * system[pivot_row][j]
                    for j in range(q)
                ]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == 4:
            break
    free_columns = [column for column in range(q) if column not in pivot_columns]
    if len(free_columns) != 1:
        return None
    vector = [Fraction(0) for _ in range(q)]
    vector[free_columns[0]] = Fraction(1)
    for row, column in enumerate(pivot_columns):
        vector[column] = -sum(
            system[row][free] * vector[free] for free in free_columns
        )
    if all(value < 0 for value in vector):
        vector = [-value for value in vector]
    if not all(value > 0 for value in vector):
        return None
    denominator_lcm = math.lcm(*(value.denominator for value in vector))
    integers = [int(value * denominator_lcm) for value in vector]
    common = math.gcd(*integers)
    return [value // common for value in integers]


def certificate_from_terms(
    certificate_type: str,
    terms: list[dict[str, object]],
    decisive_row: dict[str, object] | None,
) -> dict[str, object]:
    total = [0, 0, 0, 0]
    for term in terms:
        coefficient = term["coefficient"]
        row = term["linear_form"]
        if type(coefficient) is not int or coefficient <= 0:
            raise AssertionError("Farkas coefficient must be a positive integer")
        if type(row) is not list:
            raise AssertionError("Farkas row must be explicit")
        total = [total[j] + coefficient * row[j] for j in range(4)]
    if total != [0, 0, 0, 0]:
        raise AssertionError(f"invalid Farkas certificate: {total}")
    return {
        "search_policy": "rows sorted by (step,coordinate); first componentwise-nonpositive NEG_ROW, else support size 2..5 then lexicographic row tuple",
        "certificate_type": certificate_type,
        "support_size": len(terms),
        "decisive_row": decisive_row,
        "terms": terms,
        "coefficients_are_primitive_positive_integers": True,
        "weighted_form_sum": total,
        "contradiction": "every listed form must be >0, but their positive weighted sum is identically 0",
        "positive_cone_orbit_exists": False,
    }


def canonical_farkas_certificate(prefixes: list[Matrix]) -> dict[str, object]:
    rows = required_rows(prefixes)

    # Priority one: the first row that is nonpositive on the entire positive cone.
    for record in rows:
        row = record["linear_form"]
        if all(value <= 0 for value in row):
            terms = []
            for coordinate, value in enumerate(row):
                if value < 0:
                    terms.append(
                        {
                            **rows[coordinate],
                            "coefficient": -value,
                        }
                    )
            terms.append({**record, "coefficient": 1})
            terms.sort(key=lambda term: (int(term["step"]), int(term["coordinate"])))
            return certificate_from_terms("NEG_ROW", terms, record)

    # Priority two: the first minimal-support strictly positive dependence.
    for support_size in range(2, 6):
        for indices in itertools.combinations(range(len(rows)), support_size):
            coefficients = primitive_positive_null_vector(
                [rows[index]["linear_form"] for index in indices]
            )
            if coefficients is None:
                continue
            terms = [
                {**rows[index], "coefficient": coefficient}
                for index, coefficient in zip(indices, coefficients)
            ]
            return certificate_from_terms("POSITIVE_DEPENDENCE", terms, None)
    raise AssertionError("no canonical Farkas certificate with support <=5")


def highlighted_rows(
    prefixes: list[Matrix], descriptors: list[tuple[int, int]]
) -> list[dict[str, object]]:
    rows = required_rows(prefixes)
    lookup = {(int(row["step"]), int(row["coordinate"])): row for row in rows}
    return [lookup[descriptor] for descriptor in descriptors]


def phase_census(
    raw_path_word: list[str],
    matrices: dict[str, Matrix],
    action: PrefixAction,
    reverse_before_action: bool,
    phase_zero_descriptors: list[tuple[int, int]],
) -> dict[str, object]:
    records: list[dict[str, object]] = []
    for phase, raw_rotation in enumerate(rotations(raw_path_word)):
        action_sequence = (
            list(reversed(raw_rotation)) if reverse_before_action else raw_rotation
        )
        prefixes = action(action_sequence, matrices)
        if prefixes[-1] != eye():
            raise AssertionError(f"phase {phase} does not close at identity")
        certificate = canonical_farkas_certificate(prefixes)
        records.append(
            {
                "phase": phase,
                "raw_rotation": raw_rotation,
                "action_sequence": action_sequence,
                "final_matrix": prefixes[-1],
                "farkas_infeasibility_certificate": certificate,
                "positive_cone_orbit_exists": False,
            }
        )
    return {
        "raw_path_word": raw_path_word,
        "word_length": len(raw_path_word),
        "phase_count": len(records),
        "infeasible_phase_count": sum(
            not record["positive_cone_orbit_exists"] for record in records
        ),
        "all_cyclic_phases_infeasible": all(
            not record["positive_cone_orbit_exists"] for record in records
        ),
        "phase_zero_highlights": highlighted_rows(
            action(records[0]["action_sequence"], matrices), phase_zero_descriptors
        ),
        "phase_records": records,
    }


def load_sources() -> tuple[dict[str, object], dict[str, object], dict[str, object], dict[str, object]]:
    observed = {name: sha256(path) for name, path in SOURCE_PATHS.items()}
    if observed != EXPECTED_SOURCE_HASHES:
        raise AssertionError(f"source lock changed: {observed}")
    c25 = json.loads(SOURCE_PATHS["C25_certificate"].read_text(encoding="utf-8"))
    c26 = json.loads(SOURCE_PATHS["C26_certificate"].read_text(encoding="utf-8"))
    c29 = json.loads(SOURCE_PATHS["C29_certificate"].read_text(encoding="utf-8"))
    source_lock = {
        "files": {
            name: {
                "path": str(path.relative_to(REPO_ROOT)),
                "sha256": observed[name],
            }
            for name, path in SOURCE_PATHS.items()
        },
        "chronology_id": "RAW_LATER_ON_LEFT__FORWARD_LENGTH_INVERSE_TRANSPOSE__TRANSFER_REVERSED_TRANSPOSE",
        "data_policy": "exact integers and rationals only; no prime tables, zero tables, fitted clocks, or longer-word scans",
    }
    return c25, c26, c29, source_lock


def raw_c25_matrices(c25: dict[str, object]) -> dict[str, Matrix]:
    matrices: dict[str, Matrix] = {}
    for row in c25["graph"]["edges"]:
        token = f"{int(row['source'])}{row['type']}"
        matrices[token] = [
            [int(value) for value in values] for values in row["chronological_matrix"]
        ]
    if len(matrices) != 14:
        raise AssertionError("C25 raw edge count changed")
    return matrices


def c26_matrices(
    c26: dict[str, object], c29: dict[str, object]
) -> tuple[dict[str, Matrix], list[str], list[str]]:
    relation = c29["payload"]["c26_branch_relation"]
    matrices = {
        name: [[int(value) for value in row] for row in relation["matrices"][name]]
        for name in ("A", "B", "C")
    }
    source = c26["source_locked_branch"]
    two = c26["scalar_periodic_trace_gate"]["chronological_two_return_witness"]
    three = c26["scalar_periodic_trace_gate"][
        "three_return_spectral_chronology_witness"
    ]
    source_matrices = {
        "A": source["chronological_matrix_B"],
        "B": two["second_branch_chronological_matrix_B"],
        "C": three["third_branch_chronological_matrix_B"],
    }
    if matrices != source_matrices:
        raise AssertionError("C26 A/B/C matrices no longer match the C26 source")
    holonomy_word = [str(token) for token in relation["holonomy_order_word"]]
    path_word = [str(token) for token in relation["later_on_left_path_order_word"]]
    if path_word != list(reversed(holonomy_word)):
        raise AssertionError("C26 written/path chronology changed")
    if written_product(holonomy_word, matrices) != eye():
        raise AssertionError("C26 holonomy-order product changed")
    if later_on_left_product(path_word, matrices) != eye():
        raise AssertionError("C26 later-on-left path product changed")
    return matrices, path_word, holonomy_word


def positive_raw_control(
    raw_path_word: list[str], matrices: dict[str, Matrix], witness: Vector
) -> dict[str, object]:
    prefixes = raw_homology_prefixes(raw_path_word, matrices)
    trajectory = [witness] + [matvec(prefix, witness) for prefix in prefixes]
    if trajectory[-1] != witness or not all(
        value > 0 for state in trajectory for value in state
    ):
        raise AssertionError("raw-homology control witness changed")
    records = []
    for phase, raw_rotation in enumerate(rotations(raw_path_word)):
        initial = trajectory[phase]
        phase_prefixes = raw_homology_prefixes(raw_rotation, matrices)
        phase_trajectory = [initial] + [
            matvec(prefix, initial) for prefix in phase_prefixes
        ]
        if phase_trajectory[-1] != initial or not all(
            value > 0 for state in phase_trajectory for value in state
        ):
            raise AssertionError("cyclic raw-homology control witness failed")
        records.append(
            {
                "phase": phase,
                "raw_rotation": raw_rotation,
                "initial_positive_integer_witness": initial,
                "trajectory": phase_trajectory,
                "periodic_closure": True,
                "all_coordinates_strictly_positive": True,
            }
        )
    return {
        "raw_path_word": raw_path_word,
        "phase_zero_positive_integer_witness": witness,
        "phase_count": len(records),
        "feasible_phase_count": len(records),
        "all_cyclic_phases_feasible": True,
        "phase_records": records,
    }


def exact_chronology_gates(
    c25: dict[str, object], c26: dict[str, object], c29: dict[str, object]
) -> tuple[dict[str, object], dict[str, object], dict[str, object]]:
    c25_matrices = raw_c25_matrices(c25)
    locked_c25 = c29["payload"]["c25_identity_witnesses"]
    c1 = [str(token) for token in locked_c25["C1"]["tokens_path_order"]]
    c2 = [str(token) for token in locked_c25["C2"]["tokens_path_order"]]
    matrices26, c26_path, c26_holonomy = c26_matrices(c26, c29)
    if later_on_left_product(c1, c25_matrices) != eye():
        raise AssertionError("C25 C1 raw identity changed")
    if later_on_left_product(c2, c25_matrices) != eye():
        raise AssertionError("C25 C2 raw identity changed")

    raw_control = {
        "action": "v_k=B(t_k)*v_(k-1), with later tokens multiplying on the left",
        "classification": "covariant raw-homology zigzag; this is not the AGY forward length action",
        "C25_positive_controls": {
            "C1": positive_raw_control(c1, c25_matrices, [1, 2, 1, 1]),
            "C2": positive_raw_control(c2, c25_matrices, [1, 1, 3, 1]),
        },
        "C26_infeasibility": phase_census(
            c26_path,
            matrices26,
            raw_homology_prefixes,
            False,
            [(0, 0), (7, 3)],
        ),
    }

    forward = {
        "action": "lambda_k=B(t_k)^(-T)*lambda_(k-1) in raw path order",
        "phase_policy": "all left cyclic rotations of each raw later-on-left path word",
        "words": {
            "C25_C1": phase_census(
                c1,
                c25_matrices,
                forward_length_prefixes,
                False,
                [(1, 3), (4, 1)],
            ),
            "C25_C2": phase_census(
                c2,
                c25_matrices,
                forward_length_prefixes,
                False,
                [(0, 0), (3, 2)],
            ),
            "C26_W24": phase_census(
                c26_path,
                matrices26,
                forward_length_prefixes,
                False,
                [(4, 2), (16, 3)],
            ),
        },
    }

    transfer = {
        "action": "for each raw rotation reverse path order, then x_k=B(t_k)^T*x_(k-1)",
        "phase_policy": "reverse each left cyclic rotation of the raw later-on-left path word",
        "C26_phase_zero_equivalent_holonomy_word": c26_holonomy,
        "words": {
            "C25_C1": phase_census(
                c1,
                c25_matrices,
                transfer_prefixes,
                True,
                [(1, 1), (4, 3)],
            ),
            "C25_C2": phase_census(
                c2,
                c25_matrices,
                transfer_prefixes,
                True,
                [(0, 0), (2, 2)],
            ),
            "C26_W24": phase_census(
                c26_path,
                matrices26,
                transfer_prefixes,
                True,
                [(3, 1), (8, 3), (20, 2)],
            ),
        },
    }
    return raw_control, forward, transfer


def identity_and_clock_semantics(c29: dict[str, object]) -> dict[str, object]:
    locked_c25 = c29["payload"]["c25_identity_witnesses"]
    c1 = [str(token) for token in locked_c25["C1"]["tokens_path_order"]]
    c2 = [str(token) for token in locked_c25["C2"]["tokens_path_order"]]
    relation = c29["payload"]["c26_branch_relation"]
    c26_path = [str(token) for token in relation["later_on_left_path_order_word"]]

    c1_counts = signed_abelianization(c1, sorted({symbol_base(t) for t in c1}))
    c2_counts = signed_abelianization(c2, sorted({symbol_base(t) for t in c2}))
    c26_counts = signed_abelianization(c26_path, ("A", "B", "C"))
    c1_nonzero = {name: value for name, value in c1_counts.items() if value}
    c2_nonzero = {name: value for name, value in c2_counts.items() if value}
    if c1_nonzero != {"1b": 1, "3t": 1}:
        raise AssertionError(f"C1 signed abelianization changed: {c1_nonzero}")
    if c2_nonzero != {"4t": 1, "5b": 1}:
        raise AssertionError(f"C2 signed abelianization changed: {c2_nonzero}")
    if c26_counts != {"A": 0, "B": 0, "C": 0}:
        raise AssertionError(f"C26 signed abelianization changed: {c26_counts}")
    reduced_lengths = {
        "C25_C1": len(freely_reduce(c1)),
        "C25_C2": len(freely_reduce(c2)),
        "C26_W24": len(freely_reduce(c26_path)),
    }
    if reduced_lengths != {"C25_C1": 6, "C25_C2": 6, "C26_W24": 24}:
        raise AssertionError(f"formal word reduction changed: {reduced_lengths}")

    return {
        "identity_trichotomy": {
            "matrix_holonomy_identity_for_certified_words": True,
            "projective_map_identity_where_all_prefixes_are_defined": True,
            "matrix_holonomy_identity_is_groupoid_unit": False,
            "formal_freely_reduced_lengths": reduced_lengths,
            "scope": "B_w=I is a representation-kernel relation; it does not erase a nonempty formal path word",
        },
        "signed_abelianization": {
            "C25_C1": {
                "nonzero_generator_counts": c1_nonzero,
                "expression": "1b+3t",
                "vanishes": False,
            },
            "C25_C2": {
                "nonzero_generator_counts": c2_nonzero,
                "expression": "4t+5b",
                "vanishes": False,
            },
            "C26_W24": {
                "generator_counts": c26_counts,
                "expression": "0",
                "vanishes": True,
            },
        },
        "edge_constant_antisymmetric_cocycle": {
            "rule": "a(e^-1)=-a(e)",
            "C25_C1_forced_to_vanish": False,
            "C25_C2_forced_to_vanish": False,
            "C26_W24_forced_to_vanish_by_signed_generator_counts": True,
            "reason": "C1 and C2 have nonzero signed abelianization, so an arbitrary edge-constant antisymmetric cocycle need not vanish on them",
        },
        "projective_normalizer": {
            "increment": "rho_B(x)=log(ell(B*x))-log(ell(x))",
            "conditional_domain": "all chronological prefixes must be defined in one common projective chart",
            "telescoping_law": "sum rho_(B_k)(x_(k-1))=log(ell(B_w*x))-log(ell(x))",
            "identity_holonomy_period": 0,
            "conclusion": "if B_w=I and the domain condition holds, the normalizer period is zero",
        },
        "symmetric_positive_edge_clock": {
            "valid_new_nonbacktracking_graph_suspension": True,
            "is_AGY_time": False,
            "is_natural_extension_time": False,
            "compatible_with_groupoid_unit_cancellation_e_e_inverse": False,
            "unit_conflict": "L(e)+L(e^-1)>0 for positive symmetric L, whereas a cancellable unit path has period 0",
        },
        "repetition_fork": {
            "intrinsic_projective_normalizer": {
                "domain_condition": "conditional on w^m being defined throughout in the same normalized projective chart",
                "period_of_w_power": "0 for every m>=1",
                "flow_log_repetition_term": "1/m",
                "harmonic_repetition_sum_converges": False,
            },
            "combinatorial_unit_edge_clock": {
                "base_periods": {"C25_C1": 6, "C25_C2": 6, "C26_W24": 24},
                "period_of_w_power": {"C25_C1": "6*m", "C25_C2": "6*m", "C26_W24": "24*m"},
                "finite_hashimoto_determinant_germ_valid": True,
                "same_system_as_AGY_or_natural_extension": False,
            },
            "fork_conclusion": "the finite Hashimoto germ survives only after choosing a different combinatorial suspension clock",
        },
    }


def abstract_gates() -> dict[str, object]:
    return {
        "projective_roof_cocycle": {
            "map": "h_M(x)=M*x/ell(M*x)",
            "domain": "normalized projective simplex ell(x)=1",
            "roof": "r_M(x)=log ell(M*x)",
            "composition_law": "r_(M*N)(x)=r_N(x)+r_M(h_N(x))",
            "inverse_law": "r_(M^-1)(h_M(x))=-r_M(x)",
            "inverse_pair_sum": 0,
            "strictly_positive_on_both_M_and_M_inverse": False,
            "positive_symmetric_edge_length_is_same_AGY_time_cocycle": False,
            "classification": "signed groupoid time cocycle versus externally chosen symmetric graph length",
        },
        "same_space_nuclearity": {
            "hypotheses": [
                "one infinite-dimensional Banach/Hilbert fibre H",
                "bounded faithful edge operators C_e and C_bar_e with C_bar_e*C_e=I_H",
                "finite Hashimoto block operator whose legal block compressions expose every C_e",
            ],
            "compact_hashimoto_possible": False,
            "trace_class_hashimoto_possible": False,
            "proof": "compact/trace-class block compression makes C_e compact/trace-class; bounded C_bar_e then makes I_H compact/trace-class",
            "finite_dimensional_exception": "allowed, but it is the already-certified C29 finite graph/finite-Weil model",
        },
        "identity_word_flat_trace": {
            "base_map_for_each_certified_word": "h_W=id on its algebraic projective domain",
            "derivative": "Dh_W=I",
            "fixed_set": "the full domain, not isolated periodic points",
            "fixed_point_denominator": "det(I-Dh_W)=0",
            "standard_isolated_fixed_point_flat_trace_applies": False,
            "ordinary_nuclear_word_trace_applies": False,
            "scope": "rules out the standard holomorphic isolated-fixed-point/nuclear realization; it does not rule out every conceivable clean-fixed-set regularization",
        },
    }


def build_payload() -> dict[str, object]:
    c25, c26, c29, source_lock = load_sources()
    raw_control, forward_gate, transfer_gate = exact_chronology_gates(c25, c26, c29)
    for gate in (forward_gate, transfer_gate):
        if any(
            record["infeasible_phase_count"] != record["phase_count"]
            for record in gate["words"].values()
        ):
            raise AssertionError("an exact phase census unexpectedly reopened")
    payload = {
        "candidate_id": "HCS-C30",
        "candidate_name": "Rauzy inverse roof and flat-trace obstruction",
        "material_passport": {
            "schema": "ARS-compatible research artifact",
            "data_class": "exact source-locked integer matrices and theorem-level deductions",
            "human_subjects": False,
            "AI_assistance_disclosure_required": True,
            "verification_status": "PRODUCER_ONLY_UNTIL_INDEPENDENT_CHECKER",
        },
        "source_lock": source_lock,
        "conventions": {
            "raw_matrix_chronology": "later Rauzy arrows multiply on the left",
            "raw_homology_control": "covariant B(t) zigzags are controls and are not AGY forward length orbits",
            "forward_length_action": "B(t)^(-T) in raw path order",
            "transfer_inverse_branch_action": "reverse each raw path phase, then apply B(t)^T",
            "positive_cone": "all four unnormalised coordinates are strictly positive initially and after every prefix",
            "identity_word_scope": "raw matrix identity, not merely a finite-Weil character coincidence",
        },
        "raw_homology_zigzag_control": raw_control,
        "forward_length_positive_cone_gate": forward_gate,
        "transfer_inverse_branch_positive_cone_gate": transfer_gate,
        "identity_and_clock_semantics": identity_and_clock_semantics(c29),
        **abstract_gates(),
        "decisions": {
            "C29_formal_groupoid_algebraic_result": "RETAINS_VALIDITY",
            "raw_homology_C25_controls": "POSITIVE_BUT_NOT_AGY_LENGTH_DYNAMICS",
            "all_forward_length_cyclic_phases": "FAIL_EXACT_6_6_24",
            "all_transfer_inverse_branch_cyclic_phases": "FAIL_EXACT_6_6_24",
            "C29_identity_holonomy_cycles_as_AGY_positive_orbits": "FAIL_EXACT",
            "identity_holonomy_is_unit_path": False,
            "new_symmetric_hashimoto_suspension": "VALID_BUT_DIFFERENT_SYSTEM",
            "intrinsic_strictly_positive_bioriented_AGY_roof": "IMPOSSIBLE_AS_TIME_COCYCLE",
            "same_space_infinite_dimensional_nuclear_transfer": "FAIL_THEOREM_UNDER_FAITHFUL_INVERSE_HYPOTHESES",
            "standard_identity_word_flat_trace": "FAIL_DEGENERATE_FIXED_SET",
            "finite_graph_trace_log": "VALID_BUT_COMBINATORIAL_AND_ALREADY_C29",
            "route_A_promotion": False,
            "route_B_authorized": False,
            "C29_lane": "CLOSE_AND_PIVOT",
        },
        "pivot": {
            "next_system": "the genuine analytic area-preserving H_6 hyperbolic basic set",
            "inherited_infrastructure": "henon_pinning_trace_obstruction exact BPS one-step mixed domains and pinning kernel",
            "next_operator_form": "quantitative common-space composition and determinant-tail theorem for the existing H_6 pinning infrastructure",
            "reason": "true positive-time H_6 iterates avoid formal direction switching and identity projective words",
            "nonduplication": "do not rebuild the qualitative BPS/Rugh pinning operator or re-claim its known nuclear trace theory",
            "forbidden_next_step": "no longer-word or small-prime scan of the C29 formal inverse groupoid",
        },
        "route_a": {
            "tuple": ["A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED_FOR_DYNAMICAL_PROMOTION",
            "retained_output": "exact negative theorem plus finite combinatorial C29 determinant germ",
        },
        "runtime": {
            "arithmetic": "Python stdlib integers and Fraction only",
            "environment_fields_in_canonical_payload": False,
            "producer_sha256": sha256(Path(__file__).resolve()),
        },
    }
    return payload


def main() -> None:
    args = parse_args()
    payload = build_payload()
    certificate = {
        "schema": "hcs-c30-certificate-v3",
        "payload": payload,
        "payload_sha256": canonical_sha256(payload),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {args.output}")
    print(f"payload_sha256={certificate['payload_sha256']}")


if __name__ == "__main__":
    main()
