#!/usr/bin/env python3
"""Independent fail-closed checker for the HCS-C32 Phase-3 certificate.

The checker does not import the producer.  Its scan is based on a cycle
decomposition of the full Hénon permutation of F_p^2, rather than the
producer's separate state-by-state period tests.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Callable


SCHEMA = "HCS-C32-PHASE3-MORSE-GATE-1"
CANDIDATE = "HCS-C32-MORSE-LOCAL-HILL-GATE"
PRIMES = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
PERIODS = [1, 2, 3, 4, 5]
PROJECT = Path(__file__).resolve().parents[1]
REPO = PROJECT.parents[1]

SOURCE_EXPECTED = {
    "henon_dynamics/phase1_hcs_c32_artin_schreier_quantum_trace/RESEARCH_QUESTION_BRIEF.md": "28ccf8b0cf7dc59584630e98a88d67cd630ec46caac08a69f2a10bee4a6a9a4e",
    "henon_dynamics/phase1_hcs_c32_artin_schreier_quantum_trace/METHODOLOGY_BLUEPRINT.md": "a6be8f6d2e4ad8063ee743966390553d8e7370c15dc77a7895fb840fd5c91b8d",
    "henon_dynamics/phase1_hcs_c32_artin_schreier_quantum_trace/DEVILS_ADVOCATE_CHECKPOINT1.md": "8d60ca898d1e2fb52b95216f5e65b72d99a871804e368d43936f961aa238d974",
    "henon_dynamics/phase2_hcs_c32_artin_schreier_quantum_trace/SEARCH_STRATEGY.md": "4b156ca8b17e4fc5122d95e9d62bb300140ac8b7f2b25131b7551a58a8a162cf",
    "henon_dynamics/phase2_hcs_c32_artin_schreier_quantum_trace/SOURCE_CORPUS_AND_ANNOTATED_BIBLIOGRAPHY.md": "75b975013aea8835df561f6eb8cbea557486018379e002a80b2a26923c167ee4",
    "henon_dynamics/phase2_hcs_c32_artin_schreier_quantum_trace/SOURCE_VERIFICATION_REPORT.md": "4cc9bc74a22166f7aeb716ca91ef5bf35caf31d4c293fe87d67489a91688c1ec",
    "henon_dynamics/henon_frobenius_scheme_obstruction/DERIVATION_PACKAGE.md": "f524678196be667f0861c8cf64cb2f847824e3604bc356d6e59ca3188bdc6dfb",
    "henon_dynamics/henon_frobenius_scheme_obstruction/results/c12a_certificate.json": "851ca31f62fb508ad806c26084eab9fe092d5ee037bf99f0cb811cbccf7f8eb8",
    "henon_dynamics/phase3_hcs_c32_artin_schreier_quantum_trace/EXACT_GATE_PROTOCOL.md": "88e13159c3572a2bd64ef4801867b896b328f9e0db2c1033827ab5d5994cfe0d",
}


class GateFailure(Exception):
    """Expected semantic rejection."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise GateFailure(message)


def strict_equal(left: Any, right: Any) -> bool:
    if type(left) is not type(right):
        return False
    if isinstance(left, dict):
        return set(left) == set(right) and all(
            strict_equal(left[key], right[key]) for key in left
        )
    if isinstance(left, list):
        return len(left) == len(right) and all(
            strict_equal(a, b) for a, b in zip(left, right)
        )
    return left == right


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def step(state: tuple[int, int], p: int) -> tuple[int, int]:
    x, previous = state
    return ((1 - 6 * x * x - previous) % p, x)


def permutation_cycles(p: int) -> list[list[tuple[int, int]]]:
    unseen = {(x, y) for x in range(p) for y in range(p)}
    cycles = []
    while unseen:
        start = min(unseen)
        cycle = []
        current = start
        while True:
            require(current in unseen, "H6 state graph failed permutation partition")
            unseen.remove(current)
            cycle.append(current)
            current = step(current, p)
            if current == start:
                break
        cycles.append(cycle)
    return cycles


def rotations(word: tuple[int, ...]) -> list[tuple[int, ...]]:
    return sorted(
        {word[shift:] + word[:shift] for shift in range(len(word))}
    )


def canonical(word: tuple[int, ...]) -> tuple[int, ...]:
    return min(rotations(word))


def action(word: tuple[int, ...], p: int) -> int:
    return sum(
        word[i] * word[(i + 1) % len(word)] - word[i] + 2 * word[i] ** 3
        for i in range(len(word))
    ) % p


def residuals(word: tuple[int, ...], p: int) -> list[int]:
    return [
        (word[i - 1] + word[(i + 1) % len(word)] - 1 + 6 * word[i] ** 2)
        % p
        for i in range(len(word))
    ]


def hessian(word: tuple[int, ...], p: int) -> list[list[int]]:
    n = len(word)
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        result[i][i] = 12 * word[i] % p
    # Different construction from the producer: take two formal derivatives
    # of every cyclic bilinear monomial by iterating its variable positions.
    for i in range(n):
        j = (i + 1) % n
        result[i][j] = (result[i][j] + 1) % p
        result[j][i] = (result[j][i] + 1) % p
    return result


def determinant(matrix: list[list[int]], p: int) -> int:
    n = len(matrix)
    if n == 0:
        return 1
    # Bareiss-style recursive expansion is deliberately independent of the
    # producer's modular Gaussian elimination.  Dimensions are at most five.
    total = 0
    for column, value in enumerate(matrix[0]):
        minor = [
            row[:column] + row[column + 1 :] for row in matrix[1:]
        ]
        total += (-1) ** column * value * determinant(minor, p)
    return total % p


def character(value: int, p: int) -> int:
    value %= p
    if value == 0:
        return 0
    symbol = pow(value, (p - 1) // 2, p)
    require(symbol in (1, p - 1), "Euler criterion returned invalid value")
    return 1 if symbol == 1 else -1


def multiply_2x2(
    left: list[list[int]], right: list[list[int]], p: int
) -> list[list[int]]:
    return [
        [
            (left[i][0] * right[0][j] + left[i][1] * right[1][j]) % p
            for j in range(2)
        ]
        for i in range(2)
    ]


def derivative_product(word: tuple[int, ...], p: int) -> list[list[int]]:
    product = [[1, 0], [0, 1]]
    for x in word:
        product = multiply_2x2(
            [[(-12 * x) % p, p - 1], [1, 0]], product, p
        )
    return product


def hill(matrix: list[list[int]], p: int) -> int:
    return (
        (1 - matrix[0][0]) * (1 - matrix[1][1])
        - matrix[0][1] * matrix[1][0]
    ) % p


def record(word: tuple[int, ...], p: int) -> dict[str, Any]:
    form = hessian(word, p)
    det_form = determinant(form, p)
    mon = derivative_product(word, p)
    hill_value = hill(mon, p)
    return {
        "q_word": list(word),
        "action": action(word, p),
        "critical_residuals": residuals(word, p),
        "hessian_matrix": form,
        "hessian_det": det_form,
        "quadratic_character": character(det_form, p),
        "monodromy_matrix": mon,
        "monodromy_det": determinant(mon, p),
        "hill_det": hill_value,
        "hill_identity_rhs": ((-1) ** (len(word) + 1) * hill_value) % p,
    }


def collision_summary(cycles: list[list[tuple[int, int]]], n: int, p: int) -> list[dict[str, Any]]:
    groups: dict[tuple[int, int], dict[tuple[int, ...], dict[str, Any]]] = {}
    for cycle in cycles:
        if len(cycle) != n:
            continue
        word = tuple(state[0] for state in cycle)
        for rotation in rotations(word):
            item = record(rotation, p)
            if item["hessian_det"] == 0:
                continue
            key = (item["action"], item["quadratic_character"])
            groups.setdefault(key, {})[canonical(rotation)] = item
    result = []
    for key, orbit_map in sorted(groups.items()):
        dets = sorted({item["hessian_det"] for item in orbit_map.values()})
        if len(dets) > 1:
            result.append(
                {
                    "action": key[0],
                    "quadratic_character": key[1],
                    "cycle_count": len(orbit_map),
                    "determinants": dets,
                    "canonical_words": [
                        list(word) for word in sorted(orbit_map)
                    ],
                }
            )
    return result


def independent_scan() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    cycle_cache = {p: permutation_cycles(p) for p in PRIMES}
    rows = []
    first = None
    for n in PERIODS:
        for p in PRIMES:
            cycles = cycle_cache[p]
            primitive = [cycle for cycle in cycles if len(cycle) == n]
            primitive_records = [
                record(tuple(state[0] for state in cycle), p)
                for cycle in primitive
                for _ in cycle
            ]
            collisions = collision_summary(cycles, n, p)
            rows.append(
                {
                    "p": p,
                    "n": n,
                    "all_fixed_states": sum(
                        len(cycle) for cycle in cycles if n % len(cycle) == 0
                    ),
                    "primitive_states": sum(len(cycle) for cycle in primitive),
                    "primitive_morse_states": sum(
                        item["hessian_det"] != 0 for item in primitive_records
                    ),
                    "collision_groups": len(collisions),
                }
            )
            if first is None and collisions:
                first = {"p": p, "n": n, **collisions[0]}
    require(first is not None, "independent scan found no collision")
    return rows, first


def matrix_multiply(
    left: list[list[int]], right: list[list[int]], p: int
) -> list[list[int]]:
    return [
        [
            sum(left[i][k] * right[k][j] for k in range(len(right))) % p
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def matrix_transpose(matrix: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*matrix)]


class Audit:
    def __init__(self, certificate: dict[str, Any]):
        self.certificate = certificate
        self.results: list[dict[str, str]] = []

    def gate(self, gate_id: str, description: str, function: Callable[[], None]) -> None:
        try:
            function()
        except GateFailure as exc:
            self.results.append(
                {"gate": gate_id, "description": description, "status": "FAIL", "detail": str(exc)}
            )
        except Exception as exc:  # unexpected checker bugs are never semantic rejections
            self.results.append(
                {
                    "gate": gate_id,
                    "description": description,
                    "status": "ERROR",
                    "detail": f"{type(exc).__name__}: {exc}",
                }
            )
        else:
            self.results.append(
                {"gate": gate_id, "description": description, "status": "PASS", "detail": "exact replay passed"}
            )

    @property
    def payload(self) -> dict[str, Any]:
        payload = self.certificate.get("payload")
        require(type(payload) is dict, "payload must be an object")
        return payload


def run_audit(certificate: dict[str, Any]) -> dict[str, Any]:
    audit = Audit(certificate)

    def gate0() -> None:
        require(
            set(certificate)
            == {"schema_version", "candidate_id", "producer_status", "payload", "payload_sha256"},
            "top-level keyset mismatch",
        )
        require(certificate["schema_version"] == SCHEMA, "schema mismatch")
        require(certificate["candidate_id"] == CANDIDATE, "candidate mismatch")
        require(
            certificate["producer_status"]
            == "PRODUCER_ONLY_UNVERIFIED_UNTIL_INDEPENDENT_CHECKER",
            "producer firewall missing",
        )
        require(
            certificate["payload_sha256"] == sha256(canonical_bytes(audit.payload)),
            "canonical payload digest mismatch",
        )
        require(
            set(audit.payload)
            == {
                "material_passport",
                "source_lock",
                "conventions",
                "theorem_bridge",
                "registered_scan",
                "witness",
                "decisions",
                "scope",
            },
            "payload keyset mismatch",
        )

    audit.gate("G0", "schema, keysets, and canonical payload digest", gate0)

    def gate1() -> None:
        passport = audit.payload["material_passport"]
        expected = {
            "candidate_id": CANDIDATE,
            "phase": 3,
            "artifact_kind": "exact_experiment_certificate",
            "evidence_status": "THEOREM_PLUS_EXACT_FINITE_FIELD_CERTIFICATE",
            "ai_assistance": True,
            "post_pilot_disclosure": "p=61,n=5 witness was discovered before protocol freeze and is not a preregistered prediction",
        }
        require(strict_equal(passport, expected), "material passport mismatch")

    audit.gate("G1", "material passport and post-pilot disclosure", gate1)

    def gate2() -> None:
        observed = audit.payload["source_lock"]
        expected = [
            {"path": path, "sha256": digest}
            for path, digest in SOURCE_EXPECTED.items()
        ]
        require(strict_equal(observed, expected), "source-lock payload mismatch")
        for item in expected:
            path = REPO / item["path"]
            require(path.is_file(), f"missing source {item['path']}")
            require(sha256(path.read_bytes()) == item["sha256"], f"stale source {item['path']}")

    audit.gate("G2", "source-lock contract and live file hashes", gate2)

    expected_conventions = {
        "map": "H6(q,p)=(1-6*q^2-p,q)",
        "action": "Phi_n=sum_i(x_i*x_(i+1)-x_i+2*x_i^3)",
        "chronology": "DH^n=A(x_(n-1))*...*A(x_0), later factors on the left",
        "hessian": "derived term-by-term; n=1 diagonal and n=2 double mixed edge preserved",
        "hill_identity": "det Hess(Phi_n)=(-1)^(n+1)*det(I-DH6^n)",
        "local_fourier_shift": "shifted Fourier-Deligne trace is -E; raw unshifted Fourier integral trace is E",
    }
    audit.gate(
        "G3",
        "chronology, Hessian multiplicity, Hill, and Fourier-shift conventions",
        lambda: require(strict_equal(audit.payload["conventions"], expected_conventions), "convention mismatch"),
    )

    expected_theorem_bridge = {
        "formal_morse": {
            "source": "Deligne and Katz, SGA 7 II, Expose XV",
            "locator": "Theorem 1.2.6 and Corollary 1.3.2, journal pages 168-176",
            "hypotheses": "residue characteristic not 2 and isolated nondegenerate critical point",
            "conclusion": "the henselian germ is equivalent over the residue field to its nondegenerate quadratic model",
        },
            "quadratic_vanishing_cycles": {
                "source": "Fu, A Thom-Sebastiani Theorem in Characteristic p (2014)",
                "locator": "Example 2.3 and Corollary 2.4, published pages 104-105",
                "conclusion": "the vanishing-cycle representation of a nondegenerate quadratic germ is rank one and determined by the quadratic form through Kummer/Gauss data",
            },
        "local_fourier": {
            "source": "Laumon, Transformation de Fourier (1987)",
            "locator": "Definition 2.4.2.3, Theorem 2.4.3, and Proposition 2.5.3.1, pages 162-166",
            "conclusion": "local Fourier transform sends the quadratic Kummer character to its Gauss representation, with the stated shift conventions",
        },
        "application": "equal critical value plus the explicit F_61 Hessian congruence gives isomorphic henselian function germs and hence isomorphic Morse-local vanishing-cycle Frobenius representations",
        "infinity_boundary": "local stationary phase does not identify or eliminate the contribution at infinity of the global Fourier transform",
    }
    audit.gate(
        "G3B",
        "primary-source theorem bridge and infinity boundary",
        lambda: require(strict_equal(audit.payload["theorem_bridge"], expected_theorem_bridge), "theorem bridge mismatch"),
    )

    independent_rows, independent_first = independent_scan()

    def gate4() -> None:
        scan = audit.payload["registered_scan"]
        require(
            set(scan) == {"ordering", "primes", "periods", "rows", "first_collision"},
            "registered scan keyset mismatch",
        )
        require(scan["ordering"] == "n_then_p_ascending", "scan ordering mismatch")
        require(strict_equal(scan["primes"], PRIMES), "prime register mismatch")
        require(strict_equal(scan["periods"], PERIODS), "period register mismatch")
        require(strict_equal(scan["rows"], independent_rows), "independent scan rows disagree")
        require(strict_equal(scan["first_collision"], independent_first), "first collision disagrees")

    audit.gate("G4", "independent permutation-cycle scan", gate4)

    def witness_records() -> tuple[int, int, list[dict[str, Any]], dict[str, Any]]:
        witness = audit.payload["witness"]
        require(
            set(witness)
            == {
                "p",
                "n",
                "common_action",
                "common_quadratic_character",
                "orbit_classes",
                "determinant_square_ratio",
                "quadratic_congruence",
                "local_trace_equivalence",
            },
            "witness keyset mismatch",
        )
        p = witness["p"]
        n = witness["n"]
        require((p, n) == (61, 5), "witness coordinates changed")
        supplied = witness["orbit_classes"]
        require(type(supplied) is list and len(supplied) == 2, "need exactly two orbit classes")
        replayed = []
        for item in supplied:
            word = tuple(item["q_word"])
            require(len(word) == n, "orbit word length mismatch")
            current = (word[0], word[-1])
            states = []
            for _ in range(n):
                states.append(current)
                current = step(current, p)
            require(current == states[0], "word does not close dynamically")
            require(all(step(states[i], p) == states[(i + 1) % n] for i in range(n)), "chronology mismatch")
            require(not any(states[k] == states[0] for k in range(1, n)), "orbit is not primitive")
            require(word == canonical(word), "word is not the canonical rotation")
            expected = record(word, p)
            expected["canonical_rotation"] = True
            expected["primitive_state_period"] = n
            expected["rotations"] = [list(rotation) for rotation in rotations(word)]
            require(strict_equal(item, expected), "orbit record mismatch")
            replayed.append(expected)
        return p, n, replayed, witness

    audit.gate("G5", "primitive chronological orbit replay and rotation classes", lambda: witness_records())

    def gate6() -> None:
        p, n, replayed, witness = witness_records()
        require(witness["common_action"] == 45, "common action sentinel changed")
        require(all(item["action"] == 45 for item in replayed), "action mismatch")
        require(all(item["critical_residuals"] == [0] * n for item in replayed), "critical residual nonzero")

    audit.gate("G6", "critical equations and common action value", gate6)

    def gate7() -> None:
        p, n, replayed, witness = witness_records()
        dets = sorted(item["hessian_det"] for item in replayed)
        require(dets == [7, 44], "Hessian determinant sentinels changed")
        require(all(item["hessian_det"] != 0 for item in replayed), "non-Morse point admitted")
        require(all(item["quadratic_character"] == -1 for item in replayed), "quadratic class mismatch")
        require(witness["common_quadratic_character"] == -1, "common character mismatch")
        # Explicit small-clock sentinels protect the n=1/n=2 multiplicities.
        require(hessian((3,), p) == [[(12 * 3 + 2) % p]], "n=1 Hessian multiplicity wrong")
        require(hessian((3, 4), p) == [[36, 2], [2, 48]], "n=2 Hessian multiplicity wrong")

    audit.gate("G7", "Hessian reconstruction, nondegeneracy, and square class", gate7)

    def gate8() -> None:
        p, n, replayed, _ = witness_records()
        require(all(item["monodromy_det"] == 1 for item in replayed), "symplectic determinant failed")
        for item in replayed:
            require(item["hessian_det"] == item["hill_identity_rhs"], "Hill identity failed")
        require(sorted(item["hill_det"] for item in replayed) == [7, 44], "Hill values not distinct")

    audit.gate("G8", "chronological monodromy and cyclic Hill identity", gate8)

    def gate9() -> None:
        p, _, replayed, witness = witness_records()
        ratio = replayed[0]["hessian_det"] * pow(replayed[1]["hessian_det"], -1, p) % p
        root = next((x for x in range(p) if x * x % p == ratio), None)
        expected = {"first_over_second": ratio, "least_square_root": root, "square_check": ratio}
        require(strict_equal(witness["determinant_square_ratio"], expected), "square-ratio witness mismatch")

    audit.gate("G9", "unequal determinants with an exact square ratio", gate9)

    def gate10() -> None:
        p, _, replayed, witness = witness_records()
        block = witness["quadratic_congruence"]
        require(set(block) == {"direction", "matrix", "matrix_det", "verified"}, "congruence keyset mismatch")
        require(block["direction"] == "C^T*H_first*C=H_second mod p", "congruence direction mismatch")
        matrix = block["matrix"]
        require(type(matrix) is list and len(matrix) == 5 and all(type(row) is list and len(row) == 5 for row in matrix), "congruence shape mismatch")
        require(determinant(matrix, p) == block["matrix_det"] != 0, "congruence matrix singular or determinant false")
        transformed = matrix_multiply(
            matrix_multiply(matrix_transpose(matrix), replayed[0]["hessian_matrix"], p), matrix, p
        )
        require(transformed == replayed[1]["hessian_matrix"], "explicit Hessian congruence failed")
        require(block["verified"] is True, "congruence verification flag missing")

    audit.gate("G10", "explicit GL_5 Hessian-congruence witness", gate10)

    def gate11() -> None:
        block = audit.payload["witness"]["local_trace_equivalence"]
        expected = {
            "quadratic_sum_formula": "psi(t*c)*chi(t)^n*chi(det(H))*chi(2)^(-n)*G(psi)^n",
            "same_for_every_nonzero_t": True,
            "reason": "same c,n and discriminant square class; explicit Hessian congruence gives a finite-field bijection of quadratic models",
            "full_hill_values_distinguished": [7, 44],
            "henselian_germs_isomorphic": True,
            "morse_local_vanishing_cycle_representations_isomorphic": True,
        }
        require(strict_equal(block, expected), "local quadratic-trace contract mismatch")

    audit.gate("G11", "local quadratic trace equivalence without full Hill recovery", gate11)

    def gate12() -> None:
        expected_decisions = {
            "good_prime_morse_local_hill_information_gate": "STOP_THEOREM_EXACT_COLLISION",
            "computational_collision": "PROVED_EXACT",
            "global_artin_schreier_cohomology_no_go": False,
            "degenerate_or_bad_prime_no_go": False,
            "hilbert_polya_structure": "NOT_ESTABLISHED",
            "route_a_formal_status": "NOT_TESTABLE",
            "route_b_authorized": False,
        }
        expected_scope = {
            "proved_by_computation": "two primitive H6 period-5 classes over F_61 have identical Morse-local quadratic data and unequal Hill determinants",
            "requires_primary_theorem": "formal/etale Morse lemma and l-adic stationary phase identify the vanishing-cycle local representation with the quadratic model",
            "not_claimed": [
                "no global cohomological information",
                "no statement at degenerate critical points",
                "no statement at bad primes or at infinity",
                "no canonical global determinant or Hilbert-Polya operator",
            ],
        }
        require(strict_equal(audit.payload["decisions"], expected_decisions), "decision scope mismatch")
        require(strict_equal(audit.payload["scope"], expected_scope), "claim-boundary mismatch")

    audit.gate("G12", "STOP conditionality, Route-A status, and no-go scope", gate12)

    statuses = [item["status"] for item in audit.results]
    return {
        "schema_version": "HCS-C32-PHASE3-INDEPENDENT-CHECK-1",
        "candidate_id": CANDIDATE,
        "gates": audit.results,
        "passed": statuses.count("PASS"),
        "failed": statuses.count("FAIL"),
        "errors": statuses.count("ERROR"),
        "all_pass": all(status == "PASS" for status in statuses),
        "certificate_payload_sha256": certificate.get("payload_sha256"),
    }


def audit_file(path: Path) -> dict[str, Any]:
    try:
        certificate = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return {
            "schema_version": "HCS-C32-PHASE3-INDEPENDENT-CHECK-1",
            "candidate_id": CANDIDATE,
            "gates": [],
            "passed": 0,
            "failed": 0,
            "errors": 1,
            "all_pass": False,
            "certificate_payload_sha256": None,
            "fatal_error": f"{type(exc).__name__}: {exc}",
        }
    if type(certificate) is not dict:
        return {
            "schema_version": "HCS-C32-PHASE3-INDEPENDENT-CHECK-1",
            "candidate_id": CANDIDATE,
            "gates": [],
            "passed": 0,
            "failed": 1,
            "errors": 0,
            "all_pass": False,
            "certificate_payload_sha256": None,
            "fatal_error": "certificate root must be an object",
        }
    return run_audit(certificate)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = audit_file(args.certificate)
    text = json.dumps(report, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    raise SystemExit(0 if report["all_pass"] else 1)


if __name__ == "__main__":
    main()
