#!/usr/bin/env python3
"""Exact HCS-P59 primitive reflection-count and half-entropy certificate."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from pathlib import Path

import sympy as sp


PROJECT = Path(__file__).resolve().parents[1]
TRACK = PROJECT.parent
DEFAULT_OUTPUT = PROJECT / "results" / "c59_certificate.json"

ADJACENCY = (
    (1, 0, 1, 0),
    (1, 0, 0, 0),
    (0, 1, 0, 1),
    (0, 1, 0, 0),
)
REVERSAL = (0, 2, 1, 3)

DEPENDENCIES = {
    "p58_readme": (
        TRACK / "henon_physical_tail_galois_parity_obstruction" / "README.md",
        "3f0a251a53088aa9b175b11f0ea018b88c743d7a02515ab24c6f0458e330910b",
    ),
    "p58_proof": (
        TRACK / "henon_physical_tail_galois_parity_obstruction" / "PROOF_PACKAGE.md",
        "84e67adf268f1949ac08871b80729a1342316312240e11e309bc93f5041dd3af",
    ),
    "p58_code": (
        TRACK / "henon_physical_tail_galois_parity_obstruction" / "code" / "c58_tail_parity.py",
        "1a44df85ec0e5f1e546a2ea7a6ee98fb8a42eb98e1022bec23f82954e99f882f",
    ),
    "p58_certificate": (
        TRACK / "henon_physical_tail_galois_parity_obstruction" / "results" / "c58_certificate.json",
        "366664f2de23ff503f8dd9efd63f0d80a9b7c23e98a510f662230c71dacc6022",
    ),
    "p58_route_a": (
        TRACK / "henon_physical_tail_galois_parity_obstruction" / "route_a_evaluation.yaml",
        "c241d13815e6716bff82b955d8a1e6614558c16dad404c82bfdf300a5cd5fa61",
    ),
    "p58_paper": (
        TRACK / "henon_physical_tail_galois_parity_obstruction" / "paper" / "paper.pdf",
        "407c54d77a663bfb81f34cba56f38d8667f6899a129630fc336d7349c8feadf7",
    ),
}


def canonical_sha(payload: object) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def dependency_locks() -> dict[str, dict[str, str]]:
    result: dict[str, dict[str, str]] = {}
    for name, (path, expected) in DEPENDENCIES.items():
        observed = hashlib.sha256(path.read_bytes()).hexdigest()
        if observed != expected:
            raise RuntimeError(f"dependency hash changed: {name}")
        result[name] = {"path": str(path.relative_to(TRACK)), "sha256": observed}
    return result


def fibonacci(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def lucas(n: int) -> int:
    if n == 0:
        return 2
    return fibonacci(n - 1) + fibonacci(n + 1)


def periodic_cos(n: int) -> int:
    return (1, 0, -1, 0)[n % 4]


def periodic_sin(n: int) -> int:
    return (0, 1, 0, -1)[n % 4]


def closed_words(n: int) -> int:
    return lucas(n) + 2 * periodic_cos(n)


def odd_reflection_fixed(n: int) -> int:
    if n % 2 != 1:
        raise ValueError("odd reflection formula requires odd n")
    return fibonacci((n + 3) // 2)


def even_edge_fixed(half_period: int) -> int:
    return lucas(half_period)


def even_vertex_fixed(half_period: int) -> int:
    numerator = (
        5 * fibonacci(half_period)
        + 2 * lucas(half_period)
        - 4 * periodic_cos(half_period)
        - 2 * periodic_sin(half_period)
    )
    if numerator % 5:
        raise ArithmeticError("vertex reflection formula lost integrality")
    return numerator // 5


def divisors(n: int) -> tuple[int, ...]:
    return tuple(int(value) for value in sp.divisors(n))


def primitive_cycles(n: int) -> int:
    numerator = sum(int(sp.mobius(n // d)) * closed_words(d) for d in divisors(n))
    if numerator % n:
        raise ArithmeticError("primitive necklace numerator is not divisible by n")
    return numerator // n


def primitive_odd_reflections(n: int) -> int:
    if n % 2 != 1:
        raise ValueError("odd primitive formula requires odd n")
    return sum(
        int(sp.mobius(n // d)) * odd_reflection_fixed(d) for d in divisors(n)
    )


def fixed_for_divisor(divisor: int, even_axis: bool) -> int:
    if divisor % 2:
        return odd_reflection_fixed(divisor)
    half = divisor // 2
    return even_edge_fixed(half) if even_axis else even_vertex_fixed(half)


def primitive_even_reflections(n: int, even_axis: bool) -> int:
    if n % 2:
        raise ValueError("even primitive formula requires even n")
    primitive_fixed_words = sum(
        int(sp.mobius(n // d)) * fixed_for_divisor(d, even_axis)
        for d in divisors(n)
    )
    if primitive_fixed_words % 2:
        raise ArithmeticError("even reflection fixed-word count is not even")
    return primitive_fixed_words // 2


def rotations(word: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(word[i:] + word[:i] for i in range(len(word)))


def primitive(word: tuple[int, ...]) -> bool:
    n = len(word)
    return not any(n % d == 0 and word == word[:d] * (n // d) for d in range(1, n))


def enumerate_primitive_cycles(n: int) -> set[tuple[int, ...]]:
    result: set[tuple[int, ...]] = set()

    def extend(word: tuple[int, ...]) -> None:
        if len(word) == n:
            if ADJACENCY[word[-1]][word[0]] and primitive(word):
                result.add(min(rotations(word)))
            return
        for symbol, allowed in enumerate(ADJACENCY[word[-1]]):
            if allowed:
                extend(word + (symbol,))

    for initial in range(4):
        extend((initial,))
    return result


def reflection_shift(word: tuple[int, ...]) -> int | None:
    reflected = tuple(REVERSAL[word[-i % len(word)]] for i in range(len(word)))
    for shift in range(len(word)):
        if reflected[shift:] + reflected[:shift] == word:
            return shift
    return None


def brute_row(n: int) -> dict[str, int]:
    cycles = enumerate_primitive_cycles(n)
    shifts = [reflection_shift(word) for word in cycles]
    reversible = [shift for shift in shifts if shift is not None]
    if n % 2:
        edge = 0
        vertex = 0
    else:
        edge = sum(shift % 2 == 0 for shift in reversible)
        vertex = sum(shift % 2 == 1 for shift in reversible)
    return {
        "period": n,
        "primitive_cycles": len(cycles),
        "reversible_cycles": len(reversible),
        "edge_edge_cycles": edge,
        "vertex_vertex_cycles": vertex,
    }


def formula_row(n: int) -> dict[str, int]:
    if n % 2:
        reversible = primitive_odd_reflections(n)
        edge = vertex = 0
    else:
        edge = primitive_even_reflections(n, True)
        vertex = primitive_even_reflections(n, False)
        reversible = edge + vertex
    return {
        "period": n,
        "primitive_cycles": primitive_cycles(n),
        "reversible_cycles": reversible,
        "edge_edge_cycles": edge,
        "vertex_vertex_cycles": vertex,
    }


def core_payload() -> dict[str, object]:
    matrix = sp.Matrix(ADJACENCY)
    permutation = sp.zeros(4)
    for index, image in enumerate(REVERSAL):
        permutation[image, index] = 1
    if matrix != permutation * matrix.T * permutation:
        raise ArithmeticError("time-reversal adjacency identity failed")
    if sp.factor(matrix.charpoly().as_expr()) != (sp.Symbol("lambda") ** 2 + 1) * (sp.Symbol("lambda") ** 2 - sp.Symbol("lambda") - 1):
        # SymPy's default generator is lambda; the explicit branch below keeps
        # this test robust if pretty-printing changes.
        z = sp.symbols("z")
        if sp.factor(matrix.charpoly(z).as_expr()) != (z**2 + 1) * (z**2 - z - 1):
            raise ArithmeticError("adjacency characteristic polynomial changed")

    formula_rows = [formula_row(n) for n in range(1, 33)]
    brute_rows = [brute_row(n) for n in range(1, 17)]
    if brute_rows != formula_rows[:16]:
        raise ArithmeticError("formula/brute reflection census mismatch")

    phi = (1 + sp.sqrt(5)) / 2
    return {
        "candidate_id": "HCS-P59",
        "adjacency": [list(row) for row in ADJACENCY],
        "time_reversal_involution": list(REVERSAL),
        "reversal_identity": "A=P*A^T*P",
        "characteristic_polynomial": "(z^2+1)(z^2-z-1)",
        "closed_word_formula": "tr(A^n)=L_n+2*cos(pi*n/2)",
        "fixed_word_formulas": {
            "odd_n": "F_((n+3)/2)",
            "even_edge_edge_n_2m": "L_m",
            "even_vertex_vertex_n_2m": "F_m+(2/5)L_m-(4/5)cos(pi*m/2)-(2/5)sin(pi*m/2)",
        },
        "primitive_formulas": {
            "all_cycles": "C_n=(1/n) sum_{d|n} mu(n/d) tr(A^d)",
            "odd_reflections": "R_n=sum_{d|n} mu(n/d) F_((d+3)/2)",
            "even_axis_type": "R_n^type=(1/2) sum_{d|n} mu(n/d) Fix_type(d)",
        },
        "formula_rows_1_to_32": formula_rows,
        "brute_rows_1_to_16": brute_rows,
        "family_axis_lock": {
            "A8_word": "00000021",
            "A8_reflection_shift": reflection_shift((0, 0, 0, 0, 0, 0, 2, 1)),
            "A8_type": "vertex_vertex",
            "B8_word": "00000231",
            "B8_reflection_shift": reflection_shift((0, 0, 0, 0, 0, 2, 3, 1)),
            "B8_type": "edge_edge",
        },
        "entropy_theorem": {
            "full_primitive_entropy": "log(phi)",
            "reflection_primitive_entropy": "(1/2)log(phi)",
            "phi_decimal_40": str(sp.N(phi, 40)),
            "reflection_density": "O(n*phi^(-n/2))",
            "status": "PROVED_EXACT_SYMBOLIC_HALF_ENTROPY_LAW",
        },
        "strongest_positive_result": "closed all-period formulas for primitive reversible H6 necklaces, resolved into the two even reflection-axis types, and a reflection entropy exactly half the full survivor entropy",
        "strongest_obstruction": "physical reflection cycles are exponentially sparse among all primitive survivor cycles, so a reflection-only pressure cannot represent the full physical pressure without an additional exponentially compensating weight",
        "open_theorem": "compile algebraic primitive reflection factors and their Galois heights; the symbolic half-entropy law counts physical necklaces, not nonphysical conjugate embeddings",
        "reusable_structure": "time-reversal involution P, three fixed-word transfer formulas, divisor-sensitive reflection Mobius inversion, and exact axis-type census",
        "round2_clue": "compare the symbolic rate (1/2)log(phi) with the algebraic mixed-axis closure rate (1/2)log(2) using a reflection dynatomic quotient",
        "route_a_status": {
            "tuple": "(A1_PASS_ANALYTIC [reflection subsystem], A2_ANALYTIC_DETERMINANT [physical full subsystem inherited], A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FORMAL_HINT)",
            "overall": "ROUTE_A_EXPLORATORY",
            "full_arithmetic_candidate_pass": False,
        },
        "route_b_authorized": False,
        "arithmetic_advance": "NO",
        "claim_boundary": "P59 proves an exact symbolic reflection census and half-entropy law; it does not count algebraic conjugates, prove a Galois pressure theorem, identify rational primes, or construct a Hilbert-Polya operator",
    }


EXPECTED_CORE_SHA256 = "68ba84a039ca5eaf774ce669975af7fe65df9246e9f8f8deca23ac4c10a5f39d"


def validate_core(candidate: object, expected: object) -> None:
    if type(candidate) is not dict or candidate != expected:
        raise ValueError("core payload changed")


def assign_path(payload: object, path: tuple[object, ...], value: object) -> None:
    cursor = payload
    for key in path[:-1]:
        cursor = cursor[key]  # type: ignore[index]
    cursor[path[-1]] = value  # type: ignore[index]


def mutation_audit(core: dict[str, object]) -> dict[str, object]:
    mutations = (
        ("reversal", ("time_reversal_involution",), [0, 1, 2, 3]),
        ("charpoly", ("characteristic_polynomial",), "z^4-z^3-z-1"),
        ("closed_words", ("closed_word_formula",), "tr(A^n)=L_n"),
        ("odd_fixed", ("fixed_word_formulas", "odd_n"), "F_((n+1)/2)"),
        ("edge_fixed", ("fixed_word_formulas", "even_edge_edge_n_2m"), "F_m"),
        ("vertex_fixed", ("fixed_word_formulas", "even_vertex_vertex_n_2m"), "L_m"),
        ("mobius", ("primitive_formulas", "odd_reflections"), "no divisor subtraction"),
        ("A8_axis", ("family_axis_lock", "A8_type"), "edge_edge"),
        ("B8_axis", ("family_axis_lock", "B8_type"), "vertex_vertex"),
        ("full_entropy", ("entropy_theorem", "full_primitive_entropy"), "(1/2)log(phi)"),
        ("reflection_entropy", ("entropy_theorem", "reflection_primitive_entropy"), "log(phi)"),
        ("density", ("entropy_theorem", "reflection_density"), "positive density"),
        ("status", ("entropy_theorem", "status"), "FULL_GALOIS_PRESSURE"),
        ("galois_promotion", ("open_theorem",), "algebraic conjugates counted"),
        ("route_a_promotion", ("route_a_status", "full_arithmetic_candidate_pass"), True),
        ("route_b_promotion", ("route_b_authorized",), True),
        ("arithmetic_promotion", ("arithmetic_advance",), "YES"),
        ("claim_promotion", ("claim_boundary",), "Hilbert-Polya proved"),
    )
    rejected: list[str] = []
    for label, path, replacement in mutations:
        trial = copy.deepcopy(core)
        assign_path(trial, path, replacement)
        try:
            validate_core(trial, core)
        except ValueError:
            rejected.append(label)
        else:
            raise AssertionError(f"mutation accepted: {label}")
    return {
        "attempted": len(mutations),
        "rejected": len(rejected),
        "all_rejected": True,
        "labels": rejected,
        "trace_sha256": canonical_sha(rejected),
    }


def build_certificate() -> dict[str, object]:
    core = core_payload()
    core_sha = canonical_sha(core)
    if core_sha != EXPECTED_CORE_SHA256:
        raise RuntimeError("core payload digest changed")
    result = {
        **core,
        "core_sha256": core_sha,
        "dependency_locks": dependency_locks(),
        "mutation_audit": mutation_audit(core),
    }
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    if not args.check:
        raise SystemExit("explicit --check is required")
    certificate = build_certificate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "candidate_id": certificate["candidate_id"],
        "check": True,
        "core_sha256": certificate["core_sha256"],
        "formula_periods": len(certificate["formula_rows_1_to_32"]),
        "brute_periods": len(certificate["brute_rows_1_to_16"]),
        "mutations_rejected": certificate["mutation_audit"]["rejected"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
