#!/usr/bin/env python3
"""Independent, type-strict, fail-closed checker for HCS-C30.

The checker deliberately does not import the producer.  It reloads the locked
C25/C26/C29 artifacts, reconstructs every cyclic phase of all three matrix
actions, independently repeats the canonical exact Farkas search, and compares
the complete contracted payload recursively with type equality.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import sys
from fractions import Fraction
from pathlib import Path
from typing import Callable, Iterable


PROJECT = Path(__file__).resolve().parents[1]
HENON_ROOT = PROJECT.parent
REPO_ROOT = HENON_ROOT.parent
DEFAULT_CERTIFICATE = PROJECT / "results" / "c30_certificate.json"
DEFAULT_OUTPUT = PROJECT / "results" / "c30_independent_check.json"
PRODUCER = PROJECT / "code" / "c30_producer.py"

SOURCES = {
    "C25_certificate": HENON_ROOT / "agy_metaplectic_transfer_obstruction" / "results" / "c25_certificate.json",
    "C25_theorem": HENON_ROOT / "agy_metaplectic_transfer_obstruction" / "THEOREM_PACKAGE.md",
    "C26_certificate": HENON_ROOT / "agy_holomorphic_slice_obstruction" / "results" / "c26_certificate.json",
    "C26_theorem": HENON_ROOT / "agy_holomorphic_slice_obstruction" / "THEOREM_PACKAGE.md",
    "C29_certificate": HENON_ROOT / "rauzy_groupoid_identity_determinant" / "results" / "c29_certificate.json",
    "C29_theorem": HENON_ROOT / "rauzy_groupoid_identity_determinant" / "THEOREM_PACKAGE.md",
}
SOURCE_DIGESTS = {
    "C25_certificate": "a35cee22714abbb9dc9aadcc165720d1ff77aff3b7f29071f53a1b451760bd12",
    "C25_theorem": "e1835d63bef914b355ceb4f64acc9043d11a842e9f4e59c7573c63ff66d03702",
    "C26_certificate": "1c0289b9b47e65e0603ea001be7cce263aea13d58c66e4609eac88edf8f7ce4a",
    "C26_theorem": "4e882cbc332711b4cd2f98e9530f89268c8fcf1712eb150aacfee968dcf50495",
    "C29_certificate": "412840c37d2e474462b39ce7072614323023ac8e3f968bc16a9219cc3a0c0cca",
    "C29_theorem": "9b53a2d2971f9b3ac7e43193860345d83bfd2343cbcf4fe94acdd47aed3824cc",
}

Matrix = list[list[int]]
Vector = list[int]
Action = Callable[[Iterable[str], dict[str, Matrix]], list[Matrix]]


class GateFailure(Exception):
    pass


def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path, default=DEFAULT_CERTIFICATE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_digest(value: object) -> str:
    raw = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False
    ).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def strict_equal(observed: object, expected: object, label: str) -> None:
    if type(observed) is not type(expected):
        raise GateFailure(
            f"{label}: type {type(observed).__name__} != {type(expected).__name__}"
        )
    if isinstance(expected, dict):
        if set(observed) != set(expected):
            raise GateFailure(f"{label}: keyset mismatch")
        for key in sorted(expected):
            strict_equal(observed[key], expected[key], f"{label}.{key}")
        return
    if isinstance(expected, list):
        if len(observed) != len(expected):
            raise GateFailure(f"{label}: list length mismatch")
        for index, (left, right) in enumerate(zip(observed, expected)):
            strict_equal(left, right, f"{label}[{index}]")
        return
    if observed != expected:
        raise GateFailure(f"{label}: value mismatch")


def ident() -> Matrix:
    return [[int(i == j) for j in range(4)] for i in range(4)]


def mul(left: Matrix, right: Matrix) -> Matrix:
    return [
        [sum(left[i][k] * right[k][j] for k in range(4)) for j in range(4)]
        for i in range(4)
    ]


def mv(matrix: Matrix, vector: Vector) -> Vector:
    return [sum(matrix[i][j] * vector[j] for j in range(4)) for i in range(4)]


def trans(matrix: Matrix) -> Matrix:
    return [list(row) for row in zip(*matrix)]


def integral_inverse(matrix: Matrix) -> Matrix:
    rows = [
        [Fraction(matrix[i][j]) for j in range(4)]
        + [Fraction(int(i == j)) for j in range(4)]
        for i in range(4)
    ]
    for column in range(4):
        pivot = next((r for r in range(column, 4) if rows[r][column]), None)
        if pivot is None:
            raise GateFailure("singular raw matrix")
        rows[column], rows[pivot] = rows[pivot], rows[column]
        scale = rows[column][column]
        rows[column] = [entry / scale for entry in rows[column]]
        for r in range(4):
            if r == column:
                continue
            scale = rows[r][column]
            if scale:
                rows[r] = [
                    rows[r][j] - scale * rows[column][j] for j in range(8)
                ]
    inverse = [row[4:] for row in rows]
    if any(entry.denominator != 1 for row in inverse for entry in row):
        raise GateFailure("nonintegral inverse")
    return [[int(entry) for entry in row] for row in inverse]


def token_matrix(token: str, generators: dict[str, Matrix]) -> Matrix:
    inverse = token.endswith("^-1")
    base = token[:-3] if inverse else token
    if base not in generators:
        raise GateFailure(f"unknown token {token}")
    return integral_inverse(generators[base]) if inverse else generators[base]


def chronological(word: Iterable[str], generators: dict[str, Matrix]) -> Matrix:
    answer = ident()
    for token in word:
        answer = mul(token_matrix(token, generators), answer)
    return answer


def textual(word: Iterable[str], generators: dict[str, Matrix]) -> Matrix:
    answer = ident()
    for token in word:
        answer = mul(answer, token_matrix(token, generators))
    return answer


def cyclic_words(word: list[str]) -> list[list[str]]:
    return [word[k:] + word[:k] for k in range(len(word))]


def signed_counts(word: Iterable[str], alphabet: Iterable[str]) -> dict[str, int]:
    answer = {letter: 0 for letter in alphabet}
    for token in word:
        inverse = token.endswith("^-1")
        letter = token[:-3] if inverse else token
        if letter not in answer:
            raise GateFailure(f"unknown signed-count letter {letter}")
        answer[letter] += -1 if inverse else 1
    return answer


def free_reduction(word: Iterable[str]) -> list[str]:
    reduced: list[str] = []
    for token in word:
        inverse = token[:-3] if token.endswith("^-1") else f"{token}^-1"
        if reduced and reduced[-1] == inverse:
            reduced.pop()
        else:
            reduced.append(token)
    return reduced


def raw_prefixes(word: Iterable[str], generators: dict[str, Matrix]) -> list[Matrix]:
    answer = ident()
    out = []
    for token in word:
        answer = mul(token_matrix(token, generators), answer)
        out.append(answer)
    return out


def length_prefixes(word: Iterable[str], generators: dict[str, Matrix]) -> list[Matrix]:
    answer = ident()
    out = []
    for token in word:
        action = trans(integral_inverse(token_matrix(token, generators)))
        answer = mul(action, answer)
        out.append(answer)
    return out


def inverse_branch_prefixes(
    word: Iterable[str], generators: dict[str, Matrix]
) -> list[Matrix]:
    answer = ident()
    out = []
    for token in word:
        answer = mul(trans(token_matrix(token, generators)), answer)
        out.append(answer)
    return out


def form_records(prefixes: list[Matrix]) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for coordinate, row in enumerate(ident()):
        records.append(
            {
                "kind": "initial",
                "step": 0,
                "coordinate": coordinate,
                "linear_form": row,
            }
        )
    for step, prefix in enumerate(prefixes, 1):
        for coordinate, row in enumerate(prefix):
            records.append(
                {
                    "kind": "prefix",
                    "step": step,
                    "coordinate": coordinate,
                    "linear_form": row,
                }
            )
    return records


def one_dimensional_positive_kernel(vectors: list[Vector]) -> list[int] | None:
    width = len(vectors)
    equations = [
        [Fraction(vectors[j][coordinate]) for j in range(width)]
        for coordinate in range(4)
    ]
    pivots: list[int] = []
    next_row = 0
    for column in range(width):
        chosen = next(
            (row for row in range(next_row, 4) if equations[row][column]), None
        )
        if chosen is None:
            continue
        equations[next_row], equations[chosen] = equations[chosen], equations[next_row]
        pivot = equations[next_row][column]
        equations[next_row] = [entry / pivot for entry in equations[next_row]]
        for row in range(4):
            if row == next_row:
                continue
            factor = equations[row][column]
            if factor:
                equations[row] = [
                    equations[row][j] - factor * equations[next_row][j]
                    for j in range(width)
                ]
        pivots.append(column)
        next_row += 1
        if next_row == 4:
            break
    free = [column for column in range(width) if column not in pivots]
    if len(free) != 1:
        return None
    kernel = [Fraction(0) for _ in range(width)]
    kernel[free[0]] = Fraction(1)
    for row, column in enumerate(pivots):
        kernel[column] = -sum(equations[row][j] * kernel[j] for j in free)
    if all(entry < 0 for entry in kernel):
        kernel = [-entry for entry in kernel]
    if not all(entry > 0 for entry in kernel):
        return None
    scale = math.lcm(*(entry.denominator for entry in kernel))
    integers = [int(entry * scale) for entry in kernel]
    divisor = math.gcd(*integers)
    return [entry // divisor for entry in integers]


def relation_record(
    relation_type: str,
    terms: list[dict[str, object]],
    decisive: dict[str, object] | None,
) -> dict[str, object]:
    total = [0, 0, 0, 0]
    for term in terms:
        coefficient = term["coefficient"]
        row = term["linear_form"]
        if type(coefficient) is not int or coefficient <= 0 or type(row) is not list:
            raise GateFailure("malformed exact relation")
        total = [total[j] + coefficient * row[j] for j in range(4)]
    if total != [0, 0, 0, 0]:
        raise GateFailure("nonzero exact relation")
    return {
        "search_policy": "rows sorted by (step,coordinate); first componentwise-nonpositive NEG_ROW, else support size 2..5 then lexicographic row tuple",
        "certificate_type": relation_type,
        "support_size": len(terms),
        "decisive_row": decisive,
        "terms": terms,
        "coefficients_are_primitive_positive_integers": True,
        "weighted_form_sum": total,
        "contradiction": "every listed form must be >0, but their positive weighted sum is identically 0",
        "positive_cone_orbit_exists": False,
    }


def canonical_relation(prefixes: list[Matrix]) -> dict[str, object]:
    records = form_records(prefixes)
    for record in records:
        vector = record["linear_form"]
        if all(value <= 0 for value in vector):
            terms = [
                {**records[coordinate], "coefficient": -value}
                for coordinate, value in enumerate(vector)
                if value < 0
            ]
            terms.append({**record, "coefficient": 1})
            terms.sort(key=lambda term: (int(term["step"]), int(term["coordinate"])))
            return relation_record("NEG_ROW", terms, record)
    for size in range(2, 6):
        for indices in itertools.combinations(range(len(records)), size):
            coefficients = one_dimensional_positive_kernel(
                [records[index]["linear_form"] for index in indices]
            )
            if coefficients is None:
                continue
            terms = [
                {**records[index], "coefficient": coefficient}
                for index, coefficient in zip(indices, coefficients)
            ]
            return relation_record("POSITIVE_DEPENDENCE", terms, None)
    raise GateFailure("no support-at-most-five certificate")


def highlights(prefixes: list[Matrix], requested: list[tuple[int, int]]) -> list[dict[str, object]]:
    table = {
        (int(record["step"]), int(record["coordinate"])): record
        for record in form_records(prefixes)
    }
    return [table[key] for key in requested]


def expected_census(
    raw_word: list[str],
    generators: dict[str, Matrix],
    action: Action,
    reverse: bool,
    phase_zero_descriptors: list[tuple[int, int]],
) -> dict[str, object]:
    phase_records = []
    for phase, rotation in enumerate(cyclic_words(raw_word)):
        sequence = list(reversed(rotation)) if reverse else rotation
        prefixes = action(sequence, generators)
        if prefixes[-1] != ident():
            raise GateFailure("cyclic action fails to close")
        phase_records.append(
            {
                "phase": phase,
                "raw_rotation": rotation,
                "action_sequence": sequence,
                "final_matrix": prefixes[-1],
                "farkas_infeasibility_certificate": canonical_relation(prefixes),
                "positive_cone_orbit_exists": False,
            }
        )
    zero_prefixes = action(phase_records[0]["action_sequence"], generators)
    return {
        "raw_path_word": raw_word,
        "word_length": len(raw_word),
        "phase_count": len(phase_records),
        "infeasible_phase_count": len(phase_records),
        "all_cyclic_phases_infeasible": True,
        "phase_zero_highlights": highlights(zero_prefixes, phase_zero_descriptors),
        "phase_records": phase_records,
    }


def expected_positive_control(
    raw_word: list[str], generators: dict[str, Matrix], witness: Vector
) -> dict[str, object]:
    base_prefixes = raw_prefixes(raw_word, generators)
    base_trajectory = [witness] + [mv(prefix, witness) for prefix in base_prefixes]
    if base_trajectory[-1] != witness or not all(
        coordinate > 0 for state in base_trajectory for coordinate in state
    ):
        raise GateFailure("source raw-control witness failed")
    phase_records = []
    for phase, rotation in enumerate(cyclic_words(raw_word)):
        initial = base_trajectory[phase]
        trajectory = [initial] + [
            mv(prefix, initial) for prefix in raw_prefixes(rotation, generators)
        ]
        if trajectory[-1] != initial or not all(
            coordinate > 0 for state in trajectory for coordinate in state
        ):
            raise GateFailure("rotated raw-control witness failed")
        phase_records.append(
            {
                "phase": phase,
                "raw_rotation": rotation,
                "initial_positive_integer_witness": initial,
                "trajectory": trajectory,
                "periodic_closure": True,
                "all_coordinates_strictly_positive": True,
            }
        )
    return {
        "raw_path_word": raw_word,
        "phase_zero_positive_integer_witness": witness,
        "phase_count": len(phase_records),
        "feasible_phase_count": len(phase_records),
        "all_cyclic_phases_feasible": True,
        "phase_records": phase_records,
    }


class Audit:
    def __init__(
        self, certificate: dict[str, object], certificate_file_sha256: str | None = None
    ):
        self.certificate = certificate
        self.payload = certificate.get("payload")
        if type(self.payload) is not dict:
            raise GateFailure("payload must be a dict")
        self.c25 = json.loads(SOURCES["C25_certificate"].read_text(encoding="utf-8"))
        self.c26 = json.loads(SOURCES["C26_certificate"].read_text(encoding="utf-8"))
        self.c29 = json.loads(SOURCES["C29_certificate"].read_text(encoding="utf-8"))
        self.certificate_file_sha256 = certificate_file_sha256 or canonical_digest(certificate)
        self.gates: list[dict[str, str]] = []

    def gate(self, gate_id: str, action: Callable[[], None]) -> None:
        try:
            action()
        except GateFailure as exc:
            self.gates.append({"gate": gate_id, "status": "FAIL", "detail": str(exc)})
        except Exception as exc:
            self.gates.append(
                {"gate": gate_id, "status": "ERROR", "detail": type(exc).__name__}
            )
        else:
            self.gates.append({"gate": gate_id, "status": "PASS", "detail": "exact"})

    def source_objects(self) -> tuple[dict[str, Matrix], dict[str, Matrix], list[str], list[str], list[str], list[str]]:
        c25_generators = {
            f"{int(edge['source'])}{edge['type']}": edge["chronological_matrix"]
            for edge in self.c25["graph"]["edges"]
        }
        locked = self.c29["payload"]["c25_identity_witnesses"]
        c1 = list(locked["C1"]["tokens_path_order"])
        c2 = list(locked["C2"]["tokens_path_order"])
        relation = self.c29["payload"]["c26_branch_relation"]
        c26_generators = {name: relation["matrices"][name] for name in ("A", "B", "C")}
        c26_path = list(relation["later_on_left_path_order_word"])
        c26_holonomy = list(relation["holonomy_order_word"])
        source = self.c26["source_locked_branch"]
        two = self.c26["scalar_periodic_trace_gate"]["chronological_two_return_witness"]
        three = self.c26["scalar_periodic_trace_gate"]["three_return_spectral_chronology_witness"]
        strict_equal(
            c26_generators,
            {
                "A": source["chronological_matrix_B"],
                "B": two["second_branch_chronological_matrix_B"],
                "C": three["third_branch_chronological_matrix_B"],
            },
            "C26 matrices",
        )
        if (
            chronological(c1, c25_generators) != ident()
            or chronological(c2, c25_generators) != ident()
            or c26_path != list(reversed(c26_holonomy))
            or chronological(c26_path, c26_generators) != ident()
            or textual(c26_holonomy, c26_generators) != ident()
        ):
            raise GateFailure("source chronology identity failed")
        return c25_generators, c26_generators, c1, c2, c26_path, c26_holonomy

    def g0_envelope(self) -> None:
        strict_equal(set(self.certificate), {"schema", "payload", "payload_sha256"}, "certificate keys")
        strict_equal(self.certificate["schema"], "hcs-c30-certificate-v3", "schema")
        strict_equal(self.certificate["payload_sha256"], canonical_digest(self.payload), "payload sha")

    def g1_contract(self) -> None:
        expected_keys = {
            "candidate_id", "candidate_name", "material_passport", "source_lock",
            "conventions", "raw_homology_zigzag_control",
            "forward_length_positive_cone_gate",
            "transfer_inverse_branch_positive_cone_gate", "projective_roof_cocycle",
            "identity_and_clock_semantics", "same_space_nuclearity",
            "identity_word_flat_trace", "decisions", "pivot",
            "route_a", "runtime",
        }
        strict_equal(set(self.payload), expected_keys, "payload keys")
        strict_equal(self.payload["candidate_id"], "HCS-C30", "candidate id")
        strict_equal(self.payload["candidate_name"], "Rauzy inverse roof and flat-trace obstruction", "candidate name")
        strict_equal(
            self.payload["material_passport"],
            {
                "schema": "ARS-compatible research artifact",
                "data_class": "exact source-locked integer matrices and theorem-level deductions",
                "human_subjects": False,
                "AI_assistance_disclosure_required": True,
                "verification_status": "PRODUCER_ONLY_UNTIL_INDEPENDENT_CHECKER",
            },
            "material passport",
        )
        strict_equal(
            self.payload["runtime"],
            {
                "arithmetic": "Python stdlib integers and Fraction only",
                "environment_fields_in_canonical_payload": False,
                "producer_sha256": digest(PRODUCER),
            },
            "runtime",
        )

    def g2_sources(self) -> None:
        observed = {name: digest(path) for name, path in SOURCES.items()}
        strict_equal(observed, SOURCE_DIGESTS, "live source hashes")
        strict_equal(
            self.payload["source_lock"],
            {
                "files": {
                    name: {"path": str(path.relative_to(REPO_ROOT)), "sha256": SOURCE_DIGESTS[name]}
                    for name, path in SOURCES.items()
                },
                "chronology_id": "RAW_LATER_ON_LEFT__FORWARD_LENGTH_INVERSE_TRANSPOSE__TRANSFER_REVERSED_TRANSPOSE",
                "data_policy": "exact integers and rationals only; no prime tables, zero tables, fitted clocks, or longer-word scans",
            },
            "source lock",
        )

    def g3_raw_control(self) -> None:
        c25m, c26m, c1, c2, c26path, _ = self.source_objects()
        expected = {
            "action": "v_k=B(t_k)*v_(k-1), with later tokens multiplying on the left",
            "classification": "covariant raw-homology zigzag; this is not the AGY forward length action",
            "C25_positive_controls": {
                "C1": expected_positive_control(c1, c25m, [1, 2, 1, 1]),
                "C2": expected_positive_control(c2, c25m, [1, 1, 3, 1]),
            },
            "C26_infeasibility": expected_census(
                c26path, c26m, raw_prefixes, False, [(0, 0), (7, 3)]
            ),
        }
        strict_equal(self.payload["raw_homology_zigzag_control"], expected, "raw control")

    def g4_forward(self) -> None:
        c25m, c26m, c1, c2, c26path, _ = self.source_objects()
        expected = {
            "action": "lambda_k=B(t_k)^(-T)*lambda_(k-1) in raw path order",
            "phase_policy": "all left cyclic rotations of each raw later-on-left path word",
            "words": {
                "C25_C1": expected_census(c1, c25m, length_prefixes, False, [(1, 3), (4, 1)]),
                "C25_C2": expected_census(c2, c25m, length_prefixes, False, [(0, 0), (3, 2)]),
                "C26_W24": expected_census(c26path, c26m, length_prefixes, False, [(4, 2), (16, 3)]),
            },
        }
        strict_equal(self.payload["forward_length_positive_cone_gate"], expected, "forward length")

    def g5_transfer(self) -> None:
        c25m, c26m, c1, c2, c26path, holonomy = self.source_objects()
        expected = {
            "action": "for each raw rotation reverse path order, then x_k=B(t_k)^T*x_(k-1)",
            "phase_policy": "reverse each left cyclic rotation of the raw later-on-left path word",
            "C26_phase_zero_equivalent_holonomy_word": holonomy,
            "words": {
                "C25_C1": expected_census(c1, c25m, inverse_branch_prefixes, True, [(1, 1), (4, 3)]),
                "C25_C2": expected_census(c2, c25m, inverse_branch_prefixes, True, [(0, 0), (2, 2)]),
                "C26_W24": expected_census(c26path, c26m, inverse_branch_prefixes, True, [(3, 1), (8, 3), (20, 2)]),
            },
        }
        strict_equal(self.payload["transfer_inverse_branch_positive_cone_gate"], expected, "transfer")

    def g6_roof(self) -> None:
        strict_equal(
            self.payload["projective_roof_cocycle"],
            {
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
            "roof gate",
        )

    def g7_nuclear(self) -> None:
        strict_equal(
            self.payload["same_space_nuclearity"],
            {
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
            "nuclear gate",
        )

    def g8_flat_trace(self) -> None:
        strict_equal(
            self.payload["identity_word_flat_trace"],
            {
                "base_map_for_each_certified_word": "h_W=id on its algebraic projective domain",
                "derivative": "Dh_W=I",
                "fixed_set": "the full domain, not isolated periodic points",
                "fixed_point_denominator": "det(I-Dh_W)=0",
                "standard_isolated_fixed_point_flat_trace_applies": False,
                "ordinary_nuclear_word_trace_applies": False,
                "scope": "rules out the standard holomorphic isolated-fixed-point/nuclear realization; it does not rule out every conceivable clean-fixed-set regularization",
            },
            "flat trace gate",
        )

    def g9_decisions(self) -> None:
        strict_equal(
            self.payload["decisions"],
            {
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
            "decisions",
        )

    def g10_scope_and_pivot(self) -> None:
        strict_equal(
            self.payload["route_a"],
            {
                "tuple": ["A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
                "overall": "ROUTE_A_REJECTED_FOR_DYNAMICAL_PROMOTION",
                "retained_output": "exact negative theorem plus finite combinatorial C29 determinant germ",
            },
            "route A",
        )
        strict_equal(
            self.payload["pivot"],
            {
                "next_system": "the genuine analytic area-preserving H_6 hyperbolic basic set",
                "inherited_infrastructure": "henon_pinning_trace_obstruction exact BPS one-step mixed domains and pinning kernel",
                "next_operator_form": "quantitative common-space composition and determinant-tail theorem for the existing H_6 pinning infrastructure",
                "reason": "true positive-time H_6 iterates avoid formal direction switching and identity projective words",
                "nonduplication": "do not rebuild the qualitative BPS/Rugh pinning operator or re-claim its known nuclear trace theory",
                "forbidden_next_step": "no longer-word or small-prime scan of the C29 formal inverse groupoid",
            },
            "pivot",
        )

    def g11_conventions(self) -> None:
        strict_equal(
            self.payload["conventions"],
            {
                "raw_matrix_chronology": "later Rauzy arrows multiply on the left",
                "raw_homology_control": "covariant B(t) zigzags are controls and are not AGY forward length orbits",
                "forward_length_action": "B(t)^(-T) in raw path order",
                "transfer_inverse_branch_action": "reverse each raw path phase, then apply B(t)^T",
                "positive_cone": "all four unnormalised coordinates are strictly positive initially and after every prefix",
                "identity_word_scope": "raw matrix identity, not merely a finite-Weil character coincidence",
            },
            "conventions",
        )

    def g12_identity_and_clock(self) -> None:
        _, _, c1, c2, c26path, _ = self.source_objects()
        c1_all = signed_counts(c1, sorted({token[:-3] if token.endswith("^-1") else token for token in c1}))
        c2_all = signed_counts(c2, sorted({token[:-3] if token.endswith("^-1") else token for token in c2}))
        c1_nonzero = {name: value for name, value in c1_all.items() if value}
        c2_nonzero = {name: value for name, value in c2_all.items() if value}
        c26_all = signed_counts(c26path, ("A", "B", "C"))
        strict_equal(c1_nonzero, {"1b": 1, "3t": 1}, "C1 abelianization source")
        strict_equal(c2_nonzero, {"4t": 1, "5b": 1}, "C2 abelianization source")
        strict_equal(c26_all, {"A": 0, "B": 0, "C": 0}, "C26 abelianization source")
        reduced_lengths = {
            "C25_C1": len(free_reduction(c1)),
            "C25_C2": len(free_reduction(c2)),
            "C26_W24": len(free_reduction(c26path)),
        }
        strict_equal(reduced_lengths, {"C25_C1": 6, "C25_C2": 6, "C26_W24": 24}, "formal reduced lengths")
        expected = {
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
                    "generator_counts": c26_all,
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
        strict_equal(self.payload["identity_and_clock_semantics"], expected, "identity and clock semantics")

    def run(self) -> dict[str, object]:
        checks = [
            ("G0_ENVELOPE_AND_PAYLOAD_HASH", self.g0_envelope),
            ("G1_TYPE_STRICT_CONTRACT", self.g1_contract),
            ("G2_SOURCE_LOCK", self.g2_sources),
            ("G3_RAW_HOMOLOGY_CONTROL", self.g3_raw_control),
            ("G4_FORWARD_LENGTH_ALL_PHASES", self.g4_forward),
            ("G5_TRANSFER_BRANCH_ALL_PHASES", self.g5_transfer),
            ("G6_ROOF_COCYCLE", self.g6_roof),
            ("G7_SAME_SPACE_NUCLEARITY", self.g7_nuclear),
            ("G8_IDENTITY_WORD_FLAT_TRACE", self.g8_flat_trace),
            ("G9_DECISIONS", self.g9_decisions),
            ("G10_ROUTE_AND_PIVOT_SCOPE", self.g10_scope_and_pivot),
            ("G11_CHRONOLOGY_CONVENTIONS", self.g11_conventions),
            ("G12_IDENTITY_AND_CLOCK_SEMANTICS", self.g12_identity_and_clock),
        ]
        for gate_id, method in checks:
            self.gate(gate_id, method)
        passed = sum(item["status"] == "PASS" for item in self.gates)
        return {
            "schema": "hcs-c30-independent-check-v3",
            "certificate_sha256": self.certificate_file_sha256,
            "certificate_payload_sha256": self.certificate.get("payload_sha256"),
            "checker_independence": "does not import c30_producer",
            "gates": self.gates,
            "passed": passed,
            "total": len(self.gates),
            "all_pass": passed == len(self.gates),
        }


def main() -> None:
    args = cli()
    try:
        certificate = json.loads(args.certificate.read_text(encoding="utf-8"))
        if type(certificate) is not dict:
            raise GateFailure("certificate root must be a dict")
        report = Audit(certificate, digest(args.certificate)).run()
    except Exception as exc:
        report = {
            "schema": "hcs-c30-independent-check-v3",
            "certificate_sha256": digest(args.certificate) if args.certificate.exists() else None,
            "certificate_payload_sha256": None,
            "checker_independence": "does not import c30_producer",
            "gates": [{"gate": "G0_INPUT", "status": "ERROR", "detail": type(exc).__name__}],
            "passed": 0,
            "total": 1,
            "all_pass": False,
        }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(report, indent=2, sort_keys=True, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    print(f"independent gates: {report['passed']}/{report['total']}")
    print(f"all_pass={report['all_pass']}")
    raise SystemExit(0 if report["all_pass"] else 1)


if __name__ == "__main__":
    main()
