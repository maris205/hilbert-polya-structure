#!/usr/bin/env python3
"""Independent exact checker for the HCS-C227 Lorenz certificate.

This file deliberately does not import the producer.
"""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c227_lorenz_evidence.json"
SOURCE_COMMIT = "489672bd36abd3a4f6da92d1446a0af575917959"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"

EXPECTED_MAIN = [
    ("classic_origin", "10", "8/3", "0"),
    ("classic_pitchfork", "10", "8/3", "1"),
    ("classic_stable_wings", "10", "8/3", "20"),
    ("classic_hopf_surface", "10", "8/3", "470/19"),
    ("classic_post_hopf", "10", "8/3", "28"),
    ("no_finite_hopf", "2", "3", "100"),
    ("negative_rho", "3", "1", "-4"),
    ("simple_pre_hopf", "4", "1", "10"),
    ("simple_hopf", "4", "1", "16"),
    ("simple_post_hopf", "4", "1", "20"),
]
EXPECTED_SAMPLES = [
    ("10", "8/3", "28", ["1", "2", "3"]),
    ("2", "3", "100", ["-4", "5", "7"]),
    ("3", "1", "-4", ["2", "-3", "5"]),
    ("4", "1", "16", ["-7/3", "11/4", "-5/2"]),
    ("1/5", "7/4", "3/2", ["9/5", "-2/7", "8/3"]),
]
TOP_KEYS = {
    "schema", "candidate_id", "evaluation_date", "source_commit", "scope_literal", "evaluator",
    "headline", "frozen_object", "theorem", "regression", "exact_identities", "route_a",
    "scope_flags", "citations", "nonclaims", "payload_sha256",
}
ROW_KEYS = {
    "case_id", "sigma", "beta", "rho", "divergence", "energy_center_c",
    "differential_inequality_kappa", "absorbing_floor_beta_c2_over_kappa",
    "origin_quadratic_factor", "origin_stability", "wing_equilibria_exist",
    "wing_amplitude_squared", "wing_characteristic_polynomial", "hurwitz_margin",
    "rho_h", "wing_stability", "hopf_frequency_squared",
}
SAMPLE_KEYS = {"sigma", "beta", "rho", "point", "V", "Vdot_direct", "Vdot_square_ledger"}
SCOPE_KEYS = {
    "uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data",
    "claims_euler_factors", "claims_root_numbers", "claims_automorphy",
    "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b",
}


def q(text: str) -> Fraction:
    return Fraction(text)


def qt(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


class Audit:
    def __init__(self) -> None:
        self.count = 0

    def check(self, condition: bool, message: str) -> None:
        self.count += 1
        if not condition:
            raise AssertionError(message)


def validate(data: dict) -> int:
    a = Audit()
    a.check(set(data) == TOP_KEYS, "unknown or missing top-level key")
    a.check(data["schema"] == "hcs-c227-lorenz63-atlas-v1", "schema")
    a.check(data["candidate_id"] == "HCS-C227", "candidate")
    a.check(data["evaluation_date"] == "2026-08-29", "date")
    a.check(data["source_commit"] == SOURCE_COMMIT, "source commit")
    a.check(data["scope_literal"] == SCOPE, "scope")
    a.check(set(data["evaluator"]) == {"path", "version", "sha256"}, "evaluator keys")
    a.check(data["evaluator"]["path"] == "flow_systems/skills/route-a-evaluator.md", "evaluator path")
    a.check(data["evaluator"]["version"] == "0.2.0", "evaluator version")
    a.check(data["evaluator"]["sha256"] == EVALUATOR_SHA256, "evaluator hash")
    a.check(data["payload_sha256"] == payload_hash(data), "payload hash")
    a.check(set(data["frozen_object"]) == {"system", "main_parameter_domain", "clock", "symmetry", "lyapunov_function", "boundary_domains", "forbidden_data"}, "object keys")
    a.check(data["frozen_object"]["main_parameter_domain"] == "sigma>0, beta>0, rho in R", "parameter domain")
    a.check(data["frozen_object"]["lyapunov_function"] == "V=x^2+y^2+(z-rho-sigma)^2", "V definition")
    theorem_keys = {
        "exact_dissipation_ledger", "absorbing_inequality", "global_consequence", "divergence",
        "equilibria", "origin_polynomial", "wing_polynomial", "hopf_surface", "stability_atlas",
        "sigma_zero_boundary", "beta_zero_boundary", "double_zero_boundary", "bifurcation_scope",
    }
    a.check(set(data["theorem"]) == theorem_keys, "theorem keys")
    a.check("kappa=min(2 sigma,2,beta)" in data["theorem"]["absorbing_inequality"], "kappa theorem")
    a.check("only the linear Hopf locus is claimed" in data["theorem"]["bifurcation_scope"], "Hopf scope")
    regression = data["regression"]
    a.check(set(regression) == {"main_rows", "main_row_count", "dissipation_rows", "dissipation_row_count", "degenerate_rows"}, "regression keys")
    rows = regression["main_rows"]
    a.check(regression["main_row_count"] == len(EXPECTED_MAIN) == len(rows), "main count")
    for row, frozen in zip(rows, EXPECTED_MAIN):
        case_id, sigma_text, beta_text, rho_text = frozen
        a.check(set(row) == ROW_KEYS, f"{case_id}: row keys")
        a.check((row["case_id"], row["sigma"], row["beta"], row["rho"]) == frozen, f"{case_id}: frozen input")
        sigma, beta, rho = q(sigma_text), q(beta_text), q(rho_text)
        a.check(sigma > 0 and beta > 0, f"{case_id}: positive main domain")
        c = sigma + rho
        kappa = min(2 * sigma, Fraction(2), beta)
        a.check(row["divergence"] == qt(-(sigma + beta + 1)), f"{case_id}: divergence")
        a.check(row["energy_center_c"] == qt(c), f"{case_id}: c")
        a.check(row["differential_inequality_kappa"] == qt(kappa), f"{case_id}: kappa")
        a.check(row["absorbing_floor_beta_c2_over_kappa"] == qt(beta * c * c / kappa), f"{case_id}: floor")
        a.check(row["origin_quadratic_factor"] == ["1", qt(sigma + 1), qt(sigma * (1 - rho))], f"{case_id}: origin polynomial")
        ostab = "asymptotically_stable" if rho < 1 else ("nonhyperbolic_zero_eigenvalue" if rho == 1 else "saddle_unstable")
        a.check(row["origin_stability"] == ostab, f"{case_id}: origin stability")
        exists = rho > 1
        a.check(row["wing_equilibria_exist"] is exists, f"{case_id}: wing existence")
        if not exists:
            for key in ("wing_amplitude_squared", "wing_characteristic_polynomial", "hurwitz_margin", "rho_h", "hopf_frequency_squared"):
                a.check(row[key] is None, f"{case_id}: absent {key}")
            a.check(row["wing_stability"] == "not_present", f"{case_id}: absent stability")
            continue
        poly = [Fraction(1), sigma + beta + 1, beta * (sigma + rho), 2 * sigma * beta * (rho - 1)]
        margin = sigma * (sigma + beta + 3) + (beta + 1 - sigma) * rho
        a.check(row["wing_amplitude_squared"] == qt(beta * (rho - 1)), f"{case_id}: wing amplitude")
        a.check(row["wing_characteristic_polynomial"] == [qt(x) for x in poly], f"{case_id}: wing polynomial")
        a.check(row["hurwitz_margin"] == qt(margin), f"{case_id}: margin")
        if sigma <= beta + 1:
            a.check(row["rho_h"] is None, f"{case_id}: no finite rhoH")
            a.check(row["wing_stability"] == "asymptotically_stable_all_rho_gt_1", f"{case_id}: all stable")
            a.check(row["hopf_frequency_squared"] is None, f"{case_id}: no Hopf frequency")
        else:
            rho_h = sigma * (sigma + beta + 3) / (sigma - beta - 1)
            a.check(row["rho_h"] == qt(rho_h), f"{case_id}: rhoH")
            expected_stability = "asymptotically_stable" if rho < rho_h else ("linear_hopf_boundary" if rho == rho_h else "linearly_unstable")
            a.check(row["wing_stability"] == expected_stability, f"{case_id}: wing stability")
            expected_frequency = qt(beta * (sigma + rho_h)) if rho == rho_h else None
            a.check(row["hopf_frequency_squared"] == expected_frequency, f"{case_id}: frequency")
            a.check(margin > 0 if rho < rho_h else (margin == 0 if rho == rho_h else margin < 0), f"{case_id}: margin sign")

    samples = regression["dissipation_rows"]
    a.check(regression["dissipation_row_count"] == len(EXPECTED_SAMPLES) == len(samples), "sample count")
    for row, frozen in zip(samples, EXPECTED_SAMPLES):
        sigma_text, beta_text, rho_text, point = frozen
        a.check(set(row) == SAMPLE_KEYS, "sample keys")
        a.check((row["sigma"], row["beta"], row["rho"], row["point"]) == frozen, "frozen dissipation sample")
        sigma, beta, rho = q(sigma_text), q(beta_text), q(rho_text)
        x, y, z = map(q, point)
        c = sigma + rho
        xdot, ydot, zdot = sigma * (y - x), x * (rho - z) - y, x * y - beta * z
        direct = 2 * x * xdot + 2 * y * ydot + 2 * (z - c) * zdot
        ledger = -2 * sigma * x * x - 2 * y * y - beta * z * z - beta * (z - c) ** 2 + beta * c * c
        a.check(row["V"] == qt(x * x + y * y + (z - c) ** 2), "sample V")
        a.check(row["Vdot_direct"] == qt(direct), "sample direct")
        a.check(row["Vdot_square_ledger"] == qt(ledger), "sample ledger")
        a.check(direct == ledger, "sample cancellation")

    a.check(len(regression["degenerate_rows"]) == 3, "degenerate count")
    a.check([r["boundary"] for r in regression["degenerate_rows"]] == ["sigma=0,beta>0", "beta=0,sigma>0", "sigma=beta=0"], "degenerate labels")
    a.check(all(set(r) == {"boundary", "samples"} for r in regression["degenerate_rows"]), "degenerate row keys")
    a.check(len(data["exact_identities"]) == 6, "identity count")
    a.check(all(set(item) == {"name", "formula"} for item in data["exact_identities"]), "identity keys")
    a.check([i["name"] for i in data["exact_identities"]] == ["cross_term_cancellation", "square_ledger", "hurwitz_margin", "hopf_factorization", "sigma_zero_tangent", "beta_zero_tangent"], "identity ledger")
    route = data["route_a"]
    a.check(set(route) == {"tuple", "overall", "route_b_invocation_allowed", "strongest_positive", "strongest_failure"}, "route keys")
    a.check(route["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"], "route tuple")
    a.check(route["overall"] == "ROUTE_A_REJECTED", "route verdict")
    a.check(route["route_b_invocation_allowed"] is False, "Route B")
    a.check(set(data["scope_flags"]) == SCOPE_KEYS, "scope flag keys")
    a.check(all(value is False for value in data["scope_flags"].values()), "scope flags")
    a.check([c["doi"] for c in data["citations"]] == ["10.1175/1520-0469(1963)020<0130:DNF>2.0.CO;2", "10.1016/0375-9601(86)90031-9", "10.1007/s002080010018", "10.1007/BF02684769"], "citation ledger")
    a.check(all(set(c) == {"id", "doi", "role"} for c in data["citations"]), "citation keys")
    a.check(len(data["nonclaims"]) == 5, "nonclaim count")
    return a.count


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    count = validate(data)
    print(f"C227 independent checker: PASS ({count} assertions; producer-independent exact reconstruction)")


if __name__ == "__main__":
    main()
