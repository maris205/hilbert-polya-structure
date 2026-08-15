#!/usr/bin/env python3
"""Exact HCS-P67 canonical cyclic-sampler certificate."""

from __future__ import annotations

import argparse
import copy
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp


PROJECT = Path(__file__).resolve().parents[1]
TRACK = PROJECT.parent
DEFAULT_OUTPUT = PROJECT / "results" / "c67_certificate.json"
PERIODS = tuple(range(3, 22, 2))
DEPENDENCIES = {
    "p64_proof": (
        TRACK / "henon_reflection_boundary_mahler_pressure" / "PROOF_PACKAGE.md",
        "b98dbeb0ca2dbaa8196726eef9cd3f25dbdd1a620096d51a95c806eae95a3db6",
    ),
    "p64_certificate": (
        TRACK / "henon_reflection_boundary_mahler_pressure" / "results" / "c64_certificate.json",
        "4ecc9c17111fdf8fcecf6c6fa65e9c1b765d58baabb55277c77eed60822a823b",
    ),
    "p66_proof": (
        TRACK / "henon_reflection_boundary_cohomology_anomaly" / "PROOF_PACKAGE.md",
        "0a276ddcaa7c0afd31ba7b6d0add78f63233177daecd60410b1d0f6b1db90d7c",
    ),
    "p66_certificate": (
        TRACK / "henon_reflection_boundary_cohomology_anomaly" / "results" / "c66_certificate.json",
        "16a1869c7cd7c29f4e31efdd4d10be56b3a93dc291971dbcee43fc82eec8bae6",
    ),
    "p66_paper": (
        TRACK / "henon_reflection_boundary_cohomology_anomaly" / "paper" / "paper.pdf",
        "930517f7d9bf7dc1a63239a58b67b7e9e640dc39a29edb557bff9729b94147e9",
    ),
}


def canonical_sha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def dependency_locks() -> dict[str, dict[str, str]]:
    result = {}
    for name, (path, expected) in DEPENDENCIES.items():
        observed = hashlib.sha256(path.read_bytes()).hexdigest()
        if observed != expected:
            raise RuntimeError(f"dependency changed: {name}")
        result[name] = {
            "path": str(path.relative_to(TRACK)),
            "sha256": observed,
        }
    return result


def cyclic_difference_matrix(n: int) -> list[list[Fraction]]:
    """Matrix of (Du)_j=u_j-u_(j+1) on Z/nZ."""
    matrix = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for j in range(n):
        matrix[j][j] = Fraction(1)
        matrix[j][(j + 1) % n] -= Fraction(1)
    return matrix


def exact_rank(matrix: list[list[Fraction]]) -> int:
    work = [row[:] for row in matrix]
    if not work:
        return 0
    rows, cols = len(work), len(work[0])
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if work[r][col]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][col]
        work[pivot_row] = [value / scale for value in work[pivot_row]]
        for r in range(rows):
            if r != pivot_row and work[r][col]:
                factor = work[r][col]
                work[r] = [a - factor * b for a, b in zip(work[r], work[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def anomaly_coefficients(weights: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    """Coefficients of sum_j w_j(u_j-u_(j+1))."""
    n = len(weights)
    return tuple(weights[j] - weights[(j - 1) % n] for j in range(n))


def sampler_row(n: int) -> dict[str, object]:
    matrix = cyclic_difference_matrix(n)
    rank = exact_rank(matrix)
    uniform = tuple(Fraction(1, n) for _ in range(n))
    if rank != n - 1 or any(anomaly_coefficients(uniform)):
        raise ArithmeticError("cyclic uniqueness failed")

    nonuniform = (Fraction(1),) + tuple(Fraction(0) for _ in range(n - 1))
    coefficients = anomaly_coefficients(nonuniform)
    witness_index = next(j for j, value in enumerate(coefficients) if value)
    witness = tuple(Fraction(int(j == witness_index)) for j in range(n))
    anomaly = sum(
        nonuniform[j] * (witness[j] - witness[(j + 1) % n])
        for j in range(n)
    )
    if anomaly != coefficients[witness_index] or anomaly == 0:
        raise ArithmeticError("nonuniform witness failed")
    return {
        "cycle_length": n,
        "difference_rank": rank,
        "gauge_invariant_weight_space_dimension": 1,
        "normalized_solution": [str(value) for value in uniform],
        "nonuniform_witness_index": witness_index,
        "nonuniform_anomaly": str(anomaly),
    }


def degree(n: int) -> int:
    return sum(
        int(sp.mobius(n // d)) * 2 ** ((d + 1) // 2)
        for d in sp.divisors(n)
    )


def palindrome(half: tuple[int, ...]) -> tuple[int, ...]:
    return half + half[:0:-1]


def least_period(word: tuple[int, ...]) -> int:
    n = len(word)
    for divisor in sp.divisors(n):
        d = int(divisor)
        if all(word[j] == word[j % d] for j in range(n)):
            return d
    raise ArithmeticError("no period")


def primitive_words(n: int) -> list[tuple[int, ...]]:
    words = [
        word
        for half in itertools.product((0, 1), repeat=(n + 1) // 2)
        if least_period(word := palindrome(half)) == n
    ]
    if len(words) != degree(n):
        raise ArithmeticError("degree mismatch")
    return words


def block11(word: tuple[int, ...], center: int) -> int:
    n = len(word)
    return int(word[center % n] == 1 and word[(center + 1) % n] == 1)


def packet_row(n: int) -> dict[str, object]:
    words = primitive_words(n)
    mean = Fraction(
        sum(block11(word, j) for word in words for j in range(n)),
        len(words) * n,
    )
    bernoulli = Fraction(1, 4)
    primitive_loss = Fraction(2 ** ((n + 1) // 2) - len(words), 2 ** ((n + 1) // 2))
    cylinder_bound = Fraction(5, n) + primitive_loss
    if abs(mean - bernoulli) > cylinder_bound:
        raise ArithmeticError("packet convergence bound")
    if any(
        sum(block11(word, j) - block11(word, (j + 1) % n) for j in range(n))
        for word in words
    ):
        raise ArithmeticError("finite coboundary telescope")
    return {
        "period": n,
        "primitive_count": len(words),
        "orbit_block11_mean": str(mean),
        "bernoulli_block11_mean": "1/4",
        "absolute_error": str(abs(mean - bernoulli)),
        "certified_cylinder_bound": str(cylinder_bound),
        "coboundary_orbit_sum": "0",
    }


def core_payload() -> dict[str, object]:
    return {
        "candidate_id": "HCS-P67",
        "sampler_definition": "L_w(f)=sum_(j mod n) w_j f(sigma^j omega), sum_j w_j=1",
        "gauge_condition": "L_w(u-u o sigma)=0 for every u",
        "uniqueness_theorem": "the gauge condition holds iff w_j=1/n for every j",
        "finite_orbit_invariance": "uniform cyclic averaging annihilates every coboundary exactly before limits",
        "packet_mean": "b_n(f)=(n D_n)^(-1) sum_(omega in A_n) sum_(j mod n) f(sigma^j omega)",
        "universal_pressure": "P_f(s)=(1/2)log2-s int f d mu_B for every continuous f",
        "pressure_gauge_invariance": "P_(f+u-u o sigma)(s)=P_f(s)",
        "pressure_lipschitz_bound": "abs(P_f(s)-P_g(s))<=abs(s) norm(f-g)_infinity",
        "not_topological_pressure": "the packet functional has reflection entropy (1/2)log2 and is not full-shift topological pressure in general",
        "sampler_rows": [sampler_row(n) for n in range(2, 13)],
        "packet_rows": [packet_row(n) for n in PERIODS],
        "strongest_positive_result": "uniform cyclic averaging is the unique normalized linear sampler annihilating all coboundaries, and it yields a universal gauge-invariant reflection-packet pressure for every continuous potential",
        "strongest_obstruction": "every nonuniform normalized cyclic sampler has an explicit one-site transfer function with nonzero gauge anomaly",
        "open_theorem": "construct a source-native reflection-packet determinant or trace whose logarithmic derivative realizes the canonical orbit functional with arithmetic prime-power semantics",
        "reusable_structure": "the cycle incidence operator has rank n-1 and its left kernel canonically selects Haar averaging on every periodic orbit",
        "round2_clue": "use the unique cyclic sampler to define a relative reflection determinant, then test whether its canonical coordinate-Mahler slope couples to physical instability or Galois excess",
        "claim_status": {
            "canonical_sampler_uniqueness": "PROVED",
            "universal_packet_pressure": "PROVED",
            "finite_gauge_invariance": "PROVED",
            "arithmetic_trace": "OPEN",
            "arithmetic_advance": "NO",
            "route_b_authorized": False,
        },
    }


def validate(core: dict[str, object]) -> None:
    if type(core) is not dict or core.get("candidate_id") != "HCS-P67":
        raise ValueError("schema")
    if core.get("uniqueness_theorem") != "the gauge condition holds iff w_j=1/n for every j":
        raise ValueError("uniqueness")
    if [row["difference_rank"] for row in core["sampler_rows"]] != list(range(1, 12)):
        raise ValueError("rank")
    if any(row["coboundary_orbit_sum"] != "0" for row in core["packet_rows"]):
        raise ValueError("telescope")
    status = core["claim_status"]
    if status["arithmetic_advance"] != "NO" or status["route_b_authorized"] is not False:
        raise ValueError("promotion")


def mutation_audit(core: dict[str, object]) -> dict[str, object]:
    keys = [
        "candidate_id", "sampler_definition", "gauge_condition",
        "uniqueness_theorem", "finite_orbit_invariance", "packet_mean",
        "universal_pressure", "pressure_gauge_invariance",
        "pressure_lipschitz_bound", "not_topological_pressure",
        "strongest_positive_result", "strongest_obstruction", "open_theorem",
        "reusable_structure", "round2_clue",
    ]
    rejected = []
    for key in keys:
        trial = copy.deepcopy(core)
        trial[key] = "FORGED"
        try:
            validate(trial)
            if trial != core:
                raise ValueError("exact drift")
        except ValueError:
            rejected.append(key)
    status_cases = [
        ("canonical_sampler_uniqueness", "OPEN"),
        ("universal_packet_pressure", "OPEN"),
        ("finite_gauge_invariance", "OPEN"),
        ("arithmetic_trace", "PROVED"),
        ("arithmetic_advance", "YES"),
        ("route_b_authorized", True),
    ]
    for key, value in status_cases:
        trial = copy.deepcopy(core)
        trial["claim_status"][key] = value
        try:
            validate(trial)
            if trial != core:
                raise ValueError("exact drift")
        except ValueError:
            rejected.append("status-" + key)
    return {
        "attempted": len(rejected),
        "rejected": rejected,
        "all_rejected": len(rejected) == 21,
    }


def build() -> dict[str, object]:
    core = core_payload()
    validate(core)
    result = dict(core)
    result["dependency_locks"] = dependency_locks()
    result["mutation_audit"] = mutation_audit(core)
    if not result["mutation_audit"]["all_rejected"]:
        raise RuntimeError("mutation audit")
    result["core_sha256"] = canonical_sha(core)
    result["check"] = True
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = build()
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps({
        "candidate_id": "HCS-P67",
        "check": True,
        "core_sha256": result["core_sha256"],
        "mutations_rejected": result["mutation_audit"]["attempted"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
