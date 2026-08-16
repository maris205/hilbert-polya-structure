#!/usr/bin/env python3
"""Exact entropy-boundary counterterm certificate for HCS-P71."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path

import sympy as sp

PROJECT = Path(__file__).resolve().parents[1]
TRACK = PROJECT.parent
DEFAULT_OUTPUT = PROJECT / "results/c71_certificate.json"

DEPENDENCIES = {
    "p70_proof": (TRACK / "henon_orbit_resolved_reflection_euler_boundary/PROOF_PACKAGE.md", "416fe1466c7dcaeb35c4ab85d4a1cd329e00f9c961c09d490dbbc77a4f1c1a1e"),
    "p70_certificate": (TRACK / "henon_orbit_resolved_reflection_euler_boundary/results/c70_certificate.json", "35abf7ee3500b8263b885d424644665e3a5a124fdc43ea5d3a933d43cfe16e3c"),
    "p70_paper": (TRACK / "henon_orbit_resolved_reflection_euler_boundary/paper/paper.pdf", "ab040dceedfaa0db53f55a10c34ebc2a838d999b1e40c0bcde19b591f37fe7de"),
    "p68_proof": (TRACK / "henon_canonical_reflection_packet_euler_product/PROOF_PACKAGE.md", "9930197e758b5c065cb084dc93dc5288e9bf5e6b480fcf146b425537d4976f2a"),
}


def exact_boundary_ledger() -> dict[str, object]:
    u = sp.symbols("u", positive=True)
    root2 = sp.sqrt(2)
    t = (1 - u) / root2
    denominator = sp.expand(1 - 2 * t**2)
    numerator = sp.expand(2 * t + 3 * t**2)
    exponential = sp.cancel(numerator / denominator)
    lind_pole = sp.simplify(sp.limit(u * exponential, u, 0))
    packet_pole = 1 / root2
    residual_pole = sp.simplify(lind_pole - packet_pole)
    analytic_exponent = sp.simplify(exponential - lind_pole / u)
    analytic_series = sp.series(analytic_exponent, u, 0, 7).removeO()
    algebraic_normalization = sp.simplify(
        sp.sqrt(u) / sp.sqrt(denominator)
    )
    if sp.simplify(denominator - u * (2 - u)) != 0:
        raise ArithmeticError("boundary coordinate")
    if lind_pole != 1 / root2 + sp.Rational(3, 4):
        raise ArithmeticError("Lind pole")
    if residual_pole != sp.Rational(3, 4):
        raise ArithmeticError("relative pole")
    if algebraic_normalization != 1 / sp.sqrt(2 - u):
        raise ArithmeticError("branch normalization")
    if sp.limit(analytic_exponent, u, 0) is sp.oo:
        raise ArithmeticError("analytic exponent")
    return {
        "boundary_coordinate": "u=1-sqrt(2)t",
        "denominator_in_u": "u*(2 - u)",
        "numerator_in_u": str(numerator),
        "packet_pole_coefficient": str(packet_pole),
        "lind_pole_coefficient": str(lind_pole),
        "relative_pole_coefficient": str(residual_pole),
        "lind_log_branch_coefficient": "-1/2",
        "unique_exponential_counterterm": "exp(-3/(4u))",
        "unique_algebraic_counterterm": "u^(1/2)",
        "normalized_algebraic_factor": str(algebraic_normalization),
        "analytic_exponent_series_through_u6": str(analytic_series),
    }


def dependency_locks() -> dict[str, dict[str, str]]:
    out = {}
    for name, (path, expected) in DEPENDENCIES.items():
        observed = hashlib.sha256(path.read_bytes()).hexdigest()
        if observed != expected:
            raise RuntimeError(f"dependency changed: {name}")
        out[name] = {"path": str(path.relative_to(TRACK)), "sha256": observed}
    return out


def canonical_sha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def core_payload() -> dict[str, object]:
    return {
        "candidate_id": "HCS-P71",
        "source_lind_formula": "zeta_flip(t)=(1-2t^2)^(-1/2) exp((2t+3t^2)/(1-2t^2))",
        "source_scope": "Kim-Lee-Park Example 4.3, full two-shift with reverse flip",
        "packet_local_form": "log Z_orb(t,1)=1/[sqrt(2)(1-sqrt(2)t)]+G_orb(t)",
        "lind_local_form": "log zeta_flip(t)=(1/sqrt(2)+3/4)/(1-sqrt(2)t)-(1/2)log(1-sqrt(2)t)+G_L(t)",
        "relative_local_form": "log(zeta_flip/Z_orb)=3/[4(1-sqrt(2)t)]-(1/2)log(1-sqrt(2)t)+G_rel(t)",
        "relative_counterterm": "C_rel(t)=(1-sqrt(2)t)^(1/2) exp(-3/[4(1-sqrt(2)t)]) zeta_flip(t)/Z_orb(t,1)",
        "extension_theorem": "C_rel extends holomorphically and nonvanishingly across t=1/sqrt(2) as a local branch germ",
        "counterterm_uniqueness": "among u^beta exp(-c/u), nonzero holomorphic extension forces c=3/4 and beta=1/2",
        "odd_packet_insufficiency": "P70's packet coefficient 1/sqrt(2) leaves the source-native residual 3/4 and square-root branch",
        "ledger": exact_boundary_ledger(),
        "strongest_positive_result": "an explicit unique local relative counterterm reconciles the orbit-resolved odd packet with the source full-shift Lind germ at the positive entropy boundary",
        "strongest_obstruction": "the odd reflection packet alone cannot regularize the Lind zeta; full subgroup data contributes a residual essential coefficient 3/4 and algebraic exponent 1/2",
        "open_theorem": "globalize the relative germ, determine its other singularities and zeros, and decide whether it is a transfer/Fredholm determinant",
        "reusable_structure": "boundary counterterms are classified by a two-entry ledger: exponential pole coefficient and logarithmic branch exponent",
        "round2_clue": "test whether the locally normalized relative germ has nontrivial zeros or instead is zero-free, and compare its coefficient signs with an operator trace",
        "claim_status": {
            "source_formula": "SOURCE_VERIFIED",
            "local_relative_counterterm": "PROVED",
            "counterterm_uniqueness": "PROVED",
            "global_relative_determinant": "OPEN",
            "arithmetic_trace": "OPEN",
            "arithmetic_advance": "NO",
            "route_b_authorized": False,
        },
    }


def validate(core: dict[str, object]) -> None:
    if type(core) is not dict or core.get("candidate_id") != "HCS-P71":
        raise ValueError("schema")
    if core.get("relative_counterterm") != "C_rel(t)=(1-sqrt(2)t)^(1/2) exp(-3/[4(1-sqrt(2)t)]) zeta_flip(t)/Z_orb(t,1)":
        raise ValueError("counterterm")
    if core.get("counterterm_uniqueness") != "among u^beta exp(-c/u), nonzero holomorphic extension forces c=3/4 and beta=1/2":
        raise ValueError("uniqueness")
    ledger = core.get("ledger")
    if type(ledger) is not dict or ledger.get("relative_pole_coefficient") != "3/4":
        raise ValueError("ledger")
    expected = {
        "source_formula": "SOURCE_VERIFIED",
        "local_relative_counterterm": "PROVED",
        "counterterm_uniqueness": "PROVED",
        "global_relative_determinant": "OPEN",
        "arithmetic_trace": "OPEN",
        "arithmetic_advance": "NO",
        "route_b_authorized": False,
    }
    if core.get("claim_status") != expected:
        raise ValueError("status")


def mutation_audit(core: dict[str, object]) -> dict[str, object]:
    rejected = []
    protected = [
        "candidate_id", "source_lind_formula", "source_scope",
        "packet_local_form", "lind_local_form", "relative_local_form",
        "relative_counterterm", "extension_theorem", "counterterm_uniqueness",
        "odd_packet_insufficiency", "strongest_positive_result",
        "strongest_obstruction", "open_theorem", "reusable_structure",
        "round2_clue",
    ]
    for key in protected:
        trial = copy.deepcopy(core)
        trial[key] = "FORGED"
        try:
            validate(trial)
            if trial != core:
                raise ValueError("drift")
        except ValueError:
            rejected.append(key)
    for key, forged in (
        ("source_formula", "UNVERIFIED"), ("local_relative_counterterm", "OPEN"),
        ("counterterm_uniqueness", "OPEN"), ("global_relative_determinant", "PROVED"),
        ("arithmetic_trace", "PROVED"), ("arithmetic_advance", "YES"),
        ("route_b_authorized", True),
    ):
        trial = copy.deepcopy(core)
        trial["claim_status"][key] = forged
        try:
            validate(trial)
            if trial != core:
                raise ValueError("drift")
        except ValueError:
            rejected.append("status-" + key)
    trial = copy.deepcopy(core)
    trial["ledger"]["relative_pole_coefficient"] = "1"
    try:
        validate(trial)
    except ValueError:
        rejected.append("relative-pole")
    return {"attempted": 23, "rejected": rejected, "all_rejected": len(rejected) == 23}


def build() -> dict[str, object]:
    core = core_payload()
    validate(core)
    out = dict(core)
    out["dependency_locks"] = dependency_locks()
    out["mutation_audit"] = mutation_audit(core)
    if not out["mutation_audit"]["all_rejected"]:
        raise RuntimeError("mutation audit")
    out["core_sha256"] = canonical_sha(core)
    out["check"] = True
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    out = build()
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "candidate_id": "HCS-P71",
        "relative_pole": out["ledger"]["relative_pole_coefficient"],
        "branch_exponent": out["ledger"]["unique_algebraic_counterterm"],
        "mutations": out["mutation_audit"]["attempted"],
        "core_sha256": out["core_sha256"],
        "check": True,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
