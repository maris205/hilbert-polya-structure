#!/usr/bin/env python3
"""Canonical exact-evidence producer for HCS-C351."""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c351_jackson_evidence.json"
DEFAULT_YAML = ROOT / "evaluations/route_a/HCS-C351/2026-09-03.yaml"
SOURCE = "327fc1172cebcdeb17adfd2d8ad12636fbb94f52"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
YAML_RAW = "695c37ef6818eeeb056e9dfc638ebd720e8bf8df6cc96dec32ee2598a9628544"
YAML_SEMANTIC = "ba52d9d5a2cdd6ea1f74fbf44ddee836c5571e59e6b1796406439b3639d52fac"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"


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
            raise ValueError("YAML merge key forbidden")
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
            raise ValueError("YAML anchors and aliases forbidden")
    value = yaml.load(raw, Loader=StrictLoader)
    if type(value) is not dict:
        raise TypeError("YAML root")
    return value


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def f(value):
    return Fraction(value)


def fs(value):
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def matrix_product(left, right):
    rows, middle, columns = len(left), len(right), len(right[0])
    return [[sum((left[i][k] * right[k][j] for k in range(middle)), Fraction(0))
             for j in range(columns)] for i in range(rows)]


def routing_certificate(matrix):
    dimension = len(matrix)
    power = [[Fraction(int(i == j)) for j in range(dimension)] for i in range(dimension)]
    for exponent in range(1, 13):
        power = matrix_product(power, matrix)
        maximum = max(sum(row, Fraction(0)) for row in power)
        if maximum < 1:
            return exponent, maximum
    raise AssertionError("routing panel lacks a finite contraction certificate")


def solve_traffic(alpha, routing):
    """Gauss--Jordan solve of (I-P^T) lambda^T=alpha^T."""
    dimension = len(alpha)
    augmented = []
    for i in range(dimension):
        augmented.append([
            Fraction(int(i == j)) - routing[j][i] for j in range(dimension)
        ] + [alpha[i]])
    for column in range(dimension):
        pivot = next(row for row in range(column, dimension) if augmented[row][column])
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        divisor = augmented[column][column]
        augmented[column] = [entry / divisor for entry in augmented[column]]
        for row in range(dimension):
            if row == column:
                continue
            multiplier = augmented[row][column]
            augmented[row] = [a - multiplier * b
                              for a, b in zip(augmented[row], augmented[column])]
    return [augmented[i][-1] for i in range(dimension)]


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


def weight(state, loads):
    answer = Fraction(1)
    for exponent, load in zip(state, loads):
        answer *= load ** exponent
    return answer


def build_rows():
    network_rows, balance_rows, reverse_network_rows, reverse_jump_rows = [], [], [], []
    internal = []
    for network_id, (label, alpha, routing) in enumerate(panel_specs()):
        dimension = len(alpha)
        traffic = solve_traffic(alpha, routing)
        service = [traffic[i] + Fraction(i + 2, dimension + 2) for i in range(dimension)]
        loads = [traffic[i] / service[i] for i in range(dimension)]
        exits = [1 - sum(row, Fraction(0)) for row in routing]
        exponent, contraction = routing_certificate(routing)
        normalizer = Fraction(1)
        for load in loads:
            normalizer *= 1 - load
        row = {
            "network_id": network_id, "label": label, "dimension": dimension,
            "alpha": [fs(x) for x in alpha], "mu": [fs(x) for x in service],
            "routing": [[fs(x) for x in values] for values in routing],
            "exit_probabilities": [fs(x) for x in exits],
            "traffic": [fs(x) for x in traffic], "loads": [fs(x) for x in loads],
            "stability_margins": [fs(service[i] - traffic[i]) for i in range(dimension)],
            "normalizer": fs(normalizer),
            "routing_power_certificate": {"power": exponent,
                                           "maximum_row_sum": fs(contraction)},
        }
        network_rows.append(row)
        internal.append((label, alpha, routing, service, traffic, loads, exits))

        for state in itertools.product(range(4), repeat=dimension):
            mass = weight(state, loads)
            outgoing_rate = sum(alpha, Fraction(0))
            for i in range(dimension):
                if state[i] > 0:
                    outgoing_rate += service[i] * (1 - routing[i][i])
            incoming_mass_rate = Fraction(0)
            for i in range(dimension):
                if state[i] > 0:
                    predecessor = list(state)
                    predecessor[i] -= 1
                    incoming_mass_rate += weight(predecessor, loads) * alpha[i]
                predecessor = list(state)
                predecessor[i] += 1
                incoming_mass_rate += weight(predecessor, loads) * service[i] * exits[i]
            for i in range(dimension):
                for j in range(dimension):
                    if i == j or routing[i][j] == 0 or state[j] == 0:
                        continue
                    predecessor = list(state)
                    predecessor[i] += 1
                    predecessor[j] -= 1
                    incoming_mass_rate += (weight(predecessor, loads)
                                           * service[i] * routing[i][j])
            outgoing_mass_rate = mass * outgoing_rate
            balance_rows.append({
                "network_id": network_id, "state": list(state),
                "unnormalized_weight": fs(mass),
                "incoming_mass_rate": fs(incoming_mass_rate),
                "outgoing_mass_rate": fs(outgoing_mass_rate),
                "residual": fs(incoming_mass_rate - outgoing_mass_rate),
            })

        reverse_alpha = [traffic[i] * exits[i] for i in range(dimension)]
        reverse_routing = [[traffic[j] * routing[j][i] / traffic[i]
                            for j in range(dimension)] for i in range(dimension)]
        reverse_exits = [alpha[i] / traffic[i] for i in range(dimension)]
        reverse_row_sums = [sum(reverse_routing[i], Fraction(0)) + reverse_exits[i]
                            for i in range(dimension)]
        reverse_traffic_residual = [
            reverse_alpha[i]
            + sum((traffic[j] * reverse_routing[j][i] for j in range(dimension)), Fraction(0))
            - traffic[i] for i in range(dimension)
        ]
        reverse_network_rows.append({
            "network_id": network_id,
            "reverse_alpha": [fs(x) for x in reverse_alpha],
            "reverse_routing": [[fs(x) for x in values] for values in reverse_routing],
            "reverse_exit_probabilities": [fs(x) for x in reverse_exits],
            "augmented_row_sums": [fs(x) for x in reverse_row_sums],
            "reverse_traffic_residuals": [fs(x) for x in reverse_traffic_residual],
        })
        for i in range(dimension):
            reverse_rate = alpha[i] / loads[i]
            network_rate = service[i] * reverse_exits[i]
            reverse_jump_rows.append({
                "network_id": network_id, "kind": "external_arrival",
                "source": i, "destination": i,
                "forward_rate": fs(alpha[i]), "stationary_ratio": fs(loads[i]),
                "reverse_rate": fs(reverse_rate), "network_rate": fs(network_rate),
                "residual": fs(reverse_rate - network_rate),
            })
            reverse_rate = service[i] * exits[i] * loads[i]
            network_rate = reverse_alpha[i]
            reverse_jump_rows.append({
                "network_id": network_id, "kind": "external_departure",
                "source": i, "destination": i,
                "forward_rate": fs(service[i] * exits[i]),
                "stationary_ratio": fs(1 / loads[i]),
                "reverse_rate": fs(reverse_rate), "network_rate": fs(network_rate),
                "residual": fs(reverse_rate - network_rate),
            })
        for i in range(dimension):
            for j in range(dimension):
                if i == j or routing[i][j] == 0:
                    continue
                reverse_rate = service[i] * routing[i][j] * loads[i] / loads[j]
                network_rate = service[j] * reverse_routing[j][i]
                reverse_jump_rows.append({
                    "network_id": network_id, "kind": "internal_routing",
                    "source": i, "destination": j,
                    "forward_rate": fs(service[i] * routing[i][j]),
                    "stationary_ratio": fs(loads[j] / loads[i]),
                    "reverse_rate": fs(reverse_rate), "network_rate": fs(network_rate),
                    "residual": fs(reverse_rate - network_rate),
                })
    return network_rows, balance_rows, reverse_network_rows, reverse_jump_rows, internal


def digest(rows):
    return hashlib.sha256(canonical(rows)).hexdigest()


def build(evaluation_path):
    evaluation_raw = evaluation_path.read_bytes()
    evaluation = strict_yaml(evaluation_path)
    if hashlib.sha256(evaluation_raw).hexdigest() != YAML_RAW:
        raise AssertionError("evaluation raw hash")
    if hashlib.sha256(canonical(evaluation)).hexdigest() != YAML_SEMANTIC:
        raise AssertionError("evaluation semantic hash")
    networks, balances, reverse_networks, reverse_jumps, internal = build_rows()
    no_exit_index = next(i for i, row in enumerate(networks)
                         if row["label"] == "d3-no-direct-exit")
    independent_index = next(i for i, row in enumerate(networks)
                             if row["label"] == "d2-independent")
    tandem_index = next(i for i, row in enumerate(networks) if row["label"] == "d2-tandem")
    singleton = networks[0]
    critical_lambda = Fraction(networks[5]["traffic"][0])
    boundary_rows = [
        {"boundary": "single_node_mm1", "network_id": singleton["network_id"],
         "certificate": "lambda=alpha/(1-p_11) and rho=lambda/mu<1"},
        {"boundary": "zero_routing_independent_queues", "network_id": independent_index,
         "certificate": "P=0 and the product law separates into independent M/M/1 queues"},
        {"boundary": "feed_forward_tandem", "network_id": tandem_index,
         "certificate": "acyclic routing is included without changing the theorem"},
        {"boundary": "node_without_direct_exit", "network_id": no_exit_index,
         "certificate": "p_10=0 but a routing-power contraction still proves eventual exit"},
        {"boundary": "critical_load", "network_id": 5, "node": 0,
         "lambda": fs(critical_lambda), "mu": fs(critical_lambda),
         "classification": "not_positive_recurrent"},
        {"boundary": "overload", "network_id": 5, "node": 0,
         "lambda": fs(critical_lambda), "mu": fs(critical_lambda / 2),
         "classification": "not_positive_recurrent"},
    ]
    body = {
        "schema": "hcs-c351-open-jackson-evidence-v1",
        "candidate_id": "HCS-C351", "obstruction_id": "HEN-O335",
        "evaluation_date": "2026-09-03", "source_commit": SOURCE,
        "fixed_epoch": 1788393600, "scope_literal": SCOPE,
        "evaluator": {"authority": "flow_systems/skills/route-a-evaluator.md",
                      "version": "0.2.0", "sha256": EVALUATOR},
        "route_a_yaml": {
            "relative_path": "evaluations/route_a/HCS-C351/2026-09-03.yaml",
            "raw_sha256": YAML_RAW, "semantic_sha256": YAML_SEMANTIC},
        "model": {
            "node_set": "finite labelled nodes 0,...,d-1",
            "external_input": "independent Poisson streams with alpha_i>0",
            "service": "one exponential server of rate mu_i>0 at each node",
            "routing": "nonnegative substochastic P, including possible self-routing, with spectral radius below one",
            "state": "queue-length vector in nonnegative integer d-space",
            "traffic_convention": "row vector lambda=alpha+lambda P",
            "visible_generator": "self-routing completions are phantom events and do not change the queue-length state"},
        "theorem_contract": {
            "traffic": "lambda=alpha(I-P)^(-1) is the unique positive traffic vector",
            "stability": "positive recurrence holds exactly when lambda_i<mu_i at every node",
            "invariant_law": "unique product of geometric laws with load rho_i=lambda_i/mu_i",
            "time_reversal": "reverse network in the natural convention allowing zero exogenous rates has alpha_hat_i=lambda_i p_i0, p_hat_ji=lambda_i p_ij/lambda_j, and p_hat_i0=alpha_i/lambda_i",
            "external_departures": "stationary external departure streams are jointly independent Poisson and their past is independent of the current state; the proof identifies visible marked jumps only",
            "proof_owner": "analytic generator balance, the irreducible conservative CTMC invariant-probability lemma, stationary drift necessity, and visible-jump stationary time reversal"},
        "finite_panel": {
            "network_count": len(networks), "dimensions": [1, 2, 3, 4],
            "networks_per_dimension": 3, "state_coordinate_maximum": 3,
            "balance_row_count": len(balances),
            "reverse_network_row_count": len(reverse_networks),
            "reverse_jump_row_count": len(reverse_jumps),
            "boundary_row_count": len(boundary_rows)},
        "collision_boundary": {
            "C285": "closed fixed-population Gordon-Newell network, not open Poisson input or external departure history",
            "C233": "infinite-server immigration-death dynamics, not interacting single-server routing queues",
            "C342": "reinforced directed walk and Dirichlet environment, not an open queueing network"},
        "nonclaims": [
            "no joint-independence claim for all internal routed arc flows",
            "no theorem for multiclass, non-exponential, infinite-node, blocking, or state-dependent networks",
            "no target arithmetic local data or Euler-factor interpretation",
            "no root number, automorphy, target zero match, Hilbert-Polya operator, or Route B"],
        "references": [
            {"authors": "James R. Jackson", "year": 1957,
             "identifier": "DOI:10.1287/OPRE.5.4.518",
             "role": "primary open queueing-network product-form source"},
            {"authors": "Paul J. Burke", "year": 1956,
             "identifier": "DOI:10.1287/OPRE.4.6.699",
             "role": "primary M/M/1 output-process source"},
            {"authors": "F. P. Kelly", "year": 1975,
             "identifier": "DOI:10.2307/3212869",
             "role": "time-reversal and open-network lineage"},
            {"authors": "F. P. Kelly", "year": 1979,
             "identifier": "Cambridge-Statslab:Reversibility-and-Stochastic-Networks-1979",
             "role": "author-hosted authoritative reversibility and quasi-reversibility monograph"}],
        "route_a": {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
                    "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False},
        "scope_flags": {
            "claims_target_arithmetic_local_data": False,
            "claims_target_euler_factors": False, "claims_root_number": False,
            "claims_automorphy": False,
            "claims_target_divisor_or_counting_law": False,
            "claims_target_functional_equation": False,
            "claims_target_zero_match": False,
            "claims_hilbert_polya_operator": False, "invokes_route_b": False},
        "network_rows": networks, "balance_rows": balances,
        "reverse_network_rows": reverse_networks, "reverse_jump_rows": reverse_jumps,
        "boundary_rows": boundary_rows,
        "enumeration": {
            "all_arithmetic_exact": True, "floating_point_used": False,
            "finite_evidence_proves_infinite_theorem": False,
            "network_sha256": digest(networks), "balance_sha256": digest(balances),
            "reverse_network_sha256": digest(reverse_networks),
            "reverse_jump_sha256": digest(reverse_jumps),
            "boundary_sha256": digest(boundary_rows)},
    }
    body["payload_sha256"] = hashlib.sha256(canonical(body)).hexdigest()
    return body


def main():
    if sys.flags.optimize:
        raise RuntimeError("C351 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_YAML)
    args = parser.parse_args()
    result = build(args.evaluation)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(f"C351_PRODUCER_PASS networks={len(result['network_rows'])} "
          f"balances={len(result['balance_rows'])} reverse={len(result['reverse_jump_rows'])} "
          f"payload={result['payload_sha256']}")


if __name__ == "__main__":
    main()
