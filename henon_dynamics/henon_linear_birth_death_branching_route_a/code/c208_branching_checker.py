#!/usr/bin/env python3
"""Producer-independent exact checker with recursive key closure for C208."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c208_branching_evidence.json"
SOURCE_COMMIT = "d108ef46fea7a8f62490a69071a83fcbda7c113b"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
MAX_INITIAL = 4
MAX_STATE = 12
EXPECTED_HEADLINE = (
    "The linear birth--death branching process has an all-parameter Mobius PGF semigroup, "
    "exact survivor-mixture transitions, and a three-regime limit atlas"
)

EXPECTED_CASES = [
    ("super_2_1_delta_1_2", "off_critical", F(2), F(1), F(1, 2), "finite positive time"),
    ("super_3_1_delta_1_4", "off_critical", F(3), F(1), F(1, 4), "finite positive time"),
    ("sub_1_2_delta_2", "off_critical", F(1), F(2), F(2), "finite positive time"),
    ("sub_1_3_delta_4", "off_critical", F(1), F(3), F(4), "finite positive time"),
    ("pure_birth_1_0_delta_1_3", "off_critical", F(1), F(0), F(1, 3), "finite positive time"),
    ("pure_death_0_1_delta_2", "off_critical", F(0), F(1), F(2), "finite positive time"),
    ("super_time_zero_2_1", "off_critical", F(2), F(1), F(1), "t=0"),
    ("sub_time_zero_1_2", "off_critical", F(1), F(2), F(1), "t=0"),
    ("critical_half_tau_half", "critical", F(1, 2), F(1, 2), F(1, 2), "finite positive time"),
    ("critical_one_tau_one", "critical", F(1), F(1), F(1), "finite positive time"),
    ("critical_two_tau_two", "critical", F(2), F(2), F(2), "finite positive time"),
    ("critical_time_zero", "critical", F(1), F(1), F(0), "t=0"),
    ("zero_rates_all_times", "zero_rates", F(0), F(0), F(0), "arbitrary t>=0"),
]

EXPECTED_SEMIGROUP = [
    ("super_2_1", "off_critical", F(2), F(1), F(1, 2), F(1, 4)),
    ("super_3_1", "off_critical", F(3), F(1), F(1, 2), F(1, 3)),
    ("sub_1_2", "off_critical", F(1), F(2), F(2), F(3)),
    ("sub_1_3", "off_critical", F(1), F(3), F(2), F(4)),
    ("pure_birth", "off_critical", F(1), F(0), F(1, 2), F(1, 3)),
    ("pure_death", "off_critical", F(0), F(1), F(2), F(3)),
    ("critical_small", "critical", F(1), F(1), F(1, 2), F(1, 3)),
    ("critical_large", "critical", F(2), F(2), F(1), F(2)),
    ("zero_rates", "zero_rates", F(0), F(0), F(0), F(0)),
]


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def parameters(mode: str, lam: F, mu: F, coordinate: F) -> tuple[F, F]:
    if mode == "off_critical":
        denominator = lam - mu * coordinate
        return mu * (1 - coordinate) / denominator, lam * (1 - coordinate) / denominator
    if mode == "critical":
        return coordinate / (1 + coordinate), coordinate / (1 + coordinate)
    if mode == "zero_rates":
        return F(0), F(0)
    raise AssertionError(mode)


def mobius(p0: F, beta: F) -> tuple[F, F, F, F]:
    return p0, 1 - p0 - beta, F(1), -beta


def compose(left, right):
    a1, b1, c1, d1 = left
    a2, b2, c2, d2 = right
    ac = a1 * c2 + b1 * a2
    bc = a1 * d2 + b1 * b2
    cc = c1 * c2 + d1 * a2
    dc = c1 * d2 + d1 * b2
    return ac / cc, bc / cc, F(1), dc / cc


def lineage_probability(n: int, p0: F, beta: F) -> F:
    return p0 if n == 0 else (1 - p0) * (1 - beta) * beta ** (n - 1)


def binomial_lineages(z: int, k: int, p0: F) -> F:
    return F(comb(z, k)) * (1 - p0) ** k * p0 ** (z - k)


def transition_by_convolution(z: int, n: int, p0: F, beta: F) -> F:
    """Independent truncated polynomial convolution of z one-lineage laws."""
    base = [lineage_probability(j, p0, beta) for j in range(n + 1)]
    coefficients = [F(1)] + [F(0)] * n
    for _ in range(z):
        updated = [F(0)] * (n + 1)
        for i, left in enumerate(coefficients):
            for j, right in enumerate(base):
                if i + j <= n:
                    updated[i + j] += left * right
        coefficients = updated
    return coefficients[n]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    args = parser.parse_args()
    data = json.loads(args.evidence.read_text())
    assertions = 0

    def check(condition, message):
        nonlocal assertions
        assertions += 1
        if not condition:
            raise AssertionError(message)

    def keys(obj, expected, label):
        check(isinstance(obj, dict), f"{label} must be a mapping")
        check(set(obj) == set(expected), f"{label} exact keys failed: {set(obj) ^ set(expected)}")

    keys(data, ["schema", "candidate_id", "evaluation_date", "source_commit", "scope_literal", "evaluator",
                "headline", "frozen_object", "theorem", "asymptotics", "regression", "summary", "route_a",
                "scope_flags", "citations", "nonclaims", "payload_sha256"], "top")
    keys(data["evaluator"], ["path", "version", "sha256"], "evaluator")
    keys(data["frozen_object"], ["process", "generator", "parameters", "clock", "normalization",
                                  "determinant_convention", "allowed_data", "forbidden_data"], "frozen_object")
    keys(data["theorem"], ["backward_equation", "off_critical_mobius", "critical_mobius", "semigroup",
                            "one_ancestor_law", "off_critical_parameters", "critical_parameters",
                            "arbitrary_z_transition", "mixture_warning", "mean", "variance_off_critical",
                            "variance_critical", "subcritical_qsd", "subcritical_qsd_invariance",
                            "critical_yaglom", "supercritical_limit", "boundary_ledger"], "theorem")
    keys(data["asymptotics"], ["proof_status", "subcritical_conditional_pgf_limit",
                                "critical_scaled_laplace_limit", "supercritical_one_ancestor_laplace_limit",
                                "supercritical_z_ancestor_laplace_limit", "supercritical_atom_at_zero",
                                "supercritical_conditional_components"], "asymptotics")
    keys(data["regression"], ["maximum_initial_population", "maximum_reported_state", "parameter_cases",
                               "semigroup_cases"], "regression")
    keys(data["summary"], ["parameter_case_count", "semigroup_case_count", "population_row_count",
                            "transition_probability_count", "survivor_weight_count", "moment_identity_count",
                            "one_ancestor_parameter_identity_count", "semigroup_coefficient_identity_count",
                            "exact_scalar_identity_count"], "summary")
    keys(data["route_a"], ["tuple", "overall", "route_b_invocation_allowed", "strongest_positive",
                            "strongest_failure"], "route_a")
    keys(data["scope_flags"], ["uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data",
                                "claims_euler_factors", "claims_root_numbers", "claims_automorphy",
                                "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator",
                                "invokes_route_b"], "scope_flags")
    keys(data["citations"][0], ["key", "claim", "title", "authors", "report_number", "date", "url",
                                  "persistent_url"], "citation[0]")

    check(data["payload_sha256"] == payload_hash(data), "payload hash")
    check(data["schema"] == "hcs-c208-linear-birth-death-v1", "schema")
    check(data["candidate_id"] == "HCS-C208", "candidate")
    check(data["evaluation_date"] == "2026-08-27", "date")
    check(data["source_commit"] == SOURCE_COMMIT, "source commit")
    check(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    check(data["evaluator"] == {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0",
                                 "sha256": EVALUATOR_SHA256}, "evaluator lock")
    check(data["headline"] == EXPECTED_HEADLINE, "headline")
    check(data["frozen_object"]["determinant_convention"] ==
          "none; the probability generating function is not called a zeta or determinant", "PGF naming firewall")
    check(data["theorem"]["mixture_warning"] ==
          "the all-parameter family is a binomial-survivor mixture, not uniformly one negative-binomial law; special parameters can collapse the mixture",
          "mixture warning")
    check(data["theorem"]["subcritical_qsd_invariance"] ==
          "for rho=lambda/mu and g(s)=(1-rho)s/(1-rho*s), [g(F_t(s))-g(F_t(0))]/[1-g(F_t(0))]=g(s)",
          "subcritical QSD invariance theorem")
    check(data["asymptotics"]["proof_status"] ==
          "symbolic limits proved separately from the finite exact regression", "asymptotic separation")
    check(data["route_a"]["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"], "route tuple")
    check(data["route_a"]["overall"] == "ROUTE_A_REJECTED", "route verdict")
    check(data["route_a"]["route_b_invocation_allowed"] is False, "Route B denied")
    check(all(value is False for value in data["scope_flags"].values()), "scope flags")
    citation = data["citations"][0]
    check(citation["key"] == "KarlinMcGregor1958", "source key")
    check(citation["report_number"] == "KAR ONR 3", "report number")
    check(citation["url"] ==
          "https://statistics.stanford.edu/technical-reports/linear-growth-birth-and-death-processes", "source URL")
    check(citation["persistent_url"] == "https://purl.stanford.edu/fx071vs8733", "persistent URL")

    regression = data["regression"]
    check(regression["maximum_initial_population"] == MAX_INITIAL, "maximum initial")
    check(regression["maximum_reported_state"] == MAX_STATE, "maximum state")
    cases = regression["parameter_cases"]
    check(len(cases) == len(EXPECTED_CASES), "parameter case count")
    transition_count = survivor_count = moment_count = parameter_count = 0
    case_keys = ["case_id", "regime", "lambda", "mu", "clock_coordinate_name", "clock_coordinate",
                 "time_descriptor", "p0", "beta", "mobius_coefficients_a_b_c_d",
                 "mobius_determinant_bc_minus_ad", "one_ancestor_probabilities_n_0_to_12",
                 "one_ancestor_prefix_probability_n_0_to_12", "population_rows"]
    population_keys = ["initial_population", "survivor_weights_k_0_to_z",
                       "transition_probabilities_n_0_to_12", "prefix_probability_n_0_to_12",
                       "tail_probability_after_12", "mean", "variance", "transition_structure"]
    for index, spec in enumerate(EXPECTED_CASES):
        case_id, mode, lam, mu, coordinate, time_descriptor = spec
        row = cases[index]
        keys(row, case_keys, f"case[{index}]")
        check(row["case_id"] == case_id, "case id")
        check(row["regime"] == mode, "regime")
        check(F(row["lambda"]) == lam and F(row["mu"]) == mu, "rates")
        check(F(row["clock_coordinate"]) == coordinate, "clock coordinate")
        check(row["time_descriptor"] == time_descriptor, "time descriptor")
        expected_clock = "delta=exp(-(lambda-mu)t)" if mode == "off_critical" else "tau=lambda*t"
        if mode == "zero_rates":
            expected_clock = "tau=lambda*t=0 for every t"
        check(row["clock_coordinate_name"] == expected_clock, "clock name")
        p0, beta = parameters(mode, lam, mu, coordinate)
        check(F(row["p0"]) == p0, "p0")
        check(F(row["beta"]) == beta, "beta")
        parameter_count += 2
        expected_mobius = mobius(p0, beta)
        check(tuple(F(value) for value in row["mobius_coefficients_a_b_c_d"]) == expected_mobius,
              "Mobius coefficients")
        check(F(row["mobius_determinant_bc_minus_ad"]) ==
              expected_mobius[1] * expected_mobius[2] - expected_mobius[0] * expected_mobius[3],
              "Mobius determinant")
        lineage = [lineage_probability(n, p0, beta) for n in range(MAX_STATE + 1)]
        check([F(value) for value in row["one_ancestor_probabilities_n_0_to_12"]] == lineage,
              "one-ancestor coefficients")
        check(F(row["one_ancestor_prefix_probability_n_0_to_12"]) == sum(lineage),
              "one-ancestor prefix")
        check(len(row["population_rows"]) == MAX_INITIAL + 1, "population rows")
        for z, pop in enumerate(row["population_rows"]):
            keys(pop, population_keys, f"case[{index}].population[{z}]")
            check(pop["initial_population"] == z, "initial population")
            expected_weights = [binomial_lineages(z, k, p0) for k in range(z + 1)]
            actual_weights = [F(value) for value in pop["survivor_weights_k_0_to_z"]]
            check(actual_weights == expected_weights, "survivor weights")
            for actual, expected in zip(actual_weights, expected_weights):
                check(actual == expected, "survivor scalar")
                survivor_count += 1
            check(sum(actual_weights) == 1, "survivor normalization")
            probabilities = [F(value) for value in pop["transition_probabilities_n_0_to_12"]]
            check(len(probabilities) == MAX_STATE + 1, "transition length")
            for n, actual in enumerate(probabilities):
                expected = transition_by_convolution(z, n, p0, beta)
                check(actual == expected, "independent convolution coefficient")
                transition_count += 1
            prefix = sum(probabilities)
            check(F(pop["prefix_probability_n_0_to_12"]) == prefix, "prefix")
            check(F(pop["tail_probability_after_12"]) == 1 - prefix, "tail")
            check(0 <= prefix <= 1, "prefix bounds")
            mean_one = (1 - p0) / (1 - beta)
            second_one = (1 - p0) * (1 + beta) / (1 - beta) ** 2
            variance_one = second_one - mean_one ** 2
            check(F(pop["mean"]) == z * mean_one, "mean")
            check(F(pop["variance"]) == z * variance_one, "variance")
            moment_count += 2
            check(pop["transition_structure"] ==
                  "binomial surviving lineages mixed with conditional negative-binomial sums", "mixture label")

    semigroup_rows = regression["semigroup_cases"]
    check(len(semigroup_rows) == len(EXPECTED_SEMIGROUP), "semigroup case count")
    semigroup_keys = ["case_id", "regime", "lambda", "mu", "first_coordinate", "second_coordinate",
                      "combined_coordinate", "coordinate_rule", "composed_coefficients_a_b_c_d",
                      "target_coefficients_a_b_c_d", "four_coefficient_residuals_zero"]
    semigroup_count = 0
    for index, spec in enumerate(EXPECTED_SEMIGROUP):
        case_id, mode, lam, mu, first, second = spec
        row = semigroup_rows[index]
        keys(row, semigroup_keys, f"semigroup[{index}]")
        check(row["case_id"] == case_id and row["regime"] == mode, "semigroup identity")
        check(F(row["lambda"]) == lam and F(row["mu"]) == mu, "semigroup rates")
        check(F(row["first_coordinate"]) == first and F(row["second_coordinate"]) == second,
              "semigroup coordinates")
        target_coordinate = first * second if mode == "off_critical" else first + second
        check(F(row["combined_coordinate"]) == target_coordinate, "combined coordinate")
        expected_rule = "multiplication" if mode == "off_critical" else "addition"
        if mode == "zero_rates":
            expected_rule = "identity"
        check(row["coordinate_rule"] == expected_rule, "coordinate rule")
        left = mobius(*parameters(mode, lam, mu, first))
        right = mobius(*parameters(mode, lam, mu, second))
        actual_composed = tuple(F(value) for value in row["composed_coefficients_a_b_c_d"])
        actual_target = tuple(F(value) for value in row["target_coefficients_a_b_c_d"])
        expected_target = mobius(*parameters(mode, lam, mu, target_coordinate))
        check(actual_composed == compose(left, right), "composed coefficients")
        check(actual_target == expected_target, "target coefficients")
        for actual, expected in zip(actual_composed, expected_target):
            check(actual == expected, "semigroup coefficient")
            semigroup_count += 1
        check(row["four_coefficient_residuals_zero"] is True, "semigroup flag")

    summary = data["summary"]
    check(summary["parameter_case_count"] == len(cases), "summary parameter cases")
    check(summary["semigroup_case_count"] == len(semigroup_rows), "summary semigroup cases")
    check(summary["population_row_count"] == len(cases) * (MAX_INITIAL + 1), "summary population rows")
    check(summary["transition_probability_count"] == transition_count, "summary transitions")
    check(summary["survivor_weight_count"] == survivor_count, "summary survivor weights")
    check(summary["moment_identity_count"] == moment_count, "summary moments")
    check(summary["one_ancestor_parameter_identity_count"] == parameter_count, "summary parameters")
    check(summary["semigroup_coefficient_identity_count"] == semigroup_count, "summary semigroup")
    check(summary["exact_scalar_identity_count"] ==
          transition_count + survivor_count + moment_count + parameter_count + semigroup_count, "summary total")
    print(json.dumps({
        "status": "C208_CHECKER_PASS",
        "assertions": assertions,
        "exact_scalar_identities": summary["exact_scalar_identity_count"],
        "recursive_key_sets": 9 + len(cases) + len(cases) * (MAX_INITIAL + 1) + len(semigroup_rows),
        "producer_imported": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
