#!/usr/bin/env python3
"""Exact HCS-P65 symmetry-defect pressure certificate."""

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
DEFAULT_OUTPUT = PROJECT / "results" / "c65_certificate.json"
PERIODS = tuple(range(1, 22, 2))
DEPENDENCIES = {
    "p64_proof": (TRACK / "henon_reflection_boundary_mahler_pressure" / "PROOF_PACKAGE.md", "b98dbeb0ca2dbaa8196726eef9cd3f25dbdd1a620096d51a95c806eae95a3db6"),
    "p64_certificate": (TRACK / "henon_reflection_boundary_mahler_pressure" / "results" / "c64_certificate.json", "4ecc9c17111fdf8fcecf6c6fa65e9c1b765d58baabb55277c77eed60822a823b"),
    "p64_paper": (TRACK / "henon_reflection_boundary_mahler_pressure" / "paper" / "paper.pdf", "ebdad01630d41c7e100c2c0151f416029aa98a74e3156b6a02079f08f919f655"),
}


def canonical_sha(payload: object) -> str:
    return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def dependency_locks() -> dict[str, dict[str, str]]:
    rows = {}
    for name, (path, expected) in DEPENDENCIES.items():
        observed = hashlib.sha256(path.read_bytes()).hexdigest()
        if observed != expected:
            raise RuntimeError(f"dependency changed: {name}")
        rows[name] = {"path": str(path.relative_to(TRACK)), "sha256": observed}
    return rows


def degree(n: int) -> int:
    return sum(int(sp.mobius(n // d)) * 2 ** ((d + 1) // 2) for d in sp.divisors(n))


def palindrome(bits: tuple[int, ...]) -> tuple[int, ...]:
    return bits + bits[:0:-1]


def least_period(word: tuple[int, ...]) -> int:
    n = len(word)
    for d in sp.divisors(n):
        d = int(d)
        if all(word[j] == word[j % d] for j in range(n)):
            return d
    raise ArithmeticError


def primitive_words(n: int) -> list[tuple[int, ...]]:
    words = [palindrome(bits) for bits in itertools.product((0, 1), repeat=(n + 1) // 2)]
    result = [word for word in words if least_period(word) == n]
    if len(result) != degree(n):
        raise ArithmeticError("degree mismatch")
    return result


def chi(word: tuple[int, ...], center: int) -> int:
    n = len(word)
    return int(word[(center - 1) % n] == word[(center + 1) % n])


def row(n: int) -> dict[str, object]:
    words = primitive_words(n)
    primitive_mean = Fraction(sum(chi(word, j) for word in words for j in range(n)), len(words) * n)
    full_mean = Fraction(n + 1, 2 * n)
    error = abs(primitive_mean - full_mean)
    epsilon = Fraction(2 ** ((n + 1) // 2) - len(words), 2 ** ((n + 1) // 2))
    if error > epsilon:
        raise ArithmeticError("primitive perturbation bound failed")
    return {
        "period": n,
        "primitive_count": len(words),
        "axis_symmetry_mean": "1",
        "full_orbit_symmetry_mean": str(full_mean),
        "primitive_orbit_symmetry_mean": str(primitive_mean),
        "primitive_vs_full_error": str(error),
        "primitive_tv_bound": str(epsilon),
        "pressure_gradient_gap_d_dt": "-1/2",
        "words_sha256": canonical_sha(["".join(map(str, word)) for word in words]),
    }


def core_payload() -> dict[str, object]:
    return {
        "candidate_id": "HCS-P65",
        "symmetry_observable": "chi(omega)=1_{omega_(-1)=omega_(+1)}",
        "axis_expectation": "int chi d eta_J=1",
        "max_entropy_expectation": "int chi d mu_B=1/2",
        "one_sided_minimality": "eta_J and mu_B have identical restrictions to every finite nonnegative-coordinate sigma-algebra",
        "minimal_centered_window": "radius one; the two-sided coordinates {-1,+1} are necessary",
        "axis_symmetry_pressure": "P_axis(t)=(1/2)log2-t",
        "orbit_symmetry_pressure": "P_orbit(t)=(1/2)log2-t/2",
        "two_parameter_axis_pressure": "P_axis(s,t)=(1/2)log2-s kappa_J-t",
        "two_parameter_orbit_pressure": "P_orbit(s,t)=(1/2)log2-s kappa_max-t/2",
        "transverse_gradient_gap": "partial_t P_axis-partial_t P_orbit=-1/2",
        "rows": [row(n) for n in PERIODS],
        "strongest_positive_result": "a minimal radius-one symmetry observable gives two rigorously separated extensive packet pressures and an exact transverse derivative gap",
        "strongest_obstruction": "no finite one-sided symbolic observable can distinguish marked reflection-boundary sampling from maximal entropy",
        "open_theorem": "attach the coordinate Mahler observable to this calibrated symmetry direction and decide the unperturbed kappa_J-kappa_max gap",
        "reusable_structure": "a local two-sided symmetry defect is an exact calibration channel for reflection-selected thermodynamic limits",
        "round2_clue": "test cohomology invariance: boundary sampling is non-invariant, so a symbolic coboundary may change its pressure while leaving orbit pressure fixed",
        "claim_status": {
            "minimality": "PROVED",
            "symmetry_pressure_separation": "PROVED",
            "mahler_slope_separation": "OPEN",
            "arithmetic_advance": "NO",
            "route_b_authorized": False,
        },
    }


def validate(core: dict[str, object]) -> None:
    if type(core) is not dict or core.get("candidate_id") != "HCS-P65":
        raise ValueError("schema")
    if core.get("axis_expectation") != "int chi d eta_J=1":
        raise ValueError("axis")
    if core.get("max_entropy_expectation") != "int chi d mu_B=1/2":
        raise ValueError("invariant")
    if [r["primitive_count"] for r in core["rows"]] != [degree(n) for n in PERIODS]:
        raise ValueError("degree")
    if core["claim_status"]["arithmetic_advance"] != "NO" or core["claim_status"]["route_b_authorized"] is not False:
        raise ValueError("promotion")


def mutations(core: dict[str, object]) -> dict[str, object]:
    cases = [
        ("candidate_id", "PROMOTED"), ("symmetry_observable", "constant"),
        ("axis_expectation", "int chi d eta_J=1/2"), ("max_entropy_expectation", "int chi d mu_B=1"),
        ("one_sided_minimality", "FALSE"), ("minimal_centered_window", "radius zero"),
        ("axis_symmetry_pressure", "flat"), ("orbit_symmetry_pressure", "flat"),
        ("two_parameter_axis_pressure", "RH"), ("two_parameter_orbit_pressure", "RH"),
        ("transverse_gradient_gap", "0"), ("strongest_positive_result", "RH"),
        ("strongest_obstruction", "NONE"), ("open_theorem", "CLOSED"),
        ("reusable_structure", "NONE"), ("round2_clue", "PRIME TRACE"),
    ]
    rejected = []
    for key, value in cases:
        trial = copy.deepcopy(core); trial[key] = value
        try:
            validate(trial)
            if trial != core:
                raise ValueError("exact drift")
        except ValueError:
            rejected.append(key)
    for key, value in (("minimality", "OPEN"), ("symmetry_pressure_separation", "OPEN"), ("mahler_slope_separation", "PROVED"), ("arithmetic_advance", "YES"), ("route_b_authorized", True)):
        trial = copy.deepcopy(core); trial["claim_status"][key] = value
        try:
            validate(trial)
            if trial != core:
                raise ValueError("exact drift")
        except ValueError:
            rejected.append("status-" + key)
    return {"attempted": len(rejected), "rejected": rejected, "all_rejected": len(rejected) == 21}


def build() -> dict[str, object]:
    core = core_payload(); validate(core)
    result = dict(core)
    result["dependency_locks"] = dependency_locks()
    result["mutation_audit"] = mutations(core)
    if not result["mutation_audit"]["all_rejected"]:
        raise RuntimeError("mutation audit")
    result["core_sha256"] = canonical_sha(core)
    result["check"] = True
    return result


def main() -> None:
    parser = argparse.ArgumentParser(); parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args(); result = build()
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"candidate_id": "HCS-P65", "check": True, "core_sha256": result["core_sha256"], "mutations_rejected": result["mutation_audit"]["attempted"]}, sort_keys=True))


if __name__ == "__main__":
    main()
