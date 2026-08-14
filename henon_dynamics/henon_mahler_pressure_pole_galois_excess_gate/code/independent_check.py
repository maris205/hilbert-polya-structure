#!/usr/bin/env python3
"""Independent checker for the HCS-P54 certificate.

This module deliberately does not import ``c54_pressure_pole``.  It rebuilds
the three exact trace-root heights, dependency hashes, residue interval, core
digest, and claim firewall from separately written formulas.
"""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
from typing import Any, Callable

import mpmath as mp
import sympy as sp


PROJECT = Path(__file__).resolve().parents[1]
TRACK = PROJECT.parent
CERTIFICATE = PROJECT / "results" / "c54_certificate.json"

EXPECTED_DEPENDENCIES = {
    "p45_readme": ("henon_pressure_normalized_prime_orbit_bridge/README.md", "45cb4c5b8c735bfb5c3a497cfecef21fc81140b3c77f56c866249df8715e5ba1"),
    "p45_certificate": ("henon_pressure_normalized_prime_orbit_bridge/results/c45_certificate.json", "962e0f6aca53b8e1c8786caa291af7bb318efd631b86b7f70702c1d2bea603f7"),
    "p48_certificate": ("henon_pressure_label_six_exponentials_obstruction/results/c48_certificate.json", "7134167226aa6bd22596675bf21826b8303a2a731f087d6ad7405d7137a51234"),
    "p53_readme": ("henon_pressure_weighted_all_orbit_abel_law/README.md", "b719c290b278b874d6180ab14479a5adb743f8c9b43fc75dac55c778516586b0"),
    "p53_proof": ("henon_pressure_weighted_all_orbit_abel_law/PROOF_PACKAGE.md", "0270d20fb8b4438bd31ba504c7a9fd10b9dc49aef39620091fe66894e770276b"),
    "p53_certificate": ("henon_pressure_weighted_all_orbit_abel_law/results/c53_certificate.json", "52b1b502cd0283e01ee6de9e58a2bddbe7d7dff5538ed652cca905226c96b459"),
    "p31_theorem": ("henon_bowen_pressure_gate/THEOREM_PACKAGE.md", "5f2ae3d86094a80c89822f91af935ef09efa3893cbc50326f56174f154f721ee"),
    "instability_roof_readme": ("henon_instability_roof_zeta/README.md", "c2a63ba68fe4d7092d5304008ab5745172269c23bbc30faf93f1423ae96f798e"),
}

TOP_LEVEL_KEYS = {
    "arithmetic_advance",
    "candidate_id",
    "claim_boundary",
    "claim_status",
    "conditional_holder_completion",
    "core_sha256",
    "dependency_locks",
    "exact_orbits",
    "excess_abscissa_trichotomy",
    "finite_log_derivative_fixture",
    "mahler_decomposition",
    "open_theorem",
    "physical_pressure_pole",
    "route_b_authorized",
    "scalar_roof_cohomology_obstruction",
    "source_object",
    "source_theorem_map",
    "strongest_obstruction",
    "strongest_positive_result",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_sha(payload: object) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def pair_log(trace: sp.Expr) -> mp.mpf:
    value = mp.mpf(str(sp.N(trace, 90)))
    return mp.acosh(abs(value) / 2) if abs(value) > 2 else mp.mpf("0")


def expected_orbits() -> dict[str, dict[str, mp.mpf]]:
    roots = {
        "period_1": ((2 + 2 * sp.sqrt(7), 2 - 2 * sp.sqrt(7)), 0),
        "period_3": ((-38 - 42 * sp.sqrt(5), -38 + 42 * sp.sqrt(5)), 0),
        "period_4": ((sp.Integer(578),), 0),
    }
    result = {}
    for label, (trace_roots, physical_index) in roots.items():
        values = [pair_log(root) for root in trace_roots]
        result[label] = {
            "ell": values[physical_index],
            "height": mp.fsum(values),
            "excess": mp.fsum(values) - values[physical_index],
        }
    return result


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def validate(payload: dict[str, Any], *, verify_files: bool = True) -> None:
    require(type(payload) is dict, "certificate must be an exact dict")
    require(set(payload) == TOP_LEVEL_KEYS, "top-level schema changed")
    require(payload["candidate_id"] == "HCS-P54", "candidate id changed")
    require(payload["claim_status"] == "PROVED_PLUS_CONDITIONAL_THEOREM", "claim status changed")
    require(payload["arithmetic_advance"] == "PARTIAL_ANALYTIC_STRUCTURE_ONLY", "arithmetic status changed")
    require(payload["route_b_authorized"] is False, "Route B promotion detected")

    core = {key: value for key, value in payload.items() if key not in {"core_sha256", "dependency_locks"}}
    require(payload["core_sha256"] == canonical_sha(core), "core digest mismatch")

    decomposition = payload["mahler_decomposition"]
    require(decomposition["identity"] == "H_gamma=ell_gamma+E_gamma", "decomposition changed")
    require(decomposition["galois_excess_nonnegative"] is True, "excess sign changed")

    pole = payload["physical_pressure_pole"]
    require(pole["meromorphic_germ_at_s_1"] is True, "physical germ deleted")
    require(pole["simple_pole"] is True, "physical pole deleted")
    require(pole["residue"] == "3/(pi^2*h_star)", "physical residue changed")
    h_low = mp.mpf("0.277980")
    h_high = mp.mpf("0.277987")
    expected_low = 3 / (mp.pi**2 * h_high)
    expected_high = 3 / (mp.pi**2 * h_low)
    observed_interval = pole["residue_certificate"]["residue_open_interval"]
    left_text, right_text = observed_interval.strip("()").split(",")
    require(abs(mp.mpf(left_text) - expected_low) < mp.mpf("1e-45"), "residue lower endpoint changed")
    require(abs(mp.mpf(right_text) - expected_high) < mp.mpf("1e-45"), "residue upper endpoint changed")

    conditional = payload["conditional_holder_completion"]
    require(conditional["status"] == "CONDITIONAL_THEOREM", "conditional theorem promoted")
    require("Holder psi" in conditional["hypothesis"], "Holder hypothesis deleted")

    expected = expected_orbits()
    require(set(payload["exact_orbits"]) == set(expected), "orbit labels changed")
    for label, values in expected.items():
        row = payload["exact_orbits"][label]
        for field, expected_value in (
            ("physical_instability_length", values["ell"]),
            ("mahler_spectral_height", values["height"]),
            ("galois_excess", values["excess"]),
        ):
            require(abs(mp.mpf(row[field]) - expected_value) < mp.mpf("1e-50"), f"{label} {field} changed")
    require(payload["exact_orbits"]["period_1"]["excess_positive"] is True, "period-one witness changed")
    require(payload["exact_orbits"]["period_3"]["excess_positive"] is True, "period-three witness changed")
    require(payload["exact_orbits"]["period_4"]["excess_zero"] is True, "period-four witness changed")

    obstruction = payload["scalar_roof_cohomology_obstruction"]
    require(obstruction["period_four_forces_c"] == "1.0", "forced scalar changed")
    require(mp.mpf(obstruction["period_one_residual"]) > 1, "cohomology contradiction vanished")

    fixtures = payload["finite_log_derivative_fixture"]["fixtures"]
    require(len(fixtures) == 3, "finite Euler fixture count changed")
    for row in fixtures:
        require(mp.mpf(row["identity_abs_error"]) < mp.mpf("1e-55"), "Euler identity error too large")

    require("no continuation" in payload["claim_boundary"], "claim firewall weakened")
    require("Holder" in payload["open_theorem"], "open Holder theorem deleted")

    locks = payload["dependency_locks"]
    require(set(locks) == set(EXPECTED_DEPENDENCIES), "dependency schema changed")
    for label, (relative, expected_hash) in EXPECTED_DEPENDENCIES.items():
        require(locks[label] == {"path": relative, "sha256": expected_hash}, f"dependency row changed: {label}")
        if verify_files:
            require(sha256(TRACK / relative) == expected_hash, f"dependency bytes changed: {label}")


def mutation_suite(payload: dict[str, Any]) -> int:
    mutations: list[tuple[str, Callable[[dict[str, Any]], None]]] = [
        ("candidate", lambda x: x.__setitem__("candidate_id", "HCS-P54-PROMOTED")),
        ("route_b", lambda x: x.__setitem__("route_b_authorized", True)),
        ("status", lambda x: x.__setitem__("arithmetic_advance", "HILBERT_POLYA_REALIZATION")),
        ("excess_sign", lambda x: x["mahler_decomposition"].__setitem__("galois_excess_nonnegative", False)),
        ("pole", lambda x: x["physical_pressure_pole"].__setitem__("simple_pole", False)),
        ("residue", lambda x: x["physical_pressure_pole"].__setitem__("residue", "1")),
        ("conditional", lambda x: x["conditional_holder_completion"].__setitem__("status", "PROVED")),
        ("period_one", lambda x: x["exact_orbits"]["period_1"].__setitem__("galois_excess", "0")),
        ("period_four", lambda x: x["exact_orbits"]["period_4"].__setitem__("excess_zero", False)),
        ("cohomology", lambda x: x["scalar_roof_cohomology_obstruction"].__setitem__("period_four_forces_c", "2.0")),
        ("claim", lambda x: x.__setitem__("claim_boundary", "full completed xi determinant proved")),
        ("dependency", lambda x: x["dependency_locks"]["p53_proof"].__setitem__("sha256", "0" * 64)),
    ]
    rejected = 0
    for label, mutate in mutations:
        candidate = copy.deepcopy(payload)
        mutate(candidate)
        try:
            validate(candidate, verify_files=False)
        except RuntimeError:
            rejected += 1
        else:
            raise RuntimeError(f"mutation was accepted: {label}")
    return rejected


def main() -> int:
    mp.mp.dps = 90
    payload = json.loads(CERTIFICATE.read_text())
    validate(payload)
    rejected = mutation_suite(payload)
    print(
        json.dumps(
            {
                "candidate_id": "HCS-P54",
                "certificate_core_sha256": payload["core_sha256"],
                "dependency_hashes_recomputed": True,
                "dependency_lock_count": len(payload["dependency_locks"]),
                "exact_orbits_checked": len(payload["exact_orbits"]),
                "mutations_rejected": rejected,
                "status": "PASS",
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
