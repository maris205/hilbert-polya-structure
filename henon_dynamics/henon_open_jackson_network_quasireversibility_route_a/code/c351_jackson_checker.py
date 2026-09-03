#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C351."""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c351_jackson_evidence.json"
DEFAULT_YAML = ROOT / "evaluations/route_a/HCS-C351/2026-09-03.yaml"
SOURCE = "327fc1172cebcdeb17adfd2d8ad12636fbb94f52"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
YAML_RAW = "695c37ef6818eeeb056e9dfc638ebd720e8bf8df6cc96dec32ee2598a9628544"
YAML_SEMANTIC = "ba52d9d5a2cdd6ea1f74fbf44ddee836c5571e59e6b1796406439b3639d52fac"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
ASSERTIONS = 0
FLAGS = {
    "claims_target_arithmetic_local_data": False,
    "claims_target_euler_factors": False, "claims_root_number": False,
    "claims_automorphy": False, "claims_target_divisor_or_counting_law": False,
    "claims_target_functional_equation": False, "claims_target_zero_match": False,
    "claims_hilbert_polya_operator": False, "invokes_route_b": False,
}


def duplicate_pairs(items):
    answer = {}
    for key, value in items:
        if key in answer:
            raise ValueError("duplicate JSON key")
        answer[key] = value
    return answer


def strict_json(path):
    value = json.loads(path.read_text(), object_pairs_hook=duplicate_pairs,
                       parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)))
    if type(value) is not dict:
        raise TypeError("JSON root")
    return value


class StrictLoader(yaml.SafeLoader):
    pass


StrictLoader.yaml_implicit_resolvers = {
    key: [(tag, rx) for tag, rx in values if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def strict_mapping(loader, node, deep=False):
    answer = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in answer:
            raise ValueError("duplicate/non-string YAML key")
        answer[key] = loader.construct_object(value_node, deep=deep)
    return answer


StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, strict_mapping)


def strict_yaml(path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML anchor or alias forbidden")
    value = yaml.load(raw, Loader=StrictLoader)
    if type(value) is not dict:
        raise TypeError("YAML root")
    return value


def need(condition, label):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def exact_keys(value, keys, label):
    need(type(value) is dict and set(value) == set(keys), f"{label} keys")


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def f(value):
    return Fraction(value)


def fs(value):
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def determinant(matrix):
    dimension = len(matrix)
    answer = Fraction(0)
    for permutation in itertools.permutations(range(dimension)):
        inversions = sum(permutation[i] > permutation[j]
                         for i in range(dimension) for j in range(i + 1, dimension))
        term = Fraction(-1 if inversions % 2 else 1)
        for i in range(dimension):
            term *= matrix[i][permutation[i]]
        answer += term
    return answer


def solve_traffic(alpha, routing):
    """Cramer's rule, deliberately independent of producer Gauss--Jordan."""
    dimension = len(alpha)
    coefficient = [[Fraction(int(i == j)) - routing[j][i]
                    for j in range(dimension)] for i in range(dimension)]
    denominator = determinant(coefficient)
    need(denominator != 0, "traffic determinant")
    answer = []
    for column in range(dimension):
        replaced = [row[:] for row in coefficient]
        for row in range(dimension):
            replaced[row][column] = alpha[row]
        answer.append(determinant(replaced) / denominator)
    return answer


def matrix_product(left, right):
    return [[sum((left[i][k] * right[k][j] for k in range(len(right))), Fraction(0))
             for j in range(len(right[0]))] for i in range(len(left))]


def routing_certificate(matrix):
    dimension = len(matrix)
    current = [[Fraction(int(i == j)) for j in range(dimension)] for i in range(dimension)]
    for power in range(1, 13):
        current = matrix_product(current, matrix)
        bound = max(sum(row, Fraction(0)) for row in current)
        if bound < 1:
            return power, bound
    raise AssertionError("routing contraction not found")


def panel_specs():
    z = Fraction(0)
    return [
        ("d1-open", [f(1)], [[z]]),
        ("d1-feedback", [f(1)], [[f("1/3")]]),
        ("d1-heavy-feedback", [f(2)], [[f("2/3")]]),
        ("d2-independent", [f("1/3"), f("2/3")], [[z, z], [z, z]]),
        ("d2-tandem", [f(1), f("1/2")], [[z, f("1/2")], [z, z]]),
        ("d2-cycle-self", [f("1/2"), f("3/4")],
         [[f("1/5"), f("2/5")], [f("1/3"), f("1/6")]]),
        ("d3-no-direct-exit", [f("1/3"), f("1/2"), f("2/3")],
         [[z, f(1), z], [z, z, f("1/2")], [z, z, z]]),
        ("d3-cycle", [f("1/4"), f("1/2"), f("3/4")],
         [[z, f("1/3"), z], [z, z, f("1/2")], [f("1/4"), z, z]]),
        ("d3-mixed-self", [f("2/5"), f("3/5"), f("4/5")],
         [[f("1/6"), f("1/4"), z], [z, f("1/5"), f("1/3")],
          [f("1/7"), z, f("1/8")]]),
        ("d4-chain-no-direct-exit", [f("1/5"), f("2/5"), f("3/5"), f("4/5")],
         [[z, f(1), z, z], [z, z, f("2/3"), z],
          [z, z, z, f("1/2")], [z, z, z, z]]),
        ("d4-ring", [f("1/3"), f("1/2"), f("2/3"), f("5/6")],
         [[z, f("1/2"), z, z], [z, z, f("1/3"), z],
          [z, z, z, f("1/4")], [f("1/5"), z, z, z]]),
        ("d4-mixed-self", [f("2/7"), f("3/7"), f("4/7"), f("5/7")],
         [[f("1/10"), f("1/5"), z, f("1/10")],
          [z, f("1/8"), f("1/4"), z],
          [f("1/7"), z, f("1/9"), f("2/9")],
          [z, f("1/6"), z, f("1/12")]]),
    ]


def product_weight(state, loads):
    return math.prod((loads[i] ** state[i] for i in range(len(state))), start=Fraction(1))


def expected_rows():
    networks, balances, reversed_networks, reversed_jumps = [], [], [], []
    for network_id, (label, alpha, routing) in enumerate(panel_specs()):
        dimension = len(alpha)
        traffic = solve_traffic(alpha, routing)
        service = [traffic[i] + Fraction(i + 2, dimension + 2) for i in range(dimension)]
        loads = [traffic[i] / service[i] for i in range(dimension)]
        exits = [1 - sum(routing[i], Fraction(0)) for i in range(dimension)]
        power, bound = routing_certificate(routing)
        networks.append({
            "network_id": network_id, "label": label, "dimension": dimension,
            "alpha": [fs(x) for x in alpha], "mu": [fs(x) for x in service],
            "routing": [[fs(x) for x in row] for row in routing],
            "exit_probabilities": [fs(x) for x in exits],
            "traffic": [fs(x) for x in traffic], "loads": [fs(x) for x in loads],
            "stability_margins": [fs(service[i] - traffic[i]) for i in range(dimension)],
            "normalizer": fs(math.prod((1 - x for x in loads), start=Fraction(1))),
            "routing_power_certificate": {"power": power, "maximum_row_sum": fs(bound)},
        })
        for state in itertools.product(range(4), repeat=dimension):
            base_weight = product_weight(state, loads)
            outgoing = sum(alpha, Fraction(0)) + sum(
                (service[i] * (1 - routing[i][i]) for i in range(dimension) if state[i]),
                Fraction(0))
            incoming = Fraction(0)
            for i in range(dimension):
                if state[i]:
                    before = list(state)
                    before[i] -= 1
                    incoming += product_weight(before, loads) * alpha[i]
                before = list(state)
                before[i] += 1
                incoming += product_weight(before, loads) * service[i] * exits[i]
            for source in range(dimension):
                for destination in range(dimension):
                    if source == destination or not routing[source][destination] or not state[destination]:
                        continue
                    before = list(state)
                    before[source] += 1
                    before[destination] -= 1
                    incoming += (product_weight(before, loads) * service[source]
                                 * routing[source][destination])
            outgoing_mass = base_weight * outgoing
            balances.append({
                "network_id": network_id, "state": list(state),
                "unnormalized_weight": fs(base_weight),
                "incoming_mass_rate": fs(incoming),
                "outgoing_mass_rate": fs(outgoing_mass),
                "residual": fs(incoming - outgoing_mass),
            })
        reverse_alpha = [traffic[i] * exits[i] for i in range(dimension)]
        reverse_routing = [[traffic[j] * routing[j][i] / traffic[i]
                            for j in range(dimension)] for i in range(dimension)]
        reverse_exits = [alpha[i] / traffic[i] for i in range(dimension)]
        reversed_networks.append({
            "network_id": network_id,
            "reverse_alpha": [fs(x) for x in reverse_alpha],
            "reverse_routing": [[fs(x) for x in row] for row in reverse_routing],
            "reverse_exit_probabilities": [fs(x) for x in reverse_exits],
            "augmented_row_sums": [fs(sum(reverse_routing[i], Fraction(0)) + reverse_exits[i])
                                   for i in range(dimension)],
            "reverse_traffic_residuals": [fs(reverse_alpha[i] + sum(
                (traffic[j] * reverse_routing[j][i] for j in range(dimension)), Fraction(0))
                - traffic[i]) for i in range(dimension)],
        })
        for i in range(dimension):
            reversed_jumps.append({
                "network_id": network_id, "kind": "external_arrival",
                "source": i, "destination": i, "forward_rate": fs(alpha[i]),
                "stationary_ratio": fs(loads[i]), "reverse_rate": fs(alpha[i] / loads[i]),
                "network_rate": fs(service[i] * reverse_exits[i]), "residual": "0"})
            reversed_jumps.append({
                "network_id": network_id, "kind": "external_departure",
                "source": i, "destination": i,
                "forward_rate": fs(service[i] * exits[i]),
                "stationary_ratio": fs(1 / loads[i]),
                "reverse_rate": fs(service[i] * exits[i] * loads[i]),
                "network_rate": fs(reverse_alpha[i]), "residual": "0"})
        for i in range(dimension):
            for j in range(dimension):
                if i != j and routing[i][j]:
                    value = service[i] * routing[i][j] * loads[i] / loads[j]
                    reversed_jumps.append({
                        "network_id": network_id, "kind": "internal_routing",
                        "source": i, "destination": j,
                        "forward_rate": fs(service[i] * routing[i][j]),
                        "stationary_ratio": fs(loads[j] / loads[i]),
                        "reverse_rate": fs(value),
                        "network_rate": fs(service[j] * reverse_routing[j][i]),
                        "residual": "0"})
    critical = Fraction(networks[5]["traffic"][0])
    boundaries = [
        {"boundary": "single_node_mm1", "network_id": 0,
         "certificate": "lambda=alpha/(1-p_11) and rho=lambda/mu<1"},
        {"boundary": "zero_routing_independent_queues", "network_id": 3,
         "certificate": "P=0 and the product law separates into independent M/M/1 queues"},
        {"boundary": "feed_forward_tandem", "network_id": 4,
         "certificate": "acyclic routing is included without changing the theorem"},
        {"boundary": "node_without_direct_exit", "network_id": 6,
         "certificate": "p_10=0 but a routing-power contraction still proves eventual exit"},
        {"boundary": "critical_load", "network_id": 5, "node": 0,
         "lambda": fs(critical), "mu": fs(critical),
         "classification": "not_positive_recurrent"},
        {"boundary": "overload", "network_id": 5, "node": 0,
         "lambda": fs(critical), "mu": fs(critical / 2),
         "classification": "not_positive_recurrent"},
    ]
    return networks, balances, reversed_networks, reversed_jumps, boundaries


def row_digest(rows):
    return hashlib.sha256(canonical(rows)).hexdigest()


def check_yaml(value):
    keys = ["schema", "candidate_id", "title", "evaluation_date", "source_commit",
        "fixed_epoch", "scope_literal", "evaluator_authority", "evaluator_version",
        "evaluator_authority_sha256", "obstruction_id", "candidate_definition", "family",
        "phase_space", "dynamics", "parameters", "parameter_provenance", "arithmetic_origin",
        "clock", "normalization", "determinant_convention", "orbit_cutoff", "precision",
        "training_data", "forbidden_data", "artifact_paths", "a0", "a1", "a2", "a3",
        "a4", "tuple", "overall_verdict", "route_b_invocation_allowed",
        "route_b_lock_reason", "scope_flags", "theorem_status", "finite_evidence_role",
        "source_owner_tokens"]
    exact_keys(value, keys, "YAML top")
    expected_scalars = {
        "schema": "route-a-evaluation-v0.2.0", "candidate_id": "HCS-C351",
        "title": "Open Jackson M/M/1 networks, time reversal, and external quasi-reversibility",
        "evaluation_date": "2026-09-03", "source_commit": SOURCE,
        "fixed_epoch": 1788393600, "scope_literal": SCOPE,
        "evaluator_authority": "flow_systems/skills/route-a-evaluator.md",
        "evaluator_version": "0.2.0", "evaluator_authority_sha256": EVALUATOR,
        "obstruction_id": "HEN-O335",
        "candidate_definition": "finite open single-class Jackson network with one exponential server per node, positive external Poisson input, and a substochastic routing matrix of spectral radius below one",
        "family": "continuous-time Markov queueing networks and quasi-reversible stochastic flows",
        "phase_space": "nonnegative integer queue-length vectors on a finite labelled node set",
        "dynamics": "independent external Poisson arrivals and exponential service completions followed by routing or external departure",
        "parameters": "positive external rates and service rates together with a nonnegative substochastic routing matrix whose spectral radius is below one",
        "parameter_provenance": "source queueing parameters only, never target-fitted",
        "arithmetic_origin": "none", "clock": "physical continuous time in the source Markov network",
        "normalization": "row-vector traffic equation lambda equals alpha plus lambda P; rho_i equals lambda_i divided by mu_i",
        "determinant_convention": "none; traffic inverses and product normalizers are source queueing objects",
        "orbit_cutoff": "none; the infinite-state theorem is analytic and finite rational networks are receipt-only",
        "precision": "exact rational traffic solutions, balance identities, reversed rates, and boundary loads",
        "training_data": "none",
        "forbidden_data": "target arithmetic local data, Euler factors, root numbers, automorphy, target divisor or functional equation, target zeros, Hilbert-Polya operators, Route B",
        "overall_verdict": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False,
        "route_b_lock_reason": "all Route-A arithmetic, primitive-orbit, determinant, analytic, and operator gates fail",
        "theorem_status": "PROVABLE_AS_STATED",
        "finite_evidence_role": "convention and implementation receipt, not proof of the infinite-state network theorem",
    }
    for key, expected in expected_scalars.items():
        need(value[key] == expected, f"YAML literal {key}")
    need(value["artifact_paths"] == ["results/c351_jackson_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"], "YAML artifacts")
    expected_verdicts = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"]
    statuses = ["PROVED", "PROVED", "STOP_SCOPED", "STOP_SCOPED", "STOP_SCOPED"]
    branches = {
        "a0": ("the traffic solution and stationary flows are intrinsic exact source queueing quantities", "no rational-prime carrier, prime-power repetition, logarithmic prime clock, or arithmetic weight exists"),
        "a1": ("every transition and its stationary reverse have an intrinsic Markov interpretation", "Poisson arrivals and service events are stochastic jumps rather than isolated deterministic primitive periodic orbits"),
        "a2": ("the product-form normalizer and traffic inverse are exact source formulas", "neither object is a primitive-orbit zeta function or target Fredholm determinant"),
        "a3": ("stability, reversal, and the external departure law are analytically complete", "the queueing identities provide no target continuation, divisor, functional equation, counting law, or Weil compression"),
        "a4": ("the network has a well-defined Markov semigroup and stationary adjoint", "no same-clock natural self-adjoint target realization, unitary dynamics, scattering system, or Hilbert-Polya operator is constructed"),
    }
    for index, branch in enumerate(("a0", "a1", "a2", "a3", "a4")):
        exact_keys(value[branch], ["verdict", "evidence_status", "strongest_evidence", "strongest_failure"], f"YAML {branch}")
        need(value[branch] == {"verdict": expected_verdicts[index], "evidence_status": statuses[index],
             "strongest_evidence": branches[branch][0], "strongest_failure": branches[branch][1]}, f"YAML {branch}")
    need(value["tuple"] == expected_verdicts, "YAML tuple")
    need(value["scope_flags"] == FLAGS, "YAML flags")
    need(value["source_owner_tokens"] == ["DOI:10.1287/OPRE.5.4.518", "DOI:10.1287/OPRE.4.6.699", "DOI:10.2307/3212869", "Cambridge-Statslab:Reversibility-and-Stochastic-Networks-1979"], "YAML sources")


def compare_rows(actual, expected, label):
    need(type(actual) is list and len(actual) == len(expected), f"{label} length")
    for index, row in enumerate(expected):
        need(actual[index] == row, f"{label} row {index}")


def main():
    if sys.flags.optimize:
        raise RuntimeError("C351 checker refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_YAML)
    args = parser.parse_args()
    data = strict_json(args.evidence)
    raw_yaml = args.evaluation.read_bytes()
    evaluation = strict_yaml(args.evaluation)
    need(hashlib.sha256(raw_yaml).hexdigest() == YAML_RAW, "YAML raw digest")
    need(hashlib.sha256(canonical(evaluation)).hexdigest() == YAML_SEMANTIC, "YAML semantic digest")
    check_yaml(evaluation)
    exact_keys(data, ["schema", "candidate_id", "obstruction_id", "evaluation_date",
        "source_commit", "fixed_epoch", "scope_literal", "evaluator", "route_a_yaml",
        "model", "theorem_contract", "finite_panel", "collision_boundary", "nonclaims",
        "references", "route_a", "scope_flags", "network_rows", "balance_rows",
        "reverse_network_rows", "reverse_jump_rows", "boundary_rows", "enumeration",
        "payload_sha256"], "evidence top")
    body = dict(data)
    claimed = body.pop("payload_sha256")
    need(type(claimed) is str and claimed == hashlib.sha256(canonical(body)).hexdigest(), "payload hash")
    need(data["schema"] == "hcs-c351-open-jackson-evidence-v1", "schema")
    need(data["candidate_id"] == "HCS-C351" and data["obstruction_id"] == "HEN-O335", "ids")
    need(data["evaluation_date"] == "2026-09-03" and data["source_commit"] == SOURCE, "source")
    need(data["fixed_epoch"] == 1788393600 and data["scope_literal"] == SCOPE, "scope")
    need(data["evaluator"] == {"authority": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR}, "evaluator")
    need(data["route_a_yaml"] == {"relative_path": "evaluations/route_a/HCS-C351/2026-09-03.yaml", "raw_sha256": YAML_RAW, "semantic_sha256": YAML_SEMANTIC}, "YAML binding")
    need(data["model"] == {"node_set": "finite labelled nodes 0,...,d-1", "external_input": "independent Poisson streams with alpha_i>0", "service": "one exponential server of rate mu_i>0 at each node", "routing": "nonnegative substochastic P, including possible self-routing, with spectral radius below one", "state": "queue-length vector in nonnegative integer d-space", "traffic_convention": "row vector lambda=alpha+lambda P", "visible_generator": "self-routing completions are phantom events and do not change the queue-length state"}, "model")
    need(data["theorem_contract"] == {"traffic": "lambda=alpha(I-P)^(-1) is the unique positive traffic vector", "stability": "positive recurrence holds exactly when lambda_i<mu_i at every node", "invariant_law": "unique product of geometric laws with load rho_i=lambda_i/mu_i", "time_reversal": "reverse network in the natural convention allowing zero exogenous rates has alpha_hat_i=lambda_i p_i0, p_hat_ji=lambda_i p_ij/lambda_j, and p_hat_i0=alpha_i/lambda_i", "external_departures": "stationary external departure streams are jointly independent Poisson and their past is independent of the current state; the proof identifies visible marked jumps only", "proof_owner": "analytic generator balance, the irreducible conservative CTMC invariant-probability lemma, stationary drift necessity, and visible-jump stationary time reversal"}, "contract")
    need(data["collision_boundary"] == {"C285": "closed fixed-population Gordon-Newell network, not open Poisson input or external departure history", "C233": "infinite-server immigration-death dynamics, not interacting single-server routing queues", "C342": "reinforced directed walk and Dirichlet environment, not an open queueing network"}, "collision")
    need(data["nonclaims"] == ["no joint-independence claim for all internal routed arc flows", "no theorem for multiclass, non-exponential, infinite-node, blocking, or state-dependent networks", "no target arithmetic local data or Euler-factor interpretation", "no root number, automorphy, target zero match, Hilbert-Polya operator, or Route B"], "nonclaims")
    need(data["references"] == [{"authors": "James R. Jackson", "year": 1957, "identifier": "DOI:10.1287/OPRE.5.4.518", "role": "primary open queueing-network product-form source"}, {"authors": "Paul J. Burke", "year": 1956, "identifier": "DOI:10.1287/OPRE.4.6.699", "role": "primary M/M/1 output-process source"}, {"authors": "F. P. Kelly", "year": 1975, "identifier": "DOI:10.2307/3212869", "role": "time-reversal and open-network lineage"}, {"authors": "F. P. Kelly", "year": 1979, "identifier": "Cambridge-Statslab:Reversibility-and-Stochastic-Networks-1979", "role": "author-hosted authoritative reversibility and quasi-reversibility monograph"}], "references")
    need(data["route_a"] == {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"], "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}, "Route A")
    need(data["scope_flags"] == FLAGS, "flags")
    networks, balances, reversed_networks, reversed_jumps, boundaries = expected_rows()
    compare_rows(data["network_rows"], networks, "networks")
    compare_rows(data["balance_rows"], balances, "balances")
    compare_rows(data["reverse_network_rows"], reversed_networks, "reverse networks")
    compare_rows(data["reverse_jump_rows"], reversed_jumps, "reverse jumps")
    compare_rows(data["boundary_rows"], boundaries, "boundaries")
    need(data["finite_panel"] == {"network_count": 12, "dimensions": [1, 2, 3, 4], "networks_per_dimension": 3, "state_coordinate_maximum": 3, "balance_row_count": 1020, "reverse_network_row_count": 12, "reverse_jump_row_count": len(reversed_jumps), "boundary_row_count": 6}, "finite panel")
    need(data["enumeration"] == {"all_arithmetic_exact": True, "floating_point_used": False, "finite_evidence_proves_infinite_theorem": False, "network_sha256": row_digest(networks), "balance_sha256": row_digest(balances), "reverse_network_sha256": row_digest(reversed_networks), "reverse_jump_sha256": row_digest(reversed_jumps), "boundary_sha256": row_digest(boundaries)}, "enumeration")
    checked_rows = sum(map(len, (networks, balances, reversed_networks, reversed_jumps, boundaries)))
    print(f"C351 independent Jackson checker: PASS assertions={ASSERTIONS} rows={checked_rows} "
          f"networks={len(networks)} balances={len(balances)} reverse={len(reversed_jumps)}")


if __name__ == "__main__":
    main()
