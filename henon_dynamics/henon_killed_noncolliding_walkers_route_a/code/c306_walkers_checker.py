#!/usr/bin/env python3
"""Independent strict checker for HCS-C306 evidence and Route-A YAML.

This module deliberately does not import the producer.  It reconstructs the
killed generator and diagonalizes it numerically as an independent lane.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import re
import sys
from pathlib import Path

import numpy as np
import scipy.linalg
import yaml

if sys.flags.optimize:
    raise RuntimeError("HCS-C306 checker refuses python -O: validation must not be disabled")

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c306_walkers_evidence.json"
DEFAULT_YAML = ROOT / "evaluations/route_a/HCS-C306/2026-09-03.yaml"
SOURCE = "c0259978b1d7ebae63fe7b39fce1af2655b8529d"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600
TUPLE = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]
FLAGS = {
    "claims_target_arithmetic_local_data": False,
    "claims_target_euler_factors": False,
    "claims_root_number": False,
    "claims_automorphy": False,
    "claims_target_divisor_or_counting_law": False,
    "claims_target_functional_equation": False,
    "claims_target_zero_match": False,
    "claims_hilbert_polya_operator": False,
    "invokes_route_b": False,
}
MODEL = {
    "state_space": "W_{L,k}={1<=x_1<...<x_k<=L}, with integers 1<=k<=L",
    "one_particle_rates": "rate 1 to each nearest neighbour; Dirichlet killing at 0 and L+1",
    "many_particle_killing": "kill at the first boundary attempt or first coincidence attempt",
    "generator": "Q_k(x,y)=1 for one legal coordinate step, Q_k(x,x)=-2k, and zero otherwise",
    "not_exclusion": "illegal collision attempts kill; they are not reflected or suppressed",
}
THEOREM = {
    "one_particle": "p_t(i,j)=2/(L+1) sum_{r=1}^L exp(-epsilon_r t) sin(pi r i/(L+1)) sin(pi r j/(L+1))",
    "energies": "epsilon_r=2-2 cos(pi r/(L+1)); Lambda_m=sum_a epsilon_{m_a}",
    "karlin_mcgregor": "P_t(x,y)=det[p_t(x_i,y_j)]",
    "slater_basis": "Phi_m(x)=det[phi_{m_a}(x_b)] is a complete orthonormal eigenbasis on W_{L,k}",
    "survival": "S_x(t)=sum_m exp(-Lambda_m t) Phi_m(x) A_m, A_m=sum_y Phi_m(y)",
    "absorption": "P_x(tau<=t)=1-S_x(t); f_x(t)=sum_m Lambda_m exp(-Lambda_m t) Phi_m(x) A_m",
    "moments": "E_x[tau^r]=r! sum_m Phi_m(x) A_m/Lambda_m^r for every integer r>=1",
    "ground": "m_0=(1,...,k), h=sign(Phi_m0)>0, Lambda_0=sum_{r=1}^k epsilon_r",
    "leading": "S_x(t)=h(x)A_0 exp(-Lambda_0 t)+O(exp(-Lambda_1 t)) when k<L; k=L is exact exp(-2Lt)",
    "qsd": "nu(y)=h(y)/A_0 is the unique QSD and the Yaglom limit from every state",
    "doob": "q^h(x,y)=q(x,y)h(y)/h(x), q^h(x,x)=q(x,x)+Lambda_0, invariant pi^h(x)=h(x)^2",
    "gap": "for k<L the Q-process gap is epsilon_{k+1}-epsilon_k; for k=L the Q-process is a singleton with no nonzero relaxation mode",
}
PROOF = {
    "boundary_diagonalization": "the discrete sine basis diagonalizes the one-particle Dirichlet generator",
    "exterior_power": "antisymmetrized tensor eigenvectors restrict to the chamber and give all binomial(L,k) Slater modes",
    "path_switching": "Karlin--McGregor sign reversal cancels paths at their first coincidence",
    "positivity": "the signed consecutive-mode sine determinant is strictly positive on the chamber",
    "perron": "finite irreducibility plus symmetry makes the positive ground mode simple and controls QSD/Yaglom asymptotics",
    "transform": "Qh=-Lambda_0 h gives conservative Doob rates; symmetry gives detailed balance with h^2",
}
BOUNDARIES = [
    "The determinant is the killed collision kernel, not an exclusion or reflecting kernel.",
    "Absorption laws are exact finite spectral sums; no simpler first-passage closed form is claimed.",
    "For k=L the chamber has one state, tau is Exp(2L), and the Q-process has no nonzero relaxation mode.",
    "Finite decimal rows are regression diagnostics; the all-parameter theorem is analytic.",
]
SOURCES = ["doi:10.2140/pjm.1959.9.1141", "doi:10.2307/3212311"]


class Count:
    value = 0


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)
    Count.value += 1


def check_int(value, expected: int, message: str) -> None:
    check(type(value) is int and value == expected, message)


def exact_tree(actual, expected) -> bool:
    if type(actual) is not type(expected):
        return False
    if type(expected) is dict:
        return set(actual) == set(expected) and all(exact_tree(actual[key], expected[key]) for key in expected)
    if type(expected) is list:
        return len(actual) == len(expected) and all(exact_tree(a, b) for a, b in zip(actual, expected))
    return actual == expected


def duplicate_guard(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise ValueError(f"duplicate JSON key: {key}")
        out[key] = value
    return out


def reject_nonfinite(value):
    raise ValueError(f"non-finite JSON constant: {value}")


def strict_json(path: Path) -> dict:
    raw = path.read_bytes()
    if len(raw) > 8_000_000:
        raise ValueError("JSON size budget exceeded")
    text = raw.decode("utf-8", errors="strict")
    value = json.loads(text, object_pairs_hook=duplicate_guard, parse_constant=reject_nonfinite)
    check(type(value) is dict, "JSON top-level object")
    check(text == json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False) + "\n", "canonical JSON")
    return value


class UniqueSafeLoader(yaml.SafeLoader):
    pass


UniqueSafeLoader.yaml_implicit_resolvers = {
    key: [(tag, pattern) for tag, pattern in values if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def unique_mapping(loader, node, deep=False):
    out = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in out:
            raise ValueError("non-string or duplicate YAML key")
        out[key] = loader.construct_object(value_node, deep=deep)
    return out


UniqueSafeLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def strict_yaml(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML aliases forbidden")
    value = yaml.load(raw, Loader=UniqueSafeLoader)
    check(type(value) is dict, "YAML top-level mapping")
    return value


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def decimal(text, places: int, message: str) -> float:
    check(type(text) is str, message + " type")
    pattern = rf"-?(?:0|[1-9][0-9]*)\.[0-9]{{{places}}}"
    check(re.fullmatch(pattern, text) is not None, message + " syntax")
    value = float(text)
    check(math.isfinite(value), message + " finite")
    return value


def scientific(text, places: int, message: str) -> float:
    check(type(text) is str and re.fullmatch(rf"[0-9]\.[0-9]{{{places}}}e[+-][0-9]{{2}}", text) is not None,
          message + " syntax")
    value = float(text)
    check(math.isfinite(value), message + " finite")
    return value


def epsilon(L: int, r: int) -> float:
    return 2.0 - 2.0 * math.cos(math.pi * r / (L + 1))


def sine(L: int, r: int, x: int) -> float:
    return math.sqrt(2.0 / (L + 1)) * math.sin(math.pi * r * x / (L + 1))


def slater(L: int, mode: tuple[int, ...], state: tuple[int, ...]) -> float:
    return float(np.linalg.det(np.array([[sine(L, r, x) for x in state] for r in mode])))


def generator(states: list[tuple[int, ...]], L: int, k: int) -> np.ndarray:
    index = {state: i for i, state in enumerate(states)}
    q = np.zeros((len(states), len(states)))
    for i, state in enumerate(states):
        q[i, i] = -2 * k
        for coordinate in range(k):
            for step in (-1, 1):
                trial = list(state)
                trial[coordinate] += step
                if 1 <= trial[coordinate] <= L and len(set(trial)) == k:
                    trial.sort()
                    q[i, index[tuple(trial)]] = 1.0
    return q


CASE_KEYS = {
    "L", "k", "dimension", "states", "mode_count", "legal_directed_edges", "total_killing_rate",
    "negative_generator_trace", "ground_mode", "ground_energy_decimal_15", "ground_h_l1_decimal_15",
    "ground_h_min_decimal_15", "ground_h_l2_squared_decimal_15", "spectral_gap_decimal_15",
    "spectral_gap_boundary", "max_eigen_residual_decimal_12", "max_orthonormality_residual_decimal_12",
    "max_karlin_mcgregor_residual_decimal_12", "max_q_detailed_balance_residual_decimal_12",
    "probe_count", "probes",
}
PROBE_KEYS = {"state_index", "time", "survival_decimal_15", "absorption_density_decimal_15"}


def check_case(row: dict, L: int, k: int, heavy: bool) -> tuple[int, int]:
    check(type(row) is dict and set(row) == CASE_KEYS, "case exact keys")
    check_int(row["L"], L, "L coordinate")
    check_int(row["k"], k, "k coordinate")
    states = list(itertools.combinations(range(1, L + 1), k))
    dimension = math.comb(L, k)
    check_int(row["dimension"], dimension, "dimension")
    check(type(row["states"]) is list and len(row["states"]) == dimension, "state list length")
    expected_states = [list(state) for state in states]
    check(exact_tree(row["states"], expected_states), "state coordinates/types/order")
    check_int(row["mode_count"], dimension, "mode count")
    q = generator(states, L, k)
    legal = int(np.count_nonzero(q - np.diag(np.diag(q))))
    killing = int(round(float(np.sum(-q @ np.ones(dimension)))))
    check_int(row["legal_directed_edges"], legal, "legal edges")
    check_int(row["total_killing_rate"], killing, "killing total")
    check_int(row["negative_generator_trace"], 2 * k * dimension, "trace")
    check(exact_tree(row["ground_mode"], list(range(1, k + 1))), "ground mode")

    modes = list(itertools.combinations(range(1, L + 1), k))
    energies = np.array([sum(epsilon(L, r) for r in mode) for mode in modes])
    direct_energies = np.linalg.eigvalsh(-q)
    check(float(np.max(np.abs(np.sort(energies) - direct_energies))) < 3e-12, "direct generator spectrum")
    ground_energy = decimal(row["ground_energy_decimal_15"], 15, "ground energy")
    check(abs(ground_energy - energies[0]) < 8e-15, "ground energy value")

    sign = -1.0 if (k * (k - 1) // 2) % 2 else 1.0
    h = np.array([sign * slater(L, modes[0], state) for state in states])
    check(float(np.min(h)) > 0.0, "strict ground positivity")
    check(abs(decimal(row["ground_h_l1_decimal_15"], 15, "ground l1") - float(np.sum(h))) < 8e-15,
          "ground l1 value")
    check(abs(decimal(row["ground_h_min_decimal_15"], 15, "ground minimum") - float(np.min(h))) < 8e-15,
          "ground minimum value")
    check(abs(decimal(row["ground_h_l2_squared_decimal_15"], 15, "ground norm") - float(h @ h)) < 8e-15,
          "ground norm value")
    if k < L:
        check(type(row["spectral_gap_decimal_15"]) is str, "gap type")
        gap = decimal(row["spectral_gap_decimal_15"], 15, "gap")
        check(abs(gap - (epsilon(L, k + 1) - epsilon(L, k))) < 8e-15, "gap formula")
        check(row["spectral_gap_boundary"] == "ordinary: replace occupied mode k by k+1", "gap label")
    else:
        check(row["spectral_gap_decimal_15"] is None, "singleton gap null")
        check(row["spectral_gap_boundary"] == "singleton Q-process: no nonzero relaxation mode", "singleton label")
        check(dimension == 1 and abs(ground_energy - 2 * L) < 8e-15, "full occupancy exponential rate")

    for key in ("max_eigen_residual_decimal_12", "max_orthonormality_residual_decimal_12",
                "max_karlin_mcgregor_residual_decimal_12", "max_q_detailed_balance_residual_decimal_12"):
        check(scientific(row[key], 12, key) < 2e-12, key + " threshold")

    probe_indices = sorted({0, dimension // 2, dimension - 1})
    expected_probe_count = 3 * len(probe_indices)
    check_int(row["probe_count"], expected_probe_count, "probe count")
    check(type(row["probes"]) is list and len(row["probes"]) == expected_probe_count, "probe list length")
    cursor = 0
    for time_text in ("0", "0.375", "1.25"):
        time = float(time_text)
        p = scipy.linalg.expm(q * time)
        survival_vector = p @ np.ones(dimension)
        density_vector = -q @ np.ones(dimension) if time == 0 else p @ (-q @ np.ones(dimension))
        for state_index in probe_indices:
            probe = row["probes"][cursor]
            cursor += 1
            check(type(probe) is dict and set(probe) == PROBE_KEYS, "probe exact keys")
            check_int(probe["state_index"], state_index, "probe state index")
            check(type(probe["time"]) is str and probe["time"] == time_text, "probe time")
            survival = decimal(probe["survival_decimal_15"], 15, "survival")
            density = decimal(probe["absorption_density_decimal_15"], 15, "density")
            check(abs(survival - survival_vector[state_index]) < 2e-13, "direct survival")
            check(abs(density - density_vector[state_index]) < 2e-13, "direct absorption density")
            check(-2e-13 <= survival <= 1 + 2e-13 and density >= -2e-13, "probability faces")

    if heavy:
        phi_matrix = np.array([[slater(L, mode, state) for state in states] for mode in modes])
        check(float(np.max(np.abs(phi_matrix @ phi_matrix.T - np.eye(dimension)))) < 3e-12,
              "complete orthonormal Slater basis")
        check(float(np.max(np.abs(q @ phi_matrix.T + phi_matrix.T * energies))) < 4e-12,
              "all eigenvectors")
        for time in (0.375, 1.25):
            one = np.array([[sum(math.exp(-epsilon(L, r) * time) * sine(L, r, i) * sine(L, r, j)
                                 for r in range(1, L + 1))
                             for j in range(1, L + 1)] for i in range(1, L + 1)])
            direct = scipy.linalg.expm(q * time)
            for i in probe_indices:
                for j in probe_indices:
                    km = float(np.linalg.det(one[np.ix_([x - 1 for x in states[i]],
                                                       [y - 1 for y in states[j]])]))
                    check(abs(km - direct[i, j]) < 3e-13, "Karlin--McGregor versus direct exponential")
        qh = np.zeros_like(q)
        for i in range(dimension):
            for j in range(dimension):
                if i != j and q[i, j] != 0:
                    qh[i, j] = q[i, j] * h[j] / h[i]
            qh[i, i] = q[i, i] + energies[0]
        check(float(np.max(np.abs(qh @ np.ones(dimension)))) < 5e-12, "Doob conservativity")
        pi = h * h
        check(abs(float(np.sum(pi)) - 1.0) < 3e-12, "Doob invariant normalization")
        check(float(np.max(np.abs(pi[:, None] * qh - (pi[:, None] * qh).T))) < 5e-12,
              "Doob detailed balance")
    return dimension, expected_probe_count


def check_evidence(data: dict, heavy: bool) -> None:
    top = {"schema", "candidate_id", "obstruction_id", "title", "evaluation_date", "source_commit",
           "fixed_epoch", "scope_literal", "evaluator_authority_sha256", "model", "theorem",
           "proof_certificates", "finite_spectral_atlas", "route_a", "scope_flags", "boundaries",
           "source_owner_tokens", "regression_summary", "payload_sha256"}
    check(set(data) == top, "top-level exact keys")
    check(data["schema"] == "hcs-c306-killed-noncolliding-walkers-evidence-v1", "schema")
    check(data["candidate_id"] == "HCS-C306", "candidate")
    check(data["obstruction_id"] == "HEN-O290", "obstruction")
    check(data["title"] == "Killed noncolliding walkers: determinant, spectrum, absorption, and Q-process", "title")
    check(data["evaluation_date"] == "2026-09-03", "date")
    check(data["source_commit"] == SOURCE, "source")
    check_int(data["fixed_epoch"], EPOCH, "epoch")
    check(data["scope_literal"] == SCOPE, "scope")
    check(data["evaluator_authority_sha256"] == EVALUATOR, "evaluator")
    check(exact_tree(data["model"], MODEL), "model exact tree")
    check(exact_tree(data["theorem"], THEOREM), "theorem exact tree")
    check(exact_tree(data["proof_certificates"], PROOF), "proof exact tree")
    check(exact_tree(data["scope_flags"], FLAGS), "scope flags")
    check(exact_tree(data["boundaries"], BOUNDARIES), "boundaries")
    check(exact_tree(data["source_owner_tokens"], SOURCES), "sources")
    route = data["route_a"]
    check(type(route) is dict and set(route) == {"tuple", "overall_verdict", "route_b_invocation_allowed", "obstruction"},
          "route exact keys")
    check(exact_tree(route["tuple"], TUPLE), "route tuple")
    check(route["overall_verdict"] == "ROUTE_A_REJECTED", "route verdict")
    check(type(route["route_b_invocation_allowed"]) is bool and route["route_b_invocation_allowed"] is False, "route B")
    check(route["obstruction"] == "the finite killed-walk semigroup has no target arithmetic local carrier, primitive-orbit Euler ledger, intrinsic prime clock, or target determinant; its self-adjoint generator is only a candidate-local A4 formal hint", "route obstruction")
    check(data["payload_sha256"] == payload_hash(data), "self hash")

    atlas = data["finite_spectral_atlas"]
    check(type(atlas) is dict and set(atlas) == {"L_min", "L_max", "case_count", "state_rows", "mode_rows", "probe_rows", "cases"}, "atlas keys")
    check_int(atlas["L_min"], 1, "L min")
    check_int(atlas["L_max"], 8, "L max")
    check_int(atlas["case_count"], 36, "case count")
    check(type(atlas["cases"]) is list and len(atlas["cases"]) == 36, "cases list")
    state_rows = probe_rows = 0
    cursor = 0
    for L in range(1, 9):
        for k in range(1, L + 1):
            dimension, probes = check_case(atlas["cases"][cursor], L, k, heavy)
            cursor += 1
            state_rows += dimension
            probe_rows += probes
    check_int(atlas["state_rows"], state_rows, "atlas state rows")
    check_int(atlas["mode_rows"], state_rows, "atlas mode rows")
    check_int(atlas["probe_rows"], probe_rows, "atlas probe rows")
    summary = data["regression_summary"]
    expected_summary = {"case_count": 36, "state_rows": state_rows, "mode_rows": state_rows,
                        "probe_rows": probe_rows, "L_cutoff": 8}
    check(exact_tree(summary, expected_summary), "summary exact tree")


EVAL_KEYS = {"schema", "candidate_id", "title", "evaluation_date", "source_commit", "fixed_epoch",
             "scope_literal", "evaluator_authority", "evaluator_version", "evaluator_authority_sha256",
             "obstruction_id", "candidate_definition", "family", "phase_space", "dynamics", "parameters",
             "parameter_provenance", "arithmetic_origin", "clock", "normalization", "determinant_convention",
             "orbit_cutoff", "precision", "training_data", "forbidden_data", "artifact_paths",
             "a0", "a1", "a2", "a3", "a4", "tuple", "overall_verdict", "route_b_invocation_allowed",
             "route_b_lock_reason", "scope_flags", "theorem_status", "finite_evidence_role", "source_owner_tokens"}


def check_evaluation(value: dict) -> None:
    check(set(value) == EVAL_KEYS, "evaluation exact keys")
    check(value["schema"] == "route-a-evaluation-v0.2.0", "evaluation schema")
    check(value["candidate_id"] == "HCS-C306" and value["obstruction_id"] == "HEN-O290", "evaluation ids")
    check(value["title"] == "Killed noncolliding walkers: determinant, spectrum, absorption, and Q-process", "evaluation title")
    check(value["evaluation_date"] == "2026-09-03" and value["source_commit"] == SOURCE, "evaluation provenance")
    check_int(value["fixed_epoch"], EPOCH, "evaluation epoch")
    check(value["scope_literal"] == SCOPE and value["evaluator_authority_sha256"] == EVALUATOR, "evaluation authority")
    check(value["evaluator_authority"] == "route-a-evaluator" and value["evaluator_version"] == "0.2.0", "evaluator version")
    check(type(value["artifact_paths"]) is list and value["artifact_paths"] == ["results/c306_walkers_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"], "artifacts")
    for index, key in enumerate(("a0", "a1", "a2", "a3", "a4")):
        lane = value[key]
        check(type(lane) is dict and set(lane) == {"verdict", "evidence_status", "strongest_evidence", "strongest_failure", "artifacts"}, key + " keys")
        expected_verdict = "A4_FORMAL_HINT" if index == 4 else f"A{index}_FAIL"
        check(lane["verdict"] == expected_verdict, key + " verdict")
        check(type(lane["artifacts"]) is list and len(lane["artifacts"]) >= 1 and all(type(x) is str for x in lane["artifacts"]), key + " artifacts")
        check(all(type(lane[x]) is str and lane[x] for x in ("evidence_status", "strongest_evidence", "strongest_failure")), key + " prose")
    check(exact_tree(value["tuple"], TUPLE), "evaluation tuple")
    check(value["overall_verdict"] == "ROUTE_A_REJECTED", "evaluation verdict")
    check(type(value["route_b_invocation_allowed"]) is bool and value["route_b_invocation_allowed"] is False, "evaluation route B")
    check(exact_tree(value["scope_flags"], FLAGS), "evaluation flags")
    check(value["theorem_status"] == "PROVABLE_AS_STATED", "theorem status")
    check(exact_tree(value["source_owner_tokens"], SOURCES), "evaluation sources")
    for key in EVAL_KEYS - {"fixed_epoch", "route_b_invocation_allowed", "scope_flags", "artifact_paths", "a0", "a1", "a2", "a3", "a4", "tuple", "source_owner_tokens"}:
        check(type(value[key]) is str and bool(value[key]), "evaluation scalar " + key)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    parser.add_argument("--yaml", type=Path, default=DEFAULT_YAML)
    parser.add_argument("--skip-heavy", action="store_true")
    args = parser.parse_args()
    evidence = strict_json(args.evidence)
    evaluation = strict_yaml(args.yaml)
    check_evidence(evidence, not args.skip_heavy)
    check_evaluation(evaluation)
    print(f"C306 independent checker PASS ({Count.value} explicit checks; producer import forbidden)")
    print(f"cases=36 states=502 probes={evidence['regression_summary']['probe_rows']} heavy={not args.skip_heavy}")


if __name__ == "__main__":
    main()
